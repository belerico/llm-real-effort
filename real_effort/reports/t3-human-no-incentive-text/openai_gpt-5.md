# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-27 10:49:48

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
| sudoku_game | 5311 | 40960 | 46271 | 0 | 20 | 52.50 | 1049.98 |
| add_numbers | 3060 | 4881 | 7941 | 20 | 0 | 8.61 | 172.14 |
| counting_zeros | 4460 | 40261 | 44721 | 3 | 17 | 50.60 | 1012.0 |
| task_decoding | 4400 | 8266 | 12666 | 20 | 0 | 9.12 | 182.43 |
| task_summation | 4740 | 16371 | 21111 | 20 | 0 | 14.41 | 288.21 |
| task_transcription | 3036 | 4599 | 7635 | 19 | 1 | 11.08 | 221.63 |
| task_sequences | 3061 | 14057 | 17118 | 16 | 4 | 19.91 | 398.31 |
| string_entry | 3320 | 27437 | 30757 | 13 | 7 | 35.01 | 700.13 |
| **TOTAL** | **31388** | **156832** | **188220** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 2 3 2 3 2 1 6 2 4 5 4 6 2 |  | No | 54.35 |
| 2 | 6 3 4 6 5 2 4 1 1 6 2 4 1 3 |  | No | 51.61 |
| 3 | 5 4 4 6 1 2 5 6 4 3 6 3 6 5 |  | No | 65.71 |
| 4 | 3 1 5 3 5 3 2 1 6 6 1 4 2 6 |  | No | 52.02 |
| 5 | 2 1 4 2 4 5 2 2 3 2 5 4 4 5 |  | No | 57.8 |
| 6 | 2 3 6 5 1 4 6 3 2 4 1 4 2 3 |  | No | 47.59 |
| 7 | 5 2 1 5 1 4 2 2 6 4 2 5 6 3 |  | No | 65.01 |
| 8 | 2 5 3 2 6 5 2 6 2 3 4 6 3 5 |  | No | 45.81 |
| 9 | 1 2 5 3 5 1 2 1 3 2 5 5 2 3 |  | No | 39.73 |
| 10 | 4 5 3 2 1 2 1 6 1 3 1 2 4 2 |  | No | 56.14 |
| 11 | 5 4 6 6 3 5 1 6 3 1 3 6 4 1 |  | No | 39.63 |
| 12 | 6 1 5 2 4 3 5 4 2 4 5 1 4 2 |  | No | 53.07 |
| 13 | 3 2 6 6 2 3 1 5 2 3 6 5 1 3 |  | No | 51.85 |
| 14 | 1 6 4 3 6 5 3 5 1 6 1 5 2 5 |  | No | 59.77 |
| 15 | 1 6 4 4 1 2 2 4 1 1 6 5 5 3 |  | No | 66.76 |
| 16 | 6 1 2 1 5 6 2 3 5 4 2 3 2 1 |  | No | 57.07 |
| 17 | 1 3 1 2 5 3 6 2 3 5 2 4 6 3 |  | No | 38.02 |
| 18 | 1 3 1 6 6 6 4 1 1 5 4 4 6 1 |  | No | 44.55 |
| 19 | 3 6 4 1 4 6 5 2 3 6 5 1 1 4 |  | No | 48.93 |
| 20 | 5 1 6 4 5 6 3 4 4 5 2 2 6 1 |  | No | 54.52 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1710 | 1710 | Yes | 6.61 |
| 2 | 1350 | 1350 | Yes | 8.93 |
| 3 | 1511 | 1511 | Yes | 5.18 |
| 4 | 2158 | 2158 | Yes | 22.73 |
| 5 | 1066 | 1066 | Yes | 6.58 |
| 6 | 2226 | 2226 | Yes | 6.44 |
| 7 | 1265 | 1265 | Yes | 10.33 |
| 8 | 1427 | 1427 | Yes | 5.43 |
| 9 | 1919 | 1919 | Yes | 10.12 |
| 10 | 1514 | 1514 | Yes | 13.52 |
| 11 | 953 | 953 | Yes | 3.02 |
| 12 | 1387 | 1387 | Yes | 7.39 |
| 13 | 1555 | 1555 | Yes | 5.19 |
| 14 | 1371 | 1371 | Yes | 12.49 |
| 15 | 1493 | 1493 | Yes | 11.55 |
| 16 | 955 | 955 | Yes | 6.95 |
| 17 | 2767 | 2767 | Yes | 3.01 |
| 18 | 862 | 862 | Yes | 6.15 |
| 19 | 1850 | 1850 | Yes | 6.78 |
| 20 | 948 | 948 | Yes | 13.72 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 |  | No | 68.95 |
| 2 | 65 | 65 | Yes | 30.16 |
| 3 | 74 |  | No | 68.32 |
| 4 | 73 |  | No | 64.25 |
| 5 | 51 | 51 | Yes | 25.28 |
| 6 | 38 |  | No | 52.3 |
| 7 | 70 |  | No | 58.78 |
| 8 | 48 |  | No | 55.26 |
| 9 | 54 |  | No | 47.31 |
| 10 | 55 |  | No | 45.53 |
| 11 | 43 |  | No | 44.28 |
| 12 | 37 |  | No | 47.24 |
| 13 | 36 |  | No | 59.68 |
| 14 | 71 |  | No | 39.81 |
| 15 | 36 |  | No | 43.95 |
| 16 | 72 | 72 | Yes | 25.32 |
| 17 | 53 |  | No | 47.73 |
| 18 | 42 |  | No | 64.49 |
| 19 | 39 |  | No | 61.41 |
| 20 | 74 |  | No | 61.93 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CTLUWSB | CTLUWSB | Yes | 12.3 |
| 2 | RAHUVQW | RAHUVQW | Yes | 9.34 |
| 3 | YEBLZKG | YEBLZKG | Yes | 8.32 |
| 4 | DRAYMVU | DRAYMVU | Yes | 9.71 |
| 5 | FRYCZBQ | FRYCZBQ | Yes | 9.89 |
| 6 | BMSAIWQ | BMSAIWQ | Yes | 9.67 |
| 7 | SXRPJZQ | SXRPJZQ | Yes | 9.54 |
| 8 | ABVPFYR | ABVPFYR | Yes | 9.64 |
| 9 | XMSIKAL | XMSIKAL | Yes | 7.61 |
| 10 | EXCHNAS | EXCHNAS | Yes | 10.64 |
| 11 | EYGFLBU | EYGFLBU | Yes | 8.61 |
| 12 | EQYZAVU | EQYZAVU | Yes | 7.66 |
| 13 | RPYBDXN | RPYBDXN | Yes | 8.17 |
| 14 | RNPHOKL | RNPHOKL | Yes | 8.59 |
| 15 | GIWCOYM | GIWCOYM | Yes | 7.81 |
| 16 | AZUXJMI | AZUXJMI | Yes | 7.19 |
| 17 | XKOILQU | XKOILQU | Yes | 6.97 |
| 18 | WJKPDFM | WJKPDFM | Yes | 8.61 |
| 19 | BFEUMYI | BFEUMYI | Yes | 8.78 |
| 20 | LISAYWE | LISAYWE | Yes | 13.37 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.8, 9.2] | 9.2 0.8 | Yes | 12.3 |
| 2 | [0.2, 9.8] | 9.8 0.2 | Yes | 22.35 |
| 3 | [4.7, 5.3] | 4.7 5.3 | Yes | 13.93 |
| 4 | [3.2, 6.8] | 3.2 6.8 | Yes | 12.4 |
| 5 | [0.7, 9.3] | 0.7 9.3 | Yes | 13.43 |
| 6 | [1.8, 8.2] | 1.8 8.2 | Yes | 17.3 |
| 7 | [2.7, 7.3] | 2.7 7.3 | Yes | 17.43 |
| 8 | [2.4, 7.6] | 7.6 2.4 | Yes | 11.03 |
| 9 | [3.0, 7.0] | 7.0 3.0 | Yes | 15.61 |
| 10 | [2.0, 8.0] | 8.0 2.0 | Yes | 13.02 |
| 11 | [0.9, 9.1] | 9.1 0.9 | Yes | 10.94 |
| 12 | [4.3, 5.7] | 4.3 5.7 | Yes | 12.42 |
| 13 | [4.6, 5.4] | 5.4 4.6 | Yes | 11.16 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 21.18 |
| 15 | [2.9, 7.1] | 2.9 7.1 | Yes | 14.15 |
| 16 | [3.3, 6.7] | 3.3 6.7 | Yes | 16.48 |
| 17 | [3.6, 6.4] | 3.6 6.4 | Yes | 12.89 |
| 18 | [2.3, 7.7] | 7.7 2.3 | Yes | 9.17 |
| 19 | [1.5, 8.5] | 8.5 1.5 | Yes | 18.35 |
| 20 | [0.8, 9.2] | 9.2 0.8 | Yes | 12.63 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 661THJ0JASV0 | 661THJ0JASV0 | Yes | 3.69 |
| 2 | PW8G9VWCUO2A | PW8G9VWCUO2A | Yes | 3.84 |
| 3 | AFKFVDREXXCW | AFKFVDREXXCW | Yes | 6.51 |
| 4 | AGLE3R9ZWTLU | AGLE3R9ZWTLU | Yes | 3.57 |
| 5 | TKM95ZSBA01K | TKM95ZSBA01K | Yes | 5.2 |
| 6 | Q983993Q4QXR | Q983993Q4QXR | Yes | 9.95 |
| 7 | GV32WELMW3U4 | GV32WELMW3U4 | Yes | 8.17 |
| 8 | YGDD8NPL476C | YGDD8NPL476C | Yes | 6.91 |
| 9 | COIA2CD3GHDJ | COIA2CD3GHDJ | Yes | 4.16 |
| 10 | D9CCA2SNJYH0 | D9CCA2SNJYH0 | Yes | 2.59 |
| 11 | QVLZ1M3YTJWJ | QVLZ1M3YTJWJ | Yes | 7.74 |
| 12 | VINZPOCVY9V5 | VINZPOCVY9V5 | Yes | 2.92 |
| 13 | W7F62ADJLWHJ | W7F62ADJLWHJ | Yes | 6.92 |
| 14 | 732DAGSCB0MU | 732DAGSCB0MU | Yes | 4.76 |
| 15 | L89U89QHR28G | L89U89QHR28G | Yes | 2.71 |
| 16 | QAI0WTCQEEPE | TIMEOUT | No | 120.03 |
| 17 | TSMYPEUJ9G7I | TSMYPEUJ9G7I | Yes | 6.81 |
| 18 | ITJ6B05SRCRI | ITJ6B05SRCRI | Yes | 6.56 |
| 19 | R79URKC0VVYH | R79URKC0VVYH | Yes | 3.25 |
| 20 | AVLS99AFA3V6 | AVLS99AFA3V6 | Yes | 5.35 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 5 | Yes | 9.2 |
| 2 | 60 | 60 | Yes | 9.14 |
| 3 | 44 | 44 | Yes | 11.77 |
| 4 | 1440 | 1440 | Yes | 7.8 |
| 5 | 16 | 16 | Yes | 6.14 |
| 6 | 4 | 4 | Yes | 4.86 |
| 7 | 10 |  | No | 65.14 |
| 8 | 6 | 6 | Yes | 9.62 |
| 9 | 20 |  | No | 87.52 |
| 10 | 65 | 65 | Yes | 8.07 |
| 11 | 28 | 28 | Yes | 5.69 |
| 12 | 7 | 7 | Yes | 7.12 |
| 13 | 3 | 3 | Yes | 14.1 |
| 14 | 36 | 36 | Yes | 6.36 |
| 15 | 67 | 67 | Yes | 4.76 |
| 16 | 19 | 19 | Yes | 7.18 |
| 17 | 5 |  | No | 57.67 |
| 18 | 60 | 60 | Yes | 16.52 |
| 19 | 4096 |  | No | 51.57 |
| 20 | 73 | 73 | Yes | 8.07 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | //_((/\ ) |  | No | 69.56 |
| 2 | _/<\_ (_( | _/<\_ (_( | Yes | 13.91 |
| 3 | (\)/</\_/ | (\)/</\_/ | Yes | 19.43 |
| 4 | < __ </)< | < __ </)< | Yes | 28.69 |
| 5 | \/_ (_\(_ | \/_ (_\(_ | Yes | 27.37 |
| 6 | _\//// \< | _\//// \< | Yes | 17.66 |
| 7 | \)_\ )( / | \)_\ )( / | Yes | 20.96 |
| 8 | \))_((<_( | \))_((<_( | Yes | 19.15 |
| 9 |   < /(<)) | < /(<)) | No | 29.22 |
| 10 | /\<\\ (<\ | /\<\\ (<\ | Yes | 29.58 |
| 11 | <\<\/(/ / |  | No | 71.41 |
| 12 | )<)  ))(\ | )<)  ))(\ | Yes | 18.28 |
| 13 | (_((<<)_  |  | No | 60.73 |
| 14 |  / )(\ \\ |  | No | 71.88 |
| 15 | /__\)(</( | /__\)(</( | Yes | 15.5 |
| 16 | <) <_/ _  | TIMEOUT | No | 120.03 |
| 17 | \ ((< ()\ | \ ((< ()\ | Yes | 17.3 |
| 18 | /\(//<(</ | /\(//<(</ | Yes | 8.28 |
| 19 | //)/()\<  | //)/()\< | No | 18.88 |
| 20 | < ()//)(( | < ()//)(( | Yes | 22.31 |
