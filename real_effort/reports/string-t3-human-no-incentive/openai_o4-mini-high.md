# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-25 15:18:21

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

**Model-specific overrides:**
- temperature: `None`

### Game Config Overrides

- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| string_entry | 4800 | 32032 | 36832 | 9 | 11 | 27.99 | 559.83 |
| **TOTAL** | **4800** | **32032** | **36832** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \)__(_\\) | \)__(_\\) | Yes | 15.28 |
| 2 | (\/__ /(_ | (\/__ /(_ | Yes | 15.04 |
| 3 | __)/(/ <  |  | No | 47.46 |
| 4 | ()_ \</\  | ()_ </\ | No | 28.28 |
| 5 | _\)\_((<) | _\)\_((<) | Yes | 22.09 |
| 6 |  \\)/_)<( | \\)/_)<( | No | 16.0 |
| 7 | <\)(<\\</ |  | No | 39.32 |
| 8 | ))))_<_/< | ))))_<_/< | Yes | 14.43 |
| 9 | <_(<_ ) _ | <_(<_ ) _ | Yes | 16.05 |
| 10 |  <_(  _(  |  | No | 59.93 |
| 11 | ()_)(_//_ | ()_)(_//_ | Yes | 14.94 |
| 12 | \  <()(   |  | No | 57.37 |
| 13 | <<))/ (\) |  | No | 39.01 |
| 14 | _/\) \_\/ |  | No | 35.43 |
| 15 | /<_ \ )\/ |  | No | 42.32 |
| 16 | /_<_\/\)  | /_<_\/\) | No | 19.7 |
| 17 | <<\\\_ (\ | <<\\\_ (\ | Yes | 12.73 |
| 18 |  ()(()\/< | ()(()\/< | No | 25.3 |
| 19 | )/<(< _\) | )/<(< _\) | Yes | 19.09 |
| 20 | _  < \<(< | _  < \<(< | Yes | 20.0 |
