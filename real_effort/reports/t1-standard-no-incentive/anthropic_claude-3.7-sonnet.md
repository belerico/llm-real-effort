# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8380 | 31581 | 39961 | 0 | 20 | 23.05 | 461.13 |
| add_numbers | 4300 | 3739 | 8039 | 20 | 0 | 4.28 | 85.73 |
| counting_zeros | 7240 | 27343 | 34583 | 12 | 8 | 17.01 | 340.53 |
| task_decoding | 13680 | 7901 | 21581 | 18 | 2 | 6.48 | 129.72 |
| task_summation | 7600 | 22289 | 29889 | 20 | 0 | 14.64 | 292.97 |
| task_transcription | 4432 | 5251 | 9683 | 17 | 3 | 5.40 | 108.18 |
| task_sequences | 3560 | 16316 | 19876 | 17 | 3 | 12.03 | 240.6 |
| **TOTAL** | **49192** | **114420** | **163612** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 2 1 4 2 3 1 5 4 1 4 2 5 | 4 5 2 2 3 4 1 5 1 5 4 2 | No | 22.19 |
| 2 | 1 2 4 5 1 1 3 4 5 2 6 2 6 3 | 1 2 4 5 1 3 2 5 6 2 3 6 | No | 23.05 |
| 3 | 5 4 6 1 2 2 4 5 3 6 5 5 2 1 | 5 4 6 2 1 2 4 5 5 6 5 1 2 | No | 22.34 |
| 4 | 4 3 2 6 4 3 3 6 4 5 5 1 3 2 | 4 3 2 3 4 6 6 3 4 5 5 1 3 2 | No | 22.93 |
| 5 | 6 1 2 1 3 4 2 6 5 5 1 2 3 4 | 1 6 2 3 1 2 4 6 5 5 1 2 3 4 | No | 19.87 |
| 6 | 5 4 1 1 6 4 4 1 3 6 5 5 2 6 | 1 5 4 1 4 6 4 1 3 6 5 5 2 6 | No | 20.76 |
| 7 | 6 4 1 4 5 2 6 4 3 1 3 2 6 3 | 4 6 1 4 5 2 5 6 3 3 1 3 6 2 3 | No | 25.25 |
| 8 | 1 1 3 6 4 6 4 3 1 5 1 3 6 2 | 1 6 3 1 4 6 4 3 1 5 3 1 6 2 | No | 18.23 |
| 9 | 1 2 2 3 2 3 1 2 1 1 4 5 5 1 | 1 2 2 3 2 3 1 1 1 4 5 5 1 | No | 29.15 |
| 10 | 2 6 1 2 5 6 5 6 1 2 3 6 5 3 | 2 1 6 5 2 6 5 6 1 3 2 6 5 3 | No | 19.96 |
| 11 | 1 4 3 4 5 1 2 6 4 2 3 3 5 4 | 1 3 4 4 5 1 2 6 4 2 3 3 4 5 | No | 22.53 |
| 12 | 1 5 6 3 3 4 3 4 1 2 6 4 5 3 | 1 5 3 6 3 4 3 1 6 2 4 5 | No | 22.72 |
| 13 | 5 4 3 6 1 1 3 5 6 6 3 3 6 3 | 1 4 3 6 5 5 3 1 6 6 3 3 6 3 | No | 25.38 |
| 14 | 5 4 3 5 1 3 2 6 4 5 6 3 6 4 | 5 4 3 1 5 2 3 6 4 5 3 6 6 4 | No | 21.74 |
| 15 | 5 3 2 1 2 3 6 3 5 2 4 6 4 3 | 5 3 1 2 2 3 6 3 3 6 4 2 6 5 4 2 3 | No | 27.72 |
| 16 | 1 5 6 4 6 3 1 1 3 2 5 2 5 4 | 1 6 5 4 6 3 1 1 3 2 5 2 5 4 | No | 26.11 |
| 17 | 6 5 4 1 6 5 4 4 2 1 2 4 5 3 | 6 4 5 1 5 4 6 4 2 1 2 4 5 3 | No | 19.22 |
| 18 | 1 4 3 1 5 5 4 3 4 2 5 5 4 6 | 1 4 3 5 1 5 4 3 1 6 4 2 5 4 6 5 | No | 23.08 |
| 19 | 3 2 5 1 2 6 3 4 5 4 6 4 3 1 | Looking at this 6×6 Sudoku puzzle, I need to fill in all the missing numbers following the Sudoku rules.  I'll work through this methodically, looking at the constraints for each empty cell:  First, I'll analyze what's already given: ``` _ 1 6 _ 5 4 4 _ 3 _ 6 _ _ 2 4 5 1 _ 1 3 2 6 _ _ 5 _ 1 3 2 _ 2 6 5 _ _ _ ```  Working through each empty cell by checking rows, columns, and 2×3 boxes:  For the first row (R1C1 and R1C4): - R1C1 must be 3 (1,4,5,6 are used in row; 2,4,5 in column) - R1C4 must be 2 (1,3,5,6 are used in row; 3,5,6 in column)  Second row (R2C2, R2C4, R2C6): - R2C2 must be 2 (1,3,4,6 are used in row) - R2C4 must be 1 (2,3,4,6 are used in row) - R2C6 must be 5 (1,2,3,4,6 are used in row)  Continuing through all rows and following the constraints, the complete filled grid is: ``` 3 1 6 2 5 4 4 2 3 1 6 5 6 2 4 5 1 3 1 3 2 6 4 5 5 4 1 3 2 6 2 6 5 4 3 1 ```  Reading the previously missing numbers in left | No | 30.97 |
| 20 | 1 5 4 3 5 1 6 2 5 5 6 4 1 6 | 5 4 1 5 3 5 1 6 5 2 6 5 4 6 1 | No | 17.75 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 751 | 751 | Yes | 3.53 |
| 2 | 2040 | 2040 | Yes | 4.7 |
| 3 | 1190 | 1190 | Yes | 3.6 |
| 4 | 1882 | 1882 | Yes | 5.44 |
| 5 | 1135 | 1135 | Yes | 5.49 |
| 6 | 1379 | 1379 | Yes | 3.32 |
| 7 | 1927 | 1927 | Yes | 4.35 |
| 8 | 1341 | 1341 | Yes | 4.11 |
| 9 | 1292 | 1292 | Yes | 3.15 |
| 10 | 1679 | 1679 | Yes | 3.76 |
| 11 | 2077 | 2077 | Yes | 4.37 |
| 12 | 1809 | 1809 | Yes | 4.63 |
| 13 | 913 | 913 | Yes | 5.16 |
| 14 | 1261 | 1261 | Yes | 4.35 |
| 15 | 1051 | 1051 | Yes | 3.94 |
| 16 | 1420 | 1420 | Yes | 8.12 |
| 17 | 1227 | 1227 | Yes | 3.52 |
| 18 | 1710 | 1710 | Yes | 4.07 |
| 19 | 1672 | 1672 | Yes | 3.22 |
| 20 | 2170 | 2170 | Yes | 2.82 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 73 | Yes | 20.88 |
| 2 | 68 | 68 | Yes | 14.88 |
| 3 | 50 | 50 | Yes | 19.5 |
| 4 | 52 | 51 | No | 14.49 |
| 5 | 71 | 70 | No | 22.97 |
| 6 | 69 | 70 | No | 15.41 |
| 7 | 63 | 63 | Yes | 16.1 |
| 8 | 60 | 57 | No | 10.84 |
| 9 | 52 | 52 | Yes | 17.46 |
| 10 | 44 | 44 | Yes | 19.47 |
| 11 | 46 | 46 | Yes | 15.58 |
| 12 | 61 | 61 | Yes | 18.89 |
| 13 | 38 | 38 | Yes | 16.74 |
| 14 | 55 | 55 | Yes | 16.57 |
| 15 | 43 | 43 | Yes | 13.82 |
| 16 | 54 | 54 | Yes | 20.16 |
| 17 | 37 | Looking at the binary grid in the image, I need to count all zeros (0):  Row 1: 1 0 0 0 1 0 0 1 1 1 (4 zeros) Row 2: 0 0 1 1 1 1 1 1 1 1 (2 zeros) Row 3: 1 1 1 0 1 1 1 1 1 0 (2 zeros) Row 4: 0 1 1 1 1 1 1 1 1 1 (1 zero) Row 5: 1 1 0 0 0 1 1 1 0 1 (4 zeros) Row 6: 0 1 1 1 1 1 1 1 1 1 (1 zero) Row 7: 1 1 1 1 0 0 1 1 1 1 (2 zeros) Row 8: 1 1 1 1 1 0 0 1 1 1 (2 zeros) Row 9: 1 1 1 0 1 1 1 1 1 1 (1 zero) Row 10: 1 0 0 1 | No | 23.34 |
| 18 | 58 | 59 | No | 13.26 |
| 19 | 51 | 52 | No | 13.65 |
| 20 | 48 | 47 | No | 16.19 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MFSNCWH | MFSNCWH | Yes | 9.59 |
| 2 | AEVIZTP | AEVIZT P | No | 8.9 |
| 3 | FGDUJKQ | FGDUJKQ | Yes | 5.96 |
| 4 | HLRVBKP | HLRVBKP | Yes | 5.11 |
| 5 | NZOCBTM | NZOCBTM | Yes | 6.02 |
| 6 | QYFUKJS | QYFUKJS | Yes | 6.11 |
| 7 | ESBXARF | ESBARAF | No | 10.29 |
| 8 | CKNEDOI | CKNEDOI | Yes | 6.18 |
| 9 | AYBSGOH | AYBSGOH | Yes | 6.93 |
| 10 | BTJCWDV | BTJCWDV | Yes | 3.55 |
| 11 | AHPBQWJ | AHPBQWJ | Yes | 8.04 |
| 12 | WTOLUFP | WTOLUFP | Yes | 4.97 |
| 13 | BEGNTFO | BEGNTFO | Yes | 5.75 |
| 14 | FSAVNOK | FSAVNOK | Yes | 4.6 |
| 15 | XOJNFZM | XOJNFZM | Yes | 6.27 |
| 16 | WMDFRVK | WMDFRVK | Yes | 6.72 |
| 17 | DMWLJEP | DMWLJEP | Yes | 6.54 |
| 18 | JFYOUGH | JFYOUGH | Yes | 5.28 |
| 19 | JRHDAKW | JRHDAKW | Yes | 6.59 |
| 20 | TMSXGBZ | TMSXGBZ | Yes | 6.11 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.2, 5.8] | 4.2 5.8 | Yes | 12.77 |
| 2 | [3.2, 6.8] | 3.2 6.8 | Yes | 12.96 |
| 3 | [2.8, 7.2] | 2.8 7.2 | Yes | 15.31 |
| 4 | [4.6, 5.4] | 5.4 4.6 | Yes | 15.76 |
| 5 | [2.8, 7.2] | 2.8 7.2 | Yes | 17.78 |
| 6 | [1.6, 8.4] | 8.4 1.6 | Yes | 11.6 |
| 7 | [0.4, 9.6] | 9.6 0.4 | Yes | 17.56 |
| 8 | [3.9, 6.1] | 6.1 3.9 | Yes | 11.07 |
| 9 | [2.5, 7.5] | 7.5 2.5 | Yes | 15.62 |
| 10 | [4.4, 5.6] | 4.4 5.6 | Yes | 14.58 |
| 11 | [1.1, 8.9] | 8.9 1.1 | Yes | 14.77 |
| 12 | [2.7, 7.3] | 2.7 7.3 | Yes | 14.91 |
| 13 | [0.3, 9.7] | 9.7 0.3 | Yes | 15.45 |
| 14 | [0.9, 9.1] | 0.9 9.1 | Yes | 20.44 |
| 15 | [1.0, 9.0] | 9.0 1.0 | Yes | 15.56 |
| 16 | [1.5, 8.5] | 1.5 8.5 | Yes | 13.43 |
| 17 | [4.7, 5.3] | 4.7 5.3 | Yes | 10.31 |
| 18 | [3.8, 6.2] | 3.8 6.2 | Yes | 18.63 |
| 19 | [3.7, 6.3] | 6.3 3.7 | Yes | 13.14 |
| 20 | [4.6, 5.4] | 5.4 4.6 | Yes | 11.13 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SG5R67FWG4V1 | SG5R67FWG4V1 | Yes | 5.46 |
| 2 | VY0XLKQIDTLI | VYOXLKOIDTLI | No | 4.28 |
| 3 | 7V7FJ5CXM7H1 | 7V7FJ5CXM7H1 | Yes | 5.9 |
| 4 | GNOWEFKC57IG | GNOWEFKC57IG | Yes | 5.21 |
| 5 | GGG4XY1IW8XW | GGG4XY1IW8XW | Yes | 4.93 |
| 6 | X9DC6MHI9JVQ | X9DC6MHI9JVQ | Yes | 6.83 |
| 7 | FHMTUKKJVGLC | FHMTUKKJVGLC | Yes | 4.47 |
| 8 | D6JITE0R9B2R | D6JITE0R9B2R | Yes | 4.6 |
| 9 | 0IUXJ2S13M9A | 0IUXJ2S13M9A | Yes | 4.47 |
| 10 | PQ0R1DG05UH6 | POOR1DG05UH6 | No | 4.25 |
| 11 | 2DRISY9U732S | 2DRISY9U732S | Yes | 6.14 |
| 12 | 1TFYYLZ6DS3Y | 1TFYYLZ6DS33Y | No | 7.06 |
| 13 | HJDFA6LC3NY2 | HJDFA6LC3NY2 | Yes | 5.19 |
| 14 | SHLFSUE13W0G | SHLFSUE13W0G | Yes | 5.83 |
| 15 | 31P8W9SWBIJU | 31P8W9SWBIJU | Yes | 5.28 |
| 16 | AAY7JVC9Y4AR | AAY7JVC9Y4AR | Yes | 4.4 |
| 17 | S2O0ZQ6FUZ8D | S2O0ZQ6FUZ8D | Yes | 9.21 |
| 18 | TEUA4Z94E44Y | TEUA4Z94E44Y | Yes | 3.95 |
| 19 | O1PS8LXSRMFC | O1PS8LXSRMFC | Yes | 5.12 |
| 20 | 5VZIOIS1HV6K | 5VZIOIS1HV6K | Yes | 5.48 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 17.62 |
| 2 | 39 | 39 | Yes | 19.54 |
| 3 | 20 |  | No | 28.08 |
| 4 | 48 | 48 | Yes | 6.2 |
| 5 | 7680 | 7680 | Yes | 9.6 |
| 6 | 28 | 28 | Yes | 9.23 |
| 7 | 64 | 42 | No | 17.81 |
| 8 | 16 | 16 | Yes | 9.18 |
| 9 | 1 | 1 | Yes | 7.9 |
| 10 | 63 | 63 | Yes | 7.0 |
| 11 | 67 | 67 | Yes | 4.56 |
| 12 | 793 | 793 | Yes | 4.41 |
| 13 | 10 | 9 | No | 15.3 |
| 14 | 3 | 3 | Yes | 26.56 |
| 15 | 5 | 5 | Yes | 16.11 |
| 16 | 243 | 243 | Yes | 5.87 |
| 17 | 4 | 4 | Yes | 8.26 |
| 18 | 31 | 31 | Yes | 5.63 |
| 19 | 9 | 9 | Yes | 7.42 |
| 20 | 26 | 26 | Yes | 14.33 |
