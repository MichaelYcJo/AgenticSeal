# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 3a66113f |
| Ran by | specseal:smith on claude-opus-5-5 |

## What this phase was asked

Phase 1 of the approved `plan.md`, in the worktree on
`fix/905-four-reads-lines-say-refused-where-an-off-shape-line-passes` from
`0d2ca06d`, base `origin/release/v0.21.1` at `321e9de1`, with P1 (a) and
P2 (a) at their defaults. The two stale sentences #834's round 6 deferred
here: ⬜ 4 (`docs/the-reader-registry.md` §*What neither check can read*
names a reader for limit 5 that its own sentence says cannot see the line)
and ⬜ 5 (the recorder's *the strict side*, false since #836). The lead,
limit 5 and the `Enforced by:` line name the warden; the test module's
item 5 says the same; `agents/warden.md` §*Role* gains one sentence telling
the warden to open a helper's line where the diff changes its caller. The
three quoted lines of `spec.md` §*Removes* leave the tree.

## What this phase found

**The frame holds for phase 1, except for what the warden's sentence
drifts.** `plan.md`'s phase-1 row expected `bin/evidence-check .` to name
#835's D1 row as the one DRIFTED anchor. It names thirteen: D1, and twelve
released rows anchored on `agents/warden.md#"## Role"` (in
`seal/releases/0.15.0.md`, `0.15.1.md`, `0.17.0.md`, `0.19.0.md` and
`0.21.0.md`). §*Role* is one heading region of lines 84-397, so any
sentence in it moves every row anchored on the heading. The frame's
`## Data & interfaces` named D1 as the one released row this work moves and
did not count the warden's rows. Phase 3 re-reads all thirteen in this
item's fragment with `--reverify --into`, after reading each row's claim
against the new section; the divergence is in `overview.md`.

**W2 is answered: the sentence is a paragraph of the first bullet, after
the reference-root paragraph.** §*Role* has no paragraph that tells
the warden what to open for a changed unit, and the reference-root
paragraph is the bullet's other instruction to open a coordinate beyond the
diff. Its ledger row in
phase 3 anchors on a quoted line of it, so a later edit elsewhere in
§*Role* does not move it.

**The three `## Removes` clauses are gone.** `git grep -n "the strict side"
-- skills` and `git grep -n "does not show its line" -- docs tests agents`
each exit 1 with no output. The new wording avoids the second phrase on
purpose: limit 5 says the diff "carries no hunk on its line".

**Verification, executed at 3a66113f's tree before the commit.**
`bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py
tests/test_the_recorder_writes_what_its_process_ran.py
tests/test_one_word_one_meaning.py
tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` exit 0,
154 passed. `bin/fold-check --root .` exit 0, 185 statements in 19
documents, none over the ceiling. `bin/evidence-check .` exit 1 (the
lenient reading), 13 drifted, 0 broken.
