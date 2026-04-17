# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 9264 | 34108 | 43372 | 0 | 20 | 17.68 | 353.8 |
| add_numbers | 37694 | 7212 | 44906 | 20 | 0 | 5.91 | 118.34 |
| counting_zeros | 22362 | 31603 | 53965 | 10 | 10 | 23.88 | 477.98 |
| task_decoding | 43854 | 7719 | 51573 | 19 | 1 | 7.48 | 149.81 |
| task_summation | 27180 | 19983 | 47163 | 20 | 0 | 11.27 | 225.52 |
| task_transcription | 26900 | 9659 | 36559 | 19 | 1 | 7.53 | 150.66 |
| task_sequences | 3347 | 18068 | 21415 | 19 | 1 | 9.74 | 194.91 |
| **TOTAL** | **170601** | **128352** | **298953** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 5 1 2 6 3 1 4 6 1 5 3 1 | 2 1 5 1 2 1 6 3 4 6 1 3 1 5 3 1 5 | No | 15.17 |
| 2 | 1 2 3 2 3 6 6 6 3 4 2 5 2 1 |  | No | 40.77 |
| 3 | 2 5 2 5 1 3 6 1 2 5 5 3 4 3 | 2 5 2 5 1 5 2 3 1 5 1 3 4 3 4 | No | 15.99 |
| 4 | 6 4 2 1 6 4 4 6 2 4 5 1 5 2 | 4 6 1 2 4 6 4 2 5 2 1 5 2 5 | No | 15.03 |
| 5 | 4 3 1 5 3 5 3 2 4 6 4 5 6 4 | 4 3 1 5 3 5 2 3 4 6 5 4 6 4 5 | No | 14.9 |
| 6 | 6 1 5 4 2 6 1 6 2 1 6 1 5 3 | 6 5 4 6 1 2 1 6 2 6 2 1 1 3 5 3 5 | No | 16.16 |
| 7 | 5 1 3 4 3 2 6 2 1 4 5 6 3 4 | 5 3 1 3 4 2 6 2 6 1 2 4 5 3 4 6 3 4 6 | No | 15.4 |
| 8 | 1 4 3 5 4 5 1 2 3 6 3 6 6 4 | 1 3 4 5 4 1 5 2 6 3 3 6 6 4 | No | 16.28 |
| 9 | 3 5 5 1 1 4 5 3 4 3 5 5 2 4 | 3 5 5 1 1 4 5 3 4 3 5 3 5 4 5 2 2 4 1 5 | No | 14.25 |
| 10 | 2 1 2 1 6 2 6 3 2 1 5 1 3 6 | 2 1 2 1 6 2 1 6 2 1 6 3 1 5 6 3 5 1 3 6 | No | 14.49 |
| 11 | 3 2 6 3 6 5 4 1 3 4 6 3 4 2 | 3 6 2 3 5 4 3 6 4 3 4 3 4 2 | No | 14.92 |
| 12 | 4 1 6 3 6 5 2 1 4 6 4 5 6 3 | 4 6 1 3 6 5 2 5 4 1 6 5 4 6 5 6 3 | No | 15.12 |
| 13 | 2 5 4 6 4 5 1 3 5 5 5 1 4 3 | 2 5 4 5 4 5 1 3 5 3 5 1 3 5 4 3 1 | No | 13.89 |
| 14 | 4 5 6 1 6 2 5 4 5 1 6 3 2 4 | 4 5 5 1 6 2 5 6 4 5 3 4 1 6 4 2 4 2 6 3 4 | No | 16.74 |
| 15 | 4 5 3 2 3 5 2 4 1 6 3 3 6 1 | 5 4 2 3 3 5 4 2 1 3 6 1 6 1 6 1 | No | 16.22 |
| 16 | 4 4 2 2 6 1 2 1 5 5 5 2 1 3 | 4 4 2 2 1 6 5 2 5 5 1 5 3 2 5 3 1 | No | 14.29 |
| 17 | 5 6 1 4 5 2 3 3 5 4 3 2 3 5 | 5 1 6 4 2 5 3 5 3 4 2 3 5 3 2 5 4 | No | 15.56 |
| 18 | 3 5 4 1 3 6 4 6 1 3 5 2 5 3 | 3 4 5 1 3 6 4 6 3 1 5 3 5 1 5 3 | No | 20.96 |
| 19 | 1 2 4 2 5 1 3 2 5 2 1 4 3 5 | , 3. Column 3 has 6, 5, 3. R3C3: Row 3 has 2, 6, 5, 4. Column 3 has | No | 32.47 |
| 20 | 3 4 3 6 1 5 2 4 6 3 1 2 1 6 | 3 4 1 3 6 5 2 6 4 6 2 1 1 2 6 1 6 3 | No | 15.0 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 730 | 730 | Yes | 5.29 |
| 2 | 1431 | 1431 | Yes | 5.46 |
| 3 | 2184 | 2184 | Yes | 5.76 |
| 4 | 2848 | 2848 | Yes | 5.48 |
| 5 | 1494 | 1494 | Yes | 5.33 |
| 6 | 1478 | 1478 | Yes | 4.35 |
| 7 | 1675 | 1675 | Yes | 7.26 |
| 8 | 1777 | 1777 | Yes | 4.81 |
| 9 | 1893 | 1893 | Yes | 4.61 |
| 10 | 2134 | 2134 | Yes | 4.92 |
| 11 | 1407 | 1407 | Yes | 4.93 |
| 12 | 1158 | 1158 | Yes | 5.59 |
| 13 | 1660 | 1660 | Yes | 4.95 |
| 14 | 1210 | 1210 | Yes | 6.46 |
| 15 | 2334 | 2334 | Yes | 4.65 |
| 16 | 1495 | 1495 | Yes | 7.74 |
| 17 | 2451 | 2451 | Yes | 6.83 |
| 18 | 1718 | 1718 | Yes | 15.15 |
| 19 | 1839 | 1839 | Yes | 4.7 |
| 20 | 1199 | 1199 | Yes | 3.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 69 | 68 | No | 14.68 |
| 2 | 70 | 70 | Yes | 15.21 |
| 3 | 48 |  | No | 35.29 |
| 4 | 43 | 43 | Yes | 13.09 |
| 5 | 75 | 74 | No | 23.25 |
| 6 | 37 | 37 | Yes | 16.28 |
| 7 | 71 | 70 | No | 14.48 |
| 8 | 73 | 72 | No | 12.23 |
| 9 | 38 | 38 | Yes | 23.7 |
| 10 | 45 | 45 | Yes | 14.62 |
| 11 | 41 | TIMEOUT | No | 120.02 |
| 12 | 37 | 37 | Yes | 14.81 |
| 13 | 60 | 60 | Yes | 16.26 |
| 14 | 69 | 70 | No | 14.46 |
| 15 | 57 | 57 | Yes | 23.35 |
| 16 | 66 | 66 | Yes | 15.71 |
| 17 | 62 | 62 | Yes | 23.63 |
| 18 | 72 | 71 | No | 15.32 |
| 19 | 71 | 70 | No | 14.83 |
| 20 | 65 |  | No | 36.46 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | UKIZVEO | UKIZVEO | Yes | 6.3 |
| 2 | YQPRANT | YQPRANT | Yes | 6.24 |
| 3 | GBAENHC | GBAENHC | Yes | 7.61 |
| 4 | MGVRIFC | MGVRIFC | Yes | 8.61 |
| 5 | YZQRNHU | YZQRNHU | Yes | 5.74 |
| 6 | QNPIVHE | QNPIVHE | Yes | 15.4 |
| 7 | DIROKNB | DIROKNB | Yes | 4.48 |
| 8 | KHBIGEF | KHBIGEF | Yes | 7.71 |
| 9 | INWXZMQ | INWXZMQ | Yes | 5.39 |
| 10 | JYILDKS | JYILDKS | Yes | 5.53 |
| 11 | MQNIESA | MQNIESA | Yes | 5.97 |
| 12 | XFWLJZN | XFWLJZN | Yes | 4.63 |
| 13 | ECYRQGN | ECYRQGN | Yes | 4.48 |
| 14 | AJFILWS | AJFILWS | Yes | 4.92 |
| 15 | MGLZIOT | MGLZIOT | Yes | 15.11 |
| 16 | SGIWCXU | SGIWCXU | Yes | 15.54 |
| 17 | RPXHWJL | RPXHWJL | Yes | 5.78 |
| 18 | IKWRAON | IKWRAN | No | 6.16 |
| 19 | GIPLQXK | GIPLQXK | Yes | 5.55 |
| 20 | OPYIVNS | OPYIVNS | Yes | 8.43 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.95 |
| 2 | [1.3, 8.7] | 1.3 8.7 | Yes | 13.35 |
| 3 | [4.8, 5.2] | 4.8 5.2 | Yes | 10.5 |
| 4 | [5.0, 5.0] | 5.0 5.0 | Yes | 12.01 |
| 5 | [4.1, 5.9] | 5.9 4.1 | Yes | 9.22 |
| 6 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.49 |
| 7 | [1.0, 9.0] | 9.0 1.0 | Yes | 10.26 |
| 8 | [0.7, 9.3] | 9.3 0.7 | Yes | 10.0 |
| 9 | [0.2, 9.8] | 9.8 0.2 | Yes | 13.7 |
| 10 | [4.9, 5.1] | 5.1 4.9 | Yes | 8.68 |
| 11 | [3.9, 6.1] | 3.9 6.1 | Yes | 10.13 |
| 12 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.54 |
| 13 | [2.9, 7.1] | 7.1 2.9 | Yes | 21.18 |
| 14 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.23 |
| 15 | [0.9, 9.1] | 0.9 9.1 | Yes | 11.26 |
| 16 | [3.0, 7.0] | 3.0 7.0 | Yes | 19.15 |
| 17 | [0.5, 9.5] | 9.5 0.5 | Yes | 10.94 |
| 18 | [3.2, 6.8] | 3.2 6.8 | Yes | 9.38 |
| 19 | [1.5, 8.5] | 1.5 8.5 | Yes | 8.53 |
| 20 | [1.3, 8.7] | 8.7 1.3 | Yes | 10.85 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XZD6ZIECVV9X | XZD6ZIECVV9X | Yes | 14.77 |
| 2 | 91S347414KZ8 | 91S347414KZ8 | Yes | 15.43 |
| 3 | OOPMV7TCMBA5 | OOPMV7TCMBA5 | Yes | 5.29 |
| 4 | FMUK7LPAH9A8 | FMUK7LPAH9A8 | Yes | 5.92 |
| 5 | EKNOHW0TSEKO | EKNOHWOTSEKO | No | 5.92 |
| 6 | BT4F5J6C2MQO | BT4F5J6C2MQO | Yes | 10.54 |
| 7 | FM0VXZHJ5ZOV | FM0VXZHJ5ZOV | Yes | 6.3 |
| 8 | 4WM3TAA75YNL | 4WM3TAA75YNL | Yes | 6.46 |
| 9 | U70WO7566DDC | U70WO7566DDC | Yes | 10.95 |
| 10 | UYJ34MT5XPSO | UYJ34MT5XPSO | Yes | 5.99 |
| 11 | G8ROCYFULCD5 | G8ROCYFULCD5 | Yes | 5.96 |
| 12 | FLE8S2BCJK7F | FLE8S2BCJK7F | Yes | 7.68 |
| 13 | 4SEMUL4C2WAP | 4SEMUL4C2WAP | Yes | 5.5 |
| 14 | REVX8U4NVI0Z | REVX8U4NVI0Z | Yes | 5.86 |
| 15 | L08R0IYQI4RQ | L08R0IYQI4RQ | Yes | 8.85 |
| 16 | GGSHF49X1DJZ | GGSHF49X1DJZ | Yes | 6.8 |
| 17 | BMLCYS3GA7R0 | BMLCYS3GA7R0 | Yes | 5.17 |
| 18 | XX1IEW9U03WH | XX1IEW9U03WH | Yes | 5.75 |
| 19 | AK1TY4N35M2S | AK1TY4N35M2S | Yes | 5.11 |
| 20 | 5R2KWSUM3J89 | 5R2KWSUM3J89 | Yes | 6.32 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 8.58 |
| 2 | 16 | 16 | Yes | 8.48 |
| 3 | 10 | 10 | Yes | 13.72 |
| 4 | 243 | 243 | Yes | 9.25 |
| 5 | 3 | 3 | Yes | 16.87 |
| 6 | 4096 | 65536 | No | 14.29 |
| 7 | 1440 | 1440 | Yes | 9.58 |
| 8 | 31 | 31 | Yes | 6.62 |
| 9 | 9 | 9 | Yes | 9.05 |
| 10 | 67 | 67 | Yes | 5.82 |
| 11 | 19 | 19 | Yes | 6.31 |
| 12 | 3 | 3 | Yes | 12.27 |
| 13 | 26 | 26 | Yes | 16.22 |
| 14 | 1 | 1 | Yes | 7.9 |
| 15 | 39 | 39 | Yes | 7.57 |
| 16 | 20 | 20 | Yes | 10.88 |
| 17 | 198 | 198 | Yes | 10.58 |
| 18 | 60 | 60 | Yes | 6.55 |
| 19 | 65 | 65 | Yes | 7.92 |
| 20 | 7 | 7 | Yes | 6.42 |
