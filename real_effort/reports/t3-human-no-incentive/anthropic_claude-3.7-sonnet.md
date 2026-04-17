# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 8740 | 28911 | 37651 | 2 | 18 | 21.28 | 425.77 |
| add_numbers | 4660 | 5033 | 9693 | 20 | 0 | 5.06 | 101.19 |
| counting_zeros | 7600 | 25733 | 33333 | 14 | 6 | 16.27 | 325.64 |
| task_decoding | 14040 | 7127 | 21167 | 17 | 3 | 5.79 | 115.95 |
| task_summation | 7960 | 24197 | 32157 | 20 | 0 | 15.61 | 312.44 |
| task_transcription | 4792 | 4855 | 9647 | 16 | 4 | 4.99 | 99.82 |
| task_sequences | 3921 | 18237 | 22158 | 14 | 6 | 13.09 | 261.8 |
| **TOTAL** | **51713** | **114093** | **165806** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 3 4 1 4 6 2 3 2 2 6 5 4 | 3 5 2 1 4 6 2 4 3 2 2 6 5 6 | No | 20.27 |
| 2 | 5 6 3 1 2 5 3 2 6 4 1 6 4 1 | 5 6 3 1 5 2 3 4 6 2 4 1 6 1 4 | No | 22.08 |
| 3 | 4 2 3 5 4 5 6 6 4 1 5 6 4 2 | 4 2 5 3 5 4 6 1 4 6 6 5 4 2 | No | 20.6 |
| 4 | 5 3 6 5 2 1 5 1 6 2 3 1 6 4 | 5 3 6 5 2 1 5 1 6 2 3 6 1 4 | No | 17.53 |
| 5 | 3 4 1 1 3 5 2 6 1 2 3 1 6 6 | 3 1 4 1 5 2 3 5 2 1 6 3 6 1 2 | No | 23.52 |
| 6 | 5 1 2 4 1 6 1 4 5 2 4 4 6 5 | 5 1 2 6 1 4 1 4 5 2 4 2 4 6 4 6 5 | No | 17.45 |
| 7 | 5 4 5 4 5 3 3 5 4 2 6 4 2 5 | 4 5 5 4 3 5 5 3 4 2 6 2 5 4 | No | 18.17 |
| 8 | 5 2 3 6 5 6 4 4 5 2 1 5 2 3 | 5 2 3 5 6 6 4 4 2 5 5 2 3 | No | 21.29 |
| 9 | 3 5 4 4 3 3 6 4 5 2 2 6 3 1 | 3 5 4 4 3 3 6 4 5 2 2 6 3 1 | Yes | 21.58 |
| 10 | 2 6 3 3 2 6 2 5 4 3 6 4 2 3 | 2 3 6 3 2 6 2 5 4 6 3 4 3 2 | No | 26.58 |
| 11 | 1 5 6 1 2 2 5 6 5 3 6 2 5 3 | 1 6 2 5 6 5 2 3 2 5 6 3 | No | 23.47 |
| 12 | 6 3 5 4 5 3 2 3 4 6 4 3 4 1 | 6 5 3 4 3 5 2 4 3 6 4 3 4 1 | No | 22.68 |
| 13 | 2 5 6 2 3 2 6 3 5 6 2 5 4 2 | 2 5 6 2 6 3 2 5 3 6 2 5 4 2 | No | 21.44 |
| 14 | 6 3 5 3 6 4 2 5 4 3 4 2 6 5 | 6 3 5 3 6 4 2 5 4 3 6 2 4 | No | 19.28 |
| 15 | 3 4 5 5 6 3 5 4 2 3 1 1 6 2 | I'll solve this 6×6 Sudoku puzzle by working through each empty cell methodically.  First, let me analyze what numbers are still needed in each row, column, and 2×3 box:  Starting with Row 1: - Missing numbers: 3, 4, 5 - The first cell (1,1) must be 3 (checking columns and boxes) - The fourth cell (1,4) must be 5 - The sixth cell (1,6) must be 4  Row 2: - Missing numbers: 3, 5, 6 - Cell (2,1) must be 5 - Cell (2,2) must be 6 - Cell (2,3) must be 3  Row 4: - Missing numbers: 4, 5 - Cell (4,5) must be 5 - Cell (4,6) must be 4  Row 5: - Missing numbers: 1, 2, 3 - Cell (5,1) must be 3 - Cell (5,4) must be 1 - Cell (5,5) must be 2  Row 6: - Missing numbers: 1, 2, 6 - Cell (6,1) must be 2 - Cell (6,4) must be 6 - Cell (6,6) must be 1  Reading the empty cells from left to right, top to bottom | No | 25.78 |
| 16 | 5 4 1 2 1 2 6 2 1 6 6 3 3 2 | 5 4 1 2 6 2 6 1 2 6 3 3 2 | No | 20.07 |
| 17 | 5 1 2 2 6 3 4 2 3 5 4 3 6 1 | 5 1 2 2 6 3 4 2 3 5 4 3 6 1 | Yes | 25.04 |
| 18 | 2 4 6 1 3 2 4 4 6 4 5 1 4 5 | 2 6 4 3 4 1 2 4 6 1 4 5 4 5 | No | 19.41 |
| 19 | 5 6 1 4 2 3 4 3 5 6 4 5 6 4 | 5 6 4 1 2 3 5 6 4 3 6 5 | No | 19.49 |
| 20 | 6 2 5 4 2 1 5 2 6 3 5 6 3 1 | 5 2 6 4 2 1 5 2 6 3 6 5 3 1 | No | 19.82 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1557 | 1557 | Yes | 4.97 |
| 2 | 1635 | 1635 | Yes | 5.71 |
| 3 | 2109 | 2109 | Yes | 3.4 |
| 4 | 832 | 832 | Yes | 5.24 |
| 5 | 1701 | 1701 | Yes | 5.8 |
| 6 | 1845 | 1845 | Yes | 5.01 |
| 7 | 1805 | 1805 | Yes | 6.6 |
| 8 | 1450 | 1450 | Yes | 4.95 |
| 9 | 1845 | 1845 | Yes | 4.54 |
| 10 | 1946 | 1946 | Yes | 4.0 |
| 11 | 1137 | 1137 | Yes | 3.91 |
| 12 | 2098 | 2098 | Yes | 9.4 |
| 13 | 899 | 899 | Yes | 4.45 |
| 14 | 1403 | 1403 | Yes | 4.34 |
| 15 | 1677 | 1677 | Yes | 5.91 |
| 16 | 1885 | 1885 | Yes | 4.02 |
| 17 | 966 | 966 | Yes | 4.18 |
| 18 | 1362 | 1362 | Yes | 3.54 |
| 19 | 2254 | 2254 | Yes | 6.17 |
| 20 | 1281 | 1281 | Yes | 4.98 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 50 | 50 | Yes | 18.57 |
| 2 | 49 | 49 | Yes | 16.42 |
| 3 | 47 | 47 | Yes | 20.21 |
| 4 | 56 | 58 | No | 14.28 |
| 5 | 47 | 47 | Yes | 11.17 |
| 6 | 53 | 53 | Yes | 15.14 |
| 7 | 68 | 67 | No | 12.07 |
| 8 | 66 | 66 | Yes | 15.27 |
| 9 | 53 | 53 | Yes | 18.83 |
| 10 | 63 | 62 | No | 15.86 |
| 11 | 38 | 38 | Yes | 14.45 |
| 12 | 55 | 54 | No | 17.97 |
| 13 | 41 | 41 | Yes | 18.47 |
| 14 | 50 | 50 | Yes | 16.95 |
| 15 | 41 | 41 | Yes | 22.12 |
| 16 | 51 | 51 | Yes | 14.45 |
| 17 | 57 | 57 | Yes | 19.0 |
| 18 | 75 | 73 | No | 10.37 |
| 19 | 44 | 44 | Yes | 17.41 |
| 20 | 69 | 68 | No | 16.31 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QDCTPWN | QDCTPWN | Yes | 4.98 |
| 2 | EQCJFPV | ESCAPE | No | 4.26 |
| 3 | TVOCKMB | TVOCKMB | Yes | 6.63 |
| 4 | CZSVTJO | CSVTJO | No | 5.86 |
| 5 | QGRYNSB | QGRYSB | No | 4.36 |
| 6 | FMTXALC | FMTXALC | Yes | 6.29 |
| 7 | NRQVPIJ | NRQVPIJ | Yes | 5.33 |
| 8 | RGZLOUI | RGZLOUI | Yes | 5.25 |
| 9 | KHOINUW | KHOINUW | Yes | 5.75 |
| 10 | ROMHFBV | ROMHFBV | Yes | 7.14 |
| 11 | BSWIOZJ | BSWIOZJ | Yes | 5.45 |
| 12 | HGCFDSM | HGCFDSM | Yes | 6.81 |
| 13 | ASCKWLN | ASCKWLN | Yes | 5.98 |
| 14 | CXMTFAJ | CXMTFAJ | Yes | 5.18 |
| 15 | EDSURLB | EDSURLB | Yes | 6.09 |
| 16 | XQIOHBE | XQIOHBE | Yes | 4.92 |
| 17 | ANDJEFZ | ANDJEFZ | Yes | 8.59 |
| 18 | TIKQJRD | TIKQJRD | Yes | 5.01 |
| 19 | YBPNFOD | YBPNFOD | Yes | 6.82 |
| 20 | UCSZPBV | UCSZPBV | Yes | 5.01 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.1, 8.9] | 1.1 8.9 | Yes | 17.58 |
| 2 | [2.7, 7.3] | 7.3 2.7 | Yes | 16.13 |
| 3 | [3.4, 6.6] | 6.6 3.4 | Yes | 16.67 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 23.77 |
| 5 | [1.6, 8.4] | 8.4 1.6 | Yes | 11.4 |
| 6 | [2.0, 8.0] | 8.0 2.0 | Yes | 14.67 |
| 7 | [1.2, 8.8] | 8.8 1.2 | Yes | 12.52 |
| 8 | [3.3, 6.7] | 3.3 6.7 | Yes | 11.75 |
| 9 | [3.0, 7.0] | 3.0 7.0 | Yes | 16.62 |
| 10 | [2.3, 7.7] | 7.7 2.3 | Yes | 10.82 |
| 11 | [0.1, 9.9] | 0.1 9.9 | Yes | 16.3 |
| 12 | [4.9, 5.1] | 5.1 4.9 | Yes | 13.46 |
| 13 | [1.3, 8.7] | 1.3 8.7 | Yes | 9.48 |
| 14 | [3.9, 6.1] | 3.9 6.1 | Yes | 12.63 |
| 15 | [1.5, 8.5] | 8.5 1.5 | Yes | 19.51 |
| 16 | [0.3, 9.7] | 0.3 9.7 | Yes | 16.1 |
| 17 | [3.2, 6.8] | 6.8 3.2 | Yes | 22.92 |
| 18 | [1.8, 8.2] | 8.2 1.8 | Yes | 16.27 |
| 19 | [2.5, 7.5] | 7.5 2.5 | Yes | 19.19 |
| 20 | [3.7, 6.3] | 3.7 6.3 | Yes | 14.47 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | W2DO5LVII2JA | W2DO5LVII2JA | Yes | 4.56 |
| 2 | TPR1SE3XA6FR | TPR1SE3XA6FR | Yes | 4.08 |
| 3 | 40MAPCKR1GR1 | 40MAPCKR1GR1 | Yes | 4.43 |
| 4 | UF0M0UE0JRDO | UFOMOUEOIRDO | No | 8.13 |
| 5 | 2P9AVZF4VX58 | 2P9AVZF4VX58 | Yes | 3.84 |
| 6 | FK3GCL3D8HZS | FK3GCL3D8HZS | Yes | 4.27 |
| 7 | K541T9EXK4XY | K541T9EXK4XY | Yes | 3.95 |
| 8 | 5JXZDET1ZFRD | 5JXZDET1ZFRD | Yes | 4.35 |
| 9 | TSJ60IYJMM1J | TSJGQIYJMM1J | No | 6.74 |
| 10 | CSY55IA1AD3V | CSY55IA1AD3V | Yes | 4.2 |
| 11 | HYO0LMUMA8LL | HYO0LMUMA8LL | Yes | 4.09 |
| 12 | E9VUBFGHJ6H7 | E9VUBFGHJ6H7 | Yes | 5.19 |
| 13 | LTASJDOMLBOG | LTASJDOMLBOG | Yes | 3.82 |
| 14 | 87WUGH8UGYQ2 | 87WUGH8UGYQ2 | Yes | 4.56 |
| 15 | ICKD3RY3VG0Y | ICKD3RY3VG0Y | Yes | 6.46 |
| 16 | VPIFBNMZ7Y5K | VPIFBNMZ7Y5K | Yes | 5.38 |
| 17 | D60LX0NJ1UD4 | D60LXONJ1UD4 | No | 7.22 |
| 18 | 0XWRGUIYLCLN | OXWRGUIYLCLN | No | 4.91 |
| 19 | P1QP078A3UED | P1QP078A3UED | Yes | 5.5 |
| 20 | 340GSTZP6D1B | 340GSTZP6D1B | Yes | 4.04 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 20 | Yes | 24.01 |
| 2 | 9 | 9 | Yes | 4.98 |
| 3 | 3 | 25 | No | 12.39 |
| 4 | 198 |  | No | 26.63 |
| 5 | 4 | 4 | Yes | 12.29 |
| 6 | 4096 | 1048576 | No | 20.04 |
| 7 | 48 | 48 | Yes | 8.82 |
| 8 | 4 | 4 | Yes | 10.97 |
| 9 | 7 | 7 | Yes | 3.68 |
| 10 | 10 | 9 | No | 12.53 |
| 11 | 1440 | 1440 | Yes | 9.9 |
| 12 | 31 | 31 | Yes | 6.16 |
| 13 | 19 | 19 | Yes | 7.64 |
| 14 | 63 | 63 | Yes | 5.18 |
| 15 | 60 | I need to find the pattern in this sequence: 6 - 12 - 14 - 28 - 30 - ?  Looking at the transitions between numbers: - From 6 to | No | 28.6 |
| 16 | 67 | 67 | Yes | 5.13 |
| 17 | 28 | 28 | Yes | 11.04 |
| 18 | 243 | 243 | Yes | 4.46 |
| 19 | 26 |  | No | 28.24 |
| 20 | 44 | 44 | Yes | 19.08 |
