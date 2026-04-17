#!/usr/bin/env python3
"""Export benchmark results to JSON for analysis with pandas.

Usage:
    uv run python export_results.py                          # all experiments
    uv run python export_results.py --experiment low-no-incentive  # filter by prefix
    uv run python export_results.py --output results.json    # custom output path

Output JSON structure (load with pd.read_json or pd.json_normalize):
    [
        {
            "experiment": "low-no-incentive_gpt-5.4",
            "model": "gpt-5.4",
            "model_full": "openrouter/openai/gpt-5.4",
            "game": "sudoku_game",
            "status": "completed",
            "num_correct": 20,
            "num_failed": 0,
            "num_trials": 20,
            "num_timeout": 0,
            "prompt_tokens": 12345,
            "completion_tokens": 6789,
            "total_tokens": 19134,
            "session_time": 456.7,
            "puzzles": [
                {"iteration": 1, "response": "...", "is_correct": true, "response_time": 23.4, "timed_out": false},
                ...
            ]
        },
        ...
    ]
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DB = SCRIPT_DIR / "reports" / "results.db"
OTREE_DB = SCRIPT_DIR / "db.sqlite3"

PUZZLE_TABLES = {
    "sudoku_game": "sudoku_game_puzzle",
    "add_numbers": "add_numbers_puzzle",
    "count_numbers": "count_numbers_puzzle",
    "counting_zeros": "counting_zeros_puzzle",
    "task_decoding": "task_decoding_puzzle",
    "task_sequences": "task_sequences_question",
    "task_summation": "task_summation_puzzle",
    "task_transcription": "task_transcription_puzzle",
}
PLAYER_TABLES = {g: f"{g}_player" for g in PUZZLE_TABLES}


def get_otree_data(session_code, game):
    """Get player summary + puzzle details from oTree's db.sqlite3."""
    if not OTREE_DB.exists():
        return None, []

    conn = sqlite3.connect(OTREE_DB, timeout=30)
    conn.row_factory = sqlite3.Row

    # Resolve session code → session id
    row = conn.execute(
        "SELECT id FROM otree_session WHERE code = ?", (session_code,)
    ).fetchone()
    if not row:
        conn.close()
        return None, []
    session_id = row["id"]

    # Player summary
    player_table = PLAYER_TABLES[game]
    player = conn.execute(
        f"SELECT num_correct, num_failed, num_trials FROM [{player_table}] WHERE session_id = ?",
        (session_id,),
    ).fetchone()
    player_dict = dict(player) if player else None

    # Puzzle details
    puzzle_table = PUZZLE_TABLES[game]
    puzzles = conn.execute(
        f"SELECT iteration, solution, response, is_correct, timestamp, response_timestamp "
        f"FROM [{puzzle_table}] p JOIN [{player_table}] pl ON p.player_id = pl.id "
        f"WHERE pl.session_id = ? ORDER BY p.iteration",
        (session_id,),
    ).fetchall()

    puzzle_list = []
    for p in puzzles:
        ts = p["timestamp"] or 0
        rts = p["response_timestamp"] or 0
        resp_time = round(rts - ts, 2) if (rts and ts) else None
        timed_out = p["response"] == "TIMEOUT" if p["response"] else False
        puzzle_list.append({
            "iteration": p["iteration"],
            "solution": p["solution"],
            "response": p["response"],
            "is_correct": bool(p["is_correct"]) if p["is_correct"] is not None else None,
            "response_time": resp_time,
            "timed_out": timed_out,
        })

    conn.close()
    return player_dict, puzzle_list


def main():
    parser = argparse.ArgumentParser(description="Export benchmark results to JSON.")
    parser.add_argument("--experiment", default=None, help="Filter by experiment prefix (e.g. 'low-no-incentive')")
    parser.add_argument("--output", default=None, help="Output JSON path (default: reports/<experiment>_export.json)")
    parser.add_argument("--summary", action="store_true", default=True, help="Print summary table (default)")
    parser.add_argument("--no-summary", action="store_true", help="Skip summary table")
    args = parser.parse_args()

    if not RESULTS_DB.exists():
        print(f"ERROR: {RESULTS_DB} not found", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(RESULTS_DB)
    conn.row_factory = sqlite3.Row

    # Get experiments
    if args.experiment:
        experiments = conn.execute(
            "SELECT * FROM experiments WHERE name LIKE ?", (f"{args.experiment}%",)
        ).fetchall()
    else:
        experiments = conn.execute("SELECT * FROM experiments").fetchall()

    if not experiments:
        print("No experiments found.", file=sys.stderr)
        sys.exit(1)

    # Collect all data
    records = []
    for exp in experiments:
        exp_name = exp["name"]
        runs = conn.execute(
            "SELECT * FROM runs WHERE experiment_id = ? ORDER BY id", (exp["id"],)
        ).fetchall()

        for run in runs:
            model_full = run["model"]
            model_short = model_full.rsplit("/", 1)[-1]

            # Try oTree DB first for fresh data, fall back to results.db
            player_otree, puzzles_otree = None, []
            if run["session_code"] and run["game"] in PUZZLE_TABLES:
                player_otree, puzzles_otree = get_otree_data(run["session_code"], run["game"])

            # Use oTree data if available, otherwise results.db
            if player_otree:
                num_correct = player_otree["num_correct"]
                num_failed = player_otree["num_failed"]
                num_trials = player_otree["num_trials"]
            else:
                num_correct = run["num_correct"]
                num_failed = run["num_failed"]
                num_trials = run["num_trials"]

            if puzzles_otree:
                puzzles = puzzles_otree
            else:
                # Fall back to puzzles in results.db
                puzzles_db = conn.execute(
                    "SELECT * FROM puzzles WHERE run_id = ? ORDER BY iteration",
                    (run["id"],),
                ).fetchall()
                puzzles = [{
                    "iteration": p["iteration"],
                    "solution": p["solution"],
                    "response": p["response"],
                    "is_correct": bool(p["is_correct"]) if p["is_correct"] is not None else None,
                    "response_time": p["response_time"],
                    "timed_out": p["response"] == "TIMEOUT" if p["response"] else False,
                } for p in puzzles_db]

            num_timeout = sum(1 for p in puzzles if p.get("timed_out"))

            records.append({
                "experiment": exp_name,
                "model": model_short,
                "model_full": model_full,
                "game": run["game"],
                "status": run["status"],
                "num_correct": num_correct,
                "num_failed": num_failed,
                "num_trials": num_trials,
                "num_timeout": num_timeout,
                "prompt_tokens": run["prompt_tokens"],
                "completion_tokens": run["completion_tokens"],
                "total_tokens": run["total_tokens"],
                "session_time": run["session_time"],
                "session_code": run["session_code"],
                "puzzles": puzzles,
            })

    conn.close()

    # Summary table
    if not args.no_summary:
        games = ["sudoku_game", "add_numbers", "count_numbers", "counting_zeros",
                 "task_decoding", "task_sequences", "task_summation", "task_transcription"]
        short = ["sudoku", "add", "count", "zeros", "decode", "seq", "sum", "trscr"]

        # Group by experiment prefix
        prefixes = sorted(set(r["experiment"].rsplit("_", 1)[0] for r in records if "_" in r["experiment"]))

        for prefix in prefixes:
            print(f"\n{'='*95}")
            print(f"  {prefix}")
            print(f"{'='*95}")

            # Collect per-model results
            from collections import defaultdict
            model_data = defaultdict(dict)
            for r in records:
                if r["experiment"].startswith(prefix + "_") and r["status"] == "completed":
                    model_data[r["model"]][r["game"]] = r

            header = f"{'MODEL':<24} " + " ".join(f"{g:>7}" for g in short) + "   TOTAL"
            print(header)
            print("─" * 100)

            rows = []
            for model in sorted(model_data.keys()):
                row = f"{model:<24} "
                tot_c, tot_t = 0, 0
                for g in games:
                    if g in model_data[model]:
                        r = model_data[model][g]
                        c = r["num_correct"] or 0
                        t = r["num_trials"] or 0
                        to = r["num_timeout"]
                        if to > 0:
                            row += f"{c:>3}/{t:<3} "
                        else:
                            row += f"{c:>3}/{t:<3} "
                        tot_c += c
                        tot_t += t
                    else:
                        row += f"{'·':>7} "
                row += f"  {tot_c}/{tot_t}"
                rows.append((tot_c, row))

            for _, row in sorted(rows, key=lambda x: -x[0]):
                print(row)

        # Token summary
        print(f"\n{'─'*60}")
        print("TOKEN USAGE")
        print(f"{'─'*60}")
        from collections import defaultdict
        token_totals = defaultdict(lambda: [0, 0, 0])
        for r in records:
            if r["status"] == "completed":
                token_totals[r["model"]][0] += r["prompt_tokens"] or 0
                token_totals[r["model"]][1] += r["completion_tokens"] or 0
                token_totals[r["model"]][2] += r["total_tokens"] or 0

        print(f"{'MODEL':<24} {'PROMPT':>10} {'COMPLETION':>12} {'TOTAL':>10}")
        for model in sorted(token_totals, key=lambda x: -token_totals[x][2]):
            p, c, t = token_totals[model]
            print(f"{model:<24} {p:>10,} {c:>12,} {t:>10,}")

    # Export JSON
    output = args.output
    if not output:
        prefix = args.experiment or "all"
        output = f"reports/{prefix}_export.json"

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        json.dump(records, f, indent=2)
    print(f"\nExported {len(records)} records to {output}")
    print(f"Load with: pd.read_json('{output}')")
    print(f"Puzzles:   pd.json_normalize(json.load(open('{output}')), 'puzzles', ['experiment','model','game'])")


if __name__ == "__main__":
    main()
