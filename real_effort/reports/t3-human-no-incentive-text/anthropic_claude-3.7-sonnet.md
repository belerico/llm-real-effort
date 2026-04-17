# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-27 10:10:51

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
| sudoku_game | 6489 | 35544 | 42033 | 4 | 16 | 23.71 | 474.23 |
| add_numbers | 3860 | 7197 | 11057 | 20 | 0 | 6.20 | 123.96 |
| counting_zeros | 5180 | 24845 | 30025 | 1 | 19 | 14.62 | 292.37 |
| task_decoding | 5180 | 6300 | 11480 | 18 | 2 | 4.67 | 93.35 |
| task_summation | 5240 | 25506 | 30746 | 20 | 0 | 15.13 | 302.57 |
| task_transcription | 4022 | 3012 | 7034 | 20 | 0 | 3.01 | 60.26 |
| task_sequences | 3921 | 16152 | 20073 | 15 | 5 | 11.54 | 230.89 |
| string_entry | 4379 | 6277 | 10656 | 8 | 12 | 5.62 | 112.47 |
| **TOTAL** | **38271** | **124833** | **163104** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 1 2 3 2 1 6 3 2 6 1 3 4 | I'll solve this 6×6 Sudoku puzzle step by step.  First, I'll identify the empty cells (marked with dots) in the puzzle:  ``` 5 4 3 \| . 1 . . 6 4 \| . . 5 -----+----- . 3 . \| 5 4 . . 5 6 \| 4 2 1 -----+----- 4 . 5 | No | 27.48 |
| 2 | 4 2 5 1 3 4 1 4 5 4 5 1 4 2 | I need to solve this 6×6 Sudoku by filling in all the empty cells marked with dots. Let me work through this systematically.  First, I'll identify what numbers are possible for each empty cell based on the row, column, and 2×3 box constraints.  Working through row 1: It has 3, 6, 5, 1, so it needs 2 and 4 - Position (1,2): Looking at column 2, it already has 2, 1, 3, so this must be 4 - Position (1,3): Must be 2  For row 2: - Position (2,1): Must be 5 (checking constraints) - Position (2,3): Must be 1 - Position (2,4): Must be 3  Continuing methodically for all empty cells: - Position (3,1): Must be 5 - Position (3,3): Must be 1 - Position (3,4): Must be 4 - Position (4,1): Must | No | 27.73 |
| 3 | 3 5 1 1 6 4 1 2 3 4 2 1 4 3 | 3 5 1 1 6 4 1 2 4 3 2 1 3 4 | No | 22.06 |
| 4 | 5 3 6 4 5 1 4 2 6 5 1 4 3 1 | 5 6 3 4 5 5 4 1 6 2 4 1 3 1 | No | 27.46 |
| 5 | 4 1 5 2 5 4 1 6 4 5 1 1 5 2 | I'll solve this 6×6 Sudoku puzzle by methodically filling in the empty cells.  First, let me examine what numbers are already placed and identify constraints for each empty cell.  Working through the puzzle:  Row 1, Column 4: Must be 4 (only number missing from row 1) Row 2, Column 4: Must be 5 (checking box and column constraints) Row 2, Column 6: Must be 1 (only remaining possibility for this row)  Row 3, Column 3: Must be 2 (checking constraints) Row 3, Column 4: Must be 5 (only valid option) Row 3, Column 5: Must be 4 (only remaining option)  Row 4, Column 3: Must be 6 (only valid option) Row 4, Column 5: Must be 1 (checking constraints) Row 4, Column 6: Must be 4 (last number for row 4)  Row 5, Column 5: Must be 5 (only valid option) Row 5, Column 6: Must be 1 (only remaining option)  Row 6, Column 1: Must be 1 (only valid option) Row 6, Column 3: Must be 5 (checking constraints) Row 6, Column 6: Must be 2 (final remaining cell)  Reading the empty cells in order from left to right, top to bottom: - Row 1, Col 4: 4 - Row 2, Col 4: 5 - Row 2, Col 6: 1 - Row 3, Col 3: 2 - Row 3, Col 4: 5 - Row 3, Col 5: 4 - Row 4, Col 3: 6 - Row 4, Col 5: 1 - Row 4, Col 6: 4 | No | 24.05 |
| 6 | 4 6 6 2 5 6 5 4 2 3 1 3 1 6 | 4 6 6 2 5 6 5 4 2 3 1 3 1 6 | Yes | 26.63 |
| 7 | 3 2 4 5 1 6 1 2 3 6 1 5 3 1 | 3 2 4 5 1 6 1 2 3 6 1 5 3 1 | Yes | 24.99 |
| 8 | 6 1 5 3 2 6 2 2 5 3 4 2 6 4 | 6 1 5 3 2 6 2 2 5 3 4 2 6 4 | Yes | 21.35 |
| 9 | 6 5 5 6 2 5 3 4 2 5 3 4 5 6 | 5 6 5 6 2 5 3 4 2 5 3 4 5 6 | No | 24.35 |
| 10 | 5 2 6 3 3 4 1 6 3 6 1 3 5 3 | 6 2 5 3 3 4 1 6 6 1 5 3 | No | 27.08 |
| 11 | 3 5 1 5 6 5 6 1 5 3 1 2 6 3 | I'm going to solve this 6×6 Sudoku puzzle by analyzing the constraints for each empty cell.  First, let me represent the puzzle with row and column numbers:  ```     1 2 3 \| 4 5 6   ---------------  1 \| . . 6 \| 4 1 2 2 \| 4 . 2 \| . 3 .   --------------- 3 \| 6 2 1 \| 3 4 . 4 \| 2 3 4 \| . 5 .   --------------- 5 \| . 6 . \| . . 4 6 \| 1 4 5 \| 2 . . ```  Working through the puzzle:  1. Row 3, column 6 must be 5 (only missing number in row 3) 2. Row 5, column 3 must be 3 (only missing number in column 3) 3. Row 1, columns 1-2: Looking at box 1, only 3 and 5 are missing from row 1. Since 3 exists in box 3, position (1,2) must be 3, making (1,1) a 5 4. Row 2, column 2 must be 1 (box 1 has 4, 1, 2 placed, and 3 in row 1) 5. Row 2, column 4 must be 6 (checking remaining constraints) 6. Row 2, column 6 must be 5 (last empty in row 2) 7. Row 4, column 4 must be 1 (only option for this cell) 8. Row 4, column 6 must be | No | 26.68 |
| 12 | 1 3 4 1 6 4 6 3 1 6 2 1 4 1 | 1 3 4 6 1 4 6 3 1 6 2 1 4 1 | No | 21.6 |
| 13 | 2 1 6 4 2 5 5 3 2 5 3 5 6 3 | 2 6 5 2 4 3 5 2 5 3 5 6 3 | No | 15.96 |
| 14 | 6 2 1 2 5 4 6 4 2 5 6 3 4 6 | 6 2 1 2 5 4 6 4 2 5 6 3 4 6 | Yes | 23.93 |
| 15 | 1 6 4 2 5 1 2 6 2 2 6 4 5 4 | 1 6 4 5 2 1 2 6 2 2 6 4 5 4 | No | 25.35 |
| 16 | 2 3 2 4 4 5 4 3 2 1 6 5 1 3 | 2 2 3 4 5 4 4 3 2 1 6 5 1 3 | No | 20.72 |
| 17 | 2 5 6 6 3 5 3 2 4 4 6 2 3 1 | 6 2 5 6 5 6 2 3 4 4 3 2 1 6 | No | 24.55 |
| 18 | 1 5 1 6 6 2 3 3 4 2 5 3 6 4 | 1 5 6 1 3 2 6 2 3 4 5 3 5 3 6 4 | No | 22.46 |
| 19 | 3 5 2 1 3 5 4 5 1 2 6 3 4 3 | 3 5 2 1 5 3 4 5 1 2 6 3 4 3 | No | 20.09 |
| 20 | 5 3 2 6 3 1 2 5 1 1 5 4 1 5 | 5 3 6 2 1 3 5 2 1 5 1 5 4 5 1 | No | 19.68 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1646 | 1646 | Yes | 6.36 |
| 2 | 2059 | 2059 | Yes | 8.73 |
| 3 | 1492 | 1492 | Yes | 3.85 |
| 4 | 1491 | 1491 | Yes | 7.02 |
| 5 | 1098 | 1098 | Yes | 3.46 |
| 6 | 1383 | 1383 | Yes | 8.31 |
| 7 | 2011 | 2011 | Yes | 5.82 |
| 8 | 1541 | 1541 | Yes | 6.2 |
| 9 | 1972 | 1972 | Yes | 8.74 |
| 10 | 1330 | 1330 | Yes | 2.24 |
| 11 | 2262 | 2262 | Yes | 7.71 |
| 12 | 1485 | 1485 | Yes | 1.78 |
| 13 | 1383 | 1383 | Yes | 4.83 |
| 14 | 1586 | 1586 | Yes | 7.71 |
| 15 | 796 | 796 | Yes | 5.4 |
| 16 | 1843 | 1843 | Yes | 4.84 |
| 17 | 1536 | 1536 | Yes | 10.57 |
| 18 | 1100 | 1100 | Yes | 4.19 |
| 19 | 1780 | 1780 | Yes | 8.37 |
| 20 | 1872 | 1872 | Yes | 7.81 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 48 | 43 | No | 16.1 |
| 2 | 58 | 55 | No | 10.5 |
| 3 | 68 | 60 | No | 11.62 |
| 4 | 43 | 39 | No | 17.95 |
| 5 | 36 | 29 | No | 16.92 |
| 6 | 58 | 57 | No | 11.36 |
| 7 | 62 | 57 | No | 17.6 |
| 8 | 36 | 36 | Yes | 17.03 |
| 9 | 64 | 60 | No | 12.86 |
| 10 | 52 | 38 | No | 18.42 |
| 11 | 68 | 59 | No | 19.7 |
| 12 | 72 | 65 | No | 15.86 |
| 13 | 66 | 67 | No | 8.18 |
| 14 | 39 | 37 | No | 15.86 |
| 15 | 59 | 57 | No | 9.77 |
| 16 | 41 | 33 | No | 12.43 |
| 17 | 52 | 44 | No | 18.54 |
| 18 | 64 | 56 | No | 8.14 |
| 19 | 58 | 51 | No | 16.15 |
| 20 | 62 | 53 | No | 17.33 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HMZJOKW | HMZJOKW | Yes | 4.11 |
| 2 | GFCQODK | GFCQODK | Yes | 3.76 |
| 3 | YEKTRQV | YEKTRQV | Yes | 3.79 |
| 4 | XWZPULE | XWZPULE | Yes | 4.84 |
| 5 | XOGDLUJ | XOGDLUJ | Yes | 3.85 |
| 6 | FEGNOWQ | FEGNOWQ | Yes | 4.23 |
| 7 | AVPYORQ | AVPYORQ | Yes | 3.11 |
| 8 | TSUFZEK | TSUFZEK | Yes | 5.22 |
| 9 | GBFVZPI | GBFVZPI | Yes | 5.71 |
| 10 | RZDXGHP | RZDXGHP | Yes | 5.99 |
| 11 | ERXHOQW | ERXHOQW | Yes | 3.86 |
| 12 | OYKTRQW | OYKTRQW | Yes | 3.82 |
| 13 | XFOZCLE | XFOZCLE | Yes | 6.01 |
| 14 | YPWUKHM | YPWUKHM | Yes | 3.41 |
| 15 | APDUWNE | APDUWEN | No | 3.79 |
| 16 | KWMCNGF | KWMCNGF | Yes | 4.27 |
| 17 | PORLTDW | PORLDW | No | 13.64 |
| 18 | ZQSPUNV | ZQSPUNV | Yes | 3.0 |
| 19 | PLJNQZD | PLJNQZD | Yes | 3.37 |
| 20 | RSGTXJK | RSGTXJK | Yes | 3.58 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.0, 7.0] | 3.0 7.0 | Yes | 13.11 |
| 2 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.94 |
| 3 | [4.9, 5.1] | 4.9 5.1 | Yes | 15.59 |
| 4 | [1.9, 8.1] | 1.9 8.1 | Yes | 8.94 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 15.46 |
| 6 | [0.4, 9.6] | 0.4 9.6 | Yes | 16.77 |
| 7 | [2.9, 7.1] | 7.1 2.9 | Yes | 10.18 |
| 8 | [0.9, 9.1] | 9.1 0.9 | Yes | 12.98 |
| 9 | [4.5, 5.5] | 4.5 5.5 | Yes | 17.66 |
| 10 | [0.7, 9.3] | 0.7 9.3 | Yes | 20.45 |
| 11 | [4.2, 5.8] | 4.2 5.8 | Yes | 20.91 |
| 12 | [0.3, 9.7] | 0.3 9.7 | Yes | 15.51 |
| 13 | [3.8, 6.2] | 3.8 6.2 | Yes | 13.16 |
| 14 | [3.5, 6.5] | 6.5 3.5 | Yes | 10.25 |
| 15 | [0.6, 9.4] | 9.4 0.6 | Yes | 11.55 |
| 16 | [0.3, 9.7] | 9.7 0.3 | Yes | 21.4 |
| 17 | [2.6, 7.4] | 7.4 2.6 | Yes | 17.95 |
| 18 | [4.5, 5.5] | 5.5 4.5 | Yes | 17.25 |
| 19 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.1 |
| 20 | [2.4, 7.6] | 7.6 2.4 | Yes | 21.4 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LP0YNZBHIYGP | LP0YNZBHIYGP | Yes | 3.86 |
| 2 | YXRYTDH8Z7NQ | YXRYTDH8Z7NQ | Yes | 2.76 |
| 3 | 22ILTU83X56K | 22ILTU83X56K | Yes | 2.26 |
| 4 | COG6E9N9EAQ3 | COG6E9N9EAQ3 | Yes | 4.27 |
| 5 | 9GKRK7VFT6E4 | 9GKRK7VFT6E4 | Yes | 3.66 |
| 6 | KJMC9J2Y4C9G | KJMC9J2Y4C9G | Yes | 3.56 |
| 7 | XS4APZSHKUX9 | XS4APZSHKUX9 | Yes | 2.95 |
| 8 | SRCX48HNDKOB | SRCX48HNDKOB | Yes | 3.87 |
| 9 | MTL428FYB1FS | MTL428FYB1FS | Yes | 2.06 |
| 10 | 4UJFODF4ZM1Z | 4UJFODF4ZM1Z | Yes | 2.59 |
| 11 | XSZ438KM5U4M | XSZ438KM5U4M | Yes | 3.05 |
| 12 | 0BBFISNMWZ4M | 0BBFISNMWZ4M | Yes | 2.52 |
| 13 | 9MMHEDHDI7XX | 9MMHEDHDI7XX | Yes | 2.63 |
| 14 | OH2NPC1PR4BC | OH2NPC1PR4BC | Yes | 1.98 |
| 15 | N3EI0Q5YOCLV | N3EI0Q5YOCLV | Yes | 2.35 |
| 16 | 5BAZKG7LD9UF | 5BAZKG7LD9UF | Yes | 3.88 |
| 17 | YNJ8HMR26ZZC | YNJ8HMR26ZZC | Yes | 3.27 |
| 18 | T4MKS5SFDDYD | T4MKS5SFDDYD | Yes | 2.08 |
| 19 | D3PN0MG52TXJ | D3PN0MG52TXJ | Yes | 3.19 |
| 20 | R98LKYAS0ZWM | R98LKYAS0ZWM | Yes | 3.48 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 44 | No | 26.37 |
| 2 | 5 | 16 | No | 17.02 |
| 3 | 3 | 3 | Yes | 6.34 |
| 4 | 60 | 60 | Yes | 5.71 |
| 5 | 31 | 31 | Yes | 6.29 |
| 6 | 19 | 19 | Yes | 5.21 |
| 7 | 1 | 1 | Yes | 6.35 |
| 8 | 1440 | 1440 | Yes | 8.53 |
| 9 | 793 | 793 | Yes | 3.72 |
| 10 | 10 | 9 | No | 18.76 |
| 11 | 26 | 26 | Yes | 18.71 |
| 12 | 6 | 6 | Yes | 5.91 |
| 13 | 39 | 39 | Yes | 18.53 |
| 14 | 28 | 28 | Yes | 10.16 |
| 15 | 4096 | 1048576 | No | 18.31 |
| 16 | 16 | 16 | Yes | 8.72 |
| 17 | 44 | 42 | No | 22.32 |
| 18 | 4 | 4 | Yes | 11.76 |
| 19 | 5 | 5 | Yes | 5.76 |
| 20 | 48 | 48 | Yes | 6.4 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | / \)<<)<< | / \)<<)< | No | 5.44 |
| 2 | </ <<<)\/ | </ <<<)\/ | Yes | 5.67 |
| 3 | </\/(  )< | </\/( ) | No | 5.22 |
| 4 | \<\)\ <\_ | \<\) <\_ | No | 6.04 |
| 5 | ))(\<<_/\ | ))(\<<_/\ | Yes | 5.07 |
| 6 |  _(_<<(\\ | _(_<<(\\ | No | 5.39 |
| 7 | (//< (/<  | (//< (/< | No | 5.89 |
| 8 | /(( )_</( | /(( )_</( | Yes | 5.16 |
| 9 | ___)() (  | ___)() ( | No | 6.82 |
| 10 | (_\/\//)  | (_\/\//) | No | 5.73 |
| 11 | _ _(<(  \ | _ _(<(  \ | Yes | 6.32 |
| 12 | \//(\<)_\ | \//(\<)_\ | Yes | 4.35 |
| 13 |  /)\/\()\ | /)\/\()\ | No | 6.46 |
| 14 | \<\\\(_\< | \<\\\(_\ | No | 6.56 |
| 15 | </\<(/)   | </\<(/) | No | 4.34 |
| 16 | <__\)(/)_ | <__\)(/)_ | Yes | 4.67 |
| 17 | \\____\   | \\____\ | No | 5.04 |
| 18 | _((\  \(( | _((\  \(( | Yes | 6.83 |
| 19 | //)\(/\_) | //)\(/\_) | Yes | 4.25 |
| 20 | <((() /<  | <((() /< | No | 7.21 |
