# Under automation, a mid-run question is refused (#1002) — overview

## Why this work exists

A run routed `automation` now meets a refusal, not a person, when it reaches
for `AskUserQuestion` on its declared branch, so the promise the routing
answer made is held by a hook instead of by prose.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How the predicate compares labels | `spec.md` *Data & interfaces*: the leading phrases "are exactly `ROUTING_LABELS` as a set. This is the comparison `_routing_answer` makes inline today". Today's comparison was `sorted(...) == sorted(ROUTING_LABELS)`, which refuses a label written twice | the comparison made today: each of the three once | the spec names the inline comparison as the one to share, and the owner's direction rules out a near miss passing. `tests/test_an_automation_run_puts_no_question.py#test_a_near_miss_of_the_routing_labels_is_refused` holds a doubled `automation` refused |
| Where the gate row goes | `plan.md` phase 2: "The `README.md` gate row". `CONTRIBUTING.md` §*House rules*: "Both READMEs move together" | both editions | the house rule; `README.ko.md` carries the same gate table |
| The gate's guard on `cwd` | `spec.md` lists no guard. A first draft refused a `cwd` that was no directory before reading anything | no guard | `optin.repo_root` already answers "" for it and `routing.for_branch` answers None for an empty root, so the guard stayed green under its mutation and decided nothing |

## Not verified

| Item | Who must answer |
|---|---|
| that the harness runs a `PreToolUse` hook registered for `AskUserQuestion`, hands it `tool_input.questions` in the shape the cases use, and honours its deny | the orchestrator, by the measurement `questions.md` Q1 names, in the first session after a release carrying the gate is installed |
| the full suite and the repository-wide lint over the phases built | the orchestrator's broad run, before the sealer |

## Not done

nothing

## Fed back into the spec

none
