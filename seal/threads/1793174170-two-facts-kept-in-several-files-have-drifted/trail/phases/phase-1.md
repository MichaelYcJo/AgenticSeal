# Phase 1: 1793174170-two-facts-kept-in-several-files-have-drifted

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | a1f7a177 |

## What this phase was asked

Build `frame/plan.md`'s phase 1, the gate inventory. Both READMEs' gate
tables gain the `worktree_consent` and `root-migrate` rows. The count and
the lists of gate names leave *First run* and the `seal/` row, in both
editions, and point at the Where column. S1's case is added, and
`test_both_readmes_list_the_stamp_hook` is re-pointed to S2's absence pins.
Each scenario's case is seen red at `5287dd42` before its change.
`frame/questions.md` Q4 is built on its default. `docs/` is not edited:
the frame's `## Rule changes` item is the settle's.

## What this phase found

- **The frame held at this tree.** `hooks/dispatch.py#GROUPS` names 15
  distinct scripts and each table held 13 rows, missing `worktree_consent`
  and `root-migrate`. The coordinates *Removes* gives for the README
  sentences held their words (read). `origin/release/v0.24.0` still
  points at `5287dd42`, so no parallel work item had landed (executed,
  `git log -1 origin/release/v0.24.0`; the ref was not fetched).
- **Q4 met its first option.** `git diff --stat 5287dd42 8e7045e3 --
  hooks/` prints nothing, so `hooks/worktree_consent.py` is as it was at
  the base. The new row describes it from its docstring and `main`: it
  fires after a Bash `git worktree add` that ran and after an Agent call
  with `isolation: "worktree"`, writes an empty file under
  `<git-common-dir>/agentic-worktree-consent/`, and acts in any git repo,
  because `main` asks `optin.repo_root` and not the opt-in (read).
- **The `root-migrate` row's Where cell.** `main` resolves the repository
  with `optin.repo_root` and says in a comment that it does not ask
  `optin.opted_in`, so the cell names any git repo that still holds an
  earlier layout. `rename_state` runs before the repository check at every
  session start, so the cell says that the state rename runs at every
  session start, silently (read, `hooks/root-migrate.py:569-605`).
- **S1 seen red, then green.** At the base README the new case failed with
  exit 1, at index 6 `'routing-edit-gate' != 'root-migrate'` with two
  extra items on the right. With the rows added it passed (executed).
- **S2 seen red.** With "Nine of the thirteen gates wake only under a
  condition." put back into *First run*, the re-pointed case failed with
  exit 1 on `('README.md', 'Nine of the thirteen gates')`. The sentence
  was then taken out again (executed).
- **A reader the frame did not name went red, and the check was the
  defect.** `tests/behaviour/test_first_setup_asks_once.py#test_the_gates_table_says_the_root_may_sit_under_the_git_dir`
  read every table row whose last cell names `` `seal/` `` as a gate row.
  The `seal/` row of the records table now names `` `seal/` `` in its last
  cell, so both editions failed (exit 1, 2 failed, 48 passed). The case
  now reads the gate table's rows alone, from its header to the first line
  that is not a table row. The prose was not bent to the check (contract
  rule 18). It then passed (exit 0, 50 passed).
- **Each new unit was mutated, and each went red.** `seal mutate` printed
  `red` with exit 0 for five mutants: `break` to `continue` in
  `gate_table_names`, `worktree_consent` to `worktree-consent` in
  `README.md`'s row, `root-migrate` to `stub-remove` in `README.ko.md`'s
  row, "게이트 열셋 중 아홉" put back into `README.ko.md` against the S2
  case, and the first-setup case reading from line 0 instead of the gate
  table (executed).
- **Every module that reads a README ran green.** Found with `git grep` on
  the README names under `tests/`, one module per call. Of 36 modules, 35
  passed with exit 0 on the first pass and the first-setup module passed
  after its fix, among them `test_docs_line_wrap.py` (39),
  `test_no_passage_is_pasted_into_a_second_file.py` (8),
  `test_chain_hooks_hardening.py` (28) and
  `test_the_stamp_reaches_the_person_it_is_drawn_for.py` (8).
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py` does not
  exist in this tree. `uvx ruff check` and `uvx ruff format --check` passed
  over the three changed test files (exit 0, executed).
