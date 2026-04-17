# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 9941 | 39109 | 49050 | 0 | 20 | 75.48 | 1509.87 |
| add_numbers | 7600 | 2969 | 10569 | 20 | 0 | 4.69 | 93.96 |
| counting_zeros | 7660 | 39268 | 46928 | 0 | 20 | 49.22 | 984.65 |
| task_decoding | 11120 | 8958 | 20078 | 19 | 1 | 11.60 | 232.24 |
| task_summation | 7920 | 14345 | 22265 | 19 | 1 | 13.86 | 277.32 |
| task_transcription | 7680 | 9597 | 17277 | 19 | 1 | 10.66 | 213.31 |
| task_sequences | 3241 | 9521 | 12762 | 18 | 2 | 12.69 | 253.82 |
| **TOTAL** | **55162** | **123767** | **178929** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 6 1 4 3 1 1 4 5 6 4 2 2 |  | No | 78.05 |
| 2 | 4 3 2 1 5 1 1 5 6 1 2 6 2 4 |  | No | 86.27 |
| 3 | 1 3 2 1 5 4 3 1 2 5 2 6 3 5 |  | No | 68.93 |
| 4 | 3 2 4 2 3 6 2 1 5 5 6 1 4 5 |  | No | 73.99 |
| 5 | 2 1 5 5 6 2 3 5 4 4 6 5 4 5 |  | No | 71.89 |
| 6 | 4 5 3 6 1 4 1 4 2 6 3 4 1 4 | Answer: | No | 41.35 |
| 7 | 5 4 3 4 4 2 4 5 1 6 1 6 4 4 |  | No | 66.23 |
| 8 | 3 5 1 4 6 3 5 3 4 1 2 5 4 5 |  | No | 50.71 |
| 9 | 3 6 3 2 2 5 6 2 6 3 3 3 4 1 |  | No | 55.34 |
| 10 | 3 6 1 4 6 2 5 3 4 4 2 5 3 6 |  | No | 85.1 |
| 11 | 2 4 5 1 3 6 3 1 5 1 6 5 2 2 |  | No | 71.24 |
| 12 | 3 6 4 2 2 5 6 3 1 2 1 3 2 3 |  | No | 117.47 |
| 13 | 2 6 1 4 3 1 5 3 6 5 5 1 1 4 |  | No | 63.47 |
| 14 | 3 5 1 1 4 3 4 6 6 4 1 2 3 5 |  | No | 92.57 |
| 15 | 5 6 5 4 3 6 2 6 4 2 6 5 3 5 |  | No | 80.45 |
| 16 | 3 1 2 1 2 2 1 3 3 1 5 3 5 1 |  | No | 75.69 |
| 17 | 1 3 4 2 4 5 1 5 4 4 3 5 1 4 |  | No | 107.31 |
| 18 | 3 1 2 6 2 4 3 5 4 6 5 5 6 3 |  | No | 70.93 |
| 19 | 3 2 6 6 5 1 2 3 1 5 1 6 2 5 |  | No | 77.09 |
| 20 | 2 5 6 1 4 2 5 3 5 2 1 4 3 2 |  | No | 75.61 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1836 | 1836 | Yes | 4.66 |
| 2 | 1554 | 1554 | Yes | 7.49 |
| 3 | 1065 | 1065 | Yes | 3.8 |
| 4 | 1100 | 1100 | Yes | 4.44 |
| 5 | 488 | 488 | Yes | 5.18 |
| 6 | 1471 | 1471 | Yes | 4.46 |
| 7 | 1495 | 1495 | Yes | 3.8 |
| 8 | 2043 | 2043 | Yes | 6.5 |
| 9 | 1262 | 1262 | Yes | 3.15 |
| 10 | 1461 | 1461 | Yes | 8.18 |
| 11 | 1960 | 1960 | Yes | 3.53 |
| 12 | 2053 | 2053 | Yes | 4.52 |
| 13 | 1746 | 1746 | Yes | 3.8 |
| 14 | 1498 | 1498 | Yes | 4.54 |
| 15 | 1072 | 1072 | Yes | 5.33 |
| 16 | 1014 | 1014 | Yes | 4.63 |
| 17 | 1701 | 1701 | Yes | 4.36 |
| 18 | 1643 | 1643 | Yes | 4.68 |
| 19 | 2460 | 2460 | Yes | 2.8 |
| 20 | 1922 | 1922 | Yes | 3.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 |  | No | 66.47 |
| 2 | 40 |  | No | 52.57 |
| 3 | 58 |  | No | 61.65 |
| 4 | 60 |  | No | 64.03 |
| 5 | 43 |  | No | 53.18 |
| 6 | 46 |  | No | 29.72 |
| 7 | 71 |  | No | 64.69 |
| 8 | 72 |  | No | 58.57 |
| 9 | 43 | 67 | No | 25.91 |
| 10 | 41 |  | No | 74.61 |
| 11 | 44 |  | No | 46.01 |
| 12 | 50 |  | No | 80.92 |
| 13 | 56 |  | No | 49.03 |
| 14 | 56 |  | No | 39.22 |
| 15 | 37 |  | No | 41.84 |
| 16 | 64 | 67 | No | 21.49 |
| 17 | 41 |  | No | 53.23 |
| 18 | 59 |  | No | 33.24 |
| 19 | 73 |  | No | 36.73 |
| 20 | 69 |  | No | 31.23 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QZTLGSE | QZTLGSE | Yes | 5.62 |
| 2 | UNYOSVX | UNYOSVX | Yes | 7.25 |
| 3 | SDAMETU | SDAMETU | Yes | 7.1 |
| 4 | VGSDYEM | VGSDYEM | Yes | 8.19 |
| 5 | IPVOHES |  | No | 55.21 |
| 6 | MSBFDOE | MSBFDOE | Yes | 9.04 |
| 7 | SHLCUWZ | SHLCUWZ | Yes | 6.33 |
| 8 | RGYWQCB | RGYWQCB | Yes | 7.56 |
| 9 | VNGAHZB | VNGAHZB | Yes | 14.39 |
| 10 | ZCEDLYJ | ZCEDLYJ | Yes | 15.88 |
| 11 | SPRLBHU | SPRLBHU | Yes | 13.43 |
| 12 | RBFKTSQ | RBFKTSQ | Yes | 4.49 |
| 13 | IXSOTLR | IXSOTLR | Yes | 11.97 |
| 14 | GQWSMBL | GQWSMBL | Yes | 10.96 |
| 15 | IGAXZTN | IGAXZTN | Yes | 15.87 |
| 16 | VFYXMTS | VFYXMTS | Yes | 6.35 |
| 17 | WEFVYJD | WEFVYJD | Yes | 5.5 |
| 18 | QBAXJSN | QBAXJSN | Yes | 7.49 |
| 19 | GABUDCQ | GABUDCQ | Yes | 7.83 |
| 20 | ZWTLODS | ZWTLODS | Yes | 11.54 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 6.0 4.0 | Yes | 10.77 |
| 2 | [2.8, 7.2] | 2.8 7.2 | Yes | 14.25 |
| 3 | [0.8, 9.2] | 0.8 9.2 | Yes | 10.49 |
| 4 | [3.0, 7.0] | 3.0 7.0 | Yes | 19.89 |
| 5 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.18 |
| 6 | [2.2, 7.8] | 7.8 2.2 | Yes | 8.77 |
| 7 | [4.8, 5.2] | 4.8 5.2 | Yes | 12.66 |
| 8 | [2.3, 7.7] | 2.3 7.7 | Yes | 9.05 |
| 9 | [3.6, 6.4] | 3.6 6.4 | Yes | 11.59 |
| 10 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.73 |
| 11 | [4.9, 5.1] | 4.9 5.1 | Yes | 8.97 |
| 12 | [0.6, 9.4] | 0.6 9.4 | Yes | 11.36 |
| 13 | [4.3, 5.7] | 4.3 5.7 | Yes | 13.35 |
| 14 | [0.9, 9.1] | 0.9 9.1 | Yes | 15.82 |
| 15 | [0.3, 9.7] | 0.3 9.7 | Yes | 10.77 |
| 16 | [1.5, 8.5] |  | No | 46.77 |
| 17 | [4.4, 5.6] | 5.6 4.4 | Yes | 10.88 |
| 18 | [2.4, 7.6] | 7.6 2.4 | Yes | 14.95 |
| 19 | [0.4, 9.6] | 0.4 9.6 | Yes | 13.18 |
| 20 | [2.3, 7.7] | 2.3 7.7 | Yes | 13.73 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RUYSRH1G5XRH | RUYSRH1G5XRH | Yes | 26.39 |
| 2 | W2WK76B575LR | W2WK76B575LR | Yes | 5.29 |
| 3 | CG6RSEJYLSFB | CG6RSEJYLSFB | Yes | 8.63 |
| 4 | TG1XZKEBFZVA | TG1XZKEBFZVA | Yes | 8.94 |
| 5 | EGEK5MAPIT9B | EGEK5MAPIT9B | Yes | 16.13 |
| 6 | 683KTJ3I1CZA | 683KTJ3I1CZA | Yes | 33.33 |
| 7 | QKNTX3QSSN7N | QKNTX3QSSN7N | Yes | 13.54 |
| 8 | 73J6T86N7T7D | 73J6T86N7T7D | Yes | 9.75 |
| 9 | TWWKIZH764GU | TWWKIZH764GU | Yes | 5.97 |
| 10 | DP5WN1X0WOTT | DP5WN1X0WOTT | Yes | 14.15 |
| 11 | N12QSL1II7XO | N12QSL1117XO | No | 10.48 |
| 12 | GJN55ERRJ9GP | GJN55ERRJ9GP | Yes | 5.37 |
| 13 | D6IN43BX8UPE | D6IN43BX8UPE | Yes | 7.82 |
| 14 | 24BKJ8KNGMAG | 24BKJ8KNGMAG | Yes | 4.98 |
| 15 | ISNXN296XZY4 | ISNXN296XZY4 | Yes | 4.84 |
| 16 | FR0199V73L12 | FR0199V73L12 | Yes | 3.82 |
| 17 | VUO23WAMMARQ | VUO23WAMMARQ | Yes | 14.93 |
| 18 | YPTYIC7DAVNZ | YPTYIC7DAVNZ | Yes | 9.14 |
| 19 | AIWQ11IAWDY3 | AIWQ11IAWDY3 | Yes | 3.52 |
| 20 | AVGNIPC13VD8 | AVGNIPC13VD8 | Yes | 6.18 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 5.97 |
| 2 | 60 | 60 | Yes | 11.76 |
| 3 | 4 | 4 | Yes | 11.39 |
| 4 | 4096 |  | No | 45.72 |
| 5 | 64 | 64 | Yes | 9.96 |
| 6 | 4 | 4 | Yes | 13.48 |
| 7 | 9 | 9 | Yes | 6.08 |
| 8 | 23 | 23 | Yes | 8.49 |
| 9 | 19 | 19 | Yes | 9.47 |
| 10 | 198 | 198 | Yes | 9.06 |
| 11 | 7 | 7 | Yes | 10.32 |
| 12 | 63 | 63 | Yes | 7.23 |
| 13 | 67 | 67 | Yes | 7.14 |
| 14 | 65 | 65 | Yes | 8.95 |
| 15 | 5 | 2 | No | 13.59 |
| 16 | 31 | 31 | Yes | 6.64 |
| 17 | 6 | 6 | Yes | 3.84 |
| 18 | 28 | 28 | Yes | 15.24 |
| 19 | 26 | 26 | Yes | 34.67 |
| 20 | 39 | 39 | Yes | 14.8 |
