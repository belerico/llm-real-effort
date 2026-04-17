# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-27 10:00:56

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
| sudoku_game | 6124 | 36419 | 42543 | 8 | 12 | 27.66 | 553.28 |
| add_numbers | 3500 | 799 | 4299 | 20 | 0 | 2.14 | 42.73 |
| counting_zeros | 4820 | 13943 | 18763 | 4 | 16 | 9.16 | 183.3 |
| task_decoding | 4820 | 2440 | 7260 | 20 | 0 | 3.71 | 74.16 |
| task_summation | 4880 | 2863 | 7743 | 20 | 0 | 3.28 | 65.66 |
| task_transcription | 3666 | 766 | 4432 | 20 | 0 | 2.17 | 43.34 |
| task_sequences | 3561 | 3439 | 7000 | 18 | 2 | 4.59 | 91.7 |
| string_entry | 4052 | 1582 | 5634 | 12 | 8 | 3.41 | 68.15 |
| **TOTAL** | **35423** | **62251** | **97674** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 5 6 2 3 2 6 4 1 2 4 3 1 |  | No | 35.37 |
| 2 | 1 4 5 6 1 3 5 1 6 1 4 3 3 2 | 1 4 5 6 1 3 5 1 6 1 4 3 3 2 | Yes | 25.05 |
| 3 | 1 4 6 5 4 2 5 1 5 1 4 1 4 1 | 1 4 6 5 4 2 5 1 5 1 4 1 4 1 | Yes | 27.04 |
| 4 | 3 2 5 1 5 1 4 6 3 6 3 5 1 2 | Looking at this puzzle systematically:  **Row 3:** 1 6 5 \| _ 2 4 → missing **3** → (3,4) = 3  **Column 1:** 4,2,1,_,5,3 → missing **6** → (4,1) = 6  **Box rows 3-4, cols 4-6:** contains 3,2,4 → missing 1,5,6 **Column 4:** contains 6,3,2,1 → missing 4,5 → (2,4)=4 or 5, (4,4)=4 or 5  **Testing (4,3):** Box rows 3-4, cols 1-3 contains 1,6,5,6,4 → missing 2,3 - If (4,3)=3: Row 4 = 6,4,3,_,_,_ missing 1,2,5 - (4,4) must be in {1,5,6}∩{4,5} = **5** → (4,4)=5, (2,4)=4 - (4,5) must be in col5 missing {1,5,6} ∩ row4 missing {1,2} = **1** → (4,5)=1 - (4,6) = **2** ✓ (col 6 missing 1,2)  **Column 6:** missing 1,2 → (1,6)=1 (since (4,6)=2)  **Row 1:** 4,_,_,6,_,1 → missing 2,3,5 **Column 5:** missing 5,6 for rows 1,2; row1 needs from {2,3,5} → (1,5)=**5**, (2,5)=**6**  **Row 2:** 2,_,_,4,6,3 → missing 1,5 **Column 3:** missing 1,2 for rows 1,2; row2 missing {1,5} → (2,3)=**1**, (1,3)=** | No | 30.5 |
| 5 | 2 5 3 6 2 6 4 6 2 6 4 3 5 4 | 2 5 3 6 2 6 4 6 2 6 4 3 5 4 | Yes | 19.95 |
| 6 | 1 6 2 5 1 3 6 4 6 3 4 2 4 1 |  | No | 32.3 |
| 7 | 5 3 4 2 6 1 6 4 1 3 4 3 2 6 | 5 3 4 2 6 1 6 4 1 3 4 3 2 6 | Yes | 21.06 |
| 8 | 1 4 6 4 5 3 3 1 4 5 4 1 5 4 |  | No | 33.34 |
| 9 | 1 6 6 5 6 4 1 5 1 6 2 5 3 1 |  | No | 33.72 |
| 10 | 6 4 6 1 5 1 6 3 2 4 4 3 1 5 | Looking at this puzzle systematically:  **Row 1:** 2 5 3 \| _ _ 1 → needs 4,6 - Col 4 already has 4 (row 2) → Row 1, Col 4 = **6**; Col 5 = **4**  **Row 3:** 4 _ _ \| 2 _ 3 → needs 1,5,6 - Col 2 (has 5,1,4,2) → missing 3,6 → Col 2 = **6** - Col 3 (has 3,5,2,6) → missing 1,4 → Col 3 = **1** - Remaining: Col 5 = **5**  **Row 4:** 5 4 2 \| _ 3 _ → needs 1,6 - Col 4 (has 6,4,2) → needs 1 → Col 4 = **1**; Col 6 = **6**  **Row 5:** 1 _ 6 \| 5 _ _ → needs 2,3,4 - Col 2 (has 5,1,6,4,2) → missing 3 → Col 2 = **3** - Col 5 | No | 35.44 |
| 11 | 1 5 4 3 6 4 5 3 5 2 4 6 5 1 | 1 5 4 3 6 4 5 3 5 2 4 6 5 1 | Yes | 22.71 |
| 12 | 3 6 1 5 2 6 6 2 1 1 5 5 4 2 | 3 6 1 5 2 6 6 2 1 1 5 5 4 2 | Yes | 19.64 |
| 13 | 3 4 6 1 5 6 3 2 3 5 5 1 6 3 | ## Solving the 6×6 Sudoku  **Starting grid:** ``` . . 2 \| . 5 1 . . 4 \| 3 . 2 ------+------ 6 2 1 \| 5 . 4 . 6 . \| 1 4 . ------+------ 4 3 5 \| 2 1 6 . . . \| 4 2 . ```  **Step-by-step logic:**  **Row 3:** Has 6,2,1,5,_,4 → missing **3** → R3C5=3  **Row 4:** Has _,6,_,1,4,_ → missing 2,3,5 - Col3 has 2,1,4,5,3 → needs 6, but 6 in row4 → **R4C3=3** (col3 needs 3 or 6; row4 already has 6) - Col6 has 2,4,6 → needs 1,3,5; row4 remaining options → **R4C6=5** - R4C1: row needs 2 → Col1 check confirms → **R4C1=2**  **Row 6:** Has _,_,_,4,2,_ → missing 1,3,5,6 - Col3 has 2,1,4,5 | No | 30.61 |
| 14 | 1 1 2 4 6 2 1 2 3 1 3 6 5 4 |  | No | 35.01 |
| 15 | 6 5 3 5 2 5 6 5 2 6 6 2 1 2 | ## Solving the 6×6 Sudoku  **Starting grid:** ``` 1 . 2 \| 3 4 . . . 1 \| 4 6 2 ------+------ 4 . . \| . 1 3 . 1 4 \| . 3 . ------+------ . 4 3 \| 5 . . . 3 6 \| 1 5 4 ```  **Step-by-step reasoning:**  - **Row 1** needs 5,6. Top-right box (r1-2,c4-6) needs 1,5 → **(1,6)=5**, then **(1,2)=6** - **Col 2** = {6,?,?,1,4,3} needs 2,5. Row 2 needs 3,5 → **(2,2)=5**, then **(2,1)=3** - **Col 2** now: {6,5,?,1,4,3} → **(3,2)=2** - **Col 3** = {2,1,?,4,3,6} needs 5 → **(3,3)=5**, so **(3,4)=6** - **Col 4 | No | 23.27 |
| 16 | 3 5 4 1 3 6 1 2 2 6 5 5 2 1 | 3 5 4 1 3 6 2 1 5 6 2 1 2 5 | No | 29.25 |
| 17 | 5 4 1 1 2 4 2 1 5 3 2 6 2 3 | 5 4 1 1 2 4 2 1 5 3 2 6 2 3 | Yes | 17.89 |
| 18 | 6 2 3 4 6 5 2 3 5 6 1 1 3 2 | 6 5 3 4 6 5 2 3 5 1 1 3 2 | No | 30.41 |
| 19 | 3 5 6 5 1 4 2 6 5 4 2 3 2 6 | 3 5 6 5 1 4 2 6 5 4 2 3 2 6 | Yes | 17.36 |
| 20 | 3 4 5 6 1 1 4 2 3 1 6 5 5 4 |  | No | 33.31 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1902 | 1902 | Yes | 3.54 |
| 2 | 2411 | 2411 | Yes | 4.86 |
| 3 | 1435 | 1435 | Yes | 1.7 |
| 4 | 1656 | 1656 | Yes | 1.98 |
| 5 | 1988 | 1988 | Yes | 1.83 |
| 6 | 1701 | 1701 | Yes | 1.74 |
| 7 | 2021 | 2021 | Yes | 1.59 |
| 8 | 1659 | 1659 | Yes | 1.81 |
| 9 | 1367 | 1367 | Yes | 1.01 |
| 10 | 1829 | 1829 | Yes | 1.62 |
| 11 | 2151 | 2151 | Yes | 2.47 |
| 12 | 2187 | 2187 | Yes | 1.78 |
| 13 | 1398 | 1398 | Yes | 1.29 |
| 14 | 1659 | 1659 | Yes | 1.68 |
| 15 | 2096 | 2096 | Yes | 1.35 |
| 16 | 1597 | 1597 | Yes | 2.12 |
| 17 | 1511 | 1511 | Yes | 1.09 |
| 18 | 1540 | 1540 | Yes | 2.48 |
| 19 | 1414 | 1414 | Yes | 2.75 |
| 20 | 1993 | 1993 | Yes | 4.06 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 59 | No | 14.13 |
| 2 | 71 | 71 | Yes | 12.6 |
| 3 | 53 | 53 | Yes | 7.95 |
| 4 | 41 | 41 | Yes | 14.93 |
| 5 | 46 | 46 | Yes | 10.95 |
| 6 | 70 | 61 | No | 10.57 |
| 7 | 56 | 49 | No | 10.3 |
| 8 | 67 | 66 | No | 8.81 |
| 9 | 54 | 39 | No | 4.72 |
| 10 | 37 | 36 | No | 5.06 |
| 11 | 38 | 37 | No | 6.5 |
| 12 | 75 | 63 | No | 6.95 |
| 13 | 48 | 47 | No | 9.35 |
| 14 | 57 | 52 | No | 8.57 |
| 15 | 51 | 37 | No | 4.93 |
| 16 | 42 | 36 | No | 6.48 |
| 17 | 51 | 49 | No | 8.56 |
| 18 | 57 | 52 | No | 9.08 |
| 19 | 35 | 33 | No | 13.32 |
| 20 | 72 | 62 | No | 9.52 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BNZWDSX | BNZWDSX | Yes | 3.7 |
| 2 | GPWVFXI | GPWVFXI | Yes | 9.38 |
| 3 | MQFXDLE | MQFXDLE | Yes | 4.64 |
| 4 | OYMKEHW | OYMKEHW | Yes | 2.77 |
| 5 | SIKRHCQ | SIKRHCQ | Yes | 2.15 |
| 6 | AUHFGRV | AUHFGRV | Yes | 2.78 |
| 7 | PCWVJNY | PCWVJNY | Yes | 4.15 |
| 8 | LDPMBFQ | LDPMBFQ | Yes | 2.74 |
| 9 | FBVRZJK | FBVRZJK | Yes | 2.62 |
| 10 | SDRBVGZ | SDRBVGZ | Yes | 3.12 |
| 11 | ZEXLONI | ZEXLONI | Yes | 2.71 |
| 12 | XQTMWHD | XQTMWHD | Yes | 4.85 |
| 13 | LQHBNZK | LQHBNZK | Yes | 3.18 |
| 14 | CILVJPR | CILVJPR | Yes | 2.79 |
| 15 | SBHJLZK | SBHJLZK | Yes | 3.32 |
| 16 | BTUINPL | BTUINPL | Yes | 3.18 |
| 17 | NVRDLAQ | NVRDLAQ | Yes | 4.2 |
| 18 | DUKVCWE | DUKVCWE | Yes | 4.33 |
| 19 | FWESZXT | FWESZXT | Yes | 4.05 |
| 20 | XPAOQRI | XPAOQRI | Yes | 3.5 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.1, 7.9] | 7.9 2.1 | Yes | 2.99 |
| 2 | [4.9, 5.1] | 4.9 5.1 | Yes | 2.22 |
| 3 | [2.3, 7.7] | 2.3 7.7 | Yes | 4.15 |
| 4 | [3.1, 6.9] | 3.1 6.9 | Yes | 3.45 |
| 5 | [2.3, 7.7] | 7.7 2.3 | Yes | 3.05 |
| 6 | [0.5, 9.5] | 9.5 0.5 | Yes | 2.4 |
| 7 | [1.5, 8.5] | 8.5 1.5 | Yes | 5.24 |
| 8 | [2.0, 8.0] | 2.0 8.0 | Yes | 3.54 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 1.91 |
| 10 | [0.5, 9.5] | 9.5 0.5 | Yes | 2.81 |
| 11 | [1.6, 8.4] | 1.6 8.4 | Yes | 2.84 |
| 12 | [1.1, 8.9] | 8.9 1.1 | Yes | 3.31 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 6.02 |
| 14 | [1.5, 8.5] | 1.5 8.5 | Yes | 2.82 |
| 15 | [4.4, 5.6] | 4.4 5.6 | Yes | 3.87 |
| 16 | [3.6, 6.4] | 3.6 6.4 | Yes | 3.71 |
| 17 | [3.9, 6.1] | 3.9 6.1 | Yes | 2.99 |
| 18 | [0.4, 9.6] | 9.6 0.4 | Yes | 3.03 |
| 19 | [1.8, 8.2] | 1.8 8.2 | Yes | 3.05 |
| 20 | [2.5, 7.5] | 7.5 2.5 | Yes | 2.24 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OUY116UGMQCF | OUY116UGMQCF | Yes | 1.08 |
| 2 | 8HTFLJI5OQ02 | 8HTFLJI5OQ02 | Yes | 1.62 |
| 3 | 0YHNM9WJVY8A | 0YHNM9WJVY8A | Yes | 1.73 |
| 4 | O9KIOQL88A99 | O9KIOQL88A99 | Yes | 1.82 |
| 5 | 01YUTCZS1TQB | 01YUTCZS1TQB | Yes | 1.03 |
| 6 | QU2QOB80IRU7 | QU2QOB80IRU7 | Yes | 1.63 |
| 7 | MENDXP1GXB5U | MENDXP1GXB5U | Yes | 1.93 |
| 8 | QO6C922ZTJB6 | QO6C922ZTJB6 | Yes | 1.01 |
| 9 | L4OAHR3VSLV5 | L4OAHR3VSLV5 | Yes | 1.64 |
| 10 | GV9W1PV4UI7X | GV9W1PV4UI7X | Yes | 1.58 |
| 11 | QHLX6XG3O89J | QHLX6XG3O89J | Yes | 1.18 |
| 12 | HGMTVMECNPDT | HGMTVMECNPDT | Yes | 2.7 |
| 13 | EPFMW28M9X7W | EPFMW28M9X7W | Yes | 1.88 |
| 14 | JJQSINIA9X2N | JJQSINIA9X2N | Yes | 4.68 |
| 15 | ZVCR8JAQ9WQR | ZVCR8JAQ9WQR | Yes | 1.25 |
| 16 | YIRM8PU3EO74 | YIRM8PU3EO74 | Yes | 3.1 |
| 17 | 2JJDITNPQWXE | 2JJDITNPQWXE | Yes | 4.54 |
| 18 | TUGCFDNKSZI1 | TUGCFDNKSZI1 | Yes | 2.08 |
| 19 | DI0FSHUUXQW8 | DI0FSHUUXQW8 | Yes | 3.77 |
| 20 | 4FD3JYWO036N | 4FD3JYWO036N | Yes | 3.06 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 20 | 21 | No | 13.39 |
| 2 | 1 | 1 | Yes | 3.44 |
| 3 | 5 | 5 | Yes | 2.36 |
| 4 | 60 | 60 | Yes | 3.26 |
| 5 | 63 | 63 | Yes | 2.09 |
| 6 | 48 | 48 | Yes | 2.28 |
| 7 | 4096 | 1048576 | No | 5.3 |
| 8 | 28 | 28 | Yes | 2.33 |
| 9 | 64 | 64 | Yes | 4.11 |
| 10 | 26 | 26 | Yes | 8.53 |
| 11 | 3 | 3 | Yes | 7.58 |
| 12 | 6 | 6 | Yes | 2.9 |
| 13 | 9 | 9 | Yes | 3.59 |
| 14 | 73 | 73 | Yes | 15.4 |
| 15 | 1440 | 1440 | Yes | 1.95 |
| 16 | 36 | 36 | Yes | 2.37 |
| 17 | 39 | 39 | Yes | 2.95 |
| 18 | 7 | 7 | Yes | 2.1 |
| 19 | 7680 | 7680 | Yes | 3.79 |
| 20 | 16 | 16 | Yes | 1.99 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \ _<<\\ / | \ _<<\\ / | Yes | 2.2 |
| 2 | /_\<()</( | /_\<()</( | Yes | 3.48 |
| 3 | )()<\)_(\ | )()<\)_(\ | Yes | 3.79 |
| 4 | /))_)_(\\ | /))_)_(\\ | Yes | 3.08 |
| 5 | )<\/</ \  | )<\/</ \ | No | 4.56 |
| 6 | /(__(_)(\ | /(__(_)(\ | Yes | 4.05 |
| 7 | ((/\)  _  | ((/\)  _ | No | 3.42 |
| 8 | /_(  <_ _ | /_(  <_ _ | Yes | 6.26 |
| 9 | )\ _/ <_( | )\ _/ <_( | Yes | 1.37 |
| 10 | _< ((\ )< | _< ((\ ) | No | 4.88 |
| 11 | _ _<\) )_ | _ _<\) )_ | Yes | 2.24 |
| 12 | __</\ (/< | __</\ (/ | No | 2.13 |
| 13 | ((\)  ( / | ((\)  ( / | Yes | 3.16 |
| 14 | \\(_(/\<\ | \\(_(/\<\ | Yes | 2.58 |
| 15 | ))_ _ <)  | ))_ _ <) | No | 3.51 |
| 16 | (<</ < <_ | (<</ < <_ | Yes | 3.12 |
| 17 | //(//_)(  | //(//_)( | No | 2.99 |
| 18 | (((/)<((\ | (((/)<((\ | Yes | 4.11 |
| 19 |   \((\ <) | \((\ <) | No | 3.16 |
| 20 | /  <())\  | /  <())\ | No | 4.08 |
