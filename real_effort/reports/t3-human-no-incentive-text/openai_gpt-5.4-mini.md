# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-27 10:06:16

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
| sudoku_game | 5285 | 33639 | 38924 | 8 | 12 | 19.47 | 389.34 |
| add_numbers | 3060 | 982 | 4042 | 20 | 0 | 2.87 | 57.33 |
| counting_zeros | 4460 | 16678 | 21138 | 16 | 4 | 7.57 | 151.37 |
| task_decoding | 4400 | 2863 | 7263 | 20 | 0 | 4.08 | 81.63 |
| task_summation | 4792 | 6315 | 11107 | 20 | 0 | 5.38 | 107.61 |
| task_transcription | 3203 | 2246 | 5449 | 20 | 0 | 3.10 | 61.95 |
| task_sequences | 3061 | 7137 | 10198 | 18 | 2 | 7.01 | 140.25 |
| string_entry | 3512 | 29670 | 33182 | 7 | 13 | 21.27 | 425.38 |
| **TOTAL** | **31773** | **99530** | **131303** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 5 6 4 5 3 5 1 1 3 5 6 2 |  | No | 24.84 |
| 2 | 6 4 1 2 2 1 4 5 3 4 6 5 6 4 |  | No | 26.32 |
| 3 | 3 5 1 5 1 5 3 2 2 1 4 6 4 5 | 3 5 1 5 1 5 3 2 2 1 4 6 4 5 | Yes | 9.9 |
| 4 | 1 3 5 6 1 4 5 2 3 1 6 1 6 2 |  | No | 19.59 |
| 5 | 3 6 5 4 1 6 1 5 3 4 6 5 2 1 |  | No | 38.91 |
| 6 | 4 3 1 2 5 4 1 2 6 1 2 6 3 5 | 4 3 1 2 5 4 1 2 6 1 2 6 3 5 | Yes | 13.21 |
| 7 | 1 3 6 3 5 1 5 2 6 6 2 4 2 4 |  | No | 31.19 |
| 8 | 6 5 1 6 3 4 6 4 6 6 3 4 4 2 | 6 5 1 6 3 4 6 4 6 6 3 4 4 2 | Yes | 8.46 |
| 9 | 5 3 6 1 4 2 5 3 2 3 6 3 4 1 |  | No | 19.63 |
| 10 | 2 5 1 6 5 2 5 2 1 6 5 6 5 1 |  | No | 22.89 |
| 11 | 5 2 2 3 5 6 1 2 4 2 5 6 5 2 | 5 2 2 3 5 6 1 2 4 2 5 6 5 2 | Yes | 12.38 |
| 12 | 2 4 4 4 2 1 3 2 6 3 5 3 2 1 | 2 4 4 4 2 1 3 2 6 3 5 3 2 1 | Yes | 12.31 |
| 13 | 1 5 4 4 2 1 2 1 5 2 6 2 3 1 | 1 5 4 4 2 1 2 1 5 2 6 2 3 1 | Yes | 12.3 |
| 14 | 4 2 6 1 4 3 6 5 4 2 6 4 3 2 |  | No | 26.55 |
| 15 | 2 5 5 6 4 1 2 3 1 5 2 2 6 4 |  | No | 25.33 |
| 16 | 6 1 6 2 3 5 6 2 3 6 1 4 3 1 | 6 1 6 2 3 5 6 2 3 6 1 4 3 1 | Yes | 10.69 |
| 17 | 1 4 2 3 5 3 1 2 3 5 4 1 3 3 | 1 4 2 3 5 3 1 2 3 5 4 1 3 3 | Yes | 10.22 |
| 18 | 5 1 4 6 6 2 5 1 2 6 4 1 4 2 |  | No | 24.01 |
| 19 | 6 3 1 6 1 3 4 5 3 1 4 5 3 2 |  | No | 25.29 |
| 20 | 3 1 5 6 2 6 2 2 4 3 1 3 6 2 |  | No | 15.29 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1596 | 1596 | Yes | 2.33 |
| 2 | 1108 | 1108 | Yes | 2.58 |
| 3 | 1418 | 1418 | Yes | 2.47 |
| 4 | 1278 | 1278 | Yes | 3.39 |
| 5 | 1610 | 1610 | Yes | 3.27 |
| 6 | 1952 | 1952 | Yes | 2.64 |
| 7 | 896 | 896 | Yes | 2.2 |
| 8 | 2006 | 2006 | Yes | 3.41 |
| 9 | 1683 | 1683 | Yes | 2.65 |
| 10 | 594 | 594 | Yes | 3.87 |
| 11 | 2031 | 2031 | Yes | 3.39 |
| 12 | 1530 | 1530 | Yes | 3.4 |
| 13 | 2440 | 2440 | Yes | 2.7 |
| 14 | 2043 | 2043 | Yes | 2.71 |
| 15 | 1395 | 1395 | Yes | 0.98 |
| 16 | 1279 | 1279 | Yes | 3.51 |
| 17 | 1597 | 1597 | Yes | 3.18 |
| 18 | 1001 | 1001 | Yes | 3.06 |
| 19 | 1251 | 1251 | Yes | 2.25 |
| 20 | 2517 | 2517 | Yes | 3.36 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 74 | Yes | 7.58 |
| 2 | 45 | 45 | Yes | 7.92 |
| 3 | 53 | 53 | Yes | 5.96 |
| 4 | 74 | 74 | Yes | 10.66 |
| 5 | 57 | 56 | No | 8.56 |
| 6 | 63 | 63 | Yes | 5.47 |
| 7 | 53 | 53 | Yes | 5.98 |
| 8 | 37 | 38 | No | 10.07 |
| 9 | 54 | 54 | Yes | 11.21 |
| 10 | 39 | 35 | No | 3.45 |
| 11 | 71 | 71 | Yes | 7.45 |
| 12 | 65 | 65 | Yes | 7.81 |
| 13 | 65 | 65 | Yes | 10.36 |
| 14 | 71 | 71 | Yes | 8.22 |
| 15 | 47 | 48 | No | 10.4 |
| 16 | 45 | 45 | Yes | 5.6 |
| 17 | 65 | 65 | Yes | 4.41 |
| 18 | 43 | 43 | Yes | 8.97 |
| 19 | 75 | 75 | Yes | 6.55 |
| 20 | 42 | 42 | Yes | 4.75 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LNERCPI | LNERCPI | Yes | 4.34 |
| 2 | QUNXZFW | QUNXZFW | Yes | 4.51 |
| 3 | PVWRLQY | PVWRLQY | Yes | 1.46 |
| 4 | XHLJPQM | XHLJPQM | Yes | 5.93 |
| 5 | DFALVTU | DFALVTU | Yes | 3.27 |
| 6 | DRLXYSM | DRLXYSM | Yes | 4.56 |
| 7 | KQALZNO | KQALZNO | Yes | 4.06 |
| 8 | NPBQYJU | NPBQYJU | Yes | 4.11 |
| 9 | KIYFLSR | KIYFLSR | Yes | 4.16 |
| 10 | DUWQZRC | DUWQZRC | Yes | 3.51 |
| 11 | PZDECMX | PZDECMX | Yes | 3.8 |
| 12 | VRIHZKF | VRIHZKF | Yes | 4.1 |
| 13 | VPTBQGL | VPTBQGL | Yes | 3.69 |
| 14 | YXJZEFN | YXJZEFN | Yes | 5.6 |
| 15 | UZRFJCE | UZRFJCE | Yes | 2.09 |
| 16 | ADOSGRX | ADOSGRX | Yes | 4.09 |
| 17 | XGJHSTD | XGJHSTD | Yes | 5.92 |
| 18 | SLWAMOD | SLWAMOD | Yes | 4.39 |
| 19 | DRHCOAB | DRHCOAB | Yes | 3.81 |
| 20 | PZHTIDM | PZHTIDM | Yes | 4.21 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.5, 7.5] | 7.5 2.5 | Yes | 5.56 |
| 2 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.81 |
| 3 | [2.9, 7.1] | 7.1 2.9 | Yes | 5.18 |
| 4 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.33 |
| 5 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.41 |
| 6 | [3.6, 6.4] | 6.4 3.6 | Yes | 4.72 |
| 7 | [2.1, 7.9] | 7.9 2.1 | Yes | 5.22 |
| 8 | [2.0, 8.0] | 8.0 2.0 | Yes | 4.33 |
| 9 | [1.1, 8.9] | 8.9 1.1 | Yes | 5.47 |
| 10 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.73 |
| 11 | [3.1, 6.9] | 6.9 3.1 | Yes | 4.34 |
| 12 | [0.6, 9.4] | 9.4 0.6 | Yes | 4.58 |
| 13 | [3.9, 6.1] | 6.1 3.9 | Yes | 5.62 |
| 14 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.57 |
| 15 | [3.0, 7.0] | 7.0 3.0 | Yes | 5.69 |
| 16 | [4.3, 5.7] | 4.3 5.7 | Yes | 7.24 |
| 17 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.34 |
| 18 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.29 |
| 19 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.46 |
| 20 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.7 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 0HWQASCCGDXP | 0HWQASCCGDXP | Yes | 3.91 |
| 2 | 9XC5P2N8WVZI | 9XC5P2N8WVZI | Yes | 6.18 |
| 3 | CTHRW9KGDR15 | CTHRW9KGDR15 | Yes | 3.66 |
| 4 | K0U8MZ7BCBI2 | K0U8MZ7BCBI2 | Yes | 3.87 |
| 5 | PH0L7AW6RGZE | PH0L7AW6RGZE | Yes | 3.33 |
| 6 | R1DXVAQIDIEV | R1DXVAQIDIEV | Yes | 3.71 |
| 7 | FHZ0J6R36QGW | FHZ0J6R36QGW | Yes | 3.67 |
| 8 | QQ7LCCTBRRZA | QQ7LCCTBRRZA | Yes | 2.06 |
| 9 | VBEJHKL0T2QV | VBEJHKL0T2QV | Yes | 3.63 |
| 10 | Q27413YCN5YP | Q27413YCN5YP | Yes | 1.26 |
| 11 | 7BU7NPMMN8TL | 7BU7NPMMN8TL | Yes | 1.57 |
| 12 | ON45NGZ1Z4FH | ON45NGZ1Z4FH | Yes | 1.28 |
| 13 | J8JK27JRYFTB | J8JK27JRYFTB | Yes | 3.6 |
| 14 | 4MNQ6EHUONXA | 4MNQ6EHUONXA | Yes | 5.01 |
| 15 | Q0R6LV6Y449I | Q0R6LV6Y449I | Yes | 4.38 |
| 16 | A2Y12SM9QBJ9 | A2Y12SM9QBJ9 | Yes | 1.32 |
| 17 | OCPBFMMMAS4B | OCPBFMMMAS4B | Yes | 3.31 |
| 18 | GLETFJ6SWWOR | GLETFJ6SWWOR | Yes | 1.16 |
| 19 | S0G8IJ98VZMJ | S0G8IJ98VZMJ | Yes | 3.68 |
| 20 | 280F6EWD6XRK | 280F6EWD6XRK | Yes | 1.35 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 2.68 |
| 2 | 7680 | 7680 | Yes | 5.63 |
| 3 | 60 | 60 | Yes | 3.67 |
| 4 | 28 | 28 | Yes | 3.79 |
| 5 | 31 | 31 | Yes | 3.11 |
| 6 | 23 | 23 | Yes | 3.48 |
| 7 | 1 | 1 | Yes | 4.38 |
| 8 | 26 |  | No | 29.01 |
| 9 | 64 | 64 | Yes | 4.29 |
| 10 | 3 | 3 | Yes | 17.76 |
| 11 | 60 | 60 | Yes | 4.39 |
| 12 | 6 | 6 | Yes | 4.85 |
| 13 | 67 | 67 | Yes | 2.92 |
| 14 | 243 | 243 | Yes | 2.57 |
| 15 | 16 | 16 | Yes | 3.74 |
| 16 | 10 | 9 | No | 9.6 |
| 17 | 48 | 48 | Yes | 3.55 |
| 18 | 5 | 5 | Yes | 3.58 |
| 19 | 198 | 198 | Yes | 3.43 |
| 20 | 4096 | 4096 | Yes | 23.83 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )\\ \)((\ |  | No | 21.44 |
| 2 |  ) ( \_\< |  | No | 20.37 |
| 3 | //())\//) | //())\//) | Yes | 13.01 |
| 4 | <<\ )_</( | <<\ )_</( | Yes | 16.07 |
| 5 | /((\_))_( | /((\_))_( | Yes | 29.21 |
| 6 | )\ < <)<  |  | No | 33.45 |
| 7 |  (_ \)\<( | /\) <(_<) (_ \)\<( | No | 13.55 |
| 8 |  _/()\ << |  | No | 38.28 |
| 9 |  (_((/\_) |  | No | 32.37 |
| 10 | (/  < /<\ | (/  < /<\ | Yes | 14.72 |
| 11 | </ <(_\)\ |  | No | 26.71 |
| 12 |  \)/ (<(_ |  | No | 28.8 |
| 13 |  )(\)/<<\ | )(\)/<<\ | No | 14.31 |
| 14 | )(/( ( )) | )(/( ( )) | Yes | 5.79 |
| 15 | )\____)<  | )\____)< | No | 9.99 |
| 16 | //<)\_<)< | //<)\_<)< | Yes | 8.84 |
| 17 | \ ()<</_  |  | No | 33.03 |
| 18 | (\\) /\_  |  | No | 28.73 |
| 19 | \ /__  </ | \ /__  </ | Yes | 10.08 |
| 20 | <<(__  _) |  | No | 26.63 |
