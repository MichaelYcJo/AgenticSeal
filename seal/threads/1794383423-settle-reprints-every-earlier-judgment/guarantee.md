# Guarantee: 1794383423-settle-reprints-every-earlier-judgment

The audit read the tree at `254d9a27a` against `957a3bc7d`. That commit is
what `release/v0.37.4@{upstream}` and `origin/release/v0.37.4` resolve to.
The local `release/v0.37.4` stands at `18a7e18fb` and was not used. Every
re-run went to a `git clone --no-local` of the branch at `254d9a27a` under
the sealer's scratch directory, `sealer/at-base/`. Where a case was run
against older code, `skills/settle/scripts/settle.py` alone was restored
there from the named commit, and HEAD's file was restored after each run.
`git status --short` was clean after every restore. "git 2.39.3" means
`/Library/Developer/CommandLineTools/usr/bin/git`, reached through a scratch
directory that holds only a link to it, placed first on `PATH`. Every other
run used git 2.50.1.

The issue body is #1481 (executed: `gh issue view 1481`). It asks for three
things. A default `seal settle` whose output size and git-call count do not
grow with the number of releases. A default run here that finishes under
2 s. And `skills/settle/SKILL.md` step 5 stating the bound.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad gate ran at a commit that only this work item's records follow | `trail/gate.md:4` (`run: 84ac67961 against 957a3bc7d`) | `git merge-base --is-ancestor 84ac67961 HEAD`; `git log --no-merges --name-only 84ac67961..HEAD ^957a3bc7d` | holds (executed). The commit is an ancestor of HEAD. Only `254d9a27a` follows it, and that commit touches `trail/gate.md` alone. |
| The body file's records part is the records' own text, and its first part is `pr.md` | the body file `pr-body.md` | `seal pr-body <item> --body <file> --check`, run with the installed 0.37.3 copy and with the tree's `bin/seal` | holds (executed). Both copies exited 0 with `matches:`. |
| S4 was seen red against the per-plan reads | `trail/phases/phase-1.md:28-30` | `settle.py` from `957a3bc7d`; `bin/test tests/skills/test_settle.py -q -p no:xdist -k test_the_git_calls_do_not_grow_with_the_plans_read` | holds (executed). It failed with `assert 14 == 8`, the figures the record gives. |
| S6 was seen red at the base, and again with only its guard removed | `trail/phases/phase-1.md:31-36` | the same case filter, first at `957a3bc7d`'s `settle.py`, then at HEAD with only `if text is None:` before `NO_PLAN_TEXT` replaced by `if False:` | holds (executed). At the base it failed on its sentence line, with `git show`'s `bad object`. With the guard removed it failed with `TypeError` at `lib/blocks.py:395`, where `plan_rows` was handed `None`. |
| S1 was seen red, and again with only the bound removed | `trail/phases/phase-2.md:94-102`, and `:114`, the mutation table's first row | the S1 case at `957a3bc7d`'s `settle.py`; then at HEAD with only `if not every and len(removing) > EARLIER_WINDOW:` replaced by `if False:` | holds (executed). Both runs failed on the section's text. Each printed the oldest removing commit's row and no line counting older commits. |
| S2 and both parameters of S3 were seen red | `trail/phases/phase-2.md:94-101` | the S2 and S3 cases at `957a3bc7d`'s `settle.py` | holds (executed). All three failed with `SystemExit: 2`, because the parser does not know `--all-earlier`. |
| Round 1 finding 1, `fixed 0a354b5a7`: the nested-tag case fails before the fix on git 2.39.3 and passes after it | `trail/rounds/round-1.md` finding 1's close block; `gaps.md` *Not verified*, the closed row | `Test_versions::test_accepts_a_version_tag_of_a_tag_at_the_commit_it_peels_to` at `452d08a3d`'s `settle.py` on git 2.50.1 and on git 2.39.3; then at HEAD on git 2.39.3, run together with the batch and newline cases | holds (executed). At `452d08a3d` the case passed on 2.50.1 and failed on 2.39.3 with `'v0.2.0' == 'v0.1.0'`. At HEAD on 2.39.3, 14 cases passed. |
| Round 1 finding 2, `fixed 0a354b5a7`: a plan whose path holds a newline no longer shifts the batch | `trail/rounds/round-1.md` finding 2's close block | `test_a_removed_plan_whose_path_holds_a_newline_is_named_and_the_rest_read` at `452d08a3d`'s `settle.py`; then at HEAD with only `return [], split, older` replaced by `return [], [], older` | holds (executed). At `452d08a3d` the `[beside]` run named the plain plan with `name/frame/plan.md missing`, and both parameters failed. At HEAD with that line changed, `[alone]` failed with `IndexError` in `earlier_block`: the section was never printed, so nothing named the plan. `[beside]` passed in that run. |
| Round 2 finding 1, `fixed 05394cbca`: round 1's close of finding 2 names the commit that changed its location | `trail/rounds/round-2.md` finding 1's close block, which no round read | `git show 05394cbca`; read `trail/rounds/round-1.md:192` at HEAD; `python3 skills/code-review/scripts/chain_check.py --baseline 957a3bc7d --root <worktree> --worktree` (the tree's copy) | holds. `05394cbca` changes `round-1.md` alone. At HEAD, line 192 reads `verdict: fixed 0a354b5a7`, which is the line the finding asked for, and the answer line is unchanged (read). The chain check exited 0. It named only the missing `guarantee.md`, and no line of `frame/design.md` *Rule changes* (executed). |
| S7 and the changelog's figures. 25 git calls with or without `--all-earlier`. A section of 47,844 B. A line counting 8 older commits. Under 2 s | `trail/phases/phase-2.md:129-148`; `changelog.md:3-4` | `python3 -I test_tmp_s7.py <clone> 18a7e18fb`, which wraps `subprocess.run` and runs `settle.main` twice in each form | holds (executed). Each run made 25 calls. The dry run took 0.53 s and 0.51 s. Its section body was 47,844 B, its removing commits were `8657297d (#1495)` and `e5370691 (#1466)`, and its last line was "8 older commits removed plans this section did not read; `seal settle --all-earlier` reads them". `--all-earlier` took 0.72 s and 0.73 s, gave a 247,301 B body, named the seven removing commits, and printed no count line. The changelog's 0.56 s and 0.53 s are the fix pass's own runs. These runs did not reproduce those two figures, and the times above stand beside them. |
| *Done when*: a default run in this repository finishes under 2 s | issue #1481 *Done when*, item 2 | `bin/seal settle` in the clone, at the default `--released-at origin/main` (`18a7e18f` there), timed twice | holds (executed). Both runs exited 0, in 0.64 s and 0.63 s, and printed 108,756 B with nothing on stderr. |
| The old reading made 422 git calls | `changelog.md:4`; `trail/phases/phase-1.md:19-20` | the same probe, at `d2040b335`'s `settle.py`, `--released-at 18a7e18fb` | holds (executed). It made 422 calls in 7.86 s, where the record has 8.40 s; time varies from run to run. |
| Rows printed for the same plans are byte-identical to the old reading's | `frame/design.md` *Scope* item 4 | `diff` of `settle.py --released-at 18a7e18fb` at `d2040b335`'s script against HEAD's with `--all-earlier` | holds (executed). Only the heading differs (old lines 399-403, new lines 399-405). |
| The two narrow modules pass at HEAD | `trail/rounds/round-2.md` *Probes*, row 1 | `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py -q` | holds (executed). 233 passed. |
| Every `## Removes` row of the design, and every removal the changelog names, is gone from the tree | `frame/design.md` *Removes*; `changelog.md:4` | `git grep` at HEAD for `def version(`, `version(root`, `--contains` under `skills/settle`, `lib` and `.github/scripts`, `"show"` in `settle.py`, `every row of every` and the old bullet's sentence under `skills/settle`, the three `from` passages under `docs`, and the `show` and `tag` parameters in `test_settle.py` | holds (executed). There is no `version` reader. The one `tag --contains` hit is a docstring. The one `"show"` call is `notes` reading a changelog fragment, not the earlier section. The skill bullet has been rewritten. The failure case's parameters are the six batched calls (`test_settle.py:1653-1666`). The three `docs/` passages still stand, as the *Removes* table says they do. They are written by `## Rule changes` at the settle after the release, and the chain check named none of them. |
| The full suite, the repository-wide lint and the format check pass | both phase records, *The phase boundary run*, labelled `unverified` | not run (contract rule 2) | read. `trail/gate.md` records that the `Broad gate` command passed at `84ac67961`, the merged tree that HEAD differs from by `trail/gate.md` alone. |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | By default, read the plans the two newest removing commits deleted, and close with a line that counts the older commits. `--all-earlier` reads every plan and is refused beside `--apply` and beside `--draft`. Every read is batched: one `cat-file --batch`, one `log` of adds, and three tag calls with a `^{}` peel. `version` goes. Step 5 states the bound. Three `docs/` passages change at the settle | The issue's three *Done when* items, all re-run above. The diff of `settle.py`, `skills/settle/SKILL.md` and `tests/skills/test_settle.py` (read). The phase records. The changelog | none that the issue body or the tree decides. Read: round 2 notes one edge where a batched read fails after a newline path was split off (`settle.py:1364`). There the section prints only the failure line, so that plan goes unnamed, although *Scope* item 6 says such a plan is named "before the batch". The sentence after it in the same item says a failed batched read is named once and no row of the plans it would have read is printed. The code follows that sentence, and the failure line already tells the session that no plan in the window was read. The settling session's next act is the same either way, so no defect is opened here |
| the build | The two phase records, fix pass 1 (`0a354b5a7`, `c719f1de8`), the framer's fold `8c1eb676f`, and `05394cbca`. Each phase that has a commit in `frame/plan.md` *Phases* (`bc5f349c6`, `c89db956f`) has its record under `trail/phases/`. The departures the records name, `version` removed and `blobs` returning a list, were folded into the frame | The design. Every sampled `seen red` and `executed` claim above. The routing row `Implementation: crafter` | none |
| the last round | Round 2 confirms round 1's three fixes and opens one must finding, located in round 1's close block alone. `05394cbca` closes it | The tree at HEAD (`round-1.md:192`). The chain check, which exits 0. Its probes, which these re-runs reproduced on both gits | none. Its own S7 times (0.53 s and 0.34 s) differ from the changelog's, and it says so itself |
| the changelog | The section reads the plans of the two newest removing commits, 47,844 B with 8 older commits counted. 25 git calls in either form, where the old reading made 422. Runs of 0.56 s and 0.53 s. Newline and missing-text plans are named. `--apply` reads tags in three calls per run. One *Process changes* row for step 5 | The re-runs above for every figure except the two times, which were not reproduced and are within the 2 s bound. `skills/settle/SKILL.md` step 5 (read) | none |
| the orchestrator's part of the pull request body | `pr.md`: three quotes from `frame/plan.md` (the chosen A1 verdict, A5's "Kept as the way to reach past the window", and the `perf:` title row) and `Closes #1481`. No `pr.<lang>.md` exists, and none is owed, because both language keys of `seal/config.json` read English | Each quote appears word for word at the row it names (read). `routing.md` *Why this way* is the orchestrator's account under `agentic`. It names a settle change that narrows what the dry run shows, together with step 5, and that is what the diff changes: `settle.py`, the settle skill and its tests (read) | none |

`seal/parity.json` is not tracked. `routing.md` answers `open the pull
request`, so no parity comparison is owed. Not covered here, each with who
answers it: whether the settling session follows step 5 to `--all-earlier`
(design S8; the owner, at the next settle). The cost of `versions` on a much
larger history (rounds 1 and 2, *Not judged*; the owner). The two `## Not
done` items of `gaps.md`, which the build disclosed and this audit read.

```seal
target: 254d9a27a against 957a3bc7d
Verdict: sealed
```

## Re-audit at 5426fed88

Since `254d9a27a`, the commits outside the closing records are fix pass 2
(`f56246f6e`), which touches `tests/skills/test_settle.py` alone, and round
3's record (`72b78d30c`). `git diff --quiet 254d9a27a HEAD` exited 0 over
the work item's `frame/`, `gaps.md`, `changelog.md`, `pr.md` and
`routing.md`, over `trail/phases/` and rounds 1 and 2, and over `skills/`
(executed). So this audit re-runs the claims whose coordinates the fix
touched, which are the S6 case and the newline case, and reads the parties
again. Every rule-15 seal from the run above that does not rest on those
two cases stands as it was.

That run's clone under `sealer/` was gone when this run began. The re-runs
went to a new `git clone --no-local` at `5426fed88`, under
`sealer-2/at-base/`. One command of this run lost its `cd` into that clone.
It ran the two changed cases in the worktree instead, where 4 passed with
the tree untouched, and wrote a log to
`/Users/michael/Documents/GitHub/SpecSeal-worktrees/perf/h2-239.log`. That
log has been removed, and the worktree's `git status --short` showed only
`guarantee.md`. No row below rests on that run.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad gate ran at a commit that only this work item's records follow | `trail/gate.md`, the second block (`run: 72b78d30c against 957a3bc7d`) | `git merge-base --is-ancestor 72b78d30c HEAD`; `git log --no-merges --stat 254d9a27a..HEAD` | holds (executed). The commit is an ancestor of HEAD, and only `5426fed88` follows it, touching `trail/gate.md` alone. |
| The body file matches `pr.md` and the records at HEAD | the body file `pr-body.md`, rewritten by `seal pr-body` | `seal pr-body <item> --body <file> --check`, run with the installed copy and with the tree's `bin/seal` | holds (executed). Both copies exited 0 with `matches:`. |
| The two changed cases pass at HEAD, and on macOS they run rather than skip | `trail/rounds/round-3.md` *Probes*, rows 1 and 2 | `bin/test tests/skills/test_settle.py tests/github/test_publish_release_note.py -q -rs` on git 2.50.1; `bin/test tests/skills/test_settle.py -q -rs -p no:xdist -k "newline or git_holds_no_text"` with git 2.39.3 first on `PATH` | holds (executed). The first run gave 233 passed and the second 4 passed. No `SKIPPED` line appeared in either run. |
| S6 is still red against the old reading, and still red with only its guard removed, after the `os.chmod` added before the unlink | `tests/skills/test_settle.py:1727-1772`; `trail/phases/phase-1.md:31-36` | the cases at `957a3bc7d`'s `settle.py`; then at HEAD with only `if text is None:` before `NO_PLAN_TEXT` replaced by `if False:` | holds (executed). At the base it failed on its sentence line, where `git show` named the plan. With the guard removed it failed with `TypeError: expected string or bytes-like object, got 'NoneType'`. |
| The newline case is still red against the batch that asked for both paths, and still red with only the line naming the plan dropped, after the skip was added | `tests/skills/test_settle.py:1775-1834`; `trail/rounds/round-1.md` finding 2's close block | the newline case at `452d08a3d`'s `settle.py`; then at HEAD with only `return [], split, older` replaced by `return [], [], older` | holds (executed). At `452d08a3d` both parameters failed, and the plain plan was named with `` answered `name/frame/plan.md missing` ``. With the line dropped, `[alone]` failed with `IndexError` in `earlier_block`, because the section was never printed. The skip did not fire in either run. |
| The Windows failure is fixed, and every leg passes on the fix | PR #1526, run `42995460465`; the coordinator's message | `gh run view 42995460465`; `gh run list --commit f56246f6e…`; `gh run view 42996311201 --json jobs` | holds (executed). Run `42995460465` was on `0c2742d83` and concluded `failure`. Run `42996311201`, a `pull_request` run on `f56246f6e`, passed every job: lint, durations, the ubuntu, macOS and four Windows pytest shards. `release-report` was skipped. |
| The full suite, the repository-wide lint and the format check pass | `trail/gate.md`, the second block | not run (contract rule 2) | read. The gate record names `72b78d30c`, and HEAD differs from that commit by `trail/gate.md` alone. |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Unchanged since `254d9a27a` (executed, `git diff --quiet`) | as in the run above | as in the run above: none that the issue body or the tree decides |
| the build | Fix pass 2 makes the missing-object case clear the read-only bit before the unlink. The newline case now skips only where git refuses the odd path in the index, and fails where the plain path is refused | The re-runs above. The case still runs and holds its fact on Linux and macOS. The code under test reads the history through `git log -z` and `cat-file --batch`, not through the index, so the Windows skip hides no Windows-only behaviour of `settle.py` (read) | none |
| the last round | Round 3 opens no finding, confirms round 2's finding 1, and reads both changed cases | The tree at HEAD and the re-runs above. It notes that the case's comment and skip reason claim more than they hold, since a Windows clone can fetch such a commit made elsewhere, and opens no finding for it. This audit reads that the same way: it is wording in a test, and the claim the guarantee covers does not rest on it | none |
| the changelog | Unchanged since `254d9a27a` | as in the run above | none |
| the orchestrator's part of the pull request body | `pr.md` is unchanged since `254d9a27a`. `routing.md` is unchanged | as in the run above | none |

`seal/parity.json` is still not tracked, so no parity comparison is owed.
The items not covered are those listed above, with the same answerers.

```seal
target: 5426fed88 against 957a3bc7d
Verdict: sealed
```
