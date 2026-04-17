# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 8960 | 37503 | 46463 | 11 | 9 | 25.41 | 508.42 |
| add_numbers | 4880 | 4416 | 9296 | 20 | 0 | 5.14 | 102.85 |
| counting_zeros | 7820 | 34440 | 42260 | 15 | 5 | 18.77 | 375.8 |
| task_decoding | 14260 | 5188 | 19448 | 20 | 0 | 5.30 | 106.17 |
| task_summation | 8180 | 14909 | 23089 | 20 | 0 | 10.36 | 207.41 |
| task_transcription | 5028 | 4141 | 9169 | 20 | 0 | 4.40 | 88.09 |
| task_sequences | 4140 | 8072 | 12212 | 19 | 1 | 6.21 | 124.16 |
| **TOTAL** | **53268** | **108669** | **161937** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 5 5 2 6 5 5 3 4 1 3 6 2 4 | 6 5 5 2 6 5 5 3 4 1 3 6 2 4 | Yes | 26.8 |
| 2 | 4 1 5 4 2 4 2 3 4 2 6 1 6 5 | 4 1 5 4 2 4 2 3 4 2 6 1 6 5 | Yes | 21.81 |
| 3 | 3 6 6 2 1 4 6 1 4 5 4 4 3 1 | 3 6 6 2 1 4 6 1 4 5 4 4 3 1 | Yes | 25.57 |
| 4 | 1 3 3 6 5 5 1 1 4 4 6 2 5 4 | 3 1 5 6 3 1 5 1 4 4 6 2 5 4 | No | 26.52 |
| 5 | 6 2 5 3 2 1 6 5 6 6 5 1 4 2 |  | No | 27.28 |
| 6 | 4 1 1 6 5 2 1 4 6 1 4 5 2 1 |  | No | 28.04 |
| 7 | 4 5 6 4 2 5 6 5 6 5 3 3 1 4 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 3, 1, 6, _, 2, _ → needs 4, 5 **Row 2:** 5, _, 3, 2, 4, 1 → needs 6 **Row 3:** _, _, 1, _, _, 3 → needs 2, 4, 5, 6 **Row 4:** 1, 4, _, _, 3, 2 → needs 5, 6 **Row 5:** 2, _, 4, _, 1, 6 → needs 3, 5 **Row 6:** 6, _, 2, _, 5, _ → needs 1, 3, 4  Working through columns and boxes:  **Column 2:** Has 1, 4 → Row 2 gets 6, checking boxes: Row 5 gets 5, Row 6 gets 3, Row 3 gets 2  **Column 1:** Has 3, 5, 1, 2, 6 → Row 3 gets 4  **Column 4:** Has 2, 1 → Row 5 gets 3, Row 6 gets 4, Row 1 gets 5, Row 3 gets 5 (wait, checking again)  Let me verify with boxes: - Row 1: positions 4,6 need 4,5. Column 4 analysis → position 4 = 5, position 6 = 4 - Row 3: positions 4,5 need 5,6. Column 5 analysis → position 5 = 6, position 4 = 5 - Row 4: positions 3,4 need 5,6. Box constraint → position 3 = 5, position 4 = 6 - Row 6: position 6 needs 1  Missing numbers in reading order: Row 1: 5, 4 Row 2: 6 Row 3: | No | 32.38 |
| 8 | 4 1 5 4 6 1 4 3 6 1 2 3 2 1 | 4 1 5 4 6 1 4 3 6 1 2 3 2 1 | Yes | 24.76 |
| 9 | 6 2 4 4 5 6 1 3 6 4 5 4 2 3 | 6 2 4 4 5 6 1 3 6 4 5 4 2 3 | Yes | 25.68 |
| 10 | 2 3 1 6 2 3 4 2 5 1 3 5 1 6 | 2 3 1 6 2 3 4 2 5 1 3 5 1 6 | Yes | 22.17 |
| 11 | 5 2 6 4 6 3 2 4 3 4 2 1 5 1 |  | No | 23.34 |
| 12 | 2 4 6 1 4 1 6 3 5 2 1 2 5 4 | 2 4 6 1 4 1 6 3 5 2 1 2 5 4 | Yes | 25.7 |
| 13 | 5 4 1 6 2 1 3 6 5 1 5 2 5 1 | 5 4 1 6 2 1 3 6 5 1 5 2 5 1 | Yes | 29.16 |
| 14 | 1 2 6 3 3 5 1 2 1 1 5 5 4 3 |  | No | 27.71 |
| 15 | 4 2 1 2 6 4 1 5 5 1 6 4 6 5 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers systematically.  Let me work through the grid:  **Row 1:** Has 5,3,6 → needs 1,2,4 **Row 2:** Has 3,1,5 → needs 2,4,6 **Row 3:** Has 6,4,2,3 → needs 1,5 **Row 4:** Has 3,2 → needs 1,4,5,6 **Row 5:** Has 2,4,5,3,1 → needs 6 **Row 6:** Has 6,3,2,1,4 → needs 5  Working through columns and boxes:  **Column 3:** Has 3,1,4,5,2 → needs 6 → Row 4, Col 3 = 6 **Column 5:** Has 6,2,3,1 → needs 4,5 → Row 2, Col 5 = 4; Row 6, Col 5 = 5 **Column 6:** Has 5,3,2 → needs 1,4,6 → Row 1, Col 6 = 1; Row 5, Col 6 = 6  **Column 2:** Has 5,6,4,3 → needs 1,2 → Row 2, Col 2 = 2; Row 4, Col 2 = 1  **Row 2:** Now has 3,2,1,4,5 → Col 4 = 6  **Column 1:** Has 3,2,6 → needs 1,4,5 - Row 1, Col 1: needs {2,4} ∩ {1,4,5} = 4 - Row 3, Col 1: needs {1,5} ∩ {1,5} → checking box = 1 - Row 4, Col 1: = 5  **Column 4:** Remaining positions: - Row 1, Col 4 = 2 - Row 3, Col 4 = 5 - Row 4, Col 4 = 4  Reading missing numbers left to right, top to bottom: Row 1: 4, 2, 1 Row 2: 2, 6, 4 Row 3: 1, 5 | No | 25.64 |
| 16 | 5 3 2 5 6 6 4 5 5 3 4 1 1 3 | 5 3 2 5 6 6 4 5 5 3 4 1 1 3 | Yes | 19.37 |
| 17 | 2 3 6 1 4 6 5 3 4 1 5 3 3 5 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Row 3:** Has 5,4,2,_,1,6 → Missing 3 at position 4 **Row 5:** Has 6,5,1,4,_,2 → Missing 3 at position 5  **Column 6:** Has 3,6,_,2,1 → Needs 4,5 - Row 1, Col 6: Row 1 needs 1,2,3,4,6; Col 6 needs 4,5 → **4** - Row 4, Col 6: Row 4 needs 1,4,5; Col 6 needs 5 → **5**  **Row 6:** Has _,2,_,6,4,1 → Needs 3,5 - Col 1 needs 2,3,4; Row 6 needs 3,5 → Col 1 = **3** - Col 3 needs 5,6; Row 6 needs 5 → Col 3 = **5**  **Row 4:** Has _,_,3,2,6,5 → Needs 1,4 - Col 1 needs 2,4; Row 4 needs 1,4 → Col 1 = **4** - Col 2 then = **1**  **Row 1:** Has _,_,_,_,5,4 → Needs 1,2,3,6 - Col 1 needs 2 → **2** - Col 3 needs 6 → **6** - Col 4 needs 1,5; Row needs 1,3 → **1** - Col 2 = **3**  **Row 2:** Has 1,_,4,_,2,3 → Needs 5,6 - Col 2 needs 6 → **6** - Col 4 needs 5 → **5**  **Missing numbers in reading order:** Row 1: 2,3,6,1,4 \| Row 2: 6,5 \| Row 3: 3 \| Row 4: 4,1,5 \| Row 5: 3 \| Row | No | 27.12 |
| 18 | 5 3 4 6 2 5 4 1 3 5 2 3 6 1 |  | No | 25.97 |
| 19 | 4 5 1 1 5 3 1 5 3 4 5 6 4 5 | 4 5 1 1 5 3 1 5 3 4 5 6 4 5 | Yes | 23.19 |
| 20 | 2 3 5 2 4 1 2 5 5 6 2 4 3 5 | 2 3 5 2 4 1 2 5 5 6 2 4 3 5 | Yes | 20.0 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1444 | 1444 | Yes | 4.79 |
| 2 | 2733 | 2733 | Yes | 5.37 |
| 3 | 1368 | 1368 | Yes | 5.68 |
| 4 | 1336 | 1336 | Yes | 5.53 |
| 5 | 1159 | 1159 | Yes | 6.55 |
| 6 | 1766 | 1766 | Yes | 5.51 |
| 7 | 1926 | 1926 | Yes | 6.04 |
| 8 | 2031 | 2031 | Yes | 4.74 |
| 9 | 627 | 627 | Yes | 4.46 |
| 10 | 1749 | 1749 | Yes | 6.15 |
| 11 | 1869 | 1869 | Yes | 4.38 |
| 12 | 960 | 960 | Yes | 4.91 |
| 13 | 1883 | 1883 | Yes | 5.41 |
| 14 | 1047 | 1047 | Yes | 5.55 |
| 15 | 2460 | 2460 | Yes | 5.08 |
| 16 | 2380 | 2380 | Yes | 4.62 |
| 17 | 1095 | 1095 | Yes | 3.52 |
| 18 | 2015 | 2015 | Yes | 5.87 |
| 19 | 1143 | 1143 | Yes | 3.64 |
| 20 | 1094 | 1094 | Yes | 4.94 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 75 | 76 | No | 18.29 |
| 2 | 69 | 69 | Yes | 20.14 |
| 3 | 55 | 58 | No | 20.9 |
| 4 | 66 | 67 | No | 17.44 |
| 5 | 56 | 57 | No | 21.16 |
| 6 | 72 | 72 | Yes | 17.51 |
| 7 | 51 | 51 | Yes | 19.5 |
| 8 | 66 | 66 | Yes | 18.85 |
| 9 | 39 | 39 | Yes | 18.01 |
| 10 | 42 | 42 | Yes | 17.76 |
| 11 | 57 | 57 | Yes | 21.53 |
| 12 | 36 | 36 | Yes | 18.19 |
| 13 | 52 | 52 | Yes | 17.52 |
| 14 | 68 | 67 | No | 15.33 |
| 15 | 75 | 75 | Yes | 17.56 |
| 16 | 68 | 68 | Yes | 18.35 |
| 17 | 58 | 58 | Yes | 21.5 |
| 18 | 38 | 38 | Yes | 15.92 |
| 19 | 72 | 72 | Yes | 21.12 |
| 20 | 74 | 74 | Yes | 18.88 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KQRUSWV | KQRUSWV | Yes | 4.64 |
| 2 | QIARDGB | QIARDGB | Yes | 8.82 |
| 3 | CHMFAQE | CHMFAQE | Yes | 4.75 |
| 4 | EGYWBLX | EGYWBLX | Yes | 5.01 |
| 5 | HXVODKI | HXVODKI | Yes | 5.34 |
| 6 | JVGQKDR | JVGQKDR | Yes | 4.89 |
| 7 | JLXUEDI | JLXUEDI | Yes | 4.2 |
| 8 | SQYFPOG | SQYFPOG | Yes | 4.62 |
| 9 | WFRIAPZ | WFRIAPZ | Yes | 4.55 |
| 10 | QIEMKFC | QIEMKFC | Yes | 5.21 |
| 11 | ZIFUCLP | ZIFUCLP | Yes | 4.73 |
| 12 | MHBFELK | MHBFELK | Yes | 5.02 |
| 13 | ANHFULQ | ANHFULQ | Yes | 5.45 |
| 14 | FDMXIGO | FDMXIGO | Yes | 5.28 |
| 15 | EPGNIQX | EPGNIQX | Yes | 5.03 |
| 16 | VQKUGEL | VQKUGEL | Yes | 4.4 |
| 17 | UPNICRL | UPNICRL | Yes | 8.59 |
| 18 | ZKSFUPO | ZKSFUPO | Yes | 4.89 |
| 19 | XMRDZVQ | XMRDZVQ | Yes | 5.23 |
| 20 | UZQRKNJ | UZQRKNJ | Yes | 5.29 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.85 |
| 2 | [2.3, 7.7] | 7.7 2.3 | Yes | 10.13 |
| 3 | [2.7, 7.3] | 7.3 2.7 | Yes | 13.06 |
| 4 | [1.1, 8.9] | 8.9 1.1 | Yes | 10.61 |
| 5 | [3.6, 6.4] | 6.4 3.6 | Yes | 10.09 |
| 6 | [4.2, 5.8] | 4.2 5.8 | Yes | 12.17 |
| 7 | [1.5, 8.5] | 1.5 8.5 | Yes | 10.44 |
| 8 | [0.1, 9.9] | 9.9 0.1 | Yes | 10.18 |
| 9 | [0.6, 9.4] | 0.6 9.4 | Yes | 8.66 |
| 10 | [3.3, 6.7] | 6.7 3.3 | Yes | 13.61 |
| 11 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.14 |
| 12 | [0.9, 9.1] | 9.1 0.9 | Yes | 10.54 |
| 13 | [0.2, 9.8] | 9.8 0.2 | Yes | 9.87 |
| 14 | [2.0, 8.0] | 8.0 2.0 | Yes | 10.01 |
| 15 | [4.2, 5.8] | 4.2 5.8 | Yes | 10.48 |
| 16 | [0.1, 9.9] | 9.9 0.1 | Yes | 9.15 |
| 17 | [3.4, 6.6] | 3.4 6.6 | Yes | 10.08 |
| 18 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.86 |
| 19 | [4.5, 5.5] | 4.5 5.5 | Yes | 8.88 |
| 20 | [4.2, 5.8] | 5.8 4.2 | Yes | 12.4 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IF2E0313N2KK | IF2E0313N2KK | Yes | 4.56 |
| 2 | SKY4DXZFN5DA | SKY4DXZFN5DA | Yes | 4.31 |
| 3 | 28EMN4P1H2WP | 28EMN4P1H2WP | Yes | 4.22 |
| 4 | XQB8EG16LZLC | XQB8EG16LZLC | Yes | 4.08 |
| 5 | F6V3S389TUXN | F6V3S389TUXN | Yes | 6.43 |
| 6 | DNX6DPB4ZZRN | DNX6DPB4ZZRN | Yes | 4.63 |
| 7 | B3JPHDU277JG | B3JPHDU277JG | Yes | 3.82 |
| 8 | JL9GXGVN9V2B | JL9GXGVN9V2B | Yes | 4.13 |
| 9 | LF2TU9GP34SS | LF2TU9GP34SS | Yes | 4.44 |
| 10 | EM1MH03BMYWJ | EM1MH03BMYWJ | Yes | 6.55 |
| 11 | 5M60X3VPEJJG | 5M60X3VPEJJG | Yes | 4.53 |
| 12 | 04N8A9E53TIB | 04N8A9E53TIB | Yes | 4.23 |
| 13 | 9HPD1JEQO0SL | 9HPD1JEQO0SL | Yes | 4.55 |
| 14 | Z6VMU41B1M2B | Z6VMU41B1M2B | Yes | 4.19 |
| 15 | XI9TI5VD8ARU | XI9TI5VD8ARU | Yes | 3.48 |
| 16 | QVG2NN6ZHF8J | QVG2NN6ZHF8J | Yes | 3.95 |
| 17 | WO7CV036DCQH | WO7CV036DCQH | Yes | 4.54 |
| 18 | 5NZUXQ4QRU9Y | 5NZUXQ4QRU9Y | Yes | 3.68 |
| 19 | S2QUNPCZJ6NB | S2QUNPCZJ6NB | Yes | 3.51 |
| 20 | HCVLJFYNANM1 | HCVLJFYNANM1 | Yes | 4.14 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 20 | Yes | 13.63 |
| 2 | 23 | 23 | Yes | 4.4 |
| 3 | 28 | 28 | Yes | 5.65 |
| 4 | 9 | 9 | Yes | 4.65 |
| 5 | 67 | 67 | Yes | 3.28 |
| 6 | 4 | 4 | Yes | 4.6 |
| 7 | 3 | 3 | Yes | 13.21 |
| 8 | 198 | 198 | Yes | 6.0 |
| 9 | 60 | 60 | Yes | 4.42 |
| 10 | 10 | 10 | Yes | 7.5 |
| 11 | 36 | 36 | Yes | 2.73 |
| 12 | 1440 | 1440 | Yes | 5.13 |
| 13 | 63 | 63 | Yes | 4.06 |
| 14 | 48 | 48 | Yes | 3.77 |
| 15 | 793 | 793 | Yes | 4.21 |
| 16 | 6 | 6 | Yes | 5.6 |
| 17 | 39 | 39 | Yes | 5.06 |
| 18 | 4 | 4 | Yes | 6.54 |
| 19 | 5 | 14 | No | 14.71 |
| 20 | 73 | 73 | Yes | 4.99 |
