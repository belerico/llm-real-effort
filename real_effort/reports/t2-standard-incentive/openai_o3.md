# Benchmark Report — o3

- **Model**: `openai/o3`
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
| sudoku_game | 7828 | 38885 | 46713 | 0 | 20 | 76.53 | 1530.79 |
| add_numbers | 7260 | 3157 | 10417 | 20 | 0 | 4.91 | 98.37 |
| counting_zeros | 7320 | 40960 | 48280 | 0 | 20 | 46.70 | 934.4 |
| task_decoding | 10780 | 11105 | 21885 | 19 | 1 | 12.96 | 259.44 |
| task_summation | 7580 | 14217 | 21797 | 20 | 0 | 14.25 | 285.25 |
| task_transcription | 7340 | 9579 | 16919 | 18 | 2 | 11.77 | 235.56 |
| task_sequences | 2901 | 9329 | 12230 | 18 | 2 | 13.89 | 277.76 |
| **TOTAL** | **51009** | **127232** | **178241** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 2 6 1 4 6 6 4 2 1 6 2 3 |  | No | 68.29 |
| 2 | 2 1 6 3 5 4 3 5 6 3 1 6 4 5 |  | No | 85.72 |
| 3 | 3 4 1 3 1 2 5 3 4 6 1 6 2 1 |  | No | 56.26 |
| 4 | 2 4 3 1 1 3 3 4 1 4 1 5 4 1 |  | No | 73.09 |
| 5 | 4 2 1 5 4 5 1 1 6 4 6 6 4 1 |  | No | 82.21 |
| 6 | 4 3 5 6 4 4 5 1 1 2 3 6 6 5 |  | No | 79.66 |
| 7 | 3 4 4 5 2 6 3 2 6 1 3 2 1 5 |  | No | 56.22 |
| 8 | 5 3 6 3 4 4 3 2 6 1 1 2 4 6 |  | No | 61.86 |
| 9 | 5 2 4 3 5 6 2 3 1 6 5 4 2 1 |  | No | 60.7 |
| 10 | 1 3 3 4 1 6 2 5 1 4 3 5 1 3 |  | No | 87.88 |
| 11 | 2 3 5 1 5 4 3 2 1 6 4 6 2 5 |  | No | 71.22 |
| 12 | 6 4 6 5 1 4 2 6 1 5 2 1 3 2 |  | No | 119.01 |
| 13 | 2 5 5 2 3 3 1 4 2 6 5 1 4 1 |  | No | 68.07 |
| 14 | 4 5 5 6 2 4 6 1 5 3 2 2 1 6 |  | No | 101.78 |
| 15 | 4 3 1 5 4 5 1 4 3 4 5 1 2 3 |  | No | 82.59 |
| 16 | 5 2 6 1 3 4 3 2 6 4 6 3 1 4 |  | No | 58.14 |
| 17 | 1 2 4 6 6 5 5 3 6 5 4 6 4 3 | TIMEOUT | No | 120.02 |
| 18 | 1 6 5 5 5 1 3 6 3 4 1 4 6 3 |  | No | 45.7 |
| 19 | 5 3 6 1 2 6 2 5 3 5 5 3 4 1 |  | No | 114.3 |
| 20 | 3 6 3 1 2 5 5 6 3 6 4 1 4 3 |  | No | 37.87 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2141 | 2141 | Yes | 3.46 |
| 2 | 1433 | 1433 | Yes | 2.93 |
| 3 | 2288 | 2288 | Yes | 3.92 |
| 4 | 1725 | 1725 | Yes | 2.55 |
| 5 | 1293 | 1293 | Yes | 4.92 |
| 6 | 1013 | 1013 | Yes | 3.67 |
| 7 | 2335 | 2335 | Yes | 7.34 |
| 8 | 1917 | 1917 | Yes | 7.2 |
| 9 | 1346 | 1346 | Yes | 5.29 |
| 10 | 1106 | 1106 | Yes | 6.66 |
| 11 | 1356 | 1356 | Yes | 5.29 |
| 12 | 1025 | 1025 | Yes | 3.38 |
| 13 | 2067 | 2067 | Yes | 3.49 |
| 14 | 1937 | 1937 | Yes | 11.12 |
| 15 | 2298 | 2298 | Yes | 5.97 |
| 16 | 1946 | 1946 | Yes | 5.84 |
| 17 | 2672 | 2672 | Yes | 5.68 |
| 18 | 1399 | 1399 | Yes | 2.97 |
| 19 | 1767 | 1767 | Yes | 3.09 |
| 20 | 1520 | 1520 | Yes | 3.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 46 |  | No | 58.46 |
| 2 | 41 |  | No | 31.08 |
| 3 | 68 |  | No | 52.02 |
| 4 | 53 |  | No | 66.64 |
| 5 | 37 |  | No | 62.04 |
| 6 | 60 |  | No | 53.03 |
| 7 | 65 |  | No | 42.45 |
| 8 | 47 |  | No | 37.41 |
| 9 | 47 |  | No | 58.16 |
| 10 | 35 |  | No | 39.49 |
| 11 | 49 |  | No | 59.27 |
| 12 | 43 |  | No | 29.95 |
| 13 | 63 |  | No | 45.98 |
| 14 | 36 |  | No | 67.52 |
| 15 | 37 |  | No | 40.87 |
| 16 | 35 |  | No | 27.13 |
| 17 | 50 |  | No | 41.97 |
| 18 | 59 |  | No | 35.52 |
| 19 | 74 |  | No | 38.23 |
| 20 | 52 |  | No | 46.87 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YCHEDJA | YCHEDJA | Yes | 33.62 |
| 2 | UKZDWBQ | UKZDWBQ | Yes | 5.8 |
| 3 | KUSPLXD | KUSPLXD | Yes | 7.93 |
| 4 | EJSAGRD | EJSAGRD | Yes | 12.14 |
| 5 | ANZOWYD | ANZOWYD | Yes | 7.5 |
| 6 | WHJBEXD | WHJBEXD | Yes | 15.7 |
| 7 | TLMNOWK | TLMNOWK | Yes | 4.37 |
| 8 | IPGXZST | IPGXZST | Yes | 12.3 |
| 9 | HVKJNQF | HVKJNQF | Yes | 6.36 |
| 10 | DSXHNFG | DSXHNFG | Yes | 7.97 |
| 11 | KVFNSML | KVFNSML | Yes | 4.18 |
| 12 | YFGPEUV | YFGPEUV | Yes | 6.28 |
| 13 | BODGEWT | BODGEWT | Yes | 16.41 |
| 14 | JMQCYRN | JMQCYRN | Yes | 8.13 |
| 15 | PFAKULZ | PFAKULZ | Yes | 6.69 |
| 16 | XILYDMC | XILYDMC | Yes | 7.11 |
| 17 | RJOQCNF |  | No | 61.92 |
| 18 | VAKGESM | VAKGESM | Yes | 8.32 |
| 19 | MPOKWES | MPOKWES | Yes | 9.78 |
| 20 | JRIHZMS | JRIHZMS | Yes | 16.69 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.2, 6.8] | 3.2 6.8 | Yes | 22.02 |
| 2 | [0.4, 9.6] | 0.4 9.6 | Yes | 15.18 |
| 3 | [3.5, 6.5] | 6.5 3.5 | Yes | 20.9 |
| 4 | [2.2, 7.8] | 2.2 7.8 | Yes | 20.94 |
| 5 | [2.5, 7.5] | 2.5 7.5 | Yes | 16.72 |
| 6 | [2.0, 8.0] | 2.0 8.0 | Yes | 14.16 |
| 7 | [1.5, 8.5] | 8.5 1.5 | Yes | 10.71 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 13.01 |
| 9 | [0.3, 9.7] | 0.3 9.7 | Yes | 20.05 |
| 10 | [1.9, 8.1] | 1.9 8.1 | Yes | 12.35 |
| 11 | [0.5, 9.5] | 0.5 9.5 | Yes | 12.97 |
| 12 | [1.2, 8.8] | 1.2 8.8 | Yes | 11.59 |
| 13 | [4.9, 5.1] | 5.1 4.9 | Yes | 10.19 |
| 14 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.44 |
| 15 | [2.1, 7.9] | 2.1 7.9 | Yes | 10.06 |
| 16 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.48 |
| 17 | [0.4, 9.6] | 0.4 9.6 | Yes | 14.65 |
| 18 | [2.0, 8.0] | 2.0 8.0 | Yes | 12.94 |
| 19 | [2.9, 7.1] | 2.9 7.1 | Yes | 12.67 |
| 20 | [3.0, 7.0] | 3.0 7.0 | Yes | 12.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EK455RIAWSGN | EK455RIAWSGN | Yes | 7.91 |
| 2 | H2L84B2A8OBH | H2L84B2A8OBH | Yes | 4.87 |
| 3 | 06BNWYVHXXIT | 0GBNWYVHXIT | No | 5.5 |
| 4 | C8ONE8NCWL38 | C8ONE8NCWL38 | Yes | 24.83 |
| 5 | HS6YWXQUAI0Z | HS6YWXQUAI0Z | Yes | 14.76 |
| 6 | 15S929NERWYE | 15S929NERWYE | Yes | 4.09 |
| 7 | 4S55DB64Z93Y | 4S55DB64Z93Y | Yes | 11.99 |
| 8 | PH22PCRE1PDL | PH22PCRE1PDL | Yes | 9.72 |
| 9 | AOPQG96PIZY6 | AOPQG96PIZY6 | Yes | 40.44 |
| 10 | WJYV59UTKI5V | WJYV59UTKI5V | Yes | 5.78 |
| 11 | TRY8H70PP0QZ | TRY8H70PP0QZ | Yes | 21.58 |
| 12 | 3X9976EQI1NO | 3X9976EQI1NO | Yes | 4.83 |
| 13 | 33IXEI9PM41G | 33IXEI9PM41G | Yes | 6.39 |
| 14 | H1UMM7QZGK59 | H1UMM7QZGK59 | Yes | 8.26 |
| 15 | TYU30Z3LB0HZ | TYU30Z3LB0HZ | Yes | 16.43 |
| 16 | HEFORFSDEXN0 | HEFORFSDEXN0 | Yes | 6.12 |
| 17 | S88NZZ59LZ3L | S88NZZ59LZ3L | Yes | 6.7 |
| 18 | GALNUG90WSO8 | GALNUG90WS08 | No | 18.91 |
| 19 | JWCVSGT6OH07 | JWCVSGT6OH07 | Yes | 12.67 |
| 20 | C0VCII4KFAJ9 | C0VCII4KFAJ9 | Yes | 3.64 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 44 | Yes | 13.06 |
| 2 | 4096 |  | No | 65.29 |
| 3 | 65 | 65 | Yes | 6.54 |
| 4 | 19 | 19 | Yes | 4.06 |
| 5 | 7680 | 7680 | Yes | 4.83 |
| 6 | 60 | 60 | Yes | 5.33 |
| 7 | 20 |  | No | 69.84 |
| 8 | 10 | 10 | Yes | 12.5 |
| 9 | 9 | 9 | Yes | 6.55 |
| 10 | 793 | 793 | Yes | 4.76 |
| 11 | 73 | 73 | Yes | 16.86 |
| 12 | 16 | 16 | Yes | 9.27 |
| 13 | 4 | 4 | Yes | 9.8 |
| 14 | 3 | 3 | Yes | 13.35 |
| 15 | 1 | 1 | Yes | 7.48 |
| 16 | 63 | 63 | Yes | 5.39 |
| 17 | 1440 | 1440 | Yes | 5.62 |
| 18 | 9 | 9 | Yes | 6.94 |
| 19 | 31 | 31 | Yes | 5.14 |
| 20 | 198 | 198 | Yes | 5.15 |
