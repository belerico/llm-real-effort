# Benchmark Report — gemini-2.5-flash-lite

- **Model**: `google/gemini-2.5-flash-lite`
- **Date**: 2026-03-26 10:31:20

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
| sudoku_game | 9260 | 31461 | 40721 | 0 | 20 | 7.79 | 155.89 |
| add_numbers | 37694 | 4755 | 42449 | 20 | 0 | 3.59 | 71.81 |
| counting_zeros | 28960 | 31400 | 60360 | 5 | 15 | 6.63 | 132.83 |
| task_decoding | 50040 | 14965 | 65005 | 14 | 6 | 4.55 | 91.22 |
| task_summation | 29240 | 25626 | 54866 | 20 | 0 | 6.14 | 123.04 |
| task_transcription | 28960 | 3778 | 32738 | 14 | 6 | 2.50 | 50.14 |
| task_sequences | 3345 | 11034 | 14379 | 17 | 3 | 3.20 | 63.93 |
| string_entry | 34520 | 26301 | 60821 | 1 | 19 | 7.14 | 142.8 |
| **TOTAL** | **222019** | **149320** | **371339** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 5 1 2 1 3 5 2 1 3 6 3 1 | 1 6 2 3 5 4 3 5 1 2 6 4 6 1 2 5 3 4 2 3 4 1 5 6 5 4 3 6 1 2 | No | 6.86 |
| 2 | 1 1 5 4 6 2 3 5 2 3 5 1 1 2 | 1 2 5 3 4 6 2 5 3 1 4 6 6 1 2 5 3 4 4 3 6 2 1 5 5 4 1 3 6 2 | No | 6.59 |
| 3 | 2 5 2 4 3 6 2 2 1 5 3 4 4 1 | 2 5 4 3 1 6 4 2 3 1 6 5 6 5 2 3 4 1 2 1 4 6 5 3 3 6 1 2 5 4 | No | 11.06 |
| 4 | 6 5 2 3 1 2 6 1 2 2 6 5 1 4 | 6 2 5 1 4 3 1 5 2 4 6 3 6 4 1 2 5 5 2 1 3 6 4 4 3 6 5 1 2 3 5 4 1 2 6 | No | 9.69 |
| 5 | 1 6 4 5 3 5 1 4 1 3 2 5 6 4 | 1 6 4 5 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 6 3 1 5 2 4 | No | 5.46 |
| 6 | 4 5 1 4 2 3 1 6 5 2 3 2 5 1 | 4 5 2 1 3 6 1 2 3 4 5 6 4 5 1 6 2 3 3 4 6 1 5 2 5 3 2 6 4 1 6 1 5 3 2 4 | No | 9.6 |
| 7 | 4 2 3 5 3 2 1 6 6 1 1 3 6 5 | 2 3 6 1 5 1 6 3 2 4 5 6 1 2 3 4 6 5 | No | 8.11 |
| 8 | 5 1 2 2 4 2 6 3 4 2 4 2 1 2 | 2 1 5 2 4 6 4 2 3 6 1 3 4 2 5 2 1 4 1 3 6 5 2 4 | No | 6.44 |
| 9 | 3 1 2 1 4 6 5 2 6 1 3 4 6 5 | 1 3 2 6 5 4 1 2 6 3 5 4 5 4 2 1 3 6 3 1 4 2 5 6 | No | 7.6 |
| 10 | 6 5 1 3 3 3 2 1 4 5 1 5 1 6 | I am unable to solve this Sudoku puzzle as presented. The provided grid contains duplicate numbers within columns, violating the fundamental rules of Sudoku. Specifically, column 4 contains the number 4 twice (in row 2 and row 6), and column 5 contains the number 2 twice (in row 3 and row 6). A valid Sudoku puzzle must have each number from 1 to 6 appear exactly once in each row, column, and 2x3 box. Due to these inconsistencies, the puzzle is unsolvable. | No | 10.56 |
| 11 | 3 6 5 4 2 5 6 1 4 3 4 2 1 5 | 3 5 6 4 2 1 4 2 3 1 5 6 1 3 4 5 6 2 5 4 1 2 3 6 | No | 5.55 |
| 12 | 1 3 3 1 5 1 3 2 4 2 4 5 6 1 | 1 3 4 5 6 2 1 3 5 4 6 2 3 1 5 2 4 6 1 4 3 5 2 6 | No | 9.42 |
| 13 | 5 4 3 2 4 1 3 2 6 1 2 2 5 4 | 5 4 2 3 6 1 4 3 2 5 6 1 2 5 3 4 1 6 6 2 1 5 4 3 | No | 6.02 |
| 14 | 6 1 6 2 4 2 4 2 3 3 4 5 4 1 | 2 4 1 3 6 5 3 4 2 5 1 6 4 2 3 1 5 6 1 5 4 6 2 3 | No | 8.36 |
| 15 | 1 2 6 2 6 4 1 4 5 3 1 6 4 5 | 1 2 6 4 2 4 1 3 5 6 3 1 4 5 | No | 8.1 |
| 16 | 2 1 1 4 2 5 4 2 3 4 6 3 1 5 | 4 2 1 5 3 6 3 1 2 4 5 6 5 4 2 6 1 3 6 3 1 2 4 5 1 5 6 3 2 4 2 6 4 1 5 3 | No | 6.3 |
| 17 | 1 5 1 2 5 3 1 6 2 5 4 1 6 3 | 5 1 4 3 2 6 1 5 3 2 6 4 2 3 1 5 4 6 6 4 5 1 3 2 3 6 2 4 1 5 5 1 4 3 2 6 | No | 9.0 |
| 18 | 1 5 3 1 1 4 5 1 3 2 3 5 1 4 | 1 5 3 4 2 1 3 4 5 3 1 4 5 2 6 | No | 7.56 |
| 19 | 2 3 1 5 2 4 1 1 6 3 1 5 2 5 | 2 3 1 5 6 4 5 1 2 6 3 4 3 4 5 1 2 6 6 2 3 4 1 5 1 5 6 2 3 4 | No | 5.34 |
| 20 | 3 6 6 5 3 2 4 6 1 4 3 2 1 3 | 3 6 1 2 4 5 6 3 5 2 4 1 4 5 3 6 2 1 2 1 6 3 5 4 3 4 2 1 6 5 1 2 4 5 3 6 | No | 8.11 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 841 | 841 | Yes | 2.56 |
| 2 | 1821 | 1821 | Yes | 2.55 |
| 3 | 1692 | 1692 | Yes | 2.61 |
| 4 | 2675 | 2675 | Yes | 3.02 |
| 5 | 1728 | 1728 | Yes | 2.06 |
| 6 | 2482 | 2482 | Yes | 3.15 |
| 7 | 1697 | 1697 | Yes | 13.97 |
| 8 | 1498 | 1498 | Yes | 3.38 |
| 9 | 1299 | 1299 | Yes | 7.88 |
| 10 | 1231 | 1231 | Yes | 3.2 |
| 11 | 962 | 962 | Yes | 3.0 |
| 12 | 1138 | 1138 | Yes | 3.48 |
| 13 | 788 | 788 | Yes | 2.19 |
| 14 | 1444 | 1444 | Yes | 3.73 |
| 15 | 2098 | 2098 | Yes | 2.8 |
| 16 | 1205 | 1205 | Yes | 2.11 |
| 17 | 1986 | 1986 | Yes | 2.11 |
| 18 | 727 | 727 | Yes | 3.18 |
| 19 | 2013 | 2013 | Yes | 2.42 |
| 20 | 1683 | 1683 | Yes | 2.34 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 65 | No | 6.78 |
| 2 | 66 | 65 | No | 4.78 |
| 3 | 74 | 67 | No | 6.85 |
| 4 | 60 | 61 | No | 5.65 |
| 5 | 57 | 56 | No | 7.24 |
| 6 | 66 | 70 | No | 5.33 |
| 7 | 39 | 39 | Yes | 7.52 |
| 8 | 55 | 57 | No | 4.81 |
| 9 | 60 | 55 | No | 6.48 |
| 10 | 51 | 52 | No | 7.58 |
| 11 | 36 | 37 | No | 7.96 |
| 12 | 41 | 41 | Yes | 6.27 |
| 13 | 37 | 37 | Yes | 7.11 |
| 14 | 64 | 67 | No | 7.51 |
| 15 | 45 | 47 | No | 4.53 |
| 16 | 42 | 43 | No | 8.99 |
| 17 | 61 | 61 | Yes | 5.85 |
| 18 | 50 | 50 | Yes | 7.43 |
| 19 | 61 | 62 | No | 5.76 |
| 20 | 63 | 67 | No | 8.11 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GCEFJSO | GCEFJSO | Yes | 2.57 |
| 2 | FGZTVKQ | FGZTVKQ | Yes | 5.75 |
| 3 | VTJPSQI | VTJPSQIR | No | 6.99 |
| 4 | ZRUGCVY | ZRUGVCY | No | 6.91 |
| 5 | ARXTUJE | ARXTUJE | Yes | 5.26 |
| 6 | SAJFEKB | SAJFEKB | Yes | 3.02 |
| 7 | YNDFBCW | YNDFBCW | Yes | 3.06 |
| 8 | UHYOMCD | UHYOMCD | Yes | 2.97 |
| 9 | MPTDOSX | MPTDOX | No | 2.47 |
| 10 | WIFDBEZ | WIFDBEZ | Yes | 2.21 |
| 11 | CUOZINS | CUOZINS | Yes | 2.68 |
| 12 | VRYCQGP | VRYCQGP | Yes | 4.72 |
| 13 | OCZJEPL | OCZJEPL | Yes | 3.1 |
| 14 | ZOHTIAF | ZOHTIAF | Yes | 3.39 |
| 15 | WITMHKE | WITMHKE | Yes | 7.88 |
| 16 | IJQWMKS | IJQWMKS | Yes | 7.7 |
| 17 | VXGRACM | VXGRAMC | No | 2.68 |
| 18 | DCPZSFN | DCPZSFN | Yes | 4.56 |
| 19 | BAGQSMC | BAGQSM C | No | 5.98 |
| 20 | XOJEIDM | XOJ EIDM | No | 7.11 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.5, 8.5] | 8.5 1.5 | Yes | 8.22 |
| 2 | [0.9, 9.1] | 0.9 9.1 | Yes | 6.45 |
| 3 | [4.3, 5.7] | 5.7 4.3 | Yes | 6.07 |
| 4 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.0 |
| 5 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.07 |
| 6 | [4.6, 5.4] | 5.4 4.6 | Yes | 7.54 |
| 7 | [4.0, 6.0] | 4.0 6.0 | Yes | 5.68 |
| 8 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.86 |
| 9 | [4.3, 5.7] | 5.7 4.3 | Yes | 5.05 |
| 10 | [0.2, 9.8] | 0.2 9.8 | Yes | 5.65 |
| 11 | [3.3, 6.7] | 3.3 6.7 | Yes | 8.32 |
| 12 | [2.5, 7.5] | 2.5 7.5 | Yes | 4.94 |
| 13 | [3.8, 6.2] | 3.8 6.2 | Yes | 4.73 |
| 14 | [4.2, 5.8] | 5.8 4.2 | Yes | 6.03 |
| 15 | [2.3, 7.7] | 2.3 7.7 | Yes | 5.85 |
| 16 | [0.6, 9.4] | 9.4 0.6 | Yes | 6.32 |
| 17 | [3.2, 6.8] | 6.8 3.2 | Yes | 5.44 |
| 18 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.31 |
| 19 | [2.4, 7.6] | 2.4 7.6 | Yes | 6.29 |
| 20 | [2.1, 7.9] | 7.9 2.1 | Yes | 7.04 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | U4UBQGD30XTX | U4UBQGD30XTX | Yes | 2.6 |
| 2 | CYVAEZWW2DZ0 | CYVAEZZWW2DZO | No | 2.08 |
| 3 | H59DI77LKLZ6 | H59DI77LKLZ6 | Yes | 2.72 |
| 4 | 3MFRGZZKQF3T | 3MFRGZZKQF3T | Yes | 2.23 |
| 5 | 0LKT40RF9YDL | 0LKT40RF9YDL | Yes | 2.09 |
| 6 | YP06N1PLYGN3 | YP06N1PLYGN3 | Yes | 2.45 |
| 7 | 4UJKT1JJ4O7A | 4UJKT1JJ407A | No | 1.79 |
| 8 | 8AD9RBZYAIDK | 8AD9RBZYAI DK | No | 2.93 |
| 9 | GTRL1NOV29O9 | GTRL1NOV2909 | No | 2.42 |
| 10 | HHRJ119TPYJJ | HHRJ119TPYJJ | Yes | 2.52 |
| 11 | 61Z12MM5WJR4 | 61Z12MM5WJR4 | Yes | 3.01 |
| 12 | 7MA8XSD9B6P2 | 7MA8XSD9B6P2 | Yes | 2.61 |
| 13 | 4HC566NDI8VJ | 4HC566NDI8VJ | Yes | 2.7 |
| 14 | RBXAO50EOGJ6 | RBXA050EOGJ6 | No | 1.96 |
| 15 | 2XRGJE3AAYNL | 2XRGJE3AAYNL | Yes | 2.56 |
| 16 | MI8GUM2WVUYW | MI8GUM2WVUYW | Yes | 2.48 |
| 17 | 2WJ87VTNNC9X | 2WJ87VTNNC9X | Yes | 3.14 |
| 18 | POQ4G2GYZ540 | POO4G2GYZ540 | No | 2.67 |
| 19 | MCXQE8I8EVL4 | MCXQE8I8EVL4 | Yes | 2.87 |
| 20 | OMT8KPV9NG0H | OMT8KPV9NG0H | Yes | 2.21 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 16 | 16 | Yes | 2.47 |
| 2 | 5 | 5 | Yes | 1.93 |
| 3 | 65 | 65 | Yes | 1.89 |
| 4 | 4 | 4 | Yes | 2.0 |
| 5 | 1 | 1 | Yes | 2.3 |
| 6 | 9 | 9 | Yes | 3.42 |
| 7 | 4096 | 16384 | No | 6.72 |
| 8 | 243 | 243 | Yes | 2.03 |
| 9 | 60 | 60 | Yes | 1.92 |
| 10 | 3 | 3 | Yes | 5.6 |
| 11 | 26 | 8 | No | 6.29 |
| 12 | 36 | 36 | Yes | 1.71 |
| 13 | 60 | 60 | Yes | 1.71 |
| 14 | 1440 | 1440 | Yes | 2.54 |
| 15 | 7680 | 7680 | Yes | 2.39 |
| 16 | 63 | 63 | Yes | 1.72 |
| 17 | 48 | 48 | Yes | 3.93 |
| 18 | 64 | 64 | Yes | 2.06 |
| 19 | 5 | 8 | No | 7.64 |
| 20 | 9 | 9 | Yes | 3.67 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /_/)  \_\ | /_/)\ \_\ | No | 5.79 |
| 2 | //))/)()< | //))/)() < | No | 6.38 |
| 3 | _) (/ )(( | _)␣(/␣))( | No | 6.51 |
| 4 | \_\/_<\_) | \ _ \ / _ < \ _ ) | No | 8.56 |
| 5 | /_\)_(/)  | /_\)_(/) | No | 6.7 |
| 6 | \  _<\<_( | /␣␣_< / <_( | No | 7.46 |
| 7 | <\____\__ | <\/\/\/\/_/\__ | No | 7.18 |
| 8 | \_ \) ))) | /_␣\)␣))) | No | 4.26 |
| 9 |   <()/ _  | <()/_ | No | 8.55 |
| 10 | /<(\<\()\ | /<(\<\() | No | 5.97 |
| 11 | / __(\<\< | /\__(\<\< | No | 8.71 |
| 12 | <<\/ )\_/ | <<\ /)\_/ | No | 6.2 |
| 13 | \\<)( )/\ | \ / < ) ( _ ) / \ | No | 6.86 |
| 14 |  /( \(  ( | ␣/(␣\(␣␣( | Yes | 8.48 |
| 15 | () )  ))) | ()_ )__))) | No | 8.51 |
| 16 | ) )_</<<\ | ) ) _ < / < < \ | No | 6.72 |
| 17 |  /< (\(_) | ␣ / < ␣ ( \ ( _ ) | No | 6.66 |
| 18 | _(_//_/<_ | _(_//_/<>_ | No | 7.8 |
| 19 |  \ )_\)_< | \ )_/ )_< | No | 8.82 |
| 20 |  _\/<<)_) | _\/< <)_ | No | 6.61 |
