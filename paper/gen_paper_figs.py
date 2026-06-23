"""Generate paper figures from the analysis notebook data."""

import datetime
import math
import sqlite3
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as mtick
import seaborn as sns
from adjustText import adjust_text

# ── Global font settings (uniform across all figures) ──
sns.set_theme(style="whitegrid", context="notebook", palette="colorblind")
FONT = {
    "title": 20,
    "label": 18,
    "tick": 15,
    "annot": 13,
    "legend": 14,
    "legend_title": 15,
    "bar_label": 13,
}
plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.family": "serif",
        "font.size": FONT["tick"],
        "axes.titlesize": FONT["title"],
        "axes.labelsize": FONT["label"],
        "xtick.labelsize": FONT["tick"],
        "ytick.labelsize": FONT["tick"],
        "legend.fontsize": FONT["legend"],
        "legend.title_fontsize": FONT["legend_title"],
    }
)

OUT = Path(__file__).resolve().parent / "imgs"
DB = (
    Path(__file__).resolve().parent.parent
    / "real_effort"
    / "reports"
    / "results_orig.db"
)
HUMAN_DIR = Path(__file__).resolve().parent.parent / "human-exps"

# Humans ran two sessions on separate days with a fresh oTree participant_code
# each day, so email is the only cross-day identifier. A few people typed a
# different email each day; collapse each pair to one identity (left -> canonical).
HUMAN_EMAIL_ALIASES = {
    "c.vendra@unibg.it": "c.vendra@studenti.unibg.it",
    "a.bergamaschi04@gmail.com": "a.bergamaschi7@studenti.unibg.it",
    "matty.rossi100@gmail.com": "m.rossi111@studenti.unibg.it",
}

# ── Load data ──
conn = sqlite3.connect(DB)
df = pd.read_sql_query(
    """
    SELECT e.name AS experiment, r.model, r.game,
           p.iteration, p.is_correct, p.response_time,
           p.prompt_tokens, p.completion_tokens, p.total_tokens, p.response
    FROM puzzles p JOIN runs r ON p.run_id = r.id JOIN experiments e ON r.experiment_id = e.id
    WHERE r.status = 'completed'
    ORDER BY e.name, r.model, r.game, p.iteration
""",
    conn,
)
conn.close()

# Experiment name -> (treatment label, persona, incentive)
TREATMENT_MAP = {
    "t0-control": ("T0: Control", "control", "none"),
    "t1-standard-no-incentive": ("T1: Std No Inc", "standard", "no"),
    "t2-standard-incentive": ("T2: Std Inc", "standard", "yes"),
    "t3-human-no-incentive": ("T3: Hum No Inc", "human", "no"),
    "t4-human-incentive": ("T4: Hum Inc", "human", "yes"),
}

# Drop experiments not in our map (e.g. ad-hoc test runs)
df = df[df["experiment"].isin(TREATMENT_MAP)].copy()
TREATMENT_ORDER = [
    "T0: Control",
    "T1: Std No Inc",
    "T2: Std Inc",
    "T3: Hum No Inc",
    "T4: Hum Inc",
]

df["treatment"] = df["experiment"].map(lambda x: TREATMENT_MAP[x][0])
df["persona"] = df["experiment"].map(lambda x: TREATMENT_MAP[x][1])
df["incentive"] = df["experiment"].map(lambda x: TREATMENT_MAP[x][2])


def _clean_model_name(s):
    """Uniform display names: claude-3.7-sonnet → claude-sonnet-3.7, remove -preview."""
    s = s.replace("claude-3.7-sonnet", "claude-sonnet-3.7")
    s = s.replace("-preview", "")
    return s


df["model_short"] = df["model"].str.rsplit("/", n=1).str[-1].map(_clean_model_name)
df["is_correct"] = df["is_correct"].fillna(0).astype(int)
df["timed_out"] = df["response"] == "TIMEOUT"
df.loc[df["timed_out"], "response_time"] = 120
df.loc[df["timed_out"], "completion_tokens"] = 2048
# Impute prompt_tokens for timeouts using the average for that model+game
_timeout_mask = df["timed_out"]
if _timeout_mask.any():
    _avg_prompt = df[~_timeout_mask].groupby(["model", "game"])["prompt_tokens"].mean()
    for idx in df[_timeout_mask].index:
        key = (df.loc[idx, "model"], df.loc[idx, "game"])
        if key in _avg_prompt.index:
            df.loc[idx, "prompt_tokens"] = round(_avg_prompt[key])
    df.loc[_timeout_mask, "total_tokens"] = (
        df.loc[_timeout_mask, "prompt_tokens"]
        + df.loc[_timeout_mask, "completion_tokens"]
    )
df["treatment"] = pd.Categorical(
    df["treatment"], categories=TREATMENT_ORDER, ordered=True
)

PRICING = {
    "anthropic/claude-3.7-sonnet": {"input": 3e-6, "output": 15e-6},
    "anthropic/claude-haiku-4.5": {"input": 1e-6, "output": 5e-6},
    "anthropic/claude-opus-4.5": {"input": 5e-6, "output": 25e-6},
    "anthropic/claude-opus-4.6": {"input": 5e-6, "output": 25e-6},
    "anthropic/claude-sonnet-4": {"input": 3e-6, "output": 15e-6},
    "anthropic/claude-sonnet-4.5": {"input": 3e-6, "output": 15e-6},
    "anthropic/claude-sonnet-4.6": {"input": 3e-6, "output": 15e-6},
    "google/gemini-2.5-flash": {"input": 0.3e-6, "output": 2.5e-6},
    "google/gemini-2.5-pro": {"input": 1.25e-6, "output": 10e-6},
    "google/gemini-3-flash-preview": {"input": 0.5e-6, "output": 3e-6},
    "google/gemini-3.1-pro-preview": {"input": 2e-6, "output": 12e-6},
    "openai/gpt-5": {"input": 1.25e-6, "output": 10e-6},
    "openai/gpt-5-mini": {"input": 0.25e-6, "output": 2e-6},
    "openai/gpt-5.1": {"input": 1.25e-6, "output": 10e-6},
    "openai/gpt-5.2": {"input": 1.75e-6, "output": 14e-6},
    "openai/gpt-5.4": {"input": 2.5e-6, "output": 15e-6},
    "openai/o3": {"input": 2e-6, "output": 8e-6},
    "openai/o4-mini": {"input": 1.1e-6, "output": 4.4e-6},
    "openai/o4-mini-high": {"input": 1.1e-6, "output": 4.4e-6},
    "google/gemini-2.5-flash-lite": {"input": 0.1e-6, "output": 0.4e-6},
    "google/gemini-3.1-flash-lite-preview": {"input": 0.25e-6, "output": 1.5e-6},
    "openai/gpt-5.4-mini": {"input": 0.75e-6, "output": 4.5e-6},
    "openai/gpt-5.4-nano": {"input": 0.2e-6, "output": 1.25e-6},
}
_zero = {"input": 0, "output": 0}
df["cost_total"] = (
    df["model"].map(lambda m: PRICING.get(m, _zero)["input"]) * df["prompt_tokens"]
    + df["model"].map(lambda m: PRICING.get(m, _zero)["output"])
    * df["completion_tokens"]
)

grouped_df = (
    df.groupby(["experiment", "model", "game"], observed=True)
    .agg(
        accuracy=("is_correct", "mean"),
        total_completion_tokens=("completion_tokens", "sum"),
        total_tokens=("total_tokens", "sum"),
        total_time=("response_time", "sum"),
        cost_per_game=("cost_total", "sum"),
        n_puzzles=("is_correct", "count"),
    )
    .reset_index()
)
grouped_df["model_short"] = (
    grouped_df["model"].str.rsplit("/", n=1).str[-1].map(_clean_model_name)
)
grouped_df["treatment"] = grouped_df["experiment"].map(lambda x: TREATMENT_MAP[x][0])
grouped_df["treatment"] = pd.Categorical(
    grouped_df["treatment"], categories=TREATMENT_ORDER, ordered=True
)
grouped_df["persona"] = grouped_df["experiment"].map(lambda x: TREATMENT_MAP[x][1])
grouped_df["incentive"] = grouped_df["experiment"].map(lambda x: TREATMENT_MAP[x][2])

GAME_LABELS = {
    "add_numbers": "Addition",
    "task_summation": "Pair Summation",
    "task_decoding": "Letter Decoding",
    "task_sequences": "Sequence Completion",
    "task_transcription": "Distorted Text",
    "string_entry": "String Entry",
    "counting_zeros": "Counting Zeros",
    "sudoku_game": "Sudoku",
}


def _rename_games(obj):
    """Rename game columns/index using GAME_LABELS. Works on Series, DataFrame, or list."""
    if isinstance(obj, pd.DataFrame):
        return obj.rename(columns=GAME_LABELS, index=GAME_LABELS)
    elif isinstance(obj, pd.Series):
        return obj.rename(index=GAME_LABELS)
    elif isinstance(obj, list):
        return [GAME_LABELS.get(g, g) for g in obj]
    return obj


def load_human_trials(matched_only=True):
    """Trial-level human data, one row per trial: email, game, is_correct.

    Day-1 contributes 5 games and day-2 the other 3. Emails are lowercased and
    the hand-linked aliases applied before any matching.

    With ``matched_only=True`` (default) a participant is retained only if their
    email appears in BOTH days, so every retained participant has all 8 tasks.
    With ``matched_only=False`` every participant who attempted a task is kept,
    so each task's accuracy is computed over all of its participants rather than
    just the both-days intersection.
    """

    def _read_day(day_dir):
        frames = []
        for path in sorted(day_dir.glob("*_custom_export_*.csv")):
            game = path.name.split("_custom_export_")[0]
            if game not in GAME_LABELS:
                continue
            d = pd.read_csv(path)[["participant_label", "is_correct"]].copy()
            d["game"] = game
            frames.append(d)
        out = pd.concat(frames, ignore_index=True)
        out["email"] = (
            out["participant_label"]
            .astype(str)
            .str.strip()
            .str.lower()
            .replace(HUMAN_EMAIL_ALIASES)
        )
        return out

    day1 = _read_day(HUMAN_DIR / "day-1")
    day2 = _read_day(HUMAN_DIR / "day-2")
    hum = pd.concat([day1, day2], ignore_index=True)
    hum = hum[hum["email"].str.contains("@", na=False)].copy()
    if matched_only:
        matched = set(day1["email"]) & set(day2["email"])
        hum = hum[hum["email"].isin(matched)].copy()
    hum["is_correct"] = (
        pd.to_numeric(hum["is_correct"], errors="coerce").fillna(0).astype(int)
    )
    return hum[["email", "game", "is_correct"]]


MODEL_COLORS = {
    # Anthropic (amber/brown — warm, saturated)
    "claude-haiku-4.5": "#F5D490",
    "claude-sonnet-3.7": "#E8B850",
    "claude-sonnet-4": "#D49C28",
    "claude-sonnet-4.5": "#C08418",
    "claude-sonnet-4.6": "#A06A10",
    "claude-opus-4.5": "#7A4E0C",
    "claude-opus-4.6": "#583608",
    # Google (blues — vivid spread)
    "gemini-2.5-flash-lite": "#B8D4F0",
    "gemini-3.1-flash-lite": "#88B8E8",
    "gemini-2.5-flash": "#5898D8",
    "gemini-3-flash": "#3078C0",
    "gemini-2.5-pro": "#1860A8",
    "gemini-3.1-pro": "#0A4080",
    # OpenAI — GPT series (greens) + O series (teal, distinct hue)
    "gpt-5.4-nano": "#B8E0BA",
    "gpt-5-mini": "#88C88E",
    "gpt-5.4-mini": "#5CB064",
    "gpt-5": "#389840",
    "gpt-5.1": "#207828",
    "gpt-5.2": "#106018",
    "gpt-5.4": "#084A10",
    "o4-mini": "#6CCEC4",
    "o4-mini-high": "#30A89C",
    "o3": "#108878",
}

MODEL_ABBREV = {
    # Anthropic
    "claude-sonnet-3.7": "CS3.7",
    "claude-haiku-4.5": "CH4.5",
    "claude-sonnet-4": "CS4",
    "claude-sonnet-4.5": "CS4.5",
    "claude-sonnet-4.6": "CS4.6",
    "claude-opus-4.5": "CO4.5",
    "claude-opus-4.6": "CO4.6",
    # Google
    "gemini-2.5-flash": "G2.5F",
    "gemini-2.5-flash-lite": "G2.5FL",
    "gemini-2.5-pro": "G2.5P",
    "gemini-3-flash": "G3F",
    "gemini-3.1-flash-lite": "G3.1FL",
    "gemini-3.1-pro": "G3.1P",
    # OpenAI
    "gpt-5": "GPT5",
    "gpt-5-mini": "GPT5m",
    "gpt-5.1": "GPT5.1",
    "gpt-5.2": "GPT5.2",
    "gpt-5.4": "GPT5.4",
    "gpt-5.4-mini": "GPT5.4m",
    "gpt-5.4-nano": "GPT5.4n",
    "o3": "O3",
    "o4-mini": "O4m",
    "o4-mini-high": "O4mH",
}


def _family_color(m):
    """Return the family color for a model short name."""
    if m.startswith("claude"):
        return "#C08418"
    elif m.startswith("gemini"):
        return "#3078C0"
    else:
        return "#389840"


def model_abbrev_legend(
    ax_or_fig, ncol=3, fontsize=10, use_family_colors=False, **kwargs
):
    """Add a legend mapping abbreviated labels to full model names with colored dots."""
    from matplotlib.lines import Line2D

    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=_family_color(m) if use_family_colors else MODEL_COLORS[m],
            markersize=8,
            label=f"{MODEL_ABBREV[m]} = {m}",
        )
        for m in sort_by_family(list(MODEL_ABBREV.keys()))
    ]
    return ax_or_fig.legend(handles=handles, ncol=ncol, fontsize=fontsize, **kwargs)


TREATMENT_COLORS = {
    "T0: Control": "#999999",
    "T1: Std No Inc": "#4C72B0",
    "T2: Std Inc": "#DD8452",
    "T3: Hum No Inc": "#55A868",
    "T4: Hum Inc": "#C44E52",
}
treatment_palette = [TREATMENT_COLORS[t] for t in TREATMENT_ORDER]

MODEL_RELEASE_TS = {
    "claude-sonnet-3.7": 1740422110,
    "claude-sonnet-4": 1747930371,
    "claude-haiku-4.5": 1760547638,
    "claude-sonnet-4.5": 1759161676,
    "claude-opus-4.5": 1764010580,
    "claude-opus-4.6": 1770219050,
    "claude-sonnet-4.6": 1771342990,
    "gemini-2.5-pro": 1750169544,
    "gemini-2.5-flash": 1750172488,
    "gemini-2.5-flash-lite": 1753200276,
    "gemini-3-flash": 1765987078,
    "gemini-3.1-flash-lite": 1772512673,
    "gemini-3.1-pro": 1771509627,
    "o3": 1744823457,
    "o4-mini": 1744820942,
    "o4-mini-high": 1744824212,
    "gpt-5-mini": 1754587407,
    "gpt-5": 1754587413,
    "gpt-5.1": 1763060305,
    "gpt-5.2": 1765389775,
    "gpt-5.4": 1772734352,
    "gpt-5.4-mini": 1773748178,
    "gpt-5.4-nano": 1773748187,
}
MODEL_RELEASE_DATE = {
    m: datetime.datetime.fromtimestamp(ts) for m, ts in MODEL_RELEASE_TS.items()
}


def sort_by_family(model_list):
    def _key(m):
        for prefix, order in [
            ("claude", 0),
            ("gemini", 1),
            ("gpt", 2),
            ("o3", 2),
            ("o4", 2),
        ]:
            if m.startswith(prefix):
                return (order, m)
        return (9, m)

    return sorted(model_list, key=_key)


games = sorted(grouped_df["game"].unique())

# ── T0-only subset (used for the control heatmap) ──
t0 = grouped_df[grouped_df["treatment"] == "T0: Control"]

# ── All-treatment average (used for appendix / incentive figures) ──
avg = grouped_df  # all treatments
df_avg = df  # all treatments (raw)

# ── T0 control only (used for main-paper capacity figures) ──
avg_t0 = t0
df_avg_t0 = df[df["treatment"] == "T0: Control"]

# ═══════════════════════════════════════════════════
# MAIN PAPER FIGURES  (averaged over all treatments)
# ═══════════════════════════════════════════════════

# ═══ FIG 1: Overall Accuracy by Treatment (APPENDIX) ═══
mt_acc = (
    grouped_df.groupby(["treatment", "model_short"], observed=True)["accuracy"]
    .mean()
    .reset_index()
)
t_means = mt_acc.groupby("treatment", observed=True)["accuracy"].agg(
    ["mean", "std", "count"]
)
t_means["se"] = t_means["std"] / np.sqrt(t_means["count"])
fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(
    range(len(t_means)),
    t_means["mean"] * 100,
    yerr=t_means["se"] * 100,
    color=treatment_palette,
    capsize=5,
    edgecolor="white",
    linewidth=0.5,
)
for bar, val in zip(bars, t_means["mean"] * 100):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1.5,
        f"{val:.1f}%",
        ha="center",
        va="bottom",
        fontsize=FONT["bar_label"],
    )
ax.set_xticks(range(len(t_means)))
ax.set_xticklabels(TREATMENT_ORDER, rotation=90, ha="right")
ax.set_ylabel("Mean Accuracy (%)")
ax.set_ylim(0, 100)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(OUT / "fig_appendix_overall_accuracy.pdf", bbox_inches="tight")
plt.close(fig)
print("fig1")

# ═══ FIG 1: Accuracy Heatmap (averaged over treatments) ═══
# Full annotations, ordered by accuracy: best models top, easiest games left
avg_pivot = (
    avg.pivot_table(index="model_short", columns="game", values="accuracy") * 100
)
_mean_acc = avg_pivot.mean(axis=1)
_fam_key = lambda m: (
    0 if m.startswith("claude") else (1 if m.startswith("gemini") else 2)
)
model_order_h = sorted(_mean_acc.index, key=lambda m: (_fam_key(m), -_mean_acc[m]))
game_order_h = avg_pivot.mean(axis=0).sort_values(ascending=False).index.tolist()
avg_pivot = avg_pivot.loc[model_order_h, game_order_h]
avg_pivot = _rename_games(avg_pivot)
avg_pivot["Mean"] = avg_pivot.mean(axis=1)
avg_pivot.loc["Mean"] = avg_pivot.mean(axis=0)

fig, ax = plt.subplots(figsize=(15, 10))
# Grayscale sequential ramp so the heatmaps survive black-and-white printing:
# the old Red-Yellow-Green made low (red) and high (green) collapse to nearly the
# same gray. Low value = light, high = dark; seaborn auto-picks dark/white
# annotation text per cell from the cell luminance.
_base_colors = plt.cm.Greys(np.linspace(0.10, 0.85, 256))
_cmap_light = mcolors.LinearSegmentedColormap.from_list("grays_seq", _base_colors)
# Accuracy heatmaps: pale yellow (low) -> teal -> dark blue (high)
_cmap_acc = "YlGnBu"
sns.heatmap(
    avg_pivot,
    annot=True,
    fmt=".1f",
    cmap=_cmap_acc,
    vmin=0,
    vmax=100,
    linewidths=0.3,
    linecolor="white",
    ax=ax,
    cbar_kws={"label": "Accuracy (%)", "shrink": 0.8},
    annot_kws={"size": FONT["annot"] - 2},
)
for lbl in ax.get_xticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
# Family separators
_models_h = list(avg_pivot.index)
_prev_fam = None
for _i, _m in enumerate(_models_h):
    if _m == "Mean":
        continue
    _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
    if _prev_fam is not None and _fam != _prev_fam:
        ax.axhline(y=_i, color="black", linewidth=1.5)
    _prev_fam = _fam
ax.axhline(y=len(_models_h) - 1, color="black", linewidth=1.5)
ax.axvline(x=len(avg_pivot.columns) - 1, color="black", linewidth=1.5)
ax.set_ylabel("")
ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUT / "fig1_accuracy_heatmap.pdf", bbox_inches="tight")
plt.close(fig)
print("fig1")

# ═══ FIG 1b: Net Gain Heatmap ═══
# Color = net gain ($), annotations = accuracy (%) on Mean only
_ng_h = avg.copy()
_ng_h["net_gain"] = (
    _ng_h["accuracy"] * _ng_h["n_puzzles"] * 0.25 - _ng_h["cost_per_game"]
)
ng_pivot = _ng_h.pivot_table(
    index="model_short", columns="game", values="net_gain", aggfunc="mean"
)
acc_pivot_h = (
    avg.pivot_table(index="model_short", columns="game", values="accuracy") * 100
)
ng_pivot = ng_pivot.loc[model_order_h, game_order_h]
acc_pivot_h = acc_pivot_h.loc[model_order_h, game_order_h]
ng_pivot = _rename_games(ng_pivot)
acc_pivot_h = _rename_games(acc_pivot_h)
ng_pivot["Mean"] = ng_pivot.mean(axis=1)
ng_pivot.loc["Mean"] = ng_pivot.mean(axis=0)
acc_pivot_h["Mean"] = acc_pivot_h.mean(axis=1)
acc_pivot_h.loc["Mean"] = acc_pivot_h.mean(axis=0)

annot_ng = acc_pivot_h.copy().astype(str)
for r in annot_ng.index:
    for c in annot_ng.columns:
        if r == "Mean" or c == "Mean":
            annot_ng.loc[r, c] = f"{acc_pivot_h.loc[r, c]:.0f}%"
        else:
            annot_ng.loc[r, c] = ""

fig, ax = plt.subplots(figsize=(14, 9))
sns.heatmap(
    ng_pivot,
    annot=annot_ng,
    fmt="s",
    cmap="YlGn",
    linewidths=0.3,
    linecolor="white",
    ax=ax,
    cbar_kws={"label": "Net Gain per Task ($)", "shrink": 0.8},
    annot_kws={"size": FONT["annot"], "fontweight": "bold"},
)
for lbl in ax.get_xticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
_models_ng = list(ng_pivot.index)
_prev_fam = None
for _i, _m in enumerate(_models_ng):
    if _m == "Mean":
        continue
    _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
    if _prev_fam is not None and _fam != _prev_fam:
        ax.axhline(y=_i, color="black", linewidth=1.5)
    _prev_fam = _fam
ax.axhline(y=len(_models_ng) - 1, color="black", linewidth=1.5)
ax.axvline(x=len(ng_pivot.columns) - 1, color="black", linewidth=1.5)
ax.set_ylabel("")
ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUT / "fig1b_net_gain_heatmap.pdf", bbox_inches="tight")
plt.close(fig)
print("fig1b")

# ═══ FIG 3: Task Difficulty ═══
gd = (
    avg.groupby("game", observed=True)["accuracy"]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending=True)
)
gd["se"] = gd["std"] / np.sqrt(gd["count"])
fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(
    range(len(gd)),
    gd["mean"],
    xerr=gd["se"],
    capsize=4,
    color="#4C72B0",
    edgecolor="white",
)
ax.set_yticks(range(len(gd)))
ax.set_yticklabels([GAME_LABELS.get(g, g) for g in gd.index])
ax.set_xlim(0, 1.05)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("Accuracy")
ax.grid(axis="x", alpha=0.3)
for i, (val, se) in enumerate(zip(gd["mean"], gd["se"])):
    ax.text(val + se + 0.01, i, f"{val:.1%}", va="center", fontsize=FONT["bar_label"])
fig.tight_layout()
fig.savefig(OUT / "fig3_task_difficulty.pdf", bbox_inches="tight")
plt.close(fig)
print("fig3")

# ═══ FIG 3b: Task Difficulty — Visual vs Text ═══
conn_3b = sqlite3.connect(DB)
_df_3b = pd.read_sql_query(
    """
    SELECT e.name AS experiment, r.game, p.is_correct
    FROM puzzles p
    JOIN runs r ON p.run_id = r.id
    JOIN experiments e ON r.experiment_id = e.id
    WHERE r.status = 'completed'
      AND (e.name LIKE 't_-%%'
           OR e.name LIKE 't_-%%text')
    """,
    conn_3b,
)
conn_3b.close()
_df_3b["mode"] = _df_3b["experiment"].apply(
    lambda x: "Text" if x.endswith("-text") else "Visual"
)
_acc_3b = _df_3b.groupby(["game", "mode"])["is_correct"].mean().unstack(fill_value=0)
# Sort by visual accuracy ascending
_acc_3b = _acc_3b.sort_values("Visual", ascending=True)

fig, ax = plt.subplots(figsize=(12, 6))
y = np.arange(len(_acc_3b))
h = 0.35

bars_visual = ax.barh(
    y - h / 2,
    _acc_3b["Visual"],
    h,
    color="#4C72B0",
    edgecolor="white",
    label="Visual",
)
bars_text = ax.barh(
    y + h / 2,
    _acc_3b["Text"],
    h,
    color="#DD8452",
    edgecolor="white",
    label="Text",
)
ax.set_yticks(y)
ax.set_yticklabels([GAME_LABELS.get(g, g) for g in _acc_3b.index])
ax.set_xlim(0, 1.12)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("Accuracy")
ax.grid(axis="x", alpha=0.3)
ax.legend(fontsize=FONT["legend"], loc="lower right")

for i, (v_val, t_val) in enumerate(zip(_acc_3b["Visual"], _acc_3b["Text"])):
    ax.text(
        v_val + 0.01,
        i - h / 2,
        f"{v_val:.1%}",
        va="center",
        fontsize=FONT["bar_label"] - 1,
    )
    ax.text(
        t_val + 0.01,
        i + h / 2,
        f"{t_val:.1%}",
        va="center",
        fontsize=FONT["bar_label"] - 1,
    )

fig.tight_layout()
fig.savefig(OUT / "fig3b_task_difficulty_visual_vs_text.pdf", bbox_inches="tight")
plt.close(fig)
print("fig3b")

# ═══ FIG 4: Accuracy by Model and Treatment (APPENDIX) ═══
model_order = (
    grouped_df.groupby("model_short", observed=True)["accuracy"]
    .mean()
    .sort_values(ascending=False)
    .index.tolist()
)
fig, ax = plt.subplots(figsize=(16, 8))
mt_data = (
    grouped_df.groupby(["model_short", "treatment"], observed=True)["accuracy"]
    .mean()
    .reset_index()
)
mt_data["model_short"] = pd.Categorical(
    mt_data["model_short"], categories=model_order, ordered=True
)
sns.barplot(
    data=mt_data,
    x="model_short",
    y="accuracy",
    hue="treatment",
    ax=ax,
    palette=treatment_palette,
    edgecolor="white",
    linewidth=0.5,
)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("")
ax.set_ylabel("Accuracy")
ax.tick_params(axis="x", rotation=90)
ax.legend(title="Treatment", bbox_to_anchor=(1.02, 1), loc="upper left")
fig.tight_layout()
fig.savefig(OUT / "fig_appendix_accuracy_by_model.pdf", bbox_inches="tight")
plt.close(fig)
print("fig4")

# ═══ FIG 5: Incentive Heatmaps (APPENDIX) — one file per persona ═══
acc_pivot = grouped_df.pivot_table(
    index="model_short", columns=["treatment", "game"], values="accuracy"
)
# Shared colorbar normalisation across both files for visual comparability.
# Same YlGnBu palette as the accuracy heatmaps: light (negative) -> dark blue (positive).
norm = matplotlib.colors.Normalize(vmin=-30, vmax=30)
cmap = _cmap_acc

for filename, title, t_high, t_low in [
    (
        "fig_appendix_incentive_heatmap_standard.pdf",
        "Standard Persona",
        "T2: Std Inc",
        "T1: Std No Inc",
    ),
    (
        "fig_appendix_incentive_heatmap_human.pdf",
        "Human Persona",
        "T4: Hum Inc",
        "T3: Hum No Inc",
    ),
]:
    fig, ax = plt.subplots(figsize=(15, 11))
    delta = (acc_pivot[t_high] - acc_pivot[t_low]) * 100
    # Order within families by this panel's mean incentive (highest at top)
    _panel_mean = delta.mean(axis=1)
    _panel_order = sorted(
        _panel_mean.index, key=lambda m: (_fam_key(m), -_panel_mean[m])
    )
    delta = delta.loc[
        _panel_order,
        [g for g in game_order_h if g in delta.columns],
    ]
    delta = _rename_games(delta)
    delta["Mean"] = delta.mean(axis=1)
    delta.loc["Mean"] = delta.mean(axis=0)
    sns.heatmap(
        delta,
        annot=True,
        fmt="+.1f",
        cmap=cmap,
        norm=norm,
        linewidths=0.5,
        ax=ax,
        cbar_kws={"label": "Δ Accuracy (pp)", "shrink": 0.8},
        annot_kws={"size": FONT["annot"] - 2},
    )
    for lbl in ax.get_xticklabels():
        if lbl.get_text() == "Mean":
            lbl.set_weight("bold")
    for lbl in ax.get_yticklabels():
        if lbl.get_text() == "Mean":
            lbl.set_weight("bold")
    # Family separators
    _models_inc = list(delta.index)
    _prev_fam = None
    for _i, _m in enumerate(_models_inc):
        if _m == "Mean":
            continue
        _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
        if _prev_fam is not None and _fam != _prev_fam:
            ax.axhline(y=_i, color="black", linewidth=1.5)
        _prev_fam = _fam
    ax.axhline(y=len(_models_inc) - 1, color="black", linewidth=1.5)
    ax.axvline(x=len(delta.columns) - 1, color="black", linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", rotation=90)
    fig.tight_layout()
    fig.savefig(OUT / filename, bbox_inches="tight")
    plt.close(fig)
print("fig5 (split)")

# ═══ FIG 8: Token Delta (APPENDIX) ═══
model_tokens = (
    grouped_df.groupby(["treatment", "model_short"], observed=True)[
        "total_completion_tokens"
    ]
    .mean()
    .unstack("treatment")
)
token_contrasts = {
    "Incentive (Std)": ("T2: Std Inc", "T1: Std No Inc"),
    "Incentive (Human)": ("T4: Hum Inc", "T3: Hum No Inc"),
    "Human Framing (No Inc)": ("T3: Hum No Inc", "T1: Std No Inc"),
    "Human Framing (Inc)": ("T4: Hum Inc", "T2: Std Inc"),
}
tdd = pd.DataFrame()
for label, (th, tl) in token_contrasts.items():
    tdd[label] = ((model_tokens[th] - model_tokens[tl]) / model_tokens[tl]) * 100
fig, ax = plt.subplots(figsize=(11, 6))
means = tdd.mean()
ses = tdd.std() / np.sqrt(tdd.count())
bc = [
    TREATMENT_COLORS["T2: Std Inc"],
    TREATMENT_COLORS["T2: Std Inc"],
    TREATMENT_COLORS["T3: Hum No Inc"],
    TREATMENT_COLORS["T3: Hum No Inc"],
]
ax.bar(range(len(means)), means, yerr=ses, capsize=5, color=bc, edgecolor="white")
ax.axhline(0, color="black", linewidth=0.8)
ax.set_xticks(range(len(means)))
ax.set_xticklabels(means.index, rotation=90, ha="right")
ax.set_ylabel("Completion Tokens Δ (%)")
ax.grid(axis="y", alpha=0.3)
for bar, val in zip(ax.patches, means):
    y = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        y + (0.3 if y >= 0 else -0.8),
        f"{val:+.1f}%",
        ha="center",
        va="bottom" if y >= 0 else "top",
        fontsize=FONT["bar_label"],
    )
fig.tight_layout()
fig.savefig(OUT / "fig_appendix_token_delta.pdf", bbox_inches="tight")
plt.close(fig)
print("fig8")

# ═══ FIG 9: Bubble Chart ═══
ms = (
    avg.groupby("model_short", observed=True)
    .agg(
        accuracy=("accuracy", "mean"),
        cost_per_game=("cost_per_game", "mean"),
        tokens_per_game=("total_tokens", "mean"),
    )
    .reset_index()
)
ms = ms.sort_values(
    "model_short", key=lambda s: s.map(lambda m: sort_by_family([m])[0])
)
fig, ax = plt.subplots(figsize=(16, 12))
ss = 1000 / ms["tokens_per_game"].max()
# Plot bubbles with abbreviation labels
for _, row in ms.iterrows():
    ax.scatter(
        row["cost_per_game"],
        row["accuracy"],
        s=row["tokens_per_game"] * ss,
        color=MODEL_COLORS.get(row["model_short"], "#888"),
        alpha=0.95,
        edgecolors="white",
        linewidth=0.5,
        zorder=3,
    )
    # Offset above bubble: radius in points = sqrt(s) / 2
    bubble_s = row["tokens_per_game"] * ss
    radius_pt = np.sqrt(bubble_s) / 2
    ax.annotate(
        MODEL_ABBREV.get(row["model_short"], row["model_short"]),
        (row["cost_per_game"], row["accuracy"]),
        fontsize=11,
        ha="center",
        va="bottom",
        xytext=(0, radius_pt + 4),
        textcoords="offset points",
    )
# Pareto frontier: models where no other model is both cheaper and more accurate
_pareto = ms.sort_values("cost_per_game").copy()
_front = []
_best_acc = -1
for _, row in _pareto.iterrows():
    if row["accuracy"] > _best_acc:
        _front.append(row)
        _best_acc = row["accuracy"]
_front = pd.DataFrame(_front)
# Draw frontier as straight lines, extended to the most expensive model
_front_x = list(_front["cost_per_game"].values)
_front_y = list(_front["accuracy"].values)
_gemini_pro_cost = ms.loc[ms["model_short"] == "gemini-3.1-pro", "cost_per_game"].values
if len(_gemini_pro_cost):
    _front_x.append(_gemini_pro_cost[0])
    _front_y.append(_front_y[-1])
ax.plot(
    _front_x,
    _front_y,
    color="gray",
    linewidth=1.5,
    linestyle="--",
    alpha=0.6,
    zorder=2,
    label="Pareto frontier",
)

ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("Avg per-task cost ($)")
ax.set_ylabel("Accuracy")
ax.grid(alpha=0.3)
# Tokens/task legend (bubble sizes)
from matplotlib.lines import Line2D

token_handles = []
for t_val in [10000, 20000, 40000]:
    token_handles.append(
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="gray",
            alpha=0.4,
            markersize=np.sqrt(t_val * ss),
            label=f"{t_val // 1000}k",
        )
    )
leg_tokens = ax.legend(
    handles=token_handles,
    title="Tokens/task",
    ncol=1,
    fontsize=FONT["legend"],
    title_fontsize=FONT["legend_title"],
    loc="upper left",
    bbox_to_anchor=(1.01, 1.0),
    framealpha=0.9,
    borderpad=1.0,
    handletextpad=1.0,
    labelspacing=1.0,
)
ax.add_artist(leg_tokens)
# Model legend below plot
leg_models = model_abbrev_legend(
    ax,
    ncol=4,
    fontsize=FONT["legend"],
    loc="upper center",
    bbox_to_anchor=(0.5, -0.09),
    framealpha=0.9,
)
fig.savefig(
    OUT / "fig9_bubble_chart.pdf",
    bbox_extra_artists=[leg_tokens, leg_models],
    bbox_inches="tight",
)
plt.close(fig)
print("fig9")

# ═══ FIG 10: Cost Heatmap ═══
cpg = (
    avg.groupby(["model_short", "game"], observed=True)["cost_per_game"]
    .mean()
    .reset_index()
)
cpivot = cpg.pivot(index="model_short", columns="game", values="cost_per_game")
cpivot = cpivot.loc[sort_by_family(cpivot.index)]
cpivot = _rename_games(cpivot)
cpivot["Mean"] = cpivot.mean(axis=1)
cpivot.loc["Mean"] = cpivot.mean(axis=0)
fig, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(
    cpivot,
    annot=True,
    fmt=".3f",
    cmap="YlOrRd",
    linewidths=0.5,
    ax=ax,
    cbar_kws={"label": "Cost per Task ($)"},
    annot_kws={"size": FONT["annot"]},
)
for lbl in ax.get_xticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
ax.set_ylabel("")
ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUT / "fig10_cost_heatmap.pdf", bbox_inches="tight")
plt.close(fig)
print("fig10")

# ═══ FIG 11: Family Evolution (1×3 subplots — LARGER) ═══
families = {
    "OpenAI (GPT)": [
        m
        for m in MODEL_RELEASE_DATE
        if m.startswith("gpt-") or m.startswith("o3") or m.startswith("o4")
    ],
    "Anthropic (Claude)": [m for m in MODEL_RELEASE_DATE if m.startswith("claude-")],
    "Google (Gemini)": [m for m in MODEL_RELEASE_DATE if m.startswith("gemini-")],
}
for fam in families:
    families[fam] = sorted(families[fam], key=lambda m: MODEL_RELEASE_TS[m])
model_accuracy = df_avg.groupby("model_short")["is_correct"].mean()
family_colors = {
    "OpenAI (GPT)": "#389840",
    "Anthropic (Claude)": "#C08418",
    "Google (Gemini)": "#3078C0",
}

fig, axes = plt.subplots(1, 3, figsize=(22, 8), sharey=True)
for ax, (fam_name, models) in zip(axes, families.items()):
    accs = [model_accuracy.get(m, 0) for m in models]
    dates = [MODEL_RELEASE_DATE[m].strftime("%b %Y") for m in models]
    labels = [f"{m}\n({d})" for m, d in zip(models, dates)]
    bar_colors = [MODEL_COLORS.get(m, "#888888") for m in models]
    bars = ax.bar(
        range(len(models)), accs, color=bar_colors, edgecolor="white", linewidth=0.5
    )
    ax.set_xticks(range(len(models)))
    ax.set_xticklabels(labels, rotation=90, ha="center")
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.set_ylabel("Accuracy" if ax == axes[0] else "")
    ax.set_title(fam_name, color=family_colors[fam_name])
    ax.grid(axis="y", alpha=0.3)
    for bar, val in zip(bars, accs):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{val:.1%}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"],
        )
fig.tight_layout()
fig.savefig(OUT / "fig11_family_evolution.pdf", bbox_inches="tight")
plt.close(fig)
print("fig11")

# ═══ FIG 11b: Family Evolution — Image vs Text (APPENDIX) ═══
# Requires text-mode data; load it if available
_text_experiments = [
    "t0-control",
    "t1-standard-no-incentive",
    "t2-standard-incentive",
    "t3-human-no-incentive",
    "t4-human-incentive",
    "t0-control-text",
    "t1-standard-no-incentive-text",
    "t2-standard-incentive-text",
    "t3-human-no-incentive-text",
    "t4-human-incentive-text",
]
_text_exp_mode = {}
for e in _text_experiments:
    _text_exp_mode[e] = "Text" if e.endswith("-text") else "Image"

_text_exp_list = ", ".join(f"'{e}'" for e in _text_experiments)
conn = sqlite3.connect(DB)
_df_ivt = pd.read_sql_query(
    f"""
    SELECT e.name AS experiment, r.model, r.game, p.is_correct,
           COALESCE(r.is_text, 0) AS is_text
    FROM puzzles p
    JOIN runs r ON p.run_id = r.id
    JOIN experiments e ON r.experiment_id = e.id
    WHERE r.status = 'completed' AND e.name IN ({_text_exp_list})
    """,
    conn,
)
conn.close()
_df_ivt["mode"] = _df_ivt["experiment"].map(_text_exp_mode)
_df_ivt["model_short"] = (
    _df_ivt["model"].str.rsplit("/", n=1).str[-1].map(_clean_model_name)
)

model_acc_img = (
    _df_ivt[_df_ivt["mode"] == "Image"].groupby("model_short")["is_correct"].mean()
)
model_acc_text = (
    _df_ivt[_df_ivt["mode"] == "Text"].groupby("model_short")["is_correct"].mean()
)

fig, axes = plt.subplots(1, 3, figsize=(22, 8), sharey=True)
family_colors_ivt = {
    "OpenAI (GPT)": "#389840",
    "Anthropic (Claude)": "#C08418",
    "Google (Gemini)": "#3078C0",
}
from matplotlib.patches import Patch

for ax, (fam_name, models) in zip(axes, families.items()):
    accs_img = [model_acc_img.get(m, 0) for m in models]
    accs_text = [model_acc_text.get(m, 0) for m in models]
    dates = [MODEL_RELEASE_DATE[m].strftime("%b %Y") for m in models]
    labels = [f"{m}\n({d})" for m, d in zip(models, dates)]

    x = np.arange(len(models))
    width = 0.38

    ax.bar(
        x - width / 2,
        accs_img,
        width,
        color=[MODEL_COLORS.get(m, "#888") for m in models],
        edgecolor="white",
        linewidth=0.5,
        alpha=0.5,
    )
    ax.bar(
        x + width / 2,
        accs_text,
        width,
        color=[MODEL_COLORS.get(m, "#888") for m in models],
        edgecolor="white",
        linewidth=0.5,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90, ha="right", fontsize=FONT["tick"] - 4)
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.set_ylabel("Accuracy" if ax == axes[0] else "")
    ax.set_title(
        fam_name, fontsize=FONT["title"] - 4, color=family_colors_ivt[fam_name]
    )
    ax.grid(axis="y", alpha=0.3)
    if ax == axes[0]:
        ax.legend(
            handles=[
                Patch(facecolor="gray", alpha=0.5, edgecolor="white", label="Image"),
                Patch(facecolor="gray", alpha=1.0, edgecolor="white", label="Text"),
            ],
            fontsize=FONT["legend"] - 2,
            loc="upper left",
        )

    for i, (vi, vt) in enumerate(zip(accs_img, accs_text)):
        ax.text(
            i - width / 2,
            vi + 0.01,
            f"{vi:.0%}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"] - 4,
            alpha=0.6,
        )
        ax.text(
            i + width / 2,
            vt + 0.01,
            f"{vt:.0%}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"] - 4,
        )

fig.tight_layout()
fig.savefig(OUT / "fig_appendix_family_evolution_img_vs_text.pdf", bbox_inches="tight")
plt.close(fig)
print("fig11b")

# ═══ FIG 12: Accuracy vs Completion Tokens ═══
model_tok = (
    avg.groupby("model_short", observed=True)
    .agg(
        accuracy=("accuracy", "mean"),
        avg_completion=("total_completion_tokens", "mean"),
    )
    .reset_index()
)
model_tok = model_tok.sort_values(
    "model_short", key=lambda s: s.map(lambda m: sort_by_family([m])[0])
)
fig, ax = plt.subplots(figsize=(16, 12))
for _, row in model_tok.iterrows():
    ax.scatter(
        row["avg_completion"],
        row["accuracy"],
        s=180,
        color=MODEL_COLORS.get(row["model_short"], "#888888"),
        edgecolors="white",
        linewidth=0.5,
        zorder=3,
    )
    ax.annotate(
        MODEL_ABBREV.get(row["model_short"], row["model_short"]),
        (row["avg_completion"], row["accuracy"]),
        fontsize=11,
        ha="center",
        va="bottom",
        xytext=(0, 9),
        textcoords="offset points",
    )
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("Avg Completion Tokens per Task")
ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{x/1000:.0f}k"))
ax.set_ylabel("Accuracy")
ax.grid(alpha=0.3)
leg = model_abbrev_legend(
    ax,
    ncol=4,
    fontsize=FONT["legend"],
    loc="upper center",
    bbox_to_anchor=(0.5, -0.12),
    framealpha=0.9,
)
fig.savefig(
    OUT / "fig12_accuracy_vs_tokens.pdf", bbox_extra_artists=[leg], bbox_inches="tight"
)
plt.close(fig)
print("fig12")

# ═══ Appendix: Cost per Model (bar chart) ═══
model_cost_order = (
    avg.groupby("model_short", observed=True)["cost_per_game"]
    .mean()
    .sort_values(ascending=True)
    .index.tolist()
)
model_avg_cost = avg.groupby("model_short", observed=True)["cost_per_game"].agg(
    ["mean", "std", "count"]
)
model_avg_cost = model_avg_cost.loc[model_cost_order]
model_avg_cost["se"] = model_avg_cost["std"] / np.sqrt(model_avg_cost["count"])

fig, ax = plt.subplots(figsize=(14, 8))
bar_colors = [MODEL_COLORS.get(m, "#888888") for m in model_avg_cost.index]
ax.barh(
    range(len(model_avg_cost)),
    model_avg_cost["mean"],
    xerr=model_avg_cost["se"],
    capsize=3,
    color=bar_colors,
    edgecolor="white",
    linewidth=0.5,
)
ax.set_yticks(range(len(model_avg_cost)))
ax.set_yticklabels(model_avg_cost.index)
ax.set_xlabel("Avg per-task cost ($)")
ax.grid(axis="x", alpha=0.3)
for i, (val, se) in enumerate(zip(model_avg_cost["mean"], model_avg_cost["se"])):
    ax.text(
        val + se + 0.001,
        i,
        f"${val:.3f}",
        va="center",
        fontsize=FONT["bar_label"],
    )
fig.tight_layout()
fig.savefig(OUT / "fig_appendix_cost_per_model.pdf", bbox_inches="tight")
plt.close(fig)
print("appendix_cost_per_model")

# ═══ Net Gain per Model (averaged over all treatments) ═══
_ng = avg.copy()
_ng["net_gain"] = _ng["accuracy"] * _ng["n_puzzles"] * 0.25 - _ng["cost_per_game"]

_net_mean = _ng.groupby("model_short", observed=True)["net_gain"].mean()
_net_order = sorted(_net_mean.index, key=lambda m: (_fam_key(m), -_net_mean[m]))
net_model = _net_mean.reindex(_net_order)

# Optimal participant: best model per task, average the net gains
_ng_per_game = _ng.groupby(["model_short", "game"], observed=True)["net_gain"].mean()
_best_per_game = _ng_per_game.groupby("game").max()
_smart_ng = _best_per_game.mean()

# Append smart adversary as an extra entry
labels = list(net_model.index) + ["Optimal participant"]
values = list(net_model.values) + [_smart_ng]

fig, ax = plt.subplots(figsize=(10, 8))
y = np.arange(len(labels))
bar_colors = [MODEL_COLORS.get(m, "#888888") for m in net_model.index] + ["#E03030"]
ax.barh(y, values, color=bar_colors, edgecolor="white", linewidth=0.5)
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=9)
# Bold the smart adversary label
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Optimal participant":
        lbl.set_weight("bold")
        lbl.set_color("#E03030")
ax.axvline(0, color="black", lw=0.8)
ax.set_xlabel("Net gain per task ($)")
ax.grid(axis="x", alpha=0.3)
for i, val in enumerate(values):
    offset = 0.05 if val >= 0 else -0.05
    ha = "left" if val >= 0 else "right"
    fw = "bold" if i == len(values) - 1 else "normal"
    ax.text(
        val + offset, i, f"${val:.2f}", va="center", ha=ha, fontsize=8, fontweight=fw
    )
xmin, xmax = ax.get_xlim()
margin = (xmax - xmin) * 0.12
ax.set_xlim(xmin - margin, xmax + margin)
fig.tight_layout()
fig.savefig(OUT / "fig_net_gain_avg.pdf", bbox_inches="tight")
plt.close(fig)
print("net_gain_avg")

# ═══ Net Gain per Task by Model × Game ═══
net_model_game = (
    _ng.groupby(["model_short", "game"], observed=True)["net_gain"].mean().reset_index()
)
_games = sorted(net_model_game["game"].unique())
family_order = sort_by_family(net_model_game["model_short"].unique().tolist())

ncols = 4
nrows = int(np.ceil(len(_games) / ncols))
fig, axes = plt.subplots(nrows, ncols, figsize=(20, nrows * 5), sharey=True)
axes_flat = axes.flatten()

xmin, xmax = 0.0, 0.0
for idx, game in enumerate(_games):
    ax = axes_flat[idx]
    gdata = net_model_game[net_model_game["game"] == game].copy()
    gdata = (
        gdata.set_index("model_short").reindex(family_order).dropna(subset=["net_gain"])
    )
    y = np.arange(len(gdata))
    bar_colors = [MODEL_COLORS.get(m, "#888888") for m in gdata.index]
    ax.barh(y, gdata["net_gain"], color=bar_colors, edgecolor="white", linewidth=0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(gdata.index, fontsize=8)
    ax.set_title(GAME_LABELS.get(game, game), fontsize=11, fontweight="bold")
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlabel("Net gain per task ($)")
    ax.grid(axis="x", alpha=0.3)
    for i, val in enumerate(gdata["net_gain"]):
        offset = 0.05 if val >= 0 else -0.05
        ha = "left" if val >= 0 else "right"
        ax.text(val + offset, i, f"${val:.2f}", va="center", ha=ha, fontsize=7)
    # Add margins so annotations fit
    _xmin, _xmax = ax.get_xlim()
    if _xmin < xmin:
        xmin = _xmin
    if _xmax > xmax:
        xmax = _xmax

margin = (xmax - xmin) * 0.1
for ax in axes_flat[: len(_games)]:
    ax.set_xlim(xmin - margin, xmax + margin)

fig.tight_layout()
fig.savefig(OUT / "fig_net_gain_per_game.pdf", bbox_inches="tight")
plt.close(fig)
print("net_gain_per_game")

# ═══════════════════════════════════════════════════
# T0-ONLY CAPACITY FIGURES  (main paper)
# ═══════════════════════════════════════════════════

# ── T0 Accuracy Heatmap ──
_t0_pivot = (
    avg_t0.pivot_table(index="model_short", columns="game", values="accuracy") * 100
)
_t0_mean_acc = _t0_pivot.mean(axis=1)
_t0_model_order = sorted(
    _t0_mean_acc.index, key=lambda m: (_fam_key(m), -_t0_mean_acc[m])
)
_t0_game_order = _t0_pivot.mean(axis=0).sort_values(ascending=False).index.tolist()
_t0_pivot = _t0_pivot.loc[_t0_model_order, _t0_game_order]
_t0_pivot = _rename_games(_t0_pivot)
_t0_pivot["Mean"] = _t0_pivot.mean(axis=1)
_t0_pivot.loc["Mean"] = _t0_pivot.mean(axis=0)

fig, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(
    _t0_pivot,
    annot=True,
    fmt=".1f",
    cmap=_cmap_acc,
    vmin=0,
    vmax=100,
    linewidths=0.3,
    linecolor="white",
    ax=ax,
    cbar_kws={"label": "Accuracy (%)", "shrink": 0.8},
    annot_kws={"size": FONT["annot"] - 2},
)
for lbl in ax.get_xticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
_models_t0h = list(_t0_pivot.index)
_prev_fam = None
for _i, _m in enumerate(_models_t0h):
    if _m == "Mean":
        continue
    _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
    if _prev_fam is not None and _fam != _prev_fam:
        ax.axhline(y=_i, color="black", linewidth=1.5)
    _prev_fam = _fam
ax.axhline(y=len(_models_t0h) - 1, color="black", linewidth=1.5)
ax.axvline(x=len(_t0_pivot.columns) - 1, color="black", linewidth=1.5)
ax.set_ylabel("")
ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUT / "fig1_t0_accuracy_heatmap.pdf", bbox_inches="tight")
plt.close(fig)
print("fig1_t0")

# ── T0 Accuracy Heatmap WITH a human-benchmark row ──
# Same construction as fig1_t0, but appends a HUMAN row. Human accuracy on each
# task uses ALL participants who attempted that task (matched_only=False), not
# only the both-days matched intersection: per-participant accuracy averaged
# over participants, symmetric with the per-model LLM rows.
_hh_pivot = (
    avg_t0.pivot_table(index="model_short", columns="game", values="accuracy") * 100
)
_hh_mean_acc = _hh_pivot.mean(axis=1)
_hh_model_order = sorted(
    _hh_mean_acc.index, key=lambda m: (_fam_key(m), -_hh_mean_acc[m])
)
_hh_game_order = _hh_pivot.mean(axis=0).sort_values(ascending=False).index.tolist()
_hh_pivot = _hh_pivot.loc[_hh_model_order, _hh_game_order]

_hum_all = load_human_trials(matched_only=False)
_n_hum_all = _hum_all["email"].nunique()
_hum_pp = _hum_all.groupby(["email", "game"])["is_correct"].mean().reset_index()
_hum_task = _hum_pp.groupby("game")["is_correct"].mean() * 100
_human_row = _hum_task.reindex(_hh_game_order)  # align to LLM column (game) order

_hh_pivot = _rename_games(_hh_pivot)
_human_row.index = [GAME_LABELS.get(g, g) for g in _hh_game_order]

_hh_pivot["Mean"] = _hh_pivot.mean(axis=1)
_llm_mean = _hh_pivot.mean(axis=0)
_human_full = _human_row.reindex(_hh_pivot.columns[:-1])
_human_full["Mean"] = _human_row.mean()
_human_label = "Human"
_hh_pivot.loc["Mean"] = _llm_mean
_hh_pivot.loc[_human_label] = _human_full
# Human as the first (top) row, then models by family, then the LLM Mean row
_hh_pivot = _hh_pivot.reindex([_human_label] + list(_hh_model_order) + ["Mean"])

fig, ax = plt.subplots(figsize=(15, 10.5))
sns.heatmap(
    _hh_pivot,
    annot=True,
    fmt=".1f",
    cmap=_cmap_acc,
    vmin=0,
    vmax=100,
    linewidths=0.3,
    linecolor="white",
    ax=ax,
    cbar_kws={"label": "Accuracy (%)", "shrink": 0.8},
    annot_kws={"size": FONT["annot"] - 2},
)
for lbl in ax.get_xticklabels():
    if lbl.get_text() == "Mean":
        lbl.set_weight("bold")
for lbl in ax.get_yticklabels():
    if lbl.get_text() in ("Mean", _human_label):
        lbl.set_weight("bold")
_models_hh = [m for m in _hh_pivot.index if m not in ("Mean", _human_label)]
_n_models_hh = len(_models_hh)
_prev_fam = None
for _i, _m in enumerate(_models_hh):
    _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
    if _prev_fam is not None and _fam != _prev_fam:
        ax.axhline(y=_i + 1, color="black", linewidth=1.5)  # +1: Human occupies row 0
    _prev_fam = _fam
ax.axhline(y=1, color="black", linewidth=1.5)  # Human | models
ax.axhline(y=_n_models_hh + 1, color="black", linewidth=1.5)  # models | Mean
ax.axvline(x=len(_hh_pivot.columns) - 1, color="black", linewidth=1.5)
ax.set_ylabel("")
ax.set_xlabel("")
fig.tight_layout()
fig.savefig(OUT / "fig1_t0_accuracy_heatmap_human.pdf", bbox_inches="tight")
plt.close(fig)
print("fig1_t0_human")

# ── T0 Task Difficulty (LLM vs Human) ──
# LLM bar: mean (± SE) over the 23 models of per-model T0 accuracy on each task.
_t0_gd = (
    avg_t0.groupby("game", observed=True)["accuracy"]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending=True)
)
_t0_gd["se"] = _t0_gd["std"] / np.sqrt(_t0_gd["count"])
# Human bar: mean (± SE) over all participants of per-participant accuracy on each
# task (everyone who attempted it, not just the both-days intersection) —
# symmetric with the LLM (one accuracy value per agent per task).
_hum_trials = load_human_trials(matched_only=False)
_hum_pg = _hum_trials.groupby(["email", "game"])["is_correct"].mean().reset_index()
_hum_gd = _hum_pg.groupby("game")["is_correct"].agg(["mean", "std", "count"])
_hum_gd["se"] = _hum_gd["std"] / np.sqrt(_hum_gd["count"])

# Per-task LLM-vs-human difference p-values, taken verbatim from Table
# tab:avg_llm_hum (ALL participants). Regenerate the table — and these values —
# with paper/reestimate_llm_vs_human.py if the human sample changes.
_llm_hum_pval = {
    "add_numbers": 0.005,
    "counting_zeros": 0.0,
    "string_entry": 0.0,
    "sudoku_game": 0.0,
    "task_decoding": 0.717,
    "task_sequences": 0.0,
    "task_summation": 0.072,
    "task_transcription": 0.0,
}


def _fmt_pval(p):
    return "p < 0.001" if p < 0.001 else f"p = {p:.3f}"


_game_order = _t0_gd.index.tolist()
_y = np.arange(len(_game_order))
_bh = 0.4
_llm_m, _llm_se = _t0_gd["mean"].values, _t0_gd["se"].values
_hum_m = _hum_gd["mean"].reindex(_game_order).values
_hum_se = _hum_gd["se"].reindex(_game_order).values

fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(
    _y - _bh / 2,
    _hum_m,
    _bh,
    color="#DD8452",
    edgecolor="white",
    label="Human",
)
ax.barh(
    _y + _bh / 2,
    _llm_m,
    _bh,
    color="#4C72B0",
    edgecolor="white",
    label="LLM",
)
ax.set_yticks(_y)
ax.set_yticklabels([GAME_LABELS.get(g, g) for g in _game_order])
ax.set_xlim(0, 1.32)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xticks(np.arange(0, 1.01, 0.2))  # cap axis at 100%; p-value column sits beyond
ax.set_xlabel("Accuracy")
ax.grid(axis="x", alpha=0.3)
ax.grid(axis="y", visible=False)  # no horizontal gridlines
_leg = ax.legend(
    fontsize=FONT["legend"],
    ncol=2,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.16),
    framealpha=0.9,
)
for i in range(len(_game_order)):
    ax.text(
        _hum_m[i] + 0.01,
        i - _bh / 2,
        f"{_hum_m[i]:.1%}",
        va="center",
        fontsize=FONT["bar_label"] - 1,
    )
    ax.text(
        _llm_m[i] + 0.01,
        i + _bh / 2,
        f"{_llm_m[i]:.1%}",
        va="center",
        fontsize=FONT["bar_label"] - 1,
    )
    # LLM-vs-human difference p-value (Table tab:avg_llm_hum), right-aligned column
    ax.text(
        1.30,
        i,
        _fmt_pval(_llm_hum_pval[_game_order[i]]),
        va="center",
        ha="right",
        fontsize=FONT["bar_label"] - 1,
        color="#333333",
    )
fig.savefig(
    OUT / "fig3_t0_task_difficulty.pdf",
    bbox_extra_artists=[_leg],
    bbox_inches="tight",
)
plt.close(fig)
print("fig3_t0")

# ── T0 Bubble Chart ──
_t0_ms = (
    avg_t0.groupby("model_short", observed=True)
    .agg(
        accuracy=("accuracy", "mean"),
        cost_per_game=("cost_per_game", "mean"),
        tokens_per_game=("total_tokens", "mean"),
    )
    .reset_index()
)
_t0_ms = _t0_ms.sort_values(
    "model_short", key=lambda s: s.map(lambda m: sort_by_family([m])[0])
)
fig, ax = plt.subplots(figsize=(16, 12))
_t0_ss = 1000 / _t0_ms["tokens_per_game"].max()
for _, row in _t0_ms.iterrows():
    ax.scatter(
        row["cost_per_game"],
        row["accuracy"],
        s=row["tokens_per_game"] * _t0_ss,
        color=MODEL_COLORS.get(row["model_short"], "#888"),
        alpha=0.95,
        edgecolors="white",
        linewidth=0.5,
        zorder=3,
    )
    bubble_s = row["tokens_per_game"] * _t0_ss
    radius_pt = np.sqrt(bubble_s) / 2
    ax.annotate(
        MODEL_ABBREV.get(row["model_short"], row["model_short"]),
        (row["cost_per_game"], row["accuracy"]),
        fontsize=14,
        ha="center",
        va="bottom",
        xytext=(0, radius_pt + 4),
        textcoords="offset points",
    )
# Pareto frontier
_t0_pareto = _t0_ms.sort_values("cost_per_game").copy()
_t0_front = []
_t0_best_acc = -1
for _, row in _t0_pareto.iterrows():
    if row["accuracy"] > _t0_best_acc:
        _t0_front.append(row)
        _t0_best_acc = row["accuracy"]
_t0_front = pd.DataFrame(_t0_front)
_t0_front_x = list(_t0_front["cost_per_game"].values)
_t0_front_y = list(_t0_front["accuracy"].values)
_t0_gemini_pro_cost = _t0_ms.loc[
    _t0_ms["model_short"] == "gemini-3.1-pro", "cost_per_game"
].values
if len(_t0_gemini_pro_cost):
    _t0_front_x.append(_t0_gemini_pro_cost[0])
    _t0_front_y.append(_t0_front_y[-1])
ax.plot(
    _t0_front_x,
    _t0_front_y,
    color="gray",
    linewidth=1.5,
    linestyle="--",
    alpha=0.6,
    zorder=2,
    label="Pareto frontier",
)

ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_xlabel("Avg per-task cost ($)")
ax.set_ylabel("Accuracy")
ax.grid(alpha=0.3)
from matplotlib.lines import Line2D

_t0_token_handles = []
for t_val in [10000, 20000, 40000]:
    _t0_token_handles.append(
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="gray",
            alpha=0.4,
            markersize=np.sqrt(t_val * _t0_ss),
            label=f"{t_val // 1000}k",
        )
    )
leg_tokens = ax.legend(
    handles=_t0_token_handles,
    title="Tokens/task",
    ncol=1,
    fontsize=FONT["legend"],
    title_fontsize=FONT["legend_title"],
    loc="upper left",
    bbox_to_anchor=(1.01, 1.0),
    framealpha=0.9,
    borderpad=1.0,
    handletextpad=1.0,
    labelspacing=1.0,
)
ax.add_artist(leg_tokens)
leg_models = model_abbrev_legend(
    ax,
    ncol=4,
    fontsize=FONT["legend"],
    loc="upper center",
    bbox_to_anchor=(0.5, -0.09),
    framealpha=0.9,
)
fig.savefig(
    OUT / "fig9_t0_bubble_chart.pdf",
    bbox_extra_artists=[leg_tokens, leg_models],
    bbox_inches="tight",
)
plt.close(fig)
print("fig9_t0")

# ── T0 Family Evolution ──
_t0_model_accuracy = df_avg_t0.groupby("model_short")["is_correct"].mean()
fig, axes = plt.subplots(1, 3, figsize=(22, 8), sharey=True)
for ax, (fam_name, models) in zip(axes, families.items()):
    accs = [_t0_model_accuracy.get(m, 0) for m in models]
    dates = [MODEL_RELEASE_DATE[m].strftime("%b %Y") for m in models]
    labels = [f"{m}\n({d})" for m, d in zip(models, dates)]
    bar_colors = [MODEL_COLORS.get(m, "#888888") for m in models]
    bars = ax.bar(
        range(len(models)), accs, color=bar_colors, edgecolor="white", linewidth=0.5
    )
    ax.set_xticks(range(len(models)))
    ax.set_xticklabels(labels, rotation=90, ha="center")
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.set_ylabel("Accuracy" if ax == axes[0] else "")
    ax.set_title(fam_name, color=family_colors[fam_name])
    ax.grid(axis="y", alpha=0.3)
    for bar, val in zip(bars, accs):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{val:.1%}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"],
        )
fig.tight_layout()
fig.savefig(OUT / "fig11_t0_family_evolution.pdf", bbox_inches="tight")
plt.close(fig)
print("fig11_t0")

# ── T0 Net Gain per Model ──
_t0_ng = avg_t0.copy()
_t0_ng["net_gain"] = (
    _t0_ng["accuracy"] * _t0_ng["n_puzzles"] * 0.25 - _t0_ng["cost_per_game"]
)
_t0_net_mean = _t0_ng.groupby("model_short", observed=True)["net_gain"].mean()
_t0_net_order = sorted(
    _t0_net_mean.index, key=lambda m: (_fam_key(m), -_t0_net_mean[m])
)
_t0_net_model = _t0_net_mean.reindex(_t0_net_order)

# Optimal participant
_t0_ng_per_game = _t0_ng.groupby(["model_short", "game"], observed=True)[
    "net_gain"
].mean()
_t0_best_per_game = _t0_ng_per_game.groupby("game").max()
_t0_smart_ng = _t0_best_per_game.mean()

labels = list(_t0_net_model.index) + ["Optimal participant"]
values = list(_t0_net_model.values) + [_t0_smart_ng]

fig, ax = plt.subplots(figsize=(10, 8))
y = np.arange(len(labels))
bar_colors = (
    [MODEL_COLORS.get(m, "#888888") for m in _t0_net_model.index]
    + ["#E03030"]
)
ax.barh(y, values, color=bar_colors, edgecolor="white", linewidth=0.5)
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=9)
for lbl in ax.get_yticklabels():
    if lbl.get_text() == "Optimal participant":
        lbl.set_weight("bold")
        lbl.set_color("#E03030")
ax.axvline(0, color="black", lw=0.8)
ax.set_xlabel("Net gain per task ($)")
ax.grid(axis="x", alpha=0.3)
for i, val in enumerate(values):
    offset = 0.05 if val >= 0 else -0.05
    ha = "left" if val >= 0 else "right"
    fw = "bold" if i >= len(values) - 1 else "normal"
    ax.text(
        val + offset, i, f"${val:.2f}", va="center", ha=ha, fontsize=8, fontweight=fw
    )
xmin, xmax = ax.get_xlim()
margin = (xmax - xmin) * 0.12
ax.set_xlim(xmin - margin, xmax + margin)
fig.tight_layout()
fig.savefig(OUT / "fig_t0_net_gain_avg.pdf", bbox_inches="tight")
plt.close(fig)
print("net_gain_t0")

# ── T0 Cost per Model ──
_t0_cost_order = (
    avg_t0.groupby("model_short", observed=True)["cost_per_game"]
    .mean()
    .sort_values(ascending=True)
    .index.tolist()
)
_t0_cost = avg_t0.groupby("model_short", observed=True)["cost_per_game"].agg(
    ["mean", "std", "count"]
)
_t0_cost = _t0_cost.loc[_t0_cost_order]
_t0_cost["se"] = _t0_cost["std"] / np.sqrt(_t0_cost["count"])
fig, ax = plt.subplots(figsize=(14, 8))
bar_colors = [MODEL_COLORS.get(m, "#888888") for m in _t0_cost.index]
ax.barh(
    range(len(_t0_cost)),
    _t0_cost["mean"],
    xerr=_t0_cost["se"],
    capsize=3,
    color=bar_colors,
    edgecolor="white",
    linewidth=0.5,
)
ax.set_yticks(range(len(_t0_cost)))
ax.set_yticklabels(_t0_cost.index)
ax.set_xlabel("Avg per-task cost ($)")
ax.grid(axis="x", alpha=0.3)
for i, (val, se) in enumerate(zip(_t0_cost["mean"], _t0_cost["se"])):
    ax.text(val + se + 0.001, i, f"${val:.3f}", va="center", fontsize=FONT["bar_label"])
fig.tight_layout()
fig.savefig(OUT / "fig_t0_appendix_cost_per_model.pdf", bbox_inches="tight")
plt.close(fig)
print("cost_t0")

# ═══════════════════════════════════════════════════
# APPENDIX FIGURES  (multi-treatment / comparisons)
# ═══════════════════════════════════════════════════

# ═══ Appendix Heatmaps ═══
for treatment in TREATMENT_ORDER[1:]:
    t_data = grouped_df[grouped_df["treatment"] == treatment]
    pivot = (
        t_data.pivot_table(index="model_short", columns="game", values="accuracy") * 100
    )
    _t_mean_acc = pivot.mean(axis=1)
    _t_model_order = sorted(
        _t_mean_acc.index, key=lambda m: (_fam_key(m), -_t_mean_acc[m])
    )
    pivot = pivot.loc[_t_model_order, game_order_h]
    pivot = _rename_games(pivot)
    pivot["Mean"] = pivot.mean(axis=1)
    pivot.loc["Mean"] = pivot.mean(axis=0)
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".1f",
        cmap=_cmap_acc,
        vmin=0,
        vmax=100,
        linewidths=0.3,
        linecolor="white",
        ax=ax,
        cbar_kws={"label": "Accuracy (%)", "shrink": 0.8},
        annot_kws={"size": FONT["annot"] - 2},
    )
    for lbl in ax.get_xticklabels():
        if lbl.get_text() == "Mean":
            lbl.set_weight("bold")
    for lbl in ax.get_yticklabels():
        if lbl.get_text() == "Mean":
            lbl.set_weight("bold")
    # Family separators
    _models_app = list(pivot.index)
    _prev_fam = None
    for _i, _m in enumerate(_models_app):
        if _m == "Mean":
            continue
        _fam = 0 if _m.startswith("claude") else (1 if _m.startswith("gemini") else 2)
        if _prev_fam is not None and _fam != _prev_fam:
            ax.axhline(y=_i, color="black", linewidth=1.5)
        _prev_fam = _fam
    ax.axhline(y=len(_models_app) - 1, color="black", linewidth=1.5)
    ax.axvline(x=len(pivot.columns) - 1, color="black", linewidth=1.5)
    ax.set_ylabel("")
    ax.set_xlabel("")
    fig.tight_layout()
    tag = treatment.split(":")[0].strip().lower()
    fig.savefig(OUT / f"fig_appendix_heatmap_{tag}.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"appendix_{tag}")

# ═══ FIG: Accuracy vs Release Date (METR-style) ═══
from scipy import stats as sp_stats

# Mean accuracy per model (T0 control only, across tasks)
_model_acc = (
    t0.groupby("model_short", observed=True)["accuracy"]
    .agg(["mean", "std", "count"])
    .rename(columns={"mean": "accuracy"})
)
_model_acc["se"] = _model_acc["std"] / np.sqrt(_model_acc["count"])

# Attach release dates
_model_acc["release_date"] = _model_acc.index.map(lambda m: MODEL_RELEASE_DATE.get(m))
_model_acc = _model_acc.dropna(subset=["release_date"])
_model_acc["date_num"] = _model_acc["release_date"].apply(
    lambda d: matplotlib.dates.date2num(d)
)


# Family assignment
def _family(m):
    if m.startswith("claude"):
        return "Anthropic"
    elif m.startswith("gemini"):
        return "Google"
    else:
        return "OpenAI"


_model_acc["family"] = _model_acc.index.map(_family)
FAMILY_COLORS = {
    "Anthropic": "#C08418",
    "Google": "#3078C0",
    "OpenAI": "#389840",
}
FAMILY_MARKERS = {
    "Anthropic": "D",
    "Google": "s",
    "OpenAI": "o",
}

# Linear regression
slope, intercept, r_value, p_value, std_err = sp_stats.linregress(
    _model_acc["date_num"], _model_acc["accuracy"]
)

fig, ax = plt.subplots(figsize=(16, 9))

# Confidence band
x_fit = np.linspace(
    _model_acc["date_num"].min() - 30, _model_acc["date_num"].max() + 30, 200
)
y_fit = slope * x_fit + intercept
n = len(_model_acc)
x_mean = _model_acc["date_num"].mean()
se_fit = std_err * np.sqrt(
    1 / n + (x_fit - x_mean) ** 2 / ((n - 1) * _model_acc["date_num"].std() ** 2)
)
ax.fill_between(
    [matplotlib.dates.num2date(x) for x in x_fit],
    y_fit - 1.96 * se_fit,
    y_fit + 1.96 * se_fit,
    alpha=0.15,
    color="gray",
)
ax.plot(
    [matplotlib.dates.num2date(x) for x in x_fit],
    y_fit,
    color="gray",
    linewidth=2,
    linestyle="--",
    label="_nolegend_",
)

# Scatter with error bars, per family
for fam in ["Anthropic", "Google", "OpenAI"]:
    sub = _model_acc[_model_acc["family"] == fam]
    ax.errorbar(
        sub["release_date"],
        sub["accuracy"],
        yerr=sub["se"],
        fmt=FAMILY_MARKERS[fam],
        color=FAMILY_COLORS[fam],
        markersize=10,
        markeredgecolor="white",
        markeredgewidth=0.8,
        capsize=3,
        linewidth=0,
        elinewidth=1.2,
        label=fam,
        zorder=5,
    )

# Labels for each point (auto-repelled)
_texts = []
for m, row in _model_acc.iterrows():
    abbr = MODEL_ABBREV.get(m, m)
    _texts.append(
        ax.text(
            matplotlib.dates.date2num(row["release_date"]),
            row["accuracy"],
            abbr,
            fontsize=FONT["annot"] - 2,
            color=FAMILY_COLORS.get(row["family"], "#888"),
        )
    )
adjust_text(
    _texts,
    ax=ax,
    arrowprops=dict(arrowstyle="-", color="gray", alpha=0.2, lw=0.4),
    expand=(2.5, 3.0),
    force_text=(2.5, 3.0),
    force_points=(2.0, 2.0),
    force_objects=(1.0, 1.0),
    ensure_inside_axes=True,
    max_move=50,
    iterations=800,
    only_move={"text": "xy", "static": "xy", "explode": "xy", "pull": "xy"},
    min_arrow_len=12,
)

ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_ylabel("Accuracy")
ax.set_xlabel("Model release date")
ax.set_ylim(0.4, 1.0)
ax.grid(axis="both", alpha=0.3)


# Family legend below plot (3 columns, no trend entry)
leg_main = ax.legend(
    fontsize=FONT["legend"],
    ncol=3,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.1),
    framealpha=0.9,
)
ax.add_artist(leg_main)
leg_models = model_abbrev_legend(
    ax,
    ncol=4,
    fontsize=FONT["legend"],
    loc="upper center",
    bbox_to_anchor=(0.5, -0.17),
    framealpha=0.9,
    use_family_colors=True,
)
ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(bymonth=[1, 4, 7, 10]))
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %Y"))
ax.tick_params(axis="x", rotation=0)
fig.savefig(
    OUT / "fig_accuracy_vs_release_date.pdf",
    bbox_extra_artists=[leg_main, leg_models],
    bbox_inches="tight",
)
plt.close(fig)
print("fig_accuracy_vs_release_date")

# ═══ FIG: Accuracy by Tier within Family ═══
# Define tiers per family, ordered from highest to lowest tier
_TIERS = {
    "Anthropic": {
        "Opus": ["claude-opus-4.5", "claude-opus-4.6"],
        "Sonnet": [
            "claude-sonnet-3.7",
            "claude-sonnet-4",
            "claude-sonnet-4.5",
            "claude-sonnet-4.6",
        ],
        "Haiku": ["claude-haiku-4.5"],
    },
    "Google": {
        "Pro": ["gemini-2.5-pro", "gemini-3.1-pro"],
        "Flash": ["gemini-2.5-flash", "gemini-3-flash"],
        "Flash Lite": ["gemini-2.5-flash-lite", "gemini-3.1-flash-lite"],
    },
    "OpenAI": {
        "GPT-5": ["gpt-5", "gpt-5.1", "gpt-5.2", "gpt-5.4"],
        "Mini": ["gpt-5-mini", "gpt-5.4-mini"],
        "Nano": ["gpt-5.4-nano"],
        "o-series": ["o3", "o4-mini", "o4-mini-high"],
    },
}

# Get T0 accuracy per model
_tier_acc = t0.groupby("model_short", observed=True)["accuracy"].mean()

# Sort models within each tier by release date (newest first)
for fam in _TIERS:
    for tier in _TIERS[fam]:
        _TIERS[fam][tier] = sorted(
            _TIERS[fam][tier],
            key=lambda m: MODEL_RELEASE_TS.get(m, 0),
            reverse=True,
        )

FAMILY_PLOT_COLORS = {
    "Anthropic": "#C08418",
    "Google": "#3078C0",
    "OpenAI": "#389840",
}

fig, axes = plt.subplots(1, 3, figsize=(20, 9), sharey=True)

for ax, (fam, tiers) in zip(axes, _TIERS.items()):
    fam_color = FAMILY_PLOT_COLORS[fam]
    positions = []
    labels = []
    colors = []
    values = []
    tier_boundaries = []
    tier_labels = []
    pos = 0

    for tier_name, models in tiers.items():
        tier_start = pos
        n = len(models)
        for i, m in enumerate(models):
            acc = _tier_acc.get(m, 0)
            # Fade older models, saturate newer ones (newest = index 0 = darkest)
            alpha = 1.0 - 0.6 * (i / max(n - 1, 1))
            positions.append(pos)
            labels.append(MODEL_ABBREV.get(m, m))
            values.append(acc)
            colors.append(alpha)
            pos += 1
        tier_mid = (tier_start + pos - 1) / 2
        tier_labels.append((tier_mid, tier_name))
        pos += 0.8  # gap between tiers
        tier_boundaries.append(pos - 0.4)

    bars = ax.bar(
        positions,
        values,
        color=[(*matplotlib.colors.to_rgb(fam_color), a) for a in colors],
        edgecolor="white",
        linewidth=0.8,
        width=0.7,
    )

    # Value labels on bars
    for p, v in zip(positions, values):
        ax.text(
            p,
            v + 0.01,
            f"{v:.1%}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"] - 2,
        )

    ax.set_xticks(positions)
    ax.set_xticklabels(
        [m for tier_models in tiers.values() for m in tier_models],
        rotation=90,
        ha="center",
        fontsize=FONT["tick"] - 3,
    )
    ax.set_ylim(0.45, 0.9)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.set_ylabel("Accuracy" if ax == axes[0] else "")
    ax.set_title(fam, fontsize=FONT["title"], color=fam_color, pad=15)
    ax.grid(axis="y", alpha=0.3)

    # Tier labels below x-axis labels
    for mid, tname in tier_labels:
        ax.text(
            mid,
            -0.38,
            tname,
            ha="center",
            va="top",
            fontsize=FONT["legend"],
            fontweight="bold",
            transform=ax.get_xaxis_transform(),
        )

    # Vertical separators between tiers
    for b in tier_boundaries[:-1]:
        ax.axvline(x=b, color="gray", linewidth=0.8, linestyle=":", alpha=0.5)

# Arrow annotation: darker = newer
from matplotlib.patches import FancyArrowPatch

fig.text(
    0.5,
    0.05,
    r"Darker $\rightarrow$ newer release within each tier",
    ha="center",
    fontsize=FONT["legend"],
    fontstyle="italic",
    color="gray",
)

fig.tight_layout()
fig.savefig(OUT / "fig_accuracy_by_tier.pdf", bbox_inches="tight")
plt.close(fig)
print("fig_accuracy_by_tier")

# ═══ Cost by Tier (T0 control, mirrors fig_accuracy_by_tier) ═══
# Total API cost per model under T0: sum of cost_per_game across all 8 tasks
# (i.e., total spend for 20 runs × 8 tasks = 160 puzzles per model)
_tier_cost = t0.groupby("model_short", observed=True)["cost_per_game"].sum()

fig, axes = plt.subplots(1, 3, figsize=(20, 9), sharey=True)

# Use log scale since costs span >2 orders of magnitude
for ax in axes:
    ax.set_yscale("log")

for ax, (fam, tiers) in zip(axes, _TIERS.items()):
    fam_color = FAMILY_PLOT_COLORS[fam]
    positions = []
    labels = []
    colors = []
    values = []
    tier_boundaries = []
    tier_labels = []
    pos = 0

    for tier_name, models in tiers.items():
        tier_start = pos
        n = len(models)
        for i, m in enumerate(models):
            cost = _tier_cost.get(m, 0)
            # Fade older models, saturate newer ones (newest = index 0 = darkest)
            alpha = 1.0 - 0.6 * (i / max(n - 1, 1))
            positions.append(pos)
            labels.append(MODEL_ABBREV.get(m, m))
            values.append(cost)
            colors.append(alpha)
            pos += 1
        tier_mid = (tier_start + pos - 1) / 2
        tier_labels.append((tier_mid, tier_name))
        pos += 0.8  # gap between tiers
        tier_boundaries.append(pos - 0.4)

    bars = ax.bar(
        positions,
        values,
        color=[(*matplotlib.colors.to_rgb(fam_color), a) for a in colors],
        edgecolor="white",
        linewidth=0.8,
        width=0.7,
    )

    # Value labels on bars (dollar amounts)
    for p, v in zip(positions, values):
        ax.text(
            p,
            v * 1.08,
            f"\\${v:.2f}" if v >= 0.01 else f"\\${v:.3f}",
            ha="center",
            va="bottom",
            fontsize=FONT["bar_label"] - 2,
        )

    ax.set_xticks(positions)
    ax.set_xticklabels(
        [m for tier_models in tiers.values() for m in tier_models],
        rotation=90,
        ha="center",
        fontsize=FONT["tick"] - 3,
    )
    ax.set_ylabel("Total cost for 20 runs × 8 tasks (\\$)" if ax == axes[0] else "")
    ax.set_title(fam, fontsize=FONT["title"], color=fam_color, pad=15)
    ax.grid(axis="y", alpha=0.3, which="both")
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("$%.2f"))

    # Tier labels below x-axis labels
    for mid, tname in tier_labels:
        ax.text(
            mid,
            -0.38,
            tname,
            ha="center",
            va="top",
            fontsize=FONT["legend"],
            fontweight="bold",
            transform=ax.get_xaxis_transform(),
        )

    # Vertical separators between tiers
    for b in tier_boundaries[:-1]:
        ax.axvline(x=b, color="gray", linewidth=0.8, linestyle=":", alpha=0.5)

# Shared y-limits across all three axes for easier cross-family comparison
_all_values = [
    _tier_cost.get(m, 0)
    for fam in _TIERS
    for tier in _TIERS[fam].values()
    for m in tier
]
_ymax = max(v for v in _all_values if v > 0) * 2
_ymin = min(v for v in _all_values if v > 0) * 0.5
for ax in axes:
    ax.set_ylim(_ymin, _ymax)

fig.text(
    0.5,
    0.05,
    r"Darker $\rightarrow$ newer release within each tier",
    ha="center",
    fontsize=FONT["legend"],
    fontstyle="italic",
    color="gray",
)

fig.tight_layout()
fig.savefig(OUT / "fig_cost_by_tier.pdf", bbox_inches="tight")
plt.close(fig)
print("fig_cost_by_tier")

print("\nAll figures saved to paper/imgs/")
