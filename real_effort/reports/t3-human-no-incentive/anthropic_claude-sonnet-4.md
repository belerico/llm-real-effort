# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-19 03:13:48

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **sudoku_game**: difficulty=0.4
- **add_numbers**: num_addends=3, max_digits=3
- **counting_zeros**: rows=15, cols=10, min_zeros=35, max_zeros=75
- **task_decoding**: word_length=7
- **task_summation**: grid_size=4, target_sum=10.0
- **task_transcription**: length=12

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8740 | 38449 | 47189 | 3 | 17 | 26.83 | 536.71 |
| add_numbers | 4660 | 3623 | 8283 | 20 | 0 | 3.19 | 63.85 |
| counting_zeros | 7220 | 31161 | 38381 | 7 | 13 | 23.17 | 463.85 |
| task_decoding | 14040 | 9140 | 23180 | 19 | 1 | 7.12 | 142.47 |
| task_summation | 7960 | 17238 | 25198 | 20 | 0 | 10.55 | 211.13 |
| task_transcription | 4816 | 3605 | 8421 | 17 | 3 | 4.38 | 87.74 |
| task_sequences | 3920 | 8681 | 12601 | 18 | 2 | 6.05 | 121.07 |
| **TOTAL** | **51356** | **111897** | **163253** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 3 4 6 1 5 1 5 4 2 1 5 6 4 | 2 3 4 1 6 5 1 5 4 2 1 5 6 4 | No | 24.1 |
| 2 | 3 2 1 3 5 6 2 5 3 5 3 2 4 5 |  | No | 27.96 |
| 3 | 3 2 4 5 6 3 1 6 5 6 3 1 2 2 | 3 2 4 5 6 3 1 6 5 2 3 1 6 2 | No | 22.29 |
| 4 | 3 5 4 3 4 3 1 1 4 5 6 3 2 1 |  | No | 26.55 |
| 5 | 5 3 1 2 6 1 5 4 2 6 1 3 1 3 |  | No | 26.44 |
| 6 | 2 6 4 3 5 6 4 1 3 2 3 6 4 2 |  | No | 27.58 |
| 7 | 5 2 4 6 2 6 1 4 5 3 6 4 1 1 | 2 6 4 5 2 1 6 4 5 3 6 4 1 1 | No | 26.7 |
| 8 | 6 5 1 3 6 1 3 6 3 1 1 2 4 5 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in reading order.  Let me solve this step by step:  First, I'll identify the easiest cells to fill: - Row 5 has: _, 4, 5, 6, 3, 2 → missing only | No | 28.19 |
| 9 | 2 4 3 3 6 4 2 3 2 5 6 3 3 2 |  | No | 28.87 |
| 10 | 3 2 1 4 4 6 1 2 6 4 3 1 3 2 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically using the constraints that each row, column, and 2×3 box must contain numbers 1-6 exactly once.  Let me work through this step by step:  Row 1: _  4  2  5  1  6 Missing: 3, so (1,1) = 3  Row 3: 6  _  _  3  _  5 Looking at column constraints and row needs: - Column 5 is missing 3,4 and row 3 needs 1,2,4, so (3,5) = 4 - This leaves positions (3,2) and (3,3) needing 1,2 - Column 3 constraints give us (3,3) = 1, so (3,2) = 2  Row 4: _  3 | No | 30.04 |
| 11 | 4 4 1 3 3 2 4 3 2 5 4 3 1 1 | 4 4 1 3 3 2 4 3 2 5 4 3 1 1 | Yes | 24.39 |
| 12 | 1 6 2 2 3 1 5 1 6 3 3 1 4 5 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers following the rules that each row, column, and 2×3 box contains numbers 1-6 exactly once.  Let me solve systematically:  Row 1: Missing 1, 2, 6 in positions 1, 4, 6 Row 3: Missing 1, 2, 3 in positions 2, 4, 6   Row 4: Missing 1, 5, 6 in positions 1, 2, 3 Row 5: Missing 3 in position 1 Row 6: Missing 1, 3, 4, 5 in positions 3, 4, 5, 6  Working through the constraints:  Row 5, position 1: Must be 3 (only missing number) Row 1: Solving with box and column constraints gives [2, 5, 4, 1, 3, 6] Row 3: Solving gives [4, 2, 5, 3, 6, 1]  Row 4: Solving gives [1, 6, 3, 4, | No | 30.55 |
| 13 | 4 1 2 2 3 5 4 1 5 1 2 1 4 1 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers by analyzing rows, columns, and 2×3 boxes.  Let me work through this systematically:  Starting with easier deductions:  Row 2: `_ 1 3 5 6 4` - Missing: 2, so position (2,1) = 2  Row 6: `6 2 5 3 4 _` - Missing: 1, so position (6,6) = 1  Column 3: `_, 3, 6, 4, 2, 5` - Missing: 1, so position (1,3) = 1  Row 1: `_ 6 1 _ 5 3` - Missing: 2,4. Since (2,1) = 2, position (1,1) = 4 and (1,4) = 2  Column 1: `4, 2, _, _, _, 6` - Missing: 1,3,5.  - Row 3 needs: 1,3,4,5 and row 4 needs: 1,2,5 - Position (3,1) = 5, (4,1) = 1, (5,1) = 3  Continuing this process for all remaining positions:  Row 3: `5 _ 6 _ _ 2` - Missing: 1,3,4 | No | 28.84 |
| 14 | 4 2 6 1 6 2 5 1 5 2 6 3 2 5 | 4 2 6 1 6 2 5 1 5 2 6 3 2 5 | Yes | 22.76 |
| 15 | 3 4 6 4 2 5 4 2 4 2 4 2 2 1 | 3 4 6 4 2 5 4 2 4 2 4 2 2 1 | Yes | 23.21 |
| 16 | 1 6 4 5 3 2 3 4 1 6 2 3 6 1 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically by checking rows, columns, and 2×3 boxes.  Let me work through this step by step:  The 2×3 boxes are: - Top-left (rows 1-2, cols 1-3) - Top-right (rows 1-2, cols 4-6) - Middle-left (rows 3-4, cols 1-3) - Middle-right (rows 3-4, cols 4-6) - Bottom-left (rows 5-6, cols 1-3) - Bottom-right (rows 5-6, cols 4-6)  Working through each missing cell in reading order:  Row 2, Col 1: Top-left box needs 1, row 2 needs 1, column 1 needs 1 → **1** Row 2, Col 4: Top-right box needs 4,6, row 2 needs 4,6, column 4 needs 2,3,6 → **6** Row 2, Col 5: Top-right box needs 4, row 2 needs 4, column 5 needs 1,4 → **4**  Row 3, | No | 26.78 |
| 17 | 2 2 1 5 3 5 1 4 6 3 4 1 3 6 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers so that each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Let me solve this systematically:  Starting with easier deductions: - Row 1 needs only 2 → (1,6) = 2 - Column 1 needs only 2 → (2,1) = 2   - Row 6 needs only 6 → (6,3) = 6  Working through the constraints: - Row 2: 2, _, 4, 6, _, _ (needs 1, 3, 5) - Column 2 needs 1, 3, 5 - From box constraints: (2,2) = 1  Continuing with column and row analysis: - Column 4 needs 1, 4 → (5,4) = 1, (4,4) = 4 - Row 5 now needs only 3 → (5,5) = 3 - Column 5 | No | 30.35 |
| 18 | 4 3 5 5 4 3 4 2 5 2 6 5 4 6 | 4 3 5 2 3 4 5 6 2 5 4 6 | No | 24.75 |
| 19 | 3 1 5 3 5 6 5 1 4 2 6 1 5 3 |  | No | 28.0 |
| 20 | 1 5 1 5 2 4 5 2 4 1 6 6 4 5 |  | No | 28.18 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1386 | 1386 | Yes | 2.8 |
| 2 | 1776 | 1776 | Yes | 2.88 |
| 3 | 1666 | 1666 | Yes | 3.66 |
| 4 | 2153 | 2153 | Yes | 2.33 |
| 5 | 1498 | 1498 | Yes | 3.72 |
| 6 | 1000 | 1000 | Yes | 2.34 |
| 7 | 1181 | 1181 | Yes | 2.63 |
| 8 | 1351 | 1351 | Yes | 4.01 |
| 9 | 2256 | 2256 | Yes | 3.81 |
| 10 | 1324 | 1324 | Yes | 3.94 |
| 11 | 1864 | 1864 | Yes | 2.4 |
| 12 | 1968 | 1968 | Yes | 3.49 |
| 13 | 968 | 968 | Yes | 2.15 |
| 14 | 2542 | 2542 | Yes | 5.73 |
| 15 | 946 | 946 | Yes | 1.97 |
| 16 | 1979 | 1979 | Yes | 2.45 |
| 17 | 2052 | 2052 | Yes | 3.79 |
| 18 | 2388 | 2388 | Yes | 3.94 |
| 19 | 2039 | 2039 | Yes | 3.93 |
| 20 | 638 | 638 | Yes | 1.77 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 | 55 | Yes | 20.38 |
| 2 | 72 | Looking at the image, I'll count the zeros systematically row by row:  Row 1: 0 1 0 1 0 0 1 1 0 1 → 5 zeros Row 2: 1 0 1 0 0 0 1 1 1 0 → 5 zeros   Row 3: 0 1 1 0 0 1 0 0 0 1 → 6 zeros Row 4: 1 0 1 1 1 0 0 1 1 1 → 3 zeros Row 5: 1 0 0 0 1 0 0 0 0 1 → 7 zeros Row 6: 1 0 0 0 1 1 0 0 1 0 → 6 zeros Row 7: 1 0 1 1 1 1 1 0 1 0 → 3 zeros Row 8: 1 1 1 0 1 1 0 0 1 0 → 4 zeros Row 9: 1 1 1 1 0 1 0 0 1 0 → 4 zeros Row 10: 0 0 1 0 1 0 1 1 0 0 → 6 zeros Row 11: 1 0 1 0 1 1 1 0 0 1 → 4 zeros Row 12: 1 1 1 0 0 1 0 0 1 | No | 21.41 |
| 3 | 74 | 61 | No | 18.83 |
| 4 | 55 | 44 | No | 17.8 |
| 5 | 69 | Looking at the grid, I'll count the zeros row by row:  Row 1: 0 1 1 1 1 0 1 1 1 0 → 3 zeros Row 2: 1 0 0 0 1 0 1 1 1 0 → 5 zeros   Row 3: 0 1 1 0 0 0 1 1 0 0 → 6 zeros Row 4: 1 1 0 1 0 1 0 0 1 0 → 5 zeros Row 5: 0 1 1 1 0 0 1 0 0 0 → 6 zeros Row 6: 1 0 0 0 1 0 1 1 0 0 → 6 zeros Row 7: 0 1 0 0 1 1 1 0 0 1 → 5 zeros Row 8: 0 1 0 1 0 1 0 1 1 1 → 4 zeros Row 9: 1 1 1 1 1 1 1 1 0 0 → 2 zeros Row 10: 1 0 0 0 0 1 1 0 0 1 → 6 zeros Row 11: 0 0 1 1 0 0 1 1 1 0 → 5 zeros Row 12: 0 0 0 0 1 1 0 1 1 0 → 6 zeros Row 13: 1 1 1 1 0 1 1 0 1 1 → 2 zeros Row 14: 0 1 0 0 1 1 1 0 0 0 → 6 zeros Row 15: 1 1 1 0 1 1 1 1 1 0 → 2 zeros  Total: 3+5+6+5+6+6+5+4+2+6+5+6+2+6+2 = 69 zeros  Wait, let me recount row 3 and row 5 more carefully: Row 3: 0 1 1 0 0 0 1 1 0 0 → 5 zeros (not 6) Row 5: 0 1 1 1 0 0 1 0 0 0 → 5 zeros (not 6)  Recounting: 3+5+5+5+5+6+5+4+2+6+5+6+2+6+2 = 67 zeros | No | 21.92 |
| 6 | 38 | 29 | No | 13.08 |
| 7 | 41 | 41 | Yes | 19.29 |
| 8 | 55 | 52 | No | 14.45 |
| 9 | 41 | 41 | Yes | 18.83 |
| 10 | 70 | 64 | No | 19.13 |
| 11 | 37 | 37 | Yes | 13.5 |
| 12 | 48 | 44 | No | 16.47 |
| 13 | 67 | 67 | Yes | 21.14 |
| 14 | 66 | 64 | No | 16.18 |
| 15 | 51 | 51 | Yes | 17.12 |
| 16 | 74 | 60 | No | 18.01 |
| 17 | 70 | Looking at this image, I'll count the zeros systematically row by row:  Row 1: 1 0 1 0 1 1 0 0 0 0 → 6 zeros Row 2: 1 0 1 1 1 0 1 1 1 0 → 3 zeros   Row 3: 0 0 1 1 1 0 1 1 1 1 → 3 zeros Row 4: 1 0 1 1 1 1 1 0 1 1 → 2 zeros Row 5: 1 1 1 1 0 0 1 0 0 1 → 4 zeros Row 6: 1 1 0 0 0 1 1 0 0 0 → 6 zeros Row 7: 1 0 0 0 1 1 1 0 1 0 → 5 zeros Row 8: 0 0 0 1 0 0 1 1 1 0 → 6 zeros Row 9: 0 0 1 0 0 1 0 1 0 0 → 7 zeros Row 10: 1 0 0 0 1 1 1 1 1 0 → 4 zeros Row 11: 0 0 1 1 1 0 1 0 1 1 → 4 zeros Row 12: 0 0 0 0 1 1 0 0 0 0 → 8 zeros Row 13: 1 1 0 0 0 1 1 | No | 23.24 |
| 18 | 58 | 57 | No | 19.0 |
| 19 | 40 | 40 | Yes | 13.69 |
| 20 | 50 | TIMEOUT | No | 120.02 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YDWIKBU | YDWIKBU | Yes | 4.73 |
| 2 | HOCMIAT | HOCMIAT | Yes | 11.51 |
| 3 | LFEUHNQ | LFEUHNQ | Yes | 8.13 |
| 4 | GAOTHIE | GAOTHIE | Yes | 10.55 |
| 5 | JBMUZND | JBMUZND | Yes | 4.85 |
| 6 | SLIUDNQ | SLIUDNQ | Yes | 6.06 |
| 7 | XMRNKEU | XMRNKEU | Yes | 4.25 |
| 8 | MEIXLRN | MEIXLRN | Yes | 8.31 |
| 9 | JGWRDZL | JGWRDZL | Yes | 5.57 |
| 10 | JBROPZK | JBROPZK | Yes | 7.55 |
| 11 | OQBIMNV | OQBIMNV | Yes | 4.51 |
| 12 | KYJTZBF | KJYTZBO | No | 14.12 |
| 13 | GDLFAHI | GDLFAHI | Yes | 6.31 |
| 14 | KJIMWUC | KJIMWUC | Yes | 4.76 |
| 15 | UOHSIZF | UOHSIZF | Yes | 3.99 |
| 16 | SXZYFIH | SXZYFIH | Yes | 4.19 |
| 17 | QYKSOIX | QYKSOIX | Yes | 9.96 |
| 18 | IHDWJOP | IHDWJOP | Yes | 5.23 |
| 19 | WCHLXFM | WCHLXFM | Yes | 9.7 |
| 20 | ISBELYF | ISBELYF | Yes | 8.02 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.1, 6.9] | 6.9 3.1 | Yes | 10.93 |
| 2 | [0.3, 9.7] | 9.7 0.3 | Yes | 9.55 |
| 3 | [3.6, 6.4] | 6.4 3.6 | Yes | 10.35 |
| 4 | [0.3, 9.7] | 9.7 0.3 | Yes | 12.11 |
| 5 | [3.3, 6.7] | 3.3 6.7 | Yes | 12.38 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 10.04 |
| 7 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.66 |
| 8 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.42 |
| 9 | [2.0, 8.0] | 2.0 8.0 | Yes | 9.91 |
| 10 | [1.5, 8.5] | 1.5 8.5 | Yes | 14.41 |
| 11 | [2.7, 7.3] | 2.7 7.3 | Yes | 10.04 |
| 12 | [2.8, 7.2] | 2.8 7.2 | Yes | 9.66 |
| 13 | [4.6, 5.4] | 5.4 4.6 | Yes | 8.29 |
| 14 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.86 |
| 15 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.9 |
| 16 | [2.3, 7.7] | 7.7 2.3 | Yes | 9.4 |
| 17 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.98 |
| 18 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.14 |
| 19 | [1.4, 8.6] | 8.6 1.4 | Yes | 10.74 |
| 20 | [3.2, 6.8] | 6.8 3.2 | Yes | 15.17 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VRMDDN1YHX3G | VRMDDN1YHX3G | Yes | 7.91 |
| 2 | GXTQSA8FNY66 | GXTQSA8FNY66 | Yes | 3.63 |
| 3 | 371DJ0JBQYSV | 371DJQJBQYSV | No | 2.96 |
| 4 | VLGJ8WB422A9 | VLGJ8WB422A9 | Yes | 3.23 |
| 5 | YARYK231GZ5W | YARYK231GZ5W | Yes | 5.86 |
| 6 | S42B1T38PUN7 | S42B1T38PUN7 | Yes | 3.85 |
| 7 | ZBGWDRBCKZBO | ZBGWDRBCKZBO | Yes | 9.91 |
| 8 | 6U8VOBH7S6JA | 6U8VOBH7S6JA | Yes | 3.29 |
| 9 | J5WEFTHSA7PJ | J5WEFTHSA7PJ | Yes | 3.89 |
| 10 | ES4MUFKH0HWX | ES4MUFKH0HWX | Yes | 3.89 |
| 11 | GYHJXZMN6FAK | GYHJXZMN6FAK | Yes | 3.84 |
| 12 | GDHUPSIXQR5E | GDHUPSIXQR5E | Yes | 3.72 |
| 13 | M62KKTCBR1VD | M62KKTCBR1VD | Yes | 4.07 |
| 14 | 3LEDAGV629US | 3LEDAGV629US | Yes | 4.02 |
| 15 | LP4FAMJI6DXU | LP4FAMJI6DXU | Yes | 3.65 |
| 16 | A23YDLLYWGZG | A23YDLLYVWGZG | No | 4.67 |
| 17 | S4ZK27E0Y5AY | S4ZK27E0Y5AY | Yes | 4.02 |
| 18 | I0AJJV199XUW | I0AJJV199XUW | Yes | 3.9 |
| 19 | S506O3QW9LJL | S50603QW9LJL | No | 3.86 |
| 20 | VPEWKW2PAJ6M | VPEWKW2PAJ6M | Yes | 3.46 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 6.17 |
| 2 | 26 | 26 | Yes | 9.72 |
| 3 | 243 | 243 | Yes | 5.27 |
| 4 | 16 | 16 | Yes | 3.98 |
| 5 | 64 | 64 | Yes | 9.34 |
| 6 | 3 | -3 | No | 10.16 |
| 7 | 73 | 73 | Yes | 4.6 |
| 8 | 6 | 6 | Yes | 4.63 |
| 9 | 63 | 63 | Yes | 3.53 |
| 10 | 4 | 4 | Yes | 7.94 |
| 11 | 9 | 9 | Yes | 6.0 |
| 12 | 198 | 198 | Yes | 5.33 |
| 13 | 793 | 793 | Yes | 3.47 |
| 14 | 39 | 39 | Yes | 4.28 |
| 15 | 60 | 60 | Yes | 3.21 |
| 16 | 48 | 48 | Yes | 3.17 |
| 17 | 7 | 7 | Yes | 3.28 |
| 18 | 31 | 31 | Yes | 4.52 |
| 19 | 65 | 65 | Yes | 4.56 |
| 20 | 20 | 21 | No | 17.89 |
