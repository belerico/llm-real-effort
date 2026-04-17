# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8706 | 34410 | 43116 | 0 | 20 | 17.55 | 351.29 |
| add_numbers | 37134 | 8132 | 45266 | 20 | 0 | 6.61 | 132.36 |
| counting_zeros | 25310 | 33570 | 58880 | 11 | 9 | 17.09 | 342.12 |
| task_decoding | 43294 | 7519 | 50813 | 18 | 2 | 7.27 | 145.59 |
| task_summation | 26620 | 22923 | 49543 | 20 | 0 | 12.43 | 248.73 |
| task_transcription | 24280 | 10803 | 35083 | 14 | 6 | 9.54 | 190.83 |
| task_sequences | 2795 | 15579 | 18374 | 20 | 0 | 9.19 | 183.85 |
| **TOTAL** | **168139** | **132936** | **301075** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 5 5 3 3 2 5 4 1 6 1 2 1 | 5 3 2 3 5 5 3 2 5 2 3 1 4 1 6 1 6 2 1 2 | No | 14.66 |
| 2 | 3 5 6 6 2 5 2 6 4 5 4 3 1 1 | 3 5 6 5 2 6 2 6 2 4 3 5 4 1 3 1 | No | 15.86 |
| 3 | 1 6 4 5 4 6 2 6 2 3 2 5 1 4 | 1 6 5 4 4 6 2 6 2 4 3 2 1 4 1 2 4 3 2 1 | No | 15.48 |
| 4 | 2 6 3 1 6 6 3 1 6 1 3 5 2 4 | 2 6 3 1 6 6 1 6 1 3 1 2 3 4 5 | No | 15.49 |
| 5 | 5 4 2 1 3 6 3 4 6 5 1 6 4 2 | 5 4 2 1 3 6 1 4 3 6 6 1 2 5 4 | No | 15.63 |
| 6 | 3 1 5 4 4 2 5 3 6 1 4 2 2 5 |  | No | 34.49 |
| 7 | 4 2 6 4 1 2 5 5 1 6 1 5 2 4 | 4 2 6 4 1 5 1 2 5 4 | No | 16.37 |
| 8 | 3 1 6 6 4 3 5 1 5 6 4 5 4 3 | 6 1 3 1 6 3 4 5 6 1 3 5 6 5 4 4 5 3 4 | No | 15.47 |
| 9 | 3 2 2 1 3 6 1 2 6 5 3 4 2 1 | 3 2 2 1 3 1 6 2 1 6 6 3 5 2 4 1 2 5 | No | 25.17 |
| 10 | 3 4 1 4 2 3 5 2 6 3 5 2 5 4 | 3 4 4 1 2 3 4 3 2 5 5 2 5 3 5 4 2 5 2 4 | No | 16.37 |
| 11 | 5 6 6 3 2 5 2 4 1 2 3 5 5 3 | 5 6 6 2 3 5 2 4 1 5 2 3 4 5 3 5 3 | No | 15.53 |
| 12 | 5 2 5 6 6 2 1 2 6 5 1 5 4 3 | 5 2 6 5 6 2 1 6 2 6 5 1 5 1 6 5 3 4 | No | 15.24 |
| 13 | 1 4 1 5 6 6 3 2 3 6 3 5 5 2 | 1 4 1 5 6 3 6 2 3 3 5 6 5 2 | No | 15.95 |
| 14 | 1 2 5 1 6 4 3 1 2 4 1 6 5 3 | 1 2 5 1 6 2 4 1 3 4 1 3 4 1 6 3 5 3 | No | 15.1 |
| 15 | 5 2 6 1 3 4 5 3 2 3 5 2 3 4 | 5 2 6 1 3 4 3 2 3 5 2 3 5 3 2 4 3 2 | No | 15.24 |
| 16 | 3 3 1 2 5 5 3 6 5 6 1 3 5 3 | 3 1 5 3 5 3 6 5 6 5 1 6 5 3 5 3 | No | 24.56 |
| 17 | 6 4 2 1 4 5 6 3 6 1 1 2 6 4 | 4 6 2 1 6 1 3 1 6 1 2 6 4 4 1 6 | No | 16.18 |
| 18 | 2 5 6 2 5 3 6 6 1 3 5 2 4 2 | 2 5 2 5 6 3 5 2 4 3 5 2 4 | No | 18.21 |
| 19 | 5 4 1 2 6 2 3 5 1 5 3 6 1 6 | 5 1 2 4 5 6 3 5 1 5 3 1 6 5 1 6 3 | No | 15.56 |
| 20 | 1 2 3 4 5 3 5 1 6 6 1 3 4 5 | Answering requires solving the provided 6x6 Sudoku puzzle and then listing the missing numbers in reading order (left to right, top to bottom).  The initial grid is: ``` +---+---+---+---+---+---+ \|   \| 6 \|   \|   \|   \| 5 \| \| 4 \| 2 \|   \| 6 \|   \| 1 \| +---+---+---+---+---+---+ \| 3 \|   \|   \| 4 \|   \| 2 \| \|   \|   \|   \| 5 \| 2 \| 4 \| +---+---+---+---+---+---+ \| 5 \| 3 \| 4 \| 2 \| 1 \| 6 \| \| 2 \|   \| 6 \| 1 \|   \| 3 \| +---+---+---+---+---+---+ ```  The solved grid is: ``` +---+---+---+---+---+---+ \| 1 \| 6 \| 2 \| 3 \| 4 \| 5 \| \| 4 \| 2 \| 5 \| 6 \| 3 \| 1 \| +---+---+---+---+---+---+ \| 3 \| 5 \| 1 \| 4 \| 6 \| 2 \| \| 6 \| 1 \| 3 \| 5 \| 2 \| 4 \| +---+---+---+---+---+---+ \| 5 \| 3 \| 4 \| 2 \| 1 \| 6 \| \| 2 \| 4 \| 6 \| 1 \| 5 \| 3 \| +---+---+---+---+---+---+ ```  The missing numbers, in reading order, are the numbers we filled into the empty cells.  1.  **Row 1:** 1, 2, 3, 4 2.  **Row 2:** 5, 3 3.  **Row 3:** 5, 1, | No | 14.53 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2173 | 2173 | Yes | 6.42 |
| 2 | 2015 | 2015 | Yes | 8.08 |
| 3 | 1973 | 1973 | Yes | 5.82 |
| 4 | 1138 | 1138 | Yes | 9.11 |
| 5 | 1876 | 1876 | Yes | 4.99 |
| 6 | 1505 | 1505 | Yes | 4.89 |
| 7 | 2259 | 2259 | Yes | 6.23 |
| 8 | 1948 | 1948 | Yes | 4.21 |
| 9 | 1876 | 1876 | Yes | 5.16 |
| 10 | 1220 | 1220 | Yes | 6.2 |
| 11 | 1827 | 1827 | Yes | 16.11 |
| 12 | 1700 | 1700 | Yes | 6.46 |
| 13 | 1603 | 1603 | Yes | 4.83 |
| 14 | 1311 | 1311 | Yes | 5.5 |
| 15 | 1453 | 1453 | Yes | 6.65 |
| 16 | 1869 | 1869 | Yes | 4.74 |
| 17 | 797 | 797 | Yes | 3.86 |
| 18 | 1490 | 1490 | Yes | 6.8 |
| 19 | 1057 | 1057 | Yes | 10.63 |
| 20 | 2481 | 2481 | Yes | 5.58 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 11.45 |
| 2 | 70 | 69 | No | 15.22 |
| 3 | 61 | 61 | Yes | 24.73 |
| 4 | 37 | 37 | Yes | 14.19 |
| 5 | 66 | 66 | Yes | 13.67 |
| 6 | 52 | 51 | No | 14.61 |
| 7 | 63 | 60 | No | 14.26 |
| 8 | 36 | 36 | Yes | 15.11 |
| 9 | 68 | 68 | Yes | 14.73 |
| 10 | 67 | 67 | Yes | 14.64 |
| 11 | 39 | 39 | Yes | 12.48 |
| 12 | 67 | 65 | No | 15.96 |
| 13 | 73 | 73 | Yes | 16.25 |
| 14 | 50 | 50 | Yes | 13.37 |
| 15 | 58 | 64 | No | 14.32 |
| 16 | 47 | 46 | No | 15.44 |
| 17 | 52 |  | No | 35.81 |
| 18 | 35 | 35 | Yes | 14.04 |
| 19 | 70 |  | No | 35.79 |
| 20 | 67 | 66 | No | 15.73 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OCXHUIJ | OCXHUIJ | Yes | 6.15 |
| 2 | OYUNMXG | OYUNMXG | Yes | 5.01 |
| 3 | NYRZFDQ | NYRZFQD | No | 4.32 |
| 4 | MAGPEKY | MAGPEKY | Yes | 16.26 |
| 5 | NYCDZWA | NYCDZWA | Yes | 5.2 |
| 6 | FHJKDIM | FHJKDIM | Yes | 4.99 |
| 7 | OBMACSZ | OBMACSZ | Yes | 15.96 |
| 8 | DEHXUSF | DEHXUSF | Yes | 6.25 |
| 9 | BWHMIOD | BWHMIOD | Yes | 8.34 |
| 10 | MITGPAS | MITGPAS | Yes | 5.56 |
| 11 | USIWRCJ | USIWRCJ | Yes | 17.1 |
| 12 | EZWKMGN | EZWKMGN | Yes | 4.47 |
| 13 | WLRBYSP | WLRBYSP | Yes | 5.42 |
| 14 | HGBJARK | HGBJARK | Yes | 5.2 |
| 15 | LOUKPFJ | LOOKUPJ | No | 6.06 |
| 16 | SPVKWHF | SPVKWHF | Yes | 5.58 |
| 17 | HYOMJKD | HYOMJKD | Yes | 5.59 |
| 18 | TVOKDSH | TVOKDSH | Yes | 5.17 |
| 19 | KADCGHP | KADCGHP | Yes | 7.39 |
| 20 | HSDUPVW | HSDUPVW | Yes | 5.35 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.7, 5.3] | 4.7 5.3 | Yes | 9.55 |
| 2 | [0.7, 9.3] | 9.3 0.7 | Yes | 14.27 |
| 3 | [1.6, 8.4] | 1.6 8.4 | Yes | 10.46 |
| 4 | [4.6, 5.4] | 5.4 4.6 | Yes | 11.14 |
| 5 | [4.4, 5.6] | 4.4 5.6 | Yes | 11.77 |
| 6 | [0.1, 9.9] | 9.9 0.1 | Yes | 10.47 |
| 7 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.95 |
| 8 | [3.3, 6.7] | 6.7 3.3 | Yes | 11.71 |
| 9 | [0.8, 9.2] | 9.2 0.8 | Yes | 11.78 |
| 10 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.76 |
| 11 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.13 |
| 12 | [3.6, 6.4] | 6.4 3.6 | Yes | 9.61 |
| 13 | [3.9, 6.1] | 3.9 6.1 | Yes | 13.65 |
| 14 | [0.6, 9.4] | 0.6 9.4 | Yes | 11.26 |
| 15 | [0.2, 9.8] | 0.2 9.8 | Yes | 20.57 |
| 16 | [2.2, 7.8] | 7.8 2.2 | Yes | 12.19 |
| 17 | [4.0, 6.0] | 4.0 6.0 | Yes | 21.81 |
| 18 | [1.5, 8.5] | 1.5 8.5 | Yes | 12.13 |
| 19 | [4.0, 6.0] | 4.0 6.0 | Yes | 12.04 |
| 20 | [0.8, 9.2] | 9.2 0.8 | Yes | 15.29 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | K5EQNROZ5O26 | K5EQNROZ5026 | No | 12.51 |
| 2 | 8BJT4W1YF81A | 8BJT4W1YF81A | Yes | 6.27 |
| 3 | 9SL57OIQ8ZCY | 9SL57O1Q8ZCY | No | 10.29 |
| 4 | RBJFT3UGKM92 | RBJFT3UGKM92 | Yes | 16.62 |
| 5 | ICX4EC534J5P | ICX4EC534J5P | Yes | 5.82 |
| 6 | NPCD38SJFYLY | NPCD38SJFYLY | Yes | 5.35 |
| 7 | PXSZF09ABPNS | PXSZF09ABPNS | Yes | 6.74 |
| 8 | SJZUYRD9FOQB | SJZUYRD9FOOQB | No | 5.77 |
| 9 | NH67SYKG8M0I | NH67SYKG8M0I | Yes | 7.31 |
| 10 | P8BM7OYVR6I0 | P8BM70YVR610 | No | 16.53 |
| 11 | JOP0CMOVV9XL | JOPOCMOVV9XL | No | 6.23 |
| 12 | O53IL7QQZ31D | O53IL7QQZ31D | Yes | 6.41 |
| 13 | OMXC4C6R815A | OMXC4C6R815A | Yes | 8.19 |
| 14 | LUY8YISFGFKI | LUY8YISFGFKI | Yes | 6.68 |
| 15 | 803X6RJCGQHM | 803X6RJCGQHM | Yes | 16.21 |
| 16 | 5AKE9TKJFI1E | 5AKE9TKJFI1E | Yes | 6.21 |
| 17 | BFWTP0HABZUY | BFWTP0HABZUY | Yes | 18.58 |
| 18 | D4VDT7LKAHJ4 | D4VDTT7LKAHJ4 | No | 16.97 |
| 19 | IEW2PZ51WOOT | IEW2PZ51WOOT | Yes | 6.54 |
| 20 | 1PVSEJNFG4XR | 1PVSEJNFG4XR | Yes | 5.47 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 26 | 26 | Yes | 14.73 |
| 2 | 20 | 20 | Yes | 22.52 |
| 3 | 48 | 48 | Yes | 7.4 |
| 4 | 63 | 63 | Yes | 8.44 |
| 5 | 67 | 67 | Yes | 6.15 |
| 6 | 3 | 3 | Yes | 9.12 |
| 7 | 5 | 5 | Yes | 7.96 |
| 8 | 28 | 28 | Yes | 8.17 |
| 9 | 64 | 64 | Yes | 5.67 |
| 10 | 1 | 1 | Yes | 15.64 |
| 11 | 4 | 4 | Yes | 9.6 |
| 12 | 7680 | 7680 | Yes | 8.07 |
| 13 | 4 | 4 | Yes | 7.71 |
| 14 | 39 | 39 | Yes | 6.71 |
| 15 | 60 | 60 | Yes | 8.85 |
| 16 | 19 | 19 | Yes | 6.32 |
| 17 | 65 | 65 | Yes | 6.74 |
| 18 | 6 | 6 | Yes | 9.18 |
| 19 | 9 | 9 | Yes | 7.46 |
| 20 | 44 | 44 | Yes | 7.42 |
