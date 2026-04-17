# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-25 15:20:13

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
| string_entry | 4980 | 34272 | 39252 | 6 | 14 | 32.82 | 656.5 |
| **TOTAL** | **4980** | **34272** | **39252** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 |  /(<(</(/ |  | No | 25.73 |
| 2 | ( \/\/<\\ | ( \/\ /<\\ | No | 11.41 |
| 3 | < /()()</ | < /()()</ | Yes | 15.98 |
| 4 | <<_)<<_<( | <<_)<<_<( | Yes | 13.32 |
| 5 | (/_\)_)\_ | (/_\)_)\_ | Yes | 17.62 |
| 6 | )<<<<\/)  |  | No | 47.96 |
| 7 | (_)<_/_<) |  | No | 55.94 |
| 8 | _/((_/)</ | _/((_/)</ | Yes | 13.16 |
| 9 | ()(\(<< ) | ()(\(<< ) | Yes | 17.31 |
| 10 | _\\/_\//\ |  | No | 60.94 |
| 11 | \</\\ )</ | \</\\ )</ | Yes | 16.64 |
| 12 | _<_(\(_ ( | _<_(\_ ( | No | 13.32 |
| 13 | \_<)(<(<< |  | No | 27.02 |
| 14 | \\/_ <(_< |  | No | 39.4 |
| 15 | <\ )/_\\  |  | No | 25.78 |
| 16 | (  __ (\\ |  | No | 63.61 |
| 17 | ( _)(\\ ( |  | No | 36.31 |
| 18 | <_<_/ (_( |  | No | 60.22 |
| 19 | )(   _/<  |  | No | 37.6 |
| 20 |  )_)\/\)) |  | No | 57.12 |
