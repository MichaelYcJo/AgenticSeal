# 1792619289-the-pull-request-check-parses-rule-changes — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 22bfec31 |

## What this phase was asked

`skills/code-review/scripts/chain_check.py` gains `rule_changes_read`, the
constant `RULE_CHANGES_SAYS`, the call in `main` beside `frame`, and exit 2
where the loader fails, all as `spec.md` *Data & interfaces* states them.
The reader is `rule_changes.parse`, reached through
`unverified_check.py#rule_changes` with `unverified_check.py#policy_root`:
one reader, no copy. `tests/test_chain_check.py` gains S1 to S10, each
carrying `@pytest.mark.rule("rule-changes-read-at-the-pull-request")`, and
each refusal case is seen red against the frame commit's `chain_check.py`
first.

In the same commit, the sentences `spec.md` `## Removes` names are rewritten
in place: the module docstring's arm list and both `hygiene.yml` chain-step
comments. `skills/settle/SKILL.md` *Rule changes* gets one pointer sentence.

The owner's direction for the build: no symbol a reader can trip on as
syntax, no value stated twice, no spelling a near miss could pass, and an
instruction that names who acts, when, on which file and what counts as
done. At the phase boundary, `tests/test_chain_check.py`, every module
naming `chain_check` or `hygiene.yml` and nine named meta modules run, with
`bin/rules --check`, `bin/fold-check`, `bin/settle --released-at HEAD`,
`bin/unverified-check seal/specs/`, `chain_check.py --baseline
release/v0.22.3 --worktree`, and ruff one file per argument.

## What this phase found

- **The frame held.** Every coordinate `plan.md` *Technical context* names
  was where it said at the frame commit, and `chain_check.py` had not
  changed since then, so "red against the frame commit" and "red against the
  tree before the build" are the same run.
- **S7 as written is S1.** The fixture declares `Planning` `the session`, so
  S1 already covers that answer. The S7 case declares `framer` instead, the
  answer nothing else covered. It is a row of `overview.md`.
- **A work item with no `spec.md` never reaches the reader.**
  `rule_changes_read` returns before the loader where git carries no spec,
  so a reader that will not load stops only a check that has a spec to read.
  S10's first half holds it. The mutation that drops the guard leaves every
  other case green, because the parser reads an empty text as a spec with no
  section.
- **S8 also carries the `judged-where-carried` marker**, since it is a case
  of that rule as well as of this one.
- **The docstring's exit line was rewritten too.** It named a grammar table
  as the one cause of exit 2, and a reader that will not load is now a
  second. No sentence was removed for it.
- **The S1 case pins the refusal's text.** It compares the printed line with
  `rule_changes.parse` on the same text, so no parser reason is spelt in the
  test. The constant's own words are spelt once there, as `SAYS`, because a
  case built only from `chain.RULE_CHANGES_SAYS` would pass any edit to it.
