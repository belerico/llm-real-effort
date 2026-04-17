# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
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
| sudoku_game | 8380 | 38075 | 46455 | 5 | 15 | 27.26 | 545.31 |
| add_numbers | 4300 | 2992 | 7292 | 20 | 0 | 2.85 | 57.16 |
| counting_zeros | 7240 | 35270 | 42510 | 13 | 7 | 19.00 | 380.36 |
| task_decoding | 13680 | 8876 | 22556 | 17 | 3 | 6.77 | 135.57 |
| task_summation | 7600 | 17564 | 25164 | 20 | 0 | 10.44 | 209.0 |
| task_transcription | 4460 | 3752 | 8212 | 15 | 5 | 4.08 | 81.75 |
| task_sequences | 3561 | 9308 | 12869 | 18 | 2 | 6.67 | 133.34 |
| **TOTAL** | **49221** | **115837** | **165058** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 1 3 1 5 6 3 1 2 5 2 6 1 |  | No | 32.89 |
| 2 | 3 2 5 6 1 3 6 3 4 5 1 2 4 3 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers and solve systematically.  Let me work through the grid step by step:  Starting grid: ``` _ 1 _ \| _ 4 6 5 _ _ \| 4 2 _ ------+------ 4 2 6 \| 3 1 5 _ _ _ \| 2 _ _ ------+------ _ 5 3 \| 1 6 4 1 _ 5 \| 6 _ 2 ```  Row 5, column 1: Only missing 2 in that position, so (5,1) = 2  Row 1, column | No | 30.53 |
| 3 | 4 6 2 3 5 3 5 2 6 6 1 2 4 6 | 4 6 2 3 5 3 5 2 6 6 1 2 4 6 | Yes | 25.43 |
| 4 | 4 3 5 2 5 3 6 4 5 6 3 2 1 3 | 4 3 5 2 5 3 6 4 5 6 3 2 1 3 | Yes | 20.62 |
| 5 | 4 6 5 2 4 5 1 4 3 3 5 1 4 1 | 5 4 6 2 4 5 1 3 4 3 5 1 4 1 | No | 24.61 |
| 6 | 3 1 2 3 2 3 4 1 4 3 6 2 5 1 | 3 1 2 3 2 3 4 1 4 6 3 2 5 1 | No | 23.97 |
| 7 | 2 3 1 6 5 4 1 3 3 4 4 6 1 1 |  | No | 28.45 |
| 8 | 5 3 1 5 3 3 1 4 6 3 4 5 4 6 |  | No | 28.43 |
| 9 | 3 6 4 1 5 3 1 6 3 4 6 5 6 1 | 3 6 4 1 5 3 1 6 3 4 6 5 6 1 | Yes | 26.03 |
| 10 | 2 1 4 5 6 5 4 6 1 6 3 4 1 3 | Looking at this 6×6 Sudoku puzzle, I need to solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me start with the easiest deductions:  Row 5 is missing only one number (4) in position (5,3): Row 5: 5 3 4 1 2 6  Now column 5 is missing only 6, which must go in row 3: Row 3: 3 _ 2 _ 6 _  Column 6 needs 1 and 3. Row 3 needs 1, 4, 5 in its remaining positions. The intersection gives us 1 for position (3,6): Row 3: 3 _ 2 _ 6 1  This means column 6 position (6,2) must be 3: Row 6: 4 _ 6 2 5 3  Continuing this process of elimination using the constraints of rows, columns, and 2×3 boxes:  Row 1: 6 2 1 3 4 5 Row 2: 1 4 5 6 3 2   Row 3: 3 5 2 4 6 1 Row | No | 31.16 |
| 11 | 2 1 6 6 1 1 3 2 6 5 4 5 4 3 | 2 1 6 1 1 3 2 6 4 5 5 3 4 | No | 21.64 |
| 12 | 5 1 4 3 5 2 2 5 1 3 6 6 5 1 | 5 1 4 | No | 31.62 |
| 13 | 1 3 5 3 5 2 4 6 1 4 1 4 3 1 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically by | No | 30.49 |
| 14 | 6 5 6 3 1 2 6 2 4 5 1 3 5 2 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in reading order.  Let me solve this step by step:  **Row 2, Column 5**: Row 2 has 1,4,2,5,3, so it's missing 6.  **Row 3**: I need to determine what goes in each empty cell by checking row, column, and box constraints.  **Row 4**: Similarly checking constraints for the empty positions.  **Row 5**: Has 4,2,3,6, so missing 1 and 5.  **Row 6**: Has 1,4,6, so missing 2,3,5.  Working through the constraints systematically:  - Row 2, Col 5: **6** - Row 3, Col 1: **5**  - Row 3, Col 2: **6** - Row 3, Col 3: **3** - Row 3, Col 4: **1** - Row 3, Col 5: **2** - Row 4, Col 1: **2** - Row 4, Col 2: **4** - Row 4, Col 5: **6** - Row 5, Col 2: **1** - Row | No | 30.45 |
| 15 | 2 5 5 4 5 3 3 5 2 5 1 6 1 5 |  | No | 28.25 |
| 16 | 3 6 4 6 4 5 3 4 1 5 3 1 5 6 | 3 4 6 6 4 5 3 1 4 3 1 6 5 | No | 25.34 |
| 17 | 2 3 1 1 3 5 4 1 4 6 6 1 2 4 | 2 3 1 1 3 5 4 1 4 6 6 1 2 4 | Yes | 25.31 |
| 18 | 2 4 6 1 6 5 1 5 4 3 2 5 4 3 | 2 4 6 1 6 5 1 5 4 3 2 5 4 3 | Yes | 25.38 |
| 19 | 5 2 1 5 4 3 1 1 2 6 2 4 3 1 |  | No | 28.64 |
| 20 | 6 4 2 1 1 5 3 2 6 3 1 3 5 4 | 6 1 2 4 1 3 5 3 6 1 3 4 5 | No | 25.88 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1469 | 1469 | Yes | 3.37 |
| 2 | 2333 | 2333 | Yes | 3.98 |
| 3 | 1270 | 1270 | Yes | 2.27 |
| 4 | 1904 | 1904 | Yes | 3.85 |
| 5 | 1465 | 1465 | Yes | 2.56 |
| 6 | 2136 | 2136 | Yes | 1.84 |
| 7 | 1742 | 1742 | Yes | 2.9 |
| 8 | 2079 | 2079 | Yes | 2.12 |
| 9 | 1821 | 1821 | Yes | 1.84 |
| 10 | 1804 | 1804 | Yes | 2.55 |
| 11 | 1172 | 1172 | Yes | 3.43 |
| 12 | 732 | 732 | Yes | 3.45 |
| 13 | 896 | 896 | Yes | 4.26 |
| 14 | 1752 | 1752 | Yes | 2.69 |
| 15 | 2193 | 2193 | Yes | 4.97 |
| 16 | 1001 | 1001 | Yes | 2.44 |
| 17 | 1557 | 1557 | Yes | 2.44 |
| 18 | 1531 | 1531 | Yes | 1.82 |
| 19 | 1393 | 1393 | Yes | 2.42 |
| 20 | 1278 | 1278 | Yes | 1.85 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 | 49 | Yes | 19.55 |
| 2 | 70 | Looking at the paragraph of 0s and 1s, I'll count each zero systematically by going through each row:  Row 1: 0 1 0 0 1 1 0 1 1 0 → 5 zeros Row 2: 1 0 1 1 1 1 1 1 1 1 → 1 zero   Row 3: 0 0 0 1 1 0 1 0 0 0 → 7 zeros Row 4: 1 1 0 0 1 1 0 0 0 1 → 5 zeros Row 5: 1 1 0 1 1 0 0 1 1 1 → 3 zeros Row 6: 0 1 1 0 1 0 1 1 1 1 → 3 zeros Row 7: 1 0 0 1 1 1 0 1 1 1 → 3 zeros Row 8: 1 0 1 1 1 1 0 1 1 0 → 3 zeros Row 9: 1 0 1 1 1 0 1 0 0 0 → 5 zeros Row 10: 0 0 0 1 0 0 0 1 0 0 → 8 zeros Row 11: 0 0 0 0 1 1 1 1 0 1 → 5 zeros Row 12: 1 1 0 0 0 0 1 1 1 0 → 5 zeros Row 13: 1 1 1 0 1 0 1 0 0 0 → 5 zeros Row 14: 0 0 0 1 1 1 1 1 1 0 → 4 zeros Row 15: 0 0 1 0 0 0 0 0 1 0 → 8 zeros  Total: 5+1+7+5+3 | No | 22.18 |
| 3 | 42 | 42 | Yes | 15.35 |
| 4 | 62 | 62 | Yes | 20.24 |
| 5 | 52 | 52 | Yes | 20.14 |
| 6 | 64 | 59 | No | 20.6 |
| 7 | 63 | 53 | No | 16.91 |
| 8 | 53 | 53 | Yes | 20.95 |
| 9 | 42 | 42 | Yes | 18.23 |
| 10 | 47 | 47 | Yes | 16.55 |
| 11 | 70 | 70 | Yes | 21.29 |
| 12 | 72 | Looking at the image, I'll count the zeros row by row:  Row 1: 0 0 0 0 1 1 0 1 1 1 → 4 zeros Row 2: 0 1 1 1 1 1 0 1 1 1 → 2 zeros Row 3: 1 0 0 1 1 1 1 1 0 1 → 3 zeros Row 4: 1 0 1 0 1 1 1 0 0 1 → 4 zeros Row 5: 1 1 1 0 0 1 1 0 1 1 → 3 zeros Row 6: 0 0 0 0 1 1 0 1 1 1 → 4 zeros Row 7: 0 1 1 0 1 0 0 0 0 1 → 5 zeros Row 8: 0 1 1 1 1 1 0 1 1 1 → 2 zeros Row 9: 0 1 0 0 0 1 0 0 0 1 → 6 zeros Row 10: 0 1 1 0 0 1 0 0 0 1 → 5 zeros Row 11: 1 0 1 0 0 0 1 0 0 1 → 5 zeros Row 12: 0 1 0 0 1 1 0 0 1 1 → 4 zeros Row 13: 0 0 0 0 0 0 0 0 0 0 → 10 zeros Row 14: 1 1 1 1 1 1 1 1 1 1 → 0 zeros Row 15: 0 0 0 1 0 0 1 0 0 0 → 7 zeros  Total: 4+2+3+4+3+4+5+2+6+ | No | 20.78 |
| 13 | 36 | 36 | Yes | 13.89 |
| 14 | 68 | Looking at the image, I'll count the zeros line by line:  Line 1: 0 0 0 1 0 1 1 1 0 1 → 5 zeros Line 2: 1 1 0 1 1 1 1 1 1 1 → 1 zero Line 3: 0 1 1 1 0 1 0 0 1 0 → 5 zeros Line 4: 0 1 1 1 0 1 1 1 1 1 → 2 zeros Line 5: 0 0 1 1 0 1 1 | No | 22.76 |
| 15 | 40 | 40 | Yes | 20.22 |
| 16 | 61 | 61 | Yes | 22.39 |
| 17 | 73 | 73 | Yes | 15.31 |
| 18 | 54 | 46 | No | 16.46 |
| 19 | 73 | 73 | Yes | 19.86 |
| 20 | 72 | 71 | No | 16.37 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MOCJAWK | MOCJAWK | Yes | 5.54 |
| 2 | FRPMAKN | FRPMAKN | Yes | 6.54 |
| 3 | SOHMPCV | SOHMPÇV | No | 10.22 |
| 4 | YBPMDCN | YBPMDCN | Yes | 5.75 |
| 5 | PXVOEUA | PXVOEUA | Yes | 9.82 |
| 6 | UFMTKAL | UFMTKAL | Yes | 7.46 |
| 7 | XRFWMLD | XRFWMLD | Yes | 4.49 |
| 8 | VAISYWN | VAISYWN | Yes | 6.25 |
| 9 | ZVMINLA | ZVMINLA | Yes | 7.76 |
| 10 | AUKNFBE | AUKNFBE | Yes | 8.0 |
| 11 | DQGMYTZ | DQGMYTZ | Yes | 4.54 |
| 12 | RHLTIFU | RHLTIF | No | 11.18 |
| 13 | GQBAPRH | GQBAPRH | Yes | 4.94 |
| 14 | DUEXQVO | DUEXQVO | Yes | 5.67 |
| 15 | SEDTKWL | SEDTKWL | Yes | 4.92 |
| 16 | JMRDAYW | JMRDAYW | Yes | 6.74 |
| 17 | KBXTQYF | KBXTQYF | Yes | 6.09 |
| 18 | PEWRVFT | PEWRFT | No | 9.14 |
| 19 | RFTDQYV | RFTDQYV | Yes | 4.33 |
| 20 | JUYQHTD | JUYQHTD | Yes | 5.99 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.7, 9.3] | 0.7 9.3 | Yes | 9.13 |
| 2 | [4.2, 5.8] | 4.2 5.8 | Yes | 14.83 |
| 3 | [2.9, 7.1] | 2.9 7.1 | Yes | 9.74 |
| 4 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.01 |
| 5 | [1.8, 8.2] | 1.8 8.2 | Yes | 9.93 |
| 6 | [0.9, 9.1] | 0.9 9.1 | Yes | 9.87 |
| 7 | [3.2, 6.8] | 6.8 3.2 | Yes | 10.83 |
| 8 | [3.4, 6.6] | 3.4 6.6 | Yes | 9.74 |
| 9 | [3.5, 6.5] | 3.5 6.5 | Yes | 14.63 |
| 10 | [0.2, 9.8] | 0.2 9.8 | Yes | 10.34 |
| 11 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.22 |
| 12 | [1.8, 8.2] | 8.2 1.8 | Yes | 9.5 |
| 13 | [2.9, 7.1] | 7.1 2.9 | Yes | 8.69 |
| 14 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.94 |
| 15 | [4.3, 5.7] | 5.7 4.3 | Yes | 10.08 |
| 16 | [4.7, 5.3] | 4.7 5.3 | Yes | 8.58 |
| 17 | [4.9, 5.1] | 5.1 4.9 | Yes | 11.71 |
| 18 | [4.1, 5.9] | 5.9 4.1 | Yes | 11.24 |
| 19 | [3.0, 7.0] | 3.0 7.0 | Yes | 10.14 |
| 20 | [4.7, 5.3] | 5.3 4.7 | Yes | 10.65 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 11XVTE39R39Z | 11XVTE39R39Z | Yes | 4.33 |
| 2 | 9HVO3CWCPTOB | 9HVO3CWCPTOB | Yes | 4.25 |
| 3 | 38NND7RQ48AG | 38NND7RQ48AG | Yes | 4.51 |
| 4 | A8RM7Q70IU7I | A8RM7Q70IU7I | Yes | 3.72 |
| 5 | DNOR1J0A5BLB | DNOR1J0A5BLB | Yes | 5.18 |
| 6 | X2PCNU7QJS1M | X2PCNU7QJS1M | Yes | 3.6 |
| 7 | NCPWGMNQMYL8 | NCPWGMNQMYL3 | No | 2.97 |
| 8 | T2W49EOBXWTL | T2W49EOBXWTL | Yes | 3.82 |
| 9 | 3VD0I2VCLM8H | 3VDOI2VCLM8H | No | 4.86 |
| 10 | DEB4NN6I6KB1 | DEB4NN6I6KB1 | Yes | 3.01 |
| 11 | L20O13ENM04H | L20013ENM04H | No | 4.68 |
| 12 | H9KREXJPE6MG | H9KREXJPE6MG | Yes | 3.52 |
| 13 | RNCCM68P8M1C | RNCCM68P8M1C | Yes | 3.61 |
| 14 | 6YPRMWYUV8WF | GYPRMWYUV8WF | No | 3.78 |
| 15 | B8QFLZSB8X28 | B8QFLZSB8X28 | Yes | 3.46 |
| 16 | 61AUW13UAXJ7 | 61AUW13UAXJ7 | Yes | 4.16 |
| 17 | WEXH5FN2Z9I2 | WEXH5FN2Z9I2 | Yes | 4.9 |
| 18 | 1NW4Q2UWM1XG | 1NW4Q2UWM1XG | Yes | 3.9 |
| 19 | OJO6GPG0JT2L | OJO6GPGQJT2L | No | 4.94 |
| 20 | QMSKUH7NMAJT | QMSKUH7NMAJT | Yes | 4.45 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 243 | 243 | Yes | 3.93 |
| 2 | 19 | 19 | Yes | 4.23 |
| 3 | 39 | 39 | Yes | 3.85 |
| 4 | 16 | 16 | Yes | 5.14 |
| 5 | 36 | 36 | Yes | 4.11 |
| 6 | 63 | 63 | Yes | 3.86 |
| 7 | 64 | 64 | Yes | 7.5 |
| 8 | 48 | 48 | Yes | 3.22 |
| 9 | 65 | 65 | Yes | 4.8 |
| 10 | 73 | 73 | Yes | 5.36 |
| 11 | 4 | 4 | Yes | 3.61 |
| 12 | 198 | 198 | Yes | 5.67 |
| 13 | 3 | 10 | No | 22.08 |
| 14 | 20 | 20 | Yes | 11.83 |
| 15 | 4096 | 16384 | No | 14.16 |
| 16 | 7680 | 7680 | Yes | 5.67 |
| 17 | 1440 | 1440 | Yes | 4.37 |
| 18 | 1 | 1 | Yes | 5.73 |
| 19 | 67 | 67 | Yes | 3.95 |
| 20 | 26 | 26 | Yes | 10.27 |
