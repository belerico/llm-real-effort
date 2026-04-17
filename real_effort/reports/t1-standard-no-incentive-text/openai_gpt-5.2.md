# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-27 10:16:58

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
| sudoku_game | 4973 | 28396 | 33369 | 11 | 9 | 35.56 | 711.15 |
| add_numbers | 2720 | 735 | 3455 | 20 | 0 | 3.14 | 62.9 |
| counting_zeros | 4120 | 18788 | 22908 | 20 | 0 | 18.70 | 374.01 |
| task_decoding | 4060 | 2078 | 6138 | 20 | 0 | 5.88 | 117.59 |
| task_summation | 4400 | 4214 | 8614 | 20 | 0 | 7.16 | 143.12 |
| task_transcription | 2856 | 608 | 3464 | 20 | 0 | 1.91 | 38.16 |
| task_sequences | 2720 | 5681 | 8401 | 18 | 2 | 11.69 | 233.79 |
| string_entry | 3161 | 17395 | 20556 | 8 | 12 | 20.12 | 402.37 |
| **TOTAL** | **29010** | **77895** | **106905** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 5 4 2 4 1 6 6 3 1 5 5 2 | 3 2 5 4 2 4 1 6 6 3 1 5 5 2 | Yes | 19.8 |
| 2 | 5 4 3 1 5 6 4 3 6 5 1 4 6 3 | 5 4 3 1 5 6 4 3 6 5 1 4 6 3 | Yes | 12.69 |
| 3 | 6 3 2 4 1 5 4 2 6 1 5 2 5 2 | 6 3 2 4 1 5 4 2 6 1 5 2 5 2 | Yes | 18.1 |
| 4 | 3 4 2 5 4 4 2 1 6 3 5 1 1 4 |  | No | 54.89 |
| 5 | 2 5 1 3 2 3 5 2 5 4 1 6 2 4 | 2 5 1 3 2 3 5 2 5 4 1 6 2 4 | Yes | 13.99 |
| 6 | 5 1 3 2 6 3 1 6 2 4 1 1 6 4 |  | No | 71.81 |
| 7 | 6 5 4 5 4 1 1 5 6 3 2 1 3 3 | 6 5 4 5 4 1 1 5 6 3 2 1 3 3 | Yes | 24.31 |
| 8 | 2 6 4 1 3 5 3 1 6 1 5 4 6 3 | 2 6 4 1 3 5 3 1 6 1 5 4 6 3 | Yes | 18.15 |
| 9 | 6 1 3 5 1 2 6 3 5 2 4 1 5 4 | 6 1 3 5 1 2 6 3 5 2 4 1 5 4 | Yes | 14.94 |
| 10 | 4 6 5 4 6 1 1 5 5 1 3 2 6 4 | 4 6 5 4 6 1 1 5 5 1 3 2 6 4 | Yes | 13.22 |
| 11 | 5 2 6 1 3 4 5 1 2 6 4 5 3 4 | 5 2 6 1 3 4 1 2 6 4 5 3 4 | No | 26.99 |
| 12 | 2 6 2 3 4 2 3 2 5 1 4 3 3 5 | 2 6 2 3 4 2 3 2 5 1 4 3 3 5 | Yes | 16.0 |
| 13 | 3 4 5 6 1 3 6 4 3 1 4 2 5 4 |  | No | 67.0 |
| 14 | 3 2 6 3 3 4 5 3 2 1 6 5 6 3 |  | No | 71.42 |
| 15 | 2 6 2 4 1 2 5 1 4 6 2 3 5 2 |  | No | 45.77 |
| 16 | 4 1 5 4 6 2 1 4 1 5 4 3 6 5 |  | No | 64.14 |
| 17 | 4 4 2 3 6 6 1 2 5 4 2 5 3 1 | 4 4 2 3 6 6 1 2 5 4 2 5 3 1 | Yes | 21.49 |
| 18 | 5 4 6 2 4 1 3 1 1 5 3 1 2 4 | 5 4 6 2 4 1 3 1 1 5 3 1 2 4 | Yes | 26.85 |
| 19 | 6 1 1 5 3 6 6 3 2 1 4 2 6 3 |  | No | 55.87 |
| 20 | 1 5 2 3 6 2 2 3 5 1 5 6 4 1 |  | No | 53.7 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1808 | 1808 | Yes | 2.95 |
| 2 | 1949 | 1949 | Yes | 3.28 |
| 3 | 1018 | 1018 | Yes | 3.26 |
| 4 | 2401 | 2401 | Yes | 3.32 |
| 5 | 2121 | 2121 | Yes | 2.73 |
| 6 | 1838 | 1838 | Yes | 3.07 |
| 7 | 1400 | 1400 | Yes | 3.28 |
| 8 | 2822 | 2822 | Yes | 3.39 |
| 9 | 1532 | 1532 | Yes | 3.77 |
| 10 | 1876 | 1876 | Yes | 3.39 |
| 11 | 1104 | 1104 | Yes | 2.63 |
| 12 | 2140 | 2140 | Yes | 1.65 |
| 13 | 1418 | 1418 | Yes | 3.61 |
| 14 | 2405 | 2405 | Yes | 3.3 |
| 15 | 2293 | 2293 | Yes | 3.16 |
| 16 | 1340 | 1340 | Yes | 3.45 |
| 17 | 1575 | 1575 | Yes | 3.0 |
| 18 | 2393 | 2393 | Yes | 2.9 |
| 19 | 1983 | 1983 | Yes | 3.85 |
| 20 | 1771 | 1771 | Yes | 2.89 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 | 61 | Yes | 20.35 |
| 2 | 40 | 40 | Yes | 14.72 |
| 3 | 61 | 61 | Yes | 31.62 |
| 4 | 47 | 47 | Yes | 14.27 |
| 5 | 67 | 67 | Yes | 17.28 |
| 6 | 53 | 53 | Yes | 16.61 |
| 7 | 69 | 69 | Yes | 25.53 |
| 8 | 59 | 59 | Yes | 10.95 |
| 9 | 71 | 71 | Yes | 21.3 |
| 10 | 42 | 42 | Yes | 16.01 |
| 11 | 49 | 49 | Yes | 21.99 |
| 12 | 42 | 42 | Yes | 17.13 |
| 13 | 47 | 47 | Yes | 17.23 |
| 14 | 59 | 59 | Yes | 20.86 |
| 15 | 43 | 43 | Yes | 17.41 |
| 16 | 41 | 41 | Yes | 14.63 |
| 17 | 64 | 64 | Yes | 14.2 |
| 18 | 36 | 36 | Yes | 17.82 |
| 19 | 38 | 38 | Yes | 18.91 |
| 20 | 58 | 58 | Yes | 25.18 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LWNQTKC | LWNQTKC | Yes | 4.8 |
| 2 | EBTSZRQ | EBTSZRQ | Yes | 6.51 |
| 3 | ASZWXFR | ASZWXFR | Yes | 7.46 |
| 4 | ZDBOQCP | ZDBOQCP | Yes | 6.12 |
| 5 | QYVOITW | QYVOITW | Yes | 6.8 |
| 6 | YPZWRUX | YPZWRUX | Yes | 4.57 |
| 7 | CHPBKUO | CHPBKUO | Yes | 5.94 |
| 8 | BUQHMLK | BUQHMLK | Yes | 5.74 |
| 9 | VHGRSJC | VHGRSJC | Yes | 5.79 |
| 10 | XWLDPEB | XWLDPEB | Yes | 5.07 |
| 11 | UEGDKTJ | UEGDKTJ | Yes | 5.3 |
| 12 | TKZIRFG | TKZIRFG | Yes | 5.56 |
| 13 | IJUOMTK | IJUOMTK | Yes | 6.55 |
| 14 | UTNWALR | UTNWALR | Yes | 9.64 |
| 15 | ECHBSFV | ECHBSFV | Yes | 6.0 |
| 16 | HRAJTGN | HRAJTGN | Yes | 2.52 |
| 17 | UXSIOGR | UXSIOGR | Yes | 6.89 |
| 18 | VBNWLUK | VBNWLUK | Yes | 4.44 |
| 19 | GZUQPCM | GZUQPCM | Yes | 6.15 |
| 20 | GZRSLNE | GZRSLNE | Yes | 5.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.4, 5.6] | 4.4 5.6 | Yes | 5.09 |
| 2 | [4.5, 5.5] | 5.5 4.5 | Yes | 7.2 |
| 3 | [3.0, 7.0] | 7.0 3.0 | Yes | 8.52 |
| 4 | [2.2, 7.8] | 7.8 2.2 | Yes | 6.34 |
| 5 | [1.4, 8.6] | 8.6 1.4 | Yes | 6.38 |
| 6 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.4 |
| 7 | [4.4, 5.6] | 4.4 5.6 | Yes | 8.86 |
| 8 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.03 |
| 9 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.37 |
| 10 | [0.8, 9.2] | 9.2 0.8 | Yes | 6.19 |
| 11 | [3.1, 6.9] | 6.9 3.1 | Yes | 8.64 |
| 12 | [3.0, 7.0] | 7.0 3.0 | Yes | 7.86 |
| 13 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.76 |
| 14 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.38 |
| 15 | [2.9, 7.1] | 7.1 2.9 | Yes | 9.24 |
| 16 | [2.3, 7.7] | 2.3 7.7 | Yes | 5.94 |
| 17 | [0.1, 9.9] | 0.1 9.9 | Yes | 9.2 |
| 18 | [0.3, 9.7] | 0.3 9.7 | Yes | 5.64 |
| 19 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.06 |
| 20 | [0.9, 9.1] | 9.1 0.9 | Yes | 6.01 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4CI3W0PLCLWA | 4CI3W0PLCLWA | Yes | 1.93 |
| 2 | V5YOYZJSTMVP | V5YOYZJSTMVP | Yes | 0.84 |
| 3 | 31MTJKTV3XWF | 31MTJKTV3XWF | Yes | 1.83 |
| 4 | TVSE33QAKWJX | TVSE33QAKWJX | Yes | 0.92 |
| 5 | QMDRODYHC5A0 | QMDRODYHC5A0 | Yes | 1.05 |
| 6 | 2FTW8R5WPUFZ | 2FTW8R5WPUFZ | Yes | 1.43 |
| 7 | VFS2QTLSXH5L | VFS2QTLSXH5L | Yes | 1.08 |
| 8 | E6R4GO7IJ3MI | E6R4GO7IJ3MI | Yes | 0.95 |
| 9 | ODMFBFUBDE18 | ODMFBFUBDE18 | Yes | 1.57 |
| 10 | 3ZHVVD3ZZ63Q | 3ZHVVD3ZZ63Q | Yes | 1.59 |
| 11 | R7O5LLCROVAD | R7O5LLCROVAD | Yes | 0.99 |
| 12 | PMDQQJQDJTUE | PMDQQJQDJTUE | Yes | 2.28 |
| 13 | LN7OCUNSFNON | LN7OCUNSFNON | Yes | 3.36 |
| 14 | NEHSRUT20BEA | NEHSRUT20BEA | Yes | 4.3 |
| 15 | 689QDCUP9587 | 689QDCUP9587 | Yes | 1.89 |
| 16 | 54EU6Y2R2XQP | 54EU6Y2R2XQP | Yes | 1.4 |
| 17 | IJ0BQQVTIAKV | IJ0BQQVTIAKV | Yes | 4.28 |
| 18 | SKZV9QWT7X53 | SKZV9QWT7X53 | Yes | 1.78 |
| 19 | WRE3JPIQTUFY | WRE3JPIQTUFY | Yes | 0.9 |
| 20 | WKYG9DRDBJL1 | WKYG9DRDBJL1 | Yes | 3.79 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 5.15 |
| 2 | 23 | 23 | Yes | 5.72 |
| 3 | 19 | 19 | Yes | 3.63 |
| 4 | 198 | 198 | Yes | 5.63 |
| 5 | 39 | 39 | Yes | 4.65 |
| 6 | 26 | 26 | Yes | 9.03 |
| 7 | 48 | 48 | Yes | 3.65 |
| 8 | 1440 | 1440 | Yes | 4.45 |
| 9 | 5 | 5 | Yes | 4.67 |
| 10 | 7 | 7 | Yes | 2.95 |
| 11 | 63 | 63 | Yes | 1.72 |
| 12 | 1 | 1 | Yes | 4.49 |
| 13 | 67 | 67 | Yes | 3.51 |
| 14 | 73 | 73 | Yes | 5.4 |
| 15 | 20 |  | No | 82.63 |
| 16 | 9 | 9 | Yes | 5.53 |
| 17 | 5 |  | No | 67.15 |
| 18 | 4 | 4 | Yes | 5.04 |
| 19 | 10 | 10 | Yes | 4.97 |
| 20 | 793 | 793 | Yes | 3.82 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (/ </<(() | (/ </<(() | Yes | 6.53 |
| 2 | <<_((_)\) |  | No | 66.26 |
| 3 | <__ )( /( | <__ )( /( | Yes | 9.02 |
| 4 | _</\  /(< | _</\  /(< | Yes | 7.72 |
| 5 | )_\/ <(<\ | /\) <(_<) | No | 9.78 |
| 6 | ()_  /\(< | ()_  /\(< | Yes | 16.04 |
| 7 | /\)__<_)\ | /\)__<_)\ | Yes | 7.45 |
| 8 | <)_()_) ( | /\) <(_<) | No | 28.42 |
| 9 |  /<_)( _\ | /<_)( _\ | No | 4.29 |
| 10 | )<< \) __ | /\) <(_<) | No | 32.69 |
| 11 | ) //) )_\ | /\) <(_<) | No | 24.96 |
| 12 | //< \_\() | //< \_\() | Yes | 17.81 |
| 13 |  _/()/<\< | _/()/<\< | No | 13.59 |
| 14 | \  _\) /\ | _\) /\ | No | 7.27 |
| 15 | _(\(/(( ( |  | No | 39.78 |
| 16 | _< _(\\<( | _< _(\\<( | Yes | 22.16 |
| 17 | \ <//_/(( |  | No | 60.2 |
| 18 |  < _<(_(/ | < _<(_(/ | No | 3.94 |
| 19 | <\ _/\\_( | < _/\\_( | No | 14.56 |
| 20 | <\(\)<) \ | <\(\)<) \ | Yes | 9.89 |
