# Closing memo: 1793251202-the-citation-case-misses-files-and-wrapped-comments

## Why this work exists

The contract-rule citation case read six trees, `CONTRIBUTING.md` and five
file extensions, and no citation wrapped across a `#` comment marker, so a
`contract rule <N>` written in `CLAUDE.md`, a workflow or a hook comment
could dangle while the suite stayed green. It now reads the same corpus as
the section-citation case, through the same `flowing`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The contract-rule reader's input | `frame/plan.md` phase 2: the reader takes a root / `contract_dangling` takes `[(rel, text)]`, and each tree case passes `corpus(root)[1]` | the pairs | `trail/phases/phase-2.md` *What this phase found*, the first of three choices |
| S4 | `frame/design.md`: its own case, passing on both sides / folded into `test_a_record_is_not_read`, red in the old-walk copy | the fold | `trail/phases/phase-2.md` *What this phase found*, the second choice and copy A |
| S5's indented `.yml` fixture | spec silent on its path / `hooks/x.yml` | `hooks/x.yml` | `trail/phases/phase-2.md` *What this phase found*, the third choice |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the orchestrator, through `seal gate` |
| Whether the five new case ids, which have no `.test_durations` key, stay under `STALE_SHARE` | the orchestrator, through `seal gate` |

## Not done

Nothing pins that `test_every_cited_section_exists` reads through `corpus`:
the old walk would still meet its two floors (round 1, a confirmation). The
fixture cases pin `corpus` itself, and the tree case's reader is four lines
beside them.

## Fed back into the design

none
