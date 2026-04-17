# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-27 10:25:30

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
| sudoku_game | 5303 | 40960 | 46263 | 0 | 20 | 39.70 | 794.12 |
| add_numbers | 3060 | 3615 | 6675 | 20 | 0 | 3.02 | 60.33 |
| counting_zeros | 4460 | 40331 | 44791 | 2 | 18 | 29.44 | 588.75 |
| task_decoding | 4400 | 8571 | 12971 | 20 | 0 | 6.28 | 125.52 |
| task_summation | 4503 | 16259 | 20762 | 18 | 2 | 16.68 | 333.65 |
| task_transcription | 3195 | 2930 | 6125 | 20 | 0 | 2.58 | 51.66 |
| task_sequences | 3061 | 16576 | 19637 | 15 | 5 | 11.65 | 233.04 |
| string_entry | 3495 | 32964 | 36459 | 5 | 15 | 19.01 | 380.25 |
| **TOTAL** | **31477** | **162206** | **193683** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 4 2 4 6 5 2 6 3 5 6 3 1 2 |  | No | 40.67 |
| 2 | 3 5 6 3 5 4 3 4 4 3 5 3 2 4 |  | No | 40.95 |
| 3 | 6 1 5 3 4 6 5 4 2 3 6 6 5 2 |  | No | 36.27 |
| 4 | 3 4 1 5 2 2 5 1 2 3 6 4 6 1 |  | No | 39.61 |
| 5 | 4 5 6 1 4 5 6 1 1 2 3 6 5 1 |  | No | 52.54 |
| 6 | 2 5 4 5 2 3 4 1 6 4 6 5 3 1 |  | No | 39.26 |
| 7 | 2 1 4 1 3 6 1 2 5 1 4 3 2 6 |  | No | 42.92 |
| 8 | 5 4 2 2 1 6 3 5 1 5 3 5 4 6 |  | No | 38.89 |
| 9 | 1 4 2 5 4 2 5 4 3 1 6 5 1 2 |  | No | 32.12 |
| 10 | 5 3 6 1 2 5 6 6 1 2 6 3 2 1 |  | No | 33.03 |
| 11 | 6 5 1 5 1 6 3 2 4 6 1 2 4 3 |  | No | 41.0 |
| 12 | 4 5 6 5 2 4 3 4 5 1 3 5 6 3 |  | No | 36.21 |
| 13 | 6 3 5 6 2 5 6 3 5 4 1 2 1 4 |  | No | 38.2 |
| 14 | 2 3 4 2 3 5 4 1 6 4 3 5 6 6 |  | No | 43.97 |
| 15 | 3 1 1 2 5 3 6 2 3 5 2 6 3 1 |  | No | 42.36 |
| 16 | 2 3 6 6 3 5 4 6 3 4 3 5 1 1 |  | No | 37.85 |
| 17 | 2 3 5 6 2 5 4 5 3 6 2 1 3 5 |  | No | 37.76 |
| 18 | 5 1 3 1 5 3 1 4 6 4 5 2 4 3 |  | No | 33.91 |
| 19 | 5 2 2 5 1 1 3 2 6 1 4 2 6 3 |  | No | 30.67 |
| 20 | 1 6 2 3 1 5 4 2 1 2 1 5 1 2 |  | No | 55.9 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1557 | 1557 | Yes | 1.83 |
| 2 | 2051 | 2051 | Yes | 2.08 |
| 3 | 1695 | 1695 | Yes | 2.38 |
| 4 | 1991 | 1991 | Yes | 3.21 |
| 5 | 1454 | 1454 | Yes | 3.04 |
| 6 | 2334 | 2334 | Yes | 3.38 |
| 7 | 1118 | 1118 | Yes | 1.92 |
| 8 | 1953 | 1953 | Yes | 2.89 |
| 9 | 2491 | 2491 | Yes | 5.14 |
| 10 | 1850 | 1850 | Yes | 4.15 |
| 11 | 2033 | 2033 | Yes | 2.76 |
| 12 | 1169 | 1169 | Yes | 2.73 |
| 13 | 1313 | 1313 | Yes | 2.85 |
| 14 | 800 | 800 | Yes | 2.84 |
| 15 | 1428 | 1428 | Yes | 3.48 |
| 16 | 2115 | 2115 | Yes | 3.09 |
| 17 | 1260 | 1260 | Yes | 3.11 |
| 18 | 2011 | 2011 | Yes | 4.02 |
| 19 | 1950 | 1950 | Yes | 2.31 |
| 20 | 1689 | 1689 | Yes | 3.11 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 68 |  | No | 35.22 |
| 2 | 58 |  | No | 18.07 |
| 3 | 39 |  | No | 30.55 |
| 4 | 73 |  | No | 22.92 |
| 5 | 75 |  | No | 37.68 |
| 6 | 47 |  | No | 43.19 |
| 7 | 52 | 52 | Yes | 29.47 |
| 8 | 43 | 43 | Yes | 22.81 |
| 9 | 35 |  | No | 39.0 |
| 10 | 72 |  | No | 28.46 |
| 11 | 46 |  | No | 41.62 |
| 12 | 73 |  | No | 32.06 |
| 13 | 73 |  | No | 37.61 |
| 14 | 72 |  | No | 37.32 |
| 15 | 63 |  | No | 26.84 |
| 16 | 48 |  | No | 18.74 |
| 17 | 50 |  | No | 19.66 |
| 18 | 54 |  | No | 21.31 |
| 19 | 65 |  | No | 23.87 |
| 20 | 74 |  | No | 22.32 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VLZTAQD | VLZTAQD | Yes | 3.57 |
| 2 | BEDRPLS | BEDRPLS | Yes | 8.64 |
| 3 | OKBZWLA | OKBZWLA | Yes | 9.54 |
| 4 | VMTGSUI | VMTGSUI | Yes | 5.18 |
| 5 | GKXDFYV | GKXDFYV | Yes | 3.83 |
| 6 | WKNMHOT | WKNMHOT | Yes | 14.95 |
| 7 | WKAHEMR | WKAHEMR | Yes | 9.41 |
| 8 | DCGKZMX | DCGKZMX | Yes | 4.66 |
| 9 | ORWDJNF | ORWDJNF | Yes | 8.34 |
| 10 | UWNLPBX | UWNLPBX | Yes | 3.32 |
| 11 | ATHGDJO | ATHGDJO | Yes | 6.02 |
| 12 | WDBCMVT | WDBCMVT | Yes | 7.92 |
| 13 | IEMZJCB | IEMZJCB | Yes | 7.18 |
| 14 | DAVEHOS | DAVEHOS | Yes | 4.35 |
| 15 | TXROPJC | TXROPJC | Yes | 4.02 |
| 16 | RSEHNTQ | RSEHNTQ | Yes | 9.41 |
| 17 | QAIPTDN | QAIPTDN | Yes | 4.08 |
| 18 | VSEDNQI | VSEDNQI | Yes | 4.81 |
| 19 | KPAETZB | KPAETZB | Yes | 3.54 |
| 20 | HFYTIVL | HFYTIVL | Yes | 2.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | TIMEOUT | No | 120.02 |
| 2 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.38 |
| 3 | [1.1, 8.9] | 8.9 1.1 | Yes | 9.57 |
| 4 | [4.0, 6.0] | 4.0 6.0 | Yes | 11.97 |
| 5 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.49 |
| 6 | [4.8, 5.2] | 5.2 4.8 | Yes | 10.95 |
| 7 | [0.5, 9.5] | 9.5 0.5 | Yes | 12.93 |
| 8 | [2.4, 7.6] | 7.6 2.4 | Yes | 15.04 |
| 9 | [0.9, 9.1] | 0.9 9.1 | Yes | 8.88 |
| 10 | [4.9, 5.1] |  | No | 23.17 |
| 11 | [2.5, 7.5] | 7.5 2.5 | Yes | 9.39 |
| 12 | [1.1, 8.9] | 8.9 1.1 | Yes | 11.03 |
| 13 | [0.8, 9.2] | 0.8 9.2 | Yes | 10.55 |
| 14 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.06 |
| 15 | [2.0, 8.0] | 2.0 8.0 | Yes | 9.89 |
| 16 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.14 |
| 17 | [2.3, 7.7] | 2.3 7.7 | Yes | 10.71 |
| 18 | [5.0, 5.0] | 5.0 5.0 | Yes | 11.66 |
| 19 | [3.3, 6.7] | 3.3 6.7 | Yes | 11.65 |
| 20 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.17 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | UW7Q2UYJJWL2 | UW7Q2UYJJWL2 | Yes | 2.41 |
| 2 | AOYLMRQN4DER | AOYLMRQN4DER | Yes | 2.75 |
| 3 | 023XV3JX2ZGR | 023XV3JX2ZGR | Yes | 2.12 |
| 4 | E2X6VSRGQQCW | E2X6VSRGQQCW | Yes | 3.39 |
| 5 | KRTIUUFEM05J | KRTIUUFEM05J | Yes | 2.05 |
| 6 | CD7ML6Q8DNHC | CD7ML6Q8DNHC | Yes | 1.98 |
| 7 | EMBFB7190K36 | EMBFB7190K36 | Yes | 2.37 |
| 8 | 74WHVX67OIJ8 | 74WHVX67OIJ8 | Yes | 2.07 |
| 9 | RAU3LSLCFP4W | RAU3LSLCFP4W | Yes | 5.09 |
| 10 | S9HPRW7E9YGD | S9HPRW7E9YGD | Yes | 2.2 |
| 11 | OSTFN3770PI1 | OSTFN3770PI1 | Yes | 2.19 |
| 12 | RN1PNZV4DQH3 | RN1PNZV4DQH3 | Yes | 2.01 |
| 13 | NHNQC4MTNSNA | NHNQC4MTNSNA | Yes | 2.32 |
| 14 | 6XAZCTYSXLQN | 6XAZCTYSXLQN | Yes | 3.32 |
| 15 | 12MOPX9VNN2I | 12MOPX9VNN2I | Yes | 3.84 |
| 16 | BACS1XVUUDLE | BACS1XVUUDLE | Yes | 2.02 |
| 17 | JWWFEKXO9GD5 | JWWFEKXO9GD5 | Yes | 2.85 |
| 18 | VAP3309TA1J7 | VAP3309TA1J7 | Yes | 2.36 |
| 19 | VFXBZRC5NSCP | VFXBZRC5NSCP | Yes | 1.81 |
| 20 | WHS4CUORRM8W | WHS4CUORRM8W | Yes | 2.52 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 42 | No | 8.81 |
| 2 | 1440 | 1440 | Yes | 12.64 |
| 3 | 243 | 243 | Yes | 15.42 |
| 4 | 44 | 44 | Yes | 11.26 |
| 5 | 793 | 793 | Yes | 3.9 |
| 6 | 4 | 4 | Yes | 3.44 |
| 7 | 65 | 65 | Yes | 4.11 |
| 8 | 48 | 48 | Yes | 5.51 |
| 9 | 5 | 42 | No | 14.32 |
| 10 | 3 | 3 | Yes | 16.64 |
| 11 | 4096 |  | No | 32.93 |
| 12 | 20 | 20 | Yes | 17.56 |
| 13 | 9 | 9 | Yes | 10.96 |
| 14 | 67 | 67 | Yes | 6.66 |
| 15 | 73 | 73 | Yes | 3.14 |
| 16 | 3 | 3 | Yes | 4.95 |
| 17 | 10 |  | No | 40.71 |
| 18 | 39 | 42 | No | 9.52 |
| 19 | 4 | 4 | Yes | 3.25 |
| 20 | 23 | 23 | Yes | 7.32 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /</)<\<__ |  | No | 20.72 |
| 2 | _<_< _(_  |  | No | 23.22 |
| 3 | ()_\(< /< | ()_\(< /< | Yes | 7.64 |
| 4 | /_\/< </\ | /_\/< </\> | No | 12.77 |
| 5 | /(   )__) | /(   )__) | Yes | 11.03 |
| 6 | <(\<)()<( | /\) <(_<) | No | 10.53 |
| 7 | \__)) < / |  | No | 23.88 |
| 8 | \) (\\/_( |  | No | 22.14 |
| 9 |   //</<\( | //</<\( | No | 15.76 |
| 10 | ()</()/(( |  | No | 39.94 |
| 11 | \<(/\_<_/ |  | No | 17.94 |
| 12 | /()_/(  < | /()_/(  < | Yes | 13.01 |
| 13 | _)\(\( )< |  | No | 24.48 |
| 14 | )// < ( _ |  | No | 23.48 |
| 15 | (<\)_(( _ | /\) <(_<) | No | 11.27 |
| 16 | /(/ _)( ) | /(/ _)( ) | Yes | 20.44 |
| 17 | (()\__/<) |  | No | 48.48 |
| 18 | )< )\_/)  |  | No | 18.95 |
| 19 | _)\<)/<<  | /\) <(_<) | No | 8.55 |
| 20 | //( <<)\< | //( <<)\< | Yes | 6.01 |
