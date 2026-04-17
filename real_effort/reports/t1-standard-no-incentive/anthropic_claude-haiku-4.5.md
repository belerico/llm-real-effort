# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8380 | 27545 | 35925 | 1 | 19 | 11.00 | 220.06 |
| add_numbers | 4300 | 2423 | 6723 | 20 | 0 | 2.90 | 58.18 |
| counting_zeros | 7240 | 21500 | 28740 | 1 | 19 | 7.57 | 151.61 |
| task_decoding | 13680 | 10595 | 24275 | 16 | 4 | 4.70 | 94.25 |
| task_summation | 7600 | 15587 | 23187 | 20 | 0 | 6.37 | 127.59 |
| task_transcription | 4440 | 3811 | 8251 | 19 | 1 | 2.82 | 56.53 |
| task_sequences | 3561 | 6408 | 9969 | 19 | 1 | 3.51 | 70.17 |
| **TOTAL** | **49201** | **87869** | **137070** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 4 1 2 3 6 2 3 2 4 5 5 1 6 | 4 4 2 3 6 1 2 3 5 4 2 2 5 6 | No | 12.89 |
| 2 | 4 2 3 6 5 1 1 3 3 2 1 6 5 1 | **Answer: 4 2 3 6 1 5 1 3 3 5 5 6 2 1** | No | 13.2 |
| 3 | 1 2 6 6 4 1 3 2 1 2 6 6 5 3 | 1 6 2 6 6 4 3 1 2 1 2 6 6 5 3 | No | 13.6 |
| 4 | 1 4 3 2 3 4 6 1 2 5 5 6 5 6 | 1 2 3 2 3 4 6 5 4 2 5 6 1 6 | No | 9.46 |
| 5 | 5 4 1 3 5 4 6 5 3 1 6 2 3 1 | 5 4 1 1 4 5 6 2 3 6 5 1 2 6 1 3 | No | 8.93 |
| 6 | 6 4 4 1 5 4 2 3 4 1 5 4 4 2 | 4 6 4 1 5 2 4 3 4 1 4 5 4 2 | No | 10.94 |
| 7 | 4 3 2 6 2 6 5 4 4 6 3 3 5 2 | 4 2 3 2 6 6 5 4 3 6 6 4 3 2 | No | 10.42 |
| 8 | 1 3 4 1 5 3 6 4 4 5 1 1 5 4 | 1 3 4 1 5 3 6 4 5 4 1 1 4 5 | No | 10.6 |
| 9 | 6 2 6 4 2 4 2 1 5 5 2 3 4 2 | 6 2 2 6 4 2 4 2 1 5 5 2 3 4 2 1 5 4 | No | 11.82 |
| 10 | 5 2 1 6 4 6 2 1 4 6 5 4 1 2 | 5 2 1 6 4 6 2 1 5 4 1 2 | No | 10.29 |
| 11 | 2 5 6 1 2 1 5 6 2 1 5 6 2 6 | 2 5 1 6 1 5 2 6 5 6 | No | 11.23 |
| 12 | 2 1 6 4 4 5 3 2 1 6 1 1 3 1 | 1 4 5 6 3 2 2 5 1 6 3 4 1 3 1 3 6 1** | No | 8.79 |
| 13 | 3 2 1 3 5 2 3 4 6 1 4 4 2 1 | 3 2 1 3 5 2 3 4 6 1 4 4 2 1 | Yes | 12.16 |
| 14 | 1 2 4 2 6 4 6 3 1 6 5 2 5 4 | 1 2 4 2 6 4 6 3 1 5 2 6 5 4 | No | 9.35 |
| 15 | 1 6 4 2 5 4 4 4 3 6 5 4 1 3 | 1 6 4 2 5 4 4 3 4 4 6 5 4 1 3 | No | 13.25 |
| 16 | 3 2 6 4 6 3 3 5 5 1 3 6 3 6 | 3 2 6 3 6 4 3 5 5 3 1 6 1 6** | No | 9.97 |
| 17 | 1 4 5 4 1 5 3 5 3 2 2 1 2 6 | 1 5 4 4 1 3 5 5 2 3 1 2** | No | 9.2 |
| 18 | 2 3 5 6 3 1 4 2 6 2 1 4 3 2 | 5 2 5 6 4 3 1 2 6 2 1 4 2 3 | No | 12.52 |
| 19 | 2 6 6 1 2 2 6 1 4 2 6 6 5 5 | 2 6 6 1 2 2 1 6 4 2 6 6 5 5 | No | 10.72 |
| 20 | 5 4 3 4 1 4 3 1 6 5 5 4 4 2 | 5 4 3 4 1 1 3 4 5 6 4 5 2 4** | No | 10.56 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1677 | 1677 | Yes | 2.28 |
| 2 | 1699 | 1699 | Yes | 3.66 |
| 3 | 1422 | 1422 | Yes | 2.69 |
| 4 | 1177 | 1177 | Yes | 2.22 |
| 5 | 776 | 776 | Yes | 2.69 |
| 6 | 1314 | 1314 | Yes | 2.4 |
| 7 | 1785 | 1785 | Yes | 2.78 |
| 8 | 1519 | 1519 | Yes | 2.53 |
| 9 | 1934 | 1934 | Yes | 2.32 |
| 10 | 1156 | 1156 | Yes | 2.29 |
| 11 | 1736 | 1736 | Yes | 3.17 |
| 12 | 1413 | 1413 | Yes | 2.21 |
| 13 | 1798 | 1798 | Yes | 2.81 |
| 14 | 2310 | 2310 | Yes | 2.72 |
| 15 | 2351 | 2351 | Yes | 6.91 |
| 16 | 783 | 783 | Yes | 2.16 |
| 17 | 891 | 891 | Yes | 3.41 |
| 18 | 1381 | 1381 | Yes | 2.77 |
| 19 | 2153 | 2153 | Yes | 3.86 |
| 20 | 1030 | 1030 | Yes | 2.2 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 69 | 67 | No | 7.32 |
| 2 | 65 | 62 | No | 7.46 |
| 3 | 46 | 47 | No | 7.29 |
| 4 | 73 | 62 | No | 9.26 |
| 5 | 60 | 54 | No | 9.29 |
| 6 | 68 | 69 | No | 10.64 |
| 7 | 64 | 61 | No | 7.1 |
| 8 | 35 | 32 | No | 7.53 |
| 9 | 53 | 48 | No | 6.21 |
| 10 | 41 | 47 | No | 6.79 |
| 11 | 72 | 67 | No | 8.9 |
| 12 | 71 | 62 | No | 6.67 |
| 13 | 60 | 57 | No | 8.64 |
| 14 | 52 | 51 | No | 5.79 |
| 15 | 44 | 44 | Yes | 7.75 |
| 16 | 71 | 69 | No | 7.48 |
| 17 | 40 | 38 | No | 7.43 |
| 18 | 44 | 43 | No | 5.97 |
| 19 | 63 | 64 | No | 7.4 |
| 20 | 40 | 42 | No | 6.4 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IBTYCKA | IBTYCKA | Yes | 3.88 |
| 2 | IRVKYUO | IRVKYUO | Yes | 4.92 |
| 3 | IGWHOQB | IGWHQB | No | 6.84 |
| 4 | SLVKFAB | SLVKFAB | Yes | 4.63 |
| 5 | RVUTIOS | RVUTIOS | Yes | 4.45 |
| 6 | NHUBGTP | NHUBGTP | Yes | 4.16 |
| 7 | NJIQFZP | NJIQFZP | Yes | 4.46 |
| 8 | ENDRILB | ENDRILB | Yes | 4.95 |
| 9 | MWFRJQH | MWFRJQH | Yes | 5.19 |
| 10 | PVTJNWZ | PVTJNGWZ | No | 5.58 |
| 11 | RZUJKNB | RZUJKNB | Yes | 4.9 |
| 12 | FQTEDOS | FQTEDOS | Yes | 4.28 |
| 13 | ZMJQOCE | ZMJQOCE | Yes | 4.36 |
| 14 | JCUAHKW | JCUAHKW | Yes | 4.49 |
| 15 | DBHOZFR | DBHOZEFR | No | 4.81 |
| 16 | GQZCHKW | GQZCHKW | Yes | 4.45 |
| 17 | DIAZNBV | DIAZNBV | Yes | 4.02 |
| 18 | WPLMIRQ | WPLMIRQ | Yes | 5.0 |
| 19 | DTYAMSU | DTYYAMSU | No | 4.22 |
| 20 | KYJBNML | KYJBNML | Yes | 4.5 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.6, 6.4] | 3.6 6.4 | Yes | 5.91 |
| 2 | [1.3, 8.7] | 8.7 1.3 | Yes | 3.94 |
| 3 | [0.9, 9.1] | 0.9 9.1 | Yes | 6.63 |
| 4 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.48 |
| 5 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.78 |
| 6 | [4.8, 5.2] | 4.8 5.2 | Yes | 7.85 |
| 7 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.97 |
| 8 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.2 |
| 9 | [4.5, 5.5] | 4.5 5.5 | Yes | 5.87 |
| 10 | [4.6, 5.4] | 4.6 5.4 | Yes | 6.37 |
| 11 | [2.7, 7.3] | 2.7 7.3 | Yes | 5.81 |
| 12 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.93 |
| 13 | [1.4, 8.6] | 8.6 1.4 | Yes | 6.25 |
| 14 | [2.1, 7.9] | 7.9 2.1 | Yes | 4.73 |
| 15 | [1.2, 8.8] | 1.2 8.8 | Yes | 6.9 |
| 16 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.0 |
| 17 | [0.3, 9.7] | 9.7 0.3 | Yes | 8.45 |
| 18 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.62 |
| 19 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.61 |
| 20 | [2.3, 7.7] | 2.3 7.7 | Yes | 7.12 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ENV9SN3FO3JN | ENV9SN3FO3JN | Yes | 2.82 |
| 2 | OHKGMYPHYIGN | OHKGMYPHYIGN | Yes | 2.1 |
| 3 | W2K3FOTUKJTV | W2K3FOTUKJTV | Yes | 2.34 |
| 4 | 1J05I6W53LVR | 1J05I6W53LVR | Yes | 2.59 |
| 5 | KLID2DVRDLH8 | KLID2DVRDLH8 | Yes | 2.74 |
| 6 | 6O2SVCYFAW5C | 6O2SVCYFAW5C | Yes | 2.79 |
| 7 | BE68B3KK7QUA | BE68B3KK7QUA | Yes | 2.71 |
| 8 | XEQPTIPS66DS | XEQPTIPS66DS | Yes | 4.06 |
| 9 | R44OVXOK4462 | R44OVXOK4462 | Yes | 2.66 |
| 10 | 6I4DLZKHASDI | GI4DLZHASDI | No | 4.46 |
| 11 | SZ948AGDSOTC | SZ948AGDSOTC | Yes | 3.02 |
| 12 | OK2FID1T3J03 | OK2FID1T3J03 | Yes | 2.85 |
| 13 | AQ07L47QK5BE | AQ07L47QK5BE | Yes | 2.54 |
| 14 | N8UH6FE1I7JD | N8UH6FE1I7JD | Yes | 2.37 |
| 15 | PRKIJ91C9QGE | PRKIJ91C9QGE | Yes | 2.55 |
| 16 | SSOL3HEEL8XT | SSOL3HEEL8XT | Yes | 2.34 |
| 17 | YJT2H5KNH5RO | YJT2H5KNH5RO | Yes | 2.87 |
| 18 | OQN4M46FP3ZL | OQN4M46FP3ZL | Yes | 2.85 |
| 19 | LGGDCBIWLM4S | LGGDCBIWLM4S | Yes | 2.98 |
| 20 | 7W7PNLTCYM1L | 7W7PNLTCYM1L | Yes | 2.81 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 1.99 |
| 2 | 28 | 28 | Yes | 2.79 |
| 3 | 198 | 198 | Yes | 3.08 |
| 4 | 60 | 60 | Yes | 2.62 |
| 5 | 7 | 7 | Yes | 2.35 |
| 6 | 20 | 20 | Yes | 6.39 |
| 7 | 3 | 3 | Yes | 4.17 |
| 8 | 4 | 4 | Yes | 2.52 |
| 9 | 243 | 243 | Yes | 2.87 |
| 10 | 39 | 39 | Yes | 2.31 |
| 11 | 793 | 793 | Yes | 2.71 |
| 12 | 4096 | 1048576 | No | 9.42 |
| 13 | 1440 | 1440 | Yes | 2.81 |
| 14 | 26 | 26 | Yes | 8.66 |
| 15 | 6 | 6 | Yes | 2.66 |
| 16 | 9 | 9 | Yes | 3.5 |
| 17 | 23 | 23 | Yes | 2.42 |
| 18 | 16 | 16 | Yes | 2.26 |
| 19 | 60 | 60 | Yes | 2.22 |
| 20 | 64 | 64 | Yes | 2.41 |
