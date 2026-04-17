# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-25 15:21:06

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
| string_entry | 4640 | 35229 | 39869 | 7 | 13 | 37.05 | 741.12 |
| **TOTAL** | **4640** | **35229** | **39869** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _( <  /\< |  | No | 36.72 |
| 2 | _\_ ()/ ) |  | No | 56.57 |
| 3 | (\ </\___ |  | No | 57.79 |
| 4 | (/<))\<_< | (/<))\<_< | Yes | 9.95 |
| 5 | _(<))( __ | _(<))( __ | Yes | 16.8 |
| 6 | (<_<  (/_ |  | No | 59.26 |
| 7 | <)<_)(_<_ |  | No | 29.86 |
| 8 | //( /\))  |  | No | 46.57 |
| 9 | /<\ _( \\ |  | No | 41.23 |
| 10 | \_\)\ _\\ |  | No | 50.7 |
| 11 | )\ _)<(/_ | )\ _)<(/_ | Yes | 16.85 |
| 12 | <((\__<_  |  | No | 61.18 |
| 13 | _(_ /\/(\ | _(_ /\/(\ | Yes | 22.45 |
| 14 | _)__<__)  |  | No | 34.28 |
| 15 | <<_/_ / _ |  | No | 44.38 |
| 16 | ))( () \  |  | No | 59.97 |
| 17 | _<)\< //( | _<)\< //( | Yes | 9.32 |
| 18 | )__<<\_ \ | )__<<\_ \ | Yes | 20.96 |
| 19 | <)( /(_)_ | <)( /(_)_ | Yes | 13.55 |
| 20 | \(<_)\()\ |  | No | 52.66 |
