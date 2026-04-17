# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-25 15:25:42

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
| string_entry | 7760 | 37310 | 45070 | 3 | 17 | 50.85 | 1017.08 |
| **TOTAL** | **7760** | **37310** | **45070** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \</<<   ( | \<\/<___( | No | 35.98 |
| 2 |  /)_<\))( |  | No | 66.76 |
| 3 | <()\(/((/ | <()\(/(/ | No | 11.56 |
| 4 |  (/  _\   |  | No | 34.1 |
| 5 | /<\)\< /( |  | No | 40.97 |
| 6 | (\() (/ _ |  | No | 49.56 |
| 7 | /(<_ (/)) |  | No | 54.77 |
| 8 |  (/_(/_)< |  | No | 77.25 |
| 9 | _/\_(((<) |  | No | 72.48 |
| 10 | )//(() <\ |  | No | 47.58 |
| 11 | ))<<)//(\ | ))<<)//(\ | Yes | 41.45 |
| 12 | _)__(_//\ |  | No | 43.19 |
| 13 | _ _/ _(() |  | No | 77.51 |
| 14 |  __()<)(< |  | No | 46.9 |
| 15 | /) \ //(/ |  | No | 65.09 |
| 16 | / \(_/\/< |  | No | 70.66 |
| 17 | (/<<\)(/( | (/<<\)(/( | Yes | 11.4 |
| 18 | < _//))/_ |  | No | 75.3 |
| 19 | \))< /</_ | \))< /</_ | Yes | 35.12 |
| 20 | (\/)(< (  |  | No | 59.37 |
