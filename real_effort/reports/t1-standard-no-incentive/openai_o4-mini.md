# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-19 03:19:02

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
| sudoku_game | 8540 | 40960 | 49500 | 0 | 20 | 40.16 | 803.45 |
| add_numbers | 4060 | 4339 | 8399 | 20 | 0 | 3.94 | 78.9 |
| counting_zeros | 7480 | 40960 | 48440 | 0 | 20 | 33.88 | 677.85 |
| task_decoding | 15520 | 21833 | 37353 | 15 | 5 | 16.00 | 320.2 |
| task_summation | 8740 | 19733 | 28473 | 19 | 1 | 17.04 | 340.94 |
| task_transcription | 3750 | 10996 | 14746 | 12 | 8 | 8.59 | 171.87 |
| task_sequences | 2720 | 9581 | 12301 | 20 | 0 | 7.33 | 146.51 |
| **TOTAL** | **50810** | **148402** | **199212** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 3 1 4 2 5 5 4 2 6 2 5 1 4 |  | No | 36.21 |
| 2 | 6 1 5 3 1 6 6 2 5 6 4 3 2 5 |  | No | 36.23 |
| 3 | 5 4 6 3 2 2 6 4 4 6 5 6 2 5 |  | No | 45.97 |
| 4 | 6 3 3 1 4 6 2 3 6 4 2 3 3 2 |  | No | 22.26 |
| 5 | 5 2 6 1 4 2 5 1 6 4 3 5 3 1 |  | No | 30.45 |
| 6 | 1 1 5 3 5 3 6 6 3 1 5 2 4 6 |  | No | 22.84 |
| 7 | 1 2 3 1 3 6 4 5 5 4 1 1 3 1 |  | No | 27.13 |
| 8 | 2 6 6 4 2 5 1 4 6 1 6 3 4 1 |  | No | 34.79 |
| 9 | 3 4 6 1 1 3 5 4 1 5 1 2 2 5 |  | No | 49.75 |
| 10 | 1 2 4 2 6 5 3 2 1 6 5 4 3 1 |  | No | 43.04 |
| 11 | 1 1 5 6 4 5 6 4 6 2 5 3 1 2 |  | No | 52.7 |
| 12 | 4 6 4 5 5 1 2 6 4 2 6 5 1 4 |  | No | 53.96 |
| 13 | 4 5 2 6 3 2 2 5 2 5 6 3 5 6 |  | No | 24.72 |
| 14 | 2 5 1 1 6 4 2 4 4 3 2 6 5 4 |  | No | 29.87 |
| 15 | 1 2 6 4 6 5 3 2 5 2 5 3 1 4 |  | No | 50.37 |
| 16 | 3 4 2 5 1 6 3 5 6 4 1 1 4 3 |  | No | 49.73 |
| 17 | 2 5 3 6 2 6 4 6 4 4 5 1 6 3 |  | No | 45.59 |
| 18 | 2 3 4 6 4 5 5 6 5 6 6 5 4 1 |  | No | 46.62 |
| 19 | 4 3 5 6 3 1 5 4 3 2 4 5 3 6 |  | No | 54.36 |
| 20 | 5 4 6 3 5 6 4 2 2 5 6 4 4 3 |  | No | 46.66 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1653 | 1653 | Yes | 2.85 |
| 2 | 1849 | 1849 | Yes | 2.71 |
| 3 | 1118 | 1118 | Yes | 2.0 |
| 4 | 1984 | 1984 | Yes | 12.12 |
| 5 | 1502 | 1502 | Yes | 7.68 |
| 6 | 1875 | 1875 | Yes | 3.16 |
| 7 | 2076 | 2076 | Yes | 2.71 |
| 8 | 964 | 964 | Yes | 5.48 |
| 9 | 2224 | 2224 | Yes | 3.47 |
| 10 | 2351 | 2351 | Yes | 3.52 |
| 11 | 2267 | 2267 | Yes | 6.91 |
| 12 | 1712 | 1712 | Yes | 2.78 |
| 13 | 1043 | 1043 | Yes | 2.22 |
| 14 | 903 | 903 | Yes | 2.34 |
| 15 | 2214 | 2214 | Yes | 2.18 |
| 16 | 1227 | 1227 | Yes | 3.12 |
| 17 | 2828 | 2828 | Yes | 4.53 |
| 18 | 1743 | 1743 | Yes | 2.83 |
| 19 | 1883 | 1883 | Yes | 3.55 |
| 20 | 1922 | 1922 | Yes | 2.62 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 47 |  | No | 26.1 |
| 2 | 72 |  | No | 28.57 |
| 3 | 50 |  | No | 48.93 |
| 4 | 38 |  | No | 19.72 |
| 5 | 70 |  | No | 28.14 |
| 6 | 72 |  | No | 46.36 |
| 7 | 62 |  | No | 43.42 |
| 8 | 65 |  | No | 21.94 |
| 9 | 54 |  | No | 47.7 |
| 10 | 63 |  | No | 56.98 |
| 11 | 45 |  | No | 27.09 |
| 12 | 69 |  | No | 34.36 |
| 13 | 75 |  | No | 36.54 |
| 14 | 52 |  | No | 18.02 |
| 15 | 51 |  | No | 17.81 |
| 16 | 49 |  | No | 48.71 |
| 17 | 45 |  | No | 34.27 |
| 18 | 70 |  | No | 50.63 |
| 19 | 59 |  | No | 15.71 |
| 20 | 39 |  | No | 26.55 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | CBRLKMG | CBRLKMG | Yes | 9.24 |
| 2 | FXKAWGI | FXKAWGI | Yes | 11.06 |
| 3 | ICYGAKS |  | No | 42.89 |
| 4 | AYTPBOG | AYTPBOG | Yes | 11.74 |
| 5 | UIJRBZX | UIJRBZX | Yes | 6.51 |
| 6 | KFLGCYP | KFLGCYP | Yes | 6.25 |
| 7 | JFTLAIV |  | No | 34.43 |
| 8 | APISZJT | APISZJT | Yes | 10.96 |
| 9 | FGAVYXQ | FGAVYXQ | Yes | 7.04 |
| 10 | FEQJCTP | FEQJCTP | Yes | 7.5 |
| 11 | SJXTPHN | SJXTPHN | Yes | 6.99 |
| 12 | GQPHICR | GQPHICR | Yes | 3.75 |
| 13 | IVMNAHD |  | No | 36.09 |
| 14 | SRXEFYM | SRXEFYM | Yes | 13.81 |
| 15 | QYKXDAB | QYKXDAB | Yes | 7.79 |
| 16 | FNPUZWD | FNPUZWD | Yes | 11.64 |
| 17 | AEXHTQJ | AEXHTQJ | Yes | 3.88 |
| 18 | BVETDGR | BVETDGR | Yes | 10.21 |
| 19 | VJZNMDE |  | No | 36.44 |
| 20 | EXONLJR |  | No | 41.77 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.77 |
| 2 | [1.6, 8.4] | 1.6 8.4 | Yes | 10.8 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.86 |
| 4 | [1.9, 8.1] | 1.9 8.1 | Yes | 9.15 |
| 5 | [3.4, 6.6] | 3.4 6.6 | Yes | 14.39 |
| 6 | [4.2, 5.8] | 5.8 4.2 | Yes | 101.2 |
| 7 | [4.5, 5.5] | 4.5 5.5 | Yes | 14.68 |
| 8 | [4.8, 5.2] | 4.8 5.2 | Yes | 10.37 |
| 9 | [1.9, 8.1] | 1.9 8.1 | Yes | 10.07 |
| 10 | [4.3, 5.7] | 4.3 5.7 | Yes | 13.23 |
| 11 | [4.0, 6.0] | 6.0 4.0 | Yes | 13.79 |
| 12 | [0.9, 9.1] |  | No | 24.89 |
| 13 | [0.4, 9.6] | 0.4 9.6 | Yes | 14.51 |
| 14 | [4.2, 5.8] | 4.2 5.8 | Yes | 24.33 |
| 15 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.23 |
| 16 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.57 |
| 17 | [2.6, 7.4] | 2.6 7.4 | Yes | 11.32 |
| 18 | [1.0, 9.0] | 1.0 9.0 | Yes | 13.14 |
| 19 | [4.9, 5.1] | 5.1 4.9 | Yes | 10.81 |
| 20 | [2.7, 7.3] | 7.3 2.7 | Yes | 11.59 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RP10K9O847NR | RP10K90847NR | No | 3.67 |
| 2 | JQPMXZ6QRVZ0 | JQPMXZ6QRVZ0 | Yes | 2.73 |
| 3 | KY888VFK13L4 | KY888VFK13L4 | Yes | 2.55 |
| 4 | 6ELO6W6T2LR9 |  | No | 43.57 |
| 5 | 3BGOESE5T6WW | 3BGOE5E5T6WW | No | 19.56 |
| 6 | 8F6EXUNZ8XS3 | 8F6EXUNZ8XS3 | Yes | 2.58 |
| 7 | 66FTWE81A9FU | 66FTWE81A9FU | Yes | 3.68 |
| 8 | V1V1QYCQ9HYQ | V1V1QYCQ9HYQ | Yes | 8.46 |
| 9 | 0RX4M9GH08MW | ORX4M9GH08MW | No | 9.06 |
| 10 | 66NBT9EK3VKF | 66NBT9EK3VKF | Yes | 10.42 |
| 11 | 57VN37V747K7 | 57VN37V747K7 | Yes | 3.7 |
| 12 | IDCZ1KJXRVZS | IDCZ1KJXRVZS | Yes | 3.83 |
| 13 | Z9C2JBVMJN2E | Z9C2JBVMJN2E | Yes | 3.22 |
| 14 | 54CD2R92FBTS | 54CD2R92FBTS | Yes | 2.37 |
| 15 | HRVRQSVIAT8I | HRVROSVIATSI | No | 9.77 |
| 16 | ZUF19O7WMHIN | ZUF1907WMHIN | No | 5.27 |
| 17 | 0YIAU1NZG42V | OYIAU1NZG42V | No | 3.45 |
| 18 | XTOBQKXN5OXH | XTOBQKXN5OXH | Yes | 9.58 |
| 19 | CNV7HL8Z97K5 | CNV7HL8Z97K5 | Yes | 2.45 |
| 20 | ERPV9BO8L6VL | ERP V9BO8L6VL | No | 21.85 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 10.08 |
| 2 | 60 | 60 | Yes | 5.76 |
| 3 | 10 | 10 | Yes | 8.26 |
| 4 | 73 | 73 | Yes | 5.23 |
| 5 | 793 | 793 | Yes | 3.57 |
| 6 | 26 | 26 | Yes | 17.02 |
| 7 | 6 | 6 | Yes | 6.93 |
| 8 | 36 | 36 | Yes | 5.32 |
| 9 | 3 | 3 | Yes | 2.64 |
| 10 | 4 | 4 | Yes | 4.08 |
| 11 | 4 | 4 | Yes | 8.58 |
| 12 | 20 | 20 | Yes | 13.71 |
| 13 | 7 | 7 | Yes | 3.17 |
| 14 | 19 | 19 | Yes | 2.84 |
| 15 | 44 | 44 | Yes | 8.21 |
| 16 | 28 | 28 | Yes | 9.48 |
| 17 | 1440 | 1440 | Yes | 8.75 |
| 18 | 9 | 9 | Yes | 6.85 |
| 19 | 60 | 60 | Yes | 7.52 |
| 20 | 9 | 9 | Yes | 8.51 |
