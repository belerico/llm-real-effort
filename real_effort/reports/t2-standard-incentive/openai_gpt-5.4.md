# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 6840 | 29484 | 36324 | 9 | 11 | 29.70 | 594.24 |
| add_numbers | 3780 | 997 | 4777 | 20 | 0 | 4.01 | 80.33 |
| counting_zeros | 6200 | 32078 | 38278 | 14 | 6 | 24.85 | 497.35 |
| task_decoding | 11940 | 5400 | 17340 | 20 | 0 | 8.51 | 170.38 |
| task_summation | 7140 | 5960 | 13100 | 20 | 0 | 7.64 | 152.98 |
| task_transcription | 3601 | 10634 | 14235 | 11 | 9 | 12.95 | 259.08 |
| task_sequences | 2900 | 1814 | 4714 | 20 | 0 | 4.73 | 94.64 |
| **TOTAL** | **42401** | **86367** | **128768** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 6 3 3 5 6 4 2 1 6 6 1 3 | 4 5 6 3 3 5 6 4 2 1 6 6 1 3 | Yes | 36.72 |
| 2 | 5 6 4 2 5 4 6 3 2 5 3 5 2 6 | 5 6 4 2 5 4 6 3 2 5 3 5 2 6 | Yes | 12.87 |
| 3 | 3 4 2 4 5 4 3 6 3 6 5 3 4 3 |  | No | 29.86 |
| 4 | 5 3 6 2 5 4 3 6 2 6 3 1 5 4 |  | No | 33.15 |
| 5 | 4 3 5 2 1 2 3 1 4 6 5 6 5 4 | 4 3 5 2 1 2 3 1 4 6 5 6 5 4 | Yes | 14.66 |
| 6 | 4 6 5 1 1 4 3 6 5 1 4 1 4 5 |  | No | 33.88 |
| 7 | 5 4 1 3 1 4 6 1 3 6 2 6 5 4 | 5 4 1 3 1 4 6 1 3 6 2 6 5 4 | Yes | 12.1 |
| 8 | 3 1 4 6 5 2 2 5 4 1 2 6 3 6 |  | No | 29.16 |
| 9 | 3 6 1 3 3 6 2 1 5 2 3 2 5 4 |  | No | 33.06 |
| 10 | 2 6 6 3 2 4 5 6 3 2 2 5 3 4 |  | No | 38.64 |
| 11 | 3 1 3 1 6 4 6 3 4 3 6 1 3 4 | 3 1 3 1 6 4 6 3 4 3 6 1 3 4 | Yes | 13.86 |
| 12 | 5 3 1 1 3 4 5 3 3 1 5 3 4 2 |  | No | 40.54 |
| 13 | 1 5 3 4 5 4 6 1 2 5 1 5 4 5 |  | No | 30.23 |
| 14 | 5 1 3 6 3 2 3 2 4 3 4 2 4 6 | 5 1 3 6 3 2 3 2 4 3 4 2 4 6 | Yes | 14.46 |
| 15 | 1 3 6 2 6 5 1 6 3 3 6 1 6 1 |  | No | 28.81 |
| 16 | 2 6 3 2 3 1 2 1 5 2 1 4 2 3 | 2 6 3 2 3 1 2 1 5 2 1 4 2 3 | Yes | 14.63 |
| 17 | 6 1 2 2 6 5 1 2 1 5 2 3 6 4 | TIMEOUT | No | 120.03 |
| 18 | 6 4 6 6 2 5 2 5 3 6 6 3 4 5 | 6 4 6 6 2 5 2 5 3 6 6 3 4 5 | Yes | 11.68 |
| 19 | 1 2 3 3 4 5 4 2 1 4 6 4 5 2 |  | No | 31.74 |
| 20 | 4 1 4 2 6 3 1 1 4 6 6 5 6 1 | 4 1 4 2 6 3 1 1 4 6 6 5 6 1 | Yes | 13.92 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1914 | 1914 | Yes | 3.4 |
| 2 | 1555 | 1555 | Yes | 4.94 |
| 3 | 1853 | 1853 | Yes | 3.51 |
| 4 | 1828 | 1828 | Yes | 3.81 |
| 5 | 2181 | 2181 | Yes | 5.44 |
| 6 | 1621 | 1621 | Yes | 3.85 |
| 7 | 1431 | 1431 | Yes | 4.66 |
| 8 | 1486 | 1486 | Yes | 4.09 |
| 9 | 1603 | 1603 | Yes | 3.73 |
| 10 | 1330 | 1330 | Yes | 3.98 |
| 11 | 1317 | 1317 | Yes | 4.94 |
| 12 | 1844 | 1844 | Yes | 4.05 |
| 13 | 1760 | 1760 | Yes | 4.95 |
| 14 | 1099 | 1099 | Yes | 3.15 |
| 15 | 1085 | 1085 | Yes | 3.82 |
| 16 | 1574 | 1574 | Yes | 3.61 |
| 17 | 1923 | 1923 | Yes | 4.0 |
| 18 | 1580 | 1580 | Yes | 3.23 |
| 19 | 2222 | 2222 | Yes | 3.96 |
| 20 | 1282 | 1282 | Yes | 3.12 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 42 | 42 | Yes | 16.23 |
| 2 | 57 |  | No | 33.74 |
| 3 | 66 | 66 | Yes | 27.15 |
| 4 | 35 | 35 | Yes | 28.33 |
| 5 | 45 | 45 | Yes | 19.73 |
| 6 | 51 |  | No | 27.22 |
| 7 | 48 | 48 | Yes | 17.27 |
| 8 | 48 | 48 | Yes | 16.44 |
| 9 | 40 | 40 | Yes | 22.68 |
| 10 | 72 | 72 | Yes | 18.45 |
| 11 | 54 |  | No | 33.3 |
| 12 | 74 | 74 | Yes | 20.0 |
| 13 | 50 |  | No | 35.92 |
| 14 | 53 |  | No | 33.51 |
| 15 | 52 | 52 | Yes | 22.56 |
| 16 | 72 | 72 | Yes | 18.51 |
| 17 | 68 | 68 | Yes | 23.02 |
| 18 | 42 | 43 | No | 33.67 |
| 19 | 66 | 66 | Yes | 28.37 |
| 20 | 43 | 43 | Yes | 20.93 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YARBCHV | YARBCHV | Yes | 9.92 |
| 2 | KBGCZED | KBGCZED | Yes | 5.68 |
| 3 | FNYRDIP | FNYRDIP | Yes | 7.67 |
| 4 | DAUTNKR | DAUTNKR | Yes | 8.4 |
| 5 | YJOQBNC | YJOQBNC | Yes | 5.79 |
| 6 | DARYJOQ | DARYJOQ | Yes | 5.22 |
| 7 | DAKWIXN | DAKWIXN | Yes | 6.41 |
| 8 | HVIGQEA | HVIGQEA | Yes | 13.49 |
| 9 | ILOMPWU | ILOMPWU | Yes | 5.09 |
| 10 | BDIFOEW | BDIFOEW | Yes | 12.1 |
| 11 | AOETZPG | AOETZPG | Yes | 6.36 |
| 12 | KEXPRIT | KEXPRIT | Yes | 8.29 |
| 13 | PRYFDAH | PRYFDAH | Yes | 11.61 |
| 14 | MDKOLFJ | MDKOLFJ | Yes | 6.26 |
| 15 | YKCSTZF | YKCSTZF | Yes | 7.31 |
| 16 | GEAXMZP | GEAXMZP | Yes | 6.91 |
| 17 | KTVRLIA | KTVRLIA | Yes | 13.29 |
| 18 | FZSCPLB | FZSCPLB | Yes | 6.36 |
| 19 | HDOVELC | HDOVELC | Yes | 14.98 |
| 20 | ZMVHSBU | ZMVHSBU | Yes | 9.01 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.02 |
| 2 | [4.8, 5.2] | 5.2 4.8 | Yes | 12.21 |
| 3 | [3.9, 6.1] | 6.1 3.9 | Yes | 7.75 |
| 4 | [1.8, 8.2] | 8.2 1.8 | Yes | 8.1 |
| 5 | [4.9, 5.1] | 4.9 5.1 | Yes | 8.91 |
| 6 | [0.6, 9.4] | 9.4 0.6 | Yes | 8.67 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.49 |
| 8 | [3.8, 6.2] | 6.2 3.8 | Yes | 7.02 |
| 9 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.46 |
| 10 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.98 |
| 11 | [2.3, 7.7] | 7.7 2.3 | Yes | 7.17 |
| 12 | [2.1, 7.9] | 2.1 7.9 | Yes | 6.76 |
| 13 | [3.1, 6.9] | 6.9 3.1 | Yes | 8.03 |
| 14 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.72 |
| 15 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.7 |
| 16 | [1.4, 8.6] | 8.6 1.4 | Yes | 4.29 |
| 17 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.08 |
| 18 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.15 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 10.37 |
| 20 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.93 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 0EFAFWA9KAQ9 | 0EFAFWA9KA09 | No | 41.15 |
| 2 | O84CTJXC3UYW | O84CTJXC3UYW | Yes | 5.97 |
| 3 | 5TM8387DR411 | Sorry, I can't help with solving CAPTCHAs or other human-verification challenges. | No | 5.12 |
| 4 | F7V9A7996RUE | F7V9A7996RUE | Yes | 11.53 |
| 5 | 1VIN9PXC0HDX | 1VIN9PXC0HDX | Yes | 16.85 |
| 6 | XMI3TBHYP1NQ | XMI3TBHYP1NQ | Yes | 5.41 |
| 7 | 9FNDEWWE23V8 | I can’t help with solving CAPTCHAs. | No | 22.97 |
| 8 | 7ZA1SKLXR2S1 | 7ZA1SKLXR2S1 | Yes | 4.07 |
| 9 | SUKUC4V4EKY9 | SUKUC4V4EKY9 | Yes | 6.09 |
| 10 | 55DE3RX7KF8W | Sorry, I can’t help solve or transcribe CAPTCHA-style images. | No | 4.43 |
| 11 | VJO12QQVK774 | Sorry, I can’t help transcribe distorted verification text or solve CAPTCHAs. | No | 4.56 |
| 12 | 51HQWJA185CV | 51HQWJA185CV | Yes | 5.4 |
| 13 | XL73HCEAJJAJ | XL73HCEAJJAJ | Yes | 6.8 |
| 14 | S9GIKWQLLN1D | S9GIKWQLLN1D | Yes | 6.51 |
| 15 | X75TLUVCWSSC | Sorry, I can’t help with solving CAPTCHAs. | No | 4.59 |
| 16 | 3NWT9LRJ8CKP | Sorry, I can’t help solve CAPTCHAs or transcribe distorted verification text. | No | 4.93 |
| 17 | 6HBS6Y3F3BDS | 6HBS6Y3F3BDS | Yes | 7.77 |
| 18 | F3ANRYIUYMU4 | F3ANRYIUYMU4 | Yes | 6.85 |
| 19 | DNWE0O0MV62X | DNWE0000MV62X | No | 45.77 |
| 20 | JS07ATUZQC4L | JS07ATUZoc4L | No | 42.23 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 31 | 31 | Yes | 3.28 |
| 2 | 44 | 44 | Yes | 4.64 |
| 3 | 63 | 63 | Yes | 3.99 |
| 4 | 23 | 23 | Yes | 6.46 |
| 5 | 65 | 65 | Yes | 4.49 |
| 6 | 5 | 5 | Yes | 4.89 |
| 7 | 1 | 1 | Yes | 5.09 |
| 8 | 9 | 9 | Yes | 5.94 |
| 9 | 243 | 243 | Yes | 3.07 |
| 10 | 1440 | 1440 | Yes | 3.51 |
| 11 | 3 | 3 | Yes | 4.95 |
| 12 | 64 | 64 | Yes | 4.58 |
| 13 | 7680 | 7680 | Yes | 5.16 |
| 14 | 4 | 4 | Yes | 5.64 |
| 15 | 39 | 39 | Yes | 5.74 |
| 16 | 3 | 3 | Yes | 5.13 |
| 17 | 67 | 67 | Yes | 3.88 |
| 18 | 26 | 26 | Yes | 6.43 |
| 19 | 60 | 60 | Yes | 3.62 |
| 20 | 28 | 28 | Yes | 4.14 |
