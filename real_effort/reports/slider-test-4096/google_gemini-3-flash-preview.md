# Benchmark Report — gemini-3-flash-preview

- **Model**: `google/gemini-3-flash-preview`
- **Date**: 2026-04-01 19:57:49

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `4096`
- **reasoning_effort**: `high`

### Game Config Overrides

- **slider_puzzle**: size=3, num_shuffles=25

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| slider_puzzle | 1296 | 3372 | 4668 | 0 | 1 | 24.61 | 24.61 |
| **TOTAL** | **1296** | **3372** | **4668** | | | | |

## slider_puzzle

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | 3 6 7 1 6 3 5 2 3 5 4 6 1 7 5 4 6 1 4 6 2 3 6 5 8 | 3 1 4 3 1 2 5 1 3 4 2 3 1 5 3 2 4 1 2 3 5 3 6 8 5 6 5 | No | 24.61 |
