# Phase 1: 1794465691-the-orchestrator-polls-ci-by-hand

## What this phase found

**The frame holds against the tree at `de5c80f05`.** Each coordinate *Scope*
items 1 to 3 build on stood where `frame/design.md` *Grounding* G13 and G14
and `frame/plan.md` *Technical context* put it: `seal.py#TOOLS`, the
parametrised pair list in `tests/skills/test_seal.py`, `SHIPPED` in
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`,
`.github/scripts/release_seal.py#gh`, `tests/github/test_release_seal.py#GitHub`,
the `gh` stub at `tests/conftest.py:310-392`, and `lib/gitcmd.py#argv`
(read). The bucket table G7 gives is the one in the framer's copy of
`aggregate.go` (read). `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`
needed no edit, as G13 says (executed, the phase boundary run below).

**Each case was seen red against the guard it names.** The cases written
before the module failed at collection against `de5c80f05`, where
`pr_wait.py` did not exist (executed). The case for a last read that holds a
pending check came in `8161db5e4`, after the code, and so did the passed
checks the `UNKNOWN` case serves; the mutants below are their only red. Then
`seal mutate` broke one
guard at a time and ran the case that names it, with
`bin/test tests/skills/test_pr_wait.py -q -p no:xdist -x -k <case>`. Every
mutant read `red`, and each failing line was read for its guard (executed):

| Guard broken | Case that went red | Its failing line |
|---|---|---|
| the empty rollup keeps `gh pr checks` unasked | `test_accepts_a_push_before_any_check_has_reported` | the call order, `checks` where `view` was due |
| `fail` is a bad bucket | `Test_decide::test_refuses_a_failed_check_naming_its_workflow_and_name` | exit 0 where 1 was due |
| `cancel` is a bad bucket | `Test_decide::test_refuses_a_cancelled_check_where_watch_passes_it` | exit 0 where 1 was due |
| the two-minute limit | `test_refuses_to_start_past_two_minutes_with_no_check` | the fake clock's "the wait never ended" |
| the head is compared with HEAD | `test_refuses_a_head_that_is_still_the_commit_before_the_push` | exit 0 where 3 was due |
| the start counts `pull_request` checks alone | `test_refuses_to_start_on_another_events_finished_check` | exit 0 where 3 was due |
| the runs are read before a decision | `test_refuses_to_decide_while_a_run_has_not_completed` | exit 0 where 1 was due |
| the last read is decided only with nothing pending | `test_refuses_to_decide_on_a_last_read_that_holds_a_pending_check` | exit 0 where 1 was due |
| a pending check keeps the runs unread | `test_accepts_a_push_before_any_check_has_reported` | the call order, `runs` where `view` was due |
| `MERGED`, `CLOSED`, `CONFLICTING`, one mutant each | `test_refuses_a_pull_request_that_is_not_open_and_mergeable`, the parameter of each | exit 3, 0 and 0 where 4, 5 and 6 were due |
| `UNKNOWN` keeps the checks unasked | `test_refuses_to_start_while_mergeable_is_never_known` | exit 0 where 3 was due |
| a bucket `gh` does not name is refused | `test_refuses_a_bucket_gh_does_not_name` | `DID NOT RAISE Unanswered` |
| a state `gh` does not name is refused | `Test_once::test_refuses_a_state_gh_does_not_name` | `KeyError: 'DRAFT'` |
| no `gh` on PATH is refused | `Test_gh::test_refuses_where_no_gh_is_on_path` | `TypeError` from `subprocess.run` given `None` |
| `gh`'s non-zero exit is refused | `Test_gh::test_refuses_a_non_zero_exit_naming_the_command_and_its_stderr` | `DID NOT RAISE Unanswered` |
| `git rev-parse HEAD`'s non-zero exit is refused | `Test_head::test_refuses_a_directory_git_cannot_read` | `DID NOT RAISE Unanswered` |
| `--once` reads no HEAD | `Test_main::test_refuses_as_a_process_where_gh_answers_an_error` | stdout naming git's error where `gh`'s was due |
| HEAD is read before any `gh` call | `Test_main::test_refuses_where_git_cannot_read_head` | exit 3 where 2 was due |

Two of those reds are a traceback, `KeyError` and `TypeError`, not an
assertion. Each is what the command prints without its guard, in place of
the exit 2 line the case pins, so each names the guard's absence. The first
runs of the three state mutants and the bucket mutant went red on the hub
running out of answers, a line that named the hub and not the guard. So
`eadb9977a` serves those cases passed checks and completed runs, and the
hub now names a call it was not given an answer for. Run again, they went
red on the exit code as the table gives. The state and bucket mutants ran
at `eadb9977a`, the HEAD-first mutant at `e9c45b77d`, and the rest at
`8161db5e4`. The two later commits changed only those cases and the hub's
message.

**The registration was seen red before `seal.py#TOOLS` named the
subcommand.** The new pair in
`tests/skills/test_seal.py#test_accepts_each_tool_and_hands_its_script_every_argument`
failed on argparse's "invalid choice: 'pr-wait'", and
`test_every_shipped_command_is_classified` failed naming `seal pr-wait`
(executed).

**Five decisions the frame left to the build.**

- **A last read that holds a pending check is not decided.**
  `frame/design.md` *Data & interfaces* read 3 says the command "decides on
  that read". A read with a check still pending has no answer, and exit 0
  asks for every check to have passed or been skipped. So the command polls
  on, and `test_refuses_to_decide_on_a_last_read_that_holds_a_pending_check`
  pins it. Judged against the design's own exit table.
- **An empty list of runs counts as every run completed.** The design does
  not say. A `pull_request` check listed on HEAD means a run exists, so an
  empty list is a lag. But after the start nothing limits the wait, and a
  rule that waited for a non-empty list would wait without end where
  `gh run list` never lists the run. Judged against `frame/plan.md`
  *Alternatives considered* row 8, which keeps the wait unlimited only
  because CI's own timeouts bound it. No case pins this reading.
- **Each `gh` call is bounded at 60 seconds, and a call past that is exit
  2.** The design names no bound. Without one, a `gh` call that hangs on the
  network makes an unlimited wait that CI's timeouts do not bound. This
  follows `chain_check.py#pull_request_from_gh`, which bounds its own `gh`
  call. No case pins the bound. The module docstring states it, and states
  the empty list's reading.
- **Under `--once` the line names the pull request's head, not HEAD.**
  *Data & interfaces* says every line names the SHA, and *Scope* S8 says
  `--once` runs nothing else. So `--once` reads no HEAD, and its line names
  `headRefOid` from the one read it makes. An exit 2 before any SHA was
  read names none.
- **After the start, a head that leaves HEAD keeps the command waiting.**
  Only the orchestrator pushes to a work item's branch (`frame/plan.md`
  *Alternatives considered* row 1). The module docstring states the
  consequence.

**Two departures from the frame.**

- **The docstring cites durable sources, not *Grounding*'s rows.** *Scope*
  item 1 asks each reason to cite its row of *Grounding*. The work item's
  directory leaves the tree when the work ships (`skills/implement/SKILL.md`
  *Document layout — two roots, three lifetimes*), so a citation of
  `frame/design.md` G7 from a shipped script would point at nothing after the
  settle. Each reason in `pr_wait.py`'s docstring states its fact with the
  source a reader can still open: `gh`'s `pkg/cmd/pr/checks/aggregate.go` at
  v2.92.0, and `.github/workflows/test.yml`, which holds jobs that `needs:`
  another. The docstring names none of those jobs, since #1516 changes the
  workflow's matrix in this release. Judged against `skills/core/SKILL.md` *The rule a
  mechanism is kept against*: a fact has one source, and nothing is kept
  beside the tree to stay in step with it.
- **`tests/behaviour/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`
  gained a row for `pr_wait.py` and `2.92.0`.** The phase boundary run
  failed on `test_no_loaded_file_names_a_version_at_or_above_the_running_one`
  naming `pr_wait.py:74`, because gh's 2.92.0 is above the plugin's 0.37.5.
  That number is the tool build a reading was taken on, the class the row
  for `broad_gate.py` and git 2.54.0 already names. The frame names no
  change to that file. The red was seen before `dd1cfc636` added the row
  (executed).

**What each exit prints.** The words are this phase's, as *Data &
interfaces* leaves them to the build, and a case pins each. An exit 2 opens
"could not ask:" where a call failed, and "could not read the answer:"
where a value is none of those `gh` names, both on the one line that opens
`seal pr-wait:`. The tool's stderr follows on indented lines.

**`seal layout --pairs` reports 39 pairs, and none is a duplicate.** Every
case of `Test_wait` calls `wait(12, HEAD)`, so the report pairs them by
their equal arguments. Their input is what the hub serves, which the report
does not read (executed, `seal layout --pairs tests/skills/test_pr_wait.py`,
exit 0). `seal layout --check` passes on the file (executed).

**Rule 12's census of the statements this phase changes.** Phase 1 adds a
subcommand and rewords no rule. The lists of `seal` subcommands were found
by `git grep -n -e pr-body` outside `seal/threads/`: `seal.py#TOOLS`, the
test pair list and `SHIPPED` are the only lists, and the other hits name
`seal pr-body` in prose. That search is a sample. The paragraph that names
`seal pr-wait` to the orchestrator is phase 2's.

**For phase 2.** The exit codes, their outcome lines and `--once` stand in
`pr_wait.py`'s docstring and in its `main`'s help line. Once the paragraph in
`skills/code-review/orchestration.md` names `seal pr-wait`,
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`
holds that it carries the subcommand.

**The phase boundary run.** `bin/test -q tests/skills/test_pr_wait.py
tests/skills/test_seal.py tests/lib/test_config.py tests/lib/test_tables.py
tests/e2e/teammate/test_teammate_flow.py tests/text tests/behaviour` ran at
`a48e77f8a`, after `8d9b8eb73` committed this record, `gaps.md` and the
plan's Status cell: 2194 passed, 9 skipped, exit 0 (executed). `a48e77f8a`
changed only `pr_wait.py`'s docstring, and the run before it, at
`e9c45b77d` with the records in the working tree, gave the same count. The set is the plan
row's files, each test file the phase changed, each test file that names
`seal.py` or `pr_wait.py` (`git grep -l` over `tests/`), and `tests/text`
and `tests/behaviour`, which `CONTRIBUTING.md` names as the tree-wide files.
Its three warnings name rule changes pending in other work items. The run
before the records failed twice: on the version row above, and on
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which asks for this `gaps.md`.
