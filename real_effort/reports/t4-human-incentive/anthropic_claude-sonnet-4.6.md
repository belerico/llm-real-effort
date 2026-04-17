# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 8512 | 33165 | 41677 | 10 | 10 | 31.80 | 636.22 |
| add_numbers | 4880 | 712 | 5592 | 20 | 0 | 2.22 | 44.48 |
| counting_zeros | 7820 | 27294 | 35114 | 6 | 14 | 16.06 | 321.53 |
| task_decoding | 14260 | 5202 | 19462 | 20 | 0 | 5.35 | 107.25 |
| task_summation | 8180 | 3235 | 11415 | 20 | 0 | 3.51 | 70.29 |
| task_transcription | 5012 | 840 | 5852 | 20 | 0 | 2.19 | 43.84 |
| task_sequences | 4141 | 4211 | 8352 | 18 | 2 | 4.47 | 89.35 |
| **TOTAL** | **52805** | **74659** | **127464** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 6 6 1 4 2 3 4 4 5 3 6 1 | 4 3 6 6 1 4 2 3 4 4 5 3 6 1 | Yes | 20.59 |
| 2 | 4 1 2 6 4 5 3 4 6 6 3 4 2 1 | Looking at the puzzle systematically:  **Grid:** ``` 3  5  2  _  6  _ 4  _  1  _  3  5 1  6  5  3  2  _ _  _  _  2  1  _ _  1  _  5  _  _ 2  4  6  _  5  3 ```  **Solving step by step:**  - **Row 6** needs 1 → Col4,Row6 = **1** - **Row 1** needs {1,4}: Col4 gets **4** (Col4 now has 3,2,5,2,1→4 works); Col6 = **1** - **Row 2** needs {2,6}: Col2 needs {2,3} → **2**; Col4 = **6** - **Row 3** needs 4 → Col6,Row3 = **4** - **Row 5, Col5**: Col5 missing 4 → **4**; Row5,Col1=**6** (Col1 needs 5,6); Row5,Col3=**3**; Row5,Col6=**2** - **Row 4**: Col1=**5**, Col2=**3**, Col3=**4**, Col6=**6**  **Completed grid:** ``` 3  5  2  4  6  1 4  2  1  6  3  5 1  6  5  3  2  4 5  3  4  2  1 | No | 36.95 |
| 3 | 6 5 1 2 2 5 3 5 1 2 3 4 3 2 | 6 5 1 2 2 3 5 5 1 2 3 4 3 2 | No | 22.24 |
| 4 | 2 6 3 3 5 6 5 5 1 2 6 1 3 4 | Looking at the puzzle systematically:  **Grid layout:** ``` | No | 34.85 |
| 5 | 3 4 2 1 6 2 5 2 2 6 4 1 3 2 | 3 4 2 1 6 2 5 2 2 6 4 1 3 2 | Yes | 28.28 |
| 6 | 5 2 6 6 4 5 2 5 2 6 6 3 2 6 | 5 6 2 2 4 5 6 5 2 6 6 3 2 6 | No | 28.84 |
| 7 | 6 2 5 6 2 1 5 2 3 1 6 2 3 1 | 6 2 5 6 2 1 5 2 3 1 5 2 6 2 3 1 | No | 21.91 |
| 8 | 3 4 6 4 5 1 6 1 4 1 3 5 2 6 | 3 4 6 4 5 1 6 1 4 1 3 5 4 2 6 | No | 29.06 |
| 9 | 4 3 4 1 4 5 3 5 6 3 4 3 2 5 | 4 3 4 1 4 5 3 5 6 3 4 3 2 5 | Yes | 18.67 |
| 10 | 4 2 6 5 5 3 6 1 5 2 6 4 2 3 | 4 2 6 5 5 3 6 1 5 2 6 4 2 3 | Yes | 26.8 |
| 11 | 1 2 3 5 1 4 3 1 6 4 5 3 6 5 |  | No | 35.99 |
| 12 | 1 5 3 5 6 6 3 2 1 4 2 5 1 6 | 1 5 3 5 6 6 3 2 1 4 2 5 1 6 | Yes | 21.74 |
| 13 | 3 4 1 6 2 6 1 3 4 1 5 5 4 6 | 3 4 1 6 2 6 1 3 4 1 5 5 4 6 | Yes | 29.37 |
| 14 | 5 6 3 1 4 3 6 4 5 3 3 4 1 2 | TIMEOUT | No | 120.02 |
| 15 | 3 1 2 4 1 4 3 2 6 3 6 4 6 3 | Looking at the puzzle systematically: | No | 39.95 |
| 16 | 4 3 1 5 4 2 1 4 3 2 6 4 1 2 | 4 3 1 5 4 2 1 4 3 2 6 4 1 2 | Yes | 20.97 |
| 17 | 4 5 3 6 1 4 3 2 2 6 3 5 2 1 | 4 5 3 6 1 4 3 2 2 6 3 5 2 1 | Yes | 22.14 |
| 18 | 6 5 1 2 3 4 5 3 2 5 4 6 4 5 | 6 5 1 2 3 4 5 3 2 5 4 6 4 5 | Yes | 20.79 |
| 19 | 5 2 5 3 4 2 2 6 5 5 1 4 2 3 | 5 2 5 3 4 2 2 6 5 5 | No | 31.45 |
| 20 | 4 5 2 5 4 6 4 2 5 1 6 1 2 6 | 4 5 2 5 4 6 4 2 5 1 6 1 2 6 | Yes | 25.41 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1471 | 1471 | Yes | 2.91 |
| 2 | 1160 | 1160 | Yes | 2.26 |
| 3 | 567 | 567 | Yes | 2.17 |
| 4 | 1479 | 1479 | Yes | 1.79 |
| 5 | 808 | 808 | Yes | 2.26 |
| 6 | 1206 | 1206 | Yes | 3.1 |
| 7 | 1336 | 1336 | Yes | 2.0 |
| 8 | 1919 | 1919 | Yes | 1.88 |
| 9 | 1684 | 1684 | Yes | 2.33 |
| 10 | 2205 | 2205 | Yes | 2.58 |
| 11 | 1413 | 1413 | Yes | 1.72 |
| 12 | 1929 | 1929 | Yes | 1.76 |
| 13 | 2288 | 2288 | Yes | 1.62 |
| 14 | 1184 | 1184 | Yes | 2.02 |
| 15 | 754 | 754 | Yes | 1.79 |
| 16 | 2393 | 2393 | Yes | 1.55 |
| 17 | 2263 | 2263 | Yes | 2.17 |
| 18 | 359 | 359 | Yes | 1.86 |
| 19 | 2103 | 2103 | Yes | 3.73 |
| 20 | 1572 | 1572 | Yes | 2.87 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 46 | 67 | No | 17.82 |
| 2 | 63 | 61 | No | 18.09 |
| 3 | 59 | 67 | No | 15.15 |
| 4 | 75 | 76 | No | 22.93 |
| 5 | 58 | 59 | No | 14.09 |
| 6 | 46 | 46 | Yes | 15.6 |
| 7 | 44 | 43 | No | 14.02 |
| 8 | 62 | 62 | Yes | 15.91 |
| 9 | 65 | 67 | No | 20.07 |
| 10 | 69 | 67 | No | 13.29 |
| 11 | 49 | 49 | Yes | 14.89 |
| 12 | 37 | 37 | Yes | 12.97 |
| 13 | 52 | 50 | No | 14.21 |
| 14 | 44 | 67 | No | 17.55 |
| 15 | 48 | 47 | No | 14.43 |
| 16 | 67 | 65 | No | 14.72 |
| 17 | 68 | 68 | Yes | 18.81 |
| 18 | 39 | 39 | Yes | 14.3 |
| 19 | 64 | 61 | No | 19.75 |
| 20 | 36 | 67 | No | 12.58 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QXRYPSI | QXRYPSI | Yes | 5.27 |
| 2 | AVWPKLE | AVWPKLE | Yes | 5.2 |
| 3 | XFQJRYL | XFQJRYL | Yes | 5.37 |
| 4 | XZITRUD | XZITRUD | Yes | 5.57 |
| 5 | PMLDSCA | PMLDSCA | Yes | 5.51 |
| 6 | GWRUZDI | GWRUZDI | Yes | 4.63 |
| 7 | MECXBWQ | MECXBWQ | Yes | 4.72 |
| 8 | ALEKYFM | ALEKYFM | Yes | 6.72 |
| 9 | RNLUQXS | RNLUQXS | Yes | 5.81 |
| 10 | RINSBHF | RINSBHF | Yes | 4.88 |
| 11 | CBWPLRH | CBWPLRH | Yes | 4.01 |
| 12 | ALTPQRX | ALTPQRX | Yes | 6.43 |
| 13 | PMOJNTU | PMOJNTU | Yes | 4.9 |
| 14 | LPIBREJ | LPIBREJ | Yes | 4.62 |
| 15 | GFLRAKE | GFLRAKE | Yes | 5.04 |
| 16 | SRMBEJO | SRMBEJO | Yes | 4.73 |
| 17 | VKIAECJ | VKIAECJ | Yes | 6.56 |
| 18 | KPIUCQB | KPIUCQB | Yes | 6.61 |
| 19 | GCIKHVX | GCIKHVX | Yes | 5.44 |
| 20 | FTEWVLM | FTEWVLM | Yes | 5.02 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 4.3 5.7 | Yes | 4.74 |
| 2 | [3.4, 6.6] | 3.4 6.6 | Yes | 2.37 |
| 3 | [0.8, 9.2] | 9.2 0.8 | Yes | 3.4 |
| 4 | [1.8, 8.2] | 1.8 8.2 | Yes | 2.78 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 2.39 |
| 6 | [1.4, 8.6] | 8.6 1.4 | Yes | 3.3 |
| 7 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.99 |
| 8 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.05 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 2.98 |
| 10 | [4.9, 5.1] | 4.9 5.1 | Yes | 5.58 |
| 11 | [4.1, 5.9] | 4.1 5.9 | Yes | 2.11 |
| 12 | [4.0, 6.0] | 6.0 4.0 | Yes | 4.1 |
| 13 | [1.5, 8.5] | 1.5 8.5 | Yes | 3.07 |
| 14 | [1.0, 9.0] | 1.0 9.0 | Yes | 2.52 |
| 15 | [4.1, 5.9] | 4.1 5.9 | Yes | 5.4 |
| 16 | [1.7, 8.3] | 8.3 1.7 | Yes | 2.55 |
| 17 | [3.7, 6.3] | 6.3 3.7 | Yes | 3.33 |
| 18 | [0.1, 9.9] | 9.9 0.1 | Yes | 2.09 |
| 19 | [2.9, 7.1] | 2.9 7.1 | Yes | 2.21 |
| 20 | [2.3, 7.7] | 2.3 7.7 | Yes | 5.17 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 97LYVEU85B90 | 97LYVEU85B90 | Yes | 2.83 |
| 2 | DJPKEDJ01PQZ | DJPKEDJ01PQZ | Yes | 2.67 |
| 3 | JWI24SDE0C9B | JWI24SDE0C9B | Yes | 2.25 |
| 4 | JP2MM52O2U79 | JP2MM52O2U79 | Yes | 2.54 |
| 5 | Q9F3MG2SWSYA | Q9F3MG2SWSYA | Yes | 2.47 |
| 6 | TY6XV62WA5P8 | TY6XV62WA5P8 | Yes | 1.88 |
| 7 | 9YFBL0F07IU7 | 9YFBL0F07IU7 | Yes | 2.0 |
| 8 | ZVUSVKEY0P3F | ZVUSVKEY0P3F | Yes | 1.76 |
| 9 | 9LE3J0ZKVXB7 | 9LE3J0ZKVXB7 | Yes | 2.63 |
| 10 | WKP1RO8VLMD9 | WKP1RO8VLMD9 | Yes | 1.83 |
| 11 | 7A7M62DII5AY | 7A7M62DII5AY | Yes | 1.72 |
| 12 | GSIYB62LKDG1 | GSIYB62LKDG1 | Yes | 2.34 |
| 13 | PQTT7WPS11PC | PQTT7WPS11PC | Yes | 1.65 |
| 14 | LVCGOUU5E2FP | LVCGOUU5E2FP | Yes | 2.41 |
| 15 | 5SE90F7WCJIA | 5SE90F7WCJIA | Yes | 1.53 |
| 16 | SLV5EQ3JTYQK | SLV5EQ3JTYQK | Yes | 2.38 |
| 17 | X9ATQ6EWIUWK | X9ATQ6EWIUWK | Yes | 3.57 |
| 18 | UG7XP3J6ZF5L | UG7XP3J6ZF5L | Yes | 1.98 |
| 19 | O13G0336KKUN | O13G0336KKUN | Yes | 1.7 |
| 20 | 68C25POIBTUG | 68C25POIBTUG | Yes | 1.59 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 1.8 |
| 2 | 6 | 6 | Yes | 2.5 |
| 3 | 16 | 16 | Yes | 2.5 |
| 4 | 19 | 19 | Yes | 3.13 |
| 5 | 23 | 23 | Yes | 2.62 |
| 6 | 31 | 31 | Yes | 1.32 |
| 7 | 4096 | 1048576 | No | 5.36 |
| 8 | 7680 | 7680 | Yes | 3.92 |
| 9 | 65 | 65 | Yes | 2.07 |
| 10 | 1 | 1 | Yes | 4.48 |
| 11 | 9 | 9 | Yes | 2.5 |
| 12 | 243 | 243 | Yes | 1.5 |
| 13 | 20 | 20 | Yes | 6.47 |
| 14 | 73 | 73 | Yes | 3.64 |
| 15 | 9 | 9 | Yes | 11.84 |
| 16 | 44 | 44 | Yes | 3.6 |
| 17 | 7 | 7 | Yes | 2.69 |
| 18 | 3 | 3 | Yes | 5.6 |
| 19 | 5 | 16 | No | 19.58 |
| 20 | 60 | 60 | Yes | 2.2 |
