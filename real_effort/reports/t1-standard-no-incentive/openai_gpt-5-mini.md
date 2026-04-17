# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
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
| sudoku_game | 7020 | 40960 | 47980 | 0 | 20 | 78.07 | 1561.66 |
| add_numbers | 3600 | 4773 | 8373 | 20 | 0 | 9.71 | 194.38 |
| counting_zeros | 5719 | 31674 | 37393 | 0 | 20 | 48.03 | 960.92 |
| task_decoding | 11760 | 16327 | 28087 | 19 | 1 | 15.37 | 307.56 |
| task_summation | 6960 | 12234 | 19194 | 20 | 0 | 11.75 | 235.29 |
| task_transcription | 3414 | 18775 | 22189 | 15 | 5 | 22.77 | 455.58 |
| task_sequences | 2721 | 15664 | 18385 | 10 | 10 | 16.82 | 336.48 |
| **TOTAL** | **41194** | **140407** | **181601** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 6 4 2 5 3 6 4 2 6 3 1 2 |  | No | 78.07 |
| 2 | 2 4 3 5 5 4 4 3 2 4 1 6 5 1 |  | No | 72.69 |
| 3 | 6 4 4 3 2 4 2 1 1 5 3 3 6 5 |  | No | 88.44 |
| 4 | 4 6 2 4 3 1 5 6 4 1 4 3 3 4 |  | No | 92.85 |
| 5 | 2 6 4 3 4 6 1 1 3 2 6 4 3 1 |  | No | 79.38 |
| 6 | 5 6 2 1 5 1 1 3 2 2 5 3 5 2 |  | No | 93.37 |
| 7 | 6 1 2 5 3 5 2 6 3 6 1 4 2 5 |  | No | 85.67 |
| 8 | 5 6 2 2 5 6 6 3 2 4 3 5 6 2 |  | No | 79.71 |
| 9 | 1 3 5 4 3 6 4 5 2 4 3 1 2 5 |  | No | 89.55 |
| 10 | 5 6 2 1 5 4 1 5 6 4 2 6 4 2 |  | No | 91.84 |
| 11 | 3 4 2 6 5 6 2 5 1 4 3 2 2 5 |  | No | 92.72 |
| 12 | 3 1 2 4 4 6 3 4 2 2 5 4 3 4 |  | No | 73.61 |
| 13 | 2 5 3 1 2 1 5 4 3 2 4 5 1 6 |  | No | 66.79 |
| 14 | 3 4 1 6 1 6 5 4 6 6 1 4 2 5 |  | No | 62.06 |
| 15 | 3 1 6 5 6 1 4 1 4 6 2 3 3 1 |  | No | 66.89 |
| 16 | 3 6 5 5 3 6 3 4 2 5 3 5 4 2 |  | No | 70.13 |
| 17 | 5 1 5 1 3 6 5 1 3 5 2 6 6 4 |  | No | 83.28 |
| 18 | 5 3 4 1 5 3 6 3 4 5 4 1 1 3 |  | No | 74.61 |
| 19 | 1 4 1 4 1 2 6 2 3 5 6 2 4 1 |  | No | 57.07 |
| 20 | 6 1 3 5 2 4 6 3 2 1 5 2 2 6 |  | No | 62.72 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1208 | 1208 | Yes | 5.26 |
| 2 | 1678 | 1678 | Yes | 4.95 |
| 3 | 1915 | 1915 | Yes | 5.47 |
| 4 | 1199 | 1199 | Yes | 6.81 |
| 5 | 1376 | 1376 | Yes | 33.86 |
| 6 | 1648 | 1648 | Yes | 4.52 |
| 7 | 1737 | 1737 | Yes | 19.14 |
| 8 | 2504 | 2504 | Yes | 5.27 |
| 9 | 841 | 841 | Yes | 5.02 |
| 10 | 1864 | 1864 | Yes | 8.55 |
| 11 | 1542 | 1542 | Yes | 9.16 |
| 12 | 1733 | 1733 | Yes | 7.33 |
| 13 | 1481 | 1481 | Yes | 15.24 |
| 14 | 2062 | 2062 | Yes | 7.75 |
| 15 | 1644 | 1644 | Yes | 9.33 |
| 16 | 1378 | 1378 | Yes | 7.23 |
| 17 | 2094 | 2094 | Yes | 14.37 |
| 18 | 1717 | 1717 | Yes | 5.62 |
| 19 | 1482 | 1482 | Yes | 6.44 |
| 20 | 1052 | 1052 | Yes | 12.96 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 35 |  | No | 96.23 |
| 2 | 56 | TIMEOUT | No | 120.02 |
| 3 | 72 |  | No | 85.96 |
| 4 | 70 |  | No | 77.02 |
| 5 | 63 | 67 | No | 32.02 |
| 6 | 35 | 67 | No | 20.93 |
| 7 | 55 | 67 | No | 28.2 |
| 8 | 62 |  | No | 75.75 |
| 9 | 68 | 67 | No | 27.98 |
| 10 | 54 | 67 | No | 26.59 |
| 11 | 62 |  | No | 56.71 |
| 12 | 59 | 67 | No | 22.39 |
| 13 | 40 |  | No | 59.41 |
| 14 | 43 | 67 | No | 16.99 |
| 15 | 59 |  | No | 64.07 |
| 16 | 63 | 67 | No | 16.54 |
| 17 | 72 |  | No | 65.42 |
| 18 | 66 | 67 | No | 18.25 |
| 19 | 62 | 67 | No | 18.79 |
| 20 | 74 | 67 | No | 31.32 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XEJGOKI | XEJGOKI | Yes | 13.76 |
| 2 | PAKYDXG | PAKYDXG | Yes | 10.34 |
| 3 | MWVFIXU | MWVFIXU | Yes | 9.7 |
| 4 | QCKRXPL | QCKRXPL | Yes | 8.42 |
| 5 | NQDBGAV | NQDBGAV | Yes | 15.67 |
| 6 | PKFTDCL | PKFTDCL | Yes | 23.21 |
| 7 | AXWRVPY | AXWRVPY | Yes | 10.83 |
| 8 | TZWURMH | TZWURMH | Yes | 10.09 |
| 9 | ZIQVJET | ZIQVJET | Yes | 5.99 |
| 10 | CGFOQNK | CGFOQNK | Yes | 11.09 |
| 11 | EYUDTJS | EYUDTJS | Yes | 22.54 |
| 12 | KIZUFGL | KIZUFGL | Yes | 10.48 |
| 13 | XFDYILW | XFDYILW | Yes | 8.8 |
| 14 | AVGLBYO | AVGLBYO | Yes | 16.66 |
| 15 | BNWYHSJ | BNWYHSJ | Yes | 15.73 |
| 16 | PESUIDW | PESUIDW | Yes | 18.75 |
| 17 | FYJZTXB | FYJZTXB | Yes | 9.97 |
| 18 | SOATYDB |  | No | 59.19 |
| 19 | PIZQWCB | PIZQWCB | Yes | 9.08 |
| 20 | UPICLKX | UPICLKX | Yes | 17.04 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.2, 5.8] | 4.2 5.8 | Yes | 11.93 |
| 2 | [1.6, 8.4] | 8.4 1.6 | Yes | 15.81 |
| 3 | [4.4, 5.6] | 5.6 4.4 | Yes | 18.56 |
| 4 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.71 |
| 5 | [1.2, 8.8] | 8.8 1.2 | Yes | 10.44 |
| 6 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.62 |
| 7 | [5.0, 5.0] | 5.0 5.0 | Yes | 14.26 |
| 8 | [1.4, 8.6] | 1.4 8.6 | Yes | 13.95 |
| 9 | [4.1, 5.9] | 4.1 5.9 | Yes | 12.82 |
| 10 | [0.8, 9.2] | 0.8 9.2 | Yes | 10.34 |
| 11 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.0 |
| 12 | [4.0, 6.0] | 4.0 6.0 | Yes | 10.21 |
| 13 | [1.5, 8.5] | 1.5 8.5 | Yes | 9.47 |
| 14 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.47 |
| 15 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.92 |
| 16 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.48 |
| 17 | [2.2, 7.8] | 2.2 7.8 | Yes | 12.78 |
| 18 | [0.3, 9.7] | 9.7 0.3 | Yes | 9.45 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 12.25 |
| 20 | [4.0, 6.0] | 4.0 6.0 | Yes | 14.61 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 22HF72BHB2B2 | 22HF72BHB2B2 | Yes | 16.51 |
| 2 | RN43K6RZ7OKP | RN43K6RZ7OKP | Yes | 18.84 |
| 3 | JDD6JNOZJ79V |  | No | 75.65 |
| 4 | DN83O5CGKNBG | DN8305CGKNBG | No | 8.21 |
| 5 | N5IST4DJZA44 | N5IST4DJZA44 | Yes | 5.26 |
| 6 | WLFVLSTE3S0K | WLFVLSTE3S0K | Yes | 23.67 |
| 7 | OBT3YDUVYR2W | OBT3YDUVYR2W | Yes | 30.83 |
| 8 | MRJEES22TIVX | MRJEES22TIVX | Yes | 10.67 |
| 9 | GEOE4DWDTA1A | GEOE4DWDTA1A | Yes | 7.37 |
| 10 | 0ZP73U2L5O4O |  | No | 74.39 |
| 11 | E66WLG2CE5J3 | E66WLG2CE5J3 | Yes | 6.83 |
| 12 | R6U6GDOR8C12 | R6U6GD0R8C12 | No | 24.36 |
| 13 | JU7LEG3L7FCC | JU7LEG3L7FCC | Yes | 22.58 |
| 14 | 1WGEVCUAQVIE | 1WGEVCUAQVIE | Yes | 16.15 |
| 15 | J6EII73FUI2K |  | No | 60.62 |
| 16 | NT9VJZJG2SNL | NT9VJZJG2SNL | Yes | 9.7 |
| 17 | GTF2FS35TLBN | GTF2FS35TLBN | Yes | 10.14 |
| 18 | UGCB9QV0RGE5 | UGCB9QV0RGE5 | Yes | 19.31 |
| 19 | 35WQI6785F4M | 35WQI6785F4M | Yes | 7.34 |
| 20 | MBKETIFV6GZA | MBKETIFV6GZA | Yes | 7.01 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 73 | Yes | 8.89 |
| 2 | 243 | 42 | No | 6.78 |
| 3 | 1 | 1 | Yes | 17.37 |
| 4 | 3 |  | No | 76.44 |
| 5 | 4 | 4 | Yes | 5.82 |
| 6 | 28 | 42 | No | 16.55 |
| 7 | 6 | 6 | Yes | 8.26 |
| 8 | 793 | 793 | Yes | 6.97 |
| 9 | 4096 |  | No | 60.35 |
| 10 | 48 | 42 | No | 11.16 |
| 11 | 26 | 42 | No | 23.67 |
| 12 | 9 | 42 | No | 7.23 |
| 13 | 63 | 63 | Yes | 19.32 |
| 14 | 7 | 7 | Yes | 16.35 |
| 15 | 10 | 42 | No | 3.73 |
| 16 | 60 | 42 | No | 6.12 |
| 17 | 16 | 16 | Yes | 11.28 |
| 18 | 36 | 42 | No | 6.51 |
| 19 | 60 | 60 | Yes | 10.81 |
| 20 | 3 | 3 | Yes | 12.87 |
