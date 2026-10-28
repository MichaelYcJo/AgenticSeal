# Phase 2: 1793157214-the-pr-bodys-facts-come-from-the-records

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 452cea8b |

## What this phase was asked

Build `frame/plan.md` row 2 and nothing of phase 3. The readers are
rewritten in place. In `skills/code-review/orchestration.md`, the
orchestrator generates the body after `trail/gate.md` is committed, its own
part restates no record, and it generates again after every repair. In
`agents/sealer.md`, a step runs `seal pr-body --check`, and steps 2 and 4
and *Never* read only the part under `HEADING`. The phase also rewrites
`skills/writing-style/outside-the-review.md` *PR 본문*, the chain section and
the languages in `skills/commit-pr-convention/SKILL.md`, the language row in
`templates/setup/config.md`, the README sealer rows, and the *Grounds* of
the acts table. A pin written new is seen red once. A pin moved to new text
is proved by passing. Each sentence `frame/design.md` *Removes* lists goes
in the same commit as the text that replaces it. The verification is
`frame/plan.md` *Verification this work item owes*: no `seal mutate`, and
one `bin/test` over the row's cases and the modules `git grep -l` finds
reading what changed. `bin/seal layout --check` and `bin/seal rules --check`
run from the top.

## What this phase found

The frame holds against the tree with one exception. Every coordinate the
plan's *Technical context* names for this phase stands where it says: the
section of `skills/code-review/orchestration.md`, the sealer's steps 2 and 4
and *Never*, the three pins, and the acts table row.

The exception is the sealer's new step. `frame/design.md` S13 asks for "a
step" that runs the check, beside steps 2 and 4. A new numbered step before
step 4 would renumber steps 3, 4 and 5. `docs/the-review-record.md` cites
`agents/sealer.md` step 3 at two places and step 4 at one, and
`templates/records/sdd-guarantee.md` cites step 5 twice. The policy root is
not edited by a pull request. So the check is the opening act of step 2,
renamed *Check the body's first part, then read, yourself*. It runs
`seal pr-body <item> --body <file> --check`, and on any exit but 0 it writes
`Verdict: withheld reason: <the first line the command printed>` and
returns, as step 1 does. Every step number stays.

Decisions settled while writing the text:

- **One general rule for generating again.** The orchestrator runs
  `seal pr-body` again before every later spawn of the sealer and before
  every `gh api -X PATCH` of the body. Every repair path ends in one of the
  two, so each path is covered. The paths also name the command where they
  list their steps: the withheld repair over records, the repair outside the
  records, the merge of the base, and the stated limit's open pull request.
- **The body file is `<scratchpad>/<work-item-id>/pr-body.md`.** It is named
  as the design names it, beside the existing `gate.log`.
- **A write that refuses is a record to repair.** On exit 1 the
  orchestrator repairs the record its `refused:` line names, commits it and
  runs the command again.
- **The broad run's exit codes are named as the broad run's.** The new
  paragraph on the body sits between the broad run's exit 0 and the
  paragraph that opened *On exit 1 spawn nothing*. That paragraph now reads
  *On the broad run's exit 1* and *the broad run's exit 2*, so neither reads
  as the exit of `seal pr-body`.
- **The comparison table opens the orchestrator's part.** The design's
  *Removes* row states this, and `skills/commit-pr-convention/SKILL.md` says
  it in the moved sentence.

Places outside the row that stated the old fact, found by `git grep` on
"pull request body", were corrected in the same commit (contract rule 19):

- `skills/implement/orchestration.md` *Orchestrator: the order inside a
  ticket*, step 2. It listed the order without the body. It now names
  `seal pr-body` between the broad run and the sealer, and the pin in
  `tests/text/test_the_rules_have_one_owner.py#test_the_order_opens_the_pull_request_after_the_sealer`
  moved to the new sentence.
- `templates/records/sdd-guarantee.md`, the *The parties* placeholder. It
  named "the pull request body" as a party, and it now names the
  orchestrator's part.
- The sealer's frontmatter description, which put the body before the broad
  run.
- `skills/commit-pr-convention/SKILL.md` *The language is the repository's*,
  which said the row governs the whole body. It now points at *Pull request
  bodies* for a chain-routed body.

Left standing: `docs/the-review-record.md` *The guarantee* and
`docs/the-agent-set.md` *What each party writes, and when*. Both are in the
policy root, and `frame/design.md` *Rule changes* carries their new text for
the settle.

The first wording of the README row shared a 15-word run with the sealer's
description. `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
refused it in two cases, and the README row was reworded.

The cases written new:

- `tests/behaviour/test_the_sealer_guarantees.py::TestDefinition::test_the_sealer_checks_the_copy_and_reads_only_the_orchestrators_part`
  (S13).
- In `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_writes_the_body_file_the_sealer_reads`,
  the six new phrases of S12. The three phrases it already pinned stay, and
  `once you have written the pull request body to a file` became an absence.

Both cases collect every missing phrase into one list. Each was run once
against the tree at `9df37072`, before any of the text existed, and the run
exited 1. The S12 case listed all six new phrases as missing, and the S13
case listed all seven of its phrases as missing. So each pinned sentence was
seen red as absent, which is what deleting it shows.

The moved pins, proved by passing:

- `tests/text/test_the_chain_section_has_one_shape.py#test_the_section_states_the_chain_sections_shape`,
  rewritten to the new sentence.
- `test_the_order_opens_the_pull_request_after_the_sealer`, above.
- The language row's cases in
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`,
  unchanged.

One `bin/test` ran over 75 modules. They were the row's named modules and
the modules `git grep -l` lists in `tests` for `pull request body`,
`agents/sealer.md`, `outside-the-review`, `commit-pr-convention`,
`sdd-guarantee`, `"README.md"`, `"README.ko.md"`, `"orchestration.md"`,
`"sealer.md"`, `"config.md"` and `"outside-the-review.md"`. It passed 3119
cases and skipped 9, and exited 0. `git grep -n "list of changes" -- agents
skills` matched nothing. `bin/seal layout --check` and `bin/seal rules
--check` each exited 0 from the repository's top. `uvx ruff check` and
`uvx ruff format --check` over the three changed test files exited 0.

For phase 3: no sealer eval fixture was touched. The sealer's step 2 now
runs `seal pr-body --check`, so an eval's sealer meets it only where the
plugin under evaluation puts `seal` on its PATH. `frame/questions.md` Q4
holds that.
