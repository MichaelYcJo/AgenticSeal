# the record of truth is tests, not coordinates (#944) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. -->

## Why this work exists

The ledger re-read 1,421 prose claims to confirm 1,420, so the record of truth
moves to tests a rule's `Enforced by:` names, and the plugin stops shipping the
ledger.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| the owner's tenet, committed by #944 as its first act | `spec.md` §*Scope* names no `CLAUDE.md` section and no rewrite of `CONTRIBUTING.md` §*What a change to a gate must carry* beyond its ledger sentences / the build's first commit adds `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* below the goal section, moves the goal's `CONTRIBUTING.md` link into it, and rewrites that `CONTRIBUTING.md` section in place so a pull request adding a mechanism names the one it removes, or why none can go, with what that one caught | the build | the owner set the tenet on 2026-10-14 and the orchestrator's spawn ordered it before phase 1, so every session reads it from the tree rather than from one session's memory. `CLAUDE.md` 9,261 → 9,827 B. One released row drifts on it, `seal/releases/0.18.1.md` row O1 under `CLAUDE.md#"## The goal a design is chosen against — verification that runs unattended"@d8810fc4`; its claim, "The goal section's batch sentence is folded into its link to `implement`'s step 1", still holds, and no `Re-read ·` row is written because this work item retires the ledger (phase 2 removes the arm that reads it) |
| phase 1's slice document lost more than its ledger sentences | `spec.md` §*Removes* names no part of `docs/the-record-layout.md` beyond the survivor paragraph, the `survivors.md` row and the `evidence-todo.md` row / phase 1 removed the 64 KB half of the size rule, the `- **A release ledger file.**` bullet, the `CHANGELOG.md` and `seal/releases/` history under it, and the whole §*What is decided and not built yet* (F1–F4) | the build | the owner's tenet: a rule nothing enforced, whose only grounds were ledger rows, and four "decided" items all built, were kept only for having been written. The live rules of F2, F3 and F4 stand with their tests; `phases/phase-1.md` carries the census |
| S6 allowed `nothing — <why>` at a count of 0 | `spec.md` S6 "names a resolving test or `nothing — <why>`" / S4 and §*The replacement* count `nothing` as unenforced | S4, by the owner's answer of 2026-10-14 | S6 is rewritten in place to agree with S4 |
| the resolver refuses a name defined twice | `spec.md` §*The replacement* item 1: "defined twice … fails the run" / `fold_check.py#target_problem` passed a name `named_unit` reports twice | the spec, by the owner's answer of 2026-10-14 | a rule bound to an ambiguous target is not bound; the one resolver both checkers read refuses it, with `tests/test_a_folded_statement_names_what_enforces_it.py::test_a_name_defined_twice_is_no_target` seen red first |
| `## Unenforced rules` lists every rule file | `spec.md` §*The replacement* "one row per rule file at today's count" / 55 files listed, the 11 at 0 held by the family row's ceiling of 0 | the code | a listed row at 0 holds exactly what the family row holds |
| `bin/rules <doc>` | not in the frame / built in phase 1 at the owner's direction of 2026-10-14, relayed by the orchestrator | the owner | a reader that prints and writes no record |
| four ledger-document statements left in phase 2 | `plan.md` phase 3 moves `docs/the-evidence-ledger.md`'s fold, settle, live-lines and baseline statements / phase 2 deleted the retirement-guard statement, the records arm's ship boundary, §*A correction a merge dropped* and the lenient-reader statement, and cut `anchored_rows` from the liveness statement | the build | `enforced-unresolved` named each one's enforcers as deleted by this phase; a statement whose test is gone states a rule nothing holds |
| six test modules deleted before phase 4 | `plan.md` phase 4 deletes the ledger-mechanics modules / phase 2 deleted `test_the_lenient_run_says_what_the_broad_gate_will_say.py`, `test_a_record_states_what_the_tree_has.py`, `test_a_merge_cannot_silently_drop_a_correction.py` and `test_the_ledger_rules_have_one_home.py` with the sweep's two | the build | each one's subject left in phase 2: the CI job and gate arm, the records arm, the correction step, the homes. W2's kernel cases are in none of them |
| the release checklist's §2 is renamed | not in the frame / `## 2. Gather, fold, bump` became `## 2. Gather, bump` once its fold lines went, and `CLAUDE.md`, `CONTRIBUTING.md` and the layout document cite the new heading | the build | the heading named an act the section no longer holds |
| the gate's skip-at-main machinery | `spec.md` §*What happens to each reader* names the three arms / `SKIPPED_AT_MAIN`, `skipped_at_main` and `skipped_line` went too, with a case that no mirrored step skips at `main` | the build | they existed only for the two range arms; kept, they are a branch nothing reaches |

## Not verified

| Item | Who must answer |
|---|---|
| `bin/rules.cmd` runs on Windows: written in lockstep with `bin/fold-check.cmd`, never executed | the pull request's Windows leg |
| the full suite, the repository-wide lint and the typecheck after phase 1 | the sealer, once, after the rounds |

## Not done

Phases 3–5 of `plan.md`. `settle.py#coordinates` and `#segment_of` still
group the fold's report by ledger rows, with their sentences in the settle
skill, the release checklist and both READMEs; once phase 3 removes the data
every item is ungrouped, so phase 3 or 4 removes them. The test docstrings the slice's targets carry are
read as they are: rewriting each first sentence into the rule it guards is
written by whoever moves a rule into a test — #941 and #940 under the reader
criterion — and by #942 when it rebuilds the tests, not here.

## Fed back into the spec

none
