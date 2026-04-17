# Benchmark Report — gpt-5.4

- **Model**: `openai/gpt-5.4`
- **Date**: 2026-03-19 03:13:48

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

**Model-specific overrides:**
- temperature: `None`

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
| sudoku_game | 7360 | 28750 | 36110 | 13 | 7 | 23.02 | 460.68 |
| add_numbers | 3940 | 1008 | 4948 | 20 | 0 | 4.17 | 83.58 |
| counting_zeros | 6360 | 30407 | 36767 | 15 | 5 | 24.93 | 498.83 |
| task_decoding | 12100 | 3553 | 15653 | 20 | 0 | 5.87 | 117.53 |
| task_summation | 7300 | 6057 | 13357 | 20 | 0 | 7.76 | 155.44 |
| task_transcription | 3764 | 6892 | 10656 | 7 | 13 | 8.47 | 169.47 |
| task_sequences | 3061 | 6783 | 9844 | 18 | 2 | 10.40 | 208.05 |
| **TOTAL** | **43885** | **83450** | **127335** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 1 4 1 4 1 2 5 6 1 6 3 4 2 | 3 1 4 1 4 1 2 5 6 1 6 3 4 2 | Yes | 15.05 |
| 2 | 6 1 3 6 5 4 2 1 3 6 2 1 5 4 |  | No | 36.36 |
| 3 | 1 1 5 4 1 2 5 6 1 4 3 1 4 3 |  | No | 34.58 |
| 4 | 4 3 5 5 1 2 1 3 6 2 4 5 6 2 | 4 3 5 5 1 2 1 3 6 2 4 5 6 2 | Yes | 13.66 |
| 5 | 1 4 5 6 5 4 5 6 3 3 6 4 3 1 |  | No | 31.77 |
| 6 | 4 3 5 4 2 6 4 4 3 6 3 4 5 1 | 4 3 5 4 2 6 4 4 3 6 3 4 5 1 | Yes | 13.65 |
| 7 | 2 6 1 4 5 5 4 1 1 3 2 5 6 4 |  | No | 36.65 |
| 8 | 3 1 2 3 5 2 3 2 3 3 6 1 6 1 |  | No | 33.94 |
| 9 | 5 2 4 4 1 6 2 6 4 4 2 5 3 2 |  | No | 38.33 |
| 10 | 1 4 6 2 6 4 2 2 5 2 4 5 4 3 | 1 4 6 2 6 4 2 2 5 2 4 5 4 3 | Yes | 22.81 |
| 11 | 3 5 4 2 5 1 4 2 3 6 5 6 3 1 | 3 5 4 2 5 1 4 2 3 6 5 6 3 1 | Yes | 12.6 |
| 12 | 5 4 1 3 4 1 1 2 4 2 6 5 3 4 | 5 4 1 3 4 1 1 2 4 2 6 5 3 4 | Yes | 12.2 |
| 13 | 1 6 5 4 6 6 2 6 6 4 5 2 5 6 |  | No | 33.41 |
| 14 | 1 3 5 4 5 6 2 6 4 3 4 6 5 4 | 1 3 5 4 5 6 2 6 4 3 4 6 5 4 | Yes | 27.13 |
| 15 | 3 6 1 4 5 2 4 1 6 3 2 6 4 2 | 3 6 1 4 5 2 4 1 6 3 2 6 4 2 | Yes | 11.64 |
| 16 | 1 5 4 4 2 2 4 5 3 1 4 6 2 3 | 1 5 4 4 2 2 4 5 3 1 4 6 2 3 | Yes | 15.34 |
| 17 | 5 3 1 2 6 6 4 1 5 3 4 3 4 6 | 5 3 1 2 6 6 4 1 5 3 4 3 4 6 | Yes | 18.43 |
| 18 | 1 2 5 3 6 1 2 5 1 5 2 3 4 1 | 1 2 5 3 6 1 2 5 1 5 2 3 4 1 | Yes | 28.36 |
| 19 | 3 5 2 1 2 4 6 4 1 2 1 5 4 1 | 3 5 2 1 2 4 6 4 1 2 1 5 4 1 | Yes | 13.09 |
| 20 | 3 6 2 1 4 3 5 3 2 2 4 5 1 4 | 3 6 2 1 4 3 5 3 2 2 4 5 1 4 | Yes | 11.46 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1736 | 1736 | Yes | 4.66 |
| 2 | 1302 | 1302 | Yes | 3.26 |
| 3 | 1744 | 1744 | Yes | 3.3 |
| 4 | 1519 | 1519 | Yes | 5.54 |
| 5 | 1039 | 1039 | Yes | 3.43 |
| 6 | 1257 | 1257 | Yes | 4.17 |
| 7 | 1255 | 1255 | Yes | 3.51 |
| 8 | 1593 | 1593 | Yes | 3.15 |
| 9 | 2290 | 2290 | Yes | 3.47 |
| 10 | 1811 | 1811 | Yes | 3.94 |
| 11 | 1008 | 1008 | Yes | 3.74 |
| 12 | 1163 | 1163 | Yes | 3.88 |
| 13 | 2015 | 2015 | Yes | 8.09 |
| 14 | 2235 | 2235 | Yes | 3.91 |
| 15 | 1930 | 1930 | Yes | 4.34 |
| 16 | 1850 | 1850 | Yes | 4.04 |
| 17 | 2446 | 2446 | Yes | 4.28 |
| 18 | 1707 | 1707 | Yes | 3.67 |
| 19 | 1776 | 1776 | Yes | 5.23 |
| 20 | 2082 | 2082 | Yes | 3.87 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 49 | 49 | Yes | 25.6 |
| 2 | 75 | 75 | Yes | 28.83 |
| 3 | 36 | 36 | Yes | 23.97 |
| 4 | 40 | 40 | Yes | 23.85 |
| 5 | 55 | 55 | Yes | 19.63 |
| 6 | 71 | 71 | Yes | 24.09 |
| 7 | 61 |  | No | 26.44 |
| 8 | 72 | 72 | Yes | 25.64 |
| 9 | 45 | 45 | Yes | 22.02 |
| 10 | 45 | 45 | Yes | 29.39 |
| 11 | 41 | 41 | Yes | 23.13 |
| 12 | 73 | 73 | Yes | 19.75 |
| 13 | 41 |  | No | 34.68 |
| 14 | 41 | 40 | No | 18.42 |
| 15 | 48 | 48 | Yes | 21.72 |
| 16 | 42 | 42 | Yes | 16.36 |
| 17 | 59 |  | No | 58.23 |
| 18 | 45 | 44 | No | 15.82 |
| 19 | 44 | 44 | Yes | 20.83 |
| 20 | 67 | 67 | Yes | 20.13 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | JDXLNME | JDXLNME | Yes | 5.28 |
| 2 | CLDHPXV | CLDHPXV | Yes | 5.68 |
| 3 | JIUYNPD | JIUYNPD | Yes | 6.63 |
| 4 | KRXOQGI | KRXOQGI | Yes | 3.49 |
| 5 | HYJVUPC | HYJVUPC | Yes | 4.48 |
| 6 | TBSWKEF | TBSWKEF | Yes | 2.88 |
| 7 | WXYZVCU | WXYZVCU | Yes | 5.75 |
| 8 | BQCUTFP | BQCUTFP | Yes | 5.87 |
| 9 | ZEBJGHL | ZEBJGHL | Yes | 7.22 |
| 10 | LIPJWSK | LIPJWSK | Yes | 5.33 |
| 11 | NPFGUVZ | NPFGUVZ | Yes | 6.02 |
| 12 | XBKNYAI | XBKNYAI | Yes | 5.24 |
| 13 | IXTNGJP | IXTNGJP | Yes | 5.85 |
| 14 | OXLBGFT | OXLBGFT | Yes | 6.29 |
| 15 | KEBWQAU | KEBWQAU | Yes | 6.17 |
| 16 | WFZGQCE | WFZGQCE | Yes | 7.27 |
| 17 | IBXUOKY | IBXUOKY | Yes | 5.92 |
| 18 | ZBINVWP | ZBINVWP | Yes | 6.92 |
| 19 | EYNWUTC | EYNWUTC | Yes | 5.76 |
| 20 | VFHTRIP | VFHTRIP | Yes | 9.29 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [2.0, 8.0] | 8.0 2.0 | Yes | 6.72 |
| 2 | [1.7, 8.3] | 8.3 1.7 | Yes | 8.68 |
| 3 | [0.8, 9.2] | 0.8 9.2 | Yes | 7.08 |
| 4 | [4.1, 5.9] | 4.1 5.9 | Yes | 8.67 |
| 5 | [3.8, 6.2] | 6.2 3.8 | Yes | 7.19 |
| 6 | [3.4, 6.6] | 6.6 3.4 | Yes | 8.54 |
| 7 | [1.5, 8.5] | 1.5 8.5 | Yes | 7.75 |
| 8 | [0.4, 9.6] | 9.6 0.4 | Yes | 7.72 |
| 9 | [2.3, 7.7] | 2.3 7.7 | Yes | 9.39 |
| 10 | [2.8, 7.2] | 7.2 2.8 | Yes | 8.24 |
| 11 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.45 |
| 12 | [1.1, 8.9] | 8.9 1.1 | Yes | 6.22 |
| 13 | [0.2, 9.8] | 0.2 9.8 | Yes | 7.68 |
| 14 | [1.8, 8.2] | 8.2 1.8 | Yes | 6.85 |
| 15 | [0.3, 9.7] | 0.3 9.7 | Yes | 6.48 |
| 16 | [4.8, 5.2] | 4.8 5.2 | Yes | 9.08 |
| 17 | [2.4, 7.6] | 7.6 2.4 | Yes | 8.08 |
| 18 | [3.0, 7.0] | 3.0 7.0 | Yes | 8.9 |
| 19 | [1.2, 8.8] | 8.8 1.2 | Yes | 8.21 |
| 20 | [2.4, 7.6] | 2.4 7.6 | Yes | 7.31 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GZJ8OH2IK4VP | GZJ8OH2IK4VP | Yes | 10.91 |
| 2 | Q5BOZLPVC6IJ | Sorry, I can’t help transcribe distorted CAPTCHA text. | No | 8.32 |
| 3 | GZ2I7738NZL7 | GZ217738NZL7 | No | 11.09 |
| 4 | 0K0MRRJFLQAQ | I can’t help with solving CAPTCHAs. | No | 6.74 |
| 5 | 9QBUHTJD4C3F | 9QBUHTJD4C3F | Yes | 6.86 |
| 6 | TAMQQ7IU4PYQ | Sorry, I can’t help transcribe distorted text used for verification. | No | 10.85 |
| 7 | KC9QA4ESOI5I | Sorry, I can't help with solving CAPTCHAs. | No | 4.26 |
| 8 | PXNZ0CUY576K | PXNZ0CUY576K | Yes | 8.88 |
| 9 | GB79Y0FSDD79 | GB79YOFSDD79 | No | 16.84 |
| 10 | 10DPMWNYAHRX | 10DPMWNYAHRX | Yes | 3.42 |
| 11 | VFYMFN0EFQXP | Sorry, I can’t help solve CAPTCHAs or similar verification tests. | No | 5.89 |
| 12 | HH4LTVFSG3CG | HH4LTVFSG3CG | Yes | 5.32 |
| 13 | 211KXYIJUY2U | I can’t help with solving CAPTCHAs or transcribing distorted challenge text. | No | 5.44 |
| 14 | LCLKV8R0PA4S | LCLKV8R0PA4S | Yes | 11.73 |
| 15 | 96GM78PGGKNN | Sorry, I can’t help with solving CAPTCHAs. | No | 4.91 |
| 16 | FZTP6CP752RO | Sorry, I can’t help transcribe or solve distorted text used as a CAPTCHA. | No | 8.79 |
| 17 | FDHAJQ7O17HL | FDHAJQ7017HL | No | 22.06 |
| 18 | VM2U80P1VLDZ | Sorry, I can't help with solving CAPTCHAs. | No | 5.8 |
| 19 | JANA0U9O7WDS | Sorry, I can’t help solve CAPTCHA text. | No | 7.11 |
| 20 | PVZSU62JUQHC | PVZSU62JUQHC | Yes | 4.15 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 10 | 10 | Yes | 12.47 |
| 2 | 67 | 67 | Yes | 2.03 |
| 3 | 64 | 64 | Yes | 4.97 |
| 4 | 73 | 73 | Yes | 5.45 |
| 5 | 7 | 7 | Yes | 3.49 |
| 6 | 19 | 19 | Yes | 7.56 |
| 7 | 9 | 9 | Yes | 4.97 |
| 8 | 65 | 65 | Yes | 3.98 |
| 9 | 5 |  | No | 45.25 |
| 10 | 4096 |  | No | 43.64 |
| 11 | 16 | 16 | Yes | 5.33 |
| 12 | 23 | 23 | Yes | 10.12 |
| 13 | 3 | 3 | Yes | 11.8 |
| 14 | 20 | 20 | Yes | 17.25 |
| 15 | 5 | 5 | Yes | 5.43 |
| 16 | 4 | 4 | Yes | 4.78 |
| 17 | 28 | 28 | Yes | 5.37 |
| 18 | 9 | 9 | Yes | 5.23 |
| 19 | 7680 | 7680 | Yes | 4.88 |
| 20 | 1 | 1 | Yes | 4.04 |
