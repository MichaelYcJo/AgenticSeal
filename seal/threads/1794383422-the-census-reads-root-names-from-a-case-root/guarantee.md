# Guarantee: 1794383422-the-census-reads-root-names-from-a-case-root

Audited at `9c57c574c` against `release/v0.37.4`, which resolves to
`18a7e18fb` here (`release/v0.37.4@{upstream}`, `origin/release/v0.37.4`
and `release/v0.37.4` each answer `18a7e18fb`; executed).

`trail/gate.md` names `28e690dd9 against 18a7e18fb`. `28e690dd9` resolves and
is an ancestor of HEAD, and `git log --no-merges --name-only
28e690dd9..HEAD ^18a7e18fb` lists one commit, `9c57c574c`, which touches
`seal/threads/1794383422-the-census-reads-root-names-from-a-case-root/trail/gate.md`
alone (executed). `seal pr-body <item> --body <file> --check` exited 0, with
the installed plugin's `seal` and with the tree's `bin/seal`: the body is
`pr.md` above `## From the records` and the records' text below it
(executed). `seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed, and none stands (executed, `cat`, `ls`). No
`seal/parity.json` is tracked, so no legacy comparison is owed (executed,
`git ls-files`).

The route has no frame, no phase record and no round record: `routing.md`
answers Review `straight to the PR` and Implementation `the session`. The
claims audited are therefore those of `gaps.md`, `changelog.md`, `routing.md`
*Why this way* and `pr.md`, against the issue body and the diff.

The `seen red` below was re-run in a `git clone --no-hardlinks` of this
worktree checked out at `9c57c574c`, placed at
`<scratchpad>/<work-item-id>/at-base/`, with `tests/censuses.py` restored from
`18a7e18fb` and then from `9c57c574c`; the clone is clean at `9c57c574c` after
its runs. The tree under audit was not changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The two census cases fail when run alone in a fresh process before the change, 2 failed (`seen red`) | `gaps.md:10`, the issue body's first paragraph | In the clone, `git checkout 18a7e18fb -- tests/censuses.py`, then `bin/test tests/test_conftest.py -q -k Test_census_case -p no:xdist` | Holds. Exit 1, `2 failed, 47 deselected`: `test_accepts_a_target_every_census_passes` and `test_refuses_a_target_one_census_flags_naming_it`, each `FileNotFoundError` on `<tmp_path>/lib/optin.py` raised under `_root_names`, the defect the issue names (executed) |
| The two cases pass alone in a fresh process after the change (the issue's first *Done when* bullet) | `gaps.md:10`, `changelog.md:3` | In the clone, `git checkout 9c57c574c -- tests/censuses.py`, then the same command | Holds. Exit 0, `2 passed, 47 deselected` (executed) |
| `tests/test_conftest.py` passes whole, 49 passed | `gaps.md:10` | In the clone at HEAD, `bin/test tests/test_conftest.py -q -p no:xdist` | Holds. Exit 0, `49 passed` (executed) |
| `_root_names` still returns the plugin's two names (the other reader of the function) | `tests/test_censuses.py:1260` | In the clone at HEAD, `bin/test tests/test_censuses.py -q` | Holds. Exit 0, `231 passed` (executed) |
| `_root_names` reads `lib/optin.py` from the repository the census module stands in, not from `ROOT`, and nothing else changes but the version | `gaps.md:5`, `changelog.md:3`, the issue's *Change* | `git diff 18a7e18fb...HEAD -- . ':!seal/threads'`; `git grep -n` for `_names_read`, `_root_names`, `ROOT_NAME_HOME` | Holds. Outside the work item the diff touches `tests/censuses.py:1453-1459` and `.claude-plugin/plugin.json:4` alone. The new path is `abspath(dirname(__file__)/..)`, the same expression `ROOT` is built from at `tests/censuses.py:41`, so where no case patches `ROOT` the census reads the same file as at the base; the docstring states the new source. `_root_names` has two callers, `tests/censuses.py:1501` and `tests/test_censuses.py:1260` (executed, read) |
| The broad gate still passes (the issue's second *Done when* bullet) | `trail/gate.md`, the spawn prompt's "suite 6046 passed, 8 skipped, chain exit 0" | Not re-run (contract rule 2) | `trail/gate.md` records the run at `28e690dd9 against 18a7e18fb`, with only `trail/gate.md` after it (executed above). The counts are the orchestrator's: `<scratchpad>/<work-item-id>/gate.log` reads `suite ✓ 6046 passed · 8 skipped`, `chain ✓ exit 0`, `exit=0` (read). Answerer of the counts: the orchestrator's run, which CI re-runs on the pull request |
| The version moves to `0.37.4` in this work item, the first to merge into the release | `routing.md:21`, `gaps.md:5`, `pr.md:1` | `git diff 18a7e18fb...HEAD -- .claude-plugin/plugin.json`; `gh pr list --base release/v0.37.4 --state all`; `gh issue view 1498 --json milestone`; `git grep -n 0.37.3` outside `seal/threads/` | Holds. The base reads `0.37.3` and HEAD `0.37.4`; no pull request into `release/v0.37.4` exists yet; #1498 is in milestone `release: 0.37.4`; no other tracked file names `0.37.3`. `docs/releasing/branch-and-release.md:30` states that the version moves in the first pull request into `release/vX.Y.Z` (executed, read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | No frame stands: `routing.md` has no Planning row, on the grounds that the issue fixes the change at its coordinate | The issue's *Change* names one function and its new source; the diff changes that function alone (read) | none |
| the build | The session's commit `b2cfdf904`: `_root_names` reads from the module's own repository; `plugin.json` moves to `0.37.4`. `routing.md`'s `Implementation` row reads `the session`, so no phase record is owed | The issue's *Change* and both *Done when* bullets (executed above); `gaps.md` *Scope confirmation* (read) | none |
| the last round | No round stands: `routing.md` answers Review `straight to the PR`, on the grounds that the change touches no gate, hook or document an agent reads | The diff: a test helper's function and the plugin's version line; no file under `hooks/`, `skills/`, `agents/`, `docs/` or `.github/` changes, and the census flags the same names as before where no case patches `ROOT` (read, executed above) | none |
| the changelog | `changelog.md`: the cache filled from `ROOT`, the two cases raised `FileNotFoundError` alone and passed in the whole suite, the function now reads the module's own repository, and the cases pass in a fresh process | The issue body's second paragraph; the base run's `FileNotFoundError` and the HEAD runs (executed above); the module-level `_names_read` cache at `tests/censuses.py:1450` (read) | none |
| the orchestrator's part of the pull request body | `pr.md`: two quotes of `routing.md` *Why this way*, `Closes #1498.` and the attribution line | Each quote stands word for word once in `routing.md` (executed, a containment check of each quote against the file); the Destination quote holds by the version row above; the Review quote holds by the last-round row above (read) | none |

```seal
target: 9c57c574c against 18a7e18fb
Verdict: sealed
```
