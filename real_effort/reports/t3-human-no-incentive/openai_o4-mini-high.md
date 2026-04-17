# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
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
| sudoku_game | 8880 | 40960 | 49840 | 0 | 20 | 43.29 | 866.07 |
| add_numbers | 4400 | 4333 | 8733 | 20 | 0 | 3.88 | 77.77 |
| counting_zeros | 7820 | 40960 | 48780 | 0 | 20 | 30.41 | 608.6 |
| task_decoding | 15860 | 23841 | 39701 | 14 | 6 | 22.25 | 445.31 |
| task_summation | 9080 | 16424 | 25504 | 20 | 0 | 10.26 | 205.36 |
| task_transcription | 4090 | 8897 | 12987 | 12 | 8 | 6.16 | 123.39 |
| task_sequences | 3061 | 11916 | 14977 | 18 | 2 | 7.80 | 156.03 |
| **TOTAL** | **53191** | **147331** | **200522** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 6 3 5 4 3 5 2 4 4 1 5 6 |  | No | 41.28 |
| 2 | 2 3 2 4 5 6 1 5 2 6 4 2 5 3 |  | No | 65.34 |
| 3 | 5 3 6 5 1 2 3 2 5 6 4 1 5 3 |  | No | 21.9 |
| 4 | 2 6 3 1 2 6 4 5 6 2 5 2 1 5 |  | No | 45.69 |
| 5 | 3 5 4 4 2 3 1 6 4 5 6 2 2 5 |  | No | 38.9 |
| 6 | 1 2 6 5 2 4 5 4 1 6 6 4 2 1 |  | No | 33.02 |
| 7 | 2 6 4 4 6 3 2 6 6 5 1 2 5 6 |  | No | 51.16 |
| 8 | 1 6 6 3 6 3 4 2 6 3 2 2 5 1 |  | No | 26.06 |
| 9 | 1 4 6 2 3 2 2 5 1 6 1 3 5 6 |  | No | 34.49 |
| 10 | 3 5 3 1 4 5 1 3 1 4 4 5 2 6 |  | No | 27.61 |
| 11 | 5 6 2 1 5 4 1 6 4 2 6 3 6 4 |  | No | 53.98 |
| 12 | 2 5 4 3 1 6 4 6 5 4 3 2 2 1 |  | No | 35.19 |
| 13 | 3 5 1 6 1 2 3 3 5 6 1 3 1 5 |  | No | 50.51 |
| 14 | 4 1 1 4 6 5 3 2 5 3 4 5 6 4 |  | No | 50.23 |
| 15 | 3 2 5 6 3 2 1 3 6 1 5 3 2 1 |  | No | 52.95 |
| 16 | 3 6 4 1 5 6 3 1 1 2 4 5 6 3 |  | No | 42.42 |
| 17 | 4 5 2 2 2 3 6 5 5 4 1 1 5 3 |  | No | 60.09 |
| 18 | 1 5 4 6 4 3 1 6 5 6 4 2 2 1 |  | No | 40.75 |
| 19 | 5 3 5 1 2 6 4 6 1 3 5 5 2 1 |  | No | 47.38 |
| 20 | 2 5 1 6 5 4 5 6 3 4 5 1 5 6 |  | No | 46.92 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1806 | 1806 | Yes | 3.61 |
| 2 | 1213 | 1213 | Yes | 2.51 |
| 3 | 1712 | 1712 | Yes | 2.47 |
| 4 | 1521 | 1521 | Yes | 2.92 |
| 5 | 1628 | 1628 | Yes | 4.46 |
| 6 | 2033 | 2033 | Yes | 2.61 |
| 7 | 1557 | 1557 | Yes | 3.36 |
| 8 | 1246 | 1246 | Yes | 5.53 |
| 9 | 1485 | 1485 | Yes | 2.83 |
| 10 | 1875 | 1875 | Yes | 2.83 |
| 11 | 1326 | 1326 | Yes | 4.2 |
| 12 | 1625 | 1625 | Yes | 2.91 |
| 13 | 1774 | 1774 | Yes | 2.39 |
| 14 | 1185 | 1185 | Yes | 2.68 |
| 15 | 1766 | 1766 | Yes | 2.06 |
| 16 | 1987 | 1987 | Yes | 2.82 |
| 17 | 1299 | 1299 | Yes | 2.47 |
| 18 | 1384 | 1384 | Yes | 2.39 |
| 19 | 1703 | 1703 | Yes | 20.42 |
| 20 | 1950 | 1950 | Yes | 2.16 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 38 |  | No | 39.15 |
| 2 | 70 |  | No | 31.5 |
| 3 | 43 |  | No | 15.79 |
| 4 | 57 |  | No | 16.91 |
| 5 | 41 |  | No | 18.42 |
| 6 | 66 |  | No | 25.81 |
| 7 | 74 |  | No | 28.13 |
| 8 | 64 |  | No | 33.98 |
| 9 | 37 |  | No | 32.54 |
| 10 | 52 |  | No | 25.64 |
| 11 | 46 |  | No | 25.21 |
| 12 | 74 |  | No | 27.96 |
| 13 | 58 |  | No | 38.24 |
| 14 | 60 |  | No | 32.01 |
| 15 | 74 |  | No | 21.62 |
| 16 | 60 |  | No | 50.57 |
| 17 | 46 |  | No | 46.32 |
| 18 | 66 |  | No | 58.72 |
| 19 | 74 |  | No | 19.6 |
| 20 | 48 |  | No | 20.15 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TEMKXSG | TEMKXSG | Yes | 8.86 |
| 2 | DYNBVAL |  | No | 37.05 |
| 3 | OZMCTIG | OZMCTIG | Yes | 17.83 |
| 4 | EAVRBHM |  | No | 41.33 |
| 5 | GLUDCKI | GLUDCKI | Yes | 10.97 |
| 6 | WDUVFSR | WDUVFSR | Yes | 9.53 |
| 7 | QONHBFK | QONHBFK | Yes | 20.97 |
| 8 | NLGATUP | NLGATUP | Yes | 8.1 |
| 9 | HRXFTPL | HRXFTPL | Yes | 10.67 |
| 10 | JOUCAML |  | No | 55.47 |
| 11 | IDVSKOA | IDVSKOA | Yes | 14.72 |
| 12 | AVPBGTI | AVPBGTI | Yes | 17.63 |
| 13 | TGSCNVA | TGSCNVA | Yes | 13.76 |
| 14 | BHVXEQD | BHVXEQD | Yes | 9.68 |
| 15 | NDPUQEM | NDPUQEM | Yes | 9.65 |
| 16 | KEIGHBU |  | No | 58.6 |
| 17 | VEBHAOR |  | No | 44.01 |
| 18 | VPCDKMR | VPCDKMR | Yes | 5.2 |
| 19 | GTBFXLP | GTBFXLP | Yes | 5.36 |
| 20 | EWTQPNC |  | No | 45.69 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.8, 5.2] | 5.2 4.8 | Yes | 9.17 |
| 2 | [0.3, 9.7] | 0.3 9.7 | Yes | 12.0 |
| 3 | [1.2, 8.8] | 8.8 1.2 | Yes | 10.94 |
| 4 | [3.9, 6.1] | 3.9 6.1 | Yes | 10.96 |
| 5 | [2.8, 7.2] | 2.8 7.2 | Yes | 10.51 |
| 6 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.55 |
| 7 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.84 |
| 8 | [4.2, 5.8] | 4.2 5.8 | Yes | 10.86 |
| 9 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.44 |
| 10 | [3.3, 6.7] | 3.3 6.7 | Yes | 10.11 |
| 11 | [3.4, 6.6] | 3.4 6.6 | Yes | 11.36 |
| 12 | [0.7, 9.3] | 9.3 0.7 | Yes | 10.16 |
| 13 | [0.6, 9.4] | 0.6 9.4 | Yes | 10.09 |
| 14 | [0.8, 9.2] | 0.8 9.2 | Yes | 10.27 |
| 15 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.86 |
| 16 | [4.2, 5.8] | 5.8 4.2 | Yes | 9.96 |
| 17 | [0.3, 9.7] | 0.3 9.7 | Yes | 10.73 |
| 18 | [1.4, 8.6] | 8.6 1.4 | Yes | 10.37 |
| 19 | [2.0, 8.0] | 2.0 8.0 | Yes | 11.84 |
| 20 | [1.6, 8.4] | 1.6 8.4 | Yes | 9.14 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | L70XEUHK4E49 | L70XEUHK4E49 | Yes | 5.14 |
| 2 | I0SEMK5M7IX1 | IOSEMK5M7IX1 | No | 2.71 |
| 3 | DX9O3PKWB4LV | DX903PKWB4LV | No | 2.04 |
| 4 | WJIXKN3J4QGZ | WJIXKN3J4QGZ | Yes | 2.09 |
| 5 | VKBI25ZBFR1S | VKBI25ZBFR1S | Yes | 2.13 |
| 6 | 6DXPIO0NLXUT | 6DXPI00NLXUT | No | 4.36 |
| 7 | G4OR33YW7J9T | G40R33YW7J9T | No | 5.25 |
| 8 | VDU4GV2N258Y | VDU4GV2N258Y | Yes | 2.58 |
| 9 | G75R41OLAUFV | G75R410LAUFV | No | 17.3 |
| 10 | 8MNYTIPX8FAG | 8MNYTIPX8FAG | Yes | 2.66 |
| 11 | TQFYT66HNTVF | TQFY T66HNTVF | No | 4.84 |
| 12 | 9BWK4E9JJ835 | 9BWK4E9JJ835 | Yes | 3.61 |
| 13 | 1PFE4PGH075J | 1PFE4PGH075J | Yes | 3.17 |
| 14 | 1UQ86M06T8DW | 1UQ86M06T8DW | Yes | 5.64 |
| 15 | V2H4G98HNKKR |  | No | 38.22 |
| 16 | 2QUKVP3K01VW | 2QUKVP3K01VW | Yes | 2.95 |
| 17 | OYT9BR9D4PA2 | OYT9BR9D4PA2 | Yes | 2.36 |
| 18 | YRFLIKCCFVU4 | YRFLIKCCFVU4 | Yes | 3.69 |
| 19 | QPGZRO1OD5QU | QPGZR01OD5QU | No | 9.3 |
| 20 | AET1UUMWT7KR | AET1UUMWT7KR | Yes | 3.25 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 31 | 31 | Yes | 2.94 |
| 2 | 60 | 60 | Yes | 6.83 |
| 3 | 44 | 44 | Yes | 8.64 |
| 4 | 4 | 4 | Yes | 4.12 |
| 5 | 4096 | 16384 | No | 13.23 |
| 6 | 9 | 9 | Yes | 3.95 |
| 7 | 1 | 1 | Yes | 7.1 |
| 8 | 60 | 60 | Yes | 3.13 |
| 9 | 7680 | 7680 | Yes | 8.71 |
| 10 | 243 | 243 | Yes | 9.19 |
| 11 | 36 | 42 | No | 4.67 |
| 12 | 26 | 26 | Yes | 11.94 |
| 13 | 5 | 5 | Yes | 7.79 |
| 14 | 28 | 28 | Yes | 9.07 |
| 15 | 16 | 16 | Yes | 8.5 |
| 16 | 4 | 4 | Yes | 9.47 |
| 17 | 39 | 39 | Yes | 18.45 |
| 18 | 67 | 67 | Yes | 4.37 |
| 19 | 19 | 19 | Yes | 11.7 |
| 20 | 6 | 6 | Yes | 2.23 |
