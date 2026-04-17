# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 10:47:04

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 7020 | 36701 | 43721 | 5 | 15 | 22.95 | 459.29 |
| add_numbers | 3600 | 1879 | 5479 | 20 | 0 | 3.11 | 62.21 |
| counting_zeros | 6020 | 32949 | 38969 | 0 | 20 | 17.37 | 347.63 |
| task_decoding | 11760 | 3260 | 15020 | 20 | 0 | 4.28 | 85.74 |
| task_summation | 6960 | 6448 | 13408 | 20 | 0 | 5.89 | 118.01 |
| task_transcription | 3430 | 13386 | 16816 | 14 | 6 | 10.80 | 216.05 |
| task_sequences | 2721 | 4753 | 7474 | 19 | 1 | 5.30 | 105.93 |
| string_entry | 4020 | 31468 | 35488 | 5 | 15 | 24.59 | 491.94 |
| **TOTAL** | **45531** | **130844** | **176375** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 3 6 2 6 4 1 3 2 1 5 1 4 |  | No | 36.64 |
| 2 | 6 4 4 2 5 6 4 2 5 3 1 2 6 1 |  | No | 27.26 |
| 3 | 4 5 2 3 5 1 5 4 3 2 6 3 2 5 |  | No | 28.29 |
| 4 | 2 5 6 1 1 4 5 6 6 1 2 2 6 1 |  | No | 24.62 |
| 5 | 1 3 6 5 4 5 6 2 3 4 5 5 2 1 | 1 3 6 5 4 5 6 2 3 4 5 5 2 1 | Yes | 13.34 |
| 6 | 3 2 1 1 6 6 2 1 1 3 4 5 4 3 |  | No | 31.69 |
| 7 | 1 5 4 3 1 4 2 1 6 5 3 4 1 2 | 1 5 4 3 1 4 2 1 6 5 3 4 1 2 | Yes | 12.44 |
| 8 | 3 6 1 2 5 4 6 2 3 5 2 6 4 1 |  | No | 22.42 |
| 9 | 3 6 1 4 5 3 4 1 3 6 5 2 6 3 |  | No | 32.0 |
| 10 | 6 1 3 1 5 2 4 1 3 1 5 3 2 1 | 6 1 3 1 5 2 4 1 3 1 5 3 2 1 | Yes | 17.18 |
| 11 | 1 2 4 5 5 1 4 6 2 2 5 3 3 6 |  | No | 17.13 |
| 12 | 6 2 4 6 3 5 4 6 3 3 2 2 5 1 |  | No | 21.11 |
| 13 | 6 3 2 3 5 6 4 2 3 4 3 4 1 4 |  | No | 43.65 |
| 14 | 4 2 5 3 5 6 4 2 2 5 1 4 2 1 |  | No | 18.27 |
| 15 | 6 2 2 1 3 3 2 6 5 1 6 1 3 2 | 6 2 2 1 3 3 2 6 5 1 6 1 3 2 | Yes | 24.26 |
| 16 | 3 6 4 1 1 4 2 3 6 4 5 5 2 3 | 3 6 1 1 4 2 3 6 4 5 5 2 3 | No | 10.27 |
| 17 | 2 4 5 4 3 2 1 5 5 3 5 1 5 2 | 2 4 5 4 3 2 1 5 5 3 5 1 5 2 | Yes | 14.41 |
| 18 | 2 5 1 3 5 4 2 6 3 3 5 2 2 4 |  | No | 27.16 |
| 19 | 3 4 2 6 2 2 3 3 6 4 5 1 6 3 |  | No | 22.58 |
| 20 | 2 1 5 6 5 2 1 3 5 2 6 4 1 5 |  | No | 14.36 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1629 | 1629 | Yes | 3.19 |
| 2 | 2120 | 2120 | Yes | 3.91 |
| 3 | 1614 | 1614 | Yes | 1.52 |
| 4 | 1514 | 1514 | Yes | 3.19 |
| 5 | 1664 | 1664 | Yes | 1.61 |
| 6 | 2080 | 2080 | Yes | 3.82 |
| 7 | 1181 | 1181 | Yes | 2.89 |
| 8 | 1022 | 1022 | Yes | 4.03 |
| 9 | 1899 | 1899 | Yes | 3.35 |
| 10 | 2424 | 2424 | Yes | 2.59 |
| 11 | 2572 | 2572 | Yes | 3.34 |
| 12 | 1535 | 1535 | Yes | 2.7 |
| 13 | 1911 | 1911 | Yes | 2.95 |
| 14 | 1944 | 1944 | Yes | 3.27 |
| 15 | 1208 | 1208 | Yes | 3.29 |
| 16 | 1692 | 1692 | Yes | 4.06 |
| 17 | 1387 | 1387 | Yes | 2.81 |
| 18 | 2036 | 2036 | Yes | 3.01 |
| 19 | 1476 | 1476 | Yes | 3.05 |
| 20 | 2478 | 2478 | Yes | 3.53 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 |  | No | 18.7 |
| 2 | 59 |  | No | 25.59 |
| 3 | 68 | 67 | No | 9.87 |
| 4 | 66 |  | No | 31.04 |
| 5 | 65 | 67 | No | 10.73 |
| 6 | 46 |  | No | 35.62 |
| 7 | 45 |  | No | 24.46 |
| 8 | 40 | 38 | No | 22.55 |
| 9 | 37 | 36 | No | 15.48 |
| 10 | 62 | 57 | No | 5.45 |
| 11 | 62 |  | No | 14.58 |
| 12 | 40 |  | No | 19.78 |
| 13 | 38 | 36 | No | 16.53 |
| 14 | 39 |  | No | 17.84 |
| 15 | 42 | 40 | No | 6.92 |
| 16 | 44 | 45 | No | 7.67 |
| 17 | 72 | 63 | No | 7.3 |
| 18 | 42 |  | No | 21.47 |
| 19 | 51 |  | No | 16.04 |
| 20 | 45 |  | No | 19.72 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BDUXECP | BDUXECP | Yes | 3.66 |
| 2 | WQHELPM | WQHELPM | Yes | 3.7 |
| 3 | SHQRJBL | SHQRJBL | Yes | 3.76 |
| 4 | UISVJFZ | UISVJFZ | Yes | 4.26 |
| 5 | TSVFGHQ | TSVFGHQ | Yes | 5.56 |
| 6 | YDZULRV | YDZULRV | Yes | 4.19 |
| 7 | TMQNDZG | TMQNDZG | Yes | 4.62 |
| 8 | NVMWRKP | NVMWRKP | Yes | 4.35 |
| 9 | QGMKESI | QGMKESI | Yes | 4.44 |
| 10 | KLWHRDF | KLWHRDF | Yes | 4.82 |
| 11 | AGQFTZV | AGQFTZV | Yes | 3.99 |
| 12 | MKHCRWL | MKHCRWL | Yes | 2.41 |
| 13 | JVQTYXL | JVQTYXL | Yes | 5.48 |
| 14 | GMHAJNC | GMHAJNC | Yes | 5.33 |
| 15 | GHTEXAK | GHTEXAK | Yes | 4.55 |
| 16 | ABYWNOL | ABYWNOL | Yes | 4.38 |
| 17 | RLHGTOZ | RLHGTOZ | Yes | 4.6 |
| 18 | LKVWMEP | LKVWMEP | Yes | 5.11 |
| 19 | MWXFNZS | MWXFNZS | Yes | 4.61 |
| 20 | FQCEZBL | FQCEZBL | Yes | 1.71 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.2, 7.8] | 7.8 2.2 | Yes | 5.17 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.58 |
| 3 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.02 |
| 4 | [2.3, 7.7] | 7.7 2.3 | Yes | 6.3 |
| 5 | [1.1, 8.9] | 1.1 8.9 | Yes | 4.61 |
| 6 | [3.6, 6.4] | 6.4 3.6 | Yes | 4.69 |
| 7 | [3.6, 6.4] | 6.4 3.6 | Yes | 10.03 |
| 8 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.82 |
| 9 | [4.4, 5.6] | 4.4 5.6 | Yes | 4.36 |
| 10 | [2.9, 7.1] | 7.1 2.9 | Yes | 5.7 |
| 11 | [2.2, 7.8] | 7.8 2.2 | Yes | 5.14 |
| 12 | [2.1, 7.9] | 7.9 2.1 | Yes | 4.96 |
| 13 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.78 |
| 14 | [2.2, 7.8] | 2.2 7.8 | Yes | 7.7 |
| 15 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.23 |
| 16 | [3.1, 6.9] | 3.1 6.9 | Yes | 4.85 |
| 17 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.58 |
| 18 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.66 |
| 19 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.51 |
| 20 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.11 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5I1UW0ABH9RZ | 511UW0ABH9RZ | No | 12.71 |
| 2 | H5IANBEUCYRH | H5IANBEUCYRH | Yes | 8.94 |
| 3 | ZFNYXPC5LOT1 | ZFNYXPC5L0T1 | No | 3.88 |
| 4 | YFPPSLBDTU3S | YFPPSLBDTU3S | Yes | 12.55 |
| 5 | FTHO2K5M8S6R | FTHO2K5M8S6R | Yes | 5.86 |
| 6 | FOI53PYH0CH5 |  | No | 37.13 |
| 7 | YT22I8GTTG9M | YT22I8GTTG9M | Yes | 2.8 |
| 8 | 1MEGDIMQH97P | 1MEGDIMQH97P | Yes | 7.16 |
| 9 | 4FC49A3OJSV2 | 4FC49A3OJSV2 | Yes | 15.11 |
| 10 | JKQWWD42LLOI | JKQWWD42LLOI | Yes | 5.0 |
| 11 | JD5JREZ1D6RB | JD5JREZ1D6RB | Yes | 9.98 |
| 12 | ZF3ABHW02JYX | ZF3ABHW02JVX | No | 9.11 |
| 13 | UV17X8QCFM5V | UV17X8QCFM5V | Yes | 2.59 |
| 14 | 2J559P3HOFNM | 2J559P3HOFNM | Yes | 10.32 |
| 15 | NL0HYQOAEMG8 |  | No | 32.29 |
| 16 | RRJ2PGUB5A2B | RRJ2PGUB5A2B | Yes | 4.73 |
| 17 | SI8POEVMXJYG | SI8POEVMXJYG | Yes | 11.35 |
| 18 | LC5W003SWLB4 | LC5W003SWLB4 | Yes | 2.95 |
| 19 | ARXEOGSBVO8A | ARXEOGSBVO8A | Yes | 13.3 |
| 20 | PGFG6MMV4YA0 | PGFG6MMV4YAO | No | 8.17 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4096 |  | No | 26.46 |
| 2 | 23 | 23 | Yes | 3.32 |
| 3 | 5 | 5 | Yes | 3.42 |
| 4 | 19 | 19 | Yes | 3.66 |
| 5 | 3 | 3 | Yes | 6.92 |
| 6 | 198 | 198 | Yes | 3.79 |
| 7 | 3 | 3 | Yes | 4.65 |
| 8 | 7 | 7 | Yes | 2.79 |
| 9 | 26 | 26 | Yes | 12.43 |
| 10 | 65 | 65 | Yes | 1.85 |
| 11 | 4 | 4 | Yes | 3.57 |
| 12 | 793 | 793 | Yes | 3.42 |
| 13 | 60 | 60 | Yes | 3.6 |
| 14 | 9 | 9 | Yes | 3.75 |
| 15 | 1440 | 1440 | Yes | 3.18 |
| 16 | 4 | 4 | Yes | 3.52 |
| 17 | 28 | 28 | Yes | 3.85 |
| 18 | 243 | 243 | Yes | 2.92 |
| 19 | 44 | 44 | Yes | 3.77 |
| 20 | 73 | 73 | Yes | 5.07 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )\<<\))   |  | No | 33.04 |
| 2 | /<(\(<<)< | /<(\(<<)< | Yes | 19.1 |
| 3 | \/<<)\ << | \/<</\ << | No | 9.9 |
| 4 | )/(\(() ) |  | No | 37.56 |
| 5 | /_<<<<(\\ |  | No | 31.98 |
| 6 | (\ \ (\/_ |  | No | 30.14 |
| 7 | ()/_)(_<  | ()/_)(_< | No | 15.52 |
| 8 | _\/<)/( < |  | No | 35.19 |
| 9 | )//<_)_// | )//<_)_// | Yes | 10.04 |
| 10 | /<)<(_<_( | /<)<(_<_( | Yes | 8.51 |
| 11 | ( /)))((  |  | No | 34.63 |
| 12 | __\ <</)  |  | No | 37.06 |
| 13 | __)/ )_)  |  | No | 26.56 |
| 14 |  _ )/_<)( |  | No | 37.94 |
| 15 | ((<(<)) / | ((<(<)) / | Yes | 8.58 |
| 16 | /\()< /(\ |  | No | 34.76 |
| 17 | ( _(\(/\_ | ( _(\(/\\_ | No | 13.7 |
| 18 | //)_\_)<  | //)_\_)< | No | 19.32 |
| 19 | </__/<)/( | </__/<)/( | Yes | 18.22 |
| 20 | (/)_/)<)( |  | No | 30.12 |
