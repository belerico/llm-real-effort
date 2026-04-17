# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-27 10:48:53

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
| sudoku_game | 4722 | 38912 | 43634 | 0 | 20 | 71.18 | 1423.7 |
| add_numbers | 2720 | 3796 | 6516 | 20 | 0 | 6.74 | 134.83 |
| counting_zeros | 4120 | 39463 | 43583 | 5 | 15 | 42.98 | 859.65 |
| task_decoding | 4060 | 7007 | 11067 | 20 | 0 | 7.48 | 149.51 |
| task_summation | 4400 | 13046 | 17446 | 20 | 0 | 11.95 | 238.91 |
| task_transcription | 2861 | 3619 | 6480 | 20 | 0 | 3.73 | 74.6 |
| task_sequences | 2721 | 13991 | 16712 | 10 | 10 | 11.86 | 237.24 |
| string_entry | 3158 | 39023 | 42181 | 2 | 18 | 43.93 | 878.56 |
| **TOTAL** | **28762** | **158857** | **187619** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 1 6 2 1 6 3 5 4 2 1 6 5 |  | No | 70.59 |
| 2 | 3 6 1 4 5 6 2 3 1 1 5 6 2 4 |  | No | 70.34 |
| 3 | 4 6 4 6 2 4 3 2 2 4 5 1 6 2 |  | No | 86.01 |
| 4 | 1 2 6 5 1 5 4 1 2 4 4 2 1 6 |  | No | 67.5 |
| 5 | 2 6 6 5 1 1 2 4 4 6 2 5 4 1 |  | No | 94.64 |
| 6 | 3 6 4 5 3 4 5 1 6 4 1 6 5 6 |  | No | 62.68 |
| 7 | 5 1 2 3 2 6 4 5 5 5 3 1 4 2 |  | No | 63.92 |
| 8 | 1 3 4 3 5 2 6 1 2 5 5 3 4 2 |  | No | 56.26 |
| 9 | 1 1 4 6 2 3 4 5 2 4 4 6 3 5 |  | No | 65.83 |
| 10 | 1 6 6 4 6 5 4 6 3 1 3 2 6 4 |  | No | 63.87 |
| 11 | 1 6 2 4 4 3 1 6 2 6 1 1 6 5 |  | No | 52.45 |
| 12 | 2 6 4 6 2 1 2 5 4 1 3 5 2 6 |  | No | 73.92 |
| 13 | 2 5 6 3 1 2 3 5 1 1 6 4 2 1 |  | No | 62.77 |
| 14 | 5 2 1 3 5 5 4 1 6 3 2 1 5 4 |  | No | 49.05 |
| 15 | 1 5 4 1 3 6 4 2 1 4 2 6 5 6 |  | No | 70.36 |
| 16 | 3 4 4 3 6 4 5 2 4 3 3 6 4 4 |  | No | 55.29 |
| 17 | 1 2 5 4 4 5 1 1 4 3 5 2 1 3 |  | No | 81.21 |
| 18 | 4 1 1 2 4 2 3 5 4 2 4 3 6 5 |  | No | 77.86 |
| 19 | 3 4 1 5 1 2 6 3 2 1 6 2 1 2 |  | No | 79.06 |
| 20 | 1 3 1 2 6 1 2 6 4 4 3 2 5 4 | TIMEOUT | No | 120.02 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2070 | 2070 | Yes | 6.86 |
| 2 | 832 | 832 | Yes | 6.03 |
| 3 | 1912 | 1912 | Yes | 6.5 |
| 4 | 2616 | 2616 | Yes | 5.47 |
| 5 | 1576 | 1576 | Yes | 7.32 |
| 6 | 2439 | 2439 | Yes | 5.78 |
| 7 | 1819 | 1819 | Yes | 7.1 |
| 8 | 1545 | 1545 | Yes | 11.99 |
| 9 | 2276 | 2276 | Yes | 7.87 |
| 10 | 1086 | 1086 | Yes | 8.88 |
| 11 | 1872 | 1872 | Yes | 8.85 |
| 12 | 1532 | 1532 | Yes | 8.61 |
| 13 | 2240 | 2240 | Yes | 6.93 |
| 14 | 1376 | 1376 | Yes | 2.87 |
| 15 | 515 | 515 | Yes | 4.41 |
| 16 | 1293 | 1293 | Yes | 4.29 |
| 17 | 2090 | 2090 | Yes | 2.89 |
| 18 | 1472 | 1472 | Yes | 9.09 |
| 19 | 1556 | 1556 | Yes | 3.42 |
| 20 | 2233 | 2233 | Yes | 9.66 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 69 | 69 | Yes | 36.96 |
| 2 | 57 |  | No | 57.61 |
| 3 | 75 |  | No | 53.41 |
| 4 | 69 |  | No | 47.92 |
| 5 | 39 |  | No | 45.49 |
| 6 | 65 |  | No | 44.49 |
| 7 | 50 | 50 | Yes | 35.52 |
| 8 | 71 |  | No | 35.26 |
| 9 | 61 |  | No | 41.24 |
| 10 | 73 |  | No | 52.55 |
| 11 | 74 |  | No | 43.31 |
| 12 | 66 |  | No | 32.0 |
| 13 | 41 | 41 | Yes | 24.14 |
| 14 | 68 |  | No | 45.3 |
| 15 | 38 |  | No | 56.92 |
| 16 | 38 | 38 | Yes | 28.59 |
| 17 | 51 | 51 | Yes | 23.04 |
| 18 | 70 |  | No | 42.47 |
| 19 | 75 |  | No | 62.14 |
| 20 | 61 |  | No | 51.28 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XVMALTO | XVMALTO | Yes | 10.88 |
| 2 | UYGTFLB | UYGTFLB | Yes | 4.96 |
| 3 | OQKNZUS | OQKNZUS | Yes | 8.16 |
| 4 | BOKEFJN | BOKEFJN | Yes | 6.14 |
| 5 | GKZQCRS | GKZQCRS | Yes | 9.42 |
| 6 | UQDENWH | UQDENWH | Yes | 6.87 |
| 7 | YGWFQRO | YGWFQRO | Yes | 10.01 |
| 8 | GZJFAMI | GZJFAMI | Yes | 5.98 |
| 9 | EUWRBIJ | EUWRBIJ | Yes | 11.63 |
| 10 | IHXDZME | IHXDZME | Yes | 3.83 |
| 11 | EDZBYRT | EDZBYRT | Yes | 8.83 |
| 12 | STUERMO | STUERMO | Yes | 13.65 |
| 13 | CFPYBOH | CFPYBOH | Yes | 3.59 |
| 14 | MSNZAHB | MSNZAHB | Yes | 5.96 |
| 15 | ZTCHDEN | ZTCHDEN | Yes | 9.82 |
| 16 | UQYEMWI | UQYEMWI | Yes | 5.99 |
| 17 | BXQPIWD | BXQPIWD | Yes | 9.17 |
| 18 | TDGFKBM | TDGFKBM | Yes | 5.55 |
| 19 | JILMHZK | JILMHZK | Yes | 5.88 |
| 20 | AXUOQNK | AXUOQNK | Yes | 3.21 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 1.8 8.2 | Yes | 13.91 |
| 2 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.11 |
| 3 | [0.3, 9.7] | 9.7 0.3 | Yes | 12.01 |
| 4 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.23 |
| 5 | [4.5, 5.5] | 4.5 5.5 | Yes | 16.96 |
| 6 | [0.8, 9.2] | 9.2 0.8 | Yes | 9.85 |
| 7 | [4.7, 5.3] | 4.7 5.3 | Yes | 9.55 |
| 8 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.65 |
| 9 | [4.0, 6.0] | 4.0 6.0 | Yes | 11.54 |
| 10 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.38 |
| 11 | [3.9, 6.1] | 6.1 3.9 | Yes | 22.99 |
| 12 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.29 |
| 13 | [4.0, 6.0] | 6.0 4.0 | Yes | 15.16 |
| 14 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.34 |
| 15 | [1.1, 8.9] | 1.1 8.9 | Yes | 9.55 |
| 16 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.84 |
| 17 | [2.2, 7.8] | 2.2 7.8 | Yes | 16.02 |
| 18 | [5.0, 5.0] | 5.0 5.0 | Yes | 16.33 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 8.69 |
| 20 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.5 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BT2BX4MLGPB9 | BT2BX4MLGPB9 | Yes | 2.77 |
| 2 | A2BY9O7YDVA3 | A2BY9O7YDVA3 | Yes | 6.36 |
| 3 | RM4IV8MC7KVB | RM4IV8MC7KVB | Yes | 2.42 |
| 4 | 975MRPZEQKH8 | 975MRPZEQKH8 | Yes | 5.22 |
| 5 | WTRATAAOMMVJ | WTRATAAOMMVJ | Yes | 2.37 |
| 6 | DBF6LRKFVK2M | DBF6LRKFVK2M | Yes | 3.69 |
| 7 | JV8EMH9JYJMV | JV8EMH9JYJMV | Yes | 2.86 |
| 8 | 1BP7VG26XFSD | 1BP7VG26XFSD | Yes | 3.21 |
| 9 | G30Y44XCTYP6 | G30Y44XCTYP6 | Yes | 4.05 |
| 10 | AFZOEH07XVSC | AFZOEH07XVSC | Yes | 4.47 |
| 11 | 4JMAHV7U9D7Y | 4JMAHV7U9D7Y | Yes | 3.76 |
| 12 | A681BURH2LQ8 | A681BURH2LQ8 | Yes | 2.7 |
| 13 | MV7N3KTBWA4X | MV7N3KTBWA4X | Yes | 2.65 |
| 14 | J4893NVRVME4 | J4893NVRVME4 | Yes | 2.45 |
| 15 | F2YT59IYRWKQ | F2YT59IYRWKQ | Yes | 5.46 |
| 16 | VZDFXEN24C30 | VZDFXEN24C30 | Yes | 4.46 |
| 17 | MONJ0NMQFI0G | MONJ0NMQFI0G | Yes | 4.03 |
| 18 | ECD6Q4EQJ70K | ECD6Q4EQJ70K | Yes | 3.14 |
| 19 | E1GWBLCSJ5UG | E1GWBLCSJ5UG | Yes | 2.87 |
| 20 | 2ENTHIFZHO80 | 2ENTHIFZHO80 | Yes | 5.63 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 4.4 |
| 2 | 4096 |  | No | 41.23 |
| 3 | 6 | 6 | Yes | 4.74 |
| 4 | 64 | 42 | No | 15.24 |
| 5 | 31 | 31 | Yes | 13.7 |
| 6 | 60 | 60 | Yes | 19.2 |
| 7 | 5 | 5 | Yes | 9.79 |
| 8 | 9 | 42 | No | 14.13 |
| 9 | 4 | 4 | Yes | 8.64 |
| 10 | 73 | 73 | Yes | 10.96 |
| 11 | 19 | 19 | Yes | 10.27 |
| 12 | 4 | 42 | No | 4.87 |
| 13 | 28 | 28 | Yes | 15.92 |
| 14 | 198 | 42 | No | 13.76 |
| 15 | 65 | 42 | No | 14.79 |
| 16 | 23 | 23 | Yes | 20.8 |
| 17 | 44 | 42 | No | 5.44 |
| 18 | 10 | 42 | No | 2.67 |
| 19 | 48 | 42 | No | 4.76 |
| 20 | 20 | 42 | No | 1.93 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <)\) \(_  |  | No | 56.59 |
| 2 | \_<<<)/\/ | /\) <(_<) | No | 24.9 |
| 3 | ( )/\   _ |  | No | 65.46 |
| 4 | < _(/_/<\ | /\) <(_<) | No | 18.35 |
| 5 | _(_()(<_( |  | No | 73.91 |
| 6 | ()<\)\)_\ |  | No | 42.85 |
| 7 | \<))\(\/  | /\) <(_<) | No | 22.23 |
| 8 | \\ \\)_   |  | No | 76.4 |
| 9 | ))\( (_/< |  | No | 29.34 |
| 10 | \_<_//)_) |  | No | 58.98 |
| 11 | )<)/ ())( |  | No | 51.53 |
| 12 |   _ \()_  | /\) <(_<) | No | 26.57 |
| 13 | /( )/( <) | /( )/( <) | Yes | 22.6 |
| 14 | </ //)( _ | /\) <(_<) | No | 22.09 |
| 15 | </<\(//() | /\) <(_<) | No | 23.43 |
| 16 | ____)__(  |  | No | 43.97 |
| 17 | /<)/)\/(\ | /<)/)\/(\ | Yes | 23.03 |
| 18 | _<\(<))(( |  | No | 56.84 |
| 19 | _<//\<(/) |  | No | 68.44 |
| 20 | \\<_)_(\) |  | No | 71.02 |
