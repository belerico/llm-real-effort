# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-27 10:28:35

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
| sudoku_game | 5481 | 40960 | 46441 | 0 | 20 | 37.43 | 748.69 |
| add_numbers | 3240 | 3639 | 6879 | 20 | 0 | 3.55 | 70.93 |
| counting_zeros | 4645 | 38332 | 42977 | 2 | 18 | 27.59 | 551.79 |
| task_decoding | 4351 | 8719 | 13070 | 19 | 1 | 13.23 | 264.55 |
| task_summation | 4920 | 16772 | 21692 | 19 | 1 | 11.95 | 239.04 |
| task_transcription | 3389 | 3240 | 6629 | 20 | 0 | 2.56 | 51.14 |
| task_sequences | 3241 | 15218 | 18459 | 16 | 4 | 11.26 | 225.23 |
| string_entry | 3685 | 38251 | 41936 | 1 | 19 | 29.40 | 588.03 |
| **TOTAL** | **32952** | **165131** | **198083** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 1 2 1 3 5 4 1 2 6 2 5 1 |  | No | 42.11 |
| 2 | 5 3 4 2 3 4 2 5 2 6 1 5 3 2 |  | No | 28.07 |
| 3 | 1 2 5 6 5 6 1 4 2 3 5 2 3 1 |  | No | 36.63 |
| 4 | 2 4 3 4 1 1 6 4 5 4 6 6 1 4 |  | No | 40.8 |
| 5 | 3 4 2 1 5 2 1 1 5 1 4 3 3 2 |  | No | 43.47 |
| 6 | 5 1 3 5 2 6 1 5 5 1 6 1 6 5 |  | No | 47.83 |
| 7 | 6 1 5 2 4 3 5 4 1 4 2 1 2 6 |  | No | 32.11 |
| 8 | 3 1 4 6 3 5 2 6 5 1 4 2 3 5 |  | No | 28.97 |
| 9 | 5 5 4 2 3 1 5 2 4 6 5 1 5 2 |  | No | 50.45 |
| 10 | 6 1 3 2 4 3 2 1 4 1 1 6 3 4 |  | No | 27.87 |
| 11 | 2 6 2 1 6 1 3 6 1 3 3 2 5 6 |  | No | 44.83 |
| 12 | 5 3 6 1 3 6 1 2 4 6 3 2 5 3 |  | No | 32.81 |
| 13 | 3 5 4 4 5 2 5 5 3 1 6 2 6 1 |  | No | 36.09 |
| 14 | 6 3 1 5 5 6 1 5 2 3 5 6 1 3 |  | No | 39.98 |
| 15 | 3 2 1 4 4 3 2 5 2 6 4 2 5 6 |  | No | 38.28 |
| 16 | 6 2 5 5 6 3 1 5 6 1 5 6 2 4 |  | No | 39.85 |
| 17 | 3 5 1 5 3 2 6 4 6 3 1 4 3 2 |  | No | 42.4 |
| 18 | 1 4 2 3 1 2 6 5 4 1 5 2 4 6 |  | No | 38.75 |
| 19 | 6 6 2 3 3 5 5 6 2 4 3 2 5 6 |  | No | 25.68 |
| 20 | 3 6 5 4 5 3 6 3 6 2 5 4 6 5 |  | No | 31.69 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1876 | 1876 | Yes | 5.3 |
| 2 | 1662 | 1662 | Yes | 3.13 |
| 3 | 1846 | 1846 | Yes | 6.37 |
| 4 | 1143 | 1143 | Yes | 6.03 |
| 5 | 1367 | 1367 | Yes | 3.0 |
| 6 | 1838 | 1838 | Yes | 2.35 |
| 7 | 1993 | 1993 | Yes | 2.5 |
| 8 | 1031 | 1031 | Yes | 5.22 |
| 9 | 1822 | 1822 | Yes | 2.38 |
| 10 | 1355 | 1355 | Yes | 2.77 |
| 11 | 2409 | 2409 | Yes | 3.2 |
| 12 | 1124 | 1124 | Yes | 2.48 |
| 13 | 949 | 949 | Yes | 2.95 |
| 14 | 2007 | 2007 | Yes | 2.82 |
| 15 | 635 | 635 | Yes | 4.28 |
| 16 | 1798 | 1798 | Yes | 2.52 |
| 17 | 1807 | 1807 | Yes | 4.36 |
| 18 | 2098 | 2098 | Yes | 3.1 |
| 19 | 1574 | 1574 | Yes | 3.61 |
| 20 | 1787 | 1787 | Yes | 2.56 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 43 |  | No | 24.21 |
| 2 | 62 |  | No | 24.45 |
| 3 | 64 |  | No | 35.24 |
| 4 | 61 | 61 | Yes | 21.44 |
| 5 | 43 | 43 | Yes | 15.49 |
| 6 | 58 |  | No | 39.5 |
| 7 | 62 |  | No | 23.16 |
| 8 | 41 |  | No | 33.31 |
| 9 | 36 |  | No | 35.58 |
| 10 | 38 |  | No | 26.54 |
| 11 | 57 |  | No | 28.2 |
| 12 | 59 |  | No | 19.16 |
| 13 | 65 |  | No | 23.1 |
| 14 | 49 |  | No | 26.55 |
| 15 | 65 |  | No | 28.18 |
| 16 | 56 |  | No | 24.7 |
| 17 | 39 |  | No | 31.5 |
| 18 | 75 |  | No | 32.1 |
| 19 | 35 |  | No | 24.26 |
| 20 | 56 |  | No | 35.12 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PFXIQBT | PFXIQBT | Yes | 6.82 |
| 2 | PYDRCWE | PYDRCWE | Yes | 8.22 |
| 3 | BNGKOVH | TIMEOUT | No | 120.03 |
| 4 | XRDGWMN | XRDGWMN | Yes | 13.83 |
| 5 | JTBLSWE | JTBLSWE | Yes | 8.11 |
| 6 | DKXJYIS | DKXJYIS | Yes | 4.69 |
| 7 | MLYJUPX | MLYJUPX | Yes | 7.1 |
| 8 | YLNJEFD | YLNJEFD | Yes | 8.89 |
| 9 | UGJMVFZ | UGJMVFZ | Yes | 5.27 |
| 10 | WMPQOCS | WMPQOCS | Yes | 4.62 |
| 11 | WFVTGBR | WFVTGBR | Yes | 8.2 |
| 12 | VXHILRU | VXHILRU | Yes | 5.46 |
| 13 | FIREDOM | FIREDOM | Yes | 9.01 |
| 14 | RAQOWXP | RAQOWXP | Yes | 4.09 |
| 15 | JSGBQDC | JSGBQDC | Yes | 12.56 |
| 16 | FLWZYDB | FLWZYDB | Yes | 6.81 |
| 17 | JVUYKWH | JVUYKWH | Yes | 6.58 |
| 18 | ARIGMQJ | ARIGMQJ | Yes | 8.16 |
| 19 | ENDRWZU | ENDRWZU | Yes | 9.68 |
| 20 | VCKHASN | VCKHASN | Yes | 6.41 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [4.0, 6.0] | 6.0 4.0 | Yes | 7.89 |
| 2 | [2.4, 7.6] | 2.4 7.6 | Yes | 10.31 |
| 3 | [4.2, 5.8] | 4.2 5.8 | Yes | 9.72 |
| 4 | [1.3, 8.7] | 8.7 1.3 | Yes | 11.92 |
| 5 | [2.1, 7.9] | 7.9 2.1 | Yes | 9.67 |
| 6 | [0.6, 9.4] | 9.4 0.6 | Yes | 13.12 |
| 7 | [3.6, 6.4] | 3.6 6.4 | Yes | 16.07 |
| 8 | [4.9, 5.1] | 4.9 5.1 | Yes | 8.67 |
| 9 | [2.8, 7.2] | 2.8 7.2 | Yes | 10.88 |
| 10 | [4.9, 5.1] | 5.1 4.9 | Yes | 9.54 |
| 11 | [3.4, 6.6] | 6.6 3.4 | Yes | 13.26 |
| 12 | [0.7, 9.3] | 0.7 9.3 | Yes | 11.43 |
| 13 | [0.4, 9.6] | 9.6 0.4 | Yes | 8.75 |
| 14 | [4.1, 5.9] | 4.1 5.9 | Yes | 14.21 |
| 15 | [4.8, 5.2] | 4.8 5.2 | Yes | 11.77 |
| 16 | [3.2, 6.8] | 3.2 6.8 | Yes | 9.96 |
| 17 | [0.7, 9.3] | 0.7 9.3 | Yes | 9.29 |
| 18 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.69 |
| 19 | [2.7, 7.3] |  | No | 31.9 |
| 20 | [3.5, 6.5] | 3.5 6.5 | Yes | 9.01 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2P8NJ8QZEU2V | 2P8NJ8QZEU2V | Yes | 2.27 |
| 2 | XAND4XXQQB5T | XAND4XXQQB5T | Yes | 1.96 |
| 3 | JZH1TXDNG35A | JZH1TXDNG35A | Yes | 2.9 |
| 4 | PPZTCFMB8O7Z | PPZTCFMB8O7Z | Yes | 2.65 |
| 5 | 2MLKXPB1C2N6 | 2MLKXPB1C2N6 | Yes | 2.36 |
| 6 | HROICN5PF1Z6 | HROICN5PF1Z6 | Yes | 1.84 |
| 7 | ZBF0R9GXK7E6 | ZBF0R9GXK7E6 | Yes | 2.7 |
| 8 | FE9O6HO2EEER | FE9O6HO2EEER | Yes | 2.67 |
| 9 | G1RK5UXA1PRK | G1RK5UXA1PRK | Yes | 2.49 |
| 10 | JMERATYC9VLQ | JMERATYC9VLQ | Yes | 1.95 |
| 11 | 6DHF5PYWPHGU | 6DHF5PYWPHGU | Yes | 3.18 |
| 12 | M1XPCIFWJT47 | M1XPCIFWJT47 | Yes | 2.37 |
| 13 | OS6OHGYQ9UBF | OS6OHGYQ9UBF | Yes | 2.23 |
| 14 | TMCRU5LMJY58 | TMCRU5LMJY58 | Yes | 2.4 |
| 15 | 95DM83LVWOBF | 95DM83LVWOBF | Yes | 2.53 |
| 16 | YG2LB6DSJXNT | YG2LB6DSJXNT | Yes | 1.95 |
| 17 | 1P34N00I8SEO | 1P34N00I8SEO | Yes | 3.2 |
| 18 | L1F4QCS6RQJ8 | L1F4QCS6RQJ8 | Yes | 2.92 |
| 19 | 4WBTKSPQVQNG | 4WBTKSPQVQNG | Yes | 1.87 |
| 20 | MSU5E8NGBUSR | MSU5E8NGBUSR | Yes | 4.7 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 793 | 793 | Yes | 3.71 |
| 2 | 65 | 65 | Yes | 3.9 |
| 3 | 44 | 44 | Yes | 3.98 |
| 4 | 31 | 31 | Yes | 7.76 |
| 5 | 3 | 3 | Yes | 8.15 |
| 6 | 7 | 7 | Yes | 3.65 |
| 7 | 16 | 16 | Yes | 7.55 |
| 8 | 1 | 1 | Yes | 6.15 |
| 9 | 28 | 28 | Yes | 8.97 |
| 10 | 3 |  | No | 33.11 |
| 11 | 6 | 6 | Yes | 1.99 |
| 12 | 23 | 23 | Yes | 2.82 |
| 13 | 5 |  | No | 35.35 |
| 14 | 243 | 243 | Yes | 4.29 |
| 15 | 36 | 36 | Yes | 10.24 |
| 16 | 4096 |  | No | 35.53 |
| 17 | 19 | 19 | Yes | 4.1 |
| 18 | 39 | 39 | Yes | 3.28 |
| 19 | 4 | 4 | Yes | 5.69 |
| 20 | 20 |  | No | 34.99 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )<__/  << |  | No | 18.79 |
| 2 | <\\)_)/_( |  | No | 46.95 |
| 3 | (<)()\\\_ | /\) <(_<) | No | 13.52 |
| 4 | )< ) ___/ |  | No | 56.13 |
| 5 | \\  /_/ ( |  | No | 21.17 |
| 6 | <<)/ (/)\ | <<)/ (/)\ | Yes | 4.26 |
| 7 | <_ \<_//  | <_ \<_// | No | 17.18 |
| 8 | /) <_<\\  |  | No | 40.42 |
| 9 | \/ (\_  / |  | No | 45.01 |
| 10 |  )_)</< / | )_)</< / | No | 14.45 |
| 11 | \((<</\/\ |  | No | 52.62 |
| 12 | _/<\/(<\  |  | No | 56.92 |
| 13 |  < <((/<( |  | No | 22.75 |
| 14 | <_ \_ <(/ |  | No | 23.73 |
| 15 | \))</ ) ( |  | No | 21.01 |
| 16 | \ )<(<\)_ |  | No | 25.14 |
| 17 | <(/\\_\(\ |  | No | 44.42 |
| 18 | \/_<(())\ |  | No | 21.97 |
| 19 | _<<)/)/(_ |  | No | 23.07 |
| 20 | )/_\ ()/< |  | No | 18.52 |
