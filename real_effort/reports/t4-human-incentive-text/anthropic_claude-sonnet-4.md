# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-27 10:06:06

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 6692 | 39809 | 46501 | 1 | 19 | 25.65 | 512.96 |
| add_numbers | 4080 | 4392 | 8472 | 20 | 0 | 3.51 | 70.28 |
| counting_zeros | 5400 | 26460 | 31860 | 1 | 19 | 13.48 | 269.68 |
| task_decoding | 5400 | 7277 | 12677 | 19 | 1 | 4.84 | 96.8 |
| task_summation | 5460 | 16604 | 22064 | 20 | 0 | 8.68 | 173.59 |
| task_transcription | 4237 | 2733 | 6970 | 20 | 0 | 2.64 | 52.85 |
| task_sequences | 4140 | 8997 | 13137 | 19 | 1 | 6.49 | 129.8 |
| string_entry | 4597 | 4904 | 9501 | 13 | 7 | 4.27 | 85.41 |
| **TOTAL** | **40006** | **111176** | **151182** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 1 5 3 2 1 3 2 3 6 6 2 5 3 |  | No | 24.67 |
| 2 | 3 1 1 5 4 2 3 6 5 1 4 6 1 5 | 3 1 5 4 2 6 5 5 1 4 1 5 | No | 24.17 |
| 3 | 6 2 3 5 3 6 4 2 6 1 5 1 4 6 | Looking at this 6×6 Sudoku puzzle, I need to fill in the empty cells using logical deduction.  Let me work through this systematically by analyzing rows, columns, and 2×3 boxes:  Starting with Row 1: 1 . . \| 3 4 5 - Missing numbers: 2, 6 - Column 2 analysis shows position (1,2) = 6 - Column 3 analysis shows position (1,3) = 2  Row 2: . 5 1 \| 4 6 2 - Missing number: 3 - Position (2,1) = 3  Row 3: 4 2 . \| 6 1 . - Missing numbers: 3, 5 - Column 3 analysis shows position (3,3) = 5 - Position (3,6) = 3  Row 4: . . 3 \| 5 2 1 - Missing numbers: 4, 6 - Column 1 analysis shows position (4,1) = 6 - Position (4,2) = 4  Row 5: . 3 . \| . . 4 - Column 1 analysis shows position (5,1) = 2 - Column 4 analysis shows position (5,4) = 1 - Column 5 analysis shows position (5,5) = 5 - Position (5,3) = 6  Row 6: 5 . . \| 2 3 . - Column 2 analysis shows position (6,2) = 1 | No | 25.44 |
| 4 | 3 6 2 2 2 4 3 3 6 1 2 6 4 5 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers | No | 27.8 |
| 5 | 2 5 4 5 4 1 2 3 5 6 3 6 3 4 |  | No | 27.95 |
| 6 | 4 6 1 6 1 3 6 5 3 6 3 5 2 1 |  | No | 23.82 |
| 7 | 1 4 6 4 2 1 5 1 6 2 2 1 5 6 | 1 6 4 4 2 1 5 1 6 2 2 1 5 | No | 28.76 |
| 8 | 6 5 5 2 4 3 1 3 1 2 4 1 6 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers systematically using the constraints that each row, column, and 2×3 box must contain 1-6 exactly once.  Let me work through the puzzle step by step:  First, I'll identify the easiest cells to fill: - Row 3 is missing only one number (3), which must go in position (3,1) - Row 6 is missing only one number (4), which must go in position (6,3)  After placing these: - The bottom-left 2×3 box now needs only 1, which goes in position (4,1) - Column 1 now needs only 5, which goes in position | No | 27.61 |
| 9 | 6 3 5 2 1 5 4 3 1 2 3 5 3 3 |  | No | 25.99 |
| 10 | 3 4 6 1 4 3 6 5 1 5 6 5 4 3 |  | No | 26.0 |
| 11 | 6 4 3 4 3 1 3 4 5 1 6 4 1 4 |  | No | 24.17 |
| 12 | 3 1 5 6 1 3 6 2 5 5 6 3 5 2 |  | No | 26.31 |
| 13 | 2 1 6 3 2 3 3 5 4 2 4 6 3 4 | 2 5 3 6 1 3 2 5 4 6 3 4 | No | 22.09 |
| 14 | 2 4 6 6 2 4 5 3 3 5 1 5 3 5 | 2 4 6 6 2 5 4 3 3 5 1 4 3 5 | No | 23.51 |
| 15 | 1 6 2 4 1 3 2 1 5 6 4 4 3 6 | Looking at the 6×6 Sudoku puzzle, I'll solve it step by step using row, column, and box constraints.  Let me identify the empty positions and work through the constraints:  Starting with easier deductions: - Row 1: 4 _ 3 6 2 5 → missing 1, so position (1,2) = 1 - Column 1: 4 5 _ 1 2 6 → missing 3, so position (3,1) = 3   - Column 5: 2 3 6 _ 1 5 → missing 4, so position (4,5) = 4 - Row 4: 1 5 _ 2 4 3 → missing 6, so position (4,3) = 6  Current state: ``` 4 1 3 \| 6 2 5 5 _ _ \| _ 3 _ -----+----- 3 _ _ \| _ 6 4 1 5 6 \| 2 4 3 -----+----- 2 _ 5 \| _ 1 _ 6 3 4 \| 1 5 2 ```  Continuing with box and column constraints: - Column 3: 3 _ _ 6 5 4 → missing 1,2 for positions (2,3) and (3,3) - Top-left box needs 2,6 in positions (2,2) and (2,3) - Since (2,3) must be 1 or 2 (column) | No | 27.96 |
| 16 | 6 2 1 5 2 5 6 2 2 4 3 1 2 6 |  | No | 26.14 |
| 17 | 5 6 1 5 4 6 2 5 2 1 3 6 1 4 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step using the constraints that each row, column, and 2×3 box must contain numbers 1-6.  Let me work through the missing positions systematically:  Starting with Row 1: `2 . 3 \| . 4 1` - Missing | No | 25.94 |
| 18 | 3 6 1 2 3 3 3 6 1 6 4 6 5 1 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through this step by step:  ``` . 4 1 \| . 5 2 5 . . \| 4 6 . -----+----- 6 2 5 \| . 1 4 2 5 4 \| 1 . . -----+----- . 3 . \| 2 . 5 4 . 3 \| . 2 . ```  Starting with easier deductions:  Row 3, Col 4: Row 3 needs only 3, so this must be 3.  Row 4, Col 5: Looking at column 5, it has [5, 6, 1, ., ., 2]. Missing 3, 4. Row 4 needs 3, 6. The middle-right box needs various numbers. This must be 3.  Row 4, Col 6: Row 4 now needs only 6, so this is 6.  Working through the remaining cells systematically:  Row 1, Col 1: Column 1 needs 1, 3. Row 1 needs 3, 6. Top-left box constraints make this 3.  Row 1, Col 4: Row 1 now needs 6, and this position can hold 6, so this is 6.  Row 2, Col 2: Column 2 needs 1, 6. Row 2 needs 1, 2, 3. This must be 1.  Row 2, Col 3: Row 2 needs 2, 3. Column 3 needs 2, 6. This must be 2.  Row 2, Col 6: Row 2 needs only 3, so | No | 26.64 |
| 19 | 5 3 6 1 6 2 3 2 2 5 3 3 6 4 | 5 3 6 1 6 2 3 2 2 5 3 3 6 4 | Yes | 22.89 |
| 20 | 3 6 5 4 3 4 3 2 6 2 6 1 4 6 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the constraints:  From column 4 (positions with values _, 6, 1, 4, 3, 2): missing 5 So position (0,4) = 5  From row 2 (4, 5, _, 1, 6, 2): missing 3 So position (1,2) = 3  From column 3 (2, 1, 5, _, 4, 3): missing 6 So position (3,3) = 6  From row 4 (1, 3, _, 6, 4, 5): missing 2 So position (3,2) = 2  From row 3 (6, 2, _, 5, 1, _): missing 3, 4 From column 2 (1, 5, 2, 3, _, _): missing 4, 6 So position (2,2) = 4 (can't be 3 since column 2 needs 4 and 6)  From column 6 constraints and row 3: position (2,5) = 3  From column 1 (_, 4, 6, 1, _, 5): missing 2, 3 From top-left 2×3 box constraints: position (0,0) = 3  From row 1 (3, 1, _, 2, 5, _): missing 4, 6 From top-right 2×3 box: position (0,2) = 6, position (0,5) = 4  From column 1: position (4,0) = 2  From column 2 (1, 5, 2, 3, _, _): missing 4, 6 From bottom-left 2×3 box: position (4,1) = 1, position (5,1) = 4  From | No | 25.09 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1688 | 1688 | Yes | 4.04 |
| 2 | 1584 | 1584 | Yes | 4.04 |
| 3 | 1693 | 1693 | Yes | 2.9 |
| 4 | 2261 | 2261 | Yes | 2.57 |
| 5 | 1555 | 1555 | Yes | 3.93 |
| 6 | 2054 | 2054 | Yes | 3.14 |
| 7 | 1827 | 1827 | Yes | 5.14 |
| 8 | 1678 | 1678 | Yes | 2.63 |
| 9 | 1295 | 1295 | Yes | 2.99 |
| 10 | 1283 | 1283 | Yes | 2.48 |
| 11 | 1209 | 1209 | Yes | 4.12 |
| 12 | 2099 | 2099 | Yes | 2.89 |
| 13 | 2281 | 2281 | Yes | 5.88 |
| 14 | 1866 | 1866 | Yes | 3.31 |
| 15 | 2044 | 2044 | Yes | 4.07 |
| 16 | 1505 | 1505 | Yes | 3.02 |
| 17 | 1760 | 1760 | Yes | 4.51 |
| 18 | 1217 | 1217 | Yes | 3.72 |
| 19 | 611 | 611 | Yes | 2.3 |
| 20 | 1500 | 1500 | Yes | 2.6 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 51 | No | 13.75 |
| 2 | 52 | 53 | No | 13.76 |
| 3 | 36 | 27 | No | 10.68 |
| 4 | 54 | 45 | No | 11.33 |
| 5 | 50 | 50 | Yes | 17.45 |
| 6 | 71 | 70 | No | 9.76 |
| 7 | 68 | 64 | No | 12.82 |
| 8 | 41 | 33 | No | 12.23 |
| 9 | 52 | 44 | No | 7.88 |
| 10 | 75 | 73 | No | 14.12 |
| 11 | 46 | 39 | No | 13.49 |
| 12 | 49 | 44 | No | 15.44 |
| 13 | 42 | 35 | No | 11.72 |
| 14 | 42 | 39 | No | 13.6 |
| 15 | 68 | 63 | No | 15.92 |
| 16 | 46 | 40 | No | 16.71 |
| 17 | 51 | 50 | No | 16.66 |
| 18 | 44 | 45 | No | 13.23 |
| 19 | 64 | 63 | No | 14.39 |
| 20 | 68 | 65 | No | 14.71 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZDGHNKF | ZDGHNKF | Yes | 5.45 |
| 2 | LBJYCSM | LBJYCSM | Yes | 4.48 |
| 3 | EBOTAKZ | EBOTAKZ | Yes | 4.31 |
| 4 | KLYIHUB | KLYIHUB | Yes | 5.24 |
| 5 | MNIOWTU | MNIOWTU | Yes | 8.9 |
| 6 | KFIWRTN | KFIWRTN | Yes | 4.06 |
| 7 | QTXWLVP | QTXWLVP | Yes | 3.75 |
| 8 | KNRPIJA | KNRPIJA | Yes | 4.09 |
| 9 | NGAOXWT | NGAOXWT | Yes | 5.42 |
| 10 | SXNKACI | SXNKACI | Yes | 4.43 |
| 11 | KICAQGS | KICAQGS | Yes | 4.65 |
| 12 | URJDYVS | URJDYVS | Yes | 3.95 |
| 13 | XPUDKTR | XPUDKTR | Yes | 4.69 |
| 14 | KMOFADC | KMOFADC | Yes | 4.73 |
| 15 | DMSXEKR | DMSXEKR | Yes | 4.93 |
| 16 | NLKMZEQ | NLKMZEQ | Yes | 5.72 |
| 17 | DTXQWLH | DTXQWLH | Yes | 4.99 |
| 18 | VWQFEKN | VWQFEKN | Yes | 4.14 |
| 19 | PJEIGKX | PJEIGKX | Yes | 3.96 |
| 20 | FTURGZQ | FTURZGQ | No | 4.9 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.98 |
| 2 | [2.0, 8.0] | 8.0 2.0 | Yes | 7.59 |
| 3 | [3.4, 6.6] | 3.4 6.6 | Yes | 8.36 |
| 4 | [2.4, 7.6] | 7.6 2.4 | Yes | 6.95 |
| 5 | [1.6, 8.4] | 1.6 8.4 | Yes | 9.3 |
| 6 | [2.1, 7.9] | 2.1 7.9 | Yes | 9.64 |
| 7 | [1.5, 8.5] | 8.5 1.5 | Yes | 9.87 |
| 8 | [2.6, 7.4] | 2.6 7.4 | Yes | 9.4 |
| 9 | [2.4, 7.6] | 7.6 2.4 | Yes | 10.38 |
| 10 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.69 |
| 11 | [2.3, 7.7] | 7.7 2.3 | Yes | 7.64 |
| 12 | [2.2, 7.8] | 7.8 2.2 | Yes | 8.32 |
| 13 | [3.3, 6.7] | 3.3 6.7 | Yes | 8.41 |
| 14 | [3.0, 7.0] | 7.0 3.0 | Yes | 6.27 |
| 15 | [2.6, 7.4] | 7.4 2.6 | Yes | 8.76 |
| 16 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.85 |
| 17 | [3.7, 6.3] | 6.3 3.7 | Yes | 7.46 |
| 18 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.46 |
| 19 | [1.2, 8.8] | 1.2 8.8 | Yes | 12.58 |
| 20 | [2.2, 7.8] | 2.2 7.8 | Yes | 8.68 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HCMYK2YZM667 | HCMYK2YZM667 | Yes | 1.77 |
| 2 | MEO48Q41YZC1 | MEO48Q41YZC1 | Yes | 2.5 |
| 3 | 1CEI41VEP3EA | 1CEI41VEP3EA | Yes | 2.62 |
| 4 | 1M5BQB2S3960 | 1M5BQB2S3960 | Yes | 2.94 |
| 5 | 35D5U6UMPRTG | 35D5U6UMPRTG | Yes | 2.78 |
| 6 | ELWESDLU9SFT | ELWESDLU9SFT | Yes | 2.58 |
| 7 | WXTFXY5RSY1M | WXTFXY5RSY1M | Yes | 2.63 |
| 8 | 2K37IITO40T2 | 2K37IITO40T2 | Yes | 3.07 |
| 9 | Z4AOLYBRST35 | Z4AOLYBRST35 | Yes | 1.72 |
| 10 | W1G83YXFDKE3 | W1G83YXFDKE3 | Yes | 3.02 |
| 11 | VBRVDZ37I2HN | VBRVDZ37I2HN | Yes | 3.06 |
| 12 | OTQ42ZWALUDH | OTQ42ZWALUDH | Yes | 2.94 |
| 13 | DF3ENFM5UHXT | DF3ENFM5UHXT | Yes | 2.14 |
| 14 | XJUXL9S8JR8H | XJUXL9S8JR8H | Yes | 1.86 |
| 15 | UY1KC5T11IJF | UY1KC5T11IJF | Yes | 2.51 |
| 16 | YQOH7R71SGAN | YQOH7R71SGAN | Yes | 2.8 |
| 17 | C9BPSH45W26F | C9BPSH45W26F | Yes | 3.09 |
| 18 | ZMLXQBSY4E9C | ZMLXQBSY4E9C | Yes | 2.87 |
| 19 | G9CY6AHMANXM | G9CY6AHMANXM | Yes | 2.99 |
| 20 | UTW9O9DH7XPZ | UTW9O9DH7XPZ | Yes | 2.94 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 3.68 |
| 2 | 1 | 1 | Yes | 6.82 |
| 3 | 793 | 793 | Yes | 2.93 |
| 4 | 60 | 60 | Yes | 4.59 |
| 5 | 10 | 9 | No | 6.51 |
| 6 | 19 | 19 | Yes | 4.94 |
| 7 | 48 | 48 | Yes | 3.89 |
| 8 | 3 | 3 | Yes | 5.78 |
| 9 | 60 | 60 | Yes | 5.4 |
| 10 | 20 | 20 | Yes | 18.61 |
| 11 | 65 | 65 | Yes | 5.21 |
| 12 | 28 | 28 | Yes | 5.02 |
| 13 | 7 | 7 | Yes | 4.11 |
| 14 | 67 | 67 | Yes | 3.84 |
| 15 | 26 | 26 | Yes | 9.23 |
| 16 | 44 | 44 | Yes | 10.19 |
| 17 | 64 | 64 | Yes | 11.09 |
| 18 | 4 | 4 | Yes | 3.81 |
| 19 | 39 | 39 | Yes | 5.15 |
| 20 | 4 | 4 | Yes | 8.98 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )<(_< /() | )<(_< /() | Yes | 3.25 |
| 2 | _</ (\/\< | _</ (\/\ | No | 3.53 |
| 3 | / )))  /) | / ))))  /) | No | 3.82 |
| 4 | <_ \ (\</ | <_ \ (\</ | Yes | 3.65 |
| 5 | </_<<<_</ | </_<<<_</ | Yes | 4.84 |
| 6 | <)_(  (_< | <)_(  (_ | No | 4.92 |
| 7 | )_(\ )<(( | )_(\ )<(( | Yes | 3.55 |
| 8 |  \)_ <()/ | \)_ <()/ | No | 4.26 |
| 9 | )_<(_///  | )_<(_/// | No | 3.59 |
| 10 | _(_)\( /( | _(_)\( /( | Yes | 3.14 |
| 11 | /_/\)< /\ | /_/\)< /\ | Yes | 2.95 |
| 12 | __(____(_ | __(____(_ | Yes | 2.61 |
| 13 | \__/)<))_ | \__/)<))_ | Yes | 4.0 |
| 14 | /\\/)(\\< | /\\/)(\\ | No | 3.63 |
| 15 | \_) /)\_/ | \_) /)\_/ | Yes | 2.43 |
| 16 |  (() <<(< | (()) <<( | No | 18.61 |
| 17 | _/)_ _(_\ | _/)_ _(_\ | Yes | 3.95 |
| 18 | << (__//_ | << (__//_ | Yes | 2.25 |
| 19 | /  /\((// | /  /\((// | Yes | 2.7 |
| 20 | )( /<)((/ | )( /<)((/ | Yes | 3.74 |
