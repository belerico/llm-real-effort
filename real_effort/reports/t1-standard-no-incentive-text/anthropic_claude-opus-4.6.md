# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-27 10:05:03

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 6120 | 36732 | 42852 | 6 | 14 | 32.41 | 648.26 |
| add_numbers | 3500 | 600 | 4100 | 20 | 0 | 3.20 | 64.12 |
| counting_zeros | 4820 | 15277 | 20097 | 6 | 14 | 9.82 | 196.38 |
| task_decoding | 4820 | 1619 | 6439 | 19 | 1 | 4.47 | 89.39 |
| task_summation | 4880 | 4906 | 9786 | 20 | 0 | 5.98 | 119.62 |
| task_transcription | 3659 | 740 | 4399 | 20 | 0 | 2.99 | 59.78 |
| task_sequences | 3560 | 4025 | 7585 | 19 | 1 | 5.84 | 116.71 |
| string_entry | 4009 | 1633 | 5642 | 14 | 6 | 3.74 | 74.78 |
| **TOTAL** | **35368** | **65532** | **100900** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 4 2 5 1 2 3 1 4 2 4 4 3 1 |  | No | 36.83 |
| 2 | 3 5 4 1 4 3 2 6 2 4 6 6 3 1 | 3 5 4 1 4 3 2 6 2 4 6 6 3 1 | Yes | 49.7 |
| 3 | 2 4 2 3 6 5 3 6 5 2 6 4 1 4 |  | No | 36.2 |
| 4 | 4 5 3 2 1 6 1 3 4 3 5 4 3 6 |  | No | 37.14 |
| 5 | 2 1 4 2 4 3 2 1 5 6 4 2 5 1 |  | No | 34.62 |
| 6 | 1 5 4 1 1 4 2 5 5 4 5 6 3 1 | 1 5 4 1 1 4 2 5 5 4 5 6 3 1 | Yes | 18.71 |
| 7 | 4 2 1 6 1 3 1 6 2 5 5 4 1 2 |  | No | 32.51 |
| 8 | 5 4 6 5 4 1 1 4 3 3 6 5 1 2 |  | No | 35.42 |
| 9 | 1 5 2 3 6 2 4 2 1 2 3 1 3 2 |  | No | 35.29 |
| 10 | 3 6 4 1 4 5 1 6 5 4 3 2 1 5 |  | No | 36.12 |
| 11 | 1 6 3 2 3 2 6 1 5 2 3 5 1 1 |  | No | 32.92 |
| 12 | 1 3 4 4 6 3 6 2 5 6 3 2 5 1 | 1 3 4 4 6 3 6 2 5 6 3 2 5 1 | Yes | 19.16 |
| 13 | 3 6 4 3 5 3 4 5 3 2 5 4 6 3 | 3 6 4 3 5 3 4 5 3 2 5 4 6 3 | Yes | 17.47 |
| 14 | 4 5 3 6 1 2 5 3 2 5 3 2 4 6 | 4 5 3 6 1 2 5 3 2 5 4 6 | No | 27.41 |
| 15 | 3 2 6 5 1 5 3 5 2 4 5 5 3 2 |  | No | 35.47 |
| 16 | 1 6 4 5 3 6 3 4 3 6 2 6 1 4 |  | No | 50.1 |
| 17 | 2 6 1 1 5 4 2 2 5 3 3 6 6 1 |  | No | 33.59 |
| 18 | 3 2 5 4 4 3 4 1 5 2 3 5 1 2 | 3 2 5 4 4 3 4 1 6 5 2 3 5 1 2 | No | 32.82 |
| 19 | 3 6 4 3 6 5 6 1 1 4 6 6 4 1 | 3 6 4 3 6 5 6 1 1 4 6 6 4 1 | Yes | 21.72 |
| 20 | 1 3 4 5 1 2 4 2 5 3 2 1 2 5 | 1 3 4 5 1 2 4 2 5 3 2 1 2 5 | Yes | 25.02 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1153 | 1153 | Yes | 2.3 |
| 2 | 1597 | 1597 | Yes | 2.32 |
| 3 | 2411 | 2411 | Yes | 2.6 |
| 4 | 2299 | 2299 | Yes | 2.86 |
| 5 | 1361 | 1361 | Yes | 2.24 |
| 6 | 1384 | 1384 | Yes | 2.99 |
| 7 | 2041 | 2041 | Yes | 3.52 |
| 8 | 1736 | 1736 | Yes | 2.15 |
| 9 | 1770 | 1770 | Yes | 10.75 |
| 10 | 1699 | 1699 | Yes | 2.29 |
| 11 | 1800 | 1800 | Yes | 4.3 |
| 12 | 1023 | 1023 | Yes | 5.14 |
| 13 | 1384 | 1384 | Yes | 2.83 |
| 14 | 1941 | 1941 | Yes | 2.77 |
| 15 | 1817 | 1817 | Yes | 2.44 |
| 16 | 1384 | 1384 | Yes | 3.06 |
| 17 | 1049 | 1049 | Yes | 2.58 |
| 18 | 1405 | 1405 | Yes | 2.27 |
| 19 | 1162 | 1162 | Yes | 2.32 |
| 20 | 1440 | 1440 | Yes | 2.37 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 48 | No | 8.81 |
| 2 | 67 | 66 | No | 11.04 |
| 3 | 67 | 67 | Yes | 9.85 |
| 4 | 42 | 41 | No | 10.88 |
| 5 | 46 | 45 | No | 12.32 |
| 6 | 45 | 45 | Yes | 11.0 |
| 7 | 75 | 66 | No | 9.36 |
| 8 | 71 | 71 | Yes | 7.61 |
| 9 | 64 | 62 | No | 6.7 |
| 10 | 45 | 44 | No | 14.96 |
| 11 | 72 | 73 | No | 9.53 |
| 12 | 55 | 54 | No | 14.76 |
| 13 | 36 | 36 | Yes | 6.27 |
| 14 | 37 | 36 | No | 11.31 |
| 15 | 58 | 53 | No | 10.56 |
| 16 | 66 | 66 | Yes | 9.91 |
| 17 | 45 | 42 | No | 6.66 |
| 18 | 70 | 66 | No | 8.63 |
| 19 | 75 | 75 | Yes | 9.32 |
| 20 | 52 | 50 | No | 6.89 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZJPFQLU | ZJPFQLU | Yes | 4.05 |
| 2 | SCDQIOT | SCDQIOT | Yes | 4.17 |
| 3 | EXJSWNK | EXJSWNK | Yes | 3.08 |
| 4 | GMNPUHS | GMNPUHS | Yes | 3.09 |
| 5 | NQMBTSG | NQMBTSG | Yes | 3.54 |
| 6 | UIKYEOB | UIKYEOB | Yes | 3.01 |
| 7 | BIHEOVX | BIHEOVX | Yes | 9.48 |
| 8 | VHIDNGO | VHIDNGO | Yes | 4.35 |
| 9 | EHUKCAG | EHUKCAG | Yes | 4.73 |
| 10 | JQEVCHI | JQEVCHI | Yes | 3.89 |
| 11 | OFZPUHL | OFZPUHL | Yes | 3.04 |
| 12 | XDPZQIU | XDPZIQU | No | 2.9 |
| 13 | LHQRPEK | LHQRPEK | Yes | 3.67 |
| 14 | HJEZITM | HJEZITM | Yes | 3.34 |
| 15 | GOHQAUK | GOHQAUK | Yes | 3.34 |
| 16 | FPIJDXQ | FPIJDXQ | Yes | 3.16 |
| 17 | EQRSGYA | EQRSGYA | Yes | 13.37 |
| 18 | ZXQVABU | ZXQVABU | Yes | 4.38 |
| 19 | OYCSNZP | OYCSNZP | Yes | 3.13 |
| 20 | BEIOYZK | BEIOYZK | Yes | 5.66 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 0.5 9.5 | Yes | 3.0 |
| 2 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.43 |
| 3 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.21 |
| 4 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.11 |
| 5 | [1.5, 8.5] | 1.5 8.5 | Yes | 4.42 |
| 6 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.74 |
| 7 | [4.5, 5.5] | 5.5 4.5 | Yes | 8.13 |
| 8 | [0.1, 9.9] | 0.1 9.9 | Yes | 5.61 |
| 9 | [5.0, 5.0] | 5.0 5.0 | Yes | 9.98 |
| 10 | [3.6, 6.4] | 6.4 3.6 | Yes | 4.09 |
| 11 | [3.5, 6.5] | 6.5 3.5 | Yes | 3.88 |
| 12 | [3.1, 6.9] | 3.1 6.9 | Yes | 3.82 |
| 13 | [1.3, 8.7] | 8.7 1.3 | Yes | 6.48 |
| 14 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.68 |
| 15 | [4.1, 5.9] | 4.1 5.9 | Yes | 7.45 |
| 16 | [1.8, 8.2] | 1.8 8.2 | Yes | 5.84 |
| 17 | [1.2, 8.8] | 1.2 8.8 | Yes | 3.96 |
| 18 | [2.5, 7.5] | 2.5 7.5 | Yes | 4.21 |
| 19 | [1.7, 8.3] | 8.3 1.7 | Yes | 5.61 |
| 20 | [3.0, 7.0] | 3.0 7.0 | Yes | 3.96 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | W7ONI0XH8OO4 | W7ONI0XH8OO4 | Yes | 2.48 |
| 2 | 3U3D5VZRPDC8 | 3U3D5VZRPDC8 | Yes | 2.63 |
| 3 | NHZ79N0G69YR | NHZ79N0G69YR | Yes | 3.9 |
| 4 | UW11CM2SD82B | UW11CM2SD82B | Yes | 2.58 |
| 5 | Z9UIBNLQNZHO | Z9UIBNLQNZHO | Yes | 2.62 |
| 6 | D685FPS04YT4 | D685FPS04YT4 | Yes | 3.57 |
| 7 | EE4JYCYDD4QI | EE4JYCYDD4QI | Yes | 3.83 |
| 8 | XL1B998L58YU | XL1B998L58YU | Yes | 2.78 |
| 9 | UOK7GCBSPSNQ | UOK7GCBSPSNQ | Yes | 2.7 |
| 10 | HKXI6JN4N1C7 | HKXI6JN4N1C7 | Yes | 2.55 |
| 11 | GC00GF6CNZ3W | GC00GF6CNZ3W | Yes | 2.59 |
| 12 | NHF4PI56DCLT | NHF4PI56DCLT | Yes | 3.17 |
| 13 | EIG5L3CQZKDF | EIG5L3CQZKDF | Yes | 3.06 |
| 14 | CZ50Z2AEKKTZ | CZ50Z2AEKKTZ | Yes | 2.31 |
| 15 | 8KV13GVG9XD7 | 8KV13GVG9XD7 | Yes | 4.09 |
| 16 | NSUAAGKAJ6HM | NSUAAGKAJ6HM | Yes | 2.36 |
| 17 | 0OBI4U7M7KFY | 0OBI4U7M7KFY | Yes | 3.02 |
| 18 | AKMDPE79QIL1 | AKMDPE79QIL1 | Yes | 2.74 |
| 19 | M1U6UJWA21FM | M1U6UJWA21FM | Yes | 3.0 |
| 20 | HKSTBCJTT1CC | HKSTBCJTT1CC | Yes | 3.78 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 4.62 |
| 2 | 73 | 73 | Yes | 4.38 |
| 3 | 10 | 10 | Yes | 6.47 |
| 4 | 9 | 9 | Yes | 6.29 |
| 5 | 60 | 60 | Yes | 2.82 |
| 6 | 5 | 8 | No | 22.29 |
| 7 | 198 | 198 | Yes | 4.12 |
| 8 | 20 | 20 | Yes | 11.4 |
| 9 | 5 | 5 | Yes | 4.81 |
| 10 | 48 | 48 | Yes | 3.8 |
| 11 | 6 | 6 | Yes | 2.91 |
| 12 | 9 | 9 | Yes | 4.08 |
| 13 | 36 | 36 | Yes | 2.23 |
| 14 | 28 | 28 | Yes | 4.87 |
| 15 | 7 | 7 | Yes | 3.45 |
| 16 | 19 | 19 | Yes | 2.8 |
| 17 | 1 | 1 | Yes | 6.18 |
| 18 | 243 | 243 | Yes | 11.51 |
| 19 | 793 | 793 | Yes | 3.0 |
| 20 | 7680 | 7680 | Yes | 4.68 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( <()(_ \ | ( <()(_ \ | Yes | 3.16 |
| 2 | \((\_/\(\ | \((\_/\(\ | Yes | 4.27 |
| 3 | (((_/\(<) | (((_/\(<) | Yes | 3.32 |
| 4 | \(\<_( <\ | \(\<_( <\ | Yes | 4.15 |
| 5 | /<))((/)  | /<))((/) | No | 4.46 |
| 6 | ( /<\(\\( | ( /<\(\\( | Yes | 5.01 |
| 7 | \_/\)< (/ | \_/\)< (/ | Yes | 3.69 |
| 8 | /)/\ \()< | /)/\ \() | No | 4.01 |
| 9 | ()\ __<_\ | ()\ __<_\ | Yes | 3.03 |
| 10 |   (<<//_< | (<<//_ | No | 2.77 |
| 11 | ///()_(_\ | ///()_(_\ | Yes | 2.21 |
| 12 | <<)_(/(<  | <<)_(/(< | No | 2.99 |
| 13 | _//_\(_(_ | _//_\(_(_ | Yes | 3.7 |
| 14 | _(//)_)__ | _(//)_)__ | Yes | 3.95 |
| 15 | / \_\/(\  | / \_/(\ | No | 4.47 |
| 16 | \(((\<(/_ | \(((\<(/_ | Yes | 2.78 |
| 17 | \/<)_/ \_ | \/<)_/ \_ | Yes | 3.64 |
| 18 | \<_\<))(_ | \<_\<))(_ | Yes | 3.83 |
| 19 | )\)( (( ) | )\)( (( ) | Yes | 3.24 |
| 20 |  <)<((( ) | <)<((( ) | No | 6.09 |
