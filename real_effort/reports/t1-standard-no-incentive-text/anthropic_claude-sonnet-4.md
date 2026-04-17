# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-27 10:05:42

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
| sudoku_game | 6107 | 39767 | 45874 | 0 | 20 | 25.79 | 515.77 |
| add_numbers | 3500 | 2980 | 6480 | 20 | 0 | 2.74 | 54.85 |
| counting_zeros | 4820 | 26505 | 31325 | 6 | 14 | 13.62 | 272.49 |
| task_decoding | 4820 | 7031 | 11851 | 18 | 2 | 4.61 | 92.25 |
| task_summation | 4880 | 18595 | 23475 | 20 | 0 | 9.46 | 189.16 |
| task_transcription | 3657 | 2879 | 6536 | 20 | 0 | 2.76 | 55.23 |
| task_sequences | 3561 | 10045 | 13606 | 17 | 3 | 7.05 | 140.98 |
| string_entry | 4025 | 4766 | 8791 | 11 | 9 | 4.38 | 87.59 |
| **TOTAL** | **35370** | **112568** | **147938** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 6 1 5 2 6 2 4 1 3 5 4 2 1 |  | No | 25.23 |
| 2 | 3 5 3 1 4 1 6 1 2 4 6 5 3 4 |  | No | 27.94 |
| 3 | 1 5 4 5 6 1 3 1 4 1 3 4 5 6 | 5 1 4 1 6 5 3 1 4 1 3 4 5 6 | No | 21.95 |
| 4 | 3 2 3 4 5 6 6 5 1 4 3 3 5 4 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically by checking what's allowed in each row, column, and 2×3 box.  Let me work through this step by step:  Starting with easier positions: - Position (1,1): Row 1 needs {3}, column 1 needs {3,4}, top-left box needs {2,3} → Must be 3 - Position (2,5): Row 2 needs {2,3}, column 5 needs {3,5}, top-right box needs {3} → Must be 3 - Position (2,2): Now row 2 needs {2}, so this must be 2  Continuing with row 3: - Position (3,1): Row 3 needs {4,5,6}, column 1 needs {4}, middle-left box needs {1,5,6} → Must be 4 - Position (3,2): Row 3 needs {5,6}, column 2 needs {3,5}, middle-left box needs {1,5,6} → Must be 5 - Position (3,4): Row 3 needs {6}, so this must be 6  For row 4: - Position (4,3): Column 3 needs {6}, so this | No | 22.31 |
| 5 | 4 5 3 2 2 5 3 5 1 2 4 5 3 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers systematically.  Let me work through this step by step:  Starting with easier deductions:  Row 3: 1 6 4 \| 5 2 .  Missing only the number 3, so position (3,6) = 3  Row 2: 3 . 1 \| 6 4 . Missing 2 and 5. Looking at column 6 which now has: 1, ., 3, 2, 4, . Column 6 needs 5 and 6. Since row 2 needs 2 and 5, position (2,6) = 5 Therefore (2,2) = 2  Column 6 now: 1, 5, 3, | No | 27.86 |
| 6 | 1 3 5 3 4 5 4 6 1 4 2 3 4 1 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers systematically.  Let me work through this step by step:  First, I'll identify what numbers are missing in each row, column, and 2×3 box.  Starting with easier fills: - Row 4 is missing only 4 in the last position - Row 3 is missing only 5 in position 2 - Column 1 is missing only 3 in the bottom row - Column 3 is missing only 1 in row 5  This gives me: ``` 6 2 4 \| . . . 1 . 5 \| 6 . 2 -----+----- 4 5 3 \| 2 6 1 2 1 6 \| 3 5 4 -----+----- 5 | No | 24.59 |
| 7 | 3 2 3 4 4 3 2 3 4 5 3 1 4 2 | 3 3 2 4 4 3 2 3 4 5 4 1 3 2 | No | 28.4 |
| 8 | 1 6 1 6 3 4 4 6 4 3 4 2 6 1 |  | No | 27.62 |
| 9 | 4 6 2 4 1 3 4 5 2 1 4 4 3 6 |  | No | 25.61 |
| 10 | 5 1 5 4 6 2 2 4 3 2 4 3 1 2 | 5 1 5 4 6 2 2 4 3 2 4 3 1 5 2 | No | 23.02 |
| 11 | 3 5 3 6 2 4 4 2 4 5 1 3 6 5 | 3 5 3 6 2 4 6 | No | 27.05 |
| 12 | 3 2 6 3 4 6 2 5 2 4 3 6 5 1 | 3 2 6 3 4 6 2 5 2 3 6 5 1 | No | 32.08 |
| 13 | 1 6 2 2 3 4 4 5 3 2 1 4 3 6 |  | No | 25.91 |
| 14 | 1 4 1 5 4 3 1 1 3 6 6 2 6 4 | 1 4 1 4 3 5 1 1 3 6 6 2 4 | No | 23.65 |
| 15 | 1 5 3 1 2 4 1 3 1 2 5 3 1 3 |  | No | 20.66 |
| 16 | 1 5 6 2 6 2 4 5 2 1 5 3 2 1 |  | No | 26.55 |
| 17 | 3 2 4 5 1 5 2 4 2 4 1 5 2 3 |  | No | 26.64 |
| 18 | 4 6 1 1 4 6 4 1 3 6 2 5 2 2 | Looking at this 6×6 Sudoku, I'll solve it step by step.  Let me start by analyzing the constraints and filling in the obvious numbers:  Row 6: . 6 1 \| 3 5 4 This row is missing only 2, and column 1 needs it, so (6,1) = 2  Row 6: 2 6 1 \| 3 5 4  Now column 1 has: 3, 6, 5, 1, 2 - missing only 4 So (1,1) = 4  Row 1: 4 5 3 \| . . 2  Looking at the top-left 2×3 box: 4 5 3 3 . 2 Missing: 1, 6, so (2,2) = 1 or 6 Column 2 has: 5, 2, 3, 4, 6 - missing only 1 So (2,2) = 1  Row 2: 3 1 2 \| 5 . .  Row 2 needs 4 and 6 in positions 5 and 6 Looking at constraints: - Column 5 has: 6, 5 - allows 1,2,3,4 - Column 6 has: 2, 4 - allows 1,3,5,6  So (2,5) = 4 and (2,6) = 6  Row 2: 3 1 2 \| 5 4 6  For Row 1, positions 4 and 5 need the remaining numbers 1 and 6 Top-right 2×3 box currently has: ? ? 2, 5 4 6 Missing from this box: 1, 3 But Row 1 needs 1 and 6, so (1,5) = 1 and we need to find where 6 goes...  Actually, let me recalculate: Row 1 is missing 1 and 6, and the top-right box needs 1 and 3. This means (1,5) = 1 and (1,4) must work with the box constraint. | No | 28.51 |
| 19 | 6 4 1 2 3 1 5 2 2 6 4 1 2 6 |  | No | 27.35 |
| 20 | 4 2 3 4 2 1 6 2 5 4 5 3 4 3 | 2 4 4 3 3 1 2 2 5 4 5 3 4 3 | No | 22.78 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1851 | 1851 | Yes | 2.28 |
| 2 | 2143 | 2143 | Yes | 2.67 |
| 3 | 1604 | 1604 | Yes | 3.16 |
| 4 | 1143 | 1143 | Yes | 5.09 |
| 5 | 640 | 640 | Yes | 2.46 |
| 6 | 1634 | 1634 | Yes | 2.55 |
| 7 | 768 | 768 | Yes | 2.75 |
| 8 | 1230 | 1230 | Yes | 2.34 |
| 9 | 1295 | 1295 | Yes | 3.57 |
| 10 | 1755 | 1755 | Yes | 3.91 |
| 11 | 2106 | 2106 | Yes | 2.79 |
| 12 | 1134 | 1134 | Yes | 2.32 |
| 13 | 708 | 708 | Yes | 2.83 |
| 14 | 1435 | 1435 | Yes | 2.61 |
| 15 | 722 | 722 | Yes | 2.06 |
| 16 | 1305 | 1305 | Yes | 1.93 |
| 17 | 1664 | 1664 | Yes | 1.86 |
| 18 | 1307 | 1307 | Yes | 2.18 |
| 19 | 1229 | 1229 | Yes | 2.18 |
| 20 | 1943 | 1943 | Yes | 3.31 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 70 | 67 | No | 9.89 |
| 2 | 51 | 50 | No | 12.8 |
| 3 | 74 | 65 | No | 17.42 |
| 4 | 36 | 33 | No | 12.64 |
| 5 | 46 | 46 | Yes | 16.56 |
| 6 | 65 | 64 | No | 16.04 |
| 7 | 48 | 47 | No | 12.68 |
| 8 | 52 | 47 | No | 8.98 |
| 9 | 75 | 75 | Yes | 17.6 |
| 10 | 67 | 64 | No | 12.91 |
| 11 | 53 | 53 | Yes | 12.84 |
| 12 | 48 | 48 | Yes | 12.53 |
| 13 | 53 | 43 | No | 7.8 |
| 14 | 61 | 61 | Yes | 16.15 |
| 15 | 75 | 75 | Yes | 19.0 |
| 16 | 50 | 53 | No | 13.22 |
| 17 | 45 | 42 | No | 14.22 |
| 18 | 53 | 52 | No | 12.5 |
| 19 | 65 | 58 | No | 17.55 |
| 20 | 35 | 37 | No | 9.15 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PQZVYFX | PQZVYFX | Yes | 4.45 |
| 2 | NSOQDUT | NSOQUDT | No | 4.63 |
| 3 | QPEVLOW | QPEVLOW | Yes | 3.77 |
| 4 | CQAHUFL | CQAHUFL | Yes | 4.55 |
| 5 | GIQBMZD | GIQBMZD | Yes | 3.5 |
| 6 | PETISBW | PETISBW | Yes | 6.35 |
| 7 | QBMKTPZ | QBMKTPZ | Yes | 3.76 |
| 8 | GVWSTDP | GWSTDP | No | 3.54 |
| 9 | JDYKQCN | JDYKQCN | Yes | 4.22 |
| 10 | MSPATYH | MSPATYH | Yes | 9.11 |
| 11 | QZOFVKW | QZOFVKW | Yes | 4.02 |
| 12 | MKIYXTA | MKIYXTA | Yes | 4.72 |
| 13 | FCYEVOS | FCYEVOS | Yes | 3.27 |
| 14 | IVOCFAP | IVOCFAP | Yes | 3.81 |
| 15 | CQAVMIR | CQAVMIR | Yes | 5.65 |
| 16 | RMCOAZJ | RMCOAZJ | Yes | 5.22 |
| 17 | ZLMWDQH | ZLMWDQH | Yes | 3.6 |
| 18 | GKJNUIA | GKJNUIA | Yes | 5.57 |
| 19 | WJSVYBZ | WJSVYBZ | Yes | 4.45 |
| 20 | ZFTBUYI | ZFTBUYI | Yes | 4.05 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.9, 7.1] | 2.9 7.1 | Yes | 10.52 |
| 2 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.09 |
| 3 | [1.9, 8.1] | 8.1 1.9 | Yes | 9.94 |
| 4 | [2.9, 7.1] | 7.1 2.9 | Yes | 8.74 |
| 5 | [0.8, 9.2] | 0.8 9.2 | Yes | 8.86 |
| 6 | [0.3, 9.7] | 9.7 0.3 | Yes | 10.12 |
| 7 | [4.9, 5.1] | 5.1 4.9 | Yes | 9.15 |
| 8 | [4.2, 5.8] | 5.8 4.2 | Yes | 8.97 |
| 9 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.81 |
| 10 | [2.0, 8.0] | 8.0 2.0 | Yes | 11.9 |
| 11 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.21 |
| 12 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.6 |
| 13 | [4.3, 5.7] | 5.7 4.3 | Yes | 10.72 |
| 14 | [2.6, 7.4] | 7.4 2.6 | Yes | 8.47 |
| 15 | [0.2, 9.8] | 0.2 9.8 | Yes | 8.55 |
| 16 | [4.8, 5.2] | 4.8 5.2 | Yes | 10.58 |
| 17 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.58 |
| 18 | [4.6, 5.4] | 4.6 5.4 | Yes | 9.35 |
| 19 | [2.2, 7.8] | 2.2 7.8 | Yes | 8.91 |
| 20 | [2.2, 7.8] | 2.2 7.8 | Yes | 9.08 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | Q2ZOR55A19RW | Q2ZOR55A19RW | Yes | 3.64 |
| 2 | CLTN36PPUS4M | CLTN36PPUS4M | Yes | 2.62 |
| 3 | URJ0BHSS8FSB | URJ0BHSS8FSB | Yes | 3.38 |
| 4 | 9AHKZUOSN912 | 9AHKZUOSN912 | Yes | 2.11 |
| 5 | BXGLCLHEOZA9 | BXGLCLHEOZA9 | Yes | 2.33 |
| 6 | LWZ10TKQAHQG | LWZ10TKQAHQG | Yes | 2.08 |
| 7 | PLJQR21MPZV1 | PLJQR21MPZV1 | Yes | 1.78 |
| 8 | N51HJS9CJUGO | N51HJS9CJUGO | Yes | 2.25 |
| 9 | 3EM49BOPCWBM | 3EM49BOPCWBM | Yes | 3.4 |
| 10 | 2GYASBF8HLTQ | 2GYASBF8HLTQ | Yes | 3.52 |
| 11 | 4BIU13BPWLI4 | 4BIU13BPWLI4 | Yes | 2.64 |
| 12 | FB2NDD9MWE6R | FB2NDD9MWE6R | Yes | 3.4 |
| 13 | 4R4PRSRRTAZG | 4R4PRSRRTAZG | Yes | 2.99 |
| 14 | XQ5T87BXSOLT | XQ5T87BXSOLT | Yes | 2.74 |
| 15 | 7N4CCTEAGB0D | 7N4CCTEAGB0D | Yes | 2.67 |
| 16 | BAYGJQ7JF2GV | BAYGJQ7JF2GV | Yes | 2.84 |
| 17 | N87HZ7QIQ9FT | N87HZ7QIQ9FT | Yes | 2.6 |
| 18 | IOQ06YMVWYRD | IOQ06YMVWYRD | Yes | 2.66 |
| 19 | S18WF9FS7P1V | S18WF9FS7P1V | Yes | 2.79 |
| 20 | LY8DCWIXDQUO | LY8DCWIXDQUO | Yes | 2.81 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 3.93 |
| 2 | 36 | 36 | Yes | 3.59 |
| 3 | 10 | 10 | Yes | 9.52 |
| 4 | 7680 | 7680 | Yes | 5.15 |
| 5 | 26 | 26 | Yes | 7.77 |
| 6 | 44 | 44 | Yes | 8.03 |
| 7 | 4096 | 65536 | No | 25.83 |
| 8 | 20 | 21 | No | 13.77 |
| 9 | 19 | 19 | Yes | 4.05 |
| 10 | 16 | 16 | Yes | 4.48 |
| 11 | 73 | 73 | Yes | 4.41 |
| 12 | 48 | 48 | Yes | 3.44 |
| 13 | 31 | 31 | Yes | 3.69 |
| 14 | 5 | 5 | Yes | 5.41 |
| 15 | 23 | 23 | Yes | 4.29 |
| 16 | 5 | 14 | No | 8.65 |
| 17 | 243 | 243 | Yes | 3.24 |
| 18 | 7 | 7 | Yes | 4.25 |
| 19 | 60 | 60 | Yes | 5.61 |
| 20 | 3 | 3 | Yes | 11.86 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ((/\_<)(  | ((/\_<)( | No | 3.94 |
| 2 | //<)\/<(( | //<)\/<(( | Yes | 4.59 |
| 3 | )_\_/_((/ | )_\_/_((/ | Yes | 4.91 |
| 4 | )\))<)))< | )\))<))) | No | 3.58 |
| 5 | _(  \)<)) | _(  \)<)) | Yes | 3.23 |
| 6 | /)/\ _<<  | /)/\ _< | No | 4.01 |
| 7 |  /___  (( | /___  (( | No | 3.36 |
| 8 | <__ /(<__ | <__ /(<__ | Yes | 2.71 |
| 9 | ))((( ))\ | ))((( ))\ | Yes | 6.74 |
| 10 | )_ /</_(_ | )_ /</_(_ | Yes | 3.85 |
| 11 |  \ ( </<< | \ ( </< | No | 4.74 |
| 12 | )(</<<\<\ | )(</<<\<\ | Yes | 4.63 |
| 13 | ((<(\))/) | ((<(\))/) | Yes | 4.05 |
| 14 | <_\ /(\)/ | <_\ /(\)/ | Yes | 5.27 |
| 15 | (<)<\\< < | (<)<\\< | No | 3.49 |
| 16 | <((//<\)) | <((//<\)) | Yes | 5.85 |
| 17 |  (</)_/\) | (</)_/\) | No | 3.32 |
| 18 |    _ (</  | _ (</ | No | 6.47 |
| 19 | \\<_))_)( | \\<_))_)( | Yes | 3.52 |
| 20 |  << (<__  | << (<__ | No | 5.34 |
