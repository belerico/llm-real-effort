# Benchmark Report — gemini-2.5-flash-lite

- **Model**: `google/gemini-2.5-flash-lite`
- **Date**: 2026-03-26 10:31:47

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
| sudoku_game | 8380 | 31465 | 39845 | 0 | 20 | 12.43 | 248.89 |
| add_numbers | 38360 | 4163 | 42523 | 20 | 0 | 2.78 | 55.7 |
| counting_zeros | 28080 | 32464 | 60544 | 8 | 12 | 6.85 | 137.41 |
| task_decoding | 49160 | 16850 | 66010 | 17 | 3 | 4.99 | 99.96 |
| task_summation | 28360 | 25634 | 53994 | 19 | 1 | 6.28 | 125.86 |
| task_transcription | 28080 | 3315 | 31395 | 10 | 10 | 2.58 | 51.65 |
| task_sequences | 2483 | 11309 | 13792 | 20 | 0 | 2.97 | 59.51 |
| string_entry | 33640 | 26039 | 59679 | 1 | 19 | 6.92 | 138.53 |
| **TOTAL** | **216543** | **151239** | **367782** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 3 4 5 2 6 1 6 2 5 6 5 1 | 4 1 3 5 2 6 6 4 5 1 3 2 3 6 1 2 4 5 1 5 4 6 3 2 2 3 6 5 1 4 | No | 10.38 |
| 2 | 3 6 4 1 6 2 1 5 5 6 5 6 5 3 | 6 3 1 5 4 2 4 1 5 6 3 2 5 2 6 1 3 4 3 5 4 2 1 6 1 6 3 4 2 5 2 4 1 5 3 6 | No | 9.06 |
| 3 | 3 2 6 5 2 5 6 5 6 1 2 5 2 1 | 2 6 3 5 1 5 2 6 1 5 2 3 6 1 5 2 4 3 | No | 7.94 |
| 4 | 5 1 4 5 4 6 3 6 2 4 5 4 5 1 | 5 4 1 6 3 4 1 5 6 2 1 4 5 6 3 2 4 5 1 6 3 2 | No | 9.64 |
| 5 | 5 3 3 5 4 3 1 4 5 6 1 6 1 3 | 5 3 4 1 6 2 3 5 1 6 4 2 6 1 2 5 3 4 4 2 3 1 5 6 1 6 4 2 5 3 2 5 6 4 1 3 | No | 8.2 |
| 6 | 3 1 2 1 2 4 1 4 2 5 6 5 2 3 | 3 2 1 6 5 4 2 1 3 5 6 4 1 6 2 5 3 4 5 3 4 2 1 6 | No | 9.05 |
| 7 | 6 2 1 5 6 1 5 2 4 5 2 3 2 1 | 1 2 5 6 1 2 5 2 5 6 1 5 6 2 1 2 1 5 | No | 113.27 |
| 8 | 2 6 3 5 4 6 3 2 2 5 4 1 5 2 | 2 6 3 5 1 4 5 2 4 6 3 1 6 5 2 1 4 3 4 3 1 5 2 6 1 4 6 3 2 5 | No | 6.23 |
| 9 | 2 6 3 6 3 6 5 4 6 3 2 4 4 3 | 6 3 2 1 4 5 3 6 1 2 5 4 4 5 6 3 1 2 2 3 4 5 6 1 1 4 5 6 2 3 5 1 2 4 3 6 | No | 8.6 |
| 10 | 2 3 6 3 2 6 5 6 3 1 1 5 2 3 | 2 3 6 5 1 4 5 2 3 6 1 4 1 6 5 3 2 4 3 4 2 1 5 6 4 1 3 2 6 5 6 5 1 4 3 2 | No | 5.51 |
| 11 | 5 1 3 1 2 6 2 3 4 1 4 3 2 1 | 1 3 6 2 5 4 1 2 5 3 4 6 3 6 4 1 2 5 6 5 2 3 1 4 4 1 3 6 5 2 5 2 1 4 3 6 | No | 8.32 |
| 12 | 5 3 6 2 6 3 6 1 3 4 5 6 5 6 | 5 3 6 2 4 1 6 2 3 5 4 1 3 4 5 6 2 1 1 6 2 3 4 5 4 1 3 2 5 6 5 2 1 6 3 4 | No | 5.21 |
| 13 | 1 5 2 4 5 6 1 3 4 2 4 6 3 5 | 1 5 2 4 6 3 4 2 6 1 5 3 5 3 4 2 1 6 1 6 5 3 4 2 2 1 3 6 5 4 | No | 5.2 |
| 14 | 5 2 6 4 3 1 2 1 2 2 6 3 4 2 | 5 2 6 3 4 1 2 3 1 4 6 5 5 1 2 6 3 4 4 6 3 2 1 5 1 4 5 3 6 2 6 5 4 1 2 3 | No | 5.28 |
| 15 | 2 4 3 1 4 3 2 4 4 5 1 4 5 3 | 4 2 3 1 6 5 1 4 3 2 5 6 5 1 4 2 6 3 2 5 6 1 4 3 3 6 2 5 1 4 4 2 1 3 6 5 | No | 5.86 |
| 16 | 4 3 1 3 4 5 3 1 6 5 4 5 3 1 | 3 4 1 6 4 3 5 1 5 3 6 4 2 1 5 3 4 6 | No | 5.42 |
| 17 | 6 1 1 3 5 6 6 2 5 1 5 6 2 3 | 6 1 1 5 6 3 2 5 3 2 4 6 | No | 6.49 |
| 18 | 1 6 3 5 3 3 1 6 2 3 5 1 2 3 | 1 6 3 3 1 5 6 3 1 2 5 4 2 3 1 6 4 5 3 2 1 5 4 6 | No | 6.67 |
| 19 | 4 1 1 5 2 6 6 2 5 4 1 3 2 5 | 1 4 5 2 6 3 4 5 2 6 1 3 6 2 3 5 4 1 1 3 4 6 2 5 2 1 6 3 5 4 | No | 5.7 |
| 20 | 6 1 2 4 3 4 2 6 4 4 5 3 2 6 | 6 1 3 2 4 5 | No | 6.67 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2037 | 2037 | Yes | 2.15 |
| 2 | 1806 | 1806 | Yes | 2.57 |
| 3 | 999 | 999 | Yes | 2.6 |
| 4 | 1920 | 1920 | Yes | 4.03 |
| 5 | 1945 | 1945 | Yes | 2.92 |
| 6 | 863 | 863 | Yes | 3.09 |
| 7 | 1263 | 1263 | Yes | 2.32 |
| 8 | 1805 | 1805 | Yes | 3.29 |
| 9 | 1512 | 1512 | Yes | 2.13 |
| 10 | 1818 | 1818 | Yes | 3.91 |
| 11 | 1896 | 1896 | Yes | 2.56 |
| 12 | 1959 | 1959 | Yes | 2.21 |
| 13 | 2022 | 2022 | Yes | 2.3 |
| 14 | 2357 | 2357 | Yes | 3.3 |
| 15 | 621 | 621 | Yes | 2.94 |
| 16 | 2267 | 2267 | Yes | 3.2 |
| 17 | 1497 | 1497 | Yes | 2.8 |
| 18 | 981 | 981 | Yes | 2.28 |
| 19 | 879 | 879 | Yes | 2.45 |
| 20 | 1406 | 1406 | Yes | 2.54 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 65 | 65 | Yes | 6.43 |
| 2 | 37 | 37 | Yes | 5.5 |
| 3 | 68 | 67 | No | 5.89 |
| 4 | 36 | 36 | Yes | 5.96 |
| 5 | 53 | 55 | No | 8.2 |
| 6 | 52 | 53 | No | 7.77 |
| 7 | 63 | 70 | No | 5.75 |
| 8 | 37 | 45 | No | 5.3 |
| 9 | 72 | 78 | No | 5.77 |
| 10 | 42 | 42 | Yes | 5.48 |
| 11 | 67 | 68 | No | 8.02 |
| 12 | 35 | 35 | Yes | 6.6 |
| 13 | 45 | 45 | Yes | 9.74 |
| 14 | 72 | 72 | Yes | 8.73 |
| 15 | 74 | 72 | No | 7.02 |
| 16 | 36 | 36 | Yes | 7.66 |
| 17 | 57 | Let's count the zeros in each line: Line 1: 0 1 1 1 1 0 1 0 0 1 -> 4 zeros Line 2: 1 1 1 0 0 0 0 1 1 1 -> 4 zeros Line 3: 0 0 1 0 0 0 1 0 0 0 -> 7 zeros Line 4: 1 1 1 0 0 0 1 1 1 0 -> 4 zeros Line 5: 1 1 1 1 1 1 0 1 0 1 -> 2 zeros Line 6: 0 1 1 1 1 1 0 1 1 0 -> 3 zeros Line 7: 0 1 1 1 1 0 1 0 0 1 -> 4 zeros Line 8: 1 0 0 1 0 1 1 1 0 1 -> 4 zeros Line 9: 1 1 1 1 1 1 1 1 1 0 -> 1 zero Line 10: 1 1 1 1 1 1 1 0 1 1 -> 1 zero Line 11: 1 0 0 1 1 1 0 1 0 0 -> 5 zeros Line 12: 1 1 0 1 0 1 0 1 0 0 -> 5 zeros Line 13: 0 1 0 1 1 0 0 1 0 1 -> 5 zeros Line 14: 1 0 0 1 1 1 0 1 1 1 -> 3 zeros Line 15: 1 1 0 1 0 1 0 1 0 1 -> 5 zeros  Total zeros = 4 + 4 + 7 + 4 + 2 + 3 + 4 + 4 + 1 + 1 + 5 + 5 + 5 + 3 + 5 = 57.  Let me re-examine the image and the OCR provided by the user. The OCR has some spacing issues. Let's check the full count again, assuming each line has 10 digits.  Line 1 | No | 7.77 |
| 18 | 41 | 44 | No | 8.55 |
| 19 | 69 | 67 | No | 5.0 |
| 20 | 66 | 65 | No | 5.96 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | AYPNULK | AYPNULK | Yes | 2.92 |
| 2 | YETOQWP | YETOQWP | Yes | 7.5 |
| 3 | NCEOGLQ | NCEOGLQ | Yes | 2.64 |
| 4 | XMBHSCJ | XMBHSCJ | Yes | 7.19 |
| 5 | VZXLWBE | VZXWLBE | No | 6.54 |
| 6 | EKQPAYG | EKQPAYG | Yes | 4.97 |
| 7 | KTSFEWY | KTSFEWY | Yes | 3.1 |
| 8 | RZSJNHK | RZSNJHK | No | 6.53 |
| 9 | MLKUZQI | MLKUZQI | Yes | 6.02 |
| 10 | ZGNTVHX | ZGNTVHX | Yes | 2.74 |
| 11 | SWGMBAX | SWGMBAX | Yes | 3.0 |
| 12 | OQZRVNI | OQZRVNI | Yes | 2.59 |
| 13 | RBLGCUW | RBLGCUW | Yes | 5.73 |
| 14 | MKDNXCW | MKDNXCW | Yes | 6.93 |
| 15 | MDZGUCQ | MDZGUCQ | Yes | 7.41 |
| 16 | OPXFEZT | OPXFEZT | Yes | 6.25 |
| 17 | ILZEHYF | ILZEHYF | Yes | 3.18 |
| 18 | HXQCBAE | HXQCBAE | Yes | 7.48 |
| 19 | ZIVGOPW | ZIVGOOW | No | 3.58 |
| 20 | OIPKHYN | OIPKHYN | Yes | 3.48 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.7, 6.3] | 3.7 6.3 | Yes | 6.99 |
| 2 | [4.7, 5.3] | 4.7 5.3 | Yes | 6.32 |
| 3 | [3.4, 6.6] | 3.4 6.6 | Yes | 5.79 |
| 4 | [3.0, 7.0] | 7.0 3.0 | Yes | 5.71 |
| 5 | [1.3, 8.7] | 8.7 1.3 | Yes | 8.15 |
| 6 | [0.2, 9.8] | 0.2 9.8 | Yes | 9.47 |
| 7 | [0.8, 9.2] | 0.8 9.2 | Yes | 4.9 |
| 8 | [2.8, 7.2] | 2.8 7.2 | Yes | 7.03 |
| 9 | [0.9, 9.1] | 0.9 9.1 | Yes | 3.9 |
| 10 | [1.1, 8.9] | 1.1 8.9 | Yes | 5.3 |
| 11 | [2.5, 7.5] | 7.5 2.5 | Yes | 4.87 |
| 12 | [0.2, 9.8] | 9.8 0.2 | Yes | 5.67 |
| 13 | [3.6, 6.4] | 6.4 3.6 | Yes | 7.55 |
| 14 | [0.6, 9.4] | 0.6 9.4 | Yes | 5.48 |
| 15 | [2.0, 8.0] | 2.0 8.0 | Yes | 8.39 |
| 16 | [0.9, 9.1] | 9.1 0.9 | Yes | 6.51 |
| 17 | [4.1, 5.9] | 4.1 5.9 | Yes | 5.96 |
| 18 | [0.7, 9.3] | 9.3 0.7 | Yes | 4.75 |
| 19 | [4.4, 5.6] | 5.6 4.4 | Yes | 6.36 |
| 20 | [0.3, 9.7] | 3.1 6.9 | No | 6.54 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2L9MH1Q60ZY8 | 2L9MH1Q60ZY8 | Yes | 2.3 |
| 2 | Q85AB0EMFPLB | Q85ABOEMFPLB | No | 3.47 |
| 3 | ZH2CCH7C2MK7 | ZH2CCH7C2MK7 | Yes | 3.23 |
| 4 | NCLTZCVHP81I | NCLTZCVHP811 | No | 2.05 |
| 5 | 10HTHG6U5D4Y | 10HTHG6U5D4Y | Yes | 2.04 |
| 6 | 0XDVT5SLR90V | 0XDVTS5LR90V | No | 2.33 |
| 7 | MCI9PE6LECWC | MCI9PE6LEWC | No | 3.22 |
| 8 | 98MF4UOFY8JN | 98MF4UOFY8JN | Yes | 2.91 |
| 9 | SWQEPEF07QZV | SWQEPEF07QZV | Yes | 2.95 |
| 10 | 2YG0QMW9QMD5 | 2YGQOMW9QMD5 | No | 1.98 |
| 11 | HPUECK79PFBS | HPUECK79PFBS | Yes | 2.4 |
| 12 | 7EFEOIQDPIX6 | 7FEF0I0DPIX6 | No | 2.41 |
| 13 | BX8OQPON2KCB | BX800QPON2KCB | No | 2.0 |
| 14 | UN45EXEJB2R8 | UN45EXEJ B2R8 | No | 3.04 |
| 15 | MOQVBTG2T7MC | MOQVBTG2T7MC | Yes | 2.41 |
| 16 | OQE83KB6KPLQ | OQE83KB6KPLQ | Yes | 2.85 |
| 17 | 0LEMIDA5H4O5 | 0LEMIDA5H405 | No | 2.92 |
| 18 | Q0FL35UXG6GI | QOFL35UXG6GI | No | 2.22 |
| 19 | KXCB7QDB0FSO | KXCB7QDB0FSO | Yes | 2.13 |
| 20 | SENJ3DHE3FUY | SENJ3DHE3FUY | Yes | 2.68 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 64 | 64 | Yes | 2.02 |
| 2 | 198 | 198 | Yes | 2.98 |
| 3 | 4 | 4 | Yes | 1.75 |
| 4 | 73 | 73 | Yes | 1.71 |
| 5 | 63 | 63 | Yes | 2.36 |
| 6 | 1440 | 1440 | Yes | 1.85 |
| 7 | 39 | 39 | Yes | 1.63 |
| 8 | 65 | 65 | Yes | 3.68 |
| 9 | 9 | 9 | Yes | 2.69 |
| 10 | 20 | 20 | Yes | 7.94 |
| 11 | 9 | 9 | Yes | 2.75 |
| 12 | 3 | 3 | Yes | 4.97 |
| 13 | 6 | 6 | Yes | 1.88 |
| 14 | 28 | 28 | Yes | 1.84 |
| 15 | 31 | 31 | Yes | 2.29 |
| 16 | 48 | 48 | Yes | 1.82 |
| 17 | 19 | 19 | Yes | 1.87 |
| 18 | 5 | 5 | Yes | 5.62 |
| 19 | 793 | 793 | Yes | 1.81 |
| 20 | 3 | 3 | Yes | 6.02 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <(\) <(/( | <(\)_<(/(` | No | 6.68 |
| 2 | __()/)\(\ | __()/)\( | No | 9.04 |
| 3 | _(_\<_/<( | _( _ \ < _ / < ( | No | 5.21 |
| 4 | (_)(/)_/) | (_)(/))_/ | No | 7.28 |
| 5 | / ) (  <  | / ) (  < | No | 6.7 |
| 6 | _ (/ /(\  | - ( / / ( \ | No | 6.39 |
| 7 | _(/\__<)< | _ ( / \ _ _ < ) < | No | 8.5 |
| 8 | <)(_\<\/\ | < ) ( _ \ < / / \ | No | 3.55 |
| 9 | (()\<)  < | (( ) \ < ) [ ] < | No | 6.96 |
| 10 | \)//  /<) | \ ) / / ␣ ␣ / < ) | No | 7.22 |
| 11 | _ \/__(_( | _␣\/__(_( | Yes | 6.59 |
| 12 | /\\/_(\(/ | /\ \ / _ ( / ) ( | No | 9.26 |
| 13 | \_ )< ((< | \ _ ␣ ) < ␣ ( ( < | No | 6.78 |
| 14 |  )\<</(\  | ) \ < < / ( \ | No | 7.81 |
| 15 | _\) _\(() | _/)<_ \(( ) | No | 6.06 |
| 16 | \\)\<< () | /\)\<\<␣() | No | 7.7 |
| 17 | \ \))\/() | \ ␣ \ ) ) \ / ( ( ) | No | 6.31 |
| 18 | \<) __/_  | /<)___/__ | No | 7.18 |
| 19 | \ _/ )(\< | \ ␣ _ / ␣ ) ( \ < | No | 6.33 |
| 20 | <\( (_\ ( | <\(_\(_< | No | 6.91 |
