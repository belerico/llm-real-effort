# Benchmark Report — o4-mini-high

- **Model**: `openai/o4-mini-high`
- **Date**: 2026-03-25 15:19:23

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
| string_entry | 4640 | 34681 | 39321 | 8 | 12 | 31.88 | 637.72 |
| **TOTAL** | **4640** | **34681** | **39321** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (   /\ <\ | (   /\ <\ | Yes | 19.72 |
| 2 | _ /<_)(/\ |  | No | 38.7 |
| 3 | <\)_ //\  |  | No | 54.72 |
| 4 | \ )<_/<_) |  | No | 48.9 |
| 5 | )_ /\_ (_ | )_ /\_ (_ | Yes | 10.84 |
| 6 | << _/_/)/ | << _/_/)/ | Yes | 20.95 |
| 7 | <))(\(/(< | <))(\(/(< | Yes | 12.83 |
| 8 | (((___/<  |  | No | 35.55 |
| 9 | (/(\((_<_ | (/(\((_<_ | Yes | 12.59 |
| 10 |   /\_/\)/ |  | No | 25.99 |
| 11 | <) \(_ )( | <) \(_ )( | Yes | 13.61 |
| 12 | \ )_/< )  |  | No | 57.56 |
| 13 | )_ (//< < |  | No | 27.46 |
| 14 | / <_(\/ ) | / <_(\/ ) | Yes | 29.29 |
| 15 |   __<_/</ |  | No | 35.75 |
| 16 | \\\)<  /\ | \\\)<  /\ | Yes | 28.15 |
| 17 | <</\ _</_ | <<\/ _</_ | No | 18.81 |
| 18 | _\ \//<)< |  | No | 56.96 |
| 19 | _/_)\\)_) |  | No | 22.79 |
| 20 | \ )()(  < |  | No | 66.48 |
