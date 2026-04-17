# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-27 10:48:19

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
| sudoku_game | 5491 | 40960 | 46451 | 0 | 20 | 57.59 | 1151.82 |
| add_numbers | 3240 | 4618 | 7858 | 20 | 0 | 6.51 | 130.19 |
| counting_zeros | 4640 | 40894 | 45534 | 1 | 19 | 56.43 | 1128.64 |
| task_decoding | 4580 | 7264 | 11844 | 20 | 0 | 9.35 | 187.09 |
| task_summation | 4674 | 13781 | 18455 | 19 | 1 | 17.97 | 359.37 |
| task_transcription | 3370 | 3704 | 7074 | 20 | 0 | 4.38 | 87.71 |
| task_sequences | 3079 | 9998 | 13077 | 18 | 2 | 17.20 | 344.02 |
| string_entry | 3680 | 27930 | 31610 | 14 | 6 | 26.68 | 533.6 |
| **TOTAL** | **32754** | **149149** | **181903** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 4 1 5 4 5 6 3 4 6 4 4 4 |  | No | 59.9 |
| 2 | 1 2 3 2 1 5 5 3 3 2 3 2 4 5 |  | No | 60.13 |
| 3 | 5 6 2 5 3 1 1 3 5 6 4 6 2 1 |  | No | 66.3 |
| 4 | 1 2 5 6 4 3 2 4 3 5 5 4 3 2 |  | No | 61.03 |
| 5 | 2 5 3 2 6 1 2 1 3 1 4 5 6 2 |  | No | 51.76 |
| 6 | 3 5 2 4 3 6 4 6 4 1 2 5 6 4 |  | No | 45.0 |
| 7 | 1 5 3 3 5 2 4 1 5 6 5 2 6 6 |  | No | 49.25 |
| 8 | 4 3 2 5 3 6 1 5 3 6 4 5 1 6 |  | No | 48.56 |
| 9 | 4 5 4 5 1 5 6 4 6 2 2 1 4 5 |  | No | 48.11 |
| 10 | 5 4 1 6 6 3 4 2 5 4 2 6 5 1 |  | No | 65.61 |
| 11 | 2 1 5 3 5 6 4 6 2 5 3 1 4 1 |  | No | 58.44 |
| 12 | 2 4 3 6 3 5 5 6 6 4 1 2 1 5 |  | No | 55.71 |
| 13 | 4 1 2 2 6 6 5 6 3 5 4 5 6 2 |  | No | 51.4 |
| 14 | 6 5 2 3 2 4 2 5 3 5 6 2 1 3 |  | No | 55.53 |
| 15 | 5 2 5 2 3 2 6 4 3 1 2 6 4 5 |  | No | 64.16 |
| 16 | 5 3 6 4 1 2 5 3 4 5 6 2 1 1 |  | No | 57.79 |
| 17 | 1 4 3 5 1 6 2 6 1 3 6 3 2 5 |  | No | 60.37 |
| 18 | 5 6 2 3 5 6 4 2 3 3 6 4 3 4 |  | No | 48.96 |
| 19 | 3 4 6 2 4 2 5 1 6 5 6 1 6 4 |  | No | 66.73 |
| 20 | 1 4 4 3 1 5 4 1 3 1 5 1 2 4 |  | No | 77.04 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1866 | 1866 | Yes | 10.4 |
| 2 | 1649 | 1649 | Yes | 5.95 |
| 3 | 1800 | 1800 | Yes | 9.74 |
| 4 | 1885 | 1885 | Yes | 4.78 |
| 5 | 2168 | 2168 | Yes | 5.5 |
| 6 | 2540 | 2540 | Yes | 9.39 |
| 7 | 1753 | 1753 | Yes | 5.77 |
| 8 | 1242 | 1242 | Yes | 2.69 |
| 9 | 1920 | 1920 | Yes | 6.09 |
| 10 | 1946 | 1946 | Yes | 7.71 |
| 11 | 919 | 919 | Yes | 4.13 |
| 12 | 2390 | 2390 | Yes | 7.55 |
| 13 | 1725 | 1725 | Yes | 8.58 |
| 14 | 2688 | 2688 | Yes | 7.9 |
| 15 | 1296 | 1296 | Yes | 5.34 |
| 16 | 1738 | 1738 | Yes | 6.76 |
| 17 | 1173 | 1173 | Yes | 6.14 |
| 18 | 1531 | 1531 | Yes | 4.03 |
| 19 | 1661 | 1661 | Yes | 8.75 |
| 20 | 799 | 799 | Yes | 2.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 |  | No | 62.46 |
| 2 | 51 |  | No | 67.07 |
| 3 | 62 |  | No | 68.51 |
| 4 | 72 |  | No | 49.06 |
| 5 | 72 |  | No | 62.53 |
| 6 | 59 |  | No | 49.71 |
| 7 | 38 |  | No | 63.51 |
| 8 | 49 |  | No | 46.76 |
| 9 | 69 | 69 | Yes | 23.73 |
| 10 | 72 |  | No | 40.16 |
| 11 | 36 |  | No | 57.43 |
| 12 | 53 |  | No | 51.44 |
| 13 | 74 |  | No | 73.59 |
| 14 | 59 |  | No | 52.03 |
| 15 | 46 |  | No | 60.33 |
| 16 | 47 |  | No | 82.43 |
| 17 | 74 |  | No | 53.24 |
| 18 | 66 |  | No | 37.38 |
| 19 | 64 |  | No | 72.54 |
| 20 | 35 |  | No | 54.73 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DZRIFAU | DZRIFAU | Yes | 10.11 |
| 2 | JPATHEQ | JPATHEQ | Yes | 10.58 |
| 3 | FYNPORJ | FYNPORJ | Yes | 10.32 |
| 4 | NUEPXHZ | NUEPXHZ | Yes | 15.92 |
| 5 | BNHLYPS | BNHLYPS | Yes | 7.86 |
| 6 | KUCMDAJ | KUCMDAJ | Yes | 13.43 |
| 7 | KBYXNVT | KBYXNVT | Yes | 12.36 |
| 8 | IVNQZKG | IVNQZKG | Yes | 4.72 |
| 9 | TQACDMN | TQACDMN | Yes | 5.68 |
| 10 | BYFGENJ | BYFGENJ | Yes | 7.18 |
| 11 | PRLKIMJ | PRLKIMJ | Yes | 10.66 |
| 12 | SZHNGTL | SZHNGTL | Yes | 7.21 |
| 13 | DFCKQJH | DFCKQJH | Yes | 7.83 |
| 14 | TUHQPNW | TUHQPNW | Yes | 9.05 |
| 15 | WDBYMEO | WDBYMEO | Yes | 10.94 |
| 16 | OWLHRPC | OWLHRPC | Yes | 10.32 |
| 17 | NUYJGKL | NUYJGKL | Yes | 10.98 |
| 18 | AQMKUYT | AQMKUYT | Yes | 9.35 |
| 19 | MUNQGZS | MUNQGZS | Yes | 6.38 |
| 20 | JSNGVBH | JSNGVBH | Yes | 6.21 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.4, 6.6] | 3.4 6.6 | Yes | 14.58 |
| 2 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.82 |
| 3 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.12 |
| 4 | [0.9, 9.1] | 9.1 0.9 | Yes | 9.12 |
| 5 | [3.4, 6.6] | 3.4 6.6 | Yes | 12.67 |
| 6 | [2.3, 7.7] | 2.3 7.7 | Yes | 9.59 |
| 7 | [1.9, 8.1] | 1.9 8.1 | Yes | 12.43 |
| 8 | [1.7, 8.3] | 1.7 8.3 | Yes | 18.91 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 13.72 |
| 10 | [3.5, 6.5] | 3.5 6.5 | Yes | 13.14 |
| 11 | [2.8, 7.2] | 2.8 7.2 | Yes | 13.52 |
| 12 | [3.1, 6.9] | 3.1 6.9 | Yes | 15.95 |
| 13 | [2.6, 7.4] | 2.6 7.4 | Yes | 12.61 |
| 14 | [0.1, 9.9] | 0.1 9.9 | Yes | 9.46 |
| 15 | [2.0, 8.0] | 2.0 8.0 | Yes | 13.03 |
| 16 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.4 |
| 17 | [4.0, 6.0] | 6.0 4.0 | Yes | 13.8 |
| 18 | [4.7, 5.3] | 5.3 4.7 | Yes | 13.36 |
| 19 | [3.8, 6.2] | 6.2 3.8 | Yes | 10.12 |
| 20 | [4.8, 5.2] | TIMEOUT | No | 120.02 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9DBPPXSKT025 | 9DBPPXSKT025 | Yes | 5.16 |
| 2 | N5MR6T4IX8DS | N5MR6T4IX8DS | Yes | 2.91 |
| 3 | VXDXABPPIN42 | VXDXABPPIN42 | Yes | 2.54 |
| 4 | 5C1749XLGTUI | 5C1749XLGTUI | Yes | 6.39 |
| 5 | JRSSOJ1SI1GY | JRSSOJ1SI1GY | Yes | 6.22 |
| 6 | BK411KHWXPOP | BK411KHWXPOP | Yes | 4.07 |
| 7 | DW9PKF16O585 | DW9PKF16O585 | Yes | 6.55 |
| 8 | C168RH64YRKJ | C168RH64YRKJ | Yes | 3.26 |
| 9 | EF16APEJNIVO | EF16APEJNIVO | Yes | 4.66 |
| 10 | JSOGZCLIZFEV | JSOGZCLIZFEV | Yes | 5.09 |
| 11 | T7SNCWAPOKKY | T7SNCWAPOKKY | Yes | 2.04 |
| 12 | Q6MF3I72HY2B | Q6MF3I72HY2B | Yes | 4.0 |
| 13 | JKS3EEFC4PHA | JKS3EEFC4PHA | Yes | 2.72 |
| 14 | J12BKIM8WMLJ | J12BKIM8WMLJ | Yes | 2.11 |
| 15 | 4WDV4J3EAIJ6 | 4WDV4J3EAIJ6 | Yes | 5.19 |
| 16 | G9F5XFU5FY26 | G9F5XFU5FY26 | Yes | 3.58 |
| 17 | 3DT9828WD4AJ | 3DT9828WD4AJ | Yes | 6.41 |
| 18 | 0TRSXZJLAJ0F | 0TRSXZJLAJ0F | Yes | 5.77 |
| 19 | VAM9ELFSF5II | VAM9ELFSF5II | Yes | 2.86 |
| 20 | VABHZ77KDIOH | VABHZ77KDIOH | Yes | 6.16 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 12.2 |
| 2 | 9 | 9 | Yes | 8.35 |
| 3 | 19 | 19 | Yes | 12.59 |
| 4 | 31 | 31 | Yes | 4.18 |
| 5 | 64 | 64 | Yes | 12.38 |
| 6 | 6 | 6 | Yes | 5.98 |
| 7 | 4096 |  | No | 56.5 |
| 8 | 36 | 36 | Yes | 5.37 |
| 9 | 9 | 9 | Yes | 5.2 |
| 10 | 16 | 16 | Yes | 9.08 |
| 11 | 4 | 4 | Yes | 5.58 |
| 12 | 3 | 3 | Yes | 21.82 |
| 13 | 10 | 10 | Yes | 5.73 |
| 14 | 44 | 44 | Yes | 5.46 |
| 15 | 5 | 5 | Yes | 4.66 |
| 16 | 60 | 60 | Yes | 4.91 |
| 17 | 73 | 73 | Yes | 8.76 |
| 18 | 198 | TIMEOUT | No | 120.03 |
| 19 | 20 | 20 | Yes | 26.46 |
| 20 | 23 | 23 | Yes | 8.75 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  /(<_<    |  | No | 66.4 |
| 2 | <_(<  )/_ | <_(<  )/_ | Yes | 18.74 |
| 3 | < _< ()(/ | < _< ()(/ | Yes | 17.25 |
| 4 | </<<(_/() | </<<(_/() | Yes | 18.84 |
| 5 |  /)(\/__( | /)(\/__( | No | 27.02 |
| 6 | _\<( </<\ | _\<( </<\ | Yes | 22.4 |
| 7 | __/_/)\ _ | __/_/)\ _ | Yes | 19.69 |
| 8 | _\<</((\) | _\<</((\) | Yes | 21.41 |
| 9 | _/)_\(_// | _/)_\(_// | Yes | 18.62 |
| 10 |  </</\_\\ |  | No | 57.5 |
| 11 | <<))\)\/) | <<))\)\/) | Yes | 18.09 |
| 12 | _   )(__/ | _   )(__/ | Yes | 12.22 |
| 13 | \)\)_)/<\ | \)\)_)/<\ | Yes | 20.03 |
| 14 | )/) _)(_) | )/) _)(_) | Yes | 13.9 |
| 15 | _)<</))<( | _)<</))<( | Yes | 14.96 |
| 16 | (/\\<_)(/ | (/\\<_)(/ | Yes | 22.18 |
| 17 | (/_//(< ) | (/_//(< ) | Yes | 14.71 |
| 18 |  )/_<(\/  | )/_<(\/ | No | 29.59 |
| 19 |   )(<(_\  |  | No | 50.58 |
| 20 | \\_))/(<  |  | No | 49.42 |
