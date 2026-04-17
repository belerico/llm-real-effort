# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-26 16:32:04

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
| sudoku_game | 4435 | 38912 | 43347 | 0 | 20 | 64.09 | 1281.96 |
| add_numbers | 2420 | 3746 | 6166 | 20 | 0 | 6.00 | 120.03 |
| counting_zeros | 3820 | 37796 | 41616 | 14 | 6 | 43.65 | 872.9 |
| task_decoding | 3760 | 7851 | 11611 | 20 | 0 | 11.52 | 230.49 |
| task_summation | 4100 | 14012 | 18112 | 19 | 1 | 18.16 | 363.22 |
| task_transcription | 2561 | 3977 | 6538 | 20 | 0 | 4.47 | 89.45 |
| task_sequences | 2420 | 19449 | 21869 | 15 | 5 | 15.85 | 317.06 |
| string_entry | 2719 | 37110 | 39829 | 3 | 17 | 53.20 | 1063.94 |
| **TOTAL** | **26235** | **162853** | **189088** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 3 3 3 4 2 1 3 1 5 2 6 5 |  | No | 64.66 |
| 2 | 3 1 1 2 3 4 5 6 4 5 6 1 6 3 |  | No | 44.87 |
| 3 | 2 1 4 5 6 4 6 1 3 6 1 3 4 6 |  | No | 53.2 |
| 4 | 4 1 3 6 5 4 6 4 5 1 2 3 6 5 |  | No | 55.13 |
| 5 | 2 3 4 6 1 2 5 2 3 2 6 4 3 1 |  | No | 62.96 |
| 6 | 1 3 3 6 5 2 2 3 1 4 3 2 1 3 |  | No | 53.93 |
| 7 | 2 4 2 6 6 4 2 6 3 4 2 6 3 5 |  | No | 58.05 |
| 8 | 1 3 6 5 3 1 5 2 3 5 1 4 5 1 |  | No | 52.11 |
| 9 | 5 3 6 2 4 5 3 6 6 3 4 4 1 2 |  | No | 51.92 |
| 10 | 1 2 4 1 6 4 3 6 4 5 4 3 1 4 |  | No | 67.97 |
| 11 | 4 3 3 4 2 6 1 6 4 6 5 3 4 2 |  | No | 61.68 |
| 12 | 1 4 6 3 1 4 3 1 6 2 2 5 1 3 |  | No | 77.18 |
| 13 | 6 3 1 2 3 1 5 2 4 5 6 4 1 5 |  | No | 57.92 |
| 14 | 2 6 5 4 1 6 5 4 1 3 2 4 1 5 |  | No | 57.99 |
| 15 | 1 3 3 2 5 3 2 4 4 1 3 4 4 5 |  | No | 61.15 |
| 16 | 3 5 1 4 6 6 3 2 6 5 4 2 5 1 |  | No | 71.27 |
| 17 | 3 6 6 3 4 2 1 6 4 3 6 5 1 4 |  | No | 74.21 |
| 18 | 1 2 1 2 1 3 2 6 4 3 6 2 5 1 |  | No | 67.62 |
| 19 | 1 5 2 1 3 1 1 4 2 3 5 1 6 4 |  | No | 68.05 |
| 20 | 3 4 2 1 2 1 6 4 5 2 6 3 2 5 | TIMEOUT | No | 120.03 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1598 | 1598 | Yes | 3.45 |
| 2 | 2095 | 2095 | Yes | 5.64 |
| 3 | 1666 | 1666 | Yes | 3.93 |
| 4 | 997 | 997 | Yes | 8.04 |
| 5 | 1648 | 1648 | Yes | 10.78 |
| 6 | 2616 | 2616 | Yes | 7.4 |
| 7 | 1232 | 1232 | Yes | 5.08 |
| 8 | 1412 | 1412 | Yes | 5.88 |
| 9 | 818 | 818 | Yes | 3.81 |
| 10 | 2363 | 2363 | Yes | 4.02 |
| 11 | 2163 | 2163 | Yes | 6.98 |
| 12 | 1721 | 1721 | Yes | 8.74 |
| 13 | 1678 | 1678 | Yes | 6.88 |
| 14 | 1105 | 1105 | Yes | 5.83 |
| 15 | 2349 | 2349 | Yes | 6.15 |
| 16 | 1338 | 1338 | Yes | 5.03 |
| 17 | 1909 | 1909 | Yes | 6.24 |
| 18 | 2228 | 2228 | Yes | 4.53 |
| 19 | 1201 | 1201 | Yes | 7.0 |
| 20 | 2628 | 2628 | Yes | 4.61 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 58.31 |
| 2 | 40 | 40 | Yes | 47.85 |
| 3 | 43 | 43 | Yes | 33.71 |
| 4 | 42 | 42 | Yes | 44.48 |
| 5 | 58 |  | No | 61.4 |
| 6 | 41 | 41 | Yes | 44.61 |
| 7 | 43 | 43 | Yes | 43.83 |
| 8 | 52 | 52 | Yes | 41.12 |
| 9 | 38 | 37 | No | 43.12 |
| 10 | 37 | 37 | Yes | 38.13 |
| 11 | 67 | 67 | Yes | 28.26 |
| 12 | 39 | 39 | Yes | 30.14 |
| 13 | 49 | 49 | Yes | 35.27 |
| 14 | 59 | 59 | Yes | 36.43 |
| 15 | 48 | 48 | Yes | 31.6 |
| 16 | 60 | 60 | Yes | 47.47 |
| 17 | 69 |  | No | 61.52 |
| 18 | 43 |  | No | 64.81 |
| 19 | 65 |  | No | 55.06 |
| 20 | 38 | 38 | Yes | 25.79 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VBENPLI | VBENPLI | Yes | 8.79 |
| 2 | GXUNTWB | GXUNTWB | Yes | 9.6 |
| 3 | HJKPGCL | HJKPGCL | Yes | 10.18 |
| 4 | CKMAJUV | CKMAJUV | Yes | 9.42 |
| 5 | LHQNCWG | LHQNCWG | Yes | 11.49 |
| 6 | LKQGOXM | LKQGOXM | Yes | 13.16 |
| 7 | YLHVIPR | YLHVIPR | Yes | 8.45 |
| 8 | WRLFOXT | WRLFOXT | Yes | 20.01 |
| 9 | GJILFXZ | GJILFXZ | Yes | 11.91 |
| 10 | RIVMZWC | RIVMZWC | Yes | 14.86 |
| 11 | JHBRXIN | JHBRXIN | Yes | 8.81 |
| 12 | YKMURFC | YKMURFC | Yes | 7.49 |
| 13 | IYSPETL | IYSPETL | Yes | 6.94 |
| 14 | JDXQVTW | JDXQVTW | Yes | 8.38 |
| 15 | QBASDVF | QBASDVF | Yes | 10.98 |
| 16 | DUOCMIE | DUOCMIE | Yes | 15.4 |
| 17 | QTGMHJI | QTGMHJI | Yes | 7.91 |
| 18 | TFARPEO | TFARPEO | Yes | 24.9 |
| 19 | LQZNYKG | LQZNYKG | Yes | 9.53 |
| 20 | EXGVOPI | EXGVOPI | Yes | 12.26 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 1.5 8.5 | Yes | 15.69 |
| 2 | [1.8, 8.2] | 8.2 1.8 | Yes | 17.03 |
| 3 | [0.1, 9.9] | 9.9 0.1 | Yes | 17.73 |
| 4 | [4.2, 5.8] | 5.8 4.2 | Yes | 17.11 |
| 5 | [3.9, 6.1] | 6.1 3.9 | Yes | 17.19 |
| 6 | [4.8, 5.2] | 5.2 4.8 | Yes | 15.47 |
| 7 | [4.4, 5.6] | 5.6 4.4 | Yes | 14.76 |
| 8 | [0.3, 9.7] | 9.7 0.3 | Yes | 12.67 |
| 9 | [4.3, 5.7] | 4.3 5.7 | Yes | 15.26 |
| 10 | [0.5, 9.5] | 0.5 9.5 | Yes | 15.4 |
| 11 | [0.8, 9.2] | 0.8 9.2 | Yes | 20.45 |
| 12 | [3.6, 6.4] | 6.4 3.6 | Yes | 17.02 |
| 13 | [0.6, 9.4] | 9.4 0.6 | Yes | 16.21 |
| 14 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.56 |
| 15 | [3.1, 6.9] | 3.1 6.9 | Yes | 13.96 |
| 16 | [0.2, 9.8] |  | No | 65.92 |
| 17 | [2.8, 7.2] | 2.8 7.2 | Yes | 12.02 |
| 18 | [4.6, 5.4] | 4.6 5.4 | Yes | 12.71 |
| 19 | [4.2, 5.8] | 5.8 4.2 | Yes | 16.74 |
| 20 | [4.1, 5.9] | 5.9 4.1 | Yes | 16.31 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7HBFBY4E073K | 7HBFBY4E073K | Yes | 5.91 |
| 2 | NGQKOCRBYHYW | NGQKOCRBYHYW | Yes | 2.24 |
| 3 | 3O1FLWFUN8PO | 3O1FLWFUN8PO | Yes | 3.75 |
| 4 | OGLU890RTCYH | OGLU890RTCYH | Yes | 3.78 |
| 5 | MGB2NJQCSLPQ | MGB2NJQCSLPQ | Yes | 5.39 |
| 6 | 8E3F6TEL0FQW | 8E3F6TEL0FQW | Yes | 2.19 |
| 7 | UX0O8OZ47GL4 | UX0O8OZ47GL4 | Yes | 2.03 |
| 8 | YBT1JY9H519Y | YBT1JY9H519Y | Yes | 4.25 |
| 9 | 098C04H7TQ5P | 098C04H7TQ5P | Yes | 5.17 |
| 10 | TVMHALEGOI4Y | TVMHALEGOI4Y | Yes | 7.51 |
| 11 | T57RXLCYMWRJ | T57RXLCYMWRJ | Yes | 2.93 |
| 12 | 1FJVU6C4VFCF | 1FJVU6C4VFCF | Yes | 2.27 |
| 13 | DKH91AXS08KS | DKH91AXS08KS | Yes | 8.69 |
| 14 | C6W31JJ8XCEP | C6W31JJ8XCEP | Yes | 8.69 |
| 15 | PNCBMDIZ3H4J | PNCBMDIZ3H4J | Yes | 3.21 |
| 16 | 0P03246AC880 | 0P03246AC880 | Yes | 4.25 |
| 17 | 2IN2OZEVCA9T | 2IN2OZEVCA9T | Yes | 5.74 |
| 18 | 0NC01PAIQHH9 | 0NC01PAIQHH9 | Yes | 6.32 |
| 19 | FR3MXXH05C2A | FR3MXXH05C2A | Yes | 3.24 |
| 20 | 130WY16QOJUW | 130WY16QOJUW | Yes | 1.88 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 42 | No | 8.65 |
| 2 | 4 | 4 | Yes | 19.09 |
| 3 | 23 | 23 | Yes | 12.01 |
| 4 | 31 | 31 | Yes | 19.26 |
| 5 | 793 | 793 | Yes | 17.3 |
| 6 | 7 | 7 | Yes | 5.45 |
| 7 | 1440 | 1440 | Yes | 18.39 |
| 8 | 5 | 5 | Yes | 21.99 |
| 9 | 60 | 60 | Yes | 10.42 |
| 10 | 60 | 42 | No | 9.34 |
| 11 | 198 | 198 | Yes | 20.67 |
| 12 | 7680 | 7680 | Yes | 10.03 |
| 13 | 10 | 10 | Yes | 29.15 |
| 14 | 63 | 42 | No | 11.72 |
| 15 | 73 | 73 | Yes | 3.48 |
| 16 | 5 | 42 | No | 20.11 |
| 17 | 64 | 64 | Yes | 24.86 |
| 18 | 26 | 42 | No | 5.5 |
| 19 | 44 | 44 | Yes | 24.29 |
| 20 | 28 | 28 | Yes | 25.33 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ))_\)< /( |  | No | 46.17 |
| 2 |  )_)_(\_( | /\) <(_<) | No | 27.57 |
| 3 | /( \<<\)( | /( \<<\)( | Yes | 16.27 |
| 4 | \<\)\()\_ |  | No | 32.67 |
| 5 | /<<//</(( | /<<//</(( | Yes | 24.53 |
| 6 | ( <)(<<_/ |  | No | 62.46 |
| 7 |  ___ )(/( |  | No | 43.55 |
| 8 |  /\<<\  / |  | No | 59.71 |
| 9 |  \\ _ _/< |  | No | 64.6 |
| 10 | \  \)( \< | \  \)( \< | Yes | 35.77 |
| 11 |  )/)\(/(/ |  | No | 67.19 |
| 12 | /_<))\<_) |  | No | 64.45 |
| 13 | / /\<< )\ |  | No | 66.85 |
| 14 | < <) \</( |  | No | 55.29 |
| 15 | (()/(( __ |  | No | 52.16 |
| 16 | <\<))) </ |  | No | 63.8 |
| 17 | /)()<<_ \ |  | No | 54.0 |
| 18 | ) \(_)/// | TIMEOUT | No | 120.04 |
| 19 |  \\_( )_( |  | No | 66.29 |
| 20 | ) < (<\\< |  | No | 40.55 |
