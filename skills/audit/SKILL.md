---
name: audit
description: |
  Validate project-specific rules a linter cannot express, declared as
  `.claude/audit-rules/*.md`.
  Use when: checking conventions this repo wrote down for itself before a
  commit or release.
  NOT for: formatting or style a linter already enforces, security review
  (`security-audit`), or comparing a spec against the code (`gap-analysis`).
---

# audit, the rules this repo wrote down for itself

A linter enforces what every project agrees on. This checks what only *this*
project agreed on, declared as `.claude/audit-rules/*.md`. A rule with no
file behind it is not a rule; if the directory is empty, say so rather than
inventing conventions.

## How It Works

1. **Check for rules**: look for `.claude/audit-rules/*.md` files.
2. **If no rules exist**: suggest bootstrapping with common patterns.
3. **If rules exist**: validate each rule against the codebase.

## Rule File Format

Each `.claude/audit-rules/[name].md` defines:
- **Pattern**: what to check (a regex, a file pattern, or a description)
- **Expected**: what should be true
- **Severity**: `critical`, `warning` or `info`

## Common starting rules

Nothing here runs on its own. These are what to propose when
`.claude/audit-rules/` is empty (step 2), and each one becomes a rule only once
it is written as a file:

- No hardcoded secrets (API keys, passwords, tokens)
- No `console.log` in production code (unless a logging library wraps it)
- No TODO or FIXME in the code being committed

## Managing rules

There is no `audit` command to run. A rule is a file, so adding one means
writing `.claude/audit-rules/<name>.md`, listing them means reading that
directory, and removing one means deleting the file.

## Output Format

```
## Audit Results

passed: [N] rules
warnings: [N]
violations: [N]

[For each violation:]
violation: [rule name], severity: [severity]
   [file:line] [what's wrong]
   Fix: [suggestion]
```
