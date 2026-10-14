# 1791940762 — handoff

Written 2026-10-14 by the orchestrating session (Opus 5.5) at a pause the owner asked for. Delete this file when the next session has read it. `plan.md` Status and `phases/phase-7.md` hold what was built; this file holds only what the next session does first.

## Where it stands

- Phases 1–7 are built and pushed (tip 3139f88d). Phase 6 moved the kernel to `skills/verify/scripts/coordinates.py`. Phase 7 removed what stood on the ledger, and the pact's change-record half (Q2, owner: remove).
- No pull request is open yet.

## Next, in order

1. **Owner's Q3** (`questions.md`): `Pact notify` now decides nothing. Phase 7 kept it and reworded its text to "printed, acted on by nothing", which leaves a value standing on the removed fact. Put the recommendation to the owner as **2. Remove `Pact notify` and the one-spelling machinery, measured first against what #759's rule caught**, because "keep" rests on nothing the tree still does. Build the answer before review.
2. **Open the pull request** into `release/v0.22.0` (squash, `Closes #944`). Read `commit-pr-convention` first and compare against `gh pr list`.
3. **`.test_durations`**: phase 7 deleted 457 priced cases, so 609 of 11,810 (5.16 %) are unpriced, over the 5 % `STALE_SHARE`. Refresh it from the PR run's Windows `test-durations` artifact by `CONTRIBUTING.md`'s refresh procedure. The refresh's `--clean-durations` also drops the ~37 ledger ids nothing collects.
4. Spawn `warden` (Opus 5.5) against `origin/release/v0.22.0`, with its report in **this worktree's** `rounds/`. Then the sealer (Sonnet 5.5). Then merge.
5. After the merge: rebase #929 and #931 onto it, and run each one's verification round (see their handoffs and plans).

## Left on purpose, with the premise checked

- `tests/test_release_hygiene.py::test_a_planted_ledger_file_is_named` stays while an open branch carries `seal/ledger/<id>.md` (#937, #939): such a file re-enters at merge without a conflict. Once both have rebased onto this item, nothing carries one. Remove the guard then, in whichever of the two merges last.
- About 40 test fixtures and comments still say "ledger". Phase 7's grep excluded `tests/`, so they are #942's to sweep when it rebuilds those modules.
