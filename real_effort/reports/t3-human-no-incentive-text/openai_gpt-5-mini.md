# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-27 10:45:29

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
| sudoku_game | 5306 | 40960 | 46266 | 0 | 20 | 66.94 | 1338.87 |
| add_numbers | 3060 | 4261 | 7321 | 20 | 0 | 6.74 | 134.8 |
| counting_zeros | 4460 | 37232 | 41692 | 8 | 12 | 36.59 | 731.89 |
| task_decoding | 4400 | 8678 | 13078 | 20 | 0 | 7.57 | 151.45 |
| task_summation | 4740 | 12727 | 17467 | 20 | 0 | 11.24 | 224.92 |
| task_transcription | 3207 | 4989 | 8196 | 20 | 0 | 4.99 | 99.86 |
| task_sequences | 3061 | 23421 | 26482 | 12 | 8 | 18.64 | 372.82 |
| string_entry | 3493 | 37780 | 41273 | 3 | 17 | 35.58 | 711.69 |
| **TOTAL** | **31727** | **170048** | **201775** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 3 6 2 1 5 2 5 3 5 6 2 4 |  | No | 73.24 |
| 2 | 5 6 4 3 1 3 6 2 1 4 1 4 1 6 |  | No | 61.14 |
| 3 | 3 4 6 5 5 4 6 3 5 6 3 1 3 5 |  | No | 72.75 |
| 4 | 5 4 3 6 3 1 2 5 6 1 4 2 5 1 |  | No | 59.82 |
| 5 | 6 1 2 1 3 4 2 3 2 5 4 3 5 1 |  | No | 76.93 |
| 6 | 2 1 3 3 5 3 2 3 6 6 4 1 5 6 |  | No | 68.16 |
| 7 | 3 5 4 1 6 5 1 2 6 3 4 1 2 3 |  | No | 54.54 |
| 8 | 6 5 3 3 5 1 2 6 5 3 2 4 1 6 |  | No | 68.73 |
| 9 | 3 2 4 5 3 6 1 1 4 2 3 5 2 5 |  | No | 63.5 |
| 10 | 2 2 3 3 2 4 4 1 6 4 2 4 3 5 |  | No | 56.1 |
| 11 | 2 3 5 4 2 4 5 3 6 2 3 3 1 5 |  | No | 53.38 |
| 12 | 3 4 2 6 2 5 6 4 3 1 5 2 1 3 |  | No | 83.3 |
| 13 | 6 1 3 4 6 2 3 4 5 4 1 6 1 2 |  | No | 54.84 |
| 14 | 6 3 4 5 3 2 4 5 2 3 2 3 5 3 |  | No | 70.98 |
| 15 | 4 5 6 2 1 3 4 3 2 2 3 4 1 4 |  | No | 57.51 |
| 16 | 2 3 3 4 6 1 6 2 3 6 2 1 5 4 |  | No | 63.18 |
| 17 | 3 4 2 1 6 2 4 1 2 3 2 3 6 3 |  | No | 54.61 |
| 18 | 2 5 3 6 1 6 5 2 1 2 4 3 6 4 |  | No | 76.91 |
| 19 | 3 2 1 6 1 1 6 5 1 4 6 1 4 6 |  | No | 105.33 |
| 20 | 4 3 2 6 1 5 6 1 4 6 6 4 4 5 |  | No | 63.91 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1449 | 1449 | Yes | 11.29 |
| 2 | 1441 | 1441 | Yes | 7.15 |
| 3 | 865 | 865 | Yes | 4.45 |
| 4 | 1212 | 1212 | Yes | 4.6 |
| 5 | 2819 | 2819 | Yes | 7.38 |
| 6 | 1708 | 1708 | Yes | 5.1 |
| 7 | 1287 | 1287 | Yes | 8.47 |
| 8 | 1491 | 1491 | Yes | 3.44 |
| 9 | 1626 | 1626 | Yes | 4.27 |
| 10 | 2069 | 2069 | Yes | 7.85 |
| 11 | 1998 | 1998 | Yes | 5.16 |
| 12 | 1662 | 1662 | Yes | 8.23 |
| 13 | 2524 | 2524 | Yes | 9.0 |
| 14 | 1368 | 1368 | Yes | 8.22 |
| 15 | 1184 | 1184 | Yes | 7.83 |
| 16 | 2794 | 2794 | Yes | 6.25 |
| 17 | 1906 | 1906 | Yes | 6.32 |
| 18 | 1912 | 1912 | Yes | 6.62 |
| 19 | 1257 | 1257 | Yes | 3.75 |
| 20 | 1217 | 1217 | Yes | 9.42 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 69 |  | No | 70.27 |
| 2 | 59 |  | No | 61.16 |
| 3 | 49 |  | No | 49.79 |
| 4 | 39 | 39 | Yes | 22.05 |
| 5 | 56 |  | No | 43.96 |
| 6 | 70 |  | No | 47.38 |
| 7 | 63 |  | No | 41.96 |
| 8 | 54 |  | No | 37.12 |
| 9 | 61 |  | No | 37.43 |
| 10 | 67 | 67 | Yes | 11.8 |
| 11 | 71 |  | No | 43.3 |
| 12 | 75 |  | No | 44.86 |
| 13 | 44 | 44 | Yes | 19.94 |
| 14 | 35 | 35 | Yes | 21.37 |
| 15 | 48 | 48 | Yes | 14.16 |
| 16 | 70 |  | No | 44.32 |
| 17 | 53 | 53 | Yes | 19.73 |
| 18 | 57 | 57 | Yes | 27.29 |
| 19 | 64 |  | No | 49.59 |
| 20 | 53 | 53 | Yes | 24.38 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KSNJEPU | KSNJEPU | Yes | 8.2 |
| 2 | VWZRGML | VWZRGML | Yes | 14.43 |
| 3 | ZATVYQU | ZATVYQU | Yes | 4.95 |
| 4 | UIMGDXJ | UIMGDXJ | Yes | 4.25 |
| 5 | TUZEMAV | TUZEMAV | Yes | 6.08 |
| 6 | JMPKQOH | JMPKQOH | Yes | 6.25 |
| 7 | IFPCTAJ | IFPCTAJ | Yes | 9.26 |
| 8 | FDNBSJH | FDNBSJH | Yes | 14.64 |
| 9 | GYSDIUT | GYSDIUT | Yes | 3.96 |
| 10 | VOXRFJE | VOXRFJE | Yes | 13.6 |
| 11 | MSFWKXL | MSFWKXL | Yes | 2.57 |
| 12 | ERZOBNF | ERZOBNF | Yes | 4.25 |
| 13 | DYHNQMR | DYHNQMR | Yes | 4.57 |
| 14 | GFDHELY | GFDHELY | Yes | 6.53 |
| 15 | PWTRIGB | PWTRIGB | Yes | 5.39 |
| 16 | WZLHCEV | WZLHCEV | Yes | 7.57 |
| 17 | JSITRVZ | JSITRVZ | Yes | 11.61 |
| 18 | OMEGKCN | OMEGKCN | Yes | 11.2 |
| 19 | URZETAI | URZETAI | Yes | 6.88 |
| 20 | STQPHGO | STQPHGO | Yes | 5.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.0, 7.0] | 7.0 3.0 | Yes | 11.4 |
| 2 | [2.6, 7.4] | 7.4 2.6 | Yes | 10.41 |
| 3 | [0.8, 9.2] | 0.8 9.2 | Yes | 12.69 |
| 4 | [4.4, 5.6] | 5.6 4.4 | Yes | 13.81 |
| 5 | [3.9, 6.1] | 6.1 3.9 | Yes | 8.88 |
| 6 | [3.3, 6.7] | 3.3 6.7 | Yes | 13.86 |
| 7 | [1.0, 9.0] | 9.0 1.0 | Yes | 14.89 |
| 8 | [2.9, 7.1] | 2.9 7.1 | Yes | 15.43 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 7.88 |
| 10 | [4.0, 6.0] | 4.0 6.0 | Yes | 11.17 |
| 11 | [4.7, 5.3] | 4.7 5.3 | Yes | 13.9 |
| 12 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.93 |
| 13 | [4.3, 5.7] | 4.3 5.7 | Yes | 9.96 |
| 14 | [3.4, 6.6] | 6.6 3.4 | Yes | 10.63 |
| 15 | [4.8, 5.2] | 5.2 4.8 | Yes | 10.38 |
| 16 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.2 |
| 17 | [2.5, 7.5] | 7.5 2.5 | Yes | 14.96 |
| 18 | [1.6, 8.4] | 1.6 8.4 | Yes | 9.48 |
| 19 | [1.8, 8.2] | 8.2 1.8 | Yes | 8.53 |
| 20 | [2.1, 7.9] | 2.1 7.9 | Yes | 13.5 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7GUB1NBN84BC | 7GUB1NBN84BC | Yes | 2.58 |
| 2 | NOGU7PNQ55JC | NOGU7PNQ55JC | Yes | 3.47 |
| 3 | LU77CHG3J4CP | LU77CHG3J4CP | Yes | 6.36 |
| 4 | 6BUY8S9TC9P9 | 6BUY8S9TC9P9 | Yes | 2.97 |
| 5 | T29TO0JRHT8E | T29TO0JRHT8E | Yes | 5.61 |
| 6 | 5FXENXST0JMJ | 5FXENXST0JMJ | Yes | 3.8 |
| 7 | 3L81GOV5S9DF | 3L81GOV5S9DF | Yes | 4.42 |
| 8 | F9FSBEAKM9RY | F9FSBEAKM9RY | Yes | 8.05 |
| 9 | FE3D9DBPTQYB | FE3D9DBPTQYB | Yes | 7.51 |
| 10 | XYJH7B3NLAHK | XYJH7B3NLAHK | Yes | 2.33 |
| 11 | 35AWZZAHFGK8 | 35AWZZAHFGK8 | Yes | 10.94 |
| 12 | 3XRYHOBNOQ7G | 3XRYHOBNOQ7G | Yes | 3.83 |
| 13 | OWSU4HAAU1H5 | OWSU4HAAU1H5 | Yes | 3.13 |
| 14 | 0XKQ7B2MBGVN | 0XKQ7B2MBGVN | Yes | 6.46 |
| 15 | MMN510FKIN7M | MMN510FKIN7M | Yes | 6.11 |
| 16 | 3NZSVTOQ9NFD | 3NZSVTOQ9NFD | Yes | 3.36 |
| 17 | FI26BJUH3BC7 | FI26BJUH3BC7 | Yes | 6.54 |
| 18 | B41LZPRHX6S0 | B41LZPRHX6S0 | Yes | 2.88 |
| 19 | 5BWXKBKINP4C | 5BWXKBKINP4C | Yes | 5.48 |
| 20 | R9MWME0XGHYG | R9MWME0XGHYG | Yes | 4.04 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 12.09 |
| 2 | 65 | 65 | Yes | 21.5 |
| 3 | 6 | 6 | Yes | 20.71 |
| 4 | 7 | 7 | Yes | 14.7 |
| 5 | 10 |  | No | 49.48 |
| 6 | 60 | 60 | Yes | 18.37 |
| 7 | 36 | 42 | No | 5.83 |
| 8 | 793 | 793 | Yes | 18.15 |
| 9 | 64 | 64 | Yes | 19.87 |
| 10 | 44 | 42 | No | 8.95 |
| 11 | 9 | 42 | No | 4.94 |
| 12 | 4096 |  | No | 49.93 |
| 13 | 73 | 73 | Yes | 20.95 |
| 14 | 60 | 42 | No | 17.0 |
| 15 | 67 | 67 | Yes | 9.35 |
| 16 | 1440 | 42 | No | 22.87 |
| 17 | 19 | 19 | Yes | 19.7 |
| 18 | 23 | 23 | Yes | 9.53 |
| 19 | 28 | 28 | Yes | 12.27 |
| 20 | 63 | 42 | No | 16.6 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )_)</<(_< |  | No | 52.0 |
| 2 | ((<\(_)/< | /\) <(_<) | No | 23.21 |
| 3 |  ( ///) < | /\) <(_<) | No | 23.25 |
| 4 | (__()_<(_ |  | No | 51.64 |
| 5 | \//)(/\/\ | /\) <(_<) | No | 22.83 |
| 6 | <<__))(<\ |  | No | 24.6 |
| 7 | )__\ _(<_ |  | No | 57.01 |
| 8 | () _/<)(  | /\) <(_<) | No | 24.34 |
| 9 | \/__\\\/( |  | No | 48.82 |
| 10 |  (\))_  ( |  | No | 51.54 |
| 11 | <(<)<(((  |  | No | 48.19 |
| 12 | ) /((/(<< |  | No | 23.97 |
| 13 | \\/(<()<  |  | No | 50.74 |
| 14 | /<   _(<  | /<   _(< | No | 16.65 |
| 15 | /</<)/\\\ | /</<)/\\\ | Yes | 24.21 |
| 16 | ()<\)\    |  | No | 51.86 |
| 17 | / _)//<</ | / _)//<</ | Yes | 16.85 |
| 18 | <(_\\_)\\ |  | No | 39.22 |
| 19 | __ </</__ | __ </</__ | Yes | 20.89 |
| 20 | \/)/()_ ) |  | No | 39.86 |
