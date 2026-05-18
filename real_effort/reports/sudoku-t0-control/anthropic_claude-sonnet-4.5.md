# Benchmark Report — claude-sonnet-4.5

- **Model**: `anthropic/claude-sonnet-4.5`
- **Date**: 2026-05-18 11:55:34

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **sudoku_game**: difficulty=0.4

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| sudoku_game | 8060 | 31879 | 39939 | 11 | 9 | 23.33 | 466.78 |
| **TOTAL** | **8060** | **31879** | **39939** | | | | |

## sudoku_game

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 5 4 3 3 4 3 1 5 4 6 1 3 2 6 | 5 4 3 3 4 3 1 5 4 6 1 3 2 6 | Yes | 25.6 |
| 2 | 2 5 4 6 5 2 6 5 5 1 4 3 2 5 | 2 5 4 6 5 2 6 5 5 1 4 3 2 5 | Yes | 29.76 |
| 3 | 4 1 5 6 2 3 4 6 6 1 4 2 1 6 | 4 1 3 6 5 2 3 4 6 6 1 4 2 6 1 | No | 20.03 |
| 4 | 1 4 2 4 5 4 2 6 6 2 6 5 2 3 | 1 4 2 4 5 4 6 2 6 2 6 5 2 3 | No | 22.04 |
| 5 | 1 6 6 5 4 1 6 5 4 1 4 5 6 1 | Looking at this 6×6 Sudoku, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with the easier cells: - Row 3: Has 4,2,3,5,1 → missing 6 at position (3,1) - Column 1: Has 4,2,_,3,_,5 → with (3,1)=6, only missing 1 at position (5,1) - Column 6: Has 2,3,1,6,_,4 → missing 5 at position (5,6) - Row 5: Now has 1,3,_,6,2,5 → missing 4 at position (5,3)  For Row 6: Has 5,2,_,_,3,4 → missing 1,6 - Column 3: Has 3,_,2,1,4,_ → missing 5,6 - Position (6,3) must be 6 (from row needs) - Position (6,4) must be 1  For Row 4: Has 3, | No | 31.87 |
| 6 | 2 3 4 6 3 5 4 1 6 4 2 1 3 4 | 2 3 4 6 3 5 4 1 6 4 2 1 3 4 | Yes | 19.47 |
| 7 | 2 4 5 1 5 3 2 5 4 3 6 4 2 3 | 2 4 5 1 5 3 2 5 4 3 6 4 2 3 | Yes | 25.31 |
| 8 | 5 4 2 6 2 6 2 3 4 2 3 1 5 4 | 5 4 2 6 2 6 2 3 4 2 3 1 5 4 | Yes | 18.64 |
| 9 | 2 5 1 6 2 3 5 2 1 6 2 3 2 1 | 2 5 1 6 2 3 5 2 1 6 2 3 2 1 | Yes | 23.1 |
| 10 | 1 5 5 3 1 3 5 4 6 3 6 2 6 1 | 5 1 5 3 1 3 5 4 6 3 6 2 6 1 | No | 18.37 |
| 11 | 4 4 3 5 6 5 6 2 2 4 6 6 2 4 | 4 4 3 5 6 5 6 2 2 4 6 6 2 4 | Yes | 20.78 |
| 12 | 1 6 3 1 1 6 6 3 5 4 6 2 3 2 | 1 6 3 1 1 6 6 3 5 4 6 2 3 2 | Yes | 18.6 |
| 13 | 4 3 5 6 2 1 5 6 4 6 4 2 5 6 | 4 3 5 6 2 1 5 6 4 6 4 2 5 6 | Yes | 27.8 |
| 14 | 6 5 3 4 6 6 5 5 2 6 6 6 3 2 | 6 5 3 4 6 6 5 6 2 5 6 6 3 2 | No | 22.33 |
| 15 | 1 3 5 6 6 3 1 4 6 3 1 2 5 6 | 3 1 5 6 6 1 3 4 6 3 1 2 5 6 | No | 18.75 |
| 16 | 4 3 3 5 4 5 4 3 2 6 2 5 4 4 | Looking at the 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with what's given: - Row 1: _, 2, 6, 5, 1, _ - Row 2: _, 1, _, _, 6, 2 - Row 3: _, _, 1, _, _, _ - Row 4: _, 6, 3, 1, 4, _ - Row 5: 1, 5, 2, 6, 3, _ - Row 6: 6, 3, _, 2, 5, 1  Solving step by step:  **Row 5**: Missing only position 6 → needs 4 **Row 6**: Position 3 needs 4 (only number missing in column 3 besides 5)  **Row 1**: Needs 3 and 4 - Position 1: Must be 4 (checking box constraints) - Position 6: Must be 3  **Row 4**: Needs 2 and 5 - Position 1: Must be 2 - Position 6: Must be 5  **Row 2**: | No | 30.61 |
| 17 | 1 6 4 3 6 1 5 6 1 3 5 4 1 6 | 6 1 4 3 6 1 5 1 4 3 6 5 1 6 4 | No | 22.1 |
| 18 | 4 6 2 1 6 4 6 4 5 1 4 5 3 1 | Looking at this 6×6 Sudoku puzzle, I'll solve it systematically by analyzing rows, columns, and 2×3 boxes.  Starting with the easier cells:  **Row 2, Col 6:** Row 2 needs only 1 → **1**  **Row 3, Col 4:** Column 4 has 5,4,1,2 → needs 3,6. Row 3 needs 4,6. Checking the middle-right box confirms → **6**  **Row 3, Col 6:** Row 3 now needs only 4 → **4**  **Row 6, Col 4:** Column 4 now needs only 3 → **3**  **Row 6, Col 5:** Row 6 needs 1,3. Column 5 needs 1,2,4,5. Intersection → **1**  **Row 1, Col 5:** Top- | No | 30.14 |
| 19 | 2 5 6 4 6 1 6 3 5 1 1 3 6 6 | 2 5 6 4 6 1 6 3 5 1 1 3 6 6 | Yes | 20.87 |
| 20 | 4 1 2 3 4 2 5 6 1 3 1 6 4 2 | 4 1 2 3 4 2 5 6 1 3 1 6 4 2 | Yes | 20.41 |
