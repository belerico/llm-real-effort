# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-25 15:35:52

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
| string_entry | 4020 | 35623 | 39643 | 11 | 9 | 49.26 | 985.36 |
| **TOTAL** | **4020** | **35623** | **39643** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ))/_/\<\/ | ))/_/\<\/ | Yes | 31.36 |
| 2 | <<< ) (() | <<< ) (() | Yes | 26.93 |
| 3 | _)  ) /// | _)  ) /// | Yes | 24.63 |
| 4 | << _/\<_( |  | No | 76.47 |
| 5 | <  _///__ |  | No | 67.84 |
| 6 | \((/ _  ( |  | No | 78.19 |
| 7 | )\<)/<_/\ | )\<)/<_/\ | Yes | 23.83 |
| 8 | /  () /(  |  | No | 74.13 |
| 9 | (\)<((\\) | (\)<((\\) | Yes | 29.89 |
| 10 | \(<\<_<_/ | \(<\<_<_/ | Yes | 32.78 |
| 11 | )\_ /__/  |  | No | 68.14 |
| 12 | \/\)/)/ ) |  | No | 82.35 |
| 13 | ( )_(\/_/ | ( )_(\/_/ | Yes | 32.5 |
| 14 | \<\ ()) < |  | No | 68.17 |
| 15 | \/__<<_ ( |  | No | 64.71 |
| 16 | <<///<<)< | <<///<<)< | Yes | 26.51 |
| 17 | ) < \(\_( |  | No | 80.24 |
| 18 | <(_/(<(/_ | <(_/(<(/_ | Yes | 39.27 |
| 19 | )(<_</( / | )(<_</( / | Yes | 19.64 |
| 20 | <( )(_\)\ | <( )(_\)\ | Yes | 37.69 |
