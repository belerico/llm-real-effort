# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-27 10:09:03

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
| sudoku_game | 5297 | 22382 | 27679 | 14 | 6 | 20.22 | 404.44 |
| add_numbers | 3060 | 856 | 3916 | 20 | 0 | 3.28 | 65.58 |
| counting_zeros | 4460 | 18541 | 23001 | 19 | 1 | 13.30 | 265.94 |
| task_decoding | 4400 | 2524 | 6924 | 20 | 0 | 5.14 | 102.81 |
| task_summation | 4740 | 5243 | 9983 | 20 | 0 | 6.59 | 131.9 |
| task_transcription | 3193 | 1426 | 4619 | 20 | 0 | 2.84 | 56.81 |
| task_sequences | 3060 | 4051 | 7111 | 19 | 1 | 7.56 | 151.24 |
| string_entry | 3506 | 20134 | 23640 | 9 | 11 | 20.15 | 403.07 |
| **TOTAL** | **31716** | **75157** | **106873** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 5 3 6 5 1 4 3 2 4 2 3 1 | 4 2 5 3 6 5 1 4 3 2 4 2 3 1 | Yes | 12.66 |
| 2 | 6 2 3 3 6 6 1 4 6 4 1 6 4 1 | 6 2 3 3 6 6 1 4 6 4 1 6 4 1 | Yes | 14.85 |
| 3 | 1 5 2 5 1 4 6 5 6 3 4 2 1 5 | 1 5 2 5 1 4 6 5 6 3 4 2 1 5 | Yes | 13.12 |
| 4 | 6 5 3 3 6 6 3 6 2 5 4 1 1 2 |  | No | 37.46 |
| 5 | 6 5 4 2 4 2 6 1 6 5 1 4 2 6 | 6 5 4 2 4 2 6 1 6 5 1 4 2 6 | Yes | 10.98 |
| 6 | 2 3 6 6 5 2 5 3 6 6 2 5 4 1 | 2 3 6 6 5 2 5 3 6 6 2 5 4 1 | Yes | 12.67 |
| 7 | 1 4 2 1 3 5 5 4 1 6 5 2 1 5 | 1 4 2 1 3 5 5 4 1 6 5 2 1 5 | Yes | 13.38 |
| 8 | 5 4 3 2 2 4 6 5 6 5 3 1 4 6 |  | No | 36.08 |
| 9 | 6 2 4 3 6 4 2 5 3 1 1 5 2 3 |  | No | 33.16 |
| 10 | 4 5 1 4 1 4 1 6 3 4 3 4 1 2 | 4 5 1 4 1 4 1 6 3 4 3 4 1 2 | Yes | 13.09 |
| 11 | 5 2 6 3 1 6 3 2 4 5 1 5 3 1 | 5 2 6 3 1 6 3 2 4 5 1 5 3 1 | Yes | 12.81 |
| 12 | 2 2 4 2 5 4 1 5 2 6 5 3 4 1 |  | No | 29.24 |
| 13 | 5 5 1 6 6 5 1 3 2 6 4 1 3 2 |  | No | 30.86 |
| 14 | 6 2 3 2 6 4 1 5 6 3 2 4 2 5 | 6 2 3 2 6 4 1 5 6 3 2 4 2 5 | Yes | 27.95 |
| 15 | 1 5 4 2 5 1 3 1 6 4 1 4 2 5 |  | No | 32.99 |
| 16 | 5 3 2 3 4 3 6 1 3 5 3 2 1 5 | 5 3 2 3 4 3 6 1 3 5 3 2 1 5 | Yes | 13.09 |
| 17 | 1 4 5 6 2 3 4 2 1 5 2 6 1 4 | 1 4 5 6 2 3 4 2 1 5 2 6 1 4 | Yes | 17.51 |
| 18 | 4 2 4 6 2 4 3 1 2 1 4 2 6 1 | 4 2 4 6 2 4 3 1 2 1 4 2 6 1 | Yes | 15.52 |
| 19 | 6 3 4 6 5 5 4 1 4 3 6 6 2 3 | 6 3 4 6 5 5 4 1 4 3 6 6 2 3 | Yes | 13.21 |
| 20 | 3 2 5 1 3 6 2 1 1 4 5 2 3 6 | 3 2 5 1 3 6 2 1 1 4 5 2 3 6 | Yes | 13.79 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2189 | 2189 | Yes | 4.65 |
| 2 | 1065 | 1065 | Yes | 3.32 |
| 3 | 1347 | 1347 | Yes | 3.12 |
| 4 | 1455 | 1455 | Yes | 3.79 |
| 5 | 1907 | 1907 | Yes | 1.17 |
| 6 | 1275 | 1275 | Yes | 3.82 |
| 7 | 1379 | 1379 | Yes | 3.25 |
| 8 | 1552 | 1552 | Yes | 2.74 |
| 9 | 1888 | 1888 | Yes | 2.89 |
| 10 | 2731 | 2731 | Yes | 3.08 |
| 11 | 2463 | 2463 | Yes | 4.29 |
| 12 | 1150 | 1150 | Yes | 2.8 |
| 13 | 1798 | 1798 | Yes | 4.07 |
| 14 | 1201 | 1201 | Yes | 3.41 |
| 15 | 1440 | 1440 | Yes | 3.0 |
| 16 | 1214 | 1214 | Yes | 3.72 |
| 17 | 1677 | 1677 | Yes | 3.23 |
| 18 | 1556 | 1556 | Yes | 3.06 |
| 19 | 1018 | 1018 | Yes | 3.16 |
| 20 | 1796 | 1796 | Yes | 3.03 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 | 37 | Yes | 14.97 |
| 2 | 73 | 73 | Yes | 12.95 |
| 3 | 48 | 48 | Yes | 11.73 |
| 4 | 66 | 66 | Yes | 11.61 |
| 5 | 62 | 62 | Yes | 13.4 |
| 6 | 44 | 44 | Yes | 13.83 |
| 7 | 58 | 58 | Yes | 16.11 |
| 8 | 41 | 41 | Yes | 11.47 |
| 9 | 66 | 66 | Yes | 11.46 |
| 10 | 55 | 55 | Yes | 9.64 |
| 11 | 45 | 45 | Yes | 11.13 |
| 12 | 74 | 74 | Yes | 12.08 |
| 13 | 50 | 50 | Yes | 14.75 |
| 14 | 71 | 71 | Yes | 13.22 |
| 15 | 63 | 63 | Yes | 10.96 |
| 16 | 40 | 40 | Yes | 13.36 |
| 17 | 62 | 62 | Yes | 12.3 |
| 18 | 71 | 71 | Yes | 13.9 |
| 19 | 55 | 55 | Yes | 11.35 |
| 20 | 51 |  | No | 25.72 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PEWIYKO | PEWIYKO | Yes | 4.15 |
| 2 | CLPZMIW | CLPZMIW | Yes | 2.37 |
| 3 | TZHVMOS | TZHVMOS | Yes | 4.73 |
| 4 | FYXMTUC | FYXMTUC | Yes | 5.63 |
| 5 | QVSKHXT | QVSKHXT | Yes | 5.13 |
| 6 | VWOFLXY | VWOFLXY | Yes | 6.09 |
| 7 | CJRAXOY | CJRAXOY | Yes | 6.66 |
| 8 | XQUZATE | XQUZATE | Yes | 3.9 |
| 9 | HPXGMOT | HPXGMOT | Yes | 5.69 |
| 10 | CUHJTRI | CUHJTRI | Yes | 7.33 |
| 11 | YDJCPGX | YDJCPGX | Yes | 6.57 |
| 12 | VPLOIQK | VPLOIQK | Yes | 7.36 |
| 13 | LBFWNQJ | LBFWNQJ | Yes | 6.15 |
| 14 | WLRUTNV | WLRUTNV | Yes | 3.19 |
| 15 | DWRHCUJ | DWRHCUJ | Yes | 4.37 |
| 16 | BXWRPZD | BXWRPZD | Yes | 6.01 |
| 17 | GBFRTXA | GBFRTXA | Yes | 5.7 |
| 18 | LSBMPHO | LSBMPHO | Yes | 4.16 |
| 19 | BLKWEXY | BLKWEXY | Yes | 2.95 |
| 20 | JWUQOPG | JWUQOPG | Yes | 4.65 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.8, 7.2] | 2.8 7.2 | Yes | 5.92 |
| 2 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.41 |
| 3 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.58 |
| 4 | [2.9, 7.1] | 7.1 2.9 | Yes | 7.36 |
| 5 | [1.3, 8.7] | 8.7 1.3 | Yes | 5.84 |
| 6 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.6 |
| 7 | [0.2, 9.8] | 0.2 9.8 | Yes | 8.69 |
| 8 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.38 |
| 9 | [4.0, 6.0] | 4.0 6.0 | Yes | 6.76 |
| 10 | [2.5, 7.5] | 7.5 2.5 | Yes | 6.03 |
| 11 | [4.0, 6.0] | 4.0 6.0 | Yes | 5.4 |
| 12 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.71 |
| 13 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.7 |
| 14 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.82 |
| 15 | [3.1, 6.9] | 3.1 6.9 | Yes | 6.13 |
| 16 | [0.8, 9.2] | 9.2 0.8 | Yes | 5.98 |
| 17 | [0.1, 9.9] | 0.1 9.9 | Yes | 6.0 |
| 18 | [3.2, 6.8] | 6.8 3.2 | Yes | 4.71 |
| 19 | [1.8, 8.2] | 8.2 1.8 | Yes | 8.05 |
| 20 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.82 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | V1GN9Z06DB7R | V1GN9Z06DB7R | Yes | 3.84 |
| 2 | YUMWJV29GTVP | YUMWJV29GTVP | Yes | 3.54 |
| 3 | WPMAS27EKZAR | WPMAS27EKZAR | Yes | 1.56 |
| 4 | HQC4IQ0YWRM7 | HQC4IQ0YWRM7 | Yes | 4.53 |
| 5 | VA1PTT0BAUX0 | VA1PTT0BAUX0 | Yes | 4.55 |
| 6 | 4TANLAYDUG46 | 4TANLAYDUG46 | Yes | 3.72 |
| 7 | Y9U07KMWFRZT | Y9U07KMWFRZT | Yes | 2.74 |
| 8 | 52ICVP43ZKZW | 52ICVP43ZKZW | Yes | 1.93 |
| 9 | I9JBB5P9X6G2 | I9JBB5P9X6G2 | Yes | 2.46 |
| 10 | MPXSAT4S86RH | MPXSAT4S86RH | Yes | 4.28 |
| 11 | VRYID6DIT0PW | VRYID6DIT0PW | Yes | 2.44 |
| 12 | 96KKU247JJYA | 96KKU247JJYA | Yes | 2.55 |
| 13 | MSZZCSTUD9SH | MSZZCSTUD9SH | Yes | 1.74 |
| 14 | 540DGAXO06ZU | 540DGAXO06ZU | Yes | 2.64 |
| 15 | ZB1E4TVAO194 | ZB1E4TVAO194 | Yes | 2.33 |
| 16 | SYIJ3SRUMFNT | SYIJ3SRUMFNT | Yes | 1.8 |
| 17 | 0BKOWD63W7CY | 0BKOWD63W7CY | Yes | 2.31 |
| 18 | BLWXFRI6BQVH | BLWXFRI6BQVH | Yes | 4.37 |
| 19 | SHTRMB57OV2V | SHTRMB57OV2V | Yes | 1.99 |
| 20 | RFTUAOB33ND3 | RFTUAOB33ND3 | Yes | 1.49 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 4.93 |
| 2 | 6 | 6 | Yes | 6.42 |
| 3 | 16 | 16 | Yes | 4.34 |
| 4 | 64 | 64 | Yes | 6.58 |
| 5 | 60 | 60 | Yes | 5.84 |
| 6 | 39 | 39 | Yes | 3.97 |
| 7 | 10 | 10 | Yes | 12.75 |
| 8 | 67 | 67 | Yes | 3.22 |
| 9 | 20 |  | No | 45.81 |
| 10 | 5 | 5 | Yes | 7.51 |
| 11 | 4 | 4 | Yes | 4.24 |
| 12 | 1 | 1 | Yes | 5.35 |
| 13 | 198 | 198 | Yes | 4.72 |
| 14 | 7680 | 7680 | Yes | 5.52 |
| 15 | 36 | 36 | Yes | 1.32 |
| 16 | 243 | 243 | Yes | 4.58 |
| 17 | 60 | 60 | Yes | 5.1 |
| 18 | 48 | 48 | Yes | 1.66 |
| 19 | 26 | 26 | Yes | 12.95 |
| 20 | 19 | 19 | Yes | 4.44 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \\< /))_  | \\< /))_ | No | 28.22 |
| 2 | \_<(\\/ / | /\) <(_<)\_<(\\/ / | No | 33.45 |
| 3 | <\)/)_ () | <\)/)_ () | Yes | 3.96 |
| 4 | (/)__)\// | (/)__)\// | Yes | 16.02 |
| 5 | /(<_<<_<\ | /(<_<<_<\ | Yes | 14.85 |
| 6 | \_())\(   | \_())\( | No | 30.73 |
| 7 | (\(/ \</\ | (\(/ \</\ | Yes | 25.75 |
| 8 | ((//(<((  | ((//(<(( | No | 22.24 |
| 9 |  / \_/__< | / \_/__< | No | 20.74 |
| 10 | \/_()\ _\ | \/_()\ _\ | Yes | 10.99 |
| 11 |  ( <\_\(  | ( <\_\( | No | 16.17 |
| 12 |  \// /_ < | \// /_ < | No | 10.26 |
| 13 | \__ //  _ | \__ //  _ | Yes | 12.91 |
| 14 | (\\\ <<\_ |  | No | 35.29 |
| 15 | \)_ ))\(( | \)_ ))\(( | Yes | 9.66 |
| 16 | )\(\)(<__ |  | No | 38.53 |
| 17 | (()\))/)< | (()\))/)< | Yes | 12.55 |
| 18 |  << _ _</ | << _ _</ | No | 10.33 |
| 19 | <\\ _( _) | <\\ _( _) | Yes | 10.56 |
| 20 | )_<__//\\ |  | No | 39.87 |
