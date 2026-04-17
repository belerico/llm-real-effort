# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
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
| sudoku_game | 8740 | 33499 | 42239 | 6 | 14 | 28.20 | 564.16 |
| add_numbers | 4660 | 632 | 5292 | 20 | 0 | 3.34 | 66.83 |
| counting_zeros | 7600 | 22322 | 29922 | 8 | 12 | 14.96 | 299.61 |
| task_decoding | 14040 | 3132 | 17172 | 20 | 0 | 5.89 | 117.98 |
| task_summation | 7960 | 5592 | 13552 | 20 | 0 | 6.69 | 133.95 |
| task_transcription | 4820 | 923 | 5743 | 20 | 0 | 4.13 | 82.78 |
| task_sequences | 3920 | 4757 | 8677 | 19 | 1 | 5.25 | 104.95 |
| **TOTAL** | **51740** | **70857** | **122597** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 1 2 5 5 5 6 3 2 1 4 6 3 2 | 3 1 2 5 5 5 6 3 2 1 4 6 3 2</s> | No | 20.48 |
| 2 | 3 6 6 4 1 3 5 1 5 6 1 2 6 3 |  | No | 35.62 |
| 3 | 3 2 4 2 3 6 4 3 5 2 1 5 4 6 | 3 2 4 2 3 6 4 3 5 2 1 5 4 1 6 3 | No | 24.67 |
| 4 | 5 6 4 1 4 5 3 1 5 4 6 2 1 3 |  | No | 36.4 |
| 5 | 5 2 4 6 1 6 2 4 3 4 5 3 2 1 | 5 2 1 6 2 4 3 4 5 3 2 1 | No | 22.85 |
| 6 | 3 4 6 2 5 1 6 2 1 4 2 5 6 3 | 3 4 6 2 5 1 5 4 6 2 3 1 2 4 5 6 3 | No | 19.24 |
| 7 | 2 3 4 1 5 4 4 3 2 4 6 2 4 3 | 2 3 4 1 5 4 4 3 2 4 6 2 4 3 | Yes | 28.57 |
| 8 | 6 1 3 2 4 1 5 3 5 2 4 2 4 5 | 6 1 3 2 4 1 5 3 5 2 4 2 4 5 2 5 | No | 19.53 |
| 9 | 3 4 1 3 3 4 1 2 5 4 3 1 4 2 |  | No | 35.02 |
| 10 | 3 6 3 2 5 4 3 2 4 4 1 6 3 5 | 3 6 3 2 5 4 3 2 4 4 1 6 3 5 | Yes | 26.54 |
| 11 | 2 3 4 1 6 3 5 2 4 5 3 3 4 3 |  | No | 37.36 |
| 12 | 1 5 4 2 2 4 2 5 3 4 1 5 2 4 | 1 5 4 2 2 4 5 3 2 5 3 4 1 5 2 4 | No | 26.29 |
| 13 | 2 6 3 4 6 2 5 2 2 4 4 2 2 6 |  | No | 35.43 |
| 14 | 2 2 4 6 6 6 1 2 4 4 5 6 3 1 | 2 2 4 6 6 6 1 2 4 4 5 6 3 1 | Yes | 30.32 |
| 15 | 4 3 5 1 4 2 4 5 2 5 4 6 4 5 | 4 3 5 1 4 2 4 5 2 5 4 6 4 5 | Yes | 27.65 |
| 16 | 3 5 2 6 1 6 4 3 2 1 5 1 3 6 | 3 5 2 6 1 6 4 3 2 1 5 1 3 6 | Yes | 22.23 |
| 17 | 2 6 6 4 1 2 4 3 1 6 4 3 2 6 |  | No | 35.91 |
| 18 | 4 3 2 5 3 6 6 1 4 4 5 3 5 4 |  | No | 35.96 |
| 19 | 3 6 5 4 2 5 6 1 3 5 1 6 6 5 | 3 6 5 4 2 5 6 1 3 5 1 6 6 5 | Yes | 21.63 |
| 20 | 5 4 6 3 1 5 2 1 4 3 3 2 1 6 | 5 4 6 3 1 5 2 1 4 3 2 3 2 1 6 | No | 22.25 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1837 | 1837 | Yes | 2.59 |
| 2 | 1972 | 1972 | Yes | 3.21 |
| 3 | 1929 | 1929 | Yes | 2.82 |
| 4 | 1857 | 1857 | Yes | 2.71 |
| 5 | 2072 | 2072 | Yes | 2.71 |
| 6 | 1542 | 1542 | Yes | 2.71 |
| 7 | 1925 | 1925 | Yes | 3.27 |
| 8 | 2648 | 2648 | Yes | 2.68 |
| 9 | 2064 | 2064 | Yes | 7.84 |
| 10 | 1475 | 1475 | Yes | 2.71 |
| 11 | 1395 | 1395 | Yes | 3.54 |
| 12 | 1496 | 1496 | Yes | 4.07 |
| 13 | 2128 | 2128 | Yes | 3.05 |
| 14 | 866 | 866 | Yes | 2.77 |
| 15 | 1047 | 1047 | Yes | 2.91 |
| 16 | 2176 | 2176 | Yes | 2.7 |
| 17 | 842 | 842 | Yes | 3.33 |
| 18 | 1468 | 1468 | Yes | 3.5 |
| 19 | 1150 | 1150 | Yes | 3.05 |
| 20 | 1928 | 1928 | Yes | 4.57 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 47 | 47 | Yes | 12.2 |
| 2 | 62 | 62 | Yes | 13.1 |
| 3 | 56 | 56 | Yes | 13.39 |
| 4 | 40 | 40 | Yes | 13.74 |
| 5 | 48 | 48 | Yes | 19.17 |
| 6 | 72 | 66 | No | 13.92 |
| 7 | 58 | 58 | Yes | 12.68 |
| 8 | 68 | 67 | No | 13.18 |
| 9 | 66 | 64 | No | 17.36 |
| 10 | 66 | 63 | No | 12.99 |
| 11 | 52 | 52 | Yes | 13.91 |
| 12 | 60 | 61 | No | 32.21 |
| 13 | 68 | 67 | No | 16.83 |
| 14 | 75 | 72 | No | 12.53 |
| 15 | 59 | 55 | No | 13.38 |
| 16 | 59 | 58 | No | 14.22 |
| 17 | 64 | 62 | No | 15.03 |
| 18 | 60 | 57 | No | 12.99 |
| 19 | 68 | 67 | No | 13.76 |
| 20 | 35 | 35 | Yes | 12.71 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DSZRCPI | DSZRCPI | Yes | 7.41 |
| 2 | KSODCMB | KSODCMB | Yes | 5.89 |
| 3 | VATUQIJ | VATUQIJ | Yes | 6.32 |
| 4 | HEFBGYR | HEFBGYR | Yes | 6.16 |
| 5 | UTFNDMX | UTFNDMX | Yes | 5.88 |
| 6 | XDAMQKG | XDAMQKG | Yes | 6.39 |
| 7 | OCFTKUA | OCFTKUA | Yes | 6.55 |
| 8 | VUJMECO | VUJMECO | Yes | 5.57 |
| 9 | EMPUITX | EMPUITX | Yes | 4.02 |
| 10 | OXHVMFJ | OXHVMFJ | Yes | 4.5 |
| 11 | VLXHGSO | VLXHGSO | Yes | 4.72 |
| 12 | REQWYJC | REQWYJC | Yes | 4.04 |
| 13 | QLYGPXE | QLYGPXE | Yes | 4.13 |
| 14 | JLVYXQE | JLVYXQE | Yes | 8.85 |
| 15 | NKAYDFZ | NKAYDFZ | Yes | 6.42 |
| 16 | EQCINGP | EQCINGP | Yes | 3.45 |
| 17 | VEICQBA | VEICQBA | Yes | 8.85 |
| 18 | HMUFBXZ | HMUFBXZ | Yes | 4.15 |
| 19 | LWTZQHP | LWTZQHP | Yes | 8.15 |
| 20 | IGMNPVH | IGMNPVH | Yes | 6.31 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.6, 8.4] | 1.6 8.4 | Yes | 6.97 |
| 2 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.99 |
| 3 | [4.1, 5.9] | 4.1 5.9 | Yes | 7.14 |
| 4 | [2.3, 7.7] | 7.7 2.3 | Yes | 8.26 |
| 5 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.3 |
| 6 | [1.6, 8.4] | 1.6 8.4 | Yes | 6.19 |
| 7 | [2.3, 7.7] | 7.7 2.3 | Yes | 3.86 |
| 8 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.16 |
| 9 | [2.6, 7.4] | 2.6 7.4 | Yes | 8.31 |
| 10 | [1.7, 8.3] | 8.3 1.7 | Yes | 6.6 |
| 11 | [2.4, 7.6] | 7.6 2.4 | Yes | 7.02 |
| 12 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.2 |
| 13 | [4.9, 5.1] | 5.1 4.9 | Yes | 8.05 |
| 14 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.08 |
| 15 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.67 |
| 16 | [0.9, 9.1] | 9.1 0.9 | Yes | 10.96 |
| 17 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.76 |
| 18 | [2.0, 8.0] | 8.0 2.0 | Yes | 5.41 |
| 19 | [2.3, 7.7] | 7.7 2.3 | Yes | 4.28 |
| 20 | [0.2, 9.8] | 9.8 0.2 | Yes | 5.55 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3NQEDBL0Z2P0 | 3NQEDBL0Z2P0 | Yes | 4.3 |
| 2 | ZE1WV0DPSFQB | ZE1WV0DPSFQB | Yes | 3.77 |
| 3 | 9G9QKV9CC7H3 | 9G9QKV9CC7H3 | Yes | 4.42 |
| 4 | KOU4HL7QIOUP | KOU4HL7QIOUP | Yes | 4.9 |
| 5 | Z6NO2ZP9MON1 | Z6NO2ZP9MON1 | Yes | 5.75 |
| 6 | UYF0BB2N6FAT | UYF0BB2N6FAT | Yes | 4.79 |
| 7 | ZLBOCLGTOG6V | ZLBOCLGTOG6V | Yes | 4.4 |
| 8 | QONYWE2ZCPVN | QONYWE2ZCPVN | Yes | 6.14 |
| 9 | TVSHNW5TYWV8 | TVSHNW5TYWV8 | Yes | 5.1 |
| 10 | DL79TVSO45NO | DL79TVSO45NO | Yes | 3.49 |
| 11 | 3DR7XYNRYXAZ | 3DR7XYNRYXAZ | Yes | 3.51 |
| 12 | IEEEMM89VL9Z | IEEEMM89VL9Z | Yes | 3.93 |
| 13 | Q2IZ25QJ3T4S | Q2IZ25QJ3T4S | Yes | 3.38 |
| 14 | 6K9BUG79MRGN | 6K9BUG79MRGN | Yes | 3.24 |
| 15 | T7J3YBP81XHR | T7J3YBP81XHR | Yes | 3.4 |
| 16 | MFNE8425HUEB | MFNE8425HUEB | Yes | 3.38 |
| 17 | 3QL6F38P34WX | 3QL6F38P34WX | Yes | 5.03 |
| 18 | JORWHNP1ZIBG | JORWHNP1ZIBG | Yes | 3.22 |
| 19 | UD7G4V5ENHIO | UD7G4V5ENHIO | Yes | 3.38 |
| 20 | ATRU3BZ6CATV | ATRU3BZ6CATV | Yes | 3.15 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 4.67 |
| 2 | 198 | 198 | Yes | 4.43 |
| 3 | 63 | 63 | Yes | 4.61 |
| 4 | 6 | 6 | Yes | 4.16 |
| 5 | 4 | 4 | Yes | 3.2 |
| 6 | 64 | 64 | Yes | 5.24 |
| 7 | 793 | 793 | Yes | 2.72 |
| 8 | 9 | 9 | Yes | 5.09 |
| 9 | 36 | 36 | Yes | 3.27 |
| 10 | 9 | 9 | Yes | 4.35 |
| 11 | 5 | 18 | No | 23.19 |
| 12 | 48 | 48 | Yes | 2.99 |
| 13 | 44 | 44 | Yes | 4.43 |
| 14 | 60 | 60 | Yes | 4.88 |
| 15 | 26 | 26 | Yes | 5.99 |
| 16 | 23 | 23 | Yes | 4.32 |
| 17 | 31 | 31 | Yes | 3.81 |
| 18 | 7680 | 7680 | Yes | 4.43 |
| 19 | 39 | 39 | Yes | 4.3 |
| 20 | 5 | 5 | Yes | 4.88 |
