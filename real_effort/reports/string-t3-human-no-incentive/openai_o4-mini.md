# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-25 15:18:03

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
| string_entry | 4800 | 32176 | 36976 | 9 | 11 | 27.07 | 541.48 |
| **TOTAL** | **4800** | **32176** | **36976** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  _// \\ / |  | No | 26.16 |
| 2 | (( \ \\_( |  | No | 39.55 |
| 3 | ) <<//(<  | ) <<//(< | No | 21.02 |
| 4 | /(/\\<))_ | /(/\\<))_ | Yes | 15.92 |
| 5 | _) /)\)_  |  | No | 38.15 |
| 6 | //( <<()) | /\( <<()) | No | 16.44 |
| 7 | _()())<(\ | _()())<(\ | Yes | 11.08 |
| 8 | )__\/\_\\ | )__\/\_\\ | Yes | 21.75 |
| 9 | _\)(_/((  | _\)(_/( | No | 17.93 |
| 10 | )))<) \\< | )))<) \\< | Yes | 13.79 |
| 11 | _<() \\_< | _<() \\_< | Yes | 10.64 |
| 12 | )(_<\(__) | )(_<\(__) | Yes | 16.61 |
| 13 | //)_)<</) |  | No | 58.47 |
| 14 |  (( <<</< |  | No | 50.6 |
| 15 | __(/< )<\ | __(/< )<\ | Yes | 19.11 |
| 16 | )/) \\\_\ | )/) \\\_\ | Yes | 25.73 |
| 17 | _/))_\//  |  | No | 36.28 |
| 18 | < (\/) )< |  | No | 29.63 |
| 19 | _/)(_<\)  |  | No | 56.9 |
| 20 | )\/(\/<)_ | )\/(\/<)_ | Yes | 15.67 |
