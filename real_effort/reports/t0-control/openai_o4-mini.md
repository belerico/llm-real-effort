# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-19 10:21:30

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
| sudoku_game | 8240 | 40960 | 49200 | 0 | 20 | 36.78 | 735.83 |
| add_numbers | 3760 | 4453 | 8213 | 20 | 0 | 3.59 | 71.91 |
| counting_zeros | 7180 | 40960 | 48140 | 0 | 20 | 34.06 | 681.42 |
| task_decoding | 15220 | 28045 | 43265 | 15 | 5 | 24.09 | 482.02 |
| task_summation | 8440 | 18932 | 27372 | 20 | 0 | 13.08 | 261.69 |
| task_transcription | 3470 | 7534 | 11004 | 17 | 3 | 4.83 | 96.7 |
| task_sequences | 2420 | 11601 | 14021 | 18 | 2 | 13.30 | 266.02 |
| **TOTAL** | **48730** | **152485** | **201215** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 2 1 4 3 6 4 5 3 2 6 2 3 |  | No | 42.99 |
| 2 | 2 3 3 1 4 6 3 5 4 6 3 5 3 1 |  | No | 29.34 |
| 3 | 3 2 6 3 4 1 4 1 3 1 2 3 6 5 |  | No | 48.27 |
| 4 | 2 2 3 6 4 6 6 4 2 3 4 2 6 5 |  | No | 26.2 |
| 5 | 4 1 6 5 6 3 6 5 3 1 4 3 2 4 |  | No | 48.57 |
| 6 | 5 4 4 6 6 5 3 4 6 6 1 5 4 2 |  | No | 35.06 |
| 7 | 2 1 2 5 3 6 4 2 5 6 1 3 5 3 |  | No | 34.18 |
| 8 | 5 1 3 6 6 1 3 2 3 3 1 3 6 2 |  | No | 36.65 |
| 9 | 1 4 6 2 5 6 4 1 5 2 5 1 5 3 |  | No | 19.39 |
| 10 | 1 2 3 2 3 6 1 5 1 3 2 6 1 3 |  | No | 27.48 |
| 11 | 6 1 6 3 6 4 6 3 1 6 5 4 1 6 |  | No | 42.51 |
| 12 | 2 3 2 6 1 6 2 3 4 6 5 5 6 2 |  | No | 45.93 |
| 13 | 3 2 6 2 2 3 2 1 6 6 4 6 3 1 |  | No | 36.18 |
| 14 | 2 5 6 2 2 4 2 5 3 2 4 1 2 1 |  | No | 41.79 |
| 15 | 5 3 6 2 5 3 2 3 1 2 1 3 5 2 |  | No | 37.34 |
| 16 | 6 4 1 2 1 4 5 3 6 4 1 3 5 6 |  | No | 30.55 |
| 17 | 1 2 6 3 2 1 4 4 5 3 6 1 2 2 |  | No | 38.16 |
| 18 | 5 6 4 4 2 2 6 4 2 6 4 5 1 4 |  | No | 41.36 |
| 19 | 2 6 5 6 1 4 3 1 5 5 3 2 3 5 |  | No | 51.49 |
| 20 | 1 2 4 5 6 6 2 5 5 2 6 6 1 2 |  | No | 22.16 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1159 | 1159 | Yes | 2.49 |
| 2 | 1238 | 1238 | Yes | 4.08 |
| 3 | 2386 | 2386 | Yes | 2.65 |
| 4 | 1308 | 1308 | Yes | 4.66 |
| 5 | 1602 | 1602 | Yes | 2.86 |
| 6 | 1925 | 1925 | Yes | 5.45 |
| 7 | 1373 | 1373 | Yes | 4.45 |
| 8 | 2036 | 2036 | Yes | 2.5 |
| 9 | 1737 | 1737 | Yes | 2.16 |
| 10 | 1635 | 1635 | Yes | 3.13 |
| 11 | 1801 | 1801 | Yes | 2.79 |
| 12 | 1483 | 1483 | Yes | 3.37 |
| 13 | 1644 | 1644 | Yes | 2.3 |
| 14 | 2645 | 2645 | Yes | 3.3 |
| 15 | 894 | 894 | Yes | 2.43 |
| 16 | 1494 | 1494 | Yes | 5.37 |
| 17 | 2009 | 2009 | Yes | 4.8 |
| 18 | 1834 | 1834 | Yes | 4.66 |
| 19 | 1481 | 1481 | Yes | 2.89 |
| 20 | 1012 | 1012 | Yes | 5.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 42 |  | No | 50.91 |
| 2 | 44 |  | No | 33.14 |
| 3 | 66 |  | No | 21.08 |
| 4 | 55 |  | No | 41.19 |
| 5 | 69 |  | No | 22.02 |
| 6 | 68 |  | No | 39.81 |
| 7 | 62 |  | No | 35.7 |
| 8 | 51 |  | No | 32.97 |
| 9 | 37 |  | No | 50.37 |
| 10 | 65 |  | No | 16.78 |
| 11 | 35 |  | No | 28.36 |
| 12 | 59 |  | No | 26.52 |
| 13 | 53 |  | No | 32.47 |
| 14 | 64 |  | No | 34.37 |
| 15 | 64 |  | No | 29.3 |
| 16 | 39 |  | No | 34.61 |
| 17 | 54 |  | No | 46.96 |
| 18 | 56 |  | No | 28.35 |
| 19 | 58 |  | No | 47.16 |
| 20 | 45 |  | No | 29.11 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KHIGDMQ |  | No | 47.53 |
| 2 | DLONYFM |  | No | 33.76 |
| 3 | GVRUDXP | GVRUDXP | Yes | 11.85 |
| 4 | AXIUSHN | AXIUSHN | Yes | 18.89 |
| 5 | VITPMXO | VITPMXO | Yes | 47.65 |
| 6 | VTILJUW | VTILJUW | Yes | 12.76 |
| 7 | VDOCWEH |  | No | 55.39 |
| 8 | YWHUVFM | YWHUVFM | Yes | 15.58 |
| 9 | LQBPZGX | LQBPZGX | Yes | 9.51 |
| 10 | EDPFXRI |  | No | 50.89 |
| 11 | LHEYUKC | LHEYUKC | Yes | 19.5 |
| 12 | OSBEVCM | OSBEVCM | Yes | 9.72 |
| 13 | BKXQRYW | BKXQRYW | Yes | 7.34 |
| 14 | CYNAVJR | CYNAVJR | Yes | 9.79 |
| 15 | XIAENVM | XIAENVM | Yes | 7.33 |
| 16 | FYCAZED | FYCAZED | Yes | 13.14 |
| 17 | BLIGRNU | BLIGRNU | Yes | 18.38 |
| 18 | OJKYPEH | OJKYPEH | Yes | 20.88 |
| 19 | NFIYUED |  | No | 55.08 |
| 20 | LUJPNBH | LUJPNBH | Yes | 16.85 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 3.9 6.1 | Yes | 10.64 |
| 2 | [0.9, 9.1] | 0.9 9.1 | Yes | 17.76 |
| 3 | [3.4, 6.6] | 3.4 6.6 | Yes | 11.27 |
| 4 | [2.5, 7.5] | 2.5 7.5 | Yes | 7.83 |
| 5 | [1.6, 8.4] | 8.4 1.6 | Yes | 12.13 |
| 6 | [0.6, 9.4] | 9.4 0.6 | Yes | 17.01 |
| 7 | [3.4, 6.6] | 3.4 6.6 | Yes | 12.54 |
| 8 | [0.5, 9.5] | 0.5 9.5 | Yes | 9.92 |
| 9 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.78 |
| 10 | [0.7, 9.3] | 0.7 9.3 | Yes | 13.54 |
| 11 | [3.7, 6.3] | 3.7 6.3 | Yes | 15.23 |
| 12 | [1.7, 8.3] | 1.7 8.3 | Yes | 11.19 |
| 13 | [4.1, 5.9] | 4.1 5.9 | Yes | 11.13 |
| 14 | [2.8, 7.2] | 7.2 2.8 | Yes | 10.03 |
| 15 | [0.5, 9.5] | 0.5 9.5 | Yes | 14.4 |
| 16 | [4.8, 5.2] | 5.2 4.8 | Yes | 12.54 |
| 17 | [3.0, 7.0] | 3.0 7.0 | Yes | 14.8 |
| 18 | [1.6, 8.4] | 1.6 8.4 | Yes | 13.9 |
| 19 | [3.3, 6.7] | 3.3 6.7 | Yes | 15.01 |
| 20 | [1.5, 8.5] | 1.5 8.5 | Yes | 19.86 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5K1XCD8A2KLU | 5K1XCD8A2KLU | Yes | 2.81 |
| 2 | GGW811LUJ8RN | GGW811LUJ8RN | Yes | 3.85 |
| 3 | NO2BQ316PKND | NO2BQ316PKND | Yes | 4.32 |
| 4 | 6WHVPV8QQNON | 6WHVPV8QQNON | Yes | 2.87 |
| 5 | EGRVGLCBJJ90 | EGRVGLCBJJ90 | Yes | 1.99 |
| 6 | LZ9INK9GNV64 | LZ9INK9GNV64 | Yes | 2.94 |
| 7 | FP8PP011QDJY | FP8PP011QD JY | No | 8.29 |
| 8 | VTZRGJJKGMNF | VTZRGJJKGMNF | Yes | 2.49 |
| 9 | DP4R0P4KIDBL | DP4R0P4KIDBL | Yes | 4.48 |
| 10 | GFAMCMD1DHDM | GFAMCMD1DHDM | Yes | 3.26 |
| 11 | H4BNSR66HGCA | H4BNSR66H GCA | No | 12.75 |
| 12 | F2ME2DDL3BZT | F2ME2DDL3BZT | Yes | 2.96 |
| 13 | ATXICJJ7DVCX | ATXICJJ7DVCX | Yes | 3.37 |
| 14 | 4329AGMHWP6W | 4329AGMHWP6W | Yes | 19.53 |
| 15 | AD9QI4ONNTFM | AD9QI4ONNTFM | Yes | 3.12 |
| 16 | 6MH7VNP3S0JH | 6MH7VNP3S0JH | Yes | 3.01 |
| 17 | 6FUDQS75P8U3 | 6FUDQS75P8U3 | Yes | 2.31 |
| 18 | LAOEMCRAYHER | LAOEMCRAYHER | Yes | 3.31 |
| 19 | 2FCMUBSROR7Q | 2FCMUBSR0R7Q | No | 4.93 |
| 20 | BVY6TEEV75LX | BVY6TEEV75LX | Yes | 3.98 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 7.58 |
| 2 | 5 |  | No | 40.37 |
| 3 | 7 | 7 | Yes | 3.88 |
| 4 | 64 | 64 | Yes | 12.68 |
| 5 | 7680 | 7680 | Yes | 7.48 |
| 6 | 48 | 48 | Yes | 19.1 |
| 7 | 4 | 4 | Yes | 5.84 |
| 8 | 28 | 28 | Yes | 5.43 |
| 9 | 36 | 36 | Yes | 5.18 |
| 10 | 31 | 31 | Yes | 6.39 |
| 11 | 3 | 3 | Yes | 10.38 |
| 12 | 67 | 67 | Yes | 3.05 |
| 13 | 9 | 9 | Yes | 22.87 |
| 14 | 4 | 4 | Yes | 62.63 |
| 15 | 5 | 5 | Yes | 9.33 |
| 16 | 19 | 19 | Yes | 11.87 |
| 17 | 60 | 60 | Yes | 3.32 |
| 18 | 39 | 42 | No | 15.76 |
| 19 | 1440 | 1440 | Yes | 8.6 |
| 20 | 243 | 243 | Yes | 4.27 |
