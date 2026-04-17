# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-27 10:29:23

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
| sudoku_game | 5479 | 39347 | 44826 | 0 | 20 | 50.38 | 1007.59 |
| add_numbers | 3078 | 851 | 3929 | 19 | 1 | 9.58 | 191.67 |
| counting_zeros | 4640 | 31553 | 36193 | 16 | 4 | 27.19 | 543.77 |
| task_decoding | 4580 | 3437 | 8017 | 20 | 0 | 5.07 | 101.32 |
| task_summation | 4674 | 5737 | 10411 | 19 | 1 | 13.08 | 261.51 |
| task_transcription | 3379 | 1075 | 4454 | 20 | 0 | 2.84 | 56.77 |
| task_sequences | 3241 | 8493 | 11734 | 17 | 3 | 14.42 | 288.47 |
| string_entry | 3682 | 15674 | 19356 | 11 | 9 | 16.79 | 335.81 |
| **TOTAL** | **32753** | **106167** | **138920** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 3 6 4 1 3 6 1 6 2 3 5 1 4 |  | No | 60.09 |
| 2 | 2 3 5 4 5 3 6 5 4 2 3 5 3 5 |  | No | 55.75 |
| 3 | 1 5 6 2 4 1 2 4 3 6 2 5 2 6 |  | No | 21.15 |
| 4 | 4 5 3 6 1 2 1 5 3 2 1 6 1 4 |  | No | 65.35 |
| 5 | 3 1 6 2 5 2 6 4 2 5 1 6 5 3 |  | No | 29.59 |
| 6 | 6 1 5 3 1 5 5 4 4 3 1 5 4 6 |  | No | 45.73 |
| 7 | 2 3 1 5 2 4 1 6 5 3 6 2 3 1 |  | No | 46.85 |
| 8 | 3 2 1 6 2 6 2 3 4 6 1 2 5 6 |  | No | 52.09 |
| 9 | 4 2 2 1 1 6 2 5 4 2 2 5 1 3 |  | No | 52.68 |
| 10 | 3 4 2 5 3 4 3 2 6 1 2 3 2 6 |  | No | 50.72 |
| 11 | 1 3 5 2 3 4 3 5 6 1 6 6 1 4 |  | No | 53.91 |
| 12 | 1 6 3 3 5 1 5 1 5 4 5 1 2 6 |  | No | 59.16 |
| 13 | 2 6 2 6 1 2 4 1 6 6 6 2 4 1 |  | No | 62.09 |
| 14 | 5 6 1 6 6 2 1 3 4 6 3 3 1 5 |  | No | 53.46 |
| 15 | 2 6 6 4 3 5 6 1 1 6 5 4 1 4 |  | No | 58.84 |
| 16 | 6 4 5 3 3 5 4 6 3 6 3 2 5 4 |  | No | 47.02 |
| 17 | 1 2 4 2 2 6 1 5 3 1 6 3 4 2 |  | No | 48.37 |
| 18 | 3 6 5 4 2 6 5 4 5 2 3 3 4 5 |  | No | 43.56 |
| 19 | 2 3 4 6 4 6 1 5 6 4 5 3 2 4 |  | No | 46.66 |
| 20 | 1 2 2 1 3 6 4 5 5 2 4 6 1 6 |  | No | 54.49 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1619 | 1619 | Yes | 3.38 |
| 2 | 1733 | 1733 | Yes | 3.38 |
| 3 | 1852 | 1852 | Yes | 3.43 |
| 4 | 1386 | 1386 | Yes | 3.66 |
| 5 | 1561 | 1561 | Yes | 2.62 |
| 6 | 638 | 638 | Yes | 2.8 |
| 7 | 2083 | 2083 | Yes | 3.76 |
| 8 | 1130 | 1130 | Yes | 3.12 |
| 9 | 1465 | 1465 | Yes | 3.01 |
| 10 | 2185 | 2185 | Yes | 2.58 |
| 11 | 1114 | 1114 | Yes | 5.62 |
| 12 | 1945 | 1945 | Yes | 2.36 |
| 13 | 1602 | 1602 | Yes | 4.06 |
| 14 | 1124 | 1124 | Yes | 6.46 |
| 15 | 2715 | 2715 | Yes | 4.69 |
| 16 | 2250 | 2250 | Yes | 3.96 |
| 17 | 1083 | 1083 | Yes | 5.74 |
| 18 | 2058 | 2058 | Yes | 3.23 |
| 19 | 561 | TIMEOUT | No | 120.02 |
| 20 | 2333 | 2333 | Yes | 3.78 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 74 | Yes | 30.35 |
| 2 | 54 | 54 | Yes | 24.54 |
| 3 | 42 | 42 | Yes | 17.74 |
| 4 | 57 | 57 | Yes | 24.1 |
| 5 | 42 | 42 | Yes | 32.63 |
| 6 | 63 | 63 | Yes | 30.98 |
| 7 | 70 |  | No | 55.8 |
| 8 | 39 | 39 | Yes | 14.25 |
| 9 | 51 | 51 | Yes | 18.23 |
| 10 | 46 |  | No | 49.53 |
| 11 | 66 | 66 | Yes | 16.97 |
| 12 | 70 | 70 | Yes | 21.59 |
| 13 | 56 | 56 | Yes | 17.6 |
| 14 | 74 | 74 | Yes | 13.98 |
| 15 | 75 | 75 | Yes | 20.26 |
| 16 | 65 | 65 | Yes | 21.2 |
| 17 | 56 | 56 | Yes | 18.72 |
| 18 | 59 |  | No | 49.37 |
| 19 | 75 |  | No | 42.57 |
| 20 | 39 | 39 | Yes | 23.34 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FILOYRZ | FILOYRZ | Yes | 3.73 |
| 2 | XUCFLIZ | XUCFLIZ | Yes | 5.75 |
| 3 | HUWPRAQ | HUWPRAQ | Yes | 3.8 |
| 4 | EHOCTRI | EHOCTRI | Yes | 6.25 |
| 5 | QIWBGHR | QIWBGHR | Yes | 4.84 |
| 6 | DLGVOPR | DLGVOPR | Yes | 7.53 |
| 7 | ELYPWOD | ELYPWOD | Yes | 4.32 |
| 8 | RVDSHEP | RVDSHEP | Yes | 4.74 |
| 9 | WYGCTUV | WYGCTUV | Yes | 6.72 |
| 10 | ZVUANOG | ZVUANOG | Yes | 4.41 |
| 11 | DWEVMTL | DWEVMTL | Yes | 3.71 |
| 12 | UKLZTXC | UKLZTXC | Yes | 5.53 |
| 13 | GDMEKNO | GDMEKNO | Yes | 5.62 |
| 14 | SAFDLMG | SAFDLMG | Yes | 3.04 |
| 15 | ZWFJEYP | ZWFJEYP | Yes | 5.74 |
| 16 | XYIRKFW | XYIRKFW | Yes | 5.88 |
| 17 | BKCVRMW | BKCVRMW | Yes | 5.09 |
| 18 | IOENSZX | IOENSZX | Yes | 6.55 |
| 19 | QBETNUA | QBETNUA | Yes | 6.08 |
| 20 | HWLFKBC | HWLFKBC | Yes | 2.0 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.12 |
| 2 | [4.1, 5.9] | 5.9 4.1 | Yes | 7.25 |
| 3 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.06 |
| 4 | [3.4, 6.6] | TIMEOUT | No | 120.01 |
| 5 | [3.1, 6.9] | 3.1 6.9 | Yes | 7.28 |
| 6 | [4.1, 5.9] | 4.1 5.9 | Yes | 4.55 |
| 7 | [4.5, 5.5] | 4.5 5.5 | Yes | 12.71 |
| 8 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.36 |
| 9 | [4.4, 5.6] | 5.6 4.4 | Yes | 5.2 |
| 10 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.31 |
| 11 | [0.1, 9.9] | 9.9 0.1 | Yes | 5.27 |
| 12 | [2.9, 7.1] | 2.9 7.1 | Yes | 6.05 |
| 13 | [2.4, 7.6] | 2.4 7.6 | Yes | 8.35 |
| 14 | [1.9, 8.1] | 8.1 1.9 | Yes | 4.89 |
| 15 | [2.4, 7.6] | 2.4 7.6 | Yes | 9.72 |
| 16 | [0.7, 9.3] | 9.3 0.7 | Yes | 8.62 |
| 17 | [3.0, 7.0] | 7.0 3.0 | Yes | 5.71 |
| 18 | [3.5, 6.5] | 6.5 3.5 | Yes | 9.25 |
| 19 | [4.5, 5.5] | 5.5 4.5 | Yes | 4.63 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 12.17 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6B5Y63XYW5A8 | 6B5Y63XYW5A8 | Yes | 1.6 |
| 2 | X1CQW85P0IYZ | X1CQW85P0IYZ | Yes | 3.55 |
| 3 | MAD3UGA61ANY | MAD3UGA61ANY | Yes | 2.04 |
| 4 | 9H1ZW00FD5CV | 9H1ZW00FD5CV | Yes | 2.24 |
| 5 | WWWIL736KJ0M | WWWIL736KJ0M | Yes | 1.74 |
| 6 | JFLWSGYUFEAH | JFLWSGYUFEAH | Yes | 4.98 |
| 7 | YCN216QAEKHG | YCN216QAEKHG | Yes | 2.28 |
| 8 | 7LGSYECH0CLF | 7LGSYECH0CLF | Yes | 4.41 |
| 9 | XXIUZ94JSSDK | XXIUZ94JSSDK | Yes | 1.31 |
| 10 | Y5N2H2GLOLXG | Y5N2H2GLOLXG | Yes | 1.5 |
| 11 | D9P960SB6ECH | D9P960SB6ECH | Yes | 4.27 |
| 12 | DAISZQYJ50XF | DAISZQYJ50XF | Yes | 1.72 |
| 13 | DC49UINFYHGW | DC49UINFYHGW | Yes | 1.43 |
| 14 | EH3RX7Y2YEEG | EH3RX7Y2YEEG | Yes | 4.48 |
| 15 | N805CYB2SGI1 | N805CYB2SGI1 | Yes | 1.31 |
| 16 | 7GT62X6EU9V6 | 7GT62X6EU9V6 | Yes | 2.54 |
| 17 | 1USISJI433X0 | 1USISJI433X0 | Yes | 3.53 |
| 18 | O5VBMZME22E9 | O5VBMZME22E9 | Yes | 4.71 |
| 19 | PEEEI4YHB5FG | PEEEI4YHB5FG | Yes | 3.95 |
| 20 | OJY4WYJVEIOU | OJY4WYJVEIOU | Yes | 3.18 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 5 | Yes | 3.88 |
| 2 | 3 | 3 | Yes | 8.19 |
| 3 | 26 |  | No | 63.09 |
| 4 | 10 | 10 | Yes | 8.7 |
| 5 | 23 | 23 | Yes | 5.06 |
| 6 | 5 |  | No | 70.12 |
| 7 | 1440 | 1440 | Yes | 4.92 |
| 8 | 9 | 9 | Yes | 11.09 |
| 9 | 67 | 67 | Yes | 4.93 |
| 10 | 60 | 60 | Yes | 5.8 |
| 11 | 243 | 243 | Yes | 1.49 |
| 12 | 31 | 31 | Yes | 5.81 |
| 13 | 793 | 793 | Yes | 5.63 |
| 14 | 198 | 198 | Yes | 7.46 |
| 15 | 7 | 7 | Yes | 3.66 |
| 16 | 4096 |  | No | 55.63 |
| 17 | 44 | 44 | Yes | 10.76 |
| 18 | 19 | 19 | Yes | 2.09 |
| 19 | 4 | 4 | Yes | 6.06 |
| 20 | 39 | 39 | Yes | 4.08 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <</)/   < | <</)/   < | Yes | 7.83 |
| 2 | \ /\__<_( | \ /\__<_( | Yes | 11.28 |
| 3 | )<_)<)<<< |  | No | 50.94 |
| 4 | _\<<)<))\ |  | No | 52.39 |
| 5 | /(\((<< _ | /(\((<< _ | Yes | 2.79 |
| 6 | _/ (/ _\_ | _/ (/ _\_ | Yes | 21.78 |
| 7 | () ))_ <\ | () ))_ \< | No | 7.39 |
| 8 | (( __/\(/ | (( __/\(/ | Yes | 4.75 |
| 9 | (__(  <__ |  | No | 45.09 |
| 10 | _)(_< ()/ | _)(_< ()/ | Yes | 2.75 |
| 11 | __/_  \_/ | __/_  \_/ | Yes | 2.89 |
| 12 | /)_/(/ _  | /)_/(/ _ | No | 14.34 |
| 13 | (_<) \_<_ | (_<) \_<_ | Yes | 6.25 |
| 14 | \</)_ <(( | \</)_ <(( | Yes | 6.72 |
| 15 | <\_<</(/  | /\) <(_<) | No | 26.29 |
| 16 | _\(( _<_\ | _\(( _<_\ | Yes | 11.83 |
| 17 | <(_/(()(< | <(_/(()(< | Yes | 21.48 |
| 18 | //<)/ \   | //<)/ \ | No | 13.03 |
| 19 | (/\\(<//  | (/\(<// | No | 14.29 |
| 20 |  _\)\< \/ | _\)\< \/ | No | 11.69 |
