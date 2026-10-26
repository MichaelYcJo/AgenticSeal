# Phase 1: 1792973486-a-change-only-the-shell-makes-is-a-chore

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 77761ea9 |

## What this phase was asked

Build row 1 of `plan.md` *Phases*. Insert the two sentences of `spec.md` *Scope* item 1, word for word, into `CLAUDE.md` *The rule a mechanism is kept against*, directly after its first sentence, which ends `existing is no reason to keep it.`. Reflow that paragraph's lines, and change no other word and no other file. Where the frame and the tree cannot both hold, write a divergence row in `overview.md`. Edit `spec.md`, `plan.md` and `questions.md` only in row 1's Status cell. Verify with the word diff against `61a8455a` (S1), the `git grep` for `only such a change passes through` (S2), the five test modules row 1 names (S5) and `bin/rules --check`. Write `changelog.md` only if `skills/implement/SKILL.md` asks a fragment of a change to `CLAUDE.md` alone.

## What this phase found

**The frame holds.** The section's first sentence still ends `existing is no reason to keep it.` on `CLAUDE.md:17`, the paragraph runs from line 16 to line 30, and it holds no `check:` line (read, at `5b5c3088`). No divergence row was needed, so no `overview.md` was opened.

**The S2 grep decides one line break.** `git grep` matches within one line, so the phrase `only such a change passes through` has to sit whole on one line of `CLAUDE.md`. A greedy wrap at the paragraph's width splits it after `such a` at every width from 76 to 78 (executed, with Python's `textwrap`). The reflow keeps the phrase whole, which leaves the line before it short: `outside that work, so a gap in a gate or a check that`. The reflow runs from line 17 to line 25, and the paragraph's last five lines keep their old breaks. No line is wider than 77 columns.

**The insertion is exact.** With whitespace collapsed, the paragraph at `61a8455a` with the two sentences inserted after the anchor equals the paragraph in the tree (executed). `git diff --word-diff 61a8455a -- CLAUDE.md` shows five `{+ +}` runs and no `[- -]` run (executed).

**No changelog fragment.** `skills/implement/SKILL.md` names `changelog.md` only in *5. Incorporate review*, for a fix that changes what the work item ships, and asks nothing of a change to `CLAUDE.md` alone (read). `plan.md` row 1 names no fragment either. Two other places name the builder as the fragment's writer: `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along* says the build's last phase writes it, and `skills/code-review/orchestration.md` (line 178) says the party that builds the work item writes it before the broad run (read). This phase is the build's last phase, so the orchestrator decides whether this work item carries a fragment before the broad run.

**Checks, executed.**

- S1: the word diff above.
- S2: `git grep -n 'only such a change passes through' -- ':!seal/specs/'` finds `CLAUDE.md:21` alone.
- S5: the five modules row 1 names: 109 passed. With `tests/test_docs_line_wrap.py` added: 148 passed.
- `bin/rules --check`: all 249 check lines in 62 rule files hold.

No case was written and no `mutation-check` ran, because the phase adds prose and no unit (`spec.md` *Scope* item 2 gives the sentences no `check:` line).
