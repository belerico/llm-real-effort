# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-19 10:04:59

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8060 | 38580 | 46640 | 8 | 12 | 26.68 | 533.81 |
| add_numbers | 3980 | 4132 | 8112 | 20 | 0 | 4.46 | 89.24 |
| counting_zeros | 6920 | 30855 | 37775 | 13 | 7 | 17.79 | 356.13 |
| task_decoding | 13360 | 5169 | 18529 | 20 | 0 | 5.98 | 119.71 |
| task_summation | 7280 | 15342 | 22622 | 20 | 0 | 12.45 | 249.15 |
| task_transcription | 4132 | 3449 | 7581 | 20 | 0 | 4.49 | 89.96 |
| task_sequences | 3241 | 8680 | 11921 | 19 | 1 | 8.37 | 167.46 |
| **TOTAL** | **46973** | **106207** | **153180** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 2 1 4 2 3 2 6 4 5 2 5 4 | 4 6 2 1 4 2 3 2 6 4 5 2 5 4 | Yes | 22.94 |
| 2 | 5 1 1 2 5 3 6 6 4 1 5 4 1 4 | 5 1 1 2 5 3 6 6 4 1 5 4 1 4 | Yes | 58.26 |
| 3 | 6 1 3 4 5 6 3 4 5 5 4 1 2 4 |  | No | 24.38 |
| 4 | 3 1 4 4 1 2 2 4 5 5 1 3 2 5 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Row 1:** Has 5,2,6 → needs 1,3,4 **Row 3:** Has 5,3,6 → needs 1,2,4 **Row 4:** Has 6,3,1 → needs 2,4,5 **Row 5:** Has 6,1,4,2,3 → needs 5 **Row 6:** Has 6,4 → needs 1,2,3,5  **Column analysis:** - Col 3: Has 5,4,3,6,1 → needs 2 → Row 6, Col 3 = **2** - Col 4: Has 2,1,6,3,4 → needs 5 → Row 6, Col 4 = **5** - Col 6: Has 6,5,1,3,4 → needs 2 → Row | No | 28.27 |
| 5 | 1 4 2 4 5 1 6 2 5 4 4 5 5 6 | Looking at this 6×6 Sudoku, I need to find all missing numbers systematically.  **Row 1:** 3, _, 6, 2, 5, _ → needs 1, 4 - Column 6 needs 4,5,6 and row needs 1,4 → position 6 = 4 - Position 2 = 1  **Row 2:** 6, _, 4, 5, 1, 3 → needs 2 - Position 2 = 2  **Row 3:** _, _, _, 3, 2, _ → needs 1,4,5,6 - Column 1 needs 2,4,5 → position 1 = 4 or 5 - Column 3 needs 1,5 → checking box constraints  **Row 4:** _, 3, _, _, 6, 1 → needs 2,4,5 - Column 4 needs only 4 → position 4 = 4 - Column 3 needs 1,5 → position 3 = 5 - Position 1 = 2  **Row 5:** 1, _, 2, 6, 3, _ → needs 4,5 - Bottom-right box needs 5 → position 6 = 5 - Position 2 = 4  **Row 6:** _, _, 3, 1, 4, 2 → needs 5,6 - Column 1 needs 4,5 → position 1 = 5 - Position 2 = 6  **Back to Row 3:**  - Column 1 has 3,6,2,1,5 → position 1 = 4 - Column 2 has 1,2,3,4,6 → position 2 = 5 - Column 3 has 6,4,5,2,3 → position 3 = 1 - Column 6 has 4,3,1,5,2 → position 6 = 6  **Missing numbers in reading order:** Row 1: 1, 4 Row 2: 2 | No | 22.58 |
| 6 | 5 3 4 2 1 4 6 5 4 1 5 2 3 6 | 5 3 4 2 1 4 6 5 4 1 5 2 3 6 | Yes | 25.22 |
| 7 | 6 2 2 1 5 2 5 3 1 6 4 4 6 3 | Looking at this 6×6 Sudoku, I'll solve it systematically by checking rows, columns, and 2×3 boxes.  **Row 2:** Has 5,3,4,1 → needs 2,6 - Column 2 needs 2,6; Column 4 needs 2,3,5,6 - Checking box constraints: (2,2)=6, (2,4)=2  **Row 3:** Has 4,6,3 → needs 1,2,5 - Column 2 still needs 2: (3,2)=2 - Column 3 needs 1,4,5; Column 4 needs 3,5,6 - (3,3)=1, (3,4)=5  **Row 4:** Has 4 → needs 1,2,3,5,6 - Column 1 needs only 2: (4,1)=2 - Column 3 needs 4,5: (4,3)=5 - Column 6 needs 4,6: (4,6)=6 - Column 4 needs 3,6: (4,4)=3 - Column 5 needs 1,3: (4,5)=1  **Row 5:** Has 6,3,2,1,5 → needs 4 - (5,6)=4  **Row 6:** Has 1,5,2 → needs 3,4,6 - Column 3 needs 4: (6,3)=4 - Column 4 needs 6: (6,4)=6 - Column 5 needs 3: (6,5)=3  **Missing numbers in reading order:** Row 2: 6, 2 Row 3: 2, 1, 5 Row 4: 2, | No | 22.99 |
| 8 | 2 4 3 3 6 4 5 3 5 5 4 6 3 5 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 4:** Has 1,_,2,6,3,4 → Missing 5 → Position 2 = 5 **Row 5:** Has 2,_,5,3,1,6 → Missing 4 → Position 2 = 4  **Column 1:** Has 5,_,4,1,2,_ → Missing 3,6 - Row 2: Checking box constraints and row 2 needs → 6 - Row 6: Therefore = 3  **Column 2:** Has _,_,1,5,4,_ → Missing 2,3,6 - Row 1: | No | 32.44 |
| 9 | 4 3 4 3 6 2 3 6 5 4 6 2 4 1 |  | No | 25.72 |
| 10 | 2 6 1 3 4 3 1 5 3 5 2 6 1 3 | 2 6 1 3 4 3 1 5 3 5 2 6 1 3 | Yes | 22.52 |
| 11 | 4 1 2 4 6 2 6 1 5 5 6 2 1 5 | 4 1 2 4 6 2 6 1 5 5 6 2 1 5 | Yes | 24.16 |
| 12 | 6 4 6 6 1 2 6 1 5 1 6 2 2 5 | 6 4 6 6 1 2 6 1 5 1 6 2 2 5 | Yes | 23.04 |
| 13 | 6 4 3 6 3 4 3 2 1 6 4 5 5 4 | 6 4 6 3 3 4 3 2 1 6 4 5 5 4 | No | 28.08 |
| 14 | 3 1 6 2 2 6 5 1 3 6 2 3 3 4 |  | No | 25.17 |
| 15 | 6 6 1 5 2 4 3 3 1 4 1 5 2 4 |  | No | 29.66 |
| 16 | 2 5 6 3 4 1 3 1 6 6 2 2 4 6 | 2 5 6 3 4 1 3 1 6 2 6 4 | No | 27.68 |
| 17 | 3 5 4 6 6 5 3 2 5 6 5 4 4 3 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Row 2:** Has 4, 1, 3, 5, 2 → Missing 6 in position 2 **Row 2:** 4, **6**, 1, 3, 5, 2  **Row 1:** Analyzing with columns and top boxes: - Position 1: Column 1 needs {2,3,5}, Row needs {3,4,5,6} → 3 or 5 - Position 3: Column 3 needs {5,6} → 5 or 6 - Top-right box needs {1,4,6}, so position 5 = 4, position 6 = 6 - This means position 3 = 5, position 1 = 3 **Row 1:** **3**, 1, **5**, 2, **4**, **6**  **Row 3:** Missing 3, 5 - Column 1 needs {2,5} → position 1 = 5 - Column 6 needs {3,4,5} → position 6 = 3 **Row 3:** **5**, 2, 4, 6, 1, **3**  **Row 4:** Missing 2, 5 - Column 1 needs {2} → position 1 = 2 - Column 6 → position 6 = 5 **Row 4:** **2**, 4, 3, 1, 6, **5**  **Row 5:** Missing 4, 5, 6 - Column 3 needs 6 → position 3 = 6 - Column 4 needs {4,5} → position 4 = 5 - Column 6 → position 6 = 4 **Row 5:** 1, 3, **6**, **5**, 2, **4**  **Row 6:** Missing 3, 4 - Column 4 needs 4 → position 4 = | No | 26.66 |
| 18 | 2 4 6 1 4 2 3 6 3 3 1 4 2 1 | 2 4 6 1 4 2 3 6 3 3 1 4 2 1 | Yes | 17.18 |
| 19 | 2 6 1 4 3 3 1 6 5 3 5 1 6 3 |  | No | 25.33 |
| 20 | 4 6 2 2 4 6 1 6 4 5 4 1 5 6 | 4 6 2 2 4 6 1 6 4 5 4 1 5 6 | Yes | 21.32 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1695 | 1695 | Yes | 4.18 |
| 2 | 912 | 912 | Yes | 6.55 |
| 3 | 1871 | 1871 | Yes | 3.42 |
| 4 | 1714 | 1714 | Yes | 4.1 |
| 5 | 2202 | 2202 | Yes | 4.69 |
| 6 | 1628 | 1628 | Yes | 4.53 |
| 7 | 2456 | 2456 | Yes | 4.73 |
| 8 | 2499 | 2499 | Yes | 4.1 |
| 9 | 2384 | 2384 | Yes | 5.02 |
| 10 | 919 | 919 | Yes | 3.04 |
| 11 | 1748 | 1748 | Yes | 4.27 |
| 12 | 1841 | 1841 | Yes | 5.22 |
| 13 | 735 | 735 | Yes | 2.5 |
| 14 | 1754 | 1754 | Yes | 5.66 |
| 15 | 1837 | 1837 | Yes | 5.06 |
| 16 | 2543 | 2543 | Yes | 4.31 |
| 17 | 1751 | 1751 | Yes | 3.63 |
| 18 | 1392 | 1392 | Yes | 4.91 |
| 19 | 1651 | 1651 | Yes | 4.55 |
| 20 | 1510 | 1510 | Yes | 4.66 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 40 | Yes | 23.62 |
| 2 | 70 | 67 | No | 19.13 |
| 3 | 60 | 60 | Yes | 18.24 |
| 4 | 49 | 49 | Yes | 12.3 |
| 5 | 52 | 52 | Yes | 18.16 |
| 6 | 73 | 73 | Yes | 22.49 |
| 7 | 46 | 45 | No | 14.34 |
| 8 | 65 | 64 | No | 20.25 |
| 9 | 71 | 71 | Yes | 18.07 |
| 10 | 41 | 41 | Yes | 17.59 |
| 11 | 44 | 44 | Yes | 18.25 |
| 12 | 40 | 40 | Yes | 20.61 |
| 13 | 41 | 41 | Yes | 10.02 |
| 14 | 47 | 47 | Yes | 11.04 |
| 15 | 61 | I'll count the zeros in each row systematically.  Row 1: 0 1 1 0 1 0 0 1 0 1 → 5 zeros Row 2: 1 0 0 0 1 1 0 1 1 0 → 5 zeros Row 3: 0 0 1 1 0 1 0 0 1 1 → 5 zeros Row 4: 0 0 0 1 1 1 1 1 1 0 → 4 zeros Row 5: 0 0 0 1 0 1 0 1 1 1 → 5 zeros Row 6: 1 1 1 1 1 0 0 1 1 0 → 3 zeros Row 7: 0 0 1 1 1 0 0 1 1 0 → 5 zeros Row 8: 0 1 0 1 1 0 1 0 0 1 → 5 zeros Row 9: 1 0 1 1 1 0 1 1 1 0 → 3 zeros Row 10: 1 1 0 1 1 1 1 1 1 1 → 1 zero Row 11: 1 0 1 1 0 0 0 0 0 1 1 → 6 zeros Row 12 | No | 42.92 |
| 16 | 40 | 40 | Yes | 16.61 |
| 17 | 39 | 40 | No | 11.95 |
| 18 | 44 | 44 | Yes | 11.68 |
| 19 | 63 | 61 | No | 10.9 |
| 20 | 71 | 69 | No | 17.67 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KSWJVET | KSWJVET | Yes | 4.98 |
| 2 | SFLACEM | SFLACEM | Yes | 4.75 |
| 3 | CBVMPYT | CBVMPYT | Yes | 4.2 |
| 4 | RWAGJVD | RWAGJVD | Yes | 4.63 |
| 5 | AVZEJMW | AVZEJMW | Yes | 4.69 |
| 6 | JXHRVGN | JXHRVGN | Yes | 4.82 |
| 7 | TEDBXGA | TEDBXGA | Yes | 4.56 |
| 8 | DXWQSOY | DXWQSOY | Yes | 4.94 |
| 9 | SCKZTHR | SCKZTHR | Yes | 4.8 |
| 10 | DTWXVZH | DTWXVZH | Yes | 4.98 |
| 11 | EGUKAXI | EGUKAXI | Yes | 6.03 |
| 12 | ACDXMGK | ACDXMGK | Yes | 5.13 |
| 13 | LWGBYUT | LWGBYUT | Yes | 4.63 |
| 14 | LJVYCSB | LJVYCSB | Yes | 5.08 |
| 15 | AKVFXNM | AKVFXNM | Yes | 5.59 |
| 16 | NKQYZIF | NKQYZIF | Yes | 4.53 |
| 17 | ZINYVHM | ZINYVHM | Yes | 23.68 |
| 18 | XHIOZDC | XHIOZDC | Yes | 6.71 |
| 19 | QDERNZX | QDERNZX | Yes | 4.9 |
| 20 | RVLKQHM | RVLKQHM | Yes | 5.9 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.4, 6.6] | 3.4 6.6 | Yes | 22.52 |
| 2 | [1.3, 8.7] | 8.7 1.3 | Yes | 8.99 |
| 3 | [3.1, 6.9] | 3.1 6.9 | Yes | 9.52 |
| 4 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.88 |
| 5 | [3.5, 6.5] | 6.5 3.5 | Yes | 11.25 |
| 6 | [2.7, 7.3] | 7.3 2.7 | Yes | 9.45 |
| 7 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.18 |
| 8 | [0.1, 9.9] | 9.9 0.1 | Yes | 10.18 |
| 9 | [1.6, 8.4] | 1.6 8.4 | Yes | 9.27 |
| 10 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.44 |
| 11 | [0.9, 9.1] | 9.1 0.9 | Yes | 34.9 |
| 12 | [1.7, 8.3] | 8.3 1.7 | Yes | 15.58 |
| 13 | [2.2, 7.8] | 7.8 2.2 | Yes | 8.55 |
| 14 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.56 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.38 |
| 16 | [4.0, 6.0] | 4.0 6.0 | Yes | 20.24 |
| 17 | [0.9, 9.1] | 9.1 0.9 | Yes | 9.48 |
| 18 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.84 |
| 19 | [2.4, 7.6] | 7.6 2.4 | Yes | 8.46 |
| 20 | [2.1, 7.9] | 2.1 7.9 | Yes | 13.28 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SD7IBKLAQ20A | SD7IBKLAQ20A | Yes | 3.36 |
| 2 | QX3O712R1GG3 | QX3O712R1GG3 | Yes | 4.8 |
| 3 | 8JY1M8W21C0D | 8JY1M8W21C0D | Yes | 3.96 |
| 4 | UUEJYVRJYYU7 | UUEJYVRJYYU7 | Yes | 4.08 |
| 5 | H78D72B4E4CY | H78D72B4E4CY | Yes | 4.12 |
| 6 | NJO1RZZHHMI3 | NJO1RZZHHMI3 | Yes | 6.17 |
| 7 | PJ3FNI616IHS | PJ3FNI616IHS | Yes | 3.86 |
| 8 | UMMHCROKEDER | UMMHCROKEDER | Yes | 3.7 |
| 9 | JGOS6H6W1AYB | JGOS6H6W1AYB | Yes | 4.84 |
| 10 | L9M46NQWSPX5 | L9M46NQWSPX5 | Yes | 4.68 |
| 11 | 1VWED6465SLA | 1VWED6465SLA | Yes | 4.19 |
| 12 | 00FO3ERPRB6X | 00FO3ERPRB6X | Yes | 4.43 |
| 13 | LC0EMH39GJUO | LC0EMH39GJUO | Yes | 3.75 |
| 14 | 0QAERSZ11SUZ | 0QAERSZ11SUZ | Yes | 5.65 |
| 15 | X36R8EW3PFFC | X36R8EW3PFFC | Yes | 3.81 |
| 16 | FQ20GQNIFFQY | FQ20GQNIFFQY | Yes | 8.58 |
| 17 | KBF76UWUA2HZ | KBF76UWUA2HZ | Yes | 3.4 |
| 18 | XCD0JWXO6G7L | XCD0JWXO6G7L | Yes | 4.68 |
| 19 | XPYCV5MK0CE2 | XPYCV5MK0CE2 | Yes | 4.09 |
| 20 | OH5E5SXMOLBA | OH5E5SXMOLBA | Yes | 3.7 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 3.05 |
| 2 | 26 | 26 | Yes | 8.03 |
| 3 | 793 | 793 | Yes | 3.16 |
| 4 | 16 | 16 | Yes | 3.83 |
| 5 | 4096 | 4096 | Yes | 17.84 |
| 6 | 4 | 4 | Yes | 5.81 |
| 7 | 65 | 65 | Yes | 4.97 |
| 8 | 19 | 19 | Yes | 4.19 |
| 9 | 64 | 64 | Yes | 5.17 |
| 10 | 10 | 10 | Yes | 13.1 |
| 11 | 44 | 44 | Yes | 5.58 |
| 12 | 20 | 20 | Yes | 8.43 |
| 13 | 9 | 9 | Yes | 35.15 |
| 14 | 39 | 39 | Yes | 4.42 |
| 15 | 6 | 6 | Yes | 5.53 |
| 16 | 31 | 31 | Yes | 4.32 |
| 17 | 5 | 14 | No | 13.15 |
| 18 | 60 | 60 | Yes | 12.54 |
| 19 | 7680 | 7680 | Yes | 4.51 |
| 20 | 5 | 5 | Yes | 4.66 |
