# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-25 15:40:57

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
| string_entry | 7280 | 38548 | 45828 | 4 | 16 | 64.51 | 1290.27 |
| **TOTAL** | **7280** | **38548** | **45828** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | //_\<<\<( |  | No | 90.69 |
| 2 | _<_\ _<</ | _<\ _<</ | No | 30.79 |
| 3 | /))\__ () | /))\_ () | No | 31.53 |
| 4 | /< _<_\<_ |  | No | 78.21 |
| 5 | <()/))_ \ |  | No | 85.91 |
| 6 | ___\)< _( |  | No | 86.72 |
| 7 |  _< /_/ < |  | No | 64.34 |
| 8 | _()(( \)) |  | No | 63.02 |
| 9 | ((<(\\_/) |  | No | 71.87 |
| 10 | </_</)) < | </_</)) < | Yes | 38.93 |
| 11 | /)(/__)\< |  | No | 100.39 |
| 12 |  (/\ (<</ |  | No | 71.22 |
| 13 | _/_\<(( _ | _/\<(( _ | No | 34.17 |
| 14 | </_  \_<) | </_  \_<) | Yes | 80.43 |
| 15 | /(/ (< <( | /(/ (< <( | Yes | 32.65 |
| 16 |  \)< _  / |  | No | 60.37 |
| 17 |  (\()/_(\ |  | No | 74.65 |
| 18 | ) <))\\ / |  | No | 75.51 |
| 19 | (\</)\/<< | (\</)\/<< | Yes | 15.11 |
| 20 | ((<))<)\  |  | No | 103.62 |
