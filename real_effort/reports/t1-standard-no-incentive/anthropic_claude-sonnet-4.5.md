# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8380 | 33127 | 41507 | 4 | 16 | 25.60 | 512.21 |
| add_numbers | 4300 | 1771 | 6071 | 20 | 0 | 3.92 | 78.43 |
| counting_zeros | 7240 | 20267 | 27507 | 13 | 7 | 12.60 | 252.27 |
| task_decoding | 13680 | 9248 | 22928 | 19 | 1 | 7.89 | 157.96 |
| task_summation | 7600 | 13562 | 21162 | 20 | 0 | 9.63 | 192.7 |
| task_transcription | 4452 | 2986 | 7438 | 15 | 5 | 5.62 | 112.41 |
| task_sequences | 3560 | 7298 | 10858 | 19 | 1 | 6.31 | 126.07 |
| **TOTAL** | **49212** | **88259** | **137471** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 1 5 2 5 3 6 1 1 4 2 6 5 | 3 6 1 5 2 5 3 1 6 4 2 1 5 6 | No | 27.28 |
| 2 | 5 1 2 6 6 3 5 4 6 2 1 2 4 3 | 5 1 2 6 6 3 5 4 6 2 1 2 4 3 | Yes | 22.14 |
| 3 | 6 5 5 3 4 6 2 1 5 6 5 1 4 5 | 6 5 5 3 4 6 2 1 5 6 5 1 4 5 | Yes | 23.65 |
| 4 | 3 4 4 2 6 6 4 1 3 3 4 5 1 1 | 3 4 4 2 6 6 4 1 3 1 3 4 5 1 5 1 1 | No | 27.49 |
| 5 | 3 2 6 1 1 5 4 5 3 2 1 2 4 2 | 3 2 1 6 5 1 4 1 5 2 4 2 | No | 19.0 |
| 6 | 4 6 3 5 4 1 2 2 4 2 2 6 3 2 | 4 6 3 5 4 1 2 2 4 2 2 6 3 2 | Yes | 22.24 |
| 7 | 2 6 1 3 6 2 1 4 1 1 6 2 4 1 | 2 1 3 6 6 2 1 4 1 6 1 6 2 4 1 | No | 25.45 |
| 8 | 2 1 3 4 1 4 2 6 4 2 1 4 3 6 | 2 1 3 4 1 4 2 4 2 6 2 1 4 3 6 | No | 28.21 |
| 9 | 1 3 2 5 3 2 3 1 5 6 4 2 3 5 | 1 3 2 5 3 2 3 1 5 6 4 5 2 3 6 | No | 24.45 |
| 10 | 4 6 4 2 1 3 6 2 5 4 4 6 3 4 | 4 6 4 2 1 3 6 2 4 5 4 6 3 4 | No | 22.76 |
| 11 | 3 2 3 5 1 1 3 5 1 4 2 4 6 1 | 3 2 3 5 1 1 3 5 1 4 2 6 4 1 | No | 20.5 |
| 12 | 5 2 6 6 6 3 2 4 6 1 3 2 3 1 | 5 6 2 6 6 3 2 4 6 1 3 2 3 1 | No | 22.01 |
| 13 | 2 5 5 6 4 6 1 1 1 3 5 6 5 2 | 2 5 5 6 4 6 1 1 1 3 5 6 5 2 | Yes | 33.01 |
| 14 | 5 1 4 2 5 1 2 6 5 3 1 4 5 2 | 5 1 4 5 2 1 2 6 5 3 1 4 2 5 | No | 19.58 |
| 15 | 2 5 6 1 2 3 6 5 4 4 1 3 4 2 | Looking at the 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the puzzle:  **Row 1:** _ 4 3 6 1 5 → Missing 2 → **2** 4 3 6 1 5  **Column 4:** Complete (6,4,5,3,2,1)  **Column 6:** Has 5,_,4,1,3,6 → Missing 2 → Row 2, Col 6 = **2**  **Row 2:** _ _ _ 4 3 2 → Missing 1, 5, 6  **Column 2:** Has 4,_,3,2,_,5 → Missing 1, 6 (for rows 2 and 5)  **Row 5:** _ _ 6 2 5 3 → Missing 1, 4 Since Row 5 needs {1,4} and Col 2 needs {1,6}, R5C2 = **1**  Then R5C1 = **4** (only number left for row 5)  **Row 2, Col 2:** Must be **6** (Col 2 needs 1,6 and we placed 1)  **Row 2:** 5 6 1 4 3 2 → R2C1 = **5**, R2C3 = **1**  **Row 3:** 1 _ 2 5 6 4 → Missing 3 → R3C2 = **3**  **Row 4:** _ 2 _ 3 _ 1 → Missing 4, 5, 6 - Col 1 needs 3,6: R4C1 = **6** - Col 3 needs 4,5: R4C3 = **5** - R4C5 = **4**  **Row 6:** _ 5 _ 1 _ 6 → Missing 2, 3, 4 - | No | 32.15 |
| 16 | 1 6 5 4 2 6 4 1 5 3 3 5 5 3 | 1 6 5 4 2 6 4 1 5 3 3 5 5 3** | No | 28.32 |
| 17 | 6 5 4 5 1 6 3 5 4 6 3 6 4 1 | 5 6 4 6 1 5 3 5 4 6 3 6 4 1 | No | 28.91 |
| 18 | 3 6 4 1 3 5 4 1 4 3 6 5 2 4 | Looking at the 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with what's given: - Row 1: 2, 5, _, _, _, _ - Row 2: _, 1, _, _, 6, 2 - Row 3: 4, 6, _, 2, 5, 3 - Row 4: 5, _, 2, 1, 3, 6 - Row 5: 1, _, _, _, _, _ - Row 6: 6, 2, 4, 3, 1, 5 (complete)  Solving step by step:  Row 3 needs only 1 (position 3) Row 4 needs only 4 (position 2)  Column 1 needs 3 (position 2, row 2)  Row 2: 3, 1, _, _, 6, 2 needs 4 and 5 - From boxes and columns: position 3 = 5, position 4 = 4  Row 1: 2, 5, _, _, _, _ needs 1, 3, 4, 6 - Column 3 needs 3 or 6 → position 3 = 3 - Column 4 needs 5 or 6 → position 4 = 6   - Column 5 needs 2 or 4 → position 5 = 4 - Column 6 needs 1 or 4 → position 6 = 1  Row 5: 1, _, _, _, _, _ needs 2, 3, 4, 5, 6 - Position 2 = 3, position 3 = 6, position 4 = 5, position 5 = 2, position 6 = 4  Missing numbers in reading order: Row 1 | No | 29.13 |
| 19 | 5 1 6 6 6 5 4 3 1 2 3 1 3 2 | 5 1 6 6 4 5 3 1 2 3 1 3 2 | No | 28.48 |
| 20 | 5 2 1 3 6 6 4 3 5 6 5 3 4 4 | 5 6 1 3 2 2 4 6 3 5 6 5 3 4 4 | No | 27.25 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2152 | 2152 | Yes | 3.03 |
| 2 | 1037 | 1037 | Yes | 3.61 |
| 3 | 1477 | 1477 | Yes | 3.72 |
| 4 | 1156 | 1156 | Yes | 8.69 |
| 5 | 1293 | 1293 | Yes | 3.57 |
| 6 | 2006 | 2006 | Yes | 3.15 |
| 7 | 1891 | 1891 | Yes | 7.82 |
| 8 | 1664 | 1664 | Yes | 3.82 |
| 9 | 1973 | 1973 | Yes | 3.08 |
| 10 | 1857 | 1857 | Yes | 4.14 |
| 11 | 1357 | 1357 | Yes | 2.81 |
| 12 | 1283 | 1283 | Yes | 2.7 |
| 13 | 1783 | 1783 | Yes | 3.59 |
| 14 | 1788 | 1788 | Yes | 3.29 |
| 15 | 1767 | 1767 | Yes | 3.53 |
| 16 | 895 | 895 | Yes | 4.43 |
| 17 | 1783 | 1783 | Yes | 3.45 |
| 18 | 2302 | 2302 | Yes | 3.39 |
| 19 | 1461 | 1461 | Yes | 3.34 |
| 20 | 1714 | 1714 | Yes | 3.18 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 38 | 37 | No | 13.01 |
| 2 | 39 | 39 | Yes | 12.76 |
| 3 | 59 | 59 | Yes | 14.61 |
| 4 | 41 | 41 | Yes | 13.14 |
| 5 | 48 | 48 | Yes | 15.6 |
| 6 | 55 | 54 | No | 13.26 |
| 7 | 68 | 62 | No | 14.14 |
| 8 | 75 | 69 | No | 13.23 |
| 9 | 36 | 36 | Yes | 11.46 |
| 10 | 44 | 43 | No | 13.02 |
| 11 | 48 | 48 | Yes | 11.21 |
| 12 | 52 | 52 | Yes | 12.19 |
| 13 | 70 | 66 | No | 13.32 |
| 14 | 47 | 46 | No | 9.72 |
| 15 | 52 | 52 | Yes | 11.79 |
| 16 | 39 | 39 | Yes | 10.71 |
| 17 | 56 | 56 | Yes | 12.0 |
| 18 | 42 | 42 | Yes | 11.46 |
| 19 | 35 | 35 | Yes | 13.48 |
| 20 | 40 | 40 | Yes | 11.86 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YKGHVSE | YKGHVSE | Yes | 9.6 |
| 2 | AZLVMPN | AZLVMPN | Yes | 7.12 |
| 3 | QVRPLDI | QVRPLDI | Yes | 7.69 |
| 4 | SVEPYAO | SVEPYAO | Yes | 9.07 |
| 5 | BOIVJPR | BOIVJPR | Yes | 8.29 |
| 6 | LYHFZCS | LYHFZCS | Yes | 9.7 |
| 7 | PEKQJZF | PEKQJZF | Yes | 5.28 |
| 8 | WGQODLA | WGQODLA | Yes | 6.16 |
| 9 | AZIEOUG | AZIEOURG | No | 8.56 |
| 10 | FCXGANK | FCXGANK | Yes | 6.64 |
| 11 | YHPFEAL | YHPFEAL | Yes | 7.1 |
| 12 | ZUPOGCQ | ZUPOGCQ | Yes | 6.27 |
| 13 | DPQJBOS | DPQJBOS | Yes | 8.19 |
| 14 | REHKQIT | REHKQIT | Yes | 9.22 |
| 15 | TMDGOKU | TMDGOKU | Yes | 11.56 |
| 16 | LFBSYDT | LFBSYDT | Yes | 7.51 |
| 17 | DAJVLMR | DAJVLMR | Yes | 6.61 |
| 18 | FGXRSDN | FGXRSDN | Yes | 6.52 |
| 19 | HJCENGB | HJCENGB | Yes | 6.81 |
| 20 | IVUTOPD | IVUTOPD | Yes | 9.89 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 9.4 0.6 | Yes | 7.43 |
| 2 | [4.0, 6.0] | 4.0 6.0 | Yes | 11.84 |
| 3 | [4.2, 5.8] | 5.8 4.2 | Yes | 10.55 |
| 4 | [1.5, 8.5] | 1.5 8.5 | Yes | 7.95 |
| 5 | [2.1, 7.9] | 7.9 2.1 | Yes | 11.06 |
| 6 | [1.8, 8.2] | 8.2 1.8 | Yes | 12.39 |
| 7 | [0.8, 9.2] | 0.8 9.2 | Yes | 8.7 |
| 8 | [4.8, 5.2] | 5.2 4.8 | Yes | 10.69 |
| 9 | [2.2, 7.8] | 7.8 2.2 | Yes | 10.6 |
| 10 | [2.4, 7.6] | 7.6 2.4 | Yes | 9.24 |
| 11 | [4.3, 5.7] | 4.3 5.7 | Yes | 6.54 |
| 12 | [0.1, 9.9] | 9.9 0.1 | Yes | 7.96 |
| 13 | [2.7, 7.3] | 7.3 2.7 | Yes | 10.79 |
| 14 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.04 |
| 15 | [1.2, 8.8] | 8.8 1.2 | Yes | 8.96 |
| 16 | [4.4, 5.6] | 5.6 4.4 | Yes | 9.67 |
| 17 | [0.9, 9.1] | 9.1 0.9 | Yes | 10.22 |
| 18 | [1.4, 8.6] | 8.6 1.4 | Yes | 10.83 |
| 19 | [0.9, 9.1] | 0.9 9.1 | Yes | 10.61 |
| 20 | [4.1, 5.9] | 5.9 4.1 | Yes | 7.45 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AG9LOG69XWJG | AG9LOG69XWJG | Yes | 4.03 |
| 2 | DB89TQSB6UAD | DB89TQSB6UAD | Yes | 3.81 |
| 3 | O4RSOX9I3G01 | O4RSOX9I3G01 | Yes | 4.39 |
| 4 | 1HLGZBL6J0ZB | 1HLGZBL6J0ZB | Yes | 9.51 |
| 5 | HDZTRJH5XS8W | HDZTRJH5XS8W | Yes | 14.33 |
| 6 | OO60NWB29PJT | OO6ONWB29PJIT | No | 8.24 |
| 7 | 1MVL9PQ2RF6Q | 1MVL9PQ2RFfΩ | No | 4.83 |
| 8 | 62MEYUOX994R | 62MEYUOX994R | Yes | 4.35 |
| 9 | 1GSMKJN2BR46 | 1GSMKJN2BR46 | Yes | 3.78 |
| 10 | L9BCDGK5ICP0 | L9BCDGK5ICP0 | Yes | 8.45 |
| 11 | SVZH6TU0WENU | SVZH6TUOWENU | No | 4.16 |
| 12 | MOJIE2GLD7P1 | MOJIE2GLD7P1 | Yes | 6.95 |
| 13 | 28ABFACOFXXI | 28ABFACOFXXI | Yes | 5.07 |
| 14 | GB7C6LP28UJK | GB7C8LP28UJK | No | 4.74 |
| 15 | 2668FSZX40K1 | 2668FSZX40K1 | Yes | 4.39 |
| 16 | XXTOMNH818SM | XXTOMNH818SM | Yes | 3.65 |
| 17 | HTEZOF5C1Z4W | HTEZOF5C1Z4W | Yes | 4.0 |
| 18 | SANBQOI1KNPP | SANBOOI1KNPP | No | 4.7 |
| 19 | RPC7KBFXFM5L | RPC7KBFXFM5L | Yes | 4.72 |
| 20 | VZPR4CEX8Z0B | VZPR4CEX8Z0B | Yes | 4.22 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 243 | 243 | Yes | 4.71 |
| 2 | 65 | 65 | Yes | 5.73 |
| 3 | 7680 | 7680 | Yes | 5.96 |
| 4 | 63 | 63 | Yes | 5.43 |
| 5 | 20 | 21 | No | 10.96 |
| 6 | 4 | 4 | Yes | 4.74 |
| 7 | 5 | 5 | Yes | 7.25 |
| 8 | 28 | 28 | Yes | 6.86 |
| 9 | 1 | 1 | Yes | 6.96 |
| 10 | 60 | 60 | Yes | 5.44 |
| 11 | 3 | 3 | Yes | 10.65 |
| 12 | 6 | 6 | Yes | 5.98 |
| 13 | 7 | 7 | Yes | 5.75 |
| 14 | 39 | 39 | Yes | 9.81 |
| 15 | 16 | 16 | Yes | 5.68 |
| 16 | 44 | 44 | Yes | 5.84 |
| 17 | 19 | 19 | Yes | 4.61 |
| 18 | 31 | 31 | Yes | 3.82 |
| 19 | 36 | 36 | Yes | 3.78 |
| 20 | 10 | 10 | Yes | 6.14 |
