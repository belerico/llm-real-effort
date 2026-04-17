# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
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
| sudoku_game | 7360 | 40960 | 48320 | 0 | 20 | 73.19 | 1464.12 |
| add_numbers | 3940 | 6550 | 10490 | 20 | 0 | 9.32 | 186.45 |
| counting_zeros | 6360 | 36853 | 43213 | 0 | 20 | 53.90 | 1078.23 |
| task_decoding | 12100 | 14099 | 26199 | 20 | 0 | 13.31 | 266.36 |
| task_summation | 7300 | 14343 | 21643 | 20 | 0 | 12.66 | 253.37 |
| task_transcription | 3764 | 18719 | 22483 | 14 | 6 | 22.71 | 454.39 |
| task_sequences | 3061 | 18618 | 21679 | 5 | 15 | 20.13 | 402.54 |
| **TOTAL** | **43885** | **150142** | **194027** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 6 4 6 3 1 3 4 2 5 1 6 3 |  | No | 59.54 |
| 2 | 4 1 2 2 5 6 6 2 6 5 3 4 1 6 |  | No | 72.77 |
| 3 | 5 2 3 2 6 2 1 3 5 2 4 6 1 3 |  | No | 61.21 |
| 4 | 5 3 6 5 1 4 2 3 6 1 4 4 3 1 |  | No | 68.8 |
| 5 | 2 5 1 1 5 3 2 3 2 6 3 1 5 2 |  | No | 69.01 |
| 6 | 4 1 6 4 5 2 3 6 4 3 2 5 6 2 |  | No | 76.48 |
| 7 | 4 3 3 1 5 1 5 4 6 3 4 6 3 5 |  | No | 76.33 |
| 8 | 2 3 2 3 6 2 5 1 6 1 2 1 5 2 |  | No | 81.53 |
| 9 | 5 3 4 1 5 2 4 3 6 4 1 3 5 2 |  | No | 68.44 |
| 10 | 2 4 2 4 1 6 4 2 1 5 4 2 5 6 |  | No | 79.52 |
| 11 | 5 2 6 1 1 6 4 1 5 6 2 1 5 3 |  | No | 81.74 |
| 12 | 1 6 2 1 6 5 3 2 2 3 6 1 4 3 |  | No | 78.67 |
| 13 | 3 5 1 6 1 5 6 2 4 2 3 2 6 4 |  | No | 56.52 |
| 14 | 5 1 4 2 5 6 1 1 5 5 2 3 2 6 |  | No | 82.38 |
| 15 | 3 2 6 4 1 5 2 3 1 5 6 3 4 2 |  | No | 79.64 |
| 16 | 4 1 2 6 2 3 2 1 3 6 4 6 4 2 |  | No | 87.17 |
| 17 | 5 4 6 2 3 6 1 1 4 4 6 1 5 3 |  | No | 73.5 |
| 18 | 2 6 4 4 6 3 1 2 6 4 1 2 6 3 |  | No | 78.3 |
| 19 | 2 6 5 2 6 5 4 2 4 1 6 5 6 4 |  | No | 67.17 |
| 20 | 1 6 1 2 4 6 5 6 5 1 4 2 3 5 |  | No | 65.17 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1245 | 1245 | Yes | 11.51 |
| 2 | 1660 | 1660 | Yes | 6.56 |
| 3 | 1641 | 1641 | Yes | 9.52 |
| 4 | 843 | 843 | Yes | 6.95 |
| 5 | 1099 | 1099 | Yes | 8.76 |
| 6 | 2460 | 2460 | Yes | 6.08 |
| 7 | 1267 | 1267 | Yes | 10.59 |
| 8 | 1445 | 1445 | Yes | 18.18 |
| 9 | 2072 | 2072 | Yes | 6.97 |
| 10 | 1966 | 1966 | Yes | 9.74 |
| 11 | 1363 | 1363 | Yes | 6.66 |
| 12 | 1184 | 1184 | Yes | 8.15 |
| 13 | 1664 | 1664 | Yes | 8.39 |
| 14 | 2350 | 2350 | Yes | 16.2 |
| 15 | 1464 | 1464 | Yes | 2.94 |
| 16 | 2473 | 2473 | Yes | 11.2 |
| 17 | 1358 | 1358 | Yes | 8.25 |
| 18 | 1916 | 1916 | Yes | 12.35 |
| 19 | 1874 | 1874 | Yes | 13.02 |
| 20 | 2392 | 2392 | Yes | 4.32 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 71 | 67 | No | 32.04 |
| 2 | 49 | 67 | No | 26.66 |
| 3 | 60 |  | No | 79.34 |
| 4 | 37 | 67 | No | 24.87 |
| 5 | 51 | 67 | No | 22.43 |
| 6 | 71 | 67 | No | 30.8 |
| 7 | 45 | 67 | No | 94.32 |
| 8 | 49 | 67 | No | 41.72 |
| 9 | 40 |  | No | 92.58 |
| 10 | 35 | 67 | No | 40.26 |
| 11 | 66 | 67 | No | 33.9 |
| 12 | 53 | 67 | No | 41.88 |
| 13 | 53 |  | No | 78.39 |
| 14 | 57 |  | No | 86.23 |
| 15 | 69 | 67 | No | 61.98 |
| 16 | 61 | 67 | No | 64.24 |
| 17 | 39 |  | No | 55.45 |
| 18 | 61 |  | No | 73.36 |
| 19 | 72 | 67 | No | 29.64 |
| 20 | 52 |  | No | 67.84 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BWPRUOY | BWPRUOY | Yes | 22.45 |
| 2 | OSFXWGJ | OSFXWGJ | Yes | 10.27 |
| 3 | HTSVMWD | HTSVMWD | Yes | 20.34 |
| 4 | AYLDBPW | AYLDBPW | Yes | 12.28 |
| 5 | VECQLJB | VECQLJB | Yes | 7.98 |
| 6 | RPDWNHJ | RPDWNHJ | Yes | 12.69 |
| 7 | VWXHUAY | VWXHUAY | Yes | 12.91 |
| 8 | QMBPCGK | QMBPCGK | Yes | 6.49 |
| 9 | FWYAVZI | FWYAVZI | Yes | 12.08 |
| 10 | WQFEOIJ | WQFEOIJ | Yes | 6.83 |
| 11 | COSDAXM | COSDAXM | Yes | 14.21 |
| 12 | ATMGDNJ | ATMGDNJ | Yes | 9.0 |
| 13 | AJRLCGN | AJRLCGN | Yes | 20.6 |
| 14 | UJETHKQ | UJETHKQ | Yes | 7.19 |
| 15 | BQJGOVE | BQJGOVE | Yes | 13.72 |
| 16 | CQNFGKO | CQNFGKO | Yes | 8.31 |
| 17 | ZQBIROG | ZQBIROG | Yes | 10.04 |
| 18 | ELGSHYR | ELGSHYR | Yes | 12.18 |
| 19 | DNITOHL | DNITOHL | Yes | 29.15 |
| 20 | RMDVZEC | RMDVZEC | Yes | 17.39 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.56 |
| 2 | [1.2, 8.8] | 8.8 1.2 | Yes | 10.6 |
| 3 | [1.8, 8.2] | 1.8 8.2 | Yes | 14.51 |
| 4 | [1.2, 8.8] | 1.2 8.8 | Yes | 11.89 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 10.41 |
| 6 | [1.8, 8.2] | 1.8 8.2 | Yes | 14.32 |
| 7 | [4.3, 5.7] | 5.7 4.3 | Yes | 11.39 |
| 8 | [5.0, 5.0] | 5.0 5.0 | Yes | 13.83 |
| 9 | [1.0, 9.0] | 9.0 1.0 | Yes | 13.93 |
| 10 | [0.1, 9.9] | 9.9 0.1 | Yes | 14.6 |
| 11 | [3.6, 6.4] | 3.6 6.4 | Yes | 16.44 |
| 12 | [2.6, 7.4] | 7.4 2.6 | Yes | 9.82 |
| 13 | [1.5, 8.5] | 8.5 1.5 | Yes | 8.4 |
| 14 | [3.1, 6.9] | 6.9 3.1 | Yes | 15.74 |
| 15 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.62 |
| 16 | [0.6, 9.4] | 9.4 0.6 | Yes | 10.17 |
| 17 | [3.9, 6.1] | 6.1 3.9 | Yes | 15.81 |
| 18 | [3.7, 6.3] | 3.7 6.3 | Yes | 13.17 |
| 19 | [4.1, 5.9] | 5.9 4.1 | Yes | 14.81 |
| 20 | [5.0, 5.0] | 5.0 5.0 | Yes | 14.13 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZWTAEQDN1ZOI |  | No | 62.66 |
| 2 | 7B1GIE3699FQ | 7B1GIE3699FQ | Yes | 12.66 |
| 3 | 5208SXPJDQCC | 5208SXPJDQCC | Yes | 9.61 |
| 4 | HVNWQ4CBD28M | HVNWQ4CBD28M | Yes | 4.29 |
| 5 | PYBRDGYCFKFL | PYBRDGYCFKFL | Yes | 9.2 |
| 6 | 53J5OC3MVXAN | 53J5OC3MVXAN | Yes | 15.28 |
| 7 | A5SCXXY8XMRN | A5SCXXY8XMRN | Yes | 11.3 |
| 8 | JMFO7T5VJ5JW | JMF07T5VJ5JW | No | 14.53 |
| 9 | XFUMR9088XBN | XFUMR9088XBN | Yes | 5.38 |
| 10 | K1VCZYW1Z2J8 | K1VCZYW1Z2J8 | Yes | 16.4 |
| 11 | AVHPQMJVSBR4 | AVHPQMJVSBR4 | Yes | 6.05 |
| 12 | 3QXYTTQKT9EF | 3QXYTTQKT9EF | Yes | 8.51 |
| 13 | EK4UPMS8KFPA | EK4UPMS8KFPA | Yes | 6.6 |
| 14 | FU0YXU1VCKR7 |  | No | 64.61 |
| 15 | VEKD0PF2QIQA |  | No | 51.43 |
| 16 | 9Z360W6I46OB | 9Z360W6I46OB | Yes | 23.42 |
| 17 | JOJD9V0DS5OV | JOJD9V0DS50V | No | 22.75 |
| 18 | BFDRBNRIDGGB |  | No | 70.47 |
| 19 | 4D8VJXXYIWB9 | 4D8VJXXYIWB9 | Yes | 27.34 |
| 20 | R7QVF3B34L76 | R7QVF3B34L76 | Yes | 11.77 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 |  | No | 78.09 |
| 2 | 3 | 3 | Yes | 17.7 |
| 3 | 16 | 16 | Yes | 23.21 |
| 4 | 60 | 42 | No | 5.48 |
| 5 | 4 | 4 | Yes | 28.23 |
| 6 | 4 | 42 | No | 9.25 |
| 7 | 10 | Answer | No | 33.35 |
| 8 | 67 | 67 | Yes | 9.93 |
| 9 | 39 | 42 | No | 25.28 |
| 10 | 4096 |  | No | 62.15 |
| 11 | 9 | 42 | No | 4.11 |
| 12 | 28 | 42 | No | 8.14 |
| 13 | 5 | 42 | No | 10.44 |
| 14 | 5 | 42 | No | 7.43 |
| 15 | 9 | 42 | No | 11.19 |
| 16 | 7680 | 42 | No | 18.98 |
| 17 | 198 | 42 | No | 15.29 |
| 18 | 26 | 42 | No | 8.08 |
| 19 | 7 | 7 | Yes | 8.44 |
| 20 | 1440 | 42 | No | 17.76 |
