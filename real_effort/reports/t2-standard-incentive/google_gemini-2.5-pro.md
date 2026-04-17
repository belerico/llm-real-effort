# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8904 | 34385 | 43289 | 0 | 20 | 17.99 | 359.99 |
| add_numbers | 34242 | 7455 | 41697 | 20 | 0 | 7.11 | 142.39 |
| counting_zeros | 13150 | 37457 | 50607 | 7 | 13 | 21.10 | 422.26 |
| task_decoding | 45556 | 12399 | 57955 | 17 | 3 | 8.71 | 174.35 |
| task_summation | 26820 | 23554 | 50374 | 20 | 0 | 13.00 | 260.22 |
| task_transcription | 25510 | 10318 | 35828 | 15 | 5 | 8.57 | 171.46 |
| task_sequences | 3006 | 15260 | 18266 | 20 | 0 | 9.81 | 196.19 |
| **TOTAL** | **157188** | **140828** | **298016** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 5 3 4 1 3 4 3 3 1 3 1 4 2 | 3 5 3 4 1 3 4 3 1 3 4 1 2 1 3 2 1 4 | No | 15.51 |
| 2 | 1 5 2 6 4 2 4 1 5 2 6 5 3 2 | 1 5 2 5 2 4 2 1 5 2 5 6 2 5 3 5 2 | No | 15.8 |
| 3 | 4 3 2 2 1 3 2 3 2 1 4 4 3 1 | 4 3 2 2 1 1 3 2 1 3 2 1 4 4 3 1 | No | 27.02 |
| 4 | 5 2 6 4 2 5 6 6 1 3 6 5 6 2 | 2 6 5 6 4 6 2 5 6 1 6 3 1 3 6 2 6 2 5 2 | No | 15.83 |
| 5 | 5 4 1 6 6 4 3 6 4 4 3 5 6 4 | 4 6 1 4 6 4 6 4 3 3 4 5 4 5 | No | 16.18 |
| 6 | 2 1 5 6 4 1 2 6 2 5 1 4 2 3 | 2 1 5 4 6 1 2 6 4 2 5 1 5 2 4 3 3 2 | No | 15.01 |
| 7 | 4 5 3 6 2 1 2 4 6 4 5 3 4 4 | 6 4 2 3 5 4 1 2 6 5 3 4 4 4 | No | 14.73 |
| 8 | 3 4 5 4 6 6 3 5 1 4 3 4 6 1 |  | No | 36.76 |
| 9 | 3 5 1 4 2 1 2 3 1 6 6 2 2 4 |  | No | 20.28 |
| 10 | 2 4 3 1 2 3 1 3 1 4 3 1 4 2 | I'm trying to fill in the grid. I've been focusing on Box 1 and Row 2. I have deduced that R2C1 must be 1. Now I will update the grid and continue.   I'm continuing to solve the puzzle. I've filled in R2C1 with | No | 28.99 |
| 11 | 6 3 5 3 4 2 1 5 6 4 6 4 3 6 | 6 3 5 3 4 2 5 6 4 6 4 3 6 4 3 6 | No | 16.94 |
| 12 | 1 4 1 2 3 5 6 5 6 2 3 1 6 4 | 1 4 1 2 5 6 3 5 6 2 3 1 6 4 4 1 | No | 15.85 |
| 13 | 3 2 6 1 3 2 4 6 1 5 1 4 3 2 | 3 2 6 1 3 2 4 6 1 1 4 5 3 1 2 4 | No | 14.8 |
| 14 | 2 5 1 3 1 4 1 2 1 3 2 4 5 3 | 5 1 1 2 1 2 4 1 2 4 3 2 3 4 1 3 5 3 | No | 15.53 |
| 15 | 3 1 2 2 3 4 4 5 3 1 1 3 3 2 | 3 1 2 2 4 4 3 1 5 3 1 2 3 2 3 | No | 14.92 |
| 16 | 6 4 5 1 3 4 5 6 1 5 3 5 4 3 | 6 4 5 1 3 5 1 3 6 5 1 3 5 3 5 4 | No | 16.23 |
| 17 | 4 1 5 6 6 5 4 1 3 2 1 5 1 3 | 4 6 5 1 5 1 6 4 1 5 3 2 1 5 1 3 | No | 15.85 |
| 18 | 5 4 1 6 5 5 3 2 5 1 3 6 5 4 | 5 4 1 6 5 1 5 3 2 5 1 3 4 5 6 4 1 6 | No | 14.87 |
| 19 | 3 1 6 4 4 3 1 2 2 5 5 5 2 2 | 4 1 6 4 1 3 2 4 2 5 2 5 2 3 5 2 | No | 14.54 |
| 20 | 3 1 4 2 3 1 6 4 3 2 5 5 3 6 | 3 1 4 1 3 6 2 3 2 5 5 3 6 5 6 3 5 | No | 14.16 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1741 | 1741 | Yes | 5.1 |
| 2 | 737 | 737 | Yes | 4.37 |
| 3 | 1617 | 1617 | Yes | 4.57 |
| 4 | 1669 | 1669 | Yes | 5.0 |
| 5 | 825 | 825 | Yes | 16.03 |
| 6 | 2645 | 2645 | Yes | 17.31 |
| 7 | 2236 | 2236 | Yes | 5.55 |
| 8 | 1907 | 1907 | Yes | 5.15 |
| 9 | 1165 | 1165 | Yes | 8.64 |
| 10 | 1482 | 1482 | Yes | 5.27 |
| 11 | 963 | 963 | Yes | 3.85 |
| 12 | 2277 | 2277 | Yes | 6.4 |
| 13 | 1952 | 1952 | Yes | 4.81 |
| 14 | 1411 | 1411 | Yes | 5.36 |
| 15 | 1902 | 1902 | Yes | 6.4 |
| 16 | 1723 | 1723 | Yes | 15.85 |
| 17 | 1664 | 1664 | Yes | 5.21 |
| 18 | 2148 | 2148 | Yes | 5.0 |
| 19 | 1629 | 1629 | Yes | 5.42 |
| 20 | 1600 | 1600 | Yes | 6.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 71 | 70 | No | 14.13 |
| 2 | 46 | 46 | Yes | 17.43 |
| 3 | 75 | 73 | No | 14.68 |
| 4 | 44 | 44 | Yes | 14.23 |
| 5 | 58 | 58 | Yes | 22.48 |
| 6 | 52 |  | No | 36.17 |
| 7 | 50 | 50 | Yes | 13.73 |
| 8 | 68 |  | No | 35.84 |
| 9 | 58 | 58 | Yes | 14.2 |
| 10 | 71 |  | No | 29.93 |
| 11 | 48 |  | No | 25.37 |
| 12 | 68 |  | No | 24.64 |
| 13 | 55 | 54 | No | 16.98 |
| 14 | 42 | 42 | Yes | 17.03 |
| 15 | 49 |  | No | 27.14 |
| 16 | 72 |  | No | 24.72 |
| 17 | 52 | 53 | No | 14.04 |
| 18 | 64 |  | No | 28.01 |
| 19 | 47 | 47 | Yes | 13.58 |
| 20 | 56 | 57 | No | 17.63 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OSCYIUZ | OSCYIUZ | Yes | 6.87 |
| 2 | RBWNHKI | RBWNHKI | Yes | 17.09 |
| 3 | HFXCPSB | HFXCPSB | Yes | 5.7 |
| 4 | NUKXAFI | NUXAFI | No | 12.34 |
| 5 | RDVOELQ | RDVOELQ | Yes | 7.68 |
| 6 | TEPGUMJ | TEPGUMJ | Yes | 16.52 |
| 7 | JHOUADZ | JHOADZ | No | 5.01 |
| 8 | WQLZIPU | WQLZIPU | Yes | 4.7 |
| 9 | CXRNVWP | CXRNVWP | Yes | 15.1 |
| 10 | SAHEDFQ | SAHEDFQ | Yes | 5.75 |
| 11 | WRKHVBQ | WRKHVBQ | Yes | 4.92 |
| 12 | VNFCATJ | VNFCAJT | No | 5.75 |
| 13 | PXOZNLR | PXOZNLR | Yes | 8.18 |
| 14 | ICPJURQ | ICPJURQ | Yes | 22.0 |
| 15 | GYXKHVR | GYXKHVR | Yes | 9.96 |
| 16 | JSITXQB | JSITXQB | Yes | 4.5 |
| 17 | JHUFMKB | JHUFMKB | Yes | 6.77 |
| 18 | GQDWZMU | GQDWZMU | Yes | 4.71 |
| 19 | PFRQISZ | PFRQISZ | Yes | 5.29 |
| 20 | JIRABHY | JIRABHY | Yes | 5.31 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 6.1 3.9 | Yes | 24.45 |
| 2 | [2.3, 7.7] | 2.3 7.7 | Yes | 8.52 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 11.85 |
| 4 | [0.1, 9.9] | 9.9 0.1 | Yes | 12.08 |
| 5 | [0.2, 9.8] | 0.2 9.8 | Yes | 14.13 |
| 6 | [0.5, 9.5] | 9.5 0.5 | Yes | 10.28 |
| 7 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.53 |
| 8 | [2.7, 7.3] | 2.7 7.3 | Yes | 13.49 |
| 9 | [4.8, 5.2] | 5.2 4.8 | Yes | 12.3 |
| 10 | [2.3, 7.7] | 7.7 2.3 | Yes | 7.35 |
| 11 | [1.8, 8.2] | 8.2 1.8 | Yes | 13.4 |
| 12 | [0.6, 9.4] | 9.4 0.6 | Yes | 9.91 |
| 13 | [0.6, 9.4] | 9.4 0.6 | Yes | 13.16 |
| 14 | [2.9, 7.1] | 2.9 7.1 | Yes | 11.16 |
| 15 | [3.9, 6.1] | 6.1 3.9 | Yes | 14.06 |
| 16 | [2.7, 7.3] | 7.3 2.7 | Yes | 8.82 |
| 17 | [0.1, 9.9] | 0.1 9.9 | Yes | 10.81 |
| 18 | [3.4, 6.6] | 3.4 6.6 | Yes | 17.96 |
| 19 | [4.4, 5.6] | 5.6 4.4 | Yes | 13.64 |
| 20 | [1.1, 8.9] | 1.1 8.9 | Yes | 23.1 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BW4ZI139GF48 | BW4ZI139GF48 | Yes | 7.04 |
| 2 | GZPEO1S0ACYE | GZPE01S0ACYE | No | 16.76 |
| 3 | ULOJNRE2N609 | ULOJNRE2N609 | Yes | 6.4 |
| 4 | ADLM8UPKHVET | ADLM8UPKHVET | Yes | 8.92 |
| 5 | IPYF64Q5HDMM | IPYF64Q5HDMM | Yes | 5.66 |
| 6 | KO7ISJYH29JK | K07ISJYH29JK | No | 4.97 |
| 7 | P4EB0Z5NA1O5 | P4EB0Z5NA105 | No | 5.41 |
| 8 | DU508BYSPAXJ | DU508BYSPAXJ | Yes | 17.03 |
| 9 | CABGNBWVHAZN | CABGNBWVHAZN | Yes | 11.08 |
| 10 | 38OSYWS8XWIF | 380SYWS8XWIF | No | 6.67 |
| 11 | BOGWUBPZGHA4 | BOGWUBPZGHA4 | Yes | 16.1 |
| 12 | LXQFDW9VFWQJ | LXQFDW9VFWQJ | Yes | 6.52 |
| 13 | 8BCI6VEPYFDM | 8BCI6VEPYFDM | Yes | 6.59 |
| 14 | BDV9HE504G17 | BDV9HE504G17 | Yes | 5.25 |
| 15 | 2SJINFXZSOD4 | 2SJINFXZSOD4 | Yes | 5.68 |
| 16 | DET4I1E34IMH | DET4I1E34IMH | Yes | 13.92 |
| 17 | H41FTY8D4C6Q | H41FTY8D4C6Q | Yes | 6.67 |
| 18 | 6JDML6QYO9WD | 6JDML6QY09WD | No | 7.55 |
| 19 | H9NV2F2K4QYY | H9NV2F2K4QYY | Yes | 5.61 |
| 20 | ZEQY68ZA303G | ZEQY68ZA303G | Yes | 7.53 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 9.04 |
| 2 | 10 | 10 | Yes | 13.95 |
| 3 | 20 | 20 | Yes | 14.65 |
| 4 | 64 | 64 | Yes | 10.36 |
| 5 | 9 | 9 | Yes | 8.95 |
| 6 | 19 | 19 | Yes | 12.73 |
| 7 | 31 | 31 | Yes | 16.49 |
| 8 | 4 | 4 | Yes | 10.92 |
| 9 | 793 | 793 | Yes | 13.24 |
| 10 | 3 | 3 | Yes | 9.14 |
| 11 | 60 | 60 | Yes | 7.2 |
| 12 | 243 | 243 | Yes | 7.72 |
| 13 | 36 | 36 | Yes | 7.01 |
| 14 | 73 | 73 | Yes | 5.79 |
| 15 | 7 | 7 | Yes | 6.43 |
| 16 | 44 | 44 | Yes | 6.94 |
| 17 | 23 | 23 | Yes | 6.25 |
| 18 | 48 | 48 | Yes | 16.95 |
| 19 | 28 | 28 | Yes | 6.3 |
| 20 | 67 | 67 | Yes | 6.13 |
