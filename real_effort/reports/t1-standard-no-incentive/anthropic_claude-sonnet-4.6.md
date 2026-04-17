# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
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
| sudoku_game | 8380 | 35910 | 44290 | 10 | 10 | 28.60 | 572.25 |
| add_numbers | 4300 | 720 | 5020 | 20 | 0 | 2.18 | 43.81 |
| counting_zeros | 7240 | 30567 | 37807 | 5 | 15 | 16.90 | 338.27 |
| task_decoding | 13680 | 5233 | 18913 | 19 | 1 | 5.27 | 105.69 |
| task_summation | 7600 | 3073 | 10673 | 20 | 0 | 3.79 | 76.09 |
| task_transcription | 4452 | 853 | 5305 | 20 | 0 | 2.45 | 49.15 |
| task_sequences | 3561 | 3690 | 7251 | 19 | 1 | 4.07 | 81.45 |
| **TOTAL** | **49213** | **80046** | **129259** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 2 5 2 6 4 2 5 6 3 6 4 1 |  | No | 35.29 |
| 2 | 6 1 5 3 6 4 2 1 3 4 4 4 2 6 | 6 1 5 4 3 6 2 3 4 1 4 4 2 6 | No | 30.8 |
| 3 | 5 3 5 6 1 4 3 2 1 5 6 1 4 5 | Looking at the puzzle, I'll work through it systematically.  **Given grid:** - Row 1: 4, 2, 6, _, 1, 3 - Row 2: _, _, 2, 1, 4, 6 - Row 3: _, _, _, _, 5, _ - Row 4: _, 3, 5, 2, 6, 4 - Row 5: _, 4, 3, _, 2, _ - Row 6: 2, 6, 1, _, 3, _  **Solving step by step:**  **Row 1:** Has 1,2,3,4,6 → missing **5** at col4  **Row 6:** Missing 4,5 at cols 4,6. Box5 (rows4-6, cols3-4) needs 4 or 6 at row6 col4; row6 needs 4 or 5 → col4=**4**, col6=**5**  **Row 5, col4:** Box5 missing 6 → col4=**6**; Row5 missing 1,5 at cols1,6  **Row 4, col1:** Col1 has 4,2 → Row4 needs **1**  **Row 5, col1:** Box4 (rows4-6, cols1-2) needs 1,5; col1 missing 3,5,6 for rows2,3,5 → col1=**5**, col6=**1**  **Col2:** Has 2,3,4,6 → | No | 34.09 |
| 4 | 4 3 3 2 4 2 5 2 6 5 6 1 3 2 |  | No | 33.69 |
| 5 | 5 4 6 3 1 5 6 4 2 2 3 5 1 3 |  | No | 31.5 |
| 6 | 1 6 5 3 4 5 4 1 6 5 2 6 2 1 |  | No | 37.23 |
| 7 | 3 4 5 3 1 5 2 3 3 1 1 5 2 3 | 3 4 5 3 1 5 2 3 3 1 1 5 2 3 | Yes | 23.19 |
| 8 | 6 3 1 4 6 3 4 5 2 6 2 5 4 6 | 6 3 1 4 6 3 4 5 2 2 5 6 5 4 6 | No | 28.12 |
| 9 | 2 3 1 5 4 4 3 5 2 5 3 6 2 4 | 2 3 1 5 4 4 3 5 2 5 3 6 2 4 | Yes | 33.21 |
| 10 | 6 1 6 4 5 4 2 6 4 3 2 6 4 1 | 6 1 6 4 5 4 2 6 4 3 2 6 4 1 | Yes | 25.23 |
| 11 | 5 1 3 4 4 5 3 2 1 4 4 3 5 2 | 5 1 3 4 4 5 3 2 1 4 4 3 5 2 | Yes | 28.08 |
| 12 | 5 6 2 1 4 3 1 5 2 4 4 2 6 4 | 5 6 2 1 4 3 1 5 2 4 4 2 6 4 | Yes | 23.35 |
| 13 | 2 3 6 3 4 3 1 5 4 1 3 6 1 2 | 2 3 6 3 4 3 1 5 4 1 3 6 1 2 | Yes | 25.2 |
| 14 | 3 2 5 1 1 6 2 3 6 3 4 5 1 2 | 3 2 5 1 1 6 2 3 6 3 4 5 1 2 | Yes | 20.2 |
| 15 | 1 3 2 2 1 5 6 4 3 1 3 2 4 2 |  | No | 34.32 |
| 16 | 1 5 2 6 4 1 4 6 1 1 4 2 1 3 | 1 5 6 1 4 1 1 4 6 4 2 6 1 3 | No | 27.42 |
| 17 | 3 5 2 1 4 3 1 3 2 3 6 1 6 1 | 3 5 2 1 4 3 1 3 2 3 6 1 6 1 | Yes | 22.54 |
| 18 | 5 6 3 5 5 1 2 3 4 5 3 5 4 6 | 5 6 3 5 5 1 2 3 4 5 3 5 4 6 | Yes | 28.2 |
| 19 | 4 1 4 1 3 2 4 1 3 5 6 6 4 5 | 4 1 4 1 3 2 4 1 3 5 6 6 4 5 | Yes | 19.5 |
| 20 | 3 2 5 1 5 4 6 3 4 5 3 2 3 2 |  | No | 30.9 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2124 | 2124 | Yes | 1.96 |
| 2 | 1263 | 1263 | Yes | 1.88 |
| 3 | 1345 | 1345 | Yes | 1.62 |
| 4 | 1092 | 1092 | Yes | 1.75 |
| 5 | 1674 | 1674 | Yes | 2.01 |
| 6 | 1591 | 1591 | Yes | 2.05 |
| 7 | 2196 | 2196 | Yes | 2.13 |
| 8 | 1328 | 1328 | Yes | 2.31 |
| 9 | 2172 | 2172 | Yes | 2.49 |
| 10 | 1140 | 1140 | Yes | 1.97 |
| 11 | 1015 | 1015 | Yes | 2.11 |
| 12 | 2019 | 2019 | Yes | 2.26 |
| 13 | 1129 | 1129 | Yes | 1.42 |
| 14 | 1968 | 1968 | Yes | 1.76 |
| 15 | 1212 | 1212 | Yes | 3.42 |
| 16 | 1698 | 1698 | Yes | 2.78 |
| 17 | 2006 | 2006 | Yes | 3.14 |
| 18 | 1905 | 1905 | Yes | 2.82 |
| 19 | 1486 | 1486 | Yes | 2.21 |
| 20 | 1736 | 1736 | Yes | 1.61 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 62 | 55 | No | 13.99 |
| 2 | 65 | 67 | No | 19.13 |
| 3 | 74 | 67 | No | 14.93 |
| 4 | 55 | 50 | No | 17.52 |
| 5 | 55 | 54 | No | 17.62 |
| 6 | 62 | 56 | No | 17.61 |
| 7 | 58 | 67 | No | 17.52 |
| 8 | 36 | 67 | No | 19.26 |
| 9 | 47 | 47 | Yes | 16.75 |
| 10 | 59 | 55 | No | 15.72 |
| 11 | 35 | 35 | Yes | 18.17 |
| 12 | 43 | 42 | No | 14.29 |
| 13 | 58 | 58 | Yes | 18.79 |
| 14 | 57 | 55 | No | 14.05 |
| 15 | 36 | 67 | No | 15.39 |
| 16 | 67 | 67 | Yes | 14.28 |
| 17 | 71 | 71 | Yes | 18.6 |
| 18 | 53 | 67 | No | 18.07 |
| 19 | 66 | 67 | No | 18.0 |
| 20 | 75 | 67 | No | 18.24 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WVYHLRI | WVYHLRI | Yes | 6.09 |
| 2 | WNLBVIP | WNLBVIP | Yes | 6.06 |
| 3 | XCKQHLW | XCKQHLW | Yes | 4.89 |
| 4 | KPDXBUQ | KPDXBUQ | Yes | 5.26 |
| 5 | IKEJBXA | IKEJBXA | Yes | 5.63 |
| 6 | WKILTNV | WKILTNV | Yes | 5.26 |
| 7 | OKESLNP | OKESLNP | Yes | 4.96 |
| 8 | JHUXNZC | JHUXNZC | Yes | 4.51 |
| 9 | ACPTUEL | ACPTUEL | Yes | 5.45 |
| 10 | XODJYKQ | XODJYKQ | Yes | 5.62 |
| 11 | LPMEWXK | LPMEWXK | Yes | 5.79 |
| 12 | CRDTZVS | CRDTZVS | Yes | 5.88 |
| 13 | PJHRQMD | PJHRQMD | Yes | 5.1 |
| 14 | NGPMSOQ | NGPMSOQ | Yes | 6.19 |
| 15 | MCOYJAE | MCOYAJE | No | 5.08 |
| 16 | YSRFHUN | YSRFHUN | Yes | 4.8 |
| 17 | BKPEWLJ | BKPEWLJ | Yes | 5.16 |
| 18 | NURQJCO | NURQJCO | Yes | 3.98 |
| 19 | XYVSOGR | XYVSOGR | Yes | 4.9 |
| 20 | KVHOWDL | KVHOWDL | Yes | 4.86 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 8.2 1.8 | Yes | 3.69 |
| 2 | [4.0, 6.0] | 4.0 6.0 | Yes | 3.02 |
| 3 | [0.5, 9.5] | 0.5 9.5 | Yes | 3.62 |
| 4 | [3.1, 6.9] | 6.9 3.1 | Yes | 3.98 |
| 5 | [0.4, 9.6] | 9.6 0.4 | Yes | 4.59 |
| 6 | [4.6, 5.4] | 4.6 5.4 | Yes | 2.27 |
| 7 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.21 |
| 8 | [2.8, 7.2] | 7.2 2.8 | Yes | 3.24 |
| 9 | [0.4, 9.6] | 0.4 9.6 | Yes | 2.95 |
| 10 | [2.1, 7.9] | 7.9 2.1 | Yes | 2.62 |
| 11 | [1.0, 9.0] | 9.0 1.0 | Yes | 3.38 |
| 12 | [0.3, 9.7] | 0.3 9.7 | Yes | 4.77 |
| 13 | [3.0, 7.0] | 7.0 3.0 | Yes | 4.66 |
| 14 | [0.1, 9.9] | 9.9 0.1 | Yes | 4.36 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 2.56 |
| 16 | [1.2, 8.8] | 8.8 1.2 | Yes | 5.82 |
| 17 | [2.7, 7.3] | 7.3 2.7 | Yes | 3.5 |
| 18 | [1.2, 8.8] | 1.2 8.8 | Yes | 4.5 |
| 19 | [2.8, 7.2] | 2.8 7.2 | Yes | 2.79 |
| 20 | [3.2, 6.8] | 3.2 6.8 | Yes | 4.36 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3W731K3PUUJ8 | 3W731K3PUUJ8 | Yes | 4.25 |
| 2 | MEIFIFDMAMDN | MEIFIFDMAMDN | Yes | 2.07 |
| 3 | P9KKA8HSV4X8 | P9KKA8HSV4X8 | Yes | 1.76 |
| 4 | 1NQJ63O9ZCPZ | 1NQJ63O9ZCPZ | Yes | 1.89 |
| 5 | CHWMF4EGCM2Y | CHWMF4EGCM2Y | Yes | 2.68 |
| 6 | IHESRY4WFONR | IHESRY4WFONR | Yes | 2.31 |
| 7 | OZF6IMWJBUDP | OZF6IMWJBUDP | Yes | 2.29 |
| 8 | 6WA0FTC7MMSJ | 6WA0FTC7MMSJ | Yes | 2.67 |
| 9 | GU22XZPS81K6 | GU22XZPS81K6 | Yes | 2.63 |
| 10 | JJVXB6J5X4DL | JJVXB6J5X4DL | Yes | 1.96 |
| 11 | 827MTU9X7MF4 | 827MTU9X7MF4 | Yes | 2.19 |
| 12 | ZO7N6IOUVVOH | ZO7N6IOUVVOH | Yes | 3.57 |
| 13 | 33OVPS5SJ26A | 33OVPS5SJ26A | Yes | 3.17 |
| 14 | T378MIDIVJFU | T378MIDIVJFU | Yes | 2.41 |
| 15 | IAVM1BPP7IT6 | IAVM1BPP7IT6 | Yes | 2.92 |
| 16 | P6ZWT2GUWUZQ | P6ZWT2GUWUZQ | Yes | 2.76 |
| 17 | Z2GZIUB7QM6P | Z2GZIUB7QM6P | Yes | 1.9 |
| 18 | 3A2HQ0N93UYK | 3A2HQ0N93UYK | Yes | 1.85 |
| 19 | 18TF2GEHT76H | 18TF2GEHT76H | Yes | 1.86 |
| 20 | H7CVXRXK21HP | H7CVXRXK21HP | Yes | 1.89 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 2.41 |
| 2 | 28 | 28 | Yes | 3.05 |
| 3 | 4 | 4 | Yes | 2.06 |
| 4 | 9 | 9 | Yes | 3.1 |
| 5 | 243 | 243 | Yes | 1.53 |
| 6 | 4 | 4 | Yes | 3.73 |
| 7 | 23 | 23 | Yes | 1.9 |
| 8 | 39 | 39 | Yes | 2.3 |
| 9 | 5 | 14 | No | 17.03 |
| 10 | 10 | 10 | Yes | 2.43 |
| 11 | 44 | 44 | Yes | 4.45 |
| 12 | 60 | 60 | Yes | 2.69 |
| 13 | 16 | 16 | Yes | 3.57 |
| 14 | 20 | 20 | Yes | 4.87 |
| 15 | 6 | 6 | Yes | 1.97 |
| 16 | 7680 | 7680 | Yes | 4.01 |
| 17 | 3 | 3 | Yes | 3.59 |
| 18 | 4096 | 4096 | Yes | 13.09 |
| 19 | 60 | 60 | Yes | 1.89 |
| 20 | 36 | 36 | Yes | 1.77 |
