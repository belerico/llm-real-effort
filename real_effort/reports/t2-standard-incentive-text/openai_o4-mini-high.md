# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-27 10:25:46

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
| sudoku_game | 5144 | 40960 | 46104 | 0 | 20 | 42.34 | 846.78 |
| add_numbers | 2900 | 3199 | 6099 | 20 | 0 | 2.77 | 55.52 |
| counting_zeros | 4300 | 40662 | 44962 | 2 | 18 | 33.51 | 670.21 |
| task_decoding | 4240 | 7724 | 11964 | 20 | 0 | 6.05 | 121.06 |
| task_summation | 4580 | 16494 | 21074 | 20 | 0 | 12.62 | 252.34 |
| task_transcription | 3047 | 2787 | 5834 | 20 | 0 | 2.66 | 53.18 |
| task_sequences | 2901 | 10644 | 13545 | 19 | 1 | 8.46 | 169.11 |
| string_entry | 3345 | 32150 | 35495 | 4 | 16 | 21.37 | 427.45 |
| **TOTAL** | **30457** | **154620** | **185077** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 2 3 6 3 6 2 6 3 2 2 1 6 |  | No | 34.41 |
| 2 | 6 3 2 5 3 6 6 5 2 2 6 4 1 2 |  | No | 53.2 |
| 3 | 6 5 1 2 2 5 2 6 5 5 6 4 1 3 |  | No | 39.49 |
| 4 | 1 4 6 4 3 2 5 5 5 2 2 1 5 4 |  | No | 34.45 |
| 5 | 2 5 6 6 4 6 2 6 2 6 4 5 1 4 |  | No | 37.92 |
| 6 | 6 2 6 1 6 5 5 4 5 3 6 1 2 5 |  | No | 49.21 |
| 7 | 6 2 2 4 1 3 6 2 2 4 5 3 4 1 |  | No | 25.45 |
| 8 | 3 2 1 2 3 5 1 5 1 4 5 6 6 3 |  | No | 28.53 |
| 9 | 6 1 1 4 2 3 5 1 6 2 2 3 5 6 |  | No | 45.91 |
| 10 | 5 2 4 5 6 3 4 5 1 4 3 2 6 6 |  | No | 118.2 |
| 11 | 1 2 5 3 6 2 1 5 2 6 3 1 5 3 |  | No | 41.22 |
| 12 | 3 6 2 5 1 3 5 4 6 2 2 2 4 1 |  | No | 35.94 |
| 13 | 6 1 2 2 5 6 4 2 6 4 5 3 3 5 |  | No | 35.44 |
| 14 | 1 6 2 3 6 5 1 2 2 4 6 6 2 1 |  | No | 34.5 |
| 15 | 5 2 3 1 3 4 5 3 1 5 2 4 4 1 |  | No | 34.42 |
| 16 | 2 5 5 2 6 5 4 2 2 1 6 5 2 4 |  | No | 30.59 |
| 17 | 3 1 6 4 3 6 3 5 6 3 6 5 5 3 |  | No | 38.47 |
| 18 | 3 4 6 4 6 3 1 1 2 6 1 6 4 3 |  | No | 38.47 |
| 19 | 2 2 5 6 4 2 6 6 4 3 4 6 3 1 |  | No | 48.9 |
| 20 | 3 1 1 2 6 3 1 2 5 6 6 3 2 1 |  | No | 42.01 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2193 | 2193 | Yes | 2.34 |
| 2 | 2269 | 2269 | Yes | 2.19 |
| 3 | 2274 | 2274 | Yes | 3.95 |
| 4 | 1836 | 1836 | Yes | 2.77 |
| 5 | 1514 | 1514 | Yes | 2.89 |
| 6 | 1843 | 1843 | Yes | 1.97 |
| 7 | 1353 | 1353 | Yes | 2.15 |
| 8 | 2091 | 2091 | Yes | 3.65 |
| 9 | 1688 | 1688 | Yes | 1.94 |
| 10 | 2250 | 2250 | Yes | 4.29 |
| 11 | 1687 | 1687 | Yes | 2.22 |
| 12 | 1685 | 1685 | Yes | 2.51 |
| 13 | 1687 | 1687 | Yes | 2.99 |
| 14 | 1416 | 1416 | Yes | 3.16 |
| 15 | 1943 | 1943 | Yes | 2.26 |
| 16 | 2015 | 2015 | Yes | 2.09 |
| 17 | 1135 | 1135 | Yes | 3.99 |
| 18 | 1389 | 1389 | Yes | 2.6 |
| 19 | 1417 | 1417 | Yes | 2.8 |
| 20 | 1631 | 1631 | Yes | 2.74 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 |  | No | 32.71 |
| 2 | 73 |  | No | 25.79 |
| 3 | 52 | 52 | Yes | 23.22 |
| 4 | 38 |  | No | 56.49 |
| 5 | 72 |  | No | 40.34 |
| 6 | 41 |  | No | 27.94 |
| 7 | 44 |  | No | 25.39 |
| 8 | 39 | 39 | Yes | 21.88 |
| 9 | 40 |  | No | 32.51 |
| 10 | 40 |  | No | 29.33 |
| 11 | 47 |  | No | 39.88 |
| 12 | 66 |  | No | 40.96 |
| 13 | 36 |  | No | 37.14 |
| 14 | 55 |  | No | 38.83 |
| 15 | 44 |  | No | 22.04 |
| 16 | 53 |  | No | 39.29 |
| 17 | 60 |  | No | 46.88 |
| 18 | 51 |  | No | 38.67 |
| 19 | 70 |  | No | 30.93 |
| 20 | 73 |  | No | 19.95 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XSZLPGK | XSZLPGK | Yes | 6.18 |
| 2 | CGXZDVP | CGXZDVP | Yes | 3.83 |
| 3 | CYOMJSQ | CYOMJSQ | Yes | 8.0 |
| 4 | EUPBWNZ | EUPBWNZ | Yes | 10.55 |
| 5 | GWCNXZQ | GWCNXZQ | Yes | 3.92 |
| 6 | FXHDTWN | FXHDTWN | Yes | 3.46 |
| 7 | LAGRVTU | LAGRVTU | Yes | 7.97 |
| 8 | DMVLSIW | DMVLSIW | Yes | 4.61 |
| 9 | PVBGXQF | PVBGXQF | Yes | 3.93 |
| 10 | TZCMOEK | TZCMOEK | Yes | 8.49 |
| 11 | EYXWLOG | EYXWLOG | Yes | 8.09 |
| 12 | RUSJHWQ | RUSJHWQ | Yes | 7.81 |
| 13 | ZSMWJAN | ZSMWJAN | Yes | 3.21 |
| 14 | QEJXAGS | QEJXAGS | Yes | 4.65 |
| 15 | MLOQPSK | MLOQPSK | Yes | 4.99 |
| 16 | EYGDONX | EYGDONX | Yes | 9.08 |
| 17 | UGRYCMJ | UGRYCMJ | Yes | 3.63 |
| 18 | ZLFQKWR | ZLFQKWR | Yes | 3.51 |
| 19 | QXCGPUY | QXCGPUY | Yes | 7.69 |
| 20 | VSCBGLQ | VSCBGLQ | Yes | 7.44 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 3.3 6.7 | Yes | 9.65 |
| 2 | [2.7, 7.3] | 2.7 7.3 | Yes | 12.77 |
| 3 | [1.5, 8.5] | 8.5 1.5 | Yes | 11.43 |
| 4 | [0.5, 9.5] | 0.5 9.5 | Yes | 57.05 |
| 5 | [0.4, 9.6] | 0.4 9.6 | Yes | 8.4 |
| 6 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.8 |
| 7 | [1.3, 8.7] | 1.3 8.7 | Yes | 9.95 |
| 8 | [1.7, 8.3] | 8.3 1.7 | Yes | 10.27 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.05 |
| 10 | [4.3, 5.7] | 5.7 4.3 | Yes | 10.06 |
| 11 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.29 |
| 12 | [0.7, 9.3] | 0.7 9.3 | Yes | 12.9 |
| 13 | [1.5, 8.5] | 8.5 1.5 | Yes | 11.61 |
| 14 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.34 |
| 15 | [1.4, 8.6] | 1.4 8.6 | Yes | 14.67 |
| 16 | [1.8, 8.2] | 8.2 1.8 | Yes | 5.32 |
| 17 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.86 |
| 18 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.46 |
| 19 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.47 |
| 20 | [3.5, 6.5] | 3.5 6.5 | Yes | 10.98 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TA0AGU6RFMT8 | TA0AGU6RFMT8 | Yes | 2.3 |
| 2 | BVGN0IVE0WGF | BVGN0IVE0WGF | Yes | 1.97 |
| 3 | V1GQYF8U230U | V1GQYF8U230U | Yes | 2.19 |
| 4 | HXOHPXBFEOLN | HXOHPXBFEOLN | Yes | 2.87 |
| 5 | PO2OZBKBPTTC | PO2OZBKBPTTC | Yes | 3.13 |
| 6 | 6QI0MQEWX12O | 6QI0MQEWX12O | Yes | 3.73 |
| 7 | 061EESIQ3WXY | 061EESIQ3WXY | Yes | 2.69 |
| 8 | 3Y3Y8JX3RAGU | 3Y3Y8JX3RAGU | Yes | 2.27 |
| 9 | YECXKHT3S6ZE | YECXKHT3S6ZE | Yes | 2.28 |
| 10 | F2VHK6JAZD75 | F2VHK6JAZD75 | Yes | 3.45 |
| 11 | LF8VLSF69UL4 | LF8VLSF69UL4 | Yes | 2.56 |
| 12 | 0JANX1NOQWXA | 0JANX1NOQWXA | Yes | 2.31 |
| 13 | 3XUYSWXUHIGZ | 3XUYSWXUHIGZ | Yes | 1.95 |
| 14 | S62C8QKYG4Y0 | S62C8QKYG4Y0 | Yes | 2.18 |
| 15 | TLZQ4HJC9G73 | TLZQ4HJC9G73 | Yes | 2.01 |
| 16 | BX6HUJXVG74V | BX6HUJXVG74V | Yes | 2.28 |
| 17 | C748EKHP9PSY | C748EKHP9PSY | Yes | 7.36 |
| 18 | 69EP7ZWJ31WK | 69EP7ZWJ31WK | Yes | 1.72 |
| 19 | 8XJVQ4WEQG43 | 8XJVQ4WEQG43 | Yes | 2.01 |
| 20 | 373JZ4JTA9T8 | 373JZ4JTA9T8 | Yes | 1.9 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 3.8 |
| 2 | 16 | 16 | Yes | 8.02 |
| 3 | 793 | 793 | Yes | 4.6 |
| 4 | 3 | 3 | Yes | 8.12 |
| 5 | 4096 |  | No | 39.76 |
| 6 | 26 | 26 | Yes | 12.77 |
| 7 | 19 | 19 | Yes | 9.16 |
| 8 | 73 | 73 | Yes | 6.77 |
| 9 | 4 | 4 | Yes | 7.65 |
| 10 | 7 | 7 | Yes | 7.04 |
| 11 | 6 | 6 | Yes | 4.3 |
| 12 | 198 | 198 | Yes | 6.2 |
| 13 | 3 | 3 | Yes | 10.35 |
| 14 | 243 | 243 | Yes | 6.66 |
| 15 | 20 | 20 | Yes | 12.52 |
| 16 | 4 | 4 | Yes | 3.05 |
| 17 | 36 | 36 | Yes | 2.04 |
| 18 | 31 | 31 | Yes | 3.33 |
| 19 | 10 | 10 | Yes | 9.86 |
| 20 | 5 | 5 | Yes | 3.12 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \\_<)<(<  |  | No | 44.01 |
| 2 | <_  <) )  | <_  <) ) | No | 15.75 |
| 3 | /\()<_( < | /\()<_( < | Yes | 5.68 |
| 4 | _<\  \/ _ |  | No | 23.35 |
| 5 |  \)_)\\(_ | \)_)\\(_ ) | No | 8.11 |
| 6 | /)_  (/)\ | /)_  (/)\ | Yes | 11.36 |
| 7 | (<</_ <)< |  | No | 35.68 |
| 8 | ( //() \  |  | No | 25.0 |
| 9 | \)___ \_< | \)___ \_< | Yes | 11.17 |
| 10 | _ \\)\\)( |  | No | 29.94 |
| 11 | (_(/)\_ ) |  | No | 23.95 |
| 12 | \((/<\<_  | \((/<\<_ | No | 16.48 |
| 13 | <(_\))< _ |  | No | 25.23 |
| 14 | _ <))( (< |  | No | 40.26 |
| 15 | <()  <_</ |  | No | 25.23 |
| 16 | _<)</(\// | /\) <(_<) | No | 21.12 |
| 17 | (\_/<  _\ |  | No | 32.19 |
| 18 | <()<((/)( | /\) <(_<) | No | 12.13 |
| 19 | /_/ /<_/\ | /_/ /<_/_\ | No | 8.81 |
| 20 | \\)  \()/ | \\)  \()/ | Yes | 11.99 |
