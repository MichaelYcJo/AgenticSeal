# Phase 1: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 84668705 |

## What this phase was asked

`tests/conftest.py` removes every environment variable whose name starts with
`GITHUB_` when it is imported. One case in `tests/test_conftest.py` pins it,
seen red at `977b6613` first. Every per-case clearing line `frame/design.md`
*Removes* lists goes in the same commit, and the lines it says to keep stay.
`CONTRIBUTING.md` gains one sentence. The check is the seven modules run
twice, once as they are and once with `GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH`
and `GITHUB_ACTIONS` exported. `frame/questions.md` M1 is built on its
default.

## What this phase found

**The frame held against the tree (read).** HEAD `c22e44c5` differs from
`977b6613` only under `seal/`, so every coordinate in *Removes* stood where
the frame says. The class is complete as listed: the clearing lines in
`tests/` that take a name from a variable (`tests/github/test_release_seal.py:281`,
`tests/skills/test_agentic_pytest_record.py:96`, `tests/test_conftest.py:350`)
hold `DRY_RUN`, `SEAL_PNG`, the recorder's variables and git's identity
variables, and none holds a `GITHUB_` name.

**The red run (executed).** The new case
`Test_module.test_the_conftest_takes_every_github_variable_away` ran against
`tests/conftest.py` as it stands at `977b6613` and exited 1, with all six
names left: `GITHUB_ACTIONS`, `GITHUB_BASE_REF`, `GITHUB_EVENT_NAME`,
`GITHUB_EVENT_PATH`, `GITHUB_HEAD_REF`, `GITHUB_REF`. With the sweep written,
it exited 0.

**The phase's runs (executed).** `bin/test` over the seven modules the plan
names exited 0 as they are (1009 passed, 1 skipped), and exited 0 again with
`GITHUB_HEAD_REF=feature/x`, `GITHUB_EVENT_PATH` naming a file holding
`{"pull_request": {"draft": false}}` and `GITHUB_ACTIONS=true` exported (1009
passed, 1 skipped). The skipped case is
`tests/skills/test_broad_gate.py:1124`, which needs `cmd.exe`.
`git grep -n GITHUB_ -- tests` after the commit leaves three clearing lines,
`tests/skills/test_chain_check.py:1810` and `:1815` and
`tests/skills/test_unverified_check.py:1816`, each removing a value its own
case set (S4).

**The exported run catches the defect at S2, and not at S3 (executed, a
coverage probe through `seal mutate` with the sweep's delete replaced by
`pass`).** Under the three exported variables, the three
`declared_for_this_branch` cases of `tests/skills/test_chain_check.py` go red
(four results with the parametrisation): this is #1057's failure, seen on this
machine. `tests/skills/test_broad_gate.py` stays green under the same
mutation, so its removed filters were not load-bearing for these three names
in that module's fixtures. What shows that the gate child of
`a_recorded_run` sees no `GITHUB_` name is S1: the sweep runs at import, and a
child inherits `os.environ`. S3's green run is consistent with that, and is
not evidence of it by itself.

**Mutations (executed, `seal mutate`, each red).** The sweep's prefix
changed to `GITHUB_X`, and the sweep's delete replaced by `pass`, each turn
the new case red. `run_probe` without `env=env` turns it red too, but only
after the second commit: the first version of the case asserted only that
no `GITHUB_` name was left, and a child that inherits the already swept
parent leaves none either way. Commit `84668705` makes the probe report the
names the child was given before the conftest ran, and the case asserts they
are the six. This was seen by reading what the mutation would do, and then
confirmed by running it.

**Edits the *Removes* rows imply but do not name.** The three
`declared_for_this_branch` cases lost their only use of `monkeypatch`, so the
parameter goes from their signatures. `run_check` in
`tests/skills/test_chain_check.py` copied `os.environ` only to pop two names,
so the copy and its `env=env` go, and the child inherits. The existing gh login
case and the new case share the child through `run_probe`, a helper beside
`PROBE`.

**The CONTRIBUTING sentence is pinned.** `tests/text/test_the_suite_runs_with_gh_logged_out.py`
already pins that paragraph's sentences, so it gains a needle for the new
sentence (contract rule 14), seen red with the sentence deleted in place
(exit 1, the needle named) and green with it restored. The frame named no
such assertion; `gaps.md` records it.

**ruff (executed).** `uvx ruff check` and `uvx ruff format --check` over the
nine changed Python files both exit 0. ruff is not on PATH here; `uvx` is
the form `CONTRIBUTING.md:98` names.
