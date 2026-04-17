# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-27 10:22:56

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
| sudoku_game | 4959 | 40960 | 45919 | 0 | 20 | 39.40 | 788.09 |
| add_numbers | 2720 | 2914 | 5634 | 20 | 0 | 4.17 | 83.33 |
| counting_zeros | 4120 | 40055 | 44175 | 3 | 17 | 29.45 | 588.97 |
| task_decoding | 4060 | 5134 | 9194 | 20 | 0 | 5.30 | 105.94 |
| task_summation | 4400 | 13089 | 17489 | 19 | 1 | 10.38 | 207.68 |
| task_transcription | 2859 | 2211 | 5070 | 20 | 0 | 2.29 | 45.73 |
| task_sequences | 2720 | 14108 | 16828 | 17 | 3 | 14.29 | 285.85 |
| string_entry | 3174 | 20595 | 23769 | 11 | 9 | 16.76 | 335.12 |
| **TOTAL** | **29012** | **139066** | **168078** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 2 2 5 5 1 5 1 4 2 3 5 5 1 |  | No | 47.46 |
| 2 | 2 3 5 1 3 5 2 5 4 4 2 5 1 3 |  | No | 39.47 |
| 3 | 6 5 3 4 3 6 4 1 4 3 1 4 3 3 |  | No | 41.74 |
| 4 | 1 5 5 6 3 4 3 5 6 5 5 1 3 2 |  | No | 39.6 |
| 5 | 2 3 5 5 6 2 1 6 4 6 4 3 5 1 |  | No | 24.47 |
| 6 | 6 5 1 6 5 2 4 6 4 5 2 1 1 6 |  | No | 35.52 |
| 7 | 2 5 4 2 4 2 4 1 2 2 1 3 6 3 |  | No | 46.09 |
| 8 | 2 6 4 1 2 3 5 6 2 4 1 2 6 1 |  | No | 44.14 |
| 9 | 3 5 6 1 1 5 2 4 1 6 3 4 3 1 |  | No | 38.62 |
| 10 | 4 6 3 5 6 5 3 1 2 4 3 6 6 3 |  | No | 42.91 |
| 11 | 1 4 3 3 1 5 2 5 1 1 5 6 3 1 |  | No | 39.37 |
| 12 | 5 6 5 4 4 3 2 2 4 6 5 6 2 4 |  | No | 40.85 |
| 13 | 4 3 2 4 4 2 3 6 5 2 1 3 3 5 |  | No | 38.39 |
| 14 | 2 1 2 5 4 6 1 3 1 5 2 6 2 4 |  | No | 21.05 |
| 15 | 2 1 4 2 3 4 2 2 6 3 4 1 4 2 |  | No | 28.09 |
| 16 | 5 1 6 2 5 6 1 6 2 5 1 5 2 6 |  | No | 40.51 |
| 17 | 5 4 1 1 4 1 2 1 3 6 5 2 5 1 |  | No | 38.2 |
| 18 | 2 1 5 2 6 1 5 6 2 3 3 4 4 6 |  | No | 45.55 |
| 19 | 5 6 1 2 2 1 4 1 4 2 4 5 3 4 |  | No | 60.15 |
| 20 | 3 6 3 2 6 6 1 1 4 6 2 6 5 5 |  | No | 35.86 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1060 | 1060 | Yes | 6.05 |
| 2 | 1620 | 1620 | Yes | 2.5 |
| 3 | 1685 | 1685 | Yes | 2.51 |
| 4 | 2008 | 2008 | Yes | 2.2 |
| 5 | 2054 | 2054 | Yes | 18.02 |
| 6 | 719 | 719 | Yes | 7.28 |
| 7 | 2119 | 2119 | Yes | 2.26 |
| 8 | 2124 | 2124 | Yes | 3.68 |
| 9 | 2484 | 2484 | Yes | 1.99 |
| 10 | 1669 | 1669 | Yes | 4.45 |
| 11 | 1225 | 1225 | Yes | 3.92 |
| 12 | 1730 | 1730 | Yes | 2.8 |
| 13 | 1182 | 1182 | Yes | 2.49 |
| 14 | 1186 | 1186 | Yes | 4.33 |
| 15 | 1581 | 1581 | Yes | 2.36 |
| 16 | 2152 | 2152 | Yes | 2.1 |
| 17 | 1447 | 1447 | Yes | 2.18 |
| 18 | 1214 | 1214 | Yes | 5.01 |
| 19 | 847 | 847 | Yes | 4.65 |
| 20 | 1338 | 1338 | Yes | 2.53 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 |  | No | 29.25 |
| 2 | 74 | Answer: | No | 13.41 |
| 3 | 63 |  | No | 19.24 |
| 4 | 59 |  | No | 42.36 |
| 5 | 43 |  | No | 17.21 |
| 6 | 56 | 56 | Yes | 13.46 |
| 7 | 64 |  | No | 39.56 |
| 8 | 48 | 48 | Yes | 15.75 |
| 9 | 43 |  | No | 51.94 |
| 10 | 40 |  | No | 33.91 |
| 11 | 73 |  | No | 49.18 |
| 12 | 38 |  | No | 16.39 |
| 13 | 65 |  | No | 20.25 |
| 14 | 51 |  | No | 48.81 |
| 15 | 50 |  | No | 20.0 |
| 16 | 66 |  | No | 54.89 |
| 17 | 56 | 56 | Yes | 16.93 |
| 18 | 63 |  | No | 17.36 |
| 19 | 55 |  | No | 15.35 |
| 20 | 49 |  | No | 53.69 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NGMIDUV | NGMIDUV | Yes | 2.57 |
| 2 | AQWUTNV | AQWUTNV | Yes | 6.84 |
| 3 | OFSHINE | OFSHINE | Yes | 4.74 |
| 4 | HXPCZOM | HXPCZOM | Yes | 5.01 |
| 5 | ILNPHJU | ILNPHJU | Yes | 5.23 |
| 6 | XPMTRYL | XPMTRYL | Yes | 2.55 |
| 7 | RXYNHVL | RXYNHVL | Yes | 2.56 |
| 8 | NLOXRJQ | NLOXRJQ | Yes | 3.39 |
| 9 | ERDVLXH | ERDVLXH | Yes | 5.89 |
| 10 | CYQWLDX | CYQWLDX | Yes | 2.59 |
| 11 | TWIGJRM | TWIGJRM | Yes | 2.67 |
| 12 | BOPGFNU | BOPGFNU | Yes | 5.97 |
| 13 | LSFVCTK | LSFVCTK | Yes | 2.96 |
| 14 | RLKCIGS | RLKCIGS | Yes | 6.97 |
| 15 | AJGTOLW | AJGTOLW | Yes | 8.78 |
| 16 | ULXZGMY | ULXZGMY | Yes | 11.12 |
| 17 | YAVNUSJ | YAVNUSJ | Yes | 8.09 |
| 18 | LMSFNOC | LMSFNOC | Yes | 10.84 |
| 19 | QNZGJCA | QNZGJCA | Yes | 3.12 |
| 20 | TEKPDJA | TEKPDJA | Yes | 4.03 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.89 |
| 2 | [2.1, 7.9] | 2.1 7.9 | Yes | 7.79 |
| 3 | [2.5, 7.5] |  | No | 30.9 |
| 4 | [3.8, 6.2] | 6.2 3.8 | Yes | 2.52 |
| 5 | [0.8, 9.2] | 0.8 9.2 | Yes | 9.8 |
| 6 | [4.9, 5.1] | 5.1 4.9 | Yes | 8.3 |
| 7 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.89 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.82 |
| 9 | [2.6, 7.4] | 2.6 7.4 | Yes | 7.81 |
| 10 | [4.4, 5.6] | 4.4 5.6 | Yes | 11.41 |
| 11 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.03 |
| 12 | [2.1, 7.9] | 2.1 7.9 | Yes | 8.42 |
| 13 | [0.2, 9.8] | 0.2 9.8 | Yes | 8.13 |
| 14 | [3.1, 6.9] | 3.1 6.9 | Yes | 7.67 |
| 15 | [0.3, 9.7] | 0.3 9.7 | Yes | 9.91 |
| 16 | [3.4, 6.6] | 3.4 6.6 | Yes | 8.73 |
| 17 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.81 |
| 18 | [0.1, 9.9] | 0.1 9.9 | Yes | 9.13 |
| 19 | [2.2, 7.8] | 2.2 7.8 | Yes | 29.07 |
| 20 | [1.4, 8.6] | 8.6 1.4 | Yes | 9.65 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PWMJ7SKCK3J5 | PWMJ7SKCK3J5 | Yes | 1.91 |
| 2 | YRHLL7IYSZBR | YRHLL7IYSZBR | Yes | 2.3 |
| 3 | 3CR50QI6TR2S | 3CR50QI6TR2S | Yes | 1.89 |
| 4 | IZYI6CYF82HH | IZYI6CYF82HH | Yes | 3.48 |
| 5 | 53ZUG2AHV05L | 53ZUG2AHV05L | Yes | 3.16 |
| 6 | PZGINVSXE49Y | PZGINVSXE49Y | Yes | 2.51 |
| 7 | 4SD4VOZEE6MT | 4SD4VOZEE6MT | Yes | 1.88 |
| 8 | VV75VIS6P2BF | VV75VIS6P2BF | Yes | 3.36 |
| 9 | B3NJRYLOT3YG | B3NJRYLOT3YG | Yes | 2.43 |
| 10 | 48IADVTN3JTA | 48IADVTN3JTA | Yes | 2.0 |
| 11 | 9XQ2B4NX30BI | 9XQ2B4NX30BI | Yes | 2.15 |
| 12 | 0E85H7BFKXOT | 0E85H7BFKXOT | Yes | 2.38 |
| 13 | 9Y9YOW1UOO2Y | 9Y9YOW1UOO2Y | Yes | 2.65 |
| 14 | AHWUHMRUQODT | AHWUHMRUQODT | Yes | 1.92 |
| 15 | 900E843XVKPS | 900E843XVKPS | Yes | 1.95 |
| 16 | 8K64YIW5DNEC | 8K64YIW5DNEC | Yes | 1.92 |
| 17 | HDKTBAH88PQA | HDKTBAH88PQA | Yes | 1.77 |
| 18 | 9DFJGAE0MHLK | 9DFJGAE0MHLK | Yes | 1.9 |
| 19 | 3LB5CYKUDO86 | 3LB5CYKUDO86 | Yes | 2.04 |
| 20 | UMEUW2KTCVAF | UMEUW2KTCVAF | Yes | 2.13 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 26 | 26 | Yes | 13.48 |
| 2 | 5 | 5 | Yes | 6.21 |
| 3 | 4 | 4 | Yes | 5.18 |
| 4 | 36 | 36 | Yes | 1.9 |
| 5 | 60 | 60 | Yes | 4.2 |
| 6 | 65 | 65 | Yes | 4.45 |
| 7 | 20 |  | No | 62.43 |
| 8 | 31 | 31 | Yes | 2.79 |
| 9 | 5 |  | No | 51.02 |
| 10 | 10 | 10 | Yes | 19.05 |
| 11 | 64 | 64 | Yes | 11.66 |
| 12 | 67 | 67 | Yes | 2.78 |
| 13 | 44 | 44 | Yes | 20.62 |
| 14 | 9 | 9 | Yes | 4.02 |
| 15 | 1440 | 1440 | Yes | 5.04 |
| 16 | 28 | 28 | Yes | 9.45 |
| 17 | 19 | 19 | Yes | 5.65 |
| 18 | 6 | 6 | Yes | 9.46 |
| 19 | 3 |  | No | 42.49 |
| 20 | 1 | 1 | Yes | 3.97 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  <   \/)) |  | No | 50.44 |
| 2 | (\/(\(\/_ | (\/(\(\/_ | Yes | 15.21 |
| 3 | )) )(\\</ | )) )(\\</ | Yes | 6.69 |
| 4 | (/<)\/(   | (/<)\/( | No | 31.17 |
| 5 | _\<\   <( |  | No | 26.12 |
| 6 | (/_(<_(// | (/_(<_(// | Yes | 6.19 |
| 7 |  <(<)(<_  | <(<)(<_ | No | 14.33 |
| 8 | ()\)/\)/) | ()\)/\)/) | Yes | 19.4 |
| 9 | <\<  )/<( | <\<  )/<( | Yes | 8.96 |
| 10 |  < _(_ /< | < _(_ /< | No | 18.76 |
| 11 |  _<_// (/ | _<_// (/ | No | 14.38 |
| 12 | )<)(()<_< | )<)(()<_< | Yes | 6.58 |
| 13 | /)\)/(/\\ | /)\)/(/\\ | Yes | 8.18 |
| 14 | / ()/)< \ | / ()/)< \ | Yes | 12.52 |
| 15 | <_ \/</)  |  | No | 48.63 |
| 16 | (//_ /\ ( | (//_ /\ ( | Yes | 16.05 |
| 17 |  \_</)\<< | \_</)\<< | No | 6.98 |
| 18 | \)\\_) (  | \)\\_) ( | No | 7.87 |
| 19 | / () <)\) | / () <)\) | Yes | 11.7 |
| 20 | /()<_/ () | /()<_/ () | Yes | 4.94 |
