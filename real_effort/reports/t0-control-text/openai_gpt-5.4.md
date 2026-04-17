# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-26 15:51:10

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

**Model-specific overrides:**
- temperature: `None`

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
| sudoku_game | 4654 | 27617 | 32271 | 12 | 8 | 23.81 | 476.13 |
| add_numbers | 2420 | 883 | 3303 | 20 | 0 | 3.71 | 74.23 |
| counting_zeros | 3820 | 16831 | 20651 | 20 | 0 | 13.27 | 265.38 |
| task_decoding | 3760 | 2678 | 6438 | 20 | 0 | 4.59 | 91.78 |
| task_summation | 3895 | 5350 | 9245 | 19 | 1 | 12.59 | 251.89 |
| task_transcription | 2561 | 1488 | 4049 | 20 | 0 | 3.79 | 75.72 |
| task_sequences | 2421 | 5998 | 8419 | 18 | 2 | 9.30 | 185.99 |
| string_entry | 2850 | 24422 | 27272 | 12 | 8 | 23.21 | 464.26 |
| **TOTAL** | **26381** | **85267** | **111648** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 6 4 6 3 2 3 3 2 1 3 2 6 4 | 2 6 4 6 3 2 3 3 2 1 3 2 6 4 | Yes | 29.66 |
| 2 | 3 6 4 1 2 5 6 1 4 2 4 1 5 6 |  | No | 38.39 |
| 3 | 1 2 5 1 3 3 4 3 2 2 4 6 3 2 |  | No | 34.02 |
| 4 | 1 5 2 1 5 5 6 1 2 5 6 3 4 2 | 1 5 2 1 5 5 6 1 2 5 6 3 4 2 | Yes | 16.82 |
| 5 | 6 5 1 2 5 4 4 1 5 2 4 6 1 2 | 6 5 1 2 5 4 4 1 5 2 4 6 1 2 | Yes | 13.99 |
| 6 | 3 6 5 4 4 1 6 2 4 3 5 2 2 1 |  | No | 35.16 |
| 7 | 2 3 2 1 5 3 1 6 5 2 4 2 6 3 | 2 3 2 1 5 3 1 6 5 2 4 2 6 3 | Yes | 12.67 |
| 8 | 3 5 4 6 1 3 2 4 1 5 2 6 3 1 | 3 5 4 6 1 3 2 4 1 5 2 6 3 1 | Yes | 13.46 |
| 9 | 3 4 3 3 2 5 6 6 2 5 2 1 1 2 | 3 4 3 3 2 5 6 6 2 5 2 1 1 2 | Yes | 13.55 |
| 10 | 6 1 5 3 4 3 1 5 2 4 1 2 6 5 | 6 1 5 3 4 3 1 5 2 4 1 2 6 5 | Yes | 32.94 |
| 11 | 3 5 4 5 3 6 2 2 2 6 1 3 2 1 | 3 5 4 5 3 6 2 2 2 6 1 3 2 1 | Yes | 12.29 |
| 12 | 4 3 1 3 1 6 2 5 3 4 1 2 5 3 | 4 3 1 3 1 6 2 5 3 4 1 2 5 3 | Yes | 29.7 |
| 13 | 1 5 4 5 1 4 3 2 5 2 1 3 1 6 | 1 5 4 5 1 4 3 2 5 2 1 3 1 6 | Yes | 11.44 |
| 14 | 5 4 1 2 3 1 3 1 4 6 3 6 3 1 | 5 4 1 2 3 1 3 1 6 3 4 6 3 6 3 1 | No | 11.06 |
| 15 | 6 2 4 6 2 5 3 1 4 5 4 1 6 5 |  | No | 31.7 |
| 16 | 5 2 6 5 4 5 3 5 1 2 5 6 6 1 |  | No | 45.93 |
| 17 | 3 1 3 2 3 5 6 4 2 1 6 4 4 5 |  | No | 32.31 |
| 18 | 3 2 5 6 2 5 5 4 3 4 1 4 6 5 |  | No | 35.87 |
| 19 | 5 6 4 3 4 2 5 6 5 4 2 6 6 4 | 5 6 4 3 4 2 5 6 5 4 2 6 6 4 | Yes | 12.21 |
| 20 | 5 2 6 3 3 1 4 4 3 1 5 2 1 6 | 5 2 6 3 3 1 4 4 3 1 5 2 1 6 | Yes | 12.94 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1017 | 1017 | Yes | 3.56 |
| 2 | 1954 | 1954 | Yes | 5.76 |
| 3 | 1678 | 1678 | Yes | 3.03 |
| 4 | 2125 | 2125 | Yes | 3.26 |
| 5 | 2481 | 2481 | Yes | 3.64 |
| 6 | 1464 | 1464 | Yes | 3.86 |
| 7 | 1558 | 1558 | Yes | 4.38 |
| 8 | 1826 | 1826 | Yes | 2.91 |
| 9 | 1435 | 1435 | Yes | 3.74 |
| 10 | 1689 | 1689 | Yes | 3.33 |
| 11 | 795 | 795 | Yes | 4.2 |
| 12 | 1441 | 1441 | Yes | 3.46 |
| 13 | 1436 | 1436 | Yes | 3.25 |
| 14 | 2312 | 2312 | Yes | 4.12 |
| 15 | 2149 | 2149 | Yes | 3.3 |
| 16 | 1364 | 1364 | Yes | 4.47 |
| 17 | 1590 | 1590 | Yes | 3.37 |
| 18 | 2175 | 2175 | Yes | 4.08 |
| 19 | 2167 | 2167 | Yes | 3.32 |
| 20 | 1627 | 1627 | Yes | 3.17 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 68 | 68 | Yes | 17.01 |
| 2 | 70 | 70 | Yes | 13.3 |
| 3 | 46 | 46 | Yes | 13.35 |
| 4 | 75 | 75 | Yes | 11.49 |
| 5 | 51 | 51 | Yes | 16.91 |
| 6 | 50 | 50 | Yes | 12.16 |
| 7 | 61 | 61 | Yes | 21.38 |
| 8 | 42 | 42 | Yes | 15.1 |
| 9 | 44 | 44 | Yes | 12.17 |
| 10 | 37 | 37 | Yes | 14.37 |
| 11 | 41 | 41 | Yes | 8.2 |
| 12 | 69 | 69 | Yes | 12.51 |
| 13 | 53 | 53 | Yes | 12.22 |
| 14 | 60 | 60 | Yes | 10.12 |
| 15 | 55 | 55 | Yes | 13.01 |
| 16 | 60 | 60 | Yes | 12.69 |
| 17 | 57 | 57 | Yes | 11.94 |
| 18 | 57 | 57 | Yes | 11.79 |
| 19 | 57 | 57 | Yes | 14.31 |
| 20 | 58 | 58 | Yes | 11.34 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MGQVYAE | MGQVYAE | Yes | 4.98 |
| 2 | CIWFLGY | CIWFLGY | Yes | 4.86 |
| 3 | STRPZYE | STRPZYE | Yes | 4.26 |
| 4 | LYTASIG | LYTASIG | Yes | 3.29 |
| 5 | GZNQSOD | GZNQSOD | Yes | 3.26 |
| 6 | SMNEIVB | SMNEIVB | Yes | 4.41 |
| 7 | WTRYVGK | WTRYVGK | Yes | 4.76 |
| 8 | POAWTYQ | POAWTYQ | Yes | 4.65 |
| 9 | ZNVACFE | ZNVACFE | Yes | 5.09 |
| 10 | QYKATFN | QYKATFN | Yes | 4.56 |
| 11 | JSYWICG | JSYWICG | Yes | 5.22 |
| 12 | GVMUJYK | GVMUJYK | Yes | 4.32 |
| 13 | FMZIHPT | FMZIHPT | Yes | 2.61 |
| 14 | JEGIPWQ | JEGIPWQ | Yes | 4.84 |
| 15 | KBQJOSL | KBQJOSL | Yes | 5.73 |
| 16 | BLMRGAQ | BLMRGAQ | Yes | 6.34 |
| 17 | OBYUEPX | OBYUEPX | Yes | 2.84 |
| 18 | AFNLYWT | AFNLYWT | Yes | 4.61 |
| 19 | PMJHFCO | PMJHFCO | Yes | 5.25 |
| 20 | JWLVBYT | JWLVBYT | Yes | 5.9 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 6.0 4.0 | Yes | 7.43 |
| 2 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.73 |
| 3 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.17 |
| 4 | [0.8, 9.2] | 9.2 0.8 | Yes | 5.97 |
| 5 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.17 |
| 6 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.93 |
| 7 | [3.0, 7.0] | TIMEOUT | No | 120.03 |
| 8 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.41 |
| 9 | [1.1, 8.9] | 8.9 1.1 | Yes | 9.07 |
| 10 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.59 |
| 11 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.11 |
| 12 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.1 |
| 13 | [1.6, 8.4] | 8.4 1.6 | Yes | 7.41 |
| 14 | [2.3, 7.7] | 7.7 2.3 | Yes | 7.17 |
| 15 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.1 |
| 16 | [5.0, 5.0] | 5.0 5.0 | Yes | 7.43 |
| 17 | [4.9, 5.1] | 4.9 5.1 | Yes | 7.81 |
| 18 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.58 |
| 19 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.3 |
| 20 | [5.0, 5.0] | 5.0 5.0 | Yes | 6.38 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | N2E14QQI62VW | N2E14QQI62VW | Yes | 4.07 |
| 2 | 49XM13VF3ASM | 49XM13VF3ASM | Yes | 4.39 |
| 3 | 0H9YVEPTF2PK | 0H9YVEPTF2PK | Yes | 5.34 |
| 4 | SEWNHTFQZDG0 | SEWNHTFQZDG0 | Yes | 4.05 |
| 5 | 52MCC5J6NICO | 52MCC5J6NICO | Yes | 5.8 |
| 6 | YWLBMGJSPCMO | YWLBMGJSPCMO | Yes | 3.99 |
| 7 | ZSWBVEX5IC6Y | ZSWBVEX5IC6Y | Yes | 4.49 |
| 8 | YPKV9IADE0FE | YPKV9IADE0FE | Yes | 5.16 |
| 9 | 4E5L14K5XZ9Q | 4E5L14K5XZ9Q | Yes | 6.94 |
| 10 | 0UATHUM6UCPM | 0UATHUM6UCPM | Yes | 3.43 |
| 11 | Z08DYV827QDW | Z08DYV827QDW | Yes | 3.78 |
| 12 | WR47KZG08U4F | WR47KZG08U4F | Yes | 1.58 |
| 13 | CXN4MC3V3XDZ | CXN4MC3V3XDZ | Yes | 2.31 |
| 14 | UV3WE5DHPDQU | UV3WE5DHPDQU | Yes | 1.6 |
| 15 | LEMKBCILZ5RI | LEMKBCILZ5RI | Yes | 3.48 |
| 16 | QFBMW7MLOC1W | QFBMW7MLOC1W | Yes | 3.14 |
| 17 | AT78FALQO9JD | AT78FALQO9JD | Yes | 2.67 |
| 18 | 00K58ILMZXXW | 00K58ILMZXXW | Yes | 2.02 |
| 19 | 34XZ6LZ2BJVH | 34XZ6LZ2BJVH | Yes | 3.82 |
| 20 | C5G9HQ5SHS6C | C5G9HQ5SHS6C | Yes | 3.65 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 15.23 |
| 2 | 39 | 39 | Yes | 4.78 |
| 3 | 9 | 9 | Yes | 4.75 |
| 4 | 20 |  | No | 49.26 |
| 5 | 243 | 243 | Yes | 3.67 |
| 6 | 31 | 31 | Yes | 3.16 |
| 7 | 60 | 60 | Yes | 3.79 |
| 8 | 4096 |  | No | 41.69 |
| 9 | 4 | 4 | Yes | 4.17 |
| 10 | 64 | 64 | Yes | 5.58 |
| 11 | 4 | 4 | Yes | 4.74 |
| 12 | 63 | 63 | Yes | 3.63 |
| 13 | 73 | 73 | Yes | 3.57 |
| 14 | 19 | 19 | Yes | 3.29 |
| 15 | 7 | 7 | Yes | 3.54 |
| 16 | 5 | 5 | Yes | 7.13 |
| 17 | 36 | 36 | Yes | 3.11 |
| 18 | 26 | 26 | Yes | 6.21 |
| 19 | 44 | 44 | Yes | 10.92 |
| 20 | 65 | 65 | Yes | 3.75 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  (( ) (<< | (( ) (<< | No | 28.34 |
| 2 | (/<(/(\_< | (/<(/(\_< | Yes | 10.69 |
| 3 | )/\(\_<<( | )/\(\_<<( | Yes | 34.07 |
| 4 | _)( \(_\) |  | No | 39.03 |
| 5 | /<(/_/\() | /<(/_/\() | Yes | 10.84 |
| 6 | /)\/<(<\  | /)\/<(<\ | No | 13.59 |
| 7 |  <_(/ <(\ |  | No | 33.53 |
| 8 | )/()__/<( | )/()__/<( | Yes | 20.91 |
| 9 | <_()//( < | <_()//( < | Yes | 38.71 |
| 10 | /<// \ /  | /<// \ / | No | 11.41 |
| 11 | _\ /(/))_ | /\) <(_<) | No | 29.84 |
| 12 | \  )<) <\ | \  )<) <\ | Yes | 29.71 |
| 13 | //\)\(\ ) | //\)\(\ ) | Yes | 27.64 |
| 14 | )/<_()_\\ | /\) <(_<) | No | 19.35 |
| 15 | \/(\<)\(( | \/(\<)\(( | Yes | 9.55 |
| 16 | _)(\/(/ \ |  | No | 40.17 |
| 17 | )</)<(/_< | )</)<(/_< | Yes | 30.91 |
| 18 | )_/(() () | )_/(() () | Yes | 21.85 |
| 19 | /(\_)((_/ | /(\_)((_/ | Yes | 7.81 |
| 20 | _)_  /\/) | _)_  /\/) | Yes | 6.29 |
