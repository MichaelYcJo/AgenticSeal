# Phase 3: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 4e3f255b |

## What this phase was asked

Build phase 3 of `frame/plan.md`: the gather goes.
`.github/scripts/gather_changelog.py`, its hygiene step, the step's rows in
`broad_gate.py`, `tests/conftest.py#gathered_entry`, and the gather's
mentions in the comments and docstrings `## Removes` lists.
`tests/github/test_gather_changelog.py` and
`tests/text/test_the_changelog_is_gathered_at_release.py` keep a docstring
and no case, the first with one caseless class carrying
`second-gather-appends`. S9 and S10 hold it, `bin/seal rules --check` exits
0, and the five modules the plan's row names run green. `docs/` is not
edited, and `skills/implement/orchestration.md` is not edited under
`frame/questions.md` Q4's default (a).

## What this phase found

**S9 and S10 seen red, then green (executed).** With the hygiene step
removed and `broad_gate.py#PARTITION`'s row kept, three cases of
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py` failed, the
first naming the row as a step the workflow no longer has. With
`tests/github/test_gather_changelog.py` reduced to its docstring and no
class, `bin/seal rules --check` exited 1:
`docs/release-checklist.md:74: 2. Gather, bump: no test carries the marker
second-gather-appends`. With the caseless class in place it exited 0.

**The frame did not hold for four readers (read, then executed).** Removing
the step and its row left four cases of
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py` red. They count
the steps: 7 in the `release` job, 3 that run only into `main`, and the
verify skill's sentence that two steps have a local answer and no arm, one
of them running a script under `.github/scripts/`. `## Removes` lists none of
them, and the plan's row says the module runs green after the step and its
row go together. The counts are now 6 and 2, and
`skills/verify/orchestration.md:91-94` says one step, the inline one. The
count case built its sentence with the number words alone, so with no step
running a script it would have asked for "no run a script". It now leaves a
kind with no step out of the sentence. `seal mutate` put the old counts back
in the skill, two mutants, both red. `CONTRIBUTING.md` named the step in its
contribution table and its paragraph above it, and `hygiene.yml`'s milestone
step compared itself to "the changelog steps". Each is rewritten. `gaps.md`
holds the divergence, and it is opened in this phase.

**`gaps.md` was owed before phase 4.**
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`
failed on this work item, which had a frame and no closing memo. The
divergence above is the first thing the memo holds.

**The run over every module naming a changed path reached 161 modules
(executed).** `tests/conftest.py` changed, and its basename is in most
modules, so the list is most of the suite. It ran with `bin/test -q`: 6725
passed, 16 skipped and 1 failed, the overview case above, which passed once
`gaps.md` existed. This was not the broad gate. That gate stays the
orchestrator's.

**Comments rewritten to name what remains.** `unverified_check.py`'s list of
fence readers lost the gather and `publish_release_note.py#section_body`. Its
`live_lines` docstring now gives a `seal/config.md` row as the example of a
declaring line, as the frame's rule change does for `docs/the-record-layout.md`.
`issue_claims_check.py` cites its own loading. `publish_release_note.py`'s
`PREPARATION_RE` comment said the preparation pull request "gathers the
release". It now says it moves the version.

**A leftover outside this work.** `tests/behaviour/test_first_setup_asks_once.py`
still passes `fold_ledger`, a script #950 removed. `gaps.md` *Not done*
records it.
