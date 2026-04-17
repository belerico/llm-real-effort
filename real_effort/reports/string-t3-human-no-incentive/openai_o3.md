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
| string_entry | 7920 | 37342 | 45262 | 6 | 14 | 51.63 | 1032.7 |
| **TOTAL** | **7920** | **37342** | **45262** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /\<\()\ _ | /\<\()\ _ | Yes | 19.54 |
| 2 | ())//((_/ |  | No | 59.62 |
| 3 | )\ \\ (/( |  | No | 44.82 |
| 4 | (/)\<\))< | (/)\<\))< | Yes | 40.95 |
| 5 | (\ _)\/(< |  | No | 49.78 |
| 6 | (/< <<___ |  | No | 53.7 |
| 7 | //_/_/\\\ | ///_\\\\ | No | 57.78 |
| 8 | </)(<(<__ | </)(<(<__ | Yes | 35.46 |
| 9 | \( /))_// |  | No | 70.2 |
| 10 | ( /((\ \( |  | No | 64.81 |
| 11 | \\\)<\\\( | \\\)<\\\( | Yes | 39.67 |
| 12 | / /<)<<)( |  | No | 38.54 |
| 13 | _(\<<))\( | _(\<<))\( | Yes | 16.53 |
| 14 | (_\) /(/) |  | No | 82.26 |
| 15 | \_\\ __() |  | No | 73.92 |
| 16 | _)\(<<_/\ | _)\(<<_/\ | Yes | 23.12 |
| 17 | <_)/<</() |  | No | 76.81 |
| 18 | /</)/__\/ |  | No | 66.89 |
| 19 | _(\_(</)( |  | No | 39.38 |
| 20 | (_)/< /// |  | No | 78.85 |
