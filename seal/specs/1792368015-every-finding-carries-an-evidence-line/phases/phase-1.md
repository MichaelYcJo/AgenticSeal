# 1792368015-every-finding-carries-an-evidence-line — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 1fc88d09 |


## What this phase was asked

Phase 1 is the grammar. One `evidence:` row goes into the labelled-line table
in `docs/the-review-record.md`. In a finding it stands exactly once, as
`executed` with one or more backticked commands, or `read` with one or more
backticked `path:line` or `path:first-last` coordinates. A meaning paragraph
says three things. A claim of absence is `executed` only. A later round and
the sealer re-run an `executed` line. Records written before the line are not
findings this check re-reads. The sentence telling an item in flight to
rewrite its records is rewritten. `templates/sdd-round.md` carries the line,
and so do the fixtures in `tests/test_chain_check.py#finding`,
`tests/test_broad_gate.py` and `tests/test_the_release_seal_is_drawn.py`.
Cases S1 to S5 are seen red first. `chain_check.py`'s code does not change,
because the table is the grammar.

## What this phase found

**The frame held where it said the check needs no code.** `finding_of`
builds its rows from every table row placed in a finding, `counted` refuses a
`one` row with no line at the heading and a second at that line, and
`misspelt` is derived from the table. All three are in
`skills/code-review/scripts/chain_check.py` at the base (read). With only the
row added, S1, S3 and S4 refuse and S2 refuses by line (executed:
`bin/test tests/test_chain_check.py -q`, 80 passed).

**The frame's line coordinates had moved after #976 and #943, and its facts
had not.** The table now stands at `docs/the-review-record.md:39-55`, and the
check's readers sit a few lines off the frame's numbers. Each was re-found by
name before it was built on (read).

**Two fixtures the frame did not list build a finding the check reads.**
`tests/test_the_seal_is_taken_once_by_the_sealer.py#finding` and
`tests/test_a_rewritten_definition_proved_non_inferior.py#LABELLED_ROUND_1`
gained the line under the frame's clause for fixtures the suite then refuses.
The second module's two cases failed with the row in place and before the
fixture changed (executed). The first module's fixture changed before its
module ran, so its failure without the line was not seen. Its findings reach
`chain_check`, which S1 shows refuses a finding without the line (read). That
module then ran 373 passed (executed).

**A sixth reader of round records loses every labelled record written before
the row.** `evals/scripts/replay_targets.py#labelled_round` reads records
through the tree's `chain_check.round_of` and leaves out any the check
refuses. `plan.md`'s reader table does not name it. `replay_targets.py --list`
listed 31 targets with truth before the row and 13 after (executed, both at
this phase's tree). Every target lost is a labelled record, the shape 0.22.0
introduced, refused for its missing `evidence:` line. Phase 3 is not
touched, because its suite is pinned at af9c924b. A reader that skipped the
missing line would be a second grammar, which `questions.md` Q2 rejected for
`release_seal.py`. So the reader stands unchanged, and whether the loss is
accepted is a question for the owner (`overview.md`).

**Where each part of the meaning landed.** The shape, the absence rule and the
re-run rule are three paragraphs in §*The round record*, each with its own
`Enforced by:` line. The absence rule's line reads `nothing`, and a case
cannot share that line. The record-before-the-row sentence joined the
rewritten in-flight rule in §*What the check reads at the pull request*,
because both are about which records the check reads again. The
`overview.md` divergence row has the grounds.

**The sealer clause holds with its definition unchanged.** The re-run
paragraph says the sealer weighs no finding and cites `agents/sealer.md`
step 3. That is the frame's reading of #985's fourth point (Alternatives J).

**How each new case was shown red.** S1 to S5, S6's two updates and the
spelling extension were run before the row and its template line existed: 5
failed, each for the missing label (executed). The two pins in
`tests/test_review_axes.py` were run before the paragraphs: 2 failed
(executed). After the commit, `mutation-check` broke each unit once, and a
case went red every time (executed, exit 0 each):

- the row's `How many` changed to `at most one`;
- the `read` form's line made optional;
- the `executed` form's backticks made optional;
- the `Refused as` wording changed;
- the template's `evidence:` line removed;
- the re-run sentence's `## Probes` clause, the record-before-the-row
  sentence and the never-supplied clause, each removed.

**Narrow runs at the phase boundary**, one module per command, every module
that reads the changed files (executed). Twenty passed. In
`tests/test_chain_hooks_hardening.py`,
`test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed
because this item had no `overview.md`. The phase wrote one. The suite is
`unverified` here, and the orchestrator's broad run answers it.
