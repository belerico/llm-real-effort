# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-27 10:14:16

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
| sudoku_game | 5482 | 38359 | 43841 | 6 | 14 | 36.94 | 738.77 |
| add_numbers | 3240 | 709 | 3949 | 20 | 0 | 3.78 | 75.53 |
| counting_zeros | 4640 | 21233 | 25873 | 19 | 1 | 15.40 | 307.99 |
| task_decoding | 4580 | 3375 | 7955 | 20 | 0 | 5.38 | 107.54 |
| task_summation | 4920 | 6515 | 11435 | 20 | 0 | 6.77 | 135.3 |
| task_transcription | 3381 | 1890 | 5271 | 20 | 0 | 3.15 | 63.09 |
| task_sequences | 3241 | 8821 | 12062 | 19 | 1 | 8.91 | 178.23 |
| string_entry | 3683 | 25680 | 29363 | 4 | 16 | 13.68 | 273.51 |
| **TOTAL** | **33167** | **106582** | **139749** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 4 6 1 5 1 4 2 5 6 5 2 6 4 |  | No | 40.92 |
| 2 | 6 1 4 1 4 3 4 1 3 4 4 1 5 3 |  | No | 59.27 |
| 3 | 2 1 4 1 6 4 3 3 6 3 1 1 5 3 |  | No | 53.17 |
| 4 | 1 6 2 3 5 2 3 2 4 6 5 4 1 5 | 1 6 2 3 5 2 3 2 4 6 5 4 1 5 | Yes | 24.05 |
| 5 | 1 5 1 2 6 5 1 3 4 5 2 3 2 1 |  | No | 51.68 |
| 6 | 6 2 5 3 5 4 5 1 6 4 2 4 1 3 | 6 2 | No | 22.62 |
| 7 | 2 5 4 1 6 1 1 5 2 5 3 2 3 2 | 2 5 4 1 | No | 18.77 |
| 8 | 1 3 4 3 6 5 3 4 2 5 4 6 2 4 |  | No | 47.48 |
| 9 | 5 2 6 4 5 5 1 2 3 1 3 3 6 1 | 5 2 6 4 5 5 1 2 3 1 3 3 6 1 | Yes | 27.87 |
| 10 | 3 6 2 4 1 2 6 1 4 2 4 5 3 1 |  | No | 30.97 |
| 11 | 2 5 1 1 2 4 3 5 1 3 2 5 5 4 |  | No | 27.79 |
| 12 | 4 3 2 6 1 5 4 1 5 6 1 5 4 6 |  | No | 45.31 |
| 13 | 4 2 5 3 3 1 4 5 3 2 1 2 1 3 |  | No | 59.6 |
| 14 | 4 5 4 3 2 1 3 5 4 5 1 3 2 1 | 4 5 4 3 2 1 3 5 4 5 1 3 2 1 | Yes | 18.99 |
| 15 | 4 1 2 6 5 4 5 2 6 5 3 5 2 3 | 4 1 2 6 5 4 5 2 6 5 3 5 2 3 | Yes | 23.25 |
| 16 | 2 4 5 3 4 1 2 3 2 1 5 3 6 5 |  | No | 57.29 |
| 17 | 4 3 5 1 1 4 3 6 4 3 5 2 1 5 | 4 3 5 1 1 4 3 6 4 3 5 2 1 5 | Yes | 21.7 |
| 18 | 1 2 5 4 6 6 5 2 2 5 3 3 6 2 |  | No | 45.29 |
| 19 | 1 2 5 3 3 1 4 1 3 4 1 3 1 5 |  | No | 42.13 |
| 20 | 3 6 5 1 4 5 2 6 3 2 1 1 4 3 | 3 6 5 1 4 5 2 6 3 2 1 1 4 3 | Yes | 20.55 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1985 | 1985 | Yes | 4.1 |
| 2 | 1610 | 1610 | Yes | 2.66 |
| 3 | 2250 | 2250 | Yes | 2.94 |
| 4 | 1930 | 1930 | Yes | 3.79 |
| 5 | 1432 | 1432 | Yes | 4.35 |
| 6 | 1482 | 1482 | Yes | 4.06 |
| 7 | 928 | 928 | Yes | 3.0 |
| 8 | 1553 | 1553 | Yes | 3.88 |
| 9 | 2096 | 2096 | Yes | 3.67 |
| 10 | 1860 | 1860 | Yes | 3.84 |
| 11 | 1744 | 1744 | Yes | 3.12 |
| 12 | 620 | 620 | Yes | 5.58 |
| 13 | 1149 | 1149 | Yes | 2.4 |
| 14 | 1770 | 1770 | Yes | 3.83 |
| 15 | 1473 | 1473 | Yes | 3.15 |
| 16 | 1159 | 1159 | Yes | 3.38 |
| 17 | 1155 | 1155 | Yes | 6.42 |
| 18 | 1581 | 1581 | Yes | 4.29 |
| 19 | 1548 | 1548 | Yes | 3.55 |
| 20 | 2089 | 2089 | Yes | 3.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 | 37 | Yes | 16.51 |
| 2 | 51 | 51 | Yes | 10.69 |
| 3 | 43 | 43 | Yes | 14.75 |
| 4 | 65 | 65 | Yes | 8.45 |
| 5 | 62 | 62 | Yes | 12.6 |
| 6 | 36 | 36 | Yes | 20.0 |
| 7 | 58 | 58 | Yes | 17.89 |
| 8 | 48 | 48 | Yes | 15.06 |
| 9 | 52 | 52 | Yes | 14.54 |
| 10 | 70 | 70 | Yes | 10.44 |
| 11 | 65 | 65 | Yes | 15.99 |
| 12 | 54 | 54 | Yes | 17.8 |
| 13 | 62 | 62 | Yes | 21.36 |
| 14 | 37 | 37 | Yes | 7.56 |
| 15 | 44 | 45 | No | 5.48 |
| 16 | 55 | 55 | Yes | 12.26 |
| 17 | 53 | 53 | Yes | 13.63 |
| 18 | 35 | 35 | Yes | 21.47 |
| 19 | 69 | 69 | Yes | 24.59 |
| 20 | 75 | 75 | Yes | 26.91 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TSCGFJL | TSCGFJL | Yes | 5.17 |
| 2 | NQPVZFJ | NQPVZFJ | Yes | 5.15 |
| 3 | WMBFROU | WMBFROU | Yes | 6.0 |
| 4 | HSFBACR | HSFBACR | Yes | 6.04 |
| 5 | QXVESRY | QXVESRY | Yes | 5.7 |
| 6 | KRHVIGW | KRHVIGW | Yes | 7.58 |
| 7 | FZMDPBG | FZMDPBG | Yes | 5.65 |
| 8 | KAXJHFN | KAXJHFN | Yes | 4.99 |
| 9 | RMXUFOH | RMXUFOH | Yes | 4.5 |
| 10 | IHNWRSK | IHNWRSK | Yes | 5.77 |
| 11 | HXKABWD | HXKABWD | Yes | 4.91 |
| 12 | OCKBPZT | OCKBPZT | Yes | 4.81 |
| 13 | XDTOYGL | XDTOYGL | Yes | 4.33 |
| 14 | ZIBCJHO | ZIBCJHO | Yes | 5.62 |
| 15 | FULQRDC | FULQRDC | Yes | 4.89 |
| 16 | VPZJCLI | VPZJCLI | Yes | 6.18 |
| 17 | ILEOBSV | ILEOBSV | Yes | 5.14 |
| 18 | AUNOHFC | AUNOHFC | Yes | 2.61 |
| 19 | WHKRJEF | WHKRJEF | Yes | 4.92 |
| 20 | KCDJTEI | KCDJTEI | Yes | 7.56 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.49 |
| 2 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.31 |
| 3 | [2.4, 7.6] | 7.6 2.4 | Yes | 7.52 |
| 4 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.32 |
| 5 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.35 |
| 6 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.85 |
| 7 | [4.3, 5.7] | 5.7 4.3 | Yes | 5.3 |
| 8 | [3.4, 6.6] | 6.6 3.4 | Yes | 6.21 |
| 9 | [3.5, 6.5] | 6.5 3.5 | Yes | 5.74 |
| 10 | [0.9, 9.1] | 0.9 9.1 | Yes | 5.26 |
| 11 | [1.9, 8.1] | 1.9 8.1 | Yes | 5.72 |
| 12 | [3.4, 6.6] | 6.6 3.4 | Yes | 6.96 |
| 13 | [0.8, 9.2] | 0.8 9.2 | Yes | 6.97 |
| 14 | [2.5, 7.5] | 7.5 2.5 | Yes | 6.45 |
| 15 | [1.5, 8.5] | 1.5 8.5 | Yes | 7.12 |
| 16 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.62 |
| 17 | [1.7, 8.3] | 1.7 8.3 | Yes | 8.34 |
| 18 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.83 |
| 19 | [2.1, 7.9] | 2.1 7.9 | Yes | 12.28 |
| 20 | [1.9, 8.1] | 8.1 1.9 | Yes | 7.67 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KPH2VMMBUQB9 | KPH2VMMBUQB9 | Yes | 4.1 |
| 2 | 2V5RL3DAD8MY | 2V5RL3DAD8MY | Yes | 4.11 |
| 3 | B4HT0JB9PC5P | B4HT0JB9PC5P | Yes | 4.48 |
| 4 | LP15G7OJ7XYW | LP15G7OJ7XYW | Yes | 0.83 |
| 5 | 7WK60RA102RH | 7WK60RA102RH | Yes | 2.08 |
| 6 | DEI7X5HT2Z9B | DEI7X5HT2Z9B | Yes | 4.89 |
| 7 | 841DQAFJYJSH | 841DQAFJYJSH | Yes | 1.28 |
| 8 | 3D5VSB9806AI | 3D5VSB9806AI | Yes | 5.37 |
| 9 | PG5F7PKJQ6OR | PG5F7PKJQ6OR | Yes | 1.27 |
| 10 | FMCKZO6245UM | FMCKZO6245UM | Yes | 3.57 |
| 11 | H9MQR2GH64TC | H9MQR2GH64TC | Yes | 1.36 |
| 12 | ARFFM5IX11II | ARFFM5IX11II | Yes | 4.82 |
| 13 | LZBB8GHHAH8Q | LZBB8GHHAH8Q | Yes | 4.18 |
| 14 | JP0E1ASU1N5F | JP0E1ASU1N5F | Yes | 1.45 |
| 15 | 656RUORN3YEB | 656RUORN3YEB | Yes | 3.34 |
| 16 | J7ACGCBJRMLR | J7ACGCBJRMLR | Yes | 5.78 |
| 17 | 3AH06KEK6H2A | 3AH06KEK6H2A | Yes | 4.96 |
| 18 | 4BHP0BWDCFFF | 4BHP0BWDCFFF | Yes | 1.95 |
| 19 | HSQOI0S5MQP1 | HSQOI0S5MQP1 | Yes | 1.53 |
| 20 | BHUALT2YJ0NJ | BHUALT2YJ0NJ | Yes | 1.74 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 44 | Yes | 10.99 |
| 2 | 31 | 31 | Yes | 4.25 |
| 3 | 73 | 73 | Yes | 6.7 |
| 4 | 5 | 5 | Yes | 6.54 |
| 5 | 9 | 9 | Yes | 6.26 |
| 6 | 1440 | 1440 | Yes | 4.08 |
| 7 | 198 | 198 | Yes | 7.54 |
| 8 | 4096 | 4096 | Yes | 23.16 |
| 9 | 9 | 9 | Yes | 5.17 |
| 10 | 243 | 243 | Yes | 2.17 |
| 11 | 793 | 793 | Yes | 4.08 |
| 12 | 26 | 26 | Yes | 13.23 |
| 13 | 63 | 63 | Yes | 2.52 |
| 14 | 1 | 1 | Yes | 6.27 |
| 15 | 4 | 4 | Yes | 4.0 |
| 16 | 65 | 65 | Yes | 4.5 |
| 17 | 36 | 36 | Yes | 4.22 |
| 18 | 23 | 23 | Yes | 4.28 |
| 19 | 7680 | 7680 | Yes | 4.45 |
| 20 | 39 |  | No | 53.83 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ))_<\\ \/ | ))_<\\ \/ | Yes | 5.84 |
| 2 | _\  \\(<( | /\) <(_<)_  \\(<( | No | 10.47 |
| 3 | ) \</ )/\ |  | No | 17.42 |
| 4 |   \ (_<)< | \ (_<)< | No | 18.27 |
| 5 | <(()/\(() | <(()/\(() | Yes | 4.54 |
| 6 |  <_)\( (( | /\) <(_<) <_)\( (( | No | 12.55 |
| 7 | \<_(_//\/ | /\) <(_<)\<_(_//\/ | No | 12.07 |
| 8 | /<\\()\ < | /\) <(_</<\\()\ < | No | 16.23 |
| 9 |  <\_((/<  | /\) <(_<) <\_((/< | No | 8.12 |
| 10 | _<(\\<_<_ | /\) <(_<) _<(\\<_<_ | No | 12.78 |
| 11 | //\< _) < |  | No | 22.17 |
| 12 | _</ (\ \( | _</ (\ \(` | No | 8.26 |
| 13 | / < )//() | /\) <(_</ < )//() | No | 15.3 |
| 14 | \/_\ \/__ | \/_\ \/__ | Yes | 6.78 |
| 15 | \__(_<_<) | /\) <(_<) | No | 22.14 |
| 16 | /\_/\\/_/ | /\) <(_< | No | 13.29 |
| 17 | )/_)/((_< | /\) <(_<) | No | 3.48 |
| 18 |  _)<((\/  | /\) <(_<) _)<((\/ | No | 8.71 |
| 19 | _  _</)<_ |  | No | 44.58 |
| 20 | _/()) )/( | _/()) )/( | Yes | 10.52 |
