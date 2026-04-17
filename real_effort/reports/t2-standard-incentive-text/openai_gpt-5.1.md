# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-27 10:25:38

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
| sudoku_game | 5134 | 39951 | 45085 | 1 | 19 | 50.85 | 1017.03 |
| add_numbers | 2900 | 914 | 3814 | 20 | 0 | 3.47 | 69.47 |
| counting_zeros | 4300 | 32317 | 36617 | 17 | 3 | 28.30 | 566.07 |
| task_decoding | 4240 | 3927 | 8167 | 20 | 0 | 5.55 | 111.0 |
| task_summation | 4580 | 8249 | 12829 | 20 | 0 | 7.83 | 156.54 |
| task_transcription | 3045 | 1085 | 4130 | 20 | 0 | 2.53 | 50.53 |
| task_sequences | 2901 | 7954 | 10855 | 19 | 1 | 10.79 | 215.84 |
| string_entry | 3337 | 13991 | 17328 | 12 | 8 | 20.02 | 400.39 |
| **TOTAL** | **30437** | **108388** | **138825** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 4 2 1 2 6 1 4 4 6 3 3 2 5 |  | No | 54.43 |
| 2 | 3 5 2 4 3 4 6 1 1 3 5 6 4 1 |  | No | 59.54 |
| 3 | 5 6 6 3 6 4 5 3 1 6 2 3 4 1 |  | No | 52.71 |
| 4 | 5 4 6 3 5 1 6 1 6 3 6 4 2 1 |  | No | 46.26 |
| 5 | 3 5 6 3 3 6 1 3 4 6 3 3 6 2 |  | No | 50.3 |
| 6 | 5 3 6 4 2 5 4 6 5 3 4 2 4 2 |  | No | 52.93 |
| 7 | 2 1 2 1 4 5 3 1 5 4 5 4 6 5 |  | No | 62.52 |
| 8 | 5 1 6 2 3 5 4 2 3 2 5 4 4 6 |  | No | 54.21 |
| 9 | 4 1 3 6 4 3 6 3 6 5 4 3 4 1 |  | No | 36.59 |
| 10 | 4 6 5 1 3 4 5 1 2 4 5 2 6 2 |  | No | 46.1 |
| 11 | 6 1 4 5 3 5 2 6 4 4 3 5 1 3 |  | No | 58.74 |
| 12 | 3 6 1 2 6 6 3 5 1 6 2 1 1 6 |  | No | 72.89 |
| 13 | 1 6 3 1 4 6 4 5 2 4 5 4 3 1 |  | No | 48.5 |
| 14 | 2 6 1 5 6 5 2 2 4 2 6 1 3 5 |  | No | 44.56 |
| 15 | 4 6 3 6 1 2 3 5 5 4 1 3 6 5 |  | No | 62.56 |
| 16 | 3 6 1 3 2 5 1 4 2 6 3 1 2 4 |  | No | 52.17 |
| 17 | 3 2 6 3 1 5 4 2 3 1 4 5 5 6 |  | No | 45.21 |
| 18 | 1 2 5 5 4 3 2 5 4 6 1 2 3 5 | 1 2 5 5 4 3 2 5 4 6 1 2 3 5 | Yes | 15.45 |
| 19 | 4 1 5 6 1 3 6 4 6 2 5 3 4 2 |  | No | 52.7 |
| 20 | 6 4 3 5 4 3 5 2 4 5 4 6 4 5 |  | No | 48.62 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1378 | 1378 | Yes | 4.16 |
| 2 | 1598 | 1598 | Yes | 3.63 |
| 3 | 1909 | 1909 | Yes | 2.64 |
| 4 | 1725 | 1725 | Yes | 2.94 |
| 5 | 1007 | 1007 | Yes | 3.09 |
| 6 | 2078 | 2078 | Yes | 2.86 |
| 7 | 1126 | 1126 | Yes | 3.27 |
| 8 | 1164 | 1164 | Yes | 2.68 |
| 9 | 1903 | 1903 | Yes | 3.0 |
| 10 | 1495 | 1495 | Yes | 4.76 |
| 11 | 1997 | 1997 | Yes | 3.08 |
| 12 | 2042 | 2042 | Yes | 3.27 |
| 13 | 1605 | 1605 | Yes | 4.24 |
| 14 | 1794 | 1794 | Yes | 5.36 |
| 15 | 1501 | 1501 | Yes | 2.56 |
| 16 | 1769 | 1769 | Yes | 3.8 |
| 17 | 1834 | 1834 | Yes | 3.29 |
| 18 | 1055 | 1055 | Yes | 3.95 |
| 19 | 1862 | 1862 | Yes | 3.33 |
| 20 | 1816 | 1816 | Yes | 3.54 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 74 | Yes | 21.46 |
| 2 | 66 | 66 | Yes | 26.24 |
| 3 | 70 | 70 | Yes | 20.3 |
| 4 | 43 | 43 | Yes | 31.53 |
| 5 | 57 |  | No | 61.08 |
| 6 | 52 | 52 | Yes | 30.92 |
| 7 | 68 |  | No | 62.01 |
| 8 | 42 | 42 | Yes | 12.59 |
| 9 | 53 | 53 | Yes | 29.1 |
| 10 | 61 | 61 | Yes | 24.39 |
| 11 | 39 | 39 | Yes | 31.92 |
| 12 | 55 |  | No | 36.21 |
| 13 | 47 | 47 | Yes | 26.75 |
| 14 | 39 | 39 | Yes | 19.92 |
| 15 | 54 | 54 | Yes | 22.71 |
| 16 | 40 | 40 | Yes | 20.24 |
| 17 | 49 | 49 | Yes | 13.93 |
| 18 | 63 | 63 | Yes | 22.55 |
| 19 | 55 | 55 | Yes | 31.43 |
| 20 | 62 | 62 | Yes | 20.78 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GNEJWXK | GNEJWXK | Yes | 2.6 |
| 2 | DLYOTHR | DLYOTHR | Yes | 5.48 |
| 3 | RGHODAS | RGHODAS | Yes | 3.89 |
| 4 | JWKBDLX | JWKBDLX | Yes | 7.56 |
| 5 | CUWZRTD | CUWZRTD | Yes | 7.88 |
| 6 | XSGRMBA | XSGRMBA | Yes | 5.21 |
| 7 | QNTREJS | QNTREJS | Yes | 4.47 |
| 8 | BSKTVYZ | BSKTVYZ | Yes | 4.19 |
| 9 | VRUWJYB | VRUWJYB | Yes | 5.87 |
| 10 | PAVRIKU | PAVRIKU | Yes | 6.49 |
| 11 | GSEJDLO | GSEJDLO | Yes | 5.86 |
| 12 | VYORCGQ | VYORCGQ | Yes | 6.27 |
| 13 | DNXVZHP | DNXVZHP | Yes | 5.78 |
| 14 | TICDEHJ | TICDEHJ | Yes | 5.77 |
| 15 | VWOPINU | VWOPINU | Yes | 6.42 |
| 16 | LCGOESW | LCGOESW | Yes | 6.38 |
| 17 | DYEUSBI | DYEUSBI | Yes | 6.81 |
| 18 | IEUCGQW | IEUCGQW | Yes | 6.42 |
| 19 | IVWXALG | IVWXALG | Yes | 5.34 |
| 20 | RXCQBLW | RXCQBLW | Yes | 2.29 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.9, 8.1] | 1.9 8.1 | Yes | 8.12 |
| 2 | [1.7, 8.3] | 8.3 1.7 | Yes | 6.26 |
| 3 | [0.5, 9.5] | 0.5 9.5 | Yes | 20.8 |
| 4 | [1.7, 8.3] | 1.7 8.3 | Yes | 7.54 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 6.29 |
| 6 | [0.6, 9.4] | 0.6 9.4 | Yes | 9.36 |
| 7 | [4.6, 5.4] | 4.6 5.4 | Yes | 5.91 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 6.3 |
| 9 | [2.7, 7.3] | 2.7 7.3 | Yes | 7.19 |
| 10 | [2.1, 7.9] | 2.1 7.9 | Yes | 6.63 |
| 11 | [1.8, 8.2] | 1.8 8.2 | Yes | 9.3 |
| 12 | [0.4, 9.6] | 0.4 9.6 | Yes | 8.88 |
| 13 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.75 |
| 14 | [1.1, 8.9] | 8.9 1.1 | Yes | 5.78 |
| 15 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.0 |
| 16 | [3.3, 6.7] | 6.7 3.3 | Yes | 5.27 |
| 17 | [1.2, 8.8] | 8.8 1.2 | Yes | 9.08 |
| 18 | [0.7, 9.3] | 0.7 9.3 | Yes | 6.56 |
| 19 | [4.0, 6.0] | 4.0 6.0 | Yes | 5.34 |
| 20 | [4.7, 5.3] | 5.3 4.7 | Yes | 9.15 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | X12GI4I5MHBJ | X12GI4I5MHBJ | Yes | 2.93 |
| 2 | 95RPMXOOSC8D | 95RPMXOOSC8D | Yes | 1.32 |
| 3 | 41BFQYEOF6ET | 41BFQYEOF6ET | Yes | 1.34 |
| 4 | D778MVLYBLJ3 | D778MVLYBLJ3 | Yes | 1.17 |
| 5 | AB0BHIFNKTA4 | AB0BHIFNKTA4 | Yes | 2.77 |
| 6 | P4ZOKQZ4QCTH | P4ZOKQZ4QCTH | Yes | 1.53 |
| 7 | 30EWLPCVU0KJ | 30EWLPCVU0KJ | Yes | 5.51 |
| 8 | 6W0XYP1E8JNB | 6W0XYP1E8JNB | Yes | 3.52 |
| 9 | 7DSLOTM0VY6Y | 7DSLOTM0VY6Y | Yes | 3.96 |
| 10 | V4Z7JNB7XPTU | V4Z7JNB7XPTU | Yes | 3.87 |
| 11 | 4656T4K04VHW | 4656T4K04VHW | Yes | 2.96 |
| 12 | 7XL26WJ0HBQO | 7XL26WJ0HBQO | Yes | 1.49 |
| 13 | JDCGFOC6UHKC | JDCGFOC6UHKC | Yes | 3.43 |
| 14 | XXQKPESI4RJN | XXQKPESI4RJN | Yes | 1.5 |
| 15 | UEE5A5CQURLO | UEE5A5CQURLO | Yes | 1.22 |
| 16 | 9JKBFLEHNLSW | 9JKBFLEHNLSW | Yes | 3.04 |
| 17 | PHMP15WKN42A | PHMP15WKN42A | Yes | 1.93 |
| 18 | B5SKJ604VFFJ | B5SKJ604VFFJ | Yes | 1.22 |
| 19 | M66U8TZYQDP9 | M66U8TZYQDP9 | Yes | 2.64 |
| 20 | RF0ICP4Q1O9C | RF0ICP4Q1O9C | Yes | 3.18 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 | 64 | Yes | 20.08 |
| 2 | 26 | 26 | Yes | 22.68 |
| 3 | 9 | 9 | Yes | 5.01 |
| 4 | 1 | 1 | Yes | 4.68 |
| 5 | 19 | 19 | Yes | 4.69 |
| 6 | 48 | 48 | Yes | 5.48 |
| 7 | 198 | 198 | Yes | 5.94 |
| 8 | 4096 | 4096 | Yes | 8.7 |
| 9 | 44 | 44 | Yes | 7.19 |
| 10 | 243 | 243 | Yes | 3.78 |
| 11 | 7 | 7 | Yes | 3.65 |
| 12 | 67 | 67 | Yes | 4.22 |
| 13 | 793 | 793 | Yes | 5.63 |
| 14 | 5 | 5 | Yes | 6.15 |
| 15 | 60 | 60 | Yes | 4.48 |
| 16 | 7680 | 7680 | Yes | 6.18 |
| 17 | 6 | 6 | Yes | 5.56 |
| 18 | 20 | 20 | Yes | 29.25 |
| 19 | 16 | 16 | Yes | 7.06 |
| 20 | 5 |  | No | 55.42 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  )<//<<\/ | )<//<<\/ | No | 19.98 |
| 2 | )\ \\\(<< | )\ \\\(<< | Yes | 31.14 |
| 3 | _)(/(\)<< | _)(/(\)<< | Yes | 11.62 |
| 4 | (\/_()))_ | (\/_()))_ | Yes | 10.23 |
| 5 |  /_  // < | /_  // < | No | 9.84 |
| 6 | _</)< ( / |  | No | 67.62 |
| 7 | (( ) _)\( | (( ) _)\( | Yes | 17.86 |
| 8 | /\(/\)\)< |  | No | 102.49 |
| 9 | )\ _()(<_ | )\ _()(<_ | Yes | 9.45 |
| 10 | <//_<< \/ | <//_<< \/ | Yes | 10.55 |
| 11 | (/)//<</< | (/)//<</< | Yes | 6.12 |
| 12 | )//<(//<) | )//<(//<) | Yes | 4.59 |
| 13 | </  <  (< | </  <  (< | Yes | 5.02 |
| 14 | /_<)\))<( | /_<)\))<( | Yes | 6.38 |
| 15 | )\ _\/\(/ | ) _\/\(/ | No | 11.49 |
| 16 | (\()_ (\< | (\()_ (\< | Yes | 6.47 |
| 17 | \_ \(\))  | \_ \())) | No | 14.76 |
| 18 |  < ((\_ / | /\) <(_<) | No | 20.36 |
| 19 | /\<(_(/ / | /\<(_/ / | No | 18.2 |
| 20 | /\__)<(// | /\__)<(// | Yes | 16.21 |
