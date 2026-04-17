# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-26 15:49:28

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
| sudoku_game | 4667 | 21946 | 26613 | 17 | 3 | 22.73 | 454.71 |
| add_numbers | 2420 | 710 | 3130 | 20 | 0 | 3.37 | 67.52 |
| counting_zeros | 3820 | 18222 | 22042 | 19 | 1 | 16.60 | 332.08 |
| task_decoding | 3760 | 2295 | 6055 | 20 | 0 | 5.18 | 103.61 |
| task_summation | 4100 | 3833 | 7933 | 20 | 0 | 5.91 | 118.22 |
| task_transcription | 2561 | 595 | 3156 | 20 | 0 | 1.62 | 32.51 |
| task_sequences | 2178 | 2249 | 4427 | 18 | 2 | 17.29 | 345.86 |
| string_entry | 2866 | 14819 | 17685 | 8 | 12 | 16.48 | 329.68 |
| **TOTAL** | **26372** | **64669** | **91041** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 3 5 6 1 3 4 4 5 6 3 4 6 | 4 1 3 5 6 1 3 4 4 5 6 3 4 6 | Yes | 18.52 |
| 2 | 4 1 4 6 6 1 5 3 4 2 1 4 4 5 | 4 1 4 6 6 1 5 3 4 2 1 4 4 5 | Yes | 13.59 |
| 3 | 2 5 3 3 2 5 4 1 5 2 1 5 6 3 |  | No | 61.0 |
| 4 | 4 3 3 2 6 4 6 4 2 5 6 2 3 2 | 4 3 3 2 6 4 6 4 2 5 6 2 3 2 | Yes | 20.68 |
| 5 | 1 6 2 5 6 3 5 2 3 2 6 6 1 5 |  | No | 61.26 |
| 6 | 2 5 1 3 1 2 3 1 6 3 5 4 2 1 | 2 5 1 3 1 2 3 1 6 3 5 4 2 1 | Yes | 19.81 |
| 7 | 5 4 3 6 2 6 4 6 4 3 6 5 6 4 | 5 4 3 6 2 6 4 6 4 3 6 5 6 4 | Yes | 17.8 |
| 8 | 4 6 1 6 4 1 5 4 2 6 3 5 2 6 | 4 6 1 6 4 1 5 4 2 6 3 5 2 6 | Yes | 11.59 |
| 9 | 6 2 3 1 4 2 6 5 2 4 3 1 6 4 | 6 2 3 1 4 2 6 5 2 4 3 1 6 4 | Yes | 17.64 |
| 10 | 2 3 4 1 1 2 6 3 5 2 5 6 4 3 | 2 3 4 1 1 2 6 3 5 2 5 6 4 3 | Yes | 12.94 |
| 11 | 4 1 3 5 6 4 2 6 6 4 2 5 6 3 | 4 1 3 5 6 4 2 6 6 4 2 5 6 3 | Yes | 9.84 |
| 12 | 5 2 3 1 5 2 4 1 3 2 6 3 5 6 | 5 2 3 1 5 2 4 1 3 2 6 3 5 6 | Yes | 14.01 |
| 13 | 1 3 4 2 6 1 1 2 1 1 4 3 2 5 | 1 3 4 2 6 1 1 2 1 1 4 3 2 5 | Yes | 15.95 |
| 14 | 5 2 5 4 3 2 1 3 5 2 6 6 4 1 |  | No | 54.28 |
| 15 | 5 2 1 6 6 1 1 6 5 4 6 4 5 1 | 5 2 1 6 6 1 1 6 5 4 6 4 5 1 | Yes | 18.84 |
| 16 | 5 1 6 3 4 5 6 3 5 5 1 2 6 3 | 5 1 6 3 4 5 6 3 5 5 1 2 6 3 | Yes | 14.96 |
| 17 | 5 6 4 4 6 3 5 1 6 2 2 5 4 6 | 5 6 4 4 6 3 5 1 6 2 2 5 4 6 | Yes | 20.96 |
| 18 | 1 2 4 3 2 4 5 5 1 6 2 6 4 1 | 1 2 4 3 2 4 5 5 1 6 2 6 4 1 | Yes | 17.35 |
| 19 | 4 5 3 4 1 1 2 4 3 6 3 1 5 6 | 4 5 3 4 1 1 2 4 3 6 3 1 5 6 | Yes | 20.16 |
| 20 | 5 6 2 3 1 6 6 5 2 6 3 6 3 4 | 5 6 2 3 1 6 6 5 2 6 3 6 3 4 | Yes | 13.49 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 879 | 879 | Yes | 3.26 |
| 2 | 1858 | 1858 | Yes | 1.93 |
| 3 | 1336 | 1336 | Yes | 3.63 |
| 4 | 718 | 718 | Yes | 3.17 |
| 5 | 1020 | 1020 | Yes | 3.43 |
| 6 | 1726 | 1726 | Yes | 3.98 |
| 7 | 1982 | 1982 | Yes | 3.41 |
| 8 | 1817 | 1817 | Yes | 3.42 |
| 9 | 1459 | 1459 | Yes | 1.69 |
| 10 | 1857 | 1857 | Yes | 3.1 |
| 11 | 1771 | 1771 | Yes | 3.13 |
| 12 | 1703 | 1703 | Yes | 3.59 |
| 13 | 2831 | 2831 | Yes | 2.62 |
| 14 | 2571 | 2571 | Yes | 3.57 |
| 15 | 1180 | 1180 | Yes | 3.2 |
| 16 | 1372 | 1372 | Yes | 4.01 |
| 17 | 1054 | 1054 | Yes | 3.16 |
| 18 | 2360 | 2360 | Yes | 5.93 |
| 19 | 636 | 636 | Yes | 4.13 |
| 20 | 1099 | 1099 | Yes | 3.13 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 40 | Yes | 11.96 |
| 2 | 67 | 67 | Yes | 14.09 |
| 3 | 46 | 46 | Yes | 12.23 |
| 4 | 65 | 65 | Yes | 20.48 |
| 5 | 56 | 56 | Yes | 13.65 |
| 6 | 40 | 40 | Yes | 20.61 |
| 7 | 56 | 56 | Yes | 17.76 |
| 8 | 64 | 64 | Yes | 13.81 |
| 9 | 35 | 35 | Yes | 12.34 |
| 10 | 61 | 61 | Yes | 20.94 |
| 11 | 62 | 62 | Yes | 19.83 |
| 12 | 41 | 41 | Yes | 15.08 |
| 13 | 74 | 75 | No | 16.46 |
| 14 | 48 | 48 | Yes | 15.12 |
| 15 | 39 | 39 | Yes | 23.91 |
| 16 | 45 | 45 | Yes | 19.37 |
| 17 | 48 | 48 | Yes | 16.52 |
| 18 | 68 | 68 | Yes | 15.15 |
| 19 | 75 | 75 | Yes | 16.56 |
| 20 | 59 | 59 | Yes | 16.18 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NFHGCRV | NFHGCRV | Yes | 7.12 |
| 2 | QCGAXRW | QCGAXRW | Yes | 4.72 |
| 3 | PTCDZFV | PTCDZFV | Yes | 5.68 |
| 4 | HNMVLOJ | HNMVLOJ | Yes | 4.84 |
| 5 | ELMFHCK | ELMFHCK | Yes | 4.98 |
| 6 | BQCPJNM | BQCPJNM | Yes | 5.09 |
| 7 | HTRUCKI | HTRUCKI | Yes | 5.68 |
| 8 | MSLYOBN | MSLYOBN | Yes | 5.52 |
| 9 | UFTDHOG | UFTDHOG | Yes | 5.09 |
| 10 | EWJLHYG | EWJLHYG | Yes | 5.46 |
| 11 | CAEYLUZ | CAEYLUZ | Yes | 4.12 |
| 12 | TPQGVWK | TPQGVWK | Yes | 4.7 |
| 13 | GUCJEKM | GUCJEKM | Yes | 4.25 |
| 14 | CHYELMG | CHYELMG | Yes | 5.06 |
| 15 | XGBUZNS | XGBUZNS | Yes | 5.13 |
| 16 | GQDIKUC | GQDIKUC | Yes | 5.56 |
| 17 | IGBFJLD | IGBFJLD | Yes | 4.99 |
| 18 | XMRAUPI | XMRAUPI | Yes | 5.59 |
| 19 | MOXBAIW | MOXBAIW | Yes | 5.3 |
| 20 | XVELINZ | XVELINZ | Yes | 4.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.6, 7.4] | 2.6 7.4 | Yes | 4.66 |
| 2 | [2.4, 7.6] | 7.6 2.4 | Yes | 6.08 |
| 3 | [3.6, 6.4] | 6.4 3.6 | Yes | 8.06 |
| 4 | [1.5, 8.5] | 1.5 8.5 | Yes | 5.27 |
| 5 | [4.5, 5.5] | 5.5 4.5 | Yes | 6.08 |
| 6 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.71 |
| 7 | [0.6, 9.4] | 0.6 9.4 | Yes | 5.51 |
| 8 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.63 |
| 9 | [3.1, 6.9] | 6.9 3.1 | Yes | 6.91 |
| 10 | [2.7, 7.3] | 2.7 7.3 | Yes | 4.81 |
| 11 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.32 |
| 12 | [2.3, 7.7] | 7.7 2.3 | Yes | 5.13 |
| 13 | [2.9, 7.1] | 2.9 7.1 | Yes | 5.43 |
| 14 | [5.0, 5.0] | 5.0 5.0 | Yes | 6.23 |
| 15 | [0.4, 9.6] | 0.4 9.6 | Yes | 6.22 |
| 16 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.28 |
| 17 | [2.4, 7.6] | 7.6 2.4 | Yes | 4.06 |
| 18 | [0.4, 9.6] | 9.6 0.4 | Yes | 6.45 |
| 19 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.21 |
| 20 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.14 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IJPKLOP6AW8O | IJPKLOP6AW8O | Yes | 1.55 |
| 2 | L9ZHFTJXVBVX | L9ZHFTJXVBVX | Yes | 1.07 |
| 3 | CUBKQEHTYJ45 | CUBKQEHTYJ45 | Yes | 1.01 |
| 4 | GNS1GG278S2L | GNS1GG278S2L | Yes | 0.83 |
| 5 | VPAJXSM9SQSC | VPAJXSM9SQSC | Yes | 0.88 |
| 6 | CMBIMKAVGMWQ | CMBIMKAVGMWQ | Yes | 0.9 |
| 7 | 8CFYC1OY6NVC | 8CFYC1OY6NVC | Yes | 1.6 |
| 8 | OAEKIDY25LGL | OAEKIDY25LGL | Yes | 1.17 |
| 9 | IO0BP23WRVG2 | IO0BP23WRVG2 | Yes | 3.35 |
| 10 | TM90KOBZK6J2 | TM90KOBZK6J2 | Yes | 3.25 |
| 11 | F8XWL5RJ3GF2 | F8XWL5RJ3GF2 | Yes | 1.99 |
| 12 | P8NPRO37FRN5 | P8NPRO37FRN5 | Yes | 1.84 |
| 13 | 3YD61ENJE1OU | 3YD61ENJE1OU | Yes | 3.41 |
| 14 | AA7LKCJVXDHE | AA7LKCJVXDHE | Yes | 1.73 |
| 15 | E747ZQ9K0638 | E747ZQ9K0638 | Yes | 1.04 |
| 16 | 0MHSYQT6ILPU | 0MHSYQT6ILPU | Yes | 1.3 |
| 17 | QUDZQJPA9E7L | QUDZQJPA9E7L | Yes | 1.88 |
| 18 | GHEP6KO7BPWC | GHEP6KO7BPWC | Yes | 1.19 |
| 19 | 6NYRGUGHWLF5 | 6NYRGUGHWLF5 | Yes | 1.39 |
| 20 | P8S25YF1X80Q | P8S25YF1X80Q | Yes | 1.12 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 5.61 |
| 2 | 4 | TIMEOUT | No | 120.02 |
| 3 | 19 | 19 | Yes | 3.57 |
| 4 | 39 | 39 | Yes | 4.79 |
| 5 | 6 | 6 | Yes | 4.48 |
| 6 | 26 | 26 | Yes | 19.6 |
| 7 | 65 | TIMEOUT | No | 120.03 |
| 8 | 31 | 31 | Yes | 3.6 |
| 9 | 793 | 793 | Yes | 3.92 |
| 10 | 23 | 23 | Yes | 5.37 |
| 11 | 1440 | 1440 | Yes | 4.69 |
| 12 | 67 | 67 | Yes | 7.76 |
| 13 | 1 | 1 | Yes | 8.02 |
| 14 | 243 | 243 | Yes | 4.82 |
| 15 | 36 | 36 | Yes | 4.38 |
| 16 | 198 | 198 | Yes | 5.16 |
| 17 | 7680 | 7680 | Yes | 5.23 |
| 18 | 60 | 60 | Yes | 5.95 |
| 19 | 48 | 48 | Yes | 4.01 |
| 20 | 63 | 63 | Yes | 4.83 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (< \))_<  | /\) <(_<) | No | 21.1 |
| 2 | \_<\( /(  | \_<\( /( ) | No | 18.85 |
| 3 | )//(((</) | )//(((</) | Yes | 5.5 |
| 4 | /__\)< )) | /\) <(_<) | No | 14.66 |
| 5 | ) _(()) ( | ) _(()) ( | Yes | 5.43 |
| 6 | \_(/)(_(  |  | No | 51.53 |
| 7 |  )/_ )\</ | /\) <(_<) | No | 10.11 |
| 8 | (<//_)) < | /\) <(_<) | No | 10.61 |
| 9 | /\<)()(\< | /\<)()(\< | Yes | 6.41 |
| 10 | /< _(\(/\ | /< _(\(/\ | Yes | 11.06 |
| 11 |  )/<(_(<  | )/<(_(< | No | 3.14 |
| 12 | \// )( )) | \// )( )) | Yes | 14.86 |
| 13 | / )_) <__ | / )_) <__ | Yes | 11.1 |
| 14 | _)/_)/\(  | _)/_)/\( | No | 11.9 |
| 15 | \<)_ _(_/ | /\) <(_<) | No | 28.82 |
| 16 | / (< <_)( | / (< <_)( | Yes | 7.1 |
| 17 |  )<<<\<_/ |  | No | 59.95 |
| 18 | ((/<\\ /( | ((/<\\ /( | Yes | 7.25 |
| 19 | < ()</<\) | /\) <(_<) | No | 25.09 |
| 20 |   (\__ \< | (\__ \< | No | 5.21 |
