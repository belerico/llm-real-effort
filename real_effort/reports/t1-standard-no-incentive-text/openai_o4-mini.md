# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-27 10:26:04

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
| sudoku_game | 4981 | 40960 | 45941 | 0 | 20 | 39.30 | 786.0 |
| add_numbers | 2720 | 3386 | 6106 | 20 | 0 | 3.58 | 71.53 |
| counting_zeros | 4120 | 40353 | 44473 | 2 | 18 | 30.58 | 611.59 |
| task_decoding | 4060 | 10330 | 14390 | 20 | 0 | 7.25 | 144.95 |
| task_summation | 4400 | 19883 | 24283 | 20 | 0 | 12.41 | 248.17 |
| task_transcription | 2862 | 3000 | 5862 | 20 | 0 | 2.28 | 45.61 |
| task_sequences | 2721 | 12455 | 15176 | 18 | 2 | 9.91 | 198.28 |
| string_entry | 3172 | 36989 | 40161 | 2 | 18 | 26.13 | 522.54 |
| **TOTAL** | **29036** | **167356** | **196392** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 5 1 6 4 1 6 2 5 6 1 5 3 |  | No | 41.86 |
| 2 | 1 6 1 4 2 5 2 3 6 1 1 3 2 4 |  | No | 32.86 |
| 3 | 2 2 5 6 4 4 5 4 6 5 3 1 4 2 |  | No | 47.21 |
| 4 | 5 1 5 4 6 2 5 4 1 5 2 5 2 1 |  | No | 39.91 |
| 5 | 5 4 1 4 1 2 6 2 4 5 1 3 6 5 |  | No | 46.47 |
| 6 | 1 4 5 1 3 5 5 3 2 3 4 2 4 3 |  | No | 48.39 |
| 7 | 4 6 5 1 6 2 4 3 5 1 3 2 6 1 |  | No | 44.46 |
| 8 | 4 3 6 2 3 5 3 1 5 4 4 2 3 3 |  | No | 48.49 |
| 9 | 5 1 2 4 1 5 1 4 4 3 6 4 1 5 |  | No | 49.68 |
| 10 | 2 1 1 4 1 6 4 3 1 1 5 6 2 3 |  | No | 34.43 |
| 11 | 4 3 5 3 6 1 5 6 4 2 6 2 6 4 |  | No | 30.11 |
| 12 | 1 6 3 2 4 1 3 6 3 1 4 1 2 5 |  | No | 27.29 |
| 13 | 1 4 3 5 3 3 1 2 4 3 6 5 2 6 |  | No | 45.6 |
| 14 | 1 4 2 5 4 6 3 2 5 4 3 4 6 3 |  | No | 36.8 |
| 15 | 4 6 2 3 6 2 1 4 3 6 5 4 2 5 |  | No | 35.52 |
| 16 | 4 6 5 2 4 2 6 5 3 4 6 2 1 4 |  | No | 37.1 |
| 17 | 4 2 4 6 1 2 6 4 5 6 2 6 5 1 |  | No | 44.55 |
| 18 | 6 5 5 2 4 1 2 1 5 6 4 4 5 6 |  | No | 40.14 |
| 19 | 6 1 1 6 5 2 3 6 3 3 6 1 5 6 |  | No | 27.51 |
| 20 | 5 1 3 5 1 1 1 4 6 2 1 4 3 5 |  | No | 27.58 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1867 | 1867 | Yes | 2.2 |
| 2 | 1375 | 1375 | Yes | 5.31 |
| 3 | 2422 | 2422 | Yes | 2.82 |
| 4 | 2476 | 2476 | Yes | 5.33 |
| 5 | 1038 | 1038 | Yes | 4.06 |
| 6 | 1336 | 1336 | Yes | 4.66 |
| 7 | 1418 | 1418 | Yes | 2.97 |
| 8 | 2409 | 2409 | Yes | 4.78 |
| 9 | 1896 | 1896 | Yes | 2.09 |
| 10 | 1704 | 1704 | Yes | 2.54 |
| 11 | 955 | 955 | Yes | 2.6 |
| 12 | 1715 | 1715 | Yes | 2.41 |
| 13 | 1313 | 1313 | Yes | 2.59 |
| 14 | 2046 | 2046 | Yes | 4.84 |
| 15 | 1998 | 1998 | Yes | 5.28 |
| 16 | 1524 | 1524 | Yes | 2.22 |
| 17 | 2221 | 2221 | Yes | 2.1 |
| 18 | 2185 | 2185 | Yes | 5.47 |
| 19 | 2066 | 2066 | Yes | 4.77 |
| 20 | 2082 | 2082 | Yes | 2.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 |  | No | 35.84 |
| 2 | 68 |  | No | 22.55 |
| 3 | 66 |  | No | 19.5 |
| 4 | 59 |  | No | 23.27 |
| 5 | 38 |  | No | 27.97 |
| 6 | 58 |  | No | 48.25 |
| 7 | 60 |  | No | 31.99 |
| 8 | 54 |  | No | 49.68 |
| 9 | 40 |  | No | 37.09 |
| 10 | 74 |  | No | 27.76 |
| 11 | 67 |  | No | 54.88 |
| 12 | 71 |  | No | 24.18 |
| 13 | 46 |  | No | 24.64 |
| 14 | 50 |  | No | 18.89 |
| 15 | 65 |  | No | 21.16 |
| 16 | 42 | 42 | Yes | 16.18 |
| 17 | 52 |  | No | 41.04 |
| 18 | 48 |  | No | 28.02 |
| 19 | 58 |  | No | 35.26 |
| 20 | 68 | 68 | Yes | 23.43 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IZMFXQC | IZMFXQC | Yes | 3.42 |
| 2 | DZIKAOT | DZIKAOT | Yes | 8.96 |
| 3 | QLIOMCX | QLIOMCX | Yes | 7.22 |
| 4 | MABPRQW | MABPRQW | Yes | 10.22 |
| 5 | TUGKSVY | TUGKSVY | Yes | 12.34 |
| 6 | DYVFKAQ | DYVFKAQ | Yes | 4.27 |
| 7 | PVONGRQ | PVONGRQ | Yes | 6.99 |
| 8 | LIRQJSW | LIRQJSW | Yes | 5.99 |
| 9 | RNEVDPF | RNEVDPF | Yes | 7.24 |
| 10 | HTDLUOV | HTDLUOV | Yes | 5.33 |
| 11 | NYEORXF | NYEORXF | Yes | 13.41 |
| 12 | JUYSLWK | JUYSLWK | Yes | 4.16 |
| 13 | HMTVQJI | HMTVQJI | Yes | 7.13 |
| 14 | YBPKXTH | YBPKXTH | Yes | 3.39 |
| 15 | PXZYNFL | PXZYNFL | Yes | 5.23 |
| 16 | GYNEHLF | GYNEHLF | Yes | 12.06 |
| 17 | ERLASQF | ERLASQF | Yes | 5.89 |
| 18 | QBZRPID | QBZRPID | Yes | 13.11 |
| 19 | JLMOTHD | JLMOTHD | Yes | 4.32 |
| 20 | CTDXJKP | CTDXJKP | Yes | 4.26 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.1, 9.9] | 9.9 0.1 | Yes | 13.09 |
| 2 | [1.5, 8.5] | 1.5 8.5 | Yes | 16.75 |
| 3 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.69 |
| 4 | [0.6, 9.4] | 0.6 9.4 | Yes | 13.74 |
| 5 | [4.6, 5.4] | 4.6 5.4 | Yes | 13.97 |
| 6 | [5.0, 5.0] | 5.0 5.0 | Yes | 5.22 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 9.39 |
| 8 | [3.7, 6.3] | 3.7 6.3 | Yes | 12.13 |
| 9 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.88 |
| 10 | [2.5, 7.5] | 7.5 2.5 | Yes | 15.84 |
| 11 | [3.9, 6.1] | 3.9 6.1 | Yes | 16.42 |
| 12 | [3.8, 6.2] | 6.2 3.8 | Yes | 14.2 |
| 13 | [4.5, 5.5] | 5.5 4.5 | Yes | 14.81 |
| 14 | [3.2, 6.8] | 3.2 6.8 | Yes | 13.07 |
| 15 | [3.0, 7.0] | 3.0 7.0 | Yes | 9.29 |
| 16 | [1.9, 8.1] | 1.9 8.1 | Yes | 8.95 |
| 17 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.53 |
| 18 | [2.8, 7.2] | 7.2 2.8 | Yes | 13.9 |
| 19 | [1.7, 8.3] | 1.7 8.3 | Yes | 8.21 |
| 20 | [4.6, 5.4] | 4.6 5.4 | Yes | 19.1 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | K5DTG2LWYECS | K5DTG2LWYECS | Yes | 2.67 |
| 2 | O7HFUPZ1CVKK | O7HFUPZ1CVKK | Yes | 2.94 |
| 3 | 3IKT2XTPVB87 | 3IKT2XTPVB87 | Yes | 2.56 |
| 4 | WI4YJ37XXCGH | WI4YJ37XXCGH | Yes | 1.99 |
| 5 | VJR2S39PD420 | VJR2S39PD420 | Yes | 1.59 |
| 6 | TPN74WCHDZXB | TPN74WCHDZXB | Yes | 2.26 |
| 7 | HKHUJAJ5UDCR | HKHUJAJ5UDCR | Yes | 1.58 |
| 8 | ISC7TO9MXB67 | ISC7TO9MXB67 | Yes | 2.82 |
| 9 | CJDFDG45CMY0 | CJDFDG45CMY0 | Yes | 1.87 |
| 10 | XH76AO554I6V | XH76AO554I6V | Yes | 2.22 |
| 11 | T2VLTY3PHYK7 | T2VLTY3PHYK7 | Yes | 1.78 |
| 12 | 0W8MH4NMIUIU | 0W8MH4NMIUIU | Yes | 2.69 |
| 13 | Q7S4O2U48BS4 | Q7S4O2U48BS4 | Yes | 2.32 |
| 14 | AB1X8IU2R1YB | AB1X8IU2R1YB | Yes | 3.19 |
| 15 | LVSKLAURFJ2Q | LVSKLAURFJ2Q | Yes | 2.29 |
| 16 | 6NJ9T6ZEY0JG | 6NJ9T6ZEY0JG | Yes | 1.99 |
| 17 | GQQX8IU5KUDW | GQQX8IU5KUDW | Yes | 2.38 |
| 18 | 4PSD9VGWTHRW | 4PSD9VGWTHRW | Yes | 2.05 |
| 19 | ADQKKU5PU0GG | ADQKKU5PU0GG | Yes | 1.99 |
| 20 | 7GSY16364SPL | 7GSY16364SPL | Yes | 2.43 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 8.54 |
| 2 | 48 | 48 | Yes | 10.62 |
| 3 | 26 | 26 | Yes | 14.74 |
| 4 | 60 | 60 | Yes | 8.96 |
| 5 | 64 | 64 | Yes | 15.76 |
| 6 | 4096 |  | No | 33.05 |
| 7 | 16 | 16 | Yes | 5.63 |
| 8 | 65 | 65 | Yes | 3.06 |
| 9 | 36 | 36 | Yes | 3.12 |
| 10 | 73 | 73 | Yes | 3.68 |
| 11 | 4 | 4 | Yes | 2.77 |
| 12 | 793 | 793 | Yes | 5.2 |
| 13 | 4 | 4 | Yes | 7.74 |
| 14 | 39 |  | No | 48.17 |
| 15 | 7 | 7 | Yes | 2.48 |
| 16 | 3 | 3 | Yes | 5.44 |
| 17 | 60 | 60 | Yes | 2.84 |
| 18 | 28 | 28 | Yes | 8.2 |
| 19 | 7680 | 7680 | Yes | 5.65 |
| 20 | 5 | 5 | Yes | 2.61 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _<\ \/\_  |  | No | 18.76 |
| 2 | /)  _(\ \ | /)  _(\ \ | Yes | 15.56 |
| 3 | \_(<\<<_) | /\) <(_<) | No | 13.93 |
| 4 | (<)   //  |  | No | 44.9 |
| 5 | <<(\ _/)( |  | No | 20.52 |
| 6 |  _<)(<))< |  | No | 22.59 |
| 7 | /(\\__)(_ |  | No | 26.51 |
| 8 | _(  )/( / |  | No | 24.16 |
| 9 | _</</</<( |  | No | 20.73 |
| 10 |  )\_\_<)\ |  | No | 32.39 |
| 11 | _< __\< ( |  | No | 24.95 |
| 12 | (_\)\))/_ |  | No | 39.76 |
| 13 | //<<\ /)) | //<<\ /)) | Yes | 5.43 |
| 14 |  \/ ( /_) |  | No | 23.98 |
| 15 |  _ )</\<) |  | No | 34.71 |
| 16 | )\_<\/ \( | /\) <(_<) | No | 9.83 |
| 17 |   ((<(_ / |  | No | 38.64 |
| 18 | _\<__/\// |  | No | 56.0 |
| 19 | /\\\< ()) |  | No | 34.91 |
| 20 | \\//\ ( _ | /\) <(_<) | No | 14.29 |
