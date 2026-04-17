# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-27 09:59:26

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
| sudoku_game | 5498 | 34731 | 40229 | 3 | 17 | 8.47 | 169.5 |
| add_numbers | 2836 | 5060 | 7896 | 20 | 0 | 3.33 | 66.65 |
| counting_zeros | 5608 | 31811 | 37419 | 12 | 8 | 14.27 | 285.38 |
| task_decoding | 4132 | 16827 | 20959 | 19 | 1 | 5.97 | 119.4 |
| task_summation | 4164 | 13290 | 17454 | 20 | 0 | 4.54 | 90.79 |
| task_transcription | 2825 | 4802 | 7627 | 20 | 0 | 4.49 | 89.84 |
| task_sequences | 2821 | 5807 | 8628 | 20 | 0 | 4.78 | 95.52 |
| string_entry | 3146 | 18101 | 21247 | 5 | 15 | 5.79 | 115.85 |
| **TOTAL** | **31030** | **130429** | **161459** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 2 6 1 3 6 4 5 4 1 1 5 4 | 5 1 2 6 1 3 6 5 4 4 1 1 4 5 | No | 8.59 |
| 2 | 2 1 3 6 1 4 3 1 1 4 6 2 3 4 | 2 6 3 4 1 6 1 3 1 4 6 2 4 3 | No | 8.15 |
| 3 | 3 1 2 3 4 3 6 5 3 1 4 2 5 4 | 1 3 2 3 3 4 5 3 4 2 5 1 | No | 6.87 |
| 4 | 1 4 5 3 5 1 6 3 1 2 5 6 4 1 | 1 4 5 3 1 6 3 6 1 2 5 | No | 9.19 |
| 5 | 4 5 1 6 1 2 3 6 4 5 1 5 4 4 | 4 5 1 6 1 2 3 6 4 5 1 5 4 4 | Yes | 8.84 |
| 6 | 3 1 4 4 5 1 2 5 4 1 2 3 5 6 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Puzzle Analysis:** - Row 1: 2 . 6 \| . 5 4 → Missing: 1, 3. R1C2=3, | No | 7.05 |
| 7 | 3 2 6 4 4 5 2 5 4 1 3 1 6 5 | 3 2 4 6 6 5 2 5 4 1 3 6 5 1 | No | 7.9 |
| 8 | 3 6 5 3 1 4 2 5 2 3 4 5 3 6 | 3 6 5 3 5 4 2 1 2 3 4 6 3 5 | No | 25.41 |
| 9 | 6 3 3 2 4 1 5 2 5 3 6 2 6 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  Given grid: . 2 1 \| . 4 5 . 5 . \| . 6 . -----+----- 1 4 . \| 6 . 3 . . . \| . 1 4 -----+----- 2 1 4 \| 5 3 6 4 . . \| 1 5 2  1.  **Row 1:** Missing 3, 6. Column 4 needs 2, 3, 4. R1C4 is 3, so R1C1 is 6. Row 1: 6 2 1 \| 3 4 5. 2.  **Column 4:** Missing 2, 4. R4C4 cannot be 4 (Row 4 has 4), so R4C4 = 2 and R2C4 = 4. 3.  **Row 2:** Missing 1, 2, 3. R2C1 = 3, R2C3 = 2, R2C6 = 1. Row 2: 3 5 2 \| 4 6 1. 4.  **Column 6:** Missing 4. R3C6 is 3, R4C6 is 4, R5C6 is 6, R6C6 is 2, R1C6 is 5, R2C6 is 1. All filled. 5.  **Row 3:** Missing 2, 5. Column 3 has 1, 2, 4. R3C3 = 5, R3C5 = 2. Row 3: 1 4 5 \| 6 2 3. 6.  **Row 4:** Missing 3, 5, 6. R4C1 = 5, R4C2 = 6, R4C3 = 3. Row 4: 5 6 3 \| 2 1 4. 7.  **Row 6:** Missing 3, 6. Column 2 has 2, 5, 4, 6, 1. R6C2 = 3, R6C3 = 6. Row 6: 4 3 6 \| 1 5 2.  Filled grid: 6 2 1 \| 3 4 5 3 5 2 \| 4 6 1 1 4 5 \| 6 2 3 5 6 3 \| 2 1 4 2 1 4 \| 5 3 6 4 3 6 \| 1 5 2  Missing numbers in reading order: R1C1=6, R1C4=3 R2C1=3, R2C3=2, R2C4=4, R2C6=1 R3C3=5, R3C5=2 R4C1=5, R4C2=6 | No | 9.66 |
| 10 | 6 4 2 4 4 2 5 3 3 2 6 2 3 2 | 6 4 2 2 4 3 2 6 2 | No | 9.87 |
| 11 | 4 3 5 5 4 5 6 3 3 4 1 2 5 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1–6 exactly once.  **Original Puzzle:** . 6 1 \| 2 . . 2 1 3 \| . 6 . -----+----- 3 . . \| 4 1 2 5 . 4 \| 1 2 6 -----+----- 6 2 5 \| . . . 1 4 . \| 6 . .  **Step-by-step logic:** 1.  **Row 1:** The missing numbers are 3, 4, 5. Column 1 is missing 4, so R1C1=4. Column 5 and 6 need 3 and 5. Based on column constraints, R1C5=3 and R1C6=5. 2.  **Row 2:** The missing numbers are 4, 5. Column 4 needs 3 or 5, but 5 is already in column 4 (R5C4), so R2C4=5. R2C6=4. 3.  **Row 3:** The missing numbers are 5, 6. R3C2=5, R3C3=6. 4.  **Row 4:** The missing number is 3. R4C2=3. 5.  **Row 5:** The missing numbers are 1, 3, 4. R5C4=3, R5C5=4, R5C6=1. 6.  **Row 6:** The | No | 9.21 |
| 12 | 5 4 3 5 1 3 2 6 4 1 2 6 4 1 | 5 4 3 5 1 3 6 2 4 2 1 1 4 6 | No | 7.08 |
| 13 | 2 3 6 4 2 5 3 1 5 4 1 6 4 5 | 2 3 6 4 2 5 3 1 5 4 1 6 4 5 | Yes | 6.55 |
| 14 | 4 6 1 5 2 5 1 3 2 4 4 6 4 2 | 4 6 1 5 2 5 1 3 2 4 4 6 4 2 | Yes | 4.25 |
| 15 | 2 1 3 3 1 1 5 1 4 2 6 6 3 1 | 2 1 3 1 5 3 1 2 6 3 | No | 6.61 |
| 16 | 2 4 3 5 6 2 5 3 2 1 5 3 6 2 | 2 4 3 5 6 2 5 2 3 1 5 3 6 2 | No | 5.18 |
| 17 | 3 6 1 6 4 4 5 6 4 1 5 2 4 6 | 3 6 1 6 4 4 5 6 4 5 2 4 6 | No | 8.08 |
| 18 | 4 2 6 1 6 1 2 5 6 1 5 6 3 4 | 6 4 2 1 1 2 6 5 6 6 1 5 3 4 | No | 7.71 |
| 19 | 6 5 2 6 6 2 2 3 1 1 3 6 3 1 | 6 5 6 2 2 6 2 3 1 1 3 6 3 1 | No | 5.44 |
| 20 | 1 5 2 3 1 5 2 2 3 4 5 6 3 4 | 1 5 3 2 1 5 2 2 3 4 5 6 3 4 | No | 7.83 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 766 | 766 | Yes | 1.9 |
| 2 | 1357 | 1357 | Yes | 7.84 |
| 3 | 2044 | 2044 | Yes | 2.44 |
| 4 | 907 | 907 | Yes | 2.9 |
| 5 | 2188 | 2188 | Yes | 1.63 |
| 6 | 1335 | 1335 | Yes | 8.13 |
| 7 | 1528 | 1528 | Yes | 3.41 |
| 8 | 2933 | 2933 | Yes | 2.59 |
| 9 | 907 | 907 | Yes | 2.14 |
| 10 | 1639 | 1639 | Yes | 2.12 |
| 11 | 1497 | 1497 | Yes | 2.01 |
| 12 | 1208 | 1208 | Yes | 7.42 |
| 13 | 2101 | 2101 | Yes | 4.57 |
| 14 | 817 | 817 | Yes | 2.12 |
| 15 | 1013 | 1013 | Yes | 1.88 |
| 16 | 1472 | 1472 | Yes | 2.21 |
| 17 | 1192 | 1192 | Yes | 2.81 |
| 18 | 1829 | 1829 | Yes | 2.44 |
| 19 | 1554 | 1554 | Yes | 3.12 |
| 20 | 1630 | 1630 | Yes | 2.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 45 | 43 | No | 6.13 |
| 2 | 43 | 43 | Yes | 9.4 |
| 3 | 46 | 46 | Yes | 11.24 |
| 4 | 43 | 43 | Yes | 5.68 |
| 5 | 46 | 44 | No | 9.01 |
| 6 | 62 | 62 | Yes | 8.64 |
| 7 | 69 | 69 | Yes | 9.33 |
| 8 | 36 | 36 | Yes | 6.91 |
| 9 | 51 | 51 | Yes | 11.93 |
| 10 | 47 | 43 | No | 6.63 |
| 11 | 56 | 53 | No | 7.15 |
| 12 | 67 | 66 | No | 7.94 |
| 13 | 65 | TIMEOUT | No | 120.02 |
| 14 | 44 | 44 | Yes | 9.56 |
| 15 | 38 | 38 | Yes | 6.37 |
| 16 | 36 | 36 | Yes | 17.17 |
| 17 | 66 | 66 | Yes | 6.89 |
| 18 | 36 | 36 | Yes | 6.18 |
| 19 | 62 | 58 | No | 8.41 |
| 20 | 61 | 58 | No | 10.78 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AVNWGBM | AVNWGBM | Yes | 8.86 |
| 2 | DNVKPUI | DNVKPUI | Yes | 2.9 |
| 3 | AESQRKY | AESQRKY | Yes | 4.71 |
| 4 | NEUJIHO | NEUJIHO | Yes | 12.23 |
| 5 | JFDKHUV | JFDKHUV | Yes | 1.98 |
| 6 | KVPGHQR | KVPGHQR | Yes | 6.27 |
| 7 | GHBJYTP | GHBJYTP | Yes | 2.93 |
| 8 | ANPHESG | ANPHESG | Yes | 3.63 |
| 9 | OGMYAUN | OGMYAUN | Yes | 2.37 |
| 10 | VZSLRDG | VZSLRDG | Yes | 6.29 |
| 11 | SWELQYP | SWEQLYP | No | 5.82 |
| 12 | RBKZXTM | RBKZXTM | Yes | 10.14 |
| 13 | LBQGKNR | LBQGKNR | Yes | 5.0 |
| 14 | OAWMKIF | OAWMKIF | Yes | 7.4 |
| 15 | YMKXHCR | YMKXHCR | Yes | 5.94 |
| 16 | NWMJFUK | NWMJFUK | Yes | 6.21 |
| 17 | NHUJEKC | NHUJEKC | Yes | 4.37 |
| 18 | BOESAIZ | BOESAIZ | Yes | 2.42 |
| 19 | XOHLPJW | XOHLPJW | Yes | 15.52 |
| 20 | IDQXWMY | IDQXWMY | Yes | 4.38 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.8, 5.2] | 4.8 5.2 | Yes | 3.36 |
| 2 | [1.9, 8.1] | 1.9 8.1 | Yes | 3.81 |
| 3 | [0.6, 9.4] | 9.4 0.6 | Yes | 2.67 |
| 4 | [0.7, 9.3] | 0.7 9.3 | Yes | 8.9 |
| 5 | [0.5, 9.5] | 0.5 9.5 | Yes | 10.19 |
| 6 | [4.4, 5.6] | 4.4 5.6 | Yes | 2.81 |
| 7 | [3.8, 6.2] | 3.8 6.2 | Yes | 3.33 |
| 8 | [0.5, 9.5] | 0.5 9.5 | Yes | 3.87 |
| 9 | [3.8, 6.2] | 3.8 6.2 | Yes | 3.0 |
| 10 | [3.8, 6.2] | 3.8 6.2 | Yes | 5.17 |
| 11 | [1.5, 8.5] | 1.5 8.5 | Yes | 3.6 |
| 12 | [4.4, 5.6] | 4.4 5.6 | Yes | 3.84 |
| 13 | [3.9, 6.1] | 3.9 6.1 | Yes | 3.9 |
| 14 | [2.9, 7.1] | 7.1 2.9 | Yes | 3.44 |
| 15 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.65 |
| 16 | [2.8, 7.2] | 7.2 2.8 | Yes | 3.91 |
| 17 | [4.9, 5.1] | 5.1 4.9 | Yes | 3.74 |
| 18 | [1.0, 9.0] | 1.0 9.0 | Yes | 4.08 |
| 19 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.45 |
| 20 | [4.5, 5.5] | 5.5 4.5 | Yes | 3.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | U25ILINRY8AA | U25ILINRY8AA | Yes | 3.16 |
| 2 | W7UOC9CDJ4NI | W7UOC9CDJ4NI | Yes | 18.32 |
| 3 | H0H66CIXISOP | H0H66CIXISOP | Yes | 2.13 |
| 4 | KM63CHK6E12M | KM63CHK6E12M | Yes | 9.07 |
| 5 | UXAXTRW3HMAF | UXAXTRW3HMAF | Yes | 1.58 |
| 6 | V0QEXGMBAVVW | V0QEXGMBAVVW | Yes | 1.98 |
| 7 | KP1N1M4IPXXK | KP1N1M4IPXXK | Yes | 3.23 |
| 8 | HKJ3OC4SIIBW | HKJ3OC4SIIBW | Yes | 1.7 |
| 9 | MM3LWQ6N93Y2 | MM3LWQ6N93Y2 | Yes | 1.92 |
| 10 | OILULSCGK2GG | OILULSCGK2GG | Yes | 4.2 |
| 11 | FIM2LH6CEAN7 | FIM2LH6CEAN7 | Yes | 2.82 |
| 12 | 72KIHA2QDS8Y | 72KIHA2QDS8Y | Yes | 1.57 |
| 13 | 0QXI1BBBLPG6 | 0QXI1BBBLPG6 | Yes | 1.87 |
| 14 | Q01GE3H4QLSL | Q01GE3H4QLSL | Yes | 12.18 |
| 15 | V6P37JBFSOY4 | V6P37JBFSOY4 | Yes | 2.08 |
| 16 | K6RIY1T017N6 | K6RIY1T017N6 | Yes | 1.76 |
| 17 | VPOXFAIKD0EP | VPOXFAIKD0EP | Yes | 2.33 |
| 18 | E7VUPGWQT7RI | E7VUPGWQT7RI | Yes | 2.16 |
| 19 | OKVS8GZEQ6HN | OKVS8GZEQ6HN | Yes | 2.68 |
| 20 | EO10IQDMQ4FD | EO10IQDMQ4FD | Yes | 13.1 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 2.32 |
| 2 | 5 | 5 | Yes | 8.02 |
| 3 | 36 | 36 | Yes | 1.93 |
| 4 | 9 | 9 | Yes | 1.99 |
| 5 | 16 | 16 | Yes | 2.41 |
| 6 | 4 | 4 | Yes | 2.06 |
| 7 | 63 | 63 | Yes | 2.38 |
| 8 | 7680 | 7680 | Yes | 2.16 |
| 9 | 23 | 23 | Yes | 1.86 |
| 10 | 73 | 73 | Yes | 2.19 |
| 11 | 4 | 4 | Yes | 2.11 |
| 12 | 65 | 65 | Yes | 2.28 |
| 13 | 60 | 60 | Yes | 3.78 |
| 14 | 28 | 28 | Yes | 2.27 |
| 15 | 44 | 44 | Yes | 1.88 |
| 16 | 48 | 48 | Yes | 2.35 |
| 17 | 7 | 7 | Yes | 7.24 |
| 18 | 39 | 39 | Yes | 7.95 |
| 19 | 243 | 243 | Yes | 36.21 |
| 20 | 793 | 793 | Yes | 2.13 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _\)_)(_)( | /\) <(_<) | No | 7.0 |
| 2 | (_/ \(/_\ | (_/ \(/_\ | Yes | 5.12 |
| 3 | /<(<<)__) | /\) <(_<) | No | 5.68 |
| 4 | _\(_\  () | _\(_  ) | No | 5.41 |
| 5 | )) )\)</< | )) )\)</< | Yes | 13.01 |
| 6 | <\ \<\ )/ | <\ \ < )/ | No | 5.79 |
| 7 |  (( _ ()) | (_ ()) | No | 5.9 |
| 8 | ))(</))__ | ))(</))__ | Yes | 5.06 |
| 9 | <\_(\ <_< | <\_(\ <(_<) | No | 4.99 |
| 10 |  ((\((_ ) | ((\((_ ) | No | 6.5 |
| 11 | \\< /\))_ | \\< /\)) | No | 5.93 |
| 12 | < _) //_< | < _)//_< | No | 5.01 |
| 13 | ___)_\\(_ | ___)_\\(_ | Yes | 3.41 |
| 14 | \ /< / <  | /< / < | No | 6.41 |
| 15 | \/<<\<__  | \/<<< \__ | No | 5.33 |
| 16 | <_/<_<(<\ | <_/<_<( <) | No | 8.24 |
| 17 | /(<(\((_  | /(<(\((_ | No | 4.75 |
| 18 | <)\)<)/_\ | <)\)<)/_\) | No | 3.88 |
| 19 | <())/ (/  | <())/ (/ | No | 3.71 |
| 20 | / <__< // | / <__< // | Yes | 4.71 |
