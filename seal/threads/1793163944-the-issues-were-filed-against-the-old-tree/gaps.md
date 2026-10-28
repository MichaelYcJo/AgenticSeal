# Overview: 1793163944-the-issues-were-filed-against-the-old-tree

## Why this work exists

The issues of 0.24.0 and 0.24.1 were filed against the tree before the rename and the reorganisation, so each is folded to the tree a framer will read, and the milestones state the order the read leaves.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| F2's `docs/` count | `frame/design.md` *F2*: "`docs/` 17"; the same command at `c1b79d40` counts 18 | 18, filed in #1110 with the command | the issue carries the measurement this phase ran (executed); `trail/phases/phase-1.md` names the three path lines the word-bound match counts |
| F3's assert counts | `frame/design.md` *F3*: "`tests/text` 193, `tests/behaviour` 340, `tests/skills` 270, `tests/github` 67, `tests/hooks` 36, `tests/evals` 15", with no command given; the command this phase ran counts 182, 308, 224, 57, 31, 13 | the re-run figures, filed in #1111 with their command | a count with no command cannot be re-run; the frame's own caveat that the figure bounds the class from above stays in the body |

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over this branch; no phase ran a test, because no tree file outside this directory changes | the orchestrator |
| `frame/questions.md` Q1, built on its default (a), moving #920 to `release: 0.24.1` | the owner |

## Not done

nothing

## Fed back into the spec

none
