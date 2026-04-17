# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-25 15:30:31

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
| string_entry | 7620 | 38711 | 46331 | 3 | 17 | 64.47 | 1289.46 |
| **TOTAL** | **7620** | **38711** | **46331** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | / _)_)()( |  | No | 64.5 |
| 2 | )_\\\_ (  |  | No | 83.98 |
| 3 | )__ /((<( | )__ /((<( | Yes | 25.23 |
| 4 |  /)(/)()) |  | No | 72.07 |
| 5 | _ \_<\_ ( |  | No | 73.77 |
| 6 |  )_(_/< \ |  | No | 84.68 |
| 7 | \</ \ <)\ | \<\/ \ <)\ | No | 32.96 |
| 8 |  (  </_// | ( <_/// | No | 78.77 |
| 9 | _\\)((( / |  | No | 84.02 |
| 10 | <//\(<_ \ |  | No | 99.2 |
| 11 | /(/__)( \ | /(/__)( \ | Yes | 36.26 |
| 12 | ))_(__ _( | ))(__ _( | No | 32.74 |
| 13 | \  \) )_< |  | No | 75.86 |
| 14 | ()/(_ ) ( |  | No | 83.23 |
| 15 |  << _)(\\ |  | No | 80.5 |
| 16 | ) <_  \ ( | ) <_ \ ( | No | 32.13 |
| 17 | <__)<<)(/ | <__)<<)(/ | Yes | 33.49 |
| 18 | / (\/(/__ |  | No | 78.34 |
| 19 | \(/<) ))  |  | No | 68.65 |
| 20 | /))\/\)_) |  | No | 69.01 |
