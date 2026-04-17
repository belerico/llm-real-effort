# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-26 16:00:16

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
| sudoku_game | 4672 | 40960 | 45632 | 0 | 20 | 35.80 | 716.13 |
| add_numbers | 2420 | 3133 | 5553 | 20 | 0 | 2.87 | 57.49 |
| counting_zeros | 3820 | 40850 | 44670 | 1 | 19 | 26.42 | 528.35 |
| task_decoding | 3760 | 9334 | 13094 | 20 | 0 | 7.14 | 142.87 |
| task_summation | 4100 | 18000 | 22100 | 19 | 1 | 12.24 | 244.74 |
| task_transcription | 2559 | 2822 | 5381 | 20 | 0 | 2.43 | 48.62 |
| task_sequences | 2421 | 14949 | 17370 | 17 | 3 | 12.11 | 242.14 |
| string_entry | 2704 | 32807 | 35511 | 3 | 17 | 22.55 | 451.03 |
| **TOTAL** | **26456** | **162855** | **189311** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 5 6 2 1 5 6 2 5 3 1 4 6 1 |  | No | 27.28 |
| 2 | 4 3 6 1 3 1 3 2 5 4 3 5 2 4 |  | No | 39.77 |
| 3 | 2 3 5 5 2 3 3 4 5 6 1 3 5 4 |  | No | 29.82 |
| 4 | 5 6 1 3 3 2 6 4 1 3 1 2 3 5 |  | No | 40.68 |
| 5 | 2 6 5 4 5 2 1 1 2 3 5 5 2 5 |  | No | 27.21 |
| 6 | 1 5 4 6 1 4 1 3 3 4 5 4 2 1 |  | No | 23.94 |
| 7 | 4 2 2 5 4 6 3 1 4 1 1 1 5 2 |  | No | 42.82 |
| 8 | 4 1 1 3 3 5 2 4 4 5 3 2 2 1 |  | No | 34.02 |
| 9 | 4 5 3 2 6 3 3 6 2 2 1 3 5 5 |  | No | 34.36 |
| 10 | 2 3 1 4 3 1 3 6 3 2 4 2 6 1 |  | No | 41.93 |
| 11 | 1 3 2 6 6 4 2 5 2 5 1 3 6 5 |  | No | 37.89 |
| 12 | 1 2 1 4 6 3 6 2 2 5 1 6 1 2 |  | No | 43.31 |
| 13 | 3 2 4 1 2 5 5 2 4 6 2 6 1 5 |  | No | 36.22 |
| 14 | 6 2 3 4 3 5 4 3 4 1 6 5 3 4 |  | No | 40.27 |
| 15 | 4 3 6 1 3 4 1 5 2 6 1 3 2 4 |  | No | 43.0 |
| 16 | 1 6 3 5 1 5 2 5 5 3 2 4 2 6 |  | No | 30.63 |
| 17 | 2 4 2 1 3 2 4 5 3 5 1 4 3 2 |  | No | 24.43 |
| 18 | 1 2 5 6 2 2 4 1 6 2 4 6 3 2 |  | No | 38.82 |
| 19 | 4 6 2 3 6 2 3 2 5 1 6 3 4 2 |  | No | 39.84 |
| 20 | 4 2 6 1 1 3 5 6 5 1 3 6 5 4 |  | No | 39.83 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1483 | 1483 | Yes | 2.44 |
| 2 | 2207 | 2207 | Yes | 4.28 |
| 3 | 842 | 842 | Yes | 2.3 |
| 4 | 1106 | 1106 | Yes | 2.6 |
| 5 | 1791 | 1791 | Yes | 6.05 |
| 6 | 1027 | 1027 | Yes | 2.09 |
| 7 | 1720 | 1720 | Yes | 2.1 |
| 8 | 936 | 936 | Yes | 2.27 |
| 9 | 1333 | 1333 | Yes | 2.57 |
| 10 | 1334 | 1334 | Yes | 4.18 |
| 11 | 1979 | 1979 | Yes | 2.04 |
| 12 | 1645 | 1645 | Yes | 2.37 |
| 13 | 1495 | 1495 | Yes | 2.03 |
| 14 | 991 | 991 | Yes | 2.8 |
| 15 | 1755 | 1755 | Yes | 2.21 |
| 16 | 1493 | 1493 | Yes | 2.43 |
| 17 | 1802 | 1802 | Yes | 2.42 |
| 18 | 1735 | 1735 | Yes | 5.05 |
| 19 | 1082 | 1082 | Yes | 2.19 |
| 20 | 1397 | 1397 | Yes | 3.05 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 43 |  | No | 32.64 |
| 2 | 47 |  | No | 29.37 |
| 3 | 66 |  | No | 31.32 |
| 4 | 59 |  | No | 19.69 |
| 5 | 64 |  | No | 19.22 |
| 6 | 39 |  | No | 27.88 |
| 7 | 44 |  | No | 32.86 |
| 8 | 59 |  | No | 25.75 |
| 9 | 59 |  | No | 33.42 |
| 10 | 48 | 48 | Yes | 16.27 |
| 11 | 55 |  | No | 25.38 |
| 12 | 59 |  | No | 26.36 |
| 13 | 46 |  | No | 34.37 |
| 14 | 45 |  | No | 21.82 |
| 15 | 74 |  | No | 31.85 |
| 16 | 73 |  | No | 32.74 |
| 17 | 47 |  | No | 24.2 |
| 18 | 39 |  | No | 23.01 |
| 19 | 64 |  | No | 19.96 |
| 20 | 40 |  | No | 20.22 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LYURHQT | LYURHQT | Yes | 5.26 |
| 2 | JZSKXNU | JZSKXNU | Yes | 8.14 |
| 3 | EKRNQML | EKRNQML | Yes | 3.52 |
| 4 | NEQVKRP | NEQVKRP | Yes | 3.96 |
| 5 | TIBCSRD | TIBCSRD | Yes | 3.92 |
| 6 | KPZEQAH | KPZEQAH | Yes | 6.03 |
| 7 | QTCAEMW | QTCAEMW | Yes | 9.85 |
| 8 | NCWYMJL | NCWYMJL | Yes | 7.94 |
| 9 | VSOMUAP | VSOMUAP | Yes | 2.38 |
| 10 | KDRFWBP | KDRFWBP | Yes | 3.16 |
| 11 | EHTPURB | EHTPURB | Yes | 10.12 |
| 12 | LUYONEB | LUYONEB | Yes | 13.65 |
| 13 | ANIVWEQ | ANIVWEQ | Yes | 5.2 |
| 14 | UEQDPMX | UEQDPMX | Yes | 3.88 |
| 15 | XULFDZY | XULFDZY | Yes | 8.33 |
| 16 | BDLRIUH | BDLRIUH | Yes | 12.23 |
| 17 | LMYQRUS | LMYQRUS | Yes | 4.57 |
| 18 | YNUQJAP | YNUQJAP | Yes | 11.38 |
| 19 | ZETYMXU | ZETYMXU | Yes | 7.4 |
| 20 | FXBCYLM | FXBCYLM | Yes | 11.95 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] |  | No | 27.97 |
| 2 | [1.3, 8.7] | 8.7 1.3 | Yes | 8.5 |
| 3 | [4.4, 5.6] | 4.4 5.6 | Yes | 12.61 |
| 4 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.14 |
| 5 | [2.1, 7.9] | 7.9 2.1 | Yes | 10.24 |
| 6 | [0.7, 9.3] | 0.7 9.3 | Yes | 10.14 |
| 7 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.67 |
| 8 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.7 |
| 9 | [2.9, 7.1] | 2.9 7.1 | Yes | 24.14 |
| 10 | [4.1, 5.9] | 4.1 5.9 | Yes | 16.8 |
| 11 | [1.9, 8.1] | 8.1 1.9 | Yes | 10.87 |
| 12 | [2.1, 7.9] | 2.1 7.9 | Yes | 14.13 |
| 13 | [1.3, 8.7] | 1.3 8.7 | Yes | 8.18 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.0 |
| 15 | [4.9, 5.1] | 4.9 5.1 | Yes | 12.63 |
| 16 | [1.3, 8.7] | 1.3 8.7 | Yes | 14.15 |
| 17 | [3.9, 6.1] | 3.9 6.1 | Yes | 8.86 |
| 18 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.38 |
| 19 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.15 |
| 20 | [2.8, 7.2] | 7.2 2.8 | Yes | 9.48 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 8YTHXV47D5X4 | 8YTHXV47D5X4 | Yes | 3.71 |
| 2 | VXS0H1IPUYED | VXS0H1IPUYED | Yes | 3.55 |
| 3 | LAJEDFLWQQAI | LAJEDFLWQQAI | Yes | 2.03 |
| 4 | XUICHBJTFPS9 | XUICHBJTFPS9 | Yes | 1.93 |
| 5 | 1MRT3IJ9W235 | 1MRT3IJ9W235 | Yes | 1.92 |
| 6 | ZIVCVL4EOEEJ | ZIVCVL4EOEEJ | Yes | 1.87 |
| 7 | ZP43HTHDL463 | ZP43HTHDL463 | Yes | 2.14 |
| 8 | LXH9WYFC3RFS | LXH9WYFC3RFS | Yes | 1.94 |
| 9 | S9KBRNQJ9AIC | S9KBRNQJ9AIC | Yes | 1.87 |
| 10 | JU19H6LEMNTI | JU19H6LEMNTI | Yes | 2.45 |
| 11 | PILLX8NYQ0J7 | PILLX8NYQ0J7 | Yes | 1.82 |
| 12 | 9KUQR7JD7TA1 | 9KUQR7JD7TA1 | Yes | 2.15 |
| 13 | LR0VRY3QV8C1 | LR0VRY3QV8C1 | Yes | 2.1 |
| 14 | ZZGG0XWNVWU9 | ZZGG0XWNVWU9 | Yes | 2.9 |
| 15 | Z0832ZOLUSB4 | Z0832ZOLUSB4 | Yes | 2.56 |
| 16 | YUMYNNBI8GDB | YUMYNNBI8GDB | Yes | 2.33 |
| 17 | 4CEYIRSGKA15 | 4CEYIRSGKA15 | Yes | 4.01 |
| 18 | 414YDO0ESY9N | 414YDO0ESY9N | Yes | 1.85 |
| 19 | 9NR2H5ZKR67E | 9NR2H5ZKR67E | Yes | 2.42 |
| 20 | KWLEHDOOY9NE | KWLEHDOOY9NE | Yes | 3.04 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 4.75 |
| 2 | 20 |  | No | 37.72 |
| 3 | 4096 |  | No | 38.61 |
| 4 | 1 | 1 | Yes | 15.5 |
| 5 | 5 |  | No | 40.84 |
| 6 | 60 | 60 | Yes | 2.68 |
| 7 | 5 | 5 | Yes | 3.65 |
| 8 | 63 | 63 | Yes | 6.11 |
| 9 | 7 | 7 | Yes | 3.52 |
| 10 | 73 | 73 | Yes | 8.46 |
| 11 | 44 | 44 | Yes | 6.76 |
| 12 | 6 | 6 | Yes | 3.42 |
| 13 | 10 | 10 | Yes | 13.72 |
| 14 | 60 | 60 | Yes | 7.51 |
| 15 | 4 | 4 | Yes | 7.28 |
| 16 | 9 | 9 | Yes | 9.85 |
| 17 | 48 | 48 | Yes | 7.05 |
| 18 | 9 | 9 | Yes | 9.38 |
| 19 | 64 | 64 | Yes | 11.36 |
| 20 | 28 | 28 | Yes | 3.95 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | __\\/_()_ | __\\/_()_ | Yes | 8.39 |
| 2 | <\)/\)\)( |  | No | 25.87 |
| 3 |  )/(<\ (< | )/(<\ (< | No | 13.92 |
| 4 | /_)()<(<\ |  | No | 56.43 |
| 5 | /\((// /\ | /\((// /\ | Yes | 14.16 |
| 6 | )\(  )))) | /\) <(_<) | No | 14.13 |
| 7 | </) /<(\\ | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 16.44 |
| 8 | _\///<))_ | /\) <(_< | No | 17.27 |
| 9 | )\//  ___ |  | No | 26.21 |
| 10 |   </\(/() |  | No | 19.89 |
| 11 | \ /_ (<   | /_ (< | No | 6.61 |
| 12 | \ < _<<_\ |  | No | 45.62 |
| 13 | (_( <\\<_ |  | No | 28.03 |
| 14 | /\ _ ((__ | /\ _ ((__ | Yes | 16.78 |
| 15 | )/\()<\)( |  | No | 23.62 |
| 16 | )(_<<<\(_ | /\) <(_<) | No | 20.99 |
| 17 | )()<)(//) | /\) <(_<) | No | 14.67 |
| 18 | /__((\()< |  | No | 27.76 |
| 19 | \\(\))/\_ |  | No | 40.27 |
| 20 | <<\\// /( | \\// /( | No | 13.96 |
