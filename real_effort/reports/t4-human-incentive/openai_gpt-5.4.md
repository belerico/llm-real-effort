# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
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
| sudoku_game | 7540 | 29182 | 36722 | 10 | 10 | 25.18 | 503.84 |
| add_numbers | 4120 | 1062 | 5182 | 20 | 0 | 3.83 | 76.65 |
| counting_zeros | 6540 | 33459 | 39999 | 13 | 7 | 26.61 | 532.6 |
| task_decoding | 12280 | 5649 | 17929 | 20 | 0 | 8.40 | 168.17 |
| task_summation | 7480 | 6078 | 13558 | 20 | 0 | 7.81 | 156.34 |
| task_transcription | 3949 | 7677 | 11626 | 8 | 12 | 9.00 | 180.2 |
| task_sequences | 3240 | 3727 | 6967 | 19 | 1 | 7.38 | 147.69 |
| **TOTAL** | **45149** | **86834** | **131983** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 3 5 1 4 5 3 1 4 1 3 5 4 |  | No | 37.88 |
| 2 | 6 2 1 2 3 1 2 5 1 2 4 6 6 4 | 6 2 1 2 3 1 2 5 1 2 4 6 6 4 | Yes | 19.14 |
| 3 | 2 1 4 4 3 2 1 6 5 1 2 4 3 1 |  | No | 30.09 |
| 4 | 2 5 1 3 6 3 2 2 5 6 1 5 3 2 | 2 5 1 3 6 3 2 2 5 6 1 5 3 2 | Yes | 15.09 |
| 5 | 6 1 4 4 6 1 1 6 4 5 5 4 2 2 |  | No | 42.63 |
| 6 | 6 2 1 2 4 2 3 1 5 4 6 1 2 4 | 6 2 1 2 4 2 3 1 5 4 6 1 2 4 | Yes | 11.57 |
| 7 | 5 6 6 2 1 3 5 3 1 1 4 6 3 2 |  | No | 36.15 |
| 8 | 5 6 3 1 4 6 5 2 3 6 4 5 3 2 |  | No | 40.74 |
| 9 | 3 1 6 2 3 3 1 1 2 3 5 4 4 1 | 3 1 6 2 3 3 1 1 2 3 5 4 4 1 | Yes | 12.31 |
| 10 | 1 6 4 3 2 3 2 4 6 1 6 1 3 2 | 1 6 4 3 2 3 2 4 6 1 6 1 3 2 | Yes | 15.67 |
| 11 | 2 1 4 5 3 2 3 4 5 6 4 1 5 6 | 2 1 4 5 3 2 3 4 5 6 4 1 5 6 | Yes | 18.85 |
| 12 | 2 1 2 6 4 3 4 1 6 5 5 6 4 1 | 2 1 2 6 4 3 4 1 6 5 5 6 4 1 | Yes | 11.58 |
| 13 | 2 3 2 6 4 1 5 1 4 3 4 3 1 6 | 2 3 2 6 4 1 5 1 4 3 4 3 1 6 | Yes | 11.9 |
| 14 | 6 5 4 3 6 4 4 1 1 6 5 2 4 2 |  | No | 30.77 |
| 15 | 3 4 6 1 3 4 4 3 5 5 6 5 1 4 |  | No | 39.97 |
| 16 | 3 5 2 6 2 2 6 1 3 4 2 6 5 2 |  | No | 32.63 |
| 17 | 6 1 3 2 5 1 5 4 5 1 3 2 1 4 |  | No | 37.81 |
| 18 | 4 1 5 3 5 4 5 1 2 2 3 6 6 4 |  | No | 32.19 |
| 19 | 1 5 4 2 2 5 1 4 4 1 6 2 1 5 | 1 5 4 2 2 5 1 4 4 1 6 2 1 5 | Yes | 15.89 |
| 20 | 3 2 1 1 4 2 5 3 1 5 4 3 2 6 | 3 2 1 1 4 2 5 3 1 5 4 3 2 6 | Yes | 10.79 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1251 | 1251 | Yes | 3.41 |
| 2 | 1130 | 1130 | Yes | 3.52 |
| 3 | 1953 | 1953 | Yes | 3.68 |
| 4 | 903 | 903 | Yes | 3.77 |
| 5 | 1403 | 1403 | Yes | 5.06 |
| 6 | 2364 | 2364 | Yes | 3.53 |
| 7 | 2189 | 2189 | Yes | 3.23 |
| 8 | 1856 | 1856 | Yes | 3.49 |
| 9 | 1273 | 1273 | Yes | 5.27 |
| 10 | 1186 | 1186 | Yes | 3.49 |
| 11 | 2006 | 2006 | Yes | 3.96 |
| 12 | 1017 | 1017 | Yes | 3.27 |
| 13 | 1213 | 1213 | Yes | 3.68 |
| 14 | 1952 | 1952 | Yes | 4.3 |
| 15 | 2123 | 2123 | Yes | 3.5 |
| 16 | 2080 | 2080 | Yes | 5.04 |
| 17 | 2150 | 2150 | Yes | 5.15 |
| 18 | 1517 | 1517 | Yes | 2.8 |
| 19 | 2632 | 2632 | Yes | 3.2 |
| 20 | 1959 | 1959 | Yes | 3.17 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 75 | 75 | Yes | 34.25 |
| 2 | 44 |  | No | 28.69 |
| 3 | 38 | 38 | Yes | 28.6 |
| 4 | 38 | 38 | Yes | 24.0 |
| 5 | 75 | 75 | Yes | 19.6 |
| 6 | 36 | 36 | Yes | 18.89 |
| 7 | 54 |  | No | 40.79 |
| 8 | 63 | 63 | Yes | 27.97 |
| 9 | 66 |  | No | 27.87 |
| 10 | 48 | 48 | Yes | 19.9 |
| 11 | 69 | 69 | Yes | 22.2 |
| 12 | 72 | 71 | No | 19.77 |
| 13 | 57 | 57 | Yes | 26.52 |
| 14 | 71 |  | No | 30.73 |
| 15 | 53 | 53 | Yes | 21.79 |
| 16 | 51 | 51 | Yes | 29.2 |
| 17 | 40 | 40 | Yes | 24.01 |
| 18 | 35 |  | No | 27.53 |
| 19 | 42 | 42 | Yes | 27.89 |
| 20 | 53 |  | No | 32.1 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QBYCDEO | QBYCDEO | Yes | 6.47 |
| 2 | LJRGYIQ | LJRGYIQ | Yes | 25.44 |
| 3 | FZXIPOH | FZXIPOH | Yes | 4.77 |
| 4 | INJQOBF | INJQOBF | Yes | 7.19 |
| 5 | WURDFNC | WURDFNC | Yes | 3.31 |
| 6 | CVSFIEZ | CVSFIEZ | Yes | 7.49 |
| 7 | HGDLEOX | HGDLEOX | Yes | 18.16 |
| 8 | SURQYOH | SURQYOH | Yes | 16.98 |
| 9 | HMIPCYG | HMIPCYG | Yes | 7.97 |
| 10 | YLTCXWK | YLTCXWK | Yes | 4.06 |
| 11 | XBEKZGR | XBEKZGR | Yes | 6.31 |
| 12 | WDSBAUH | WDSBAUH | Yes | 3.52 |
| 13 | OZLYWIV | OZLYWIV | Yes | 7.07 |
| 14 | PQXMZFG | PQXMZFG | Yes | 5.84 |
| 15 | UBZRHWL | UBZRHWL | Yes | 7.94 |
| 16 | SATOFRM | SATOFRM | Yes | 8.12 |
| 17 | UOAWHQN | UOAWHQN | Yes | 7.07 |
| 18 | IGQFARH | IGQFARH | Yes | 9.29 |
| 19 | ZREQWKD | ZREQWKD | Yes | 5.2 |
| 20 | ZGQFIMB | ZGQFIMB | Yes | 5.79 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 9.6 0.4 | Yes | 9.16 |
| 2 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.92 |
| 3 | [0.9, 9.1] | 0.9 9.1 | Yes | 7.35 |
| 4 | [0.2, 9.8] | 9.8 0.2 | Yes | 6.96 |
| 5 | [0.5, 9.5] | 0.5 9.5 | Yes | 7.44 |
| 6 | [1.1, 8.9] | 1.1 8.9 | Yes | 7.48 |
| 7 | [1.1, 8.9] | 8.9 1.1 | Yes | 6.29 |
| 8 | [2.1, 7.9] | 2.1 7.9 | Yes | 7.57 |
| 9 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.78 |
| 10 | [3.6, 6.4] | 6.4 3.6 | Yes | 9.3 |
| 11 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.74 |
| 12 | [0.6, 9.4] | 0.6 9.4 | Yes | 6.74 |
| 13 | [4.4, 5.6] | 4.4 5.6 | Yes | 7.96 |
| 14 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.57 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 7.64 |
| 16 | [2.4, 7.6] | 2.4 7.6 | Yes | 8.82 |
| 17 | [4.3, 5.7] | 4.3 5.7 | Yes | 9.18 |
| 18 | [3.3, 6.7] | 6.7 3.3 | Yes | 7.73 |
| 19 | [0.2, 9.8] | 9.8 0.2 | Yes | 8.15 |
| 20 | [4.9, 5.1] | 4.9 5.1 | Yes | 7.4 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 08E15285E9E9 | 08E15285E9E9 | Yes | 7.55 |
| 2 | 3XOXPNQPNA8G | 3XOXPNQPNA8G | Yes | 7.73 |
| 3 | COY34QRNI4R3 | Sorry, I can't help with transcribing CAPTCHA text. | No | 4.84 |
| 4 | NQLBASOR2SPV | NQLBASOR2SPV | Yes | 4.93 |
| 5 | T1X9L41IX4RO | Sorry, I can’t help with transcribing CAPTCHA or CAPTCHA-like distorted text. | No | 11.32 |
| 6 | VG5A27GO7GDL | Sorry, I can’t help transcribe or solve distorted text used for verification or security checks. | No | 3.34 |
| 7 | PEINLQ0UA8W1 | I can’t help with transcribing CAPTCHA text. | No | 4.86 |
| 8 | 8WR3GN1NXK9N | 8WR3GN1NXK9N | Yes | 6.15 |
| 9 | 3KSWB2815O4O | 3KSWB2815040 | No | 38.58 |
| 10 | K6XKM49HFMWC | K6XKM49HFMWC | Yes | 4.9 |
| 11 | T5M83DIFK886 | Sorry, I can’t help transcribe text from a CAPTCHA or similar verification image. | No | 3.32 |
| 12 | GYAQ9342MCO0 | GYAQ9342MCOO | No | 33.45 |
| 13 | 26FBXIMSOHHR | 26FBXIMSOHHR | Yes | 11.09 |
| 14 | EXL71LHL60CG | Sorry, I can’t help transcribe or solve CAPTCHA-style distorted text. | No | 4.5 |
| 15 | L2LFFVBS1WLQ | L2LFFVBS1WLQ | Yes | 4.25 |
| 16 | II2UU2JINGH1 | Sorry, I can’t help with solving CAPTCHAs. | No | 5.43 |
| 17 | IUNMNPNXW1KS | IUNMNPNXW1KS | Yes | 5.91 |
| 18 | MPI1WJ6QRE72 | Sorry, I can't help with transcribing CAPTCHA text. | No | 5.19 |
| 19 | 1AHFNMVGAVOW | Sorry, I can’t help solve CAPTCHAs. | No | 6.43 |
| 20 | 2JJ1OZ7L2L8O | Sorry, I can’t help transcribe or solve CAPTCHA-style verification images. | No | 6.32 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 6.19 |
| 2 | 23 | 23 | Yes | 6.17 |
| 3 | 6 | 6 | Yes | 5.38 |
| 4 | 5 | 5 | Yes | 5.21 |
| 5 | 4 | 4 | Yes | 3.58 |
| 6 | 65 | 65 | Yes | 4.44 |
| 7 | 44 | 44 | Yes | 6.44 |
| 8 | 20 |  | No | 51.69 |
| 9 | 243 | 243 | Yes | 3.44 |
| 10 | 26 | 26 | Yes | 5.8 |
| 11 | 198 | 198 | Yes | 5.09 |
| 12 | 67 | 67 | Yes | 4.56 |
| 13 | 9 | 9 | Yes | 3.79 |
| 14 | 1 | 1 | Yes | 5.67 |
| 15 | 3 | 3 | Yes | 5.79 |
| 16 | 63 | 63 | Yes | 4.76 |
| 17 | 28 | 28 | Yes | 5.36 |
| 18 | 60 | 60 | Yes | 5.14 |
| 19 | 16 | 16 | Yes | 4.28 |
| 20 | 793 | 793 | Yes | 4.92 |
