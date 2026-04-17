# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-19 03:16:59

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 7200 | 29255 | 36455 | 12 | 8 | 37.25 | 745.25 |
| add_numbers | 3780 | 868 | 4648 | 20 | 0 | 4.36 | 87.21 |
| counting_zeros | 6200 | 36831 | 43031 | 8 | 12 | 54.05 | 1081.47 |
| task_decoding | 11940 | 3816 | 15756 | 20 | 0 | 5.55 | 111.29 |
| task_summation | 7140 | 5214 | 12354 | 20 | 0 | 6.34 | 126.95 |
| task_transcription | 3617 | 2766 | 6383 | 14 | 6 | 4.45 | 89.18 |
| task_sequences | 2900 | 4685 | 7585 | 18 | 2 | 7.35 | 147.08 |
| **TOTAL** | **42777** | **83435** | **126212** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 6 2 2 6 5 3 3 2 1 6 4 6 | 3 2 6 2 2 6 5 3 3 2 1 6 4 6 | Yes | 18.83 |
| 2 | 3 4 1 5 6 4 2 3 4 3 4 3 4 5 | 3 4 1 5 6 4 2 3 4 3 4 3 4 5 | Yes | 21.29 |
| 3 | 3 1 5 3 6 5 4 2 3 6 3 4 4 5 |  | No | 56.02 |
| 4 | 4 6 5 1 4 1 5 3 6 4 2 3 2 5 |  | No | 67.17 |
| 5 | 2 3 6 1 4 3 4 3 3 4 1 4 5 2 | 2 3 6 1 4 3 4 3 3 4 1 4 5 2 | Yes | 18.8 |
| 6 | 3 6 4 5 1 1 6 4 5 2 1 6 5 4 |  | No | 66.15 |
| 7 | 2 6 5 2 5 6 1 1 4 1 3 6 2 4 | 2 6 5 2 5 6 1 1 4 1 3 6 2 4 | Yes | 22.53 |
| 8 | 5 2 3 3 6 1 5 5 1 2 6 4 2 6 |  | No | 44.86 |
| 9 | 3 5 3 2 6 4 2 5 4 2 1 6 2 4 | 3 5 3 2 6 4 2 5 4 2 1 6 2 4 | Yes | 19.3 |
| 10 | 3 5 6 5 3 1 4 3 6 5 2 4 5 3 | 3 5 6 5 3 1 4 3 6 5 2 4 5 3 | Yes | 19.93 |
| 11 | 3 1 2 4 6 4 3 6 4 1 5 6 2 1 |  | No | 65.86 |
| 12 | 5 4 1 6 4 2 3 6 2 6 1 5 4 3 | 5 4 1 6 4 2 3 6 2 6 1 5 4 3 | Yes | 16.93 |
| 13 | 2 1 6 2 6 2 4 6 1 2 4 2 3 5 | 2 1 6 2 6 2 4 6 1 2 4 2 3 5 | Yes | 18.59 |
| 14 | 4 2 5 6 4 1 2 4 5 3 4 5 6 1 | 4 2 5 6 4 1 2 4 5 3 4 5 6 1 | Yes | 18.41 |
| 15 | 3 5 2 4 1 3 6 1 4 1 3 4 3 1 |  | No | 69.27 |
| 16 | 3 1 6 3 5 2 4 5 1 6 5 3 6 5 | 3 1 6 3 5 2 4 5 1 6 5 3 6 5 | Yes | 21.42 |
| 17 | 4 5 6 1 1 2 5 2 3 4 1 3 5 4 |  | No | 65.03 |
| 18 | 1 5 2 3 1 5 4 2 5 6 2 2 4 1 | 1 5 2 3 1 5 4 2 5 6 2 2 4 1 | Yes | 17.61 |
| 19 | 1 3 6 3 6 4 5 5 4 1 3 5 4 5 |  | No | 71.97 |
| 20 | 3 6 2 3 4 2 4 1 5 5 6 1 4 3 | 3 6 2 3 4 2 4 1 5 5 6 1 4 3 | Yes | 25.07 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1794 | 1794 | Yes | 3.85 |
| 2 | 1454 | 1454 | Yes | 4.38 |
| 3 | 1881 | 1881 | Yes | 3.4 |
| 4 | 1574 | 1574 | Yes | 3.57 |
| 5 | 2235 | 2235 | Yes | 4.09 |
| 6 | 1778 | 1778 | Yes | 6.55 |
| 7 | 885 | 885 | Yes | 4.49 |
| 8 | 1403 | 1403 | Yes | 4.57 |
| 9 | 1902 | 1902 | Yes | 4.69 |
| 10 | 1072 | 1072 | Yes | 3.74 |
| 11 | 2315 | 2315 | Yes | 3.48 |
| 12 | 1632 | 1632 | Yes | 3.88 |
| 13 | 2162 | 2162 | Yes | 4.84 |
| 14 | 1927 | 1927 | Yes | 4.1 |
| 15 | 1587 | 1587 | Yes | 4.71 |
| 16 | 1485 | 1485 | Yes | 6.61 |
| 17 | 995 | 995 | Yes | 4.11 |
| 18 | 573 | 573 | Yes | 3.67 |
| 19 | 1929 | 1929 | Yes | 4.32 |
| 20 | 1985 | 1985 | Yes | 4.06 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 43 | 43 | Yes | 35.42 |
| 2 | 49 |  | No | 86.05 |
| 3 | 70 | 70 | Yes | 38.63 |
| 4 | 44 |  | No | 79.35 |
| 5 | 43 |  | No | 75.85 |
| 6 | 58 |  | No | 91.26 |
| 7 | 66 | 66 | Yes | 34.5 |
| 8 | 65 | 65 | Yes | 22.14 |
| 9 | 39 |  | No | 65.66 |
| 10 | 55 | 55 | Yes | 29.09 |
| 11 | 50 |  | No | 73.2 |
| 12 | 35 |  | No | 72.21 |
| 13 | 73 |  | No | 66.36 |
| 14 | 67 | 67 | Yes | 14.31 |
| 15 | 71 |  | No | 72.75 |
| 16 | 57 | 57 | Yes | 30.96 |
| 17 | 55 |  | No | 53.43 |
| 18 | 55 |  | No | 68.28 |
| 19 | 75 | 75 | Yes | 28.34 |
| 20 | 74 |  | No | 43.3 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SOFBUDR | SOFBUDR | Yes | 7.43 |
| 2 | NZEFOUK | NZEFOUK | Yes | 6.68 |
| 3 | YTSAVXD | YTSAVXD | Yes | 2.83 |
| 4 | JPKLYTH | JPKLYTH | Yes | 4.84 |
| 5 | ISGLMAD | ISGLMAD | Yes | 6.02 |
| 6 | IHEAKXZ | IHEAKXZ | Yes | 5.83 |
| 7 | YFOSATK | YFOSATK | Yes | 6.64 |
| 8 | NCVKOUH | NCVKOUH | Yes | 3.27 |
| 9 | MSUGTFJ | MSUGTFJ | Yes | 4.48 |
| 10 | HLEGRIF | HLEGRIF | Yes | 4.1 |
| 11 | HNDZMPQ | HNDZMPQ | Yes | 5.68 |
| 12 | CUSPILH | CUSPILH | Yes | 7.29 |
| 13 | VSCBJQM | VSCBJQM | Yes | 5.38 |
| 14 | WHDLVAM | WHDLVAM | Yes | 6.24 |
| 15 | UPZKHGX | UPZKHGX | Yes | 5.05 |
| 16 | XNDKWCZ | XNDKWCZ | Yes | 5.47 |
| 17 | IUAMPYC | IUAMPYC | Yes | 5.39 |
| 18 | HRNYZWV | HRNYZWV | Yes | 6.01 |
| 19 | TUOWRAS | TUOWRAS | Yes | 7.17 |
| 20 | JGCLNPX | JGCLNPX | Yes | 5.25 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 6.5 3.5 | Yes | 6.01 |
| 2 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.65 |
| 3 | [0.7, 9.3] | 0.7 9.3 | Yes | 5.88 |
| 4 | [1.8, 8.2] | 8.2 1.8 | Yes | 6.35 |
| 5 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.96 |
| 6 | [0.8, 9.2] | 0.8 9.2 | Yes | 7.22 |
| 7 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.2 |
| 8 | [4.5, 5.5] | 4.5 5.5 | Yes | 7.12 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.78 |
| 10 | [0.2, 9.8] | 0.2 9.8 | Yes | 6.05 |
| 11 | [2.0, 8.0] | 2.0 8.0 | Yes | 5.02 |
| 12 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.05 |
| 13 | [1.1, 8.9] | 8.9 1.1 | Yes | 7.44 |
| 14 | [3.1, 6.9] | 6.9 3.1 | Yes | 7.21 |
| 15 | [4.5, 5.5] | 5.5 4.5 | Yes | 5.4 |
| 16 | [2.5, 7.5] | 7.5 2.5 | Yes | 5.64 |
| 17 | [4.9, 5.1] | 5.1 4.9 | Yes | 5.99 |
| 18 | [4.4, 5.6] | 4.4 5.6 | Yes | 5.96 |
| 19 | [1.7, 8.3] | 8.3 1.7 | Yes | 6.71 |
| 20 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.11 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | V3SDL6LVVD0C | V3SDL6LVVDOC | No | 3.92 |
| 2 | BZX63EU84L7U | BZX63EU84L7U | Yes | 3.31 |
| 3 | 5JFGIW9XN2NK | 5JFGIW9XN2NK | Yes | 5.03 |
| 4 | GK50555N55TV | GK50555N55TV | Yes | 3.79 |
| 5 | NB5P5TBOYDEO | NB5P5TBOYDEO | Yes | 7.19 |
| 6 | 2N2SHO1TR4QX | 2N2SH01TR4QX | No | 4.51 |
| 7 | QH3ZJPG6VQBE | QH3ZJPG6VQBE | Yes | 3.09 |
| 8 | C3DWBOIHE2YE | C3DWB0IHE2YE | No | 5.86 |
| 9 | WUQN815STTJC | WUQN815STTJC | Yes | 4.82 |
| 10 | 9WQ3H8B8231T | 9WQ3H8B8231T | Yes | 5.18 |
| 11 | DXP8UWAV8O2Z | DXP8UWAVS02Z | No | 7.08 |
| 12 | 6AQ4WLIMFCBS | 6AQ4WLIMFCBS | Yes | 4.88 |
| 13 | 8FJ9SB3CFJT1 | 8FJ9SB3CFJT1 | Yes | 3.71 |
| 14 | AV93XVM1WOVN | AV93XVM1WOVN | Yes | 2.79 |
| 15 | 8BCC9M7GMR73 | 8BCC9M7GMR73 | Yes | 4.45 |
| 16 | FQKAMWW9W4HX | FQKAMWWSW4HX | No | 4.04 |
| 17 | S4VHH0IL74UJ | S4VHH0IL74UJ | Yes | 4.14 |
| 18 | QX7456DGSK2F | QX7436DGSK2F | No | 3.42 |
| 19 | ZOJZKOVKLSWY | ZOJZKOVKLSWY | Yes | 3.55 |
| 20 | Q7XLLD1TAU5F | Q7XLLD1TAU5F | Yes | 4.32 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 2 | No | 16.5 |
| 2 | 10 | 10 | Yes | 3.74 |
| 3 | 1 | 1 | Yes | 4.36 |
| 4 | 19 | 19 | Yes | 4.29 |
| 5 | 1440 | 1440 | Yes | 3.4 |
| 6 | 64 | 64 | Yes | 4.44 |
| 7 | 793 | 793 | Yes | 3.61 |
| 8 | 3 | 3 | Yes | 7.63 |
| 9 | 23 | 23 | Yes | 3.45 |
| 10 | 60 | 60 | Yes | 5.67 |
| 11 | 16 | 16 | Yes | 4.29 |
| 12 | 4 | 4 | Yes | 3.63 |
| 13 | 44 | 44 | Yes | 6.4 |
| 14 | 7680 | 7680 | Yes | 4.53 |
| 15 | 9 | 9 | Yes | 6.39 |
| 16 | 20 |  | No | 54.79 |
| 17 | 36 | 36 | Yes | 2.97 |
| 18 | 3 | 3 | Yes | 3.39 |
| 19 | 243 | 243 | Yes | 1.29 |
| 20 | 67 | 67 | Yes | 2.3 |
