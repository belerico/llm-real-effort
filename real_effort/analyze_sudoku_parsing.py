"""Analyze sudoku puzzle parsing errors from experiment results.

Given that the original board (`text`) is NOT stored in experiment.json,
we extract the board the model "saw" from its `reasoning_content`, then:

1. Count blanks vs expected solution length (mismatch = parsing error)
2. Fill the model's blanks with the known solution → check sudoku validity
   (invalid = the model misread given numbers)
3. Fill the model's blanks with its response → check sudoku validity
   (helps distinguish parsing errors from solving errors)

Usage:
    # From experiment.json:
    python analyze_sudoku_parsing.py real_effort/reports/t0-control
    python analyze_sudoku_parsing.py real_effort/reports/t0-control --model claude-opus-4.6

    # From results.db (all experiments at once):
    python analyze_sudoku_parsing.py real_effort/reports/results_orig.db
    python analyze_sudoku_parsing.py real_effort/reports/results_orig.db --treatment t0-control
    python analyze_sudoku_parsing.py real_effort/reports/results_orig.db --model claude-opus-4.6 --only-failures
"""

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path


GRID_SIZE = 6
BOX_ROWS = 2
BOX_COLS = 3


@dataclass
class ParsingResult:
    model: str
    puzzle_idx: int
    is_correct: bool
    board_extracted: bool
    parsed_board: list | None  # 6x6, None for blanks
    blank_count: int | None
    expected_blank_count: int
    blank_count_match: bool | None
    board_with_solution_valid: bool | None  # blanks filled with solution → valid?
    board_with_response_valid: bool | None  # blanks filled with response → valid?
    solution_violations: list | None  # which constraints are violated
    response_violations: list | None
    error_type: str  # "correct", "solving_error", "parsing_error", "no_reasoning", "parse_failed", "no_response"
    detail: str


def parse_board_from_reasoning(reasoning: str) -> list | None:
    """Extract a 6x6 board from reasoning_content.

    Models typically describe the board in formats like:
      Row 1: 1, _, 4, 2, _, _
      Row 1: 1 _ 4 2 _ _
      _ 5 3 | 6 _ _
      . 5 3 6 . .

    Returns 6x6 list (int or None for blanks), or None if extraction fails.
    """
    if not reasoning:
        return None

    # Strategy: find 6 consecutive lines that each contain exactly 6 cell values
    lines = reasoning.strip().split("\n")
    board_lines = []

    for line in lines:
        row = _try_parse_row(line)
        if row is not None and len(row) == GRID_SIZE:
            board_lines.append(row)
            if len(board_lines) == GRID_SIZE:
                return board_lines
        else:
            # Reset if we hit a non-board line after starting
            if board_lines:
                # Allow separator lines (e.g., "------+------")
                if re.match(r"^[\s\-\+]+$", line):
                    continue
                # Allow empty lines between rows
                if line.strip() == "":
                    continue
                # Otherwise reset
                board_lines = []

    # If we got some but not 6 rows, return None
    return None


def _try_parse_row(line: str) -> list | None:
    """Try to parse a single row from a line.

    Handles formats:
      "Row 1: 1, _, 4, 2, _, _"
      "Row 1: 1 _ 4 2 _ _"
      "_ 5 3 | 6 _ _"
      ". 5 3 6 . ."
      "1 _ 4 | 2 _ _"
      "| 1 _ 4 | 2 _ _ |"
      "- Row 1 is [3, 4, 2, ., ., .]"   (gpt-5 style)
    """
    line = line.strip()

    # Strip leading bullet/dash
    line = re.sub(r"^[-*•]\s*", "", line)

    # Strip "Row N:" or "Row N is" prefix
    line = re.sub(r"^Row\s*\d+\s*(?:is\s*|:\s*)", "", line, flags=re.IGNORECASE)

    # Remove brackets
    line = line.strip("[]")

    # Remove pipe separators and surrounding whitespace
    line = line.replace("|", " ")

    # Remove backticks (from markdown code blocks)
    line = line.replace("`", "")

    # Remove leading/trailing pipes or brackets
    line = line.strip("| ")

    # Split by comma+space or just spaces
    if "," in line:
        tokens = [t.strip() for t in line.split(",")]
    else:
        tokens = line.split()

    # Filter empty tokens
    tokens = [t for t in tokens if t]

    if len(tokens) != GRID_SIZE:
        return None

    row = []
    for t in tokens:
        t = t.strip()
        if t in ("_", ".", "?", "*", "x", "X", "□", "▢"):
            row.append(None)
        elif t.isdigit() and 1 <= int(t) <= GRID_SIZE:
            row.append(int(t))
        else:
            return None  # not a valid cell

    return row


def check_sudoku_validity(board: list) -> list:
    """Check if a filled 6x6 board is valid. Returns list of violation descriptions."""
    violations = []

    # Check rows
    for r in range(GRID_SIZE):
        vals = [board[r][c] for c in range(GRID_SIZE) if board[r][c] is not None]
        dupes = [v for v in set(vals) if vals.count(v) > 1]
        if dupes:
            violations.append(f"Row {r+1} has duplicates: {dupes}")
        missing = set(range(1, GRID_SIZE + 1)) - set(vals)
        if missing and len(vals) == GRID_SIZE:
            violations.append(f"Row {r+1} missing: {missing}")

    # Check columns
    for c in range(GRID_SIZE):
        vals = [board[r][c] for r in range(GRID_SIZE) if board[r][c] is not None]
        dupes = [v for v in set(vals) if vals.count(v) > 1]
        if dupes:
            violations.append(f"Col {c+1} has duplicates: {dupes}")

    # Check boxes
    for box_r in range(GRID_SIZE // BOX_ROWS):
        for box_c in range(GRID_SIZE // BOX_COLS):
            vals = []
            for r in range(box_r * BOX_ROWS, (box_r + 1) * BOX_ROWS):
                for c in range(box_c * BOX_COLS, (box_c + 1) * BOX_COLS):
                    if board[r][c] is not None:
                        vals.append(board[r][c])
            dupes = [v for v in set(vals) if vals.count(v) > 1]
            if dupes:
                violations.append(f"Box ({box_r+1},{box_c+1}) has duplicates: {dupes}")

    return violations


def fill_blanks(board: list, values: list) -> list | None:
    """Fill None cells with values in reading order. Returns new board or None if count mismatch."""
    filled = [row[:] for row in board]
    vi = 0
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if filled[r][c] is None:
                if vi >= len(values):
                    return None
                filled[r][c] = values[vi]
                vi += 1
    if vi != len(values):
        return None
    return filled


def parse_values(s: str) -> list:
    """Parse space-separated integers from a solution/response string."""
    if not s or not s.strip():
        return []
    tokens = s.strip().split()
    result = []
    for t in tokens:
        try:
            result.append(int(t))
        except ValueError:
            pass  # skip non-numeric tokens
    return result


def analyze_puzzle(model: str, puzzle: dict) -> ParsingResult:
    """Analyze a single puzzle attempt."""
    solution_vals = parse_values(puzzle.get("solution", ""))
    response_vals = parse_values(puzzle.get("response", ""))
    reasoning = puzzle.get("reasoning_content") or ""
    is_correct = puzzle.get("is_correct", False)
    idx = puzzle.get("iteration", 0)

    if not reasoning:
        return ParsingResult(
            model=model,
            puzzle_idx=idx,
            is_correct=is_correct,
            board_extracted=False,
            parsed_board=None,
            blank_count=None,
            expected_blank_count=len(solution_vals),
            blank_count_match=None,
            board_with_solution_valid=None,
            board_with_response_valid=None,
            solution_violations=None,
            response_violations=None,
            error_type="correct" if is_correct else "no_reasoning",
            detail="No reasoning content available",
        )

    board = parse_board_from_reasoning(reasoning)
    if board is None:
        return ParsingResult(
            model=model,
            puzzle_idx=idx,
            is_correct=is_correct,
            board_extracted=False,
            parsed_board=None,
            blank_count=None,
            expected_blank_count=len(solution_vals),
            blank_count_match=None,
            board_with_solution_valid=None,
            board_with_response_valid=None,
            solution_violations=None,
            response_violations=None,
            error_type="correct" if is_correct else "parse_failed",
            detail="Could not extract board from reasoning",
        )

    # Count blanks
    blank_count = sum(1 for r in board for c in r if c is None)
    blank_match = blank_count == len(solution_vals)

    # Fill with solution
    sol_board = fill_blanks(board, solution_vals)
    sol_violations = (
        check_sudoku_validity(sol_board) if sol_board else ["blank count mismatch"]
    )
    sol_valid = sol_board is not None and len(sol_violations) == 0

    # Fill with response
    if not response_vals:
        resp_board = None
        resp_violations = None
        resp_valid = None
    else:
        resp_board = fill_blanks(board, response_vals)
        resp_violations = (
            check_sudoku_validity(resp_board)
            if resp_board
            else ["blank count mismatch"]
        )
        resp_valid = resp_board is not None and len(resp_violations) == 0

    # Classify error type
    if is_correct:
        error_type = "correct"
        detail = "Correct answer"
    elif not blank_match:
        error_type = "parsing_error"
        detail = f"Blank count mismatch: model saw {blank_count}, expected {len(solution_vals)}"
    elif not sol_valid:
        error_type = "parsing_error"
        detail = f"Board + correct solution is invalid: {sol_violations}"
    elif not response_vals:
        error_type = "no_response"
        detail = "Board parsed correctly but model returned empty response"
    elif resp_valid is False:
        error_type = "solving_error"
        detail = "Board parsed correctly but solution attempt is invalid"
    else:
        # Board parsed correctly, response is valid sudoku but doesn't match expected
        # This shouldn't happen for a valid puzzle, but just in case
        error_type = "solving_error"
        detail = "Board parsed correctly, response differs from expected solution"

    return ParsingResult(
        model=model,
        puzzle_idx=idx,
        is_correct=is_correct,
        board_extracted=True,
        parsed_board=board,
        blank_count=blank_count,
        expected_blank_count=len(solution_vals),
        blank_count_match=blank_match,
        board_with_solution_valid=sol_valid,
        board_with_response_valid=resp_valid,
        solution_violations=sol_violations,
        response_violations=resp_violations,
        error_type=error_type,
        detail=detail,
    )


def format_board(board: list) -> str:
    """Pretty-print a 6x6 board."""
    lines = []
    for r in range(GRID_SIZE):
        cells = []
        for c in range(GRID_SIZE):
            v = board[r][c]
            cells.append(str(v) if v is not None else "_")
            if c == BOX_COLS - 1 and c < GRID_SIZE - 1:
                cells.append("|")
        lines.append(" ".join(cells))
        if (r + 1) % BOX_ROWS == 0 and r < GRID_SIZE - 1:
            lines.append("------+------")
    return "\n".join(lines)


def load_from_json(exp_dir: Path, model_filter: str | None = None) -> list:
    """Load puzzles from experiment.json."""
    exp_path = exp_dir / "experiment.json"
    if not exp_path.exists():
        print(f"Error: {exp_path} not found", file=sys.stderr)
        sys.exit(1)

    with open(exp_path) as f:
        data = json.load(f)

    results = []
    for run in data["runs"]:
        if run["game"] != "sudoku_game":
            continue
        model = run["model"]
        if model_filter and model_filter not in model:
            continue
        for puzzle in run.get("puzzles", []):
            result = analyze_puzzle(model, puzzle)
            results.append(result)
    return results


def load_from_db(
    db_path: Path,
    model_filter: str | None = None,
    treatment: str | None = None,
    is_text: bool | None = None,
) -> list:
    """Load puzzles from results.db."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """
        SELECT r.model, e.name as experiment, r.is_text,
               p.iteration, p.solution, p.response, p.reasoning_content,
               p.reasoning_tokens, p.is_correct, p.response_time,
               p.prompt_tokens, p.completion_tokens, p.total_tokens
        FROM puzzles p
        JOIN runs r ON p.run_id = r.id
        JOIN experiments e ON r.experiment_id = e.id
        WHERE r.game = 'sudoku_game'
    """
    params = []
    if model_filter:
        query += " AND r.model LIKE ?"
        params.append(f"%{model_filter}%")
    if treatment:
        query += " AND e.name LIKE ?"
        params.append(f"%{treatment}%")
    if is_text is not None:
        query += " AND r.is_text = ?"
        params.append(int(is_text))
    query += " ORDER BY r.model, p.iteration"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        puzzle = {
            "iteration": row["iteration"],
            "solution": row["solution"],
            "response": row["response"],
            "reasoning_content": row["reasoning_content"],
            "is_correct": bool(row["is_correct"]),
        }
        result = analyze_puzzle(row["model"], puzzle)
        results.append(result)
    return results


def main():
    parser = argparse.ArgumentParser(description="Analyze sudoku parsing errors")
    parser.add_argument(
        "source",
        help="Path to experiment directory (with experiment.json) or results.db",
    )
    parser.add_argument("--model", help="Filter to specific model (substring match)")
    parser.add_argument(
        "--only-failures", action="store_true", help="Only show failed puzzles"
    )
    parser.add_argument(
        "--summary", action="store_true", help="Show summary statistics only"
    )
    parser.add_argument(
        "--treatment", help="Filter to specific treatment/experiment name (DB only)"
    )
    parser.add_argument(
        "--text-only",
        action="store_true",
        help="Only text-mode experiments (DB only)",
    )
    parser.add_argument(
        "--image-only",
        action="store_true",
        help="Only image-mode experiments (DB only)",
    )
    args = parser.parse_args()

    source = Path(args.source)
    if source.suffix == ".db" or source.name == "results_orig.db":
        is_text = None
        if args.text_only:
            is_text = True
        elif args.image_only:
            is_text = False
        results = load_from_db(source, args.model, args.treatment, is_text)
    else:
        results = load_from_json(source, args.model)

    if not results:
        print("No sudoku puzzles found matching criteria.")
        return

    # Print detailed results
    if not args.summary:
        for r in results:
            if args.only_failures and r.is_correct:
                continue

            print(f"\n{'='*60}")
            print(
                f"Model: {r.model} | Puzzle #{r.puzzle_idx} | Correct: {r.is_correct}"
            )
            print(f"Error type: {r.error_type}")
            print(f"Detail: {r.detail}")

            if r.board_extracted and r.parsed_board:
                print(
                    f"\nParsed board (blanks: {r.blank_count}, expected: {r.expected_blank_count}):"
                )
                print(format_board(r.parsed_board))

            if r.solution_violations:
                print(f"\nSolution fill violations: {r.solution_violations}")
            if r.response_violations:
                print(f"\nResponse fill violations: {r.response_violations}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    models = sorted(set(r.model for r in results))
    for model in models:
        model_results = [r for r in results if r.model == model]
        total = len(model_results)
        correct = sum(1 for r in model_results if r.error_type == "correct")
        parsing_err = sum(1 for r in model_results if r.error_type == "parsing_error")
        solving_err = sum(1 for r in model_results if r.error_type == "solving_error")
        no_reasoning = sum(1 for r in model_results if r.error_type == "no_reasoning")
        parse_failed = sum(1 for r in model_results if r.error_type == "parse_failed")
        no_response = sum(1 for r in model_results if r.error_type == "no_response")
        extracted = sum(1 for r in model_results if r.board_extracted)

        print(f"\n{model}:")
        print(f"  Total puzzles: {total}")
        print(f"  Board extracted from reasoning: {extracted}/{total}")
        print(f"  Correct: {correct}/{total} ({100*correct/total:.0f}%)")
        if total - correct > 0:
            failures = total - correct
            print(f"  Failures: {failures}")
            if parsing_err:
                print(
                    f"    Parsing errors: {parsing_err} ({100*parsing_err/failures:.0f}% of failures)"
                )
            if solving_err:
                print(
                    f"    Solving errors: {solving_err} ({100*solving_err/failures:.0f}% of failures)"
                )
            if no_reasoning:
                print(f"    No reasoning (can't classify): {no_reasoning}")
            if parse_failed:
                print(f"    Board extraction failed (can't classify): {parse_failed}")
            if no_response:
                print(f"    Empty response: {no_response}")


if __name__ == "__main__":
    main()
