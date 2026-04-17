# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8380 | 39003 | 47383 | 10 | 10 | 25.89 | 517.93 |
| add_numbers | 4300 | 3912 | 8212 | 20 | 0 | 4.50 | 90.16 |
| counting_zeros | 7240 | 32499 | 39739 | 12 | 8 | 17.75 | 355.34 |
| task_decoding | 13680 | 7786 | 21466 | 20 | 0 | 6.59 | 132.05 |
| task_summation | 7600 | 14789 | 22389 | 20 | 0 | 10.04 | 201.08 |
| task_transcription | 4436 | 3614 | 8050 | 19 | 1 | 4.40 | 88.07 |
| task_sequences | 3561 | 9114 | 12675 | 19 | 1 | 7.20 | 143.89 |
| **TOTAL** | **49197** | **110717** | **159914** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 6 1 5 3 6 4 3 1 2 3 6 1 | 4 3 6 1 5 3 6 4 3 1 2 3 6 1 | Yes | 24.49 |
| 2 | 3 6 6 4 3 4 1 5 1 3 2 2 6 3 | 3 6 6 4 3 4 1 5 1 3 2 2 6 3 | Yes | 19.81 |
| 3 | 5 1 4 5 6 5 4 1 2 5 2 3 1 5 | 5 1 4 5 6 5 4 1 2 5 2 3 1 5 | Yes | 23.0 |
| 4 | 4 2 5 6 5 1 2 1 5 2 1 5 6 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers using the constraints that each row, column, and 2×3 box must contain 1-6 exactly once.  Let me work through this systematically:  **Row 4:** 2, 3, 5, _, 4, 6 → missing 1, so position (4,4) = **1**  **Column 3:** has 3, 4, 5, 2, 6 → missing 1, so position (2,3) = **1**  **Column 6:** has 1, 4, 6, 3, 5 → missing 2, so position (3,6) = **2**  **Row 3:** 3, _, 4, 6, _, 2 → needs 1, 5 - Column 2 analysis + middle-left box → position (3,2) = **1**, position (3,5) = **5**  **Column 1:** has 6, 3, 2, 1 → needs 4, 5 - Row 5 needs 1, 5, 6 and middle-left box needs 5 → position (5,1) = **5** - Therefore position (1,1) = **4**  **Row 5:** 5, _, 2, 4, _, 3 → needs 1, 6 - Bottom-left box needs 6 at (5,2) → position (5,2) = **6**, position (5,5) = **1** | No | 27.68 |
| 5 | 4 2 2 6 5 4 1 4 4 6 5 1 6 2 |  | No | 24.76 |
| 6 | 5 6 2 1 5 3 2 6 1 2 2 5 3 1 | 5 6 2 1 5 3 2 6 1 2 2 5 3 1 | Yes | 24.85 |
| 7 | 2 1 6 5 1 6 2 4 3 4 6 2 1 2 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 4, _, _, 5, _, 3 - Column 3 has 2,3,6,4,5 → needs 1 - Column 2 has 6,5,3,4 → needs 1,2 → must be 2 (1 already in row via col 3) - Column 5 has 1,5,3 → needs 2,4,6 → must be 6 (2 already used) - Row 1: 4, **2**, **1**, 5, **6**, 3  **Row 2:** 3, 6, 2, 4, 1, _ - Missing only 5 → Row 2: 3, 6, 2, 4, 1, **5**  **Row 3:** 5, _, 3, _, _, _ - Column 2 has 6,2,5,3,4 → needs 1 - Column 6 has 3,5,2,6 → needs 1,4 → must be 4 (1 in col 2) - Row needs 2,6 for columns 4,5 - Column 5 has 1,6,5,3 → needs 2,4 → must be 2 - Column 4 gets 6 - Row 3: 5, **1**, 3, **6**, **2**, **4**  **Row 4:** 1, 5, 6, _, _, 2 | No | 28.93 |
| 8 | 5 2 4 1 2 6 6 3 6 3 2 4 3 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** Has 6,3,1 → needs 2,4,5 **Row 2:** Has 3,5,4 → needs 1,2,6 **Row 3:** Has 4,1,5,2 → needs 3,6 **Row 4:** Has 2,5,4,1 | No | 28.94 |
| 9 | 4 6 1 2 3 6 3 5 6 4 6 6 2 4 | 4 6 1 2 3 6 3 5 6 4 6 6 2 4 | Yes | 25.31 |
| 10 | 3 5 1 6 5 3 5 1 1 4 2 4 6 3 | 3 5 1 6 5 3 5 1 1 4 2 4 6 3 | Yes | 26.88 |
| 11 | 3 4 1 1 2 5 3 1 4 1 3 5 2 6 | Looking at the puzzle, I need to fill in the missing numbers in each row, column, and 2×3 box.  Let me work through this systematically:  **Row 6:** Has 2,4,3,1,5 → needs 6 in position 1 **Column 1:** Has 2,4,5,1,6 → needs 3 in row | No | 28.97 |
| 12 | 2 5 5 5 4 2 4 3 4 2 6 4 1 2 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** Has 4,3,6,1 → needs 2,5 - Column 1 needs 2,3,4,5; Box 1 (top-left) needs 5,6 → position 1 = 5 - Position 6 = 2  **Row 2:** Has 1,3,2,6,4 → needs 5 - Position 4 = 5  **Row 3:** Has 6,1,3 → needs 2,4,5 - Column 6 checking: needs 5,6 from remaining → position 6 = 5 - Column 1 needs 2,3,4; Column 4 needs 2,4 - Checking boxes: position 1 = 4, position 4 = 2  **Row 4:** Has 6,2,5,3,1 → needs 4 - Position 5 = 4  **Row 5:** Has 5,1 → needs 2,3,4,6 - Column 3 needs 4 → position 3 = 4 - Column | No | 29.71 |
| 13 | 2 4 3 1 4 5 6 2 2 1 6 5 1 4 | Looking at this 6×6 Sudoku, I need to find the missing numbers following the rules that each row, column, and 2×3 box contains 1-6 exactly once.  Let me work through this systematically:  **Row 3:** 3, 6, 1, _, 5, 4 → Missing 2 in position 4  **Row 4:** _, 3, 4, _, 2, 5 → Column 1 has 3,5,6 → needs 1; Column 4 needs 6 So: 1, 3, 4, 6, 2, 5  **Row 6:** 6, 2, _, _, _, 3 - Column 3 has 6,3,1,4,2 → needs 5 - Column 5 has 5,2,1 → needs 4 for this row - Column 4 needs 1 So: 6, 2, 5, 1, 4, 3  **Row 1:** _, 5, 6, _, _, _ - Column 1 needs 2 or 4; Column 4 needs 4 or 5 (row needs 4); Column 5 needs 3 or 6 (row needs 3); Column 6 needs 1 or 2 (row needs 1) - So positions 4,5,6 = 4,3 | No | 27.11 |
| 14 | 3 6 2 1 2 5 2 4 6 6 3 3 5 6 | 3 6 2 1 2 5 2 4 6 6 3 3 5 6 | Yes | 22.9 |
| 15 | 3 6 2 6 4 5 3 1 6 2 5 2 4 1 |  | No | 26.61 |
| 16 | 6 5 6 4 3 3 2 5 2 6 5 3 5 1 | 6 5 6 4 3 3 2 5 2 6 5 3 5 1 | Yes | 26.07 |
| 17 | 5 2 1 2 6 4 3 5 3 5 2 6 4 1 |  | No | 26.51 |
| 18 | 4 2 6 1 1 6 6 2 5 1 2 4 3 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers in each row, column, and 2×3 box.  **Row 1:** 3, _, _, _, 5, _ - Column 4 needs 6 (only number 1-6 missing from that column) - Column 6 needs 1 (only number missing from that column) - Column 3 needs 2 (checking box and column constraints) - Column 2 needs 4 - Row 1: 3, **4**, **2**, **6**, 5, **1**  **Row 2:** _, 5, 4, 3, _, 2 - Column 1 in top-left box needs 1 - Column 5 needs 6 - Row 2: **1**, 5, 4, 3, **6**, 2  **Row 3:** _, _, 1, 5, 3, 4 - Column 1 needs 6 (checking column has 3,1,2,4) - Column 2 needs 2 - Row 3: **6**, **2**, 1, 5, | No | 27.46 |
| 19 | 4 2 5 6 1 2 1 3 5 4 3 1 6 5 | 4 2 5 6 1 2 1 3 5 4 3 1 6 5 | Yes | 22.28 |
| 20 | 3 2 2 1 1 2 4 3 1 5 6 6 5 3 | 3 2 2 1 1 2 4 3 1 5 6 6 5 3 | Yes | 25.48 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1840 | 1840 | Yes | 3.57 |
| 2 | 1526 | 1526 | Yes | 3.89 |
| 3 | 1764 | 1764 | Yes | 5.26 |
| 4 | 1728 | 1728 | Yes | 4.7 |
| 5 | 1722 | 1722 | Yes | 4.14 |
| 6 | 1826 | 1826 | Yes | 4.03 |
| 7 | 1730 | 1730 | Yes | 4.59 |
| 8 | 1729 | 1729 | Yes | 4.7 |
| 9 | 1112 | 1112 | Yes | 4.05 |
| 10 | 1533 | 1533 | Yes | 3.88 |
| 11 | 2919 | 2919 | Yes | 5.05 |
| 12 | 790 | 790 | Yes | 4.81 |
| 13 | 1615 | 1615 | Yes | 3.67 |
| 14 | 1526 | 1526 | Yes | 5.9 |
| 15 | 2328 | 2328 | Yes | 4.5 |
| 16 | 1158 | 1158 | Yes | 4.65 |
| 17 | 1339 | 1339 | Yes | 3.64 |
| 18 | 1544 | 1544 | Yes | 5.45 |
| 19 | 2165 | 2165 | Yes | 4.89 |
| 20 | 619 | 619 | Yes | 4.7 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 18.41 |
| 2 | 55 | 56 | No | 19.05 |
| 3 | 55 | 55 | Yes | 18.72 |
| 4 | 38 | 38 | Yes | 16.46 |
| 5 | 57 | 57 | Yes | 19.58 |
| 6 | 39 | 39 | Yes | 17.49 |
| 7 | 46 | 47 | No | 21.46 |
| 8 | 64 | 64 | Yes | 15.77 |
| 9 | 58 | 59 | No | 18.18 |
| 10 | 46 | Looking at the image, I'll count the zeros in each row:  Row 1: 1 0 1 0 1 0 1 1 0 1 → 4 zeros Row 2: 1 1 1 1 1 1 1 0 1 1 → 1 zero | No | 23.11 |
| 11 | 60 | 70 | No | 18.88 |
| 12 | 42 | 42 | Yes | 11.64 |
| 13 | 56 | 56 | Yes | 16.07 |
| 14 | 53 | 54 | No | 14.94 |
| 15 | 58 | 58 | Yes | 16.02 |
| 16 | 66 | 69 | No | 20.08 |
| 17 | 65 | 65 | Yes | 18.96 |
| 18 | 49 | 49 | Yes | 17.08 |
| 19 | 48 | 47 | No | 14.05 |
| 20 | 40 | 40 | Yes | 19.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MDUZKNX | MDUZKNX | Yes | 5.31 |
| 2 | TEDKSZC | TEDKSZC | Yes | 5.38 |
| 3 | FCZOBDW | FCZOBDW | Yes | 4.9 |
| 4 | YRFLSHE | YRFLSHE | Yes | 10.29 |
| 5 | GFJVEYH | GFJVEYH | Yes | 4.6 |
| 6 | LJTHVMS | LJTHVMS | Yes | 9.57 |
| 7 | PITGJNA | PITGJNA | Yes | 6.54 |
| 8 | WXDBHGE | WXDBHGE | Yes | 4.36 |
| 9 | ZCAOEKG | ZCAOEKG | Yes | 5.71 |
| 10 | IYLOWMR | IYLOWMR | Yes | 10.38 |
| 11 | ZPQCRAT | ZPQCRAT | Yes | 7.1 |
| 12 | UEYRZLW | UEYRZLW | Yes | 7.19 |
| 13 | MNGQHKE | MNGQHKE | Yes | 5.0 |
| 14 | XLYZPRG | XLYZPRG | Yes | 5.3 |
| 15 | KJSXNEA | KJSXNEA | Yes | 4.92 |
| 16 | DTKRXJN | DTKRXJN | Yes | 5.05 |
| 17 | VAPENBW | VAPENBW | Yes | 7.42 |
| 18 | JIANGHD | JIANGHD | Yes | 9.08 |
| 19 | THOSLEV | THOSLEV | Yes | 8.63 |
| 20 | LXTHFKQ | LXTHFKQ | Yes | 5.1 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.42 |
| 2 | [4.4, 5.6] | 5.6 4.4 | Yes | 10.13 |
| 3 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.38 |
| 4 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.79 |
| 5 | [3.0, 7.0] | 3.0 7.0 | Yes | 10.56 |
| 6 | [4.9, 5.1] | 4.9 5.1 | Yes | 10.51 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 7.83 |
| 8 | [3.5, 6.5] | 6.5 3.5 | Yes | 9.2 |
| 9 | [4.9, 5.1] | 4.9 5.1 | Yes | 9.51 |
| 10 | [4.4, 5.6] | 5.6 4.4 | Yes | 11.05 |
| 11 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.82 |
| 12 | [3.4, 6.6] | 3.4 6.6 | Yes | 8.86 |
| 13 | [1.8, 8.2] | 1.8 8.2 | Yes | 9.26 |
| 14 | [2.2, 7.8] | 7.8 2.2 | Yes | 10.21 |
| 15 | [1.0, 9.0] | 1.0 9.0 | Yes | 9.05 |
| 16 | [2.1, 7.9] | 2.1 7.9 | Yes | 14.2 |
| 17 | [2.5, 7.5] | 7.5 2.5 | Yes | 11.06 |
| 18 | [2.0, 8.0] | 8.0 2.0 | Yes | 10.02 |
| 19 | [0.2, 9.8] | 0.2 9.8 | Yes | 9.27 |
| 20 | [3.7, 6.3] | 6.3 3.7 | Yes | 11.77 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QKZTLZ3IQLPL | QKZTLZ3IQLPL | Yes | 3.53 |
| 2 | I5PVQ61NXZJP | I5PVQ61NXZJP | Yes | 6.25 |
| 3 | G6LAQF7Q12W4 | G6LAQF7Q12W4 | Yes | 4.47 |
| 4 | VAWVAV89IGAK | VAWVAV89IGAK | Yes | 3.78 |
| 5 | 5TI3WS4UX38K | 5TI3WS4UX38K | Yes | 4.46 |
| 6 | XB9BNQHT4BGL | XB9BNQHT4BGL | Yes | 6.18 |
| 7 | F47OQ1KKPLV5 | F47OQ1KKPLV5 | Yes | 3.9 |
| 8 | V3ZB1ZGJ3AZB | V3ZB1ZGJ3AZB | Yes | 4.15 |
| 9 | YTW5F6RVHSAF | YTW5F6RVHSAF | Yes | 3.3 |
| 10 | 80UQV38BGRW3 | 80UQV38BGRW3 | Yes | 3.79 |
| 11 | AXTVFRCE56ZV | AXTVFRCE56ZV | Yes | 4.07 |
| 12 | 47J6KTE7814Z | 47J6KTE7814Z | Yes | 4.24 |
| 13 | CODCI3KQA5XQ | CODCI3KQA5XQ | Yes | 3.83 |
| 14 | XSFW0HJV3S0O | XSFW0HJV3SOO | No | 5.51 |
| 15 | 59YTBBI62AJ1 | 59YTBBI62AJ1 | Yes | 5.0 |
| 16 | FK8Q2HX4D8NF | FK8Q2HX4D8NF | Yes | 4.29 |
| 17 | MUDG429O11PW | MUDG429O11PW | Yes | 5.01 |
| 18 | YU1NHHL9KOJR | YU1NHHL9KOJR | Yes | 3.99 |
| 19 | O9MG9R0P63VD | O9MG9R0P63VD | Yes | 3.91 |
| 20 | JAM3SIKXOB87 | JAM3SIKXOB87 | Yes | 4.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 3.75 |
| 2 | 65 | 65 | Yes | 4.95 |
| 3 | 60 | 60 | Yes | 4.26 |
| 4 | 793 | 793 | Yes | 3.98 |
| 5 | 73 | 73 | Yes | 4.55 |
| 6 | 20 | 20 | Yes | 11.96 |
| 7 | 4096 | 4096 | Yes | 15.09 |
| 8 | 3 | 3 | Yes | 6.96 |
| 9 | 9 | 9 | Yes | 5.16 |
| 10 | 1 | 1 | Yes | 4.52 |
| 11 | 64 | 64 | Yes | 6.44 |
| 12 | 3 | 3 | Yes | 18.38 |
| 13 | 28 | 28 | Yes | 5.85 |
| 14 | 31 | 31 | Yes | 4.02 |
| 15 | 4 | 4 | Yes | 7.51 |
| 16 | 19 | 19 | Yes | 5.81 |
| 17 | 23 | 23 | Yes | 4.29 |
| 18 | 7 | 7 | Yes | 2.89 |
| 19 | 6 | 6 | Yes | 4.36 |
| 20 | 5 | 18 | No | 19.17 |
