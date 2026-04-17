# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-19 03:07:05

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
| sudoku_game | 8960 | 35331 | 44291 | 9 | 11 | 29.28 | 585.79 |
| add_numbers | 4880 | 618 | 5498 | 20 | 0 | 3.29 | 65.78 |
| counting_zeros | 7820 | 21913 | 29733 | 6 | 14 | 14.04 | 281.24 |
| task_decoding | 14260 | 3466 | 17726 | 20 | 0 | 6.26 | 125.41 |
| task_summation | 8180 | 6200 | 14380 | 20 | 0 | 7.34 | 146.92 |
| task_transcription | 5020 | 991 | 6011 | 19 | 1 | 3.84 | 76.97 |
| task_sequences | 4141 | 4429 | 8570 | 20 | 0 | 5.21 | 104.27 |
| **TOTAL** | **53261** | **72948** | **126209** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 4 5 1 4 3 2 2 4 2 2 1 4 6 |  | No | 36.03 |
| 2 | 5 4 5 2 6 6 5 1 2 4 4 6 2 3 |  | No | 35.88 |
| 3 | 1 1 5 3 6 4 2 2 4 1 3 4 2 6 | Looking at this puzzle, I need to find all missing numbers by applying Sudoku constraints for rows, columns, and 2×3 boxes.  **Row-by-row analysis:**  **Row 1:** 4, 6, _, 2, 5, 3 → missing **1** **Row 2:** 2, _, 3, _, 6, 4 → missing 1, 5 **Row 3:** _, 5, _, _, 1, _ → missing several **Row 4:** 6, _, 5, 3, _, _ → missing several **Row 5:** 5, _, 4, 1, 2, 6 → missing **3** **Row 6:** 1, _, _, _, 3, 5 → missing 2, 4, 6  **Column analysis to pin | No | 34.82 |
| 4 | 2 6 3 6 5 1 6 2 1 1 2 6 4 3 | 2 6 3 6 5 1 6 2 1 1 2 6 4 3 | Yes | 23.11 |
| 5 | 6 1 5 2 4 5 3 5 3 4 1 4 2 5 |  | No | 37.87 |
| 6 | 4 1 6 3 1 1 2 3 4 1 4 1 6 3 | 4 1 6 3 1 1 2 3 4 1 4 1 6 3 | Yes | 32.85 |
| 7 | 2 6 5 4 2 2 5 2 1 6 5 5 2 4 | Looking at this puzzle, I need to find all missing numbers by applying Sudoku logic to rows, columns, and 2×3 boxes.  **Starting with the easier cells:**  **Row 2:** 5, 4, _, 3, 1, 6 → missing **2** **Row 3:** 1, 6, 4, 5, _, 3 → missing **2** **Row 4:** 3, 1, _, 4, 6, 2 → missing **5**  **Column 1:** _, 5, 1, 3, 4, 6 → missing **2** → Row 1, Col 1 = **2**  **Now Row 1:** 2, 3, _, 1, _, _ → needs 4, 5, 6 - Column 3 has 2, 4, 5, 3 → needs 1, 6 → Row 1 Col 3 = **6** - Box (rows 1-2, cols 1-3) has 2, 3, 6, 5, 4, 2 → confirms placement  **Row 5 Col 3:** Column 3 now needs **1** → Row 5 Col 3 = **1**  **Row 1 remaining (cols 5, 6):** needs 4, 5 - Column 6 has 6, 3, 2, 1 → needs 4, 5 - Column 5 has 1, 2, 6, 3 → needs 4, 5 - Box (rows 1-2, cols 4-6): has 1, 3, 1, 6 → using 3×2 box logic: Row | No | 35.7 |
| 8 | 3 4 4 3 6 1 1 3 5 6 4 2 4 3 | 3 4 4 3 6 1 1 3 5 6 4 2 4 3 | Yes | 19.53 |
| 9 | 1 3 1 2 6 3 4 6 4 2 1 2 6 5 | 1 3 1 2 6 3 4 6 4 2 1 2 6 5 | Yes | 20.04 |
| 10 | 3 6 1 4 3 1 6 2 4 3 5 2 4 6 | 3 6 1 3 1 4 6 2 4 3 5 2 4 6 | No | 31.01 |
| 11 | 4 2 6 2 1 3 3 2 5 1 4 5 1 6 | 4 2 6 2 1 3 3 2 5 1 4 5 1 3 6 | No | 23.9 |
| 12 | 5 2 1 6 3 5 6 2 2 3 6 5 4 3 | 5 2 1 6 3 5 6 2 2 3 6 5 4 3 | Yes | 20.92 |
| 13 | 2 5 6 4 1 6 3 3 6 5 4 6 3 2 |  | No | 33.96 |
| 14 | 2 5 1 6 3 5 4 6 3 2 4 4 2 4 | 2 5 1 6 3 5 4 6 3 2 4 4 2 4 | Yes | 19.69 |
| 15 | 5 2 4 1 5 4 1 5 6 2 3 5 3 6 |  | No | 37.69 |
| 16 | 1 6 6 6 4 5 5 3 4 3 1 5 3 6 | 1 6 6 6 4 5 5 3 4 3 1 5 3 6 | Yes | 24.22 |
| 17 | 5 3 1 4 6 2 2 6 1 5 6 2 4 3 | 5 3 1 4 6 2 2 6 1 5 6 2 4 3 | Yes | 21.17 |
| 18 | 2 5 5 6 2 3 2 1 3 2 4 5 1 6 | 2 5 5 6 1 4 2 3 2 1 2 3 2 4 5 1 | No | 40.35 |
| 19 | 2 5 1 5 5 5 6 3 2 4 5 3 2 5 | 2 5 1 5 5 5 6 3 2 4 5 3 2 5 | Yes | 21.6 |
| 20 | 4 5 4 2 3 3 1 4 5 2 5 4 5 6 |  | No | 35.24 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1633 | 1633 | Yes | 2.69 |
| 2 | 1614 | 1614 | Yes | 2.76 |
| 3 | 2178 | 2178 | Yes | 3.09 |
| 4 | 1882 | 1882 | Yes | 3.87 |
| 5 | 1911 | 1911 | Yes | 3.22 |
| 6 | 1071 | 1071 | Yes | 2.75 |
| 7 | 1410 | 1410 | Yes | 3.11 |
| 8 | 2217 | 2217 | Yes | 2.75 |
| 9 | 1325 | 1325 | Yes | 3.26 |
| 10 | 1670 | 1670 | Yes | 2.98 |
| 11 | 1044 | 1044 | Yes | 2.61 |
| 12 | 1876 | 1876 | Yes | 3.18 |
| 13 | 1598 | 1598 | Yes | 5.72 |
| 14 | 1379 | 1379 | Yes | 2.84 |
| 15 | 1872 | 1872 | Yes | 4.1 |
| 16 | 2060 | 2060 | Yes | 2.78 |
| 17 | 1939 | 1939 | Yes | 3.74 |
| 18 | 2253 | 2253 | Yes | 3.27 |
| 19 | 1795 | 1795 | Yes | 3.66 |
| 20 | 1664 | 1664 | Yes | 3.32 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 74 | 71 | No | 15.27 |
| 2 | 75 | 77 | No | 14.61 |
| 3 | 69 | 66 | No | 14.5 |
| 4 | 41 | 41 | Yes | 12.59 |
| 5 | 68 | 65 | No | 13.13 |
| 6 | 39 | 39 | Yes | 12.94 |
| 7 | 71 | 67 | No | 14.29 |
| 8 | 51 | 48 | No | 12.11 |
| 9 | 71 | 67 | No | 12.9 |
| 10 | 54 | 52 | No | 13.14 |
| 11 | 49 | 49 | Yes | 12.98 |
| 12 | 58 | 57 | No | 14.23 |
| 13 | 37 | 37 | Yes | 12.2 |
| 14 | 43 | 43 | Yes | 12.45 |
| 15 | 57 | 55 | No | 14.1 |
| 16 | 75 | 73 | No | 13.28 |
| 17 | 39 | 40 | No | 13.2 |
| 18 | 70 | 69 | No | 14.4 |
| 19 | 36 | 36 | Yes | 25.67 |
| 20 | 63 | 61 | No | 12.91 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VPYCHZU | VPYCHZU | Yes | 5.65 |
| 2 | AEDKSMR | AEDKSMR | Yes | 3.93 |
| 3 | LKRMPQA | LKRMPQA | Yes | 3.48 |
| 4 | CINJDRL | CINJDRL | Yes | 3.51 |
| 5 | MYBSFGR | MYBSFGR | Yes | 5.73 |
| 6 | YBQORPT | YBQORPT | Yes | 6.63 |
| 7 | EMAOTQS | EMAOTQS | Yes | 6.28 |
| 8 | XJMVLTC | XJMVLTC | Yes | 3.98 |
| 9 | TIHPACK | TIHPACK | Yes | 5.42 |
| 10 | JWIXEVH | JWIXEVH | Yes | 5.71 |
| 11 | RVQESYF | RVQESYF | Yes | 8.69 |
| 12 | GVLKPTQ | GVLKPTQ | Yes | 8.31 |
| 13 | LGHKMSA | LGHKMSA | Yes | 4.63 |
| 14 | MUGAPXK | MUGAPXK | Yes | 14.94 |
| 15 | QIZERJY | QIZERJY | Yes | 6.13 |
| 16 | DXKAGZJ | DXKAGZJ | Yes | 7.12 |
| 17 | QGWVFHN | QGWVFHN | Yes | 6.03 |
| 18 | LWIEFSG | LWIEFSG | Yes | 3.35 |
| 19 | LHYDNMZ | LHYDNMZ | Yes | 5.95 |
| 20 | PBZOCSQ | PBZOCSQ | Yes | 9.74 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 0.6 9.4 | Yes | 10.2 |
| 2 | [3.7, 6.3] | 6.3 3.7 | Yes | 5.6 |
| 3 | [1.4, 8.6] | 1.4 8.6 | Yes | 7.14 |
| 4 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.2 |
| 5 | [0.4, 9.6] | 9.6 0.4 | Yes | 5.1 |
| 6 | [1.0, 9.0] | 9.0 1.0 | Yes | 4.46 |
| 7 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.68 |
| 8 | [1.9, 8.1] | 1.9 8.1 | Yes | 7.06 |
| 9 | [4.9, 5.1] | 5.1 4.9 | Yes | 6.55 |
| 10 | [2.4, 7.6] | 7.6 2.4 | Yes | 8.96 |
| 11 | [2.0, 8.0] | 8.0 2.0 | Yes | 4.98 |
| 12 | [0.5, 9.5] | 9.5 0.5 | Yes | 6.68 |
| 13 | [0.9, 9.1] | 9.1 0.9 | Yes | 11.41 |
| 14 | [1.4, 8.6] | 8.6 1.4 | Yes | 7.78 |
| 15 | [4.7, 5.3] | 4.7 5.3 | Yes | 9.42 |
| 16 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.89 |
| 17 | [0.9, 9.1] | 9.1 0.9 | Yes | 5.98 |
| 18 | [2.5, 7.5] | 2.5 7.5 | Yes | 7.54 |
| 19 | [2.4, 7.6] | 2.4 7.6 | Yes | 10.92 |
| 20 | [2.1, 7.9] | 2.1 7.9 | Yes | 9.16 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | QP56F9FNQVZL | QP56F9FNQVZL | Yes | 3.3 |
| 2 | X9QPAAOH24Z5 | X9QPAAOH24Z5 | Yes | 3.44 |
| 3 | DA8WNSQARH13 | DA8WNSQARH13 | Yes | 3.31 |
| 4 | WIRMOR2LCMEE | WIRMOR2LCMEE | Yes | 3.72 |
| 5 | L2Z6RWI4PX2M | L2Z6RWI4PX2M | Yes | 3.67 |
| 6 | 7X7PFRLN5NS3 | 7X7PFRLN5NS3 | Yes | 3.39 |
| 7 | T3AGDJI19V6G | T3AGDJI19V6G | Yes | 3.77 |
| 8 | PRKUH3334NYV | PRKUH3334NYV | Yes | 5.46 |
| 9 | 7W574HFN1292 | 7W574HFN1292 | Yes | 4.19 |
| 10 | S3DQV1F6VVND | S3DQV1F6VVND | Yes | 4.41 |
| 11 | 9NWL1OMO355D | 9NWL1OMO355D | Yes | 3.6 |
| 12 | 92P8W2AEJEDR | 92P8W2AEJEDR | Yes | 3.18 |
| 13 | XZCBQCXX1QHB | XZCBQCXX1QHB | Yes | 3.02 |
| 14 | 7K8QSGUOEBU7 | 7K8QSGUOEBU7 | Yes | 4.44 |
| 15 | X65E0J39400D | X65E0J39400D | Yes | 3.18 |
| 16 | 8H90HK0Y6HCO | 8H90HK0Y6HC0 | No | 4.14 |
| 17 | 28K9R40J85HX | 28K9R40J85HX | Yes | 2.86 |
| 18 | OFHJFZAIZD4M | OFHJFZAIZD4M | Yes | 3.58 |
| 19 | T71V04Y7VLMI | T71V04Y7VLMI | Yes | 6.24 |
| 20 | RRIHNGJA7M9E | RRIHNGJA7M9E | Yes | 3.97 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 9 | 9 | Yes | 4.76 |
| 2 | 65 | 65 | Yes | 5.48 |
| 3 | 63 | 63 | Yes | 4.18 |
| 4 | 7 | 7 | Yes | 2.77 |
| 5 | 10 | 10 | Yes | 3.62 |
| 6 | 67 | 67 | Yes | 2.46 |
| 7 | 20 | 20 | Yes | 15.15 |
| 8 | 36 | 36 | Yes | 4.12 |
| 9 | 31 | 31 | Yes | 4.0 |
| 10 | 3 | 3 | Yes | 5.16 |
| 11 | 48 | 48 | Yes | 4.26 |
| 12 | 73 | 73 | Yes | 4.82 |
| 13 | 16 | 16 | Yes | 4.64 |
| 14 | 60 | 60 | Yes | 3.9 |
| 15 | 198 | 198 | Yes | 3.75 |
| 16 | 28 | 28 | Yes | 4.27 |
| 17 | 4096 | 4096 | Yes | 16.76 |
| 18 | 60 | 60 | Yes | 3.03 |
| 19 | 793 | 793 | Yes | 2.83 |
| 20 | 44 | 44 | Yes | 4.31 |
