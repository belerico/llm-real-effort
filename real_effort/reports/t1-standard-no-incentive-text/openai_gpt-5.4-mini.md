# Benchmark Report — gpt-5.4-mini

- **Model**: `openai/gpt-5.4-mini`
- **Date**: 2026-03-27 10:09:19

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
| sudoku_game | 4969 | 34908 | 39877 | 8 | 12 | 21.20 | 423.95 |
| add_numbers | 2720 | 982 | 3702 | 20 | 0 | 2.93 | 58.69 |
| counting_zeros | 4120 | 18821 | 22941 | 16 | 4 | 9.09 | 181.85 |
| task_decoding | 4060 | 2728 | 6788 | 20 | 0 | 3.93 | 78.69 |
| task_summation | 4427 | 6089 | 10516 | 20 | 0 | 5.82 | 116.38 |
| task_transcription | 2867 | 2080 | 4947 | 20 | 0 | 3.88 | 77.56 |
| task_sequences | 2720 | 9284 | 12004 | 16 | 4 | 8.74 | 174.76 |
| string_entry | 3163 | 36920 | 40083 | 4 | 16 | 25.61 | 512.26 |
| **TOTAL** | **29046** | **111812** | **140858** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 1 2 6 4 3 1 5 6 4 6 3 3 |  | No | 16.39 |
| 2 | 1 2 3 1 4 4 3 5 2 2 4 5 5 1 | 1 2 3 1 4 4 3 5 2 2 4 5 5 1 | Yes | 13.16 |
| 3 | 3 2 5 1 1 5 2 3 6 5 1 4 3 6 |  | No | 18.93 |
| 4 | 6 1 3 5 4 5 6 2 6 4 5 6 2 4 | 6 1 3 5 4 5 6 2 6 4 5 6 2 4 | Yes | 12.36 |
| 5 | 2 4 2 3 5 1 4 3 1 4 2 6 4 3 |  | No | 17.59 |
| 6 | 2 4 1 2 5 6 2 3 3 6 4 2 6 3 | 2 4 1 2 5 6 2 3 3 6 4 2 6 3 | Yes | 8.01 |
| 7 | 1 5 4 2 5 1 3 5 6 2 2 3 6 1 | 1 5 4 2 5 1 3 5 6 2 2 3 6 1 | Yes | 14.01 |
| 8 | 4 6 1 5 3 6 4 5 6 4 3 2 5 6 |  | No | 38.73 |
| 9 | 2 3 1 6 6 4 2 3 1 2 5 1 3 1 | 2 3 1 6 6 4 2 3 1 2 5 1 3 1 | Yes | 14.26 |
| 10 | 5 3 1 6 3 5 5 6 2 5 1 1 1 4 | 5 3 1 6 3 5 5 6 2 5 1 1 1 4 | Yes | 9.66 |
| 11 | 6 1 4 3 3 5 2 3 3 1 2 1 6 4 |  | No | 35.64 |
| 12 | 2 6 1 2 1 6 3 5 6 4 5 4 3 2 | 2 6 1 2 1 6 3 5 6 4 5 4 3 2 | Yes | 20.48 |
| 13 | 5 3 4 4 4 1 5 6 2 1 6 5 3 2 |  | No | 44.48 |
| 14 | 2 1 4 1 5 2 3 1 4 2 6 4 1 2 |  | No | 38.98 |
| 15 | 4 3 2 5 2 4 6 2 5 5 1 5 1 5 |  | No | 25.34 |
| 16 | 5 6 2 1 6 5 5 4 2 4 1 4 6 2 |  | No | 19.61 |
| 17 | 1 5 2 6 3 1 5 4 2 5 1 5 3 1 |  | No | 24.11 |
| 18 | 4 5 5 6 1 3 4 3 2 3 6 5 2 1 |  | No | 22.25 |
| 19 | 1 6 4 5 2 2 3 6 1 4 3 5 6 1 | 1 6 4 5 2 2 3 6 1 4 3 5 6 1 | Yes | 11.34 |
| 20 | 3 1 1 4 3 2 6 1 6 5 4 3 1 5 |  | No | 18.57 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1009 | 1009 | Yes | 3.93 |
| 2 | 1340 | 1340 | Yes | 2.55 |
| 3 | 1754 | 1754 | Yes | 1.22 |
| 4 | 1717 | 1717 | Yes | 3.01 |
| 5 | 1712 | 1712 | Yes | 2.58 |
| 6 | 1763 | 1763 | Yes | 2.38 |
| 7 | 1488 | 1488 | Yes | 3.49 |
| 8 | 1657 | 1657 | Yes | 3.01 |
| 9 | 853 | 853 | Yes | 3.59 |
| 10 | 1081 | 1081 | Yes | 2.88 |
| 11 | 1435 | 1435 | Yes | 3.47 |
| 12 | 1229 | 1229 | Yes | 2.14 |
| 13 | 2555 | 2555 | Yes | 2.49 |
| 14 | 1589 | 1589 | Yes | 1.04 |
| 15 | 1938 | 1938 | Yes | 3.41 |
| 16 | 1427 | 1427 | Yes | 3.46 |
| 17 | 751 | 751 | Yes | 4.16 |
| 18 | 1048 | 1048 | Yes | 3.18 |
| 19 | 1367 | 1367 | Yes | 2.6 |
| 20 | 1798 | 1798 | Yes | 4.09 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 40 | Yes | 7.54 |
| 2 | 59 | 58 | No | 10.62 |
| 3 | 39 | 39 | Yes | 9.34 |
| 4 | 75 | 75 | Yes | 8.05 |
| 5 | 71 | 71 | Yes | 7.37 |
| 6 | 39 | 39 | Yes | 7.44 |
| 7 | 60 | 60 | Yes | 10.76 |
| 8 | 66 | 66 | Yes | 10.99 |
| 9 | 75 | 75 | Yes | 7.54 |
| 10 | 44 | 44 | Yes | 9.56 |
| 11 | 57 | 57 | Yes | 5.03 |
| 12 | 74 | 74 | Yes | 8.31 |
| 13 | 66 | 66 | Yes | 7.76 |
| 14 | 37 | 36 | No | 12.22 |
| 15 | 55 | 55 | Yes | 8.18 |
| 16 | 60 | 60 | Yes | 11.13 |
| 17 | 62 | 62 | Yes | 13.86 |
| 18 | 62 | 62 | Yes | 11.65 |
| 19 | 67 | 66 | No | 8.1 |
| 20 | 58 | 57 | No | 6.39 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MCGYKRU | MCGYKRU | Yes | 4.41 |
| 2 | VBRQHXP | VBRQHXP | Yes | 3.94 |
| 3 | ERLUSBJ | ERLUSBJ | Yes | 3.78 |
| 4 | BVQMIDJ | BVQMIDJ | Yes | 4.6 |
| 5 | HESKDQZ | HESKDQZ | Yes | 3.67 |
| 6 | BOWDPYJ | BOWDPYJ | Yes | 4.15 |
| 7 | PLAFUVW | PLAFUVW | Yes | 4.31 |
| 8 | LTXDKZW | LTXDKZW | Yes | 2.73 |
| 9 | BDGYQVN | BDGYQVN | Yes | 3.82 |
| 10 | GKSPCUF | GKSPCUF | Yes | 4.84 |
| 11 | TKJASLM | TKJASLM | Yes | 2.22 |
| 12 | SENOFLW | SENOFLW | Yes | 3.86 |
| 13 | HWSMGLR | HWSMGLR | Yes | 3.36 |
| 14 | ZGBEAWN | ZGBEAWN | Yes | 4.83 |
| 15 | ODVBIJX | ODVBIJX | Yes | 4.2 |
| 16 | RXPQIUS | RXPQIUS | Yes | 3.43 |
| 17 | CGMXZRN | CGMXZRN | Yes | 4.53 |
| 18 | PBXDYGV | PBXDYGV | Yes | 4.73 |
| 19 | UJHLSVF | UJHLSVF | Yes | 3.87 |
| 20 | FMEWUYN | FMEWUYN | Yes | 3.39 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.6, 6.4] | 6.4 3.6 | Yes | 5.5 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 4.67 |
| 3 | [3.9, 6.1] | 3.9 6.1 | Yes | 5.05 |
| 4 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.05 |
| 5 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.7 |
| 6 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.43 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.68 |
| 8 | [3.5, 6.5] | 6.5 3.5 | Yes | 7.1 |
| 9 | [1.6, 8.4] | 8.4 1.6 | Yes | 5.82 |
| 10 | [4.2, 5.8] | 4.2 5.8 | Yes | 6.47 |
| 11 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.77 |
| 12 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.75 |
| 13 | [0.5, 9.5] | 9.5 0.5 | Yes | 5.74 |
| 14 | [1.5, 8.5] | 1.5 8.5 | Yes | 5.36 |
| 15 | [0.1, 9.9] | 9.9 0.1 | Yes | 5.09 |
| 16 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.85 |
| 17 | [0.3, 9.7] | 9.7 0.3 | Yes | 4.96 |
| 18 | [2.7, 7.3] | 7.3 2.7 | Yes | 10.01 |
| 19 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.56 |
| 20 | [0.5, 9.5] | 0.5 9.5 | Yes | 3.8 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NR6NG6PJQKOZ | NR6NG6PJQKOZ | Yes | 3.84 |
| 2 | 6RNIMQ9PT0IA | 6RNIMQ9PT0IA | Yes | 4.71 |
| 3 | O8TJRLECOKLT | O8TJRLECOKLT | Yes | 3.56 |
| 4 | FHV4RK65RQNG | FHV4RK65RQNG | Yes | 4.22 |
| 5 | HA2UQIAW7UR1 | HA2UQIAW7UR1 | Yes | 3.18 |
| 6 | PDZTL2PCS1IT | PDZTL2PCS1IT | Yes | 1.71 |
| 7 | WTDVA1WX2JNO | WTDVA1WX2JNO | Yes | 3.57 |
| 8 | BXF0395DLK5L | BXF0395DLK5L | Yes | 4.13 |
| 9 | KQGLN002ZQUX | KQGLN002ZQUX | Yes | 3.46 |
| 10 | J6MO2WNNR0NM | J6MO2WNNR0NM | Yes | 2.13 |
| 11 | DYDQLJ259G96 | DYDQLJ259G96 | Yes | 3.78 |
| 12 | W0UZ8WZIXVM7 | W0UZ8WZIXVM7 | Yes | 3.59 |
| 13 | 99OROSZV8BTL | 99OROSZV8BTL | Yes | 3.89 |
| 14 | F2YYQNKFC4SC | F2YYQNKFC4SC | Yes | 3.42 |
| 15 | 3S9PR1DD5T8O | 3S9PR1DD5T8O | Yes | 3.56 |
| 16 | L5C6ZZAYYV9V | L5C6ZZAYYV9V | Yes | 3.36 |
| 17 | 2UJJLZ7WF07D | 2UJJLZ7WF07D | Yes | 3.67 |
| 18 | 8PYMOFQV8J2C | 8PYMOFQV8J2C | Yes | 10.78 |
| 19 | G0DDX8MS1QZU | G0DDX8MS1QZU | Yes | 3.17 |
| 20 | T907B2VDZ27P | T907B2VDZ27P | Yes | 3.84 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 | 64 | Yes | 4.11 |
| 2 | 48 | 48 | Yes | 3.38 |
| 3 | 5 | 15 | No | 3.49 |
| 4 | 60 | 60 | Yes | 4.35 |
| 5 | 20 |  | No | 30.12 |
| 6 | 73 | 73 | Yes | 4.21 |
| 7 | 10 | 10 | Yes | 20.02 |
| 8 | 3 | 3 | Yes | 3.88 |
| 9 | 1440 | 1440 | Yes | 3.44 |
| 10 | 5 |  | No | 28.42 |
| 11 | 67 | 67 | Yes | 3.08 |
| 12 | 26 |  | No | 29.25 |
| 13 | 243 | 243 | Yes | 3.35 |
| 14 | 60 | 60 | Yes | 4.09 |
| 15 | 3 | 3 | Yes | 2.14 |
| 16 | 39 | 39 | Yes | 5.28 |
| 17 | 65 | 65 | Yes | 7.9 |
| 18 | 28 | 28 | Yes | 4.5 |
| 19 | 793 | 793 | Yes | 5.42 |
| 20 | 44 | 44 | Yes | 4.35 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( <(\\ )\ |  | No | 41.35 |
| 2 | </ <  ))_ | </ <  ))_ | Yes | 8.94 |
| 3 | /(/(_ ((/ |  | No | 19.17 |
| 4 | \/(/)_)\/ | \/(/)_)\/ | Yes | 11.86 |
| 5 |  \_)<(<\< |  | No | 34.1 |
| 6 | _\/_  \(< |  | No | 32.68 |
| 7 | (/\\\( )/ |  | No | 27.2 |
| 8 | \)_)(  <\ | \)_)(  <\ | Yes | 15.95 |
| 9 |   \/_<) / |  | No | 27.16 |
| 10 | )(<\\ <<\ |  | No | 36.97 |
| 11 | \<)\\)(_( | \<)\\)(_(` | No | 24.33 |
| 12 | _  ())<(( |  | No | 19.43 |
| 13 | ((<\__)_/ |  | No | 23.58 |
| 14 | _((()_<<  |  | No | 46.99 |
| 15 | \/(\<<//) | \/(\<<//) | Yes | 17.29 |
| 16 | ))<()<//( |  | No | 26.02 |
| 17 | </(/ ()<\ |  | No | 26.64 |
| 18 | /(__ ( __ |  | No | 20.46 |
| 19 |  / _<()/_ |  | No | 21.2 |
| 20 | < )/<</\\ |  | No | 30.96 |
