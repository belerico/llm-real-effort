# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-27 10:13:25

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
| sudoku_game | 5832 | 34787 | 40619 | 11 | 9 | 33.92 | 678.39 |
| add_numbers | 3500 | 3665 | 7165 | 20 | 0 | 5.39 | 107.86 |
| counting_zeros | 4820 | 18963 | 23783 | 5 | 15 | 13.76 | 275.14 |
| task_decoding | 4820 | 7234 | 12054 | 17 | 3 | 7.85 | 156.92 |
| task_summation | 4636 | 12537 | 17173 | 19 | 1 | 14.48 | 289.54 |
| task_transcription | 3664 | 2498 | 6162 | 20 | 0 | 4.12 | 82.49 |
| task_sequences | 3560 | 7691 | 11251 | 18 | 2 | 6.28 | 125.52 |
| string_entry | 4035 | 4629 | 8664 | 12 | 8 | 7.74 | 154.78 |
| **TOTAL** | **34867** | **92004** | **126871** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 4 1 6 4 6 1 4 5 1 6 2 1 5 | 6 4 1 6 4 1 6 4 5 1 6 2 1 5 | No | 23.05 |
| 2 | 3 1 2 4 3 6 2 3 1 6 3 5 6 5 | 3 1 2 4 3 6 2 3 1 6 3 5 6 5 | Yes | 25.06 |
| 3 | 1 3 2 5 1 3 6 3 6 2 2 6 4 3 | 3 1 2 5 1 6 3 6 3 2 2 3 4 6 | No | 23.23 |
| 4 | 4 4 2 5 6 5 2 3 3 1 6 2 5 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with the easiest cells:  **Row 1:** 3 1 2 6 5 _ → Missing: 4  **Row 5:** 1 4 6 _ 3 5 → Missing: 2  **Column 4 analysis:** Already complete: 6,3,4,5,2,1  Now working through the remaining cells:  **Row 2:** _ _ _ 3 _ 1 - Column 3 needs 3 or 5; Row 2 needs 2,4,5,6 → Position [2,3] = 5 - Column 1 needs 4 or 5; with [2,3]=5, Position [2,1] = 4 - Remaining in Row 2: 2,6. Column 2 needs 2,3,5 → Position [2,2] = 2 - Position [2,5] = 6  **Row 3:** _ 6 1 4 _ _ - Column 1 needs 5 → Position [3,1] = 5 - Row 3 needs 2,3. Column 5 needs 1,2,6 → Position [3,5] = 2 - Position [3,6] = 3  **Row 4:** 2 _ 4 5 _ _ - Column 6 needs 6 → Position [4,6] = 6 - Row 4 needs 1,3. Column 5 needs 1 → Position [4,5] = 1 - Position [4,2] = 3  **Row 6:** 6 _ _ 1 4 2 - Column 2 needs 5 → Position [6,2] = 5 - Position [6,3] = 3  Missing numbers in reading order: Row 1: 4 Row 2: 4, 2, 5 Row 3: 5, 2, 3 Row 4: 3, 1, 6 Row 5: | No | 69.12 |
| 5 | 1 4 5 4 1 5 3 6 3 2 4 5 4 2 | 1 4 5 4 1 5 3 6 3 2 4 5 4 2 | Yes | 20.7 |
| 6 | 6 3 4 2 2 4 3 1 3 4 6 3 1 2 | 6 3 4 2 2 4 3 1 3 4 6 3 1 2 | Yes | 29.1 |
| 7 | 1 2 5 2 6 1 3 3 5 5 6 3 1 2 | 1 2 5 2 6 1 3 3 5 5 6 3 1 2 | Yes | 19.98 |
| 8 | 2 5 1 1 6 1 5 2 4 6 4 3 4 3 | TIMEOUT | No | 120.02 |
| 9 | 4 5 3 4 2 6 1 3 4 5 1 6 6 6 | 4 5 3 4 2 6 1 3 4 5 1 6 6 6 | Yes | 22.0 |
| 10 | 2 6 1 5 2 6 1 3 4 6 1 4 5 6 | 2 6 1 5 2 6 1 3 4 6 1 4 5 6 | Yes | 27.24 |
| 11 | 6 6 6 4 3 4 2 2 5 6 1 3 5 2 | 6 6 4 6 3 2 4 2 5 6 1 3 2 5 | No | 24.24 |
| 12 | 6 4 1 2 1 4 5 3 5 1 5 4 3 6 | 6 4 1 2 1 4 5 3 5 1 5 4 3 6 | Yes | 20.98 |
| 13 | 4 6 1 2 3 5 6 1 1 6 3 2 1 3 | 4 6 1 2 3 5 6 1 1 6 3 2 1 3 | Yes | 27.51 |
| 14 | 1 1 3 6 6 2 2 5 3 6 3 1 5 6 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the empty cells:  **Row 1:** 5 2 6 _ 4 3 → Missing: 1 → Cell (1,4) = **1**  **Row 6:** 1 5 2 _ 3 4 → Missing: 6 → Cell (6,4) = **6**  **Column 5:** 4 _ 5 1 2 3 → Missing: 6 → Cell (2,5) = **6**  **Column 6:** 3 2 1 6 _ 4 → Missing: 5 → Cell (5,6) = **5**  **Row 2:** 4 _ _ 5 | No | 28.77 |
| 15 | 5 6 2 1 4 6 6 2 3 5 6 5 1 4 | 5 6 2 1 4 6 6 2 3 5 6 5 1 4 | Yes | 17.57 |
| 16 | 2 6 1 1 4 2 4 1 5 3 6 3 5 2 | 2 6 1 1 4 2 4 1 5 3 6 3 5 2 | Yes | 24.04 |
| 17 | 6 5 1 2 2 4 2 6 5 2 4 6 5 2 | 6 2 1 5 2 4 2 6 5 2 4 6 5 2 | No | 74.05 |
| 18 | 3 6 4 1 6 2 2 1 2 4 3 1 4 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the empty cells:  **Row 1:** . 5 2 4 . 1 - Missing: 3, 6 - R1C1: Checking column 1 and top-left box → must be 3 - R1C5: Must be 6  **Row 2:** . . . 3 5 . - Missing: 1, 2, 4, 6 - R2C6: Column 6 needs 2 or 3; row needs 1,2,4,6 → must be 2 - R2C3: Column 3 needs 1 | No | 28.23 |
| 19 | 2 1 6 2 1 2 5 4 2 3 5 1 4 6 | 2 1 6 2 1 2 5 4 2 3 5 1 4 6 | Yes | 24.15 |
| 20 | 3 1 2 4 2 5 4 3 4 2 1 3 1 4 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step.  Starting with the given numbers: ``` 5 . 6 \| 4 . . 2 . 1 \| 5 3 6 -----+----- 1 6 . \| 3 4 . 6 1 . \| 2 5 . -----+----- . 5 3 \| 6 . . . 2 5 \| . 6 . ```  Solving systematically:  **Row 1:** Has 5,6,4 → needs 1,2,3 - R1C2: Column 2 has 6,1,5,2 → needs 3,4. Box needs 3,4 → **3** - R1C5 and R1C6: Need 1,2  **Row 2:** Has 2,1,5,3,6 → needs 4 - R2C2: **4**  **Row 3:** Has 1,6,3,4 → needs 2,5 - R3C3: Column 3 has 6,1,3,5 → needs 2,4. Row needs 2,5 → **2** - R3C6: **5**  **Row 4:** Has 6,1,2,5 → needs 3,4 - R4C3: Column 3 now needs 4 → **4** - R4C6: **3**  **Row 5:** Has 5,3,6 → needs 1,2,4 - R5C1: Column 1 has 5,2,1,6 → needs 3,4. Row needs 1,2,4 → **4** - R5C5 and R5C6: Need 1,2  **Row 6:** Has 2,5,6 → needs 1,3,4 - R6C1: Column 1 now needs 3 → **3** - R6C4: Column 4 has 4,5,3,2,6 → needs 1 → **1** - R6C6: **4**  **Final deduction:** - R5C5: Column 5 needs 1,2. Since R | No | 29.31 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1370 | 1370 | Yes | 4.72 |
| 2 | 1726 | 1726 | Yes | 3.32 |
| 3 | 1431 | 1431 | Yes | 3.82 |
| 4 | 2263 | 2263 | Yes | 3.92 |
| 5 | 1353 | 1353 | Yes | 3.68 |
| 6 | 2081 | 2081 | Yes | 17.15 |
| 7 | 2112 | 2112 | Yes | 3.39 |
| 8 | 1488 | 1488 | Yes | 4.06 |
| 9 | 1091 | 1091 | Yes | 10.19 |
| 10 | 1691 | 1691 | Yes | 3.58 |
| 11 | 2000 | 2000 | Yes | 5.29 |
| 12 | 1382 | 1382 | Yes | 2.62 |
| 13 | 1217 | 1217 | Yes | 3.59 |
| 14 | 1784 | 1784 | Yes | 4.18 |
| 15 | 1337 | 1337 | Yes | 3.67 |
| 16 | 1172 | 1172 | Yes | 13.98 |
| 17 | 1403 | 1403 | Yes | 3.66 |
| 18 | 1206 | 1206 | Yes | 4.13 |
| 19 | 1260 | 1260 | Yes | 5.05 |
| 20 | 1850 | 1850 | Yes | 3.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 | 71 | No | 12.53 |
| 2 | 38 | 38 | Yes | 9.81 |
| 3 | 69 | 68 | No | 17.15 |
| 4 | 48 | 48 | Yes | 12.03 |
| 5 | 37 | 33 | No | 10.41 |
| 6 | 47 | 45 | No | 11.25 |
| 7 | 39 | 37 | No | 9.34 |
| 8 | 64 | 46 | No | 7.51 |
| 9 | 38 | 33 | No | 13.31 |
| 10 | 54 | 37 | No | 9.71 |
| 11 | 52 | 50 | No | 13.15 |
| 12 | 44 | 40 | No | 9.97 |
| 13 | 62 | 62 | Yes | 12.49 |
| 14 | 57 | 49 | No | 11.1 |
| 15 | 75 | 67 | No | 7.57 |
| 16 | 60 | 58 | No | 12.47 |
| 17 | 50 | 45 | No | 58.96 |
| 18 | 47 | 47 | Yes | 12.24 |
| 19 | 46 | 46 | Yes | 10.86 |
| 20 | 67 | 59 | No | 13.25 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FIWDRHA | FIWDRHA | Yes | 8.47 |
| 2 | BCUOJNK | BCUOJNK | Yes | 6.12 |
| 3 | QZVJCTE | QZVJCTE | Yes | 5.38 |
| 4 | UZGEJPA | UZGEJPA | Yes | 5.66 |
| 5 | KTABRDY | KTABRDY | Yes | 9.55 |
| 6 | HESXOIT | HESXOIT | Yes | 5.51 |
| 7 | KXBJCDU | KXBJCDU | Yes | 4.87 |
| 8 | YJTASGC | YTJASGC | No | 3.94 |
| 9 | GJOAWDX | GJOWADX | No | 37.02 |
| 10 | LXCHGNZ | LXCHGNZ | Yes | 5.05 |
| 11 | PRWSJAD | PRWSJAD | Yes | 5.52 |
| 12 | TAIEMZD | TAIEZMD | No | 8.25 |
| 13 | BOKIPZW | BOKIPZW | Yes | 4.69 |
| 14 | AXOILCS | AXOILCS | Yes | 6.43 |
| 15 | BLMUDYQ | BLMUDYQ | Yes | 13.99 |
| 16 | SOBVIHM | SOBVIHM | Yes | 6.77 |
| 17 | EBCNTWJ | EBCNTWJ | Yes | 4.27 |
| 18 | BYOQAGC | BYOQAGC | Yes | 6.04 |
| 19 | AVTXIWQ | AVTXIWQ | Yes | 5.46 |
| 20 | KMTEZPF | KMTEZPF | Yes | 3.95 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.31 |
| 2 | [0.5, 9.5] | 9.5 0.5 | Yes | 12.43 |
| 3 | [3.0, 7.0] | 7.0 3.0 | Yes | 8.16 |
| 4 | [2.8, 7.2] | 2.8 7.2 | Yes | 9.03 |
| 5 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.77 |
| 6 | [1.6, 8.4] | 1.6 8.4 | Yes | 7.48 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 9.82 |
| 8 | [4.1, 5.9] | 5.9 4.1 | Yes | 6.05 |
| 9 | [2.7, 7.3] | 7.3 2.7 | Yes | 9.28 |
| 10 | [3.5, 6.5] | TIMEOUT | No | 120.02 |
| 11 | [3.3, 6.7] | 3.3 6.7 | Yes | 7.82 |
| 12 | [2.7, 7.3] | 7.3 2.7 | Yes | 11.55 |
| 13 | [3.8, 6.2] | 3.8 6.2 | Yes | 5.77 |
| 14 | [3.4, 6.6] | 6.6 3.4 | Yes | 7.52 |
| 15 | [0.3, 9.7] | 0.3 9.7 | Yes | 16.66 |
| 16 | [1.9, 8.1] | 1.9 8.1 | Yes | 6.79 |
| 17 | [1.2, 8.8] | 8.8 1.2 | Yes | 9.0 |
| 18 | [0.2, 9.8] | 9.8 0.2 | Yes | 8.47 |
| 19 | [0.6, 9.4] | 9.4 0.6 | Yes | 9.07 |
| 20 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.52 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CK0WB7ZBN2K9 | CK0WB7ZBN2K9 | Yes | 3.22 |
| 2 | 0P152KW2QCS5 | 0P152KW2QCS5 | Yes | 3.69 |
| 3 | H4FUMO7SWWRK | H4FUMO7SWWRK | Yes | 3.85 |
| 4 | BHNQ719OGLM1 | BHNQ719OGLM1 | Yes | 6.91 |
| 5 | 5GG9B3D8U4CP | 5GG9B3D8U4CP | Yes | 3.6 |
| 6 | ZHQ46QXNO6M7 | ZHQ46QXNO6M7 | Yes | 3.48 |
| 7 | 7MPD4G0XLL07 | 7MPD4G0XLL07 | Yes | 3.31 |
| 8 | G0EOWNZ8VCWS | G0EOWNZ8VCWS | Yes | 3.68 |
| 9 | 8640LX3ZKNZH | 8640LX3ZKNZH | Yes | 3.57 |
| 10 | RTRDOLYU1ITO | RTRDOLYU1ITO | Yes | 11.27 |
| 11 | B5L92552K5UU | B5L92552K5UU | Yes | 4.47 |
| 12 | 3CWG24OC53GH | 3CWG24OC53GH | Yes | 2.62 |
| 13 | 0F3JA15QGTRZ | 0F3JA15QGTRZ | Yes | 3.44 |
| 14 | 3ODTLPD49OVA | 3ODTLPD49OVA | Yes | 5.34 |
| 15 | MFI0CVH3F7J7 | MFI0CVH3F7J7 | Yes | 2.72 |
| 16 | Z80F38V9JJBT | Z80F38V9JJBT | Yes | 3.15 |
| 17 | 23CBM9FZ2KF6 | 23CBM9FZ2KF6 | Yes | 2.71 |
| 18 | G02MU88R5N6F | G02MU88R5N6F | Yes | 3.34 |
| 19 | BCSQ5T68EDDJ | BCSQ5T68EDDJ | Yes | 3.78 |
| 20 | OJ2OWEB1JRX8 | OJ2OWEB1JRX8 | Yes | 4.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 5 | No | 14.15 |
| 2 | 16 | 16 | Yes | 4.69 |
| 3 | 67 | 67 | Yes | 3.9 |
| 4 | 48 | 48 | Yes | 4.56 |
| 5 | 60 | 60 | Yes | 4.77 |
| 6 | 198 | 198 | Yes | 6.21 |
| 7 | 39 | 39 | Yes | 6.16 |
| 8 | 793 | 793 | Yes | 4.04 |
| 9 | 23 | 23 | Yes | 6.02 |
| 10 | 31 | 31 | Yes | 3.73 |
| 11 | 9 | 9 | Yes | 6.58 |
| 12 | 64 | 64 | Yes | 6.37 |
| 13 | 5 | 5 | Yes | 7.71 |
| 14 | 6 | 6 | Yes | 5.09 |
| 15 | 1440 | 1440 | Yes | 4.82 |
| 16 | 10 | 10 | Yes | 6.77 |
| 17 | 9 | 9 | Yes | 4.74 |
| 18 | 73 | 73 | Yes | 5.06 |
| 19 | 5 | 2 | No | 16.27 |
| 20 | 4 | 4 | Yes | 3.88 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (<\<(()\( | (<\<(()\( | Yes | 4.85 |
| 2 | /\ < _()) | /\ < _()) | Yes | 3.9 |
| 3 | /((<) </) | /((<) </) | Yes | 5.19 |
| 4 | /_ )  <<_ | /_ )  <<_ | Yes | 4.68 |
| 5 | <<</(/\_\ | <<</(/\_\ | Yes | 4.97 |
| 6 | <</\()_</ | <</\()_</ | Yes | 7.24 |
| 7 | )/_)_/(<_ | )/_)_/(<_ | Yes | 10.3 |
| 8 |  _\<(_(() | _\<(_(() | No | 5.12 |
| 9 | /_(_)(  _ | /_(_)(  _ | Yes | 4.28 |
| 10 |  (</) / \ | (</) / \ | No | 6.4 |
| 11 | \)<<()  _ | \)<<()  _ | Yes | 3.41 |
| 12 |  )( _)<\( | )(  _)<\( | No | 9.92 |
| 13 | /_ //_\\  | /_ //_\ | No | 6.98 |
| 14 | (\/))()<( | (\/))()<( | Yes | 14.95 |
| 15 |  \) / <(/ | \) / <(/ | No | 5.11 |
| 16 | ))(_<_\(/ | ))(_<_\(/ | Yes | 4.0 |
| 17 | /((< /_(/ | /((< /_(/ | Yes | 24.34 |
| 18 |   /_/_)_( | /_/_)_( | No | 6.41 |
| 19 |  <\<<_(/( | <\<<_(/( | No | 16.59 |
| 20 |  \_ ( <(( | \_  ( <(( | No | 6.15 |
