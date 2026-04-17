# Benchmark Report — gpt-5.4-nano

- **Model**: `openai/gpt-5.4-nano`
- **Date**: 2026-03-27 10:18:57

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
| sudoku_game | 5290 | 34667 | 39957 | 8 | 12 | 34.31 | 686.24 |
| add_numbers | 2907 | 682 | 3589 | 19 | 1 | 9.02 | 180.44 |
| counting_zeros | 4460 | 19389 | 23849 | 19 | 1 | 13.58 | 271.61 |
| task_decoding | 4400 | 2805 | 7205 | 20 | 0 | 5.42 | 108.45 |
| task_summation | 4503 | 6037 | 10540 | 18 | 2 | 12.12 | 242.31 |
| task_transcription | 3203 | 1934 | 5137 | 20 | 0 | 2.94 | 58.83 |
| task_sequences | 3061 | 17626 | 20687 | 14 | 6 | 15.88 | 317.67 |
| string_entry | 3492 | 21558 | 25050 | 9 | 11 | 15.43 | 308.54 |
| **TOTAL** | **31316** | **104698** | **136014** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 2 6 1 3 4 2 4 6 3 6 5 3 |  | No | 33.64 |
| 2 | 2 3 5 6 2 5 2 1 3 1 6 4 2 4 | 2 3 5 6 2 5 2 1 3 1 6 4 2 4 | Yes | 16.09 |
| 3 | 6 3 4 6 5 3 1 4 4 3 2 1 5 2 |  | No | 39.24 |
| 4 | 2 2 5 1 6 4 2 3 5 6 1 5 4 2 |  | No | 50.93 |
| 5 | 2 5 2 3 3 1 6 4 4 2 1 3 1 6 |  | No | 51.26 |
| 6 | 6 1 6 1 2 3 5 4 5 3 5 6 4 2 |  | No | 52.45 |
| 7 | 6 2 2 4 2 1 4 5 1 1 5 6 4 3 | 6 2 2 4 2 1 4 5 1 1 5 6 4 3 | Yes | 18.21 |
| 8 | 1 6 3 2 6 4 3 1 2 3 6 1 2 6 |  | No | 34.77 |
| 9 | 5 3 2 6 2 4 1 3 2 4 2 3 4 1 | 5 3 2 6 2 4 1 3 2 4 2 3 4 1 | Yes | 25.21 |
| 10 | 3 5 1 2 5 4 1 4 5 2 4 1 3 5 | 3 5 1 2 5 4 1 4 5 2 4 1 3 5 | Yes | 21.86 |
| 11 | 5 1 6 3 5 4 5 6 1 3 3 5 2 4 |  | No | 25.03 |
| 12 | 6 5 3 2 1 6 2 4 3 1 6 2 4 3 | 6 5 3 2 1 6 2 4 3 1 6 2 4 3 | Yes | 18.21 |
| 13 | 4 3 6 1 3 5 6 1 2 3 5 4 2 2 | 4 3 6 1 3 5 6 1 2 3 5 4 2 2 | Yes | 27.02 |
| 14 | 2 5 4 2 6 6 3 1 5 4 5 2 2 3 | 2 5 4 2 6 6 3 1 5 4 5 2 2 3 | Yes | 15.74 |
| 15 | 3 2 4 5 2 5 4 6 2 1 5 4 5 3 |  | No | 44.81 |
| 16 | 1 3 6 4 3 5 1 1 5 2 4 4 3 6 |  | No | 42.87 |
| 17 | 4 1 3 5 3 6 6 2 4 2 4 3 6 1 |  | No | 56.98 |
| 18 | 2 6 4 3 1 2 6 6 1 5 4 3 2 5 |  | No | 46.04 |
| 19 | 5 4 3 2 2 4 4 3 2 5 1 3 6 3 | 5 4 3 2 2 4 4 3 2 5 1 3 6 3 | Yes | 18.67 |
| 20 | 4 2 4 1 2 5 1 2 5 1 5 5 4 3 |  | No | 47.15 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1062 | 1062 | Yes | 2.8 |
| 2 | 1087 | 1087 | Yes | 3.0 |
| 3 | 1913 | 1913 | Yes | 3.31 |
| 4 | 1806 | 1806 | Yes | 3.57 |
| 5 | 1836 | 1836 | Yes | 3.05 |
| 6 | 1753 | 1753 | Yes | 3.75 |
| 7 | 2315 | 2315 | Yes | 3.14 |
| 8 | 1299 | 1299 | Yes | 3.63 |
| 9 | 1908 | 1908 | Yes | 3.25 |
| 10 | 1163 | 1163 | Yes | 2.73 |
| 11 | 1781 | 1781 | Yes | 3.04 |
| 12 | 1611 | 1611 | Yes | 3.24 |
| 13 | 1854 | 1854 | Yes | 2.85 |
| 14 | 1445 | 1445 | Yes | 3.37 |
| 15 | 1341 | 1341 | Yes | 2.84 |
| 16 | 1535 | 1535 | Yes | 2.87 |
| 17 | 2043 | 2043 | Yes | 1.17 |
| 18 | 1179 | 1179 | Yes | 4.02 |
| 19 | 1605 | TIMEOUT | No | 120.02 |
| 20 | 1907 | 1907 | Yes | 4.77 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 55 | 55 | Yes | 9.76 |
| 2 | 64 | 64 | Yes | 6.91 |
| 3 | 68 | 68 | Yes | 13.73 |
| 4 | 65 | 65 | Yes | 13.88 |
| 5 | 39 | 39 | Yes | 18.85 |
| 6 | 71 | 71 | Yes | 13.45 |
| 7 | 42 | 42 | Yes | 7.11 |
| 8 | 45 | 45 | Yes | 13.97 |
| 9 | 71 | 71 | Yes | 8.61 |
| 10 | 67 | 67 | Yes | 14.34 |
| 11 | 57 | 57 | Yes | 15.6 |
| 12 | 64 | 63 | No | 11.31 |
| 13 | 38 | 38 | Yes | 11.76 |
| 14 | 58 | 58 | Yes | 9.99 |
| 15 | 60 | 60 | Yes | 15.86 |
| 16 | 63 | 63 | Yes | 10.29 |
| 17 | 35 | 35 | Yes | 16.55 |
| 18 | 54 | 54 | Yes | 19.3 |
| 19 | 36 | 36 | Yes | 24.02 |
| 20 | 43 | 43 | Yes | 16.3 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | GBJACVN | GBJACVN | Yes | 7.94 |
| 2 | DVHWBRO | DVHWBRO | Yes | 6.73 |
| 3 | HLJUGPZ | HLJUGPZ | Yes | 6.03 |
| 4 | JVCEYAR | JVCEYAR | Yes | 5.2 |
| 5 | LXODNWF | LXODNWF | Yes | 3.7 |
| 6 | DHZEPTR | DHZEPTR | Yes | 7.26 |
| 7 | LYJUDPC | LYJUDPC | Yes | 4.74 |
| 8 | TCDMOGS | TCDMOGS | Yes | 5.51 |
| 9 | FKARUSJ | FKARUSJ | Yes | 5.57 |
| 10 | TUIOBRN | TUIOBRN | Yes | 6.36 |
| 11 | NRTGKSW | NRTGKSW | Yes | 5.12 |
| 12 | XWEYKDG | XWEYKDG | Yes | 6.87 |
| 13 | VJAIOYR | VJAIOYR | Yes | 2.18 |
| 14 | UGLSIOR | UGLSIOR | Yes | 1.74 |
| 15 | EFZNJTR | EFZNJTR | Yes | 5.72 |
| 16 | HNQRKXF | HNQRKXF | Yes | 3.7 |
| 17 | ZCSKXRG | ZCSKXRG | Yes | 6.35 |
| 18 | BGLDUAR | BGLDUAR | Yes | 7.08 |
| 19 | ZERDUTA | ZERDUTA | Yes | 4.59 |
| 20 | MCVDQUI | MCVDQUI | Yes | 6.08 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.6, 9.4] | 9.4 0.6 | Yes | 7.76 |
| 2 | [2.7, 7.3] | 7.3 2.7 | Yes | 5.69 |
| 3 | [3.2, 6.8] | 6.8 3.2 | Yes | 7.27 |
| 4 | [2.3, 7.7] | 2.3 7.7 | Yes | 4.85 |
| 5 | [2.2, 7.8] | 2.2 7.8 | Yes | 6.44 |
| 6 | [3.1, 6.9] | 1.3 6.7 | No | 9.55 |
| 7 | [4.8, 5.2] | 5.2 4.8 | Yes | 5.74 |
| 8 | [2.6, 7.4] | 7.4 2.6 | Yes | 7.41 |
| 9 | [4.5, 5.5] | TIMEOUT | No | 120.02 |
| 10 | [1.1, 8.9] | 8.9 1.1 | Yes | 6.26 |
| 11 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.19 |
| 12 | [0.4, 9.6] | 9.6 0.4 | Yes | 4.04 |
| 13 | [1.2, 8.8] | 1.2 8.8 | Yes | 6.33 |
| 14 | [4.5, 5.5] | 4.5 5.5 | Yes | 6.59 |
| 15 | [1.2, 8.8] | 1.2 8.8 | Yes | 8.3 |
| 16 | [1.4, 8.6] | 8.6 1.4 | Yes | 5.69 |
| 17 | [0.3, 9.7] | 9.7 0.3 | Yes | 5.42 |
| 18 | [1.8, 8.2] | 8.2 1.8 | Yes | 7.6 |
| 19 | [2.0, 8.0] | 8.0 2.0 | Yes | 5.55 |
| 20 | [2.2, 7.8] | 7.8 2.2 | Yes | 5.6 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ARTOVXR0CMHW | ARTOVXR0CMHW | Yes | 1.72 |
| 2 | BHUC5EJO1V8A | BHUC5EJO1V8A | Yes | 1.36 |
| 3 | WSCS376IUH1W | WSCS376IUH1W | Yes | 1.5 |
| 4 | 32EAVNPGK7LW | 32EAVNPGK7LW | Yes | 7.2 |
| 5 | 164WABW07VK2 | 164WABW07VK2 | Yes | 1.24 |
| 6 | WFVL2QHKBZC6 | WFVL2QHKBZC6 | Yes | 4.21 |
| 7 | YWY754NRC11X | YWY754NRC11X | Yes | 3.95 |
| 8 | XJSBSZZRGUX7 | XJSBSZZRGUX7 | Yes | 0.87 |
| 9 | QQAU8M8NV0U5 | QQAU8M8NV0U5 | Yes | 2.16 |
| 10 | YC4V8L0JSO4L | YC4V8L0JSO4L | Yes | 4.25 |
| 11 | 941SBQZ4Z1YA | 941SBQZ4Z1YA | Yes | 1.07 |
| 12 | 6BUGQ04MLFNV | 6BUGQ04MLFNV | Yes | 3.35 |
| 13 | A6Q5BH8WASNZ | A6Q5BH8WASNZ | Yes | 4.26 |
| 14 | ST5HZO4PRD0C | ST5HZO4PRD0C | Yes | 4.39 |
| 15 | DN5KOEHEA5P5 | DN5KOEHEA5P5 | Yes | 1.96 |
| 16 | UKB5JMWXI6AT | UKB5JMWXI6AT | Yes | 1.34 |
| 17 | IYKDQ6L4VW3S | IYKDQ6L4VW3S | Yes | 2.75 |
| 18 | BYX379IM1U3D | BYX379IM1U3D | Yes | 0.8 |
| 19 | A4MPV925564Q | A4MPV925564Q | Yes | 5.69 |
| 20 | N5F545O3BFZK | N5F545O3BFZK | Yes | 4.75 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 | 2 | No | 15.66 |
| 2 | 73 | 73 | Yes | 4.22 |
| 3 | 23 | 23 | Yes | 4.69 |
| 4 | 4096 |  | No | 37.16 |
| 5 | 5 | 5 | Yes | 8.49 |
| 6 | 198 | 198 | Yes | 5.11 |
| 7 | 10 |  | No | 47.29 |
| 8 | 1 | 1 | Yes | 10.81 |
| 9 | 793 | 793 | Yes | 2.78 |
| 10 | 3 |  | No | 41.31 |
| 11 | 4 | 4 | Yes | 7.18 |
| 12 | 48 | 48 | Yes | 4.01 |
| 13 | 67 | 67 | Yes | 3.44 |
| 14 | 64 |  | No | 34.35 |
| 15 | 60 | 60 | Yes | 11.53 |
| 16 | 1440 | 1440 | Yes | 4.09 |
| 17 | 4 | 4 | Yes | 14.05 |
| 18 | 28 | 28 | Yes | 17.39 |
| 19 | 26 |  | No | 41.72 |
| 20 | 31 | 31 | Yes | 2.38 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <_/</ ))_ | <_/</ ))_ | Yes | 14.59 |
| 2 | (()\_\(</ | (()\_\(</ | Yes | 4.8 |
| 3 | //_///) < | /\) <(_<//_///) < | No | 5.15 |
| 4 | <__)___() | /\) <(_<) | No | 10.74 |
| 5 |  _< \(_)\ | /\) <(_<) _< \(_)\ | No | 15.29 |
| 6 | (/__\<\ / | (/__\< / | No | 6.4 |
| 7 | <_)\<<)<) | <_)\<<)<) | Yes | 5.96 |
| 8 | _ ) ( / \ |  | No | 57.4 |
| 9 | <<_/<__ < | <<_/<__ < | Yes | 6.37 |
| 10 | <_)\<//\) | /\) <(_<) | No | 6.84 |
| 11 | \\( \_</_ | \\( \_</_ | Yes | 16.44 |
| 12 | )_<\<)_\< | )_<\<)_\< | Yes | 19.85 |
| 13 | ))_\_ )\\ | ))_\_ )\\ | Yes | 14.63 |
| 14 | ( )((/(_) | /\) <(_<) | No | 8.79 |
| 15 | </<\ )(\\ |  | No | 48.33 |
| 16 | _/<<)//(  | _/<<)//( | No | 10.39 |
| 17 | _// \/ </ | _// \/ </ | Yes | 11.51 |
| 18 |  _ ) <))_ | /\) <(_<) _ ) <))_ | No | 22.15 |
| 19 | <<((<(_<< | <<((<(_<< | Yes | 10.03 |
| 20 | //)\\ \(  | //)\\ \( | No | 12.88 |
