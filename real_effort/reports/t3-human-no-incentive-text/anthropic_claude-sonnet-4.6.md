# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-27 10:01:23

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
| sudoku_game | 6492 | 36052 | 42544 | 8 | 12 | 26.95 | 539.02 |
| add_numbers | 3860 | 944 | 4804 | 20 | 0 | 2.25 | 45.09 |
| counting_zeros | 5180 | 16039 | 21219 | 4 | 16 | 10.35 | 207.04 |
| task_decoding | 5180 | 2418 | 7598 | 16 | 4 | 3.72 | 74.34 |
| task_summation | 5240 | 3053 | 8293 | 20 | 0 | 3.95 | 78.94 |
| task_transcription | 4024 | 772 | 4796 | 20 | 0 | 1.78 | 35.6 |
| task_sequences | 3921 | 3144 | 7065 | 19 | 1 | 4.14 | 82.74 |
| string_entry | 4394 | 1437 | 5831 | 14 | 6 | 2.96 | 59.1 |
| **TOTAL** | **38291** | **63859** | **102150** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 4 5 4 2 1 6 1 5 1 3 2 5 |  | No | 35.87 |
| 2 | 3 6 1 5 5 6 1 6 5 2 1 2 6 5 |  | No | 31.9 |
| 3 | 2 1 2 5 4 2 1 2 5 4 3 2 5 6 | 2 1 2 5 4 2 1 2 5 3 2 5 6 | No | 24.66 |
| 4 | 2 5 5 6 2 6 2 1 3 5 4 6 4 2 | 2 5 5 6 2 6 2 1 3 5 4 6 4 2 | Yes | 26.61 |
| 5 | 4 3 6 1 2 4 1 3 3 6 4 2 4 4 | Looking at this 6×6 Sudoku puzzle:  ``` 5 . . \| . 2 . 1 3 2 \| 5 6 4 ------+------ . 6 . \| . 5 . . 5 . \| . 1 . ------+------ . 1 5 \| 2 3 6 6 2 1 \| 3 . 5 ```  **Row 1** (missing 1,3,4,6): - Top-left box (rows 1-2, cols 1-3) has {1,2,3,5} → needs 4,6 → R1C2=4, R1C3=6 - Top-right box (rows 1-2, cols 4-6) has {2,4,5,6} → needs 1,3 → Col4 already has 3 → R1C4=1, R1C6=3 - **Row 1: 5 4 6 1 2 3**  **Row 3** (missing 1,2,3,4): - Bottom-left box has {5,6} → needs 1,2,3,4 from cols 1,3 - Col4 can't have 1,2,3,5 → R3C4=4; Col3 can't have 1,2,5 → R3C3=3 - Col1 can't have 1,5,6 → R3C1=2; R3C6=1 - **Row 3: 2 6 3 4 5 1**  ** | No | 29.24 |
| 6 | 3 1 1 6 3 1 2 4 6 6 4 1 2 6 | 3 1 1 6 3 1 2 4 6 6 4 1 2 6 | Yes | 28.74 |
| 7 | 3 2 4 1 5 6 3 1 4 3 1 4 3 1 |  | No | 33.51 |
| 8 | 2 4 1 3 4 5 3 1 4 3 4 5 6 3 | 2 4 1 3 4 5 3 1 4 3 4 5 6 3 | Yes | 18.21 |
| 9 | 6 3 4 3 2 1 6 2 1 6 2 3 2 1 | 6 3 4 3 2 1 6 2 1 6 2 3 2 1 | Yes | 17.99 |
| 10 | 4 6 3 1 2 4 6 6 6 2 3 2 5 6 |  | No | 33.24 |
| 11 | 1 2 3 1 5 3 1 2 3 5 2 6 6 3 | 1 2 3 1 5 3 1 2 3 5 2 6 6 3 | Yes | 13.47 |
| 12 | 1 2 6 3 5 5 6 3 1 2 6 4 6 5 | 1 2 6 3 5 5 6 3 1 2 6 4 6 5 | Yes | 15.35 |
| 13 | 6 4 1 6 6 1 3 4 5 1 4 5 3 1 |  | No | 34.58 |
| 14 | 6 2 5 2 5 1 5 2 1 4 6 6 2 5 |  | No | 28.8 |
| 15 | 6 1 4 6 5 4 6 3 1 2 5 5 2 3 |  | No | 31.48 |
| 16 | 4 3 1 2 6 5 4 1 1 6 1 4 5 2 |  | No | 31.74 |
| 17 | 3 1 2 5 5 3 6 1 3 5 1 1 6 2 | 3 1 2 5 5 3 6 1 3 5 1 1 4 6 2 | No | 20.2 |
| 18 | 3 2 4 1 6 2 6 1 1 6 4 3 5 2 | 3 2 4 1 6 2 6 1 1 6 4 3 5 2 | Yes | 28.11 |
| 19 | 5 4 6 1 3 1 6 1 3 5 4 5 6 4 | 5 4 6 1 3 1 6 1 3 5 4 5 6 4 | Yes | 22.21 |
| 20 | 1 2 4 6 3 4 4 5 6 2 4 3 5 2 |  | No | 33.08 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2297 | 2297 | Yes | 1.81 |
| 2 | 1688 | 1688 | Yes | 1.9 |
| 3 | 2043 | 2043 | Yes | 1.39 |
| 4 | 2289 | 2289 | Yes | 1.77 |
| 5 | 1839 | 1839 | Yes | 1.8 |
| 6 | 1408 | 1408 | Yes | 1.18 |
| 7 | 1701 | 1701 | Yes | 1.86 |
| 8 | 1895 | 1895 | Yes | 1.43 |
| 9 | 2060 | 2060 | Yes | 1.3 |
| 10 | 1835 | 1835 | Yes | 1.82 |
| 11 | 1476 | 1476 | Yes | 3.63 |
| 12 | 1387 | 1387 | Yes | 1.96 |
| 13 | 1541 | 1541 | Yes | 1.49 |
| 14 | 1918 | 1918 | Yes | 2.94 |
| 15 | 1102 | 1102 | Yes | 4.05 |
| 16 | 1603 | 1603 | Yes | 2.59 |
| 17 | 1844 | 1844 | Yes | 3.59 |
| 18 | 807 | 807 | Yes | 2.2 |
| 19 | 1136 | 1136 | Yes | 2.74 |
| 20 | 664 | 664 | Yes | 3.62 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53 | 49 | No | 13.29 |
| 2 | 71 | 63 | No | 9.29 |
| 3 | 64 | 65 | No | 9.69 |
| 4 | 45 | 45 | Yes | 7.86 |
| 5 | 38 | 36 | No | 8.42 |
| 6 | 52 | 46 | No | 14.9 |
| 7 | 41 | 40 | No | 9.34 |
| 8 | 67 | 63 | No | 8.36 |
| 9 | 43 | 43 | Yes | 11.96 |
| 10 | 73 | 67 | No | 7.86 |
| 11 | 54 | 53 | No | 8.68 |
| 12 | 74 | 67 | No | 9.15 |
| 13 | 45 | 45 | Yes | 19.6 |
| 14 | 62 | 61 | No | 7.53 |
| 15 | 74 | 69 | No | 9.64 |
| 16 | 63 | 63 | Yes | 16.9 |
| 17 | 41 | 37 | No | 4.84 |
| 18 | 70 | 62 | No | 14.47 |
| 19 | 42 | 40 | No | 6.68 |
| 20 | 73 | 64 | No | 8.56 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HDTWIBL | HDTWIBL | Yes | 3.1 |
| 2 | QWNGCJO | QWNGCJO | Yes | 3.55 |
| 3 | ZEJIPOR | ZEJIPOR | Yes | 3.85 |
| 4 | BZSTGHV | BZSTHGV | No | 4.9 |
| 5 | CSJVBLN | CSVJBLN | No | 4.38 |
| 6 | EVZNKBJ | EVZNKBJ | Yes | 2.66 |
| 7 | XPWQGKS | XPWQGKS | Yes | 7.18 |
| 8 | OYHKAMJ | OYHKAMJ | Yes | 3.89 |
| 9 | HINOXSQ | HINOXSQ | Yes | 3.72 |
| 10 | JYNQTBP | JYNQTBP | Yes | 3.03 |
| 11 | OAJIUVS | OAJIVUS | No | 2.69 |
| 12 | MBGXHAU | MBGXHAU | Yes | 2.79 |
| 13 | QUXTPHG | QUXTPHG | Yes | 5.46 |
| 14 | YLWBGUH | YLWBGUH | Yes | 2.46 |
| 15 | WZJFSOY | WZJFSOY | Yes | 4.15 |
| 16 | CDSMPKB | CDSMKPB | No | 2.64 |
| 17 | STYQIBX | STYQIBX | Yes | 2.27 |
| 18 | DZIGLRH | DZIGLRH | Yes | 5.01 |
| 19 | XCWBOFY | XCWBOFY | Yes | 2.99 |
| 20 | VSBPMYX | VSBPMYX | Yes | 3.63 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 9.4 0.6 | Yes | 3.39 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 2.64 |
| 3 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.94 |
| 4 | [0.8, 9.2] | 0.8 9.2 | Yes | 4.09 |
| 5 | [3.8, 6.2] | 3.8 6.2 | Yes | 3.54 |
| 6 | [4.2, 5.8] | 5.8 4.2 | Yes | 2.78 |
| 7 | [4.1, 5.9] | 5.9 4.1 | Yes | 3.13 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 4.09 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 2.84 |
| 10 | [3.9, 6.1] | 6.1 3.9 | Yes | 3.22 |
| 11 | [2.1, 7.9] | 2.1 7.9 | Yes | 3.3 |
| 12 | [0.4, 9.6] | 0.4 9.6 | Yes | 4.2 |
| 13 | [4.7, 5.3] | 4.7 5.3 | Yes | 3.32 |
| 14 | [0.2, 9.8] | 9.8 0.2 | Yes | 2.58 |
| 15 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.18 |
| 16 | [1.7, 8.3] | 8.3 1.7 | Yes | 2.7 |
| 17 | [1.7, 8.3] | 8.3 1.7 | Yes | 7.02 |
| 18 | [3.8, 6.2] | 3.8 6.2 | Yes | 4.41 |
| 19 | [1.8, 8.2] | 8.2 1.8 | Yes | 3.1 |
| 20 | [0.3, 9.7] | 0.3 9.7 | Yes | 6.46 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WH2YPJRMA5O0 | WH2YPJRMA5O0 | Yes | 1.58 |
| 2 | 8DFXB042D0P4 | 8DFXB042D0P4 | Yes | 1.63 |
| 3 | CJTXTN8NFRV9 | CJTXTN8NFRV9 | Yes | 1.8 |
| 4 | P6GNDR6MRDN4 | P6GNDR6MRDN4 | Yes | 1.69 |
| 5 | ZH6J9SESJ16R | ZH6J9SESJ16R | Yes | 1.08 |
| 6 | GO1O7QU4L6SM | GO1O7QU4L6SM | Yes | 1.62 |
| 7 | 82QF0BXCSWJ5 | 82QF0BXCSWJ5 | Yes | 1.63 |
| 8 | XJZX3P17E5OG | XJZX3P17E5OG | Yes | 2.32 |
| 9 | 6ZNRBPKDE34R | 6ZNRBPKDE34R | Yes | 1.61 |
| 10 | 513J2H7IQI3O | 513J2H7IQI3O | Yes | 2.44 |
| 11 | 0G3GTEJNUMJ0 | 0G3GTEJNUMJ0 | Yes | 1.04 |
| 12 | VYK4N3GCMJWM | VYK4N3GCMJWM | Yes | 1.93 |
| 13 | M0A5BBAGQ9K0 | M0A5BBAGQ9K0 | Yes | 1.83 |
| 14 | A961KBQ8MF3Q | A961KBQ8MF3Q | Yes | 2.18 |
| 15 | DYQ753A0MMXH | DYQ753A0MMXH | Yes | 2.49 |
| 16 | Q78W8IS0MABI | Q78W8IS0MABI | Yes | 1.8 |
| 17 | YKAYUE2S8X4R | YKAYUE2S8X4R | Yes | 1.64 |
| 18 | F9QW605BHNFT | F9QW605BHNFT | Yes | 2.23 |
| 19 | BZKYDMVORPCP | BZKYDMVORPCP | Yes | 1.07 |
| 20 | SM49RJY53VYY | SM49RJY53VYY | Yes | 1.99 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 4.51 |
| 2 | 39 | 39 | Yes | 3.44 |
| 3 | 5 | 5 | Yes | 3.04 |
| 4 | 16 | 16 | Yes | 3.78 |
| 5 | 48 | 48 | Yes | 4.22 |
| 6 | 28 | 28 | Yes | 1.7 |
| 7 | 6 | 6 | Yes | 2.19 |
| 8 | 7 | 7 | Yes | 2.49 |
| 9 | 3 | 3 | Yes | 3.24 |
| 10 | 36 | 36 | Yes | 1.77 |
| 11 | 63 | 63 | Yes | 10.17 |
| 12 | 60 | 60 | Yes | 4.69 |
| 13 | 31 | 31 | Yes | 2.75 |
| 14 | 198 | 198 | Yes | 2.45 |
| 15 | 20 | 20 | Yes | 7.47 |
| 16 | 4096 | 1048576 | No | 13.06 |
| 17 | 10 | 10 | Yes | 2.88 |
| 18 | 4 | 4 | Yes | 3.16 |
| 19 | 9 | 9 | Yes | 2.7 |
| 20 | 44 | 44 | Yes | 3.04 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /\\\_(( < | /\\\_(( | No | 1.52 |
| 2 |  _ < / \  | _ < / \ | No | 2.5 |
| 3 | /) ()(  / | /) ()(  / | Yes | 3.92 |
| 4 | \))(\)\\  | \))(\)\\ | No | 2.29 |
| 5 | \_/< ( </ | \_/< ( </ | Yes | 1.74 |
| 6 | __)<_<//\ | __)<_<//\ | Yes | 2.57 |
| 7 | /  /)\_(( | /  /)\_(( | Yes | 2.61 |
| 8 | <)()/)\() | <)()/)\() | Yes | 2.86 |
| 9 | _  /))( / | _  /))( / | Yes | 4.33 |
| 10 | <(</\/)<\ | <(</\/)<\ | Yes | 2.64 |
| 11 | \((()_)_/ | \((()_)_/ | Yes | 3.32 |
| 12 | \)_ )) \_ | \)_ )) \_ | Yes | 2.96 |
| 13 | < \/(_))) | < \/(_))) | Yes | 3.3 |
| 14 | ())__\(\  | ())__\(\ | No | 2.83 |
| 15 | \\_/\(<(< | \\_/\(<( | No | 3.67 |
| 16 | _ /<)\))/ | _ /<)\))/ | Yes | 2.76 |
| 17 | (</ _  \< | (</ _ \ | No | 2.95 |
| 18 | <)_)/)\</ | <)_)/)\</ | Yes | 4.07 |
| 19 | /) < (_\_ | /) < (_\_ | Yes | 2.37 |
| 20 | _\\(//(_) | _\\(//(_) | Yes | 3.89 |
