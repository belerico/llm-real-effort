# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-27 10:25:38

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
| sudoku_game | 4955 | 40960 | 45915 | 0 | 20 | 38.46 | 769.28 |
| add_numbers | 2720 | 3388 | 6108 | 20 | 0 | 2.75 | 55.04 |
| counting_zeros | 4120 | 39884 | 44004 | 4 | 16 | 27.88 | 557.63 |
| task_decoding | 4060 | 10236 | 14296 | 20 | 0 | 8.61 | 172.3 |
| task_summation | 4180 | 16287 | 20467 | 19 | 1 | 16.04 | 320.87 |
| task_transcription | 2860 | 2864 | 5724 | 20 | 0 | 2.50 | 50.03 |
| task_sequences | 2721 | 10830 | 13551 | 19 | 1 | 8.50 | 170.06 |
| string_entry | 3155 | 33755 | 36910 | 2 | 18 | 25.31 | 506.17 |
| **TOTAL** | **28771** | **158204** | **186975** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6 1 6 5 3 6 4 3 5 3 5 4 4 2 |  | No | 38.49 |
| 2 | 4 3 3 4 6 3 4 3 6 2 1 2 5 1 |  | No | 36.31 |
| 3 | 4 6 2 4 6 2 6 5 5 4 6 1 6 5 |  | No | 31.14 |
| 4 | 1 3 2 2 5 4 4 3 1 3 5 1 4 3 |  | No | 40.84 |
| 5 | 1 6 5 6 5 3 2 1 5 2 4 1 4 5 |  | No | 33.58 |
| 6 | 5 3 6 1 2 6 3 5 5 6 3 3 2 4 |  | No | 47.36 |
| 7 | 2 1 5 4 6 4 3 5 3 5 3 4 4 2 |  | No | 39.97 |
| 8 | 1 3 5 6 2 5 4 6 2 4 3 5 3 6 |  | No | 40.62 |
| 9 | 6 3 2 1 5 2 1 5 3 6 5 1 2 3 |  | No | 38.04 |
| 10 | 3 6 1 6 1 3 2 3 5 2 4 3 6 1 |  | No | 50.94 |
| 11 | 3 5 6 4 6 3 2 1 5 3 4 2 4 6 |  | No | 41.36 |
| 12 | 2 3 1 5 4 4 6 5 1 6 4 5 4 2 |  | No | 33.95 |
| 13 | 2 4 1 5 6 5 2 3 4 4 2 3 6 4 |  | No | 37.49 |
| 14 | 4 5 2 6 6 4 3 4 1 2 2 5 1 4 |  | No | 22.62 |
| 15 | 1 6 1 2 2 5 3 5 2 5 6 5 3 2 |  | No | 35.68 |
| 16 | 2 6 4 4 2 5 1 4 5 1 3 6 2 5 |  | No | 35.22 |
| 17 | 6 1 2 1 5 4 3 2 3 1 4 3 1 4 |  | No | 37.28 |
| 18 | 3 6 4 2 5 2 3 6 4 2 2 6 3 6 |  | No | 32.69 |
| 19 | 6 1 5 3 2 6 4 3 1 2 6 3 6 3 |  | No | 45.91 |
| 20 | 5 2 2 5 2 6 3 4 6 5 5 3 1 6 |  | No | 49.74 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1906 | 1906 | Yes | 2.23 |
| 2 | 1479 | 1479 | Yes | 1.95 |
| 3 | 1214 | 1214 | Yes | 1.89 |
| 4 | 1152 | 1152 | Yes | 3.17 |
| 5 | 1904 | 1904 | Yes | 4.31 |
| 6 | 1515 | 1515 | Yes | 2.78 |
| 7 | 1833 | 1833 | Yes | 3.09 |
| 8 | 2472 | 2472 | Yes | 2.66 |
| 9 | 970 | 970 | Yes | 2.59 |
| 10 | 985 | 985 | Yes | 2.24 |
| 11 | 1121 | 1121 | Yes | 3.03 |
| 12 | 997 | 997 | Yes | 2.8 |
| 13 | 1816 | 1816 | Yes | 3.03 |
| 14 | 1755 | 1755 | Yes | 2.84 |
| 15 | 1858 | 1858 | Yes | 2.91 |
| 16 | 1713 | 1713 | Yes | 3.59 |
| 17 | 2182 | 2182 | Yes | 3.06 |
| 18 | 1696 | 1696 | Yes | 2.01 |
| 19 | 1795 | 1795 | Yes | 2.43 |
| 20 | 1461 | 1461 | Yes | 2.42 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 41 |  | No | 37.64 |
| 2 | 52 |  | No | 19.29 |
| 3 | 38 |  | No | 32.06 |
| 4 | 36 | 36 | Yes | 19.68 |
| 5 | 61 |  | No | 32.16 |
| 6 | 40 | 40 | Yes | 14.71 |
| 7 | 43 |  | No | 22.0 |
| 8 | 46 | 46 | Yes | 13.98 |
| 9 | 56 |  | No | 22.93 |
| 10 | 59 |  | No | 21.45 |
| 11 | 70 |  | No | 22.38 |
| 12 | 74 |  | No | 37.46 |
| 13 | 63 |  | No | 49.51 |
| 14 | 69 |  | No | 40.17 |
| 15 | 72 |  | No | 39.35 |
| 16 | 66 | 66 | Yes | 16.58 |
| 17 | 60 |  | No | 22.01 |
| 18 | 52 |  | No | 19.68 |
| 19 | 41 |  | No | 31.66 |
| 20 | 74 |  | No | 42.9 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | DLBZVYU | DLBZVYU | Yes | 9.68 |
| 2 | VOYIZWB | VOYIZWB | Yes | 3.88 |
| 3 | ZODACMY | ZODACMY | Yes | 9.41 |
| 4 | BXOIPAD | BXOIPAD | Yes | 16.31 |
| 5 | LPGNQFT | LPGNQFT | Yes | 4.56 |
| 6 | FAVDLXE | FAVDLXE | Yes | 14.05 |
| 7 | MZTHUXF | MZTHUXF | Yes | 4.54 |
| 8 | VDTSWFH | VDTSWFH | Yes | 11.01 |
| 9 | OHAZWRP | OHAZWRP | Yes | 5.25 |
| 10 | PGUHMCR | PGUHMCR | Yes | 2.68 |
| 11 | NYBQPGR | NYBQPGR | Yes | 9.06 |
| 12 | GJOCEHV | GJOCEHV | Yes | 9.02 |
| 13 | TWLOMKR | TWLOMKR | Yes | 14.57 |
| 14 | MQVSDTF | MQVSDTF | Yes | 6.2 |
| 15 | RMGZTHI | RMGZTHI | Yes | 10.18 |
| 16 | AJRDIUB | AJRDIUB | Yes | 4.1 |
| 17 | RALWNZX | RALWNZX | Yes | 5.7 |
| 18 | AJVWMQL | AJVWMQL | Yes | 5.74 |
| 19 | MZGKLRE | MZGKLRE | Yes | 7.35 |
| 20 | APRUHXL | APRUHXL | Yes | 18.99 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.22 |
| 2 | [4.8, 5.2] | 4.8 5.2 | Yes | 8.89 |
| 3 | [0.9, 9.1] | 0.9 9.1 | Yes | 9.52 |
| 4 | [3.6, 6.4] | 3.6 6.4 | Yes | 11.33 |
| 5 | [3.0, 7.0] | 7.0 3.0 | Yes | 11.43 |
| 6 | [0.2, 9.8] | 0.2 9.8 | Yes | 10.04 |
| 7 | [3.0, 7.0] | 7.0 3.0 | Yes | 7.99 |
| 8 | [4.7, 5.3] | 4.7 5.3 | Yes | 13.16 |
| 9 | [1.5, 8.5] | 1.5 8.5 | Yes | 10.54 |
| 10 | [4.9, 5.1] | 5.1 4.9 | Yes | 12.76 |
| 11 | [2.5, 7.5] | 2.5 7.5 | Yes | 6.36 |
| 12 | [4.5, 5.5] | 4.5 5.5 | Yes | 10.31 |
| 13 | [1.7, 8.3] | 1.7 8.3 | Yes | 13.59 |
| 14 | [2.5, 7.5] | 7.5 2.5 | Yes | 10.95 |
| 15 | [4.2, 5.8] | 4.2 5.8 | Yes | 12.47 |
| 16 | [3.3, 6.7] | 3.3 6.7 | Yes | 9.66 |
| 17 | [0.5, 9.5] | 9.5 0.5 | Yes | 14.39 |
| 18 | [3.8, 6.2] | TIMEOUT | No | 120.02 |
| 19 | [4.5, 5.5] | 4.5 5.5 | Yes | 9.43 |
| 20 | [3.2, 6.8] | 6.8 3.2 | Yes | 10.79 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | P0BD5GISZPW9 | P0BD5GISZPW9 | Yes | 2.44 |
| 2 | D2AVWEOVCLFK | D2AVWEOVCLFK | Yes | 7.44 |
| 3 | APXM9X71VWZ9 | APXM9X71VWZ9 | Yes | 2.03 |
| 4 | Z4N9S4KATHCL | Z4N9S4KATHCL | Yes | 2.38 |
| 5 | KTFF6HLD1BAV | KTFF6HLD1BAV | Yes | 2.3 |
| 6 | 1CF1OFE9DFGG | 1CF1OFE9DFGG | Yes | 2.64 |
| 7 | QSORYKYPE3CN | QSORYKYPE3CN | Yes | 1.74 |
| 8 | 9R3IXUT48C2O | 9R3IXUT48C2O | Yes | 1.76 |
| 9 | XI4NY96OF8BP | XI4NY96OF8BP | Yes | 2.08 |
| 10 | P9QLHZFZGI6E | P9QLHZFZGI6E | Yes | 2.3 |
| 11 | LEYI7C3P76X6 | LEYI7C3P76X6 | Yes | 1.76 |
| 12 | 147KTV0XTYTV | 147KTV0XTYTV | Yes | 1.83 |
| 13 | NG6D6IEBEF4E | NG6D6IEBEF4E | Yes | 2.65 |
| 14 | Y3GXDKOPRIJ9 | Y3GXDKOPRIJ9 | Yes | 2.12 |
| 15 | FD9VL8HZBUYQ | FD9VL8HZBUYQ | Yes | 3.11 |
| 16 | TXDF0BXASVP4 | TXDF0BXASVP4 | Yes | 2.05 |
| 17 | 8JUH2D329NSJ | 8JUH2D329NSJ | Yes | 2.35 |
| 18 | 7WLN14G22R3K | 7WLN14G22R3K | Yes | 3.09 |
| 19 | YEV86CVFH2I6 | YEV86CVFH2I6 | Yes | 2.02 |
| 20 | Z5C4VGPDAN5M | Z5C4VGPDAN5M | Yes | 1.94 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 31 | 31 | Yes | 3.66 |
| 2 | 65 | 65 | Yes | 8.68 |
| 3 | 9 | 9 | Yes | 8.73 |
| 4 | 19 | 19 | Yes | 8.6 |
| 5 | 198 | 198 | Yes | 11.63 |
| 6 | 7680 | 7680 | Yes | 9.11 |
| 7 | 44 | 44 | Yes | 7.69 |
| 8 | 36 | 36 | Yes | 3.27 |
| 9 | 7 | 7 | Yes | 2.63 |
| 10 | 73 | 73 | Yes | 9.91 |
| 11 | 26 | 26 | Yes | 6.22 |
| 12 | 5 | 5 | Yes | 4.78 |
| 13 | 23 | 23 | Yes | 9.88 |
| 14 | 4096 |  | No | 33.33 |
| 15 | 243 | 243 | Yes | 2.5 |
| 16 | 48 | 48 | Yes | 7.82 |
| 17 | 3 | 3 | Yes | 4.98 |
| 18 | 28 | 28 | Yes | 7.05 |
| 19 | 20 | 20 | Yes | 14.18 |
| 20 | 16 | 16 | Yes | 5.41 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /)<)(  )/ | /)<)(  )/ | Yes | 10.44 |
| 2 | \ (((//)< |  | No | 39.87 |
| 3 |  ))_<  </ | ))_<  </ | No | 17.97 |
| 4 | \\/(  \)< |  | No | 36.03 |
| 5 | )((( __\< | /\) <(_<) | No | 13.58 |
| 6 | \/\<<(((_ |  | No | 32.15 |
| 7 | ( /\_)<_< |  | No | 32.69 |
| 8 | __)(\<((  |  | No | 32.7 |
| 9 | <_/)_))(( | <_/)_))(( | Yes | 11.77 |
| 10 | _\ )(/ (  |  | No | 35.4 |
| 11 | \\_</<<</ | /\) <(_<) | No | 14.27 |
| 12 | )_(/<<\</ | /\) <(_<) | No | 11.59 |
| 13 | ()\)(<  < |  | No | 24.03 |
| 14 | _/_<(/</< | /\) <(_<) | No | 12.95 |
| 15 | ))/<()))( | ))/<())))( | No | 15.93 |
| 16 | <(\ ))  _ |  | No | 20.19 |
| 17 | (\))\<\_( |  | No | 46.1 |
| 18 |  (/( \)(\ | (/( \)(\ | No | 18.56 |
| 19 |  <<\<(_<< |  | No | 45.05 |
| 20 | _ /  _/(\ |  | No | 34.9 |
