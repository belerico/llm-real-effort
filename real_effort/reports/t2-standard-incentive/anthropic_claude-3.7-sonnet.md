# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8600 | 31476 | 40076 | 1 | 19 | 22.64 | 452.92 |
| add_numbers | 4520 | 5005 | 9525 | 20 | 0 | 5.11 | 102.31 |
| counting_zeros | 7460 | 27718 | 35178 | 12 | 8 | 17.35 | 347.32 |
| task_decoding | 13900 | 8640 | 22540 | 20 | 0 | 6.83 | 136.87 |
| task_summation | 7820 | 26406 | 34226 | 19 | 1 | 16.88 | 337.73 |
| task_transcription | 4676 | 5564 | 10240 | 16 | 4 | 5.59 | 111.88 |
| task_sequences | 3781 | 12420 | 16201 | 20 | 0 | 9.26 | 185.19 |
| **TOTAL** | **50757** | **117229** | **167986** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 4 2 5 2 6 1 2 5 4 2 5 6 | 5 4 4 5 2 2 6 1 2 5 4 2 6 5 | No | 24.3 |
| 2 | 6 1 2 1 3 4 5 2 1 6 3 1 4 4 | 6 1 2 1 3 4 5 2 1 6 3 1 4 4 | Yes | 20.9 |
| 3 | 4 6 1 6 4 6 1 6 3 1 5 3 1 6 | 4 6 6 4 1 6 1 1 3 6 3 5 1 6 | No | 16.81 |
| 4 | 4 3 5 1 6 5 1 3 6 1 3 2 6 1 | 4 3 5 6 1 5 1 3 6 1 3 2 1 6 | No | 23.48 |
| 5 | 3 3 5 4 3 5 6 2 2 4 3 3 2 3 | 3 3 5 4 3 5 6 2 2 4 3 2 3 | No | 23.48 |
| 6 | 5 4 3 1 2 1 1 4 1 3 6 6 2 5 | 4 5 3 2 1 1 6 1 3 4 6 5 2 | No | 22.18 |
| 7 | 2 6 4 5 6 3 5 2 4 2 5 1 3 6 | 2 6 5 6 5 2 5 1 3 6 | No | 28.07 |
| 8 | 4 1 3 2 5 3 5 2 4 2 6 3 4 2 | 3 1 5 2 4 3 5 2 4 2 3 4 6 2 3 4 6 | No | 25.87 |
| 9 | 5 2 1 2 6 4 5 4 5 3 2 6 1 3 | 5 2 1 2 5 4 6 6 5 3 2 4 1 3 | No | 26.99 |
| 10 | 6 4 5 5 3 1 1 5 6 2 3 1 3 6 | 6 4 5 5 3 1 1 5 6 2 3 1 6 3 | No | 24.09 |
| 11 | 2 6 1 1 4 1 2 1 6 4 6 3 4 2 | 1 6 2 1 4 1 2 1 6 4 6 3 4 2 | No | 22.13 |
| 12 | 1 6 4 1 2 2 1 1 1 6 5 2 4 6 | 1 1 6 2 4 1 2 1 1 6 5 2 6 4 | No | 23.08 |
| 13 | 4 1 3 4 1 6 5 4 3 5 4 5 3 6 | 4 1 3 4 1 6 5 4 3 5 5 3 4 5 3 6 | No | 21.79 |
| 14 | 5 6 6 1 6 1 3 2 4 3 1 1 4 2 | 6 5 6 1 1 3 6 2 1 4 3 2 4 1 | No | 22.22 |
| 15 | 2 4 1 6 3 6 5 6 1 3 2 6 4 1 | 2 6 1 6 3 3 5 6 5 6 1 3 1 6 4 2 | No | 21.55 |
| 16 | 3 6 2 4 5 1 4 3 3 5 6 4 3 5 | 3 6 2 4 5 1 4 3 3 5 6 5 3 4 | No | 15.64 |
| 17 | 1 4 5 2 6 1 3 5 6 2 6 1 5 3 | 1 4 5 6 2 1 6 5 3 2 3 1 5 6 | No | 17.23 |
| 18 | 3 2 6 2 3 4 6 3 5 2 5 6 2 6 | 3 2 6 3 2 4 6 5 3 2 6 5 2 6 | No | 23.57 |
| 19 | 3 6 1 1 3 5 2 1 3 3 2 1 2 3 | 3 6 1 1 3 5 2 3 1 3 2 1 2 3 | No | 24.84 |
| 20 | 1 2 4 6 3 5 4 5 1 2 6 1 6 3 | 1 6 5 2 4 6 4 5 1 6 2 3 | No | 24.49 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1382 | 1382 | Yes | 6.28 |
| 2 | 2137 | 2137 | Yes | 4.55 |
| 3 | 1309 | 1309 | Yes | 4.03 |
| 4 | 1234 | 1234 | Yes | 8.5 |
| 5 | 1817 | 1817 | Yes | 3.6 |
| 6 | 1955 | 1955 | Yes | 5.92 |
| 7 | 1188 | 1188 | Yes | 4.49 |
| 8 | 1771 | 1771 | Yes | 5.25 |
| 9 | 1359 | 1359 | Yes | 3.73 |
| 10 | 2073 | 2073 | Yes | 4.88 |
| 11 | 1947 | 1947 | Yes | 6.07 |
| 12 | 2083 | 2083 | Yes | 6.37 |
| 13 | 1905 | 1905 | Yes | 3.38 |
| 14 | 1706 | 1706 | Yes | 3.98 |
| 15 | 2104 | 2104 | Yes | 6.31 |
| 16 | 2126 | 2126 | Yes | 5.21 |
| 17 | 1471 | 1471 | Yes | 2.6 |
| 18 | 2085 | 2085 | Yes | 5.11 |
| 19 | 1892 | 1892 | Yes | 6.57 |
| 20 | 1395 | 1395 | Yes | 5.37 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 11.68 |
| 2 | 55 | 55 | Yes | 9.39 |
| 3 | 51 | 52 | No | 19.83 |
| 4 | 36 | 36 | Yes | 21.02 |
| 5 | 51 | I'm going to count the zeros in the grid systematically, row by row.  Row 1: 1 0 1 0 1 1 0 1 1 1 - 3 zeros Row 2: 1 0 1 1 0 0 1 1 1 1 - 3 zeros Row 3: 1 0 1 1 1 0 1 1 1 1 - 2 zeros Row 4: 1 1 1 1 1 0 0 1 1 0 - 3 zeros Row 5: 1 1 1 1 0 0 0 0 1 1 - 4 zeros Row 6: 1 1 0 0 1 1 0 0 1 1 - 4 zeros Row 7: 0 0 1 1 1 1 1 0 1 1 - 3 zeros Row 8: 1 1 0 1 1 0 0 0 0 0 - 6 zeros Row 9: 1 0 1 0 1 1 1 1 1 1 - 2 zeros Row 10: 1 1 1 1 0 1 0 1 0 0 - 4 zeros Row 11: 1 1 1 1 0 1 0 1 1 1 - 2 zeros Row 12: 1 0 1 1 1 1 0 1 0 0 - 4 zeros Row 13: 0 0 0 0 1 0 1 1 1 1 - 5 zeros Row 14: 1 1 1 0 1 0 0 1 1 0 - 4 zeros Row 15: 1 0 1 1 1 1 1 0 1 1 - 2 zeros  Answer | No | 23.77 |
| 6 | 53 | 51 | No | 16.2 |
| 7 | 38 | 38 | Yes | 19.25 |
| 8 | 35 | 35 | Yes | 13.9 |
| 9 | 75 | 69 | No | 19.67 |
| 10 | 55 | I'll count all the zeros (0s) in the image:  Row 1: 1 1 1 0 1 0 0 0 0 1 (5 zeros) Row 2: 1 1 0 1 0 0 1 1 1 1 (3 zeros) Row 3: 1 1 0 1 1 1 1 1 1 1 (1 zero) Row 4: 0 0 0 1 0 1 0 1 1 0 (6 zeros) Row 5: 0 1 1 0 0 1 1 1 0 1 (4 zeros) Row 6: 1 1 1 1 0 1 1 0 0 1 (3 zeros) Row 7: 1 1 1 1 0 0 1 0 1 0 (4 zeros) Row 8: 0 0 0 1 1 1 0 0 0 1 (6 zeros) Row 9: 1 1 1 1 1 1 1 0 1 0 (2 zeros) Row 10: 0 0 0 1 1 0 0 0 0 0 (8 zeros) Row 11: 1 1 1 1 1 1 1 0 0 1 (2 zeros) Row 12: 0 0 1 1 1 0 1 0 1 1 (4 zeros) Row 13: 1 1 1 1 1 1 1 1 0 0 (2 zeros) | No | 28.13 |
| 11 | 71 | 71 | Yes | 11.09 |
| 12 | 38 | 38 | Yes | 13.58 |
| 13 | 49 | 49 | Yes | 23.07 |
| 14 | 43 | 43 | Yes | 22.34 |
| 15 | 63 | 63 | Yes | 15.52 |
| 16 | 52 | 50 | No | 18.2 |
| 17 | 41 | 41 | Yes | 14.86 |
| 18 | 38 | 37 | No | 14.56 |
| 19 | 38 | 38 | Yes | 13.53 |
| 20 | 71 | 72 | No | 17.42 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LWDJSVH | LWDJSVH | Yes | 6.52 |
| 2 | EZFAIMU | EZFAIMU | Yes | 5.09 |
| 3 | LKTXVWY | LKTXVWY | Yes | 5.62 |
| 4 | NAVDZKO | NAVDZKO | Yes | 8.38 |
| 5 | GFWDTQV | GFWDTQV | Yes | 6.07 |
| 6 | MTXRZDQ | MTXRZDQ | Yes | 6.5 |
| 7 | VIXFCBQ | VIXFCBQ | Yes | 8.72 |
| 8 | WASDZPK | WASDZPK | Yes | 6.24 |
| 9 | MZPHNGT | MZPHNGT | Yes | 5.09 |
| 10 | AVDQEXW | AVDQEXW | Yes | 5.64 |
| 11 | SLZMNIR | SLZMNIR | Yes | 8.49 |
| 12 | SQGNJVU | SQGNJVU | Yes | 5.74 |
| 13 | PBZYNOX | PBZYNOX | Yes | 5.85 |
| 14 | DAEOCQN | DAEOCQN | Yes | 10.52 |
| 15 | XFACPSN | XFACPSN | Yes | 8.58 |
| 16 | RCOGPJM | RCOGPJM | Yes | 4.27 |
| 17 | WNKCTUI | WNKCTUI | Yes | 10.34 |
| 18 | RUDGIHW | RUDGIHW | Yes | 8.6 |
| 19 | LCOXMQG | LCOXMQG | Yes | 5.14 |
| 20 | OZMXJFC | OZMXJFC | Yes | 5.24 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.0, 9.0] | 9.0 1.0 | Yes | 20.28 |
| 2 | [0.6, 9.4] | 0.6 9.4 | Yes | 22.72 |
| 3 | [0.9, 9.1] | 9.1 0.9 | Yes | 12.66 |
| 4 | [2.8, 7.2] | 7.2 2.8 | Yes | 12.38 |
| 5 | [4.0, 6.0] | 6.0 4.0 | Yes | 11.57 |
| 6 | [0.1, 9.9] | 0.1 9.9 | Yes | 16.45 |
| 7 | [4.9, 5.1] | 5.1 4.9 | Yes | 14.91 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 15.99 |
| 9 | [2.4, 7.6] | 2.4 7.6 | Yes | 21.1 |
| 10 | [4.7, 5.3] | 5.3 4.7 | Yes | 14.83 |
| 11 | [2.6, 7.4] | 7.4 2.6 | Yes | 13.23 |
| 12 | [3.2, 6.8] | 3.2 6.8 | Yes | 13.36 |
| 13 | [3.5, 6.5] | 6.5 3.5 | Yes | 22.55 |
| 14 | [0.1, 9.9] | 0.1 9.9 | Yes | 20.81 |
| 15 | [3.4, 6.6] | 3.4 6.6 | Yes | 12.78 |
| 16 | [1.0, 9.0] | I need to examine the grid and find two numbers that sum to exactly 10.0.  Looking at all the numbers in the grid: - Row 1: 1.0, 3.2, 8.6, 2.4 - Row 2: 9.0, 2.7, 4.6, 9.9 - Row 3: 8.8, 8.5, 7.5, 0.3 - Row 4: 9.2, 8.4, 5.8, 6.4  Testing various combinations: - 1.0 + 9.0 = 10.0 ✓ - 3.2 + 6.8 = 10.0 (but 6.8 is not in the grid) - 2.4 + 7.6 = 10.0 (but 7.6 is not in the grid) - 4.6 + 5.4 = 10.0 (but 5.4 is not in the grid)  I continue checking all possible pairs and find: - 7.5 + 2.5 = 10.0 (but 2.5 is not in the grid) - 3.6 + 6.4 = 10.0 (but 3.6 is not in the grid) - 5.8 + 4.2 = 10.0 (but 4.2 is not in the grid)  The pair that sums to 10.0 is 1.0 an | No | 25.08 |
| 17 | [2.7, 7.3] | 7.3 2.7 | Yes | 20.91 |
| 18 | [3.3, 6.7] | 6.7 3.3 | Yes | 11.98 |
| 19 | [0.2, 9.8] | 0.2 9.8 | Yes | 18.89 |
| 20 | [2.2, 7.8] | 7.8 2.2 | Yes | 15.07 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OAO6APYDHTE3 | OAO6APYDHTE3 | Yes | 4.95 |
| 2 | J48LKQ159E92 | J48LKO159E92 | No | 4.65 |
| 3 | O7E7IX5MUAO6 | O7E7IX5MUAO6 | Yes | 5.93 |
| 4 | 60ELOK6EX0PC | 60ELOK$EX0PC | No | 5.95 |
| 5 | 4QDFF8DAMK9J | 4QDFF8DAMK9J | Yes | 5.89 |
| 6 | 8AWQF1QWWREU | 8AWOF1OWWREU | No | 8.32 |
| 7 | TBWGR4M51GFC | TBWGR4M51GFC | Yes | 4.98 |
| 8 | XIWZ5QCXEXMN | XIWZ5QCXEXMN | Yes | 6.27 |
| 9 | PCX6AH64GHHF | PCX6AH64GHHF | Yes | 5.56 |
| 10 | 4TCF49GVU6UW | 4TCF49GVU6UW | Yes | 6.73 |
| 11 | S2X9A943OANI | S2X9A943OANI | Yes | 6.14 |
| 12 | 04ZVHIXDSG2R | 04ZVHIXDSG2R | Yes | 4.25 |
| 13 | Y6QIU2HWUWVN | Y6QIU2HWUWVN | Yes | 5.56 |
| 14 | S20YD9UK1YNV | S20YD9UK1YNV | Yes | 4.46 |
| 15 | 8P3ELEZROEU8 | 8P3ELEZROEU8 | Yes | 4.04 |
| 16 | VHNQ0GS0HEL5 | VHNOOGSOHEL5 | No | 6.71 |
| 17 | UGW1VKM42PUN | UGW1VKM42PUN | Yes | 5.1 |
| 18 | 70RRCH9AIS5S | 70RRCH9AIS5S | Yes | 6.81 |
| 19 | WSDLPMBSNIVJ | WSDLPMBSNIVJ | Yes | 4.44 |
| 20 | UBUFD7YSHENZ | UBUFD7YSHENZ | Yes | 5.03 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 22.36 |
| 2 | 16 | 16 | Yes | 12.06 |
| 3 | 4096 | 4096 | Yes | 15.93 |
| 4 | 36 | 36 | Yes | 3.88 |
| 5 | 243 | 243 | Yes | 8.71 |
| 6 | 63 | 63 | Yes | 5.39 |
| 7 | 10 | 10 | Yes | 13.99 |
| 8 | 44 | 44 | Yes | 22.56 |
| 9 | 5 | 5 | Yes | 5.75 |
| 10 | 1 | 1 | Yes | 5.03 |
| 11 | 48 | 48 | Yes | 4.18 |
| 12 | 23 | 23 | Yes | 5.83 |
| 13 | 6 | 6 | Yes | 9.49 |
| 14 | 7680 | 7680 | Yes | 9.89 |
| 15 | 31 | 31 | Yes | 4.92 |
| 16 | 3 | 3 | Yes | 9.61 |
| 17 | 1440 | 1440 | Yes | 5.68 |
| 18 | 9 | 9 | Yes | 9.05 |
| 19 | 7 | 7 | Yes | 5.78 |
| 20 | 19 | 19 | Yes | 5.09 |
