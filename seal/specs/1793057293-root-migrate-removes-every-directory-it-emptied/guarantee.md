# Guarantee: 1793057293-root-migrate-removes-every-directory-it-emptied

| Field | Value |
|---|---|
| Target SHA | 285e214d against fa7d1374; earlier run: 9cc6ddc5 withheld |
| Broad gate | f416c213 against fa7d1374 |

`release/v0.22.4` resolved to `fa7d1374` through `release/v0.22.4@{upstream}`
(executed: `git rev-parse --verify --quiet`). `origin/release/v0.22.4` and the
local branch resolve to the same commit. `broad-gate.md` names `f416c213`, an
ancestor of HEAD (executed: `git merge-base --is-ancestor`, exit 0). Two
commits follow it. `9cc6ddc5` touches only `broad-gate.md` and `overview.md`,
and `285e214d` touches only `guarantee.md`, both under this work item's
directory (executed: `git log --no-merges --name-only f416c213..HEAD
^fa7d1374`).

This run audits what changed after the earlier run's target, `9cc6ddc5`.
`git diff --stat 9cc6ddc5 HEAD` lists only `guarantee.md` (executed). So no
coordinate under the earlier run's claims changed, and those claims are
carried below and not re-run. The pull request body was rewritten outside
the tree. This run read it again against the records, the tree and the
issues.

The broad run's kept output was read at
`/var/folders/zl/ljfbytx13tx76ybw21p5nvz00000gn/T/broad-gate-gz1ms_11/`. Its
files name no commit. They were written between 09:26:55 and 09:26:59. That
is after `f416c213` was committed at 09:25:09 and before `9cc6ddc5`, which
records the run at `f416c213`, was committed at 09:27:14. `chain.txt` names
`--baseline fa7d1374` and this worktree as its root. The binding to
`f416c213` is read from those times and is not executed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The cases were committed alone at `db3670d2`, and run 40421812732 ran at `07638965`, which adds only phase 1's record | pull request body *How it was verified*, first row; `phases/phase-1.md` *Commit* row; `plan.md` phase 1 *Status* | `git show --stat db3670d2 07638965`; `git diff --name-only fa7d1374 db3670d2 -- hooks tests`; `git diff --name-only db3670d2 07638965`; `git log -1 07638965^` | holds, executed: `db3670d2` changes only `tests/test_root_migrate.py`, and `hooks/root-migrate.py` is unchanged there. `07638965`'s parent is `db3670d2`. `07638965` adds `phases/phase-1.md` and sets `plan.md` phase 1's *Status* cell to `db3670d2`, so it changes no code. Its commit subject calls both phase 1's record |
| Round 2 found a divergence row quoting frame and docstring text the fix pass had rewritten, and no row for the docstring's second limit, and 3de79fd3 fixed both | pull request body *How it was verified*, *Review* row; `rounds/round-2.md` findings 1 and 2 | `git show 3de79fd3`; `rounds/round-2.md` and `rounds/round-3.md` read | holds, executed and read: finding 1 is the row quoting *In* item 4's old link sentence, which beab5ed4 rewrote, and the docstring that 3fd067a8 changed. Finding 2 is the missing row for the second limit. Both read `verdict: fixed 3de79fd3`. 3de79fd3 changes only `overview.md`: it removes the first row and adds the held-open row. Round 3 confirms both and opens nothing |
| Run 40425810821 at `087d676e` passed every leg, the four Windows groups included, and the commits after it change only records | pull request body *How it was verified*, *CI at the head* row; `overview.md` *Not verified*, first row | `gh run view 40425810821 --json headSha,conclusion,jobs`; `git diff --name-only 087d676e HEAD` | holds, executed: head `087d676e`, conclusion success. Windows groups 1 to 4, macOS groups 1 to 3, ubuntu, lint, both arm-check-grammar legs and durations succeeded, and `release-report` was skipped. After `087d676e`, only `broad-gate.md`, `guarantee.md`, `overview.md` and `rounds/round-3.md` change |
| The broad run at `f416c213`: ruff check and format clean, the suite 6,551 passed and 14 skipped, chain-check exit 0 | pull request body *How it was verified*, last row; `overview.md` *Not verified*, last row | the kept `suite.txt`, `chain.txt` and `mode.txt` read; nothing run (contract rule 2) | holds, read: `suite.txt` runs `uvx ruff check . && uvx ruff format --check . && bin/test -q`, `exit 0`, "All checks passed!", "249 files already formatted", and ends "6551 passed, 14 skipped in 94.94s". `chain.txt` runs `chain_check.py --baseline fa7d1374 --sealing`, `exit 0`. The overview's "BROAD GATE PASSED" is a printed line that no kept file holds, so it stays unverified, and the orchestrator answers it |
| S1 and both S2 rows fail against the walk before the fix, on "the item's directory stayed" | `phases/phase-1.md`, *The cases were seen red against the unfixed hook* | carried from the run at `9cc6ddc5`: `git checkout fa7d1374 -- hooks/root-migrate.py` in a `--no-local` clone, then `bin/test tests/test_root_migrate.py tests/test_tmp_sealer_s3.py -q -p no:xdist -rf` | holds, carried: that run executed it, with exit 1 and 4 failed. Not re-run here, since `hooks/` and `tests/` are unchanged since |
| S2's printed-line assertion fails on its own against the unfixed walk | `phases/phase-1.md`, *Two assertions sit behind another one* | carried from the run at `9cc6ddc5`: base code, S2's directory assertion deleted, `-k resumes_its_item` | holds, carried: that run executed it, and both rows failed on the printed line. Not re-run here |
| S4 passes against the unfixed walk, and is red under the `if True:` mutant | `phases/phase-2.md`, *S4 was green before the fix, and red under the mutant* | carried from the run at `9cc6ddc5`: `-k an_ignored_file_holds_under_any_rmdir` at base code, and again at HEAD code under the mutant | holds, carried: that run executed both, exit 0 at base and exit 1 under the mutant on the `.DS_Store` assertion. Not re-run here |
| #1018's merge leaves neither the item's directory nor `specs/`, though S3 was deleted as a case | `overview.md`, the S3 divergence row; #1018 *Done when* | carried from the run at `9cc6ddc5`: S3's deleted text as a `test_tmp_*` probe, at HEAD and at base code | holds, carried: that run executed it, passing at HEAD and failing at base on "the item's directory stayed". Not re-run here |
| The two modules pass at the head, 78 cases | `rounds/round-2.md` *Probes* | carried from the run at `9cc6ddc5`: `bin/test tests/test_root_migrate.py tests/test_the_root_migrates_itself.py -q -p no:xdist` | holds, carried: that run executed it, exit 0 and 78 passed. Not re-run here |
| Run 40421812732 at `07638965` failed exactly S1, both S2 rows and S3 on ubuntu, macOS and Windows, and the overview case | `questions.md` Q1 *Status*; pull request body *How it was verified*, first row | carried from the run at `9cc6ddc5`: `gh run view 40421812732 --log-failed` | holds, carried: that run executed it, and those five cases were the only failures. Not re-run here |
| Every `## Removes` row is gone from the tree | `spec.md` *Removes* | carried from the run at `9cc6ddc5`: `git grep` for each row's text | holds, carried: that run executed it with no hit, and no tracked file outside this work item changed since |
| The mutation batches went red: phase 2's 3 mutants, and rounds 1 and 2's 5 | `phases/phase-2.md`; `rounds/round-1.md` finding 1; `rounds/round-2.md` *Probes*; pull request body *Mutation* row | none re-run | read: only S4's own mutant was re-run, by the earlier run. The batches are the smith's and the warden's account, unverified here, and the warden's record answers them |
| The two Windows limits, the junction and the held-open directory | `hooks/root-migrate.py` `move` docstring; `overview.md` *Not verified* rows 2 and 3; pull request body *Left open* | none | unverified: nobody ran them on Windows. The repository owner answers, as `overview.md` names |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `move`'s walk lists each directory again when it reaches it; S1 to S4; one limit sentence; four `Removes` rows | both issues' *Done when*; the tree for every `Removes` row | the build on S3 and on a second limit sentence. `overview.md` *Where spec and implementation diverged* records both, with grounds, so neither is an unrecorded departure |
| the build | `hooks/root-migrate.py` takes the fresh `os.listdir`; S1 and S2 are rewritten; S4 is added; S3 was deleted after round 1; the docstring states two limits | the issues, the spec's design, both CI runs and every claim above | none |
| the last round | round 3 confirms round 2's two fixes, opens nothing, and leaves the Windows limits and Q2 to the owner | the tree at `087d676e`; `overview.md`; 3de79fd3's diff | none |
| the changelog | `changelog.md`: both cases fixed, the notice no longer names the moved item, an ignored file keeps its directory, and three limits | the docstring word for word on the two Windows limits; `spec.md` *Out* on the migrated repository; the pull request body's *Limits* section | none |
| the pull request body | `Closes #1016` and `Closes #1018`; the before and after table; the three limits; *How it was verified*; Q2 under *Decisions left open*; the Windows limits and `.test_durations` under *Left open* | the issues, the diff, the changelog, `questions.md` Q2 and its default (a), `overview.md` *Not done*, both CI runs, the kept broad-run output, `phases/phase-1.md`'s *Commit* row and `rounds/round-2.md` findings 1 and 2 | none. The two sentences the earlier run withheld over now read as that run asked, and both hold against the tree |

Verdict: sealed
