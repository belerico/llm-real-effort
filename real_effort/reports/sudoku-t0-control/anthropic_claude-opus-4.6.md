# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-05-18 11:56:05

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **sudoku_game**: difficulty=0.4

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8060 | 31272 | 39332 | 13 | 7 | 24.88 | 497.86 |
| **TOTAL** | **8060** | **31272** | **39332** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 3 6 2 2 4 3 5 5 4 3 1 6 | 2 5 3 6 2 2 4 3 5 5 4 3 1 6 | Yes | 26.5 |
| 2 | 1 6 3 6 2 5 2 1 4 3 1 1 5 6 | 1 6 3 6 2 5 2 1 4 3 1 1 5 6 | Yes | 18.61 |
| 3 | 1 3 1 4 6 2 3 4 4 2 1 6 4 3 | 1 3 1 4 6 2 3 4 4 2 1 6 4 3 | Yes | 21.08 |
| 4 | 6 5 4 3 6 2 6 4 6 5 3 4 3 5 | 6 5 4 3 6 2 1 6 4 6 5 2 4 3 5 2 6 | No | 26.0 |
| 5 | 1 3 1 4 5 1 5 3 4 5 6 1 3 2 | 1 3 1 4 5 1 5 3 4 5 6 1 3 2 | Yes | 22.15 |
| 6 | 5 6 3 4 3 1 4 2 1 4 6 6 4 1 | Looking at this puzzle, I need to find all missing numbers by analyzing rows, columns, and 2×3 boxes.  **Row-by-row analysis:**  **Row 2** (_, 2, _, 1, _, _): Needs {3,4,5,6} - C6 can only be 4 (C6 has 6,_,_,3,5,2 → needs 1,4; row needs 3,4,5,6 → **4**) - This means R3C6 = **1** - R3C3 = **3** (Row 3 only needs 3) - C3 now needs {2,6} → R2C3 must be **6** (row needs 3,5,6), R5C3 = **2** - R2C1 = **5**, R2C5 = **3** (remaining for row 2)  **Row 4** (_, 6, 1, _, 5, 3): Needs {2,4} - C1 already has {3,5,2} → R4C1 = **4** - R4C4 = **2**  **Row 6** (_, 3, 5, _, _, 2): C4 needs 4 → R6C4 = **4**  **Rows 5 & 6 remaining:** - Row 5: (_, 4, 2, 3, _, 5) needs {1,6} - Row 6: (_, 3, | No | 33.54 |
| 7 | 4 1 3 1 4 3 6 5 4 1 2 2 1 3 | 4 1 3 1 4 3 6 5 4 1 2 2 1 3 | Yes | 24.28 |
| 8 | 4 5 2 1 1 3 6 4 5 1 4 1 1 2 | 4 5 2 1 1 3 6 4 5 1 4 1 6 1 2 | No | 25.88 |
| 9 | 2 4 3 1 4 2 6 1 6 5 6 2 2 3 | 2 4 3 1 4 2 6 1 6 5 6 2 2 3 | Yes | 23.42 |
| 10 | 3 1 5 4 3 5 1 6 4 1 2 3 1 4 | 3 1 5 4 3 5 1 6 4 1 2 3 1 4 2 | No | 25.48 |
| 11 | 1 5 3 2 5 1 4 3 4 3 6 1 6 4 | 1 5 3 2 5 1 4 3 4 3 6 1 6 4 | Yes | 31.76 |
| 12 | 2 6 3 1 5 5 1 1 2 1 5 5 4 1 | 2 6 3 1 5 5 1 1 2 1 5 4 1Endtml | No | 27.84 |
| 13 | 3 4 6 1 5 4 1 6 4 3 1 5 3 4 | 3 4 6 1 5 4 1 6 4 3 1 5 3 4 | Yes | 22.6 |
| 14 | 1 5 5 1 4 4 6 2 5 6 3 6 4 1 | 1 5 5 1 4 4 6 2 5 6 3 6 4 1 | Yes | 20.58 |
| 15 | 5 3 1 5 6 4 5 1 2 2 2 3 1 5 | 5 3 1 5 6 4 5 1 2 2 2 3 1 5 | Yes | 24.82 |
| 16 | 4 1 6 5 6 1 2 2 5 1 6 5 6 1 | 4 1 6 5 6 1 2 2 5 1 6 5 6 1 | Yes | 24.62 |
| 17 | 3 3 4 3 4 5 1 5 3 4 1 4 6 1 | 3 3 4 4 5 1 5 3 4 1 4 6 1 2 | No | 32.66 |
| 18 | 1 5 6 2 4 5 1 2 5 3 4 2 3 3 | 1 5 6 2 4 5 1 2 5 3 4 2 3 3 3 | No | 21.75 |
| 19 | 5 2 4 3 1 2 1 3 5 2 3 5 2 6 | 5 2 4 3 1 2 1 3 5 2 3 5 2 6 | Yes | 21.29 |
| 20 | 4 3 4 6 5 3 2 5 4 2 6 2 5 3 | 4 3 4 6 5 3 2 5 4 2 6 2 5 3 | Yes | 22.79 |
