# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-27 10:12:19

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
| sudoku_game | 5156 | 27419 | 32575 | 12 | 8 | 25.15 | 502.94 |
| add_numbers | 2900 | 838 | 3738 | 20 | 0 | 3.63 | 72.58 |
| counting_zeros | 4300 | 17923 | 22223 | 19 | 1 | 13.42 | 268.36 |
| task_decoding | 4240 | 2834 | 7074 | 20 | 0 | 5.08 | 101.53 |
| task_summation | 4580 | 5357 | 9937 | 20 | 0 | 6.67 | 133.53 |
| task_transcription | 3037 | 1378 | 4415 | 20 | 0 | 4.01 | 80.2 |
| task_sequences | 2900 | 3521 | 6421 | 19 | 1 | 6.98 | 139.53 |
| string_entry | 3356 | 22985 | 26341 | 8 | 12 | 24.58 | 491.6 |
| **TOTAL** | **30469** | **82255** | **112724** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 5 1 2 3 6 3 1 2 5 5 3 5 1 | 3 5 1 2 3 6 3 1 2 5 5 3 5 1 | Yes | 12.54 |
| 2 | 4 5 1 6 5 5 4 6 5 6 1 4 6 5 |  | No | 56.33 |
| 3 | 4 5 6 3 5 4 6 4 5 5 3 1 3 6 | 4 5 6 3 5 4 6 4 5 5 3 1 3 6 | Yes | 13.4 |
| 4 | 6 6 1 3 3 5 6 5 6 2 3 5 1 5 | 6 6 1 3 3 5 6 5 6 2 3 5 1 5 | Yes | 15.59 |
| 5 | 2 1 3 5 2 4 1 2 1 3 2 4 2 6 | 2 1 3 5 2 4 1 2 1 3 2 4 2 6 | Yes | 15.75 |
| 6 | 4 1 1 6 3 6 2 6 1 6 6 3 4 2 |  | No | 37.0 |
| 7 | 4 2 3 2 4 2 1 5 5 6 3 6 4 2 | 4 2 3 2 4 2 1 5 5 6 3 6 4 2 | Yes | 12.75 |
| 8 | 5 3 6 1 5 4 6 2 2 6 5 4 1 6 | 5 3 6 1 5 4 6 2 2 6 5 4 1 6 | Yes | 11.32 |
| 9 | 6 1 6 3 6 4 1 6 1 5 4 5 1 6 | 6 1 6 3 6 4 1 6 1 5 4 5 1 6 | Yes | 12.2 |
| 10 | 4 6 2 4 1 3 2 5 1 5 2 2 6 4 |  | No | 40.73 |
| 11 | 2 4 1 5 6 1 5 6 5 2 5 3 4 1 | 2 4 1 5 6 1 5 6 5 2 5 3 4 1 | Yes | 12.43 |
| 12 | 1 5 6 3 5 3 6 4 2 1 4 5 3 1 |  | No | 39.9 |
| 13 | 4 6 4 6 2 2 5 2 6 4 1 3 2 4 | 4 6 4 6 2 2 5 2 6 4 1 3 2 4 | Yes | 12.09 |
| 14 | 3 6 1 2 5 4 2 4 2 1 4 5 5 4 | 3 6 1 2 5 4 2 4 2 1 4 5 5 4 | Yes | 15.71 |
| 15 | 5 2 1 3 5 1 3 6 5 1 5 6 6 3 |  | No | 53.23 |
| 16 | 3 4 2 5 6 3 2 5 3 6 3 4 5 4 |  | No | 44.43 |
| 17 | 1 3 4 5 4 6 5 6 4 5 5 2 5 4 | 1 3 4 5 4 6 5 6 4 5 5 2 5 4 | Yes | 28.52 |
| 18 | 3 3 5 6 4 6 1 2 5 3 3 5 2 5 |  | No | 27.47 |
| 19 | 1 2 4 2 1 5 1 3 6 2 1 2 5 4 | 1 2 4 2 1 5 1 3 6 2 1 2 5 4 | Yes | 11.24 |
| 20 | 4 2 5 6 4 1 3 1 4 5 1 4 5 1 |  | No | 30.28 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1856 | 1856 | Yes | 3.32 |
| 2 | 1494 | 1494 | Yes | 3.47 |
| 3 | 1576 | 1576 | Yes | 6.77 |
| 4 | 2085 | 2085 | Yes | 4.4 |
| 5 | 2088 | 2088 | Yes | 3.45 |
| 6 | 1612 | 1612 | Yes | 3.01 |
| 7 | 2027 | 2027 | Yes | 5.48 |
| 8 | 1549 | 1549 | Yes | 3.72 |
| 9 | 1394 | 1394 | Yes | 3.37 |
| 10 | 1551 | 1551 | Yes | 3.01 |
| 11 | 1905 | 1905 | Yes | 3.02 |
| 12 | 1993 | 1993 | Yes | 3.04 |
| 13 | 2325 | 2325 | Yes | 3.14 |
| 14 | 1571 | 1571 | Yes | 2.92 |
| 15 | 873 | 873 | Yes | 3.28 |
| 16 | 2343 | 2343 | Yes | 3.28 |
| 17 | 1219 | 1219 | Yes | 3.4 |
| 18 | 1470 | 1470 | Yes | 3.29 |
| 19 | 975 | 975 | Yes | 3.88 |
| 20 | 1885 | 1885 | Yes | 3.32 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53 | 52 | No | 10.15 |
| 2 | 49 | 49 | Yes | 9.39 |
| 3 | 53 | 53 | Yes | 21.71 |
| 4 | 63 | 63 | Yes | 14.23 |
| 5 | 60 | 60 | Yes | 11.16 |
| 6 | 63 | 63 | Yes | 10.35 |
| 7 | 69 | 69 | Yes | 11.5 |
| 8 | 52 | 52 | Yes | 13.2 |
| 9 | 39 | 39 | Yes | 12.22 |
| 10 | 37 | 37 | Yes | 12.87 |
| 11 | 36 | 36 | Yes | 10.17 |
| 12 | 65 | 65 | Yes | 17.59 |
| 13 | 44 | 44 | Yes | 18.27 |
| 14 | 65 | 65 | Yes | 13.19 |
| 15 | 58 | 58 | Yes | 13.23 |
| 16 | 56 | 56 | Yes | 12.11 |
| 17 | 45 | 45 | Yes | 11.84 |
| 18 | 63 | 63 | Yes | 16.9 |
| 19 | 69 | 69 | Yes | 12.86 |
| 20 | 61 | 61 | Yes | 15.39 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QRFCELY | QRFCELY | Yes | 6.76 |
| 2 | ZLHNFQI | ZLHNFQI | Yes | 4.37 |
| 3 | SPQAKCZ | SPQAKCZ | Yes | 3.96 |
| 4 | OGQYXJW | OGQYXJW | Yes | 4.35 |
| 5 | BCYTUGH | BCYTUGH | Yes | 5.43 |
| 6 | PZVXOTJ | PZVXOTJ | Yes | 5.11 |
| 7 | LYGZOTE | LYGZOTE | Yes | 5.06 |
| 8 | SCHWAVR | SCHWAVR | Yes | 5.78 |
| 9 | MAGIRQK | MAGIRQK | Yes | 4.84 |
| 10 | XKROSHY | XKROSHY | Yes | 7.4 |
| 11 | BEFMXAH | BEFMXAH | Yes | 5.55 |
| 12 | XZELCGF | XZELCGF | Yes | 4.8 |
| 13 | VQCMPYW | VQCMPYW | Yes | 5.02 |
| 14 | ZYHUSNT | ZYHUSNT | Yes | 4.96 |
| 15 | ASFILMJ | ASFILMJ | Yes | 5.13 |
| 16 | DLEQZYB | DLEQZYB | Yes | 4.78 |
| 17 | RVEAOPN | RVEAOPN | Yes | 4.24 |
| 18 | SFOUJBW | SFOUJBW | Yes | 6.29 |
| 19 | KNUQLSW | KNUQLSW | Yes | 3.28 |
| 20 | BNKUESL | BNKUESL | Yes | 4.41 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.0, 7.0] | 7.0 3.0 | Yes | 7.76 |
| 2 | [0.7, 9.3] | 0.7 9.3 | Yes | 5.54 |
| 3 | [0.9, 9.1] | 0.9 9.1 | Yes | 6.81 |
| 4 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.61 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 8.28 |
| 6 | [3.6, 6.4] | 6.4 3.6 | Yes | 6.56 |
| 7 | [4.6, 5.4] | 5.4 4.6 | Yes | 5.8 |
| 8 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.41 |
| 9 | [4.9, 5.1] | 5.1 4.9 | Yes | 7.07 |
| 10 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.7 |
| 11 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.14 |
| 12 | [2.9, 7.1] | 7.1 2.9 | Yes | 7.02 |
| 13 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.04 |
| 14 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.74 |
| 15 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.38 |
| 16 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.01 |
| 17 | [1.5, 8.5] | 8.5 1.5 | Yes | 4.31 |
| 18 | [1.5, 8.5] | 8.5 1.5 | Yes | 8.13 |
| 19 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.75 |
| 20 | [4.4, 5.6] | 4.4 5.6 | Yes | 8.44 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 825G5XMRM933 | 825G5XMRM933 | Yes | 3.21 |
| 2 | OA3ZHOPML9ZY | OA3ZHOPML9ZY | Yes | 6.34 |
| 3 | PIRDNSLMITRY | PIRDNSLMITRY | Yes | 5.28 |
| 4 | UCZVUDRJULY9 | UCZVUDRJULY9 | Yes | 4.46 |
| 5 | EL4IYNVMUHUK | EL4IYNVMUHUK | Yes | 5.55 |
| 6 | M6RRX5UXCP0U | M6RRX5UXCP0U | Yes | 5.24 |
| 7 | 5MECWVTJFXG9 | 5MECWVTJFXG9 | Yes | 1.89 |
| 8 | 7BLAGS3G9AE3 | 7BLAGS3G9AE3 | Yes | 3.88 |
| 9 | ES19RUHD5OZ4 | ES19RUHD5OZ4 | Yes | 6.64 |
| 10 | IZAG45JSZLID | IZAG45JSZLID | Yes | 1.47 |
| 11 | G1M9EV3E7575 | G1M9EV3E7575 | Yes | 3.82 |
| 12 | 3QQXA1BMDARL | 3QQXA1BMDARL | Yes | 2.47 |
| 13 | BJEJOQT66ILT | BJEJOQT66ILT | Yes | 5.09 |
| 14 | F483O3SK4A28 | F483O3SK4A28 | Yes | 3.61 |
| 15 | 28EQIS8AM30H | 28EQIS8AM30H | Yes | 4.31 |
| 16 | MSGTWF1EEZHA | MSGTWF1EEZHA | Yes | 1.58 |
| 17 | SEVB5FGL8VJ5 | SEVB5FGL8VJ5 | Yes | 4.54 |
| 18 | 5RYM8AQZ6E8A | 5RYM8AQZ6E8A | Yes | 1.83 |
| 19 | KK1NU05PLQHT | KK1NU05PLQHT | Yes | 4.37 |
| 20 | D23U5K1M0KPV | D23U5K1M0KPV | Yes | 4.61 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 |  | No | 50.64 |
| 2 | 65 | 65 | Yes | 4.24 |
| 3 | 5 | 5 | Yes | 4.32 |
| 4 | 16 | 16 | Yes | 4.78 |
| 5 | 39 | 39 | Yes | 5.98 |
| 6 | 7 | 7 | Yes | 4.39 |
| 7 | 1440 | 1440 | Yes | 3.76 |
| 8 | 67 | 67 | Yes | 2.93 |
| 9 | 198 | 198 | Yes | 4.48 |
| 10 | 36 | 36 | Yes | 3.75 |
| 11 | 48 | 48 | Yes | 3.61 |
| 12 | 1 | 1 | Yes | 7.81 |
| 13 | 9 | 9 | Yes | 4.28 |
| 14 | 9 | 9 | Yes | 2.7 |
| 15 | 3 | 3 | Yes | 8.65 |
| 16 | 793 | 793 | Yes | 3.67 |
| 17 | 60 | 60 | Yes | 4.03 |
| 18 | 31 | 31 | Yes | 4.91 |
| 19 | 44 | 44 | Yes | 4.49 |
| 20 | 10 | 10 | Yes | 6.09 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |    <)/ /  | <)/ / | No | 10.3 |
| 2 | _(<)/)\<  | _(<)/)\< | No | 10.44 |
| 3 | _ /)\)/__ | _ /)\)/__ | Yes | 10.31 |
| 4 | <((__<\// | <((__<\// | Yes | 14.82 |
| 5 | \ (/)  (\ |  | No | 45.99 |
| 6 | _\//_<<   | _\//_<< | No | 31.25 |
| 7 | /((/  //( | /((/  //( | Yes | 7.12 |
| 8 | <\_(/)/)) | <\_(/)/)) | Yes | 10.16 |
| 9 |  _<) \ (  | _<) \ ( | No | 25.02 |
| 10 | < /_()_\\ | < /_()_\\ | Yes | 15.5 |
| 11 | \\ )(/\_/ |  | No | 50.38 |
| 12 | )(<\\))\\ |  | No | 42.87 |
| 13 | )\)) / )) | )\)) / )) | Yes | 11.52 |
| 14 | </\<(( () |  | No | 38.31 |
| 15 | <)</_()_( | <)</_()_( | Yes | 24.07 |
| 16 | _    < (  | _    < ( | No | 11.59 |
| 17 | _//<))_(_ |  | No | 42.24 |
| 18 | _\\((\\(< |  | No | 40.02 |
| 19 | /\\( )__< | /\\( )__< | Yes | 7.35 |
| 20 | <\/_\_)<< |  | No | 42.33 |
