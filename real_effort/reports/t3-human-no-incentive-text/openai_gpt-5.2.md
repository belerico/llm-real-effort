# Benchmark Report — gpt-5.2

- **Model**: `openai/gpt-5.2`
- **Date**: 2026-03-27 10:08:22

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
| sudoku_game | 5298 | 22175 | 27473 | 17 | 3 | 24.71 | 494.24 |
| add_numbers | 3060 | 705 | 3765 | 20 | 0 | 3.68 | 73.57 |
| counting_zeros | 4460 | 16760 | 21220 | 20 | 0 | 16.25 | 325.06 |
| task_decoding | 4400 | 2213 | 6613 | 20 | 0 | 4.81 | 96.21 |
| task_summation | 4740 | 3233 | 7973 | 20 | 0 | 6.07 | 121.43 |
| task_transcription | 3197 | 869 | 4066 | 20 | 0 | 2.23 | 44.6 |
| task_sequences | 3060 | 2437 | 5497 | 20 | 0 | 6.11 | 122.31 |
| string_entry | 3513 | 11483 | 14996 | 9 | 11 | 13.13 | 262.69 |
| **TOTAL** | **31728** | **59875** | **91603** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 2 4 6 4 3 6 3 2 5 6 4 1 | 1 2 2 4 6 4 3 6 3 2 5 6 4 1 | Yes | 24.08 |
| 2 | 4 5 3 1 5 6 2 5 6 4 2 2 3 5 | 4 5 3 1 5 6 2 5 6 4 2 2 3 5 | Yes | 14.5 |
| 3 | 6 4 4 5 6 5 4 5 2 1 6 4 1 3 | 6 4 4 5 6 5 4 5 2 1 6 4 1 3 | Yes | 19.09 |
| 4 | 2 1 1 5 3 3 5 5 1 4 3 6 2 4 | 2 1 1 5 3 3 5 5 1 4 3 6 2 4 | Yes | 21.45 |
| 5 | 4 3 6 1 4 1 3 5 3 5 3 4 1 3 | 4 3 6 1 4 1 3 5 3 5 3 4 1 3 | Yes | 20.04 |
| 6 | 4 6 2 3 5 5 4 2 5 1 4 6 3 6 |  | No | 58.97 |
| 7 | 3 3 1 6 4 3 1 3 6 1 3 2 6 4 |  | No | 61.17 |
| 8 | 6 2 4 6 4 3 5 6 1 2 5 6 3 1 | 6 2 4 6 4 3 5 6 1 2 5 6 3 1 | Yes | 19.49 |
| 9 | 3 1 2 3 5 2 5 3 4 1 6 4 3 5 | 3 1 2 3 5 2 5 3 4 1 6 4 3 5 | Yes | 13.96 |
| 10 | 3 2 4 6 1 6 2 4 4 3 6 1 2 1 |  | No | 58.05 |
| 11 | 6 2 2 3 1 4 5 5 1 2 6 6 1 2 | 6 2 2 3 1 4 5 5 1 2 6 6 1 2 | Yes | 14.3 |
| 12 | 4 3 5 2 1 4 2 3 1 4 5 3 2 4 | 4 3 5 2 1 4 2 3 1 4 5 3 2 4 | Yes | 26.69 |
| 13 | 1 4 3 1 6 4 5 4 2 6 1 5 3 2 | 1 4 3 1 6 4 5 4 2 6 1 5 3 2 | Yes | 17.5 |
| 14 | 1 4 1 5 5 1 3 4 2 4 2 3 5 1 | 1 4 1 5 5 1 3 4 2 4 2 3 5 1 | Yes | 20.7 |
| 15 | 6 3 2 4 5 5 3 3 2 5 4 6 4 5 | 6 3 2 4 5 5 3 3 2 5 4 6 4 5 | Yes | 15.86 |
| 16 | 3 4 6 4 5 3 4 2 3 6 2 3 6 5 | 3 4 6 4 5 3 4 2 3 6 2 3 6 5 | Yes | 17.83 |
| 17 | 6 5 4 1 4 2 1 6 3 3 5 1 3 6 | 6 5 4 1 4 2 1 6 3 3 5 1 3 6 | Yes | 11.97 |
| 18 | 6 5 1 6 6 1 2 3 1 4 5 4 5 1 | 6 5 1 6 6 1 2 3 1 4 5 4 5 1 | Yes | 10.97 |
| 19 | 1 6 4 1 4 3 6 2 1 4 3 5 2 6 | 1 6 4 1 4 3 6 2 1 4 3 5 2 6 | Yes | 16.03 |
| 20 | 4 1 2 6 4 2 6 1 3 5 4 2 5 1 | 4 1 2 6 4 2 6 1 3 5 4 2 5 1 | Yes | 31.55 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1252 | 1252 | Yes | 3.6 |
| 2 | 1141 | 1141 | Yes | 5.34 |
| 3 | 1600 | 1600 | Yes | 2.98 |
| 4 | 1346 | 1346 | Yes | 3.54 |
| 5 | 1709 | 1709 | Yes | 3.27 |
| 6 | 1772 | 1772 | Yes | 1.15 |
| 7 | 967 | 967 | Yes | 2.91 |
| 8 | 1998 | 1998 | Yes | 3.02 |
| 9 | 770 | 770 | Yes | 5.73 |
| 10 | 1307 | 1307 | Yes | 3.09 |
| 11 | 1827 | 1827 | Yes | 3.68 |
| 12 | 2458 | 2458 | Yes | 7.25 |
| 13 | 1396 | 1396 | Yes | 3.23 |
| 14 | 868 | 868 | Yes | 4.73 |
| 15 | 1381 | 1381 | Yes | 2.9 |
| 16 | 2294 | 2294 | Yes | 3.19 |
| 17 | 1719 | 1719 | Yes | 2.98 |
| 18 | 1504 | 1504 | Yes | 3.36 |
| 19 | 1264 | 1264 | Yes | 2.88 |
| 20 | 1935 | 1935 | Yes | 4.74 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 41 | 41 | Yes | 16.41 |
| 2 | 47 | 47 | Yes | 13.08 |
| 3 | 67 | 67 | Yes | 11.97 |
| 4 | 66 | 66 | Yes | 16.26 |
| 5 | 63 | 63 | Yes | 14.83 |
| 6 | 69 | 69 | Yes | 22.2 |
| 7 | 58 | 58 | Yes | 16.55 |
| 8 | 65 | 65 | Yes | 15.78 |
| 9 | 58 | 58 | Yes | 15.86 |
| 10 | 66 | 66 | Yes | 19.01 |
| 11 | 50 | 50 | Yes | 15.4 |
| 12 | 42 | 42 | Yes | 17.95 |
| 13 | 56 | 56 | Yes | 26.54 |
| 14 | 43 | 43 | Yes | 17.14 |
| 15 | 54 | 54 | Yes | 13.0 |
| 16 | 44 | 44 | Yes | 17.83 |
| 17 | 70 | 70 | Yes | 13.92 |
| 18 | 50 | 50 | Yes | 15.87 |
| 19 | 59 | 59 | Yes | 14.86 |
| 20 | 41 | 41 | Yes | 10.57 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TUOXNMI | TUOXNMI | Yes | 4.22 |
| 2 | DUGXVWY | DUGXVWY | Yes | 5.12 |
| 3 | CVTYBUN | CVTYBUN | Yes | 5.25 |
| 4 | DCQMOIP | DCQMOIP | Yes | 4.75 |
| 5 | WLFBTNI | WLFBTNI | Yes | 4.74 |
| 6 | WTZPFLH | WTZPFLH | Yes | 5.54 |
| 7 | BCWDEGY | BCWDEGY | Yes | 5.28 |
| 8 | KPRZGAF | KPRZGAF | Yes | 4.35 |
| 9 | JIBOYRX | JIBOYRX | Yes | 5.6 |
| 10 | LWPTRBN | LWPTRBN | Yes | 4.28 |
| 11 | BTVPRLU | BTVPRLU | Yes | 4.77 |
| 12 | ACZEGKI | ACZEGKI | Yes | 6.19 |
| 13 | VTAOJLE | VTAOJLE | Yes | 4.03 |
| 14 | RUDEFHN | RUDEFHN | Yes | 5.2 |
| 15 | NFVHPLR | NFVHPLR | Yes | 4.91 |
| 16 | EORJZNL | EORJZNL | Yes | 3.94 |
| 17 | WEHVKMD | WEHVKMD | Yes | 4.31 |
| 18 | CEGTSQR | CEGTSQR | Yes | 4.41 |
| 19 | BQLNJWV | BQLNJWV | Yes | 4.65 |
| 20 | KODFVBX | KODFVBX | Yes | 4.65 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.1, 8.9] | 8.9 1.1 | Yes | 4.41 |
| 2 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.83 |
| 3 | [0.3, 9.7] | 0.3 9.7 | Yes | 3.75 |
| 4 | [2.7, 7.3] | 7.3 2.7 | Yes | 4.71 |
| 5 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.39 |
| 6 | [1.1, 8.9] | 8.9 1.1 | Yes | 5.91 |
| 7 | [2.8, 7.2] | 7.2 2.8 | Yes | 3.88 |
| 8 | [1.4, 8.6] | 1.4 8.6 | Yes | 5.78 |
| 9 | [1.6, 8.4] | 8.4 1.6 | Yes | 4.74 |
| 10 | [1.9, 8.1] | 8.1 1.9 | Yes | 7.04 |
| 11 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.18 |
| 12 | [0.8, 9.2] | 0.8 9.2 | Yes | 3.88 |
| 13 | [2.8, 7.2] | 2.8 7.2 | Yes | 8.07 |
| 14 | [4.1, 5.9] | 4.1 5.9 | Yes | 4.87 |
| 15 | [1.3, 8.7] | 1.3 8.7 | Yes | 6.13 |
| 16 | [2.8, 7.2] | 2.8 7.2 | Yes | 9.27 |
| 17 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.52 |
| 18 | [2.9, 7.1] | 7.1 2.9 | Yes | 7.53 |
| 19 | [2.3, 7.7] | 2.3 7.7 | Yes | 7.8 |
| 20 | [5.0, 5.0] | 5.0 5.0 | Yes | 8.75 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5F83FVQWG2Q9 | 5F83FVQWG2Q9 | Yes | 1.61 |
| 2 | PBON92NB7P4D | PBON92NB7P4D | Yes | 1.63 |
| 3 | CEC0F3O43C3C | CEC0F3O43C3C | Yes | 6.04 |
| 4 | WTREBLQPQGWM | WTREBLQPQGWM | Yes | 2.43 |
| 5 | W41ETUWQX1UR | W41ETUWQX1UR | Yes | 1.95 |
| 6 | 4IVVJM367ARG | 4IVVJM367ARG | Yes | 1.3 |
| 7 | Y000ITW1BWKV | Y000ITW1BWKV | Yes | 6.62 |
| 8 | I5DIR9T3WJJO | I5DIR9T3WJJO | Yes | 1.49 |
| 9 | 9H8EG9V65EZV | 9H8EG9V65EZV | Yes | 1.33 |
| 10 | LDFTHFGJUTI9 | LDFTHFGJUTI9 | Yes | 1.53 |
| 11 | 63B817VBAKAL | 63B817VBAKAL | Yes | 1.74 |
| 12 | OMIB5GB7RKMT | OMIB5GB7RKMT | Yes | 1.34 |
| 13 | YYRZ8NZMHSYL | YYRZ8NZMHSYL | Yes | 1.57 |
| 14 | ZDUZC3WTO4L8 | ZDUZC3WTO4L8 | Yes | 1.49 |
| 15 | 3TUHJBN6X12S | 3TUHJBN6X12S | Yes | 1.82 |
| 16 | 9J832UC14PZR | 9J832UC14PZR | Yes | 1.43 |
| 17 | K7CRCCJFQBN2 | K7CRCCJFQBN2 | Yes | 1.57 |
| 18 | CMJ767OHR2JS | CMJ767OHR2JS | Yes | 4.7 |
| 19 | TT3I55AGZG05 | TT3I55AGZG05 | Yes | 1.48 |
| 20 | UFEC3RK5E1LB | UFEC3RK5E1LB | Yes | 1.53 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 3.46 |
| 2 | 60 | 60 | Yes | 6.29 |
| 3 | 198 | 198 | Yes | 5.64 |
| 4 | 5 | 5 | Yes | 7.16 |
| 5 | 3 | 3 | Yes | 6.42 |
| 6 | 36 | 36 | Yes | 4.08 |
| 7 | 9 | 9 | Yes | 9.0 |
| 8 | 1440 | 1440 | Yes | 4.64 |
| 9 | 19 | 19 | Yes | 4.09 |
| 10 | 39 | 39 | Yes | 4.88 |
| 11 | 6 | 6 | Yes | 3.32 |
| 12 | 3 | 3 | Yes | 7.34 |
| 13 | 4 | 4 | Yes | 6.12 |
| 14 | 63 | 63 | Yes | 4.33 |
| 15 | 64 | 64 | Yes | 6.59 |
| 16 | 48 | 48 | Yes | 5.1 |
| 17 | 23 | 23 | Yes | 5.62 |
| 18 | 31 | 31 | Yes | 1.64 |
| 19 | 26 | 26 | Yes | 20.98 |
| 20 | 16 | 16 | Yes | 5.59 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _ (   )\  | /\) <(_<) | No | 27.57 |
| 2 | _  (\/)<\ | /\) <(_<) | No | 14.7 |
| 3 | _ \((()<\ | /\) <(_<) | No | 12.66 |
| 4 | <)(\</ <_ | <)(\</ <_ | Yes | 7.35 |
| 5 | _<(\_<//( | /\) <(_<) | No | 29.43 |
| 6 | (_ _(<_(( | (_ _(<_(( | Yes | 8.4 |
| 7 | _ \)</(<( | /\) <(_<) | No | 10.62 |
| 8 |  \<<  ((/ | \<<  ((/ | No | 8.63 |
| 9 | \\ _) _)( | \\ _) _)( | Yes | 16.78 |
| 10 | )<)<\<_<( | /\) <(_<) | No | 14.3 |
| 11 | (/\__\<() | /\) <(_<) | No | 23.11 |
| 12 |  \\ \( (  | \\ \( ( | No | 8.02 |
| 13 |  _)/\ //  | _)/\ // | No | 21.1 |
| 14 | \<<_(_(// | /\) <(_<) | No | 13.73 |
| 15 | \/\) \) / | \/\) \) / | Yes | 9.44 |
| 16 | __()<_ (( | __()<_ (( | Yes | 6.93 |
| 17 | \_)<  ((< | \_)<  ((< | Yes | 6.59 |
| 18 | /__ /<_(\ | /__ /<_(\ | Yes | 5.33 |
| 19 | (\(//\ (( | (\(//\ (( | Yes | 9.84 |
| 20 | \()\ _//\ | \()\ _//\ | Yes | 8.15 |
