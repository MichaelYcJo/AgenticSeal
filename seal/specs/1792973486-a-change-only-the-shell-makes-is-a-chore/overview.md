# Overview: 1792973486-a-change-only-the-shell-makes-is-a-chore

## Why this work exists

The owner's principle that a change only the shell makes is a chore, and that no gate is built to catch it, stood in one session's memory; it now stands in `CLAUDE.md`, which every session and agent here reads.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| none | | | |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator's broad run; the repository has no typecheck to run (#951 adds one) |

## Not done

No changelog fragment is written. The change is one principle in this repository's own `CLAUDE.md`, which a consuming repository never receives, and it changes no gate, hook, skill or template the plugin ships; `skills/implement/SKILL.md` and `plan.md` row 1 ask none (read by the smith, `phases/phase-1.md`).

The session memory that held the principle before this work is removed by the orchestrator once this pull request merges, as issue #1031's *Done when* says; it is outside the repository, so no commit here can remove it.

## Fed back into the spec

none
