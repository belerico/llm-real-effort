# Benchmark Report — gemini-3-flash-preview

- **Model**: `google/gemini-3-flash-preview`
- **Date**: 2026-04-01 19:56:17

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **slider_puzzle**: size=3, num_shuffles=25

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| slider_puzzle | 1294 | 2044 | 3338 | 0 | 1 | 12.98 | 12.99 |
| **TOTAL** | **1294** | **2044** | **3338** | | | | |

## slider_puzzle

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 7 4 8 1 5 7 4 6 3 4 7 5 1 7 4 3 6 8 7 4 5 2 3 6 | To solve the sliding tile puzzle, we need to arrange the tiles in the order 1-2-3, 4-5-6, 7-8 with the empty space at the bottom-right.  **Initial State:** 1 5 2 8 3 _ 4 7 6  **Step-by-step solution:** 1. Move **2** down into the empty space. (State: 1 5 _, 8 3 2, 4 7 6) 2. Move **5** right. (State: 1 _ 5, 8 3 2, 4 7 6) 3. Move **3** up. (State: 1 3 5, 8 _ 2, 4 7 6) 4. Move **2** left. (State: 1 3 5, 8 2 _, 4 7 6) 5. Move **5** down. (State: 1 3 _, 8 2 5, 4 7 6) 6. Move **3** right. (State: 1 _ 3, 8 2 5, 4 7 6) 7. Move **2** up. (State: 1 2 3, 8 _ 5, 4 7 6) - *Top row 1-2-3 is complete.* 8. Move **8** right. (State: 1 2 3, _ 8 5, 4 7 6) 9. Move **4** up. (State: 1 2 3, 4 8 5, _ 7 6) 10. Move **7** left. (State: 1 2 3, 4 8 5, 7 _ 6) 11. Move **8** down. (State: 1 2 3, 4 _ 5, 7 8 6) 12. Move | No | 12.98 |
