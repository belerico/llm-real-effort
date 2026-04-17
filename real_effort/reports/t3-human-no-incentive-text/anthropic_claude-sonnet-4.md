# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-27 10:07:29

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
| sudoku_game | 6476 | 39910 | 46386 | 2 | 18 | 26.14 | 522.84 |
| add_numbers | 3860 | 4193 | 8053 | 20 | 0 | 3.27 | 65.33 |
| counting_zeros | 4921 | 24595 | 29516 | 2 | 18 | 18.83 | 376.65 |
| task_decoding | 5180 | 6997 | 12177 | 19 | 1 | 4.58 | 91.63 |
| task_summation | 5240 | 16764 | 22004 | 20 | 0 | 8.85 | 177.04 |
| task_transcription | 4016 | 2873 | 6889 | 20 | 0 | 2.76 | 55.15 |
| task_sequences | 3921 | 8878 | 12799 | 18 | 2 | 6.16 | 123.27 |
| string_entry | 4415 | 4077 | 8492 | 9 | 11 | 3.79 | 75.83 |
| **TOTAL** | **38029** | **108287** | **146316** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 6 5 4 6 1 5 3 5 5 6 6 5 | 6 2 5 4 6 3 5 5 6 4 5 | No | 24.32 |
| 2 | 4 5 2 5 1 2 6 3 2 6 2 4 3 1 | 4 5 2 5 2 6 3 2 6 4 1 | No | 23.95 |
| 3 | 2 3 5 6 4 4 1 2 4 3 5 3 1 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell while ensuring each row, column, and 2×3 box contains numbers 1-6 exactly once.  Let me work through this systematically:  Starting with the puzzle: ``` 1 | No | 25.12 |
| 4 | 4 1 4 5 5 3 1 2 4 2 5 6 5 2 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step by analyzing rows, columns, and 2×3 boxes.  Let me work through the constraints systematically:  **Row 1:** 2 3 6 _ 1 5 → Missing: 4 So (1,4) = 4  **Row 4:** 6 _ _ 3 4 1 → Missing: 2, 5 - Column 2 already has: 3, 6, 1, 5 → Missing: 2, 4 - Since row 4 needs 2,5 and column 2 needs 2,4 → (4,2) = 2 - Column 3 already has: 6, 2, 4, 1 → Missing: 3, 5   - Since row | No | 27.17 |
| 5 | 2 2 6 3 2 4 2 1 5 1 5 4 3 1 |  | No | 26.36 |
| 6 | 4 1 6 2 4 3 6 4 5 2 6 1 2 4 |  | No | 24.07 |
| 7 | 5 6 1 5 3 1 5 6 3 5 6 1 3 6 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step:  First, let me identify the easy fills:  Row 2: 1 6 2 \| 3 4 .  Missing: 5, so (2,6) = 5  Row 6: 4 5 3 \| 2 . 1 Missing: 6, so (6,5) = 6  Column 6: 3 5 . 4 2 1 Missing: 6, so (3,6) = 6  Now working with the constraints:  Row 3: . 4 . \| . 2 6 Missing: 1, 3, 5  Column 4: . 3 . 1 4 2   Missing: 5, 6 So (1,4) and (3,4) must be 5 and 6  Looking at the middle-right box, it needs 3 and 5. Since (3,6) = 6 is already filled, (3,4) must be 5, making (1,4) = 6.  This means in the middle-right box, (4,5) = 3.  Row 4: 2 . 6 \| 1 3 4 Missing: 5, so (4,2) = 5  Row 3: . 4 . \| 5 2 6   Missing: 1, 3 Column 3: 4 2 . 6 5 3 Missing: 1, so (3,3) = 1 Therefore (3,1) = 3  Row 1: . 2 4 \| 6 . 3 Missing: 1, 5   Column 5: . 4 2 3 . 6 Missing: 1, 5 Since the top-right box needs 1 and 2, and we already have other numbers, (1,5) = 1 So (1, | No | 27.73 |
| 8 | 2 3 5 2 4 1 5 1 3 6 5 6 1 6 | Looking at this 6×6 | No | 26.44 |
| 9 | 1 4 2 1 5 6 3 6 4 2 5 4 3 5 | 1 4 2 1 5 6 3 6 4 2 5 4 3 5 | Yes | 24.44 |
| 10 | 1 5 2 2 3 4 6 5 4 3 6 4 3 5 | 1 5 2 3 4 4 3 6 5 3 6 4 5 | No | 24.99 |
| 11 | 1 5 6 1 4 2 2 5 3 6 5 6 1 2 |  | No | 28.15 |
| 12 | 5 4 6 6 5 4 1 4 1 3 1 4 2 5 |  | No | 24.58 |
| 13 | 1 4 2 3 6 1 2 6 4 3 6 4 6 3 | 1 4 2 3 6 1 2 6 4 3 6 4 6 3 | Yes | 23.84 |
| 14 | 5 3 2 1 1 4 6 4 3 1 5 4 6 6 | Looking at this 6×6 Sudoku puzzle, I'll work systematically through the constraints.  Let me start by analyzing what's missing in each region:  Row 3: 2 6 1 \| 3 5 . → Missing: 4 So position (3,6) = 4  Top-right box (rows 1-2, cols 4-6) currently has: 4, 5, 3 Missing: 1, 2, 6  Column 5 currently has: 5, 1, 3 Missing: 2, 4, 6  Row 2 is missing: 1, 4, 6 For row 2, col 5: must be in intersection of row 2 missing {1,4,6}, col 5 missing {2,4,6}, and top-right box missing {1,2,6} Intersection = {6} So (2,5) = 6  Column 5 now missing: 2, 4 Row 1 missing: 1, 2, 3, 5 For (1,5): intersection of row 1 missing and col 5 missing and top-right box missing {1,2} = {2} So (1,5 | No | 27.88 |
| 15 | 6 5 3 1 2 6 3 2 6 5 4 4 3 3 |  | No | 25.72 |
| 16 | 2 5 6 5 5 4 3 4 6 2 6 6 3 5 |  | No | 27.99 |
| 17 | 5 4 1 4 1 6 5 2 6 1 4 5 3 1 |  | No | 28.04 |
| 18 | 3 2 6 1 6 3 4 1 6 3 3 1 2 5 |  | No | 29.64 |
| 19 | 5 2 4 1 4 5 3 6 2 4 3 1 5 3 |  | No | 24.93 |
| 20 | 3 6 2 6 3 5 3 6 6 2 4 1 3 4 |  | No | 27.46 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1959 | 1959 | Yes | 4.39 |
| 2 | 2023 | 2023 | Yes | 3.8 |
| 3 | 1370 | 1370 | Yes | 1.97 |
| 4 | 2043 | 2043 | Yes | 5.08 |
| 5 | 2337 | 2337 | Yes | 2.53 |
| 6 | 1529 | 1529 | Yes | 3.15 |
| 7 | 1063 | 1063 | Yes | 2.2 |
| 8 | 1076 | 1076 | Yes | 1.89 |
| 9 | 1588 | 1588 | Yes | 3.47 |
| 10 | 1785 | 1785 | Yes | 3.24 |
| 11 | 602 | 602 | Yes | 3.42 |
| 12 | 1096 | 1096 | Yes | 2.76 |
| 13 | 1308 | 1308 | Yes | 4.17 |
| 14 | 1404 | 1404 | Yes | 3.93 |
| 15 | 1733 | 1733 | Yes | 3.48 |
| 16 | 1471 | 1471 | Yes | 4.88 |
| 17 | 1066 | 1066 | Yes | 3.31 |
| 18 | 2179 | 2179 | Yes | 2.54 |
| 19 | 1408 | 1408 | Yes | 2.54 |
| 20 | 1491 | 1491 | Yes | 2.56 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 35 | No | 11.75 |
| 2 | 62 | 60 | No | 18.57 |
| 3 | 60 | TIMEOUT | No | 120.03 |
| 4 | 74 | I'll count the zeros in each line:  Line 1: 1000101011 → 5 zeros Line 2: 0001010011 → 6 zeros   Line 3: 0001011011 → 5 zeros Line 4: 0111100000 → 6 zeros Line 5: 0000101011 → 6 zeros Line 6: 1011010101 → 4 zeros Line 7: 1111011000 → 4 zeros Line 8: 0110111010 → 4 zeros Line 9: 1111011100 → 3 zeros Line 10: 0011100100 → 6 zeros Line 11: 0111101001 → 4 zeros Line 12: 0110110100 → 5 zeros Line 13: 1100101110 → 4 zeros Line 14: 0001111001 → 5 zeros Line 15: 1010001000 → 7 zeros  Total: 5+6+5+6+6+4+4+4+3+ | No | 19.87 |
| 5 | 68 | 59 | No | 13.0 |
| 6 | 47 | 40 | No | 10.94 |
| 7 | 46 | 45 | No | 15.75 |
| 8 | 73 | 73 | Yes | 13.41 |
| 9 | 40 | 41 | No | 12.96 |
| 10 | 50 | 45 | No | 12.01 |
| 11 | 39 | 33 | No | 13.36 |
| 12 | 49 | 49 | Yes | 13.79 |
| 13 | 45 | 40 | No | 15.86 |
| 14 | 53 | 45 | No | 12.17 |
| 15 | 62 | 54 | No | 12.57 |
| 16 | 56 | 48 | No | 12.61 |
| 17 | 45 | 42 | No | 12.8 |
| 18 | 75 | 71 | No | 15.46 |
| 19 | 64 | 61 | No | 10.8 |
| 20 | 73 | 67 | No | 8.92 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KZWSBVJ | KZWSBVJ | Yes | 3.41 |
| 2 | BWVIAEO | BWVIAEO | Yes | 5.15 |
| 3 | YZSECKG | YZSECKG | Yes | 2.74 |
| 4 | JHECMZT | JHECMZT | Yes | 4.24 |
| 5 | TWUQXNP | TWUQXNP | Yes | 3.03 |
| 6 | JAPBROL | JAPBROL | Yes | 4.88 |
| 7 | YRJTLOX | YRJTLOX | Yes | 3.28 |
| 8 | IAVDNJO | IAVDNJO | Yes | 4.95 |
| 9 | NLHEKIP | NLHEKIP | Yes | 4.8 |
| 10 | JUTIOCW | JUTIOCW | Yes | 5.71 |
| 11 | JVFCTBK | JVFCTBK | Yes | 4.67 |
| 12 | YFCEIZQ | YFCEIZQ | Yes | 4.8 |
| 13 | SRHGVXD | SRHGVXD | Yes | 4.2 |
| 14 | SBGHZKV | SBGHZKV | Yes | 5.5 |
| 15 | PEKDGIX | PEKDGIX | Yes | 6.36 |
| 16 | ARIWJZY | ARIJWZY | No | 5.2 |
| 17 | RYADIWB | RYADIWB | Yes | 4.69 |
| 18 | UHYINZQ | UHYINZQ | Yes | 5.1 |
| 19 | LGAWNIO | LGAWNIO | Yes | 5.11 |
| 20 | TSDKVRZ | TSDKVRZ | Yes | 3.8 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 1.8 8.2 | Yes | 9.49 |
| 2 | [4.1, 5.9] | 5.9 4.1 | Yes | 8.73 |
| 3 | [2.7, 7.3] | 7.3 2.7 | Yes | 10.2 |
| 4 | [4.7, 5.3] | 5.3 4.7 | Yes | 8.03 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 8.71 |
| 6 | [1.8, 8.2] | 8.2 1.8 | Yes | 9.33 |
| 7 | [3.1, 6.9] | 6.9 3.1 | Yes | 8.66 |
| 8 | [1.5, 8.5] | 8.5 1.5 | Yes | 9.22 |
| 9 | [4.0, 6.0] | 6.0 4.0 | Yes | 8.64 |
| 10 | [0.9, 9.1] | 0.9 9.1 | Yes | 6.22 |
| 11 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.02 |
| 12 | [4.2, 5.8] | 4.2 5.8 | Yes | 8.94 |
| 13 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.79 |
| 14 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.11 |
| 15 | [3.1, 6.9] | 3.1 6.9 | Yes | 9.08 |
| 16 | [4.5, 5.5] | 5.5 4.5 | Yes | 8.5 |
| 17 | [0.7, 9.3] | 0.7 9.3 | Yes | 7.99 |
| 18 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.98 |
| 19 | [1.7, 8.3] | 1.7 8.3 | Yes | 8.35 |
| 20 | [2.8, 7.2] | 7.2 2.8 | Yes | 9.02 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LA3Z8GZS0GX5 | LA3Z8GZS0GX5 | Yes | 2.15 |
| 2 | FNHMYD3WBP4S | FNHMYD3WBP4S | Yes | 2.53 |
| 3 | JZA1PH4DKIFK | JZA1PH4DKIFK | Yes | 2.39 |
| 4 | BQGI9IFNGYPK | BQGI9IFNGYPK | Yes | 3.01 |
| 5 | PVPFCJ08SM7M | PVPFCJ08SM7M | Yes | 3.08 |
| 6 | HF6NP7TIJTG7 | HF6NP7TIJTG7 | Yes | 2.99 |
| 7 | KA95G4XSKC2Z | KA95G4XSKC2Z | Yes | 2.97 |
| 8 | 0058606X6C8X | 0058606X6C8X | Yes | 2.28 |
| 9 | R4GQJTKU1DRY | R4GQJTKU1DRY | Yes | 2.6 |
| 10 | DGUT457VR0AU | DGUT457VR0AU | Yes | 2.73 |
| 11 | BDF6K5HIZFZ8 | BDF6K5HIZFZ8 | Yes | 2.4 |
| 12 | F1POOI11DA75 | F1POOI11DA75 | Yes | 2.84 |
| 13 | FK6CXP37SS50 | FK6CXP37SS50 | Yes | 2.51 |
| 14 | 7PUDQQAE595M | 7PUDQQAE595M | Yes | 2.56 |
| 15 | 49IC295RY7N7 | 49IC295RY7N7 | Yes | 3.35 |
| 16 | KFET1IXKSSG2 | KFET1IXKSSG2 | Yes | 2.56 |
| 17 | YKPZDC3I0C4M | YKPZDC3I0C4M | Yes | 2.44 |
| 18 | 89VOPES18QSU | 89VOPES18QSU | Yes | 3.65 |
| 19 | RKF9JKKZZPE8 | RKF9JKKZZPE8 | Yes | 2.26 |
| 20 | 0WL9X2F5JS2P | 0WL9X2F5JS2P | Yes | 3.84 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 6.86 |
| 2 | 16 | 16 | Yes | 4.78 |
| 3 | 7680 | 7680 | Yes | 4.22 |
| 4 | 793 | 793 | Yes | 3.29 |
| 5 | 67 | 67 | Yes | 4.24 |
| 6 | 73 | 73 | Yes | 4.47 |
| 7 | 4 | 4 | Yes | 8.95 |
| 8 | 7 | 7 | Yes | 3.5 |
| 9 | 20 | 20 | Yes | 9.59 |
| 10 | 48 | 48 | Yes | 4.33 |
| 11 | 26 | 26 | Yes | 6.29 |
| 12 | 28 | 28 | Yes | 4.41 |
| 13 | 5 | 18 | No | 11.54 |
| 14 | 243 | 243 | Yes | 3.9 |
| 15 | 44 | 44 | Yes | 5.41 |
| 16 | 4096 | 262144 | No | 14.83 |
| 17 | 60 | 60 | Yes | 4.93 |
| 18 | 23 | 23 | Yes | 4.89 |
| 19 | 4 | 4 | Yes | 6.28 |
| 20 | 3 | 3 | Yes | 6.56 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \)_)_ _   | \)_)_ _ | No | 4.41 |
| 2 | _\(/_)<(< | _\(/_)<( | No | 3.51 |
| 3 | )_  /< __ | )_  /< __ | Yes | 2.83 |
| 4 | (/)/((<)_ | (/)/((<)_ | Yes | 3.4 |
| 5 | //) /)</< | //) /)</ | No | 2.72 |
| 6 | /)\/_\)/  | /)\/_\)/ | No | 3.97 |
| 7 | _\ )  _(_ | _\ )  _(_ | Yes | 5.25 |
| 8 | ((/_ <)<  | ((/_ <)< | No | 3.34 |
| 9 | \(/<\()\\ | \(/<\()\\ | Yes | 4.15 |
| 10 |  _ //<  < | _ //< | No | 3.76 |
| 11 | /)_/__< ) | /)_/__< ) | Yes | 3.26 |
| 12 | _<( )_/   | _<( )_/ | No | 4.64 |
| 13 | ()< _/ /< | ()< _/ / | No | 2.85 |
| 14 | )\)))\ <_ | )\)))\ <_ | Yes | 3.71 |
| 15 | \\/ \())  | \\/ \()) | No | 5.52 |
| 16 | ()<( _(__ | ()<( _(__ | Yes | 2.8 |
| 17 | //// (\   | //// (\ | No | 4.82 |
| 18 | \))<(\ /_ | \))<(\ /_ | Yes | 4.52 |
| 19 | \\)(<(/ \ | \\)(<(/ \ | Yes | 3.28 |
| 20 |  ))_//< < | )))_//< | No | 3.09 |
