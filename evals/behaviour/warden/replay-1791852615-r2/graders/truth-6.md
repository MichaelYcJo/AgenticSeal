---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/rounds/round-2-report.md'}
pattern: '^\| (?:🔴|🟡) \d+ \|.*(?:docs\/the-evidence-ledger\.md:(?:627|628|629|630|631|632|633|634|635|636|637|638|639|640|641|642|643|644|645|646|647|648|649|650|651|652|653|654|655|656|657)(?!\d))'
flags: 'm'
---
Round 2's 🟡 6: the excusing bullet attributes `routing.md` rows to `hidden_lines` and calls a row below an unclosed comment opener the one place a hidden line declares; `routing.md` is read by `hooks/routing.py#shown`, which declares a row below a fence nobody closed; `hidden_lines`' `Reads:` line names `routing.md`, which no caller hands it
