# 1791779434-under-automation-the-guard-asks-nobody — handoff

Written 2026-10-12, evening KST, by the orchestrating session, when the owner
stopped for the day. The whole run's state is in
`seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md` on
branch `chore/834-every-reader-and-record-is-inventoried`; read it first.

| | |
|---|---|
| Issue(s) | #894 |
| PR | #897, draft, labels `chain: reframed` and to add: `chain: capped` |
| State | Reframed after round 3: the deny states only what the guard read and what the guard does. Rounds 4–6 reviewed the redesign. Round 6 (5356b8a6) found nothing to fix and capped the run, with four ⬜ notes open. `origin/release/v0.21.0` (dae101ab, #835 landed) is merged in at 1762901d. |
| Last commit | 35c0cade: `hooks/worktree-guard.py#main` declares its `Reads:` line and leaves the census, because #835's rule refused it after the merge. The smith was stopped before re-reading the ledger rows this drifts. |
| Owner's questions | P1, P2 and P3 at default (a); none blocks. |

**Next act, in order:**

1. **Re-read the drifted ledger rows.** `bin/evidence-check . --strict` exits 2
   with `hooks/worktree-guard.py#main` DRIFTED in several families. That is
   only the docstring line 35c0cade added. Read each claim, then run
   `bin/evidence-check --reverify --into seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md --checked <date>`
   for released rows, and `--reverify` in place for live-fragment rows.
2. **Close round 6's four notes**, in `rounds/round-6-report.md`:
   - ⬜ 3: the Korean full-text case for the deny issued via `git -C`.
   - ⬜ 4: a case that checks the index-residue note under the press.
   - ⬜ 2: correct `spec.md:168` and `overview.md:23`.
   - ⬜ 1: the heading *Why the reason predicts nothing*. Rename it and re-read the six `## Decision matrix` rows, or answer it.

   Write `rounds/round-6-fixes.md` with one `## Fixes` row per ⬜. The installed 0.20.0 generator wants a row for a ⬜, as `answered — corrected at <sha>`. Close it with the installed `round_record.py close --range 5356b8a6..<last>`.
3. Add the `chain: capped` label, run `bin/broad-gate --preflight --base origin/release/v0.21.0`, then spawn the sealer. Commit the `Broad gate` cell.
4. Write the PR body (writing-style), then land with `gh pr ready`, wait for checks, and `gh pr merge --squash --match-head-commit <sha>`.

**Watch for:**
- Run `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` and `tests/test_the_printed_ledger_name_is_the_file_that_was_read.py` beside the nine guards. Narrow runs missed them on #835.
- `round-record new` drops hand-added `NAME NOT IN TREE` markers (#899). After `new`, re-add them on the rows naming `test_a_creating_switch_under_the_press_takes_the_stash_way` and `test_an_orphan_switch_under_the_press_takes_the_commit_way`.
- #896 lands after this item, and copies the press sentence byte for byte. Do not change that sentence.
