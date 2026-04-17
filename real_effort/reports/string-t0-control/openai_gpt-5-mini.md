# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-25 15:25:31

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
| string_entry | 3720 | 35688 | 39408 | 9 | 11 | 53.29 | 1065.86 |
| **TOTAL** | **3720** | **35688** | **39408** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \<<_<_ (  |  | No | 75.6 |
| 2 | _ \)_\()) |  | No | 62.7 |
| 3 | \)(< ((\< | \)(< ((\< | Yes | 32.82 |
| 4 |  <(/_ ))  |  | No | 80.92 |
| 5 |  (\ __/ _ |  | No | 74.21 |
| 6 | ((/\(\( / |  | No | 71.68 |
| 7 | \_< _/_(< | \_< _/_(< | Yes | 23.4 |
| 8 | _ /<)(/_\ |  | No | 81.75 |
| 9 | (__\\_((_ | (__\\_((_ | Yes | 30.85 |
| 10 | (((_) ))\ |  | No | 66.02 |
| 11 | (\)<<)(<( | (\)<<)(<( | Yes | 29.19 |
| 12 | ((/\_//() | ((/\_//() | Yes | 22.74 |
| 13 | () <\_ \< |  | No | 66.7 |
| 14 | /<</_\ _( | /<</_\ _( | Yes | 29.45 |
| 15 | /_\((_)<_ |  | No | 89.68 |
| 16 | _\_( )_(( | _\_( )_(( | Yes | 23.38 |
| 17 | (\//\(__< | (\//\(__< | Yes | 31.17 |
| 18 | \<))<_\ ) | \<))<_\ ) | Yes | 24.13 |
| 19 | / /)\)\(< |  | No | 66.71 |
| 20 | \)<\<())) | \)<\<(())) | No | 82.64 |
