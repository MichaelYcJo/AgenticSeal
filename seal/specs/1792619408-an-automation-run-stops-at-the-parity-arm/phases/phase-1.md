# 1792619408-an-automation-run-stops-at-the-parity-arm — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 9cf4b376 |

## What this phase was asked

The pull-request half, built first, so the branch never holds a state in
which the commit-time stop is gone and nothing at the pull request stands in
its place. The `original:` row of the grammar table in
`docs/the-review-record.md` *The round record*, edited in the build commit,
because `chain_check.py#grammar` loads that table at run time. One reader of
`seal/parity.md`'s `Baseline commit` row in `hooks/config.py`, and
`hooks/gate.py` loaded by path, which is `questions.md` Q2's default.
`chain_check.py`'s refusal of S4, S6, S10 and S11, reading the document-root
rule from `hooks/gate.py#DOC_ROOTS` and `touches_code` rather than a copy.
The `templates/sdd-round.md` placeholder, `agents/warden.md` step 5, and
`skills/legacy-parity/SKILL.md` *Recording the comparison*. Cases S4 to S11
in `tests/test_chain_check.py`, the refusal cases marked
`@pytest.mark.rule("parity-at-the-pull-request")`.

The owner's direction for the build: no symbol a reader can trip on as
syntax, no value stated twice, no spelling a near miss could pass, and an
instruction that names who acts, when, on which file and what counts as
done.

## What this phase found

- **The frame held.** `hooks/gate.py#arms_missing` lines 162 to 168,
  `chain_check.py#grammar` and `GRAMMAR_DOC`, `hooks/config.py#read_table`
  and the `| Field | Value |` table of `templates/parity.md` stood where
  `plan.md` *Technical context* says. `git grep -n 'Baseline commit' --
  hooks skills .github bin` returned `skills/implement/orchestration.md:249`
  alone before the build, and no round record in `seal/specs/` or `evals/`
  opens a line that reads as `original:` in any case or emphasis.
- **Q2, answered by the work.** The reader is
  `hooks/config.py#baseline_commit`, beside `read_table`, which it reads the
  table through. `chain_check.py#parity_readers` loads `hooks/config.py` and
  then `hooks/gate.py` by path. The order matters only in a process that
  loaded no routing reader: `gate.py` imports `optin` and `routing` by name,
  and `config.py` is what puts `hooks/` on `sys.path` there. A case runs that
  process. The repository-relative config path is built from
  `optin.HOME` and a new `optin.PARITY_CONFIG`, which `optin.parity_config`
  now reads too, so the file name is spelt once.
- **`original:` is a row the check reads a meaning from.** It joins
  `chain_check.py#READ_ROWS` at `at most one` only, so a table that moves
  the row into a finding, drops its `commit` part or makes it `one` stops
  the check at exit 2. The paragraph under the table that names those rows
  was edited in the same commit; `overview.md` holds that divergence.
- **A line the table refuses is refused once.** `original_of` counts a line
  spelt otherwise, as `misspelt` reads it, as a line, so a record holding
  `Original:` meets the grammar's refusal at that line and no second
  refusal saying it has none. The same holds for a line inside a finding and
  for a second line.
- **The config's refusal is printed once per run**, not once per work item,
  because `originals_of` reads `seal/parity.md` once for every work item the
  run judges through the review chain.
- **S5 cannot be seen red against the tree as it stood**, since a check that
  does not exist refuses nothing. It was seen red under `mutation-check`
  instead: the prefix comparison replaced with equality fails both of its
  cases.
- **`legacy-parity` *Recording the comparison* gained the `original:`
  paragraph in this phase.** Its sentence that committing code with no
  record makes the gate ask stays as it is until phase 2 changes the gate.
- **The handoff's base reads two ways.** The local `release/v0.22.3` ref in
  this clone stands at 5aed51cb, and `origin/release/v0.22.3` at eae7f0ad,
  the commit this branch is rebased onto. `chain_check.py --baseline
  release/v0.22.3 --worktree` therefore also names #1006's squash as
  carried. Both bases were run, and both exit 0 with only the records this
  work item does not hold yet.
