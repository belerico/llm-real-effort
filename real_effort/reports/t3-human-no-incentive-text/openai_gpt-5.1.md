# Benchmark Report — gpt-5.1

- **Model**: `openai/gpt-5.1`
- **Date**: 2026-03-27 10:24:54

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
| sudoku_game | 5304 | 40352 | 45656 | 1 | 19 | 47.32 | 946.34 |
| add_numbers | 3060 | 949 | 4009 | 20 | 0 | 3.46 | 69.3 |
| counting_zeros | 4460 | 32183 | 36643 | 17 | 3 | 31.28 | 625.63 |
| task_decoding | 4400 | 5019 | 9419 | 20 | 0 | 6.75 | 135.0 |
| task_summation | 4740 | 7452 | 12192 | 20 | 0 | 7.47 | 149.41 |
| task_transcription | 3194 | 949 | 4143 | 20 | 0 | 2.00 | 39.92 |
| task_sequences | 3060 | 6659 | 9719 | 19 | 1 | 9.51 | 190.28 |
| string_entry | 3508 | 14938 | 18446 | 10 | 10 | 18.79 | 375.83 |
| **TOTAL** | **31726** | **108501** | **140227** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 3 3 6 4 1 6 1 3 3 1 6 2 6 |  | No | 42.4 |
| 2 | 3 1 6 5 3 6 5 3 4 6 3 2 4 3 | 3 1 6 5 3 6 5 3 4 6 3 2 4 3 | Yes | 21.69 |
| 3 | 5 4 6 3 2 4 6 3 2 4 2 3 1 2 |  | No | 56.34 |
| 4 | 2 3 6 5 1 3 4 3 2 5 4 6 2 4 |  | No | 53.13 |
| 5 | 1 3 3 6 5 4 2 6 2 1 3 4 2 4 |  | No | 57.33 |
| 6 | 4 6 3 1 5 1 6 2 3 2 5 5 2 1 |  | No | 51.81 |
| 7 | 6 4 5 4 3 2 6 5 1 6 5 2 4 3 |  | No | 48.54 |
| 8 | 4 6 1 3 2 1 4 5 2 6 6 2 4 6 |  | No | 57.77 |
| 9 | 3 1 2 4 1 2 6 6 6 4 3 5 1 2 |  | No | 43.77 |
| 10 | 5 4 6 6 2 6 3 2 4 3 3 1 5 1 |  | No | 50.74 |
| 11 | 6 5 3 2 1 6 1 3 2 6 6 1 4 2 |  | No | 41.78 |
| 12 | 5 4 6 3 5 6 3 5 5 4 3 2 2 6 |  | No | 35.85 |
| 13 | 3 2 5 4 4 5 3 2 2 5 4 3 6 2 |  | No | 61.25 |
| 14 | 1 4 6 6 4 3 2 2 1 1 5 2 2 4 |  | No | 48.03 |
| 15 | 2 3 6 1 5 4 3 4 2 5 4 5 3 5 |  | No | 46.23 |
| 16 | 2 6 5 1 2 3 5 4 4 2 1 2 4 6 |  | No | 46.51 |
| 17 | 6 2 5 1 2 4 5 2 1 6 6 2 4 1 |  | No | 40.7 |
| 18 | 2 5 4 3 1 5 1 6 2 5 4 6 2 5 |  | No | 56.99 |
| 19 | 3 6 3 6 1 5 2 2 5 3 2 6 6 5 |  | No | 38.0 |
| 20 | 5 3 6 3 5 4 2 1 4 1 5 3 6 3 |  | No | 47.46 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1922 | 1922 | Yes | 4.26 |
| 2 | 1958 | 1958 | Yes | 3.2 |
| 3 | 2230 | 2230 | Yes | 3.23 |
| 4 | 691 | 691 | Yes | 2.39 |
| 5 | 1393 | 1393 | Yes | 3.05 |
| 6 | 1180 | 1180 | Yes | 3.36 |
| 7 | 902 | 902 | Yes | 2.97 |
| 8 | 1868 | 1868 | Yes | 3.16 |
| 9 | 2262 | 2262 | Yes | 3.29 |
| 10 | 1434 | 1434 | Yes | 4.17 |
| 11 | 1532 | 1532 | Yes | 4.1 |
| 12 | 1778 | 1778 | Yes | 3.32 |
| 13 | 995 | 995 | Yes | 3.34 |
| 14 | 1239 | 1239 | Yes | 2.85 |
| 15 | 2421 | 2421 | Yes | 2.56 |
| 16 | 2022 | 2022 | Yes | 2.5 |
| 17 | 1322 | 1322 | Yes | 3.6 |
| 18 | 1783 | 1783 | Yes | 2.73 |
| 19 | 1358 | 1358 | Yes | 7.48 |
| 20 | 2637 | 2637 | Yes | 3.73 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 50 | 50 | Yes | 26.25 |
| 2 | 40 |  | No | 52.19 |
| 3 | 37 |  | No | 63.2 |
| 4 | 37 | 37 | Yes | 46.02 |
| 5 | 54 | 54 | Yes | 29.05 |
| 6 | 58 |  | No | 53.79 |
| 7 | 65 | 65 | Yes | 18.33 |
| 8 | 39 | 39 | Yes | 30.12 |
| 9 | 68 | 68 | Yes | 16.02 |
| 10 | 69 | 69 | Yes | 25.01 |
| 11 | 36 | 36 | Yes | 30.04 |
| 12 | 36 | 36 | Yes | 25.2 |
| 13 | 68 | 68 | Yes | 34.51 |
| 14 | 58 | 58 | Yes | 41.67 |
| 15 | 65 | 65 | Yes | 20.51 |
| 16 | 48 | 48 | Yes | 17.93 |
| 17 | 55 | 55 | Yes | 19.93 |
| 18 | 46 | 46 | Yes | 27.65 |
| 19 | 48 | 48 | Yes | 26.69 |
| 20 | 56 | 56 | Yes | 21.51 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | PFCSHNZ | PFCSHNZ | Yes | 6.35 |
| 2 | KBIYRLP | KBIYRLP | Yes | 2.74 |
| 3 | POARTGB | POARTGB | Yes | 2.89 |
| 4 | TEVXOQD | TEVXOQD | Yes | 8.89 |
| 5 | VBKQYJF | VBKQYJF | Yes | 5.2 |
| 6 | QMTUILB | QMTUILB | Yes | 5.41 |
| 7 | HRTINCV | HRTINCV | Yes | 9.48 |
| 8 | ZBFOLCM | ZBFOLCM | Yes | 6.27 |
| 9 | QEOXYTW | QEOXYTW | Yes | 6.31 |
| 10 | EIQWABR | EIQWABR | Yes | 5.66 |
| 11 | DKHNJCM | DKHNJCM | Yes | 6.13 |
| 12 | BVOQKDR | BVOQKDR | Yes | 5.29 |
| 13 | FVPAHTM | FVPAHTM | Yes | 7.49 |
| 14 | BOVTDYE | BOVTDYE | Yes | 7.92 |
| 15 | TUEQIFX | TUEQIFX | Yes | 2.96 |
| 16 | HDQACVX | HDQACVX | Yes | 2.51 |
| 17 | AIFJMKO | AIFJMKO | Yes | 22.31 |
| 18 | ODEJABT | ODEJABT | Yes | 8.15 |
| 19 | EAZSQIP | EAZSQIP | Yes | 8.68 |
| 20 | XLMPRNI | XLMPRNI | Yes | 4.36 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.5, 9.5] | 0.5 9.5 | Yes | 7.32 |
| 2 | [0.4, 9.6] | 9.6 0.4 | Yes | 7.04 |
| 3 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.66 |
| 4 | [2.7, 7.3] | 2.7 7.3 | Yes | 7.26 |
| 5 | [1.2, 8.8] | 1.2 8.8 | Yes | 9.05 |
| 6 | [2.7, 7.3] | 2.7 7.3 | Yes | 7.61 |
| 7 | [1.7, 8.3] | 1.7 8.3 | Yes | 6.5 |
| 8 | [4.3, 5.7] | 5.7 4.3 | Yes | 7.31 |
| 9 | [0.1, 9.9] | 9.9 0.1 | Yes | 6.08 |
| 10 | [2.2, 7.8] | 7.8 2.2 | Yes | 7.68 |
| 11 | [4.4, 5.6] | 4.4 5.6 | Yes | 13.23 |
| 12 | [3.5, 6.5] | 3.5 6.5 | Yes | 6.1 |
| 13 | [3.8, 6.2] | 3.8 6.2 | Yes | 3.53 |
| 14 | [4.0, 6.0] | 4.0 6.0 | Yes | 7.37 |
| 15 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.77 |
| 16 | [0.7, 9.3] | 9.3 0.7 | Yes | 12.37 |
| 17 | [4.0, 6.0] | 6.0 4.0 | Yes | 8.78 |
| 18 | [2.6, 7.4] | 2.6 7.4 | Yes | 5.58 |
| 19 | [2.9, 7.1] | 2.9 7.1 | Yes | 6.25 |
| 20 | [1.9, 8.1] | 8.1 1.9 | Yes | 7.9 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NH99V1VDX04J | NH99V1VDX04J | Yes | 1.4 |
| 2 | IU9UTTP1DYEK | IU9UTTP1DYEK | Yes | 1.4 |
| 3 | SIV0RSTNJDW2 | SIV0RSTNJDW2 | Yes | 1.54 |
| 4 | VBE250ZQLOEW | VBE250ZQLOEW | Yes | 1.38 |
| 5 | PPJPXYA55NS8 | PPJPXYA55NS8 | Yes | 2.85 |
| 6 | D45L0LRAZMOM | D45L0LRAZMOM | Yes | 1.29 |
| 7 | BFGDZATX9E6O | BFGDZATX9E6O | Yes | 2.84 |
| 8 | ODVYAFZXMOGG | ODVYAFZXMOGG | Yes | 1.3 |
| 9 | 29DQ9I9ZWLPD | 29DQ9I9ZWLPD | Yes | 1.38 |
| 10 | RS49JY5WU139 | RS49JY5WU139 | Yes | 1.27 |
| 11 | LIY00PG6K16N | LIY00PG6K16N | Yes | 1.16 |
| 12 | RBVV6S8WE46N | RBVV6S8WE46N | Yes | 3.59 |
| 13 | FS15QAV40NXM | FS15QAV40NXM | Yes | 3.1 |
| 14 | L1WFSDEJJ1N5 | L1WFSDEJJ1N5 | Yes | 1.96 |
| 15 | 1UX6GIPL6U30 | 1UX6GIPL6U30 | Yes | 1.62 |
| 16 | 4DVSV8QMI9IG | 4DVSV8QMI9IG | Yes | 1.63 |
| 17 | I751IUJIT544 | I751IUJIT544 | Yes | 3.36 |
| 18 | YLXD22WLVI9I | YLXD22WLVI9I | Yes | 3.47 |
| 19 | KH1VB68OBD7L | KH1VB68OBD7L | Yes | 1.61 |
| 20 | DXNG6F1BYSWE | DXNG6F1BYSWE | Yes | 1.77 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 65 | Yes | 5.33 |
| 2 | 64 | 64 | Yes | 5.59 |
| 3 | 28 | 28 | Yes | 10.46 |
| 4 | 63 | 63 | Yes | 3.72 |
| 5 | 198 | 198 | Yes | 4.81 |
| 6 | 243 | 243 | Yes | 3.03 |
| 7 | 6 | 6 | Yes | 4.23 |
| 8 | 20 |  | No | 51.34 |
| 9 | 7680 | 7680 | Yes | 6.04 |
| 10 | 3 | 3 | Yes | 11.85 |
| 11 | 5 | 5 | Yes | 5.05 |
| 12 | 9 | 9 | Yes | 5.52 |
| 13 | 23 | 23 | Yes | 4.88 |
| 14 | 7 | 7 | Yes | 3.33 |
| 15 | 3 | 3 | Yes | 12.83 |
| 16 | 4 | 4 | Yes | 6.4 |
| 17 | 4 | 4 | Yes | 7.89 |
| 18 | 60 | 60 | Yes | 10.53 |
| 19 | 19 | 19 | Yes | 6.1 |
| 20 | 26 | 26 | Yes | 21.34 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <_())() / | <_())() / | Yes | 7.23 |
| 2 | /(( (\)/_ | /(( (\)/_ | Yes | 8.34 |
| 3 | __/()\\(< | __/()\\(< | Yes | 9.24 |
| 4 | /()/ ((<) | /()/ ((<) | Yes | 2.84 |
| 5 | ))<_)  (  | ))<_)  ( | No | 12.87 |
| 6 | \\(/ _\)/ | \\(/ _\) | No | 7.22 |
| 7 | _/)()(()_ | _/)()(()_ | Yes | 34.5 |
| 8 | /\)/<\) < | /\)/<\) < | Yes | 17.41 |
| 9 | ((\(\<)   | ((\(\<) | No | 15.07 |
| 10 | <)<(_/()  | <)<(_/() | No | 8.68 |
| 11 | (\ )(\/   | (\ )(\/ | No | 19.53 |
| 12 | /))((/(// | /))((/(// | Yes | 9.17 |
| 13 |    ( )(<) | ( )(<) | No | 12.6 |
| 14 |  \/_\<\ _ |  | No | 44.82 |
| 15 |  <\\(_\\< |  | No | 58.77 |
| 16 | ((/ <\/(_ | ((/ <\/(_ | Yes | 4.7 |
| 17 | (<_\/ \)/ | (<_\/ \)/ | Yes | 11.38 |
| 18 | \((_\<//) |  | No | 74.29 |
| 19 | ( <\_ /// | ( <\_ /// | Yes | 5.18 |
| 20 |   /)\ (   | /)\ ( | No | 11.98 |
