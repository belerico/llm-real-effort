# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-26 15:42:56

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
| sudoku_game | 5797 | 35695 | 41492 | 5 | 15 | 29.71 | 594.34 |
| add_numbers | 3180 | 598 | 3778 | 20 | 0 | 4.10 | 82.08 |
| counting_zeros | 4500 | 14352 | 18852 | 5 | 15 | 10.24 | 204.9 |
| task_decoding | 4500 | 2191 | 6691 | 20 | 0 | 5.19 | 103.8 |
| task_summation | 4560 | 3792 | 8352 | 20 | 0 | 6.65 | 132.97 |
| task_transcription | 3336 | 663 | 3999 | 20 | 0 | 3.70 | 74.08 |
| task_sequences | 3240 | 4277 | 7517 | 20 | 0 | 5.56 | 111.14 |
| string_entry | 3673 | 1402 | 5075 | 15 | 5 | 4.47 | 89.41 |
| **TOTAL** | **32786** | **62970** | **95756** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 1 6 4 3 4 1 3 1 2 6 3 1 1 | Looking at this puzzle, I need to find each missing number systematically using row, column, and box constraints.  **Row-by-row analysis:**  **Row 6:** Has 6,4,3,_,2,5 → R6C4 = **1**  **Column 2:** Has _,6,2,3,5,4 → R1C2 = **1** (only missing value)  **Row 2:** Has _,6,1,_,5,2 → needs 3,4. Column 1 needs {1,3,4}, Column 4 needs {3}. So R2C4 = **3**, R2C1 = **4**  **Row 1:** Has _,1,5,2,4,_ → needs 3,6. Column 1 needs {1,3}, so R1C1 = **3**, R1C6 = **6**  **Row 4:** Has _,3,_,5,6,4 → needs 1,2. Column 1 needs {1}, so R4C1 = **1**, R4C3 = **2**  **Row 3:** Has 5,2,_,6,_,_ → needs 1,3,4. Column 3 needs {4,6}, so R3C3 = **4**. Column 5 needs {1,3}, Box 2 needs {1,3}: R3C5 = **3**, R3C6 = **1**  **Row 5:** Has 2,5,_,4,_,_ → needs 1,3,6. Column 3 needs {6}, so R5C3 = **6**. Column 5 needs {1}, so R5C5 = **1**, R5C6 = **3**  Answer: | No | 32.05 |
| 2 | 2 5 3 4 3 2 6 3 2 1 3 5 6 2 |  | No | 35.43 |
| 3 | 4 6 5 3 1 3 5 6 1 1 6 3 4 3 |  | No | 35.77 |
| 4 | 6 6 5 4 1 4 3 6 2 4 6 1 3 2 | 6 6 5 4 1 4 5 3 6 2 4 6 1 3 2 | No | 25.56 |
| 5 | 3 5 2 5 6 4 1 2 1 6 4 2 4 3 | 3 5 2 5 6 4 1 2 1 6 4 2 4 3 | Yes | 33.71 |
| 6 | 2 1 6 3 1 4 3 5 4 2 6 4 2 3 | 2 1 6 3 1 4 3 5 4 2 6 4 2 3 5 | No | 18.01 |
| 7 | 1 3 2 6 5 4 1 4 1 2 6 1 2 6 |  | No | 31.06 |
| 8 | 5 1 4 3 5 5 3 4 4 5 4 3 4 6 | Looking at this puzzle, I need to find each missing number systematically using row, column, and box constraints.  **Row-by-row analysis:**  **Row 1:** 3 _ 2 \| 4 6 _ → needs {1, 5} - Col 6 options from column: {1, 4, 6} → intersect {1, 5} → **R1C6 = 1**, **R1C2 = 5**  **Row 2:** _ 1 6 \| _ _ 2 → needs {3, 4, 5} - Col 1 options: {4} → **R2C1 = 4**  **Row 4:** 2 _ 3 \| 6 1 5 → needs {4} → **R4C2 = 4**  **Row 6:** 5 _ _ \| 1 2 _ → needs {3, 4, 6} - Col 2 remaining: {3} → **R6C2 = 3** - Col 3 remaining: {4, 5}, intersect row needs {4, 6} → **R6C3 = 4** - Col 6 remaining: | No | 33.59 |
| 9 | 6 2 2 5 3 4 2 1 2 1 3 3 6 5 |  | No | 34.73 |
| 10 | 6 1 5 3 2 1 6 4 5 6 3 5 2 6 |  | No | 35.13 |
| 11 | 2 6 1 4 1 5 2 3 4 6 3 5 2 4 | 2 6 1 4 1 5 2 3 4 6 3 5 2 4 | Yes | 16.46 |
| 12 | 6 3 3 4 5 5 3 1 3 4 1 2 5 2 | 6 3 3 4 5 5 3 1 3 4 1 2 5 2 | Yes | 19.92 |
| 13 | 6 1 3 1 1 2 6 5 4 5 6 1 6 3 |  | No | 32.27 |
| 14 | 2 1 5 6 4 3 5 4 4 2 3 5 5 1 |  | No | 33.3 |
| 15 | 3 1 6 5 5 2 4 3 5 6 2 6 3 5 | 3 1 6 5 5 2 1 6 4 3 3 1 5 6 2 6 4 2 3 5 1 | No | 28.79 |
| 16 | 6 4 5 2 2 3 4 1 5 6 1 3 6 3 | 6 4 5 2 2 3 4 1 5 6 1 3 6 3 | Yes | 18.96 |
| 17 | 4 6 5 2 1 6 6 2 1 3 6 5 1 2 | 4 6 5 2 1 6 6 2 1 3 6 5 1 2 | Yes | 21.73 |
| 18 | 1 2 5 1 5 6 2 3 6 4 5 2 4 1 | 1 2 5 1 5 6 1 4 2 3 6 4 3 2 1 5 2 4 1 3 6 | No | 22.91 |
| 19 | 2 6 4 3 6 5 1 4 3 5 1 3 2 1 | 2 6 4 3 6 5 1 4 3 5 1 2 3 2 1 | No | 32.95 |
| 20 | 5 6 1 2 4 3 1 2 4 3 6 6 1 5 |  | No | 51.96 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1609 | 1609 | Yes | 2.94 |
| 2 | 870 | 870 | Yes | 2.51 |
| 3 | 1842 | 1842 | Yes | 2.58 |
| 4 | 1532 | 1532 | Yes | 2.17 |
| 5 | 1726 | 1726 | Yes | 2.96 |
| 6 | 1385 | 1385 | Yes | 3.03 |
| 7 | 1567 | 1567 | Yes | 2.58 |
| 8 | 2107 | 2107 | Yes | 2.76 |
| 9 | 1324 | 1324 | Yes | 11.95 |
| 10 | 2110 | 2110 | Yes | 2.36 |
| 11 | 1243 | 1243 | Yes | 2.77 |
| 12 | 2194 | 2194 | Yes | 2.72 |
| 13 | 2402 | 2402 | Yes | 3.31 |
| 14 | 1761 | 1761 | Yes | 3.31 |
| 15 | 1579 | 1579 | Yes | 12.0 |
| 16 | 1475 | 1475 | Yes | 2.28 |
| 17 | 1283 | 1283 | Yes | 2.58 |
| 18 | 1481 | 1481 | Yes | 2.65 |
| 19 | 2581 | 2581 | Yes | 12.1 |
| 20 | 1974 | 1974 | Yes | 2.51 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 58 | No | 7.26 |
| 2 | 37 | 36 | No | 7.57 |
| 3 | 60 | 59 | No | 12.1 |
| 4 | 62 | 59 | No | 7.13 |
| 5 | 70 | 66 | No | 7.46 |
| 6 | 35 | 35 | Yes | 17.25 |
| 7 | 47 | 40 | No | 16.94 |
| 8 | 58 | 52 | No | 9.43 |
| 9 | 62 | 50 | No | 6.84 |
| 10 | 59 | 59 | Yes | 18.65 |
| 11 | 75 | 72 | No | 9.97 |
| 12 | 62 | 57 | No | 7.24 |
| 13 | 55 | 49 | No | 6.56 |
| 14 | 39 | 39 | Yes | 13.42 |
| 15 | 63 | 56 | No | 7.31 |
| 16 | 73 | 73 | Yes | 10.45 |
| 17 | 45 | 44 | No | 8.31 |
| 18 | 35 | 35 | Yes | 6.34 |
| 19 | 63 | 60 | No | 18.69 |
| 20 | 51 | 43 | No | 5.96 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LFKEWBH | LFKEWBH | Yes | 3.66 |
| 2 | GHCMKIU | GHCMKIU | Yes | 4.02 |
| 3 | BTJGWCR | BTJGWCR | Yes | 4.37 |
| 4 | TKMRQSH | TKMRQSH | Yes | 3.06 |
| 5 | DAYJUIX | DAYJUIX | Yes | 4.43 |
| 6 | OYQPGZE | OYQPGZE | Yes | 3.73 |
| 7 | PBZHVDT | PBZHVDT | Yes | 4.48 |
| 8 | VANGRYS | VANGRYS | Yes | 4.76 |
| 9 | ENVIWFH | ENVIWFH | Yes | 3.88 |
| 10 | JSLQPIA | JSLQPIA | Yes | 4.26 |
| 11 | UBHATRE | UBHATRE | Yes | 3.86 |
| 12 | IXMGDZP | IXMGDZP | Yes | 3.75 |
| 13 | GQUCBNM | GQUCBNM | Yes | 3.06 |
| 14 | NVPFMAG | NVPFMAG | Yes | 9.83 |
| 15 | XRMWVEC | XRMWVEC | Yes | 3.96 |
| 16 | AZDRCKJ | AZDRCKJ | Yes | 3.82 |
| 17 | NOSPXHL | NOSPXHL | Yes | 3.95 |
| 18 | EZMPGVA | EZMPGVA | Yes | 13.57 |
| 19 | TZCSEDN | TZCSEDN | Yes | 3.99 |
| 20 | EABQNOP | EABQNOP | Yes | 13.35 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.2, 6.8] | 6.8 3.2 | Yes | 8.33 |
| 2 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.06 |
| 3 | [1.7, 8.3] | 8.3 1.7 | Yes | 8.62 |
| 4 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.4 |
| 5 | [2.0, 8.0] | 8.0 2.0 | Yes | 6.11 |
| 6 | [0.9, 9.1] | 0.9 9.1 | Yes | 13.23 |
| 7 | [2.3, 7.7] | 7.7 2.3 | Yes | 15.93 |
| 8 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.71 |
| 9 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.2 |
| 10 | [1.2, 8.8] | 1.2 8.8 | Yes | 3.08 |
| 11 | [1.4, 8.6] | 8.6 1.4 | Yes | 9.23 |
| 12 | [1.1, 8.9] | 1.1 8.9 | Yes | 10.4 |
| 13 | [3.7, 6.3] | 3.7 6.3 | Yes | 4.01 |
| 14 | [0.4, 9.6] | 0.4 9.6 | Yes | 4.61 |
| 15 | [2.1, 7.9] | 2.1 7.9 | Yes | 8.32 |
| 16 | [3.3, 6.7] | 3.3 6.7 | Yes | 3.79 |
| 17 | [2.6, 7.4] | 2.6 7.4 | Yes | 4.25 |
| 18 | [0.1, 9.9] | 9.9 0.1 | Yes | 4.2 |
| 19 | [4.4, 5.6] | 5.6 4.4 | Yes | 5.66 |
| 20 | [4.1, 5.9] | 4.1 5.9 | Yes | 2.85 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53N6FT6OH2RC | 53N6FT6OH2RC | Yes | 2.43 |
| 2 | MEX2PGQYP4CS | MEX2PGQYP4CS | Yes | 2.56 |
| 3 | 8LL7Z1TE4X5O | 8LL7Z1TE4X5O | Yes | 2.34 |
| 4 | JWGHVIDVY7RZ | JWGHVIDVY7RZ | Yes | 2.62 |
| 5 | DCEFP15QE235 | DCEFP15QE235 | Yes | 2.35 |
| 6 | BPUBYJSZCL19 | BPUBYJSZCL19 | Yes | 4.56 |
| 7 | GP5XHO735UNF | GP5XHO735UNF | Yes | 2.28 |
| 8 | ZQG4BOXM21RO | ZQG4BOXM21RO | Yes | 12.93 |
| 9 | R2WGKX6AISI2 | R2WGKX6AISI2 | Yes | 2.26 |
| 10 | 06L8KUE206MQ | 06L8KUE206MQ | Yes | 3.54 |
| 11 | A6BDIJCB6L12 | A6BDIJCB6L12 | Yes | 13.28 |
| 12 | SKZILOB6VG1Z | SKZILOB6VG1Z | Yes | 3.5 |
| 13 | VM382TXBGH7M | VM382TXBGH7M | Yes | 2.27 |
| 14 | 8NS9JUE5U93U | 8NS9JUE5U93U | Yes | 2.6 |
| 15 | TM9YXSRU0OD6 | TM9YXSRU0OD6 | Yes | 2.4 |
| 16 | 8DLP5VUR44AV | 8DLP5VUR44AV | Yes | 2.41 |
| 17 | 4GQNDEKSDIVS | 4GQNDEKSDIVS | Yes | 2.54 |
| 18 | WBOGAWDU6D0X | WBOGAWDU6D0X | Yes | 2.24 |
| 19 | NWK9HH2P26E7 | NWK9HH2P26E7 | Yes | 2.54 |
| 20 | RWKI0GTZK6OA | RWKI0GTZK6OA | Yes | 2.42 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 4.56 |
| 2 | 7 | 7 | Yes | 2.8 |
| 3 | 20 | 20 | Yes | 11.17 |
| 4 | 60 | 60 | Yes | 3.98 |
| 5 | 23 | 23 | Yes | 4.93 |
| 6 | 5 | 5 | Yes | 5.06 |
| 7 | 67 | 67 | Yes | 3.35 |
| 8 | 44 | 44 | Yes | 4.04 |
| 9 | 7680 | 7680 | Yes | 4.67 |
| 10 | 9 | 9 | Yes | 5.44 |
| 11 | 793 | 793 | Yes | 5.92 |
| 12 | 64 | 64 | Yes | 6.1 |
| 13 | 4 | 4 | Yes | 4.85 |
| 14 | 4 | 4 | Yes | 5.09 |
| 15 | 48 | 48 | Yes | 9.57 |
| 16 | 19 | 19 | Yes | 3.39 |
| 17 | 3 | 3 | Yes | 6.06 |
| 18 | 198 | 198 | Yes | 6.21 |
| 19 | 9 | 9 | Yes | 4.99 |
| 20 | 26 | 26 | Yes | 8.95 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \/_)/\\/) | \/_)/\\/) | Yes | 3.05 |
| 2 | ))(</)//_ | ))(</)//_ | Yes | 3.2 |
| 3 | )\\)/(/\/ | )\\)/(/\/ | Yes | 3.02 |
| 4 | __()<<)(( | __()<<)(( | Yes | 2.47 |
| 5 | ()/\<\(// | ()/\<\(// | Yes | 12.57 |
| 6 | _ )<(<(_< | _ )<(<(_ | No | 2.8 |
| 7 | _<\<\</_( | _<\<\</_( | Yes | 3.29 |
| 8 | \/\\/(((< | \/\\/((( | No | 3.15 |
| 9 | )\_<)\))( | )\_<)\))( | Yes | 2.9 |
| 10 | ())_ / _( | ())_ / _( | Yes | 3.38 |
| 11 | / /()_/<< | / /()_/< | No | 6.26 |
| 12 | ) )()((/( | ) )()((/( | Yes | 3.63 |
| 13 | (/\</\/__ | (/\</\/__ | Yes | 15.78 |
| 14 | \/)<)\)_  | \/)<)\)_ | No | 2.92 |
| 15 | (/\ _)/\/ | (/\ _)/\/ | Yes | 3.26 |
| 16 | _<_)__ __ | _<_)__ __ | Yes | 4.95 |
| 17 | )/\_  ((_ | )/\_  ((_ | Yes | 3.29 |
| 18 | (() /\/_( | (() /\/_( | Yes | 2.9 |
| 19 | /</(<  (< | /</(<  ( | No | 3.41 |
| 20 | )_<\ <)/) | )_<\ <)/) | Yes | 3.18 |
