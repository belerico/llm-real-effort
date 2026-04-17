# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 8960 | 38450 | 47410 | 2 | 18 | 26.70 | 534.17 |
| add_numbers | 4880 | 4091 | 8971 | 20 | 0 | 3.60 | 72.12 |
| counting_zeros | 7820 | 33644 | 41464 | 11 | 9 | 18.04 | 361.22 |
| task_decoding | 14260 | 8161 | 22421 | 20 | 0 | 6.35 | 127.12 |
| task_summation | 8180 | 16785 | 24965 | 20 | 0 | 10.13 | 202.72 |
| task_transcription | 5040 | 3870 | 8910 | 8 | 12 | 4.05 | 81.13 |
| task_sequences | 4141 | 12276 | 16417 | 17 | 3 | 9.23 | 184.58 |
| **TOTAL** | **53281** | **117277** | **170558** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 3 6 2 5 1 4 2 6 3 3 4 6 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step by analyzing each empty cell.  Let me work through the constraints for each empty position:  Starting with easier deductions: - Row 1, Column 5: Row 1 has 2,5,4 and Column 5 has 1,6,4,5, so this must be 3 - Row 3, Column 6: Column 6 has 4,6,3,2,1, so this must be 5   - Row 3, Column 5: Row 3 now has 3,1,4,5 and Column 5 needs 2,3, so this must be 2 - Row 3, Column 3: Row 3 now has 3,1,4,2,5, so this must be 6  Continuing with Row 1: - Row 1 now has 2,5,3,4 and needs 1,6 - Column 1 needs 1,6 and Column 3 needs 1,3,4  - So (1,3) = 1 and (1,1) = 6  For Row 4: - Row 4 has 5,6,3 and needs 1,2,4 - Column 1 needs 1 (after 6 placed), so (4,1) = 1 - Column 4 needs 2,6, Row 4 needs 2,4 | No | 28.53 |
| 2 | 1 2 3 5 1 4 2 5 5 4 1 3 6 5 | 1 2 3 5 1 4 2 5 5 4 1 3 6 | No | 26.49 |
| 3 | 6 4 2 2 1 3 2 5 5 6 4 1 3 6 | 6 4 2 2 1 3 5 1 5 6 4 1 3 6 | No | 24.51 |
| 4 | 1 3 5 2 5 5 6 6 4 2 3 2 3 1 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Let me work through this systematically:  Row 1: Missing 1 and 3 - Column 1 is missing 1, so position (1,1) = 1 - That leaves position (1,5) = 3  Row 2: Missing 5 - Column 2 needs 2 or 5, checking constraints shows position (2,2) = 5  Row 3: Missing 2 and 5   - Column 2 | No | 26.23 |
| 5 | 3 4 2 1 6 5 2 6 2 3 1 5 6 4 |  | No | 27.65 |
| 6 | 5 4 6 1 5 5 3 6 2 1 4 6 3 5 | Looking at this 6×6 Sudoku puzzle, I need to fill in the empty cells so that each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Let me solve this systematically:  Row 1: 3, 1, _, 2, _, 6 Missing numbers: 4, 5 Looking at column 3, it already has a 4, so position (1,3) = 5 This means position (1,5) = 4  Row 2: _, 2, 4, _, 3, _ Looking at column 1, it needs a 6, so (2,1) = 6 For the top-right 2×3 box, we need 1 and 5 in positions (2,4) and (2,6) Column 4 analysis shows (2,4) = 1, so (2,6) = 5  Row 3: 4, _, _, _, 1, _ Column 6 needs a 2, so (3,6) = 2 Column 2 needs a 5, so (3,2) = 5   For the middle-left box, we need a 6, so (3,3) = 6 This leaves (3,4) = 3  Row 5: 5, 6, _, 4, 2, | No | 27.21 |
| 7 | 1 2 4 6 5 4 3 2 5 6 4 1 5 2 | Looking at this 6×6 Sudoku puzzle, I need to fill in the empty cells systematically.  Let me work through this step by step:  Starting with Row 5: 2 4 6 3 5 _  This row is missing only 1, so position (5,6) = 1  Column 1: 3, _, 5, 1, 2, 6 This column is missing only 4, so position (2,1) = 4  Now Row 2: 4 _ 3 1 2 _ This row is missing 5 and 6  Looking at the top-left 2×3 box, it needs 1, 2, and 6 Since (1,4) is in the top-right box and Row 1 needs 1 and 2, and (1,2) must be from the remaining numbers in the top-left box, (1,2) = 1  Row 1: 3 1 5 _ 4 6 This row is missing only 2, so (1,4) = 2  Back to Row 2: 4 _ 3 1 2 _ Column 2 needs 5 and 6, and Row 2 needs 5 and 6, so (2,2) and (2,6) are 5 and 6  Looking at the top-right 2×3 box: 2, 4, 6 (from row 1) and 1, 2, _ ( | No | 29.53 |
| 8 | 1 5 4 2 3 4 2 6 4 5 3 2 1 1 | 1 5 4 2 3 4 2 6 4 5 3 2 1 1 | Yes | 23.11 |
| 9 | 4 5 6 6 1 1 4 2 1 3 4 5 4 1 | 4 5 6 6 1 1 4 2 1 3 4 5 4 1 | Yes | 27.64 |
| 10 | 3 6 1 4 5 6 5 6 1 3 4 6 6 2 | 3 6 5 4 1 6 1 6 5 3 4 2 2 6 | No | 27.37 |
| 11 | 4 1 2 6 5 5 1 2 2 4 2 3 2 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers for each empty cell.  Let me work through this systematically by analyzing rows, columns, and 2×3 boxes:  Starting with the more constrained positions: - Row 4 only needs one number (2) in position (4,2) - This helps constrain other positions  Working through the logic: 1. Row 4, column 2: needs 2 2. Row 5, column 2: needs 4 (since column 2 already has 2) 3. Row 5, column 3: needs 2 (only missing number in row 5) 4. Row 6, column 2: needs 3 (only remaining for column 2) 5. Row 6, column 5: needs | No | 27.23 |
| 12 | 6 4 3 1 5 1 4 6 3 4 1 2 6 5 | 4 6 3 1 5 1 4 4 3 6 1 2 6 5 | No | 29.4 |
| 13 | 5 2 5 4 6 3 2 4 4 3 2 6 1 5 | Looking at the 6×6 Sudoku grid, I need to find the missing numbers in each empty cell.  Let me work through this systematically:  Row 1: 4, 6, 1, 2, _, 3 → missing 5 Row 2: _, 3, _, _, _, 1 → need to solve step by step Row 3: 5, 1, _, 6, _, _ Row 4: 1, _, 6, 5, _, _ Row 5: 3, 5, 2, 1, 4, 6 (complete) Row 6: _, 2, 4, 3, _, _  Working through the constraints:  Row 1, Col 5: = 5  Row 2, Col 1: Looking at column 1 and the top-left box constraints = 2 Row 2, Col 4: Looking at column 4 constraints = 4   Row 2, Col 5: Looking at top-right box constraints = 6 Row 2, Col 3: By elimination in row 2 = 5  Row 3, Col 3: Looking at column 3 constraints = 3 Row 3, Col 5: = 2 Row 3, Col 6: = 4  Row 4, Col 2: Looking at column 2 constraints = 4 Row 4, Col 5: = 3 | No | 26.39 |
| 14 | 3 6 5 2 1 1 6 4 5 1 3 6 4 2 |  | No | 30.73 |
| 15 | 4 6 3 2 6 3 4 5 2 6 6 1 3 3 | 4 3 6 2 6 3 4 5 2 6 6 1 3 3 | No | 23.75 |
| 16 | 1 3 4 2 5 6 2 3 1 4 5 5 4 3 |  | No | 26.95 |
| 17 | 2 1 4 1 3 1 6 6 6 4 1 3 2 4 |  | No | 28.04 |
| 18 | 3 1 5 4 6 3 5 3 2 3 6 1 3 5 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically by checking row, column, and 2×3 box constraints.  Let me | No | 29.2 |
| 19 | 3 6 4 2 3 6 1 3 4 1 5 4 4 5 | 3 6 4 2 3 6 1 3 4 5 4 5 | No | 19.5 |
| 20 | 5 2 1 3 5 3 2 5 3 5 6 6 1 5 | 5 2 1 3 5 2 3 5 3 6 5 1 5 | No | 24.52 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1349 | 1349 | Yes | 2.63 |
| 2 | 1633 | 1633 | Yes | 3.76 |
| 3 | 745 | 745 | Yes | 3.76 |
| 4 | 1803 | 1803 | Yes | 3.9 |
| 5 | 2027 | 2027 | Yes | 2.72 |
| 6 | 1311 | 1311 | Yes | 2.76 |
| 7 | 1771 | 1771 | Yes | 3.63 |
| 8 | 1581 | 1581 | Yes | 3.22 |
| 9 | 1917 | 1917 | Yes | 3.41 |
| 10 | 646 | 646 | Yes | 4.32 |
| 11 | 2234 | 2234 | Yes | 5.24 |
| 12 | 1206 | 1206 | Yes | 2.96 |
| 13 | 1309 | 1309 | Yes | 3.93 |
| 14 | 1631 | 1631 | Yes | 6.65 |
| 15 | 1987 | 1987 | Yes | 3.91 |
| 16 | 1611 | 1611 | Yes | 4.98 |
| 17 | 1306 | 1306 | Yes | 1.87 |
| 18 | 1760 | 1760 | Yes | 1.9 |
| 19 | 1984 | 1984 | Yes | 2.91 |
| 20 | 1617 | 1617 | Yes | 3.53 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | I'll count the zeros row by row from the image:  Row 1: 1 0 0 1 0 1 1 1 1 0 → 4 zeros Row 2: 0 0 1 1 0 0 1 1 1 0 → 5 zeros   Row 3: 0 1 1 1 1 1 0 0 0 0 → 5 zeros Row 4: 1 0 0 1 0 0 1 0 0 0 → 7 zeros Row 5: 0 1 0 0 0 1 0 1 1 1 → 5 zeros Row 6: 0 1 0 1 1 1 1 1 1 0 → 3 zeros Row 7: 0 1 0 0 0 1 1 0 0 0 → 7 zeros Row 8: 1 1 1 1 1 0 1 1 0 0 → 3 zeros Row 9: 1 1 1 1 1 1 0 0 1 1 → 2 zeros Row 10: 1 1 0 1 0 0 1 1 1 0 → 4 zeros Row 11: 0 0 0 0 1 0 1 0 1 0 → 7 zeros Row 12: 1 1 1 0 0 1 0 0 0 1 → 5 zeros Row 13: 1 0 0 0 0 0 1 1 0 0 → 7 zeros Row 14: 1 1 0 0 0 0 1 1 0 1 → 5 zeros Row 15: 1 0 1 1 1 1 0 1 0 0 | No | 21.48 |
| 2 | 54 | 54 | Yes | 19.86 |
| 3 | 37 | 37 | Yes | 19.13 |
| 4 | 50 | 50 | Yes | 18.13 |
| 5 | 73 | 59 | No | 16.97 |
| 6 | 62 | 62 | Yes | 20.27 |
| 7 | 40 | 40 | Yes | 16.45 |
| 8 | 58 | 58 | Yes | 21.28 |
| 9 | 41 | 41 | Yes | 18.64 |
| 10 | 74 | 65 | No | 13.06 |
| 11 | 73 | 73 | Yes | 20.36 |
| 12 | 69 | 57 | No | 20.62 |
| 13 | 36 | 34 | No | 16.59 |
| 14 | 43 | 43 | Yes | 18.57 |
| 15 | 38 | 38 | Yes | 14.45 |
| 16 | 49 | 48 | No | 14.29 |
| 17 | 50 | 48 | No | 13.3 |
| 18 | 55 | 55 | Yes | 14.93 |
| 19 | 51 | Looking at the image, I'll count the zeros row by row:  Row 1: 0 1 0 1 0 0 1 1 0 0 → 6 zeros Row 2: 1 0 1 1 1 1 1 0 0 1 → 3 zeros   Row 3: 1 1 0 1 1 1 0 1 1 0 → 3 zeros Row 4: 1 1 0 1 0 0 0 1 1 1 → 4 zeros Row 5: 0 1 0 1 1 1 0 1 1 1 → 3 zeros Row 6: 1 1 1 1 1 0 1 1 1 0 → 2 zeros Row 7: 0 1 1 0 0 1 1 1 1 1 → 3 zeros Row 8: 1 0 1 1 0 1 1 1 0 1 → 3 zeros Row 9: 1 0 1 1 1 1 0 0 1 1 → 3 zeros Row 10: 1 0 1 1 0 1 1 1 0 0 → 4 zeros Row 11: 1 0 1 1 1 1 1 1 1 1 → 1 zero Row 12: 1 1 1 0 1 1 0 1 0 0 → 4 zeros Row 13: 0 1 1 0 1 1 1 0 0 1 → 4 zeros Row 14: 0 1 1 0 0 1 1 1 0 1 → 4 zeros Row 15: 1 1 0 1 1 0 0 1 1 0 → 4 zeros  Total: 6 + 3 + 3 + 4 + 3 | No | 20.94 |
| 20 | 63 | Looking at the image, I'll count the zeros in each row systematically:  Row 1: 0 1 0 1 0 0 1 1 1 0 → 4 zeros Row 2: 1 0 1 0 1 1 0 1 1 1 → 3 zeros Row 3: 0 1 1 1 1 0 0 0 1 0 → 5 zeros Row 4: 0 0 0 0 1 1 1 1 0 0 → 6 zeros Row 5: 1 1 1 1 1 1 1 1 1 0 → 1 zero Row 6: 1 0 1 1 1 0 0 1 1 1 → 3 zeros Row 7: 0 0 0 0 1 1 1 0 1 0 → 6 zeros Row 8: 1 0 0 1 1 1 1 1 1 1 → 2 zeros Row 9: 1 0 1 0 0 0 1 1 1 0 → 5 zeros Row 10: 1 1 0 1 1 1 0 1 1 0 → 3 zeros Row 11: 0 1 0 1 0 1 0 0 0 0 → 7 zeros Row 12: 1 0 1 1 1 0 1 0 1 0 → 4 zeros Row 13: 0 1 1 0 0 0 1 1 1 0 | No | 21.57 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ONRBHJP | ONRBHJP | Yes | 6.06 |
| 2 | JSIDWFQ | JSIDWFQ | Yes | 4.71 |
| 3 | KZVDEHO | KZVDEHO | Yes | 5.97 |
| 4 | JYVCFNW | JYVCFNW | Yes | 5.24 |
| 5 | VFHWDGR | VFHWDGR | Yes | 5.32 |
| 6 | NOEXWTZ | NOEXWTZ | Yes | 5.89 |
| 7 | IZKBOJM | IZKBOJM | Yes | 6.58 |
| 8 | DICHMFK | DICHMFK | Yes | 5.37 |
| 9 | EBOUZLC | EBOUZLC | Yes | 5.8 |
| 10 | CJEMFBR | CJEMFBR | Yes | 5.39 |
| 11 | DGZSCEF | DGZSCEF | Yes | 5.79 |
| 12 | ZEVNLPJ | ZEVNLPJ | Yes | 4.48 |
| 13 | MBCYZWN | MBCYZWN | Yes | 4.94 |
| 14 | ETWKHJN | ETWKHJN | Yes | 8.84 |
| 15 | SPNCDGY | SPNCDGY | Yes | 6.62 |
| 16 | GIXSQCU | GIXSQCU | Yes | 5.95 |
| 17 | WLHRZVG | WLHRZVG | Yes | 7.95 |
| 18 | YVQOLWP | YVQOLWP | Yes | 5.78 |
| 19 | PBUCEQZ | PBUCEQZ | Yes | 7.07 |
| 20 | DKFTNYI | DKFTNYI | Yes | 13.17 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.27 |
| 2 | [0.7, 9.3] | 9.3 0.7 | Yes | 6.49 |
| 3 | [2.3, 7.7] | 2.3 7.7 | Yes | 10.87 |
| 4 | [3.0, 7.0] | 3.0 7.0 | Yes | 10.1 |
| 5 | [2.2, 7.8] | 7.8 2.2 | Yes | 9.93 |
| 6 | [2.4, 7.6] | 7.6 2.4 | Yes | 13.82 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 9.62 |
| 8 | [2.7, 7.3] | 7.3 2.7 | Yes | 9.78 |
| 9 | [2.2, 7.8] | 7.8 2.2 | Yes | 9.83 |
| 10 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.14 |
| 11 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.89 |
| 12 | [0.8, 9.2] | 9.2 0.8 | Yes | 9.64 |
| 13 | [3.0, 7.0] | 7.0 3.0 | Yes | 9.09 |
| 14 | [0.9, 9.1] | 9.1 0.9 | Yes | 13.17 |
| 15 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.16 |
| 16 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.32 |
| 17 | [2.1, 7.9] | 2.1 7.9 | Yes | 11.07 |
| 18 | [4.1, 5.9] | 5.9 4.1 | Yes | 9.17 |
| 19 | [1.3, 8.7] | 8.7 1.3 | Yes | 11.8 |
| 20 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.38 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 13KRHIQ5TXH2 | 13KBHIQ5TXH2 | No | 4.27 |
| 2 | GBWQSJXULDBF | GBWOSJXULDBF | No | 3.58 |
| 3 | 96XYMB83Q7RC | 96XYMB33Q7RC | No | 4.38 |
| 4 | Y13W2VHEEXVY | Y13W2VHEEXVY | Yes | 4.92 |
| 5 | 0N79TLG4CT60 | 0N79TLG4CT60 | Yes | 3.34 |
| 6 | WIJMDKGVQ2YC | WIJMDKGVQ2YG | No | 4.16 |
| 7 | KJ8WBWU1O576 | KJ8WBWU10578 | No | 3.59 |
| 8 | TE4PSU3A44RN | TE4PSU3A44RN | Yes | 4.7 |
| 9 | 3MNGUKM0D8VY | 3MNGUKMQD8VY | No | 3.75 |
| 10 | 0XTSSBLH3Z67 | 0XTSSBBLH3Z67 | No | 7.48 |
| 11 | LJH0F2SLPQL6 | LJHQF2SLPQLG | No | 3.91 |
| 12 | MTKQR145LM9D | MTKQR145LM9D | Yes | 3.34 |
| 13 | ITLKM8ADRWGY | ITLKM3ADRWGY | No | 3.51 |
| 14 | 85BYOGRRX6HR | 85BYQGRRX6HR | No | 3.41 |
| 15 | MWT4KSHM6GZO | MWT4KSHM6GZO | Yes | 3.54 |
| 16 | S1TS6W228E9S | S1TS6W228E9S | Yes | 3.63 |
| 17 | H5CYZZEZK44M | H5CYZZEZK44M | Yes | 3.95 |
| 18 | S2W9ODEASZI7 | S2W9ODEASZI7 | Yes | 3.49 |
| 19 | B9MB6HZLUZT0 | B9MB6HZLUZTO | No | 4.11 |
| 20 | WXIQK3EZZPCY | WXIOK3EZZPCY | No | 3.98 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 5 | Yes | 4.67 |
| 2 | 31 | 31 | Yes | 3.66 |
| 3 | 1440 | 1440 | Yes | 4.29 |
| 4 | 26 | 26 | Yes | 11.96 |
| 5 | 20 | 20 | Yes | 13.21 |
| 6 | 5 | 8 | No | 13.6 |
| 7 | 1 | 1 | Yes | 5.56 |
| 8 | 28 | 28 | Yes | 4.35 |
| 9 | 73 | 73 | Yes | 4.54 |
| 10 | 9 | 9 | Yes | 5.43 |
| 11 | 3 | 3 | Yes | 15.11 |
| 12 | 65 | 65 | Yes | 6.62 |
| 13 | 7680 | 7680 | Yes | 5.39 |
| 14 | 64 | 64 | Yes | 5.19 |
| 15 | 4096 | 16384 | No | 13.63 |
| 16 | 3 |  | No | 34.97 |
| 17 | 4 | 4 | Yes | 17.72 |
| 18 | 23 | 23 | Yes | 5.29 |
| 19 | 63 | 63 | Yes | 4.45 |
| 20 | 36 | 36 | Yes | 4.92 |
