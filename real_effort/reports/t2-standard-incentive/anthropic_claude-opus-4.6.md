# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
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
| sudoku_game | 8600 | 33971 | 42571 | 9 | 11 | 26.57 | 531.69 |
| add_numbers | 4520 | 594 | 5114 | 20 | 0 | 3.34 | 66.83 |
| counting_zeros | 7460 | 22770 | 30230 | 7 | 13 | 14.34 | 287.18 |
| task_decoding | 13900 | 3244 | 17144 | 20 | 0 | 7.55 | 151.17 |
| task_summation | 7820 | 5498 | 13318 | 20 | 0 | 6.83 | 136.88 |
| task_transcription | 4684 | 738 | 5422 | 17 | 3 | 3.62 | 72.5 |
| task_sequences | 3781 | 4473 | 8254 | 20 | 0 | 5.05 | 100.98 |
| **TOTAL** | **50765** | **71288** | **122053** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 1 6 2 1 3 2 4 3 1 6 4 5 | 3 2 1 6 4 2 1 3 2 4 3 1 6 4 5 | No | 25.24 |
| 2 | 4 2 3 5 6 4 5 5 1 1 3 6 4 1 | 4 2 3 5 6 4 5 5 1 1 3 6 4 1 | Yes | 24.08 |
| 3 | 5 2 4 5 3 5 1 2 1 4 2 3 1 5 | 5 2 4 5 3 5 1 2 1 4 2 3 1 5 | Yes | 18.5 |
| 4 | 4 6 2 5 3 3 1 3 6 4 3 1 6 4 | 4 6 2 5 3 3 1 3 6 4 3 1 6 4 | Yes | 24.58 |
| 5 | 2 3 2 1 3 5 5 6 4 2 5 2 4 3 | 2 3 2 1 5 5 6 5 2 4 3 | No | 26.19 |
| 6 | 6 1 3 6 6 4 3 2 1 5 3 5 2 2 | Looking at this puzzle, I need to find the missing numbers by analyzing rows, columns, and 2×3 boxes.  **Row-by-row analysis:**  **Row 1:** 2,4,3,_,1,5 → missing **6** **Row 2:** _,_,2,5,_,4 → missing 1,3,6 **Row 3:** 5,_,1,_,_,_ → missing 2,3,4,6 **Row 4:** 4,_,6,2,_,3 → missing 1,5 **Row 5:** _,_,4,1,_,6 → missing 2,3,5 **Row 6:** 6,_,5,3,4,1 → missing **2**  **Using column and box constraints:**  - **Col 4** needs 4 → Row 3 gets **4** - **Row 4:** Col 5 must be 5 (box constraint), Col 2 = **1** → 4,**1**,6,2,**5**,3 - **Bottom-left box** (R5-6, C1-3): needs 1,3 → R5C1=**3**, R5C2=**5** (column constraints) - **Bottom-right box** (R5-6, C4-6): R5C5=**2** → Row 5: 3,5,4,1,2,6 - **Row 3:** Col 5 = **6**, Col 2 = **3**, Col 6 = **2** → 5,3,1,4,6,2 - **Row 2:** Col 2 = **6**, Col 1 = **1**, Col 5 = **3** → 1,6, | No | 33.37 |
| 7 | 4 2 3 6 4 5 6 3 2 5 1 4 2 6 | 4 2 6 3 4 5 3 6 2 5 1 4 2 6 | No | 24.63 |
| 8 | 3 1 2 3 1 4 1 5 2 3 4 1 5 3 | 3 1 2 3 1 4 1 5 2 3 4 1 5 3 | Yes | 22.69 |
| 9 | 4 6 1 4 5 3 4 4 4 3 1 6 4 1 |  | No | 40.25 |
| 10 | 3 4 1 1 4 2 5 4 1 3 6 6 5 1 | Looking at this puzzle, I need to find the missing numbers by applying Sudoku constraints for rows, columns, and 2×3 boxes.  **Starting with the easiest deductions:**  - **Row 6:** Has 3,6,2,4,5 → missing **1** → R6C1 = 1 - **Row 3:** Has 6,2,5,3,1 → missing **4** → R3C6 = 4 - **Row 2:** Has 5,2,4,6,3 → missing **1** → R2C2 = 1 - **Column 5:** Has 5,6,1,2,4 → missing **3** → R4C5 = 3 - **Column 6:** Has 2,3,4,1,5 → missing ** | No | 34.36 |
| 11 | 3 6 1 4 3 6 3 1 5 2 6 3 6 3 |  | No | 34.78 |
| 12 | 6 1 3 2 1 4 1 2 6 6 4 1 1 5 | 6 1 3 2 1 4 1 2 6 6 4 1 1 5 | Yes | 23.26 |
| 13 | 4 5 1 3 5 3 5 4 4 1 2 2 3 5 | 4 5 1 3 5 3 5 4 4 1 2 2 3 5 | Yes | 19.72 |
| 14 | 2 5 2 6 4 6 5 6 3 4 5 1 5 3 | 2 5 6 2 4 6 3 5 6 3 4 1 5 3 2 | No | 17.59 |
| 15 | 3 2 4 5 5 1 6 6 3 4 2 3 5 6 | 3 2 4 5 5 1 6 3 4 6 3 4 2 3 5 6 | No | 27.46 |
| 16 | 4 4 5 6 4 1 3 6 5 5 5 1 3 6 |  | No | 34.88 |
| 17 | 2 4 4 6 5 4 1 2 2 6 1 4 3 5 | 2 4 4 6 5 4 1 2 2 6 1 4 3 5 | Yes | 22.55 |
| 18 | 4 2 5 6 2 3 3 1 5 2 6 5 1 5 | 4 2 5 6 2 3 3 1 5 2 6 5 1 5 | Yes | 23.3 |
| 19 | 6 1 4 6 6 4 2 3 5 6 2 2 1 3 | 6 1 4 6 6 4 2 3 5 6 2 2 1 3 | Yes | 19.21 |
| 20 | 6 1 3 5 1 6 6 5 3 6 3 2 4 3 |  | No | 34.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1623 | 1623 | Yes | 3.03 |
| 2 | 1531 | 1531 | Yes | 2.66 |
| 3 | 1201 | 1201 | Yes | 4.68 |
| 4 | 1567 | 1567 | Yes | 3.09 |
| 5 | 1744 | 1744 | Yes | 5.1 |
| 6 | 1087 | 1087 | Yes | 3.18 |
| 7 | 1738 | 1738 | Yes | 2.68 |
| 8 | 1536 | 1536 | Yes | 3.79 |
| 9 | 1289 | 1289 | Yes | 2.81 |
| 10 | 1897 | 1897 | Yes | 3.04 |
| 11 | 745 | 745 | Yes | 2.88 |
| 12 | 958 | 958 | Yes | 3.48 |
| 13 | 684 | 684 | Yes | 2.71 |
| 14 | 1479 | 1479 | Yes | 3.25 |
| 15 | 1810 | 1810 | Yes | 3.86 |
| 16 | 1338 | 1338 | Yes | 2.74 |
| 17 | 1994 | 1994 | Yes | 2.92 |
| 18 | 1204 | 1204 | Yes | 3.29 |
| 19 | 2252 | 2252 | Yes | 3.7 |
| 20 | 1897 | 1897 | Yes | 3.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 56 | 55 | No | 14.4 |
| 2 | 37 | 36 | No | 13.97 |
| 3 | 48 | 46 | No | 12.59 |
| 4 | 50 | 49 | No | 15.82 |
| 5 | 49 | 51 | No | 19.41 |
| 6 | 57 | 56 | No | 14.77 |
| 7 | 59 | 57 | No | 13.85 |
| 8 | 44 | 43 | No | 24.56 |
| 9 | 63 | 61 | No | 12.83 |
| 10 | 59 | 58 | No | 13.74 |
| 11 | 41 | 41 | Yes | 13.42 |
| 12 | 66 | 62 | No | 13.27 |
| 13 | 36 | 36 | Yes | 11.52 |
| 14 | 52 | 52 | Yes | 12.73 |
| 15 | 36 | 36 | Yes | 12.02 |
| 16 | 62 | 62 | Yes | 13.2 |
| 17 | 74 | 78 | No | 14.84 |
| 18 | 42 | 41 | No | 12.23 |
| 19 | 51 | 51 | Yes | 14.79 |
| 20 | 53 | 53 | Yes | 12.93 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DINYRWS | DINYRWS | Yes | 6.9 |
| 2 | HXZAOTI | HXZAOTI | Yes | 6.86 |
| 3 | ZRLCKHF | ZRLCKHF | Yes | 8.2 |
| 4 | RLYXNET | RLYXNET | Yes | 5.71 |
| 5 | SQKOVCR | SQKOVCR | Yes | 4.46 |
| 6 | YLJXSKU | YLJXSKU | Yes | 7.17 |
| 7 | DRLOPXW | DRLOPXW | Yes | 5.42 |
| 8 | EYRMDHI | EYRMDHI | Yes | 3.75 |
| 9 | DMOZESL | DMOZESL | Yes | 7.29 |
| 10 | PMSFIAW | PMSFIAW | Yes | 6.44 |
| 11 | QLDSPKX | QLDSPKX | Yes | 3.67 |
| 12 | RGCFJTD | RGCFJTD | Yes | 15.26 |
| 13 | MSXIUGT | MSXIUGT | Yes | 3.71 |
| 14 | GIRLUBT | GIRLUBT | Yes | 19.14 |
| 15 | OEUXYSJ | OEUXYSJ | Yes | 6.49 |
| 16 | BWOFKCZ | BWOFKCZ | Yes | 8.21 |
| 17 | IGYHOWK | IGYHOWK | Yes | 7.37 |
| 18 | NWSJUOG | NWSJUOG | Yes | 3.97 |
| 19 | DVTOEKJ | DVTOEKJ | Yes | 14.79 |
| 20 | FRZVIXC | FRZVIXC | Yes | 6.15 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.5, 7.5] | 2.5 7.5 | Yes | 7.17 |
| 2 | [3.0, 7.0] | 3.0 7.0 | Yes | 4.14 |
| 3 | [3.8, 6.2] | 6.2 3.8 | Yes | 6.01 |
| 4 | [2.8, 7.2] | 2.8 7.2 | Yes | 4.58 |
| 5 | [4.5, 5.5] | 4.5 5.5 | Yes | 3.8 |
| 6 | [1.2, 8.8] | 8.8 1.2 | Yes | 9.24 |
| 7 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.64 |
| 8 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.43 |
| 9 | [2.0, 8.0] | 8.0 2.0 | Yes | 7.67 |
| 10 | [2.5, 7.5] | 7.5 2.5 | Yes | 7.04 |
| 11 | [3.1, 6.9] | 3.1 6.9 | Yes | 5.65 |
| 12 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.57 |
| 13 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.81 |
| 14 | [4.4, 5.6] | 5.6 4.4 | Yes | 7.05 |
| 15 | [1.3, 8.7] | 8.7 1.3 | Yes | 5.96 |
| 16 | [4.8, 5.2] | 4.8 5.2 | Yes | 7.62 |
| 17 | [2.2, 7.8] | 7.8 2.2 | Yes | 4.99 |
| 18 | [0.1, 9.9] | 0.1 9.9 | Yes | 6.75 |
| 19 | [0.8, 9.2] | 9.2 0.8 | Yes | 7.2 |
| 20 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.35 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | Y1NKE73K0GWG | Y1NKE73K0GWG | Yes | 4.29 |
| 2 | MT0T15R1NKEQ | MT0T15R1NKEQ | Yes | 3.52 |
| 3 | 1IMGZWH79PJF | 1IMGZWH79PJF | Yes | 3.81 |
| 4 | G0V4AT3MDWW2 | GOV4AT3MDWW2 | No | 3.55 |
| 5 | BOT1H5D3Y47R | BOT1H5D3Y47R | Yes | 3.13 |
| 6 | 29M7KTLEFJ1J | 29M7KTLEFJ1J | Yes | 3.76 |
| 7 | PZZKM15870DY | PZZKM15870DY | Yes | 3.97 |
| 8 | IS15PME9F5ZM | IS15PME9F5ZM | Yes | 2.97 |
| 9 | W3Q97LSB259O | W3Q97LSB259O | Yes | 4.24 |
| 10 | 7WFFIXYM0VKV | 7WFFIXYMOVKV | No | 3.19 |
| 11 | EMK96M7WWJ3Z | EMK96M7WWJ3Z | Yes | 3.4 |
| 12 | HJSGE7EYMSPT | HJSGE7EYMSPT | Yes | 3.12 |
| 13 | B7AFGS9ADK09 | B7AFGS9ADK09 | Yes | 3.13 |
| 14 | AWAC9DFWSPZV | AWAC9DFWSPZV | Yes | 4.27 |
| 15 | 51ZG02FQXEQ1 | 51ZG02FQXEQ1 | Yes | 3.15 |
| 16 | SG1ZVOT2N1XQ | SG1ZVOT2N1XQ | Yes | 3.1 |
| 17 | V852NDNDYMHM | V852NDNDYMHM | Yes | 4.29 |
| 18 | Z0XY7WRWKZGK | ZOXY7WRWKZGK | No | 4.22 |
| 19 | D3MMB5WY72T6 | D3MMB5WY72T6 | Yes | 3.15 |
| 20 | S64WL3RPHTZJ | S64WL3RPHTZJ | Yes | 4.15 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4096 | 4096 | Yes | 13.14 |
| 2 | 39 | 39 | Yes | 4.06 |
| 3 | 28 | 28 | Yes | 3.7 |
| 4 | 3 | 3 | Yes | 7.11 |
| 5 | 67 | 67 | Yes | 2.82 |
| 6 | 64 | 64 | Yes | 5.6 |
| 7 | 5 | 5 | Yes | 4.6 |
| 8 | 60 | 60 | Yes | 3.83 |
| 9 | 20 | 20 | Yes | 10.54 |
| 10 | 60 | 60 | Yes | 4.04 |
| 11 | 9 | 9 | Yes | 4.49 |
| 12 | 65 | 65 | Yes | 4.41 |
| 13 | 4 | 4 | Yes | 5.33 |
| 14 | 243 | 243 | Yes | 3.09 |
| 15 | 9 | 9 | Yes | 5.17 |
| 16 | 4 | 4 | Yes | 2.89 |
| 17 | 1440 | 1440 | Yes | 4.08 |
| 18 | 10 | 10 | Yes | 4.88 |
| 19 | 63 | 63 | Yes | 4.11 |
| 20 | 793 | 793 | Yes | 3.1 |
