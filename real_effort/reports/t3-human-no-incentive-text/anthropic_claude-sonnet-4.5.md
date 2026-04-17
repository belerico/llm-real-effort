# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-27 10:13:45

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
| sudoku_game | 6158 | 34903 | 41061 | 7 | 13 | 39.85 | 797.05 |
| add_numbers | 3860 | 3458 | 7318 | 20 | 0 | 3.83 | 76.51 |
| counting_zeros | 5180 | 19779 | 24959 | 1 | 19 | 14.90 | 298.05 |
| task_decoding | 5180 | 6431 | 11611 | 19 | 1 | 6.09 | 121.84 |
| task_summation | 5240 | 13566 | 18806 | 20 | 0 | 11.14 | 222.8 |
| task_transcription | 4020 | 2685 | 6705 | 20 | 0 | 4.30 | 85.94 |
| task_sequences | 3920 | 7714 | 11634 | 17 | 3 | 7.61 | 152.21 |
| string_entry | 4388 | 4630 | 9018 | 10 | 10 | 5.48 | 109.63 |
| **TOTAL** | **37946** | **93166** | **131112** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 3 1 2 3 5 5 2 3 6 6 3 5 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the empty cells:  **Row 1:** . 2 1 \| . 6 . - Needs: 3, 4, 5 - R1C1: Column 1 needs 2,4,5; Box needs 3,4,5 → must be 4 or 5 - R1C4: Column 4 needs 3,5; Row needs 3,4,5 → must be 3 - R1C6: Row needs 4,5; Column 6 needs 3,5,6 → must be 5 - Therefore R1C1 = 4  **Row 2:** 6 . . \| . 5 4 - Needs: 1, 2, 3 - R2C2: Box needs 3,5; Row needs 1,2,3 → must be 3 - R2C3: Column 3 needs only 2 → must be 2 - R2C4: Must be 1  **Row 3:** 3 . 6 \| 4 1 2 - Only missing 5 at R3C2  **Row 4:** . 4 3 \| 6 2 1 - Column 1 needs 2,5; Row needs 5 → must be 5  **Row 5:** . . 5 \| 1 4 . - R5C1: Column 1 needs 2 → must be 2 - R5C2: Column 2 needs 6 → must be 6 - R5C6: Row needs 3 → must be 3  **Row 6:** 1 . 4 \| 2 . . - R6C2: Column 2 needs 3 → must be 3 - R6C5: Column 5 needs 3, but row needs 5,6... checking: Column 5 has 6,5,1,2,4, needs 3. But Row 6 needs 5,6,3. So R6C5 = 5 - R6C6: Must be 6  Missing numbers in | No | 28.74 |
| 2 | 1 2 2 3 2 5 6 6 4 1 6 1 2 3 | 1 2 2 3 2 5 6 6 4 1 6 1 2 3 | Yes | 19.63 |
| 3 | 1 5 3 5 5 3 5 6 3 4 1 3 6 2 | 5 1 3 5 5 3 6 4 5 3 1 3 2 6 | No | 24.08 |
| 4 | 1 4 6 1 5 1 5 4 3 5 5 4 3 2 | TIMEOUT | No | 120.02 |
| 5 | 4 2 3 3 4 6 6 4 5 1 6 3 4 1 | 4 2 3 3 4 6 6 4 5 1 6 3 4 1 | Yes | 26.57 |
| 6 | 6 3 4 4 3 1 4 6 4 1 4 1 5 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting grid: ``` 1 . 2 \| . . 5 . 2 5 \| 6 3 1 -----+----- . 5 . \| . . 2 5 3 . \| 2 . 6 -----+----- 6 1 3 \| 5 2 4 2 . 6 \| . . . ```  Let me solve step by step:  **Row 2**: Only missing 4 → position (2,1) = 4 **Column 1**: Now needs only 3 → position (3,1) = 3 **Column 6**: Needs only 3 → position (6,6) = 3 **Column 2**: Needs 4,6. Row 6 needs 1,4,5 → position (6,2) = 4 **Column 2**: Now needs only 6 → position (1,2) = 6 **Row 6**: Missing 1,5 in columns 4,5. Column 4 needs 1,3,4 → position (6,4) = 1 **Row 6**: Position (6,5) = 5 **Column 5**: Row 1 can have 3,4; column needs 1,4,6 → position (1,5) = 4 **Row 1**: Position (1,4) = 3 **Column 4**: Position ( | No | 29.11 |
| 7 | 6 2 4 1 4 2 6 1 1 5 2 2 4 3 | 2 6 4 | No | 95.93 |
| 8 | 6 3 6 1 5 1 3 2 5 6 3 4 1 4 | 6 3 6 1 5 3 1 2 5 6 3 4 1 4 | No | 111.12 |
| 9 | 3 1 6 5 2 1 3 1 2 4 1 3 4 2 |  | No | 29.82 |
| 10 | 5 4 3 4 2 6 3 2 1 5 1 2 6 3 | 5 4 3 4 2 6 3 2 1 5 1 2 6 3 | Yes | 19.85 |
| 11 | 4 5 3 2 1 3 2 4 6 5 1 5 6 2 | 4 5 3 2 1 3 2 4 6 5 1 5 6 2 | Yes | 20.6 |
| 12 | 3 1 5 2 4 5 2 2 3 4 6 6 2 1 | 3 1 5 2 4 5 2 2 3 4 6 6 2 1 | Yes | 26.19 |
| 13 | 3 6 1 6 3 3 6 4 3 1 3 5 1 4 | 6 3 1 3 3 6 3 4 1 3 5 1 4 | No | 24.31 |
| 14 | 5 6 4 6 2 2 6 5 2 6 5 4 6 3 | 5 6 4 6 2 2 6 5 2 6 5 4 6 3 | Yes | 21.28 |
| 15 | 6 2 4 3 5 3 2 1 3 5 3 5 1 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with the easier cells:  **Row 6:** 3 4 2 5 _ 6 → missing 1 → R6C5 = 1  **Row 5:** 5 6 _ 4 2 3 → missing 1 → R5C3 = 1  **Column 4:** 1 _ 6 _ 4 5 → missing 2, 3 **Row 4:** 2 1 6 _ _ 4 → missing 3, 5 Since R4 needs 3 and 5, and C4 needs 2 and 3: R4C4 = 3, R4C5 = 5  **Column 4 continued:** R2C4 = 2  **Column 5:** _ 6 4 5 2 1 → missing 3 → R1C5 = 3  **Row 2:** 4 5 _ 2 6 _ → missing 1, 3 → R2C3 = 3, R2C6 = 1  **Column 6:** _ 1 2 4 3 6 → missing 5 → R1C6 = 5  **Column 1:** _ 4 1 2 5 3 → missing 6 → R1C1 = 6  **Row 1:** 6 _ _ 1 3 5 → missing 2, 4 **Column 2:** _ 5 _ 1 6 4 → missing 2, 3 **Row 3:** 1 _ _ 6 4 2 → missing 3, 5  From the constraints: R1C2 = 2, R1C3 = 4, R3C2 | No | 27.16 |
| 16 | 3 4 6 5 1 2 3 5 2 6 5 6 3 5 |  | No | 29.98 |
| 17 | 5 3 6 1 5 3 4 2 3 1 5 4 3 1 | 5 3 6 1 5 3 1 4 6 2 3 1 3 4 3 1 | No | 19.39 |
| 18 | 3 6 1 2 5 1 4 4 5 4 3 3 6 2 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the missing values:  **Row 1:** 2 5 _ \| 6 4 1 → Missing: 3 → **Position (1,3) = 3**  **Row 4:** 6 2 _ \| 1 3 5 → Missing: 4 → **Position (4,3) = 4**  **Column 1:** 2,4,3,6,_,1 → Missing: 5 → **Position (5,1) = 5**  **Row 3:** 3 _ 5 \| _ 6 2 → Missing: 1,4 - Top-left box needs 1,6 in row 2 positions - Middle-left box needs 1 → **Position (3,2) = 1** - Column 4 at row 3 → **Position (3,4) = 4**  **Row 2:** 4 _ _ \| _ _ 3 → In top-left box, needs 6 - **Position (2,2) = 6** - **Position (2,3) = 1** - Top-right box needs 2,5 → **Position (2,4) = 2, Position | No | 28.51 |
| 19 | 5 6 3 3 1 4 3 6 3 1 3 1 5 2 | 6 3 5 3 3 4 5 1 6 3 1 4 1 3 5 2 | No | 26.3 |
| 20 | 5 3 2 6 1 5 3 6 3 4 1 5 4 6 | 5 3 2 6 1 5 3 6 3 4 1 5 4 6 | Yes | 68.44 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1742 | 1742 | Yes | 3.29 |
| 2 | 1572 | 1572 | Yes | 3.56 |
| 3 | 1972 | 1972 | Yes | 3.53 |
| 4 | 1155 | 1155 | Yes | 3.42 |
| 5 | 2293 | 2293 | Yes | 4.58 |
| 6 | 1666 | 1666 | Yes | 3.47 |
| 7 | 1988 | 1988 | Yes | 3.87 |
| 8 | 1680 | 1680 | Yes | 3.79 |
| 9 | 1655 | 1655 | Yes | 3.28 |
| 10 | 1550 | 1550 | Yes | 4.08 |
| 11 | 988 | 988 | Yes | 3.58 |
| 12 | 1509 | 1509 | Yes | 4.86 |
| 13 | 1997 | 1997 | Yes | 3.99 |
| 14 | 1556 | 1556 | Yes | 3.45 |
| 15 | 1836 | 1836 | Yes | 4.87 |
| 16 | 2317 | 2317 | Yes | 3.97 |
| 17 | 1892 | 1892 | Yes | 3.44 |
| 18 | 1361 | 1361 | Yes | 3.75 |
| 19 | 1079 | 1079 | Yes | 4.46 |
| 20 | 1220 | 1220 | Yes | 3.28 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 38 | 39 | No | 11.75 |
| 2 | 41 | 39 | No | 10.44 |
| 3 | 62 | 57 | No | 11.03 |
| 4 | 56 | 55 | No | 9.96 |
| 5 | 46 | 42 | No | 10.2 |
| 6 | 52 | 47 | No | 13.31 |
| 7 | 57 | 56 | No | 15.46 |
| 8 | 51 | 49 | No | 12.98 |
| 9 | 49 | 47 | No | 14.96 |
| 10 | 46 | 36 | No | 8.78 |
| 11 | 51 | 48 | No | 38.9 |
| 12 | 73 | 67 | No | 5.98 |
| 13 | 66 | 63 | No | 36.27 |
| 14 | 75 | 72 | No | 19.67 |
| 15 | 47 | 36 | No | 11.55 |
| 16 | 71 | 65 | No | 12.72 |
| 17 | 44 | 43 | No | 19.36 |
| 18 | 67 | 61 | No | 13.39 |
| 19 | 39 | 39 | Yes | 10.13 |
| 20 | 60 | 46 | No | 11.2 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WFTZDMV | WFTZDMV | Yes | 4.63 |
| 2 | CYQUEZG | CYQUEZG | Yes | 13.84 |
| 3 | SEYPANM | SEYPANM | Yes | 5.0 |
| 4 | GHVQZBR | GHVQZBR | Yes | 10.07 |
| 5 | TCVHGNI | TCVHGNI | Yes | 4.74 |
| 6 | DPVBCRA | DPVBCRA | Yes | 6.45 |
| 7 | XBKEACW | XBKEACW | Yes | 5.26 |
| 8 | PWVTBIO | PWVTBIO | Yes | 4.47 |
| 9 | UTKSGWP | UTKSGWP | Yes | 5.82 |
| 10 | FCSGEDV | FCSGEDV | Yes | 5.89 |
| 11 | CPDEXWL | CPDEXWL | Yes | 5.37 |
| 12 | VQCFUYX | VQCFUYX | Yes | 4.83 |
| 13 | CHEVZOB | CHEVZOB | Yes | 4.21 |
| 14 | QIUETAZ | QUIETAZ | No | 8.26 |
| 15 | QXLFPCO | QXLFPCO | Yes | 8.13 |
| 16 | MVQIBOD | MVQIBOD | Yes | 5.28 |
| 17 | EVDBINZ | EVDBINZ | Yes | 5.09 |
| 18 | DORFWUC | DORFWUC | Yes | 4.91 |
| 19 | TYNLCXB | TYNLCXB | Yes | 4.33 |
| 20 | TDSMXJO | TDSMXJO | Yes | 5.25 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.1, 9.9] | 0.1 9.9 | Yes | 6.82 |
| 2 | [1.2, 8.8] | 8.8 1.2 | Yes | 10.03 |
| 3 | [3.6, 6.4] | 3.6 6.4 | Yes | 37.34 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 10.7 |
| 5 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.86 |
| 6 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.4 |
| 7 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.41 |
| 8 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.99 |
| 9 | [4.8, 5.2] | 5.2 4.8 | Yes | 4.13 |
| 10 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.95 |
| 11 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.03 |
| 12 | [1.8, 8.2] | 1.8 8.2 | Yes | 14.28 |
| 13 | [0.1, 9.9] | 9.9 0.1 | Yes | 12.35 |
| 14 | [1.0, 9.0] | 1.0 9.0 | Yes | 8.59 |
| 15 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.03 |
| 16 | [3.2, 6.8] | 3.2 6.8 | Yes | 24.71 |
| 17 | [3.1, 6.9] | 3.1 6.9 | Yes | 6.55 |
| 18 | [4.1, 5.9] | 4.1 5.9 | Yes | 8.8 |
| 19 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.98 |
| 20 | [3.3, 6.7] | 6.7 3.3 | Yes | 13.85 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PKHU0BKYXBJ2 | PKHU0BKYXBJ2 | Yes | 3.37 |
| 2 | JNOUY5XYA3JO | JNOUY5XYA3JO | Yes | 3.57 |
| 3 | 9ZF14EO1GTD3 | 9ZF14EO1GTD3 | Yes | 15.92 |
| 4 | 4F4ZI4MLR7YH | 4F4ZI4MLR7YH | Yes | 3.74 |
| 5 | 8D2BBUO6KIL7 | 8D2BBUO6KIL7 | Yes | 3.93 |
| 6 | 2JX5SLJLDZNT | 2JX5SLJLDZNT | Yes | 3.24 |
| 7 | 7TFG3DP2U1OH | 7TFG3DP2U1OH | Yes | 3.15 |
| 8 | OF8WYPIII4Q0 | OF8WYPIII4Q0 | Yes | 3.65 |
| 9 | 4JUPZQRJLSUQ | 4JUPZQRJLSUQ | Yes | 3.49 |
| 10 | 5T9TZ46QILZV | 5T9TZ46QILZV | Yes | 4.07 |
| 11 | UU1IGTR7ENPQ | UU1IGTR7ENPQ | Yes | 3.05 |
| 12 | GJX4ONIQ5SZ2 | GJX4ONIQ5SZ2 | Yes | 5.46 |
| 13 | VAHSQH7Z23LQ | VAHSQH7Z23LQ | Yes | 2.64 |
| 14 | KARSF39O2NAG | KARSF39O2NAG | Yes | 2.9 |
| 15 | 4PK74UZQJGID | 4PK74UZQJGID | Yes | 3.65 |
| 16 | 1VRAGULGXVQD | 1VRAGULGXVQD | Yes | 3.53 |
| 17 | L1SCC97AQQD4 | L1SCC97AQQD4 | Yes | 3.32 |
| 18 | 10NGYRLI41H0 | 10NGYRLI41H0 | Yes | 5.55 |
| 19 | UFJ02ML1834N | UFJ02ML1834N | Yes | 2.97 |
| 20 | HZS0RZ98Y6I8 | HZS0RZ98Y6I8 | Yes | 4.74 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 4.24 |
| 2 | 5 | 18 | No | 13.07 |
| 3 | 23 | 23 | Yes | 6.03 |
| 4 | 3 | 5 | No | 16.3 |
| 5 | 9 | 9 | Yes | 5.3 |
| 6 | 73 | 73 | Yes | 5.69 |
| 7 | 36 | 36 | Yes | 3.63 |
| 8 | 65 | 65 | Yes | 5.8 |
| 9 | 7 | 7 | Yes | 5.87 |
| 10 | 60 | 60 | Yes | 5.63 |
| 11 | 7680 | 7680 | Yes | 6.68 |
| 12 | 4 | 4 | Yes | 7.5 |
| 13 | 60 | 60 | Yes | 4.72 |
| 14 | 48 | 48 | Yes | 5.46 |
| 15 | 9 | 9 | Yes | 16.16 |
| 16 | 4 | 4 | Yes | 4.74 |
| 17 | 793 | 793 | Yes | 4.6 |
| 18 | 19 | 19 | Yes | 4.23 |
| 19 | 1 | 1 | Yes | 6.88 |
| 20 | 20 | 22 | No | 19.66 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ) ()\(<(( | ) ()\<(( | No | 5.05 |
| 2 | <\)(< )<< | <\)(< )< | No | 4.3 |
| 3 | (/(///_)/ | (/(///_)/ | Yes | 6.5 |
| 4 | /) <_<< / | /) <_<< / | Yes | 4.96 |
| 5 |  _())/_// | _())/_// | No | 4.73 |
| 6 |  /)\( /(/ | /)\( /(/ | No | 5.17 |
| 7 | __)//_/<( | __)//_/<( | Yes | 5.62 |
| 8 | (\/(/\ _\ | (\/(/\ _\ | Yes | 4.03 |
| 9 | < ) <\((\ | < ) <\((\ | Yes | 6.21 |
| 10 | (_) /() / | (_) /() / | Yes | 6.2 |
| 11 | )/(/)/  \ | )/(/)/  \ | Yes | 5.06 |
| 12 | )\ \\)_\  | )\ \\)_\ | No | 8.36 |
| 13 | /_\ _ (\/ | /_\ _ (\/ | Yes | 4.33 |
| 14 | \<<\(/<(< | \<<\(/<( | No | 4.44 |
| 15 | )\()))/\  | )\()))/\ | No | 5.73 |
| 16 | /(/  (\_\ | /(/  (\_\ | Yes | 4.1 |
| 17 | \(<)<_</  | \(<)<_</ | No | 7.41 |
| 18 |   \((/_<< | \((/_< | No | 6.21 |
| 19 | /)()\<\ ( | /)()\<\ ( | Yes | 5.21 |
| 20 |  \/\//< _ | \/\//< _ | No | 6.01 |
