# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-27 10:15:39

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
| sudoku_game | 5154 | 28622 | 33776 | 11 | 9 | 39.52 | 790.44 |
| add_numbers | 2900 | 662 | 3562 | 20 | 0 | 3.59 | 71.87 |
| counting_zeros | 4300 | 16593 | 20893 | 20 | 0 | 17.23 | 344.69 |
| task_decoding | 4240 | 2038 | 6278 | 20 | 0 | 5.48 | 109.63 |
| task_summation | 4580 | 3288 | 7868 | 20 | 0 | 6.53 | 130.56 |
| task_transcription | 3033 | 639 | 3672 | 20 | 0 | 2.04 | 40.88 |
| task_sequences | 2900 | 5904 | 8804 | 18 | 2 | 10.63 | 212.51 |
| string_entry | 3337 | 13902 | 17239 | 4 | 16 | 14.44 | 288.9 |
| **TOTAL** | **30444** | **71648** | **102092** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 6 3 4 1 3 2 6 1 4 6 2 5 3 | 1 6 3 4 1 3 2 6 1 4 6 2 5 3 | Yes | 17.46 |
| 2 | 5 4 6 3 2 3 6 4 3 5 1 3 2 6 | 5 4 6 3 2 3 6 4 3 5 1 3 2 6 | Yes | 29.53 |
| 3 | 3 2 5 6 6 2 5 4 2 6 1 4 2 5 | 3 2 5 6 6 2 5 4 2 6 1 4 2 5 | Yes | 11.71 |
| 4 | 2 3 1 4 6 2 1 6 3 5 3 2 2 3 |  | No | 62.31 |
| 5 | 4 3 1 2 1 5 3 2 6 4 1 4 3 3 |  | No | 81.56 |
| 6 | 3 6 6 1 4 1 2 5 4 4 4 6 3 2 | 3 6 6 1 4 1 2 5 4 4 4 6 3 2 | Yes | 16.26 |
| 7 | 1 5 6 2 1 4 6 3 5 3 6 6 3 4 | 1 5 6 2 1 4 6 3 5 3 6 6 3 4 | Yes | 20.87 |
| 8 | 6 1 4 5 3 5 2 6 1 3 4 6 2 4 | 6 1 4 5 3 5 2 6 1 3 4 6 2 4 | Yes | 23.26 |
| 9 | 5 2 4 5 6 2 4 2 6 5 4 1 6 5 |  | No | 82.69 |
| 10 | 4 5 2 2 5 3 5 2 1 2 3 4 4 3 | 4 5 2 2 5 3 5 2 1 2 3 4 4 3 | Yes | 19.02 |
| 11 | 5 2 5 3 2 4 2 6 1 4 6 5 4 3 | 5 2 5 3 2 4 2 6 1 4 6 5 4 3 | Yes | 18.93 |
| 12 | 6 4 3 5 2 6 3 3 6 1 1 5 3 2 |  | No | 39.71 |
| 13 | 6 1 4 1 3 2 3 5 6 1 4 1 5 3 |  | No | 64.67 |
| 14 | 2 4 1 6 2 1 2 3 3 4 6 3 4 2 | 2 4 1 6 2 1 2 3 3 4 6 3 4 2 | Yes | 10.76 |
| 15 | 1 5 3 3 2 6 3 6 2 6 1 2 5 3 |  | No | 56.12 |
| 16 | 6 2 3 6 4 1 4 3 4 6 6 1 4 3 | 6 2 3 6 4 1 4 3 4 6 6 1 4 3 | Yes | 19.17 |
| 17 | 5 2 1 4 5 1 1 3 4 6 3 4 4 1 |  | No | 65.07 |
| 18 | 3 6 1 6 2 6 2 6 1 5 5 6 4 2 |  | No | 69.1 |
| 19 | 6 2 3 4 5 4 1 6 3 6 5 5 3 6 | 6 2 3 4 5 4 1 6 3 6 5 5 3 6 | Yes | 15.54 |
| 20 | 1 6 2 5 5 2 3 3 6 5 3 2 6 2 |  | No | 66.66 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2164 | 2164 | Yes | 4.76 |
| 2 | 1648 | 1648 | Yes | 3.36 |
| 3 | 1494 | 1494 | Yes | 3.3 |
| 4 | 942 | 942 | Yes | 2.65 |
| 5 | 1631 | 1631 | Yes | 3.03 |
| 6 | 1684 | 1684 | Yes | 4.29 |
| 7 | 2333 | 2333 | Yes | 3.62 |
| 8 | 2259 | 2259 | Yes | 3.43 |
| 9 | 1644 | 1644 | Yes | 3.95 |
| 10 | 2020 | 2020 | Yes | 3.22 |
| 11 | 1660 | 1660 | Yes | 2.79 |
| 12 | 827 | 827 | Yes | 5.15 |
| 13 | 1362 | 1362 | Yes | 4.08 |
| 14 | 1555 | 1555 | Yes | 3.32 |
| 15 | 1837 | 1837 | Yes | 5.21 |
| 16 | 1337 | 1337 | Yes | 3.32 |
| 17 | 2051 | 2051 | Yes | 2.83 |
| 18 | 1238 | 1238 | Yes | 3.53 |
| 19 | 1218 | 1218 | Yes | 2.41 |
| 20 | 1106 | 1106 | Yes | 3.63 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 | 49 | Yes | 16.38 |
| 2 | 60 | 60 | Yes | 13.96 |
| 3 | 43 | 43 | Yes | 18.75 |
| 4 | 38 | 38 | Yes | 18.43 |
| 5 | 68 | 68 | Yes | 12.0 |
| 6 | 40 | 40 | Yes | 15.8 |
| 7 | 54 | 54 | Yes | 22.42 |
| 8 | 62 | 62 | Yes | 13.96 |
| 9 | 56 | 56 | Yes | 14.61 |
| 10 | 54 | 54 | Yes | 23.32 |
| 11 | 60 | 60 | Yes | 14.04 |
| 12 | 70 | 70 | Yes | 14.46 |
| 13 | 62 | 62 | Yes | 18.59 |
| 14 | 63 | 63 | Yes | 21.87 |
| 15 | 71 | 71 | Yes | 17.24 |
| 16 | 38 | 38 | Yes | 16.4 |
| 17 | 52 | 52 | Yes | 14.71 |
| 18 | 59 | 59 | Yes | 13.12 |
| 19 | 73 | 73 | Yes | 26.37 |
| 20 | 54 | 54 | Yes | 18.24 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | UWKTFQZ | UWKTFQZ | Yes | 5.74 |
| 2 | MYXNRDP | MYXNRDP | Yes | 5.55 |
| 3 | OPFQKLU | OPFQKLU | Yes | 5.73 |
| 4 | JYRCWXH | JYRCWXH | Yes | 5.16 |
| 5 | RKWUOEA | RKWUOEA | Yes | 6.28 |
| 6 | BDJXCUM | BDJXCUM | Yes | 4.63 |
| 7 | GBARLYZ | GBARLYZ | Yes | 3.28 |
| 8 | BOTZMUK | BOTZMUK | Yes | 6.24 |
| 9 | WJDATLG | WJDATLG | Yes | 5.52 |
| 10 | ALVBEZI | ALVBEZI | Yes | 5.41 |
| 11 | SIWLXVQ | SIWLXVQ | Yes | 4.97 |
| 12 | UEAWKTQ | UEAWKTQ | Yes | 7.35 |
| 13 | MIAWECN | MIAWECN | Yes | 4.4 |
| 14 | AGLMZOD | AGLMZOD | Yes | 3.61 |
| 15 | ATXQHNB | ATXQHNB | Yes | 5.56 |
| 16 | JKXRWUP | JKXRWUP | Yes | 5.85 |
| 17 | XCEGBLH | XCEGBLH | Yes | 7.33 |
| 18 | ONCFBEA | ONCFBEA | Yes | 5.2 |
| 19 | VWXOPLC | VWXOPLC | Yes | 6.05 |
| 20 | DLFSTVK | DLFSTVK | Yes | 5.75 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.04 |
| 2 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.16 |
| 3 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.84 |
| 4 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.54 |
| 5 | [2.5, 7.5] | 7.5 2.5 | Yes | 5.19 |
| 6 | [2.5, 7.5] | 7.5 2.5 | Yes | 8.16 |
| 7 | [0.4, 9.6] | 0.4 9.6 | Yes | 8.25 |
| 8 | [4.8, 5.2] | 5.2 4.8 | Yes | 7.24 |
| 9 | [0.1, 9.9] | 9.9 0.1 | Yes | 5.38 |
| 10 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.91 |
| 11 | [1.4, 8.6] | 8.6 1.4 | Yes | 4.84 |
| 12 | [3.9, 6.1] | 3.9 6.1 | Yes | 4.73 |
| 13 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.08 |
| 14 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.61 |
| 15 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.79 |
| 16 | [3.5, 6.5] | 6.5 3.5 | Yes | 6.24 |
| 17 | [4.8, 5.2] | 5.2 4.8 | Yes | 7.32 |
| 18 | [3.8, 6.2] | 3.8 6.2 | Yes | 7.6 |
| 19 | [2.1, 7.9] | 2.1 7.9 | Yes | 6.48 |
| 20 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.14 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | C4JT8P1NQHYW | C4JT8P1NQHYW | Yes | 1.02 |
| 2 | 9Y0GSZ7CDHAW | 9Y0GSZ7CDHAW | Yes | 4.22 |
| 3 | OO8VB3O4NSHL | OO8VB3O4NSHL | Yes | 5.08 |
| 4 | 3NUZZ541JNWH | 3NUZZ541JNWH | Yes | 1.2 |
| 5 | WTRF177Y6903 | WTRF177Y6903 | Yes | 1.04 |
| 6 | 15EVDGD198GO | 15EVDGD198GO | Yes | 1.63 |
| 7 | 8KFXTUH95N93 | 8KFXTUH95N93 | Yes | 1.98 |
| 8 | OHVLFHIGUHY5 | OHVLFHIGUHY5 | Yes | 1.91 |
| 9 | R5BVT6SWXNST | R5BVT6SWXNST | Yes | 1.3 |
| 10 | AGE63Y7ELXSB | AGE63Y7ELXSB | Yes | 2.45 |
| 11 | JAGN0BWDUJ9W | JAGN0BWDUJ9W | Yes | 2.69 |
| 12 | RJPFSEJ972UY | RJPFSEJ972UY | Yes | 1.74 |
| 13 | JSDP8MOHJNFZ | JSDP8MOHJNFZ | Yes | 0.86 |
| 14 | LC7EG4SBLL19 | LC7EG4SBLL19 | Yes | 1.39 |
| 15 | U2OTQJJFNEMZ | U2OTQJJFNEMZ | Yes | 1.22 |
| 16 | LCT6WB7ZE1RV | LCT6WB7ZE1RV | Yes | 0.81 |
| 17 | Z517X70LDREO | Z517X70LDREO | Yes | 3.79 |
| 18 | 7FTSHA6AVHEA | 7FTSHA6AVHEA | Yes | 1.41 |
| 19 | CC43FQGQDT39 | CC43FQGQDT39 | Yes | 1.82 |
| 20 | 6OQ5VYPC256H | 6OQ5VYPC256H | Yes | 3.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 44 | Yes | 6.12 |
| 2 | 39 | 39 | Yes | 5.93 |
| 3 | 26 | 26 | Yes | 14.57 |
| 4 | 28 | 28 | Yes | 5.31 |
| 5 | 243 | 243 | Yes | 1.6 |
| 6 | 20 |  | No | 80.52 |
| 7 | 1440 | 1440 | Yes | 4.35 |
| 8 | 60 | 60 | Yes | 5.7 |
| 9 | 5 | 2 | No | 26.21 |
| 10 | 23 | 23 | Yes | 12.66 |
| 11 | 3 | 3 | Yes | 5.82 |
| 12 | 31 | 31 | Yes | 2.61 |
| 13 | 4 | 4 | Yes | 3.38 |
| 14 | 64 | 64 | Yes | 4.57 |
| 15 | 198 | 198 | Yes | 6.06 |
| 16 | 73 | 73 | Yes | 5.82 |
| 17 | 4 | 4 | Yes | 2.83 |
| 18 | 16 | 16 | Yes | 4.06 |
| 19 | 10 | 10 | Yes | 10.19 |
| 20 | 3 | 3 | Yes | 4.2 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \)_(/_(/( | /\) <(_<) | No | 19.72 |
| 2 | (\ <(\/)( | /\) <(_<) | No | 13.73 |
| 3 | (/_/_\ __ | (/_/_\ __ | Yes | 4.91 |
| 4 |  _)\)( )( | _)\)( )( | No | 8.91 |
| 5 | /_(_/\__< | /\) <(_<) | No | 10.19 |
| 6 | <\()))(_< | /\) <(_<) | No | 7.52 |
| 7 |  ( //_</_ | ( //_</_ | No | 26.43 |
| 8 |  / )_<_/\ | / )_<_/\ | No | 11.14 |
| 9 | _)_<_ _\\ | _)_<_ _\\ | Yes | 10.61 |
| 10 | <// \(/(< | <// \(/(< | Yes | 19.01 |
| 11 | ((<(/_)(< | /\) <(_<) | No | 27.75 |
| 12 |  )< )(()_ | )< )(()_ | No | 6.82 |
| 13 |  _<\< (/\ | _<\< (/\ | No | 8.23 |
| 14 | )<\<)\\\< | /\) <(_<) | No | 21.2 |
| 15 | <  </\(<_ | /\) <(_<) | No | 32.59 |
| 16 |  (\(<_ )/ | (\(<_ )/ | No | 8.58 |
| 17 |  (_(_(\_/ | (_(_(\_/ | No | 14.75 |
| 18 | /<(\/(<)/ | /\) <(_<) | No | 13.33 |
| 19 | ))  (_<<\ | ))  (_<<\ | Yes | 5.94 |
| 20 | /(<_)//(\ | /\) <(_<) | No | 17.54 |
