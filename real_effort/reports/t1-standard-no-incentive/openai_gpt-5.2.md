# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 7020 | 25722 | 32742 | 16 | 4 | 30.66 | 613.37 |
| add_numbers | 3600 | 861 | 4461 | 20 | 0 | 4.05 | 81.07 |
| counting_zeros | 5719 | 34576 | 40295 | 6 | 14 | 58.41 | 1168.51 |
| task_decoding | 11760 | 3572 | 15332 | 20 | 0 | 5.40 | 108.15 |
| task_summation | 6960 | 5252 | 12212 | 20 | 0 | 6.27 | 125.62 |
| task_transcription | 3422 | 2669 | 6091 | 15 | 5 | 4.63 | 92.72 |
| task_sequences | 2720 | 5297 | 8017 | 17 | 3 | 11.53 | 230.53 |
| **TOTAL** | **41201** | **77949** | **119150** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 6 1 1 5 1 3 6 2 5 6 3 2 | 4 2 6 1 1 5 1 3 6 2 5 6 3 2 | Yes | 19.88 |
| 2 | 6 5 6 1 3 5 4 4 5 3 6 3 2 4 | 6 5 6 1 3 5 4 4 5 3 6 3 2 4 | Yes | 28.05 |
| 3 | 2 4 6 4 5 1 5 6 4 4 3 2 1 4 | 2 4 6 4 5 1 5 6 4 4 3 2 1 4 | Yes | 24.79 |
| 4 | 4 6 1 4 2 4 1 3 2 6 4 4 1 2 |  | No | 58.81 |
| 5 | 1 5 2 4 6 2 6 4 1 3 2 6 4 6 |  | No | 66.07 |
| 6 | 1 2 2 3 6 4 5 4 2 6 4 3 2 3 | 1 2 2 3 6 4 5 4 2 6 4 3 2 3 | Yes | 19.17 |
| 7 | 6 5 1 3 6 2 3 6 5 4 2 1 4 5 |  | No | 67.92 |
| 8 | 5 1 2 6 5 4 3 6 6 1 4 4 6 1 | 5 1 2 6 5 4 3 6 6 1 4 4 6 1 | Yes | 18.51 |
| 9 | 2 3 4 6 5 1 1 5 6 4 2 2 1 5 | 2 3 4 6 5 1 1 5 6 4 2 2 1 5 | Yes | 17.82 |
| 10 | 3 4 5 2 5 4 3 2 5 6 1 4 2 1 | 3 4 5 2 5 4 3 2 5 6 1 4 2 1 | Yes | 16.53 |
| 11 | 2 5 5 6 2 6 4 2 3 5 3 4 1 5 | 2 5 5 6 2 6 4 2 3 5 3 4 1 5 | Yes | 22.36 |
| 12 | 2 3 4 2 6 2 4 5 3 1 5 2 4 5 | 2 3 4 2 6 2 4 5 3 1 5 2 4 5 | Yes | 23.08 |
| 13 | 2 5 6 4 1 1 2 2 5 6 3 5 2 6 |  | No | 78.05 |
| 14 | 1 2 4 1 6 3 1 3 5 6 1 4 3 6 | 1 2 4 1 6 3 1 3 5 6 1 4 3 6 | Yes | 19.7 |
| 15 | 2 5 4 6 1 2 5 4 1 4 5 6 3 2 | 2 5 4 6 1 2 5 4 1 4 5 6 3 2 | Yes | 24.0 |
| 16 | 3 2 5 4 3 5 3 2 6 5 4 1 3 2 | 3 2 5 4 3 5 3 2 6 5 4 1 3 2 | Yes | 20.45 |
| 17 | 4 5 6 2 4 1 3 2 4 1 3 4 3 5 | 4 5 6 2 4 1 3 2 4 1 3 4 3 5 | Yes | 29.54 |
| 18 | 5 4 2 5 1 4 2 4 1 6 4 5 1 4 | 5 4 2 5 1 4 2 4 1 6 4 5 1 4 | Yes | 22.91 |
| 19 | 6 1 2 1 4 1 3 2 6 1 4 2 4 5 | 6 1 2 1 4 1 3 2 6 1 4 2 4 5 | Yes | 16.19 |
| 20 | 2 1 3 5 3 5 5 2 1 4 5 6 3 1 | 2 1 3 5 3 5 5 2 1 4 5 6 3 1 | Yes | 19.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1936 | 1936 | Yes | 3.19 |
| 2 | 2179 | 2179 | Yes | 4.25 |
| 3 | 1975 | 1975 | Yes | 5.35 |
| 4 | 1621 | 1621 | Yes | 3.8 |
| 5 | 1293 | 1293 | Yes | 4.39 |
| 6 | 1414 | 1414 | Yes | 3.86 |
| 7 | 1771 | 1771 | Yes | 3.58 |
| 8 | 1066 | 1066 | Yes | 4.75 |
| 9 | 1794 | 1794 | Yes | 1.82 |
| 10 | 1308 | 1308 | Yes | 3.93 |
| 11 | 1877 | 1877 | Yes | 3.55 |
| 12 | 1328 | 1328 | Yes | 4.04 |
| 13 | 2043 | 2043 | Yes | 3.9 |
| 14 | 645 | 645 | Yes | 3.14 |
| 15 | 2109 | 2109 | Yes | 4.06 |
| 16 | 1916 | 1916 | Yes | 5.8 |
| 17 | 2057 | 2057 | Yes | 2.91 |
| 18 | 1601 | 1601 | Yes | 3.91 |
| 19 | 1151 | 1151 | Yes | 6.04 |
| 20 | 1651 | 1651 | Yes | 4.68 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 66 | 66 | Yes | 24.56 |
| 2 | 38 | 38 | Yes | 27.62 |
| 3 | 52 |  | No | 96.61 |
| 4 | 74 | 74 | Yes | 32.34 |
| 5 | 52 |  | No | 90.93 |
| 6 | 56 | 55 | No | 45.48 |
| 7 | 68 |  | No | 83.17 |
| 8 | 41 | 41 | Yes | 21.08 |
| 9 | 63 |  | No | 69.73 |
| 10 | 46 |  | No | 63.31 |
| 11 | 41 |  | No | 64.87 |
| 12 | 71 | 71 | Yes | 24.42 |
| 13 | 71 | 71 | Yes | 16.97 |
| 14 | 55 |  | No | 46.25 |
| 15 | 71 |  | No | 56.55 |
| 16 | 67 | TIMEOUT | No | 120.02 |
| 17 | 38 |  | No | 58.53 |
| 18 | 46 |  | No | 66.33 |
| 19 | 41 |  | No | 70.22 |
| 20 | 50 |  | No | 89.2 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ELQJRAC | ELQJRAC | Yes | 5.29 |
| 2 | PZCKBDW | PZCKBDW | Yes | 4.47 |
| 3 | LNJFKGI | LNJFKGI | Yes | 3.0 |
| 4 | CVZUSBK | CVZUSBK | Yes | 4.94 |
| 5 | VTACOJF | VTACOJF | Yes | 8.98 |
| 6 | PCUGEOM | PCUGEOM | Yes | 7.55 |
| 7 | TFCPQIG | TFCPQIG | Yes | 5.71 |
| 8 | SOKCRFH | SOKCRFH | Yes | 4.52 |
| 9 | AQHJIGS | AQHJIGS | Yes | 5.83 |
| 10 | EZNFBVR | EZNFBVR | Yes | 4.6 |
| 11 | MFDQRIS | MFDQRIS | Yes | 5.2 |
| 12 | OTNCSWQ | OTNCSWQ | Yes | 5.94 |
| 13 | QCEPHDM | QCEPHDM | Yes | 4.09 |
| 14 | VUKJSRH | VUKJSRH | Yes | 5.2 |
| 15 | EBOWJFN | EBOWJFN | Yes | 5.84 |
| 16 | RTQHVUE | RTQHVUE | Yes | 4.92 |
| 17 | VNCTUQH | VNCTUQH | Yes | 5.73 |
| 18 | ISGVPOB | ISGVPOB | Yes | 5.68 |
| 19 | EHCRYKZ | EHCRYKZ | Yes | 5.47 |
| 20 | DMBGOCF | DMBGOCF | Yes | 5.0 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.9 |
| 2 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.55 |
| 3 | [4.5, 5.5] | 5.5 4.5 | Yes | 3.9 |
| 4 | [2.2, 7.8] | 7.8 2.2 | Yes | 6.42 |
| 5 | [4.5, 5.5] | 5.5 4.5 | Yes | 8.87 |
| 6 | [1.2, 8.8] | 1.2 8.8 | Yes | 5.72 |
| 7 | [3.6, 6.4] | 3.6 6.4 | Yes | 6.36 |
| 8 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.34 |
| 9 | [0.1, 9.9] | 9.9 0.1 | Yes | 7.44 |
| 10 | [1.7, 8.3] | 1.7 8.3 | Yes | 5.36 |
| 11 | [2.9, 7.1] | 2.9 7.1 | Yes | 6.09 |
| 12 | [0.3, 9.7] | 0.3 9.7 | Yes | 5.85 |
| 13 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.3 |
| 14 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.64 |
| 15 | [4.2, 5.8] | 4.2 5.8 | Yes | 5.88 |
| 16 | [3.7, 6.3] | 6.3 3.7 | Yes | 6.39 |
| 17 | [0.1, 9.9] | 0.1 9.9 | Yes | 6.69 |
| 18 | [2.1, 7.9] | 2.1 7.9 | Yes | 5.84 |
| 19 | [2.1, 7.9] | 2.1 7.9 | Yes | 7.24 |
| 20 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.64 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | C3S1DUZAEKXG | C3S1DUZAEKXG | Yes | 3.8 |
| 2 | 10SKDVJN7VKN | 10SKDVJN7VKN | Yes | 5.94 |
| 3 | ZDS63W58B80S | ZDS63W58B80S | Yes | 2.93 |
| 4 | AJI4G21LIVY8 | AJI4G21LIVY8 | Yes | 2.97 |
| 5 | M0QABR00BBFH | MOQABR00BBFH | No | 3.89 |
| 6 | KKBNW223WQXW | KKBNW223WQXW | Yes | 4.15 |
| 7 | 53T3QZJP4QJ5 | 53T30ZJP4QJ5 | No | 6.67 |
| 8 | 1JCGEXEZOSTW | 1JCGEXEZOSTW | Yes | 4.29 |
| 9 | R2SQW7BCGCRV | R2SQW7BCGCRV | Yes | 3.71 |
| 10 | 8M6T5UU4LLZ0 | 8M6T5UU4LLZ0 | Yes | 4.12 |
| 11 | 4CU4TQBIYM6T | 4CU4TQBIYM6T | Yes | 5.26 |
| 12 | 79BUS4FSTRDE | 79BUS4FSTRDE | Yes | 3.42 |
| 13 | 1EWHE28BTRRJ | 1EWHE28BTRRJ | Yes | 3.73 |
| 14 | 9H388TTPICFI | 9H388TTPICFI | Yes | 3.66 |
| 15 | RDXE2BUCKPX9 | RDXE2BUCKPX9 | Yes | 4.45 |
| 16 | 71M7PI5OSWQO | 71M7PI5OSWQOO | No | 15.25 |
| 17 | 7E5CL0R9O1SS | 7E5CL0R901SS | No | 4.36 |
| 18 | PGVX7H9USUF5 | PGVX7H9USUF5 | Yes | 3.76 |
| 19 | EXV41R6FBPF9 | EXV41R6FBPF9 | Yes | 3.26 |
| 20 | MQJ7T0BBUB8R | MOJ7TOBBUB8R | No | 2.99 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 |  | No | 54.15 |
| 2 | 23 | 23 | Yes | 3.92 |
| 3 | 19 | 19 | Yes | 4.25 |
| 4 | 31 | 31 | Yes | 3.15 |
| 5 | 1 | 1 | Yes | 5.06 |
| 6 | 16 | 16 | Yes | 2.99 |
| 7 | 65 | 65 | Yes | 3.46 |
| 8 | 10 | 9 | No | 22.4 |
| 9 | 5 | 5 | Yes | 3.69 |
| 10 | 793 | 793 | Yes | 3.27 |
| 11 | 26 |  | No | 51.26 |
| 12 | 39 | 39 | Yes | 4.55 |
| 13 | 7 | 7 | Yes | 2.21 |
| 14 | 73 | 73 | Yes | 46.83 |
| 15 | 48 | 48 | Yes | 2.93 |
| 16 | 4 | 4 | Yes | 4.71 |
| 17 | 198 | 198 | Yes | 4.11 |
| 18 | 243 | 243 | Yes | 1.3 |
| 19 | 44 | 44 | Yes | 3.77 |
| 20 | 67 | 67 | Yes | 2.51 |
