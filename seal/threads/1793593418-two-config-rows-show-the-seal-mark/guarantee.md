# Guarantee: 1793593418-two-config-rows-show-the-seal-mark

| Field | Value |
|---|---|
| Broad gate | 42883972e against 9c61be933 |

The audit is of `c53fb3a7d`, against `release/v0.28.0`, which resolved to
`9c61be933` through its upstream (executed `git rev-parse --verify --quiet`).
The gate's run commit `42883972e` is an ancestor of HEAD, and the one commit
after it, `c53fb3a7d`, touches only this work item's `trail/gate.md`
(executed `git log --no-merges --name-only 42883972e..HEAD ^9c61be933`).
The scratch clone named below is a `git clone --no-local` of the worktree at
`c53fb3a7d` under the scratchpad, removed after the runs.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The body file's part below `## From the records` is the records' own text | the orchestrator's `seal pr-body` run, before this spawn | `seal pr-body <item> --body <the body file> --check`, with the installed 0.27.3 `seal` and with the tree's `bin/seal` | holds: exit 0 from each, `matches:` (executed) |
| Phase 1's twenty new cases and phase 2's eight ran red against the code before the change | `trail/phases/phase-1.md` *The cases, and how each was shown red*; `trail/phases/phase-2.md` same section | in the scratch clone, `git checkout 9c61be933 --` `pr_body.py`, `release_seal.py`, `publish_release_note.py`, `templates/setup/config.md` and `skills/config/SKILL.md`, then `bin/test tests/skills/test_pr_body.py tests/github/test_release_seal.py tests/github/test_publish_release_note.py tests/text/test_the_settings_have_a_front_door.py -q -p no:xdist` | holds: exit 1, 34 failed and 144 passed. Every `Test_seal_mark` case, the four mark cases of `Test_main`, the six S6 cases, the S7 case and both front-door rows failed. The count is above phase 1's twenty because round 1's fix and `a566ad6b2` added cases since (executed) |
| S3's case is red with the `follows` condition alone removed | `trail/phases/phase-1.md` *Mutations*, row S3 | in the scratch clone at HEAD, `pr_body.py#_seal_at_head`'s `return behind is None, None` changed to `return True, None` with the Edit tool, then `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k later_commit_follows` | holds: exit 1, `test_refuses_a_seal_a_later_commit_follows` failed (executed) |
| S6's absent-row case is red with the row's read alone removed | `trail/phases/phase-2.md` *Mutations*, row S6 | in the scratch clone at HEAD, `release_seal.py:546` `on, unread = mark_on(ROOT)` changed to `on, unread = True, None`, then `bin/test tests/github/test_release_seal.py -q -p no:xdist -k "other_than_yes and absent"` | holds: exit 1, the `absent` case failed (executed) |
| Before round 1 finding 1's fix the main-checkout case and both naming cases failed and the local-mode case passed | `trail/rounds/round-1.md:93`, the answer to finding 1 | in the scratch clone, `git checkout bf3efaf23 -- skills/code-review/scripts/pr_body.py`, then `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "another_checkout or local_mode_work_item or head_does_not_hold"` | holds: exit 1, 3 failed (`[off]`, `[unseen]`, the main-checkout case) and 1 passed (the local-mode case) (executed) |
| The work item's modules pass at HEAD | `trail/phases/phase-1.md` and `phase-2.md` *The phase-boundary run*; `trail/rounds/round-2.md` *Probes* | in the scratch clone at `c53fb3a7d`, `bin/test tests/skills/test_pr_body.py tests/github/test_release_seal.py tests/github/test_publish_release_note.py tests/text/test_the_settings_have_a_front_door.py tests/behaviour/test_the_release_seal_is_drawn.py -q` | holds: exit 0, 180 passed (executed) |
| S10: the terminal stamp is unchanged, and no policy document is edited ahead of the settle | `frame/design.md` S10 and *Removes*; `trail/phases/phase-2.md` S10 | `git diff --stat 9c61be933...HEAD -- skills/verify/scripts/seal_stamp.py skills/verify/scripts/seal-mark.txt hooks/sealer-stamp-queue.py hooks/sealer-stamp.py .claude-plugin/ docs/` | holds: nothing printed, exit 0 (executed) |
| Every `## Removes` row: the unconditional sentences no longer stand | `frame/design.md` *Removes* | `git grep` for "Draw the release's seal as a PNG, attach it, and put it in the note", "replaces the note's header with a table of two cells" and "body the sealer read"; read `release_seal.py:1-13`, `publish_release_note.py:90-96` and `:645-658`, `publish-release.yml:30-36`, `orchestration.md:222-230`, `pr_body.py:19-31` | holds: no match outside `seal/threads/`; each place now states the row's condition (executed, read) |
| Round 2 finding 1, fixed at `332455460` in the records alone | `trail/rounds/round-2.md:481-484` | read `frame/design.md:52-69` and `:232-252`, `changelog.md:3` at HEAD against the finding's three proposed sentences, and the finding's sentence leaving `design.md` *Data & interfaces* "to the same edit as the others" | does not hold in full: the three proposed sentences stand as given, and `frame/design.md:177-182` *Data & interfaces*, which the finding left to the same edit, still lists the lines a reader sees without the unresolved-base line and the sealed-commit line (read) |
| "No case builds a local-mode root" | `gaps.md:10`, *Not verified*, copied into the pull request body | read `tests/skills/test_pr_body.py:737-765`, run in the HEAD row above; `git log -S local_mode_work_item -- tests/skills/test_pr_body.py` | does not hold: `Test_main::test_accepts_a_local_mode_work_item_from_the_working_directorys_checkout` builds the root under `.git/seal` and passed at HEAD; it came in at `863a7d2af` (executed) |
| "Broad run at 42883972e against 9c61be933 (`trail/gate.md`): 6328 passed, 12 skipped" | the pull request body, the orchestrator's part, line 17 | read `trail/gate.md` | does not hold against its citation: the record holds `run: 42883972e against 9c61be933` alone. The counts stand only in the orchestrator's own gate log in the scratchpad, line 12, which this audit read and did not run (read) |
| The orchestrator's commits are 09d7e5c8f, e20307530, e3981d8fb, f2c96cda7, 332455460, the merge and the round and gate records (`frame/plan.md` *Judgments of the run*) | the pull request body, the orchestrator's part, line 15 | read `frame/plan.md:101-107`; `git show --stat` of each listed commit | does not hold against its citation: the table holds no commit and no row for `332455460`, whose fold `trail/rounds/round-2.md:483` states. Each listed commit touches only this work item's records (executed). `be0548a17`, a records-only `gaps.md` edit, is not listed, and no record names its author (unverified; the orchestrator answers) |
| "The branch merged `release/v0.28.0` (#1281) at 42883972e with no conflict" | the pull request body, the orchestrator's part, line 17 | `git merge-tree --write-tree 5f6c4100e 9c61be933` against `git rev-parse 42883972e^{tree}`; `gh issue view 1281` | holds: exit 0 and the same tree, `256faaa04`; #1281 is the issue the merged #1295 implements, as `trail/rounds/round-1.md:9` names it (executed) |
| #1216's pin and copy notices | `trail/rounds/round-1.md` and `round-2.md` *Confirmations* | the tree's `python3 skills/code-review/scripts/chain_check.py --baseline 9c61be933 --root <worktree> --worktree`; `bin/seal rules --check`; `git grep` over `tests` for the `from` values' sentences | holds: exit 0 from each, and the check prints no pin or copy notice. The one test that reads a `from` sentence, `tests/behaviour/test_the_release_seal_is_drawn.py:54`, pins the job's and the asset's names, a fact the checklist's `to` keeps (executed, read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Two rows, each off unless `yes`; `pr-body` writes the mark only under a `sealed` guarantee at HEAD or followed only by the closing records, read in the item's own checkout; the release row is read by this repository's `seal` job alone; the terminal stamp and `plugin.json` are untouched | the issue's direction and *Done when*; the diff; the changelog; round 2 | itself and the tree: `frame/design.md:177-182` lists the lines a reader sees without the unresolved-base line and the sealed-commit line that `pr_body.py:223-230` prints and its own *Scope* item 2 (`:65-67`) names |
| the build | The diff, the phase records and the closing memo: the rows read through `hooks/lib/config.py#declared_value`, `seal_mark` and `mark_on`, cases seen red, the docstrings rewritten in place | the design's *Scope* and *Removes*; every re-run above | the tree: `gaps.md:10` says no case builds a local-mode root, where `tests/skills/test_pr_body.py:737-765` builds one |
| the last round | Round 2 confirms round 1's three fixes and raises one `should` on the records, fixed at `332455460` | the tree at HEAD on round 1's three findings; the re-runs above | the design at HEAD on the part of its finding left to the same edit: `frame/design.md:177-182` was not edited |
| the changelog | The PR row and the release row with their conditions, the named lines, the second `seal pr-body` run, and the settle's targets | the design's `add` and `change` values; `pr_body.py`, `release_seal.py`, `orchestration.md:222-230` and `:319-325`; the issue | none |
| the orchestrator's part of the pull request body | The summary, the framer's rejected alternatives, the rounds, the orchestrator's commits, the merge and the broad run | the changelog, `frame/plan.md` A2, A5 to A7 and A11, `frame/questions.md` Q1, both round records, the tree on the merge | its own citations: the broad run's counts are not in `trail/gate.md`, and `frame/plan.md` *Judgments of the run* holds none of the commits it is cited for |

```seal
target: c53fb3a7d against 9c61be933
Verdict: withheld reason: four record claims do not hold at c53fb3a7d. (1) The build's closing memo, gaps.md line 10, says "No case builds a local-mode root", where tests/skills/test_pr_body.py lines 737-765, added at 863a7d2af, build one and passed at HEAD; the pull request body copies that row. (2) The design, frame/design.md lines 177-182 *Data & interfaces*, lists the lines a reader sees without the unresolved-base line and the sealed-commit line that pr_body.py lines 223-230 print and its own Scope item 2 names; round 2 finding 1 left it to the same edit, and 332455460 did not make it. (3) The orchestrator's part of the pull request body, line 17, gives the broad run as "6328 passed, 12 skipped" citing trail/gate.md, which holds only `run: 42883972e against 9c61be933`. (4) The same part, line 15, cites frame/plan.md *Judgments of the run* for commits 09d7e5c8f, e20307530, e3981d8fb, f2c96cda7 and 332455460; that table holds no commit and no row for 332455460, whose fold trail/rounds/round-2.md finding 1's answer states.
```

## Re-audit at 3f234897a

The newest block above names `c53fb3a7d`. The one commit since then,
`3f234897a`, touches `frame/design.md`, `frame/plan.md`, `gaps.md` and
`guarantee.md` under this work item, and nothing else (executed
`git log --no-merges --name-only c53fb3a7d..HEAD`; `git diff --stat
c53fb3a7d HEAD` outside the work item prints nothing). The gate's run
`42883972e` is still followed only by this work item's records, and the
base still resolves to `9c61be933` (executed). No code coordinate changed,
so the code claims re-run above stand at this HEAD. This run re-reads the
four reasons, the records the commit touched, and the parties.

| Field | Value |
|---|---|
| Broad gate | 42883972e against 9c61be933 |

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The body file's part below `## From the records` is the records' own text | the orchestrator's `seal pr-body` rewrite after `3f234897a` | `seal pr-body <item> --body <the body file> --check`, with the installed 0.27.3 `seal` and with the tree's `bin/seal` | holds: exit 0 from each, `matches:` (executed) |
| Reason 1: `gaps.md` no longer says no case builds a local-mode root | `3f234897a`, `gaps.md` | `git show 3f234897a -- gaps.md` | holds: the row is removed. Its subject, a seal at HEAD in local mode, is held by `tests/skills/test_pr_body.py:737-765`, which passed at `c53fb3a7d`, and round 1's confirmation on local mode (executed, read) |
| Reason 2: *Data & interfaces* names the unresolved-base line and the sealed-commit line | `frame/design.md:177-184` | read against `pr_body.py:223-230` (`BASE_UNSEEN`, `NOT_IN_HISTORY`) and *Scope* item 2 (`:65-67`) | holds: the sentence names the base git cannot resolve and the sealed commit the work item's checkout's HEAD does not hold, as the code prints and *Scope* item 2 says (read) |
| The new *Judgments of the run* row | `frame/plan.md:108` | read against `3f234897a`'s diff and the block above | holds: it states the two record edits and their grounds as made (read) |
| Reason 3: the broad-run line cites only what `trail/gate.md` holds | the pull request body, the orchestrator's part, last bullet | read `trail/gate.md`; `broad_gate.py` docstring on `--record` | holds: no counts and no conflict claim remain. "Passed" stands on the record, which `seal gate --record` writes only on success (read) |
| Reason 4: the commit line cites the records that hold each commit, and every commit named touches only the work item's records | the pull request body, the orchestrator's part, the commits bullet | `git show --stat` of 09d7e5c8f, e20307530, be0548a17, 950150dbf, e3981d8fb, bf3efaf23, f2c96cda7, 39d06243f, 332455460, 5f6c4100e, c53fb3a7d and 3f234897a; `git merge-tree --write-tree 5f6c4100e 9c61be933` against `42883972e^{tree}`; `git diff --name-only 9c61be933...HEAD` | holds: each non-merge commit touches only this work item's records. The merge `42883972e` resolves no conflict, since its tree equals the clean merge's, and it adds no path to the pull request's diff, whose 12 paths outside the work item are this work's own. `routing.md`, *Judgments of the run* and `trail/rounds/round-2.md:483` hold what they are cited for. That be0548a17 is the orchestrator's is the orchestrator's own account, and no record contradicts it (executed, read) |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | As above, and *Data & interfaces* now names every line `seal pr-body` prints about the mark | the tree (`pr_body.py:207-238`, `#seal_mark` at `:396`); its own *Scope* item 2 and `add`; the changelog; round 2 | none |
| the build | The diff and the phase records as above; the closing memo without the local-mode row | the design; the tree; every re-run above | none |
| the last round | Round 2 confirms round 1's three fixes and raises one finding, whose records fix `332455460` and `3f234897a` now complete | the design and the changelog at HEAD | none |
| the changelog | Unchanged since the block above | the design's `add` and `change` values; the code; `orchestration.md`; the issue | none |
| the orchestrator's part of the pull request body | The summary, the framer's rejected alternatives, the rounds, the orchestrator's commits by the records that hold them, the merge, and the broad run as `trail/gate.md` records it | the changelog; `frame/plan.md` A2, A5 to A7, A11 and *Judgments of the run*; `frame/questions.md` Q1; both round records; `routing.md`; `trail/gate.md`; the tree | none |

```seal
target: 3f234897a against 9c61be933
Verdict: sealed
```
