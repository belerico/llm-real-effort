# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-26 16:05:59

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
| sudoku_game | 4681 | 40341 | 45022 | 3 | 17 | 29.60 | 591.99 |
| add_numbers | 2520 | 3407 | 5927 | 20 | 0 | 12.14 | 242.9 |
| counting_zeros | 5592 | 35120 | 40712 | 18 | 2 | 29.11 | 582.18 |
| task_decoding | 3800 | 4811 | 8611 | 20 | 0 | 14.78 | 295.57 |
| task_summation | 3844 | 9933 | 13777 | 20 | 0 | 15.88 | 317.67 |
| task_transcription | 2505 | 2609 | 5114 | 20 | 0 | 12.32 | 246.47 |
| task_sequences | 2494 | 6046 | 8540 | 19 | 1 | 11.79 | 235.88 |
| string_entry | 2816 | 5568 | 8384 | 16 | 4 | 13.11 | 262.16 |
| **TOTAL** | **28252** | **107835** | **136087** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 6 3 5 1 4 6 4 5 2 6 5 5 6 | 4 6 4 1 5 5 6 4 5 6 2 6 5 5 6 | No | 30.18 |
| 2 | 4 6 1 6 5 4 1 6 3 5 2 1 1 3 | 4 6 1 5 6 4 6 3 1 2 1 5 | No | 31.49 |
| 3 | 2 5 6 4 4 1 2 3 5 4 6 4 1 5 | 2 6 5 4 4 1 2 3 5 4 6 4 1 5 | No | 19.25 |
| 4 | 1 5 6 3 4 1 2 4 1 2 6 1 2 3 | 1 5 6 3 4 1 2 1 4 2 6 2 3 1 2 | No | 29.99 |
| 5 | 1 5 6 4 6 1 6 1 5 1 5 5 2 4 | To solve the Sudoku, we need to place the numbers 1-6 in each row, column, and 3x2 box exactly once. (Note: Based on the grid's layout and numbers, the boxes are 3 rows by 2 columns, despite the ASCII separator placement, since a 2x3 box would contain duplicate 4s in the second block).  Let' | No | 30.23 |
| 6 | 5 6 4 6 5 3 6 5 2 2 4 3 4 2 | To solve the 6x6 Sudoku puzzle, we first need to determine the layout of the boxes. Based on the grid lines (`-----+-----`), the grid is divided into 3 rows and 2 columns of boxes, meaning each box is 3 rows tall and 2 columns wide (a 3x2 box layout).  Let's fill in the grid step-by-step | No | 30.97 |
| 7 | 3 2 3 3 5 4 1 1 3 4 2 3 6 2 | To solve the 6×6 Sudoku puzzle, we need to ensure that every row, column, and 2×3 box contains the numbers 1 through 6 exactly once.   Let's deduce the missing numbers step-by-step: 1. **Row 1:** The given numbers are 4, 6, 1, 2, and 5. The | No | 30.18 |
| 8 | 1 4 2 3 3 4 6 6 3 5 4 4 3 6 | To solve the 6x6 Sudoku puzzle, we can deduce the missing numbers step by step. The grid is divided into six 2x3 boxes.   Here is the initial grid: R1: . 5 . \| 6 . . R2: 6 2 1 \| . 4 5 R3: 3 . 2 \| | No | 30.23 |
| 9 | 3 2 1 3 1 2 5 5 1 4 3 3 1 2 | To solve the Sudoku puzzle, we can deduce the missing numbers step by step:  1. **Row 3:** The given numbers are 6 2 4 \| . 3 5. The missing number is 1, so R3C4 = **1**. 2. **Row 4:** The given numbers are . 4 6 \| 3 . 1 | No | 28.38 |
| 10 | 5 4 6 2 6 4 5 6 5 3 3 6 4 1 | To solve the Sudoku puzzle, we need to fill in the missing numbers such that each row, column, and 3×2 box contains the numbers 1-6 exactly once.   Let's deduce the missing values step-by-step: 1. **Column 2** has `3, 4, 5, 2, 1, .`, so the missing | No | 31.18 |
| 11 | 2 1 4 3 1 5 5 4 2 6 2 2 1 4 | To solve the 6x6 Sudoku puzzle, we can deduce the missing numbers step by step using the rules of Sudoku (each row, column, and 2x3 box must contain the numbers 1-6 exactly once).  **Row 1:** `_ 3 5 \| _ 4 6` **Row 2:** `_ 6 _ | No | 19.32 |
| 12 | 4 2 3 6 3 6 1 3 3 2 2 6 2 1 | 4 2 6 3 3 6 1 3 2 3 2 2 1 6 1 | No | 32.07 |
| 13 | 5 6 3 2 6 1 3 4 5 6 4 5 6 2 | To solve the Sudoku puzzle, we need to fill the empty cells so that every row, column, and region contains the numbers 1 through 6 exactly once.   Let's analyze the grid step by step based on standard Sudoku rules (noting the regions defined by the grid lines):  **Row 1:** 6 2 1 \| 3 4 | No | 27.11 |
| 14 | 5 3 6 2 3 2 6 3 2 6 6 5 4 3 | 5 3 6 2 3 2 6 2 6 3 6 3 4 3 4 6 | No | 30.04 |
| 15 | 2 1 5 6 4 2 6 1 1 5 2 4 3 2 | 2 1 5 6 4 2 6 1 1 5 2 4 3 2 | Yes | 17.34 |
| 16 | 1 4 6 1 2 6 2 3 1 5 6 1 4 2 | To solve the Sudoku puzzle, we can determine the missing numbers by ensuring each row, column, and block contains the numbers 1 to 6 exactly once.   Although the visual grid implies 2x3 blocks, checking Row 2 (`. 2 4 \| 5 1 3`) reveals the missing number must be 6. If the blocks were 2 | No | 30.79 |
| 17 | 1 5 2 2 1 4 3 5 3 1 6 1 3 2 | 1 5 2 2 1 4 3 5 3 1 6 1 3 2 | Yes | 29.81 |
| 18 | 3 5 2 6 5 1 1 3 6 5 3 6 1 3 | 5 3 2 6 1 5 1 6 3 3 1 6 5 3 1 5 3 6 | No | 29.83 |
| 19 | 2 5 6 1 5 4 6 4 1 5 6 1 1 2 | 2 5 6 1 5 4 6 4 1 5 6 1 2 1 2 | No | 30.21 |
| 20 | 6 1 6 2 1 5 3 1 4 6 2 6 6 1 | 6 1 6 2 1 5 3 1 4 6 2 6 6 1 | Yes | 53.35 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1600 | 1600 | Yes | 4.05 |
| 2 | 1430 | 1430 | Yes | 15.46 |
| 3 | 1743 | 1743 | Yes | 14.5 |
| 4 | 1681 | 1681 | Yes | 20.17 |
| 5 | 2746 | 2746 | Yes | 5.99 |
| 6 | 835 | 835 | Yes | 8.86 |
| 7 | 1650 | 1650 | Yes | 24.34 |
| 8 | 1166 | 1166 | Yes | 4.39 |
| 9 | 2227 | 2227 | Yes | 15.0 |
| 10 | 1873 | 1873 | Yes | 15.5 |
| 11 | 598 | 598 | Yes | 14.66 |
| 12 | 1403 | 1403 | Yes | 10.49 |
| 13 | 1426 | 1426 | Yes | 22.1 |
| 14 | 728 | 728 | Yes | 3.88 |
| 15 | 1620 | 1620 | Yes | 4.33 |
| 16 | 1915 | 1915 | Yes | 5.77 |
| 17 | 1629 | 1629 | Yes | 4.39 |
| 18 | 1441 | 1441 | Yes | 8.79 |
| 19 | 1431 | 1431 | Yes | 14.16 |
| 20 | 1481 | 1481 | Yes | 26.07 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 57 | 57 | Yes | 48.62 |
| 2 | 56 | 56 | Yes | 24.39 |
| 3 | 35 | 35 | Yes | 18.06 |
| 4 | 43 | 43 | Yes | 25.05 |
| 5 | 58 | 57 | No | 27.95 |
| 6 | 61 | 61 | Yes | 37.05 |
| 7 | 40 | 40 | Yes | 29.25 |
| 8 | 67 | 67 | Yes | 30.11 |
| 9 | 63 | 63 | Yes | 31.78 |
| 10 | 46 | 46 | Yes | 27.51 |
| 11 | 55 | 55 | Yes | 29.21 |
| 12 | 53 | 53 | Yes | 28.69 |
| 13 | 54 | 54 | Yes | 29.99 |
| 14 | 60 | 60 | Yes | 31.26 |
| 15 | 60 | 60 | Yes | 28.41 |
| 16 | 70 | 68 | No | 24.41 |
| 17 | 52 | 52 | Yes | 30.66 |
| 18 | 71 | 71 | Yes | 26.94 |
| 19 | 56 | 56 | Yes | 27.33 |
| 20 | 42 | 42 | Yes | 25.51 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | IJRPSBC | IJRPSBC | Yes | 9.81 |
| 2 | BITXDFN | BITXDFN | Yes | 10.61 |
| 3 | CBRGDWN | CBRGDWN | Yes | 21.62 |
| 4 | WBZISXE | WBZISXE | Yes | 16.42 |
| 5 | FMOUWXT | FMOUWXT | Yes | 5.08 |
| 6 | UIZWJTD | UIZWJTD | Yes | 5.39 |
| 7 | EMGLRFX | EMGLRFX | Yes | 16.46 |
| 8 | OPMBTDC | OPMBTDC | Yes | 19.57 |
| 9 | WDKOCSF | WDKOCSF | Yes | 27.4 |
| 10 | EBHTSPV | EBHTSPV | Yes | 14.06 |
| 11 | NXPRBVH | NXPRBVH | Yes | 8.1 |
| 12 | XGOYRHA | XGOYRHA | Yes | 17.33 |
| 13 | VGYNFJT | VGYNFJT | Yes | 14.13 |
| 14 | XDOECGZ | XDOECGZ | Yes | 17.76 |
| 15 | SMQIBEF | SMQIBEF | Yes | 14.47 |
| 16 | ZXOVTFM | ZXOVTFM | Yes | 6.02 |
| 17 | ZWIOVJL | ZWIOVJL | Yes | 8.82 |
| 18 | XEDZSHR | XEDZSHR | Yes | 5.26 |
| 19 | GEIWYDZ | GEIWYDZ | Yes | 6.77 |
| 20 | PQJFEUO | PQJFEUO | Yes | 50.46 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.1, 8.9] | 8.9 1.1 | Yes | 6.85 |
| 2 | [3.9, 6.1] | 3.9 6.1 | Yes | 8.79 |
| 3 | [2.2, 7.8] | 2.2 7.8 | Yes | 16.31 |
| 4 | [0.5, 9.5] | 0.5 9.5 | Yes | 19.02 |
| 5 | [1.3, 8.7] | 1.3 8.7 | Yes | 19.17 |
| 6 | [2.1, 7.9] | 7.9 2.1 | Yes | 17.7 |
| 7 | [1.1, 8.9] | 1.1 8.9 | Yes | 18.03 |
| 8 | [2.3, 7.7] | 2.3 7.7 | Yes | 12.24 |
| 9 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.78 |
| 10 | [1.8, 8.2] | 1.8 8.2 | Yes | 7.52 |
| 11 | [3.4, 6.6] | 6.6 3.4 | Yes | 18.11 |
| 12 | [0.1, 9.9] | 0.1 9.9 | Yes | 53.55 |
| 13 | [1.8, 8.2] | 1.8 8.2 | Yes | 20.0 |
| 14 | [4.4, 5.6] | 4.4 5.6 | Yes | 8.23 |
| 15 | [2.3, 7.7] | 2.3 7.7 | Yes | 20.97 |
| 16 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.3 |
| 17 | [0.6, 9.4] | 0.6 9.4 | Yes | 17.34 |
| 18 | [1.3, 8.7] | 1.3 8.7 | Yes | 18.05 |
| 19 | [1.0, 9.0] | 9.0 1.0 | Yes | 7.53 |
| 20 | [2.0, 8.0] | 8.0 2.0 | Yes | 12.15 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PXQ993BCTA4D | PXQ993BCTA4D | Yes | 14.01 |
| 2 | 850SGZZRPC22 | 850SGZZRPC22 | Yes | 7.35 |
| 3 | 4QAVV7ETKBJW | 4QAVV7ETKBJW | Yes | 14.05 |
| 4 | GO1R5ZLKV1GB | GO1R5ZLKV1GB | Yes | 3.96 |
| 5 | FNR24LDDS1LR | FNR24LDDS1LR | Yes | 7.09 |
| 6 | HY9AJRMICD5N | HY9AJRMICD5N | Yes | 4.22 |
| 7 | DDI343OFIDP4 | DDI343OFIDP4 | Yes | 5.3 |
| 8 | O3IZW4S42OQ7 | O3IZW4S42OQ7 | Yes | 58.52 |
| 9 | M35NKBN97UFD | M35NKBN97UFD | Yes | 7.33 |
| 10 | 64MBRETQEFXM | 64MBRETQEFXM | Yes | 18.5 |
| 11 | VDOM29CVJPKH | VDOM29CVJPKH | Yes | 13.76 |
| 12 | 6M98EGP1IFHP | 6M98EGP1IFHP | Yes | 3.98 |
| 13 | LI8GIUFKZTLV | LI8GIUFKZTLV | Yes | 4.83 |
| 14 | BWHYHODQSM6C | BWHYHODQSM6C | Yes | 6.15 |
| 15 | TSV2UMCXOAW8 | TSV2UMCXOAW8 | Yes | 16.66 |
| 16 | 3F43Q0PSNPQ8 | 3F43Q0PSNPQ8 | Yes | 23.82 |
| 17 | QBUCVXENPE7W | QBUCVXENPE7W | Yes | 13.34 |
| 18 | YS11W5QSL945 | YS11W5QSL945 | Yes | 4.89 |
| 19 | WLJ4UHE7R9XO | WLJ4UHE7R9XO | Yes | 3.92 |
| 20 | 2CLGQ9NF1YIM | 2CLGQ9NF1YIM | Yes | 14.79 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 10.58 |
| 2 | 10 | 10 | Yes | 23.75 |
| 3 | 44 | 44 | Yes | 5.55 |
| 4 | 3 | 3 | Yes | 16.21 |
| 5 | 26 | 26 | Yes | 16.98 |
| 6 | 243 | 243 | Yes | 5.22 |
| 7 | 3 | 3 | Yes | 14.26 |
| 8 | 20 | 20 | Yes | 9.6 |
| 9 | 4096 | To find the next number in the sequence, let's look at the relationship between the consecutive terms by finding the multiplier used to get from one term to the next:  - 4 ÷ 1 = **4** - 16 ÷ 4 = **4** - 256 ÷ 16 = **16** - 1024 ÷ 2 | No | 30.5 |
| 10 | 65 | 65 | Yes | 7.22 |
| 11 | 198 | 198 | Yes | 9.39 |
| 12 | 23 | 23 | Yes | 5.55 |
| 13 | 67 | 67 | Yes | 4.13 |
| 14 | 16 | 16 | Yes | 14.12 |
| 15 | 9 | 9 | Yes | 13.99 |
| 16 | 5 | 5 | Yes | 8.15 |
| 17 | 60 | 60 | Yes | 13.72 |
| 18 | 6 | 6 | Yes | 4.95 |
| 19 | 9 | 9 | Yes | 8.01 |
| 20 | 48 | 48 | Yes | 13.99 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | </<<\\\<) | </<<\\\<) | Yes | 17.54 |
| 2 | ()((_\/\_ | ()((_\/\_ | Yes | 3.7 |
| 3 | \/ )/\_// | \/ )/\_// | Yes | 10.78 |
| 4 | /(_)\ )<( | /(_)\ )<( | Yes | 7.21 |
| 5 | \_</<(/__ | \_</<(/__ | Yes | 15.66 |
| 6 | \\ _)<<\  | \\ _)<<\ | No | 20.63 |
| 7 | /(( <\)_\ | /(( <\)_\ | Yes | 14.83 |
| 8 | ) /)(\_<\ | ) /)(\_<\ | Yes | 6.16 |
| 9 | (_)//) \< | (_)//) \< | Yes | 3.3 |
| 10 |  )_(\ //) | )_(\ //) | No | 5.77 |
| 11 | (</<) /__ | (</<) /__ | Yes | 7.23 |
| 12 | (\\_\(/ ) | (\\_\(/ ) | Yes | 20.08 |
| 13 |  )/<_( (\ | )/<_( (\ | No | 10.95 |
| 14 | ___/_/< \ | ___/_/< \ | Yes | 16.21 |
| 15 |  )/\_<_(_ | )/\_<_(_ | No | 15.71 |
| 16 | <( _\/_\( | <( _\/_\( | Yes | 43.12 |
| 17 | _/<\ /__( | _/<\ /__( | Yes | 5.26 |
| 18 | //</\\<_\ | //</\\<_\ | Yes | 15.8 |
| 19 | // < ((</ | // < ((</ | Yes | 11.14 |
| 20 | _\</_\_<_ | _\</_\_<_ | Yes | 11.06 |
