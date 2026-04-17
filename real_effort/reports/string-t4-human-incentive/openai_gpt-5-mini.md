# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-25 15:30:40

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
| string_entry | 4540 | 39203 | 43743 | 2 | 18 | 64.20 | 1284.07 |
| **TOTAL** | **4540** | **39203** | **43743** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ()(\)//<  |  | No | 63.67 |
| 2 | /_() (_ \ |  | No | 55.54 |
| 3 |  __/)\_<) | __/)\_<) | No | 42.99 |
| 4 |  _<(_/(/< |  | No | 84.48 |
| 5 |  <<))()\\ |  | No | 80.14 |
| 6 |  )<\_)))( |  | No | 61.4 |
| 7 |  \<  <_ / |  | No | 81.97 |
| 8 | _ _))( \< |  | No | 79.44 |
| 9 | )(//\\ _/ |  | No | 80.23 |
| 10 | (/)/ /___ |  | No | 65.57 |
| 11 | /)/\<(/)_ |  | No | 75.97 |
| 12 |  <__)_<)\ | <__)_<)\ | No | 30.42 |
| 13 |  ) ))< /  |  | No | 73.7 |
| 14 | \((<)_\(  |  | No | 64.24 |
| 15 | (_\()/ () | (_\()/ () | Yes | 24.57 |
| 16 | )()<(/__\ |  | No | 77.2 |
| 17 |  /)/<_<(/ |  | No | 67.36 |
| 18 |  /) )<_)_ |  | No | 70.99 |
| 19 | _ \)/)_\( | _ \)/)_\( | Yes | 35.02 |
| 20 | /<_) \( _ |  | No | 69.1 |
