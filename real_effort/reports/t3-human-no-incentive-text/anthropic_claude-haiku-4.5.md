# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-27 09:55:48

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
| sudoku_game | 6478 | 32039 | 38517 | 4 | 16 | 12.43 | 248.59 |
| add_numbers | 3860 | 3293 | 7153 | 20 | 0 | 2.79 | 55.72 |
| counting_zeros | 5180 | 21013 | 26193 | 1 | 19 | 7.10 | 141.94 |
| task_decoding | 5180 | 7186 | 12366 | 19 | 1 | 3.09 | 61.9 |
| task_summation | 5240 | 14815 | 20055 | 20 | 0 | 5.66 | 113.22 |
| task_transcription | 4015 | 2698 | 6713 | 20 | 0 | 1.92 | 38.41 |
| task_sequences | 3921 | 7650 | 11571 | 18 | 2 | 3.36 | 67.2 |
| string_entry | 4421 | 5654 | 10075 | 8 | 12 | 3.06 | 61.18 |
| **TOTAL** | **38295** | **94348** | **132643** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 3 1 4 6 2 1 3 2 4 6 1 2 3 | 2 3 1 4 6 2 1 3 2 4 1 6 4 5 | No | 12.3 |
| 2 | 1 3 5 1 4 1 6 2 3 2 3 1 4 1 | 1 3 5 1 4 2 3 1 2 6 1 3 2 4 2 | No | 34.47 |
| 3 | 1 2 6 1 3 1 3 4 6 3 4 4 2 3 | 2 1 3 1 6 1 3 4 6 4 4 4 1 3 | No | 13.85 |
| 4 | 6 2 1 4 6 3 2 4 4 5 5 1 2 3 | 6 2 1 3 4 1 4 5 6 3 2 4 2 3 4 5 1 6 5 1 4 2 5 3 | No | 9.69 |
| 5 | 3 5 6 1 5 3 3 6 5 3 2 6 1 5 | 5 3 6 1 3 3 5 2 6 1 4 5 | No | 11.79 |
| 6 | 3 6 4 4 1 2 2 3 2 5 4 1 1 4 | 3 6 4 4 2 1 2 5 3 4 1 1 4 | No | 8.35 |
| 7 | 3 5 2 4 2 4 6 3 6 3 4 5 1 6 | 3 5 2 4 2 4 3 6 5 6 4 6 1 3 | No | 18.4 |
| 8 | 5 1 2 3 2 1 5 2 2 3 5 1 3 2 | 1 2 5 3 2 1 5 3 1 2 3 2 | No | 11.48 |
| 9 | 3 1 6 1 5 6 2 5 1 2 1 2 4 2 | 3 6 1 1 5 2 6 1 5 2 1 2 4 2 | No | 10.38 |
| 10 | 5 1 2 2 5 4 3 2 1 6 3 1 4 2 | 5 1 2 2 5 4 3 1 6 3 1 4 2 | No | 9.11 |
| 11 | 1 6 5 2 6 6 2 1 3 5 3 4 3 1 | 1 6 5 2 6 6 2 1 3 5 3 4 3 1 | Yes | 9.67 |
| 12 | 5 6 2 1 5 4 2 5 1 1 4 5 2 3 | 5 6 2 5 1 4 5 2 1 1 4 2 5 3 | No | 9.58 |
| 13 | 3 6 1 4 5 6 2 6 1 2 6 2 5 1 | 3 6 1 4 5 6 2 6 1 2 6 2 5 1 | Yes | 9.09 |
| 14 | 2 5 5 3 6 4 1 3 1 2 6 2 3 3 | 2 5 5 3 6 4 1 3 2 1 6 1 3 3** | No | 8.79 |
| 15 | 2 4 5 4 5 3 2 5 1 5 1 6 2 5 | 2 4 5 4 5 3 2 5 1 5 1 6 2 5 | Yes | 7.63 |
| 16 | 3 2 6 2 4 3 5 5 4 2 1 2 6 5 | 3 2 6 2 4 3 5 5 4 2 1 2 6 5 | Yes | 8.34 |
| 17 | 2 3 4 3 4 6 1 5 3 5 2 3 1 3 | 4 2 3 5 3 4 5 2 1 3 | No | 9.09 |
| 18 | 6 1 2 5 1 3 5 5 3 1 2 6 2 5 | ** 6 1 5 2 5 3 3 5 1 2 6 2 | No | 10.78 |
| 19 | 1 5 2 5 5 1 6 1 3 5 4 1 4 3 | 5 1 2 5 5 1 6 1 3 5 5 4 3 | No | 10.71 |
| 20 | 4 3 4 1 6 2 5 5 1 3 3 1 2 2 | 4 6 3 1 2 5 6 5 3 1 1 3 2 2 | No | 25.06 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1530 | 1530 | Yes | 1.64 |
| 2 | 2271 | 2271 | Yes | 2.41 |
| 3 | 1471 | 1471 | Yes | 12.31 |
| 4 | 1162 | 1162 | Yes | 1.62 |
| 5 | 1104 | 1104 | Yes | 2.22 |
| 6 | 1144 | 1144 | Yes | 1.76 |
| 7 | 2672 | 2672 | Yes | 3.27 |
| 8 | 2041 | 2041 | Yes | 2.09 |
| 9 | 2587 | 2587 | Yes | 1.95 |
| 10 | 369 | 369 | Yes | 1.48 |
| 11 | 1702 | 1702 | Yes | 1.91 |
| 12 | 2032 | 2032 | Yes | 2.22 |
| 13 | 2121 | 2121 | Yes | 2.37 |
| 14 | 1581 | 1581 | Yes | 4.62 |
| 15 | 1308 | 1308 | Yes | 1.83 |
| 16 | 1541 | 1541 | Yes | 2.52 |
| 17 | 1838 | 1838 | Yes | 2.11 |
| 18 | 2272 | 2272 | Yes | 2.78 |
| 19 | 1854 | 1854 | Yes | 1.7 |
| 20 | 1699 | 1699 | Yes | 2.91 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 62 | No | 4.33 |
| 2 | 48 | 47 | No | 7.05 |
| 3 | 73 | 63 | No | 7.7 |
| 4 | 45 | 36 | No | 7.84 |
| 5 | 64 | 62 | No | 6.11 |
| 6 | 67 | 65 | No | 8.91 |
| 7 | 46 | 45 | No | 6.47 |
| 8 | 44 | 37 | No | 5.81 |
| 9 | 70 | 55 | No | 6.6 |
| 10 | 50 | 43 | No | 8.11 |
| 11 | 39 | 38 | No | 6.3 |
| 12 | 63 | 58 | No | 6.63 |
| 13 | 52 | 48 | No | 9.14 |
| 14 | 58 | 58 | Yes | 8.2 |
| 15 | 73 | 54 | No | 6.88 |
| 16 | 47 | 42 | No | 3.87 |
| 17 | 63 | 49 | No | 7.53 |
| 18 | 39 | 36 | No | 7.84 |
| 19 | 65 | 63 | No | 9.72 |
| 20 | 35 | 34 | No | 6.91 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FEJILYC | FEJILCY | No | 2.84 |
| 2 | ZVUCONF | ZVUCONF | Yes | 2.72 |
| 3 | WGOXAZS | WGOXAZS | Yes | 2.78 |
| 4 | UILKGMO | UILKGMO | Yes | 2.56 |
| 5 | DFTCSYL | DFTCSYL | Yes | 2.44 |
| 6 | QCZVNXO | QCZVNXO | Yes | 2.77 |
| 7 | YXTMBHS | YXTMBHS | Yes | 2.65 |
| 8 | CRITNKV | CRITNKV | Yes | 3.33 |
| 9 | YGLONSC | YGLONSC | Yes | 2.59 |
| 10 | TVIRGAX | TVIRGAX | Yes | 3.87 |
| 11 | AMISNYG | AMISNYG | Yes | 4.32 |
| 12 | FLYVIXQ | FLYVIXQ | Yes | 3.25 |
| 13 | CDKPJZV | CDKPJZV | Yes | 3.73 |
| 14 | BYQSNHG | BYQSNHG | Yes | 2.28 |
| 15 | IMEODZR | IMEODZR | Yes | 3.65 |
| 16 | TKUDYQH | TKUDYQH | Yes | 3.31 |
| 17 | FUEHYOT | FUEHYOT | Yes | 3.91 |
| 18 | HZKMXIB | HZKMXIB | Yes | 2.49 |
| 19 | IQXNPAW | IQXNPAW | Yes | 3.17 |
| 20 | SLCJXYU | SLCJXYU | Yes | 3.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.0, 7.0] | 7.0 3.0 | Yes | 5.44 |
| 2 | [3.0, 7.0] | 3.0 7.0 | Yes | 5.09 |
| 3 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.31 |
| 4 | [4.2, 5.8] | 4.2 5.8 | Yes | 5.5 |
| 5 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.94 |
| 6 | [4.9, 5.1] | 5.1 4.9 | Yes | 9.44 |
| 7 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.87 |
| 8 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.57 |
| 9 | [2.4, 7.6] | 2.4 7.6 | Yes | 7.09 |
| 10 | [0.8, 9.2] | 9.2 0.8 | Yes | 7.66 |
| 11 | [3.1, 6.9] | 6.9 3.1 | Yes | 5.93 |
| 12 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.28 |
| 13 | [1.7, 8.3] | 8.3 1.7 | Yes | 5.35 |
| 14 | [4.6, 5.4] | 5.4 4.6 | Yes | 4.69 |
| 15 | [1.8, 8.2] | 8.2 1.8 | Yes | 5.43 |
| 16 | [0.2, 9.8] | 9.8 0.2 | Yes | 4.12 |
| 17 | [3.9, 6.1] | 3.9 6.1 | Yes | 4.38 |
| 18 | [1.1, 8.9] | 1.1 8.9 | Yes | 4.3 |
| 19 | [4.0, 6.0] | 4.0 6.0 | Yes | 4.71 |
| 20 | [3.8, 6.2] | 3.8 6.2 | Yes | 7.09 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9LNJ3IQY0783 | 9LNJ3IQY0783 | Yes | 2.6 |
| 2 | GVC7DS3M2YK1 | GVC7DS3M2YK1 | Yes | 1.72 |
| 3 | 8IEN6QSI7MD3 | 8IEN6QSI7MD3 | Yes | 1.7 |
| 4 | UDDOMF4X4S2N | UDDOMF4X4S2N | Yes | 1.89 |
| 5 | 7NP4GHOMQ741 | 7NP4GHOMQ741 | Yes | 2.0 |
| 6 | FC7K9BPNJGJP | FC7K9BPNJGJP | Yes | 1.86 |
| 7 | H6CRP4D5MIEY | H6CRP4D5MIEY | Yes | 1.87 |
| 8 | 78C0VCIMCI0W | 78C0VCIMCI0W | Yes | 2.21 |
| 9 | 4VUD3L42V458 | 4VUD3L42V458 | Yes | 1.65 |
| 10 | 9KRV70MDAEQH | 9KRV70MDAEQH | Yes | 2.04 |
| 11 | OJOZMFHL0D4F | OJOZMFHL0D4F | Yes | 1.84 |
| 12 | PGOVIVGHVO9C | PGOVIVGHVO9C | Yes | 1.49 |
| 13 | 0XJ15YH53OKZ | 0XJ15YH53OKZ | Yes | 2.16 |
| 14 | MMLG2ATNTYEA | MMLG2ATNTYEA | Yes | 2.37 |
| 15 | HIZJY6H86LBH | HIZJY6H86LBH | Yes | 1.89 |
| 16 | J0TTW6H757XC | J0TTW6H757XC | Yes | 1.92 |
| 17 | MK7CHPBHI8TZ | MK7CHPBHI8TZ | Yes | 1.88 |
| 18 | SQQXSFSJD0TZ | SQQXSFSJD0TZ | Yes | 1.82 |
| 19 | JG0WCKKGNFJU | JG0WCKKGNFJU | Yes | 1.92 |
| 20 | ICSNBXPF3U8F | ICSNBXPF3U8F | Yes | 1.56 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 2.02 |
| 2 | 5 | 16 | No | 9.39 |
| 3 | 20 | 42 | No | 7.04 |
| 4 | 243 | 243 | Yes | 2.21 |
| 5 | 60 | 60 | Yes | 2.11 |
| 6 | 64 | 64 | Yes | 2.11 |
| 7 | 31 | 31 | Yes | 2.22 |
| 8 | 1 | 1 | Yes | 2.54 |
| 9 | 73 | 73 | Yes | 2.1 |
| 10 | 3 | 3 | Yes | 6.69 |
| 11 | 60 | 60 | Yes | 3.04 |
| 12 | 28 | 28 | Yes | 1.99 |
| 13 | 7 | 7 | Yes | 2.15 |
| 14 | 4 | 4 | Yes | 2.02 |
| 15 | 4096 | 4096 | Yes | 5.37 |
| 16 | 16 | 16 | Yes | 3.28 |
| 17 | 3 | 3 | Yes | 2.86 |
| 18 | 26 | 26 | Yes | 3.7 |
| 19 | 10 | 10 | Yes | 2.61 |
| 20 | 48 | 48 | Yes | 1.73 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | </ ((<_(  | </ ((<_( | No | 4.43 |
| 2 |  \\\(\</< | \\\(\</ | No | 4.05 |
| 3 | /  __\/__ | /  __\/__ | Yes | 2.25 |
| 4 | \<\(<_)   | \<\(<_) | No | 2.34 |
| 5 | ( //\((\/ | ( //\((\/ | Yes | 3.29 |
| 6 | ()()( / _ | ()()( / _ | Yes | 2.62 |
| 7 | ) \\ ()<\ | /\) <(_<) | No | 3.49 |
| 8 | \ \<(\\ ) | \ \<(\ ) | Yes | 3.27 |
| 9 | /\\  (<\< | /\\  (<\ | No | 2.78 |
| 10 | ))(\<)_ < | ))(\<)_ | No | 2.75 |
| 11 | <_ _\ </  | /\) <(_<) | No | 2.75 |
| 12 | \ \ )(_(< | \  \  )(_( | No | 2.59 |
| 13 | (/_ <<_<  | (/_ <<_ | No | 3.15 |
| 14 | <(<_)/\ ) | <(<_)/\ ) | Yes | 1.95 |
| 15 | _)((()/ ( | _)((()/·( | No | 2.86 |
| 16 | \/\ ( <)/ | \/\ ( <)/ | Yes | 2.95 |
| 17 | \\ </ )_\ | \\ </ )_\ | Yes | 3.64 |
| 18 |  ))( ((   | )))(  (( | No | 2.81 |
| 19 |  (_/_()\( | (_/_()\( | No | 3.0 |
| 20 | (/ )<\\)_ | (/ )<\\)_ | Yes | 4.23 |
