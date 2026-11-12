# Guarantee: 1794465691-the-orchestrator-polls-ci-by-hand

Audited on 2026-11-12 by the sealer, at `9a68b469b` against the base
`release/v0.38.0`. Its `@{upstream}` resolved to `8e711ade9`, #1516's
squash merge. The local ref stands at `79f815a74` and was not used
(`executed`: `git rev-parse --verify --quiet` on the three forms). The gate
record `trail/gate.md` names `run: e2ae6e808 against 8e711ade9`.
`e2ae6e808` is an ancestor of HEAD, and the one commit after it,
`9a68b469b`, touches only `trail/gate.md` (`executed`: `git merge-base
--is-ancestor` and `git log --no-merges --name-only e2ae6e808..HEAD
^8e711ade9`). The broad gate's pass is the orchestrator's account. The
sealer read the record and ran nothing broad (`read`, contract rule 2).
`seal pr-body <item> --body <file> --check` exited 0 with the tree's
`bin/seal`, answering `matches` (`executed`). The repository declares no
`seal/parity.json` (`executed`: `git ls-files` printed nothing), so no
comparison with an original is owed. `chain_check.py --baseline 8e711ade9
--sealing` exited 0 in a clone at HEAD (`executed`). It judged no ready
pull request, since the clone has no GitHub remote.

After round 2's target `1dae28a6f`, three commits are records only:
`ea152511b` (`round-2.md`), `7f64ab305` (`frame/plan.md`, `gaps.md`) and
`9a68b469b` (`trail/gate.md`) (`executed`, `git show --name-only`). The
merge `e2ae6e808` has an empty `git show --remerge-diff`, so it resolved
nothing by hand (`executed`). Every file of the work's code, tests and
skill text is the same at `1dae28a6f` and at HEAD (`executed`, `git diff
--stat 1dae28a6f HEAD` over the eight paths, empty). So round 2 read the
code that HEAD holds. Round 2 has no finding, so no `fixed` claim remains
for the sealer to read in place of a round.

The probes ran in two `git clone --no-local` copies of the branch under
the sealer's scratch directory. `at-head` stayed clean at HEAD.
`at-base` took the base's files or a mutant one file at a time, and each
file was restored with `git checkout HEAD --` after its run (`executed`,
`git status --short` empty at the end).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The module's cases and the pin pass: 60 passed | `trail/rounds/round-2.md:135-137` | `bin/test -q tests/skills/test_pr_wait.py tests/text/test_the_rules_have_one_owner.py` in `at-head` | Holds: 60 passed, exit 0 (`executed`) |
| The registration, `SHIPPED`, release-hygiene and script-reach modules pass | `trail/rounds/round-1.md:338-346`; `trail/phases/phase-1.md:59-64` | `bin/test -q` on `test_a_reference_root_is_read_and_never_taken.py`, `test_release_hygiene.py` and `test_a_document_that_names_a_script_says_how_to_reach_it.py`; `bin/test -q tests/skills/test_seal.py -k accepts_each_tool` | Holds: 82 passed and 8 skipped, exit 0; 14 passed, exit 0 (`executed`) |
| The cases were red before the module existed | `trail/phases/phase-1.md:17-18` | `pr_wait.py` taken out, as at the base; `bin/test -q -p no:xdist tests/skills/test_pr_wait.py` | Holds: exit 2, `FileNotFoundError` for `pr_wait.py` at collection (`executed`) |
| The pin was red against the old paragraphs | `trail/phases/phase-2.md:16-18` | `skills/code-review/orchestration.md` from `8e711ade9`; the pin case alone | Holds: exit 1, "the owner section no longer says '`seal pr-wait <N> --once`'" (`executed`) |
| The registration was red before `TOOLS`, `SHIPPED` and the version row named the command | `trail/phases/phase-1.md:59-64`, `:111-118` | `seal.py` from the base, then the `pr-wait` pair; then both behaviour modules from the base | Holds: argparse "invalid choice: 'pr-wait'"; "not classified here … ['seal pr-wait']"; "`pr_wait.py:70` names v2.92.0" (`executed`) |
| S7: the cancelled case is red with only the `cancel` guard removed | `trail/phases/phase-1.md:30` | HEAD's code with `BAD` cut to `{"fail": "failed"}`; `-k test_refuses_a_cancelled_check_where_watch_passes_it` | Holds: exit 1, `(0, ['every c...was skipped']) == (1, …hygiene')`, a pass where 1 was due (`executed`) |
| S6: the dependent-job case is red without the runs read | `trail/phases/phase-1.md:34` | `and _completed(sha)` removed from `wait`; `-k test_refuses_to_decide_while_a_run_has_not_completed` | Holds: exit 1, 0 where 1 was due, on `release-report` (`executed`) |
| S4: the stale-head case is red without the head comparison | `trail/phases/phase-1.md:32` | `and not moved` removed from the checks condition; `-k test_refuses_a_head_that_is_still_the_commit_before_the_push` | Holds: exit 1, 0 where 3 was due (`executed`) |
| S5: the other-event case is red when the start counts every check | `trail/phases/phase-1.md:33` | `_started` made `bool(listed)`; `-k test_refuses_to_start_on_another_events_finished_check` | Holds: exit 1, 0 where 3 was due (`executed`) |
| Round 1 finding 1's case is red with its guard off and against `be4b321da`'s code | `trail/rounds/round-1.md:87`; `trail/rounds/round-2.md:41-45` | `if moved and started:` made `if False:`; then `pr_wait.py` from `be4b321da` with the whole module | Holds: "the wait never ended" at 3600; against `be4b321da`, 3 failed and 32 passed, the moved-head case and the two `UNKNOWN` cases (`executed`) |
| Round 1 finding 3's `mergeable` guard is held by a case | `trail/rounds/round-1.md:220` | `if mergeable not in MERGEABLE:` made `if False:`; `-k test_refuses_a_view_gh_does_not_shape` | Holds: the `BLOCKED` parameter fails on `DID NOT RAISE Unanswered`, and the two shape parameters pass (`executed`) |
| Nothing of *Removes* rows 1 to 4 stands | `frame/design.md:101-110` | `git grep` outside `seal/threads/` for `state,mergeable`, `pr checks <N> --watch`, `headRefOid --jq` and `select(.event == `; `git grep -i` in `orchestration.md` for `ten seconds`, `two minutes`, `UNKNOWN`, `reads it again` and `--watch`; the pin's tuple read for its old strings | Holds. `state,mergeable` stands only as the prefix of the command's own four-field read, in `pr_wait.py:36` and its cases. The section has none of the five. The pin keeps no old string, and its docstring names the old wait as history (`executed`) |
| The removal the changelog names: the hand read, the poll and `--watch` | `changelog.md:15` | The same searches, and `git grep` for `gh pr checks`, `pr-wait` and `wait(s) on CI` outside the work item and the two new files, the `.ko.md` editions included | Holds. The only statements are the new paragraph, the registration and the pin (`executed`) |
| The issue's 363 words, which the title repeats | issue #1494; the orchestrator's title | `git show 79f815a74:skills/code-review/orchestration.md`, the paragraph from **The orchestrator waits on CI with** to **A conflict with the base**, `wc -w` | Holds: 363 (`executed`) |
| Each `pr.md` quote stands at its coordinate | `pr.md:1-4` | A `python3 -I` check of each quote against the file it names | Holds: 4 of 4 (`executed`) |
| A line opening with `seal` falls in no `git` family of `seal cost` | `changelog.md:9`; `frame/plan.md:49` | Read `skills/verify/scripts/session_cost.py:143-158` | Holds: `git` matches `^\s*(git\|gh)\b` alone, and no other family matches `seal pr-wait` (`read`) |

Not re-run, by choice of sample: phase 1's boundary run of 2194 cases and
phase 2's of 1096, the mutants of the state, bucket, `gh`, `git` and
`--once` guards, and `seal layout --pairs`. Each is `read`. The sample
took the guards that decide a pass, exits 0 and 1, and the guards round 1's
fixes added.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `seal pr-wait <N>` reads the state, the head and the checks through `gh`'s JSON, confirms a read with nothing pending against the `pull_request` runs, and answers with exits 0 to 6. `--once` reads the state. The two paragraphs become one paragraph and a table, and the pin holds the commands and the codes (*Scope* 1-6; S1-S11; *Data & interfaces*) | The build. `pr_wait.py#wait`, `#once` and `#main` follow *Data & interfaces* read for read, and the exit table matches code for code, the folds of `e0deb977e` and `1dae28a6f` included (`read`). The issue's *Change* (`read`) | none |
| the build | Phases 1 and 2 at `a48e77f8a` and `06ac413c2`, the Status cells of `frame/plan.md:31-32`, each with its `trail/phases/phase-N.md`, as `routing.md`'s `crafter` row asks. The fix pass at `a02ca9542`, `aa5ee134b`, `cab760882` and `573882a23` | The design. The claims re-run above. Phase 1's last decision, that a head leaving HEAD keeps the wait going (`phase-1.md:92-95`), was replaced by round 1 finding 1, and the fix pass says the record stays as written (`read`) | none |
| the last round | Round 2 at `1dae28a6f`: no finding; confirms round 1's five closes; leaves two *Not judged* rows to the orchestrator | The tree at HEAD, since the code is the same as at `1dae28a6f`. Its two open rows are answered by `frame/plan.md:60-61`, which agree with the table: row 0 gives the push to exit 0 alone, row 2 takes nothing as known, and row 3 already stops the wait and does not treat the pull request as checked (`read`) | none |
| the changelog | *Added*: the command, its codes, `--once`, and the two results `--watch` passes that it does not. *Process changes*: the orchestrator's step after a push, replacing the hand read, the poll and the watch | `pr_wait.py`'s behaviour as the cases pin it (`executed`, above). The section at `orchestration.md:266-288` (`read`). The *Removes* searches (`executed`) | none |
| the orchestrator's part of the pull request body | Two *Operational impact* quotes, Q2's default and the `feat:` title judgment, then `Closes #1494.` | Each quote at its coordinate (`executed`). The diff adds a subcommand, which the `feat:` row's grounds say. The diff moves no version, as `routing.md` says #1516 carries it (`executed`, `git diff --stat`) | none |

`routing.md` *Why this way* gives the orchestrator's grounds under
`agentic`: a framer because the issue leaves the reads, the codes and the
tests open; a crafter; the review chain because the change rewrites an
instruction every orchestrating session acts on; and the pull request into
`release/v0.38.0` after #1516. The diff is a new script with its cases and
registration, and the rewritten section with its pin. The grounds describe
it (`read`).

The issue's *Done when*, read against the tree. First, a push before any
check has reported and a failed check end at different codes: exit 3 past
the limit (S3) or the wait going on, and exit 1 (S2). The cases pass, and
the guards behind S4 to S7 go red when removed (`executed`). Second, "the
paragraph states only the command and its exit codes". The paragraph at
`orchestration.md:266-278` also says what the wait reads, keeps the reason
it reads every workflow's checks, and says the limit covers the start
alone. *Scope* item 4 keeps those sentences by name, and S10 takes the
criterion to mean no `gh` command for the wait. The sealer reads "only" as
setting the command and its codes against the hand procedure it replaces.
Under that reading the criterion holds, and the section names no `gh`
command for the wait (`read`). Under the strict word, the reason sentence
and the limit sentence are extra. The owner can say which reading the
issue meant.

Left `unverified`, with who answers. S11 and Q1: the first real run on
this pull request, and how long the first `pull_request` check takes to be
listed. The orchestrator answers at this pull request's first `seal pr-wait`
run. Q2, Enterprise Server: whoever runs the plugin against one. The cases
on Linux, Windows, Python 3.12 and 3.14: the pull request's `tests`
workflow. The broad gate's pass is the orchestrator's record, which the
sealer read and did not re-run.

```seal
target: 9a68b469b61eec92d479793fcc1a31ecea60ab9e against 8e711ade98b059106d63f82253e44a4764898bd7
Verdict: sealed
```
