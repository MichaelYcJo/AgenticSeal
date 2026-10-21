---
name: build-fix
description: |
  Resolve build, compile, and type-check errors at their cause instead of
  suppressing them.
  Use when: the build does not produce output: type errors, missing modules,
  syntax or config failures.
  NOT for: code that compiles but behaves wrong (that is `debug`).
---

# build-fix, fix the cause, never the message

Nothing runs yet, so there is nothing to reproduce: the compiler already said
where it stopped. The failure mode here is suppression: a cast, an `any`, an
ignore comment makes the message go away and leaves the defect. The first
error is usually the only real one; the rest are its shadow.

## Process

1. **Read the full error.** Don't fix based on the first line alone.
2. **Categorize**
   - Type error: check type definitions, imports
   - Missing module: check dependencies, paths
   - Syntax error: check recent changes
   - Config error: check build config files
3. **Fix the root cause**, not the symptoms.
4. **Verify**: run the full build again after the fix.

## Rules

- Fix ONE error category at a time (cascade errors are common)
- After fixing, re-run the build to check for new errors
- If the same error persists after two attempts, re-examine the approach
- If three attempts fail, invoke the 3+ Fix Rule: stop and ask the user

## Common Traps
- Fixing type errors by adding `any` or `as unknown`
- Suppressing errors with `@ts-ignore` or `# type: ignore`
- Fixing import errors by creating empty stub files
- These are symptoms, not fixes. Find the real cause.

## Output Format

```
Error: [category], [summary]
Root cause: [why it's happening]
Fix: [what was changed]
Build: [PASS or FAIL after the fix]
```
