# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-27 10:17:07

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
| sudoku_game | 6474 | 37732 | 44206 | 11 | 9 | 33.17 | 663.39 |
| add_numbers | 3860 | 1615 | 5475 | 20 | 0 | 3.50 | 69.94 |
| counting_zeros | 5180 | 26083 | 31263 | 17 | 3 | 19.43 | 388.69 |
| task_decoding | 5180 | 5417 | 10597 | 20 | 0 | 7.06 | 141.16 |
| task_summation | 5240 | 15189 | 20429 | 20 | 0 | 15.21 | 304.25 |
| task_transcription | 4028 | 2694 | 6722 | 20 | 0 | 6.07 | 121.38 |
| task_sequences | 3921 | 6717 | 10638 | 19 | 1 | 8.92 | 178.44 |
| string_entry | 4382 | 4028 | 8410 | 12 | 8 | 9.90 | 198.03 |
| **TOTAL** | **38265** | **99475** | **137740** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 4 1 1 5 2 5 3 2 2 5 6 4 | 5 6 4 1 1 5 2 5 3 2 2 5 6 4 | Yes | 34.41 |
| 2 | 1 5 4 3 3 1 1 4 1 2 6 5 5 2 | 1 5 4 3 3 1 1 4 1 2 6 5 5 2 | Yes | 25.79 |
| 3 | 6 5 4 2 5 5 6 6 1 3 6 1 3 2 | 6 5 4 2 5 5 6 6 1 3 6 1 3 2 | Yes | 31.07 |
| 4 | 6 5 3 1 5 1 2 3 5 6 4 2 1 5 |  | No | 45.91 |
| 5 | 5 2 1 6 3 2 4 4 5 6 5 4 1 2 | 5 2 1 6 3 4 2 4 5 6 5 2 1 4 | No | 29.9 |
| 6 | 2 1 6 3 1 5 3 6 2 5 3 6 3 2 |  | No | 40.73 |
| 7 | 5 1 6 5 4 5 4 1 2 5 3 3 4 1 | 5 1 6 5 4 5 4 1 2 5 3 3 4 1 | Yes | 35.72 |
| 8 | 6 4 2 5 3 2 1 5 2 4 3 5 2 4 | 6 4 2 5 3 2 1 5 2 4 5 3 5 2 4 | No | 36.18 |
| 9 | 1 6 2 4 1 4 3 1 3 1 5 6 5 2 | 1 6 2 4 1 4 3 1 3 1 5 6 5 2 | Yes | 18.98 |
| 10 | 1 5 2 6 1 3 6 5 4 6 3 2 4 1 |  | No | 43.74 |
| 11 | 2 3 1 4 6 5 5 3 4 2 1 6 3 1 | 2 3 1 4 6 5 5 3 4 2 1 6 3 1 | Yes | 26.92 |
| 12 | 3 4 2 1 6 3 4 5 1 6 3 3 1 1 |  | No | 41.31 |
| 13 | 6 3 1 5 5 3 6 2 1 2 3 1 3 4 | 6 3 1 5 5 3 6 2 1 2 3 1 3 4 | Yes | 22.89 |
| 14 | 5 2 6 6 2 4 5 2 6 6 2 2 1 3 |  | No | 27.77 |
| 15 | 5 1 3 2 4 1 6 2 3 6 5 6 1 2 | 5 1 3 2 4 1 6 2 3 6 5 6 1 2 | Yes | 25.0 |
| 16 | 5 5 1 4 2 3 1 4 5 6 2 3 2 1 | 5 5 1 4 2 3 1 4 5 6 2 3 2 1 | Yes | 43.15 |
| 17 | 2 6 1 2 1 5 3 5 2 6 1 2 4 3 |  | No | 37.87 |
| 18 | 1 4 3 5 2 4 1 2 4 6 5 3 1 3 | 1 4 3 5 2 4 1 2 4 6 5 3 1 3 | Yes | 32.72 |
| 19 | 1 4 6 3 1 4 5 5 4 3 1 5 4 3 | 1 4 6 3 1 4 5 5 4 3 1 5 4 3 | Yes | 30.81 |
| 20 | 6 5 3 6 5 4 1 1 2 6 2 5 4 6 |  | No | 32.49 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1879 | 1879 | Yes | 2.72 |
| 2 | 1195 | 1195 | Yes | 2.68 |
| 3 | 1329 | 1329 | Yes | 2.77 |
| 4 | 1599 | 1599 | Yes | 3.76 |
| 5 | 1823 | 1823 | Yes | 3.93 |
| 6 | 1695 | 1695 | Yes | 5.0 |
| 7 | 432 | 432 | Yes | 2.87 |
| 8 | 2206 | 2206 | Yes | 4.34 |
| 9 | 1557 | 1557 | Yes | 2.63 |
| 10 | 1576 | 1576 | Yes | 4.36 |
| 11 | 1890 | 1890 | Yes | 4.66 |
| 12 | 2006 | 2006 | Yes | 5.1 |
| 13 | 1162 | 1162 | Yes | 2.48 |
| 14 | 2342 | 2342 | Yes | 2.7 |
| 15 | 1503 | 1503 | Yes | 2.84 |
| 16 | 1127 | 1127 | Yes | 3.27 |
| 17 | 1641 | 1641 | Yes | 2.31 |
| 18 | 1330 | 1330 | Yes | 2.56 |
| 19 | 1247 | 1247 | Yes | 3.66 |
| 20 | 1947 | 1947 | Yes | 5.29 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 45 | No | 16.53 |
| 2 | 42 | 42 | Yes | 20.34 |
| 3 | 48 | 48 | Yes | 18.15 |
| 4 | 53 | 53 | Yes | 30.01 |
| 5 | 51 | 51 | Yes | 17.05 |
| 6 | 72 | 71 | No | 21.07 |
| 7 | 50 | 50 | Yes | 17.84 |
| 8 | 55 | 55 | Yes | 23.52 |
| 9 | 68 | 68 | Yes | 20.89 |
| 10 | 67 | 67 | Yes | 16.39 |
| 11 | 44 | 44 | Yes | 21.9 |
| 12 | 36 | 36 | Yes | 16.05 |
| 13 | 40 | 40 | Yes | 18.43 |
| 14 | 68 | 68 | Yes | 19.56 |
| 15 | 65 | 65 | Yes | 19.04 |
| 16 | 45 | 45 | Yes | 17.35 |
| 17 | 71 | 70 | No | 17.19 |
| 18 | 66 | 66 | Yes | 20.06 |
| 19 | 53 | 53 | Yes | 18.6 |
| 20 | 38 | 38 | Yes | 18.7 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GTVQOPJ | GTVQOPJ | Yes | 5.28 |
| 2 | VLKGAQC | VLKGAQC | Yes | 5.22 |
| 3 | JIMNDYT | JIMNDYT | Yes | 13.8 |
| 4 | JTQHIOR | JTQHIOR | Yes | 5.77 |
| 5 | WSGCRNT | WSGCRNT | Yes | 6.42 |
| 6 | UJXBSTI | UJXBSTI | Yes | 10.58 |
| 7 | OXKUEDJ | OXKUEDJ | Yes | 15.21 |
| 8 | MFOQKJI | MFOQKJI | Yes | 7.12 |
| 9 | AJCBIUT | AJCBIUT | Yes | 5.33 |
| 10 | SEMKZRX | SEMKZRX | Yes | 4.46 |
| 11 | BCGXTSF | BCGXTSF | Yes | 6.25 |
| 12 | QSOMPCU | QSOMPCU | Yes | 5.6 |
| 13 | BYHWTUK | BYHWTUK | Yes | 6.36 |
| 14 | HSBFGQD | HSBFGQD | Yes | 4.76 |
| 15 | CZRQLWX | CZRQLWX | Yes | 5.72 |
| 16 | BGPMIYE | BGPMIYE | Yes | 5.89 |
| 17 | NRJGDUK | NRJGDUK | Yes | 5.22 |
| 18 | ILCBTDF | ILCBTDF | Yes | 12.87 |
| 19 | RVFOTJK | RVFOTJK | Yes | 4.27 |
| 20 | ERCOXUZ | ERCOXUZ | Yes | 5.01 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.6, 5.4] | 5.4 4.6 | Yes | 13.87 |
| 2 | [4.1, 5.9] | 5.9 4.1 | Yes | 19.66 |
| 3 | [0.8, 9.2] | 9.2 0.8 | Yes | 12.17 |
| 4 | [1.6, 8.4] | 1.6 8.4 | Yes | 16.47 |
| 5 | [3.3, 6.7] | 3.3 6.7 | Yes | 11.22 |
| 6 | [0.8, 9.2] | 9.2 0.8 | Yes | 17.51 |
| 7 | [2.5, 7.5] | 2.5 7.5 | Yes | 7.93 |
| 8 | [0.7, 9.3] | 9.3 0.7 | Yes | 27.27 |
| 9 | [2.0, 8.0] | 2.0 8.0 | Yes | 17.23 |
| 10 | [3.3, 6.7] | 6.7 3.3 | Yes | 9.11 |
| 11 | [1.0, 9.0] | 1.0 9.0 | Yes | 17.43 |
| 12 | [4.4, 5.6] | 5.6 4.4 | Yes | 11.43 |
| 13 | [1.7, 8.3] | 1.7 8.3 | Yes | 16.88 |
| 14 | [0.4, 9.6] | 9.6 0.4 | Yes | 18.88 |
| 15 | [0.7, 9.3] | 9.3 0.7 | Yes | 14.22 |
| 16 | [1.1, 8.9] | 8.9 1.1 | Yes | 20.0 |
| 17 | [3.9, 6.1] | 3.9 6.1 | Yes | 11.2 |
| 18 | [0.7, 9.3] | 0.7 9.3 | Yes | 15.4 |
| 19 | [0.3, 9.7] | 9.7 0.3 | Yes | 18.2 |
| 20 | [5.0, 5.0] | 5.0 5.0 | Yes | 8.15 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KOK9KSR016P3 | KOK9KSR016P3 | Yes | 5.92 |
| 2 | 5T4VVL17KGQT | 5T4VVL17KGQT | Yes | 3.3 |
| 3 | M13EYOR2BP07 | M13EYOR2BP07 | Yes | 4.72 |
| 4 | 9KI5C8XQRHKQ | 9KI5C8XQRHKQ | Yes | 3.59 |
| 5 | GQUQEFZG2AV8 | GQUQEFZG2AV8 | Yes | 6.13 |
| 6 | 4TU4YNPIC952 | 4TU4YNPIC952 | Yes | 12.44 |
| 7 | PPECFMX7ZKS8 | PPECFMX7ZKS8 | Yes | 4.15 |
| 8 | T9CUYTR4YGT6 | T9CUYTR4YGT6 | Yes | 5.36 |
| 9 | 0SEKTXD10JSD | 0SEKTXD10JSD | Yes | 12.96 |
| 10 | VMPD7YKMORUT | VMPD7YKMORUT | Yes | 3.24 |
| 11 | NBOJDPN6SWHI | NBOJDPN6SWHI | Yes | 6.07 |
| 12 | LRCBL1E9VDF2 | LRCBL1E9VDF2 | Yes | 3.97 |
| 13 | 9BTE8JVP0IC6 | 9BTE8JVP0IC6 | Yes | 10.17 |
| 14 | BLTRGK3PKCZA | BLTRGK3PKCZA | Yes | 5.09 |
| 15 | 6NMDWOSYVCJ6 | 6NMDWOSYVCJ6 | Yes | 6.47 |
| 16 | HNXZCFGD2GNF | HNXZCFGD2GNF | Yes | 12.61 |
| 17 | GK7UT2Q6FICF | GK7UT2Q6FICF | Yes | 4.69 |
| 18 | UPCHCWV757JJ | UPCHCWV757JJ | Yes | 3.27 |
| 19 | F4Z23CZGH6UH | F4Z23CZGH6UH | Yes | 4.01 |
| 20 | F8U6G5ZV6DF3 | F8U6G5ZV6DF3 | Yes | 3.22 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 10 | 10 | Yes | 15.54 |
| 2 | 73 | 73 | Yes | 6.13 |
| 3 | 64 | 64 | Yes | 5.58 |
| 4 | 7 | 7 | Yes | 3.85 |
| 5 | 198 | 198 | Yes | 10.88 |
| 6 | 6 | 6 | Yes | 6.73 |
| 7 | 28 | 28 | Yes | 4.54 |
| 8 | 67 | 67 | Yes | 8.56 |
| 9 | 20 | 20 | Yes | 18.51 |
| 10 | 39 | 39 | Yes | 5.31 |
| 11 | 60 | 60 | Yes | 4.94 |
| 12 | 4096 | 16384 | No | 14.68 |
| 13 | 16 | 16 | Yes | 7.89 |
| 14 | 4 | 4 | Yes | 4.97 |
| 15 | 5 | 5 | Yes | 7.37 |
| 16 | 36 | 36 | Yes | 9.16 |
| 17 | 48 | 48 | Yes | 4.88 |
| 18 | 9 | 9 | Yes | 15.55 |
| 19 | 19 | 19 | Yes | 14.28 |
| 20 | 793 | 793 | Yes | 9.08 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _()/<)\\< | _()/<)\\ | No | 4.87 |
| 2 | <<</)<\/< | <<</)<\/ | No | 5.74 |
| 3 | ()<<(//_< | ()<<(//_ | No | 3.55 |
| 4 | ) ))<)/// | ) ))<)/// | Yes | 14.26 |
| 5 |   //)_ _  | //)_ _ | No | 7.04 |
| 6 | /__/((\<\ | /__/((\<\ | Yes | 3.3 |
| 7 | )_\<)__<_ | )_\<)__<_ | Yes | 10.04 |
| 8 |  \/)_/< / | \/)_/< / | No | 16.6 |
| 9 | \)( <<(<_ | \)( <<(<_ | Yes | 14.21 |
| 10 | ((//\ ()< | ((//\ () | No | 4.8 |
| 11 | _)_\/ //) | _)_\/ //) | Yes | 14.21 |
| 12 | )<( <)<)  | )<( <)<) | No | 14.87 |
| 13 | _ _</_/)_ | _ _</_/)_ | Yes | 4.5 |
| 14 | (<<))_/)/ | (<<))_/)/ | Yes | 13.2 |
| 15 | ((_\ )\)( | ((_\ )\)( | Yes | 13.83 |
| 16 | \  /<\ /\ | \  /<\ /\ | Yes | 14.41 |
| 17 | _(\_/)\__ | _(\_/)\__ | Yes | 13.3 |
| 18 | _ (<_< _  | _ (<_< _ | No | 8.08 |
| 19 | \_()/(\_) | \_()/(\_) | Yes | 3.97 |
| 20 | / <<<\ _\ | / <<<\ _\ | Yes | 13.25 |
