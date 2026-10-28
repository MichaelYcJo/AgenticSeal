# Questions for the planner: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

## Answered by the tree, not to be reopened

- **The sweep runs when the conftest is imported, not in an autouse
  fixture.** The issue names a fixture beside `_no_session_in_the_environment`.
  A function-scoped fixture runs after every module-scoped one, and
  `tests/skills/test_broad_gate.py#a_recorded_run` (`:2322`) starts the gate
  as a child from a module-scoped fixture. Its `env=clean_env()` filter could
  not go under a fixture, and the issue's second *Done when* bullet would not
  hold. The `gh` block at `tests/conftest.py:385` to `:416` is the precedent
  for import time (`plan.md` *Alternatives considered*).
- **The sweep removes every name with the `GITHUB_` prefix, not a list.** A
  list has to be edited when a reader takes a new name, and a reader added
  without that edit fails only on a pull request.
- **The pull request still opens after the sealer, and the orchestrator still
  reads a `workflow_dispatch` run.** The issue left the choice to the frame.
  #943's order is the standing rule (`skills/code-review/orchestration.md:161`),
  and after the sweep no case sees the difference between the two events. The
  paragraph names the dispatch run and what it cannot have.
- **"The run the sealer reads" is the local broad run.** The sealer reads
  `trail/gate.md` and runs nothing broad (`docs/the-broad-gate.md` *One act,
  one owner, and the owner is the orchestrator*). `agents/sealer.md` names no
  CI run (executed, `grep -n`). That run's environment holds no `GITHUB_`
  variable, the same as a case's after the sweep.
- **`GH_CREDENTIALS` keeps its four names.** Its comment states `gh`'s lookup
  order, which is a different fact from the workflow's environment. The sweep
  removing `GITHUB_TOKEN` a second time changes nothing `gh` sees, and
  `tests/test_conftest.py#test_the_conftest_takes_every_gh_login_away` keeps
  passing as written.
- **`RUNNER_` variables and `CI` stay out.** No reader in the tree takes
  either from the environment (executed, `git grep -nE` over `*.py`, nothing
  printed).
- **A `delenv` of a value the same case set earlier stays.**
  `tests/skills/test_chain_check.py:1812` and `:1817` and
  `tests/skills/test_unverified_check.py:1816` at `977b6613` switch a case
  between two states it set up itself. They clear nothing the runner set.
- **No case depends on the runner's real `GITHUB_` values.** The broad run
  is taken on the orchestrator's machine, where no workflow sets one, and the
  last work item on this base recorded a passing broad run
  (`seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/gate.md`,
  read; this frame ran no suite). The sweep gives every run that environment.
  Where a case does depend on one, phase 1's plain run of the seven modules
  shows it, and the phase records it as a divergence.
- **`SESSION_VARIABLES` reaching a module-scoped fixture is out of scope.**
  That defect shows on a local run inside a session, which is read before the
  pull request, so it is not this issue's class (`frame/design.md` *Scope*).
- **No file the parallel work items name is touched.** The spawn prompt names
  `pact_check.py`, `coordinates.py`, `hooks/lib/config.py` and `templates/`
  for #913, `skills/verify/scripts/session_cost.py` for #712 and
  `hooks/worktree-guard.py` for #920. This frame edits none of them (read
  against `frame/design.md` *Scope* and *Removes*). A conflict in a file
  they also edit, such as `tests/conftest.py`, is merged as
  `skills/code-review/orchestration.md` *Orchestrator: the pull request opens
  once the sealer seals* says.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| M1 | Do the cases that call `chain.declared_for_this_branch` without setting `GITHUB_HEAD_REF`, and the module-scoped `a_recorded_run`, pass on this pull request's own `pull_request` run of `tests`, on every platform leg? The tree cannot answer it: the pull request opens only after the sealer, and only GitHub starts that run. | a measurement | Green on every leg: the issue's first *Done when* bullet holds under `pull_request` as well as under `workflow_dispatch`. Red on a leg: the fix takes the repair path of the stated limit in `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*. | Phase 1's run with `GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH` and `GITHUB_ACTIONS` exported stands for that run before the pull request. The orchestrator reads the `pull_request` run once the pull request opens, as it does for every pull request. | open |
