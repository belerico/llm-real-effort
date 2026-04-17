# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-27 09:54:47

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
| sudoku_game | 6122 | 30664 | 36786 | 2 | 18 | 10.67 | 213.41 |
| add_numbers | 3500 | 3260 | 6760 | 20 | 0 | 2.14 | 42.8 |
| counting_zeros | 4820 | 20062 | 24882 | 0 | 20 | 6.63 | 132.54 |
| task_decoding | 4820 | 7282 | 12102 | 20 | 0 | 3.69 | 73.72 |
| task_summation | 4880 | 14998 | 19878 | 20 | 0 | 5.54 | 110.9 |
| task_transcription | 3668 | 1992 | 5660 | 20 | 0 | 2.35 | 47.08 |
| task_sequences | 3561 | 6281 | 9842 | 19 | 1 | 3.92 | 78.47 |
| string_entry | 4021 | 4877 | 8898 | 8 | 12 | 2.75 | 54.98 |
| **TOTAL** | **35392** | **89416** | **124808** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 3 4 6 3 2 1 3 6 3 5 6 3 | 4 1 4 3 6 3 2 1 3 6 3 5 6 3 | No | 11.09 |
| 2 | 1 5 4 5 6 3 5 6 4 4 2 6 1 4 | 5 5 1 5 6 6 4 5 3 4 2 1 6 4 | No | 9.24 |
| 3 | 2 1 6 3 5 5 1 5 3 4 5 4 5 1 | 2 1 6 3 5 5 1 5 4 5 3 1 4 5 | No | 8.23 |
| 4 | 3 1 4 2 1 1 5 6 3 5 5 4 3 1 | 3 1 4 1 2 5 6 1 3 5 1 4 3 1 | No | 27.96 |
| 5 | 3 5 2 6 2 6 4 2 2 5 3 6 4 2 | 5 3 2 6 2 2 4 6 2 3 3 5 6 2 | No | 9.61 |
| 6 | 1 2 1 2 5 3 2 5 6 1 3 4 1 5 | 1 2 1 2 5 3 2 5 6 1 3 4 4 1 5 | No | 7.8 |
| 7 | 4 6 4 1 5 3 5 4 4 2 2 1 1 2 | 4 6 1 4 5 3 4 5 2 4 2 1 1 2 | No | 9.97 |
| 8 | 5 3 2 6 2 1 3 5 4 1 3 2 4 2 | 5 3 2 6 2 1 3 5 4 1 3 2 4 2 | Yes | 13.58 |
| 9 | 3 4 5 6 5 6 3 1 4 2 3 4 6 1 | 3 4 5 6 5 6 1 2 6 3 1 4 | No | 10.68 |
| 10 | 2 5 2 3 5 5 4 2 3 4 1 5 2 4 | 2 5 1 3 2 4 5 2 3 5 4 2** | No | 11.96 |
| 11 | 3 2 5 1 1 3 6 2 1 4 6 6 5 2 | 3 1 5 2 6 3 1 5 2 4 6 1 6 | No | 9.56 |
| 12 | 2 6 1 3 4 6 6 5 3 2 4 2 6 1 | 2 6 1 3 6 4 6 5 3 2 4 2 6 1 | No | 11.89 |
| 13 | 6 5 5 6 4 2 1 5 4 5 3 4 6 5 | 5 6 5 6 2 4 1 4 5 5 3 4 6 5** | No | 10.35 |
| 14 | 3 1 5 2 4 6 3 5 5 6 1 1 4 2 | 3 4 5 1 2 5 6 3 5 6 1 1 4 2** | No | 7.58 |
| 15 | 1 6 3 4 5 6 2 6 4 2 1 1 5 3 | 3 6 1 4 2 3 6 4 2 1 5 3 | No | 8.73 |
| 16 | 3 1 1 4 2 2 6 3 5 4 3 6 1 6 | 1 3 4 2 1 2 6 3 5 1 4 6 1 6 | No | 9.44 |
| 17 | 3 5 6 2 6 5 1 3 1 4 6 2 5 2 | 3 5 6 2 1 6 5 1 3 5 4 6 2 2 | No | 7.66 |
| 18 | 4 1 1 5 2 4 3 2 1 2 5 3 1 6 | 4 1 1 5 2 4 3 2 1 2 5 3 1 6 | Yes | 9.39 |
| 19 | 1 6 4 1 3 4 6 3 5 6 6 3 3 1 | 1 6 1 3 4 4 6 3 5 6 6 3 3 1** | No | 8.67 |
| 20 | 5 3 6 4 3 6 6 3 2 4 5 3 2 6 | 5 3 4 6 3 3 1 6 2 4 5 | No | 9.99 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1331 | 1331 | Yes | 2.26 |
| 2 | 1619 | 1619 | Yes | 2.05 |
| 3 | 1111 | 1111 | Yes | 1.49 |
| 4 | 2183 | 2183 | Yes | 2.59 |
| 5 | 2016 | 2016 | Yes | 2.57 |
| 6 | 961 | 961 | Yes | 2.41 |
| 7 | 969 | 969 | Yes | 1.79 |
| 8 | 2253 | 2253 | Yes | 2.2 |
| 9 | 2382 | 2382 | Yes | 2.96 |
| 10 | 1570 | 1570 | Yes | 1.84 |
| 11 | 1277 | 1277 | Yes | 2.26 |
| 12 | 1204 | 1204 | Yes | 2.93 |
| 13 | 1336 | 1336 | Yes | 1.7 |
| 14 | 1704 | 1704 | Yes | 2.42 |
| 15 | 1883 | 1883 | Yes | 1.93 |
| 16 | 1285 | 1285 | Yes | 2.15 |
| 17 | 1628 | 1628 | Yes | 2.18 |
| 18 | 1960 | 1960 | Yes | 1.34 |
| 19 | 1487 | 1487 | Yes | 2.11 |
| 20 | 1010 | 1010 | Yes | 1.61 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 44 | 39 | No | 5.73 |
| 2 | 58 | 49 | No | 6.22 |
| 3 | 74 | 58 | No | 9.63 |
| 4 | 58 | 53 | No | 7.07 |
| 5 | 60 | 54 | No | 5.93 |
| 6 | 55 | 47 | No | 5.27 |
| 7 | 63 | 48 | No | 6.68 |
| 8 | 58 | 55 | No | 9.93 |
| 9 | 55 | 45 | No | 8.4 |
| 10 | 41 | 36 | No | 3.49 |
| 11 | 54 | 47 | No | 4.04 |
| 12 | 52 | 48 | No | 6.36 |
| 13 | 69 | 65 | No | 9.31 |
| 14 | 69 | 62 | No | 6.27 |
| 15 | 51 | 44 | No | 7.82 |
| 16 | 69 | 70 | No | 6.22 |
| 17 | 44 | 41 | No | 5.44 |
| 18 | 57 | 55 | No | 6.44 |
| 19 | 73 | 67 | No | 4.52 |
| 20 | 41 | 36 | No | 7.77 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GXDLENC | GXDLENC | Yes | 2.62 |
| 2 | CBTXGIW | CBTXGIW | Yes | 3.07 |
| 3 | BPNYEAV | BPNYEAV | Yes | 2.46 |
| 4 | LISAKXT | LISAKXT | Yes | 2.74 |
| 5 | PDCYJTZ | PDCYJTZ | Yes | 2.63 |
| 6 | FOTBCDS | FOTBCDS | Yes | 4.23 |
| 7 | RPUZBOW | RPUZBOW | Yes | 2.52 |
| 8 | ZHIRWOJ | ZHIRWOJ | Yes | 2.65 |
| 9 | WJAXSPB | WJAXSPB | Yes | 3.31 |
| 10 | OXVNGTD | OXVNGTD | Yes | 2.45 |
| 11 | MCOFGXA | MCOFGXA | Yes | 2.83 |
| 12 | AKPQFNV | AKPQFNV | Yes | 2.72 |
| 13 | QXKIYPH | QXKIYPH | Yes | 2.63 |
| 14 | LBWFMIJ | LBWFMIJ | Yes | 2.93 |
| 15 | METHNBX | METHNBX | Yes | 4.3 |
| 16 | XHZYDUO | XHZYDUO | Yes | 2.64 |
| 17 | VPXTYJD | VPXTYJD | Yes | 2.45 |
| 18 | IGNUJSA | IGNUJSA | Yes | 7.24 |
| 19 | EIKFNMS | EIKFNMS | Yes | 13.57 |
| 20 | PHOKSGT | PHOKSGT | Yes | 3.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.1, 7.9] | 7.9 2.1 | Yes | 5.09 |
| 2 | [1.8, 8.2] | 1.8 8.2 | Yes | 5.13 |
| 3 | [4.3, 5.7] | 4.3 5.7 | Yes | 4.88 |
| 4 | [0.4, 9.6] | 0.4 9.6 | Yes | 6.46 |
| 5 | [1.2, 8.8] | 8.8 1.2 | Yes | 4.93 |
| 6 | [2.4, 7.6] | 2.4 7.6 | Yes | 4.78 |
| 7 | [0.3, 9.7] | 9.7 0.3 | Yes | 4.63 |
| 8 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.53 |
| 9 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.29 |
| 10 | [3.0, 7.0] | 3.0 7.0 | Yes | 6.41 |
| 11 | [1.8, 8.2] | 1.8 8.2 | Yes | 7.75 |
| 12 | [3.4, 6.6] | 6.6 3.4 | Yes | 5.55 |
| 13 | [1.8, 8.2] | 1.8 8.2 | Yes | 8.22 |
| 14 | [1.3, 8.7] | 1.3 8.7 | Yes | 4.97 |
| 15 | [3.7, 6.3] | 3.7 6.3 | Yes | 4.5 |
| 16 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.06 |
| 17 | [2.2, 7.8] | 2.2 7.8 | Yes | 5.49 |
| 18 | [1.9, 8.1] | 8.1 1.9 | Yes | 5.05 |
| 19 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.53 |
| 20 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.63 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | E6A3RYD230KB | E6A3RYD230KB | Yes | 4.36 |
| 2 | HM4KZRNPG6MA | HM4KZRNPG6MA | Yes | 2.05 |
| 3 | KCMS9CGL76Q2 | KCMS9CGL76Q2 | Yes | 1.63 |
| 4 | IUCM0IND14NS | IUCM0IND14NS | Yes | 2.31 |
| 5 | HK0XMPY9NGD5 | HK0XMPY9NGD5 | Yes | 3.93 |
| 6 | MN7DKU3GD1SC | MN7DKU3GD1SC | Yes | 2.12 |
| 7 | FX0HV5TUHBR6 | FX0HV5TUHBR6 | Yes | 2.15 |
| 8 | SCN8D1XWPMFY | SCN8D1XWPMFY | Yes | 3.1 |
| 9 | 8KCY4XU0EC4J | 8KCY4XU0EC4J | Yes | 1.87 |
| 10 | D7RX1XNB3X41 | D7RX1XNB3X41 | Yes | 2.1 |
| 11 | O1LMH0CM64HX | O1LMH0CM64HX | Yes | 1.69 |
| 12 | 9YNAD6CQBFLA | 9YNAD6CQBFLA | Yes | 1.51 |
| 13 | M5C9K68OLZFH | M5C9K68OLZFH | Yes | 1.99 |
| 14 | 5YXF72RP1Q0G | 5YXF72RP1Q0G | Yes | 1.51 |
| 15 | RE6GTRVZIAQR | RE6GTRVZIAQR | Yes | 1.66 |
| 16 | B3PF2Y3TVAQ9 | B3PF2Y3TVAQ9 | Yes | 1.71 |
| 17 | XN2BA9PYFKXF | XN2BA9PYFKXF | Yes | 5.92 |
| 18 | SKZBTG2YFV8O | SKZBTG2YFV8O | Yes | 1.8 |
| 19 | YCKS1PVRBCNA | YCKS1PVRBCNA | Yes | 1.37 |
| 20 | DD9OK20PNOD5 | DD9OK20PNOD5 | Yes | 2.29 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 42 | No | 7.7 |
| 2 | 23 | 23 | Yes | 2.44 |
| 3 | 60 | 60 | Yes | 2.31 |
| 4 | 44 | 44 | Yes | 3.12 |
| 5 | 3 | 3 | Yes | 3.74 |
| 6 | 65 | 65 | Yes | 2.27 |
| 7 | 26 | 26 | Yes | 14.05 |
| 8 | 39 | 39 | Yes | 2.64 |
| 9 | 28 | 28 | Yes | 2.29 |
| 10 | 48 | 48 | Yes | 1.91 |
| 11 | 64 | 64 | Yes | 2.06 |
| 12 | 36 | 36 | Yes | 1.95 |
| 13 | 19 | 19 | Yes | 2.98 |
| 14 | 63 | 63 | Yes | 12.23 |
| 15 | 60 | 60 | Yes | 1.88 |
| 16 | 243 | 243 | Yes | 1.93 |
| 17 | 7680 | 7680 | Yes | 2.32 |
| 18 | 4096 | 4096 | Yes | 6.12 |
| 19 | 31 | 31 | Yes | 1.72 |
| 20 | 9 | 9 | Yes | 2.82 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /\(<<\ (< | /\(<<\ ( | No | 2.12 |
| 2 | <(<\<(< _ | <(<\<(< _ | Yes | 2.51 |
| 3 | ))_) <<__ | ))_) <<__ | Yes | 1.45 |
| 4 |  <_<(\)\) | <_<(\)\) | No | 2.34 |
| 5 | (()(() \\ | (()()( \\ | No | 4.0 |
| 6 | <))\/ \)< | <))\/ \) | No | 3.66 |
| 7 | ( \( _<(< | ( \( _<( | No | 2.65 |
| 8 | \< (/_()/ | \< (/_()/ | Yes | 2.5 |
| 9 | )/\ (<)/) | )/\ (<)/) | Yes | 2.2 |
| 10 | )/_))_)_) | )/_))_)_) | Yes | 3.11 |
| 11 | <_</)((_/ | /\) <(_<) | No | 4.31 |
| 12 | <))_<\))< | <))_<\)) | No | 3.1 |
| 13 | (\)(/\\ \ | (\)(/\\ \ | Yes | 2.27 |
| 14 | _<( \\  ) | _<( \  )) | No | 2.69 |
| 15 | _<(_<(__  | _<(_<(__ | No | 1.92 |
| 16 | \\<\ )\</ | \\<\ )\</ | Yes | 2.27 |
| 17 | (_(/\_  < | (_(/\_ | No | 2.53 |
| 18 |  \ \\)_)) | \ \\)_)) | No | 2.78 |
| 19 | /\/)_)\)( | /\/)_)\)( | Yes | 2.03 |
| 20 | )(< /< )) | )(<​ /<​ ))) | No | 4.52 |
