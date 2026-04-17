# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-27 10:03:17

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
| sudoku_game | 6704 | 35219 | 41923 | 10 | 10 | 25.80 | 516.14 |
| add_numbers | 4080 | 886 | 4966 | 20 | 0 | 1.79 | 35.91 |
| counting_zeros | 5400 | 14810 | 20210 | 4 | 16 | 10.10 | 202.08 |
| task_decoding | 5400 | 2243 | 7643 | 20 | 0 | 3.36 | 67.16 |
| task_summation | 5460 | 2747 | 8207 | 20 | 0 | 3.45 | 68.94 |
| task_transcription | 4026 | 718 | 4744 | 19 | 1 | 8.87 | 177.38 |
| task_sequences | 4140 | 3322 | 7462 | 19 | 1 | 4.59 | 91.8 |
| string_entry | 4643 | 1539 | 6182 | 10 | 10 | 3.18 | 63.5 |
| **TOTAL** | **39853** | **61484** | **101337** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 5 5 1 4 6 2 6 5 4 4 5 1 6 | 3 5 5 1 4 6 2 6 5 4 4 5 1 6 | Yes | 26.2 |
| 2 | 4 6 5 3 3 1 3 1 5 6 5 6 3 1 |  | No | 30.2 |
| 3 | 1 4 6 2 3 1 3 2 1 6 3 6 2 6 | 1 4 6 2 3 1 3 2 1 6 3 6 2 6 | Yes | 22.5 |
| 4 | 1 4 6 5 2 1 4 2 2 6 1 6 6 2 | 1 4 6 5 2 1 4 2 6 1 6 2 | No | 24.03 |
| 5 | 2 2 6 1 3 1 5 1 6 3 2 6 2 3 |  | No | 34.38 |
| 6 | 1 3 5 2 4 1 3 4 5 6 5 3 3 2 | 1 3 5 2 4 1 3 4 5 6 5 3 3 2 | Yes | 18.74 |
| 7 | 5 4 6 1 2 1 5 1 6 2 1 3 2 1 |  | No | 30.49 |
| 8 | 5 2 6 1 1 5 2 3 2 4 3 4 3 1 | 5 2 6 1 1 5 2 3 2 4 3 4 3 1 | Yes | 21.31 |
| 9 | 6 1 5 5 2 6 1 4 3 5 4 1 1 1 |  | No | 29.13 |
| 10 | 1 3 6 6 4 5 6 3 4 5 1 6 5 4 |  | No | 33.36 |
| 11 | 2 6 1 1 5 6 5 6 6 1 5 5 2 1 | 2 6 1 1 5 6 5 6 6 1 5 5 2 1 | Yes | 26.1 |
| 12 | 3 4 5 3 6 5 3 2 3 5 6 2 6 4 | 3 4 5 3 6 5 3 2 3 5 6 2 6 4 | Yes | 22.53 |
| 13 | 2 5 4 2 6 3 6 2 5 2 3 3 4 2 |  | No | 31.84 |
| 14 | 5 3 1 5 6 2 1 5 4 2 1 3 6 5 | 5 3 1 5 6 2 1 5 4 2 3 6 5 | No | 18.09 |
| 15 | 4 1 1 2 6 6 2 5 3 5 2 4 1 3 |  | No | 33.23 |
| 16 | 2 1 5 6 3 6 2 1 3 2 5 3 6 5 | 2 1 5 6 3 6 2 1 3 2 5 3 6 5 | Yes | 24.97 |
| 17 | 3 5 1 6 3 2 6 1 4 2 5 4 2 3 | 3 5 1 6 3 2 6 1 4 2 5 4 2 3 | Yes | 17.29 |
| 18 | 2 5 3 1 3 4 1 6 4 2 1 1 5 1 | 2 5 3 3 1 4 1 6 4 2 1 1 5 1 | No | 21.47 |
| 19 | 1 6 2 4 2 4 1 1 5 4 1 6 3 5 | 1 6 2 4 2 4 1 1 5 4 1 6 3 5 | Yes | 21.93 |
| 20 | 1 2 4 6 4 2 5 6 4 4 3 6 4 2 | 1 2 4 6 4 2 5 6 4 4 3 6 4 2 | Yes | 28.31 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1584 | 1584 | Yes | 2.66 |
| 2 | 1223 | 1223 | Yes | 1.85 |
| 3 | 2542 | 2542 | Yes | 1.79 |
| 4 | 1163 | 1163 | Yes | 1.68 |
| 5 | 1849 | 1849 | Yes | 1.11 |
| 6 | 1654 | 1654 | Yes | 1.82 |
| 7 | 1279 | 1279 | Yes | 1.14 |
| 8 | 1224 | 1224 | Yes | 1.86 |
| 9 | 1738 | 1738 | Yes | 1.11 |
| 10 | 1852 | 1852 | Yes | 1.05 |
| 11 | 1777 | 1777 | Yes | 1.78 |
| 12 | 1299 | 1299 | Yes | 2.73 |
| 13 | 1881 | 1881 | Yes | 1.82 |
| 14 | 1278 | 1278 | Yes | 1.8 |
| 15 | 1507 | 1507 | Yes | 1.7 |
| 16 | 1827 | 1827 | Yes | 1.27 |
| 17 | 1847 | 1847 | Yes | 1.92 |
| 18 | 1986 | 1986 | Yes | 2.28 |
| 19 | 1445 | 1445 | Yes | 1.92 |
| 20 | 934 | 934 | Yes | 2.6 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 | 36 | No | 12.09 |
| 2 | 35 | 34 | No | 17.16 |
| 3 | 56 | 55 | No | 5.2 |
| 4 | 47 | 44 | No | 8.94 |
| 5 | 39 | 36 | No | 8.46 |
| 6 | 61 | 55 | No | 7.95 |
| 7 | 41 | 41 | Yes | 10.46 |
| 8 | 54 | 54 | Yes | 9.71 |
| 9 | 47 | 47 | Yes | 9.34 |
| 10 | 64 | 60 | No | 8.11 |
| 11 | 51 | 47 | No | 8.63 |
| 12 | 55 | 52 | No | 6.07 |
| 13 | 47 | 45 | No | 9.7 |
| 14 | 41 | 41 | Yes | 8.69 |
| 15 | 66 | 64 | No | 9.77 |
| 16 | 75 | 73 | No | 19.03 |
| 17 | 68 | 60 | No | 7.62 |
| 18 | 63 | 56 | No | 11.38 |
| 19 | 39 | 40 | No | 11.28 |
| 20 | 72 | 61 | No | 12.46 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DNGAJWI | DNGAJWI | Yes | 4.73 |
| 2 | JBXHEZU | JBXHEZU | Yes | 2.7 |
| 3 | ZSMPFXL | ZSMPFXL | Yes | 2.46 |
| 4 | IOGUBYL | IOGUBYL | Yes | 3.16 |
| 5 | OSWCPJB | OSWCPJB | Yes | 2.9 |
| 6 | DTPILAB | DTPILAB | Yes | 2.66 |
| 7 | HISZUOM | HISZUOM | Yes | 2.1 |
| 8 | CVDSEWJ | CVDSEWJ | Yes | 2.6 |
| 9 | STCUIJG | STCUIJG | Yes | 2.85 |
| 10 | WLZNUGT | WLZNUGT | Yes | 3.32 |
| 11 | DHXITEZ | DHXITEZ | Yes | 3.28 |
| 12 | TGQMFHV | TGQMFHV | Yes | 2.98 |
| 13 | NZJCWBE | NZJCWBE | Yes | 3.02 |
| 14 | SWQELYX | SWQELYX | Yes | 3.63 |
| 15 | PMXVAFT | PMXVAFT | Yes | 5.55 |
| 16 | UCDIOGS | UCDIOGS | Yes | 3.72 |
| 17 | PWHLEZF | PWHLEZF | Yes | 3.22 |
| 18 | TROKDLJ | TROKDLJ | Yes | 4.35 |
| 19 | ZDRBHPE | ZDRBHPE | Yes | 4.29 |
| 20 | BOMHVTQ | BOMHVTQ | Yes | 3.62 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 9.4 0.6 | Yes | 2.4 |
| 2 | [1.9, 8.1] | 1.9 8.1 | Yes | 2.89 |
| 3 | [4.0, 6.0] | 6.0 4.0 | Yes | 2.26 |
| 4 | [3.8, 6.2] | 6.2 3.8 | Yes | 3.59 |
| 5 | [0.9, 9.1] | 0.9 9.1 | Yes | 3.8 |
| 6 | [4.3, 5.7] | 5.7 4.3 | Yes | 4.1 |
| 7 | [0.9, 9.1] | 0.9 9.1 | Yes | 2.84 |
| 8 | [3.6, 6.4] | 3.6 6.4 | Yes | 1.56 |
| 9 | [0.7, 9.3] | 9.3 0.7 | Yes | 3.95 |
| 10 | [4.0, 6.0] | 6.0 4.0 | Yes | 2.94 |
| 11 | [3.9, 6.1] | 3.9 6.1 | Yes | 3.47 |
| 12 | [4.2, 5.8] | 5.8 4.2 | Yes | 3.49 |
| 13 | [3.0, 7.0] | 3.0 7.0 | Yes | 6.61 |
| 14 | [1.7, 8.3] | 8.3 1.7 | Yes | 4.68 |
| 15 | [0.3, 9.7] | 0.3 9.7 | Yes | 2.87 |
| 16 | [0.8, 9.2] | 9.2 0.8 | Yes | 3.59 |
| 17 | [2.4, 7.6] | 2.4 7.6 | Yes | 4.46 |
| 18 | [4.9, 5.1] | 5.1 4.9 | Yes | 2.95 |
| 19 | [2.7, 7.3] | 7.3 2.7 | Yes | 2.55 |
| 20 | [2.6, 7.4] | 2.6 7.4 | Yes | 3.94 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1XW9QGRKP7X3 | TIMEOUT | No | 120.03 |
| 2 | OQWNVEFKCBXI | OQWNVEFKCBXI | Yes | 1.75 |
| 3 | ROA6O0G0WRK6 | ROA6O0G0WRK6 | Yes | 2.61 |
| 4 | CRK8KPUJHCCV | CRK8KPUJHCCV | Yes | 1.03 |
| 5 | OW12E0FPMHUN | OW12E0FPMHUN | Yes | 4.23 |
| 6 | Q8SQE4L59K4K | Q8SQE4L59K4K | Yes | 1.75 |
| 7 | OLOF90HLMX57 | OLOF90HLMX57 | Yes | 3.45 |
| 8 | OCVR9F2HSQK7 | OCVR9F2HSQK7 | Yes | 2.38 |
| 9 | W18CQLCTUFV4 | W18CQLCTUFV4 | Yes | 3.01 |
| 10 | 1U6WFF8QSG8F | 1U6WFF8QSG8F | Yes | 2.9 |
| 11 | 63P5D3MR7FP6 | 63P5D3MR7FP6 | Yes | 1.96 |
| 12 | R3UCNMY0I9GO | R3UCNMY0I9GO | Yes | 2.97 |
| 13 | JP58RDOYXUU1 | JP58RDOYXUU1 | Yes | 2.28 |
| 14 | YRKM1M4G22S2 | YRKM1M4G22S2 | Yes | 3.5 |
| 15 | 70EV7QUFFB36 | 70EV7QUFFB36 | Yes | 4.18 |
| 16 | P45RASTA979X | P45RASTA979X | Yes | 2.16 |
| 17 | 19HB3MXTCXC6 | 19HB3MXTCXC6 | Yes | 1.62 |
| 18 | OTYKFB5M9XPC | OTYKFB5M9XPC | Yes | 11.9 |
| 19 | RHJJRDUL0NFX | RHJJRDUL0NFX | Yes | 1.99 |
| 20 | PRN5PVUJVNEX | PRN5PVUJVNEX | Yes | 1.67 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 16 | No | 17.2 |
| 2 | 9 | 9 | Yes | 3.48 |
| 3 | 7 | 7 | Yes | 3.81 |
| 4 | 64 | 64 | Yes | 5.8 |
| 5 | 9 | 9 | Yes | 5.51 |
| 6 | 36 | 36 | Yes | 2.69 |
| 7 | 26 | 26 | Yes | 8.09 |
| 8 | 39 | 39 | Yes | 3.24 |
| 9 | 793 | 793 | Yes | 1.98 |
| 10 | 23 | 23 | Yes | 3.72 |
| 11 | 67 | 67 | Yes | 2.46 |
| 12 | 3 | 3 | Yes | 4.81 |
| 13 | 60 | 60 | Yes | 5.37 |
| 14 | 5 | 5 | Yes | 4.26 |
| 15 | 19 | 19 | Yes | 2.22 |
| 16 | 44 | 44 | Yes | 3.63 |
| 17 | 10 | 10 | Yes | 3.55 |
| 18 | 16 | 16 | Yes | 4.19 |
| 19 | 48 | 48 | Yes | 2.14 |
| 20 | 6 | 6 | Yes | 3.67 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | </<//\ /) | </<//\ /) | Yes | 1.98 |
| 2 |  _<(_ )_  | _<(_ )_ | No | 3.1 |
| 3 | ()/_\  (  | ()/_\  ( | No | 5.66 |
| 4 | __</_\)_/ | __</_\)_/ | Yes | 4.2 |
| 5 | \/ /   /) | \/ /   /) | Yes | 3.08 |
| 6 | (_/)< _<( | (_/)< _<( | Yes | 1.98 |
| 7 | /<<)(\\(< | /<<)(\\( | No | 2.45 |
| 8 | _/_<)/\_/ | _/_<)/\_/ | Yes | 2.62 |
| 9 | \<\</_( < | \<\</_( | No | 2.2 |
| 10 | )(_)())() | )(_)())() | Yes | 2.16 |
| 11 | ) </\ /_  | ) </\ /_ | No | 3.01 |
| 12 | ( \)< ) ( | ( \)< ) ( | Yes | 2.68 |
| 13 | (()( )\(  | (()( )\( | No | 2.38 |
| 14 | ))))\)    | ))))\) | No | 2.71 |
| 15 | _ _)_\  < | _ _)_\ | No | 4.64 |
| 16 | < __ (_/) | < __ (_/) | Yes | 3.91 |
| 17 | <())/ ()/ | <())/ ()/ | Yes | 3.7 |
| 18 | (</ ( /)) | (</ ( /)) | Yes | 2.89 |
| 19 | \   \)\_  | \   \)\_ | No | 5.32 |
| 20 | \\(<(< _< | \\(<(< _ | No | 2.84 |
