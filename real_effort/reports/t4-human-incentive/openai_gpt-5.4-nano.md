# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 10:59:58

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
| sudoku_game | 7540 | 40094 | 47634 | 5 | 15 | 42.73 | 854.89 |
| add_numbers | 4120 | 1201 | 5321 | 20 | 0 | 3.56 | 71.39 |
| counting_zeros | 6540 | 34293 | 40833 | 0 | 20 | 36.85 | 737.29 |
| task_decoding | 12280 | 4855 | 17135 | 20 | 0 | 5.61 | 112.37 |
| task_summation | 7480 | 6468 | 13948 | 20 | 0 | 5.97 | 119.49 |
| task_transcription | 3950 | 8917 | 12867 | 7 | 13 | 8.05 | 161.07 |
| task_sequences | 3240 | 8294 | 11534 | 17 | 3 | 7.28 | 145.56 |
| string_entry | 4540 | 26018 | 30558 | 14 | 6 | 17.41 | 348.36 |
| **TOTAL** | **49690** | **130140** | **179830** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 1 5 6 3 6 2 5 4 2 5 4 3 6 |  | No | 46.34 |
| 2 | 5 1 2 6 3 4 1 2 6 2 2 5 4 3 |  | No | 49.69 |
| 3 | 5 1 1 3 5 6 3 6 3 5 4 6 2 1 |  | No | 81.01 |
| 4 | 4 3 1 6 6 1 4 3 4 1 6 5 2 4 | 4 3 1 6 6 1 4 3 4 1 6 5 2 4 | Yes | 21.56 |
| 5 | 5 3 2 1 3 1 5 3 6 3 4 1 4 2 |  | No | 55.69 |
| 6 | 5 3 4 2 6 5 2 3 1 5 2 3 6 1 | 5 3 4 2 6 5 2 3 1 5 2 3 6 1 | Yes | 24.03 |
| 7 | 5 1 6 2 3 1 2 3 6 1 5 4 4 2 |  | No | 56.67 |
| 8 | 1 6 4 3 3 5 6 4 2 4 3 6 3 2 | 1 6 4 3 3 5 6 4 2 4 3 6 3 2 | Yes | 19.19 |
| 9 | 2 5 5 2 5 4 2 3 5 2 1 6 1 3 |  | No | 41.77 |
| 10 | 5 6 1 4 2 6 3 6 3 5 3 5 4 3 | 5 6 1 4 2 6 3 6 3 5 3 5 4 3 | Yes | 30.73 |
| 11 | 6 3 3 1 6 4 2 1 1 5 6 3 1 4 |  | No | 53.82 |
| 12 | 2 6 6 2 3 1 6 4 2 5 6 4 3 5 |  | No | 46.72 |
| 13 | 2 1 5 3 1 6 4 6 6 2 5 1 4 2 |  | No | 41.91 |
| 14 | 5 4 2 2 3 4 5 2 5 4 1 5 6 5 |  | No | 46.45 |
| 15 | 5 6 4 2 2 3 4 4 6 3 4 6 2 4 |  | No | 23.48 |
| 16 | 1 6 4 5 3 2 6 1 2 6 2 6 6 4 |  | No | 44.57 |
| 17 | 1 5 2 1 3 5 4 3 6 6 4 1 2 1 |  | No | 43.92 |
| 18 | 2 3 2 5 3 5 1 2 5 6 1 5 6 3 |  | No | 51.88 |
| 19 | 4 3 3 2 6 1 2 6 1 3 5 1 6 4 | 4 3 3 2 6 1 2 6 1 3 5 1 6 4 | Yes | 26.1 |
| 20 | 3 4 6 6 5 1 2 4 6 6 1 4 3 4 |  | No | 49.16 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1872 | 1872 | Yes | 5.11 |
| 2 | 1460 | 1460 | Yes | 4.02 |
| 3 | 1197 | 1197 | Yes | 4.23 |
| 4 | 1859 | 1859 | Yes | 3.55 |
| 5 | 1190 | 1190 | Yes | 3.71 |
| 6 | 1448 | 1448 | Yes | 3.09 |
| 7 | 1068 | 1068 | Yes | 3.11 |
| 8 | 1270 | 1270 | Yes | 3.05 |
| 9 | 1593 | 1593 | Yes | 3.0 |
| 10 | 1501 | 1501 | Yes | 3.47 |
| 11 | 1647 | 1647 | Yes | 3.62 |
| 12 | 1556 | 1556 | Yes | 4.43 |
| 13 | 1914 | 1914 | Yes | 3.43 |
| 14 | 1434 | 1434 | Yes | 3.09 |
| 15 | 1630 | 1630 | Yes | 3.19 |
| 16 | 2069 | 2069 | Yes | 3.03 |
| 17 | 1645 | 1645 | Yes | 3.57 |
| 18 | 2132 | 2132 | Yes | 3.46 |
| 19 | 1623 | 1623 | Yes | 2.97 |
| 20 | 2087 | 2087 | Yes | 4.14 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 52 | 67 | No | 21.21 |
| 2 | 74 |  | No | 60.59 |
| 3 | 39 | 67 | No | 16.66 |
| 4 | 47 | 67 | No | 17.47 |
| 5 | 71 | 68 | No | 20.78 |
| 6 | 75 |  | No | 45.6 |
| 7 | 73 | 67 | No | 22.13 |
| 8 | 72 |  | No | 47.9 |
| 9 | 65 | 67 | No | 24.76 |
| 10 | 38 |  | No | 55.4 |
| 11 | 49 | 67 | No | 18.28 |
| 12 | 48 | 67 | No | 20.54 |
| 13 | 47 | 67 | No | 17.31 |
| 14 | 54 | 67 | No | 21.47 |
| 15 | 40 |  | No | 52.76 |
| 16 | 35 | 67 | No | 27.41 |
| 17 | 45 |  | No | 74.6 |
| 18 | 58 |  | No | 61.95 |
| 19 | 49 |  | No | 54.04 |
| 20 | 45 |  | No | 56.13 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | INGDAEY | INGDAEY | Yes | 9.57 |
| 2 | QUXHOWD | QUXHOWD | Yes | 6.92 |
| 3 | MYAQEDR | MYAQEDR | Yes | 5.77 |
| 4 | LXZOWIF | LXZOWIF | Yes | 3.96 |
| 5 | FLHSPAW | FLHSPAW | Yes | 4.86 |
| 6 | JKLVUAY | JKLVUAY | Yes | 4.99 |
| 7 | UYKFXNM | UYKFXNM | Yes | 5.24 |
| 8 | VKCWBSI | VKCWBSI | Yes | 6.99 |
| 9 | AXCMEOH | AXCMEOH | Yes | 6.04 |
| 10 | AYBHKDO | AYBHKDO | Yes | 6.31 |
| 11 | DBRXNTZ | DBRXNTZ | Yes | 2.57 |
| 12 | OBLKPNR | OBLKPNR | Yes | 4.66 |
| 13 | YZBUHFX | YZBUHFX | Yes | 7.26 |
| 14 | HNMYOBC | HNMYOBC | Yes | 5.76 |
| 15 | GDHBWXM | GDHBWXM | Yes | 5.75 |
| 16 | CYFRXKM | CYFRXKM | Yes | 5.51 |
| 17 | KEIRVWU | KEIRVWU | Yes | 2.78 |
| 18 | IZVGFEL | IZVGFEL | Yes | 8.8 |
| 19 | ZPICLNX | ZPICLNX | Yes | 5.2 |
| 20 | VSTYROF | VSTYROF | Yes | 3.2 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.55 |
| 2 | [3.2, 6.8] | 6.8 3.2 | Yes | 5.79 |
| 3 | [4.1, 5.9] | 4.1 5.9 | Yes | 5.26 |
| 4 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.69 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.64 |
| 6 | [1.5, 8.5] | 1.5 8.5 | Yes | 6.02 |
| 7 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.57 |
| 8 | [1.5, 8.5] | 1.5 8.5 | Yes | 6.73 |
| 9 | [3.7, 6.3] | 6.3 3.7 | Yes | 5.44 |
| 10 | [3.6, 6.4] | 6.4 3.6 | Yes | 5.5 |
| 11 | [0.1, 9.9] | 0.1 9.9 | Yes | 5.39 |
| 12 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.08 |
| 13 | [2.1, 7.9] | 7.9 2.1 | Yes | 8.95 |
| 14 | [1.2, 8.8] | 8.8 1.2 | Yes | 6.65 |
| 15 | [1.2, 8.8] | 8.8 1.2 | Yes | 6.41 |
| 16 | [4.9, 5.1] | 4.9 5.1 | Yes | 6.04 |
| 17 | [3.4, 6.6] | 6.6 3.4 | Yes | 4.71 |
| 18 | [4.5, 5.5] | 5.5 4.5 | Yes | 4.37 |
| 19 | [3.3, 6.7] | 3.3 6.7 | Yes | 5.97 |
| 20 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.56 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3C7JBSM2RTSM | 3C7JBSM2RTSM | Yes | 14.82 |
| 2 | KJX4L3SMLFWC | KJX4L3SMLFWC | Yes | 4.63 |
| 3 | SN0MN4Y0LU4A | SNOMNAYOLU4A | No | 11.37 |
| 4 | VK6K97CH9P3X | VK6KS7CH9P3X | No | 6.03 |
| 5 | UYGN6UHYCVZH | UVGN6UHYCVZH | No | 4.34 |
| 6 | 57VL5SBONZB5 | 57VL5SB0NZE5 | No | 12.66 |
| 7 | OAQ312FFROXL | 0A0312FFROXL | No | 13.34 |
| 8 | KQKWF1CE2J1H | KOKWFICE2J1H | No | 4.91 |
| 9 | H3Y238VMX9M3 | H3Y238VMX9M3 | Yes | 3.17 |
| 10 | 40MYBCH4KZQ1 | 40MYBCH4KZ01 | No | 10.03 |
| 11 | XE3YPCEIWYUH | XE3YPCEIWYUH | Yes | 6.86 |
| 12 | XRVG8JWZRU2Q | XRVG8JWZRU2Q | Yes | 5.53 |
| 13 | FBZ69RIKGH11 | FBZ69R1KGH11 | No | 5.3 |
| 14 | QM2MV7IVINTU | QM2MV7IVINTU | Yes | 4.48 |
| 15 | JX2F1OJJH3SX | JX2F10JIH3SX | No | 9.85 |
| 16 | I3TWYU8Y2HPB | 13TWYUY8Y2HPB | No | 6.28 |
| 17 | MR4WI5RVYHKK | MR4W15RVYHKK | No | 7.18 |
| 18 | RG65BVEQS4Q4 | RG65BVEOS404 | No | 9.85 |
| 19 | KWKALJ6T9WI4 | KWKALJ6T9WI4 | Yes | 8.02 |
| 20 | U8TR8RHLRT9J | USTR8RHLRTJ | No | 12.32 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 | 64 | Yes | 4.45 |
| 2 | 4 | 4 | Yes | 9.17 |
| 3 | 44 | 44 | Yes | 4.69 |
| 4 | 3 | 3 | Yes | 11.18 |
| 5 | 6 | 6 | Yes | 7.26 |
| 6 | 10 | 8 | No | 15.98 |
| 7 | 3 | 3 | Yes | 8.16 |
| 8 | 9 | 9 | Yes | 5.64 |
| 9 | 39 | 39 | Yes | 6.99 |
| 10 | 7680 | 7680 | Yes | 4.92 |
| 11 | 26 | 7 | No | 8.22 |
| 12 | 63 | 63 | Yes | 6.11 |
| 13 | 4 | 4 | Yes | 11.09 |
| 14 | 1 | 42 | No | 9.9 |
| 15 | 23 | 23 | Yes | 4.29 |
| 16 | 73 | 73 | Yes | 6.69 |
| 17 | 48 | 48 | Yes | 2.93 |
| 18 | 65 | 65 | Yes | 6.64 |
| 19 | 7 | 7 | Yes | 3.76 |
| 20 | 9 | 9 | Yes | 7.5 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (_<) )/ _ | (_<) )/ _ | Yes | 11.06 |
| 2 | /<<<_ (<\ | /<<<_ (<\ | Yes | 16.57 |
| 3 | _\<_(\<_) | _\<_(\<_) | Yes | 11.62 |
| 4 | (/<_(\)/< | (/<_(\)/< | Yes | 6.22 |
| 5 | )</_(\/<( | )</_(\/<( | Yes | 12.52 |
| 6 | __/_(/(/  |  | No | 48.05 |
| 7 | \_  \  \/ | \_  \  \/ | Yes | 15.02 |
| 8 | /_\/ (/ \ | /_\/ (/ \ | Yes | 21.82 |
| 9 | ()__\ < < |  | No | 35.26 |
| 10 | )( // _<_ | )( // _<_ | Yes | 21.53 |
| 11 |  <_( << \ | _<(_<<_\ | No | 9.85 |
| 12 | _)/_/(/() | _)/_/(/() | Yes | 11.52 |
| 13 | <\_((<)(/ | <\_((<)(/ | Yes | 4.85 |
| 14 | /\_ ((\<< | /\_␣((\<< | Yes | 17.75 |
| 15 | ()/((_\/\ | ()/((_\/\ | Yes | 19.55 |
| 16 | \\_  /(\) | \\__/(\) | No | 19.65 |
| 17 | ) /\__ () | )_/\___() | Yes | 16.09 |
| 18 | <(/(<\\\\ | <(/(<\\\\ | Yes | 15.78 |
| 19 | _/\_()\ / | _/\_()\</ | No | 17.5 |
| 20 | ))</\ <<( | )) </\_<<( | No | 16.09 |
