# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-27 10:17:33

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
| sudoku_game | 6696 | 40041 | 46737 | 9 | 11 | 33.15 | 663.09 |
| add_numbers | 4080 | 1571 | 5651 | 20 | 0 | 3.86 | 77.28 |
| counting_zeros | 5400 | 26169 | 31569 | 16 | 4 | 18.84 | 376.78 |
| task_decoding | 5400 | 5135 | 10535 | 20 | 0 | 6.64 | 132.86 |
| task_summation | 5460 | 15130 | 20590 | 20 | 0 | 11.79 | 235.76 |
| task_transcription | 4247 | 2901 | 7148 | 20 | 0 | 7.75 | 155.08 |
| task_sequences | 4141 | 8370 | 12511 | 19 | 1 | 10.81 | 216.24 |
| string_entry | 4590 | 4547 | 9137 | 14 | 6 | 11.00 | 220.03 |
| **TOTAL** | **40014** | **103864** | **143878** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 1 6 2 1 4 2 5 1 4 3 1 6 |  | No | 40.6 |
| 2 | 2 6 1 4 6 2 3 4 3 2 1 6 6 3 |  | No | 34.61 |
| 3 | 1 6 6 3 5 5 4 1 1 5 6 2 5 1 |  | No | 32.8 |
| 4 | 4 5 1 5 3 4 4 2 6 4 5 3 6 5 | 4 5 1 5 3 4 4 2 6 4 5 3 6 5 | Yes | 36.03 |
| 5 | 3 5 1 2 3 4 1 3 4 6 4 2 5 2 | 3 5 1 2 3 4 1 3 4 6 4 2 5 2 | Yes | 31.31 |
| 6 | 4 6 1 6 3 4 1 5 4 2 6 1 5 4 |  | No | 30.75 |
| 7 | 2 4 2 1 1 5 2 1 6 5 4 5 1 4 |  | No | 37.89 |
| 8 | 1 6 2 4 5 2 5 6 4 3 1 2 3 6 | 1 6 2 4 5 2 5 6 4 3 1 2 3 6 | Yes | 33.62 |
| 9 | 2 4 6 6 3 1 5 4 6 3 5 6 6 4 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 3 1 5 \| _ _ _ - Missing: 2, 4, 6 - Column 5 has 2,1,3,6,5 → needs 4, so position (1,5) = 4 - Column 4 has 4,5,3 → needs 1,2,6; Row 1 needs 2,6 → position (1,4) = 2 - Position (1,6) = 6  **Row 2:** 4 _ _ \| _ 2 _ - Column 1 has 3,4,5,2,1 → Row 6, Col 1 = 6 - Column 2 needs 4,5,6; after solving Row 4, Col 2 = 6 - Column 3 needs 3,4,6; Row 2 needs 1,3,5 → position (2,3) = 3 - Column 4 needs 1,6 → position (2,4) = 1 - Position (2,6) = 5  **Row 3:** 5 2 _ \| _ 1 _ - Column 3 needs 4 → position (3,3) = 4 - Column 4 needs 6 → position (3,4) = 6 - Position (3,6) = 3  **Row 4:** 2 _ _ \| 4 3 1 - Missing: 5, 6 - Column 3 can only have 6 (from | No | 34.08 |
| 10 | 3 2 6 1 3 1 5 4 3 4 5 5 3 1 | 3 2 6 1 3 1 5 4 3 4 5 5 3 1 | Yes | 31.06 |
| 11 | 6 1 6 3 5 4 2 6 1 4 6 6 5 3 |  | No | 31.55 |
| 12 | 4 1 6 4 1 2 1 5 2 2 6 1 6 4 | 4 1 6 4 1 2 1 5 2 2 6 1 6 4 | Yes | 29.54 |
| 13 | 5 5 3 2 4 6 2 4 5 6 5 6 2 5 |  | No | 29.21 |
| 14 | 4 2 4 3 3 4 2 6 6 4 2 3 5 1 | 4 2 4 3 3 4 2 6 6 4 2 3 5 1 | Yes | 31.11 |
| 15 | 1 4 5 3 2 2 6 2 3 5 3 1 6 3 | 1 4 5 3 2 2 6 2 3 5 3 1 6 3 | Yes | 39.64 |
| 16 | 5 5 6 5 4 1 3 2 5 1 4 5 6 4 | 5 5 6 5 4 1 3 2 5 1 4 5 6 4 | Yes | 25.17 |
| 17 | 2 5 3 5 1 4 6 3 1 1 4 6 3 5 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** Has 3,1,4,6 → needs 2,5 - Column 1 needs 1,2,3,4 (has 6,5) → Position (1,1) = 2 - Position (1,3 | No | 34.97 |
| 18 | 2 5 1 4 2 3 2 4 5 5 6 4 1 5 | 2 5 1 4 2 3 4 | No | 34.32 |
| 19 | 1 5 4 3 6 2 3 1 5 4 4 3 5 6 | 1 5 4 3 6 2 3 1 5 4 4 3 5 6 | Yes | 34.45 |
| 20 | 4 3 2 2 4 6 3 3 2 4 1 1 6 4 |  | No | 30.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1687 | 1687 | Yes | 2.98 |
| 2 | 2522 | 2522 | Yes | 3.69 |
| 3 | 2051 | 2051 | Yes | 5.09 |
| 4 | 1054 | 1054 | Yes | 2.46 |
| 5 | 1742 | 1742 | Yes | 2.89 |
| 6 | 2158 | 2158 | Yes | 2.65 |
| 7 | 1939 | 1939 | Yes | 4.74 |
| 8 | 1585 | 1585 | Yes | 3.58 |
| 9 | 1798 | 1798 | Yes | 2.86 |
| 10 | 1289 | 1289 | Yes | 4.87 |
| 11 | 1745 | 1745 | Yes | 3.06 |
| 12 | 1851 | 1851 | Yes | 6.62 |
| 13 | 873 | 873 | Yes | 2.98 |
| 14 | 1433 | 1433 | Yes | 4.48 |
| 15 | 1291 | 1291 | Yes | 2.64 |
| 16 | 1824 | 1824 | Yes | 3.58 |
| 17 | 2175 | 2175 | Yes | 5.16 |
| 18 | 1221 | 1221 | Yes | 3.61 |
| 19 | 1770 | 1770 | Yes | 6.52 |
| 20 | 549 | 549 | Yes | 2.8 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 17.23 |
| 2 | 62 | 62 | Yes | 22.55 |
| 3 | 56 | 55 | No | 14.42 |
| 4 | 39 | 39 | Yes | 14.19 |
| 5 | 56 | 56 | Yes | 22.35 |
| 6 | 73 | 74 | No | 25.16 |
| 7 | 39 | 39 | Yes | 18.7 |
| 8 | 52 | 52 | Yes | 16.48 |
| 9 | 62 | 62 | Yes | 17.16 |
| 10 | 69 | 68 | No | 25.0 |
| 11 | 54 | 54 | Yes | 18.48 |
| 12 | 57 | 53 | No | 21.95 |
| 13 | 55 | 55 | Yes | 17.66 |
| 14 | 52 | 52 | Yes | 16.52 |
| 15 | 52 | 52 | Yes | 15.69 |
| 16 | 67 | 67 | Yes | 18.13 |
| 17 | 73 | 73 | Yes | 21.81 |
| 18 | 50 | 50 | Yes | 16.16 |
| 19 | 58 | 58 | Yes | 21.31 |
| 20 | 53 | 53 | Yes | 15.83 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | RVXHWUK | RVXHWUK | Yes | 4.71 |
| 2 | NOHMWAD | NOHMWAD | Yes | 15.32 |
| 3 | ECFWUXA | ECFWUXA | Yes | 4.79 |
| 4 | YZSFUEI | YZSFUEI | Yes | 4.64 |
| 5 | RFVQPMA | RFVQPMA | Yes | 4.9 |
| 6 | HKXVCGI | HKXVCGI | Yes | 5.66 |
| 7 | KBMWIQZ | KBMWIQZ | Yes | 5.6 |
| 8 | IDUZJMW | IDUZJMW | Yes | 14.67 |
| 9 | BOEPKYJ | BOEPKYJ | Yes | 4.29 |
| 10 | TVOHEKY | TVOHEKY | Yes | 4.39 |
| 11 | FWKOBHR | FWKOBHR | Yes | 4.12 |
| 12 | SATGYEZ | SATGYEZ | Yes | 14.34 |
| 13 | ZQKLGYA | ZQKLGYA | Yes | 5.46 |
| 14 | AFLQZPN | AFLQZPN | Yes | 5.75 |
| 15 | AVUELWM | AVUELWM | Yes | 4.46 |
| 16 | QWJVLKY | QWJVLKY | Yes | 5.41 |
| 17 | ZGLEMKY | ZGLEMKY | Yes | 4.61 |
| 18 | KVEXFNT | KVEXFNT | Yes | 5.05 |
| 19 | WIMBSGP | WIMBSGP | Yes | 10.21 |
| 20 | FTLCYBX | FTLCYBX | Yes | 4.46 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 4.0 6.0 | Yes | 13.64 |
| 2 | [3.0, 7.0] | 3.0 7.0 | Yes | 13.33 |
| 3 | [1.1, 8.9] | 8.9 1.1 | Yes | 10.4 |
| 4 | [2.6, 7.4] | 7.4 2.6 | Yes | 6.48 |
| 5 | [0.5, 9.5] | 9.5 0.5 | Yes | 11.2 |
| 6 | [1.9, 8.1] | 8.1 1.9 | Yes | 12.12 |
| 7 | [4.1, 5.9] | 4.1 5.9 | Yes | 12.26 |
| 8 | [1.5, 8.5] | 8.5 1.5 | Yes | 8.5 |
| 9 | [2.2, 7.8] | 2.2 7.8 | Yes | 11.86 |
| 10 | [3.3, 6.7] | 6.7 3.3 | Yes | 13.57 |
| 11 | [4.7, 5.3] | 5.3 4.7 | Yes | 9.62 |
| 12 | [0.8, 9.2] | 9.2 0.8 | Yes | 10.48 |
| 13 | [4.7, 5.3] | 5.3 4.7 | Yes | 11.37 |
| 14 | [3.7, 6.3] | 3.7 6.3 | Yes | 11.01 |
| 15 | [1.4, 8.6] | 8.6 1.4 | Yes | 10.45 |
| 16 | [2.6, 7.4] | 7.4 2.6 | Yes | 7.88 |
| 17 | [3.1, 6.9] | 3.1 6.9 | Yes | 17.77 |
| 18 | [3.7, 6.3] | 3.7 6.3 | Yes | 18.16 |
| 19 | [2.7, 7.3] | 2.7 7.3 | Yes | 11.95 |
| 20 | [1.1, 8.9] | 1.1 8.9 | Yes | 13.7 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4HV94D3I38DW | 4HV94D3I38DW | Yes | 3.99 |
| 2 | DIZIQYJQ3NHK | DIZIQYJQ3NHK | Yes | 3.72 |
| 3 | 8DSYP2BSJLEP | 8DSYP2BSJLEP | Yes | 4.5 |
| 4 | QP4QVN2PYXT9 | QP4QVN2PYXT9 | Yes | 3.2 |
| 5 | D2PI9AHQ3WOV | D2PI9AHQ3WOV | Yes | 14.19 |
| 6 | L8JADRD8QBVK | L8JADRD8QBVK | Yes | 9.26 |
| 7 | PU9AH57VFNYX | PU9AH57VFNYX | Yes | 13.26 |
| 8 | 98J0KSJ7QDLE | 98J0KSJ7QDLE | Yes | 6.52 |
| 9 | 13Y8SLZ7KDV2 | 13Y8SLZ7KDV2 | Yes | 4.08 |
| 10 | AUYCTXE7POUA | AUYCTXE7POUA | Yes | 13.01 |
| 11 | 0FQ1PRUEF90A | 0FQ1PRUEF90A | Yes | 4.05 |
| 12 | KRWMZN2GS2PB | KRWMZN2GS2PB | Yes | 13.0 |
| 13 | 4VFYO27R74MY | 4VFYO27R74MY | Yes | 10.27 |
| 14 | V38WV8G3DGMB | V38WV8G3DGMB | Yes | 13.49 |
| 15 | 1FFP4MCMOLV8 | 1FFP4MCMOLV8 | Yes | 10.82 |
| 16 | FHWYCTO0F3JD | FHWYCTO0F3JD | Yes | 13.04 |
| 17 | DMO9UP6ZE7H4 | DMO9UP6ZE7H4 | Yes | 3.64 |
| 18 | WFYZ7BP3AZE4 | WFYZ7BP3AZE4 | Yes | 2.86 |
| 19 | ZX9Z336IVSW6 | ZX9Z336IVSW6 | Yes | 3.32 |
| 20 | TYZ07N425VCO | TYZ07N425VCO | Yes | 4.85 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 36 | 36 | Yes | 12.6 |
| 2 | 4096 | 4096 | Yes | 20.84 |
| 3 | 9 | 9 | Yes | 6.76 |
| 4 | 243 | 243 | Yes | 3.89 |
| 5 | 26 | 26 | Yes | 10.65 |
| 6 | 67 | 67 | Yes | 4.45 |
| 7 | 28 | 28 | Yes | 5.51 |
| 8 | 65 | 65 | Yes | 6.77 |
| 9 | 1 | 1 | Yes | 10.91 |
| 10 | 9 | 9 | Yes | 15.16 |
| 11 | 63 | 63 | Yes | 5.73 |
| 12 | 7 | 7 | Yes | 8.15 |
| 13 | 5 | 16 | No | 23.16 |
| 14 | 1440 | 1440 | Yes | 7.53 |
| 15 | 6 | 6 | Yes | 6.77 |
| 16 | 44 | 44 | Yes | 16.08 |
| 17 | 793 | 793 | Yes | 3.74 |
| 18 | 3 | 3 | Yes | 16.28 |
| 19 | 19 | 19 | Yes | 14.28 |
| 20 | 64 | 64 | Yes | 16.97 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )\\)//__) | )\\)//__) | Yes | 9.98 |
| 2 | )(\/((/(< | )(\/((/( | No | 3.55 |
| 3 | (/)//_) _ | (/)//_) _ | Yes | 4.26 |
| 4 | )\)(/<_/) | )\)(/<_/) | Yes | 4.95 |
| 5 | /)((\__\\ | /)((\__\\ | Yes | 5.44 |
| 6 | / (<)\\/  | / (<)\\/ | No | 23.57 |
| 7 | /\\__/_(( | /\\__/_(( | Yes | 14.33 |
| 8 | <)\( <\_\ | <)\( <\_\ | Yes | 11.39 |
| 9 |  _ \_\()\ | _ \_\()\ | No | 7.72 |
| 10 |  /_( _\_  | /_( _\_ | No | 16.9 |
| 11 |  ()<<\)_) | ()<<\)_) | No | 14.18 |
| 12 | _( ( <//( | _( ( <//( | Yes | 15.96 |
| 13 | \)((()))/ | \)((()))/ | Yes | 13.08 |
| 14 | )/_\)(/ _ | )/_\)(/ _ | Yes | 13.97 |
| 15 | /)//_/\() | /)//_/\() | Yes | 13.54 |
| 16 | ) <\_/\/_ | ) <\_/\/_ | Yes | 6.84 |
| 17 | () (\(\\_ | () (\(\\_ | Yes | 14.04 |
| 18 | <\ \/_< / | <\ \/_< / | Yes | 4.67 |
| 19 | )(<_/( _< | )(<_/( _ | No | 7.49 |
| 20 | ///\ ((<) | ///\ ((<) | Yes | 14.16 |
