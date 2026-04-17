# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-27 10:12:36

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
| sudoku_game | 5118 | 35048 | 40166 | 8 | 12 | 35.25 | 705.06 |
| add_numbers | 2900 | 897 | 3797 | 20 | 0 | 3.27 | 65.49 |
| counting_zeros | 4300 | 23489 | 27789 | 17 | 3 | 17.12 | 342.37 |
| task_decoding | 4240 | 3132 | 7372 | 19 | 1 | 5.35 | 106.92 |
| task_summation | 4580 | 6184 | 10764 | 20 | 0 | 5.74 | 114.75 |
| task_transcription | 3048 | 1797 | 4845 | 20 | 0 | 2.96 | 59.26 |
| task_sequences | 2900 | 7573 | 10473 | 20 | 0 | 7.62 | 152.52 |
| string_entry | 3340 | 26397 | 29737 | 1 | 19 | 13.06 | 261.13 |
| **TOTAL** | **30426** | **104517** | **134943** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 2 1 3 4 6 5 6 2 1 4 5 1 3 |  | No | 5.61 |
| 2 | 3 6 2 3 6 4 5 6 1 4 3 6 2 3 |  | No | 52.58 |
| 3 | 4 6 2 6 2 4 3 5 6 3 2 5 2 6 | 4 6 2 6 2 4 3 5 6 3 2 5 2 6 | Yes | 24.88 |
| 4 | 6 1 4 3 2 6 2 1 4 1 4 3 2 4 |  | No | 48.14 |
| 5 | 3 2 5 4 4 1 3 2 1 6 3 2 3 1 |  | No | 55.08 |
| 6 | 6 2 5 2 3 5 4 2 5 2 6 4 1 5 |  | No | 51.81 |
| 7 | 5 2 6 1 1 6 2 2 3 5 4 4 6 2 |  | No | 60.91 |
| 8 | 6 5 2 5 4 2 3 4 5 6 6 5 6 5 | 6 5 2 5 4 2 3 4 5 6 6 5 6 5 | Yes | 16.7 |
| 9 | 3 3 5 1 3 2 4 3 5 2 1 1 5 6 | 3 3 5 1 3 2 4 3 5 2 1 1 5 6 | Yes | 27.28 |
| 10 | 6 4 5 2 3 5 4 1 4 3 3 1 6 5 | 6 4 5 2 3 5 4 1 4 3 3 1 6 5 | Yes | 21.75 |
| 11 | 3 5 2 2 1 3 6 1 3 1 6 5 6 4 | 3 5 2 2 1 3 6 1 3 1 6 5 6 4 | Yes | 22.73 |
| 12 | 4 6 2 1 5 4 5 3 4 2 3 4 2 1 |  | No | 57.52 |
| 13 | 6 2 3 4 2 1 6 2 5 1 6 3 2 4 |  | No | 43.61 |
| 14 | 3 5 1 4 5 5 2 3 4 3 6 3 2 1 |  | No | 51.73 |
| 15 | 2 3 4 4 1 5 1 4 4 2 5 1 4 6 | 2 3 4 4 1 5 1 4 4 2 5 1 4 6 | Yes | 8.74 |
| 16 | 5 3 6 1 2 5 3 3 5 4 6 4 1 2 |  | No | 39.58 |
| 17 | 1 2 2 1 4 6 1 2 5 1 6 3 5 1 | 1 2 2 1 4 6 1 2 5 1 6 3 5 1 | Yes | 23.3 |
| 18 | 1 6 6 1 3 4 2 6 1 3 4 1 4 6 |  | No | 33.7 |
| 19 | 5 6 4 2 1 5 3 3 6 2 6 5 3 2 | 5 6 4 2 1 5 3 3 6 2 6 5 3 2 | Yes | 18.85 |
| 20 | 6 1 4 3 6 3 4 6 5 3 5 6 1 4 |  | No | 40.51 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1119 | 1119 | Yes | 3.95 |
| 2 | 1837 | 1837 | Yes | 3.29 |
| 3 | 1532 | 1532 | Yes | 3.75 |
| 4 | 1358 | 1358 | Yes | 4.86 |
| 5 | 983 | 983 | Yes | 4.45 |
| 6 | 1642 | 1642 | Yes | 3.55 |
| 7 | 1707 | 1707 | Yes | 3.77 |
| 8 | 1524 | 1524 | Yes | 3.31 |
| 9 | 1108 | 1108 | Yes | 2.76 |
| 10 | 1794 | 1794 | Yes | 2.48 |
| 11 | 1799 | 1799 | Yes | 3.45 |
| 12 | 1231 | 1231 | Yes | 1.26 |
| 13 | 2239 | 2239 | Yes | 3.4 |
| 14 | 1577 | 1577 | Yes | 3.09 |
| 15 | 2499 | 2499 | Yes | 2.99 |
| 16 | 1477 | 1477 | Yes | 3.03 |
| 17 | 1229 | 1229 | Yes | 3.58 |
| 18 | 1738 | 1738 | Yes | 2.25 |
| 19 | 1846 | 1846 | Yes | 2.84 |
| 20 | 1424 | 1424 | Yes | 3.43 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 68 | 67 | No | 13.23 |
| 2 | 57 | 57 | Yes | 14.37 |
| 3 | 41 | 41 | Yes | 23.17 |
| 4 | 42 | 42 | Yes | 24.33 |
| 5 | 69 | 69 | Yes | 15.21 |
| 6 | 71 |  | No | 37.33 |
| 7 | 35 | 35 | Yes | 16.22 |
| 8 | 37 | 38 | No | 13.71 |
| 9 | 74 | 74 | Yes | 14.08 |
| 10 | 68 | 68 | Yes | 18.71 |
| 11 | 48 | 48 | Yes | 15.6 |
| 12 | 44 | 44 | Yes | 18.84 |
| 13 | 47 | 47 | Yes | 14.28 |
| 14 | 39 | 39 | Yes | 13.96 |
| 15 | 51 | 51 | Yes | 10.68 |
| 16 | 67 | 67 | Yes | 10.16 |
| 17 | 47 | 47 | Yes | 10.97 |
| 18 | 68 | 68 | Yes | 22.97 |
| 19 | 42 | 42 | Yes | 14.99 |
| 20 | 75 | 75 | Yes | 19.53 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VZHQRPM | VZHQRPM | Yes | 11.0 |
| 2 | KQINPJM | KQINPJM | Yes | 4.56 |
| 3 | CXEYRGT | CXEYRGT | Yes | 5.52 |
| 4 | TMIYLHU | TMIYLHU | Yes | 5.23 |
| 5 | KBVNUJO | KBVNUJO | Yes | 5.41 |
| 6 | CJHZQFP | CJHZQFP | Yes | 2.0 |
| 7 | RCJHWTA | RCJHWTA | Yes | 5.4 |
| 8 | THORPZA | THORPZA | Yes | 5.32 |
| 9 | EDJIKBM | EDJIKBM | Yes | 4.81 |
| 10 | BJRPYAL | BJR PYAL | No | 6.8 |
| 11 | AIBDEJW | AIBDEJW | Yes | 4.08 |
| 12 | ASDWRZX | ASDWRZX | Yes | 5.13 |
| 13 | WGFMYKP | WGFMYKP | Yes | 5.86 |
| 14 | DIKWSJV | DIKWSJV | Yes | 6.77 |
| 15 | MXPTRGE | MXPTRGE | Yes | 5.46 |
| 16 | FQICMDG | FQICMDG | Yes | 5.29 |
| 17 | MZRPSDL | MZRPSDL | Yes | 3.02 |
| 18 | BHNYKUE | BHNYKUE | Yes | 4.49 |
| 19 | FYUPGQL | FYUPGQL | Yes | 6.0 |
| 20 | DLVJPFU | DLVJPFU | Yes | 4.78 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.8, 5.2] | 4.8 5.2 | Yes | 4.52 |
| 2 | [4.0, 6.0] | 4.0 6.0 | Yes | 4.5 |
| 3 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.46 |
| 4 | [3.6, 6.4] | 6.4 3.6 | Yes | 6.04 |
| 5 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.12 |
| 6 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.88 |
| 7 | [4.7, 5.3] | 5.3 4.7 | Yes | 5.82 |
| 8 | [4.8, 5.2] | 5.2 4.8 | Yes | 6.43 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 8.28 |
| 10 | [3.1, 6.9] | 3.1 6.9 | Yes | 4.65 |
| 11 | [1.1, 8.9] | 1.1 8.9 | Yes | 6.04 |
| 12 | [2.5, 7.5] | 2.5 7.5 | Yes | 5.95 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 5.23 |
| 14 | [3.9, 6.1] | 3.9 6.1 | Yes | 4.82 |
| 15 | [4.9, 5.1] | 4.9 5.1 | Yes | 5.84 |
| 16 | [1.0, 9.0] | 1.0 9.0 | Yes | 5.26 |
| 17 | [1.1, 8.9] | 8.9 1.1 | Yes | 5.09 |
| 18 | [1.9, 8.1] | 8.1 1.9 | Yes | 5.69 |
| 19 | [3.2, 6.8] | 3.2 6.8 | Yes | 6.49 |
| 20 | [3.9, 6.1] | 3.9 6.1 | Yes | 5.62 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZPSX31WVVDPY | ZPSX31WVVDPY | Yes | 1.3 |
| 2 | YZ0DG41CL4TI | YZ0DG41CL4TI | Yes | 2.27 |
| 3 | N2YQGLF805YH | N2YQGLF805YH | Yes | 2.72 |
| 4 | E9R60HG3C6JL | E9R60HG3C6JL | Yes | 5.49 |
| 5 | JKEM7FV3YJGY | JKEM7FV3YJGY | Yes | 1.35 |
| 6 | KU7KIM4M2UT8 | KU7KIM4M2UT8 | Yes | 0.8 |
| 7 | YBNC6C0OSEDH | YBNC6C0OSEDH | Yes | 4.94 |
| 8 | AESL60AHA2DB | AESL60AHA2DB | Yes | 2.21 |
| 9 | 0JWMIGKCMAJ3 | 0JWMIGKCMAJ3 | Yes | 0.73 |
| 10 | C11BIOB2H1OP | C11BIOB2H1OP | Yes | 0.87 |
| 11 | JMUUBV5BH8O6 | JMUUBV5BH8O6 | Yes | 0.84 |
| 12 | 3EO0GLIXC9A8 | 3EO0GLIXC9A8 | Yes | 3.06 |
| 13 | V0WY0U1FVZ9Q | V0WY0U1FVZ9Q | Yes | 8.28 |
| 14 | P3OA63OADLF2 | P3OA63OADLF2 | Yes | 5.01 |
| 15 | 80EBXYO1RXIN | 80EBXYO1RXIN | Yes | 4.04 |
| 16 | 1J676B2A4T85 | 1J676B2A4T85 | Yes | 2.41 |
| 17 | 5K3OUKG0FXYR | 5K3OUKG0FXYR | Yes | 1.82 |
| 18 | 6LZE16EP0Q4K | 6LZE16EP0Q4K | Yes | 1.84 |
| 19 | V7CX2LO0V8T0 | V7CX2LO0V8T0 | Yes | 3.7 |
| 20 | E3GHLO2Z209V | E3GHLO2Z209V | Yes | 5.56 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 73 | 73 | Yes | 5.54 |
| 2 | 23 | 23 | Yes | 17.67 |
| 3 | 26 | 26 | Yes | 16.07 |
| 4 | 1 | 1 | Yes | 8.25 |
| 5 | 16 | 16 | Yes | 5.55 |
| 6 | 198 | 198 | Yes | 7.68 |
| 7 | 63 | 63 | Yes | 3.13 |
| 8 | 64 | 64 | Yes | 5.7 |
| 9 | 48 | 48 | Yes | 9.67 |
| 10 | 60 | 60 | Yes | 11.07 |
| 11 | 39 | 39 | Yes | 7.43 |
| 12 | 5 | 5 | Yes | 6.95 |
| 13 | 793 | 793 | Yes | 4.98 |
| 14 | 28 | 28 | Yes | 11.14 |
| 15 | 1440 | 1440 | Yes | 4.95 |
| 16 | 7 | 7 | Yes | 4.65 |
| 17 | 60 | 60 | Yes | 4.89 |
| 18 | 6 | 6 | Yes | 4.59 |
| 19 | 65 | 65 | Yes | 6.51 |
| 20 | 44 | 44 | Yes | 6.06 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( /_<))(< | /\) <(_<)( /_<))(< | No | 16.22 |
| 2 | <_()_\ /_ | /\) <(_<) | No | 12.53 |
| 3 | <)((__ )) | /\) <(_<)<)((__ )) | No | 16.16 |
| 4 | _(/<_(<(  | _(/<_(<( | No | 16.92 |
| 5 | )\<<__/ _ | /\) <(_<) | No | 14.12 |
| 6 | )(/)/ __  | /\) <(_<) | No | 6.22 |
| 7 | )_/\/< <( | /\) <(_<))_/\/< <( | No | 7.77 |
| 8 |  / (_ ) \ |  | No | 40.29 |
| 9 | //(< (/_\ | //(< (/_\ | Yes | 4.22 |
| 10 | (\) ))(/_ |  | No | 17.64 |
| 11 | /)\_)<)\) | /\) <(_< | No | 9.71 |
| 12 | )_)/_<( _ | /\) <(_<) | No | 6.75 |
| 13 | <\_<</ () | /\) <(_<) | No | 16.37 |
| 14 |  /_ (/<// | /\) <(_<) /_ (/<// | No | 6.41 |
| 15 | _ )_/(_ ( | /\) <(_<)_ )_/(_ ( | No | 9.72 |
| 16 | ___< /)(_ | /\) <(_<)___< /()_ | No | 13.09 |
| 17 |  /(< __<) | /\) <(_<) | No | 6.85 |
| 18 | (/)__</ ) | /\) <(_<) | No | 5.33 |
| 19 | \\_)_ <(\ |  | No | 19.21 |
| 20 | \<__)\\ / | /\) <(_<)\<__)\\ / | No | 15.59 |
