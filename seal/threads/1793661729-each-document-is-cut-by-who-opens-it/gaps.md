# Closing memo: 1793661729-each-document-is-cut-by-who-opens-it

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1 changed text that agents act on: `agents/framer.md` *A design states its rule changes*, `agents/sealer.md` *The guarantee covers HEAD, and a re-run audits what came after*, and two paragraphs of `skills/code-review/orchestration.md`. No behaviour eval was run for them, since `evals/README.md` *The behaviour suite* makes no later edit owe a run. Whether a framer, a sealer and an orchestrator still act the same is read, not measured | the proofer at review |
| Phase 3 cut `skills/settle/SKILL.md` into it and four files beside it, each named at the step that opens it. Whether a framer opens `skills/settle/rule-changes.md` from its citation, and whether a settling session opens `local-mode.md`, `named-directories.md` and `draft.md` at the steps `SKILL.md` names, is read, not measured; no agent of this run receives the cut files, since agents read the installed 0.29.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| Phase 4 moved the batch, the ladder and the drain out of `skills/implement/SKILL.md` into `skills/implement/orchestration.md`, and the `seal arms` and `seal mutate` sections out of `skills/verify/SKILL.md` into a file each. Whether an orchestrator opens the three new sections at the steps `SKILL.md` names, and whether a crafter opens `skills/verify/seal-mutate.md` before it runs `seal mutate`, is read, not measured; no agent of this run receives the cut files, since agents read the installed 0.29.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |

## Not done

Phase 1 kept each pair `frame/design.md` D6 names on one side. The ten-word
census still lists pairs D6 does not name, and phase 1 left them. Their
grounds are in `trail/phases/phase-1.md` *What this phase found*. Two are
whole passages and not phrases. *The run*'s regression paragraph and the
table in `skills/code-review/orchestration.md` *A regression is routed by
comparing the fix with the frame* state the same routes; both are the
orchestrator's, and the design did not choose a side. `agents/proofer.md`
states the regression line's rule that *The run* states, and the frame's
*Scope* keeps an agent's own rules in its definition.

Phase 2 left
`tests/github/test_release_report.py::Test_module::test_the_table_reads_this_tree_against_the_last_tag`
listing `docs/` with `os.listdir`. Today that lists every policy document,
since the root is flat. Once phase 5 groups it, the case checks
`docs/README.md` alone. Phase 2 left it because the root it reads changes
in phase 5. `Test_documents` holds the report's reading of a group in
the meantime.

Phase 4 left `seal layout --check tests` refusing
`tests/github/test_release_report.py`: its class `Test_documents`, added at
fd331c80b in phase 2, has no `test_accepts_` case and no `test_refuses_`
case, so `tests/skills/test_test_layout.py::Test_main::test_accepts_this_repositorys_tests`
fails. The refusal stands at b29c630cc, before phase 4's first commit
(`trail/phases/phase-4.md`, executed). Phase 4 changed neither file and
builds only its own row of the plan, so the orchestrator routes the repair
before the broad run.
