# Benchmark Report — gemini-2.5-pro

- **Model**: `google/gemini-2.5-pro`
- **Date**: 2026-03-19 03:13:48

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
| sudoku_game | 9074 | 35475 | 44549 | 0 | 20 | 21.57 | 431.6 |
| add_numbers | 39040 | 7530 | 46570 | 20 | 0 | 5.44 | 108.88 |
| counting_zeros | 24232 | 31428 | 55660 | 15 | 5 | 22.03 | 440.9 |
| task_decoding | 47778 | 7409 | 55187 | 18 | 2 | 6.78 | 135.8 |
| task_summation | 29040 | 19615 | 48655 | 20 | 0 | 11.27 | 225.71 |
| task_transcription | 24640 | 7991 | 32631 | 16 | 4 | 7.97 | 159.46 |
| task_sequences | 3160 | 18432 | 21592 | 19 | 1 | 12.02 | 240.44 |
| **TOTAL** | **176964** | **127880** | **304844** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2 5 6 4 6 1 2 5 3 1 4 4 3 1 |  | No | 37.02 |
| 2 | 1 3 5 4 6 1 6 2 3 6 3 4 3 6 | 1 3 4 5 1 6 6 2 3 6 2 3 6 4 3 6 | No | 14.69 |
| 3 | 5 6 2 5 3 5 5 1 6 2 6 3 6 1 | 5 6 5 2 2 5 3 5 6 1 2 6 3 6 3 6 1 | No | 15.84 |
| 4 | 6 6 2 5 5 4 5 1 4 3 2 3 2 6 | 6 6 2 5 5 4 3 5 2 3 2 6 3 2 6 5 3 2 6 | No | 14.99 |
| 5 | 3 1 5 4 2 1 6 2 1 1 6 5 4 2 | 3 1 5 1 2 6 1 2 6 2 1 6 2 4 5 4 6 2 5 4 | No | 25.87 |
| 6 | 2 3 1 5 1 5 2 6 2 3 5 1 5 6 | 2 3 1 5 2 5 1 5 2 6 2 5 3 6 5 6 5 1 | No | 15.69 |
| 7 | 2 1 6 5 3 1 2 5 1 3 2 1 5 3 |  | No | 35.47 |
| 8 | 3 2 6 1 3 2 2 3 3 4 3 2 1 2 | 3 2 6 1 3 2 3 2 3 1 4 3 2 1 2 | No | 15.55 |
| 9 | 3 6 1 5 1 5 2 1 2 4 5 1 2 2 | 1 3 6 5 1 5 2 1 2 1 5 2 1 5 2 4 2 5 1 4 | No | 15.32 |
| 10 | 3 1 5 4 2 5 5 3 6 3 1 3 1 6 |  | No | 38.56 |
| 11 | 1 6 2 3 4 5 4 6 2 1 6 6 1 5 | 6 1 2 4 3 5 4 1 6 1 2 5 6 1 5 3 | No | 15.94 |
| 12 | 2 4 3 1 2 6 2 5 6 2 5 3 1 6 | 2 1 3 4 2 6 2 5 6 1 3 6 5 2 6 1 2 1 6 5 | No | 15.6 |
| 13 | 4 2 3 2 4 6 2 2 6 5 6 5 3 6 | **Grid update 7** \| 4 \| 5 \| 3 \| 2 \| 6 \| 1 \| \|---\|---\|---\|---\|---\|---\| \| 2 \| 6 \| 1 \| | No | 32.87 |
| 14 | 2 5 1 6 4 5 3 1 2 4 5 6 4 2 | 2 5 1 6 4 5 3 1 2 4 4 2 6 5 | No | 16.08 |
| 15 | 3 1 3 6 2 3 6 4 2 5 4 3 6 3 | **Finalizing Solution**  I've completed the Sudoku puzzle by applying the rules of Sudoku to deduce the remaining missing numbers. The grid is now fully solved. I'm now extracting the missing numbers in reading order to format the final answer.    Final Check | No | 35.96 |
| 16 | 3 4 5 3 5 2 6 2 3 1 1 4 1 3 | 3 4 5 3 2 6 2 3 1 5 3 1 2 1 4 3 4 1 | No | 15.55 |
| 17 | 6 4 4 6 3 5 4 6 1 3 1 5 2 6 | 6 4 4 6 3 5 4 3 5 6 1 6 1 5 3 2 1 6 2 3 5 6 1 2 | No | 15.57 |
| 18 | 5 1 2 2 1 3 4 2 5 4 5 4 6 2 | 5 1 2 2 1 3 2 3 5 4 2 5 4 6 5 2 | No | 24.63 |
| 19 | 6 2 6 3 4 6 1 2 4 2 2 4 3 5 | 6 2 6 3 4 1 2 1 4 4 2 4 2 5 3 5 | No | 15.26 |
| 20 | 3 4 6 1 1 6 4 1 5 2 1 2 3 4 | 3 4 1 6 1 1 6 2 4 5 2 3 1 2 3 4 | No | 14.96 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2442 | 2442 | Yes | 5.47 |
| 2 | 1986 | 1986 | Yes | 5.68 |
| 3 | 1582 | 1582 | Yes | 5.25 |
| 4 | 2654 | 2654 | Yes | 5.41 |
| 5 | 1774 | 1774 | Yes | 5.26 |
| 6 | 1721 | 1721 | Yes | 6.06 |
| 7 | 1177 | 1177 | Yes | 5.21 |
| 8 | 1875 | 1875 | Yes | 5.52 |
| 9 | 2076 | 2076 | Yes | 5.03 |
| 10 | 1800 | 1800 | Yes | 5.45 |
| 11 | 1453 | 1453 | Yes | 4.99 |
| 12 | 774 | 774 | Yes | 4.22 |
| 13 | 1669 | 1669 | Yes | 7.39 |
| 14 | 1064 | 1064 | Yes | 5.06 |
| 15 | 756 | 756 | Yes | 4.41 |
| 16 | 909 | 909 | Yes | 5.57 |
| 17 | 1441 | 1441 | Yes | 5.57 |
| 18 | 2190 | 2190 | Yes | 5.67 |
| 19 | 1178 | 1178 | Yes | 5.81 |
| 20 | 2138 | 2138 | Yes | 5.75 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 56 | 55 | No | 14.91 |
| 2 | 72 | 72 | Yes | 14.35 |
| 3 | 39 | 39 | Yes | 26.35 |
| 4 | 68 | 68 | Yes | 13.93 |
| 5 | 60 | 60 | Yes | 14.57 |
| 6 | 54 | 54 | Yes | 15.82 |
| 7 | 59 | 59 | Yes | 14.1 |
| 8 | 48 | 48 | Yes | 14.67 |
| 9 | 51 | 51 | Yes | 15.24 |
| 10 | 62 | 62 | Yes | 16.59 |
| 11 | 72 | **Re | No | 34.09 |
| 12 | 49 | 49 | Yes | 15.07 |
| 13 | 65 | 67 | No | 14.11 |
| 14 | 37 | 37 | Yes | 23.69 |
| 15 | 43 | 43 | Yes | 15.53 |
| 16 | 43 | 43 | Yes | 12.3 |
| 17 | 56 | TIMEOUT | No | 120.03 |
| 18 | 45 | 45 | Yes | 15.93 |
| 19 | 53 | 52 | No | 14.49 |
| 20 | 61 | 61 | Yes | 14.83 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | XYOHJVN | XYOHJVN | Yes | 5.31 |
| 2 | BTUIJMA | BTUIJMA | Yes | 5.48 |
| 3 | MXJLHFD | MXJLHFD | Yes | 4.77 |
| 4 | FQASJLK | FQASJLK | Yes | 4.66 |
| 5 | GSZDXRP | GSZDXRP | Yes | 4.93 |
| 6 | MHAKLRB | MHAKLRB | Yes | 5.69 |
| 7 | MAJWFKT | MAJWFT | No | 7.3 |
| 8 | XYILCAJ | XYILCAJ | Yes | 5.72 |
| 9 | VONRCHA | VONRCHA | Yes | 6.33 |
| 10 | EDUTYPQ | EDUTYPQ | Yes | 5.03 |
| 11 | WIOKLYU | WIKLYU | No | 5.79 |
| 12 | XIKFBNV | XIKFBNV | Yes | 6.42 |
| 13 | EMJQDNG | EMJQDNG | Yes | 4.74 |
| 14 | MVTAQFP | MVTAQFP | Yes | 5.52 |
| 15 | NZAMVIG | NZAMVIG | Yes | 21.48 |
| 16 | WDEUTGV | WDEUTGV | Yes | 5.38 |
| 17 | KUARLJX | KUARLJX | Yes | 4.72 |
| 18 | SDQWRFU | SDQWRFU | Yes | 15.17 |
| 19 | EALQKSX | EALQKSX | Yes | 5.72 |
| 20 | ZQJXOFG | ZQJXOFG | Yes | 5.44 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.8, 9.2] | 9.2 0.8 | Yes | 10.24 |
| 2 | [4.1, 5.9] | 4.1 5.9 | Yes | 9.97 |
| 3 | [3.0, 7.0] | 7.0 3.0 | Yes | 9.85 |
| 4 | [0.9, 9.1] | 9.1 0.9 | Yes | 9.68 |
| 5 | [2.4, 7.6] | 2.4 7.6 | Yes | 13.38 |
| 6 | [2.4, 7.6] | 7.6 2.4 | Yes | 17.5 |
| 7 | [1.9, 8.1] | 1.9 8.1 | Yes | 8.35 |
| 8 | [2.9, 7.1] | 7.1 2.9 | Yes | 8.29 |
| 9 | [1.5, 8.5] | 1.5 8.5 | Yes | 11.04 |
| 10 | [3.3, 6.7] | 6.7 3.3 | Yes | 10.12 |
| 11 | [2.7, 7.3] | 2.7 7.3 | Yes | 10.21 |
| 12 | [1.6, 8.4] | 1.6 8.4 | Yes | 10.2 |
| 13 | [4.5, 5.5] | 4.5 5.5 | Yes | 21.71 |
| 14 | [0.4, 9.6] | 0.4 9.6 | Yes | 9.66 |
| 15 | [0.2, 9.8] | 0.2 9.8 | Yes | 10.95 |
| 16 | [5.0, 5.0] | 5.0 5.0 | Yes | 15.65 |
| 17 | [4.4, 5.6] | 4.4 5.6 | Yes | 10.2 |
| 18 | [2.2, 7.8] | 2.2 7.8 | Yes | 8.3 |
| 19 | [2.9, 7.1] | 7.1 2.9 | Yes | 10.18 |
| 20 | [1.8, 8.2] | 8.2 1.8 | Yes | 10.01 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 827CLFSFSD6W | 827CLFSFSD6W | Yes | 6.02 |
| 2 | K5WHO0XP71RZ | K5WHOOXP71RZ | No | 6.47 |
| 3 | 8WUO4XPKGAXD | 8WU04XPKGAXD | No | 16.86 |
| 4 | HU6R6MEUSBC9 | HU6R6MEUSBC9 | Yes | 7.05 |
| 5 | 7CYALVKJVE4Y | 7CYALVKJVE4Y | Yes | 5.95 |
| 6 | VSQ3JQB4S5VU | VSQ3JQB4S5VU | Yes | 17.96 |
| 7 | HPBDSV28AXUG | HPBDSV28AXUG | Yes | 4.48 |
| 8 | KNJHHNOZ1YT8 | KNJHHNOZ1YT8 | Yes | 6.19 |
| 9 | I1HP6TH1GXWV | I1HP6TH1GXWV | Yes | 7.08 |
| 10 | YTZVKAIIZBTV | YTZVKAIIZBTV | Yes | 4.95 |
| 11 | R8Z53HDYFZHF | R8Z53HDYFZHF | Yes | 4.98 |
| 12 | WOAUWJAOGRDK | WOAUWJAOGRDK | Yes | 16.98 |
| 13 | Y4UO70PZ8022 | Y4U070PZ8022 | No | 15.51 |
| 14 | OEP6TXT7VFHT | OEP6TXT7VFHT | Yes | 6.21 |
| 15 | BWQJL3Q3AGAI | BWQJL303AGAI | No | 5.21 |
| 16 | OPG7E4XGRH1J | OPG7E4XGRH1J | Yes | 4.36 |
| 17 | HV2486R59DIP | HV2486R59DIP | Yes | 5.42 |
| 18 | TSEMOVV4ORMZ | TSEMOVV4ORMZ | Yes | 5.3 |
| 19 | GF8VRDOIYJSH | GF8VRDOIYJSH | Yes | 6.92 |
| 20 | FUZSOUJDJ7DI | FUZSOUJDJ7DI | Yes | 5.48 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 60 | 60 | Yes | 6.05 |
| 2 | 36 | 36 | Yes | 6.58 |
| 3 | 26 | 26 | Yes | 22.36 |
| 4 | 1 | 1 | Yes | 9.35 |
| 5 | 65 | 65 | Yes | 12.15 |
| 6 | 20 | 20 | Yes | 10.18 |
| 7 | 7680 | 7680 | Yes | 9.45 |
| 8 | 243 | 243 | Yes | 6.75 |
| 9 | 3 | 3 | Yes | 10.6 |
| 10 | 7 | 7 | Yes | 5.54 |
| 11 | 73 | 73 | Yes | 11.04 |
| 12 | 3 | 3 | Yes | 24.35 |
| 13 | 5 | 11 | No | 27.35 |
| 14 | 5 | 5 | Yes | 16.82 |
| 15 | 67 | 67 | Yes | 16.46 |
| 16 | 19 | 19 | Yes | 8.88 |
| 17 | 9 | 9 | Yes | 10.22 |
| 18 | 4 | 4 | Yes | 9.94 |
| 19 | 793 | 793 | Yes | 10.0 |
| 20 | 60 | 60 | Yes | 6.35 |
