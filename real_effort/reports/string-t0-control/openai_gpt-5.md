# Benchmark Report — gpt-5

- **Model**: `openai/gpt-5`
- **Date**: 2026-03-25 15:31:07

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
| string_entry | 6980 | 37712 | 44692 | 4 | 16 | 68.49 | 1369.95 |
| **TOTAL** | **6980** | **37712** | **44692** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | / </\_/<( |  | No | 91.56 |
| 2 | _/ <)\\(( |  | No | 97.66 |
| 3 | (_\<(\_(  |  | No | 87.58 |
| 4 | <<<_ _\/  |  | No | 91.67 |
| 5 | )  /)<))< |  | No | 70.15 |
| 6 | (_( ( /(/ |  | No | 90.83 |
| 7 | / / \)_<( |  | No | 82.57 |
| 8 | //\  ( )< |  | No | 96.25 |
| 9 | <(<(\_//_ | <(<(\_//_ | Yes | 42.53 |
| 10 | <)<_(_<(\ | <)<_(_<(\ | Yes | 27.12 |
| 11 | (  _)_(/\ |  | No | 76.29 |
| 12 | \_<</)    | \_<</) | No | 47.47 |
| 13 | _\/)_)(\( | _\/)_)(\( | Yes | 42.41 |
| 14 | _)_\(\_)\ |  | No | 73.89 |
| 15 | \_\()) </ |  | No | 68.25 |
| 16 | ()_ //_ _ |  | No | 68.27 |
| 17 | /()_)) _( | /()_)) _( | Yes | 19.42 |
| 18 | /))_  /\  |  | No | 91.48 |
| 19 | \)_<< /)( |  | No | 80.86 |
| 20 | )/)_)/___ | )/)_)/__ | No | 23.57 |
