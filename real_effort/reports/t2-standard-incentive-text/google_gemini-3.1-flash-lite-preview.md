# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-27 09:58:43

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
| sudoku_game | 5181 | 34479 | 39660 | 5 | 15 | 8.03 | 160.63 |
| add_numbers | 3036 | 4850 | 7886 | 20 | 0 | 3.85 | 77.07 |
| counting_zeros | 6092 | 36742 | 42834 | 11 | 9 | 8.35 | 167.0 |
| task_decoding | 4320 | 15792 | 20112 | 20 | 0 | 7.58 | 151.53 |
| task_summation | 4362 | 14456 | 18818 | 20 | 0 | 6.32 | 126.42 |
| task_transcription | 3032 | 4845 | 7877 | 20 | 0 | 4.94 | 98.78 |
| task_sequences | 3024 | 6945 | 9969 | 19 | 1 | 3.35 | 67.13 |
| string_entry | 3330 | 16587 | 19917 | 11 | 9 | 6.32 | 126.43 |
| **TOTAL** | **32377** | **134696** | **167073** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 2 1 6 5 2 1 6 4 3 6 6 4 | 4 5 2 1 6 5 2 1 6 4 3 6 6 4 | Yes | 5.98 |
| 2 | 2 4 6 1 5 6 2 6 2 3 5 1 4 3 | 5 4 6 1 2 6 5 6 2 3 5 1 4 3 | No | 7.13 |
| 3 | 1 4 1 5 6 5 4 1 5 2 6 3 6 5 | 1 4 1 5 6 5 4 1 5 2 6 3 6 5 | Yes | 7.48 |
| 4 | 3 1 6 5 5 1 3 4 5 6 3 1 5 1 | 3 1 6 5 4 5 1 3 4 5 6 1 3 1 5 | No | 8.41 |
| 5 | 6 2 2 5 4 1 5 3 5 4 5 6 4 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Puzzle analysis:** 1.  **Row 1:** . 3 4 \| 1 5 . — Missing: 2, 6. Since Col 6 already has 4, 6, 3, 2 must be in R1C6, making R1C1 = 6. (6 3 4 \| 1 5 2) 2.  **Row 2:** . . 3 \| 6 1 4 — Missing: 2, 5. Based on column constraints, R2C1 = 2, R2C2 = 5. (2 5 3 \| 6 1 4) 3.  **Row 3:** . . . \| 2 3 6 — Missing: 1, 4, 5. Based on column constraints: R3C3 = 5, R3C1 = 4, R3C2 = 1. (4 1 5 \| 2 3 6) 4.  **Row 4:** . 6 1 \| 4 2 . — Missing: 3, 5. Based on column constraints: R4C1 = 3, R4C6 = 5. (3 6 1 \| 4 2 5) 5.  **Row 5:** 1 . 2 \| . . 3 — Missing: 4, 5, 6. Based on column constraints: R5C2 = 4, R5C4 = 5, R5C5 = 6. (1 4 2 \| 5 6 3) 6.  **Row 6:** 5 2 6 \| 3 . . — Missing: 1 | No | 9.79 |
| 6 | 1 2 1 6 4 1 4 3 5 6 5 4 2 1 | 1 2 1 6 4 5 4 3 1 5 6 4 2 1 | No | 5.11 |
| 7 | 6 1 3 3 2 5 4 2 3 6 5 1 6 5 | 4 6 3 3 2 5 6 2 3 4 5 1 6 5 | No | 9.04 |
| 8 | 4 1 1 4 3 2 3 2 1 5 3 6 5 4 | 4 1 1 4 3 2 2 3 1 3 5 6 5 4 | No | 10.5 |
| 9 | 5 1 3 6 1 2 4 2 5 4 6 5 6 4 | 5 1 3 6 1 2 5 2 4 4 6 4 5 6 | No | 7.52 |
| 10 | 4 3 2 5 3 4 5 1 6 2 5 4 2 1 | 4 3 2 5 3 5 4 1 6 2 4 5 2 1 | No | 7.52 |
| 11 | 1 2 1 6 2 5 1 3 3 2 6 6 3 6 | 1 2 6 2 1 3 4 5 3 6 3 6 2 3 6 | No | 8.4 |
| 12 | 4 5 4 2 6 5 6 2 4 4 6 6 6 4 | 5 4 4 6 2 4 6 2 5 6 4 6 4 6 | No | 6.56 |
| 13 | 5 1 1 1 2 6 3 6 5 2 6 4 3 5 | 5 1 1 1 2 6 3 6 5 2 6 4 3 5 | Yes | 8.14 |
| 14 | 1 3 6 2 3 4 3 2 4 6 2 2 4 1 | 1 3 6 2 3 4 3 4 2 6 2 2 4 1 | No | 8.42 |
| 15 | 5 1 6 5 6 3 2 5 1 2 1 6 1 6 | 1 5 6 5 6 3 2 5 1 6 2 1 1 6 | No | 7.79 |
| 16 | 1 5 6 3 1 5 3 5 3 5 5 4 6 6 | 1 5 6 3 1 5 3 5 3 5 5 6 4 6 | No | 6.66 |
| 17 | 3 2 3 4 3 4 5 3 1 3 2 4 2 6 | 3 2 3 4 4 3 5 3 1 3 2 4 2 6 | No | 7.45 |
| 18 | 1 6 5 4 1 6 6 2 4 1 2 5 3 4 | 1 6 5 4 1 6 6 2 4 1 2 5 3 4 | Yes | 11.06 |
| 19 | 3 2 5 1 2 5 4 5 2 3 3 5 5 2 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers row by row, ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Puzzle Analysis:** 1.  **Row 1:** 4 6 . \| 5 1 . (Missing: 2, 3). Since column 3 already has 4, 6, 1 and box 1 has 2, 4, 6, R1C3 must be 3. Thus, R1C6 is 2.     *   Row 1: 4 6 3 \| 5 1 2 2.  **Row 2:** 2 . 4 \| 1 3 6 (Missing: 5). R | No | 12.13 |
| 20 | 5 4 1 2 6 1 3 2 6 6 5 1 1 4 | 5 4 1 2 6 1 3 2 6 6 5 1 1 4 | Yes | 5.5 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1217 | 1217 | Yes | 5.1 |
| 2 | 1954 | 1954 | Yes | 2.78 |
| 3 | 2250 | 2250 | Yes | 2.56 |
| 4 | 2092 | 2092 | Yes | 1.77 |
| 5 | 2069 | 2069 | Yes | 2.94 |
| 6 | 1765 | 1765 | Yes | 7.42 |
| 7 | 969 | 969 | Yes | 8.84 |
| 8 | 848 | 848 | Yes | 2.39 |
| 9 | 1560 | 1560 | Yes | 1.81 |
| 10 | 1559 | 1559 | Yes | 7.47 |
| 11 | 1800 | 1800 | Yes | 2.36 |
| 12 | 1533 | 1533 | Yes | 2.83 |
| 13 | 1172 | 1172 | Yes | 2.32 |
| 14 | 1755 | 1755 | Yes | 1.98 |
| 15 | 1233 | 1233 | Yes | 2.0 |
| 16 | 1198 | 1198 | Yes | 6.96 |
| 17 | 2169 | 2169 | Yes | 7.53 |
| 18 | 1936 | 1936 | Yes | 3.02 |
| 19 | 1490 | 1490 | Yes | 2.89 |
| 20 | 1067 | 1067 | Yes | 2.1 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 9.08 |
| 2 | 74 | 72 | No | 9.33 |
| 3 | 67 | 60 | No | 9.18 |
| 4 | 68 | 68 | Yes | 6.93 |
| 5 | 43 | 43 | Yes | 8.25 |
| 6 | 54 | 53 | No | 8.5 |
| 7 | 73 | To count the total number of zeros in the provided text, we analyze each line:  1.  0001010111: 0, 0, 0, 0, 0 (5 zeros) 2.  1000101100: 0, 0, 0, 0, 0, 0 (6 zeros) 3.  0011110100: 0, 0, 0, 0, 0 (5 zeros) 4.  1100011000: 0, 0, 0, 0, 0, 0 (6 zeros) 5.  1101110100: 0, 0, 0, 0 (4 zeros) 6.  1000011001: 0, 0, 0, 0, 0, 0 (6 zeros) 7.  1010111100: 0, 0, 0, 0 (4 zeros) 8.  0011111101: 0, 0, 0 (3 zeros) 9.  0100110000: 0, 0, 0, 0, 0, 0 (6 zeros) 10. 0110010111: 0, 0, 0, 0 (4 zeros) 11. 11011 | No | 7.68 |
| 8 | 70 | 70 | Yes | 8.49 |
| 9 | 74 | To count the zeros in the provided text, we examine each line individually:  1.  1111100000: 5 zeros 2.  1101010110: 4 zeros 3.  1010110001: 5 zeros 4.  1011000 | No | 17.83 |
| 10 | 37 | 35 | No | 7.78 |
| 11 | 52 | 52 | Yes | 9.44 |
| 12 | 67 | 67 | Yes | 8.99 |
| 13 | 71 | 69 | No | 4.53 |
| 14 | 63 | 63 | Yes | 8.78 |
| 15 | 64 | 63 | No | 5.41 |
| 16 | 35 | 35 | Yes | 5.29 |
| 17 | 56 | 56 | Yes | 5.95 |
| 18 | 44 | 44 | Yes | 9.61 |
| 19 | 53 | To count the total number of zeros in the provided text:  1.  0100110011: 6 zeros 2.  0010110111: 4 zeros 3.  1010111100: 4 zeros 4.  110111100 | No | 7.6 |
| 20 | 45 | 45 | Yes | 8.32 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KHQDCJB | KHQDCJB | Yes | 5.65 |
| 2 | FXBUASN | FXBUASN | Yes | 11.23 |
| 3 | RCSKENH | RCSKENH | Yes | 7.66 |
| 4 | UOJKCQZ | UOJKCQZ | Yes | 10.73 |
| 5 | HMEXFJQ | HMEXFJQ | Yes | 7.25 |
| 6 | GBIRTNA | GBIRTNA | Yes | 9.32 |
| 7 | RIBDCUJ | RIBDCUJ | Yes | 4.43 |
| 8 | LUMZQAJ | LUMZQAJ | Yes | 10.32 |
| 9 | UHOZKDS | UHOZKDS | Yes | 3.18 |
| 10 | JKCAFSO | JKCAFSO | Yes | 11.53 |
| 11 | CXQSDWA | CXQSDWA | Yes | 3.37 |
| 12 | TGZMFOR | TGZMFOR | Yes | 2.01 |
| 13 | QEMXRAU | QEMXRAU | Yes | 4.91 |
| 14 | NROWXPK | NROWXPK | Yes | 5.43 |
| 15 | HLONQUG | HLONQUG | Yes | 3.0 |
| 16 | CZPHGVX | CZPHGVX | Yes | 1.75 |
| 17 | EXTZWQD | EXTZWQD | Yes | 12.91 |
| 18 | NGHIQJE | NGHIQJE | Yes | 4.84 |
| 19 | GNLPCEK | GNLPCEK | Yes | 11.79 |
| 20 | IJEPYDR | IJEPYDR | Yes | 20.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.0 |
| 2 | [3.7, 6.3] | 3.7 6.3 | Yes | 2.58 |
| 3 | [2.2, 7.8] | 2.2 7.8 | Yes | 13.86 |
| 4 | [4.4, 5.6] | 4.4 5.6 | Yes | 7.09 |
| 5 | [3.0, 7.0] | 3.0 7.0 | Yes | 12.77 |
| 6 | [0.9, 9.1] | 0.9 9.1 | Yes | 3.97 |
| 7 | [3.6, 6.4] | 3.6 6.4 | Yes | 3.57 |
| 8 | [0.9, 9.1] | 0.9 9.1 | Yes | 14.32 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 3.69 |
| 10 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.24 |
| 11 | [4.2, 5.8] | 4.2 5.8 | Yes | 4.37 |
| 12 | [3.4, 6.6] | 3.4 6.6 | Yes | 15.4 |
| 13 | [4.7, 5.3] | 4.7 5.3 | Yes | 3.82 |
| 14 | [4.4, 5.6] | 5.6 4.4 | Yes | 3.38 |
| 15 | [4.7, 5.3] | 4.7 5.3 | Yes | 2.0 |
| 16 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.25 |
| 17 | [1.2, 8.8] | 8.8 1.2 | Yes | 4.26 |
| 18 | [2.9, 7.1] | 7.1 2.9 | Yes | 3.13 |
| 19 | [4.6, 5.4] | 5.4 4.6 | Yes | 4.68 |
| 20 | [3.9, 6.1] | 3.9 6.1 | Yes | 2.04 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | P5XN1AM9Y5MR | P5XN1AM9Y5MR | Yes | 1.79 |
| 2 | G2930VFYSG1B | G2930VFYSG1B | Yes | 2.02 |
| 3 | IFUCK9Q4CGYJ | IFUCK9Q4CGYJ | Yes | 2.93 |
| 4 | YUHB3ALN7EYO | YUHB3ALN7EYO | Yes | 1.69 |
| 5 | MQV8CRHI9CN6 | MQV8CRHI9CN6 | Yes | 11.88 |
| 6 | BSQCXZDNXCK3 | BSQCXZDNXCK3 | Yes | 2.2 |
| 7 | JF30USWK7UE2 | JF30USWK7UE2 | Yes | 4.07 |
| 8 | DM94A4BI6DKT | DM94A4BI6DKT | Yes | 2.08 |
| 9 | 05OAXUIQELTN | 05OAXUIQELTN | Yes | 4.79 |
| 10 | E0FFC384ZT1T | E0FFC384ZT1T | Yes | 1.86 |
| 11 | QPD3U83XSK5J | QPD3U83XSK5J | Yes | 22.14 |
| 12 | 0347OCXMEE4B | 0347OCXMEE4B | Yes | 9.17 |
| 13 | 150AR9PTAKT8 | 150AR9PTAKT8 | Yes | 4.4 |
| 14 | LYQVD4F1WEC9 | LYQVD4F1WEC9 | Yes | 2.87 |
| 15 | BX1BJRVBXNEO | BX1BJRVBXNEO | Yes | 1.91 |
| 16 | SJRUS8W4E5HT | SJRUS8W4E5HT | Yes | 2.16 |
| 17 | 3PSZ52UDRXN8 | 3PSZ52UDRXN8 | Yes | 1.79 |
| 18 | U1R4J1FX5CTX | U1R4J1FX5CTX | Yes | 1.71 |
| 19 | 0TH2G6YODPB6 | 0TH2G6YODPB6 | Yes | 7.81 |
| 20 | HXBD9UEASMWW | HXBD9UEASMWW | Yes | 9.51 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 26 | 26 | Yes | 3.51 |
| 2 | 4 | 4 | Yes | 1.91 |
| 3 | 44 | 44 | Yes | 2.67 |
| 4 | 793 | 793 | Yes | 1.43 |
| 5 | 6 | 6 | Yes | 4.32 |
| 6 | 36 | 36 | Yes | 2.0 |
| 7 | 3 | 3 | Yes | 3.7 |
| 8 | 67 | 67 | Yes | 2.2 |
| 9 | 19 | 19 | Yes | 2.56 |
| 10 | 39 | 39 | Yes | 2.03 |
| 11 | 7 | 7 | Yes | 3.19 |
| 12 | 1 | 1 | Yes | 2.06 |
| 13 | 64 | 64 | Yes | 3.94 |
| 14 | 65 | 65 | Yes | 2.8 |
| 15 | 73 | 73 | Yes | 2.68 |
| 16 | 198 | 198 | Yes | 2.15 |
| 17 | 243 | 243 | Yes | 11.92 |
| 18 | 9 | 9 | Yes | 1.93 |
| 19 | 7680 | 7680 | Yes | 2.1 |
| 20 | 5 | 18 | No | 8.0 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (_<   )() | (_<   )() | Yes | 1.6 |
| 2 | <)_(_(< ( | <)_(_(< ( | Yes | 13.59 |
| 3 | \/\ / _)( | \/ / _< | No | 3.85 |
| 4 | __ \(\/(< | __ \(\/(< | Yes | 3.78 |
| 5 | ()\<()(<  | ()\<()(< | No | 4.5 |
| 6 | /)(\)/(<_ | /)(\)/(<_ | Yes | 16.52 |
| 7 | (/\ /\__) | (/ /\__) | No | 5.27 |
| 8 |  < _ <\<\ | < _ <<\ | No | 11.37 |
| 9 | (<__)<(\( | (<__)<(\( | Yes | 6.79 |
| 10 | <<_<)\\// | <<_<)\\// | Yes | 6.4 |
| 11 | /_ //\ << | /_ //\ << | Yes | 4.64 |
| 12 | <)\<\__/_ | <)\<\__/_<) | No | 8.6 |
| 13 |  <<( \ )/ | << (\ )/ | No | 6.43 |
| 14 | <__\(<\<_ | <__\(<\<_ | Yes | 5.12 |
| 15 | /\)\)<) _ | /\)\)<) _< | No | 5.09 |
| 16 | _/ )_<__< | _/ )<_<__< | No | 4.75 |
| 17 | (/ /\\)<( | (/ /\)<( | Yes | 4.93 |
| 18 | (<_)<_//  | (<_)<_// | No | 3.6 |
| 19 | /\\/\_< ( | /\\/\_< ( | Yes | 5.07 |
| 20 | <<() ((_/ | <<() ((_/ | Yes | 4.53 |
