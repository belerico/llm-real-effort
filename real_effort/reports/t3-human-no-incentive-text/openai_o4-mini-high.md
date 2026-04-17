# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-27 10:27:22

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
| sudoku_game | 5306 | 40960 | 46266 | 0 | 20 | 38.76 | 775.24 |
| add_numbers | 3060 | 3550 | 6610 | 20 | 0 | 3.11 | 62.22 |
| counting_zeros | 4460 | 38693 | 43153 | 5 | 15 | 29.75 | 595.02 |
| task_decoding | 4400 | 7984 | 12384 | 20 | 0 | 6.46 | 129.31 |
| task_summation | 4503 | 15942 | 20445 | 19 | 1 | 16.03 | 320.52 |
| task_transcription | 3203 | 3239 | 6442 | 20 | 0 | 2.59 | 51.88 |
| task_sequences | 3061 | 14345 | 17406 | 19 | 1 | 10.28 | 205.51 |
| string_entry | 3508 | 36044 | 39552 | 2 | 18 | 26.98 | 539.6 |
| **TOTAL** | **31501** | **160757** | **192258** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 4 4 5 2 3 6 6 3 1 5 2 6 |  | No | 42.35 |
| 2 | 5 4 1 3 6 3 5 1 2 3 5 4 2 5 |  | No | 43.5 |
| 3 | 5 4 1 6 6 5 1 6 4 1 4 6 5 3 |  | No | 32.09 |
| 4 | 2 5 4 5 3 1 3 6 1 3 4 5 3 2 |  | No | 37.63 |
| 5 | 6 4 2 3 6 1 2 3 2 1 3 5 4 2 |  | No | 39.32 |
| 6 | 6 5 4 2 1 6 4 5 4 3 1 6 1 2 |  | No | 42.08 |
| 7 | 5 6 3 2 5 4 5 3 2 6 5 3 2 3 |  | No | 44.31 |
| 8 | 6 1 3 4 4 1 6 5 2 5 4 3 5 1 |  | No | 38.68 |
| 9 | 4 2 1 3 3 4 5 1 4 6 6 2 1 3 |  | No | 54.03 |
| 10 | 4 2 5 1 6 2 4 2 5 3 6 5 2 3 |  | No | 37.39 |
| 11 | 4 2 5 3 2 1 2 4 3 4 5 1 1 6 |  | No | 34.49 |
| 12 | 3 6 1 6 5 3 2 2 4 5 1 4 6 3 |  | No | 51.08 |
| 13 | 1 2 6 5 2 5 6 5 3 2 1 5 4 2 |  | No | 16.98 |
| 14 | 3 6 3 4 3 2 5 5 3 2 4 5 2 2 |  | No | 38.65 |
| 15 | 2 1 4 6 4 1 5 2 6 1 1 6 2 1 |  | No | 45.63 |
| 16 | 5 4 6 1 2 2 6 3 2 4 4 5 3 6 |  | No | 43.28 |
| 17 | 4 5 3 1 5 4 3 5 6 3 2 2 4 1 |  | No | 22.18 |
| 18 | 6 1 3 3 6 4 3 5 6 4 5 2 6 5 |  | No | 37.46 |
| 19 | 2 5 2 1 5 6 6 4 5 1 6 1 6 2 |  | No | 34.46 |
| 20 | 5 1 6 1 4 4 2 4 3 5 1 1 4 3 |  | No | 39.62 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1538 | 1538 | Yes | 2.3 |
| 2 | 1557 | 1557 | Yes | 2.04 |
| 3 | 1392 | 1392 | Yes | 3.02 |
| 4 | 2187 | 2187 | Yes | 5.12 |
| 5 | 2527 | 2527 | Yes | 3.08 |
| 6 | 1538 | 1538 | Yes | 2.89 |
| 7 | 2115 | 2115 | Yes | 2.72 |
| 8 | 2077 | 2077 | Yes | 4.91 |
| 9 | 2173 | 2173 | Yes | 3.04 |
| 10 | 2220 | 2220 | Yes | 2.92 |
| 11 | 946 | 946 | Yes | 2.96 |
| 12 | 1389 | 1389 | Yes | 3.67 |
| 13 | 1305 | 1305 | Yes | 2.24 |
| 14 | 1333 | 1333 | Yes | 4.8 |
| 15 | 1225 | 1225 | Yes | 2.81 |
| 16 | 1946 | 1946 | Yes | 2.16 |
| 17 | 2106 | 2106 | Yes | 2.68 |
| 18 | 1945 | 1945 | Yes | 3.27 |
| 19 | 1011 | 1011 | Yes | 2.89 |
| 20 | 1811 | 1811 | Yes | 2.71 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 |  | No | 29.51 |
| 2 | 42 |  | No | 48.53 |
| 3 | 46 |  | No | 38.78 |
| 4 | 67 | 67 | Yes | 10.87 |
| 5 | 64 | 64 | Yes | 17.8 |
| 6 | 65 |  | No | 30.98 |
| 7 | 59 |  | No | 22.31 |
| 8 | 50 |  | No | 69.5 |
| 9 | 38 |  | No | 39.54 |
| 10 | 64 |  | No | 29.6 |
| 11 | 74 |  | No | 24.05 |
| 12 | 55 |  | No | 22.08 |
| 13 | 36 | 36 | Yes | 11.91 |
| 14 | 73 |  | No | 34.67 |
| 15 | 47 |  | No | 19.19 |
| 16 | 53 |  | No | 34.45 |
| 17 | 35 |  | No | 43.7 |
| 18 | 38 | 38 | Yes | 19.72 |
| 19 | 55 |  | No | 32.26 |
| 20 | 50 | 50 | Yes | 15.57 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QZRMIHY | QZRMIHY | Yes | 8.89 |
| 2 | ROZITFJ | ROZITFJ | Yes | 13.77 |
| 3 | KBGWXVO | KBGWXVO | Yes | 7.75 |
| 4 | OMNRPGY | OMNRPGY | Yes | 4.79 |
| 5 | UBAIVDQ | UBAIVDQ | Yes | 2.27 |
| 6 | EOGXPAL | EOGXPAL | Yes | 7.73 |
| 7 | YFNRHOX | YFNRHOX | Yes | 5.06 |
| 8 | CMAUNSQ | CMAUNSQ | Yes | 10.41 |
| 9 | QXRKDCP | QXRKDCP | Yes | 3.03 |
| 10 | KUMHVCF | KUMHVCF | Yes | 7.69 |
| 11 | ZQSNEYF | ZQSNEYF | Yes | 9.4 |
| 12 | DJROVAF | DJROVAF | Yes | 6.14 |
| 13 | EHBGLJV | EHBGLJV | Yes | 3.86 |
| 14 | JGXTYBI | JGXTYBI | Yes | 4.43 |
| 15 | VRLKJSG | VRLKJSG | Yes | 3.43 |
| 16 | ZVTFDHY | ZVTFDHY | Yes | 7.35 |
| 17 | SXIFVPC | SXIFVPC | Yes | 5.39 |
| 18 | MPIZAYN | MPIZAYN | Yes | 5.97 |
| 19 | TCYAPUQ | TCYAPUQ | Yes | 7.41 |
| 20 | QRGJKET | QRGJKET | Yes | 4.52 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.96 |
| 2 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.65 |
| 3 | [3.9, 6.1] | 3.9 6.1 | Yes | 10.19 |
| 4 | [3.9, 6.1] | 3.9 6.1 | Yes | 13.82 |
| 5 | [0.5, 9.5] | 0.5 9.5 | Yes | 7.96 |
| 6 | [4.4, 5.6] | 4.4 5.6 | Yes | 8.9 |
| 7 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.6 |
| 8 | [2.7, 7.3] | 2.7 7.3 | Yes | 8.05 |
| 9 | [3.8, 6.2] | 6.2 3.8 | Yes | 8.78 |
| 10 | [2.8, 7.2] | 7.2 2.8 | Yes | 14.95 |
| 11 | [4.2, 5.8] | 4.2 5.8 | Yes | 10.85 |
| 12 | [3.5, 6.5] | 3.5 6.5 | Yes | 10.26 |
| 13 | [4.1, 5.9] | 4.1 5.9 | Yes | 12.15 |
| 14 | [2.9, 7.1] | TIMEOUT | No | 120.02 |
| 15 | [2.5, 7.5] | 2.5 7.5 | Yes | 17.78 |
| 16 | [1.9, 8.1] | 1.9 8.1 | Yes | 11.6 |
| 17 | [4.5, 5.5] | 4.5 5.5 | Yes | 8.66 |
| 18 | [0.5, 9.5] | 0.5 9.5 | Yes | 9.39 |
| 19 | [0.8, 9.2] | 9.2 0.8 | Yes | 9.38 |
| 20 | [1.5, 8.5] | 8.5 1.5 | Yes | 8.57 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 19EUN17BE2II | 19EUN17BE2II | Yes | 2.56 |
| 2 | B7OOBSM7BUZQ | B7OOBSM7BUZQ | Yes | 2.45 |
| 3 | M1QE8EISPCDZ | M1QE8EISPCDZ | Yes | 3.17 |
| 4 | 6LIZI0HLZTPD | 6LIZI0HLZTPD | Yes | 3.04 |
| 5 | T8DV4YEV8E4G | T8DV4YEV8E4G | Yes | 2.07 |
| 6 | WYVM3659SA1C | WYVM3659SA1C | Yes | 2.47 |
| 7 | A0BZ2IAWJUU3 | A0BZ2IAWJUU3 | Yes | 2.52 |
| 8 | YPR4G5NB4Z9X | YPR4G5NB4Z9X | Yes | 2.57 |
| 9 | 03E5MBZ2N2YT | 03E5MBZ2N2YT | Yes | 2.45 |
| 10 | ZUPM9Q5YRN0Q | ZUPM9Q5YRN0Q | Yes | 2.54 |
| 11 | EHJMLLHUMGYG | EHJMLLHUMGYG | Yes | 3.73 |
| 12 | AQTBSSRVN8BC | AQTBSSRVN8BC | Yes | 1.89 |
| 13 | WEJF0JW584D5 | WEJF0JW584D5 | Yes | 2.6 |
| 14 | TSQLVT8HCFV5 | TSQLVT8HCFV5 | Yes | 2.51 |
| 15 | JXKTZYDT6JWQ | JXKTZYDT6JWQ | Yes | 2.36 |
| 16 | 0PDV5RGGXWMG | 0PDV5RGGXWMG | Yes | 2.27 |
| 17 | R6I46VZHDEKG | R6I46VZHDEKG | Yes | 2.22 |
| 18 | PZCOAZUYHBHE | PZCOAZUYHBHE | Yes | 3.31 |
| 19 | 1PS79XRSP5EF | 1PS79XRSP5EF | Yes | 2.2 |
| 20 | MYZLKF3URTJR | MYZLKF3URTJR | Yes | 2.94 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 9.37 |
| 2 | 23 | 23 | Yes | 6.11 |
| 3 | 67 | 67 | Yes | 5.31 |
| 4 | 44 | 44 | Yes | 9.64 |
| 5 | 7 | 7 | Yes | 15.66 |
| 6 | 19 | 19 | Yes | 5.17 |
| 7 | 5 | 5 | Yes | 3.97 |
| 8 | 4096 |  | No | 39.42 |
| 9 | 3 | 3 | Yes | 9.88 |
| 10 | 4 | 4 | Yes | 9.28 |
| 11 | 64 | 64 | Yes | 11.69 |
| 12 | 9 | 9 | Yes | 11.1 |
| 13 | 31 | 31 | Yes | 6.9 |
| 14 | 26 | 26 | Yes | 11.22 |
| 15 | 20 | 20 | Yes | 11.85 |
| 16 | 4 | 4 | Yes | 8.3 |
| 17 | 793 | 793 | Yes | 3.46 |
| 18 | 9 | 9 | Yes | 12.13 |
| 19 | 73 | 73 | Yes | 6.08 |
| 20 | 28 | 28 | Yes | 8.96 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \\(</<\ ) |  | No | 46.29 |
| 2 | <  \_\ (_ |  | No | 21.06 |
| 3 | </__(<\_/ | /\) <(_<) | No | 12.34 |
| 4 | \< (\/( ) |  | No | 20.88 |
| 5 | \_<)/)  ) | /\) <(_<) | No | 11.91 |
| 6 | \_ </ (<_ |  | No | 58.85 |
| 7 | _) \<)_ / | _) \<)_ / | Yes | 7.2 |
| 8 | )_)()/\<  |  | No | 24.56 |
| 9 | /<</_\<)_ | /<</_\<)_ | Yes | 20.57 |
| 10 | _ <( (<<< |  | No | 23.43 |
| 11 | (< _(  <) |  | No | 22.43 |
| 12 | < /_//< _ | /\) <(_<) | No | 16.5 |
| 13 | _  /)\ \( |  | No | 50.97 |
| 14 | <(__(//\) |  | No | 45.12 |
| 15 | /)<_)_\(( |  | No | 21.9 |
| 16 | ( <\_\_)/ | /\) <(_<) | No | 13.88 |
| 17 | )_  <\\)  |  | No | 51.16 |
| 18 | _\<</(  \ | /\) <(_<) | No | 10.19 |
| 19 | \_/(<_(() |  | No | 28.95 |
| 20 | )(\__<(/  |  | No | 31.4 |
