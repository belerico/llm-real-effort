#!/usr/bin/env python3
"""Generate summary statistics from benchmark results.

Usage:
    uv run python summary_stats.py                          # latest experiment group
    uv run python summary_stats.py -e low-no-incentive
    uv run python summary_stats.py -e low-no-incentive --csv
    uv run python summary_stats.py --melted -e low-no-incentive -e low-incentive
    uv run python summary_stats.py --melted -e low-no-incentive -e low-incentive --csv
"""

import argparse
import math
import sqlite3
from pathlib import Path

RESULTS_DB = Path(__file__).resolve().parent / "reports" / "results.db"


def _std(values: list[float]) -> float:
    """Population standard deviation."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))


def load_data(db_path: Path, experiment_prefix: str | None = None) -> list[dict]:
    """Load puzzle-level data from the DB."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    if experiment_prefix:
        prefix = experiment_prefix
    else:
        row = conn.execute(
            "SELECT name FROM experiments WHERE status = 'completed' ORDER BY created_at DESC LIMIT 1"
        ).fetchone()
        if not row:
            print("No completed experiments found.")
            return []
        name = row["name"]
        prefix = name.rsplit("_", 1)[0] if "_" in name else name
        all_names = [
            r["name"]
            for r in conn.execute(
                "SELECT name FROM experiments WHERE status = 'completed' ORDER BY created_at DESC"
            ).fetchall()
        ]
        for i in range(len(name), 0, -1):
            candidate = name[:i]
            matches = sum(1 for n in all_names if n.startswith(candidate))
            if matches > 1:
                prefix = candidate.rstrip("_")
                break

    rows = conn.execute(
        """
        SELECT r.model, r.game, p.is_correct, p.completion_tokens, p.reasoning_tokens,
               p.prompt_tokens, p.total_tokens, p.response_time, p.response
        FROM puzzles p
        JOIN runs r ON p.run_id = r.id
        JOIN experiments e ON r.experiment_id = e.id
        WHERE e.name LIKE ? AND e.status = 'completed' AND r.status = 'completed'
        ORDER BY r.model, r.game, p.iteration
        """,
        (f"{prefix}%",),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def _compute_group_stats(puzzles: list[dict]) -> dict:
    """Compute stats for a group of puzzles."""
    n = len(puzzles)
    if n == 0:
        return {}
    corrects = [p["is_correct"] or 0 for p in puzzles]
    c_tokens = [p["completion_tokens"] or 0 for p in puzzles]
    times = [p["response_time"] or 0 for p in puzzles]
    timeouts = sum(1 for p in puzzles if p["response"] == "TIMEOUT")
    reasoning_rows = [
        p
        for p in puzzles
        if p["response"] != "TIMEOUT" and p["reasoning_tokens"] is not None
    ]
    r_tokens = [p["reasoning_tokens"] for p in reasoning_rows]
    c_tokens_reasoning = [p["completion_tokens"] or 0 for p in reasoning_rows]

    return {
        "n": n,
        "accuracy": sum(corrects) / n,
        "accuracy_std": _std(corrects),
        "avg_c_tok": sum(c_tokens) / n,
        "std_c_tok": _std(c_tokens),
        "reasoning_rows": len(reasoning_rows),
        "avg_c_tok_reasoning": (
            sum(c_tokens_reasoning) / len(c_tokens_reasoning) if c_tokens_reasoning else 0.0
        ),
        "avg_r_tok": sum(r_tokens) / len(r_tokens) if r_tokens else 0.0,
        "std_r_tok": _std(r_tokens),
        "avg_time": sum(times) / n,
        "std_time": _std(times),
        "timeouts": timeouts,
    }


def compute_stats(data: list[dict]) -> tuple[list[dict], list[dict]]:
    """Compute per-model-game and per-model aggregate stats."""
    groups: dict[tuple[str, str], list[dict]] = {}
    for row in data:
        key = (row["model"], row["game"])
        groups.setdefault(key, []).append(row)

    game_stats = []
    for (model, game), puzzles in sorted(groups.items()):
        s = _compute_group_stats(puzzles)
        s["model"] = model
        s["game"] = game
        game_stats.append(s)

    model_groups: dict[str, list[dict]] = {}
    for row in data:
        model_groups.setdefault(row["model"], []).append(row)

    model_stats = []
    for model, puzzles in sorted(model_groups.items()):
        s = _compute_group_stats(puzzles)
        s["model"] = model
        model_stats.append(s)

    return game_stats, model_stats


def compute_melted(datasets: dict[str, list[dict]]) -> list[dict]:
    """Compute melted table: one row per (model, game, condition)."""
    rows = []
    for condition, data in datasets.items():
        groups: dict[tuple[str, str], list[dict]] = {}
        for row in data:
            key = (row["model"], row["game"])
            groups.setdefault(key, []).append(row)

        for (model, game), puzzles in sorted(groups.items()):
            s = _compute_group_stats(puzzles)
            s["model"] = model
            s["game"] = game
            s["condition"] = condition
            rows.append(s)

    return rows


def print_tables(game_stats: list[dict], model_stats: list[dict]):
    """Print formatted tables."""
    print("=" * 100)
    print("OVERALL MODEL RANKING")
    print("=" * 100)
    header = f"{'Model':<40} {'N':>4} {'R_n':>5} {'Acc%':>7} {'±std':>6} {'Avg c_tok':>10} {'±std':>8} {'Avg r_tok':>10} {'±std':>8} {'Avg time':>9} {'±std':>7} {'TO':>4}"
    print(header)
    print("-" * len(header))
    for s in sorted(model_stats, key=lambda x: -x["accuracy"]):
        model_short = s["model"].rsplit("/", 1)[-1]
        print(
            f"{model_short:<40} {s['n']:>4} {s['reasoning_rows']:>5} "
            f"{s['accuracy']*100:>6.1f}% {s['accuracy_std']*100:>5.1f} "
            f"{s['avg_c_tok']:>10.0f} {s['std_c_tok']:>8.0f} "
            f"{s['avg_r_tok']:>10.0f} {s['std_r_tok']:>8.0f} "
            f"{s['avg_time']:>9.1f} {s['std_time']:>7.1f} "
            f"{s['timeouts']:>4}"
        )

    games = sorted({s["game"] for s in game_stats})
    models = sorted({s["model"] for s in model_stats}, key=lambda m: next(
        -s["accuracy"] for s in model_stats if s["model"] == m
    ))

    print(f"\n{'=' * 100}")
    print("PER-GAME ACCURACY (% ± std)")
    print("=" * 100)

    col_w = 18
    header = f"{'Model':<28}" + "".join(f"{g:>{col_w}}" for g in games)
    print(header)
    print("-" * len(header))

    lookup = {(s["model"], s["game"]): s for s in game_stats}
    for model in models:
        model_short = model.rsplit("/", 1)[-1]
        row = f"{model_short:<28}"
        for game in games:
            s = lookup.get((model, game))
            if s:
                row += f"{s['accuracy']*100:>7.0f}±{s['accuracy_std']*100:<4.0f}    "
            else:
                row += f"{'—':>{col_w}}"
        print(row)

    print(f"\n{'=' * 100}")
    print("PER-GAME COMPLETION TOKENS (avg ± std)")
    print("=" * 100)

    header = f"{'Model':<28}" + "".join(f"{g:>{col_w}}" for g in games)
    print(header)
    print("-" * len(header))

    for model in models:
        model_short = model.rsplit("/", 1)[-1]
        row = f"{model_short:<28}"
        for game in games:
            s = lookup.get((model, game))
            if s:
                row += f"{s['avg_c_tok']:>7.0f}±{s['std_c_tok']:<4.0f}    "
            else:
                row += f"{'—':>{col_w}}"
        print(row)

    print(f"\n{'=' * 100}")
    print("PER-GAME RESPONSE TIME (avg ± std seconds)")
    print("=" * 100)

    header = f"{'Model':<28}" + "".join(f"{g:>{col_w}}" for g in games)
    print(header)
    print("-" * len(header))

    for model in models:
        model_short = model.rsplit("/", 1)[-1]
        row = f"{model_short:<28}"
        for game in games:
            s = lookup.get((model, game))
            if s:
                row += f"{s['avg_time']:>7.1f}±{s['std_time']:<4.1f}    "
            else:
                row += f"{'—':>{col_w}}"
        print(row)


def print_melted(melted: list[dict], as_csv: bool = False):
    """Print melted table."""
    if as_csv:
        print("model,game,condition,n,reasoning_rows,accuracy,accuracy_std,avg_c_tok,std_c_tok,avg_c_tok_reasoning,avg_r_tok,std_r_tok,avg_time,std_time,timeouts")
        for s in melted:
            print(
                f"{s['model']},{s['game']},{s['condition']},{s['n']},{s['reasoning_rows']},"
                f"{s['accuracy']:.4f},{s['accuracy_std']:.4f},"
                f"{s['avg_c_tok']:.1f},{s['std_c_tok']:.1f},"
                f"{s['avg_c_tok_reasoning']:.1f},{s['avg_r_tok']:.1f},{s['std_r_tok']:.1f},"
                f"{s['avg_time']:.2f},{s['std_time']:.2f},{s['timeouts']}"
            )
        return

    header = (
        f"{'Model':<28} {'Game':<20} {'Condition':<16} {'N':>4} {'R_n':>5} "
        f"{'Acc%':>7} {'±std':>6} "
        f"{'c_tok':>7} {'±std':>7} "
        f"{'r_tok':>7} {'±std':>7} "
        f"{'time':>7} {'±std':>6} "
        f"{'TO':>4}"
    )
    print(header)
    print("-" * len(header))

    prev_model = None
    for s in melted:
        model_short = s["model"].rsplit("/", 1)[-1]
        if prev_model and prev_model != s["model"]:
            print()
        prev_model = s["model"]
        print(
            f"{model_short:<28} {s['game']:<20} {s['condition']:<16} {s['n']:>4} {s['reasoning_rows']:>5} "
            f"{s['accuracy']*100:>6.1f}% {s['accuracy_std']*100:>5.1f} "
            f"{s['avg_c_tok']:>7.0f} {s['std_c_tok']:>7.0f} "
            f"{s['avg_r_tok']:>7.0f} {s['std_r_tok']:>7.0f} "
            f"{s['avg_time']:>7.1f} {s['std_time']:>6.1f} "
            f"{s['timeouts']:>4}"
        )


def print_csv(game_stats: list[dict], model_stats: list[dict]):
    """Print CSV output."""
    print("type,model,game,n,reasoning_rows,accuracy,accuracy_std,avg_c_tok,std_c_tok,avg_c_tok_reasoning,avg_r_tok,std_r_tok,avg_time,std_time,timeouts")
    for s in model_stats:
        print(
            f"model,{s['model']},,{s['n']},{s['reasoning_rows']},{s['accuracy']:.4f},{s['accuracy_std']:.4f},"
            f"{s['avg_c_tok']:.1f},{s['std_c_tok']:.1f},"
            f"{s['avg_c_tok_reasoning']:.1f},{s['avg_r_tok']:.1f},{s['std_r_tok']:.1f},"
            f"{s['avg_time']:.2f},{s['std_time']:.2f},{s['timeouts']}"
        )
    for s in game_stats:
        print(
            f"game,{s['model']},{s['game']},{s['n']},{s['reasoning_rows']},{s['accuracy']:.4f},{s['accuracy_std']:.4f},"
            f"{s['avg_c_tok']:.1f},{s['std_c_tok']:.1f},"
            f"{s['avg_c_tok_reasoning']:.1f},{s['avg_r_tok']:.1f},{s['std_r_tok']:.1f},"
            f"{s['avg_time']:.2f},{s['std_time']:.2f},{s['timeouts']}"
        )


def main():
    parser = argparse.ArgumentParser(description="Benchmark summary statistics")
    parser.add_argument(
        "--experiment", "-e", action="append", dest="experiments",
        help="Experiment name prefix(es). Use multiple -e for melted comparison.",
    )
    parser.add_argument("--db", default=str(RESULTS_DB), help="Path to results.db")
    parser.add_argument("--csv", action="store_true", help="Output as CSV")
    parser.add_argument("--melted", action="store_true", help="Melted table comparing multiple experiments")
    args = parser.parse_args()

    db_path = Path(args.db)
    experiments = args.experiments or [None]

    if args.melted or len(experiments) > 1:
        datasets = {}
        for exp in experiments:
            data = load_data(db_path, exp)
            label = exp or "latest"
            datasets[label] = data
            print(f"  Loaded {len(data)} puzzles for '{label}'")
        print()
        melted = compute_melted(datasets)
        print_melted(melted, as_csv=args.csv)
    else:
        data = load_data(db_path, experiments[0])
        if not data:
            return
        print(f"  {len(data)} puzzles loaded\n")
        game_stats, model_stats = compute_stats(data)
        if args.csv:
            print_csv(game_stats, model_stats)
        else:
            print_tables(game_stats, model_stats)


if __name__ == "__main__":
    main()
