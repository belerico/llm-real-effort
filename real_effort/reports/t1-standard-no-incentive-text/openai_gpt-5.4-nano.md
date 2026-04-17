# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-27 10:15:44

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 4974 | 37008 | 41982 | 9 | 11 | 36.74 | 734.85 |
| add_numbers | 2720 | 741 | 3461 | 20 | 0 | 3.37 | 67.43 |
| counting_zeros | 4120 | 19956 | 24076 | 18 | 2 | 14.52 | 290.46 |
| task_decoding | 4060 | 3111 | 7171 | 20 | 0 | 5.68 | 113.6 |
| task_summation | 4400 | 6984 | 11384 | 20 | 0 | 6.41 | 128.29 |
| task_transcription | 2864 | 1969 | 4833 | 20 | 0 | 3.16 | 63.25 |
| task_sequences | 2585 | 12236 | 14821 | 17 | 3 | 14.97 | 299.39 |
| string_entry | 3150 | 27888 | 31038 | 3 | 17 | 15.60 | 311.98 |
| **TOTAL** | **28873** | **109893** | **138766** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 2 2 4 1 5 5 6 4 3 4 6 3 | 1 6 2 2 4 1 5 5 6 4 3 4 6 3 | Yes | 21.56 |
| 2 | 4 2 6 2 4 4 1 4 5 1 1 3 5 2 | 4 2 6 2 4 4 1 4 5 1 1 3 5 2 | Yes | 19.78 |
| 3 | 3 2 6 4 2 5 6 3 4 6 3 4 2 3 |  | No | 45.04 |
| 4 | 5 2 2 6 2 4 1 6 4 3 6 5 2 3 |  | No | 54.79 |
| 5 | 2 5 4 3 3 2 5 4 1 6 6 2 4 3 |  | No | 36.0 |
| 6 | 2 6 4 3 6 3 4 1 5 6 5 4 3 6 |  | No | 43.47 |
| 7 | 6 3 2 6 4 3 2 3 4 6 1 2 6 3 | 6 3 2 6 4 3 2 3 4 6 1 2 6 3 | Yes | 28.21 |
| 8 | 1 5 3 1 6 5 2 3 1 2 2 1 4 6 |  | No | 64.94 |
| 9 | 6 2 5 3 3 5 3 4 2 2 3 5 1 3 | 6 2 5 3 3 5 3 4 2 2 3 5 1 3 | Yes | 23.07 |
| 10 | 4 6 3 2 5 6 1 3 1 2 5 1 3 2 |  | No | 51.47 |
| 11 | 2 4 5 2 3 5 6 1 1 3 2 3 6 1 |  | No | 36.78 |
| 12 | 1 2 3 3 1 3 4 1 1 4 4 6 3 1 | 1 2 3 3 1 3 4 1 1 4 4 6 3 1 | Yes | 24.65 |
| 13 | 1 6 3 3 4 1 4 3 5 1 5 2 1 4 |  | No | 51.24 |
| 14 | 5 1 5 3 1 2 5 6 4 5 2 1 3 5 | 5 1 5 3 1 2 5 6 4 5 2 1 3 5 | Yes | 25.03 |
| 15 | 6 1 5 3 6 6 1 4 5 4 4 2 6 3 | 6 1 5 3 6 6 1 4 5 4 4 2 6 3 | Yes | 21.44 |
| 16 | 4 2 4 5 6 2 5 6 4 2 5 4 1 6 | 4 2 4 5 6 2 5 6 4 2 5 4 1 6 | Yes | 23.34 |
| 17 | 6 4 1 3 5 5 2 1 5 2 3 3 6 5 |  | No | 52.6 |
| 18 | 2 1 4 3 6 2 4 1 2 4 2 5 5 1 | 2 1 4 3 6 2 4 1 2 4 2 5 5 1 | Yes | 12.91 |
| 19 | 6 4 2 3 5 2 5 1 4 1 5 6 3 2 |  | No | 49.83 |
| 20 | 4 4 6 5 6 1 4 3 1 2 6 3 2 4 |  | No | 48.66 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2525 | 2525 | Yes | 2.88 |
| 2 | 2067 | 2067 | Yes | 3.0 |
| 3 | 2411 | 2411 | Yes | 3.44 |
| 4 | 1440 | 1440 | Yes | 3.42 |
| 5 | 1506 | 1506 | Yes | 2.9 |
| 6 | 1306 | 1306 | Yes | 3.21 |
| 7 | 748 | 748 | Yes | 3.35 |
| 8 | 1508 | 1508 | Yes | 3.52 |
| 9 | 1632 | 1632 | Yes | 2.26 |
| 10 | 1889 | 1889 | Yes | 3.49 |
| 11 | 885 | 885 | Yes | 4.09 |
| 12 | 1160 | 1160 | Yes | 3.82 |
| 13 | 671 | 671 | Yes | 3.16 |
| 14 | 1813 | 1813 | Yes | 3.8 |
| 15 | 1102 | 1102 | Yes | 3.55 |
| 16 | 1950 | 1950 | Yes | 3.39 |
| 17 | 1727 | 1727 | Yes | 3.52 |
| 18 | 1886 | 1886 | Yes | 3.38 |
| 19 | 880 | 880 | Yes | 4.28 |
| 20 | 1505 | 1505 | Yes | 2.95 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 66 | 66 | Yes | 20.89 |
| 2 | 67 | 67 | Yes | 12.24 |
| 3 | 63 | 62 | No | 13.01 |
| 4 | 47 | 47 | Yes | 15.95 |
| 5 | 36 | 34 | No | 13.55 |
| 6 | 39 | 39 | Yes | 11.7 |
| 7 | 46 | 46 | Yes | 16.35 |
| 8 | 64 | 64 | Yes | 26.26 |
| 9 | 74 | 74 | Yes | 18.03 |
| 10 | 75 | 75 | Yes | 12.77 |
| 11 | 35 | 35 | Yes | 11.85 |
| 12 | 46 | 46 | Yes | 15.67 |
| 13 | 46 | 46 | Yes | 13.48 |
| 14 | 45 | 45 | Yes | 10.82 |
| 15 | 42 | 42 | Yes | 12.79 |
| 16 | 42 | 42 | Yes | 11.46 |
| 17 | 41 | 41 | Yes | 12.28 |
| 18 | 38 | 38 | Yes | 8.42 |
| 19 | 68 | 68 | Yes | 14.84 |
| 20 | 72 | 72 | Yes | 18.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YWJZQBE | YWJZQBE | Yes | 8.61 |
| 2 | GWNLSUF | GWNLSUF | Yes | 4.74 |
| 3 | VFGAEKC | VFGAEKC | Yes | 4.17 |
| 4 | SHTGPKU | SHTGPKU | Yes | 6.13 |
| 5 | TYLUDQR | TYLUDQR | Yes | 4.96 |
| 6 | LNIQRHS | LNIQRHS | Yes | 6.8 |
| 7 | CLBIYSK | CLBIYSK | Yes | 5.38 |
| 8 | TEOKJPR | TEOKJPR | Yes | 6.43 |
| 9 | ZQCYUIV | ZQCYUIV | Yes | 10.73 |
| 10 | SRMOINC | SRMOINC | Yes | 7.79 |
| 11 | QDBFTVK | QDBFTVK | Yes | 6.94 |
| 12 | PGAISFE | PGAISFE | Yes | 5.18 |
| 13 | DIFYMRW | DIFYMRW | Yes | 6.93 |
| 14 | QICHBZX | QICHBZX | Yes | 3.68 |
| 15 | HFMYUIT | HFMYUIT | Yes | 4.82 |
| 16 | AQKPFYE | AQKPFYE | Yes | 2.43 |
| 17 | ZPEOKYQ | ZPEOKYQ | Yes | 1.79 |
| 18 | FOMDJCQ | FOMDJCQ | Yes | 5.62 |
| 19 | MYEAXRT | MYEAXRT | Yes | 6.27 |
| 20 | PXIZEYQ | PXIZEYQ | Yes | 4.19 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.7, 5.3] | 4.7 5.3 | Yes | 7.02 |
| 2 | [2.5, 7.5] | 7.5 2.5 | Yes | 6.02 |
| 3 | [1.0, 9.0] | 9.0 1.0 | Yes | 6.32 |
| 4 | [4.7, 5.3] | 4.7 5.3 | Yes | 6.23 |
| 5 | [0.9, 9.1] | 9.1 0.9 | Yes | 6.46 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 7.55 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.78 |
| 8 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.29 |
| 9 | [2.7, 7.3] | 7.3 2.7 | Yes | 9.01 |
| 10 | [4.0, 6.0] | 4.0 6.0 | Yes | 6.09 |
| 11 | [3.5, 6.5] | 6.5 3.5 | Yes | 7.69 |
| 12 | [0.3, 9.7] | 9.7 0.3 | Yes | 5.5 |
| 13 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.8 |
| 14 | [1.6, 8.4] | 8.4 1.6 | Yes | 4.45 |
| 15 | [1.1, 8.9] | 1.1 8.9 | Yes | 8.97 |
| 16 | [0.5, 9.5] | 9.5 0.5 | Yes | 5.48 |
| 17 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.63 |
| 18 | [2.3, 7.7] | 2.3 7.7 | Yes | 5.99 |
| 19 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.14 |
| 20 | [2.3, 7.7] | 2.3 7.7 | Yes | 5.84 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | A4MDLLJ9F8PF | A4MDLLJ9F8PF | Yes | 0.8 |
| 2 | RZCEBS282JPQ | RZCEBS282JPQ | Yes | 3.79 |
| 3 | WP6O6FIF6UNJ | WP6O6FIF6UNJ | Yes | 3.31 |
| 4 | W7FXHFVJSZA8 | W7FXHFVJSZA8 | Yes | 3.23 |
| 5 | BGX1963CQQXI | BGX1963CQQXI | Yes | 1.35 |
| 6 | ND74V85676FV | ND74V85676FV | Yes | 1.21 |
| 7 | KU4ODZOX0V5X | KU4ODZOX0V5X | Yes | 1.89 |
| 8 | J47I7LR86RX8 | J47I7LR86RX8 | Yes | 5.83 |
| 9 | OO11PV408IP4 | OO11PV408IP4 | Yes | 1.69 |
| 10 | 8A9HOJHDZ0G4 | 8A9HOJHDZ0G4 | Yes | 2.48 |
| 11 | LGAFA1Y8S83C | LGAFA1Y8S83C | Yes | 6.0 |
| 12 | YJZEKFHCTWAP | YJZEKFHCTWAP | Yes | 1.4 |
| 13 | CBAXJ7DS3BC7 | CBAXJ7DS3BC7 | Yes | 0.87 |
| 14 | 7KJQH8U403K9 | 7KJQH8U403K9 | Yes | 7.64 |
| 15 | PO7R0IJQ7OQF | PO7R0IJQ7OQF | Yes | 6.41 |
| 16 | FMHC36C2DC3Z | FMHC36C2DC3Z | Yes | 5.63 |
| 17 | 2M18ZONM4JOJ | 2M18ZONM4JOJ | Yes | 1.73 |
| 18 | 35QJMDSOUNZ8 | 35QJMDSOUNZ8 | Yes | 1.34 |
| 19 | J983X83SUG21 | J983X83SUG21 | Yes | 1.82 |
| 20 | V1KSQ27O8HQ5 | V1KSQ27O8HQ5 | Yes | 4.82 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | TIMEOUT | No | 120.03 |
| 2 | 793 | 793 | Yes | 4.22 |
| 3 | 4096 | 16384 | No | 24.07 |
| 4 | 9 | 9 | Yes | 3.3 |
| 5 | 7 | 7 | Yes | 2.47 |
| 6 | 3 | 3 | Yes | 16.41 |
| 7 | 1440 | 1440 | Yes | 7.7 |
| 8 | 10 | 9 | No | 17.0 |
| 9 | 6 | 6 | Yes | 5.93 |
| 10 | 16 | 16 | Yes | 3.28 |
| 11 | 7680 | 7680 | Yes | 4.6 |
| 12 | 19 | 19 | Yes | 10.6 |
| 13 | 243 | 243 | Yes | 4.82 |
| 14 | 9 | 9 | Yes | 16.37 |
| 15 | 65 | 65 | Yes | 5.39 |
| 16 | 198 | 198 | Yes | 9.7 |
| 17 | 23 | 23 | Yes | 13.12 |
| 18 | 44 | 44 | Yes | 8.24 |
| 19 | 1 | 1 | Yes | 11.86 |
| 20 | 64 | 64 | Yes | 10.27 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /\ /\_/\_ | /\) <(_<)/ /\_/\_ | No | 11.68 |
| 2 | /<\(  <)( | /\) <(_<)/<\(  <)( | No | 7.83 |
| 3 | \ )/)\</_ | /\) <(_<) )/)\</_ | No | 16.28 |
| 4 | (\\((</\< | /\) <(_<) (\\((</\< | No | 12.68 |
| 5 | \_(<)\()/ | \_(<)\()/ | Yes | 18.68 |
| 6 | \<__ (<_) | /\) <(_<)\<__ (<_) | No | 14.68 |
| 7 | _))/\ ((\ | _))/\ ((\ | Yes | 9.87 |
| 8 | \_)_(/(_< | /\) <(_<)\_)_(/(_< | No | 8.51 |
| 9 | \\ /(\)(/ | \\ /(\)(/ | Yes | 7.77 |
| 10 | ) _)/()/  |  | No | 17.06 |
| 11 | (/)_\)_/_ | /\) <(_<)(/)_\)_/_ | No | 10.91 |
| 12 | /_)_ \_<\ | /\) <(_< | No | 4.03 |
| 13 | )/() /\ ) |  | No | 44.6 |
| 14 |  _\<(< (_ | _\<(< (_ | No | 12.57 |
| 15 |  \\/ \\<_ | /\) <(_<) \/\ \<_ | No | 13.16 |
| 16 |  </<_< )( | /\) <(_<) </<_< )(` | No | 20.19 |
| 17 | ) _/_)\_( | /\) <(_<)) _/_)\_( | No | 15.31 |
| 18 | //</ ((__ | /\) <(_<//</ ((__ | No | 5.43 |
| 19 | < __)</__ |  | No | 54.07 |
| 20 | /_))_/ \\ | /\) <(_< | No | 6.65 |
