# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-25 15:29:26

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
| string_entry | 4460 | 32093 | 36553 | 9 | 11 | 29.95 | 599.01 |
| **TOTAL** | **4460** | **32093** | **36553** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | /(_<(_/__ | /(_<(_/__ | Yes | 12.63 |
| 2 | (<)< __\  | (<)< __\ | No | 18.68 |
| 3 | </ )/\_<( |  | No | 32.83 |
| 4 | \/)/)_( < | \/)/)_( < | Yes | 10.44 |
| 5 | <))()<_)) |  | No | 45.18 |
| 6 | /_< \/< _ | /_< \/< _ | Yes | 22.05 |
| 7 | _/\\/<\<  |  | No | 53.11 |
| 8 | (_)\<_)// | (_)\<_)// | Yes | 21.82 |
| 9 | <\\/)__\/ | <\\/)__\/ | Yes | 18.21 |
| 10 | < _/)_) ( | < _/)_) ( | Yes | 24.2 |
| 11 |  (_))   < |  | No | 52.2 |
| 12 |  _/(_<\)/ | _/(_<\)/ | No | 10.84 |
| 13 | /_/<</ )( |  | No | 22.97 |
| 14 | //< )))<\ |  | No | 42.56 |
| 15 | __ )(_<(( |  | No | 52.37 |
| 16 | < \  (( / |  | No | 50.92 |
| 17 | \_(\/)</_ | \_(\/)</_ | Yes | 15.26 |
| 18 | ///)<))() | ///)<))() | Yes | 19.36 |
| 19 | < <\\_//) |  | No | 64.29 |
| 20 | )<) <)_<_ | )<) <)_<_ | Yes | 8.99 |
