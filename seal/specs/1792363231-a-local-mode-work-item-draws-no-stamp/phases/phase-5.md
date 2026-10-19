# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 5

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 11b90191 |


## What this phase was asked

The orchestrator ran the measurement itself, because `agents/sealer.md` lost
one word in phase 4. The smith was asked to close the phase on the records
alone:

- write this record from the facts the orchestrator reported, labelled as
  executed by the orchestrator and read by the smith;
- fill `plan.md`'s Status cell with 11b90191;
- add the sealer's evaluation row to `changelog.md` the way #975's fragment
  did;
- run `test_the_verdict_is_recomputed_from_the_records_numbers` and the
  changelog module narrowly.

## What this phase found

**What the orchestrator ran (executed by the orchestrator; read here from
its report).** It ran `noninferiority.py run --agent sealer --rev f99ab3a9
--suite-rev 981b0acc --runs 2 -j 4 --max-cost-usd 10`, which exited 0. It
kept the raw output at `/Users/michael/Documents/GitHub/SpecSeal-worktrees/976-phase-5-raw`,
and `diff -r` against it was clean. It then ran `compare --agent sealer
--phase 5`, with #975's `evals/sealer-phase-4.json` as the old side and this
directory's `evals/sealer-phase-5.json` as the new one. That exited 0 and
wrote `evals/sealer-phase-5.md`. Finally, `check` on that record exited 0.
Both files were committed at 11b90191.

**What the record says (read).** `evals/sealer-phase-5.md` ends with
`Verdict: pass` and "every pass rule holds".

| Measure | #975's phase-4 side | This side |
|---|---|---|
| Tree | `981b0acc` | `f99ab3a9` |
| Suite | `981b0acc`, tree `5c3e8119` | the same |
| Cut short | no | no |
| Preload bytes | 24,700 | 24,690 |
| Spend USD | 3.5731 | 3.3379 |
| Tokens read, every model | 3,239,330 | 2,883,649 |
| Tool calls | 90 | 81 |
| Tokens per tool call | 35,992.6 | 35,600.6 |
| Wall seconds | 452.0 | 140.5 |
| Graders passed | 68 of 68 | 68 of 68 |

Each side is two runs of each of the five cases. Every one of the 34
graders passed both runs on both sides. The preload changed in
`agents/sealer.md` alone. `skills/agent-contract/SKILL.md` hashes the same
on both sides. The two sides ran under different Claude Code versions,
2.1.302 and 2.1.303, as the two `.json` files record.

**What the smith ran (executed).**
`tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`
and `tests/test_the_changelog_is_gathered_at_release.py`, each run alone,
with the exit codes given in the hand-back.

**The changelog fragment.** It carries the sealer's row in #975's shape,
inside the local-trigger entry, because the one word left the sealer's
definition with that trigger. `overview.md`'s row for this measurement is
closed, and it names 11b90191.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
