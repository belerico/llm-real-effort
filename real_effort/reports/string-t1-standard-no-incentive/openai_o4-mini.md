# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-25 15:28:53

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
| string_entry | 4460 | 31681 | 36141 | 8 | 12 | 28.32 | 566.56 |
| **TOTAL** | **4460** | **31681** | **36141** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ))()/_( < | ))()/_( < | Yes | 9.79 |
| 2 | /)\_/ /)/ |  | No | 61.39 |
| 3 | \<\<((/__ | \<\<((/__ | Yes | 9.82 |
| 4 |   \)_)_(\ | \)__)_(\ | No | 17.16 |
| 5 |  )\_)<__\ |  | No | 25.62 |
| 6 | /)\_(</() | /)\_(</() | Yes | 14.88 |
| 7 | \)_ \_))\ |  | No | 30.56 |
| 8 |  <)<<\/ / |  | No | 34.57 |
| 9 | _(  / \)< | _(  /\)< | No | 13.02 |
| 10 | \</ _\ \< | \</ _\ \< | Yes | 24.22 |
| 11 | \\//\(\(/ |  | No | 33.44 |
| 12 | )(_))/)\  | )(_))/)\ | No | 19.17 |
| 13 | <(()(\((/ | <(()(\((/ | Yes | 12.23 |
| 14 | <_(\/ __  |  | No | 77.69 |
| 15 | /\)_//(\  |  | No | 41.2 |
| 16 | ___<\__(( |  | No | 30.02 |
| 17 |  _\</ \)/ |  | No | 60.43 |
| 18 | (\\()</(_ | (\\()</(_ | Yes | 13.56 |
| 19 | \__/)\)/) | \__/)\)/) | Yes | 20.91 |
| 20 | _(</<) __ | _(</<) __ | Yes | 16.8 |
