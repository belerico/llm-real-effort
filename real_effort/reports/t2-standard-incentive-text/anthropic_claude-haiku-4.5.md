# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-27 09:56:31

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
| sudoku_game | 6333 | 32490 | 38823 | 2 | 18 | 10.71 | 214.16 |
| add_numbers | 3720 | 2966 | 6686 | 20 | 0 | 2.73 | 54.57 |
| counting_zeros | 5040 | 21664 | 26704 | 1 | 19 | 7.13 | 142.62 |
| task_decoding | 4788 | 6170 | 10958 | 18 | 2 | 9.05 | 181.07 |
| task_summation | 5100 | 14054 | 19154 | 20 | 0 | 4.86 | 97.14 |
| task_transcription | 3881 | 2848 | 6729 | 20 | 0 | 2.04 | 40.9 |
| task_sequences | 3781 | 6106 | 9887 | 19 | 1 | 2.69 | 53.71 |
| string_entry | 4243 | 5182 | 9425 | 14 | 6 | 2.96 | 59.28 |
| **TOTAL** | **36886** | **91480** | **128366** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 1 6 3 4 5 2 3 4 1 5 4 6 | 3 1 6 6 3 4 5 2 3 4 1 5 4 6 | No | 11.09 |
| 2 | 1 2 3 6 2 1 3 6 5 3 1 3 6 4 | 6 2 3 1 2 1 3 6 5 3 1 3 6 4 | No | 8.08 |
| 3 | 5 1 2 1 3 6 2 5 5 4 2 6 5 3 |  | No | 13.94 |
| 4 | 6 5 1 3 6 2 6 5 3 1 3 6 2 1 | 6 5 3 1 6 2 6 5 3 1 1 6 2 3** | No | 11.52 |
| 5 | 6 3 5 1 6 4 5 5 2 4 6 3 6 5 | 6 3 2 1 6 4 5 5 2 4 3 6 5 6 | No | 9.3 |
| 6 | 1 4 5 5 6 4 1 2 1 2 6 2 5 3 | 1 4 5 5 6 2 1 4 2 1 6 1 2 3** | No | 9.7 |
| 7 | 2 5 2 3 5 4 6 6 2 4 4 6 5 1 | 2 5 2 3 5 6 4 4 2 6 4 6 5 1 | No | 10.78 |
| 8 | 2 5 6 3 1 3 1 3 4 4 3 6 6 5 | 6 5 2 3 4 1 1 4 3 5 4 2 3 1 6 6 5 | No | 9.67 |
| 9 | 5 2 2 1 4 6 2 3 6 2 4 6 2 5 | 2 5 5 1 2 3 6 4 6 2 4 6 2 5 | No | 9.59 |
| 10 | 1 6 2 3 3 5 6 2 6 1 6 6 2 5 | 3 6 2 3 6 5 3 2 2 | No | 14.22 |
| 11 | 4 2 5 4 1 2 6 1 3 2 5 2 1 2 | 4 2 5 4 1 2 6 1 3 2 5 2 1 2 | Yes | 9.91 |
| 12 | 2 3 1 3 5 6 6 4 2 1 2 3 2 4 | 2 3 5 6 6 4 2 1 2 3 4 | No | 10.74 |
| 13 | 2 1 3 6 3 5 1 6 2 3 6 1 3 2 | # 6×6 Sudoku Solution  Let me solve this step-by-step using row, column, and box constraints.  **Solving systematically:**  Row 1: 5 ? 4 \| 6 ? ? - (1,2): Box 1 needs 1,2,3,6; Col 2 has 4,1,5 → (1,2) = 3 - (1,5): Col 5 has 4,2,5,3,6 → (1,5) = 1   - (1,6): Row needs 2 → (1,6) = 2  Row 2: 1 ? 2 \| ? 4 ? - (2,2): Col 2 needs 2,6; Row needs 3,5,6 → (2,2) = 6 - (2,4): Col 4 needs 1,2,3; Row needs 3,5 → (2,4) = 3 - (2,6): Row needs 5 → (2,6) = 5  Row 3: 3 4 ? \| 5 2 ? - (3,3): Col 3 needs 1,3,6; Row needs 1,6; Box 3 needs 1,2,5,6 → (3,3) = 6 - (3,6): Row needs 1 → (3,6) = 1  Row 4: ? ? ? \| ? 5 4 - (4,1): Col 1 needs 2; Box 3 needs 2,5 → (4,1) = 2 - (4,2): Col 2 needs 2; already used → (4,2) = 2... wait. Let me recalculate. - (4,2): Col 2 needs 2; Row 4 needs 1,2,3,6 → (4,2) = 2 - (4,3): Col 3 needs 1,3; Row 4 needs 1,3,6 → (4,3) = 1 - (4,4): Col 4 needs 1,2; Row 4 needs 6 or 3 → (4,4) = 2    Wait, let me recalculate row 4 more carefully: has 5,4. Needs 1,2,3,6. - (4,4): Col 4 has 6,3,5,4; needs 1,2 → (4,4) = 2 - (4,3): needs 1 or 3; Col 3 has 4,2,6,5; needs 1,3 → Box 3 connection suggests (4,3) = 1 - (4,2): Col 2 missing 2 → (4,2) = 2 - (4,1): Col 1 missing 2 | No | 19.56 |
| 14 | 3 4 5 1 2 6 4 4 2 3 2 3 4 1 | 3 4 5 1 1 6 2 2 4 2 3 1 | No | 11.19 |
| 15 | 2 3 6 1 5 1 4 2 6 3 1 5 6 2 | 2 3 6 1 5 1 4 2 6 3 1 5 6 2 2 | No | 7.49 |
| 16 | 4 2 3 1 4 6 4 3 5 3 3 5 3 2 | 4 2 3 1 4 6 4 3 5 3 3 5 3 2 | Yes | 10.71 |
| 17 | 6 3 4 2 6 3 5 1 5 3 2 6 6 5 | 3 6 4 6 3 2 5 1 5 3 6 2 2 6 | No | 8.14 |
| 18 | 2 3 5 4 2 3 5 1 5 2 6 4 2 5 | 2 5 3 4 5 2 3 1 2 5 6 4 3 5 | No | 8.45 |
| 19 | 2 3 1 5 3 2 5 1 4 5 1 2 1 5 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  **Starting with easier cells:**  Row 5: 5, 6, 3 \| 2, 4, ? → Missing 1, so R5C6 = **1**  Row 2: 1, 4, 5 \| ?, 6, ? → Missing 2, 3 - Column 6 has 4, _, 3, 6, 1, ? → Missing 2, 5 - So R2C6 = **2**, R2C4 = **3**, R6C6 = **5**  Row 6: 4, ?, 6 \| ?, 3, 5 → Missing 1, 2 - Column 4 has 6, 3, 4, ?, 2, ? → Missing 1, 5 - So R6C4 = **1**, R4C4 = **5**, R6C2 = **2**  Row 4: 3, ?, ? \| 5, 2, 6 → Missing 1, 4 - Column 2 has ?, 4, ?, ?, 6, 2 → Missing 1, 3, 5 - R4C2 must be in both {1,4} and {1,3,5} → R4C2 = **1**, R4C3 = **4**  Row 3: 6, ?, 2 \| 4, | No | 11.6 |
| 20 | 4 1 3 1 6 6 1 2 4 3 3 3 6 4 | 4 1 3 1 6 1 2 4 3 3 6 4 | No | 8.42 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1367 | 1367 | Yes | 1.95 |
| 2 | 2507 | 2507 | Yes | 2.39 |
| 3 | 1686 | 1686 | Yes | 2.43 |
| 4 | 1197 | 1197 | Yes | 2.29 |
| 5 | 1255 | 1255 | Yes | 2.38 |
| 6 | 2513 | 2513 | Yes | 11.7 |
| 7 | 580 | 580 | Yes | 1.7 |
| 8 | 1085 | 1085 | Yes | 2.9 |
| 9 | 1708 | 1708 | Yes | 2.42 |
| 10 | 1694 | 1694 | Yes | 2.31 |
| 11 | 738 | 738 | Yes | 2.31 |
| 12 | 1476 | 1476 | Yes | 2.07 |
| 13 | 832 | 832 | Yes | 1.61 |
| 14 | 1315 | 1315 | Yes | 2.05 |
| 15 | 1030 | 1030 | Yes | 1.93 |
| 16 | 2163 | 2163 | Yes | 1.95 |
| 17 | 1324 | 1324 | Yes | 2.11 |
| 18 | 2234 | 2234 | Yes | 2.73 |
| 19 | 1735 | 1735 | Yes | 3.15 |
| 20 | 2353 | 2353 | Yes | 2.19 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 75 | 68 | No | 7.16 |
| 2 | 63 | 66 | No | 9.52 |
| 3 | 37 | 31 | No | 5.77 |
| 4 | 52 | 53 | No | 8.36 |
| 5 | 69 | 64 | No | 6.8 |
| 6 | 62 | 54 | No | 5.27 |
| 7 | 42 | 39 | No | 8.26 |
| 8 | 44 | 37 | No | 5.91 |
| 9 | 70 | 68 | No | 9.86 |
| 10 | 37 | 32 | No | 6.54 |
| 11 | 65 | 55 | No | 8.2 |
| 12 | 70 | 65 | No | 6.16 |
| 13 | 69 | 64 | No | 9.33 |
| 14 | 41 | 42 | No | 7.85 |
| 15 | 71 | 54 | No | 5.78 |
| 16 | 56 | 56 | Yes | 4.03 |
| 17 | 55 | 46 | No | 6.68 |
| 18 | 50 | 52 | No | 5.47 |
| 19 | 48 | 45 | No | 5.94 |
| 20 | 66 | 61 | No | 9.71 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | BTWEPHY | BTWEPTHY | No | 4.26 |
| 2 | FSYZMCX | FSYZMCX | Yes | 3.74 |
| 3 | YMBISXU | YMBISXU | Yes | 2.98 |
| 4 | XPWIDMZ | XPWIDMZ | Yes | 3.22 |
| 5 | TRFSHGC | TRFSHGC | Yes | 2.58 |
| 6 | HUBTQDK | HUBTQDK | Yes | 2.55 |
| 7 | CPXBQAT | CPXBQAT | Yes | 5.68 |
| 8 | RTWYZEX | RTWYZEX | Yes | 3.11 |
| 9 | NBJFZSV | NBJFZSV | Yes | 2.42 |
| 10 | DIOQGSZ | DIOQGSZ | Yes | 2.46 |
| 11 | QMASVYL | QMASVYL | Yes | 2.47 |
| 12 | DABXNFL | DABXNFL | Yes | 3.97 |
| 13 | VNSGPHA | VNSGPHA | Yes | 2.96 |
| 14 | GIALSPV | GIALSPV | Yes | 4.18 |
| 15 | KSPGMUI | KSPGMUI | Yes | 2.27 |
| 16 | UYFJILQ | TIMEOUT | No | 120.03 |
| 17 | VTEMXWB | VTEMXWB | Yes | 2.14 |
| 18 | NQKVSGT | NQKVSGT | Yes | 3.01 |
| 19 | FWMEHBY | FWMEHBY | Yes | 3.94 |
| 20 | QULYCPK | QULYCPK | Yes | 3.08 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.3, 5.7] | 4.3 5.7 | Yes | 5.15 |
| 2 | [0.4, 9.6] | 0.4 9.6 | Yes | 4.04 |
| 3 | [2.1, 7.9] | 7.9 2.1 | Yes | 5.55 |
| 4 | [2.1, 7.9] | 2.1 7.9 | Yes | 2.96 |
| 5 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.75 |
| 6 | [2.3, 7.7] | 7.7 2.3 | Yes | 4.67 |
| 7 | [3.9, 6.1] | 6.1 3.9 | Yes | 6.05 |
| 8 | [1.4, 8.6] | 1.4 8.6 | Yes | 6.33 |
| 9 | [2.2, 7.8] | 2.2 7.8 | Yes | 7.13 |
| 10 | [1.6, 8.4] | 8.4 1.6 | Yes | 4.16 |
| 11 | [4.1, 5.9] | 4.1 5.9 | Yes | 5.16 |
| 12 | [2.7, 7.3] | 2.7 7.3 | Yes | 5.17 |
| 13 | [4.4, 5.6] | 4.4 5.6 | Yes | 4.66 |
| 14 | [2.5, 7.5] | 2.5 7.5 | Yes | 5.14 |
| 15 | [2.6, 7.4] | 2.6 7.4 | Yes | 2.54 |
| 16 | [1.5, 8.5] | 8.5 1.5 | Yes | 3.96 |
| 17 | [4.5, 5.5] | 5.5 4.5 | Yes | 3.89 |
| 18 | [1.0, 9.0] | 9.0 1.0 | Yes | 5.15 |
| 19 | [2.7, 7.3] | 7.3 2.7 | Yes | 4.24 |
| 20 | [0.9, 9.1] | 0.9 9.1 | Yes | 4.42 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4NMBGH34T0GE | 4NMBGH34T0GE | Yes | 1.99 |
| 2 | 5AAVG383NS6U | 5AAVG383NS6U | Yes | 1.98 |
| 3 | 88O7U2LWGF9K | 88O7U2LWGF9K | Yes | 1.88 |
| 4 | LYPGQOPI9ZW0 | LYPGQOPI9ZW0 | Yes | 1.6 |
| 5 | 4T5VBU8GA1Y2 | 4T5VBU8GA1Y2 | Yes | 1.98 |
| 6 | CRHUQYW03JJZ | CRHUQYW03JJZ | Yes | 1.93 |
| 7 | 1ZQH2OR4GGHR | 1ZQH2OR4GGHR | Yes | 1.85 |
| 8 | P37W4K3XPQR3 | P37W4K3XPQR3 | Yes | 2.42 |
| 9 | DT033EZW9QL8 | DT033EZW9QL8 | Yes | 1.57 |
| 10 | H9HD4FFC3L27 | H9HD4FFC3L27 | Yes | 1.74 |
| 11 | Y61K36ATYX48 | Y61K36ATYX48 | Yes | 4.73 |
| 12 | TJZ9N3WWA4Q3 | TJZ9N3WWA4Q3 | Yes | 1.59 |
| 13 | DRDYCG6PJCRI | DRDYCG6PJCRI | Yes | 1.82 |
| 14 | 1LG6L5A72N8P | 1LG6L5A72N8P | Yes | 1.36 |
| 15 | E9QM0JCCR2N7 | E9QM0JCCR2N7 | Yes | 2.02 |
| 16 | 2WMMKBCIYHL7 | 2WMMKBCIYHL7 | Yes | 2.07 |
| 17 | S043ZM9ECU94 | S043ZM9ECU94 | Yes | 1.75 |
| 18 | WU39YNEVHXWD | WU39YNEVHXWD | Yes | 2.08 |
| 19 | 0FBO8L4137D9 | 0FBO8L4137D9 | Yes | 2.24 |
| 20 | RFUWN0DEUF8G | RFUWN0DEUF8G | Yes | 2.28 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 65 | Yes | 2.54 |
| 2 | 3 | 3 | Yes | 2.58 |
| 3 | 7 | 7 | Yes | 2.05 |
| 4 | 60 | 60 | Yes | 2.14 |
| 5 | 20 | 20 | Yes | 4.62 |
| 6 | 63 | 63 | Yes | 2.32 |
| 7 | 243 | 243 | Yes | 1.91 |
| 8 | 19 | 19 | Yes | 1.94 |
| 9 | 4096 | 1048576 | No | 6.99 |
| 10 | 48 | 48 | Yes | 1.91 |
| 11 | 4 | 4 | Yes | 4.8 |
| 12 | 1 | 1 | Yes | 2.71 |
| 13 | 1440 | 1440 | Yes | 3.38 |
| 14 | 31 | 31 | Yes | 1.91 |
| 15 | 23 | 23 | Yes | 2.1 |
| 16 | 64 | 64 | Yes | 2.11 |
| 17 | 5 | 5 | Yes | 2.51 |
| 18 | 793 | 793 | Yes | 1.6 |
| 19 | 10 | 10 | Yes | 1.8 |
| 20 | 28 | 28 | Yes | 1.79 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /_\)/<_(_ | /_\)/<_(_ | Yes | 2.81 |
| 2 | (</\< \ ) | (</ \< \ ) | No | 3.96 |
| 3 |  \</( <<  | \</(  << | No | 3.34 |
| 4 | \////))(/ | \////))(/ | Yes | 2.62 |
| 5 | /\(\_/) / | /\(\_/) / | Yes | 8.23 |
| 6 | _<)__(((/ | _<)__(((/ | Yes | 2.46 |
| 7 | )/()\(\<( | )/()\(\<( | Yes | 1.91 |
| 8 | )< _(_) ) | )< _(_) ) | Yes | 2.36 |
| 9 | )//<((/(  | )//<((/( | No | 2.27 |
| 10 | ((\ <) __ | ((\ <) __ | Yes | 2.48 |
| 11 | )<( ((/<\ | )<( ((/<\ | Yes | 2.92 |
| 12 | /<<\_)  < | /<<\_) | No | 2.0 |
| 13 | <_/) \\() | <_/) \\() | Yes | 3.28 |
| 14 | \) <__(/_ | \) <__(/_ | Yes | 2.26 |
| 15 | </\\_/ (\ | </\\_/ (\ | Yes | 2.42 |
| 16 | ( <()/ () | ( <()/ () | Yes | 3.97 |
| 17 |  \<_()<)< | \<_()<) | No | 2.23 |
| 18 | _\ /(</\\ | _\ /(</\\ | Yes | 2.58 |
| 19 | )(<<(  (\ | )(<<(  (\ | Yes | 2.57 |
| 20 | / (//__/  | / (//__/ | No | 2.6 |
