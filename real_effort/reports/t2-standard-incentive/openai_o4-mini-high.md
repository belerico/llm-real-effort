# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
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
| sudoku_game | 8720 | 40960 | 49680 | 0 | 20 | 43.90 | 878.25 |
| add_numbers | 4240 | 3705 | 7945 | 20 | 0 | 3.04 | 60.81 |
| counting_zeros | 7660 | 40960 | 48620 | 0 | 20 | 36.84 | 737.14 |
| task_decoding | 15700 | 26976 | 42676 | 17 | 3 | 20.30 | 406.17 |
| task_summation | 8920 | 19921 | 28841 | 19 | 1 | 10.97 | 219.53 |
| task_transcription | 3955 | 8313 | 12268 | 13 | 7 | 4.85 | 97.24 |
| task_sequences | 2901 | 13570 | 16471 | 18 | 2 | 13.06 | 261.28 |
| **TOTAL** | **52096** | **154405** | **206501** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 1 1 3 1 2 5 2 6 4 3 2 4 |  | No | 43.35 |
| 2 | 6 4 5 5 6 3 2 3 4 6 4 1 4 1 |  | No | 57.73 |
| 3 | 6 5 3 2 5 1 2 3 4 2 4 6 5 3 |  | No | 47.88 |
| 4 | 2 5 3 6 1 3 1 5 2 6 4 1 2 3 |  | No | 66.42 |
| 5 | 1 5 4 4 1 3 5 3 1 4 3 5 6 4 |  | No | 22.55 |
| 6 | 2 5 3 3 2 5 4 5 3 5 3 4 3 4 |  | No | 49.92 |
| 7 | 4 6 3 1 4 5 1 2 6 3 2 3 2 6 |  | No | 32.16 |
| 8 | 3 5 4 2 4 6 5 4 2 1 2 4 2 6 |  | No | 44.89 |
| 9 | 3 4 1 3 6 3 6 4 2 4 2 3 3 2 |  | No | 39.51 |
| 10 | 5 3 2 2 4 1 3 1 3 2 4 6 6 2 |  | No | 46.83 |
| 11 | 3 2 6 6 4 1 1 3 4 5 2 6 5 1 |  | No | 43.26 |
| 12 | 6 3 5 2 5 2 4 6 5 6 1 4 4 5 |  | No | 50.28 |
| 13 | 3 1 4 1 1 5 2 1 4 2 6 6 4 2 |  | No | 47.3 |
| 14 | 6 3 6 1 5 5 1 4 6 5 1 6 1 6 |  | No | 39.95 |
| 15 | 3 5 2 2 6 1 4 1 6 1 3 4 5 1 |  | No | 34.77 |
| 16 | 6 3 6 1 5 3 1 2 1 6 1 5 6 4 |  | No | 40.73 |
| 17 | 3 1 4 2 5 3 4 6 6 3 4 1 4 5 |  | No | 36.63 |
| 18 | 2 4 3 4 1 3 5 2 1 6 5 1 4 5 |  | No | 43.95 |
| 19 | 6 4 1 2 6 4 5 6 6 1 1 2 3 4 |  | No | 40.13 |
| 20 | 3 6 5 1 4 1 4 1 6 2 3 2 5 5 |  | No | 49.81 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1248 | 1248 | Yes | 1.69 |
| 2 | 1337 | 1337 | Yes | 4.03 |
| 3 | 885 | 885 | Yes | 2.09 |
| 4 | 983 | 983 | Yes | 2.82 |
| 5 | 1205 | 1205 | Yes | 2.66 |
| 6 | 2050 | 2050 | Yes | 2.48 |
| 7 | 1882 | 1882 | Yes | 3.97 |
| 8 | 2052 | 2052 | Yes | 1.98 |
| 9 | 1436 | 1436 | Yes | 2.45 |
| 10 | 1253 | 1253 | Yes | 3.42 |
| 11 | 2413 | 2413 | Yes | 2.67 |
| 12 | 1986 | 1986 | Yes | 3.81 |
| 13 | 1921 | 1921 | Yes | 2.56 |
| 14 | 1057 | 1057 | Yes | 4.41 |
| 15 | 1241 | 1241 | Yes | 2.7 |
| 16 | 1668 | 1668 | Yes | 3.32 |
| 17 | 2224 | 2224 | Yes | 3.94 |
| 18 | 2442 | 2442 | Yes | 5.73 |
| 19 | 1752 | 1752 | Yes | 1.86 |
| 20 | 1450 | 1450 | Yes | 2.11 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 70 |  | No | 21.06 |
| 2 | 56 |  | No | 37.55 |
| 3 | 43 |  | No | 43.32 |
| 4 | 65 |  | No | 54.62 |
| 5 | 52 |  | No | 20.27 |
| 6 | 71 |  | No | 35.18 |
| 7 | 63 |  | No | 22.05 |
| 8 | 72 |  | No | 46.49 |
| 9 | 42 |  | No | 35.46 |
| 10 | 45 |  | No | 54.67 |
| 11 | 65 |  | No | 25.79 |
| 12 | 54 |  | No | 31.58 |
| 13 | 61 |  | No | 34.37 |
| 14 | 74 |  | No | 37.66 |
| 15 | 50 |  | No | 46.26 |
| 16 | 49 |  | No | 25.65 |
| 17 | 75 |  | No | 31.2 |
| 18 | 66 |  | No | 40.51 |
| 19 | 70 |  | No | 46.07 |
| 20 | 42 |  | No | 47.04 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DJPEQWR | DJPEQWR | Yes | 14.23 |
| 2 | MNQRKCU |  | No | 47.76 |
| 3 | NRCBXDV | NRCBXDV | Yes | 23.37 |
| 4 | WYNQODT | WYNQODT | Yes | 18.91 |
| 5 | TPISBNU | TPISBNU | Yes | 12.29 |
| 6 | SHFKBMG | SHFKBMG | Yes | 17.86 |
| 7 | QYZMKEA | QYZMKEA | Yes | 13.33 |
| 8 | YTGAPNH | YTGAPNH | Yes | 11.47 |
| 9 | XKTGQON | XKTGQON | Yes | 11.32 |
| 10 | KXEWZHL |  | No | 56.12 |
| 11 | VACHWUT | VACHWUT | Yes | 13.65 |
| 12 | JSZCNKA | JSZCNKA | Yes | 15.72 |
| 13 | TVHOFBA | TVHOFBA | Yes | 20.53 |
| 14 | DCFSEUV |  | No | 49.53 |
| 15 | AGUEWZT | AGUEWZT | Yes | 16.42 |
| 16 | FUYEQKI | FUYEQKI | Yes | 16.52 |
| 17 | NHZQRCI | NHZQRCI | Yes | 7.32 |
| 18 | BJNMDHT | BJNMDHT | Yes | 19.47 |
| 19 | SQIGRWT | SQIGRWT | Yes | 12.03 |
| 20 | UTBQKLR | UTBQKLR | Yes | 8.1 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 3.5 6.5 | Yes | 10.51 |
| 2 | [1.3, 8.7] | 1.3 8.7 | Yes | 9.36 |
| 3 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.1 |
| 4 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.62 |
| 5 | [0.9, 9.1] | 0.9 9.1 | Yes | 11.3 |
| 6 | [0.1, 9.9] | 0.1 9.9 | Yes | 12.02 |
| 7 | [4.9, 5.1] | 4.9 5.1 | Yes | 10.3 |
| 8 | [2.3, 7.7] | 7.7 2.3 | Yes | 8.08 |
| 9 | [4.5, 5.5] |  | No | 18.9 |
| 10 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.7 |
| 11 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.75 |
| 12 | [0.1, 9.9] | 0.1 9.9 | Yes | 11.14 |
| 13 | [0.7, 9.3] | 0.7 9.3 | Yes | 10.35 |
| 14 | [1.3, 8.7] | 8.7 1.3 | Yes | 10.06 |
| 15 | [0.1, 9.9] | 0.1 9.9 | Yes | 12.88 |
| 16 | [2.4, 7.6] | 2.4 7.6 | Yes | 11.63 |
| 17 | [3.0, 7.0] | 3.0 7.0 | Yes | 14.76 |
| 18 | [5.0, 5.0] | 5.0 5.0 | Yes | 6.52 |
| 19 | [3.9, 6.1] | 3.9 6.1 | Yes | 12.64 |
| 20 | [4.4, 5.6] | 4.4 5.6 | Yes | 12.7 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QALBGWQM3YLX | QALBGWQM3YLX | Yes | 5.94 |
| 2 | 5GOU2WD4N0CM | 5GOU2WD4N0CM | Yes | 2.78 |
| 3 | 7FR1LI4VSX6C | 7FR1LI4VSX6C | Yes | 3.13 |
| 4 | 30KLG6765XOJ | 30KLG6765XOJ | Yes | 3.33 |
| 5 | Y1DNPGBRC22Q | Y1DNPG BRC22Q | No | 5.99 |
| 6 | 9KI92ORSSG12 | 9KI92ORSSG12 | Yes | 5.7 |
| 7 | 4TMEECF0ESDE | 4TMEECFOESDE | No | 13.23 |
| 8 | F3HBE61YWOO6 | F3HBE61YWO06 | No | 13.74 |
| 9 | EFMEE0UCRBVV | EFMEEOUCRBVV | No | 3.88 |
| 10 | VG3Y73G80U94 | VG3Y73G80U94 | Yes | 2.52 |
| 11 | W3HU5QXJM62J | W3HU5QXJM62J | Yes | 2.77 |
| 12 | NGTOIOPKHZ6J | NGTOIOPKHZ6J | Yes | 2.8 |
| 13 | 30C8XHJXBOR2 | 30C8XHJXB0R2 | No | 5.98 |
| 14 | 4K9MWR16XTQJ | 4K9MWR16XTQJ | Yes | 3.4 |
| 15 | AT677O3MT97Z | AT677O3MT97Z | Yes | 4.89 |
| 16 | 3OK14967PWFC | 3OK14967PWFC | Yes | 3.1 |
| 17 | SFTF62UD3ZVE | SFTF62UD3ZVE | Yes | 2.67 |
| 18 | JED7W79F7DWC | JED7W79F7DWC | Yes | 2.5 |
| 19 | 0JQSR9RBYKPH | OJQSR9RBYKPH | No | 5.49 |
| 20 | GJN1NJOOUSGW | GJN1NJ00USGW | No | 3.26 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 6.82 |
| 2 | 20 | 20 | Yes | 22.13 |
| 3 | 63 | 63 | Yes | 13.19 |
| 4 | 36 | 36 | Yes | 4.28 |
| 5 | 3 | 3 | Yes | 9.99 |
| 6 | 5 |  | No | 40.73 |
| 7 | 3 | 3 | Yes | 13.77 |
| 8 | 65 | 65 | Yes | 4.0 |
| 9 | 39 | 39 | Yes | 3.72 |
| 10 | 19 | 19 | Yes | 4.62 |
| 11 | 64 | 64 | Yes | 57.12 |
| 12 | 73 | 73 | Yes | 8.56 |
| 13 | 48 | 48 | Yes | 6.99 |
| 14 | 1440 | 1440 | Yes | 2.44 |
| 15 | 4096 |  | No | 28.88 |
| 16 | 6 | 6 | Yes | 4.55 |
| 17 | 31 | 31 | Yes | 5.21 |
| 18 | 10 | 10 | Yes | 8.4 |
| 19 | 26 | 26 | Yes | 13.12 |
| 20 | 243 | 243 | Yes | 2.75 |
