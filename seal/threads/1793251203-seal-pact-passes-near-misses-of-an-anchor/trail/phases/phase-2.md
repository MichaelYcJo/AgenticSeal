# Phase 2: 1793251203-seal-pact-passes-near-misses-of-an-anchor

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 063644e5 |

## What this phase was asked

Build phase 2, the inline token, after phase 1, and commit it with this
record and its Status cell. S6's new ids are seen red against `28edee12`,
as the plan's *Verified by* cell states, and the phase runs the command
that cell names.

## What this phase found

**The frame holds for this phase.** `frame/design.md` *Data & interfaces*
gives the pattern, and it is built as written. The `INLINE` sentence is
unchanged.

**S6 is six ids on the existing case.**
`test_refuses_the_inline_anchor_naming_the_row_to_write` gained `PACT:abc`,
`Pact:abc` and `PACT:orders-api/"## A"@1a2b3c4d`, each once in a table cell
and once in prose.

**S7's spellings are in the passes case.** `pact: abc` and `pact :abc` were
added to the prose line that already held `Read the pact: it is short.`.
They are refused by no build of the token, so they pin the limit and were
not seen red. The space limit is the pattern's `(?=\S)`, which predates this
work and so owes no mutation run.

**The token's texts, rewritten in place.** The comment above `INLINE_TOKEN`
states the case fold and the space limit. The module docstring's token
sentence now stands in a paragraph of its own and says the same. A
`git grep` outside `docs/` and `seal/threads/` for the token's other
statements found none. `docs/the-pact.md` is changed by the design's
`## Rule changes`, not in this diff.

**Red first, executed.** In a `git clone --no-local` of the worktree at
`28edee12`, with this phase's test module copied in, the six new ids failed
with exit 0 where 2 was expected. The passes case passed there. The clone
was removed before hand-back.

**Mutation, executed.** `seal mutate` dropped `re.IGNORECASE` from
`INLINE_TOKEN`, and the result was `red` against
`test_refuses_the_inline_anchor_naming_the_row_to_write`.

**Phase boundary, executed.** The command was the same eleven-module
`bin/test` command as phase 1. It counted 1017 passed, 8 skipped and 1
failed. The failure is the census of `frame/design.md` line 49 that phase
1's record names. It fails at the frame commit too.
