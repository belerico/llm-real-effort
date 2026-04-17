# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-26 15:39:06

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
| sudoku_game | 5521 | 31377 | 36898 | 5 | 15 | 29.44 | 588.87 |
| add_numbers | 3180 | 701 | 3881 | 20 | 0 | 1.85 | 37.0 |
| counting_zeros | 4500 | 15296 | 19796 | 3 | 17 | 10.15 | 203.1 |
| task_decoding | 4500 | 2277 | 6777 | 19 | 1 | 3.74 | 74.83 |
| task_summation | 4560 | 3268 | 7828 | 20 | 0 | 3.54 | 70.82 |
| task_transcription | 3349 | 769 | 4118 | 20 | 0 | 2.13 | 42.6 |
| task_sequences | 3241 | 3462 | 6703 | 19 | 1 | 4.21 | 84.22 |
| string_entry | 3697 | 1520 | 5217 | 12 | 8 | 3.10 | 62.08 |
| **TOTAL** | **32548** | **58670** | **91218** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 6 1 3 4 4 6 5 4 5 5 4 3 |  | No | 35.35 |
| 2 | 2 6 1 4 6 3 6 5 3 2 6 2 4 1 | 2 6 1 4 6 3 6 5 3 2 6 2 4 1 | Yes | 15.66 |
| 3 | 4 6 5 2 4 1 6 2 2 4 5 1 6 3 | 4 6 5 2 6 2 4 1 2 3 4 5 1 6 3 | No | 20.0 |
| 4 | 2 1 6 2 5 2 3 5 3 4 6 5 6 1 | 2 1 6 2 5 2 3 5 3 4 6 5 3 4 6 5 6 1 | No | 24.49 |
| 5 | 3 1 6 6 3 6 3 3 6 4 1 2 6 1 | 1 6 3 6 3 1 6 6 6 4 3 2 3 1 | No | 27.09 |
| 6 | 5 1 3 3 5 6 6 2 5 6 3 4 1 6 |  | No | 36.63 |
| 7 | 6 2 6 2 1 5 6 4 3 6 5 1 2 5 | TIMEOUT | No | 120.04 |
| 8 | 4 2 2 5 1 3 5 4 6 4 2 3 5 1 | 4 2 2 5 1 4 5 3 1 3 6 2 4 6 5 3 2 4 5 1 | No | 21.54 |
| 9 | 6 2 4 5 1 3 6 2 2 5 6 6 5 4 | 6 2 4 5 1 3 2 2 5 6 6 4 | No | 18.92 |
| 10 | 2 5 5 6 6 5 2 3 4 6 3 5 5 4 | 2 5 5 6 6 5 2 3 4 6 3 5 5 4 | Yes | 25.93 |
| 11 | 1 2 3 5 4 5 4 2 3 4 2 5 1 1 |  | No | 25.43 |
| 12 | 5 3 1 4 6 1 6 2 6 4 5 1 6 3 | 5 3 1 6 4 1 6 2 4 6 1 6 | No | 20.99 |
| 13 | 5 1 6 2 3 2 3 6 2 6 3 5 6 4 | 5 1 6 2 3 2 3 6 2 6 3 5 6 4 | Yes | 19.38 |
| 14 | 2 6 5 3 3 6 5 1 1 5 2 3 4 1 | 2 6 5 3 3 6 5 1 1 4 5 2 5 3 4 1 3 1 | No | 18.69 |
| 15 | 3 4 3 1 3 1 1 5 2 2 3 4 4 3 |  | No | 34.65 |
| 16 | 6 2 4 1 6 2 4 6 4 5 3 5 6 2 | 6 2 4 1 6 2 4 6 4 5 3 5 6 2 | Yes | 18.08 |
| 17 | 5 3 2 6 2 6 4 4 3 2 5 6 5 2 | 5 3 2 6 2 6 4 4 3 2 5 6 5 2 | Yes | 19.75 |
| 18 | 2 6 3 1 5 5 1 2 1 3 2 5 5 4 |  | No | 33.41 |
| 19 | 1 3 5 1 6 2 4 6 1 2 6 4 4 5 | 1 3 5 1 6 2 4 6 1 2 6 3 4 4 5 | No | 20.29 |
| 20 | 1 3 5 4 2 1 3 4 6 2 3 4 2 5 |  | No | 32.52 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1618 | 1618 | Yes | 3.27 |
| 2 | 900 | 900 | Yes | 1.34 |
| 3 | 1850 | 1850 | Yes | 2.07 |
| 4 | 2212 | 2212 | Yes | 1.92 |
| 5 | 2237 | 2237 | Yes | 1.33 |
| 6 | 1654 | 1654 | Yes | 2.99 |
| 7 | 1892 | 1892 | Yes | 2.8 |
| 8 | 1046 | 1046 | Yes | 1.87 |
| 9 | 1658 | 1658 | Yes | 2.12 |
| 10 | 787 | 787 | Yes | 2.07 |
| 11 | 1467 | 1467 | Yes | 1.52 |
| 12 | 1961 | 1961 | Yes | 1.68 |
| 13 | 2063 | 2063 | Yes | 1.49 |
| 14 | 890 | 890 | Yes | 1.24 |
| 15 | 1398 | 1398 | Yes | 1.28 |
| 16 | 893 | 893 | Yes | 1.69 |
| 17 | 1637 | 1637 | Yes | 1.64 |
| 18 | 1695 | 1695 | Yes | 1.3 |
| 19 | 2043 | 2043 | Yes | 1.68 |
| 20 | 634 | 634 | Yes | 1.69 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 58 | 50 | No | 14.44 |
| 2 | 42 | 42 | Yes | 15.41 |
| 3 | 35 | 34 | No | 11.61 |
| 4 | 53 | 52 | No | 11.04 |
| 5 | 56 | 55 | No | 12.27 |
| 6 | 52 | 48 | No | 5.15 |
| 7 | 50 | 49 | No | 6.99 |
| 8 | 47 | 46 | No | 10.61 |
| 9 | 37 | 34 | No | 10.27 |
| 10 | 70 | 67 | No | 8.94 |
| 11 | 69 | 64 | No | 6.71 |
| 12 | 52 | 45 | No | 7.61 |
| 13 | 62 | 54 | No | 13.55 |
| 14 | 37 | 35 | No | 9.64 |
| 15 | 75 | 75 | Yes | 10.56 |
| 16 | 75 | 68 | No | 9.02 |
| 17 | 36 | 36 | Yes | 6.72 |
| 18 | 44 | 41 | No | 8.26 |
| 19 | 61 | 52 | No | 9.33 |
| 20 | 54 | 49 | No | 14.97 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KNXIMUQ | KNXIMUQ | Yes | 4.19 |
| 2 | FPTWVMY | FPTWVMY | Yes | 2.32 |
| 3 | BRTKFDE | BRTKFDE | Yes | 2.82 |
| 4 | KLFOJCI | KLFOJCI | Yes | 4.0 |
| 5 | DHMUSKV | DHUSMKV | No | 2.32 |
| 6 | OBVDXQC | OBVDXQC | Yes | 2.97 |
| 7 | FWHXQMO | FWHXQMO | Yes | 3.0 |
| 8 | FJHKDAB | FJHKDAB | Yes | 5.03 |
| 9 | DNYZGQR | DNYZGQR | Yes | 3.75 |
| 10 | CEFPQNM | CEFPQNM | Yes | 3.67 |
| 11 | UNCFPIM | UNCFPIM | Yes | 3.6 |
| 12 | EDIFMAP | EDIFMAP | Yes | 3.27 |
| 13 | IMYCZSL | IMYCZSL | Yes | 10.76 |
| 14 | AORNGWF | AORNGWF | Yes | 3.17 |
| 15 | ANZRJPS | ANZRJPS | Yes | 3.72 |
| 16 | PSFBQWZ | PSFBQWZ | Yes | 3.11 |
| 17 | YLQWVEP | YLQWVEP | Yes | 2.36 |
| 18 | DVYXOIF | DVYXOIF | Yes | 2.91 |
| 19 | PNOACJF | PNOACJF | Yes | 3.27 |
| 20 | EJOZSTM | EJOZSTM | Yes | 4.6 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.1, 6.9] | 6.9 3.1 | Yes | 1.76 |
| 2 | [4.8, 5.2] | 4.8 5.2 | Yes | 2.67 |
| 3 | [3.0, 7.0] | 7.0 3.0 | Yes | 4.21 |
| 4 | [2.6, 7.4] | 2.6 7.4 | Yes | 3.07 |
| 5 | [1.0, 9.0] | 9.0 1.0 | Yes | 2.3 |
| 6 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.34 |
| 7 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.01 |
| 8 | [4.2, 5.8] | 4.2 5.8 | Yes | 3.79 |
| 9 | [4.6, 5.4] | 5.4 4.6 | Yes | 2.91 |
| 10 | [1.5, 8.5] | 8.5 1.5 | Yes | 7.11 |
| 11 | [1.3, 8.7] | 8.7 1.3 | Yes | 2.81 |
| 12 | [4.7, 5.3] | 4.7 5.3 | Yes | 3.59 |
| 13 | [0.8, 9.2] | 0.8 9.2 | Yes | 4.3 |
| 14 | [4.4, 5.6] | 5.6 4.4 | Yes | 2.7 |
| 15 | [2.8, 7.2] | 7.2 2.8 | Yes | 2.26 |
| 16 | [4.2, 5.8] | 4.2 5.8 | Yes | 3.38 |
| 17 | [1.6, 8.4] | 1.6 8.4 | Yes | 2.52 |
| 18 | [0.6, 9.4] | 9.4 0.6 | Yes | 4.06 |
| 19 | [2.9, 7.1] | 7.1 2.9 | Yes | 4.84 |
| 20 | [0.2, 9.8] | 0.2 9.8 | Yes | 3.18 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1HBD2LFKIG8N | 1HBD2LFKIG8N | Yes | 1.83 |
| 2 | WD8IMJI0B859 | WD8IMJI0B859 | Yes | 1.16 |
| 3 | WSPJHGQ9BYV9 | WSPJHGQ9BYV9 | Yes | 1.06 |
| 4 | 9Q7AIXUQTX9Z | 9Q7AIXUQTX9Z | Yes | 1.67 |
| 5 | 60CC5FP4J6GE | 60CC5FP4J6GE | Yes | 2.6 |
| 6 | J9H7GWM96X9O | J9H7GWM96X9O | Yes | 2.2 |
| 7 | 4HC9M7AQ8FE0 | 4HC9M7AQ8FE0 | Yes | 2.38 |
| 8 | 0KN0UTW73O9K | 0KN0UTW73O9K | Yes | 2.85 |
| 9 | Y07HE6IP4DNO | Y07HE6IP4DNO | Yes | 3.62 |
| 10 | 4GV0CRH7PK3V | 4GV0CRH7PK3V | Yes | 3.25 |
| 11 | PS0MWMK3K2IK | PS0MWMK3K2IK | Yes | 4.76 |
| 12 | A3BKOJ5XY06J | A3BKOJ5XY06J | Yes | 1.64 |
| 13 | KQU55YM291HL | KQU55YM291HL | Yes | 2.12 |
| 14 | 39SDCGBVTV7I | 39SDCGBVTV7I | Yes | 1.82 |
| 15 | 0NAVP00WQTU8 | 0NAVP00WQTU8 | Yes | 1.73 |
| 16 | U3NQOEF38OYU | U3NQOEF38OYU | Yes | 1.1 |
| 17 | SUO0WMUBFXBU | SUO0WMUBFXBU | Yes | 1.69 |
| 18 | 2M4CUYIB8SP3 | 2M4CUYIB8SP3 | Yes | 1.29 |
| 19 | JC3DUK19AG3A | JC3DUK19AG3A | Yes | 2.74 |
| 20 | DSFGAOCXN5T2 | DSFGAOCXN5T2 | Yes | 1.1 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 10 | 10 | Yes | 2.43 |
| 2 | 20 | 20 | Yes | 9.6 |
| 3 | 31 | 31 | Yes | 3.33 |
| 4 | 60 | 60 | Yes | 3.96 |
| 5 | 1 | 1 | Yes | 5.72 |
| 6 | 39 | 39 | Yes | 4.73 |
| 7 | 23 | 23 | Yes | 3.85 |
| 8 | 26 | 26 | Yes | 6.98 |
| 9 | 198 | 198 | Yes | 2.21 |
| 10 | 3 | 3 | Yes | 4.38 |
| 11 | 4096 | 16384 | No | 7.32 |
| 12 | 9 | 9 | Yes | 3.66 |
| 13 | 48 | 48 | Yes | 2.05 |
| 14 | 63 | 63 | Yes | 2.07 |
| 15 | 9 | 9 | Yes | 4.95 |
| 16 | 65 | 65 | Yes | 2.3 |
| 17 | 36 | 36 | Yes | 1.79 |
| 18 | 3 | 3 | Yes | 6.86 |
| 19 | 1440 | 1440 | Yes | 3.26 |
| 20 | 7 | 7 | Yes | 2.77 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (\/)( (/< | (\/)( (/ | No | 4.93 |
| 2 | ()_((<_ / | ()_((<_ / | Yes | 2.48 |
| 3 | << ( <(\( | << ( <(\( | Yes | 5.4 |
| 4 | </<_<)<)< | </<_<)<) | No | 4.22 |
| 5 | /) \(()<( | /) \(()<( | Yes | 2.16 |
| 6 | ) /( /( ) | ) /( /( ) | Yes | 2.28 |
| 7 |  </)__/</ | </)__/</ | No | 1.91 |
| 8 |  <_\\(\/( | <_\\(\/( | No | 2.34 |
| 9 | (\< ))/</ | (\< ]))/</ | No | 2.87 |
| 10 | )))(  _/) | )))(  _/) | Yes | 1.71 |
| 11 | </<<)/(/) | </<<)/(/) | Yes | 4.83 |
| 12 | \ _/<(/\/ | \ _/<(/\/ | Yes | 1.54 |
| 13 | _)\ _)/\  | _)\ _)/\ | No | 2.27 |
| 14 | < )(_)))( | < )(_)))( | Yes | 2.48 |
| 15 | (/<_)_<)/ | (/<_)_<)/ | Yes | 4.7 |
| 16 | )( <_\()  | )( <_\() | No | 3.07 |
| 17 | /))\/ /)  | /))\ /) | No | 3.38 |
| 18 | /)<())((_ | /)<())((_ | Yes | 3.28 |
| 19 | </(_)( \) | </(_)( \) | Yes | 4.29 |
| 20 | ((( \\( ) | ((( \\( ) | Yes | 1.92 |
