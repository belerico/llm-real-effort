# Benchmark Report — claude-opus-4.6

- **Model**: `anthropic/claude-opus-4.6`
- **Date**: 2026-03-27 10:02:58

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
| sudoku_game | 6329 | 33405 | 39734 | 10 | 10 | 26.49 | 529.86 |
| add_numbers | 3720 | 1014 | 4734 | 18 | 2 | 3.18 | 63.58 |
| counting_zeros | 5040 | 14612 | 19652 | 8 | 12 | 9.84 | 196.89 |
| task_decoding | 5040 | 2066 | 7106 | 20 | 0 | 4.86 | 97.23 |
| task_summation | 5100 | 4047 | 9147 | 20 | 0 | 5.54 | 110.8 |
| task_transcription | 3878 | 752 | 4630 | 20 | 0 | 2.84 | 56.87 |
| task_sequences | 3780 | 3723 | 7503 | 20 | 0 | 4.94 | 98.75 |
| string_entry | 4239 | 1630 | 5869 | 11 | 9 | 3.80 | 76.06 |
| **TOTAL** | **37126** | **61249** | **98375** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 5 3 6 4 4 2 6 3 1 3 5 4 |  | No | 37.87 |
| 2 | 1 4 3 5 1 6 3 4 2 4 1 5 5 2 | 1 4 3 5 1 6 3 4 2 4 1 5 5 2 | Yes | 20.47 |
| 3 | 3 1 6 4 5 6 4 2 3 4 6 4 6 6 | 3 1 6 4 5 6 4 2 3 4 6 4 6 6 | Yes | 26.09 |
| 4 | 2 3 1 5 1 1 6 4 3 4 5 5 1 4 |  | No | 33.37 |
| 5 | 6 2 1 4 5 4 6 4 5 2 5 3 2 4 | Looking at this puzzle, I need to determine the box layout. With a 6×6 grid and the dividers shown, the boxes are **3×2** (3 rows × 2 columns).  **Filling in systematically:**  **Row 3/4 (easy starts):** - R3C1: Box(R1-3,C1-2) has {1,2,3,5,6} → **4** - R4C4: Row 4 has {1,2,3, | No | 35.07 |
| 6 | 2 3 2 1 3 3 6 4 1 1 3 5 5 3 | 2 3 2 1 3 3 6 4 1 1 3 5 5 3 | Yes | 19.19 |
| 7 | 3 1 5 4 1 3 2 3 1 3 1 2 1 4 | 3 1 5 4 1 3 2 3 1 3 1 2 1 4 | Yes | 36.75 |
| 8 | 2 6 1 4 2 5 6 1 6 2 4 4 1 5 |  | No | 34.47 |
| 9 | 2 3 4 3 1 2 6 4 4 3 5 2 4 3 | 2 3 4 3 1 2 1 6 4 4 3 6 5 2 4 3 | No | 28.74 |
| 10 | 4 6 2 4 2 6 1 4 4 3 6 1 2 5 | 4 6 2 4 2 6 1 4 4 3 6 1 5 2 5 | No | 19.0 |
| 11 | 3 4 6 1 5 6 6 3 4 1 5 6 4 1 | 3 4 6 1 5 6 6 3 4 1 5 6 2 4 1 3 | No | 17.84 |
| 12 | 2 6 1 4 2 5 2 4 5 2 4 4 1 5 | 2 6 1 4 2 5 2 4 5 4 1 3 2 4 4 1 5 | No | 28.91 |
| 13 | 3 5 5 1 2 4 3 2 1 6 3 5 4 5 | 3 5 5 1 2 4 3 2 1 6 3 5 4 5 | Yes | 18.95 |
| 14 | 5 1 4 1 2 5 2 5 3 4 3 5 5 2 | 5 1 4 1 2 5 2 5 3 4 3 5 5 2 | Yes | 23.28 |
| 15 | 3 6 1 4 4 6 5 3 4 2 5 1 6 5 |  | No | 32.76 |
| 16 | 6 2 3 4 1 4 2 1 4 5 3 5 3 1 |  | No | 34.61 |
| 17 | 5 2 5 3 5 1 6 2 4 6 4 1 2 6 | 5 2 5 3 5 1 6 2 4 6 4 1 2 6 | Yes | 20.69 |
| 18 | 4 1 3 6 2 6 4 3 2 5 6 2 6 5 | 4 1 3 6 2 6 4 3 2 5 6 2 6 5 | Yes | 18.56 |
| 19 | 4 6 1 3 2 5 1 6 5 4 3 2 6 4 | 4 6 1 3 2 5 1 6 5 4 3 2 6 4 | Yes | 23.32 |
| 20 | 6 1 2 1 5 4 6 4 2 5 5 4 1 1 | 6 1 2 1 5 4 6 4 2 5 5 4 1 1 | Yes | 19.86 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1585 | 1585 | Yes | 2.42 |
| 2 | 1433 | 1433 | Yes | 5.78 |
| 3 | 2053 | 2053 | Yes | 3.26 |
| 4 | 1873 | 1873 | Yes | 2.61 |
| 5 | 1695 | 1695 | Yes | 2.87 |
| 6 | 1376 | 2752 | No | 3.42 |
| 7 | 1068 | 1068 | Yes | 2.77 |
| 8 | 1897 | 1897 | Yes | 2.73 |
| 9 | 1759 | 1759 | Yes | 2.42 |
| 10 | 1400 | 1400 | Yes | 2.63 |
| 11 | 1872 | 1872 | Yes | 6.41 |
| 12 | 2196 | 2196 | Yes | 2.73 |
| 13 | 1677 | 1677 | Yes | 3.18 |
| 14 | 1036 | 1036 | Yes | 2.64 |
| 15 | 1391 | 1391 | Yes | 2.35 |
| 16 | 1136 | 2272 | No | 5.27 |
| 17 | 1532 | 1532 | Yes | 2.67 |
| 18 | 2443 | 2443 | Yes | 2.4 |
| 19 | 1420 | 1420 | Yes | 2.59 |
| 20 | 1174 | 1174 | Yes | 2.43 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 46 | 45 | No | 6.71 |
| 2 | 61 | 60 | No | 11.85 |
| 3 | 50 | 46 | No | 7.55 |
| 4 | 75 | 75 | Yes | 6.83 |
| 5 | 70 | 62 | No | 7.37 |
| 6 | 71 | 71 | Yes | 18.35 |
| 7 | 75 | 64 | No | 8.37 |
| 8 | 61 | 59 | No | 8.15 |
| 9 | 73 | 73 | Yes | 12.88 |
| 10 | 36 | 36 | Yes | 7.62 |
| 11 | 47 | 45 | No | 9.2 |
| 12 | 64 | 54 | No | 7.53 |
| 13 | 56 | 56 | Yes | 12.83 |
| 14 | 36 | 36 | Yes | 11.98 |
| 15 | 57 | 57 | Yes | 9.58 |
| 16 | 62 | 63 | No | 20.05 |
| 17 | 64 | 64 | Yes | 9.63 |
| 18 | 47 | 42 | No | 6.1 |
| 19 | 66 | 57 | No | 6.94 |
| 20 | 52 | 46 | No | 7.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ALIBYGC | ALIBYGC | Yes | 5.98 |
| 2 | EUIFQNW | EUIFQNW | Yes | 5.72 |
| 3 | ORHGFYA | ORHGFYA | Yes | 3.66 |
| 4 | YTCIFKG | YTCIFKG | Yes | 3.69 |
| 5 | RJXKHAQ | RJXKHAQ | Yes | 4.43 |
| 6 | PSIURHE | PSIURHE | Yes | 3.28 |
| 7 | LBAFIXV | LBAFIXV | Yes | 4.35 |
| 8 | XIRJSYM | XIRJSYM | Yes | 4.74 |
| 9 | GKOLBIY | GKOLBIY | Yes | 13.5 |
| 10 | MWUKEZT | MWUKEZT | Yes | 3.67 |
| 11 | PDEIMQG | PDEIMQG | Yes | 4.68 |
| 12 | XDOVYKH | XDOVYKH | Yes | 3.82 |
| 13 | CYFODBX | CYFODBX | Yes | 4.68 |
| 14 | JFIYDTS | JFIYDTS | Yes | 3.49 |
| 15 | FUNEKZR | FUNEKZR | Yes | 3.51 |
| 16 | FQBDTZN | FQBDTZN | Yes | 5.91 |
| 17 | CVKDLYA | CVKDLYA | Yes | 6.66 |
| 18 | FWDSXOR | FWDSXOR | Yes | 4.18 |
| 19 | IHZPDFN | IHZPDFN | Yes | 4.1 |
| 20 | ORWGZMY | ORWGZMY | Yes | 3.18 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [3.5, 6.5] | 3.5 6.5 | Yes | 8.84 |
| 2 | [2.9, 7.1] | 7.1 2.9 | Yes | 4.47 |
| 3 | [4.5, 5.5] | 4.5 5.5 | Yes | 3.69 |
| 4 | [4.5, 5.5] | 5.5 4.5 | Yes | 7.06 |
| 5 | [4.1, 5.9] | 5.9 4.1 | Yes | 4.44 |
| 6 | [4.2, 5.8] | 5.8 4.2 | Yes | 5.85 |
| 7 | [2.0, 8.0] | 2.0 8.0 | Yes | 5.14 |
| 8 | [4.7, 5.3] | 4.7 5.3 | Yes | 5.92 |
| 9 | [1.4, 8.6] | 8.6 1.4 | Yes | 4.32 |
| 10 | [3.7, 6.3] | 6.3 3.7 | Yes | 5.57 |
| 11 | [3.0, 7.0] | 7.0 3.0 | Yes | 4.65 |
| 12 | [0.3, 9.7] | 9.7 0.3 | Yes | 3.45 |
| 13 | [2.0, 8.0] | 8.0 2.0 | Yes | 9.23 |
| 14 | [2.8, 7.2] | 7.2 2.8 | Yes | 5.89 |
| 15 | [2.7, 7.3] | 7.3 2.7 | Yes | 6.39 |
| 16 | [2.2, 7.8] | 7.8 2.2 | Yes | 6.94 |
| 17 | [4.2, 5.8] | 4.2 5.8 | Yes | 6.1 |
| 18 | [0.9, 9.1] | 0.9 9.1 | Yes | 4.27 |
| 19 | [3.4, 6.6] | 3.4 6.6 | Yes | 4.87 |
| 20 | [4.5, 5.5] | 5.5 4.5 | Yes | 3.71 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | NFJCKGZLKLXA | NFJCKGZLKLXA | Yes | 2.87 |
| 2 | QVQ7J9A6H7D0 | QVQ7J9A6H7D0 | Yes | 3.3 |
| 3 | F40C5A3BP7NB | F40C5A3BP7NB | Yes | 2.58 |
| 4 | XKMRKGKS2A4P | XKMRKGKS2A4P | Yes | 3.13 |
| 5 | 3MO05EJPBQLY | 3MO05EJPBQLY | Yes | 2.36 |
| 6 | O6PJ9PP461C7 | O6PJ9PP461C7 | Yes | 3.85 |
| 7 | Q4ONGVGBZJ0B | Q4ONGVGBZJ0B | Yes | 3.16 |
| 8 | H5SBJRY4DJGR | H5SBJRY4DJGR | Yes | 2.48 |
| 9 | 6V8ME23CPZHJ | 6V8ME23CPZHJ | Yes | 2.68 |
| 10 | RMJ2HHAQDDQ6 | RMJ2HHAQDDQ6 | Yes | 3.48 |
| 11 | XMQ325OL69NR | XMQ325OL69NR | Yes | 2.51 |
| 12 | 19PBLM7B1WPG | 19PBLM7B1WPG | Yes | 2.72 |
| 13 | QKUP78KBJ46T | QKUP78KBJ46T | Yes | 3.15 |
| 14 | 60KOQIVT88DH | 60KOQIVT88DH | Yes | 2.67 |
| 15 | FZ2LDL3T07SP | FZ2LDL3T07SP | Yes | 2.63 |
| 16 | R2ARCPEGLA9W | R2ARCPEGLA9W | Yes | 2.6 |
| 17 | CRA5UOZ94OND | CRA5UOZ94OND | Yes | 2.55 |
| 18 | II63THGJ0G7T | II63THGJ0G7T | Yes | 2.76 |
| 19 | WOIGOLJ8042O | WOIGOLJ8042O | Yes | 2.7 |
| 20 | MI5OC0HJ80NB | MI5OC0HJ80NB | Yes | 2.68 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 28 | 28 | Yes | 4.84 |
| 2 | 4 | 4 | Yes | 7.02 |
| 3 | 31 | 31 | Yes | 4.59 |
| 4 | 793 | 793 | Yes | 4.76 |
| 5 | 3 | 3 | Yes | 5.32 |
| 6 | 36 | 36 | Yes | 3.28 |
| 7 | 7 | 7 | Yes | 2.81 |
| 8 | 1 | 1 | Yes | 4.77 |
| 9 | 39 | 39 | Yes | 5.16 |
| 10 | 63 | 63 | Yes | 4.21 |
| 11 | 60 | 60 | Yes | 4.73 |
| 12 | 73 | 73 | Yes | 5.35 |
| 13 | 9 | 9 | Yes | 4.49 |
| 14 | 1440 | 1440 | Yes | 4.49 |
| 15 | 6 | 6 | Yes | 4.79 |
| 16 | 16 | 16 | Yes | 4.61 |
| 17 | 23 | 23 | Yes | 5.02 |
| 18 | 26 | 26 | Yes | 7.57 |
| 19 | 64 | 64 | Yes | 5.93 |
| 20 | 243 | 243 | Yes | 4.99 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _( ))<_\< | _( ))<_\ | No | 3.66 |
| 2 |  /\\((/)_ | /\\((/)_ | No | 4.61 |
| 3 | _/_/<\_/( | _/_/<\_/( | Yes | 3.06 |
| 4 | \_\\)<\<\ | \_\\)<\<\ | Yes | 3.3 |
| 5 | )<(<(/)\  | )<(<(/)\ | No | 3.97 |
| 6 | )\)< ()(\ | )\)< ()(\ | Yes | 4.71 |
| 7 | ()_  (\ ) | ()_  (\ ) | Yes | 4.03 |
| 8 | <_<<\/<\) | <_<<\/<\) | Yes | 3.36 |
| 9 | )// (\  _ | )// (\  _ | Yes | 4.47 |
| 10 | \ )(\_/(/ | \ )(\_/(/ | Yes | 3.41 |
| 11 | _()<_)<() | _()<_)<() | Yes | 4.37 |
| 12 | __<\//\_  | __<\//\_ | No | 2.75 |
| 13 | <\( _(\_< | <\( _(\_ | No | 3.1 |
| 14 | /\_)(_<)/ | /\_)(_<)/ | Yes | 3.0 |
| 15 | /_(\_ )_) | /_(\ )_) | No | 5.14 |
| 16 |   )))_)_\ | )))_)_\ | No | 4.17 |
| 17 | \()( < (\ | \()( < (\ | Yes | 3.3 |
| 18 | (<//\<\\/ | (<//\<\\/ | Yes | 4.28 |
| 19 |  )_/(//(_ | )_/(//(_ | No | 2.7 |
| 20 |  //\\/<   | //\\/< | No | 4.68 |
