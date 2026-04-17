# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 7760 | 40960 | 48720 | 0 | 20 | 57.74 | 1154.89 |
| add_numbers | 6780 | 1328 | 8108 | 20 | 0 | 4.06 | 81.31 |
| counting_zeros | 6840 | 40960 | 47800 | 0 | 20 | 65.57 | 1311.81 |
| task_decoding | 10100 | 6415 | 16515 | 20 | 0 | 7.16 | 143.38 |
| task_summation | 7100 | 10133 | 17233 | 20 | 0 | 10.39 | 208.01 |
| task_transcription | 6860 | 3558 | 10418 | 17 | 3 | 4.31 | 86.44 |
| task_sequences | 2720 | 4054 | 6774 | 20 | 0 | 5.84 | 116.78 |
| **TOTAL** | **48160** | **107408** | **155568** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 4 5 3 6 6 5 3 1 4 5 3 3 |  | No | 47.95 |
| 2 | 1 4 6 3 2 3 5 4 6 2 5 4 3 5 |  | No | 52.34 |
| 3 | 3 6 6 2 1 4 3 1 5 4 4 3 4 6 |  | No | 37.99 |
| 4 | 1 3 5 2 4 1 3 1 6 4 1 2 5 2 |  | No | 32.01 |
| 5 | 5 3 1 4 2 6 6 3 5 2 5 6 2 1 |  | No | 56.8 |
| 6 | 3 4 2 1 1 4 2 1 6 4 6 3 1 2 |  | No | 65.97 |
| 7 | 4 1 2 5 3 5 4 2 2 1 3 5 3 2 |  | No | 43.51 |
| 8 | 5 6 6 3 5 6 2 5 2 6 4 4 3 1 |  | No | 57.03 |
| 9 | 2 5 4 5 3 5 6 3 4 6 3 6 5 2 |  | No | 67.17 |
| 10 | 3 1 6 2 5 1 6 1 2 6 3 5 2 6 |  | No | 62.22 |
| 11 | 2 5 3 6 3 5 4 5 3 2 6 2 4 5 |  | No | 61.86 |
| 12 | 5 2 6 1 5 4 3 6 4 1 5 2 6 1 |  | No | 49.83 |
| 13 | 3 6 2 3 2 6 4 6 2 5 3 5 4 5 |  | No | 79.31 |
| 14 | 5 3 4 4 3 3 5 6 4 1 6 1 5 2 |  | No | 67.41 |
| 15 | 2 5 6 6 1 3 1 3 2 5 5 2 1 6 |  | No | 58.76 |
| 16 | 2 3 1 4 2 6 1 4 6 3 6 2 4 1 |  | No | 71.76 |
| 17 | 2 1 6 5 4 1 1 3 2 1 2 3 2 3 |  | No | 38.59 |
| 18 | 2 5 1 6 3 4 2 4 6 6 5 5 3 4 |  | No | 76.82 |
| 19 | 5 4 2 1 2 4 1 4 6 2 6 2 4 3 |  | No | 62.54 |
| 20 | 2 5 6 4 3 2 1 4 1 6 3 2 4 3 |  | No | 64.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1461 | 1461 | Yes | 4.25 |
| 2 | 1195 | 1195 | Yes | 3.92 |
| 3 | 1172 | 1172 | Yes | 4.19 |
| 4 | 1948 | 1948 | Yes | 3.91 |
| 5 | 1330 | 1330 | Yes | 3.32 |
| 6 | 764 | 764 | Yes | 3.31 |
| 7 | 2381 | 2381 | Yes | 4.06 |
| 8 | 2161 | 2161 | Yes | 3.69 |
| 9 | 1199 | 1199 | Yes | 5.11 |
| 10 | 2032 | 2032 | Yes | 4.19 |
| 11 | 2522 | 2522 | Yes | 3.48 |
| 12 | 1255 | 1255 | Yes | 5.42 |
| 13 | 2013 | 2013 | Yes | 3.79 |
| 14 | 1942 | 1942 | Yes | 3.71 |
| 15 | 1239 | 1239 | Yes | 6.27 |
| 16 | 2087 | 2087 | Yes | 3.3 |
| 17 | 1892 | 1892 | Yes | 3.28 |
| 18 | 1244 | 1244 | Yes | 4.16 |
| 19 | 1949 | 1949 | Yes | 3.99 |
| 20 | 1530 | 1530 | Yes | 3.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 82.48 |
| 2 | 49 |  | No | 68.18 |
| 3 | 36 |  | No | 68.85 |
| 4 | 57 |  | No | 72.05 |
| 5 | 41 |  | No | 65.79 |
| 6 | 39 |  | No | 76.12 |
| 7 | 68 |  | No | 73.43 |
| 8 | 60 |  | No | 78.68 |
| 9 | 69 |  | No | 76.56 |
| 10 | 68 |  | No | 47.44 |
| 11 | 71 |  | No | 59.97 |
| 12 | 57 |  | No | 58.18 |
| 13 | 50 |  | No | 52.1 |
| 14 | 75 |  | No | 62.81 |
| 15 | 49 |  | No | 67.63 |
| 16 | 65 |  | No | 55.94 |
| 17 | 60 |  | No | 60.64 |
| 18 | 58 |  | No | 56.34 |
| 19 | 41 |  | No | 67.13 |
| 20 | 68 |  | No | 61.15 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IGBDSUT | IGBDSUT | Yes | 16.29 |
| 2 | NZIWVKB | NZIWVKB | Yes | 9.74 |
| 3 | EOJVGDL | EOJVGDL | Yes | 7.89 |
| 4 | WVBXLSK | WVBXLSK | Yes | 4.81 |
| 5 | FYCDEUK | FYCDEUK | Yes | 7.16 |
| 6 | LGSRHJB | LGSRHJB | Yes | 5.82 |
| 7 | WPGZCKB | WPGZCKB | Yes | 7.06 |
| 8 | PZQGITE | PZQGITE | Yes | 3.06 |
| 9 | LZFPICW | LZFPICW | Yes | 9.41 |
| 10 | DWPXYFS | DWPXYFS | Yes | 8.13 |
| 11 | AGHOEJP | AGHOEJP | Yes | 2.65 |
| 12 | HZPFQBA | HZPFQBA | Yes | 6.7 |
| 13 | RMHXCIQ | RMHXCIQ | Yes | 5.48 |
| 14 | MNFAWXD | MNFAWXD | Yes | 5.38 |
| 15 | TQELYUX | TQELYUX | Yes | 6.0 |
| 16 | IXAMGCO | IXAMGCO | Yes | 12.03 |
| 17 | LCXRWBD | LCXRWBD | Yes | 6.15 |
| 18 | AXIZTLG | AXIZTLG | Yes | 3.28 |
| 19 | VRYJMLE | VRYJMLE | Yes | 11.26 |
| 20 | WJPITCM | WJPITCM | Yes | 4.88 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.9, 5.1] | 5.1 4.9 | Yes | 8.9 |
| 2 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.28 |
| 3 | [0.3, 9.7] | 9.7 0.3 | Yes | 9.21 |
| 4 | [2.6, 7.4] | 7.4 2.6 | Yes | 8.14 |
| 5 | [2.2, 7.8] | 2.2 7.8 | Yes | 3.21 |
| 6 | [2.8, 7.2] | 2.8 7.2 | Yes | 5.55 |
| 7 | [1.7, 8.3] | 8.3 1.7 | Yes | 7.84 |
| 8 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.3 |
| 9 | [0.6, 9.4] | 0.6 9.4 | Yes | 6.84 |
| 10 | [0.9, 9.1] | 9.1 0.9 | Yes | 8.66 |
| 11 | [4.0, 6.0] | 4.0 6.0 | Yes | 11.29 |
| 12 | [3.6, 6.4] | 6.4 3.6 | Yes | 9.14 |
| 13 | [4.2, 5.8] | 5.8 4.2 | Yes | 19.61 |
| 14 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.92 |
| 15 | [0.9, 9.1] | 9.1 0.9 | Yes | 7.54 |
| 16 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.32 |
| 17 | [1.1, 8.9] | 8.9 1.1 | Yes | 13.67 |
| 18 | [4.8, 5.2] | 4.8 5.2 | Yes | 37.35 |
| 19 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.54 |
| 20 | [0.4, 9.6] | 9.6 0.4 | Yes | 9.51 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DZ45SSKEFFKR | DZ45SSKEFFKR | Yes | 10.35 |
| 2 | 54ZYHMVR46A9 | 54ZYHMVR46A9 | Yes | 2.03 |
| 3 | 6JJPOV6EZFUE | 6JJPOV6EZFUE | Yes | 4.8 |
| 4 | BUH2X4RHZ236 | BUH2X4RHZ236 | Yes | 4.08 |
| 5 | KJ3RJZ7BZYHI | KJ3RJZ7BZYHI | Yes | 2.32 |
| 6 | T5US9C6HVWHO | T5US9C6HVWHO | Yes | 3.21 |
| 7 | PDR9HPK137EP | PDR9HPK137EP | Yes | 3.78 |
| 8 | 2TVPGGWY8HBE | 2TVPGGWY8HBE | Yes | 1.56 |
| 9 | XG7XDF2LTMO9 | XG7XDF2LTM09 | No | 2.99 |
| 10 | 7X784MLWKHSI | 7X784MLWKHSI | Yes | 3.18 |
| 11 | L4X2JXZHKBPR | L4X2JXZHK8PR | No | 13.37 |
| 12 | UR9EQTMSVSYA | UR9EQTMSVSYA | Yes | 3.83 |
| 13 | IAXLZ0QPF453 | IAXLZ0QPF453 | Yes | 2.64 |
| 14 | MRX832I5PVB7 | MRX832I5PVB7 | Yes | 3.05 |
| 15 | VZSIZKLECMSE | VZSIZKLECMSE | Yes | 3.32 |
| 16 | Q9UT1UUQLH2C | Q9UT1UWQLH2C | No | 9.15 |
| 17 | NTLKK2INUK5N | NTLKK2INUK5N | Yes | 2.74 |
| 18 | DQ3LBTN43IME | DQ3LBTN43IME | Yes | 1.69 |
| 19 | QY2TEXW11V9R | QY2TEXW11V9R | Yes | 3.86 |
| 20 | 0X4M52JFKSHQ | 0X4M52JFKSHQ | Yes | 4.34 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 2.51 |
| 2 | 5 | 5 | Yes | 7.61 |
| 3 | 1 | 1 | Yes | 15.13 |
| 4 | 16 | 16 | Yes | 4.71 |
| 5 | 7680 | 7680 | Yes | 4.62 |
| 6 | 7 | 7 | Yes | 3.0 |
| 7 | 63 | 63 | Yes | 4.76 |
| 8 | 23 | 23 | Yes | 3.66 |
| 9 | 64 | 64 | Yes | 13.19 |
| 10 | 73 | 73 | Yes | 6.08 |
| 11 | 9 | 9 | Yes | 4.51 |
| 12 | 65 | 65 | Yes | 5.53 |
| 13 | 28 | 28 | Yes | 10.07 |
| 14 | 4 | 4 | Yes | 3.75 |
| 15 | 67 | 67 | Yes | 3.33 |
| 16 | 3 | 3 | Yes | 4.5 |
| 17 | 1440 | 1440 | Yes | 4.63 |
| 18 | 20 | 20 | Yes | 6.74 |
| 19 | 19 | 19 | Yes | 3.86 |
| 20 | 198 | 198 | Yes | 4.58 |
