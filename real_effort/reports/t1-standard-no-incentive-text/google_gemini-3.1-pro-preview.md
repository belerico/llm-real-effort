# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-27 10:22:52

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
| sudoku_game | 4998 | 40296 | 45294 | 5 | 15 | 31.09 | 621.71 |
| add_numbers | 2848 | 3835 | 6683 | 20 | 0 | 10.78 | 215.68 |
| counting_zeros | 5606 | 33072 | 38678 | 19 | 1 | 31.19 | 623.72 |
| task_decoding | 4110 | 4847 | 8957 | 20 | 0 | 7.77 | 155.48 |
| task_summation | 4162 | 9024 | 13186 | 20 | 0 | 10.48 | 209.54 |
| task_transcription | 2828 | 3119 | 5947 | 20 | 0 | 9.55 | 191.12 |
| task_sequences | 2820 | 5921 | 8741 | 20 | 0 | 10.24 | 204.73 |
| string_entry | 3141 | 7491 | 10632 | 12 | 8 | 10.73 | 214.52 |
| **TOTAL** | **30513** | **107605** | **138118** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 2 3 4 6 4 2 5 3 2 3 6 1 | 4 6 2 3 1 6 3 4 2 3 5 6 1 2 3 6 1 | No | 24.77 |
| 2 | 5 1 1 2 4 5 3 6 3 2 6 5 1 5 | 1 5 1 2 4 6 5 6 3 3 2 6 5 1 5 | No | 30.45 |
| 3 | 3 2 6 2 6 6 2 2 5 1 1 5 3 2 | R3 R4 -----+----- R5 R6 Wait, there are two horizontal lines: after R2 and after R4. So boxes are 2 rows by 3 columns. Box 1 is R1-2, C1-3. Wait, if Box 1 is R1-2, C1-3, then R1C2 | No | 29.85 |
| 4 | 4 5 2 1 4 2 2 3 1 3 2 3 4 6 | To solve the Sudoku puzzle, we first deduce the correct box dimensions. Based on the given numbers, the grid is divided into six 3×2 boxes (3 rows by 2 columns), meaning each box spans three rows and two columns.  Let's fill in the missing numbers step by step:  **Row 2:** 3 1 . \| 6 5 2 | No | 27.4 |
| 5 | 3 4 5 2 4 1 3 4 1 6 2 6 4 3 | 3 4 5 2 4 1 3 4 1 6 2 6 4 3 | Yes | 46.47 |
| 6 | 3 6 2 4 1 3 2 4 1 6 3 5 2 5 | To solve the 6x6 Sudoku puzzle, we need to fill in the grid so that each row, column, and 2x3 box contains the numbers 1 through 6 exactly once.  Given puzzle: . . 5 \| 4 1 2 . 1 6 \| 3 5 4 ------+------ . 5 . \| | No | 39.65 |
| 7 | 6 3 3 2 4 5 6 4 6 6 6 3 4 2 | 3 6 3 4 4 6 6 4 6 3 2 4 6 4 2 3 | No | 29.64 |
| 8 | 5 6 1 5 4 3 3 5 4 4 3 6 3 1 | 5 6 1 5 4 3 3 5 4 3 4 6 3 1 | No | 48.26 |
| 9 | 2 6 5 6 2 1 3 5 4 3 6 2 2 1 | 2 6 5 2 6 1 3 5 4 3 2 6 2 1 2 | No | 25.49 |
| 10 | 5 4 3 1 1 3 6 1 3 3 1 6 6 5 | 5 1 3 4 1 3 6 1 3 1 3 6 6 1 5 6 | No | 27.46 |
| 11 | 6 4 1 5 2 6 3 1 5 6 5 4 4 3 | 6 1 4 5 2 6 3 1 5 6 4 5 4 3 | No | 32.61 |
| 12 | 2 5 1 5 4 4 3 2 1 4 6 3 4 5 | 2 5 1 5 4 4 3 2 1 4 6 3 4 5 | Yes | 29.58 |
| 13 | 5 4 3 5 6 3 5 6 4 3 2 1 5 6 | 5 4 3 5 6 3 5 6 4 3 2 1 5 6 | Yes | 73.46 |
| 14 | 3 1 2 3 4 5 3 6 2 1 5 3 4 3 | 3 1 2 3 4 5 2 5 3 6 1 5 3 4 3 | No | 25.86 |
| 15 | 2 3 4 6 4 2 3 5 1 2 6 4 5 4 | To solve the 6×6 Sudoku puzzle, we need to fill the empty cells so that every row, column, and 2×3 box (which here are arranged as 3 rows by 2 columns based on the logical distribution of numbers, despite the visual separators, or vice-versa) contains the numbers 1 through 6 exactly once.   Looking at the grid and the | No | 16.89 |
| 16 | 5 3 2 4 1 6 1 2 4 6 2 4 6 1 | 5 3 2 4 1 6 1 2 4 6 2 4 6 1 | Yes | 18.07 |
| 17 | 1 6 2 3 5 3 5 1 6 6 4 5 6 3 | 1 6 2 3 5 3 5 1 6 6 4 5 6 3 | Yes | 29.62 |
| 18 | 5 6 3 6 5 3 6 1 1 3 6 3 4 5 | To solve the 6×6 Sudoku puzzle, we need to fill in the grid such that every row, column, and 3×2 box contains the numbers 1-6 exactly once.  Here is the step-by-step logical deduction: 1. **Row 3** has `2 5 . \| 6 1 4`. The only missing number | No | 18.84 |
| 19 | 3 6 4 2 1 6 4 4 5 2 6 5 1 3 | 3 4 4 6 2 1 6 5 2 1 3 1 5 3 4 | No | 26.66 |
| 20 | 4 2 3 3 6 1 6 4 1 6 3 3 6 2 | To solve the Sudoku, we need to fill the 6x6 grid so that each row, column, and rectangular box contains the numbers 1-6 exactly once. Although the ASCII separators are drawn at 3x3 intervals, the placement of the numbers (like the two 5s in the top-left 2x3 area) indicates that the boxes for this puzzle are actually | No | 20.67 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 948 | 948 | Yes | 3.96 |
| 2 | 1071 | 1071 | Yes | 10.14 |
| 3 | 1818 | 1818 | Yes | 10.12 |
| 4 | 1888 | 1888 | Yes | 11.75 |
| 5 | 1744 | 1744 | Yes | 14.26 |
| 6 | 2659 | 2659 | Yes | 4.38 |
| 7 | 511 | 511 | Yes | 3.96 |
| 8 | 1547 | 1547 | Yes | 14.84 |
| 9 | 1296 | 1296 | Yes | 14.54 |
| 10 | 2322 | 2322 | Yes | 14.32 |
| 11 | 2608 | 2608 | Yes | 12.48 |
| 12 | 1522 | 1522 | Yes | 10.83 |
| 13 | 1972 | 1972 | Yes | 22.11 |
| 14 | 1660 | 1660 | Yes | 10.66 |
| 15 | 1342 | 1342 | Yes | 15.29 |
| 16 | 2346 | 2346 | Yes | 4.93 |
| 17 | 1590 | 1590 | Yes | 9.01 |
| 18 | 1374 | 1374 | Yes | 9.18 |
| 19 | 1347 | 1347 | Yes | 9.32 |
| 20 | 1296 | 1296 | Yes | 9.59 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 66 | 66 | Yes | 30.26 |
| 2 | 53 | 53 | Yes | 20.73 |
| 3 | 62 | TIMEOUT | No | 120.02 |
| 4 | 59 | 59 | Yes | 29.18 |
| 5 | 38 | 38 | Yes | 18.77 |
| 6 | 62 | 62 | Yes | 23.09 |
| 7 | 50 | 50 | Yes | 26.95 |
| 8 | 72 | 72 | Yes | 24.7 |
| 9 | 39 | 39 | Yes | 12.69 |
| 10 | 46 | 46 | Yes | 27.68 |
| 11 | 44 | 44 | Yes | 24.75 |
| 12 | 63 | 63 | Yes | 27.38 |
| 13 | 67 | 67 | Yes | 23.24 |
| 14 | 72 | 72 | Yes | 28.96 |
| 15 | 54 | 54 | Yes | 22.88 |
| 16 | 63 | 63 | Yes | 28.19 |
| 17 | 59 | 59 | Yes | 18.13 |
| 18 | 55 | 55 | Yes | 61.72 |
| 19 | 72 | 72 | Yes | 24.99 |
| 20 | 73 | 73 | Yes | 29.42 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WVLFNIA | WVLFNIA | Yes | 17.68 |
| 2 | DPUZFLN | DPUZFLN | Yes | 14.9 |
| 3 | BTWDURP | BTWDURP | Yes | 15.54 |
| 4 | BXWQRNU | BXWQRNU | Yes | 6.66 |
| 5 | IBWYPOS | IBWYPOS | Yes | 6.65 |
| 6 | XSMIPBL | XSMIPBL | Yes | 7.08 |
| 7 | RJEXUTI | RJEXUTI | Yes | 6.58 |
| 8 | PTKEUMW | PTKEUMW | Yes | 5.16 |
| 9 | SAEOXUL | SAEOXUL | Yes | 5.92 |
| 10 | XSCKNDI | XSCKNDI | Yes | 9.47 |
| 11 | GMCNQDU | GMCNQDU | Yes | 5.86 |
| 12 | KPLNOHY | KPLNOHY | Yes | 4.28 |
| 13 | IZVGOBP | IZVGOBP | Yes | 5.73 |
| 14 | IHMWDXC | IHMWDXC | Yes | 5.79 |
| 15 | OXLSQTR | OXLSQTR | Yes | 7.45 |
| 16 | HQSPTKM | HQSPTKM | Yes | 9.37 |
| 17 | MVZCWYK | MVZCWYK | Yes | 4.47 |
| 18 | CBDGVIE | CBDGVIE | Yes | 5.99 |
| 19 | GCTZBFX | GCTZBFX | Yes | 3.94 |
| 20 | JCVBELK | JCVBELK | Yes | 6.94 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.3, 8.7] | 1.3 8.7 | Yes | 5.66 |
| 2 | [4.2, 5.8] | 4.2 5.8 | Yes | 13.02 |
| 3 | [2.5, 7.5] | 2.5 7.5 | Yes | 5.9 |
| 4 | [3.7, 6.3] | 3.7 6.3 | Yes | 16.06 |
| 5 | [4.9, 5.1] | 4.9 5.1 | Yes | 6.05 |
| 6 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.41 |
| 7 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.69 |
| 8 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.38 |
| 9 | [0.6, 9.4] | 0.6 9.4 | Yes | 7.01 |
| 10 | [3.5, 6.5] | 3.5 6.5 | Yes | 16.46 |
| 11 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.61 |
| 12 | [2.7, 7.3] | 2.7 7.3 | Yes | 15.66 |
| 13 | [0.1, 9.9] | 0.1 9.9 | Yes | 13.47 |
| 14 | [1.4, 8.6] | 1.4 8.6 | Yes | 7.73 |
| 15 | [2.8, 7.2] | 2.8 7.2 | Yes | 18.06 |
| 16 | [4.2, 5.8] | 4.2 5.8 | Yes | 8.08 |
| 17 | [2.5, 7.5] | 7.5 2.5 | Yes | 16.96 |
| 18 | [2.2, 7.8] | 2.2 7.8 | Yes | 16.11 |
| 19 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.7 |
| 20 | [2.6, 7.4] | 2.6 7.4 | Yes | 8.51 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RX87FYG1B905 | RX87FYG1B905 | Yes | 14.91 |
| 2 | 6FT44HW80X8C | 6FT44HW80X8C | Yes | 9.77 |
| 3 | JW44OPQA7509 | JW44OPQA7509 | Yes | 14.13 |
| 4 | 4UKCA3JWDVOJ | 4UKCA3JWDVOJ | Yes | 4.58 |
| 5 | QQ0TRB2G0JTK | QQ0TRB2G0JTK | Yes | 4.02 |
| 6 | BY2ID1V4ZBQP | BY2ID1V4ZBQP | Yes | 15.95 |
| 7 | O2H6QLWOIELO | O2H6QLWOIELO | Yes | 14.11 |
| 8 | 4RSUDJNI8N0Z | 4RSUDJNI8N0Z | Yes | 27.74 |
| 9 | LJVST8WNJFXL | LJVST8WNJFXL | Yes | 5.92 |
| 10 | HUBBXOCABH7D | HUBBXOCABH7D | Yes | 2.84 |
| 11 | 7W6ZTLGW9AZ9 | 7W6ZTLGW9AZ9 | Yes | 15.13 |
| 12 | ANPILBNHGMKY | ANPILBNHGMKY | Yes | 6.22 |
| 13 | BDUPO8ZRHV6Q | BDUPO8ZRHV6Q | Yes | 5.44 |
| 14 | XYRM1SVS2N8M | XYRM1SVS2N8M | Yes | 14.8 |
| 15 | 5I8BMDD4CHZV | 5I8BMDD4CHZV | Yes | 2.97 |
| 16 | T90WZZ1BSODL | T90WZZ1BSODL | Yes | 4.4 |
| 17 | 0SPQIG7UZKMU | 0SPQIG7UZKMU | Yes | 4.74 |
| 18 | Y8VJ40KS87QN | Y8VJ40KS87QN | Yes | 14.42 |
| 19 | 3Q3I4N74V6B1 | 3Q3I4N74V6B1 | Yes | 4.23 |
| 20 | U0L5FEVTK1JA | U0L5FEVTK1JA | Yes | 4.78 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7 | 7 | Yes | 4.34 |
| 2 | 4 | 4 | Yes | 10.31 |
| 3 | 4096 | 4096 | Yes | 17.82 |
| 4 | 3 | 3 | Yes | 14.11 |
| 5 | 9 | 9 | Yes | 14.3 |
| 6 | 9 | 9 | Yes | 9.4 |
| 7 | 1 | 1 | Yes | 11.29 |
| 8 | 36 | 36 | Yes | 3.71 |
| 9 | 67 | 67 | Yes | 11.04 |
| 10 | 26 | 26 | Yes | 11.93 |
| 11 | 4 | 4 | Yes | 11.04 |
| 12 | 243 | 243 | Yes | 10.14 |
| 13 | 64 | 64 | Yes | 10.58 |
| 14 | 60 | 60 | Yes | 9.75 |
| 15 | 10 | 10 | Yes | 6.29 |
| 16 | 19 | 19 | Yes | 5.76 |
| 17 | 6 | 6 | Yes | 3.9 |
| 18 | 20 | 20 | Yes | 13.95 |
| 19 | 60 | 60 | Yes | 10.48 |
| 20 | 31 | 31 | Yes | 14.58 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /(\\\<__< | `/(\\\<__<` | No | 6.61 |
| 2 | ((<(  _/) | ((<(  _/) | Yes | 13.43 |
| 3 | ()\__\<\\ | ()\__\<\\ | Yes | 10.34 |
| 4 | ( (  )<<  | ( (  )<< | No | 6.3 |
| 5 | /\)\(()/  | /\)\(()/ | No | 15.57 |
| 6 | (\(<<)(\< | (\(<<)(\< | Yes | 4.79 |
| 7 | \)()<\//  | \)()<\// | No | 4.11 |
| 8 | < (\_//\/ | < (\_//\/ | Yes | 11.55 |
| 9 | \)_\/ _\\ | \)_\/ _\\ | Yes | 11.93 |
| 10 | <<)_))//\ | <<)_))//\ | Yes | 6.18 |
| 11 | </( _/\\  | </( _/\ | No | 23.12 |
| 12 | \<_<(/\   | \<_<(/\ | No | 8.5 |
| 13 | <)_//<_(_ | <)_//<_(_ | Yes | 6.03 |
| 14 | <\)\ _<_\ | <\)\ _<_\ | Yes | 10.83 |
| 15 |  \() )_/( | \() )_/( | No | 14.64 |
| 16 | \<)_)(\/( | \<)_)(\/( | Yes | 16.97 |
| 17 |  \\ ))/<\ | \\ ))/<\ | No | 9.58 |
| 18 | )_/\(<\_< | )_/\(<\_< | Yes | 4.79 |
| 19 | \( < ()__ | \( < ()__ | Yes | 9.07 |
| 20 | )()< <_)( | )()< <_)( | Yes | 20.18 |
