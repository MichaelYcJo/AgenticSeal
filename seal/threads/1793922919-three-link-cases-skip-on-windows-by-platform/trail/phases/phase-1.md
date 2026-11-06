# Phase 1: 1793922919-three-link-cases-skip-on-windows-by-platform

## What this phase found

**The frame holds at the base.** The issue #1247 is the frame on this rung. Read at `296475ec`, `tests/skills/test_agentic_pytest_record.py` carried `skipif(os.name == "nt", reason="a symlink needs privileges on Windows")` at `:868`, `:890` and `:916`, on the three cases the issue names, and the cases made their links with `Path.symlink_to` at `:882`, `:904` and `:929`. `tests/conftest.py:620` defines `symlink_or_skip(target, link, directory=False)`, and its docstring names the platform skip as the form that drops coverage where the privilege is held. Every coordinate the issue and the spawn cite stood where they said.

**The arguments are swapped, not copied.** `Path.symlink_to` is called on the link and takes the target, and `symlink_or_skip` takes the target first and the link second. So `link.symlink_to(root, target_is_directory=True)` became `symlink_or_skip(root, link, directory=True)` in the first two cases. In the third case, `(root / "shared_tests").symlink_to(shared, ...)` became `symlink_or_skip(shared, root / "shared_tests", directory=True)`. The helper asserts that the link's parent exists; `tmp_path` and `root` both exist when the call is made. Judged against the helper's own signature and docstring at `tests/conftest.py:620`.

**The module keeps `os` and `pytest`.** Both are used by other cases of the module, and `uvx ruff check` on the file reports nothing once the three decorators are gone.

**The lint hook removes an import that nothing uses yet.** `hooks/lint-python.py` runs ruff's fixes on each save. The import of `symlink_or_skip` was added in the edit before the three calls, so the hook removed it as unused, and the first narrow run failed with `NameError` in the three cases. The import was added again after the calls. An editor of this module adds an import after the code that uses it, or in the same edit.

**No case is written new, so none is owed a red.** The change moves three existing cases onto an existing helper and adds no behaviour the plugin ships. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* asks the existing cases to prove it, and contract rule 15 binds a new case only.

**Executed: the narrow file passes on the tree `b97741a0` commits.** Run on the working tree just before that commit, which staged it unchanged, `bin/test tests/skills/test_agentic_pytest_record.py -q -rs` exited 0 with 47 passed and no skip. Run verbose with `-p no:xdist -k 'rootdir_named_through_a_symlink or argument_named_through_a_symlink or symlinked_directory_under_the_rootdir'`, each of the three cases printed `PASSED`. `uvx ruff check` and `uvx ruff format --check` on the file both exited 0.

**Executed: a refused link call now skips the three cases with the helper's reason.** One `seal mutate` run replaced `os.symlink(target, link, target_is_directory=directory)` in `tests/conftest.py` with `raise OSError('probe: the link call is made to fail')`. Its `--tests` was `bin/test tests/skills/test_agentic_pytest_record.py -q -rs -p no:xdist -k` over the three cases. The same run was made twice:

| Tree | Verdict, exit | What the three cases did under the break |
|---|---|---|
| `296475ec`, before the change | `SURVIVED`, 1 | `3 passed`: none of them called the helper |
| `b97741a0`, the change committed | `SURVIVED`, 1 | `3 skipped`, as `SKIPPED [3] tests/conftest.py:643: symbolic links are not available here (probe: the link call is made to fail)` |

The verdict word is `SURVIVED` both times because a skipped case is not a failing one. What the two runs show is the outcome moving from passed to skipped. That move is the claim: each case now makes its link through `symlink_or_skip`, and a refused call skips it rather than failing it. `seal mutate` restored `tests/conftest.py` from the bytes it had read each time, and `git status --short` printed nothing after each run.

**The class is listed for the tests tree, and one member stays out of scope.** The class is a link a case makes without the helper. It was listed from what makes a link in Python, `os.symlink` and `Path.symlink_to`, which calls it: `git grep -n 'symlink_to(\|os\.symlink(' -- tests`. A second search for `ln -s`, `mklink`, `CreateJunction`, `hardlink_to` and `os.link(` under `tests/` found nothing. At `296475ec`, outside `tests/conftest.py`, the first search listed the three cases and `tests/github/test_finding_counts.py:255`; at HEAD it lists only the last, where `rounds.symlink_to("held", target_is_directory=True)` makes a link with no skip of either kind. On a Windows machine without the privilege that case fails rather than skips. The spawn names the three cases and nothing else, and `agents/crafter.md` *Never* bars building beyond the request, so it is left as it stands and named in `gaps.md` `## Not done`. `git grep -n 'skipif(os.name'` over `tests/` lists no other platform skip whose reason is a link. The phrase `a symlink needs privileges` now appears nowhere under `tests/`; this record and `changelog.md` quote it as the base held it.

**The version moves with the fragment.** `.claude-plugin/plugin.json`'s `"version"` moves from `0.32.5` to `0.32.6` in the commit that adds `changelog.md`. The spawn names this work item as the first of release 0.32.6 to merge, and `skills/implement/orchestration.md`, the paragraph on which branch the pull request lands on, puts the move in that item's changelog commit.
