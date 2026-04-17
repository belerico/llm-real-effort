# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-27 10:21:54

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
| sudoku_game | 5283 | 38438 | 43721 | 2 | 18 | 35.65 | 712.96 |
| add_numbers | 3404 | 4288 | 7692 | 20 | 0 | 8.67 | 173.51 |
| counting_zeros | 6462 | 30977 | 37439 | 19 | 1 | 20.32 | 406.34 |
| task_decoding | 4672 | 5133 | 9805 | 20 | 0 | 9.16 | 183.16 |
| task_summation | 4716 | 8588 | 13304 | 20 | 0 | 10.86 | 217.14 |
| task_transcription | 3381 | 3708 | 7089 | 20 | 0 | 10.14 | 202.74 |
| task_sequences | 3400 | 6139 | 9539 | 19 | 1 | 12.06 | 241.15 |
| string_entry | 3705 | 4915 | 8620 | 14 | 6 | 10.09 | 201.89 |
| **TOTAL** | **35023** | **102186** | **137209** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 4 2 6 4 4 5 2 5 2 5 3 4 | To solve the 6x6 Sudoku puzzle, we need to ensure that every row and column contains the numbers 1 through 6 exactly once.   Let's deduce the missing numbers step-by-step: * **Row 1:** 1 . 2 \| 5 6 3 → The only missing number is **4**. * **Row 5:** | No | 26.96 |
| 2 | 2 4 3 1 2 4 1 2 6 4 3 1 2 5 | To solve the 6x6 Sudoku puzzle, we need to fill the grid so that each row, column, and 2x3 box contains the numbers 1-6 exactly once.   Let's analyze the grid: Row 1: 5 . . \| 6 . 1 Row 2: 6 3 . \| . 5 . | No | 29.98 |
| 3 | 3 1 4 6 4 1 3 2 6 3 1 2 5 1 | 4 1 3 6 3 1 4 2 6 5 1 2 5 2 1 | No | 24.99 |
| 4 | 3 1 2 6 4 4 5 2 3 3 2 5 2 1 | To solve the 6x6 Sudoku puzzle, we need to ensure that every row, column, and 2x3 box contains the numbers 1 through 6 exactly once.   Let's evaluate the grid: Row 1: 6 . 4 \| . 5 . Row 2: 2 5 3 \| . 1 . Row | No | 26.24 |
| 5 | 3 2 4 3 6 3 3 5 6 1 6 5 1 4 | 3 2 4 3 6 3 3 5 6 1 6 5 1 4 | Yes | 17.75 |
| 6 | 3 1 3 5 3 6 6 3 1 5 1 3 2 6 | To find the missing numbers, let's analyze the grid. The puzzle is a 6x6 Sudoku, which means it consists of 2×3 boxes (2 rows and 3 columns per box).   **Row 1:** 2 . 5 \| . 4 6 The missing numbers are 1 and 3. Looking at Box 1 (top- | No | 29.99 |
| 7 | 5 4 1 1 5 2 6 6 4 3 2 3 2 1 | To solve the 6×6 Sudoku puzzle, we can deduce the missing numbers step by step. The grid is divided into 2×3 boxes (2 rows and 3 columns each).  **Row 3** is complete: `2 6 3 \| 5 1 4`  **Row 4:** `1 4 . \| 3 . 5 | No | 27.0 |
| 8 | 2 6 1 6 1 1 4 6 1 2 4 1 6 2 | 1 2 1 6 6 1 4 1 2 1 6 2 | No | 29.51 |
| 9 | 6 2 3 1 5 4 5 5 6 4 2 2 5 1 | 6 1 2 3 5 4 5 5 2 4 1 2 5 1 2 | No | 21.61 |
| 10 | 4 1 3 1 5 4 2 4 2 1 3 4 3 5 | 4 1 2 4 1 5 1 2 4 3 4 3 5 | No | 30.49 |
| 11 | 1 6 1 2 3 4 5 6 1 2 5 5 2 4 | To solve the Sudoku puzzle, we can deduce the missing numbers by ensuring each row, column, and 2×3 box (or in this case, based on the grid layout and numbers, a 3×2 box structure fits perfectly without conflicts) contains the digits 1-6 exactly once.   Here is the step-by-step deduction: 1. **Row 2 | No | 29.85 |
| 12 | 2 3 4 6 4 1 3 6 2 6 1 5 2 3 | 2 3 4 1 4 3 6 6 2 2 1 5 3 2 | No | 51.57 |
| 13 | 2 6 1 1 2 6 4 6 4 2 2 5 4 2 | 1 2 6 2 1 4 6 6 2 4 2 5 2 4 2 4 | No | 29.07 |
| 14 | 5 2 6 4 4 3 5 5 6 1 2 5 5 2 | To solve the 6x6 Sudoku, we need to fill in the grid so that every row, column, and 2x3 box contains the numbers 1-6 exactly once.   Let's look at the grid and deduce the missing values: R1: . . 4 \| 6 3 1 R2: 1 3 2 \| | No | 42.42 |
| 15 | 5 2 2 3 5 5 2 1 2 5 4 4 2 6 | To solve the 6x6 Sudoku puzzle, we need to fill in the empty cells (.) such that each row, column, and 2x3 box contains the numbers 1-6 exactly once.   Given puzzle: . 4 3 \| 6 1 . . . 1 \| . 4 6 -----+----- 1 6 | No | 44.16 |
| 16 | 6 3 6 1 5 1 2 4 1 5 6 1 4 3 | 6 3 1 6 5 1 1 2 4 1 6 5 5 6 1 4 3 | No | 44.93 |
| 17 | 3 6 3 2 1 4 1 6 1 3 5 3 2 1 | 3 5 2 3 1 1 4 6 1 3 5 3 2 | No | 26.72 |
| 18 | 2 6 3 1 5 4 3 6 4 6 4 3 1 6 | TIMEOUT | No | 120.02 |
| 19 | 4 1 3 3 6 6 4 5 2 6 3 5 2 1 | To solve the 6x6 Sudoku puzzle, we need to fill in the missing numbers so that each row, column, and 2x3 box contains the numbers 1-6 exactly once.   Here is the starting grid: 6 2 . \| . . 5 4 5 . \| 2 . 1 ------+------ 1 3 5 \| | No | 29.94 |
| 20 | 3 1 2 4 1 5 3 2 1 5 1 3 6 1 | 3 1 2 4 1 5 3 2 1 5 1 3 6 1 | Yes | 29.73 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1257 | 1257 | Yes | 14.2 |
| 2 | 1946 | 1946 | Yes | 10.5 |
| 3 | 1147 | 1147 | Yes | 10.61 |
| 4 | 2021 | 2021 | Yes | 4.38 |
| 5 | 1380 | 1380 | Yes | 5.67 |
| 6 | 2163 | 2163 | Yes | 13.7 |
| 7 | 1584 | 1584 | Yes | 10.27 |
| 8 | 2418 | 2418 | Yes | 5.29 |
| 9 | 2169 | 2169 | Yes | 11.64 |
| 10 | 1879 | 1879 | Yes | 13.12 |
| 11 | 2524 | 2524 | Yes | 6.07 |
| 12 | 1979 | 1979 | Yes | 4.02 |
| 13 | 2192 | 2192 | Yes | 4.79 |
| 14 | 1844 | 1844 | Yes | 9.84 |
| 15 | 1847 | 1847 | Yes | 9.99 |
| 16 | 810 | 810 | Yes | 8.28 |
| 17 | 2096 | 2096 | Yes | 11.37 |
| 18 | 1758 | 1758 | Yes | 5.17 |
| 19 | 2541 | 2541 | Yes | 4.58 |
| 20 | 1522 | 1522 | Yes | 10.0 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 73 | Yes | 20.75 |
| 2 | 47 | 46 | No | 22.85 |
| 3 | 59 | 59 | Yes | 18.65 |
| 4 | 61 | 61 | Yes | 19.8 |
| 5 | 71 | 71 | Yes | 23.48 |
| 6 | 45 | 45 | Yes | 12.77 |
| 7 | 44 | 44 | Yes | 16.48 |
| 8 | 52 | 52 | Yes | 18.7 |
| 9 | 42 | 42 | Yes | 17.92 |
| 10 | 56 | 56 | Yes | 26.17 |
| 11 | 45 | 45 | Yes | 20.89 |
| 12 | 71 | 71 | Yes | 21.67 |
| 13 | 71 | 71 | Yes | 29.92 |
| 14 | 46 | 46 | Yes | 25.43 |
| 15 | 61 | 61 | Yes | 15.3 |
| 16 | 38 | 38 | Yes | 20.76 |
| 17 | 35 | 35 | Yes | 19.41 |
| 18 | 56 | 56 | Yes | 18.67 |
| 19 | 40 | 40 | Yes | 24.41 |
| 20 | 50 | 50 | Yes | 12.29 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TDMKUJI | TDMKUJI | Yes | 6.74 |
| 2 | YSRXLWC | YSRXLWC | Yes | 16.19 |
| 3 | PWYNRFM | PWYNRFM | Yes | 12.3 |
| 4 | UHDMTEW | UHDMTEW | Yes | 4.01 |
| 5 | TCIVWKB | TCIVWKB | Yes | 8.21 |
| 6 | IHCOZEW | IHCOZEW | Yes | 4.51 |
| 7 | JVRGYCF | JVRGYCF | Yes | 5.39 |
| 8 | FSTONVD | FSTONVD | Yes | 6.9 |
| 9 | FTGLKHQ | FTGLKHQ | Yes | 11.42 |
| 10 | WACGJNL | WACGJNL | Yes | 8.87 |
| 11 | TAIQVGL | TAIQVGL | Yes | 15.18 |
| 12 | NOECQWB | NOECQWB | Yes | 4.2 |
| 13 | ESJNLGM | ESJNLGM | Yes | 9.1 |
| 14 | EWOJDVB | EWOJDVB | Yes | 6.12 |
| 15 | RQGYIMN | RQGYIMN | Yes | 9.66 |
| 16 | JZPGEHX | JZPGEHX | Yes | 9.47 |
| 17 | ASDEXPG | ASDEXPG | Yes | 10.67 |
| 18 | WHMAIBZ | WHMAIBZ | Yes | 14.83 |
| 19 | PBIQVKL | PBIQVKL | Yes | 10.23 |
| 20 | OBPWRXF | OBPWRXF | Yes | 9.13 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.41 |
| 2 | [1.6, 8.4] | 1.6 8.4 | Yes | 6.93 |
| 3 | [0.3, 9.7] | 0.3 9.7 | Yes | 11.7 |
| 4 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.31 |
| 5 | [3.6, 6.4] | 3.6 6.4 | Yes | 7.35 |
| 6 | [1.7, 8.3] | 1.7 8.3 | Yes | 15.79 |
| 7 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.04 |
| 8 | [1.2, 8.8] | 8.8 1.2 | Yes | 6.61 |
| 9 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.25 |
| 10 | [2.3, 7.7] | 2.3 7.7 | Yes | 17.11 |
| 11 | [0.8, 9.2] | 0.8 9.2 | Yes | 7.29 |
| 12 | [1.5, 8.5] | 8.5 1.5 | Yes | 15.99 |
| 13 | [3.4, 6.6] | 3.4 6.6 | Yes | 16.17 |
| 14 | [2.2, 7.8] | 2.2 7.8 | Yes | 6.72 |
| 15 | [0.4, 9.6] | 9.6 0.4 | Yes | 17.43 |
| 16 | [0.2, 9.8] | 9.8 0.2 | Yes | 6.38 |
| 17 | [4.4, 5.6] | 4.4 5.6 | Yes | 17.22 |
| 18 | [0.3, 9.7] | 0.3 9.7 | Yes | 6.72 |
| 19 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.97 |
| 20 | [1.3, 8.7] | 1.3 8.7 | Yes | 16.73 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CLX0QPDARO2D | CLX0QPDARO2D | Yes | 12.88 |
| 2 | X36Q5ZTBR0LV | X36Q5ZTBR0LV | Yes | 14.77 |
| 3 | P0AYRT83AOWQ | P0AYRT83AOWQ | Yes | 8.55 |
| 4 | C9OWHXBTQKE0 | C9OWHXBTQKE0 | Yes | 3.71 |
| 5 | GFOJ11OYVQEM | GFOJ11OYVQEM | Yes | 13.51 |
| 6 | MRAIEZ2KHUQ8 | MRAIEZ2KHUQ8 | Yes | 6.64 |
| 7 | QJZYRYR0OZTO | QJZYRYR0OZTO | Yes | 5.96 |
| 8 | K9CQWU4CX4WM | K9CQWU4CX4WM | Yes | 10.63 |
| 9 | 0CIF5P8DH4QO | 0CIF5P8DH4QO | Yes | 12.69 |
| 10 | 94VCLFMMCNB5 | 94VCLFMMCNB5 | Yes | 14.3 |
| 11 | WNQUZL0LDYSG | WNQUZL0LDYSG | Yes | 14.45 |
| 12 | G0QEJA0TCCDD | G0QEJA0TCCDD | Yes | 3.67 |
| 13 | OSGVPN5ROQUU | OSGVPN5ROQUU | Yes | 4.19 |
| 14 | EVNFJF5AKC0F | EVNFJF5AKC0F | Yes | 14.85 |
| 15 | WXA0KM7PN0PE | WXA0KM7PN0PE | Yes | 26.93 |
| 16 | HJ72SKETHXTD | HJ72SKETHXTD | Yes | 9.7 |
| 17 | JY7R62Y5EKSZ | JY7R62Y5EKSZ | Yes | 10.23 |
| 18 | YGY3YMRQZLFG | YGY3YMRQZLFG | Yes | 4.84 |
| 19 | EJS728IFILPC | EJS728IFILPC | Yes | 4.06 |
| 20 | VJPM43FQLIZH | VJPM43FQLIZH | Yes | 6.16 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 3.92 |
| 2 | 60 | 60 | Yes | 14.92 |
| 3 | 44 | 44 | Yes | 14.68 |
| 4 | 7 | 7 | Yes | 14.03 |
| 5 | 243 | 243 | Yes | 14.47 |
| 6 | 64 | 64 | Yes | 5.73 |
| 7 | 67 | 67 | Yes | 14.26 |
| 8 | 28 | 28 | Yes | 6.72 |
| 9 | 73 | 73 | Yes | 10.07 |
| 10 | 4 | 4 | Yes | 4.31 |
| 11 | 4096 | 65536 | No | 20.27 |
| 12 | 10 | 10 | Yes | 18.19 |
| 13 | 19 | 19 | Yes | 14.46 |
| 14 | 6 | 6 | Yes | 4.59 |
| 15 | 793 | 793 | Yes | 15.81 |
| 16 | 3 | 3 | Yes | 16.37 |
| 17 | 4 | 4 | Yes | 14.09 |
| 18 | 16 | 16 | Yes | 11.87 |
| 19 | 5 | 5 | Yes | 9.83 |
| 20 | 20 | 20 | Yes | 12.54 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ))<_ ))<_ | ))<_ ))<_ | Yes | 15.25 |
| 2 | _))<\((\) | _))<\((\) | Yes | 5.33 |
| 3 | )_\//_<<\ | )_\//_<<\ | Yes | 14.06 |
| 4 |  (/(< /// | (/(< /// | No | 5.7 |
| 5 | )/\// /)< | )/\// /)< | Yes | 14.26 |
| 6 | _)\)((//\ | _)\)((//\ | Yes | 3.32 |
| 7 | \()\\_ /\ | \()\\_ /\ | Yes | 5.51 |
| 8 | \\(\/_ /) | \\(\/_ /) | Yes | 10.48 |
| 9 |  _(_() () | _(_() () | No | 11.16 |
| 10 | \__\(<<)< | \__\(<<)< | Yes | 14.98 |
| 11 | \ )<()<\_ | \ )<()<\_ | Yes | 4.76 |
| 12 | /<))))</) | /<))))</) | Yes | 14.59 |
| 13 |   )//\)() | )//\)() | No | 16.14 |
| 14 | <\(\</<)< | <\(\</<)< | Yes | 5.67 |
| 15 |   )<\/\)  | )<\/\) | No | 16.71 |
| 16 | /(<)_<//  | /(<)_<// | No | 3.4 |
| 17 | <( <<\<)_ | <( <<\<)_ | Yes | 8.07 |
| 18 | <(<)<__ ) | <(<)<__ ) | Yes | 5.95 |
| 19 | )/(\)\/\  | )/(\)\/\ | No | 12.44 |
| 20 | /_ / /)<\ | /_ / /)<\ | Yes | 14.11 |
