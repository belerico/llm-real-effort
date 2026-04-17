# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-25 15:20:26

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
| string_entry | 4160 | 37127 | 41287 | 4 | 16 | 38.04 | 760.91 |
| **TOTAL** | **4160** | **37127** | **41287** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | / << )/\_ |  | No | 45.93 |
| 2 | <_\_/)_   |  | No | 31.29 |
| 3 | <_(<<(/() | <_(<<(/() | Yes | 18.17 |
| 4 | _//(<<)// |  | No | 39.9 |
| 5 | )(</__(<) |  | No | 47.42 |
| 6 |    / /<(/ |  | No | 51.36 |
| 7 | _<\\/<  < |  | No | 29.33 |
| 8 | _/</()(/_ |  | No | 26.64 |
| 9 |  <())/()< |  | No | 58.61 |
| 10 | )\\))()() |  | No | 21.73 |
| 11 | <\< _<\(\ |  | No | 49.68 |
| 12 | (/_\____  |  | No | 51.95 |
| 13 | <//_(_(_( | <//_(_(_( | Yes | 6.95 |
| 14 | _< ( _\)\ |  | No | 56.25 |
| 15 | /\< )(  < |  | No | 50.02 |
| 16 | \)  )(\(( |  | No | 61.39 |
| 17 | <(< )/< / | <(< )/< / | Yes | 10.2 |
| 18 | \/ _)_()_ |  | No | 56.57 |
| 19 |  _)\/_<_  |  | No | 31.65 |
| 20 | /)\/_<(\< | /)\/_<(\< | Yes | 15.82 |
