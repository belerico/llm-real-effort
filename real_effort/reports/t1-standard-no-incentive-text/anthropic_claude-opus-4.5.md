# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-27 10:15:28

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
| sudoku_game | 6126 | 39267 | 45393 | 10 | 10 | 33.93 | 678.66 |
| add_numbers | 3500 | 1459 | 4959 | 20 | 0 | 3.61 | 72.19 |
| counting_zeros | 4820 | 23975 | 28795 | 15 | 5 | 18.11 | 362.2 |
| task_decoding | 4820 | 5644 | 10464 | 20 | 0 | 6.16 | 123.29 |
| task_summation | 4880 | 14778 | 19658 | 20 | 0 | 13.08 | 261.64 |
| task_transcription | 3663 | 2723 | 6386 | 20 | 0 | 5.95 | 119.04 |
| task_sequences | 3561 | 7992 | 11553 | 19 | 1 | 9.35 | 187.04 |
| string_entry | 4018 | 3955 | 7973 | 12 | 8 | 9.46 | 189.27 |
| **TOTAL** | **35388** | **99793** | **135181** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 5 4 4 6 5 2 3 1 3 4 1 5 |  | No | 39.98 |
| 2 | 1 2 3 2 2 4 5 3 3 5 6 2 6 3 | 1 2 3 2 2 4 5 3 3 5 6 2 6 3 | Yes | 36.43 |
| 3 | 4 1 5 6 5 5 2 4 5 3 6 4 2 6 |  | No | 36.15 |
| 4 | 3 4 1 2 6 3 6 5 2 5 4 1 2 5 | 3 4 1 2 6 3 6 5 2 5 4 1 2 5 | Yes | 29.81 |
| 5 | 1 4 2 5 2 6 3 2 3 6 6 6 4 5 |  | No | 28.0 |
| 6 | 6 5 2 3 5 5 1 3 2 4 3 5 5 3 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 4 . 1 \| 2 . 3 → Missing: 5, 6 - Column 5 has 6, so position (1,5) = 5 - Therefore position (1,2) = 6  **Row 2:** . . . \| 4 6 1 → Missing: 2, 3, 5 - Column 1 has 4,6,3,1 → position (2,1) = 2 or 5 - Column 3 has 1,6,2 → position (2,3) needs 3,4,5  **Row 3:** . . . \| 6 . 4 → Missing: 1, 2, 3, 5 - Column 1 has 4,6,3,1 → position (3,1) = 5 - Column 5 has 5,6,1,4,3 → position (3,5) = 2  **Row 4:** 6 2 . \| 1 . 5 → Missing: 3, 4 - Column 5 has 5,6,2,1,4 → position (4,5) = 3 - Therefore position (4,3) = 4  **Back to Row 3:** With (3,1)=5, need 1,3 in positions (3,2) and (3,3) - Column 3 needs 3,5 → position (3,3) = 3 - Therefore position (3,2) = 1  **Back to Row 2:**  - Column 1 now has 4,5,6,3,1 → position (2,1) = 2 - Column 3 now has 1,3,4,6,2 → position (2,3 | No | 34.75 |
| 7 | 4 6 5 1 3 6 3 4 6 2 3 4 1 1 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Row 1:** Has 3,1,2,5 → needs 4,6 - Column 5 has 2,1,3,5,6 → needs 4, so position (1,5) = 4 - Position (1,6) = 6  **Row 2:** Has 6,4,2 → needs 1,3,5 - Column 1 has 3,4,1,6,2 → needs 5, so position (2,1) = 5 - Column 3 needs 1,4,6; Row 2 needs 1,3 → intersection is 1, so position (2,3) = 1 - Position (2,6) = 3  **Row 3:** Has 4,2,1,5 → needs 3,6 - Column 3 now needs 4,6; Row 3 needs 3,6 → position (3,3) = 6 - Position (3,4) = 3  **Row 4:** Has 1,5,3 → needs 2,4,6 - Column 4 needs 1,6 (after placing 3); so position (4,4) = 6 - Column 2 needs 3,4; Row 4 needs 2,4 → position (4,2) = 4 - Position (4,6) = 2  **Row 5:** Has 6,2,5 → needs 1,3,4 - Column 2 now needs 3, so position (5,2) = 3 - Column 3 needs 4, so position (5,3) = 4 - Position (5,6) = 1  **Row 6:** Has 2,5,3,6, | No | 34.84 |
| 8 | 2 3 5 6 4 5 3 1 3 5 4 3 4 1 | 2 3 5 6 4 5 3 1 3 5 4 3 4 1 | Yes | 37.24 |
| 9 | 1 5 1 2 4 4 1 2 5 1 4 6 5 3 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers.  Let me work through the puzzle systematically:  **Row 1:** 2 4 3 \| 6 _ _ → Missing: 1, 5 - Column 5 analysis: has 3, 6, 4 → needs 1, 2, 5 - Column 6 analysis: has 2, 6 → needs 1, 3, 4, 5  **Row 3:** _ 3 _ \| 5 6 _ → Missing: 1, 2, 4 - Column 1: has 2, 5, 3, 6 → needs 1, 4 - Position (3,1): Checking box (rows 3-4, cols 1-3), has 3, 3, 5 → needs 1, 2, 4, 6 - Position (3,3): Column 3 needs 2, 4, 5, 6  **Row 4:** 3 5 _ \| _ _ 6 → Missing: 1, 2, 4 - Column 4: has 6, 4, 5, 3, 2 → | No | 40.28 |
| 10 | 3 6 5 2 1 5 2 1 6 3 5 5 2 3 | 3 6 5 2 1 5 2 1 6 3 5 5 2 3 | Yes | 38.39 |
| 11 | 2 1 3 2 5 3 1 3 5 4 6 3 4 2 | 2 1 3 2 5 3 1 3 5 4 6 3 4 2 | Yes | 29.93 |
| 12 | 4 2 6 5 4 1 2 6 4 3 5 2 6 3 | 4 2 6 5 4 1 2 6 4 3 5 2 6 3 | Yes | 34.22 |
| 13 | 3 2 5 3 4 2 2 1 1 3 4 6 3 5 | 3 2 5 3 4 2 2 1 1 3 4 6 3 5 | Yes | 31.33 |
| 14 | 5 6 6 4 2 5 4 6 5 4 1 6 5 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 2 3 _ 1 4 _ - Missing: 5, 6 - Column 3 analysis + Box 1 needs → position 3 = 5 - Position 6 = 6  **Row 2:** 1 _ _ _ 3 _ - Missing: 2, 4, 5, 6 - Column 2 has 3,5,2,4 → position 2 = 6 - Box 1 now needs 4 → position 3 = 4 - Column 4 needs 2,5,6; Box 2 needs 2,5 → position 4 = 2 - Position 6 = 5  **Row 3:** _ 5 3 _ 1 2 - Missing: 4, 6 - Column 1 has 2,1,3,5,6 → position 1 = 4 - Position 4 = 6  **Row 4:** 3 2 1 _ 6 _ - Missing: 4, 5 - Column 4 needs 5 → position 4 = 5 - Position 6 = 4  **Row 5:** 5 _ _ 4 2 3 - Missing: 1, 6 - Column 2 has 3,6,5,2,4 → position 2 = 1 - Position 3 = 6  **Row 6:** 6 | No | 29.94 |
| 15 | 2 3 1 1 6 4 5 4 3 6 4 2 6 4 | 2 3 1 1 6 4 5 4 3 6 4 2 6 4 | Yes | 31.11 |
| 16 | 3 4 6 6 5 2 1 2 3 1 4 3 1 1 | 3 4 6 6 5 2 1 2 3 1 4 3 1 1 | Yes | 36.73 |
| 17 | 3 1 2 5 4 6 2 3 1 2 4 4 6 3 |  | No | 41.5 |
| 18 | 5 6 4 2 1 2 6 5 2 1 3 6 3 1 | 5 6 4 2 1 2 6 5 2 1 3 6 3 1 | Yes | 23.34 |
| 19 | 2 1 5 4 6 3 2 5 2 3 1 3 4 1 |  | No | 27.51 |
| 20 | 5 2 6 4 2 5 3 6 4 2 1 1 5 4 |  | No | 37.13 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1628 | 1628 | Yes | 4.24 |
| 2 | 1334 | 1334 | Yes | 3.08 |
| 3 | 1943 | 1943 | Yes | 3.92 |
| 4 | 1103 | 1103 | Yes | 2.93 |
| 5 | 1910 | 1910 | Yes | 3.0 |
| 6 | 1025 | 1025 | Yes | 2.58 |
| 7 | 2659 | 2659 | Yes | 5.03 |
| 8 | 1568 | 1568 | Yes | 3.15 |
| 9 | 1867 | 1867 | Yes | 2.81 |
| 10 | 837 | 837 | Yes | 2.35 |
| 11 | 2255 | 2255 | Yes | 7.61 |
| 12 | 1643 | 1643 | Yes | 3.07 |
| 13 | 785 | 785 | Yes | 3.06 |
| 14 | 1581 | 1581 | Yes | 3.1 |
| 15 | 1210 | 1210 | Yes | 3.97 |
| 16 | 1332 | 1332 | Yes | 4.78 |
| 17 | 962 | 962 | Yes | 3.97 |
| 18 | 576 | 576 | Yes | 2.82 |
| 19 | 518 | 518 | Yes | 3.43 |
| 20 | 1573 | 1573 | Yes | 3.28 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 | 49 | Yes | 18.1 |
| 2 | 38 | 38 | Yes | 15.23 |
| 3 | 39 | 39 | Yes | 16.27 |
| 4 | 60 | 60 | Yes | 23.89 |
| 5 | 40 | 40 | Yes | 12.12 |
| 6 | 54 | 53 | No | 14.34 |
| 7 | 55 | 55 | Yes | 25.31 |
| 8 | 52 | 52 | Yes | 18.36 |
| 9 | 63 | 63 | Yes | 20.55 |
| 10 | 50 | 50 | Yes | 14.77 |
| 11 | 70 | 73 | No | 15.49 |
| 12 | 46 | 46 | Yes | 16.64 |
| 13 | 50 | 50 | Yes | 18.52 |
| 14 | 44 | 44 | Yes | 21.23 |
| 15 | 72 | 72 | Yes | 19.15 |
| 16 | 38 | 38 | Yes | 27.03 |
| 17 | 39 | 40 | No | 16.98 |
| 18 | 70 | 71 | No | 16.22 |
| 19 | 59 | 58 | No | 17.91 |
| 20 | 62 | 62 | Yes | 14.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LHJCOIZ | LHJCOIZ | Yes | 8.11 |
| 2 | BGRDZES | BGRDZES | Yes | 4.49 |
| 3 | DIYWXMZ | DIYWXMZ | Yes | 4.76 |
| 4 | KOEASZN | KOEASZN | Yes | 8.36 |
| 5 | EUGJAZI | EUGJAZI | Yes | 3.58 |
| 6 | FLYCAMK | FLYCAMK | Yes | 4.54 |
| 7 | YXSBNKC | YXSBNKC | Yes | 4.5 |
| 8 | BTYLSOR | BTYLSOR | Yes | 4.52 |
| 9 | DBLMNIO | DBLMNIO | Yes | 14.81 |
| 10 | NPSXEQH | NPSXEQH | Yes | 4.84 |
| 11 | LDPBJZN | LDPBJZN | Yes | 4.9 |
| 12 | FVYHWRL | FVYHWRL | Yes | 4.85 |
| 13 | KHIZLVG | KHIZLVG | Yes | 5.24 |
| 14 | EAVDTGI | EAVDTGI | Yes | 6.76 |
| 15 | IAZSVGL | IAZSVGL | Yes | 5.36 |
| 16 | LHBOQWI | LHBOQWI | Yes | 8.56 |
| 17 | AFCDBWX | AFCDBWX | Yes | 6.46 |
| 18 | HXQJLIC | HXQJLIC | Yes | 4.94 |
| 19 | BVFYTKA | BVFYTKA | Yes | 5.9 |
| 20 | TNLRKSJ | TNLRKSJ | Yes | 7.79 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.49 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.05 |
| 3 | [2.0, 8.0] | 8.0 2.0 | Yes | 8.77 |
| 4 | [1.3, 8.7] | 8.7 1.3 | Yes | 18.59 |
| 5 | [4.0, 6.0] | 6.0 4.0 | Yes | 9.96 |
| 6 | [1.4, 8.6] | 8.6 1.4 | Yes | 15.52 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 12.04 |
| 8 | [3.1, 6.9] | 3.1 6.9 | Yes | 18.08 |
| 9 | [2.7, 7.3] | 2.7 7.3 | Yes | 10.01 |
| 10 | [3.8, 6.2] | 6.2 3.8 | Yes | 11.44 |
| 11 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.26 |
| 12 | [4.6, 5.4] | 5.4 4.6 | Yes | 9.36 |
| 13 | [3.9, 6.1] | 6.1 3.9 | Yes | 19.16 |
| 14 | [1.4, 8.6] | 8.6 1.4 | Yes | 9.42 |
| 15 | [0.4, 9.6] | 9.6 0.4 | Yes | 9.3 |
| 16 | [4.3, 5.7] | 5.7 4.3 | Yes | 10.1 |
| 17 | [2.9, 7.1] | 7.1 2.9 | Yes | 17.62 |
| 18 | [2.4, 7.6] | 7.6 2.4 | Yes | 22.09 |
| 19 | [1.4, 8.6] | 1.4 8.6 | Yes | 11.81 |
| 20 | [4.2, 5.8] | 5.8 4.2 | Yes | 17.55 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 21OUG7U7FJFJ | 21OUG7U7FJFJ | Yes | 3.48 |
| 2 | FWVDRJSC4D91 | FWVDRJSC4D91 | Yes | 6.82 |
| 3 | 6IZR29DC4ZSZ | 6IZR29DC4ZSZ | Yes | 4.97 |
| 4 | IBY8ZAGO7EVY | IBY8ZAGO7EVY | Yes | 12.62 |
| 5 | 5BQN33PY5LAQ | 5BQN33PY5LAQ | Yes | 3.89 |
| 6 | K2OOU6X6DA8E | K2OOU6X6DA8E | Yes | 12.62 |
| 7 | GNRMDNQGBZG8 | GNRMDNQGBZG8 | Yes | 3.16 |
| 8 | APGEQ9GIN7RY | APGEQ9GIN7RY | Yes | 3.37 |
| 9 | YAEONK48G87Z | YAEONK48G87Z | Yes | 13.06 |
| 10 | T22GQ6WA1V2E | T22GQ6WA1V2E | Yes | 12.94 |
| 11 | SDTFTWBJZG7S | SDTFTWBJZG7S | Yes | 3.13 |
| 12 | P48ZGC1PP8Z9 | P48ZGC1PP8Z9 | Yes | 5.83 |
| 13 | VU5X9QISOLBO | VU5X9QISOLBO | Yes | 3.92 |
| 14 | KWV7P10QFT34 | KWV7P10QFT34 | Yes | 5.35 |
| 15 | Q8I0XGAOCLEK | Q8I0XGAOCLEK | Yes | 3.47 |
| 16 | YSPV7MOMR2EL | YSPV7MOMR2EL | Yes | 4.98 |
| 17 | WL23VL3LYQSK | WL23VL3LYQSK | Yes | 4.06 |
| 18 | P0MULU4W6PVI | P0MULU4W6PVI | Yes | 4.94 |
| 19 | TGO4HSR9NKWV | TGO4HSR9NKWV | Yes | 2.97 |
| 20 | ABYOD5BIKW3T | ABYOD5BIKW3T | Yes | 3.47 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 6.82 |
| 2 | 4 | 4 | Yes | 7.48 |
| 3 | 64 | 64 | Yes | 14.76 |
| 4 | 19 | 19 | Yes | 5.89 |
| 5 | 67 | 67 | Yes | 4.09 |
| 6 | 1 | 1 | Yes | 7.04 |
| 7 | 1440 | 1440 | Yes | 12.4 |
| 8 | 26 | 26 | Yes | 8.44 |
| 9 | 28 | 28 | Yes | 5.43 |
| 10 | 60 | 60 | Yes | 5.69 |
| 11 | 243 | 243 | Yes | 6.0 |
| 12 | 39 | 39 | Yes | 6.08 |
| 13 | 16 | 16 | Yes | 5.77 |
| 14 | 7 | 7 | Yes | 4.53 |
| 15 | 4096 | 4096 | Yes | 16.42 |
| 16 | 7680 | 7680 | Yes | 15.4 |
| 17 | 5 | 16 | No | 19.42 |
| 18 | 48 | 48 | Yes | 11.65 |
| 19 | 793 | 793 | Yes | 4.79 |
| 20 | 3 | 3 | Yes | 18.93 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /()\\/(_< | /()\\/(_ | No | 3.3 |
| 2 | / )//\/\) | / )//\/\) | Yes | 13.39 |
| 3 | \___(_()  | \___(_() | No | 4.22 |
| 4 | /_ (<\_\( | /_ (<\_\( | Yes | 6.42 |
| 5 | )(_/\)_)( | )(_/\)_)( | Yes | 13.35 |
| 6 | \ \/</_)  | \ \/</_) | No | 9.98 |
| 7 | \()()/\)/ | \()()/\)/ | Yes | 3.45 |
| 8 | < /()))_  | < /()))_ | No | 6.33 |
| 9 | /(<)_\\/  | /(<)_\\/ | No | 5.74 |
| 10 | /\/(( _)( | /\/(( _)( | Yes | 15.22 |
| 11 | (/)(_/) ) | (/)(_/) ) | Yes | 11.0 |
| 12 | </<__ \(_ | </<__ \(_ | Yes | 5.57 |
| 13 |  ___/<_\_ | ___/<_\_ | No | 11.0 |
| 14 | _/ /(\<_) | _/ /(\<_) | Yes | 4.47 |
| 15 |  _(_ (/ / | _(_ (/ / | No | 9.35 |
| 16 | /)_<\)<\< | /)_<\)<\ | No | 13.09 |
| 17 | _/<//) \_ | _/<//) \_ | Yes | 12.37 |
| 18 | < _ _(/_) | < _ _(/_) | Yes | 12.56 |
| 19 | _(\/\<<_) | _(\/\<<_) | Yes | 12.87 |
| 20 | /<)/< ( _ | /<)/< ( _ | Yes | 15.58 |
