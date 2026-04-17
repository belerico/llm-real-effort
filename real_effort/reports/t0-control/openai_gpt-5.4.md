# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-19 10:09:16

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
| sudoku_game | 6720 | 24102 | 30822 | 15 | 5 | 20.29 | 406.09 |
| add_numbers | 3300 | 1041 | 4341 | 20 | 0 | 3.60 | 72.17 |
| counting_zeros | 5720 | 34652 | 40372 | 11 | 9 | 28.77 | 575.59 |
| task_decoding | 11460 | 7257 | 18717 | 20 | 0 | 9.62 | 192.63 |
| task_summation | 6660 | 5944 | 12604 | 20 | 0 | 8.08 | 161.87 |
| task_transcription | 3130 | 10634 | 13764 | 13 | 7 | 15.22 | 304.52 |
| task_sequences | 2420 | 4073 | 6493 | 19 | 1 | 7.45 | 149.02 |
| **TOTAL** | **39410** | **87703** | **127113** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 5 1 4 3 2 3 4 2 5 1 2 6 | 4 3 5 1 4 3 2 3 4 2 5 1 2 6 | Yes | 17.49 |
| 2 | 6 6 4 2 4 4 1 5 5 1 4 3 3 1 | 6 6 4 2 4 4 1 5 5 1 4 3 3 1 | Yes | 14.1 |
| 3 | 2 3 1 4 6 5 1 3 2 6 2 1 3 2 |  | No | 34.67 |
| 4 | 4 1 4 6 2 3 4 5 5 1 6 5 4 1 |  | No | 35.16 |
| 5 | 4 5 6 3 2 5 6 2 4 1 4 4 6 3 | 4 5 6 3 2 5 6 2 4 1 4 4 6 3 | Yes | 15.5 |
| 6 | 4 2 1 4 5 2 6 1 3 5 3 6 5 1 | 4 2 1 4 5 2 6 1 3 5 3 6 5 1 | Yes | 11.49 |
| 7 | 3 1 2 4 6 2 5 6 4 3 1 4 2 5 |  | No | 38.12 |
| 8 | 1 5 5 2 1 4 6 3 1 4 4 3 6 1 | 1 5 5 2 1 4 6 3 1 4 4 3 6 1 | Yes | 12.49 |
| 9 | 2 6 5 6 6 2 1 3 6 4 5 3 6 2 | 2 6 5 6 6 2 1 3 6 4 5 3 6 2 | Yes | 17.79 |
| 10 | 6 2 2 3 4 2 3 3 2 3 2 6 4 3 |  | No | 39.12 |
| 11 | 6 1 1 4 5 4 2 1 4 1 2 2 5 4 | 6 1 1 4 5 4 2 1 4 1 2 2 5 4 | Yes | 12.69 |
| 12 | 2 6 3 6 5 4 2 3 4 5 2 2 4 1 | 2 6 3 6 5 4 2 3 4 5 2 2 4 1 | Yes | 13.72 |
| 13 | 6 5 4 5 5 1 3 5 3 1 6 1 5 2 | 6 5 4 5 5 1 3 5 3 1 6 1 5 2 | Yes | 9.46 |
| 14 | 2 1 3 5 1 4 4 6 5 3 5 4 3 1 | 2 1 3 5 1 4 4 6 5 3 5 4 3 1 | Yes | 13.16 |
| 15 | 5 4 1 3 5 3 1 5 3 6 1 6 6 2 | 5 4 1 3 5 3 1 5 3 6 1 6 6 2 | Yes | 27.53 |
| 16 | 4 6 3 3 6 4 2 4 5 1 6 2 5 3 |  | No | 34.02 |
| 17 | 3 1 3 6 5 3 2 5 6 1 2 3 4 1 | 3 1 3 6 5 3 2 5 6 1 2 3 4 1 | Yes | 17.22 |
| 18 | 6 2 4 1 4 6 5 6 1 3 1 3 4 1 | 6 2 4 1 4 6 5 6 1 3 1 3 4 1 | Yes | 12.25 |
| 19 | 1 4 2 3 2 4 1 3 3 4 6 5 6 4 | 1 4 2 3 2 4 1 3 3 4 6 5 6 4 | Yes | 12.08 |
| 20 | 6 3 3 1 5 6 1 4 6 1 4 3 5 4 | 6 3 3 1 5 6 1 4 6 1 4 3 5 4 | Yes | 17.84 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2376 | 2376 | Yes | 3.95 |
| 2 | 1372 | 1372 | Yes | 3.89 |
| 3 | 2382 | 2382 | Yes | 3.6 |
| 4 | 2147 | 2147 | Yes | 2.91 |
| 5 | 1283 | 1283 | Yes | 3.08 |
| 6 | 1817 | 1817 | Yes | 2.9 |
| 7 | 1390 | 1390 | Yes | 4.56 |
| 8 | 917 | 917 | Yes | 3.96 |
| 9 | 1499 | 1499 | Yes | 3.89 |
| 10 | 2083 | 2083 | Yes | 3.28 |
| 11 | 943 | 943 | Yes | 3.01 |
| 12 | 2155 | 2155 | Yes | 3.32 |
| 13 | 2261 | 2261 | Yes | 3.12 |
| 14 | 1398 | 1398 | Yes | 3.79 |
| 15 | 1352 | 1352 | Yes | 4.09 |
| 16 | 2068 | 2068 | Yes | 3.07 |
| 17 | 1074 | 1074 | Yes | 3.82 |
| 18 | 1695 | 1695 | Yes | 4.21 |
| 19 | 1979 | 1979 | Yes | 3.88 |
| 20 | 1719 | 1719 | Yes | 3.74 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 |  | No | 39.85 |
| 2 | 70 |  | No | 32.84 |
| 3 | 48 | 48 | Yes | 18.52 |
| 4 | 45 | 45 | Yes | 20.1 |
| 5 | 65 | 65 | Yes | 31.95 |
| 6 | 74 |  | No | 32.14 |
| 7 | 42 | 42 | Yes | 18.18 |
| 8 | 50 | 50 | Yes | 26.95 |
| 9 | 50 | 50 | Yes | 17.43 |
| 10 | 73 |  | No | 35.84 |
| 11 | 63 | 63 | Yes | 34.89 |
| 12 | 40 | 40 | Yes | 24.6 |
| 13 | 47 | 47 | Yes | 13.4 |
| 14 | 39 |  | No | 28.96 |
| 15 | 43 |  | No | 37.04 |
| 16 | 37 | 37 | Yes | 19.85 |
| 17 | 43 |  | No | 45.81 |
| 18 | 53 | 53 | Yes | 32.45 |
| 19 | 48 |  | No | 33.87 |
| 20 | 49 | 48 | No | 30.65 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WUCGSHQ | WUCGSHQ | Yes | 6.48 |
| 2 | ZVMUBOR | ZVMUBOR | Yes | 5.97 |
| 3 | GLSOJMP | GLSOJMP | Yes | 7.06 |
| 4 | RTQVSML | RTQVSML | Yes | 5.74 |
| 5 | SJPMQFZ | SJPMQFZ | Yes | 6.38 |
| 6 | MYCPTLR | MYCPTLR | Yes | 7.41 |
| 7 | JAHLTDU | JAHLTDU | Yes | 28.57 |
| 8 | NXIOLZA | NXIOLZA | Yes | 6.17 |
| 9 | DEMWSBJ | DEMWSBJ | Yes | 8.82 |
| 10 | SOYVIPZ | SOYVIPZ | Yes | 9.84 |
| 11 | EOCMJKI | EOCMJKI | Yes | 9.1 |
| 12 | INDXBRW | INDXBRW | Yes | 12.5 |
| 13 | JRVBSMQ | JRVBSMQ | Yes | 6.94 |
| 14 | HNOIEPT | HNOIEPT | Yes | 21.03 |
| 15 | JIWDBES | JIWDBES | Yes | 6.01 |
| 16 | COSQLJT | COSQLJT | Yes | 12.61 |
| 17 | VWYDTXL | VWYDTXL | Yes | 7.16 |
| 18 | UAIDLTS | UAIDLTS | Yes | 6.51 |
| 19 | BAMINGY | BAMINGY | Yes | 13.45 |
| 20 | SZCDTUF | SZCDTUF | Yes | 4.68 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.4, 9.6] | 9.6 0.4 | Yes | 6.25 |
| 2 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.39 |
| 3 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.83 |
| 4 | [4.6, 5.4] | 5.4 4.6 | Yes | 6.38 |
| 5 | [3.9, 6.1] | 3.9 6.1 | Yes | 7.98 |
| 6 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.88 |
| 7 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.7 |
| 8 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.58 |
| 9 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.38 |
| 10 | [0.5, 9.5] | 0.5 9.5 | Yes | 9.01 |
| 11 | [4.0, 6.0] | 6.0 4.0 | Yes | 10.41 |
| 12 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.23 |
| 13 | [4.4, 5.6] | 4.4 5.6 | Yes | 7.94 |
| 14 | [0.5, 9.5] | 9.5 0.5 | Yes | 9.02 |
| 15 | [3.8, 6.2] | 6.2 3.8 | Yes | 8.0 |
| 16 | [2.3, 7.7] | 7.7 2.3 | Yes | 8.03 |
| 17 | [0.4, 9.6] | 9.6 0.4 | Yes | 8.58 |
| 18 | [0.7, 9.3] | 9.3 0.7 | Yes | 9.32 |
| 19 | [2.3, 7.7] | 2.3 7.7 | Yes | 8.91 |
| 20 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.87 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JFEBW3E4WDI8 | JFEBW3E4WDI8 | Yes | 11.48 |
| 2 | GXN1BECM3T8Y | Sorry, I can’t help solve or transcribe CAPTCHA-style distorted text. | No | 5.54 |
| 3 | ZUGY9YBELHK4 | ZUGY9YBELHK4 | Yes | 8.11 |
| 4 | VPDLXP3PD8M6 | Sorry, I can't help with transcribing CAPTCHA text. | No | 7.12 |
| 5 | JM0FYX3LRR0H | JMOFYX3LRROH | No | 14.63 |
| 6 | GWJVPM7TSXRS | GWJVPM7TSXRS | Yes | 8.77 |
| 7 | 96OXO7B79G6T |  | No | 52.62 |
| 8 | F2YBX3VV8DKE | F2YBX3VV8DKE | Yes | 8.1 |
| 9 | OOPH8UNIF87O | OOPH8UNIF87O | Yes | 25.59 |
| 10 | C11FYP3HMCC8 | C11FYP3HMCC8 | Yes | 4.67 |
| 11 | L1KVR7PFIAIM | L1KVR7PFIAIM | Yes | 12.71 |
| 12 | 9D0B6UQZ4VMK | 9D0B6UQZ4VMK | Yes | 22.01 |
| 13 | WCQL78YS90KW | WCQL78YSS90KW | No | 8.48 |
| 14 | DNINTUYT8GYQ | DNINTUYT8GYQ | Yes | 8.93 |
| 15 | SJ67GDYMKQ6C | SJ67GDYMKQ6C | Yes | 19.1 |
| 16 | AZZT9YB6L55K | AZZT9YB6L55K | Yes | 7.01 |
| 17 | TOPXFDO70ZEW | TOPXFDO70ZEW | Yes | 15.15 |
| 18 | 2POPAORYZB9F | Sorry, I can’t help with solving CAPTCHAs. | No | 5.02 |
| 19 | ADINI8WY6RAB | ADINI8WYGRAB | No | 51.04 |
| 20 | 0K3DVOT1F2CQ | 0K3DVOT1F2CQ | Yes | 8.3 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 48 | 48 | Yes | 4.6 |
| 2 | 39 | 39 | Yes | 4.02 |
| 3 | 9 | 9 | Yes | 4.84 |
| 4 | 67 | 67 | Yes | 3.05 |
| 5 | 64 | 64 | Yes | 4.13 |
| 6 | 16 | 16 | Yes | 4.87 |
| 7 | 198 | 198 | Yes | 5.59 |
| 8 | 60 | 60 | Yes | 4.05 |
| 9 | 36 | 36 | Yes | 1.61 |
| 10 | 44 | 44 | Yes | 6.88 |
| 11 | 19 | 19 | Yes | 4.19 |
| 12 | 28 | 28 | Yes | 3.69 |
| 13 | 3 | 3 | Yes | 9.91 |
| 14 | 1 | 1 | Yes | 5.42 |
| 15 | 243 | 243 | Yes | 3.24 |
| 16 | 23 | 23 | Yes | 20.17 |
| 17 | 60 | 60 | Yes | 5.91 |
| 18 | 20 |  | No | 45.27 |
| 19 | 65 | 65 | Yes | 3.44 |
| 20 | 793 | 793 | Yes | 4.14 |
