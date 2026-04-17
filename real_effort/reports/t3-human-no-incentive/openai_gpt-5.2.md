# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 7360 | 23935 | 31295 | 17 | 3 | 22.97 | 459.5 |
| add_numbers | 3940 | 933 | 4873 | 20 | 0 | 3.74 | 74.82 |
| counting_zeros | 6360 | 38696 | 45056 | 4 | 16 | 64.96 | 1299.59 |
| task_decoding | 12100 | 3735 | 15835 | 20 | 0 | 5.79 | 116.1 |
| task_summation | 7300 | 5267 | 12567 | 20 | 0 | 6.40 | 128.15 |
| task_transcription | 3770 | 2279 | 6049 | 7 | 13 | 3.59 | 71.96 |
| task_sequences | 3061 | 5045 | 8106 | 19 | 1 | 6.94 | 138.82 |
| **TOTAL** | **43891** | **79890** | **123781** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 1 2 2 1 3 6 4 5 3 5 2 3 |  | No | 39.32 |
| 2 | 3 5 1 5 4 2 1 4 5 6 2 4 6 3 |  | No | 60.51 |
| 3 | 3 6 1 2 2 1 5 4 5 6 2 5 5 2 | 3 6 1 2 2 1 5 4 5 6 2 5 5 2 | Yes | 17.23 |
| 4 | 2 3 1 4 2 5 4 2 6 1 5 6 2 1 | 2 3 1 4 2 5 4 2 6 1 5 6 2 1 | Yes | 16.18 |
| 5 | 5 3 2 4 2 3 5 2 4 6 4 1 6 5 | 5 3 2 4 2 3 5 2 4 6 4 1 6 5 | Yes | 13.31 |
| 6 | 5 3 6 2 5 4 3 1 4 2 5 3 6 1 | 5 3 6 2 5 4 3 1 4 2 5 3 6 1 | Yes | 19.61 |
| 7 | 1 5 1 5 4 3 2 6 4 5 2 3 1 4 | 1 5 1 5 4 3 2 6 4 5 2 3 1 4 | Yes | 18.29 |
| 8 | 2 1 5 2 6 4 2 1 2 3 5 3 1 6 | 2 1 5 2 6 4 2 1 2 3 5 3 1 6 | Yes | 15.22 |
| 9 | 4 5 3 2 5 4 4 5 6 3 2 6 2 4 | 4 5 3 2 5 4 4 5 6 3 2 6 2 4 | Yes | 18.14 |
| 10 | 5 3 4 3 6 5 3 2 2 4 1 1 5 6 | 5 3 4 3 6 5 3 2 2 4 1 1 5 6 | Yes | 17.4 |
| 11 | 2 4 3 4 3 2 5 4 1 6 4 1 2 3 | 2 4 3 4 3 2 5 4 1 6 4 1 2 3 | Yes | 19.33 |
| 12 | 1 1 6 3 1 3 4 6 2 4 1 1 6 3 | 1 1 6 3 1 3 4 6 2 4 1 1 6 3 | Yes | 17.89 |
| 13 | 3 6 2 4 3 2 1 5 4 3 6 2 3 2 | 3 6 2 4 3 2 1 5 4 3 6 2 3 2 | Yes | 21.52 |
| 14 | 6 1 3 4 1 2 5 3 2 6 1 5 2 6 | 6 1 3 4 1 2 5 3 2 6 1 5 2 6 | Yes | 26.75 |
| 15 | 4 2 5 6 1 4 6 3 6 5 5 3 4 2 | 4 2 5 6 1 4 6 3 6 5 5 3 4 2 | Yes | 16.45 |
| 16 | 3 5 6 1 1 4 6 2 3 6 1 5 4 5 | 3 5 6 1 1 4 6 2 3 6 1 5 4 5 | Yes | 18.92 |
| 17 | 6 6 3 1 5 6 1 4 6 3 2 4 3 1 | 6 6 3 1 5 6 1 4 6 3 2 4 3 1 | Yes | 18.53 |
| 18 | 4 2 3 6 4 3 4 6 2 1 2 5 6 4 |  | No | 48.1 |
| 19 | 4 3 6 2 5 4 2 4 3 1 6 5 1 1 | 4 3 6 2 5 4 2 4 3 1 6 5 1 1 | Yes | 18.45 |
| 20 | 6 2 4 1 1 5 2 6 1 1 4 3 4 3 | 6 2 4 1 1 5 2 6 1 1 4 3 4 3 | Yes | 18.17 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1084 | 1084 | Yes | 3.6 |
| 2 | 1195 | 1195 | Yes | 3.52 |
| 3 | 1813 | 1813 | Yes | 4.25 |
| 4 | 1557 | 1557 | Yes | 4.74 |
| 5 | 967 | 967 | Yes | 4.28 |
| 6 | 1133 | 1133 | Yes | 3.93 |
| 7 | 1581 | 1581 | Yes | 2.93 |
| 8 | 1470 | 1470 | Yes | 3.42 |
| 9 | 1130 | 1130 | Yes | 3.55 |
| 10 | 2037 | 2037 | Yes | 4.34 |
| 11 | 1286 | 1286 | Yes | 3.19 |
| 12 | 1773 | 1773 | Yes | 3.44 |
| 13 | 2196 | 2196 | Yes | 3.38 |
| 14 | 1791 | 1791 | Yes | 3.3 |
| 15 | 1431 | 1431 | Yes | 4.09 |
| 16 | 1219 | 1219 | Yes | 3.91 |
| 17 | 1719 | 1719 | Yes | 4.76 |
| 18 | 2011 | 2011 | Yes | 2.94 |
| 19 | 1259 | 1259 | Yes | 3.2 |
| 20 | 1692 | 1692 | Yes | 3.95 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 59.2 |
| 2 | 58 | 58 | Yes | 19.26 |
| 3 | 75 | 75 | Yes | 21.29 |
| 4 | 63 |  | No | 74.21 |
| 5 | 45 |  | No | 79.04 |
| 6 | 54 |  | No | 75.56 |
| 7 | 66 |  | No | 68.87 |
| 8 | 60 |  | No | 63.95 |
| 9 | 74 |  | No | 90.47 |
| 10 | 37 |  | No | 81.5 |
| 11 | 74 | 74 | Yes | 28.18 |
| 12 | 62 |  | No | 111.69 |
| 13 | 47 | 47 | Yes | 31.24 |
| 14 | 43 |  | No | 83.53 |
| 15 | 58 |  | No | 69.29 |
| 16 | 48 |  | No | 72.52 |
| 17 | 47 |  | No | 66.08 |
| 18 | 35 |  | No | 71.23 |
| 19 | 35 |  | No | 75.54 |
| 20 | 37 |  | No | 56.59 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IEOHQND | IEOHQND | Yes | 5.26 |
| 2 | VXBZWGH | VXBZWGH | Yes | 7.76 |
| 3 | NHYBAEU | NHYBAEU | Yes | 6.05 |
| 4 | IUPGVYH | IUPGVYH | Yes | 5.79 |
| 5 | MFXYHBT | MFXYHBT | Yes | 5.18 |
| 6 | OURIPLQ | OURIPLQ | Yes | 9.07 |
| 7 | COHFSRB | COHFSRB | Yes | 5.07 |
| 8 | BIHFSXP | BIHFSXP | Yes | 3.66 |
| 9 | ERXMBGA | ERXMBGA | Yes | 6.13 |
| 10 | ILTGKMC | ILTGKMC | Yes | 6.34 |
| 11 | RVABWOI | RVABWOI | Yes | 5.87 |
| 12 | BLTRDJE | BLTRDJE | Yes | 3.78 |
| 13 | YUZJWCO | YUZJWCO | Yes | 6.12 |
| 14 | TAQVPKJ | TAQVPKJ | Yes | 6.12 |
| 15 | CWTINZF | CWTINZF | Yes | 4.78 |
| 16 | OQRATVD | OQRATVD | Yes | 3.36 |
| 17 | MYKUEBX | MYKUEBX | Yes | 5.81 |
| 18 | ZGIWJRH | ZGIWJRH | Yes | 6.02 |
| 19 | MULZOCT | MULZOCT | Yes | 8.43 |
| 20 | BQSMVUL | BQSMVUL | Yes | 5.26 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 1.8 8.2 | Yes | 6.38 |
| 2 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.11 |
| 3 | [1.2, 8.8] | 8.8 1.2 | Yes | 5.92 |
| 4 | [0.2, 9.8] | 0.2 9.8 | Yes | 4.75 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 7.42 |
| 6 | [1.8, 8.2] | 1.8 8.2 | Yes | 6.97 |
| 7 | [4.7, 5.3] | 4.7 5.3 | Yes | 6.94 |
| 8 | [2.0, 8.0] | 8.0 2.0 | Yes | 5.79 |
| 9 | [2.2, 7.8] | 2.2 7.8 | Yes | 5.93 |
| 10 | [2.2, 7.8] | 2.2 7.8 | Yes | 6.06 |
| 11 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.92 |
| 12 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.5 |
| 13 | [1.8, 8.2] | 8.2 1.8 | Yes | 4.66 |
| 14 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.24 |
| 15 | [3.9, 6.1] | 6.1 3.9 | Yes | 7.35 |
| 16 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.95 |
| 17 | [4.6, 5.4] | 4.6 5.4 | Yes | 5.73 |
| 18 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.32 |
| 19 | [3.4, 6.6] | 3.4 6.6 | Yes | 8.1 |
| 20 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.91 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WA1KXXC4GDMC | WA1KXXC4GDMC | Yes | 4.59 |
| 2 | 9OPNGPINUOSW | Sorry, I can’t help with solving CAPTCHAs or transcribing distorted text used for verification. | No | 1.71 |
| 3 | 76BLP2VS0QDX | 76BLP2VS0QDX | Yes | 3.56 |
| 4 | 0YEQ41JMHDNW | 0YEQ41JMHDNW | Yes | 4.24 |
| 5 | BTH3UMWA0IC2 | I can’t help with transcribing CAPTCHAs. | No | 3.7 |
| 6 | 5E13NI0EN8NY | Sorry, I can’t help with transcribing distorted text from an image like a CAPTCHA. | No | 1.9 |
| 7 | EU5RBKFUBF0X | I can’t help with transcribing CAPTCHAs or other distorted text used to bypass security measures. | No | 6.01 |
| 8 | 4U7DZ7APVOHG | Sorry, I can’t help with solving or transcribing CAPTCHA-style distorted text. | No | 4.88 |
| 9 | V68UNBZ9V79K | V68UNBZ9V79K | Yes | 4.88 |
| 10 | 394NGOZ62DLS | I can’t help transcribe distorted text from an image that appears to be a CAPTCHA. | No | 3.3 |
| 11 | RBEGZ680ADK1 | I can’t help with transcribing CAPTCHA text. | No | 2.99 |
| 12 | GO6ZJNE7LO2F | G06ZJNE7L02F | No | 1.94 |
| 13 | 3VBY4QRU4T4M | 3VBY4QRU4T4M | Yes | 2.96 |
| 14 | PQWN93T5TZX8 | P0WN93T5TZX8 | No | 4.86 |
| 15 | I5DW94WE9YV3 | I5DW94WE9YV3 | Yes | 2.39 |
| 16 | 63ZW6E13MCCA | 63ZW6E13MCCA | Yes | 4.6 |
| 17 | U8O9A631ZE0X | U809A631ZE0X | No | 3.99 |
| 18 | IK1CULSVSVZD | I can’t help with solving CAPTCHAs or transcribing distorted verification text. | No | 3.09 |
| 19 | HBIHRT6B3TE8 | I can’t help with transcribing CAPTCHA-like distorted text. | No | 3.84 |
| 20 | 2WH64HM4XY90 | I can’t help with transcribing CAPTCHA-style distorted text. | No | 2.42 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 4.48 |
| 2 | 198 | 198 | Yes | 4.17 |
| 3 | 73 | 73 | Yes | 4.79 |
| 4 | 3 | 3 | Yes | 6.2 |
| 5 | 5 |  | No | 40.34 |
| 6 | 1440 | 1440 | Yes | 3.99 |
| 7 | 19 | 19 | Yes | 3.34 |
| 8 | 6 | 6 | Yes | 3.01 |
| 9 | 793 | 793 | Yes | 3.63 |
| 10 | 16 | 16 | Yes | 3.93 |
| 11 | 9 | 9 | Yes | 4.9 |
| 12 | 4096 | 4096 | Yes | 23.9 |
| 13 | 10 | 10 | Yes | 4.04 |
| 14 | 64 | 64 | Yes | 5.11 |
| 15 | 60 | 60 | Yes | 3.57 |
| 16 | 63 | 63 | Yes | 3.35 |
| 17 | 7 | 7 | Yes | 3.06 |
| 18 | 26 | 26 | Yes | 5.97 |
| 19 | 28 | 28 | Yes | 3.41 |
| 20 | 5 | 5 | Yes | 3.62 |
