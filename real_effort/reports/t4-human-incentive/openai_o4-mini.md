# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
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
| sudoku_game | 9060 | 40960 | 50020 | 0 | 20 | 40.54 | 811.0 |
| add_numbers | 4580 | 4470 | 9050 | 20 | 0 | 4.14 | 82.99 |
| counting_zeros | 8000 | 40606 | 48606 | 0 | 20 | 31.08 | 621.88 |
| task_decoding | 16040 | 20817 | 36857 | 18 | 2 | 15.18 | 303.74 |
| task_summation | 9260 | 17341 | 26601 | 20 | 0 | 9.62 | 192.57 |
| task_transcription | 4275 | 8695 | 12970 | 13 | 7 | 5.60 | 112.03 |
| task_sequences | 3240 | 14540 | 17780 | 17 | 3 | 10.33 | 206.69 |
| **TOTAL** | **54455** | **147429** | **201884** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 5 5 4 1 6 4 2 4 2 3 4 1 |  | No | 41.36 |
| 2 | 6 3 2 1 3 3 2 6 4 2 5 6 1 2 |  | No | 44.02 |
| 3 | 3 2 6 3 1 4 4 2 3 4 5 3 6 2 |  | No | 45.57 |
| 4 | 3 6 3 6 2 5 1 5 3 4 1 6 1 3 |  | No | 26.81 |
| 5 | 5 3 2 5 3 2 5 5 3 4 2 5 6 1 |  | No | 49.09 |
| 6 | 2 4 3 1 2 5 6 6 3 5 1 6 3 2 |  | No | 33.82 |
| 7 | 6 3 1 2 6 1 5 1 6 3 5 1 2 5 |  | No | 48.4 |
| 8 | 6 3 4 5 1 1 4 6 5 3 1 2 3 4 |  | No | 46.17 |
| 9 | 2 3 6 2 5 4 6 2 2 5 5 5 1 6 |  | No | 43.56 |
| 10 | 4 1 2 1 4 2 6 5 3 2 6 3 2 2 |  | No | 39.78 |
| 11 | 2 5 3 5 3 2 3 1 2 4 3 3 5 6 |  | No | 30.11 |
| 12 | 1 5 6 3 6 2 6 5 2 3 2 6 3 6 |  | No | 47.02 |
| 13 | 4 5 3 6 2 2 5 4 4 1 6 4 2 3 |  | No | 50.69 |
| 14 | 1 2 2 1 3 5 3 5 2 6 4 5 4 2 |  | No | 38.52 |
| 15 | 6 2 5 3 1 4 3 4 1 4 2 4 3 2 |  | No | 47.35 |
| 16 | 1 2 5 4 6 2 1 6 2 5 3 1 6 5 |  | No | 30.2 |
| 17 | 3 2 1 4 5 4 3 6 6 3 4 2 6 5 |  | No | 41.45 |
| 18 | 2 6 4 4 1 2 1 3 4 3 6 1 6 2 |  | No | 32.93 |
| 19 | 4 5 1 5 6 4 2 6 3 1 2 6 2 4 |  | No | 44.52 |
| 20 | 1 5 1 5 3 5 4 3 5 4 3 6 1 4 |  | No | 29.43 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1840 | 1840 | Yes | 4.26 |
| 2 | 1201 | 1201 | Yes | 6.0 |
| 3 | 1747 | 1747 | Yes | 4.9 |
| 4 | 1555 | 1555 | Yes | 2.8 |
| 5 | 1707 | 1707 | Yes | 4.91 |
| 6 | 1059 | 1059 | Yes | 2.13 |
| 7 | 1800 | 1800 | Yes | 6.66 |
| 8 | 2151 | 2151 | Yes | 4.66 |
| 9 | 2138 | 2138 | Yes | 3.59 |
| 10 | 1671 | 1671 | Yes | 8.22 |
| 11 | 1647 | 1647 | Yes | 3.57 |
| 12 | 1711 | 1711 | Yes | 2.69 |
| 13 | 1991 | 1991 | Yes | 2.59 |
| 14 | 1996 | 1996 | Yes | 2.94 |
| 15 | 2122 | 2122 | Yes | 4.01 |
| 16 | 1794 | 1794 | Yes | 3.22 |
| 17 | 1716 | 1716 | Yes | 6.56 |
| 18 | 1629 | 1629 | Yes | 2.76 |
| 19 | 2153 | 2153 | Yes | 2.55 |
| 20 | 1781 | 1781 | Yes | 3.86 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 |  | No | 19.72 |
| 2 | 47 |  | No | 26.98 |
| 3 | 60 |  | No | 44.11 |
| 4 | 52 |  | No | 36.29 |
| 5 | 57 |  | No | 28.09 |
| 6 | 73 |  | No | 55.95 |
| 7 | 45 |  | No | 41.04 |
| 8 | 40 |  | No | 32.32 |
| 9 | 56 | 67 | No | 18.21 |
| 10 | 61 |  | No | 44.45 |
| 11 | 70 |  | No | 53.51 |
| 12 | 49 |  | No | 22.02 |
| 13 | 43 |  | No | 21.28 |
| 14 | 39 |  | No | 28.84 |
| 15 | 38 |  | No | 26.27 |
| 16 | 45 |  | No | 16.55 |
| 17 | 60 |  | No | 25.97 |
| 18 | 58 |  | No | 37.35 |
| 19 | 47 |  | No | 23.55 |
| 20 | 46 |  | No | 19.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GQCAFSE | GQCAFSE | Yes | 6.73 |
| 2 | QOGRKJP | QOGRKJP | Yes | 16.81 |
| 3 | RLGMYCI | RLGMYCI | Yes | 17.39 |
| 4 | FAPNETJ |  | No | 43.26 |
| 5 | NLVREYW | NLVREYW | Yes | 11.53 |
| 6 | YFSTCKO | YFSTCKO | Yes | 7.38 |
| 7 | VRUKSAT | VRUKSAT | Yes | 11.26 |
| 8 | GZJEXTL | GZJEXTL | Yes | 15.75 |
| 9 | MEVFDNO | MEVFDNO | Yes | 12.83 |
| 10 | MOBRFQK | MOBRFQK | Yes | 14.17 |
| 11 | LDFEOTB |  | No | 50.5 |
| 12 | NQYRCDU | NQYRCDU | Yes | 11.74 |
| 13 | NVSORMX | NVSORMX | Yes | 7.61 |
| 14 | YUAPXCG | YUAPXCG | Yes | 4.26 |
| 15 | ACRFXVJ | ACRFXVJ | Yes | 11.88 |
| 16 | KMDNPJH | KMDNPJH | Yes | 9.9 |
| 17 | XFJSEIR | XFJSEIR | Yes | 34.24 |
| 18 | LVXODFC | LVXODFC | Yes | 2.77 |
| 19 | WDPYHJI | WDPYHJI | Yes | 7.53 |
| 20 | ZGMYBRH | ZGMYBRH | Yes | 5.98 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.7, 7.3] | 7.3 2.7 | Yes | 7.36 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.61 |
| 3 | [4.3, 5.7] | 5.7 4.3 | Yes | 8.84 |
| 4 | [0.6, 9.4] | 0.6 9.4 | Yes | 10.05 |
| 5 | [2.2, 7.8] | 7.8 2.2 | Yes | 8.69 |
| 6 | [4.8, 5.2] | 4.8 5.2 | Yes | 6.29 |
| 7 | [2.8, 7.2] | 2.8 7.2 | Yes | 8.44 |
| 8 | [4.2, 5.8] | 4.2 5.8 | Yes | 11.26 |
| 9 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.45 |
| 10 | [2.2, 7.8] | 7.8 2.2 | Yes | 9.63 |
| 11 | [4.4, 5.6] | 5.6 4.4 | Yes | 10.32 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 14.17 |
| 13 | [3.1, 6.9] | 3.1 6.9 | Yes | 8.62 |
| 14 | [4.8, 5.2] | 5.2 4.8 | Yes | 9.41 |
| 15 | [1.5, 8.5] | 8.5 1.5 | Yes | 15.08 |
| 16 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.52 |
| 17 | [0.3, 9.7] | 0.3 9.7 | Yes | 8.5 |
| 18 | [2.0, 8.0] | 2.0 8.0 | Yes | 10.38 |
| 19 | [4.4, 5.6] | 4.4 5.6 | Yes | 7.9 |
| 20 | [2.9, 7.1] | 7.1 2.9 | Yes | 9.86 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AWVKFNYNAF20 | AWVKFNYNAF20 | Yes | 3.08 |
| 2 | 2EDLBWZO4A9A | 2EDLBWZO4A9A | Yes | 4.75 |
| 3 | ISWV4UA07HE4 | ISWV4UA07HE4 | Yes | 3.72 |
| 4 | B6HB0G8CH27S | B6HB0G8CH27S | Yes | 2.33 |
| 5 | 3WT482NYUTOB |  | No | 37.52 |
| 6 | HN1U14NMHOTZ | HN1U14NMHOTZ | Yes | 2.41 |
| 7 | 3L0440B2Z44E | 3L0440BZ244E | No | 2.28 |
| 8 | 6P91OIGZ92GQ | 6P910IGZ92GQ | No | 9.97 |
| 9 | CR4HSEVW4DIE | CR4HSEVV4DIE | No | 7.29 |
| 10 | OI56HAS91QI7 | OI56HAS91Q17 | No | 8.86 |
| 11 | ET2IHAWZJ67Q | ET2IHAWZJ67Q | Yes | 2.62 |
| 12 | H8C14GQDKSSP | H8C14GQDKSSP | Yes | 2.66 |
| 13 | Q2IME0JG2TFF | Q2IME0JG2TFF | Yes | 3.24 |
| 14 | F730V8U5JVKZ | F730V8U5JVKZ | Yes | 2.35 |
| 15 | 1I3ES30L170R | 113ES30L170R | No | 2.17 |
| 16 | QKDK4KW0PMNH | QKDK4KWOPMNH | No | 2.5 |
| 17 | Z9C6OHDXAZRP | Z9C6OHDXAZRP | Yes | 4.91 |
| 18 | RETBG3185F4Y | RETBG3185F4Y | Yes | 2.65 |
| 19 | RJOOHOXZFM2J | RJOOHOXZFM2J | Yes | 3.02 |
| 20 | MG03FE51CK4K | MG03FE51CK4K | Yes | 3.58 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 5.66 |
| 2 | 7680 | 7680 | Yes | 3.67 |
| 3 | 44 | 44 | Yes | 6.68 |
| 4 | 23 | 23 | Yes | 7.27 |
| 5 | 39 | 39 | Yes | 5.37 |
| 6 | 16 | 16 | Yes | 7.9 |
| 7 | 198 | 198 | Yes | 9.25 |
| 8 | 6 | 6 | Yes | 3.26 |
| 9 | 64 | 64 | Yes | 5.36 |
| 10 | 9 | 9 | Yes | 5.16 |
| 11 | 5 |  | No | 33.23 |
| 12 | 1440 | 1440 | Yes | 2.61 |
| 13 | 48 | 48 | Yes | 8.34 |
| 14 | 63 | 63 | Yes | 3.99 |
| 15 | 3 |  | No | 34.82 |
| 16 | 7 | 7 | Yes | 3.9 |
| 17 | 1 | 1 | Yes | 9.29 |
| 18 | 26 |  | No | 38.43 |
| 19 | 31 | 31 | Yes | 4.71 |
| 20 | 9 | 9 | Yes | 7.8 |
