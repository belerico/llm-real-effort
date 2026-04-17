# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-19 10:03:47

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
| sudoku_game | 8060 | 38694 | 46754 | 2 | 18 | 26.77 | 535.66 |
| add_numbers | 3980 | 3768 | 7748 | 20 | 0 | 3.26 | 65.36 |
| counting_zeros | 6920 | 32790 | 39710 | 16 | 4 | 17.79 | 356.04 |
| task_decoding | 13360 | 8598 | 21958 | 18 | 2 | 6.88 | 137.88 |
| task_summation | 7280 | 18602 | 25882 | 20 | 0 | 11.07 | 221.64 |
| task_transcription | 4132 | 3551 | 7683 | 14 | 6 | 3.95 | 79.0 |
| task_sequences | 3241 | 9766 | 13007 | 15 | 5 | 6.89 | 137.86 |
| **TOTAL** | **46973** | **115769** | **162742** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 4 4 3 1 6 5 4 6 5 3 5 3 |  | No | 26.79 |
| 2 | 6 1 5 4 5 4 2 6 2 5 4 2 6 3 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in reading order.  Let me solve systematically by analyzing rows, columns, and 2×3 boxes:  From column 6, which has: _, 6, 3, 2, 1, 5 Missing: 4 So position (1,6) = 4  From column 4, which has: _, 3, 5, 4, 2, _ Missing: 1, 6 Since row 1 needs 1, 5, 6 and position (1,6) = 4, position (1,4) = 1 Therefore position (6,4) = 6  Row 1 now has: 2, 3, _, 1, _, 4 Missing: 5, 6  From column 5, which has: _, 1, _, 6, 4, _ Missing: 2, 3, 5 Since row 1 needs 5 or 6, position (1,5) = 5 Therefore position (1,3) = 6  Row 6 now has: _, _, 1, 6, _, 5 Missing: 2, 3, 4  Continuing this process for all remaining positions:  Row 2: Position (2,1) = 4, (2,2) = 2, (2,3) = 5 Row 3: Position (3,2) = 6, (3,5) | No | 29.53 |
| 3 | 5 3 6 4 6 4 5 5 6 3 4 1 5 1 | 5 3 4 6 4 1 6 2 5 1 2 6 3 4 5 5 1 | No | 27.83 |
| 4 | 3 2 2 3 1 6 5 3 4 6 2 5 3 1 |  | No | 26.42 |
| 5 | 2 5 3 1 4 2 2 3 1 6 4 1 1 6 |  | No | 28.51 |
| 6 | 2 5 4 3 1 5 2 5 2 1 4 1 5 3 | 2 5 4 3 1 5 2 5 1 5 2 1 | No | 25.66 |
| 7 | 4 3 1 1 6 4 6 1 2 3 3 6 2 5 | 4 3 1 6 1 4 1 6 2 3 3 6 2 5 | No | 25.27 |
| 8 | 5 6 4 2 3 3 6 1 6 2 4 2 6 3 | 5 6 4 2 3 3 6 1 6 2 4 2 3 6 | No | 24.24 |
| 9 | 3 6 1 6 5 1 2 6 5 4 1 3 6 1 | 3 6 1 6 5 1 2 6 5 4 1 3 6 1 | Yes | 21.94 |
| 10 | 3 6 4 5 5 6 3 6 1 5 4 3 4 1 | 3 6 4 5 5 6 3 6 1 5 4 3 4 1 | Yes | 21.72 |
| 11 | 3 5 4 6 4 6 3 2 5 6 3 3 5 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell.  Let me work through this systematically:  First, I'll identify what numbers are missing in each row: - Row 1: Missing 3, 4, 5, 6 - Row 2: Missing 4 (only one empty cell, so position 1 = 4) - Row 3: Missing 3, 6 - Row 4: Missing 2, 3, 5, 6 - Row 5: Missing 3, 5 - Row 6: Missing 6 (only one empty cell, so position 1 = 6)  Now I'll use row, column, and 2×3 box constraints to solve:  Row 2, Col 1 = 4 Row 6, Col 1 = 6  Using column constraints: - Column 1 now has 4, 5, _, 1 | No | 27.25 |
| 12 | 4 6 5 2 1 6 5 6 4 3 1 4 2 6 | Looking at this 6×6 Sudoku puzzle, I need to fill in the empty cells following the constraints that each row, column, and 2×3 box contains numbers 1-6 exactly once.  Let me work through this systematically:  Starting with the most constrained positions: - Row 4 is missing only one number: 3 (in position 4,4) - Row 5 is missing only one number: 1 (in position 5,1)  After placing these: - Column 6 needs only 6, which goes in position (6,6) - Column 5 analysis: Row 2 needs 1,2,6 and column 5 needs 5,6, so position (2,5) = 6 - This means position (1,5) = 5 (completing column 5)  Continuing with rows 1 and 2: - Row 1 needs 4,6 in positions (1,1) and (1,2) - Row 2 needs 1,2 in positions (2,1) and (2,2) - Column 1 needs 2,4, so position (2,1) = 2 and (1,1) = 4 - This gives us (1,2) = 6 and (2,2) = 1  For row 3: - Needs 4,5,6 in positions (3,2), (3,3), (3,4) - Column 4 needs 4, so position (3,4) = 4 - Column 3 needs 2,6, and row 3 needs 6, so position (3,3) = 6 - Position (3,2) = 5  Finally for row 6: - Column 2 needs 4, so position (6, | No | 26.51 |
| 13 | 1 2 3 4 2 5 4 6 2 6 4 6 1 5 | Looking at this 6×6 Sudoku puzzle, I need to solve it systematically using the constraint that each row, column, and 2×3 box contains numbers 1-6 exactly once.  Let me work through this step by step:  First, I notice that column 5 has: 4, 3, ?, 5, 1, 2. The only missing number is 6, so position (3,5) = 6.  Now row 3 has: 3, ?, 1, ?, 6, 2. Missing numbers are 4 and 5.  Looking at the 2×3 boxes and continuing to solve using elimination:  After working through all the constraints systematically:  Row 1: 2, 6, 3, 5, 4, 1 → positions (1,1)=2, (1,3)=3, (1,4)=5 - Wait, this is incorrect since (1,6)=5 is given.  Let me solve more carefully:  Row 1: ?, 6, ?, ?, 4, 5 → Missing: 1, 2, 3 After solving: positions (1,1)=1, (1,3)=2, (1,4)=3  Row 2: ?, ?, 5, 6, 3, 1 → Missing: 2, 4 After solving: positions (2,1)=2, (2,2)=4  Row 3: 3, ?, 1, ?, ?, 2 → position (3,5)=6, then (3,2)=5, (3,4)=4  Row 4: ?, 4, ?, 1, 5, 3 → positions (4,1)=6, (4,3)=2  Row 5: 5, 3, ?, 2, 1 | No | 29.72 |
| 14 | 6 3 4 2 4 5 6 5 3 1 6 5 6 3 | Looking at this 6×6 Sudoku puzzle, I need to fill in the empty cells systematically.  Let me work through this step by step:  First, I'll identify what numbers are missing in each row: - Row | No | 28.4 |
| 15 | 5 6 1 1 2 5 4 5 5 6 4 3 6 1 |  | No | 30.94 |
| 16 | 2 3 5 1 5 1 4 2 5 6 5 5 6 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by working through each row and checking constraints.  Let me work through the empty cells:  Row 2: Has 6, 4, 2, 3, _, 1. Missing number is 5.  Row 4: Has 4, 1, 3, _, 6, _. Looking at column 6, it has 6, 1, 3, _, 4, 2, so missing is 5. | No | 26.75 |
| 17 | 3 4 6 5 4 4 1 2 3 4 3 6 5 2 | 4 3 1 5 4 4 3 2 1 4 3 6 5 2 | No | 28.57 |
| 18 | 5 3 2 4 3 6 3 5 4 3 2 3 1 6 | 3 5 2 4 3 6 4 5 1 6 1 3 6 | No | 28.4 |
| 19 | 3 2 4 5 2 6 3 3 5 6 4 6 1 5 | 3 4 5 2 6 3 3 5 6 4 6 1 5 | No | 23.81 |
| 20 | 4 6 1 5 2 2 1 1 2 6 6 1 3 4 |  | No | 27.16 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1774 | 1774 | Yes | 3.12 |
| 2 | 1165 | 1165 | Yes | 2.27 |
| 3 | 1626 | 1626 | Yes | 3.63 |
| 4 | 907 | 907 | Yes | 1.7 |
| 5 | 1668 | 1668 | Yes | 2.62 |
| 6 | 2284 | 2284 | Yes | 2.05 |
| 7 | 1764 | 1764 | Yes | 3.5 |
| 8 | 1693 | 1693 | Yes | 4.05 |
| 9 | 1740 | 1740 | Yes | 2.98 |
| 10 | 1736 | 1736 | Yes | 4.42 |
| 11 | 1672 | 1672 | Yes | 3.04 |
| 12 | 1661 | 1661 | Yes | 3.93 |
| 13 | 2475 | 2475 | Yes | 3.92 |
| 14 | 1737 | 1737 | Yes | 3.94 |
| 15 | 2375 | 2375 | Yes | 3.89 |
| 16 | 1468 | 1468 | Yes | 3.72 |
| 17 | 1170 | 1170 | Yes | 1.78 |
| 18 | 1112 | 1112 | Yes | 1.75 |
| 19 | 2183 | 2183 | Yes | 4.85 |
| 20 | 1035 | 1035 | Yes | 4.11 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 13.91 |
| 2 | 61 | 61 | Yes | 20.29 |
| 3 | 58 | 58 | Yes | 16.74 |
| 4 | 57 | 47 | No | 14.49 |
| 5 | 67 | 67 | Yes | 20.65 |
| 6 | 56 | 56 | Yes | 19.27 |
| 7 | 40 | 39 | No | 14.77 |
| 8 | 70 | 70 | Yes | 16.33 |
| 9 | 45 | 45 | Yes | 19.38 |
| 10 | 51 | 51 | Yes | 20.38 |
| 11 | 65 | 65 | Yes | 20.47 |
| 12 | 36 | 33 | No | 18.27 |
| 13 | 74 | 61 | No | 19.54 |
| 14 | 72 | 72 | Yes | 16.67 |
| 15 | 56 | 56 | Yes | 21.49 |
| 16 | 39 | 39 | Yes | 14.7 |
| 17 | 49 | 49 | Yes | 19.57 |
| 18 | 47 | 47 | Yes | 18.79 |
| 19 | 65 | 65 | Yes | 12.4 |
| 20 | 35 | 35 | Yes | 17.61 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GAZBVKC | GAZBVKC | Yes | 7.65 |
| 2 | OENIAFG | ONEIAFG | No | 10.56 |
| 3 | HQZKGJE | HQZKGJE | Yes | 5.66 |
| 4 | LCZTVWH | LCZTVWH | Yes | 6.82 |
| 5 | JQATYDW | JQATYDW | Yes | 9.05 |
| 6 | CHVDXAW | CHVDXAW | Yes | 6.32 |
| 7 | EMVBQYO | EMVBQYO | Yes | 5.27 |
| 8 | TPQVUFI | TPQVUFI | Yes | 6.7 |
| 9 | QHSCFWY | QHSCFWY | Yes | 5.76 |
| 10 | EGBYASI | EGBYASI | Yes | 6.22 |
| 11 | ZSQLMBP | ZSQLMBP | Yes | 4.26 |
| 12 | MDIBYAU | MDIBYAS | No | 10.37 |
| 13 | DIEUWTR | DIEUWTR | Yes | 9.94 |
| 14 | RQDFNVC | RQDFNVC | Yes | 5.49 |
| 15 | TDCWKUQ | TDCWKUQ | Yes | 7.14 |
| 16 | VPICKWA | VPICKWA | Yes | 7.68 |
| 17 | HJYDLZU | HJYDLZU | Yes | 6.54 |
| 18 | SDCXJRF | SDCXJRF | Yes | 5.86 |
| 19 | PGJRWBN | PGJRWBN | Yes | 4.21 |
| 20 | ADFXMLK | ADFXMLK | Yes | 6.18 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.9, 9.1] | 9.1 0.9 | Yes | 15.64 |
| 2 | [2.0, 8.0] | 2.0 8.0 | Yes | 12.58 |
| 3 | [2.5, 7.5] | 7.5 2.5 | Yes | 11.11 |
| 4 | [1.3, 8.7] | 8.7 1.3 | Yes | 13.92 |
| 5 | [1.8, 8.2] | 8.2 1.8 | Yes | 11.26 |
| 6 | [0.6, 9.4] | 0.6 9.4 | Yes | 10.53 |
| 7 | [0.9, 9.1] | 0.9 9.1 | Yes | 11.01 |
| 8 | [0.9, 9.1] | 0.9 9.1 | Yes | 9.53 |
| 9 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.83 |
| 10 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.9 |
| 11 | [2.0, 8.0] | 8.0 2.0 | Yes | 16.11 |
| 12 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.44 |
| 13 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.65 |
| 14 | [3.2, 6.8] | 3.2 6.8 | Yes | 8.5 |
| 15 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.08 |
| 16 | [1.0, 9.0] | 9.0 1.0 | Yes | 10.49 |
| 17 | [3.7, 6.3] | 3.7 6.3 | Yes | 12.0 |
| 18 | [3.8, 6.2] | 3.8 6.2 | Yes | 9.91 |
| 19 | [3.5, 6.5] | 6.5 3.5 | Yes | 10.81 |
| 20 | [2.6, 7.4] | 2.6 7.4 | Yes | 9.12 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KFS8U2SK6Z6U | KFS8U2SK6Z6U | Yes | 2.78 |
| 2 | JKAPLDCE7POD | JKAPLDCE7POD | Yes | 5.21 |
| 3 | XJGFYTGN2PDS | XJGFYTGN2PDS | Yes | 3.29 |
| 4 | K9WI2HCFEPRT | K9WI2HCFEPRT | Yes | 3.88 |
| 5 | QYV1R8XXLPIN | QYV1R8XXLPIN | Yes | 2.95 |
| 6 | KIJ9JYC8D6KP | KIJ9JYC8D6KP | Yes | 4.57 |
| 7 | 4Q7TTEE8QTRS | 4Q7TTEE8QTRS | Yes | 5.79 |
| 8 | UV5P56LMG077 | UV5P5GLMG077 | No | 4.07 |
| 9 | ALSM3HDK45O3 | ALSM3HDK45O3 | Yes | 3.55 |
| 10 | ZJ7OQN9MRZSS | ZJ70QN9MRZSS | No | 4.95 |
| 11 | U331519DJJWM | U331519DJ1WM | No | 3.98 |
| 12 | ZLJ996X5R15J | ZLJ996X5R15J | Yes | 3.37 |
| 13 | VLTUIQFZ4WWP | VLTUJQFZ4WWP | No | 5.3 |
| 14 | IP6R0YBQ58EE | IP6R0YBQ58EE | Yes | 2.8 |
| 15 | 6LUNK99ZP6AK | 6LJNK99ZP6AK | No | 4.0 |
| 16 | ZMPUBJRTJMOS | ZMPUBJRTJMOS | Yes | 3.62 |
| 17 | 9B319QC9ZBMC | 9B319QC9ZBMC | Yes | 3.93 |
| 18 | E8KKON2XKMY8 | E8KKON2XKMY8 | Yes | 4.02 |
| 19 | BN36OZWBWY6V | BN36OZWBWV6V | No | 3.37 |
| 20 | CKHXWSJHP9OG | CKHXWSJHP9OG | Yes | 3.47 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 5.1 |
| 2 | 7 | 7 | Yes | 3.07 |
| 3 | 4096 | 16384 | No | 15.53 |
| 4 | 10 | 9 | No | 6.11 |
| 5 | 44 | 44 | Yes | 5.59 |
| 6 | 65 | 65 | Yes | 4.17 |
| 7 | 9 | 9 | Yes | 6.32 |
| 8 | 63 | 63 | Yes | 3.52 |
| 9 | 5 | 5 | Yes | 4.02 |
| 10 | 4 | 5 | No | 18.66 |
| 11 | 5 | 18 | No | 10.86 |
| 12 | 9 | 9 | Yes | 4.89 |
| 13 | 60 | 60 | Yes | 4.18 |
| 14 | 28 | 25 | No | 6.54 |
| 15 | 20 | 20 | Yes | 7.89 |
| 16 | 60 | 60 | Yes | 4.56 |
| 17 | 7680 | 7680 | Yes | 4.94 |
| 18 | 6 | 6 | Yes | 8.48 |
| 19 | 16 | 16 | Yes | 6.04 |
| 20 | 64 | 64 | Yes | 7.39 |
