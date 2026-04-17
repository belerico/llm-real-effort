# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 11:03:30

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
| sudoku_game | 7360 | 39434 | 46794 | 5 | 15 | 41.25 | 825.17 |
| add_numbers | 3940 | 1538 | 5478 | 20 | 0 | 3.96 | 79.31 |
| counting_zeros | 6360 | 32372 | 38732 | 0 | 20 | 33.15 | 663.41 |
| task_decoding | 12100 | 4515 | 16615 | 20 | 0 | 6.27 | 125.54 |
| task_summation | 7300 | 6406 | 13706 | 20 | 0 | 5.88 | 117.9 |
| task_transcription | 3780 | 10352 | 14132 | 3 | 17 | 8.00 | 160.19 |
| task_sequences | 3061 | 14889 | 17950 | 17 | 3 | 13.17 | 263.51 |
| string_entry | 5794 | 28245 | 34039 | 12 | 8 | 27.36 | 547.24 |
| **TOTAL** | **49695** | **137751** | **187446** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 2 1 1 6 3 4 6 1 1 5 6 4 |  | No | 43.69 |
| 2 | 1 6 2 3 3 2 4 2 1 6 2 4 1 2 | 1 6 2 3 3 2 4 2 1 6 2 4 1 2 | Yes | 30.76 |
| 3 | 1 5 5 2 6 3 6 6 3 5 2 3 1 3 |  | No | 44.34 |
| 4 | 2 3 1 1 6 2 4 3 3 5 4 6 2 4 |  | No | 43.34 |
| 5 | 1 2 2 3 1 6 5 1 3 2 3 4 6 2 |  | No | 54.07 |
| 6 | 2 5 3 6 6 4 4 5 6 6 5 2 2 3 |  | No | 31.66 |
| 7 | 2 3 1 3 4 4 1 5 5 4 3 3 2 3 |  | No | 48.72 |
| 8 | 5 2 1 3 2 5 1 4 5 2 6 3 5 4 |  | No | 43.09 |
| 9 | 3 2 2 4 5 2 6 3 1 3 6 3 1 5 |  | No | 44.1 |
| 10 | 6 2 1 3 1 2 3 1 6 4 3 6 6 3 | 6 2 1 3 1 2 3 1 6 4 3 6 6 3 | Yes | 25.14 |
| 11 | 4 2 6 3 5 3 1 4 3 6 1 5 1 4 | 4 2 6 3 5 3 1 4 3 6 1 5 1 4 | Yes | 19.53 |
| 12 | 1 4 3 4 1 4 3 4 2 4 1 4 5 3 |  | No | 48.47 |
| 13 | 6 2 3 6 4 2 6 1 3 6 4 4 1 3 |  | No | 49.06 |
| 14 | 6 2 4 1 2 4 2 1 2 4 3 3 5 1 |  | No | 44.91 |
| 15 | 5 3 1 6 3 1 4 1 6 2 4 2 6 3 |  | No | 49.54 |
| 16 | 2 3 1 5 2 4 1 6 3 5 2 6 4 1 |  | No | 52.21 |
| 17 | 3 6 1 3 4 5 1 5 3 4 6 3 3 6 |  | No | 53.26 |
| 18 | 4 5 1 4 6 3 4 6 5 3 2 6 3 2 | 4 5 1 4 6 3 4 6 5 3 2 6 3 2 | Yes | 27.94 |
| 19 | 2 1 5 3 1 3 6 5 4 5 1 5 2 1 |  | No | 47.04 |
| 20 | 6 5 3 2 1 5 6 6 2 2 1 5 6 3 | 6 5 3 2 1 5 6 6 2 2 1 5 6 3 | Yes | 24.11 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1100 | 1100 | Yes | 4.42 |
| 2 | 1405 | 1405 | Yes | 3.73 |
| 3 | 1683 | 1683 | Yes | 5.14 |
| 4 | 2046 | 2046 | Yes | 4.34 |
| 5 | 1581 | 1581 | Yes | 1.88 |
| 6 | 1729 | 1729 | Yes | 4.88 |
| 7 | 1474 | 1474 | Yes | 3.26 |
| 8 | 1501 | 1501 | Yes | 4.8 |
| 9 | 1342 | 1342 | Yes | 4.48 |
| 10 | 2322 | 2322 | Yes | 4.61 |
| 11 | 1957 | 1957 | Yes | 5.02 |
| 12 | 1544 | 1544 | Yes | 3.06 |
| 13 | 1667 | 1667 | Yes | 4.25 |
| 14 | 1603 | 1603 | Yes | 4.01 |
| 15 | 1950 | 1950 | Yes | 3.13 |
| 16 | 2163 | 2163 | Yes | 2.48 |
| 17 | 1861 | 1861 | Yes | 4.71 |
| 18 | 1580 | 1580 | Yes | 4.44 |
| 19 | 1864 | 1864 | Yes | 3.45 |
| 20 | 655 | 655 | Yes | 3.12 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 | 67 | No | 22.9 |
| 2 | 70 | 67 | No | 20.25 |
| 3 | 71 |  | No | 43.68 |
| 4 | 61 | 67 | No | 19.21 |
| 5 | 44 | 67 | No | 16.39 |
| 6 | 37 | 67 | No | 23.16 |
| 7 | 70 | 67 | No | 16.85 |
| 8 | 43 | 67 | No | 21.81 |
| 9 | 56 |  | No | 51.88 |
| 10 | 71 |  | No | 45.78 |
| 11 | 48 |  | No | 53.82 |
| 12 | 64 | 67 | No | 13.64 |
| 13 | 51 |  | No | 42.72 |
| 14 | 42 |  | No | 53.06 |
| 15 | 60 |  | No | 42.13 |
| 16 | 56 |  | No | 45.32 |
| 17 | 71 | 67 | No | 17.46 |
| 18 | 37 |  | No | 52.45 |
| 19 | 48 |  | No | 56.93 |
| 20 | 53 | 67 | No | 3.62 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CVAEBTL | CVAEBTL | Yes | 5.85 |
| 2 | OQGFHNL | OQGFHNL | Yes | 7.45 |
| 3 | VTICEKD | VTICEKD | Yes | 6.21 |
| 4 | HYMLRTU | HYMLRTU | Yes | 5.96 |
| 5 | PLUGSQT | PLUGSQT | Yes | 5.46 |
| 6 | DBTKCRN | DBTKCRN | Yes | 5.4 |
| 7 | MAREUVW | MAREUVW | Yes | 6.21 |
| 8 | OBIVEKD | OBIVEKD | Yes | 5.34 |
| 9 | ZSDFURB | ZSDFURB | Yes | 5.57 |
| 10 | KPJDSUW | KPJDSUW | Yes | 4.71 |
| 11 | SGAQNFX | SGAQNFX | Yes | 6.98 |
| 12 | YEOBHAQ | YEOBHAQ | Yes | 5.32 |
| 13 | ZKHDEIP | ZKHDEIP | Yes | 6.76 |
| 14 | WHBZRXI | WHBZRXI | Yes | 10.83 |
| 15 | WQTCIBD | WQTCIBD | Yes | 5.58 |
| 16 | CIVJKRX | CIVJKRX | Yes | 5.47 |
| 17 | LMABXDE | LMABXDE | Yes | 5.8 |
| 18 | BVHPJWI | BVHPJWI | Yes | 7.01 |
| 19 | SCGBMXJ | SCGBMXJ | Yes | 5.85 |
| 20 | KDWORSA | KDWORSA | Yes | 7.57 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.2, 7.8] | 2.2 7.8 | Yes | 7.0 |
| 2 | [0.2, 9.8] | 9.8 0.2 | Yes | 6.31 |
| 3 | [4.3, 5.7] | 4.3 5.7 | Yes | 7.12 |
| 4 | [0.7, 9.3] | 0.7 9.3 | Yes | 6.52 |
| 5 | [2.0, 8.0] | 8.0 2.0 | Yes | 5.39 |
| 6 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.7 |
| 7 | [1.8, 8.2] | 1.8 8.2 | Yes | 5.53 |
| 8 | [1.4, 8.6] | 8.6 1.4 | Yes | 5.24 |
| 9 | [0.6, 9.4] | 9.4 0.6 | Yes | 8.66 |
| 10 | [4.5, 5.5] | 5.5 4.5 | Yes | 4.55 |
| 11 | [4.6, 5.4] | 5.4 4.6 | Yes | 6.94 |
| 12 | [2.1, 7.9] | 2.1 7.9 | Yes | 5.57 |
| 13 | [2.7, 7.3] | 2.7 7.3 | Yes | 2.65 |
| 14 | [4.3, 5.7] | 5.7 4.3 | Yes | 4.1 |
| 15 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.32 |
| 16 | [4.9, 5.1] | 5.1 4.9 | Yes | 5.35 |
| 17 | [0.3, 9.7] | 9.7 0.3 | Yes | 6.34 |
| 18 | [4.2, 5.8] | 4.2 5.8 | Yes | 6.87 |
| 19 | [1.3, 8.7] | 8.7 1.3 | Yes | 5.75 |
| 20 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.79 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HZW3UTVTO1XX | HZW3UTVT01XX | No | 8.12 |
| 2 | PM3EC4OKHFEQ | PM3EC4OKHFEOQ | No | 13.41 |
| 3 | VGMQQCZDCV2R | VGMQOCZDCV2R | No | 3.92 |
| 4 | F3ILN1G9ZXKZ | F3ILN1G9ZXKZ | Yes | 3.33 |
| 5 | 1XI6LQIGOESW | 1X16LQIGQESW | No | 13.52 |
| 6 | 8KRCJ5G79LOY | 8KRCJ5G79L0Y | No | 12.82 |
| 7 | QSXTPD3OSMXA | QSXTPD305SMXA | No | 8.51 |
| 8 | 6DCPYNALB1Y3 | 6DCPVNALB1Y3 | No | 2.7 |
| 9 | B75GX3NLT7PK | B75G3XNLT7PK | No | 6.29 |
| 10 | QLZ7AJJPB95T | QLZ7AJUPB95T | No | 4.64 |
| 11 | SMGYGHQQIQ5E | SMGYGHQOI5E | No | 16.72 |
| 12 | JPWTMMGY7JY9 | JPWTMMGY7JY9 | Yes | 3.75 |
| 13 | WKMWKLVRHMOT | WKMVWKLVRHMOT | No | 6.12 |
| 14 | W3RVGRWME40R | W3RVG8RWME4OR | No | 10.91 |
| 15 | V79UM1WKY0SP | V79UM1WKYOSP | No | 8.41 |
| 16 | 0Y8SJEAT3GX8 | 0Y8SJEAT3GX8 | Yes | 3.15 |
| 17 | 0QAYQIQ02EVW | 00AYQI002EVVW | No | 3.92 |
| 18 | DCV2E2XSRMO2 | DCV2E2XSRM02 | No | 6.25 |
| 19 | QDK52GOFHO7T | QDKS2GOFH07T | No | 17.67 |
| 20 | G5ZHV7AHQL7W | G5ZHNV7AHOL7W | No | 5.91 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7 | 7 | Yes | 1.71 |
| 2 | 64 |  | No | 43.65 |
| 3 | 67 | 67 | Yes | 3.61 |
| 4 | 28 | 28 | Yes | 5.73 |
| 5 | 63 | 63 | Yes | 13.2 |
| 6 | 48 | 48 | Yes | 6.55 |
| 7 | 16 | 16 | Yes | 5.83 |
| 8 | 4096 | 4096 | Yes | 20.51 |
| 9 | 39 | 39 | Yes | 4.59 |
| 10 | 198 | 198 | Yes | 18.31 |
| 11 | 19 | 19 | Yes | 7.5 |
| 12 | 20 |  | No | 44.5 |
| 13 | 26 |  | No | 44.33 |
| 14 | 31 | 31 | Yes | 7.57 |
| 15 | 73 | 73 | Yes | 4.15 |
| 16 | 7680 | 7680 | Yes | 10.59 |
| 17 | 5 | 5 | Yes | 4.16 |
| 18 | 9 | 9 | Yes | 9.14 |
| 19 | 243 | 243 | Yes | 3.67 |
| 20 | 793 | 793 | Yes | 4.19 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _   _<)_\ |  | No | 63.87 |
| 2 | /((  \_\( |  | No | 65.04 |
| 3 | /((( _< ) |  | No | 72.55 |
| 4 | _\ )/))<  | _\␣)/))<␣ | Yes | 6.14 |
| 5 | \(())_))/ |  | No | 22.41 |
| 6 | <_\/)<(_\ |  | No | 17.1 |
| 7 | ) //\_ _< |  | No | 62.77 |
| 8 | /< <\(/)_ | /< <\(/)_ | Yes | 13.25 |
| 9 | ///))/(__ | ///))/(__ | Yes | 11.1 |
| 10 | __ \(/\/< | __ \(/\/< | Yes | 17.42 |
| 11 | \)<_\)_</ | \)<_\)_</ | Yes | 19.05 |
| 12 | (_)\\<_/< | (_)\\</< | No | 23.9 |
| 13 | \/<\((((  | /\) <(_<) | No | 20.28 |
| 14 | _)/)\() < | _)/)\() < | Yes | 11.23 |
| 15 | (\  ) <)/ | (\__)_<)/ | Yes | 20.44 |
| 16 | _< <(<_)) | _< <(<_)) | Yes | 19.77 |
| 17 | ( / \)_<< | ( / \)_<< | Yes | 27.51 |
| 18 |  ( </(\<\ | _(_</(\<\ | Yes | 22.8 |
| 19 | <\(<_/) _ | <\(<_/) _ | Yes | 17.2 |
| 20 | ((_<<(\)_ | ((_<<(\)_ | Yes | 13.33 |
