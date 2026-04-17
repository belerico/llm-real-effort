# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 10:46:53

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
| sudoku_game | 7360 | 35200 | 42560 | 8 | 12 | 18.48 | 369.83 |
| add_numbers | 3940 | 1905 | 5845 | 19 | 1 | 3.75 | 75.12 |
| counting_zeros | 6360 | 30528 | 36888 | 2 | 18 | 14.78 | 295.83 |
| task_decoding | 12100 | 3376 | 15476 | 20 | 0 | 4.55 | 91.19 |
| task_summation | 7300 | 6202 | 13502 | 20 | 0 | 5.52 | 110.52 |
| task_transcription | 3764 | 12843 | 16607 | 17 | 3 | 10.65 | 213.11 |
| task_sequences | 3060 | 8049 | 11109 | 17 | 3 | 7.46 | 149.24 |
| string_entry | 4360 | 31086 | 35446 | 9 | 11 | 24.01 | 480.25 |
| **TOTAL** | **48244** | **129189** | **177433** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 6 2 4 1 3 1 5 2 5 6 4 1 |  | No | 24.49 |
| 2 | 4 6 3 1 5 1 5 3 2 2 6 4 6 3 |  | No | 28.26 |
| 3 | 3 1 4 5 3 6 1 1 1 4 2 6 5 3 |  | No | 17.72 |
| 4 | 6 2 1 4 4 2 3 6 6 5 1 5 2 4 | 6 2 1 4 4 2 3 6 6 5 1 5 2 4 | Yes | 12.58 |
| 5 | 3 5 6 4 2 6 1 4 2 6 1 3 6 2 | 3 5 6 4 2 6 1 4 2 6 1 3 6 2 | Yes | 8.94 |
| 6 | 6 2 5 4 6 2 3 5 5 1 6 4 3 1 | 6 2 5 4 6 2 3 5 5 1 6 4 3 1 | Yes | 12.8 |
| 7 | 3 6 2 3 1 5 1 2 4 1 3 5 3 1 |  | No | 15.28 |
| 8 | 5 4 6 2 1 3 5 1 5 3 5 3 6 3 | 5 4 6 2 1 3 5 1 5 3 5 3 6 3 | Yes | 10.54 |
| 9 | 6 2 3 2 1 6 2 2 4 5 6 6 3 2 |  | No | 24.91 |
| 10 | 4 1 2 6 6 4 1 4 2 5 3 6 3 3 |  | No | 24.06 |
| 11 | 6 2 3 5 2 3 1 1 4 6 6 3 4 2 |  | No | 24.97 |
| 12 | 5 2 6 5 3 6 4 5 6 1 2 4 2 1 |  | No | 26.63 |
| 13 | 5 6 3 6 1 5 4 3 6 2 4 5 3 5 |  | No | 29.89 |
| 14 | 2 6 5 4 5 5 2 3 1 4 6 6 2 1 | 2 6 5 4 5 5 2 3 1 4 6 6 2 1 | Yes | 15.72 |
| 15 | 1 5 6 1 3 4 6 4 5 3 4 1 3 6 | 1 5 6 1 3 4 6 4 5 3 4 1 3 6 | Yes | 11.52 |
| 16 | 2 3 4 4 2 6 5 2 3 6 5 5 6 3 |  | No | 18.97 |
| 17 | 3 5 3 1 2 5 3 1 1 3 6 6 4 1 |  | No | 26.97 |
| 18 | 5 2 4 6 6 3 1 4 5 6 6 3 1 5 | 5 2 4 6 6 3 1 4 5 6 6 3 1 5 | Yes | 12.69 |
| 19 | 6 2 1 1 4 4 6 5 1 6 1 5 2 3 |  | No | 17.35 |
| 20 | 4 6 1 4 2 1 6 4 6 5 2 5 6 2 | 4 6 1 4 2 1 6 4 6 5 2 5 6 2 | Yes | 5.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1610 | 1610 | Yes | 4.1 |
| 2 | 1870 | 1870 | Yes | 4.34 |
| 3 | 1600 | 1600 | Yes | 3.78 |
| 4 | 2199 | 2199 | Yes | 4.72 |
| 5 | 1687 | 1687 | Yes | 4.15 |
| 6 | 1959 | 1959 | Yes | 3.16 |
| 7 | 1437 | 1437 | Yes | 3.03 |
| 8 | 1703 | 2103 | No | 1.76 |
| 9 | 1931 | 1931 | Yes | 4.36 |
| 10 | 1372 | 1372 | Yes | 3.79 |
| 11 | 1137 | 1137 | Yes | 3.49 |
| 12 | 1665 | 1665 | Yes | 6.1 |
| 13 | 1804 | 1804 | Yes | 4.59 |
| 14 | 810 | 810 | Yes | 3.52 |
| 15 | 1002 | 1002 | Yes | 2.57 |
| 16 | 731 | 731 | Yes | 3.69 |
| 17 | 2084 | 2084 | Yes | 2.8 |
| 18 | 1449 | 1449 | Yes | 4.27 |
| 19 | 1567 | 1567 | Yes | 4.2 |
| 20 | 1848 | 1848 | Yes | 2.6 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 38 | No | 9.64 |
| 2 | 68 |  | No | 27.97 |
| 3 | 50 |  | No | 23.48 |
| 4 | 37 |  | No | 19.46 |
| 5 | 53 |  | No | 23.03 |
| 6 | 75 | 75 | Yes | 11.27 |
| 7 | 49 | 45 | No | 10.28 |
| 8 | 69 | 71 | No | 8.51 |
| 9 | 36 | 33 | No | 13.85 |
| 10 | 44 | 42 | No | 8.15 |
| 11 | 51 | 50 | No | 13.73 |
| 12 | 60 | 61 | No | 8.63 |
| 13 | 47 |  | No | 11.08 |
| 14 | 70 | 72 | No | 14.17 |
| 15 | 73 | 71 | No | 17.15 |
| 16 | 58 | 55 | No | 11.78 |
| 17 | 47 | 46 | No | 9.65 |
| 18 | 62 |  | No | 14.49 |
| 19 | 54 |  | No | 24.85 |
| 20 | 40 | 40 | Yes | 14.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EVOMRKJ | EVOMRKJ | Yes | 6.96 |
| 2 | DOYZGFC | DOYZGFC | Yes | 5.37 |
| 3 | YBJLNOH | YBJLNOH | Yes | 4.29 |
| 4 | JXFQATK | JXFQATK | Yes | 5.54 |
| 5 | PLWHAMX | PLWHAMX | Yes | 4.47 |
| 6 | RQPMEXU | RQPMEXU | Yes | 2.2 |
| 7 | JOALSWQ | JOALSWQ | Yes | 4.22 |
| 8 | WVCHMDY | WVCHMDY | Yes | 2.14 |
| 9 | NILJBEF | NILJBEF | Yes | 5.03 |
| 10 | TENPSOI | TENPSOI | Yes | 4.8 |
| 11 | COHKTVS | COHKTVS | Yes | 4.79 |
| 12 | GEINTAQ | GEINTAQ | Yes | 4.42 |
| 13 | BQSGVLA | BQSGVLA | Yes | 4.47 |
| 14 | KMJPCOS | KMJPCOS | Yes | 4.37 |
| 15 | TLHYBCZ | TLHYBCZ | Yes | 4.38 |
| 16 | QAOYKCR | QAOYKCR | Yes | 5.21 |
| 17 | DRFWTVH | DRFWTVH | Yes | 3.82 |
| 18 | LDIUNJS | LDIUNJS | Yes | 5.33 |
| 19 | SBQYVEI | SBQYVEI | Yes | 3.72 |
| 20 | QUVSAZJ | QUVSAZJ | Yes | 5.46 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.4, 6.6] | 6.6 3.4 | Yes | 4.57 |
| 2 | [4.8, 5.2] | 5.2 4.8 | Yes | 6.23 |
| 3 | [4.5, 5.5] | 4.5 5.5 | Yes | 4.42 |
| 4 | [4.4, 5.6] | 4.4 5.6 | Yes | 5.39 |
| 5 | [0.4, 9.6] | 9.6 0.4 | Yes | 6.18 |
| 6 | [0.7, 9.3] | 9.3 0.7 | Yes | 5.52 |
| 7 | [4.5, 5.5] | 5.5 4.5 | Yes | 7.3 |
| 8 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.54 |
| 9 | [4.5, 5.5] | 5.5 4.5 | Yes | 5.58 |
| 10 | [2.6, 7.4] | 2.6 7.4 | Yes | 7.59 |
| 11 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.37 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.04 |
| 13 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.34 |
| 14 | [4.4, 5.6] | 5.6 4.4 | Yes | 5.26 |
| 15 | [1.3, 8.7] | 8.7 1.3 | Yes | 4.61 |
| 16 | [0.9, 9.1] | 0.9 9.1 | Yes | 5.24 |
| 17 | [3.8, 6.2] | 3.8 6.2 | Yes | 4.08 |
| 18 | [5.0, 5.0] | 5.0 5.0 | Yes | 4.45 |
| 19 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.43 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.2 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 10NJDRZXI7KJ | 10NJDRZXI7KJ | Yes | 3.35 |
| 2 | RA50DS10EATB | RA50DS10EATB | Yes | 6.32 |
| 3 | 8OGGYRVQAWB4 | 8OGGYRVQAWB4 | Yes | 6.89 |
| 4 | 00HTS44HNUBV | 00HTS44HNUBV | Yes | 7.61 |
| 5 | JL85QNM515GF | JL85QNM515GF | Yes | 6.22 |
| 6 | PP0KQSPPT3MF | PP0K0SPPT3MF | No | 3.74 |
| 7 | H425PSU8RQZS | H425PSU8RQZS | Yes | 15.73 |
| 8 | 2B5AWORZG52L |  | No | 43.13 |
| 9 | 0OBG7SNW0TOW | OOBG7SNWOTOW | No | 9.61 |
| 10 | KKQNNRMAV3Z2 | KKQNNRMAV3Z2 | Yes | 11.13 |
| 11 | Q73WIBUXCNDI | Q73WIBUXCNDI | Yes | 4.26 |
| 12 | XQPHQULQ6AUU | XQPHQULQ6AUU | Yes | 14.6 |
| 13 | 7R4LGBIZKPTW | 7R4LGBIZKPTW | Yes | 4.67 |
| 14 | 0BZU54JLNR8F | 0BZU54JLNR8F | Yes | 10.44 |
| 15 | 41UVYV3NDGNS | 41UVYV3NDGNS | Yes | 4.95 |
| 16 | FUDKT199FR7Q | FUDKT199FR7Q | Yes | 7.86 |
| 17 | MTI70VRI8AUP | MTI70VRI8AUP | Yes | 31.64 |
| 18 | E1P4R7GNICPT | E1P4R7GNICPT | Yes | 7.73 |
| 19 | R2EKYEARJXYV | R2EKYEARJXYV | Yes | 10.21 |
| 20 | EG4W5WDDKFKV | EG4W5WDDKFKV | Yes | 2.91 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 4.44 |
| 2 | 48 | 48 | Yes | 3.36 |
| 3 | 36 | 36 | Yes | 2.77 |
| 4 | 7680 | 7680 | Yes | 5.23 |
| 5 | 4 | 4 | Yes | 3.36 |
| 6 | 28 | 28 | Yes | 4.48 |
| 7 | 4 | 4 | Yes | 3.08 |
| 8 | 5 |  | No | 21.95 |
| 9 | 39 | 39 | Yes | 3.55 |
| 10 | 31 | 31 | Yes | 2.97 |
| 11 | 1440 | 1440 | Yes | 3.3 |
| 12 | 3 |  | No | 29.25 |
| 13 | 64 | 64 | Yes | 5.13 |
| 14 | 6 | 6 | Yes | 2.94 |
| 15 | 198 | 198 | Yes | 5.46 |
| 16 | 7 | 7 | Yes | 3.74 |
| 17 | 23 | 23 | Yes | 4.0 |
| 18 | 10 |  | No | 32.72 |
| 19 | 9 | 9 | Yes | 3.92 |
| 20 | 60 | 60 | Yes | 3.58 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _<<(< \)< | _<<(< \)< | Yes | 8.15 |
| 2 | / ((/(_\  |  | No | 29.18 |
| 3 | <) )/  /\ |  | No | 35.87 |
| 4 | _)/(\/)<) |  | No | 28.28 |
| 5 | <\/( )(<< | <\/( )(<< | Yes | 20.67 |
| 6 | _/)/\< (< | _/)/\< (< | Yes | 10.99 |
| 7 | /)\<_  <\ | /)\<_  <\ | Yes | 23.38 |
| 8 | ///<</(\_ | ///<</(\_ | Yes | 15.01 |
| 9 | <)\<)_/\\ | <)\<)_/\\ | Yes | 10.51 |
| 10 | _)/ __<\) | _)/ __<\) | Yes | 18.75 |
| 11 |  /\<)_(__ |  | No | 44.85 |
| 12 | <_\\( )/  |  | No | 32.53 |
| 13 | <  < <_)_ |  | No | 30.68 |
| 14 | )(//< )_( | )((//< )_( | No | 16.56 |
| 15 | _/_ )\ (/ | _/_ )\ (/ | Yes | 25.65 |
| 16 | //(<_ )</ |  | No | 26.67 |
| 17 | /)(\)\(<\ |  | No | 38.6 |
| 18 | <\)))(\(/ | <\)))(\(/ | Yes | 7.68 |
| 19 | ( /(_ /_  |  | No | 20.8 |
| 20 | /_/\)/ \\ |  | No | 35.34 |
