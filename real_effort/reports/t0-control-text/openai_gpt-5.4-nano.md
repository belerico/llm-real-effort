# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 15:54:47

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
| sudoku_game | 4671 | 38637 | 43308 | 4 | 16 | 41.36 | 827.27 |
| add_numbers | 2420 | 754 | 3174 | 20 | 0 | 3.23 | 64.67 |
| counting_zeros | 3820 | 21178 | 24998 | 20 | 0 | 14.38 | 287.52 |
| task_decoding | 3760 | 3033 | 6793 | 18 | 2 | 4.05 | 81.06 |
| task_summation | 4100 | 6988 | 11088 | 20 | 0 | 6.07 | 121.45 |
| task_transcription | 2563 | 4351 | 6914 | 20 | 0 | 4.66 | 93.13 |
| task_sequences | 2421 | 15947 | 18368 | 14 | 6 | 14.69 | 293.79 |
| string_entry | 2862 | 28817 | 31679 | 2 | 18 | 16.67 | 333.44 |
| **TOTAL** | **26617** | **119705** | **146322** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 2 4 6 1 3 4 3 2 2 4 3 3 3 |  | No | 37.08 |
| 2 | 4 5 1 2 3 4 4 3 6 6 2 3 5 1 | 4 5 1 2 3 4 4 3 6 6 2 3 5 1 | Yes | 18.21 |
| 3 | 1 2 3 1 2 1 4 1 5 5 4 4 6 3 | 1 2 3 1 2 1 4 1 5 5 4 4 6 3 | Yes | 12.67 |
| 4 | 6 3 5 3 2 3 6 4 3 4 3 1 2 3 |  | No | 47.41 |
| 5 | 1 6 3 2 3 5 1 4 3 6 6 6 4 2 |  | No | 46.4 |
| 6 | 3 1 4 2 5 6 3 5 2 3 6 2 2 1 |  | No | 51.54 |
| 7 | 3 4 4 3 1 2 4 3 2 5 4 5 4 3 |  | No | 54.94 |
| 8 | 5 2 4 3 1 1 4 1 6 2 5 6 3 5 |  | No | 43.5 |
| 9 | 4 2 3 6 1 6 2 1 3 6 4 3 5 2 | 4 2 3 6 1 6 2 1 | No | 24.58 |
| 10 | 2 4 2 3 6 5 3 2 1 5 6 1 2 3 |  | No | 82.67 |
| 11 | 5 3 3 1 2 5 1 3 6 3 2 1 3 2 |  | No | 43.81 |
| 12 | 6 1 3 3 4 3 1 4 6 5 2 5 2 4 |  | No | 50.46 |
| 13 | 2 6 4 2 2 4 4 1 2 2 4 6 3 2 |  | No | 45.84 |
| 14 | 1 3 3 2 1 6 3 4 1 6 2 4 5 1 | 1 3 3 2 1 6 3 4 1 6 2 4 5 1 | Yes | 21.21 |
| 15 | 5 3 1 4 5 3 6 2 6 3 5 3 5 1 |  | No | 49.22 |
| 16 | 2 3 6 1 1 5 4 3 6 1 3 1 2 3 | 2 3 6 1 1 5 4 3 6 1 3 1 2 3 | Yes | 16.11 |
| 17 | 3 6 1 6 2 2 3 4 5 1 5 4 2 5 |  | No | 36.81 |
| 18 | 6 3 1 5 3 5 2 5 5 1 3 4 3 5 |  | No | 65.84 |
| 19 | 6 3 1 2 5 1 5 1 3 6 5 3 1 5 |  | No | 29.61 |
| 20 | 5 1 6 1 2 4 4 6 1 3 5 3 2 1 |  | No | 49.3 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1619 | 1619 | Yes | 1.37 |
| 2 | 1891 | 1891 | Yes | 5.07 |
| 3 | 2049 | 2049 | Yes | 3.22 |
| 4 | 1990 | 1990 | Yes | 3.08 |
| 5 | 1651 | 1651 | Yes | 3.49 |
| 6 | 570 | 570 | Yes | 3.71 |
| 7 | 1449 | 1449 | Yes | 4.91 |
| 8 | 2269 | 2269 | Yes | 2.7 |
| 9 | 1975 | 1975 | Yes | 2.48 |
| 10 | 1037 | 1037 | Yes | 2.74 |
| 11 | 1040 | 1040 | Yes | 3.32 |
| 12 | 979 | 979 | Yes | 2.82 |
| 13 | 1510 | 1510 | Yes | 4.63 |
| 14 | 1215 | 1215 | Yes | 3.5 |
| 15 | 2129 | 2129 | Yes | 2.71 |
| 16 | 1736 | 1736 | Yes | 2.93 |
| 17 | 1121 | 1121 | Yes | 3.1 |
| 18 | 1168 | 1168 | Yes | 2.86 |
| 19 | 2299 | 2299 | Yes | 3.13 |
| 20 | 1878 | 1878 | Yes | 2.9 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 54 | 54 | Yes | 12.44 |
| 2 | 46 | 46 | Yes | 12.06 |
| 3 | 43 | 43 | Yes | 9.96 |
| 4 | 67 | 67 | Yes | 9.16 |
| 5 | 54 | 54 | Yes | 15.97 |
| 6 | 44 | 44 | Yes | 16.64 |
| 7 | 54 | 54 | Yes | 15.95 |
| 8 | 63 | 63 | Yes | 11.5 |
| 9 | 39 | 39 | Yes | 21.17 |
| 10 | 66 | 66 | Yes | 15.92 |
| 11 | 61 | 61 | Yes | 12.28 |
| 12 | 73 | 73 | Yes | 11.66 |
| 13 | 65 | 65 | Yes | 12.78 |
| 14 | 56 | 56 | Yes | 23.17 |
| 15 | 51 | 51 | Yes | 19.15 |
| 16 | 63 | 63 | Yes | 14.71 |
| 17 | 56 | 56 | Yes | 15.61 |
| 18 | 73 | 73 | Yes | 11.65 |
| 19 | 57 | 57 | Yes | 12.85 |
| 20 | 57 | 57 | Yes | 12.87 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MHNJUOS | MHNJUOS | Yes | 4.61 |
| 2 | PFVJCAU | PFVJCAU | Yes | 4.66 |
| 3 | ANGQBUK | ANGQBUK | Yes | 2.12 |
| 4 | EUWJTIB | EUWJTIB | Yes | 1.94 |
| 5 | DLJSFQN | DLJSFQN | Yes | 4.52 |
| 6 | DIXECKZ | DIXECKZ | Yes | 4.23 |
| 7 | XUCHFTZ | XUCHFTZ | Yes | 4.27 |
| 8 | YEXSNFH | YEXSNFH | Yes | 4.0 |
| 9 | EGWDYBK | EGWDYBK | Yes | 2.26 |
| 10 | JVAPKOZ | JVAPKOZ | Yes | 5.04 |
| 11 | ZPVWTFL | ZPVWTF L | No | 4.37 |
| 12 | IVMFZPL | IVMFZPL | Yes | 3.93 |
| 13 | DAKSOYN | DAKSOYN | Yes | 4.4 |
| 14 | VPJITAG | VPJITAG | Yes | 4.43 |
| 15 | PABDIJW | PABD IJW | No | 3.99 |
| 16 | WVLBGZI | WVLBGZI | Yes | 4.11 |
| 17 | IFMKVOC | IFMKVOC | Yes | 4.46 |
| 18 | SKUFJAR | SKUFJAR | Yes | 4.25 |
| 19 | FTERNZA | FTERNZA | Yes | 4.79 |
| 20 | MTUJRPN | MTUJRPN | Yes | 4.68 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.4, 8.6] | 8.6 1.4 | Yes | 5.14 |
| 2 | [4.1, 5.9] | 5.9 4.1 | Yes | 5.49 |
| 3 | [1.2, 8.8] | 1.2 8.8 | Yes | 5.76 |
| 4 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.45 |
| 5 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.44 |
| 6 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.46 |
| 7 | [3.2, 6.8] | 3.2 6.8 | Yes | 6.44 |
| 8 | [4.6, 5.4] | 4.6 5.4 | Yes | 5.81 |
| 9 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.48 |
| 10 | [4.6, 5.4] | 5.4 4.6 | Yes | 5.54 |
| 11 | [0.6, 9.4] | 0.6 9.4 | Yes | 8.12 |
| 12 | [0.6, 9.4] | 9.4 0.6 | Yes | 7.28 |
| 13 | [4.9, 5.1] | 5.1 4.9 | Yes | 4.88 |
| 14 | [5.0, 5.0] | 5.0 5.0 | Yes | 4.53 |
| 15 | [2.9, 7.1] | 7.1 2.9 | Yes | 6.33 |
| 16 | [2.0, 8.0] | 8.0 2.0 | Yes | 5.17 |
| 17 | [0.5, 9.5] | 9.5 0.5 | Yes | 7.31 |
| 18 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.72 |
| 19 | [2.8, 7.2] | 2.8 7.2 | Yes | 5.12 |
| 20 | [3.2, 6.8] | 6.8 3.2 | Yes | 9.0 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | I5W70KVK32RJ | I5W70KVK32RJ | Yes | 3.59 |
| 2 | BAMSIK41PW23 | BAMSIK41PW23 | Yes | 4.19 |
| 3 | 0VJFKKLW0GOW | 0VJFKKLW0GOW | Yes | 9.7 |
| 4 | W7KZXGAGSHTB | W7KZXGAGSHTB | Yes | 3.66 |
| 5 | 9CDAXO57UVC0 | 9CDAXO57UVC0 | Yes | 3.08 |
| 6 | 6EYNUUYDFFW2 | 6EYNUUYDFFW2 | Yes | 5.47 |
| 7 | BW66NA9W4MBO | BW66NA9W4MBO | Yes | 1.01 |
| 8 | M6YHOI9VR1NX | M6YHOI9VR1NX | Yes | 1.85 |
| 9 | AXCZNE5AO45E | AXCZNE5AO45E | Yes | 3.53 |
| 10 | S11K42JVOUZ6 | S11K42JVOUZ6 | Yes | 8.84 |
| 11 | 4MZWT2XJKULZ | 4MZWT2XJKULZ | Yes | 6.29 |
| 12 | FJ0Y17MQI8XS | FJ0Y17MQI8XS | Yes | 10.23 |
| 13 | HTSMM6ENEGHP | HTSMM6ENEGHP | Yes | 3.73 |
| 14 | 79JKQLF7NTEU | 79JKQLF7NTEU | Yes | 5.99 |
| 15 | DNZCIMXNATKI | DNZCIMXNATKI | Yes | 0.74 |
| 16 | Y6IR4VARRCQL | Y6IR4VARRCQL | Yes | 7.82 |
| 17 | 6GNT7AOCZBCW | 6GNT7AOCZBCW | Yes | 1.62 |
| 18 | FJ6PZFSGTY7Q | FJ6PZFSGTY7Q | Yes | 1.28 |
| 19 | 2X3BRKUDNUSR | 2X3BRKUDNUSR | Yes | 5.54 |
| 20 | P4XH42CT7O68 | P4XH42CT7O68 | Yes | 4.96 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 9.74 |
| 2 | 5 | 5 | Yes | 4.62 |
| 3 | 4096 |  | No | 40.15 |
| 4 | 16 | 16 | Yes | 9.99 |
| 5 | 60 | 60 | Yes | 6.71 |
| 6 | 31 | 31 | Yes | 2.26 |
| 7 | 1 | 1 | Yes | 11.71 |
| 8 | 793 | 793 | Yes | 5.07 |
| 9 | 20 |  | No | 43.86 |
| 10 | 9 | 9 | Yes | 16.45 |
| 11 | 67 | 67 | Yes | 3.21 |
| 12 | 3 |  | No | 39.14 |
| 13 | 10 | 8 | No | 12.59 |
| 14 | 198 |  | No | 39.9 |
| 15 | 23 | 23 | Yes | 13.12 |
| 16 | 73 | 73 | Yes | 4.69 |
| 17 | 5 | 42 | No | 12.07 |
| 18 | 65 | 65 | Yes | 5.21 |
| 19 | 63 | 63 | Yes | 6.0 |
| 20 | 7680 | 7680 | Yes | 7.29 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )/))<(<(\ |  | No | 17.69 |
| 2 | /) /<)(   | /\) <(_</) /<)( | No | 21.24 |
| 3 | __ _(<\(( | /\) <(_<)__ _(<\(( | No | 10.95 |
| 4 |   ((_)/_( | ((_)/_( | No | 12.47 |
| 5 | )</\ )(\_ |  | No | 20.66 |
| 6 | /)\\(/ /) | /\) <(_< | No | 11.16 |
| 7 | (<\)__/_  | /\) <(_<) | No | 15.26 |
| 8 | ) /_\)/)_ |  | No | 18.62 |
| 9 | \ <( ((_) | /\) <(_<)\ <( ((_) | No | 18.62 |
| 10 |  ((_)<)(/ | ((_)<)(/ | No | 20.15 |
| 11 | _/\//_/(\ | _/\//_/(\ | Yes | 9.57 |
| 12 | /_/\_ <   | /\) <(_< | No | 12.99 |
| 13 | _ /)</) / | /\) <(_<)_ /)</) / | No | 18.24 |
| 14 | (_//(_/_  |  | No | 43.36 |
| 15 | <)/</ /_< | <)/</ /_< | Yes | 10.2 |
| 16 | /_<\/\)/  | /\) <(_< | No | 7.63 |
| 17 | _)((/) \_ | _)((/ \_ | No | 9.77 |
| 18 | <)/_  )// | /\) <(_<) | No | 12.12 |
| 19 | _  /_\ </ | /\) <(_<) | No | 11.14 |
| 20 | <<<(/_/)_ |  | No | 31.58 |
