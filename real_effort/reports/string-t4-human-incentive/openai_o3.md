# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-25 15:26:14

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
| string_entry | 8100 | 37251 | 45351 | 1 | 19 | 50.91 | 1018.18 |
| **TOTAL** | **8100** | **37251** | **45351** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | \<_\) <<) |  | No | 53.6 |
| 2 | _///_\\(_ | _///_\\( | No | 23.79 |
| 3 | \ \\\<)<) |  | No | 29.42 |
| 4 | /(\\)<\)) |  | No | 69.26 |
| 5 | <)_)___/( |  | No | 57.91 |
| 6 |  )/)<) \( |  | No | 76.8 |
| 7 | \/ )\\(/\ |  | No | 62.52 |
| 8 | \_/)(/_() |  | No | 60.0 |
| 9 | )_) (_<<  |  | No | 52.98 |
| 10 | \/(</_)// | \/(</_)// | Yes | 28.36 |
| 11 | /()\) _// |  | No | 70.71 |
| 12 | <(<\( /)\ | <(<\(_/)\ | No | 22.85 |
| 13 | ) ) <())/ |  | No | 59.61 |
| 14 | /\/)(\()< | /\)(\()< | No | 38.72 |
| 15 | _((_/))_) | _((_/))) | No | 47.33 |
| 16 | \(_\ _(_  |  | No | 58.04 |
| 17 |  /\(\\//\ |  | No | 45.09 |
| 18 |  < \/__<( |  | No | 61.29 |
| 19 | /_ <(\\<  |  | No | 50.55 |
| 20 | /))<__ <  |  | No | 49.27 |
