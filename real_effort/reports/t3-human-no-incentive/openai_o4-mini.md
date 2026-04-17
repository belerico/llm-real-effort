# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
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
| sudoku_game | 8880 | 40960 | 49840 | 0 | 20 | 47.28 | 945.7 |
| add_numbers | 4400 | 5206 | 9606 | 20 | 0 | 3.83 | 76.64 |
| counting_zeros | 7820 | 40960 | 48780 | 0 | 20 | 34.80 | 696.43 |
| task_decoding | 15860 | 19185 | 35045 | 19 | 1 | 11.53 | 230.74 |
| task_summation | 9080 | 18188 | 27268 | 20 | 0 | 10.14 | 202.98 |
| task_transcription | 4085 | 7156 | 11241 | 19 | 1 | 4.08 | 81.72 |
| task_sequences | 3061 | 14532 | 17593 | 16 | 4 | 8.27 | 165.35 |
| **TOTAL** | **53186** | **146187** | **199373** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 4 2 5 3 2 3 4 5 4 1 6 6 |  | No | 45.75 |
| 2 | 3 6 6 6 4 6 5 3 2 4 1 1 4 6 |  | No | 41.62 |
| 3 | 3 6 5 2 6 5 1 1 2 6 3 1 3 1 |  | No | 47.9 |
| 4 | 4 3 2 3 3 4 5 5 1 6 2 4 5 2 |  | No | 30.01 |
| 5 | 4 2 1 4 6 2 2 5 4 3 1 6 4 2 |  | No | 46.67 |
| 6 | 3 5 3 1 2 3 4 5 1 6 5 6 3 1 |  | No | 33.39 |
| 7 | 3 6 1 1 5 4 2 1 2 4 3 1 6 2 |  | No | 28.94 |
| 8 | 4 3 6 1 1 3 2 6 1 6 5 2 1 2 |  | No | 50.46 |
| 9 | 5 2 4 4 6 1 4 3 1 2 1 6 2 3 |  | No | 55.43 |
| 10 | 4 2 6 4 5 3 6 1 2 2 4 1 3 2 |  | No | 32.2 |
| 11 | 2 4 3 4 5 3 1 5 5 4 2 6 1 1 |  | No | 46.99 |
| 12 | 4 3 2 5 2 6 2 3 5 4 3 2 4 5 |  | No | 47.71 |
| 13 | 5 1 2 1 1 5 4 6 5 1 6 4 3 6 |  | No | 44.74 |
| 14 | 4 1 5 3 2 3 4 1 6 2 1 3 3 5 |  | No | 57.3 |
| 15 | 1 5 4 6 5 2 1 5 2 1 3 4 5 1 |  | No | 41.25 |
| 16 | 5 2 4 1 2 4 5 5 4 2 3 5 5 4 |  | No | 75.51 |
| 17 | 4 5 1 3 5 6 4 2 3 2 5 2 2 3 |  | No | 65.89 |
| 18 | 1 3 5 3 5 6 4 3 5 6 5 3 2 6 |  | No | 62.88 |
| 19 | 3 4 5 6 3 5 3 2 4 5 4 2 5 1 |  | No | 53.17 |
| 20 | 2 3 1 5 1 2 3 6 4 6 4 5 4 3 |  | No | 37.71 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1281 | 1281 | Yes | 2.62 |
| 2 | 2514 | 2514 | Yes | 4.18 |
| 3 | 958 | 958 | Yes | 3.22 |
| 4 | 1408 | 1408 | Yes | 3.35 |
| 5 | 1847 | 1847 | Yes | 3.15 |
| 6 | 2060 | 2060 | Yes | 2.77 |
| 7 | 1886 | 1886 | Yes | 3.29 |
| 8 | 2134 | 2134 | Yes | 7.59 |
| 9 | 2144 | 2144 | Yes | 8.06 |
| 10 | 1974 | 1974 | Yes | 4.81 |
| 11 | 2045 | 2045 | Yes | 3.33 |
| 12 | 1621 | 1621 | Yes | 4.07 |
| 13 | 2107 | 2107 | Yes | 3.57 |
| 14 | 1686 | 1686 | Yes | 2.47 |
| 15 | 1334 | 1334 | Yes | 5.23 |
| 16 | 1881 | 1881 | Yes | 2.34 |
| 17 | 1882 | 1882 | Yes | 3.78 |
| 18 | 934 | 934 | Yes | 2.81 |
| 19 | 1459 | 1459 | Yes | 2.75 |
| 20 | 1270 | 1270 | Yes | 3.15 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 45 |  | No | 26.57 |
| 2 | 43 |  | No | 30.36 |
| 3 | 43 |  | No | 27.27 |
| 4 | 58 |  | No | 38.91 |
| 5 | 49 |  | No | 19.76 |
| 6 | 74 |  | No | 31.44 |
| 7 | 35 |  | No | 19.39 |
| 8 | 73 |  | No | 43.78 |
| 9 | 63 |  | No | 20.47 |
| 10 | 35 |  | No | 67.14 |
| 11 | 54 |  | No | 34.52 |
| 12 | 71 |  | No | 42.31 |
| 13 | 66 |  | No | 43.08 |
| 14 | 49 |  | No | 32.77 |
| 15 | 54 |  | No | 47.35 |
| 16 | 62 |  | No | 18.36 |
| 17 | 70 |  | No | 28.43 |
| 18 | 61 |  | No | 51.68 |
| 19 | 62 |  | No | 29.07 |
| 20 | 42 |  | No | 43.44 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LMERHNQ | LMERHNQ | Yes | 13.11 |
| 2 | RKTDBXW | RKTDBXW | Yes | 3.92 |
| 3 | BVXQWRY | BVXQWRY | Yes | 4.66 |
| 4 | KSATNEW | KSATNEW | Yes | 17.84 |
| 5 | VBOIFPJ | VBOIFPJ | Yes | 14.38 |
| 6 | WQGAXCZ | WQGAXCZ | Yes | 7.79 |
| 7 | ADJEWUF |  | No | 41.32 |
| 8 | TMVJBCK | TMVJBCK | Yes | 7.89 |
| 9 | WDUEKTM | WDUEKTM | Yes | 8.76 |
| 10 | MIFQAJY | MIFQAJY | Yes | 7.87 |
| 11 | WYGNBHP | WYGNBHP | Yes | 10.88 |
| 12 | BYIRVWX | BYIRVWX | Yes | 9.52 |
| 13 | XCEDOWN | XCEDOWN | Yes | 10.2 |
| 14 | JBWGUNO | JBWGUNO | Yes | 8.22 |
| 15 | THIJRZG | THIJRZG | Yes | 14.24 |
| 16 | VHMCJPI | VHMCJPI | Yes | 4.87 |
| 17 | DVPJFSE | DVPJFSE | Yes | 9.02 |
| 18 | POAZRBF | POAZRBF | Yes | 10.74 |
| 19 | QIFMOLC | QIFMOLC | Yes | 11.74 |
| 20 | DVBMJHZ | DVBMJHZ | Yes | 13.55 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.8, 9.2] | 0.8 9.2 | Yes | 8.95 |
| 2 | [1.8, 8.2] | 8.2 1.8 | Yes | 9.9 |
| 3 | [0.4, 9.6] | 0.4 9.6 | Yes | 10.56 |
| 4 | [3.8, 6.2] | 3.8 6.2 | Yes | 9.52 |
| 5 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.23 |
| 6 | [4.2, 5.8] | 5.8 4.2 | Yes | 19.23 |
| 7 | [3.3, 6.7] | 3.3 6.7 | Yes | 14.82 |
| 8 | [4.2, 5.8] | 5.8 4.2 | Yes | 14.13 |
| 9 | [4.8, 5.2] | 5.2 4.8 | Yes | 8.83 |
| 10 | [0.5, 9.5] | 0.5 9.5 | Yes | 8.51 |
| 11 | [1.7, 8.3] | 1.7 8.3 | Yes | 10.97 |
| 12 | [2.6, 7.4] | 2.6 7.4 | Yes | 8.81 |
| 13 | [2.8, 7.2] | 2.8 7.2 | Yes | 8.58 |
| 14 | [4.0, 6.0] | 6.0 4.0 | Yes | 12.39 |
| 15 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.09 |
| 16 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.21 |
| 17 | [0.4, 9.6] | 0.4 9.6 | Yes | 6.39 |
| 18 | [3.9, 6.1] | 6.1 3.9 | Yes | 8.56 |
| 19 | [1.0, 9.0] | 9.0 1.0 | Yes | 9.38 |
| 20 | [3.4, 6.6] | 3.4 6.6 | Yes | 10.72 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | B64KLOKTJ3XV | B64KLOKTJ3XV | Yes | 2.06 |
| 2 | E0QRRQHY90KQ | E0QRRQHY90KQ | Yes | 5.02 |
| 3 | 5ELOFHBYEZ1Y | 5ELOFHBYEZ1Y | Yes | 4.32 |
| 4 | 4UROID85FYIY | 4UROID85FYIY | Yes | 3.65 |
| 5 | GFH8M1007D5A | GFH8M1007D5A | Yes | 3.11 |
| 6 | D82WRNQ6Y2PV | D82WRNQ6Y2PV | Yes | 2.65 |
| 7 | 9N9UG7KK29OF | 9N9UG7KK29OF | Yes | 4.6 |
| 8 | 9V2N3FX8KXTJ | 9V2N3FX8KXTJ | Yes | 2.42 |
| 9 | HTYM9IM197SZ | HTYM9IM197SZ | Yes | 4.29 |
| 10 | QFHE0GT8VH5D | QFHE0GT8VH5D | Yes | 5.34 |
| 11 | B7ZT81C6AGY3 | B7ZT81C6AGY3 | Yes | 3.11 |
| 12 | BXR6JK3KJ59T | BXR6JK3KJ59T | Yes | 2.49 |
| 13 | 49W641ESY09I | 49W641ESY09I | Yes | 3.0 |
| 14 | ADGUEXE8N9D7 | ADGUEXE8N9D7 | Yes | 2.7 |
| 15 | PPKVT5CC63DA | PPKVT5CC63DA | Yes | 2.38 |
| 16 | 22I0EHWETRI3 | 2210EHWETRI3 | No | 12.97 |
| 17 | KN6ITMVV0B5V | KN6ITMVV0B5V | Yes | 4.52 |
| 18 | A7L8TRJE2YPN | A7L8TRJE2YPN | Yes | 3.71 |
| 19 | 901XMMLATTKX | 901XMMLATTKX | Yes | 3.82 |
| 20 | J0FJSGDBCPZ8 | J0FJSGDBCPZ8 | Yes | 5.44 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 19 | 19 | Yes | 4.57 |
| 2 | 39 | 39 | Yes | 15.35 |
| 3 | 4 | 4 | Yes | 2.54 |
| 4 | 23 | 23 | Yes | 9.63 |
| 5 | 9 | 9 | Yes | 9.1 |
| 6 | 6 | 6 | Yes | 3.9 |
| 7 | 5 | 42 | No | 9.08 |
| 8 | 5 | 5 | Yes | 5.72 |
| 9 | 26 |  | No | 29.62 |
| 10 | 64 | 42 | No | 9.03 |
| 11 | 20 | 20 | Yes | 11.48 |
| 12 | 31 | 31 | Yes | 3.04 |
| 13 | 9 | 9 | Yes | 12.83 |
| 14 | 4096 | 42 | No | 5.37 |
| 15 | 60 | 60 | Yes | 7.75 |
| 16 | 36 | 36 | Yes | 4.54 |
| 17 | 16 | 16 | Yes | 4.41 |
| 18 | 60 | 60 | Yes | 8.88 |
| 19 | 7 | 7 | Yes | 4.34 |
| 20 | 3 | 3 | Yes | 4.19 |
