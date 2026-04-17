# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-27 10:05:40

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
| sudoku_game | 5186 | 32736 | 37922 | 12 | 8 | 18.03 | 360.6 |
| add_numbers | 2900 | 962 | 3862 | 20 | 0 | 3.38 | 67.67 |
| counting_zeros | 4300 | 16541 | 20841 | 18 | 2 | 7.69 | 153.75 |
| task_decoding | 4240 | 2552 | 6792 | 20 | 0 | 3.96 | 79.1 |
| task_summation | 4585 | 6395 | 10980 | 20 | 0 | 5.30 | 105.95 |
| task_transcription | 3037 | 2117 | 5154 | 20 | 0 | 3.23 | 64.64 |
| task_sequences | 2900 | 7819 | 10719 | 16 | 4 | 7.64 | 152.83 |
| string_entry | 3334 | 28172 | 31506 | 10 | 10 | 20.35 | 407.0 |
| **TOTAL** | **30482** | **97294** | **127776** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 6 1 4 5 4 3 2 5 1 6 4 4 | 1 5 6 1 4 5 4 3 2 5 1 6 4 4 | Yes | 11.56 |
| 2 | 4 1 3 3 6 6 1 1 4 3 1 3 6 4 |  | No | 22.2 |
| 3 | 3 6 4 4 2 4 6 5 1 6 2 5 2 4 |  | No | 37.97 |
| 4 | 2 3 1 6 2 1 3 5 6 1 3 2 3 6 | 2 3 1 6 2 1 3 5 6 1 3 2 3 6 | Yes | 13.26 |
| 5 | 5 4 2 4 3 2 2 1 3 4 6 5 1 1 | 5 4 2 4 3 2 2 1 3 4 6 5 1 1 | Yes | 18.58 |
| 6 | 6 3 1 4 4 2 5 6 2 3 6 4 1 3 |  | No | 21.13 |
| 7 | 5 3 6 4 5 2 3 4 3 2 3 5 2 4 |  | No | 31.02 |
| 8 | 3 6 1 3 4 5 6 1 6 1 2 5 2 5 | 3 6 1 3 4 5 6 1 6 1 2 5 2 5 | Yes | 15.45 |
| 9 | 6 2 4 1 2 4 2 3 3 4 6 6 3 1 | 6 2 4 1 2 4 2 3 3 4 6 6 3 1 | Yes | 10.01 |
| 10 | 4 5 6 6 5 1 4 1 4 3 5 1 2 4 | 4 5 6 6 5 1 4 1 4 3 5 1 2 4 | Yes | 20.1 |
| 11 | 6 5 1 5 2 3 2 2 5 3 2 6 1 4 | 6 5 1 5 2 3 2 2 5 3 2 6 1 4 | Yes | 8.7 |
| 12 | 5 3 6 2 4 1 3 5 5 3 5 3 6 2 | 5 3 6 2 4 1 3 5 5 3 5 3 6 2 | Yes | 11.92 |
| 13 | 1 6 3 4 5 2 3 6 3 1 1 6 2 5 | 1 6 3 4 5 2 3 6 3 1 1 6 2 5 | Yes | 13.65 |
| 14 | 5 4 6 5 6 4 6 5 6 4 2 5 5 6 |  | No | 21.63 |
| 15 | 3 6 1 5 1 3 5 4 1 5 4 4 2 1 | 3 6 1 5 1 3 5 4 1 5 4 4 2 1 | Yes | 13.22 |
| 16 | 4 5 2 3 4 6 5 2 1 5 6 2 4 3 |  | No | 24.96 |
| 17 | 4 5 6 4 5 6 1 4 1 2 5 4 1 2 | 4 5 6 4 5 6 1 4 1 2 5 4 1 2 | Yes | 10.88 |
| 18 | 2 6 3 2 6 5 4 4 5 3 5 4 1 6 |  | No | 15.16 |
| 19 | 6 5 5 3 4 5 1 6 4 3 2 4 6 5 | 6 5 5 3 4 5 1 6 4 3 2 4 6 5 | Yes | 13.68 |
| 20 | 4 2 3 5 6 5 3 2 1 5 2 4 2 1 |  | No | 25.47 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2217 | 2217 | Yes | 3.34 |
| 2 | 2603 | 2603 | Yes | 4.39 |
| 3 | 1010 | 1010 | Yes | 3.31 |
| 4 | 1551 | 1551 | Yes | 3.3 |
| 5 | 1449 | 1449 | Yes | 3.35 |
| 6 | 1676 | 1676 | Yes | 3.26 |
| 7 | 1194 | 1194 | Yes | 3.53 |
| 8 | 1958 | 1958 | Yes | 3.32 |
| 9 | 1956 | 1956 | Yes | 3.08 |
| 10 | 2503 | 2503 | Yes | 2.78 |
| 11 | 1607 | 1607 | Yes | 3.13 |
| 12 | 1281 | 1281 | Yes | 3.6 |
| 13 | 1953 | 1953 | Yes | 2.24 |
| 14 | 2185 | 2185 | Yes | 2.97 |
| 15 | 1508 | 1508 | Yes | 3.4 |
| 16 | 2067 | 2067 | Yes | 4.09 |
| 17 | 1372 | 1372 | Yes | 2.91 |
| 18 | 1604 | 1604 | Yes | 3.14 |
| 19 | 1786 | 1786 | Yes | 4.28 |
| 20 | 817 | 817 | Yes | 4.23 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 54 | Yes | 9.46 |
| 2 | 54 | 54 | Yes | 4.52 |
| 3 | 72 | 72 | Yes | 7.27 |
| 4 | 55 | 55 | Yes | 8.21 |
| 5 | 63 | 63 | Yes | 8.73 |
| 6 | 73 | 73 | Yes | 13.01 |
| 7 | 46 | 46 | Yes | 7.22 |
| 8 | 42 | 42 | Yes | 9.25 |
| 9 | 47 | 47 | Yes | 3.75 |
| 10 | 49 | 49 | Yes | 5.48 |
| 11 | 70 | 70 | Yes | 6.66 |
| 12 | 42 | 42 | Yes | 10.33 |
| 13 | 41 | 42 | No | 9.27 |
| 14 | 74 | 74 | Yes | 8.88 |
| 15 | 59 | 59 | Yes | 4.79 |
| 16 | 43 | 43 | Yes | 8.4 |
| 17 | 38 | 38 | Yes | 9.79 |
| 18 | 72 | 71 | No | 6.44 |
| 19 | 58 | 58 | Yes | 7.35 |
| 20 | 37 | 37 | Yes | 4.91 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MIPNXSY | MIPNXSY | Yes | 5.03 |
| 2 | KBGTIYN | KBGTIYN | Yes | 1.64 |
| 3 | EXFVILC | EXFVILC | Yes | 2.76 |
| 4 | ZCNWUDM | ZCNWUDM | Yes | 5.28 |
| 5 | ZJDYXKO | ZJDYXKO | Yes | 6.2 |
| 6 | DQRFIKG | DQRFIKG | Yes | 4.74 |
| 7 | DTZQGBN | DTZQGBN | Yes | 1.45 |
| 8 | HMZQPCG | HMZQPCG | Yes | 1.75 |
| 9 | XAGPRCZ | XAGPRCZ | Yes | 3.3 |
| 10 | AYWBHGK | AYWBHGK | Yes | 3.8 |
| 11 | CTXZYOG | CTXZYOG | Yes | 5.05 |
| 12 | RQJZVDW | RQJZVDW | Yes | 5.29 |
| 13 | PMHYTEG | PMHYTEG | Yes | 4.66 |
| 14 | GHUZIYP | GHUZIYP | Yes | 4.06 |
| 15 | SHLWDME | SHLWDME | Yes | 4.03 |
| 16 | RVNPLGM | RVNPLGM | Yes | 4.0 |
| 17 | VHMUBQD | VHMUBQD | Yes | 3.73 |
| 18 | VTEMWJU | VTEMWJU | Yes | 4.49 |
| 19 | JLDOTXF | JLDOTXF | Yes | 4.32 |
| 20 | ADUVBMF | ADUVBMF | Yes | 3.53 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 9.5 0.5 | Yes | 6.32 |
| 2 | [4.5, 5.5] | 5.5 4.5 | Yes | 6.45 |
| 3 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.5 |
| 4 | [2.3, 7.7] | 7.7 2.3 | Yes | 4.58 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.5 |
| 6 | [0.6, 9.4] | 0.6 9.4 | Yes | 7.43 |
| 7 | [0.9, 9.1] | 9.1 0.9 | Yes | 4.42 |
| 8 | [2.0, 8.0] | 2.0 8.0 | Yes | 3.67 |
| 9 | [0.1, 9.9] | 0.1 9.9 | Yes | 4.9 |
| 10 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.26 |
| 11 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.36 |
| 12 | [4.7, 5.3] | 5.3 4.7 | Yes | 6.26 |
| 13 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.14 |
| 14 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.74 |
| 15 | [2.4, 7.6] | 2.4 7.6 | Yes | 6.09 |
| 16 | [2.2, 7.8] | 2.2 7.8 | Yes | 5.47 |
| 17 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.71 |
| 18 | [0.5, 9.5] | 0.5 9.5 | Yes | 4.83 |
| 19 | [0.2, 9.8] | 9.8 0.2 | Yes | 5.67 |
| 20 | [2.7, 7.3] | 2.7 7.3 | Yes | 4.66 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | V81WECTWCM0K | V81WECTWCM0K | Yes | 3.31 |
| 2 | 6VD5JFKSHOMK | 6VD5JFKSHOMK | Yes | 1.94 |
| 3 | ODYIK3W8C5ME | ODYIK3W8C5ME | Yes | 4.11 |
| 4 | YOGT09854YLI | YOGT09854YLI | Yes | 4.18 |
| 5 | JPPALBZ2UDN4 | JPPALBZ2UDN4 | Yes | 4.47 |
| 6 | 7Z1P6BMJLMWP | 7Z1P6BMJLMWP | Yes | 4.2 |
| 7 | APB14ZIUKBNF | APB14ZIUKBNF | Yes | 2.71 |
| 8 | OGSW5SJ8GVN4 | OGSW5SJ8GVN4 | Yes | 4.65 |
| 9 | MGPEJ0P624KM | MGPEJ0P624KM | Yes | 4.79 |
| 10 | 989IDW0CF8H2 | 989IDW0CF8H2 | Yes | 3.96 |
| 11 | FKISZKRGL5PC | FKISZKRGL5PC | Yes | 1.82 |
| 12 | 0L3584YNOQXU | 0L3584YNOQXU | Yes | 3.4 |
| 13 | B9C14AMASDRJ | B9C14AMASDRJ | Yes | 3.15 |
| 14 | ROHENU656865 | ROHENU656865 | Yes | 2.17 |
| 15 | UVFN4NM5AKGB | UVFN4NM5AKGB | Yes | 1.47 |
| 16 | 9WVS16YV84JY | 9WVS16YV84JY | Yes | 1.22 |
| 17 | OZA7TVXRC9M7 | OZA7TVXRC9M7 | Yes | 5.12 |
| 18 | 61MLKJMN9EEA | 61MLKJMN9EEA | Yes | 3.35 |
| 19 | BHW3RSY3QFY1 | BHW3RSY3QFY1 | Yes | 2.88 |
| 20 | ZXOHVJPHLHE3 | ZXOHVJPHLHE3 | Yes | 1.75 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 3.62 |
| 2 | 5 |  | No | 26.72 |
| 3 | 63 | 63 | Yes | 3.17 |
| 4 | 10 | 8 | No | 4.28 |
| 5 | 28 | 28 | Yes | 3.58 |
| 6 | 793 | 793 | Yes | 2.93 |
| 7 | 23 | 23 | Yes | 3.76 |
| 8 | 9 | 9 | Yes | 4.06 |
| 9 | 67 | 67 | Yes | 3.7 |
| 10 | 44 | 44 | Yes | 3.26 |
| 11 | 26 |  | No | 35.51 |
| 12 | 64 | 64 | Yes | 5.55 |
| 13 | 60 | 60 | Yes | 3.29 |
| 14 | 1440 | 1440 | Yes | 3.89 |
| 15 | 9 | 9 | Yes | 4.42 |
| 16 | 3 | 3 | Yes | 3.98 |
| 17 | 20 |  | No | 25.05 |
| 18 | 198 | 198 | Yes | 4.36 |
| 19 | 7 | 7 | Yes | 3.92 |
| 20 | 73 | 73 | Yes | 3.77 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /)</_(/ \ |  | No | 22.2 |
| 2 | \< /_/\_  |  | No | 37.59 |
| 3 | _<)<(//<_ |  | No | 20.74 |
| 4 | <)_ )(_ ( |  | No | 40.27 |
| 5 | _/(_\ <<\ | _/(_\ <<\ | Yes | 23.55 |
| 6 |  (( _(<)_ |  | No | 22.27 |
| 7 | ( ((_<(<\ |  | No | 28.87 |
| 8 | (_)\ <)<\ |  | No | 44.89 |
| 9 | <\/_\ <<< | <\/_\ <<< | Yes | 15.34 |
| 10 | ))\ <(_(< | ))\ <(_(< | Yes | 6.29 |
| 11 | __\)((<(\ | __\)((<(\ | Yes | 20.04 |
| 12 | ((_ /_(\/ |  | No | 30.23 |
| 13 | )) /\()// | )) /\()// | Yes | 8.19 |
| 14 | ))_  /_/\ | ))_  /_/\ | Yes | 14.4 |
| 15 | </\<)< /( | </\<)< /( | Yes | 13.1 |
| 16 | /)\(\\ /) | /)\(\\ /) | Yes | 9.42 |
| 17 |  __ _ )\_ | __ _ )\_ | No | 10.54 |
| 18 | /)((_(</( | /)((_(</( | Yes | 17.65 |
| 19 | ) <((\)_/ | ) <((\)_/ | Yes | 6.12 |
| 20 | )<)(_)/\/ | /\) <(_<) | No | 15.29 |
