# Implementation Plan: 1795860048-what-iadd-claims

## Technical context

The tree as read at `5c18f931`.

`docs/method/iadd.md` *The principles* lists eight principles, each a sentence and the files that state it. Failure scenario of the chosen approach: a principle that restates the routes would drift from `routing-question.md` the first time that file changes, so the principle states the claim and points to the files.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A section of its own beside *The principles* | the scope reads as a rule of the plugin, not as one of the method's principles | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The principle in `docs/method/iadd.md`, the changelog fragment | `uv run --no-project tests/run_tests.py -q tests/behaviour tests/text` | |

## Overlap with the release

#1648 (`1795849897-submodule-pointer-in-typed-diffs`, PR #1673 open on 2026-11-28) changes `agents/inspector.md` and `agents/proofer.md`, and #1677 changes `skills/verify/`. Neither changes `docs/method/iadd.md`, so none meets this work. #1648 carries the release's version move.

## Operational impact

None. This work item carries no version move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-28 | Which prefix the pull request's title takes: `docs:`. | `docs/method/iadd.md` governs nothing itself, and the principle points to rules other files state, so the change is text people read that no party acts on. | `skills/commit-pr-convention/SKILL.md`, its prefix table |
