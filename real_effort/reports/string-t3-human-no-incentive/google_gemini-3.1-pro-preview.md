# Benchmark Report — gemini-3.1-pro-preview

- **Model**: `google/gemini-3.1-pro-preview`
- **Date**: 2026-03-25 15:14:15

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| string_entry | 24023 | 8725 | 32748 | 12 | 8 | 15.69 | 313.81 |
| **TOTAL** | **24023** | **8725** | **32748** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | ( \\<)<\/ | ( \\<)<\/ | Yes | 7.62 |
| 2 |  _(_<(</_ | _(_<(</_ | No | 8.15 |
| 3 |  /_\)(</  | /_\)(</ | No | 17.37 |
| 4 | \/  __)<  | \/  __)< | No | 19.49 |
| 5 | _/\ /( \( | _/\ /( \( | Yes | 17.61 |
| 6 | ()\\ /\/) | ()\\ /\/) | Yes | 10.05 |
| 7 | <)/(\ /(_ | <)/(\ /(_ | Yes | 21.04 |
| 8 | <)_ __/ / | <)_ __/ / | Yes | 27.0 |
| 9 | (_( \/_)< | (_( \/_)< | Yes | 17.54 |
| 10 | <<)_/ <_\ | ERROR: TypeError: 'NoneType' object is not subscriptable | No | 10.91 |
| 11 | /)/\(<_/< | /)/\(<_/< | Yes | 20.82 |
| 12 | /)   () ( | /)   () ( | Yes | 17.09 |
| 13 | < </)/)_  | < </) /)_ | No | 8.44 |
| 14 | (_\()/(   | (_\()/( | No | 18.22 |
| 15 | <(_ <<\_  | <(_ <<\_ | No | 19.25 |
| 16 |  /</ <(</ | /</ <(</ | No | 8.51 |
| 17 | (\\__ )/) | (\\__ )/) | Yes | 16.07 |
| 18 | ( (  )\)_ | ( (  )\)_ | Yes | 19.71 |
| 19 | _//\ \_)( | _//\ \_)( | Yes | 20.09 |
| 20 | <\) </<\( | <\) </<\( | Yes | 8.78 |
