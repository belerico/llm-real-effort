# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-19 10:37:38

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
| sudoku_game | 6720 | 40960 | 47680 | 0 | 20 | 61.68 | 1233.86 |
| add_numbers | 3300 | 4339 | 7639 | 20 | 0 | 5.95 | 119.11 |
| counting_zeros | 6725 | 32500 | 39225 | 0 | 20 | 51.93 | 1038.94 |
| task_decoding | 11460 | 15083 | 26543 | 20 | 0 | 16.11 | 322.5 |
| task_summation | 6660 | 13107 | 19767 | 20 | 0 | 12.63 | 252.76 |
| task_transcription | 3121 | 15854 | 18975 | 14 | 6 | 14.75 | 295.09 |
| task_sequences | 2420 | 17430 | 19850 | 11 | 9 | 15.05 | 301.0 |
| **TOTAL** | **40406** | **139273** | **179679** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 6 3 4 1 5 2 5 6 1 1 6 3 4 |  | No | 52.34 |
| 2 | 6 1 4 2 6 1 5 2 6 1 5 4 5 2 |  | No | 66.36 |
| 3 | 2 5 3 4 4 2 5 5 4 2 6 6 5 6 |  | No | 57.45 |
| 4 | 5 1 6 3 1 3 6 4 1 4 3 4 5 3 |  | No | 62.23 |
| 5 | 1 3 6 4 6 3 5 4 4 2 3 2 3 4 |  | No | 65.29 |
| 6 | 6 3 1 3 6 4 2 4 3 2 4 1 1 3 |  | No | 65.46 |
| 7 | 2 1 2 3 4 6 1 6 2 3 6 2 3 1 |  | No | 56.56 |
| 8 | 3 6 2 5 2 1 3 1 2 4 3 1 6 4 |  | No | 53.79 |
| 9 | 6 5 3 2 6 3 4 1 3 6 5 6 3 2 |  | No | 57.15 |
| 10 | 4 3 2 1 2 6 3 5 3 1 4 6 3 2 |  | No | 62.97 |
| 11 | 5 4 1 3 5 3 4 6 6 3 4 3 6 2 |  | No | 69.86 |
| 12 | 5 2 4 5 2 4 5 3 4 3 5 5 1 4 |  | No | 65.67 |
| 13 | 1 6 3 3 4 1 2 1 3 5 4 6 2 4 |  | No | 55.34 |
| 14 | 4 6 6 4 3 2 3 2 5 6 5 4 4 5 |  | No | 70.17 |
| 15 | 5 4 1 3 4 5 2 6 4 4 2 6 3 2 |  | No | 60.65 |
| 16 | 1 3 1 4 6 1 4 5 1 3 5 2 2 1 |  | No | 64.66 |
| 17 | 2 3 4 3 1 2 4 6 2 5 6 4 1 4 |  | No | 61.05 |
| 18 | 2 5 6 1 4 6 3 6 1 2 5 6 5 2 |  | No | 59.67 |
| 19 | 1 5 5 6 3 1 5 2 6 4 5 1 3 5 |  | No | 60.21 |
| 20 | 4 2 2 3 1 3 6 3 6 5 5 3 2 6 |  | No | 66.77 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2094 | 2094 | Yes | 8.36 |
| 2 | 1061 | 1061 | Yes | 4.15 |
| 3 | 1281 | 1281 | Yes | 9.69 |
| 4 | 2411 | 2411 | Yes | 5.28 |
| 5 | 1809 | 1809 | Yes | 8.99 |
| 6 | 1639 | 1639 | Yes | 5.97 |
| 7 | 1700 | 1700 | Yes | 7.84 |
| 8 | 1994 | 1994 | Yes | 4.68 |
| 9 | 941 | 941 | Yes | 5.26 |
| 10 | 1442 | 1442 | Yes | 4.62 |
| 11 | 1286 | 1286 | Yes | 6.01 |
| 12 | 1781 | 1781 | Yes | 4.01 |
| 13 | 1254 | 1254 | Yes | 7.91 |
| 14 | 1507 | 1507 | Yes | 3.96 |
| 15 | 2319 | 2319 | Yes | 8.33 |
| 16 | 1078 | 1078 | Yes | 3.99 |
| 17 | 2300 | 2300 | Yes | 5.6 |
| 18 | 1636 | 1636 | Yes | 6.29 |
| 19 | 2059 | 2059 | Yes | 3.34 |
| 20 | 2151 | 2151 | Yes | 4.74 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 |  | No | 76.57 |
| 2 | 70 | TIMEOUT | No | 120.02 |
| 3 | 57 | 67 | No | 29.88 |
| 4 | 37 | 67 | No | 19.95 |
| 5 | 70 | 67 | No | 20.34 |
| 6 | 43 |  | No | 39.21 |
| 7 | 65 |  | No | 90.81 |
| 8 | 65 | 67 | No | 23.71 |
| 9 | 57 | 67 | No | 28.09 |
| 10 | 73 | 67 | No | 39.33 |
| 11 | 56 |  | No | 67.21 |
| 12 | 47 | 67 | No | 33.53 |
| 13 | 59 | 67 | No | 22.83 |
| 14 | 62 | 67 | No | 31.63 |
| 15 | 66 |  | No | 75.15 |
| 16 | 64 | 67 | No | 35.76 |
| 17 | 46 |  | No | 87.41 |
| 18 | 58 |  | No | 84.8 |
| 19 | 35 |  | No | 83.71 |
| 20 | 68 | 67 | No | 28.67 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HGKSWEU | HGKSWEU | Yes | 17.23 |
| 2 | AHVXCWE | AHVXCWE | Yes | 16.36 |
| 3 | MFDYVTA | MFDYVTA | Yes | 16.88 |
| 4 | BUPVLHJ | BUPVLHJ | Yes | 16.36 |
| 5 | SYDHBGN | SYDHBGN | Yes | 26.64 |
| 6 | RJFQESV | RJFQESV | Yes | 13.57 |
| 7 | SZFKTDB | SZFKTDB | Yes | 16.2 |
| 8 | BOJFAPS | BOJFAPS | Yes | 11.31 |
| 9 | RFTMUOB | RFTMUOB | Yes | 20.41 |
| 10 | OYZKWPQ | OYZKWPQ | Yes | 23.31 |
| 11 | PKRQOIH | PKRQOIH | Yes | 17.33 |
| 12 | UCNKRWA | UCNKRWA | Yes | 13.62 |
| 13 | WOHNDZI | WOHNDZI | Yes | 14.52 |
| 14 | MNPRKZG | MNPRKZG | Yes | 14.37 |
| 15 | MZWIAUO | MZWIAUO | Yes | 16.41 |
| 16 | MFGDCSZ | MFGDCSZ | Yes | 13.9 |
| 17 | PWYLIVX | PWYLIVX | Yes | 12.77 |
| 18 | IXNVZRM | IXNVZRM | Yes | 13.07 |
| 19 | AYBGQPN | AYBGQPN | Yes | 12.27 |
| 20 | YHDGXPW | YHDGXPW | Yes | 15.75 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.2, 6.8] | 3.2 6.8 | Yes | 15.75 |
| 2 | [3.0, 7.0] | 7.0 3.0 | Yes | 14.87 |
| 3 | [2.2, 7.8] | 2.2 7.8 | Yes | 7.76 |
| 4 | [4.5, 5.5] | 5.5 4.5 | Yes | 12.2 |
| 5 | [3.1, 6.9] | 3.1 6.9 | Yes | 11.16 |
| 6 | [1.2, 8.8] | 8.8 1.2 | Yes | 18.14 |
| 7 | [2.1, 7.9] | 7.9 2.1 | Yes | 14.54 |
| 8 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.6 |
| 9 | [1.0, 9.0] | 1.0 9.0 | Yes | 15.33 |
| 10 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.67 |
| 11 | [0.9, 9.1] | 0.9 9.1 | Yes | 16.04 |
| 12 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.59 |
| 13 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.68 |
| 14 | [2.6, 7.4] | 2.6 7.4 | Yes | 14.41 |
| 15 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.69 |
| 16 | [3.0, 7.0] | 7.0 3.0 | Yes | 13.49 |
| 17 | [0.8, 9.2] | 0.8 9.2 | Yes | 17.18 |
| 18 | [4.7, 5.3] | 5.3 4.7 | Yes | 8.52 |
| 19 | [2.8, 7.2] | 7.2 2.8 | Yes | 11.66 |
| 20 | [3.7, 6.3] | 3.7 6.3 | Yes | 11.28 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KGMUZ8EDNOMP | KGMUZ8EDNOMP | Yes | 6.1 |
| 2 | M7FIEC5B4TZR | M7FIEC5B4TZR | Yes | 18.94 |
| 3 | VJSNPWR0UDAA | VJSNPWROUDAA | No | 6.67 |
| 4 | IN3YHL8SWFP3 | IN3YHL8SWFP3 | Yes | 6.64 |
| 5 | MX4UPQ3LMGEV | MX4UPQ3LMGEV | Yes | 4.63 |
| 6 | 0YGDO2D23D7A | OYGD02D23D7A | No | 24.27 |
| 7 | YURKUA324651 | YURKUA324651 | Yes | 8.27 |
| 8 | V7C73HGK2R7C | V7C73HGK2R7C | Yes | 8.83 |
| 9 | RPTRJIKCSY9N |  | No | 51.99 |
| 10 | HMRDAXTZMO5A | HMRDAXTZMO5A | Yes | 12.89 |
| 11 | VOD16128BJ6O | VOD16128BJ60 | No | 22.84 |
| 12 | C27V2RSHNQW6 | C27V2RSHNQW6 | Yes | 8.68 |
| 13 | 8PSVV7QGIPXZ | 8PSVV7QGIPXZ | Yes | 11.79 |
| 14 | E2DD73K58HJR | E2DD73K58HJR | Yes | 8.7 |
| 15 | RP331WSDWB6G | RP331WSDWB6G | Yes | 8.99 |
| 16 | CNKRI4KIMORI | CNKRI4KIMORI | Yes | 17.21 |
| 17 | Y18O6PLBGDHV | Y18OGPLEGDHV | No | 21.52 |
| 18 | DR6AX33OEC0Q | DR6AX33OEC0Q | Yes | 14.82 |
| 19 | PZ29QUYX641R | PZ29QUYX641R | Yes | 9.62 |
| 20 | CQICXIVOV9DQ | COICXIVOV9DQ | No | 21.56 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 12.59 |
| 2 | 243 | 42 | No | 10.39 |
| 3 | 64 | 42 | No | 9.41 |
| 4 | 31 | 31 | Yes | 5.35 |
| 5 | 16 | 16 | Yes | 13.21 |
| 6 | 65 | 65 | Yes | 11.95 |
| 7 | 73 | 73 | Yes | 12.35 |
| 8 | 3 | 3 | Yes | 11.61 |
| 9 | 1440 |  | No | 52.07 |
| 10 | 4 | 42 | No | 16.24 |
| 11 | 44 | 42 | No | 5.93 |
| 12 | 28 | 28 | Yes | 10.54 |
| 13 | 60 | 42 | No | 3.9 |
| 14 | 26 | 42 | No | 14.8 |
| 15 | 67 | 67 | Yes | 8.99 |
| 16 | 20 |  | No | 46.99 |
| 17 | 10 | 42 | No | 5.74 |
| 18 | 36 | 36 | Yes | 18.36 |
| 19 | 5 | 5 | Yes | 27.73 |
| 20 | 7 | 7 | Yes | 2.84 |
