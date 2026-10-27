# Phase 2: 1793140810-each-directory-holds-everything-in-one-level

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | dd01eb7e |

## What this phase was asked

Build `frame/plan.md` row 2 and nothing of phases 3 to 5. The 13 modules
move into `hooks/lib/` by `git mv`, and every reader follows:

- each gate's `sys.path` insert, and `dispatch.py#opted_in`;
- the scripts outside `hooks/`, `bin/seal`, `bin/seal.cmd` and
  `run_tests.py`;
- `tests/conftest.py#load_hook_module` and its callers;
- `tests/test_launch.py#loaded_by`, and `replay_targets.py#CHECK_FILES`
  reading both spellings;
- the freeze case's `FROZEN` and the rider's paths, the `KEPT_FILES` of both
  censuses, `ruff.toml`'s comment and every prose citation;
- each test file's `TARGET` at `hooks/lib/`.

`hooks/hooks.json` stays where it is. `hooks/lib/cmdline_base.py` stays byte
for byte below its rider. A moved module owes no new case, no red run and no
`seal mutate`. Three cases are new, and each is seen red once: every gate
of `dispatch.GROUPS` loads in a fresh interpreter, a commit holding
`hooks/lib/blocks.py` has it copied by the replay, and `loaded_by` reaches a
module under `hooks/lib/`. The phase ends with one `bin/test` command over
the 28 hook module test files, the four named modules and the modules
`git grep -l` finds loading a moved module. Every path is joined from single
segments, so that Windows gets one separator.

## What this phase found

**The frame holds, with one departure in the gate inserts.**
`frame/design.md` *Data & interfaces* says each gate "inserts
`os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")` where it
inserted its own directory". Twelve gates had their own-directory insert
replaced by the `lib` insert. Three gates also import `worktree_consent`,
which is a gate and stays at the top of `hooks/`: `question-gate.py`,
`routing-edit-gate.py` and `worktree-guard.py`. Each keeps its own-directory
insert and adds the `lib` insert after it. A gate loaded alone finds
`worktree_consent` only through its own-directory insert.

**The kept files of `vacated_paths` are a constant of their own.** It is
named `tests/censuses.py#VACATED_KEPT_FILES` and holds
`hooks/lib/cmdline_base.py`. The name `KEPT_FILES` was already taken by
`old_names`. That census's entry now reads `hooks/lib/cmdline_base.py`. The
sweep of every tracked file in `tests/test_censuses.py` passes the frozen
file whole through this constant. Its docstring below the rider names
`86256492`'s `hooks/optin.py`, a spelling the census refuses and a line that
cannot change.

**Readers that shrink instead of failing (contract rule 12).** The plan's
`git grep` for a moved module's file name found these code readers. Each one
now reads `hooks/lib/`:

- `hooks/dispatch.py#opted_in`;
- `hooks/lib/config.py:61` and `hooks/lib/routing.py:51`, which read the file
  beside themselves and so did not change;
- `skills/code-review/scripts/chain_check.py#HOOKS`;
- `skills/implement/scripts/seal.py#HOOKS` and `#PLUGIN`, where `PLUGIN` now
  goes up two levels;
- `skills/settle/scripts/settle.py` and `fold_check.py`;
- `skills/verify/scripts/broad_gate.py`, `pact_check.py#HOOKS` and
  `unverified_check.py#HOOKS`;
- `.github/scripts/rules.py#SIBLINGS`, `release_seal.py#readers` and
  `run_tests.py`;
- the `sys.path` inserts of `gather_changelog.py`, `issue_claims_check.py`,
  `plugin_directory_check.py`, `publish_release_note.py`,
  `tracker_labels.py` and `evals/scripts/rule_cases.py`;
- `evals/scripts/replay_targets.py#CHECK_FILES`.

The test files that join `"hooks"` and a module name also follow. The
listings over `hooks/`, `templates/` and `tests/` are these:

- `tests/test_the_frozen_reading_never_grows.py` (`rglob`) and
  `tests/test_censuses.py:975` (`os.walk` over `tests`) already read
  recursively.
- `tests/test_a_record_carries_no_comment.py` reads `templates/records/` and
  was phase 1's.
- `tests/test_the_root_migrates_itself.py#test_no_hook_names_the_0_3_x_roots`
  listed `hooks/` one level deep. After the move it would have read no
  module, so it now lists `hooks/` and `hooks/lib/`.
- `tests/test_one_word_one_meaning.py:922` lists the top of `tests/` and
  belongs to phase 3, which moves the test files.

**Two loader calls had no path in them for the census to see.**
`tests/test_root_migrate.py` called `load_hook_module("routing.py", ...)` and
`load_hook_module("optin.py", ...)`. The census reads `hooks/<name>`
spellings only, so it did not flag them. The first narrow run failed on both
calls, and both now pass `lib/<name>`. No other bare loader call remains:
`git grep` for `load_hook_module`, `load_hook` and `run_hook` with a moved
module's bare name finds none.

**`load_hook_module` and `run_hook` split their argument on `/`.** A module
is passed as `lib/optin.py`, and the path is joined from single segments.
`tests/test_dispatch.py#hooks_copy` does the same for the files it
overwrites.

**History stays cited at its commit.** Five lines named the old path as a
fact of the past. Each is now written in the `<commit>:<path>` form, which
the census passes:

- the rider of `hooks/lib/cmdline_base.py`, whose bytes below `START` are
  unchanged and still match the hash;
- `tests/test_the_frozen_reading_never_grows.py#PINNED`;
- `tests/test_routing.py`'s comment on `3911a8cf`;
- `docs/worktree-guard-spec.md`;
- the comment above `tests/censuses.py#KEPT_FILES`.

Two lines keep the old path on purpose, each under a `vacated_paths`
exemption. They are the `hooks/blocks.py` entry of `CHECK_FILES` and its
case's parameter.

**Two messages a person reads still say `hooks/`, and both still hold.** The
import refusals in `hooks/lib/config.py` and `hooks/lib/routing.py` say "This
file ships beside it under `hooks/`". The refusal in `seal.py` says "the
plugin that holds `hooks/`". Each is true at the new path, so the text did
not change and no case pin moved.

**The two failures phase 1 recorded now pass.** One was the census sweep on
`frame/plan.md:87`, the other the overview check that wanted a `gaps.md`.
Both were answered after phase 1, in `c28dff5a`.

**New cases, each seen red against the tree after the `git mv` and before
its reader changed:**

- `tests/test_dispatch.py::Test_module::test_every_gate_loads_from_its_own_file_in_a_fresh_interpreter`
  failed with a `ModuleNotFoundError` for every gate that imports a module.
  An example is `mode-gate.py`: "No module named 'config'".
- `tests/test_replay_targets.py::Test_module::test_a_commit_has_its_hook_module_copied_where_it_holds_it[lib]`
  failed with `FileNotFoundError` on the copy at `hooks/lib/blocks.py`. The
  `[before]` parameter passed both before and after.
- `tests/test_launch.py::Test_module::test_a_hook_reaches_the_modules_under_lib`
  failed with `set() == {'hooks/lib/a.py', 'hooks/lib/b.py'}`.

**Existing cases relied on:** the 80 modules of the narrow run. They are the
28 hook module test files, `tests/test_the_frozen_reading_never_grows.py`,
`tests/test_chain_hooks_hardening.py`, `tests/test_censuses.py` and
`tests/test_replay_targets.py`. The others are every test file that
`git grep -l` finds loading a moved module, the test file of each script
whose hooks path changed, and `tests/test_docs_line_wrap.py`. The run passed
5197 cases and skipped 6. `bin/seal layout --check` and
`bin/seal rules --check` from the tree both exited 0.
