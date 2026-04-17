# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
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
| sudoku_game | 8960 | 30883 | 39843 | 9 | 11 | 23.21 | 464.32 |
| add_numbers | 4880 | 2079 | 6959 | 20 | 0 | 3.84 | 76.94 |
| counting_zeros | 7820 | 21300 | 29120 | 5 | 15 | 13.14 | 263.04 |
| task_decoding | 14260 | 7499 | 21759 | 20 | 0 | 6.64 | 133.02 |
| task_summation | 8180 | 14554 | 22734 | 20 | 0 | 10.08 | 201.7 |
| task_transcription | 5020 | 3057 | 8077 | 17 | 3 | 4.62 | 92.44 |
| task_sequences | 4141 | 7689 | 11830 | 18 | 2 | 6.71 | 134.25 |
| **TOTAL** | **53261** | **87061** | **140322** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 6 6 1 4 2 1 4 5 6 3 5 1 | 3 2 6 6 1 4 2 1 4 5 6 3 5 1 | Yes | 23.09 |
| 2 | 3 2 1 3 5 1 3 3 5 4 6 6 4 1 | 3 2 1 3 5 3 1 6 5 4 3 6 | No | 29.95 |
| 3 | 1 4 5 1 1 6 3 1 5 3 2 5 1 4 | 1 4 5 1 1 6 3 1 | No | 24.47 |
| 4 | 2 3 4 2 4 1 5 3 2 4 4 3 6 5 | 2 4 3 2 4 1 5 3 2 4 4 3 6 5 | No | 22.64 |
| 5 | 2 6 6 4 4 3 5 2 5 2 3 4 4 3 | 2 6 4 6 4 1 3 5 2 5 2 3 4 4 3 | No | 20.41 |
| 6 | 4 3 6 1 5 4 2 5 1 6 4 6 5 2 | 4 3 6 1 5 4 2 5 1 6 4 6 5 2 | Yes | 24.1 |
| 7 | 6 4 5 6 2 6 2 5 4 1 6 6 4 4 | 6 4 5 6 2 6 2 5 4 1 6 6 4 4 | Yes | 22.64 |
| 8 | 1 4 6 3 3 5 6 4 2 3 6 5 3 2 | 1 4 3 6 3 5 6 4 2 3 6 5 3 2 | No | 22.28 |
| 9 | 4 3 5 2 2 3 5 4 6 3 2 3 4 5 | 4 3 5 2 2 3 5 4 6 3 2 3 4 5 | Yes | 22.11 |
| 10 | 6 2 5 6 5 4 5 1 4 6 1 5 4 2 | 6 2 5 6 5 4 4 1 5 6 1 5 4 2 | No | 26.03 |
| 11 | 5 6 4 2 4 1 6 1 3 5 2 4 3 3 | 5 6 4 2 4 1 6 1 3 5 2 4 3 3 | Yes | 23.46 |
| 12 | 5 6 1 6 6 2 5 4 1 6 5 3 1 2 | 5 6 1 5 2 6 2 4 6 5 4 1 3 5 1 2 6 | No | 21.32 |
| 13 | 2 3 4 2 1 6 6 4 2 1 5 4 6 3 | 2 3 1 4 2 6 6 2 4 1 5 4 6 3 | No | 24.9 |
| 14 | 6 1 3 1 5 3 5 2 1 5 1 6 2 5 | 6 1 3 5 1 3 5 2 1 1 5 5 6 2 | No | 25.8 |
| 15 | 5 6 6 1 2 5 4 3 2 1 2 1 1 2 | 5 6 6 1 2 5 4 3 2 1 2 1 1 2 | Yes | 28.45 |
| 16 | 3 6 4 3 4 6 2 3 4 1 6 3 2 5 | 3 6 4 3 4 6 2 3 4 1 6 3 2 5 | Yes | 18.01 |
| 17 | 6 4 1 5 6 4 1 5 2 2 4 3 4 1 | 6 4 1 5 6 4 1 5 2 2 4 3 4 1 | Yes | 25.29 |
| 18 | 3 2 3 6 1 3 3 2 2 5 6 4 2 5 | 3 2 3 6 1 3 3 2 2 5 6 4 2 5 | Yes | 19.31 |
| 19 | 2 1 6 1 2 1 3 6 2 2 4 6 1 2 | 2 1 1 6 2 2 1 6 3 2 4 6 1 2 | No | 21.51 |
| 20 | 1 4 5 6 4 6 3 6 3 2 5 2 3 1 | 1 4 5 6 4 6 3 6 2 5 2 3 1 | No | 18.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1891 | 1891 | Yes | 3.33 |
| 2 | 1537 | 1537 | Yes | 2.98 |
| 3 | 1374 | 1374 | Yes | 5.81 |
| 4 | 2036 | 2036 | Yes | 2.91 |
| 5 | 2218 | 2218 | Yes | 2.96 |
| 6 | 1758 | 1758 | Yes | 3.94 |
| 7 | 1696 | 1696 | Yes | 3.03 |
| 8 | 2261 | 2261 | Yes | 7.12 |
| 9 | 1120 | 1120 | Yes | 3.94 |
| 10 | 1964 | 1964 | Yes | 3.62 |
| 11 | 1946 | 1946 | Yes | 3.94 |
| 12 | 1786 | 1786 | Yes | 3.35 |
| 13 | 1366 | 1366 | Yes | 4.37 |
| 14 | 1556 | 1556 | Yes | 3.15 |
| 15 | 1299 | 1299 | Yes | 5.53 |
| 16 | 897 | 897 | Yes | 2.52 |
| 17 | 2554 | 2554 | Yes | 3.89 |
| 18 | 1799 | 1799 | Yes | 3.11 |
| 19 | 1437 | 1437 | Yes | 2.9 |
| 20 | 2671 | 2671 | Yes | 4.46 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 38 | 38 | Yes | 11.37 |
| 2 | 75 | 69 | No | 12.55 |
| 3 | 55 | 54 | No | 15.37 |
| 4 | 53 | 41 | No | 13.17 |
| 5 | 68 | 67 | No | 11.66 |
| 6 | 38 | 38 | Yes | 12.58 |
| 7 | 55 | 54 | No | 12.05 |
| 8 | 64 | 63 | No | 16.34 |
| 9 | 72 | 71 | No | 11.31 |
| 10 | 47 | 47 | Yes | 12.46 |
| 11 | 52 | 54 | No | 16.57 |
| 12 | 45 | 45 | Yes | 10.71 |
| 13 | 54 | 56 | No | 12.05 |
| 14 | 50 | 48 | No | 10.35 |
| 15 | 75 | 73 | No | 13.82 |
| 16 | 69 | 69 | Yes | 16.94 |
| 17 | 49 | 48 | No | 13.74 |
| 18 | 73 | 74 | No | 14.32 |
| 19 | 50 | 48 | No | 13.4 |
| 20 | 60 | 61 | No | 11.97 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GLYVWFZ | GLYVWFZ | Yes | 6.68 |
| 2 | MYFZSIJ | MYFZSIJ | Yes | 7.15 |
| 3 | VMEXBQP | VMEXBQP | Yes | 6.49 |
| 4 | BGFOALN | BGFOALN | Yes | 6.56 |
| 5 | CHXYJFD | CHXYJFD | Yes | 5.68 |
| 6 | PZYNDVH | PZYNDVH | Yes | 5.95 |
| 7 | TZLGVNH | TZLGVNH | Yes | 5.51 |
| 8 | NRMWBIC | NRMWBIC | Yes | 5.23 |
| 9 | PFCQTHN | PFCQTHN | Yes | 5.09 |
| 10 | ERIBOAD | ERIBOAD | Yes | 6.16 |
| 11 | KGVPXNM | KGVPXNM | Yes | 5.98 |
| 12 | SKLQHVY | SKLQHVY | Yes | 8.08 |
| 13 | DXNJFHU | DXNJFHU | Yes | 8.47 |
| 14 | CTVDOYG | CTVDOYG | Yes | 9.29 |
| 15 | XQSYLUP | XQSYLUP | Yes | 9.15 |
| 16 | ZLSDMKN | ZLSDMKN | Yes | 6.68 |
| 17 | UVXFREA | UVXFREA | Yes | 6.06 |
| 18 | STXIRDW | STXIRDW | Yes | 6.59 |
| 19 | WQIPJRM | WQIPJRM | Yes | 5.77 |
| 20 | EITGQLJ | EITGQLJ | Yes | 6.25 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 3.5 6.5 | Yes | 10.22 |
| 2 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.04 |
| 3 | [1.9, 8.1] | 1.9 8.1 | Yes | 11.09 |
| 4 | [1.4, 8.6] | 1.4 8.6 | Yes | 12.28 |
| 5 | [0.3, 9.7] | 9.7 0.3 | Yes | 10.63 |
| 6 | [0.9, 9.1] | 9.1 0.9 | Yes | 8.96 |
| 7 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.67 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 11.98 |
| 9 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.36 |
| 10 | [0.7, 9.3] | 0.7 9.3 | Yes | 14.29 |
| 11 | [5.0, 5.0] | 5.0 5.0 | Yes | 10.37 |
| 12 | [3.2, 6.8] | 6.8 3.2 | Yes | 9.19 |
| 13 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.03 |
| 14 | [0.2, 9.8] | 0.2 9.8 | Yes | 9.91 |
| 15 | [2.1, 7.9] | 7.9 2.1 | Yes | 10.94 |
| 16 | [3.3, 6.7] | 6.7 3.3 | Yes | 8.1 |
| 17 | [4.7, 5.3] | 4.7 5.3 | Yes | 7.72 |
| 18 | [2.3, 7.7] | 2.3 7.7 | Yes | 9.81 |
| 19 | [4.8, 5.2] | 5.2 4.8 | Yes | 11.03 |
| 20 | [3.2, 6.8] | 3.2 6.8 | Yes | 7.91 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | P7RIGISXZOMJ | P7RIGISXZOMJ | Yes | 8.49 |
| 2 | 8G82RE6YW4WE | 8G82RE6YW4WE | Yes | 4.05 |
| 3 | E18B7FFH0870 | E18B7FFH0870 | Yes | 3.52 |
| 4 | XM3RGBYG1FPT | XM3RGBYG1FPT | Yes | 3.89 |
| 5 | 0MMZZO63I32Q | 0MMZZO63I32Q | Yes | 4.22 |
| 6 | GKLQFOFASUPK | GKLQFOFASUPK | Yes | 4.61 |
| 7 | 6GZ8HYNV4O9W | 6GZ8HYNV4O9W | Yes | 4.04 |
| 8 | X6NHVEK4XG02 | X6NHVEK4XG02 | Yes | 3.85 |
| 9 | 98NWIC3UD7NC | 98NWIC3UD7NC | Yes | 3.72 |
| 10 | Y8T4WTW1GMED | Y8T4WTW1GMED | Yes | 4.18 |
| 11 | CK0TRN0JCVMP | CK0TBRN0JCVMP | No | 6.19 |
| 12 | R9MPL2G4MJSL | R9MPL2G1MJSL | No | 4.07 |
| 13 | 6N2HRV1UI8Z3 | 6N2HRV1UI8Z3 | Yes | 4.19 |
| 14 | 8E6G1F6XPLZP | 8E6G1F6XPLZP | Yes | 4.45 |
| 15 | 8T4SKPX0PR25 | 8T4SKPX0PR25 | Yes | 5.72 |
| 16 | 7W5NZ6LLJO8F | 7W5NZ6LLJO8F | Yes | 3.94 |
| 17 | BFC6BTWZ60LX | BFC8BTWZG0LX | No | 5.47 |
| 18 | 9B4D32BG14X5 | 9B4D32BG14X5 | Yes | 3.8 |
| 19 | KUGGG03C51TA | KUGGG03C51TA | Yes | 5.26 |
| 20 | SK2TM05DMR3E | SK2TM05DMR3E | Yes | 4.7 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 21 | No | 12.01 |
| 2 | 60 | 60 | Yes | 8.62 |
| 3 | 3 | 3 | Yes | 6.49 |
| 4 | 67 | 67 | Yes | 3.96 |
| 5 | 48 | 48 | Yes | 4.85 |
| 6 | 23 | 23 | Yes | 5.76 |
| 7 | 44 | 44 | Yes | 7.96 |
| 8 | 26 | 26 | Yes | 9.15 |
| 9 | 4 | 4 | Yes | 6.68 |
| 10 | 36 | 36 | Yes | 4.49 |
| 11 | 4 | 4 | Yes | 5.36 |
| 12 | 4096 | 1048576 | No | 12.47 |
| 13 | 243 | 243 | Yes | 4.85 |
| 14 | 39 | 39 | Yes | 5.75 |
| 15 | 73 | 73 | Yes | 5.73 |
| 16 | 9 | 9 | Yes | 6.54 |
| 17 | 63 | 63 | Yes | 6.06 |
| 18 | 28 | 28 | Yes | 4.6 |
| 19 | 1 | 1 | Yes | 8.12 |
| 20 | 7 | 7 | Yes | 4.79 |
