# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 8490 | 40570 | 49060 | 0 | 20 | 63.18 | 1263.77 |
| add_numbers | 7120 | 1336 | 8456 | 20 | 0 | 4.33 | 86.66 |
| counting_zeros | 7180 | 40960 | 48140 | 0 | 20 | 69.65 | 1393.39 |
| task_decoding | 10440 | 6273 | 16713 | 20 | 0 | 7.57 | 151.53 |
| task_summation | 7440 | 8784 | 16224 | 20 | 0 | 9.28 | 185.83 |
| task_transcription | 7200 | 3450 | 10650 | 16 | 4 | 4.75 | 95.19 |
| task_sequences | 3072 | 6464 | 9536 | 19 | 1 | 7.89 | 157.83 |
| **TOTAL** | **50942** | **107837** | **158779** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 5 4 4 1 3 2 1 4 3 5 5 3 6 |  | No | 43.0 |
| 2 | 6 2 3 1 4 2 6 3 2 6 1 5 6 1 |  | No | 66.42 |
| 3 | 4 5 3 2 6 4 5 6 6 5 2 6 4 1 |  | No | 62.53 |
| 4 | 2 3 5 4 3 1 6 5 4 3 1 6 4 3 |  | No | 75.62 |
| 5 | 3 2 6 1 2 5 6 2 2 3 6 1 1 4 |  | No | 39.12 |
| 6 | 6 4 2 3 6 1 2 5 2 5 4 3 5 2 |  | No | 89.88 |
| 7 | 6 1 1 3 5 6 3 3 6 1 5 2 4 3 |  | No | 57.15 |
| 8 | 3 2 6 5 6 1 1 2 5 6 4 3 4 2 |  | No | 53.63 |
| 9 | 4 1 3 6 5 3 6 1 3 2 4 1 5 3 |  | No | 99.69 |
| 10 | 4 6 1 4 1 5 6 2 5 5 4 1 6 1 |  | No | 65.11 |
| 11 | 6 1 3 2 2 4 3 3 6 5 5 2 1 4 |  | No | 66.43 |
| 12 | 6 5 1 5 6 4 5 1 4 2 3 3 5 6 |  | No | 53.6 |
| 13 | 6 1 1 6 2 1 2 6 5 1 3 2 5 4 |  | No | 52.71 |
| 14 | 3 2 5 4 6 1 3 2 6 1 5 3 5 3 |  | No | 76.54 |
| 15 | 6 4 5 6 2 5 1 5 1 3 6 1 4 2 |  | No | 42.02 |
| 16 | 6 4 2 5 4 5 6 3 2 5 6 4 2 3 |  | No | 51.66 |
| 17 | 4 3 4 5 1 2 4 5 3 3 4 3 4 2 |  | No | 63.05 |
| 18 | 3 6 5 4 1 6 3 1 4 3 5 2 1 3 |  | No | 72.14 |
| 19 | 5 4 2 2 5 1 1 4 6 4 5 3 5 3 |  | No | 62.39 |
| 20 | 2 1 5 3 3 2 4 5 4 2 3 4 5 1 |  | No | 70.88 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1283 | 1283 | Yes | 4.57 |
| 2 | 2200 | 2200 | Yes | 4.19 |
| 3 | 1065 | 1065 | Yes | 3.86 |
| 4 | 1691 | 1691 | Yes | 3.3 |
| 5 | 1451 | 1451 | Yes | 3.29 |
| 6 | 2384 | 2384 | Yes | 3.63 |
| 7 | 1701 | 1701 | Yes | 5.73 |
| 8 | 1659 | 1659 | Yes | 3.76 |
| 9 | 1928 | 1928 | Yes | 3.51 |
| 10 | 1184 | 1184 | Yes | 3.72 |
| 11 | 2388 | 2388 | Yes | 3.59 |
| 12 | 2032 | 2032 | Yes | 3.3 |
| 13 | 1870 | 1870 | Yes | 7.51 |
| 14 | 2235 | 2235 | Yes | 4.38 |
| 15 | 2012 | 2012 | Yes | 3.07 |
| 16 | 2001 | 2001 | Yes | 4.21 |
| 17 | 1594 | 1594 | Yes | 3.47 |
| 18 | 1642 | 1642 | Yes | 4.22 |
| 19 | 2485 | 2485 | Yes | 3.76 |
| 20 | 1304 | 1304 | Yes | 9.49 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 |  | No | 61.06 |
| 2 | 51 |  | No | 74.72 |
| 3 | 72 |  | No | 89.65 |
| 4 | 61 |  | No | 88.3 |
| 5 | 60 |  | No | 83.8 |
| 6 | 35 |  | No | 56.16 |
| 7 | 57 |  | No | 89.94 |
| 8 | 69 |  | No | 65.51 |
| 9 | 44 |  | No | 49.0 |
| 10 | 52 |  | No | 77.31 |
| 11 | 63 |  | No | 50.33 |
| 12 | 61 |  | No | 86.3 |
| 13 | 74 |  | No | 67.54 |
| 14 | 65 |  | No | 80.37 |
| 15 | 67 |  | No | 62.32 |
| 16 | 60 |  | No | 57.74 |
| 17 | 49 |  | No | 66.11 |
| 18 | 47 |  | No | 47.85 |
| 19 | 38 |  | No | 78.05 |
| 20 | 37 |  | No | 60.98 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SJOUMPY | SJOUMPY | Yes | 9.3 |
| 2 | FIQKRDJ | FIQKRDJ | Yes | 3.1 |
| 3 | MCYBSHR | MCYBSHR | Yes | 4.35 |
| 4 | HKCLSIG | HKCLSIG | Yes | 6.38 |
| 5 | AXQIFDZ | AXQIFDZ | Yes | 4.48 |
| 6 | IOQVDCP | IOQVDCP | Yes | 6.6 |
| 7 | HKOFYSQ | HKOFYSQ | Yes | 7.28 |
| 8 | FWCOTKN | FWCOTKN | Yes | 6.8 |
| 9 | XVLRSPU | XVLRSPU | Yes | 8.25 |
| 10 | HFKBXZI | HFKBXZI | Yes | 15.91 |
| 11 | IZVTDAR | IZVTDAR | Yes | 5.49 |
| 12 | CORGSUI | CORGSUI | Yes | 11.51 |
| 13 | UNSBYFH | UNSBYFH | Yes | 7.44 |
| 14 | MKIBVNG | MKIBVNG | Yes | 6.32 |
| 15 | ESQVNAL | ESQVNAL | Yes | 15.28 |
| 16 | IGXLSQZ | IGXLSQZ | Yes | 4.58 |
| 17 | ZWRGEQL | ZWRGEQL | Yes | 8.7 |
| 18 | VPRBKXF | VPRBKXF | Yes | 6.19 |
| 19 | EJBZASK | EJBZASK | Yes | 8.08 |
| 20 | WEVZDRT | WEVZDRT | Yes | 5.26 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.61 |
| 2 | [0.5, 9.5] | 0.5 9.5 | Yes | 8.11 |
| 3 | [4.2, 5.8] | 4.2 5.8 | Yes | 6.75 |
| 4 | [0.7, 9.3] | 0.7 9.3 | Yes | 8.09 |
| 5 | [0.1, 9.9] | 0.1 9.9 | Yes | 9.53 |
| 6 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.19 |
| 7 | [2.7, 7.3] | 2.7 7.3 | Yes | 8.58 |
| 8 | [3.5, 6.5] | 3.5 6.5 | Yes | 12.74 |
| 9 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.14 |
| 10 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.32 |
| 11 | [3.3, 6.7] | 3.3 6.7 | Yes | 10.63 |
| 12 | [4.9, 5.1] | 4.9 5.1 | Yes | 6.95 |
| 13 | [4.2, 5.8] | 5.8 4.2 | Yes | 13.91 |
| 14 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.8 |
| 15 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.09 |
| 16 | [3.5, 6.5] | 6.5 3.5 | Yes | 10.04 |
| 17 | [4.0, 6.0] | 4.0 6.0 | Yes | 15.26 |
| 18 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.5 |
| 19 | [4.3, 5.7] | 5.7 4.3 | Yes | 9.86 |
| 20 | [0.3, 9.7] | 0.3 9.7 | Yes | 10.51 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1WH74IIJI6WY | 1WH74IIJ6WY | No | 4.42 |
| 2 | 9Q1T20VYFVFS | 9Q1T20VYFVFS | Yes | 3.43 |
| 3 | PK3WN5EYAUW9 | PK3WN5EYAUW9 | Yes | 1.82 |
| 4 | 9PWWMTZ8FAEQ | 9PWWMTZ8FAEQ | Yes | 1.6 |
| 5 | P1D9NIRWRJOW | P1D9NIRWRJ0W | No | 10.26 |
| 6 | JXCCVXOXQ3GR | JXCCVXOXQ3GR | Yes | 4.0 |
| 7 | RBUJKNDE65Q4 | RBUJKNDE65Q4 | Yes | 2.29 |
| 8 | 9V86114JM6L9 | 9V86114JM6L9 | Yes | 2.88 |
| 9 | N93X7OKQ14JR | N93X7OKQ14JR | Yes | 4.38 |
| 10 | O6PVVW761QH8 | O6PVVW761QH8 | Yes | 7.24 |
| 11 | ZFT3D3AG7WQA | ZFT3D3AG7WQA | Yes | 2.1 |
| 12 | X3REP9OGHVPF | X3REP9OGHVPF | Yes | 8.23 |
| 13 | 40LW1ITWWYVV | 4QLW1ITWWYVV | No | 5.0 |
| 14 | HX58TYOSLP23 | HX58TYOSLP23 | Yes | 3.26 |
| 15 | 1OKTLBME5W3H | 10KTLBME5W3H | No | 11.88 |
| 16 | 197DQD832DKD | 197DQD832DKD | Yes | 3.68 |
| 17 | RM8N71VRYPQ0 | RM8N71VRYPQ0 | Yes | 5.94 |
| 18 | K8J9OFYHJ0R9 | K8J9OFYHJ0R9 | Yes | 2.62 |
| 19 | 2ZEJBOSKXD39 | 2ZEJBOSKXD39 | Yes | 4.01 |
| 20 | Z9TNETAPM23G | Z9TNETAPM23G | Yes | 6.01 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 4.04 |
| 2 | 67 | 67 | Yes | 3.91 |
| 3 | 28 | 28 | Yes | 11.64 |
| 4 | 36 | 36 | Yes | 3.0 |
| 5 | 64 | 64 | Yes | 7.34 |
| 6 | 5 | 5 | Yes | 8.96 |
| 7 | 7680 | 7680 | Yes | 6.77 |
| 8 | 243 | 243 | Yes | 3.37 |
| 9 | 20 |  | No | 44.93 |
| 10 | 60 | 60 | Yes | 4.88 |
| 11 | 26 | 26 | Yes | 16.6 |
| 12 | 4 | 4 | Yes | 5.08 |
| 13 | 19 | 19 | Yes | 3.4 |
| 14 | 3 | 3 | Yes | 8.54 |
| 15 | 60 | 60 | Yes | 4.35 |
| 16 | 4 | 4 | Yes | 3.31 |
| 17 | 7 | 7 | Yes | 3.31 |
| 18 | 9 | 9 | Yes | 6.36 |
| 19 | 9 | 9 | Yes | 3.58 |
| 20 | 1 | 1 | Yes | 4.44 |
