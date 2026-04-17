# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-27 10:12:23

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
| sudoku_game | 6701 | 36747 | 43448 | 10 | 10 | 36.22 | 724.39 |
| add_numbers | 4080 | 3366 | 7446 | 20 | 0 | 5.49 | 109.77 |
| counting_zeros | 5400 | 18964 | 24364 | 1 | 19 | 12.52 | 250.47 |
| task_decoding | 5400 | 6761 | 12161 | 19 | 1 | 5.61 | 112.24 |
| task_summation | 5460 | 12907 | 18367 | 20 | 0 | 10.48 | 209.64 |
| task_transcription | 4236 | 2753 | 6989 | 20 | 0 | 4.69 | 93.84 |
| task_sequences | 4140 | 7814 | 11954 | 18 | 2 | 7.55 | 150.94 |
| string_entry | 4623 | 4347 | 8970 | 11 | 9 | 5.85 | 116.93 |
| **TOTAL** | **40040** | **93659** | **133699** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 3 6 4 1 3 6 3 1 2 4 2 3 1 | 2 3 6 4 1 3 6 3 1 2 4 2 3 1 | Yes | 27.2 |
| 2 | 6 3 5 6 6 1 5 4 4 1 2 2 6 2 | 6 3 5 6 6 1 5 4 4 1 2 2 6 2 | Yes | 22.23 |
| 3 | 5 4 5 2 3 1 4 1 5 4 3 4 1 2 | 5 4 5 2 3 1 4 1 5 4 3 4 1 2 | Yes | 22.13 |
| 4 | 6 3 5 2 1 2 5 5 3 2 1 1 5 1 | 6 3 5 2 2 1 5 5 3 1 2 1 5 1 | No | 25.14 |
| 5 | 2 1 4 4 6 1 3 1 5 6 3 4 6 1 | Looking at this 6×6 | No | 33.24 |
| 6 | 4 3 6 6 3 6 2 5 3 5 6 2 5 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through each empty cell:  **Row 1:** 2 . . \| . 1 5 - Missing: 3, 4, 6 - Position 2: Must be 4 (from box and column constraints) - Position 3: Must be 3 (from box constraint) - Position 4: Must be 6 (remaining) - **Result: 2 4 3 6 1 5**  **Row 2:** 5 . 1 \| 4 . 2 - Missing: 3, 6 - Position 2: Must be 6 (column constraint) - Position 5: Must be 3 (column constraint) - **Result: 5 6 1 4 3 2**  **Row 4:** 4 1 . \| . . . - Missing: 2, 3, 5, 6 - Position 3: Must be 6 (box constraint) - Position 4: Must be 2 (column constraint) - Position 5: Must be 5 (column constraint) - Position 6: Must be 3 (remaining) - **Result: 4 1 6 2 5 3**  **Row 5:** 3 . 4 \| 1 2 . - Missing: 5, 6 - Position 2: Must be 5 (column constraint) - Position 6: Must be 6 (remaining) - **Result: 3 5 4 1 2 6**  **Row 6:** 6 . . \| . 4 1 - Missing: 2, 3, 5 - Position 2: Must be 2 (column constraint) - Position 3 | No | 28.85 |
| 7 | 2 4 4 2 1 2 3 1 4 5 6 6 3 2 | 2 4 4 2 1 2 3 1 4 5 6 6 3 2 | Yes | 35.92 |
| 8 | 6 3 3 1 4 2 2 6 2 6 5 6 3 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the empty cells in reading order:  **Row 1:** (1 4 2 5 _ _) - Missing: 3, 6 - C5 must be 6 (column 5 already has 1,3,4,5) - C6 must be 3  **Row 2:** (_ 6 _ _ _ 5) - C1: Column 1 needs 2,3; top-left box needs 3,5 → **3** - C3: Row needs 1,2,4; column 3 needs 1,5,6; box has 5 → **1** - C4: Row needs 2,4; column 4 needs 1,4,6 → **4** - C5: Must be **2**  **Row 3:** (_ 5 3 _ 1 4) - C1: Column 1 needs 2 → **2** - C4: Row needs 6 → **6**  **Row 4:** (5 _ _ 3 4 1) - C2: Row needs 2,6; column 2 needs 2,3 → **2** - C3: Must be **6**  **Row 5:** (4 1 _ 2 3 _) - C3: Row needs 5,6; column 3 needs 5 → **5** - C6: Must be **6**  **Row 6:** (6 _ 4 _ 5 2) - C2: Column 2 needs 3 | No | 28.43 |
| 9 | 2 3 2 5 2 4 3 1 2 6 5 6 4 3 | 2 3 2 5 2 4 3 1 2 6 5 6 4 3 | Yes | 28.93 |
| 10 | 1 4 6 3 2 1 4 6 3 3 1 5 3 6 | 1 4 6 3 2 1 4 6 3 3 1 5 3 6 | Yes | 26.73 |
| 11 | 2 4 1 2 3 1 4 1 6 2 4 6 4 3 | 2 1 4 2 3 1 4 6 1 2 4 4 6 3 | No | 20.92 |
| 12 | 3 4 6 2 3 2 3 4 5 6 5 1 5 3 | 3 6 3 4 2 2 3 4 5 6 5 1 3 5 | No | 31.6 |
| 13 | 2 5 3 4 2 3 1 1 5 6 4 5 2 3 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and boxes.  Let me work through the empty cells:  **Row 1:** 6 _ | No | 39.24 |
| 14 | 4 6 5 1 2 3 4 1 3 4 6 2 4 1 | 4 6 5 1 2 3 4 1 3 4 6 2 4 1 | Yes | 21.33 |
| 15 | 4 1 2 6 2 5 1 3 3 1 5 3 3 4 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the constraints:  **Row 3**: Has 1,2,6,5,4 → missing only 3 (position 1)  **Column 6**: Has 3,4,2,1,5 → missing only 6 (row 1, col 6)  **Row 4, Column 4**: Row needs 1,3; Column needs 1,5 → must be 1 **Row 4, Column 3**: Row now needs only 3 → must be 3  **Row 5, Column 4**: Column 4 now needs only 5 → must be 5 **Row 5, Column 5**: Row 5 now needs only 3 → must be 3  **Row 6, Column 5**: Column 5 needs 1,2,4; Row 6 needs 3,4 → must be 4 **Row 6, Column 2**: Row 6 now needs only 3 → must be 3  **Column 2**: Now has 6,1,5,2,3 → missing only 4 (row 1, col 2)  **Column 1**: Has 5,4,6,1 → missing 2,3 - Row 2, Col 1: Row needs 1,2,5; must be 2 - Row 3, Col 1: must be 3  **Column 5**: Now needs 1,2 - Row 2, Col 5: Row needs 1,5; must be 1 - Row 1, Col 5: must be 2  **Row 1, Column 3**: Row now needs only 1 → must be 1 **Row 2, Column | No | 30.14 |
| 16 | 5 6 2 5 1 6 5 3 4 5 1 3 2 3 | 5 6 2 5 1 6 5 3 4 5 1 3 2 3 | Yes | 23.23 |
| 17 | 2 1 4 4 5 6 3 3 5 4 4 6 4 5 | 2 1 4 4 5 6 3 3 5 4 6 4 6 4 5 | No | 115.74 |
| 18 | 1 4 5 6 6 3 5 4 2 5 2 1 2 5 | 1 4 5 6 6 3 5 4 2 5 2 1 2 5 | Yes | 24.61 |
| 19 | 3 1 4 3 1 6 3 4 4 5 1 3 6 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with easier cells:  **Row 1:** Has 4,1,6,2,5 → missing 3 at position (1,3)  **Row 2:** Has | No | 35.27 |
| 20 | 4 5 2 6 3 4 2 3 1 3 3 1 4 2 | 4 5 2 6 3 4 2 3 1 3 3 1 4 2 | Yes | 103.46 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1232 | 1232 | Yes | 3.24 |
| 2 | 1959 | 1959 | Yes | 4.25 |
| 3 | 1381 | 1381 | Yes | 4.07 |
| 4 | 1794 | 1794 | Yes | 4.06 |
| 5 | 1831 | 1831 | Yes | 24.18 |
| 6 | 2244 | 2244 | Yes | 4.05 |
| 7 | 1535 | 1535 | Yes | 3.32 |
| 8 | 1885 | 1885 | Yes | 7.19 |
| 9 | 1811 | 1811 | Yes | 3.69 |
| 10 | 1197 | 1197 | Yes | 3.65 |
| 11 | 1662 | 1662 | Yes | 3.32 |
| 12 | 2348 | 2348 | Yes | 4.04 |
| 13 | 1148 | 1148 | Yes | 4.0 |
| 14 | 982 | 982 | Yes | 3.16 |
| 15 | 1780 | 1780 | Yes | 2.94 |
| 16 | 1558 | 1558 | Yes | 3.67 |
| 17 | 2196 | 2196 | Yes | 15.79 |
| 18 | 2081 | 2081 | Yes | 3.44 |
| 19 | 1174 | 1174 | Yes | 3.62 |
| 20 | 1809 | 1809 | Yes | 4.07 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 | 58 | No | 12.85 |
| 2 | 63 | 64 | No | 14.48 |
| 3 | 47 | 42 | No | 11.18 |
| 4 | 42 | 42 | Yes | 9.69 |
| 5 | 45 | 44 | No | 7.65 |
| 6 | 46 | 36 | No | 8.61 |
| 7 | 47 | 43 | No | 30.06 |
| 8 | 48 | 49 | No | 9.75 |
| 9 | 60 | 56 | No | 10.05 |
| 10 | 75 | 74 | No | 19.35 |
| 11 | 70 | 61 | No | 15.01 |
| 12 | 65 | 61 | No | 11.41 |
| 13 | 75 | 74 | No | 11.91 |
| 14 | 61 | 46 | No | 10.34 |
| 15 | 64 | 58 | No | 13.96 |
| 16 | 46 | 39 | No | 10.04 |
| 17 | 52 | 47 | No | 12.49 |
| 18 | 37 | 35 | No | 9.9 |
| 19 | 61 | 53 | No | 9.51 |
| 20 | 61 | 58 | No | 12.2 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LKYHTPX | LKYHTPX | Yes | 4.37 |
| 2 | FZTONLC | FZTONLC | Yes | 6.54 |
| 3 | EJANZUI | EJANZUI | Yes | 5.9 |
| 4 | KTJVNZE | KTJVNZE | Yes | 5.24 |
| 5 | CBPUFDI | CBPUFDI | Yes | 8.46 |
| 6 | XOVJBFQ | XOVJBFQ | Yes | 3.77 |
| 7 | HDMAVGE | HDMAVGE | Yes | 5.05 |
| 8 | RLIWKGE | RLIWKGE | Yes | 6.18 |
| 9 | SBJMCWE | SBJMCWE | Yes | 4.97 |
| 10 | HMWBKNX | HMWBKNX | Yes | 5.43 |
| 11 | JKGFCEA | JKGFCEA | Yes | 5.54 |
| 12 | USRYNHK | USRYNHK | Yes | 4.88 |
| 13 | JBPEING | JBPEING | Yes | 5.98 |
| 14 | WRGNQLK | WRGNQLK | Yes | 4.93 |
| 15 | BWDECJK | BWDECKJ | No | 7.08 |
| 16 | CKRBNVZ | CKRBNVZ | Yes | 5.49 |
| 17 | SWFXERJ | SWFXERJ | Yes | 5.22 |
| 18 | RBZSDNT | RBZSDNT | Yes | 6.45 |
| 19 | IFCTZSU | IFCTZSU | Yes | 5.15 |
| 20 | NIFUQTD | NIFUQTD | Yes | 5.61 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.3, 9.7] | 9.7 0.3 | Yes | 24.47 |
| 2 | [1.3, 8.7] | 8.7 1.3 | Yes | 7.2 |
| 3 | [0.7, 9.3] | 0.7 9.3 | Yes | 5.96 |
| 4 | [3.6, 6.4] | 6.4 3.6 | Yes | 16.18 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.79 |
| 6 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.93 |
| 7 | [2.6, 7.4] | 7.4 2.6 | Yes | 7.19 |
| 8 | [3.3, 6.7] | 6.7 3.3 | Yes | 23.97 |
| 9 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.02 |
| 10 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.77 |
| 11 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.29 |
| 12 | [3.3, 6.7] | 6.7 3.3 | Yes | 18.95 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.9 |
| 14 | [3.5, 6.5] | 6.5 3.5 | Yes | 8.35 |
| 15 | [1.2, 8.8] | 8.8 1.2 | Yes | 8.26 |
| 16 | [0.6, 9.4] | 9.4 0.6 | Yes | 8.74 |
| 17 | [1.5, 8.5] | 1.5 8.5 | Yes | 7.19 |
| 18 | [4.2, 5.8] | 4.2 5.8 | Yes | 8.78 |
| 19 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.37 |
| 20 | [2.3, 7.7] | 2.3 7.7 | Yes | 7.31 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 8AHNN0CX6DKX | 8AHNN0CX6DKX | Yes | 3.06 |
| 2 | 2K605P57GR9Q | 2K605P57GR9Q | Yes | 3.47 |
| 3 | 87LU0IL7V1JP | 87LU0IL7V1JP | Yes | 3.12 |
| 4 | V3G88RM3AET7 | V3G88RM3AET7 | Yes | 13.4 |
| 5 | 7Y18VD8XU8R8 | 7Y18VD8XU8R8 | Yes | 3.45 |
| 6 | 0A6FTNM004E7 | 0A6FTNM004E7 | Yes | 3.31 |
| 7 | 8C4KY1QOU5H1 | 8C4KY1QOU5H1 | Yes | 4.28 |
| 8 | LCGGNMOQSKBK | LCGGNMOQSKBK | Yes | 3.27 |
| 9 | UIDGJHGDBDKU | UIDGJHGDBDKU | Yes | 3.54 |
| 10 | 3YVHTF0V2MVK | 3YVHTF0V2MVK | Yes | 3.65 |
| 11 | 6Y6SZ9NM8J3K | 6Y6SZ9NM8J3K | Yes | 4.22 |
| 12 | 7OBNAHL6GVMW | 7OBNAHL6GVMW | Yes | 3.9 |
| 13 | NC5XN11YAY89 | NC5XN11YAY89 | Yes | 3.35 |
| 14 | FRLOO58SL8ZY | FRLOO58SL8ZY | Yes | 4.92 |
| 15 | 2J2XFEHCCQ6F | 2J2XFEHCCQ6F | Yes | 5.41 |
| 16 | BHXBZ3UN4213 | BHXBZ3UN4213 | Yes | 4.22 |
| 17 | WYNH1E3U3U0R | WYNH1E3U3U0R | Yes | 12.86 |
| 18 | A2NTAWCLB1YY | A2NTAWCLB1YY | Yes | 3.38 |
| 19 | 473NGB1855PZ | 473NGB1855PZ | Yes | 3.81 |
| 20 | 234INDNECEZM | 234INDNECEZM | Yes | 3.21 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 18 | No | 12.4 |
| 2 | 3 | 3 | Yes | 16.97 |
| 3 | 20 | 21 | No | 11.0 |
| 4 | 44 | 44 | Yes | 5.34 |
| 5 | 4 | 4 | Yes | 4.74 |
| 6 | 39 | 39 | Yes | 5.46 |
| 7 | 73 | 73 | Yes | 5.63 |
| 8 | 36 | 36 | Yes | 4.12 |
| 9 | 7680 | 7680 | Yes | 9.11 |
| 10 | 5 | 5 | Yes | 7.8 |
| 11 | 60 | 60 | Yes | 5.73 |
| 12 | 26 | 26 | Yes | 10.86 |
| 13 | 64 | 64 | Yes | 5.36 |
| 14 | 67 | 67 | Yes | 3.75 |
| 15 | 9 | 9 | Yes | 6.07 |
| 16 | 7 | 7 | Yes | 4.31 |
| 17 | 1440 | 1440 | Yes | 15.69 |
| 18 | 23 | 23 | Yes | 4.99 |
| 19 | 48 | 48 | Yes | 6.72 |
| 20 | 793 | 793 | Yes | 4.9 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  <<\ _/() | <<\ _/() | No | 4.21 |
| 2 | (/(  _/ ) | (/(  _/ ) | Yes | 7.04 |
| 3 | \\< _)/ _ | \\< _)/ _ | Yes | 5.78 |
| 4 | _) )(_( < | _) )(_( | No | 5.33 |
| 5 | ))\\_) )/ | ))\\_) )/ | Yes | 12.9 |
| 6 | < (</)/ / | < (</)/ / | Yes | 5.52 |
| 7 | \_\(_ \)/ | \_\(_ \)/ | Yes | 4.74 |
| 8 | \) < \<<) | \) < \<<) | Yes | 3.37 |
| 9 | _)/__/ /_ | _)/__/ /_ | Yes | 9.79 |
| 10 | //()\/ (_ | //()\ (_ | No | 7.14 |
| 11 | (\(<_<< < | (\(<_<< | No | 4.03 |
| 12 | <<<<<)(<  | <<<<<)(< | No | 5.28 |
| 13 | < )/ < (< | < )/ < ( | No | 5.79 |
| 14 | /\)<\< \/ | /\)<\< \/ | Yes | 3.78 |
| 15 | \ (__< /\ | \ (__< /\ | Yes | 6.03 |
| 16 |  ((/ \</\ | ((/ \</\ | No | 6.22 |
| 17 |  (_///_)( | (_///_)( | No | 5.93 |
| 18 | /<\/(_<)) | /<\/(_<)) | Yes | 4.95 |
| 19 |  __<__(<\ | __<__(<\ | No | 4.75 |
| 20 | <))</\/ \ | <))</\/ \ | Yes | 4.34 |
