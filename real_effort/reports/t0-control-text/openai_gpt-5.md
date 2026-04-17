# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-26 16:33:32

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
| sudoku_game | 4444 | 38912 | 43356 | 0 | 20 | 63.13 | 1262.59 |
| add_numbers | 2420 | 4775 | 7195 | 20 | 0 | 6.92 | 138.46 |
| counting_zeros | 3820 | 40960 | 44780 | 0 | 20 | 58.45 | 1169.03 |
| task_decoding | 3760 | 9349 | 13109 | 20 | 0 | 12.80 | 256.09 |
| task_summation | 4100 | 17010 | 21110 | 20 | 0 | 15.59 | 311.8 |
| task_transcription | 2563 | 4698 | 7261 | 20 | 0 | 6.89 | 137.84 |
| task_sequences | 2420 | 13027 | 15447 | 19 | 1 | 16.15 | 323.0 |
| string_entry | 2709 | 27884 | 30593 | 10 | 10 | 41.40 | 828.02 |
| **TOTAL** | **26236** | **156615** | **182851** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 2 6 1 3 4 1 6 4 6 1 4 1 |  | No | 69.88 |
| 2 | 6 3 1 2 3 1 1 4 2 6 6 5 4 6 |  | No | 65.36 |
| 3 | 3 2 3 6 1 4 2 3 1 5 6 5 3 4 | TIMEOUT | No | 120.03 |
| 4 | 4 6 2 1 4 3 5 2 4 5 1 3 1 4 |  | No | 57.79 |
| 5 | 3 4 6 2 1 3 2 5 4 5 3 6 3 4 |  | No | 84.13 |
| 6 | 4 4 2 5 1 4 6 2 4 5 4 1 3 1 |  | No | 58.11 |
| 7 | 3 1 5 4 4 5 1 6 4 3 1 5 3 6 |  | No | 67.28 |
| 8 | 5 4 1 4 6 4 6 1 2 2 1 3 5 6 |  | No | 64.09 |
| 9 | 6 3 4 1 1 4 6 5 4 3 6 6 3 4 |  | No | 75.31 |
| 10 | 4 1 1 4 4 1 2 1 3 4 2 6 3 4 |  | No | 53.38 |
| 11 | 6 5 3 1 6 3 5 4 6 2 6 2 6 3 |  | No | 48.16 |
| 12 | 5 3 1 2 2 6 3 4 5 5 3 6 2 6 |  | No | 37.35 |
| 13 | 2 1 3 5 6 5 2 4 1 3 5 4 1 4 |  | No | 75.87 |
| 14 | 1 2 3 5 6 6 1 4 5 3 2 6 4 1 |  | No | 60.61 |
| 15 | 2 4 3 6 1 6 4 5 4 3 2 1 5 1 |  | No | 59.12 |
| 16 | 5 4 2 3 6 5 4 2 5 6 3 2 6 5 |  | No | 58.56 |
| 17 | 1 6 2 4 5 6 1 3 4 5 3 2 6 1 |  | No | 57.58 |
| 18 | 3 1 3 2 5 4 4 6 3 2 4 6 5 4 |  | No | 49.0 |
| 19 | 1 2 5 1 4 2 6 6 1 4 6 2 3 6 |  | No | 55.4 |
| 20 | 5 3 3 6 5 2 1 6 4 6 2 4 6 6 |  | No | 45.56 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1784 | 1784 | Yes | 5.41 |
| 2 | 1087 | 1087 | Yes | 5.25 |
| 3 | 797 | 797 | Yes | 4.37 |
| 4 | 2669 | 2669 | Yes | 4.63 |
| 5 | 1810 | 1810 | Yes | 4.82 |
| 6 | 1591 | 1591 | Yes | 2.74 |
| 7 | 1753 | 1753 | Yes | 4.61 |
| 8 | 1995 | 1995 | Yes | 7.73 |
| 9 | 2110 | 2110 | Yes | 14.28 |
| 10 | 1074 | 1074 | Yes | 6.81 |
| 11 | 1109 | 1109 | Yes | 7.91 |
| 12 | 1243 | 1243 | Yes | 8.38 |
| 13 | 1613 | 1613 | Yes | 5.52 |
| 14 | 1924 | 1924 | Yes | 7.14 |
| 15 | 2087 | 2087 | Yes | 12.75 |
| 16 | 2259 | 2259 | Yes | 7.1 |
| 17 | 1223 | 1223 | Yes | 11.66 |
| 18 | 905 | 905 | Yes | 5.17 |
| 19 | 1598 | 1598 | Yes | 4.92 |
| 20 | 1069 | 1069 | Yes | 7.25 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 |  | No | 61.55 |
| 2 | 56 |  | No | 66.17 |
| 3 | 69 |  | No | 68.76 |
| 4 | 37 |  | No | 36.83 |
| 5 | 62 |  | No | 60.71 |
| 6 | 43 |  | No | 55.41 |
| 7 | 42 |  | No | 55.5 |
| 8 | 69 |  | No | 63.01 |
| 9 | 51 |  | No | 57.15 |
| 10 | 57 |  | No | 57.59 |
| 11 | 64 |  | No | 59.79 |
| 12 | 72 |  | No | 66.84 |
| 13 | 52 |  | No | 51.36 |
| 14 | 49 |  | No | 51.79 |
| 15 | 65 |  | No | 62.07 |
| 16 | 50 |  | No | 48.79 |
| 17 | 73 |  | No | 53.25 |
| 18 | 60 |  | No | 52.63 |
| 19 | 67 |  | No | 72.5 |
| 20 | 71 |  | No | 67.31 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GMJAYBL | GMJAYBL | Yes | 10.25 |
| 2 | JRFQMLH | JRFQMLH | Yes | 12.56 |
| 3 | TOYZNVL | TOYZNVL | Yes | 17.52 |
| 4 | OBTYSDP | OBTYSDP | Yes | 13.23 |
| 5 | OILRDAP | OILRDAP | Yes | 18.53 |
| 6 | WYMDTPL | WYMDTPL | Yes | 23.33 |
| 7 | HRQYCUZ | HRQYCUZ | Yes | 12.54 |
| 8 | ICHFTPL | ICHFTPL | Yes | 12.28 |
| 9 | MZDYCLI | MZDYCLI | Yes | 9.03 |
| 10 | UHRPIAQ | UHRPIAQ | Yes | 9.52 |
| 11 | ZHMRXDP | ZHMRXDP | Yes | 8.86 |
| 12 | PDWKVSZ | PDWKVSZ | Yes | 9.62 |
| 13 | WCTBMAE | WCTBMAE | Yes | 11.57 |
| 14 | CNRFWMB | CNRFWMB | Yes | 18.44 |
| 15 | NORWFLD | NORWFLD | Yes | 15.11 |
| 16 | ZXASMYT | ZXASMYT | Yes | 12.26 |
| 17 | LVRMXWB | LVRMXWB | Yes | 7.25 |
| 18 | FBDUCPR | FBDUCPR | Yes | 10.02 |
| 19 | FKRQSUH | FKRQSUH | Yes | 12.22 |
| 20 | XNFCAJZ | XNFCAJZ | Yes | 11.91 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [5.0, 5.0] | 5.0 5.0 | Yes | 13.6 |
| 2 | [0.4, 9.6] | 0.4 9.6 | Yes | 19.11 |
| 3 | [4.6, 5.4] | 5.4 4.6 | Yes | 11.31 |
| 4 | [4.7, 5.3] | 4.7 5.3 | Yes | 10.8 |
| 5 | [2.8, 7.2] | 2.8 7.2 | Yes | 16.24 |
| 6 | [0.3, 9.7] | 0.3 9.7 | Yes | 20.85 |
| 7 | [2.8, 7.2] | 2.8 7.2 | Yes | 13.79 |
| 8 | [0.6, 9.4] | 9.4 0.6 | Yes | 11.78 |
| 9 | [2.3, 7.7] | 7.7 2.3 | Yes | 19.93 |
| 10 | [4.8, 5.2] | 4.8 5.2 | Yes | 14.1 |
| 11 | [0.6, 9.4] | 0.6 9.4 | Yes | 11.89 |
| 12 | [1.8, 8.2] | 8.2 1.8 | Yes | 11.65 |
| 13 | [0.4, 9.6] | 9.6 0.4 | Yes | 13.91 |
| 14 | [0.6, 9.4] | 9.4 0.6 | Yes | 16.71 |
| 15 | [3.0, 7.0] | 7.0 3.0 | Yes | 12.73 |
| 16 | [2.6, 7.4] | 7.4 2.6 | Yes | 18.34 |
| 17 | [1.9, 8.1] | 8.1 1.9 | Yes | 17.45 |
| 18 | [2.5, 7.5] | 7.5 2.5 | Yes | 23.05 |
| 19 | [1.3, 8.7] | 1.3 8.7 | Yes | 17.85 |
| 20 | [1.3, 8.7] | 1.3 8.7 | Yes | 16.69 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BF05FSFKVGO8 | BF05FSFKVGO8 | Yes | 5.08 |
| 2 | OYB4T55AAXBS | OYB4T55AAXBS | Yes | 13.69 |
| 3 | ENF4XE0UBSEG | ENF4XE0UBSEG | Yes | 6.69 |
| 4 | VQ440A3YV9QY | VQ440A3YV9QY | Yes | 6.46 |
| 5 | 6GQDAP470ZFP | 6GQDAP470ZFP | Yes | 6.42 |
| 6 | T7PVL6J3DSR6 | T7PVL6J3DSR6 | Yes | 4.4 |
| 7 | YBL3EZGTVKQ9 | YBL3EZGTVKQ9 | Yes | 6.03 |
| 8 | 2WG883M2LIP4 | 2WG883M2LIP4 | Yes | 7.92 |
| 9 | WLUHDNOBTSIZ | WLUHDNOBTSIZ | Yes | 4.88 |
| 10 | 98I1JVMTI3AQ | 98I1JVMTI3AQ | Yes | 6.93 |
| 11 | Y4UMWEG1RJFV | Y4UMWEG1RJFV | Yes | 5.41 |
| 12 | UYIJFAPKSDFQ | UYIJFAPKSDFQ | Yes | 3.81 |
| 13 | 6AARE74QT5KN | 6AARE74QT5KN | Yes | 7.33 |
| 14 | NPSO2RBN18M2 | NPSO2RBN18M2 | Yes | 6.65 |
| 15 | A6C9ASV83JY1 | A6C9ASV83JY1 | Yes | 8.15 |
| 16 | MPN799YCEISV | MPN799YCEISV | Yes | 6.17 |
| 17 | GCRBGU3YIPH5 | GCRBGU3YIPH5 | Yes | 4.74 |
| 18 | C9KN5CXT016M | C9KN5CXT016M | Yes | 18.0 |
| 19 | V8GY4FVQJ5AK | V8GY4FVQJ5AK | Yes | 4.23 |
| 20 | 26Y0WJSIFA1O | 26Y0WJSIFA1O | Yes | 4.82 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 |  | No | 73.83 |
| 2 | 23 | 23 | Yes | 9.83 |
| 3 | 19 | 19 | Yes | 8.42 |
| 4 | 48 | 48 | Yes | 13.69 |
| 5 | 1440 | 1440 | Yes | 7.85 |
| 6 | 6 | 6 | Yes | 8.73 |
| 7 | 5 | 5 | Yes | 39.2 |
| 8 | 7 | 7 | Yes | 6.32 |
| 9 | 16 | 16 | Yes | 8.53 |
| 10 | 60 | 60 | Yes | 9.06 |
| 11 | 3 | 3 | Yes | 12.73 |
| 12 | 793 | 793 | Yes | 5.91 |
| 13 | 198 | 198 | Yes | 9.76 |
| 14 | 36 | 36 | Yes | 10.87 |
| 15 | 28 | 28 | Yes | 12.93 |
| 16 | 39 | 39 | Yes | 18.64 |
| 17 | 26 | 26 | Yes | 24.87 |
| 18 | 3 | 3 | Yes | 14.66 |
| 19 | 10 | 10 | Yes | 13.67 |
| 20 | 7680 | 7680 | Yes | 13.47 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (\_(_ /<( | (\_(_ /<( | Yes | 31.96 |
| 2 | (_)<__ _  | (_)<__ _ | No | 28.78 |
| 3 | \_(_))_ \ | \_(_))_ \ | Yes | 21.15 |
| 4 | _/(/__ _) | _/(/__ _) | Yes | 43.65 |
| 5 | <_<\//\_( |  | No | 77.17 |
| 6 | /_<)\)/<) |  | No | 63.95 |
| 7 | /)\_</ <) | /)\_</ <) | Yes | 23.15 |
| 8 | _(\\\(/(  |  | No | 79.23 |
| 9 | )(</)//\( | )(</)//\( | Yes | 21.48 |
| 10 | <<\<_\)<\ | <<\<_\)<\ | Yes | 46.82 |
| 11 | \/ /\<)_< | TIMEOUT | No | 120.04 |
| 12 | <)/ () \< | <)/ () \< | Yes | 15.06 |
| 13 |  )/())/__ | )/())/__ | No | 31.28 |
| 14 | <\)/\((<) | <\)/\((<) | Yes | 18.48 |
| 15 |  _\  _\_\ | _\  _\_\ | No | 34.85 |
| 16 |  (_//\//\ | (_//\//\ | No | 24.08 |
| 17 | ()_<\(\<\ | ()_<\(\<\ | Yes | 26.89 |
| 18 | <\/_)//_\ | <\/_)//_\ | Yes | 24.45 |
| 19 |  <(/)\(_/ | <(/)\(_/ | No | 18.07 |
| 20 | (\() ))(< |  | No | 77.48 |
