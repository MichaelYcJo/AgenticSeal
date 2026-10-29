# Closing memo: 1793273065-the-core-reaches-no-users-repository

## Why this work exists

The plugin's core stood only in this repository's `CLAUDE.md`, so no agent or session in a plugin user's repository read it; it becomes `skills/core/SKILL.md`, which every agent preloads and the preset block imports.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The agents' opening sentence wraps | `frame/design.md` gives the sentence on one line of 115 columns; `tests/behaviour/test_docs_line_wrap.py` holds agent definitions to 88 | the design's words, with one fixed break after "and both" | `trail/phases/phase-1.md` *What this phase found* |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |
| `frame/questions.md` Q2: the one-line block in `~/.claude/CLAUDE.md` puts the core in an interactive and a headless session with no dialog | the orchestrator, on an installed machine after the 0.25.0 release |

## Not done

nothing

## Fed back into the design

none
