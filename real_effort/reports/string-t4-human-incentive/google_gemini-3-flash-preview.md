# Benchmark Report — gemini-3-flash-preview

- **Model**: `google/gemini-3-flash-preview`
- **Date**: 2026-03-25 15:13:01

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| string_entry | 24199 | 18221 | 42420 | 11 | 9 | 11.26 | 225.36 |
| **TOTAL** | **24199** | **18221** | **42420** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | _ /_ )/() | _ /_ )/() | Yes | 10.52 |
| 2 | < (< /(/< | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 11.22 |
| 3 | /()_) _)\ | /()_) _) \ | No | 15.25 |
| 4 | <</ __(/\ | <</ __(/\ | Yes | 13.71 |
| 5 | <(_\/)  ) | <(_\/)  ) | Yes | 6.11 |
| 6 | /_<)/)()_ | /_<)/)()_ | Yes | 13.17 |
| 7 |  )</<)) / | )</<)) / | No | 10.65 |
| 8 | \_()) / ) | \_()) / ) | Yes | 16.48 |
| 9 | <  /_(<   | <  /_ (< | No | 17.12 |
| 10 | _/(((//\( | _/(( (//\( | No | 8.49 |
| 11 | <_((//<)  | <_((//<) 💡 | No | 6.01 |
| 12 | /__\ )\<) | /__\ )\<) | Yes | 7.78 |
| 13 | <\  <_(_\ | <\  <(__\ | No | 13.81 |
| 14 | \_)/\_\/( | \_)/\_ \/( | No | 18.27 |
| 15 | ( << <\\< | ( << <\\< | Yes | 5.75 |
| 16 | \\<_(</\) | \\<_(</\) | Yes | 7.31 |
| 17 | \(\ \_<__ | \(\ \_<__ | Yes | 4.97 |
| 18 | ) _\_ /() | ) _\_ /() | Yes | 7.29 |
| 19 | \_) \(/<) | \_) \(/(<) | No | 15.37 |
| 20 | \/ _)/)() | \/ _)/)() | Yes | 15.88 |
