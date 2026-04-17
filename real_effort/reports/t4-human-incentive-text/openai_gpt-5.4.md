# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-27 10:12:32

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 5496 | 32247 | 37743 | 8 | 12 | 26.92 | 538.37 |
| add_numbers | 3240 | 808 | 4048 | 20 | 0 | 3.32 | 66.44 |
| counting_zeros | 4640 | 17077 | 21717 | 20 | 0 | 12.65 | 253.07 |
| task_decoding | 4580 | 2875 | 7455 | 20 | 0 | 4.26 | 85.17 |
| task_summation | 4920 | 5345 | 10265 | 20 | 0 | 7.45 | 148.98 |
| task_transcription | 3380 | 1572 | 4952 | 20 | 0 | 3.85 | 77.05 |
| task_sequences | 3241 | 6006 | 9247 | 18 | 2 | 9.83 | 196.68 |
| string_entry | 3697 | 18417 | 22114 | 11 | 9 | 20.54 | 410.91 |
| **TOTAL** | **33194** | **84347** | **117541** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 5 5 1 6 1 3 5 2 3 6 3 1 | 1 2 5 5 1 6 1 3 5 2 3 6 3 1 | Yes | 16.76 |
| 2 | 1 2 3 5 3 4 2 2 3 6 1 2 3 5 |  | No | 33.33 |
| 3 | 3 6 1 1 2 4 2 1 6 4 4 6 5 3 |  | No | 32.1 |
| 4 | 3 5 6 2 1 3 2 2 1 5 3 2 1 5 |  | No | 33.07 |
| 5 | 2 3 2 6 1 3 3 4 4 5 1 4 2 3 |  | No | 41.09 |
| 6 | 1 4 5 6 2 2 3 5 4 1 4 1 3 5 |  | No | 30.38 |
| 7 | 4 1 1 3 5 4 5 1 3 4 2 6 1 5 | 4 1 1 3 5 4 5 1 3 4 2 6 1 5 | Yes | 12.26 |
| 8 | 5 2 6 3 6 1 1 6 2 4 1 2 5 4 |  | No | 32.75 |
| 9 | 6 1 3 2 5 4 6 4 6 1 4 3 1 6 |  | No | 41.42 |
| 10 | 5 5 6 6 3 4 1 4 3 6 4 6 3 1 |  | No | 37.38 |
| 11 | 4 2 1 6 3 4 6 2 1 4 5 6 2 2 |  | No | 34.36 |
| 12 | 5 6 4 6 1 2 5 5 5 4 6 1 5 2 | 5 6 4 6 1 2 5 5 5 4 6 1 5 2 | Yes | 15.16 |
| 13 | 5 2 6 4 1 5 5 1 1 3 2 4 1 6 | 5 2 6 4 1 5 5 1 1 3 2 4 1 6 | Yes | 17.4 |
| 14 | 1 4 6 2 5 5 2 6 3 5 6 2 4 3 | 1 4 6 2 5 5 2 6 3 5 6 2 4 3 | Yes | 25.7 |
| 15 | 6 2 4 5 4 5 3 6 1 5 1 6 3 2 | 6 2 4 5 4 5 3 6 1 5 1 6 3 2 | Yes | 11.79 |
| 16 | 6 5 1 2 5 1 6 5 4 6 4 2 3 1 |  | No | 35.05 |
| 17 | 2 5 1 6 1 3 6 3 1 6 6 3 2 5 | 2 5 1 6 1 3 6 3 1 6 6 3 2 5 | Yes | 15.8 |
| 18 | 6 4 4 1 3 6 2 3 1 6 6 2 5 4 |  | No | 26.48 |
| 19 | 2 6 1 2 5 6 5 2 6 4 3 1 2 5 | 2 6 1 2 5 6 5 2 6 4 3 1 2 5 | Yes | 12.29 |
| 20 | 3 6 4 2 4 6 3 6 6 4 2 3 5 6 |  | No | 33.76 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 808 | 808 | Yes | 4.17 |
| 2 | 1623 | 1623 | Yes | 3.61 |
| 3 | 1433 | 1433 | Yes | 1.27 |
| 4 | 1804 | 1804 | Yes | 1.19 |
| 5 | 1106 | 1106 | Yes | 3.31 |
| 6 | 1967 | 1967 | Yes | 3.11 |
| 7 | 1794 | 1794 | Yes | 3.44 |
| 8 | 1477 | 1477 | Yes | 3.19 |
| 9 | 1205 | 1205 | Yes | 3.27 |
| 10 | 1401 | 1401 | Yes | 3.39 |
| 11 | 1925 | 1925 | Yes | 3.45 |
| 12 | 1095 | 1095 | Yes | 4.48 |
| 13 | 1974 | 1974 | Yes | 3.47 |
| 14 | 1884 | 1884 | Yes | 5.29 |
| 15 | 1400 | 1400 | Yes | 3.12 |
| 16 | 1379 | 1379 | Yes | 1.3 |
| 17 | 606 | 606 | Yes | 4.83 |
| 18 | 1246 | 1246 | Yes | 3.65 |
| 19 | 1092 | 1092 | Yes | 3.65 |
| 20 | 1840 | 1840 | Yes | 3.24 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 | 59 | Yes | 12.42 |
| 2 | 75 | 75 | Yes | 13.23 |
| 3 | 70 | 70 | Yes | 14.94 |
| 4 | 43 | 43 | Yes | 9.86 |
| 5 | 71 | 71 | Yes | 12.95 |
| 6 | 40 | 40 | Yes | 13.0 |
| 7 | 75 | 75 | Yes | 12.44 |
| 8 | 60 | 60 | Yes | 14.93 |
| 9 | 49 | 49 | Yes | 13.19 |
| 10 | 67 | 67 | Yes | 11.68 |
| 11 | 61 | 61 | Yes | 13.47 |
| 12 | 50 | 50 | Yes | 12.36 |
| 13 | 63 | 63 | Yes | 15.84 |
| 14 | 43 | 43 | Yes | 11.49 |
| 15 | 50 | 50 | Yes | 11.33 |
| 16 | 45 | 45 | Yes | 10.28 |
| 17 | 51 | 51 | Yes | 11.74 |
| 18 | 51 | 51 | Yes | 10.78 |
| 19 | 70 | 70 | Yes | 14.65 |
| 20 | 41 | 41 | Yes | 12.48 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZEKHVJL | ZEKHVJL | Yes | 5.02 |
| 2 | BJOIWVP | BJOIWVP | Yes | 4.48 |
| 3 | AOIFKQS | AOIFKQS | Yes | 4.37 |
| 4 | KSDGRVC | KSDGRVC | Yes | 6.04 |
| 5 | UJVRBLN | UJVRBLN | Yes | 4.94 |
| 6 | NGUKXSL | NGUKXSL | Yes | 5.95 |
| 7 | FBDNSZX | FBDNSZX | Yes | 3.42 |
| 8 | RWJDUSI | RWJDUSI | Yes | 4.08 |
| 9 | ATMVWQI | ATMVWQI | Yes | 3.14 |
| 10 | GQLHZFV | GQLHZFV | Yes | 2.79 |
| 11 | OPRUKYE | OPRUKYE | Yes | 3.28 |
| 12 | MQRZEPO | MQRZEPO | Yes | 5.82 |
| 13 | SDOKTBY | SDOKTBY | Yes | 3.17 |
| 14 | YLSIXOT | YLSIXOT | Yes | 2.52 |
| 15 | KGQRVIJ | KGQRVIJ | Yes | 5.56 |
| 16 | RHSGJUY | RHSGJUY | Yes | 6.03 |
| 17 | UAVNIFL | UAVNIFL | Yes | 3.54 |
| 18 | ROJIWSG | ROJIWSG | Yes | 2.75 |
| 19 | GUDZWOT | GUDZWOT | Yes | 2.99 |
| 20 | WJZIPQR | WJZIPQR | Yes | 5.27 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.65 |
| 2 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.38 |
| 3 | [1.7, 8.3] | 8.3 1.7 | Yes | 5.9 |
| 4 | [3.6, 6.4] | 6.4 3.6 | Yes | 8.3 |
| 5 | [0.5, 9.5] | 0.5 9.5 | Yes | 6.17 |
| 6 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.01 |
| 7 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.65 |
| 8 | [1.6, 8.4] | 8.4 1.6 | Yes | 5.94 |
| 9 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.48 |
| 10 | [2.0, 8.0] | 2.0 8.0 | Yes | 6.69 |
| 11 | [1.7, 8.3] | 8.3 1.7 | Yes | 7.63 |
| 12 | [2.4, 7.6] | 7.6 2.4 | Yes | 5.9 |
| 13 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.73 |
| 14 | [0.2, 9.8] | 0.2 9.8 | Yes | 8.21 |
| 15 | [2.6, 7.4] | 2.6 7.4 | Yes | 9.74 |
| 16 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.98 |
| 17 | [0.7, 9.3] | 9.3 0.7 | Yes | 13.13 |
| 18 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.25 |
| 19 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.84 |
| 20 | [1.3, 8.7] | 8.7 1.3 | Yes | 7.41 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XSW4HB12YUGT | XSW4HB12YUGT | Yes | 2.38 |
| 2 | A7KRQJL3AXZ5 | A7KRQJL3AXZ5 | Yes | 4.34 |
| 3 | LO9OFTIA61NX | LO9OFTIA61NX | Yes | 2.67 |
| 4 | 025T6GN5P193 | 025T6GN5P193 | Yes | 5.84 |
| 5 | 2HU3GS9G0MUB | 2HU3GS9G0MUB | Yes | 4.82 |
| 6 | ED410OX3PDJQ | ED410OX3PDJQ | Yes | 4.1 |
| 7 | BM15MM1MPMYX | BM15MM1MPMYX | Yes | 3.38 |
| 8 | FWYYE94YTYX2 | FWYYE94YTYX2 | Yes | 1.47 |
| 9 | TCR908TQ64F3 | TCR908TQ64F3 | Yes | 1.67 |
| 10 | 7SP466T8AIBL | 7SP466T8AIBL | Yes | 4.56 |
| 11 | J9UAZ7FC29J4 | J9UAZ7FC29J4 | Yes | 5.82 |
| 12 | QQ4T93PR5IAX | QQ4T93PR5IAX | Yes | 4.68 |
| 13 | OHJ3ALESXBCY | OHJ3ALESXBCY | Yes | 1.75 |
| 14 | 5ECIFHUB8ZAL | 5ECIFHUB8ZAL | Yes | 5.14 |
| 15 | 3C21LPYIKJ5K | 3C21LPYIKJ5K | Yes | 4.84 |
| 16 | JMNX3C744UB5 | JMNX3C744UB5 | Yes | 4.01 |
| 17 | JWDC87T8EG8N | JWDC87T8EG8N | Yes | 2.12 |
| 18 | PZZ4OMI0P0EL | PZZ4OMI0P0EL | Yes | 5.62 |
| 19 | REZHPQE0GJV7 | REZHPQE0GJV7 | Yes | 4.5 |
| 20 | YR7ZXZW3VFEW | YR7ZXZW3VFEW | Yes | 3.31 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 73 | Yes | 6.4 |
| 2 | 39 | 39 | Yes | 4.06 |
| 3 | 10 | 10 | Yes | 14.18 |
| 4 | 793 | 793 | Yes | 4.35 |
| 5 | 36 | 36 | Yes | 2.72 |
| 6 | 3 | 3 | Yes | 6.13 |
| 7 | 48 | 48 | Yes | 2.45 |
| 8 | 60 | 60 | Yes | 5.4 |
| 9 | 4096 |  | No | 42.75 |
| 10 | 7680 | 7680 | Yes | 6.02 |
| 11 | 65 | 65 | Yes | 4.1 |
| 12 | 7 | 7 | Yes | 3.46 |
| 13 | 64 | 64 | Yes | 5.44 |
| 14 | 9 | 9 | Yes | 4.11 |
| 15 | 23 | 23 | Yes | 5.07 |
| 16 | 63 | 63 | Yes | 3.91 |
| 17 | 20 |  | No | 57.24 |
| 18 | 19 | 19 | Yes | 5.57 |
| 19 | 5 | 5 | Yes | 5.51 |
| 20 | 3 | 3 | Yes | 7.79 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  )</)/  / | )</)/  / | No | 18.39 |
| 2 | //</ \ <  | //</ \ < | No | 14.67 |
| 3 | \/\)__\\_ | \/\)__\\_ | Yes | 7.5 |
| 4 | _\ <))_/_ |  | No | 46.12 |
| 5 | \</_( <_\ | \</_( <_\ | Yes | 7.33 |
| 6 | <_/_/(_\( |  | No | 46.03 |
| 7 | \/// <( _ | \/// <( _ | Yes | 19.67 |
| 8 | \//<_/<_  | \//<_/<_ | No | 13.18 |
| 9 | _)</(_/(  | _)</(_/( | No | 38.34 |
| 10 | \(</ /<)_ | \(</ /<)_ | Yes | 23.84 |
| 11 | \(\\))\(  |  | No | 46.61 |
| 12 | (((<_  )\ | (((<_  )\ | Yes | 22.33 |
| 13 | \/(<<  \< | \/(<<  \< | Yes | 11.18 |
| 14 | /\)< _(<( | /\)< _(<( | Yes | 3.83 |
| 15 | / _\<< (( | / _\<< (( | Yes | 6.51 |
| 16 | <\)/(\ /  | <\)/(\ / | No | 32.0 |
| 17 | \//_)  )\ | \//_)  )\ | Yes | 14.67 |
| 18 | \()\/ \</ | \()\/ \</ | Yes | 7.35 |
| 19 | ) ))_/ /  | ) ))_/ / | No | 11.74 |
| 20 | /(_< </ ( | /(_< </ ( | Yes | 19.6 |
