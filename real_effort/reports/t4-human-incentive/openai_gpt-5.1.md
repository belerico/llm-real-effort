# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
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
| sudoku_game | 8796 | 38931 | 47727 | 0 | 20 | 55.69 | 1114.09 |
| add_numbers | 7300 | 1462 | 8762 | 20 | 0 | 4.27 | 85.41 |
| counting_zeros | 7562 | 40758 | 48320 | 0 | 20 | 63.93 | 1278.83 |
| task_decoding | 10620 | 5844 | 16464 | 20 | 0 | 6.89 | 137.93 |
| task_summation | 7620 | 8690 | 16310 | 20 | 0 | 8.92 | 178.52 |
| task_transcription | 7380 | 4331 | 11711 | 19 | 1 | 5.97 | 119.49 |
| task_sequences | 3240 | 7422 | 10662 | 18 | 2 | 9.05 | 181.01 |
| **TOTAL** | **52518** | **107438** | **159956** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 5 3 2 2 6 4 6 2 3 3 1 4 |  | No | 58.9 |
| 2 | 6 4 3 1 6 5 3 2 2 6 1 4 2 4 |  | No | 83.72 |
| 3 | 6 5 1 2 3 2 1 3 4 2 6 1 2 4 |  | No | 63.69 |
| 4 | 3 1 5 6 2 1 2 1 6 3 1 2 5 6 |  | No | 56.42 |
| 5 | 5 1 3 5 6 4 6 3 5 2 4 4 2 1 |  | No | 58.03 |
| 6 | 3 3 6 1 3 6 4 5 4 2 3 4 2 6 |  | No | 28.84 |
| 7 | 4 5 1 3 6 4 1 5 3 2 2 1 1 2 |  | No | 51.77 |
| 8 | 4 1 4 2 6 1 4 1 4 6 4 3 4 1 |  | No | 49.5 |
| 9 | 3 2 1 3 6 1 3 5 2 1 6 5 5 1 |  | No | 55.91 |
| 10 | 6 2 2 3 4 2 3 5 1 5 6 2 3 1 | 6 2 1 4 2 6 3 2 4 5 6 2 1 6 2 1 | No | 12.15 |
| 11 | 5 2 1 5 2 3 1 6 3 2 4 6 2 1 |  | No | 60.23 |
| 12 | 3 1 6 1 6 6 2 5 3 3 5 3 1 4 |  | No | 58.77 |
| 13 | 2 6 4 3 6 4 6 2 1 6 1 3 5 4 |  | No | 39.8 |
| 14 | 2 5 6 6 2 1 4 2 3 1 4 2 3 5 |  | No | 70.71 |
| 15 | 3 3 4 4 5 1 3 3 2 4 1 5 5 2 |  | No | 67.7 |
| 16 | 3 2 6 4 1 6 6 3 4 5 4 3 2 5 |  | No | 30.81 |
| 17 | 2 5 4 1 6 2 4 5 5 2 1 6 2 3 |  | No | 59.27 |
| 18 | 5 6 4 4 3 1 5 1 6 4 3 2 1 3 |  | No | 63.76 |
| 19 | 5 3 2 6 1 4 2 1 1 5 2 3 6 5 |  | No | 71.18 |
| 20 | 4 1 2 3 5 6 5 6 2 6 1 5 5 2 |  | No | 72.71 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2288 | 2288 | Yes | 4.47 |
| 2 | 1947 | 1947 | Yes | 4.3 |
| 3 | 1308 | 1308 | Yes | 4.52 |
| 4 | 1013 | 1013 | Yes | 4.95 |
| 5 | 2364 | 2364 | Yes | 3.81 |
| 6 | 2143 | 2143 | Yes | 4.65 |
| 7 | 1684 | 1684 | Yes | 3.73 |
| 8 | 804 | 804 | Yes | 4.99 |
| 9 | 1254 | 1254 | Yes | 2.85 |
| 10 | 1216 | 1216 | Yes | 5.01 |
| 11 | 1566 | 1566 | Yes | 4.01 |
| 12 | 1146 | 1146 | Yes | 2.92 |
| 13 | 1769 | 1769 | Yes | 7.31 |
| 14 | 1710 | 1710 | Yes | 3.56 |
| 15 | 1385 | 1385 | Yes | 5.13 |
| 16 | 708 | 708 | Yes | 3.07 |
| 17 | 2030 | 2030 | Yes | 3.19 |
| 18 | 1488 | 1488 | Yes | 3.05 |
| 19 | 1694 | 1694 | Yes | 4.85 |
| 20 | 2099 | 2099 | Yes | 4.94 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 |  | No | 73.87 |
| 2 | 75 |  | No | 87.14 |
| 3 | 60 |  | No | 56.16 |
| 4 | 59 |  | No | 66.91 |
| 5 | 70 |  | No | 90.53 |
| 6 | 72 |  | No | 74.82 |
| 7 | 41 |  | No | 41.71 |
| 8 | 43 |  | No | 56.99 |
| 9 | 45 |  | No | 55.6 |
| 10 | 50 |  | No | 64.14 |
| 11 | 35 |  | No | 53.53 |
| 12 | 43 |  | No | 64.71 |
| 13 | 63 |  | No | 68.6 |
| 14 | 61 |  | No | 57.81 |
| 15 | 64 |  | No | 69.89 |
| 16 | 52 |  | No | 63.44 |
| 17 | 56 |  | No | 56.26 |
| 18 | 52 |  | No | 62.2 |
| 19 | 41 |  | No | 58.26 |
| 20 | 65 |  | No | 55.94 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZCEOLUM | ZCEOLUM | Yes | 10.17 |
| 2 | TBFCPQZ | TBFCPQZ | Yes | 8.36 |
| 3 | XNJWIYB | XNJWIYB | Yes | 8.42 |
| 4 | ZNOXITD | ZNOXITD | Yes | 7.08 |
| 5 | QLZGROH | QLZGROH | Yes | 5.73 |
| 6 | RTBSYFK | RTBSYFK | Yes | 6.3 |
| 7 | QXHUDJR | QXHUDJR | Yes | 5.37 |
| 8 | LVMZNFJ | LVMZNFJ | Yes | 6.12 |
| 9 | WVEIDLP | WVEIDLP | Yes | 6.97 |
| 10 | CQADMYJ | CQADMYJ | Yes | 6.84 |
| 11 | EVXJNFB | EVXJNFB | Yes | 4.07 |
| 12 | GHLXMNK | GHLXMNK | Yes | 6.14 |
| 13 | WFZLAIY | WFZLAIY | Yes | 6.09 |
| 14 | KLGSANV | KLGSANV | Yes | 7.87 |
| 15 | ETUXMHP | ETUXMHP | Yes | 7.54 |
| 16 | PENFSRG | PENFSRG | Yes | 8.73 |
| 17 | DCHFEXQ | DCHFEXQ | Yes | 4.69 |
| 18 | GFAKWVX | GFAKWVX | Yes | 4.71 |
| 19 | OPYVGHF | OPYVGHF | Yes | 6.3 |
| 20 | USXVAOP | USXVAOP | Yes | 10.22 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.15 |
| 2 | [3.8, 6.2] | 3.8 6.2 | Yes | 9.54 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.98 |
| 4 | [4.1, 5.9] | 5.9 4.1 | Yes | 7.9 |
| 5 | [3.3, 6.7] | 6.7 3.3 | Yes | 8.1 |
| 6 | [2.1, 7.9] | 2.1 7.9 | Yes | 9.13 |
| 7 | [4.3, 5.7] | 4.3 5.7 | Yes | 6.55 |
| 8 | [1.9, 8.1] | 8.1 1.9 | Yes | 10.21 |
| 9 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.32 |
| 10 | [1.5, 8.5] | 8.5 1.5 | Yes | 7.0 |
| 11 | [4.2, 5.8] | 4.2 5.8 | Yes | 12.48 |
| 12 | [4.9, 5.1] | 4.9 5.1 | Yes | 6.43 |
| 13 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.8 |
| 14 | [4.8, 5.2] | 5.2 4.8 | Yes | 9.64 |
| 15 | [4.4, 5.6] | 5.6 4.4 | Yes | 8.05 |
| 16 | [3.1, 6.9] | 3.1 6.9 | Yes | 6.97 |
| 17 | [2.3, 7.7] | 7.7 2.3 | Yes | 9.27 |
| 18 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.99 |
| 19 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.17 |
| 20 | [0.9, 9.1] | 9.1 0.9 | Yes | 15.63 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 8YELLNZ4JUYI | 8YELLNZ4JUYI | Yes | 3.93 |
| 2 | V811YPR48QPN | V811YPR48QPN | Yes | 27.86 |
| 3 | IV5TJ1T5F3OD | IV5TJ1T5F3OD | Yes | 5.06 |
| 4 | 1D787MWAEXMS | 1D787MWAEXMS | Yes | 10.35 |
| 5 | DMQX8NHFPH5Y | DMQX8NHFPH5Y | Yes | 4.85 |
| 6 | S5I8D2EQLDWM | S5I8D2EQLDWM | Yes | 2.57 |
| 7 | TNT9KW9U27CD | TNT9KW9U27CD | Yes | 1.59 |
| 8 | SXXSXORXG9BJ | SXXSXORXG9BJ | Yes | 4.27 |
| 9 | 3LK7Z2X6UNRN | 3LK7Z2X6UNRN | Yes | 4.63 |
| 10 | VTFD0BGVDSMC | VTFD0BGVDSMC | Yes | 2.63 |
| 11 | 98ZV76W886WF | 98ZV76W886WF | Yes | 1.43 |
| 12 | F61C93Z5NCL0 | F61C9Z5NCL0 | No | 6.71 |
| 13 | BK0F8PJ6ZMDE | BK0F8PJ6ZMDE | Yes | 3.71 |
| 14 | P39G6H4L90KM | P39G6H4L90KM | Yes | 3.15 |
| 15 | UB1TNBTIW6ID | UB1TNBTIW6ID | Yes | 3.64 |
| 16 | ZRRDE9PGPC1W | ZRRDE9PGPC1W | Yes | 3.78 |
| 17 | 0X1MVTVP8AI8 | 0X1MVTVP8AI8 | Yes | 17.6 |
| 18 | 9NYRW1DN41BY | 9NYRW1DN41BY | Yes | 1.67 |
| 19 | RPWVKVHDRQP4 | RPWVKVHDRQP4 | Yes | 5.45 |
| 20 | HH5Q7NI69HCN | HH5Q7NI69HCN | Yes | 4.49 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 4.12 |
| 2 | 36 | 36 | Yes | 4.06 |
| 3 | 5 | 5 | Yes | 5.89 |
| 4 | 60 | 60 | Yes | 5.43 |
| 5 | 9 | 9 | Yes | 4.03 |
| 6 | 26 |  | No | 47.28 |
| 7 | 10 | 10 | Yes | 5.53 |
| 8 | 16 | 16 | Yes | 3.49 |
| 9 | 1 | 1 | Yes | 4.27 |
| 10 | 23 | 23 | Yes | 3.37 |
| 11 | 48 | 48 | Yes | 3.12 |
| 12 | 7 | 7 | Yes | 3.55 |
| 13 | 73 | 73 | Yes | 3.55 |
| 14 | 6 | 6 | Yes | 4.47 |
| 15 | 3 | 3 | Yes | 8.67 |
| 16 | 5 |  | No | 41.42 |
| 17 | 28 | 28 | Yes | 8.3 |
| 18 | 20 | 20 | Yes | 9.48 |
| 19 | 31 | 31 | Yes | 4.65 |
| 20 | 60 | 60 | Yes | 6.31 |
