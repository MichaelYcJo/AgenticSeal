# Phase 3: 1793157214-the-pr-bodys-facts-come-from-the-records

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 93baffa6 |

## What this phase was asked

Build `frame/plan.md` row 3, the last phase. `evals/scripts/rule_cases.py`
writes each sealer fixture's body as `compose` over the fixture's records,
then the heading, then the hand-written part, in place of
`rule_cases.py#PR_BODY`. The five sealer scaffolds are regenerated. Each
committed scaffold is edited with the Edit tool until it equals the
generator's output, and the generator writes only into the scratchpad.
`frame/questions.md` Q6 is answered here: a hexadecimal placeholder in place
of `BUILD_SHA`, used in the records and the body alike and filled in both
the same way, with the choice recorded in this file. The phase also writes
the work item's `changelog.md` in the shape of the owl thread's fragment at
`74a680c1`, saying what changes for a user of the plugin. The verification
is `frame/plan.md` *Verification this work item owes*. A new case is seen
red once, a regenerated scaffold is proved by the case that holds it equal
to the generator, no `seal mutate` runs, and no paid eval runs (Q4). One
`bin/test` runs over the row's cases and the modules `git grep -l` finds,
and `bin/seal layout --check` and `bin/seal rules --check` run from the top.

## What this phase found

The frame holds against the tree. `rule_cases.py#PR_BODY` and the
`target: BUILD_SHA against main` line stood where the plan's *Technical
context* says. The test that holds the committed cases equal to the
generator is `tests/behaviour/test_evals_layout.py`, as the plan says; the
spawn prompt named it at `tests/evals/test_evals_layout.py`, where no file
stands.

**Q6: the placeholder is `b0b0b0b`.** It is the constant
`rule_cases.py#BUILD_SHA`, and no other line of a sealer fixture holds it.
It stands in the phase record's `Commit` row and the round record's
`target:` line, which `chain_check.py`'s grammar reads as a commit. It also
stands in the body, because `compose` copies the `target:` line. The
scaffold fills it with `$build` in the two records and in the body through
one `sed` each, written by one new helper, `rule_cases.py#fill`. The broad
run's placeholders `RUN_SHA` and `BASE_SHA` are kept. No grammar reads
`trail/gate.md` when `compose` copies it, and the body's `sed` fills them
as the gate record's `sed` does, in the cases whose broad run is on
record.

Decisions settled while writing the code:

- **The body is composed over the records as the generator holds them**,
  before the scaffold fills a placeholder. `compose` copies the `target:`
  line and the gate's table lines unchanged, so filling the body after
  writing it gives the body the filled records would give.
- **The orchestrator's part is `OWN_PART`, `Closes #101.`**, with the
  untrue-body case's README sentence and a blank line before it. The old
  body's paragraph restated the changelog and the phase record, which is
  the restatement this work item removes, so it is not kept.
- **`frame/plan.md` is one of the records `compose` reads.** Its *Phases*
  section is copied, so the plan the scaffold writes and the plan the body
  is composed from are one text in `sealer_case`'s `records` mapping.
- **`rule_cases.py` loads `pr_body.py` by its path**, as `PR_BODY_MODULE`.
  The removed constant's name is not reused, so a reader does not take the
  path for the old body.

The only changes in the five scaffolds are the placeholder, the body and
the body's `sed` line. The generator's output under the scratchpad differed
from the tree in those lines alone, and after the edits `diff -r` of its
`sealer/` against `evals/behaviour/sealer/` exited 0. The proofer, crafter
and framer rule cases were unchanged; the generator's `proofer/` lacks only
the replay and seeded cases, which other generators write.

The case written new is
`tests/evals/test_rule_cases.py::Test_main::test_a_sealer_case_body_is_its_records_then_its_own_part`
(S14). It reads each sealer case's scaffold in the process: every heredoc
written and every `sed` applied in order, each shell value standing in for
a commit. It writes the work item's records and the body under the case's
own directory and runs `pr_body.main` with `--check`, which must exit 0. It
then reads the part under `HEADING`, which must end with `Closes #101.` and
must hold the README sentence in the untrue-body case alone. It does not
run the scaffold through a shell or git. It was seen red once against the
tree before the generator changed. `pr_body.main` exited 1 for
`rule-sealer-sealed` with `no line reads ## Not from the records`, and the
run exited 1.

The existing cases relied on are
`tests/behaviour/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output`
for the regenerated scaffolds, and `test_census` of
`tests/evals/test_rule_cases.py`.

One `bin/test` ran over 19 modules and passed 1254 cases, exit 0. The
modules were the row's four, `tests/evals/test_rule_cases.py`,
`tests/behaviour/test_evals_layout.py`,
`tests/behaviour/test_the_sealer_guarantees.py` and
`tests/skills/test_pr_body.py`. The rest were the modules
`git grep -l -e rule_cases -e "behaviour/sealer" -e pr_body -e "evals/scripts" -e "changelog.md" -- tests`
lists, plus `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
and `tests/behaviour/test_chain_hooks_hardening.py`.
`bin/seal layout --check` and `bin/seal rules --check` each exited 0 from
the repository's top, and `bin/seal layout --pairs` over the test file
named no pair. `uvx ruff check` and `uvx ruff format --check` over the two
changed Python files exited 0.

Whether the five paid sealer cases still grade as before is not run here;
`frame/questions.md` Q4 names the owner's next paid run as its answer.
