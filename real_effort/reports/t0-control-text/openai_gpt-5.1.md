# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-26 16:03:40

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
| sudoku_game | 4670 | 40960 | 45630 | 0 | 20 | 51.39 | 1027.85 |
| add_numbers | 2420 | 963 | 3383 | 20 | 0 | 3.76 | 75.19 |
| counting_zeros | 3820 | 32396 | 36216 | 17 | 3 | 31.19 | 623.73 |
| task_decoding | 3760 | 3739 | 7499 | 20 | 0 | 5.53 | 110.64 |
| task_summation | 4100 | 8350 | 12450 | 20 | 0 | 8.82 | 176.35 |
| task_transcription | 2562 | 954 | 3516 | 20 | 0 | 2.67 | 53.41 |
| task_sequences | 2421 | 8178 | 10599 | 19 | 1 | 10.12 | 202.37 |
| string_entry | 2855 | 16223 | 19078 | 13 | 7 | 18.31 | 366.12 |
| **TOTAL** | **26608** | **111763** | **138371** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 2 4 6 2 6 1 6 2 6 1 3 4 3 |  | No | 30.67 |
| 2 | 3 1 4 5 6 4 3 4 5 3 6 1 3 4 |  | No | 45.87 |
| 3 | 2 4 3 2 4 3 5 3 1 6 1 6 2 6 |  | No | 57.73 |
| 4 | 3 4 5 4 3 6 5 4 6 2 6 5 6 2 |  | No | 57.98 |
| 5 | 2 6 1 5 1 4 6 3 5 3 1 6 1 2 |  | No | 60.51 |
| 6 | 1 2 3 5 2 6 4 6 4 1 4 1 5 3 |  | No | 55.8 |
| 7 | 5 2 6 4 5 6 2 5 6 4 5 1 2 6 |  | No | 59.3 |
| 8 | 6 1 1 3 5 4 6 5 5 1 2 6 6 5 |  | No | 58.6 |
| 9 | 4 2 6 3 2 5 4 2 4 1 1 6 2 3 |  | No | 41.32 |
| 10 | 2 1 5 2 6 2 5 3 6 3 5 2 6 3 |  | No | 50.46 |
| 11 | 5 4 3 2 3 5 2 3 5 1 2 2 4 3 |  | No | 52.73 |
| 12 | 3 5 4 6 1 4 1 6 5 1 6 2 4 4 |  | No | 45.39 |
| 13 | 4 1 6 3 5 3 4 1 3 6 4 5 2 4 |  | No | 50.34 |
| 14 | 2 5 4 5 1 6 2 6 5 5 3 3 1 6 |  | No | 40.42 |
| 15 | 5 6 5 4 6 5 2 6 4 4 1 5 3 6 |  | No | 49.41 |
| 16 | 5 6 6 1 1 6 3 1 6 2 5 2 3 5 |  | No | 57.33 |
| 17 | 2 4 3 4 2 1 3 5 1 2 4 5 6 5 |  | No | 49.65 |
| 18 | 5 3 1 3 6 2 2 1 3 2 1 4 5 3 |  | No | 50.35 |
| 19 | 2 4 6 4 1 6 3 6 5 1 6 6 4 1 |  | No | 55.0 |
| 20 | 1 4 2 1 5 6 6 1 2 3 3 1 6 3 |  | No | 58.92 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1468 | 1468 | Yes | 5.7 |
| 2 | 2743 | 2743 | Yes | 4.23 |
| 3 | 2235 | 2235 | Yes | 4.16 |
| 4 | 1795 | 1795 | Yes | 3.34 |
| 5 | 2411 | 2411 | Yes | 3.84 |
| 6 | 1786 | 1786 | Yes | 3.17 |
| 7 | 1552 | 1552 | Yes | 3.2 |
| 8 | 1332 | 1332 | Yes | 3.35 |
| 9 | 1331 | 1331 | Yes | 3.69 |
| 10 | 1749 | 1749 | Yes | 3.33 |
| 11 | 1962 | 1962 | Yes | 3.25 |
| 12 | 1455 | 1455 | Yes | 4.17 |
| 13 | 1956 | 1956 | Yes | 3.86 |
| 14 | 1448 | 1448 | Yes | 3.49 |
| 15 | 1566 | 1566 | Yes | 3.46 |
| 16 | 1839 | 1839 | Yes | 4.6 |
| 17 | 2296 | 2296 | Yes | 3.34 |
| 18 | 1945 | 1945 | Yes | 3.48 |
| 19 | 2314 | 2314 | Yes | 3.71 |
| 20 | 1411 | 1411 | Yes | 3.82 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 45 | 45 | Yes | 20.75 |
| 2 | 59 | 59 | Yes | 46.86 |
| 3 | 42 | 42 | Yes | 26.97 |
| 4 | 51 |  | No | 52.63 |
| 5 | 47 | 47 | Yes | 17.28 |
| 6 | 43 | 43 | Yes | 14.3 |
| 7 | 60 | 60 | Yes | 25.11 |
| 8 | 40 | 40 | Yes | 20.89 |
| 9 | 62 | 62 | Yes | 43.75 |
| 10 | 48 | 48 | Yes | 22.05 |
| 11 | 65 |  | No | 52.06 |
| 12 | 35 | 35 | Yes | 42.33 |
| 13 | 51 | 51 | Yes | 26.73 |
| 14 | 61 | 61 | Yes | 26.98 |
| 15 | 56 | 56 | Yes | 28.33 |
| 16 | 70 | 70 | Yes | 31.83 |
| 17 | 53 | 53 | Yes | 23.58 |
| 18 | 73 |  | No | 52.12 |
| 19 | 40 | 40 | Yes | 26.44 |
| 20 | 65 | 65 | Yes | 22.73 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VPJUTAO | VPJUTAO | Yes | 3.47 |
| 2 | TXUZFLN | TXUZFLN | Yes | 5.4 |
| 3 | SAPKFNQ | SAPKFNQ | Yes | 5.24 |
| 4 | VQKGIWC | VQKGIWC | Yes | 6.07 |
| 5 | FODJTBG | FODJTBG | Yes | 5.94 |
| 6 | RGNEMHP | RGNEMHP | Yes | 3.48 |
| 7 | OWPBMLN | OWPBMLN | Yes | 4.37 |
| 8 | HNPVKFA | HNPVKFA | Yes | 6.25 |
| 9 | GTPFBSE | GTPFBSE | Yes | 6.36 |
| 10 | WAJBZNC | WAJBZNC | Yes | 4.24 |
| 11 | DIAUGTR | DIAUGTR | Yes | 7.03 |
| 12 | KWRNCBD | KWRNCBD | Yes | 6.28 |
| 13 | RODMHVU | RODMHVU | Yes | 6.85 |
| 14 | BYVWIHK | BYVWIHK | Yes | 4.58 |
| 15 | CPTXAYF | CPTXAYF | Yes | 6.21 |
| 16 | PAYLHFU | PAYLHFU | Yes | 6.48 |
| 17 | JCXFMYB | JCXFMYB | Yes | 4.47 |
| 18 | YZWEGJC | YZWEGJC | Yes | 5.53 |
| 19 | MJYOIAX | MJYOIAX | Yes | 4.48 |
| 20 | SKRWTHL | SKRWTHL | Yes | 7.92 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.1, 9.9] | 9.9 0.1 | Yes | 11.06 |
| 2 | [0.2, 9.8] | 0.2 9.8 | Yes | 7.2 |
| 3 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.06 |
| 4 | [0.9, 9.1] | 9.1 0.9 | Yes | 9.1 |
| 5 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.33 |
| 6 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.57 |
| 7 | [0.9, 9.1] | 9.1 0.9 | Yes | 9.98 |
| 8 | [2.5, 7.5] | 7.5 2.5 | Yes | 7.85 |
| 9 | [1.6, 8.4] | 1.6 8.4 | Yes | 5.03 |
| 10 | [3.8, 6.2] | 6.2 3.8 | Yes | 12.01 |
| 11 | [3.9, 6.1] | 6.1 3.9 | Yes | 9.79 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 9.21 |
| 13 | [3.2, 6.8] | 6.8 3.2 | Yes | 9.06 |
| 14 | [3.1, 6.9] | 3.1 6.9 | Yes | 9.13 |
| 15 | [0.6, 9.4] | 0.6 9.4 | Yes | 6.57 |
| 16 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.78 |
| 17 | [0.3, 9.7] | 0.3 9.7 | Yes | 5.56 |
| 18 | [4.3, 5.7] | 4.3 5.7 | Yes | 9.83 |
| 19 | [3.5, 6.5] | 6.5 3.5 | Yes | 12.97 |
| 20 | [3.9, 6.1] | 3.9 6.1 | Yes | 7.25 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZZQAU983VJ1H | ZZQAU983VJ1H | Yes | 2.71 |
| 2 | A1Y8V0EHZVG7 | A1Y8V0EHZVG7 | Yes | 1.85 |
| 3 | PO7GRE693W4Q | PO7GRE693W4Q | Yes | 1.62 |
| 4 | BOLS7R1C2POR | BOLS7R1C2POR | Yes | 1.96 |
| 5 | VLGJUJ30F47K | VLGJUJ30F47K | Yes | 2.89 |
| 6 | VQM76RV6EI4P | VQM76RV6EI4P | Yes | 3.91 |
| 7 | S62KRICYD0GG | S62KRICYD0GG | Yes | 1.94 |
| 8 | C6COKR78FXEQ | C6COKR78FXEQ | Yes | 1.68 |
| 9 | 4XQBU3DV4ZMF | 4XQBU3DV4ZMF | Yes | 3.98 |
| 10 | YQTBUUE67VCA | YQTBUUE67VCA | Yes | 4.32 |
| 11 | J945X5AZOSEX | J945X5AZOSEX | Yes | 3.76 |
| 12 | 569TBBOYCEWE | 569TBBOYCEWE | Yes | 3.73 |
| 13 | 6RYQU8GHMGM6 | 6RYQU8GHMGM6 | Yes | 1.31 |
| 14 | 5PA3PDP2FRIR | 5PA3PDP2FRIR | Yes | 2.15 |
| 15 | AW6KUBGNSX9J | AW6KUBGNSX9J | Yes | 3.93 |
| 16 | QHD7JKU6AVB3 | QHD7JKU6AVB3 | Yes | 1.72 |
| 17 | 7E6QVZQ50QLF | 7E6QVZQ50QLF | Yes | 2.04 |
| 18 | W8UIDWT6YX5V | W8UIDWT6YX5V | Yes | 1.42 |
| 19 | U604CX9OVLZJ | U604CX9OVLZJ | Yes | 4.15 |
| 20 | N1HX1TQ3FMX5 | N1HX1TQ3FMX5 | Yes | 2.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 5.61 |
| 2 | 63 | 63 | Yes | 4.19 |
| 3 | 4096 |  | No | 50.01 |
| 4 | 6 | 6 | Yes | 8.0 |
| 5 | 73 | 73 | Yes | 6.8 |
| 6 | 31 | 31 | Yes | 6.21 |
| 7 | 9 | 9 | Yes | 4.42 |
| 8 | 44 | 44 | Yes | 12.96 |
| 9 | 4 | 4 | Yes | 4.74 |
| 10 | 60 | 60 | Yes | 3.85 |
| 11 | 7 | 7 | Yes | 3.92 |
| 12 | 64 | 64 | Yes | 14.43 |
| 13 | 20 | 20 | Yes | 11.64 |
| 14 | 4 | 4 | Yes | 5.89 |
| 15 | 3 | 3 | Yes | 7.83 |
| 16 | 7680 | 7680 | Yes | 3.94 |
| 17 | 10 | 10 | Yes | 22.79 |
| 18 | 39 | 39 | Yes | 10.28 |
| 19 | 793 | 793 | Yes | 5.18 |
| 20 | 28 | 28 | Yes | 9.66 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  (_ /_(<< |  | No | 51.55 |
| 2 | (<\(/__<< | (<\(/__<< | Yes | 11.4 |
| 3 | (\\__/(_) |  | No | 47.56 |
| 4 | <)/)/_(\  | <)/)/_(\ | No | 16.56 |
| 5 | )/)<_<\<( | )/)<_<\<( | Yes | 5.35 |
| 6 | < ((((<)/ | < ((((<)/ | Yes | 4.62 |
| 7 |    <)_/ _ | <)_/ _ | No | 7.94 |
| 8 | //) )_< < | //) )_< < | Yes | 3.44 |
| 9 | ///_\)(<_ | ///_\)(<_ | Yes | 16.49 |
| 10 | <\ <)<(/\ | < <)<(/\ | No | 11.03 |
| 11 | /) / //)\ | /) / //)\ | Yes | 8.9 |
| 12 | (/(/\ /(_ | (/(/\ /(_ | Yes | 14.73 |
| 13 | ( <(/_ (/ | ( <(/_ (/ | Yes | 8.74 |
| 14 | <(\)\ <)) | <(\)\ <)) | Yes | 7.25 |
| 15 | //(_ \ <\ | //(_ \ <\ | Yes | 8.88 |
| 16 | )/_(<___\ |  | No | 70.41 |
| 17 | /(/<)(\<< | /(/<)(\<< | Yes | 27.01 |
| 18 | /\_ /<\\\ | /\_ /<\\\ | Yes | 13.17 |
| 19 |  )  )<()/ | )  )<()/ | No | 19.0 |
| 20 | ( (_)/ </ | ( (_)/ </ | Yes | 12.09 |
