# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-26 11:02:46

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
| sudoku_game | 7200 | 38667 | 45867 | 6 | 14 | 40.89 | 817.95 |
| add_numbers | 3780 | 1704 | 5484 | 19 | 1 | 3.51 | 70.4 |
| counting_zeros | 6200 | 36633 | 42833 | 2 | 18 | 39.10 | 782.27 |
| task_decoding | 11940 | 4674 | 16614 | 20 | 0 | 5.45 | 109.18 |
| task_summation | 7140 | 6253 | 13393 | 20 | 0 | 6.24 | 125.05 |
| task_transcription | 3598 | 10073 | 13671 | 1 | 19 | 6.48 | 129.78 |
| task_sequences | 2900 | 13593 | 16493 | 15 | 5 | 12.90 | 257.97 |
| string_entry | 4200 | 27966 | 32166 | 9 | 11 | 28.44 | 568.93 |
| **TOTAL** | **46958** | **139563** | **186521** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 4 4 3 5 2 6 6 4 2 1 1 4 3 |  | No | 70.76 |
| 2 | 2 3 2 5 6 3 3 6 1 4 3 4 2 6 | 2 3 2 5 6 3 3 6 1 4 3 4 2 6 | Yes | 23.27 |
| 3 | 2 4 5 2 4 6 3 6 6 4 2 3 2 3 |  | No | 49.72 |
| 4 | 2 5 3 6 2 4 5 2 6 2 6 6 3 5 |  | No | 46.16 |
| 5 | 4 1 2 6 3 5 1 6 5 3 5 4 2 1 | 4 1 2 6 3 5 1 6 5 3 5 4 2 1 | Yes | 26.39 |
| 6 | 4 2 6 5 4 6 4 2 4 6 5 6 2 1 |  | No | 59.08 |
| 7 | 2 4 1 4 5 2 1 4 5 1 6 1 5 4 |  | No | 40.7 |
| 8 | 2 2 6 1 5 5 3 6 4 2 1 4 6 1 |  | No | 47.76 |
| 9 | 1 6 6 3 4 3 4 2 1 2 5 5 3 6 |  | No | 59.87 |
| 10 | 5 3 3 5 4 1 2 6 1 4 1 2 6 1 |  | No | 36.3 |
| 11 | 4 2 5 3 1 5 5 1 4 5 1 3 5 4 |  | No | 35.32 |
| 12 | 4 2 3 6 1 3 5 4 2 1 3 3 4 2 |  | No | 43.51 |
| 13 | 4 3 6 1 3 1 6 2 3 6 5 4 6 5 |  | No | 43.12 |
| 14 | 3 5 2 6 1 4 2 1 3 1 2 4 3 1 | 3 5 2 6 1 4 2 1 3 1 2 4 3 1 | Yes | 18.22 |
| 15 | 3 6 5 5 5 3 6 4 5 5 1 2 3 4 |  | No | 62.11 |
| 16 | 2 3 4 4 5 3 2 6 1 2 3 5 6 1 |  | No | 55.01 |
| 17 | 3 1 2 1 3 6 1 2 3 5 1 1 4 3 | 3 1 2 1 3 6 1 2 3 5 1 1 4 3 | Yes | 22.12 |
| 18 | 2 1 1 6 3 1 4 5 2 5 4 4 2 3 | 2 1 1 6 3 1 4 5 2 5 4 4 2 3 | Yes | 21.88 |
| 19 | 2 6 1 1 2 6 1 2 5 3 4 1 3 1 |  | No | 42.24 |
| 20 | 2 6 2 1 5 5 6 5 2 1 3 1 4 5 | 2 6 2 1 5 5 6 5 2 1 3 1 4 5 | Yes | 14.21 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1667 | 1667 | Yes | 3.48 |
| 2 | 941 | 941 | Yes | 3.59 |
| 3 | 2294 | 2294 | Yes | 3.67 |
| 4 | 1138 | 1138 | Yes | 2.78 |
| 5 | 2371 | 2371 | Yes | 3.33 |
| 6 | 537 | 537 | Yes | 2.05 |
| 7 | 1712 | 1712 | Yes | 3.44 |
| 8 | 1913 | 1913 | Yes | 4.18 |
| 9 | 2323 | 2317 | No | 4.61 |
| 10 | 2116 | 2116 | Yes | 3.97 |
| 11 | 1930 | 1930 | Yes | 3.99 |
| 12 | 1721 | 1721 | Yes | 2.94 |
| 13 | 1397 | 1397 | Yes | 3.32 |
| 14 | 1772 | 1772 | Yes | 4.22 |
| 15 | 1268 | 1268 | Yes | 3.45 |
| 16 | 1727 | 1727 | Yes | 1.91 |
| 17 | 2080 | 2080 | Yes | 2.62 |
| 18 | 2265 | 2265 | Yes | 4.16 |
| 19 | 1482 | 1482 | Yes | 4.11 |
| 20 | 1807 | 1807 | Yes | 4.48 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 40 | 67 | No | 20.42 |
| 2 | 52 | 67 | No | 20.67 |
| 3 | 52 |  | No | 77.58 |
| 4 | 46 |  | No | 75.02 |
| 5 | 46 |  | No | 65.01 |
| 6 | 69 | 67 | No | 18.77 |
| 7 | 70 | 69 | No | 21.94 |
| 8 | 64 |  | No | 46.91 |
| 9 | 73 |  | No | 43.02 |
| 10 | 43 |  | No | 49.24 |
| 11 | 75 | 67 | No | 19.95 |
| 12 | 61 | 67 | No | 19.88 |
| 13 | 48 |  | No | 50.98 |
| 14 | 45 | 67 | No | 17.34 |
| 15 | 75 | 75 | Yes | 22.4 |
| 16 | 45 |  | No | 44.88 |
| 17 | 53 | 67 | No | 14.14 |
| 18 | 72 | 72 | Yes | 22.0 |
| 19 | 54 |  | No | 57.72 |
| 20 | 69 |  | No | 74.09 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | EJVIAXY | EJVIAXY | Yes | 7.33 |
| 2 | XRTANJO | XRTANJO | Yes | 3.52 |
| 3 | XODJZGB | XODJZGB | Yes | 3.25 |
| 4 | JSQTPHA | JSQTPHA | Yes | 4.98 |
| 5 | AXHIBJD | AXHIBJD | Yes | 8.09 |
| 6 | NSWDKXC | NSWDKXC | Yes | 5.84 |
| 7 | FXWPLYR | FXWPLYR | Yes | 5.62 |
| 8 | FKQIBEY | FKQIBEY | Yes | 5.7 |
| 9 | HYSGMNA | HYSGMNA | Yes | 5.23 |
| 10 | JCVBKWT | JCVBKWT | Yes | 5.43 |
| 11 | ROZGVMY | ROZGVMY | Yes | 5.43 |
| 12 | IBQUFHK | IBQUFHK | Yes | 4.64 |
| 13 | LBTWMQA | LBTWMQA | Yes | 7.52 |
| 14 | APDLJER | APDLJER | Yes | 5.7 |
| 15 | LVUSBDZ | LVUSBDZ | Yes | 5.04 |
| 16 | LFNVOXG | LFNVOXG | Yes | 6.59 |
| 17 | GSUNFMR | GSUNFMR | Yes | 5.59 |
| 18 | FIKPXEJ | FIKPXEJ | Yes | 5.12 |
| 19 | LNHVKBJ | LNHVKBJ | Yes | 6.0 |
| 20 | EZTNVSB | EZTNVSB | Yes | 2.35 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.8, 7.2] | 2.8 7.2 | Yes | 5.33 |
| 2 | [2.4, 7.6] | 2.4 7.6 | Yes | 5.95 |
| 3 | [3.0, 7.0] | 3.0 7.0 | Yes | 7.76 |
| 4 | [0.5, 9.5] | 9.5 0.5 | Yes | 7.31 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 5.48 |
| 6 | [3.9, 6.1] | 3.9 6.1 | Yes | 6.79 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.91 |
| 8 | [4.5, 5.5] | 4.5 5.5 | Yes | 4.69 |
| 9 | [4.0, 6.0] | 6.0 4.0 | Yes | 6.89 |
| 10 | [0.2, 9.8] | 9.8 0.2 | Yes | 6.4 |
| 11 | [2.5, 7.5] | 7.5 2.5 | Yes | 7.8 |
| 12 | [2.6, 7.4] | 7.4 2.6 | Yes | 5.32 |
| 13 | [2.2, 7.8] | 2.2 7.8 | Yes | 5.64 |
| 14 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.49 |
| 15 | [3.7, 6.3] | 3.7 6.3 | Yes | 7.05 |
| 16 | [4.6, 5.4] | 5.4 4.6 | Yes | 7.22 |
| 17 | [2.9, 7.1] | 7.1 2.9 | Yes | 4.62 |
| 18 | [0.2, 9.8] | 0.2 9.8 | Yes | 7.08 |
| 19 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.62 |
| 20 | [0.5, 9.5] | 0.5 9.5 | Yes | 5.49 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | E1ISWKRDXR84 | E1ISWKRDOXR84 | No | 7.16 |
| 2 | 75LOH60QZ9FE | 75LOH8OOZ9FE | No | 3.1 |
| 3 | AYSGEGKELMLO | AYSGEKEKELMLO | No | 9.75 |
| 4 | YSQEBCXEALKK | VSOEBCXEALKK | No | 5.22 |
| 5 | YUB0U2W90VFZ | YUEB0U2W90VFZ | No | 5.2 |
| 6 | YEB2YUZDBIXK | YEB2YUZDBIXK | Yes | 4.75 |
| 7 | SIGZB0FFQ6DW | SIGZBOFFQ6DW | No | 2.04 |
| 8 | UWV93400GTP6 | UWV93400GPT6 | No | 4.82 |
| 9 | JSGAKNMARV0Q | JSGAKNMARVOQ | No | 7.51 |
| 10 | A8I8EYNM3MQB | A818EYNM3MQB | No | 2.97 |
| 11 | IZQ8PXHVGWQW | IZQ8PXHVGWQV | No | 11.53 |
| 12 | Q8DFYPJG5337 | Q8DFYPJGS337 | No | 5.28 |
| 13 | Z3USM76Q1BIZ | Z3USM7601BIZ | No | 3.17 |
| 14 | 3JHB4EF1YJO0 | 3JHB4EF1YJ00 | No | 7.41 |
| 15 | 0REL1K8AX2XO | OREL1K8AX2XO | No | 5.4 |
| 16 | 7AZQSOZSDMYZ | 7AZOSOZSDMYZ | No | 7.47 |
| 17 | POHSOKP59VYD | POHS0KP5SVYD | No | 11.24 |
| 18 | BRQ5707JA3G2 | BR050707JA3G2 | No | 9.7 |
| 19 | H1S582WFJ29Q | H1S582WFJ290 | No | 11.31 |
| 20 | JWI6EDGALAJT | JWISEDGALAJT | No | 4.62 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 7680 | 7680 | Yes | 2.2 |
| 2 | 793 | 793 | Yes | 2.82 |
| 3 | 3 |  | No | 35.76 |
| 4 | 20 |  | No | 39.72 |
| 5 | 3 | 3 | Yes | 19.07 |
| 6 | 73 | 73 | Yes | 3.99 |
| 7 | 39 | 39 | Yes | 4.23 |
| 8 | 5 |  | No | 39.41 |
| 9 | 7 | 7 | Yes | 3.1 |
| 10 | 23 |  | No | 45.68 |
| 11 | 4 | 4 | Yes | 7.91 |
| 12 | 5 | 5 | Yes | 7.3 |
| 13 | 1440 | 1440 | Yes | 5.41 |
| 14 | 1 | 1 | Yes | 7.12 |
| 15 | 19 | 19 | Yes | 4.57 |
| 16 | 198 | 198 | Yes | 3.91 |
| 17 | 9 | 9 | Yes | 4.46 |
| 18 | 10 | 9 | No | 9.16 |
| 19 | 60 | 60 | Yes | 4.0 |
| 20 | 4 | 4 | Yes | 8.14 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  /_\<\)_\ |  | No | 55.08 |
| 2 | \</ _//<) | \</(_//<) | No | 15.52 |
| 3 | \()<<</_) | \()<<</_) | Yes | 6.62 |
| 4 | </(\<)\)_ | </(\<)\)_ | Yes | 12.35 |
| 5 | //<)<<)(_ |  | No | 58.18 |
| 6 | )///<(\<  | )///<(\<␣ | Yes | 19.47 |
| 7 | </_// )<( |  | No | 59.67 |
| 8 | _(\_( <)  | _(\_(<)␣␣ | No | 19.59 |
| 9 | ))(<\/ /) | ))(<\/_/ ) | No | 10.36 |
| 10 | /\<< )/)  |  | No | 59.02 |
| 11 | <\/ _(/ < |  | No | 23.8 |
| 12 |  \(\<_\\  |  | No | 35.03 |
| 13 | /_(/)_<(_ | /_(/)_<(_ | Yes | 3.42 |
| 14 | ))/(_  \( |  | No | 55.68 |
| 15 | () <\//\\ | () <\//\\ | Yes | 17.04 |
| 16 | <)\) <)// | <)\)_<)// | Yes | 13.39 |
| 17 |   \_/\    | __\_/\___ | Yes | 15.83 |
| 18 | / \ \__\\ |  | No | 53.9 |
| 19 | __ _</</\ | __ _</</\ | Yes | 21.01 |
| 20 | <\ < <_/_ | <\ < <_/_ | Yes | 13.9 |
