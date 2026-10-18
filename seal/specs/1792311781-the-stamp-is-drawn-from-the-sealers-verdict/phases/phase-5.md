# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 5

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 55747b46 |


## What this phase was asked

The close, after round 2's fix pass. `overview.md` carries one line of
purpose, the divergences the phases and the fix passes recorded (round 2's
finding 3 among them), `## Not verified` and the fed-back clauses.
`changelog.md` is written for a plugin user: the stamp is the sealer's and
is drawn once at the commit of a `sealed` guarantee; the gate's line reads
`BROAD GATE PASSED`/`FAILED` and draws nothing; `seal-stamp --from` is
unchanged; a clone with a foreign git hooks slot, and local mode (#976),
draw no stamp. It carries the sealer's row, 1483d8ba → 981b0acc, read with
`noninferiority.py#side_numbers`. `plan.md`'s Status cells for phases 4
and 5 are filled, phase 4 at 826cd0da. `questions.md` is the
orchestrator's and is not edited.

## What this phase found

**The fragment's figures, traced** (executed: `side_numbers` over each
file, then the grader passes summed, and `evals/sealer-phase-4.md` read):

| Figure | #969's `evals/reference-sealer.json` | `evals/sealer-phase-4.json` |
|---|---|---|
| Preload bytes | 24,702 | 24,700 |
| Tokens / tool calls | 2,855,195 / 77 = 37,080.5 | 3,239,330 / 90 = 35,992.6 |
| Spend USD (`costUsd`) | 3.3897899 | 3.5730526 |
| Grader passes / grader runs | 68 / 68 (34 graders, 2 runs each) | 68 / 68 |
| Runs, cut short | 10, no | 10, no |
| Suite tree (`sealer-phase-4.md`) | `5c3e8119…` at `1483d8ba` | `5c3e8119…` at `981b0acc` |

The verdict row of `evals/sealer-phase-4.md` reads `pass`, as phase 4
recorded.

**Round 2's finding 3 went to the memo, not to `spec.md`.** The implement
skill makes `spec.md` the framer's and sends a divergence to the builder's
memo with both sides quoted, so the sealer's shortened clause is a row of
`overview.md` §*Where spec and implementation diverged*, with the round's
own words.

**A module nobody had run was red on this branch.**
`tests/test_every_reader_ends_a_line_where_gfm_does.py::test_every_splitlines_call_left_is_named_with_its_reason`
failed on `seal_stamp.py#queue_for_guarantee` and `#_queue_one`, the two
units phase 2 added, which split git's path lists. It was found while
running the fragment's readers, and both units are named with the `GIT`
reason (3820f7bb). It had been red since 0dd09a37: no phase, round or pin
list named that module. Other tree-walking inventory modules were probed
once, and passed (`test_every_agent_reads_the_contract.py`,
`test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`,
`test_every_orchestrator_act_names_its_delivery.py`,
`test_a_format_has_one_reader.py`,
`test_a_process_record_drop_passes_the_readers.py`,
`test_gates_do_not_fail_open.py`). That is a probe, not a seal: the full
suite is the orchestrator's broad run.

**The overview case went from red to green.**
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
failed with the memo removed and passes with it (executed).
