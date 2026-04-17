# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 10:44:02

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
| sudoku_game | 7200 | 36038 | 43238 | 7 | 13 | 21.84 | 436.95 |
| add_numbers | 3780 | 1590 | 5370 | 20 | 0 | 3.58 | 71.65 |
| counting_zeros | 6200 | 29234 | 35434 | 4 | 16 | 12.84 | 257.07 |
| task_decoding | 11940 | 3538 | 15478 | 20 | 0 | 4.31 | 86.46 |
| task_summation | 7140 | 6612 | 13752 | 20 | 0 | 5.37 | 107.53 |
| task_transcription | 3613 | 10609 | 14222 | 17 | 3 | 9.39 | 187.95 |
| task_sequences | 2900 | 5639 | 8539 | 18 | 2 | 5.89 | 117.78 |
| string_entry | 4200 | 31029 | 35229 | 9 | 11 | 23.57 | 471.45 |
| **TOTAL** | **46973** | **124289** | **171262** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 6 6 3 5 6 6 3 1 6 1 2 6 |  | No | 30.16 |
| 2 | 1 3 5 4 3 5 1 6 3 4 5 2 6 4 | 1 3 5 4 3 5 1 6 3 4 5 2 6 4 | Yes | 16.35 |
| 3 | 1 4 3 2 2 4 3 5 4 3 2 4 1 1 |  | No | 24.09 |
| 4 | 2 6 1 3 6 1 5 3 1 4 2 3 4 1 | 2 6 1 3 6 1 5 3 1 4 2 3 4 1 | Yes | 14.08 |
| 5 | 3 2 5 4 6 6 2 5 3 4 1 6 3 1 |  | No | 23.51 |
| 6 | 1 6 6 2 5 3 4 6 2 5 4 6 3 1 |  | No | 45.82 |
| 7 | 2 1 5 6 3 3 1 2 1 6 4 1 6 3 | 2 1 5 6 3 3 1 2 1 6 4 1 6 3 | Yes | 14.7 |
| 8 | 6 5 4 3 6 6 3 5 2 4 1 6 1 3 |  | No | 39.77 |
| 9 | 5 4 1 6 4 3 4 5 3 1 5 4 2 1 |  | No | 15.1 |
| 10 | 2 4 1 3 5 4 2 6 5 4 4 2 6 4 |  | No | 17.42 |
| 11 | 1 1 2 5 6 3 5 4 1 2 4 2 5 3 |  | No | 18.66 |
| 12 | 5 3 6 1 2 3 2 1 2 6 3 4 5 6 |  | No | 19.13 |
| 13 | 4 3 3 5 6 2 6 3 5 5 4 3 6 1 | 4 3 3 5 6 2 6 3 5 5 4 3 6 1 | Yes | 14.18 |
| 14 | 6 2 6 3 3 4 6 3 4 5 5 6 3 4 |  | No | 16.8 |
| 15 | 3 1 2 1 4 3 3 6 1 2 1 3 5 4 | 3 1 2 1 4 3 3 6 1 2 1 3 5 4 | Yes | 10.55 |
| 16 | 6 4 3 2 4 3 6 2 6 3 5 4 2 5 |  | No | 20.72 |
| 17 | 6 1 6 4 4 2 6 1 1 3 4 1 2 1 |  | No | 24.95 |
| 18 | 2 3 6 6 5 4 3 2 4 3 3 6 4 1 |  | No | 37.44 |
| 19 | 2 5 6 2 4 2 2 4 3 5 2 4 2 3 | 2 5 6 2 4 2 2 4 3 5 2 4 2 3 | Yes | 19.39 |
| 20 | 3 4 6 4 2 6 2 5 3 6 4 2 5 1 | 3 4 6 4 2 6 2 5 3 6 4 2 5 1 | Yes | 13.94 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1579 | 1579 | Yes | 4.12 |
| 2 | 1370 | 1370 | Yes | 2.7 |
| 3 | 1932 | 1932 | Yes | 3.26 |
| 4 | 2172 | 2172 | Yes | 3.39 |
| 5 | 1836 | 1836 | Yes | 3.91 |
| 6 | 1308 | 1308 | Yes | 4.1 |
| 7 | 1675 | 1675 | Yes | 3.7 |
| 8 | 1634 | 1634 | Yes | 4.17 |
| 9 | 1294 | 1294 | Yes | 3.62 |
| 10 | 1684 | 1684 | Yes | 3.29 |
| 11 | 2519 | 2519 | Yes | 3.86 |
| 12 | 1622 | 1622 | Yes | 3.06 |
| 13 | 1069 | 1069 | Yes | 3.04 |
| 14 | 2773 | 2773 | Yes | 3.31 |
| 15 | 2060 | 2060 | Yes | 4.28 |
| 16 | 2363 | 2363 | Yes | 3.12 |
| 17 | 2489 | 2489 | Yes | 3.45 |
| 18 | 1705 | 1705 | Yes | 4.71 |
| 19 | 1310 | 1310 | Yes | 3.38 |
| 20 | 2234 | 2234 | Yes | 3.09 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 9.05 |
| 2 | 42 | 42 | Yes | 7.73 |
| 3 | 53 | 55 | No | 10.63 |
| 4 | 56 |  | No | 15.43 |
| 5 | 70 | 69 | No | 12.98 |
| 6 | 50 |  | No | 11.39 |
| 7 | 74 |  | No | 9.75 |
| 8 | 55 |  | No | 23.93 |
| 9 | 40 | 40 | Yes | 7.44 |
| 10 | 55 | 53 | No | 7.84 |
| 11 | 71 | 67 | No | 10.55 |
| 12 | 63 | 63 | Yes | 13.25 |
| 13 | 44 | 45 | No | 13.98 |
| 14 | 58 |  | No | 19.43 |
| 15 | 69 |  | No | 22.56 |
| 16 | 54 | 52 | No | 9.67 |
| 17 | 73 |  | No | 18.13 |
| 18 | 40 | 33 | No | 6.63 |
| 19 | 54 | 53 | No | 13.59 |
| 20 | 68 | 67 | No | 12.82 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KOUCMRB | KOUCMRB | Yes | 4.18 |
| 2 | RMAPEFK | RMAPEFK | Yes | 3.73 |
| 3 | AXBOJEU | AXBOJEU | Yes | 4.72 |
| 4 | KTDZQBE | KTDZQBE | Yes | 4.71 |
| 5 | NZCSKAU | NZCSKAU | Yes | 4.38 |
| 6 | UPWLRDN | UPWLRDN | Yes | 4.97 |
| 7 | XVQHKGZ | XVQHKGZ | Yes | 4.7 |
| 8 | PVBWLKX | PVBWLKX | Yes | 3.98 |
| 9 | CTQJUYX | CTQJUYX | Yes | 4.5 |
| 10 | LVCYMIN | LVCYMIN | Yes | 4.84 |
| 11 | JWFHNOI | JWFHNOI | Yes | 2.47 |
| 12 | MVTHFJK | MVTHFJK | Yes | 4.83 |
| 13 | WYGXLIN | WYGXLIN | Yes | 4.31 |
| 14 | BZUIWRK | BZUIWRK | Yes | 4.29 |
| 15 | YBITWJV | YBITWJV | Yes | 3.88 |
| 16 | QOHYVTS | QOHYVTS | Yes | 4.15 |
| 17 | YWLRXUK | YWLRXUK | Yes | 5.01 |
| 18 | MHWQZPL | MHWQZPL | Yes | 3.57 |
| 19 | HNCIFXE | HNCIFXE | Yes | 3.84 |
| 20 | XGCBASM | XGCBASM | Yes | 5.22 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.0, 9.0] | 9.0 1.0 | Yes | 8.3 |
| 2 | [4.5, 5.5] | 5.5 4.5 | Yes | 5.3 |
| 3 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.44 |
| 4 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.66 |
| 5 | [4.4, 5.6] | 5.6 4.4 | Yes | 5.35 |
| 6 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.28 |
| 7 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.12 |
| 8 | [1.1, 8.9] | 8.9 1.1 | Yes | 4.52 |
| 9 | [1.6, 8.4] | 8.4 1.6 | Yes | 4.81 |
| 10 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.39 |
| 11 | [1.9, 8.1] | 1.9 8.1 | Yes | 4.84 |
| 12 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.78 |
| 13 | [3.7, 6.3] | 3.7 6.3 | Yes | 4.21 |
| 14 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.05 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.96 |
| 16 | [2.2, 7.8] | 7.8 2.2 | Yes | 4.74 |
| 17 | [4.2, 5.8] | 4.2 5.8 | Yes | 4.66 |
| 18 | [4.2, 5.8] | 4.2 5.8 | Yes | 5.12 |
| 19 | [3.9, 6.1] | 3.9 6.1 | Yes | 5.0 |
| 20 | [2.2, 7.8] | 7.8 2.2 | Yes | 5.84 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6ZW42CYMTED0 | 6ZW42CYMTED0 | Yes | 7.9 |
| 2 | WHIP1UA1ZD4R | WHIP1UA1ZD4R | Yes | 23.71 |
| 3 | DRKHMB7HIKB2 | DRKHMB7HIKB2 | Yes | 7.94 |
| 4 | XVDGND6T1AEP | XVDGND6T1AEP | Yes | 5.39 |
| 5 | 1XOQ9URA1QE6 | 1XOQ9URA1QE6 | Yes | 3.16 |
| 6 | ICLG5GX6T1U2 | ICLG5GX6T1U2 | Yes | 8.65 |
| 7 | M832RYL623I5 | M832RYL62315 | No | 6.47 |
| 8 | NI7XUJL8NORA | NI7XUJL8NORA | Yes | 6.84 |
| 9 | P0XGC2VHQFQU |  | No | 32.0 |
| 10 | 4PGH0JEYZA36 | 4PGH0JEYZA36 | Yes | 7.02 |
| 11 | 6ROYQZO1G8PC | 6R0YQZ01G8PC | No | 18.98 |
| 12 | UOYRWJOBGOVX | UOYRWJOBGOVX | Yes | 6.33 |
| 13 | X66DLSGHNHXR | X66DLSGHNHXR | Yes | 5.93 |
| 14 | WNUMTBMJH4LX | WNUMTBMJH4LX | Yes | 5.61 |
| 15 | ZA1Y8ZUDHVHK | ZA1Y8ZUDHVHK | Yes | 6.17 |
| 16 | B4PPEHU55H0Z | B4PPEHU55H0Z | Yes | 12.27 |
| 17 | 5G4CC7FF9XWL | 5G4CC7FF9XWL | Yes | 6.09 |
| 18 | DERJW8C11YPC | DERJW8C11YPC | Yes | 8.25 |
| 19 | Q03YCCUXG1ZF | Q03YCCUXG1ZF | Yes | 2.8 |
| 20 | PXJQ7L5DMEJ2 | PXJQ7L5DMEJ2 | Yes | 6.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 243 | 243 | Yes | 2.92 |
| 2 | 6 | 6 | Yes | 3.5 |
| 3 | 9 | 9 | Yes | 3.47 |
| 4 | 1440 | 1440 | Yes | 3.64 |
| 5 | 26 |  | No | 29.14 |
| 6 | 20 |  | No | 25.62 |
| 7 | 65 | 65 | Yes | 3.12 |
| 8 | 60 | 60 | Yes | 4.11 |
| 9 | 19 | 19 | Yes | 3.37 |
| 10 | 31 | 31 | Yes | 3.29 |
| 11 | 793 | 793 | Yes | 3.17 |
| 12 | 36 | 36 | Yes | 2.78 |
| 13 | 44 | 44 | Yes | 3.59 |
| 14 | 4 | 4 | Yes | 3.68 |
| 15 | 63 | 63 | Yes | 3.36 |
| 16 | 3 | 3 | Yes | 4.75 |
| 17 | 7 | 7 | Yes | 2.92 |
| 18 | 7680 | 7680 | Yes | 4.43 |
| 19 | 48 | 48 | Yes | 3.84 |
| 20 | 73 | 73 | Yes | 3.09 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (\)/ /_<_ |  | No | 25.61 |
| 2 | <\ \<< <\ | <\ \< <\ | No | 8.61 |
| 3 |  )) ( \\\ |  | No | 31.75 |
| 4 | _)  _ )\< | _)  _ )\< | Yes | 20.01 |
| 5 | (/<_ \</\ |  | No | 35.76 |
| 6 | )((<\_)__ |  | No | 35.38 |
| 7 | (_<\_)< ( | (_<\_)< ( | Yes | 9.61 |
| 8 | \  _ \(\  |  | No | 36.17 |
| 9 | /  \/)< ( | /  \/)< ( | Yes | 12.25 |
| 10 | _ </ /(/< |  | No | 26.98 |
| 11 | /_)_\)_ / |  | No | 44.06 |
| 12 | __ _(/(\( |  | No | 28.01 |
| 13 | / _ <<\(\ | / _ <<\(\ | Yes | 18.46 |
| 14 | </\)\(_/) | </\)\(_/) | Yes | 9.72 |
| 15 | (\(</\((_ |  | No | 32.93 |
| 16 | \(_( _<<_ | \(_( _<<_ | Yes | 12.84 |
| 17 | //  /)(/< |  | No | 23.5 |
| 18 | \ ((( _<( | \ ((( _<( | Yes | 14.19 |
| 19 | </(  (\_\ | </(  (\_\ | Yes | 32.11 |
| 20 | <((__))(< | <((__))(< | Yes | 13.41 |
