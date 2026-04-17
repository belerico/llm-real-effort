# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-26 15:45:23

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
| sudoku_game | 5779 | 38184 | 43963 | 11 | 9 | 25.95 | 519.11 |
| add_numbers | 3180 | 1673 | 4853 | 20 | 0 | 2.91 | 58.26 |
| counting_zeros | 4500 | 24352 | 28852 | 16 | 4 | 14.63 | 292.54 |
| task_decoding | 4500 | 5346 | 9846 | 19 | 1 | 6.41 | 128.25 |
| task_summation | 4560 | 15529 | 20089 | 20 | 0 | 9.75 | 194.96 |
| task_transcription | 3343 | 2854 | 6197 | 20 | 0 | 3.87 | 77.32 |
| task_sequences | 3240 | 7457 | 10697 | 19 | 1 | 6.58 | 131.67 |
| string_entry | 3714 | 5092 | 8806 | 11 | 9 | 6.86 | 137.15 |
| **TOTAL** | **32816** | **100487** | **133303** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 6 5 4 1 6 2 6 5 4 1 1 4 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Row 1:** 5 _ 4 \| 1 _ _ - Column 2 has 6,2,5 and row needs 2,3,6 → position (1,2) = 3 - Column 5 has 1,5,4,3,6 → position (1,5) = 2 - Remaining for row 1 → position (1,6) = 6  **Row 2:** 2 6 3 \| _ 1 _ - After analyzing box and columns → (2,4) = 5, (2,6) = 4  **Row 3:** 4 _ _ \| _ 5 3 - Middle-right box needs 1,2,6 for remaining cells - Column 4 analysis → (3,4) = 2 - Column 2 has 3,6,2,5, row needs 1,6 → (3,2) = 1 - Remaining → (3,3) = 6  **Row 4:** 3 2 1 \| _ 4 _ - Box constraint and column 4 → (4,4) = 6 - Column 6 needs 1,4,5, row needs 5,6 → (4,6) = 5  **Row 5:** 6 5 2 \| _ 3 _ - Column 4 needs 4 → (5,4) = 4 - Remaining → (5,6) = 1  **Row 6:** _ _ 5 \| 3 6 2 - Column 1 has 5,2,4,3,6 → (6,1) = 1 - Remaining → (6, | No | 24.25 |
| 2 | 3 3 6 4 2 2 3 6 5 3 2 1 4 1 |  | No | 28.56 |
| 3 | 3 2 5 3 2 4 6 2 3 4 2 4 1 3 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 4 1 . \| 6 . . - Has: 1,4,6 → Missing: 2,3,5 - Column 5 needs 2 (only option) → position 5 = 2 - Column 3 needs {2,3,4}, row needs {3,5} → position 3 = 3 - Remaining position 6 = 5  **Row 2:** . . 1 \| 5 6 . - Has: 1,5,6 → Missing: 2,3,4 - Column 6 needs {4,5}, row needs {2,3,4} → position 6 = 4 - Top-left box analysis: position 1 = 3, position 2 = 2  **Row 3:** 5 . . \| 4 1 3 - Has: 1,3,4,5 → Missing: 2,6 - Column 2 needs {3,6}, row needs {2,6} → position 2 = 6 - Remaining position 3 = 2  **Row 4:** 6 . . \| 2 5 1 - Has: 1,2,5,6 → Missing: 3,4 - Column 2 needs 3 → position 2 = 3 - Remaining position 3 = 4  **Row 5:** . . 5 \| 1 3 6 - Has: 1,3,5, | No | 30.39 |
| 4 | 2 1 4 5 6 1 6 2 1 3 5 6 3 4 | 2 1 4 5 6 1 6 2 1 3 5 6 3 4 | Yes | 29.36 |
| 5 | 2 4 6 2 5 5 3 3 2 6 1 1 4 4 | 2 4 6 2 5 5 3 3 2 6 1 1 4 4 | Yes | 24.84 |
| 6 | 6 6 2 1 3 6 4 1 5 4 1 3 3 6 | 6 6 2 4 3 6 1 5 1 5 1 4 3 3 6 | No | 31.5 |
| 7 | 2 3 5 1 4 6 4 6 5 6 1 3 2 4 |  | No | 28.94 |
| 8 | 1 6 3 2 3 4 6 4 1 2 4 1 3 2 | 1 6 3 2 3 4 6 4 1 2 4 1 3 2 | Yes | 23.4 |
| 9 | 2 1 4 6 4 5 6 6 6 3 4 5 1 3 | 2 1 4 6 4 5 6 6 6 3 4 5 1 3 | Yes | 25.24 |
| 10 | 4 6 3 2 5 4 4 6 4 4 5 6 3 1 | 4 6 3 2 5 4 4 6 4 4 5 6 3 1 | Yes | 21.9 |
| 11 | 6 4 6 1 3 1 5 2 4 2 1 3 3 1 |  | No | 30.67 |
| 12 | 3 6 5 4 4 6 2 4 3 1 2 6 3 2 | 3 6 5 4 4 6 2 4 3 1 2 6 3 2 | Yes | 33.18 |
| 13 | 3 2 5 1 5 2 4 6 1 4 5 4 5 2 | 3 2 5 1 5 2 4 6 1 4 5 4 5 2 | Yes | 29.32 |
| 14 | 3 2 4 2 5 6 1 4 2 6 4 5 1 1 |  | No | 27.57 |
| 15 | 3 3 4 5 4 3 1 1 4 2 5 1 5 4 |  | No | 24.47 |
| 16 | 1 6 4 3 5 4 1 1 4 2 3 2 3 1 | 1 6 4 3 5 4 1 1 4 2 3 2 3 1 | Yes | 17.51 |
| 17 | 1 6 4 2 3 2 1 4 2 3 5 1 5 4 | 1 6 4 2 3 2 1 4 2 3 5 1 5 4 | Yes | 19.22 |
| 18 | 1 4 6 5 3 4 6 3 6 5 4 1 5 2 | 4 1 6 5 3 4 6 3 6 5 1 4 5 2 | No | 32.12 |
| 19 | 2 1 1 6 3 3 5 3 1 2 1 4 2 5 | 2 1 1 6 3 3 5 3 1 2 1 4 2 5 | Yes | 16.53 |
| 20 | 6 3 6 5 3 6 4 5 1 4 5 5 2 1 | 6 3 6 5 3 6 4 5 1 4 5 5 2 1 | Yes | 20.09 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1453 | 1453 | Yes | 2.39 |
| 2 | 1159 | 1159 | Yes | 2.72 |
| 3 | 2167 | 2167 | Yes | 2.37 |
| 4 | 1441 | 1441 | Yes | 2.53 |
| 5 | 911 | 911 | Yes | 2.41 |
| 6 | 1722 | 1722 | Yes | 3.19 |
| 7 | 1352 | 1352 | Yes | 2.58 |
| 8 | 781 | 781 | Yes | 2.63 |
| 9 | 1685 | 1685 | Yes | 2.77 |
| 10 | 1655 | 1655 | Yes | 2.73 |
| 11 | 489 | 489 | Yes | 3.47 |
| 12 | 2217 | 2217 | Yes | 2.45 |
| 13 | 2202 | 2202 | Yes | 2.71 |
| 14 | 1721 | 1721 | Yes | 4.02 |
| 15 | 1762 | 1762 | Yes | 4.1 |
| 16 | 2312 | 2312 | Yes | 2.84 |
| 17 | 1840 | 1840 | Yes | 2.47 |
| 18 | 898 | 898 | Yes | 3.14 |
| 19 | 1225 | 1225 | Yes | 4.04 |
| 20 | 1555 | 1555 | Yes | 2.71 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 71 | 71 | Yes | 22.8 |
| 2 | 53 | 52 | No | 14.03 |
| 3 | 42 | 42 | Yes | 20.38 |
| 4 | 54 | 54 | Yes | 12.95 |
| 5 | 58 | 57 | No | 13.94 |
| 6 | 37 | 37 | Yes | 13.95 |
| 7 | 59 | 59 | Yes | 15.61 |
| 8 | 35 | 35 | Yes | 11.92 |
| 9 | 67 | 67 | Yes | 12.01 |
| 10 | 57 | 57 | Yes | 14.86 |
| 11 | 45 | 45 | Yes | 16.36 |
| 12 | 41 | 41 | Yes | 11.87 |
| 13 | 57 | 53 | No | 13.5 |
| 14 | 75 | 79 | No | 17.65 |
| 15 | 67 | 67 | Yes | 11.86 |
| 16 | 53 | 53 | Yes | 10.44 |
| 17 | 68 | 68 | Yes | 11.65 |
| 18 | 57 | 57 | Yes | 8.56 |
| 19 | 59 | 59 | Yes | 21.23 |
| 20 | 51 | 51 | Yes | 16.99 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IUJMBWQ | IUJMBWQ | Yes | 6.0 |
| 2 | ZQFWBPT | ZQFWBPT | Yes | 7.85 |
| 3 | OADKYMW | OADKYMW | Yes | 4.79 |
| 4 | DLTHMPX | DLTHMPX | Yes | 7.98 |
| 5 | FTCXHAB | FTCXHAB | Yes | 6.06 |
| 6 | OVWLBKA | OVWLBKA | Yes | 5.48 |
| 7 | XIPGHDM | XIPGHDM | Yes | 7.91 |
| 8 | WXAGCMP | WXAGCMP | Yes | 5.33 |
| 9 | PFBGRNH | PFBGRNH | Yes | 5.83 |
| 10 | VDJBZLU | VDJBZLU | Yes | 4.06 |
| 11 | MPIOZLN | MPIOZLN | Yes | 14.6 |
| 12 | XEYUPRJ | XEYUPRJ | Yes | 7.6 |
| 13 | HWBUOTF | HWBUOTF | Yes | 3.8 |
| 14 | OFAHKCQ | OFAHKCQ | Yes | 9.34 |
| 15 | HWNICUG | HWNICUG | Yes | 6.38 |
| 16 | JSIFZMP | JISFZMP | No | 5.45 |
| 17 | SJIZHDF | SJIZHDF | Yes | 5.8 |
| 18 | LGTIZKA | LGTIZKA | Yes | 4.79 |
| 19 | BYQHKVA | BYQHKVA | Yes | 4.37 |
| 20 | QONRJGI | QONRJGI | Yes | 4.82 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.3, 9.7] | 0.3 9.7 | Yes | 13.51 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.08 |
| 3 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.96 |
| 4 | [4.5, 5.5] | 4.5 5.5 | Yes | 12.28 |
| 5 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.04 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 8.15 |
| 7 | [3.6, 6.4] | 3.6 6.4 | Yes | 6.89 |
| 8 | [4.1, 5.9] | 4.1 5.9 | Yes | 8.45 |
| 9 | [2.0, 8.0] | 2.0 8.0 | Yes | 9.47 |
| 10 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.69 |
| 11 | [3.0, 7.0] | 3.0 7.0 | Yes | 9.57 |
| 12 | [2.1, 7.9] | 7.9 2.1 | Yes | 12.72 |
| 13 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.94 |
| 14 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.31 |
| 15 | [2.5, 7.5] | 2.5 7.5 | Yes | 12.23 |
| 16 | [2.7, 7.3] | 2.7 7.3 | Yes | 11.53 |
| 17 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.52 |
| 18 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.33 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 8.86 |
| 20 | [1.4, 8.6] | 1.4 8.6 | Yes | 8.4 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | Q4PK84DT50V9 | Q4PK84DT50V9 | Yes | 4.38 |
| 2 | MLXOJC13S1X3 | MLXOJC13S1X3 | Yes | 3.63 |
| 3 | QGUZKOKVCTJP | QGUZKOKVCTJP | Yes | 3.34 |
| 4 | 2UGT8Z8DIXJW | 2UGT8Z8DIXJW | Yes | 3.66 |
| 5 | S9PMQ5YK1DXL | S9PMQ5YK1DXL | Yes | 3.44 |
| 6 | TUI4LQ50U9LO | TUI4LQ50U9LO | Yes | 4.11 |
| 7 | BRNKUHWDLHMH | BRNKUHWDLHMH | Yes | 3.84 |
| 8 | SBSBKKDZ11FC | SBSBKKDZ11FC | Yes | 4.4 |
| 9 | JS97XA9LOBJI | JS97XA9LOBJI | Yes | 3.78 |
| 10 | HK2VFBPLM4HQ | HK2VFBPLM4HQ | Yes | 3.45 |
| 11 | 4YKS69SOJO0L | 4YKS69SOJO0L | Yes | 3.55 |
| 12 | 5C15WCKO0Q5J | 5C15WCKO0Q5J | Yes | 4.65 |
| 13 | 32XMXQ9AIXLA | 32XMXQ9AIXLA | Yes | 4.09 |
| 14 | WFCVWZ19809X | WFCVWZ19809X | Yes | 3.59 |
| 15 | BKB6EB0J0B6U | BKB6EB0J0B6U | Yes | 3.44 |
| 16 | QU8D7ICSVP2L | QU8D7ICSVP2L | Yes | 3.82 |
| 17 | HAHAVO3PZXQH | HAHAVO3PZXQH | Yes | 4.15 |
| 18 | XWCTHXB5YLC3 | XWCTHXB5YLC3 | Yes | 4.25 |
| 19 | 4MSM38C8MMRD | 4MSM38C8MMRD | Yes | 3.91 |
| 20 | 7FGSJ6CHU74C | 7FGSJ6CHU74C | Yes | 3.83 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 4.71 |
| 2 | 73 | 73 | Yes | 6.13 |
| 3 | 20 | 20 | Yes | 9.75 |
| 4 | 64 | 64 | Yes | 6.43 |
| 5 | 5 | 16 | No | 14.48 |
| 6 | 31 | 31 | Yes | 4.71 |
| 7 | 39 | 39 | Yes | 5.17 |
| 8 | 9 | 9 | Yes | 6.82 |
| 9 | 7 | 7 | Yes | 3.54 |
| 10 | 793 | 793 | Yes | 3.44 |
| 11 | 60 | 60 | Yes | 5.1 |
| 12 | 67 | 67 | Yes | 3.02 |
| 13 | 3 | 3 | Yes | 12.4 |
| 14 | 9 | 9 | Yes | 5.94 |
| 15 | 63 | 63 | Yes | 5.71 |
| 16 | 19 | 19 | Yes | 4.71 |
| 17 | 6 | 6 | Yes | 6.26 |
| 18 | 36 | 36 | Yes | 2.94 |
| 19 | 10 | 10 | Yes | 12.48 |
| 20 | 44 | 44 | Yes | 7.93 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )\)<  < ( | )\)<  < ( | Yes | 4.75 |
| 2 | \ _</_<(  | \ _</_<( | No | 6.26 |
| 3 | <\/\/<\<  | <\/\/<\< | No | 4.74 |
| 4 | <\_(<__\_ | <\_(<__\_ | Yes | 9.84 |
| 5 | <__  /()( | <__  /()( | Yes | 4.82 |
| 6 |  _) < \\\ | _) < \\\ | No | 4.14 |
| 7 | \(\)))((\ | \(\)))((\ | Yes | 5.47 |
| 8 | () (\_()  | () (\_() | No | 6.05 |
| 9 | _\\\<))\_ | _\\\<))\_ | Yes | 4.29 |
| 10 | < ))/\) < | < ))/\) | No | 5.17 |
| 11 |  ((_ ))__ | ((_ )))__ | No | 12.68 |
| 12 | (((()/ )) | (((()/ ))) | No | 9.0 |
| 13 | (_)( _((( | (_)( _((( | Yes | 5.73 |
| 14 |  (<)_ (</ | (<)_ (</ | No | 6.22 |
| 15 | ()< (\ \( | ()< (\ \( | Yes | 5.37 |
| 16 | )\_  <_(_ | )\_  <_(_ | Yes | 5.07 |
| 17 | <(/<\  )\ | <(/<\  )\ | Yes | 14.15 |
| 18 | )<))(/)_  | )<))(/)_ | No | 13.8 |
| 19 | ))__()_\\ | ))__()_\\ | Yes | 4.21 |
| 20 | \((__(_ / | \((__(_ / | Yes | 5.37 |
