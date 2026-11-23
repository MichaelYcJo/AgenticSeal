# Review round 1: 1795439973-six-test-modules-cost-past-the-rewrite-bound

```seal
target: 283f33baf against origin/release/v0.38.6
```

This is the first round, so no earlier record carries a coordinate, and
every fact below was established here. The diff was read from the merge
base `ef776317b` to `283f33baf`, in a `git clone --no-local` at
`283f33baf`. `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were each read whole at `283f33baf`. The phase
records were read whole for phases 7, 9 and 11, and in their findings,
departures and verdict tables for the others. No `pr.<lang>.md` stands, and
none is owed: `seal/config.json` names English for both language keys. No
`seal/parity.json` is declared.

The diff changes six test modules and the work item's records, and no
shipped file (executed: `git diff --stat ef776317b..283f33baf`). The round
spent its reading where the prompt and the frame put the risk: whether each
rewritten or cut case still holds the fact the old one held. Three methods
covered that, each over all six modules or over the gates that refuse a
ready pull request.

- **Every test function's assertions, base against target.** A script
  parsed each module at `ef776317b` and at `283f33baf` and listed, per test
  function, the assertions gone, added and changed (executed: the script
  `asserts_diff.py` in this round's scratch). It names 2 functions gone and 3
  added in `test_chain_check.py`, 38 moved between classes and none lost in
  `test_settle.py`, 1 gone and 3 added in `test_seal.py`, 2 gone and 3 added
  in `test_broad_gate.py`, 3 moved in `test_test_layout.py`, and only
  record sizes in `test_release_seal.py`. Each function whose assertions
  changed was read against the phase record that rewrote it.
- **The mutation tables of the gates, run again at the target.** The
  mutant sets phases 2, 3 and 9 ran over `chain_check.py`, and phase 7's over
  `broad_gate.py` and the recorder, ran again against `283f33baf` from the
  phases' own scripts. The results stand in *Probes*.
- **A world shared without a copy.** A probe ran `main` over each of the
  three module templates of `test_chain_check.py` that cases read without a
  copy, and compared every byte under each, `.git` among it.

Two facts the round read and does not raise as findings. First,
`trail/phases/phase-9.md:209-210` ends with two stray lines, a closing
`content` tag and a closing `invoke` tag, left from the tool call that wrote
the file. Nothing stands below them, so they hide no fence, and the record
above them is whole. Second, `trail/phases/phase-3.md` *Departures from the
frame* records that `Test_main::test_refuses_a_last_records_fixed_finding_owing_a_verifying_round`
lost its draft run, and names the two cases that hold the draft's exit now.
The assertion comparison found that loss, and the record already holds it.

## Findings

### 1. The changelog says `at` runs `draft`, and names three plain functions as fixtures

```seal
severity: should
location: `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/changelog.md:20`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/changelog.md:30`
evidence: read `tests/skills/test_settle.py:697-711`, `tests/skills/test_settle.py:3889-3970` and, at `ef776317b`, `tests/skills/test_settle.py:86`, `:101`, `:113`, `:381`, `:514`; executed `grep -n "settle.draft(\|\.draft(" tests/skills/test_settle.py`, which printed nothing
```

Why it matters: the changelog fragment becomes the release note. It lists
the seams a contributor uses to write a new case. A contributor who reads
that `at` runs `draft` and writes a `--draft` case through it gets a
report.

The claims and what the tree holds:

- **Claimed** at `changelog.md:20`: "`at` runs `survey` with `report`,
  `apply` or `draft`." **Found**: `at` (`tests/skills/test_settle.py:697-711`)
  calls `settle.apply` where `--apply` is among its arguments and
  `settle.report` otherwise. No case of the module calls `settle.draft`. The
  `--draft` cases, such as
  `Test_main::test_draft_writes_each_operation_in_merge_order_and_names_what_it_missed`,
  run `settle.main` through `dry_run`.
- **Claimed** at `changelog.md:30`: "`tests/skills/test_settle.py`'s own
  `git`, `commit`, `repo`, `local` and `settled_repo` fixtures." **Found**:
  at `ef776317b`, `repo` (`:113`) and `local` (`:514`) were fixtures, and
  `git` (`:86`), `commit` (`:101`) and `settled_repo` (`:381`) were plain
  functions. `frame/design.md` *Removes* calls the first two "the module's
  own git runner" and "commit helper".

The fix rewrites the two lines. It reaches every statement of the two facts
in the fragment: no other line of `changelog.md` names `at` or these five
helpers.

```markdown
  - `test_settle.py`: `drawn` is a world with no history. `answered` answers `settle.py`'s ten readers that ask git from the disk, and `real` names the ones a case keeps. `at` runs `survey` at a ref and then `report`, or `apply` under `--apply`; a `--draft` case runs `settle.main`. The `gh` fixture answers in the process, and one case keeps a `gh` script on `PATH` (`gh_on_path`). `imported`, `committed` and `merged_history` write a history in one `git fast-import`.
```

```markdown
- **`tests/skills/test_settle.py`'s own `git` and `commit` helpers, its `settled_repo` builder, and its `repo` and `local` fixtures.** Its cases reach `tests/conftest.py#git_out`, `#git` and `#commit_everything`, and module worlds copied per case.
```

### 2. Phase 9's 32 "Answered" verdicts are a third kind, and the frame, the judgment and the changelog name two

```seal
severity: should
location: `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/design.md:131`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/plan.md:69`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/changelog.md:15`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/gaps.md:61`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:107`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:114`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:118-121`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:130`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:143`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:146`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:151`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:156`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:177`
evidence: read `trail/phases/phase-9.md:34`, `:94-196`, `tests/skills/test_chain_check.py:466-488`; executed a count of the verdict column of `trail/phases/phase-9.md` part 4 (32 rows open with "Answered", 11 of them read "Answered.", "Answered, its two runs." or "Answered, over the template." and nothing else) and a count over `tests/skills/test_chain_check.py` of test functions that call `answered(monkeypatch` and run `check` or `checked` (31)
```

Why it matters: the orchestrator stopped `tests/skills/test_chain_check.py`
at 132 s, above the 60 s bound, on the grounds that every case left over
real git is named with the reason it stays. `pr.md` hands that judgment to
the owner, and the release note repeats it. The record the grounds point at
does not hold it for 11 cases.

`frame/design.md:131` (*Scope* item 11) says each listed case "either
becomes a unit call on the reader it reads through ... or stays a real-git
case, and the phase record names it with the agreement between the reading
and git that its fact is". The target has a third kind. Thirty-one test
functions run `main` with `answered` (`tests/skills/test_chain_check.py:466-488`),
which replaces `read_record`, `tracked_files` and `follows`. Every other git
`main` starts stays real: the top, the baseline, the diff, the merge base,
the root's entry, the trailers, the tree the rule-changes arm lists, the
current branch, `carried_by` and a fixed commit's ancestry. Phase 9 names
this kind a departure (`trail/phases/phase-9.md:34`). Items 6, 7 and 13 took
in the like seams of phases 6, 7 and 8 (`at_top`, `arms_answered`,
`answered` in `test_settle.py`), and item 11 was not amended.

Of the 32 rows of part 4 that open with "Answered", 21 name a reader kept
real or what changed in the case's world. The other 11 name nothing:
`phase-9.md:107`, `:114`, `:118`, `:119`, `:121`, `:130`, `:143`, `:146`,
`:151`, `:156` and `:177`. Those cases are a ready pull request's refusal,
a draft's exit 0, `--sealing` or a notice under `--worktree`. Each is a fact
of what `main` does with an arm's answer, which is a reason to keep the
`main` run. The record never says so for these 11.

The statements that rest on two kinds:

- **Claimed** at `frame/plan.md:69`, in the grounds: "Phase 9 gave each
  listed case the verdict `CONTRIBUTING.md` asks, a unit call or the git
  agreement its fact is, so the cases that stay are each named with the
  reason they stay". **Found**: 11 rows give neither.
- **Claimed** at `changelog.md:15`: "Each record gives one verdict per case
  that costs more than 0.5 s: the case became a call, or it kept real git
  and the record names the answer of git it holds." **Found**: phase 9's
  32 "Answered" rows are neither a call nor, for 11 of them, a named answer
  of git.
- **Claimed** at `gaps.md:61`: "*Scope* item 11 keeps those readers'
  agreement with git in the runs". **Found**: item 11 says nothing of the
  readers `answered` leaves real. Each of those readers' agreement with git
  is held by its own class (`Test_merge_base`, `Test_changed`,
  `Test_carried_by`, `Test_routing_trailers`) and by the kept runs with
  every reader real (`phase-9.md:89`), not by the 11.

This does not show that the module could come under 60 s. By phase 9's own
count, the answered runs start 736 of the module's 1,675 processes
(`phase-9.md:85`). The judgment may well stand. What it rests on has to say
what the record holds.

The fix gives each of the 11 rows the fact of `main` it holds, folds the
third kind into item 11 as items 6, 7 and 13 were folded, and rewrites the
three sentences that state two kinds. The snippets cover item 11, the
changelog sentence and the gaps sentence. The fix pass also owes the
grounds cell of `frame/plan.md:69` and the 11 rows, which it writes from
each case's assertions. `pr.md`'s first quote is the judgment cell of that
row, not its grounds, so it stands.

```markdown
Where a listed case's fact is what `main` does with an arm's answer, such as the exit on a ready or a draft pull request, `--sealing`'s exit or a notice, the case keeps its `main` run with `answered` replacing `read_record`, `tracked_files` and `follows`. The other git `main` starts stays real, and the phase record names the fact of `main` the case holds (`trail/phases/phase-9.md` *Departures from the frame*).
```

The paragraph above is appended to item 11 at `frame/design.md:131`, after
its sentence on `Test_retired`.

```markdown
- **Two of the six stay above 60 s on the Windows leg, and a third may in a slow run.** Each record gives one verdict per case that costs more than 0.5 s. The case became a call. Or it runs the command with the readers it does not test answered, and the record names what of the command it holds. Or it kept real git, and the record names the answer of git it holds. The records are this work item's, under `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/`, and git history keeps them after the settle. The orchestrator's judgment of each module stands in that directory's `frame/plan.md` *Judgments of the run*.
```

```markdown
Phase 9 did not bring `tests/skills/test_chain_check.py` under 60 s by its own estimate. Of the 1,675 processes its cases start, 396 stand in the twelve test functions that run `main` with every reader real, 736 in the 32 that run it with `answered`, each run still starting 12 git processes and each commit three, and 543 in the cases that run no `main`, most of them readers that ask git over a real history (`trail/phases/phase-9.md`, *Q2* and the third of the four parts). Answering the diff, the merge base and the other readers `answered` leaves real in most of the 32, or keeping fewer runs per arm, would cut it further. Those readers' agreement with git is held by their own classes and by the runs with every reader real, so the choice is the framer's and the orchestrator's.
```

## Confirmations

What matched: no case of the six modules left without its fact held, by
the three methods above. The functions the assertion comparison names as
gone each have a holder. `Test_declared_for_this_branch::test_accepts_a_shared_root_and_tells_it_to_add_the_file`'s
three assertions stand in
`test_the_shared_sentence_says_what_it_searched_and_for_what`
(`tests/skills/test_chain_check.py`, read).
`Test_main::test_s3_the_pull_request_that_adds_agentic_seal_is_judged_under_it`
is `test_s3_the_root_is_named_agentic_seal_beside_the_package`'s two later
instances, with `main` under the name held by
`test_s3_the_check_judges_the_declaration_under_agentic_seal` over
`#shared`. A mutant of `_checked` that read the root's entry at `seal` would
turn `test_s3_a_pull_request_deleting_agentic_seal_declares_nothing` red
(read). `Test_seal`'s one gone function split into two, and the base's
`[an index git cannot list]` instance moved to its own case with the same
assertion (read, `tests/skills/test_seal.py:3274-3289`).

What matched: the broad gate's verdicts keep a real run for each kind of
answer. The two cut `Test_gate` cases are held as `phase-7.md:223-224`
says. `test_refuses_a_red_suite_an_act_after_the_run_loop_turned_to_exit_0`
now asserts `failing on base too` over `red-base`
(`tests/skills/test_broad_gate.py:1919-1944`), and the recorder's readings
of a late hook and an `os._exit(0)` stand in `Test_read_record` (read).
`test_s5_gate_reads_its_key_from_agentic_seal_and_names_it_where_none_is`
now asserts `seal_home` and `broad_command` in place of the stderr line.
`gate` asks exactly those two, in that order, before anything runs
(`skills/verify/scripts/broad_gate.py:1951-1963`, read), and the preflight
case holds the line (read). `arms_answered` replaces `gate.run` for the named
arms alone, and the row and the run at the base stay real
(`tests/skills/test_broad_gate.py:1714-1732`, read).

What matched: `settle`'s seven arm runs and its readers' own cases stand
as the comment above `has_history` names them
(`tests/skills/test_settle.py:234-267`). Each of the seven named arm cases
exists in `Test_main`, and none calls `answered` or takes `drawn` or
`answered_tree`. The `_ancestor` case keeps `order` and `_ancestor` real
(executed: an `ast` walk over the named cases). `answered` makes any
process `lib/gitcmd.py` starts raise where the world has no history
(`tests/skills/test_settle.py:349-354`, read), so a drawn case that leans on
git is told. The 38 functions the comparison names as gone from `Test_main`
are the same names under `Test_report`, `Test_apply` or `Test_module`, with
the same assertions but the world's name. The one exception,
`test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it`, now
asserts `rules.order`'s pair, which is phase 11's verdict at
`phase-11.md:227` (read).

What matched: `at_top` and `guards_answered` replace readers of
`seal.py`, not git, and the classes `guards_answered` names hold each
replaced reader against git: `Test_porcelain` (`tests/skills/test_seal.py:2132`),
`Test_other_worktrees` (`:2216`), `Test_gitlinks_under_root` (`:2681`) and
`Test_refusals` (`:2713`) (read). `tree`, which replaced `snapshot` in ten
refusal cases, compares every byte under the repository, the index among
it, where `snapshot` compared the roots' listings and git's status (read,
`tests/skills/test_seal.py:326-343` against `:220-229` at `ef776317b`).

What matched: the names *Data & interfaces* lists stand at their homes:
`unanswered` and `past_the_bound` (`tests/skills/test_settle.py:188`,
`:206`), `tool` and `configured` (`tests/skills/test_seal.py:462`, `:475`),
`gate_module` and `unquoted_flat` (`tests/skills/test_broad_gate.py:76`,
`:561`) and `layout` (`tests/skills/test_test_layout.py:35`) (read). Fifteen
files import from `test_settle` (executed: `git grep -l`).

What matched: the figures of `changelog.md:5-12` and of the judgment rows
at `frame/plan.md:69-71` are the sums of the artifacts the prompt names
(executed: the sum by module over each `.test_durations` under
`1581-dispatch-1/` to `-10/` and `frame/d45181872904/`). The rows read 601,
253, 107, 106, 105 and 95 s at run 45181872904, and 132, 75, 48, 17, 40
and 8 s in `1581-dispatch-10/`. Which run id each directory holds was not
opened. The five quotes of `pr.md` stand word for word in
`frame/plan.md:67-72`, in the cells their coordinates name (read).

What matched: every mutant the phases record as red over the two gates'
modules is red at `283f33baf`, and the survivors are the phases' own
(executed, *Probes*). Over `chain_check.py`: phase 2's set leaves its 8,
phase 3's its 1, 7, 9, 10, 12, 16, 39, 43, 52 and 70, and phase 9's its 8,
as `trail/phases/phase-9.md:45-47` records. Over `broad_gate.py`: phase 7's
hand-written set leaves 51, 54, 55, 62, 65, 66, 70 and 74, and the
recorder's four are red, as `trail/phases/phase-7.md:44` records. So no
fact that killed a gate's mutant before the rebuild was lost on the way to
the target. As `skills/code-review/SKILL.md` says of a mutation score, this
licenses *tested*, not *safe*.

What matched: a `main` run over `_branch_template`, `_item_template` or
`_bodied_template` leaves every byte under it as it was, `.git` among it.
That holds on a ready and a draft pull request, plain, under `--sealing`
and under `--worktree` (executed, *Probes*). So the cases that take a
template without a copy and run `check` over it cannot change the world a
later case reads (`frame/design.md` S5).

What matched: the narrow runs pass. `bin/test tests/skills/test_chain_check.py tests/skills/test_broad_gate.py -q`
passed 455 and skipped 1 in the clone at `283f33baf` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target. The suite stands `unverified`, and the phase records label it so. | the repository | the orchestrator, once the rounds settle |
| Each module's Windows figure after the rounds, and *Done when* on the first push run on `main` after the release | `frame/questions.md` Q3 and Q4 | the orchestrator for Q3, the repository owner for Q4 |
| The mutant sets of `test_settle.py`, `test_seal.py`, `test_test_layout.py` and `test_release_seal.py` were not run again. The sets of the two gate modules were, so the round's mutation evidence is a sample of the six modules. | `trail/phases/phase-1.md`, `-4.md`, `-5.md`, `-6.md`, `-8.md`, `-10.md`, `-11.md`, each first part | the sealer, where it weighs the phase records' `executed` lines |
| Which run id each dispatch directory of the scratchpad holds. The sums match the rows, and the ids were not opened. | `frame/plan.md:61-71` | the orchestrator, who downloaded them |

## Probes

| Command | Result |
|---|---|
| `python3 -I asserts_diff.py <the module at ef776317b> <the module at 283f33baf>`, for each of the six modules | the gone, added and changed functions summed in the opening paragraphs |
| `python3 phase-9/run_mutants.py phase-2 tests/skills/test_chain_check.py`, the phase scratch directories, in the clone | `seal mutate: 57 mutants, 56 red, 1 SURVIVED, 0 with no verdict (279.5s)`; the survivor is 8 |
| the same with `phase-3` | `seal mutate: 85 mutants, 75 red, 10 SURVIVED, 0 with no verdict (508.7s)`; the survivors are 1, 7, 9, 10, 12, 16, 39, 43, 52 and 70 |
| the same with `phase-9` | `seal mutate: 20 mutants, 19 red, 1 SURVIVED, 0 with no verdict (147.7s)`; the survivor is 8 |
| `python3 phase-7/mut/run_mutants.py phase-7/mut M tests/skills/test_broad_gate.py` | `seal mutate: 78 mutants, 70 red, 8 SURVIVED, 0 with no verdict (211.2s)`; the survivors are 51, 54, 55, 62, 65, 66, 70 and 74 |
| the same with `R` | `seal mutate: 4 mutants, 4 red, 0 SURVIVED, 0 with no verdict (17.7s)` |
| `git status --short` in the clone after the mutant runs | the probe file alone; every shipped file is back as committed |
| `bin/test tests/skills/test_tmp_templates_readonly.py -q -p no:xdist`, a probe in the clone that runs `check` over each of the three templates, ready and draft, plain, `--sealing` and `--worktree`, and compares every byte under the template before and after | `18 passed in 7.09s` |
| `bin/test tests/skills/test_chain_check.py tests/skills/test_broad_gate.py -q` | `455 passed, 1 skipped in 9.46s` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <the branch worktree> --worktree`, before this record | exit 0; no notice at a line of `frame/design.md` |
