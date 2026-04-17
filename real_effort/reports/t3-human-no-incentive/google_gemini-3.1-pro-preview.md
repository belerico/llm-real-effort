# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-19 03:13:48

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

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 25720 | 40644 | 66364 | 3 | 17 | 29.55 | 591.23 |
| add_numbers | 25064 | 4016 | 29080 | 20 | 0 | 11.84 | 236.98 |
| counting_zeros | 23598 | 36097 | 59695 | 17 | 3 | 32.20 | 644.24 |
| task_decoding | 25258 | 8594 | 33852 | 20 | 0 | 12.29 | 246.05 |
| task_summation | 25036 | 9878 | 34914 | 20 | 0 | 11.99 | 239.99 |
| task_transcription | 24631 | 7591 | 32222 | 15 | 5 | 12.89 | 257.98 |
| task_sequences | 3162 | 5748 | 8910 | 20 | 0 | 8.36 | 167.18 |
| **TOTAL** | **152469** | **112568** | **265037** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 2 2 1 4 3 6 1 3 5 6 4 3 1 | 6 2 4 2 1 3 6 1 3 5 6 4 3 1 | No | 28.61 |
| 2 | 5 4 3 2 3 6 6 5 2 6 6 1 5 2 | 5 4 3 2 3 6 6 5 2 6 6 1 5 2 | Yes | 28.78 |
| 3 | 3 6 2 1 5 4 3 2 5 6 6 2 4 5 | To solve the Sudoku puzzle, we need to fill the 6x6 grid so that each row, column, and 2x3 box contains the numbers 1-6 exactly once.   Let's transcribe the given grid: Row 1: 5, _, _, 4, _, _ Row 2: 2, 6, 1, | No | 28.87 |
| 4 | 3 1 1 4 6 5 1 5 6 4 1 6 2 5 | To solve the 6×6 Sudoku puzzle, we need to fill in the grid so that each row, column, and 3×2 box contains the numbers 1 through 6 exactly once.   Based on the grid, the boxes are 3 rows by 2 columns.  **Initial Grid:** Row 1: 4, 6, _, 5, _, | No | 29.49 |
| 5 | 1 5 4 3 2 1 5 6 5 4 3 4 2 6 | To solve the puzzle, we need to fill the 6×6 grid so that each row, each column, and each 2×3 box contains the numbers 1 to 6 exactly once.  Based on the grid provided: Row 1: 2 3 6 \| _ _ 4 Row 2: _ 5 _ \| _ 6 1 Row | No | 29.94 |
| 6 | 4 5 1 4 6 3 1 2 2 6 5 4 6 4 | 2 and R6C1 is 6! Ah! R5C1 is 2, R6C1 is 6. So C1 has 3, 5, 4, 1, 2, 6. So 4 is in R3C1. Then where is 4 in the bottom left block? R5C1=2, R | No | 29.34 |
| 7 | 6 1 2 1 1 4 5 2 1 4 3 3 1 3 | To solve the 6×6 Sudoku puzzle, we need to ensure that every row, column, and 2×3 box contains the numbers 1 through 6 exactly once.   By deducing the missing values step-by-step: - **Row 6** is missing only a 3 in the first column. - **Column 1** is now missing only a | No | 29.15 |
| 8 | 6 4 4 1 2 5 3 4 5 4 5 6 4 1 | To solve the Sudoku puzzle, we need to fill the 6x6 grid so that each row, column, and 2x3 box contains the numbers 1-6 exactly once.  Let's determine the missing numbers step by step: **Row 1:** 2 5 3 _ 1 _  Missing: 4, 6. Since Column | No | 29.69 |
| 9 | 1 2 5 4 3 5 3 5 2 6 6 2 4 5 | To solve the Sudoku puzzle, we need to fill in the empty cells so that every row, column, and 2×3 box contains the numbers 1 through 6 exactly once.  1. **Row 1:** The missing numbers are 1, 2, and 5. Looking at the top-left box, the missing numbers are 1 and 2. Since column | No | 29.51 |
| 10 | 2 4 1 4 3 3 2 1 6 1 5 3 4 6 | To solve the puzzle, we first determine the missing numbers in each row and column, using the standard Sudoku rules (each number 1-6 must appear exactly once in each row, column, and 2x3 box).   By analyzing the grid, we can deduce the boxes are 3 rows high by 2 columns wide (despite the misleading thick grid lines), as Column 3 contains | No | 29.96 |
| 11 | 4 2 4 6 3 6 3 4 5 1 2 1 2 2 | 4 2 4 6 3 6 3 4 5 1 2 1 2 2 | Yes | 29.33 |
| 12 | 6 3 6 4 5 4 4 3 6 3 4 2 5 1 | 6 6 3 4 5 4 4 6 4 6 3 4 1 5 2 1 5 1 2 5 1 | No | 28.77 |
| 13 | 3 1 6 6 1 3 1 6 5 3 4 6 1 5 | To solve the 6×6 Sudoku puzzle, we need to fill in the missing numbers so that each row, column, and 3×2 box contains the numbers 1-6 exactly once.   Let's write down the initial grid based on the image: Row 1: _ 5 2 \| 4 _ _ Row 2: _ 2 | No | 29.14 |
| 14 | 2 6 4 2 3 5 6 2 5 1 3 2 4 6 | 2 6 4 2 3 5 6 2 5 1 3 2 4 6 | Yes | 28.74 |
| 15 | 6 1 3 4 1 5 2 1 2 1 5 4 5 1 | To solve the 6×6 Sudoku puzzle, we first identify the given numbers from the image and the grid's structure. The grid is divided into six 2×3 boxes (2 rows and 3 columns each).  Here is the initial grid based on the image: Row 1: 5, 2, 4 \| _, _, 3 Row 2: | No | 30.0 |
| 16 | 4 5 5 2 6 2 5 1 1 3 2 6 1 5 | To solve the Sudoku puzzle, we need to fill in the grid so that each row, column, and 2×3 box contains the numbers 1-6 exactly once.  Here is the initial grid based on the image: Row 1: 3, _, 1 \| 6, _, 2 Row 2: _, 1, _ \| 4, | No | 30.57 |
| 17 | 6 2 1 5 2 4 1 3 4 3 5 5 3 2 | To solve the 6×6 Sudoku puzzle, we need to fill in the empty cells such that every row, column, and 2×3 box contains the numbers 1 through 6 exactly once.  Let's deduce the numbers step by step: 1. **Column 2** has the numbers 4, 5, 6, 2, and 3. | No | 29.31 |
| 18 | 3 2 6 1 6 4 1 1 4 2 3 3 5 1 | To solve the 6×6 Sudoku puzzle, we need to fill the grid so that each row, each column, and each of the six 3×2 boxes (3 rows high, 2 columns wide) contains the numbers 1 through 6 exactly once.  Here is the initial grid based on the image: Row 1: _ 4 \| _ _ \| 5 | No | 31.58 |
| 19 | 2 5 4 2 5 1 4 6 4 2 5 2 1 4 | To solve the 6×6 Sudoku puzzle, we need to fill in the grid so that each row, column, and 2×3 box contains the numbers 1 through 6 exactly once.   Let's analyze the grid based on the provided numbers: **Row 1:** 1 6 4 \| _ 3 _ **Row 2:** _ | No | 29.41 |
| 20 | 2 4 2 5 5 1 3 3 6 2 5 2 6 3 | To solve the 6×6 Sudoku puzzle, we need to fill in the missing numbers so that each row, each column, and each 3×2 box (3 rows by 2 columns) contains the numbers 1 through 6 exactly once.   Looking closely at the grid's bold lines, the boxes are 3 rows high and 2 columns wide.  **Given | No | 30.83 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 923 | 923 | Yes | 6.34 |
| 2 | 2001 | 2001 | Yes | 10.49 |
| 3 | 1666 | 1666 | Yes | 15.24 |
| 4 | 2151 | 2151 | Yes | 15.66 |
| 5 | 945 | 945 | Yes | 5.71 |
| 6 | 1192 | 1192 | Yes | 5.56 |
| 7 | 2289 | 2289 | Yes | 15.61 |
| 8 | 1414 | 1414 | Yes | 14.99 |
| 9 | 1545 | 1545 | Yes | 15.57 |
| 10 | 710 | 710 | Yes | 15.62 |
| 11 | 1016 | 1016 | Yes | 5.57 |
| 12 | 2467 | 2467 | Yes | 15.64 |
| 13 | 1842 | 1842 | Yes | 15.38 |
| 14 | 1622 | 1622 | Yes | 6.54 |
| 15 | 2156 | 2156 | Yes | 14.86 |
| 16 | 1493 | 1493 | Yes | 14.49 |
| 17 | 2093 | 2093 | Yes | 5.57 |
| 18 | 1684 | 1684 | Yes | 15.41 |
| 19 | 2000 | 2000 | Yes | 15.62 |
| 20 | 1865 | 1865 | Yes | 7.01 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 67 | 67 | Yes | 28.32 |
| 2 | 42 | 42 | Yes | 28.16 |
| 3 | 46 | 46 | Yes | 27.82 |
| 4 | 68 | 68 | Yes | 28.43 |
| 5 | 40 | 40 | Yes | 24.43 |
| 6 | 50 | TIMEOUT | No | 120.03 |
| 7 | 54 | 53 | No | 27.78 |
| 8 | 37 | 37 | Yes | 24.1 |
| 9 | 66 | 66 | Yes | 28.6 |
| 10 | 52 | 52 | Yes | 27.7 |
| 11 | 64 | 65 | No | 27.55 |
| 12 | 72 | 72 | Yes | 28.43 |
| 13 | 60 | 60 | Yes | 27.51 |
| 14 | 36 | 36 | Yes | 27.32 |
| 15 | 36 | 36 | Yes | 28.42 |
| 16 | 69 | 69 | Yes | 27.59 |
| 17 | 44 | 44 | Yes | 27.94 |
| 18 | 53 | 53 | Yes | 28.54 |
| 19 | 47 | 47 | Yes | 28.42 |
| 20 | 36 | 36 | Yes | 26.83 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ROTDHUF | ROTDHUF | Yes | 16.74 |
| 2 | ARHBPWC | ARHBPWC | Yes | 17.73 |
| 3 | XMLAEIQ | XMLAEIQ | Yes | 16.13 |
| 4 | DMOKRHL | DMOKRHL | Yes | 8.18 |
| 5 | SNAZQFE | SNAZQFE | Yes | 6.02 |
| 6 | HKARXUQ | HKARXUQ | Yes | 8.36 |
| 7 | BWSHVYR | BWSHVYR | Yes | 9.8 |
| 8 | QXZMWJD | QXZMWJD | Yes | 8.49 |
| 9 | PSWIBLZ | PSWIBLZ | Yes | 8.78 |
| 10 | BHQRLIU | BHQRLIU | Yes | 17.16 |
| 11 | RUHZPVC | RUHZPVC | Yes | 9.81 |
| 12 | DULZEJX | DULZEJX | Yes | 8.26 |
| 13 | IEBHYLR | IEBHYLR | Yes | 24.34 |
| 14 | DEKIBVP | DEKIBVP | Yes | 18.24 |
| 15 | LDUMETN | LDUMETN | Yes | 17.36 |
| 16 | TAOQBKV | TAOQBKV | Yes | 10.9 |
| 17 | BMVQTNG | BMVQTNG | Yes | 8.92 |
| 18 | OBXTEFC | OBXTEFC | Yes | 15.64 |
| 19 | WDRJKCN | WDRJKCN | Yes | 8.44 |
| 20 | IWMHFBA | IWMHFBA | Yes | 6.54 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.1, 7.9] | 7.9 2.1 | Yes | 10.37 |
| 2 | [4.5, 5.5] | 4.5 5.5 | Yes | 16.92 |
| 3 | [2.9, 7.1] | 2.9 7.1 | Yes | 6.77 |
| 4 | [3.9, 6.1] | 6.1 3.9 | Yes | 9.5 |
| 5 | [1.1, 8.9] | 8.9 1.1 | Yes | 9.3 |
| 6 | [2.7, 7.3] | 7.3 2.7 | Yes | 9.02 |
| 7 | [0.9, 9.1] | 9.1 0.9 | Yes | 10.26 |
| 8 | [4.5, 5.5] | 5.5 4.5 | Yes | 9.91 |
| 9 | [2.7, 7.3] | 2.7 7.3 | Yes | 8.93 |
| 10 | [1.3, 8.7] | 8.7 1.3 | Yes | 8.16 |
| 11 | [3.6, 6.4] | 3.6 6.4 | Yes | 16.73 |
| 12 | [3.7, 6.3] | 3.7 6.3 | Yes | 9.71 |
| 13 | [2.2, 7.8] | 2.2 7.8 | Yes | 16.92 |
| 14 | [1.1, 8.9] | 1.1 8.9 | Yes | 17.91 |
| 15 | [2.2, 7.8] | 2.2 7.8 | Yes | 9.38 |
| 16 | [2.6, 7.4] | 7.4 2.6 | Yes | 19.03 |
| 17 | [4.4, 5.6] | 5.6 4.4 | Yes | 18.94 |
| 18 | [0.9, 9.1] | 0.9 9.1 | Yes | 16.79 |
| 19 | [2.8, 7.2] | 7.2 2.8 | Yes | 7.69 |
| 20 | [0.5, 9.5] | 0.5 9.5 | Yes | 7.56 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZG7QUQFZ0B63 | ZG7OUQFZOB63 | No | 12.76 |
| 2 | MOKG268R1DO6 | MOKG268R1D06 | No | 10.06 |
| 3 | E9HEF0KZBX78 | E9HEF0KZBX78 | Yes | 6.84 |
| 4 | XYNZ2S6LKVVJ | XYNZ2S6LKVVJ | Yes | 15.25 |
| 5 | A48FU2LXW2IG | A48FU2LXW2IG | Yes | 14.55 |
| 6 | G22IJBRO1XAT | G22IJBRO1XAT | Yes | 16.08 |
| 7 | ACE0UKEHZX57 | ACE0UKEHZX57 | Yes | 18.7 |
| 8 | PENC0DJMZ1XV | PENC0DJMZ1XV | Yes | 17.55 |
| 9 | EIXJ9HLMTGIF | EIXJ9HLMTGIF | Yes | 13.84 |
| 10 | 606T0EP55M78 | 606T0EP55M78 | Yes | 16.01 |
| 11 | KZMAID1DVTUM | KZMAID1DVTUM | Yes | 5.69 |
| 12 | 4XIND5O3NG7I | 4XIND503NG7I | No | 8.71 |
| 13 | Y1X0KBSYTN0O | Y1X0KBSYTN00 | No | 10.02 |
| 14 | DWWKNTZMVPDO | DWWKNTZMVPDO | Yes | 15.31 |
| 15 | 01IWVY0EB5J2 | 01IWVY0EB5J2 | Yes | 17.12 |
| 16 | 66T084PMR37C | 66T084PMR37C | Yes | 10.38 |
| 17 | G2W17WPBO9R2 | G2W17WPB09R2 | No | 10.44 |
| 18 | ACDX9OR6HJHO | ACDX9OR6HJHO | Yes | 20.53 |
| 19 | ITILI1QMBCQH | ITILI1QMBCQH | Yes | 7.55 |
| 20 | I2QJPMJLZ2RM | I2QJPMJLZ2RM | Yes | 10.48 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 7.41 |
| 2 | 31 | 31 | Yes | 13.28 |
| 3 | 1 | 1 | Yes | 4.56 |
| 4 | 67 | 67 | Yes | 3.96 |
| 5 | 3 | 3 | Yes | 4.47 |
| 6 | 20 | 20 | Yes | 17.94 |
| 7 | 1440 | 1440 | Yes | 4.22 |
| 8 | 16 | 16 | Yes | 6.71 |
| 9 | 4096 | 4096 | Yes | 21.28 |
| 10 | 3 | 3 | Yes | 9.17 |
| 11 | 60 | 60 | Yes | 5.1 |
| 12 | 44 | 44 | Yes | 5.96 |
| 13 | 36 | 36 | Yes | 5.01 |
| 14 | 9 | 9 | Yes | 4.62 |
| 15 | 39 | 39 | Yes | 5.4 |
| 16 | 4 | 4 | Yes | 13.59 |
| 17 | 26 | 26 | Yes | 14.4 |
| 18 | 28 | 28 | Yes | 5.26 |
| 19 | 10 | 10 | Yes | 6.07 |
| 20 | 7680 | 7680 | Yes | 8.78 |
