# Closing memo: 1793232075-the-living-text-still-calls-the-design-a-spec

## Why this work exists

0.23.0 moved a work item's design to `frame/design.md` and kept calling it
a spec, and the closing memo an overview. A reader met two names for one
document. After phases 1 and 2, the templates, agents, skills, READMEs and
the settle and unverified scripts say "design" and "closing memo". Phase 3
carries the same change into #1020's files once #1020 merges.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Pins the frame's list missed | `frame/design.md` *Living occurrences* names five pins. `tests/text/test_settle_reads_before_it_removes.py` pins five more phase-1 sentences, at base lines `:81`, `:112`, `:150`, `:177` and `:223` | the build | *Scope* item 7: "Each test string that pins a sentence this work rewrites, in the commit that rewrites the sentence." Each was moved and seen red (`trail/phases/phase-1.md`) |
| A Korean line in neither table | `README.ko.md:438`, "스펙 체인", whose English edition `README.md:445` is a phase-1 row | the build | `frame/questions.md` Q2 default (a): a line naming the design is rewritten as its file's row would be |
| A test local renamed with its path | *Scope* keeps identifiers. The mirror case's local `specs` named the directory the frame re-points | the build | The identifiers *Scope* lists are shipped code's. The local is one case's, on the lines item 8 re-points (`trail/phases/phase-2.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch, including `.test_durations` against the renamed parametrize id of `test_each_sibling_is_refused_with_its_own_purpose` | the orchestrator, through `seal gate` |
| Phase 3, and C1, C2 and C3 printing only kept lines across the whole tree (S1), after #1020 merges into `release/v0.24.0` | the orchestrator, when it merges `release/v0.24.0` into this branch and spawns phase 3 |

## Not done

Phase 3 is not built. `frame/questions.md` Q1 stands on its default (a),
which holds it until #1020 merges.

`.test_durations` is not refreshed. `CONTRIBUTING.md` refreshes it from a
`tests` run's artifact, and this branch has had no such run.

`evals/scripts/replay_targets.py:132` still reads `seal/specs/` in the
working tree, where nothing stands since 0.23.0. `frame/design.md`
*Scope* puts `evals/` out, and Q2 (c) leaves the line for the review
(`trail/phases/phase-2.md`).

## Fed back into the design

none
