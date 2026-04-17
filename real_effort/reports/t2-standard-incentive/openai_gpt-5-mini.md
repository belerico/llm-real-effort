# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
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
| sudoku_game | 6840 | 38912 | 45752 | 0 | 20 | 73.84 | 1476.99 |
| add_numbers | 3780 | 4234 | 8014 | 20 | 0 | 8.76 | 175.26 |
| counting_zeros | 6200 | 30668 | 36868 | 0 | 20 | 47.03 | 940.98 |
| task_decoding | 11940 | 16367 | 28307 | 18 | 2 | 21.13 | 422.9 |
| task_summation | 7140 | 11848 | 18988 | 20 | 0 | 12.20 | 244.13 |
| task_transcription | 3604 | 13163 | 16767 | 18 | 2 | 12.48 | 249.8 |
| task_sequences | 2756 | 15094 | 17850 | 15 | 5 | 22.47 | 449.32 |
| **TOTAL** | **42260** | **130286** | **172546** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 2 3 6 5 1 2 1 5 6 5 2 4 |  | No | 83.28 |
| 2 | 2 5 1 3 4 5 3 6 1 6 6 5 4 1 |  | No | 53.5 |
| 3 | 4 5 3 6 5 2 1 3 6 5 3 1 5 2 |  | No | 61.1 |
| 4 | 5 3 4 2 5 3 2 6 3 3 2 3 1 4 |  | No | 69.9 |
| 5 | 4 3 5 1 4 3 5 4 2 3 2 3 1 6 |  | No | 57.23 |
| 6 | 2 5 3 4 2 6 5 5 6 3 2 2 4 5 |  | No | 63.07 |
| 7 | 5 4 6 1 4 2 2 3 6 6 2 4 3 1 |  | No | 52.12 |
| 8 | 5 6 4 4 3 6 4 1 4 1 6 4 2 4 |  | No | 62.92 |
| 9 | 5 2 1 4 5 3 2 4 4 3 6 2 5 1 |  | No | 66.0 |
| 10 | 3 6 4 3 1 5 4 5 3 2 5 2 1 3 |  | No | 64.18 |
| 11 | 2 4 4 1 3 4 1 5 6 5 5 4 3 5 |  | No | 76.45 |
| 12 | 5 4 3 2 2 1 4 6 1 1 5 4 5 4 | TIMEOUT | No | 120.02 |
| 13 | 3 6 5 1 2 1 3 5 4 3 6 5 2 4 |  | No | 78.68 |
| 14 | 1 5 6 2 3 2 4 1 5 1 6 3 2 5 |  | No | 79.33 |
| 15 | 6 1 2 5 4 1 3 5 6 1 5 6 1 3 |  | No | 71.84 |
| 16 | 5 4 6 4 5 4 2 4 6 2 3 1 1 2 |  | No | 79.36 |
| 17 | 4 2 6 3 1 3 3 6 6 2 3 5 6 4 |  | No | 95.35 |
| 18 | 3 1 6 5 4 1 4 6 3 6 5 4 3 1 |  | No | 83.45 |
| 19 | 4 6 5 2 5 6 5 6 3 4 1 5 3 1 |  | No | 86.61 |
| 20 | 5 3 6 4 1 3 2 6 2 1 5 3 1 3 |  | No | 72.42 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2257 | 2257 | Yes | 9.6 |
| 2 | 1761 | 1761 | Yes | 8.78 |
| 3 | 2377 | 2377 | Yes | 13.45 |
| 4 | 1397 | 1397 | Yes | 7.69 |
| 5 | 1042 | 1042 | Yes | 5.87 |
| 6 | 1168 | 1168 | Yes | 8.62 |
| 7 | 1899 | 1899 | Yes | 6.98 |
| 8 | 1031 | 1031 | Yes | 7.32 |
| 9 | 1221 | 1221 | Yes | 7.82 |
| 10 | 2171 | 2171 | Yes | 5.37 |
| 11 | 1612 | 1612 | Yes | 6.46 |
| 12 | 1733 | 1733 | Yes | 6.64 |
| 13 | 1433 | 1433 | Yes | 36.13 |
| 14 | 2344 | 2344 | Yes | 10.45 |
| 15 | 2551 | 2551 | Yes | 6.62 |
| 16 | 1957 | 1957 | Yes | 4.66 |
| 17 | 1413 | 1413 | Yes | 6.19 |
| 18 | 1661 | 1661 | Yes | 7.47 |
| 19 | 1638 | 1638 | Yes | 3.99 |
| 20 | 1801 | 1801 | Yes | 5.03 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 58 | 67 | No | 24.03 |
| 2 | 70 | 67 | No | 21.13 |
| 3 | 48 | 67 | No | 19.77 |
| 4 | 63 | 67 | No | 23.66 |
| 5 | 61 |  | No | 69.49 |
| 6 | 53 |  | No | 61.84 |
| 7 | 55 |  | No | 89.15 |
| 8 | 37 | 67 | No | 23.86 |
| 9 | 69 | 67 | No | 12.51 |
| 10 | 46 | 67 | No | 36.83 |
| 11 | 71 | 67 | No | 21.37 |
| 12 | 65 |  | No | 55.36 |
| 13 | 46 | 67 | No | 54.64 |
| 14 | 54 | 67 | No | 40.06 |
| 15 | 46 | 67 | No | 44.04 |
| 16 | 49 |  | No | 103.92 |
| 17 | 52 | 67 | No | 45.84 |
| 18 | 59 |  | No | 79.21 |
| 19 | 40 |  | No | 81.06 |
| 20 | 71 | 67 | No | 32.9 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XLUTYAP | XLUTYAP | Yes | 14.43 |
| 2 | GWTDVBU | GWTDVBU | Yes | 10.56 |
| 3 | BKNJHDX | BKNJHDX | Yes | 24.84 |
| 4 | OQVMAFB | OQVMAFB | Yes | 9.6 |
| 5 | SBYWRDC | SBYWRDC | Yes | 16.79 |
| 6 | KIHETYW | KIHETYW | Yes | 13.06 |
| 7 | PYOFTMV | PYOFTMV | Yes | 14.12 |
| 8 | WOQMXHC | WOQMXHC | Yes | 15.66 |
| 9 | AGYMJLK | AGYMJLK | Yes | 18.46 |
| 10 | OWZXRIT |  | No | 66.71 |
| 11 | MRDVZHQ | MRDVZHQ | Yes | 18.42 |
| 12 | REUAGBJ | REUAGBJ | Yes | 19.71 |
| 13 | YDXFVTW | YDXFVTW | Yes | 10.46 |
| 14 | RJBUTAI | RJBUTAI | Yes | 22.57 |
| 15 | KTRPUCN | KTRPUCN | Yes | 21.93 |
| 16 | XIQLPKS | XIQLPKS | Yes | 17.86 |
| 17 | OCEDIAT |  | No | 64.96 |
| 18 | SQBUFMD | SQBUFMD | Yes | 22.6 |
| 19 | RFZSXDL | RFZSXDL | Yes | 10.38 |
| 20 | OSZXBAM | OSZXBAM | Yes | 9.57 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 9.6 0.4 | Yes | 12.97 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 11.73 |
| 3 | [2.7, 7.3] | 7.3 2.7 | Yes | 12.9 |
| 4 | [0.3, 9.7] | 9.7 0.3 | Yes | 12.76 |
| 5 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.52 |
| 6 | [4.0, 6.0] | 6.0 4.0 | Yes | 13.8 |
| 7 | [1.1, 8.9] | 8.9 1.1 | Yes | 13.19 |
| 8 | [1.7, 8.3] | 8.3 1.7 | Yes | 8.93 |
| 9 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.11 |
| 10 | [3.2, 6.8] | 6.8 3.2 | Yes | 13.68 |
| 11 | [5.0, 5.0] | 5.0 5.0 | Yes | 13.38 |
| 12 | [0.6, 9.4] | 9.4 0.6 | Yes | 14.69 |
| 13 | [0.4, 9.6] | 0.4 9.6 | Yes | 10.51 |
| 14 | [2.4, 7.6] | 7.6 2.4 | Yes | 10.4 |
| 15 | [2.3, 7.7] | 7.7 2.3 | Yes | 10.76 |
| 16 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.5 |
| 17 | [2.9, 7.1] | 7.1 2.9 | Yes | 22.0 |
| 18 | [4.4, 5.6] | 5.6 4.4 | Yes | 9.95 |
| 19 | [1.9, 8.1] | 1.9 8.1 | Yes | 14.86 |
| 20 | [3.1, 6.9] | 3.1 6.9 | Yes | 10.3 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | Y9AU0FV877A6 | Y9AU0FV877A6 | Yes | 4.76 |
| 2 | JL72XB36V3DB | JL72XB36V3DB | Yes | 12.96 |
| 3 | BZUXX83DICH5 | BZUXX83DICH5 | Yes | 8.0 |
| 4 | 8C1HE8357AMQ | 8C1HE8357AMQ | Yes | 5.91 |
| 5 | X58WRB5LEKHX | X58WRB5LEKHX | Yes | 11.49 |
| 6 | UYRVBE09U82L | UYRVBE09U82L | Yes | 9.19 |
| 7 | 4HTJC40SJ2AI |  | No | 46.32 |
| 8 | V4SEVS7W8BHJ | V4SEVS7W8BHJ | Yes | 10.88 |
| 9 | LRXUXWDSCAOK | LRXUXWDSCAOK | Yes | 4.74 |
| 10 | VYPNG4UM27F3 | VYPNG4UM27F3 | Yes | 5.32 |
| 11 | F6G28QJAU6EW | F6G28QJAU6EW | Yes | 15.9 |
| 12 | QNYNVIK68MMJ | QNYNVIK68MMJ | Yes | 5.65 |
| 13 | DRQJGTF730VJ | DRQJGTF730VJ | Yes | 8.02 |
| 14 | X100CF8SXEP0 | X100CF8SXEP0 | Yes | 10.68 |
| 15 | F7X83NKS83H1 | F7X83NKS83H1 | Yes | 9.26 |
| 16 | 80M85L399APV | 80M85L399APV | Yes | 16.57 |
| 17 | PMTEFF1NH17T | PMTEFF1NH17T | Yes | 8.32 |
| 18 | HCQQWW38SOG9 | HCQQWW38SOG9 | Yes | 21.43 |
| 19 | TS94Z2KC7QG9 | TS94Z2KC7QG9 | Yes | 7.53 |
| 20 | 0LVHUWLJ4XK2 | OLVHUWLJ4XK2 | No | 26.75 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 |  | No | 54.62 |
| 2 | 7680 | 7680 | Yes | 15.31 |
| 3 | 4 | 4 | Yes | 10.33 |
| 4 | 23 | 23 | Yes | 8.17 |
| 5 | 9 | 9 | Yes | 21.35 |
| 6 | 1 | 1 | Yes | 14.62 |
| 7 | 9 | TIMEOUT | No | 120.03 |
| 8 | 793 | 793 | Yes | 5.91 |
| 9 | 6 | 6 | Yes | 11.42 |
| 10 | 4 | 4 | Yes | 28.69 |
| 11 | 48 | 42 | No | 7.22 |
| 12 | 19 | 19 | Yes | 14.17 |
| 13 | 198 | 198 | Yes | 25.87 |
| 14 | 4096 |  | No | 51.79 |
| 15 | 63 | 42 | No | 6.85 |
| 16 | 65 | 65 | Yes | 5.53 |
| 17 | 16 | 16 | Yes | 9.32 |
| 18 | 7 | 7 | Yes | 6.76 |
| 19 | 5 | 5 | Yes | 18.7 |
| 20 | 73 | 73 | Yes | 12.66 |
