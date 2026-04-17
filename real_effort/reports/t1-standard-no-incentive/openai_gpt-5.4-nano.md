# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 11:03:31

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
| sudoku_game | 7020 | 40625 | 47645 | 3 | 17 | 44.16 | 883.41 |
| add_numbers | 3600 | 1621 | 5221 | 20 | 0 | 3.65 | 73.02 |
| counting_zeros | 6020 | 32665 | 38685 | 2 | 18 | 28.78 | 575.9 |
| task_decoding | 11760 | 4997 | 16757 | 20 | 0 | 6.06 | 121.51 |
| task_summation | 6960 | 6741 | 13701 | 20 | 0 | 6.34 | 126.95 |
| task_transcription | 3426 | 10571 | 13997 | 7 | 13 | 6.92 | 138.56 |
| task_sequences | 2721 | 15623 | 18344 | 15 | 5 | 12.75 | 255.08 |
| string_entry | 4020 | 32555 | 36575 | 5 | 15 | 35.02 | 700.41 |
| **TOTAL** | **45527** | **145398** | **190925** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 3 1 2 5 5 6 2 4 1 2 4 6 |  | No | 47.97 |
| 2 | 2 1 3 1 6 2 6 1 3 3 6 1 2 4 |  | No | 57.03 |
| 3 | 2 6 3 6 1 4 5 2 3 5 2 1 6 5 |  | No | 49.99 |
| 4 | 3 2 6 5 4 2 4 6 1 5 1 4 2 3 | 3 2 6 5 4 2 4 6 1 5 1 4 2 3 | Yes | 27.42 |
| 5 | 5 2 1 3 2 1 3 4 2 6 5 1 5 4 | 5 2 1 3 2 1 3 4 2 6 5 1 5 4 | Yes | 26.37 |
| 6 | 5 4 1 5 2 6 5 4 2 1 6 2 3 5 |  | No | 48.04 |
| 7 | 6 1 5 4 3 6 2 4 1 5 1 6 2 2 |  | No | 62.76 |
| 8 | 2 5 3 4 6 1 6 3 2 6 6 5 2 1 |  | No | 43.55 |
| 9 | 4 2 4 1 5 4 2 1 3 5 2 1 4 2 |  | No | 40.57 |
| 10 | 4 2 5 2 1 4 4 6 3 2 5 4 6 5 |  | No | 38.57 |
| 11 | 1 6 4 5 5 6 3 3 4 2 6 4 2 1 | 1 6 4 5 5 6 3 3 4 2 6 4 2 1 | Yes | 24.59 |
| 12 | 6 2 5 3 5 2 2 4 1 5 2 6 1 5 |  | No | 43.79 |
| 13 | 6 4 6 4 6 1 2 3 1 3 3 4 1 6 |  | No | 36.0 |
| 14 | 3 6 6 4 2 1 4 2 2 4 5 5 6 4 |  | No | 52.9 |
| 15 | 4 5 1 2 5 6 3 1 2 5 6 2 6 1 |  | No | 50.9 |
| 16 | 1 4 6 3 5 1 4 5 3 5 2 5 4 6 |  | No | 46.91 |
| 17 | 1 4 2 5 3 6 1 4 4 5 2 2 4 1 |  | No | 57.52 |
| 18 | 6 1 3 2 2 6 1 4 6 3 2 3 1 1 |  | No | 44.63 |
| 19 | 3 6 4 3 5 4 5 2 4 3 1 6 4 3 |  | No | 28.4 |
| 20 | 4 1 6 3 2 5 3 2 1 2 1 3 5 4 |  | No | 55.34 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2023 | 2023 | Yes | 3.22 |
| 2 | 1688 | 1688 | Yes | 3.53 |
| 3 | 1459 | 1459 | Yes | 3.47 |
| 4 | 1059 | 1059 | Yes | 3.36 |
| 5 | 1909 | 1909 | Yes | 2.92 |
| 6 | 2123 | 2123 | Yes | 3.41 |
| 7 | 1792 | 1792 | Yes | 4.49 |
| 8 | 1497 | 1497 | Yes | 2.94 |
| 9 | 2021 | 2021 | Yes | 5.08 |
| 10 | 1885 | 1885 | Yes | 3.69 |
| 11 | 1936 | 1936 | Yes | 2.2 |
| 12 | 2120 | 2120 | Yes | 2.93 |
| 13 | 889 | 889 | Yes | 1.64 |
| 14 | 1191 | 1191 | Yes | 4.26 |
| 15 | 1798 | 1798 | Yes | 3.69 |
| 16 | 1045 | 1045 | Yes | 3.06 |
| 17 | 1788 | 1788 | Yes | 6.55 |
| 18 | 1617 | 1617 | Yes | 3.32 |
| 19 | 1494 | 1494 | Yes | 3.87 |
| 20 | 1890 | 1890 | Yes | 5.29 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 67 | No | 25.5 |
| 2 | 67 | 67 | Yes | 29.14 |
| 3 | 59 |  | No | 59.16 |
| 4 | 38 | 67 | No | 19.5 |
| 5 | 67 | 67 | Yes | 23.75 |
| 6 | 46 | 67 | No | 16.66 |
| 7 | 61 |  | No | 48.36 |
| 8 | 64 |  | No | 62.35 |
| 9 | 36 | 67 | No | 23.84 |
| 10 | 50 | 67 | No | 22.72 |
| 11 | 39 | 67 | No | 20.58 |
| 12 | 66 | 67 | No | 22.13 |
| 13 | 60 | 67 | No | 22.26 |
| 14 | 37 | 67 | No | 28.96 |
| 15 | 62 | 67 | No | 17.75 |
| 16 | 50 | 67 | No | 21.98 |
| 17 | 47 | 67 | No | 16.42 |
| 18 | 47 | 67 | No | 12.48 |
| 19 | 62 | 67 | No | 13.98 |
| 20 | 58 |  | No | 68.05 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PHILDMO | PHILDMO | Yes | 10.91 |
| 2 | GKFXLQE | GKFXLQE | Yes | 4.98 |
| 3 | ZPXYVQL | ZPXYVQL | Yes | 6.62 |
| 4 | LFMZWXO | LFMZWXO | Yes | 4.87 |
| 5 | XTAYODB | XTAYODB | Yes | 5.07 |
| 6 | PFBXEWG | PFBXEWG | Yes | 4.03 |
| 7 | TSUYGRZ | TSUYGRZ | Yes | 5.69 |
| 8 | TZXKLQF | TZXKLQF | Yes | 4.72 |
| 9 | RWNCDMV | RWNCDMV | Yes | 5.8 |
| 10 | KTVXZYA | KTVXZYA | Yes | 5.17 |
| 11 | BKLTDES | BKLTDES | Yes | 9.62 |
| 12 | NHKWBJT | NHKWBJT | Yes | 4.34 |
| 13 | FEULBKY | FEULBKY | Yes | 4.42 |
| 14 | UBJTKZP | UBJTKZP | Yes | 9.93 |
| 15 | KXNABFY | KXNABFY | Yes | 7.52 |
| 16 | LPAKVXZ | LPAKVXZ | Yes | 4.24 |
| 17 | YEBNSPR | YEBNSPR | Yes | 4.87 |
| 18 | HBDYQGI | HBDYQGI | Yes | 6.24 |
| 19 | ZFLGTEA | ZFLGTEA | Yes | 6.92 |
| 20 | ZENOBMP | ZENOBMP | Yes | 5.33 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.1, 6.9] | 6.9 3.1 | Yes | 4.11 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 7.0 |
| 3 | [0.1, 9.9] | 0.1 9.9 | Yes | 5.98 |
| 4 | [0.6, 9.4] | 9.4 0.6 | Yes | 7.12 |
| 5 | [1.8, 8.2] | 1.8 8.2 | Yes | 6.91 |
| 6 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.55 |
| 7 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.82 |
| 8 | [0.7, 9.3] | 0.7 9.3 | Yes | 7.16 |
| 9 | [3.1, 6.9] | 3.1 6.9 | Yes | 7.72 |
| 10 | [4.4, 5.6] | 4.4 5.6 | Yes | 5.58 |
| 11 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.47 |
| 12 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.48 |
| 13 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.39 |
| 14 | [3.0, 7.0] | 7.0 3.0 | Yes | 5.62 |
| 15 | [1.6, 8.4] | 1.6 8.4 | Yes | 6.98 |
| 16 | [3.6, 6.4] | 6.4 3.6 | Yes | 6.69 |
| 17 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.81 |
| 18 | [2.9, 7.1] | 2.9 7.1 | Yes | 5.59 |
| 19 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.28 |
| 20 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.5 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | H2SVWMJMBYOV | H2SVWMJMBYOV | Yes | 5.85 |
| 2 | N61TMPLMWMV0 | N61TMPLMWNVO | No | 15.99 |
| 3 | ZRCVLEHL8LFD | ZRCVLEHL8LFD | Yes | 15.01 |
| 4 | YFSW3GAPP5RH | YFSW3GAPPSRH | No | 5.11 |
| 5 | Q7T6M7EQ43PX | Q7T6M7EQ43PX | Yes | 5.11 |
| 6 | AHWTX0RGKC8Y | AHWTXORGKC8Y | No | 6.07 |
| 7 | ZQI5747E59B1 | ZO15747E59B1 | No | 3.78 |
| 8 | 48Z314HPEUBS | 48Z314HPEUBS | Yes | 3.97 |
| 9 | 6RT70ZG008YL | 6RT7OZG008YL | No | 4.36 |
| 10 | J75CPJL6XKT7 | J75CPJL6XKT7 | Yes | 3.83 |
| 11 | DNZMYXKMF5E1 | DNZMYXKMFSE1 | No | 7.21 |
| 12 | YHVLPR0RYIBH | YHVLPPRBYIBH | No | 9.84 |
| 13 | OBY1MEU14WOM | OBY1MEU14WOM | Yes | 13.74 |
| 14 | 0RH6W9LU6SWU | 0RH6WSLUGSWU | No | 6.11 |
| 15 | EAXHJBSSJVSW | EAXHJBSSJVSJVW | No | 6.07 |
| 16 | 87KJ0VE58Z4D | 87KJ0VE5824D | No | 4.52 |
| 17 | 6ODF619ULNMY | 60DF619ULNMVY | No | 9.72 |
| 18 | 8BYFS39O9075 | 8BYFS3909075 | No | 4.11 |
| 19 | KEB4ICDUPXKS | KEB4ICDUPXKS | Yes | 3.83 |
| 20 | XL0TOQ8XSKML | XL0T008XSKML | No | 4.22 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 31 | 31 | Yes | 4.17 |
| 2 | 1 | 1 | Yes | 7.84 |
| 3 | 60 | 60 | Yes | 4.38 |
| 4 | 3 |  | No | 52.97 |
| 5 | 198 | 198 | Yes | 13.35 |
| 6 | 60 | 60 | Yes | 15.32 |
| 7 | 7 | 7 | Yes | 3.82 |
| 8 | 65 | 65 | Yes | 4.81 |
| 9 | 9 | 9 | Yes | 4.19 |
| 10 | 3 |  | No | 31.36 |
| 11 | 4096 | 4096 | Yes | 10.57 |
| 12 | 28 | 25 | No | 11.44 |
| 13 | 67 | 67 | Yes | 3.33 |
| 14 | 10 | 8 | No | 19.24 |
| 15 | 39 | 39 | Yes | 12.01 |
| 16 | 20 |  | No | 28.57 |
| 17 | 9 | 9 | Yes | 4.51 |
| 18 | 19 | 19 | Yes | 5.61 |
| 19 | 48 | 48 | Yes | 12.03 |
| 20 | 6 | 6 | Yes | 5.55 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ) _(\)</( | )__(\)</( | Yes | 16.72 |
| 2 | )/_/  \ < | )/_/  \  < | No | 16.82 |
| 3 | /) \_</_  |  | No | 58.45 |
| 4 |  < /( //_ | /\) <(_<) | No | 15.61 |
| 5 | )/\((/\)\ | )/\((/\)\ | Yes | 13.48 |
| 6 | _(\_< /\) | _(\_< /\) | Yes | 16.85 |
| 7 | (\<<< \(( |  | No | 47.46 |
| 8 |  (<_(<\\\ |  | No | 55.7 |
| 9 | )<_ \\\\) | )<_<\\\\) | No | 22.0 |
| 10 | \_\((<(_\ |  | No | 64.57 |
| 11 | \__<<<< ) |  | No | 62.26 |
| 12 |  ( / (<\\ |  | No | 34.8 |
| 13 | )  <(_))  | /\) <(_<) | No | 29.44 |
| 14 | <_() <//) |  | No | 57.3 |
| 15 |  )<\/(_ / |  | No | 50.44 |
| 16 | _)</)_//( | _)</)_//( | Yes | 27.14 |
| 17 | (__/(_)// | (__/(_)// | Yes | 8.59 |
| 18 | _(<_\)  < | _(<_ \)  < | No | 13.32 |
| 19 |  //\/(((_ | /\) <(_<) | No | 19.03 |
| 20 | _ _)_\< / |  | No | 70.37 |
