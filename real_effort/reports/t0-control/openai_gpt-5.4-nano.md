# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 11:02:15

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
| sudoku_game | 6720 | 40352 | 47072 | 3 | 17 | 39.61 | 792.34 |
| add_numbers | 3300 | 1744 | 5044 | 20 | 0 | 3.90 | 78.01 |
| counting_zeros | 5720 | 33864 | 39584 | 0 | 20 | 36.01 | 720.56 |
| task_decoding | 11460 | 5018 | 16478 | 20 | 0 | 5.78 | 115.73 |
| task_summation | 6660 | 6164 | 12824 | 20 | 0 | 5.74 | 114.99 |
| task_transcription | 3121 | 11069 | 14190 | 7 | 13 | 7.75 | 155.01 |
| task_sequences | 2420 | 12730 | 15150 | 18 | 2 | 9.25 | 185.02 |
| string_entry | 3720 | 31833 | 35553 | 8 | 12 | 29.15 | 583.02 |
| **TOTAL** | **43121** | **142774** | **185895** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 5 1 4 6 3 1 5 4 5 6 2 3 |  | No | 63.1 |
| 2 | 2 5 1 1 4 6 4 5 2 4 5 4 6 4 |  | No | 45.41 |
| 3 | 3 6 5 6 5 4 2 3 2 3 1 1 2 1 | 3 6 5 6 5 4 2 3 2 3 1 1 2 1 | Yes | 24.71 |
| 4 | 2 1 4 1 5 4 1 6 5 2 3 5 1 6 |  | No | 55.17 |
| 5 | 3 4 2 1 3 4 5 3 6 5 5 2 4 1 | 3 4 2 1 3 4 5 3 6 5 5 2 4 1 | Yes | 22.32 |
| 6 | 5 2 2 5 5 4 1 4 6 6 2 3 5 1 |  | No | 42.62 |
| 7 | 2 1 1 5 6 3 5 6 4 4 2 2 3 1 |  | No | 63.47 |
| 8 | 3 1 2 4 4 2 6 3 1 4 6 5 1 1 |  | No | 50.97 |
| 9 | 1 3 1 3 5 6 3 1 2 5 3 2 5 1 |  | No | 41.48 |
| 10 | 2 6 4 1 2 3 1 2 3 5 2 4 3 6 |  | No | 39.75 |
| 11 | 4 5 1 4 6 3 5 5 2 4 6 1 4 3 |  | No | 20.27 |
| 12 | 1 6 2 5 3 2 5 6 3 5 2 2 3 6 | 1 6 2 5 3 2 5 6 3 5 2 2 3 6 | Yes | 20.68 |
| 13 | 3 4 1 6 5 3 5 5 2 1 3 2 4 1 |  | No | 40.25 |
| 14 | 2 1 6 3 6 3 1 4 2 2 1 6 6 1 |  | No | 39.03 |
| 15 | 6 5 4 5 1 3 1 3 1 6 3 1 3 2 |  | No | 46.32 |
| 16 | 1 3 5 4 4 6 2 1 3 6 4 6 4 1 |  | No | 39.03 |
| 17 | 4 2 3 4 1 4 2 3 6 1 5 6 4 2 |  | No | 43.14 |
| 18 | 2 1 1 3 6 4 2 5 2 6 3 6 1 5 | 2 1 1 3 6 | No | 24.3 |
| 19 | 1 3 4 5 1 6 2 5 3 6 5 2 1 4 |  | No | 43.36 |
| 20 | 5 2 6 6 4 5 1 4 1 2 3 6 1 5 |  | No | 26.77 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2466 | 2466 | Yes | 2.83 |
| 2 | 1825 | 1825 | Yes | 5.61 |
| 3 | 1294 | 1294 | Yes | 5.45 |
| 4 | 2249 | 2249 | Yes | 4.04 |
| 5 | 2031 | 2031 | Yes | 2.36 |
| 6 | 1059 | 1059 | Yes | 4.25 |
| 7 | 1422 | 1422 | Yes | 4.31 |
| 8 | 579 | 579 | Yes | 3.84 |
| 9 | 1121 | 1121 | Yes | 3.8 |
| 10 | 1462 | 1462 | Yes | 3.42 |
| 11 | 2135 | 2135 | Yes | 3.5 |
| 12 | 1522 | 1522 | Yes | 3.83 |
| 13 | 1122 | 1122 | Yes | 3.57 |
| 14 | 1412 | 1412 | Yes | 3.56 |
| 15 | 1387 | 1387 | Yes | 4.26 |
| 16 | 1128 | 1128 | Yes | 3.57 |
| 17 | 1288 | 1288 | Yes | 2.83 |
| 18 | 1112 | 1112 | Yes | 4.24 |
| 19 | 1270 | 1270 | Yes | 4.41 |
| 20 | 2034 | 2034 | Yes | 4.23 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 37 |  | No | 64.41 |
| 2 | 69 |  | No | 55.61 |
| 3 | 40 | 67 | No | 19.33 |
| 4 | 37 |  | No | 54.96 |
| 5 | 47 |  | No | 46.64 |
| 6 | 52 | 67 | No | 15.07 |
| 7 | 63 | 67 | No | 20.86 |
| 8 | 66 | 67 | No | 18.28 |
| 9 | 74 | 67 | No | 19.05 |
| 10 | 54 | 67 | No | 18.76 |
| 11 | 75 |  | No | 58.04 |
| 12 | 37 | 67 | No | 20.3 |
| 13 | 56 |  | No | 44.71 |
| 14 | 39 |  | No | 59.19 |
| 15 | 42 |  | No | 47.55 |
| 16 | 54 | 67 | No | 25.02 |
| 17 | 42 | 40 | No | 20.35 |
| 18 | 73 |  | No | 41.66 |
| 19 | 65 |  | No | 48.84 |
| 20 | 65 | 67 | No | 21.62 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VDCAFZG | VDCAFZG | Yes | 6.45 |
| 2 | VSZYKQX | VSZYKQX | Yes | 6.1 |
| 3 | LVMHENB | LVMHENB | Yes | 6.55 |
| 4 | RETPGLK | RETPGLK | Yes | 5.95 |
| 5 | NMVHDAG | NMVHDAG | Yes | 4.97 |
| 6 | YVJNDCG | YVJNDCG | Yes | 8.09 |
| 7 | YRMODVP | YRMODVP | Yes | 4.1 |
| 8 | DTENRQV | DTENRQV | Yes | 7.15 |
| 9 | JEZXIUG | JEZXIUG | Yes | 5.17 |
| 10 | MLTSZPF | MLTSZPF | Yes | 5.41 |
| 11 | JNDOBPK | JNDOBPK | Yes | 5.84 |
| 12 | ZAIWUOB | ZAIWUOB | Yes | 4.98 |
| 13 | UWBPXCM | UWBPXCM | Yes | 4.8 |
| 14 | VXZTBYW | VXZTBYW | Yes | 4.94 |
| 15 | ZOISNJU | ZOISNJU | Yes | 6.09 |
| 16 | YJLQKFM | YJLQKFM | Yes | 5.26 |
| 17 | CUQVSPH | CUQVSPH | Yes | 6.42 |
| 18 | DMVSQIL | DMVSQIL | Yes | 5.36 |
| 19 | DPMEHJR | DPMEHJR | Yes | 6.34 |
| 20 | NYRQVFD | NYRQVFD | Yes | 5.54 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.2, 9.8] | 9.8 0.2 | Yes | 4.82 |
| 2 | [0.1, 9.9] | 0.1 9.9 | Yes | 5.25 |
| 3 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.07 |
| 4 | [0.6, 9.4] | 0.6 9.4 | Yes | 6.4 |
| 5 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.37 |
| 6 | [0.8, 9.2] | 9.2 0.8 | Yes | 7.28 |
| 7 | [2.5, 7.5] | 2.5 7.5 | Yes | 5.2 |
| 8 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.01 |
| 9 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.93 |
| 10 | [3.9, 6.1] | 3.9 6.1 | Yes | 5.81 |
| 11 | [1.2, 8.8] | 8.8 1.2 | Yes | 5.0 |
| 12 | [2.9, 7.1] | 7.1 2.9 | Yes | 5.77 |
| 13 | [4.4, 5.6] | 5.6 4.4 | Yes | 4.78 |
| 14 | [3.7, 6.3] | 3.7 6.3 | Yes | 4.91 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.07 |
| 16 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.0 |
| 17 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.68 |
| 18 | [1.7, 8.3] | 1.7 8.3 | Yes | 5.25 |
| 19 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.77 |
| 20 | [2.5, 7.5] | 7.5 2.5 | Yes | 6.43 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 22OY5689MLOL | 220Y5689ML0L | No | 7.14 |
| 2 | Q5LR6BOTHURN | Q5LR6BOTHURN | Yes | 7.28 |
| 3 | P7P8AYB1RYOX | P7P8AYB1RYOX | Yes | 2.34 |
| 4 | 9GC48X10VPNU | 9GC48X10VPNIU | No | 8.68 |
| 5 | PQ89Z41XFART | PQ89Z41XFART | Yes | 5.26 |
| 6 | CXP2FFQRULWF | CXP2FFORULWF | No | 4.8 |
| 7 | SVUKZRD4IEJT | SVUKZRD4IEJT | Yes | 4.21 |
| 8 | VT6CJFSF0PN7 | VT6CJFSSFOPN7 | No | 9.16 |
| 9 | K4IYZFQ6DUBI | A3BK7 | No | 5.74 |
| 10 | FVQZTKQA4YJT | FVQZTKQAA4YJT | No | 11.46 |
| 11 | TUZ830EMB8J2 | TUZ830EMB8J2 | Yes | 5.15 |
| 12 | UPPT1DHKN6ZX | UPPT1DHKNGZX | No | 3.65 |
| 13 | 28DOJJHOJSVE | 28DOJJHOJSVE | Yes | 6.64 |
| 14 | 2TKPVDB64H07 | 2TKPVDB64H07 | Yes | 11.67 |
| 15 | AZTZAXWH1UP4 | AZTZAXWH11UP4 | No | 5.43 |
| 16 | PZCR7QKFOHZK | PZCR7OKFOHZK | No | 6.33 |
| 17 | FMSKQW7CSN6R | FMSKOWINCSNGR | No | 12.43 |
| 18 | 9QOUFRRO4NTD | 900UFFBROINTD | No | 18.78 |
| 19 | YNAEF9L6L0TV | YNAEF9L6LOTTV | No | 9.57 |
| 20 | YB0L2GVTIJKX | YBOL2GVTIIJKX | No | 9.19 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 | 3 | Yes | 9.02 |
| 2 | 1 | 1 | Yes | 4.72 |
| 3 | 4 | 4 | Yes | 7.87 |
| 4 | 63 | 63 | Yes | 10.37 |
| 5 | 198 | 198 | Yes | 16.37 |
| 6 | 65 | 65 | Yes | 2.48 |
| 7 | 10 | 8 | No | 8.36 |
| 8 | 48 | 48 | Yes | 8.14 |
| 9 | 6 | 6 | Yes | 11.69 |
| 10 | 5 |  | No | 36.55 |
| 11 | 5 | 5 | Yes | 7.75 |
| 12 | 60 | 60 | Yes | 7.63 |
| 13 | 26 | 26 | Yes | 14.64 |
| 14 | 73 | 73 | Yes | 3.24 |
| 15 | 7680 | 7680 | Yes | 4.48 |
| 16 | 23 | 23 | Yes | 3.95 |
| 17 | 4 | 4 | Yes | 4.92 |
| 18 | 19 | 19 | Yes | 8.39 |
| 19 | 67 | 67 | Yes | 5.2 |
| 20 | 44 | 44 | Yes | 9.23 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \_<\_\ (_ | \_<\_ (_ | No | 20.6 |
| 2 | )(\(\/ /  |  | No | 44.3 |
| 3 | (\)_<\_<( | (\)_<\_<(@ | No | 17.19 |
| 4 |   \<<_) / |  | No | 46.72 |
| 5 | /) _ )_)) |  | No | 31.78 |
| 6 | /<\( ((_< |  | No | 63.14 |
| 7 | \ )<__/<) | \ )<__/<) | Yes | 16.96 |
| 8 | \ (_( <(\ | /\) < | No | 21.75 |
| 9 |  </\)\ (\ | /\) <(_<) | No | 18.09 |
| 10 | _(//__ /\ | _(//__ /\ | Yes | 14.22 |
| 11 | ))</<(<)  | ))</<(<)_ | Yes | 25.04 |
| 12 | \/)(<\_ _ |  | No | 66.12 |
| 13 | (\\/)_)(  |  | No | 57.03 |
| 14 | (( _()(/\ | (( _()(/\ | Yes | 21.32 |
| 15 | )/( )\<(( | )/(_)\<(( | Yes | 27.87 |
| 16 | <(/\<_) ( | <(/\\<_) ( | No | 19.77 |
| 17 | ()\__/_<_ | ()\__/_<_ | Yes | 4.02 |
| 18 | <)\_\/<// | <)\_\/<// | Yes | 20.5 |
| 19 | ( \< ))(( | (_\<_))(( | Yes | 23.08 |
| 20 | (<<(\ <_/ | Answer: | No | 23.46 |
