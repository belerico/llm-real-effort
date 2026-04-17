# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 8740 | 38839 | 47579 | 8 | 12 | 25.16 | 503.31 |
| add_numbers | 4660 | 4059 | 8719 | 20 | 0 | 4.94 | 98.86 |
| counting_zeros | 7600 | 34470 | 42070 | 14 | 6 | 18.64 | 373.2 |
| task_decoding | 14040 | 5460 | 19500 | 20 | 0 | 5.37 | 107.62 |
| task_summation | 7960 | 15304 | 23264 | 20 | 0 | 10.73 | 214.86 |
| task_transcription | 4792 | 3632 | 8424 | 18 | 2 | 4.24 | 84.91 |
| task_sequences | 3920 | 7516 | 11436 | 19 | 1 | 5.93 | 118.55 |
| **TOTAL** | **51712** | **109280** | **160992** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 6 2 4 1 3 4 1 2 2 3 1 4 |  | No | 23.1 |
| 2 | 3 4 5 5 4 5 3 5 1 3 6 6 1 2 | 3 4 5 5 4 5 3 5 1 3 | No | 25.44 |
| 3 | 5 1 5 4 6 5 6 4 2 5 2 6 3 4 | 5 1 5 4 6 5 6 4 2 5 2 6 3 4 | Yes | 22.33 |
| 4 | 3 1 6 2 3 2 4 1 5 4 6 1 4 2 | 3 1 6 2 3 2 4 1 5 4 6 1 4 2 | Yes | 23.83 |
| 5 | 5 3 6 6 5 2 3 6 5 4 2 6 6 4 | 5 3 6 6 5 2 3 6 5 4 2 6 6 4 | Yes | 24.72 |
| 6 | 3 1 5 2 6 3 1 4 6 4 1 6 5 2 |  | No | 26.52 |
| 7 | 6 2 5 5 2 2 4 5 1 3 6 6 4 2 |  | No | 26.13 |
| 8 | 6 5 1 5 3 3 5 4 2 4 1 4 1 2 |  | No | 25.01 |
| 9 | 1 3 4 6 5 4 3 6 2 6 1 3 5 6 |  | No | 25.35 |
| 10 | 3 1 6 1 6 5 1 5 3 2 5 6 2 5 | 6 1 3 1 5 6 1 3 5 2 5 6 2 5 | No | 28.74 |
| 11 | 1 2 4 1 2 4 1 2 4 3 6 3 5 1 |  | No | 28.94 |
| 12 | 5 1 4 2 4 1 3 1 5 6 3 2 3 2 | 5 1 4 2 4 1 3 1 5 6 3 2 3 2 | Yes | 21.07 |
| 13 | 4 2 2 4 3 1 5 4 6 1 4 4 3 5 |  | No | 25.67 |
| 14 | 1 6 4 4 1 3 5 3 5 4 4 3 4 5 | 1 6 4 4 1 3 5 3 5 4 4 3 4 5 | Yes | 25.13 |
| 15 | 5 6 1 2 2 3 1 6 3 6 4 6 1 1 | 5 6 1 2 2 3 1 6 3 6 4 6 1 1 | Yes | 23.09 |
| 16 | 2 6 1 1 3 6 4 3 2 3 5 4 2 1 | 2 6 1 1 3 6 4 3 2 3 5 2 1 | No | 27.6 |
| 17 | 3 4 3 1 5 4 5 6 3 6 2 3 4 1 |  | No | 25.76 |
| 18 | 5 3 6 2 2 4 6 1 1 4 6 5 6 5 | 5 3 6 2 2 4 6 1 1 4 6 5 6 5 | Yes | 27.63 |
| 19 | 2 6 3 5 2 1 6 1 4 2 4 6 3 3 | 2 6 3 5 | No | 24.82 |
| 20 | 1 6 1 2 6 3 6 1 4 3 3 6 2 4 | 1 6 1 2 6 3 6 1 4 3 3 6 2 4 | Yes | 22.26 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1055 | 1055 | Yes | 3.06 |
| 2 | 2098 | 2098 | Yes | 4.21 |
| 3 | 1298 | 1298 | Yes | 3.91 |
| 4 | 836 | 836 | Yes | 4.62 |
| 5 | 888 | 888 | Yes | 12.48 |
| 6 | 1307 | 1307 | Yes | 4.89 |
| 7 | 1673 | 1673 | Yes | 4.43 |
| 8 | 719 | 719 | Yes | 3.88 |
| 9 | 1788 | 1788 | Yes | 4.02 |
| 10 | 1247 | 1247 | Yes | 3.62 |
| 11 | 2379 | 2379 | Yes | 5.47 |
| 12 | 1493 | 1493 | Yes | 4.58 |
| 13 | 1137 | 1137 | Yes | 4.28 |
| 14 | 2426 | 2426 | Yes | 4.7 |
| 15 | 1431 | 1431 | Yes | 5.19 |
| 16 | 1343 | 1343 | Yes | 5.07 |
| 17 | 1881 | 1881 | Yes | 5.62 |
| 18 | 1730 | 1730 | Yes | 4.4 |
| 19 | 996 | 996 | Yes | 4.98 |
| 20 | 1725 | 1725 | Yes | 5.36 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 37 | No | 21.64 |
| 2 | 41 | 41 | Yes | 18.42 |
| 3 | 55 | 55 | Yes | 20.2 |
| 4 | 46 | 43 | No | 10.59 |
| 5 | 38 | 38 | Yes | 14.93 |
| 6 | 57 | 57 | Yes | 19.56 |
| 7 | 51 | 51 | Yes | 22.59 |
| 8 | 35 | 35 | Yes | 15.86 |
| 9 | 68 | 68 | Yes | 18.29 |
| 10 | 36 | 36 | Yes | 16.95 |
| 11 | 49 | 49 | Yes | 19.6 |
| 12 | 49 | 48 | No | 11.83 |
| 13 | 60 | 60 | Yes | 19.27 |
| 14 | 38 | 39 | No | 16.06 |
| 15 | 70 | 70 | Yes | 20.31 |
| 16 | 74 | 73 | No | 20.82 |
| 17 | 64 | 64 | Yes | 22.35 |
| 18 | 72 | 69 | No | 16.22 |
| 19 | 64 | 64 | Yes | 17.84 |
| 20 | 57 | 57 | Yes | 29.53 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CFMSGJI | CFMSGJI | Yes | 5.13 |
| 2 | PKADTHR | PKADTHR | Yes | 5.09 |
| 3 | HFDJOEK | HFDJOEK | Yes | 7.55 |
| 4 | YEJKABQ | YEJKABQ | Yes | 4.71 |
| 5 | WFEGCUD | WFEGCUD | Yes | 4.85 |
| 6 | GADIMUR | GADIMUR | Yes | 4.87 |
| 7 | SJWNKOF | SJWNKOF | Yes | 4.91 |
| 8 | MWNTFAH | MWNTFAH | Yes | 5.45 |
| 9 | IDZBLKP | IDZBLKP | Yes | 4.7 |
| 10 | NMADQPW | NMADQPW | Yes | 4.93 |
| 11 | XEDLVJN | XEDLVJN | Yes | 5.46 |
| 12 | UKVAMLX | UKVAMLX | Yes | 5.19 |
| 13 | NUIZEMJ | NUIZEMJ | Yes | 5.78 |
| 14 | GUXAYIR | GUXAYIR | Yes | 5.24 |
| 15 | OFYIVDH | OFYIVDH | Yes | 6.18 |
| 16 | QXILCZP | QXILCZP | Yes | 4.83 |
| 17 | BTSZOQJ | BTSZOQJ | Yes | 6.23 |
| 18 | CGIATJR | CGIATJR | Yes | 6.44 |
| 19 | CWBJXLU | CWBJXLU | Yes | 4.87 |
| 20 | VCTDMIZ | VCTDMIZ | Yes | 4.98 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.7, 8.3] | 8.3 1.7 | Yes | 10.24 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 12.05 |
| 3 | [2.5, 7.5] | 2.5 7.5 | Yes | 10.52 |
| 4 | [1.9, 8.1] | 8.1 1.9 | Yes | 11.02 |
| 5 | [2.2, 7.8] | 2.2 7.8 | Yes | 9.35 |
| 6 | [1.3, 8.7] | 8.7 1.3 | Yes | 12.07 |
| 7 | [4.3, 5.7] | 4.3 5.7 | Yes | 10.85 |
| 8 | [0.1, 9.9] | 9.9 0.1 | Yes | 9.53 |
| 9 | [4.1, 5.9] | 5.9 4.1 | Yes | 9.78 |
| 10 | [3.4, 6.6] | 6.6 3.4 | Yes | 9.67 |
| 11 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.59 |
| 12 | [4.3, 5.7] | 4.3 5.7 | Yes | 13.22 |
| 13 | [0.5, 9.5] | 9.5 0.5 | Yes | 10.1 |
| 14 | [0.3, 9.7] | 9.7 0.3 | Yes | 10.43 |
| 15 | [2.9, 7.1] | 2.9 7.1 | Yes | 9.74 |
| 16 | [1.6, 8.4] | 1.6 8.4 | Yes | 10.57 |
| 17 | [0.7, 9.3] | 0.7 9.3 | Yes | 10.52 |
| 18 | [1.3, 8.7] | 1.3 8.7 | Yes | 14.52 |
| 19 | [2.8, 7.2] | 7.2 2.8 | Yes | 11.42 |
| 20 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.45 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 91E3YJGY9OZT | 91E3YJGY90ZT | No | 4.56 |
| 2 | XCJXQE3LIAD6 | XCJXQE3LIAD6 | Yes | 4.7 |
| 3 | 7IKAPK4RVYNJ | 7IKAPK4RVYNJ | Yes | 4.15 |
| 4 | SUJC6BDWKUT4 | SUJC6BDWKUT4 | Yes | 3.83 |
| 5 | XMXQ340R327V | XMXQ340R327V | Yes | 5.5 |
| 6 | 9YYULWYVK2J6 | 9YYULWYVK2JG | No | 4.23 |
| 7 | ZHA9S160NFO0 | ZHA9S160NFO0 | Yes | 4.91 |
| 8 | MMMI8FXBHH16 | MMMI8FXBHH16 | Yes | 3.33 |
| 9 | OXNE7N9W9BC5 | OXNE7N9W9BC5 | Yes | 4.05 |
| 10 | IIX2AHPFOMYP | IIX2AHPFOMYP | Yes | 3.54 |
| 11 | 0HY8NNWN288I | 0HY8NNWN288I | Yes | 6.45 |
| 12 | XTZ034B3PI6R | XTZ034B3PI6R | Yes | 3.71 |
| 13 | 06AHB3YHB7KD | 06AHB3YHB7KD | Yes | 4.03 |
| 14 | B5QG2G5DYDCZ | B5QG2G5DYDCZ | Yes | 4.02 |
| 15 | 17KDC4J33GJT | 17KDC4J33GJT | Yes | 4.37 |
| 16 | WHN6I483A1BP | WHN6I483A1BP | Yes | 3.87 |
| 17 | JD59F6BLL0T2 | JD59F6BLL0T2 | Yes | 4.42 |
| 18 | L9FBDB2AE9BF | L9FBDB2AE9BF | Yes | 3.6 |
| 19 | OYK2BFSNGB9Q | OYK2BFSNGB9Q | Yes | 3.4 |
| 20 | 3BLULGPX2TZL | 3BLULGPX2TZL | Yes | 4.13 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 16 | No | 19.42 |
| 2 | 1440 | 1440 | Yes | 4.41 |
| 3 | 64 | 64 | Yes | 5.77 |
| 4 | 9 | 9 | Yes | 3.8 |
| 5 | 39 | 39 | Yes | 4.47 |
| 6 | 23 | 23 | Yes | 4.35 |
| 7 | 20 | 20 | Yes | 9.99 |
| 8 | 5 | 5 | Yes | 5.26 |
| 9 | 9 | 9 | Yes | 6.49 |
| 10 | 3 | 3 | Yes | 6.03 |
| 11 | 4 | 4 | Yes | 6.88 |
| 12 | 28 | 28 | Yes | 4.61 |
| 13 | 7680 | 7680 | Yes | 4.89 |
| 14 | 63 | 63 | Yes | 3.11 |
| 15 | 243 | 243 | Yes | 3.56 |
| 16 | 19 | 19 | Yes | 3.75 |
| 17 | 3 | 3 | Yes | 9.15 |
| 18 | 48 | 48 | Yes | 3.81 |
| 19 | 4 | 4 | Yes | 4.57 |
| 20 | 31 | 31 | Yes | 4.21 |
