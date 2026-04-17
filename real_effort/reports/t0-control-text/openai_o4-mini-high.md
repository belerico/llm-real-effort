# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-26 16:04:39

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
| sudoku_game | 4662 | 40960 | 45622 | 0 | 20 | 39.76 | 795.33 |
| add_numbers | 2420 | 3172 | 5592 | 20 | 0 | 2.89 | 57.9 |
| counting_zeros | 3820 | 39646 | 43466 | 4 | 16 | 23.88 | 477.59 |
| task_decoding | 3572 | 10773 | 14345 | 19 | 1 | 14.21 | 284.24 |
| task_summation | 4100 | 18541 | 22641 | 20 | 0 | 10.96 | 219.28 |
| task_transcription | 2563 | 2817 | 5380 | 20 | 0 | 2.80 | 56.07 |
| task_sequences | 2421 | 13070 | 15491 | 18 | 2 | 8.67 | 173.39 |
| string_entry | 2860 | 35766 | 38626 | 3 | 17 | 31.55 | 630.99 |
| **TOTAL** | **26418** | **164745** | **191163** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 5 3 4 5 3 1 2 4 1 2 6 6 4 |  | No | 34.37 |
| 2 | 1 2 4 2 5 6 5 4 2 5 1 3 6 1 |  | No | 47.51 |
| 3 | 4 1 5 3 6 5 4 3 6 2 1 4 6 5 |  | No | 39.69 |
| 4 | 2 6 1 4 5 2 3 5 6 1 4 2 2 5 |  | No | 36.65 |
| 5 | 5 1 4 5 6 4 5 2 2 6 5 4 3 6 |  | No | 45.96 |
| 6 | 6 5 4 5 4 6 1 2 4 5 3 4 2 6 |  | No | 38.05 |
| 7 | 4 6 6 1 3 5 2 2 4 5 1 4 6 5 |  | No | 29.61 |
| 8 | 5 1 2 4 3 5 3 1 2 6 4 3 1 2 |  | No | 31.82 |
| 9 | 4 5 2 6 6 5 3 5 1 2 2 5 1 3 |  | No | 41.26 |
| 10 | 3 1 2 4 1 6 4 3 2 1 4 5 3 4 |  | No | 45.42 |
| 11 | 4 4 1 1 2 3 3 6 2 5 1 6 3 2 |  | No | 55.42 |
| 12 | 2 5 4 6 6 5 6 4 3 3 6 6 3 1 |  | No | 46.11 |
| 13 | 2 6 3 3 5 4 1 3 3 1 2 3 2 1 |  | No | 25.66 |
| 14 | 6 5 6 2 2 5 6 5 1 6 5 4 4 1 |  | No | 31.5 |
| 15 | 1 4 1 6 2 1 3 4 6 1 5 4 3 1 |  | No | 58.32 |
| 16 | 1 5 3 2 1 5 4 5 6 3 4 6 2 1 |  | No | 31.68 |
| 17 | 4 6 1 1 2 6 2 6 3 1 6 5 4 3 |  | No | 31.32 |
| 18 | 6 4 2 2 6 4 6 1 3 2 5 1 1 3 |  | No | 43.34 |
| 19 | 6 4 1 2 4 1 5 2 1 6 6 6 5 3 |  | No | 40.05 |
| 20 | 5 4 6 1 6 4 2 5 2 4 2 6 6 3 |  | No | 41.55 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1801 | 1801 | Yes | 2.0 |
| 2 | 670 | 670 | Yes | 2.31 |
| 3 | 2616 | 2616 | Yes | 5.05 |
| 4 | 1290 | 1290 | Yes | 2.18 |
| 5 | 1060 | 1060 | Yes | 2.28 |
| 6 | 1382 | 1382 | Yes | 2.11 |
| 7 | 1342 | 1342 | Yes | 2.49 |
| 8 | 2111 | 2111 | Yes | 3.49 |
| 9 | 928 | 928 | Yes | 3.36 |
| 10 | 1345 | 1345 | Yes | 1.96 |
| 11 | 2317 | 2317 | Yes | 2.48 |
| 12 | 1663 | 1663 | Yes | 2.41 |
| 13 | 2548 | 2548 | Yes | 2.8 |
| 14 | 1812 | 1812 | Yes | 1.99 |
| 15 | 1580 | 1580 | Yes | 5.42 |
| 16 | 2323 | 2323 | Yes | 2.36 |
| 17 | 1965 | 1965 | Yes | 1.97 |
| 18 | 1547 | 1547 | Yes | 3.77 |
| 19 | 464 | 464 | Yes | 4.24 |
| 20 | 1469 | 1469 | Yes | 3.22 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 |  | No | 22.33 |
| 2 | 44 |  | No | 21.59 |
| 3 | 71 |  | No | 30.78 |
| 4 | 42 |  | No | 20.93 |
| 5 | 75 |  | No | 19.91 |
| 6 | 63 |  | No | 20.06 |
| 7 | 61 |  | No | 21.87 |
| 8 | 55 | 55 | Yes | 17.75 |
| 9 | 64 |  | No | 17.68 |
| 10 | 72 |  | No | 31.8 |
| 11 | 53 | 53 | Yes | 20.83 |
| 12 | 73 |  | No | 34.46 |
| 13 | 46 |  | No | 17.77 |
| 14 | 65 |  | No | 23.86 |
| 15 | 50 |  | No | 24.57 |
| 16 | 52 |  | No | 23.78 |
| 17 | 67 | 67 | Yes | 12.79 |
| 18 | 72 |  | No | 38.28 |
| 19 | 74 |  | No | 40.09 |
| 20 | 57 | 57 | Yes | 16.43 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LWTZANR | LWTZANR | Yes | 9.11 |
| 2 | XOLYQDV | XOLYQDV | Yes | 3.84 |
| 3 | HEJZCVP | HEJZCVP | Yes | 3.44 |
| 4 | SPFLUGT | SPFLUGT | Yes | 17.37 |
| 5 | SNKWDTJ | SNKWDTJ | Yes | 3.7 |
| 6 | ZHNWEID | ZHNWEID | Yes | 8.88 |
| 7 | DLZTEVH | DLZTEVH | Yes | 3.4 |
| 8 | PTNGKAD | PTNGKAD | Yes | 6.7 |
| 9 | CRYXPGB | CRYXPGB | Yes | 9.45 |
| 10 | FKVIBXH | FKVIBXH | Yes | 6.28 |
| 11 | ISQKVNO | ISQKVNO | Yes | 8.25 |
| 12 | DIXRHLY | DIXRHLY | Yes | 14.06 |
| 13 | LQMPYUT | LQMPYUT | Yes | 8.51 |
| 14 | TGBLWJV | TGBLWJV | Yes | 11.05 |
| 15 | EQFONYP | EQFONYP | Yes | 10.29 |
| 16 | WAIHNQD | WAIHNQD | Yes | 14.38 |
| 17 | HSVBARW | HSVBARW | Yes | 13.39 |
| 18 | QMAOPUE | TIMEOUT | No | 120.03 |
| 19 | XVNJRWE | XVNJRWE | Yes | 8.44 |
| 20 | IFYAQBO | IFYAQBO | Yes | 3.66 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.4, 7.6] | 2.4 7.6 | Yes | 8.72 |
| 2 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.21 |
| 3 | [0.8, 9.2] | 0.8 9.2 | Yes | 8.91 |
| 4 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.07 |
| 5 | [3.0, 7.0] | 3.0 7.0 | Yes | 14.89 |
| 6 | [1.3, 8.7] | 8.7 1.3 | Yes | 9.55 |
| 7 | [0.4, 9.6] | 0.4 9.6 | Yes | 11.13 |
| 8 | [0.1, 9.9] | 9.9 0.1 | Yes | 9.59 |
| 9 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.85 |
| 10 | [2.9, 7.1] | 2.9 7.1 | Yes | 10.84 |
| 11 | [1.7, 8.3] | 1.7 8.3 | Yes | 15.64 |
| 12 | [0.9, 9.1] | 9.1 0.9 | Yes | 7.05 |
| 13 | [3.8, 6.2] | 3.8 6.2 | Yes | 9.83 |
| 14 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.24 |
| 15 | [4.9, 5.1] | 4.9 5.1 | Yes | 11.76 |
| 16 | [1.6, 8.4] | 1.6 8.4 | Yes | 12.63 |
| 17 | [1.4, 8.6] | 1.4 8.6 | Yes | 8.84 |
| 18 | [2.1, 7.9] | 2.1 7.9 | Yes | 12.33 |
| 19 | [1.9, 8.1] | 1.9 8.1 | Yes | 13.07 |
| 20 | [2.1, 7.9] | 2.1 7.9 | Yes | 16.13 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5LIJ4IDTKZ77 | 5LIJ4IDTKZ77 | Yes | 2.96 |
| 2 | 6KEYC4PSNC7R | 6KEYC4PSNC7R | Yes | 2.42 |
| 3 | HKTTFR5P76G5 | HKTTFR5P76G5 | Yes | 2.29 |
| 4 | 7P7H76HRGQGA | 7P7H76HRGQGA | Yes | 5.36 |
| 5 | 3UF2IOCNCO4L | 3UF2IOCNCO4L | Yes | 2.42 |
| 6 | PKXJN5FLBLK1 | PKXJN5FLBLK1 | Yes | 3.76 |
| 7 | ZKR3RFAHG5EI | ZKR3RFAHG5EI | Yes | 2.26 |
| 8 | JKQ6EHN3JL2S | JKQ6EHN3JL2S | Yes | 1.97 |
| 9 | FNBDVS722OWN | FNBDVS722OWN | Yes | 2.41 |
| 10 | ULAS4CMHKMH0 | ULAS4CMHKMH0 | Yes | 2.58 |
| 11 | U8A0WGA9OAOQ | U8A0WGA9OAOQ | Yes | 2.44 |
| 12 | HTWREMLC4VHC | HTWREMLC4VHC | Yes | 2.04 |
| 13 | SX4XOEU6W7W8 | SX4XOEU6W7W8 | Yes | 3.82 |
| 14 | BPFMRGT4V6XH | BPFMRGT4V6XH | Yes | 6.08 |
| 15 | ZL6PU3GMT2JY | ZL6PU3GMT2JY | Yes | 2.08 |
| 16 | VAVPHUTL4HWU | VAVPHUTL4HWU | Yes | 1.99 |
| 17 | 9NS0VF7WJNY0 | 9NS0VF7WJNY0 | Yes | 2.09 |
| 18 | QVUPONE4UE87 | QVUPONE4UE87 | Yes | 2.01 |
| 19 | 7TOAIMNULKXW | 7TOAIMNULKXW | Yes | 1.86 |
| 20 | 4K3LRUYBDTWH | 4K3LRUYBDTWH | Yes | 3.22 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 10.64 |
| 2 | 73 | 73 | Yes | 4.31 |
| 3 | 67 | 67 | Yes | 5.06 |
| 4 | 4 | 4 | Yes | 10.39 |
| 5 | 44 | 44 | Yes | 13.78 |
| 6 | 793 | 793 | Yes | 6.68 |
| 7 | 26 | 29 | No | 17.63 |
| 8 | 31 | 31 | Yes | 4.51 |
| 9 | 3 | 3 | Yes | 5.1 |
| 10 | 16 | 16 | Yes | 3.06 |
| 11 | 1440 | 1440 | Yes | 7.58 |
| 12 | 10 | 10 | Yes | 15.44 |
| 13 | 243 | 243 | Yes | 2.94 |
| 14 | 5 | 5 | Yes | 5.02 |
| 15 | 48 | 48 | Yes | 9.95 |
| 16 | 60 | 60 | Yes | 7.02 |
| 17 | 36 | 36 | Yes | 3.26 |
| 18 | 19 | 19 | Yes | 3.51 |
| 19 | 4096 |  | No | 29.29 |
| 20 | 60 | 60 | Yes | 8.2 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /) )<<)\_ | /) )<<)\_ | Yes | 7.57 |
| 2 | _) \ (\/) |  | No | 25.1 |
| 3 | \ / \\))) | \ / \\))) | Yes | 18.1 |
| 4 |  _\\(/_\) |  | No | 25.02 |
| 5 | \</<_)\</ |  | No | 21.74 |
| 6 | ) __\_(// | /\) <(_<) | No | 12.87 |
| 7 | (<<(_) )_ |  | No | 49.14 |
| 8 | <\<\(<(\< |  | No | 21.74 |
| 9 | \  \_ ))/ |  | No | 22.93 |
| 10 | ) (\/\)_  |  | No | 30.12 |
| 11 | <_(/)_) / |  | No | 27.25 |
| 12 | _<_( \<<  |  | No | 59.26 |
| 13 | /\<</<_)/ | /\<</<_)/ | Yes | 13.8 |
| 14 | \/ ))\(\< |  | No | 21.93 |
| 15 |  \ )( ))/ | \ ) ( ))/ | No | 6.28 |
| 16 | )<() _<_/ |  | No | 57.15 |
| 17 | )_\( (\ \ |  | No | 117.77 |
| 18 | )\)\(<\)/ |  | No | 27.46 |
| 19 | /)__)\_\  |  | No | 38.13 |
| 20 | _)<_)/\_  |  | No | 27.59 |
