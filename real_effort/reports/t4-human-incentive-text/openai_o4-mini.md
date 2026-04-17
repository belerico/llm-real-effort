# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-27 10:29:24

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
| sudoku_game | 5217 | 38912 | 44129 | 0 | 20 | 41.65 | 833.11 |
| add_numbers | 3240 | 3457 | 6697 | 20 | 0 | 2.92 | 58.34 |
| counting_zeros | 4640 | 40771 | 45411 | 3 | 17 | 32.43 | 648.7 |
| task_decoding | 4580 | 8456 | 13036 | 20 | 0 | 6.49 | 129.71 |
| task_summation | 4920 | 17247 | 22167 | 19 | 1 | 11.66 | 233.18 |
| task_transcription | 3387 | 3184 | 6571 | 20 | 0 | 3.41 | 68.17 |
| task_sequences | 3079 | 12551 | 15630 | 15 | 5 | 16.21 | 324.12 |
| string_entry | 3682 | 34936 | 38618 | 2 | 18 | 24.60 | 492.1 |
| **TOTAL** | **32745** | **159514** | **192259** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 2 5 4 5 3 2 3 5 2 5 4 1 |  | No | 46.41 |
| 2 | 1 2 4 4 1 2 2 4 3 2 3 2 1 5 |  | No | 31.52 |
| 3 | 4 2 1 4 2 4 5 3 6 3 5 6 4 2 |  | No | 38.0 |
| 4 | 5 2 4 4 1 1 5 4 6 2 6 4 2 1 |  | No | 22.68 |
| 5 | 2 3 4 6 4 1 5 6 2 5 1 6 3 4 |  | No | 19.27 |
| 6 | 2 6 4 3 1 3 4 5 1 2 5 2 5 4 |  | No | 41.96 |
| 7 | 6 5 2 5 1 3 6 3 3 1 2 1 4 2 |  | No | 51.31 |
| 8 | 5 3 5 6 4 6 2 5 5 1 3 6 4 2 |  | No | 41.81 |
| 9 | 2 6 3 5 4 1 6 1 2 4 5 3 2 4 | TIMEOUT | No | 120.03 |
| 10 | 1 2 5 6 3 4 6 4 3 2 6 4 3 2 |  | No | 36.86 |
| 11 | 2 6 6 2 1 5 1 2 6 5 4 3 2 1 |  | No | 42.62 |
| 12 | 1 5 6 4 6 2 2 5 5 3 1 4 5 1 |  | No | 42.55 |
| 13 | 2 3 2 6 3 5 5 4 3 6 4 5 4 3 |  | No | 42.17 |
| 14 | 3 4 2 5 3 1 3 4 1 2 4 2 3 1 |  | No | 39.72 |
| 15 | 4 6 2 3 5 1 6 2 1 3 5 3 4 4 |  | No | 47.4 |
| 16 | 5 3 5 4 3 6 5 2 6 4 3 5 5 2 |  | No | 22.38 |
| 17 | 4 1 4 3 6 4 4 5 3 5 4 6 3 1 |  | No | 36.66 |
| 18 | 1 5 1 2 5 3 4 1 4 2 5 1 2 3 |  | No | 36.26 |
| 19 | 5 2 6 3 1 3 2 5 3 2 1 5 4 1 |  | No | 27.45 |
| 20 | 2 1 3 1 4 3 4 2 5 6 1 3 4 2 |  | No | 46.02 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1224 | 1224 | Yes | 2.41 |
| 2 | 1806 | 1806 | Yes | 4.3 |
| 3 | 1984 | 1984 | Yes | 2.4 |
| 4 | 1853 | 1853 | Yes | 2.24 |
| 5 | 908 | 908 | Yes | 3.19 |
| 6 | 1978 | 1978 | Yes | 3.1 |
| 7 | 2079 | 2079 | Yes | 2.46 |
| 8 | 1091 | 1091 | Yes | 2.3 |
| 9 | 1370 | 1370 | Yes | 3.62 |
| 10 | 1440 | 1440 | Yes | 2.92 |
| 11 | 2475 | 2475 | Yes | 2.79 |
| 12 | 1708 | 1708 | Yes | 2.12 |
| 13 | 1910 | 1910 | Yes | 2.92 |
| 14 | 1841 | 1841 | Yes | 3.19 |
| 15 | 2258 | 2258 | Yes | 2.68 |
| 16 | 1125 | 1125 | Yes | 2.7 |
| 17 | 905 | 905 | Yes | 6.22 |
| 18 | 894 | 894 | Yes | 2.07 |
| 19 | 1057 | 1057 | Yes | 2.68 |
| 20 | 1905 | 1905 | Yes | 2.0 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 |  | No | 24.71 |
| 2 | 51 |  | No | 18.35 |
| 3 | 36 |  | No | 32.25 |
| 4 | 37 | 37 | Yes | 17.89 |
| 5 | 73 |  | No | 21.51 |
| 6 | 41 | 41 | Yes | 25.25 |
| 7 | 42 |  | No | 26.68 |
| 8 | 70 |  | No | 37.73 |
| 9 | 67 |  | No | 37.3 |
| 10 | 43 |  | No | 39.61 |
| 11 | 49 |  | No | 28.35 |
| 12 | 38 | 38 | Yes | 16.41 |
| 13 | 65 |  | No | 45.95 |
| 14 | 50 |  | No | 43.56 |
| 15 | 73 |  | No | 35.56 |
| 16 | 68 |  | No | 24.83 |
| 17 | 39 |  | No | 46.33 |
| 18 | 69 |  | No | 34.88 |
| 19 | 75 |  | No | 52.49 |
| 20 | 68 |  | No | 39.04 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LQJCUSW | LQJCUSW | Yes | 9.12 |
| 2 | WESMTKL | WESMTKL | Yes | 9.49 |
| 3 | TPLSIVU | TPLSIVU | Yes | 4.03 |
| 4 | JXWZLHD | JXWZLHD | Yes | 4.44 |
| 5 | BPXTDEG | BPXTDEG | Yes | 4.04 |
| 6 | KVDPURJ | KVDPURJ | Yes | 7.23 |
| 7 | QNKDWRV | QNKDWRV | Yes | 13.61 |
| 8 | GMQLEID | GMQLEID | Yes | 8.82 |
| 9 | RJCPUEI | RJCPUEI | Yes | 3.78 |
| 10 | YETAXOZ | YETAXOZ | Yes | 8.06 |
| 11 | RSFNJHP | RSFNJHP | Yes | 5.23 |
| 12 | JVWDCLZ | JVWDCLZ | Yes | 3.3 |
| 13 | ZFPVUCB | ZFPVUCB | Yes | 6.52 |
| 14 | TNBQKSA | TNBQKSA | Yes | 8.23 |
| 15 | XMPTAQV | XMPTAQV | Yes | 3.89 |
| 16 | KUFYCWM | KUFYCWM | Yes | 9.4 |
| 17 | NILUGFX | NILUGFX | Yes | 3.3 |
| 18 | ZLPDRJI | ZLPDRJI | Yes | 5.04 |
| 19 | VGLQBCX | VGLQBCX | Yes | 3.07 |
| 20 | AUSCBYR | AUSCBYR | Yes | 9.11 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.9, 7.1] | 7.1 2.9 | Yes | 8.36 |
| 2 | [1.7, 8.3] | 8.3 1.7 | Yes | 8.17 |
| 3 | [0.7, 9.3] | 9.3 0.7 | Yes | 14.54 |
| 4 | [1.0, 9.0] | 1.0 9.0 | Yes | 10.45 |
| 5 | [0.1, 9.9] | 9.9 0.1 | Yes | 9.83 |
| 6 | [3.4, 6.6] |  | No | 30.58 |
| 7 | [3.2, 6.8] | 3.2 6.8 | Yes | 12.69 |
| 8 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.88 |
| 9 | [2.7, 7.3] | 2.7 7.3 | Yes | 8.22 |
| 10 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.52 |
| 11 | [3.3, 6.7] | 3.3 6.7 | Yes | 11.87 |
| 12 | [3.0, 7.0] | 3.0 7.0 | Yes | 9.53 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.15 |
| 14 | [3.8, 6.2] | 3.8 6.2 | Yes | 11.84 |
| 15 | [4.2, 5.8] | 5.8 4.2 | Yes | 10.67 |
| 16 | [1.9, 8.1] | 1.9 8.1 | Yes | 11.4 |
| 17 | [2.8, 7.2] | 7.2 2.8 | Yes | 8.63 |
| 18 | [0.9, 9.1] | 0.9 9.1 | Yes | 13.26 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 9.54 |
| 20 | [0.1, 9.9] | 9.9 0.1 | Yes | 11.06 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JE0K1G1Y3ZFL | JE0K1G1Y3ZFL | Yes | 2.39 |
| 2 | EZ1L2RHMOVHL | EZ1L2RHMOVHL | Yes | 11.25 |
| 3 | 9PEBDKB5GJ0W | 9PEBDKB5GJ0W | Yes | 2.32 |
| 4 | YOK475PZBMKI | YOK475PZBMKI | Yes | 2.04 |
| 5 | JK1Y5X3E4JOH | JK1Y5X3E4JOH | Yes | 2.89 |
| 6 | PA34DP5EMS5V | PA34DP5EMS5V | Yes | 1.93 |
| 7 | GNRJCJZ9KB9S | GNRJCJZ9KB9S | Yes | 3.24 |
| 8 | SXKVYFVX9IR7 | SXKVYFVX9IR7 | Yes | 1.71 |
| 9 | 3F1EINGBR80O | 3F1EINGBR80O | Yes | 3.68 |
| 10 | 9KFAX44VB8DL | 9KFAX44VB8DL | Yes | 2.47 |
| 11 | PRS7AOUDXYTM | PRS7AOUDXYTM | Yes | 2.56 |
| 12 | H0W6Z6FAJS4X | H0W6Z6FAJS4X | Yes | 2.7 |
| 13 | LRITM6CPV5FQ | LRITM6CPV5FQ | Yes | 3.26 |
| 14 | 9835G1QMGW7W | 9835G1QMGW7W | Yes | 2.89 |
| 15 | R8WC9YK9HVWV | R8WC9YK9HVWV | Yes | 2.47 |
| 16 | ZYJZDOF3TMOE | ZYJZDOF3TMOE | Yes | 2.95 |
| 17 | FLQKPF3Q8YY5 | FLQKPF3Q8YY5 | Yes | 8.12 |
| 18 | CLELB7GPGW7C | CLELB7GPGW7C | Yes | 4.3 |
| 19 | DBEMAT1LP0YU | DBEMAT1LP0YU | Yes | 2.22 |
| 20 | K0YTI1CSAXKJ | K0YTI1CSAXKJ | Yes | 2.77 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 3.01 |
| 2 | 5 |  | No | 43.72 |
| 3 | 20 | 20 | Yes | 16.45 |
| 4 | 28 | 28 | Yes | 8.89 |
| 5 | 65 | 65 | Yes | 5.5 |
| 6 | 243 | 243 | Yes | 2.72 |
| 7 | 1 | 42 | No | 3.73 |
| 8 | 793 | TIMEOUT | No | 120.02 |
| 9 | 4096 |  | No | 39.04 |
| 10 | 44 | 44 | Yes | 6.37 |
| 11 | 48 | 42 | No | 6.62 |
| 12 | 60 | 60 | Yes | 11.07 |
| 13 | 9 | 9 | Yes | 8.14 |
| 14 | 60 | 60 | Yes | 4.65 |
| 15 | 19 | 19 | Yes | 9.22 |
| 16 | 3 | 3 | Yes | 10.09 |
| 17 | 16 | 16 | Yes | 6.21 |
| 18 | 63 | 63 | Yes | 6.66 |
| 19 | 67 | 67 | Yes | 8.59 |
| 20 | 36 | 36 | Yes | 3.41 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | __()) <)< | __()) <)< | Yes | 7.69 |
| 2 | \<_( \\)_ |  | No | 24.47 |
| 3 | _\)__ )\  |  | No | 59.46 |
| 4 | )(_)<__ _ |  | No | 50.05 |
| 5 | <(/\< ___ |  | No | 39.29 |
| 6 | /\\/ )_)_ | /\\/ )_)_ | Yes | 16.48 |
| 7 | _((__//// | /\) <(_<) | No | 14.03 |
| 8 | _  )//((  | _  )//(( | No | 9.94 |
| 9 |  (/\/ /<< |  | No | 18.92 |
| 10 | )_\\(/(/_ |  | No | 24.38 |
| 11 | \_\_ )_ ( |  | No | 21.77 |
| 12 | <_/ () _/ |  | No | 22.95 |
| 13 | _<<((<( ) |  | No | 41.11 |
| 14 | << \\< _) |  | No | 25.94 |
| 15 | _ (< _( ) |  | No | 24.61 |
| 16 |   < </</  |  | No | 35.0 |
| 17 | ___ (_<<( | ___ (_<< | No | 5.5 |
| 18 | __/)/<</< |  | No | 22.66 |
| 19 | \_)_/\ _( | /\) <(_<) | No | 11.54 |
| 20 | _\ _<<<\) | /\) <(_<) | No | 16.31 |
