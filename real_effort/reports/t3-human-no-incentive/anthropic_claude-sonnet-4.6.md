# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
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
| sudoku_game | 8740 | 36133 | 44873 | 9 | 11 | 29.38 | 587.82 |
| add_numbers | 4660 | 803 | 5463 | 20 | 0 | 2.12 | 42.47 |
| counting_zeros | 7600 | 28526 | 36126 | 8 | 12 | 16.40 | 328.26 |
| task_decoding | 14040 | 5469 | 19509 | 19 | 1 | 5.31 | 106.38 |
| task_summation | 7960 | 3757 | 11717 | 20 | 0 | 4.23 | 84.7 |
| task_transcription | 4812 | 854 | 5666 | 19 | 1 | 2.51 | 50.4 |
| task_sequences | 3921 | 3465 | 7386 | 18 | 2 | 3.39 | 67.81 |
| **TOTAL** | **51733** | **79007** | **130740** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 3 1 2 1 5 4 3 1 6 5 6 3 5 | 5 3 1 2 1 5 4 3 1 6 5 6 3 5 | Yes | 20.71 |
| 2 | 1 2 2 6 5 5 5 2 1 1 2 4 5 2 |  | No | 41.83 |
| 3 | 3 5 4 2 6 3 5 1 4 6 1 5 2 3 | 3 5 4 2 6 3 5 1 4 6 1 5 2 3 | Yes | 27.56 |
| 4 | 5 4 1 1 1 3 2 2 3 1 2 5 1 4 | 5 4 1 1 1 3 2 2 3 1 2 5 1 4 | Yes | 23.14 |
| 5 | 3 6 6 2 1 3 6 1 1 3 2 5 1 4 | 3 6 6 2 1 3 6 1 1 3 2 5 1 4 | Yes | 22.31 |
| 6 | 5 1 6 2 3 5 3 1 3 6 4 6 1 2 |  | No | 36.22 |
| 7 | 6 2 5 6 4 2 3 5 6 6 4 3 4 5 |  | No | 33.05 |
| 8 | 6 4 1 5 5 4 5 6 1 4 3 1 4 1 | 6 4 1 5 4 5 6 1 4 3 1 4 1 | No | 25.15 |
| 9 | 1 5 6 2 4 4 3 5 6 3 1 5 3 1 | 1 5 6 2 4 4 3 5 6 3 1 5 3 1 | Yes | 27.89 |
| 10 | 2 5 2 5 3 3 6 1 2 5 3 4 1 4 | 2 5 2 5 3 3 6 1 2 5 3 4 1 4 | Yes | 17.59 |
| 11 | 3 2 2 3 6 1 1 6 2 1 3 4 6 3 |  | No | 32.41 |
| 12 | 1 5 1 3 4 1 6 4 2 5 3 2 4 1 |  | No | 36.25 |
| 13 | 6 3 5 3 3 5 1 6 6 1 5 5 6 4 |  | No | 33.52 |
| 14 | 6 2 3 5 3 1 2 5 6 4 2 1 3 5 | 6 2 3 5 3 1 2 5 6 4 2 1 3 5 | Yes | 18.86 |
| 15 | 5 4 3 4 1 3 5 2 3 6 1 2 2 6 | Looking at the puzzle systematically:  **Row 1:** _, 2, 6, 1, _, _ - Missing: 3, 4, 5 - Col 5 needs from {2,4} → **4**; Col 6 needs from {2,3} → **3**; Col 1 = **5** - Row 1: **5**, 2, 6, 1, **4**, **3**  **Row 2:** _, _, _, _, 6, _ - Top-right box (rows 1-2, cols 4-6): has 1,4,3,_,6,_ → needs 2,5 - Col 4 needs 5 → Row 2 Col 4 = **5**; Row 2 Col 6 = **2** - Col 2 needs 1 → **1**; Col 3 needs 3 → **3**; Col 1 = **4** - Row 2: **4**, **1**, **3**, **5**, 6, **2**  **Row 3:** _, 6, 4, 2, 5, 1 - Col 1 needs 3 → **3** - Row 3: **3**, 6, 4, 2, 5, 1  **Row 4:** _, 3, _, 4, _, 5 - Middle-right box (rows 3-4, cols 4-6): has 2,5,1,4,_,5 → Col 5 = **6** - Row 4 missing: 1,2,6 → Col 3 needs 1 → **1**; Col 1 = **2** - Row 4: **2**, 3, **1**, 4, **6**, 5  **Row 6:** 1, 5, _, _, 3, 4 - Col 3 needs (from {1,2,3}) → **2**; Col 4 = **6** - Row 6: 1, 5, **2**, **6**, 3, 4  **Missing numbers in | No | 32.52 |
| 16 | 4 1 5 4 1 2 1 3 1 6 2 3 5 2 | 4 1 5 4 1 2 1 3 1 6 2 3 5 2 | Yes | 25.91 |
| 17 | 4 1 3 2 1 1 3 4 2 5 5 4 4 3 |  | No | 35.95 |
| 18 | 1 3 4 5 1 4 6 2 3 2 1 5 6 1 |  | No | 36.13 |
| 19 | 3 1 2 5 4 5 3 4 1 3 5 2 4 3 | 3 1 2 5 4 5 3 4 1 3 5 2 4 3 | Yes | 26.96 |
| 20 | 3 1 3 5 4 6 1 2 3 2 5 3 6 4 |  | No | 33.67 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 872 | 872 | Yes | 1.95 |
| 2 | 1001 | 1001 | Yes | 2.22 |
| 3 | 1453 | 1453 | Yes | 2.07 |
| 4 | 1277 | 1277 | Yes | 1.59 |
| 5 | 1785 | 1785 | Yes | 2.18 |
| 6 | 1016 | 1016 | Yes | 1.66 |
| 7 | 2621 | 2621 | Yes | 1.99 |
| 8 | 1615 | 1615 | Yes | 2.02 |
| 9 | 1356 | 1356 | Yes | 1.49 |
| 10 | 1799 | 1799 | Yes | 2.57 |
| 11 | 1345 | 1345 | Yes | 1.78 |
| 12 | 1998 | 1998 | Yes | 1.87 |
| 13 | 2472 | 2472 | Yes | 2.76 |
| 14 | 899 | 899 | Yes | 2.52 |
| 15 | 2478 | 2478 | Yes | 2.38 |
| 16 | 1616 | 1616 | Yes | 2.17 |
| 17 | 1712 | 1712 | Yes | 2.49 |
| 18 | 1646 | 1646 | Yes | 2.18 |
| 19 | 989 | 989 | Yes | 2.33 |
| 20 | 1895 | 1895 | Yes | 2.12 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 67 | No | 15.87 |
| 2 | 47 | 44 | No | 14.06 |
| 3 | 41 | 41 | Yes | 14.16 |
| 4 | 45 | 67 | No | 13.71 |
| 5 | 74 | 67 | No | 16.28 |
| 6 | 40 | 40 | Yes | 13.05 |
| 7 | 56 | 52 | No | 16.69 |
| 8 | 41 | 41 | Yes | 14.1 |
| 9 | 59 | 59 | Yes | 15.03 |
| 10 | 54 | 55 | No | 19.11 |
| 11 | 60 | 57 | No | 15.43 |
| 12 | 63 | 63 | Yes | 20.82 |
| 13 | 46 | 67 | No | 13.07 |
| 14 | 45 | 45 | Yes | 13.38 |
| 15 | 75 | 67 | No | 18.53 |
| 16 | 67 | 67 | Yes | 20.78 |
| 17 | 64 | 61 | No | 18.66 |
| 18 | 75 | 67 | No | 21.24 |
| 19 | 52 | 51 | No | 16.43 |
| 20 | 68 | 68 | Yes | 17.54 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YTMXQKG | YTMXQKG | Yes | 5.83 |
| 2 | CQIBEZG | CQIBEZG | Yes | 4.27 |
| 3 | CLXRPOI | CLXRPOI | Yes | 5.05 |
| 4 | XWREMOI | XWREMOI | Yes | 4.7 |
| 5 | OVRQBUT | OVRQBUT | Yes | 5.24 |
| 6 | PRAKXEJ | PRAKXEJ | Yes | 5.02 |
| 7 | BZSDCOU | BZSDCOU | Yes | 4.96 |
| 8 | CFRYBPN | CFRYBPN | Yes | 5.4 |
| 9 | GFKBPMO | GFKBPMO | Yes | 5.49 |
| 10 | ITQOZRA | ITQOZRA | Yes | 5.28 |
| 11 | UYIPBVK | UYIPBVK | Yes | 5.45 |
| 12 | VOJAUWX | VOJAUWX | Yes | 4.09 |
| 13 | DKSUAGE | DKSUAGE | Yes | 5.42 |
| 14 | MUZXEFA | MUZXEFA | Yes | 5.66 |
| 15 | SFCBEIK | SFCBEIK | Yes | 6.3 |
| 16 | NKJXATU | NKJXATU | Yes | 6.04 |
| 17 | DEMYJLV | DEMYJLV | Yes | 4.28 |
| 18 | XQMKDFG | XQMKDFG | Yes | 5.42 |
| 19 | HEVWTPQ | HEWVTPQ | No | 7.93 |
| 20 | CSHRZEO | CSHRZEO | Yes | 4.36 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.2 |
| 2 | [4.8, 5.2] | 5.2 4.8 | Yes | 2.69 |
| 3 | [0.1, 9.9] | 9.9 0.1 | Yes | 2.99 |
| 4 | [4.0, 6.0] | 6.0 4.0 | Yes | 4.55 |
| 5 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.22 |
| 6 | [2.4, 7.6] | 2.4 7.6 | Yes | 2.26 |
| 7 | [3.8, 6.2] | 6.2 3.8 | Yes | 2.92 |
| 8 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.89 |
| 9 | [2.4, 7.6] | 7.6 2.4 | Yes | 3.59 |
| 10 | [2.7, 7.3] | 2.7 7.3 | Yes | 3.69 |
| 11 | [0.5, 9.5] | 0.5 9.5 | Yes | 7.53 |
| 12 | [1.1, 8.9] | 1.1 8.9 | Yes | 2.76 |
| 13 | [1.3, 8.7] | 1.3 8.7 | Yes | 5.78 |
| 14 | [2.7, 7.3] | 2.7 7.3 | Yes | 2.85 |
| 15 | [2.6, 7.4] | 2.6 7.4 | Yes | 3.94 |
| 16 | [1.4, 8.6] | 8.6 1.4 | Yes | 2.9 |
| 17 | [1.5, 8.5] | 1.5 8.5 | Yes | 3.09 |
| 18 | [4.8, 5.2] | 5.2 4.8 | Yes | 6.92 |
| 19 | [1.5, 8.5] | 8.5 1.5 | Yes | 2.7 |
| 20 | [1.8, 8.2] | 8.2 1.8 | Yes | 4.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | U4Z2JQZDKJK0 | U4Z2JQZDKJK0 | Yes | 3.7 |
| 2 | BODKN7ENMYSK | BODKN7ENMYSK | Yes | 2.24 |
| 3 | 3UC0JMHP76QX | 3UC0JMHP76QX | Yes | 2.48 |
| 4 | 2ANRD6YR3IKL | 2ANRD6YR3IKL | Yes | 2.33 |
| 5 | EQPTUHPZZ64Y | EQPTUHPZZ64Y | Yes | 2.2 |
| 6 | TXWPLZKBNJD6 | TXWPLZKBNJD6 | Yes | 2.35 |
| 7 | N3NYJNRU6OZZ | N3NYJNRU6OZZ | Yes | 2.38 |
| 8 | NAAF5DC4B7T5 | NAAF5DC4B7T5 | Yes | 1.98 |
| 9 | 5E111221WX60 | 5E11221WX60 | No | 4.08 |
| 10 | 1HB181OLIXFO | 1HB181OLIXFO | Yes | 2.26 |
| 11 | W1EG9D6XHV2K | W1EG9D6XHV2K | Yes | 2.29 |
| 12 | H4U3E9JEYNZC | H4U3E9JEYNZC | Yes | 1.95 |
| 13 | C8SX4XIE7P91 | C8SX4XIE7P91 | Yes | 1.73 |
| 14 | QC5LC96410QQ | QC5LC96410QQ | Yes | 2.28 |
| 15 | W7F9NWRTUCON | W7F9NWRTUCON | Yes | 2.37 |
| 16 | V4I22237E2EH | V4I22237E2EH | Yes | 3.08 |
| 17 | KEOUKRNAT2W8 | KEOUKRNAT2W8 | Yes | 2.22 |
| 18 | NEZSTG55VZ8M | NEZSTG55VZ8M | Yes | 2.02 |
| 19 | WDND5N6BEDIR | WDND5N6BEDIR | Yes | 2.28 |
| 20 | MV7TUYVB0R67 | MV7TUYVB0R67 | Yes | 4.08 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 26 | 26 | Yes | 8.38 |
| 2 | 3 | 3 | Yes | 6.3 |
| 3 | 36 | 36 | Yes | 1.8 |
| 4 | 4096 | 16384 | No | 6.31 |
| 5 | 10 | 10 | Yes | 2.34 |
| 6 | 3 | 3 | Yes | 5.02 |
| 7 | 67 | 67 | Yes | 2.37 |
| 8 | 23 | 23 | Yes | 1.98 |
| 9 | 60 | 60 | Yes | 1.5 |
| 10 | 28 | 28 | Yes | 2.27 |
| 11 | 48 | 48 | Yes | 1.63 |
| 12 | 198 | 198 | Yes | 2.15 |
| 13 | 1 | 1 | Yes | 3.29 |
| 14 | 9 | 9 | Yes | 2.41 |
| 15 | 7680 | 7680 | Yes | 3.37 |
| 16 | 16 | 16 | Yes | 3.08 |
| 17 | 6 | 6 | Yes | 2.04 |
| 18 | 20 | 21 | No | 8.31 |
| 19 | 1440 | 1440 | Yes | 1.68 |
| 20 | 4 | 4 | Yes | 1.58 |
