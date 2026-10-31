# Phase 4: 1793411151-judgment-where-meaning-is-the-question

## What this phase found

**The frame holds at every coordinate the plan's technical context gives
for this phase.** `PRE_MERGE_EVENTS`, the trigger patterns, `unquoted`,
`block_entries`, `continued`, `read_events`, `runners_in` and `inspect`
stand in `deferral_check.py` where the plan says, and
`skills/verify/SKILL.md` *The answerer has to exist* states the five
outcomes (read).

**One sentence of item 10 reads two ways, and the phase took one.** The
item says the tool prints "every workflow file and hook that holds a runner
command" and "exits 1 only where nothing holds a runner". Read word for
word, a pre-commit hook alone would then exit 0. The phase reads the exit
sentence as "no CI file holds a runner", so a pre-commit hook alone exits 1,
as it did before. Grounds: `## Removes` names the trigger reading and its
outcomes and nothing about the local hook, and *The answerer has to exist*
says a pre-commit hook runs on the committer's machine alone, which answers
no deferral to CI. Judged against item 10, the frame's `## Removes` and
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change
removes what stood on the old fact, and the local-hook outcome did not stand
on the trigger reading.

**The other CI systems lose their trigger reading too.** `inspect` counted a
GitLab, CircleCI, Jenkins, Azure, Drone, Travis or Buildkite file as
answering, on the stated ground that those systems run every pipeline on
push by default. That ground is a reading of when the file runs. The phase
names those files as `ci` lines beside the workflows, under the same trigger
line, so no trigger of any kind is read. Judged against item 10, "reads no
trigger".

**The output, line by line, each pinned by a case.** Per kind: a header,
`<kind>: a runner in CI` or `<kind>: NO RUNNER IN CI`; one
`  ci        <file> — <commands>` line per CI file holding a runner; one
`  local     .pre-commit-config.yaml (the committer's machine only) —
<commands>` line; the trigger line, `  trigger   not read: open each ci file
above for whether it runs before the change merges`, printed only where a
`ci` line is; and `  nothing runs it` where no other line is. The limit line
now ends "no trigger is read, so a file named here may run only after the
change merges". The closing sentence on exit 1 is unchanged. The cases
compare the whole output, so no case names an event, and the tab-indented
block, a U+2028 inside a comment, a push-only block, a flow mapping and no
`on:` key give one output.

**A push-only workflow now exits 0, as the frame decided.** Its catch moves
to the reader: `## Removes` says the reader sees `on: push` in the file the
tool named. The SKILL's new paragraph says what that reader looks for, a
workflow that runs on push to the default branch alone or on a schedule.

**Two places the frame's `## Removes` did not name.** `README.md` and
`README.ko.md` list the five outcomes in their `seal deferrals` row; both
rows are rewritten in place (contract rule 19). Three other places name the
removed code and stand. `evals/behaviour/proofer/replay-1791382684-r2` and
`evals/scripts/recurred_truths.json` cite `deferral_check.py:176-206` and
`read_events`. The replay's `scaffold.sh` checks out `7ef6abbf`, so the
citation names that commit's file (read). `.test_durations` names the
removed case ids, and CI's Windows legs rewrite it with `--clean-durations`.

**Seen red.** The new and rewritten cases ran against the tool at
`ce2bc211` before its code changed: 10 failed, 6 passed (executed). The
tab-indented block failed on `tests: resolves` above
`answers   .github/workflows/test.yml (on pull_request) — pytest`, the
scenario's "seen red against `resolves`". The U+2028 row failed at exit 1,
read as `too late` on push. The kept nothing-runs case failed on its added
whole-output assertion only. The six that passed on both trees are the two
kind cases, the missing path, the module case, the census, and
`test_workflows_that_run_no_tests_do_not_resolve`. That last case's `or`
was tightened to two `not in` assertions, because the new header holds "no
runner" and would have made it true by itself.

**Cases removed.** The three parametrised trigger cases (40 rows),
`test_inline_event_list_is_read`,
`test_runner_on_wrong_trigger_is_named_not_counted`,
`test_a_trailing_comment_is_not_read_as_an_event` and
`test_an_unread_workflow_beside_one_that_answers_still_resolves`: each
asserted an event the tool read, or the unread outcome. `seal layout
--pairs` over the module names 0 pairs (executed).

**Mutation.** One `seal mutate` call over `deferral_check.py` at
`7b70b22f`, ten mutants, 10 red, 0 survived (executed). Each is one
boundary of `inspect` or one line `main` prints: the local hook counted as
CI; the other CI files dropped; the trigger line never printed; the trigger
line printed where no CI file holds a runner; `nothing runs it` printed
beside a local line; a file whose text holds `push` dropped, which is a
trigger reading come back; the `ci` line without its commands; the `local`
line dropped; the header always `a runner in CI`; the limit without its
trigger clause.

**Found and not built.** `runners_in` splits a file with `str.splitlines`,
which ends a line at U+2028 where YAML does not. So
`- run: echo hi # note<U+2028>pytest` reads `pytest` as a command line
(executed, one `python3 -I -c` call over `runners_in`), and the tool names
the file as holding a runner. The frame keeps `runners_in`, and the reader
the trigger line sends to the file sees the comment. It is the owner's
second shape, met in the command reading where the frame removed it from
the trigger reading; the hand-back offers it for `seal/follow-up.md`.

**The boundary set ran green.** One `bin/test -n auto` over 94 modules at
`7b70b22f`: the plan's module and every module under `tests/` that names
`deferral_check`, `skills/verify/SKILL.md` or a README, or globs the skills
or a `scripts/` directory. 4541 passed and 3 skipped, exit 0 (executed). The
list was built by `git grep` over `tests/` and is not a census: a module
that reaches a changed path another way is the broad gate's. `seal rules
--check` holds all 265 check lines in 54 rule files (executed).
