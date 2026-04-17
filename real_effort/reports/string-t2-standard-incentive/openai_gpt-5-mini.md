# Benchmark Report — gpt-5-mini

- **Model**: `openai/gpt-5-mini`
- **Date**: 2026-03-25 15:24:11

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
| string_entry | 4200 | 34529 | 38729 | 6 | 14 | 46.27 | 925.6 |
| **TOTAL** | **4200** | **34529** | **38729** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( )_< _/) |  | No | 61.29 |
| 2 | ) )( / )_ | ) )( / )_ | Yes | 34.14 |
| 3 | _\/<( )/  | _\/<( )/ | No | 30.5 |
| 4 | ) < <<)\) | ) < <<)\) | Yes | 37.98 |
| 5 |   )_/(_/\ |  | No | 57.4 |
| 6 | (/_/)<(\  | (/_/)<(\ ) | No | 27.35 |
| 7 | </( <((<\ | </( <((\< | No | 32.24 |
| 8 |  /\\(\</_ |  | No | 71.73 |
| 9 | //))<\)\< | //))<\)\< | Yes | 21.89 |
| 10 | (_(<(/)_/ | (_(<(/)_/ | Yes | 20.54 |
| 11 | (_/( _)<< | (_/(_ )<< | No | 17.73 |
| 12 | \/<<\_(/( | \/<\<\_(/( | No | 30.98 |
| 13 | _(/\_ ) ) |  | No | 73.56 |
| 14 | \ _//_)(_ |  | No | 72.86 |
| 15 | )/ <</\<( |  | No | 68.69 |
| 16 | _/)))/\)_ | _/)))/\)_ | Yes | 18.64 |
| 17 |  _//\<<_/ |  | No | 73.47 |
| 18 | /_\\)/)\_ |  | No | 79.43 |
| 19 | \<((\\<_/ | \<((\\<_/ | Yes | 13.81 |
| 20 | )\)_\\( _ |  | No | 81.27 |
