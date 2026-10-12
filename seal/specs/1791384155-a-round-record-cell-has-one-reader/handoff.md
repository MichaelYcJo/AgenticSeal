# 1791384155-a-round-record-cell-has-one-reader — handoff

## State (2026-10-12) — read this first

- All seven phases are closed at f8d134de. Phase 5's `wip:` commit e682fe84 was verified again after the resume and left as it is.
- Next: the draft PR and round 1.
- Before the seal, merge `release/v0.21.0` again. The release branch's own 33 drifted rows make `evidence-check --strict` exit 2 here, and #836's branch clears them.
- Write and close records with the installed 0.20.0 `round_record.py --root .`, not the tree's copy.

Written 2026-10-08 by the orchestrating session, for a session on another
machine. The whole run's state, the owner's batch and the starting notes are
in `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md`
on branch `chore/834-every-reader-and-record-is-inventoried`; read it first.

| | |
|---|---|
| Issue(s) | #866 |
| State | framed by `framer` on Fable 5.1; `routing.md` answered `automation`; no smith spawned; `plan.md` not approved |
| Owner's questions | None for a person. |
| Build order | Shares `round_record.py`/`chain_check.py` with #837 and #860, and `broad_gate.py` with #869; build after #837 and #860. Its frame counts 172 released ledger rows on the units it edits. |

**Next act:** the owner's answers to every open row of the run, asked
together in one call; then fill `plan.md`'s `Approved <date> by <who>` line
and spawn smith on this branch. In a fresh worktree, run tests with
`bin/test <files>`; `uv run --frozen pytest` cannot start pytest there.
