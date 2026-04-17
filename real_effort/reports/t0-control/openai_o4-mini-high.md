# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-19 10:22:44

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
| sudoku_game | 7828 | 38912 | 46740 | 0 | 20 | 39.23 | 784.85 |
| add_numbers | 3760 | 4228 | 7988 | 20 | 0 | 3.66 | 73.39 |
| counting_zeros | 7180 | 40960 | 48140 | 0 | 20 | 35.70 | 714.35 |
| task_decoding | 15220 | 23822 | 39042 | 15 | 5 | 22.47 | 449.69 |
| task_summation | 8440 | 17668 | 26108 | 19 | 1 | 13.65 | 273.25 |
| task_transcription | 3465 | 11019 | 14484 | 14 | 6 | 8.92 | 178.5 |
| task_sequences | 2421 | 11656 | 14077 | 19 | 1 | 9.80 | 196.0 |
| **TOTAL** | **48314** | **148265** | **196579** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 3 1 1 3 5 2 6 2 5 4 5 6 4 |  | No | 35.53 |
| 2 | 3 1 6 5 2 3 4 1 2 6 4 5 3 2 |  | No | 16.63 |
| 3 | 2 5 1 6 2 6 5 1 2 6 4 2 1 5 |  | No | 30.22 |
| 4 | 6 2 3 6 1 5 2 4 6 3 6 5 4 6 |  | No | 35.75 |
| 5 | 5 6 4 1 2 3 2 5 4 6 3 5 3 6 | TIMEOUT | No | 120.03 |
| 6 | 6 3 4 6 1 1 5 6 4 5 3 1 4 3 |  | No | 45.18 |
| 7 | 5 2 5 1 3 1 6 4 1 4 5 3 1 4 |  | No | 24.44 |
| 8 | 4 1 3 3 5 4 1 2 1 5 2 5 3 4 |  | No | 35.91 |
| 9 | 2 1 3 3 4 4 2 4 2 6 4 4 1 3 |  | No | 41.11 |
| 10 | 5 3 3 1 4 2 4 5 3 4 3 6 6 1 |  | No | 51.1 |
| 11 | 1 2 3 6 1 5 2 5 2 5 3 2 6 1 |  | No | 34.91 |
| 12 | 2 3 1 5 5 2 3 1 3 1 5 4 3 6 |  | No | 19.74 |
| 13 | 4 3 4 6 2 4 4 1 2 6 6 1 5 3 |  | No | 35.1 |
| 14 | 4 1 6 3 1 3 2 4 1 2 3 6 5 2 |  | No | 43.04 |
| 15 | 2 3 5 5 6 4 3 4 2 3 3 2 2 5 |  | No | 35.61 |
| 16 | 6 5 2 6 5 6 2 6 5 6 3 6 5 1 |  | No | 43.86 |
| 17 | 1 4 1 6 3 6 3 1 5 4 6 2 5 2 |  | No | 30.9 |
| 18 | 3 5 2 6 1 3 2 2 3 6 5 2 2 4 |  | No | 23.1 |
| 19 | 4 3 2 3 2 6 4 5 2 3 6 5 2 4 |  | No | 37.46 |
| 20 | 5 4 6 1 2 3 1 4 4 2 3 3 6 4 |  | No | 44.99 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 973 | 973 | Yes | 2.43 |
| 2 | 1932 | 1932 | Yes | 6.09 |
| 3 | 1599 | 1599 | Yes | 7.07 |
| 4 | 1410 | 1410 | Yes | 4.75 |
| 5 | 1698 | 1698 | Yes | 1.8 |
| 6 | 1623 | 1623 | Yes | 3.01 |
| 7 | 959 | 959 | Yes | 4.76 |
| 8 | 1096 | 1096 | Yes | 1.97 |
| 9 | 1944 | 1944 | Yes | 2.55 |
| 10 | 1378 | 1378 | Yes | 2.68 |
| 11 | 1719 | 1719 | Yes | 3.36 |
| 12 | 1677 | 1677 | Yes | 4.17 |
| 13 | 2048 | 2048 | Yes | 7.26 |
| 14 | 1165 | 1165 | Yes | 3.19 |
| 15 | 2312 | 2312 | Yes | 2.51 |
| 16 | 1808 | 1808 | Yes | 5.41 |
| 17 | 1491 | 1491 | Yes | 1.84 |
| 18 | 1615 | 1615 | Yes | 3.03 |
| 19 | 755 | 755 | Yes | 2.63 |
| 20 | 2002 | 2002 | Yes | 2.68 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 |  | No | 47.38 |
| 2 | 41 |  | No | 17.35 |
| 3 | 36 |  | No | 21.31 |
| 4 | 61 |  | No | 31.65 |
| 5 | 66 |  | No | 22.37 |
| 6 | 69 |  | No | 36.27 |
| 7 | 39 |  | No | 17.5 |
| 8 | 62 |  | No | 54.94 |
| 9 | 55 |  | No | 52.78 |
| 10 | 66 |  | No | 51.88 |
| 11 | 53 |  | No | 39.15 |
| 12 | 67 |  | No | 48.24 |
| 13 | 71 |  | No | 17.91 |
| 14 | 40 |  | No | 28.03 |
| 15 | 57 |  | No | 49.34 |
| 16 | 43 |  | No | 34.99 |
| 17 | 50 |  | No | 43.02 |
| 18 | 61 |  | No | 35.82 |
| 19 | 37 |  | No | 25.48 |
| 20 | 46 |  | No | 38.66 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OSMWKLQ | OSMWKLQ | Yes | 10.5 |
| 2 | KFJYODS | KFJYODS | Yes | 9.19 |
| 3 | YCQMWJB | YCQMWJB | Yes | 10.43 |
| 4 | SBGQMOD | SBGQMOD | Yes | 13.08 |
| 5 | OLXNWMD | OLXNWMD | Yes | 9.22 |
| 6 | QIWTPVZ | QIWTPVZ | Yes | 3.69 |
| 7 | CBEUPGF | CBEUPGF | Yes | 19.68 |
| 8 | SNFRKMD |  | No | 58.98 |
| 9 | GSQATEZ | GSQATEZ | Yes | 9.5 |
| 10 | ACJQDFZ | ACJQDFZ | Yes | 3.89 |
| 11 | YTVBHUK | YTVBHUK | Yes | 7.6 |
| 12 | WIOMBCH |  | No | 69.68 |
| 13 | DEOXWFY |  | No | 45.32 |
| 14 | CSLRYZK | CSLRYZK | Yes | 12.67 |
| 15 | KOXSCNT |  | No | 48.12 |
| 16 | WHGPCDU | WHGPCDU | Yes | 15.33 |
| 17 | LKHUMZF | LKHUMZF | Yes | 12.14 |
| 18 | ABWLPSG | ABWLPSG | Yes | 14.42 |
| 19 | ODTIMGC | ODTIMGC | Yes | 17.42 |
| 20 | SHOVDLI |  | No | 58.62 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 0.6 9.4 | Yes | 11.87 |
| 2 | [0.7, 9.3] | 0.7 9.3 | Yes | 15.04 |
| 3 | [1.6, 8.4] | 8.4 1.6 | Yes | 9.22 |
| 4 | [2.8, 7.2] | 2.8 7.2 | Yes | 9.23 |
| 5 | [2.1, 7.9] | 2.1 7.9 | Yes | 10.37 |
| 6 | [4.4, 5.6] | 5.6 4.4 | Yes | 8.62 |
| 7 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.23 |
| 8 | [3.7, 6.3] | 3.7 6.3 | Yes | 13.35 |
| 9 | [2.4, 7.6] | 2.4 7.6 | Yes | 12.26 |
| 10 | [4.2, 5.8] | 5.8 4.2 | Yes | 12.61 |
| 11 | [3.2, 6.8] | 3.2 6.8 | Yes | 12.39 |
| 12 | [0.6, 9.4] | 0.6 9.4 | Yes | 22.0 |
| 13 | [2.0, 8.0] | 8.0 2.0 | Yes | 11.83 |
| 14 | [1.3, 8.7] | 8.7 1.3 | Yes | 12.5 |
| 15 | [2.3, 7.7] | 2.3 7.7 | Yes | 12.76 |
| 16 | [2.5, 7.5] |  | No | 37.6 |
| 17 | [1.4, 8.6] | 1.4 8.6 | Yes | 12.58 |
| 18 | [0.4, 9.6] | 0.4 9.6 | Yes | 17.59 |
| 19 | [3.2, 6.8] | 3.2 6.8 | Yes | 8.61 |
| 20 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.39 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ESUB0ZK2LRBU | ESUB0ZK2LRBU | Yes | 4.31 |
| 2 | 2MDJ19ZI5EAH | 2MDJ19ZI5EAH | Yes | 3.06 |
| 3 | Z5PJP1F51YNY | Z5PJP1F51YNY | Yes | 3.9 |
| 4 | 5BOIPVVTU97X | 5BOIPVVTU97X | Yes | 4.02 |
| 5 | 0X0FXUNRHO0B | OXOFXUNRH00B | No | 15.43 |
| 6 | G0QJL3Q1O9JR | G0QJL3Q1O9JR | Yes | 3.51 |
| 7 | 94BGLWKRQCI2 | 94BGLWKRQC12 | No | 3.28 |
| 8 | HT7UFKT2LHCQ | HT7UFKT2LHCQ | Yes | 4.25 |
| 9 | 2H544NLFDI0X | 2H544NLFDIOX | No | 4.8 |
| 10 | WVVJ4E39A50A | WVVJ4E39A50A | Yes | 13.23 |
| 11 | NMJSXJGF4WKU | NMJSXJGF4WKU | Yes | 2.45 |
| 12 | CLTEKC6RJM3C | CLTEKC6RJM3C | Yes | 4.66 |
| 13 | VNYB1646RELN | VNYB1646RELN | Yes | 4.27 |
| 14 | KTOZXWXMISOK | KTOZXWXMISOK | Yes | 2.43 |
| 15 | G1034C659OAD | G1034C659OAD | Yes | 4.92 |
| 16 | XV7FWVOZYDR3 | XV7FWVOZYDR3 | Yes | 2.23 |
| 17 | 9VVUEJFP3Q4J | 9VVUEJFP3Q4J | Yes | 2.78 |
| 18 | QS0OYQXVIDJ5 |  | No | 62.64 |
| 19 | KKPXCLFITOM4 | KKPXCLFIT0M4 | No | 3.39 |
| 20 | QGDI6RKQUDBU |  | No | 28.85 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 4.17 |
| 2 | 23 | 23 | Yes | 5.51 |
| 3 | 64 | 64 | Yes | 10.19 |
| 4 | 1 | 1 | Yes | 9.48 |
| 5 | 19 | 19 | Yes | 9.62 |
| 6 | 4 | 4 | Yes | 10.85 |
| 7 | 793 | 793 | Yes | 6.94 |
| 8 | 6 | 6 | Yes | 8.23 |
| 9 | 16 | 16 | Yes | 7.05 |
| 10 | 67 | 67 | Yes | 6.18 |
| 11 | 243 | 243 | Yes | 6.12 |
| 12 | 4096 |  | No | 22.76 |
| 13 | 39 | 39 | Yes | 11.74 |
| 14 | 44 | 44 | Yes | 8.16 |
| 15 | 1440 | 1440 | Yes | 9.78 |
| 16 | 9 | 9 | Yes | 11.53 |
| 17 | 7680 | 7680 | Yes | 9.87 |
| 18 | 26 | 26 | Yes | 14.82 |
| 19 | 9 | 9 | Yes | 10.01 |
| 20 | 28 | 28 | Yes | 12.97 |
