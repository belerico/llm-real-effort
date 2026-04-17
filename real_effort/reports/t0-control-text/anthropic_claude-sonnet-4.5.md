# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-26 15:45:01

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
| sudoku_game | 5799 | 34194 | 39993 | 10 | 10 | 25.31 | 506.28 |
| add_numbers | 3180 | 3487 | 6667 | 20 | 0 | 4.55 | 91.06 |
| counting_zeros | 4500 | 19131 | 23631 | 1 | 19 | 12.60 | 252.06 |
| task_decoding | 4500 | 6204 | 10704 | 19 | 1 | 5.52 | 110.42 |
| task_summation | 4560 | 13095 | 17655 | 20 | 0 | 9.68 | 193.7 |
| task_transcription | 3356 | 2545 | 5901 | 20 | 0 | 4.85 | 97.1 |
| task_sequences | 3241 | 8539 | 11780 | 17 | 3 | 8.32 | 166.45 |
| string_entry | 3706 | 4008 | 7714 | 12 | 8 | 5.04 | 100.73 |
| **TOTAL** | **32842** | **91203** | **124045** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 2 2 3 5 3 1 5 4 6 3 1 3 | 4 1 2 1 2 3 2 5 3 1 5 4 6 3 1 3 | No | 23.67 |
| 2 | 4 4 2 5 3 3 6 1 2 5 6 1 4 3 | 4 3 4 5 2 3 6 1 2 5 6 1 4 3 | No | 21.3 |
| 3 | 2 1 5 2 6 5 2 4 1 4 6 3 5 3 | 2 1 5 2 6 5 2 4 1 4 6 3 5 3 | Yes | 28.99 |
| 4 | 1 5 6 4 4 6 1 3 5 3 2 2 5 6 | 1 5 6 4 4 6 1 3 5 3 2 2 5 6 | Yes | 20.07 |
| 5 | 2 3 1 5 3 1 4 5 2 4 3 1 6 4 | 2 3 1 5 3 1 4 5 2 4 3 1 6 4 | Yes | 26.11 |
| 6 | 1 4 4 1 4 3 2 3 5 6 6 2 5 2 | 1 4 4 1 4 3 2 3 5 6 6 2 5 2 | Yes | 26.64 |
| 7 | 2 6 1 3 3 6 5 4 2 5 4 1 4 6 | 2 6 1 3 3 6 5 4 2 5 4 1 4 6 | Yes | 28.37 |
| 8 | 1 1 5 6 2 6 4 3 1 1 5 3 6 4 | 1 1 5 6 2 6 4 3 1 1 5 3 6 4 | Yes | 22.01 |
| 9 | 1 3 2 5 6 3 5 6 6 5 2 4 3 1 | 3 1 2 5 6 3 5 6 6 5 2 4 1 3 | No | 24.87 |
| 10 | 2 1 6 5 2 1 3 6 4 2 3 4 3 1 | 2 6 5 2 1 3 6 4 2 3 4 3 1 | No | 23.15 |
| 11 | 4 5 3 2 6 3 4 5 6 3 4 6 1 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step.  Starting with the given numbers: ``` . . . \| . . 1 . 1 . \| 6 . 2 -----+----- . 2 1 \| 5 . . 2 . 5 \| 4 . 3 -----+----- 5 . 2 \| 1 4 6 1 4 6 \| 3 2 5 ```  Let me work through the logic:  **Row 6 | No | 32.7 |
| 12 | 1 4 1 5 1 6 3 2 1 2 6 1 5 2 | 1 4 1 5 1 6 3 2 1 2 6 1 5 2 | Yes | 19.62 |
| 13 | 4 1 6 3 2 1 6 2 6 1 5 2 6 4 | 4 1 6 3 2 1 6 2 6 1 5 2 6 4 | Yes | 21.24 |
| 14 | 5 2 1 6 4 5 2 4 1 3 6 4 4 3 | 5 2 1 6 4 5 4 2 1 3 6 4 4 3 | No | 23.72 |
| 15 | 2 5 6 1 3 4 3 5 1 4 4 1 4 3 | 2 5 6 1 3 4 1 5 3 4 4 3 4 1 | No | 22.24 |
| 16 | 5 4 2 6 1 6 5 3 1 6 2 5 4 3 | 5 4 6 2 1 6 5 3 1 2 6 5 4 3 | No | 24.97 |
| 17 | 4 4 1 3 4 5 3 5 4 3 1 2 4 1 | 4 4 1 3 4 5 3 5 4 3 1 2 4 1 | Yes | 28.77 |
| 18 | 3 5 1 4 2 3 5 4 6 2 1 6 5 4 | 3 5 1 4 2 3 5 4 6 2 1 6 5 4 | Yes | 26.85 |
| 19 | 2 1 6 2 5 1 4 5 2 5 2 3 2 1 | 1 2 2 5 6 5 4 1 6 2 5 2 1 | No | 27.94 |
| 20 | 2 6 4 3 2 1 1 3 5 6 5 6 4 3 |  | No | 33.02 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2332 | 2332 | Yes | 3.84 |
| 2 | 2042 | 2042 | Yes | 4.37 |
| 3 | 1987 | 1987 | Yes | 3.63 |
| 4 | 1188 | 1188 | Yes | 4.41 |
| 5 | 1677 | 1677 | Yes | 4.9 |
| 6 | 1887 | 1887 | Yes | 6.78 |
| 7 | 2018 | 2018 | Yes | 3.71 |
| 8 | 2090 | 2090 | Yes | 3.9 |
| 9 | 1488 | 1488 | Yes | 4.24 |
| 10 | 1213 | 1213 | Yes | 4.68 |
| 11 | 1354 | 1354 | Yes | 3.0 |
| 12 | 2645 | 2645 | Yes | 4.12 |
| 13 | 1809 | 1809 | Yes | 9.06 |
| 14 | 898 | 898 | Yes | 3.04 |
| 15 | 1840 | 1840 | Yes | 4.94 |
| 16 | 726 | 726 | Yes | 3.77 |
| 17 | 1593 | 1593 | Yes | 6.35 |
| 18 | 1731 | 1731 | Yes | 4.32 |
| 19 | 986 | 986 | Yes | 4.62 |
| 20 | 1716 | 1716 | Yes | 3.39 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 51 | 48 | No | 18.5 |
| 2 | 59 | 55 | No | 13.95 |
| 3 | 39 | 35 | No | 9.61 |
| 4 | 37 | 36 | No | 14.27 |
| 5 | 48 | 37 | No | 8.13 |
| 6 | 41 | 41 | Yes | 13.8 |
| 7 | 47 | 35 | No | 11.35 |
| 8 | 75 | 68 | No | 11.19 |
| 9 | 55 | 54 | No | 7.94 |
| 10 | 50 | 41 | No | 8.33 |
| 11 | 48 | 43 | No | 11.18 |
| 12 | 46 | 40 | No | 11.61 |
| 13 | 63 | 61 | No | 12.2 |
| 14 | 45 | 42 | No | 11.54 |
| 15 | 72 | 64 | No | 16.87 |
| 16 | 48 | 42 | No | 20.83 |
| 17 | 46 | 47 | No | 17.09 |
| 18 | 72 | 60 | No | 12.18 |
| 19 | 44 | 38 | No | 8.78 |
| 20 | 60 | 57 | No | 12.7 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RGHKCOW | RGHKCOW | Yes | 4.55 |
| 2 | PQSDNGI | PQSDNGI | Yes | 6.45 |
| 3 | JPSOMZT | JPSOMZT | Yes | 5.67 |
| 4 | EWYVXAH | EWYVXAH | Yes | 5.06 |
| 5 | JZQGRMN | JZQGRMN | Yes | 6.33 |
| 6 | MKVUWCA | MKVUWCA | Yes | 6.2 |
| 7 | UTMXOSC | UTMXOSC | Yes | 5.62 |
| 8 | LGPJTFZ | LGPJTFZ | Yes | 5.52 |
| 9 | WLYTGRJ | WLYTGRJ | Yes | 5.66 |
| 10 | TVOMAUB | TVOMAUB | Yes | 5.23 |
| 11 | WLCZVKQ | WLCZVKQ | Yes | 5.71 |
| 12 | OTCIBVA | OTCIBVA | Yes | 7.49 |
| 13 | QLUMXPW | QLUMXPW | Yes | 5.35 |
| 14 | YSPFAJU | YSPFAJU | Yes | 5.18 |
| 15 | WDQPYTR | WDQPYTR | Yes | 4.72 |
| 16 | MOSTZAU | MOSTZAU | Yes | 4.8 |
| 17 | LWGTAHK | LWGTAHK | Yes | 6.18 |
| 18 | DHJQVNK | DHJQVNK | Yes | 4.8 |
| 19 | IVSZBAG | IVSZABG | No | 4.23 |
| 20 | QXAGIYB | QXAGIYB | Yes | 5.63 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.0, 9.0] | 9.0 1.0 | Yes | 12.51 |
| 2 | [2.0, 8.0] | 8.0 2.0 | Yes | 7.32 |
| 3 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.87 |
| 4 | [1.0, 9.0] | 9.0 1.0 | Yes | 8.48 |
| 5 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.25 |
| 6 | [0.6, 9.4] | 0.6 9.4 | Yes | 14.67 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 8.55 |
| 8 | [2.6, 7.4] | 7.4 2.6 | Yes | 8.4 |
| 9 | [1.9, 8.1] | 1.9 8.1 | Yes | 16.45 |
| 10 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.13 |
| 11 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.5 |
| 12 | [1.4, 8.6] | 1.4 8.6 | Yes | 8.02 |
| 13 | [1.5, 8.5] | 8.5 1.5 | Yes | 6.61 |
| 14 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.91 |
| 15 | [1.4, 8.6] | 1.4 8.6 | Yes | 8.97 |
| 16 | [3.4, 6.6] | 6.6 3.4 | Yes | 12.67 |
| 17 | [4.4, 5.6] | 5.6 4.4 | Yes | 9.39 |
| 18 | [4.4, 5.6] | 5.6 4.4 | Yes | 9.6 |
| 19 | [0.4, 9.6] | 9.6 0.4 | Yes | 8.97 |
| 20 | [0.3, 9.7] | 9.7 0.3 | Yes | 7.43 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9LCHQAXY2LER | 9LCHQAXY2LER | Yes | 6.23 |
| 2 | SC3U8D1WT4OQ | SC3U8D1WT4OQ | Yes | 4.31 |
| 3 | 16YS6U3G6A0D | 16YS6U3G6A0D | Yes | 4.63 |
| 4 | FIUTLLNBX5RH | FIUTLLNBX5RH | Yes | 5.01 |
| 5 | 74S6P1DWJZNC | 74S6P1DWJZNC | Yes | 5.52 |
| 6 | 9TRLC7PZR5S3 | 9TRLC7PZR5S3 | Yes | 4.51 |
| 7 | UEBFCDSMVPBH | UEBFCDSMVPBH | Yes | 8.92 |
| 8 | G7H6ZKB34X6C | G7H6ZKB34X6C | Yes | 8.18 |
| 9 | VCJH5TPX9BN1 | VCJH5TPX9BN1 | Yes | 2.8 |
| 10 | JW4G2ST5M1SI | JW4G2ST5M1SI | Yes | 3.55 |
| 11 | NX2ETJ1GW9B1 | NX2ETJ1GW9B1 | Yes | 3.35 |
| 12 | 1Z1YGZX5R4Z0 | 1Z1YGZX5R4Z0 | Yes | 4.35 |
| 13 | 0Q5N7MWB602B | 0Q5N7MWB602B | Yes | 7.07 |
| 14 | QRWIMYTSQWK2 | QRWIMYTSQWK2 | Yes | 3.63 |
| 15 | WQN7LR1GO9EQ | WQN7LR1GO9EQ | Yes | 3.58 |
| 16 | SDJNSJL58CEK | SDJNSJL58CEK | Yes | 3.8 |
| 17 | LJXY36IXLUZM | LJXY36IXLUZM | Yes | 4.01 |
| 18 | FEXO5O4F70T6 | FEXO5O4F70T6 | Yes | 2.9 |
| 19 | OI0ZU4H4JA8Y | OI0ZU4H4JA8Y | Yes | 6.48 |
| 20 | P6JA19S4JCWU | P6JA19S4JCWU | Yes | 4.25 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 20 | Yes | 10.55 |
| 2 | 4096 | 1048576 | No | 13.0 |
| 3 | 36 | 36 | Yes | 3.95 |
| 4 | 64 | 64 | Yes | 5.73 |
| 5 | 4 | 4 | Yes | 5.54 |
| 6 | 10 | 10 | Yes | 20.53 |
| 7 | 60 | 60 | Yes | 6.69 |
| 8 | 3 | 3 | Yes | 5.56 |
| 9 | 5 | 16 | No | 16.4 |
| 10 | 44 | 44 | Yes | 5.8 |
| 11 | 39 | 39 | Yes | 6.33 |
| 12 | 9 | 9 | Yes | 6.34 |
| 13 | 28 | 28 | Yes | 5.99 |
| 14 | 60 | 60 | Yes | 8.03 |
| 15 | 9 | 9 | Yes | 7.41 |
| 16 | 7 | 7 | Yes | 5.82 |
| 17 | 3 | 25 | No | 11.67 |
| 18 | 26 | 26 | Yes | 9.32 |
| 19 | 67 | 67 | Yes | 6.49 |
| 20 | 73 | 73 | Yes | 5.29 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( (<\(< ( | ( (<\(< ( | Yes | 4.2 |
| 2 | /\\/) \_\ | /\\/) \_\ | Yes | 4.51 |
| 3 | _\( \_<_< | _\( \_<_ | No | 3.8 |
| 4 |  \(<)_\ / | \(<)_\ / | No | 5.57 |
| 5 | \)\(((_<) | \)\(((_<) | Yes | 5.1 |
| 6 |  /\/<_<\_ | /\/<_<\_ | No | 5.22 |
| 7 | /<( ) _<  | /<( ) _ | No | 5.83 |
| 8 | )(/)\\<(  | )(/)\\<( | No | 5.86 |
| 9 |  _<<  \\_ | _<<  \\_ | No | 5.78 |
| 10 | </_)/_\)) | </_)/_\)) | Yes | 6.02 |
| 11 | < <(((/)( | < <(((/)( | Yes | 3.87 |
| 12 | (( /(_/(\ | (( /(_/(\ | Yes | 3.49 |
| 13 | <)/\)(_(/ | <)/\)(_(/ | Yes | 5.09 |
| 14 | _/ )())_< | _/ )())_ | No | 5.12 |
| 15 | )<)(/\<)\ | )<)(/\<)\ | Yes | 5.43 |
| 16 | \\( < / / | \\( < / / | Yes | 4.42 |
| 17 | <<()/<<)_ | <<()/<<)_ | Yes | 4.95 |
| 18 |  ()_<( )  | ()_<( ) | No | 6.74 |
| 19 | <(((__)(( | <(((__)(( | Yes | 3.7 |
| 20 | /_\) (\_\ | /_\) (\_\ | Yes | 6.0 |
