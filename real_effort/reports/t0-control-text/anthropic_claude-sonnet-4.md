# Benchmark Report — claude-sonnet-4

- **Model**: `anthropic/claude-sonnet-4`
- **Date**: 2026-03-26 15:44:45

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
| sudoku_game | 5507 | 37457 | 42964 | 2 | 18 | 30.77 | 615.36 |
| add_numbers | 3180 | 3208 | 6388 | 20 | 0 | 3.13 | 62.67 |
| counting_zeros | 4500 | 27678 | 32178 | 1 | 19 | 14.74 | 294.9 |
| task_decoding | 4500 | 7980 | 12480 | 17 | 3 | 5.19 | 103.88 |
| task_summation | 4560 | 17638 | 22198 | 20 | 0 | 9.08 | 181.57 |
| task_transcription | 3338 | 2846 | 6184 | 20 | 0 | 2.80 | 56.05 |
| task_sequences | 3240 | 7705 | 10945 | 18 | 2 | 5.28 | 105.53 |
| string_entry | 3720 | 4051 | 7771 | 15 | 5 | 4.05 | 81.0 |
| **TOTAL** | **32545** | **108563** | **141108** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 6 4 4 3 6 4 5 5 1 2 2 6 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step by analyzing each empty cell using row, column, and 2×3 box constraints.  Starting with the given puzzle: ``` 6 2 . \| . 3 4 3 1 . \| . 2 5 -----+----- . 5 2 \| . 1 . 1 . . \| 2 6 3 -----+----- . 6 3 \| . 4 . . 3 4 \| . 5 1 ```  Let me work through each empty cell systematically:  Row 1, Col 3: Row 1 needs {1,5}, Col 3 needs {1,4,5,6}, Box 1 (top-left) needs {4,5} Intersection: {5} → **5**  Row 1, Col 4: Row 1 now needs {1}, so → **1**  Row 2, Col 3: Box 1 now needs {4}, so → **4**  Row 2, Col 4: Row 2 needs {6}, so → **6**  Row 3, Col 1: Row 3 needs {3,4,6}, Col 1 needs {2,4,5}, Box 3 needs {3,4,6} Intersection: {4} → **4**  Row 3, Col 4: Row 3 needs {3,6}, Col 4 needs {3,4,5}, Box 4 needs {4,5} Intersection: {} - Let me recalculate...  Actually, Row 3 needs {3,6}, Col 4 needs {3,4,5}, Box 4 needs {4,5} The intersection is empty, so I need to check other cells first.  Row 3, Col 6: Row 3 needs {3,6}, Col 6 needs {2, | No | 27.09 |
| 2 | 6 1 3 6 5 1 5 4 3 1 6 2 3 4 |  | No | 27.92 |
| 3 | 2 4 6 3 1 1 3 1 4 3 5 3 2 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the constraints:  Starting with the easiest deductions: - Column 5 has 1,2,4,5,6, missing only 3 → (5,5) = 3 - Column 6 has 2 | No | 28.46 |
| 4 | 6 3 1 2 1 2 5 6 3 6 3 4 2 6 | 6 3 1 2 1 2 5 6 3 4 2 6 | No | 18.92 |
| 5 | 5 2 1 3 2 1 5 5 3 4 3 6 3 2 |  | No | 27.91 |
| 6 | 1 5 4 6 6 1 5 4 2 5 2 4 6 5 | TIMEOUT | No | 120.03 |
| 7 | 3 1 6 4 6 6 2 5 4 3 1 2 5 1 | 3 1 6 4 6 6 2 4 5 3 1 2 5 1 | No | 25.28 |
| 8 | 3 1 6 2 4 1 6 3 1 6 6 4 2 3 | Looking at this 6×6 Sudoku puzzle, I need to fill in the missing numbers while ensuring each row, column, and 2× | No | 29.52 |
| 9 | 6 1 1 6 1 2 5 4 6 6 4 5 2 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it step by step by analyzing rows, columns, and 2×3 boxes.  Let me work through the constraints systematically:  Starting with easier deductions: - Row 2, Column 6: Only missing 6 in that position - Row 2, Column 3: After placing 6, only 1 remains for this position  Working through the remaining cells: - Row 1: Missing 1 and 6. Column 5 | No | 24.05 |
| 10 | 2 1 4 2 1 6 4 2 5 2 3 1 5 5 |  | No | 25.16 |
| 11 | 4 5 4 2 1 5 3 2 2 5 1 6 2 1 | Looking at this 6×6 Sudoku puzzle, I'll solve systematically by analyzing the constraints for each empty cell.  Current puzzle: ``` 3 1 6 \| . 2 . 5 6 3 \| 2 4 1 -----+----- . . . \| . 6 3 1 4 5 \| 6 . . -----+----- . . 4 \| 3 . . 6 3 . \| . 5 4 ```  Let me solve step by step:  Row 1, Col 4: Row 1 needs 4,5. Column 4 needs 1,4,5. Box constraint gives us → **5** Row 1, Col 6: Row 1 needs 4 (remaining) → **4**  Row 3, Col 1: Column 1 needs 2,4. Row 3 constraints → **2** Row 3, Col 2: Column 2 needs 2,5. Since col 1 has 2, this must be → **5**   Row 3, Col 3: Row 3 needs 1,4. Column 3 needs 1,2. Must be → **1** Row 3, Col 4: Row 3 needs 4 (remaining) → **4**  Row 4, Col 5: Column 5 needs 1,3. Row 4 needs 2,3 → **3** Row 4, Col 6: Row 4 needs 2 (remaining) → **2**  Row 5, Col 1: Column 1 needs 4 (remaining) → **4** Row 5, Col 2: Column 2 needs 2 (remaining) → **2** Row 5, Col 5: Column 5 needs 1 (remaining) → **1** Row 5, Col 6: Row 5 needs 6 (remaining) → **6**  Row 6, Col 3: Column 3 needs 2 (remaining) → **2** Row 6, Col 4: Column 4 needs 1 (remaining) → **1**  Reading the missing numbers in order (left to right, top to bottom):  Answer: | No | 27.15 |
| 12 | 6 1 2 4 3 3 1 4 2 3 5 6 2 1 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing the constraints for each empty cell.  Let me work through the grid:  ``` 5 3 . \| 4 . . 1 . 2 \| 5 6 . -----+----- 2 6 1 \| 3 5 4 . . 5 \| 2 . 6 -----+----- 6 . 4 \| 1 . 5 4 . 3 \| . . . ```  Starting with easier cells:  Row 1, Col 3: Column 3 already has {2,1,5,4,3}, missing only 6. Row 4, Col 1: Column 1 has {5,1,2,6,4}, missing only 3. Row 4, Col 5: Middle-right box has {3,5,4,2,6}, missing only 1. Row 4, Col 2: Row 4 now has {3,5,2,1,6}, missing only 4.  Row 2, Col 2: Top-left box has {5,3,1,2}, missing {4,6}. Row 2 has {1,2,5,6}, missing {3,4}. Intersection is 4.  Row 6, Col 2: Column 2 now has {3,4,6}, missing {1,2,5}. Row 6 has {4,3}, missing {1,2,5,6}. Bottom-left box has {6,4,4,3}, but need to check constraints more carefully.  Let me continue systematically:  Row 6, Col 2: Bottom-left box needs {1,2,5}. Column 2 needs {1,2,5}. Row 6 needs {1,2,5,6}. This must be 2.  Row 6, Col 5: Row 6 has {4,2,3}, missing {1,5,6}. | No | 25.6 |
| 13 | 4 1 1 5 6 4 1 1 6 2 1 5 3 2 | 4 1 1 5 6 4 1 1 6 2 1 5 3 2 | Yes | 21.19 |
| 14 | 5 6 4 1 2 3 6 1 5 2 3 1 2 5 | 5 6 4 1 2 3 6 1 3 2 2 5 | No | 28.22 |
| 15 | 3 4 1 4 2 1 5 3 6 5 2 1 1 2 | 3 4 1 4 2 1 5 3 6 5 2 1 1 2 | Yes | 21.55 |
| 16 | 3 1 1 6 2 1 5 3 4 3 2 1 4 6 |  | No | 27.07 |
| 17 | 2 6 1 6 2 6 5 3 1 5 2 2 1 6 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each empty cell.  Let me work through this systematically, using the constraints that each row, column, and 2×3 box must contain 1-6 exactly once.  Starting with easier positions:  Row 6: 5 3 4 _ _ _ Missing in row 6: 1, 2, 6 Column 4 has: 4, 3, _, 6, 1, _ Missing in column 4: 2, 5 Since row 6 already has 5, position (6,4) = 2  Row 6: 5 3 4 2 _ _ Remaining for row 6: 1, 6  Column 5 missing: 1, 3, 6 (has _, 5, _, 2, 4, _) Column 6 missing: 2, 6 (has 1, _, 4, 3, 5, _)  Since row 6 needs 1,6 and column 6 needs 2,6: position (6,6) = 6 Therefore position (6,5) = 1  Now working on other positions: Row 5: _ 6 3 1 4 5 Missing: 2 Position (5,1) = 2  Row 4: _ 4 _ 6 2 3 Missing: 1, 5 Column 1 missing at this point: 1, 6 Since row 4 needs 1,5 and column 1 needs 1,6: position (4,1) = 1 Therefore position (4,3) = 5  Row 3: _ 2 1 _ _ 4 Missing: 3, 5, 6 Column 4 missing: | No | 29.29 |
| 18 | 5 3 1 4 1 2 5 3 1 1 4 3 3 4 |  | No | 27.08 |
| 19 | 3 5 2 4 6 2 6 1 3 1 6 2 5 3 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers for each empty cell.  Let me work through this systematically by analyzing rows, columns, and 2×3 boxes:  Starting with Row 1: . . 6 \| 4 1 . - Missing numbers: 2, 3, 5 - Position (1,1): Checking column 1 constraints and top-left box → 3 - Position (1,2): Checking column 2 constraints and top-left box → 5   - Position (1,6): Checking column 6 constraints and top-right box → 2  Row 2 | No | 28.33 |
| 20 | 1 4 4 6 3 2 4 5 3 2 5 1 6 3 |  | No | 25.53 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2202 | 2202 | Yes | 3.14 |
| 2 | 2167 | 2167 | Yes | 2.99 |
| 3 | 2087 | 2087 | Yes | 2.56 |
| 4 | 2162 | 2162 | Yes | 1.96 |
| 5 | 2521 | 2521 | Yes | 3.61 |
| 6 | 1555 | 1555 | Yes | 2.59 |
| 7 | 1429 | 1429 | Yes | 3.13 |
| 8 | 736 | 736 | Yes | 4.52 |
| 9 | 1919 | 1919 | Yes | 3.02 |
| 10 | 1149 | 1149 | Yes | 2.64 |
| 11 | 1956 | 1956 | Yes | 3.73 |
| 12 | 1904 | 1904 | Yes | 4.31 |
| 13 | 1251 | 1251 | Yes | 2.18 |
| 14 | 1289 | 1289 | Yes | 2.93 |
| 15 | 1623 | 1623 | Yes | 3.06 |
| 16 | 1741 | 1741 | Yes | 1.83 |
| 17 | 2011 | 2011 | Yes | 5.2 |
| 18 | 1667 | 1667 | Yes | 3.5 |
| 19 | 1600 | 1600 | Yes | 3.31 |
| 20 | 1523 | 1523 | Yes | 2.45 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 | 54 | No | 11.96 |
| 2 | 49 | 50 | No | 15.59 |
| 3 | 57 | 49 | No | 17.66 |
| 4 | 63 | 60 | No | 13.62 |
| 5 | 55 | 44 | No | 14.71 |
| 6 | 71 | 63 | No | 10.35 |
| 7 | 46 | 45 | No | 21.19 |
| 8 | 60 | 58 | No | 14.71 |
| 9 | 63 | 45 | No | 12.42 |
| 10 | 65 | 61 | No | 15.07 |
| 11 | 72 | 69 | No | 14.08 |
| 12 | 64 | 64 | Yes | 17.04 |
| 13 | 47 | 46 | No | 13.38 |
| 14 | 39 | 31 | No | 14.96 |
| 15 | 75 | 68 | No | 14.39 |
| 16 | 52 | 50 | No | 13.71 |
| 17 | 62 | 54 | No | 16.01 |
| 18 | 64 | 54 | No | 13.02 |
| 19 | 57 | 55 | No | 15.17 |
| 20 | 59 | 48 | No | 15.82 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TYASMBN | TYASMBN | Yes | 4.82 |
| 2 | XHARYDW | XHARYOW | No | 5.83 |
| 3 | QSRECGL | QSRECGL | Yes | 4.42 |
| 4 | OUGVMNP | OUGVMNP | Yes | 7.2 |
| 5 | QCWFHRZ | QCWFHRZ | Yes | 3.86 |
| 6 | RIJNKXZ | RIJKXZ | No | 5.4 |
| 7 | UJADKHO | UJADKHO | Yes | 5.09 |
| 8 | BDPLNRS | BDPLNRS | Yes | 4.59 |
| 9 | DSKMPJC | DSKMPJC | Yes | 9.52 |
| 10 | INWABUT | INWABUT | Yes | 4.9 |
| 11 | ZSMPDTH | ZSMPDTH | Yes | 5.11 |
| 12 | FCENJAG | FCENJAG | Yes | 4.79 |
| 13 | HMICTAD | HMICTAD | Yes | 4.29 |
| 14 | JLKVDES | JLKVDES | Yes | 5.37 |
| 15 | GPUKIES | GPUKIES | Yes | 3.86 |
| 16 | PREQXCO | PREQXCO | Yes | 4.25 |
| 17 | VDONGJE | VDONGJЕ | No | 5.27 |
| 18 | AXKCTJE | AXKCTJE | Yes | 5.18 |
| 19 | RPJNSTM | RPJNSTM | Yes | 4.2 |
| 20 | GWIZJFS | GWIZJFS | Yes | 5.92 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.33 |
| 2 | [3.1, 6.9] | 6.9 3.1 | Yes | 9.31 |
| 3 | [2.5, 7.5] | 7.5 2.5 | Yes | 9.62 |
| 4 | [2.8, 7.2] | 7.2 2.8 | Yes | 8.41 |
| 5 | [3.4, 6.6] | 6.6 3.4 | Yes | 7.97 |
| 6 | [2.3, 7.7] | 2.3 7.7 | Yes | 9.81 |
| 7 | [0.7, 9.3] | 9.3 0.7 | Yes | 7.71 |
| 8 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.0 |
| 9 | [3.2, 6.8] | 3.2 6.8 | Yes | 8.08 |
| 10 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.29 |
| 11 | [3.7, 6.3] | 6.3 3.7 | Yes | 9.11 |
| 12 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.94 |
| 13 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.96 |
| 14 | [1.8, 8.2] | 8.2 1.8 | Yes | 8.43 |
| 15 | [3.3, 6.7] | 6.7 3.3 | Yes | 8.62 |
| 16 | [2.3, 7.7] | 2.3 7.7 | Yes | 13.09 |
| 17 | [4.2, 5.8] | 5.8 4.2 | Yes | 11.33 |
| 18 | [4.8, 5.2] | 4.8 5.2 | Yes | 7.22 |
| 19 | [2.3, 7.7] | 7.7 2.3 | Yes | 8.04 |
| 20 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.3 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FJ5HF9KFU5X3 | FJ5HF9KFU5X3 | Yes | 3.42 |
| 2 | SFWUEICDNKLC | SFWUEICDNKLC | Yes | 2.81 |
| 3 | RUNTS3W4OZHT | RUNTS3W4OZHT | Yes | 3.15 |
| 4 | U6V19AMRTOMZ | U6V19AMRTOMZ | Yes | 3.15 |
| 5 | BQ3L3KOIOPGY | BQ3L3KOIOPGY | Yes | 2.15 |
| 6 | XOSA0YW743F8 | XOSA0YW743F8 | Yes | 3.17 |
| 7 | 7FLTE6BPP80F | 7FLTE6BPP80F | Yes | 3.05 |
| 8 | AGPM9ZSAL0TF | AGPM9ZSAL0TF | Yes | 3.01 |
| 9 | 8J7AWMPPU8YY | 8J7AWMPPU8YY | Yes | 3.21 |
| 10 | QPYDOXKF8U2T | QPYDOXKF8U2T | Yes | 2.48 |
| 11 | VSQ2CYA1NRGV | VSQ2CYA1NRGV | Yes | 2.53 |
| 12 | 448MORNX3YR5 | 448MORNX3YR5 | Yes | 2.78 |
| 13 | Y5FLNULJLPKR | Y5FLNULJLPKR | Yes | 3.55 |
| 14 | GT7Q6SDPZ8ZQ | GT7Q6SDPZ8ZQ | Yes | 2.06 |
| 15 | P489C7J81AWZ | P489C7J81AWZ | Yes | 2.67 |
| 16 | WDYSQE183XV0 | WDYSQE183XV0 | Yes | 2.26 |
| 17 | 3DGETTAE6DQF | 3DGETTAE6DQF | Yes | 2.15 |
| 18 | GXEYF8VLM6U7 | GXEYF8VLM6U7 | Yes | 2.35 |
| 19 | A17T9IHDF1GX | A17T9IHDF1GX | Yes | 2.64 |
| 20 | BHDGMALLM4KU | BHDGMALLM4KU | Yes | 3.47 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 2 | No | 12.63 |
| 2 | 1440 | 1440 | Yes | 4.75 |
| 3 | 36 | 36 | Yes | 3.18 |
| 4 | 793 | 793 | Yes | 3.66 |
| 5 | 60 | 60 | Yes | 3.15 |
| 6 | 4 | 4 | Yes | 4.17 |
| 7 | 6 | 6 | Yes | 5.16 |
| 8 | 243 | 243 | Yes | 4.29 |
| 9 | 4 | 4 | Yes | 5.44 |
| 10 | 23 | 23 | Yes | 4.7 |
| 11 | 3 | 3 | Yes | 8.46 |
| 12 | 16 | 16 | Yes | 4.5 |
| 13 | 65 | 65 | Yes | 3.79 |
| 14 | 60 | 60 | Yes | 5.34 |
| 15 | 28 | 28 | Yes | 5.58 |
| 16 | 39 | 39 | Yes | 4.1 |
| 17 | 198 | 198 | Yes | 5.02 |
| 18 | 1 | 1 | Yes | 4.96 |
| 19 | 19 | 19 | Yes | 3.27 |
| 20 | 10 | 9 | No | 9.37 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /_<_\_ /\ | /_<_\_ /\ | Yes | 4.23 |
| 2 | < /<_(_)_ | < /<_(_)_ | Yes | 2.97 |
| 3 | _\)__\/\_ | _\)__\/\_ | Yes | 2.96 |
| 4 | \ (((<)\  | \ (((<)\ | No | 6.36 |
| 5 | _<)<<<)(_ | _<)<<<)(_ | Yes | 3.08 |
| 6 | \()_(_ /_ | \()_(_ /_ | Yes | 3.72 |
| 7 | _ _/ \< ) | _ _/ \< ) | Yes | 4.39 |
| 8 | \<)\<(\<_ | \<)\<(\<_ | Yes | 2.37 |
| 9 | )(</_<  _ | )(</_<  _ | Yes | 5.48 |
| 10 | \ /(<\/   | \ /(<\/ | No | 5.1 |
| 11 | /) )<)))\ | /) )<)))\ | Yes | 3.93 |
| 12 | _\\)\<</\ | _\\)\<</\ | Yes | 2.45 |
| 13 | ( \< (/   | ( \< (/ | No | 6.8 |
| 14 | )__(\)_<_ | )__(\)_<_ | Yes | 4.43 |
| 15 | <_/ _\)_/ | <_/ _\)_/ | Yes | 3.6 |
| 16 | (\ _/ (_\ | (\ _/ (_\ | Yes | 3.53 |
| 17 | <\( <( <  | <\( <( < | No | 5.07 |
| 18 | \\ _/_/_\ | \\ _/_/_\ | Yes | 3.64 |
| 19 | )\\)(_\(_ | )\\)(_\(_ | Yes | 3.5 |
| 20 | <)\/(\\_< | <)\/(\\_ | No | 3.35 |
