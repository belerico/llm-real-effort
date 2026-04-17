# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-27 10:43:23

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
| sudoku_game | 5149 | 40960 | 46109 | 0 | 20 | 55.63 | 1112.6 |
| add_numbers | 2755 | 3618 | 6373 | 19 | 1 | 11.87 | 237.32 |
| counting_zeros | 4300 | 40103 | 44403 | 5 | 15 | 47.45 | 948.94 |
| task_decoding | 4240 | 7320 | 11560 | 20 | 0 | 9.42 | 188.41 |
| task_summation | 4580 | 13928 | 18508 | 20 | 0 | 12.96 | 259.3 |
| task_transcription | 3038 | 3748 | 6786 | 20 | 0 | 5.35 | 106.96 |
| task_sequences | 2900 | 8489 | 11389 | 19 | 1 | 10.58 | 211.65 |
| string_entry | 3337 | 27378 | 30715 | 10 | 10 | 29.39 | 587.86 |
| **TOTAL** | **30299** | **145544** | **175843** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 4 6 3 2 4 5 6 1 3 6 5 4 |  | No | 54.68 |
| 2 | 5 4 1 4 5 2 6 3 5 2 3 4 5 4 |  | No | 54.18 |
| 3 | 2 5 5 6 1 4 2 1 5 6 6 4 5 2 |  | No | 65.22 |
| 4 | 1 5 2 2 5 6 1 6 5 1 6 1 2 6 |  | No | 55.54 |
| 5 | 4 2 3 5 4 6 3 4 5 6 2 4 6 1 |  | No | 60.48 |
| 6 | 3 6 3 1 2 6 4 6 2 1 6 4 6 2 |  | No | 51.7 |
| 7 | 3 4 6 2 3 2 3 5 1 4 5 1 2 4 |  | No | 56.79 |
| 8 | 6 4 2 5 1 6 4 2 1 5 2 1 5 2 |  | No | 61.97 |
| 9 | 2 5 3 2 1 6 3 5 1 6 4 3 2 1 |  | No | 47.61 |
| 10 | 5 3 2 1 2 1 4 4 3 1 2 1 3 5 |  | No | 53.79 |
| 11 | 2 4 6 1 4 2 3 4 2 3 6 4 5 6 |  | No | 65.37 |
| 12 | 4 6 1 3 5 2 5 1 2 2 4 3 1 5 |  | No | 45.91 |
| 13 | 4 1 5 3 3 2 4 1 3 4 3 6 6 2 |  | No | 33.06 |
| 14 | 5 3 2 5 6 2 3 4 4 3 6 3 1 4 |  | No | 56.07 |
| 15 | 4 6 2 6 1 6 5 1 3 5 4 2 1 6 |  | No | 53.25 |
| 16 | 2 5 1 4 6 5 2 4 6 5 6 1 2 4 |  | No | 58.08 |
| 17 | 3 2 5 6 2 4 5 3 4 3 1 2 2 4 |  | No | 66.74 |
| 18 | 3 5 2 3 1 6 2 3 6 5 3 6 6 4 |  | No | 45.04 |
| 19 | 2 5 4 1 6 3 3 2 2 5 4 6 1 6 |  | No | 57.22 |
| 20 | 4 2 1 4 4 6 3 1 2 5 4 1 1 5 |  | No | 69.86 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1046 | 1046 | Yes | 3.8 |
| 2 | 2221 | 2221 | Yes | 6.19 |
| 3 | 1225 | 1225 | Yes | 6.86 |
| 4 | 1318 | TIMEOUT | No | 120.03 |
| 5 | 1973 | 1973 | Yes | 5.57 |
| 6 | 1166 | 1166 | Yes | 6.64 |
| 7 | 1820 | 1820 | Yes | 6.7 |
| 8 | 1976 | 1976 | Yes | 6.59 |
| 9 | 1659 | 1659 | Yes | 7.09 |
| 10 | 1100 | 1100 | Yes | 5.76 |
| 11 | 952 | 952 | Yes | 6.12 |
| 12 | 1900 | 1900 | Yes | 7.42 |
| 13 | 1585 | 1585 | Yes | 9.4 |
| 14 | 1368 | 1368 | Yes | 4.2 |
| 15 | 1460 | 1460 | Yes | 5.31 |
| 16 | 1627 | 1627 | Yes | 5.26 |
| 17 | 1399 | 1399 | Yes | 5.63 |
| 18 | 2067 | 2067 | Yes | 6.51 |
| 19 | 1652 | 1652 | Yes | 4.74 |
| 20 | 990 | 990 | Yes | 7.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 |  | No | 79.83 |
| 2 | 56 | 56 | Yes | 22.83 |
| 3 | 48 |  | No | 60.1 |
| 4 | 45 |  | No | 57.3 |
| 5 | 65 |  | No | 52.44 |
| 6 | 44 | 44 | Yes | 24.24 |
| 7 | 45 |  | No | 44.84 |
| 8 | 37 | 37 | Yes | 24.22 |
| 9 | 71 | 71 | Yes | 24.34 |
| 10 | 50 |  | No | 49.59 |
| 11 | 53 |  | No | 45.59 |
| 12 | 38 |  | No | 52.42 |
| 13 | 66 |  | No | 48.01 |
| 14 | 35 |  | No | 38.12 |
| 15 | 47 |  | No | 53.82 |
| 16 | 63 |  | No | 57.22 |
| 17 | 41 |  | No | 54.13 |
| 18 | 61 |  | No | 67.85 |
| 19 | 75 | 75 | Yes | 27.81 |
| 20 | 58 |  | No | 64.23 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HDXVCNM | HDXVCNM | Yes | 11.22 |
| 2 | PAZVJIY | PAZVJIY | Yes | 7.22 |
| 3 | IZDWFHT | IZDWFHT | Yes | 7.76 |
| 4 | WNTDOAC | WNTDOAC | Yes | 9.7 |
| 5 | EIPSBDA | EIPSBDA | Yes | 9.08 |
| 6 | ARETPBY | ARETPBY | Yes | 4.4 |
| 7 | HQERANM | HQERANM | Yes | 11.41 |
| 8 | RGOLUZF | RGOLUZF | Yes | 9.86 |
| 9 | WTRGZQY | WTRGZQY | Yes | 7.48 |
| 10 | BKLVDIQ | BKLVDIQ | Yes | 9.5 |
| 11 | KJFYZDX | KJFYZDX | Yes | 8.8 |
| 12 | RMPQNSJ | RMPQNSJ | Yes | 10.16 |
| 13 | FZRMXTK | FZRMXTK | Yes | 13.47 |
| 14 | ZEXNGLY | ZEXNGLY | Yes | 7.58 |
| 15 | CGETANZ | CGETANZ | Yes | 9.84 |
| 16 | VRQUBWX | VRQUBWX | Yes | 9.78 |
| 17 | UMNPXQK | UMNPXQK | Yes | 8.2 |
| 18 | GWIBELJ | GWIBELJ | Yes | 11.86 |
| 19 | SCZBUFH | SCZBUFH | Yes | 11.48 |
| 20 | ARUPMQL | ARUPMQL | Yes | 9.62 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.6, 5.4] | 5.4 4.6 | Yes | 14.63 |
| 2 | [2.3, 7.7] | 7.7 2.3 | Yes | 12.17 |
| 3 | [4.2, 5.8] | 5.8 4.2 | Yes | 15.07 |
| 4 | [3.3, 6.7] | 3.3 6.7 | Yes | 8.29 |
| 5 | [3.0, 7.0] | 3.0 7.0 | Yes | 19.86 |
| 6 | [0.4, 9.6] | 0.4 9.6 | Yes | 15.47 |
| 7 | [3.3, 6.7] | 6.7 3.3 | Yes | 12.56 |
| 8 | [2.4, 7.6] | 2.4 7.6 | Yes | 8.51 |
| 9 | [3.1, 6.9] | 3.1 6.9 | Yes | 10.5 |
| 10 | [0.4, 9.6] | 0.4 9.6 | Yes | 14.0 |
| 11 | [4.1, 5.9] | 5.9 4.1 | Yes | 15.13 |
| 12 | [4.1, 5.9] | 4.1 5.9 | Yes | 13.96 |
| 13 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.37 |
| 14 | [2.4, 7.6] | 7.6 2.4 | Yes | 16.99 |
| 15 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.61 |
| 16 | [4.8, 5.2] | 4.8 5.2 | Yes | 11.28 |
| 17 | [4.5, 5.5] | 4.5 5.5 | Yes | 15.4 |
| 18 | [2.6, 7.4] | 7.4 2.6 | Yes | 10.57 |
| 19 | [1.3, 8.7] | 8.7 1.3 | Yes | 14.7 |
| 20 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.23 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YUR2KM257DPZ | YUR2KM257DPZ | Yes | 10.57 |
| 2 | 9SF3AHU2K818 | 9SF3AHU2K818 | Yes | 6.4 |
| 3 | DA5RY4KHQNS1 | DA5RY4KHQNS1 | Yes | 5.33 |
| 4 | 8RQF3SGS8SXL | 8RQF3SGS8SXL | Yes | 4.53 |
| 5 | OR5D5BQFZ5LN | OR5D5BQFZ5LN | Yes | 6.36 |
| 6 | BGIA41DWWDRR | BGIA41DWWDRR | Yes | 5.56 |
| 7 | GTBYR1ICPM6A | GTBYR1ICPM6A | Yes | 3.27 |
| 8 | YQY06IQEUR2R | YQY06IQEUR2R | Yes | 5.5 |
| 9 | 2JURMHZZK50Y | 2JURMHZZK50Y | Yes | 3.11 |
| 10 | X83SWDCQYN5Y | X83SWDCQYN5Y | Yes | 3.22 |
| 11 | LQNKCCQV1QTE | LQNKCCQV1QTE | Yes | 6.91 |
| 12 | L3W091K38TAL | L3W091K38TAL | Yes | 3.93 |
| 13 | XSEMB7XNYQYL | XSEMB7XNYQYL | Yes | 5.21 |
| 14 | 6ZI17YZRNC6H | 6ZI17YZRNC6H | Yes | 4.39 |
| 15 | 9JC585RBH9CK | 9JC585RBH9CK | Yes | 2.44 |
| 16 | ESHOL6AZY9M6 | ESHOL6AZY9M6 | Yes | 7.54 |
| 17 | 2WVYSASSNMMG | 2WVYSASSNMMG | Yes | 5.84 |
| 18 | T1PDTQ53EIQM | T1PDTQ53EIQM | Yes | 5.83 |
| 19 | KTNOKMGX4N39 | KTNOKMGX4N39 | Yes | 5.84 |
| 20 | 2RH1SLB2ECLP | 2RH1SLB2ECLP | Yes | 5.16 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 4.98 |
| 2 | 3 | 3 | Yes | 6.86 |
| 3 | 60 | 60 | Yes | 5.45 |
| 4 | 31 | 31 | Yes | 10.54 |
| 5 | 73 | 73 | Yes | 9.94 |
| 6 | 63 | 63 | Yes | 7.32 |
| 7 | 65 | 65 | Yes | 10.89 |
| 8 | 9 | 9 | Yes | 6.08 |
| 9 | 26 | 26 | Yes | 27.09 |
| 10 | 23 | 23 | Yes | 6.07 |
| 11 | 198 | 198 | Yes | 6.44 |
| 12 | 64 | 64 | Yes | 9.36 |
| 13 | 9 | 9 | Yes | 5.82 |
| 14 | 5 | 5 | Yes | 6.03 |
| 15 | 1440 | 1440 | Yes | 5.71 |
| 16 | 243 | 243 | Yes | 5.02 |
| 17 | 16 | 16 | Yes | 5.11 |
| 18 | 5 |  | No | 61.0 |
| 19 | 7680 | 7680 | Yes | 6.94 |
| 20 | 7 | 7 | Yes | 5.01 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _( \_/_ _ |  | No | 85.68 |
| 2 | / /_ (\(  | / /_ (\( | No | 25.81 |
| 3 | /\<<)((/) | /\<<)((/) | Yes | 17.55 |
| 4 | )))(<\_<  | )))(<\_< | No | 26.09 |
| 5 | \))<_ <__ | \))<_ <__ | Yes | 16.48 |
| 6 | \</)< (/( | \</)< (/( | Yes | 14.97 |
| 7 | <_/_)(()\ |  | No | 60.47 |
| 8 | __)//))// | __)//))// | Yes | 14.01 |
| 9 | ) \  ()/_ | ) \  ()/_ | Yes | 16.45 |
| 10 |  )/<_/\)/ | )/<_/\)/ | No | 18.43 |
| 11 | //(  (/(\ | //(  (/\ | No | 20.34 |
| 12 | _ \\_\<\_ |  | No | 67.53 |
| 13 | </\) \(<\ | </\) \(<\ | Yes | 13.73 |
| 14 | <\_(<(\)) | <\_(<(\)) | Yes | 23.86 |
| 15 | /<(</)<)  |  | No | 64.25 |
| 16 |  _\___( < | _\___( < | No | 22.68 |
| 17 | <)\\(_\<) | <)\\(_\<) | Yes | 21.55 |
| 18 | )\ ) </\< | )\ ) </\< | Yes | 21.42 |
| 19 | \// /_)(/ | \// /_)(/ | Yes | 13.45 |
| 20 | \< \(/()/ | \< \(/()/% | No | 23.1 |
