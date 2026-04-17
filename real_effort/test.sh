#!/usr/bin/env bash
set -euo pipefail

MODEL="qwen/qwen3.5-397b-a17b"
GAME="sudoku_game"

run() {
  local name="$1"; shift
  echo "=== $name ==="
  python run_benchmarks.py --models "$MODEL" --games "$GAME" "$@" --repetitions 1 --experiment-name "$name" --no-reload
  echo ""
}

# Baseline: no reasoning
run qwen-no-reasoning        --reasoning-effort none --max-tokens 2048

# Effort levels (auto-converted to reasoning.max_tokens in code)
run qwen-effort-minimal      --reasoning-effort minimal --max-tokens 2048
run qwen-effort-low          --reasoning-effort low     --max-tokens 2048
run qwen-effort-medium       --reasoning-effort medium  --max-tokens 2048
run qwen-effort-high         --reasoning-effort high    --max-tokens 2048

# Explicit reasoning_max_tokens (does Qwen respect them?)
run qwen-rmt128              --reasoning-max-tokens 128  --max-tokens 2048
run qwen-rmt256              --reasoning-max-tokens 256  --max-tokens 2048
run qwen-rmt512              --reasoning-max-tokens 512  --max-tokens 2048
run qwen-rmt1024             --reasoning-max-tokens 1024 --max-tokens 2048

# Higher max_tokens to give room for both reasoning + answer
run qwen-rmt1024-mt4096      --reasoning-max-tokens 1024 --max-tokens 4096
run qwen-effort-high-mt4096  --reasoning-effort high     --max-tokens 4096
