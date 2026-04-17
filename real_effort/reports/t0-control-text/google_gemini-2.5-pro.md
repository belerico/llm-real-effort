# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-26 15:55:09

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

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
| sudoku_game | 4679 | 35802 | 40481 | 0 | 20 | 20.00 | 400.09 |
| add_numbers | 2540 | 20409 | 22949 | 3 | 17 | 10.74 | 214.81 |
| counting_zeros | 5600 | 32682 | 38282 | 8 | 12 | 15.68 | 313.55 |
| task_decoding | 3818 | 14078 | 17896 | 19 | 1 | 8.63 | 172.6 |
| task_summation | 3836 | 23435 | 27271 | 20 | 0 | 16.06 | 321.24 |
| task_transcription | 2501 | 6759 | 9260 | 20 | 0 | 9.14 | 182.85 |
| task_sequences | 2498 | 17481 | 19979 | 19 | 1 | 16.82 | 336.44 |
| string_entry | 2820 | 11198 | 14018 | 14 | 6 | 9.17 | 183.33 |
| **TOTAL** | **28292** | **161844** | **190136** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 5 3 2 5 1 5 2 1 6 5 3 1 | 1 5 3 1 2 5 1 5 5 1 2 1 6 5 3 1 | No | 16.71 |
| 2 | 5 4 6 1 2 4 2 3 2 3 3 4 2 2 | 5 4 3 2 1 6 2 3 4 2 3 5 2 3 4 2 4 3 | No | 15.2 |
| 3 | 5 4 6 1 2 1 3 2 4 5 4 1 5 3 | Let's re-evaluate the state. I've determined that (5,2) must be 3, making (6,2) a 1. I am now updating the grid with these new values.    I | No | 22.5 |
| 4 | 5 4 6 6 2 5 2 1 4 6 4 4 5 3 |  | No | 30.78 |
| 5 | 4 6 3 5 1 2 4 5 6 5 4 1 4 5 | 5 6 4 4 1 4 2 5 1 4 5 | No | 14.98 |
| 6 | 1 5 4 3 3 6 4 5 2 5 3 6 5 4 |  | No | 28.67 |
| 7 | 1 4 6 3 5 4 2 1 5 5 6 4 3 5 |  | No | 28.95 |
| 8 | 1 3 3 5 3 5 4 6 6 3 4 2 3 5 | 1 3 3 5 3 5 6 3 6 3 4 3 2 5 | No | 13.48 |
| 9 | 2 4 6 1 6 1 2 5 4 1 3 5 4 2 | 2 4 6 1 6 1 5 2 4 1 2 5 4 3 5 2 | No | 15.62 |
| 10 | 3 5 2 3 1 2 6 4 5 3 1 3 3 2 | 3 5 2 3 1 2 4 6 3 1 3 2 5 3 2 3 2 4 1 | No | 13.66 |
| 11 | 6 2 3 5 6 5 2 4 5 3 6 1 3 4 | 6 2 5 3 6 5 2 5 2 6 4 3 4 3 4 1 | No | 16.77 |
| 12 | 5 6 2 2 6 2 1 6 5 2 1 6 6 5 |  | No | 32.4 |
| 13 | 2 4 5 5 3 1 5 2 5 4 5 3 4 2 | 2 5 4 5 2 1 5 2 5 4 3 5 4 2 4 2 | No | 11.53 |
| 14 | 2 6 4 2 5 6 3 4 6 1 6 5 1 4 | 2 4 6 5 6 2 6 2 5 1 4 6 1 6 4 1 5 4 | No | 14.71 |
| 15 | 2 3 6 3 4 3 2 1 5 4 5 5 3 1 | 2 3 6 5 3 4 3 5 1 2 5 4 5 1 5 3 1 | No | 15.02 |
| 16 | 2 5 5 6 2 6 4 2 5 4 3 1 5 3 |  | No | 29.44 |
| 17 | 1 2 4 5 1 2 5 4 6 5 5 2 3 1 | 1 2 4 5 1 5 5 4 6 5 2 5 1 3 | No | 16.8 |
| 18 | 6 2 6 5 2 5 4 3 2 2 3 6 6 2 | 6 2 6 5 2 2 5 3 4 6 2 5 3 6 3 6 2 2 6 | No | 14.97 |
| 19 | 1 5 6 3 2 5 3 4 1 2 3 2 1 5 | 1 5 6 3 5 2 3 2 1 2 5 3 1 2 5 1 5 2 | No | 18.25 |
| 20 | 6 3 4 6 2 4 3 3 5 2 4 2 6 1 |  | No | 29.57 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1686 | 3372 | No | 11.07 |
| 2 | 1416 | 2832 | No | 10.39 |
| 3 | 1399 | 2798 | No | 13.93 |
| 4 | 1606 | 3212 | No | 8.07 |
| 5 | 2093 | 4186 | No | 9.04 |
| 6 | 2165 | 4330 | No | 9.62 |
| 7 | 1094 | 2188 | No | 10.24 |
| 8 | 2302 | 4604 | No | 9.86 |
| 9 | 1158 | 2316 | No | 13.44 |
| 10 | 1300 | 1300 | Yes | 12.45 |
| 11 | 1279 | 2558 | No | 10.77 |
| 12 | 1294 | 2588 | No | 9.54 |
| 13 | 1858 | 3716 | No | 12.78 |
| 14 | 1533 | 3066 | No | 10.55 |
| 15 | 973 | 1946 | No | 10.41 |
| 16 | 987 | 1974 | No | 10.33 |
| 17 | 1246 | 2492 | No | 8.54 |
| 18 | 1445 | 2890 | No | 12.66 |
| 19 | 1873 | 1873 | Yes | 8.72 |
| 20 | 1382 | 1382 | Yes | 12.38 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 46 | 46 | Yes | 13.36 |
| 2 | 58 |  | No | 28.08 |
| 3 | 52 | 53 | No | 17.02 |
| 4 | 47 | 48 | No | 13.52 |
| 5 | 69 | 69 | Yes | 11.9 |
| 6 | 72 |  | No | 28.22 |
| 7 | 53 | 53 | Yes | 13.1 |
| 8 | 59 | 61 | No | 14.59 |
| 9 | 37 | 37 | Yes | 16.72 |
| 10 | 62 | 63 | No | 15.77 |
| 11 | 45 | 44 | No | 15.15 |
| 12 | 62 |  | No | 25.26 |
| 13 | 40 | 40 | Yes | 11.04 |
| 14 | 54 | 54 | Yes | 13.05 |
| 15 | 63 | 60 | No | 14.66 |
| 16 | 37 | 37 | Yes | 12.45 |
| 17 | 40 | 41 | No | 11.95 |
| 18 | 75 | 67 | No | 9.99 |
| 19 | 68 | 67 | No | 15.24 |
| 20 | 51 | 51 | Yes | 12.45 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GIBLCDY | GIBLCDY | Yes | 24.7 |
| 2 | FWUYXPS | FWUYXPS | Yes | 6.84 |
| 3 | FMORKBH | FMORKBH | Yes | 7.36 |
| 4 | TDKWEHO | TDKWEHO | Yes | 8.21 |
| 5 | JTVYMFG | JTVYMFG | Yes | 7.09 |
| 6 | BWRSJFU | BWRSJFU | Yes | 7.44 |
| 7 | LRMBEIG | LRMBEIG | Yes | 7.93 |
| 8 | UCMFQLD | UCMFQLD | Yes | 8.06 |
| 9 | IXCEDGA | IXCEDGA | Yes | 6.86 |
| 10 | YRLGEHK | YRLGEHK | Yes | 8.16 |
| 11 | RFEPHWX | RFEPHWX | Yes | 7.16 |
| 12 | SFKMTHZ | SFKMTHZ | Yes | 9.92 |
| 13 | SHEINOF | SHEINOF | Yes | 8.99 |
| 14 | GHENVKL | GHENVKL | Yes | 7.76 |
| 15 | GCNSDJV | GCNSDJV | Yes | 7.11 |
| 16 | DVTMICN | DVTMICN | Yes | 6.98 |
| 17 | CADSGUV | CADSGUV | Yes | 6.49 |
| 18 | INJORWK | INJOWRK | No | 11.35 |
| 19 | NIXECWQ | NIXECWQ | Yes | 6.92 |
| 20 | OEXKDIH | OEXKDIH | Yes | 7.24 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.4, 7.6] | 2.4 7.6 | Yes | 12.47 |
| 2 | [0.8, 9.2] | 9.2 0.8 | Yes | 13.22 |
| 3 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.44 |
| 4 | [2.5, 7.5] | 7.5 2.5 | Yes | 13.93 |
| 5 | [4.4, 5.6] | 5.6 4.4 | Yes | 17.24 |
| 6 | [1.6, 8.4] | 1.6 8.4 | Yes | 9.86 |
| 7 | [2.4, 7.6] | 2.4 7.6 | Yes | 18.24 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 30.46 |
| 9 | [1.7, 8.3] | 8.3 1.7 | Yes | 11.39 |
| 10 | [1.2, 8.8] | 1.2 8.8 | Yes | 11.86 |
| 11 | [3.6, 6.4] | 6.4 3.6 | Yes | 18.49 |
| 12 | [3.9, 6.1] | 3.9 6.1 | Yes | 8.8 |
| 13 | [1.0, 9.0] | 1.0 9.0 | Yes | 12.68 |
| 14 | [2.3, 7.7] | 2.3 7.7 | Yes | 13.32 |
| 15 | [0.8, 9.2] | 0.8 9.2 | Yes | 42.1 |
| 16 | [1.5, 8.5] | 8.5 1.5 | Yes | 7.9 |
| 17 | [0.6, 9.4] | 9.4 0.6 | Yes | 9.65 |
| 18 | [3.3, 6.7] | 6.7 3.3 | Yes | 23.66 |
| 19 | [4.3, 5.7] | 4.3 5.7 | Yes | 21.22 |
| 20 | [2.9, 7.1] | 2.9 7.1 | Yes | 13.31 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CA2MSJ5FE16K | CA2MSJ5FE16K | Yes | 7.34 |
| 2 | AKL4UUC2C5LN | AKL4UUC2C5LN | Yes | 10.22 |
| 3 | 3FZ8T4E6VHQJ | 3FZ8T4E6VHQJ | Yes | 7.1 |
| 4 | NAM01J6WYDDN | NAM01J6WYDDN | Yes | 6.39 |
| 5 | IG4F8S99TU5F | IG4F8S99TU5F | Yes | 8.94 |
| 6 | KOCK647LPM3B | KOCK647LPM3B | Yes | 11.62 |
| 7 | FLENLTQMZK91 | FLENLTQMZK91 | Yes | 3.64 |
| 8 | U1OM6PW79I76 | U1OM6PW79I76 | Yes | 17.1 |
| 9 | AF05QEL47XG0 | AF05QEL47XG0 | Yes | 7.27 |
| 10 | B6UBQ6606L0P | B6UBQ6606L0P | Yes | 3.98 |
| 11 | BRX0VOA5WO05 | BRX0VOA5WO05 | Yes | 18.23 |
| 12 | NK2Z4G12MM2I | NK2Z4G12MM2I | Yes | 2.35 |
| 13 | FL15HHYCV1FN | FL15HHYCV1FN | Yes | 4.89 |
| 14 | QKPFP9ANTUM9 | QKPFP9ANTUM9 | Yes | 17.26 |
| 15 | VW9SLPPZR0RN | VW9SLPPZR0RN | Yes | 12.2 |
| 16 | XN7ZZGF4MGEC | XN7ZZGF4MGEC | Yes | 9.36 |
| 17 | J0GNEUI8R0Y1 | J0GNEUI8R0Y1 | Yes | 10.15 |
| 18 | BXANKTP5XVFF | BXANKTP5XVFF | Yes | 16.18 |
| 19 | OGHO4AH0DRA7 | OGHO4AH0DRA7 | Yes | 6.07 |
| 20 | RHE5C28UOSXT | RHE5C28UOSXT | Yes | 2.55 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7 | 7 | Yes | 16.86 |
| 2 | 5 | 18 | No | 22.22 |
| 3 | 793 | 793 | Yes | 15.9 |
| 4 | 16 | 16 | Yes | 9.39 |
| 5 | 9 | 9 | Yes | 18.76 |
| 6 | 4 | 4 | Yes | 18.56 |
| 7 | 23 | 23 | Yes | 6.5 |
| 8 | 1440 | 1440 | Yes | 10.65 |
| 9 | 67 | 67 | Yes | 47.16 |
| 10 | 20 | 20 | Yes | 43.61 |
| 11 | 19 | 19 | Yes | 13.9 |
| 12 | 4096 | 4096 | Yes | 16.03 |
| 13 | 36 | 36 | Yes | 18.45 |
| 14 | 73 | 73 | Yes | 18.68 |
| 15 | 39 | 39 | Yes | 8.36 |
| 16 | 3 | 3 | Yes | 6.96 |
| 17 | 28 | 28 | Yes | 9.86 |
| 18 | 48 | 48 | Yes | 8.26 |
| 19 | 44 | 44 | Yes | 8.76 |
| 20 | 60 | 60 | Yes | 17.56 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _\/(/_ _\ | _\/(/_ _\ | Yes | 7.77 |
| 2 | _<_/(/<(< | _<_/(/<(< | Yes | 6.46 |
| 3 | /_/\_/_(_ | /_/\_/_(_ | Yes | 6.5 |
| 4 | <\\<)) << | <\\<)) << | Yes | 7.69 |
| 5 | < (_\\ /\ | < (_\\ / | No | 19.21 |
| 6 | </_< \)// | </_< \))/) | No | 17.23 |
| 7 | /< ()\\\< | /< () \\\< | No | 10.1 |
| 8 | ((/<))/ < | ((/<))/ < | Yes | 7.13 |
| 9 | <</ <\\(< | <</ <\\(< | Yes | 6.43 |
| 10 | (/) <<<<\ | (/) <<<<\ | Yes | 6.87 |
| 11 | </ _<((\_ | </ _<((\_ | Yes | 6.52 |
| 12 |  \\\)/(\< | \\\)/(\< | No | 6.17 |
| 13 | ___\/_\(\ | ___\/_\(\ | Yes | 20.07 |
| 14 | _)\<(/)\) | _)\<(/)\) | Yes | 6.49 |
| 15 | (_) \_/<( | (_) \_/<( | Yes | 4.98 |
| 16 | <\<< _ (_ | <\<< _ (_ | Yes | 7.14 |
| 17 |  _)//_))( | _)//_))( | No | 6.74 |
| 18 | </< _(_\( | </< _(_\( | Yes | 6.37 |
| 19 | /)< <///\ | /)< <///\ | Yes | 16.1 |
| 20 |  \<)<<_</ | \<)<<_</ | No | 7.36 |
