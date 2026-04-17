# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 10:47:39

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
| sudoku_game | 6720 | 31959 | 38679 | 11 | 9 | 19.58 | 391.76 |
| add_numbers | 3300 | 1767 | 5067 | 20 | 0 | 3.50 | 70.05 |
| counting_zeros | 5720 | 33916 | 39636 | 1 | 19 | 16.35 | 327.37 |
| task_decoding | 11460 | 3599 | 15059 | 19 | 1 | 4.85 | 97.28 |
| task_summation | 6660 | 6416 | 13076 | 20 | 0 | 5.72 | 114.6 |
| task_transcription | 3124 | 14670 | 17794 | 16 | 4 | 10.55 | 211.2 |
| task_sequences | 2420 | 8110 | 10530 | 17 | 3 | 7.72 | 154.45 |
| string_entry | 3720 | 32483 | 36203 | 6 | 14 | 25.10 | 501.97 |
| **TOTAL** | **43124** | **132920** | **176044** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 5 2 4 4 3 5 1 5 6 5 3 6 |  | No | 47.58 |
| 2 | 5 3 4 1 6 2 5 1 2 6 4 5 3 2 | 5 3 4 1 6 2 5 1 2 6 4 5 3 2 | Yes | 16.6 |
| 3 | 1 6 2 5 4 6 2 6 2 1 3 4 2 1 |  | No | 21.35 |
| 4 | 2 6 1 1 4 1 2 5 5 2 6 4 5 4 | 2 6 1 1 4 1 2 5 5 2 6 4 5 4 | Yes | 17.11 |
| 5 | 4 1 4 3 2 1 2 3 4 1 6 5 6 3 | 4 1 4 3 2 1 2 3 4 1 6 5 6 3 | Yes | 13.42 |
| 6 | 1 5 2 5 4 5 1 4 6 1 4 2 5 3 | 1 5 2 5 4 5 1 4 6 1 4 2 5 3 | Yes | 8.0 |
| 7 | 1 5 1 2 4 3 3 5 6 1 2 3 1 6 |  | No | 31.9 |
| 8 | 1 4 1 5 6 4 6 5 6 2 2 1 6 3 | 1 4 1 5 6 4 6 5 6 2 2 1 6 3 | Yes | 13.14 |
| 9 | 1 6 3 4 4 2 5 4 1 5 1 2 3 4 | 1 6 3 4 4 2 5 4 1 5 1 2 3 4 | Yes | 15.04 |
| 10 | 5 4 6 1 2 5 1 2 3 6 1 4 2 6 |  | No | 41.13 |
| 11 | 4 1 5 2 5 6 4 5 1 6 2 5 5 2 |  | No | 24.62 |
| 12 | 4 3 2 2 1 5 6 4 5 2 1 3 1 4 | 4 3 2 2 1 5 6 4 5 2 1 3 1 4 | Yes | 13.82 |
| 13 | 3 5 1 2 2 5 4 1 4 5 6 6 2 1 |  | No | 25.12 |
| 14 | 1 3 5 2 1 4 6 3 4 5 3 4 1 5 | 1 3 5 2 1 4 6 3 4 5 3 4 1 5 | Yes | 15.39 |
| 15 | 1 2 3 1 3 4 5 5 1 5 1 6 6 3 | 1 2 3 1 3 4 5 5 1 5 6 6 3 | No | 10.97 |
| 16 | 3 5 4 3 5 4 6 2 3 4 4 1 6 5 | 3 5 4 3 5 4 6 2 3 4 4 1 6 5 | Yes | 17.17 |
| 17 | 2 3 5 1 4 6 1 1 2 1 5 6 3 1 | 2 3 5 1 4 6 1 1 2 1 5 6 3 1 | Yes | 9.23 |
| 18 | 3 1 5 6 3 3 2 5 3 3 6 4 1 3 |  | No | 26.35 |
| 19 | 4 2 3 3 6 2 1 6 5 6 4 4 5 6 |  | No | 13.14 |
| 20 | 3 1 5 6 2 4 1 5 3 2 5 6 4 1 | 3 1 5 6 2 4 1 5 3 2 5 6 4 1 | Yes | 10.48 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2128 | 2128 | Yes | 2.9 |
| 2 | 1494 | 1494 | Yes | 4.69 |
| 3 | 1949 | 1949 | Yes | 3.52 |
| 4 | 1616 | 1616 | Yes | 3.15 |
| 5 | 1986 | 1986 | Yes | 3.33 |
| 6 | 1513 | 1513 | Yes | 4.73 |
| 7 | 1239 | 1239 | Yes | 2.84 |
| 8 | 1496 | 1496 | Yes | 3.44 |
| 9 | 1740 | 1740 | Yes | 3.02 |
| 10 | 1770 | 1770 | Yes | 3.93 |
| 11 | 2095 | 2095 | Yes | 3.05 |
| 12 | 1708 | 1708 | Yes | 3.2 |
| 13 | 1311 | 1311 | Yes | 3.44 |
| 14 | 566 | 566 | Yes | 3.33 |
| 15 | 2287 | 2287 | Yes | 4.08 |
| 16 | 1638 | 1638 | Yes | 3.13 |
| 17 | 1355 | 1355 | Yes | 2.81 |
| 18 | 2035 | 2035 | Yes | 4.81 |
| 19 | 2123 | 2123 | Yes | 3.58 |
| 20 | 1950 | 1950 | Yes | 2.98 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 56 | No | 10.25 |
| 2 | 69 | 67 | No | 16.29 |
| 3 | 64 |  | No | 18.32 |
| 4 | 56 |  | No | 27.74 |
| 5 | 75 |  | No | 16.99 |
| 6 | 58 |  | No | 16.64 |
| 7 | 68 | 67 | No | 15.62 |
| 8 | 72 | 70 | No | 11.93 |
| 9 | 40 |  | No | 24.82 |
| 10 | 63 |  | No | 21.76 |
| 11 | 65 |  | No | 25.33 |
| 12 | 43 | 43 | Yes | 5.44 |
| 13 | 37 |  | No | 22.61 |
| 14 | 59 | 60 | No | 8.84 |
| 15 | 49 | 51 | No | 5.08 |
| 16 | 56 | 55 | No | 7.97 |
| 17 | 63 |  | No | 13.33 |
| 18 | 41 |  | No | 18.08 |
| 19 | 42 |  | No | 24.57 |
| 20 | 66 |  | No | 15.44 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BXYKNUJ | BXYKNUJ | Yes | 5.64 |
| 2 | AWTXVRN | AWTXVRN | Yes | 7.14 |
| 3 | ZKPFNJX | ZKPFNJX | Yes | 4.69 |
| 4 | BYSQTEJ | BYSQTEJ | Yes | 4.07 |
| 5 | XIZLQKE | XIZLQKE | Yes | 4.39 |
| 6 | NWERTSK | NWERTSK | Yes | 5.41 |
| 7 | WSPHARJ | WSPHARJ | Yes | 4.06 |
| 8 | NDXCMYZ | NDXCMYZ | Yes | 4.01 |
| 9 | TOWNFQX | TOWNFQX | Yes | 3.34 |
| 10 | AWFDXYE | AWFDXYE | Yes | 4.91 |
| 11 | XGBULPR | XGBULPR | Yes | 5.48 |
| 12 | FKQYIZB | FKQYIZB | Yes | 5.0 |
| 13 | WVTHMPC | WVTHMPC | Yes | 4.87 |
| 14 | OAVSWED | OVASWED | No | 5.27 |
| 15 | PMJOILS | PMJOILS | Yes | 4.28 |
| 16 | GXTJKYI | GXTJKYI | Yes | 5.17 |
| 17 | LKHPAWO | LKHPAWO | Yes | 5.8 |
| 18 | HUTLEMN | HUTLEMN | Yes | 4.51 |
| 19 | ZIMCVYL | ZIMCVYL | Yes | 5.26 |
| 20 | LSRJOMD | LSRJOMD | Yes | 3.78 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.44 |
| 2 | [3.9, 6.1] | 3.9 6.1 | Yes | 6.59 |
| 3 | [0.5, 9.5] | 9.5 0.5 | Yes | 5.52 |
| 4 | [1.2, 8.8] | 8.8 1.2 | Yes | 5.12 |
| 5 | [1.0, 9.0] | 1.0 9.0 | Yes | 7.66 |
| 6 | [1.2, 8.8] | 1.2 8.8 | Yes | 7.96 |
| 7 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.87 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 4.36 |
| 9 | [4.1, 5.9] | 5.9 4.1 | Yes | 7.15 |
| 10 | [0.7, 9.3] | 0.7 9.3 | Yes | 5.45 |
| 11 | [1.5, 8.5] | 8.5 1.5 | Yes | 6.14 |
| 12 | [3.0, 7.0] | 3.0 7.0 | Yes | 5.06 |
| 13 | [4.6, 5.4] | 4.6 5.4 | Yes | 4.81 |
| 14 | [0.6, 9.4] | 9.4 0.6 | Yes | 4.73 |
| 15 | [3.9, 6.1] | 3.9 6.1 | Yes | 4.44 |
| 16 | [3.5, 6.5] | 3.5 6.5 | Yes | 4.78 |
| 17 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.84 |
| 18 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.76 |
| 19 | [2.1, 7.9] | 7.9 2.1 | Yes | 6.2 |
| 20 | [4.6, 5.4] | 5.4 4.6 | Yes | 4.54 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RH2GTLZTSHUQ | RH2GTLZTSHUQ | Yes | 5.13 |
| 2 | 0BJPJ6IJUY37 | 0BJPJ6IJUY37 | Yes | 18.07 |
| 3 | 2VOH11V3GXWS | 2VOH11V3GXWS | Yes | 7.94 |
| 4 | 9OUHUZQ058QV | 9OUHUZQ058QV | Yes | 8.42 |
| 5 | S9U2OX6CQOXY | S9U2OX6CQOXY | Yes | 16.16 |
| 6 | SFHXBGULNIV4 | SFHXBGULNIV4 | Yes | 8.56 |
| 7 | 7MWIUVI1BBMR |  | No | 32.34 |
| 8 | T4ACA915R98T | T4ACA915R98T | Yes | 4.15 |
| 9 | IUGGVJ3JTCXJ | IUGGVJ3JTCXJ | Yes | 5.69 |
| 10 | HYDY9ADT0V76 | HYDY9 | No | 23.87 |
| 11 | SUIC4OFVI6ZD | SUIC4OFVI6ZD | Yes | 7.18 |
| 12 | MWZOOV499TEM | MWZOOV499TEM | Yes | 14.71 |
| 13 | 6ARAOB1UFGWY | 6ARAOB1UFGWY | Yes | 8.01 |
| 14 | ZFCOJH0192FN | ZFCOJH0192FN | Yes | 4.41 |
| 15 | DJ65G7F0717Z | DJ65G7F0717Z | Yes | 7.72 |
| 16 | 7GUW5DAZW3XY | 7GUW5DAZW3XY | Yes | 2.52 |
| 17 | 293Y4DGG5EC1 | 293Y4DGG5EC1 | Yes | 4.05 |
| 18 | VFZRYC0M9PZC | VFZRYCOM9PZC | No | 7.43 |
| 19 | XLA1ODI2MDZ5 |  | No | 20.33 |
| 20 | 2FD7T6Z79E9J | 2FD7T6Z79E9J | Yes | 4.4 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 3.4 |
| 2 | 60 | 60 | Yes | 3.25 |
| 3 | 26 |  | No | 28.97 |
| 4 | 48 | 48 | Yes | 4.92 |
| 5 | 28 | 28 | Yes | 4.01 |
| 6 | 36 | 36 | Yes | 3.24 |
| 7 | 793 | 793 | Yes | 3.55 |
| 8 | 39 | 39 | Yes | 3.18 |
| 9 | 5 |  | No | 26.57 |
| 10 | 64 | 64 | Yes | 5.58 |
| 11 | 243 | 243 | Yes | 2.8 |
| 12 | 3 | 3 | Yes | 7.82 |
| 13 | 5 | 5 | Yes | 3.89 |
| 14 | 73 | 73 | Yes | 3.42 |
| 15 | 198 | 198 | Yes | 2.8 |
| 16 | 10 |  | No | 32.75 |
| 17 | 67 | 67 | Yes | 3.12 |
| 18 | 1 | 1 | Yes | 3.97 |
| 19 | 7 | 7 | Yes | 3.85 |
| 20 | 63 | 63 | Yes | 3.38 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \<((\_ <  |  | No | 24.35 |
| 2 | )_(\\</   |  | No | 33.68 |
| 3 | //\/_<\/\ |  | No | 36.44 |
| 4 | <))(/<<)  |  | No | 39.34 |
| 5 | ( (/\ \_\ |  | No | 28.93 |
| 6 | \__/)(_ ) | \__/)(_ ) | Yes | 16.07 |
| 7 | _//)(((/< | _//)(((/< | Yes | 22.71 |
| 8 | /< //(<)\ |  | No | 31.51 |
| 9 | ( \ __/(  | ( \ __/( | No | 10.82 |
| 10 | /()()/<\) | /()()/<\) | Yes | 14.16 |
| 11 | \_<)\<<<) |  | No | 23.7 |
| 12 |   )\ //__ |  | No | 37.87 |
| 13 | )\))(<_<_ |  | No | 35.87 |
| 14 | )/\ \()\) | )/\ \()\) | Yes | 12.91 |
| 15 | _())  _\) |  | No | 25.76 |
| 16 | \_ <\_)_/ | \_ <\_)_/ | Yes | 8.55 |
| 17 | /\(\\_ << |  | No | 37.56 |
| 18 | _\/)) )\( | _\/)) )\( | Yes | 8.21 |
| 19 | ) <_/_/(< |  | No | 30.94 |
| 20 |  _<( <<\) | _<( <<\) | No | 22.53 |
