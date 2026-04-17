# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-27 10:26:51

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
| sudoku_game | 4887 | 38912 | 43799 | 0 | 20 | 42.02 | 840.5 |
| add_numbers | 2900 | 3235 | 6135 | 20 | 0 | 3.19 | 63.77 |
| counting_zeros | 4300 | 40494 | 44794 | 1 | 19 | 35.84 | 716.85 |
| task_decoding | 4240 | 8985 | 13225 | 20 | 0 | 7.36 | 147.23 |
| task_summation | 4580 | 18462 | 23042 | 20 | 0 | 11.19 | 223.89 |
| task_transcription | 3044 | 2769 | 5813 | 20 | 0 | 2.40 | 48.01 |
| task_sequences | 2901 | 11616 | 14517 | 18 | 2 | 9.80 | 196.08 |
| string_entry | 3342 | 35387 | 38729 | 4 | 16 | 21.25 | 424.99 |
| **TOTAL** | **30194** | **159860** | **190054** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 3 5 1 6 2 2 3 5 4 6 1 3 2 |  | No | 41.0 |
| 2 | 2 4 2 1 5 4 5 1 6 1 1 4 5 2 |  | No | 37.51 |
| 3 | 1 2 4 2 2 3 1 3 5 2 2 5 6 3 |  | No | 41.53 |
| 4 | 4 2 5 6 6 5 6 1 4 2 2 3 6 5 |  | No | 40.15 |
| 5 | 6 4 3 5 4 5 4 2 3 5 5 5 2 3 | TIMEOUT | No | 120.05 |
| 6 | 3 6 2 5 3 2 1 4 4 3 2 5 4 1 |  | No | 33.67 |
| 7 | 1 5 2 5 6 4 1 6 3 5 5 6 6 3 |  | No | 38.17 |
| 8 | 5 3 2 6 1 5 2 1 6 1 6 5 4 3 |  | No | 31.13 |
| 9 | 4 1 2 6 2 4 1 6 3 6 5 2 4 3 |  | No | 36.12 |
| 10 | 2 1 6 2 5 1 1 3 6 6 3 2 5 1 |  | No | 38.42 |
| 11 | 5 4 6 3 1 3 4 2 3 2 2 5 6 4 |  | No | 29.57 |
| 12 | 3 4 2 1 5 6 2 1 3 5 5 5 6 1 |  | No | 34.68 |
| 13 | 3 5 4 6 4 2 2 6 6 1 4 2 4 5 |  | No | 28.11 |
| 14 | 4 5 1 4 2 4 1 2 4 5 3 3 5 2 |  | No | 37.44 |
| 15 | 6 1 2 2 3 2 5 5 6 3 4 1 4 5 |  | No | 41.11 |
| 16 | 1 5 4 5 1 3 6 4 3 1 2 6 2 3 |  | No | 43.33 |
| 17 | 3 6 2 6 6 4 4 4 6 2 3 2 3 4 |  | No | 39.54 |
| 18 | 5 3 1 2 1 6 4 5 6 2 2 5 4 3 |  | No | 40.75 |
| 19 | 5 4 6 3 6 1 3 5 6 3 1 1 5 6 |  | No | 42.03 |
| 20 | 5 5 3 4 4 6 2 1 3 2 4 5 5 1 |  | No | 46.15 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2418 | 2418 | Yes | 2.32 |
| 2 | 1410 | 1410 | Yes | 3.87 |
| 3 | 1695 | 1695 | Yes | 2.65 |
| 4 | 1703 | 1703 | Yes | 2.47 |
| 5 | 1851 | 1851 | Yes | 2.41 |
| 6 | 1845 | 1845 | Yes | 4.42 |
| 7 | 1544 | 1544 | Yes | 2.92 |
| 8 | 2040 | 2040 | Yes | 4.9 |
| 9 | 1994 | 1994 | Yes | 2.31 |
| 10 | 2158 | 2158 | Yes | 2.45 |
| 11 | 1899 | 1899 | Yes | 4.0 |
| 12 | 1801 | 1801 | Yes | 4.96 |
| 13 | 1525 | 1525 | Yes | 2.52 |
| 14 | 1180 | 1180 | Yes | 2.52 |
| 15 | 1780 | 1780 | Yes | 3.52 |
| 16 | 2136 | 2136 | Yes | 2.92 |
| 17 | 1385 | 1385 | Yes | 4.79 |
| 18 | 1637 | 1637 | Yes | 2.78 |
| 19 | 1970 | 1970 | Yes | 2.04 |
| 20 | 1430 | 1430 | Yes | 2.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 22.39 |
| 2 | 54 |  | No | 36.33 |
| 3 | 73 |  | No | 29.35 |
| 4 | 68 |  | No | 42.3 |
| 5 | 62 |  | No | 63.03 |
| 6 | 59 |  | No | 57.29 |
| 7 | 53 |  | No | 43.48 |
| 8 | 57 |  | No | 36.29 |
| 9 | 60 |  | No | 33.23 |
| 10 | 60 |  | No | 37.61 |
| 11 | 64 | 64 | Yes | 14.99 |
| 12 | 53 |  | No | 53.81 |
| 13 | 60 |  | No | 23.71 |
| 14 | 46 |  | No | 30.19 |
| 15 | 58 |  | No | 32.33 |
| 16 | 55 |  | No | 39.01 |
| 17 | 37 |  | No | 37.21 |
| 18 | 50 |  | No | 22.35 |
| 19 | 63 |  | No | 32.41 |
| 20 | 35 |  | No | 29.49 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PGWHUDB | PGWHUDB | Yes | 5.93 |
| 2 | RSLBVUO | RSLBVUO | Yes | 4.31 |
| 3 | QPKVRMJ | QPKVRMJ | Yes | 5.07 |
| 4 | JZWOMNC | JZWOMNC | Yes | 10.71 |
| 5 | VOQHTDX | VOQHTDX | Yes | 9.64 |
| 6 | NKJUVFX | NKJUVFX | Yes | 4.37 |
| 7 | KYNFBQM | KYNFBQM | Yes | 8.13 |
| 8 | YOXWRFT | YOXWRFT | Yes | 10.59 |
| 9 | RIFSJYH | RIFSJYH | Yes | 8.28 |
| 10 | MPSJQDZ | MPSJQDZ | Yes | 7.35 |
| 11 | MRKCGTW | MRKCGTW | Yes | 5.69 |
| 12 | XZTHAVW | XZTHAVW | Yes | 7.2 |
| 13 | QZMKGUF | QZMKGUF | Yes | 6.61 |
| 14 | PKLAUHC | PKLAUHC | Yes | 7.86 |
| 15 | MXLQJBK | MXLQJBK | Yes | 4.79 |
| 16 | VWBCHPU | VWBCHPU | Yes | 13.65 |
| 17 | ZQJNTXR | ZQJNTXR | Yes | 7.47 |
| 18 | XJBYDQC | XJBYDQC | Yes | 8.08 |
| 19 | FVBYPDC | FVBYPDC | Yes | 5.09 |
| 20 | NJZIXSG | NJZIXSG | Yes | 6.4 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.7, 5.3] | 4.7 5.3 | Yes | 8.76 |
| 2 | [3.3, 6.7] | 3.3 6.7 | Yes | 9.31 |
| 3 | [0.9, 9.1] | 0.9 9.1 | Yes | 14.12 |
| 4 | [0.4, 9.6] | 0.4 9.6 | Yes | 13.3 |
| 5 | [0.7, 9.3] | 0.7 9.3 | Yes | 10.8 |
| 6 | [1.6, 8.4] | 8.4 1.6 | Yes | 12.64 |
| 7 | [0.4, 9.6] | 0.4 9.6 | Yes | 7.02 |
| 8 | [4.1, 5.9] | 4.1 5.9 | Yes | 8.12 |
| 9 | [1.0, 9.0] | 9.0 1.0 | Yes | 17.86 |
| 10 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.16 |
| 11 | [4.4, 5.6] | 4.4 5.6 | Yes | 8.89 |
| 12 | [3.3, 6.7] | 3.3 6.7 | Yes | 15.34 |
| 13 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.72 |
| 14 | [1.0, 9.0] | 1.0 9.0 | Yes | 11.28 |
| 15 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.46 |
| 16 | [3.6, 6.4] | 3.6 6.4 | Yes | 10.09 |
| 17 | [0.4, 9.6] | 0.4 9.6 | Yes | 10.04 |
| 18 | [3.2, 6.8] | 3.2 6.8 | Yes | 8.55 |
| 19 | [3.9, 6.1] | 3.9 6.1 | Yes | 9.58 |
| 20 | [2.0, 8.0] | 8.0 2.0 | Yes | 19.84 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MWP3Z7X8MYCJ | MWP3Z7X8MYCJ | Yes | 1.75 |
| 2 | ZDINASLSXGT9 | ZDINASLSXGT9 | Yes | 1.92 |
| 3 | NVEIS0N4CWRS | NVEIS0N4CWRS | Yes | 4.5 |
| 4 | HBJZH2T4MOB1 | HBJZH2T4MOB1 | Yes | 2.08 |
| 5 | SKTVSIHUMZY1 | SKTVSIHUMZY1 | Yes | 1.9 |
| 6 | KKXY6F8DIM7C | KKXY6F8DIM7C | Yes | 2.26 |
| 7 | XJFL5E7Q1DNN | XJFL5E7Q1DNN | Yes | 2.52 |
| 8 | 436QIK8NSY3L | 436QIK8NSY3L | Yes | 2.16 |
| 9 | YIHW97J3O7ND | YIHW97J3O7ND | Yes | 2.53 |
| 10 | I9YH25LYQQ3E | I9YH25LYQQ3E | Yes | 2.63 |
| 11 | 2L5344DVGLFJ | 2L5344DVGLFJ | Yes | 1.89 |
| 12 | 2TQCWB942TKZ | 2TQCWB942TKZ | Yes | 3.9 |
| 13 | 6GPOEOOK26SV | 6GPOEOOK26SV | Yes | 2.14 |
| 14 | 0OM29TT8GBY5 | 0OM29TT8GBY5 | Yes | 2.51 |
| 15 | 5RP5YB5IJQ7E | 5RP5YB5IJQ7E | Yes | 2.05 |
| 16 | NQSVRLB7AT8L | NQSVRLB7AT8L | Yes | 2.67 |
| 17 | W50H63CUY6BD | W50H63CUY6BD | Yes | 2.26 |
| 18 | T3DP512J5IL9 | T3DP512J5IL9 | Yes | 1.98 |
| 19 | GEOYOM0CONM5 | GEOYOM0CONM5 | Yes | 2.32 |
| 20 | 8RC53J9562AV | 8RC53J9562AV | Yes | 2.04 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 3.78 |
| 2 | 67 | 67 | Yes | 4.75 |
| 3 | 10 | 10 | Yes | 7.18 |
| 4 | 3 | 3 | Yes | 13.43 |
| 5 | 60 | 60 | Yes | 4.85 |
| 6 | 5 | 5 | Yes | 9.28 |
| 7 | 793 | 793 | Yes | 3.21 |
| 8 | 4 | 4 | Yes | 6.6 |
| 9 | 48 | 48 | Yes | 3.51 |
| 10 | 44 | 44 | Yes | 11.6 |
| 11 | 1 | 1 | Yes | 6.61 |
| 12 | 63 | 63 | Yes | 2.25 |
| 13 | 16 | 16 | Yes | 2.14 |
| 14 | 9 | 9 | Yes | 4.68 |
| 15 | 7 | 7 | Yes | 2.63 |
| 16 | 6 | 6 | Yes | 8.97 |
| 17 | 7680 | 7680 | Yes | 7.88 |
| 18 | 20 | 20 | Yes | 9.5 |
| 19 | 26 |  | No | 42.1 |
| 20 | 4096 |  | No | 41.11 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \()/)(/<< |  | No | 22.32 |
| 2 | )(\_) (<_ |  | No | 20.16 |
| 3 | ()< \ )/\ |  | No | 21.69 |
| 4 | </)_(< )( |  | No | 24.52 |
| 5 | </ \\( _\ |  | No | 20.46 |
| 6 | ((\/  //_ | /\) <(_<) | No | 14.4 |
| 7 | )\\  (\)  |  | No | 29.02 |
| 8 | ( ) /) (  |  | No | 19.98 |
| 9 | /( _  /<< | /( _  /<< | Yes | 5.2 |
| 10 | /))()(</\ | /))()(</\ | Yes | 12.72 |
| 11 | )(/<_/(/< |  | No | 22.8 |
| 12 | //( _(((/ | //( _(((/) | No | 13.83 |
| 13 | )))//(\\) | /\) <(_<) | No | 16.76 |
| 14 | _(/  /()< | _(/  /()\< | No | 11.56 |
| 15 | <\(\(/<(_ |  | No | 47.05 |
| 16 |  ( )\\  < | ( )\\  < | No | 18.14 |
| 17 | (\)_ _/ _ | (\)_ _/ _ | Yes | 16.02 |
| 18 | <()/(((\( |  | No | 24.69 |
| 19 | /((</(_)_ | /((</(_)_ | Yes | 15.05 |
| 20 |  <\_/_<)\ |  | No | 48.61 |
