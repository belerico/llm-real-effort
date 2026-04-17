# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-27 10:03:22

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
| sudoku_game | 6485 | 33306 | 39791 | 8 | 12 | 25.22 | 504.36 |
| add_numbers | 3860 | 614 | 4474 | 20 | 0 | 2.64 | 52.89 |
| counting_zeros | 5180 | 15440 | 20620 | 9 | 11 | 10.08 | 201.64 |
| task_decoding | 5180 | 1813 | 6993 | 19 | 1 | 3.92 | 78.44 |
| task_summation | 5240 | 5437 | 10677 | 20 | 0 | 5.65 | 112.92 |
| task_transcription | 4024 | 757 | 4781 | 20 | 0 | 3.45 | 68.96 |
| task_sequences | 3921 | 5539 | 9460 | 18 | 2 | 7.07 | 141.48 |
| string_entry | 4390 | 1352 | 5742 | 13 | 7 | 4.04 | 80.9 |
| **TOTAL** | **38280** | **64258** | **102538** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 5 6 3 2 3 1 4 1 5 4 6 1 | 4 6 5 6 3 2 3 1 4 1 5 4 1 6 1 | No | 19.09 |
| 2 | 2 3 6 5 4 2 1 3 2 6 1 2 3 1 |  | No | 35.3 |
| 3 | 4 2 2 3 5 4 6 3 1 5 6 4 6 3 | 4 2 2 3 5 4 6 3 1 5 6 4 6 3 1 | No | 21.6 |
| 4 | 1 2 4 5 3 1 3 6 6 1 4 2 2 1 | 1 2 4 5 3 1 3 6 6 1 4 2 2 1 | Yes | 20.98 |
| 5 | 4 5 1 3 6 4 6 3 5 3 4 2 4 1 | 4 5 1 3 6 4 6 3 5 3 4 2 4 1 | Yes | 17.42 |
| 6 | 3 2 1 4 6 2 4 3 5 3 2 3 6 2 |  | No | 35.93 |
| 7 | 1 5 5 1 1 5 2 6 1 4 2 3 6 2 | 1 5 5 1 1 5 2 6 1 4 2 3 6 2 | Yes | 21.69 |
| 8 | 6 2 5 1 4 3 5 1 5 3 2 2 3 1 |  | No | 34.61 |
| 9 | 1 2 6 2 4 6 3 6 5 2 6 1 5 1 | 1 2 6 2 4 6 3 6 5 2 6 1 5 1 | Yes | 21.3 |
| 10 | 3 1 4 5 3 1 6 2 1 5 1 3 2 1 | 3 1 4 5 3 1 6 2 1 5 1 3 2 1 | Yes | 18.42 |
| 11 | 5 2 3 4 4 2 6 5 5 1 2 3 6 5 | 5 2 3 4 4 2 6 5 5 1 2 3 6 5 | Yes | 20.37 |
| 12 | 3 1 6 5 3 4 1 3 6 3 4 3 6 1 | Looking at this puzzle, I need to find all missing numbers using Sudoku constraints.  **Given grid:** ``` . 4 2 \| 5 . . . 2 1 \| 6 . . ------+------ 1 6 4 \| 3 2 5 2 . 5 \| 4 6 . ------+------ . 5 . \| 1 . 2 4 . . \| 2 5 . ```  **Solving step-by-step:**  - **Box 3 (R3-4, C1-3):** Has {1,6,4,2,5} → R4C2 = **3**, then R4C6 = **1** - **Column 2:** Needs {1,3}, R4C2=3 → R6C2 | No | 31.25 |
| 13 | 3 1 6 2 3 5 3 6 6 4 2 1 2 4 | 3 1 6 2 3 5 3 6 6 4 2 1 2 4 | Yes | 17.87 |
| 14 | 3 4 3 5 2 1 6 1 4 3 1 6 4 1 | 3 4 3 5 2 1 6 1 4 3 6 1 2 6 4 1 | No | 20.32 |
| 15 | 2 4 4 5 6 2 5 1 4 1 5 6 4 1 | 2 4 4 5 6 2 3 5 6 1 4 1 5 6 4 1 2 | No | 22.03 |
| 16 | 3 2 6 5 6 5 4 1 6 5 2 1 4 6 |  | No | 32.02 |
| 17 | 3 1 4 4 5 3 1 4 2 4 6 5 6 3 | 3 1 4 4 5 3 1 4 2 4 6 5 6 3 | Yes | 20.71 |
| 18 | 3 2 4 5 2 4 1 3 2 6 4 5 4 3 |  | No | 30.39 |
| 19 | 2 5 1 4 3 5 1 2 1 2 3 2 5 1 |  | No | 36.21 |
| 20 | 2 5 3 3 4 5 1 3 4 2 3 4 2 1 | 2 5 3 3 4 5 1 3 4 2 1 3 4 2 1 | No | 26.81 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1177 | 1177 | Yes | 3.35 |
| 2 | 1693 | 1693 | Yes | 2.61 |
| 3 | 1578 | 1578 | Yes | 2.77 |
| 4 | 1928 | 1928 | Yes | 2.55 |
| 5 | 1323 | 1323 | Yes | 2.74 |
| 6 | 665 | 665 | Yes | 2.19 |
| 7 | 2155 | 2155 | Yes | 2.4 |
| 8 | 2122 | 2122 | Yes | 3.08 |
| 9 | 1795 | 1795 | Yes | 2.83 |
| 10 | 1735 | 1735 | Yes | 3.28 |
| 11 | 1542 | 1542 | Yes | 2.28 |
| 12 | 589 | 589 | Yes | 2.98 |
| 13 | 1607 | 1607 | Yes | 2.69 |
| 14 | 1777 | 1777 | Yes | 2.26 |
| 15 | 1351 | 1351 | Yes | 3.53 |
| 16 | 1940 | 1940 | Yes | 2.36 |
| 17 | 1355 | 1355 | Yes | 2.17 |
| 18 | 2056 | 2056 | Yes | 2.32 |
| 19 | 1196 | 1196 | Yes | 2.09 |
| 20 | 1736 | 1736 | Yes | 2.41 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 61 | 61 | Yes | 11.87 |
| 2 | 67 | 67 | Yes | 9.41 |
| 3 | 68 | 62 | No | 6.89 |
| 4 | 62 | 60 | No | 12.14 |
| 5 | 65 | 66 | No | 10.47 |
| 6 | 49 | 49 | Yes | 15.42 |
| 7 | 41 | 41 | Yes | 11.07 |
| 8 | 55 | 50 | No | 8.12 |
| 9 | 65 | 65 | Yes | 9.7 |
| 10 | 49 | 46 | No | 7.86 |
| 11 | 65 | 65 | Yes | 9.58 |
| 12 | 54 | 51 | No | 6.7 |
| 13 | 63 | 63 | Yes | 10.29 |
| 14 | 52 | 50 | No | 10.24 |
| 15 | 72 | 73 | No | 7.5 |
| 16 | 64 | 64 | Yes | 10.06 |
| 17 | 67 | 67 | Yes | 21.67 |
| 18 | 60 | 54 | No | 8.88 |
| 19 | 71 | 64 | No | 6.69 |
| 20 | 68 | 62 | No | 7.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VMWNZCX | VMWNZCX | Yes | 3.31 |
| 2 | LTBFVQK | LTBFVQK | Yes | 3.82 |
| 3 | XRNCEMA | XRNCEMA | Yes | 3.75 |
| 4 | YSUZWDQ | YSUZWDQ | Yes | 5.45 |
| 5 | CZFGKLY | CZFGKLY | Yes | 3.35 |
| 6 | PQNELWD | PQNELWD | Yes | 3.68 |
| 7 | OJWHCQG | OJWHCQG | Yes | 4.47 |
| 8 | QZHYTML | QZHYTML | Yes | 4.2 |
| 9 | EQFYGSR | EQFYGSR | Yes | 3.51 |
| 10 | QXZEAKJ | QXZEAKJ | Yes | 3.8 |
| 11 | VTOGZWN | VTOGZWN | Yes | 3.97 |
| 12 | YSIEZJT | YSIEZJT | Yes | 4.39 |
| 13 | IJACXFD | IJACXFD | Yes | 3.9 |
| 14 | KFNWAQC | KFNWAQC | Yes | 4.05 |
| 15 | QJUDVRL | QJUDVRL | Yes | 5.14 |
| 16 | QYTSBOK | QYTSBOK | Yes | 4.35 |
| 17 | TRZIHKG | TRZIKHG | No | 3.52 |
| 18 | QRWBFZS | QRWBFZS | Yes | 3.04 |
| 19 | FKTABNM | FKTABNM | Yes | 3.66 |
| 20 | ZSNFAVH | ZSNFAVH | Yes | 3.08 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.2, 8.8] | 8.8 1.2 | Yes | 6.71 |
| 2 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.92 |
| 3 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.58 |
| 4 | [1.4, 8.6] | 8.6 1.4 | Yes | 5.36 |
| 5 | [2.2, 7.8] | 7.8 2.2 | Yes | 5.98 |
| 6 | [1.7, 8.3] | 8.3 1.7 | Yes | 4.03 |
| 7 | [3.3, 6.7] | 6.7 3.3 | Yes | 6.92 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 3.38 |
| 9 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.58 |
| 10 | [4.5, 5.5] | 5.5 4.5 | Yes | 7.67 |
| 11 | [0.3, 9.7] | 9.7 0.3 | Yes | 6.79 |
| 12 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.64 |
| 13 | [4.4, 5.6] | 4.4 5.6 | Yes | 4.39 |
| 14 | [4.5, 5.5] | 4.5 5.5 | Yes | 5.28 |
| 15 | [3.5, 6.5] | 6.5 3.5 | Yes | 7.85 |
| 16 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.63 |
| 17 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.1 |
| 18 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.01 |
| 19 | [1.4, 8.6] | 8.6 1.4 | Yes | 6.45 |
| 20 | [2.8, 7.2] | 7.2 2.8 | Yes | 5.65 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OVT1WMBUJNAF | OVT1WMBUJNAF | Yes | 2.82 |
| 2 | C6NM4PNH071A | C6NM4PNH071A | Yes | 2.73 |
| 3 | TP3WP9UGZ4AG | TP3WP9UGZ4AG | Yes | 2.54 |
| 4 | Y0HVJRK17I4N | Y0HVJRK17I4N | Yes | 2.62 |
| 5 | BWS1TGFHK0W8 | BWS1TGFHK0W8 | Yes | 2.62 |
| 6 | GGK8Z2OZS873 | GGK8Z2OZS873 | Yes | 2.85 |
| 7 | G2D7CHA39WEX | G2D7CHA39WEX | Yes | 2.59 |
| 8 | D3ZQ5W0J7S17 | D3ZQ5W0J7S17 | Yes | 2.81 |
| 9 | QLSEV2ISAP5J | QLSEV2ISAP5J | Yes | 2.61 |
| 10 | HJSUUTHA88NT | HJSUUTHA88NT | Yes | 2.56 |
| 11 | 5CWLW3NNF6XG | 5CWLW3NNF6XG | Yes | 3.01 |
| 12 | GKCO1KWNCGP0 | GKCO1KWNCGP0 | Yes | 2.7 |
| 13 | WGL8K7BZCZZS | WGL8K7BZCZZS | Yes | 9.82 |
| 14 | 7HDOUUYEFVO2 | 7HDOUUYEFVO2 | Yes | 4.13 |
| 15 | LE1I6QBZ7Y55 | LE1I6QBZ7Y55 | Yes | 3.24 |
| 16 | DL3NA6BG604N | DL3NA6BG604N | Yes | 3.01 |
| 17 | A0L4D7CI78TJ | A0L4D7CI78TJ | Yes | 2.35 |
| 18 | LJMA9I89FDAD | LJMA9I89FDAD | Yes | 8.04 |
| 19 | VMG46I4LD9YL | VMG46I4LD9YL | Yes | 3.08 |
| 20 | JDI1KAR53F0N | JDI1KAR53F0N | Yes | 2.84 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 5.52 |
| 2 | 1440 | 1440 | Yes | 5.2 |
| 3 | 10 | 10 | Yes | 4.0 |
| 4 | 63 | 63 | Yes | 13.26 |
| 5 | 60 | 60 | Yes | 4.59 |
| 6 | 4 | 4 | Yes | 2.6 |
| 7 | 9 | 9 | Yes | 4.99 |
| 8 | 67 | 67 | Yes | 2.59 |
| 9 | 793 | 793 | Yes | 4.25 |
| 10 | 26 | 26 | Yes | 7.28 |
| 11 | 4 | 4 | Yes | 5.76 |
| 12 | 64 | 64 | Yes | 7.91 |
| 13 | 60 | 60 | Yes | 4.7 |
| 14 | 1 | 1 | Yes | 6.55 |
| 15 | 198 | 198 | Yes | 6.58 |
| 16 | 73 | 73 | Yes | 6.26 |
| 17 | 28 | 28 | Yes | 4.06 |
| 18 | 23 | 23 | Yes | 5.25 |
| 19 | 5 | 18 | No | 24.76 |
| 20 | 4096 | 16384 | No | 15.38 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _<(( (/)/ | _<(( (/)/ | Yes | 5.52 |
| 2 | \_\//(  \ | \_\//(  \ | Yes | 3.28 |
| 3 |  \\/_)/\\ | \\/_)/\\ | No | 2.98 |
| 4 | ( \\()  < | ( \\() | No | 3.17 |
| 5 | \_\ /(\\  | \_\ /(\\ | No | 7.14 |
| 6 | <<))<< _( | <<))<< _( | Yes | 2.96 |
| 7 | <//)\ _(\ | <//)\ _(\ | Yes | 5.48 |
| 8 |   )(/_\)) | )(/_\)) | No | 3.8 |
| 9 | )((/\_/<_ | )((/\_/<_ | Yes | 3.82 |
| 10 | \(  _ <_( | \(  _ <_( | Yes | 3.05 |
| 11 | (<__ ())  | (<__ ()) | No | 3.34 |
| 12 | )_)\(\(_/ | )_)\(\(_/ | Yes | 4.16 |
| 13 | \\ _)/\(/ | \\ _)/\(/ | Yes | 3.67 |
| 14 | /))() /_/ | /))() /_/ | Yes | 3.2 |
| 15 | <_ (/ ((  | <_ (/ (( | No | 3.55 |
| 16 |  <()__ (_ | <()__ (_ | No | 7.64 |
| 17 | \)(<_(_// | \)(<_(_// | Yes | 3.74 |
| 18 | _ _)(\/)) | _ _)(\/)) | Yes | 3.85 |
| 19 | <\))/\(// | <\))/\(// | Yes | 3.0 |
| 20 | <))_ (((\ | <))_ (((\ | Yes | 3.55 |
