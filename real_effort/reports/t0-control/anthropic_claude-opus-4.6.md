# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-19 09:59:26

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
| sudoku_game | 8060 | 33190 | 41250 | 12 | 8 | 26.56 | 531.52 |
| add_numbers | 3980 | 596 | 4576 | 20 | 0 | 2.97 | 59.51 |
| counting_zeros | 6920 | 23042 | 29962 | 8 | 12 | 14.47 | 289.65 |
| task_decoding | 13360 | 2714 | 16074 | 20 | 0 | 4.77 | 95.66 |
| task_summation | 7280 | 4881 | 12161 | 20 | 0 | 6.52 | 130.57 |
| task_transcription | 4136 | 650 | 4786 | 18 | 2 | 3.14 | 62.78 |
| task_sequences | 3241 | 4648 | 7889 | 20 | 0 | 5.12 | 102.45 |
| **TOTAL** | **46977** | **69721** | **116698** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 3 5 5 4 4 1 6 4 6 3 4 6 5 | 6 3 5 5 4 4 1 6 4 6 3 4 6 5 | Yes | 24.07 |
| 2 | 5 1 6 2 6 3 6 3 4 6 2 6 4 3 | 5 1 6 2 6 3 6 3 4 6 2 6 4 3 | Yes | 17.32 |
| 3 | 2 4 3 6 1 5 6 6 1 2 1 2 6 6 | 2 4 3 6 1 5 6 6 1 2 1 2 6 6 | Yes | 22.34 |
| 4 | 1 5 6 2 3 6 5 2 1 4 4 5 5 2 |  | No | 33.45 |
| 5 | 1 2 5 2 4 3 1 3 5 6 2 1 5 4 | 1 2 5 2 4 3 1 3 5 6 2 1 5 4 | Yes | 23.29 |
| 6 | 5 4 1 5 4 6 3 5 2 5 5 1 2 4 | 5 4 1 5 4 6 3 5 2 5 1 2 4 | No | 20.95 |
| 7 | 4 3 3 1 2 5 1 3 5 3 4 2 1 4 | 4 3 3 1 2 5 1 3 5 3 4 2 1 4 | Yes | 24.04 |
| 8 | 3 4 4 5 2 6 1 5 6 5 4 2 6 5 | 3 4 4 5 2 6 1 5 6 5 4 2 6 5 | Yes | 23.02 |
| 9 | 5 6 1 6 1 3 4 1 5 3 5 2 1 3 | 5 6 1 6 1 3 4 1 5 3 5 2 1 3 | Yes | 20.2 |
| 10 | 6 2 5 4 5 5 4 1 1 2 5 1 2 3 | 6 2 5 4 5 5 4 1 1 2 5 1 2 3 | Yes | 25.4 |
| 11 | 5 3 4 4 5 4 2 1 4 2 3 6 2 6 |  | No | 37.49 |
| 12 | 3 2 3 1 6 4 1 2 4 3 4 6 3 2 | 3 2 3 1 6 4 1 2 4 3 4 6 3 2 | Yes | 27.36 |
| 13 | 3 1 6 3 5 6 2 4 5 4 6 5 4 2 |  | No | 37.83 |
| 14 | 3 6 4 1 2 4 3 2 5 6 4 6 4 1 | 3 6 4 1 2 4 3 2 5 6 4 6 4 1 | Yes | 20.67 |
| 15 | 5 2 4 6 3 5 2 4 3 5 6 4 3 1 | 5 2 4 6 3 5 2 4 3 5 6 4 3 1 | Yes | 18.46 |
| 16 | 5 6 4 5 2 4 5 1 4 5 4 1 1 6 | 5 6 4 5 2 4 5 1 4 5 4 1 1 6 | Yes | 24.06 |
| 17 | 1 3 4 2 6 2 1 5 1 5 1 2 6 4 | 1 3 4 2 6 2 1 5 1 5 2 6 4 | No | 25.0 |
| 18 | 6 1 4 6 6 5 2 5 2 1 3 5 2 4 |  | No | 30.52 |
| 19 | 3 5 4 4 5 2 6 2 4 1 5 6 5 3 |  | No | 39.72 |
| 20 | 4 1 3 5 5 6 5 3 3 4 4 3 6 4 |  | No | 36.1 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2453 | 2453 | Yes | 3.03 |
| 2 | 2254 | 2254 | Yes | 2.5 |
| 3 | 1400 | 1400 | Yes | 2.72 |
| 4 | 1649 | 1649 | Yes | 2.68 |
| 5 | 1545 | 1545 | Yes | 3.29 |
| 6 | 1592 | 1592 | Yes | 2.52 |
| 7 | 1376 | 1376 | Yes | 2.59 |
| 8 | 1855 | 1855 | Yes | 2.87 |
| 9 | 1067 | 1067 | Yes | 2.62 |
| 10 | 1563 | 1563 | Yes | 2.77 |
| 11 | 1813 | 1813 | Yes | 2.87 |
| 12 | 1488 | 1488 | Yes | 3.98 |
| 13 | 1722 | 1722 | Yes | 2.83 |
| 14 | 1535 | 1535 | Yes | 2.49 |
| 15 | 2149 | 2149 | Yes | 4.9 |
| 16 | 1172 | 1172 | Yes | 2.7 |
| 17 | 897 | 897 | Yes | 3.56 |
| 18 | 987 | 987 | Yes | 2.96 |
| 19 | 2016 | 2016 | Yes | 2.68 |
| 20 | 1456 | 1456 | Yes | 2.88 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 | 53 | No | 20.21 |
| 2 | 36 | 35 | No | 12.31 |
| 3 | 71 | 67 | No | 13.32 |
| 4 | 62 | 62 | Yes | 16.52 |
| 5 | 62 | 62 | Yes | 12.68 |
| 6 | 37 | 36 | No | 16.3 |
| 7 | 41 | 41 | Yes | 12.1 |
| 8 | 55 | 52 | No | 13.01 |
| 9 | 67 | 66 | No | 13.22 |
| 10 | 40 | 40 | Yes | 12.72 |
| 11 | 70 | 69 | No | 13.01 |
| 12 | 48 | 47 | No | 12.56 |
| 13 | 49 | 48 | No | 16.14 |
| 14 | 51 | 49 | No | 17.15 |
| 15 | 58 | 58 | Yes | 12.17 |
| 16 | 48 | 48 | Yes | 15.14 |
| 17 | 48 | 48 | Yes | 13.16 |
| 18 | 57 | 56 | No | 13.68 |
| 19 | 72 | 72 | Yes | 15.15 |
| 20 | 75 | 77 | No | 18.78 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZHDNFWY | ZHDNFWY | Yes | 3.49 |
| 2 | DKJTWBO | DKJTWBO | Yes | 3.53 |
| 3 | TALQVFC | TALQVFC | Yes | 6.13 |
| 4 | FEOLSUX | FEOLSUX | Yes | 4.84 |
| 5 | ISHZEAU | ISHZEAU | Yes | 3.13 |
| 6 | VUEDNWT | VUEDNWT | Yes | 6.12 |
| 7 | FUOLNMT | FUOLNMT | Yes | 4.73 |
| 8 | DMCIWXE | DMCIWXE | Yes | 4.07 |
| 9 | GDSBMOE | GDSBMOE | Yes | 6.54 |
| 10 | WTFMHQC | WTFMHQC | Yes | 3.68 |
| 11 | GKEXLAM | GKEXLAM | Yes | 3.87 |
| 12 | ABCWYST | ABCWYST | Yes | 6.37 |
| 13 | KFMOZYR | KFMOZYR | Yes | 3.74 |
| 14 | PQWTAHJ | PQWTAHJ | Yes | 3.29 |
| 15 | XZKCUGH | XZKCUGH | Yes | 6.6 |
| 16 | QMTWEZR | QMTWEZR | Yes | 7.51 |
| 17 | AXVIRTM | AXVIRTM | Yes | 3.55 |
| 18 | TZVCHUK | TZVCHUK | Yes | 4.21 |
| 19 | JZKXSRN | JZKXSRN | Yes | 4.03 |
| 20 | JQONAGL | JQONAGL | Yes | 6.03 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.2, 7.8] | 2.2 7.8 | Yes | 10.93 |
| 2 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.4 |
| 3 | [0.4, 9.6] | 9.6 0.4 | Yes | 4.22 |
| 4 | [3.8, 6.2] | 3.8 6.2 | Yes | 5.84 |
| 5 | [1.0, 9.0] | 1.0 9.0 | Yes | 6.75 |
| 6 | [2.1, 7.9] | 2.1 7.9 | Yes | 6.69 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.23 |
| 8 | [3.0, 7.0] | 3.0 7.0 | Yes | 6.39 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 6.88 |
| 10 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.28 |
| 11 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.47 |
| 12 | [1.7, 8.3] | 1.7 8.3 | Yes | 3.28 |
| 13 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.33 |
| 14 | [0.2, 9.8] | 9.8 0.2 | Yes | 3.35 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.78 |
| 16 | [2.5, 7.5] | 7.5 2.5 | Yes | 6.8 |
| 17 | [3.4, 6.6] | 6.6 3.4 | Yes | 3.68 |
| 18 | [0.8, 9.2] | 0.8 9.2 | Yes | 10.25 |
| 19 | [4.8, 5.2] | 4.8 5.2 | Yes | 12.55 |
| 20 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.31 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5VZKAWH7HICP | 5VZKAWH7HICP | Yes | 2.72 |
| 2 | H22SW0M575UW | H22SW0M575UW | Yes | 2.86 |
| 3 | B1PRPW3Z3SLZ | B1PRPW3Z3SLZ | Yes | 3.27 |
| 4 | 5N2N7B2OV2K8 | 5N2N7B2OV2K8 | Yes | 3.07 |
| 5 | TKYSQG5WI9HN | TKYSQG5WI9HN | Yes | 3.09 |
| 6 | AKAVMQHHDKLH | AKAVMQHHDKLH | Yes | 3.64 |
| 7 | 0XNLNYLEFV71 | OXNLNYLEFV71 | No | 4.2 |
| 8 | F3SPOUCU4S8K | F3SPOUCU4S8K | Yes | 2.97 |
| 9 | 17L9TH7OC7T8 | 17L9TH7OC7T8 | Yes | 2.84 |
| 10 | F4VAMAH226J1 | F4VAMAH226J1 | Yes | 2.8 |
| 11 | 98IRSI3GJAPD | 98IRSI3GJAPD | Yes | 3.36 |
| 12 | S9AB8K28OPBG | S9AB8K28OPBG | Yes | 3.02 |
| 13 | BOZ1XOSOZLUQ | BOZ1XOSOZLUQ | Yes | 3.91 |
| 14 | JPMBS2W05211 | JPMBS2W05211 | Yes | 2.81 |
| 15 | K5JSWOXIIZOD | K5JSWOXIIZOD | Yes | 3.38 |
| 16 | I1BDT6MVQPNH | I1BDT6MVQPNH | Yes | 3.14 |
| 17 | WXXDA42E6CFZ | WXXDA42E6CFZ | Yes | 2.76 |
| 18 | M8KWSOIB2J98 | M8KWSOIB2J98 | Yes | 3.08 |
| 19 | HITZ2MEFRMLR | HITZ2MEFRMLR | Yes | 2.9 |
| 20 | DCRDVTEXXHX0 | DCRDVTEXXHXO | No | 2.9 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 5.75 |
| 2 | 36 | 36 | Yes | 2.62 |
| 3 | 20 | 20 | Yes | 11.22 |
| 4 | 39 | 39 | Yes | 3.65 |
| 5 | 60 | 60 | Yes | 3.91 |
| 6 | 67 | 67 | Yes | 2.44 |
| 7 | 7680 | 7680 | Yes | 5.56 |
| 8 | 31 | 31 | Yes | 3.69 |
| 9 | 4096 | 4096 | Yes | 10.02 |
| 10 | 19 | 19 | Yes | 3.16 |
| 11 | 1 | 1 | Yes | 4.93 |
| 12 | 73 | 73 | Yes | 4.66 |
| 13 | 9 | 9 | Yes | 4.31 |
| 14 | 26 | 26 | Yes | 13.16 |
| 15 | 44 | 44 | Yes | 5.3 |
| 16 | 4 | 4 | Yes | 2.76 |
| 17 | 23 | 23 | Yes | 4.2 |
| 18 | 198 | 198 | Yes | 3.67 |
| 19 | 243 | 243 | Yes | 2.49 |
| 20 | 16 | 16 | Yes | 4.95 |
