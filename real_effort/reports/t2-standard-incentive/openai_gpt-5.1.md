# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
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
| sudoku_game | 7940 | 36132 | 44072 | 0 | 20 | 48.47 | 969.7 |
| add_numbers | 6960 | 1352 | 8312 | 20 | 0 | 4.41 | 88.28 |
| counting_zeros | 7020 | 39043 | 46063 | 0 | 20 | 61.43 | 1228.84 |
| task_decoding | 10280 | 6042 | 16322 | 20 | 0 | 6.67 | 133.69 |
| task_summation | 7280 | 10687 | 17967 | 20 | 0 | 11.22 | 224.65 |
| task_transcription | 7040 | 4472 | 11512 | 16 | 4 | 6.63 | 132.74 |
| task_sequences | 2901 | 9371 | 12272 | 17 | 3 | 12.52 | 250.44 |
| **TOTAL** | **49421** | **107099** | **156520** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 4 5 6 1 4 2 6 1 4 3 6 2 |  | No | 40.73 |
| 2 | 2 1 5 4 6 4 6 5 4 4 2 1 5 2 |  | No | 62.3 |
| 3 | 1 5 2 5 5 3 3 1 5 3 2 5 1 3 |  | No | 55.62 |
| 4 | 4 5 5 6 6 2 1 3 2 3 5 2 1 3 |  | No | 59.68 |
| 5 | 2 1 3 2 1 6 2 2 6 3 5 3 5 6 |  | No | 70.36 |
| 6 | 2 6 4 1 4 5 3 2 5 6 2 5 2 6 |  | No | 54.56 |
| 7 | 6 2 3 4 3 6 4 5 4 1 2 6 1 5 | 6 3 2 4 1 6 4 2 3 6 1 2 4 6 2 5 6 1 5 6 | No | 17.38 |
| 8 | 5 3 4 2 6 2 3 6 2 3 1 3 2 1 | 2 3 4 6 5 3 6 2 3 6 1 4 3 1 6 2 1 3 2 1 | No | 14.36 |
| 9 | 3 1 2 5 6 2 3 4 1 4 6 5 5 2 |  | No | 36.11 |
| 10 | 3 2 6 4 1 2 4 6 4 4 5 6 2 1 |  | No | 52.8 |
| 11 | 1 2 6 2 5 1 4 5 5 3 4 1 2 6 |  | No | 66.12 |
| 12 | 4 6 6 1 3 4 4 6 4 6 5 2 3 1 |  | No | 53.27 |
| 13 | 1 3 6 3 1 3 3 5 2 4 6 5 2 3 |  | No | 65.86 |
| 14 | 2 3 5 2 4 6 1 2 3 1 5 3 6 6 |  | No | 68.5 |
| 15 | 6 1 2 2 5 6 3 5 6 5 1 3 3 4 | 6 2 1 3 5 2 6 5 6 3 1 4 3 6 | No | 26.6 |
| 16 | 6 5 2 1 6 1 6 2 3 4 5 4 1 3 |  | No | 35.88 |
| 17 | 1 4 4 4 1 2 6 3 5 6 1 4 6 5 |  | No | 68.06 |
| 18 | 6 4 3 4 3 1 6 5 5 6 4 4 3 2 | 4 6 3 1 5 3 6 4 1 2 5 6 3 2 4 1 2 4 | No | 5.82 |
| 19 | 4 2 1 3 6 1 3 4 2 1 4 5 1 3 |  | No | 39.3 |
| 20 | 5 2 2 5 4 2 6 6 1 3 6 5 6 4 |  | No | 76.17 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2258 | 2258 | Yes | 4.43 |
| 2 | 2070 | 2070 | Yes | 4.33 |
| 3 | 1661 | 1661 | Yes | 2.69 |
| 4 | 2742 | 2742 | Yes | 3.38 |
| 5 | 2298 | 2298 | Yes | 3.71 |
| 6 | 2267 | 2267 | Yes | 4.28 |
| 7 | 1185 | 1185 | Yes | 3.56 |
| 8 | 1342 | 1342 | Yes | 3.18 |
| 9 | 860 | 860 | Yes | 5.8 |
| 10 | 1998 | 1998 | Yes | 5.24 |
| 11 | 1910 | 1910 | Yes | 3.51 |
| 12 | 1445 | 1445 | Yes | 3.94 |
| 13 | 705 | 705 | Yes | 4.12 |
| 14 | 1305 | 1305 | Yes | 3.34 |
| 15 | 954 | 954 | Yes | 5.85 |
| 16 | 2292 | 2292 | Yes | 4.93 |
| 17 | 2274 | 2274 | Yes | 5.39 |
| 18 | 1417 | 1417 | Yes | 4.78 |
| 19 | 1440 | 1440 | Yes | 6.02 |
| 20 | 2001 | 2001 | Yes | 5.71 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 |  | No | 51.94 |
| 2 | 63 |  | No | 47.36 |
| 3 | 44 |  | No | 73.29 |
| 4 | 42 | 64 | No | 7.47 |
| 5 | 36 |  | No | 97.22 |
| 6 | 42 |  | No | 80.11 |
| 7 | 65 |  | No | 62.59 |
| 8 | 45 |  | No | 78.88 |
| 9 | 67 |  | No | 66.21 |
| 10 | 51 |  | No | 63.48 |
| 11 | 58 |  | No | 64.94 |
| 12 | 46 |  | No | 72.0 |
| 13 | 64 |  | No | 47.68 |
| 14 | 47 |  | No | 63.51 |
| 15 | 40 |  | No | 61.8 |
| 16 | 39 |  | No | 66.29 |
| 17 | 56 |  | No | 54.0 |
| 18 | 72 |  | No | 72.39 |
| 19 | 46 |  | No | 46.3 |
| 20 | 63 |  | No | 51.05 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DZAHFNV | DZAHFNV | Yes | 7.8 |
| 2 | RPZXGAK | RPZXGAK | Yes | 3.18 |
| 3 | ANRYQVH | ANRYQVH | Yes | 11.37 |
| 4 | SEHOXIM | SEHOXIM | Yes | 10.72 |
| 5 | XPWOUFD | XPWOUFD | Yes | 4.41 |
| 6 | PIZDTJN | PIZDTJN | Yes | 4.16 |
| 7 | UNRSZJX | UNRSZJX | Yes | 7.87 |
| 8 | OZAXSEQ | OZAXSEQ | Yes | 4.42 |
| 9 | ZWVSIQU | ZWVSIQU | Yes | 3.87 |
| 10 | HWGXIZT | HWGXIZT | Yes | 5.12 |
| 11 | DZKPEFX | DZKPEFX | Yes | 5.61 |
| 12 | OKTUWGV | OKTUWGV | Yes | 7.27 |
| 13 | RLDQYJE | RLDQYJE | Yes | 5.76 |
| 14 | RFHJGNO | RFHJGNO | Yes | 10.49 |
| 15 | FETXYWD | FETXYWD | Yes | 6.47 |
| 16 | HXVZASU | HXVZASU | Yes | 9.68 |
| 17 | EXVZKWP | EXVZKWP | Yes | 5.23 |
| 18 | AGIKTBM | AGIKTBM | Yes | 6.62 |
| 19 | GTHISUV | GTHISUV | Yes | 7.58 |
| 20 | QROCGPK | QROCGPK | Yes | 5.8 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.99 |
| 2 | [1.5, 8.5] | 1.5 8.5 | Yes | 9.58 |
| 3 | [0.7, 9.3] | 9.3 0.7 | Yes | 13.5 |
| 4 | [0.4, 9.6] | 0.4 9.6 | Yes | 12.09 |
| 5 | [4.2, 5.8] | 5.8 4.2 | Yes | 11.01 |
| 6 | [4.7, 5.3] | 5.3 4.7 | Yes | 7.86 |
| 7 | [4.3, 5.7] | 4.3 5.7 | Yes | 7.27 |
| 8 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.22 |
| 9 | [0.4, 9.6] | 0.4 9.6 | Yes | 10.11 |
| 10 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.67 |
| 11 | [4.1, 5.9] | 4.1 5.9 | Yes | 17.47 |
| 12 | [4.7, 5.3] | 5.3 4.7 | Yes | 7.61 |
| 13 | [1.5, 8.5] | 8.5 1.5 | Yes | 7.26 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 10.04 |
| 15 | [2.0, 8.0] | 8.0 2.0 | Yes | 10.31 |
| 16 | [3.1, 6.9] | 3.1 6.9 | Yes | 34.62 |
| 17 | [4.5, 5.5] | 4.5 5.5 | Yes | 9.61 |
| 18 | [2.9, 7.1] | 7.1 2.9 | Yes | 12.1 |
| 19 | [2.9, 7.1] | 2.9 7.1 | Yes | 8.62 |
| 20 | [3.6, 6.4] | 6.4 3.6 | Yes | 10.51 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 0QPR7ZUX5XF5 | 0QPR7ZUX5XF5 | Yes | 4.91 |
| 2 | MSHODUWYGWP6 | MSHODUWYGP6 | No | 34.35 |
| 3 | 8JJ6CNG9CTNU | 8JJ6CNG9CTNU | Yes | 5.49 |
| 4 | EY248O26SEKF | EY248026SEKF | No | 5.45 |
| 5 | 4988DUYD6LRH | 4988DUYD6LRH | Yes | 3.64 |
| 6 | J4Y6AUXXVAWO | J4Y6AUXXVAWO | Yes | 6.01 |
| 7 | Q3O41GO9ZJNF | Q3041GO9ZJNF | No | 17.85 |
| 8 | 32RSEOXJ2CF4 | 32RSEOXJ2CF4 | Yes | 3.45 |
| 9 | 8SL1M45PLPJH | 8SL1M45PLPJH | Yes | 2.17 |
| 10 | V57XOX5LAM5R | V57XOX5LAM5R | Yes | 5.92 |
| 11 | WCK5KJ9KA5B3 | WCK5KJ9KA5B3 | Yes | 3.62 |
| 12 | CPSBVZKLFFMX | CPSBVZKLFFMX | Yes | 4.44 |
| 13 | ZGB14XC4TQ1V | ZGB14XC4TQ1V | Yes | 4.78 |
| 14 | 1R68JBQH7ESB | 1R68JBQH7ESB | Yes | 7.45 |
| 15 | CKC2ZELADK1Z | CKC2ZELADK1Z | Yes | 4.35 |
| 16 | J1R58XYU82GO | J1R58XYU82GO | Yes | 4.6 |
| 17 | GR0P808RYCPL | GR0P808RYCPL | Yes | 4.06 |
| 18 | MVFX2WA1UCQP | MVFX2WA1UCQP | Yes | 3.35 |
| 19 | 1WIKN6RLJOH1 | 1WIKN6RLJOH1 | Yes | 1.9 |
| 20 | SFM60OBLJXTH | SFM600BLJXTH | No | 4.83 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4096 |  | No | 52.91 |
| 2 | 28 | 28 | Yes | 24.98 |
| 3 | 36 | 36 | Yes | 3.08 |
| 4 | 9 | 9 | Yes | 4.04 |
| 5 | 5 |  | No | 52.6 |
| 6 | 10 | 10 | Yes | 6.13 |
| 7 | 243 | 243 | Yes | 3.19 |
| 8 | 198 | 198 | Yes | 4.72 |
| 9 | 26 |  | No | 44.23 |
| 10 | 31 | 31 | Yes | 3.99 |
| 11 | 65 | 65 | Yes | 3.6 |
| 12 | 60 | 60 | Yes | 8.76 |
| 13 | 1 | 1 | Yes | 4.89 |
| 14 | 67 | 67 | Yes | 2.86 |
| 15 | 23 | 23 | Yes | 4.74 |
| 16 | 64 | 64 | Yes | 4.58 |
| 17 | 1440 | 1440 | Yes | 5.46 |
| 18 | 5 | 5 | Yes | 5.79 |
| 19 | 9 | 9 | Yes | 5.24 |
| 20 | 6 | 6 | Yes | 4.64 |
