# Benchmark Report — claude-sonnet-4.6

- **Model**: `anthropic/claude-sonnet-4.6`
- **Date**: 2026-03-19 03:16:59

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
| sudoku_game | 8600 | 35480 | 44080 | 11 | 9 | 28.29 | 565.89 |
| add_numbers | 4520 | 703 | 5223 | 20 | 0 | 2.30 | 46.06 |
| counting_zeros | 7460 | 27805 | 35265 | 6 | 14 | 15.78 | 315.99 |
| task_decoding | 13900 | 4939 | 18839 | 20 | 0 | 5.08 | 101.75 |
| task_summation | 7820 | 2940 | 10760 | 20 | 0 | 3.46 | 69.37 |
| task_transcription | 4660 | 843 | 5503 | 20 | 0 | 2.38 | 47.67 |
| task_sequences | 3781 | 3602 | 7383 | 19 | 1 | 3.54 | 70.87 |
| **TOTAL** | **50741** | **76312** | **127053** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 3 5 4 5 6 3 5 6 3 2 3 2 6 | 3 3 5 4 5 6 3 5 6 3 2 3 2 6 | Yes | 21.25 |
| 2 | 2 4 6 2 1 5 4 3 6 1 3 5 4 3 |  | No | 35.96 |
| 3 | 6 4 5 6 2 1 4 5 3 6 2 5 5 6 | Looking at this 6×6 Sudoku, I'll solve it systematically.  **Given grid:** \| 3 \| 1 \| _ \| _ \| 2 \| _ \| \| 5 \| _ \| 3 \| _ \| 4 \| _ \| \| _ \| 2 \| 1 \| _ \| 6 \| 3 \| \| 2 \| 4 \| 5 \| _ \| 1 \| _ \| \| 6 \| 3 \| _ \| 1 \| _ \| 4 \| \| 1 \| _ \| 4 \| _ \| 3 \| 2 \|  **Step-by-step solving:**  - **Col 1:** has {3,5,2,6,1} → Row 3, C1 = **4** - **Col 5:** has {2,4,6,1,3} → Row 5, C5 = **5** - **Row 3:** has | No | 32.71 |
| 4 | 3 5 1 4 3 1 6 3 1 6 4 5 1 2 | 3 5 1 4 3 1 6 3 1 6 4 5 1 2 | Yes | 20.49 |
| 5 | 1 2 6 1 2 3 4 2 6 3 1 3 2 3 |  | No | 33.79 |
| 6 | 2 4 6 3 5 5 6 1 6 4 6 2 4 3 | 2 4 6 3 5 5 6 1 6 4 6 3 4 2 | No | 24.78 |
| 7 | 4 5 6 6 4 5 4 3 5 2 6 5 4 3 | 4 5 6 6 4 5 4 3 5 2 6 5 4 3 | Yes | 27.89 |
| 8 | 3 5 6 4 2 4 3 6 1 2 6 1 2 3 | 3 5 6 4 2 4 3 6 1 2 6 1 2 3 | Yes | 21.61 |
| 9 | 3 4 6 2 6 1 4 2 3 6 2 5 3 4 | 3 4 6 2 6 1 4 2 3 6 2 5 3 4 | Yes | 26.33 |
| 10 | 2 2 5 6 1 3 5 2 6 3 1 3 6 2 | 2 2 5 6 1 3 5 2 6 3 1 3 6 2 | Yes | 28.09 |
| 11 | 5 3 1 2 6 5 1 6 5 3 3 1 6 2 |  | No | 37.25 |
| 12 | 3 5 4 6 4 2 1 2 5 6 3 6 3 1 | 3 5 4 6 4 2 1 2 5 6 3 6 3 1 | Yes | 21.46 |
| 13 | 1 1 5 3 4 2 1 3 1 5 4 2 1 6 | 1 1 5 3 4 2 1 3 1 5 | No | 34.01 |
| 14 | 4 5 2 5 6 5 2 1 3 4 5 3 1 3 | 4 5 2 5 6 5 2 1 3 4 5 3 1 3 | Yes | 25.58 |
| 15 | 3 4 1 5 1 3 1 1 3 6 2 4 5 1 | 3 4 1 5 1 3 1 1 3 6 2 4 5 1 | Yes | 28.65 |
| 16 | 1 6 3 1 2 4 6 5 1 6 2 3 1 1 |  | No | 35.19 |
| 17 | 3 4 1 1 2 5 3 1 5 5 3 1 4 5 |  | No | 34.11 |
| 18 | 2 4 5 6 4 3 2 6 5 3 4 1 2 3 | 2 4 5 6 4 3 4 6 5 3 2 4 1 3 | No | 31.99 |
| 19 | 6 3 5 1 6 2 1 5 6 3 5 1 3 4 | 6 3 5 1 6 2 1 5 6 3 5 1 3 4 | Yes | 24.96 |
| 20 | 1 5 1 2 5 3 6 1 3 4 5 2 5 6 | 1 5 1 2 5 3 6 1 3 4 5 2 5 6 | Yes | 19.6 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2409 | 2409 | Yes | 2.65 |
| 2 | 1446 | 1446 | Yes | 2.45 |
| 3 | 1216 | 1216 | Yes | 2.77 |
| 4 | 2163 | 2163 | Yes | 2.14 |
| 5 | 1848 | 1848 | Yes | 2.08 |
| 6 | 1291 | 1291 | Yes | 2.19 |
| 7 | 1626 | 1626 | Yes | 2.5 |
| 8 | 1984 | 1984 | Yes | 2.53 |
| 9 | 2048 | 2048 | Yes | 2.46 |
| 10 | 2040 | 2040 | Yes | 3.01 |
| 11 | 1797 | 1797 | Yes | 1.64 |
| 12 | 1085 | 1085 | Yes | 2.23 |
| 13 | 1139 | 1139 | Yes | 2.18 |
| 14 | 2075 | 2075 | Yes | 2.5 |
| 15 | 1132 | 1132 | Yes | 2.22 |
| 16 | 858 | 858 | Yes | 1.95 |
| 17 | 2119 | 2119 | Yes | 2.01 |
| 18 | 1141 | 1141 | Yes | 1.55 |
| 19 | 1267 | 1267 | Yes | 2.2 |
| 20 | 2082 | 2082 | Yes | 2.69 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 53 | 53 | Yes | 13.59 |
| 2 | 61 | 57 | No | 16.16 |
| 3 | 61 | 58 | No | 17.9 |
| 4 | 70 | 67 | No | 20.27 |
| 5 | 49 | 49 | Yes | 15.53 |
| 6 | 70 | 67 | No | 13.34 |
| 7 | 70 | 64 | No | 16.31 |
| 8 | 59 | 58 | No | 17.7 |
| 9 | 66 | 66 | Yes | 14.92 |
| 10 | 50 | 50 | Yes | 18.58 |
| 11 | 50 | 49 | No | 13.69 |
| 12 | 71 | 68 | No | 13.17 |
| 13 | 35 | 35 | Yes | 12.87 |
| 14 | 58 | 56 | No | 17.64 |
| 15 | 59 | 52 | No | 15.09 |
| 16 | 53 | I'll count the zeros in each row systematically:  Row 1: **0** 1 **0** 1 **0** **0** 1 **0** **0** **0** → 6 zeros Row 2: 1 1 1 1 1 **0** **0** 1 **0** 1 → 3 zeros Row 3: 1 **0** **0** **0** **0** 1 **0** **0** 1 1 → 6 zeros Row 4: 1 1 1 1 1 1 **0** 1 1 1 → 1 zero Row 5: 1 1 **0** 1 **0** **0** **0** 1 1 1 → 4 zeros Row 6: 1 **0** 1 1 1 1 1 **0** 1 **0** → 3 zeros Row 7: 1 1 1 1 1 **0** **0** 1 1 1 → 2 zeros Row 8: 1 **0** **0** 1 1 **0** **0** 1 **0** 1 → 5 zeros Row 9: **0** 1 1 1 1 1 1 **0** 1 1 → 2 zeros Row 10: 1 1 1 1 1 1 1 1 1 **0** → 1 zero Row 11: **0** 1 1 1 **0** **0** 1 **0** 1 1 → 4 zeros Row 12: 1 **0** **0** 1 1 **0** 1 **0** 1 1 → 4 zeros Row 13: 1 1 1 **0** 1 1 1 **0** **0** 1 → 3 zeros Row 14: 1 1 **0** **0** 1 1 **0** 1 1 1 → 3 zeros Row 15: **0** 1 **0** 1 1 **0** 1 1 **0** **0** → 5 zeros  Total: 6+3+6+1+4+3+2+5+2+1+4+4+3+3+ | No | 23.18 |
| 17 | 74 | 74 | Yes | 14.38 |
| 18 | 58 | 67 | No | 13.36 |
| 19 | 65 | 67 | No | 15.24 |
| 20 | 37 | 36 | No | 12.72 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | FRZOLAX | FRZOLAX | Yes | 4.42 |
| 2 | HSPXLBR | HSPXLBR | Yes | 5.15 |
| 3 | IWZFXCR | IWZFXCR | Yes | 4.55 |
| 4 | QZYPGBI | QZYPGBI | Yes | 4.61 |
| 5 | CZUKSPI | CZUKSPI | Yes | 5.63 |
| 6 | AMEDIZT | AMEDIZT | Yes | 5.28 |
| 7 | HITWBVO | HITWBVO | Yes | 4.76 |
| 8 | CBRPQEO | CBRPQEO | Yes | 5.6 |
| 9 | CMOWSHB | CMOWSHB | Yes | 5.44 |
| 10 | YLSMVHO | YLSMVHO | Yes | 4.8 |
| 11 | XTGYNJR | XTGYNjr | Yes | 5.62 |
| 12 | FSEIKPB | FSEIKPB | Yes | 5.51 |
| 13 | NVAFJZC | NVAFJZC | Yes | 5.02 |
| 14 | SKBZQDY | SKBZQDY | Yes | 5.09 |
| 15 | FWZCGNU | FWZCGNU | Yes | 4.63 |
| 16 | MYJITOV | MYJITOV | Yes | 5.69 |
| 17 | LFYJGSH | LFYJGSH | Yes | 4.81 |
| 18 | IDLJSFK | IDLJSFK | Yes | 5.01 |
| 19 | PBDFKZJ | PBDFKZJ | Yes | 5.32 |
| 20 | SWRNIUP | SWRNIUP | Yes | 4.6 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.8, 6.2] | 6.2 3.8 | Yes | 2.46 |
| 2 | [1.1, 8.9] | 8.9 1.1 | Yes | 2.53 |
| 3 | [3.8, 6.2] | 3.8 6.2 | Yes | 6.13 |
| 4 | [3.5, 6.5] | 3.5 6.5 | Yes | 2.53 |
| 5 | [2.8, 7.2] | 2.8 7.2 | Yes | 4.17 |
| 6 | [3.3, 6.7] | 6.7 3.3 | Yes | 3.63 |
| 7 | [1.8, 8.2] | 8.2 1.8 | Yes | 3.44 |
| 8 | [4.1, 5.9] | 5.9 4.1 | Yes | 3.74 |
| 9 | [2.6, 7.4] | 7.4 2.6 | Yes | 2.66 |
| 10 | [4.5, 5.5] | 4.5 5.5 | Yes | 4.57 |
| 11 | [3.1, 6.9] | 3.1 6.9 | Yes | 2.88 |
| 12 | [0.8, 9.2] | 0.8 9.2 | Yes | 3.34 |
| 13 | [0.8, 9.2] | 9.2 0.8 | Yes | 4.64 |
| 14 | [4.0, 6.0] | 6.0 4.0 | Yes | 3.01 |
| 15 | [4.8, 5.2] | 5.2 4.8 | Yes | 4.12 |
| 16 | [2.3, 7.7] | 7.7 2.3 | Yes | 3.19 |
| 17 | [2.5, 7.5] | 7.5 2.5 | Yes | 2.23 |
| 18 | [0.4, 9.6] | 0.4 9.6 | Yes | 2.75 |
| 19 | [0.7, 9.3] | 0.7 9.3 | Yes | 4.43 |
| 20 | [1.9, 8.1] | 8.1 1.9 | Yes | 2.71 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9RC965QN7X3K | 9RC965QN7X3K | Yes | 1.67 |
| 2 | 4F1S0HXU1UBG | 4F1S0HXU1UBG | Yes | 2.43 |
| 3 | 3GRCVW1PTDKK | 3GRCVW1PTDKK | Yes | 2.1 |
| 4 | R0MKKVLGIRG2 | R0MKKVLGIRG2 | Yes | 1.77 |
| 5 | XRTKS3NOZG08 | XRTKS3NOZG08 | Yes | 2.31 |
| 6 | O26O44H47NL7 | O26O44H47NL7 | Yes | 3.02 |
| 7 | DHGZXFIGYTE4 | DHGZXFIGYTE4 | Yes | 4.61 |
| 8 | YMP7TFCI2NMW | YMP7TFCI2NMW | Yes | 2.53 |
| 9 | XI8MTPFJ3J71 | XI8MTPFJ3J71 | Yes | 2.49 |
| 10 | M0GYAJA6Q67E | M0GYAJA6Q67E | Yes | 2.48 |
| 11 | Q46G7KUR8JTQ | Q46G7KUR8JTQ | Yes | 2.59 |
| 12 | 9OMBLNGO3P9T | 9OMBLNGO3P9T | Yes | 2.19 |
| 13 | RQNG3ROPFK9S | RQNG3ROPFK9S | Yes | 2.24 |
| 14 | 9F9RRLRKXI4O | 9F9RRLRKXI4O | Yes | 2.31 |
| 15 | 2EZDL6B2FN0S | 2EZDL6B2FN0S | Yes | 1.98 |
| 16 | 7PXOV83XUYOY | 7PXOV83XUYOY | Yes | 1.87 |
| 17 | NH1KXSNQ1Y68 | NH1KXSNQ1Y68 | Yes | 2.38 |
| 18 | FDHZD2637YR6 | FDHZD2637YR6 | Yes | 1.88 |
| 19 | ZPA5YOKMKH1N | ZPA5YOKMKH1N | Yes | 2.16 |
| 20 | GVADSXLH3OBJ | GVADSXLH3OBJ | Yes | 2.53 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 | 4 | Yes | 3.26 |
| 2 | 60 | 60 | Yes | 2.2 |
| 3 | 60 | 60 | Yes | 1.77 |
| 4 | 65 | 65 | Yes | 2.06 |
| 5 | 6 | 6 | Yes | 3.27 |
| 6 | 23 | 23 | Yes | 1.81 |
| 7 | 243 | 243 | Yes | 1.58 |
| 8 | 19 | 19 | Yes | 2.22 |
| 9 | 36 | 36 | Yes | 1.64 |
| 10 | 4096 | 16384 | No | 11.96 |
| 11 | 1 | 1 | Yes | 3.92 |
| 12 | 26 | 26 | Yes | 8.02 |
| 13 | 10 | 10 | Yes | 2.29 |
| 14 | 39 | 39 | Yes | 4.19 |
| 15 | 63 | 63 | Yes | 2.2 |
| 16 | 7 | 7 | Yes | 1.2 |
| 17 | 16 | 16 | Yes | 2.6 |
| 18 | 3 | 3 | Yes | 6.14 |
| 19 | 3 | 3 | Yes | 5.78 |
| 20 | 73 | 73 | Yes | 2.75 |
