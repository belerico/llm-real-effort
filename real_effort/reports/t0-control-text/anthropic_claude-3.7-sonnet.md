# Benchmark Report — claude-3.7-sonnet

- **Model**: `anthropic/claude-3.7-sonnet`
- **Date**: 2026-03-26 15:46:33

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
| sudoku_game | 5793 | 32959 | 38752 | 2 | 18 | 22.42 | 448.47 |
| add_numbers | 3180 | 8422 | 11602 | 20 | 0 | 6.98 | 139.56 |
| counting_zeros | 4500 | 21250 | 25750 | 3 | 17 | 12.88 | 257.63 |
| task_decoding | 4500 | 5791 | 10291 | 20 | 0 | 4.75 | 95.04 |
| task_summation | 4560 | 22885 | 27445 | 20 | 0 | 14.19 | 283.92 |
| task_transcription | 3348 | 3336 | 6684 | 20 | 0 | 3.54 | 70.87 |
| task_sequences | 3241 | 14473 | 17714 | 16 | 4 | 10.57 | 211.33 |
| string_entry | 3720 | 5551 | 9271 | 13 | 7 | 5.10 | 102.07 |
| **TOTAL** | **32842** | **114667** | **147509** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 2 1 4 6 3 5 5 4 2 5 6 2 | 4 1 2 1 4 6 3 5 5 2 4 5 6 2 | No | 25.39 |
| 2 | 4 1 5 6 1 6 6 4 3 2 6 5 4 1 | 4 5 1 6 1 6 6 4 3 6 1 5 4 | No | 25.45 |
| 3 | 1 6 5 3 2 6 4 1 1 2 6 4 5 1 | 1 6 5 3 2 6 4 1 1 2 6 4 5 1 | Yes | 25.2 |
| 4 | 4 3 2 5 2 5 2 1 3 2 5 6 3 2 | 4 3 2 5 2 5 2 1 1 3 6 4 3 2 5 6 3 2 | No | 22.7 |
| 5 | 1 1 3 6 2 1 5 3 2 3 2 3 1 5 | 1 1 3 6 2 3 5 1 3 2 2 1 3 5 | No | 24.47 |
| 6 | 4 2 1 3 6 4 1 4 5 4 1 6 5 4 | 4 1 2 3 6 4 1 4 5 4 6 1 5 4 | No | 18.41 |
| 7 | 2 3 1 6 3 2 1 2 6 2 1 2 6 3 | 2 3 6 1 2 3 2 1 6 4 2 1 1 6 3 | No | 24.96 |
| 8 | 2 6 4 2 5 1 3 2 6 4 5 4 1 6 | 6 2 4 2 5 1 3 2 6 4 5 4 6 1 | No | 19.17 |
| 9 | 2 6 6 6 3 5 4 6 3 1 4 5 6 2 | 2 6 6 5 3 6 4 6 3 1 4 5 6 2 | No | 23.23 |
| 10 | 3 5 1 6 6 1 4 6 3 1 1 2 5 4 | 3 5 6 1 1 6 4 6 3 1 1 2 5 4 | No | 18.23 |
| 11 | 5 4 1 2 6 2 4 3 6 4 1 5 6 1 | 4 5 1 3 2 2 6 4 3 6 5 1 4 6 1 | No | 15.79 |
| 12 | 6 4 2 6 2 5 1 3 2 5 1 1 3 1 | 6 2 4 6 2 5 1 3 1 5 2 1 3 1 | No | 20.02 |
| 13 | 2 4 1 2 5 5 6 1 1 6 3 5 1 6 | Looking at this 6×6 Sudoku puzzle, I'll work through it systematically to find all missing numbers.  First, I'll analyze the puzzle by rows, columns, and 2×3 boxes:  Row 1: [? ? 3 6 ? 5] - missing 1,2,4 Row 2: [1 3 ? ? 6 4] - missing 2,5 Row 3: [? ? ? 4 3 2] - missing 1,5,6 Row 4: [4 ? ? 2 5 ?] - missing 1,3,6 Row 5: [6 2 ? 3 4 ?] - missing 1,5 Row 6: [3 5 4 1 2 ?] - missing 6  Working through each empty cell:  R1C1: Can't be 1,3,4,6 (column 1), can't be 3,5,6 (row 1) → must be 2 R1C2: Can't be 2,3,5 (column 2), can't be 2,3,5,6 (row 1) → must be 4 R1C5: Can't be 2,4,6 (column 5), can't be 2,3,4,6 (row 1) → must be 1  R2C3: Can't be 3,4 (column 3), can't be 1,3,4,6 (row 2) → must be 5 R2C4: Can't be 1,3,6 (column 4), can't be 1,3,4,5,6 (row 2) → must be 2  R3C1: Can't be 1,3,4,6 (column 1), can't be 2,3,4 (row 3) → must be 5 R3C2: Can't be 2,3,4,5 (column 2), can't be 2,3,4,5 (row 3) → must be 6 R3C3: Can't be 3,4,5 (column 3), can't be 2,3,4,5,6 (row 3) → must be 1  R4C2: Can't be 2,3,4,5,6 (column 2), can't be 2,4,5 (row 4) → must be 1 R4C3: Can't be 1,3,4,5 (column 3), can't be 1,2,4,5 (row 4) → must be 6 R4C6: Can't be 2,4,5,6 (column 6), can't be 1,2,4,5,6 (row 4) → must be 3  R5C3: Can't be 1,3,4,5,6 (column 3), can't be 2,3,4,6 (row 5) → must be 5 R5C6: Can't be 2,3,4,5 (column 6), can't be 2,3,4,5,6 (row 5) → must be 1  R6C6: Can't be 1,3,4,5 (column 6), can't be | No | 27.11 |
| 14 | 3 4 3 5 5 3 1 3 6 4 2 1 6 4 | 3 4 3 5 5 3 1 3 6 4 2 1 6 4 | Yes | 25.57 |
| 15 | 1 6 2 6 3 1 5 3 1 4 2 5 6 4 | 6 1 6 3 1 5 3 1 4 2 6 5 4 | No | 22.65 |
| 16 | 1 3 4 1 2 5 3 4 2 4 5 1 4 2 | 4 3 1 2 1 3 5 4 2 1 5 4 4 2 | No | 20.97 |
| 17 | 4 2 2 5 1 6 2 5 4 6 5 3 2 4 | 2 4 5 1 2 5 6 2 4 6 5 3 4 2 | No | 21.08 |
| 18 | 6 5 1 2 4 1 6 3 4 4 3 1 3 6 | 6 1 5 2 4 1 6 3 4 4 3 1 3 6 | No | 20.41 |
| 19 | 2 3 2 3 5 1 2 4 1 3 6 5 4 2 | 2 3 2 6 4 3 5 1 2 4 1 3 6 5 4 2 | No | 19.66 |
| 20 | 3 2 6 6 6 5 1 1 4 3 6 1 2 4 | 3 6 6 1 5 6 1 4 3 6 1 2 4 | No | 27.96 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1512 | 1512 | Yes | 5.45 |
| 2 | 1954 | 1954 | Yes | 7.51 |
| 3 | 1868 | 1868 | Yes | 6.21 |
| 4 | 2904 | 2904 | Yes | 7.44 |
| 5 | 1287 | 1287 | Yes | 5.92 |
| 6 | 900 | 900 | Yes | 9.41 |
| 7 | 1590 | 1590 | Yes | 6.37 |
| 8 | 1517 | 1517 | Yes | 7.81 |
| 9 | 1718 | 1718 | Yes | 7.28 |
| 10 | 1783 | 1783 | Yes | 6.27 |
| 11 | 1433 | 1433 | Yes | 7.39 |
| 12 | 1362 | 1362 | Yes | 8.23 |
| 13 | 1280 | 1280 | Yes | 6.82 |
| 14 | 1589 | 1589 | Yes | 3.76 |
| 15 | 1563 | 1563 | Yes | 6.66 |
| 16 | 1609 | 1609 | Yes | 6.93 |
| 17 | 724 | 724 | Yes | 6.75 |
| 18 | 1812 | 1812 | Yes | 7.44 |
| 19 | 1942 | 1942 | Yes | 8.69 |
| 20 | 1780 | 1780 | Yes | 7.23 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 57 | 54 | No | 8.42 |
| 2 | 71 | 63 | No | 14.56 |
| 3 | 59 | 58 | No | 16.96 |
| 4 | 74 | 73 | No | 16.92 |
| 5 | 64 | 61 | No | 15.8 |
| 6 | 44 | 38 | No | 12.54 |
| 7 | 70 | 65 | No | 14.26 |
| 8 | 61 | 67 | No | 16.47 |
| 9 | 57 | 57 | Yes | 12.17 |
| 10 | 43 | 34 | No | 11.32 |
| 11 | 57 | 53 | No | 8.54 |
| 12 | 39 | 33 | No | 12.97 |
| 13 | 70 | 61 | No | 18.03 |
| 14 | 36 | 36 | Yes | 8.85 |
| 15 | 39 | 42 | No | 13.72 |
| 16 | 73 | 61 | No | 7.75 |
| 17 | 73 | 67 | No | 12.95 |
| 18 | 53 | 49 | No | 7.11 |
| 19 | 52 | 52 | Yes | 14.07 |
| 20 | 45 | 40 | No | 14.22 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | SXKCTJY | SXKCTJY | Yes | 5.87 |
| 2 | ZECHRGD | ZECHRGD | Yes | 5.39 |
| 3 | XMUWPVD | XMUWPVD | Yes | 5.62 |
| 4 | AUGJHSV | AUGJHSV | Yes | 4.65 |
| 5 | TYXOEFC | TYXOEFC | Yes | 4.41 |
| 6 | CEDKXYO | CEDKXYO | Yes | 4.45 |
| 7 | HJFMGUS | HJFMGUS | Yes | 4.47 |
| 8 | LBIUTPN | LBIUTPN | Yes | 5.04 |
| 9 | BWKPFNI | BWKPFNI | Yes | 3.71 |
| 10 | SBHIFAM | SBHIFAM | Yes | 4.13 |
| 11 | XRIZTJB | XRIZTJB | Yes | 4.24 |
| 12 | HGFZAVC | HGFZAVC | Yes | 3.91 |
| 13 | JFAMPQU | JFAMPQU | Yes | 5.36 |
| 14 | UHQXBEY | UHQXBEY | Yes | 5.94 |
| 15 | XURVTQB | XURVTQB | Yes | 3.6 |
| 16 | DXUELRV | DXUELRV | Yes | 4.72 |
| 17 | GWZJOQM | GWZJOQM | Yes | 4.55 |
| 18 | CGHKLEF | CGHKLEF | Yes | 4.36 |
| 19 | USWEATG | USWEATG | Yes | 6.26 |
| 20 | KXPCBUQ | KXPCBUQ | Yes | 4.35 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.3, 9.7] | 9.7 0.3 | Yes | 14.23 |
| 2 | [0.9, 9.1] | 0.9 9.1 | Yes | 16.47 |
| 3 | [4.5, 5.5] | 4.5 5.5 | Yes | 14.1 |
| 4 | [2.1, 7.9] | 7.9 2.1 | Yes | 11.25 |
| 5 | [0.3, 9.7] | 9.7 0.3 | Yes | 10.71 |
| 6 | [0.7, 9.3] | 0.7 9.3 | Yes | 13.18 |
| 7 | [0.9, 9.1] | 9.1 0.9 | Yes | 13.69 |
| 8 | [3.2, 6.8] | 3.2 6.8 | Yes | 23.67 |
| 9 | [2.9, 7.1] | 2.9 7.1 | Yes | 16.56 |
| 10 | [1.1, 8.9] | 1.1 8.9 | Yes | 12.18 |
| 11 | [3.5, 6.5] | 3.5 6.5 | Yes | 12.42 |
| 12 | [1.6, 8.4] | 8.4 1.6 | Yes | 14.91 |
| 13 | [4.0, 6.0] | 4.0 6.0 | Yes | 17.92 |
| 14 | [1.5, 8.5] | 8.5 1.5 | Yes | 12.05 |
| 15 | [4.0, 6.0] | 4.0 6.0 | Yes | 19.47 |
| 16 | [0.5, 9.5] | 0.5 9.5 | Yes | 11.19 |
| 17 | [4.0, 6.0] | 4.0 6.0 | Yes | 12.2 |
| 18 | [2.5, 7.5] | 2.5 7.5 | Yes | 12.66 |
| 19 | [2.1, 7.9] | 7.9 2.1 | Yes | 13.78 |
| 20 | [3.7, 6.3] | 6.3 3.7 | Yes | 11.26 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | C4NPUCQ8W4Q9 | C4NPUCQ8W4Q9 | Yes | 2.9 |
| 2 | Q9LMBG0FYGFU | Q9LMBG0FYGFU | Yes | 3.54 |
| 3 | RU4ZN8I15AGT | RU4ZN8I15AGT | Yes | 2.47 |
| 4 | L4FKH67R3OV1 | L4FKH67R3OV1 | Yes | 2.74 |
| 5 | BP8PU13FV8AR | BP8PU13FV8AR | Yes | 3.61 |
| 6 | F8IE0KPD1ABT | F8IE0KPD1ABT | Yes | 3.93 |
| 7 | SPEGB1D03CL4 | SPEGB1D03CL4 | Yes | 4.71 |
| 8 | NBLYLDUXGASR | NBLYLDUXGASR | Yes | 2.21 |
| 9 | MK84ZTYYR3H1 | MK84ZTYYR3H1 | Yes | 2.32 |
| 10 | 1K2YRJ1VI3XW | 1K2YRJ1VI3XW | Yes | 4.85 |
| 11 | 6LIH0GRNRRA4 | 6LIH0GRNRRA4 | Yes | 3.42 |
| 12 | RHF0J0VKRN56 | RHF0J0VKRN56 | Yes | 3.06 |
| 13 | 5PW7UNXRLCPR | 5PW7UNXRLCPR | Yes | 4.92 |
| 14 | WZSBW0WBIZTH | WZSBW0WBIZTH | Yes | 4.12 |
| 15 | B3SYGO3JWK7E | B3SYGO3JWK7E | Yes | 4.01 |
| 16 | RP620WS5ZEWD | RP620WS5ZEWD | Yes | 3.76 |
| 17 | Z0YYRBY7F1P3 | Z0YYRBY7F1P3 | Yes | 3.48 |
| 18 | UO5A5WQXEBK9 | UO5A5WQXEBK9 | Yes | 3.85 |
| 19 | T3CKX0UFPI4M | T3CKX0UFPI4M | Yes | 2.98 |
| 20 | LFVWCLFJIWPI | LFVWCLFJIWPI | Yes | 3.98 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 | 1 | Yes | 9.81 |
| 2 | 60 | 60 | Yes | 24.44 |
| 3 | 10 | 9 | No | 11.68 |
| 4 | 60 | 60 | Yes | 6.34 |
| 5 | 31 | 31 | Yes | 5.32 |
| 6 | 3 | 3 | Yes | 20.21 |
| 7 | 19 | 19 | Yes | 5.44 |
| 8 | 63 | 63 | Yes | 6.83 |
| 9 | 4096 | 16384 | No | 13.73 |
| 10 | 7680 | 7680 | Yes | 10.21 |
| 11 | 9 | 9 | Yes | 6.97 |
| 12 | 7 | 7 | Yes | 4.6 |
| 13 | 1440 | 1440 | Yes | 7.27 |
| 14 | 3 | 3 | Yes | 10.25 |
| 15 | 67 | 67 | Yes | 5.14 |
| 16 | 20 | 21 | No | 20.51 |
| 17 | 9 | 9 | Yes | 7.21 |
| 18 | 6 | 6 | Yes | 6.18 |
| 19 | 5 | 17 | No | 13.87 |
| 20 | 4 | 4 | Yes | 15.3 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )/< \( _\ | )/< \( _\ | Yes | 3.44 |
| 2 | __\\/\_(  | __\\/\_( | No | 6.18 |
| 3 | \\)\\ _ ( | \\)\\ _ ( | Yes | 8.4 |
| 4 | (\/(\_<__ | (\/(\_<__ | Yes | 6.01 |
| 5 | )\_)_)(<( | )\_)_)(<( | Yes | 2.81 |
| 6 | / \)_<)\< | / \)_<)\ | No | 3.74 |
| 7 | _)_\((\_) | _)_\((\_) | Yes | 3.6 |
| 8 | \(/// )_  | \(/// )_ | No | 5.34 |
| 9 | \)\< \\ _ | \)\< \\ _ | Yes | 7.63 |
| 10 | _/\/<)\_( | _/\/<)\_( | Yes | 5.64 |
| 11 | \\</<<\ ) | \\</<<\ ) | Yes | 6.61 |
| 12 | /\ /) _   | /\ /) _ | No | 5.15 |
| 13 | \__\()(_  | \__\()(_ | No | 5.39 |
| 14 | /_))_)<_( | /_))_)<_( | Yes | 6.05 |
| 15 |   ((/<<</ | ((/<<</ | No | 4.77 |
| 16 |  <) ) <<_ | <) ) <<_ | No | 4.8 |
| 17 | )_<<( /() | )_<<( /() | Yes | 4.4 |
| 18 | /<< <\(/( | /<< <\(/( | Yes | 4.03 |
| 19 | /) _ < <_ | /) _ < <_ | Yes | 3.25 |
| 20 | ) ((/_<)\ | ) ((/_<)\ | Yes | 4.84 |
