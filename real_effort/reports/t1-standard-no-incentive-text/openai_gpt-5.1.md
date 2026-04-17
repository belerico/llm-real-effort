# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-27 10:27:58

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
| sudoku_game | 4970 | 40764 | 45734 | 1 | 19 | 52.74 | 1054.9 |
| add_numbers | 2720 | 1045 | 3765 | 20 | 0 | 4.13 | 82.52 |
| counting_zeros | 4120 | 31502 | 35622 | 19 | 1 | 25.92 | 518.42 |
| task_decoding | 4060 | 4340 | 8400 | 20 | 0 | 5.61 | 112.16 |
| task_summation | 4400 | 7482 | 11882 | 20 | 0 | 7.79 | 155.89 |
| task_transcription | 2854 | 1004 | 3858 | 20 | 0 | 2.60 | 51.96 |
| task_sequences | 2721 | 9408 | 12129 | 17 | 3 | 14.53 | 290.54 |
| string_entry | 3158 | 21343 | 24501 | 7 | 13 | 23.77 | 475.4 |
| **TOTAL** | **29003** | **116888** | **145891** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 1 4 4 6 3 5 1 3 6 4 2 1 6 |  | No | 48.73 |
| 2 | 4 3 5 1 6 3 1 6 4 2 6 2 4 6 |  | No | 73.12 |
| 3 | 4 3 2 2 4 5 3 2 3 2 1 6 5 3 |  | No | 53.96 |
| 4 | 3 6 1 2 5 2 3 4 4 6 1 5 3 3 |  | No | 45.46 |
| 5 | 2 4 6 3 1 5 5 4 4 5 1 1 6 3 |  | No | 55.62 |
| 6 | 2 1 4 5 6 3 6 2 6 4 5 1 6 4 |  | No | 48.73 |
| 7 | 2 3 4 6 5 4 3 2 2 5 3 2 6 6 |  | No | 56.3 |
| 8 | 1 6 4 6 4 2 3 5 1 2 1 4 5 6 |  | No | 55.1 |
| 9 | 4 2 3 6 4 2 5 2 4 3 6 2 2 5 | 4 2 3 6 4 2 5 2 4 3 6 2 2 5 | Yes | 27.29 |
| 10 | 3 6 1 6 1 6 5 2 2 1 5 3 1 5 |  | No | 54.41 |
| 11 | 2 3 6 4 2 5 3 6 4 3 5 1 6 3 |  | No | 48.48 |
| 12 | 6 1 1 6 4 3 5 2 6 2 1 3 2 3 |  | No | 48.24 |
| 13 | 5 2 1 4 1 6 3 3 6 1 2 6 4 5 |  | No | 43.04 |
| 14 | 3 1 2 1 6 4 6 5 6 4 3 5 1 4 |  | No | 54.15 |
| 15 | 4 5 2 4 2 6 5 4 6 4 2 3 2 6 |  | No | 36.25 |
| 16 | 4 2 2 4 3 1 3 4 6 5 2 4 6 2 |  | No | 69.22 |
| 17 | 3 1 6 5 6 2 4 4 3 4 3 6 6 3 |  | No | 57.18 |
| 18 | 5 4 2 1 4 1 3 2 4 3 4 2 4 5 |  | No | 88.29 |
| 19 | 3 5 4 1 2 6 4 3 4 2 5 1 3 4 |  | No | 56.2 |
| 20 | 5 2 1 1 5 6 1 2 5 4 1 3 1 6 |  | No | 35.1 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1582 | 1582 | Yes | 3.21 |
| 2 | 1385 | 1385 | Yes | 3.32 |
| 3 | 1869 | 1869 | Yes | 4.07 |
| 4 | 2208 | 2208 | Yes | 3.21 |
| 5 | 2204 | 2204 | Yes | 3.13 |
| 6 | 1930 | 1930 | Yes | 2.74 |
| 7 | 2000 | 2000 | Yes | 3.84 |
| 8 | 1640 | 1640 | Yes | 2.55 |
| 9 | 1904 | 1904 | Yes | 5.63 |
| 10 | 2108 | 2108 | Yes | 2.97 |
| 11 | 1311 | 1311 | Yes | 3.99 |
| 12 | 1863 | 1863 | Yes | 3.57 |
| 13 | 1918 | 1918 | Yes | 5.25 |
| 14 | 1671 | 1671 | Yes | 6.27 |
| 15 | 1928 | 1928 | Yes | 5.75 |
| 16 | 2505 | 2505 | Yes | 3.56 |
| 17 | 1691 | 1691 | Yes | 4.65 |
| 18 | 1483 | 1483 | Yes | 4.61 |
| 19 | 1625 | 1625 | Yes | 6.76 |
| 20 | 2359 | 2359 | Yes | 3.45 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 42 | 42 | Yes | 19.08 |
| 2 | 62 | 62 | Yes | 24.74 |
| 3 | 45 | 45 | Yes | 26.75 |
| 4 | 57 | 57 | Yes | 28.64 |
| 5 | 45 | 45 | Yes | 24.62 |
| 6 | 63 | 63 | Yes | 27.21 |
| 7 | 58 | 58 | Yes | 25.86 |
| 8 | 65 |  | No | 68.3 |
| 9 | 45 | 45 | Yes | 28.61 |
| 10 | 62 | 62 | Yes | 31.48 |
| 11 | 58 | 58 | Yes | 17.4 |
| 12 | 45 | 45 | Yes | 27.02 |
| 13 | 74 | 74 | Yes | 27.94 |
| 14 | 68 | 68 | Yes | 22.46 |
| 15 | 61 | 61 | Yes | 16.1 |
| 16 | 57 | 57 | Yes | 20.47 |
| 17 | 48 | 48 | Yes | 15.09 |
| 18 | 69 | 69 | Yes | 25.41 |
| 19 | 54 | 54 | Yes | 16.35 |
| 20 | 47 | 47 | Yes | 24.89 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WHKOFSQ | WHKOFSQ | Yes | 4.31 |
| 2 | GAXPRWN | GAXPRWN | Yes | 5.03 |
| 3 | IPWCELH | IPWCELH | Yes | 3.7 |
| 4 | SEWZRHJ | SEWZRHJ | Yes | 3.59 |
| 5 | GBAQYWU | GBAQYWU | Yes | 7.47 |
| 6 | YTISFQZ | YTISFQZ | Yes | 5.2 |
| 7 | BJDVQYA | BJDVQYA | Yes | 3.12 |
| 8 | QPUDSLE | QPUDSLE | Yes | 5.48 |
| 9 | PCKYVMN | PCKYVMN | Yes | 5.23 |
| 10 | CRHVINL | CRHVINL | Yes | 11.16 |
| 11 | NELPRXA | NELPRXA | Yes | 4.03 |
| 12 | KGRWFMA | KGRWFMA | Yes | 4.72 |
| 13 | OIZSKDN | OIZSKDN | Yes | 8.3 |
| 14 | NGWLBKI | NGWLBKI | Yes | 2.37 |
| 15 | RPIUEDX | RPIUEDX | Yes | 5.4 |
| 16 | JTUBVZO | JTUBVZO | Yes | 6.17 |
| 17 | YPMNGSK | YPMNGSK | Yes | 9.25 |
| 18 | ROIFXJM | ROIFXJM | Yes | 7.48 |
| 19 | SNQBWEJ | SNQBWEJ | Yes | 4.87 |
| 20 | HADFMKE | HADFMKE | Yes | 5.27 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 6.7 3.3 | Yes | 12.96 |
| 2 | [4.0, 6.0] | 4.0 6.0 | Yes | 9.39 |
| 3 | [0.6, 9.4] | 0.6 9.4 | Yes | 7.58 |
| 4 | [0.9, 9.1] | 0.9 9.1 | Yes | 6.62 |
| 5 | [0.8, 9.2] | 0.8 9.2 | Yes | 5.98 |
| 6 | [4.4, 5.6] | 4.4 5.6 | Yes | 9.48 |
| 7 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.46 |
| 8 | [3.3, 6.7] | 3.3 6.7 | Yes | 4.66 |
| 9 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.87 |
| 10 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.07 |
| 11 | [2.7, 7.3] | 2.7 7.3 | Yes | 5.94 |
| 12 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.85 |
| 13 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.82 |
| 14 | [0.6, 9.4] | 9.4 0.6 | Yes | 5.92 |
| 15 | [3.0, 7.0] | 3.0 7.0 | Yes | 6.99 |
| 16 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.38 |
| 17 | [4.1, 5.9] | 4.1 5.9 | Yes | 4.74 |
| 18 | [3.1, 6.9] | 6.9 3.1 | Yes | 7.09 |
| 19 | [3.1, 6.9] | 3.1 6.9 | Yes | 7.04 |
| 20 | [4.7, 5.3] | 4.7 5.3 | Yes | 10.05 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1JGCGL735ILY | 1JGCGL735ILY | Yes | 1.53 |
| 2 | TEDOOK78W00C | TEDOOK78W00C | Yes | 1.63 |
| 3 | 0LGYZ8OA4IC7 | 0LGYZ8OA4IC7 | Yes | 4.59 |
| 4 | HJISA4O8LN69 | HJISA4O8LN69 | Yes | 2.89 |
| 5 | B90BOLPS9PYY | B90BOLPS9PYY | Yes | 3.38 |
| 6 | RSWNWR0WJAOB | RSWNWR0WJAOB | Yes | 3.17 |
| 7 | P30BQODFGL25 | P30BQODFGL25 | Yes | 1.69 |
| 8 | 6KY6Y79SZKXE | 6KY6Y79SZKXE | Yes | 1.14 |
| 9 | PSTHU8MT4CKO | PSTHU8MT4CKO | Yes | 3.49 |
| 10 | UXQJRCMQN35T | UXQJRCMQN35T | Yes | 2.75 |
| 11 | MT6ZI34MJU2C | MT6ZI34MJU2C | Yes | 2.05 |
| 12 | 30TBCLXK5S17 | 30TBCLXK5S17 | Yes | 1.43 |
| 13 | BXE9OWV35VP2 | BXE9OWV35VP2 | Yes | 1.67 |
| 14 | 6P5N0VVEAK56 | 6P5N0VVEAK56 | Yes | 1.57 |
| 15 | H46FC5SC7PX8 | H46FC5SC7PX8 | Yes | 1.98 |
| 16 | SQ2YDPQJ8VUV | SQ2YDPQJ8VUV | Yes | 4.85 |
| 17 | ARB7K1P4F8XZ | ARB7K1P4F8XZ | Yes | 3.35 |
| 18 | RSVI1V1PJ8DY | RSVI1V1PJ8DY | Yes | 3.36 |
| 19 | DUNTOUJXPMLK | DUNTOUJXPMLK | Yes | 1.66 |
| 20 | JWOELSIXNMH7 | JWOELSIXNMH7 | Yes | 3.76 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 5.87 |
| 2 | 1 | 1 | Yes | 7.3 |
| 3 | 16 | 16 | Yes | 5.22 |
| 4 | 6 | 6 | Yes | 4.89 |
| 5 | 26 | 26 | Yes | 8.76 |
| 6 | 7680 | 7680 | Yes | 4.41 |
| 7 | 20 |  | No | 56.47 |
| 8 | 65 | 65 | Yes | 3.57 |
| 9 | 4096 |  | No | 61.0 |
| 10 | 64 | 64 | Yes | 11.82 |
| 11 | 67 | 67 | Yes | 3.01 |
| 12 | 4 | 4 | Yes | 3.94 |
| 13 | 39 | 39 | Yes | 6.01 |
| 14 | 36 | 36 | Yes | 5.34 |
| 15 | 73 | 73 | Yes | 6.38 |
| 16 | 9 | 9 | Yes | 4.86 |
| 17 | 198 | 198 | Yes | 6.66 |
| 18 | 44 | 44 | Yes | 11.34 |
| 19 | 23 | 23 | Yes | 5.73 |
| 20 | 10 |  | No | 67.97 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ) )_  \_  | ) )_  \_ | No | 9.02 |
| 2 | __(\ /)<  | __( /)< | No | 19.97 |
| 3 | \() <(<\/ | \() <(<\/ | Yes | 10.57 |
| 4 | _/<_/\(/\ | /\) <(_<) | No | 26.98 |
| 5 | )((_\_/_< | )((_\_/_< | Yes | 34.55 |
| 6 | <<<(\/\(\ |  | No | 63.31 |
| 7 | \/)/\<<<\ |  | No | 81.71 |
| 8 | \<))/ ((_ | \<))/ ((_ | Yes | 8.87 |
| 9 | /___ /)\  | /___ /)\ | No | 7.53 |
| 10 |  (/))_(<\ | (/))_(<\ | No | 16.18 |
| 11 |  \_( ()_( | \_( ()_( | No | 40.29 |
| 12 | \)<<)< \  | \)<<)< \ | No | 16.14 |
| 13 | )) _<(_)/ | )) _<(_)/ | Yes | 5.56 |
| 14 | _))</)))) | /\) <(_<) _ | No | 34.25 |
| 15 |  <(\<<()\ | <(\<<()\ | No | 14.02 |
| 16 | / (\_\\// | / (\_\\// | Yes | 30.03 |
| 17 | ((/< _/<< | ((/< _/<< | Yes | 4.61 |
| 18 | )\_/\\\_  | )\_/\\\_ | No | 15.85 |
| 19 |  )( /\ <\ | )( /\ \< | No | 21.34 |
| 20 | _\/\(_/ _ | _\/\(_/ _ | Yes | 14.63 |
