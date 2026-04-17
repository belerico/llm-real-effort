# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8720 | 40960 | 49680 | 0 | 20 | 41.63 | 832.81 |
| add_numbers | 4240 | 3940 | 8180 | 20 | 0 | 3.37 | 67.5 |
| counting_zeros | 7277 | 38912 | 46189 | 0 | 20 | 42.02 | 840.63 |
| task_decoding | 15700 | 26520 | 42220 | 13 | 7 | 20.03 | 400.74 |
| task_summation | 8920 | 20033 | 28953 | 19 | 1 | 11.22 | 224.67 |
| task_transcription | 3930 | 11492 | 15422 | 15 | 5 | 6.14 | 123.01 |
| task_sequences | 2901 | 14477 | 17378 | 17 | 3 | 10.41 | 208.18 |
| **TOTAL** | **51688** | **156334** | **208022** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 6 2 1 4 2 1 4 2 3 1 1 3 |  | No | 32.16 |
| 2 | 3 3 6 3 3 5 5 3 2 4 1 2 4 6 |  | No | 36.72 |
| 3 | 6 1 5 3 1 4 3 6 3 6 1 4 5 3 |  | No | 37.51 |
| 4 | 3 5 6 1 5 3 2 5 3 4 1 6 6 5 |  | No | 43.18 |
| 5 | 4 3 2 3 4 6 4 2 2 6 4 2 1 6 |  | No | 57.08 |
| 6 | 6 2 6 3 2 5 2 3 6 2 5 2 4 1 |  | No | 23.31 |
| 7 | 1 2 2 4 1 3 3 6 4 6 5 6 2 4 |  | No | 39.4 |
| 8 | 6 4 1 1 4 2 5 3 3 2 1 6 2 3 |  | No | 36.14 |
| 9 | 6 2 4 4 2 2 6 2 4 6 5 3 1 2 |  | No | 59.57 |
| 10 | 6 4 2 5 6 3 2 5 3 6 4 1 4 2 |  | No | 47.77 |
| 11 | 4 2 1 2 4 2 3 2 3 2 4 5 1 2 |  | No | 22.86 |
| 12 | 4 1 3 2 2 1 3 1 5 1 6 1 4 3 |  | No | 27.84 |
| 13 | 4 5 1 6 3 2 3 3 6 1 6 5 3 4 |  | No | 40.75 |
| 14 | 2 3 1 2 3 2 3 1 3 2 1 4 2 3 |  | No | 42.36 |
| 15 | 1 6 5 5 6 1 1 2 5 6 3 1 1 3 |  | No | 50.22 |
| 16 | 1 5 4 1 6 2 3 5 6 4 1 1 3 6 |  | No | 45.25 |
| 17 | 1 2 2 4 1 3 4 6 3 1 5 4 6 2 |  | No | 43.1 |
| 18 | 5 2 6 3 6 5 1 3 6 6 3 3 2 6 |  | No | 18.62 |
| 19 | 1 4 5 2 4 4 3 4 2 1 3 5 5 3 |  | No | 72.22 |
| 20 | 3 4 1 1 6 3 2 6 1 3 1 4 1 6 |  | No | 56.52 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1957 | 1957 | Yes | 2.76 |
| 2 | 1968 | 1968 | Yes | 2.95 |
| 3 | 1341 | 1341 | Yes | 3.31 |
| 4 | 1734 | 1734 | Yes | 3.4 |
| 5 | 2168 | 2168 | Yes | 3.13 |
| 6 | 697 | 697 | Yes | 3.01 |
| 7 | 1700 | 1700 | Yes | 5.52 |
| 8 | 1745 | 1745 | Yes | 4.79 |
| 9 | 2284 | 2284 | Yes | 3.67 |
| 10 | 1330 | 1330 | Yes | 2.75 |
| 11 | 1426 | 1426 | Yes | 2.69 |
| 12 | 1869 | 1869 | Yes | 3.32 |
| 13 | 910 | 910 | Yes | 4.46 |
| 14 | 1788 | 1788 | Yes | 4.12 |
| 15 | 1128 | 1128 | Yes | 3.54 |
| 16 | 1944 | 1944 | Yes | 3.13 |
| 17 | 1526 | 1526 | Yes | 2.24 |
| 18 | 1464 | 1464 | Yes | 2.24 |
| 19 | 1374 | 1374 | Yes | 3.56 |
| 20 | 2092 | 2092 | Yes | 2.82 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 |  | No | 48.1 |
| 2 | 49 |  | No | 24.95 |
| 3 | 62 |  | No | 68.21 |
| 4 | 42 |  | No | 27.89 |
| 5 | 56 |  | No | 24.75 |
| 6 | 72 |  | No | 54.56 |
| 7 | 69 |  | No | 37.88 |
| 8 | 70 |  | No | 20.51 |
| 9 | 63 |  | No | 34.28 |
| 10 | 50 |  | No | 30.62 |
| 11 | 38 |  | No | 38.88 |
| 12 | 67 |  | No | 16.95 |
| 13 | 52 |  | No | 49.83 |
| 14 | 55 |  | No | 44.45 |
| 15 | 37 |  | No | 47.06 |
| 16 | 55 |  | No | 15.84 |
| 17 | 70 | TIMEOUT | No | 120.03 |
| 18 | 66 |  | No | 26.53 |
| 19 | 61 |  | No | 63.19 |
| 20 | 68 |  | No | 45.81 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NUPCKEL |  | No | 42.86 |
| 2 | LNFCYAV | LNFCYAV | Yes | 14.63 |
| 3 | MWEUZKB | MWEUZKB | Yes | 4.64 |
| 4 | QGWRZBJ | QGWRZBJ | Yes | 9.68 |
| 5 | QZFMAVN | QZFMAVN | Yes | 5.36 |
| 6 | HBVUOLF |  | No | 45.24 |
| 7 | GIKVDMP | GIKVDMP | Yes | 12.56 |
| 8 | ABKLHCO |  | No | 38.11 |
| 9 | RSHZWPB | RSHZWPB | Yes | 8.19 |
| 10 | TNUOSPD |  | No | 36.28 |
| 11 | QSEWGZK |  | No | 35.67 |
| 12 | YPRWSZJ |  | No | 26.59 |
| 13 | MEUTDOF | MEUTDOF | Yes | 18.54 |
| 14 | ARHYSMX |  | No | 38.81 |
| 15 | KPVRDHJ | KPVRDHJ | Yes | 10.74 |
| 16 | SKIDTNU | SKIDTNU | Yes | 8.14 |
| 17 | OVYXWSK | OVYXWSK | Yes | 12.74 |
| 18 | CONIEHA | CONIEHA | Yes | 11.47 |
| 19 | BNPFSKM | BNPFSKM | Yes | 6.62 |
| 20 | JUPTGQM | JUPTGQM | Yes | 13.65 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.8, 9.2] | 0.8 9.2 | Yes | 12.08 |
| 2 | [0.5, 9.5] | 0.5 9.5 | Yes | 13.77 |
| 3 | [0.5, 9.5] | 0.5 9.5 | Yes | 12.53 |
| 4 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.82 |
| 5 | [2.6, 7.4] | 2.6 7.4 | Yes | 9.65 |
| 6 | [3.0, 7.0] |  | No | 27.14 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.99 |
| 8 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.58 |
| 9 | [1.2, 8.8] | 8.8 1.2 | Yes | 7.22 |
| 10 | [1.1, 8.9] | 8.9 1.1 | Yes | 17.4 |
| 11 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.63 |
| 12 | [3.8, 6.2] | 3.8 6.2 | Yes | 9.56 |
| 13 | [0.9, 9.1] | 9.1 0.9 | Yes | 8.91 |
| 14 | [3.2, 6.8] | 3.2 6.8 | Yes | 9.92 |
| 15 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.66 |
| 16 | [3.0, 7.0] | 3.0 7.0 | Yes | 9.59 |
| 17 | [3.2, 6.8] | 3.2 6.8 | Yes | 11.96 |
| 18 | [4.2, 5.8] | 4.2 5.8 | Yes | 10.24 |
| 19 | [4.6, 5.4] | 4.6 5.4 | Yes | 9.9 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 7.95 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IZI9I21M1WM1 | IZI9I21M1WM1 | Yes | 6.59 |
| 2 | O2R89HX0BE8H | O2R89HX0BE8H | Yes | 9.27 |
| 3 | BGW93J8VSJY6 | BGW93J8VSJY6 | Yes | 2.4 |
| 4 | OUU5ZR9S9X0J | OUU5ZR9S9X0J | Yes | 4.38 |
| 5 | XW5G0QPGY0TB | XW5G0QPGY0TE | No | 4.09 |
| 6 | CTTLNLS43LTT |  | No | 21.24 |
| 7 | LRXR6I0QUITZ | LRXR610QUITZ | No | 1.82 |
| 8 | M3K8HZXQO3W0 | M3K8HZXQO3W0 | Yes | 2.75 |
| 9 | 7LAG8OPN4AEX | 7LAG8OPN4AEX | Yes | 3.08 |
| 10 | NQ8V01K00ECS | NQ8V01K00ECS | Yes | 3.37 |
| 11 | ELBH2GE5NXO2 | ELBH2GE5NXO2 | Yes | 2.81 |
| 12 | 5IBCB4R78RJ2 | 5IBCB4R78RJ2 | Yes | 19.41 |
| 13 | 9X2IAUA4BGG1 | 9X2IAUA4BGG1 | Yes | 5.09 |
| 14 | BTEMTIK5YTO9 | BTEMTIK5YTO9 | Yes | 2.29 |
| 15 | QYORAH8Q6PI5 | QYORAH8Q6PI5 | Yes | 5.67 |
| 16 | KO9GJVOXL5GF | K09GJVOXL5GF | No | 3.8 |
| 17 | G9WM0715MYBG | G9WM0715MYBG | Yes | 4.66 |
| 18 | 75DQQODYEV06 | 75DQOODYEV06 | No | 15.21 |
| 19 | L88GUD60ZNCR | L88GUD60ZNCR | Yes | 2.3 |
| 20 | JBFN9LPO97II | JBFN9LPO97II | Yes | 2.65 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 9.04 |
| 2 | 4 | 4 | Yes | 3.9 |
| 3 | 39 | 39 | Yes | 5.46 |
| 4 | 4096 |  | No | 32.16 |
| 5 | 48 | 48 | Yes | 3.39 |
| 6 | 23 | 23 | Yes | 3.09 |
| 7 | 6 | 6 | Yes | 7.15 |
| 8 | 26 | 26 | Yes | 15.35 |
| 9 | 60 | 60 | Yes | 7.11 |
| 10 | 5 |  | No | 35.53 |
| 11 | 19 | 19 | Yes | 6.24 |
| 12 | 64 | 64 | Yes | 20.16 |
| 13 | 1440 | 1440 | Yes | 2.74 |
| 14 | 20 | 20 | Yes | 12.74 |
| 15 | 3 | 3 | Yes | 4.84 |
| 16 | 60 |  | No | 23.29 |
| 17 | 5 | 5 | Yes | 2.71 |
| 18 | 3 | 3 | Yes | 4.45 |
| 19 | 65 | 65 | Yes | 5.52 |
| 20 | 243 | 243 | Yes | 3.31 |
