# Benchmark Report — gemini-3.1-flash-lite-preview

- **Model**: `google/gemini-3.1-flash-lite-preview`
- **Date**: 2026-03-26 10:33:58

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
| sudoku_game | 25702 | 34431 | 60133 | 5 | 15 | 10.69 | 214.0 |
| add_numbers | 25072 | 5214 | 30286 | 20 | 0 | 3.77 | 75.39 |
| counting_zeros | 24824 | 34401 | 59225 | 19 | 1 | 9.19 | 184.2 |
| task_decoding | 25266 | 8842 | 34108 | 20 | 0 | 5.01 | 100.41 |
| task_summation | 25042 | 16073 | 41115 | 20 | 0 | 6.60 | 132.13 |
| task_transcription | 24560 | 5505 | 30065 | 20 | 0 | 4.90 | 98.08 |
| task_sequences | 3179 | 7474 | 10653 | 19 | 1 | 4.06 | 81.28 |
| string_entry | 25280 | 16583 | 41863 | 7 | 13 | 6.23 | 124.72 |
| **TOTAL** | **178925** | **128523** | **307448** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 1 5 1 3 4 5 5 4 4 2 2 5 | 3 2 1 5 1 3 4 5 5 4 2 2 5 | No | 8.87 |
| 2 | 3 6 2 1 5 6 1 2 4 6 3 4 3 5 | 6 3 2 1 5 6 1 2 4 3 6 4 3 5 | No | 8.02 |
| 3 | 3 2 6 3 1 5 6 2 5 6 3 2 2 5 | To solve the 6×6 Sudoku puzzle, we fill in the empty cells while ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Step-by-step completion:** 1.  **Row 5** is missing 2: [2, 5, 3, 1, 6, 4]. 2.  **Row 2** is missing 3 and 1: [4, 2, 6, 3, 1, 5]. 3.  **Row 6** is missing 2 and 5: [6, 3, 4, 2, 5, 1]. 4.  **Row 1** is missing 3, 2, and 6: [3, 1, 2, 5, 4, 6]. 5.  **Row 4** is missing 5, 6, and 3: [1, 4, 5, 6, 3, 2]. 6.  **Row 3** is missing 5, 6, and 2: [5, 6, 1, 4, 2, 3].  **Completed grid:** 3 1 2 5 4 6 4 2 6 3 1 5 5 6 1 4 2 3 1 4 5 6 3 2 2 5 3 1 6 4 6 3 4 2 5 1  **Extracting the missing numbers in reading order:** | No | 8.54 |
| 4 | 3 1 6 6 4 1 4 6 5 6 1 2 3 4 | 3 1 6 6 4 1 4 6 5 6 1 2 3 4 | Yes | 10.19 |
| 5 | 2 1 3 5 2 1 6 4 1 6 4 2 5 1 | 2 1 3 5 2 1 6 4 1 6 4 2 5 1 | Yes | 18.11 |
| 6 | 2 1 3 2 5 4 1 5 2 4 2 3 5 1 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  The completed grid is: 4 2 1 \| 5 6 3 6 1 2 \| 3 5 4 3 5 6 \| 4 1 2 5 4 3 \| 6 2 1 1 6 4 \| 2 3 5 2 3 5 \| 1 4 6  The missing numbers in reading order (left to right, top to bottom) are: R1: 2, 1, 3 R2: 2 R3: 5, 4, 1 R4: 5, 2 R5: 4, 2, 3 R6: 5, 1  Wait, let's list the missing cells | No | 8.71 |
| 7 | 4 1 2 2 1 3 5 6 5 4 4 1 4 6 | 4 1 2 2 1 3 5 6 5 4 4 1 4 6 | Yes | 6.45 |
| 8 | 3 4 6 4 6 4 3 3 1 1 2 1 5 6 | 6 4 3 4 6 4 3 3 1 1 2 1 5 6 | No | 14.36 |
| 9 | 4 2 6 1 5 2 3 4 6 4 3 4 4 5 | 6 2 1 4 5 2 3 4 4 6 3 4 4 5 | No | 7.74 |
| 10 | 1 2 2 6 1 3 5 3 2 3 6 6 4 1 | 1 2 2 6 1 3 5 3 2 3 6 6 4 1 | Yes | 11.04 |
| 11 | 4 5 1 2 1 5 1 6 5 3 5 4 5 6 | 4 5 1 2 1 5 5 6 1 3 4 5 5 6 | No | 16.95 |
| 12 | 1 4 5 2 6 3 3 5 6 2 6 5 5 4 | 1 4 5 2 6 3 3 5 6 2 6 5 4 | No | 7.38 |
| 13 | 3 5 6 2 6 6 3 5 5 1 2 4 6 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  1.  **Analyze the grid:**     *   R1: [_, 1, _, 2, 4, _]     *   R | No | 19.83 |
| 14 | 1 4 3 5 4 5 2 3 6 2 3 6 4 2 | 1 4 3 5 4 5 2 3 6 2 3 6 4 2 | Yes | 7.27 |
| 15 | 4 5 3 6 3 1 5 2 3 5 2 2 3 4 | 4 5 6 3 3 1 5 2 3 5 2 3 2 4 | No | 11.71 |
| 16 | 1 3 1 5 6 3 1 5 2 5 3 4 2 1 | To solve the 6×6 Sudoku, we fill in the missing numbers based on the rules that each row, column, and 2×3 box must contain the numbers 1–6 exactly once.  **Step-by-step resolution:** 1.  **Row 1:** The missing numbers are 1 and 3. Column 5 already contains 1, 2, 4, 5, 6, so (1, 5) must be 3. Thus, (1, 1) is 1. (Row 1: 1 5 6 2 3 4) 2.  **Row 2:** The missing number is 1. (Row 2: 6 4 3 1 2 5) 3.  **Row 3:** The missing numbers are 5 and 6. Column 4 already contains 2, 1, 4, 6, 3, so (3, 4) must be 5. Thus, (3, 6) is 6. (Row 3: 2 3 4 5 1 6) 4.  **Column 4:** The missing number is 5. (Already filled in step 3). 5.  **Row 5:** The missing numbers are 3 and 5. Column 6 already contains 4, 5, 6, (4, 6), (5, 6), (6, 6). The missing numbers for Column 6 are 1, 2, 3. Since (5, 6) must be 3 or 5, it must be 3. Thus, (5, 1) is 5. (Row 5: 5 2 1 6 4 3) 6.  **Column 3:** The missing numbers are 2 and 5. (4, 3) must be 5 (as 2 is in Row 4, Column 1 or 6), and (6, 3) must be 2. 7.  **Row 4:** The missing numbers are 1, 2, 3, 5. Based on the remaining empty cells and column constraints, we complete the grid:     (4, 1)=3, (4, 2)=1, (4, 3)=5, (4, 6)=2. 8.  **Row 6:** The missing numbers are 1 and 4. (6, 1)=4, (6, 6)=1.  **Completed Grid:** 1 5 6 2 3 4 6 4 3 1 2 5 2 3 4 5 1 6 3 1 | No | 9.91 |
| 17 | 4 2 5 3 3 4 1 2 1 3 2 5 1 4 | 3 2 5 4 4 3 1 2 1 3 2 5 1 4 | No | 9.37 |
| 18 | 1 4 4 6 1 2 4 1 2 4 6 3 1 3 | 1 4 4 6 2 1 4 2 4 6 3 3 1 | No | 9.84 |
| 19 | 4 6 4 1 2 3 4 1 4 2 2 5 4 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers based on the rule that each row, column, and 2×3 box must contain the numbers 1-6 exactly once.  **Grid representation (0 = empty):** Row 1: 5 3 0 \| 1 2 0 Row 2: 0 0 6 \| 0 5 3 Row 3: 2 6 0 \| 5 1 0 Row 4: 3 5 0 \| 0 6 0 Row 5: 6 0 0 \| 3 0 1 Row 6: 1 4 2 \| 6 0 5  **Step-by-step reasoning:** 1. **Row 1:** Missing 4 and 6. Column 3 already contains 6, so R1C3 must be 4. R1C6 must be 6. Row 1: 5 3 4 1 2 6. 2. **Column 1:** Missing 4. R2C1 must be 4. 3. **Box 1 (Top-Left):** Missing 1 and 2. R2C2 must be 1 (since 2 is already in Column 2). R2C1 is 4. 4. **Row 2:** Missing 2. R2C4 must be 2. Row 2: 4 1 6 2 5 3. 5. **Column 2:** Missing 2. R5C2 must be 2. 6. **Box 3 (Middle-Left):** Missing 1 and 4. R3C3 must be 4 (since 1 is in Column 3), and R4C3 must be 1. 7. **Row 3:** Missing 3 and 4. R3C6 must be 4 (since 3 is in Column 6). R3C3 is 4, so R3C6 is 3. Row 3: 2 6 4 5 1 3. 8. **Row 4:** Missing 2 and 4. R4C4 must be 4, R4C6 must be 2. Row 4: 3 5 1 4 6 2. 9. **Row 5:** Missing 4 and 5. R5C3 must be 5, R5C5 must be 4. Row 5: 6 2 5 3 4 1. 10. **Row 6:** Missing 3. R6C5 must be 3. Row 6: 1 4 2 6 3 5.  **Completed Grid:** 5 3 4 1 2 6 4 1 6 2 5 3 2 6 4 5 1 3 3 5 1 4 6 2 6 2 5 3 4 1 1 4 2 6 3 5  **Missing numbers in reading order:** R1: 4, | No | 9.82 |
| 20 | 3 3 5 1 2 3 5 2 1 2 3 6 1 3 | To solve the 6×6 Sudoku puzzle, we fill in the missing numbers by ensuring each row, column, and 2×3 box contains the numbers 1-6 exactly once.  **Completed Grid:** 4 2 1 \| 5 6 3 3 5 6 \| 4 1 2 6 1 2 \| 3 | No | 9.71 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1925 | 1925 | Yes | 3.79 |
| 2 | 1556 | 1556 | Yes | 4.04 |
| 3 | 2641 | 2641 | Yes | 2.53 |
| 4 | 2016 | 2016 | Yes | 3.59 |
| 5 | 1134 | 1134 | Yes | 2.93 |
| 6 | 1600 | 1600 | Yes | 2.26 |
| 7 | 2555 | 2555 | Yes | 2.64 |
| 8 | 1944 | 1944 | Yes | 2.05 |
| 9 | 1776 | 1776 | Yes | 3.83 |
| 10 | 1711 | 1711 | Yes | 3.22 |
| 11 | 894 | 894 | Yes | 2.45 |
| 12 | 1950 | 1950 | Yes | 13.22 |
| 13 | 1485 | 1485 | Yes | 3.43 |
| 14 | 840 | 840 | Yes | 2.48 |
| 15 | 1067 | 1067 | Yes | 3.12 |
| 16 | 1649 | 1649 | Yes | 3.72 |
| 17 | 1135 | 1135 | Yes | 2.78 |
| 18 | 1465 | 1465 | Yes | 7.23 |
| 19 | 1326 | 1326 | Yes | 3.75 |
| 20 | 735 | 735 | Yes | 2.27 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 6.92 |
| 2 | 40 | 40 | Yes | 7.38 |
| 3 | 60 | 60 | Yes | 7.22 |
| 4 | 46 | 46 | Yes | 8.46 |
| 5 | 40 | 40 | Yes | 10.17 |
| 6 | 75 | 75 | Yes | 10.27 |
| 7 | 53 | 53 | Yes | 10.54 |
| 8 | 56 | 56 | Yes | 8.91 |
| 9 | 68 | 68 | Yes | 6.37 |
| 10 | 42 | 42 | Yes | 17.86 |
| 11 | 60 | 60 | Yes | 17.61 |
| 12 | 69 | 69 | Yes | 6.77 |
| 13 | 75 | 75 | Yes | 7.66 |
| 14 | 42 | 42 | Yes | 5.76 |
| 15 | 54 | 54 | Yes | 10.37 |
| 16 | 53 | 53 | Yes | 7.46 |
| 17 | 73 | 73 | Yes | 8.56 |
| 18 | 72 | 72 | Yes | 8.59 |
| 19 | 65 | 65 | Yes | 9.91 |
| 20 | 45 | 44 | No | 7.09 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GFQYULJ | GFQYULJ | Yes | 7.92 |
| 2 | GAOWVRS | GAOWVRS | Yes | 3.06 |
| 3 | FZQCBUI | FZQCBUI | Yes | 2.92 |
| 4 | JQDFOHW | JQDFOHW | Yes | 4.28 |
| 5 | XHABTCD | XHABTCD | Yes | 7.22 |
| 6 | RYHAOGS | RYHAOGS | Yes | 5.16 |
| 7 | PNTKLMU | PNTKLMU | Yes | 3.0 |
| 8 | ZMRAUYP | ZMRAUYP | Yes | 2.6 |
| 9 | QPJFMSN | QPJFMSN | Yes | 4.03 |
| 10 | ARDITQF | ARDITQF | Yes | 6.04 |
| 11 | GOZDJEK | GOZDJEK | Yes | 4.0 |
| 12 | APGURXE | APGURXE | Yes | 3.64 |
| 13 | ORKJBED | ORKJBED | Yes | 5.67 |
| 14 | SPEGRQX | SPEGRQX | Yes | 4.21 |
| 15 | UBSHAGD | UBSHAGD | Yes | 6.86 |
| 16 | IVUKELN | IVUKELN | Yes | 4.47 |
| 17 | OCYDTAZ | OCYDTAZ | Yes | 14.68 |
| 18 | PJXDHZO | PJXDHZO | Yes | 4.78 |
| 19 | VUKXLMR | VUKXLMR | Yes | 2.74 |
| 20 | QXTIZGR | QXTIZGR | Yes | 2.93 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 0.4 9.6 | Yes | 4.33 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 3.47 |
| 3 | [0.6, 9.4] | 0.6 9.4 | Yes | 8.27 |
| 4 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.89 |
| 5 | [1.4, 8.6] | 1.4 8.6 | Yes | 4.38 |
| 6 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.21 |
| 7 | [1.6, 8.4] | 8.4 1.6 | Yes | 4.77 |
| 8 | [4.9, 5.1] | 5.1 4.9 | Yes | 8.42 |
| 9 | [3.2, 6.8] | 3.2 6.8 | Yes | 4.16 |
| 10 | [3.8, 6.2] | 3.8 6.2 | Yes | 3.06 |
| 11 | [1.1, 8.9] | 8.9 1.1 | Yes | 9.09 |
| 12 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.33 |
| 13 | [1.5, 8.5] | 1.5 8.5 | Yes | 3.33 |
| 14 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.99 |
| 15 | [2.3, 7.7] | 7.7 2.3 | Yes | 7.32 |
| 16 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.28 |
| 17 | [1.5, 8.5] | 1.5 8.5 | Yes | 14.78 |
| 18 | [4.3, 5.7] | 4.3 5.7 | Yes | 4.2 |
| 19 | [4.1, 5.9] | 5.9 4.1 | Yes | 4.32 |
| 20 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.36 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | O4WQP34PWYMT | O4WQP34PWYMT | Yes | 1.93 |
| 2 | RQ3M8W76BIVQ | RQ3M8W76BIVQ | Yes | 13.74 |
| 3 | QQDE9N617LOL | QQDE9N617LOL | Yes | 2.86 |
| 4 | KIXOLSY3J0DT | KIXOLSY3J0DT | Yes | 17.06 |
| 5 | QK52QYT9C7NZ | QK52QYT9C7NZ | Yes | 3.96 |
| 6 | C49Y75MQBTEK | C49Y75MQBTEK | Yes | 7.46 |
| 7 | DWPX83M1PSON | DWPX83M1PSON | Yes | 2.77 |
| 8 | FBNIHAZJRNPO | FBNIHAZJRNPO | Yes | 3.71 |
| 9 | TD78IF10TFS3 | TD78IF10TFS3 | Yes | 9.53 |
| 10 | 1I7BNZQGRZX8 | 1I7BNZQGRZX8 | Yes | 3.4 |
| 11 | B6TMZQF95NH8 | B6TMZQF95NH8 | Yes | 1.34 |
| 12 | OUKDKT5Y24AC | OUKDKT5Y24AC | Yes | 2.17 |
| 13 | J3OPW0E7GCTM | J3OPW0E7GCTM | Yes | 4.16 |
| 14 | RI13OK0IVJ5L | RI13OK0IVJ5L | Yes | 6.51 |
| 15 | ZI4BRC9AJD48 | ZI4BRC9AJD48 | Yes | 1.56 |
| 16 | MDJLXOIQ9XTB | MDJLXOIQ9XTB | Yes | 2.2 |
| 17 | 5PX2ZBZ8HSX7 | 5PX2ZBZ8HSX7 | Yes | 2.21 |
| 18 | K18EVESA69UX | K18EVESA69UX | Yes | 3.97 |
| 19 | CCEX8I62C506 | CCEX8I62C506 | Yes | 3.64 |
| 20 | XGGXEUFA2IAR | XGGXEUFA2IAR | Yes | 3.79 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 4.33 |
| 2 | 65 | 65 | Yes | 2.22 |
| 3 | 44 | 44 | Yes | 2.67 |
| 4 | 4 | 4 | Yes | 2.19 |
| 5 | 20 | 20 | Yes | 13.26 |
| 6 | 67 | 67 | Yes | 2.13 |
| 7 | 19 | 19 | Yes | 3.71 |
| 8 | 793 | 793 | Yes | 1.74 |
| 9 | 7680 | 7680 | Yes | 2.07 |
| 10 | 39 | 39 | Yes | 3.63 |
| 11 | 60 | 60 | Yes | 2.89 |
| 12 | 26 | 26 | Yes | 5.38 |
| 13 | 64 | 64 | Yes | 5.39 |
| 14 | 3 | 3 | Yes | 3.35 |
| 15 | 5 | 5 | Yes | 8.78 |
| 16 | 5 | 50 | No | 8.53 |
| 17 | 28 | 28 | Yes | 2.58 |
| 18 | 3 | 3 | Yes | 2.33 |
| 19 | 73 | 73 | Yes | 2.09 |
| 20 | 31 | 31 | Yes | 1.99 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <_))<)__) | <_))<)__) | Yes | 9.03 |
| 2 | )___ (/() | )___ (/( ) | No | 4.65 |
| 3 | _<(_)( \  | _<(_)( \ ␣ | No | 6.32 |
| 4 | /_/____(< | /_/____(< | Yes | 4.27 |
| 5 | /(_/_///  | /(_/_/// | No | 17.09 |
| 6 |  \/_(()/_ | \/_(()/_ | No | 5.4 |
| 7 |  )( <( /( | _)(_<(_/( | Yes | 5.3 |
| 8 | ))_)<())) | ))_)<(()) | No | 4.15 |
| 9 | </ /() _) | < / /() _) | No | 5.16 |
| 10 |   /_<)_\( | /_<)_ \( | No | 6.13 |
| 11 | \ ( ()/(_ | \ ( ( ) / (_ | No | 8.85 |
| 12 | \ ()_(//) | \ ()_ (//) | No | 5.42 |
| 13 | \  /\ /(_ | \  /\ /(_ | Yes | 5.58 |
| 14 | (\ (( __( | (\ (( __ ( | No | 5.17 |
| 15 | (\__) <_< | (\__) <_< | Yes | 4.36 |
| 16 | /  <)() / | /  <)()( ␣/ | No | 6.18 |
| 17 | ((   )< ) | ((   ) < ) | No | 3.32 |
| 18 |   _)_()(< | _)_()(< | No | 4.75 |
| 19 | )<<) / << | )<<) / << | Yes | 8.16 |
| 20 | \ /)  _\< | \ /)  _\< | Yes | 5.38 |
