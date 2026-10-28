# Phase 1: 1793171929-the-suite-tells-the-agent-it-is-evaluated

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 5ac41e48 |

## What this phase was asked

Write the text case first and see it red. Then change the author to one
constant, move the sealer's inputs to `.git/<work-item-id>/`, drop the `-c`
flags from the seeded amend, and write the 14 rule cases and the 4 seeded
cases again with their generators. `tests/evals/test_rule_cases.py` reads
the body path from the generator. One paragraph in `evals/README.md` *The
behaviour suite* states the rule. Q1 is built on its default (a). Q3 is
this phase's to answer.

## What this phase found

**The frame holds.** Every coordinate the frame names was opened before the
first edit: `rule_cases.py` at `:205`, `:280`, `:288`, `:370`, `:636` and
`:660`, `seed_defects.py` at `:313`, and `noninferiority.py` at `:611`
(read). The regenerated diff is what the frame says. The rule cases changed
only in their commit lines and the sealer cases' input paths. The seeded
cases changed only in the amend line and the `git remote add origin` URL
(read: `git diff -U0`).

**The case was seen red against the suite as it stood.** At `d7cc30c9`,
`bin/test tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q -p no:xdist`
exited 1, with 128 hits in 18 scaffolds and 5 sealer prompts (executed).
The frame counts 18 scaffolds and 7 prompts before any exemption. The other
two prompts are `replay-1791382684-r2` and `seeded-8a100e13`, whose words
are copied values. After the change, the four modules the plan names passed
with exit 0, 47 passed (executed).

**How a copied value is exempted.** The case renders each replay or seeded
generator's `prompt` and `scaffold` with a token in the place of each value,
once for each way the base ref and the asked paragraph can be present. Each
rendering becomes a regex. Where a case file holds one, the spans of the
copied values are blanked before the scan. A file that holds none keeps no
exemption. The target commit, the round number, the mutation's line number
and the remote URL are matched by their shape but still scanned, so the
exempt values are exactly the frame's list.

**S5's case gained a third reading, found by mutation.** `seal mutate` over
the case's units first left one mutant alive. It was an equivalent mutant
of the fallthrough in `copied_spans`, and it showed that no case read a file
that is not its generator's text. The case now also reads a planted prompt
against the real generator, which finds both words (commit `5ac41e48`).
The record lines, the exemption's scope, the fallthrough, the word boundary
and the typed slots each went red when broken (executed, 5 mutants red over
two runs). In `rule_cases.py`,
`AUTHOR` and `EVIDENCE` each went red when broken, under
`tests/behaviour/test_evals_layout.py -k sealer_cases_are_the_generators_output`
(executed).

**Q3: the seeded amend runs with no identity configured.** The seeded
scaffold case,
`tests/evals/test_seed_defects.py::Test_module::test_the_seeded_scaffold_leaves_round_1s_tree_and_no_copy_of_it`,
passed with `HOME` set to an empty directory and `GIT_CONFIG_NOSYSTEM=1`,
exit 0 (executed). An empty `HOME` still lets git guess an identity from the
host. So the case also ran with a `HOME` whose only config is
`user.useConfigOnly = true`, and passed with exit 0 (executed). Under that
config, a plain `git commit` exits 128 with `Author identity unknown`
(executed). Both flags are gone, as the issue asks.

**Nothing pins the removal of the seeded amend's flags except the text
case.** No case compares a seeded case with its generator. A generator that
gained an `eval` identity again would stay green until its cases were
written again, and the text case would then refuse them.
