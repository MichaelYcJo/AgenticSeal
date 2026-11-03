# Closing memo: 1793661729-each-document-is-cut-by-who-opens-it

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1 changed text that agents act on: `agents/framer.md` *A design states its rule changes*, `agents/sealer.md` *The guarantee covers HEAD, and a re-run audits what came after*, and two paragraphs of `skills/code-review/orchestration.md`. No behaviour eval was run for them, since `evals/README.md` *The behaviour suite* makes no later edit owe a run. Whether a framer, a sealer and an orchestrator still act the same is read, not measured | the proofer at review |
| Phase 3 cut `skills/settle/SKILL.md` into it and four files beside it, each named at the step that opens it. Whether a framer opens `skills/settle/rule-changes.md` from its citation, and whether a settling session opens `local-mode.md`, `named-directories.md` and `draft.md` at the steps `SKILL.md` names, is read, not measured; no agent of this run receives the cut files, since agents read the installed 0.29.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| Phase 4 moved the batch, the ladder and the drain out of `skills/implement/SKILL.md` into `skills/implement/orchestration.md`, and the `seal arms` and `seal mutate` sections out of `skills/verify/SKILL.md` into a file each. Whether an orchestrator opens the three new sections at the steps `SKILL.md` names, and whether a crafter opens `skills/verify/seal-mutate.md` before it runs `seal mutate`, is read, not measured; no agent of this run receives the cut files, since agents read the installed 0.29.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| Phase 5 gave four path-less cross-references in the moved review-record sections the path of the document they now name, and left one that names a plan section (`trail/phases/phase-5.md`). The list came from a scan of italic spans; no case reads such a reference, so whether one was missed is read, not measured | the proofer at review (`frame/design.md` D7) |
| Phase 5 moved every policy document into a group directory. Whether an agent opens the new path from the citation in its definition, the contract or a skill is read, not measured; no agent of this run receives the moved paths, since agents read the installed 0.29.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| Phase 6 changed text every agent receives: the core's new paragraph on cutting documents, the core's routing sentence removed, contract rule 2's sentence on the orchestrator's gate command removed, contract rule 20 retired, and `agents/sealer.md` step 1's citation. No behaviour eval was run, since `evals/README.md` *The behaviour suite* makes no later edit owe a run. Whether an agent acts the same, and whether an orchestrating session still finds the routing section without the core's sentence (the hook's refusal names it), is read, not measured | the proofer at review; the live reading is `frame/questions.md` Q1's |
| Phase 7's replay (S10) holds the past Read calls fixed and measures the two trees under them. It does not measure what a spawn reads under the installed 0.30.0. Most of the framer's reads of the cut skills are ranged, and a range lands on other text at HEAD; reads through `cat`, `sed` or `grep` are not counted. The limits and the readings are in `trail/phases/phase-7.md` | the orchestrator of the first work item run under the installed 0.30.0 (`frame/questions.md` Q1) |

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

Phase 2's open item, the release report's table case listing `docs/` with
`os.listdir`, is closed at 2e7a946c9. Phase 4's open item, `seal layout
--check tests` refusing `tests/github/test_release_report.py`, is closed at
ecaa65963. `trail/phases/phase-5.md` holds both, with the runs that saw each
case red.

Phase 5 left nine lines naming `docs/the-review-record.md`. Each names the
file at an earlier commit, where it still stands: the 0.22.0 replay in
`evals/scripts/replay_targets.py` and its two test modules, and two comments
on the check before #1198. The list and the grounds are in
`trail/phases/phase-5.md` *A departure from S8*.

Phase 6 kept D1's text at its framed length and did not tighten it, since
S2 held without that. The framer's preload stands 3 bytes under the base,
so the next edit that grows the core, the contract or `agents/framer.md`
puts it above again. The grounds and both measurements are in
`trail/phases/phase-6.md`.
