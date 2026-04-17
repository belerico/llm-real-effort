# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-26 15:42:23

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
| sudoku_game | 4667 | 36307 | 40974 | 4 | 16 | 20.28 | 405.67 |
| add_numbers | 2420 | 984 | 3404 | 20 | 0 | 3.07 | 61.4 |
| counting_zeros | 3820 | 16431 | 20251 | 12 | 8 | 8.24 | 164.76 |
| task_decoding | 3760 | 2691 | 6451 | 20 | 0 | 4.43 | 88.58 |
| task_summation | 4100 | 6428 | 10528 | 20 | 0 | 5.50 | 110.01 |
| task_transcription | 2566 | 2155 | 4721 | 20 | 0 | 3.11 | 62.15 |
| task_sequences | 2420 | 4728 | 7148 | 19 | 1 | 5.49 | 109.78 |
| string_entry | 2846 | 27209 | 30055 | 11 | 9 | 17.86 | 357.21 |
| **TOTAL** | **26599** | **96933** | **123532** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 4 4 3 1 5 4 5 1 6 2 3 5 2 |  | No | 16.15 |
| 2 | 6 3 2 1 2 5 6 6 1 4 5 1 2 6 | 6 3 2 1 2 5 6 6 1 4 5 1 2 6 | Yes | 12.72 |
| 3 | 5 6 4 3 3 5 2 4 1 3 2 1 1 6 | 5 3 4 6 3 5 2 4 1 3 2 1 1 6 | No | 11.33 |
| 4 | 5 3 4 1 4 3 1 3 6 2 3 5 1 6 | 5 3 4 1 4 3 3 1 6 2 1 5 3 6 | No | 8.13 |
| 5 | 5 4 6 3 1 2 3 5 1 5 6 5 2 4 |  | No | 23.01 |
| 6 | 4 2 5 1 4 3 4 1 4 5 3 4 2 5 |  | No | 34.87 |
| 7 | 5 1 2 4 2 3 2 6 4 3 5 6 3 5 |  | No | 21.25 |
| 8 | 1 4 3 3 6 2 2 3 5 6 3 6 1 6 |  | No | 22.62 |
| 9 | 6 5 4 2 3 5 2 5 6 5 6 1 4 3 | 6 5 4 2 3 5 2 5 6 5 6 1 4 3 | Yes | 11.41 |
| 10 | 6 4 5 1 6 2 4 2 2 3 6 3 5 4 |  | No | 20.83 |
| 11 | 5 4 1 3 6 6 5 5 2 6 5 5 3 1 |  | No | 26.87 |
| 12 | 6 1 5 1 4 5 2 2 5 6 3 5 4 1 | 6 1 5 1 4 5 2 2 5 6 3 5 4 1 | Yes | 9.95 |
| 13 | 1 3 1 2 4 1 5 4 2 3 4 4 2 5 |  | No | 32.63 |
| 14 | 2 5 6 6 3 1 4 6 1 3 5 4 6 3 |  | No | 25.54 |
| 15 | 3 6 2 4 2 3 2 1 6 5 6 4 5 6 |  | No | 26.12 |
| 16 | 5 3 6 1 5 4 1 5 6 6 2 5 3 4 |  | No | 25.31 |
| 17 | 5 2 4 3 4 1 6 2 6 5 1 4 5 6 |  | No | 26.84 |
| 18 | 2 3 5 1 3 4 3 4 1 4 1 4 1 5 |  | No | 18.3 |
| 19 | 5 3 4 2 1 1 6 5 5 6 1 3 2 3 | 5 3 4 2 1 1 6 5 5 6 1 3 2 3 | Yes | 13.64 |
| 20 | 6 3 1 6 3 3 2 5 4 3 1 2 6 2 |  | No | 18.12 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2525 | 2525 | Yes | 3.33 |
| 2 | 2017 | 2017 | Yes | 2.94 |
| 3 | 1468 | 1468 | Yes | 3.08 |
| 4 | 940 | 940 | Yes | 3.79 |
| 5 | 1853 | 1853 | Yes | 3.45 |
| 6 | 1041 | 1041 | Yes | 2.61 |
| 7 | 1623 | 1623 | Yes | 2.55 |
| 8 | 956 | 956 | Yes | 4.12 |
| 9 | 1444 | 1444 | Yes | 3.1 |
| 10 | 1915 | 1915 | Yes | 3.02 |
| 11 | 1541 | 1541 | Yes | 3.08 |
| 12 | 1109 | 1109 | Yes | 3.31 |
| 13 | 1663 | 1663 | Yes | 2.86 |
| 14 | 1344 | 1344 | Yes | 2.63 |
| 15 | 1331 | 1331 | Yes | 2.87 |
| 16 | 1411 | 1411 | Yes | 2.57 |
| 17 | 2011 | 2011 | Yes | 2.87 |
| 18 | 825 | 825 | Yes | 3.24 |
| 19 | 1532 | 1532 | Yes | 3.26 |
| 20 | 2036 | 2036 | Yes | 2.71 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 57 | 57 | Yes | 7.87 |
| 2 | 62 | 62 | Yes | 9.87 |
| 3 | 48 | 47 | No | 10.12 |
| 4 | 68 | 75 | No | 5.14 |
| 5 | 60 | 60 | Yes | 9.14 |
| 6 | 71 | 70 | No | 9.91 |
| 7 | 65 | 65 | Yes | 8.46 |
| 8 | 63 | 64 | No | 4.59 |
| 9 | 56 | 56 | Yes | 8.28 |
| 10 | 51 | 50 | No | 10.27 |
| 11 | 60 | 60 | Yes | 6.05 |
| 12 | 64 | 63 | No | 13.66 |
| 13 | 66 | 65 | No | 6.47 |
| 14 | 67 | 67 | Yes | 5.36 |
| 15 | 48 | 48 | Yes | 8.29 |
| 16 | 70 | 70 | Yes | 10.12 |
| 17 | 58 | 57 | No | 4.78 |
| 18 | 36 | 36 | Yes | 9.38 |
| 19 | 57 | 57 | Yes | 8.08 |
| 20 | 40 | 40 | Yes | 8.92 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | YAQLVNZ | YAQLVNZ | Yes | 4.46 |
| 2 | SKYHZAD | SKYHZAD | Yes | 5.43 |
| 3 | QWZCSKO | QWZCSKO | Yes | 4.13 |
| 4 | GCOSBND | GCOSBND | Yes | 4.46 |
| 5 | RGPJUCA | RGPJUCA | Yes | 4.08 |
| 6 | RGXISWJ | RGXISWJ | Yes | 3.8 |
| 7 | VQLBAGD | VQLBAGD | Yes | 4.23 |
| 8 | CGRMVSH | CGRMVSH | Yes | 3.79 |
| 9 | TNBKAXM | TNBKAXM | Yes | 5.08 |
| 10 | BZCNDEU | BZCNDEU | Yes | 4.07 |
| 11 | QJGPMUX | QJGPMUX | Yes | 4.95 |
| 12 | MDBRSJH | MDBRSJH | Yes | 3.82 |
| 13 | ZBWTQXA | ZBWTQXA | Yes | 6.34 |
| 14 | PDVMCTL | PDVMCTL | Yes | 4.02 |
| 15 | RPMECZI | RPMECZI | Yes | 4.1 |
| 16 | UZOTYGN | UZOTYGN | Yes | 5.0 |
| 17 | FAEQPNV | FAEQPNV | Yes | 4.12 |
| 18 | BZLEPKC | BZLEPKC | Yes | 3.8 |
| 19 | RHGXMFD | RHGXMFD | Yes | 4.91 |
| 20 | EVOXDIW | EVOXDIW | Yes | 4.0 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.2, 7.8] | 7.8 2.2 | Yes | 6.03 |
| 2 | [3.6, 6.4] | 6.4 3.6 | Yes | 5.08 |
| 3 | [0.7, 9.3] | 9.3 0.7 | Yes | 5.7 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 5.28 |
| 5 | [2.6, 7.4] | 2.6 7.4 | Yes | 4.51 |
| 6 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.2 |
| 7 | [4.9, 5.1] | 4.9 5.1 | Yes | 4.91 |
| 8 | [3.7, 6.3] | 6.3 3.7 | Yes | 5.42 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 8.53 |
| 10 | [1.5, 8.5] | 1.5 8.5 | Yes | 8.05 |
| 11 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.09 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.91 |
| 13 | [0.5, 9.5] | 9.5 0.5 | Yes | 3.69 |
| 14 | [3.5, 6.5] | 6.5 3.5 | Yes | 5.82 |
| 15 | [3.4, 6.6] | 3.4 6.6 | Yes | 3.17 |
| 16 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.5 |
| 17 | [1.5, 8.5] | 1.5 8.5 | Yes | 4.56 |
| 18 | [2.0, 8.0] | 2.0 8.0 | Yes | 5.66 |
| 19 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.18 |
| 20 | [3.8, 6.2] | 6.2 3.8 | Yes | 4.72 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7IVP0FBKDKCZ | 7IVP0FBKDKCZ | Yes | 2.95 |
| 2 | YSQ3SJJX7ZQT | YSQ3SJJX7ZQT | Yes | 3.7 |
| 3 | LZ69CWFQKGWU | LZ69CWFQKGWU | Yes | 3.29 |
| 4 | A5M66Z0ZPE09 | A5M66Z0ZPE09 | Yes | 1.84 |
| 5 | 1NHJTW2BDWLL | 1NHJTW2BDWLL | Yes | 4.02 |
| 6 | YRUHPHL8HDAY | YRUHPHL8HDAY | Yes | 3.13 |
| 7 | 2YYSQH4DFSV3 | 2YYSQH4DFSV3 | Yes | 1.45 |
| 8 | PFCUNBLXRO0Y | PFCUNBLXRO0Y | Yes | 3.69 |
| 9 | U7JGDH2JYMWG | U7JGDH2JYMWG | Yes | 3.2 |
| 10 | QJVRFDPLYDGV | QJVRFDPLYDGV | Yes | 3.34 |
| 11 | MPSWIG7YA61S | MPSWIG7YA61S | Yes | 2.83 |
| 12 | 48RDJVJJ2QZ2 | 48RDJVJJ2QZ2 | Yes | 3.84 |
| 13 | 1JVPPDDC8O5U | 1JVPPDDC8O5U | Yes | 1.52 |
| 14 | EJL3TOY9P3F8 | EJL3TOY9P3F8 | Yes | 3.42 |
| 15 | 74559OL7NRYL | 74559OL7NRYL | Yes | 1.36 |
| 16 | OGQ1OBHTLWWO | OGQ1OBHTLWWO | Yes | 4.42 |
| 17 | GUIW2P49QXBC | GUIW2P49QXBC | Yes | 3.96 |
| 18 | M55DSZN1CDXB | M55DSZN1CDXB | Yes | 2.98 |
| 19 | 0QZOXJK4XW3S | 0QZOXJK4XW3S | Yes | 4.3 |
| 20 | R68LQ57E66GG | R68LQ57E66GG | Yes | 2.91 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 3.1 |
| 2 | 65 | 65 | Yes | 3.42 |
| 3 | 73 | 73 | Yes | 2.99 |
| 4 | 4 | 4 | Yes | 4.02 |
| 5 | 28 | 28 | Yes | 4.44 |
| 6 | 63 | 63 | Yes | 2.98 |
| 7 | 67 | 67 | Yes | 3.61 |
| 8 | 7 | 7 | Yes | 3.19 |
| 9 | 1 | 1 | Yes | 4.78 |
| 10 | 60 | 60 | Yes | 9.6 |
| 11 | 16 | 16 | Yes | 3.9 |
| 12 | 7680 | 7680 | Yes | 5.49 |
| 13 | 1440 | 1440 | Yes | 3.58 |
| 14 | 23 | 23 | Yes | 3.55 |
| 15 | 31 | 31 | Yes | 3.23 |
| 16 | 3 | 3 | Yes | 3.83 |
| 17 | 64 | 64 | Yes | 5.05 |
| 18 | 48 | 48 | Yes | 3.44 |
| 19 | 243 | 243 | Yes | 4.47 |
| 20 | 20 |  | No | 31.11 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ())_)) _) | ())_)) _) | Yes | 3.69 |
| 2 | (\\(</<)( |  | No | 23.41 |
| 3 | /((<)< \\ | /((<)< \\ | Yes | 17.44 |
| 4 | _ \(/\))( | _ \(/\))( | Yes | 3.61 |
| 5 | \/(<_())( |  | No | 28.77 |
| 6 | _</_  (_/ | _</_  (_/ | Yes | 1.94 |
| 7 | \\) )_)<) | \\) )_)<) | Yes | 19.18 |
| 8 | <(_)_)/(( |  | No | 22.25 |
| 9 | \__\_\<\/ | \__\_\<\/ | Yes | 20.68 |
| 10 | <</\)\<   | <</\)\< | No | 21.9 |
| 11 | /<(\(//_\ |  | No | 20.79 |
| 12 | ))</( \<( | ))</( \<( | Yes | 11.55 |
| 13 | (())<)/<  | (())<)/< | No | 8.51 |
| 14 | \< <)(</< | \< <)(</< | Yes | 15.86 |
| 15 | /()(()< _ | /()(()< _ | Yes | 11.17 |
| 16 | /_)_)\/_( | /_)_)\/_( | Yes | 41.62 |
| 17 | ()\_(\ /\ |  | No | 30.72 |
| 18 |  (<<_  )) |  | No | 18.93 |
| 19 | ))))<((   |  | No | 27.03 |
| 20 | __\\<)\/_ | __\\<)\/_ | Yes | 8.15 |
