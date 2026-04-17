# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-19 10:04:48

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
| sudoku_game | 8060 | 30465 | 38525 | 1 | 19 | 21.90 | 438.1 |
| add_numbers | 3980 | 3635 | 7615 | 20 | 0 | 3.82 | 76.42 |
| counting_zeros | 6920 | 28070 | 34990 | 11 | 9 | 17.96 | 359.55 |
| task_decoding | 13360 | 8039 | 21399 | 17 | 3 | 6.54 | 131.05 |
| task_summation | 7280 | 21529 | 28809 | 20 | 0 | 14.12 | 282.61 |
| task_transcription | 4128 | 4756 | 8884 | 11 | 9 | 4.95 | 99.14 |
| task_sequences | 3240 | 13825 | 17065 | 16 | 4 | 10.35 | 206.91 |
| **TOTAL** | **46968** | **110319** | **157287** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 5 3 1 4 6 3 1 2 4 6 2 4 | 5 1 3 2 1 4 6 3 1 2 4 6 2 4 | No | 19.93 |
| 2 | 5 4 6 4 2 3 1 2 2 6 4 5 1 3 | 6 4 5 2 1 3 4 2 4 6 2 5 1 3 | No | 25.2 |
| 3 | 3 4 1 2 6 1 5 6 3 1 5 2 5 3 | 3 4 1 2 1 6 6 5 3 5 1 2 3 5 | No | 23.18 |
| 4 | 3 6 2 5 6 3 4 1 4 6 3 6 1 3 | 3 6 2 6 3 5 4 1 4 6 3 6 1 3 | No | 23.37 |
| 5 | 6 5 4 3 3 5 3 2 6 5 4 1 4 2 | 6 5 3 4 3 5 3 2 6 4 5 1 4 2 | No | 19.04 |
| 6 | 5 3 2 6 4 3 3 6 1 1 4 1 3 4 | 5 3 2 6 3 4 1 6 3 4 1 1 3 4 | No | 18.19 |
| 7 | 3 2 5 1 2 4 4 3 5 3 1 1 5 3 | 3 2 5 2 4 3 1 5 3 | No | 17.94 |
| 8 | 4 6 3 1 5 2 6 4 3 1 4 2 1 2 | 6 3 4 1 5 2 6 4 1 6 3 2 1 2 | No | 27.3 |
| 9 | 1 5 1 2 4 6 2 1 2 3 2 3 4 4 | 1 5 1 2 4 6 2 1 3 2 4 2 3 | No | 14.45 |
| 10 | 6 1 5 3 1 6 1 2 3 2 5 2 6 1 | 6 1 5 3 2 6 1 1 2 3 2 5 2 6 1 | No | 24.43 |
| 11 | 5 6 2 5 4 2 6 4 5 2 1 3 4 3 | 6 5 5 2 4 5 2 4 6 2 3 1 4 3 | No | 16.42 |
| 12 | 5 2 1 5 4 3 6 4 1 3 6 2 1 2 | 5 2 1 5 3 4 6 6 1 3 2 1 2 | No | 22.99 |
| 13 | 2 6 1 2 6 1 5 6 4 1 3 2 6 4 | 2 6 1 2 6 1 5 6 4 1 3 2 6 4 | Yes | 21.36 |
| 14 | 3 2 5 2 5 2 1 2 6 4 1 5 6 2 | 3 5 2 2 5 2 1 1 6 2 5 4 6 2 | No | 20.05 |
| 15 | 5 1 3 3 6 3 3 1 2 6 1 4 5 1 | 3 1 5 3 6 3 3 1 1 6 2 4 5 1 | No | 25.65 |
| 16 | 5 6 1 2 2 5 6 4 2 3 3 1 6 4 | 5 6 1 2 5 6 4 2 3 3 6 1 4 | No | 26.77 |
| 17 | 5 3 6 3 5 4 2 4 5 1 6 3 5 3 | 6 5 3 5 3 4 4 2 5 1 6 3 3 5 | No | 22.26 |
| 18 | 2 5 4 1 3 1 4 4 2 1 6 3 3 2 | 1 5 3 4 2 1 4 2 3 6 3 2 | No | 20.78 |
| 19 | 6 1 3 2 1 5 6 4 2 6 1 6 4 5 | 6 1 3 2 1 5 6 4 2 6 1 6 5 4 4 | No | 28.31 |
| 20 | 5 4 3 1 3 5 1 3 5 2 1 5 1 2 | 4 5 3 5 3 1 3 5 2 1 5 1 2 | No | 20.31 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1770 | 1770 | Yes | 4.07 |
| 2 | 765 | 765 | Yes | 4.4 |
| 3 | 2454 | 2454 | Yes | 3.63 |
| 4 | 1134 | 1134 | Yes | 5.45 |
| 5 | 1247 | 1247 | Yes | 3.52 |
| 6 | 1682 | 1682 | Yes | 3.66 |
| 7 | 1355 | 1355 | Yes | 3.43 |
| 8 | 962 | 962 | Yes | 2.97 |
| 9 | 1938 | 1938 | Yes | 3.62 |
| 10 | 1619 | 1619 | Yes | 3.6 |
| 11 | 1386 | 1386 | Yes | 4.34 |
| 12 | 1739 | 1739 | Yes | 3.36 |
| 13 | 2328 | 2328 | Yes | 2.9 |
| 14 | 1297 | 1297 | Yes | 3.4 |
| 15 | 1252 | 1252 | Yes | 3.58 |
| 16 | 1896 | 1896 | Yes | 3.66 |
| 17 | 2260 | 2260 | Yes | 5.8 |
| 18 | 1153 | 1153 | Yes | 3.11 |
| 19 | 1464 | 1464 | Yes | 4.45 |
| 20 | 1394 | 1394 | Yes | 3.39 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 | I'll count all the zeros (0s) in the image:  Row 1: 0 1 1 1 1 1 0 1 0 1 (3 zeros) Row 2: 1 0 1 1 1 1 1 0 0 0 (4 zeros) Row 3: 1 0 0 1 1 1 0 1 1 0 (4 zeros) Row 4: 0 0 1 0 1 0 1 1 1 1 (4 zeros) Row 5: 1 1 1 1 0 0 0 0 1 0 (5 zeros) Row 6: 1 1 0 1 0 0 1 1 1 1 (3 zeros) Row 7: 1 1 0 0 1 1 1 | No | 26.01 |
| 2 | 71 | 70 | No | 13.45 |
| 3 | 62 | 62 | Yes | 19.59 |
| 4 | 72 | 72 | Yes | 22.57 |
| 5 | 59 | 59 | Yes | 20.29 |
| 6 | 49 | 50 | No | 17.46 |
| 7 | 56 | 56 | Yes | 20.54 |
| 8 | 39 | 39 | Yes | 19.38 |
| 9 | 73 | 73 | Yes | 19.55 |
| 10 | 47 | 47 | Yes | 16.86 |
| 11 | 42 | 42 | Yes | 18.87 |
| 12 | 68 | 67 | No | 9.15 |
| 13 | 36 | 36 | Yes | 19.16 |
| 14 | 46 | 46 | Yes | 9.98 |
| 15 | 57 | 57 | Yes | 19.94 |
| 16 | 72 | 71 | No | 19.61 |
| 17 | 72 | 67 | No | 20.21 |
| 18 | 49 | 50 | No | 14.64 |
| 19 | 72 | 69 | No | 15.85 |
| 20 | 59 | 58 | No | 16.14 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BKDXPVF | BKDXPVF | Yes | 4.66 |
| 2 | YNVUERS | YNVUERS | Yes | 6.43 |
| 3 | RNTBJSW | RNTBJSW | Yes | 7.77 |
| 4 | XKBWHGS | XKBWHGS | Yes | 4.59 |
| 5 | QYTPUHN | QTYPUHN | No | 5.55 |
| 6 | PWRIYLX | PWRIYLX | Yes | 5.5 |
| 7 | SMWUGPE | SMWUGPE | Yes | 7.86 |
| 8 | OGESKMT | OGESКMT | No | 8.84 |
| 9 | VBLFGYU | VBLFGYU | Yes | 5.12 |
| 10 | JGUMQFC | JGUMQFC | Yes | 5.98 |
| 11 | CUWDZTF | CUWDZTF | Yes | 5.85 |
| 12 | KXSVCNQ | KXSVCNQ | Yes | 5.27 |
| 13 | IVQARBM | IVQARBM | Yes | 5.66 |
| 14 | XJETNGB | XJETNGB | Yes | 5.61 |
| 15 | EWVRSJT | EWVRSJT | Yes | 7.82 |
| 16 | OANQLDX | OANQLDX | Yes | 7.02 |
| 17 | LCMYBIS | LCMYBIS | Yes | 6.95 |
| 18 | PSCZNMV | PSCZNMV | Yes | 5.54 |
| 19 | SVRUHYO | SVRUOHY | No | 10.81 |
| 20 | KACIJXO | KACIJXO | Yes | 8.0 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 3.5 6.5 | Yes | 12.5 |
| 2 | [3.3, 6.7] | 6.7 3.3 | Yes | 10.31 |
| 3 | [1.8, 8.2] | 8.2 1.8 | Yes | 19.0 |
| 4 | [4.1, 5.9] | 4.1 5.9 | Yes | 15.68 |
| 5 | [2.8, 7.2] | 7.2 2.8 | Yes | 11.0 |
| 6 | [0.2, 9.8] | 9.8 0.2 | Yes | 11.2 |
| 7 | [0.1, 9.9] | 9.9 0.1 | Yes | 13.98 |
| 8 | [4.1, 5.9] | 4.1 5.9 | Yes | 14.97 |
| 9 | [0.2, 9.8] | 9.8 0.2 | Yes | 12.05 |
| 10 | [4.2, 5.8] | 5.8 4.2 | Yes | 11.61 |
| 11 | [4.1, 5.9] | 4.1 5.9 | Yes | 14.57 |
| 12 | [4.2, 5.8] | 4.2 5.8 | Yes | 16.78 |
| 13 | [2.4, 7.6] | 2.4 7.6 | Yes | 14.43 |
| 14 | [3.0, 7.0] | 7.0 3.0 | Yes | 14.55 |
| 15 | [1.8, 8.2] | 8.2 1.8 | Yes | 16.06 |
| 16 | [3.5, 6.5] | 3.5 6.5 | Yes | 13.11 |
| 17 | [2.4, 7.6] | 7.6 2.4 | Yes | 16.65 |
| 18 | [0.9, 9.1] | 0.9 9.1 | Yes | 18.25 |
| 19 | [3.8, 6.2] | 6.2 3.8 | Yes | 11.98 |
| 20 | [1.7, 8.3] | 1.7 8.3 | Yes | 13.74 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TQTWMR6FX3PV | TOTWMR8FX3PV | No | 6.83 |
| 2 | 13FM2JSAA579 | 13FM2JSAA579 | Yes | 4.25 |
| 3 | IICN8A3XU3ZL | IICN8A3XU3ZL | Yes | 4.82 |
| 4 | 0AI59SG11F9C | 0AI59SG11F9C | Yes | 6.76 |
| 5 | EM0MAVOP43GF | EM0MAVOP43GF | Yes | 4.66 |
| 6 | R5V9J40N3KQY | R5V9J40N3KOY | No | 4.37 |
| 7 | DEAT5MR0W7QV | DEAT5MROW7QV | No | 3.88 |
| 8 | EE1XE5CWF4VU | EE1XE5CWF4VU | Yes | 4.05 |
| 9 | R7QRTGJ1T6A1 | R7ORTGJ1T6A1 | No | 5.57 |
| 10 | RK6X8IMPLQ4F | RK6X8IMPLO4F | No | 4.67 |
| 11 | YTGMS5V4GFRA | YTGMS35V4GFRA | No | 4.06 |
| 12 | 0S4L0C6SYC2M | OS4LOC6SYC2M | No | 4.54 |
| 13 | E6Y0XF29WH0Z | E6Y0XF29WH0Z | Yes | 4.94 |
| 14 | G47U4T29UKY7 | G47U4T29UKY7 | Yes | 5.33 |
| 15 | PZGEEGC67392 | PZGEEGC67392 | Yes | 4.34 |
| 16 | A0RH2E79M6OW | A0RH2E79M6OW | Yes | 5.95 |
| 17 | LHIPDU2SVXG6 | LHIPDU2SVXG6 | Yes | 4.79 |
| 18 | 0OTESOARAWNZ | OOTESOARAWNZ | No | 4.01 |
| 19 | 0YQIE9OXT13Q | 0YQIE9OXT13Q | Yes | 5.56 |
| 20 | 2O5CEEAV7DKH | 205CEEAV7DKH | No | 5.64 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 8.78 |
| 2 | 9 | 9 | Yes | 9.95 |
| 3 | 793 | 793 | Yes | 5.61 |
| 4 | 26 | 42 | No | 25.41 |
| 5 | 198 | 198 | Yes | 16.67 |
| 6 | 3 | 3 | Yes | 7.65 |
| 7 | 3 | 3 | Yes | 14.95 |
| 8 | 7680 | 7680 | Yes | 6.49 |
| 9 | 64 | 42 | No | 9.67 |
| 10 | 39 | 39 | Yes | 15.38 |
| 11 | 5 | 5 | Yes | 5.73 |
| 12 | 10 | 9 | No | 9.56 |
| 13 | 28 | 28 | Yes | 15.47 |
| 14 | 16 | 16 | Yes | 5.74 |
| 15 | 6 | 6 | Yes | 6.21 |
| 16 | 31 | 31 | Yes | 5.59 |
| 17 | 19 | 19 | Yes | 5.59 |
| 18 | 67 | 67 | Yes | 4.76 |
| 19 | 20 | 42 | No | 21.97 |
| 20 | 9 | 9 | Yes | 5.72 |
