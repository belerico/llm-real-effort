# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-27 09:55:41

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
| sudoku_game | 6696 | 31472 | 38168 | 1 | 19 | 10.93 | 218.6 |
| add_numbers | 4080 | 2611 | 6691 | 20 | 0 | 2.63 | 52.67 |
| counting_zeros | 5400 | 22688 | 28088 | 1 | 19 | 7.58 | 151.6 |
| task_decoding | 5400 | 6629 | 12029 | 19 | 1 | 2.92 | 58.44 |
| task_summation | 5460 | 15186 | 20646 | 20 | 0 | 5.74 | 114.75 |
| task_transcription | 4227 | 2630 | 6857 | 20 | 0 | 2.02 | 40.35 |
| task_sequences | 4140 | 5779 | 9919 | 20 | 0 | 3.00 | 59.9 |
| string_entry | 4618 | 5080 | 9698 | 8 | 12 | 3.57 | 71.5 |
| **TOTAL** | **40021** | **92075** | **132096** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1 2 3 4 5 2 6 6 1 5 4 5 6 1 | 1 2 3 4 5 2 6 6 1 5 4 5 1 6 | No | 10.43 |
| 2 | 5 1 3 2 6 6 3 2 5 4 2 1 1 4 | 6 1 4 3 1 2 5 6 5 2 2 3 2 1 | No | 8.43 |
| 3 | 6 4 5 1 6 5 3 4 1 2 6 5 2 4 | 6 4 5 1 6 5 3 4 2 1 6 5 1 4 | No | 9.56 |
| 4 | 4 6 3 2 4 4 2 4 3 1 3 2 4 5 | 4 3 6 2 4 4 2 4 3 1 3 2 4 5 | No | 10.19 |
| 5 | 5 4 3 5 1 2 5 5 3 6 5 1 1 5 | 5 4 3 5 1 2 5 5 3 6 1 5 1 5 | No | 8.35 |
| 6 | 1 4 5 5 3 5 6 1 6 2 5 5 4 3 | 1 4 5 5 3 6 1 5 6 1 2 5 5 4 3** | No | 9.91 |
| 7 | 4 6 4 6 4 4 6 6 5 1 4 2 5 4 | 4 4 6 4 6 4 4 6 6 5 1 2 5 4** | No | 16.21 |
| 8 | 5 2 1 2 3 6 2 4 6 3 4 2 5 3 | 2 5 1 2 6 3 2 4 3 6 2 5 3 | No | 20.57 |
| 9 | 2 4 3 5 3 6 1 5 5 3 4 3 3 5 | 2 4 3 5 3 6 1 5 5 3 3 4 3 5 | No | 13.95 |
| 10 | 2 6 4 5 6 6 4 3 2 3 5 3 1 4 | 2 6 4 5 6 4 3 4 5 3 1 5 4** | No | 10.84 |
| 11 | 2 6 1 4 5 6 2 6 1 4 5 6 1 2 | 2 6 6 4 1 2 5 3 4 2 5 1 5 6 2 1** | No | 10.39 |
| 12 | 2 5 3 4 6 5 6 5 6 3 4 1 3 1 | 5 6 3 2 6 5 5 3 1 4 6 3 1** | No | 10.0 |
| 13 | 4 6 2 5 6 2 1 6 4 4 2 6 4 3 | 4 6 2 5 6 2 4 6 1 4 2 6 4 3 | No | 7.38 |
| 14 | 3 5 1 5 6 3 4 3 2 3 2 5 1 2 |  | No | 11.49 |
| 15 | 3 6 2 1 5 2 5 1 1 2 5 4 4 1 | 1 2 3 5 1 2 5 1 1 2 5 4 4 1 | No | 7.9 |
| 16 | 4 1 5 1 2 5 6 3 6 6 5 4 5 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Let me work through the empty cells:  **Row 1:** 2 3 6 \| ? ? ? (needs 1, 4, 5) **Row 2:** 5 6 3 \| ? 4 ? (needs 1, 2) **Row 3:** 1 4 ? \| 2 ? 3 (needs 5, 6) **Row 4:** 4 5 1 \| ? 2 ? (needs 3, 6) **Row 5:** 3 1 2 \| ? ? ? (needs 4, 5, 6) **Row 6:** 6 2 4 \| ? 3 ? (needs 1, 5)  **Solving by constraints:**  Row 3, Col 3: Row needs 5,6; Col 3 has 6,3,1,2,4 → must be **5** Row 2, Col 4: Row needs 1,2; Col 4 has 2 → must be **1** Row 2, Col 6: Row needs 2 → must be **2** Row 1, Col 4: Row needs 1,4,5; Col 4 has 2,1 → must be **4** Row 1, Col 5: Row needs 1,5; Col 5 has 4,2,3 → must be **5** Row 1, Col 6: Row needs 1 → must be **1** Row 3, Col 5: Row needs 6; Col 5 has 4,5,2,3 → must be **6** Row 4, Col 4: Row needs 3,6; Col 4 has 2,1,4 → must be **3** Row 4, Col 6: Row needs 6 | No | 11.4 |
| 17 | 1 5 3 4 3 2 5 3 6 5 5 3 2 6 | 5 1 3 4 2 3 5 3 6 3 5 2 6 | No | 7.72 |
| 18 | 1 6 3 5 6 6 4 5 1 2 6 3 1 5 | 1 6 3 5 6 4 5 1 2 6 3 1 5 | No | 9.88 |
| 19 | 4 6 1 5 3 1 3 6 2 5 2 1 2 4 | 4 6 1 5 3 2 1 6 3 5 1 | No | 11.17 |
| 20 | 3 4 2 3 1 1 6 5 6 4 4 4 6 5 | 3 4 2 3 1 1 6 5 6 4 4 4 6 5 | Yes | 12.81 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 929 | 929 | Yes | 2.98 |
| 2 | 2138 | 2138 | Yes | 2.26 |
| 3 | 1419 | 1419 | Yes | 1.61 |
| 4 | 2276 | 2276 | Yes | 2.0 |
| 5 | 2200 | 2200 | Yes | 1.79 |
| 6 | 1725 | 1725 | Yes | 1.4 |
| 7 | 2209 | 2209 | Yes | 1.71 |
| 8 | 1297 | 1297 | Yes | 1.74 |
| 9 | 1497 | 1497 | Yes | 2.23 |
| 10 | 2011 | 2011 | Yes | 2.5 |
| 11 | 1073 | 1073 | Yes | 2.68 |
| 12 | 1988 | 1988 | Yes | 2.58 |
| 13 | 2242 | 2242 | Yes | 1.71 |
| 14 | 1450 | 1450 | Yes | 2.1 |
| 15 | 1839 | 1839 | Yes | 3.65 |
| 16 | 1649 | 1649 | Yes | 11.6 |
| 17 | 1608 | 1608 | Yes | 2.08 |
| 18 | 2124 | 2124 | Yes | 1.62 |
| 19 | 1866 | 1866 | Yes | 2.41 |
| 20 | 1695 | 1695 | Yes | 1.99 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 61 | No | 7.74 |
| 2 | 36 | 37 | No | 9.1 |
| 3 | 42 | 35 | No | 5.35 |
| 4 | 49 | 54 | No | 5.45 |
| 5 | 62 | 65 | No | 8.35 |
| 6 | 40 | 39 | No | 6.45 |
| 7 | 63 | 49 | No | 6.52 |
| 8 | 44 | 45 | No | 14.22 |
| 9 | 42 | 37 | No | 6.76 |
| 10 | 47 | 32 | No | 6.05 |
| 11 | 55 | 55 | Yes | 7.09 |
| 12 | 60 | 54 | No | 5.02 |
| 13 | 39 | 37 | No | 12.82 |
| 14 | 42 | 41 | No | 8.17 |
| 15 | 56 | 49 | No | 6.46 |
| 16 | 60 | 51 | No | 7.02 |
| 17 | 49 | 43 | No | 7.6 |
| 18 | 68 | 50 | No | 7.51 |
| 19 | 38 | 35 | No | 6.75 |
| 20 | 39 | 36 | No | 7.16 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ZYKOEIN | ZYKOEIN | Yes | 5.42 |
| 2 | LIGZYVS | LIGZYVS | Yes | 2.75 |
| 3 | TVOQSUK | TVOQUSK | No | 2.54 |
| 4 | IKGNBOY | IKGNBOY | Yes | 2.64 |
| 5 | IWLBAGK | IWLBAGK | Yes | 2.86 |
| 6 | FORMXAQ | FORMXAQ | Yes | 2.84 |
| 7 | JCNOHSZ | JCNOHSZ | Yes | 3.65 |
| 8 | KLXABPT | KLXABPT | Yes | 2.69 |
| 9 | VXUZDYF | VXUZDYF | Yes | 2.31 |
| 10 | SAUHZKM | SAUHZKM | Yes | 3.22 |
| 11 | MPNRYDH | MPNRYDH | Yes | 2.83 |
| 12 | CADSVKX | CADSVKX | Yes | 2.38 |
| 13 | DYHGJZE | DYHGJZE | Yes | 2.51 |
| 14 | NUAWIQX | NUAWIQX | Yes | 3.5 |
| 15 | DZEPWHR | DZEPWHR | Yes | 2.45 |
| 16 | CYEMTWV | CYEMTWV | Yes | 2.63 |
| 17 | JPHDLRW | JPHDLRW | Yes | 3.72 |
| 18 | DFKXTPJ | DFKXTPJ | Yes | 2.29 |
| 19 | HRXOBIJ | HRXOBIJ | Yes | 2.5 |
| 20 | XZIUCPM | XZIUCPM | Yes | 2.71 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.23 |
| 2 | [1.8, 8.2] | 8.2 1.8 | Yes | 5.24 |
| 3 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.33 |
| 4 | [2.2, 7.8] | 2.2 7.8 | Yes | 6.44 |
| 5 | [1.7, 8.3] | 1.7 8.3 | Yes | 4.53 |
| 6 | [2.8, 7.2] | 2.8 7.2 | Yes | 6.26 |
| 7 | [0.5, 9.5] | 9.5 0.5 | Yes | 7.15 |
| 8 | [4.7, 5.3] | 5.3 4.7 | Yes | 4.84 |
| 9 | [0.3, 9.7] | 0.3 9.7 | Yes | 5.26 |
| 10 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.62 |
| 11 | [3.1, 6.9] | 3.1 6.9 | Yes | 5.69 |
| 12 | [1.8, 8.2] | 1.8 8.2 | Yes | 4.45 |
| 13 | [3.5, 6.5] | 6.5 3.5 | Yes | 5.2 |
| 14 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.45 |
| 15 | [1.5, 8.5] | 1.5 8.5 | Yes | 5.06 |
| 16 | [3.6, 6.4] | 3.6 6.4 | Yes | 14.6 |
| 17 | [1.4, 8.6] | 8.6 1.4 | Yes | 5.0 |
| 18 | [0.1, 9.9] | 9.9 0.1 | Yes | 4.29 |
| 19 | [2.9, 7.1] | 2.9 7.1 | Yes | 4.35 |
| 20 | [4.6, 5.4] | 4.6 5.4 | Yes | 4.72 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6QNGOOZEO7OF | 6QNGOOZEO7OF | Yes | 1.98 |
| 2 | UYRE2NC7S25B | UYRE2NC7S25B | Yes | 1.75 |
| 3 | 0GO6EVNDX725 | 0GO6EVNDX725 | Yes | 2.24 |
| 4 | 5TXCZJDOVRQN | 5TXCZJDOVRQN | Yes | 2.26 |
| 5 | C79GP8Y0UPPU | C79GP8Y0UPPU | Yes | 2.18 |
| 6 | J7LIJCG1P7VP | J7LIJCG1P7VP | Yes | 1.94 |
| 7 | SGGN67OGD6O5 | SGGN67OGD6O5 | Yes | 1.81 |
| 8 | OU9GVAKQ3C9V | OU9GVAKQ3C9V | Yes | 2.35 |
| 9 | FAT6BONHRWLS | FAT6BONHRWLS | Yes | 1.7 |
| 10 | 0USNIRZDU2TV | 0USNIRZDU2TV | Yes | 2.86 |
| 11 | OQA17GZ68XWE | OQA17GZ68XWE | Yes | 2.83 |
| 12 | O1MROFUXRTRC | O1MROFUXRTRC | Yes | 1.83 |
| 13 | T0WKNWYLENR8 | T0WKNWYLENR8 | Yes | 1.88 |
| 14 | LEIKTHW6Z3SX | LEIKTHW6Z3SX | Yes | 1.87 |
| 15 | 4TMJAFNYVZO1 | 4TMJAFNYVZO1 | Yes | 1.54 |
| 16 | ZHJ69BD4GN0S | ZHJ69BD4GN0S | Yes | 1.78 |
| 17 | BR0ZWTILMG75 | BR0ZWTILMG75 | Yes | 1.91 |
| 18 | FDYJHJURQVDA | FDYJHJURQVDA | Yes | 1.66 |
| 19 | PYKAXSVB3JUP | PYKAXSVB3JUP | Yes | 1.64 |
| 20 | WOG7CWF21E0V | WOG7CWF21E0V | Yes | 2.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 19 | 19 | Yes | 5.18 |
| 2 | 793 | 793 | Yes | 1.89 |
| 3 | 63 | 63 | Yes | 2.31 |
| 4 | 60 | 60 | Yes | 2.28 |
| 5 | 6 | 6 | Yes | 2.51 |
| 6 | 65 | 65 | Yes | 2.11 |
| 7 | 3 | 3 | Yes | 4.67 |
| 8 | 26 | 26 | Yes | 2.98 |
| 9 | 7680 | 7680 | Yes | 2.04 |
| 10 | 10 | 10 | Yes | 2.16 |
| 11 | 48 | 48 | Yes | 2.91 |
| 12 | 36 | 36 | Yes | 1.69 |
| 13 | 73 | 73 | Yes | 7.27 |
| 14 | 7 | 7 | Yes | 1.67 |
| 15 | 1 | 1 | Yes | 3.79 |
| 16 | 39 | 39 | Yes | 2.93 |
| 17 | 9 | 9 | Yes | 3.71 |
| 18 | 31 | 31 | Yes | 1.84 |
| 19 | 28 | 28 | Yes | 2.37 |
| 20 | 3 | 3 | Yes | 3.59 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  /\\__<\( | /\\__<\( | No | 3.37 |
| 2 | /(\)//)_\ | /(\)//)_\ | Yes | 2.28 |
| 3 | \<<\<_/<) | \<<\<_/<) | Yes | 2.26 |
| 4 | _(()</ (_ | _(()</ (_ | Yes | 4.14 |
| 5 | __\)(_<\  | __\)(_<\ | No | 2.8 |
| 6 | )) \<(  ) | ))  \<(  ) | No | 2.96 |
| 7 | (<_\)\//) | (<_\)\//) | Yes | 4.61 |
| 8 |  </) /<\( | </) /<\( | No | 2.52 |
| 9 | )\(<__/   | )\(<__/ | No | 2.35 |
| 10 | _\/__<(<( | _\/__<(<( | Yes | 2.17 |
| 11 | _/())/ )( | _/())/ )( | Yes | 3.35 |
| 12 | \)  ) \ < | \)  ) \ | No | 2.29 |
| 13 | ) </(<<)( | /\) <(_<) | No | 18.28 |
| 14 | )\\\ <_)  | )\\\ <_) | No | 2.94 |
| 15 |  )(\<_ _\ | )(\<_ _\ | No | 3.15 |
| 16 | <__\( ))< | <__\( )) | No | 2.44 |
| 17 | )(/<\/)(  | )(/<\/)( | No | 2.49 |
| 18 | (<) (<\<\ | (<) (<\<\ | Yes | 2.3 |
| 19 | /_  /</_< | /_  /</_ | No | 2.48 |
| 20 | _ <_\ _<) | _ <_\ _<) | Yes | 2.31 |
