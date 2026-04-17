# Benchmark Report — o4-mini

- **Model**: `openai/o4-mini`
- **Date**: 2026-03-25 15:18:56

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
| string_entry | 4980 | 30428 | 35408 | 10 | 10 | 29.00 | 580.05 |
| **TOTAL** | **4980** | **30428** | **35408** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | )()\\/< ) |  | No | 51.01 |
| 2 | (<_\/(_ / | (<_\/(_ / | Yes | 15.25 |
| 3 | \ /_/\\() |  | No | 45.23 |
| 4 | (/)\/  /  |  | No | 42.82 |
| 5 | )\()\/(<) | )\()\/(<) | Yes | 15.97 |
| 6 | /\\<(((<  |  | No | 61.25 |
| 7 | )<<\))/_( | )<<\))/_( | Yes | 15.75 |
| 8 | )\_))<)\( | )\_))<)\( | Yes | 16.05 |
| 9 |  /)_)(_/) |  | No | 49.81 |
| 10 | (__()\<(( | (__()\<(( | Yes | 15.5 |
| 11 | _(( <_/_( | _(( <_/_( | Yes | 6.77 |
| 12 | \((<_  <( | \((<_  <( | Yes | 16.38 |
| 13 | _ /<<\_// | _ /<<\_// | Yes | 8.77 |
| 14 | (_)< \ <) | (_)< \ <) | Yes | 14.38 |
| 15 | \/ /\())  |  | No | 52.61 |
| 16 |  \_)_(<(< | \_)_(<(< | No | 15.13 |
| 17 |  (< _()_/ |  | No | 31.05 |
| 18 | <\/_<_ \  | <\ /_<_\ | No | 32.88 |
| 19 |  )/)/_\<) |  | No | 58.99 |
| 20 | (/\)//<\\ | (/\)//<\\ | Yes | 14.33 |
