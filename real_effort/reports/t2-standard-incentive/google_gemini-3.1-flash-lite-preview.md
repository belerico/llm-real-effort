# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-26 10:34:18

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
| sudoku_game | 25540 | 34494 | 60034 | 6 | 14 | 10.20 | 204.11 |
| add_numbers | 24898 | 4863 | 29761 | 20 | 0 | 5.08 | 101.79 |
| counting_zeros | 24664 | 38852 | 63516 | 9 | 11 | 8.94 | 179.13 |
| task_decoding | 25104 | 10636 | 35740 | 17 | 3 | 6.25 | 125.28 |
| task_summation | 23641 | 15338 | 38979 | 18 | 2 | 13.10 | 262.27 |
| task_transcription | 24236 | 3849 | 28085 | 15 | 5 | 3.80 | 76.07 |
| task_sequences | 3022 | 8088 | 11110 | 18 | 2 | 3.59 | 71.87 |
| string_entry | 25124 | 16208 | 41332 | 11 | 9 | 6.64 | 132.79 |
| **TOTAL** | **176229** | **132328** | **308557** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 4 6 1 2 5 2 4 3 4 1 2 3 | 4 6 4 6 1 2 5 2 4 3 4 1 2 3 | Yes | 9.27 |
| 2 | 2 4 3 6 5 2 2 1 5 2 4 4 3 1 | 2 4 3 6 5 2 2 1 5 2 4 4 3 1 | Yes | 7.85 |
| 3 | 6 2 5 1 3 6 6 4 5 5 4 3 1 2 | 6 2 5 1 3 6 6 5 4 4 5 3 1 2 | No | 8.16 |
| 4 | 4 5 2 6 1 3 2 2 3 4 3 4 1 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Initial Grid:** ``` R1: [., ., 3, ., ., .] R2: [1, ., 6, 5, 2, 4] R3: [6, ., 4, 1, 3, 5] R4: [5, 6, ., 4, 1, 3] R5: [2, 1, 5, ., ., 6] R6: [., ., ., 6, 5, .] ```  **Step-by-step resolution:** 1.  **R2C2:** Missing 3. Row 2 is now [1, 3, 6, 5, 2, 4]. 2.  **R3C2:** Missing 2. Row 3 is now [6, 2, 4, 1, 3, 5]. 3.  **R4C3:** Missing 2. Row 4 is now [5, 6, 2, 4, 1, 3]. 4.  **R6C3:** Column 3 missing 1. R6C3 = 1. 5.  **R5C4 and R5C5:** Row 5 missing 3, 4. Column 4 missing 2, 3. Column 5 missing 4, 6. R5C4 = 3, R5C5 = 4. Row 5 is [2, 1, 5, 3, 4, 6]. 6.  **R6C1, R6C2, R6C6:** Row 6 missing 2, 3, 4. R6C1 = 4, R6C2 = 2, R6C6 = 3. Row 6 is [4, 2, 1, 6, 5, 3]. 7.  **R1C1, R1C2, R1C4, R1C5, R1C6:** Row 1 missing 1, 2, 4, 5, 6.     *   R1C1 = 5, R1C2 = 4, R1C4 = 2, R1C5 = 6, R1C6 = 1. Row 1 is [5, 4, 3, 2, 6, 1].  **Completed Grid:** ``` 5 4 3 2 6 1 1 3 6 5 2 4 6 2 4 1 3 5 5 6 2 4 1 3 2 1 5 3 4 6 4 2 1 6 5 3 ```  **Missing numbers in reading order:** R1C1: 5, R1C2: 4, R1C4: 2, R1C5: 6, R1C6: 1 | No | 13.19 |
| 5 | 1 4 3 2 6 4 5 4 1 4 6 6 5 2 | 1 4 3 4 6 2 5 4 1 4 6 6 5 2 | No | 9.67 |
| 6 | 3 2 4 5 6 4 3 2 5 2 5 4 6 3 | 3 2 4 6 5 4 3 2 5 2 5 4 6 3 | No | 7.42 |
| 7 | 4 6 3 5 1 3 6 4 5 1 5 2 1 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Step-by-step resolution:** 1.  **Row 2:** Missing numbers are 1 and 5. Column 3 has 1, 5, 2, 6, 4. R2C3 must be 5, leaving R2C6 as 1. 2.  **Row 1:** Missing numbers are 3, 4, 6. Column 1 already has 2, 5, 3, 6. Missing 1 and 4. Since R1C1 must be 4, R1C2 is 6, and R1C6 is 3. R5C1 is 1. 3.  **Row 3:** Missing numbers are 3 and 6. Column 3 already has 1, 5, 2, 6, 4. R3C3 is 3, making R3C4 6. 4.  **Row 4:** Missing numbers are 4 and 5. Column 4 already has 2, 4, 6, 3. R4C4 is 5, making R4C2 4. 5.  **Row 5:** Missing numbers are 1 and 5. R5C1 is 1, so R5C2 is 5. | No | 9.53 |
| 8 | 3 1 6 2 3 4 5 4 5 1 6 1 5 3 | 3 1 6 2 4 5 3 5 4 1 6 1 3 5 | No | 9.99 |
| 9 | 2 1 2 5 1 5 4 2 3 2 1 6 2 1 | 2 1 2 5 1 5 4 2 3 2 1 6 2 1 | Yes | 14.62 |
| 10 | 4 1 5 4 2 1 4 3 1 4 5 6 3 2 | 4 1 5 4 2 1 4 3 1 4 5 6 3 2 | Yes | 7.29 |
| 11 | 1 3 6 2 3 1 2 4 1 6 1 2 3 4 | 1 3 6 2 3 1 2 4 1 6 1 2 3 4 | Yes | 10.64 |
| 12 | 1 6 3 5 5 4 2 4 5 6 1 5 2 6 | 5 6 3 1 5 4 2 4 5 1 6 6 2 5 | No | 9.17 |
| 13 | 1 5 1 3 4 1 3 5 4 6 2 3 5 4 | 1 5 1 3 4 1 3 5 4 6 2 3 5 4 | Yes | 11.3 |
| 14 | 3 1 4 6 5 6 5 6 3 2 5 1 6 1 | To solve the 6×6 Sudoku, we fill in the missing numbers row by row, ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  1.  **Row 1:** The missing numbers are 1 and 3. Looking at Column 2, it already has 1 (at Row 2), so (1,2) must be 3 and (1,4) must be 1. Row 1: **5 3 4 1 2 6**. 2.  **Row 4:** The missing number is 6. Row 4: **1 4 2 3 6 5**. 3.  **Column 5:** Missing numbers in Column 5 were 5 and 6. Since (4,5) is 6, (2,5) must be 5. 4.  **Row 2:** Missing numbers are 4 and 6. Given the constraints of the box and columns, (2,1) is 4 and (2,3) is 6. Row 2: **4 1 6 2 5 3**. 5.  **Row 3:** Missing numbers are 5 and 6. Column 2 needs 6 (as 2 is taken by (5,2)), so (3,2) is 6 and (3,4) is 5. Row 3: **2 6 3 5 1 4**. 6.  **Row 5:** Missing numbers are 1, 2, 3, 5. Column 1 needs 3, Column 2 needs 2, Column 3 needs 1, Column 6 needs 5. Row 5: **3 2 1 6 4 5**. 7.  **Row 6:** Missing numbers are 1 and 6. Column 1 needs 6, Column 3 needs 1. Row 6: **6 5 1 4 3 2**.  **Completed Grid:** 5 3 4 1 2 6 4 1 6 2 5 3 2 6 3 5 1 4 1 4 2 3 6 5 3 2 1 6 4 5 6 5 1 4 3 2  The missing numbers in reading order are: (1,2): 3, (1,4): 1 (2,1): 4, (2,3): 6, (2,5): 5 (3,2): 6, (3,4): 5 (4,5 | No | 9.32 |
| 15 | 5 3 4 1 2 4 6 3 1 6 5 4 2 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  1.  **Row 3:** [4, 1, _, 2, 5, 3] — Missing: **6** 2.  **Row | No | 8.6 |
| 16 | 4 3 5 4 1 4 2 5 3 4 4 1 6 2 | 4 3 5 4 4 1 2 5 3 4 1 6 2 4 | No | 10.3 |
| 17 | 2 5 6 1 2 3 5 6 4 6 2 5 3 6 | 2 5 6 1 2 3 5 6 2 6 4 5 3 6 | No | 19.8 |
| 18 | 2 1 6 6 1 3 2 6 1 2 4 5 6 1 | 2 6 1 6 1 3 2 6 1 2 4 5 1 6 | No | 8.34 |
| 19 | 3 1 5 4 4 1 6 1 2 3 6 1 5 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  1.  **Analyze the grid:**     Row 1: [_, _, 2, _, _, 6]     Row 2: [_, 2, 6, 3, _, 5]     Row 3: [5, _, _, 4, _, 3]     Row 4: [6, 3, 4, 2, 5, 1]     Row 5: [2, 5, _, 1, _, 4]     Row 6: [_, 4, _, 6, 3, _]  2.  **Step-by-step filling:**     *   **Row 5:** Missing 3, 6. C3 has 2, 6, 4, so R5C3 = 3. Thus, R5C5 = 6. (Row 5: 2 5 3 1 6 4)     *   **Row 6:** Missing 1, 2, 5. C6 needs 2 (already has 6, 5, | No | 9.66 |
| 20 | 5 4 3 2 6 2 6 4 6 3 6 4 5 1 | 2 4 5 6 6 2 4 6 3 5 4 6 1 | No | 9.8 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1558 | 1558 | Yes | 7.3 |
| 2 | 2081 | 2081 | Yes | 13.7 |
| 3 | 1545 | 1545 | Yes | 2.91 |
| 4 | 1651 | 1651 | Yes | 9.4 |
| 5 | 1002 | 1002 | Yes | 2.72 |
| 6 | 2238 | 2238 | Yes | 14.19 |
| 7 | 1691 | 1691 | Yes | 7.4 |
| 8 | 1912 | 1912 | Yes | 2.57 |
| 9 | 1648 | 1648 | Yes | 8.21 |
| 10 | 2362 | 2362 | Yes | 3.11 |
| 11 | 1792 | 1792 | Yes | 4.38 |
| 12 | 2154 | 2154 | Yes | 2.99 |
| 13 | 1348 | 1348 | Yes | 2.41 |
| 14 | 1239 | 1239 | Yes | 2.67 |
| 15 | 1469 | 1469 | Yes | 2.53 |
| 16 | 2004 | 2004 | Yes | 1.99 |
| 17 | 2015 | 2015 | Yes | 5.14 |
| 18 | 1426 | 1426 | Yes | 2.93 |
| 19 | 971 | 971 | Yes | 2.4 |
| 20 | 2204 | 2204 | Yes | 2.75 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | To count the total number of zeros in the provided image, we examine each row one by one:  1.  **0** 1 1 **0** 1 1 1 **0** 1 1 (3 zeros) 2.  1 1 **0** **0** 1 1 1 1 1 1 (2 | No | 8.11 |
| 2 | 63 | 63 | Yes | 6.82 |
| 3 | 39 | 39 | Yes | 9.25 |
| 4 | 45 | 45 | Yes | 5.21 |
| 5 | 63 | To count the total number of zeros efficiently, we can count them row by row:  1.  Row 1: 0 0 1 1 1 0 0 0 0 1 — 6 zeros 2.  Row 2: 1 0 1 1 0 1 0 1 1 1 — 3 zeros 3.  Row 3: 0 0 1 1 1 0 0 1 0 0 — 6 zeros 4.  Row 4: 1 0 1 0 1 0 1 1 0 0 — 5 zeros 5.  Row 5: 1 1 1 1 0 0 1 0 1 1 — 3 zeros 6.  Row 6: 1 1 1 0 0 0 0 1 1 1 — 4 zeros 7.  Row 7: 1 1 0 0 0 0 1 1 1 0 — 5 zeros 8.  Row 8: 1 0 1 1 1 0 1 0 0 1 — 4 zeros 9.  Row 9: 1 1 1 1 0 0 0 0 1 1 — 4 zeros 10. Row 10: 1 1 1 1 1 0 1 1 0 0 — 3 zeros 11. Row 11: 1 0 1 1 1 1 1 1 1 1 — 1 zero 12. Row 12: 0 0 1 1 0 1 1 0 1 1 — 4 zeros 13. Row 13: 1 1 1 1 0 0 1 1 1 1 — 2 zeros 14. Row 14: 0 1 1 0 0 0 1 0 0 0 — 7 zeros 15. Row | No | 8.38 |
| 6 | 38 | To count the total number of zeros in the provided image, we examine each row one by one:  1.  Row 1: 0 0 1 1 1 1 1 1 0 1 (3 zeros) 2.  Row 2: 1 0 1 0 1 1 1 1 | No | 8.69 |
| 7 | 54 | To count the total number of zeros in the grid, we will count them row by row:  - Row 1: 0, 0, 1, 1, 1, 0, 0, 1, 1, 0 (5 zeros) - Row 2: 1, 0, 0, 1, 1, 0, | No | 18.55 |
| 8 | 49 | To count the total number of zeros in the provided grid, let's go through it row by row:  1.  Row 1: 1 1 0 1 1 1 1 1 1 1 - (1 zero) 2.  Row 2: 0 0 1 1 1 0 1 1 1 1 - (3 zeros) 3.  Row 3: 1 1 1 0 1 0 1 1 1 0 - (3 zeros) 4.  Row 4: 1 1 0 1 1 1 0 1 0 1 - (3 zeros) 5.  Row 5: 1 1 1 0 1 0 0 1 1 1 - (3 zeros) 6.  Row 6: 1 0 1 1 1 0 1 0 0 1 - (4 zeros) 7.  Row 7: 1 0 1 1 1 1 1 0 0 1 - (3 zeros) 8.  Row 8: 1 1 1 0 0 1 1 1 0 1 - (3 zeros) 9.  Row 9: 0 1 0 0 1 1 0 1 0 1 - (5 zeros) 10. Row 10: 0 1 1 1 0 0 1 1 1 1 - (3 zeros) 11. Row 11: 0 0 0 1 0 1 0 1 1 1 - (5 zeros) 12. Row 12: 0 0 1 1 0 0 1 0 0 1 - (6 zeros) 13. Row 13: 1 1 1 1 1 0 1 1 0 1 - (2 zeros) 14. Row 14: 1 1 1 1 1 0 1 | No | 9.16 |
| 9 | 55 | 56 | No | 8.55 |
| 10 | 53 | 53 | Yes | 8.18 |
| 11 | 72 | To count the total number of zeros in the provided image, we can count them row by row:  1.  1 1 1 **0** 1 1 1 **0** 1 **0** (3 zeros) 2.  **0** 1 1 **0** **0** 1 **0** **0** **0 | No | 7.7 |
| 12 | 62 | 61 | No | 10.77 |
| 13 | 43 | To count the total number of zeros in the provided image, we examine it row by row:  1.  Row 1: 1 1 1 1 1 0 1 1 1 1 (1 zero) 2.  Row 2: 0 1 1 0 1 1 1 0 1 1 (3 zeros) 3.  Row 3: 1 1 1 0 1 0 1 0 1 0 (4 zeros) 4.  Row 4: 0 0 0 0 1 1 1 1 1 1 (4 zeros) 5.  Row 5: 1 1 1 0 1 0 0 0 0 1 (5 zeros) 6.  Row 6: 1 1 0 1 1 1 1 1 0 0 (3 zeros) 7.  Row 7: 1 1 1 0 1 1 1 0 1 0 (3 zeros) 8.  Row 8: 1 1 1 1 1 1 1 1 1 0 (1 zero) 9.  Row 9: 0 1 1 0 1 0 1 1 1 0 (4 zeros) 10. Row 10: 1 1 0 1 0 1 1 1 0 0 (4 zeros) 11. Row 11: 1 1 1 1 1 0 0 1 1 1 (2 zeros) 12. Row 12: 1 1 1 1 1 1 0 0 0 1 (3 zeros) 13. Row 13: 0 1 1 1 1 1 1 1 1 0 (2 zeros) 14. Row 14: 0 1 1 1 1 1 1 1 0 1 (2 zeros) 15. Row 15: 1 0 1 1 1 1 1 0 0 1 (3 zeros)  Summing these counts: 1 + 3 + 4 + 4 + 5 + 3 + 3 + 1 + 4 + 4 + 2 + 3 + 2 + | No | 7.46 |
| 14 | 43 | 43 | Yes | 8.68 |
| 15 | 42 | 42 | Yes | 8.24 |
| 16 | 45 | 45 | Yes | 8.19 |
| 17 | 44 | 44 | Yes | 7.49 |
| 18 | 50 | 50 | Yes | 9.57 |
| 19 | 56 | To count the number of zeros in the grid, we examine each row one by one:  1.  **Row 1:** 0 0 1 1 0 1 0 1 1 1 (4 zeros) 2.  **Row 2:** 1 1 0 1 0 1 0 1 1 1 (3 zeros) 3.  **Row 3:** 0 1 1 1 | No | 11.53 |
| 20 | 71 | To count the total number of zeros in the provided image, we can examine each row one by one:  1.  Row 1: 1 1 1 **0** 1 **0** 1 **0** 1 **0** (4 zeros) 2.  Row 2: **0** 1 **0** 1 1 | No | 8.28 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KYLSVWA | KYLSVWA | Yes | 14.1 |
| 2 | HIKZBLA | HIKZBLA | Yes | 2.54 |
| 3 | XDJBGIY | XDJBGIY | Yes | 3.13 |
| 4 | ZFYBAUX | ZFYBAUX | Yes | 2.82 |
| 5 | HKPZMWO | HKPZMWO | Yes | 7.65 |
| 6 | QFJWVEK | QFJWVEK | Yes | 4.15 |
| 7 | FSTIOKR | FSTIOKR | Yes | 4.48 |
| 8 | KNOEUJB | KNOEUJB | Yes | 5.35 |
| 9 | IPXTSDK | IPXTSDK | Yes | 6.15 |
| 10 | RBPMIDT | RBPMIDT | Yes | 3.99 |
| 11 | JEOLKQF | JEO LKQF | No | 3.65 |
| 12 | MOKPBZU | MOKPBUZ | No | 3.48 |
| 13 | EKJHYPF | EKJHYPF | Yes | 8.15 |
| 14 | COLPXER | COLPXER | Yes | 4.1 |
| 15 | ESHKLXD | ESHKLXD | Yes | 6.6 |
| 16 | ATXICZG | ATXICZG | Yes | 14.74 |
| 17 | DZJNUFR | DZJNUFR | Yes | 3.18 |
| 18 | MGVHIOS | MGVHIOS | Yes | 19.06 |
| 19 | SHWZGPX | SWZGPX | No | 3.99 |
| 20 | MXSBPUO | MXSBPUO | Yes | 3.75 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 6.1 3.9 | Yes | 7.46 |
| 2 | [3.6, 6.4] | 3.6 6.4 | Yes | 15.08 |
| 3 | [4.5, 5.5] | 5.5 4.5 | Yes | 4.15 |
| 4 | [2.2, 7.8] | 7.8 2.2 | Yes | 19.76 |
| 5 | [1.1, 8.9] | 8.9 1.1 | Yes | 4.3 |
| 6 | [1.4, 8.6] | 1.4 8.6 | Yes | 4.86 |
| 7 | [0.9, 9.1] | 0.9 9.1 | Yes | 14.81 |
| 8 | [3.6, 6.4] | 6.4 3.6 | Yes | 4.06 |
| 9 | [0.9, 9.1] | 9.1 0.9 | Yes | 3.91 |
| 10 | [4.1, 5.9] | TIMEOUT | No | 120.03 |
| 11 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.75 |
| 12 | [1.6, 8.4] | 1.6 8.4 | Yes | 3.13 |
| 13 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.76 |
| 14 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.87 |
| 15 | [3.9, 6.1] | 6.1 3.9 | Yes | 4.75 |
| 16 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.36 |
| 17 | [0.2, 9.8] | To find two numbers from the grid that sum to 10.0, we can test combinations of the numbers provided:  The grid contains: Row 1: 6.6, 0.3, 5.4, 4.2 Row 2: 9.6, 9.0, 4.3, 1.4 | No | 8.49 |
| 18 | [4.8, 5.2] | 5.2 4.8 | Yes | 11.1 |
| 19 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.62 |
| 20 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.83 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EE84EYD4VU7Y | EE84EYD4VU7Y | Yes | 4.47 |
| 2 | QMXFCH1NXMHC | QMXFCH1NXMHC | Yes | 1.38 |
| 3 | BZR27QJGB88C | BZR27QJGB88C | Yes | 2.8 |
| 4 | QLJUFZDLLT1O | QLJUFZDLLT10 | No | 6.67 |
| 5 | 0TT8XBEI29OR | 0TT8XBEI290R | No | 7.07 |
| 6 | D6EVHYAK89S0 | D6EVHYAK89S0 | Yes | 1.94 |
| 7 | RT85J5RKJ6NO | RT85J5RKJ6NO | Yes | 2.91 |
| 8 | P261KZ6VZZNA | P261KZ6VZZNA | Yes | 2.09 |
| 9 | WWK26DRIELQ5 | WWK26DRIELQ5 | Yes | 2.75 |
| 10 | 1U9JGGNRRGH0 | 1U9JGGNRRGHO | No | 7.09 |
| 11 | Q7J7C7VBPUSX | Q7J7C7VBPUSX | Yes | 2.04 |
| 12 | Z3UVUYU7E055 | Z3UVUYU7E055 | Yes | 6.91 |
| 13 | 9MQ8ZB8OFIB4 | 9MQ8ZB8OFIB4 | Yes | 4.45 |
| 14 | ONVCIIA2BA5W | ONVCIIA2BA5W | Yes | 3.69 |
| 15 | 4O10B8NGF8V9 | 4010B8NGF8V9 | No | 7.96 |
| 16 | 21MKKR2B1OC2 | 21MKKR2B10C2 | No | 4.53 |
| 17 | JTYK3U4DJ458 | JTYK3U4DJ458 | Yes | 1.55 |
| 18 | U5BIN0HZLDJO | U5BIN0HZLDJO | Yes | 2.78 |
| 19 | EEMIG0NMTK6D | EEMIG0NMTK6D | Yes | 1.34 |
| 20 | 4CS9RWTMRL84 | 4CS9RWTMRL84 | Yes | 1.54 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 2.16 |
| 2 | 36 | 36 | Yes | 2.09 |
| 3 | 243 | 243 | Yes | 2.11 |
| 4 | 9 | 9 | Yes | 1.84 |
| 5 | 64 | 64 | Yes | 3.67 |
| 6 | 39 | 39 | Yes | 2.44 |
| 7 | 4096 | 65536 | No | 5.55 |
| 8 | 19 | 19 | Yes | 4.19 |
| 9 | 3 | 3 | Yes | 3.45 |
| 10 | 1 | 1 | Yes | 3.03 |
| 11 | 198 | 198 | Yes | 2.3 |
| 12 | 48 | 48 | Yes | 12.54 |
| 13 | 67 | 67 | Yes | 2.05 |
| 14 | 44 | 44 | Yes | 2.52 |
| 15 | 26 | 26 | Yes | 3.58 |
| 16 | 65 | 65 | Yes | 2.96 |
| 17 | 793 | 793 | Yes | 1.94 |
| 18 | 5 | 18 | No | 6.5 |
| 19 | 3 | 3 | Yes | 3.98 |
| 20 | 1440 | 1440 | Yes | 2.94 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )_ _\ < / | )_ _\ < / | Yes | 5.33 |
| 2 |  \)  ))(( | \ ))(( | No | 4.89 |
| 3 | _/ )/  )( | _/ )/  )( | Yes | 14.21 |
| 4 | )))__(\/) | )))__(\/) | Yes | 5.53 |
| 5 | <__(\()<) | <__(\()<) | Yes | 14.42 |
| 6 | /(_  \\<) | /(_  \\<) | Yes | 5.57 |
| 7 | //\ //(\/ | //\ //(\/ | Yes | 5.93 |
| 8 | ))\ ()))< | ))\ (( )))< | No | 6.74 |
| 9 | //<)\/<\  | //<)\/<\_ | Yes | 4.02 |
| 10 | /<)/\( <  | /<)/\ < | No | 3.97 |
| 11 | _\ <<)\ \ | _\ <<)\ \ | Yes | 16.1 |
| 12 | ( ))_<((/ | ( ))_<((/ | Yes | 4.52 |
| 13 | (/_// _   | (/_// _ | No | 6.81 |
| 14 | \/<(_ (// | \ / < ( _ ( / / | No | 6.26 |
| 15 |  _(( )_\< | _(( )_\< | No | 4.75 |
| 16 | )_< ((\<< | )_< ((\<< | Yes | 4.14 |
| 17 | ((///<)(\ | ((///<)(\ | Yes | 4.37 |
| 18 | __(__()/) | __(__()/ ) | No | 5.03 |
| 19 |  <(_ )/(_ | <(_ )/(_ | No | 5.38 |
| 20 | _\ )<\/(_ | _\ )< \/(_ | No | 4.76 |
