# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
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
| sudoku_game | 8600 | 37592 | 46192 | 14 | 6 | 24.48 | 489.84 |
| add_numbers | 4520 | 4446 | 8966 | 20 | 0 | 4.59 | 91.92 |
| counting_zeros | 7460 | 31328 | 38788 | 11 | 9 | 16.25 | 325.41 |
| task_decoding | 13900 | 6039 | 19939 | 20 | 0 | 5.58 | 111.73 |
| task_summation | 7820 | 14932 | 22752 | 20 | 0 | 10.31 | 206.46 |
| task_transcription | 4668 | 3747 | 8415 | 19 | 1 | 4.24 | 84.97 |
| task_sequences | 3781 | 9547 | 13328 | 19 | 1 | 7.35 | 147.04 |
| **TOTAL** | **50749** | **107631** | **158380** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 4 2 5 2 5 1 2 3 6 6 4 1 | 3 6 4 2 5 2 5 1 2 3 6 6 4 1 | Yes | 20.85 |
| 2 | 1 3 6 1 2 2 5 3 1 3 6 6 5 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row-by-row analysis:**  **Row 1:** Has 5,4,2 → needs 1,3,6 **Row 2:** Has 3,6,5,4 → needs 1,2 **Row 3:** Has 6,4,1 → needs 2,3,5 **Row 4:** Has 4,2,5 → needs 1,3,6 **Row 5:** Complete **Row 6:** Has 4,2,3 → needs 1,5,6  **Solving step by step:**  - Column 5 missing only 6 → Row 4, Col 5 = **6** - Column 2 needs 1,3; Row 2 needs 1,2 → Row 2, Col 2 = **1** - Row 2, Col 3 = **2** (only number left for row 2) - Column 2 now needs only 3 → Row 4, Col 2 = **3** - Row 4, Col 1 = **1** (only number left for row 4) - Column 1 needs 2 → Row 3, Col 1 = **2** - Row 3: needs 3,5 for cols 3,6. Col 3 needs 1,5,6 → Row 3, Col 3 = **5 | No | 27.25 |
| 3 | 3 4 1 4 6 3 6 5 1 4 3 3 2 4 | 3 4 1 4 6 3 6 5 1 4 3 3 2 4 | Yes | 21.53 |
| 4 | 1 5 3 4 5 6 6 1 1 6 1 4 6 3 |  | No | 28.64 |
| 5 | 3 2 4 3 4 4 3 2 6 1 5 6 2 1 | 3 2 4 3 4 4 3 2 6 1 5 6 2 1 | Yes | 25.21 |
| 6 | 5 6 6 2 3 6 4 3 1 4 3 2 5 3 |  | No | 23.53 |
| 7 | 3 1 2 6 4 5 3 1 5 4 6 1 2 5 | 3 1 2 6 4 5 3 1 5 4 6 1 2 5 | Yes | 23.47 |
| 8 | 4 2 5 5 1 6 2 5 2 4 3 4 6 1 | 4 2 5 5 1 6 2 5 2 4 3 4 6 1 | Yes | 25.55 |
| 9 | 2 5 3 2 5 4 2 6 6 1 3 2 3 1 | 2 5 3 2 5 4 2 6 6 1 3 2 3 1 | Yes | 19.75 |
| 10 | 2 6 1 1 6 2 5 5 3 1 2 6 6 5 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 3 and Row 4 analysis:** - Row 3 is complete: 6, 2, 1, 5, 3, 4 - Row 4 has 2, | No | 27.46 |
| 11 | 5 3 1 6 4 2 1 5 1 5 2 5 6 4 | 5 3 1 6 4 2 1 5 1 5 2 5 6 4 | Yes | 23.51 |
| 12 | 1 4 4 3 5 3 1 4 6 1 2 5 4 3 | 1 4 4 3 5 3 1 4 6 1 2 5 4 3 | Yes | 21.76 |
| 13 | 6 2 4 4 6 5 2 5 6 1 5 4 2 4 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row-by-row analysis:**  **Row 1:** Has 1, 5, 3. Missing: 2, 4, 6 **Row 2:** Has 5, 1, 3, 2. Missing: 4, 6 **Row 3:** Has 2, 3, 6, 4, 1. Missing: 5 **Row 4:** Has 3, 4. Missing: 1, 2, 5, 6 **Row 5:** Has 3, 1, 6. Missing: 2, 4, 5 **Row 6:** Has 6, 1, 2, 5, 3. Missing: 4  **Solving step by step:**  - Row 3, Col 6: Must be **5** - Row 6, Col 3: Must be **4** - Row 4, Col 4: Column 4 needs 6, so **6** - Row 2, Col 1: Column 1 needs 4 or 5, Row 2 needs 4 or 6 → **4** - Row 2, Col 6: Row 2 now needs **6** - Row 5, Col 1: Column 1 needs **5** - Row 1, Col 2: Checking box and column → **6** - Row 1, Col 3: Must be **2** - Row 1, Col 6: Must be **4** - Row 4, Col 2: Must be **2** - Row 4, Col 3: Must be **5** - Row 4, Col 6: Must be **1** - Row 5, Col 2: Must be **4** | No | 28.86 |
| 14 | 4 3 2 6 3 5 4 6 1 5 3 4 5 6 | 4 3 2 6 3 5 4 6 1 5 3 4 5 6 | Yes | 18.8 |
| 15 | 1 4 3 5 2 5 4 3 1 5 6 2 3 1 | 1 4 3 5 2 5 4 3 1 5 6 2 3 1 | Yes | 26.11 |
| 16 | 1 5 3 6 1 5 5 2 6 1 3 6 3 4 | 1 5 3 6 1 5 5 2 6 1 3 6 3 4 | Yes | 23.24 |
| 17 | 2 1 6 6 4 5 3 5 4 5 1 2 4 5 |  | No | 27.43 |
| 18 | 5 6 4 2 6 2 6 3 5 5 2 6 5 1 | 5 6 4 2 6 2 6 3 5 5 2 6 5 1 | Yes | 26.28 |
| 19 | 4 3 4 3 5 6 2 3 6 6 5 1 5 2 | 4 3 4 3 5 6 2 3 6 6 5 1 5 2 | Yes | 25.76 |
| 20 | 6 3 5 6 1 3 5 3 6 1 3 6 1 4 | 6 3 5 6 1 3 5 3 6 1 3 6 1 4 | Yes | 24.66 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1900 | 1900 | Yes | 4.82 |
| 2 | 1023 | 1023 | Yes | 3.73 |
| 3 | 2233 | 2233 | Yes | 3.59 |
| 4 | 1885 | 1885 | Yes | 3.42 |
| 5 | 1391 | 1391 | Yes | 4.54 |
| 6 | 2091 | 2091 | Yes | 5.06 |
| 7 | 1952 | 1952 | Yes | 5.23 |
| 8 | 1573 | 1573 | Yes | 3.83 |
| 9 | 2441 | 2441 | Yes | 4.87 |
| 10 | 1555 | 1555 | Yes | 4.86 |
| 11 | 1466 | 1466 | Yes | 4.75 |
| 12 | 2223 | 2223 | Yes | 4.88 |
| 13 | 1904 | 1904 | Yes | 4.68 |
| 14 | 2330 | 2330 | Yes | 4.91 |
| 15 | 2601 | 2601 | Yes | 6.24 |
| 16 | 1554 | 1554 | Yes | 4.38 |
| 17 | 925 | 925 | Yes | 4.12 |
| 18 | 1708 | 1708 | Yes | 5.26 |
| 19 | 1728 | 1728 | Yes | 4.99 |
| 20 | 1146 | 1146 | Yes | 3.65 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 48 | No | 11.67 |
| 2 | 53 | 54 | No | 12.95 |
| 3 | 52 | 53 | No | 14.77 |
| 4 | 67 | 67 | Yes | 11.23 |
| 5 | 51 | 51 | Yes | 16.15 |
| 6 | 39 | 39 | Yes | 20.31 |
| 7 | 75 | 75 | Yes | 17.69 |
| 8 | 73 | 73 | Yes | 15.22 |
| 9 | 36 | 36 | Yes | 17.22 |
| 10 | 62 | 64 | No | 20.96 |
| 11 | 51 | 51 | Yes | 14.62 |
| 12 | 66 | 63 | No | 10.86 |
| 13 | 57 | 56 | No | 14.8 |
| 14 | 44 | 44 | Yes | 16.47 |
| 15 | 35 | 35 | Yes | 20.58 |
| 16 | 75 | 75 | Yes | 17.53 |
| 17 | 52 | Looking at the image, I'll count the zeros row by row:  Row 1: 1 0 0 1 1 1 1 0 1 1 → 3 zeros Row 2: 0 0 0 1 1 1 1 0 1 0 → 5 zeros Row 3: 1 1 1 1 0 1 1 1 0 1 → 2 zeros Row 4: 1 0 1 1 0 1 0 1 1 1 → 3 zeros Row 5: 1 1 1 0 1 1 1 1 1 1 → 1 zero Row 6: 1 1 1 1 1 0 1 0 0 1 → 3 zeros Row 7: 0 0 1 1 1 1 0 1 0 1 → 4 zeros Row 8: 1 1 1 1 0 1 0 1 1 0 → 3 zeros Row 9: 0 0 0 1 0 1 1 0 1 1 → 5 zeros Row 10: 1 1 0 1 0 0 1 1 1 1 → 3 zeros Row 11: 1 0 1 1 1 1 1 0 0 0 1 → 4 zeros Row 12: 0 1 0 1 1 0 1 1 1 1 → 3 zeros Row 13: 0 | No | 21.28 |
| 18 | 37 | 37 | Yes | 16.52 |
| 19 | 66 | 67 | No | 13.02 |
| 20 | 51 | Looking at the image, I'll count the zeros in each row:  Row 1: 0 1 0 1 1 1 0 0 1 0 → 5 zeros Row 2: 0 1 1 1 1 1 1 0 1 0 → 3 zeros Row 3: 0 1 0 1 1 0 1 0 0 1 → 5 zeros Row 4: 0 1 0 1 1 1 1 1 1 1 → 2 zeros Row 5: 1 0 0 0 1 1 1 0 1 1 0 → 5 zeros Row 6: 1 0 1 0 1 0 1 1 1 1 → 3 zeros Row 7: 1 1 1 1 1 0 0 1 1 1 → 2 zeros Row 8: 0 1 0 1 1 1 1 0 1 1 → 3 zeros Row 9: 1 1 0 0 0 1 1 1 0 1 → 4 zeros Row 10: 0 1 0 1 1 1 0 1 1 0 → 4 zeros Row 11: 1 0 1 1 1 1 1 1 1 1 → 1 zero Row 12: 1 1 1 0 1 1 1 1 1 1 → 1 zero Row 13: 0 1 0 0 0 0 1 0 0 1 | No | 21.21 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AXETJMC | AXETJMC | Yes | 6.65 |
| 2 | QPDZKCM | QPDZKCM | Yes | 10.48 |
| 3 | TOAGFQR | TOAGFQR | Yes | 6.19 |
| 4 | LXWNQDR | LXWNQDR | Yes | 4.71 |
| 5 | OJHIWDL | OJHIWDL | Yes | 5.51 |
| 6 | HPDTVES | HPDTVES | Yes | 6.28 |
| 7 | LFZRKGB | LFZRKGB | Yes | 4.68 |
| 8 | HFPGJTR | HFPGJTR | Yes | 4.93 |
| 9 | PCHGUMF | PCHGUMF | Yes | 5.77 |
| 10 | EKYCFLW | EKYCFLW | Yes | 7.15 |
| 11 | DAKVJBR | DAKVJBR | Yes | 5.12 |
| 12 | AKLHUZG | AKLHUZG | Yes | 4.87 |
| 13 | OKLEPWJ | OKLEPWJ | Yes | 5.11 |
| 14 | FDXVZPR | FDXVZPR | Yes | 4.91 |
| 15 | XNQTMJV | XNQTMJV | Yes | 4.59 |
| 16 | UBMIWKN | UBMIWKN | Yes | 4.91 |
| 17 | YNTPDGU | YNTPDGU | Yes | 5.43 |
| 18 | CVZMWUI | CVZMWUI | Yes | 4.73 |
| 19 | VJFRCET | VJFRCET | Yes | 5.28 |
| 20 | QUYVFTP | QUYVFTP | Yes | 4.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 9.4 0.6 | Yes | 7.91 |
| 2 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.2 |
| 3 | [2.1, 7.9] | 2.1 7.9 | Yes | 8.71 |
| 4 | [2.7, 7.3] | 2.7 7.3 | Yes | 11.42 |
| 5 | [4.0, 6.0] | 6.0 4.0 | Yes | 9.89 |
| 6 | [0.1, 9.9] | 0.1 9.9 | Yes | 7.85 |
| 7 | [1.5, 8.5] | 8.5 1.5 | Yes | 11.15 |
| 8 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.89 |
| 9 | [1.1, 8.9] | 8.9 1.1 | Yes | 14.29 |
| 10 | [3.8, 6.2] | 3.8 6.2 | Yes | 11.2 |
| 11 | [4.8, 5.2] | 4.8 5.2 | Yes | 11.26 |
| 12 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.82 |
| 13 | [3.0, 7.0] | 7.0 3.0 | Yes | 9.21 |
| 14 | [1.5, 8.5] | 1.5 8.5 | Yes | 9.98 |
| 15 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.85 |
| 16 | [4.5, 5.5] | 4.5 5.5 | Yes | 11.16 |
| 17 | [1.7, 8.3] | 1.7 8.3 | Yes | 13.55 |
| 18 | [3.3, 6.7] | 3.3 6.7 | Yes | 10.05 |
| 19 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.67 |
| 20 | [3.4, 6.6] | 3.4 6.6 | Yes | 11.21 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 941G171CSYFX | 941G171CSYFX | Yes | 4.15 |
| 2 | FZ5EB67TNKRP | FZ5EB67TNKRP | Yes | 3.82 |
| 3 | QDWD38L84QY0 | QDWD38L84QY0 | Yes | 4.92 |
| 4 | T1RJD6TNJU7F | T1RJD6TNJU7F | Yes | 3.22 |
| 5 | 6JN9GDBW5U8K | 6JN9GDBW5U8K | Yes | 4.84 |
| 6 | EECNDI5FFNQ4 | EECNDI5FFNQ4 | Yes | 3.8 |
| 7 | 7Y9AQS46NPZI | 7Y9AQS46NPZI | Yes | 4.16 |
| 8 | 9AF5K52YJ4BM | 9AF5K52YJ4BM | Yes | 4.55 |
| 9 | NBJ8BYL96XIV | NBJ8BYL9GXIV | No | 3.47 |
| 10 | HH4XQE4VYNUT | HH4XQE4VYNUT | Yes | 4.04 |
| 11 | 3LTXY7R3MOEJ | 3LTXY7R3MOEJ | Yes | 5.65 |
| 12 | DUG8QSF5AOP8 | DUG8QSF5AOP8 | Yes | 4.31 |
| 13 | RUU0BG2IB054 | RUU0BG2IB054 | Yes | 5.68 |
| 14 | A6KCI2LIOMW2 | A6KCI2LIOMW2 | Yes | 3.94 |
| 15 | ID4OOCC0HBKQ | ID4OOCC0HBKQ | Yes | 4.18 |
| 16 | WSWGD5RAE72U | WSWGD5RAE72U | Yes | 4.53 |
| 17 | VSZGO7IDPMEP | VSZGO7IDPMEP | Yes | 3.55 |
| 18 | 40BBXVOX1YER | 40BBXVOX1YER | Yes | 4.37 |
| 19 | E3FPTV4MU5T9 | E3FPTV4MU5T9 | Yes | 3.55 |
| 20 | V9NCVBH32WTH | V9NCVBH32WTH | Yes | 4.13 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 3.8 |
| 2 | 44 | 44 | Yes | 5.75 |
| 3 | 65 | 65 | Yes | 8.13 |
| 4 | 5 | 8 | No | 18.8 |
| 5 | 7 | 7 | Yes | 4.38 |
| 6 | 28 | 28 | Yes | 4.5 |
| 7 | 9 | 9 | Yes | 5.32 |
| 8 | 63 | 63 | Yes | 3.94 |
| 9 | 23 | 23 | Yes | 4.2 |
| 10 | 10 | 10 | Yes | 8.4 |
| 11 | 1440 | 1440 | Yes | 5.08 |
| 12 | 73 | 73 | Yes | 4.64 |
| 13 | 198 | 198 | Yes | 4.52 |
| 14 | 26 | 26 | Yes | 12.02 |
| 15 | 4096 | 4096 | Yes | 14.14 |
| 16 | 31 | 31 | Yes | 4.36 |
| 17 | 1 | 1 | Yes | 4.48 |
| 18 | 3 | 3 | Yes | 5.14 |
| 19 | 3 | 3 | Yes | 19.69 |
| 20 | 5 | 5 | Yes | 5.77 |
