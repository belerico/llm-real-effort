# Benchmark Report — gemini-2.5-flash-lite

- **Model**: `google/gemini-2.5-flash-lite`
- **Date**: 2026-03-26 10:30:39

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
| sudoku_game | 8900 | 31539 | 40439 | 0 | 20 | 14.02 | 280.58 |
| add_numbers | 38880 | 3163 | 42043 | 20 | 0 | 2.40 | 48.0 |
| counting_zeros | 27570 | 32074 | 59644 | 7 | 13 | 7.27 | 145.64 |
| task_decoding | 49680 | 16173 | 65853 | 16 | 4 | 4.86 | 97.3 |
| task_summation | 28880 | 26568 | 55448 | 18 | 2 | 6.23 | 124.72 |
| task_transcription | 28600 | 3876 | 32476 | 12 | 8 | 2.53 | 50.66 |
| task_sequences | 3002 | 8874 | 11876 | 20 | 0 | 2.60 | 51.92 |
| string_entry | 34160 | 24526 | 58686 | 0 | 20 | 6.76 | 135.31 |
| **TOTAL** | **219672** | **146793** | **366465** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 6 2 6 2 4 3 1 3 5 2 4 3 | 5 6 3 4 2 1 | No | 6.3 |
| 2 | 4 1 3 2 5 3 2 6 2 2 6 1 5 2 | 1 3 4 2 6 5 2 4 6 3 1 5 3 2 5 6 4 1 6 5 1 2 3 4 4 6 3 1 5 2 5 1 2 4 6 3 | No | 5.74 |
| 3 | 1 6 1 4 1 2 5 3 2 6 4 5 2 1 | 1 6 4 2 5 3 5 4 2 3 1 6 3 1 5 2 6 4 4 2 6 5 3 1 2 3 1 6 4 5 6 5 4 1 2 3 | No | 5.68 |
| 4 | 1 2 2 6 5 1 1 2 5 1 4 3 5 1 | 1 2 6 2 1 4 5 3 1 4 5 2 3 1 2 6 5 4 6 5 4 1 3 2 | No | 12.21 |
| 5 | 6 2 5 4 5 5 4 1 2 3 5 1 6 3 | 2 4 5 6 3 1 5 3 4 1 6 2 1 6 3 5 2 4 6 2 1 3 4 5 4 5 2 1 6 3 | No | 29.08 |
| 6 | 6 5 4 4 2 6 4 2 3 6 1 5 3 6 | 4 5 6 3 2 1 3 4 2 6 5 1 5 1 3 4 6 2 4 6 1 5 3 2 2 3 5 1 4 6 6 2 4 3 1 5 | No | 7.09 |
| 7 | 4 3 6 1 4 1 3 5 6 4 4 2 1 6 | The provided Sudoku puzzle contains an error, as column 4 has two '3's (at R3C4 and R5C4), violating the Sudoku rules. Therefore, the puzzle is unsolvable as presented. However, if we assume there was a typo and R5C4 should be a '6' instead of a '3', the puzzle becomes solvable.  Assuming R5C4 is '6' (instead of '3'): The grid becomes: [3, 1, 6, 4, 2, 5] [ , 2, 1, 5, 6,  ] [5,  ,  , 3, 2,  ] [ ,  ,  ,  ,  , 2] [6,  ,  , 6, 5, 1]  <- Changed R5C4 from 3 to 6 [2, 5, 4,  ,  , 3]  Let's solve this modified puzzle:  1.  **R2**: Missing 3, 4.     *   C1: Has 3, 5, 6, 2. Missing 1, 4.     *   C6: Has 5, 2, 1, 3. Missing 4, 6.     *   Box 1 (R1-2, C1-3): Contains 3, 1, 6, 2, 1. Missing 4, 5.     *   Box 2 (R1-2, C4-6): Contains 4, 2, 5, 5, 6. Missing 1, 3.     *   R2C1 must be 4 (cannot be 3 due to R3C1=5, R4C1=?, R5C1=6, R6C1=2, R1C1=3. C1 missing 1,4. Box 1 missing 4,5. R2C1 cannot be 5. So R2C1 must be 4).     *   R2C6 must be 3 (C6 missing 4,6. Box 2 missing 1,3. R2C6 cannot be 4. So R2C6 must be 3).     *   Grid is now:         [3, 1, 6, 4, 2, 5]         [4, 2, 1, 5, 6, 3]         [5,  ,  , 3, 2,  ]         [ ,  ,  ,  ,  , 2]         [6,  ,  , 6, 5, 1] | No | 11.03 |
| 8 | 3 4 6 2 2 4 4 6 5 5 1 6 3 2 | 4 6 3 1 2 5 2 3 1 4 6 5 5 1 4 6 3 2 6 2 5 3 1 4 4 5 6 2 1 3 3 1 2 5 4 6 | No | 6.57 |
| 9 | 4 2 6 6 1 6 5 5 1 4 2 6 4 1 | 4 6 2 1 5 6 1 5 4 2 1 5 4 2 1 6 4 2 | No | 5.68 |
| 10 | 3 6 4 1 4 2 5 3 4 1 2 4 5 6 | 4 3 6 1 2 5 1 4 2 3 6 5 3 1 5 4 2 6 6 2 3 5 1 4 4 5 6 2 3 1 | No | 9.61 |
| 11 | 4 3 1 6 4 5 1 4 6 2 1 1 6 3 | 4 3 6 1 5 1 4 6 1 2 3 4 4 6 3 1 | No | 115.06 |
| 12 | 3 2 6 4 2 6 6 2 3 2 1 3 4 5 | 2 6 3 4 1 5 3 2 5 6 4 1 6 1 4 2 3 5 5 4 6 3 1 2 3 5 1 6 2 4 4 2 3 5 6 1 | No | 5.83 |
| 13 | 6 3 4 2 3 4 5 1 6 5 1 6 2 1 | 6 3 4 3 4 1 5 2 6 2 5 1 4 2 3 1 | No | 7.93 |
| 14 | 5 6 3 1 3 1 3 5 6 2 6 5 2 4 | 5 3 6 1 3 5 1 4 2 4 1 2 6 | No | 6.46 |
| 15 | 2 6 4 1 3 6 6 5 5 1 6 3 1 2 | 6 2 4 3 1 5 2 3 1 6 4 5 5 6 3 1 2 4 4 1 5 2 3 6 3 5 2 4 1 6 | No | 6.98 |
| 16 | 5 1 5 2 6 5 4 6 1 5 4 5 3 1 | 5 6 2 4 3 1 3 5 1 2 4 6 2 4 3 5 1 6 4 1 6 3 2 5 5 2 4 1 6 3 1 6 5 2 4 3 | No | 9.51 |
| 17 | 3 1 6 1 6 2 5 6 1 3 4 6 5 2 | 3 6 1 3 6 2 6 5 4 5 4 3 5 2 6 | No | 5.73 |
| 18 | 2 5 6 1 2 3 6 2 3 2 3 1 5 1 | 2 5 6 1 3 4 2 1 3 6 5 2 5 6 1 3 4 2 4 2 3 1 6 5 1 4 2 3 6 5 3 5 4 1 2 6 | No | 8.36 |
| 19 | 6 4 3 1 6 6 3 6 6 4 5 1 5 3 | 4 6 3 3 6 5 1 4 5 2 1 3 4 5 6 1 2 3 5 2 1 6 4 3 | No | 6.02 |
| 20 | 3 4 2 2 4 2 3 6 5 3 6 3 2 6 | 2 3 4 6 5 4 3 2 1 6 5 2 6 3 4 1 3 5 1 2 6 4 5 3 | No | 9.54 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1703 | 1703 | Yes | 2.67 |
| 2 | 1227 | 1227 | Yes | 2.26 |
| 3 | 858 | 858 | Yes | 2.75 |
| 4 | 1473 | 1473 | Yes | 2.49 |
| 5 | 1440 | 1440 | Yes | 2.02 |
| 6 | 761 | 761 | Yes | 2.21 |
| 7 | 1566 | 1566 | Yes | 2.16 |
| 8 | 1748 | 1748 | Yes | 2.92 |
| 9 | 2162 | 2162 | Yes | 2.09 |
| 10 | 1441 | 1441 | Yes | 3.21 |
| 11 | 1896 | 1896 | Yes | 2.22 |
| 12 | 1589 | 1589 | Yes | 1.74 |
| 13 | 2453 | 2453 | Yes | 2.31 |
| 14 | 1513 | 1513 | Yes | 2.55 |
| 15 | 1300 | 1300 | Yes | 2.15 |
| 16 | 1762 | 1762 | Yes | 2.13 |
| 17 | 2072 | 2072 | Yes | 1.95 |
| 18 | 2288 | 2288 | Yes | 2.6 |
| 19 | 2090 | 2090 | Yes | 2.43 |
| 20 | 1352 | 1352 | Yes | 3.07 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 58 | 58 | Yes | 5.24 |
| 2 | 44 | 44 | Yes | 8.25 |
| 3 | 55 | 59 | No | 7.54 |
| 4 | 53 | 54 | No | 8.27 |
| 5 | 46 | 45 | No | 5.51 |
| 6 | 47 | 52 | No | 6.55 |
| 7 | 73 | 73 | Yes | 7.62 |
| 8 | 68 | 72 | No | 5.9 |
| 9 | 55 | 55 | Yes | 5.58 |
| 10 | 73 | 72 | No | 17.64 |
| 11 | 39 | 39 | Yes | 6.25 |
| 12 | 66 | 67 | No | 5.78 |
| 13 | 51 | 53 | No | 6.82 |
| 14 | 69 | 65 | No | 7.56 |
| 15 | 67 | 64 | No | 6.44 |
| 16 | 44 | 44 | Yes | 8.37 |
| 17 | 67 | 65 | No | 6.56 |
| 18 | 62 | 63 | No | 5.74 |
| 19 | 48 | 48 | Yes | 7.14 |
| 20 | 63 | 66 | No | 6.59 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GIZPRDH | GIZPRDH | Yes | 3.3 |
| 2 | LBRXFUA | LBRXFUA | Yes | 2.62 |
| 3 | ZUPBTRW | ZUPBTRW | Yes | 2.76 |
| 4 | PAVEWGR | PAVEWGR | Yes | 2.66 |
| 5 | TFXEJLQ | TFXEJLQ | Yes | 4.82 |
| 6 | RGTLQAY | RGTLQAY | Yes | 2.51 |
| 7 | KNMAWYO | KNMAWYO | Yes | 9.64 |
| 8 | VJBITAC | VJBITAC | Yes | 3.94 |
| 9 | FBHORZC | FBHORZC | Yes | 7.02 |
| 10 | XNQVLRB | XNQVL RB | No | 8.75 |
| 11 | USBQDHF | USBQDHF | Yes | 2.88 |
| 12 | RBNQJXS | RBNQJXS | Yes | 6.78 |
| 13 | JLMBWDC | JLM BWDC | No | 5.96 |
| 14 | THRVIGK | THRVI GK | No | 5.55 |
| 15 | JQUEKVR | JQUEKVR | Yes | 2.23 |
| 16 | AUMDXZC | AUMDXZC | Yes | 2.7 |
| 17 | HOUSVMY | HOUSVMY | Yes | 6.55 |
| 18 | HEMROUB | HEMROUB | Yes | 8.39 |
| 19 | HQRIKSE | HQRIKSE | Yes | 5.31 |
| 20 | PZEQKNJ | PZEQKJN | No | 2.75 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.6, 8.4] | 1.6 8.4 | Yes | 4.75 |
| 2 | [4.7, 5.3] | 3.7 6.3 | No | 7.32 |
| 3 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.93 |
| 4 | [1.6, 8.4] | 1.6 8.4 | Yes | 7.03 |
| 5 | [2.0, 8.0] | 2.0 8.0 | Yes | 5.43 |
| 6 | [1.2, 8.8] | 8.8 1.2 | Yes | 7.79 |
| 7 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.13 |
| 8 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.0 |
| 9 | [0.2, 9.8] | 9.8 0.2 | Yes | 4.38 |
| 10 | [1.2, 8.8] | 3.7 6.3 | No | 5.07 |
| 11 | [2.7, 7.3] | 7.3 2.7 | Yes | 4.19 |
| 12 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.91 |
| 13 | [1.6, 8.4] | 1.6 8.4 | Yes | 5.03 |
| 14 | [3.0, 7.0] | 3.0 7.0 | Yes | 4.55 |
| 15 | [3.5, 6.5] | 3.5 6.5 | Yes | 5.48 |
| 16 | [2.0, 8.0] | 8.0 2.0 | Yes | 6.48 |
| 17 | [4.0, 6.0] | 4.0 6.0 | Yes | 6.12 |
| 18 | [0.6, 9.4] | 0.6 9.4 | Yes | 5.31 |
| 19 | [3.9, 6.1] | 6.1 3.9 | Yes | 4.37 |
| 20 | [1.0, 9.0] | 1.0 9.0 | Yes | 9.25 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PBR48GIMECH5 | PBR48GIMECH5 | Yes | 2.6 |
| 2 | 31C52S6JPJIX | 31C52S6JPJIX | Yes | 2.02 |
| 3 | 4M0JOUPRIT1Z | 4M0JOUPRIT1Z | Yes | 2.18 |
| 4 | D8I7AJJ5S966 | D817AJJ5S966 | No | 3.2 |
| 5 | 2YFG0NETKNR7 | 2YFGONETKNR7 | No | 2.54 |
| 6 | R6UZQ46X8WIK | R6UZQ46X8WIK | Yes | 3.06 |
| 7 | U6CSWBWV049Z | U6CSWBWVO49Z | No | 2.79 |
| 8 | B9F6ZOUXTIY2 | B9F6ZOUXT IY2 | No | 2.32 |
| 9 | KA4U68KT05YW | KA4U68KT05YW | Yes | 2.96 |
| 10 | U2NCHRSC1GMV | U2NHRSC1GMV | No | 2.48 |
| 11 | X9CG0GNT7DX9 | X9CG0GNT7DX9 | Yes | 2.96 |
| 12 | AYP52FZ3MF8V | AYP52FZ3MF8V | Yes | 2.49 |
| 13 | Q91M1DC77RHL | Q91M1DC77RHL | Yes | 2.48 |
| 14 | 0QIAH294W6WW | 0QIAH294W6WW | Yes | 3.07 |
| 15 | MBXG8XTXTUGA | MBXG8XTXTUGA | Yes | 1.79 |
| 16 | GL2604G9Y227 | GL2604G9Y227 | Yes | 2.61 |
| 17 | N4BWQGDWDU7B | N4BWOGDWDU7B | No | 2.23 |
| 18 | L3AR81OX1VHK | L3AR810X1VHK | No | 2.01 |
| 19 | YU6MNWOZBD35 | YUGMNWOZBD35 | No | 2.6 |
| 20 | LGSI4OHFBATS | LGSI4OHFBATS | Yes | 2.16 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 2.91 |
| 2 | 4 | 4 | Yes | 1.94 |
| 3 | 4096 | 4096 | Yes | 4.66 |
| 4 | 5 | 5 | Yes | 1.96 |
| 5 | 44 | 44 | Yes | 2.11 |
| 6 | 48 | 48 | Yes | 1.78 |
| 7 | 39 | 39 | Yes | 3.33 |
| 8 | 23 | 23 | Yes | 1.59 |
| 9 | 1440 | 1440 | Yes | 2.21 |
| 10 | 19 | 19 | Yes | 1.86 |
| 11 | 3 | 3 | Yes | 3.56 |
| 12 | 67 | 67 | Yes | 1.76 |
| 13 | 4 | 4 | Yes | 3.06 |
| 14 | 793 | 793 | Yes | 4.65 |
| 15 | 243 | 243 | Yes | 1.75 |
| 16 | 7680 | 7680 | Yes | 1.59 |
| 17 | 36 | 36 | Yes | 2.08 |
| 18 | 63 | 63 | Yes | 1.91 |
| 19 | 20 | 20 | Yes | 4.78 |
| 20 | 9 | 9 | Yes | 2.42 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <))\_/\ < | `<))_\/\ <` | No | 3.84 |
| 2 | /_( _< )/ | / _ ( _ < _ ) / | No | 9.28 |
| 3 | )<_/<)\\  | )<_/<)\\\\ | No | 7.99 |
| 4 | \_<_ )\_  | / _ < _ ( ) / _ ( | No | 8.22 |
| 5 | //)<_<\ < | //)<_<\< | No | 5.8 |
| 6 | <\ (<)  \ | < \ ( < ) \ | No | 5.92 |
| 7 | ))(\((\<_ | ))(\((\\<_ | No | 5.96 |
| 8 | _<(<< \<\ | _<((< \< \ | No | 7.7 |
| 9 | ( <))_\<\ | ( < ) ) _ / < \ | No | 6.95 |
| 10 | )\(\(/<// | )\( \(/ / / / | No | 9.24 |
| 11 | <__\ \\(/ | <  \ ( ( / | No | 8.05 |
| 12 | )/\ <_ _( | ) / \ ␣ < _ ␣ _ ␣ ( | No | 7.74 |
| 13 | ) )<_)\\) | )␣) < _ ) \ \ ) | No | 6.66 |
| 14 | <<<( (\_< | <<< ( ( \ _ < | No | 5.22 |
| 15 | (\\/)()</ | ( \ \ / ) ( ) < / | No | 3.0 |
| 16 |  <((__)(_ | <((__)(_ | No | 6.3 |
| 17 | (__(_(< \ | (_ _ (_ _ (< ␣ \ | No | 4.58 |
| 18 | _ )<)\ (( | _␣) < ) \␣(( | No | 9.93 |
| 19 | \ ) //(() | \␣)␣//(( ) | No | 5.86 |
| 20 | __//<< /_ | __//<< [ /_ | No | 7.02 |
