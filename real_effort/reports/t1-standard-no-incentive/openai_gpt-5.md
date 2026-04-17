# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 7760 | 40960 | 48720 | 0 | 20 | 70.47 | 1409.52 |
| add_numbers | 6780 | 4606 | 11386 | 20 | 0 | 7.30 | 146.17 |
| counting_zeros | 6840 | 40960 | 47800 | 0 | 20 | 76.97 | 1539.69 |
| task_decoding | 9595 | 16430 | 26025 | 19 | 1 | 20.24 | 405.0 |
| task_summation | 7100 | 22027 | 29127 | 20 | 0 | 18.51 | 370.35 |
| task_transcription | 6860 | 13011 | 19871 | 18 | 2 | 14.69 | 293.97 |
| task_sequences | 2721 | 10083 | 12804 | 18 | 2 | 12.67 | 253.41 |
| **TOTAL** | **47656** | **148077** | **195733** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 5 2 4 5 3 4 6 1 2 3 2 6 |  | No | 70.8 |
| 2 | 3 2 6 4 4 6 5 1 5 1 6 3 1 6 |  | No | 61.95 |
| 3 | 1 4 1 6 4 5 2 5 4 6 1 2 6 2 |  | No | 54.86 |
| 4 | 5 3 3 1 2 3 5 2 2 5 1 3 6 2 |  | No | 59.39 |
| 5 | 3 5 6 4 6 5 3 4 5 3 2 2 6 3 |  | No | 77.29 |
| 6 | 3 4 5 2 6 6 4 2 4 6 2 5 4 6 |  | No | 76.36 |
| 7 | 2 3 6 4 5 2 4 3 1 5 6 3 3 1 |  | No | 74.55 |
| 8 | 3 1 5 4 1 4 3 6 5 6 2 4 5 4 |  | No | 74.23 |
| 9 | 6 2 3 5 2 1 5 6 3 4 2 4 2 1 |  | No | 67.03 |
| 10 | 6 2 3 1 5 4 6 1 1 5 2 3 5 4 |  | No | 78.29 |
| 11 | 4 1 4 6 3 2 3 1 5 2 5 3 2 5 |  | No | 71.33 |
| 12 | 5 3 6 3 5 1 1 6 1 4 6 5 4 2 |  | No | 76.5 |
| 13 | 4 2 2 4 1 5 3 1 4 6 6 1 2 5 |  | No | 76.08 |
| 14 | 4 3 3 6 5 1 6 5 6 4 3 2 5 1 |  | No | 65.07 |
| 15 | 6 5 1 4 3 2 4 3 1 4 4 1 6 1 |  | No | 68.26 |
| 16 | 4 1 2 6 3 5 4 1 6 3 2 5 4 1 |  | No | 71.48 |
| 17 | 5 6 4 6 5 2 4 6 1 3 6 2 6 3 |  | No | 68.89 |
| 18 | 1 4 1 4 1 2 5 3 2 5 6 3 4 1 |  | No | 71.71 |
| 19 | 4 4 1 2 3 6 3 1 6 2 5 4 2 1 |  | No | 72.73 |
| 20 | 5 3 3 5 3 6 6 3 1 5 3 2 2 3 |  | No | 72.5 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1934 | 1934 | Yes | 6.63 |
| 2 | 1080 | 1080 | Yes | 6.6 |
| 3 | 1124 | 1124 | Yes | 6.39 |
| 4 | 1968 | 1968 | Yes | 7.52 |
| 5 | 955 | 955 | Yes | 5.4 |
| 6 | 2026 | 2026 | Yes | 6.92 |
| 7 | 1971 | 1971 | Yes | 5.78 |
| 8 | 1850 | 1850 | Yes | 6.27 |
| 9 | 1385 | 1385 | Yes | 5.62 |
| 10 | 2173 | 2173 | Yes | 7.74 |
| 11 | 2004 | 2004 | Yes | 5.45 |
| 12 | 1051 | 1051 | Yes | 5.91 |
| 13 | 2137 | 2137 | Yes | 6.52 |
| 14 | 1202 | 1202 | Yes | 8.52 |
| 15 | 1331 | 1331 | Yes | 12.25 |
| 16 | 1333 | 1333 | Yes | 8.29 |
| 17 | 1307 | 1307 | Yes | 6.94 |
| 18 | 1656 | 1656 | Yes | 8.84 |
| 19 | 1837 | 1837 | Yes | 7.42 |
| 20 | 1824 | 1824 | Yes | 11.06 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 50 |  | No | 78.45 |
| 2 | 45 |  | No | 71.76 |
| 3 | 59 |  | No | 83.65 |
| 4 | 58 |  | No | 81.25 |
| 5 | 70 |  | No | 97.66 |
| 6 | 43 |  | No | 79.9 |
| 7 | 50 |  | No | 118.65 |
| 8 | 57 |  | No | 73.47 |
| 9 | 41 |  | No | 73.18 |
| 10 | 73 |  | No | 78.66 |
| 11 | 73 |  | No | 74.81 |
| 12 | 40 |  | No | 66.89 |
| 13 | 64 |  | No | 66.53 |
| 14 | 44 |  | No | 60.66 |
| 15 | 49 |  | No | 71.7 |
| 16 | 48 |  | No | 72.95 |
| 17 | 72 |  | No | 69.58 |
| 18 | 63 |  | No | 69.98 |
| 19 | 54 |  | No | 74.9 |
| 20 | 70 |  | No | 74.73 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MZSWIDC | MZSWIDC | Yes | 10.74 |
| 2 | UOEYKVZ | UOEYKVZ | Yes | 12.49 |
| 3 | LRNYEKH | LRNYEKH | Yes | 20.58 |
| 4 | ANQTLDE | ANQTLDE | Yes | 12.44 |
| 5 | XWYTCHA | TIMEOUT | No | 120.02 |
| 6 | PAILOYW | PAILOYW | Yes | 23.45 |
| 7 | HOSABMX | HOSABMX | Yes | 9.56 |
| 8 | SFYCBZW | SFYCBZW | Yes | 21.75 |
| 9 | XGDAENF | XGDAENF | Yes | 12.93 |
| 10 | GURNTIZ | GURNTIZ | Yes | 15.97 |
| 11 | SWNEBQP | SWNEBQP | Yes | 11.06 |
| 12 | PBRMDFQ | PBRMDFQ | Yes | 7.55 |
| 13 | ZNASPCM | ZNASPCM | Yes | 20.32 |
| 14 | OZNVGHA | OZNVGHA | Yes | 18.32 |
| 15 | ZNIREQU | ZNIREQU | Yes | 14.81 |
| 16 | DCXEOSZ | DCXEOSZ | Yes | 18.54 |
| 17 | NBXUPCY | NBXUPCY | Yes | 12.53 |
| 18 | NZEHJXT | NZEHJXT | Yes | 5.23 |
| 19 | ABXFPHQ | ABXFPHQ | Yes | 14.3 |
| 20 | NERJKIL | NERJKIL | Yes | 22.2 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 4.3 5.7 | Yes | 14.05 |
| 2 | [1.8, 8.2] | 1.8 8.2 | Yes | 13.0 |
| 3 | [5.0, 5.0] | 5.0 5.0 | Yes | 14.71 |
| 4 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.89 |
| 5 | [3.9, 6.1] | 3.9 6.1 | Yes | 15.55 |
| 6 | [1.0, 9.0] | 9.0 1.0 | Yes | 26.4 |
| 7 | [4.3, 5.7] | 5.7 4.3 | Yes | 16.99 |
| 8 | [4.3, 5.7] | 4.3 5.7 | Yes | 18.4 |
| 9 | [4.4, 5.6] | 4.4 5.6 | Yes | 18.9 |
| 10 | [0.8, 9.2] | 0.8 9.2 | Yes | 22.48 |
| 11 | [4.0, 6.0] | 4.0 6.0 | Yes | 23.91 |
| 12 | [3.0, 7.0] | 7.0 3.0 | Yes | 16.86 |
| 13 | [1.9, 8.1] | 1.9 8.1 | Yes | 19.53 |
| 14 | [0.2, 9.8] | 0.2 9.8 | Yes | 22.38 |
| 15 | [1.2, 8.8] | 1.2 8.8 | Yes | 22.59 |
| 16 | [4.6, 5.4] | 5.4 4.6 | Yes | 16.52 |
| 17 | [0.8, 9.2] | 0.8 9.2 | Yes | 21.35 |
| 18 | [1.3, 8.7] | 8.7 1.3 | Yes | 24.11 |
| 19 | [2.4, 7.6] | 2.4 7.6 | Yes | 14.18 |
| 20 | [3.8, 6.2] | 6.2 3.8 | Yes | 16.36 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JZR9GTJ0IPSA | JZR9GTJ0IPSA | Yes | 9.02 |
| 2 | GD5MXR6LZ7NS | GD5MXR6LZ7NS | Yes | 6.73 |
| 3 | ACD5R1QEXPSC | ACD5R1QEXPSC | Yes | 7.39 |
| 4 | HFZGG236FMXZ | HFZGG236FMXZ | Yes | 6.08 |
| 5 | 36K2Z2M0JHDU | 36K2Z2M0JHDU | Yes | 14.09 |
| 6 | PGZRU2739DSZ | PGZRU2739DSZ | Yes | 8.22 |
| 7 | XID7G8J29CGD | XID7G8J29CGD | Yes | 16.59 |
| 8 | 8ETCQ89L8KRO | 8ETCQ89L8KRO | Yes | 29.98 |
| 9 | KC05DYGYHFFJ | KC05DYGYHFFJ | Yes | 8.77 |
| 10 | 5B8PBPPIJXU8 | 5B8PBPPJXU8 | No | 23.32 |
| 11 | 8IUPCRTA8IRK | 8IUPCRTA8IRK | Yes | 11.4 |
| 12 | 8KHVZIW0Z7KK | 8KHVZIW0Z7KK | Yes | 17.08 |
| 13 | 7V3N47OPMXMA | 7V3N47OPMXMA | Yes | 9.8 |
| 14 | 4G5HTI8M3F7K | 4G5HTI8M3F7K | Yes | 15.14 |
| 15 | 2O13BAQYS5K3 | 2013BAQYS5K3 | No | 10.98 |
| 16 | 9CQPXC8IVRCC | 9CQPXC8IVRCC | Yes | 12.04 |
| 17 | 4GLDZCH85HTG | 4GLDZCH85HTG | Yes | 15.26 |
| 18 | KQEQXSTECTWF | KQEQXSTECTWF | Yes | 34.78 |
| 19 | CLA5YU5KE2BQ | CLA5YU5KE2BQ | Yes | 11.62 |
| 20 | KI18DPCMSQNR | KI18DPCMSQNR | Yes | 25.53 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 16.64 |
| 2 | 7680 | 7680 | Yes | 11.04 |
| 3 | 16 | 16 | Yes | 7.08 |
| 4 | 6 | 6 | Yes | 5.6 |
| 5 | 4 | 4 | Yes | 7.91 |
| 6 | 73 | 73 | Yes | 9.39 |
| 7 | 23 | 23 | Yes | 8.32 |
| 8 | 48 | 48 | Yes | 6.49 |
| 9 | 4096 |  | No | 52.66 |
| 10 | 5 |  | No | 53.14 |
| 11 | 60 | 60 | Yes | 10.82 |
| 12 | 9 | 9 | Yes | 7.63 |
| 13 | 44 | 44 | Yes | 9.21 |
| 14 | 793 | 793 | Yes | 5.15 |
| 15 | 36 | 36 | Yes | 5.33 |
| 16 | 198 | 198 | Yes | 9.54 |
| 17 | 1440 | 1440 | Yes | 6.57 |
| 18 | 63 | 63 | Yes | 4.82 |
| 19 | 28 | 28 | Yes | 5.47 |
| 20 | 19 | 19 | Yes | 10.61 |
