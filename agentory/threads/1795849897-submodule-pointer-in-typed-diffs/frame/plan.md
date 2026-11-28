# Implementation Plan: 1795849897-submodule-pointer-in-typed-diffs

## Technical context

The tree as read at `4a63fef1`.

`agents/inspector.md:81` reads the diff as `git diff <base>...HEAD`. `agents/proofer.md:157-158` reads a merge round's code as `git log --no-merges -p <a>..<b> ^<base>` and `git show <merge>`. `agents/inspector.md:63`, step 1's listing, already carries `--ignore-submodules=none`, and `tests/behaviour/test_the_inspector_inspects.py#test_step_1_reads_the_record_and_runs_nothing` pins it. Failure scenario of the chosen approach: a fourth typed read that shows a diff is added later without the flag. No case reads every typed command for it, because a grammar rule over agent prose would guess at what a command is (`skills/core/SKILL.md` *The rule a mechanism is kept against*). A round reads that addition.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A case that greps every backticked `git diff`/`log`/`show` in `agents/` for the flag | it refuses reads whose paths name no submodule, such as step 3's records-only diff, and guesses a command from prose | rejected |
| One sentence in each agent saying every typed git read carries the flag | the command as typed still omits it, and the agent types what it reads | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The flag in the three commands, the cases pinning each, the changelog fragment and the version move | the cases red against `4a63fef1` and green after; `uv run --no-project tests/run_tests.py -q tests/behaviour/test_the_inspector_inspects.py` and the proofer's module | 8de791d6 |

## Overlap with the release

#1593 (`1795849898-body-decision-with-its-question`, branch `fix/1593-body-decision-with-its-question`, routed and not yet framed on 2026-11-28) changes how a pull request body carries a decision's question. It may change `agents/inspector.md`'s reading of the body, which is step 2's text around line 81.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1593 | possibly `agents/inspector.md` step 2 | #1648 | this item carries the version move, and its diff is one flag per command, so it is cleared first and #1593's rounds read the merged line |

## Operational impact

This pull request carries the release's version move: phase 1's commit that adds `changelog.md` moves `.claude-plugin/plugin.json`'s `version` to the patch the release branch names.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
