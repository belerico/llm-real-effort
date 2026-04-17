# Benchmark Report — claude-opus-4.5

- **Model**: `anthropic/claude-opus-4.5`
- **Date**: 2026-03-27 10:19:00

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
| sudoku_game | 6340 | 38201 | 44541 | 13 | 7 | 33.98 | 679.73 |
| add_numbers | 3534 | 1772 | 5306 | 19 | 1 | 9.88 | 197.63 |
| counting_zeros | 5040 | 25055 | 30095 | 14 | 6 | 16.85 | 337.08 |
| task_decoding | 5040 | 5605 | 10645 | 20 | 0 | 7.57 | 151.48 |
| task_summation | 5100 | 14546 | 19646 | 20 | 0 | 13.55 | 271.09 |
| task_transcription | 3878 | 2932 | 6810 | 20 | 0 | 6.11 | 122.15 |
| task_sequences | 3781 | 8306 | 12087 | 19 | 1 | 11.10 | 222.0 |
| string_entry | 4261 | 4197 | 8458 | 13 | 7 | 10.44 | 208.77 |
| **TOTAL** | **36974** | **100614** | **137588** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 5 4 2 3 4 5 3 2 5 4 1 5 2 | 1 5 4 2 3 4 5 3 2 5 4 1 5 2 | Yes | 35.6 |
| 2 | 2 4 3 1 6 1 6 1 3 6 6 5 3 3 | 2 4 3 1 6 1 6 1 3 6 6 5 3 3 | Yes | 28.45 |
| 3 | 4 6 1 5 1 6 2 6 5 6 3 6 4 1 | 4 6 1 5 1 6 2 6 5 6 3 6 4 1 | Yes | 28.77 |
| 4 | 2 1 1 4 5 2 6 3 5 3 2 4 4 3 | 2 1 1 4 5 2 6 3 5 3 2 4 4 3 | Yes | 37.44 |
| 5 | 3 3 4 1 2 2 6 2 5 6 2 1 3 6 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 1:** 4 2 1 5 6 . → Missing 3 **R1C6 = 3**  **Row 2:** . 5 6 . . .  - Column 1 has: 4,6,1,5,2 → Missing 3, so **R2C1 = 3** - Top-right box needs: 1,2,4 for positions R2C4-C6 - Column 4 has: 5,3,1 → R2C4 can be 2 or 4 - Column 5 has: 6,5,4 → R2C5 can only be 1 or 2 - Column 6 has: 3,4 → R2C6 can only be 1 or 2 - So **R2C4 = 4**, and R2C5,C6 are 1,2  **Row 3:** 6 1 . 3 5 4 → Missing 2 **R3C3 = 2**  **Row 5:** 5 . 3 . 4 . - Column 2 has: 2,5,1,3,4 → **R5C2 = 6** - Column 4 has: 5,4,3,1 → R5C4 can be 2 or 6 - Row 5 needs: 1,2 for C4,C6 → **R5C4 = 2**, **R5C6 = 1**  **Row 6:** 2 4 5 1 . . - Column 5 needs: 1,2,3 → only 3 works → **R6C5 = 3** - **R6C6 = 6**  **Back to Row 2:** - Column 5 now has: 6,5,4,3 → **R2C5 = 1** - Column 6 now has: 3,4,1,6 → **R2C6 = 2**  **Row 4:** 1 3 4 . . . - Column 4 needs: 6 → **R4C4 = 6** - Column 5 needs: 2 → **R4C5 = 2** - **R4C6 = 5**  Missing numbers in reading order: Row 1: 3 Row 2: 3, 4, 1, 2 Row 3: 2 Row 4: 6, 2, 5 Row 5: 6, 2, 1 Row 6: 3, 6  Answer: | No | 42.73 |
| 6 | 4 3 6 2 5 5 1 6 5 2 4 4 3 4 | 4 3 6 2 5 5 1 6 5 2 4 4 3 4 | Yes | 40.38 |
| 7 | 5 6 6 2 5 5 4 2 3 5 2 5 6 1 | 5 6 6 2 5 5 4 2 3 5 2 5 6 1 | Yes | 39.79 |
| 8 | 3 4 1 6 5 3 5 1 2 2 3 5 4 1 | 3 4 1 6 5 3 5 1 2 2 3 5 4 1 | Yes | 32.42 |
| 9 | 5 4 6 3 4 1 4 5 3 5 6 1 2 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers systematically.  **Row 2:** Has 6,3,1,2,5 → missing 4 (position 6)  **Row 1:**  - Col 1: Column has 6,3,4 → needs 1,2,5. Row needs 3,4,5,6 → **5** - Col 3: Column has 1,2,3,6 → needs 4,5. Row now needs 3,4,6 → **4** - Col 5: Column has 5,6,4,2 → needs 1,3. Row needs 3,6 → **3** - Col 4: Row needs 6 → **6**  **Row 3:** - Col 1: Column needs 1,2. Row needs 1,3,4,5 → **1** - Col 2: Column has 2,3,1,5 → needs 4,6. Row needs 3,4,5 → **4** - Col 3: Column needs 5 → **5** - Col 4: Row needs 3 → **3**  **Row 4:** Col 4 needs 5 (row has 3,1,2,4,6) → **5**  **Row 5:** - Col 2: Column needs 6 → **6** - Col 4: Row needs 1 → **1**  **Row 6:** - Col | No | 41.6 |
| 10 | 1 6 4 2 5 5 4 1 3 4 6 1 3 6 |  | No | 29.51 |
| 11 | 3 4 5 6 4 1 6 4 1 5 6 3 5 3 |  | No | 32.19 |
| 12 | 4 3 3 4 1 4 2 6 3 1 5 1 6 5 | 4 3 3 4 1 4 2 6 3 1 5 1 6 5 | Yes | 32.04 |
| 13 | 2 4 6 3 1 3 5 3 4 6 2 5 6 3 |  | No | 35.45 |
| 14 | 4 2 3 2 4 1 5 6 3 1 4 6 3 5 | 4 2 3 2 4 1 5 6 3 1 4 6 3 5 | Yes | 32.3 |
| 15 | 5 2 3 4 1 2 6 2 4 1 1 2 6 5 | 5 2 3 4 1 2 6 2 4 1 1 2 6 5 | Yes | 36.73 |
| 16 | 4 3 5 6 1 4 1 6 2 6 4 1 2 3 | 4 3 5 6 1 4 1 6 2 6 4 1 2 3 | Yes | 25.28 |
| 17 | 3 5 4 6 3 2 1 4 2 3 6 3 1 3 | 3 5 4 6 3 2 1 4 2 3 6 3 1 3 | Yes | 30.58 |
| 18 | 4 2 1 5 3 6 4 2 6 1 5 1 6 2 |  | No | 35.29 |
| 19 | 1 2 5 4 1 3 5 2 2 5 6 1 2 1 | Looking at this 6×6 Sudoku, I need to find the missing numbers in each row, column, and 2×3 box.  **Row 1:** _ 6 _ \| 3 4 _ (needs 1,2,5) - Column 3 needs 2, so position (1,3) = 2 - Box 1 needs 1,3,4; Row 1 needs 1,5; so (1,1) = 1 - Position (1,6) = 5  **Row 2:** _ 2 5 \| 6 3 _ (needs 1,4) - Box 1 needs 3,4 after row 1; (2,1) = 4 - Position (2,6) = 1  **Row 3:** _ _ 1 \| 4 6 _ (needs 2,3,5) - Column 2 needs 1,5; Row 3 needs 5, so (3,2) = 5 - Column 6 has 5,1,3,4,6; needs 2, so (3,6) = 2 - Position (3,1) = 3  **Row 4:** _ 4 6 \| 1 _ | No | 36.98 |
| 20 | 2 5 4 2 3 4 2 6 5 3 1 6 5 3 | 2 5 4 2 3 4 2 6 5 3 1 6 5 3 | Yes | 26.16 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1528 | 1528 | Yes | 2.57 |
| 2 | 1732 | 1732 | Yes | 2.73 |
| 3 | 1448 | 1448 | Yes | 3.08 |
| 4 | 1740 | 1740 | Yes | 5.06 |
| 5 | 1929 | 1929 | Yes | 3.24 |
| 6 | 1201 | 1201 | Yes | 7.54 |
| 7 | 1865 | 1865 | Yes | 4.18 |
| 8 | 1896 | 1896 | Yes | 3.91 |
| 9 | 1620 | 1620 | Yes | 2.61 |
| 10 | 1400 | 1400 | Yes | 5.95 |
| 11 | 988 | 988 | Yes | 4.46 |
| 12 | 2309 | 2309 | Yes | 2.79 |
| 13 | 2244 | 2244 | Yes | 4.57 |
| 14 | 2099 | 2099 | Yes | 2.82 |
| 15 | 1495 | 1495 | Yes | 3.06 |
| 16 | 2013 | TIMEOUT | No | 120.02 |
| 17 | 1291 | 1291 | Yes | 7.03 |
| 18 | 1854 | 1854 | Yes | 2.61 |
| 19 | 1736 | 1736 | Yes | 4.91 |
| 20 | 1331 | 1331 | Yes | 4.5 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 | 63 | Yes | 17.96 |
| 2 | 59 | 58 | No | 18.56 |
| 3 | 63 | 63 | Yes | 13.89 |
| 4 | 58 | 58 | Yes | 25.88 |
| 5 | 74 | 75 | No | 23.65 |
| 6 | 53 | 53 | Yes | 13.04 |
| 7 | 48 | 48 | Yes | 17.66 |
| 8 | 69 | 68 | No | 22.33 |
| 9 | 63 | 63 | Yes | 14.8 |
| 10 | 49 | 49 | Yes | 14.69 |
| 11 | 48 | 46 | No | 13.21 |
| 12 | 54 | 54 | Yes | 14.14 |
| 13 | 60 | 60 | Yes | 16.43 |
| 14 | 39 | 39 | Yes | 19.48 |
| 15 | 35 | 35 | Yes | 16.52 |
| 16 | 63 | 63 | Yes | 10.46 |
| 17 | 70 | 71 | No | 15.46 |
| 18 | 59 | 56 | No | 15.36 |
| 19 | 48 | 48 | Yes | 16.76 |
| 20 | 54 | 54 | Yes | 16.79 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OYKEPCL | OYKEPCL | Yes | 11.27 |
| 2 | IFYJDPA | IFYJDPA | Yes | 6.51 |
| 3 | CPLFODH | CPLFODH | Yes | 6.75 |
| 4 | OBRLMXU | OBRLMXU | Yes | 8.76 |
| 5 | OHMEBRP | OHMEBRP | Yes | 4.33 |
| 6 | UGDCTXF | UGDCTXF | Yes | 14.82 |
| 7 | ALIERYT | ALIERYT | Yes | 17.19 |
| 8 | RCLBPMS | RCLBPMS | Yes | 14.12 |
| 9 | SRQIJMW | SRQIJMW | Yes | 8.51 |
| 10 | GPEXNOC | GPEXNOC | Yes | 4.23 |
| 11 | UXFCPAH | UXFCPAH | Yes | 4.61 |
| 12 | VJWEDAO | VJWEDAO | Yes | 5.07 |
| 13 | IUGEZKD | IUGEZKD | Yes | 6.29 |
| 14 | QNLJFXK | QNLJFXK | Yes | 8.12 |
| 15 | NSQIBMJ | NSQIBMJ | Yes | 5.52 |
| 16 | SDCETMQ | SDCETMQ | Yes | 5.58 |
| 17 | YSPKQLM | YSPKQLM | Yes | 5.08 |
| 18 | JSZRWBL | JSZRWBL | Yes | 5.35 |
| 19 | IGHEFTS | IGHEFTS | Yes | 4.75 |
| 20 | IHBCTYZ | IHBCTYZ | Yes | 4.61 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.5, 5.5] | 4.5 5.5 | Yes | 13.36 |
| 2 | [4.8, 5.2] | 5.2 4.8 | Yes | 21.72 |
| 3 | [0.2, 9.8] | 0.2 9.8 | Yes | 12.18 |
| 4 | [3.1, 6.9] | 6.9 3.1 | Yes | 14.59 |
| 5 | [4.1, 5.9] | 5.9 4.1 | Yes | 16.91 |
| 6 | [2.7, 7.3] | 7.3 2.7 | Yes | 18.26 |
| 7 | [1.4, 8.6] | 8.6 1.4 | Yes | 17.41 |
| 8 | [1.8, 8.2] | 1.8 8.2 | Yes | 16.1 |
| 9 | [3.3, 6.7] | 6.7 3.3 | Yes | 17.56 |
| 10 | [3.4, 6.6] | 3.4 6.6 | Yes | 7.09 |
| 11 | [3.1, 6.9] | 6.9 3.1 | Yes | 10.63 |
| 12 | [1.4, 8.6] | 1.4 8.6 | Yes | 10.82 |
| 13 | [2.7, 7.3] | 2.7 7.3 | Yes | 13.43 |
| 14 | [5.0, 5.0] | 5.0 5.0 | Yes | 18.9 |
| 15 | [3.0, 7.0] | 7.0 3.0 | Yes | 7.86 |
| 16 | [1.8, 8.2] | 8.2 1.8 | Yes | 13.31 |
| 17 | [2.0, 8.0] | 2.0 8.0 | Yes | 7.9 |
| 18 | [3.2, 6.8] | 6.8 3.2 | Yes | 11.02 |
| 19 | [2.7, 7.3] | 2.7 7.3 | Yes | 11.22 |
| 20 | [4.1, 5.9] | 4.1 5.9 | Yes | 10.81 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1VQJN77RUEIO | 1VQJN77RUEIO | Yes | 8.55 |
| 2 | 05MALPXSNPYR | 05MALPXSNPYR | Yes | 4.94 |
| 3 | U1V94GOT9R76 | U1V94GOT9R76 | Yes | 6.99 |
| 4 | GDNRFVPVI9R2 | GDNRFVPVI9R2 | Yes | 3.2 |
| 5 | 6WOWUM6W787H | 6WOWUM6W787H | Yes | 3.69 |
| 6 | S7UZZT79AXSZ | S7UZZT79AXSZ | Yes | 3.81 |
| 7 | MVV3E7OS0VDE | MVV3E7OS0VDE | Yes | 3.59 |
| 8 | IWDTA1M4C2G7 | IWDTA1M4C2G7 | Yes | 3.96 |
| 9 | PXCAZ86LQYC0 | PXCAZ86LQYC0 | Yes | 13.32 |
| 10 | FCD3VRZGNHBR | FCD3VRZGNHBR | Yes | 4.0 |
| 11 | 9UFR4PMKL0A6 | 9UFR4PMKL0A6 | Yes | 3.72 |
| 12 | GH4RJP68X4CI | GH4RJP68X4CI | Yes | 3.38 |
| 13 | X4S66Q0S5LWW | X4S66Q0S5LWW | Yes | 7.62 |
| 14 | K4CA5BR71TUG | K4CA5BR71TUG | Yes | 3.37 |
| 15 | G61TS31NZFJG | G61TS31NZFJG | Yes | 3.88 |
| 16 | REQF68MTFRQ4 | REQF68MTFRQ4 | Yes | 13.23 |
| 17 | 3SUN9VQT9MB2 | 3SUN9VQT9MB2 | Yes | 4.08 |
| 18 | IIHOT10Z1FW2 | IIHOT10Z1FW2 | Yes | 12.44 |
| 19 | 8VE3CG55VI19 | 8VE3CG55VI19 | Yes | 3.48 |
| 20 | 0W12B44E4WVM | 0W12B44E4WVM | Yes | 10.87 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 198 | 198 | Yes | 7.98 |
| 2 | 4 | 4 | Yes | 6.03 |
| 3 | 9 | 9 | Yes | 6.48 |
| 4 | 60 | 60 | Yes | 13.94 |
| 5 | 23 | 23 | Yes | 6.16 |
| 6 | 67 | 67 | Yes | 14.7 |
| 7 | 6 | 6 | Yes | 5.84 |
| 8 | 26 | 26 | Yes | 14.36 |
| 9 | 9 | 9 | Yes | 6.54 |
| 10 | 65 | 65 | Yes | 9.2 |
| 11 | 7 | 7 | Yes | 5.33 |
| 12 | 44 | 44 | Yes | 16.31 |
| 13 | 793 | 793 | Yes | 6.46 |
| 14 | 31 | 31 | Yes | 7.25 |
| 15 | 4 | 4 | Yes | 6.0 |
| 16 | 5 | 14 | No | 24.44 |
| 17 | 3 | 3 | Yes | 14.19 |
| 18 | 243 | 243 | Yes | 13.95 |
| 19 | 4096 | 4096 | Yes | 21.37 |
| 20 | 60 | 60 | Yes | 15.48 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <_(/_)_<\ | <_(/_)_<\ | Yes | 7.46 |
| 2 | ()(<<)//  | ()(<<)// | No | 13.82 |
| 3 | /<)  )\_) | /<)  )\_) | Yes | 7.32 |
| 4 | /__ _))<_ | /__ _))<_ | Yes | 9.67 |
| 5 | </<(_)< \ | </<(_)< \ | Yes | 10.17 |
| 6 |  )_ _ _ < | )_ _ _ | No | 16.33 |
| 7 | ( <<\< __ | ( <<\< __ | Yes | 15.5 |
| 8 | \<_ <()<) | \<_ <()<) | Yes | 7.72 |
| 9 | <( \\/ _) | <( \\/ _) | Yes | 17.04 |
| 10 | \\)_/<( < | \\)_/<( | No | 14.21 |
| 11 | / / <<//  | / / <<// | No | 13.82 |
| 12 | (<\(/_)\/ | (<\(/_)\/ | Yes | 3.29 |
| 13 | _<<\< /<< | _<<\< /< | No | 4.88 |
| 14 | </ <\\((( | </ <\\((( | Yes | 10.59 |
| 15 | (_<(\/_)_ | (_<(\/_)_ | Yes | 3.67 |
| 16 | _/\<)(</< | _/\<)(</ | No | 7.02 |
| 17 | __\/( <\( | __\/( <\( | Yes | 13.89 |
| 18 | _( \/<) \ | _( \/<) \ | Yes | 4.55 |
| 19 | /(_< )<\/ | /(_< )<\/ | Yes | 14.15 |
| 20 | (< /\  _< | (< /\  _ | No | 13.65 |
