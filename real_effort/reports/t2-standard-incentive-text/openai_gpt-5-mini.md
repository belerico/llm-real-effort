# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-27 10:41:39

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
| sudoku_game | 5154 | 40960 | 46114 | 0 | 20 | 66.12 | 1322.54 |
| add_numbers | 2900 | 3026 | 5926 | 20 | 0 | 5.54 | 110.7 |
| counting_zeros | 4300 | 38335 | 42635 | 11 | 9 | 34.65 | 692.92 |
| task_decoding | 4240 | 6824 | 11064 | 20 | 0 | 7.20 | 143.93 |
| task_summation | 4580 | 12892 | 17472 | 20 | 0 | 12.09 | 241.75 |
| task_transcription | 3043 | 3127 | 6170 | 20 | 0 | 3.14 | 62.86 |
| task_sequences | 2755 | 11783 | 14538 | 14 | 6 | 17.29 | 345.84 |
| string_entry | 3336 | 36214 | 39550 | 2 | 18 | 31.43 | 628.56 |
| **TOTAL** | **30308** | **153161** | **183469** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 4 3 6 5 1 3 5 5 2 1 6 3 |  | No | 57.52 |
| 2 | 5 4 3 2 1 4 6 1 3 5 4 2 1 6 |  | No | 73.34 |
| 3 | 4 2 1 5 5 6 6 1 2 5 1 4 2 5 |  | No | 70.97 |
| 4 | 6 4 1 3 2 3 1 6 4 2 5 4 3 5 |  | No | 64.62 |
| 5 | 3 5 5 2 6 3 1 1 4 5 2 1 1 3 |  | No | 60.65 |
| 6 | 1 4 6 2 3 2 1 2 5 2 3 5 5 3 |  | No | 61.17 |
| 7 | 4 1 6 5 4 4 5 1 4 5 3 6 6 3 |  | No | 61.47 |
| 8 | 3 6 2 5 3 1 2 5 4 3 5 1 2 5 |  | No | 52.75 |
| 9 | 5 6 6 1 2 5 4 5 6 6 3 1 4 3 |  | No | 67.16 |
| 10 | 2 2 1 3 2 4 1 1 5 3 6 1 5 2 |  | No | 63.19 |
| 11 | 4 1 5 1 6 5 3 4 5 5 6 3 2 1 |  | No | 68.12 |
| 12 | 3 1 4 5 6 4 6 4 1 3 4 2 4 1 |  | No | 60.27 |
| 13 | 6 2 3 3 5 1 5 1 2 4 5 2 6 3 |  | No | 62.55 |
| 14 | 2 4 6 2 3 5 6 5 4 6 5 5 6 1 |  | No | 67.89 |
| 15 | 4 1 3 5 2 4 5 4 6 1 5 5 2 6 |  | No | 44.86 |
| 16 | 1 2 4 3 1 1 2 5 2 5 4 1 5 2 |  | No | 78.93 |
| 17 | 4 2 6 4 3 1 2 5 1 4 2 5 1 6 |  | No | 59.46 |
| 18 | 5 6 6 3 4 5 1 2 6 5 2 5 4 1 |  | No | 84.16 |
| 19 | 3 4 1 2 2 5 2 4 4 3 4 3 5 1 |  | No | 78.99 |
| 20 | 4 3 3 2 6 4 3 5 1 2 4 1 4 2 |  | No | 84.43 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1436 | 1436 | Yes | 4.29 |
| 2 | 1806 | 1806 | Yes | 4.76 |
| 3 | 2133 | 2133 | Yes | 3.53 |
| 4 | 1478 | 1478 | Yes | 6.1 |
| 5 | 1460 | 1460 | Yes | 5.53 |
| 6 | 1988 | 1988 | Yes | 7.25 |
| 7 | 940 | 940 | Yes | 4.06 |
| 8 | 2261 | 2261 | Yes | 7.35 |
| 9 | 2103 | 2103 | Yes | 3.19 |
| 10 | 994 | 994 | Yes | 6.15 |
| 11 | 1537 | 1537 | Yes | 6.11 |
| 12 | 1908 | 1908 | Yes | 3.48 |
| 13 | 2120 | 2120 | Yes | 5.88 |
| 14 | 1149 | 1149 | Yes | 7.79 |
| 15 | 1546 | 1546 | Yes | 5.69 |
| 16 | 1269 | 1269 | Yes | 6.14 |
| 17 | 1967 | 1967 | Yes | 5.68 |
| 18 | 1825 | 1825 | Yes | 8.02 |
| 19 | 2030 | 2030 | Yes | 3.04 |
| 20 | 1483 | 1483 | Yes | 6.67 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 |  | No | 59.76 |
| 2 | 69 | 69 | Yes | 38.53 |
| 3 | 66 |  | No | 64.63 |
| 4 | 55 |  | No | 61.71 |
| 5 | 68 |  | No | 49.98 |
| 6 | 39 | 39 | Yes | 18.71 |
| 7 | 54 | 54 | Yes | 28.4 |
| 8 | 56 |  | No | 41.18 |
| 9 | 67 | 67 | Yes | 19.21 |
| 10 | 70 | 70 | Yes | 19.55 |
| 11 | 57 | 57 | Yes | 24.32 |
| 12 | 51 | 51 | Yes | 22.87 |
| 13 | 60 |  | No | 41.09 |
| 14 | 36 | 36 | Yes | 20.65 |
| 15 | 40 |  | No | 37.33 |
| 16 | 60 | 60 | Yes | 22.47 |
| 17 | 43 | 43 | Yes | 21.69 |
| 18 | 42 | 42 | Yes | 19.36 |
| 19 | 43 |  | No | 42.7 |
| 20 | 50 |  | No | 38.78 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TLBUSAP | TLBUSAP | Yes | 10.36 |
| 2 | MIQKJSF | MIQKJSF | Yes | 7.36 |
| 3 | QXOBDUM | QXOBDUM | Yes | 6.51 |
| 4 | MAXTWCZ | MAXTWCZ | Yes | 7.18 |
| 5 | CEQUZLP | CEQUZLP | Yes | 9.34 |
| 6 | OZDYPGV | OZDYPGV | Yes | 5.45 |
| 7 | ZLAXTJP | ZLAXTJP | Yes | 9.68 |
| 8 | GIRUVWS | GIRUVWS | Yes | 8.93 |
| 9 | KLRBWNV | KLRBWNV | Yes | 6.66 |
| 10 | UKBTLMG | UKBTLMG | Yes | 6.88 |
| 11 | TFCEIRU | TFCEIRU | Yes | 10.03 |
| 12 | XKFTJAW | XKFTJAW | Yes | 3.64 |
| 13 | GDKJQRU | GDKJQRU | Yes | 5.7 |
| 14 | WUFBOGR | WUFBOGR | Yes | 7.73 |
| 15 | ONZXAMJ | ONZXAMJ | Yes | 7.35 |
| 16 | WOQUDHI | WOQUDHI | Yes | 5.28 |
| 17 | MXJKSTH | MXJKSTH | Yes | 3.66 |
| 18 | TYRGNWP | TYRGNWP | Yes | 11.99 |
| 19 | WLYKOPZ | WLYKOPZ | Yes | 6.38 |
| 20 | NOVDQLP | NOVDQLP | Yes | 3.81 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.9, 7.1] | 7.1 2.9 | Yes | 9.63 |
| 2 | [3.2, 6.8] | 3.2 6.8 | Yes | 12.23 |
| 3 | [2.4, 7.6] | 2.4 7.6 | Yes | 8.39 |
| 4 | [4.8, 5.2] | 4.8 5.2 | Yes | 7.17 |
| 5 | [0.5, 9.5] | 0.5 9.5 | Yes | 9.45 |
| 6 | [1.0, 9.0] | 1.0 9.0 | Yes | 10.57 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 10.23 |
| 8 | [3.0, 7.0] | 3.0 7.0 | Yes | 13.88 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 13.45 |
| 10 | [4.5, 5.5] | 4.5 5.5 | Yes | 12.87 |
| 11 | [2.6, 7.4] | 7.4 2.6 | Yes | 13.97 |
| 12 | [2.8, 7.2] | 2.8 7.2 | Yes | 9.63 |
| 13 | [1.5, 8.5] | 8.5 1.5 | Yes | 15.39 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 15.93 |
| 15 | [4.1, 5.9] | 5.9 4.1 | Yes | 10.56 |
| 16 | [1.1, 8.9] | 8.9 1.1 | Yes | 19.15 |
| 17 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.56 |
| 18 | [4.7, 5.3] | 4.7 5.3 | Yes | 12.47 |
| 19 | [3.3, 6.7] | 6.7 3.3 | Yes | 15.65 |
| 20 | [2.1, 7.9] | 7.9 2.1 | Yes | 11.56 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | O4MNV3KZU4M9 | O4MNV3KZU4M9 | Yes | 2.36 |
| 2 | HE84152VIDWD | HE84152VIDWD | Yes | 4.51 |
| 3 | XGKY5TULZ2XG | XGKY5TULZ2XG | Yes | 1.83 |
| 4 | Q7XD603TAVWA | Q7XD603TAVWA | Yes | 2.2 |
| 5 | H7P9NRMV7GEU | H7P9NRMV7GEU | Yes | 1.71 |
| 6 | FL0MJ831QS8K | FL0MJ831QS8K | Yes | 5.02 |
| 7 | VV5KGZYRV4HL | VV5KGZYRV4HL | Yes | 4.66 |
| 8 | TGVNSBY9R4YX | TGVNSBY9R4YX | Yes | 1.87 |
| 9 | 50DJD7XGTPK4 | 50DJD7XGTPK4 | Yes | 1.78 |
| 10 | 633F47EF31B1 | 633F47EF31B1 | Yes | 4.93 |
| 11 | P1XUEPJFL6TY | P1XUEPJFL6TY | Yes | 3.45 |
| 12 | QK3K6ITFMGTO | QK3K6ITFMGTO | Yes | 2.25 |
| 13 | WZZ1DFDBBRP5 | WZZ1DFDBBRP5 | Yes | 4.32 |
| 14 | 1ZSVWZC48DA6 | 1ZSVWZC48DA6 | Yes | 2.74 |
| 15 | 6DA3DYRKG7O2 | 6DA3DYRKG7O2 | Yes | 2.63 |
| 16 | O3RIJ3LGEFZ2 | O3RIJ3LGEFZ2 | Yes | 2.73 |
| 17 | KGEG37V581Q1 | KGEG37V581Q1 | Yes | 5.28 |
| 18 | 2CDHNIFU48ML | 2CDHNIFU48ML | Yes | 2.97 |
| 19 | F4YTRIJWUAQB | F4YTRIJWUAQB | Yes | 2.13 |
| 20 | JGA0BLRYB4GL | JGA0BLRYB4GL | Yes | 3.5 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 5.62 |
| 2 | 198 |  | No | 54.09 |
| 3 | 20 | 42 | No | 4.05 |
| 4 | 60 | 42 | No | 4.55 |
| 5 | 793 | 793 | Yes | 5.01 |
| 6 | 1 | 1 | Yes | 11.1 |
| 7 | 5 | 5 | Yes | 12.22 |
| 8 | 3 | 3 | Yes | 8.05 |
| 9 | 7 | 7 | Yes | 14.28 |
| 10 | 5 | 42 | No | 11.05 |
| 11 | 6 | 6 | Yes | 9.96 |
| 12 | 63 | 63 | Yes | 16.05 |
| 13 | 1440 | 1440 | Yes | 3.9 |
| 14 | 3 | 3 | Yes | 14.56 |
| 15 | 48 | 48 | Yes | 19.41 |
| 16 | 39 | 42 | No | 4.24 |
| 17 | 23 | 23 | Yes | 13.63 |
| 18 | 67 | 67 | Yes | 4.93 |
| 19 | 16 | TIMEOUT | No | 120.03 |
| 20 | 73 | 73 | Yes | 9.1 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \_< <\(<( |  | No | 54.29 |
| 2 | _/<_\/(\) | _/<_\/(\) | Yes | 16.03 |
| 3 | )(/)))_<( | /\) <(_<) | No | 24.69 |
| 4 | _/(\<)((\ | /\) <(_<) | No | 15.03 |
| 5 | )\_\/<\</ | /\) <(_<) | No | 26.5 |
| 6 | _))((<<)/ | /\) <(_<) | No | 20.05 |
| 7 | </_(/\((/ |  | No | 61.86 |
| 8 | \))(<)\\_ |  | No | 28.17 |
| 9 | <//)<<\<\ | /\) <(_<) | No | 18.91 |
| 10 |  \/ \<_ _ |  | No | 38.75 |
| 11 | )()))_(\_ |  | No | 59.68 |
| 12 | )<\) _/ ) | /\) <(_<) | No | 20.28 |
| 13 |  <_\ ()(/ |  | No | 26.25 |
| 14 | _</ _(</  |  | No | 54.83 |
| 15 | _(////)_) | /\) <(_<) | No | 15.1 |
| 16 |  (_<_<_ < |  | No | 34.06 |
| 17 | /(\/  \\/ | /(\/  \/ | Yes | 23.5 |
| 18 | \_\(</_(\ | /\) <(_<) | No | 19.72 |
| 19 | )(_)()\\  |  | No | 30.71 |
| 20 | <\((   () |  | No | 40.14 |
