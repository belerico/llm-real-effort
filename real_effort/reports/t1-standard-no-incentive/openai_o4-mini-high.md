# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-19 03:19:02

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8113 | 38912 | 47025 | 0 | 20 | 44.95 | 899.29 |
| add_numbers | 4060 | 4261 | 8321 | 20 | 0 | 4.56 | 91.38 |
| counting_zeros | 7480 | 40960 | 48440 | 0 | 20 | 33.85 | 677.25 |
| task_decoding | 15520 | 26167 | 41687 | 18 | 2 | 15.52 | 310.66 |
| task_summation | 8740 | 18113 | 26853 | 20 | 0 | 11.41 | 228.47 |
| task_transcription | 3740 | 6780 | 10520 | 15 | 5 | 4.81 | 96.37 |
| task_sequences | 2720 | 11696 | 14416 | 18 | 2 | 10.13 | 202.64 |
| **TOTAL** | **50373** | **146889** | **197262** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 1 2 6 3 1 5 6 1 5 4 6 2 |  | No | 55.78 |
| 2 | 6 4 5 2 5 6 4 2 5 6 4 3 1 6 |  | No | 40.1 |
| 3 | 1 5 2 1 1 5 4 6 4 6 3 3 2 4 |  | No | 35.19 |
| 4 | 5 2 1 1 5 3 4 6 1 6 5 2 2 6 |  | No | 52.38 |
| 5 | 2 1 5 5 4 1 2 1 5 5 1 4 1 6 |  | No | 46.18 |
| 6 | 5 1 6 4 2 5 2 5 2 1 4 5 3 6 | TIMEOUT | No | 120.03 |
| 7 | 4 1 2 2 5 3 2 5 1 2 3 1 4 6 |  | No | 57.17 |
| 8 | 5 3 2 6 2 6 6 4 6 5 4 5 3 1 |  | No | 20.57 |
| 9 | 3 1 2 2 4 6 3 5 6 5 6 1 6 3 |  | No | 53.77 |
| 10 | 3 1 5 4 2 2 6 1 5 6 3 5 5 6 |  | No | 48.98 |
| 11 | 4 5 1 1 2 6 5 1 5 5 2 1 1 5 |  | No | 32.28 |
| 12 | 6 3 1 2 3 5 2 1 1 5 1 4 2 3 |  | No | 44.51 |
| 13 | 1 2 3 6 4 5 6 2 6 2 5 1 5 3 |  | No | 40.49 |
| 14 | 4 6 5 2 6 5 4 4 2 2 6 3 2 4 |  | No | 38.01 |
| 15 | 5 6 4 6 3 2 5 4 5 6 2 2 1 4 |  | No | 33.22 |
| 16 | 4 2 2 4 4 6 3 5 1 4 6 1 4 3 |  | No | 39.97 |
| 17 | 5 3 1 3 4 1 6 1 6 5 3 4 2 6 |  | No | 39.82 |
| 18 | 5 3 6 1 2 6 4 2 2 3 5 4 2 5 |  | No | 44.1 |
| 19 | 5 4 5 6 5 1 4 2 4 3 2 1 1 5 |  | No | 37.64 |
| 20 | 3 5 3 3 5 4 6 1 2 3 3 2 5 1 |  | No | 18.88 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1914 | 1914 | Yes | 2.71 |
| 2 | 2131 | 2131 | Yes | 2.91 |
| 3 | 2639 | 2639 | Yes | 7.88 |
| 4 | 2091 | 2091 | Yes | 3.99 |
| 5 | 1921 | 1921 | Yes | 3.36 |
| 6 | 1570 | 1570 | Yes | 3.78 |
| 7 | 2244 | 2244 | Yes | 5.53 |
| 8 | 1962 | 1962 | Yes | 5.45 |
| 9 | 1763 | 1763 | Yes | 5.45 |
| 10 | 1701 | 1701 | Yes | 3.11 |
| 11 | 886 | 886 | Yes | 3.08 |
| 12 | 1095 | 1095 | Yes | 2.72 |
| 13 | 1335 | 1335 | Yes | 5.3 |
| 14 | 559 | 559 | Yes | 4.08 |
| 15 | 2152 | 2152 | Yes | 5.01 |
| 16 | 1588 | 1588 | Yes | 8.28 |
| 17 | 1206 | 1206 | Yes | 5.01 |
| 18 | 1168 | 1168 | Yes | 2.15 |
| 19 | 2369 | 2369 | Yes | 3.69 |
| 20 | 2546 | 2546 | Yes | 7.78 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 43 |  | No | 43.1 |
| 2 | 38 |  | No | 27.25 |
| 3 | 73 |  | No | 19.79 |
| 4 | 47 |  | No | 45.38 |
| 5 | 68 |  | No | 44.93 |
| 6 | 45 |  | No | 24.01 |
| 7 | 44 |  | No | 19.96 |
| 8 | 42 |  | No | 33.1 |
| 9 | 61 |  | No | 19.17 |
| 10 | 63 |  | No | 21.47 |
| 11 | 59 |  | No | 25.53 |
| 12 | 68 |  | No | 40.58 |
| 13 | 46 |  | No | 40.65 |
| 14 | 48 |  | No | 32.96 |
| 15 | 43 |  | No | 33.96 |
| 16 | 44 |  | No | 26.52 |
| 17 | 64 |  | No | 52.58 |
| 18 | 39 |  | No | 41.42 |
| 19 | 71 |  | No | 63.2 |
| 20 | 69 |  | No | 21.35 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NCIGSBX | NCIGSBX | Yes | 9.68 |
| 2 | EBHIFJT | EBHIFJT | Yes | 13.18 |
| 3 | EMNCLRY | EMNCLRY | Yes | 17.99 |
| 4 | YRSPOXL | YRSPOXL | Yes | 13.64 |
| 5 | MVUAQNP | MVUAQNP | Yes | 8.32 |
| 6 | PZAUEJX | PZAUEJX | Yes | 9.77 |
| 7 | YXIKFJB | YXIKFJB | Yes | 12.38 |
| 8 | OEVKSIN | OEVKSIN | Yes | 14.78 |
| 9 | ZHUYEDX |  | No | 43.69 |
| 10 | LZFQDAY | LZFQDAY | Yes | 11.74 |
| 11 | MNXQJUF | MNXQJUF | Yes | 8.37 |
| 12 | VHTNJYU | VHTNJYU | Yes | 17.1 |
| 13 | OCSTAUP | OCSTAUP | Yes | 17.01 |
| 14 | XLWKADZ |  | No | 34.02 |
| 15 | OGNPMTI | OGNPMTI | Yes | 18.26 |
| 16 | TYOFIGR | TYOFIGR | Yes | 13.62 |
| 17 | QOTHSVP | QOTHSVP | Yes | 14.83 |
| 18 | XVIKUGT | XVIKUGT | Yes | 8.12 |
| 19 | MJCEPHD | MJCEPHD | Yes | 8.43 |
| 20 | UYFLVXD | UYFLVXD | Yes | 15.52 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 3.9 6.1 | Yes | 11.35 |
| 2 | [2.0, 8.0] | 2.0 8.0 | Yes | 9.83 |
| 3 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.99 |
| 4 | [4.8, 5.2] | 4.8 5.2 | Yes | 11.95 |
| 5 | [3.8, 6.2] | 3.8 6.2 | Yes | 14.55 |
| 6 | [3.6, 6.4] | 3.6 6.4 | Yes | 14.54 |
| 7 | [2.2, 7.8] | 2.2 7.8 | Yes | 13.83 |
| 8 | [4.3, 5.7] | 4.3 5.7 | Yes | 9.79 |
| 9 | [0.7, 9.3] | 0.7 9.3 | Yes | 11.27 |
| 10 | [0.6, 9.4] | 9.4 0.6 | Yes | 9.37 |
| 11 | [4.3, 5.7] | 4.3 5.7 | Yes | 11.66 |
| 12 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.8 |
| 13 | [3.4, 6.6] | 3.4 6.6 | Yes | 9.44 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 12.6 |
| 15 | [2.5, 7.5] | 2.5 7.5 | Yes | 12.96 |
| 16 | [1.1, 8.9] | 1.1 8.9 | Yes | 14.87 |
| 17 | [1.0, 9.0] | 1.0 9.0 | Yes | 10.4 |
| 18 | [4.1, 5.9] | 4.1 5.9 | Yes | 12.27 |
| 19 | [2.9, 7.1] | 7.1 2.9 | Yes | 12.49 |
| 20 | [4.0, 6.0] | 4.0 6.0 | Yes | 9.33 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | UEVUD3SVBRFN | UEVUD3SVBRFN | Yes | 3.04 |
| 2 | L0XDN2QU91L8 | L0XDN2QU91L8 | Yes | 4.49 |
| 3 | U9QAO5XZ2YMK | U9QAD5XZ2YMK | No | 3.63 |
| 4 | T4GADXJDT1HF | T4GADXJDT1HF | Yes | 3.57 |
| 5 | CA5OU4I5R5PQ | CA5OU4I5R5PQ | Yes | 10.25 |
| 6 | VKP7IDIH6F0N | VKP7IDIH6F0N | Yes | 3.67 |
| 7 | ZRIHI0IRSGE6 | ZRIHIOIRSGE6 | No | 12.41 |
| 8 | KR7DKMEXQCDF | KR7DKMEXQCDF | Yes | 4.19 |
| 9 | XZG8ASEZFACD | XZG8ASEZFACD | Yes | 2.27 |
| 10 | 5R2SNISSGGKC | 5R2SNISSGGKC | Yes | 7.35 |
| 11 | VE0KRJMXSMPM | VEOKRJMXSMPM | No | 3.05 |
| 12 | 38YZ5N29AQJS | 38YZ5N29AQJS | Yes | 3.78 |
| 13 | Q6AN2WIUBN08 | Q6AN2WIUEN08 | No | 5.77 |
| 14 | SLNOH6KYU422 | SLNOH6KYU422 | Yes | 2.23 |
| 15 | B8PJF67RYMDJ | B8PJF67RYMDJ | Yes | 2.87 |
| 16 | 8WDHO23GTA0M | 8WDHO23GTA0M | Yes | 11.08 |
| 17 | 14X7UPA11RE6 | 14X7UPA11RE6 | Yes | 3.35 |
| 18 | 5M3QK8S8IFA5 | 5M3QK8S8IFA5 | Yes | 3.62 |
| 19 | TPDGP31M390E | TPDGP31M390E | Yes | 2.75 |
| 20 | HVIA5S6EPCCF | HVIA5S6SEPCCF | No | 2.87 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 5.48 |
| 2 | 4 | 4 | Yes | 8.06 |
| 3 | 4 | 4 | Yes | 2.33 |
| 4 | 67 | 67 | Yes | 7.16 |
| 5 | 198 | 198 | Yes | 7.31 |
| 6 | 3 |  | No | 37.74 |
| 7 | 793 | 793 | Yes | 5.73 |
| 8 | 20 | 20 | Yes | 13.86 |
| 9 | 39 | 39 | Yes | 12.04 |
| 10 | 5 | 5 | Yes | 3.19 |
| 11 | 64 |  | No | 32.15 |
| 12 | 36 | 36 | Yes | 1.92 |
| 13 | 10 | 10 | Yes | 16.32 |
| 14 | 1 | 1 | Yes | 11.2 |
| 15 | 9 | 9 | Yes | 3.28 |
| 16 | 7 | 7 | Yes | 5.37 |
| 17 | 65 | 65 | Yes | 5.92 |
| 18 | 3 | 3 | Yes | 9.85 |
| 19 | 44 | 44 | Yes | 11.17 |
| 20 | 243 | 243 | Yes | 2.55 |
