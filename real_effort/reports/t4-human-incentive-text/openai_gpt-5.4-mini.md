# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-27 10:08:11

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
| sudoku_game | 5500 | 36643 | 42143 | 6 | 14 | 21.94 | 438.78 |
| add_numbers | 3240 | 971 | 4211 | 20 | 0 | 3.20 | 64.08 |
| counting_zeros | 4640 | 16121 | 20761 | 17 | 3 | 8.60 | 171.96 |
| task_decoding | 4580 | 2657 | 7237 | 20 | 0 | 4.26 | 85.11 |
| task_summation | 4757 | 5557 | 10314 | 19 | 1 | 5.11 | 102.25 |
| task_transcription | 3381 | 2396 | 5777 | 20 | 0 | 3.06 | 61.26 |
| task_sequences | 3240 | 3837 | 7077 | 19 | 1 | 5.07 | 101.43 |
| string_entry | 3684 | 32961 | 36645 | 5 | 15 | 24.54 | 490.92 |
| **TOTAL** | **33022** | **101143** | **134165** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 3 3 3 5 2 4 1 4 5 2 1 6 |  | No | 25.84 |
| 2 | 3 5 6 4 1 2 3 2 6 3 2 6 5 1 |  | No | 28.56 |
| 3 | 4 6 2 3 5 3 5 4 6 2 1 4 3 1 | 4 6 2 3 5 3 5 4 6 2 1 4 3 1 | Yes | 17.75 |
| 4 | 4 2 1 3 2 4 3 6 2 2 3 2 1 4 |  | No | 26.63 |
| 5 | 6 5 4 5 1 5 1 2 2 5 5 6 2 3 | 6 5 4 5 1 5 1 2 2 5 5 6 2 3 | Yes | 14.17 |
| 6 | 4 3 2 2 1 4 2 3 4 5 1 2 5 2 | 4 3 2 2 1 4 2 3 4 5 1 2 5 2 | Yes | 13.71 |
| 7 | 4 2 3 3 6 1 5 4 6 2 3 4 2 1 |  | No | 21.61 |
| 8 | 5 4 2 2 3 4 2 5 3 2 6 2 1 5 |  | No | 30.42 |
| 9 | 5 2 6 3 1 3 6 2 6 3 4 5 5 1 |  | No | 24.35 |
| 10 | 6 4 1 3 5 5 4 2 6 1 4 3 5 6 |  | No | 30.35 |
| 11 | 4 2 6 2 3 5 4 6 5 5 2 3 6 1 | 4 2 6 2 3 5 4 6 5 5 2 3 6 1 | Yes | 10.89 |
| 12 | 2 3 4 3 4 5 3 6 6 3 6 4 5 2 |  | No | 25.97 |
| 13 | 3 1 6 5 1 4 6 6 1 5 2 6 3 2 |  | No | 29.4 |
| 14 | 6 3 3 3 1 2 4 5 5 1 4 5 4 2 |  | No | 14.7 |
| 15 | 2 3 1 5 3 6 6 3 1 2 6 3 3 1 |  | No | 22.46 |
| 16 | 1 4 5 3 2 1 2 4 6 3 1 4 3 1 |  | No | 34.43 |
| 17 | 3 6 4 5 6 5 4 2 3 4 2 1 4 3 | 3 6 4 5 6 5 4 2 3 4 2 1 4 3 | Yes | 9.79 |
| 18 | 1 2 4 4 1 2 1 5 6 6 2 6 4 3 |  | No | 18.94 |
| 19 | 2 6 1 5 4 4 5 2 6 3 5 6 4 1 |  | No | 24.42 |
| 20 | 6 3 5 1 2 2 3 6 3 5 4 2 2 5 | 6 3 5 1 2 2 3 6 3 5 4 2 2 5 | Yes | 14.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1935 | 1935 | Yes | 2.6 |
| 2 | 531 | 531 | Yes | 2.9 |
| 3 | 727 | 727 | Yes | 2.64 |
| 4 | 1235 | 1235 | Yes | 2.53 |
| 5 | 654 | 654 | Yes | 2.87 |
| 6 | 1977 | 1977 | Yes | 5.16 |
| 7 | 1816 | 1816 | Yes | 2.47 |
| 8 | 2617 | 2617 | Yes | 2.58 |
| 9 | 1987 | 1987 | Yes | 7.12 |
| 10 | 1683 | 1683 | Yes | 4.48 |
| 11 | 1864 | 1864 | Yes | 2.98 |
| 12 | 1764 | 1764 | Yes | 2.47 |
| 13 | 2092 | 2092 | Yes | 1.24 |
| 14 | 2119 | 2119 | Yes | 2.48 |
| 15 | 1717 | 1717 | Yes | 3.45 |
| 16 | 1572 | 1572 | Yes | 4.98 |
| 17 | 1696 | 1696 | Yes | 2.96 |
| 18 | 1274 | 1274 | Yes | 2.71 |
| 19 | 2416 | 2416 | Yes | 2.73 |
| 20 | 932 | 932 | Yes | 2.7 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 41 | 41 | Yes | 5.48 |
| 2 | 59 | 59 | Yes | 12.32 |
| 3 | 44 | 44 | Yes | 7.03 |
| 4 | 63 | 62 | No | 9.27 |
| 5 | 63 | 62 | No | 9.49 |
| 6 | 61 | 61 | Yes | 9.46 |
| 7 | 49 | 49 | Yes | 8.44 |
| 8 | 61 | 60 | No | 8.75 |
| 9 | 50 | 50 | Yes | 7.83 |
| 10 | 75 | 75 | Yes | 8.11 |
| 11 | 64 | 64 | Yes | 13.07 |
| 12 | 49 | 49 | Yes | 9.88 |
| 13 | 43 | 43 | Yes | 6.95 |
| 14 | 65 | 65 | Yes | 14.7 |
| 15 | 68 | 68 | Yes | 5.37 |
| 16 | 68 | 68 | Yes | 9.57 |
| 17 | 59 | 59 | Yes | 3.91 |
| 18 | 44 | 44 | Yes | 7.48 |
| 19 | 72 | 72 | Yes | 4.59 |
| 20 | 63 | 63 | Yes | 10.24 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OXJWGNB | OXJWGNB | Yes | 3.94 |
| 2 | CNPZXJM | CNPZXJM | Yes | 4.0 |
| 3 | XWBLCUT | XWBLCUT | Yes | 2.98 |
| 4 | MJIGLCX | MJIGLCX | Yes | 4.33 |
| 5 | ZRTVHMS | ZRTVHMS | Yes | 5.21 |
| 6 | KZTRXLI | KZTRXLI | Yes | 4.05 |
| 7 | KGYCILT | KGYCILT | Yes | 3.53 |
| 8 | URWMVCB | URWMVCB | Yes | 4.51 |
| 9 | NSYABEO | NSYABEO | Yes | 4.42 |
| 10 | XIFPGBH | XIFPGBH | Yes | 4.47 |
| 11 | WNTPUZH | WNTPUZH | Yes | 5.47 |
| 12 | AKUDQZS | AKUDQZS | Yes | 4.71 |
| 13 | FOZBYKG | FOZBYKG | Yes | 3.27 |
| 14 | EQZMKFX | EQZMKFX | Yes | 4.29 |
| 15 | QMCJSYO | QMCJSYO | Yes | 4.42 |
| 16 | FRMBANU | FRMBANU | Yes | 3.89 |
| 17 | CFHXLEN | CFHXLEN | Yes | 4.69 |
| 18 | YGOSERK | YGOSERK | Yes | 4.61 |
| 19 | MVZJWCE | MVZJWCE | Yes | 4.43 |
| 20 | YORXIZB | YORXIZB | Yes | 3.89 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.9, 7.1] | 2.9 7.1 | Yes | 4.99 |
| 2 | [3.8, 6.2] | 6.2 3.8 | Yes | 5.92 |
| 3 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.63 |
| 4 | [3.1, 6.9] | 6.9 3.1 | Yes | 7.83 |
| 5 | [3.0, 7.0] | 7.0 3.0 | Yes | 3.0 |
| 6 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.09 |
| 7 | [0.5, 9.5] | 0.5 9.5 | Yes | 4.11 |
| 8 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.92 |
| 9 | [3.4, 6.6] | 3.4 6.6 | Yes | 6.23 |
| 10 | [1.2, 8.8] | 8.8 1.2 | Yes | 4.66 |
| 11 | [3.9, 6.1] | 6.1 3.9 | Yes | 5.37 |
| 12 | [3.1, 6.9] | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 1.6 |
| 13 | [3.2, 6.8] | 3.2 6.8 | Yes | 5.63 |
| 14 | [4.1, 5.9] | 4.1 5.9 | Yes | 5.09 |
| 15 | [3.1, 6.9] | 3.1 6.9 | Yes | 4.68 |
| 16 | [0.1, 9.9] | 9.9 0.1 | Yes | 4.1 |
| 17 | [4.9, 5.1] | 5.1 4.9 | Yes | 4.29 |
| 18 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.0 |
| 19 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.76 |
| 20 | [0.5, 9.5] | 9.5 0.5 | Yes | 5.35 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4DFAM7WDCLAT | 4DFAM7WDCLAT | Yes | 1.68 |
| 2 | 2KOD506ADX9J | 2KOD506ADX9J | Yes | 3.19 |
| 3 | H7LOIPVXOK5X | H7LOIPVXOK5X | Yes | 2.05 |
| 4 | FLX8ZUX1NARD | FLX8ZUX1NARD | Yes | 1.29 |
| 5 | 1N7273I8Z9CO | 1N7273I8Z9CO | Yes | 3.38 |
| 6 | M3HYYA2P43NY | M3HYYA2P43NY | Yes | 4.84 |
| 7 | 8SXI8503DFQT | 8SXI8503DFQT | Yes | 2.61 |
| 8 | CTUTO2SEF8PA | CTUTO2SEF8PA | Yes | 3.64 |
| 9 | 44O2RXPC3TSD | 44O2RXPC3TSD | Yes | 4.71 |
| 10 | W6GLGWUW0H4U | W6GLGWUW0H4U | Yes | 1.66 |
| 11 | SD2EM2TQ1WZY | SD2EM2TQ1WZY | Yes | 1.54 |
| 12 | R5AMRMMLCNVU | R5AMRMMLCNVU | Yes | 3.62 |
| 13 | YSZKXM3F4O62 | YSZKXM3F4O62 | Yes | 3.33 |
| 14 | 2627GF1BA1LX | 2627GF1BA1LX | Yes | 4.42 |
| 15 | ASE9FR2M0MY9 | ASE9FR2M0MY9 | Yes | 1.97 |
| 16 | F0KOW6B58MTO | F0KOW6B58MTO | Yes | 3.26 |
| 17 | 37U39UC3WQSJ | 37U39UC3WQSJ | Yes | 3.08 |
| 18 | K8ZSD170V52G | K8ZSD170V52G | Yes | 3.4 |
| 19 | 2Y96ALSQTN1D | 2Y96ALSQTN1D | Yes | 3.38 |
| 20 | YT4R12Q0P9PW | YT4R12Q0P9PW | Yes | 4.22 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 3.76 |
| 2 | 60 | 60 | Yes | 3.59 |
| 3 | 65 | 65 | Yes | 5.28 |
| 4 | 44 | 44 | Yes | 4.2 |
| 5 | 5 | 5 | Yes | 3.96 |
| 6 | 9 | 9 | Yes | 4.2 |
| 7 | 67 | 67 | Yes | 3.1 |
| 8 | 793 | 793 | Yes | 3.03 |
| 9 | 1440 | 1440 | Yes | 2.98 |
| 10 | 73 | 73 | Yes | 2.98 |
| 11 | 243 | 243 | Yes | 3.2 |
| 12 | 60 | 60 | Yes | 3.33 |
| 13 | 6 | 6 | Yes | 5.36 |
| 14 | 4 | 4 | Yes | 4.3 |
| 15 | 20 |  | No | 29.61 |
| 16 | 9 | 9 | Yes | 1.6 |
| 17 | 3 | 3 | Yes | 3.3 |
| 18 | 48 | 48 | Yes | 3.95 |
| 19 | 198 | 198 | Yes | 5.98 |
| 20 | 31 | 31 | Yes | 3.73 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _<(/\_(_\ |  | No | 27.85 |
| 2 | \ _\)__(  |  | No | 30.94 |
| 3 | /_/\/\</< |  | No | 42.19 |
| 4 | <_( \))\  |  | No | 36.38 |
| 5 | (<(___\\( |  | No | 35.8 |
| 6 | (\)\_\ )  |  | No | 17.23 |
| 7 | <( )))(<< |  | No | 22.95 |
| 8 | /\_\))</) | /\_\))</) | Yes | 24.47 |
| 9 | \/\ \<)\< |  | No | 25.31 |
| 10 | _/)/_ _\  |  | No | 29.89 |
| 11 | /( (<)) / | /( (<)) / | Yes | 20.24 |
| 12 | (()< _/ < | (()< _/ < | Yes | 2.38 |
| 13 | )<)(_</\_ |  | No | 21.4 |
| 14 | ) _ /(  ) | ) _ /(  ) | Yes | 9.1 |
| 15 | )\<(\ )(\ |  | No | 28.85 |
| 16 | )\ <<)/<< | )\ <<)/<< | Yes | 14.05 |
| 17 | <_(\/(\\( |  | No | 37.92 |
| 18 | <(  \ \\\ |  | No | 34.2 |
| 19 |  _(<(_(<_ | _(<(_(<_ | No | 10.38 |
| 20 |  _<</)\   | _<</)\ | No | 19.36 |
