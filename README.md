# Artificial Effort

Benchmarking suite for the paper **"Artificial Effort"** (Belotti, Coniglio, Cosma, Fallucchi).

We evaluate frontier LLMs on ten real-effort tasks under a 2×2 experimental design of **persona** (standard vs. human) × **incentive** (with vs. without monetary bonus), plus a silent control. Tasks are implemented as [oTree](https://www.otree.org/) apps so they can also be played by human participants; the benchmark script calls [OpenRouter](https://openrouter.ai/) directly and does not require a running oTree server.

## Project structure

```
real_effort/
├── real_effort/                      # Python package (also an oTree project)
│   ├── add_numbers/                  # Puzzle modules — each exposes
│   ├── count_numbers/                #   generate_puzzle_fields(),
│   ├── counting_zeros/               #   render_image(), render_text(),
│   ├── task_decoding/                #   is_correct(response, puzzle)
│   ├── task_sequences/               # (+ oTree pages for the human experiment)
│   ├── task_summation/
│   ├── task_transcription/
│   ├── sudoku_game/
│   ├── slider_puzzle/
│   ├── string_entry/
│   ├── config/
│   │   └── benchmark_config.yaml     # Single source of truth for benchmark settings
│   ├── reports/                      # SQLite results DB + per-experiment reports
│   ├── run_benchmarks.py             # Main benchmark runner (direct OpenRouter)
│   ├── run_parallel.sh               # Parallel wrapper (one process per model)
│   ├── export_results.py             # Dump results.db → JSON for pandas
│   ├── summary_stats.py              # Aggregate stats from results.db
│   ├── plot_results.py               # Quick matplotlib plots from melted CSV
│   └── settings.py                   # oTree session configs
├── paper/                            # LaTeX source + figures + figure scripts
└── pyproject.toml
```

## Tasks

| Task | Modality | Description |
|------|----------|-------------|
| `add_numbers` | Image | Sum three three-digit numbers |
| `count_numbers` | Image | Count occurrences of a target digit in a matrix |
| `counting_zeros` | Image | Count zeros in a paragraph of 1s and 0s |
| `task_decoding` | Image | Decode a digit sequence using a letter↔digit lookup table |
| `task_sequences` | Text | Predict the next number in an arithmetic/geometric sequence |
| `task_summation` | Image | Find two cells of a grid that sum to a target value |
| `task_transcription` | Image | Transcribe distorted alphanumeric text |
| `sudoku_game` | Image | Fill in a 6×6 Sudoku |
| `slider_puzzle` | Image | Produce a move sequence that solves a 3×3 sliding-tile puzzle |
| `string_entry` | Image | Transcribe a string of special characters (including spaces) |

All image tasks have a mirror `--text-only` mode that feeds a textual representation of the puzzle to models that either cannot see images or for which we want to isolate the vision component.

## Experimental design

Each benchmark run is parameterized by:

- **Persona** — `standard` (LLM is addressed as a puzzle solver) or `human` (LLM is told it is a human participant in an academic experiment).
- **Incentive** — `true` (compensation text is shown, e.g. "$0.50 per correct answer") or `explicit_none` (prompt explicitly states no compensation). There is also a `control` persona that keeps the prompt silent on both identity and compensation.

The five treatments reported in the paper are:

| Code | Persona | Incentive mention |
|------|---------|-------------------|
| T0 (control) | silent | silent |
| T1 | standard | explicitly none |
| T2 | standard | compensation shown |
| T3 | human | explicitly none |
| T4 | human | compensation shown |

## Requirements

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/)
- An [OpenRouter](https://openrouter.ai/) API key

No browser or oTree server is needed for benchmarking — `run_benchmarks.py` calls OpenRouter directly and renders puzzle images in-process with Pillow. The oTree server is only needed if you want to run the experiment with human participants.

## Installation

```bash
git clone <repo-url>
cd real-effort
uv sync
export OPENROUTER_API_KEY=sk-or-...
```

## Running the LLM benchmark

All settings live in [`real_effort/config/benchmark_config.yaml`](real_effort/config/benchmark_config.yaml) — the models list, sampling parameters, reasoning effort, per-game puzzle parameters, and treatment defaults. CLI flags override YAML values.

### Single-process run

```bash
cd real_effort

# Run everything in the YAML (all models × all games), sequentially
uv run python run_benchmarks.py

# Subset of games / models
uv run python run_benchmarks.py \
  --models google/gemini-3-flash-preview openai/gpt-5-mini \
  --games add_numbers sudoku_game

# Text-only variant (sends textual puzzle representations instead of images)
uv run python run_benchmarks.py --text-only

# Specify a treatment explicitly
uv run python run_benchmarks.py --persona human --incentive true
```

### Parallel runs (recommended)

`run_parallel.sh` launches one worker process per model, sharing a single experiment (and a single SQLite DB row per run) so the workers don't collide. The folder name becomes the experiment name; if a run with that name already exists the wrapper auto-resumes it.

```bash
# Auto-named folder from tier + incentive, all models from YAML
./run_parallel.sh

# Explicit folder + overrides
./run_parallel.sh t4-human-incentive --tier high --persona human --incentive true

# Text-only variant of T1
./run_parallel.sh t1-standard-no-incentive-text \
  --tier high --persona standard --incentive explicit_none --text-only
```

Per-worker logs are written to `reports/<experiment-name>/<model-short>.log`.

### Resume and iteration

Experiments and per-run state are stored in `real_effort/reports/results.db` (SQLite). To resume an interrupted experiment or re-run only failed cells:

```bash
uv run python run_benchmarks.py --resume <experiment-name>
```

Adding new `--models` or `--games` on resume extends the experiment with additional runs without touching completed ones.

### Key CLI options

| Option | Description |
|--------|-------------|
| `--config PATH` | Alternate YAML config |
| `--models M [M ...]` | Override the YAML model list |
| `--games G [G ...]` | Games to run (use `all` for every game) |
| `--persona {standard,human,control}` | Prompt persona |
| `--incentive {true,false,explicit_none}` | Whether/how compensation is mentioned |
| `--text-only` | Send textual puzzle representations instead of images |
| `--reasoning-effort {xhigh,high,medium,low,minimal,none}` | Reasoning budget as a fraction of `max_tokens` |
| `--reasoning-max-tokens INT` | Hard cap on reasoning tokens (overrides effort) |
| `--max-tokens INT` | Total output budget (reasoning + answer, per OpenRouter) |
| `--temperature FLOAT` / `--top-p FLOAT` | Sampling |
| `--repetitions INT` | Repetitions per (model, game) cell |
| `--run-delay FLOAT` | Sleep between runs (rate-limit protection) |
| `--max-retries INT` | Max retries per failed run |
| `--resume NAME` | Resume an existing experiment |
| `--experiment-name NAME` | Custom experiment name (default: UTC timestamp) |
| `--report-dir PATH` | Output directory for reports |

Run `uv run python run_benchmarks.py --help` for the complete list.

## Results and analysis

Every run writes to `real_effort/reports/results.db`. Each experiment gets a folder under `real_effort/reports/<experiment-name>/` with a full JSON export and per-model markdown reports (token usage, accuracy, per-puzzle detail).

Analysis helpers (all read-only against `results.db`):

```bash
# Export one or more experiments to JSON for pandas
uv run python export_results.py --experiment t4-human-incentive

# Aggregate summary statistics (accuracy, tokens, cost) as table or CSV
uv run python summary_stats.py -e t4-human-incentive

# Paper figures
uv run python paper/gen_paper_figs.py
```

## Running the human experiment (oTree)

The same puzzle modules are wired into oTree apps for recruiting human participants.

```bash
cd real_effort
uv run otree devserver             # http://localhost:8000
```

Session configs are defined in `real_effort/settings.py`; each puzzle task is a live-method oTree app with the same `is_correct` logic used by the benchmark.

## Citation

If you use this code or data, please cite:

> Belotti, F., Coniglio, S., Cosma, A., & Fallucchi, F. (2026). *Artificial Effort*. Working paper.

## License

MIT
