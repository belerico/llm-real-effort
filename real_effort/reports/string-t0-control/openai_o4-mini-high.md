# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-25 15:21:21

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
| string_entry | 4160 | 36799 | 40959 | 6 | 14 | 39.25 | 785.1 |
| **TOTAL** | **4160** | **36799** | **40959** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (<  (___< |  | No | 61.34 |
| 2 | )\ )_/((_ |  | No | 56.23 |
| 3 | <_\(\\/// | <_\(\\/// | Yes | 19.93 |
| 4 | _  /()_(( |  | No | 44.94 |
| 5 | <\(__\))( | <\(__\))( | Yes | 9.03 |
| 6 | \  ____/_ |  | No | 48.4 |
| 7 | _/_(( ) / | _/_(( ) / | Yes | 13.2 |
| 8 |  \\_(<)_( |  | No | 27.16 |
| 9 | ()_ ))\   |  | No | 51.88 |
| 10 | (\<<_(((\ |  | No | 41.56 |
| 11 | )() ( (\) |  | No | 29.76 |
| 12 | / \(_\\__ |  | No | 53.05 |
| 13 | \/)/<(()< |  | No | 33.71 |
| 14 | (<(\_<<\< | (<(\_<<\< | Yes | 19.87 |
| 15 |   /(\\/ \ |  | No | 58.64 |
| 16 | <_\((_/() | <_\((_/() | Yes | 20.67 |
| 17 | ))\/(_ << |  | No | 59.82 |
| 18 | /_\< _)/_ | /_\< _)/_ | Yes | 17.73 |
| 19 | ) (\\/_/_ |  | No | 50.95 |
| 20 | <\_/)((\/ |  | No | 67.17 |
