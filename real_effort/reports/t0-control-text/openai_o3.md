# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-26 16:08:49

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
| sudoku_game | 4672 | 40920 | 45592 | 1 | 19 | 43.16 | 863.25 |
| add_numbers | 2420 | 2697 | 5117 | 20 | 0 | 3.81 | 76.19 |
| counting_zeros | 3820 | 39508 | 43328 | 3 | 17 | 43.72 | 874.44 |
| task_decoding | 3760 | 5562 | 9322 | 20 | 0 | 5.35 | 107.0 |
| task_summation | 4100 | 14385 | 18485 | 18 | 2 | 14.27 | 285.36 |
| task_transcription | 2555 | 1947 | 4502 | 20 | 0 | 2.84 | 56.72 |
| task_sequences | 2421 | 11506 | 13927 | 17 | 3 | 16.59 | 331.75 |
| string_entry | 2859 | 18373 | 21232 | 13 | 7 | 17.47 | 349.41 |
| **TOTAL** | **26607** | **134898** | **161505** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 3 6 1 4 1 5 6 3 1 3 3 3 4 |  | No | 53.71 |
| 2 | 5 3 4 2 3 6 4 6 2 6 3 2 6 1 | 5 3 4 2 3 6 4 6 2 6 3 2 6 1 | Yes | 30.44 |
| 3 | 4 1 1 6 4 4 6 1 1 2 3 5 4 1 |  | No | 29.14 |
| 4 | 6 1 4 6 5 4 2 1 5 1 3 6 4 5 |  | No | 49.15 |
| 5 | 5 1 3 1 6 3 5 6 1 4 2 2 5 5 |  | No | 52.74 |
| 6 | 2 4 1 4 1 1 4 6 1 3 6 2 6 1 |  | No | 33.92 |
| 7 | 2 3 3 1 2 4 1 2 1 6 5 1 5 3 |  | No | 23.4 |
| 8 | 1 4 4 2 3 6 2 5 3 2 1 1 6 6 |  | No | 44.07 |
| 9 | 1 2 2 3 5 1 6 4 3 6 2 2 3 2 |  | No | 54.68 |
| 10 | 2 1 4 2 5 3 6 1 1 5 3 4 2 5 |  | No | 75.01 |
| 11 | 5 1 6 2 5 1 6 5 2 3 4 1 6 4 |  | No | 50.46 |
| 12 | 2 4 3 5 4 6 3 6 6 4 5 1 5 4 |  | No | 33.73 |
| 13 | 6 3 3 5 3 1 6 2 2 6 5 4 6 3 |  | No | 37.16 |
| 14 | 6 2 1 3 5 5 6 1 1 2 6 1 3 4 |  | No | 40.14 |
| 15 | 5 1 6 4 1 3 4 5 5 4 2 6 2 4 |  | No | 34.88 |
| 16 | 5 1 3 6 3 1 5 5 4 6 1 4 6 2 |  | No | 34.01 |
| 17 | 3 1 5 2 5 3 3 1 4 5 2 1 4 2 |  | No | 62.84 |
| 18 | 1 5 1 5 2 2 3 1 2 1 6 4 2 4 |  | No | 40.46 |
| 19 | 3 1 5 2 6 4 2 3 4 3 4 1 6 3 |  | No | 55.03 |
| 20 | 1 1 3 5 4 5 6 2 6 1 3 4 2 1 |  | No | 28.23 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2020 | 2020 | Yes | 3.7 |
| 2 | 1073 | 1073 | Yes | 4.53 |
| 3 | 1575 | 1575 | Yes | 2.44 |
| 4 | 1331 | 1331 | Yes | 2.67 |
| 5 | 1529 | 1529 | Yes | 4.75 |
| 6 | 1040 | 1040 | Yes | 2.7 |
| 7 | 1367 | 1367 | Yes | 2.33 |
| 8 | 1500 | 1500 | Yes | 3.67 |
| 9 | 2391 | 2391 | Yes | 2.29 |
| 10 | 2098 | 2098 | Yes | 3.27 |
| 11 | 2155 | 2155 | Yes | 4.15 |
| 12 | 1739 | 1739 | Yes | 3.73 |
| 13 | 1355 | 1355 | Yes | 3.16 |
| 14 | 1848 | 1848 | Yes | 1.77 |
| 15 | 1546 | 1546 | Yes | 3.93 |
| 16 | 1641 | 1641 | Yes | 6.96 |
| 17 | 1021 | 1021 | Yes | 8.48 |
| 18 | 1272 | 1272 | Yes | 3.07 |
| 19 | 2088 | 2088 | Yes | 4.83 |
| 20 | 1339 | 1339 | Yes | 3.75 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 |  | No | 50.92 |
| 2 | 50 |  | No | 62.76 |
| 3 | 74 |  | No | 48.92 |
| 4 | 67 | 67 | Yes | 18.73 |
| 5 | 73 |  | No | 37.18 |
| 6 | 73 |  | No | 49.75 |
| 7 | 63 |  | No | 53.7 |
| 8 | 73 |  | No | 50.9 |
| 9 | 58 |  | No | 39.55 |
| 10 | 73 | 73 | Yes | 22.58 |
| 11 | 72 |  | No | 64.37 |
| 12 | 49 |  | No | 56.59 |
| 13 | 56 |  | No | 46.8 |
| 14 | 50 |  | No | 43.93 |
| 15 | 36 |  | No | 43.5 |
| 16 | 67 | 67 | Yes | 28.73 |
| 17 | 46 |  | No | 24.35 |
| 18 | 51 |  | No | 47.76 |
| 19 | 47 |  | No | 38.67 |
| 20 | 43 |  | No | 44.73 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | LSXZQVJ | LSXZQVJ | Yes | 3.71 |
| 2 | XZAOJUN | XZAOJUN | Yes | 4.17 |
| 3 | HOAKVBX | HOAKVBX | Yes | 3.57 |
| 4 | MUVHIPG | MUVHIPG | Yes | 6.54 |
| 5 | JCZSEAX | JCZSEAX | Yes | 12.74 |
| 6 | CZREQSM | CZREQSM | Yes | 13.61 |
| 7 | WAZTYUE | WAZTYUE | Yes | 3.4 |
| 8 | QDCLJIM | QDCLJIM | Yes | 3.37 |
| 9 | FTNIMVY | FTNIMVY | Yes | 4.31 |
| 10 | ELXWKPD | ELXWKPD | Yes | 6.06 |
| 11 | UHCBVQW | UHCBVQW | Yes | 3.1 |
| 12 | CQUYGTA | CQUYGTA | Yes | 8.63 |
| 13 | YBOQXCD | YBOQXCD | Yes | 4.02 |
| 14 | DFAHPIZ | DFAHPIZ | Yes | 3.54 |
| 15 | TXYWSVR | TXYWSVR | Yes | 5.46 |
| 16 | WZDXVPC | WZDXVPC | Yes | 3.73 |
| 17 | FLUZAPR | FLUZAPR | Yes | 6.15 |
| 18 | XNIBSLJ | XNIBSLJ | Yes | 3.13 |
| 19 | QDGLBRE | QDGLBRE | Yes | 3.52 |
| 20 | FOJVTQW | FOJVTQW | Yes | 4.23 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 3.9 6.1 | Yes | 11.54 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 7.48 |
| 3 | [4.7, 5.3] | 5.3 4.7 | Yes | 7.04 |
| 4 | [4.1, 5.9] | 5.9 4.1 | Yes | 15.61 |
| 5 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.06 |
| 6 | [0.3, 9.7] | 9.7 0.3 | Yes | 10.51 |
| 7 | [4.0, 6.0] |  | No | 59.18 |
| 8 | [2.7, 7.3] | 2.7 7.3 | Yes | 10.52 |
| 9 | [4.0, 6.0] | 4.0 6.0 | Yes | 6.02 |
| 10 | [3.6, 6.4] | 6.4 3.6 | Yes | 9.86 |
| 11 | [4.6, 5.4] | 4.6 5.4 | Yes | 15.38 |
| 12 | [4.8, 5.2] | 4.8 5.2 | Yes | 5.19 |
| 13 | [0.6, 9.4] | 0.6 9.4 | Yes | 21.2 |
| 14 | [1.6, 8.4] |  | No | 37.57 |
| 15 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.79 |
| 16 | [0.5, 9.5] | 0.5 9.5 | Yes | 8.87 |
| 17 | [0.2, 9.8] | 0.2 9.8 | Yes | 13.15 |
| 18 | [3.2, 6.8] | 3.2 6.8 | Yes | 10.93 |
| 19 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.72 |
| 20 | [3.5, 6.5] | 3.5 6.5 | Yes | 7.73 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | WUTGU3TSW324 | WUTGU3TSW324 | Yes | 1.75 |
| 2 | LKBUSODA29Q5 | LKBUSODA29Q5 | Yes | 2.21 |
| 3 | ZAGXATLFALE6 | ZAGXATLFALE6 | Yes | 2.31 |
| 4 | WHXG7QIOK1OM | WHXG7QIOK1OM | Yes | 2.05 |
| 5 | DRH82GREC4VM | DRH82GREC4VM | Yes | 2.04 |
| 6 | EUZWLLVSAQR1 | EUZWLLVSAQR1 | Yes | 2.22 |
| 7 | S6FQD56I6EZG | S6FQD56I6EZG | Yes | 2.43 |
| 8 | AMC99JL9FSHO | AMC99JL9FSHO | Yes | 1.81 |
| 9 | K5AUDW2TOBOC | K5AUDW2TOBOC | Yes | 2.54 |
| 10 | 9XPBY1E9IBD9 | 9XPBY1E9IBD9 | Yes | 2.82 |
| 11 | GC9CQE3IDFE0 | GC9CQE3IDFE0 | Yes | 3.6 |
| 12 | BHRP0XTWMSRQ | BHRP0XTWMSRQ | Yes | 2.08 |
| 13 | FO41NLRN6XNI | FO41NLRN6XNI | Yes | 5.27 |
| 14 | ALPU9DQ6IRJO | ALPU9DQ6IRJO | Yes | 3.53 |
| 15 | SZ2XV5O8TNJZ | SZ2XV5O8TNJZ | Yes | 2.08 |
| 16 | Z2F4739RG38Q | Z2F4739RG38Q | Yes | 1.9 |
| 17 | 2RGQL6BB0OQ2 | 2RGQL6BB0OQ2 | Yes | 1.98 |
| 18 | Y2OMLLWEH3NP | Y2OMLLWEH3NP | Yes | 2.43 |
| 19 | TODJIWE9386R | TODJIWE9386R | Yes | 7.24 |
| 20 | C74VS4ZU8QQD | C74VS4ZU8QQD | Yes | 4.42 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 9.54 |
| 2 | 5 |  | No | 86.11 |
| 3 | 7680 | 7680 | Yes | 9.58 |
| 4 | 1 | 1 | Yes | 9.3 |
| 5 | 65 | 65 | Yes | 9.08 |
| 6 | 63 | 63 | Yes | 6.78 |
| 7 | 9 | 9 | Yes | 8.41 |
| 8 | 5 | 5 | Yes | 8.35 |
| 9 | 243 | 243 | Yes | 3.26 |
| 10 | 19 | 19 | Yes | 6.52 |
| 11 | 4096 |  | No | 59.84 |
| 12 | 3 | 3 | Yes | 12.04 |
| 13 | 20 |  | No | 50.75 |
| 14 | 9 | 9 | Yes | 5.46 |
| 15 | 60 | 60 | Yes | 6.69 |
| 16 | 16 | 16 | Yes | 4.39 |
| 17 | 31 | 31 | Yes | 4.1 |
| 18 | 48 | 48 | Yes | 4.92 |
| 19 | 793 | 793 | Yes | 2.88 |
| 20 | 26 | 26 | Yes | 23.75 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | < ) / )</ | /\) <(_<)< ) / )< | No | 27.18 |
| 2 | \\) )<_ ) | \\) )<_ ) | Yes | 19.3 |
| 3 | <(\)) /_/ | <(\)) /_/ | Yes | 6.55 |
| 4 | /(_)/<\__ | /\) <(_<) | No | 7.26 |
| 5 | _/()<\/)_ | _/()<\/)_ | Yes | 11.11 |
| 6 |  <_/ <(_  | <_/ <(_ | No | 16.32 |
| 7 | ()\ _ _(/ | ()\ _ _(/ | Yes | 22.79 |
| 8 | <_\(\()\) |  | No | 38.72 |
| 9 | )_))\(/\/ | /\) <(_<) | No | 29.52 |
| 10 | <)\ )/ \_ | <)\ )/ \_ | Yes | 11.74 |
| 11 |  )_//_/_< | )_//_/_< | No | 10.4 |
| 12 | ((\)\(/ \ | ((\)\(/ \ | Yes | 7.54 |
| 13 | /) \_ \<\ | /) \_ \<\ | Yes | 4.18 |
| 14 | ) <<\_)(( | ) <<\_)(( | Yes | 5.08 |
| 15 | //\_(\(/) | //\_(\(/) | Yes | 7.86 |
| 16 | ((\)\  (  |  | No | 63.93 |
| 17 | (/(<)) <_ | (/(<)) <_ | Yes | 12.79 |
| 18 | (<(()(\)< | (<(()(\)< | Yes | 8.07 |
| 19 | \( /<)_ ( | \( /<)_ ( | Yes | 21.99 |
| 20 | \( _\<()) | \( _\<()) | Yes | 17.07 |
