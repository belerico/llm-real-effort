# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-27 10:25:00

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
| sudoku_game | 4888 | 38912 | 43800 | 0 | 20 | 44.15 | 883.06 |
| add_numbers | 2755 | 2448 | 5203 | 19 | 1 | 8.85 | 177.08 |
| counting_zeros | 4300 | 40046 | 44346 | 3 | 17 | 32.85 | 657.06 |
| task_decoding | 4240 | 5409 | 9649 | 20 | 0 | 5.58 | 111.63 |
| task_summation | 4580 | 11434 | 16014 | 20 | 0 | 9.23 | 184.63 |
| task_transcription | 3031 | 2089 | 5120 | 20 | 0 | 2.59 | 51.92 |
| task_sequences | 2900 | 8800 | 11700 | 18 | 2 | 9.57 | 191.43 |
| string_entry | 3332 | 20501 | 23833 | 15 | 5 | 14.62 | 292.43 |
| **TOTAL** | **30026** | **129639** | **159665** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 3 5 6 2 5 4 2 1 2 4 2 6 |  | No | 37.73 |
| 2 | 2 2 3 4 2 5 4 3 2 3 6 3 2 1 |  | No | 37.98 |
| 3 | 6 1 5 4 6 1 4 5 6 2 3 1 4 2 |  | No | 41.06 |
| 4 | 2 1 2 6 1 3 5 3 3 1 2 6 4 5 |  | No | 54.78 |
| 5 | 1 5 4 6 6 1 2 5 2 2 3 6 1 2 |  | No | 47.07 |
| 6 | 5 5 2 4 6 3 5 4 2 3 4 5 2 6 |  | No | 40.2 |
| 7 | 3 6 1 2 2 4 3 1 1 4 2 5 3 2 |  | No | 21.81 |
| 8 | 2 1 1 5 1 4 2 1 2 4 6 2 5 6 |  | No | 38.5 |
| 9 | 4 2 6 2 6 3 4 2 4 3 5 1 2 1 |  | No | 45.78 |
| 10 | 4 2 5 5 6 1 2 2 4 4 1 6 4 3 |  | No | 16.34 |
| 11 | 1 2 3 5 6 1 3 1 4 6 5 3 4 1 |  | No | 35.78 |
| 12 | 4 2 5 2 1 6 3 4 3 2 6 5 3 2 | TIMEOUT | No | 120.02 |
| 13 | 6 1 2 1 5 4 4 6 1 3 3 5 4 2 |  | No | 43.58 |
| 14 | 2 1 4 2 5 3 6 5 4 4 2 3 5 3 |  | No | 45.78 |
| 15 | 5 3 1 5 3 1 4 6 5 2 4 1 4 6 |  | No | 28.17 |
| 16 | 6 2 2 5 6 2 4 3 1 1 4 5 2 3 |  | No | 40.79 |
| 17 | 1 4 5 1 2 1 2 5 2 6 1 4 6 1 |  | No | 52.99 |
| 18 | 6 1 5 3 1 5 5 1 4 3 3 4 5 4 |  | No | 43.63 |
| 19 | 6 4 5 4 2 3 2 1 4 6 4 5 1 4 |  | No | 47.85 |
| 20 | 1 2 6 3 5 1 2 3 2 4 3 1 5 4 |  | No | 43.19 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1629 | 1629 | Yes | 3.69 |
| 2 | 1808 | 1808 | Yes | 6.25 |
| 3 | 711 | TIMEOUT | No | 120.04 |
| 4 | 2137 | 2137 | Yes | 4.49 |
| 5 | 827 | 827 | Yes | 1.85 |
| 6 | 2109 | 2109 | Yes | 1.97 |
| 7 | 2115 | 2115 | Yes | 4.09 |
| 8 | 2068 | 2068 | Yes | 5.03 |
| 9 | 2265 | 2265 | Yes | 3.02 |
| 10 | 1343 | 1343 | Yes | 2.19 |
| 11 | 1349 | 1349 | Yes | 2.31 |
| 12 | 1315 | 1315 | Yes | 3.83 |
| 13 | 1359 | 1359 | Yes | 1.93 |
| 14 | 1505 | 1505 | Yes | 1.91 |
| 15 | 1525 | 1525 | Yes | 2.03 |
| 16 | 2003 | 2003 | Yes | 2.97 |
| 17 | 1809 | 1809 | Yes | 2.09 |
| 18 | 1275 | 1275 | Yes | 2.87 |
| 19 | 2131 | 2131 | Yes | 2.46 |
| 20 | 2272 | 2272 | Yes | 2.06 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 45 |  | No | 55.05 |
| 2 | 58 |  | No | 43.59 |
| 3 | 54 |  | No | 42.16 |
| 4 | 51 |  | No | 33.73 |
| 5 | 73 |  | No | 50.94 |
| 6 | 72 |  | No | 34.5 |
| 7 | 38 |  | No | 21.61 |
| 8 | 59 |  | No | 35.76 |
| 9 | 64 |  | No | 19.44 |
| 10 | 40 |  | No | 19.73 |
| 11 | 48 |  | No | 28.11 |
| 12 | 65 | 65 | Yes | 15.97 |
| 13 | 57 |  | No | 35.46 |
| 14 | 40 |  | No | 43.46 |
| 15 | 68 | 68 | Yes | 13.53 |
| 16 | 48 |  | No | 40.46 |
| 17 | 38 | 38 | Yes | 13.7 |
| 18 | 60 |  | No | 36.84 |
| 19 | 54 |  | No | 33.47 |
| 20 | 63 |  | No | 39.5 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CDHPNMS | CDHPNMS | Yes | 5.9 |
| 2 | CUJGTAD | CUJGTAD | Yes | 2.87 |
| 3 | MEWRGLU | MEWRGLU | Yes | 13.49 |
| 4 | GDUVPLK | GDUVPLK | Yes | 3.71 |
| 5 | NCYXDWA | NCYXDWA | Yes | 6.46 |
| 6 | DVFBUCG | DVFBUCG | Yes | 5.3 |
| 7 | MJLAIWD | MJLAIWD | Yes | 4.03 |
| 8 | QJBRWLX | QJBRWLX | Yes | 8.06 |
| 9 | NASGOZU | NASGOZU | Yes | 8.45 |
| 10 | TUEXSPZ | TUEXSPZ | Yes | 4.59 |
| 11 | CPFOYKN | CPFOYKN | Yes | 6.62 |
| 12 | OGACSPE | OGACSPE | Yes | 4.02 |
| 13 | HNFVRIL | HNFVRIL | Yes | 13.98 |
| 14 | SYVKZPQ | SYVKZPQ | Yes | 2.41 |
| 15 | GPUOCBZ | GPUOCBZ | Yes | 4.11 |
| 16 | KVYLRIA | KVYLRIA | Yes | 5.91 |
| 17 | POAXIVB | POAXIVB | Yes | 2.34 |
| 18 | JQMPAFV | JQMPAFV | Yes | 4.62 |
| 19 | IJQLXHB | IJQLXHB | Yes | 2.53 |
| 20 | KFGJWCX | KFGJWCX | Yes | 2.24 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.6, 5.4] | 5.4 4.6 | Yes | 9.07 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 5.57 |
| 3 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.99 |
| 4 | [3.8, 6.2] | 6.2 3.8 | Yes | 7.98 |
| 5 | [2.4, 7.6] | 7.6 2.4 | Yes | 16.05 |
| 6 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.75 |
| 7 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.94 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 8.55 |
| 9 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.88 |
| 10 | [2.9, 7.1] | 2.9 7.1 | Yes | 10.23 |
| 11 | [4.0, 6.0] | 4.0 6.0 | Yes | 13.75 |
| 12 | [2.3, 7.7] | 2.3 7.7 | Yes | 13.6 |
| 13 | [3.7, 6.3] | 3.7 6.3 | Yes | 8.05 |
| 14 | [1.8, 8.2] | 1.8 8.2 | Yes | 9.0 |
| 15 | [3.9, 6.1] | 3.9 6.1 | Yes | 7.94 |
| 16 | [1.4, 8.6] | 1.4 8.6 | Yes | 7.74 |
| 17 | [1.4, 8.6] | 8.6 1.4 | Yes | 12.59 |
| 18 | [3.5, 6.5] | 3.5 6.5 | Yes | 10.32 |
| 19 | [0.2, 9.8] | 0.2 9.8 | Yes | 6.17 |
| 20 | [1.6, 8.4] | 1.6 8.4 | Yes | 7.45 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QPF63K0YTRM7 | QPF63K0YTRM7 | Yes | 2.39 |
| 2 | N6SGDT3RNHT6 | N6SGDT3RNHT6 | Yes | 2.52 |
| 3 | 7423OH04L39Z | 7423OH04L39Z | Yes | 2.68 |
| 4 | 2WFEM68KK8XL | 2WFEM68KK8XL | Yes | 3.43 |
| 5 | IMX61I2OXVY9 | IMX61I2OXVY9 | Yes | 2.72 |
| 6 | BPMRIXB9IRMV | BPMRIXB9IRMV | Yes | 3.27 |
| 7 | JEL35J0UXZRO | JEL35J0UXZRO | Yes | 2.92 |
| 8 | QT7UX5VO51NA | QT7UX5VO51NA | Yes | 2.67 |
| 9 | UOJMYWUSJWCI | UOJMYWUSJWCI | Yes | 2.23 |
| 10 | PS94X7V0D16O | PS94X7V0D16O | Yes | 2.45 |
| 11 | 9GDP07AIJQUY | 9GDP07AIJQUY | Yes | 1.96 |
| 12 | FEIVTN876HPT | FEIVTN876HPT | Yes | 4.45 |
| 13 | 6CDEA6P56TMP | 6CDEA6P56TMP | Yes | 2.33 |
| 14 | 843ZVEUI7562 | 843ZVEUI7562 | Yes | 3.54 |
| 15 | 4ZCW81VUBKB9 | 4ZCW81VUBKB9 | Yes | 1.8 |
| 16 | I9ODFN7YQ9MG | I9ODFN7YQ9MG | Yes | 2.61 |
| 17 | P4AV7NJIRW76 | P4AV7NJIRW76 | Yes | 2.11 |
| 18 | J2X9WD53DRVD | J2X9WD53DRVD | Yes | 1.82 |
| 19 | YZQMFCEJVPOA | YZQMFCEJVPOA | Yes | 1.6 |
| 20 | II182JO9RRKI | II182JO9RRKI | Yes | 2.38 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 6.02 |
| 2 | 60 | 60 | Yes | 2.95 |
| 3 | 9 | 9 | Yes | 4.91 |
| 4 | 5 | 5 | Yes | 7.02 |
| 5 | 73 | 73 | Yes | 5.53 |
| 6 | 3 | 3 | Yes | 11.66 |
| 7 | 4 | 4 | Yes | 2.67 |
| 8 | 9 | 9 | Yes | 7.56 |
| 9 | 48 | 48 | Yes | 4.81 |
| 10 | 39 | 39 | Yes | 9.52 |
| 11 | 44 | 44 | Yes | 7.42 |
| 12 | 16 | 16 | Yes | 6.42 |
| 13 | 19 | 19 | Yes | 5.21 |
| 14 | 5 |  | No | 40.53 |
| 15 | 63 | 63 | Yes | 6.53 |
| 16 | 65 | 65 | Yes | 4.18 |
| 17 | 243 | 243 | Yes | 4.55 |
| 18 | 1 | 1 | Yes | 5.22 |
| 19 | 20 |  | No | 43.22 |
| 20 | 3 | 3 | Yes | 5.5 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (\_)/<_(_ | (\_)/<_(_ | Yes | 18.48 |
| 2 | ///))</<_ | ///))</<_ | Yes | 16.09 |
| 3 |  /\/_/ (  | /\/_/ ( | No | 13.04 |
| 4 | ))\) <<\/ | ))\) <<\/ | Yes | 7.29 |
| 5 | )_(()//)< | )_(()//)< | Yes | 19.8 |
| 6 |   _  )_ _ |  | No | 50.59 |
| 7 | \_<//(<\< | \_<//(<\< | Yes | 9.68 |
| 8 | / __\//(( | / __\//(( | Yes | 6.86 |
| 9 | _) (<)\/_ | _) (<)\/_ | Yes | 5.29 |
| 10 | )(    (() | )(    (() | Yes | 12.73 |
| 11 | )\\/(__\/ | )\\/(__\/ | Yes | 11.67 |
| 12 |  \)\\\//( |  | No | 30.11 |
| 13 | <(\ ))_(< | <(\ ))_(< | Yes | 7.76 |
| 14 | //_)\(/(( | //_)\(/(( | Yes | 7.04 |
| 15 | _(__<_)\< | _(__<_)\< | Yes | 4.48 |
| 16 | \\\()/_(/ | \\\()/_(/ | Yes | 5.56 |
| 17 | (__/) /\/ | (__/) /\/ | Yes | 14.46 |
| 18 | /_< _ (\/ | /_< _ (\/ | Yes | 4.73 |
| 19 | \_\)___)) | /\) <(_<) | No | 18.53 |
| 20 |  (_)__)<< |  | No | 28.22 |
