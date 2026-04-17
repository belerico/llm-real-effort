# Benchmark Report — gemini-2.5-flash-lite

- **Model**: `google/gemini-2.5-flash-lite`
- **Date**: 2026-03-27 09:51:29

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
| sudoku_game | 5523 | 30835 | 36358 | 0 | 20 | 5.74 | 114.75 |
| add_numbers | 3380 | 5632 | 9012 | 20 | 0 | 2.12 | 42.4 |
| counting_zeros | 6118 | 24412 | 30530 | 4 | 16 | 4.99 | 99.85 |
| task_decoding | 4660 | 3964 | 8624 | 17 | 3 | 2.00 | 40.09 |
| task_summation | 4700 | 23098 | 27798 | 20 | 0 | 3.96 | 79.32 |
| task_transcription | 3371 | 1683 | 5054 | 20 | 0 | 1.60 | 32.02 |
| task_sequences | 3345 | 11841 | 15186 | 18 | 2 | 3.26 | 65.23 |
| string_entry | 3675 | 4864 | 8539 | 8 | 12 | 2.09 | 41.89 |
| **TOTAL** | **34772** | **106329** | **141101** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 5 1 3 2 3 5 2 3 6 1 6 2 3 | 4 5 3 1 2 6 3 2 5 2 1 3 4 6 5 1 5 4 2 3 6 1 4 2 1 6 3 5 4 2 5 4 1 3 6 | No | 8.87 |
| 2 | 1 1 6 4 5 4 3 2 3 4 4 6 3 5 | 1 4 5 3 6 2 6 5 4 2 3 1 3 1 6 4 2 5 2 3 1 5 6 4 4 6 5 1 2 3 | No | 6.38 |
| 3 | 3 3 2 5 4 4 6 2 5 1 4 5 4 1 | 3 4 5 2 1 6 4 5 2 1 3 6 1 4 5 3 2 6 | No | 5.41 |
| 4 | 4 1 6 4 6 2 4 5 3 3 2 3 4 6 | 4 1 6 2 3 5 | No | 4.77 |
| 5 | 1 5 3 4 6 3 5 4 2 5 1 4 1 3 | 5 1 4 3 6 2 3 5 4 6 1 2 6 2 3 5 4 1 4 6 1 2 3 5 1 3 2 4 5 6 5 4 6 1 2 3 | No | 4.96 |
| 6 | 5 6 4 6 5 3 5 4 6 2 4 3 1 4 | 5 6 4 1 2 3 4 5 6 1 2 3 1 2 4 | No | 5.29 |
| 7 | 3 1 4 3 2 6 5 2 1 3 1 3 5 2 | 3 4 5 2 1 6 2 3 1 6 4 5 5 6 2 3 1 4 4 5 1 6 3 2 | No | 6.71 |
| 8 | 3 6 1 3 5 6 1 6 2 6 1 2 5 4 | 6 1 3 5 2 4 | No | 5.08 |
| 9 | 4 3 6 3 2 3 5 5 4 6 5 1 4 6 | 4 3 6 2 5 1 3 2 4 1 6 5 1 5 3 4 2 6 5 6 2 3 1 4 | No | 4.77 |
| 10 | 2 1 4 6 1 5 4 2 6 4 2 1 2 4 | 6 4 2 5 2 4 5 6 1 2 4 5 6 2 1 2 4 | No | 5.89 |
| 11 | 4 6 1 1 3 2 4 6 3 1 1 5 2 4 | 1 4 6 3 1 4 2 3 5 6 1 4 3 1 2 5 | No | 7.17 |
| 12 | 5 3 5 1 5 2 2 3 1 4 5 3 1 6 | 5 3 4 1 5 6 2 1 2 3 5 1 4 6 5 3 1 2 | No | 5.77 |
| 13 | 2 6 1 5 3 4 5 5 2 1 4 2 1 6 | 2 6 4 1 5 3 1 5 3 2 6 4 6 4 5 3 1 2 3 2 1 4 5 6 5 3 6 1 2 4 4 1 2 6 3 5 | No | 4.79 |
| 14 | 4 1 2 2 2 5 3 4 2 5 3 5 2 4 | 2 4 1 5 6 3 5 2 6 3 4 1 4 5 3 2 1 6 1 3 2 5 6 4 | No | 5.13 |
| 15 | 4 5 3 5 2 1 5 1 4 4 5 1 6 2 | 4 5 3 1 2 6 5 2 4 6 1 3 1 6 5 2 4 3 6 4 1 5 3 2 3 1 2 4 6 5 2 3 6 1 5 4 | No | 4.33 |
| 16 | 1 5 6 1 3 5 1 2 1 4 6 4 4 6 | I am sorry, but the Sudoku puzzle you provided is invalid. The number 3 appears twice in the top-left 2x3 box (cells R3C3 and R4C2). A valid Sudoku puzzle must have each number from 1 to 6 appear exactly once in each row, column, and 2x3 box.  Therefore, I cannot provide a solution. | No | 5.66 |
| 17 | 1 5 3 4 4 2 5 4 1 2 5 5 1 3 | 1 3 4 5 6 2 5 4 3 6 1 2 2 6 5 4 3 1 1 5 3 2 6 4 4 1 2 6 5 3 | No | 7.64 |
| 18 | 1 2 1 3 5 5 2 4 6 4 3 5 2 4 | 2 1 4 5 6 3 5 3 1 2 4 6 1 4 5 3 2 6 6 2 3 1 5 4 4 5 6 2 1 3 | No | 4.52 |
| 19 | 4 6 2 4 6 2 1 4 3 4 2 2 6 4 | 4 6 2 1 5 3 2 4 6 1 3 5 5 1 4 3 2 6 6 2 3 5 1 4 3 5 1 4 6 2 | No | 6.61 |
| 20 | 1 4 5 4 1 6 5 2 6 5 4 1 3 4 | 5 4 1 6 3 2 1 5 6 4 2 3 2 6 5 3 1 4 3 1 4 5 6 2 6 3 2 1 4 5 4 2 1 6 3 5 | No | 4.95 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 1075 | 1075 | Yes | 2.37 |
| 2 | 2012 | 2012 | Yes | 1.99 |
| 3 | 852 | 852 | Yes | 3.02 |
| 4 | 816 | 816 | Yes | 1.75 |
| 5 | 2015 | 2015 | Yes | 2.39 |
| 6 | 2144 | 2144 | Yes | 2.29 |
| 7 | 1345 | 1345 | Yes | 1.8 |
| 8 | 1546 | 1546 | Yes | 1.75 |
| 9 | 2274 | 2274 | Yes | 1.83 |
| 10 | 1256 | 1256 | Yes | 1.45 |
| 11 | 1785 | 1785 | Yes | 1.74 |
| 12 | 2241 | 2241 | Yes | 3.84 |
| 13 | 2422 | 2422 | Yes | 2.32 |
| 14 | 1780 | 1780 | Yes | 1.74 |
| 15 | 1793 | 1793 | Yes | 1.72 |
| 16 | 917 | 917 | Yes | 1.72 |
| 17 | 2304 | 2304 | Yes | 1.55 |
| 18 | 1640 | 1640 | Yes | 2.65 |
| 19 | 2168 | 2168 | Yes | 1.95 |
| 20 | 2157 | 2157 | Yes | 2.52 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 48 | 50 | No | 4.96 |
| 2 | 46 | 46 | Yes | 4.91 |
| 3 | 47 | 44 | No | 2.67 |
| 4 | 49 | 48 | No | 4.32 |
| 5 | 72 | 74 | No | 5.42 |
| 6 | 42 | 42 | Yes | 5.22 |
| 7 | 48 | 56 | No | 6.88 |
| 8 | 49 | 48 | No | 7.25 |
| 9 | 35 | 34 | No | 4.97 |
| 10 | 71 | 73 | No | 4.6 |
| 11 | 48 | 48 | Yes | 4.91 |
| 12 | 45 |  | No | 5.19 |
| 13 | 45 | 40 | No | 2.66 |
| 14 | 74 | 73 | No | 4.38 |
| 15 | 62 | 61 | No | 3.67 |
| 16 | 67 | 63 | No | 3.8 |
| 17 | 36 | 35 | No | 8.89 |
| 18 | 58 | 56 | No | 5.37 |
| 19 | 63 | 61 | No | 4.8 |
| 20 | 49 | 49 | Yes | 4.95 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | MPLISGV | MPLISGV | Yes | 2.4 |
| 2 | AGPSJLV | AGPSJLV | Yes | 1.53 |
| 3 | NJYHEOT | NJYHEOT | Yes | 1.97 |
| 4 | ANELMUC | ANELMUC | Yes | 1.79 |
| 5 | SCMRYQJ | SCMRYQJ | Yes | 2.2 |
| 6 | FVOPTZN | FVOPTZN | Yes | 2.3 |
| 7 | XOKHUVP | XOKHUP | No | 1.58 |
| 8 | JUSQONE | JUSQONE | Yes | 1.67 |
| 9 | GLVAOWY | GLVAOWY | Yes | 1.58 |
| 10 | QEAXJDK | QEAXJDK | Yes | 1.77 |
| 11 | BNMEGHA | BNMEGHA | Yes | 2.19 |
| 12 | TNCXSVE | TNCXSVE | Yes | 1.76 |
| 13 | YGQEBSM | YGQEBSM | Yes | 1.63 |
| 14 | ORXFGML | ORXGFML | No | 2.44 |
| 15 | WDRPEIL | WDRPEIL | Yes | 1.95 |
| 16 | WCZVINQ | WCZVINQ | Yes | 1.81 |
| 17 | SADBTKC | SADBTKC | Yes | 1.61 |
| 18 | ATCZIQG | ATCZIG | No | 3.02 |
| 19 | WJNSPMB | WJNSPMB | Yes | 2.19 |
| 20 | BFNXETS | BFNXETS | Yes | 2.69 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [1.3, 8.7] | 1.3 8.7 | Yes | 7.54 |
| 2 | [2.8, 7.2] | 7.2 2.8 | Yes | 4.4 |
| 3 | [1.1, 8.9] | 8.9 1.1 | Yes | 2.97 |
| 4 | [2.1, 7.9] | 2.1 7.9 | Yes | 5.02 |
| 5 | [4.7, 5.3] | 5.3 4.7 | Yes | 3.65 |
| 6 | [3.0, 7.0] | 7.0 3.0 | Yes | 3.31 |
| 7 | [3.2, 6.8] | 3.2 6.8 | Yes | 4.57 |
| 8 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.31 |
| 9 | [1.3, 8.7] | 8.7 1.3 | Yes | 3.97 |
| 10 | [2.4, 7.6] | 7.6 2.4 | Yes | 2.61 |
| 11 | [2.0, 8.0] | 2.0 8.0 | Yes | 4.35 |
| 12 | [0.9, 9.1] | 0.9 9.1 | Yes | 2.24 |
| 13 | [3.5, 6.5] | 6.5 3.5 | Yes | 4.53 |
| 14 | [2.7, 7.3] | 2.7 7.3 | Yes | 3.36 |
| 15 | [2.3, 7.7] | 7.7 2.3 | Yes | 3.59 |
| 16 | [3.6, 6.4] | 3.6 6.4 | Yes | 3.88 |
| 17 | [1.5, 8.5] | 8.5 1.5 | Yes | 4.37 |
| 18 | [4.0, 6.0] | 4.0 6.0 | Yes | 4.34 |
| 19 | [2.0, 8.0] | 2.0 8.0 | Yes | 3.21 |
| 20 | [4.2, 5.8] | 5.8 4.2 | Yes | 3.08 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2KHYUM5T3TIK | 2KHYUM5T3TIK | Yes | 2.23 |
| 2 | 13VKB9VDI508 | 13VKB9VDI508 | Yes | 1.24 |
| 3 | BWZTO4FG6GQL | BWZTO4FG6GQL | Yes | 1.37 |
| 4 | XARK5PP6KVPB | XARK5PP6KVPB | Yes | 1.38 |
| 5 | ZV0MSDXETYN1 | ZV0MSDXETYN1 | Yes | 1.25 |
| 6 | 02PV1MAYBHI1 | 02PV1MAYBHI1 | Yes | 1.71 |
| 7 | 90Q4ECWOW4UH | 90Q4ECWOW4UH | Yes | 1.77 |
| 8 | 3QBGRR28PQ4O | 3QBGRR28PQ4O | Yes | 1.69 |
| 9 | G048ME2V10DI | G048ME2V10DI | Yes | 1.87 |
| 10 | KMWMLOV2LTXZ | KMWMLOV2LTXZ | Yes | 1.32 |
| 11 | BQP5X3Y0VT0D | BQP5X3Y0VT0D | Yes | 1.47 |
| 12 | XXYJQ9GQZAQT | XXYJQ9GQZAQT | Yes | 1.42 |
| 13 | C3JJF57P8M2Z | C3JJF57P8M2Z | Yes | 1.88 |
| 14 | MOJTXB6GPJJ7 | MOJTXB6GPJJ7 | Yes | 1.98 |
| 15 | REYVFMK5HV9F | REYVFMK5HV9F | Yes | 1.2 |
| 16 | 49Y04TKB9CTV | 49Y04TKB9CTV | Yes | 1.56 |
| 17 | 5KH8P8Q6Z2X9 | 5KH8P8Q6Z2X9 | Yes | 1.94 |
| 18 | MZBKZITP03IH | MZBKZITP03IH | Yes | 1.43 |
| 19 | ANSL657A2YZX | ANSL657A2YZX | Yes | 1.42 |
| 20 | LER3UETKSIQH | LER3UETKSIQH | Yes | 1.9 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 2.36 |
| 2 | 3 | 3 | Yes | 6.63 |
| 3 | 5 | 5 | Yes | 2.13 |
| 4 | 36 | 36 | Yes | 1.57 |
| 5 | 26 | 26 | Yes | 9.37 |
| 6 | 6 | 6 | Yes | 2.24 |
| 7 | 16 | 16 | Yes | 1.75 |
| 8 | 73 | 73 | Yes | 1.85 |
| 9 | 3 | 3 | Yes | 3.46 |
| 10 | 9 |  | No | 7.62 |
| 11 | 4096 | 65536 | No | 4.91 |
| 12 | 10 | 10 | Yes | 2.32 |
| 13 | 1 | 1 | Yes | 5.64 |
| 14 | 48 | 48 | Yes | 1.76 |
| 15 | 243 | 243 | Yes | 2.15 |
| 16 | 60 | 60 | Yes | 2.24 |
| 17 | 64 | 64 | Yes | 1.81 |
| 18 | 19 | 19 | Yes | 1.69 |
| 19 | 4 | 4 | Yes | 2.04 |
| 20 | 60 | 60 | Yes | 1.69 |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <(__<_<_( | <(__<_<_( | Yes | 1.76 |
| 2 | <\(/()\\  | <\(/()\ \ | No | 1.97 |
| 3 | <(_ _( )/ | <(_ _(/ | No | 2.17 |
| 4 | /)_(/_)<_ | /)_(/_)<_ | Yes | 1.92 |
| 5 | ///  _ \  | ///  _ \ | No | 1.8 |
| 6 | \<<_/<\\) | \<<_/<\\) | Yes | 2.47 |
| 7 | / ))_)((/ | / )))_)((/ | No | 3.21 |
| 8 | _<</( <_/ | _<</ ( <_/ | No | 1.73 |
| 9 | ) </<\ () | )</< () | No | 1.8 |
| 10 | _(<\\\<<_ | _(<\\\<<_ | Yes | 1.85 |
| 11 | )/)/\<) / | )/)/\<) / | Yes | 2.14 |
| 12 |  __/ < (_ | __/ < (_ | No | 1.73 |
| 13 | )\(_/<<\< | )(_/<<\< | No | 2.04 |
| 14 | _<_ <  \  | _< < \ | No | 1.83 |
| 15 | /\_)\(_<\ | /\_)\(_< | No | 2.0 |
| 16 | )((_<\__( | )((_<\__( | Yes | 1.58 |
| 17 | (/_/_)()_ | (/_/_)()_ | Yes | 2.03 |
| 18 | _(_<\_)\_ | _(_<\_)\_ | Yes | 2.03 |
| 19 |  (_)( )__ | ( _ ) ( ) _ _ | No | 4.04 |
| 20 | (/ )/_ <) | ([ ])/_[ ])<) | No | 1.79 |
