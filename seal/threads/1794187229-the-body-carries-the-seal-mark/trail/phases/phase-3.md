# Phase 3: 1794187229-the-body-carries-the-seal-mark

## What this phase found

**The frame holds for this phase.** `templates/setup/hygiene.yml` listed
the default events and the two draft events, `.github/workflows/hygiene.yml`
listed `edited` with the comment the design's `## Removes` quotes, and
`tests/text/test_ci_gives_the_checks_what_they_need.py` held `DRAFT_EVENTS`
and `DRAFT_READER` at line 71 (read). `skills/verify/scripts/broad_gate.py`
runs the check with `--sealing` at line 3082 (read).

**Decision: the `edited` pin is a case of its own, required where
`chain_check.py` runs and refused nowhere.** The draft events' case refuses
them where no step reads the draft state. This repository's issue-claims
step reads the body with no `chain_check.py` involved, so `edited` has a
second reader, and refusing it elsewhere would refuse a workflow that is
right. The new case reads the same `DRAFT_READER` constant, so the script is
named once. Judged against `frame/design.md` *Scope* item 3, "pins `edited`
wherever a workflow runs `chain_check.py`".

**Sentences found standing on the old fact beyond the frame's list,
corrected in `ce06efa7`.** Each was found by `git grep` on `seal mark`,
`pr-body --check` and `chain_check` outside the work item's records, and
the list is a sample (rule 12): the class is every sentence in the tree
that says who reads the body.

- `templates/setup/config.md` *The seal mark* said that none of the rows
  stops anything. Under `yes` the mark line is now compared by the pull
  request's check, so the paragraph says the row stops nothing by itself
  and a differing mark line fails a ready pull request as any other line
  does.
- `templates/setup/hygiene.yml`'s header named what the checks read, and
  the body was not among it. It now names the body.
- `skills/code-review/orchestration.md`, the paragraph on `seal pr-body`'s
  exit 1, named the sealer's check alone as the reader of the body file. It
  now names the pull request's check too.

The sentences in the policy root stand until the settle, since this work
item's subject is the code: `docs/checks/the-pull-request-check.md` *What
the check reads at the pull request*, `docs/forms/the-guarantee.md` *The
guarantee*, and `docs/running/what-a-script-gates.md` *The checks*. Each is
an operation of `frame/design.md` `## Rule changes`. `agents/sealer.md`
step 2, `skills/config/SKILL.md`'s `Pull request seal mark` row and
`skills/writing-style/outside-the-review.md` line 29 say what the sealer's
check and `seal pr-body` do, which this work leaves true (read).

**`git grep` finds neither sentence of `## Removes` outside the frame.**
The two quoted sentences stand only in `frame/design.md`'s own table
(executed: `git grep -n` on each).

**Seen red.** The new case was shown red against each workflow's `types:`
line as it stood before this work, with `edited` removed, by `bin/seal
mutate` (executed). Each run failed on the case's own assertion, naming the
workflow, `chain_check.py` and the missing `edited`: once for
`templates/setup/hygiene.yml`, once for `hygiene.yml`. Both breaks ran on the
uncommitted edit, before `ce06efa7`. The crafter's rule asks for a commit
before a mutation. `seal mutate` restored each file from the bytes it read,
and `git status --short` showed the edits intact afterwards (executed).

**No unit was renamed or moved,** so no census is owed. The phase removed
the two sentences `## Removes` names and nothing else.

**The phase-boundary run.** One `bin/test` command ran the files that read
a path this phase changed: `tests/skills/test_pr_body.py`,
`tests/skills/test_chain_check.py`, `tests/evals/test_rule_cases.py`,
`tests/skills/test_seal.py`, `tests/e2e/teammate/test_teammate_flow.py`,
`tests/github/test_issue_claims_check.py`, `tests/hooks/test_core_start.py`,
`tests/lib/test_core.py`, `tests/lib/test_config.py`,
`tests/skills/test_broad_gate.py` and `tests/skills/test_fold_check.py`.
It also ran `tests/text` and `tests/behaviour`, which hold the plan row's
case. It exited 0, with 3162 passed and 9 skipped (executed, at
`ce06efa7`).
