# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-26 10:33:30

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
| sudoku_game | 25902 | 33521 | 59423 | 5 | 15 | 8.55 | 171.26 |
| add_numbers | 25262 | 5170 | 30432 | 20 | 0 | 4.16 | 83.35 |
| counting_zeros | 25030 | 35100 | 60130 | 18 | 2 | 9.78 | 195.86 |
| task_decoding | 25466 | 7977 | 33443 | 20 | 0 | 5.76 | 115.51 |
| task_summation | 25242 | 15975 | 41217 | 20 | 0 | 6.64 | 133.02 |
| task_transcription | 24748 | 5182 | 29930 | 16 | 4 | 4.04 | 80.89 |
| task_sequences | 3375 | 5628 | 9003 | 20 | 0 | 4.12 | 82.42 |
| string_entry | 25478 | 12824 | 38302 | 13 | 7 | 5.00 | 100.03 |
| **TOTAL** | **180503** | **121377** | **301880** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 2 5 3 1 5 5 3 1 6 6 4 3 | 5 6 2 5 3 5 1 1 3 6 5 6 4 3 | No | 7.94 |
| 2 | 5 2 4 6 3 1 2 2 6 4 3 5 5 6 | 5 2 4 6 3 1 2 2 6 4 3 5 5 6 | Yes | 8.5 |
| 3 | 5 3 4 5 3 1 5 1 1 6 5 2 4 6 | 5 3 4 5 1 3 1 5 5 6 1 2 4 6 | No | 8.5 |
| 4 | 3 5 6 5 3 4 2 6 1 6 3 2 6 5 | 3 5 6 5 3 4 2 1 1 6 3 6 5 2 | No | 8.36 |
| 5 | 1 6 4 6 4 3 2 1 3 1 4 4 5 1 | 1 6 4 6 4 3 1 2 3 1 4 4 5 1 | No | 7.48 |
| 6 | 4 5 5 6 6 2 3 4 1 1 2 4 6 3 | 4 5 5 6 6 2 1 3 4 6 2 4 3 6 | No | 9.05 |
| 7 | 5 1 6 4 2 1 4 6 3 1 1 2 3 4 | 5 1 6 4 1 2 4 6 3 1 2 4 1 3 | No | 8.56 |
| 8 | 1 5 2 4 6 2 4 3 3 1 5 3 6 4 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Grid analysis:** - Row 1: 6 4 **5** \| 3 **1** 2 - Row 2: 3 1 | No | 17.09 |
| 9 | 4 5 5 6 2 4 1 3 6 6 5 4 6 4 | 4 5 6 5 2 4 1 6 3 4 5 6 6 4 | No | 6.83 |
| 10 | 2 5 4 1 6 3 2 1 5 4 3 6 1 6 | 2 5 4 1 6 3 2 1 5 4 3 6 1 6 | Yes | 6.46 |
| 11 | 6 1 3 3 6 3 6 2 5 4 3 6 2 1 | 6 1 3 3 6 3 6 2 5 4 3 6 2 1 | Yes | 8.24 |
| 12 | 3 6 1 5 4 5 4 1 5 2 2 1 6 5 | 3 5 1 6 4 5 4 1 5 2 2 1 6 5 | No | 8.15 |
| 13 | 1 4 6 6 4 1 6 3 3 1 5 4 2 3 | 1 4 6 6 4 1 6 3 3 1 5 4 2 3 | Yes | 12.31 |
| 14 | 3 1 5 2 4 4 5 3 1 5 6 3 2 4 | 3 1 5 2 4 4 5 3 1 6 3 2 4 | No | 7.65 |
| 15 | 5 2 6 1 3 1 3 2 3 5 4 3 1 6 | 5 2 6 1 3 3 1 2 3 5 4 1 3 6 | No | 5.34 |
| 16 | 3 1 5 6 2 1 4 5 6 5 2 1 3 2 | 3 1 5 6 2 1 4 5 6 5 2 1 3 2 | Yes | 7.38 |
| 17 | 6 4 3 5 1 4 3 2 6 2 5 1 1 6 | To solve the 6×6 Sudoku puzzle, we fill in the empty cells such that each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Step-by-step resolution:** 1.  **Row 1:** The missing number is 6 (2, 3, 5, 1, 4, ** | No | 9.13 |
| 18 | 2 6 1 5 1 6 3 4 6 2 4 5 6 3 | 1 6 5 2 2 6 3 2 6 4 4 5 6 3 | No | 8.41 |
| 19 | 2 6 3 6 3 5 1 4 4 6 2 1 4 2 | 6 2 3 6 3 5 1 4 4 6 2 1 4 2 | No | 6.55 |
| 20 | 3 2 5 2 4 1 4 3 5 1 2 3 5 6 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules (each row, column, and 2×3 box must contain the numbers 1-6 exactly once).  **Step-by-step resolution:** 1.  **Row 6:** [2, 3, _, 4, _, 1]. Missing numbers are {5, 6}. Looking at Column 5, we have {1, 3, 2, 5, 4}. The missing number is 6. Thus, (6,5) = 6, and (6,3) = 5. 2.  **Column 2:** [4, (2,2), 6, (4,2), 5, 3]. Missing numbers are {1, 2}. Box 1 contains {4, 5, 1}. The missing numbers are {2, 3, 6}. Since (2,2) must be 1 or 2, and 1 is already in Box 1, (2,2) = 2. Consequently, (4,2) = 1. 3.  **Column 1:** [(1,1), 5, (3,1), 4, 6, 2]. Missing numbers are {1, 3}. Looking at Row 1, we have {4, 1, 6}. Looking at Row 3, we have {6, 2}. Since (1,1) cannot be 1 (already in R1), (1,1) = 3 and (3,1) = 1. 4.  **Row 1:** [3, 4, (1,3), (1,4), 1, 6]. Missing numbers are {2, 5}. Column 3 has {5, 1, 6, 3}. Thus, (1,3) = 2, and (1,4) = 5. 5.  **Box 1:** [3, 4, 2, 5, 2, 1] — wait, checking the grid:     *   (1,1)=3, (1,2)=4, (1 | No | 9.17 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1887 | 1887 | Yes | 3.98 |
| 2 | 1051 | 1051 | Yes | 2.49 |
| 3 | 1106 | 1106 | Yes | 2.35 |
| 4 | 1198 | 1198 | Yes | 2.85 |
| 5 | 1373 | 1373 | Yes | 2.4 |
| 6 | 1693 | 1693 | Yes | 4.46 |
| 7 | 1447 | 1447 | Yes | 3.11 |
| 8 | 1577 | 1577 | Yes | 4.2 |
| 9 | 1936 | 1936 | Yes | 2.97 |
| 10 | 1977 | 1977 | Yes | 2.9 |
| 11 | 1179 | 1179 | Yes | 2.9 |
| 12 | 2037 | 2037 | Yes | 3.32 |
| 13 | 1562 | 1562 | Yes | 3.82 |
| 14 | 1676 | 1676 | Yes | 5.51 |
| 15 | 2030 | 2030 | Yes | 5.48 |
| 16 | 2172 | 2172 | Yes | 10.69 |
| 17 | 1380 | 1380 | Yes | 3.33 |
| 18 | 911 | 911 | Yes | 9.71 |
| 19 | 1630 | 1630 | Yes | 4.54 |
| 20 | 1698 | 1698 | Yes | 2.26 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 43 | 43 | Yes | 8.32 |
| 2 | 38 | 38 | Yes | 7.99 |
| 3 | 54 | 54 | Yes | 7.97 |
| 4 | 58 | 58 | Yes | 8.88 |
| 5 | 37 | 37 | Yes | 11.16 |
| 6 | 40 | 40 | Yes | 6.66 |
| 7 | 39 | 39 | Yes | 5.94 |
| 8 | 72 | To count the total number of zeros in the provided image, we examine each row one by one:  1.  0 0 0 1 0 0 1 1 1 1: 5 zeros 2.  0 0 1 1 1 1 0 1 1 1: 3 zeros 3. | No | 18.85 |
| 9 | 71 | 71 | Yes | 4.61 |
| 10 | 51 | 51 | Yes | 6.84 |
| 11 | 58 | 58 | Yes | 7.04 |
| 12 | 57 | 57 | Yes | 9.22 |
| 13 | 44 | To count the total number of zeros in the image, we examine each row individually:  1.  Row 1: 1 1 1 1 1 1 1 1 1 0 (1 zero) 2.  Row 2: 1 1 0 1 1 0 1 1 1 1 (2 zeros) | No | 11.87 |
| 14 | 55 | 55 | Yes | 8.5 |
| 15 | 56 | 56 | Yes | 8.77 |
| 16 | 44 | 44 | Yes | 8.11 |
| 17 | 49 | 49 | Yes | 8.6 |
| 18 | 47 | 47 | Yes | 18.95 |
| 19 | 43 | 43 | Yes | 9.64 |
| 20 | 57 | 57 | Yes | 17.65 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WMKXNBE | WMKXNBE | Yes | 2.74 |
| 2 | ULERBNW | ULERBNW | Yes | 2.94 |
| 3 | HRZKALQ | HRZKALQ | Yes | 3.77 |
| 4 | WNCYGEP | WNCYGEP | Yes | 4.05 |
| 5 | ANHGYOW | ANHGYOW | Yes | 6.13 |
| 6 | JZWXUHE | JZWXUHE | Yes | 4.86 |
| 7 | MKYTFBW | MKYTFBW | Yes | 4.69 |
| 8 | BCTUEZF | BCTUEZF | Yes | 3.56 |
| 9 | TIMJSWN | TIMJSWN | Yes | 13.51 |
| 10 | PVLOIFT | PVLOIFT | Yes | 3.07 |
| 11 | OBTSQVG | OBTSQVG | Yes | 3.51 |
| 12 | XSHGCDB | XSHGCDB | Yes | 3.13 |
| 13 | XKFYABT | XKFYABT | Yes | 7.68 |
| 14 | ZCAITOL | ZCAITOL | Yes | 3.83 |
| 15 | BFICQKZ | BFICQKZ | Yes | 2.82 |
| 16 | ELHCNDF | ELHCNDF | Yes | 5.8 |
| 17 | IHZEBNU | IHZEBNU | Yes | 5.45 |
| 18 | TAPQYSR | TAPQYSR | Yes | 6.23 |
| 19 | JSYKBGZ | JSYKBGZ | Yes | 12.83 |
| 20 | YZDPNLO | YZDPNLO | Yes | 14.68 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.16 |
| 2 | [3.4, 6.6] | 6.6 3.4 | Yes | 14.66 |
| 3 | [0.8, 9.2] | 0.8 9.2 | Yes | 3.97 |
| 4 | [2.0, 8.0] | 8.0 2.0 | Yes | 4.69 |
| 5 | [3.2, 6.8] | 6.8 3.2 | Yes | 4.48 |
| 6 | [0.1, 9.9] | 9.9 0.1 | Yes | 14.86 |
| 7 | [4.3, 5.7] | 5.7 4.3 | Yes | 4.22 |
| 8 | [4.0, 6.0] | 4.0 6.0 | Yes | 4.54 |
| 9 | [5.0, 5.0] | 5.0 5.0 | Yes | 8.77 |
| 10 | [2.1, 7.9] | 7.9 2.1 | Yes | 14.54 |
| 11 | [2.2, 7.8] | 2.2 7.8 | Yes | 7.81 |
| 12 | [4.9, 5.1] | 4.9 5.1 | Yes | 3.94 |
| 13 | [0.6, 9.4] | 9.4 0.6 | Yes | 3.88 |
| 14 | [1.2, 8.8] | 1.2 8.8 | Yes | 4.13 |
| 15 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.67 |
| 16 | [3.2, 6.8] | 3.2 6.8 | Yes | 3.68 |
| 17 | [2.2, 7.8] | 2.2 7.8 | Yes | 8.63 |
| 18 | [1.7, 8.3] | 8.3 1.7 | Yes | 7.04 |
| 19 | [0.7, 9.3] | 9.3 0.7 | Yes | 4.27 |
| 20 | [4.5, 5.5] | 5.5 4.5 | Yes | 4.85 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CW0LQWX6N0MP | CW0LOWX6N0MP | No | 6.94 |
| 2 | ROWSWA1I9A0M | ROWSWA119A0M | No | 6.99 |
| 3 | TPNCLXI7R7OZ | TPNCLXI7R7OZ | Yes | 1.61 |
| 4 | EICZP2NKUPAM | EICZP2NKUPAM | Yes | 2.36 |
| 5 | IF2OQ51750KO | IF20051750K0 | No | 5.23 |
| 6 | 281U8VA4MEPZ | 281U8VA4MEPZ | Yes | 6.12 |
| 7 | F5N6AGJ8U2LO | F5N6AGJ8U2LO | Yes | 1.97 |
| 8 | 37FVZK2L08SS | 37FVZK2L08SS | Yes | 1.35 |
| 9 | 64QTGFUIVEV0 | 64QTGFUIVEV0 | Yes | 4.79 |
| 10 | ZPYBH56KQLBI | ZPYBH56KQLBI | Yes | 2.42 |
| 11 | 3MF8FTX4OW2V | 3MF8FTX4OW2V | Yes | 7.32 |
| 12 | 5RGFCEHT4DCJ | 5RGFCEHT4DCJ | Yes | 4.19 |
| 13 | POO9RJCE2WNS | POO9RJCE2WNS | Yes | 1.64 |
| 14 | J6EHKODLYDR6 | J6EHKODLYDR6 | Yes | 3.36 |
| 15 | L2PDH1UNHU4F | L2PDH1UNHU4F | Yes | 1.81 |
| 16 | P3T90W9RAHCG | P3T90W9RAHCG | Yes | 9.46 |
| 17 | UCBP5GEXZCY6 | UCBP5GEXZCY6 | Yes | 4.21 |
| 18 | 2EGA2MOQCPYV | 2EGA2MOOCPYV | No | 2.7 |
| 19 | O8HROMSBALMZ | O8HROMSBALMZ | Yes | 4.02 |
| 20 | C0B8440FBG5X | C0B8440FBG5X | Yes | 2.32 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 19.32 |
| 2 | 36 | 36 | Yes | 2.22 |
| 3 | 39 | 39 | Yes | 3.81 |
| 4 | 23 | 23 | Yes | 2.24 |
| 5 | 63 | 63 | Yes | 2.55 |
| 6 | 31 | 31 | Yes | 2.09 |
| 7 | 3 | 3 | Yes | 2.31 |
| 8 | 9 | 9 | Yes | 2.33 |
| 9 | 48 | 48 | Yes | 2.64 |
| 10 | 7 | 7 | Yes | 4.24 |
| 11 | 73 | 73 | Yes | 2.37 |
| 12 | 65 | 65 | Yes | 2.86 |
| 13 | 19 | 19 | Yes | 2.54 |
| 14 | 60 | 60 | Yes | 12.98 |
| 15 | 44 | 44 | Yes | 2.32 |
| 16 | 16 | 16 | Yes | 1.9 |
| 17 | 28 | 28 | Yes | 2.46 |
| 18 | 26 | 26 | Yes | 4.09 |
| 19 | 1 | 1 | Yes | 2.71 |
| 20 | 10 | 10 | Yes | 4.45 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (<(//((_/ | (<(//((_/ | Yes | 2.94 |
| 2 |  _))(_(_( | _))(_(_( | No | 3.52 |
| 3 | (<))\_ \< | (<))\_\ \< | No | 5.59 |
| 4 | __\/)<) ( | __\/)<) ( | Yes | 4.15 |
| 5 | /<(  /<(  | /< (  /< ( ␣ | No | 7.28 |
| 6 | ))<\_))_( | ))<\_))_( | Yes | 4.65 |
| 7 | _)_(<\((< | _)_(<\((< | Yes | 4.56 |
| 8 | \\<_\\)<< | \\<_\\)<< | Yes | 4.08 |
| 9 | _ )_(__(  | _ )_(__( ␣ | No | 5.61 |
| 10 | \</))(_ / | \< /))(_ / | No | 13.84 |
| 11 | /)_ _<\\_ | /)_ _<\\_ | Yes | 5.13 |
| 12 | /)/)//\\_ | /)/)//\\_ | Yes | 3.87 |
| 13 | _\ /_(()\ | _\ /_(()\ | Yes | 4.05 |
| 14 | /<_(\((_< | /<_(\((_< | Yes | 4.28 |
| 15 | /)<( \()  | /)< (\()_ | No | 4.25 |
| 16 | _ ((</)\< | _ ((</)\< | Yes | 3.36 |
| 17 | /)\  \)<_ | /)\  \)<_ | Yes | 5.6 |
| 18 | <)/ _\<)< | <)/ _\<)< | Yes | 3.75 |
| 19 | )_<(<(/ \ | )_<(<(/ \ | Yes | 3.97 |
| 20 |  </ (/ <_ | < / ( / <_ | No | 5.5 |
