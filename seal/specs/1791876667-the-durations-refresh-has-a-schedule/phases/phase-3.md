# 1791876667-the-durations-refresh-has-a-schedule — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 68c162e0 |
| Ran by | specseal:smith on Opus 5.5, as `routing.md` and `handoff.md` name it |

## What this phase was asked

Write the records, the last phase. The ledger fragment with S1–S8
anchored to units and tests; re-reads of `test.yml#"pytest:"`,
`CONTRIBUTING.md#"## Running the checks"` and
`docs/release-checklist.md#"## 0. Before starting"`; `Corrected ·` rows for
1791852613's S1, S2 and S4 and for 0.21.0's S5 quoted line, which covers the
0.21.1 S4 row `survivors.md` names; the changelog fragment; `overview.md`
closed. Leave `evidence-check --strict .` and the lenient run both at exit
0. #930 (#938) lands first and adds `seal/budgets.md`'s `## Price level`
row, which a pull request that changes `.test_durations` sets to the ratio
its budget step reports. That cannot be done before the rebase, so it is
written down for it, and `REMEDY` and the recipe name it only if it reads
true on this branch now, which it does not.

## What this phase found

- **Nineteen released rows, not sixteen.** `evidence-check --reverify`
  without `--into` named 19 released rows whose coordinates the branch
  drifted: `CONTRIBUTING.md#"## Running the checks"` in rows from 0.8.2,
  0.10.0, 0.15.1, 0.15.3, 0.20.0 and 0.21.0, the section's two quoted lines,
  `docs/release-checklist.md#"## 0. Before starting"` in 0.11.1 and 0.18.0,
  `test.yml#"pytest:"` and `#"on:"`, and the T2 case; `--strict` counted 60
  drifted coordinates across them. The spawn's 16 is a figure this phase
  did not reproduce, and where it came from was not read. Each
  claim was read in full against the tree before any row was dated. Fifteen
  hold. Two do not, and take the corrections below: 0.21.1's S4 (the file
  refreshed at each release's preparation by a 60-minute measuring leg, and
  the checklist box) and 0.21.0's S5 (the refresh as a Windows-only run with
  the macOS shard times read again after it). 0.21.1's S1 and S2 had not
  drifted, because they cite tests that still exist, but their claims went
  with the code — one measuring job, one direction — and take corrections
  too. `--reverify --into` then wrote 17 `Re-read ·` rows. It wrote an
  eighteenth for 0.21.1's S4 because the first spelling of that row's
  citation, `"S4 ·"`, sits on two lines of its section; that row was
  removed when the `Corrected ·` row's citation was lengthened.
- **A row holds a test or a code coordinate, never both.** The first draft
  mixed them, and the checker refused all ten mixed rows as `MALFORMED`
  (`docs/the-evidence-ledger.md` §*A claim held by a test*). S1–S7 and C1
  are now held by their tests alone, each seen red through `mutation-check`
  in phases 1 and 2, and the corrections of S1, S2 and S4 cite the released
  row and name the tests. The correction of 0.21.0's S5 stays hashed: no
  test holds what the workflow comments say.
- **S8 is no row.** It claims the fragment and the checker's exit, and a row
  grounded in this work item's records would break when `settle` retires
  the directory. Its evidence is the exit codes below; `overview.md` names
  the divergence.
- **The records arm reads this work item once it has a fragment.** With the
  fragment in place, `evidence-check` read the work item's names and
  refused 14: `plan.md`'s test rows named the cases without their `test_`
  prefix, and three lines meant the two names never built (T2's and T8's
  plan names). The test rows now carry the names the tree has, and the three
  lines carry `NAME NOT IN TREE`. The four `## Removes` texts are gone from
  `CONTRIBUTING.md` and `docs/release-checklist.md` (`grep -c -F`, 0 each).
- **The price level waits for the rebase.** Under #930's design this
  branch's union reads 1.0706 against the file it replaced, so
  `seal/budgets.md`'s `## Price level` is about 1071 once #930 is under it.
  `overview.md`'s Not done carries it for the session that rebases.

`executed` 2026-10-14:

- `evidence_check.py --strict .`: exit 0, 9,062 ok, 0 drifted, 0 broken, 0
  malformed; the records arm 1 work item read, 85 names, 0 refused. The
  lenient run: exit 0. Test rows were read for existence alone; the sealed
  run's record is the sealer's.
- `unverified_check.py --baseline origin/release/v0.22.0`: exit 0.
- `correction-check --range origin/release/v0.22.0...HEAD`: exit 0, no
  released ledger file changed.
- `bin/test tests/test_docs_line_wrap.py tests/test_release_hygiene.py
  tests/test_a_phase_hands_the_next_one_a_record.py
  tests/test_the_changelog_is_gathered_at_release.py
  tests/test_the_ledger_fragments_fold_at_release.py
  tests/test_a_record_says_what_ran_it.py -q`: exit 0, 285 passed.
