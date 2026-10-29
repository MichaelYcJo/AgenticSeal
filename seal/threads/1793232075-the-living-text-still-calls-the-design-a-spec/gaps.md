# Closing memo: 1793232075-the-living-text-still-calls-the-design-a-spec

## Why this work exists

0.23.0 moved a work item's design to `frame/design.md` and kept calling it
a spec, and the closing memo an overview. A reader met two names for one
document. Now the templates, agents, skills, READMEs, `CLAUDE.md`, the
settle and unverified scripts and chain-check's refusal say "design" and
"closing memo". `implement`'s step 1 is titled *Read the documents that
outrank the code first*, and `code-review`'s first stage is "compliance".

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Pins the frame's list missed | `frame/design.md` *Living occurrences* names five pins. `tests/text/test_settle_reads_before_it_removes.py` pins five more phase-1 sentences, at base lines `:81`, `:112`, `:150`, `:177` and `:223` | the build | *Scope* item 7: "Each test string that pins a sentence this work rewrites, in the commit that rewrites the sentence." Each was moved and seen red (`trail/phases/phase-1.md`) |
| A Korean line in neither table | `README.ko.md:438`, "스펙 체인", whose English edition `README.md:445` is a phase-1 row | the build | `frame/questions.md` Q2 default (a): a line naming the design is rewritten as its file's row would be |
| A test local renamed with its path | *Scope* keeps identifiers. The mirror case's local `specs` named the directory the frame re-points | the build | The identifiers *Scope* lists are shipped code's. The local is one case's, on the lines item 8 re-points (`trail/phases/phase-2.md`) |
| The count of the step-1 heading's citations | `frame/design.md` *Scope* item 5 and `plan.md`'s phase-3 row say "twelve". The frame's own list and `git grep -n -i 'Read the spec'` give ten, plus the heading | the tree | All ten moved with the heading, and the grep prints nothing after `3816dfca` (`trail/phases/phase-3.md`) |
| A pin the gate's prompt did not have | `frame/design.md` S7 verifies the option text by running `tests/hooks/test_review_skill_gate.py`, which read no word of it | the build | Contract rule 14: a change to what a person reads is pinned in the same commit. The pin was seen red under `bin/seal mutate` (`trail/phases/phase-3.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch, including `.test_durations` against the renamed parametrize id of `test_each_sibling_is_refused_with_its_own_purpose` | the orchestrator, through `seal gate` |
| closed Phase 3, and C1, C2 and C3 printing only kept lines across the whole tree (S1), after #1020 merges into `release/v0.24.0` | #1020 moved to 0.25.0 (`frame/questions.md` Q1 at `6d33f30b`); phase 3 built at `3816dfca`, and C1 to C3 there read against the kept table in `trail/phases/phase-3.md` |

## Not done

`.test_durations` is not refreshed. `CONTRIBUTING.md` refreshes it from a
`tests` run's artifact, and this branch has had no such run.

`evals/scripts/replay_targets.py` finds no round record written since
0.23.0. With no flag it reads the working tree and the last two release
tags, `v0.23.1` and `v0.23.0`, under `seal/specs/<item>/rounds/`, and
since 0.23.0 the records stand at `seal/threads/<id>/trail/rounds/`:
`--list` prints nothing. Only `--case`, which reads every tag, still
reaches the 0.22.x records. Teaching it the second layout changes what the
generator picks, outside this work's wording, so it is #1150, filed by the
orchestrator.

## Fed back into the design

none
