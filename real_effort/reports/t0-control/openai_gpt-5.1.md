# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-19 10:37:08

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
| sudoku_game | 7460 | 40960 | 48420 | 0 | 20 | 58.89 | 1178.01 |
| add_numbers | 6480 | 1441 | 7921 | 20 | 0 | 3.71 | 74.31 |
| counting_zeros | 6540 | 40960 | 47500 | 0 | 20 | 80.45 | 1609.39 |
| task_decoding | 9800 | 5317 | 15117 | 20 | 0 | 7.50 | 150.27 |
| task_summation | 6800 | 9129 | 15929 | 20 | 0 | 10.33 | 206.84 |
| task_transcription | 6560 | 2900 | 9460 | 19 | 1 | 4.97 | 99.61 |
| task_sequences | 2421 | 9459 | 11880 | 20 | 0 | 10.78 | 215.64 |
| **TOTAL** | **46061** | **110166** | **156227** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 3 1 6 5 3 2 1 1 3 4 5 2 4 |  | No | 54.46 |
| 2 | 2 1 3 6 1 3 5 2 4 3 6 1 3 6 |  | No | 54.06 |
| 3 | 1 5 6 3 3 6 5 1 3 2 5 3 2 6 |  | No | 60.8 |
| 4 | 3 1 3 1 4 6 3 1 1 4 4 2 1 3 |  | No | 60.13 |
| 5 | 3 3 3 5 2 4 2 6 3 5 6 1 2 3 |  | No | 53.7 |
| 6 | 2 1 5 6 3 1 3 5 6 1 4 5 1 3 |  | No | 51.79 |
| 7 | 1 3 4 3 5 4 6 3 5 2 1 4 2 5 |  | No | 64.0 |
| 8 | 3 1 2 5 2 3 6 6 1 3 6 3 3 4 |  | No | 65.0 |
| 9 | 1 6 3 6 4 3 2 6 4 4 5 2 5 1 |  | No | 43.51 |
| 10 | 2 6 5 1 4 3 3 6 5 1 2 6 4 3 |  | No | 59.84 |
| 11 | 3 5 3 1 3 1 2 6 5 1 4 2 3 6 |  | No | 79.44 |
| 12 | 5 4 1 2 3 6 4 2 4 5 2 3 4 2 |  | No | 51.15 |
| 13 | 3 6 2 1 2 2 2 5 5 4 1 2 1 4 |  | No | 62.05 |
| 14 | 2 5 3 1 6 3 2 1 6 1 5 2 3 6 |  | No | 62.22 |
| 15 | 1 2 4 6 4 5 3 1 1 3 6 5 1 3 |  | No | 62.67 |
| 16 | 5 6 1 3 4 2 2 5 6 3 5 5 1 6 |  | No | 59.79 |
| 17 | 5 3 1 5 4 1 6 4 1 3 3 5 2 4 |  | No | 57.81 |
| 18 | 3 1 1 5 3 4 5 1 1 2 4 6 6 5 |  | No | 61.38 |
| 19 | 2 3 3 3 5 2 6 3 6 5 6 5 3 2 |  | No | 49.22 |
| 20 | 5 3 2 6 3 5 3 5 2 3 2 4 6 1 |  | No | 64.76 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1443 | 1443 | Yes | 3.56 |
| 2 | 1701 | 1701 | Yes | 3.29 |
| 3 | 1314 | 1314 | Yes | 3.66 |
| 4 | 1727 | 1727 | Yes | 4.49 |
| 5 | 1349 | 1349 | Yes | 4.07 |
| 6 | 2302 | 2302 | Yes | 3.13 |
| 7 | 1093 | 1093 | Yes | 3.63 |
| 8 | 2279 | 2279 | Yes | 4.08 |
| 9 | 1138 | 1138 | Yes | 4.03 |
| 10 | 1229 | 1229 | Yes | 3.35 |
| 11 | 2625 | 2625 | Yes | 2.86 |
| 12 | 1239 | 1239 | Yes | 3.36 |
| 13 | 1176 | 1176 | Yes | 3.5 |
| 14 | 1876 | 1876 | Yes | 4.13 |
| 15 | 1210 | 1210 | Yes | 3.18 |
| 16 | 2071 | 2071 | Yes | 4.25 |
| 17 | 1008 | 1008 | Yes | 3.95 |
| 18 | 1580 | 1580 | Yes | 3.52 |
| 19 | 1430 | 1430 | Yes | 4.36 |
| 20 | 2013 | 2013 | Yes | 3.79 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 |  | No | 60.97 |
| 2 | 44 |  | No | 78.3 |
| 3 | 61 |  | No | 54.16 |
| 4 | 61 |  | No | 73.84 |
| 5 | 69 |  | No | 119.77 |
| 6 | 38 |  | No | 70.32 |
| 7 | 38 |  | No | 84.59 |
| 8 | 40 |  | No | 56.67 |
| 9 | 46 |  | No | 88.62 |
| 10 | 60 |  | No | 62.59 |
| 11 | 67 |  | No | 81.09 |
| 12 | 54 |  | No | 110.96 |
| 13 | 38 |  | No | 72.18 |
| 14 | 48 |  | No | 87.31 |
| 15 | 69 |  | No | 107.64 |
| 16 | 35 |  | No | 64.45 |
| 17 | 57 |  | No | 81.39 |
| 18 | 74 |  | No | 93.13 |
| 19 | 45 |  | No | 90.99 |
| 20 | 61 |  | No | 70.09 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QTRBOWY | QTRBOWY | Yes | 6.96 |
| 2 | NKJUPME | NKJUPME | Yes | 6.97 |
| 3 | UEIFQMD | UEIFQMD | Yes | 7.96 |
| 4 | LKMZPBJ | LKMZPBJ | Yes | 7.11 |
| 5 | UCVPAMW | UCVPAMW | Yes | 9.27 |
| 6 | XMYHKST | XMYHKST | Yes | 7.27 |
| 7 | KFSHXZR | KFSHXZR | Yes | 11.76 |
| 8 | HLMZUCY | HLMZUCY | Yes | 8.48 |
| 9 | OHRGVJD | OHRGVJD | Yes | 5.83 |
| 10 | XTMZAQN | XTMZAQN | Yes | 5.63 |
| 11 | XHCPBJF | XHCPBJF | Yes | 7.99 |
| 12 | DRKCHXY | DRKCHXY | Yes | 8.87 |
| 13 | VBYAGWU | VBYAGWU | Yes | 4.37 |
| 14 | LTHBSOF | LTHBSOF | Yes | 9.87 |
| 15 | MQUNPWE | MQUNPWE | Yes | 8.98 |
| 16 | JPHOVFX | JPHOVFX | Yes | 5.89 |
| 17 | HGEJUPL | HGEJUPL | Yes | 3.67 |
| 18 | QEMORCJ | QEMORCJ | Yes | 7.05 |
| 19 | REHMLUZ | REHMLUZ | Yes | 6.34 |
| 20 | JGRUEAM | JGRUEAM | Yes | 9.77 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 4.3 5.7 | Yes | 14.98 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.27 |
| 3 | [2.3, 7.7] | 2.3 7.7 | Yes | 8.71 |
| 4 | [4.6, 5.4] | 4.6 5.4 | Yes | 8.29 |
| 5 | [2.0, 8.0] | 2.0 8.0 | Yes | 11.03 |
| 6 | [2.5, 7.5] | 2.5 7.5 | Yes | 10.32 |
| 7 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.33 |
| 8 | [3.8, 6.2] | 6.2 3.8 | Yes | 7.97 |
| 9 | [4.6, 5.4] | 4.6 5.4 | Yes | 9.38 |
| 10 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.85 |
| 11 | [3.0, 7.0] | 7.0 3.0 | Yes | 11.11 |
| 12 | [0.7, 9.3] | 9.3 0.7 | Yes | 7.5 |
| 13 | [2.6, 7.4] | 2.6 7.4 | Yes | 8.18 |
| 14 | [1.2, 8.8] | 1.2 8.8 | Yes | 14.67 |
| 15 | [3.1, 6.9] | 3.1 6.9 | Yes | 12.57 |
| 16 | [2.9, 7.1] | 2.9 7.1 | Yes | 8.28 |
| 17 | [3.6, 6.4] | 3.6 6.4 | Yes | 8.77 |
| 18 | [0.7, 9.3] | 9.3 0.7 | Yes | 15.1 |
| 19 | [4.8, 5.2] | 5.2 4.8 | Yes | 12.37 |
| 20 | [2.5, 7.5] | 2.5 7.5 | Yes | 11.94 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VI1W1MUY8XIY | VI1W1MUY8XIY | Yes | 4.27 |
| 2 | 4Z6ESGI7569A | 4Z6ESGI7569A | Yes | 5.31 |
| 3 | BJXNB253OMN2 | BJXNB253OMN2 | Yes | 6.91 |
| 4 | VER5DLEORUNU | VER5DLEORUNU | Yes | 7.51 |
| 5 | S7S2V8YHQ65W | S7S2V8YHQ65W | Yes | 4.27 |
| 6 | 1WNIUKGT4RV7 | 1WNIUKGT4RV7 | Yes | 3.98 |
| 7 | 3V8UE2MKYX9K | 3V8UE2MKYX9K | Yes | 3.66 |
| 8 | ZQADJGQIZFM8 | ZQADJGQIZFM8 | Yes | 2.05 |
| 9 | 45CAUTKKO6EF | 45CAUTKKO6EF | Yes | 2.78 |
| 10 | XGAWY3OZHO9T | XGAWY3OZH09T | No | 6.35 |
| 11 | 866Z6OGYZMT2 | 866Z6OGYZMT2 | Yes | 8.9 |
| 12 | RX0XNU44TY4L | RX0XNU44TY4L | Yes | 4.91 |
| 13 | 3J8C2R6VYAHT | 3J8C2R6VYAHT | Yes | 6.75 |
| 14 | BNURLTTUYZG6 | BNURLTTUYZG6 | Yes | 4.99 |
| 15 | IAVHLIKGMRAS | IAVHLIKGMRAS | Yes | 5.72 |
| 16 | 8ZJDJXVBGDUZ | 8ZJDJXVBGDUZ | Yes | 3.61 |
| 17 | 414ZMH4ECFF9 | 414ZMH4ECFF9 | Yes | 6.35 |
| 18 | 01H7LQCXYFIB | 01H7LQCXYFIB | Yes | 4.05 |
| 19 | 5X2ETEQHG0RU | 5X2ETEQHG0RU | Yes | 4.52 |
| 20 | X393SHGBX9HN | X393SHGBX9HN | Yes | 2.6 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 5.81 |
| 2 | 60 | 60 | Yes | 5.23 |
| 3 | 20 | 20 | Yes | 38.61 |
| 4 | 6 | 6 | Yes | 4.21 |
| 5 | 793 | 793 | Yes | 4.89 |
| 6 | 73 | 73 | Yes | 8.46 |
| 7 | 65 | 65 | Yes | 4.18 |
| 8 | 67 | 67 | Yes | 4.27 |
| 9 | 9 | 9 | Yes | 7.15 |
| 10 | 3 | 3 | Yes | 4.72 |
| 11 | 48 | 48 | Yes | 3.93 |
| 12 | 26 | 26 | Yes | 33.89 |
| 13 | 44 | 44 | Yes | 12.48 |
| 14 | 4096 | 4096 | Yes | 34.81 |
| 15 | 4 | 4 | Yes | 3.4 |
| 16 | 39 | 39 | Yes | 5.99 |
| 17 | 7 | 7 | Yes | 3.13 |
| 18 | 3 | 3 | Yes | 15.41 |
| 19 | 28 | 28 | Yes | 11.52 |
| 20 | 16 | 16 | Yes | 3.54 |
