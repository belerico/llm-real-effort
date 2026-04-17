# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-27 10:13:06

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
| sudoku_game | 4956 | 26417 | 31373 | 13 | 7 | 22.59 | 451.86 |
| add_numbers | 2720 | 854 | 3574 | 20 | 0 | 3.52 | 70.37 |
| counting_zeros | 4120 | 17689 | 21809 | 19 | 1 | 13.46 | 269.21 |
| task_decoding | 4060 | 2581 | 6641 | 20 | 0 | 5.07 | 101.46 |
| task_summation | 4400 | 5614 | 10014 | 20 | 0 | 7.25 | 145.06 |
| task_transcription | 2855 | 1355 | 4210 | 20 | 0 | 3.40 | 68.06 |
| task_sequences | 2584 | 3387 | 5971 | 18 | 2 | 12.97 | 259.38 |
| string_entry | 3165 | 22001 | 25166 | 7 | 13 | 24.27 | 485.31 |
| **TOTAL** | **28860** | **79898** | **108758** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 4 5 6 2 1 5 3 6 1 2 6 1 | 3 2 4 5 6 2 1 5 3 6 1 2 6 1 | Yes | 13.97 |
| 2 | 2 6 1 2 5 5 4 4 1 5 6 2 4 6 | 2 6 1 2 5 5 4 4 1 5 6 2 4 6 | Yes | 10.31 |
| 3 | 3 3 4 2 5 2 1 5 3 6 5 2 6 4 |  | No | 36.09 |
| 4 | 6 3 1 3 6 4 1 6 2 6 5 2 6 3 |  | No | 37.65 |
| 5 | 6 4 4 4 3 1 2 1 3 5 6 2 5 1 | 6 4 4 4 3 1 2 1 3 5 6 2 5 1 | Yes | 17.45 |
| 6 | 6 1 2 5 2 6 5 1 3 2 5 1 3 6 | 6 1 2 5 2 6 5 1 3 2 5 1 3 6 | Yes | 16.33 |
| 7 | 2 6 1 5 4 1 4 2 3 3 6 3 6 5 | 2 6 1 5 4 1 4 2 3 3 6 3 6 5 | Yes | 13.11 |
| 8 | 1 1 2 5 1 3 5 6 5 1 3 2 1 2 | 1 1 2 5 1 3 5 6 5 1 3 2 1 2 | Yes | 26.58 |
| 9 | 1 5 2 3 2 4 2 5 1 2 5 4 1 2 |  | No | 35.46 |
| 10 | 4 5 1 5 3 6 4 1 2 3 4 3 5 2 | 4 5 1 5 3 6 4 1 2 3 4 3 5 2 | Yes | 38.54 |
| 11 | 1 4 3 4 6 6 5 6 5 4 6 2 4 5 | 1 4 3 4 6 6 5 6 5 4 6 2 4 5 | Yes | 13.68 |
| 12 | 3 1 4 6 6 1 4 1 1 2 6 3 5 1 | 3 1 4 6 6 1 4 1 1 2 6 3 5 1 | Yes | 14.55 |
| 13 | 3 2 3 5 3 4 6 2 3 2 6 3 5 6 |  | No | 34.3 |
| 14 | 1 5 2 6 5 4 3 1 2 4 5 2 4 5 | 1 5 2 6 5 4 3 1 2 4 5 2 4 5 | Yes | 24.11 |
| 15 | 1 3 6 5 6 3 2 6 2 4 1 1 2 3 |  | No | 34.98 |
| 16 | 5 1 2 1 3 6 6 1 3 4 5 1 6 4 | 5 1 2 1 3 6 6 1 3 4 5 1 6 4 | Yes | 12.0 |
| 17 | 5 3 4 3 6 4 2 4 1 6 3 5 1 6 | 5 3 4 3 6 4 2 4 1 6 3 5 1 6 | Yes | 13.49 |
| 18 | 3 4 6 2 5 1 6 1 6 5 3 4 6 3 | 3 4 6 2 5 1 6 1 5 5 3 4 6 4 6 3 | No | 11.65 |
| 19 | 3 2 5 4 6 4 1 1 6 3 1 6 4 5 |  | No | 37.12 |
| 20 | 5 2 2 5 6 1 2 6 5 2 4 3 5 1 | 5 2 2 5 6 1 2 6 5 2 4 3 5 1 | Yes | 10.46 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1881 | 1881 | Yes | 3.64 |
| 2 | 1441 | 1441 | Yes | 2.76 |
| 3 | 2017 | 2017 | Yes | 3.26 |
| 4 | 1567 | 1567 | Yes | 3.66 |
| 5 | 1548 | 1548 | Yes | 3.06 |
| 6 | 1162 | 1162 | Yes | 4.46 |
| 7 | 1858 | 1858 | Yes | 3.68 |
| 8 | 1307 | 1307 | Yes | 2.73 |
| 9 | 1830 | 1830 | Yes | 3.03 |
| 10 | 1694 | 1694 | Yes | 3.62 |
| 11 | 1562 | 1562 | Yes | 3.82 |
| 12 | 1970 | 1970 | Yes | 4.21 |
| 13 | 1923 | 1923 | Yes | 4.14 |
| 14 | 1817 | 1817 | Yes | 2.97 |
| 15 | 1711 | 1711 | Yes | 3.37 |
| 16 | 1440 | 1440 | Yes | 3.37 |
| 17 | 1934 | 1934 | Yes | 5.16 |
| 18 | 2657 | 2657 | Yes | 2.83 |
| 19 | 1298 | 1298 | Yes | 3.18 |
| 20 | 2285 | 2285 | Yes | 3.39 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 10.23 |
| 2 | 38 | 38 | Yes | 10.39 |
| 3 | 40 | 40 | Yes | 10.13 |
| 4 | 55 | 55 | Yes | 15.4 |
| 5 | 57 | 57 | Yes | 14.58 |
| 6 | 35 | 35 | Yes | 13.45 |
| 7 | 72 | 72 | Yes | 12.19 |
| 8 | 58 | 58 | Yes | 12.48 |
| 9 | 57 | 57 | Yes | 13.01 |
| 10 | 48 | 48 | Yes | 9.68 |
| 11 | 75 | 74 | No | 12.13 |
| 12 | 39 | 39 | Yes | 11.63 |
| 13 | 47 | 47 | Yes | 19.44 |
| 14 | 58 | 58 | Yes | 20.59 |
| 15 | 70 | 70 | Yes | 17.25 |
| 16 | 66 | 66 | Yes | 14.91 |
| 17 | 46 | 46 | Yes | 11.4 |
| 18 | 35 | 35 | Yes | 12.26 |
| 19 | 52 | 52 | Yes | 13.55 |
| 20 | 71 | 71 | Yes | 14.5 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PBKZUCT | PBKZUCT | Yes | 5.31 |
| 2 | EDBOLGS | EDBOLGS | Yes | 7.44 |
| 3 | ISOVWMK | ISOVWMK | Yes | 5.91 |
| 4 | JFALXEO | JFALXEO | Yes | 6.95 |
| 5 | CVZJOSM | CVZJOSM | Yes | 6.63 |
| 6 | CSEYKMT | CSEYKMT | Yes | 2.87 |
| 7 | ATEDCBK | ATEDCBK | Yes | 6.18 |
| 8 | HCQSTVU | HCQSTVU | Yes | 2.58 |
| 9 | ZJMWPNK | ZJMWPNK | Yes | 5.51 |
| 10 | IHWYJUM | IHWYJUM | Yes | 7.42 |
| 11 | VGCXARW | VGCXARW | Yes | 2.45 |
| 12 | DFYJQSI | DFYJQSI | Yes | 3.72 |
| 13 | JNQUBIL | JNQUBIL | Yes | 6.65 |
| 14 | NPFBJDS | NPFBJDS | Yes | 3.82 |
| 15 | WXMHCNS | WXMHCNS | Yes | 4.29 |
| 16 | CFTELAM | CFTELAM | Yes | 4.62 |
| 17 | HGIQLBN | HGIQLBN | Yes | 3.07 |
| 18 | HLPEOSU | HLPEOSU | Yes | 8.09 |
| 19 | LKYPZMB | LKYPZMB | Yes | 5.79 |
| 20 | RIYKJTL | RIYKJTL | Yes | 2.15 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.01 |
| 2 | [2.0, 8.0] | 8.0 2.0 | Yes | 4.27 |
| 3 | [4.7, 5.3] | 4.7 5.3 | Yes | 8.74 |
| 4 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.35 |
| 5 | [2.1, 7.9] | 2.1 7.9 | Yes | 6.62 |
| 6 | [4.5, 5.5] | 5.5 4.5 | Yes | 10.57 |
| 7 | [3.4, 6.6] | 6.6 3.4 | Yes | 9.09 |
| 8 | [0.4, 9.6] | 0.4 9.6 | Yes | 8.55 |
| 9 | [3.1, 6.9] | 6.9 3.1 | Yes | 7.52 |
| 10 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.68 |
| 11 | [1.5, 8.5] | 1.5 8.5 | Yes | 6.91 |
| 12 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.7 |
| 13 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.71 |
| 14 | [0.8, 9.2] | 9.2 0.8 | Yes | 6.66 |
| 15 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.27 |
| 16 | [1.0, 9.0] | 9.0 1.0 | Yes | 6.81 |
| 17 | [3.2, 6.8] | 6.8 3.2 | Yes | 7.64 |
| 18 | [3.1, 6.9] | 3.1 6.9 | Yes | 6.63 |
| 19 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.79 |
| 20 | [4.3, 5.7] | 4.3 5.7 | Yes | 7.54 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EVXKF5ZGQI3D | EVXKF5ZGQI3D | Yes | 1.25 |
| 2 | CXVGXE5ZHURB | CXVGXE5ZHURB | Yes | 2.12 |
| 3 | E6KB24CV6DP5 | E6KB24CV6DP5 | Yes | 1.73 |
| 4 | J4FLLTUEFRP0 | J4FLLTUEFRP0 | Yes | 4.25 |
| 5 | CUS1CZXN1JJN | CUS1CZXN1JJN | Yes | 3.51 |
| 6 | 26FVMMCXPXHQ | 26FVMMCXPXHQ | Yes | 1.6 |
| 7 | DB8C00LM0L3K | DB8C00LM0L3K | Yes | 2.62 |
| 8 | 17WAFPX4MR74 | 17WAFPX4MR74 | Yes | 3.01 |
| 9 | PDB5SJXJ43KB | PDB5SJXJ43KB | Yes | 4.32 |
| 10 | APSHUFH806T1 | APSHUFH806T1 | Yes | 3.4 |
| 11 | HJTRBNBA0LY1 | HJTRBNBA0LY1 | Yes | 1.48 |
| 12 | IU2PEEKLB2AH | IU2PEEKLB2AH | Yes | 4.79 |
| 13 | V818Z24HDAQC | V818Z24HDAQC | Yes | 3.41 |
| 14 | 4DZQ2M4G4NTC | 4DZQ2M4G4NTC | Yes | 3.08 |
| 15 | ELJSCWDSDL4X | ELJSCWDSDL4X | Yes | 2.9 |
| 16 | 7NAPSTP744X6 | 7NAPSTP744X6 | Yes | 3.46 |
| 17 | O59TLLCR74I0 | O59TLLCR74I0 | Yes | 5.12 |
| 18 | XGPUHDZOSJD1 | XGPUHDZOSJD1 | Yes | 7.15 |
| 19 | 1S5FFFEZSJ5E | 1S5FFFEZSJ5E | Yes | 4.82 |
| 20 | 3XPOI8MASLHH | 3XPOI8MASLHH | Yes | 4.06 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 5 | Yes | 5.08 |
| 2 | 60 | 60 | Yes | 4.79 |
| 3 | 793 | TIMEOUT | No | 120.03 |
| 4 | 1440 | 1440 | Yes | 3.95 |
| 5 | 4 | 4 | Yes | 5.28 |
| 6 | 19 | 19 | Yes | 4.29 |
| 7 | 26 | 26 | Yes | 6.18 |
| 8 | 36 | 36 | Yes | 5.47 |
| 9 | 20 |  | No | 47.4 |
| 10 | 4 | 4 | Yes | 4.73 |
| 11 | 44 | 44 | Yes | 5.78 |
| 12 | 16 | 16 | Yes | 4.83 |
| 13 | 67 | 67 | Yes | 1.99 |
| 14 | 6 | 6 | Yes | 4.79 |
| 15 | 63 | 63 | Yes | 8.45 |
| 16 | 31 | 31 | Yes | 3.38 |
| 17 | 1 | 1 | Yes | 6.01 |
| 18 | 9 | 9 | Yes | 4.9 |
| 19 | 3 | 3 | Yes | 6.16 |
| 20 | 9 | 9 | Yes | 5.89 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \ /))< /< | \ /))< /< | Yes | 38.08 |
| 2 | <)<) ))\\ | <)<) ))\\ | Yes | 9.03 |
| 3 | \/\\__//\ | \/\\__//\ | Yes | 14.61 |
| 4 |   (((/_ _ | (((/_ _ | No | 12.29 |
| 5 | )__( )(\  | )__( )(\ | No | 14.52 |
| 6 | ) //)()_< |  | No | 38.94 |
| 7 | _((\)\/)_ |  | No | 61.31 |
| 8 | (()\))_\  | (())\))_\ | No | 12.61 |
| 9 | ((<//_( ( | ((<//_( ( | Yes | 7.86 |
| 10 | )(/(()))_ |  | No | 41.37 |
| 11 | <_)_\ )\  | <_)_\ )\ | No | 38.96 |
| 12 | _\</_  )) |  | No | 43.51 |
| 13 | \<\<</__  | \<\<</__ | No | 22.0 |
| 14 | )( <)) <\ | )( <)) <\ | Yes | 7.91 |
| 15 | \ )\)\\_  | \ )\)\\_ | No | 13.42 |
| 16 | \\))\<\</ |  | No | 43.82 |
| 17 | \\ (< /\) | \\ (< /\) | Yes | 11.36 |
| 18 | __/ \//\< | __/ \//\< | Yes | 6.31 |
| 19 |  <(((<<<_ | <(((<<<_ | No | 4.28 |
| 20 |  _)<(( <  |  | No | 43.12 |
