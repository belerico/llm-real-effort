# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 8960 | 28100 | 37060 | 2 | 18 | 11.25 | 225.13 |
| add_numbers | 4880 | 3604 | 8484 | 20 | 0 | 3.13 | 62.71 |
| counting_zeros | 7820 | 19413 | 27233 | 1 | 19 | 7.39 | 148.13 |
| task_decoding | 14260 | 11760 | 26020 | 16 | 4 | 5.19 | 103.93 |
| task_summation | 7771 | 16485 | 24256 | 18 | 2 | 12.67 | 253.58 |
| task_transcription | 4792 | 3825 | 8617 | 13 | 7 | 8.83 | 176.63 |
| task_sequences | 4141 | 6543 | 10684 | 19 | 1 | 3.34 | 66.7 |
| **TOTAL** | **52624** | **89730** | **142354** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 1 4 5 3 6 6 4 1 3 2 6 4 1 | 1 4 6 5 3 1 6 4 1 3 2 6 4 1** | No | 10.71 |
| 2 | 3 5 2 3 5 4 5 2 3 1 6 4 1 3 | 3 5 2 3 5 4 5 2 1 6 4 3 1 | No | 9.72 |
| 3 | 3 5 2 5 3 6 6 5 2 3 1 4 2 5 | 3 5 2 5 3 6 6 2 5 3 1 4 2 5 | No | 18.15 |
| 4 | 3 1 4 3 4 6 2 1 4 5 2 5 1 3 | 3 1 4 3 4 6 2 1 4 5 2 5 1 3 | Yes | 9.39 |
| 5 | 5 4 2 1 4 4 3 3 2 4 1 4 1 3 | 4 2 5 1 4 4 3 3 2 4 1 4 1 3 | No | 11.69 |
| 6 | 1 5 1 2 5 6 4 6 4 2 4 1 6 3 | 1 5 1 2 5 6 4 6 4 2 4 1 6 3 | Yes | 10.37 |
| 7 | 4 3 6 3 1 1 1 5 4 3 6 2 5 1 | 1 3 6 3 1 1 5 6 2 4 5 4 3 1 5 1 | No | 11.89 |
| 8 | 3 3 5 5 2 5 3 4 2 6 5 5 6 3 | 3 5 3 5 5 2 3 4 2 6 5 3 6 3 | No | 11.96 |
| 9 | 2 6 4 6 2 6 3 5 4 6 6 3 1 5 | 2 6 6 4 2 6 3 4 6 5 6 3 1 5 | No | 12.9 |
| 10 | 2 5 4 3 3 1 2 6 6 3 4 1 5 4 | 2 5 4 3 3 6 2 6 1 3 4 6 5 4** | No | 11.14 |
| 11 | 6 5 1 6 6 5 1 6 2 2 4 1 3 6 | 6 5 1 6 6 5 1 6 2 2 4 6 3 1 | No | 9.52 |
| 12 | 5 1 3 3 5 6 1 3 1 5 4 2 1 6 | 5 3 1 3 5 6 1 3 3 1 5 1 5 | No | 13.6 |
| 13 | 2 6 4 1 6 3 4 4 6 5 2 1 2 6 | 6 2 4 4 1 4 3 6 4 6 5 2 1 6 2 | No | 13.05 |
| 14 | 4 5 5 6 1 4 3 3 5 1 6 3 1 2 | 4 5 5 6 2 1 4 3 1 5 1 6 3 1 2** | No | 9.04 |
| 15 | 3 6 2 1 3 3 1 6 5 4 2 6 5 6 | 3 6 2 1 3 3 1 5 6 4 2 6 6 5** | No | 10.77 |
| 16 | 1 6 2 3 5 2 1 2 3 2 6 1 5 4 | 1 2 6 2 3 5 3 5 6 1 5 4 | No | 11.38 |
| 17 | 4 5 2 2 3 4 5 3 1 6 2 5 2 1 | 5 4 2 2 4 3 5 3 1 6 2 2 1 5** | No | 8.76 |
| 18 | 1 4 6 2 5 6 1 3 1 5 3 6 3 6 | 1 4 6 2 5 6 1 3 1 3 5 3 6 3 6** | No | 9.6 |
| 19 | 5 6 1 4 6 1 3 5 6 4 1 6 3 5 | 5 6 1 4 6 3 5 1 1 4 6 3 6 5 | No | 10.13 |
| 20 | 1 2 3 4 1 6 4 6 2 4 3 1 5 3 | 1 2 3 4 6 4 1 3 2 4 1 3 5 3 | No | 11.19 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1491 | 1491 | Yes | 3.44 |
| 2 | 1826 | 1826 | Yes | 3.18 |
| 3 | 1690 | 1690 | Yes | 2.63 |
| 4 | 1846 | 1846 | Yes | 3.02 |
| 5 | 1553 | 1553 | Yes | 3.52 |
| 6 | 1398 | 1398 | Yes | 2.75 |
| 7 | 1976 | 1976 | Yes | 4.47 |
| 8 | 1641 | 1641 | Yes | 2.14 |
| 9 | 999 | 999 | Yes | 3.32 |
| 10 | 2336 | 2336 | Yes | 3.27 |
| 11 | 939 | 939 | Yes | 3.18 |
| 12 | 1330 | 1330 | Yes | 3.51 |
| 13 | 1765 | 1765 | Yes | 2.99 |
| 14 | 1512 | 1512 | Yes | 3.61 |
| 15 | 1556 | 1556 | Yes | 2.66 |
| 16 | 1433 | 1433 | Yes | 2.55 |
| 17 | 1876 | 1876 | Yes | 2.92 |
| 18 | 1775 | 1775 | Yes | 3.32 |
| 19 | 1895 | 1895 | Yes | 3.18 |
| 20 | 1133 | 1133 | Yes | 2.95 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 53 | No | 8.3 |
| 2 | 69 | 61 | No | 7.14 |
| 3 | 48 | 44 | No | 6.67 |
| 4 | 47 | 44 | No | 5.41 |
| 5 | 56 | 49 | No | 6.03 |
| 6 | 74 | 68 | No | 6.95 |
| 7 | 47 | 45 | No | 10.82 |
| 8 | 54 | 48 | No | 6.5 |
| 9 | 48 | 46 | No | 8.2 |
| 10 | 42 | 39 | No | 8.4 |
| 11 | 62 | 58 | No | 9.04 |
| 12 | 44 | 44 | Yes | 7.06 |
| 13 | 61 | 56 | No | 7.84 |
| 14 | 75 | 82 | No | 6.81 |
| 15 | 69 | 70** | No | 8.64 |
| 16 | 68 | 62** | No | 6.22 |
| 17 | 57 | 47 | No | 6.91 |
| 18 | 48 | 46 | No | 7.79 |
| 19 | 49 | 50 | No | 5.49 |
| 20 | 71 | 65 | No | 7.66 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LHCAOXE | LHCAOXE | Yes | 4.59 |
| 2 | HFXYZOD | HFXYZOD | Yes | 4.67 |
| 3 | ABLEWDY | ABLEDWY | No | 5.21 |
| 4 | PMXLOQN | PMXLOQN | Yes | 4.57 |
| 5 | PEFOJLG | PEFOJLG | Yes | 7.57 |
| 6 | UCWYVMX | UCWYVMX | Yes | 4.44 |
| 7 | IQCVNFO | IQCVNFO | Yes | 5.82 |
| 8 | FHGRVYP | FHGRVVYP | No | 4.57 |
| 9 | WSRBONL | WSRBONL | Yes | 5.09 |
| 10 | EHTGDMF | EHTGDMF | Yes | 4.78 |
| 11 | LOYQEFH | LOYQEFH | Yes | 4.61 |
| 12 | LZQOIAW | LZQOIAW | Yes | 5.45 |
| 13 | UKPCNVB | UKPCNVB | Yes | 5.2 |
| 14 | UHXKGVZ | UHXKGVZ | Yes | 4.62 |
| 15 | IFEBNQH | IFEBMQH | No | 6.45 |
| 16 | ZQCBOKV | ZQCBOKV | Yes | 6.03 |
| 17 | NKRTHQF | NKRTHQF | Yes | 4.78 |
| 18 | ESMVRZH | ESMVRZH | Yes | 4.82 |
| 19 | HJMBTZE | HJMBTZЕ | No | 5.45 |
| 20 | DKWQMOG | DKWQMOG | Yes | 5.03 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.72 |
| 2 | [4.5, 5.5] | 5.5 4.5 | Yes | 6.69 |
| 3 | [4.6, 5.4] | 4.6 5.4 | Yes | 6.22 |
| 4 | [3.6, 6.4] | 6.4 3.6 | Yes | 6.87 |
| 5 | [2.6, 7.4] | 7.4 2.6 | Yes | 7.03 |
| 6 | [3.0, 7.0] | 3.0 7.0 | Yes | 6.76 |
| 7 | [0.6, 9.4] | 3.7 6.3 | No | 11.14 |
| 8 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.93 |
| 9 | [2.4, 7.6] | 2.4 7.6 | Yes | 7.0 |
| 10 | [2.1, 7.9] | 2.1 7.9 | Yes | 7.08 |
| 11 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.22 |
| 12 | [1.6, 8.4] | 8.4 1.6 | Yes | 8.54 |
| 13 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.84 |
| 14 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.06 |
| 15 | [1.6, 8.4] | TIMEOUT | No | 120.03 |
| 16 | [0.3, 9.7] | 0.3 9.7 | Yes | 5.65 |
| 17 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.11 |
| 18 | [3.7, 6.3] | 6.3 3.7 | Yes | 7.82 |
| 19 | [3.4, 6.6] | 6.6 3.4 | Yes | 6.59 |
| 20 | [3.9, 6.1] | 6.1 3.9 | Yes | 7.12 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZADUO5HQIM5J | ZADUO5HQIM5J | Yes | 2.82 |
| 2 | 0LEDZZQ4VTWI | OLEDZZQ4VTWI | No | 2.66 |
| 3 | YMRR79AV979I | TIMEOUT | No | 120.03 |
| 4 | ONENY13RTSKL | ONENY13RTSKL | Yes | 2.51 |
| 5 | 695PF5M1PAK7 | 695PF5M1PAK7 | Yes | 2.54 |
| 6 | WFZ9AFWQM8KB | WFZ9AFWQM8KB | Yes | 2.14 |
| 7 | TC2SJ6W43SV0 | TC2SJ6W43SV0 | Yes | 2.54 |
| 8 | 5R0SQYA2UPUS | 5ROSQYA2UPUS | No | 2.77 |
| 9 | E1KFG8JUGTS0 | E1KFG8JUGTS0 | Yes | 2.3 |
| 10 | PJQJ79BRZCDN | PJQJ79BRZECDN | No | 3.28 |
| 11 | G1LELR8TC2JY | G1LELR8TC2JY | Yes | 3.19 |
| 12 | SMNLANGC78U0 | SMNLANGC78U0 | Yes | 3.39 |
| 13 | S5VCULBPNNAC | S5VCULBPNNAC | Yes | 3.21 |
| 14 | OBWE8K25ZW5B | OBWE8K25ZW5B | Yes | 3.95 |
| 15 | S97G7ONH3SCB | S97G7QNH3SCB | No | 2.43 |
| 16 | 0Z53YYDZBJI0 | 0Z53YYDZBJI0 | Yes | 3.04 |
| 17 | JXY3REXL7R0T | JXY3REXL7R0T | Yes | 3.29 |
| 18 | HSZ1KQRU62NB | HSZ1KQRU62NB | Yes | 4.06 |
| 19 | BDW1O7PHFWYE | BDW107PHEWYE | No | 2.22 |
| 20 | XBAQXLDTQFHV | XBAQXLDTCFHV | No | 4.17 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 1.8 |
| 2 | 64 | 64 | Yes | 2.12 |
| 3 | 1440 | 1440 | Yes | 2.53 |
| 4 | 63 | 63 | Yes | 2.73 |
| 5 | 31 | 31 | Yes | 2.19 |
| 6 | 243 | 243 | Yes | 2.38 |
| 7 | 1 | 1 | Yes | 3.69 |
| 8 | 10 | 10 | Yes | 2.39 |
| 9 | 19 | 19 | Yes | 2.56 |
| 10 | 73 | 73 | Yes | 3.0 |
| 11 | 793 | 793 | Yes | 2.09 |
| 12 | 7 | 7 | Yes | 2.08 |
| 13 | 9 | 9 | Yes | 3.72 |
| 14 | 28 | 28 | Yes | 2.57 |
| 15 | 4096 | 1048576 | No | 6.51 |
| 16 | 20 | 20 | Yes | 7.77 |
| 17 | 3 | 3 | Yes | 4.75 |
| 18 | 67 | 67 | Yes | 2.52 |
| 19 | 9 | 9 | Yes | 3.67 |
| 20 | 198 | 198 | Yes | 5.64 |
