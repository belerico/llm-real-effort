# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-19 10:04:10

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
| sudoku_game | 8060 | 32837 | 40897 | 11 | 9 | 27.75 | 555.3 |
| add_numbers | 3980 | 1621 | 5601 | 20 | 0 | 4.08 | 81.68 |
| counting_zeros | 6920 | 20670 | 27590 | 8 | 12 | 15.11 | 302.42 |
| task_decoding | 13360 | 9492 | 22852 | 19 | 1 | 8.18 | 163.87 |
| task_summation | 7280 | 13225 | 20505 | 20 | 0 | 10.60 | 212.13 |
| task_transcription | 4124 | 2825 | 6949 | 17 | 3 | 4.58 | 91.61 |
| task_sequences | 3241 | 7871 | 11112 | 17 | 3 | 7.47 | 149.45 |
| **TOTAL** | **46965** | **88541** | **135506** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 4 2 6 1 4 5 1 4 5 1 1 6 | 2 4 1 2 6 1 4 5 1 4 5 1 1 6 | No | 16.66 |
| 2 | 1 2 6 4 2 3 6 4 2 6 3 2 5 6 | 1 2 6 4 2 3 6 4 2 6 3 2 5 6 | Yes | 23.84 |
| 3 | 4 5 3 6 2 4 6 3 3 6 1 1 6 5 | 4 5 3 6 2 4 6 3 3 6 1 1 6 5 | Yes | 26.93 |
| 4 | 5 6 5 5 1 6 2 4 3 5 1 3 6 3 | 5 6 5 5 1 6 2 4 3 5 1 3 6 3 | Yes | 31.46 |
| 5 | 1 4 6 5 3 3 6 5 2 4 6 4 5 2 | 1 4 6 5 3 3 6 5 2 4 6 4 5 2 | Yes | 19.16 |
| 6 | 3 1 5 4 1 6 6 5 3 1 3 6 4 6 | 3 1 5 4 1 6 6 5 3 1 3 6 4 6 | Yes | 30.3 |
| 7 | 1 4 6 3 5 6 2 4 2 1 5 3 5 1 | 1 4 6 3 5 6 2 4 2 1 4 5 3 5 1 | No | 23.8 |
| 8 | 3 5 1 4 3 2 1 5 2 3 4 4 5 2 | 3 5 1 3 2 4 1 5 2 4 3 2 4 5 | No | 25.29 |
| 9 | 1 6 2 5 3 4 4 5 3 4 5 1 6 5 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the puzzle:  **Row 1:** 3 _ _ 4 _ _ - Needs: 1, 2, 5, 6 - Column 2 analysis: needs 1 or 4; Row 1 needs 1, so position (1,2) = 1 - Working through constraints: 3 **1** **5** 4 **2** **6**  **Row 2:** 5 6 _ 2 _ 1 - Needs: 3, 4 - Position (2,3) from box constraint = 3 - Position (2,5) = 4 - Result: 5 6 **3** 2 **4** 1  **Row 3:** _ 2 1 _ 6 _ - Column 1 needs only 4 for this row - Position (3,4) = 5 (from column) - Position (3,6) = 3 - Result: **4** 2 1 **5** 6 **3**  **Row 4:** 1 _ _ 6 3 2 - Needs: 4, 5 - Position (4,2) = 4, Position (4,3) = 5 - Result: 1 **4** **5** 6 3 2  **Row 5:** 2 | No | 33.72 |
| 10 | 6 6 2 3 5 3 1 5 6 1 5 4 4 2 | 6 6 5 2 5 3 1 5 6 1 5 4 4 2 | No | 23.74 |
| 11 | 2 4 6 3 5 6 3 2 6 4 3 5 1 5 | 2 4 6 3 5 6 3 2 6 4 3 5 1 5 | Yes | 28.39 |
| 12 | 2 6 3 6 4 2 5 4 2 6 1 2 4 2 | 2 6 3 6 4 2 5 4 2 6 1 2 4 2 | Yes | 36.0 |
| 13 | 4 2 1 5 6 3 2 6 5 3 6 5 4 2 | 4 2 1 5 6 3 2 6 5 3 6 5 4 2 | Yes | 24.62 |
| 14 | 5 1 6 2 1 4 5 2 5 6 6 4 6 2 |  | No | 33.89 |
| 15 | 2 3 6 1 6 2 5 6 6 5 2 1 3 5 | Looking at the 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with the given numbers: - Row 1: _ _ _ 1 5 4 - Row 2: _ _ 4 5 _ 3 - Row 3: _ 4 2 3 1 _ - Row 4: 3 1 5 4 6 2 (complete) - Row 5: _ _ 3 2 4 1 - Row 6: 4 _ _ 6 _ _  Let me solve step by step:  **Row 3:** Needs 5, 6. Column 6 needs 5, 6. Column 1 needs 1, 2, 5, 6. - Row 3, Col 6: Looking at the bottom-right box and constraints → 6 - Row 3, Col 1: Must be 5  **Row 6:** With Row 3, Col 6 = 6, then Row 6, Col 6 = 5 - Row 6 needs: 1, 2, 5. Position 6 = 5 - Positions 2, 3 need 1, 2 → checking columns: Col 2 needs 2, so Row 6, Col 2 = 2 - Row 6, Col 3 = 1 - Row 6, Col 5 = 3  **Row 2:** Col 5 needs 2, 3. Row 2 needs 1, 2, 6 → Row 2, Col 5 = 2 - Positions 1, 2 need 1, 6 → Col 1 needs 1, 6; Col 2 needs 6 - Row 2, Col 1 = 1, Row 2, Col 2 = 6  **Row 5:** Needs 5, 6 in positions | No | 35.34 |
| 16 | 5 1 6 1 3 5 4 1 4 6 6 4 5 3 | 5 1 6 1 5 3 4 1 4 6 6 4 3 5 | No | 31.59 |
| 17 | 1 6 1 3 5 1 6 2 1 3 2 5 4 1 | 1 6 1 3 5 1 6 2 1 3 2 5 4 1 | Yes | 21.8 |
| 18 | 3 4 5 1 4 4 2 3 1 2 4 5 3 3 | 3 4 5 1 4 4 2 3 1 2 4 5 3 3 | Yes | 21.47 |
| 19 | 2 3 1 5 6 2 3 5 2 4 6 2 5 2 | 2 3 1 5 6 2 3 5 2 4 6 2 5 2 | Yes | 28.04 |
| 20 | 4 6 1 4 2 4 3 1 6 4 2 6 4 5 |  | No | 39.01 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1477 | 1477 | Yes | 3.5 |
| 2 | 1408 | 1408 | Yes | 2.88 |
| 3 | 1138 | 1138 | Yes | 4.44 |
| 4 | 1661 | 1661 | Yes | 5.38 |
| 5 | 1660 | 1660 | Yes | 3.8 |
| 6 | 2476 | 2476 | Yes | 3.35 |
| 7 | 2012 | 2012 | Yes | 2.99 |
| 8 | 2001 | 2001 | Yes | 5.7 |
| 9 | 2045 | 2045 | Yes | 2.55 |
| 10 | 1423 | 1423 | Yes | 3.0 |
| 11 | 1152 | 1152 | Yes | 2.84 |
| 12 | 902 | 902 | Yes | 4.79 |
| 13 | 1541 | 1541 | Yes | 3.32 |
| 14 | 1506 | 1506 | Yes | 4.23 |
| 15 | 809 | 809 | Yes | 5.88 |
| 16 | 1807 | 1807 | Yes | 3.26 |
| 17 | 2191 | 2191 | Yes | 4.14 |
| 18 | 2417 | 2417 | Yes | 2.86 |
| 19 | 2072 | 2072 | Yes | 4.04 |
| 20 | 1899 | 1899 | Yes | 8.62 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 | 36 | No | 16.81 |
| 2 | 35 | 35 | Yes | 9.62 |
| 3 | 44 | 44 | Yes | 16.65 |
| 4 | 47 | 47 | Yes | 13.06 |
| 5 | 64 | 64 | Yes | 15.84 |
| 6 | 70 | 69 | No | 13.96 |
| 7 | 62 | 61 | No | 16.34 |
| 8 | 37 | 37 | Yes | 12.67 |
| 9 | 70 | 63 | No | 20.94 |
| 10 | 66 | 54 | No | 17.28 |
| 11 | 55 | 56 | No | 18.98 |
| 12 | 71 | 63 | No | 17.23 |
| 13 | 39 | 40 | No | 13.03 |
| 14 | 39 | 39 | Yes | 14.39 |
| 15 | 43 | 43 | Yes | 13.33 |
| 16 | 49 | 49 | Yes | 10.81 |
| 17 | 51 | 50 | No | 15.85 |
| 18 | 48 | 46 | No | 12.07 |
| 19 | 49 | 48 | No | 13.66 |
| 20 | 54 | 52 | No | 19.6 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KZBTFSO | KZBTFSO | Yes | 9.32 |
| 2 | OKPUAIC | OKPUAIC | Yes | 6.88 |
| 3 | BTHWFDS | BTHWFDS | Yes | 6.35 |
| 4 | MZJEKOR | MZJEKOR | Yes | 7.84 |
| 5 | ORHQUFP | ORHQUFP | Yes | 9.41 |
| 6 | OQDUVWX | OQDUVWX | Yes | 8.02 |
| 7 | JRCFHPK | JRCFHPK | Yes | 8.48 |
| 8 | CSBAKLU | CSBAKLU | Yes | 11.11 |
| 9 | HVUERBQ | HVUERBQ | Yes | 8.28 |
| 10 | CMIOTAE | CMIOTAE | Yes | 10.31 |
| 11 | TXGJQLB | TXGJQLB | Yes | 9.22 |
| 12 | ANRBLHY | ANRBLHY | Yes | 7.39 |
| 13 | DNKLVJS | DNKLVJS | Yes | 6.88 |
| 14 | TAPVDHX | TAPVDHX | Yes | 6.01 |
| 15 | GIBUCWP | GIBUCWP | Yes | 6.94 |
| 16 | JNCASMY | JNCASMY | Yes | 5.65 |
| 17 | MBKCSFR | MBKCSRF | No | 10.48 |
| 18 | NWXQYHL | NWXQYHL | Yes | 7.94 |
| 19 | BOUPSDL | BOUPSDL | Yes | 8.24 |
| 20 | JNBCTZO | JNBCTZO | Yes | 8.93 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 0.6 9.4 | Yes | 12.07 |
| 2 | [1.1, 8.9] | 8.9 1.1 | Yes | 8.41 |
| 3 | [1.0, 9.0] | 9.0 1.0 | Yes | 11.76 |
| 4 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.04 |
| 5 | [3.3, 6.7] | 3.3 6.7 | Yes | 10.36 |
| 6 | [0.4, 9.6] | 9.6 0.4 | Yes | 11.97 |
| 7 | [4.0, 6.0] | 6.0 4.0 | Yes | 18.69 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 12.06 |
| 9 | [2.4, 7.6] | 7.6 2.4 | Yes | 11.07 |
| 10 | [2.8, 7.2] | 7.2 2.8 | Yes | 10.56 |
| 11 | [4.7, 5.3] | 4.7 5.3 | Yes | 9.08 |
| 12 | [3.1, 6.9] | 3.1 6.9 | Yes | 11.55 |
| 13 | [0.8, 9.2] | 9.2 0.8 | Yes | 9.23 |
| 14 | [0.2, 9.8] | 9.8 0.2 | Yes | 11.56 |
| 15 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.48 |
| 16 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.54 |
| 17 | [4.9, 5.1] | 4.9 5.1 | Yes | 10.0 |
| 18 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.81 |
| 19 | [0.2, 9.8] | 9.8 0.2 | Yes | 7.49 |
| 20 | [2.2, 7.8] | 7.8 2.2 | Yes | 11.2 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | T6W8GF1K1HIR | T6W8GF1K1HIR | Yes | 4.2 |
| 2 | R3DK8ICSZBHP | R3DK8ICSZBHP | Yes | 4.7 |
| 3 | 7RMSG2R0OTV2 | 7RMSG2ROOTV2 | No | 3.66 |
| 4 | PK4LCC1U2UUO | PK4LCC1U2UUO | Yes | 4.03 |
| 5 | KJOXI38L9RC3 | KJOXI38L9RC3 | Yes | 7.71 |
| 6 | RXAEL6FH2KT6 | RXAEL6FH2KT6 | Yes | 3.99 |
| 7 | DFXYCE6285TW | DFXYCE6285TW | Yes | 4.41 |
| 8 | AE3X54THIKUJ | AE3X54THIKUJ | Yes | 4.79 |
| 9 | EQRT0QQWY5KY | EQRTOQQWY5KY | No | 5.03 |
| 10 | 0OW7MNPVMOD8 | 00W7MNPVMOD8 | No | 3.94 |
| 11 | H9A57KAI8XOD | H9A57KAI8XOD | Yes | 4.52 |
| 12 | 1VZ2N7GNQL93 | 1VZ2N7GNQL93 | Yes | 4.76 |
| 13 | DC18HY1ONNZG | DC18HY1ONNZG | Yes | 4.86 |
| 14 | 7N6FGOCI16DY | 7N6FGOCI16DY | Yes | 3.65 |
| 15 | QS7ZABNX2RVE | QS7ZABNX2RVE | Yes | 4.47 |
| 16 | XH9NL284W7WG | XH9NL284W7WG | Yes | 4.35 |
| 17 | S8SHZSJ6GW1S | S8SHZSJ6GW1S | Yes | 4.5 |
| 18 | PNKHV2YK0YD8 | PNKHV2YK0YD8 | Yes | 5.33 |
| 19 | KCT46QABG7XP | KCT46QABG7XP | Yes | 4.27 |
| 20 | LKST312D6B0Z | LKST312D6B0Z | Yes | 4.35 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 7.83 |
| 2 | 16 | 16 | Yes | 5.59 |
| 3 | 9 | 9 | Yes | 6.16 |
| 4 | 793 | 793 | Yes | 5.0 |
| 5 | 60 | 60 | Yes | 5.49 |
| 6 | 48 | 48 | Yes | 3.93 |
| 7 | 7680 | 7680 | Yes | 5.84 |
| 8 | 4 | 4 | Yes | 4.64 |
| 9 | 31 | 31 | Yes | 4.72 |
| 10 | 3 | 3 | Yes | 8.62 |
| 11 | 10 | 10 | Yes | 6.45 |
| 12 | 73 | 73 | Yes | 4.71 |
| 13 | 64 | 64 | Yes | 5.32 |
| 14 | 1440 | 1440 | Yes | 6.75 |
| 15 | 3 | 5 | No | 12.65 |
| 16 | 5 | 2 | No | 16.42 |
| 17 | 198 | 198 | Yes | 9.24 |
| 18 | 19 | 19 | Yes | 3.82 |
| 19 | 26 | 26 | Yes | 14.75 |
| 20 | 4096 | 1048576 | No | 11.52 |
