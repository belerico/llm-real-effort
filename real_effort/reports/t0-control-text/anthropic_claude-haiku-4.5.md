# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-26 15:35:10

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
| sudoku_game | 5789 | 32763 | 38552 | 4 | 16 | 14.04 | 280.92 |
| add_numbers | 3180 | 2893 | 6073 | 20 | 0 | 2.60 | 51.99 |
| counting_zeros | 4500 | 20847 | 25347 | 2 | 18 | 8.25 | 164.95 |
| task_decoding | 4500 | 6214 | 10714 | 20 | 0 | 4.24 | 84.84 |
| task_summation | 4560 | 13816 | 18376 | 20 | 0 | 5.86 | 117.21 |
| task_transcription | 3335 | 2595 | 5930 | 20 | 0 | 3.60 | 72.0 |
| task_sequences | 3241 | 6198 | 9439 | 19 | 1 | 3.45 | 68.97 |
| string_entry | 3707 | 5563 | 9270 | 9 | 11 | 4.31 | 86.17 |
| **TOTAL** | **32812** | **90889** | **123701** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 6 4 1 3 6 5 3 1 3 5 1 5 6 | 2 6 4 1 3 6 5 3 1 3 5 1 5 6 | Yes | 11.16 |
| 2 | 3 1 1 5 1 2 3 3 6 1 6 2 1 4 | 1 3 1 5 1 6 3 2 1 6 2 1 4 | No | 15.31 |
| 3 | 6 3 4 2 5 6 1 4 5 6 2 2 3 4 | 3 2 6 5 6 1 4 5 6 2 3 2 4 | No | 11.8 |
| 4 | 1 3 5 5 3 2 6 1 6 2 1 5 3 4 | 1 3 5 5 3 2 6 1 | No | 10.63 |
| 5 | 5 6 5 3 1 6 5 2 4 6 3 3 2 6 | 5 6 5 3 1 6 2 4 3 6 | No | 43.61 |
| 6 | 6 3 1 4 1 5 3 6 6 1 4 2 4 6 | 3 6 1 4 1 5 6 3 1 5 4 6 1 2 3 4 6 5 | No | 10.71 |
| 7 | 4 6 6 5 1 5 5 3 4 1 2 2 4 3 | 4 6 6 5 1 5 5 3 4 1 2 2 4 3 | Yes | 11.18 |
| 8 | 6 2 4 5 2 3 6 5 3 6 6 4 6 5 | 6 2 4 5 3 5 6 2 3 1 6 6 4 6 5 | No | 10.61 |
| 9 | 4 1 3 2 3 1 4 6 3 2 3 5 2 1 | 4 6 1 3 2 3 5 1 4 6 5 3 2 3 5 2 1 | No | 10.51 |
| 10 | 1 6 3 3 4 5 1 6 5 4 6 6 3 1 | 3 6 1 3 4 5 1 6 5 4 6 6 3 1 | No | 8.69 |
| 11 | 1 2 5 6 4 3 1 2 1 5 6 2 3 1 | 1 2 5 6 3 1 2 1 5 6 2 3 1 | No | 9.53 |
| 12 | 1 2 3 6 2 2 6 2 4 5 4 3 2 6 | 1 2 3 6 2 2 6 2 4 5 4 3 2 6 | Yes | 10.77 |
| 13 | 6 3 4 2 3 4 5 1 3 6 4 6 1 4 | 3 4 6 2 5 3 4 1 3 6 4 6 1 4 | No | 14.09 |
| 14 | 6 4 3 4 1 3 5 3 6 1 6 3 5 4 | 4 5 3 4 3 1 5 3 6 1 6 3 4 5 | No | 12.45 |
| 15 | 4 6 1 4 3 1 4 3 5 4 6 5 1 2 | 4 6 1 4 3 1 4 3 5 4 6 5 1 2 | Yes | 10.72 |
| 16 | 3 5 1 2 3 6 5 2 3 4 4 2 5 6 | 3 5 2 1 5 3 3 2 4 6 4 2 5 6 | No | 10.1 |
| 17 | 4 6 2 1 5 1 3 6 1 6 5 1 6 3 | 4 6 2 1 5 1 3 6 5 1 6 1 5 6 3 | No | 37.56 |
| 18 | 1 5 4 4 1 3 5 6 4 2 4 6 1 3 | 4 5 1 4 1 3 5 6 2 4 4 6 1 3 | No | 12.35 |
| 19 | 3 5 1 2 6 2 4 4 5 4 5 2 5 2 | 3 5 1 2 4 2 6 4 5 5 4 2 5 2 | No | 8.91 |
| 20 | 5 3 1 1 2 5 2 5 3 2 3 5 4 2 | 3 5 1 4 5 1 2 3 2 4 5 2 3 5 4 | No | 10.18 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 952 | 952 | Yes | 3.12 |
| 2 | 896 | 896 | Yes | 1.46 |
| 3 | 1644 | 1644 | Yes | 2.85 |
| 4 | 720 | 720 | Yes | 2.1 |
| 5 | 2457 | 2457 | Yes | 1.56 |
| 6 | 1102 | 1102 | Yes | 2.33 |
| 7 | 2325 | 2325 | Yes | 2.66 |
| 8 | 1229 | 1229 | Yes | 3.15 |
| 9 | 1615 | 1615 | Yes | 4.42 |
| 10 | 1529 | 1529 | Yes | 2.89 |
| 11 | 1839 | 1839 | Yes | 2.25 |
| 12 | 883 | 883 | Yes | 1.6 |
| 13 | 1477 | 1477 | Yes | 2.82 |
| 14 | 1739 | 1739 | Yes | 1.79 |
| 15 | 1871 | 1871 | Yes | 2.06 |
| 16 | 1829 | 1829 | Yes | 2.54 |
| 17 | 1575 | 1575 | Yes | 4.51 |
| 18 | 1395 | 1395 | Yes | 1.89 |
| 19 | 1370 | 1370 | Yes | 4.18 |
| 20 | 1844 | 1844 | Yes | 1.81 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 60 | No | 7.86 |
| 2 | 39 | 36 | No | 7.62 |
| 3 | 70 | 62 | No | 7.39 |
| 4 | 75 | 63 | No | 7.18 |
| 5 | 47 | 47 | Yes | 8.55 |
| 6 | 35 | 33 | No | 7.19 |
| 7 | 54 | 46 | No | 11.69 |
| 8 | 41 | 36 | No | 6.44 |
| 9 | 66 | 50 | No | 6.71 |
| 10 | 59 | 52 | No | 6.76 |
| 11 | 37 | 43 | No | 14.66 |
| 12 | 63 | 61 | No | 15.57 |
| 13 | 54 | 47 | No | 3.07 |
| 14 | 39 | 42 | No | 7.13 |
| 15 | 71 | 61 | No | 9.83 |
| 16 | 41 | 41 | Yes | 7.18 |
| 17 | 69 | 59 | No | 6.68 |
| 18 | 62 | 63 | No | 4.93 |
| 19 | 55 | 43 | No | 8.51 |
| 20 | 74 | 55 | No | 9.99 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FILGSDT | FILGSDT | Yes | 3.94 |
| 2 | TEVMXQD | TEVMXQD | Yes | 4.48 |
| 3 | VCHTBLX | VCHTBLX | Yes | 2.89 |
| 4 | WPYKQNF | WPYKQNF | Yes | 6.21 |
| 5 | IQUMXPT | IQUMXPT | Yes | 2.4 |
| 6 | FTQNGKW | FTQNGKW | Yes | 3.16 |
| 7 | AKUSOVY | AKUSOVY | Yes | 3.34 |
| 8 | YBIHMNV | YBIHMNV | Yes | 3.36 |
| 9 | MXZGBWU | MXZGBWU | Yes | 4.13 |
| 10 | UAFRTQI | UAFRTQI | Yes | 2.7 |
| 11 | VDSOLRX | VDSOLRX | Yes | 2.92 |
| 12 | DGKJSLF | DGKJSLF | Yes | 5.13 |
| 13 | ATOJHKX | ATOJHKX | Yes | 2.91 |
| 14 | QWKDJHP | QWKDJHP | Yes | 3.17 |
| 15 | GYCNJHS | GYCNJHS | Yes | 5.43 |
| 16 | PHKZTSN | PHKZTSN | Yes | 2.86 |
| 17 | VBUJLGO | VBUJLGO | Yes | 2.9 |
| 18 | JFHLQKG | JFHLQKG | Yes | 14.58 |
| 19 | FQHIXDV | FQHIXDV | Yes | 4.88 |
| 20 | PBNCALF | PBNCALF | Yes | 3.44 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.56 |
| 2 | [0.9, 9.1] | 0.9 9.1 | Yes | 4.45 |
| 3 | [0.1, 9.9] | 9.9 0.1 | Yes | 8.2 |
| 4 | [4.1, 5.9] | 4.1 5.9 | Yes | 6.21 |
| 5 | [0.5, 9.5] | 9.5 0.5 | Yes | 13.61 |
| 6 | [4.2, 5.8] | 4.2 5.8 | Yes | 8.46 |
| 7 | [0.8, 9.2] | 0.8 9.2 | Yes | 3.23 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 5.29 |
| 9 | [2.1, 7.9] | 2.1 7.9 | Yes | 4.97 |
| 10 | [0.7, 9.3] | 0.7 9.3 | Yes | 4.75 |
| 11 | [3.2, 6.8] | 6.8 3.2 | Yes | 6.46 |
| 12 | [2.4, 7.6] | 7.6 2.4 | Yes | 5.19 |
| 13 | [4.3, 5.7] | 4.3 5.7 | Yes | 4.91 |
| 14 | [2.2, 7.8] | 7.8 2.2 | Yes | 2.39 |
| 15 | [1.6, 8.4] | 1.6 8.4 | Yes | 5.96 |
| 16 | [0.1, 9.9] | 0.1 9.9 | Yes | 5.38 |
| 17 | [0.8, 9.2] | 9.2 0.8 | Yes | 4.77 |
| 18 | [1.7, 8.3] | 1.7 8.3 | Yes | 4.08 |
| 19 | [4.4, 5.6] | 5.6 4.4 | Yes | 8.14 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 6.17 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 163O84GXLE5A | 163O84GXLE5A | Yes | 2.49 |
| 2 | 8FHDITB7UXRI | 8FHDITB7UXRI | Yes | 2.02 |
| 3 | L7YSSDKQJ4ZW | L7YSSDKQJ4ZW | Yes | 2.37 |
| 4 | PQDGAZQM2UBU | PQDGAZQM2UBU | Yes | 3.02 |
| 5 | F6F8NDWV3QL6 | F6F8NDWV3QL6 | Yes | 4.11 |
| 6 | RKJVEWUJOKSN | RKJVEWUJOKSN | Yes | 2.38 |
| 7 | P07K5Y5RHOP3 | P07K5Y5RHOP3 | Yes | 2.34 |
| 8 | 122SPXVFYSDD | 122SPXVFYSDD | Yes | 3.1 |
| 9 | SAU0R907RNN2 | SAU0R907RNN2 | Yes | 2.82 |
| 10 | ZY2T0VAGQ9TQ | ZY2T0VAGQ9TQ | Yes | 2.65 |
| 11 | 220TKXIWITVM | 220TKXIWITVM | Yes | 4.52 |
| 12 | PV305SSO9K30 | PV305SSO9K30 | Yes | 1.84 |
| 13 | E6KA87BQUGNK | E6KA87BQUGNK | Yes | 2.38 |
| 14 | WOBQS5XGN26X | WOBQS5XGN26X | Yes | 4.06 |
| 15 | DMFURJP2OOE9 | DMFURJP2OOE9 | Yes | 9.71 |
| 16 | NOOS0AG4S8U7 | NOOS0AG4S8U7 | Yes | 9.38 |
| 17 | GY9OGE2IWWS6 | GY9OGE2IWWS6 | Yes | 4.01 |
| 18 | 4ETWY8TGU0CS | 4ETWY8TGU0CS | Yes | 2.75 |
| 19 | 1AAXA27XZ55L | 1AAXA27XZ55L | Yes | 3.65 |
| 20 | TR6QZEJLIYIL | TR6QZEJLIYIL | Yes | 2.39 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 2.49 |
| 2 | 7 | 7 | Yes | 2.65 |
| 3 | 6 | 6 | Yes | 2.56 |
| 4 | 3 | 3 | Yes | 3.24 |
| 5 | 36 | 36 | Yes | 2.33 |
| 6 | 60 | 60 | Yes | 4.65 |
| 7 | 1440 | 1440 | Yes | 4.2 |
| 8 | 65 | 65 | Yes | 2.46 |
| 9 | 1 | 1 | Yes | 3.66 |
| 10 | 7680 | 7680 | Yes | 2.78 |
| 11 | 20 | 20 | Yes | 5.42 |
| 12 | 5 | 5 | Yes | 4.79 |
| 13 | 44 | 44 | Yes | 3.26 |
| 14 | 198 | 198 | Yes | 2.75 |
| 15 | 60 | 60 | Yes | 2.74 |
| 16 | 31 | 31 | Yes | 2.92 |
| 17 | 67 | 67 | Yes | 3.26 |
| 18 | 39 | 39 | Yes | 2.22 |
| 19 | 4096 | 1048576 | No | 6.01 |
| 20 | 10 | 10 | Yes | 4.58 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )<<//< \( | )<<//<\( | No | 11.41 |
| 2 | <\ __(/(  | <\ __(/( | No | 4.96 |
| 3 | )<<\/_ (_ | )<<\/_ (_ | Yes | 2.71 |
| 4 | (<(< <))\ | (<(< <))\ | Yes | 2.44 |
| 5 | (<<\/)_\_ | (<<\/)_\_ | Yes | 5.83 |
| 6 | )/_)\_) < | )/_)\_) | No | 2.48 |
| 7 | _(() <<)\ | _() <<)\ | No | 2.97 |
| 8 | _))_\_(<_ | _))_\_(<_ | Yes | 5.59 |
| 9 |  ) )<)_ ) | ) )<)_ ) | No | 3.5 |
| 10 | / \<(</\  | / \<(</ \ | No | 3.89 |
| 11 | )(/<_()_  | )(/<_()_ | No | 2.11 |
| 12 | <\)/  \() | <\)/  \() | Yes | 5.55 |
| 13 | <( _(//(  | <( _(//( | No | 2.53 |
| 14 | _)/(\\()< | _)/(\\() | No | 8.77 |
| 15 | \_\< /\// | \_\< /\// | Yes | 3.67 |
| 16 | )/_/ __<) | )/_/ __<) | Yes | 1.83 |
| 17 | \_\)()//\ | /\) <(_<) | No | 4.76 |
| 18 | <<</)  () | <<</)  () | Yes | 2.48 |
| 19 | /\ /)\ )_ | /\ /)\ )_ | Yes | 4.08 |
| 20 | )<< </<\) | )<<  </<\) | No | 4.6 |
