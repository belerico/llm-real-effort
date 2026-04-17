# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
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
| sudoku_game | 8740 | 32685 | 41425 | 11 | 9 | 24.39 | 487.91 |
| add_numbers | 4660 | 1931 | 6591 | 20 | 0 | 3.49 | 69.94 |
| counting_zeros | 7600 | 21072 | 28672 | 7 | 13 | 12.73 | 254.87 |
| task_decoding | 14040 | 8560 | 22600 | 20 | 0 | 7.49 | 149.88 |
| task_summation | 7960 | 13195 | 21155 | 20 | 0 | 9.71 | 194.33 |
| task_transcription | 4804 | 2808 | 7612 | 18 | 2 | 4.43 | 88.73 |
| task_sequences | 3921 | 8174 | 12095 | 18 | 2 | 6.67 | 133.31 |
| **TOTAL** | **51725** | **88425** | **140150** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 2 6 4 6 5 2 6 4 5 3 2 4 | 2 5 4 6 5 4 6 5 4 6 2 5 3 2 4 | No | 25.52 |
| 2 | 1 2 6 2 1 6 4 5 6 2 5 4 1 6 | 1 2 6 2 1 6 4 5 6 2 5 4 1 6 | Yes | 28.09 |
| 3 | 4 3 5 1 2 6 2 3 3 2 1 5 6 5 | 4 3 5 1 2 6 2 3 3 2 1 5 6 5 | Yes | 23.4 |
| 4 | 3 2 6 1 3 2 4 3 5 1 3 6 4 6 | 2 3 6 1 3 3 4 2 5 6 2 3 4 6 | No | 20.04 |
| 5 | 3 5 4 6 5 1 2 4 6 3 6 2 1 4 | 3 5 4 6 5 1 2 4 6 3 6 2 1 4 | Yes | 21.16 |
| 6 | 4 5 3 6 2 4 6 4 2 5 4 2 6 1 | 4 5 3 2 4 6 4 2 5 4 2 6 1 | No | 26.82 |
| 7 | 4 1 3 3 4 2 3 6 5 1 1 5 4 2 | 3 1 4 4 3 2 3 1 5 6 1 5 4 2 | No | 24.31 |
| 8 | 6 4 4 5 2 1 3 4 2 6 3 3 5 6 | 6 4 4 5 2 1 3 2 6 3 3 5 6 | No | 24.03 |
| 9 | 3 1 2 4 1 3 6 1 4 3 2 1 6 6 | 3 1 2 4 1 3 1 4 3 | No | 24.68 |
| 10 | 2 3 5 6 1 1 3 6 5 6 4 2 2 5 | 2 3 5 6 1 1 3 6 5 6 4 2 2 5 | Yes | 21.76 |
| 11 | 4 5 6 3 2 2 6 4 3 1 3 4 3 5 | 4 5 6 3 2 2 6 4 3 1 3 4 3 5 | Yes | 28.53 |
| 12 | 2 1 3 5 1 5 2 5 3 2 5 6 4 5 | 2 1 3 5 1 5 2 2 5 3 5 6 4 5 | No | 29.72 |
| 13 | 3 4 1 5 4 2 5 1 5 6 3 1 1 6 | 3 4 1 5 4 2 5 1 5 6 3 1 1 6 | Yes | 22.82 |
| 14 | 6 5 5 4 6 2 3 4 2 4 5 3 3 2 | 6 5 5 4 6 2 3 4 2 4 5 3 3 2 | Yes | 18.61 |
| 15 | 2 3 4 6 6 5 6 5 1 2 4 2 3 1 | 2 3 4 6 6 5 6 5 1 2 4 2 3 1 | Yes | 25.05 |
| 16 | 4 5 3 3 3 2 6 1 3 3 5 6 5 4 | 4 3 5 3 3 2 6 3 1 5 3 6 5 4 | No | 25.73 |
| 17 | 3 5 4 6 1 5 2 3 1 5 1 3 4 2 | 3 4 5 6 1 5 2 1 3 5 1 3 2 4 | No | 20.71 |
| 18 | 2 4 1 6 6 5 5 1 2 3 4 4 2 6 | 2 4 1 6 6 5 5 1 2 3 4 4 2 6 | Yes | 21.98 |
| 19 | 4 1 6 2 5 4 2 3 4 5 1 3 1 4 | 4 1 6 2 5 4 2 3 4 5 1 3 1 4 | Yes | 25.34 |
| 20 | 3 5 4 5 1 4 1 4 5 6 5 3 1 4 | 3 5 4 5 1 4 1 4 5 6 5 3 1 4 | Yes | 29.41 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2292 | 2292 | Yes | 3.62 |
| 2 | 2210 | 2210 | Yes | 3.64 |
| 3 | 1834 | 1834 | Yes | 2.54 |
| 4 | 2521 | 2521 | Yes | 2.88 |
| 5 | 2310 | 2310 | Yes | 3.53 |
| 6 | 2328 | 2328 | Yes | 2.78 |
| 7 | 1185 | 1185 | Yes | 3.68 |
| 8 | 1497 | 1497 | Yes | 3.25 |
| 9 | 1403 | 1403 | Yes | 5.7 |
| 10 | 1899 | 1899 | Yes | 3.39 |
| 11 | 1859 | 1859 | Yes | 2.96 |
| 12 | 1359 | 1359 | Yes | 3.0 |
| 13 | 2028 | 2028 | Yes | 3.24 |
| 14 | 1964 | 1964 | Yes | 3.67 |
| 15 | 1130 | 1130 | Yes | 3.34 |
| 16 | 1267 | 1267 | Yes | 2.71 |
| 17 | 1508 | 1508 | Yes | 5.31 |
| 18 | 1978 | 1978 | Yes | 2.64 |
| 19 | 1486 | 1486 | Yes | 4.23 |
| 20 | 1236 | 1236 | Yes | 3.74 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 61 | No | 12.93 |
| 2 | 39 | 39 | Yes | 13.5 |
| 3 | 48 | 48 | Yes | 11.14 |
| 4 | 43 | 43 | Yes | 11.48 |
| 5 | 51 | 48 | No | 13.56 |
| 6 | 50 | 50 | Yes | 12.68 |
| 7 | 55 | 50 | No | 13.91 |
| 8 | 58 | 56 | No | 13.78 |
| 9 | 36 | 36 | Yes | 12.68 |
| 10 | 63 | 51 | No | 12.93 |
| 11 | 61 | 51 | No | 11.98 |
| 12 | 67 | 62 | No | 12.82 |
| 13 | 71 | 70 | No | 14.01 |
| 14 | 51 | 50 | No | 9.3 |
| 15 | 56 | 56 | Yes | 10.79 |
| 16 | 65 | 63 | No | 13.78 |
| 17 | 73 | 71 | No | 14.79 |
| 18 | 35 | 35 | Yes | 13.02 |
| 19 | 62 | 58 | No | 14.28 |
| 20 | 57 | 54 | No | 11.23 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CFUBSPQ | CFUBSPQ | Yes | 6.04 |
| 2 | GCXDJRA | GCXDJRA | Yes | 6.1 |
| 3 | WLSKOFR | WLSKOFR | Yes | 9.5 |
| 4 | GKVETQD | GKVETQD | Yes | 7.5 |
| 5 | JFLQYCM | JFLQYCM | Yes | 5.99 |
| 6 | OMFPWVI | OMFPWVI | Yes | 8.03 |
| 7 | FYHSJWD | FYHSJWD | Yes | 5.11 |
| 8 | ZYDXKFG | ZYDXKFG | Yes | 5.61 |
| 9 | WCXTKID | WCXTKID | Yes | 6.55 |
| 10 | QDOPTAC | QDOPTAC | Yes | 7.65 |
| 11 | CDYWNIJ | CDYWNIJ | Yes | 10.34 |
| 12 | BEGFVTC | BEGFVTC | Yes | 6.5 |
| 13 | DAPHMKE | DAPHMKE | Yes | 9.55 |
| 14 | SFXMOZC | SFXMOZC | Yes | 6.18 |
| 15 | FBPCZEV | FBPCZEV | Yes | 5.62 |
| 16 | LOJXZMW | LOJXZMW | Yes | 5.85 |
| 17 | DKOLYMQ | DKOLYMQ | Yes | 10.41 |
| 18 | SUGTYFJ | SUGTYFJ | Yes | 9.62 |
| 19 | JIBUVLY | JIBUVLY | Yes | 8.27 |
| 20 | DIBLRWN | DIBLRWN | Yes | 9.29 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 8.2 1.8 | Yes | 10.04 |
| 2 | [1.0, 9.0] | 9.0 1.0 | Yes | 10.13 |
| 3 | [1.1, 8.9] | 8.9 1.1 | Yes | 8.03 |
| 4 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.83 |
| 5 | [2.3, 7.7] | 7.7 2.3 | Yes | 13.5 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 11.21 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 7.63 |
| 8 | [1.9, 8.1] | 8.1 1.9 | Yes | 9.64 |
| 9 | [1.4, 8.6] | 1.4 8.6 | Yes | 7.58 |
| 10 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.06 |
| 11 | [0.7, 9.3] | 9.3 0.7 | Yes | 7.61 |
| 12 | [4.3, 5.7] | 4.3 5.7 | Yes | 7.59 |
| 13 | [3.8, 6.2] | 6.2 3.8 | Yes | 10.83 |
| 14 | [4.4, 5.6] | 5.6 4.4 | Yes | 10.51 |
| 15 | [1.9, 8.1] | 8.1 1.9 | Yes | 10.49 |
| 16 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.44 |
| 17 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.29 |
| 18 | [3.9, 6.1] | 3.9 6.1 | Yes | 16.07 |
| 19 | [0.1, 9.9] | 0.1 9.9 | Yes | 9.36 |
| 20 | [1.5, 8.5] | 8.5 1.5 | Yes | 7.32 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DFVQJ42SKLB2 | DFVQJ42SKLB2 | Yes | 4.05 |
| 2 | K2T28MC732BK | K2T28MC732BK | Yes | 3.95 |
| 3 | L3PY9QH5X78K | L3PY9QH5X78K | Yes | 4.75 |
| 4 | 1T4DZTXBX884 | 1T4DZTXBX884 | Yes | 3.75 |
| 5 | LBRW3F3POUA9 | LBRW3F3POUA9 | Yes | 4.72 |
| 6 | F8KKBVBZZU40 | F8KKBVBZZU40 | Yes | 4.21 |
| 7 | P0XWZWOAR9UC | PQXWZWOAR9UC | No | 3.9 |
| 8 | 6GD2U3VNVTU3 | 6GD2U3VNVTU3 | Yes | 4.31 |
| 9 | QJIWJHBAMIUS | QJIWJHBAMIUS | Yes | 4.19 |
| 10 | AD6K5IHNU75S | AD6K5IHNU75S | Yes | 4.99 |
| 11 | ZNZHI374L4VI | ZNZHI374L4VI | Yes | 4.92 |
| 12 | CWRNEVU9FR12 | CWRNEVU9FR12 | Yes | 6.04 |
| 13 | 6RWEZ8Z83DSP | 6RWEZ8Z83DSP | Yes | 4.11 |
| 14 | NO351FR977K7 | NO351FR977K7 | Yes | 3.49 |
| 15 | AL9YBHZN00EZ | AL9YBHZN00EZ | Yes | 4.94 |
| 16 | BGU79KBVIC0S | BGU79KBVIC0S | Yes | 5.32 |
| 17 | NJAJK8F27CRI | NJAJK8F27CRI | Yes | 4.08 |
| 18 | S6ONTMUXW0EL | S6ONTMUXWOEL | No | 4.34 |
| 19 | T35FM0HOS3KC | T35FM0HOS3KC | Yes | 4.37 |
| 20 | VS15ES1SX1VI | VS15ES1SX1VI | Yes | 4.18 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 48 | 48 | Yes | 4.98 |
| 2 | 4096 | 1048576 | No | 13.11 |
| 3 | 793 | 793 | Yes | 5.47 |
| 4 | 198 | 198 | Yes | 6.0 |
| 5 | 6 | 6 | Yes | 4.78 |
| 6 | 9 | 9 | Yes | 5.67 |
| 7 | 23 | 23 | Yes | 5.7 |
| 8 | 20 | 20 | Yes | 9.15 |
| 9 | 16 | 16 | Yes | 5.2 |
| 10 | 7680 | 7680 | Yes | 6.56 |
| 11 | 26 | 26 | Yes | 10.29 |
| 12 | 1 | 1 | Yes | 8.43 |
| 13 | 67 | 67 | Yes | 4.12 |
| 14 | 243 | 243 | Yes | 5.26 |
| 15 | 44 | 44 | Yes | 6.94 |
| 16 | 19 | 19 | Yes | 4.98 |
| 17 | 63 | 63 | Yes | 5.18 |
| 18 | 60 | 60 | Yes | 5.1 |
| 19 | 10 | 9 | No | 10.09 |
| 20 | 64 | 64 | Yes | 6.32 |
