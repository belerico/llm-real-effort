# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-27 10:23:16

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
| sudoku_game | 4932 | 38363 | 43295 | 0 | 20 | 32.35 | 647.13 |
| add_numbers | 3046 | 3974 | 7020 | 20 | 0 | 10.47 | 209.33 |
| counting_zeros | 6104 | 36356 | 42460 | 20 | 0 | 23.93 | 478.72 |
| task_decoding | 4314 | 5789 | 10103 | 20 | 0 | 9.61 | 192.24 |
| task_summation | 4358 | 10495 | 14853 | 20 | 0 | 10.08 | 201.69 |
| task_transcription | 3034 | 3748 | 6782 | 20 | 0 | 10.88 | 217.7 |
| task_sequences | 3031 | 6821 | 9852 | 19 | 1 | 12.95 | 259.09 |
| string_entry | 3346 | 7715 | 11061 | 15 | 5 | 12.03 | 240.66 |
| **TOTAL** | **32165** | **113261** | **145426** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 3 1 4 1 5 2 6 3 2 5 6 1 3 | 2 3 1 4 1 2 5 6 3 5 2 6 1 3 | No | 19.77 |
| 2 | 3 6 1 5 6 4 5 3 2 6 5 6 4 3 | 1 6 3 5 6 4 5 3 2 6 5 6 4 3 | No | 26.73 |
| 3 | 4 6 5 1 2 3 6 3 2 4 5 2 6 4 | To solve the 6x6 Sudoku puzzle, we must fill the grid so that every row, column, and 3x2 box (3 rows, 2 columns) contains the numbers 1 through 6 exactly once.   Let's deduce the missing values: 1. **Column 1:** Contains 3, 5, 1, 6, 2. | No | 39.92 |
| 4 | 1 1 2 6 2 5 6 6 5 4 3 3 2 4 | To solve this 6×6 Sudoku puzzle, we can determine the missing numbers by ensuring each row and column contains the digits 1 through 6 exactly once.   Here is the step-by-step logical deduction: * **Row 1:** 3 4 2 \| 5 . 6 — The only missing number is **1** (R1C5 | No | 29.96 |
| 5 | 1 6 3 4 5 1 6 2 3 5 2 2 6 1 | 1 3 1 4 5 5 4 2 2 6 2 6 3 5 2 1 6 1 | No | 19.82 |
| 6 | 3 4 3 6 2 6 4 3 6 5 3 6 1 5 | To solve the 6x6 Sudoku puzzle, we can deduce the missing numbers step-by-step:  1. **Row 1** has `_ 4 2 \| 6 5 1`. The only missing number is **3**. So, R1C1 = 3. 2. **Column 1** now has `3, 1 | No | 29.45 |
| 7 | 3 6 1 2 5 3 5 4 5 3 1 3 2 1 | 3 6 1 2 3 5 5 4 5 3 1 2 1 3 2 1 | No | 30.0 |
| 8 | 6 3 6 5 3 4 1 5 3 6 5 1 4 3 | 6. Col 2: 2, ., ., ., 3, . Col 3: 4, 2, ., ., 6, 5. Col 4: ., 3, 5, 1, 2, . Col 5: 1, 4, 2, ., ., . Col 6: ., ., 6, | No | 25.29 |
| 9 | 2 1 1 4 4 5 6 3 1 3 1 5 5 4 | To solve this 6x6 Sudoku puzzle, we first need to determine the missing numbers in each row, column, and 2×3 box. Note that based on the placement of the numbers, the boxes are 3 rows by 2 columns (despite the visual cross in the middle of the grid).   Let's fill in the grid logically: - **Row 2 | No | 29.96 |
| 10 | 2 6 3 2 6 2 3 5 5 2 1 4 6 3 | To solve the Sudoku puzzle, we need to fill the empty cells so that each row, column, and 2×3 box contains the numbers 1 through 6 exactly once.   Let's analyze the grid: Row 1: 4 5 3 \| . . 1 Row 2: . 1 4 \| 6 5 . | No | 24.96 |
| 11 | 4 6 3 4 5 3 4 6 2 1 1 5 3 2 | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 17.68 |
| 12 | 4 6 1 2 2 3 2 6 5 4 3 2 6 4 | 6 4 1 2 2 3 2 4 5 6 3 4 6 | No | 30.34 |
| 13 | 6 2 5 4 1 3 5 1 5 6 3 2 6 1 | 6 2 5 1 4 3 5 1 6 3 1 2 2 1 | No | 26.03 |
| 14 | 3 5 2 3 6 2 3 1 4 4 3 1 4 3 |  | No | 29.59 |
| 15 | 2 5 4 1 2 5 1 5 4 5 3 1 6 3 | 2 4 5 1 2 5 5 1 5 4 3 6 1 3 | No | 28.07 |
| 16 | 3 2 1 5 5 2 2 3 5 1 2 6 3 4 | To solve the 6x6 Sudoku puzzle, we first deduce the box dimensions. Given the layout and the numbers, the boxes must be 3 rows high and 2 columns wide to avoid duplicate numbers in any box (for instance, a 2x3 box would place two 4s in the middle-left box and two 6s in the top-right box). | No | 29.32 |
| 17 | 1 2 6 2 4 5 6 1 2 6 4 1 4 3 | To solve the 6x6 Sudoku puzzle, we must fill the grid so that every row, column, and 3x2 box contains the numbers 1 through 6 exactly once. (Note: Based on the grid layout and the numbers provided, the boxes are 3 rows by 2 columns).  Here is the step-by-step logical deduction:  1. **Row | No | 29.61 |
| 18 | 5 3 1 1 6 3 4 5 1 6 6 5 4 3 | 5 1 3 6 1 4 3 1 5 6 3 4 3 4 | No | 30.74 |
| 19 | 3 6 4 6 4 2 4 5 5 4 3 1 5 2 | 3 6 4 6 4 4 2 5 5 4 1 5 2 | No | 118.91 |
| 20 | 1 3 2 1 2 5 4 4 3 5 5 3 3 1 | 1 2 3 1 2 4 4 3 5 5 3 1 3 | No | 30.94 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1559 | 1559 | Yes | 14.55 |
| 2 | 1168 | 1168 | Yes | 4.27 |
| 3 | 1958 | 1958 | Yes | 3.94 |
| 4 | 2193 | 2193 | Yes | 10.77 |
| 5 | 1577 | 1577 | Yes | 7.88 |
| 6 | 1608 | 1608 | Yes | 35.71 |
| 7 | 2129 | 2129 | Yes | 3.69 |
| 8 | 1741 | 1741 | Yes | 11.64 |
| 9 | 2602 | 2602 | Yes | 5.08 |
| 10 | 1763 | 1763 | Yes | 15.24 |
| 11 | 1578 | 1578 | Yes | 10.75 |
| 12 | 1990 | 1990 | Yes | 14.88 |
| 13 | 1504 | 1504 | Yes | 5.05 |
| 14 | 2239 | 2239 | Yes | 7.12 |
| 15 | 1408 | 1408 | Yes | 11.22 |
| 16 | 1734 | 1734 | Yes | 11.29 |
| 17 | 1531 | 1531 | Yes | 10.5 |
| 18 | 1276 | 1276 | Yes | 10.5 |
| 19 | 1818 | 1818 | Yes | 5.76 |
| 20 | 1863 | 1863 | Yes | 9.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 54 | Yes | 15.71 |
| 2 | 61 | 61 | Yes | 26.18 |
| 3 | 50 | 50 | Yes | 25.94 |
| 4 | 41 | 41 | Yes | 20.06 |
| 5 | 59 | 59 | Yes | 32.72 |
| 6 | 58 | 58 | Yes | 24.64 |
| 7 | 73 | 73 | Yes | 23.86 |
| 8 | 49 | 49 | Yes | 18.58 |
| 9 | 55 | 55 | Yes | 19.52 |
| 10 | 69 | 69 | Yes | 28.85 |
| 11 | 73 | 73 | Yes | 27.63 |
| 12 | 62 | 62 | Yes | 29.27 |
| 13 | 70 | 70 | Yes | 26.14 |
| 14 | 57 | 57 | Yes | 23.74 |
| 15 | 68 | 68 | Yes | 26.87 |
| 16 | 61 | 61 | Yes | 30.87 |
| 17 | 61 | 61 | Yes | 12.28 |
| 18 | 48 | 48 | Yes | 24.1 |
| 19 | 68 | 68 | Yes | 24.06 |
| 20 | 66 | 66 | Yes | 17.68 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OBMXJLP | OBMXJLP | Yes | 14.3 |
| 2 | LZTHNDJ | LZTHNDJ | Yes | 7.4 |
| 3 | OZDVQJI | OZDVQJI | Yes | 4.07 |
| 4 | VGXZHLR | VGXZHLR | Yes | 5.68 |
| 5 | XSGHZMI | XSGHZMI | Yes | 6.75 |
| 6 | MCQEWPT | MCQEWPT | Yes | 6.27 |
| 7 | FUGSZIO | FUGSZIO | Yes | 14.21 |
| 8 | SFJIMTN | SFJIMTN | Yes | 15.69 |
| 9 | EBGLPRS | EBGLPRS | Yes | 16.75 |
| 10 | VEPIHAJ | VEPIHAJ | Yes | 5.51 |
| 11 | BEZNSPD | BEZNSPD | Yes | 5.78 |
| 12 | MOHICTP | MOHICTP | Yes | 17.59 |
| 13 | EGLYWPC | EGLYWPC | Yes | 10.29 |
| 14 | CBSDWOX | CBSDWOX | Yes | 11.07 |
| 15 | LCJBUYT | LCJBUYT | Yes | 7.56 |
| 16 | RSPOZME | RSPOZME | Yes | 16.08 |
| 17 | ERCJSZT | ERCJSZT | Yes | 8.4 |
| 18 | PKNDITA | PKNDITA | Yes | 8.56 |
| 19 | ZHFBDUP | ZHFBDUP | Yes | 5.56 |
| 20 | HVNDMQS | HVNDMQS | Yes | 4.71 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.2, 5.8] | 4.2 5.8 | Yes | 7.72 |
| 2 | [0.7, 9.3] | 9.3 0.7 | Yes | 16.42 |
| 3 | [4.0, 6.0] | 6.0 4.0 | Yes | 17.56 |
| 4 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.85 |
| 5 | [3.5, 6.5] | 3.5 6.5 | Yes | 7.73 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 10.82 |
| 7 | [0.9, 9.1] | 0.9 9.1 | Yes | 9.3 |
| 8 | [5.0, 5.0] | 5.0 5.0 | Yes | 7.43 |
| 9 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.93 |
| 10 | [3.9, 6.1] | 3.9 6.1 | Yes | 8.26 |
| 11 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.12 |
| 12 | [2.1, 7.9] | 2.1 7.9 | Yes | 7.47 |
| 13 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.91 |
| 14 | [4.0, 6.0] | 4.0 6.0 | Yes | 8.63 |
| 15 | [0.7, 9.3] | 0.7 9.3 | Yes | 6.53 |
| 16 | [2.3, 7.7] | 2.3 7.7 | Yes | 7.24 |
| 17 | [3.2, 6.8] | 3.2 6.8 | Yes | 5.76 |
| 18 | [2.8, 7.2] | 2.8 7.2 | Yes | 14.56 |
| 19 | [0.1, 9.9] | 0.1 9.9 | Yes | 17.26 |
| 20 | [2.0, 8.0] | 2.0 8.0 | Yes | 18.19 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WRAPDIW1GGL8 | WRAPDIW1GGL8 | Yes | 13.74 |
| 2 | JHBWIX86NHJR | JHBWIX86NHJR | Yes | 5.58 |
| 3 | IMBEIYK4QDTE | IMBEIYK4QDTE | Yes | 14.73 |
| 4 | YIZSWLPSFSY8 | YIZSWLPSFSY8 | Yes | 3.06 |
| 5 | VV57CJ10HFVW | VV57CJ10HFVW | Yes | 15.2 |
| 6 | 4XNOQ638JHY9 | 4XNOQ638JHY9 | Yes | 3.41 |
| 7 | TM88ECXFQL5B | TM88ECXFQL5B | Yes | 3.97 |
| 8 | 64BXX1RRBX8P | 64BXX1RRBX8P | Yes | 14.33 |
| 9 | RXXPZ3UWKPTH | RXXPZ3UWKPTH | Yes | 5.16 |
| 10 | 69YKA07R8EGS | 69YKA07R8EGS | Yes | 14.02 |
| 11 | VP93NKGXVU0I | VP93NKGXVU0I | Yes | 10.94 |
| 12 | XC9UGDUFVP7D | XC9UGDUFVP7D | Yes | 14.87 |
| 13 | 5LNU8A3NOIVZ | 5LNU8A3NOIVZ | Yes | 4.2 |
| 14 | FVG0Z5YBG7YV | FVG0Z5YBG7YV | Yes | 15.01 |
| 15 | ZH5NKZO8JR25 | ZH5NKZO8JR25 | Yes | 15.51 |
| 16 | 6VECWU5R38VV | 6VECWU5R38VV | Yes | 11.75 |
| 17 | IEQ24ELOJ9XS | IEQ24ELOJ9XS | Yes | 22.4 |
| 18 | FV7WOUYX1B0V | FV7WOUYX1B0V | Yes | 5.06 |
| 19 | 7UEIARZR1GDO | 7UEIARZR1GDO | Yes | 9.39 |
| 20 | 2VTRVA6P453W | 2VTRVA6P453W | Yes | 15.36 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 4.89 |
| 2 | 5 | 5 | Yes | 5.05 |
| 3 | 63 | 63 | Yes | 3.92 |
| 4 | 48 | 48 | Yes | 4.62 |
| 5 | 26 | 26 | Yes | 4.78 |
| 6 | 9 | 9 | Yes | 14.77 |
| 7 | 7680 | 7680 | Yes | 14.64 |
| 8 | 793 | 793 | Yes | 13.07 |
| 9 | 3 | 3 | Yes | 16.4 |
| 10 | 65 | 65 | Yes | 9.73 |
| 11 | 60 | 60 | Yes | 10.45 |
| 12 | 16 | 16 | Yes | 9.54 |
| 13 | 5 | 14 | No | 30.61 |
| 14 | 10 | 10 | Yes | 15.66 |
| 15 | 4 | 4 | Yes | 13.85 |
| 16 | 28 | 28 | Yes | 14.0 |
| 17 | 19 | 19 | Yes | 10.06 |
| 18 | 20 | 20 | Yes | 12.56 |
| 19 | 60 | 60 | Yes | 14.15 |
| 20 | 67 | 67 | Yes | 36.32 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (/<_(<) _ | (/<_(<) _ | Yes | 15.01 |
| 2 | <  _(\\_\ | <  _(\\_\ | Yes | 12.98 |
| 3 | _<(_<\  _ | _<(_<\  _ | Yes | 6.65 |
| 4 | _\\\_(_\/ | _\\\_(_\/ | Yes | 17.82 |
| 5 |  _/\)/\__ | _/\)/\__ | No | 6.58 |
| 6 | <\\\\\<\) | <\\\\\<\) | Yes | 19.19 |
| 7 | _))) __ < | _))) __ < | Yes | 14.66 |
| 8 | (/ ) (_/_ | (/ ) (_/_ | Yes | 15.47 |
| 9 | << )(_<)) | << )(_<)) | Yes | 4.65 |
| 10 |  <\)//\)( | <\)//\)( | No | 9.17 |
| 11 |  \/) ) </ | \/) ) </ | No | 11.39 |
| 12 | //< )  <_ | //< )  <_ | Yes | 10.64 |
| 13 | <</\<\/)  | <</\<\/) | No | 13.59 |
| 14 | /(_)))<_< | /(_)))<_< | Yes | 17.68 |
| 15 | /< <\\<\) | /< <\\<\) | Yes | 7.19 |
| 16 | \//()<(__ | \//()<(__ | Yes | 4.25 |
| 17 | </ \<\_(  | </ \<\_( | No | 32.26 |
| 18 | _\\\/ ) \ | _\\\/ ) \ | Yes | 10.08 |
| 19 | _\\<((< ( | _\\<((< ( | Yes | 4.29 |
| 20 | ) <(<<(_( | ) <(<<(_( | Yes | 7.08 |
