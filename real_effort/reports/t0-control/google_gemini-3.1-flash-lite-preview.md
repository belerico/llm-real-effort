# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-26 10:34:33

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
| sudoku_game | 25018 | 36821 | 61839 | 6 | 14 | 10.85 | 217.1 |
| add_numbers | 24378 | 4770 | 29148 | 20 | 0 | 3.90 | 78.14 |
| counting_zeros | 24140 | 38409 | 62549 | 13 | 7 | 11.71 | 234.43 |
| task_decoding | 24584 | 10415 | 34999 | 20 | 0 | 7.68 | 153.83 |
| task_summation | 24362 | 15242 | 39604 | 20 | 0 | 5.74 | 115.01 |
| task_transcription | 23850 | 4195 | 28045 | 19 | 1 | 3.82 | 76.54 |
| task_sequences | 2488 | 6267 | 8755 | 19 | 1 | 3.88 | 77.69 |
| string_entry | 24600 | 17880 | 42480 | 9 | 11 | 6.54 | 130.84 |
| **TOTAL** | **173420** | **133999** | **307419** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 3 5 6 5 3 1 4 2 4 3 2 1 | 6 1 5 3 1 3 5 6 4 2 4 3 2 1 | No | 17.13 |
| 2 | 2 3 6 1 6 2 1 4 6 5 4 4 2 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  Given grid: ``` R1: [_, _, _, 1, 5, 4] R2: [4, 5, 3, 2, 6, _] R3: [1, _, 4, 5, 2, 3] R4: [5, _, _, 3, _, _] R5: [6, 1, _, _, 3, 2] R6: [ | No | 9.47 |
| 3 | 3 5 2 3 6 5 1 2 3 2 1 4 2 6 | 3 5 2 3 6 5 | No | 13.84 |
| 4 | 5 1 3 5 3 5 3 3 4 2 6 6 3 5 | 5 1 3 5 3 5 3 3 4 2 6 6 3 5 | Yes | 9.4 |
| 5 | 5 1 6 2 6 3 1 3 5 2 1 4 3 5 | 5 6 1 2 3 5 6 3 5 2 1 4 3 5 | No | 7.44 |
| 6 | 2 2 4 5 1 6 4 6 1 6 2 3 4 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules (each row, column, and 2×3 box contains numbers 1-6 exactly once).  **Initial Grid:** Row 1: 1 5 6 \| 0 3 4 Row 2: 0 3 0 \| 0 0 0 Row 3: 0 0 3 \| 0 2 5 Row 4: 3 4 1 \| 0 5 2 Row 5: 5 1 2 \| 4 6 3 Row 6: 6 0 5 \| 0 0 0  **Solving:** 1.  **Row 1:** Missing 2. **R1C4 = 2**. 2.  **Row 4:** Missing 6. **R4C4 = 6**. 3.  **Box (1,1):** Contains 1, 5, 6 (R1) and 3, 4 (R2). Missing is 2. **R2C1 = 2**. 4.  **Column 3:** Already has 6, 4, 3, 1, 2, 5. (Complete). 5.  **Column 1:** Has 1, 2, 3, 5, 6. Missing is 4. **R3C1 = 4**. 6.  **Column 5:** Has 3, 1, 2, 5, 6. Missing is 4. **R6C5 = 4**. 7.  **Column 6:** Has 4 | No | 12.84 |
| 7 | 1 2 3 3 5 6 2 1 5 2 4 6 3 5 | 1 3 2 3 5 6 2 1 2 5 4 6 5 3 | No | 9.14 |
| 8 | 2 4 1 5 6 5 6 1 2 4 1 5 6 2 | 2 4 1 5 6 5 6 1 2 4 | No | 14.37 |
| 9 | 3 5 1 3 2 4 4 3 1 2 5 6 3 1 | 3 5 3 1 2 4 4 1 3 2 5 6 3 1 | No | 6.31 |
| 10 | 2 5 2 3 2 3 2 5 1 3 6 5 4 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Initial Grid:** ``` 3 1 6 \| _ _ 4 5 _ 4 \| 1 6 3 ------+------ 4 6 _ \| | No | 9.92 |
| 11 | 6 2 5 2 1 2 6 3 3 4 1 1 3 4 | 6 2 5 2 1 2 6 3 3 4 1 1 3 4 | Yes | 8.77 |
| 12 | 4 2 5 3 4 5 1 4 4 1 6 3 5 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the digits 1-6 exactly once.  1.  **Grid Representation:**     Row 1: 1 _ _ \| _ 6 3     Row 2: _ 6 1 \| _ 2 _     Row 3: 2 5 3 \| 6 _ _     Row 4: _ _ 5 \| 2 3 _     Row 5: 6 _ 4 \| 1 _ 2     Row 6: 5 2 6 \| _ 4 1  2.  **Solving Step-by-Step:**     *   **Row 6:** Missing number is 3. R6C4 = 3.     *   **Column 5:** Missing numbers are 1, 5. Since R3C5 must be 1 or 4, and R5C5 must be 5, we assign R5C5 = 5 and R3C5 = 1.     *   **Row 3:** Now missing is R3C6 = 4.     *   **Column 2:** Missing numbers are 1, 4. Since R1C2 must be 4 and R4C2 must be 1.     *   **Row 4:** Missing numbers are 4, 6. Since R4C6 must be 6 (Col 6 missing 5, 6), R4C1 = 4 and R4C6 = 6.     *   **Column 6:** Missing number is 5. R2C6 = 5.     *   **Row 2:** Missing numbers are 3, 4. Since R2C4 must be 4, R2C1 = 3.     *   **Column 4:** Missing number | No | 8.3 |
| 13 | 6 2 6 5 3 2 6 4 6 4 5 1 5 3 | 6 2 6 5 3 2 6 4 6 4 5 1 5 3 | Yes | 18.14 |
| 14 | 2 3 6 1 6 5 3 4 4 2 4 1 2 1 | 2 3 6 1 6 5 3 4 4 2 4 1 2 1 | Yes | 9.91 |
| 15 | 5 1 2 4 1 3 2 6 6 4 3 3 1 5 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Initial Grid:** ``` . 4 3 \| 6 2 . . 6 . \| 1 5 3 ------+------ . . | No | 13.22 |
| 16 | 3 2 6 2 1 1 6 3 2 1 3 1 5 3 | 3 2 6 2 1 1 6 3 2 1 3 1 5 3 | Yes | 6.67 |
| 17 | 3 1 2 3 5 4 6 3 5 6 1 5 1 6 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Step-by-step derivation:** 1.  **Row 2:** The missing number is 3 (Row 2, Col 5). 2.  **Row 3:** The missing numbers are 5 and 4 (Row 3, Col 4 and Col 5). 3.  **Row 4:** | No | 8.72 |
| 18 | 3 5 6 4 2 5 5 2 2 5 3 3 2 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  1.  **Grid Representation:**     Row 1: [R1C1, 1, 2, R1C4, 4, R1C | No | 9.05 |
| 19 | 1 2 4 5 1 6 6 1 2 5 1 2 2 5 | 1 2 4 5 1 6 6 1 2 5 1 2 2 5 | Yes | 18.25 |
| 20 | 5 4 3 6 4 1 3 6 5 3 1 4 4 2 | 5 4 5 6 4 1 3 6 3 5 1 4 4 2 | No | 6.07 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1648 | 1648 | Yes | 2.6 |
| 2 | 1657 | 1657 | Yes | 3.93 |
| 3 | 1648 | 1648 | Yes | 6.04 |
| 4 | 1546 | 1546 | Yes | 5.64 |
| 5 | 2526 | 2526 | Yes | 2.33 |
| 6 | 1030 | 1030 | Yes | 2.26 |
| 7 | 1161 | 1161 | Yes | 2.75 |
| 8 | 2150 | 2150 | Yes | 2.5 |
| 9 | 1849 | 1849 | Yes | 2.35 |
| 10 | 1424 | 1424 | Yes | 3.99 |
| 11 | 2371 | 2371 | Yes | 2.47 |
| 12 | 1217 | 1217 | Yes | 13.19 |
| 13 | 1053 | 1053 | Yes | 2.7 |
| 14 | 1060 | 1060 | Yes | 3.22 |
| 15 | 828 | 828 | Yes | 4.37 |
| 16 | 1832 | 1832 | Yes | 2.61 |
| 17 | 962 | 962 | Yes | 2.76 |
| 18 | 1764 | 1764 | Yes | 3.34 |
| 19 | 1489 | 1489 | Yes | 3.34 |
| 20 | 849 | 849 | Yes | 5.69 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 | 61 | Yes | 9.45 |
| 2 | 48 | 48 | Yes | 6.74 |
| 3 | 68 | To count the number of zeros in the grid, we can count them row by row:  - Row 1: 0, 0, 0, 0 (4) - Row 2: 0, 0, 0, 0, 0 (5) - Row 3: 0, 0, 0 (3) - Row 4: 0, 0, 0, 0 (4) - Row 5: 0, 0, 0, 0, 0, 0 (6) - Row 6: 0, 0, 0, 0, 0, 0 (6) - Row 7: 0, 0 (2) - Row 8: 0, 0, 0, 0, 0, 0 (6) - Row 9: 0, 0, 0, 0 (4) - Row 10: 0, 0, 0, 0, 0, 0 (6) - Row 11: 0, 0, 0, 0, 0, 0 (6) - Row 12: 0, 0 (2) - Row 13: 0, 0, 0, 0, 0 (5) - Row 14: 0, 0, 0, 0 (4) - Row 15: 0, 0, 0, 0, 0 (5)  Summing these counts: 4 + 5 + 3 + 4 + 6 + 6 + | No | 10.53 |
| 4 | 39 | 39 | Yes | 8.99 |
| 5 | 35 | 35 | Yes | 20.52 |
| 6 | 40 | To count the total number of zeros in the grid, we examine each row one by one:  1.  Row 1: 1 **0** 1 1 1 **0** 1 **0** **0** 1 (4 zeros) 2.  Row 2: 1 1 1 1 1 1 1 1 1 1 (0 zeros) 3.  Row 3: 1 1 1 1 **0** **0** 1 1 1 1 (2 zeros) 4.  Row 4: 1 1 1 **0** **0** 1 **0** 1 1 1 (3 zeros) 5.  Row 5: 1 1 1 1 1 1 1 1 1 1 (0 zeros) 6.  Row 6: 1 1 1 **0** **0** **0** 1 **0** **0** **0** (6 zeros) 7.  Row 7: 1 1 1 1 1 1 **0** 1 1 **0** (2 zeros) 8.  Row 8: 1 **0** 1 1 1 **0** **0** 1 1 1 (3 zeros) 9.  Row 9: **0** 1 **0** 1 1 1 1 1 **0** 1 (3 zeros) 10. Row 10: **0** **0** 1 **0** **0** 1 1 1 1 **0** (5 zeros) 11. Row 11: **0** 1 1 1 1 1 1 1 1 1 (1 zero) 12. Row 12: 1 **0** 1 1 **0** 1 1 **0** 1 1 (3 | No | 8.0 |
| 7 | 36 | 36 | Yes | 7.21 |
| 8 | 60 | To count the zeros in the image, we examine each row individually:  1.  1 1 1 **0** **0** 1 **0** **0** **0** 1 (5 zeros) 2.  1 1 1 **0** 1 1 1 **0** 1 1 (2 zeros) 3. | No | 9.68 |
| 9 | 50 | 50 | Yes | 7.95 |
| 10 | 44 | 44 | Yes | 6.8 |
| 11 | 36 | 36 | Yes | 6.61 |
| 12 | 52 | 52 | Yes | 7.55 |
| 13 | 49 | 49 | Yes | 8.96 |
| 14 | 49 | To count the total number of zeros in the grid, we examine each row one by one:  1.  **Row 1:** 0 1 0 1 0 0 0 0 1 1 — (6 zeros) 2.  **Row 2:** 0 1 1 1 1 1 1 1 1 | No | 18.63 |
| 15 | 52 | To count the zeros in the provided image, we examine each row one by one:  1.  Row 1: 1 0 0 0 0 0 0 0 0 0 (9 zeros) 2.  Row 2: 0 1 0 0 0 0 0 1 1 1 (6 zeros | No | 18.52 |
| 16 | 58 | To count the total number of zeros in the provided image, we examine each row one by one:  1.  Row 1: 1 1 1 1 1 1 **0** **0** **0** 1 (3 zeros) 2.  Row 2: 1 **0** **0** 1 **0** **0** | No | 42.29 |
| 17 | 39 | 39 | Yes | 7.49 |
| 18 | 53 | 53 | Yes | 8.88 |
| 19 | 63 | To count the total number of zeros in the image, we examine each row one by one:  1.  `1 0 1 0 1 0 1 1 1 0` — 4 zeros 2.  `1 1 0 1 1 1 1 1 1 0` — 2 zeros 3. | No | 8.66 |
| 20 | 35 | 35 | Yes | 10.69 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZBWELPG | ZBWELPG | Yes | 9.61 |
| 2 | DQNCWOK | DQNCWOK | Yes | 7.45 |
| 3 | LUJDREA | LUJDREA | Yes | 2.82 |
| 4 | YSPENUM | YSPENUM | Yes | 4.07 |
| 5 | SQCLTUX | SQCLTUX | Yes | 14.72 |
| 6 | LIPYKOZ | LIPYKOZ | Yes | 3.68 |
| 7 | OBDYQSX | OBDYQSX | Yes | 3.44 |
| 8 | TPZUONS | TPZUONS | Yes | 3.37 |
| 9 | QDYINXH | QDYINXH | Yes | 3.9 |
| 10 | YJDIMUF | YJDIMUF | Yes | 3.48 |
| 11 | WRVGUDY | WRVGUDY | Yes | 6.67 |
| 12 | NCWSVFI | NCWSVFI | Yes | 4.4 |
| 13 | TFIGCYP | TFIGCYP | Yes | 41.26 |
| 14 | ZYWLDTB | ZYWLDTB | Yes | 3.51 |
| 15 | GFDNQLB | GFDNQLB | Yes | 6.84 |
| 16 | DIJOSXE | DIJOSXE | Yes | 15.79 |
| 17 | ZIKFLUG | ZIKFLUG | Yes | 4.05 |
| 18 | XGYPQJM | XGYPQJM | Yes | 3.89 |
| 19 | WBLNCGJ | WBLNCGJ | Yes | 3.41 |
| 20 | JANSZTE | JANSZTE | Yes | 7.28 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.7, 7.3] | 2.7 7.3 | Yes | 4.46 |
| 2 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.2 |
| 3 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.91 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 4.54 |
| 5 | [0.3, 9.7] | 9.7 0.3 | Yes | 3.79 |
| 6 | [0.6, 9.4] | 9.4 0.6 | Yes | 8.09 |
| 7 | [4.6, 5.4] | 4.6 5.4 | Yes | 9.01 |
| 8 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.64 |
| 9 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.97 |
| 10 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.37 |
| 11 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.41 |
| 12 | [4.4, 5.6] | 5.6 4.4 | Yes | 8.73 |
| 13 | [0.9, 9.1] | 9.1 0.9 | Yes | 4.78 |
| 14 | [1.9, 8.1] | 1.9 8.1 | Yes | 5.26 |
| 15 | [2.1, 7.9] | 7.9 2.1 | Yes | 4.92 |
| 16 | [1.8, 8.2] | 8.2 1.8 | Yes | 3.83 |
| 17 | [1.6, 8.4] | 1.6 8.4 | Yes | 5.25 |
| 18 | [4.9, 5.1] | 4.9 5.1 | Yes | 6.02 |
| 19 | [3.4, 6.6] | 3.4 6.6 | Yes | 2.73 |
| 20 | [2.0, 8.0] | 8.0 2.0 | Yes | 7.88 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XE8QRX13QM3W | XE8QRX13QM3W | Yes | 3.08 |
| 2 | 9DI727AM0RR9 | 9DI727AM0RR9 | Yes | 7.99 |
| 3 | NVIUWTXTLMWQ | NVIUWTXTLMWQ | Yes | 2.94 |
| 4 | WH2S2AVIO72F | WH2S2AVIO72F | Yes | 1.85 |
| 5 | OF9ASJEWHSB6 | OF9ASJEWHSB6 | Yes | 2.19 |
| 6 | PLFTW0IWY7ZV | PLFTW0IWY7ZV | Yes | 2.88 |
| 7 | DVM1FP2QU509 | DVM1FP2QU509 | Yes | 2.02 |
| 8 | ML6KEJF0ZR98 | ML6KEJF0ZR98 | Yes | 3.77 |
| 9 | U3UPKIHIT5N4 | U3UPKIHIT5N4 | Yes | 2.37 |
| 10 | WM7W89S6CGTU | WM7W89S6CGTU | Yes | 1.66 |
| 11 | LSV39QBMKRR9 | LSV39QBMKRR9 | Yes | 4.99 |
| 12 | SBFOPG9YQECW | SBFOPG9YQECW | Yes | 2.59 |
| 13 | AX0GP4IXK3EB | AX0GP4IXK3EB | Yes | 2.4 |
| 14 | T3NQJ03B5VKY | T3NQJ03B5VKY | Yes | 6.38 |
| 15 | D005OETWA54P | D005OETWA54P | Yes | 2.43 |
| 16 | 9JJ1MQQT9ARW | 9JJ1MOQT9ARW | No | 4.81 |
| 17 | 7VAGA5LBKD47 | 7VAGA5LBKD47 | Yes | 2.97 |
| 18 | 9DN4I79RFVK2 | 9DN4I79RFVK2 | Yes | 4.0 |
| 19 | 5NZA74QIRYJI | 5NZA74QIRYJI | Yes | 1.44 |
| 20 | Q4OMY3JDKZY0 | Q4OMY3JDKZY0 | Yes | 13.7 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 2.09 |
| 2 | 9 | 9 | Yes | 2.15 |
| 3 | 48 | 48 | Yes | 2.35 |
| 4 | 4 | 4 | Yes | 4.35 |
| 5 | 44 | 44 | Yes | 2.58 |
| 6 | 36 | 36 | Yes | 2.33 |
| 7 | 10 | 10 | Yes | 2.1 |
| 8 | 31 | 31 | Yes | 1.86 |
| 9 | 23 | 23 | Yes | 12.27 |
| 10 | 1 | 1 | Yes | 3.17 |
| 11 | 243 | 243 | Yes | 2.08 |
| 12 | 5 | 18 | No | 11.44 |
| 13 | 9 | 9 | Yes | 2.53 |
| 14 | 64 | 64 | Yes | 2.06 |
| 15 | 67 | 67 | Yes | 12.07 |
| 16 | 3 | 3 | Yes | 3.1 |
| 17 | 63 | 63 | Yes | 2.01 |
| 18 | 60 | 60 | Yes | 2.09 |
| 19 | 6 | 6 | Yes | 2.33 |
| 20 | 73 | 73 | Yes | 2.72 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /(\ / \(\ | /(\ / \(\ | Yes | 4.43 |
| 2 | \ ) (_<(\ | \ ) ( _ < ( \ | No | 6.17 |
| 3 |  \) \_<</ | \) \_ <</ | No | 5.84 |
| 4 | </\)< _(( | </\)< _(( | Yes | 4.83 |
| 5 | )(/_\/ (< | )(/_\/ ( < | No | 5.23 |
| 6 | /\<_)_ )  | /\<_)_ ) | No | 6.5 |
| 7 | <_) \((_( | <_) \((_( | Yes | 4.72 |
| 8 | \</ )< _/ | \ < / ) < _ / | No | 5.82 |
| 9 | ( \)__((  | ( \ )__(( ␣ | No | 6.02 |
| 10 | (<\\/(_(/ | (<\ \ /(_(/ | No | 9.42 |
| 11 | )_()\<\// | )_( ()\<\/\/ | No | 9.43 |
| 12 | <))</ )(\ | <))</ )(\ | Yes | 8.06 |
| 13 | (<_/<<_ _ | (<_ /<<_ _ | No | 3.89 |
| 14 | <_(<//\\( | <_(<//\\( | Yes | 9.66 |
| 15 | <(/<(/<<_ | <(/</<<_ | No | 3.1 |
| 16 | //(_(<_<_ | //(_(<_<_ | Yes | 4.04 |
| 17 | \\)</\/\_ | \\)</\/\_ | Yes | 7.37 |
| 18 | /_<\\)<<_ | /_<\\)<<_ | Yes | 7.21 |
| 19 | (<)__<()\ | (<)__<()\ | Yes | 4.54 |
| 20 | /<< ( \(  | /<<_( _\( _ | No | 14.48 |
