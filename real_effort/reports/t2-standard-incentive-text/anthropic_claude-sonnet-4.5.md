# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-27 10:09:12

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
| sudoku_game | 6026 | 33043 | 39069 | 10 | 10 | 30.73 | 614.72 |
| add_numbers | 3720 | 2995 | 6715 | 20 | 0 | 4.65 | 92.95 |
| counting_zeros | 5040 | 20530 | 25570 | 4 | 16 | 13.04 | 260.8 |
| task_decoding | 5040 | 7354 | 12394 | 20 | 0 | 6.16 | 123.13 |
| task_summation | 5100 | 13333 | 18433 | 20 | 0 | 9.23 | 184.56 |
| task_transcription | 3879 | 2892 | 6771 | 20 | 0 | 3.88 | 77.59 |
| task_sequences | 3781 | 8074 | 11855 | 18 | 2 | 7.67 | 153.5 |
| string_entry | 4231 | 3975 | 8206 | 12 | 8 | 4.78 | 95.49 |
| **TOTAL** | **36817** | **92196** | **129013** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 4 6 6 1 2 2 6 5 5 3 6 1 6 | 2 4 6 6 1 2 2 6 5 5 3 6 1 6 | Yes | 20.94 |
| 2 | 3 2 1 6 3 2 6 1 4 6 3 4 3 5 | 3 2 1 6 3 2 6 1 4 6 3 4 3 5 | Yes | 23.01 |
| 3 | 2 2 4 1 3 5 6 5 1 5 6 3 2 5 | 2 2 1 5 3 6 | No | 30.13 |
| 4 | 3 1 6 6 2 4 6 2 3 6 3 2 6 4 | Looking at this 6×6 Sudoku puzzle, I need to find the missing numbers in each row.  Let me solve systematically:  **Row 1:** . . 5 \| 2 4 . - Missing: 1, 3, 6 - Col 1 needs: 2, 3, 6 (has 4, 5, 1) - Col 2 needs: 1, 6 (has 2, 4, 5, 3) - Col 6 needs: 2, 4, 6 (has 5, 3, 1) - Row 1, Col 6 must be 6 (only option from {1,3,6} ∩ {2,4,6}) - Row 1, Col 1 must be 3, Col 2 must be 1 - **Row 1: 3 1 5 2 4 6**  **Row 2:** 4 . 3 \| 1 . 5 - Missing: 2, 6 - Col 2 needs 6 (checking column constraints) - Col 5 must be 2 - **Row 2: 4 6 3 1 2 5**  **Row 3:** 5 2 . \| . 1 3 - Missing: 4, 6 - Col 3 needs 4 (has 5, 3, 6, 1, 2) - Col 4 must be 6 - **Row 3: 5 2 4 6 1 3**  **Row 4:** . 4 6 \| . 5 1 - Missing: 2, 3 - Col 1 needs 2 or 6, row needs 2, so Col 1 = 2 - Col 4 must be 3 - **Row 4: 2 4 6 3 5 1**  **Row 5:** . 5 1 \| 4 . . - Missing: 2, 3, 6 - Col 1 needs 6 (only option left) - Col 5 needs 3, Col 6 needs 2 - **Row 5: 6 5 1 4 3 2**  **Row 6:** 1 3 2 \| 5 . . - Missing: 4, 6 - Col 5 needs 6, Col 6 needs 4 - **Row 6: 1 3 2 5 6 4**  Missing numbers in reading order: 3 1 6 6 2 4 | No | 27.24 |
| 5 | 5 4 1 3 4 4 3 6 3 4 2 6 1 3 | 5 4 1 3 4 4 3 6 3 4 2 6 1 3 | Yes | 20.42 |
| 6 | 6 5 3 5 3 3 4 6 5 5 4 3 1 2 | TIMEOUT | No | 120.02 |
| 7 | 2 6 1 4 2 6 2 5 4 1 2 4 6 2 | 2 6 1 4 2 6 2 5 4 1 2 4 6 2 | Yes | 24.28 |
| 8 | 4 3 2 3 4 2 5 4 6 5 4 1 4 2 | 2 3 4 3 4 4 5 2 6 5 4 1 4 2 | No | 24.51 |
| 9 | 4 6 2 3 5 1 4 6 3 6 1 4 3 6 | 4 6 2 3 5 1 4 6 3 6 1 4 3 6 | Yes | 21.64 |
| 10 | 1 5 6 3 4 6 1 1 4 6 4 3 2 5 | 1 5 6 3 4 6 1 1 4 6 4 3 2 5 | Yes | 21.21 |
| 11 | 4 6 1 3 4 4 5 3 6 4 3 2 4 6 | 4 6 1 3 4 4 5 3 6 4 3 2 4 6 | Yes | 20.68 |
| 12 | 2 1 1 6 2 2 1 6 4 6 1 6 1 3 | 2 1 6 5 2 1 6 2 4 6 1 6 1 3 | No | 28.88 |
| 13 | 3 2 4 6 2 1 3 6 3 4 2 4 1 2 | 3 2 4 6 2 3 1 6 4 3 2 4 1 2 | No | 27.59 |
| 14 | 3 1 2 3 2 4 5 3 6 3 5 6 3 2 | 3 1 3 2 3 5 6 4 4 5 3 2 6 | No | 19.8 |
| 15 | 2 3 2 1 3 6 2 3 5 2 4 4 3 6 | 2 3 2 1 3 6 2 3 5 2 4 4 3 6 | Yes | 17.28 |
| 16 | 1 6 4 5 3 6 2 6 3 3 5 4 5 3 | 1 6 4 5 3 6 2 6 3 3 5 4 5 3 | Yes | 25.58 |
| 17 | 1 3 6 1 3 2 6 4 2 3 3 2 6 4 | 3 1 6 1 2 3 6 4 3 2 3 2 6 4 | No | 27.46 |
| 18 | 5 2 3 4 1 5 4 6 1 5 4 6 1 5 | 5 2 3 4 1 5 4 6 1 5 4 6 1 5 | Yes | 22.79 |
| 19 | 3 2 6 1 4 5 6 2 3 1 4 1 6 2 | 3 2 6 1 4 5 2 3 1 4 1 6 2 | No | 60.53 |
| 20 | 6 1 3 1 2 1 3 4 5 1 4 2 1 6 | 1 6 3 1 2 1 3 4 5 1 4 2 1 6 | No | 30.7 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2160 | 2160 | Yes | 4.05 |
| 2 | 1226 | 1226 | Yes | 3.44 |
| 3 | 644 | 644 | Yes | 3.87 |
| 4 | 1762 | 1762 | Yes | 3.22 |
| 5 | 1000 | 1000 | Yes | 3.63 |
| 6 | 2189 | 2189 | Yes | 2.71 |
| 7 | 2101 | 2101 | Yes | 3.5 |
| 8 | 1831 | 1831 | Yes | 3.34 |
| 9 | 1666 | 1666 | Yes | 3.31 |
| 10 | 2273 | 2273 | Yes | 2.96 |
| 11 | 1797 | 1797 | Yes | 2.85 |
| 12 | 1441 | 1441 | Yes | 3.53 |
| 13 | 1317 | 1317 | Yes | 3.12 |
| 14 | 1477 | 1477 | Yes | 9.16 |
| 15 | 2064 | 2064 | Yes | 4.48 |
| 16 | 1865 | 1865 | Yes | 10.34 |
| 17 | 1468 | 1468 | Yes | 11.13 |
| 18 | 1794 | 1794 | Yes | 7.3 |
| 19 | 2198 | 2198 | Yes | 3.16 |
| 20 | 1376 | 1376 | Yes | 3.85 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 54 | No | 11.77 |
| 2 | 54 | 51 | No | 10.92 |
| 3 | 57 | 55 | No | 11.71 |
| 4 | 44 | 38 | No | 12.41 |
| 5 | 54 | 54 | Yes | 19.15 |
| 6 | 53 | 53 | Yes | 11.95 |
| 7 | 54 | 48 | No | 8.73 |
| 8 | 67 | 60 | No | 14.82 |
| 9 | 59 | 47 | No | 8.33 |
| 10 | 62 | 63 | No | 12.58 |
| 11 | 74 | 72 | No | 12.0 |
| 12 | 40 | 29 | No | 13.31 |
| 13 | 70 | 70 | Yes | 14.1 |
| 14 | 57 | 55 | No | 18.65 |
| 15 | 52 | 50 | No | 7.15 |
| 16 | 62 | 60 | No | 32.47 |
| 17 | 71 | 69 | No | 11.73 |
| 18 | 53 | 50 | No | 9.47 |
| 19 | 62 | 50 | No | 7.95 |
| 20 | 65 | 65 | Yes | 11.58 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EDTRJZM | EDTRJZM | Yes | 4.67 |
| 2 | JANYGUH | JANYGUH | Yes | 8.12 |
| 3 | OHINMLD | OHINMLD | Yes | 9.76 |
| 4 | SICGKYF | SICGKYF | Yes | 6.56 |
| 5 | GIZWSJQ | GIZWSJQ | Yes | 5.79 |
| 6 | FCHYZIE | FCHYZIE | Yes | 7.67 |
| 7 | AQZEMJU | AQZEMJU | Yes | 5.03 |
| 8 | RNGYXBO | RNGYXBO | Yes | 6.55 |
| 9 | XBOIYKG | XBOIYKG | Yes | 8.88 |
| 10 | ODGWKYC | ODGWKYC | Yes | 6.9 |
| 11 | CNBIPZM | CNBIPZM | Yes | 4.74 |
| 12 | LARODUX | LARODUX | Yes | 4.84 |
| 13 | OMSAGXD | OMSAGXD | Yes | 6.52 |
| 14 | JEXTSHW | JEXTSHW | Yes | 8.04 |
| 15 | IJCTLYH | IJCTLYH | Yes | 5.06 |
| 16 | SUGOCVH | SUGOCVH | Yes | 5.88 |
| 17 | JSLOGQV | JSLOGQV | Yes | 4.69 |
| 18 | UTKFHAZ | UTKFHAZ | Yes | 4.2 |
| 19 | GWMKZHJ | GWMKZHJ | Yes | 4.5 |
| 20 | PTXNMFL | PTXNMFL | Yes | 4.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.59 |
| 2 | [4.3, 5.7] | 4.3 5.7 | Yes | 9.16 |
| 3 | [4.4, 5.6] | 5.6 4.4 | Yes | 7.2 |
| 4 | [5.0, 5.0] | 5.0 5.0 | Yes | 10.71 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 8.14 |
| 6 | [1.4, 8.6] | 8.6 1.4 | Yes | 6.95 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.48 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 18.95 |
| 9 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.11 |
| 10 | [4.5, 5.5] | 4.5 5.5 | Yes | 12.16 |
| 11 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.52 |
| 12 | [2.9, 7.1] | 7.1 2.9 | Yes | 10.59 |
| 13 | [2.8, 7.2] | 2.8 7.2 | Yes | 14.89 |
| 14 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.32 |
| 15 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.98 |
| 16 | [0.7, 9.3] | 9.3 0.7 | Yes | 11.37 |
| 17 | [2.3, 7.7] | 7.7 2.3 | Yes | 8.33 |
| 18 | [3.0, 7.0] | 7.0 3.0 | Yes | 8.49 |
| 19 | [4.7, 5.3] | 4.7 5.3 | Yes | 10.51 |
| 20 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.12 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CAYT37O0J6L8 | CAYT37O0J6L8 | Yes | 3.57 |
| 2 | 6O6JY43HBHWQ | 6O6JY43HBHWQ | Yes | 3.67 |
| 3 | 4YRVCCD0VRU7 | 4YRVCCD0VRU7 | Yes | 3.7 |
| 4 | 7O8E95L9BJPU | 7O8E95L9BJPU | Yes | 3.46 |
| 5 | 6JQRDMH26TN0 | 6JQRDMH26TN0 | Yes | 3.74 |
| 6 | IZMR6Y3N317R | IZMR6Y3N317R | Yes | 3.13 |
| 7 | E3SDV525J76X | E3SDV525J76X | Yes | 3.89 |
| 8 | VHNIXQSB3BEP | VHNIXQSB3BEP | Yes | 3.29 |
| 9 | LWWWC257J9K1 | LWWWC257J9K1 | Yes | 4.2 |
| 10 | AH1OLCPT0M4U | AH1OLCPT0M4U | Yes | 4.2 |
| 11 | BIEXXXL59WFD | BIEXXXL59WFD | Yes | 3.22 |
| 12 | S9V2M8EHUF85 | S9V2M8EHUF85 | Yes | 3.47 |
| 13 | XCN622U9X0UT | XCN622U9X0UT | Yes | 3.55 |
| 14 | QDHTRURDR2F4 | QDHTRURDR2F4 | Yes | 3.24 |
| 15 | NUFN1GH3SEGN | NUFN1GH3SEGN | Yes | 6.76 |
| 16 | GGYZ71OH583U | GGYZ71OH583U | Yes | 6.0 |
| 17 | DFIKL08P28HI | DFIKL08P28HI | Yes | 3.3 |
| 18 | 2R2XY25MQC7B | 2R2XY25MQC7B | Yes | 3.05 |
| 19 | IBP1LMLY5XFC | IBP1LMLY5XFC | Yes | 3.73 |
| 20 | 9I4J3TJKHCHE | 9I4J3TJKHCHE | Yes | 4.43 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 4.72 |
| 2 | 6 | 6 | Yes | 5.08 |
| 3 | 198 | 198 | Yes | 6.14 |
| 4 | 1 | 1 | Yes | 6.47 |
| 5 | 243 | 243 | Yes | 5.03 |
| 6 | 16 | 16 | Yes | 14.76 |
| 7 | 4096 | 1048576 | No | 12.23 |
| 8 | 28 | 28 | Yes | 5.82 |
| 9 | 26 | 26 | Yes | 8.49 |
| 10 | 48 | 48 | Yes | 4.71 |
| 11 | 4 | 4 | Yes | 6.19 |
| 12 | 9 | 9 | Yes | 5.5 |
| 13 | 39 | 39 | Yes | 5.38 |
| 14 | 31 | 31 | Yes | 5.23 |
| 15 | 65 | 65 | Yes | 5.25 |
| 16 | 3 | 3 | Yes | 25.88 |
| 17 | 7 | 7 | Yes | 3.11 |
| 18 | 5 | 18 | No | 11.39 |
| 19 | 9 | 9 | Yes | 7.29 |
| 20 | 4 | 4 | Yes | 4.83 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /\_(\()_< | /\_(\()_ | No | 4.79 |
| 2 | _((_)/ \< | _((_)/ \ | No | 4.56 |
| 3 | ___\/\/\  | ___\/\/\ | No | 5.59 |
| 4 | <<\\//< / | <<\\//< / | Yes | 3.75 |
| 5 | /<(\///_( | /<(\///_( | Yes | 4.93 |
| 6 | /</)(\\_) | /</)(\\_) | Yes | 5.04 |
| 7 | ((//(<\<\ | ((//(<\<\ | Yes | 4.01 |
| 8 | \) _\(<(  | \) _\(< | No | 5.87 |
| 9 | /\\(_\<<< | /\\(_\<< | No | 5.36 |
| 10 | /_))</_<\ | /_))</_<\ | Yes | 3.52 |
| 11 | ((<)  _/\ | ((<)  _/\ | Yes | 4.81 |
| 12 |  / \ (_\< | /  \ (_\ | No | 6.64 |
| 13 | <(<)_\((< | <(<)_\(( | No | 4.15 |
| 14 | _)(\ \_<\ | _)(\ \_<\ | Yes | 3.6 |
| 15 | _  )<\) ) | _  )<\) ) | Yes | 5.67 |
| 16 |  <\(\_\(/ | <\(\_\(/ | No | 5.65 |
| 17 | ()\\))\_\ | ()\\))\_\ | Yes | 4.14 |
| 18 | ) <)\_\<_ | ) <)\_\<_ | Yes | 3.6 |
| 19 | )/  \/)\) | )/  \/)\) | Yes | 4.97 |
| 20 | ))<__ _\_ | ))<__ _\_ | Yes | 4.85 |
