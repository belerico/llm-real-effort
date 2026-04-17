# Benchmark Report — claude-haiku-4.5

- **Model**: `anthropic/claude-haiku-4.5`
- **Date**: 2026-03-19 09:50:42

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
| sudoku_game | 8060 | 29801 | 37861 | 3 | 17 | 10.67 | 213.64 |
| add_numbers | 3980 | 3067 | 7047 | 20 | 0 | 2.54 | 50.76 |
| counting_zeros | 6920 | 20405 | 27325 | 3 | 17 | 7.05 | 141.25 |
| task_decoding | 13360 | 11563 | 24923 | 18 | 2 | 5.06 | 101.41 |
| task_summation | 7280 | 18091 | 25371 | 20 | 0 | 6.48 | 129.83 |
| task_transcription | 4124 | 3567 | 7691 | 18 | 2 | 2.63 | 52.73 |
| task_sequences | 3240 | 6705 | 9945 | 19 | 1 | 2.96 | 59.22 |
| **TOTAL** | **46964** | **93199** | **140163** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 4 1 4 3 6 5 2 1 6 6 1 2 5 3 | # Solving the 6×6 Sudoku  Let me work through this systematically:  **Row 1:** 5 3 6 \| _ 1 2 → Missing 4 → **4**  **Row 2:** _ 6 2 \| 3 4 5 → Missing 1 → **1**  **Row 3:** 2 _ 1 \| 5 _ _ - Col 2: Already has 3,6,2 → need 1,4,5. Row 3 has 2,1,5 → need 3,4,6. Box has 2,1,4,3 → need 5,6. So → **4** - Col 5: Row 3 needs 3,6; Col 5 has 1,4 → needs 2,3,5,6; Box needs 1,2,3,4 → **3** - Col 6: Row 3 needs 6; Col 6 has 2,5,4 → needs 1,3,6 → **6**  **Row 4:** 4 _ 3 \| 6 _ _ - Col 2: Row 4 needs 1,2,5,6; Col 2 has 3,6,4,2 → needs 1,5; → **5** - Col 5: Row 4 needs 1,2,5; Col 5 has 1,4,3,6 → needs 2,5; → **2** | No | 14.26 |
| 2 | 4 2 2 5 3 2 5 6 6 4 1 1 5 3 | 4 2 2 5 3 2 5 6 6 4 1 1 5 3 | Yes | 10.46 |
| 3 | 5 4 1 1 2 5 4 6 3 1 6 6 4 1 | 4 5 1 2 5 1 2 6 4 3 1 6 4 1 6 | No | 10.98 |
| 4 | 6 4 1 6 1 5 6 5 1 6 2 4 3 2 | 1 4 6 6 1 5 6 5 1 3 6 2 4 3 | No | 8.83 |
| 5 | 6 5 4 1 2 4 5 2 6 5 4 1 3 4 | 6 5 4 2 4 5 2 6 5 4 1 3 4 | No | 9.66 |
| 6 | 3 2 6 3 5 2 1 2 5 4 6 2 5 1 | 3 2 6 5 2 1 4 6 2 5 4 2 1 5 1 | No | 8.44 |
| 7 | 2 1 6 1 5 3 1 6 2 5 5 2 6 4 | 2 1 1 6 5 3 1 6 2 5 5 2 6 4** | No | 9.89 |
| 8 | 5 4 6 1 2 6 3 2 6 1 6 4 6 1 | 5 4 6 1 2 6 3 2 6 1 6 4 6 1 | Yes | 9.49 |
| 9 | 4 1 6 2 3 1 6 4 5 3 2 5 1 1 | 4 1 5 2 6 1 3 4 1 5 1 | No | 12.18 |
| 10 | 2 4 6 3 5 2 5 4 3 1 2 6 4 1 | 2 3 4 6 5 2 5 4 1 3 2 6 1 4 | No | 9.35 |
| 11 | 4 1 3 5 2 5 4 5 4 5 3 4 5 4 | 4 1 5 3 2 4 5 4 5 4 3 5 | No | 11.58 |
| 12 | 3 2 6 5 4 2 5 6 1 2 6 3 6 3 | 3 2 4 5 6 2 5 1 6 2 3 6 6 3 | No | 10.87 |
| 13 | 2 5 5 5 6 4 5 1 1 6 2 3 2 5 | 2 5 5 5 6 1 4 5 2 6 3 1 4 5 | No | 12.33 |
| 14 | 3 6 4 1 1 5 3 5 1 6 4 2 4 5 | 3 6 4 3 1 5 6 5 4 2 4 | No | 11.05 |
| 15 | 6 3 4 1 2 4 1 6 5 6 4 4 3 5 | 6 3 4 1 2 4 6 1 4 4 3 5 | No | 11.08 |
| 16 | 2 1 4 1 5 3 1 6 4 6 5 2 1 4 | 2 4 1 1 5 3 1 6 1 6 4 2 1 4 | No | 10.2 |
| 17 | 6 1 5 4 6 3 3 1 4 2 6 4 2 6 | 6 1 5 4 6 3 2 1 4 3 6 4 2 6** | No | 10.14 |
| 18 | 1 2 6 6 1 3 2 6 1 4 2 6 3 1 | 1 2 6 6 1 3 2 6 5 1 2 4 6 3 1** | No | 10.57 |
| 19 | 1 2 5 6 1 4 3 1 3 4 1 3 4 2 | 1 2 5 6 1 4 3 1 3 4 1 3 4 2 | Yes | 8.9 |
| 20 | 4 3 5 1 4 5 2 4 5 3 1 6 1 6 | # 6×6 Sudoku Solution  Let me solve this step by step using logical deduction.  **Analyzing the given grid:**  Row 1: 5 2 6 \| 1 4 3 ✓ (complete) Row 2: _ 1 _ \| _ 6 2 Row 3: 3 6 4 \| 2 5 1 ✓ (complete) Row 4: 6 3 _ \| _ 2 _ Row 5: _ _ _ \| _ _ _ Row 6: _ 5 2 \| _ 3 4  **Solving by boxes and constraints:**  **Row 2:** Missing 3, 4, 5 - Box 1 needs 3, 4 → (2,1)=4, (2,3)=3 - Row 2 col 4: (2,4)=5  **Row 4:** Missing 1, 4, 5 - Box 3 needs 1, | No | 13.22 |

## add_numbers

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 2104 | 2104 | Yes | 1.96 |
| 2 | 1498 | 1498 | Yes | 2.11 |
| 3 | 2207 | 2207 | Yes | 2.96 |
| 4 | 1192 | 1192 | Yes | 1.92 |
| 5 | 984 | 984 | Yes | 1.87 |
| 6 | 1096 | 1096 | Yes | 2.36 |
| 7 | 1981 | 1981 | Yes | 3.23 |
| 8 | 1418 | 1418 | Yes | 2.98 |
| 9 | 1406 | 1406 | Yes | 1.99 |
| 10 | 1661 | 1661 | Yes | 3.47 |
| 11 | 1919 | 1919 | Yes | 2.12 |
| 12 | 1311 | 1311 | Yes | 1.96 |
| 13 | 2196 | 2196 | Yes | 2.17 |
| 14 | 1194 | 1194 | Yes | 2.25 |
| 15 | 1347 | 1347 | Yes | 2.08 |
| 16 | 2330 | 2330 | Yes | 2.85 |
| 17 | 1585 | 1585 | Yes | 2.81 |
| 18 | 1373 | 1373 | Yes | 2.69 |
| 19 | 2143 | 2143 | Yes | 4.04 |
| 20 | 1852 | 1852 | Yes | 2.88 |

## counting_zeros

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 59 | 56 | No | 6.55 |
| 2 | 39 | 39 | Yes | 7.36 |
| 3 | 51 | 51 | Yes | 7.92 |
| 4 | 66 | 62 | No | 5.65 |
| 5 | 41 | 47 | No | 7.41 |
| 6 | 74 | 73 | No | 6.49 |
| 7 | 52 | 47 | No | 7.28 |
| 8 | 38 | 38 | Yes | 7.47 |
| 9 | 61 | 52 | No | 6.91 |
| 10 | 40 | 45 | No | 6.33 |
| 11 | 36 | 38 | No | 5.04 |
| 12 | 36 | 35 | No | 7.65 |
| 13 | 37 | 40 | No | 7.57 |
| 14 | 75 | 67** | No | 8.27 |
| 15 | 53 | 51 | No | 7.96 |
| 16 | 69 | 60 | No | 6.2 |
| 17 | 62 | 55 | No | 8.39 |
| 18 | 50 | 49 | No | 7.1 |
| 19 | 52 | 48 | No | 7.05 |
| 20 | 49 | 42 | No | 6.36 |

## task_decoding

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | OWIZCDQ | OWIZCDQ | Yes | 4.62 |
| 2 | HXSWKFB | HXSWKFB | Yes | 5.1 |
| 3 | HZKJDWR | HZKJDWR | Yes | 4.8 |
| 4 | YTNDABK | YTNDABK | Yes | 3.66 |
| 5 | LJIPMTD | LJIPMATD | No | 6.24 |
| 6 | MXAJTUO | MXAJTUO | Yes | 5.21 |
| 7 | MUNWXVB | MUNWXVB | Yes | 4.88 |
| 8 | JKTFDPV | JKTFDPV | Yes | 6.88 |
| 9 | HRSQTLK | HRSQTLK | Yes | 5.66 |
| 10 | TQOWZMK | TQOWZMK | Yes | 4.86 |
| 11 | EJSXKUB | EJSXKUB | Yes | 3.47 |
| 12 | VEWFJUK | VEWFJUK | Yes | 6.31 |
| 13 | YWVMJPI | YWVMJPI | Yes | 5.3 |
| 14 | DVEQMJN | DVEQMJN | Yes | 5.41 |
| 15 | WVPATRG | WVPATRG | Yes | 4.44 |
| 16 | JBMGHVC | JBMGHVC | Yes | 4.29 |
| 17 | HIXYBCF | HIXYBCF | Yes | 4.32 |
| 18 | NGIHVRS | NGHVRS | No | 4.88 |
| 19 | PVRIWCN | PVRIWCN | Yes | 6.64 |
| 20 | JYCPMNI | JYCPMNI | Yes | 4.22 |

## task_summation

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | [0.7, 9.3] | 9.3 0.7 | Yes | 5.61 |
| 2 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.14 |
| 3 | [3.2, 6.8] | 3.2 6.8 | Yes | 5.71 |
| 4 | [3.6, 6.4] | 6.4 3.6 | Yes | 5.47 |
| 5 | [1.6, 8.4] | 8.4 1.6 | Yes | 6.49 |
| 6 | [1.8, 8.2] | 1.8 8.2 | Yes | 5.55 |
| 7 | [4.3, 5.7] | 4.3 5.7 | Yes | 8.66 |
| 8 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.52 |
| 9 | [0.3, 9.7] | 9.7 0.3 | Yes | 7.31 |
| 10 | [1.0, 9.0] | 1.0 9.0 | Yes | 6.13 |
| 11 | [2.8, 7.2] | 7.2 2.8 | Yes | 6.17 |
| 12 | [2.8, 7.2] | 2.8 7.2 | Yes | 8.49 |
| 13 | [2.7, 7.3] | 2.7 7.3 | Yes | 6.19 |
| 14 | [3.8, 6.2] | 6.2 3.8 | Yes | 6.33 |
| 15 | [0.5, 9.5] | 9.5 0.5 | Yes | 8.54 |
| 16 | [3.2, 6.8] | 3.2 6.8 | Yes | 5.6 |
| 17 | [3.2, 6.8] | 3.2 6.8 | Yes | 6.13 |
| 18 | [0.4, 9.6] | 0.4 9.6 | Yes | 5.89 |
| 19 | [0.3, 9.7] | 0.3 9.7 | Yes | 6.02 |
| 20 | [1.8, 8.2] | 1.8 8.2 | Yes | 7.67 |

## task_transcription

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 6IZ8F4HN5V9C | 6IZ3F4HN5V9C | No | 2.11 |
| 2 | O43NDP9D7L89 | O43NDP9D7L89 | Yes | 2.33 |
| 3 | 6X4V73KA9NJ1 | 6X4V73KA9NJ1 | Yes | 2.12 |
| 4 | WSEMELHAOH8K | WSEMELHAOH8K | Yes | 2.88 |
| 5 | GL4A7S63LYQD | GL4A7S63LYQD | Yes | 2.24 |
| 6 | 6XALZ5WDJVJJ | 6XALZ5WDJVJJ | Yes | 3.27 |
| 7 | 9FWWQ6ZGU4AX | 9FWWQ6ZGUAAX | No | 6.87 |
| 8 | C0ZXD1V2NKSP | C0ZXD1V2NKSP | Yes | 2.5 |
| 9 | VJ00M5FR8N03 | VJ00M5FR8N03 | Yes | 2.2 |
| 10 | HIHHXGDVJW8S | HIHHXGDVJW8S | Yes | 2.03 |
| 11 | 4VN169KEQKUJ | 4VN169KEQKUJ | Yes | 2.28 |
| 12 | 9U9CC8B97Y18 | 9U9CC8B97Y18 | Yes | 2.83 |
| 13 | IBF78V8Z23DC | IBF78V8Z23DC | Yes | 2.62 |
| 14 | 9CP6OA2RH7AM | 9CP6OA2RH7AM | Yes | 2.6 |
| 15 | EIP6W7WQX6L3 | EIP6W7WQX6L3 | Yes | 2.27 |
| 16 | 5SNWT6U860ZX | 5SNWT6U860ZX | Yes | 2.52 |
| 17 | N5FSY7U51M8W | N5FSY7U51M8W | Yes | 1.89 |
| 18 | EW300LPBEUON | EW300LPBEUON | Yes | 2.72 |
| 19 | TGBY99LP859S | TGBY99LP859S | Yes | 2.01 |
| 20 | INXF3DUAQFQ1 | INXF3DUAQFQ1 | Yes | 2.33 |

## task_sequences

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 23 | 23 | Yes | 2.39 |
| 2 | 198 | 198 | Yes | 2.71 |
| 3 | 3 | 3 | Yes | 2.59 |
| 4 | 243 | 243 | Yes | 1.87 |
| 5 | 10 | 10 | Yes | 2.84 |
| 6 | 9 | 9 | Yes | 2.8 |
| 7 | 5 | 5 | Yes | 2.62 |
| 8 | 5 | 58 | No | 8.09 |
| 9 | 64 | 64 | Yes | 2.41 |
| 10 | 7680 | 7680 | Yes | 2.71 |
| 11 | 9 | 9 | Yes | 2.72 |
| 12 | 20 | 20 | Yes | 3.51 |
| 13 | 44 | 44 | Yes | 4.55 |
| 14 | 19 | 19 | Yes | 2.07 |
| 15 | 73 | 73 | Yes | 2.34 |
| 16 | 36 | 36 | Yes | 2.05 |
| 17 | 4 | 4 | Yes | 2.77 |
| 18 | 1440 | 1440 | Yes | 2.67 |
| 19 | 60 | 60 | Yes | 3.23 |
| 20 | 28 | 28 | Yes | 2.28 |
