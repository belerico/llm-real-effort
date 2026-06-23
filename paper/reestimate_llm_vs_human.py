#!/usr/bin/env python3
"""Re-estimate the LLM-vs-human task-difficulty LPM (Tables tab:lm_llm_hum and
tab:avg_llm_hum) from data, comparing the both-days MATCHED human sample with
the ALL-participants sample.

Model (accuracy in percentage points, one row per agent x task):

    acc_{a,t} = b0 + Task'b + LLM*g + (Task x LLM)'d + e

    - LLM agents: per-model T0 (t0-control) accuracy, one value per (model, task).
    - Human agents: per-participant accuracy, one value per (participant, task).
    - Reference task = Addition; LLM = 1 for models, 0 for humans.

tab:lm_llm_hum = the full coefficient table.
tab:avg_llm_hum = the per-task average marginal effect of LLM, i.e. the linear
combination (LLM + Task_t x LLM), tested with res.t_test.

Read-only on the DB and the human CSVs. Run from repo root:
    uv run python paper/reestimate_llm_vs_human.py
"""

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "real_effort" / "reports" / "results_orig.db"
HUMAN_DIR = ROOT / "human-exps"

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
# Row order used in the paper tables (Addition is the reference / intercept).
TASK_ORDER = [
    "add_numbers",
    "counting_zeros",
    "string_entry",
    "sudoku_game",
    "task_decoding",
    "task_sequences",
    "task_summation",
    "task_transcription",
]
HUMAN_EMAIL_ALIASES = {
    "c.vendra@unibg.it": "c.vendra@studenti.unibg.it",
    "a.bergamaschi04@gmail.com": "a.bergamaschi7@studenti.unibg.it",
    "matty.rossi100@gmail.com": "m.rossi111@studenti.unibg.it",
}


def llm_t0_accuracy():
    """Per-(model, game) T0 accuracy in percentage points (one row per agent x task)."""
    con = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
    df = pd.read_sql_query(
        "SELECT r.model, r.game, p.is_correct "
        "FROM puzzles p JOIN runs r ON p.run_id=r.id "
        "JOIN experiments e ON r.experiment_id=e.id "
        "WHERE r.status='completed' AND e.name='t0-control'",
        con,
    )
    con.close()
    df["is_correct"] = pd.to_numeric(df["is_correct"], errors="coerce").fillna(0)
    g = df.groupby(["model", "game"])["is_correct"].mean().reset_index()
    g["acc"] = g["is_correct"] * 100.0
    g["LLM"] = 1
    return g[["game", "acc", "LLM"]]


def human_accuracy(matched_only):
    """Per-(participant, game) accuracy in percentage points."""

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
            out["participant_label"].astype(str).str.strip().str.lower().replace(
                HUMAN_EMAIL_ALIASES
            )
        )
        return out

    day1 = _read_day(HUMAN_DIR / "day-1")
    day2 = _read_day(HUMAN_DIR / "day-2")
    hum = pd.concat([day1, day2], ignore_index=True)
    hum = hum[hum["email"].str.contains("@", na=False)].copy()
    if matched_only:
        matched = set(day1["email"]) & set(day2["email"])
        hum = hum[hum["email"].isin(matched)].copy()
    hum["is_correct"] = pd.to_numeric(hum["is_correct"], errors="coerce").fillna(0)
    pp = hum.groupby(["email", "game"])["is_correct"].mean().reset_index()
    pp["acc"] = pp["is_correct"] * 100.0
    pp["LLM"] = 0
    return pp[["game", "acc", "LLM"]], hum["email"].nunique()


def fit(matched_only):
    llm = llm_t0_accuracy()
    hum, n_hum = human_accuracy(matched_only)
    data = pd.concat([llm, hum], ignore_index=True)
    data["game"] = pd.Categorical(data["game"], categories=TASK_ORDER, ordered=True)
    res = smf.ols("acc ~ C(game, Treatment('add_numbers')) * LLM", data=data).fit()
    return res, n_hum


def marginal_effects(res):
    """Per-task average marginal effect of LLM = LLM + (Task_t x LLM)."""
    names = res.params.index
    rows = []
    for t in TASK_ORDER:
        c = pd.Series(0.0, index=names)
        c["LLM"] = 1.0
        if t != "add_numbers":
            inter = f"C(game, Treatment('add_numbers'))[T.{t}]:LLM"
            c[inter] = 1.0
        tt = res.t_test(c.values)
        rows.append(
            {
                "Task": GAME_LABELS[t],
                "Estimate": float(np.ravel(tt.effect)[0]),
                "SE": float(np.ravel(tt.sd)[0]),
                "Stat": float(np.ravel(tt.tvalue)[0]),
                "P": float(np.ravel(tt.pvalue)[0]),
            }
        )
    return pd.DataFrame(rows)


def _term_label(name):
    if name == "Intercept":
        return "Intercept"
    if name == "LLM":
        return "LLM"
    is_inter = name.endswith(":LLM")
    base = name[: -len(":LLM")] if is_inter else name
    for t in TASK_ORDER[1:]:
        if base.endswith(f"[T.{t}]"):
            lab = f"Task: {GAME_LABELS[t]}"
            return f"{lab} x LLM" if is_inter else lab
    return name


def coef_table(res):
    """Full coefficient table (tab:lm_llm_hum) in the paper's row order."""
    order = (
        ["Intercept"]
        + [f"C(game, Treatment('add_numbers'))[T.{t}]" for t in TASK_ORDER[1:]]
        + ["LLM"]
        + [f"C(game, Treatment('add_numbers'))[T.{t}]:LLM" for t in TASK_ORDER[1:]]
    )
    rows = []
    for nm in order:
        rows.append(
            {
                "Term": _term_label(nm),
                "Estimate": res.params[nm],
                "SE": res.bse[nm],
                "Stat": res.tvalues[nm],
                "P": res.pvalues[nm],
            }
        )
    return pd.DataFrame(rows)


def main():
    for matched_only in (True, False):
        tag = "MATCHED (both-days)" if matched_only else "ALL participants"
        res, n_hum = fit(matched_only)
        print("\n" + "=" * 72)
        print(f"{tag}:  humans={n_hum},  N obs={int(res.nobs)},  R^2={res.rsquared:.3f}")
        print("-- tab:avg_llm_hum  (per-task marginal effect of LLM) --")
        me = marginal_effects(res)
        for _, r in me.iterrows():
            print(
                f"  {r['Task']:<26} {r['Estimate']:7.1f} {r['SE']:6.1f} "
                f"{r['Stat']:7.1f} {r['P']:8.3f}"
            )
        if not matched_only:
            print("-- tab:lm_llm_hum  (full coefficients) --")
            for _, r in coef_table(res).iterrows():
                print(
                    f"  {r['Term']:<30} {r['Estimate']:7.1f} {r['SE']:6.1f} "
                    f"{r['Stat']:7.1f} {r['P']:8.3f}"
                )


if __name__ == "__main__":
    main()
