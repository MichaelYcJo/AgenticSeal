# Closing memo: 1793240966-the-framer-has-no-read-only-probe

## Why this work exists

A question a read-only command answers was queued for the build as an `a measurement` row, and after this work the framer runs that command and writes the answer into the frame.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How phase 1 shows the new graders' regexes | `plan.md` phase 1 *Verified by*: "Each new grader's regex is shown matching a hand-written frame that answers in `## Grounding` and failing one that leaves the answer as a row, run once in a `test_tmp_*` file and deleted". Phase 1 wrote that check as `Test_framer_case`, two cases kept in `tests/evals/test_rule_cases.py` | the kept cases | `agents/crafter.md` *Rules*: "Mutation-test every unit you added ... a unit that stays green while broken has nothing behind it". With the probe deleted, no case in the tree reads the two patterns, and each of the six mutants of phase 1's units would have stayed green |
| The residue rule's wording in `agents/framer.md` | `frame/design.md` *Data & interfaces*: "Every row owes a reason the tree could not answer it" becomes "a reason neither the tree nor a probe could answer it". Phase 2 wrote "Every row owes a reason the tree could not answer it and no probe could either" | the phase 2 wording | `frame/plan.md` *Technical context*: "Every sentence the existing cases pin stays". `tests/behaviour/test_waiver_decided_at_start.py:793` pins "owes a reason the tree could not answer it", and the design's wording would have turned it red |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |

## Not done

nothing

## Fed back into the design

none
