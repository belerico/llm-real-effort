# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-26 10:31:52

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
| sudoku_game | 25336 | 31176 | 56512 | 6 | 14 | 10.89 | 218.06 |
| add_numbers | 24698 | 4960 | 29658 | 20 | 0 | 3.85 | 77.04 |
| counting_zeros | 24462 | 35545 | 60007 | 16 | 4 | 8.30 | 166.36 |
| task_decoding | 24904 | 10254 | 35158 | 18 | 2 | 5.40 | 108.11 |
| task_summation | 24690 | 15995 | 40685 | 20 | 0 | 6.94 | 139.02 |
| task_transcription | 24272 | 3862 | 28134 | 18 | 2 | 4.14 | 82.88 |
| task_sequences | 2812 | 6718 | 9530 | 19 | 1 | 3.12 | 62.39 |
| string_entry | 24920 | 15261 | 40181 | 6 | 14 | 6.09 | 121.92 |
| **TOTAL** | **176094** | **123771** | **299865** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 4 5 2 4 1 1 4 5 5 3 4 2 | 2 1 4 5 2 4 1 1 4 5 5 3 4 2 | Yes | 6.95 |
| 2 | 1 4 6 6 2 1 4 2 1 6 2 5 1 2 | 1 4 6 6 2 4 1 2 1 6 2 5 1 2 | No | 9.74 |
| 3 | 4 6 3 2 6 6 3 5 1 3 2 6 4 6 | 6 3 4 2 6 6 3 5 1 3 2 6 4 6 | No | 21.79 |
| 4 | 3 1 4 4 2 6 5 3 6 4 2 1 4 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Initial Grid:** ``` . . 2 \| 6 5 . . . 5 \| 3 . 1 ------------- . 6 1 \| 4 2 . . . 3 \| . . 5 ------------- 2 5 . \| 1 . 6 1 3 6 \| 5 4 2 ```  **Step-by-step resolution:** 1.  **Column 3:** The missing number is 4. So, (5,3) = 4. 2.  **Row 5:** The missing number is 3. So, (5,5) = 3. 3.  **Column 4:** The missing number is 2. So, (4,4) = 2. 4.  **Column 5:** The missing numbers are 1 and 6. Looking at Row 2, if (2,5) = 6, then (4,5) = 1. 5.  **Column 6:** The missing numbers are 3 and 4. Looking at Row 3, (3,6) = 3, leaving (1,6) = 4. 6.  **Row 4:** The missing numbers are 4 and 6. Looking at Column 1 and 2, (4,1) = 6 and (4,2) = 4. 7.  **Row 3:** The missing number is 5. So, (3,1) = 5. 8.  **Row 2:** The missing numbers are 2 and 4. Looking at Column 1 and 2, (2,1) = 4 and (2,2) = 2. 9.  **Row 1:** The missing numbers are 1 and 3. Looking at Column 1 and 2, (1,1) = 3 and (1,2) = 1.  **Filled Grid:** ``` 3 1 2 \| 6 5 4 4 2 5 \| 3 6 1 5 6 1 \| 4 2 3 6 4 3 \| 2 1 5 2 5 4 \| 1 3 6 1 3 6 \| | No | 10.66 |
| 5 | 3 4 6 4 6 5 6 2 5 3 3 4 6 5 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Step-by-step resolution:** 1.  **Rows 4, 5, and 6:**     *   Row 4 is given: 2, 4, 3, 6, 1, 5.     *   Row 5: 5, _, _, 1, 2, 6. Missing are 3 and 4. Based on columns, R5C2=3, R5C3=4. Row 5: 5, 3, 4, 1, 2, 6.     *   Row 6: 1, _, _, 2, 4, 3. Missing are 6 and 5. Based on columns, R6C2=6, R6C3=5. Row 6: 1, 6, 5, 2, 4, 3.  2.  **Rows 1, 2, and 3:**     *   Row 2: _, 1, _, 3, | No | 36.96 |
| 6 | 3 5 6 2 6 2 1 3 6 6 6 3 4 1 | 6 5 3 2 1 2 6 3 6 6 6 3 4 1 | No | 11.12 |
| 7 | 2 3 5 4 1 4 6 2 5 6 1 6 5 6 | 2 3 5 4 1 4 6 2 5 6 1 6 5 6 | Yes | 14.83 |
| 8 | 5 2 4 1 6 1 2 4 6 5 5 6 1 5 | 5 2 4 6 1 1 2 4 5 6 5 6 1 5 | No | 7.31 |
| 9 | 3 4 2 1 3 4 4 5 3 2 6 3 6 1 | 3 4 1 6 3 4 4 5 3 2 6 3 6 1 | No | 10.58 |
| 10 | 6 1 2 5 2 3 5 4 5 2 6 4 1 3 | 6 1 2 5 2 5 4 3 4 5 6 1 5 1 4 6 | No | 6.75 |
| 11 | 6 6 3 4 1 3 6 2 4 3 1 3 1 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1–6 exactly once.  **Step-by-step resolution:** 1.  **Row 1:** 3 1 5 \| 2 4 **6** (Missing 6) 2.  **Row 3:** **4** 6 1 \| 3 5 2 (Missing 4) 3.  **Column 2:** 1, 2, 6 | No | 9.86 |
| 12 | 3 2 1 3 5 3 6 3 4 5 1 3 2 5 | 3 2 1 3 5 3 6 3 4 5 1 3 2 5 | Yes | 5.64 |
| 13 | 3 6 2 2 1 4 2 3 5 6 3 5 2 3 | 3 6 2 2 1 4 2 3 5 6 3 5 2 3 | Yes | 7.97 |
| 14 | 1 2 5 4 6 4 3 6 1 3 5 2 5 3 | 1 5 2 4 6 4 3 6 1 3 2 5 5 3 | No | 9.9 |
| 15 | 6 2 1 6 5 5 2 6 5 6 3 5 4 2 | 6 2 1 6 5 5 2 6 5 6 3 5 4 2 | Yes | 6.22 |
| 16 | 6 3 2 1 1 4 2 6 1 4 6 3 3 3 | 6 3 1 2 1 2 4 6 1 4 6 3 3 3 | No | 13.23 |
| 17 | 2 5 6 3 2 5 1 4 5 3 1 2 3 3 | 6 2 3 5 2 5 1 5 4 3 1 2 3 3 | No | 8.03 |
| 18 | 1 4 2 5 6 1 2 1 6 5 4 1 4 3 | 2 5 4 1 1 6 6 1 2 5 4 1 4 3 | No | 6.23 |
| 19 | 5 3 6 4 3 6 1 5 4 6 6 4 1 5 | 5 3 6 4 3 6 1 6 4 5 6 5 1 4 | No | 7.92 |
| 20 | 4 2 1 3 3 5 2 6 6 1 5 6 2 5 | 4 2 1 3 3 5 2 6 6 1 5 6 2 5 | Yes | 6.19 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2294 | 2294 | Yes | 2.01 |
| 2 | 2122 | 2122 | Yes | 5.73 |
| 3 | 1311 | 1311 | Yes | 3.1 |
| 4 | 1917 | 1917 | Yes | 7.68 |
| 5 | 1375 | 1375 | Yes | 3.14 |
| 6 | 901 | 901 | Yes | 2.92 |
| 7 | 1947 | 1947 | Yes | 2.38 |
| 8 | 1531 | 1531 | Yes | 2.82 |
| 9 | 858 | 858 | Yes | 7.7 |
| 10 | 1541 | 1541 | Yes | 2.75 |
| 11 | 1373 | 1373 | Yes | 2.79 |
| 12 | 1249 | 1249 | Yes | 4.86 |
| 13 | 1053 | 1053 | Yes | 3.18 |
| 14 | 1594 | 1594 | Yes | 2.58 |
| 15 | 982 | 982 | Yes | 6.58 |
| 16 | 1495 | 1495 | Yes | 2.38 |
| 17 | 1198 | 1198 | Yes | 2.93 |
| 18 | 2410 | 2410 | Yes | 4.44 |
| 19 | 1591 | 1591 | Yes | 2.43 |
| 20 | 1317 | 1317 | Yes | 4.55 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 35 | To count the total number of zeros in the image, we will examine each row:  1.  Row 1: 1 1 1 1 1 **0** 1 1 1 1 — (1 zero) 2.  Row 2: 1 1 1 1 1 **0** 1 1 **0** — ( | No | 12.76 |
| 2 | 62 | 62 | Yes | 6.25 |
| 3 | 46 | 46 | Yes | 8.12 |
| 4 | 38 | 38 | Yes | 8.7 |
| 5 | 56 | To count the total number of zeros, let's go row by row:  1.  **Row 1:** 0 1 1 1 1 0 1 1 0 1 (3 zeros) 2.  **Row 2:** 0 0 0 0 1 0 1 0 0 1 (7 zeros | No | 7.78 |
| 6 | 67 | 67 | Yes | 7.72 |
| 7 | 64 | 64 | Yes | 8.49 |
| 8 | 37 | To count the total number of zeros in the image, we examine each row one by one:  1.  Row 1: 1 1 1 1 0 0 1 1 1 1 (2 zeros) 2.  Row 2: 0 0 0 0 0 1 1 1 1 1 (5 | No | 7.8 |
| 9 | 40 | 40 | Yes | 6.67 |
| 10 | 35 | 35 | Yes | 7.5 |
| 11 | 72 | 73 | No | 8.51 |
| 12 | 57 | 57 | Yes | 7.61 |
| 13 | 75 | 75 | Yes | 9.91 |
| 14 | 67 | 67 | Yes | 7.43 |
| 15 | 38 | 38 | Yes | 9.01 |
| 16 | 44 | 44 | Yes | 7.63 |
| 17 | 66 | 66 | Yes | 9.82 |
| 18 | 71 | 71 | Yes | 8.37 |
| 19 | 46 | 46 | Yes | 6.09 |
| 20 | 67 | 67 | Yes | 9.87 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JSFQIVD | JSFQIVD | Yes | 8.81 |
| 2 | OBEZCHP | OBEZCHP | Yes | 5.34 |
| 3 | TRXEBGM | TRXE BGM | No | 7.23 |
| 4 | AJEOLVM | AJEOLVM | Yes | 3.07 |
| 5 | RVNEQOZ | RVNEQOZ | Yes | 4.78 |
| 6 | JSKGPEF | JSKGPEF | Yes | 10.01 |
| 7 | IMRVTLH | IMRVTLH | Yes | 3.2 |
| 8 | GUATYVO | GUATYVO | Yes | 8.0 |
| 9 | FIMWLBK | FIMWLBK | Yes | 4.4 |
| 10 | AHIPWCG | AHIPWCG | Yes | 7.0 |
| 11 | HQCJNDT | HQCNJDT | No | 3.98 |
| 12 | ECQPKTX | ECQPKTX | Yes | 5.45 |
| 13 | WXLKHYC | WXLKHYC | Yes | 7.21 |
| 14 | XQLBAGC | XQLBAGC | Yes | 6.09 |
| 15 | EOUKJHM | EOUKJHM | Yes | 3.75 |
| 16 | STHMFVN | STHMFVN | Yes | 6.68 |
| 17 | OYZLUAI | OYZLUAI | Yes | 2.72 |
| 18 | ODWMNBT | ODWMNBT | Yes | 4.44 |
| 19 | GVEPFQT | GVEPFQT | Yes | 3.21 |
| 20 | KDLCMIO | KDLCMIO | Yes | 2.56 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.4, 7.6] | 7.6 2.4 | Yes | 4.37 |
| 2 | [1.6, 8.4] | 1.6 8.4 | Yes | 6.55 |
| 3 | [2.5, 7.5] | 2.5 7.5 | Yes | 4.6 |
| 4 | [4.9, 5.1] | 4.9 5.1 | Yes | 5.3 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 3.76 |
| 6 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.06 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 5.19 |
| 8 | [2.6, 7.4] | 2.6 7.4 | Yes | 15.21 |
| 9 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.8 |
| 10 | [4.6, 5.4] | 5.4 4.6 | Yes | 15.22 |
| 11 | [2.8, 7.2] | 2.8 7.2 | Yes | 12.63 |
| 12 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.68 |
| 13 | [4.0, 6.0] | 4.0 6.0 | Yes | 4.1 |
| 14 | [2.7, 7.3] | 2.7 7.3 | Yes | 4.6 |
| 15 | [4.6, 5.4] | 5.4 4.6 | Yes | 6.65 |
| 16 | [0.6, 9.4] | 9.4 0.6 | Yes | 4.18 |
| 17 | [0.1, 9.9] | 9.9 0.1 | Yes | 5.5 |
| 18 | [2.4, 7.6] | 7.6 2.4 | Yes | 15.96 |
| 19 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.35 |
| 20 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.14 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VJO2XSMZJBUB | VJO2XSMZJBUB | Yes | 2.47 |
| 2 | OJBHP7ME7RWU | OJBHP7ME7RWU | Yes | 3.75 |
| 3 | R5C0IRNJT4WN | R5C0IRNJT4WN | Yes | 6.78 |
| 4 | I5C35TCBKG8N | I5C35TCBKG8N | Yes | 6.04 |
| 5 | 7GXSVB9QSXVQ | 7GXSVB9QSXVQ | Yes | 2.84 |
| 6 | L6HI7C3G18K7 | L6HI7C3G18K7 | Yes | 3.31 |
| 7 | P139C7E9XJZ6 | P139C7E9XJZ6 | Yes | 3.74 |
| 8 | T8MPXMNAI6WO | T8MPXMNAI6WO | Yes | 2.75 |
| 9 | E0M1YK8F8H2F | E0M1YK8F8H2F | Yes | 2.34 |
| 10 | SZFOI0D2I1AJ | SZFOI0D2I1AJ | Yes | 2.66 |
| 11 | JG4E17OUBRDX | JG4E17OUBRDX | Yes | 7.78 |
| 12 | 8PLM49NMVTG7 | 8PLM49NMVTG7 | Yes | 5.44 |
| 13 | 6QTK5WG2SSU0 | 6QTK5WG2SSU0 | Yes | 12.72 |
| 14 | PSWVZ1LGX3ZT | PSWVZ1LGX3ZT | Yes | 1.53 |
| 15 | LSA18GXLW3I2 | LSA18GXLW3I2 | Yes | 3.9 |
| 16 | YEYRYKK4COZK | YEYRYKK4COZK | Yes | 2.06 |
| 17 | 8BL5IU2B65SQ | 8BL5IU2B65SQ | Yes | 3.18 |
| 18 | WM2ZDK7ZVOIA | WM2ZDK7ZVOIA | Yes | 1.97 |
| 19 | 9H44B1OKF9ST | 9H44B10KF9ST | No | 5.01 |
| 20 | 7MZHRF0O50RC | 7MZHRF0050RC | No | 2.51 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 2.24 |
| 2 | 7680 | 7680 | Yes | 8.4 |
| 3 | 5 | 5 | Yes | 2.41 |
| 4 | 28 | 28 | Yes | 2.69 |
| 5 | 3 | 3 | Yes | 3.46 |
| 6 | 9 | 9 | Yes | 1.51 |
| 7 | 9 | 9 | Yes | 2.28 |
| 8 | 20 | 20 | Yes | 4.32 |
| 9 | 67 | 67 | Yes | 2.61 |
| 10 | 60 | 60 | Yes | 1.92 |
| 11 | 60 | 60 | Yes | 2.8 |
| 12 | 7 | 7 | Yes | 2.58 |
| 13 | 4 | 4 | Yes | 2.69 |
| 14 | 65 | 65 | Yes | 2.55 |
| 15 | 5 | 2 | No | 8.46 |
| 16 | 63 | 63 | Yes | 2.49 |
| 17 | 31 | 31 | Yes | 2.16 |
| 18 | 39 | 39 | Yes | 2.31 |
| 19 | 16 | 16 | Yes | 2.61 |
| 20 | 48 | 48 | Yes | 1.88 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /<( / <)) | /<( / <)) | Yes | 7.87 |
| 2 | (\)( \)(/ | (\)(_\)(/ | Yes | 3.47 |
| 3 | _)(</)\\_ | _)(</)\\ _ | No | 4.68 |
| 4 | <  /\\<\) | <  /\\<\) | Yes | 5.46 |
| 5 | /\__/(/ ) | /\__/(/ ) | Yes | 6.13 |
| 6 | / <\/(\)< | / <\/(\)< | Yes | 5.28 |
| 7 | /_\   \)\ | /_ \   \)\ | No | 6.04 |
| 8 | /(\(()/_  | /(\(()/_ | No | 3.45 |
| 9 | \/(<\(()) | \/(<\(( )) | No | 5.49 |
| 10 | /(<  (/\/ | /(<  (/ \/ | No | 7.1 |
| 11 | \(<( _\   | \(<( _\ | No | 14.98 |
| 12 | <\(<<(//_ | <\(<<(/ /_ | No | 3.58 |
| 13 |  \/(/_<// | \/(/_<// | No | 7.06 |
| 14 | _\)_\_)<_ | _\)_\_)<_ | Yes | 6.33 |
| 15 | (_ <((()_ | (_ <((())_ | No | 5.85 |
| 16 |  )/(<  _) | )/(<  _) | No | 4.81 |
| 17 | \<()<<\)< | \( )<<\)< | No | 3.87 |
| 18 | <)()(</ \ | <)(()</ \ | No | 4.14 |
| 19 | _  )\_()  | _  )\_() | No | 4.43 |
| 20 | \ _) _/)\ | \ _ ) _ / ) \ | No | 11.84 |
