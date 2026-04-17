# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
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
| sudoku_game | 8740 | 28164 | 36904 | 1 | 19 | 11.62 | 232.57 |
| add_numbers | 4660 | 3444 | 8104 | 20 | 0 | 2.81 | 56.36 |
| counting_zeros | 7600 | 18898 | 26498 | 0 | 20 | 7.90 | 158.34 |
| task_decoding | 14040 | 11421 | 25461 | 16 | 4 | 5.13 | 102.86 |
| task_summation | 7960 | 16821 | 24781 | 20 | 0 | 6.69 | 133.91 |
| task_transcription | 4792 | 4282 | 9074 | 13 | 7 | 3.08 | 61.76 |
| task_sequences | 3920 | 4967 | 8887 | 20 | 0 | 2.88 | 57.68 |
| **TOTAL** | **51712** | **87997** | **139709** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 1 6 6 5 3 1 5 1 5 4 6 2 | 5 1 4 6 6 8 3 1 5 1 5 6 2** | No | 9.44 |
| 2 | 2 6 6 4 2 5 3 6 4 1 2 4 1 5 | 2 6 6 4 2 5 3 4 4 1 2 4 6 5 | No | 13.49 |
| 3 | 5 6 4 3 1 6 1 2 5 6 4 3 4 6 | 5 6 4 3 6 1 2 5 4 3 4 6 | No | 11.82 |
| 4 | 4 2 5 3 6 5 2 4 6 2 5 5 2 1 | 2 6 5 3 6 5 4 2 2 6 5 2 1 | No | 12.57 |
| 5 | 3 5 2 4 1 6 5 4 5 3 6 2 1 2 | 3 5 2 4 1 6 4 3 5 6 2 1 2** | No | 10.25 |
| 6 | 3 4 1 2 3 3 6 6 3 2 1 5 4 3 | 3 4 1 2 3 6 3 2 3 6 3 2 1 6 3 2 1 5 4 3 | No | 13.0 |
| 7 | 5 2 1 5 2 6 5 6 2 4 4 1 1 3 | 5 2 1 2 5 6 5 6 2 4 4 1 1 3** | No | 11.85 |
| 8 | 4 3 5 4 6 2 5 4 2 3 2 3 5 6 | 4 3 5 4 6 2 5 4 2 3 2 3 5 6** | No | 11.98 |
| 9 | 5 4 1 2 3 1 2 5 6 1 2 2 3 3 | 4 5 1 2 3 1 2 5 6 2 1 3** | No | 11.52 |
| 10 | 3 4 2 6 1 4 6 6 4 3 1 6 4 1 | 6 3 2 4 1 4 6 3 4 5 3 1 6 4 1** | No | 10.28 |
| 11 | 6 6 2 5 3 6 4 6 1 5 4 6 2 6 | 6 6 2 5 3 6 4 1 5 4 6 2 | No | 10.02 |
| 12 | 5 1 6 4 2 5 3 1 4 6 2 4 2 1 | 5 1 6 4 2 1 2 5 3 1 4 6 2 4 2 1 | No | 13.75 |
| 13 | 2 5 3 4 5 1 6 5 2 3 6 5 1 5 | 3 5 1 4 2 5 1 6 5 1 2 3 6 4 | No | 17.43 |
| 14 | 1 2 5 2 4 6 3 3 2 4 6 3 6 5 | 2 1 5 6 3 4 2 3 2 4 6 6 5 | No | 8.82 |
| 15 | 5 1 6 3 4 6 2 3 2 5 5 1 4 2 | 5 1 6 3 2 6 3 4 4 5 5 2 4 1** | No | 9.68 |
| 16 | 4 2 6 1 3 1 3 2 6 4 1 3 6 1 | 4 2 6 1 3 1 2 6 4 1 3 6 1 | No | 11.05 |
| 17 | 2 4 3 5 4 1 2 1 6 6 4 5 2 6 | 2 4 3 5 4 1 2 1 6 6 4 5 2 6 | Yes | 9.54 |
| 18 | 1 5 3 4 6 2 5 6 4 1 2 2 6 5 | 5 1 3 6 4 2 6 4 1 2 2 6 5** | No | 12.96 |
| 19 | 3 3 5 2 6 6 2 3 4 2 4 3 6 2 | 3 2 3 6 5 6 2 3 4 2 4 3 6 2 | No | 12.13 |
| 20 | 1 6 3 4 1 2 6 2 5 6 2 5 3 6 | 1 6 3 2 1 6 4 5 2 6 2 3 6 5 1 | No | 10.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1834 | 1834 | Yes | 3.06 |
| 2 | 1514 | 1514 | Yes | 2.54 |
| 3 | 1765 | 1765 | Yes | 2.77 |
| 4 | 1055 | 1055 | Yes | 2.6 |
| 5 | 1908 | 1908 | Yes | 3.21 |
| 6 | 1368 | 1368 | Yes | 2.45 |
| 7 | 975 | 975 | Yes | 2.87 |
| 8 | 1770 | 1770 | Yes | 3.1 |
| 9 | 1181 | 1181 | Yes | 2.11 |
| 10 | 1934 | 1934 | Yes | 3.78 |
| 11 | 2317 | 2317 | Yes | 3.5 |
| 12 | 1903 | 1903 | Yes | 2.76 |
| 13 | 796 | 796 | Yes | 2.43 |
| 14 | 1797 | 1797 | Yes | 2.41 |
| 15 | 1644 | 1644 | Yes | 2.55 |
| 16 | 1253 | 1253 | Yes | 2.45 |
| 17 | 1392 | 1392 | Yes | 2.52 |
| 18 | 1806 | 1806 | Yes | 3.25 |
| 19 | 2094 | 2094 | Yes | 3.5 |
| 20 | 1327 | 1327 | Yes | 2.43 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 75 | 66 | No | 8.84 |
| 2 | 57 | 47 | No | 11.62 |
| 3 | 43 | 45 | No | 6.53 |
| 4 | 73 | 65 | No | 6.72 |
| 5 | 57 | 58 | No | 8.14 |
| 6 | 42 | 41 | No | 7.1 |
| 7 | 71 | 70 | No | 9.08 |
| 8 | 72 | 68 | No | 6.78 |
| 9 | 47 | 44 | No | 7.96 |
| 10 | 65 | 61 | No | 7.3 |
| 11 | 74 | 73 | No | 6.8 |
| 12 | 46 | 48 | No | 8.24 |
| 13 | 69 | 67 | No | 7.8 |
| 14 | 55 | 49 | No | 6.86 |
| 15 | 72 | 74 | No | 7.68 |
| 16 | 57 | 51 | No | 6.65 |
| 17 | 56 | 54 | No | 7.83 |
| 18 | 45 | 41 | No | 12.57 |
| 19 | 49 | 47 | No | 7.38 |
| 20 | 39 | 43 | No | 6.15 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JENBYWT | JENBYWT | Yes | 4.91 |
| 2 | ABYFDJO | ABYFDJО | No | 5.75 |
| 3 | YFZRCDW | YFZRCDW | Yes | 6.19 |
| 4 | AXCYMVW | AXCYMVW | Yes | 4.39 |
| 5 | ZOFJNXL | ZOFJNXL | Yes | 5.67 |
| 6 | YEWBZRT | YEWBZZRT | No | 5.09 |
| 7 | JTGRFNP | JTGRFNP | Yes | 4.34 |
| 8 | HJQISVD | HJQISVSD | No | 4.87 |
| 9 | LADSQKR | LADSQKR | Yes | 4.7 |
| 10 | KDGQIRE | KDGQIRE | Yes | 4.23 |
| 11 | WHETKOV | WHETKOV | Yes | 5.06 |
| 12 | RTHEZPM | RTHEZPM | Yes | 4.2 |
| 13 | RZIKMQP | RZIKMQP | Yes | 3.95 |
| 14 | RGYIDPJ | RGYIDPJ | Yes | 7.87 |
| 15 | ICOXTGJ | ICOXDGJ | No | 7.06 |
| 16 | JOEUMDA | JOEUMDA | Yes | 4.83 |
| 17 | AQDLVHW | AQDLVHW | Yes | 4.34 |
| 18 | QVKZCJW | QVKZCJW | Yes | 4.41 |
| 19 | DEPNAQJ | DEPNAQJ | Yes | 4.72 |
| 20 | XAOCPET | XAOCPET | Yes | 6.1 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.83 |
| 2 | [1.0, 9.0] | 9.0 1.0 | Yes | 6.65 |
| 3 | [3.3, 6.7] | 6.7 3.3 | Yes | 6.05 |
| 4 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.77 |
| 5 | [2.4, 7.6] | 2.4 7.6 | Yes | 7.97 |
| 6 | [5.0, 5.0] | 5.0 5.0 | Yes | 7.13 |
| 7 | [1.5, 8.5] | 1.5 8.5 | Yes | 6.38 |
| 8 | [2.7, 7.3] | 2.7 7.3 | Yes | 5.87 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.72 |
| 10 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.4 |
| 11 | [1.5, 8.5] | 8.5 1.5 | Yes | 6.61 |
| 12 | [3.6, 6.4] | 6.4 3.6 | Yes | 6.97 |
| 13 | [1.1, 8.9] | 8.9 1.1 | Yes | 7.08 |
| 14 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.56 |
| 15 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.61 |
| 16 | [0.7, 9.3] | 0.7 9.3 | Yes | 6.39 |
| 17 | [1.8, 8.2] | 1.8 8.2 | Yes | 7.54 |
| 18 | [0.5, 9.5] | 9.5 0.5 | Yes | 6.9 |
| 19 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.56 |
| 20 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.78 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 0KQKQ8UFG69K | 0KOK08UFG69K | No | 5.21 |
| 2 | R0ESSRW18QLT | R0ESSRW18QLT | Yes | 3.16 |
| 3 | 5J3A7PD88EX9 | 5J3A7PD88EX9 | Yes | 2.8 |
| 4 | 2U6KEYCL5CKE | 2U6KEYCL5CKE | Yes | 3.02 |
| 5 | MYY0KO5I29ZY | MYY0KO5I29ZY | Yes | 4.51 |
| 6 | CX7HWRPH24ES | CX7HWRBPH24ES | No | 2.73 |
| 7 | 320QNQO0LJ6K | 320QNQ00LJ6K | No | 3.66 |
| 8 | C73E6UP24YUI | C73E6UP24YUI | Yes | 2.83 |
| 9 | F2JVFGZ1885O | F2JVFGZ1885O | Yes | 2.87 |
| 10 | SYUP45NVCM0K | SYUP45NVCMOK | No | 2.98 |
| 11 | I6MUEWT07O20 | I6MUEWT07O20 | Yes | 3.49 |
| 12 | HVYT0SV8BSM0 | HVYT0SV8BSM0 | Yes | 2.84 |
| 13 | 13JVM85ANJ3V | 13JVM35ANJ3V | No | 2.68 |
| 14 | UAG4HQWGXDEF | UAG4HQWGXDEF | Yes | 2.04 |
| 15 | 7XJLKP5CX839 | 7XJLKP5CX839 | Yes | 2.9 |
| 16 | 3YG5B49VGFLW | 3YG5B49VGFLW | Yes | 2.41 |
| 17 | 33T9TB2YYPUA | 33T9TB2YYPUA | Yes | 2.91 |
| 18 | PQQYLLUEJZ8R | PQQYLLUEJZ3R | No | 2.89 |
| 19 | WIAEBVO50J71 | WIAEBVO50J71 | Yes | 2.9 |
| 20 | 64BD7ILLCE8D | 64BD7ILLCE3D | No | 2.83 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 65 | Yes | 2.84 |
| 2 | 7 | 7 | Yes | 2.56 |
| 3 | 63 | 63 | Yes | 2.87 |
| 4 | 16 | 16 | Yes | 3.16 |
| 5 | 64 | 64 | Yes | 3.01 |
| 6 | 60 | 60 | Yes | 3.8 |
| 7 | 4 | 4 | Yes | 2.28 |
| 8 | 44 | 44 | Yes | 4.15 |
| 9 | 60 | 60 | Yes | 2.29 |
| 10 | 793 | 793 | Yes | 1.99 |
| 11 | 198 | 198 | Yes | 4.2 |
| 12 | 26 | 26 | Yes | 2.45 |
| 13 | 9 | 9 | Yes | 2.57 |
| 14 | 28 | 28 | Yes | 2.23 |
| 15 | 1440 | 1440 | Yes | 3.04 |
| 16 | 19 | 19 | Yes | 2.35 |
| 17 | 73 | 73 | Yes | 2.41 |
| 18 | 48 | 48 | Yes | 2.4 |
| 19 | 39 | 39 | Yes | 3.62 |
| 20 | 36 | 36 | Yes | 3.46 |
