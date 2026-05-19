#!/usr/bin/env python3
"""Plot benchmark results from melted CSV.

Usage:
    uv run python plot_results.py
    uv run python plot_results.py --csv reports/melted_comparison.csv
    uv run python plot_results.py -e low-no-incentive -e low-incentive
"""

import argparse
import sqlite3
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

RESULTS_DB = Path(__file__).resolve().parent / "reports" / "results_orig.db"
PLOT_DIR = Path(__file__).resolve().parent / "reports" / "plots"

# Short names for readability
MODEL_SHORT = {
    "anthropic/claude-opus-4.6": "Opus 4.6",
    "anthropic/claude-sonnet-4.6": "Sonnet 4.6",
    "google/gemini-3-flash-preview": "Gemini Flash",
    "google/gemini-3.1-pro-preview": "Gemini Pro",
    "openai/gpt-5.4": "GPT-5.4",
    "openai/gpt-5.2": "GPT-5.2",
    "moonshotai/kimi-k2.5": "Kimi K2.5",
    "qwen/qwen3.5-397b-a17b": "Qwen 3.5",
    "bytedance-seed/seed-2.0-mini": "Seed 2.0",
}

GAME_SHORT = {
    "add_numbers": "Addition",
    "count_numbers": "Count",
    "counting_zeros": "Zeros",
    "sudoku_game": "Sudoku",
    "task_decoding": "Decoding",
    "task_sequences": "Sequences",
    "task_summation": "Summation",
    "task_transcription": "Transcription",
}

CONDITION_LABELS = {
    "low-no-incentive": "No Incentive",
    "low-incentive": "Incentive",
}

COLORS = {
    "low-no-incentive": "#4C72B0",
    "low-incentive": "#DD8452",
}


def _std(values):
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))


def load_from_db(db_path, experiment_prefixes):
    """Load data directly from DB."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    datasets = {}
    for prefix in experiment_prefixes:
        rows = conn.execute(
            """
            SELECT r.model, r.game, p.is_correct, p.completion_tokens,
                   p.reasoning_tokens, p.response_time, p.response
            FROM puzzles p
            JOIN runs r ON p.run_id = r.id
            JOIN experiments e ON r.experiment_id = e.id
            WHERE e.name LIKE ? AND e.status = 'completed' AND r.status = 'completed'
            ORDER BY r.model, r.game, p.iteration
            """,
            (f"{prefix}%",),
        ).fetchall()
        datasets[prefix] = [dict(r) for r in rows]
    conn.close()
    return datasets


def compute_stats(datasets):
    """Compute per (model, game, condition) stats."""
    stats = []
    for condition, data in datasets.items():
        groups = {}
        for row in data:
            key = (row["model"], row["game"])
            groups.setdefault(key, []).append(row)

        for (model, game), puzzles in sorted(groups.items()):
            n = len(puzzles)
            corrects = [p["is_correct"] or 0 for p in puzzles]
            c_tokens = [p["completion_tokens"] or 0 for p in puzzles]
            times = [p["response_time"] or 0 for p in puzzles]
            reasoning_rows = [
                p
                for p in puzzles
                if p["response"] != "TIMEOUT" and p["reasoning_tokens"] is not None
            ]
            r_tokens = [p["reasoning_tokens"] for p in reasoning_rows]
            c_tokens_reasoning = [p["completion_tokens"] or 0 for p in reasoning_rows]

            stats.append({
                "model": model,
                "game": game,
                "condition": condition,
                "n": n,
                "reasoning_rows": len(reasoning_rows),
                "accuracy": sum(corrects) / n,
                "accuracy_std": _std(corrects),
                "accuracy_se": _std(corrects) / math.sqrt(n) if n > 1 else 0,
                "avg_c_tok": sum(c_tokens) / n,
                "std_c_tok": _std(c_tokens),
                "se_c_tok": _std(c_tokens) / math.sqrt(n) if n > 1 else 0,
                "avg_c_tok_reasoning": (
                    sum(c_tokens_reasoning) / len(c_tokens_reasoning)
                    if c_tokens_reasoning else 0.0
                ),
                "avg_r_tok": sum(r_tokens) / len(r_tokens) if r_tokens else 0.0,
                "std_r_tok": _std(r_tokens),
                "avg_time": sum(times) / n,
                "std_time": _std(times),
                "se_time": _std(times) / math.sqrt(n) if n > 1 else 0,
            })
    return stats


def _model_order(stats):
    """Sort models by overall accuracy (first condition)."""
    conds = sorted({s["condition"] for s in stats})
    first = conds[0]
    model_acc = {}
    for s in stats:
        if s["condition"] == first:
            model_acc.setdefault(s["model"], []).append(s["accuracy"])
    return sorted(model_acc, key=lambda m: -np.mean(model_acc[m]))


def plot_overall_accuracy(stats, conditions, models):
    """Bar chart: overall accuracy per model, grouped by condition."""
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(models))
    width = 0.35 if len(conditions) > 1 else 0.6
    offsets = np.linspace(-width * (len(conditions) - 1) / 2, width * (len(conditions) - 1) / 2, len(conditions))

    for i, cond in enumerate(conditions):
        accs, ses = [], []
        for model in models:
            vals = [s for s in stats if s["model"] == model and s["condition"] == cond]
            all_correct = [s["accuracy"] for s in vals]
            accs.append(np.mean(all_correct) * 100 if all_correct else 0)
            # SE of the mean across games
            ses.append(np.std(all_correct) / math.sqrt(len(all_correct)) * 100 if len(all_correct) > 1 else 0)

        label = CONDITION_LABELS.get(cond, cond)
        color = COLORS.get(cond, None)
        bars = ax.bar(x + offsets[i], accs, width, yerr=ses, label=label,
                      color=color, capsize=3, edgecolor="white", linewidth=0.5)
        for bar, acc in zip(bars, accs):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                    f"{acc:.1f}", ha="center", va="bottom", fontsize=7)

    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Overall Accuracy by Model")
    ax.set_xticks(x)
    ax.set_xticklabels([MODEL_SHORT.get(m, m.rsplit("/", 1)[-1]) for m in models], rotation=30, ha="right")
    ax.set_ylim(0, 110)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def plot_per_game_accuracy(stats, conditions, models):
    """Heatmap: accuracy per model × game, one per condition."""
    games = sorted({s["game"] for s in stats})
    figs = []

    for cond in conditions:
        fig, ax = plt.subplots(figsize=(12, 6))
        matrix = np.full((len(models), len(games)), np.nan)
        for s in stats:
            if s["condition"] != cond:
                continue
            if s["model"] in models and s["game"] in games:
                mi = models.index(s["model"])
                gi = games.index(s["game"])
                matrix[mi, gi] = s["accuracy"] * 100

        im = ax.imshow(matrix, cmap="RdYlGn", vmin=0, vmax=100, aspect="auto")
        for mi in range(len(models)):
            for gi in range(len(games)):
                val = matrix[mi, gi]
                if not np.isnan(val):
                    color = "white" if val < 40 or val > 85 else "black"
                    ax.text(gi, mi, f"{val:.0f}", ha="center", va="center", fontsize=9, color=color)

        ax.set_xticks(range(len(games)))
        ax.set_xticklabels([GAME_SHORT.get(g, g) for g in games], rotation=30, ha="right")
        ax.set_yticks(range(len(models)))
        ax.set_yticklabels([MODEL_SHORT.get(m, m.rsplit("/", 1)[-1]) for m in models])
        label = CONDITION_LABELS.get(cond, cond)
        ax.set_title(f"Accuracy by Game — {label}")
        fig.colorbar(im, ax=ax, label="Accuracy (%)", shrink=0.8)
        fig.tight_layout()
        figs.append((fig, f"heatmap_{cond}"))

    return figs


def plot_incentive_delta(stats, conditions, models):
    """Bar chart: accuracy delta (incentive - no_incentive) per game per model."""
    if len(conditions) < 2:
        return None
    cond_a, cond_b = conditions[0], conditions[1]
    games = sorted({s["game"] for s in stats})

    lookup = {}
    for s in stats:
        lookup[(s["model"], s["game"], s["condition"])] = s

    fig, ax = plt.subplots(figsize=(14, 6))
    x = np.arange(len(games))
    width = 0.8 / len(models)

    for i, model in enumerate(models):
        deltas = []
        for game in games:
            a = lookup.get((model, game, cond_a), {}).get("accuracy", 0)
            b = lookup.get((model, game, cond_b), {}).get("accuracy", 0)
            deltas.append((b - a) * 100)

        offset = (i - len(models) / 2 + 0.5) * width
        ax.bar(x + offset, deltas, width, label=MODEL_SHORT.get(model, model.rsplit("/", 1)[-1]),
               edgecolor="white", linewidth=0.3)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel("Δ Accuracy (pp)")
    ax.set_title(f"Incentive Effect: {CONDITION_LABELS.get(cond_b, cond_b)} − {CONDITION_LABELS.get(cond_a, cond_a)}")
    ax.set_xticks(x)
    ax.set_xticklabels([GAME_SHORT.get(g, g) for g in games], rotation=30, ha="right")
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=7)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def plot_tokens_vs_accuracy(stats, conditions, models):
    """Scatter: avg completion tokens vs accuracy, per model."""
    fig, ax = plt.subplots(figsize=(10, 7))

    for cond in conditions:
        marker = "o" if "no" in cond else "s"
        for model in models:
            vals = [s for s in stats if s["model"] == model and s["condition"] == cond]
            if not vals:
                continue
            avg_acc = np.mean([s["accuracy"] for s in vals]) * 100
            avg_tok = np.mean([s["avg_c_tok"] for s in vals])
            label_str = MODEL_SHORT.get(model, model.rsplit("/", 1)[-1])
            cond_label = CONDITION_LABELS.get(cond, cond)
            ax.scatter(avg_tok, avg_acc, s=80, marker=marker, zorder=3)
            ax.annotate(f"{label_str}\n({cond_label})", (avg_tok, avg_acc),
                        fontsize=6, ha="center", va="bottom", xytext=(0, 5),
                        textcoords="offset points")

    ax.set_xlabel("Avg Completion Tokens")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Efficiency: Tokens vs Accuracy")
    ax.set_ylim(50, 105)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    return fig


def plot_response_time(stats, conditions, models):
    """Bar chart: avg response time per model."""
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(models))
    width = 0.35 if len(conditions) > 1 else 0.6
    offsets = np.linspace(-width * (len(conditions) - 1) / 2, width * (len(conditions) - 1) / 2, len(conditions))

    for i, cond in enumerate(conditions):
        times, ses = [], []
        for model in models:
            vals = [s for s in stats if s["model"] == model and s["condition"] == cond]
            all_times = [s["avg_time"] for s in vals]
            times.append(np.mean(all_times) if all_times else 0)
            ses.append(np.std(all_times) / math.sqrt(len(all_times)) if len(all_times) > 1 else 0)

        label = CONDITION_LABELS.get(cond, cond)
        color = COLORS.get(cond, None)
        ax.bar(x + offsets[i], times, width, yerr=ses, label=label,
               color=color, capsize=3, edgecolor="white", linewidth=0.5)

    ax.set_ylabel("Avg Response Time (s)")
    ax.set_title("Response Time by Model")
    ax.set_xticks(x)
    ax.set_xticklabels([MODEL_SHORT.get(m, m.rsplit("/", 1)[-1]) for m in models], rotation=30, ha="right")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def plot_reasoning_ratio(stats, conditions, models):
    """Stacked bar: reasoning vs answer tokens per model."""
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(models))
    # Use first condition only
    cond = conditions[0]

    r_tokens, a_tokens = [], []
    for model in models:
        vals = [s for s in stats if s["model"] == model and s["condition"] == cond]
        valid = [s for s in vals if s["reasoning_rows"] > 0]
        avg_r = np.mean([s["avg_r_tok"] for s in valid]) if valid else 0
        avg_c = np.mean([s["avg_c_tok_reasoning"] for s in valid]) if valid else 0
        r_tokens.append(avg_r)
        a_tokens.append(max(0, avg_c - avg_r))

    ax.bar(x, r_tokens, 0.6, label="Reasoning", color="#E07B54")
    ax.bar(x, a_tokens, 0.6, bottom=r_tokens, label="Answer", color="#4C72B0")

    for i, (r, a) in enumerate(zip(r_tokens, a_tokens)):
        total = r + a
        if total > 0:
            ax.text(i, total + 10, f"{r / total * 100:.0f}%r", ha="center", va="bottom", fontsize=7)

    ax.set_ylabel("Avg Tokens")
    ax.set_title(f"Reasoning vs Answer Tokens — {CONDITION_LABELS.get(cond, cond)}")
    ax.set_xticks(x)
    ax.set_xticklabels([MODEL_SHORT.get(m, m.rsplit("/", 1)[-1]) for m in models], rotation=30, ha="right")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def plot_reasoning_vs_accuracy_per_game(datasets, conditions, models):
    """Scatter: reasoning tokens vs accuracy per game (subplots), using puzzle-level data."""
    # Use first condition
    cond = conditions[0]
    data = datasets[cond]
    games = sorted({d["game"] for d in data})

    ncols = 4
    nrows = math.ceil(len(games) / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4.5 * nrows), squeeze=False)

    model_colors = {}
    cmap = plt.colormaps["tab10"]
    for i, m in enumerate(models):
        model_colors[m] = cmap(i / max(len(models) - 1, 1))

    for idx, game in enumerate(games):
        ax = axes[idx // ncols][idx % ncols]
        game_data = [d for d in data if d["game"] == game]

        # Group by model
        model_groups = {}
        for d in game_data:
            model_groups.setdefault(d["model"], []).append(d)

        all_r, all_acc = [], []
        for model in models:
            puzzles = model_groups.get(model, [])
            if not puzzles:
                continue
            reasoning_rows = [
                p
                for p in puzzles
                if p["response"] != "TIMEOUT" and p["reasoning_tokens"] is not None
            ]
            if not reasoning_rows:
                continue
            r_tokens = [p["reasoning_tokens"] for p in reasoning_rows]
            corrects = [p["is_correct"] or 0 for p in puzzles]
            avg_r = np.mean(r_tokens)
            acc = np.mean(corrects) * 100
            se_acc = np.std(corrects) / math.sqrt(len(corrects)) * 100 if len(corrects) > 1 else 0

            all_r.append(avg_r)
            all_acc.append(acc)

            short = MODEL_SHORT.get(model, model.rsplit("/", 1)[-1])
            ax.scatter(avg_r, acc, s=70, color=model_colors[model], zorder=3)
            ax.annotate(short, (avg_r, acc), fontsize=5.5, ha="center", va="bottom",
                        xytext=(0, 4), textcoords="offset points")

        # Correlation
        if len(all_r) > 2:
            r_arr, acc_arr = np.array(all_r), np.array(all_acc)
            if np.std(r_arr) > 0 and np.std(acc_arr) > 0:
                corr = np.corrcoef(r_arr, acc_arr)[0, 1]
                z = np.polyfit(r_arr, acc_arr, 1)
                p = np.poly1d(z)
                x_line = np.linspace(r_arr.min(), r_arr.max(), 50)
                ax.plot(x_line, p(x_line), "--", color="gray", alpha=0.5, linewidth=1)
                ax.text(0.95, 0.05, f"r={corr:.2f}", transform=ax.transAxes,
                        ha="right", va="bottom", fontsize=8, color="gray")

        ax.set_title(GAME_SHORT.get(game, game), fontsize=11)
        ax.set_xlabel("Avg Reasoning Tokens", fontsize=8)
        ax.set_ylabel("Accuracy (%)", fontsize=8)
        ax.set_ylim(-5, 110)
        ax.grid(alpha=0.3)
        ax.tick_params(labelsize=7)

    # Hide empty subplots
    for idx in range(len(games), nrows * ncols):
        axes[idx // ncols][idx % ncols].set_visible(False)

    label = CONDITION_LABELS.get(cond, cond)
    fig.suptitle(f"Reasoning Tokens vs Accuracy by Game — {label}", fontsize=14, y=1.01)
    fig.tight_layout()
    return fig


def plot_reasoning_vs_accuracy_overall(datasets, conditions, models):
    """Scatter: avg reasoning tokens vs accuracy per model, all games pooled, with correlation."""
    fig, ax = plt.subplots(figsize=(10, 7))

    model_colors = {}
    cmap = plt.colormaps["tab10"]
    for i, m in enumerate(models):
        model_colors[m] = cmap(i / max(len(models) - 1, 1))

    for ci, cond in enumerate(conditions):
        data = datasets[cond]
        marker = "o" if ci == 0 else "s"
        all_r, all_acc = [], []

        for model in models:
            puzzles = [d for d in data if d["model"] == model]
            if not puzzles:
                continue
            reasoning_rows = [
                p
                for p in puzzles
                if p["response"] != "TIMEOUT" and p["reasoning_tokens"] is not None
            ]
            if not reasoning_rows:
                continue
            avg_r = np.mean([p["reasoning_tokens"] for p in reasoning_rows])
            acc = np.mean([p["is_correct"] or 0 for p in puzzles]) * 100
            all_r.append(avg_r)
            all_acc.append(acc)

            short = MODEL_SHORT.get(model, model.rsplit("/", 1)[-1])
            cond_label = CONDITION_LABELS.get(cond, cond)
            ax.scatter(avg_r, acc, s=90, marker=marker, color=model_colors[model], zorder=3)
            ax.annotate(f"{short}\n({cond_label})", (avg_r, acc), fontsize=6, ha="center",
                        va="bottom", xytext=(0, 5), textcoords="offset points")

        # Regression line per condition
        if len(all_r) > 2:
            r_arr, acc_arr = np.array(all_r), np.array(all_acc)
            if np.std(r_arr) > 0 and np.std(acc_arr) > 0:
                corr = np.corrcoef(r_arr, acc_arr)[0, 1]
                z = np.polyfit(r_arr, acc_arr, 1)
                p = np.poly1d(z)
                x_line = np.linspace(r_arr.min(), r_arr.max(), 50)
                color = COLORS.get(cond, "gray")
                cond_label = CONDITION_LABELS.get(cond, cond)
                ax.plot(x_line, p(x_line), "--", color=color, alpha=0.7, linewidth=1.5,
                        label=f"{cond_label} (r={corr:.2f})")

    ax.set_xlabel("Avg Reasoning Tokens")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Reasoning Tokens vs Accuracy (Overall)")
    ax.set_ylim(50, 105)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    return fig


def main():
    parser = argparse.ArgumentParser(description="Plot benchmark results")
    parser.add_argument("-e", "--experiment", action="append", dest="experiments",
                        help="Experiment prefix(es)")
    parser.add_argument("--db", default=str(RESULTS_DB))
    parser.add_argument("--show", action="store_true", help="Show plots interactively")
    args = parser.parse_args()

    experiments = args.experiments or ["low-no-incentive", "low-incentive"]
    datasets = load_from_db(Path(args.db), experiments)
    for exp, data in datasets.items():
        print(f"  {exp}: {len(data)} puzzles")

    all_stats = compute_stats(datasets)
    conditions = list(datasets.keys())
    models = _model_order(all_stats)

    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Overall accuracy
    fig = plot_overall_accuracy(all_stats, conditions, models)
    fig.savefig(PLOT_DIR / "overall_accuracy.png", dpi=150)
    print(f"  Saved: {PLOT_DIR / 'overall_accuracy.png'}")

    # 2. Heatmaps
    for fig, name in plot_per_game_accuracy(all_stats, conditions, models):
        fig.savefig(PLOT_DIR / f"{name}.png", dpi=150)
        print(f"  Saved: {PLOT_DIR / f'{name}.png'}")

    # 3. Incentive delta
    if len(conditions) > 1:
        fig = plot_incentive_delta(all_stats, conditions, models)
        if fig:
            fig.savefig(PLOT_DIR / "incentive_delta.png", dpi=150)
            print(f"  Saved: {PLOT_DIR / 'incentive_delta.png'}")

    # 4. Tokens vs accuracy scatter
    fig = plot_tokens_vs_accuracy(all_stats, conditions, models)
    fig.savefig(PLOT_DIR / "tokens_vs_accuracy.png", dpi=150)
    print(f"  Saved: {PLOT_DIR / 'tokens_vs_accuracy.png'}")

    # 5. Response time
    fig = plot_response_time(all_stats, conditions, models)
    fig.savefig(PLOT_DIR / "response_time.png", dpi=150)
    print(f"  Saved: {PLOT_DIR / 'response_time.png'}")

    # 6. Reasoning ratio
    fig = plot_reasoning_ratio(all_stats, conditions, models)
    fig.savefig(PLOT_DIR / "reasoning_ratio.png", dpi=150)
    print(f"  Saved: {PLOT_DIR / 'reasoning_ratio.png'}")

    # 7. Reasoning vs accuracy (overall)
    fig = plot_reasoning_vs_accuracy_overall(datasets, conditions, models)
    fig.savefig(PLOT_DIR / "reasoning_vs_accuracy_overall.png", dpi=150)
    print(f"  Saved: {PLOT_DIR / 'reasoning_vs_accuracy_overall.png'}")

    # 8. Reasoning vs accuracy (per game)
    fig = plot_reasoning_vs_accuracy_per_game(datasets, conditions, models)
    fig.savefig(PLOT_DIR / "reasoning_vs_accuracy_per_game.png", dpi=150, bbox_inches="tight")
    print(f"  Saved: {PLOT_DIR / 'reasoning_vs_accuracy_per_game.png'}")

    if args.show:
        plt.show()
    else:
        plt.close("all")

    print(f"\n  All plots saved to {PLOT_DIR}/")


if __name__ == "__main__":
    main()
