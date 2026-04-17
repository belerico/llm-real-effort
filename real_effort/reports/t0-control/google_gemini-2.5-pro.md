# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-19 10:07:35

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
| sudoku_game | 8400 | 35932 | 44332 | 0 | 20 | 24.15 | 483.19 |
| add_numbers | 35268 | 8222 | 43490 | 20 | 0 | 6.87 | 137.59 |
| counting_zeros | 9540 | 38173 | 47713 | 1 | 19 | 25.15 | 503.33 |
| task_decoding | 7920 | 7958 | 15878 | 19 | 1 | 5.93 | 118.83 |
| task_summation | 7760 | 23510 | 31270 | 19 | 1 | 11.38 | 227.7 |
| task_transcription | 7480 | 10251 | 17731 | 12 | 8 | 6.71 | 134.29 |
| task_sequences | 2520 | 15693 | 18213 | 20 | 0 | 7.83 | 156.58 |
| **TOTAL** | **78888** | **139739** | **218627** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 3 6 5 1 3 5 1 3 4 1 4 2 3 | 1 3 6 5 1 3 5 4 1 5 1 4 2 3 1 4 2 3 | No | 23.09 |
| 2 | 6 4 1 5 3 2 2 6 2 3 4 2 1 1 | 6 4 1 5 2 3 2 6 2 3 4 2 1 4 1 2 1 | No | 14.93 |
| 3 | 4 2 1 2 3 3 1 5 6 3 2 5 5 6 | 4 2 1 2 3 3 5 1 5 3 5 2 6 5 6 | No | 15.84 |
| 4 | 4 1 3 1 4 5 4 2 4 6 4 3 1 5 | R2: [ | No | 41.92 |
| 5 | 6 3 1 2 6 3 2 6 1 4 5 2 1 4 | , 6. (2,2) and (2,3) are in Box | No | 29.21 |
| 6 | 3 1 5 4 6 1 3 2 3 5 3 4 1 3 | 3 1 5 1 4 6 3 5 3 2 3 4 3 1 | No | 16.42 |
| 7 | 4 5 2 4 2 3 1 3 4 2 2 6 1 1 | 4 5 2 2 3 4 1 4 2 3 1 6 2 1 6 | No | 15.55 |
| 8 | 5 3 6 3 5 4 1 2 1 6 4 5 4 1 |  | No | 36.96 |
| 9 | 3 4 5 6 2 3 4 6 6 5 4 6 5 1 | 4 6 3 5 3 2 4 6 6 5 4 5 1 6 5 1 | No | 15.46 |
| 10 | 5 2 3 5 1 3 6 5 3 4 6 2 4 6 | 5 2 3 3 5 1 5 3 6 3 4 2 6 2 3 6 4 | No | 27.3 |
| 11 | 2 6 5 1 4 5 6 1 3 5 5 1 1 3 |  | No | 38.58 |
| 12 | 5 4 2 1 1 3 4 5 3 1 1 3 5 6 |  | No | 34.33 |
| 13 | 3 6 4 3 6 3 2 2 4 5 4 2 1 6 | 3 6 4 3 6 3 2 4 2 5 6 4 1 2 6 4 5 | No | 14.98 |
| 14 | 6 2 4 1 2 4 6 1 6 1 4 1 4 6 | 6 2 4 1 2 1 6 4 4 1 6 1 4 6 1 4 | No | 15.43 |
| 15 | 1 2 3 4 1 2 5 6 3 1 5 4 5 2 |  | No | 34.62 |
| 16 | 3 1 1 3 3 6 3 4 1 3 6 5 4 1 | 1 3 3 1 3 6 3 6 4 3 1 6 1 5 4 1 4 | No | 15.25 |
| 17 | 5 6 4 3 2 5 2 3 4 1 5 6 1 6 | 5 6 4 3 2 3 2 5 3 2 5 6 1 5 1 6 1 6 | No | 16.44 |
| 18 | 2 4 3 6 4 1 4 1 6 2 3 4 5 5 | 2 4 1 3 6 4 1 6 4 6 2 4 3 5 5 3 | No | 24.69 |
| 19 | 4 2 1 3 3 4 3 5 2 6 5 4 3 6 | 4 3 1 3 3 4 5 4 2 3 6 2 5 6 5 3 4 6 5 3 | No | 15.69 |
| 20 | 3 4 6 2 5 1 5 1 6 4 2 3 4 3 |  | No | 36.3 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2285 | 2285 | Yes | 4.89 |
| 2 | 2105 | 2105 | Yes | 4.43 |
| 3 | 1078 | 1078 | Yes | 3.99 |
| 4 | 2358 | 2358 | Yes | 7.28 |
| 5 | 1825 | 1825 | Yes | 17.04 |
| 6 | 1278 | 1278 | Yes | 4.8 |
| 7 | 2277 | 2277 | Yes | 4.43 |
| 8 | 1486 | 1486 | Yes | 15.17 |
| 9 | 1276 | 1276 | Yes | 6.34 |
| 10 | 1156 | 1156 | Yes | 5.1 |
| 11 | 1647 | 1647 | Yes | 7.43 |
| 12 | 1099 | 1099 | Yes | 7.18 |
| 13 | 1758 | 1758 | Yes | 6.28 |
| 14 | 2161 | 2161 | Yes | 5.81 |
| 15 | 2157 | 2157 | Yes | 6.1 |
| 16 | 1665 | 1665 | Yes | 7.07 |
| 17 | 905 | 905 | Yes | 5.17 |
| 18 | 1471 | 1471 | Yes | 4.76 |
| 19 | 1048 | 1048 | Yes | 7.42 |
| 20 | 2196 | 2196 | Yes | 6.79 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 41 | 41 | Yes | 15.82 |
| 2 | 67 |  | No | 35.79 |
| 3 | 60 | 62 | No | 15.79 |
| 4 | 69 | 68 | No | 26.09 |
| 5 | 41 |  | No | 35.79 |
| 6 | 75 | 73 | No | 27.24 |
| 7 | 73 |  | No | 37.28 |
| 8 | 40 |  | No | 25.07 |
| 9 | 70 |  | No | 25.91 |
| 10 | 41 |  | No | 24.59 |
| 11 | 48 |  | No | 23.04 |
| 12 | 47 |  | No | 26.86 |
| 13 | 48 |  | No | 23.67 |
| 14 | 61 |  | No | 28.33 |
| 15 | 69 |  | No | 25.88 |
| 16 | 66 | 67 | No | 8.43 |
| 17 | 75 |  | No | 27.66 |
| 18 | 55 |  | No | 17.94 |
| 19 | 65 |  | No | 27.94 |
| 20 | 50 | Col 3: 1 0 1 1 1 1 1 1 0 1 1 1 0 0 0 -> 5 zeros. Correct. Col | No | 23.92 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SFYTIDG | SFYTIDG | Yes | 5.61 |
| 2 | EZFNXIL | EZFNXIL | Yes | 5.39 |
| 3 | MROINCH | MROINCH | Yes | 7.86 |
| 4 | LRQYPXK | LRQYPXK | Yes | 5.8 |
| 5 | BJKUWVR | BJKWUVR | No | 5.99 |
| 6 | JHBORDX | JHBORDX | Yes | 6.72 |
| 7 | LRDPYVC | LRDPYVC | Yes | 6.27 |
| 8 | CMETHWX | CMETHWX | Yes | 5.51 |
| 9 | PXGMNDK | PXGMNDK | Yes | 5.65 |
| 10 | RUHLXAB | RUHLXAB | Yes | 4.62 |
| 11 | FIQGHYZ | FIQGHYZ | Yes | 6.71 |
| 12 | IMVQESA | IMVQESA | Yes | 4.61 |
| 13 | XARHDUL | XARHDUL | Yes | 6.37 |
| 14 | QIVELHX | QIVELHX | Yes | 4.53 |
| 15 | FIYVEHZ | FIYVEHZ | Yes | 6.36 |
| 16 | WKFLDBQ | WKFLDBQ | Yes | 5.92 |
| 17 | RYAHQCE | RYAHQCE | Yes | 5.72 |
| 18 | SXIWJNG | SXIWJNG | Yes | 6.44 |
| 19 | ZKMOJYA | ZKMOJYA | Yes | 5.68 |
| 20 | LGZIVHB | LGZIVHB | Yes | 6.86 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.28 |
| 2 | [1.0, 9.0] | 1.0 9.0 | Yes | 8.74 |
| 3 | [1.5, 8.5] | 1.5 8.5 | Yes | 10.71 |
| 4 | [1.6, 8.4] | 8.4 1.6 | Yes | 11.41 |
| 5 | [3.4, 6.6] | 3.4 6.6 | Yes | 10.05 |
| 6 | [3.1, 6.9] | 3.1 6.9 | Yes | 10.21 |
| 7 | [1.9, 8.1] | 8.1 1.9 | Yes | 9.7 |
| 8 | [4.4, 5.6] | 4.4 5.6 | Yes | 11.01 |
| 9 | [0.2, 9.8] | 9.8 0.2 | Yes | 11.65 |
| 10 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.35 |
| 11 | [2.3, 7.7] | 2.3 7.7 | Yes | 11.2 |
| 12 | [0.4, 9.6] | 9.6 0.4 | Yes | 8.75 |
| 13 | [0.3, 9.7] | 0.3 9.7 | Yes | 10.21 |
| 14 | [3.8, 6.2] | 6.2 3.8 | Yes | 12.52 |
| 15 | [3.2, 6.8] | 6.8 3.2 | Yes | 9.67 |
| 16 | [4.8, 5.2] | 5.2 4.8 | Yes | 10.04 |
| 17 | [1.9, 8.1] |  | No | 25.38 |
| 18 | [0.9, 9.1] | 0.9 9.1 | Yes | 10.52 |
| 19 | [1.0, 9.0] | 1.0 9.0 | Yes | 9.06 |
| 20 | [2.4, 7.6] | 2.4 7.6 | Yes | 13.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53FE0JHWPB81 | 53FE0JHWPB81 | Yes | 6.18 |
| 2 | 2LYJAO9YXDC1 | 2LYJA09YXDC1 | No | 7.52 |
| 3 | 7R2OL2IUCNLM | 7R20L2IUCNLM | No | 7.7 |
| 4 | DIJU0LMA2IF8 | DIJU0LMA2IF8 | Yes | 5.67 |
| 5 | WMMBPF8I6706 | WMMBPF816706 | No | 5.82 |
| 6 | HUTE8Z57M07I | HUTE8Z57M071 | No | 6.17 |
| 7 | IODWDQ1VQ9KH | IODWDQ1VQ9KH | Yes | 5.31 |
| 8 | I4MNVGCARECS | I4MNVGCARECS | Yes | 14.34 |
| 9 | UFGET43M5V03 | UFGET43M5V03 | Yes | 6.75 |
| 10 | 6BW0DWXCYOFZ | 6BWODWXCYOFZ | No | 8.29 |
| 11 | 0F780KBQTIMF | 0F780KBQTIMF | Yes | 5.3 |
| 12 | WMWS9E24MHJY | WMWS9E24MHJY | Yes | 6.59 |
| 13 | 2WBD58AAGWCM | 2WBD58AAGWCM | Yes | 5.64 |
| 14 | K5MOOV48H1AY | K5MOOV48H1AY | Yes | 6.08 |
| 15 | AHDLH2YRYF3E | AHDLH2YRYRF3E | No | 6.21 |
| 16 | JJB4RP3AR7B4 | JJB4RP3AR7B4 | Yes | 6.21 |
| 17 | DF4Z2CS7F2DF | DF4Z2CS7F2DF | Yes | 4.91 |
| 18 | Q1SI9PJJC2H0 | Q1SI9PJJC2H0 | Yes | 6.52 |
| 19 | ITQAS1V8Q0BN | ITQAS1V8Q00BN | No | 7.6 |
| 20 | 09IS6OIT9B5T | 09IS60IT9B5T | No | 5.34 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 19 | 19 | Yes | 5.38 |
| 2 | 5 | 5 | Yes | 16.27 |
| 3 | 793 | 793 | Yes | 8.26 |
| 4 | 7680 | 7680 | Yes | 8.04 |
| 5 | 60 | 60 | Yes | 9.0 |
| 6 | 9 | 9 | Yes | 7.19 |
| 7 | 9 | 9 | Yes | 6.73 |
| 8 | 4 | 4 | Yes | 7.11 |
| 9 | 63 | 63 | Yes | 4.14 |
| 10 | 36 | 36 | Yes | 7.69 |
| 11 | 16 | 16 | Yes | 7.95 |
| 12 | 67 | 67 | Yes | 5.77 |
| 13 | 23 | 23 | Yes | 9.85 |
| 14 | 26 | 26 | Yes | 10.78 |
| 15 | 7 | 7 | Yes | 5.91 |
| 16 | 73 | 73 | Yes | 6.19 |
| 17 | 1440 | 1440 | Yes | 7.09 |
| 18 | 4 | 4 | Yes | 8.3 |
| 19 | 44 | 44 | Yes | 7.84 |
| 20 | 6 | 6 | Yes | 7.08 |
