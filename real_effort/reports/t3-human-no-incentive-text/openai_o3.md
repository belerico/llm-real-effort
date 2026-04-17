# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-27 10:25:00

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 5292 | 40960 | 46252 | 0 | 20 | 35.97 | 719.51 |
| add_numbers | 3060 | 3660 | 6720 | 20 | 0 | 3.51 | 70.12 |
| counting_zeros | 4460 | 39402 | 43862 | 3 | 17 | 31.48 | 629.54 |
| task_decoding | 4400 | 5163 | 9563 | 20 | 0 | 4.42 | 88.41 |
| task_summation | 4740 | 11195 | 15935 | 20 | 0 | 8.31 | 166.22 |
| task_transcription | 3044 | 1902 | 4946 | 19 | 1 | 7.95 | 159.07 |
| task_sequences | 2907 | 10841 | 13748 | 16 | 4 | 17.88 | 357.68 |
| string_entry | 3498 | 23450 | 26948 | 9 | 11 | 17.29 | 345.84 |
| **TOTAL** | **31401** | **136573** | **167974** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 5 5 5 2 2 6 5 3 6 1 6 4 |  | No | 42.32 |
| 2 | 3 1 4 3 6 4 6 4 1 1 4 2 6 3 |  | No | 39.68 |
| 3 | 6 3 5 2 5 6 2 3 5 6 6 2 1 3 |  | No | 19.92 |
| 4 | 6 2 5 1 4 6 1 3 2 6 1 2 6 3 |  | No | 42.65 |
| 5 | 2 3 2 6 1 6 1 6 3 4 5 3 4 2 |  | No | 38.01 |
| 6 | 4 2 5 3 3 5 2 2 2 6 2 6 1 4 |  | No | 37.5 |
| 7 | 2 3 5 2 6 4 1 6 3 4 5 6 4 1 |  | No | 43.84 |
| 8 | 5 4 2 1 3 5 6 4 2 6 4 2 5 1 |  | No | 34.23 |
| 9 | 4 1 2 5 4 5 2 2 6 1 4 3 1 6 |  | No | 44.07 |
| 10 | 6 3 4 5 6 3 1 1 2 6 4 1 1 2 |  | No | 22.7 |
| 11 | 3 6 1 5 3 1 2 6 2 4 5 1 5 4 |  | No | 40.29 |
| 12 | 4 1 5 3 3 2 4 1 6 4 6 1 5 2 |  | No | 39.67 |
| 13 | 5 4 1 5 6 1 3 3 4 5 1 5 6 3 |  | No | 18.65 |
| 14 | 3 6 6 3 1 5 1 3 3 1 4 3 1 4 |  | No | 31.16 |
| 15 | 1 6 4 5 3 5 1 5 5 1 6 3 5 4 |  | No | 42.82 |
| 16 | 1 3 4 1 5 4 1 6 2 2 3 1 4 3 |  | No | 21.55 |
| 17 | 3 6 4 5 3 4 6 2 5 1 5 1 5 4 |  | No | 41.0 |
| 18 | 4 2 5 1 6 2 4 6 4 1 4 3 5 1 |  | No | 39.26 |
| 19 | 3 6 1 3 4 6 2 1 3 6 5 6 4 1 |  | No | 27.7 |
| 20 | 2 3 5 5 5 2 4 6 2 5 3 2 3 6 |  | No | 52.43 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 927 | 927 | Yes | 4.09 |
| 2 | 2043 | 2043 | Yes | 3.59 |
| 3 | 1604 | 1604 | Yes | 2.68 |
| 4 | 1915 | 1915 | Yes | 2.93 |
| 5 | 2256 | 2256 | Yes | 2.15 |
| 6 | 1329 | 1329 | Yes | 3.97 |
| 7 | 693 | 693 | Yes | 3.67 |
| 8 | 1304 | 1304 | Yes | 3.69 |
| 9 | 1379 | 1379 | Yes | 5.29 |
| 10 | 1885 | 1885 | Yes | 3.7 |
| 11 | 1863 | 1863 | Yes | 4.22 |
| 12 | 1066 | 1066 | Yes | 2.87 |
| 13 | 1505 | 1505 | Yes | 4.17 |
| 14 | 2280 | 2280 | Yes | 4.23 |
| 15 | 1350 | 1350 | Yes | 2.67 |
| 16 | 1102 | 1102 | Yes | 3.71 |
| 17 | 1506 | 1506 | Yes | 4.26 |
| 18 | 2115 | 2115 | Yes | 2.17 |
| 19 | 1336 | 1336 | Yes | 3.78 |
| 20 | 1520 | 1520 | Yes | 2.27 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 62 |  | No | 37.75 |
| 2 | 73 |  | No | 45.84 |
| 3 | 59 |  | No | 32.36 |
| 4 | 60 | 60 | Yes | 11.09 |
| 5 | 61 |  | No | 28.76 |
| 6 | 73 |  | No | 31.5 |
| 7 | 37 |  | No | 34.65 |
| 8 | 49 |  | No | 24.76 |
| 9 | 67 | 67 | Yes | 25.61 |
| 10 | 74 |  | No | 56.79 |
| 11 | 43 |  | No | 33.17 |
| 12 | 56 |  | No | 21.06 |
| 13 | 52 |  | No | 41.27 |
| 14 | 60 |  | No | 23.41 |
| 15 | 60 |  | No | 31.82 |
| 16 | 67 | 67 | Yes | 15.63 |
| 17 | 58 |  | No | 27.95 |
| 18 | 48 |  | No | 32.85 |
| 19 | 62 |  | No | 37.21 |
| 20 | 71 |  | No | 36.03 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TUXJZHM | TUXJZHM | Yes | 9.08 |
| 2 | GQTDVLN | GQTDVLN | Yes | 2.79 |
| 3 | UKYZTMV | UKYZTMV | Yes | 4.42 |
| 4 | MOPXLEC | MOPXLEC | Yes | 2.85 |
| 5 | HMNVDPA | HMNVDPA | Yes | 5.48 |
| 6 | XJAHPQO | XJAHPQO | Yes | 4.53 |
| 7 | KJAYOGZ | KJAYOGZ | Yes | 3.01 |
| 8 | BCVHNLU | BCVHNLU | Yes | 5.23 |
| 9 | QAFHGJN | QAFHGJN | Yes | 3.28 |
| 10 | UYHVPGI | UYHVPGI | Yes | 3.53 |
| 11 | WENGFYT | WENGFYT | Yes | 6.2 |
| 12 | KUQESWC | KUQESWC | Yes | 2.77 |
| 13 | JCWYDAP | JCWYDAP | Yes | 4.75 |
| 14 | MURXQZT | MURXQZT | Yes | 2.68 |
| 15 | UODMCFA | UODMCFA | Yes | 3.41 |
| 16 | ZNUSDAQ | ZNUSDAQ | Yes | 9.08 |
| 17 | DUPVMEL | DUPVMEL | Yes | 6.51 |
| 18 | JXHVQOI | JXHVQOI | Yes | 2.35 |
| 19 | YVKFROD | YVKFROD | Yes | 3.36 |
| 20 | GTEFKVB | GTEFKVB | Yes | 3.1 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.6, 8.4] | 1.6 8.4 | Yes | 5.08 |
| 2 | [4.0, 6.0] | 4.0 6.0 | Yes | 8.21 |
| 3 | [1.3, 8.7] | 8.7 1.3 | Yes | 14.12 |
| 4 | [1.6, 8.4] | 8.4 1.6 | Yes | 8.17 |
| 5 | [4.7, 5.3] | 4.7 5.3 | Yes | 8.93 |
| 6 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.32 |
| 7 | [3.1, 6.9] | 6.9 3.1 | Yes | 5.65 |
| 8 | [1.0, 9.0] | 1.0 9.0 | Yes | 8.49 |
| 9 | [3.8, 6.2] | 6.2 3.8 | Yes | 8.24 |
| 10 | [4.0, 6.0] | 6.0 4.0 | Yes | 8.4 |
| 11 | [1.3, 8.7] | 1.3 8.7 | Yes | 9.76 |
| 12 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.85 |
| 13 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.97 |
| 14 | [3.6, 6.4] | 3.6 6.4 | Yes | 9.09 |
| 15 | [4.5, 5.5] | 4.5 5.5 | Yes | 7.98 |
| 16 | [1.3, 8.7] | 1.3 8.7 | Yes | 8.98 |
| 17 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.97 |
| 18 | [0.1, 9.9] | 0.1 9.9 | Yes | 10.27 |
| 19 | [3.8, 6.2] | 6.2 3.8 | Yes | 6.86 |
| 20 | [0.9, 9.1] | 0.9 9.1 | Yes | 5.89 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 544ILIJQS7PT | 544ILIJQS7PT | Yes | 1.55 |
| 2 | ZANV9T5WTRAC | ZANV9T5WTRAC | Yes | 1.82 |
| 3 | ZNBYUR2P3KZO | ZNBYUR2P3KZO | Yes | 1.7 |
| 4 | X6RLVY8ZYDDA | X6RLVY8ZYDDA | Yes | 1.61 |
| 5 | RTSBFXVVG7S4 | RTSBFXVVG7S4 | Yes | 1.7 |
| 6 | 8QPPHML9CUYO | 8QPPHML9CUYO | Yes | 2.32 |
| 7 | 7VIH2IZNGKGW | 7VIH2IZNGKGW | Yes | 2.6 |
| 8 | YIQOCCYJ0X1B | YIQOCCYJ0X1B | Yes | 1.76 |
| 9 | RODRGQFIBFAG | RODRGQFIBFAG | Yes | 1.73 |
| 10 | XM5BBK2UX73Q | XM5BBK2UX73Q | Yes | 1.8 |
| 11 | O7SYTSH3BECP | O7SYTSH3BECP | Yes | 1.89 |
| 12 | 5L44U39OAS6R | 5L44U39OAS6R | Yes | 1.72 |
| 13 | B1TJN378MXJE | B1TJN378MXJE | Yes | 1.88 |
| 14 | NY10QKWI85P6 | NY10QKWI85P6 | Yes | 1.77 |
| 15 | 7AEZQI1WKOKL | 7AEZQI1WKOKL | Yes | 1.62 |
| 16 | POEFOOF3GYV4 | POEFOOF3GYV4 | Yes | 2.47 |
| 17 | 8X9EIUIFS1QV | 8X9EIUIFS1QV | Yes | 3.93 |
| 18 | 3ORAFR4TZQ0U | 3ORAFR4TZQ0U | Yes | 2.9 |
| 19 | 32GPBL6D2X3K | TIMEOUT | No | 120.03 |
| 20 | 3OJVXND0E87J | 3OJVXND0E87J | Yes | 2.26 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 |  | No | 42.81 |
| 2 | 3 | 3 | Yes | 21.88 |
| 3 | 4 | 4 | Yes | 3.55 |
| 4 | 60 | 60 | Yes | 8.06 |
| 5 | 73 | 73 | Yes | 11.26 |
| 6 | 60 | TIMEOUT | No | 120.03 |
| 7 | 3 | 3 | Yes | 7.06 |
| 8 | 5 | 2 | No | 10.95 |
| 9 | 793 | 793 | Yes | 2.53 |
| 10 | 26 | 26 | Yes | 10.52 |
| 11 | 48 | 48 | Yes | 4.84 |
| 12 | 31 | 31 | Yes | 5.07 |
| 13 | 28 | 28 | Yes | 9.63 |
| 14 | 19 | 19 | Yes | 16.89 |
| 15 | 9 | 9 | Yes | 7.77 |
| 16 | 20 |  | No | 50.35 |
| 17 | 7680 | 7680 | Yes | 10.2 |
| 18 | 65 | 65 | Yes | 3.79 |
| 19 | 1440 | 1440 | Yes | 2.41 |
| 20 | 44 | 44 | Yes | 8.07 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( ( (<)/\ | ( ( (<)/\ | Yes | 11.17 |
| 2 | _(</_\((  |  | No | 69.98 |
| 3 | ))< <_ \) | ))< <_ \) | Yes | 3.28 |
| 4 | )<\\_( _/ | )<\\_ (_/ | No | 7.8 |
| 5 | ))<  /<(  | ))<  /<( | No | 11.16 |
| 6 | \(/)((_)< |  | No | 22.52 |
| 7 | \<<)/<_)\ | \<<)/<_)\ | Yes | 18.68 |
| 8 | _(/(<// \ | _(/(<// \ | Yes | 7.45 |
| 9 |  </))<_\\ | </))<_\\ | No | 7.07 |
| 10 | \_/(</(<( |  | No | 32.78 |
| 11 | ())(/ </  | /\) <(_<) | No | 22.13 |
| 12 | _)(<( \() |  | No | 25.89 |
| 13 | <\//((/ _ | <\//((/ _ | Yes | 4.94 |
| 14 |  /(\)\  ( | /(\)\  ( | No | 17.89 |
| 15 | _<()(//)\ | _<()(//)\ | Yes | 5.65 |
| 16 | )\  \((_  | )\  \((_ | No | 15.42 |
| 17 | )(_/))\ < | )(_/))\ < | Yes | 6.36 |
| 18 | )\_<\)<() | )\_<\)<() | Yes | 3.96 |
| 19 | \)) \)\_/ | \)) \)\_/ | Yes | 7.4 |
| 20 | )())(\\\  |  | No | 44.3 |
