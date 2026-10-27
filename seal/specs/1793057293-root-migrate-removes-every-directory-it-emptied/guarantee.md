# Guarantee: 1793057293-root-migrate-removes-every-directory-it-emptied

| Field | Value |
|---|---|
| Target SHA | 9cc6ddc5 against fa7d1374 |
| Broad gate | f416c213 against fa7d1374 |

`release/v0.22.4` resolved to `fa7d1374` through `release/v0.22.4@{upstream}`.
`broad-gate.md` names `f416c213`, an ancestor of HEAD. The one commit after
it, `9cc6ddc5`, touches only `broad-gate.md` and `overview.md` under this
work item's directory (executed: `git log --no-merges --name-only
f416c213..HEAD ^fa7d1374`). The suite counts the pull request body and
`overview.md` quote from that run are not in `broad-gate.md`, so they are
`unverified`, and the orchestrator answers them. The record itself is written
only on a pass (read: `skills/verify/scripts/broad_gate.py`, the `--record`
paragraph of its docstring).

Every re-run below ran in a `git clone --no-local` of the branch at
`9cc6ddc5`, under the scratchpad's `at-base/`, which was removed afterwards.
The tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 and both S2 rows fail against the walk before the fix, on "the item's directory stayed" | `phases/phase-1.md`, *The cases were seen red against the unfixed hook* | `git checkout fa7d1374 -- hooks/root-migrate.py` in the clone, then `bin/test tests/test_root_migrate.py tests/test_tmp_sealer_s3.py -q -p no:xdist -rf` | holds, executed: exit 1, 4 failed and 70 passed. The failures were S1, both S2 rows and the S3 probe, each on "the item's directory stayed" |
| S2's printed-line assertion fails on its own against the unfixed walk | `phases/phase-1.md`, *Two assertions sit behind another one* | the clone at base code, with S2's directory assertion deleted, `bin/test tests/test_root_migrate.py -q -p no:xdist -rf -k resumes_its_item` | holds, executed: exit 1, both rows failed on the line "left specs/1788000002-one-mark where it is (no routing.md or rounds/ that git tracks — not a SpecSeal work item)" |
| S4 passes against the unfixed walk | `phases/phase-2.md`, *S4 was green before the fix* | the clone at base code, `bin/test tests/test_root_migrate.py -q -p no:xdist -k an_ignored_file_holds_under_any_rmdir` | holds, executed: exit 0, 1 passed |
| S4 is red under the mutant that replaces the fresh listing with `if True:` | `phases/phase-2.md`, *S4 was green before the fix, and red under the mutant* | the clone at HEAD code with `if not os.listdir(here):` replaced by `if True:` (one match asserted), `bin/test tests/test_root_migrate.py -q -p no:xdist -rf -k an_ignored_file_holds_under_any_rmdir` | holds, executed: exit 1, the `.DS_Store` assertion failed |
| #1018's merge leaves neither the item's directory nor `specs/`, though S3 was deleted as a case | `overview.md`, the S3 divergence row; #1018 *Done when* | `tests/test_tmp_sealer_s3.py`, round 1's deleted S3 text, run at HEAD and at base code in the clone, then deleted | holds, executed: exit 0 at HEAD, 1 passed; at base it failed on "the item's directory stayed" |
| The two modules pass at the head, 78 cases | `rounds/round-1.md` finding 1 *answer*; `rounds/round-2.md` *Probes* | `bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py -q -p no:xdist` in the clone at HEAD | holds, executed: exit 0, 78 passed |
| Run 40421812732 at `07638965` failed exactly S1, both S2 rows and S3 on ubuntu, macOS and Windows, and the overview case | `questions.md` Q1 *Status*; `phases/phase-2.md` *Q1 is answered (a)* | `gh run view 40421812732 --json headSha,conclusion` and `--log-failed`, the FAILED lines counted | holds, executed: head `07638965`, failure; each of the four cases and `test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed 3 times, in ubuntu, macOS groups 1 and 2, and Windows groups 2 and 3; nothing else failed |
| Run 40425810821 at `087d676e` passed every leg | `overview.md` *Not verified*, first row; pull request body *How it was verified* | `gh run view 40425810821 --json headSha,conclusion,jobs` | holds, executed: head `087d676e`, success; every pytest, lint, arm-check-grammar and durations job succeeded, `release-report` skipped |
| Every `## Removes` row is gone from the tree | `spec.md` *Removes* | `git grep` at HEAD for `if not dirs and not files`, "The empty directories left behind are removed", "The walk removes each emptied directory below the item", `iterdir()) == []`, `ONE_MARK / "rounds").exists()`, and `merged_into_one_that_exists` over `tests/` and `.test_durations` | holds, executed: no hit for any of them |
| The mutation batches went red: phase 2's 3 mutants, rounds 1 and 2's 5 | `phases/phase-2.md`; `rounds/round-1.md` finding 1; `rounds/round-2.md` *Probes* | none re-run | read: S4's own mutant is re-run above; the batches are the smith's and the warden's account, unverified, answered by the warden's record |
| The two Windows limits, the junction and the held-open directory | `hooks/root-migrate.py` `move` docstring; `overview.md` *Not verified* rows 2 and 3 | none | unverified: nobody ran them on Windows; the repository owner answers, as `overview.md` names |
| The broad run's counts: ruff clean, 6,551 passed and 14 skipped, chain-check exit 0 | pull request body *How it was verified*, last row; `overview.md` *Not verified*, last row | none (contract rule 2) | unverified: `broad-gate.md` holds the commit and base and no counts; the orchestrator answers |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `move`'s walk reads each directory again when it reaches it; S1 to S4; one limit sentence; four `Removes` rows | the issues' *Done when* for both shapes; the tree for every `Removes` row | the build on S3 and on a second limit sentence. Both are recorded in `overview.md` *Where spec and implementation diverged*, with grounds, so neither is an unrecorded departure |
| the build | `hooks/root-migrate.py` takes the fresh `os.listdir`; S1 and S2 rewritten; S4 added; S3 deleted after round 1; the docstring states two limits | the issues, the spec's design, the CI runs and every re-run above | none |
| the last round | round 3 confirms round 2's two fixes, opens nothing, and leaves the Windows limits and Q2 to the owner | the tree at `087d676e`; `overview.md` | none |
| the changelog | `changelog.md`: both shapes fixed, the notice no longer names the moved item, an ignored file keeps its directory; three limits | the docstring word for word on the two Windows limits; `spec.md` *Out* on the migrated repository; the S2 re-run on the notice | none |
| the pull request body | `Closes #1016` and `Closes #1018`; the before and after table; the three limits; *How it was verified*; Q2 under *Decisions left open* | the issues, the diff, the changelog, `questions.md` Q2 and its default (a), both CI runs | the tree and the records on two sentences of *How it was verified*: its first row, "committed alone at `07638965`", and its *Review* row, "Round 2 found two rows of the closing memo's divergence table that the fix pass left out of step" |

The two sentences of the pull request body that do not hold:

- **First row, "committed alone at `07638965`".** The cases were committed in
  `db3670d2`. `phases/phase-1.md` gives its *Commit* row as `db3670d2`, and
  `plan.md` phase 1's *Status* cell says the same. `git show --stat 07638965`
  shows that commit changes only `phases/phase-1.md` and `plan.md`. The CI run
  was at `07638965`, so the run's commit is right and the commit named for
  the cases is wrong.
- **Review row, "two rows ... left out of step".** Round 2 found one row that
  quoted frame and docstring text the fix pass had rewritten (finding 1). It
  also found a row missing: the docstring's second limit had no divergence
  row (finding 2). One row was out of step and the other did not exist.

Verdict: withheld reason: the pull request body, the file the orchestrator wrote, makes two claims the records contradict. In its *How it was verified* table, first row, change "committed alone at `07638965`; the branch's `tests` run 40421812732 there failed" to "committed alone at `db3670d2`; the branch's `tests` run 40421812732 at `07638965`, which adds only phase 1's record, failed" (`phases/phase-1.md` *Commit* row; `git show --stat 07638965`). In its *Review* row, change "Round 2 found two rows of the closing memo's divergence table that the fix pass left out of step." to "Round 2 found that the closing memo's divergence table kept a row quoting frame and docstring text the fix pass had rewritten, and had no row for the docstring's second limit; 3de79fd3 fixed both." (`rounds/round-2.md` findings 1 and 2). Nothing in the tree changes; the re-audit reads the body again
