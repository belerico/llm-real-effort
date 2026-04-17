# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 7540 | 24500 | 32040 | 16 | 4 | 25.95 | 519.19 |
| add_numbers | 4120 | 912 | 5032 | 20 | 0 | 4.41 | 88.24 |
| counting_zeros | 6540 | 35542 | 42082 | 7 | 13 | 53.41 | 1068.63 |
| task_decoding | 12280 | 3675 | 15955 | 20 | 0 | 5.49 | 109.94 |
| task_summation | 7480 | 4854 | 12334 | 20 | 0 | 6.18 | 123.69 |
| task_transcription | 3956 | 2297 | 6253 | 4 | 16 | 3.49 | 69.99 |
| task_sequences | 3240 | 4682 | 7922 | 19 | 1 | 7.67 | 153.46 |
| **TOTAL** | **45156** | **76462** | **121618** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 4 2 2 6 4 3 5 4 3 6 6 2 4 | 3 4 2 2 6 4 3 5 4 3 6 6 2 4 | Yes | 20.35 |
| 2 | 6 4 1 4 2 6 2 4 3 5 4 5 2 6 | 6 4 1 4 2 6 2 4 3 5 4 5 2 6 | Yes | 19.47 |
| 3 | 6 4 3 4 6 1 5 2 6 6 4 3 5 4 |  | No | 59.3 |
| 4 | 4 5 1 3 1 2 6 6 5 2 5 6 2 3 | 4 5 1 3 1 6 2 2 5 6 5 2 6 3 | No | 25.17 |
| 5 | 4 4 5 1 3 4 5 3 4 6 5 2 5 2 | 4 4 5 1 3 4 5 3 4 6 5 2 5 2 | Yes | 18.03 |
| 6 | 4 1 2 3 2 1 3 5 3 4 5 4 6 1 | 4 1 2 3 2 1 3 5 3 4 5 4 6 1 | Yes | 16.18 |
| 7 | 6 2 5 1 6 1 2 5 1 4 6 6 3 6 | 6 2 5 1 6 1 2 5 1 4 6 6 3 6 | Yes | 15.6 |
| 8 | 4 3 5 4 5 6 2 4 1 4 2 5 1 3 | 4 3 5 4 5 6 2 4 1 4 2 5 1 3 | Yes | 17.13 |
| 9 | 2 4 1 6 2 5 4 5 2 6 6 3 6 1 | 2 4 1 6 2 5 4 5 2 6 6 3 6 1 | Yes | 24.64 |
| 10 | 1 6 2 3 5 3 4 5 6 4 6 2 1 2 | 1 6 2 3 5 3 4 5 6 4 6 2 1 2 | Yes | 19.51 |
| 11 | 1 5 6 4 6 4 5 1 6 6 3 5 1 2 |  | No | 53.39 |
| 12 | 4 6 5 1 1 4 6 1 6 5 3 6 1 4 | 4 6 5 1 1 4 6 1 6 5 3 6 1 4 | Yes | 16.15 |
| 13 | 2 5 4 2 4 6 3 4 3 2 1 3 4 2 | 2 5 4 2 4 6 3 4 3 2 1 3 4 2 | Yes | 23.89 |
| 14 | 3 6 1 2 6 3 5 3 6 1 5 3 1 1 |  | No | 70.46 |
| 15 | 5 6 1 1 4 2 3 4 4 2 2 3 4 1 | 5 6 1 1 4 2 3 4 4 2 2 3 4 1 | Yes | 19.61 |
| 16 | 1 2 2 3 1 3 2 6 3 2 4 5 2 6 | 1 2 2 3 1 3 2 6 3 2 4 5 2 6 | Yes | 17.38 |
| 17 | 6 2 3 4 6 1 5 6 4 5 6 2 4 3 | 6 2 3 4 6 1 5 6 4 5 6 2 4 3 | Yes | 18.25 |
| 18 | 5 6 3 4 6 3 5 4 1 1 6 3 3 4 | 5 6 3 4 6 3 5 4 1 1 6 3 3 4 | Yes | 21.07 |
| 19 | 1 5 3 2 5 1 4 4 3 5 2 3 6 4 | 1 5 3 2 5 1 4 4 3 5 2 3 6 4 | Yes | 19.6 |
| 20 | 1 5 4 5 4 1 6 2 5 3 1 4 1 3 | 1 5 4 5 4 1 6 2 5 3 1 4 1 3 | Yes | 23.81 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1136 | 1136 | Yes | 4.51 |
| 2 | 2440 | 2440 | Yes | 3.43 |
| 3 | 1816 | 1816 | Yes | 4.7 |
| 4 | 1284 | 1284 | Yes | 5.11 |
| 5 | 1071 | 1071 | Yes | 5.7 |
| 6 | 2358 | 2358 | Yes | 3.99 |
| 7 | 2396 | 2396 | Yes | 3.21 |
| 8 | 2011 | 2011 | Yes | 4.38 |
| 9 | 1074 | 1074 | Yes | 8.01 |
| 10 | 2722 | 2722 | Yes | 3.83 |
| 11 | 1708 | 1708 | Yes | 3.46 |
| 12 | 1316 | 1316 | Yes | 4.1 |
| 13 | 1389 | 1389 | Yes | 5.0 |
| 14 | 2227 | 2227 | Yes | 4.64 |
| 15 | 1878 | 1878 | Yes | 3.52 |
| 16 | 2125 | 2125 | Yes | 4.24 |
| 17 | 1765 | 1765 | Yes | 4.0 |
| 18 | 1830 | 1830 | Yes | 4.12 |
| 19 | 1623 | 1623 | Yes | 3.7 |
| 20 | 2024 | 2024 | Yes | 4.49 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 70 |  | No | 64.2 |
| 2 | 55 |  | No | 104.69 |
| 3 | 42 |  | No | 97.27 |
| 4 | 56 | 56 | Yes | 27.9 |
| 5 | 46 |  | No | 77.39 |
| 6 | 69 |  | No | 95.04 |
| 7 | 67 | 67 | Yes | 23.89 |
| 8 | 63 | 63 | Yes | 26.21 |
| 9 | 40 |  | No | 67.06 |
| 10 | 67 | 67 | Yes | 18.86 |
| 11 | 54 |  | No | 60.27 |
| 12 | 73 |  | No | 68.27 |
| 13 | 67 | 67 | Yes | 21.89 |
| 14 | 69 |  | No | 61.11 |
| 15 | 39 |  | No | 75.77 |
| 16 | 54 | 55 | No | 27.78 |
| 17 | 56 | 56 | Yes | 17.7 |
| 18 | 66 |  | No | 45.55 |
| 19 | 48 | 48 | Yes | 28.31 |
| 20 | 62 |  | No | 59.12 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JPWHVKD | JPWHVKD | Yes | 4.96 |
| 2 | CMSTXFV | CMSTXFV | Yes | 5.33 |
| 3 | HJKZNYQ | HJKZNYQ | Yes | 5.63 |
| 4 | FOMRPDC | FOMRPDC | Yes | 7.21 |
| 5 | TMENGYR | TMENGYR | Yes | 8.7 |
| 6 | RNHGDLU | RNHGDLU | Yes | 5.69 |
| 7 | UFXMGOI | UFXMGOI | Yes | 5.81 |
| 8 | DKZVXFH | DKZVXFH | Yes | 2.69 |
| 9 | GFOTULK | GFOTULK | Yes | 3.32 |
| 10 | HGIDXON | HGIDXON | Yes | 5.71 |
| 11 | PQUMGTA | PQUMGTA | Yes | 5.19 |
| 12 | HVYNJQU | HVYNJQU | Yes | 5.34 |
| 13 | DAVPUJY | DAVPUJY | Yes | 5.71 |
| 14 | MUKQZSB | MUKQZSB | Yes | 5.98 |
| 15 | KEUXHJD | KEUXHJD | Yes | 5.91 |
| 16 | WKEJISX | WKEJISX | Yes | 5.85 |
| 17 | LOYHCRT | LOYHCRT | Yes | 5.0 |
| 18 | UHSJKRM | UHSJKRM | Yes | 4.92 |
| 19 | WFESNGR | WFESNGR | Yes | 5.32 |
| 20 | OXMVFRP | OXMVFRP | Yes | 5.47 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.63 |
| 2 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.54 |
| 3 | [2.6, 7.4] | 2.6 7.4 | Yes | 10.06 |
| 4 | [2.6, 7.4] | 7.4 2.6 | Yes | 4.84 |
| 5 | [4.3, 5.7] | 5.7 4.3 | Yes | 5.75 |
| 6 | [1.2, 8.8] | 8.8 1.2 | Yes | 6.33 |
| 7 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.49 |
| 8 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.07 |
| 9 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.37 |
| 10 | [3.3, 6.7] | 3.3 6.7 | Yes | 6.35 |
| 11 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.18 |
| 12 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.52 |
| 13 | [0.7, 9.3] | 9.3 0.7 | Yes | 6.35 |
| 14 | [5.0, 5.0] | 5.0 5.0 | Yes | 4.86 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.26 |
| 16 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.34 |
| 17 | [3.3, 6.7] | 3.3 6.7 | Yes | 6.48 |
| 18 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.27 |
| 19 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.93 |
| 20 | [2.1, 7.9] | 2.1 7.9 | Yes | 5.89 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KINOYIKW96P4 | KINOYIKW96P4 | Yes | 6.01 |
| 2 | 5KJKNQ9HAC9K | Sorry, I can’t help with transcribing CAPTCHA-like distorted verification text. | No | 2.0 |
| 3 | E1ZDNPZQ8MRO | E1ZDNPZQ8MRO | Yes | 5.24 |
| 4 | XYQVXYTTW08X | I can’t help with transcribing or solving CAPTCHA-style distorted text. | No | 2.73 |
| 5 | 4SO4TKUJ163U | Sorry, I can’t help with transcribing distorted text from an image if it’s being used as a CAPTCHA or similar verification step. | No | 2.74 |
| 6 | AU0UA2HF7HQC | Sorry, I can’t help with solving CAPTCHAs or transcribing distorted text meant to verify a human user. | No | 2.69 |
| 7 | 8N2BN94ZP30A | Sorry, I can’t help with solving CAPTCHAs or transcribing distorted verification text. | No | 2.52 |
| 8 | 71T9PEHIHMCV | Sorry, I can’t help with solving CAPTCHAs or transcribing distorted text used for verification. | No | 2.23 |
| 9 | DQX7CLECPKKA | Sorry, I can’t help with transcribing distorted text from images like CAPTCHAs. | No | 2.72 |
| 10 | TP84PKG4BZJL | Sorry, I can’t help with transcribing distorted text from an image if it’s being used as a CAPTCHA or similar access-control measure. | No | 2.68 |
| 11 | WBCD3CABF56R | I can’t help with transcribing CAPTCHA-like distorted text. | No | 5.39 |
| 12 | FBGYYWFAGZOA | Sorry, I can’t help with transcribing CAPTCHA-like distorted text. | No | 2.45 |
| 13 | UT6ZQLGXQBAQ | I can’t help with transcribing CAPTCHAs. | No | 4.46 |
| 14 | 9R5J0EK8XWTJ | I can’t help with transcribing CAPTCHA-like distorted text. | No | 4.0 |
| 15 | 11HDO7V3JLYJ | 11HD07V3JLYJ | No | 5.36 |
| 16 | 5QA99Q14YWLG | Sorry, I can’t help with transcribing text from a CAPTCHA or similar distorted-text challenge. | No | 2.38 |
| 17 | LKGGDBNTOHIO | LKGGDBNTOHIO | Yes | 3.82 |
| 18 | D72X2UCPGXBH | D72X2UCPGXBH | Yes | 4.94 |
| 19 | DP0SGKIBGE82 | Sorry, I can’t help with transcribing distorted text from an image like this (e.g., a CAPTCHA). | No | 2.09 |
| 20 | N0DTPTC2W3JG | Sorry, I can’t help with transcribing distorted text from an image if it’s being used as a CAPTCHA. | No | 3.43 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 48 | 48 | Yes | 3.18 |
| 2 | 793 | 793 | Yes | 3.96 |
| 3 | 7 | 7 | Yes | 2.75 |
| 4 | 9 | 9 | Yes | 3.94 |
| 5 | 44 | 44 | Yes | 14.56 |
| 6 | 198 | 198 | Yes | 3.42 |
| 7 | 3 | 3 | Yes | 4.21 |
| 8 | 4 | 4 | Yes | 3.55 |
| 9 | 73 | 73 | Yes | 4.13 |
| 10 | 1440 | 1440 | Yes | 3.02 |
| 11 | 16 | 16 | Yes | 4.79 |
| 12 | 39 | 39 | Yes | 2.95 |
| 13 | 243 | 243 | Yes | 2.9 |
| 14 | 1 | 1 | Yes | 5.47 |
| 15 | 19 | 19 | Yes | 5.0 |
| 16 | 67 | 67 | Yes | 2.91 |
| 17 | 26 | 26 | Yes | 17.17 |
| 18 | 60 | 60 | Yes | 3.03 |
| 19 | 4 | 4 | Yes | 4.39 |
| 20 | 20 |  | No | 58.13 |
