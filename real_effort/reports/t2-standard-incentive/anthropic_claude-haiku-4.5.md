# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
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
| sudoku_game | 8600 | 27565 | 36165 | 5 | 15 | 13.24 | 264.95 |
| add_numbers | 4520 | 3429 | 7949 | 20 | 0 | 3.23 | 64.73 |
| counting_zeros | 7460 | 21452 | 28912 | 2 | 18 | 8.32 | 166.66 |
| task_decoding | 13900 | 11148 | 25048 | 18 | 2 | 5.35 | 107.18 |
| task_summation | 7820 | 16787 | 24607 | 20 | 0 | 6.89 | 137.9 |
| task_transcription | 4664 | 3635 | 8299 | 15 | 5 | 3.23 | 64.76 |
| task_sequences | 3780 | 5348 | 9128 | 20 | 0 | 2.86 | 57.22 |
| **TOTAL** | **50744** | **89364** | **140108** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 4 3 5 1 4 3 2 1 2 5 4 2 | 4 6 4 3 4 5 1 2 1 3 5 2 3 4 | No | 13.67 |
| 2 | 4 2 3 5 6 2 2 4 3 4 1 6 6 2 | 4 2 3 5 6 2 2 4 3 4 1 6 6 2 | Yes | 10.25 |
| 3 | 1 5 2 5 5 2 1 6 4 3 2 4 2 3 | 1 5 2 5 5 2 1 6 4 3 2 4 2 3 | Yes | 21.17 |
| 4 | 2 6 1 4 3 5 2 1 2 3 6 4 5 4 | 2 6 1 4 3 4 5 2 1 6 3 4 2 4 6 5 6** | No | 15.19 |
| 5 | 3 1 2 5 4 5 1 2 3 5 4 3 2 5 | 3 1 2 5 4 5 1 2 3 5 4 3 2 5 | Yes | 15.0 |
| 6 | 3 1 2 5 2 1 3 2 3 6 3 5 4 6 | ** 3 1 5 2 2 1 3 2 3 6 3 5 4 | No | 10.4 |
| 7 | 3 5 4 2 1 2 3 1 3 6 4 3 5 1 | 3 5 4 2 1 2 3 1 3 6 4 3 5 1 | Yes | 12.31 |
| 8 | 2 6 5 6 4 3 1 2 1 2 5 1 4 6 | 2 6 5 4 6 3 1 2 1 2 5 1 6 4 | No | 10.11 |
| 9 | 2 1 6 3 1 3 1 5 3 4 1 6 5 3 | 6 5 2 3 1 1 1 3 5 3 4 1 6 4 5 3 6 | No | 14.18 |
| 10 | 3 6 4 2 6 3 1 2 6 3 4 3 5 6 | 3 6 4 2 6 1 3 2 6 3 4 3 5 6 | No | 13.51 |
| 11 | 1 2 1 2 5 6 5 5 4 2 6 3 1 2 | 1 2 5 2 6 1 5 4 1 5 6 2 3 2 | No | 9.6 |
| 12 | 2 1 6 4 3 4 1 2 4 5 1 4 2 6 | 2 1 6 4 3 4 1 2 4 5 1 5 4 2 6 | No | 17.82 |
| 13 | 1 5 3 6 4 2 4 6 6 5 5 6 6 3 | 1 5 3 6 4 6 4 2 2 6 5 6 6 3 | No | 13.69 |
| 14 | 2 5 3 2 5 4 1 4 6 4 3 1 6 2 | 2 5 3 2 5 4 1 4 6 4 3 1 6 2 | Yes | 10.13 |
| 15 | 5 4 3 1 2 3 5 1 6 2 3 2 6 4 | 5 3 2 2 4 1 5 3 6 6 1 4 2 3 5 2 6 4 | No | 13.59 |
| 16 | 3 6 6 2 4 5 6 2 6 4 3 6 2 6 | 3 6 6 2 4 5 4 2 6 2 4 3 6 | No | 16.21 |
| 17 | 4 3 5 3 2 1 4 3 2 5 6 1 3 2 | 4 3 5 2 3 1 4 3 1 2 6 5 3 2 | No | 9.71 |
| 18 | 6 5 4 5 3 1 6 2 4 3 6 3 4 5 | 6 5 4 5 3 6 4 2 5 3 1 3 6 4 | No | 15.08 |
| 19 | 2 3 1 4 6 4 1 6 4 2 2 4 5 3 | 2 3 1 4 6 1 6 4 2 5 4 2 3 5** | No | 13.61 |
| 20 | 6 4 1 1 3 1 5 4 2 3 2 5 3 5 | 6 4 1 3 1 1 5 3 2 3 2 5 3 5 | No | 9.54 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1142 | 1142 | Yes | 2.63 |
| 2 | 1574 | 1574 | Yes | 4.75 |
| 3 | 1981 | 1981 | Yes | 2.49 |
| 4 | 1628 | 1628 | Yes | 3.74 |
| 5 | 1781 | 1781 | Yes | 3.89 |
| 6 | 1775 | 1775 | Yes | 2.79 |
| 7 | 1343 | 1343 | Yes | 2.99 |
| 8 | 1642 | 1642 | Yes | 2.34 |
| 9 | 1777 | 1777 | Yes | 2.62 |
| 10 | 1974 | 1974 | Yes | 2.49 |
| 11 | 1104 | 1104 | Yes | 2.63 |
| 12 | 1733 | 1733 | Yes | 2.41 |
| 13 | 1862 | 1862 | Yes | 3.06 |
| 14 | 1215 | 1215 | Yes | 8.28 |
| 15 | 1775 | 1775 | Yes | 3.04 |
| 16 | 1736 | 1736 | Yes | 2.84 |
| 17 | 1575 | 1575 | Yes | 2.93 |
| 18 | 1720 | 1720 | Yes | 2.62 |
| 19 | 1664 | 1664 | Yes | 3.06 |
| 20 | 1638 | 1638 | Yes | 3.04 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 52 | 52 | Yes | 9.32 |
| 2 | 47 | 43 | No | 7.05 |
| 3 | 38 | 34 | No | 8.79 |
| 4 | 45 | 46 | No | 8.53 |
| 5 | 62 | 67 | No | 7.84 |
| 6 | 38 | 37 | No | 7.07 |
| 7 | 54 | 54 | Yes | 9.72 |
| 8 | 38 | 41 | No | 7.56 |
| 9 | 60 | 59 | No | 11.22 |
| 10 | 63 | 60 | No | 6.71 |
| 11 | 40 | 38 | No | 7.33 |
| 12 | 61 | 57 | No | 7.91 |
| 13 | 58 | 56 | No | 7.09 |
| 14 | 40 | 37 | No | 8.51 |
| 15 | 38 | 36 | No | 8.45 |
| 16 | 55 | 53 | No | 9.34 |
| 17 | 55 | 52 | No | 10.1 |
| 18 | 58 | 54 | No | 8.91 |
| 19 | 75 | 91 | No | 8.5 |
| 20 | 54 | 56 | No | 6.41 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CSWFAEM | CSWFAEM | Yes | 4.14 |
| 2 | TMBIWXR | TMBIWXR | Yes | 4.66 |
| 3 | LBVWZFN | LBVWZFN | Yes | 5.06 |
| 4 | XEYAJON | XEYAJON | Yes | 7.37 |
| 5 | AIQZGYW | AIQZGYW | Yes | 4.37 |
| 6 | ELISVDR | ELISVDR | Yes | 4.76 |
| 7 | ZNVJLSH | ZNVJLSH | Yes | 4.56 |
| 8 | HJXWAGL | HJXWAGL | Yes | 5.15 |
| 9 | LGFEOSU | LGFEOSU | Yes | 8.55 |
| 10 | UYTIGQO | UTIQO | No | 6.43 |
| 11 | ZARYFST | ZARYFST | Yes | 4.45 |
| 12 | LPZUOYI | LPZUOYI | Yes | 4.62 |
| 13 | QWMLFZC | QWMLFFZC | No | 6.0 |
| 14 | OVMQWGD | OVMQWGD | Yes | 7.83 |
| 15 | KCSRBIO | KCSRBIO | Yes | 6.54 |
| 16 | OQYMABR | OQYMABR | Yes | 4.27 |
| 17 | EJXOAHY | EJXOAHY | Yes | 4.35 |
| 18 | UWCNFHP | UWCNFHP | Yes | 4.89 |
| 19 | RXEJYOZ | RXEJYOZ | Yes | 3.77 |
| 20 | SHVZNJW | SHVZNJW | Yes | 5.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 0.5 9.5 | Yes | 6.67 |
| 2 | [4.4, 5.6] | 4.4 5.6 | Yes | 5.72 |
| 3 | [0.4, 9.6] | 9.6 0.4 | Yes | 6.16 |
| 4 | [3.0, 7.0] | 7.0 3.0 | Yes | 9.27 |
| 5 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.2 |
| 6 | [1.7, 8.3] | 1.7 8.3 | Yes | 10.03 |
| 7 | [0.1, 9.9] | 0.1 9.9 | Yes | 7.18 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 5.51 |
| 9 | [0.5, 9.5] | 0.5 9.5 | Yes | 6.82 |
| 10 | [4.6, 5.4] | 4.6 5.4 | Yes | 6.28 |
| 11 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.06 |
| 12 | [2.5, 7.5] | 7.5 2.5 | Yes | 7.18 |
| 13 | [2.5, 7.5] | 2.5 7.5 | Yes | 5.88 |
| 14 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.81 |
| 15 | [4.5, 5.5] | 5.5 4.5 | Yes | 7.25 |
| 16 | [3.6, 6.4] | 6.4 3.6 | Yes | 5.96 |
| 17 | [1.3, 8.7] | 1.3 8.7 | Yes | 8.08 |
| 18 | [2.5, 7.5] | 7.5 2.5 | Yes | 7.51 |
| 19 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.81 |
| 20 | [3.2, 6.8] | 6.8 3.2 | Yes | 7.37 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5S60TTDWTT8K | 5S60TTDWTT3K | No | 2.99 |
| 2 | 2M2G51KGN0YX | 2M2G51KGN0YX | Yes | 2.92 |
| 3 | TRPILLDY5EIT | TRPILLDY5EIT | Yes | 2.9 |
| 4 | AIV0EFUAGA27 | AIV0EFUAGA27 | Yes | 3.05 |
| 5 | J4P801HW9AVD | J4P801HW9AVD | Yes | 2.85 |
| 6 | DFPT3LK9L6KO | DFPT3LK9L6KO | Yes | 3.89 |
| 7 | 6CUHNPRLDNC8 | 6CUHNPBLQNC8 | No | 3.66 |
| 8 | BQIAUGYGRM39 | BQIAUGYGRM39 | Yes | 7.01 |
| 9 | M9HQQ7TP18RC | M9HQQ7TP18RC | Yes | 3.71 |
| 10 | K7CU9AHUM5GW | K7CU9AHUM5GW | Yes | 2.7 |
| 11 | VZDX2WZ5T40F | VZDX2WZ5T40F | Yes | 2.54 |
| 12 | K1UEYP340VZ5 | K1UEYP340VZ5 | Yes | 2.67 |
| 13 | 0SHZA1NCVH6G | OSHZA1NCVH8G | No | 3.06 |
| 14 | QQJ0HPQ47PI1 | QQJQHPQ47PII | No | 2.38 |
| 15 | KNI3NZJRLNOE | KNI3NZJRLNOE | Yes | 3.63 |
| 16 | TH5CL8ZP0BX3 | TH5CL8ZP0BX3 | Yes | 3.65 |
| 17 | H0KUN00B8JFX | H0KUN00B8JFX | Yes | 3.04 |
| 18 | 57U1BXGPJS1M | 57U1BXGPJS1M | Yes | 2.49 |
| 19 | IPP1B6234DBD | IPP1B6234DBD | Yes | 2.13 |
| 20 | O0ONM8JJC4JL | OOONM8JJC4JL | No | 3.4 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 3.64 |
| 2 | 26 | 26 | Yes | 6.18 |
| 3 | 1 | 1 | Yes | 2.89 |
| 4 | 1440 | 1440 | Yes | 2.74 |
| 5 | 44 | 44 | Yes | 3.28 |
| 6 | 60 | 60 | Yes | 2.18 |
| 7 | 4 | 4 | Yes | 2.54 |
| 8 | 5 | 5 | Yes | 2.65 |
| 9 | 60 | 60 | Yes | 2.29 |
| 10 | 9 | 9 | Yes | 3.6 |
| 11 | 39 | 39 | Yes | 2.41 |
| 12 | 36 | 36 | Yes | 2.45 |
| 13 | 73 | 73 | Yes | 2.27 |
| 14 | 67 | 67 | Yes | 2.42 |
| 15 | 23 | 23 | Yes | 2.29 |
| 16 | 10 | 10 | Yes | 2.38 |
| 17 | 9 | 9 | Yes | 2.47 |
| 18 | 65 | 65 | Yes | 2.73 |
| 19 | 4 | 4 | Yes | 2.65 |
| 20 | 63 | 63 | Yes | 3.18 |
