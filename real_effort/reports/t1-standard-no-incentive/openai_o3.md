# Benchmark Report — o3

- **Model**: `openai/o3`
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
| sudoku_game | 7657 | 38815 | 46472 | 0 | 20 | 65.70 | 1314.3 |
| add_numbers | 7080 | 2780 | 9860 | 20 | 0 | 3.73 | 74.7 |
| counting_zeros | 7140 | 39182 | 46322 | 0 | 20 | 48.78 | 975.95 |
| task_decoding | 10600 | 10978 | 21578 | 18 | 2 | 15.37 | 307.52 |
| task_summation | 7400 | 14293 | 21693 | 20 | 0 | 13.21 | 264.4 |
| task_transcription | 7160 | 10214 | 17374 | 17 | 3 | 11.98 | 239.69 |
| task_sequences | 2720 | 9996 | 12716 | 18 | 2 | 12.29 | 245.86 |
| **TOTAL** | **49757** | **126258** | **176015** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 3 2 3 4 1 5 6 4 5 4 2 1 |  | No | 53.58 |
| 2 | 6 1 5 5 4 3 5 2 4 1 4 3 5 4 |  | No | 83.32 |
| 3 | 2 3 6 4 2 6 4 3 5 1 2 6 5 3 |  | No | 73.64 |
| 4 | 6 3 3 6 4 2 4 5 6 2 3 6 4 5 |  | No | 115.36 |
| 5 | 4 5 1 4 3 4 6 2 5 1 4 5 1 3 |  | No | 83.21 |
| 6 | 3 2 5 4 3 1 5 6 1 3 5 6 6 2 |  | No | 89.4 |
| 7 | 6 4 3 5 6 4 3 1 2 6 6 4 6 5 |  | No | 71.64 |
| 8 | 2 4 1 4 3 1 5 2 1 2 4 3 4 5 | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 15.81 |
| 9 | 2 3 5 4 1 2 1 6 4 2 3 5 1 4 |  | No | 50.51 |
| 10 | 6 3 2 4 3 6 5 3 2 6 5 6 1 3 |  | No | 55.93 |
| 11 | 6 2 4 5 3 4 4 3 5 4 3 2 6 1 |  | No | 64.18 |
| 12 | 2 3 6 3 5 5 2 4 6 2 3 6 2 3 |  | No | 61.5 |
| 13 | 5 2 4 5 2 5 6 3 1 5 4 4 2 1 |  | No | 63.76 |
| 14 | 3 6 6 4 5 1 3 6 4 6 4 3 1 4 |  | No | 44.26 |
| 15 | 4 5 1 5 2 4 6 3 6 5 1 2 3 6 |  | No | 88.45 |
| 16 | 6 1 6 4 3 1 3 6 4 5 6 5 2 3 |  | No | 68.24 |
| 17 | 6 3 5 6 4 2 4 5 2 6 3 6 3 5 |  | No | 76.47 |
| 18 | 2 3 4 2 3 4 1 2 5 6 1 4 4 1 |  | No | 54.59 |
| 19 | 4 1 6 1 6 3 5 1 2 3 6 1 4 5 |  | No | 49.61 |
| 20 | 1 3 4 4 6 3 6 4 3 2 5 3 2 1 |  | No | 50.64 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2434 | 2434 | Yes | 3.04 |
| 2 | 1629 | 1629 | Yes | 3.26 |
| 3 | 1177 | 1177 | Yes | 3.4 |
| 4 | 1167 | 1167 | Yes | 2.41 |
| 5 | 1349 | 1349 | Yes | 3.4 |
| 6 | 1279 | 1279 | Yes | 2.82 |
| 7 | 1541 | 1541 | Yes | 2.94 |
| 8 | 846 | 846 | Yes | 3.03 |
| 9 | 1707 | 1707 | Yes | 2.96 |
| 10 | 1457 | 1457 | Yes | 3.5 |
| 11 | 2751 | 2751 | Yes | 4.55 |
| 12 | 1951 | 1951 | Yes | 3.61 |
| 13 | 1009 | 1009 | Yes | 3.25 |
| 14 | 2318 | 2318 | Yes | 7.33 |
| 15 | 1794 | 1794 | Yes | 5.4 |
| 16 | 1567 | 1567 | Yes | 3.89 |
| 17 | 757 | 757 | Yes | 3.06 |
| 18 | 1350 | 1350 | Yes | 4.57 |
| 19 | 1454 | 1454 | Yes | 4.83 |
| 20 | 1488 | 1488 | Yes | 3.32 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 62 | 67 | No | 15.51 |
| 2 | 66 |  | No | 73.41 |
| 3 | 74 |  | No | 40.53 |
| 4 | 71 |  | No | 55.83 |
| 5 | 51 |  | No | 60.33 |
| 6 | 58 |  | No | 49.01 |
| 7 | 37 |  | No | 35.74 |
| 8 | 75 |  | No | 39.27 |
| 9 | 35 |  | No | 51.34 |
| 10 | 63 |  | No | 36.75 |
| 11 | 74 |  | No | 45.73 |
| 12 | 71 |  | No | 70.63 |
| 13 | 47 |  | No | 43.46 |
| 14 | 55 |  | No | 61.13 |
| 15 | 71 | 67 | No | 31.33 |
| 16 | 44 | 67 | No | 30.79 |
| 17 | 48 |  | No | 51.12 |
| 18 | 57 |  | No | 79.13 |
| 19 | 51 |  | No | 60.44 |
| 20 | 64 |  | No | 44.16 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MPCWNJD |  | No | 53.04 |
| 2 | OVUZXFW | OVUZXFW | Yes | 49.87 |
| 3 | XPZQGLD | XPZQGLD | Yes | 6.97 |
| 4 | YPKJQVF | YPKJQVF | Yes | 9.49 |
| 5 | RQTKESN | RQTKESN | Yes | 4.76 |
| 6 | FLTPWKA | FLTPWKA | Yes | 4.44 |
| 7 | WUYGKIO | WUYGKIO | Yes | 5.28 |
| 8 | BNFYQLM | BNFYQLM | Yes | 7.34 |
| 9 | TVAOWLH |  | No | 59.01 |
| 10 | KJQOTGL | KJQOTGL | Yes | 12.45 |
| 11 | IDLGRQH | IDLGRQH | Yes | 16.38 |
| 12 | KSINEYV | KSINEYV | Yes | 8.69 |
| 13 | KVZGCRW | KVZGCRW | Yes | 13.35 |
| 14 | HBZICDS | HBZICDS | Yes | 10.91 |
| 15 | BIJCXKA | BIJCXKA | Yes | 12.78 |
| 16 | ALYXZUP | ALYXZUP | Yes | 5.51 |
| 17 | VEHULSJ | VEHULSJ | Yes | 7.85 |
| 18 | IGKQZRA | IGKQZRA | Yes | 5.7 |
| 19 | MWUYEPR | MWUYEPR | Yes | 6.34 |
| 20 | JIBXCOV | JIBXCOV | Yes | 7.15 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.5, 7.5] | 2.5 7.5 | Yes | 12.01 |
| 2 | [2.2, 7.8] | 2.2 7.8 | Yes | 10.24 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.56 |
| 4 | [2.7, 7.3] | 2.7 7.3 | Yes | 7.57 |
| 5 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.06 |
| 6 | [4.3, 5.7] | 4.3 5.7 | Yes | 13.15 |
| 7 | [1.6, 8.4] | 8.4 1.6 | Yes | 17.85 |
| 8 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.01 |
| 9 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.84 |
| 10 | [3.2, 6.8] | 6.8 3.2 | Yes | 15.89 |
| 11 | [2.8, 7.2] | 7.2 2.8 | Yes | 12.63 |
| 12 | [4.3, 5.7] | 5.7 4.3 | Yes | 16.09 |
| 13 | [3.6, 6.4] | 6.4 3.6 | Yes | 13.8 |
| 14 | [4.2, 5.8] | 4.2 5.8 | Yes | 12.66 |
| 15 | [4.7, 5.3] | 5.3 4.7 | Yes | 12.14 |
| 16 | [3.0, 7.0] | 7.0 3.0 | Yes | 16.13 |
| 17 | [4.7, 5.3] | 5.3 4.7 | Yes | 15.56 |
| 18 | [0.2, 9.8] | 9.8 0.2 | Yes | 11.84 |
| 19 | [0.8, 9.2] | 0.8 9.2 | Yes | 15.51 |
| 20 | [3.2, 6.8] | 3.2 6.8 | Yes | 21.67 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EUHMWK2K9EC7 | EUHMWK2K9EC7 | Yes | 4.16 |
| 2 | FONHRVFBRK24 | FONHRVFBRK24 | Yes | 8.91 |
| 3 | FXCHTHOKJKYL | FXCHTHOKJKYL | Yes | 4.17 |
| 4 | 2TWTGFMH4WXC | 2TWTGFMH4WXC | Yes | 4.34 |
| 5 | GA0J3R8DPWN4 | GA0J3R8DPWN4 | Yes | 6.34 |
| 6 | 3TLOJYPGK9SY | 3TLOJYPGK9SY | Yes | 12.5 |
| 7 | AWGJYG6HQ8NK | AWGJYG6HQ8NK | Yes | 7.33 |
| 8 | YSCKIMOQ8JJL | YSCKIMOQ&JJL | No | 23.66 |
| 9 | TSKE1WBSQ2N5 | TSKE1WBSQ2N5 | Yes | 5.4 |
| 10 | MLT4P6BX0P7B | MLT4P6BX0P7B | Yes | 5.68 |
| 11 | SAX8Y65IXOBM | SAX8Y65IXOBM | Yes | 16.67 |
| 12 | 7SIZVH6JR5E6 | 7SIZVH6JR5E6 | Yes | 14.36 |
| 13 | 4741SH7T62LY | 4741SH7T62LY | Yes | 7.26 |
| 14 | SSCMQO7UO6YN |  | No | 59.63 |
| 15 | BATWTX9PR5V1 | BATWTX9PR5V1 | Yes | 4.46 |
| 16 | A4YRUUOVZDDG | A4YRUUOVZDDG | Yes | 9.94 |
| 17 | CWQ15B17H0LX | CWQ15B17H0LX | Yes | 19.19 |
| 18 | 6OS2EQ6URZM3 | 6OS2EQ6URZM3 | Yes | 18.18 |
| 19 | RKG89FHA074F | RKG89FHA074F | Yes | 3.7 |
| 20 | PUQZ0YMIUFSS | PUQZOYMIUFSS | No | 3.67 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 8.7 |
| 2 | 16 | 16 | Yes | 7.94 |
| 3 | 44 | 44 | Yes | 33.18 |
| 4 | 7680 | 7680 | Yes | 7.13 |
| 5 | 67 | 67 | Yes | 3.35 |
| 6 | 63 | 63 | Yes | 7.67 |
| 7 | 5 |  | No | 43.84 |
| 8 | 20 |  | No | 65.36 |
| 9 | 793 | 793 | Yes | 4.54 |
| 10 | 9 | 9 | Yes | 5.02 |
| 11 | 7 | 7 | Yes | 4.49 |
| 12 | 4 | 4 | Yes | 7.71 |
| 13 | 5 | 5 | Yes | 7.92 |
| 14 | 31 | 31 | Yes | 5.16 |
| 15 | 28 | 28 | Yes | 11.15 |
| 16 | 48 | 48 | Yes | 4.38 |
| 17 | 243 | 243 | Yes | 2.43 |
| 18 | 73 | 73 | Yes | 4.33 |
| 19 | 65 | 65 | Yes | 5.17 |
| 20 | 198 | 198 | Yes | 6.38 |
