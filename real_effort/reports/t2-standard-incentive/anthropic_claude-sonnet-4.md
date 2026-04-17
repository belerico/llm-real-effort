# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8600 | 38956 | 47556 | 3 | 17 | 27.00 | 540.15 |
| add_numbers | 4520 | 3377 | 7897 | 20 | 0 | 3.07 | 61.59 |
| counting_zeros | 7460 | 31474 | 38934 | 9 | 11 | 17.41 | 348.52 |
| task_decoding | 13900 | 8926 | 22826 | 18 | 2 | 7.02 | 140.72 |
| task_summation | 7820 | 17985 | 25805 | 20 | 0 | 10.81 | 216.35 |
| task_transcription | 4652 | 3894 | 8546 | 15 | 5 | 4.21 | 84.34 |
| task_sequences | 3781 | 9424 | 13205 | 17 | 3 | 7.09 | 141.74 |
| **TOTAL** | **50733** | **114036** | **164769** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 4 1 3 5 4 5 6 6 3 3 4 5 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers while ensuring each row, column, and 2×3 box contains numbers 1-6 exactly once.  Let me work through this systematically:  First, I'll identify what numbers are missing in each row and column, then use logical deduction:  Starting with easier deductions: - Row 5 is missing only one number (3), so position (5,1) = 3 - Column 3 is missing only one number (6), so position (1,3) = 6   - Column 5 is missing only one number (1), | No | 27.33 |
| 2 | 2 2 6 4 5 4 1 3 2 4 1 1 4 3 | 2 2 6 4 5 4 1 3 2 4 1 1 4 3 | Yes | 17.67 |
| 3 | 1 4 2 5 1 6 3 1 5 6 2 4 1 5 | 1 4 2 5 1 6 3 1 5 6 2 4 1 5 | Yes | 24.08 |
| 4 | 3 1 5 6 4 2 4 2 5 4 6 3 5 2 |  | No | 27.34 |
| 5 | 5 2 5 3 4 6 3 5 3 6 1 6 3 6 |  | No | 29.17 |
| 6 | 1 4 5 4 1 5 6 2 5 6 3 2 4 6 |  | No | 27.7 |
| 7 | 5 3 6 1 4 1 2 5 2 5 1 5 3 4 |  | No | 28.74 |
| 8 | 5 1 3 3 6 2 5 2 1 3 1 5 6 2 |  | No | 29.43 |
| 9 | 1 3 4 2 6 1 6 2 5 4 2 6 3 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell, working systematically through the constraints.  Let me identify the empty positions in reading order (left to right, top to bottom): - Row 1, Col 3 - Row 1, Col 5   - Row 2, Col 1 - Row 2, Col 3 - Row 2, Col 6 - Row 3, Col 2 - Row 3, Col 3 - Row 3, Col 5 - Row 3, Col 6 - Row 4, Col 2 - Row 4, Col 4 - Row 4, Col 5 - Row 5, Col 3 - Row 5, Col 5  Working through the constraints systematically:  1. Row 2, Col 1 = 4 (only number missing from column 1) 2. Row 4, Col 4 = 2 (only number missing from column 4)   3. Row 3, Col 2 = 1 (column 2 constraint with row 3) 4. Row 4, Col 2 = 4 (remaining number for column 2) 5. Row 1, Col 3 = 1 (top-left box and row constraints) 6. Row 1, | No | 33.45 |
| 10 | 6 4 3 4 2 1 1 5 2 6 5 6 3 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers and list them in reading order.  Let me work through this systematically:  Starting grid: ``` 2 5 3 _ 1 _ _ 6 1 _ _ 5 4 _ 2 5 3 6 _ 4 _ _ _ 3 _ 2 _ _ 4 1 _ 3 4 1 5 2 ```  Let me solve step by step:  Row 3 is missing only 1, which must go in column 2: (3,2) = 1 Row 6 is missing only 6, which must go in column 1: (6,1) = 6 Column 6 is now missing only 4, which must go in row 1: (1,6) = 4  Updated grid: ``` 2 5 3 _ 1 4 _ 6 1 _ _ 5 4 1 2 5 3 6 _ 4 _ _ _ 3 _ 2 _ _ 4 1 6 3 4 1 5 2 ```  Row 1 is missing only 6: (1,4) = 6  For the top-left 2×3 box (rows 1-2, columns 1-3), it has: 2,5,3 | No | 26.46 |
| 11 | 2 3 6 4 2 3 5 2 3 2 6 6 5 4 | 2 3 6 4 2 3 5 2 6 2 6 6 5 4 | No | 25.89 |
| 12 | 5 4 1 3 1 2 6 6 3 5 1 3 5 2 |  | No | 28.96 |
| 13 | 6 4 1 2 4 4 2 5 6 3 5 6 2 4 | 4 5 1 2 4 4 5 5 6 3 5 6 2 4 | No | 19.94 |
| 14 | 6 1 6 1 3 5 3 6 6 3 1 4 2 3 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers while ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Let me solve this systematically:  Starting with what's given and working through the constraints:  Row 1: 5 3 _ 4 2 _ → needs 1,6 Row 2: 2 _ _ _ _ 4 → needs 1,3,5,6   Row 3: 1 4 2 5 6 3 → complete Row 4: _ 2 4 _ 1 5 → needs 3,6 Row 5: _ 5 _ _ 4 2 → needs 1,3,6 Row 6: _ 1 5 _ _ 6 → needs 2,3,4  Working through column and box constraints:  Column 2 needs only 6 in row 2, so (2,2) = 6 Column 6 needs only 1 in row 1, so (1,6) | No | 29.09 |
| 15 | 3 5 4 6 3 4 5 1 1 4 2 6 5 1 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell, working systematically through rows, columns, and 2×3 boxes.  Let me solve each empty position:  Row 1, Column 2: Row 1 has {2,1}, Column 2 has {5,1,6,2 | No | 26.98 |
| 16 | 6 4 3 4 1 3 6 2 6 5 5 5 2 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in reading order.  Let me work through the grid systematically:  Current grid: ``` 5 2 _ 1 _ _ 3 6 4 2 5 1 _ _ _ 5 _ _ _ 3 1 4 2 _ 2 4 _ 3 1 6 1 _ _ 6 3 _ ```  Working through each empty position:  Row 1, Col 3: Row 1 needs {3,4,6}, Column 3 needs {2,3,5,6}, Box 1 needs {1} → Must be 3 Row 1, Col 5: Row 1 needs {4,6}, Column 5 needs {4,6}, Box 2 needs {3,4,6} → Must be 4   Row 1, Col 6: Row 1 needs {6}, Column 6 needs {2,3,4,5}, Box 2 needs {3,6} → Must be 6  Row 3, Col 1: Row 3 needs {1,2,3,4,6}, Column 1 needs {4,6}, Box 3 needs {1,5,6} → Must be 6 Row 3, Col 2: Row 3 needs {1,2,4}, Column 2 needs {1,5}, Box 3 needs {1,5} → Must be 1 Row 3, Col 3: Row 3 needs {2,4}, Column 3 needs {2,5,6}, Box 3 needs {5} → Must be 5 Row 3, Col 5: Row 3 needs {2,4}, Column 5 needs {6}, Box 4 needs {1,3,6} → Must be | No | 29.75 |
| 17 | 6 2 4 1 3 6 2 1 1 6 5 6 3 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell.  Let me work through this systematically by analyzing rows, columns, and 2×3 boxes:  Starting with the easier deductions: - Row 3 is missing only 1, which goes in position (3,6) - Row 5 is missing only 6, which goes in position (5,2)  Now analyzing columns: - Column 4 has 1,2,3,4,5 so needs 6 in row 2: (2,4) = 6 - Column 5 has 3,4,6,2,1 so needs 5 in row 4: (4,5) | No | 27.93 |
| 18 | 5 6 1 4 2 3 6 1 2 3 1 5 4 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers for each empty cell.  Let me solve this systematically by analyzing rows, columns, and 2×3 boxes:  Starting with easier deductions: - Row 2 is missing only one number: 4 (goes in position 2,2) - Row 3 is missing only one number: 2 (goes in position 3,1) - Column 4 is missing only one number: 6 (goes in position 4,4)  Continuing with the analysis: - Column 1 needs 3 and 5 in the remaining positions - Row 1 needs 1, 5, and 6 - Since position (1,1) is in both column 1 and row 1, and column 1 needs 5, position (1,1) = 5 - This means position (5,1) = 3  For row 1: With 5 in position (1,1), I need 1 and 6 in positions (1,3) and (1,6) - Column 3 needs 3, 5, and 6 in remaining positions - Since row 1 position (1,3) can be 1 or 6, and column 3 needs 6, position (1,3) = 6 - Therefore position (1,6) = 1  Continuing this logical process for the remaining cells: - Position (4,6) = 2 (completing the pattern in that 2×3 box) - Position (5,6) = 6 (completing column 6) - Position (4,5) = 1 (completing row 4's requirements) - Position | No | 29.23 |
| 19 | 3 5 3 6 4 6 4 3 1 4 4 1 2 3 | 3 5 4 6 3 6 3 4 1 4 4 1 2 3 | No | 24.01 |
| 20 | 3 6 5 6 3 5 3 2 3 5 1 2 6 5 | 3 6 5 6 3 5 3 2 3 5 1 2 6 5 | Yes | 26.81 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1910 | 1910 | Yes | 2.33 |
| 2 | 2034 | 2034 | Yes | 4.24 |
| 3 | 1549 | 1549 | Yes | 2.97 |
| 4 | 1947 | 1947 | Yes | 2.75 |
| 5 | 1263 | 1263 | Yes | 2.19 |
| 6 | 1615 | 1615 | Yes | 2.42 |
| 7 | 1544 | 1544 | Yes | 2.79 |
| 8 | 969 | 969 | Yes | 2.23 |
| 9 | 1882 | 1882 | Yes | 2.75 |
| 10 | 1027 | 1027 | Yes | 2.22 |
| 11 | 1504 | 1504 | Yes | 2.64 |
| 12 | 1813 | 1813 | Yes | 3.85 |
| 13 | 1948 | 1948 | Yes | 4.09 |
| 14 | 1570 | 1570 | Yes | 2.55 |
| 15 | 2178 | 2178 | Yes | 4.13 |
| 16 | 2117 | 2117 | Yes | 6.23 |
| 17 | 928 | 928 | Yes | 2.33 |
| 18 | 1731 | 1731 | Yes | 3.87 |
| 19 | 1174 | 1174 | Yes | 2.15 |
| 20 | 1430 | 1430 | Yes | 2.73 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 65 | No | 13.65 |
| 2 | 66 | 55 | No | 12.45 |
| 3 | 69 | 67 | No | 15.91 |
| 4 | 51 | Looking at the image, I need to count each zero in the paragraph of binary digits. Let me go through each line systematically:  Line 1: 0 1 0 1 1 0 0 1 0 0 → 6 zeros Line 2: 0 1 1 0 1 0 0 1 1 1 → 4 zeros Line 3: 1 0 1 1 1 1 1 1 0 1 → 2 zeros Line 4: 1 0 1 1 1 1 0 1 1 1 → 2 zeros Line 5: 1 1 1 1 0 0 1 1 1 0 → 3 zeros Line 6: 0 1 1 1 1 0 1 1 0 1 → 3 zeros Line 7: 1 1 1 1 | No | 23.82 |
| 5 | 39 | 39 | Yes | 15.53 |
| 6 | 62 | 62 | Yes | 20.18 |
| 7 | 53 | 53 | Yes | 18.11 |
| 8 | 40 | 35 | No | 12.95 |
| 9 | 72 | 61 | No | 19.6 |
| 10 | 53 | 49 | No | 16.93 |
| 11 | 66 | 53 | No | 22.91 |
| 12 | 59 | 59 | Yes | 20.89 |
| 13 | 55 | 47 | No | 12.74 |
| 14 | 71 | 71 | Yes | 19.78 |
| 15 | 63 | 63 | Yes | 20.85 |
| 16 | 45 | 45 | Yes | 15.11 |
| 17 | 49 | 49 | Yes | 15.45 |
| 18 | 57 | 62 | No | 16.25 |
| 19 | 54 | 36 | No | 17.87 |
| 20 | 58 | 58 | Yes | 17.19 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NBGKPQL | NBGKPQL | Yes | 4.62 |
| 2 | UAGKPTS | UAGKPTS | Yes | 6.39 |
| 3 | WQIPNCT | WQIPNCT | Yes | 4.57 |
| 4 | MFLZVHB | MFLZVHB | Yes | 5.18 |
| 5 | YUALSFX | YUALSFX | Yes | 14.0 |
| 6 | QOYSXEK | QOYSXEK | Yes | 5.33 |
| 7 | IJCKQOY | IJCKQOY | Yes | 7.49 |
| 8 | YGRSANI | YGRSANI | Yes | 7.47 |
| 9 | YMIANXP | YMIANXP | Yes | 5.29 |
| 10 | GUOISNC | GUOISNC | Yes | 7.71 |
| 11 | VYKHJQD | VYKHJQD | Yes | 5.1 |
| 12 | HLFZKED | HLFZKED | Yes | 6.03 |
| 13 | ZMXVYLO | ZMXVYLO | Yes | 5.45 |
| 14 | BPTAYHR | BPTAYHR | Yes | 10.1 |
| 15 | LQMUNWG | LQMUNWG | Yes | 6.52 |
| 16 | VEHGJRS | VEHJRS | No | 7.93 |
| 17 | BMFULXQ | BMFULXQ | Yes | 4.87 |
| 18 | PJAKHSI | PJAKSHI | No | 9.77 |
| 19 | ZSNETWJ | ZSNETWJ | Yes | 11.23 |
| 20 | AEZMYBP | AEZMYBP | Yes | 5.43 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 0.4 9.6 | Yes | 10.05 |
| 2 | [1.2, 8.8] | 1.2 8.8 | Yes | 10.45 |
| 3 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.27 |
| 4 | [1.8, 8.2] | 1.8 8.2 | Yes | 17.8 |
| 5 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.39 |
| 6 | [4.7, 5.3] | 4.7 5.3 | Yes | 9.51 |
| 7 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.09 |
| 8 | [1.1, 8.9] | 1.1 8.9 | Yes | 11.43 |
| 9 | [3.5, 6.5] | 3.5 6.5 | Yes | 9.73 |
| 10 | [3.8, 6.2] | 6.2 3.8 | Yes | 11.3 |
| 11 | [0.1, 9.9] | 9.9 0.1 | Yes | 9.9 |
| 12 | [1.6, 8.4] | 1.6 8.4 | Yes | 14.16 |
| 13 | [2.8, 7.2] | 7.2 2.8 | Yes | 7.95 |
| 14 | [1.1, 8.9] | 8.9 1.1 | Yes | 11.66 |
| 15 | [4.3, 5.7] | 5.7 4.3 | Yes | 10.13 |
| 16 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.84 |
| 17 | [1.2, 8.8] | 8.8 1.2 | Yes | 12.45 |
| 18 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.35 |
| 19 | [1.2, 8.8] | 1.2 8.8 | Yes | 10.79 |
| 20 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.88 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | R2USNYQASK50 | R2USNYOASK50 | No | 4.47 |
| 2 | 779RYURIO285 | 779RYURIO285 | Yes | 3.55 |
| 3 | 4X7FHWE423NJ | 4X7FHWE423NJ | Yes | 4.63 |
| 4 | 1J0TRKBTZ5LC | 1J0TRKBTZ5LC | Yes | 4.12 |
| 5 | RLYBSQ5GFVVX | RLYBSQ5GFVVX | Yes | 3.95 |
| 6 | O6DBUJWN0D7C | O6DBUJWN0D7C | Yes | 4.24 |
| 7 | UXD576TMZBT2 | UXD576TMZBT2 | Yes | 3.71 |
| 8 | RPG4RAZB8GMS | RPGJRAZB8GMS | No | 4.83 |
| 9 | IM4HERK1D162 | IM4HERK1D162 | Yes | 3.33 |
| 10 | LQJ6FO56FP26 | LQJ6FO56FP26 | Yes | 3.99 |
| 11 | Y74P5VS0A70N | Y74P5VS0A70N | Yes | 3.64 |
| 12 | ZCRR6F9BYK86 | ZCRR6F9BYK86 | Yes | 3.47 |
| 13 | 12ZHPK755O2M | 12ZHPK75502M | No | 6.54 |
| 14 | KQBJHVL9VB7H | KQBJHVL9VB7H | Yes | 5.05 |
| 15 | V9MAFHHBGGSZ | V9MAFHH8GGSZ | No | 4.8 |
| 16 | RTCOXD74V3R7 | RTCOXD74V3R7 | Yes | 3.75 |
| 17 | GP1GE64PO6L4 | GP1GE64PO6L4 | Yes | 3.36 |
| 18 | RIV42ZI4T4IN | RIV42ZI4T4IN | Yes | 5.34 |
| 19 | CH6SJNKF3AQU | CH6SJNKF3AQU | Yes | 4.02 |
| 20 | L8A7HLV760HD | L3A7HLV760HD | No | 3.45 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 13.5 |
| 2 | 1440 | 1440 | Yes | 5.86 |
| 3 | 5 | 14 | No | 11.17 |
| 4 | 31 | 31 | Yes | 5.44 |
| 5 | 67 | 67 | Yes | 4.44 |
| 6 | 36 | 36 | Yes | 3.13 |
| 7 | 7 | 7 | Yes | 5.06 |
| 8 | 44 | 44 | Yes | 8.01 |
| 9 | 28 | 28 | Yes | 6.14 |
| 10 | 16 | 16 | Yes | 4.57 |
| 11 | 9 | 9 | Yes | 5.6 |
| 12 | 39 | 39 | Yes | 5.07 |
| 13 | 23 | 23 | Yes | 5.22 |
| 14 | 793 | 793 | Yes | 3.39 |
| 15 | 4096 | 65536 | No | 17.61 |
| 16 | 6 | 6 | Yes | 5.13 |
| 17 | 1 | 1 | Yes | 5.28 |
| 18 | 60 | 60 | Yes | 3.55 |
| 19 | 3 | 35 | No | 18.8 |
| 20 | 19 | 19 | Yes | 4.79 |
