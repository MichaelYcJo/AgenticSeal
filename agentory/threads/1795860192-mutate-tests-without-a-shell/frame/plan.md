# Implementation Plan: 1795860192-mutate-tests-without-a-shell

## Technical context

The tree as read at `8e130543`.

`main` calls `command_words(args.tests)` and refuses only an empty list, and `_run` starts the words with `subprocess.Popen`. Failure scenario of the chosen approach: a person who wants two commands must write `sh -c '…'`, which a machine with no POSIX shell cannot run. That is the cost G1 accepts, because the alternative measures nothing in silence.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Run `--tests` through `sh -c` | no `sh` on a Windows runner; the shell becomes the direct child the bound and the verdict read | rejected (G1) |
| Read operators with `shlex` in non-POSIX mode | refuses `\;`, which a shell reads as one literal character (G2) | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 to 4 | the new cases red against `8e130543` and green after; `uv run --no-project tests/run_tests.py -q tests/skills/test_mutation_check.py tests/text tests/behaviour`; `uvx ruff check` and `format --check` on both Python files | d86d5c6f |

## Overlap with the release

#1648 (PR #1673) changes `agents/inspector.md` and `agents/proofer.md`, and #1676 changes `docs/method/iadd.md`, read 2026-11-28. Neither meets this work.

## Operational impact

A `--tests` that held a shell operator outside quotes ran its first program alone. It is now refused with exit 2. This work item carries no version move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-28 | Which prefix the pull request's title takes: `fix:`. | The command reported `SURVIVED` for a run in which the cases that watch the unit never ran, against the rule in `skills/verify/agentic-mutate.md` that every run which measured nothing exits 2. | `skills/commit-pr-convention/SKILL.md`, its prefix table |
| 2026-11-28 | Whether a round follows round 3's fix pass: yes, round 4, a verifying round on that fix. | The findings fell from five to three to one, each round's a regression of the fix before it, so the run converges. The one fix changes a test's case, outside the records, which the row *No fix that no round reads* gives to a round. Round 4's target is that one case. | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* |
