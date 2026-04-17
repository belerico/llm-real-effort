# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-27 10:00:17

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
| sudoku_game | 5546 | 35056 | 40602 | 5 | 15 | 7.79 | 155.86 |
| add_numbers | 3404 | 4850 | 8254 | 20 | 0 | 2.47 | 49.38 |
| counting_zeros | 6466 | 36143 | 42609 | 11 | 9 | 8.73 | 174.65 |
| task_decoding | 4451 | 15678 | 20129 | 16 | 4 | 12.42 | 248.48 |
| task_summation | 4726 | 15131 | 19857 | 20 | 0 | 7.09 | 141.88 |
| task_transcription | 3391 | 5313 | 8704 | 20 | 0 | 4.75 | 94.99 |
| task_sequences | 3365 | 7300 | 10665 | 20 | 0 | 3.36 | 67.24 |
| string_entry | 3681 | 17117 | 20798 | 9 | 11 | 5.58 | 111.67 |
| **TOTAL** | **35030** | **136588** | **171618** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 2 1 6 1 2 5 1 4 6 3 6 3 | 2 6 2 1 6 1 2 5 6 4 3 1 6 3 | No | 8.32 |
| 2 | 2 3 1 2 4 6 5 3 4 6 4 3 5 4 | 2 3 4 2 1 6 5 3 4 6 4 | No | 7.15 |
| 3 | 2 5 6 1 5 4 2 2 5 6 1 4 3 6 | 2 5 6 5 1 4 2 2 5 6 1 4 3 6 | No | 7.16 |
| 4 | 2 1 3 2 4 1 6 3 1 6 2 1 5 4 | 2 1 3 2 4 1 6 3 1 6 2 1 5 4 | Yes | 7.3 |
| 5 | 3 1 3 1 5 4 6 1 5 2 4 6 1 2 | 3 1 3 1 5 4 6 1 5 2 4 6 1 2 | Yes | 8.9 |
| 6 | 3 5 2 5 3 2 3 2 6 5 4 3 1 1 | 3 5 2 5 3 2 2 3 6 5 4 3 1 1 | No | 6.97 |
| 7 | 5 6 6 1 6 5 2 3 2 4 6 2 1 5 | 5 3 6 1 6 5 2 2 3 4 6 2 1 5 | No | 8.05 |
| 8 | 3 6 4 1 1 6 3 1 2 6 4 6 4 3 | 3 6 4 1 1 6 6 1 2 3 4 3 4 6 | No | 5.31 |
| 9 | 6 2 1 3 6 2 3 4 1 5 1 5 3 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the digits 1–6 exactly once.  The puzzle grid (with empty cells as .): ``` 1 . . \| 5 3 4 4 5 . \| . 2 . ------+------ . . 6 \| . . . 3 2 5 \| 6 4 . ------+------ . 4 . \| 1 6 2 6 . 4 \| 2 5 3 ```  **Step-by-step resolution:** 1.  **Row 1:** 1, 2, 6 | No | 9.55 |
| 10 | 3 6 5 1 3 4 5 4 2 2 6 6 5 4 | 3 6 5 1 3 4 5 4 2 2 6 6 5 4 | Yes | 9.61 |
| 11 | 5 2 6 4 2 4 5 3 6 3 4 6 5 2 | 5 2 6 4 2 4 6 5 3 3 4 6 5 2 | No | 7.51 |
| 12 | 3 1 5 2 3 6 1 5 6 1 3 4 2 2 | 3 1 5 2 6 5 5 6 3 2 4 3 4 2 | No | 8.45 |
| 13 | 2 3 4 1 4 6 1 2 5 2 3 5 1 4 | 2 3 4 1 4 6 2 1 5 3 2 5 1 4 | No | 7.99 |
| 14 | 3 2 6 1 1 4 5 3 4 5 4 2 3 2 | 3 6 4 2 1 5 1 4 5 3 3 4 5 2 2 4 | No | 3.96 |
| 15 | 3 5 1 4 6 3 2 1 1 5 1 1 3 2 | 3 5 1 4 6 3 2 1 1 5 1 1 3 2 | Yes | 6.16 |
| 16 | 4 6 3 1 5 3 2 6 1 6 5 2 3 5 | 4 6 3 1 5 3 2 6 1 6 5 2 3 5 | Yes | 8.32 |
| 17 | 6 2 4 3 2 1 3 1 4 2 4 6 5 1 | 6 2 4 3 2 1 3 4 1 2 4 6 5 1 | No | 9.08 |
| 18 | 5 2 4 1 1 6 5 3 3 6 2 5 5 3 | 5 2 4 1 1 6 5 3 5 6 2 3 3 5 | No | 9.13 |
| 19 | 4 2 2 4 1 5 1 6 3 4 2 5 3 6 | 4 2 2 4 1 5 6 1 3 4 2 3 5 6 | No | 7.11 |
| 20 | 4 2 3 2 6 4 2 3 3 4 2 1 2 1 | To solve the 6×6 Sudoku puzzle, we fill in the empty cells following the rules (each row, column, and 2×3 box contains 1-6):  **Puzzle Grid:** . 1 3 \| 6 . 5 . . 1 \| 5 . . -----+----- 5 6 . \| 4 1 . 1 5 6 \| . 4 2 -----+----- 6 3 . \| . 5 . . 4 5 \| . 3 6  **Solving process:** 1. R4C4 must be 3 (only number missing in R4). 2. Through logical deduction for the remaining cells:    - R1: 4 1 3 \| 6 2 5    - R2: 3 2 1 \| 5 6 4    - R3: 5 6 2 \| 4 1 3    - R4: 1 5 6 \| 3 4 2    - R5: 6 3 4 \| 2 5 1    - R6: 2 4 5 \| 1 3 6  **The missing numbers | No | 9.79 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1591 | 1591 | Yes | 4.95 |
| 2 | 1320 | 1320 | Yes | 2.4 |
| 3 | 1613 | 1613 | Yes | 2.4 |
| 4 | 1591 | 1591 | Yes | 1.72 |
| 5 | 1917 | 1917 | Yes | 2.88 |
| 6 | 1692 | 1692 | Yes | 2.37 |
| 7 | 2055 | 2055 | Yes | 1.6 |
| 8 | 2272 | 2272 | Yes | 2.2 |
| 9 | 1423 | 1423 | Yes | 2.0 |
| 10 | 1158 | 1158 | Yes | 5.7 |
| 11 | 1391 | 1391 | Yes | 2.02 |
| 12 | 1760 | 1760 | Yes | 1.93 |
| 13 | 1627 | 1627 | Yes | 2.19 |
| 14 | 2336 | 2336 | Yes | 2.23 |
| 15 | 2199 | 2199 | Yes | 2.43 |
| 16 | 1795 | 1795 | Yes | 1.95 |
| 17 | 2202 | 2202 | Yes | 2.1 |
| 18 | 776 | 776 | Yes | 2.42 |
| 19 | 2579 | 2579 | Yes | 1.6 |
| 20 | 1697 | 1697 | Yes | 2.29 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 59 | No | 4.24 |
| 2 | 63 | 63 | Yes | 9.02 |
| 3 | 47 | 45 | No | 9.71 |
| 4 | 55 | 55 | Yes | 7.38 |
| 5 | 45 | 39 | No | 8.53 |
| 6 | 47 | 47 | Yes | 8.35 |
| 7 | 62 | To count the total number of zeros in the provided text, we examine each row:  1.  1101110001: 4 zeros 2.  0101110101: 4 zeros 3.  0111011001: 4 zeros 4.  011 | No | 9.03 |
| 8 | 66 | 62 | No | 6.48 |
| 9 | 62 | 57 | No | 7.22 |
| 10 | 72 | 73 | No | 8.12 |
| 11 | 62 | 61 | No | 9.44 |
| 12 | 58 | 58 | Yes | 20.03 |
| 13 | 66 | 66 | Yes | 6.86 |
| 14 | 59 | 59 | Yes | 11.8 |
| 15 | 60 | 60 | Yes | 8.36 |
| 16 | 46 | 46 | Yes | 7.13 |
| 17 | 44 | 44 | Yes | 5.22 |
| 18 | 64 | 63 | No | 8.34 |
| 19 | 59 | 59 | Yes | 8.83 |
| 20 | 67 | 67 | Yes | 10.55 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AJWVIRH | AJWVIRH | Yes | 1.97 |
| 2 | SCPIVET | SCPIVET | Yes | 5.75 |
| 3 | UJKETQB | UJKETQB | Yes | 7.47 |
| 4 | AXIGDRZ | TIMEOUT | No | 120.03 |
| 5 | KRGSOWC | KRG SOWC | No | 4.8 |
| 6 | XCPKLIU | XCPLKIU | No | 10.88 |
| 7 | AFMYLPO | AFMYLPO | Yes | 4.67 |
| 8 | DKZTHRO | DKZTHRO | Yes | 16.54 |
| 9 | XIFSLEO | XIFSLEO | Yes | 4.53 |
| 10 | QJMBFXA | QJMBFXA | Yes | 3.35 |
| 11 | HOKXWVR | HOKXWVR | Yes | 4.32 |
| 12 | OTIESNY | OTIESNY | Yes | 26.1 |
| 13 | GZMYCLH | GZMYCL | No | 6.39 |
| 14 | HQTIFNJ | HQTIFNJ | Yes | 3.83 |
| 15 | BPLAIHZ | BPLAIHZ | Yes | 6.88 |
| 16 | ADNCSQW | ADNCSQW | Yes | 4.2 |
| 17 | WHJNAVG | WHJNAVG | Yes | 5.0 |
| 18 | NXURPEZ | NXURPEZ | Yes | 3.01 |
| 19 | KRIXTQC | KRIXTQC | Yes | 4.88 |
| 20 | MZAVELO | MZAVELO | Yes | 3.89 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.8, 7.2] | 2.8 7.2 | Yes | 2.7 |
| 2 | [4.6, 5.4] | 5.4 4.6 | Yes | 10.38 |
| 3 | [4.6, 5.4] | 4.6 5.4 | Yes | 3.68 |
| 4 | [4.6, 5.4] | 4.6 5.4 | Yes | 3.75 |
| 5 | [0.3, 9.7] | 0.3 9.7 | Yes | 3.91 |
| 6 | [0.8, 9.2] | 9.2 0.8 | Yes | 3.92 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 9.69 |
| 8 | [1.1, 8.9] | 8.9 1.1 | Yes | 14.93 |
| 9 | [1.2, 8.8] | 1.2 8.8 | Yes | 3.19 |
| 10 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.34 |
| 11 | [0.1, 9.9] | 9.9 0.1 | Yes | 3.83 |
| 12 | [4.7, 5.3] | 4.7 5.3 | Yes | 3.96 |
| 13 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.22 |
| 14 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.28 |
| 15 | [3.1, 6.9] | 6.9 3.1 | Yes | 43.2 |
| 16 | [4.2, 5.8] | 4.2 5.8 | Yes | 4.2 |
| 17 | [2.1, 7.9] | 2.1 7.9 | Yes | 4.09 |
| 18 | [1.4, 8.6] | 8.6 1.4 | Yes | 3.11 |
| 19 | [0.6, 9.4] | 0.6 9.4 | Yes | 4.44 |
| 20 | [4.1, 5.9] | 5.9 4.1 | Yes | 4.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | O3OAL0RACGZF | O3OAL0RACGZF | Yes | 12.15 |
| 2 | IY6NA5GBGQW3 | IY6NA5GBGQW3 | Yes | 1.97 |
| 3 | NX9VQTK9QX9G | NX9VQTK9QX9G | Yes | 3.13 |
| 4 | AA1I6HKPR7IE | AA1I6HKPR7IE | Yes | 1.98 |
| 5 | MZ0AAYPE7U6X | MZ0AAYPE7U6X | Yes | 14.68 |
| 6 | I3AG8KURCT3Z | I3AG8KURCT3Z | Yes | 5.22 |
| 7 | Q2OI4S5YW6Z8 | Q2OI4S5YW6Z8 | Yes | 3.66 |
| 8 | Z2Q1W7TUSEFM | Z2Q1W7TUSEFM | Yes | 1.98 |
| 9 | 4MM2XQFFLSFZ | 4MM2XQFFLSFZ | Yes | 1.85 |
| 10 | 9KBE05J1MLVE | 9KBE05J1MLVE | Yes | 8.81 |
| 11 | PV7VXOQVEAJU | PV7VXOQVEAJU | Yes | 1.88 |
| 12 | KX4YHGOMPKAG | KX4YHGOMPKAG | Yes | 4.88 |
| 13 | 626BNFG2YABY | 626BNFG2YABY | Yes | 3.54 |
| 14 | 4KVKQUR6R1X7 | 4KVKQUR6R1X7 | Yes | 7.04 |
| 15 | OJMS3Y1ZBMI5 | OJMS3Y1ZBMI5 | Yes | 2.23 |
| 16 | Q18FRPCT26MX | Q18FRPCT26MX | Yes | 2.43 |
| 17 | PC7NXZ92FSAW | PC7NXZ92FSAW | Yes | 2.17 |
| 18 | 2VSFVOZB7B9M | 2VSFVOZB7B9M | Yes | 2.2 |
| 19 | PQ6JAF38BW1F | PQ6JAF38BW1F | Yes | 2.18 |
| 20 | R8CEGT00P4OZ | R8CEGT00P4OZ | Yes | 10.97 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 2.76 |
| 2 | 23 | 23 | Yes | 2.36 |
| 3 | 5 | 5 | Yes | 2.45 |
| 4 | 26 | 26 | Yes | 3.88 |
| 5 | 39 | 39 | Yes | 1.94 |
| 6 | 67 | 67 | Yes | 2.26 |
| 7 | 7 | 7 | Yes | 2.92 |
| 8 | 9 | 9 | Yes | 9.21 |
| 9 | 64 | 64 | Yes | 2.69 |
| 10 | 20 | 20 | Yes | 6.33 |
| 11 | 65 | 65 | Yes | 1.76 |
| 12 | 4 | 4 | Yes | 2.29 |
| 13 | 44 | 44 | Yes | 2.28 |
| 14 | 6 | 6 | Yes | 2.25 |
| 15 | 5 | 5 | Yes | 5.99 |
| 16 | 36 | 36 | Yes | 5.64 |
| 17 | 48 | 48 | Yes | 2.15 |
| 18 | 4 | 4 | Yes | 2.33 |
| 19 | 28 | 28 | Yes | 2.47 |
| 20 | 60 | 60 | Yes | 3.27 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ()()(  (_ | ()()(  (_ | Yes | 5.47 |
| 2 | ) )(\/\_  | ) )(\/\_ | No | 5.27 |
| 3 | /   __((< | /   __((< | Yes | 3.07 |
| 4 | \\___/(__ | \\___/(__ | Yes | 5.55 |
| 5 |  ((__\ /_ | ((__ /_ | No | 7.58 |
| 6 | <\/_(() < | <\/_(() < | Yes | 6.76 |
| 7 | )\(/\)(<( | )\(/\)(<(_<) | No | 5.66 |
| 8 | \_(_(\\(  | \_(_(\\ | No | 5.5 |
| 9 | \_<__\(<\ | \_<__\(<\) | No | 4.9 |
| 10 | _\)\__)\/ | _\)\__)\/ | Yes | 3.57 |
| 11 | \/\ <(/(  | \/ <(/ ( | No | 4.32 |
| 12 | )_<\< <)) | )_<\< <)) | Yes | 6.26 |
| 13 | _/\ ))(/  | _/ \))(/ | No | 4.45 |
| 14 | _<__)(_ _ | _<__)(_ _ | Yes | 15.98 |
| 15 | </\__<//) | /\) <(_<) | No | 4.54 |
| 16 | )__))_((\ | ))__))_(< | No | 4.74 |
| 17 | _\/((\(// | _\/((\(// | Yes | 4.22 |
| 18 |  /__<\<(( | /__<\<( | No | 3.9 |
| 19 | \(_(_\___ | \(_(_\ | No | 4.93 |
| 20 | /<)_((/// | /<)_((/// | Yes | 5.01 |
