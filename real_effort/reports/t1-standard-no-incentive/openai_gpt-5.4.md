# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
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
| sudoku_game | 7020 | 26917 | 33937 | 14 | 6 | 22.23 | 444.92 |
| add_numbers | 3600 | 1078 | 4678 | 20 | 0 | 4.11 | 82.29 |
| counting_zeros | 5719 | 30899 | 36618 | 12 | 8 | 30.45 | 609.25 |
| task_decoding | 11760 | 5139 | 16899 | 20 | 0 | 7.92 | 158.55 |
| task_summation | 6960 | 5918 | 12878 | 20 | 0 | 7.85 | 157.11 |
| task_transcription | 3424 | 7503 | 10927 | 12 | 8 | 9.37 | 187.52 |
| task_sequences | 2721 | 5910 | 8631 | 18 | 2 | 9.10 | 181.97 |
| **TOTAL** | **41204** | **83364** | **124568** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 3 1 6 2 5 5 1 6 5 4 6 6 | 1 5 3 1 6 2 5 5 1 6 5 4 6 6 | Yes | 15.34 |
| 2 | 3 6 6 5 3 2 6 2 4 6 2 6 3 2 | 3 6 6 5 3 2 6 2 4 6 2 6 3 2 | Yes | 17.32 |
| 3 | 6 3 6 1 4 5 2 3 6 6 4 3 1 6 | 6 3 6 1 4 5 2 3 6 6 4 3 1 6 | Yes | 27.41 |
| 4 | 4 6 2 1 3 5 4 4 2 6 3 5 4 5 |  | No | 36.69 |
| 5 | 5 6 5 4 3 3 4 2 6 5 4 2 6 1 | 5 6 5 4 3 3 4 2 6 5 4 2 6 1 | Yes | 12.71 |
| 6 | 2 1 6 3 4 1 5 2 6 2 4 3 6 5 | 2 1 6 3 4 1 5 2 6 2 4 3 6 5 | Yes | 11.48 |
| 7 | 1 6 3 3 5 6 2 1 5 2 6 1 2 5 |  | No | 37.06 |
| 8 | 1 6 2 5 4 1 3 5 3 6 3 2 5 3 | 1 6 2 5 4 1 3 5 3 6 3 2 5 3 | Yes | 10.49 |
| 9 | 3 5 4 6 3 1 5 3 2 5 6 3 6 4 | 3 5 4 6 3 1 5 3 2 5 6 3 6 4 | Yes | 13.63 |
| 10 | 5 2 2 1 5 3 2 4 6 1 5 1 3 4 |  | No | 34.4 |
| 11 | 3 4 6 2 1 3 2 1 4 5 6 4 3 2 | 3 4 6 2 1 3 2 1 4 5 6 4 3 2 | Yes | 17.1 |
| 12 | 6 4 1 1 2 5 4 6 5 3 5 1 4 5 |  | No | 30.35 |
| 13 | 1 2 6 3 2 5 3 3 1 1 6 4 2 1 | 1 2 6 3 2 5 3 3 1 1 6 4 2 1 | Yes | 27.57 |
| 14 | 2 5 4 6 4 6 2 2 5 6 1 3 6 5 |  | No | 38.62 |
| 15 | 6 5 2 4 1 6 6 1 4 3 5 3 1 5 | 6 5 2 4 1 6 6 1 4 3 5 3 1 5 | Yes | 10.62 |
| 16 | 1 5 5 4 2 2 6 1 6 5 5 6 4 3 | 1 5 5 4 2 2 6 1 6 5 5 6 4 3 | Yes | 12.26 |
| 17 | 5 1 1 5 6 3 6 1 2 4 1 4 5 6 | 5 1 1 5 6 3 6 1 2 4 1 4 5 6 | Yes | 19.03 |
| 18 | 6 2 4 5 5 6 1 6 3 2 4 5 4 1 |  | No | 43.06 |
| 19 | 4 6 1 6 2 6 4 2 1 1 3 4 6 5 | 4 6 1 6 2 6 4 2 1 1 3 4 6 5 | Yes | 13.64 |
| 20 | 1 4 2 3 3 4 2 3 5 3 4 6 1 6 | 1 4 2 3 3 4 2 3 5 3 4 6 1 6 | Yes | 15.92 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2063 | 2063 | Yes | 4.07 |
| 2 | 1315 | 1315 | Yes | 3.77 |
| 3 | 451 | 451 | Yes | 3.39 |
| 4 | 1587 | 1587 | Yes | 2.96 |
| 5 | 1781 | 1781 | Yes | 3.33 |
| 6 | 1069 | 1069 | Yes | 2.66 |
| 7 | 1761 | 1761 | Yes | 3.38 |
| 8 | 1215 | 1215 | Yes | 4.69 |
| 9 | 1192 | 1192 | Yes | 3.43 |
| 10 | 1743 | 1743 | Yes | 5.46 |
| 11 | 1649 | 1649 | Yes | 3.85 |
| 12 | 1312 | 1312 | Yes | 3.65 |
| 13 | 1904 | 1904 | Yes | 3.91 |
| 14 | 478 | 478 | Yes | 3.53 |
| 15 | 1292 | 1292 | Yes | 4.06 |
| 16 | 1040 | 1040 | Yes | 4.26 |
| 17 | 1106 | 1106 | Yes | 7.25 |
| 18 | 1255 | 1255 | Yes | 4.74 |
| 19 | 1662 | 1662 | Yes | 3.82 |
| 20 | 1343 | 1343 | Yes | 5.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 28.95 |
| 2 | 75 |  | No | 29.77 |
| 3 | 55 | 55 | Yes | 29.45 |
| 4 | 68 | 68 | Yes | 26.05 |
| 5 | 72 | 72 | Yes | 18.48 |
| 6 | 69 |  | No | 34.58 |
| 7 | 65 |  | No | 28.34 |
| 8 | 63 |  | No | 26.04 |
| 9 | 72 | 72 | Yes | 18.76 |
| 10 | 72 | 72 | Yes | 23.12 |
| 11 | 63 | TIMEOUT | No | 120.02 |
| 12 | 39 | 39 | Yes | 17.03 |
| 13 | 70 |  | No | 36.14 |
| 14 | 55 | 55 | Yes | 24.65 |
| 15 | 58 | 58 | Yes | 27.26 |
| 16 | 38 | 38 | Yes | 20.02 |
| 17 | 41 |  | No | 37.16 |
| 18 | 43 | 43 | Yes | 16.67 |
| 19 | 44 | 44 | Yes | 18.61 |
| 20 | 47 | 47 | Yes | 27.85 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LEVUDTJ | LEVUDTJ | Yes | 5.89 |
| 2 | AEBVINY | AEBVINY | Yes | 24.34 |
| 3 | CAYPXBI | CAYPXBI | Yes | 4.33 |
| 4 | ABGRTSW | ABGRTSW | Yes | 5.22 |
| 5 | DUQMNHZ | DUQMNHZ | Yes | 7.13 |
| 6 | MFUDAVR | MFUDAVR | Yes | 8.91 |
| 7 | WKPMXHT | WKPMXHT | Yes | 3.43 |
| 8 | GSCPFIK | GSCPFIK | Yes | 6.03 |
| 9 | DPXWLRB | DPXWLRB | Yes | 3.44 |
| 10 | KOWJCNU | KOWJCNU | Yes | 5.5 |
| 11 | JUFYLRW | JUFYLRW | Yes | 7.4 |
| 12 | QZOCUPH | QZOCUPH | Yes | 6.45 |
| 13 | IFLOSPV | IFLOSPV | Yes | 10.18 |
| 14 | HNTMAKP | HNTMAKP | Yes | 5.86 |
| 15 | RLIJETN | RLIJETN | Yes | 21.28 |
| 16 | HMDTJXI | HMDTJXI | Yes | 6.37 |
| 17 | CLZYHJG | CLZYHJG | Yes | 7.38 |
| 18 | RQLFPMK | RQLFPMK | Yes | 5.64 |
| 19 | ZGSLNVY | ZGSLNVY | Yes | 5.38 |
| 20 | XEYWIMJ | XEYWIMJ | Yes | 8.2 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.17 |
| 2 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.44 |
| 3 | [3.5, 6.5] | 6.5 3.5 | Yes | 9.73 |
| 4 | [3.3, 6.7] | 6.7 3.3 | Yes | 8.21 |
| 5 | [0.1, 9.9] | 0.1 9.9 | Yes | 8.38 |
| 6 | [3.1, 6.9] | 3.1 6.9 | Yes | 8.24 |
| 7 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.08 |
| 8 | [1.9, 8.1] | 8.1 1.9 | Yes | 7.9 |
| 9 | [4.9, 5.1] | 4.9 5.1 | Yes | 8.81 |
| 10 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.59 |
| 11 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.43 |
| 12 | [3.6, 6.4] | 3.6 6.4 | Yes | 7.51 |
| 13 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.12 |
| 14 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.3 |
| 15 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.3 |
| 16 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.09 |
| 17 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.25 |
| 18 | [0.1, 9.9] | 0.1 9.9 | Yes | 7.07 |
| 19 | [0.1, 9.9] | 0.1 9.9 | Yes | 7.94 |
| 20 | [1.6, 8.4] | 1.6 8.4 | Yes | 8.38 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HSKQJ7ENR67D | Sorry, I can’t help transcribe or solve distorted text used for verification or CAPTCHA challenges. | No | 3.6 |
| 2 | XZIIONIP6CXT | XZIIONIP6CXT | Yes | 17.78 |
| 3 | L8R2FL4T0WEN | L8R2FL4T0WEN | Yes | 10.94 |
| 4 | FIZY8MGMO2LK | FIZY8MGMO2LK | Yes | 3.6 |
| 5 | S85A71GYF23R | Sorry, I can’t help solve or transcribe CAPTCHA/verification text. | No | 3.15 |
| 6 | PSZQUP93FQJH | PSZQUP93FQJH | Yes | 7.51 |
| 7 | V5GJVY8QDIIS | V5GJVY8QDIIS | Yes | 10.18 |
| 8 | 5MFDUESILQWE | 5MFDUESILQWE | Yes | 15.48 |
| 9 | YXA0O8I7CQ7E | YXA0O8I7CQ7E | Yes | 40.35 |
| 10 | KF9LBE2BN5ZO | KF9LBE2BN5ZO | Yes | 10.97 |
| 11 | Y9GY0WUL2TTN | I can’t help with solving CAPTCHAs. | No | 4.06 |
| 12 | SZL9MH64WK4X | SZL9MH64WK4X | Yes | 7.69 |
| 13 | P32RBJ3W56GG | P32RBJ3W56GG | Yes | 7.66 |
| 14 | XIY6EVUVHMAQ | XIY6EVUVHMAQ | Yes | 5.9 |
| 15 | 80VKYCE1IJ64 | Sorry, I can’t help transcribe or solve distorted text used for CAPTCHA-like verification. | No | 4.28 |
| 16 | XZ06KE3AD27J | XZ06KE3AD27J | Yes | 10.65 |
| 17 | PKDF6KY7UPZ8 | Sorry, I can’t help solve or transcribe CAPTCHA text. | No | 4.01 |
| 18 | RQAFV03B5D2K | Sorry, I can’t help solve CAPTCHAs or other anti-bot verification text. | No | 7.54 |
| 19 | 67J4GF53EYXJ | I can’t help with solving CAPTCHAs. | No | 4.65 |
| 20 | H0NAWLODW2P7 | HONAWLODW2P7 | No | 7.44 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 4.14 |
| 2 | 4 | 4 | Yes | 4.99 |
| 3 | 16 | 16 | Yes | 4.41 |
| 4 | 243 | 243 | Yes | 3.9 |
| 5 | 3 | 3 | Yes | 6.58 |
| 6 | 5 |  | No | 41.02 |
| 7 | 10 | 10 | Yes | 9.67 |
| 8 | 63 | 63 | Yes | 4.01 |
| 9 | 26 | 26 | Yes | 8.59 |
| 10 | 28 | 28 | Yes | 5.05 |
| 11 | 60 | 60 | Yes | 4.47 |
| 12 | 65 | 65 | Yes | 4.84 |
| 13 | 198 | 198 | Yes | 5.39 |
| 14 | 793 | 793 | Yes | 3.93 |
| 15 | 23 | 23 | Yes | 7.3 |
| 16 | 67 | 67 | Yes | 2.34 |
| 17 | 44 | 44 | Yes | 6.94 |
| 18 | 5 | 5 | Yes | 5.9 |
| 19 | 4096 |  | No | 44.46 |
| 20 | 1440 | 1440 | Yes | 4.03 |
