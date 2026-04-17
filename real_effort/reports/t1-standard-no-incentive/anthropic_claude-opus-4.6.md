# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-19 03:19:02

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8380 | 36421 | 44801 | 5 | 15 | 31.64 | 632.9 |
| add_numbers | 4300 | 598 | 4898 | 20 | 0 | 3.39 | 67.8 |
| counting_zeros | 7240 | 21756 | 28996 | 6 | 14 | 13.64 | 273.16 |
| task_decoding | 13680 | 2289 | 15969 | 20 | 0 | 6.12 | 122.63 |
| task_summation | 7600 | 4705 | 12305 | 20 | 0 | 6.44 | 128.92 |
| task_transcription | 4440 | 800 | 5240 | 18 | 2 | 3.86 | 77.35 |
| task_sequences | 3560 | 3975 | 7535 | 19 | 1 | 5.13 | 102.67 |
| **TOTAL** | **49200** | **70544** | **119744** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 5 3 6 4 2 5 1 2 5 2 6 4 | 4 2 5 3 6 4 2 1 2 5 2 6 4 | No | 24.66 |
| 2 | 2 5 4 1 1 2 6 2 4 6 4 2 3 6 | 2 5 4 1 1 2 6 2 4 6 4 2 3 6 | Yes | 22.15 |
| 3 | 3 5 6 1 5 4 6 4 6 2 5 3 6 3 |  | No | 37.67 |
| 4 | 2 3 4 1 5 1 3 1 5 5 5 3 2 6 |  | No | 44.2 |
| 5 | 5 2 4 2 5 1 6 3 2 4 5 1 3 4 |  | No | 38.57 |
| 6 | 3 6 1 3 1 4 2 4 6 5 1 3 1 4 | 3 6 1 3 1 4 2 4 6 5 1 3 1 4At first sight, the title of this article might confuse a number of readers: isn't an API per definition technical? Isn't an API designed for developers primarily, and for them to use in their software? This should indeed make it technical, right? | No | 39.45 |
| 7 | 4 2 5 1 5 6 5 2 6 4 1 5 1 3 | 4 2 5 1 5 6 5 2 6 4 1 5 6 1 3 | No | 24.09 |
| 8 | 2 5 4 5 5 3 6 3 1 5 5 3 4 2 | 2 5 4 5 3 5 3 6 3 1 5 5 3 4 2 | No | 32.0 |
| 9 | 6 5 2 1 3 5 1 3 6 1 2 2 1 3 |  | No | 50.9 |
| 10 | 2 4 1 6 6 1 2 2 5 1 6 5 5 3 |  | No | 35.85 |
| 11 | 5 5 2 1 3 1 2 6 4 3 3 2 3 1 | 5 5 2 1 3 1 2 6 4 3 3 2 3 1 | Yes | 25.14 |
| 12 | 6 4 3 1 5 4 5 6 2 6 4 1 1 2 |  | No | 36.16 |
| 13 | 6 2 3 5 5 6 3 6 2 2 5 1 5 6 |  | No | 35.33 |
| 14 | 1 3 1 5 4 4 1 2 4 5 3 2 5 6 | 1 3 1 5 4 4 1 2 4 5 3 2 5 6 | Yes | 23.29 |
| 15 | 1 3 2 6 4 2 3 2 6 4 3 5 4 1 | 1 3 2 6 4 2 3 6 2 4 3 5 4 1 2 6 | No | 20.56 |
| 16 | 2 1 6 5 5 4 3 5 2 5 1 2 3 6 | 2 1 6 5 5 4 3 5 2 5 1 2 3 6 | Yes | 24.21 |
| 17 | 4 6 4 5 4 2 6 2 4 1 5 2 1 6 | 4 4 6 5 4 2 6 2 4 1 5 2 1 6 | No | 22.48 |
| 18 | 2 5 4 6 2 4 3 1 6 5 2 3 1 2 |  | No | 35.27 |
| 19 | 4 6 1 2 2 1 4 3 5 5 4 6 2 5 | 4 6 1 2 2 1 4 3 5 5 4 6 2 5 | Yes | 24.4 |
| 20 | 3 4 1 6 3 6 3 5 6 5 6 1 6 1 |  | No | 36.32 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1903 | 1903 | Yes | 6.13 |
| 2 | 1811 | 1811 | Yes | 2.67 |
| 3 | 892 | 892 | Yes | 2.85 |
| 4 | 1592 | 1592 | Yes | 2.83 |
| 5 | 2204 | 2204 | Yes | 3.53 |
| 6 | 1883 | 1883 | Yes | 3.58 |
| 7 | 1930 | 1930 | Yes | 3.96 |
| 8 | 1737 | 1737 | Yes | 2.75 |
| 9 | 1154 | 1154 | Yes | 5.3 |
| 10 | 1948 | 1948 | Yes | 2.87 |
| 11 | 1860 | 1860 | Yes | 3.62 |
| 12 | 1846 | 1846 | Yes | 2.66 |
| 13 | 1561 | 1561 | Yes | 2.92 |
| 14 | 1925 | 1925 | Yes | 2.57 |
| 15 | 1500 | 1500 | Yes | 3.7 |
| 16 | 2367 | 2367 | Yes | 3.18 |
| 17 | 1906 | 1906 | Yes | 3.05 |
| 18 | 1810 | 1810 | Yes | 3.27 |
| 19 | 1363 | 1363 | Yes | 3.47 |
| 20 | 1096 | 1096 | Yes | 2.82 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 58 | 57 | No | 12.8 |
| 2 | 73 | 70 | No | 12.9 |
| 3 | 61 | 61 | Yes | 14.44 |
| 4 | 74 | 74 | Yes | 14.98 |
| 5 | 64 | 58 | No | 12.24 |
| 6 | 37 | 37 | Yes | 15.35 |
| 7 | 54 | 52 | No | 12.52 |
| 8 | 45 | 45 | Yes | 14.95 |
| 9 | 53 | 51 | No | 13.45 |
| 10 | 41 | 40 | No | 13.86 |
| 11 | 70 | 69 | No | 12.94 |
| 12 | 44 | 43 | No | 13.48 |
| 13 | 49 | 47 | No | 13.97 |
| 14 | 74 | 67 | No | 12.53 |
| 15 | 70 | 70 | Yes | 14.36 |
| 16 | 72 | 71 | No | 15.16 |
| 17 | 45 | 45 | Yes | 12.43 |
| 18 | 63 | 62 | No | 12.37 |
| 19 | 74 | 70 | No | 13.25 |
| 20 | 70 | 65 | No | 14.87 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FCVAWOG | FCVAWOG | Yes | 8.21 |
| 2 | GVZILHS | GVZILHS | Yes | 15.59 |
| 3 | RSTDAKU | RSTDAKU | Yes | 3.55 |
| 4 | FSXMOKE | FSXMOKE | Yes | 4.52 |
| 5 | BCFWRMG | BCFWRMG | Yes | 6.83 |
| 6 | INVFSGX | INVFSGX | Yes | 5.77 |
| 7 | KPRGVUA | KPRGVUA | Yes | 6.26 |
| 8 | LICUHAX | LICUHAX | Yes | 15.02 |
| 9 | TGEOHBW | TGEOHBW | Yes | 3.79 |
| 10 | MBXSGFY | MBXSGFY | Yes | 4.73 |
| 11 | IZNPJGY | IZNPJGY | Yes | 3.48 |
| 12 | WQASDTE | WQASDTE | Yes | 8.77 |
| 13 | TONQYCA | TONQYCA | Yes | 4.23 |
| 14 | KZRCJSQ | KZRCJSQ | Yes | 6.7 |
| 15 | FAVURHS | FAVURHS | Yes | 3.6 |
| 16 | NYVJRGW | NYVJRGW | Yes | 5.0 |
| 17 | IMSRXZF | IMSRXZF | Yes | 3.48 |
| 18 | CFBVQZU | CFBVQZU | Yes | 3.59 |
| 19 | PKXIVON | PKXIVON | Yes | 3.69 |
| 20 | OMQNJCU | OMQNJCU | Yes | 5.62 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 1.5 8.5 | Yes | 7.4 |
| 2 | [1.9, 8.1] | 1.9 8.1 | Yes | 6.8 |
| 3 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.8 |
| 4 | [3.6, 6.4] | 3.6 6.4 | Yes | 2.67 |
| 5 | [2.2, 7.8] | 2.2 7.8 | Yes | 5.28 |
| 6 | [1.7, 8.3] | 8.3 1.7 | Yes | 7.09 |
| 7 | [4.2, 5.8] | 4.2 5.8 | Yes | 4.17 |
| 8 | [3.4, 6.6] | 6.6 3.4 | Yes | 9.81 |
| 9 | [4.9, 5.1] | 5.1 4.9 | Yes | 7.57 |
| 10 | [0.6, 9.4] | 0.6 9.4 | Yes | 10.14 |
| 11 | [0.1, 9.9] | 0.1 9.9 | Yes | 7.01 |
| 12 | [1.8, 8.2] | 8.2 1.8 | Yes | 6.15 |
| 13 | [3.3, 6.7] | 6.7 3.3 | Yes | 6.11 |
| 14 | [1.2, 8.8] | 1.2 8.8 | Yes | 5.12 |
| 15 | [4.7, 5.3] | 4.7 5.3 | Yes | 8.94 |
| 16 | [0.3, 9.7] | 9.7 0.3 | Yes | 3.11 |
| 17 | [2.6, 7.4] | 2.6 7.4 | Yes | 6.91 |
| 18 | [4.3, 5.7] | 5.7 4.3 | Yes | 4.14 |
| 19 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.72 |
| 20 | [3.1, 6.9] | 3.1 6.9 | Yes | 9.78 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5MWQAJW9IILH | 5MWQAJW9IILH | Yes | 4.2 |
| 2 | 2T3VTJKF5EJN | 2T3VTJKF5EJN | Yes | 3.18 |
| 3 | IV4ZF02T9AGO | IV4ZF02T9AGO | Yes | 4.27 |
| 4 | DD1DSZBY8DIO | DD1DSZBY8DIO | Yes | 3.91 |
| 5 | CIOY2P7TTKKP | CIOY2P7TTKKP | Yes | 3.64 |
| 6 | T3SGFQA6STCR | T3SGFQA6STCR | Yes | 4.12 |
| 7 | 4AUIJ8BWFNBT | 4AUIJ8BWFNBT | Yes | 3.66 |
| 8 | Z3YXGTHLQ0TP | Z3YXGTHLQ0TP | Yes | 5.27 |
| 9 | J94RYA6ZXUV2 | J94RYAGZXUV2 | No | 3.48 |
| 10 | 3RO05MCFPGE6 | 3ROO5MCFPGE6 | No | 3.37 |
| 11 | 84CDFY81KZ35 | 84CDFY81KZ35 | Yes | 3.16 |
| 12 | WPXUCL1VO2XH | WPXUCL1VO2XH | Yes | 4.0 |
| 13 | RG99XRXL6CC0 | RG99XRXL6CC0 | Yes | 3.37 |
| 14 | I9YCA4QCL5P9 | I9YCA4QCL5P9 | Yes | 3.08 |
| 15 | OPGG4ZFWP1LT | OPGG4ZFWP1LT | Yes | 4.28 |
| 16 | 3K8ZW5T829CH | 3K8ZW5T829CH | Yes | 4.02 |
| 17 | XK87IRFTSGZH | XK87IRFTSGZH | Yes | 4.17 |
| 18 | MPKV2OOSR71R | MPKV2OOSR71R | Yes | 5.14 |
| 19 | WHJQK2ZUTUZ5 | WHJQK2ZUTUZ5 | Yes | 3.85 |
| 20 | IAQW76RJEEWV | IAQW76RJEEWV | Yes | 3.08 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 10 | 10 | Yes | 3.01 |
| 2 | 3 | 3 | Yes | 5.75 |
| 3 | 23 | 23 | Yes | 4.48 |
| 4 | 198 | 198 | Yes | 3.99 |
| 5 | 19 | 19 | Yes | 3.2 |
| 6 | 64 | 64 | Yes | 5.54 |
| 7 | 26 | 26 | Yes | 6.78 |
| 8 | 1 | 1 | Yes | 7.14 |
| 9 | 9 | 9 | Yes | 4.24 |
| 10 | 7680 | 7680 | Yes | 4.65 |
| 11 | 67 | 67 | Yes | 2.8 |
| 12 | 44 | 44 | Yes | 4.1 |
| 13 | 793 | 793 | Yes | 3.1 |
| 14 | 5 | 5 | Yes | 5.28 |
| 15 | 31 | 31 | Yes | 3.9 |
| 16 | 36 | 36 | Yes | 2.38 |
| 17 | 60 | 60 | Yes | 5.08 |
| 18 | 5 | 18 | No | 19.87 |
| 19 | 243 | 243 | Yes | 3.09 |
| 20 | 16 | 16 | Yes | 4.31 |
