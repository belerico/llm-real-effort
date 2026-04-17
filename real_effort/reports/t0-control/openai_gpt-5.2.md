# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-19 10:09:31

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
| sudoku_game | 6720 | 23205 | 29925 | 17 | 3 | 21.82 | 436.62 |
| add_numbers | 3300 | 895 | 4195 | 20 | 0 | 2.98 | 59.72 |
| counting_zeros | 5720 | 37224 | 42944 | 7 | 13 | 40.53 | 810.99 |
| task_decoding | 11460 | 3332 | 14792 | 20 | 0 | 6.26 | 125.37 |
| task_summation | 6660 | 5728 | 12388 | 20 | 0 | 6.69 | 134.07 |
| task_transcription | 3111 | 1906 | 5017 | 13 | 7 | 4.15 | 83.15 |
| task_sequences | 2420 | 5852 | 8272 | 18 | 2 | 11.36 | 227.26 |
| **TOTAL** | **39391** | **78142** | **117533** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 3 2 2 2 3 5 1 4 3 6 2 1 3 | 5 3 2 2 2 3 5 1 4 3 6 2 1 3 | Yes | 16.57 |
| 2 | 1 4 6 6 3 2 5 4 6 2 6 1 3 6 | 1 4 6 6 3 2 5 4 6 2 6 1 3 6 | Yes | 12.7 |
| 3 | 2 3 1 3 2 4 5 5 4 4 3 5 1 2 |  | No | 43.79 |
| 4 | 5 6 1 4 5 2 3 1 3 4 4 1 5 3 |  | No | 53.54 |
| 5 | 2 5 4 1 6 2 6 5 6 5 1 2 3 5 | 2 5 4 1 6 2 6 5 6 5 1 2 3 5 | Yes | 18.76 |
| 6 | 4 3 2 5 1 6 2 3 4 5 6 4 5 1 | 4 3 2 5 1 6 2 3 4 5 6 4 5 1 | Yes | 22.49 |
| 7 | 4 6 3 3 6 4 5 2 6 4 4 1 4 1 | 4 6 3 3 6 4 5 2 6 4 4 1 4 1 | Yes | 15.73 |
| 8 | 3 6 1 5 4 5 1 5 2 6 4 2 3 5 | 3 6 1 5 4 5 1 5 2 6 4 2 3 5 | Yes | 23.69 |
| 9 | 6 5 5 2 3 6 1 3 4 1 6 3 5 5 | 6 5 5 2 3 6 1 3 4 1 6 3 5 5 | Yes | 14.13 |
| 10 | 2 1 3 2 6 2 1 6 3 4 5 4 2 1 | 2 1 3 2 6 2 1 6 3 4 5 4 2 1 | Yes | 17.16 |
| 11 | 5 4 4 5 6 4 2 6 4 5 1 4 2 3 | 5 4 4 5 6 4 2 6 4 5 1 4 2 3 | Yes | 15.15 |
| 12 | 3 5 4 4 1 3 6 5 6 4 3 2 2 5 | 3 5 4 4 1 3 6 5 6 4 3 2 2 5 | Yes | 20.31 |
| 13 | 2 3 4 1 2 5 5 3 1 2 2 4 2 5 |  | No | 53.9 |
| 14 | 3 1 2 3 5 1 4 4 5 3 2 5 6 2 | 3 1 2 3 5 1 4 4 5 3 2 5 6 2 | Yes | 20.16 |
| 15 | 5 5 4 1 4 6 3 4 6 1 5 6 4 2 | 5 5 4 1 4 6 3 4 6 1 5 6 4 2 | Yes | 10.65 |
| 16 | 5 4 1 3 4 4 6 6 5 3 2 6 1 3 | 5 4 1 3 4 4 6 6 5 3 2 6 1 3 | Yes | 17.11 |
| 17 | 3 4 5 1 3 3 5 1 6 3 5 3 4 3 | 3 4 5 1 3 3 5 1 6 3 5 3 4 3 | Yes | 13.74 |
| 18 | 3 6 2 4 4 3 1 1 3 6 4 3 6 4 | 3 6 2 4 4 3 1 1 3 6 4 3 6 4 | Yes | 15.42 |
| 19 | 5 2 4 4 1 6 4 1 5 6 2 5 3 4 | 5 2 4 4 1 6 4 1 5 6 2 5 3 4 | Yes | 16.86 |
| 20 | 5 6 1 4 4 1 3 1 2 4 3 5 6 4 | 5 6 1 4 4 1 3 1 2 4 3 5 6 4 | Yes | 14.56 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1967 | 1967 | Yes | 2.44 |
| 2 | 1845 | 1845 | Yes | 2.93 |
| 3 | 799 | 799 | Yes | 2.54 |
| 4 | 2213 | 2213 | Yes | 3.06 |
| 5 | 1314 | 1314 | Yes | 3.06 |
| 6 | 2351 | 2351 | Yes | 2.91 |
| 7 | 1368 | 1368 | Yes | 2.89 |
| 8 | 1796 | 1796 | Yes | 2.38 |
| 9 | 1702 | 1702 | Yes | 3.68 |
| 10 | 1752 | 1752 | Yes | 2.94 |
| 11 | 1023 | 1023 | Yes | 3.02 |
| 12 | 1635 | 1635 | Yes | 3.28 |
| 13 | 1931 | 1931 | Yes | 2.54 |
| 14 | 1482 | 1482 | Yes | 2.86 |
| 15 | 2158 | 2158 | Yes | 2.86 |
| 16 | 1780 | 1780 | Yes | 3.29 |
| 17 | 1794 | 1794 | Yes | 3.34 |
| 18 | 2011 | 2011 | Yes | 3.54 |
| 19 | 1356 | 1356 | Yes | 2.85 |
| 20 | 2056 | 2056 | Yes | 3.21 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 66 |  | No | 36.59 |
| 2 | 62 |  | No | 55.79 |
| 3 | 59 | 59 | Yes | 21.59 |
| 4 | 47 |  | No | 37.14 |
| 5 | 60 |  | No | 49.05 |
| 6 | 42 |  | No | 70.66 |
| 7 | 51 |  | No | 53.22 |
| 8 | 54 |  | No | 66.53 |
| 9 | 60 | 60 | Yes | 22.54 |
| 10 | 54 | 54 | Yes | 22.72 |
| 11 | 70 |  | No | 49.68 |
| 12 | 36 |  | No | 57.08 |
| 13 | 48 | 48 | Yes | 27.49 |
| 14 | 46 | 46 | Yes | 14.99 |
| 15 | 73 | 74 | No | 20.25 |
| 16 | 48 |  | No | 48.84 |
| 17 | 50 |  | No | 57.64 |
| 18 | 57 |  | No | 50.78 |
| 19 | 67 | 67 | Yes | 22.67 |
| 20 | 59 | 59 | Yes | 25.44 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GPKRVYQ | GPKRVYQ | Yes | 5.77 |
| 2 | ACWSFNT | ACWSFNT | Yes | 4.47 |
| 3 | YXCEDVK | YXCEDVK | Yes | 5.75 |
| 4 | EIPVDKH | EIPVDKH | Yes | 5.57 |
| 5 | DJANZBE | DJANZBE | Yes | 6.74 |
| 6 | HMXOVIG | HMXOVIG | Yes | 7.72 |
| 7 | CWJMTAL | CWJMTAL | Yes | 5.42 |
| 8 | GZLCRHV | GZLCRHV | Yes | 5.84 |
| 9 | PXZAVDT | PXZAVDT | Yes | 7.18 |
| 10 | MIFTNSB | MIFTNSB | Yes | 7.1 |
| 11 | YJQOEHB | YJQOEHB | Yes | 8.13 |
| 12 | UBJXCDF | UBJXCDF | Yes | 7.37 |
| 13 | AXPDKYJ | AXPDKYJ | Yes | 7.62 |
| 14 | MPSCONA | MPSCONA | Yes | 5.7 |
| 15 | QBJTUXI | QBJTUXI | Yes | 5.63 |
| 16 | BMRPALZ | BMRPALZ | Yes | 5.34 |
| 17 | TCXQHON | TCXQHON | Yes | 6.08 |
| 18 | BWMLUIO | BWMLUIO | Yes | 5.14 |
| 19 | VSFBJXW | VSFBJXW | Yes | 5.9 |
| 20 | MBNTVDC | MBNTVDC | Yes | 6.69 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.4, 8.6] | 1.4 8.6 | Yes | 5.82 |
| 2 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.42 |
| 3 | [2.2, 7.8] | 7.8 2.2 | Yes | 7.16 |
| 4 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.73 |
| 5 | [1.9, 8.1] | 8.1 1.9 | Yes | 6.0 |
| 6 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.93 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.1 |
| 8 | [0.4, 9.6] | 0.4 9.6 | Yes | 6.16 |
| 9 | [0.9, 9.1] | 0.9 9.1 | Yes | 7.39 |
| 10 | [4.7, 5.3] | 4.7 5.3 | Yes | 7.31 |
| 11 | [0.3, 9.7] | 9.7 0.3 | Yes | 7.05 |
| 12 | [5.0, 5.0] | 5.0 5.0 | Yes | 5.67 |
| 13 | [4.7, 5.3] | 4.7 5.3 | Yes | 6.62 |
| 14 | [1.7, 8.3] | 8.3 1.7 | Yes | 8.52 |
| 15 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.48 |
| 16 | [2.9, 7.1] | 7.1 2.9 | Yes | 8.04 |
| 17 | [1.1, 8.9] | 8.9 1.1 | Yes | 4.71 |
| 18 | [1.1, 8.9] | 1.1 8.9 | Yes | 7.75 |
| 19 | [2.7, 7.3] | 2.7 7.3 | Yes | 7.34 |
| 20 | [1.5, 8.5] | 1.5 8.5 | Yes | 5.68 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 66VZ94RO4ZXU | 66VZ94R04ZXU | No | 5.16 |
| 2 | OPCV3XT5U4G1 | OPCV3XT5U4G1 | Yes | 4.23 |
| 3 | 55NR4ET21Z8B | 55NR4ET21Z8B | Yes | 4.68 |
| 4 | 561K5YB8QPFF | 561K5YB8QPFF | Yes | 3.29 |
| 5 | 84P0O0JJFH29 | 84P000JJFH29 | No | 5.07 |
| 6 | D9NRLSF8WT5U | D9NRLSF8WT5U | Yes | 2.41 |
| 7 | 7GO4QUB3JAFW | 7G04QUB3JAFW | No | 2.42 |
| 8 | SLY530X8LPM8 | SLY530X8LPM8 | Yes | 3.9 |
| 9 | DDQN786U7AW5 | DDQN786U7AW5 | Yes | 3.68 |
| 10 | QKCBLX09XAXQ | I can’t help with transcribing distorted text from a CAPTCHA or similar verification image. | No | 3.39 |
| 11 | NSI6GST359OI | NSI6GST3590I | No | 8.27 |
| 12 | 2DRQJ7JI4ILC | 2DRQJ7JI4ILC | Yes | 3.57 |
| 13 | 8VD3AZ7JKXRI | 8VD3AZ7JKXR1 | No | 3.87 |
| 14 | 95DS4C31NBZ0 | 95DS4C31NBZ0 | Yes | 2.17 |
| 15 | J2HPB3JYWLY5 | J2HPB3JYWLY5 | Yes | 5.02 |
| 16 | LXY6DF20SMT8 | LXY6DF20SMT8 | Yes | 6.59 |
| 17 | GX1ZZIF60TAR | GX1ZZIF60TAR | Yes | 4.08 |
| 18 | IBDWZIDGXS0Z | IBDWZIDGXSOZ | No | 2.8 |
| 19 | CCS0GR24EQ9E | CCS0GR24EQ9E | Yes | 3.58 |
| 20 | BGUS02MALGS8 | BGUS02MALGS8 | Yes | 4.84 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 19 | 19 | Yes | 4.95 |
| 2 | 1 | 1 | Yes | 11.84 |
| 3 | 243 | 243 | Yes | 1.37 |
| 4 | 793 | 793 | Yes | 4.07 |
| 5 | 60 | 60 | Yes | 5.16 |
| 6 | 3 | 3 | Yes | 4.26 |
| 7 | 5 |  | No | 67.33 |
| 8 | 3 | 3 | Yes | 5.49 |
| 9 | 60 | 60 | Yes | 3.58 |
| 10 | 31 | 31 | Yes | 1.57 |
| 11 | 9 | 9 | Yes | 5.48 |
| 12 | 7 | 7 | Yes | 4.51 |
| 13 | 4 | 4 | Yes | 4.99 |
| 14 | 4 | 4 | Yes | 4.06 |
| 15 | 7680 | 7680 | Yes | 4.67 |
| 16 | 48 | 48 | Yes | 4.01 |
| 17 | 67 | 67 | Yes | 3.99 |
| 18 | 73 | 73 | Yes | 5.15 |
| 19 | 20 |  | No | 76.57 |
| 20 | 63 | 63 | Yes | 4.21 |
