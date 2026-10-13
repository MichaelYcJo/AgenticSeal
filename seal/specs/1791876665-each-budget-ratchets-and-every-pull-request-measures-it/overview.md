# each budget ratchets and every pull request measures it — overview

<!-- The closing memo (implement skill, step 4). Opened at phase 1's first
divergence; later phases add to it as they go. -->

## Why this work exists

Nothing held the repository's size and speed, so each slowdown was found by a
person; after this work every pull request measures each budget and a raised
ceiling has to say why in the body.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How the checker knows a pull request is a release | `spec.md` §*Data & interfaces* lists `--baseline`, `--pr-body-env`, `--ci-run`, `--trend`, `--json` and no flag for the base; the code takes `--base-ref <branch>` and treats `main` as a release | code (phase 1) | `spec.md` §*The budgets*: "A pull request into `main` is exempt from the body rule". The rule needs the branch, and a condition inside the script is one a case drives (T6), where a shell guard in `hygiene.yml` would be a second reading the broad gate's `steps_guarded_off_main` reader also counts |
| The hygiene workflow re-runs on a body edit | spec silent; `hygiene.yml` gains `edited` in `on.pull_request.types` | code (phase 1) | S3 is "the body carries the line → exit 0". Writing the line is an edit and no commit, and a re-run replays the original event's body, so without `edited` the line is read only at the next push |
| The broad gate's partition and its printed counts | `plan.md` names no change outside the checker, the workflow step, the test module and the record-layout row; the tree's `tests/test_the_gate_names_every_step_ci_runs.py::test_every_step_the_workflow_runs_is_classified` refuses an unclassified step | code (phase 1): a `PARTITION` row excluding the step with its reason; the feature and release counts pinned at 10/5 and 12/9; `skills/verify/SKILL.md`'s count sentence and its pin moved with them; the two released rows stating the old counts corrected in the ledger fragment | the partition test is the rule that a step reaches the gate's list, and the count sentences are pinned verbatim (`agent-contract` §14) |
| A `CONTRIBUTING.md` sentence the new step made false | `spec.md` §*Scope* names "CI runs five jobs" for phase 3; §*What a contribution is not asked for* said "The remaining two … are always-on and CAN refuse a contribution", and the budget step is a third | code (phase 1): the sentence rewritten in place, saying what the budget step asks of a contribution | `spec.md` §*Scope*: "The in-place rewrites of sentences the new checks make false" |
| A gate row that becomes a `report` | `spec.md` §*The budgets*: "a row that is gone, fails unless the pull request body carries … `Budget removed:`"; silent on a kind change | code (phase 1): a gate row no longer a gate needs the `Budget removed:` line too | a gate turned into a report lifts its ceiling as fully as a deleted row; reading it as unchanged would be the loophole the removal rule closes |
| The names in `plan.md`'s test-rows table | the frame wrote each case without its `test_` prefix, and `evidence-check`'s records arm refused all sixteen names at exit 2, the lenient reading CI's ledger job runs | record corrected (phase 1): the planted names as the tree carries them, T4 as its two cases, and the five later-phase names marked as not yet planted | the arm reads a backticked name as a token of the tree, and no pytest case can carry the bare name |

## Not verified

| Item | Who must answer |
|---|---|
| The hygiene step on the branch's pull request, green at the pushed tip | the orchestrator, from the pull request's `hygiene` run after the push |
| That an edit to the pull request body re-runs the `hygiene` job and the budget step reads the new body | the orchestrator, by one body edit on the pull request |
| The full suite, the repository-wide lint and the typecheck at this branch's tip | the sealer, after the review rounds settle |
| `test_the_trees_budgets_hold` and the module on the Windows and macOS legs | the pull request's `tests` run |

## Not done

`--json`, which `spec.md` §*Data & interfaces* lists, is not built: no phase
of `plan.md` names it and no case asks for it. Phases 2–4 carry the rest of
the plan.

## Fed back into the spec

Inferred during implementation, phase 1 — a planner may overturn each:

- A `Budget raised:` or `Budget removed:` line may sit in a markdown list item
  and may put the name in backticks.
- An absolute slack is `+N`, optionally followed by the row's own unit word;
  `+N` in another unit is refused.
- A gate row that becomes a `report` row is a removal for the ratchet.
- The summary lists every raise and removal it read, and marks one the body
  does not declare, since the row's band verdict alone reads `holds`.
