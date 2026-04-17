# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-19 09:59:28

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
| sudoku_game | 8060 | 36616 | 44676 | 10 | 10 | 29.14 | 582.92 |
| add_numbers | 3980 | 705 | 4685 | 20 | 0 | 2.40 | 48.1 |
| counting_zeros | 6920 | 29425 | 36345 | 2 | 18 | 16.80 | 336.39 |
| task_decoding | 13360 | 5004 | 18364 | 20 | 0 | 5.16 | 103.4 |
| task_summation | 7280 | 3510 | 10790 | 20 | 0 | 3.90 | 78.1 |
| task_transcription | 4124 | 847 | 4971 | 19 | 1 | 2.59 | 52.02 |
| task_sequences | 3241 | 3571 | 6812 | 18 | 2 | 3.70 | 74.04 |
| **TOTAL** | **46965** | **79678** | **126643** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 2 1 5 2 5 4 3 5 4 3 5 1 1 |  | No | 35.53 |
| 2 | 6 3 5 4 6 1 4 1 6 5 3 6 2 1 | 6 3 5 4 6 1 4 1 6 5 3 6 2 1 | Yes | 31.06 |
| 3 | 1 2 6 4 5 1 2 2 6 4 5 2 4 1 |  | No | 34.85 |
| 4 | 2 3 2 4 5 1 2 2 4 1 3 6 2 6 |  | No | 36.73 |
| 5 | 1 5 2 1 3 3 2 5 1 1 1 5 4 2 |  | No | 34.26 |
| 6 | 1 5 1 2 4 3 5 4 1 2 6 3 1 4 |  | No | 31.44 |
| 7 | 1 5 4 6 2 6 4 3 4 2 5 3 5 3 | Looking at this puzzle, I'll work through it systematically.  **Given grid:** ``` _  _  _  _  _  3 _  2  1  3  _  5 _  _  _  _  1  6 4  _  6  1  5  2 2  6  5  4  3  1 _  1  _  2  6  4 ```  **Step-by-step solving:**  **Row 2 (cols 1,5):** Row needs 4,6. Col 1 needs {1,3,5,6}, so col1=6; col5=4  **Row 3:** Col 4 must be 5 (col 4 needs 5 or 6, Box 4 confirms). Col 5=1 ✓, Col 6=6 ✓ - Col 1 row 3: intersection of col1 needs {1,3,5} and row needs {2,3,4} → **3** - Col 2 row 3: col2 needs {3,4,5}, row needs {2,4} → **4**   - Col 3 row 3: remaining → **2**  **Row 4 col 2:** Col 2 needs 3, Box 3 confirms → **3**  **Row 6 (cols 1,3):** Row needs | No | 34.09 |
| 8 | 4 1 4 2 6 5 1 1 4 2 5 5 6 4 | 4 1 4 2 6 5 1 1 4 2 5 5 6 4 | Yes | 19.33 |
| 9 | 5 3 1 6 4 3 1 5 5 1 3 3 1 6 |  | No | 34.55 |
| 10 | 5 1 3 1 5 3 6 4 3 4 4 5 2 6 | 5 1 3 1 5 3 6 4 3 4 4 5 2 6 | Yes | 25.5 |
| 11 | 2 6 1 6 3 4 2 1 4 3 2 5 1 6 | 2 6 1 6 3 4 2 1 4 3 2 5 1 6 | Yes | 29.43 |
| 12 | 3 5 4 2 1 5 2 4 1 3 2 4 1 5 | 3 5 4 2 1 5 2 4 1 3 2 4 1 5 | Yes | 18.78 |
| 13 | 1 2 3 6 1 4 4 6 2 5 4 3 6 5 |  | No | 35.58 |
| 14 | 2 5 3 3 5 2 5 4 3 6 3 1 4 5 | 2 5 3 3 5 2 5 4 3 6 3 1 4 5 | Yes | 25.65 |
| 15 | 6 4 5 2 5 1 6 3 5 5 2 3 6 4 | 6 4 5 2 5 1 6 3 5 5 2 3 6 4 | Yes | 22.1 |
| 16 | 2 3 4 3 6 1 6 2 4 5 1 5 2 3 | 2 3 4 3 6 1 6 2 4 5 1 5 2 3 | Yes | 20.12 |
| 17 | 6 3 2 5 5 3 2 6 3 4 6 3 4 2 | 6 3 2 5 5 3 2 6 3 4 6 3 4 2 | Yes | 21.15 |
| 18 | 1 6 3 5 5 6 1 3 2 4 5 6 6 4 | 1 6 3 5 5 6 1 3 2 4 5 6 6 4 | Yes | 24.66 |
| 19 | 2 1 5 4 5 3 2 6 5 5 1 2 3 4 | 2 1 5 5 4 3 2 6 5 5 1 2 | No | 34.06 |
| 20 | 3 5 3 5 4 6 6 4 5 1 3 4 4 6 |  | No | 33.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1697 | 1697 | Yes | 2.72 |
| 2 | 1171 | 1171 | Yes | 2.12 |
| 3 | 2334 | 2334 | Yes | 1.56 |
| 4 | 1314 | 1314 | Yes | 2.16 |
| 5 | 1404 | 1404 | Yes | 2.24 |
| 6 | 1820 | 1820 | Yes | 1.92 |
| 7 | 1282 | 1282 | Yes | 2.47 |
| 8 | 1358 | 1358 | Yes | 2.04 |
| 9 | 1846 | 1846 | Yes | 2.57 |
| 10 | 1495 | 1495 | Yes | 2.1 |
| 11 | 1714 | 1714 | Yes | 2.14 |
| 12 | 1952 | 1952 | Yes | 3.77 |
| 13 | 1367 | 1367 | Yes | 2.72 |
| 14 | 2064 | 2064 | Yes | 2.71 |
| 15 | 2653 | 2653 | Yes | 3.42 |
| 16 | 1201 | 1201 | Yes | 1.43 |
| 17 | 1880 | 1880 | Yes | 2.65 |
| 18 | 1896 | 1896 | Yes | 2.17 |
| 19 | 1286 | 1286 | Yes | 2.91 |
| 20 | 1433 | 1433 | Yes | 2.2 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 67 | No | 22.17 |
| 2 | 69 | 69 | Yes | 18.61 |
| 3 | 37 | 36 | No | 16.83 |
| 4 | 73 | 67 | No | 16.06 |
| 5 | 37 | 38 | No | 12.65 |
| 6 | 44 | 41 | No | 14.39 |
| 7 | 68 | 67 | No | 20.21 |
| 8 | 75 | 67 | No | 17.14 |
| 9 | 52 | 52 | Yes | 18.15 |
| 10 | 52 | 53 | No | 19.06 |
| 11 | 75 | 68 | No | 17.39 |
| 12 | 51 | 52 | No | 16.6 |
| 13 | 68 | 67 | No | 19.38 |
| 14 | 58 | 55 | No | 13.45 |
| 15 | 51 | 52 | No | 18.31 |
| 16 | 48 | 43 | No | 12.9 |
| 17 | 70 | 67 | No | 14.98 |
| 18 | 37 | 67 | No | 13.29 |
| 19 | 65 | 67 | No | 20.41 |
| 20 | 53 | 51 | No | 14.1 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PZYFEDV | PZYFEDV | Yes | 6.64 |
| 2 | KPDRONT | KPDRONT | Yes | 6.0 |
| 3 | YAORQTD | YAORQTD | Yes | 4.9 |
| 4 | LVAPTFM | LVAPTFM | Yes | 5.61 |
| 5 | KOESIPJ | KOESIPJ | Yes | 5.23 |
| 6 | BSTIUYN | BSTIUYN | Yes | 4.61 |
| 7 | EXFTVAN | EXFTVAN | Yes | 4.77 |
| 8 | PXIOYNE | PXIOYNE | Yes | 5.01 |
| 9 | KCQBORY | KCQBORY | Yes | 4.58 |
| 10 | YMHUQTF | YMHUQTF | Yes | 5.48 |
| 11 | LTHVUSI | LTHVUSI | Yes | 6.34 |
| 12 | HYBSZGT | HYBSZGT | Yes | 5.71 |
| 13 | AZUVCPE | AZUVCPE | Yes | 5.14 |
| 14 | QDPZYMN | QDPZYMN | Yes | 5.09 |
| 15 | AWTOEKF | AWTOEKF | Yes | 4.12 |
| 16 | KRAMUEV | KRAMUEV | Yes | 5.93 |
| 17 | BEDXMGT | BEDXMGT | Yes | 4.4 |
| 18 | ZXTSKUA | ZXTSKUA | Yes | 5.0 |
| 19 | LRTMZWN | LRTMZWN | Yes | 3.57 |
| 20 | SKNEIQC | SKNEIQC | Yes | 5.07 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.0, 9.0] | 9.0 1.0 | Yes | 2.95 |
| 2 | [4.4, 5.6] | 5.6 4.4 | Yes | 4.54 |
| 3 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.14 |
| 4 | [0.9, 9.1] | 9.1 0.9 | Yes | 3.36 |
| 5 | [3.8, 6.2] | 3.8 6.2 | Yes | 2.72 |
| 6 | [0.1, 9.9] | 9.9 0.1 | Yes | 3.31 |
| 7 | [3.8, 6.2] | 6.2 3.8 | Yes | 2.36 |
| 8 | [4.2, 5.8] | 4.2 5.8 | Yes | 2.77 |
| 9 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.36 |
| 10 | [2.1, 7.9] | 2.1 7.9 | Yes | 2.87 |
| 11 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.84 |
| 12 | [3.0, 7.0] | 7.0 3.0 | Yes | 2.37 |
| 13 | [4.0, 6.0] | 4.0 6.0 | Yes | 3.92 |
| 14 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.1 |
| 15 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.02 |
| 16 | [2.1, 7.9] | 2.1 7.9 | Yes | 2.76 |
| 17 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.02 |
| 18 | [1.9, 8.1] | 8.1 1.9 | Yes | 4.11 |
| 19 | [3.1, 6.9] | 3.1 6.9 | Yes | 3.85 |
| 20 | [3.8, 6.2] | 6.2 3.8 | Yes | 2.6 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | L5IN0XFPAAJJ | L5IN0XFPAAJJ | Yes | 2.54 |
| 2 | L96W5KZVEYOV | L96W5KZVEYOV | Yes | 2.29 |
| 3 | EBUC1SZ9I86V | EBUC1SZ9I86V | Yes | 2.69 |
| 4 | G34TIVP5X3WS | G34TIVP5X3WS | Yes | 2.76 |
| 5 | UQRWUFF8R2Q9 | UQRWUFF8R2Q9 | Yes | 2.46 |
| 6 | V45YC07V1JR9 | V45YC07V1JR9 | Yes | 2.63 |
| 7 | ZEX6VFU6ZNQ1 | ZEX6VFU6ZNQ1 | Yes | 2.75 |
| 8 | WPXAEYS78W5N | WPXAEYS78W5N | Yes | 2.51 |
| 9 | C21UT4YYG4P3 | C21UT4YYG4P3 | Yes | 1.97 |
| 10 | LD756FP7KJW0 | LD756FP7KJWO | No | 2.11 |
| 11 | BJUIKX3RTDWM | BJUIKX3RTDWM | Yes | 2.61 |
| 12 | WU11FO1AMT3G | WU11FO1AMT3G | Yes | 2.75 |
| 13 | 0KUAN1M7RVCH | 0KUAN1M7RVCH | Yes | 2.95 |
| 14 | U9BSX29X8PUO | U9BSX29X8PUO | Yes | 2.46 |
| 15 | EYH4F3XG6CY8 | EYH4F3XG6CY8 | Yes | 2.7 |
| 16 | 883EZ90QGKPI | 883EZ90QGKPI | Yes | 2.67 |
| 17 | 4FZSTP6YHDX0 | 4FZSTP6YHDX0 | Yes | 2.66 |
| 18 | TQVDP5151DTK | TQVDP5151DTK | Yes | 3.32 |
| 19 | S9O4G958ATMA | S9O4G958ATMA | Yes | 3.28 |
| 20 | HCB6NR20EP4B | HCB6NR20EP4B | Yes | 1.79 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 2.05 |
| 2 | 4096 | 16384 | No | 14.95 |
| 3 | 19 | 19 | Yes | 2.03 |
| 4 | 16 | 16 | Yes | 1.71 |
| 5 | 793 | 793 | Yes | 2.06 |
| 6 | 9 | 9 | Yes | 2.01 |
| 7 | 3 | 3 | Yes | 5.68 |
| 8 | 64 | 64 | Yes | 3.4 |
| 9 | 23 | 23 | Yes | 2.68 |
| 10 | 6 | 6 | Yes | 1.75 |
| 11 | 4 | 4 | Yes | 2.04 |
| 12 | 5 | 16 | No | 12.84 |
| 13 | 198 | 198 | Yes | 1.71 |
| 14 | 60 | 60 | Yes | 2.35 |
| 15 | 5 | 5 | Yes | 5.14 |
| 16 | 10 | 10 | Yes | 1.71 |
| 17 | 1440 | 1440 | Yes | 2.22 |
| 18 | 48 | 48 | Yes | 2.2 |
| 19 | 73 | 73 | Yes | 3.87 |
| 20 | 7680 | 7680 | Yes | 1.65 |
