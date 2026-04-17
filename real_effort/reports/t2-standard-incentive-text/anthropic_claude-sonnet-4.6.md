# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-27 09:59:50

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
| sudoku_game | 6335 | 32118 | 38453 | 13 | 7 | 22.72 | 454.42 |
| add_numbers | 3720 | 789 | 4509 | 20 | 0 | 2.40 | 48.04 |
| counting_zeros | 5040 | 15494 | 20534 | 7 | 13 | 10.05 | 200.99 |
| task_decoding | 5040 | 2387 | 7427 | 20 | 0 | 3.51 | 70.21 |
| task_summation | 5100 | 3430 | 8530 | 20 | 0 | 3.67 | 73.37 |
| task_transcription | 3886 | 750 | 4636 | 20 | 0 | 2.48 | 49.54 |
| task_sequences | 3781 | 3493 | 7274 | 20 | 0 | 4.33 | 86.56 |
| string_entry | 4254 | 1361 | 5615 | 13 | 7 | 3.01 | 60.28 |
| **TOTAL** | **37156** | **59822** | **96978** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 3 4 1 5 2 2 1 5 1 4 5 6 | 4 3 3 4 1 5 2 2 1 5 1 4 5 6 | Yes | 22.3 |
| 2 | 4 3 6 4 4 3 1 5 6 4 2 4 3 5 | 4 3 6 4 4 3 1 5 6 4 2 4 3 5 | Yes | 21.26 |
| 3 | 5 1 4 5 3 1 5 6 4 2 3 2 4 2 | 5 1 4 5 3 1 5 6 4 2 3 2 4 2 | Yes | 17.15 |
| 4 | 3 6 5 4 2 3 6 1 6 5 4 2 5 6 | 3 6 5 4 2 3 6 1 6 1 5 4 2 5 6 | No | 22.46 |
| 5 | 2 6 1 5 3 6 2 1 3 2 6 3 6 4 | 2 6 1 5 3 6 2 1 3 2 6 3 6 4 | Yes | 24.64 |
| 6 | 2 3 6 4 6 3 2 5 6 1 2 6 4 3 | 2 3 6 4 6 3 2 5 6 1 2 6 4 3 | Yes | 23.78 |
| 7 | 5 1 4 2 1 4 3 5 2 2 4 2 3 1 | 5 1 4 2 1 4 1 3 5 2 2 3 1 | No | 28.5 |
| 8 | 5 5 1 6 2 3 4 4 6 1 6 5 4 3 | 5 5 1 6 2 3 4 4 6 1 6 5 4 3 | Yes | 20.57 |
| 9 | 1 2 1 5 4 4 1 3 3 2 2 4 2 1 | 1 2 1 5 4 4 1 3 3 2 2 4 2 1 | Yes | 18.92 |
| 10 | 6 4 5 4 4 6 2 4 6 6 5 2 1 4 | 6 4 5 4 4 6 2 6 4 6 5 2 1 4 | No | 27.56 |
| 11 | 3 6 1 2 4 3 6 1 2 5 4 5 3 6 | 3 6 1 2 4 1 5 3 6 1 2 5 4 5 3 6 | No | 15.72 |
| 12 | 3 5 6 2 5 3 5 4 5 4 1 6 1 6 | 3 5 6 2 5 3 5 4 5 4 1 6 1 6 | Yes | 18.82 |
| 13 | 5 4 1 5 4 1 4 5 4 1 3 3 6 2 |  | No | 35.0 |
| 14 | 5 4 3 6 1 5 1 5 3 6 5 3 6 1 | 5 4 3 6 1 5 1 5 3 6 5 3 6 1 | Yes | 20.99 |
| 15 | 4 6 5 1 3 6 3 6 6 2 2 3 6 2 | 4 6 5 1 3 6 3 6 6 2 2 3 6 2 | Yes | 19.03 |
| 16 | 4 4 3 5 1 5 6 4 5 1 5 2 6 3 | 4 4 3 5 1 5 6 4 5 1 5 2 6 3 | Yes | 26.56 |
| 17 | 2 3 5 5 4 1 2 3 5 3 1 5 2 2 | 2 3 5 5 4 1 3 5 2 2 1 3 5 2 | No | 24.0 |
| 18 | 1 5 4 4 6 3 2 2 6 1 5 2 4 3 | 1 5 4 4 6 3 2 2 6 1 5 2 4 3 | Yes | 22.28 |
| 19 | 1 5 3 4 6 4 5 2 3 6 2 3 4 1 | 1 5 2 3 4 6 4 5 2 3 6 2 3 4 1 | No | 24.02 |
| 20 | 5 4 3 5 3 6 1 2 3 6 2 5 1 4 | 5 4 3 5 3 6 1 2 3 6 2 5 1 4 | Yes | 20.8 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1186 | 1186 | Yes | 1.84 |
| 2 | 1662 | 1662 | Yes | 1.71 |
| 3 | 672 | 672 | Yes | 1.97 |
| 4 | 2623 | 2623 | Yes | 1.06 |
| 5 | 1835 | 1835 | Yes | 1.59 |
| 6 | 1772 | 1772 | Yes | 3.57 |
| 7 | 2037 | 2037 | Yes | 3.71 |
| 8 | 2160 | 2160 | Yes | 4.96 |
| 9 | 1596 | 1596 | Yes | 1.83 |
| 10 | 2620 | 2620 | Yes | 4.33 |
| 11 | 1944 | 1944 | Yes | 2.72 |
| 12 | 1423 | 1423 | Yes | 3.17 |
| 13 | 1668 | 1668 | Yes | 1.85 |
| 14 | 1721 | 1721 | Yes | 2.3 |
| 15 | 2128 | 2128 | Yes | 1.62 |
| 16 | 1620 | 1620 | Yes | 1.83 |
| 17 | 2230 | 2230 | Yes | 1.82 |
| 18 | 1838 | 1838 | Yes | 1.58 |
| 19 | 1198 | 1198 | Yes | 2.95 |
| 20 | 1643 | 1643 | Yes | 1.62 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 58 | 58 | Yes | 10.62 |
| 2 | 47 | 47 | Yes | 9.61 |
| 3 | 50 | 49 | No | 8.08 |
| 4 | 45 | 45 | Yes | 16.6 |
| 5 | 35 | 35 | Yes | 10.37 |
| 6 | 74 | 69 | No | 8.09 |
| 7 | 55 | 48 | No | 8.19 |
| 8 | 40 | 37 | No | 5.87 |
| 9 | 59 | 55 | No | 16.45 |
| 10 | 56 | 54 | No | 7.23 |
| 11 | 67 | 50 | No | 4.92 |
| 12 | 67 | 64 | No | 8.99 |
| 13 | 38 | 38 | Yes | 16.62 |
| 14 | 38 | 38 | Yes | 10.62 |
| 15 | 46 | 40 | No | 11.01 |
| 16 | 59 | 53 | No | 12.55 |
| 17 | 69 | 62 | No | 8.49 |
| 18 | 67 | 66 | No | 9.73 |
| 19 | 42 | 42 | Yes | 11.49 |
| 20 | 46 | 40 | No | 5.42 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | KABDEQY | KABDEQY | Yes | 7.45 |
| 2 | VWBUJHK | VWBUJHK | Yes | 3.29 |
| 3 | QYTWSNB | QYTWSNB | Yes | 3.43 |
| 4 | PBCKLQZ | PBCKLQZ | Yes | 4.18 |
| 5 | VXJWETM | VXJWETM | Yes | 2.63 |
| 6 | DZPIALK | DZPIALK | Yes | 3.26 |
| 7 | ALKIXHO | ALKIXHO | Yes | 2.54 |
| 8 | DUSMKZX | DUSMKZX | Yes | 3.09 |
| 9 | EMUNKDA | EMUNKDA | Yes | 2.94 |
| 10 | HTAKPEW | HTAKPEW | Yes | 2.67 |
| 11 | GBCLRFY | GBCLRFY | Yes | 3.92 |
| 12 | KBPCZUR | KBPCZUR | Yes | 4.33 |
| 13 | SNHTLRJ | SNHTLRJ | Yes | 3.35 |
| 14 | PFBCXRV | PFBCXRV | Yes | 2.17 |
| 15 | UJIVTKS | UJIVTKS | Yes | 2.64 |
| 16 | VWDJNGT | VWDJNGT | Yes | 2.07 |
| 17 | JACZIBP | JACZIBP | Yes | 4.67 |
| 18 | SQXZCWL | SQXZCWL | Yes | 3.69 |
| 19 | XZMDCIP | XZMDCIP | Yes | 4.09 |
| 20 | FTUMZLR | FTUMZLR | Yes | 3.81 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 8.5 1.5 | Yes | 6.13 |
| 2 | [2.2, 7.8] | 2.2 7.8 | Yes | 3.88 |
| 3 | [2.4, 7.6] | 7.6 2.4 | Yes | 4.42 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 3.55 |
| 5 | [4.2, 5.8] | 4.2 5.8 | Yes | 5.09 |
| 6 | [0.2, 9.8] | 9.8 0.2 | Yes | 2.93 |
| 7 | [2.7, 7.3] | 2.7 7.3 | Yes | 2.48 |
| 8 | [2.3, 7.7] | 7.7 2.3 | Yes | 4.11 |
| 9 | [4.9, 5.1] | 4.9 5.1 | Yes | 3.59 |
| 10 | [1.3, 8.7] | 8.7 1.3 | Yes | 3.35 |
| 11 | [3.6, 6.4] | 3.6 6.4 | Yes | 2.12 |
| 12 | [4.3, 5.7] | 5.7 4.3 | Yes | 3.87 |
| 13 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.68 |
| 14 | [2.6, 7.4] | 7.4 2.6 | Yes | 6.02 |
| 15 | [2.7, 7.3] | 2.7 7.3 | Yes | 4.05 |
| 16 | [3.9, 6.1] | 3.9 6.1 | Yes | 3.08 |
| 17 | [2.6, 7.4] | 7.4 2.6 | Yes | 3.43 |
| 18 | [1.3, 8.7] | 1.3 8.7 | Yes | 2.27 |
| 19 | [4.4, 5.6] | 4.4 5.6 | Yes | 2.6 |
| 20 | [4.8, 5.2] | 4.8 5.2 | Yes | 1.71 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | B37ZADFOIYP7 | B37ZADFOIYP7 | Yes | 2.49 |
| 2 | FWPMNVHV2O9L | FWPMNVHV2O9L | Yes | 1.65 |
| 3 | 77JTUCEDZOX6 | 77JTUCEDZOX6 | Yes | 2.96 |
| 4 | 3UEYIXNUEQVM | 3UEYIXNUEQVM | Yes | 1.71 |
| 5 | HMN20GK6UDN8 | HMN20GK6UDN8 | Yes | 1.05 |
| 6 | Y2WGKIW0DCN4 | Y2WGKIW0DCN4 | Yes | 2.39 |
| 7 | 5WB8OOYC2OFA | 5WB8OOYC2OFA | Yes | 1.84 |
| 8 | FNMOQBR3WDZ4 | FNMOQBR3WDZ4 | Yes | 1.69 |
| 9 | LBTA3BZ7E8J2 | LBTA3BZ7E8J2 | Yes | 1.96 |
| 10 | SJ712XC3LFBV | SJ712XC3LFBV | Yes | 1.73 |
| 11 | IZH88CM2LZDJ | IZH88CM2LZDJ | Yes | 1.7 |
| 12 | Y9W2HL5XIV80 | Y9W2HL5XIV80 | Yes | 4.53 |
| 13 | BLOQ5URTFLLW | BLOQ5URTFLLW | Yes | 2.52 |
| 14 | KN5SGFZ81MU9 | KN5SGFZ81MU9 | Yes | 2.71 |
| 15 | ZOZVR6X6VFUJ | ZOZVR6X6VFUJ | Yes | 2.14 |
| 16 | P34JPVQQT3MQ | P34JPVQQT3MQ | Yes | 2.58 |
| 17 | TCIAHWYCH5SG | TCIAHWYCH5SG | Yes | 2.92 |
| 18 | UM26T9JXNFGV | UM26T9JXNFGV | Yes | 6.65 |
| 19 | OTTINY7O9AKK | OTTINY7O9AKK | Yes | 2.74 |
| 20 | TQC9SSKTVYM3 | TQC9SSKTVYM3 | Yes | 1.56 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 5 | Yes | 2.42 |
| 2 | 39 | 39 | Yes | 2.73 |
| 3 | 1 | 1 | Yes | 3.8 |
| 4 | 4096 | 4096 | Yes | 8.83 |
| 5 | 64 | 64 | Yes | 4.4 |
| 6 | 73 | 73 | Yes | 2.53 |
| 7 | 243 | 243 | Yes | 1.43 |
| 8 | 10 | 10 | Yes | 4.74 |
| 9 | 1440 | 1440 | Yes | 11.89 |
| 10 | 26 | 26 | Yes | 12.39 |
| 11 | 7 | 7 | Yes | 1.93 |
| 12 | 198 | 198 | Yes | 1.61 |
| 13 | 9 | 9 | Yes | 2.99 |
| 14 | 16 | 16 | Yes | 2.27 |
| 15 | 4 | 4 | Yes | 2.87 |
| 16 | 7680 | 7680 | Yes | 2.72 |
| 17 | 60 | 60 | Yes | 2.09 |
| 18 | 6 | 6 | Yes | 2.25 |
| 19 | 20 | 20 | Yes | 10.4 |
| 20 | 31 | 31 | Yes | 2.27 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <)_\<)_(\ | <)_\<)_(\ | Yes | 2.57 |
| 2 | _ /(\< <( | _ /(\< <( | Yes | 2.39 |
| 3 | )( \_//// | )( \_//// | Yes | 1.81 |
| 4 | </__</_/_ | </__</_/_ | Yes | 4.4 |
| 5 | \ //_(/</ | \ //_(/</ | Yes | 3.91 |
| 6 | _</_\)/(_ | _</_\)/(_ | Yes | 2.91 |
| 7 | \\/_ (<_) | \\/_  (<_) | No | 3.49 |
| 8 |  (< __)_  | (<  __)_ | No | 3.24 |
| 9 |  \_\/<__  | \_\/<__ | No | 3.8 |
| 10 |  \_(( \ ( | \_(( \ ( | No | 6.21 |
| 11 | )_\/_// / | )_\/_// / | Yes | 2.34 |
| 12 | _<\)<(()/ | _<\)<(()/ | Yes | 3.71 |
| 13 | (\/ (( </ | (\/ (( </ | Yes | 1.7 |
| 14 |  <_/\)\<( | <_/\)\<( | No | 2.16 |
| 15 | /(( ()_// | /(( ()_// | Yes | 4.18 |
| 16 | )_//_/\\) | )_//_/\\) | Yes | 2.27 |
| 17 | \)_/ ( /\ | \)_/ ( /\ | Yes | 1.86 |
| 18 |  < \(<_ ) | < \(<_ ) | No | 2.41 |
| 19 | )_ _ <))\ | )_ _<))\ | No | 1.8 |
| 20 | </\\()<// | </\\()<// | Yes | 3.11 |
