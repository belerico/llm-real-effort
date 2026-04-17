# Benchmark Report — o3

- **Model**: `openai/o3`
- **Date**: 2026-03-25 15:27:37

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
| string_entry | 7280 | 40042 | 47322 | 1 | 19 | 58.04 | 1160.86 |
| **TOTAL** | **7280** | **40042** | **47322** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | (  /)/_ \ |  | No | 63.51 |
| 2 |  \)_/ (_  |  | No | 38.57 |
| 3 | <)(</\<<  |  | No | 65.36 |
| 4 | )\)<_ /(< | )\)<_ /(< | Yes | 25.71 |
| 5 | )\)\_((_/ |  | No | 50.6 |
| 6 |  )<)\ (/  |  | No | 63.63 |
| 7 |  \\//()(/ |  | No | 81.79 |
| 8 | )_)\ </)< |  | No | 43.81 |
| 9 | _<(<<)<)\ |  | No | 59.67 |
| 10 | (()/ / <) |  | No | 46.57 |
| 11 | ( )<< ) \ |  | No | 50.97 |
| 12 | )\\< \_/( |  | No | 68.19 |
| 13 | /_/ _ /_) |  | No | 63.22 |
| 14 | \/ )<(/_  |  | No | 79.09 |
| 15 | )\_<  __( |  | No | 44.16 |
| 16 | ) /(\ <\) | )_/(\<\) | No | 36.29 |
| 17 | <<\)(<(<  |  | No | 45.4 |
| 18 | _\ ()/\/\ |  | No | 75.42 |
| 19 | </ ) (</( |  | No | 76.72 |
| 20 | < / \(/(< |  | No | 82.08 |
