# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 7940 | 40960 | 48900 | 0 | 20 | 66.76 | 1335.43 |
| add_numbers | 6960 | 4334 | 11294 | 20 | 0 | 7.21 | 144.23 |
| counting_zeros | 7020 | 40960 | 47980 | 0 | 20 | 72.83 | 1456.93 |
| task_decoding | 10280 | 16576 | 26856 | 20 | 0 | 14.67 | 293.57 |
| task_summation | 7280 | 24394 | 31674 | 19 | 1 | 18.04 | 360.94 |
| task_transcription | 7040 | 11594 | 18634 | 18 | 2 | 13.15 | 263.12 |
| task_sequences | 2901 | 11432 | 14333 | 18 | 2 | 15.59 | 311.87 |
| **TOTAL** | **49421** | **150250** | **199671** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 1 3 4 3 5 2 1 4 2 3 6 5 |  | No | 59.89 |
| 2 | 4 5 2 6 1 5 6 4 2 6 5 6 5 6 |  | No | 57.78 |
| 3 | 5 3 2 1 3 5 6 1 4 5 4 6 2 3 |  | No | 53.23 |
| 4 | 5 1 2 3 6 4 5 4 2 4 1 6 2 3 |  | No | 57.74 |
| 5 | 3 5 2 5 3 6 1 3 4 2 6 2 5 3 |  | No | 61.74 |
| 6 | 3 3 5 2 4 5 3 5 6 2 1 1 4 5 |  | No | 41.17 |
| 7 | 3 4 1 3 5 2 6 3 6 6 3 2 6 3 |  | No | 66.52 |
| 8 | 1 4 6 5 3 1 4 2 4 1 6 5 6 3 |  | No | 70.62 |
| 9 | 1 2 3 1 4 3 5 6 3 5 1 1 2 5 |  | No | 59.56 |
| 10 | 5 2 3 3 2 5 1 2 3 2 4 1 5 2 |  | No | 81.56 |
| 11 | 5 4 3 6 3 6 1 5 3 2 6 5 4 2 |  | No | 62.28 |
| 12 | 5 1 3 2 6 6 3 2 5 6 1 5 6 4 |  | No | 64.78 |
| 13 | 4 6 6 2 4 2 1 2 3 5 1 4 2 3 |  | No | 66.5 |
| 14 | 6 2 6 4 2 3 1 1 6 2 3 1 4 2 |  | No | 84.53 |
| 15 | 6 4 6 2 4 3 3 2 2 5 4 3 3 6 |  | No | 66.46 |
| 16 | 4 1 5 6 3 1 2 6 3 4 6 6 3 1 |  | No | 78.78 |
| 17 | 6 3 2 6 1 1 2 6 3 5 1 4 2 3 |  | No | 72.79 |
| 18 | 1 4 5 3 1 4 4 6 3 5 1 4 3 6 |  | No | 78.1 |
| 19 | 5 4 1 5 4 6 6 3 5 2 1 6 2 6 |  | No | 66.58 |
| 20 | 5 3 5 4 2 4 6 2 3 5 2 3 5 2 |  | No | 84.59 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1604 | 1604 | Yes | 7.73 |
| 2 | 1888 | 1888 | Yes | 6.97 |
| 3 | 2027 | 2027 | Yes | 7.2 |
| 4 | 1576 | 1576 | Yes | 6.35 |
| 5 | 1501 | 1501 | Yes | 5.02 |
| 6 | 1542 | 1542 | Yes | 6.06 |
| 7 | 1191 | 1191 | Yes | 5.84 |
| 8 | 1873 | 1873 | Yes | 9.18 |
| 9 | 1384 | 1384 | Yes | 8.0 |
| 10 | 1379 | 1379 | Yes | 8.48 |
| 11 | 1960 | 1960 | Yes | 9.3 |
| 12 | 1895 | 1895 | Yes | 8.9 |
| 13 | 1512 | 1512 | Yes | 6.79 |
| 14 | 2250 | 2250 | Yes | 6.0 |
| 15 | 1638 | 1638 | Yes | 6.83 |
| 16 | 1199 | 1199 | Yes | 8.32 |
| 17 | 1598 | 1598 | Yes | 5.74 |
| 18 | 1842 | 1842 | Yes | 7.56 |
| 19 | 1362 | 1362 | Yes | 6.65 |
| 20 | 1841 | 1841 | Yes | 7.21 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 68 |  | No | 58.06 |
| 2 | 63 |  | No | 82.03 |
| 3 | 52 |  | No | 64.47 |
| 4 | 66 |  | No | 74.84 |
| 5 | 69 |  | No | 75.38 |
| 6 | 58 |  | No | 85.09 |
| 7 | 54 |  | No | 80.64 |
| 8 | 47 |  | No | 57.17 |
| 9 | 53 |  | No | 75.34 |
| 10 | 63 |  | No | 80.87 |
| 11 | 42 |  | No | 74.14 |
| 12 | 61 |  | No | 77.48 |
| 13 | 59 |  | No | 92.11 |
| 14 | 61 |  | No | 77.08 |
| 15 | 38 |  | No | 64.21 |
| 16 | 43 |  | No | 68.22 |
| 17 | 63 |  | No | 70.72 |
| 18 | 69 |  | No | 69.26 |
| 19 | 65 |  | No | 59.48 |
| 20 | 48 |  | No | 70.02 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XIHFZAQ | XIHFZAQ | Yes | 5.22 |
| 2 | JWYILUO | JWYILUO | Yes | 8.24 |
| 3 | RAJCFIW | RAJCFIW | Yes | 12.09 |
| 4 | KPIVJWN | KPIVJWN | Yes | 11.6 |
| 5 | UKNDSAG | UKNDSAG | Yes | 23.13 |
| 6 | SNRXBYM | SNRXBYM | Yes | 8.7 |
| 7 | XUVPSQM | XUVPSQM | Yes | 9.23 |
| 8 | BIZCLJR | BIZCLJR | Yes | 15.07 |
| 9 | QALNIKO | QALNIKO | Yes | 9.75 |
| 10 | AWOKEXT | AWOKEXT | Yes | 13.67 |
| 11 | OCWMFNK | OCWMFNK | Yes | 10.72 |
| 12 | BZTFMIC | BZTFMIC | Yes | 33.82 |
| 13 | NWARUID | NWARUID | Yes | 26.99 |
| 14 | SKLRNTD | SKLRNTD | Yes | 21.58 |
| 15 | FWLTQNK | FWLTQNK | Yes | 10.02 |
| 16 | PUSDCME | PUSDCME | Yes | 19.69 |
| 17 | AYKCLNM | AYKCLNM | Yes | 14.6 |
| 18 | JIXZGWB | JIXZGWB | Yes | 10.43 |
| 19 | IXGBSVW | IXGBSVW | Yes | 14.54 |
| 20 | ZRIXMYB | ZRIXMYB | Yes | 14.27 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 1.5 8.5 | Yes | 22.65 |
| 2 | [4.7, 5.3] | 5.3 4.7 | Yes | 16.44 |
| 3 | [4.4, 5.6] | 5.6 4.4 | Yes | 23.29 |
| 4 | [4.0, 6.0] | 4.0 6.0 | Yes | 12.6 |
| 5 | [3.9, 6.1] | 6.1 3.9 | Yes | 12.51 |
| 6 | [3.1, 6.9] | 3.1 6.9 | Yes | 18.3 |
| 7 | [2.9, 7.1] | 2.9 7.1 | Yes | 13.93 |
| 8 | [2.2, 7.8] | 2.2 7.8 | Yes | 16.74 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 16.48 |
| 10 | [1.4, 8.6] | 8.6 1.4 | Yes | 13.72 |
| 11 | [3.6, 6.4] | 3.6 6.4 | Yes | 17.53 |
| 12 | [4.1, 5.9] | 4.1 5.9 | Yes | 15.5 |
| 13 | [4.6, 5.4] | 4.6 5.4 | Yes | 13.34 |
| 14 | [3.5, 6.5] | 6.5 3.5 | Yes | 13.5 |
| 15 | [3.8, 6.2] | 3.8 6.2 | Yes | 15.77 |
| 16 | [0.2, 9.8] | 0.2 9.8 | Yes | 21.97 |
| 17 | [3.1, 6.9] | 3.1 6.9 | Yes | 15.59 |
| 18 | [0.7, 9.3] | 0.7 9.3 | Yes | 18.14 |
| 19 | [1.6, 8.4] | 8.4 1.6 | Yes | 20.6 |
| 20 | [4.4, 5.6] |  | No | 42.14 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NHS6O61U9882 | NHS6061U9882 | No | 10.6 |
| 2 | BD92MWVAIPO5 | BD92MWVAIP05 | No | 22.39 |
| 3 | OJRYNIZD922Z | OJRYNIZD922Z | Yes | 11.15 |
| 4 | DSM3YQ73A69A | DSM3YQ73A69A | Yes | 6.44 |
| 5 | RXWJMEVZHL1C | RXWJMEVZHL1C | Yes | 7.01 |
| 6 | AXEZ2YTN1L47 | AXEZ2YTN1L47 | Yes | 5.63 |
| 7 | 2G32GJVW5UXK | 2G32GJVW5UXK | Yes | 12.54 |
| 8 | X2ROPZT0V4CD | X2ROPZT0V4CD | Yes | 8.6 |
| 9 | 1L5LXJQC6J2S | 1L5LXJQC6J2S | Yes | 11.33 |
| 10 | BYOKXUKIUG3A | BYOKXUKIUG3A | Yes | 9.63 |
| 11 | 1T7L6JXV5CGY | 1T7L6JXV5CGY | Yes | 10.46 |
| 12 | UXZFZVJY7R0W | UXZFZVJY7R0W | Yes | 13.09 |
| 13 | PI34URUDDAHO | PI34URUDDAHO | Yes | 29.35 |
| 14 | 0N8MBGYEA0QL | 0N8MBGYEA0QL | Yes | 13.82 |
| 15 | R3XTSXYEUZ4A | R3XTSXYEUZ4A | Yes | 10.29 |
| 16 | 8T2RKJTX570H | 8T2RKJTX570H | Yes | 12.22 |
| 17 | PPEV4GMG08VB | PPEV4GMG08VB | Yes | 10.82 |
| 18 | 4CGTOT3W7G36 | 4CGTOT3W7G36 | Yes | 18.75 |
| 19 | EQKNF7OR9ZNI | EQKNF7OR9ZNI | Yes | 11.45 |
| 20 | PV58Q22J2WHB | PV58Q22J2WHB | Yes | 27.44 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 18.69 |
| 2 | 67 | 67 | Yes | 4.14 |
| 3 | 4096 |  | No | 52.12 |
| 4 | 28 | 28 | Yes | 9.18 |
| 5 | 3 | 3 | Yes | 7.48 |
| 6 | 60 | 60 | Yes | 6.0 |
| 7 | 7680 | 7680 | Yes | 6.72 |
| 8 | 44 | 44 | Yes | 14.79 |
| 9 | 36 | 36 | Yes | 8.12 |
| 10 | 9 | 9 | Yes | 6.27 |
| 11 | 5 | 5 | Yes | 6.53 |
| 12 | 20 | 20 | Yes | 41.78 |
| 13 | 1440 | 1440 | Yes | 11.16 |
| 14 | 6 | 6 | Yes | 9.26 |
| 15 | 65 | 65 | Yes | 6.68 |
| 16 | 26 |  | No | 64.28 |
| 17 | 39 | 39 | Yes | 8.82 |
| 18 | 9 | 9 | Yes | 11.45 |
| 19 | 793 | 793 | Yes | 11.44 |
| 20 | 16 | 16 | Yes | 6.97 |
