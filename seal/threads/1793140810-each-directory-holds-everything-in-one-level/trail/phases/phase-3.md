# Phase 3: 1793140810-each-directory-holds-everything-in-one-level

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 18fb2091 |

## What this phase was asked

Build `frame/plan.md` row 3 and nothing of phases 4 and 5:

- the 63 module test files move by `git mv` into `tests/hooks/`,
  `tests/skills/`, `tests/github/` and `tests/evals/`, each to the area of
  its `TARGET`'s first path segment;
- each moved file imports `ROOT` from `tests/conftest.py` instead of
  computing it from `__file__`;
- `test_layout.py --check` refuses a module test file outside its area, and
  `CONTRIBUTING.md` *The test layout* is rewritten in place to match;
- `.github/workflows/test.yml:238`, every `check:` line and every citation of
  a moved file name the new path;
- every reader that lists `tests/` one level deep reaches the areas, found by
  searching for `tests/*.py`, `glob("test_*`, `iterdir`, `listdir` and
  `"tests"` joins.

A moved file owes no new case, no red run and no `seal mutate`. The one new
case is the area refusal in `tests/skills/test_test_layout.py`, seen red
once. The moved files are collected before and after the move, and the node
ids are compared as file name plus the rest of the id. The phase ends with
one `bin/test` command over the four areas and the modules that read what
changed, and with the tree's `bin/seal layout --check` and
`bin/seal rules --check` exiting 0. The first run answers whether pytest's
`prepend` mode keeps `from conftest import` working from a subdirectory.
Every path is joined from single segments.

## What this phase found

**`from conftest import` works from each area, and one import class the frame
missed does not.** The first collection after the `git mv` and before any
edit failed in 18 files. Every failure was a `FileNotFoundError` from a root
computed one level too shallow, and no file failed to import `conftest`. So
pytest's `prepend` mode puts `tests/` on `sys.path` for the subdirectories.

`frame/design.md` *Data & interfaces* says "the other helper imports keep
working from every subdirectory". That does not hold for a test file that
imports from another test file in a different directory. Twelve top-level
test files import from a moved file, for example
`tests/test_a_body_naming_two_issues_claims_one.py` from
`test_issue_claims_check`. Run alone, three of them failed collection with
`ModuleNotFoundError`:

- `tests/test_a_body_naming_two_issues_claims_one.py`;
- `tests/test_a_unit_is_bounded_where_a_parser_decides.py`;
- `tests/test_the_root_migrates_itself.py`.

pytest puts a test file's own directory on the path only as it imports that
file. In a full run these pass by order alone, because `evals`, `github`,
`hooks` and `skills` sort before `test_`. Phase 4's `behaviour/` sorts before
`evals`, so the same import would fail there in a full run.
`tests/conftest.py` now puts each directory under `tests/` that holds a test
file on `sys.path` as it loads. After that change the three files collect
alone. The imports between test files stay as they are.

**Readers that listed `tests/` one level deep (contract rule 12).** The
searches found these, and each now reaches the areas:

- `tests/test_one_word_one_meaning.py`, the file-name sweep at line 922,
  listed the top of `tests/`. It now walks the tree.
- `skills/verify/scripts/test_layout.py#_moved_main` resolved
  `from test_x import` against the modules directly under `tests/` only, in
  both trees. It now reads every module under `tests/` by its file name, and
  of two modules with one name it reads the one nearer `tests/`.
- `tests/skills/test_arm_check.py#selects_this_module` counted a pytest line
  as running this module only when it named the module or `tests`. It now
  counts any directory above the module, so `pytest tests/skills` counts.
- `tests/evals/test_seed_defects.py` copied every `CHECK_FILES` entry from
  the working tree. Phase 2 added `hooks/blocks.py` to `CHECK_FILES` for
  commits cut before the move, and the tree no longer holds that file. So 7
  cases of this file have failed since `dd01eb7e` (read: the loop and the
  constant at `51a616cd`; phase 2's narrow run did not include this module).
  The scaffold now skips an entry the tree does not hold.

These readers needed no change:

- `git ls-files tests/*.py` in `tests/test_a_shrunken_corpus_declines_to_judge.py`
  already matches the areas, because a git pathspec `*` crosses `/`. It
  listed the 28 files of `tests/hooks/` (executed).
- `.github/scripts/rules.py#markers`, `test_layout.py#_read_tests` and
  `tests/test_censuses.py:975` already walk the tree.
- `CITED_TREES`, `SCANNED` and `STAYS_HOME` name `tests` as a prefix.
- `ruff.toml`'s per-file ignore `"tests/*"` reaches the areas. With it,
  `uvx ruff check --select SIM115 tests/hooks/test_optin.py` passes, and with
  the ignores cleared it finds 2 errors (executed).

**How each moved file reaches the root.** A file that used `ROOT` as a string
imports it from `conftest`. Four files used it as a `pathlib.Path`:
`test_broad_gate.py`, `test_chain_check.py`, `test_mutation_check.py` and
`test_seal_stamp.py`. Each binds `ROOT = pathlib.Path(conftest.ROOT)`. A
`HOOKS` or script path that was built from `__file__` is joined under `ROOT`.
In `test_seal.py`, 11 local `root` assignments went the same way.
`test_issue_claims_check.py` had a relative root, and it now has the
absolute one.

Some `__file__` uses remain in the moved files, and none of them computes the
root:

- uses inside fixture source strings in `test_agentic_pytest_record.py`,
  `test_launch.py` and `test_settle.py`;
- a loaded module's own `__file__`, in `test_optin.py`,
  `test_unverified_check.py` and `test_issue_claims_check.py`.

Phase 4's case, "no file under `tests/` but `conftest.py` derives the root
from its own `__file__`", has to pass these.

**The edit hook removes an import that has no use yet.** The post-edit
formatter runs `ruff --fix`. An import added in one edit, before the edit
that uses it, was removed as unused in 12 files. Add the use first, or the
import and its use in one edit.

**Citations.** After the `git mv`, the census `vacated_paths` found 290 lines
in 117 files spelling a vacated `tests/test_<name>.py` (executed, over every
tracked file). Each was rewritten to the new path, and the census then found
none. No `<commit>:<path>` citation was rewritten: a search for
`<sha>:tests/<area>/` matches nothing. One join that the census cannot see
also moved, `("tests", "test_session_cost.py")` in
`tests/test_one_word_one_meaning.py#SEGMENT_SWEPT`.

**`CONTRIBUTING.md` *The test layout*** now says the file is
`tests/<area>/test_<stem>.py` and how the area is read. The rule that a test
file takes its root from `tests/conftest.py#ROOT` is not stated there yet.
Its case is phase 4's, and the sentence belongs with that case.

**The collection, before and after.** `bin/test <the 63 files> --collect-only -q`
collected 4584 node ids at `51a616cd` and 4589 after the build. Compared as
file name plus the rest of the id:

- 4580 ids are the same.
- 4 ids changed their text. Each is a parametrize row of
  `test_arm_check.py::test_a_job_counts_only_where_its_pytest_line_selects_this_module`
  whose parameter is a CI line that spells this module's own path. The path
  inside the parameter moved with the file.
- 5 ids are new, and each is a case this phase wrote (below).

A collection taken after the `git mv` and the root edits, before any new
case, gave the same 4584 ids as the base.

**New cases, each seen red before its reader changed:**

- `tests/skills/test_test_layout.py::Test_check::test_refuses_a_module_test_file_outside_its_area`,
  the one the plan names. Against the script before the change it failed
  with `assert [] == ['refused: tests/test_x.py: the file for hooks/x.py
  stands in tests/hooks/']`.
- `tests/skills/test_test_layout.py::Test_moved::test_accepts_a_pure_move[a-name-imported-from-a-test-file-in-an-area]`.
  Against the one-level reader it failed with
  `name V: its definition differs from the base's`.
- `tests/skills/test_arm_check.py`, three rows of
  `test_a_job_counts_only_where_its_pytest_line_selects_this_module`:
  `pytest tests/skills -q` (True), `pytest tests/hooks -q` (False) and
  `pytest tests/ --ignore=tests/skills -q` (False). The first failed against
  the old reader. The other two passed against it, and they pin the two
  directions of the new prefix rule.

Nine existing cases of `Test_check` and one of `Test_main` placed their
fixture file for `hooks/x.py` at `tests/test_x.py`. The area refusal refused
each one. Their fixture now stands at `tests/hooks/test_x.py`. The two
twin-report cases now expect the sorted file order of the new path.

**Existing cases relied on.** One `bin/test` command ran these 113 modules:

- the 63 files of `tests/hooks`, `tests/skills`, `tests/github` and
  `tests/evals`;
- the 48 top-level test files whose text this phase changed, which include
  `tests/test_censuses.py` and the twelve cross-area importers;
- `tests/test_conftest.py` and `tests/test_docs_line_wrap.py`.

It passed 5969 cases and skipped 16 (executed). The tree's
`bin/seal layout --check` exited 0 ("158 files read, 0 refused"), and
`bin/seal rules --check` exited 0 ("all 263 check lines in 63 rule files
hold").

**Which readers the narrow run took.** `git grep -l` for the paths this phase
changed finds 91 of the 93 top-level test files. Most of them read a document
whose citations changed, so running them all is the suite. This phase ran the
top-level files whose own text changed and the named readers. The other
top-level files are left to the orchestrator's broad run.
