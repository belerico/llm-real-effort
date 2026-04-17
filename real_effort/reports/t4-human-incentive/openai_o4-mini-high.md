# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 9060 | 40960 | 50020 | 0 | 20 | 40.77 | 815.63 |
| add_numbers | 4580 | 4071 | 8651 | 20 | 0 | 3.53 | 70.67 |
| counting_zeros | 8000 | 40960 | 48960 | 0 | 20 | 32.54 | 651.08 |
| task_decoding | 16040 | 21409 | 37449 | 15 | 5 | 19.59 | 391.97 |
| task_summation | 9260 | 17432 | 26692 | 20 | 0 | 12.15 | 243.15 |
| task_transcription | 4285 | 6912 | 11197 | 16 | 4 | 4.17 | 83.49 |
| task_sequences | 3241 | 12395 | 15636 | 18 | 2 | 9.00 | 179.91 |
| **TOTAL** | **54466** | **144139** | **198605** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 6 5 1 4 5 3 4 5 3 2 5 4 |  | No | 34.89 |
| 2 | 3 5 4 6 4 2 5 4 3 2 5 6 3 2 |  | No | 24.63 |
| 3 | 2 6 3 1 4 6 5 2 6 1 4 6 1 3 |  | No | 20.11 |
| 4 | 6 4 2 5 4 3 6 1 2 1 5 3 3 2 |  | No | 36.18 |
| 5 | 6 2 3 5 1 4 5 6 5 6 1 4 5 3 |  | No | 51.57 |
| 6 | 6 4 3 5 4 3 1 6 5 1 4 2 5 1 |  | No | 34.36 |
| 7 | 4 5 3 4 5 6 6 2 6 5 5 1 2 6 |  | No | 38.81 |
| 8 | 3 5 5 6 1 3 5 4 3 1 5 6 2 1 |  | No | 42.8 |
| 9 | 6 4 2 2 5 1 5 6 2 1 4 2 5 1 |  | No | 48.29 |
| 10 | 5 4 2 1 3 2 5 6 5 4 3 1 3 2 |  | No | 41.44 |
| 11 | 3 4 5 6 4 1 5 1 2 3 1 4 6 5 |  | No | 51.35 |
| 12 | 6 3 6 1 6 4 4 5 2 5 4 3 4 2 |  | No | 47.28 |
| 13 | 6 3 2 6 3 5 3 6 4 5 1 2 6 4 |  | No | 33.42 |
| 14 | 4 2 3 6 1 6 3 6 1 4 1 5 6 3 |  | No | 42.71 |
| 15 | 4 2 1 5 2 4 3 2 6 3 6 1 2 3 |  | No | 58.02 |
| 16 | 2 4 3 5 4 2 2 3 2 4 6 1 5 6 |  | No | 50.32 |
| 17 | 3 5 3 2 3 4 2 3 6 5 1 1 6 2 |  | No | 51.17 |
| 18 | 4 1 3 5 6 2 6 4 1 5 6 1 5 6 |  | No | 40.2 |
| 19 | 4 4 5 6 3 4 3 3 2 6 5 4 4 5 |  | No | 20.94 |
| 20 | 6 3 3 5 3 1 2 6 3 1 1 4 6 3 |  | No | 46.92 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1305 | 1305 | Yes | 2.43 |
| 2 | 2350 | 2350 | Yes | 4.22 |
| 3 | 1485 | 1485 | Yes | 3.44 |
| 4 | 1800 | 1800 | Yes | 2.63 |
| 5 | 1629 | 1629 | Yes | 3.08 |
| 6 | 1847 | 1847 | Yes | 5.21 |
| 7 | 1551 | 1551 | Yes | 6.75 |
| 8 | 2245 | 2245 | Yes | 1.92 |
| 9 | 1572 | 1572 | Yes | 3.46 |
| 10 | 1838 | 1838 | Yes | 2.37 |
| 11 | 633 | 633 | Yes | 2.41 |
| 12 | 1352 | 1352 | Yes | 2.78 |
| 13 | 851 | 851 | Yes | 3.14 |
| 14 | 1992 | 1992 | Yes | 2.24 |
| 15 | 1209 | 1209 | Yes | 4.35 |
| 16 | 1360 | 1360 | Yes | 2.57 |
| 17 | 1716 | 1716 | Yes | 7.91 |
| 18 | 1478 | 1478 | Yes | 2.55 |
| 19 | 1120 | 1120 | Yes | 4.52 |
| 20 | 1455 | 1455 | Yes | 2.59 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 47 |  | No | 22.72 |
| 2 | 35 |  | No | 34.38 |
| 3 | 42 |  | No | 50.76 |
| 4 | 38 |  | No | 18.28 |
| 5 | 73 |  | No | 62.75 |
| 6 | 54 |  | No | 34.62 |
| 7 | 60 |  | No | 25.39 |
| 8 | 38 |  | No | 23.78 |
| 9 | 35 |  | No | 16.88 |
| 10 | 54 |  | No | 27.28 |
| 11 | 43 |  | No | 16.2 |
| 12 | 36 |  | No | 32.62 |
| 13 | 65 |  | No | 45.77 |
| 14 | 58 |  | No | 20.98 |
| 15 | 56 |  | No | 34.31 |
| 16 | 35 |  | No | 44.64 |
| 17 | 47 |  | No | 24.73 |
| 18 | 57 |  | No | 40.23 |
| 19 | 73 |  | No | 44.72 |
| 20 | 75 |  | No | 29.71 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YQSCHRA | YQSCHRA | Yes | 9.59 |
| 2 | MOWYTZR | MOWYTZR | Yes | 12.78 |
| 3 | BPUJHIF | BPUJHIF | Yes | 8.82 |
| 4 | UOTJHRF | UOTJHRF | Yes | 13.85 |
| 5 | LMNFGST | LMNFGST | Yes | 8.28 |
| 6 | NTLYKPE |  | No | 44.91 |
| 7 | YKZREAP |  | No | 38.8 |
| 8 | DPZOXSC | DPZOXSC | Yes | 6.41 |
| 9 | NJPYLDF |  | No | 37.31 |
| 10 | ZJNAYWM | ZJNAYWM | Yes | 11.62 |
| 11 | VPDKAYH | VPDKAYH | Yes | 12.08 |
| 12 | NGIRJDS | NGIRJDS | Yes | 22.73 |
| 13 | DKPRBFQ | DKPRBFQ | Yes | 21.42 |
| 14 | DBEJYTF | DBEJYTF | Yes | 18.77 |
| 15 | WBISXZL | WBISXZL | Yes | 8.4 |
| 16 | JSOPNQU |  | No | 49.63 |
| 17 | SDGPYZE | SDGPYZE | Yes | 4.18 |
| 18 | KNJCDXH | KNJCDXH | Yes | 11.5 |
| 19 | AZJXTHG | AZJXTHG | Yes | 11.79 |
| 20 | ILJEUMV |  | No | 38.9 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 3.3 6.7 | Yes | 11.98 |
| 2 | [3.5, 6.5] | 6.5 3.5 | Yes | 8.92 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 12.27 |
| 4 | [2.7, 7.3] | 2.7 7.3 | Yes | 9.56 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.34 |
| 6 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.33 |
| 7 | [0.4, 9.6] | 0.4 9.6 | Yes | 19.06 |
| 8 | [1.5, 8.5] | 1.5 8.5 | Yes | 8.08 |
| 9 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.67 |
| 10 | [0.6, 9.4] | 0.6 9.4 | Yes | 14.01 |
| 11 | [0.9, 9.1] | 0.9 9.1 | Yes | 11.27 |
| 12 | [2.3, 7.7] | 2.3 7.7 | Yes | 11.0 |
| 13 | [0.5, 9.5] | 0.5 9.5 | Yes | 9.18 |
| 14 | [4.7, 5.3] | 4.7 5.3 | Yes | 18.31 |
| 15 | [2.8, 7.2] | 7.2 2.8 | Yes | 12.5 |
| 16 | [4.9, 5.1] | 5.1 4.9 | Yes | 21.19 |
| 17 | [1.1, 8.9] | 1.1 8.9 | Yes | 10.84 |
| 18 | [2.6, 7.4] | 2.6 7.4 | Yes | 11.71 |
| 19 | [3.5, 6.5] | 3.5 6.5 | Yes | 12.43 |
| 20 | [3.8, 6.2] | 6.2 3.8 | Yes | 12.3 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | A4ZSPVG8SMY7 | A4ZSPVG8SMY7 | Yes | 2.69 |
| 2 | X700VHND3Y48 | X700VHND3Y48 | Yes | 3.78 |
| 3 | 1S6EG787VXMG | 1S6EG787VXMG | Yes | 3.46 |
| 4 | OZW9NKRPTAAQ | OZW9NKRPTAAQ | Yes | 2.78 |
| 5 | VVWAXC2OKAHU | VVWAXC20KAHU | No | 2.94 |
| 6 | C2SNGBL5NXH8 | C2SNGBL5NXH8 | Yes | 2.41 |
| 7 | TXS9QGXYHPYV | TXS9QGXYHPYV | Yes | 2.75 |
| 8 | CO4682AUGC5U | CO4682AUGC5U | Yes | 1.76 |
| 9 | HXGW4CEBXE1Z | HXGW4CEBXE1Z | Yes | 3.56 |
| 10 | ZHAOX6CGR5SL | ZHAOX6CGR5SL | Yes | 2.41 |
| 11 | SMSTSOFT8VOY | SMSTSOFT8VOY | Yes | 19.21 |
| 12 | SCSNE114TFCH | SCSNE114TFCH | Yes | 2.36 |
| 13 | 5FR3I4TGBKJB | 5FR3I4TGBKJB | Yes | 4.12 |
| 14 | 6XTVYXU81J4P | 6XTVYXU81J4P | Yes | 3.73 |
| 15 | XF88JJDPFH6T | XF88JJD PFH6T | No | 6.4 |
| 16 | SW89F74I354W | SW89F74I354W | Yes | 2.41 |
| 17 | SJNMJV1IF2DB | SJNMJV11F2DB | No | 3.26 |
| 18 | 7OLU6U8X10PS | 70LU6U8X10PS | No | 3.54 |
| 19 | 8E9R6RQFM3XM | 8E9R6RQFM3XM | Yes | 3.72 |
| 20 | JRK4C6ZZQMSD | JRK4C6ZZQMSD | Yes | 6.08 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 7.43 |
| 2 | 65 | 65 | Yes | 7.86 |
| 3 | 3 | 3 | Yes | 17.57 |
| 4 | 36 | 36 | Yes | 4.77 |
| 5 | 3 | 3 | Yes | 7.01 |
| 6 | 6 | 6 | Yes | 8.47 |
| 7 | 793 | 793 | Yes | 7.66 |
| 8 | 4096 |  | No | 31.94 |
| 9 | 26 | 26 | Yes | 7.32 |
| 10 | 20 | 20 | Yes | 9.68 |
| 11 | 67 | 67 | Yes | 2.79 |
| 12 | 5 | 5 | Yes | 8.29 |
| 13 | 19 | 19 | Yes | 7.91 |
| 14 | 60 | 60 | Yes | 9.12 |
| 15 | 4 | 4 | Yes | 5.68 |
| 16 | 39 | 42 | No | 7.63 |
| 17 | 7 | 7 | Yes | 2.69 |
| 18 | 1440 | 1440 | Yes | 5.96 |
| 19 | 9 | 9 | Yes | 10.01 |
| 20 | 1 | 1 | Yes | 10.12 |
