# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-27 10:22:00

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
| sudoku_game | 5199 | 38912 | 44111 | 0 | 20 | 37.05 | 740.98 |
| add_numbers | 3240 | 3031 | 6271 | 20 | 0 | 3.40 | 67.97 |
| counting_zeros | 4640 | 39395 | 44035 | 3 | 17 | 35.37 | 707.36 |
| task_decoding | 4580 | 4901 | 9481 | 20 | 0 | 5.05 | 100.96 |
| task_summation | 4920 | 12310 | 17230 | 20 | 0 | 9.53 | 190.69 |
| task_transcription | 3386 | 1973 | 5359 | 20 | 0 | 1.93 | 38.62 |
| task_sequences | 3241 | 11545 | 14786 | 18 | 2 | 11.41 | 228.2 |
| string_entry | 3677 | 18819 | 22496 | 11 | 9 | 13.46 | 269.16 |
| **TOTAL** | **32883** | **130886** | **163769** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 2 1 2 5 4 5 3 6 6 2 1 3 |  | No | 34.05 |
| 2 | 4 1 6 3 2 6 1 2 1 6 5 6 2 3 |  | No | 44.1 |
| 3 | 6 1 1 6 4 5 1 6 4 6 3 3 2 4 |  | No | 22.61 |
| 4 | 3 5 6 6 3 5 2 6 4 1 5 5 4 2 |  | No | 40.82 |
| 5 | 3 1 6 5 3 6 2 3 3 2 1 2 3 1 |  | No | 34.94 |
| 6 | 4 1 6 5 1 1 2 2 1 6 5 3 6 1 |  | No | 43.04 |
| 7 | 5 2 3 1 4 5 1 5 4 3 2 5 2 6 | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 14.1 |
| 8 | 3 6 4 5 2 6 2 4 2 6 4 1 4 5 |  | No | 27.12 |
| 9 | 6 6 3 1 2 2 5 6 6 3 5 2 3 4 |  | No | 53.53 |
| 10 | 6 1 2 1 3 4 4 5 6 5 4 5 1 4 |  | No | 43.23 |
| 11 | 2 6 6 4 5 3 2 6 2 1 6 3 2 1 |  | No | 24.94 |
| 12 | 1 4 6 3 2 2 1 4 2 5 1 6 4 5 |  | No | 21.98 |
| 13 | 3 4 6 2 5 5 6 4 4 5 6 2 3 1 |  | No | 28.2 |
| 14 | 3 4 1 6 2 5 2 6 3 4 1 3 4 2 |  | No | 40.65 |
| 15 | 5 4 6 6 2 1 3 4 6 3 1 5 2 1 |  | No | 40.05 |
| 16 | 3 4 1 5 6 4 2 6 4 5 6 1 4 3 |  | No | 28.31 |
| 17 | 5 2 3 1 3 4 5 6 5 2 4 3 5 4 |  | No | 48.8 |
| 18 | 6 3 6 3 2 5 5 3 6 3 1 5 4 1 |  | No | 46.1 |
| 19 | 4 6 1 3 4 1 2 6 3 2 5 5 1 3 |  | No | 55.69 |
| 20 | 3 6 2 6 1 4 4 6 3 2 6 3 4 1 |  | No | 48.71 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2179 | 2179 | Yes | 2.97 |
| 2 | 1045 | 1045 | Yes | 4.65 |
| 3 | 1375 | 1375 | Yes | 3.52 |
| 4 | 2024 | 2024 | Yes | 6.06 |
| 5 | 1937 | 1937 | Yes | 2.66 |
| 6 | 1074 | 1074 | Yes | 2.6 |
| 7 | 2285 | 2285 | Yes | 3.08 |
| 8 | 1673 | 1673 | Yes | 2.42 |
| 9 | 1652 | 1652 | Yes | 2.41 |
| 10 | 1720 | 1720 | Yes | 2.33 |
| 11 | 1811 | 1811 | Yes | 1.91 |
| 12 | 1719 | 1719 | Yes | 7.63 |
| 13 | 2036 | 2036 | Yes | 4.37 |
| 14 | 1327 | 1327 | Yes | 2.47 |
| 15 | 1151 | 1151 | Yes | 2.51 |
| 16 | 1463 | 1463 | Yes | 2.64 |
| 17 | 1853 | 1853 | Yes | 4.08 |
| 18 | 1993 | 1993 | Yes | 2.75 |
| 19 | 1710 | 1710 | Yes | 4.39 |
| 20 | 2111 | 2111 | Yes | 2.48 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53 |  | No | 36.27 |
| 2 | 58 |  | No | 45.46 |
| 3 | 47 |  | No | 37.28 |
| 4 | 66 | 66 | Yes | 11.01 |
| 5 | 70 |  | No | 43.57 |
| 6 | 37 |  | No | 39.07 |
| 7 | 56 |  | No | 46.64 |
| 8 | 53 |  | No | 37.81 |
| 9 | 51 | 51 | Yes | 13.21 |
| 10 | 66 |  | No | 46.59 |
| 11 | 64 | 64 | Yes | 17.92 |
| 12 | 69 |  | No | 48.24 |
| 13 | 68 |  | No | 44.78 |
| 14 | 72 |  | No | 40.44 |
| 15 | 58 |  | No | 48.95 |
| 16 | 51 |  | No | 46.73 |
| 17 | 75 |  | No | 37.33 |
| 18 | 64 |  | No | 15.86 |
| 19 | 47 |  | No | 31.12 |
| 20 | 42 |  | No | 19.05 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | HCGTDSY | HCGTDSY | Yes | 4.44 |
| 2 | PIVWLHD | PIVWLHD | Yes | 7.97 |
| 3 | CRMYSEQ | CRMYSEQ | Yes | 5.19 |
| 4 | AJPGUQB | AJPGUQB | Yes | 6.54 |
| 5 | GFJHEBT | GFJHEBT | Yes | 3.05 |
| 6 | RYOMSBX | RYOMSBX | Yes | 5.48 |
| 7 | PKFSNYI | PKFSNYI | Yes | 6.56 |
| 8 | KEYPBTG | KEYPBTG | Yes | 4.85 |
| 9 | HGZASQO | HGZASQO | Yes | 4.61 |
| 10 | WCZTGRY | WCZTGRY | Yes | 5.76 |
| 11 | CJWVYNE | CJWVYNE | Yes | 2.37 |
| 12 | LERCPNS | LERCPNS | Yes | 3.52 |
| 13 | AVZUBMJ | AVZUBMJ | Yes | 6.09 |
| 14 | XKMUEJY | XKMUEJY | Yes | 2.51 |
| 15 | STBEUXQ | STBEUXQ | Yes | 4.53 |
| 16 | ZMIWVKO | ZMIWVKO | Yes | 9.4 |
| 17 | VUJSPXF | VUJSPXF | Yes | 5.19 |
| 18 | RFGMWBE | RFGMWBE | Yes | 2.54 |
| 19 | UPJIHGW | UPJIHGW | Yes | 4.15 |
| 20 | YADVPLG | YADVPLG | Yes | 6.21 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.3, 6.7] | 3.3 6.7 | Yes | 4.11 |
| 2 | [2.6, 7.4] | 7.4 2.6 | Yes | 6.66 |
| 3 | [4.2, 5.8] | 5.8 4.2 | Yes | 9.34 |
| 4 | [2.5, 7.5] | 2.5 7.5 | Yes | 9.5 |
| 5 | [3.8, 6.2] | 3.8 6.2 | Yes | 8.76 |
| 6 | [0.8, 9.2] | 9.2 0.8 | Yes | 8.7 |
| 7 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.49 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 8.54 |
| 9 | [0.5, 9.5] | 0.5 9.5 | Yes | 8.47 |
| 10 | [0.7, 9.3] | 9.3 0.7 | Yes | 8.19 |
| 11 | [4.4, 5.6] | 4.4 5.6 | Yes | 13.61 |
| 12 | [3.6, 6.4] | 3.6 6.4 | Yes | 8.0 |
| 13 | [3.6, 6.4] | 6.4 3.6 | Yes | 25.54 |
| 14 | [0.9, 9.1] | 0.9 9.1 | Yes | 7.74 |
| 15 | [1.1, 8.9] | 8.9 1.1 | Yes | 8.14 |
| 16 | [1.3, 8.7] | 1.3 8.7 | Yes | 10.17 |
| 17 | [3.6, 6.4] | 3.6 6.4 | Yes | 6.45 |
| 18 | [1.6, 8.4] | 1.6 8.4 | Yes | 11.41 |
| 19 | [4.3, 5.7] | 4.3 5.7 | Yes | 13.03 |
| 20 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.83 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | W6IN0F306UWX | W6IN0F306UWX | Yes | 2.12 |
| 2 | OAWXNTR3XZT8 | OAWXNTR3XZT8 | Yes | 1.54 |
| 3 | ZSPOHQHM1RT1 | ZSPOHQHM1RT1 | Yes | 1.7 |
| 4 | PKGCZ3M1F6U6 | PKGCZ3M1F6U6 | Yes | 1.93 |
| 5 | 4L3WEMALOWQ9 | 4L3WEMALOWQ9 | Yes | 1.4 |
| 6 | CICFAV2W69Z3 | CICFAV2W69Z3 | Yes | 1.59 |
| 7 | LKZMP21UG5OF | LKZMP21UG5OF | Yes | 4.54 |
| 8 | YC69WS0IXO1R | YC69WS0IXO1R | Yes | 1.56 |
| 9 | 25ZKD83SVCD4 | 25ZKD83SVCD4 | Yes | 1.99 |
| 10 | 14YIMWAWD6LC | 14YIMWAWD6LC | Yes | 1.34 |
| 11 | 2YUKAOML4WAT | 2YUKAOML4WAT | Yes | 1.76 |
| 12 | MILN4BD7DME2 | MILN4BD7DME2 | Yes | 1.36 |
| 13 | IXN9LMQT42Q6 | IXN9LMQT42Q6 | Yes | 1.95 |
| 14 | 4K09OFVU2WXH | 4K09OFVU2WXH | Yes | 2.1 |
| 15 | RWS90RSZV8Y3 | RWS90RSZV8Y3 | Yes | 1.8 |
| 16 | PABGYU0FBLP5 | PABGYU0FBLP5 | Yes | 2.13 |
| 17 | 7MJQ7U4P2Z3W | 7MJQ7U4P2Z3W | Yes | 1.82 |
| 18 | AVNSC02K8NTR | AVNSC02K8NTR | Yes | 1.99 |
| 19 | 1LHTNTWIX0ZF | 1LHTNTWIX0ZF | Yes | 2.46 |
| 20 | ZDUVEDCUA0BD | ZDUVEDCUA0BD | Yes | 1.57 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 5.19 |
| 2 | 5 |  | No | 48.18 |
| 3 | 3 | 3 | Yes | 11.27 |
| 4 | 23 | 23 | Yes | 4.64 |
| 5 | 198 | 198 | Yes | 3.0 |
| 6 | 20 |  | No | 47.22 |
| 7 | 1440 | 1440 | Yes | 5.25 |
| 8 | 44 | 44 | Yes | 12.88 |
| 9 | 3 | 3 | Yes | 19.29 |
| 10 | 9 | 9 | Yes | 3.49 |
| 11 | 16 | 16 | Yes | 6.18 |
| 12 | 6 | 6 | Yes | 4.89 |
| 13 | 60 | 60 | Yes | 4.2 |
| 14 | 31 | 31 | Yes | 6.93 |
| 15 | 10 | 10 | Yes | 6.5 |
| 16 | 4096 | 4096 | Yes | 13.44 |
| 17 | 63 | 63 | Yes | 5.6 |
| 18 | 7680 | 7680 | Yes | 6.02 |
| 19 | 5 | 5 | Yes | 10.08 |
| 20 | 67 | 67 | Yes | 3.95 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <)/\_ \_\ | <)/\_ \_\ | Yes | 11.66 |
| 2 | \(/)_<\/( | /\) <(_<) | No | 8.26 |
| 3 | <___\( (< | <___\ ( (< | No | 10.65 |
| 4 | <<<)(\/\/ | <<<)(\/\/ | Yes | 7.56 |
| 5 | <\/\/<< < | <\/\/<< < | Yes | 14.88 |
| 6 | (// _/_(_ | (// _/_(_ | Yes | 5.28 |
| 7 | _/_\//_   | _/_\//_ | No | 11.14 |
| 8 | _ \_/<)\) | /\) <(_<) | No | 21.04 |
| 9 | \_(/)< <) | /\) <(_<) | No | 25.19 |
| 10 | )< <)< () | )< <)< () | Yes | 4.78 |
| 11 |  <_<_/_/< | <_<_/_< | No | 14.71 |
| 12 | )\_<_\( ( | )\_<_\( ( | Yes | 9.05 |
| 13 | ) ) ( (\< | ) ) ( (\< | Yes | 19.06 |
| 14 |  (\_//)__ | /\) <(_<) (\_//)__ | No | 11.29 |
| 15 | \_<))(< < | \_<))(< < | Yes | 9.65 |
| 16 |  )(\()(\  |  | No | 42.91 |
| 17 | _<\<//\)< | _<\<//\)< | Yes | 3.05 |
| 18 | )<_(_<_)( | )<_(_<_)( | Yes | 13.28 |
| 19 | / \<//()_ | / \<//()_ | Yes | 10.46 |
| 20 | _\)(<//\  | _\)(<//\ | No | 15.28 |
