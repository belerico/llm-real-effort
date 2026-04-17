# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-19 10:21:42

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 7760 | 40919 | 48679 | 0 | 20 | 40.21 | 804.38 |
| add_numbers | 6780 | 3188 | 9968 | 20 | 0 | 3.11 | 62.33 |
| counting_zeros | 6840 | 39301 | 46141 | 0 | 20 | 38.82 | 776.7 |
| task_decoding | 10300 | 10451 | 20751 | 20 | 0 | 9.05 | 181.17 |
| task_summation | 7100 | 16051 | 23151 | 18 | 2 | 11.56 | 231.41 |
| task_transcription | 6860 | 13550 | 20410 | 15 | 5 | 13.79 | 275.94 |
| task_sequences | 2421 | 10510 | 12931 | 17 | 3 | 13.80 | 276.1 |
| **TOTAL** | **48061** | **133970** | **182031** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 4 6 4 4 2 6 3 4 1 3 1 2 |  | No | 29.9 |
| 2 | 5 4 3 6 2 5 4 6 2 3 1 4 1 3 |  | No | 50.91 |
| 3 | 3 2 4 6 2 4 3 1 4 5 6 2 6 1 |  | No | 47.14 |
| 4 | 6 3 1 2 3 6 1 3 2 3 1 4 2 3 |  | No | 57.1 |
| 5 | 1 5 6 6 3 4 3 1 3 4 1 5 4 2 |  | No | 30.39 |
| 6 | 5 1 4 3 2 1 3 4 5 2 5 4 3 1 |  | No | 60.8 |
| 7 | 5 5 3 6 1 5 1 6 3 4 3 1 1 4 |  | No | 27.57 |
| 8 | 4 3 6 4 4 1 2 3 6 1 5 3 5 1 |  | No | 33.55 |
| 9 | 2 6 5 6 1 1 3 6 2 5 2 1 4 6 |  | No | 56.49 |
| 10 | 3 4 5 2 1 6 5 3 2 6 5 1 2 6 |  | No | 40.95 |
| 11 | 5 6 1 6 2 5 6 5 2 3 1 4 4 1 |  | No | 24.4 |
| 12 | 5 1 2 4 2 6 1 6 1 2 3 2 2 3 |  | No | 54.23 |
| 13 | 5 1 3 4 5 1 4 2 6 6 3 5 2 3 |  | No | 21.12 |
| 14 | 5 4 3 2 5 6 2 3 4 6 2 5 6 3 |  | No | 34.93 |
| 15 | 1 6 4 2 4 2 6 5 6 5 4 5 6 3 |  | No | 56.66 |
| 16 | 2 4 6 1 2 3 1 5 4 6 2 4 6 4 |  | No | 43.54 |
| 17 | 3 5 2 4 6 4 3 4 1 6 2 3 6 5 |  | No | 35.04 |
| 18 | 6 5 4 3 1 2 6 4 6 4 2 3 5 4 |  | No | 23.44 |
| 19 | 5 2 6 3 2 5 4 1 5 2 3 4 1 6 |  | No | 39.17 |
| 20 | 1 3 4 1 3 2 5 4 4 5 5 6 1 6 |  | No | 36.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1604 | 1604 | Yes | 2.7 |
| 2 | 2258 | 2258 | Yes | 2.98 |
| 3 | 1635 | 1635 | Yes | 2.44 |
| 4 | 1137 | 1137 | Yes | 3.77 |
| 5 | 1856 | 1856 | Yes | 2.58 |
| 6 | 1374 | 1374 | Yes | 3.57 |
| 7 | 1935 | 1935 | Yes | 2.14 |
| 8 | 1574 | 1574 | Yes | 2.85 |
| 9 | 1577 | 1577 | Yes | 3.44 |
| 10 | 2328 | 2328 | Yes | 2.82 |
| 11 | 2326 | 2326 | Yes | 2.74 |
| 12 | 1348 | 1348 | Yes | 2.56 |
| 13 | 1678 | 1678 | Yes | 3.09 |
| 14 | 888 | 888 | Yes | 4.57 |
| 15 | 1552 | 1552 | Yes | 2.9 |
| 16 | 1694 | 1694 | Yes | 2.27 |
| 17 | 1991 | 1991 | Yes | 5.53 |
| 18 | 2042 | 2042 | Yes | 2.8 |
| 19 | 1885 | 1885 | Yes | 3.38 |
| 20 | 1690 | 1690 | Yes | 3.1 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 |  | No | 43.41 |
| 2 | 60 |  | No | 48.47 |
| 3 | 38 |  | No | 40.13 |
| 4 | 49 |  | No | 49.4 |
| 5 | 42 |  | No | 34.18 |
| 6 | 39 |  | No | 29.24 |
| 7 | 64 |  | No | 26.42 |
| 8 | 69 |  | No | 38.96 |
| 9 | 46 |  | No | 65.52 |
| 10 | 66 |  | No | 41.39 |
| 11 | 66 |  | No | 55.33 |
| 12 | 45 | 67 | No | 18.89 |
| 13 | 50 | I’m sorry, but I can’t view the image. Could you please describe the digits or provide them in text form so I can count the zeros for you? | No | 11.27 |
| 14 | 58 |  | No | 57.39 |
| 15 | 48 | 67 | No | 26.33 |
| 16 | 52 |  | No | 23.9 |
| 17 | 59 |  | No | 62.9 |
| 18 | 37 |  | No | 36.04 |
| 19 | 46 |  | No | 32.99 |
| 20 | 44 |  | No | 34.21 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PDCHFLM | PDCHFLM | Yes | 11.63 |
| 2 | UEGODTQ | UEGODTQ | Yes | 9.94 |
| 3 | MEKPTGL | MEKPTGL | Yes | 11.7 |
| 4 | XUCJKBN | XUCJKBN | Yes | 10.87 |
| 5 | CJMOIGH | CJMOIGH | Yes | 11.9 |
| 6 | NPDTWBU | NPDTWBU | Yes | 23.11 |
| 7 | ILFMSZO | ILFMSZO | Yes | 3.56 |
| 8 | BXFVLEO | BXFVLEO | Yes | 9.08 |
| 9 | KVXULSP | KVXULSP | Yes | 6.47 |
| 10 | YQGEKZC | YQGEKZC | Yes | 7.9 |
| 11 | TKQRCMO | TKQRCMO | Yes | 13.6 |
| 12 | XSPKJTG | XSPKJTG | Yes | 11.81 |
| 13 | VSAUHLM | VSAUHLM | Yes | 6.13 |
| 14 | VDYONQK | VDYONQK | Yes | 6.59 |
| 15 | RZGXPCE | RZGXPCE | Yes | 8.44 |
| 16 | EGACNZD | EGACNZD | Yes | 4.92 |
| 17 | QJEWZHN | QJEWZHN | Yes | 4.83 |
| 18 | RJLGCKF | RJLGCKF | Yes | 4.72 |
| 19 | UGXTPQK | UGXTPQK | Yes | 6.0 |
| 20 | UWLACBZ | UWLACBZ | Yes | 7.77 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.6, 5.4] | 4.6 5.4 | Yes | 7.4 |
| 2 | [0.2, 9.8] |  | No | 21.07 |
| 3 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.93 |
| 4 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.28 |
| 5 | [3.4, 6.6] | 3.4 6.6 | Yes | 8.17 |
| 6 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.67 |
| 7 | [0.7, 9.3] | 0.7 9.3 | Yes | 13.46 |
| 8 | [1.0, 9.0] | 1.0 9.0 | Yes | 10.8 |
| 9 | [1.1, 8.9] | 1.1 8.9 | Yes | 8.64 |
| 10 | [4.6, 5.4] | 4.6 5.4 | Yes | 10.36 |
| 11 | [3.5, 6.5] | 3.5 6.5 | Yes | 11.96 |
| 12 | [2.5, 7.5] | 2.5 7.5 | Yes | 10.58 |
| 13 | [2.3, 7.7] | 2.3 7.7 | Yes | 10.19 |
| 14 | [1.1, 8.9] | 1.1 8.9 | Yes | 14.66 |
| 15 | [1.2, 8.8] | 1.2 8.8 | Yes | 11.4 |
| 16 | [0.1, 9.9] | 9.9 0.1 | Yes | 8.71 |
| 17 | [1.0, 9.0] | 1.0 9.0 | Yes | 9.47 |
| 18 | [2.6, 7.4] | 7.4 2.6 | Yes | 9.24 |
| 19 | [3.9, 6.1] | 3.9 6.1 | Yes | 8.58 |
| 20 | [3.0, 7.0] |  | No | 26.65 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VVZCZE6108L3 | VVZCZE6108L3 | Yes | 8.0 |
| 2 | UB0A5Z3U2OST | UB0A5Z3U20ST | No | 15.49 |
| 3 | U61P7M4V2LXV | U61P7M4V2LXV | Yes | 9.75 |
| 4 | 7ZZTT7KODGP7 | 7ZZTT7KODGP7 | Yes | 6.95 |
| 5 | ACKF7KN0TH7C | ACKF7KN0TH7C | Yes | 5.33 |
| 6 | GYS4NIAKMO0C | GYS4NIAKM00C | No | 11.52 |
| 7 | AWNGHU8GO17K | AWNGHU8GO17K | Yes | 23.6 |
| 8 | 0T6TNWFFRU0K |  | No | 63.99 |
| 9 | QK8VRHGG6ZBY | QK8VRHGG6ZBY | Yes | 18.66 |
| 10 | XY0182D2H8NK | XY0182D2H8NK | Yes | 3.75 |
| 11 | QHQXFIEDNK3O | QHOXFIEDNK3O | No | 15.76 |
| 12 | 7ETWMQ404715 | 7ETWMQ404715 | Yes | 3.31 |
| 13 | 4X527WU8M92C | 4X527WU8M92C | Yes | 3.13 |
| 14 | H5LUQTLNAKMI | H5LUQTLNAKMI | Yes | 5.94 |
| 15 | UYQ7V308IW9X | UYQ7V308IW9X | Yes | 18.11 |
| 16 | MBY501XCVOIQ | MBY501XCVOIQ | Yes | 12.55 |
| 17 | 7MJ80JDI0Z5E | 7MJ8QJDIOZ5E | No | 12.83 |
| 18 | J4MRNLLA4P1O | J4MRNLLA4P1O | Yes | 12.94 |
| 19 | FFXMF5VE0EOI | FFXMF5VE0EOI | Yes | 14.63 |
| 20 | WLZ9KBCZWYO7 | WLZ9KBCZWYO7 | Yes | 9.6 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 5.96 |
| 2 | 1440 | 1440 | Yes | 6.31 |
| 3 | 3 | 3 | Yes | 3.73 |
| 4 | 7 | 7 | Yes | 4.14 |
| 5 | 16 | 16 | Yes | 1.88 |
| 6 | 44 | 44 | Yes | 9.38 |
| 7 | 243 | 243 | Yes | 4.6 |
| 8 | 63 | 63 | Yes | 1.85 |
| 9 | 198 | 198 | Yes | 5.59 |
| 10 | 19 | 19 | Yes | 5.01 |
| 11 | 48 | 48 | Yes | 3.52 |
| 12 | 73 | 73 | Yes | 13.54 |
| 13 | 60 | 60 | Yes | 2.75 |
| 14 | 64 |  | No | 75.49 |
| 15 | 1 | 1 | Yes | 8.3 |
| 16 | 31 | 31 | Yes | 3.03 |
| 17 | 23 | 23 | Yes | 8.56 |
| 18 | 4096 |  | No | 57.65 |
| 19 | 5 | 5 | Yes | 6.31 |
| 20 | 26 |  | No | 48.48 |
