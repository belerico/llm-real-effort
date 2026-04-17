# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-19 03:07:05

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

**Model-specific overrides:**
- temperature: `None`

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
| sudoku_game | 8280 | 40960 | 49240 | 0 | 20 | 66.59 | 1331.89 |
| add_numbers | 7300 | 3975 | 11275 | 20 | 0 | 6.59 | 131.85 |
| counting_zeros | 7360 | 40960 | 48320 | 0 | 20 | 72.71 | 1454.47 |
| task_decoding | 10620 | 14100 | 24720 | 20 | 0 | 13.33 | 266.84 |
| task_summation | 7620 | 21507 | 29127 | 20 | 0 | 16.46 | 329.42 |
| task_transcription | 7380 | 17155 | 24535 | 16 | 4 | 17.86 | 357.37 |
| task_sequences | 3079 | 8688 | 11767 | 18 | 2 | 17.62 | 352.41 |
| **TOTAL** | **51639** | **147345** | **198984** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 3 2 5 6 4 3 1 5 6 2 5 4 |  | No | 57.98 |
| 2 | 3 6 1 4 4 5 3 4 3 6 4 6 3 4 |  | No | 57.56 |
| 3 | 1 6 5 6 6 3 2 5 1 4 5 6 3 5 |  | No | 61.15 |
| 4 | 3 6 5 4 1 2 5 5 2 5 2 4 6 4 |  | No | 66.66 |
| 5 | 5 4 5 6 4 1 5 4 3 2 6 6 4 3 |  | No | 56.34 |
| 6 | 2 1 4 6 2 1 1 4 3 5 2 5 6 2 |  | No | 73.48 |
| 7 | 3 1 4 1 3 2 5 4 2 5 6 3 1 2 |  | No | 53.2 |
| 8 | 6 4 5 3 6 1 4 5 1 6 4 2 5 4 |  | No | 62.02 |
| 9 | 4 1 3 5 1 3 3 5 4 6 2 4 2 5 |  | No | 61.61 |
| 10 | 1 2 3 4 2 6 5 5 2 6 3 4 6 1 |  | No | 79.29 |
| 11 | 6 5 6 2 1 3 1 5 4 6 4 2 5 4 |  | No | 79.63 |
| 12 | 2 4 3 1 2 5 5 1 6 1 2 4 1 2 |  | No | 70.27 |
| 13 | 6 3 4 1 2 1 5 6 3 4 5 6 3 1 |  | No | 59.24 |
| 14 | 2 5 6 4 1 6 1 5 2 1 4 3 3 2 |  | No | 51.95 |
| 15 | 2 4 6 5 2 3 1 5 3 4 1 3 6 4 |  | No | 61.46 |
| 16 | 4 5 3 2 1 2 5 1 6 6 5 4 3 2 |  | No | 87.55 |
| 17 | 6 2 2 6 4 3 5 1 4 1 2 6 5 4 |  | No | 74.81 |
| 18 | 3 2 4 6 2 1 3 1 1 2 6 5 4 3 |  | No | 76.8 |
| 19 | 2 4 6 4 3 2 5 2 3 6 6 5 2 4 |  | No | 70.18 |
| 20 | 6 4 1 3 3 6 6 3 1 2 1 5 2 6 |  | No | 70.52 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1556 | 1556 | Yes | 6.67 |
| 2 | 1374 | 1374 | Yes | 2.77 |
| 3 | 1257 | 1257 | Yes | 6.38 |
| 4 | 1365 | 1365 | Yes | 6.03 |
| 5 | 2019 | 2019 | Yes | 9.96 |
| 6 | 1438 | 1438 | Yes | 9.71 |
| 7 | 1477 | 1477 | Yes | 7.76 |
| 8 | 1187 | 1187 | Yes | 6.55 |
| 9 | 1560 | 1560 | Yes | 6.61 |
| 10 | 2090 | 2090 | Yes | 3.27 |
| 11 | 1807 | 1807 | Yes | 4.5 |
| 12 | 1516 | 1516 | Yes | 10.42 |
| 13 | 1599 | 1599 | Yes | 7.27 |
| 14 | 2456 | 2456 | Yes | 8.27 |
| 15 | 2033 | 2033 | Yes | 5.22 |
| 16 | 819 | 819 | Yes | 5.45 |
| 17 | 2250 | 2250 | Yes | 7.24 |
| 18 | 2054 | 2054 | Yes | 5.74 |
| 19 | 1696 | 1696 | Yes | 6.08 |
| 20 | 1128 | 1128 | Yes | 5.84 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 |  | No | 74.49 |
| 2 | 46 |  | No | 71.9 |
| 3 | 42 |  | No | 71.29 |
| 4 | 43 |  | No | 75.91 |
| 5 | 70 |  | No | 77.83 |
| 6 | 71 |  | No | 96.28 |
| 7 | 59 |  | No | 73.12 |
| 8 | 39 |  | No | 76.1 |
| 9 | 60 |  | No | 67.52 |
| 10 | 51 |  | No | 67.79 |
| 11 | 56 |  | No | 77.56 |
| 12 | 48 |  | No | 68.17 |
| 13 | 61 |  | No | 74.1 |
| 14 | 61 |  | No | 76.2 |
| 15 | 73 |  | No | 58.02 |
| 16 | 37 |  | No | 68.97 |
| 17 | 52 |  | No | 72.52 |
| 18 | 55 |  | No | 72.96 |
| 19 | 56 |  | No | 66.37 |
| 20 | 75 |  | No | 67.05 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JUCBOLX | JUCBOLX | Yes | 17.34 |
| 2 | EWPDRCJ | EWPDRCJ | Yes | 9.51 |
| 3 | FEBHWQX | FEBHWQX | Yes | 13.43 |
| 4 | XQCHMWD | XQCHMWD | Yes | 9.57 |
| 5 | SXIPFVC | SXIPFVC | Yes | 13.06 |
| 6 | JDUZCWP | JDUZCWP | Yes | 15.46 |
| 7 | LBPADJR | LBPADJR | Yes | 9.11 |
| 8 | MBSUPEQ | MBSUPEQ | Yes | 12.93 |
| 9 | ROZJTME | ROZJTME | Yes | 7.69 |
| 10 | OSEWAVY | OSEWAVY | Yes | 11.33 |
| 11 | RZVDOTC | RZVDOTC | Yes | 11.47 |
| 12 | ROQDYZB | ROQDYZB | Yes | 18.29 |
| 13 | PTGJNFV | PTGJNFV | Yes | 11.86 |
| 14 | XOLRHFB | XOLRHFB | Yes | 10.73 |
| 15 | BDXCRLE | BDXCRLE | Yes | 12.03 |
| 16 | RYPLEUH | RYPLEUH | Yes | 17.19 |
| 17 | EXZURNQ | EXZURNQ | Yes | 21.04 |
| 18 | UFAWYCO | UFAWYCO | Yes | 9.88 |
| 19 | PTUEOKV | PTUEOKV | Yes | 11.93 |
| 20 | WOHBKXM | WOHBKXM | Yes | 22.78 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.8, 7.2] | 7.2 2.8 | Yes | 18.44 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 15.76 |
| 3 | [3.6, 6.4] | 6.4 3.6 | Yes | 12.0 |
| 4 | [3.1, 6.9] | 3.1 6.9 | Yes | 26.34 |
| 5 | [1.4, 8.6] | 1.4 8.6 | Yes | 20.29 |
| 6 | [3.4, 6.6] | 3.4 6.6 | Yes | 15.12 |
| 7 | [1.0, 9.0] | 9.0 1.0 | Yes | 12.22 |
| 8 | [0.3, 9.7] | 0.3 9.7 | Yes | 16.61 |
| 9 | [0.1, 9.9] | 0.1 9.9 | Yes | 14.67 |
| 10 | [4.3, 5.7] | 4.3 5.7 | Yes | 12.71 |
| 11 | [3.4, 6.6] | 3.4 6.6 | Yes | 12.01 |
| 12 | [1.2, 8.8] | 1.2 8.8 | Yes | 18.05 |
| 13 | [2.7, 7.3] | 7.3 2.7 | Yes | 22.99 |
| 14 | [2.9, 7.1] | 2.9 7.1 | Yes | 20.43 |
| 15 | [3.0, 7.0] | 3.0 7.0 | Yes | 10.25 |
| 16 | [1.8, 8.2] | 8.2 1.8 | Yes | 15.46 |
| 17 | [2.2, 7.8] | 2.2 7.8 | Yes | 19.61 |
| 18 | [3.9, 6.1] | 3.9 6.1 | Yes | 16.99 |
| 19 | [4.9, 5.1] | 4.9 5.1 | Yes | 16.36 |
| 20 | [2.9, 7.1] | 7.1 2.9 | Yes | 12.9 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | X2TWBL6KDBZQ | X2TWBL6KDBZQ | Yes | 18.17 |
| 2 | D80TQW8QNUM6 |  | No | 63.42 |
| 3 | QALUT157RP4W | QALUT157RP4W | Yes | 8.26 |
| 4 | U9TZJO5BV3R0 | U9TZJO5BV3R0 | Yes | 22.81 |
| 5 | XJDWJ3IAH2Z3 | XJDWJ3IAH2Z3 | Yes | 10.24 |
| 6 | KRNM09TCX684 | KRNM09TCX684 | Yes | 17.06 |
| 7 | QWJXTLFQL5HS | QWJXTLFQL5HS | Yes | 9.26 |
| 8 | WJ6AXSRB6JOE | WJ6AXSRB6JOE | Yes | 18.66 |
| 9 | 2QZBF6HGSZFT | 2QZBF6HGSZFT | Yes | 10.8 |
| 10 | O0GG10ZONT3V | 00GG10ZONT3V | No | 25.76 |
| 11 | OPLOHDE1KFTU | OPLOHDE1KFTU | Yes | 11.13 |
| 12 | SZQKQQEWC3C9 | SZAKQQEWC3C9 | No | 19.98 |
| 13 | ZXH5KB88YD3M | ZXH5KB88YD9M | No | 11.06 |
| 14 | YCVHBW8PECX1 | YCVHBW8PECX1 | Yes | 9.38 |
| 15 | OO446WRV8IGS | OO446WRV8IGS | Yes | 19.1 |
| 16 | K6C6RHUCKUBU | K6C6RHUCKUBU | Yes | 23.39 |
| 17 | 22GHISBK737J | 22GHISBK737J | Yes | 13.9 |
| 18 | FWQYERGJU1UV | FWQYERGJU1UV | Yes | 8.84 |
| 19 | FGT2WIJXPCI6 | FGT2WIJXPCI6 | Yes | 14.86 |
| 20 | GZRPOSS01PFA | GZRPOSS01PFA | Yes | 21.16 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 8.39 |
| 2 | 39 | 39 | Yes | 8.74 |
| 3 | 23 | 23 | Yes | 4.43 |
| 4 | 60 | 60 | Yes | 9.85 |
| 5 | 243 | 243 | Yes | 4.53 |
| 6 | 63 | 63 | Yes | 11.43 |
| 7 | 3 | 3 | Yes | 11.26 |
| 8 | 3 | TIMEOUT | No | 120.02 |
| 9 | 73 | 73 | Yes | 7.06 |
| 10 | 793 | 793 | Yes | 5.61 |
| 11 | 1 | 1 | Yes | 4.42 |
| 12 | 44 | 44 | Yes | 25.16 |
| 13 | 4096 |  | No | 58.51 |
| 14 | 64 | 64 | Yes | 9.72 |
| 15 | 28 | 28 | Yes | 15.36 |
| 16 | 60 | 60 | Yes | 17.34 |
| 17 | 4 | 4 | Yes | 5.33 |
| 18 | 16 | 16 | Yes | 12.6 |
| 19 | 67 | 67 | Yes | 3.92 |
| 20 | 36 | 36 | Yes | 8.71 |
