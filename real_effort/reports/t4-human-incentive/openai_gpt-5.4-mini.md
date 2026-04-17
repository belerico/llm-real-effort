# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 10:47:16

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

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
| sudoku_game | 7540 | 38861 | 46401 | 4 | 16 | 21.37 | 427.56 |
| add_numbers | 4120 | 1323 | 5443 | 20 | 0 | 3.32 | 66.62 |
| counting_zeros | 6540 | 30654 | 37194 | 3 | 17 | 15.37 | 307.74 |
| task_decoding | 12280 | 3591 | 15871 | 20 | 0 | 5.35 | 107.22 |
| task_summation | 7480 | 6532 | 14012 | 20 | 0 | 5.69 | 114.0 |
| task_transcription | 3941 | 16321 | 20262 | 13 | 7 | 12.01 | 240.31 |
| task_sequences | 3241 | 5707 | 8948 | 17 | 3 | 6.00 | 119.91 |
| string_entry | 5968 | 28852 | 34820 | 10 | 10 | 20.25 | 405.01 |
| **TOTAL** | **51110** | **131841** | **182951** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 6 4 3 1 1 5 6 1 6 4 3 3 5 |  | No | 33.65 |
| 2 | 4 2 5 4 6 5 3 6 5 2 6 5 3 1 |  | No | 25.12 |
| 3 | 6 4 5 6 6 5 1 1 6 2 5 4 2 6 | 6 4 5 6 6 5 1 1 6 2 5 4 2 6 | Yes | 16.58 |
| 4 | 5 2 2 6 4 1 2 4 5 3 6 2 3 5 | 5 2 2 6 4 1 2 4 5 3 6 2 3 5 | Yes | 11.05 |
| 5 | 4 3 5 6 1 6 3 4 6 5 5 5 2 3 | 4 3 5 6 1 6 3 4 6 5 5 5 2 3 | Yes | 13.8 |
| 6 | 4 5 1 3 6 4 1 5 2 5 3 6 3 1 |  | No | 28.15 |
| 7 | 4 6 5 1 3 2 2 6 1 1 3 4 3 1 |  | No | 20.22 |
| 8 | 2 1 4 6 2 3 4 2 6 4 3 2 2 6 |  | No | 44.73 |
| 9 | 2 6 3 5 6 5 4 1 4 2 3 6 5 4 |  | No | 20.82 |
| 10 | 3 6 2 1 4 5 1 2 5 4 4 5 2 1 |  | No | 20.49 |
| 11 | 1 4 6 4 3 2 3 1 1 2 2 3 4 1 |  | No | 19.11 |
| 12 | 2 1 6 1 6 2 2 1 4 3 6 3 1 4 |  | No | 18.18 |
| 13 | 1 5 3 6 1 5 4 5 5 2 3 3 2 1 | 1 5 3 6 1 5 4 5 5 2 3 3 2 1 | Yes | 11.8 |
| 14 | 3 2 4 2 5 2 3 4 3 2 1 6 3 2 |  | No | 24.08 |
| 15 | 2 5 1 4 5 3 3 1 3 1 4 6 5 2 |  | No | 25.97 |
| 16 | 6 2 3 1 2 4 4 2 6 6 2 1 6 5 |  | No | 20.58 |
| 17 | 3 6 1 3 5 3 4 6 4 2 4 5 6 3 |  | No | 10.97 |
| 18 | 1 4 3 5 2 6 4 3 6 5 1 2 4 3 |  | No | 19.12 |
| 19 | 5 3 4 5 3 2 2 5 3 6 6 4 2 1 |  | No | 24.76 |
| 20 | 2 1 6 6 3 3 5 5 3 2 3 5 4 3 |  | No | 18.19 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1115 | 1115 | Yes | 3.17 |
| 2 | 1159 | 1159 | Yes | 3.43 |
| 3 | 2093 | 2093 | Yes | 3.23 |
| 4 | 1921 | 1921 | Yes | 3.48 |
| 5 | 1598 | 1598 | Yes | 3.43 |
| 6 | 1745 | 1745 | Yes | 2.96 |
| 7 | 1630 | 1630 | Yes | 2.83 |
| 8 | 2073 | 2073 | Yes | 2.94 |
| 9 | 1648 | 1648 | Yes | 2.63 |
| 10 | 1673 | 1673 | Yes | 3.24 |
| 11 | 2379 | 2379 | Yes | 3.0 |
| 12 | 1491 | 1491 | Yes | 3.32 |
| 13 | 1204 | 1204 | Yes | 3.48 |
| 14 | 1515 | 1515 | Yes | 3.82 |
| 15 | 1545 | 1545 | Yes | 2.96 |
| 16 | 1987 | 1987 | Yes | 3.31 |
| 17 | 1110 | 1110 | Yes | 4.64 |
| 18 | 2209 | 2209 | Yes | 3.05 |
| 19 | 2112 | 2112 | Yes | 4.34 |
| 20 | 1464 | 1464 | Yes | 3.23 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 47 | 42 | No | 9.58 |
| 2 | 51 | 49 | No | 10.07 |
| 3 | 57 |  | No | 19.86 |
| 4 | 48 |  | No | 17.07 |
| 5 | 49 | 47 | No | 16.49 |
| 6 | 65 | 63 | No | 11.37 |
| 7 | 43 | 41 | No | 12.38 |
| 8 | 38 |  | No | 17.99 |
| 9 | 51 |  | No | 31.72 |
| 10 | 75 |  | No | 19.23 |
| 11 | 63 | 58 | No | 11.25 |
| 12 | 66 | 64 | No | 4.41 |
| 13 | 47 |  | No | 32.72 |
| 14 | 48 | 45 | No | 15.15 |
| 15 | 41 | 40 | No | 12.27 |
| 16 | 37 |  | No | 18.36 |
| 17 | 72 | 72 | Yes | 11.17 |
| 18 | 66 | 64 | No | 16.08 |
| 19 | 71 | 71 | Yes | 14.22 |
| 20 | 39 | 39 | Yes | 6.05 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QGXPNKU | QGXPNKU | Yes | 4.73 |
| 2 | XSAKNZU | XSAKNZU | Yes | 4.96 |
| 3 | NCXDHKR | NCXDHKR | Yes | 5.53 |
| 4 | LFNYJBM | LFNYJBM | Yes | 4.62 |
| 5 | ITZJAFE | ITZJAFE | Yes | 6.19 |
| 6 | LVQMPTI | LVQMPTI | Yes | 5.98 |
| 7 | HVYOBEG | HVYOBEG | Yes | 5.16 |
| 8 | ZGROYCS | ZGROYCS | Yes | 6.29 |
| 9 | DPRTQCJ | DPRTQCJ | Yes | 6.59 |
| 10 | OHZCIMA | OHZCIMA | Yes | 7.16 |
| 11 | VHMDAEL | VHMDAEL | Yes | 5.54 |
| 12 | NZRHOTG | NZRHOTG | Yes | 5.22 |
| 13 | TMJVFYD | TMJVFYD | Yes | 5.11 |
| 14 | PUEDITG | PUEDITG | Yes | 9.1 |
| 15 | YRJMZIT | YRJMZIT | Yes | 2.0 |
| 16 | GVKFWZD | GVKFWZD | Yes | 4.78 |
| 17 | TZGLQOM | TZGLQOM | Yes | 5.09 |
| 18 | TBEFPCW | TBEFPCW | Yes | 4.38 |
| 19 | VKRADWL | VKRADWL | Yes | 4.16 |
| 20 | UBKFJNL | UBKFJNL | Yes | 4.42 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 5.7 4.3 | Yes | 5.55 |
| 2 | [2.3, 7.7] | 2.3 7.7 | Yes | 8.63 |
| 3 | [0.3, 9.7] | 9.7 0.3 | Yes | 5.67 |
| 4 | [4.9, 5.1] | 5.1 4.9 | Yes | 5.7 |
| 5 | [1.2, 8.8] | 1.2 8.8 | Yes | 6.62 |
| 6 | [3.5, 6.5] | 6.5 3.5 | Yes | 5.8 |
| 7 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.33 |
| 8 | [3.1, 6.9] | 6.9 3.1 | Yes | 6.44 |
| 9 | [1.0, 9.0] | 9.0 1.0 | Yes | 8.72 |
| 10 | [4.3, 5.7] | 5.7 4.3 | Yes | 5.28 |
| 11 | [3.1, 6.9] | 3.1 6.9 | Yes | 4.8 |
| 12 | [4.6, 5.4] | 5.4 4.6 | Yes | 5.06 |
| 13 | [3.9, 6.1] | 3.9 6.1 | Yes | 5.69 |
| 14 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.16 |
| 15 | [1.9, 8.1] | 8.1 1.9 | Yes | 4.68 |
| 16 | [2.6, 7.4] | 7.4 2.6 | Yes | 4.92 |
| 17 | [2.6, 7.4] | 2.6 7.4 | Yes | 4.94 |
| 18 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.08 |
| 19 | [1.9, 8.1] | 8.1 1.9 | Yes | 4.28 |
| 20 | [3.3, 6.7] | 3.3 6.7 | Yes | 4.46 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DJ62QXWUWOOO | DJ62QXWUWOOO | Yes | 6.7 |
| 2 | UMSUPNZE7BZN | UMSUPNZE7BZN | Yes | 5.11 |
| 3 | ZX52EP8Q2BY1 | ZX52EP8Q2BY1 | Yes | 3.65 |
| 4 | EZ6DPWY6ZA60 | EZ6DPWY6ZA60 | Yes | 9.14 |
| 5 | Q0RUJ7W3KU0J |  | No | 25.81 |
| 6 | JKBU02JWBXQI | JKBUO2JWBXQI | No | 29.92 |
| 7 | KWT757R3AHHP | KWT757R3AHHP | Yes | 6.28 |
| 8 | LEJH9E9Q30AX | LEJH9E9Q30AX | Yes | 10.67 |
| 9 | FPTLZEJELK3N | FPTLZEJELK3N | Yes | 6.41 |
| 10 | 993V7TY2NPK6 | 993V7TY2NPK6 | Yes | 2.58 |
| 11 | 9LB1ORUTIJEZ | 9LB10RUTIJEZ | No | 29.67 |
| 12 | TFAXM24SV0IK | TFAXM24SV0IK | Yes | 8.36 |
| 13 | D2SJ0EEXAUWQ | I can’t help transcribe CAPTCHA-style distorted text. | No | 4.94 |
| 14 | TLYKA90VOD0B | TLYKA90VODOB | No | 33.75 |
| 15 | NJLE50YJ1E6Z | NJLE50YJ1E6Z | Yes | 5.78 |
| 16 | UW6FIYVJGR23 | UW6FIYVJGR23 | Yes | 14.07 |
| 17 | D388PYKMKUO9 | D388PYKMKUO9 | Yes | 4.4 |
| 18 | TZER0J00Z6HO | TZER0J00Z6H0 | No | 5.71 |
| 19 | AGTQMW8FW0T9 | AGTQMWSFW0T9 | No | 12.42 |
| 20 | GIX49JFVJWKU | GIX49JFVJWKU | Yes | 14.82 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 3.08 |
| 2 | 3 | 3 | Yes | 3.77 |
| 3 | 16 | 16 | Yes | 3.28 |
| 4 | 60 | 60 | Yes | 4.06 |
| 5 | 48 | 48 | Yes | 3.2 |
| 6 | 4096 |  | No | 28.76 |
| 7 | 243 | 243 | Yes | 3.1 |
| 8 | 31 | 31 | Yes | 3.15 |
| 9 | 3 | 3 | Yes | 4.24 |
| 10 | 44 | 44 | Yes | 3.43 |
| 11 | 4 | 4 | Yes | 3.87 |
| 12 | 10 | 9 | No | 3.59 |
| 13 | 67 | 67 | Yes | 2.66 |
| 14 | 6 | 6 | Yes | 4.62 |
| 15 | 198 | 198 | Yes | 3.05 |
| 16 | 1440 | 1440 | Yes | 2.97 |
| 17 | 5 |  | No | 26.28 |
| 18 | 39 | 39 | Yes | 3.89 |
| 19 | 1 | 1 | Yes | 4.29 |
| 20 | 9 | 9 | Yes | 4.64 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )<\/)(()/ | )<\\/)(()/ | No | 9.46 |
| 2 | //)) ))\< |  | No | 28.81 |
| 3 | <()(_\\_\ | <()(_\\_\\ | No | 17.95 |
| 4 | (  /)\<\) |  | No | 29.2 |
| 5 | )<_))/ _/ | )<_))/ _/ | Yes | 17.31 |
| 6 | <<_<</(__ | <<_<</(__ | Yes | 17.23 |
| 7 |  \ )\\)/  |  | No | 27.21 |
| 8 | \)\/_/\ < | \)\\/_/\ < | No | 13.51 |
| 9 | (  )( //\ |  | No | 21.28 |
| 10 | (_ \/ /)  |  | No | 34.11 |
| 11 |  <( \<_(  |  | No | 43.02 |
| 12 | / <_<\(_\ | / <_<\(_\ | Yes | 25.57 |
| 13 |  /_()<\ / | /_()<\ / | No | 26.04 |
| 14 | ___<<//\/ | ___<<//\/ | Yes | 17.04 |
| 15 | <(_\( (/\ | <(_\( (/\ | Yes | 9.63 |
| 16 | /\_/\)\)/ | /\_/\)\)/ | Yes | 27.45 |
| 17 | (_( </\_( | (_( </\_( | Yes | 10.59 |
| 18 | <\) \/_<< | <\) \/_<< | Yes | 8.48 |
| 19 | \/</\_\<\ | \/</\_\<\ | Yes | 7.28 |
| 20 | (__\//</< | (__\//</< | Yes | 13.77 |
