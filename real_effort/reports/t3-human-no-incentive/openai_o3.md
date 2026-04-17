# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 8400 | 40803 | 49203 | 0 | 20 | 76.19 | 1523.99 |
| add_numbers | 7420 | 2903 | 10323 | 20 | 0 | 3.55 | 71.11 |
| counting_zeros | 7480 | 38996 | 46476 | 0 | 20 | 47.56 | 951.56 |
| task_decoding | 10940 | 8883 | 19823 | 20 | 0 | 10.02 | 200.69 |
| task_summation | 7740 | 13613 | 21353 | 20 | 0 | 12.41 | 248.47 |
| task_transcription | 7500 | 11160 | 18660 | 15 | 5 | 12.53 | 250.76 |
| task_sequences | 3060 | 11592 | 14652 | 18 | 2 | 13.45 | 268.98 |
| **TOTAL** | **52540** | **127950** | **180490** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 4 1 6 5 4 2 6 1 3 4 6 4 3 |  | No | 77.83 |
| 2 | 1 4 2 6 6 2 1 3 4 6 3 3 2 6 |  | No | 76.78 |
| 3 | 5 3 6 2 1 4 5 1 5 4 3 6 5 1 | Answer: | No | 28.44 |
| 4 | 4 1 3 6 2 6 3 6 3 1 2 4 3 2 |  | No | 61.31 |
| 5 | 1 6 2 1 3 6 3 1 4 3 6 4 2 4 |  | No | 99.14 |
| 6 | 4 6 1 4 2 4 6 1 3 5 4 4 3 3 |  | No | 61.92 |
| 7 | 2 3 5 1 3 2 1 2 1 2 4 4 6 3 |  | No | 117.0 |
| 8 | 6 4 2 1 4 5 2 4 1 3 1 2 4 5 |  | No | 118.17 |
| 9 | 6 1 6 3 3 5 4 6 1 1 3 1 4 4 |  | No | 89.59 |
| 10 | 5 4 2 1 5 2 4 1 4 6 1 5 6 3 |  | No | 54.79 |
| 11 | 3 6 3 2 2 6 3 2 4 3 6 1 3 5 |  | No | 92.03 |
| 12 | 2 3 1 1 5 6 2 1 4 6 1 5 1 3 |  | No | 83.5 |
| 13 | 2 1 2 3 5 3 4 6 5 6 2 3 3 4 |  | No | 77.22 |
| 14 | 6 1 5 3 4 6 2 3 4 5 5 4 3 5 |  | No | 94.58 |
| 15 | 4 2 6 3 2 2 1 4 2 4 5 2 3 6 |  | No | 71.21 |
| 16 | 2 3 6 1 5 4 5 3 2 6 4 6 5 3 |  | No | 59.61 |
| 17 | 5 3 1 5 4 6 3 6 5 2 2 4 5 4 |  | No | 71.54 |
| 18 | 1 6 2 3 1 5 3 6 3 4 5 2 3 2 |  | No | 66.91 |
| 19 | 3 2 4 1 3 5 1 6 3 5 1 6 5 4 |  | No | 66.11 |
| 20 | 5 6 2 5 3 2 6 3 2 4 6 3 1 3 |  | No | 56.11 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1683 | 1683 | Yes | 4.2 |
| 2 | 2170 | 2170 | Yes | 3.85 |
| 3 | 1488 | 1488 | Yes | 2.78 |
| 4 | 1276 | 1276 | Yes | 5.07 |
| 5 | 1807 | 1807 | Yes | 3.53 |
| 6 | 1475 | 1475 | Yes | 4.0 |
| 7 | 801 | 801 | Yes | 3.72 |
| 8 | 1637 | 1637 | Yes | 2.79 |
| 9 | 2144 | 2144 | Yes | 5.54 |
| 10 | 2089 | 2089 | Yes | 2.77 |
| 11 | 1498 | 1498 | Yes | 4.28 |
| 12 | 1223 | 1223 | Yes | 3.03 |
| 13 | 1498 | 1498 | Yes | 3.56 |
| 14 | 1091 | 1091 | Yes | 2.74 |
| 15 | 1517 | 1517 | Yes | 3.31 |
| 16 | 2263 | 2263 | Yes | 3.25 |
| 17 | 736 | 736 | Yes | 3.76 |
| 18 | 1932 | 1932 | Yes | 2.58 |
| 19 | 1831 | 1831 | Yes | 3.86 |
| 20 | 2078 | 2078 | Yes | 2.4 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 53.61 |
| 2 | 55 |  | No | 39.99 |
| 3 | 40 |  | No | 51.71 |
| 4 | 53 |  | No | 49.57 |
| 5 | 64 |  | No | 50.62 |
| 6 | 35 |  | No | 65.79 |
| 7 | 68 |  | No | 63.0 |
| 8 | 69 |  | No | 55.42 |
| 9 | 71 | 67 | No | 23.36 |
| 10 | 64 |  | No | 39.35 |
| 11 | 55 |  | No | 56.44 |
| 12 | 38 |  | No | 37.7 |
| 13 | 67 |  | No | 66.91 |
| 14 | 35 |  | No | 61.6 |
| 15 | 52 |  | No | 40.03 |
| 16 | 35 | 67 | No | 30.41 |
| 17 | 63 | 67 | No | 42.01 |
| 18 | 64 |  | No | 48.59 |
| 19 | 35 | 67 | No | 33.35 |
| 20 | 57 |  | No | 41.77 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GWFAZKV | GWFAZKV | Yes | 13.51 |
| 2 | FMONLHY | FMONLHY | Yes | 12.15 |
| 3 | FMSCHNR | FMSCHNR | Yes | 19.91 |
| 4 | XYAKNEP | XYAKNEP | Yes | 10.28 |
| 5 | DZCMXVJ | DZCMXVJ | Yes | 5.09 |
| 6 | AHTSPFQ | AHTSPFQ | Yes | 11.78 |
| 7 | XQDYHMW | XQDYHMW | Yes | 8.08 |
| 8 | EARUXPY | EARUXPY | Yes | 17.01 |
| 9 | PHGXWZC | PHGXWZC | Yes | 5.2 |
| 10 | IUQELXH | IUQELXH | Yes | 6.4 |
| 11 | DAGSKTU | DAGSKTU | Yes | 5.66 |
| 12 | EZKMVSP | EZKMVSP | Yes | 13.45 |
| 13 | XFNKPVE | XFNKPVE | Yes | 11.42 |
| 14 | VOJKCEN | VOJKCEN | Yes | 15.24 |
| 15 | EHQTAYN | EHQTAYN | Yes | 9.49 |
| 16 | ANYMTOL | ANYMTOL | Yes | 6.25 |
| 17 | HBTLVAJ | HBTLVAJ | Yes | 5.97 |
| 18 | UVKSQRJ | UVKSQRJ | Yes | 8.62 |
| 19 | BGFPHWQ | BGFPHWQ | Yes | 10.45 |
| 20 | CHQSJKL | CHQSJKL | Yes | 4.52 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.17 |
| 2 | [4.4, 5.6] | 5.6 4.4 | Yes | 17.87 |
| 3 | [3.0, 7.0] | 3.0 7.0 | Yes | 12.52 |
| 4 | [2.8, 7.2] | 2.8 7.2 | Yes | 19.76 |
| 5 | [3.5, 6.5] | 3.5 6.5 | Yes | 20.49 |
| 6 | [4.6, 5.4] | 4.6 5.4 | Yes | 13.58 |
| 7 | [1.7, 8.3] | 1.7 8.3 | Yes | 13.11 |
| 8 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.25 |
| 9 | [1.9, 8.1] | 1.9 8.1 | Yes | 14.33 |
| 10 | [2.4, 7.6] | 2.4 7.6 | Yes | 14.12 |
| 11 | [0.9, 9.1] | 0.9 9.1 | Yes | 12.06 |
| 12 | [0.5, 9.5] | 0.5 9.5 | Yes | 11.31 |
| 13 | [4.3, 5.7] | 5.7 4.3 | Yes | 9.07 |
| 14 | [2.5, 7.5] | 2.5 7.5 | Yes | 10.66 |
| 15 | [4.5, 5.5] | 5.5 4.5 | Yes | 8.1 |
| 16 | [2.2, 7.8] | 2.2 7.8 | Yes | 9.11 |
| 17 | [2.1, 7.9] | 2.1 7.9 | Yes | 11.2 |
| 18 | [3.6, 6.4] | 3.6 6.4 | Yes | 11.69 |
| 19 | [2.3, 7.7] | 2.3 7.7 | Yes | 12.02 |
| 20 | [4.0, 6.0] | 4.0 6.0 | Yes | 8.84 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AH1BBSZW8T7H | AH1BBSZW8T7H | Yes | 12.13 |
| 2 | 4MUI5E4O5HBO | 4MUI5E405HBO | No | 29.18 |
| 3 | K0O1MOZWNAPL | K001MOZWNAPL | No | 9.78 |
| 4 | M490D53S18RE | M490D53S18RE | Yes | 18.06 |
| 5 | 4JQPNGEYCK9J | 4JQPNGEYCK9J | Yes | 3.89 |
| 6 | Z6MCGQP0I4UV | Z6MCGQP014UV | No | 21.65 |
| 7 | O7135PDLTJ63 | O7135PDLTJ63 | Yes | 4.64 |
| 8 | U5QL7E5NOIQW | U5QL7E5NOIQW | Yes | 13.27 |
| 9 | 0FUGCZN77CQM | 0FUGCZN77CQM | Yes | 15.55 |
| 10 | D0XQ8J5J6NFY | D0XQ8J5J6NFY | Yes | 12.26 |
| 11 | NS5VXXC0KHDF | NS5VXXC0KHDF | Yes | 10.07 |
| 12 | BYWW0JLQ0JH6 | BYWWQL0QJH6 | No | 21.5 |
| 13 | AJMJNRRYICL4 | AJMJNRRYICL4 | Yes | 20.98 |
| 14 | 72I9R7QXG99X | 7219R7QXG99X | No | 18.61 |
| 15 | AASCTR3T61WG | AASCTR3T61WG | Yes | 4.6 |
| 16 | 71LJL7DFPNSI | 71LJL7DFPNSI | Yes | 8.87 |
| 17 | 7KW2S6ARQS63 | 7KW2S6ARQS63 | Yes | 11.48 |
| 18 | WD9QVXRFJ5J3 | WD9QVXRFJ5J3 | Yes | 5.26 |
| 19 | PRA63R497DC4 | PRA63R497DC4 | Yes | 4.4 |
| 20 | K8SK7433IP9H | K8SK7433IP9H | Yes | 4.46 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 |  | No | 48.67 |
| 2 | 793 | 793 | Yes | 5.38 |
| 3 | 60 | 60 | Yes | 3.86 |
| 4 | 7 | 7 | Yes | 4.23 |
| 5 | 28 | 28 | Yes | 9.54 |
| 6 | 64 | 64 | Yes | 8.51 |
| 7 | 20 |  | No | 59.44 |
| 8 | 73 | 73 | Yes | 10.93 |
| 9 | 26 | 26 | Yes | 18.44 |
| 10 | 23 | 23 | Yes | 6.43 |
| 11 | 6 | 6 | Yes | 7.39 |
| 12 | 31 | 31 | Yes | 5.33 |
| 13 | 67 | 67 | Yes | 6.44 |
| 14 | 3 | 3 | Yes | 27.68 |
| 15 | 4 | 4 | Yes | 9.48 |
| 16 | 48 | 48 | Yes | 2.91 |
| 17 | 44 | 44 | Yes | 9.73 |
| 18 | 4 | 4 | Yes | 3.7 |
| 19 | 60 | 60 | Yes | 10.85 |
| 20 | 7680 | 7680 | Yes | 10.02 |
