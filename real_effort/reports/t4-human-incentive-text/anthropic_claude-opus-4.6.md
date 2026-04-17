# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-27 10:07:07

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
| sudoku_game | 6706 | 35294 | 42000 | 5 | 15 | 27.97 | 559.38 |
| add_numbers | 4080 | 626 | 4706 | 20 | 0 | 2.50 | 50.04 |
| counting_zeros | 5130 | 16151 | 21281 | 7 | 13 | 16.79 | 335.78 |
| task_decoding | 5400 | 1953 | 7353 | 20 | 0 | 4.82 | 96.35 |
| task_summation | 5460 | 5914 | 11374 | 20 | 0 | 6.23 | 124.61 |
| task_transcription | 4242 | 755 | 4997 | 20 | 0 | 3.79 | 75.79 |
| task_sequences | 4141 | 4882 | 9023 | 20 | 0 | 5.93 | 118.66 |
| string_entry | 4583 | 2176 | 6759 | 15 | 5 | 4.60 | 91.95 |
| **TOTAL** | **39742** | **67751** | **107493** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 5 4 5 5 2 4 5 2 3 1 6 5 4 | 3 5 4 5 5 2 4 5 2 3 1 6 5 4 | Yes | 21.81 |
| 2 | 4 2 6 5 4 6 3 4 1 2 2 5 3 1 | 4 2 6 5 4 6 3 4 1 2 2 5 3 1 | Yes | 25.81 |
| 3 | 1 2 3 1 2 4 1 3 1 4 6 2 5 1 | 1 2 3 1 2 4 1 3 1 4 6 2 5 1 4 2 3 6 | No | 18.08 |
| 4 | 1 5 6 3 6 2 3 3 1 3 1 2 3 5 | 1 5 6 3 6 2 3 3 1 3 1 2 3 5 | Yes | 18.57 |
| 5 | 6 2 3 2 6 4 3 1 5 4 3 2 1 1 | 6 2 3 2 6 4 3 1 5 4 3 2 1 1 5 4 6 2 | No | 26.26 |
| 6 | 5 3 6 1 6 4 2 3 3 1 2 3 4 3 |  | No | 36.37 |
| 7 | 5 1 3 4 2 5 6 1 3 1 5 3 1 2 | 5 1 3 4 2 5 6 3 1 5 1 3 1 2 5 | No | 22.85 |
| 8 | 3 5 5 4 3 5 3 1 1 3 2 3 2 4 |  | No | 32.11 |
| 9 | 1 4 2 6 3 3 5 4 2 3 2 1 6 3 | 1 4 2 6 3 3 5 4 2 3 2 1 6 3 | Yes | 24.37 |
| 10 | 5 2 1 3 6 2 1 6 3 4 5 5 6 5 | 5 1 2 3 2 6 6 1 3 4 5 5 6 5 | No | 24.42 |
| 11 | 2 5 1 2 4 5 2 6 4 1 4 5 2 3 |  | No | 32.43 |
| 12 | 5 1 4 3 5 4 6 5 3 2 3 5 4 1 |  | No | 39.43 |
| 13 | 3 4 2 6 2 3 5 6 3 1 4 2 6 6 |  | No | 35.45 |
| 14 | 4 2 3 1 5 1 4 3 2 1 1 1 6 3 |  | No | 36.29 |
| 15 | 4 5 5 1 5 2 1 4 6 2 1 4 2 3 | 4 5 5 1 5 2 1 4 6 2 1 4 2 3 | Yes | 19.5 |
| 16 | 4 6 4 2 1 6 6 4 6 5 4 5 3 1 | 4 6 4 6 1 2 6 4 6 5 4 5 3 1 | No | 22.56 |
| 17 | 3 6 5 5 2 6 3 4 3 1 6 5 4 1 |  | No | 36.45 |
| 18 | 1 6 2 5 2 4 3 1 4 6 4 1 1 6 | 1 6 2 5 2 4 3 1 4 6 4 1 2 1 6 | No | 21.57 |
| 19 | 3 1 6 2 1 6 6 3 4 1 4 2 4 5 |  | No | 33.16 |
| 20 | 3 2 5 4 4 2 6 5 4 5 2 6 3 2 |  | No | 31.88 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2006 | 2006 | Yes | 2.02 |
| 2 | 1638 | 1638 | Yes | 2.33 |
| 3 | 914 | 914 | Yes | 2.29 |
| 4 | 1928 | 1928 | Yes | 2.65 |
| 5 | 1375 | 1375 | Yes | 3.16 |
| 6 | 2267 | 2267 | Yes | 2.82 |
| 7 | 605 | 605 | Yes | 2.45 |
| 8 | 685 | 685 | Yes | 2.38 |
| 9 | 1403 | 1403 | Yes | 2.93 |
| 10 | 1842 | 1842 | Yes | 2.03 |
| 11 | 2705 | 2705 | Yes | 2.12 |
| 12 | 945 | 945 | Yes | 2.3 |
| 13 | 2151 | 2151 | Yes | 3.13 |
| 14 | 1822 | 1822 | Yes | 2.4 |
| 15 | 2050 | 2050 | Yes | 2.52 |
| 16 | 1526 | 1526 | Yes | 2.5 |
| 17 | 881 | 881 | Yes | 2.42 |
| 18 | 1922 | 1922 | Yes | 2.52 |
| 19 | 1881 | 1881 | Yes | 2.53 |
| 20 | 2235 | 2235 | Yes | 2.51 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 | 60 | No | 9.06 |
| 2 | 70 | 63 | No | 11.17 |
| 3 | 61 | 58 | No | 10.18 |
| 4 | 64 | 55 | No | 8.47 |
| 5 | 53 | 53 | Yes | 10.83 |
| 6 | 46 | 45 | No | 6.89 |
| 7 | 54 | 47 | No | 8.63 |
| 8 | 48 | 48 | Yes | 28.46 |
| 9 | 38 | 38 | Yes | 14.49 |
| 10 | 64 | 64 | Yes | 9.81 |
| 11 | 44 | 44 | Yes | 13.32 |
| 12 | 58 | 53 | No | 8.67 |
| 13 | 42 | 42 | Yes | 11.54 |
| 14 | 64 | 61 | No | 10.12 |
| 15 | 40 | 38 | No | 7.97 |
| 16 | 61 | 59 | No | 9.54 |
| 17 | 37 | 37 | Yes | 9.04 |
| 18 | 39 | 38 | No | 16.31 |
| 19 | 67 | TIMEOUT | No | 120.03 |
| 20 | 58 | 57 | No | 11.25 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QNXCATW | QNXCATW | Yes | 5.49 |
| 2 | VIDTJXG | VIDTJXG | Yes | 3.37 |
| 3 | KXNAFLW | KXNAFLW | Yes | 4.12 |
| 4 | NJHELDQ | NJHELDQ | Yes | 3.79 |
| 5 | XUTFNDW | XUTFNDW | Yes | 4.18 |
| 6 | ZJRYBGX | ZJRYBGX | Yes | 4.85 |
| 7 | WRTQFGB | WRTQFGB | Yes | 4.17 |
| 8 | OVBIERC | OVBIERC | Yes | 3.21 |
| 9 | XMVOGJY | XMVOGJY | Yes | 3.86 |
| 10 | CFGUVOJ | CFGUVOJ | Yes | 3.47 |
| 11 | VCMYAGQ | VCMYAGQ | Yes | 3.7 |
| 12 | WEYUTAB | WEYUTAB | Yes | 5.34 |
| 13 | WSRANQC | WSRANQC | Yes | 13.82 |
| 14 | YJPIDWU | YJPIDWU | Yes | 4.23 |
| 15 | CZXVPSG | CZXVPSG | Yes | 3.48 |
| 16 | LIBUYJW | LIBUYJW | Yes | 6.06 |
| 17 | LWEIVTP | LWEIVTP | Yes | 5.47 |
| 18 | AXDIHTL | AXDIHTL | Yes | 3.75 |
| 19 | EUPKLRD | EUPKLRD | Yes | 4.51 |
| 20 | AUBTDQG | AUBTDQG | Yes | 5.48 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 4.0 6.0 | Yes | 6.52 |
| 2 | [4.4, 5.6] | 4.4 5.6 | Yes | 6.97 |
| 3 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.96 |
| 4 | [5.0, 5.0] | 5.0 5.0 | Yes | 6.12 |
| 5 | [2.4, 7.6] | 2.4 7.6 | Yes | 4.63 |
| 6 | [1.0, 9.0] | 1.0 9.0 | Yes | 4.21 |
| 7 | [3.5, 6.5] | 6.5 3.5 | Yes | 5.5 |
| 8 | [4.0, 6.0] | 4.0 6.0 | Yes | 12.46 |
| 9 | [0.3, 9.7] | 9.7 0.3 | Yes | 4.28 |
| 10 | [4.9, 5.1] | 4.9 5.1 | Yes | 5.62 |
| 11 | [0.6, 9.4] | 9.4 0.6 | Yes | 4.4 |
| 12 | [2.2, 7.8] | 7.8 2.2 | Yes | 6.51 |
| 13 | [2.3, 7.7] | 7.7 2.3 | Yes | 5.83 |
| 14 | [3.6, 6.4] | 3.6 6.4 | Yes | 3.94 |
| 15 | [5.0, 5.0] | 5.0 5.0 | Yes | 10.43 |
| 16 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.07 |
| 17 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.16 |
| 18 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.51 |
| 19 | [0.8, 9.2] | 9.2 0.8 | Yes | 5.96 |
| 20 | [2.4, 7.6] | 7.6 2.4 | Yes | 7.54 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | APNHXI2V7IZ1 | APNHXI2V7IZ1 | Yes | 3.61 |
| 2 | NRF3KYA5GQ8A | NRF3KYA5GQ8A | Yes | 2.49 |
| 3 | 2USF6ARU9L9R | 2USF6ARU9L9R | Yes | 2.78 |
| 4 | UOFXG7MM524P | UOFXG7MM524P | Yes | 8.43 |
| 5 | VM16NS02M2EP | VM16NS02M2EP | Yes | 13.77 |
| 6 | U31TAIDIE6GI | U31TAIDIE6GI | Yes | 2.59 |
| 7 | 5FKZJ8OJB7XV | 5FKZJ8OJB7XV | Yes | 3.54 |
| 8 | 5PQNGTGE0WOD | 5PQNGTGE0WOD | Yes | 2.79 |
| 9 | OD9OTWJYXL8D | OD9OTWJYXL8D | Yes | 3.35 |
| 10 | STU88TUB8EW1 | STU88TUB8EW1 | Yes | 2.45 |
| 11 | ZD3WVA2CSOJU | ZD3WVA2CSOJU | Yes | 3.05 |
| 12 | X3WJLBBV77KG | X3WJLBBV77KG | Yes | 3.79 |
| 13 | 3NFU915J652U | 3NFU915J652U | Yes | 2.4 |
| 14 | QHXQ6ULYTRPQ | QHXQ6ULYTRPQ | Yes | 2.89 |
| 15 | UBQXMYRLB27H | UBQXMYRLB27H | Yes | 2.39 |
| 16 | 2AD2WLQ5L02H | 2AD2WLQ5L02H | Yes | 3.03 |
| 17 | V99CLRHQOO90 | V99CLRHQOO90 | Yes | 3.21 |
| 18 | HKF30X59ODJG | HKF30X59ODJG | Yes | 2.45 |
| 19 | FRRP0KVPUFNZ | FRRP0KVPUFNZ | Yes | 3.04 |
| 20 | UJQAOBV3Q60W | UJQAOBV3Q60W | Yes | 3.73 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 5.72 |
| 2 | 60 | 60 | Yes | 4.89 |
| 3 | 3 | 3 | Yes | 5.42 |
| 4 | 19 | 19 | Yes | 2.95 |
| 5 | 3 | 3 | Yes | 5.6 |
| 6 | 4096 | 4096 | Yes | 15.69 |
| 7 | 64 | 64 | Yes | 5.88 |
| 8 | 1 | 1 | Yes | 5.05 |
| 9 | 36 | 36 | Yes | 2.58 |
| 10 | 48 | 48 | Yes | 4.31 |
| 11 | 31 | 31 | Yes | 5.21 |
| 12 | 243 | 243 | Yes | 2.9 |
| 13 | 26 | 26 | Yes | 7.88 |
| 14 | 5 | 5 | Yes | 5.22 |
| 15 | 793 | 793 | Yes | 2.99 |
| 16 | 63 | 63 | Yes | 4.71 |
| 17 | 4 | 4 | Yes | 2.79 |
| 18 | 73 | 73 | Yes | 6.64 |
| 19 | 6 | 6 | Yes | 7.74 |
| 20 | 20 | 20 | Yes | 14.48 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _ (<\)<<\ | _ (<\)<<\ | Yes | 2.62 |
| 2 | ()\< </)) | ()\< </)) | Yes | 3.11 |
| 3 | <)(_)\<\) | <)(_)\<\) | Yes | 7.9 |
| 4 | <  <)(__< | <  <)(__ | No | 4.78 |
| 5 | _\\_\)/\\ | _\\_\)/\\ | Yes | 3.94 |
| 6 |  <()//\_( | <()//\_( | No | 3.22 |
| 7 | ())_(\\_\ | ())_(\\_\ | Yes | 2.71 |
| 8 | _\_ )\/_\ | _\_ )\/_\ | Yes | 3.81 |
| 9 | ()(\<_\/) | ()(\<_\/) | Yes | 3.92 |
| 10 | /<_(_(<\( | /<_(_(<\( | Yes | 6.35 |
| 11 | \_))()  / | \_))()  / | Yes | 3.72 |
| 12 | /( )<<\(/ | /( )<<\(/ | Yes | 2.97 |
| 13 | \\\\_(</\ | \\\\_(</\ | Yes | 3.53 |
| 14 | //<_\/<(/ | //<_\/<(/ | Yes | 3.23 |
| 15 | __<()(<)  | __<()(<) | No | 5.13 |
| 16 | /\\)//</  | /\)//</ | No | 13.44 |
| 17 | ( /_((_(/ | ( /_((_(/ | Yes | 3.13 |
| 18 | </ ( )<(  | </ ( )<( | No | 8.1 |
| 19 | <)__)_)/\ | <)__)_)/\ | Yes | 3.3 |
| 20 | <\/  _)<( | <\/  _)<( | Yes | 3.03 |
