# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-19 10:56:13

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
| sudoku_game | 7460 | 40960 | 48420 | 0 | 20 | 70.24 | 1404.95 |
| add_numbers | 6480 | 5106 | 11586 | 20 | 0 | 8.70 | 174.07 |
| counting_zeros | 5559 | 34816 | 40375 | 0 | 20 | 95.92 | 1918.78 |
| task_decoding | 9800 | 16614 | 26414 | 20 | 0 | 13.73 | 274.78 |
| task_summation | 6800 | 22559 | 29359 | 20 | 0 | 17.57 | 351.88 |
| task_transcription | 6560 | 15549 | 22109 | 16 | 4 | 14.23 | 284.76 |
| task_sequences | 2421 | 11112 | 13533 | 18 | 2 | 13.49 | 269.75 |
| **TOTAL** | **45080** | **146716** | **191796** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 6 5 1 5 1 5 5 3 6 4 3 1 |  | No | 69.22 |
| 2 | 4 1 2 3 5 4 3 2 2 1 5 4 5 3 |  | No | 75.6 |
| 3 | 2 4 6 4 5 2 6 1 3 6 5 1 2 5 |  | No | 70.41 |
| 4 | 5 2 3 3 1 5 3 2 5 5 2 6 3 2 |  | No | 78.06 |
| 5 | 5 2 5 1 4 2 1 3 2 2 3 1 5 6 |  | No | 66.69 |
| 6 | 2 4 5 6 3 1 1 1 4 6 2 2 4 1 |  | No | 64.76 |
| 7 | 4 3 6 4 5 4 1 3 6 3 4 2 4 3 |  | No | 73.83 |
| 8 | 5 4 4 5 6 2 5 1 6 4 5 5 6 4 |  | No | 55.08 |
| 9 | 5 3 5 4 1 5 2 3 6 3 4 2 6 4 |  | No | 65.37 |
| 10 | 5 4 1 3 4 6 3 1 5 4 1 5 3 2 |  | No | 68.21 |
| 11 | 1 4 6 6 1 1 3 5 3 6 1 3 1 4 |  | No | 69.43 |
| 12 | 1 3 6 3 6 2 3 4 5 1 3 6 2 4 |  | No | 70.23 |
| 13 | 5 4 1 3 3 1 2 1 1 5 6 2 3 5 |  | No | 78.78 |
| 14 | 6 2 5 6 2 1 3 5 1 3 6 3 5 1 |  | No | 68.88 |
| 15 | 3 4 2 4 2 3 2 5 2 1 1 3 2 5 |  | No | 69.72 |
| 16 | 4 6 1 5 5 6 2 2 6 4 6 3 1 2 |  | No | 64.36 |
| 17 | 6 1 5 4 4 3 1 6 4 3 4 2 5 4 |  | No | 89.59 |
| 18 | 5 6 1 5 2 3 4 6 4 5 4 2 1 3 |  | No | 60.01 |
| 19 | 4 2 1 2 5 6 1 5 3 2 1 2 4 6 |  | No | 68.66 |
| 20 | 4 6 5 6 1 3 3 2 6 1 4 2 3 5 |  | No | 77.85 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1218 | 1218 | Yes | 8.8 |
| 2 | 1298 | 1298 | Yes | 13.52 |
| 3 | 2683 | 2683 | Yes | 8.96 |
| 4 | 1527 | 1527 | Yes | 6.63 |
| 5 | 1646 | 1646 | Yes | 10.7 |
| 6 | 1571 | 1571 | Yes | 11.52 |
| 7 | 1026 | 1026 | Yes | 6.48 |
| 8 | 1284 | 1284 | Yes | 8.39 |
| 9 | 2235 | 2235 | Yes | 6.02 |
| 10 | 1332 | 1332 | Yes | 10.45 |
| 11 | 1306 | 1306 | Yes | 6.3 |
| 12 | 1837 | 1837 | Yes | 9.27 |
| 13 | 1038 | 1038 | Yes | 6.03 |
| 14 | 2346 | 2346 | Yes | 9.2 |
| 15 | 1504 | 1504 | Yes | 8.45 |
| 16 | 1103 | 1103 | Yes | 7.62 |
| 17 | 1735 | 1735 | Yes | 9.16 |
| 18 | 2290 | 2290 | Yes | 7.17 |
| 19 | 1795 | 1795 | Yes | 7.01 |
| 20 | 1635 | 1635 | Yes | 12.29 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 |  | No | 95.28 |
| 2 | 70 |  | No | 113.29 |
| 3 | 63 |  | No | 97.64 |
| 4 | 36 | TIMEOUT | No | 120.02 |
| 5 | 39 |  | No | 96.98 |
| 6 | 64 |  | No | 112.26 |
| 7 | 58 |  | No | 108.24 |
| 8 | 50 | TIMEOUT | No | 120.02 |
| 9 | 39 |  | No | 75.58 |
| 10 | 71 |  | No | 98.98 |
| 11 | 65 |  | No | 108.37 |
| 12 | 40 | TIMEOUT | No | 120.02 |
| 13 | 63 |  | No | 81.88 |
| 14 | 53 |  | No | 104.64 |
| 15 | 48 |  | No | 85.84 |
| 16 | 58 |  | No | 78.54 |
| 17 | 40 |  | No | 85.57 |
| 18 | 41 |  | No | 78.99 |
| 19 | 36 |  | No | 89.94 |
| 20 | 41 |  | No | 46.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KZBVQTN | KZBVQTN | Yes | 10.64 |
| 2 | IZFRKBL | IZFRKBL | Yes | 14.24 |
| 3 | KRSVMZA | KRSVMZA | Yes | 11.09 |
| 4 | UTNZHVX | UTNZHVX | Yes | 7.05 |
| 5 | UWGYKXD | UWGYKXD | Yes | 13.47 |
| 6 | LHRSBCD | LHRSBCD | Yes | 10.69 |
| 7 | GAPVORT | GAPVORT | Yes | 26.78 |
| 8 | ISUGZXC | ISUGZXC | Yes | 17.6 |
| 9 | ECIPZGA | ECIPZGA | Yes | 13.07 |
| 10 | PCVMFHB | PCVMFHB | Yes | 21.45 |
| 11 | WKDMPQO | WKDMPQO | Yes | 15.3 |
| 12 | WHCKGZM | WHCKGZM | Yes | 10.03 |
| 13 | AEOJGMW | AEOJGMW | Yes | 17.7 |
| 14 | DSYFMPQ | DSYFMPQ | Yes | 14.64 |
| 15 | SYRXLCI | SYRXLCI | Yes | 12.93 |
| 16 | VOPWJAC | VOPWJAC | Yes | 9.8 |
| 17 | WJSNFGI | WJSNFGI | Yes | 11.21 |
| 18 | DQNWMTL | DQNWMTL | Yes | 12.02 |
| 19 | XNAJBVD | XNAJBVD | Yes | 9.62 |
| 20 | AJMORUN | AJMORUN | Yes | 15.29 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.7, 8.3] | 8.3 1.7 | Yes | 17.26 |
| 2 | [3.7, 6.3] | 3.7 6.3 | Yes | 17.23 |
| 3 | [2.3, 7.7] | 2.3 7.7 | Yes | 14.92 |
| 4 | [2.3, 7.7] | 2.3 7.7 | Yes | 20.27 |
| 5 | [2.2, 7.8] | 7.8 2.2 | Yes | 13.0 |
| 6 | [1.4, 8.6] | 8.6 1.4 | Yes | 17.28 |
| 7 | [4.6, 5.4] | 5.4 4.6 | Yes | 16.2 |
| 8 | [3.3, 6.7] | 3.3 6.7 | Yes | 25.56 |
| 9 | [3.0, 7.0] | 3.0 7.0 | Yes | 22.41 |
| 10 | [2.3, 7.7] | 7.7 2.3 | Yes | 22.1 |
| 11 | [4.8, 5.2] | 4.8 5.2 | Yes | 12.34 |
| 12 | [4.9, 5.1] | 5.1 4.9 | Yes | 15.93 |
| 13 | [4.0, 6.0] | 6.0 4.0 | Yes | 15.74 |
| 14 | [4.5, 5.5] | 5.5 4.5 | Yes | 23.06 |
| 15 | [0.6, 9.4] | 0.6 9.4 | Yes | 17.46 |
| 16 | [3.4, 6.6] | 6.6 3.4 | Yes | 11.0 |
| 17 | [1.2, 8.8] | 1.2 8.8 | Yes | 15.46 |
| 18 | [0.7, 9.3] | 9.3 0.7 | Yes | 23.74 |
| 19 | [4.9, 5.1] | 5.1 4.9 | Yes | 12.89 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 17.55 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TNIMFU8H335M | TNIMFU8H335M | Yes | 2.67 |
| 2 | 04J20MDR13FB | 04J20MDR13FB | Yes | 22.19 |
| 3 | N0IK33HHKOR7 | N0IK33HHK0R7 | No | 24.66 |
| 4 | 8JPQRFBU7S4Z | &JPQRFBU7S4Z | No | 22.31 |
| 5 | R8Z68A4256P5 | R8Z68A4256P5 | Yes | 7.26 |
| 6 | RX06RHGANBWX | RX06RHGANBWX | Yes | 11.1 |
| 7 | SFDTTDYLYB41 | SFDTTDYLYB41 | Yes | 12.18 |
| 8 | T2OTMQD8C6WD | T2OTMQD8C6WD | Yes | 4.77 |
| 9 | BTDJK26CO4T7 | BTDJK26CO4T7 | Yes | 18.69 |
| 10 | 2GNOPK3117LD | 2GNOPK3117LD | Yes | 3.57 |
| 11 | C7DS3EB0DG16 | C7DS3EB0DG16 | Yes | 11.47 |
| 12 | 1AQ7XVNNX7RM | 1AQ7XVNNX7RM | Yes | 48.62 |
| 13 | FFK9BNDTCR1J | FFK9BNDTCR1J | Yes | 9.19 |
| 14 | RK99RLOLNX14 | RK99RLOLNX14 | Yes | 9.3 |
| 15 | RDAZO02ZK9GU | RDAZO02ZK9GU | Yes | 8.08 |
| 16 | UW0KK7EG4AUR | UW0KK7EG4AUR | Yes | 14.34 |
| 17 | FQ83VDFVYKBB | FQ83VDFVYKBB | Yes | 8.98 |
| 18 | E8JN603Z5LQT | E8JN603Z5LOT | No | 11.92 |
| 19 | R0RYLGUR4BM8 | R0RYLGUR4BM8 | Yes | 17.78 |
| 20 | N0RHNRQXLJJT | NORHNROXLJJT | No | 15.56 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 5.04 |
| 2 | 65 | 65 | Yes | 6.04 |
| 3 | 16 | 16 | Yes | 7.62 |
| 4 | 9 | 9 | Yes | 8.05 |
| 5 | 19 | 19 | Yes | 7.68 |
| 6 | 9 | 9 | Yes | 7.59 |
| 7 | 3 | 3 | Yes | 9.65 |
| 8 | 67 | 67 | Yes | 4.18 |
| 9 | 4096 |  | No | 60.51 |
| 10 | 7680 | 7680 | Yes | 13.84 |
| 11 | 44 | 44 | Yes | 5.61 |
| 12 | 64 | 64 | Yes | 10.85 |
| 13 | 20 |  | No | 58.81 |
| 14 | 23 | 23 | Yes | 13.13 |
| 15 | 48 | 48 | Yes | 8.82 |
| 16 | 1 | 1 | Yes | 15.78 |
| 17 | 793 | 793 | Yes | 4.91 |
| 18 | 31 | 31 | Yes | 6.34 |
| 19 | 60 | 60 | Yes | 9.93 |
| 20 | 4 | 4 | Yes | 5.38 |
