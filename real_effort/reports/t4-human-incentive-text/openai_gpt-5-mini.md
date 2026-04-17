# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-27 10:46:15

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
| sudoku_game | 5481 | 40960 | 46441 | 0 | 20 | 71.18 | 1423.67 |
| add_numbers | 3240 | 3924 | 7164 | 20 | 0 | 6.52 | 130.46 |
| counting_zeros | 4640 | 38334 | 42974 | 9 | 11 | 35.44 | 708.84 |
| task_decoding | 4580 | 6305 | 10885 | 20 | 0 | 6.96 | 139.16 |
| task_summation | 4920 | 13176 | 18096 | 20 | 0 | 11.29 | 225.83 |
| task_transcription | 3388 | 4640 | 8028 | 20 | 0 | 4.21 | 84.27 |
| task_sequences | 3079 | 16634 | 19713 | 11 | 9 | 18.12 | 362.42 |
| string_entry | 3673 | 36615 | 40288 | 3 | 17 | 36.20 | 723.97 |
| **TOTAL** | **33001** | **160588** | **193589** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 1 5 5 6 1 3 2 2 2 5 3 1 |  | No | 73.49 |
| 2 | 2 4 6 3 5 1 6 5 2 2 6 4 3 6 |  | No | 64.64 |
| 3 | 4 3 1 5 5 4 2 1 2 3 5 4 2 5 |  | No | 74.89 |
| 4 | 6 3 1 1 6 5 1 4 6 2 3 4 1 2 |  | No | 69.07 |
| 5 | 4 3 6 1 3 2 2 1 5 4 3 1 5 6 |  | No | 58.99 |
| 6 | 6 5 4 1 6 2 5 5 3 1 3 1 6 4 |  | No | 68.19 |
| 7 | 2 6 5 4 1 6 5 2 2 4 3 2 5 4 |  | No | 67.32 |
| 8 | 4 5 3 6 4 4 3 5 1 2 6 2 3 1 |  | No | 63.61 |
| 9 | 5 6 6 1 2 2 6 6 1 6 3 2 3 4 |  | No | 78.15 |
| 10 | 2 6 5 5 6 2 6 5 3 1 2 6 3 2 |  | No | 73.65 |
| 11 | 5 6 5 3 6 4 6 2 3 4 1 3 2 1 |  | No | 62.17 |
| 12 | 1 4 2 3 6 6 1 4 6 3 4 5 6 1 |  | No | 64.77 |
| 13 | 6 4 2 5 6 3 4 6 4 1 2 2 3 6 |  | No | 68.26 |
| 14 | 2 5 4 2 6 4 3 2 6 4 5 6 3 2 |  | No | 61.67 |
| 15 | 6 2 3 1 4 5 2 3 3 1 4 5 6 2 |  | No | 67.15 |
| 16 | 6 1 3 5 2 5 2 3 1 1 5 2 5 4 |  | No | 96.07 |
| 17 | 4 2 1 2 3 4 3 2 5 4 6 3 5 3 |  | No | 98.94 |
| 18 | 1 4 1 2 5 3 4 5 2 3 3 4 1 4 |  | No | 69.5 |
| 19 | 3 1 5 2 3 6 3 4 5 6 4 5 6 3 |  | No | 63.64 |
| 20 | 2 4 3 3 6 4 5 2 1 3 1 5 2 3 |  | No | 79.47 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1346 | 1346 | Yes | 7.36 |
| 2 | 2011 | 2011 | Yes | 6.28 |
| 3 | 1798 | 1798 | Yes | 4.69 |
| 4 | 983 | 983 | Yes | 5.93 |
| 5 | 1905 | 1905 | Yes | 4.74 |
| 6 | 2338 | 2338 | Yes | 6.68 |
| 7 | 1398 | 1398 | Yes | 8.97 |
| 8 | 2011 | 2011 | Yes | 6.68 |
| 9 | 1840 | 1840 | Yes | 6.27 |
| 10 | 1256 | 1256 | Yes | 6.55 |
| 11 | 1809 | 1809 | Yes | 6.9 |
| 12 | 1343 | 1343 | Yes | 5.54 |
| 13 | 1994 | 1994 | Yes | 5.77 |
| 14 | 1614 | 1614 | Yes | 11.49 |
| 15 | 2417 | 2417 | Yes | 4.79 |
| 16 | 1984 | 1984 | Yes | 7.51 |
| 17 | 1083 | 1083 | Yes | 7.53 |
| 18 | 2071 | 2071 | Yes | 3.66 |
| 19 | 1696 | 1696 | Yes | 6.3 |
| 20 | 1480 | 1480 | Yes | 6.81 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 | 61 | Yes | 33.07 |
| 2 | 43 |  | No | 51.95 |
| 3 | 36 | 36 | Yes | 23.49 |
| 4 | 45 |  | No | 46.89 |
| 5 | 46 |  | No | 47.91 |
| 6 | 67 | 67 | Yes | 17.39 |
| 7 | 55 |  | No | 43.3 |
| 8 | 48 | 48 | Yes | 22.29 |
| 9 | 70 | 70 | Yes | 24.61 |
| 10 | 61 | 61 | Yes | 16.14 |
| 11 | 50 | 50 | Yes | 15.59 |
| 12 | 58 |  | No | 30.22 |
| 13 | 69 |  | No | 41.14 |
| 14 | 43 |  | No | 48.63 |
| 15 | 39 | 39 | Yes | 25.16 |
| 16 | 55 |  | No | 55.23 |
| 17 | 65 |  | No | 35.42 |
| 18 | 62 |  | No | 53.73 |
| 19 | 62 |  | No | 51.69 |
| 20 | 58 | 58 | Yes | 24.97 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FPIUTEV | FPIUTEV | Yes | 3.9 |
| 2 | OUBESPJ | OUBESPJ | Yes | 4.04 |
| 3 | BRYZVLM | BRYZVLM | Yes | 6.05 |
| 4 | LZNOCRB | LZNOCRB | Yes | 5.77 |
| 5 | ZHYPTUD | ZHYPTUD | Yes | 7.73 |
| 6 | ZXHOERB | ZXHOERB | Yes | 5.35 |
| 7 | IPFVQGL | IPFVQGL | Yes | 3.81 |
| 8 | WXMEAPZ | WXMEAPZ | Yes | 10.91 |
| 9 | ZHMQXOV | ZHMQXOV | Yes | 7.23 |
| 10 | AZCPWYH | AZCPWYH | Yes | 7.68 |
| 11 | RCTULQS | RCTULQS | Yes | 7.9 |
| 12 | ALPZCEH | ALPZCEH | Yes | 10.48 |
| 13 | WMOYUTJ | WMOYUTJ | Yes | 5.54 |
| 14 | NFQXHWM | NFQXHWM | Yes | 7.72 |
| 15 | HIXALQU | HIXALQU | Yes | 4.12 |
| 16 | YHBLQMW | YHBLQMW | Yes | 3.91 |
| 17 | YWJKURS | YWJKURS | Yes | 7.61 |
| 18 | KMZUIRO | KMZUIRO | Yes | 10.97 |
| 19 | UZDRIOE | UZDRIOE | Yes | 8.35 |
| 20 | JFWAREC | JFWAREC | Yes | 10.08 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.59 |
| 2 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.85 |
| 3 | [1.4, 8.6] | 8.6 1.4 | Yes | 10.02 |
| 4 | [3.5, 6.5] | 6.5 3.5 | Yes | 12.03 |
| 5 | [0.8, 9.2] | 9.2 0.8 | Yes | 14.91 |
| 6 | [4.0, 6.0] | 4.0 6.0 | Yes | 20.19 |
| 7 | [5.0, 5.0] | 5.0 5.0 | Yes | 10.36 |
| 8 | [3.2, 6.8] | 3.2 6.8 | Yes | 9.31 |
| 9 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.07 |
| 10 | [2.0, 8.0] | 8.0 2.0 | Yes | 8.85 |
| 11 | [4.6, 5.4] | 4.6 5.4 | Yes | 10.77 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.82 |
| 13 | [0.1, 9.9] | 0.1 9.9 | Yes | 12.23 |
| 14 | [3.6, 6.4] | 3.6 6.4 | Yes | 10.07 |
| 15 | [4.5, 5.5] | 4.5 5.5 | Yes | 12.33 |
| 16 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.73 |
| 17 | [2.9, 7.1] | 2.9 7.1 | Yes | 10.61 |
| 18 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.65 |
| 19 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.06 |
| 20 | [0.3, 9.7] | 0.3 9.7 | Yes | 14.36 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2IML4EKMO49U | 2IML4EKMO49U | Yes | 3.14 |
| 2 | 2032OCJO8X4I | 2032OCJO8X4I | Yes | 6.24 |
| 3 | MCXBEHCJMKMQ | MCXBEHCJMKMQ | Yes | 3.99 |
| 4 | U9GRT3RHDJ4J | U9GRT3RHDJ4J | Yes | 3.9 |
| 5 | ZD0VCSRA9KFY | ZD0VCSRA9KFY | Yes | 3.24 |
| 6 | FR5ARR3V1Y1S | FR5ARR3V1Y1S | Yes | 3.37 |
| 7 | KOGN50Z5KNSQ | KOGN50Z5KNSQ | Yes | 3.4 |
| 8 | IF9ITVUWW1HL | IF9ITVUWW1HL | Yes | 2.46 |
| 9 | KJJXD143TR9B | KJJXD143TR9B | Yes | 5.16 |
| 10 | Y5A35N1QI8JT | Y5A35N1QI8JT | Yes | 5.88 |
| 11 | RT8OZYUGKBUQ | RT8OZYUGKBUQ | Yes | 3.1 |
| 12 | W5X5ITL3ZY1C | W5X5ITL3ZY1C | Yes | 3.42 |
| 13 | 4BO9HJQ7O03C | 4BO9HJQ7O03C | Yes | 4.21 |
| 14 | ZP3G7XOW0ZRN | ZP3G7XOW0ZRN | Yes | 10.12 |
| 15 | QOQRSP6HP3M9 | QOQRSP6HP3M9 | Yes | 2.31 |
| 16 | T4IJV8T0YVDY | T4IJV8T0YVDY | Yes | 5.74 |
| 17 | B0ZTJE0XZKCY | B0ZTJE0XZKCY | Yes | 5.1 |
| 18 | 4685R3J210PR | 4685R3J210PR | Yes | 3.58 |
| 19 | W7GZFZFG67YU | W7GZFZFG67YU | Yes | 2.7 |
| 20 | U8RU218YE28M | U8RU218YE28M | Yes | 3.2 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4096 | 42 | No | 12.81 |
| 2 | 198 | 198 | Yes | 18.02 |
| 3 | 6 | 6 | Yes | 6.3 |
| 4 | 31 | 31 | Yes | 12.87 |
| 5 | 63 | 63 | Yes | 22.33 |
| 6 | 9 | 42 | No | 13.6 |
| 7 | 60 | 42 | No | 4.18 |
| 8 | 65 | 42 | No | 12.97 |
| 9 | 16 | 16 | Yes | 13.8 |
| 10 | 5 | TIMEOUT | No | 120.02 |
| 11 | 36 | 42 | No | 12.02 |
| 12 | 60 | 60 | Yes | 12.34 |
| 13 | 3 | 3 | Yes | 12.88 |
| 14 | 20 | 42 | No | 19.02 |
| 15 | 1440 | 1440 | Yes | 13.1 |
| 16 | 3 | 3 | Yes | 14.0 |
| 17 | 26 | 42 | No | 6.16 |
| 18 | 7680 | 7680 | Yes | 15.16 |
| 19 | 9 | 42 | No | 8.02 |
| 20 | 67 | 67 | Yes | 12.82 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _((//) () | /\) <(_<) | No | 26.86 |
| 2 | _/ \(\/)) | _/ \(\/)) | Yes | 22.03 |
| 3 | _\ /<_ (/ |  | No | 44.43 |
| 4 | <<__( )\( | <<__( )\( | Yes | 11.91 |
| 5 | ((\<) )\< |  | No | 38.22 |
| 6 | /)_<___ ( |  | No | 66.66 |
| 7 | ()(/_((_( | /\) <(_<) | No | 21.15 |
| 8 | / )((_(\  | / )((_(\ | No | 14.44 |
| 9 | _/( _\<_  |  | No | 29.37 |
| 10 | ___)<(\\/ |  | No | 48.86 |
| 11 |  )<)<)\ \ |  | No | 26.47 |
| 12 | _\_(/ \<_ |  | No | 48.01 |
| 13 | <)((<\ << |  | No | 57.09 |
| 14 | _((/)(    | /\) <(_<) | No | 22.3 |
| 15 | /() /\(// | /() /\(// | Yes | 17.46 |
| 16 | /<_\  ___ |  | No | 51.89 |
| 17 | \_/\//(\  |  | No | 41.78 |
| 18 | \(_)_<_(( | /\) <(_<) | No | 20.88 |
| 19 | \((_\)\(  |  | No | 57.26 |
| 20 | \/</_\(_) |  | No | 56.9 |
