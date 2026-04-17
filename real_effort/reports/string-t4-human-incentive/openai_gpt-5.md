# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-25 15:31:44

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
| string_entry | 7800 | 38714 | 46514 | 2 | 18 | 67.36 | 1347.29 |
| **TOTAL** | **7800** | **38714** | **46514** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  /)///<_) | /)//<_) | No | 41.4 |
| 2 |  )())/ \( |  | No | 68.62 |
| 3 | _)_ _<(   |  | No | 67.57 |
| 4 | (_ \\< )_ |  | No | 84.17 |
| 5 | __(/ <(<) | __(/ <(<) | Yes | 27.79 |
| 6 | \/_((<<\( | \/_(<<\( | No | 30.29 |
| 7 | _(\ \_\)< |  | No | 80.9 |
| 8 | _<)< \<\  |  | No | 68.58 |
| 9 |  (<< /)_) | (<< /)_) | No | 87.17 |
| 10 |  _\\ /(_< |  | No | 90.44 |
| 11 | / \\<\//_ |  | No | 101.45 |
| 12 |  _ \ _\(\ |  | No | 88.72 |
| 13 | /< (_<)_( | /< (_<)_( | Yes | 24.55 |
| 14 | \<( (<_(  |  | No | 83.19 |
| 15 | ((_)) //< |  | No | 101.29 |
| 16 | / (/_)<<) |  | No | 81.86 |
| 17 | <(_///(_  | <(_//(_ | No | 28.2 |
| 18 | <\__/ \ ) | <\_/  \) | No | 30.22 |
| 19 | (((_)(_\  |  | No | 79.98 |
| 20 | )\ \<(_\) |  | No | 80.76 |
