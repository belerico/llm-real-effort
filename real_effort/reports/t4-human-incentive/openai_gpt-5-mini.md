# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
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
| sudoku_game | 7540 | 40960 | 48500 | 0 | 20 | 72.31 | 1446.33 |
| add_numbers | 4120 | 4914 | 9034 | 20 | 0 | 6.62 | 132.44 |
| counting_zeros | 6213 | 31543 | 37756 | 0 | 20 | 55.05 | 1101.36 |
| task_decoding | 12280 | 15583 | 27863 | 19 | 1 | 17.65 | 353.15 |
| task_summation | 7480 | 11521 | 19001 | 20 | 0 | 9.93 | 198.75 |
| task_transcription | 3944 | 18956 | 22900 | 16 | 4 | 16.77 | 335.44 |
| task_sequences | 3241 | 18434 | 21675 | 13 | 7 | 17.63 | 352.66 |
| **TOTAL** | **44818** | **141911** | **186729** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 1 2 3 6 2 6 4 6 5 2 5 3 |  | No | 75.81 |
| 2 | 1 3 2 6 4 5 4 6 5 1 6 4 3 2 |  | No | 60.91 |
| 3 | 1 6 5 3 3 1 4 6 4 1 3 1 4 3 |  | No | 57.33 |
| 4 | 6 3 1 5 3 1 5 4 5 6 3 5 6 6 |  | No | 68.62 |
| 5 | 1 5 3 3 5 6 2 6 3 3 4 1 6 3 |  | No | 53.28 |
| 6 | 1 4 4 5 3 1 4 2 6 3 5 2 5 6 |  | No | 65.61 |
| 7 | 5 6 3 1 3 5 4 5 3 1 6 3 1 2 |  | No | 69.89 |
| 8 | 5 4 6 5 6 6 2 4 1 3 3 4 6 1 |  | No | 69.87 |
| 9 | 6 6 4 1 2 4 6 6 3 2 5 1 4 3 |  | No | 89.41 |
| 10 | 6 1 1 4 4 2 6 4 1 5 2 3 2 1 |  | No | 70.99 |
| 11 | 1 2 4 5 1 3 4 1 2 4 1 1 6 3 |  | No | 80.82 |
| 12 | 4 6 5 6 3 4 1 1 6 3 4 6 1 3 |  | No | 67.66 |
| 13 | 2 6 4 3 1 4 3 6 1 4 2 6 4 3 |  | No | 86.83 |
| 14 | 3 3 6 5 6 5 1 4 2 1 4 4 6 5 |  | No | 101.41 |
| 15 | 3 1 5 2 2 3 1 6 5 2 4 1 3 4 |  | No | 66.97 |
| 16 | 4 6 2 3 4 5 4 6 1 6 1 4 6 5 |  | No | 74.96 |
| 17 | 2 4 4 6 2 1 5 5 2 5 6 4 4 1 |  | No | 79.79 |
| 18 | 3 2 1 5 4 6 1 4 5 4 1 1 5 6 |  | No | 68.1 |
| 19 | 1 3 1 6 2 4 1 5 6 2 6 3 5 4 |  | No | 90.27 |
| 20 | 2 1 3 6 1 5 6 3 1 1 2 3 3 1 |  | No | 47.6 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2036 | 2036 | Yes | 6.74 |
| 2 | 925 | 925 | Yes | 6.2 |
| 3 | 451 | 451 | Yes | 4.17 |
| 4 | 1242 | 1242 | Yes | 9.47 |
| 5 | 1719 | 1719 | Yes | 7.85 |
| 6 | 799 | 799 | Yes | 8.08 |
| 7 | 796 | 796 | Yes | 7.3 |
| 8 | 2572 | 2572 | Yes | 7.45 |
| 9 | 1294 | 1294 | Yes | 5.3 |
| 10 | 2150 | 2150 | Yes | 7.31 |
| 11 | 1703 | 1703 | Yes | 5.22 |
| 12 | 1820 | 1820 | Yes | 6.07 |
| 13 | 2019 | 2019 | Yes | 7.28 |
| 14 | 1220 | 1220 | Yes | 7.64 |
| 15 | 941 | 941 | Yes | 5.99 |
| 16 | 1468 | 1468 | Yes | 9.01 |
| 17 | 2125 | 2125 | Yes | 3.64 |
| 18 | 2262 | 2262 | Yes | 5.14 |
| 19 | 1771 | 1771 | Yes | 4.58 |
| 20 | 1442 | 1442 | Yes | 7.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 | 67 | No | 28.13 |
| 2 | 73 |  | No | 69.83 |
| 3 | 57 |  | No | 79.62 |
| 4 | 58 | 67 | No | 35.18 |
| 5 | 57 |  | No | 76.44 |
| 6 | 73 | 67 | No | 33.68 |
| 7 | 37 |  | No | 83.4 |
| 8 | 42 | 67 | No | 29.56 |
| 9 | 65 | TIMEOUT | No | 120.03 |
| 10 | 58 | 67 | No | 43.58 |
| 11 | 72 | 67 | No | 32.31 |
| 12 | 67 |  | No | 108.73 |
| 13 | 56 | 67 | No | 39.84 |
| 14 | 35 |  | No | 83.25 |
| 15 | 68 |  | No | 76.57 |
| 16 | 54 | 67 | No | 19.55 |
| 17 | 63 | 67 | No | 25.45 |
| 18 | 66 | 67 | No | 25.12 |
| 19 | 68 | 67 | No | 17.38 |
| 20 | 62 |  | No | 73.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JKNQPSG | JKNQPSG | Yes | 8.82 |
| 2 | KGSUBRF | KGSUBRF | Yes | 18.27 |
| 3 | KNZTMXO | KNZTMXO | Yes | 12.41 |
| 4 | TGCZSPY | TGCZSPY | Yes | 12.44 |
| 5 | SFCOJLU | SFCOJLU | Yes | 22.05 |
| 6 | CYKJMOI | CYKJMOI | Yes | 14.0 |
| 7 | OEYQZXN | OEYQZXN | Yes | 11.06 |
| 8 | GXUMBVD | GXUMBVD | Yes | 16.42 |
| 9 | PVIORHL | PVIORHL | Yes | 24.4 |
| 10 | FINEUKR | FINEUKR | Yes | 22.6 |
| 11 | PBZEWYC | PBZEWYC | Yes | 11.25 |
| 12 | LQATIYO | LQATIYO | Yes | 11.98 |
| 13 | JVROLPZ | JVROLPZ | Yes | 17.24 |
| 14 | RUFWDGC | RUFWDGC | Yes | 16.18 |
| 15 | BGMXRPW | BGMXRPW | Yes | 11.66 |
| 16 | OPQKSXW | OPQKSXW | Yes | 19.52 |
| 17 | IJHDOWR |  | No | 57.92 |
| 18 | JXEOYVA | JXEOYVA | Yes | 14.64 |
| 19 | KFTRYCG | KFTRYCG | Yes | 19.52 |
| 20 | NHXMPAZ | NHXMPAZ | Yes | 10.53 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.25 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 10.79 |
| 3 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.51 |
| 4 | [4.5, 5.5] | 4.5 5.5 | Yes | 11.3 |
| 5 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.73 |
| 6 | [2.9, 7.1] | 7.1 2.9 | Yes | 14.94 |
| 7 | [0.4, 9.6] | 9.6 0.4 | Yes | 9.47 |
| 8 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.82 |
| 9 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.27 |
| 10 | [2.6, 7.4] | 7.4 2.6 | Yes | 10.04 |
| 11 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.96 |
| 12 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.8 |
| 13 | [4.4, 5.6] | 5.6 4.4 | Yes | 12.47 |
| 14 | [3.8, 6.2] | 3.8 6.2 | Yes | 10.8 |
| 15 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.48 |
| 16 | [2.7, 7.3] | 2.7 7.3 | Yes | 9.82 |
| 17 | [0.2, 9.8] | 9.8 0.2 | Yes | 8.53 |
| 18 | [1.0, 9.0] | 9.0 1.0 | Yes | 11.95 |
| 19 | [2.0, 8.0] | 2.0 8.0 | Yes | 7.61 |
| 20 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.99 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2V7LUU4EVD4J | 2V7LUU4EVD4J | Yes | 12.65 |
| 2 | 2RK8KO1ENJ8E | 2RK8KO1ENJ8E | Yes | 12.76 |
| 3 | 52HWPHJQW1YV | 52WHPHJQW1YV | No | 21.19 |
| 4 | 2T05PYXS4Z4Q | 2T05PYXS4Z4Q | Yes | 10.32 |
| 5 | 63D0SVUGL4ND | 63D0SVUGL4ND | Yes | 18.34 |
| 6 | XHUBY9Q2LCFS | XHUBY9Q2LCFS | Yes | 7.63 |
| 7 | YEHTBZFB9HJY | YEHTBZFB9HJY | Yes | 9.37 |
| 8 | OIL2HUIFU887 | OIL2HUIFU887 | Yes | 10.75 |
| 9 | G893M4XAVN63 | G893M4XAVN63 | Yes | 7.11 |
| 10 | 6QMCBALZNSM3 | 6QMCBALZNSM3 | Yes | 3.51 |
| 11 | S5BJFWNMTVZ8 | S5BJFWNMTVZ8 | Yes | 21.86 |
| 12 | RP7T6UKGXW98 | RP7T6UKGXW98 | Yes | 7.65 |
| 13 | RU0ORVG8DPSB | RUOORVG8DPSB | No | 20.24 |
| 14 | 7BWO7IIMLTRQ |  | No | 49.03 |
| 15 | MB6IQUV1BOW0 | MB6IQUV1BOW0 | Yes | 15.91 |
| 16 | TS8H3M14ZIS5 | TS8H3M14ZIS5 | Yes | 29.26 |
| 17 | H0892W7N6LY0 | H0892W7N6LY0 | Yes | 25.71 |
| 18 | DOZ9FWHLID1H | DOZ9FWHLID1H | Yes | 9.0 |
| 19 | 0OSV3ZF1H5VK | OOSV3ZF1H5VK | No | 29.88 |
| 20 | 8GMLR4YKC7BA | 8GMLR4YKC7BA | Yes | 13.14 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 14.53 |
| 2 | 4096 | 42 | No | 24.09 |
| 3 | 19 | 19 | Yes | 9.93 |
| 4 | 48 | 42 | No | 7.68 |
| 5 | 6 | 6 | Yes | 18.39 |
| 6 | 63 | 63 | Yes | 12.93 |
| 7 | 44 | 44 | Yes | 22.09 |
| 8 | 23 | 42 | No | 22.36 |
| 9 | 198 | 42 | No | 11.5 |
| 10 | 67 | 67 | Yes | 11.39 |
| 11 | 10 | 42 | No | 16.76 |
| 12 | 4 | 4 | Yes | 30.71 |
| 13 | 243 | 243 | Yes | 24.15 |
| 14 | 64 | 42 | No | 19.59 |
| 15 | 4 | 4 | Yes | 17.0 |
| 16 | 31 | 31 | Yes | 13.99 |
| 17 | 39 | 42 | No | 23.54 |
| 18 | 65 | 65 | Yes | 26.61 |
| 19 | 7680 | 7680 | Yes | 14.63 |
| 20 | 60 | 60 | Yes | 10.78 |
