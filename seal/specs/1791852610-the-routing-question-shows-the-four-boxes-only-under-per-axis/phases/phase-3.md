# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 3be7922b |
| Ran by | unknown — the spawn prompt named no agent or model for this segment; the orchestrator fills this row |

## What this phase was asked

Write the records: `changelog.md` in this directory as a `### Changed`
entry saying what a person sees at the start of a run, which answer now
costs two waits, and that the reader accepts both shapes;
`seal/ledger/1791852610-….md` in one pass from the rows drafted in phases 1
and 2, plus the re-read rows `--reverify --into` writes for the drifted
`seal/releases/0.12.0.md` coordinates; `overview.md`. Verified by
`bin/evidence-check` over the fragment and `bin/unverified-check --baseline
origin/release/v0.21.1`, both exit 0.

## What this phase found

**The fragment was written with placeholder hashes and stamped by the tool.**
The five `Corrected ·` rows and S5 went in with `@00000000` on every
coordinate; `bin/evidence-check --reverify --into <fragment> --checked
2026-10-13` (exit 0) re-stamped them in place, then wrote 22 `Re-read ·` rows,
one per drifted released family, `0 released rows left`. Each of those 22
claims was read against this branch's edits before the run dated them: the
edits to the acts table, `docs/worktree-guard-spec.md` §*Known limits* and
§*Creation consent*, `agents/framer.md`'s diagram, the test cases' stale
lists and the `CLAUDE.md` block touch none of what those claims state.

**`bin/evidence-check --strict` refused the overview once**: it named
the S1 case's old name on the divergence row, a name the tree no longer
carries. The row now marks it `NAME NOT IN TREE`.
After that, `--strict` over every ledger exited 0 (`8482 ok · 0 drifted ·
0 broken`), and `unverified-check` exited 0 with three open rows, each with
its answerer.
