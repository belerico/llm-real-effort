# Benchmark Report — gemini-2.5-flash

- **Model**: `google/gemini-2.5-flash`
- **Date**: 2026-03-25 15:11:23

## Run Configuration

- **temperature**: `0.6`
- **max_tokens**: `2048`
- **reasoning_effort**: `high`

### Game Config Overrides

- **string_entry**: length=9

## Summary

| Game | Prompt Tokens | Completion Tokens | Total Tokens | Correct | Incorrect | Avg Response Time (s) | Session Time (s) |
|------|--------------|-------------------|-------------|---------|-----------|----------------------|------------------|
| string_entry | 23336 | 14221 | 37557 | 4 | 16 | 9.35 | 187.09 |
| **TOTAL** | **23336** | **14221** | **37557** | | | | |

## string_entry

| Iteration | Solution | Response | Correct | Response Time (s) |
|-----------|----------|----------|---------|-------------------|
| 1 | <(<//_) \ | <(<//_) \ | Yes | 4.93 |
| 2 | < <<(\<\_ | < <<(\<\_ | Yes | 14.48 |
| 3 | ))/_)<)/  | ))/_)<)/ | No | 3.51 |
| 4 | \ /\ /_\_ | \ /\ /_\_ | Yes | 15.5 |
| 5 | )_<<(_/<\ | )_<<(_</\ | No | 10.06 |
| 6 |  )(\< /)_ | )(\< /)_ | No | 4.72 |
| 7 | <((<)( (( | <(( (<)) ( (( | No | 5.08 |
| 8 | _(_(\/_ \ | _(_(\/_ _\ | No | 8.46 |
| 9 | )_\<_/_)\ | ) _ \ < _ / _ ) \ | No | 3.69 |
| 10 | )_)_/<</_ | )_ )_ / << / _ | No | 3.49 |
| 11 | / _((_(/  | / _((_(` / | No | 17.05 |
| 12 | __(\( _ / | __(\( _ / | Yes | 19.94 |
| 13 | _(\_<\\)< | _(\_\\)< | No | 4.92 |
| 14 | <<__\<<)\ | The image displays a sequence of characters within individual boxes. I need to transcribe these characters in order, including any spaces. The allowed characters are: `/ \ ) ( _ <` and space. The prompt states, "Spaces are shown as the ␣ (open box) symbol."  Let's go through the characters one by one:  1.  First box: `<` 2.  Second box: `<` 3.  Third box: `_` 4.  Fourth box: `_` 5.  Fifth box: This box is empty. The instruction "Spaces are shown as the ␣ (open box) symbol" implies that an empty box *is* a space, and the `␣` is just an illustrative symbol for it. Therefore, this is a space. 6.  Sixth box: `/` (forward slash) 7.  Seventh box: `<` 8.  Eighth box: `<` 9.  Ninth box: `)` 10. Tenth box: `\` (backslash)  Combining these, the transcribed string is `<<__ /<<)\`.  The final answer is `<<__ /<<)\` | No | 10.22 |
| 15 | __<  <<)) | __<<((<)) | No | 18.81 |
| 16 | \\/( )(   | \\ / ( ) (   ) | No | 16.41 |
| 17 | <__(<_//\ | <___(<_ _/\ | No | 8.27 |
| 18 | /_<)_)/\\ | /_ <)_ )//\\ | No | 5.45 |
| 19 |  ( /()/ _ | ` ( / ( ) / _` | No | 7.18 |
| 20 | \/ (/ <<  | \ / ( / << | No | 4.89 |
