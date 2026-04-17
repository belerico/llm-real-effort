# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-27 10:19:02

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
| sudoku_game | 5085 | 38260 | 43345 | 4 | 16 | 31.93 | 638.73 |
| add_numbers | 3202 | 3861 | 7063 | 20 | 0 | 7.93 | 158.51 |
| counting_zeros | 6252 | 30706 | 36958 | 18 | 2 | 20.02 | 400.45 |
| task_decoding | 4478 | 4840 | 9318 | 20 | 0 | 8.34 | 166.79 |
| task_summation | 4516 | 8793 | 13309 | 20 | 0 | 9.30 | 185.96 |
| task_transcription | 3193 | 3892 | 7085 | 20 | 0 | 9.33 | 186.62 |
| task_sequences | 3183 | 4927 | 8110 | 19 | 1 | 10.77 | 215.48 |
| string_entry | 3490 | 4330 | 7820 | 20 | 0 | 11.31 | 226.24 |
| **TOTAL** | **33399** | **99609** | **133008** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 3 6 3 4 5 6 1 1 6 4 2 3 | 4 6 3 6 4 1 3 5 5 1 6 1 6 2 4 2 4 2 3 | No | 45.43 |
| 2 | 2 2 6 4 3 5 2 1 5 1 6 5 3 2 | 2 2 6 4 3 5 2 1 5 1 6 5 3 2 | Yes | 39.44 |
| 3 | 4 1 2 3 2 5 3 6 3 6 3 3 2 6 | To solve the 6x6 Sudoku puzzle, we can determine the missing numbers by ensuring each row, column, and 3x2 box contains the digits 1-6 exactly once.   Here is the step-by-step deduction: 1. **Row 2** has `. 1 2 5 4 6`, so the missing number in R2C1 | No | 26.23 |
| 4 | 4 5 1 2 4 2 4 1 2 1 6 1 1 5 | To solve the Sudoku puzzle, we can deduce the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.   Here is the step-by-step logical deduction: 1. **Column 4** has `2, 5, ., 3, 4, 6`. The only missing number is | No | 18.5 |
| 5 | 6 5 2 6 1 6 1 6 4 3 1 5 6 4 | 6 5 2 6 1 6 1 6 4 3 1 5 6 4 | Yes | 30.82 |
| 6 | 4 1 2 5 6 6 5 2 5 3 1 2 5 6 | To solve the 6x6 Sudoku puzzle, we need to fill the grid so that each row, column, and 2x3 box contains the numbers 1-6 exactly once. Based on the grid layout, the boxes are 2 rows by 3 columns.   Let's analyze the grid step by step:  **Row 1:** 5 2 . | No | 17.46 |
| 7 | 1 2 1 4 4 1 2 3 6 4 2 5 2 4 | 1 2 1 4 4 1 2 3 2 4 2 4 5 2 4 2 4 5 | No | 33.5 |
| 8 | 4 2 2 2 5 3 4 4 2 1 5 3 2 1 | 4 2 2 2 5 3 4 4 1 2 1 2 5 1 3 | No | 30.14 |
| 9 | 3 5 1 3 1 5 2 1 2 6 2 2 5 4 | 1 5 3 3 1 5 2 2 1 6 2 4 2 5 4 | No | 27.08 |
| 10 | 1 4 2 5 4 6 6 3 2 1 4 6 5 2 | 1 4 2 5 6 4 3 6 4 6 2 5 2 5 | No | 25.29 |
| 11 | 2 6 1 1 6 6 1 5 4 1 3 3 2 4 | To solve this 6x6 Sudoku puzzle, we need to fill the grid so that each row, column, and 2x3 box contains the numbers 1 through 6 exactly once.   Let's deduce the missing numbers step-by-step: 1. **Column 1** has 4, 3, 2, 1, 5 | No | 27.7 |
| 12 | 4 3 1 3 4 1 2 1 3 2 1 4 6 5 | 4 3 1 3 4 1 2 1 3 2 1 4 6 5 | Yes | 23.78 |
| 13 | 5 6 3 1 5 1 2 4 6 2 3 5 2 3 | 5 6 3 1 5 1 2 4 6 2 2 3 5 2 3 | No | 22.39 |
| 14 | 1 5 4 2 3 1 2 6 3 6 5 5 1 3 | 1 5 4 2 3 1 2 6 5 3 5 6 3 1 5 3 | No | 25.89 |
| 15 | 2 1 1 2 4 2 3 5 4 6 3 5 2 3 | 2 1 1 2 4 2 5 3 4 6 3 5 2 | No | 26.39 |
| 16 | 3 1 3 2 3 2 1 5 4 4 1 6 2 6 | 3 1 3 2 3 2 1 5 4 4 1 6 2 6 | Yes | 25.3 |
| 17 | 2 6 4 3 6 4 3 4 2 6 4 3 5 6 | TIMEOUT | No | 120.02 |
| 18 | 4 3 3 6 2 6 1 2 5 3 5 5 6 1 | To solve the 6x6 Sudoku puzzle, we can determine the missing numbers by ensuring each row, column, and 3x2 box (noting the grid layout implies 3 rows by 2 columns per box to avoid the conflicting 1s in the top-left) contains the numbers 1-6 exactly once.  Here is the step-by-step logical deduction: | No | 20.44 |
| 19 | 3 6 4 3 4 1 3 3 6 3 4 6 2 1 | 3 4 6 3 4 1 3 3 6 3 4 2 6 2 1 | No | 22.09 |
| 20 | 6 4 4 2 3 6 2 3 4 3 2 5 4 3 | To solve the Sudoku puzzle, we need to fill in the missing numbers such that each row, column, and 2x3 box contains the numbers 1-6 exactly once.   Based on the grid, the boxes are 3 rows by 2 columns (since the first two columns of the first three rows are 5, 2, 3, 6, | No | 30.8 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1503 | 1503 | Yes | 4.05 |
| 2 | 2031 | 2031 | Yes | 5.84 |
| 3 | 1763 | 1763 | Yes | 3.37 |
| 4 | 2122 | 2122 | Yes | 4.45 |
| 5 | 1715 | 1715 | Yes | 11.22 |
| 6 | 1714 | 1714 | Yes | 5.0 |
| 7 | 1664 | 1664 | Yes | 5.25 |
| 8 | 1050 | 1050 | Yes | 14.64 |
| 9 | 2152 | 2152 | Yes | 14.53 |
| 10 | 706 | 706 | Yes | 4.83 |
| 11 | 1183 | 1183 | Yes | 4.35 |
| 12 | 1271 | 1271 | Yes | 6.02 |
| 13 | 1222 | 1222 | Yes | 11.35 |
| 14 | 1871 | 1871 | Yes | 10.11 |
| 15 | 1457 | 1457 | Yes | 9.48 |
| 16 | 2244 | 2244 | Yes | 9.33 |
| 17 | 2187 | 2187 | Yes | 5.05 |
| 18 | 2265 | 2265 | Yes | 14.45 |
| 19 | 1915 | 1915 | Yes | 4.67 |
| 20 | 1986 | 1986 | Yes | 10.52 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 54 | Yes | 22.82 |
| 2 | 68 | 67 | No | 18.86 |
| 3 | 64 | 64 | Yes | 14.82 |
| 4 | 64 | 64 | Yes | 24.91 |
| 5 | 55 | 55 | Yes | 15.02 |
| 6 | 40 | 40 | Yes | 18.27 |
| 7 | 69 | 69 | Yes | 14.06 |
| 8 | 39 | 39 | Yes | 11.44 |
| 9 | 36 | 36 | Yes | 9.53 |
| 10 | 38 | 38 | Yes | 31.84 |
| 11 | 60 | 60 | Yes | 28.79 |
| 12 | 73 | 73 | Yes | 12.23 |
| 13 | 70 | 70 | Yes | 14.42 |
| 14 | 52 | 52 | Yes | 26.66 |
| 15 | 37 | 37 | Yes | 16.02 |
| 16 | 59 | 59 | Yes | 26.39 |
| 17 | 49 | 49 | Yes | 20.44 |
| 18 | 70 | 69 | No | 20.43 |
| 19 | 66 | 66 | Yes | 28.47 |
| 20 | 66 | 66 | Yes | 24.99 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EXRDWKO | EXRDWKO | Yes | 5.75 |
| 2 | DLFUCYN | DLFUCYN | Yes | 9.15 |
| 3 | ZNICLSB | ZNICLSB | Yes | 5.33 |
| 4 | ZRXVIUK | ZRXVIUK | Yes | 4.65 |
| 5 | QCHXOKE | QCHXOKE | Yes | 6.16 |
| 6 | JXYCFVU | JXYCFVU | Yes | 8.21 |
| 7 | PCVWFHA | PCVWFHA | Yes | 5.83 |
| 8 | HYLXFVW | HYLXFVW | Yes | 9.07 |
| 9 | RNSLMHB | RNSLMHB | Yes | 4.93 |
| 10 | BMDCIUK | BMDCIUK | Yes | 10.99 |
| 11 | NHJWBEL | NHJWBEL | Yes | 11.62 |
| 12 | XDEJHQB | XDEJHQB | Yes | 3.39 |
| 13 | VRHESTG | VRHESTG | Yes | 3.82 |
| 14 | ZMXSRAB | ZMXSRAB | Yes | 16.92 |
| 15 | OIWAPFR | OIWAPFR | Yes | 5.8 |
| 16 | YMGEHSV | YMGEHSV | Yes | 5.86 |
| 17 | DRKHUFE | DRKHUFE | Yes | 15.02 |
| 18 | EVYPAWM | EVYPAWM | Yes | 4.52 |
| 19 | OUVXWJA | OUVXWJA | Yes | 15.13 |
| 20 | GFLXIPT | GFLXIPT | Yes | 14.62 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 0.5 9.5 | Yes | 11.41 |
| 2 | [1.9, 8.1] | 1.9 8.1 | Yes | 16.42 |
| 3 | [1.6, 8.4] | 8.4 1.6 | Yes | 5.0 |
| 4 | [3.6, 6.4] | 3.6 6.4 | Yes | 5.71 |
| 5 | [3.6, 6.4] | 3.6 6.4 | Yes | 6.79 |
| 6 | [4.2, 5.8] | 4.2 5.8 | Yes | 5.86 |
| 7 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.43 |
| 8 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.99 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 16.89 |
| 10 | [3.3, 6.7] | 3.3 6.7 | Yes | 13.49 |
| 11 | [1.8, 8.2] | 8.2 1.8 | Yes | 15.84 |
| 12 | [0.3, 9.7] | 0.3 9.7 | Yes | 13.48 |
| 13 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.94 |
| 14 | [3.1, 6.9] | 3.1 6.9 | Yes | 6.82 |
| 15 | [0.8, 9.2] | 0.8 9.2 | Yes | 7.93 |
| 16 | [3.4, 6.6] | 3.4 6.6 | Yes | 13.45 |
| 17 | [0.8, 9.2] | 9.2 0.8 | Yes | 6.21 |
| 18 | [2.9, 7.1] | 2.9 7.1 | Yes | 6.81 |
| 19 | [3.2, 6.8] | 3.2 6.8 | Yes | 5.79 |
| 20 | [0.4, 9.6] | 9.6 0.4 | Yes | 7.67 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9LSDTDO4YB1A | 9LSDTDO4YB1A | Yes | 10.68 |
| 2 | 449JGJHAEF1Z | 449JGJHAEF1Z | Yes | 3.86 |
| 3 | Y0X36WU0LG3W | Y0X36WU0LG3W | Yes | 4.08 |
| 4 | 1AVBUWENMV25 | 1AVBUWENMV25 | Yes | 4.58 |
| 5 | FQ69L1GB0OE1 | FQ69L1GB0OE1 | Yes | 8.28 |
| 6 | 1AZZO805225W | 1AZZO805225W | Yes | 12.15 |
| 7 | QUGCXPUE8421 | QUGCXPUE8421 | Yes | 4.86 |
| 8 | 907WGFKIX0M4 | 907WGFKIX0M4 | Yes | 12.97 |
| 9 | 6B73VB6XHKAD | 6B73VB6XHKAD | Yes | 12.87 |
| 10 | Z4POSUJUADPI | Z4POSUJUADPI | Yes | 12.37 |
| 11 | V07X226H9A0E | V07X226H9A0E | Yes | 9.59 |
| 12 | AEVEJ3XPAK75 | AEVEJ3XPAK75 | Yes | 4.3 |
| 13 | W0S6XBQF0LKG | W0S6XBQF0LKG | Yes | 4.96 |
| 14 | UMAWH6UJF24Y | UMAWH6UJF24Y | Yes | 5.14 |
| 15 | FQWQRAHVWK41 | FQWQRAHVWK41 | Yes | 4.4 |
| 16 | 08DEV7U317EI | 08DEV7U317EI | Yes | 13.58 |
| 17 | UBEE7VKUB5PM | UBEE7VKUB5PM | Yes | 14.62 |
| 18 | HKEKYTN59461 | HKEKYTN59461 | Yes | 4.09 |
| 19 | 9POG0MEOJZAT | 9POG0MEOJZAT | Yes | 24.62 |
| 20 | UCFYER1AHV1T | UCFYER1AHV1T | Yes | 14.62 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 8.58 |
| 2 | 4096 | 65536 | No | 19.07 |
| 3 | 63 | 63 | Yes | 3.75 |
| 4 | 198 | 198 | Yes | 5.4 |
| 5 | 16 | 16 | Yes | 14.98 |
| 6 | 793 | 793 | Yes | 14.08 |
| 7 | 7 | 7 | Yes | 14.88 |
| 8 | 48 | 48 | Yes | 6.92 |
| 9 | 23 | 23 | Yes | 4.1 |
| 10 | 64 | 64 | Yes | 14.61 |
| 11 | 3 | 3 | Yes | 9.18 |
| 12 | 9 | 9 | Yes | 4.43 |
| 13 | 31 | 31 | Yes | 6.45 |
| 14 | 4 | 4 | Yes | 4.68 |
| 15 | 243 | 243 | Yes | 13.96 |
| 16 | 28 | 28 | Yes | 17.92 |
| 17 | 36 | 36 | Yes | 14.74 |
| 18 | 26 | 26 | Yes | 16.75 |
| 19 | 3 | 3 | Yes | 14.63 |
| 20 | 4 | 4 | Yes | 6.36 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _/()\(\ / | _/()\(\ / | Yes | 6.62 |
| 2 | )_( /\_<_ | )_( /\_<_ | Yes | 8.73 |
| 3 | _<)()/ )) | _<)()/ )) | Yes | 14.24 |
| 4 | (\\)(_(</ | (\\)(_(</ | Yes | 5.67 |
| 5 | ( /   //) | ( /   //) | Yes | 7.86 |
| 6 | /)( /\\ ( | /)( /\ ( | Yes | 17.6 |
| 7 | _(/) ____ | _(/) ____ | Yes | 3.93 |
| 8 | \(</) ()( | \(</) ()( | Yes | 3.24 |
| 9 | </<\\) (_ | </<\\) (_ | Yes | 14.64 |
| 10 | \)/))()</ | \)/))()</ | Yes | 15.8 |
| 11 | /\_/<__ \ | /\_/<__ \ | Yes | 5.22 |
| 12 | <\ /( /<_ | <\ /( /<_ | Yes | 14.5 |
| 13 | /\//<))/( | /\//<))/( | Yes | 16.17 |
| 14 | _/)\/_()\ | _/)\/_()\ | Yes | 15.53 |
| 15 | )_)( / \\ | )_)( / \ | Yes | 12.79 |
| 16 | /(\<<__<\ | /(\<<__<\ | Yes | 15.11 |
| 17 | \/ (( <_\ | \/ (( <_\ | Yes | 10.8 |
| 18 | \\(\/<)/_ | \\(\/<)/_ | Yes | 10.96 |
| 19 | \/<\\_<<_ | \/<\\_<<_ | Yes | 13.87 |
| 20 | /() (<<<( | /() (<<<( | Yes | 12.97 |
