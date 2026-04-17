# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
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
| sudoku_game | 8100 | 40960 | 49060 | 0 | 20 | 68.78 | 1375.86 |
| add_numbers | 7120 | 5066 | 12186 | 20 | 0 | 7.49 | 149.99 |
| counting_zeros | 7180 | 40960 | 48140 | 0 | 20 | 73.92 | 1478.8 |
| task_decoding | 10440 | 16543 | 26983 | 19 | 1 | 15.84 | 317.06 |
| task_summation | 7440 | 21419 | 28859 | 20 | 0 | 21.34 | 427.07 |
| task_transcription | 7200 | 15027 | 22227 | 15 | 5 | 15.18 | 303.69 |
| task_sequences | 3060 | 9449 | 12509 | 19 | 1 | 12.08 | 241.61 |
| **TOTAL** | **50540** | **149424** | **199964** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 5 3 4 1 3 4 5 3 5 6 1 4 |  | No | 55.49 |
| 2 | 5 4 1 4 6 5 6 3 1 4 5 4 6 3 |  | No | 61.58 |
| 3 | 3 3 6 4 3 1 5 4 4 5 3 4 6 1 |  | No | 60.39 |
| 4 | 3 5 4 1 5 2 4 6 4 3 5 5 4 3 |  | No | 52.0 |
| 5 | 4 5 3 2 1 6 3 4 3 5 3 1 1 5 |  | No | 76.33 |
| 6 | 1 6 4 1 4 6 4 5 4 5 3 2 1 6 |  | No | 62.91 |
| 7 | 5 4 3 1 3 1 2 6 6 2 5 3 1 6 |  | No | 68.41 |
| 8 | 4 1 3 4 5 2 2 3 4 5 6 2 1 4 |  | No | 76.17 |
| 9 | 6 2 5 1 5 4 1 5 6 6 2 3 5 6 |  | No | 64.87 |
| 10 | 5 2 1 1 5 5 6 3 1 1 3 4 5 6 |  | No | 72.51 |
| 11 | 4 1 3 2 2 6 3 3 4 5 1 2 6 5 |  | No | 57.27 |
| 12 | 3 6 2 5 4 5 1 4 2 6 5 1 4 3 |  | No | 76.03 |
| 13 | 2 1 5 6 3 5 2 4 6 3 1 5 4 1 |  | No | 78.17 |
| 14 | 1 3 5 6 4 5 4 3 2 5 3 6 4 1 |  | No | 70.75 |
| 15 | 3 6 2 3 2 5 6 5 3 2 2 6 1 4 |  | No | 75.46 |
| 16 | 4 1 3 4 3 5 6 1 6 2 4 2 1 6 |  | No | 75.8 |
| 17 | 2 4 6 5 2 4 6 3 5 6 6 5 3 5 |  | No | 70.06 |
| 18 | 2 4 2 5 3 5 1 6 5 4 5 6 2 4 |  | No | 83.72 |
| 19 | 5 5 2 3 5 2 6 1 4 4 1 2 3 5 |  | No | 70.0 |
| 20 | 5 3 1 2 4 5 5 4 3 1 6 1 2 3 |  | No | 67.73 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2721 | 2721 | Yes | 6.78 |
| 2 | 1728 | 1728 | Yes | 8.79 |
| 3 | 2020 | 2020 | Yes | 4.86 |
| 4 | 1272 | 1272 | Yes | 5.09 |
| 5 | 1777 | 1777 | Yes | 8.56 |
| 6 | 872 | 872 | Yes | 10.06 |
| 7 | 1434 | 1434 | Yes | 6.85 |
| 8 | 2064 | 2064 | Yes | 6.44 |
| 9 | 2124 | 2124 | Yes | 7.08 |
| 10 | 1739 | 1739 | Yes | 8.65 |
| 11 | 1518 | 1518 | Yes | 6.48 |
| 12 | 1061 | 1061 | Yes | 6.91 |
| 13 | 2076 | 2076 | Yes | 5.25 |
| 14 | 1175 | 1175 | Yes | 12.71 |
| 15 | 1890 | 1890 | Yes | 8.56 |
| 16 | 1476 | 1476 | Yes | 8.23 |
| 17 | 1682 | 1682 | Yes | 5.63 |
| 18 | 2089 | 2089 | Yes | 9.42 |
| 19 | 1474 | 1474 | Yes | 5.54 |
| 20 | 1491 | 1491 | Yes | 8.0 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 63 |  | No | 67.74 |
| 2 | 62 |  | No | 51.59 |
| 3 | 52 |  | No | 74.13 |
| 4 | 38 |  | No | 97.52 |
| 5 | 64 |  | No | 98.32 |
| 6 | 35 |  | No | 77.82 |
| 7 | 70 |  | No | 80.24 |
| 8 | 45 |  | No | 76.62 |
| 9 | 51 |  | No | 75.6 |
| 10 | 41 |  | No | 107.33 |
| 11 | 61 |  | No | 85.22 |
| 12 | 66 |  | No | 59.85 |
| 13 | 47 |  | No | 62.94 |
| 14 | 39 |  | No | 70.98 |
| 15 | 72 |  | No | 61.84 |
| 16 | 43 |  | No | 75.65 |
| 17 | 38 |  | No | 57.77 |
| 18 | 48 |  | No | 67.14 |
| 19 | 36 |  | No | 57.98 |
| 20 | 73 |  | No | 72.18 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | TIFWDNR | TIFWDNR | Yes | 17.48 |
| 2 | DRLQZXO | DRLQZXO | Yes | 22.46 |
| 3 | XEHFSVG | XEHFSVG | Yes | 20.73 |
| 4 | PBZTXLQ | PBZTXLQ | Yes | 12.36 |
| 5 | BPJZTSD | BPJZTSD | Yes | 22.92 |
| 6 | CPAGLHZ | CPAGLHZ | Yes | 10.74 |
| 7 | TOVJKZG | TOVJKZG | Yes | 10.97 |
| 8 | FERJSGQ | FERJSGQ | Yes | 14.54 |
| 9 | FDVCOTQ | FDVCOTQ | Yes | 8.87 |
| 10 | YFXPORK | YFXPORK | Yes | 12.85 |
| 11 | JVDKNXQ | JVDKNXQ | Yes | 12.84 |
| 12 | VEPYFGR | VEPYFGR | Yes | 18.36 |
| 13 | NBZCXHE | NBZCXHE | Yes | 9.55 |
| 14 | LTSJAUG | LTSJAUG | Yes | 19.17 |
| 15 | WYTHGAN | WYTHGAN | Yes | 16.78 |
| 16 | GYBMVQL | GYBMVQL | Yes | 12.79 |
| 17 | HSNUOFQ | HSNUOFQ | Yes | 12.13 |
| 18 | XEKUSMD | XEKUSMD | Yes | 12.23 |
| 19 | OUVSQND |  | No | 35.59 |
| 20 | GKHJXQO | GKHJXQO | Yes | 13.48 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.9, 6.1] | 3.9 6.1 | Yes | 18.29 |
| 2 | [3.0, 7.0] | 7.0 3.0 | Yes | 14.92 |
| 3 | [2.9, 7.1] | 2.9 7.1 | Yes | 11.03 |
| 4 | [3.1, 6.9] | 6.9 3.1 | Yes | 18.44 |
| 5 | [0.7, 9.3] | 9.3 0.7 | Yes | 14.76 |
| 6 | [2.0, 8.0] | 2.0 8.0 | Yes | 23.62 |
| 7 | [0.7, 9.3] | 0.7 9.3 | Yes | 17.7 |
| 8 | [2.5, 7.5] | 2.5 7.5 | Yes | 14.66 |
| 9 | [3.5, 6.5] | 3.5 6.5 | Yes | 19.81 |
| 10 | [0.2, 9.8] | 0.2 9.8 | Yes | 78.58 |
| 11 | [1.5, 8.5] | 8.5 1.5 | Yes | 18.82 |
| 12 | [1.9, 8.1] | 1.9 8.1 | Yes | 16.39 |
| 13 | [1.7, 8.3] | 1.7 8.3 | Yes | 17.92 |
| 14 | [2.5, 7.5] | 7.5 2.5 | Yes | 19.14 |
| 15 | [1.9, 8.1] | 8.1 1.9 | Yes | 13.89 |
| 16 | [0.9, 9.1] | 0.9 9.1 | Yes | 14.15 |
| 17 | [2.8, 7.2] | 2.8 7.2 | Yes | 13.83 |
| 18 | [3.9, 6.1] | 6.1 3.9 | Yes | 45.71 |
| 19 | [4.3, 5.7] | 4.3 5.7 | Yes | 15.73 |
| 20 | [0.2, 9.8] | 0.2 9.8 | Yes | 19.48 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | Y7784R7ML9LJ | Y7784R7ML9LJ | Yes | 9.01 |
| 2 | 51K7674DW6GE | 51K7674DW6GE | Yes | 7.83 |
| 3 | CYP807W48SCE | CYP807W48SCE | Yes | 8.75 |
| 4 | OCMSQCZV1U3T | OCMSQCZV1U3T | Yes | 7.55 |
| 5 | BB8IFUBFLIXO | BB8IFUBFLIXO | Yes | 8.6 |
| 6 | G3I91SR6FZPP | G3I91SR6FZPP | Yes | 33.32 |
| 7 | ARI8AUZDOPQ7 | AR18AUZDOPQ7 | No | 26.07 |
| 8 | W5B3Y5YJGHH2 | W5B3Y5YJGHH2 | Yes | 9.71 |
| 9 | 7ME7J0I2XQRV | 7ME7J012XQRV | No | 31.22 |
| 10 | Y69DIJ1X6ZIA | Y69DIJ1X6ZIA | Yes | 9.39 |
| 11 | OITRCE64JFFA | OITRCE64JFFA | Yes | 8.78 |
| 12 | GAEWMLR1JRNI | GAEWMLR1JRNI | Yes | 15.91 |
| 13 | 39LO6VKFYZ19 | 39LO6VKFYZ19 | Yes | 12.71 |
| 14 | 6HA6HK79PBRH | 6HAGHK79PBRH | No | 18.33 |
| 15 | 6S95CK4U9NYD | 6S95CK4U9NYD | Yes | 11.91 |
| 16 | OG14BIB0IJP7 | OG14BIB0JP7 | No | 12.78 |
| 17 | 1RQ5TICP3UFH | 1RQ5TICP3UFH | Yes | 13.77 |
| 18 | IUVOW4N1I0F7 | IUVOW4N11QF7 | No | 33.71 |
| 19 | T9GX39QVN5N4 | T9GX39QVN5N4 | Yes | 7.83 |
| 20 | Y0SHBDF19TG8 | Y0SHBDF19TG8 | Yes | 16.37 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1440 | 1440 | Yes | 8.54 |
| 2 | 19 | 19 | Yes | 7.23 |
| 3 | 3 | 3 | Yes | 9.5 |
| 4 | 5 |  | No | 53.71 |
| 5 | 4 | 4 | Yes | 12.11 |
| 6 | 63 | 63 | Yes | 7.0 |
| 7 | 48 | 48 | Yes | 10.19 |
| 8 | 73 | 73 | Yes | 15.64 |
| 9 | 16 | 16 | Yes | 9.26 |
| 10 | 9 | 9 | Yes | 7.19 |
| 11 | 65 | 65 | Yes | 6.89 |
| 12 | 28 | 28 | Yes | 8.82 |
| 13 | 1 | 1 | Yes | 12.09 |
| 14 | 7 | 7 | Yes | 5.08 |
| 15 | 4 | 4 | Yes | 6.19 |
| 16 | 64 | 64 | Yes | 22.38 |
| 17 | 39 | 39 | Yes | 17.56 |
| 18 | 5 | 5 | Yes | 6.43 |
| 19 | 60 | 60 | Yes | 7.15 |
| 20 | 60 | 60 | Yes | 8.65 |
