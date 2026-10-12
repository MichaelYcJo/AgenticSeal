# 1791779434-under-automation-the-guard-asks-nobody — round 4 fixes

Fix range: `5e2e9ad5..7bc54620`.

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | fixed | b6851ffb — the report's paste-ready text: *This row of the guard stops a branch switch …* in English and *이 guard 의 이 규칙은 …* in Korean, in the hook and in `dirty_deny`; S1 was seen red through `mutation-check` with the old sentence put back |
| 2 | fixed | 927497cc — the clause *and git's own output reports what each one did* and its Korean twin are gone from the hook, `dirty_deny`, `docs/worktree-guard-spec.md`, `changelog.md`, `spec.md` In 2 and its S1 row, and ledger S1; S1 was seen red through `mutation-check` with the clause put back |
| 3 | answered | corrected at 97ee27c4 — `option_words` takes the report's text and strips the `git -C <path>` command word and `restore --staged` before scanning; `test_the_press_is_read_from_the_sessions_own_root` now runs the check on a deny issued from another repository, red through `mutation-check` without the strip |

7bc54620 marks round 4's two inherited coordinates naming removed cases
NAME NOT IN TREE, which the record check and `evidence-check --strict`
required.

## Fix surface

| Field | Value |
|---|---|
| Contract changes | none |
| New units | none |
