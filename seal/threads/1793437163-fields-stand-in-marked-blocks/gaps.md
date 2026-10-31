# Closing memo: 1793437163-fields-stand-in-marked-blocks

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch after phase 1 | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| The full suite, the repository-wide lint and the typecheck over the branch after phase 2 | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| The full suite, the repository-wide lint and the typecheck over the branch after phase 3 | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| The full suite, the repository-wide lint and the typecheck over the branch after phase 4 | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| Whether a proofer and a sealer that follow the rewritten instructions pass the changed `shape-findings` and `shape-verdict` graders; no eval run is part of this work (`frame/questions.md`) | the next comparison of the proofer and the sealer suites, run on both sides fresh (`frame/plan.md` *Operational impact*) |
| This work item's `trail/rounds/round-1.md` is in labelled lines, and the check refuses it with `NO_ROUND_BLOCK` until it is rewritten into blocks; the rewrite stands in the phase 2 crafter's scratchpad, read whole by the new reader | the orchestrator, by committing the rewrite in a commit that touches only that record (`trail/phases/phase-2.md`) |
| closed `tests/evals/test_seed_defects.py` failed 7 of its 17 cases in two runs during phase 1 | explained by round 1 of #1198, finding 3: the test copies the working tree's `replay_targets.CHECK_FILES` into a scratch repository, `unverified_check.py` loads `hooks/lib/fields.py` from `e52833c6`, and `CHECK_FILES` lists it only from `99ca2178`, so a tree between the two fails the same 7 cases; 7 failed at `e52833c6` and all pass at `968f5ac4` |

## Not done

Phase 1 left the writers' instructions and the eval graders as they stand, because `frame/plan.md` gives them to phase 3; the sealer cases' generator writes the gate record as a run block since round 1's fix pass. So `agents/sealer.md`, `skills/code-review/orchestration.md` (its line naming "the one `Verdict:`" of the guarantee), `templates/setup/config.md` *What no row governs* (`Target SHA`, `Broad gate`) and the sealer eval graders still describe the `Target SHA` row, its `; earlier run:` chain and the one `Verdict:` line. The case `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` no longer lists `chain_check.TARGET` and `chain_check.BROAD_GATE`, which left the code; it lists no key of `hooks/lib/fields.py` yet, since the list must match `templates/setup/config.md`, which phase 3 rewrites.

Phase 2 left the same instructions, `templates/setup/config.md` and the proofer graders as they stand, for the same reason: they still describe a round record's labelled lines and the fix pass's in-place close. It did not write this work item's `trail/rounds/round-1.md` into blocks, because a round record is no write `agents/crafter.md` names outside a fix pass's two lines; `trail/phases/phase-2.md` says where the rewrite stands.

Phase 3 left `skills/code-review/orchestration.md` *Orchestrator: verify before posting* without a step that reads the round record against `templates/records/sdd-round.md` before its commit, which `docs/the-review-record.md` *What the check reads at the pull request* names as what catches a finding written inside a fence, before #1198 and after it. *Scope* item 7 names the preflight reading and not this one, and `skills/implement/acts.md` counts that section's four checks. It left `CONTRIBUTING.md` *What a change to a gate must carry*, **What it reads**, as it stands, because that rule covers every gate, the settle's readers among them, which keep naming near misses (`trail/phases/phase-3.md`).
