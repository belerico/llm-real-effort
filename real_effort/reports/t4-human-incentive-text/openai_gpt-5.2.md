# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-27 10:14:17

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
| sudoku_game | 5224 | 22314 | 27538 | 14 | 6 | 29.35 | 587.11 |
| add_numbers | 3240 | 740 | 3980 | 20 | 0 | 3.25 | 65.0 |
| counting_zeros | 4640 | 16759 | 21399 | 20 | 0 | 16.04 | 320.92 |
| task_decoding | 4580 | 2292 | 6872 | 20 | 0 | 5.07 | 101.33 |
| task_summation | 4920 | 3203 | 8123 | 20 | 0 | 6.39 | 127.82 |
| task_transcription | 3389 | 903 | 4292 | 20 | 0 | 2.40 | 48.06 |
| task_sequences | 3079 | 4725 | 7804 | 18 | 2 | 14.85 | 297.04 |
| string_entry | 3684 | 14171 | 17855 | 3 | 17 | 16.70 | 333.94 |
| **TOTAL** | **32756** | **65107** | **97863** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 2 1 4 5 3 4 5 2 5 5 4 2 1 | 5 2 1 4 5 3 4 5 2 5 5 4 2 1 | Yes | 16.89 |
| 2 | 2 6 1 6 2 4 6 2 1 6 6 1 5 2 | 2 6 1 6 2 4 6 2 1 6 6 1 5 2 | Yes | 17.42 |
| 3 | 3 5 4 5 4 6 3 5 6 3 5 6 4 5 | 3 5 4 5 4 6 3 5 6 3 5 6 4 5 | Yes | 15.02 |
| 4 | 1 3 1 4 2 5 5 4 2 3 2 2 3 1 | TIMEOUT | No | 120.03 |
| 5 | 2 4 5 4 1 2 1 5 4 5 1 3 2 6 | 2 4 5 4 1 2 1 5 4 5 1 3 2 6 | Yes | 25.44 |
| 6 | 4 2 6 5 5 3 2 3 6 2 1 5 4 2 |  | No | 73.33 |
| 7 | 5 2 4 6 3 5 2 3 5 1 6 5 4 2 | 5 2 4 6 3 5 2 3 5 1 6 5 4 2 | Yes | 17.83 |
| 8 | 5 2 3 6 4 5 6 2 4 3 6 1 3 5 | 5 3 6 2 4 5 2 6 4 6 3 1 3 5 | No | 16.61 |
| 9 | 5 6 2 3 2 3 4 1 3 4 6 3 4 5 | 5 6 2 3 2 3 4 1 3 4 6 3 4 5 | Yes | 15.83 |
| 10 | 2 1 2 4 6 3 3 1 5 4 1 6 1 3 | 2 1 2 4 6 3 3 1 5 4 1 6 1 3 | Yes | 13.76 |
| 11 | 3 5 6 4 3 2 6 3 3 2 4 6 3 1 | 3 5 6 4 3 2 6 3 3 2 4 6 3 1 | Yes | 16.62 |
| 12 | 2 3 1 1 2 6 4 6 1 3 2 1 1 2 | 2 3 1 1 2 6 4 6 1 3 2 1 1 2 | Yes | 25.05 |
| 13 | 3 6 6 2 5 3 3 2 5 6 4 5 3 2 |  | No | 62.79 |
| 14 | 2 4 4 3 1 5 4 4 2 6 2 3 4 1 |  | No | 33.27 |
| 15 | 2 6 1 3 1 6 5 2 2 4 2 5 4 2 | 2 6 1 3 1 6 5 2 2 4 2 5 4 2 | Yes | 16.32 |
| 16 | 2 4 3 1 4 4 3 4 5 2 1 6 4 3 | 2 4 3 1 4 4 3 4 5 2 1 6 4 3 | Yes | 19.29 |
| 17 | 5 3 2 1 5 2 6 1 3 2 4 4 3 1 | 5 3 2 1 5 2 6 1 3 2 4 4 3 1 | Yes | 14.04 |
| 18 | 3 2 6 1 4 1 4 6 2 5 1 5 2 2 | 3 2 6 1 4 1 4 6 2 5 1 5 2 2 | Yes | 16.64 |
| 19 | 6 5 3 1 2 2 5 6 1 6 5 3 2 5 |  | No | 33.44 |
| 20 | 5 1 1 6 3 5 3 4 2 4 1 1 6 3 | 5 1 1 6 3 5 3 4 2 4 1 1 6 3 | Yes | 17.43 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1997 | 1997 | Yes | 3.11 |
| 2 | 1627 | 1627 | Yes | 4.03 |
| 3 | 1655 | 1655 | Yes | 3.46 |
| 4 | 694 | 694 | Yes | 3.26 |
| 5 | 1849 | 1849 | Yes | 3.45 |
| 6 | 1792 | 1792 | Yes | 1.53 |
| 7 | 1635 | 1635 | Yes | 4.0 |
| 8 | 1522 | 1522 | Yes | 1.81 |
| 9 | 1615 | 1615 | Yes | 3.21 |
| 10 | 1537 | 1537 | Yes | 2.86 |
| 11 | 2165 | 2165 | Yes | 3.63 |
| 12 | 1427 | 1427 | Yes | 3.27 |
| 13 | 1180 | 1180 | Yes | 2.94 |
| 14 | 2381 | 2381 | Yes | 3.14 |
| 15 | 2050 | 2050 | Yes | 3.61 |
| 16 | 1960 | 1960 | Yes | 3.42 |
| 17 | 1843 | 1843 | Yes | 3.14 |
| 18 | 1919 | 1919 | Yes | 4.1 |
| 19 | 2258 | 2258 | Yes | 3.15 |
| 20 | 1948 | 1948 | Yes | 3.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 | 59 | Yes | 17.13 |
| 2 | 65 | 65 | Yes | 20.6 |
| 3 | 71 | 71 | Yes | 15.29 |
| 4 | 58 | 58 | Yes | 17.06 |
| 5 | 54 | 54 | Yes | 19.16 |
| 6 | 55 | 55 | Yes | 19.2 |
| 7 | 50 | 50 | Yes | 17.94 |
| 8 | 54 | 54 | Yes | 18.73 |
| 9 | 37 | 37 | Yes | 14.45 |
| 10 | 67 | 67 | Yes | 15.85 |
| 11 | 67 | 67 | Yes | 12.09 |
| 12 | 60 | 60 | Yes | 14.5 |
| 13 | 48 | 48 | Yes | 9.7 |
| 14 | 54 | 54 | Yes | 10.98 |
| 15 | 55 | 55 | Yes | 14.42 |
| 16 | 50 | 50 | Yes | 17.65 |
| 17 | 61 | 61 | Yes | 16.95 |
| 18 | 64 | 64 | Yes | 15.72 |
| 19 | 64 | 64 | Yes | 18.94 |
| 20 | 53 | 53 | Yes | 14.54 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PMSLEUG | PMSLEUG | Yes | 4.08 |
| 2 | GKEHYSV | GKEHYSV | Yes | 2.7 |
| 3 | RDGNSWL | RDGNSWL | Yes | 5.28 |
| 4 | IOHSTBJ | IOHSTBJ | Yes | 6.75 |
| 5 | BFYGENA | BFYGENA | Yes | 5.86 |
| 6 | AGEBUNJ | AGEBUNJ | Yes | 3.78 |
| 7 | NEVALGS | NEVALGS | Yes | 5.05 |
| 8 | NRALGUX | NRALGUX | Yes | 5.25 |
| 9 | HZAONVG | HZAONVG | Yes | 3.99 |
| 10 | JXRAGIP | JXRAGIP | Yes | 4.07 |
| 11 | SLFZWJR | SLFZWJR | Yes | 5.23 |
| 12 | HAYOGDK | HAYOGDK | Yes | 3.64 |
| 13 | JCNTHLM | JCNTHLM | Yes | 5.7 |
| 14 | BTWVLHP | BTWVLHP | Yes | 5.22 |
| 15 | NQFTEHW | NQFTEHW | Yes | 7.81 |
| 16 | QJLTHXK | QJLTHXK | Yes | 4.61 |
| 17 | DNWTVFL | DNWTVFL | Yes | 5.96 |
| 18 | DZRCOJE | DZRCOJE | Yes | 4.52 |
| 19 | ZGWMLHY | ZGWMLHY | Yes | 5.62 |
| 20 | TSBUWKI | TSBUWKI | Yes | 6.19 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 0.6 9.4 | Yes | 5.89 |
| 2 | [1.1, 8.9] | 1.1 8.9 | Yes | 7.93 |
| 3 | [2.0, 8.0] | 2.0 8.0 | Yes | 5.18 |
| 4 | [0.6, 9.4] | 9.4 0.6 | Yes | 8.4 |
| 5 | [2.8, 7.2] | 7.2 2.8 | Yes | 4.35 |
| 6 | [4.3, 5.7] | 4.3 5.7 | Yes | 4.54 |
| 7 | [2.9, 7.1] | 7.1 2.9 | Yes | 9.03 |
| 8 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.14 |
| 9 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.08 |
| 10 | [1.2, 8.8] | 8.8 1.2 | Yes | 9.25 |
| 11 | [1.6, 8.4] | 8.4 1.6 | Yes | 5.41 |
| 12 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.51 |
| 13 | [2.9, 7.1] | 2.9 7.1 | Yes | 8.94 |
| 14 | [4.4, 5.6] | 4.4 5.6 | Yes | 4.26 |
| 15 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.95 |
| 16 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.98 |
| 17 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.81 |
| 18 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.3 |
| 19 | [2.4, 7.6] | 7.6 2.4 | Yes | 6.28 |
| 20 | [1.9, 8.1] | 1.9 8.1 | Yes | 6.59 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OKZ3D2D1B7YK | OKZ3D2D1B7YK | Yes | 1.65 |
| 2 | IT9VG8GKCF01 | IT9VG8GKCF01 | Yes | 1.5 |
| 3 | IWM0W6H9R1CA | IWM0W6H9R1CA | Yes | 4.22 |
| 4 | XPJ0J6G1RZ1Y | XPJ0J6G1RZ1Y | Yes | 3.87 |
| 5 | MFI58P9HJ76E | MFI58P9HJ76E | Yes | 1.68 |
| 6 | RVRDFVV8CCDA | RVRDFVV8CCDA | Yes | 1.51 |
| 7 | BLC6MA0ZO98J | BLC6MA0ZO98J | Yes | 5.7 |
| 8 | NXDJPV78SDMH | NXDJPV78SDMH | Yes | 1.81 |
| 9 | G21X7A5OWTN5 | G21X7A5OWTN5 | Yes | 1.23 |
| 10 | 6KRWA9OM6RMQ | 6KRWA9OM6RMQ | Yes | 4.11 |
| 11 | EHI77N4VDAHR | EHI77N4VDAHR | Yes | 1.79 |
| 12 | E16DCIDJBMD7 | E16DCIDJBMD7 | Yes | 1.65 |
| 13 | 3K0GO8FKX33V | 3K0GO8FKX33V | Yes | 3.9 |
| 14 | ODNAG306B6KU | ODNAG306B6KU | Yes | 1.77 |
| 15 | BG2HQODIWS4D | BG2HQODIWS4D | Yes | 3.91 |
| 16 | ZVW6YRKONZ5P | ZVW6YRKONZ5P | Yes | 1.47 |
| 17 | KH81MS76TF6T | KH81MS76TF6T | Yes | 1.65 |
| 18 | OQDXDAU2OBCF | OQDXDAU2OBCF | Yes | 0.98 |
| 19 | C7K0IXJLE8G1 | C7K0IXJLE8G1 | Yes | 1.86 |
| 20 | Z1LUG0WVDXK9 | Z1LUG0WVDXK9 | Yes | 1.79 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 3.09 |
| 2 | 1440 | 1440 | Yes | 4.63 |
| 3 | 60 | 60 | Yes | 4.77 |
| 4 | 793 | 793 | Yes | 3.86 |
| 5 | 28 | 28 | Yes | 5.24 |
| 6 | 9 | 9 | Yes | 6.49 |
| 7 | 4 | 4 | Yes | 4.2 |
| 8 | 31 | TIMEOUT | No | 120.02 |
| 9 | 39 | 39 | Yes | 5.54 |
| 10 | 60 | 60 | Yes | 4.25 |
| 11 | 4096 | 4096 | Yes | 19.65 |
| 12 | 48 | 48 | Yes | 4.04 |
| 13 | 19 | 19 | Yes | 5.29 |
| 14 | 5 | 5 | Yes | 6.22 |
| 15 | 26 | 26 | Yes | 15.86 |
| 16 | 65 | 65 | Yes | 4.79 |
| 17 | 63 | 63 | Yes | 3.44 |
| 18 | 64 | 64 | Yes | 7.43 |
| 19 | 3 | 3 | Yes | 6.23 |
| 20 | 20 |  | No | 61.98 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |   /<<\<</ |  | No | 70.4 |
| 2 | \ <<\))_/ | /\) <(_<) <<\))_/ | No | 22.02 |
| 3 |  /< _<(() | /< _<(() | No | 11.17 |
| 4 | \_<   _\  | \_<   _\ | No | 9.99 |
| 5 | /\_/\_< / | /\_/\_< / | Yes | 3.57 |
| 6 | \)//(\) _ | /\) <(_<) | No | 23.26 |
| 7 | )<((\<\<< | /\) <(_<) | No | 31.12 |
| 8 | <\ < _(/\ | <\ < _(/\ | Yes | 17.23 |
| 9 | () )_/(_( | /\) <(_<) | No | 8.22 |
| 10 | )/\)_ <</ | )/\)_ <</ | Yes | 3.75 |
| 11 | <)\_\/\<_ | /\) <(_<) | No | 10.37 |
| 12 |  )/_ /<<_ | /\) <(_<) )/_ /<<_ | No | 19.13 |
| 13 |   )(_<_(  | )(_<_( | No | 6.56 |
| 14 |   \//(\\  | \//(\\ | No | 17.74 |
| 15 | _ /<//)(( | /\) <(_<) | No | 7.75 |
| 16 | \/(/\)<)_ | /\) <(_<) | No | 13.94 |
| 17 | _()(_\(<\ | /\) <(_<) | No | 20.68 |
| 18 |  /\/(\_)\ | /\) <(_<) | No | 14.3 |
| 19 | \  (\_)\/ | /\) <(_<) | No | 11.85 |
| 20 | <_())\)<< | /\) <(_<) | No | 10.89 |
