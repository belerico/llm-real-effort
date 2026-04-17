# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8600 | 30429 | 39029 | 11 | 9 | 24.71 | 494.41 |
| add_numbers | 4520 | 1789 | 6309 | 20 | 0 | 3.73 | 74.78 |
| counting_zeros | 7460 | 20933 | 28393 | 10 | 10 | 13.74 | 275.07 |
| task_decoding | 13900 | 8817 | 22717 | 18 | 2 | 7.80 | 156.17 |
| task_summation | 7820 | 14001 | 21821 | 20 | 0 | 9.91 | 198.45 |
| task_transcription | 4676 | 2787 | 7463 | 17 | 3 | 5.05 | 101.16 |
| task_sequences | 3780 | 7265 | 11045 | 20 | 0 | 5.99 | 119.85 |
| **TOTAL** | **50756** | **86021** | **136777** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 6 4 3 5 6 2 1 1 4 5 6 4 | 5 6 6 4 3 5 6 2 1 1 4 5 6 4 | Yes | 22.57 |
| 2 | 3 2 4 6 3 1 2 3 2 5 2 5 6 4 | 3 2 4 6 3 1 2 3 2 5 2 5 6 4 | Yes | 27.97 |
| 3 | 3 2 2 6 3 4 4 2 3 1 5 4 6 3 | 3 2 2 6 3 4 4 2 3 1 5 4 6 3 | Yes | 23.76 |
| 4 | 4 2 6 5 1 1 6 4 3 5 5 1 4 3 | 4 2 6 5 1 1 6 4 3 5 5 1 4 3 | Yes | 21.2 |
| 5 | 5 4 6 4 3 5 5 1 2 3 1 1 4 2 | 5 4 6 4 3 5 5 1 2 3 1 1 4 2 | Yes | 18.6 |
| 6 | 5 1 2 1 4 6 1 4 5 6 5 5 4 2 | 5 1 2 1 4 6 1 4 5 6 5 5 4 2 | Yes | 27.6 |
| 7 | 1 6 4 6 1 4 5 6 4 3 6 1 5 1 | 1 6 4 6 1 4 5 6 4 3 6 1 5 1 | Yes | 24.76 |
| 8 | 2 1 2 3 4 5 2 2 3 3 4 6 5 1 | 2 1 2 3 4 5 4 2 3 3 4 6 5 1 | No | 35.41 |
| 9 | 6 2 4 2 5 1 5 4 1 1 3 2 1 6 | 6 2 4 5 2 1 5 4 1 1 2 3 1 6 | No | 19.63 |
| 10 | 3 4 1 5 1 4 3 4 6 1 1 2 2 4 | 3 4 1 5 1 4 3 4 6 1 1 2 2 4 | Yes | 21.16 |
| 11 | 5 2 6 3 6 1 4 6 5 6 3 1 6 3 | 5 2 6 3 1 6 4 6 5 6 3 1 6 3 | No | 23.87 |
| 12 | 5 3 6 2 2 6 4 1 3 1 4 4 2 5 | 5 3 6 2 2 6 4 1 3 1 4 4 2 5 | Yes | 20.56 |
| 13 | 4 6 2 1 3 6 3 2 1 3 2 2 5 6 | 4 6 2 1 3 6 3 2 2 3 1 1 5 2 | No | 21.51 |
| 14 | 5 5 6 2 2 4 3 4 2 2 3 4 3 1 | 5 4 5 2 6 2 4 3 4 2 3 2 4 3 1 | No | 22.2 |
| 15 | 4 5 1 6 6 2 1 3 4 5 2 5 6 1 | 4 5 1 6 6 2 1 3 4 5 2 5 6 1 | Yes | 26.26 |
| 16 | 4 3 6 1 5 1 3 2 5 3 5 1 6 4 | 4 3 6 1 5 3 5 2 1 1 3 5 6 4 | No | 30.98 |
| 17 | 3 3 6 2 4 4 3 5 4 1 5 3 2 4 | 3 3 6 2 4 5 3 4 4 1 2 3 5 4 | No | 33.46 |
| 18 | 5 6 3 2 1 5 3 5 2 4 4 3 1 2 | 3 6 5 5 1 2 3 5 2 4 4 2 1 3 | No | 24.96 |
| 19 | 4 1 6 3 4 5 4 3 5 4 6 1 2 5 | 4 1 6 3 4 5 4 3 5 4 6 1 2 5 | Yes | 28.47 |
| 20 | 2 1 1 3 2 3 2 1 4 1 4 6 3 2 | 2 1 3 2 1 2 3 1 4 1 4 6 3 2 | No | 19.3 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1602 | 1602 | Yes | 4.79 |
| 2 | 2544 | 2544 | Yes | 2.8 |
| 3 | 815 | 815 | Yes | 3.06 |
| 4 | 1689 | 1689 | Yes | 3.92 |
| 5 | 1811 | 1811 | Yes | 3.77 |
| 6 | 1684 | 1684 | Yes | 5.34 |
| 7 | 1673 | 1673 | Yes | 4.36 |
| 8 | 1900 | 1900 | Yes | 3.59 |
| 9 | 1381 | 1381 | Yes | 3.33 |
| 10 | 1352 | 1352 | Yes | 4.18 |
| 11 | 1773 | 1773 | Yes | 3.27 |
| 12 | 1044 | 1044 | Yes | 4.64 |
| 13 | 2076 | 2076 | Yes | 3.72 |
| 14 | 1806 | 1806 | Yes | 3.96 |
| 15 | 850 | 850 | Yes | 2.56 |
| 16 | 1034 | 1034 | Yes | 3.18 |
| 17 | 1542 | 1542 | Yes | 2.99 |
| 18 | 774 | 774 | Yes | 2.88 |
| 19 | 2137 | 2137 | Yes | 3.24 |
| 20 | 1729 | 1729 | Yes | 5.11 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 70 | 69 | No | 15.3 |
| 2 | 47 | 47 | Yes | 13.91 |
| 3 | 36 | 36 | Yes | 10.57 |
| 4 | 65 | 63 | No | 14.27 |
| 5 | 60 | 58 | No | 13.52 |
| 6 | 63 | 62 | No | 16.05 |
| 7 | 52 | 51 | No | 12.97 |
| 8 | 47 | 47 | Yes | 12.41 |
| 9 | 48 | 47 | No | 10.73 |
| 10 | 41 | 41 | Yes | 13.03 |
| 11 | 36 | 36 | Yes | 10.99 |
| 12 | 55 | 52 | No | 13.99 |
| 13 | 37 | 37 | Yes | 10.71 |
| 14 | 53 | 50 | No | 15.72 |
| 15 | 62 | 61 | No | 14.72 |
| 16 | 40 | 40 | Yes | 23.83 |
| 17 | 61 | 58 | No | 14.29 |
| 18 | 56 | 56 | Yes | 13.94 |
| 19 | 67 | 67 | Yes | 10.43 |
| 20 | 51 | 51 | Yes | 13.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FMDCYPL | FMDCYPL | Yes | 5.11 |
| 2 | IUHFWBY | IUHFWBY | Yes | 8.45 |
| 3 | ZINDJQR | ZINDJQR | Yes | 5.58 |
| 4 | KLARJIQ | KLARJIQ | Yes | 8.47 |
| 5 | FCYLZMS | FCYLZMS | Yes | 7.13 |
| 6 | PKQMHXT | PKQMHXT | Yes | 6.47 |
| 7 | THSVPUL | THSVPUL | Yes | 9.16 |
| 8 | FSBNKVE | FSBNKVE | Yes | 6.33 |
| 9 | WGRSZNL | WGRSZNL | Yes | 9.41 |
| 10 | ARBLOYF | ARBLOYF | Yes | 5.87 |
| 11 | KAXBFTV | KAXBFTV | Yes | 8.77 |
| 12 | XDAGYHK | XDAGYHK | Yes | 7.6 |
| 13 | OJQCINF | OJQCINF | Yes | 7.26 |
| 14 | EHYNFKJ | EZYNFKJ | No | 9.58 |
| 15 | VQJXZGY | VQJXZGY | Yes | 5.9 |
| 16 | FJXYURM | FJXYURM | Yes | 7.32 |
| 17 | TVXOMFB | TVXOMFB | Yes | 8.31 |
| 18 | SGCVXYH | SGCVXYH | Yes | 9.1 |
| 19 | OKFRGTD | OKFRGDT | No | 11.75 |
| 20 | YRKXQBN | YRKXQBN | Yes | 8.4 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.6, 5.4] | 4.6 5.4 | Yes | 10.96 |
| 2 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.5 |
| 3 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.41 |
| 4 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.06 |
| 5 | [4.2, 5.8] | 5.8 4.2 | Yes | 8.23 |
| 6 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.98 |
| 7 | [3.0, 7.0] | 3.0 7.0 | Yes | 10.81 |
| 8 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.52 |
| 9 | [0.2, 9.8] | 0.2 9.8 | Yes | 10.39 |
| 10 | [1.9, 8.1] | 8.1 1.9 | Yes | 10.33 |
| 11 | [3.2, 6.8] | 6.8 3.2 | Yes | 10.8 |
| 12 | [2.7, 7.3] | 2.7 7.3 | Yes | 12.01 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.04 |
| 14 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.91 |
| 15 | [2.3, 7.7] | 7.7 2.3 | Yes | 11.85 |
| 16 | [1.5, 8.5] | 8.5 1.5 | Yes | 10.0 |
| 17 | [3.2, 6.8] | 3.2 6.8 | Yes | 11.25 |
| 18 | [1.0, 9.0] | 9.0 1.0 | Yes | 10.81 |
| 19 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.1 |
| 20 | [2.9, 7.1] | 7.1 2.9 | Yes | 11.33 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7XPNYHWEF7SF | 7XPNYHWEF7SF | Yes | 4.8 |
| 2 | DM60SDBOC3AP | DM60SDBOC3AP | Yes | 5.01 |
| 3 | 8LMX19UTVP5V | 8LMX19UTVP5V | Yes | 4.32 |
| 4 | KZDOH1RIP5TA | KZDOH1RIP5TA | Yes | 4.68 |
| 5 | MPF4787UFCDG | MPF4787UFCDG | Yes | 4.29 |
| 6 | HMUCKSJ4RH5Q | HMUCKSJ4RH5Q | Yes | 3.86 |
| 7 | KZAVZ67S6OXA | KZAVZ67S6OXA | Yes | 5.05 |
| 8 | PG5DFTHLOWW6 | PG5DFTHLOWW6 | Yes | 4.54 |
| 9 | L1FVNNTNXQIA | L1FVNNTNXQIA | Yes | 4.54 |
| 10 | 9RFTVLG18IXU | 9RFTVLG18IXU | Yes | 4.52 |
| 11 | EO9FOPOIHO5K | EO9FOPOIHO5K | Yes | 4.14 |
| 12 | OT26HFGUW5MN | OT28HFGUW5MN | No | 4.31 |
| 13 | LURLQ5E2QWI0 | LURLO5E2QWIO | No | 15.82 |
| 14 | HOEESI34HJFY | HOEESI34HJFY | Yes | 4.32 |
| 15 | X75ECR3N19F8 | X75ECR3N19F8 | Yes | 4.49 |
| 16 | 2PNZTYJO5OUZ | 2PNZTYJO5OUZ | Yes | 3.7 |
| 17 | YOHHPPYC6ZLZ | YOHHPPYC8ZLZ | No | 5.48 |
| 18 | O3F35YMB03V0 | O3F35YMB03V0 | Yes | 4.42 |
| 19 | HRHS4J4T3DU9 | HRHS4J4T3DU9 | Yes | 4.07 |
| 20 | NNPKLPVB0FIP | NNPKLPVB0FIP | Yes | 4.68 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 6.77 |
| 2 | 793 | 793 | Yes | 5.08 |
| 3 | 7680 | 7680 | Yes | 7.25 |
| 4 | 10 | 10 | Yes | 6.46 |
| 5 | 9 | 9 | Yes | 6.91 |
| 6 | 7 | 7 | Yes | 4.86 |
| 7 | 1 | 1 | Yes | 4.78 |
| 8 | 6 | 6 | Yes | 6.36 |
| 9 | 60 | 60 | Yes | 5.64 |
| 10 | 4 | 4 | Yes | 4.49 |
| 11 | 3 | 3 | Yes | 9.24 |
| 12 | 65 | 65 | Yes | 6.83 |
| 13 | 243 | 243 | Yes | 4.75 |
| 14 | 44 | 44 | Yes | 6.65 |
| 15 | 3 | 3 | Yes | 9.03 |
| 16 | 60 | 60 | Yes | 4.91 |
| 17 | 16 | 16 | Yes | 5.44 |
| 18 | 31 | 31 | Yes | 4.19 |
| 19 | 63 | 63 | Yes | 5.25 |
| 20 | 73 | 73 | Yes | 4.97 |
