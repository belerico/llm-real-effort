# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-27 10:45:11

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
- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 4959 | 40960 | 45919 | 0 | 20 | 55.33 | 1106.65 |
| add_numbers | 2720 | 4292 | 7012 | 20 | 0 | 7.30 | 145.99 |
| counting_zeros | 3914 | 38764 | 42678 | 1 | 19 | 59.12 | 1182.47 |
| task_decoding | 4060 | 8316 | 12376 | 20 | 0 | 9.27 | 185.34 |
| task_summation | 4400 | 17367 | 21767 | 20 | 0 | 15.39 | 307.76 |
| task_transcription | 2861 | 4283 | 7144 | 20 | 0 | 5.07 | 101.35 |
| task_sequences | 2721 | 8014 | 10735 | 19 | 1 | 10.48 | 209.56 |
| string_entry | 3175 | 28028 | 31203 | 12 | 8 | 26.77 | 535.49 |
| **TOTAL** | **28810** | **150024** | **178834** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 6 4 4 2 4 1 3 5 4 6 5 5 1 |  | No | 54.52 |
| 2 | 5 1 6 4 1 2 3 5 1 2 2 3 4 1 |  | No | 45.7 |
| 3 | 3 5 1 6 2 3 2 6 3 6 5 1 5 4 |  | No | 53.93 |
| 4 | 4 1 5 2 3 4 2 3 5 1 1 4 2 4 |  | No | 58.8 |
| 5 | 5 6 6 4 1 1 3 5 4 3 2 3 1 3 |  | No | 67.31 |
| 6 | 6 3 5 6 2 4 5 5 2 3 2 1 6 6 |  | No | 48.33 |
| 7 | 4 3 1 5 2 3 2 5 3 4 1 6 3 2 |  | No | 56.23 |
| 8 | 2 6 6 3 6 2 3 3 2 6 2 4 5 5 |  | No | 50.99 |
| 9 | 5 4 3 1 3 4 6 5 4 3 5 4 2 6 |  | No | 55.89 |
| 10 | 3 4 2 5 2 1 3 6 4 6 2 1 6 1 |  | No | 50.13 |
| 11 | 6 5 6 4 4 5 6 1 3 6 4 5 5 3 |  | No | 54.97 |
| 12 | 3 5 2 6 2 3 4 1 5 3 4 4 3 1 |  | No | 71.02 |
| 13 | 2 3 4 1 5 2 1 4 1 5 2 5 4 1 |  | No | 59.0 |
| 14 | 1 3 3 5 2 2 4 6 3 1 5 6 3 2 |  | No | 68.87 |
| 15 | 4 2 5 5 4 6 4 6 1 2 5 5 1 6 |  | No | 49.35 |
| 16 | 1 6 2 5 6 2 1 6 5 2 1 6 1 5 |  | No | 46.03 |
| 17 | 5 4 3 1 5 2 6 3 2 4 6 2 4 5 |  | No | 60.92 |
| 18 | 3 5 1 6 1 6 5 2 6 4 3 5 4 1 |  | No | 52.53 |
| 19 | 6 2 4 1 3 5 2 6 4 3 5 2 4 6 |  | No | 50.43 |
| 20 | 2 4 3 3 2 5 6 1 2 5 1 4 2 2 |  | No | 51.67 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1417 | 1417 | Yes | 5.19 |
| 2 | 1566 | 1566 | Yes | 4.73 |
| 3 | 1987 | 1987 | Yes | 10.26 |
| 4 | 1425 | 1425 | Yes | 11.62 |
| 5 | 1370 | 1370 | Yes | 6.28 |
| 6 | 2193 | 2193 | Yes | 5.68 |
| 7 | 1733 | 1733 | Yes | 9.63 |
| 8 | 2607 | 2607 | Yes | 8.87 |
| 9 | 1622 | 1622 | Yes | 2.41 |
| 10 | 2427 | 2427 | Yes | 7.85 |
| 11 | 1782 | 1782 | Yes | 6.19 |
| 12 | 2403 | 2403 | Yes | 6.65 |
| 13 | 2034 | 2034 | Yes | 12.9 |
| 14 | 996 | 996 | Yes | 6.05 |
| 15 | 972 | 972 | Yes | 6.08 |
| 16 | 1746 | 1746 | Yes | 5.49 |
| 17 | 1732 | 1732 | Yes | 6.09 |
| 18 | 1418 | 1418 | Yes | 6.26 |
| 19 | 1854 | 1854 | Yes | 7.92 |
| 20 | 1879 | 1879 | Yes | 9.82 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 72 |  | No | 77.28 |
| 2 | 61 |  | No | 55.37 |
| 3 | 54 |  | No | 71.53 |
| 4 | 51 |  | No | 64.31 |
| 5 | 66 |  | No | 64.71 |
| 6 | 62 |  | No | 57.85 |
| 7 | 38 |  | No | 61.41 |
| 8 | 63 |  | No | 48.76 |
| 9 | 35 |  | No | 37.49 |
| 10 | 60 |  | No | 47.01 |
| 11 | 62 |  | No | 55.64 |
| 12 | 52 |  | No | 47.4 |
| 13 | 70 | 70 | Yes | 20.59 |
| 14 | 55 | TIMEOUT | No | 120.02 |
| 15 | 64 |  | No | 54.57 |
| 16 | 52 |  | No | 50.02 |
| 17 | 52 |  | No | 52.91 |
| 18 | 58 |  | No | 61.3 |
| 19 | 52 |  | No | 69.21 |
| 20 | 37 |  | No | 65.07 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | VRSBTPF | VRSBTPF | Yes | 11.09 |
| 2 | FCVINMR | FCVINMR | Yes | 9.27 |
| 3 | OGATCDB | OGATCDB | Yes | 11.84 |
| 4 | SUVDAYN | SUVDAYN | Yes | 12.23 |
| 5 | XFBPIJS | XFBPIJS | Yes | 10.07 |
| 6 | RJACIBF | RJACIBF | Yes | 7.55 |
| 7 | MTCKAGS | MTCKAGS | Yes | 7.43 |
| 8 | PQFBMED | PQFBMED | Yes | 10.28 |
| 9 | JVPLCUE | JVPLCUE | Yes | 4.52 |
| 10 | OCNZRQS | OCNZRQS | Yes | 9.44 |
| 11 | FJKZELU | FJKZELU | Yes | 5.97 |
| 12 | FUGIXJT | FUGIXJT | Yes | 9.63 |
| 13 | LWMVHTJ | LWMVHTJ | Yes | 4.2 |
| 14 | ISHDGQB | ISHDGQB | Yes | 8.71 |
| 15 | QZNSMDA | QZNSMDA | Yes | 8.68 |
| 16 | AJSQTZP | AJSQTZP | Yes | 5.97 |
| 17 | PSOKFZE | PSOKFZE | Yes | 16.18 |
| 18 | ZDTKAFW | ZDTKAFW | Yes | 10.3 |
| 19 | KBXHRJO | KBXHRJO | Yes | 11.31 |
| 20 | QSJHIRB | QSJHIRB | Yes | 10.66 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.7, 8.3] | 1.7 8.3 | Yes | 11.67 |
| 2 | [0.4, 9.6] | 0.4 9.6 | Yes | 17.21 |
| 3 | [1.8, 8.2] | 1.8 8.2 | Yes | 13.88 |
| 4 | [3.8, 6.2] | 6.2 3.8 | Yes | 13.46 |
| 5 | [1.7, 8.3] | 1.7 8.3 | Yes | 13.34 |
| 6 | [0.9, 9.1] | 0.9 9.1 | Yes | 14.12 |
| 7 | [0.2, 9.8] | 9.8 0.2 | Yes | 12.46 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 20.75 |
| 9 | [3.9, 6.1] | 3.9 6.1 | Yes | 17.27 |
| 10 | [0.4, 9.6] | 0.4 9.6 | Yes | 20.2 |
| 11 | [2.6, 7.4] | 2.6 7.4 | Yes | 8.91 |
| 12 | [1.8, 8.2] | 1.8 8.2 | Yes | 17.71 |
| 13 | [3.3, 6.7] | 3.3 6.7 | Yes | 20.33 |
| 14 | [4.7, 5.3] | 4.7 5.3 | Yes | 16.98 |
| 15 | [2.4, 7.6] | 7.6 2.4 | Yes | 13.21 |
| 16 | [1.0, 9.0] | 1.0 9.0 | Yes | 21.72 |
| 17 | [0.8, 9.2] | 0.8 9.2 | Yes | 15.41 |
| 18 | [3.9, 6.1] | 3.9 6.1 | Yes | 13.88 |
| 19 | [0.9, 9.1] | 9.1 0.9 | Yes | 12.55 |
| 20 | [0.1, 9.9] | 0.1 9.9 | Yes | 12.68 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XR4KI4UYEZL2 | XR4KI4UYEZL2 | Yes | 2.63 |
| 2 | 11HL16IBLGLX | 11HL16IBLGLX | Yes | 5.18 |
| 3 | ZE3SFVEZ4B6M | ZE3SFVEZ4B6M | Yes | 5.19 |
| 4 | THPRA2N0AX2S | THPRA2N0AX2S | Yes | 5.59 |
| 5 | 2545ICO9UTLP | 2545ICO9UTLP | Yes | 3.91 |
| 6 | MY3WFCWU0255 | MY3WFCWU0255 | Yes | 3.35 |
| 7 | NSZWT02VE8FM | NSZWT02VE8FM | Yes | 5.09 |
| 8 | Q79V652Y9TBW | Q79V652Y9TBW | Yes | 4.78 |
| 9 | W2MRV6BPUSUZ | W2MRV6BPUSUZ | Yes | 8.93 |
| 10 | Z6AFAYJ7G5FL | Z6AFAYJ7G5FL | Yes | 2.01 |
| 11 | 8IK1U3NAR6HS | 8IK1U3NAR6HS | Yes | 5.98 |
| 12 | RY5X0CSRUFM0 | RY5X0CSRUFM0 | Yes | 5.44 |
| 13 | T4VWM29VK6ZI | T4VWM29VK6ZI | Yes | 5.25 |
| 14 | 79JDJMCNT3SR | 79JDJMCNT3SR | Yes | 5.57 |
| 15 | J7S9LVJ0Y2WI | J7S9LVJ0Y2WI | Yes | 10.21 |
| 16 | AJFKTZW3TH6Y | AJFKTZW3TH6Y | Yes | 5.23 |
| 17 | LB4Z42ZH4ME6 | LB4Z42ZH4ME6 | Yes | 2.61 |
| 18 | SW1FLSBL7JXA | SW1FLSBL7JXA | Yes | 5.32 |
| 19 | Z6KHTNQ6OLS7 | Z6KHTNQ6OLS7 | Yes | 5.88 |
| 20 | CXRI3RJOAYGV | CXRI3RJOAYGV | Yes | 3.19 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 39 | 39 | Yes | 4.32 |
| 2 | 3 | 3 | Yes | 10.59 |
| 3 | 9 | 9 | Yes | 12.87 |
| 4 | 4 | 4 | Yes | 4.83 |
| 5 | 19 | 19 | Yes | 10.06 |
| 6 | 6 | 6 | Yes | 6.4 |
| 7 | 48 | 48 | Yes | 7.77 |
| 8 | 5 | 5 | Yes | 9.1 |
| 9 | 4 | 4 | Yes | 5.74 |
| 10 | 67 | 67 | Yes | 6.78 |
| 11 | 36 | 36 | Yes | 7.7 |
| 12 | 4096 |  | No | 57.72 |
| 13 | 9 | 9 | Yes | 10.65 |
| 14 | 7680 | 7680 | Yes | 13.88 |
| 15 | 63 | 63 | Yes | 5.13 |
| 16 | 44 | 44 | Yes | 6.21 |
| 17 | 7 | 7 | Yes | 9.95 |
| 18 | 60 | 60 | Yes | 6.11 |
| 19 | 1440 | 1440 | Yes | 6.11 |
| 20 | 23 | 23 | Yes | 7.65 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /)_\(<\/< | /)_\(<\/< | Yes | 24.9 |
| 2 | \//<  _)\ | \//<  _)\ | Yes | 20.85 |
| 3 | /)_ </ <( |  | No | 73.85 |
| 4 | < _\/\  ) | < _\/\  ) | Yes | 17.91 |
| 5 | _ (() \)( | _ (() \)( | Yes | 16.09 |
| 6 | __) )() ) | __) )() ) | Yes | 11.56 |
| 7 | \_/<(_  _ | \_/<(_  _ | Yes | 28.88 |
| 8 | \_</\_(_  | \_</\_(_ | No | 33.9 |
| 9 | <<(\ <//( | <<(\ <//( | Yes | 12.73 |
| 10 | \\() )<() | \\() )<() | Yes | 15.85 |
| 11 | \_/_\ //) | \_/\ //) | No | 33.9 |
| 12 |   \\ ((   |  | No | 62.0 |
| 13 | __)/)_ )_ | __)/)_ )_ | Yes | 16.35 |
| 14 | <_) _( \) | <_) _( \) | Yes | 18.61 |
| 15 | ))//(_    | ))//(_ | No | 19.02 |
| 16 | ((__\_\</ |  | No | 57.75 |
| 17 | _)/<<< \( | _)/<<< \( | Yes | 7.47 |
| 18 |  __<\ )_\ | __<\ )_\ | No | 19.46 |
| 19 | <(((\\<)_ | <(((\\<)_ | Yes | 18.07 |
| 20 | /_<<\))_  | /_<<\))_ | No | 26.34 |
