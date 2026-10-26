# Phase 2: 1792976216-the-records-and-the-pr-checks-are-two-answers

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | ce6b9afe |

## What this phase was asked

Build phase 2 of `plan.md` after phase 1 closed: `seal pr-checks
[install|remove]`, `seal mode` without the workflow carry, the mode gate's
options, the bootstrap's three options, and every text and test pin
`spec.md` *Places* lists, plus the changelog fragment from `spec.md` *Data &
interfaces*. Build on the defaults of the open questions: Q1 (a), the
workflow file is the record and no config row is added, and Q2 and Q3 as
`questions.md` states them. Do not edit `docs/`; a rule there changes only
through the spec's `## Rule changes`.

## What this phase found

**The frame holds, with two coordinates it did not list** (`read`). Every
row of `spec.md` *Places* stood where it said. The table names lines 71 to
91 of `tests/test_first_setup_asks_once.py` for the two-option pin. Two
more cases in that file located the old `**shared**` label:
`test_an_unmoved_old_layout_is_not_asked_but_told` and
`test_a_bare_specs_is_asked_and_only_the_plugins_marks_are_told`. Both now
read `**shared, records only**`. The second is a case that stands on a fact
this work changes and that this phase may not edit:
`test_the_record_no_longer_says_the_checks_would_refuse`, at the same file's
line 666, asserts `red forever` or `영원히 빨간불` in
`docs/one-root-by-lifetime.md` and its Korean edition. It passes today,
because `docs/` still carries those sentences. It fails at the settle that
applies this spec's `## Rule changes`, which replace them. That run has to
change the case in the same commit.

**Each rewritten pin was seen red before the code** (`executed`). Against
phase 1's commit, the rewritten and new cases of `tests/test_seal.py` failed
38 times. The new case of `tests/test_mode_gate.py` failed on the old
*Shared* sentence. Six cases of `tests/test_first_setup_asks_once.py`
failed before `skills/implement/orchestration.md`, `templates/hygiene.yml`
and the two READMEs were edited.

**One reader tells this plugin's file from anybody else's.**
`seal.py#workflow_at` returns the kind of file at the workflow's path:
this plugin's, absent, a link, unreadable, or one without the clone line.
For the last three it also returns the clause saying why. The report, the
install and the removal all read it. Before this, `remove_workflow` held
that rule alone, and the new install and report would each have held
another copy.

**The install and remove lines lost their two-space indent.** The switch
printed them indented under its own lines, and the switch no longer calls
either. `seal pr-checks` prints each line as the command's whole output.
The sentences that said *local mode commits none* left the removal's
messages. A removal is no longer only the switch to local's.

**The switch to shared names `seal pr-checks install` only where no file is
at the path.** `spec.md` *In* item 4 says *where no such file is there*.
Where somebody else's file stands there, the install refuses, so naming the
command would send a person to a refusal. The switch prints nothing there.

**The guard text says one path now.** The switch's dirty-tree refusal read
*the paths this would stage*. It stages `seal/` only, so the refusal reads
*the path this would stage*, and `Test_refusals` pins the new words. A
switch over an edited workflow file is accepted now, and that row moved
from the refusing case to the accepting one.

**The `.github/` arm of the stage-refused case moved.**
`Test_switch::test_refuses_to_call_a_stage_git_turned_down_staged` ran the
switch twice: under an ignore rule for `seal/` and under one for
`.github/`. The second arm is now
`Test_pr_checks::test_refuses_to_call_an_install_git_turned_down_staged`.
It still runs the `git add -f` the refusal prints, from a subdirectory.

**The command runs as a person types it** (`executed`). `bin/seal
pr-checks`, then `install`, then `pr-checks` again ran in a scratch
repository holding `seal/`. They printed *not installed*, *wrote … (pinned
to v0.22.3) and staged it* and *installed … pinned to v0.22.3*, each with
exit 0. `bin/seal pr-checks add` exited 2. The scratch repository was
removed afterwards.

**The mutation runs** (`executed`, `bin/mutation-check`, after
`ce6b9afe`):

| Unit | Mutants | Result |
|---|---|---|
| `workflow_at`, `pinned` | the link branch dropped; an unreadable file read as `other`; the clone-line test dropped; `pinned` answering "" | 4 red |
| `install_workflow`, `remove_workflow`, `pr_checks` | the root precondition off; the already-installed answer off; the kept answer off; each exit mapping answering 0; the removal's `other` branch off | 6 red |
| `switch`, `refusals`, `main`, the report | each new switch line off or always on (two mutants); the workflow path put back in the guard; `pr-checks` dispatched to `mode`; the action's `choices` removed; the report's not-installed branch off | 6 red |
| `hooks/mode-gate.py#question_reason` | each new option sentence put back to the old promise | 2 red |

**The narrow runs** (`executed`, `bin/test`). The plan's set,
`tests/test_seal.py tests/test_mode_gate.py tests/test_first_setup_asks_once.py tests/test_the_mode_is_a_row_and_a_command.py tests/e2e/teammate`,
exited 0. The 24 modules that read the documents this phase changed
also exited 0: 934 passed and 8 skipped. Among them are
`tests/test_docs_line_wrap.py`, `tests/test_both_editions_carry_the_same_folds.py`,
`tests/test_every_orchestrator_act_names_its_delivery.py` and
`tests/test_gather_changelog.py`. `bin/test-layout --check` refused none of
the four rewritten files.

**The plan's grep** (`executed`). `git grep -n -e 'workflows/hygiene' -e
'install_workflow' -e 'red forever'` outside `docs/`, `changelog/`,
`CHANGELOG.md` and `seal/specs/` finds three kinds of line. The first is
this repository's own workflow, which *Places* keeps. The second is the new
text naming the path `seal pr-checks install` writes. The third is the
line-666 case above, and `.test_durations` entries for case names this
phase renamed, which the runner rewrites.
