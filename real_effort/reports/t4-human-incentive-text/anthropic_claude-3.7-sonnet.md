# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-27 10:09:38

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
| sudoku_game | 6699 | 34148 | 40847 | 2 | 18 | 23.08 | 461.66 |
| add_numbers | 4080 | 7914 | 11994 | 20 | 0 | 6.42 | 128.33 |
| counting_zeros | 5400 | 23304 | 28704 | 0 | 20 | 13.67 | 273.39 |
| task_decoding | 5400 | 5463 | 10863 | 18 | 2 | 4.26 | 85.21 |
| task_summation | 5460 | 22868 | 28328 | 20 | 0 | 13.73 | 274.6 |
| task_transcription | 4226 | 3227 | 7453 | 20 | 0 | 3.16 | 63.15 |
| task_sequences | 4140 | 14254 | 18394 | 18 | 2 | 10.26 | 205.22 |
| string_entry | 4611 | 6431 | 11042 | 14 | 6 | 5.61 | 112.16 |
| **TOTAL** | **40016** | **117609** | **157625** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 1 3 5 2 4 3 3 5 4 6 5 2 | 5 6 1 3 5 3 2 3 5 3 4 6 2 5 | No | 23.94 |
| 2 | 4 6 3 2 1 2 4 2 1 2 4 5 6 2 | 2 4 6 3 1 2 4 2 1 2 4 6 5 2 | No | 22.32 |
| 3 | 4 5 6 2 2 3 1 4 6 1 2 5 6 4 | 4 6 5 2 2 3 1 4 6 1 5 6 4 2 | No | 21.7 |
| 4 | 2 3 4 5 4 2 1 4 2 3 5 2 1 5 | 3 4 2 5 5 6 4 2 1 3 4 2 5 2 1 5 | No | 23.96 |
| 5 | 2 1 5 2 6 2 1 5 2 3 6 5 2 1 | 2 1 5 2 6 2 1 5 2 3 6 5 2 1 | Yes | 25.1 |
| 6 | 1 4 3 2 6 2 3 3 1 6 6 4 2 2 | 1 4 3 2 6 2 3 1 6 6 4 2 | No | 20.77 |
| 7 | 1 6 5 2 1 4 2 1 5 4 3 1 5 2 | 1 6 5 1 2 4 1 5 4 1 5 2 3 | No | 23.13 |
| 8 | 2 3 5 3 4 2 5 1 2 5 1 3 2 1 | 2 3 5 3 4 5 2 2 1 5 1 3 2 1 | No | 20.34 |
| 9 | 4 3 2 3 5 2 4 1 2 3 6 5 2 4 | I'll solve this 6×6 Sudoku puzzle step by step.  First, let me analyze the given puzzle: ``` . 6 . \| 5 1 . 2 1 4 \| 6 5 . -----+----- 3 . 1 \| . . 6 . 4 . \| . . . -----+----- 5 . 6 \| 1 3 . 6 3 5 \| 4 2 1 ```  Working through the constraints:  Row 1: Missing 2, 3, 4 - Column 1 already has 2, 3, 5, 6 → Cell(1,1) must be 4 - Column 3 has 1, 4, 5, 6 → Cell(1,3) must be 3 - Column 6 missing 2, 3, 4, 6 → After other constraints, Cell(1,6) must be 2  Row 2: Missing 3 - Only Cell(2,6) is empty → must be 3  Row 3: Missing 2, 4, 5 - Column 2 already has 1, 3, 4, 6 → Cell(3,2) must be 5 - Column 4 has constraints → Cell(3,4) must be 2 - Column 5 has constraints → Cell(3,5) must be 4  Row 4: All cells empty except Cell(4,2)=4 - Column 1 has | No | 27.15 |
| 10 | 6 4 3 2 3 6 1 1 6 2 1 2 3 5 | I'll solve this 6×6 Sudoku puzzle by examining each row, column, and 2×3 box.  First, let me analyze the given puzzle: ``` 1 . . \| 2 . 5 4 5 3 \| 1 6 . -----+----- . 2 5 \| . . 4 5 . . \| 4 2 3 -----+----- . 3 . \| 5 4 6 6 4 . \| . . 1 ```  Working through the empty cells:  - Row 1, Column 2: This can only be 6 (checking row, column, and box constraints) - Row 1, Column 3: Only 3 fits here - Row 1, Column 5: Must be 4 (only remaining number for this row) - Row 2, Column 6: Must be 2 (only missing number in this row)  - Row 3, Column 1: Must be 6 - Row 3, Column 4: Only 3 works here - Row 3, Column 5: Must be 1  - Row 4, Column 2: Must be 6 - Row 4, Column 3: Must be 1  - Row 5, Column 1: Must be 2 - Row 5 | No | 25.6 |
| 11 | 4 1 4 3 6 2 5 3 4 1 2 1 6 3 | 4 1 4 6 3 2 3 4 1 2 5 1 6 3 | No | 21.39 |
| 12 | 2 3 1 5 5 6 4 6 5 5 4 1 3 6 | 3 2 1 5 5 4 5 4 3 1 3 6 | No | 23.54 |
| 13 | 2 1 5 2 2 4 6 4 5 3 5 4 2 1 | 2 1 5 2 2 4 6 5 3 4 4 5 | No | 24.33 |
| 14 | 3 5 6 4 2 1 6 3 5 4 3 1 2 5 | 3 5 6 4 2 1 6 3 5 4 5 1 2 3 | No | 21.02 |
| 15 | 5 1 4 2 2 3 5 6 3 1 2 1 4 3 | 5 1 4 2 3 1 5 2 6 3 1 2 1 4 3 | No | 21.47 |
| 16 | 3 2 5 4 5 6 2 5 3 4 6 4 3 5 | 3 5 2 4 5 5 6 2 3 4 6 4 3 6 | No | 22.9 |
| 17 | 3 1 3 5 3 6 4 1 1 2 5 4 2 1 | 3 1 3 6 1 4 3 6 1 2 5 1 2 1 | No | 27.02 |
| 18 | 4 5 2 4 5 2 3 4 4 6 1 4 3 6 | 5 2 4 4 5 2 3 4 6 4 1 3 4 6 | No | 23.15 |
| 19 | 6 4 1 1 5 5 2 1 3 2 6 4 2 1 | 6 4 1 1 5 5 2 1 3 2 6 4 2 1 | Yes | 19.42 |
| 20 | 1 4 2 6 2 5 4 3 4 2 1 2 4 3 | 1 4 2 6 2 5 4 3 2 1 4 4 2 3 | No | 23.39 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1150 | 1150 | Yes | 5.85 |
| 2 | 1320 | 1320 | Yes | 6.77 |
| 3 | 1328 | 1328 | Yes | 9.39 |
| 4 | 2146 | 2146 | Yes | 7.9 |
| 5 | 2165 | 2165 | Yes | 6.71 |
| 6 | 1497 | 1497 | Yes | 6.22 |
| 7 | 773 | 773 | Yes | 7.61 |
| 8 | 1723 | 1723 | Yes | 6.3 |
| 9 | 1796 | 1796 | Yes | 7.62 |
| 10 | 1656 | 1656 | Yes | 4.99 |
| 11 | 1602 | 1602 | Yes | 5.7 |
| 12 | 1601 | 1601 | Yes | 8.52 |
| 13 | 1207 | 1207 | Yes | 4.26 |
| 14 | 1458 | 1458 | Yes | 4.98 |
| 15 | 646 | 646 | Yes | 5.68 |
| 16 | 986 | 986 | Yes | 4.83 |
| 17 | 1924 | 1924 | Yes | 5.92 |
| 18 | 1396 | 1396 | Yes | 6.59 |
| 19 | 1625 | 1625 | Yes | 6.54 |
| 20 | 1610 | 1610 | Yes | 5.94 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 47 | 40 | No | 12.85 |
| 2 | 70 | 55 | No | 13.41 |
| 3 | 64 | 59 | No | 18.38 |
| 4 | 58 | 52 | No | 19.09 |
| 5 | 68 | 60 | No | 12.86 |
| 6 | 52 | 53 | No | 18.87 |
| 7 | 56 | 47 | No | 11.67 |
| 8 | 39 | 31 | No | 12.86 |
| 9 | 58 | 53 | No | 11.46 |
| 10 | 67 | 62 | No | 14.5 |
| 11 | 39 | 35 | No | 16.56 |
| 12 | 36 | 34 | No | 11.86 |
| 13 | 64 | 55 | No | 12.45 |
| 14 | 55 | 51 | No | 16.04 |
| 15 | 65 | 56 | No | 15.58 |
| 16 | 70 | 67 | No | 8.49 |
| 17 | 55 | 51 | No | 14.91 |
| 18 | 72 | 65 | No | 11.46 |
| 19 | 54 | 50 | No | 10.84 |
| 20 | 56 | 55 | No | 9.25 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GFNIWUV | GFNIWUV | Yes | 4.37 |
| 2 | AWMNPHU | AWMNPHU | Yes | 5.51 |
| 3 | FRNVKMJ | FRNVKMJ | Yes | 4.72 |
| 4 | CLWYTVI | CLWTVI | No | 3.74 |
| 5 | KONRXLU | KONRXLU | Yes | 3.49 |
| 6 | EAUYRLJ | EAUYRLJ | Yes | 4.74 |
| 7 | OGERWQV | OGERWQV | Yes | 5.26 |
| 8 | SKLAYUX | SKLAYUX | Yes | 2.62 |
| 9 | XKRZIJB | XKRZIJB | Yes | 4.24 |
| 10 | IODQLPG | IODQLPG | Yes | 4.15 |
| 11 | YKOSBLX | YKOABLX | No | 4.05 |
| 12 | XEPITCZ | XEPITCZ | Yes | 3.8 |
| 13 | RIOVHKY | RIOVHKY | Yes | 4.88 |
| 14 | MBAHPRS | MBAHPRS | Yes | 4.81 |
| 15 | QPHOMEI | QPHOMEI | Yes | 4.88 |
| 16 | GFEDXNR | GFEDXNR | Yes | 4.76 |
| 17 | AZJNPOC | AZJNPOC | Yes | 3.06 |
| 18 | SVJFOYD | SVJFOYD | Yes | 3.76 |
| 19 | TENZXJW | TENZXJW | Yes | 5.0 |
| 20 | PXMVQUZ | PXMVQUZ | Yes | 3.36 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 0.5 9.5 | Yes | 13.32 |
| 2 | [0.8, 9.2] | 0.8 9.2 | Yes | 12.33 |
| 3 | [3.9, 6.1] | 6.1 3.9 | Yes | 12.04 |
| 4 | [4.0, 6.0] | 6.0 4.0 | Yes | 9.62 |
| 5 | [2.3, 7.7] | 7.7 2.3 | Yes | 17.85 |
| 6 | [4.6, 5.4] | 4.6 5.4 | Yes | 12.42 |
| 7 | [4.9, 5.1] | 4.9 5.1 | Yes | 10.45 |
| 8 | [3.8, 6.2] | 3.8 6.2 | Yes | 20.9 |
| 9 | [1.8, 8.2] | 8.2 1.8 | Yes | 13.75 |
| 10 | [2.5, 7.5] | 2.5 7.5 | Yes | 11.53 |
| 11 | [4.9, 5.1] | 4.9 5.1 | Yes | 19.48 |
| 12 | [3.4, 6.6] | 3.4 6.6 | Yes | 14.07 |
| 13 | [1.8, 8.2] | 1.8 8.2 | Yes | 16.99 |
| 14 | [3.3, 6.7] | 6.7 3.3 | Yes | 11.83 |
| 15 | [1.2, 8.8] | 8.8 1.2 | Yes | 11.12 |
| 16 | [4.2, 5.8] | 4.2 5.8 | Yes | 15.43 |
| 17 | [4.3, 5.7] | 4.3 5.7 | Yes | 10.87 |
| 18 | [0.1, 9.9] | 0.1 9.9 | Yes | 20.7 |
| 19 | [3.7, 6.3] | 3.7 6.3 | Yes | 10.79 |
| 20 | [1.4, 8.6] | 1.4 8.6 | Yes | 9.08 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | L4WR9DSM3HGE | L4WR9DSM3HGE | Yes | 2.25 |
| 2 | 1PB09FJP8UA2 | 1PB09FJP8UA2 | Yes | 3.7 |
| 3 | 2YMGNLIWVMPD | 2YMGNLIWVMPD | Yes | 2.87 |
| 4 | RP85QMJIXL5Z | RP85QMJIXL5Z | Yes | 3.13 |
| 5 | 57W57F47R90U | 57W57F47R90U | Yes | 2.53 |
| 6 | I3EJZCN2IX1R | I3EJZCN2IX1R | Yes | 4.41 |
| 7 | VJEWRT838EGA | VJEWRT838EGA | Yes | 3.19 |
| 8 | 3C03P2FM25TF | 3C03P2FM25TF | Yes | 1.71 |
| 9 | ATS05P19VZFS | ATS05P19VZFS | Yes | 3.23 |
| 10 | BN6GQR7234VZ | BN6GQR7234VZ | Yes | 3.65 |
| 11 | FN4LTJR9GO66 | FN4LTJR9GO66 | Yes | 3.44 |
| 12 | YD4K901V76CH | YD4K901V76CH | Yes | 3.83 |
| 13 | PRZ3J9G2XN6C | PRZ3J9G2XN6C | Yes | 2.57 |
| 14 | 4EHRC3SZGTX1 | 4EHRC3SZGTX1 | Yes | 3.44 |
| 15 | F4ZTTXOVCYYN | F4ZTTXOVCYYN | Yes | 2.15 |
| 16 | F65XV5IMCBM9 | F65XV5IMCBM9 | Yes | 3.25 |
| 17 | ROLJ6NOGX0KO | ROLJ6NOGX0KO | Yes | 3.64 |
| 18 | OXGOC0PR38CO | OXGOC0PR38CO | Yes | 3.38 |
| 19 | WUR5Z4GY59AL | WUR5Z4GY59AL | Yes | 4.17 |
| 20 | NSGJBYLLW9UI | NSGJBYLLW9UI | Yes | 2.59 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 5.88 |
| 2 | 67 | 67 | Yes | 4.33 |
| 3 | 9 | 9 | Yes | 6.04 |
| 4 | 793 | 793 | Yes | 5.42 |
| 5 | 7 | 7 | Yes | 4.44 |
| 6 | 10 | 10 | Yes | 14.39 |
| 7 | 60 | 60 | Yes | 5.12 |
| 8 | 20 | 20 | Yes | 24.69 |
| 9 | 31 | 31 | Yes | 4.88 |
| 10 | 4 | 4 | Yes | 9.66 |
| 11 | 5 | 17 | No | 17.69 |
| 12 | 4 | 4 | Yes | 15.69 |
| 13 | 60 |  | No | 26.31 |
| 14 | 3 | 3 | Yes | 10.26 |
| 15 | 73 | 73 | Yes | 5.95 |
| 16 | 48 | 48 | Yes | 8.36 |
| 17 | 26 | 26 | Yes | 20.05 |
| 18 | 5 | 5 | Yes | 6.89 |
| 19 | 23 | 23 | Yes | 5.48 |
| 20 | 36 | 36 | Yes | 3.71 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _) )/))() | _) )/))() | Yes | 4.65 |
| 2 | )() \(//\ | )() \(//\ | Yes | 4.9 |
| 3 | <)\)\ / \ | <)\) / \ | No | 5.61 |
| 4 | (__)_ /_\ | (__)_ /_\ | Yes | 4.76 |
| 5 | _  /_\\(< | _  /_\( | No | 7.51 |
| 6 | <_// _(_\ | <_// _(_\ | Yes | 5.35 |
| 7 | _ < <__(/ | _ < <__(/ | Yes | 4.55 |
| 8 | )<)_<__\) | )<)_<__\) | Yes | 4.37 |
| 9 | ((<\< (/  | ((<\< (/ | No | 6.07 |
| 10 |  /))\) << | /))\) < | No | 5.76 |
| 11 | (/<//<_<_ | (/<//<_<_ | Yes | 5.89 |
| 12 |  <  \(//\ | <  \(//\ | No | 4.96 |
| 13 | /(\)) ( \ | /(\)) ( \ | Yes | 8.07 |
| 14 | <_\<_< /  | <_\<_< / | No | 6.94 |
| 15 | /)\< )<__ | /)\< )<__ | Yes | 5.63 |
| 16 | ( \(/_)/) | ( \(/_)/) | Yes | 4.69 |
| 17 | /</\_()// | /</\_()// | Yes | 4.71 |
| 18 | _/( \\\() | _/( \\\() | Yes | 7.32 |
| 19 | \/ \(/))) | \/ \(/))) | Yes | 4.89 |
| 20 | /\)<\\ )) | /\)<\\ )) | Yes | 5.52 |
