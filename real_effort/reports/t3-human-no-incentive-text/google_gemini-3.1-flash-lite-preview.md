# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-27 09:59:31

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
| sudoku_game | 5362 | 35776 | 41138 | 2 | 18 | 8.84 | 176.78 |
| add_numbers | 3198 | 4606 | 7804 | 20 | 0 | 3.73 | 74.56 |
| counting_zeros | 6254 | 36171 | 42425 | 15 | 5 | 11.83 | 236.66 |
| task_decoding | 4478 | 13727 | 18205 | 20 | 0 | 5.90 | 117.97 |
| task_summation | 4528 | 14797 | 19325 | 20 | 0 | 5.84 | 116.83 |
| task_transcription | 3198 | 5829 | 9027 | 20 | 0 | 4.99 | 99.81 |
| task_sequences | 3184 | 7896 | 11080 | 20 | 0 | 3.89 | 77.82 |
| string_entry | 3498 | 18044 | 21542 | 7 | 13 | 5.48 | 109.67 |
| **TOTAL** | **33700** | **136846** | **170546** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 6 5 6 3 4 6 4 5 4 1 5 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Puzzle Analysis:** 1.  **Row 1:** 1 4 2 \| 5 6 3 (Complete) 2.  **Row 2:** R2C1, 5, 3 \| 6, R2C5, 4. Missing: 1, 2. Col 1 already has 1, so R2C1=2. Col 5 already has 6, 2, 3, so R2C5=1. (Row 2: 2 5 3 \| 6 1 4) 3.  **Row 3:** 3, R3C2, 1 \| 4, 2, 5. Missing: 6. R3C2=6. (Row 3: 3 6 1 \| 4 2 5) 4.  **Col 2:** 4, 5, 6, 2, 3, R6C2. Missing: 1. R6C2=1. 5.  **Col 4:** 5, 6, 4, R4C4, 1, R6C4. Missing: 2, 3. Box 4 (Rows 3-4, Cols 4-6) needs 3 and 6. R4C4 must be 3, R6C4 must be 2. 6.  **Box 4 (Rows 3 | No | 9.7 |
| 2 | 1 2 1 3 6 2 3 4 1 2 3 6 2 1 | 1 6 1 2 2 1 2 3 1 2 1 | No | 6.18 |
| 3 | 3 5 5 3 3 6 1 4 1 3 1 3 5 4 | 3 5 5 3 3 1 3 1 1 4 4 3 | No | 8.4 |
| 4 | 4 1 3 6 2 6 3 1 4 4 2 4 3 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules (each row, column, and 2×3 box must contain the numbers 1-6 exactly once).  **Initial Grid:** ``` . 5 . \| 2 6 . 3 1 4 \| . 5 . -----+----- . 2 | No | 10.77 |
| 5 | 1 4 3 2 6 5 4 2 5 2 2 6 3 5 | 1 4 3 2 6 5 4 2 5 2 6 3 5 | No | 8.08 |
| 6 | 3 3 6 5 1 5 4 5 2 6 6 2 4 5 | To solve the 6×6 Sudoku puzzle, we fill in the grid row by row, ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Given grid: 4 5 1 \| 2 3 6 2 1 . \| 6 4 5 . . . \| 4 1 2 . 3 6 \| . 2 . . 4 . \| 1 . 3 . . . \| 3 . 1  1.  **Row 2:** The missing number in `2 1 . \| 6 4 5` is 3. So, R2C3 = 3. 2.  **Row 3:** The missing numbers are 3, 5, 6. Since R3C4, R3C5, R3C6 are 4, 1, 2, we look at the columns. R3C3 must be 5 (as 1, 3, 6 are in column 3). R3C2 must be 6 (as 5, 1, 3, 4 are in column 2). R3C1 must be 3. Row 3 is: 3 6 5 \| 4 1 2. 3.  **Row 4:** The missing numbers are 1, 4, 5. R4C4 must be 5 (column 4). R4C6 must be 4 (column 6). R4C1 must be 1. Row 4 is: 1 3 6 \| 5 2 4. 4.  **Row 5:** The missing numbers are 2, 5, 6. R5C3 must be 2 (column 3). R5C1 must be 6 (column 1). R5C5 must be 5 (column 5). Row 5 is: 6 4 2 \| 1 5 3. 5.  **Row 6:** The missing numbers are 2, 4, 5, 6. R6C1 must be 5 (column 1). R6C3 must be 4 (column 3). R6C2 must be 2 (column 2). R6C5 must be 6 | No | 6.74 |
| 7 | 3 4 2 1 1 3 2 6 3 5 1 4 4 5 | 1 4 2 3 3 1 2 6 3 5 1 4 4 5 | No | 7.0 |
| 8 | 1 2 2 3 5 4 1 5 6 5 6 2 3 5 | 1 2 2 3 5 4 1 5 6 5 6 2 3 5 | Yes | 7.11 |
| 9 | 5 3 4 2 6 1 4 6 4 3 5 5 2 3 | 5 3 4 2 6 1 4 6 4 3 5 5 2 3 | Yes | 8.47 |
| 10 | 6 1 3 1 1 2 3 5 4 3 2 3 1 4 | 6 1 3 1 2 3 1 5 3 4 1 3 4 2 | No | 7.67 |
| 11 | 4 5 3 3 6 4 2 3 1 2 3 4 1 3 | 3 4 5 4 6 3 2 3 1 2 3 4 1 3 | No | 7.33 |
| 12 | 4 1 3 4 5 6 5 6 4 2 2 3 2 5 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules (each row, column, and 2×3 box must contain 1-6 exactly once):  **Initial Grid:** 5 2 6 \| 1 3 4 . 6 3 \| 2 . 5 -----+----- . 1 . \| . 2 . 1 3 . \| . . . -----+----- . 5 1 \| 4 6 . 6 4 . \| 3 . 1  **Step-by-step Deduction:** 1.  **Row 2:** Missing 1, 4. Column 1 has 5, 1, 6, so R2C1 must be 4. Column 5 has 3, 2, 6, so R2C5 must be 1. (Row 2: 4 6 3 2 1 5) 2.  **Column 1:** Missing 2, 3. R3C1 and R5C1. Column 1 already has 5, 4, 1, 6. R5C1 must be 2 (since row 5 has 5, 1, 4, 6), so R3C1 must be 3. 3.  **Row 3:** Missing 4, 5, 6. R3C3, R3C4, R3C6. Column 3 has 6, 3, 1, so R3C3 is 5 (by elimination). Column 4 has 1, 2, 4, 3, so R3C4 is 6. Column 6 has 4, 5, 1, so R3C6 is 2. (Row 3: 3 1 5 6 2 4) 4.  **Row 4:** Missing 2, 4, 5, 6. R4C3, R4C4, R4C5, R4C6. Column 3 has 6, 3, 5, 1, so R4C3 is 2 or 4. By checking columns and boxes, we determine the remaining values. 5.  **Completing the grid:**     Row 1: 5 2 6 \| 1 3 4     Row 2: 4 6 3 \| 2 1 5     Row 3: 3 1 5 \| 6 2 4     Row 4: 1 3 | No | 9.61 |
| 13 | 2 1 3 3 6 1 1 4 1 5 2 6 4 1 | 3 1 1 2 6 2 4 1 1 2 5 4 1 4 | No | 6.63 |
| 14 | 6 3 2 5 4 3 1 2 4 6 1 5 5 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules (each row, column, and 2×3 box must contain the numbers 1-6 exactly once).  **Puzzle:** ``` 5 2 4 \| 6 3 1 . . 1 \| . . . -----+----- 1 4 5 \| . 6 2 3 . . \| 5 4 6 -----+----- . . 3 \| . 2 . 2 . 6 \| 4 . 3 ```  **Step-by-step logic:** 1.  **Row 3:** The missing number in R3 is 3 (1, 4, 5, _, 6, 2). So, R3C4 = 3. 2.  **Row 4:** The missing numbers are 1 and 2. Since C2 already has a 2 (in R1), R4C2 = 1 and R4C3 = 2. 3.  **Row 6:** The missing numbers are 1 and 5. Since C2 already has a 1 (in R4), R6C2 = 5 and R6C5 = 1. 4.  **Box 5 (R5-R6, C1-C3):** Missing numbers are 1 and 4. Since C1 already has 5, 1, 3, 2, R5C1 must be 4. Thus, R5C2 = 1. 5.  **Box 6 (R5-R6, C4-C6):** Missing numbers are 5 and 6. In R5, we have 4, 1, 3, 2, so R5C4 and R5C6 must be 5 and 6. Since C4 has 6, 3, 5, 4, R5C4 must be 6. Thus, R5C6 = 5. 6.  **Row 2:** The missing numbers are 2, 3, 4, 5, 6. Filling in the remaining constraints: R2C1=6, R2C2=3, R2C4=2, R2C5=5, R2C6=4.  **Completed Grid:** ``` 5 2 4 \| 6 3 1 6 3 1 \| 2 5 4 -----+----- 1 4 5 \| 3 6 2 3 1 2 \| 5 4 6 -----+----- 4 1 3 \| 6 2 5 2 5 6 \| 4 1 3 ``` | No | 9.69 |
| 15 | 2 4 4 4 5 1 6 4 3 6 1 3 4 6 | 2 4 4 1 5 4 6 6 3 4 4 3 1 6 | No | 8.85 |
| 16 | 4 2 6 3 4 6 2 4 5 2 5 6 3 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Puzzle Analysis:** Initial grid: . . 1 \| 5 . 3 . 5 6 \| . 1 2 -----+----- . 1 . \| 3 5 . 1 3 4 \| 6 2 . -----+----- . 4 . \| 1 3 . 5 6 . \| . 4 1  **Step-by-step resolution:** 1.  **R4C6:** R4 contains 1, 3, 4, 6, 2. The missing number is 5. 2.  **R6C3, R6C4:** R6 contains 5, 6, 4, 1. Missing are 2, 3. Column 3 has 1, 6, 4, so R6C3 must be 2 or 3. Column 4 has 5, 3, 6, 1. R6C4 must be 2. Thus, R6C3 is 3. 3.  **R5C6:** Column 6 has 3, 2, 5, 1. Missing are 4, 6. R5 has 4, 1, 3. R5C6 must be 6. 4.  **R5C1, R5C3:** R5 has 4, 1, 3, 6. Missing are 2, 5. Column 1 has 1, 5. R5C1 must be 2, R5C3 is 5. 5.  **R3C1, R3C3, R3C6:** R3 has 1, 3, 5. Missing are 2, 4, 6. Column 1 has 1, 5, 2. R3C1 must be 4 or 6. Through deduction, R3C6 is 4, R3C3 is 2, R3C1 is 6. 6.  **R2C1, R2C4:** R2 has 5, 6, 1, 2. Missing are 3, 4. Column 4 has 5, 3, 6, 1, 2. R2C4 is 4, R2C1 is 3. 7.  **R1C1, R1C2, R1C5:** R1 has 1, 5, 3. Missing are 2, 4, 6. Filling in the remaining constraints, R1C1 is 2, R1C2 is 4, R1C5 is 6. 8.  **R6C4:** R6C4 is 2.  **Completed Grid:** 2 4 1 \| 5 6 3 3 5 6 \| 4 1 2 6 1 2 \| 3 5 4 1 3 4 \| 6 2 5 2 4 5 \| 1 3 6 5 6 3 \| 2 4 1  **Missing numbers in reading order:** 2 4 6 3 4 6 2 4 | No | 8.8 |
| 17 | 3 4 4 3 2 6 6 1 5 2 3 2 4 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Puzzle:** 2 . 6 \| 1 5 . . 5 . \| . . 1 -----+----- 1 . 4 \| 5 2 3 6 . . \| 4 3 . -----+----- . . 1 \| 6 4 5 5 . 2 \| . 1 6  **Step-by-step solution:** 1.  **Row 3:** The missing number is 6. Row 3 becomes: 1 6 4 \| 5 2 3. 2.  **Row 1:** The missing numbers are 3 and 4. Column 6 already has 1, 3, 5, 6. Thus, R1C6 must be 4, and R1C2 must be 3. Row 1 becomes: 2 3 6 \| 1 5 4. 3.  **Row 2:** Missing numbers are 2, 3, 4, 6. By checking columns and boxes, we find R2C3 is 3, R2C1 is 4, R2C5 is 6, and R2C4 is 2. Row 2 becomes: 4 5 3 \| 2 6 1. 4.  **Row 4:** Missing numbers are 1, 2, 5. Checking columns, R4C3 is 5, R4 | No | 9.0 |
| 18 | 6 3 4 6 2 3 4 5 2 5 6 6 4 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Puzzle Analysis:** 1.  **Row 2:** Missing number is 6 (R2C6 = 6). 2.  **Column 5:** Missing number is 3 (R1C5 = 3). 3.  **Row 1:** Missing numbers are 4 and 6. Given Column 6 already has 6, 1, 3, 2, R1C6 must be 4, and R1C2 must be 6. 4.  **Row 6:** Missing numbers are 3 and 4. Given Column 3 already has 2, 1, 6, 4, R6C3 must be 3, and R6C2 must be 4. 5.  **Row 5:** Missing number is 6 (R5C1 = 6). 6.  **Row 4:** Missing numbers are 2, 5, and 6. Based on column constraints, R4C2 = 2, R4C4 = 6, and R4C3 = 5. 7.  **Row 3:** Missing numbers are 2, 3, 4, and 5. Based on column constraints, R3C1 = 2, R3C2 = 3, R3C4 = 4, and R3C6 = 5.  **Completed Grid:** 1 6 2 \| 5 3 4 4 5 1 \| 3 2 6 -----+----- 2 3 6 \| 4 1 5 3 2 5 \| 6 4 1 -----+----- 6 1 4 \| 2 5 3 5 4 3 \| 1 6 2  **Missing numbers in reading order:** R1C2: 6, R1C5: 3, R1C6: 4 R2C6: 6 R3C1: 2, R3C2: 3, R3C4: 4, R3C6: | No | 9.7 |
| 19 | 3 1 2 4 3 2 3 3 5 6 3 6 5 4 | 3 1 2 4 3 2 3 5 | No | 19.19 |
| 20 | 5 4 1 2 6 1 4 2 3 1 6 5 5 1 | 4 5 1 2 6 1 3 2 4 5 6 1 5 1 | No | 7.83 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1909 | 1909 | Yes | 2.27 |
| 2 | 1305 | 1305 | Yes | 5.23 |
| 3 | 865 | 865 | Yes | 2.1 |
| 4 | 1791 | 1791 | Yes | 1.91 |
| 5 | 1668 | 1668 | Yes | 2.57 |
| 6 | 1673 | 1673 | Yes | 1.81 |
| 7 | 714 | 714 | Yes | 1.99 |
| 8 | 1046 | 1046 | Yes | 2.09 |
| 9 | 2317 | 2317 | Yes | 3.0 |
| 10 | 1468 | 1468 | Yes | 6.24 |
| 11 | 1793 | 1793 | Yes | 2.92 |
| 12 | 1683 | 1683 | Yes | 5.3 |
| 13 | 2334 | 2334 | Yes | 2.56 |
| 14 | 1418 | 1418 | Yes | 8.66 |
| 15 | 1529 | 1529 | Yes | 2.69 |
| 16 | 1568 | 1568 | Yes | 2.6 |
| 17 | 2382 | 2382 | Yes | 3.63 |
| 18 | 1918 | 1918 | Yes | 2.43 |
| 19 | 599 | 599 | Yes | 12.3 |
| 20 | 2041 | 2041 | Yes | 2.26 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 65 | Yes | 7.34 |
| 2 | 36 | 36 | Yes | 7.62 |
| 3 | 65 | 65 | Yes | 8.07 |
| 4 | 66 | 66 | Yes | 4.92 |
| 5 | 61 | 61 | Yes | 9.26 |
| 6 | 70 | 66 | No | 6.86 |
| 7 | 68 | 68 | Yes | 8.88 |
| 8 | 50 | 50 | Yes | 9.16 |
| 9 | 72 | 65 | No | 8.44 |
| 10 | 51 | 51 | Yes | 19.02 |
| 11 | 51 | 51 | Yes | 6.7 |
| 12 | 64 | 64 | Yes | 7.93 |
| 13 | 59 | 59 | Yes | 8.82 |
| 14 | 67 | 67 | Yes | 8.54 |
| 15 | 67 | 67 | Yes | 8.9 |
| 16 | 41 | 41 | Yes | 7.0 |
| 17 | 60 | 61 | No | 65.17 |
| 18 | 48 | 48 | Yes | 10.21 |
| 19 | 40 | 36 | No | 17.59 |
| 20 | 43 | 42 | No | 6.2 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XRWCBPG | XRWCBPG | Yes | 12.76 |
| 2 | YWMCFIT | YWMCFIT | Yes | 5.15 |
| 3 | WXRPOLG | WXRPOLG | Yes | 2.21 |
| 4 | JAHOTGE | JAHOTGE | Yes | 2.34 |
| 5 | BWJZULC | BWJZULC | Yes | 3.42 |
| 6 | PNTASYR | PNTASYR | Yes | 6.73 |
| 7 | POYCSTD | POYCSTD | Yes | 9.64 |
| 8 | UPHSNDY | UPHSNDY | Yes | 3.87 |
| 9 | PSJLUEM | PSJLUEM | Yes | 5.27 |
| 10 | VQRDAKM | VQRDAKM | Yes | 2.41 |
| 11 | XFICLTY | XFICLTY | Yes | 3.17 |
| 12 | SEXZLOF | SEXZLOF | Yes | 2.45 |
| 13 | WCNSIUH | WCNSIUH | Yes | 4.83 |
| 14 | PUTVFXL | PUTVFXL | Yes | 7.35 |
| 15 | QYCNFOR | QYCNFOR | Yes | 9.32 |
| 16 | AKBUIZM | AKBUIZM | Yes | 3.06 |
| 17 | GHLSATC | GHLSATC | Yes | 13.46 |
| 18 | ZSCUXIY | ZSCUXIY | Yes | 7.76 |
| 19 | TMVCNXK | TMVCNXK | Yes | 1.5 |
| 20 | ZIJCWGB | ZIJCWGB | Yes | 11.27 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 1.5 8.5 | Yes | 4.15 |
| 2 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.78 |
| 3 | [2.8, 7.2] | 2.8 7.2 | Yes | 4.25 |
| 4 | [0.2, 9.8] | 9.8 0.2 | Yes | 3.88 |
| 5 | [4.1, 5.9] | 4.1 5.9 | Yes | 4.27 |
| 6 | [0.2, 9.8] | 9.8 0.2 | Yes | 4.1 |
| 7 | [0.3, 9.7] | 9.7 0.3 | Yes | 4.02 |
| 8 | [2.2, 7.8] | 7.8 2.2 | Yes | 4.34 |
| 9 | [0.5, 9.5] | 0.5 9.5 | Yes | 8.61 |
| 10 | [3.1, 6.9] | 6.9 3.1 | Yes | 4.36 |
| 11 | [4.8, 5.2] | 4.8 5.2 | Yes | 4.17 |
| 12 | [4.6, 5.4] | 5.4 4.6 | Yes | 4.81 |
| 13 | [2.1, 7.9] | 7.9 2.1 | Yes | 2.78 |
| 14 | [2.1, 7.9] | 2.1 7.9 | Yes | 13.89 |
| 15 | [4.6, 5.4] | 5.4 4.6 | Yes | 5.37 |
| 16 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.07 |
| 17 | [0.7, 9.3] | 9.3 0.7 | Yes | 4.25 |
| 18 | [1.2, 8.8] | 8.8 1.2 | Yes | 14.39 |
| 19 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.74 |
| 20 | [2.0, 8.0] | 8.0 2.0 | Yes | 2.6 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9QS3YCV1I87A | 9QS3YCV1I87A | Yes | 8.85 |
| 2 | 8N9H6X0QQ0BN | 8N9H6X0QQ0BN | Yes | 1.97 |
| 3 | OR7AEBVQDYCH | OR7AEBVQDYCH | Yes | 1.92 |
| 4 | G50CTAOIHQ9B | G50CTAOIHQ9B | Yes | 2.79 |
| 5 | Z0QDIQ9QQ87O | Z0QDIQ9QQ87O | Yes | 1.69 |
| 6 | HY9MNZ77PF7X | HY9MNZ77PF7X | Yes | 4.53 |
| 7 | MLHB4TCYLFB0 | MLHB4TCYLFB0 | Yes | 7.64 |
| 8 | D61XI5I40L9B | D61XI5I40L9B | Yes | 7.4 |
| 9 | 1A8061ARPI5M | 1A8061ARPI5M | Yes | 16.57 |
| 10 | TB8TNIKSVQPE | TB8TNIKSVQPE | Yes | 2.07 |
| 11 | LBTV60TGMZPJ | LBTV60TGMZPJ | Yes | 2.47 |
| 12 | C2M1PR4OOLX1 | C2M1PR4OOLX1 | Yes | 4.01 |
| 13 | BU1YORH8PYNX | BU1YORH8PYNX | Yes | 3.71 |
| 14 | FNCQKX58XH1U | FNCQKX58XH1U | Yes | 8.36 |
| 15 | 40K2M0L9QIJP | 40K2M0L9QIJP | Yes | 1.85 |
| 16 | 8GCYWAWQ1XAA | 8GCYWAWQ1XAA | Yes | 7.97 |
| 17 | TWLNC2ZBB563 | TWLNC2ZBB563 | Yes | 2.54 |
| 18 | 4ATZ46H6YJMN | 4ATZ46H6YJMN | Yes | 1.62 |
| 19 | 9XVZ5NLAFLAP | 9XVZ5NLAFLAP | Yes | 10.0 |
| 20 | JRQDJPC24592 | JRQDJPC24592 | Yes | 1.82 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 26 | 26 | Yes | 4.47 |
| 2 | 73 | 73 | Yes | 9.05 |
| 3 | 44 | 44 | Yes | 2.14 |
| 4 | 60 | 60 | Yes | 2.32 |
| 5 | 4096 | 4096 | Yes | 8.97 |
| 6 | 5 | 5 | Yes | 2.69 |
| 7 | 31 | 31 | Yes | 2.07 |
| 8 | 3 | 3 | Yes | 3.28 |
| 9 | 67 | 67 | Yes | 2.36 |
| 10 | 198 | 198 | Yes | 2.65 |
| 11 | 48 | 48 | Yes | 2.04 |
| 12 | 1 | 1 | Yes | 4.83 |
| 13 | 6 | 6 | Yes | 2.77 |
| 14 | 39 | 39 | Yes | 8.5 |
| 15 | 64 | 64 | Yes | 7.29 |
| 16 | 3 | 3 | Yes | 1.57 |
| 17 | 28 | 28 | Yes | 2.18 |
| 18 | 793 | 793 | Yes | 2.11 |
| 19 | 60 | 60 | Yes | 4.13 |
| 20 | 9 | 9 | Yes | 2.38 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  _/)/__ _ | _/)/__ _ | No | 4.67 |
| 2 | \/)_<// < | \/)_<// < | Yes | 2.98 |
| 3 | _\_\  ))< | _\_  ))< | No | 3.64 |
| 4 | <\ <<__/) | < <<__/) | No | 6.82 |
| 5 | ((<)\ ___ | ((<) ___ | No | 4.24 |
| 6 | \)(/))__/ | \)(/))_ | No | 4.44 |
| 7 |  )_\/()(  | )_\/()( | No | 5.2 |
| 8 | )<\\_/\<  | )<\\_/\< | No | 6.35 |
| 9 | ( /)/( (\ | ( /)/ / | No | 7.16 |
| 10 |  <()__)\  | <()__)\ | No | 5.33 |
| 11 | )\<</ )(_ | )\<</ )(_ | Yes | 5.13 |
| 12 | \(_)/(_\  | \(_)/(_ | No | 2.69 |
| 13 | \_/<( < ( | \_/<( < ( | Yes | 2.96 |
| 14 | \  )\)(/) | )\)(/) | No | 4.65 |
| 15 |  ////\)<_ | ////\)<_ | No | 5.43 |
| 16 | /__\) __/ | /__\) __/ | Yes | 6.18 |
| 17 | /<(<\///) | /<(<\///) | Yes | 3.82 |
| 18 | //(<\(\\_ | //(<\(\\_ | Yes | 5.6 |
| 19 | \\()</_ ) | \\()</_ ) | Yes | 15.78 |
| 20 | <((\)((\\ | <((\)((\\) | No | 6.61 |
