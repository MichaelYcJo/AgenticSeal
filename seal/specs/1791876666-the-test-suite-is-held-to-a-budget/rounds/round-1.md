# 1791876666-the-test-suite-is-held-to-a-budget — review round 1

| Field | Value |
|---|---|
| Target SHA | 692cef316bf7cdd4b5d4ee31b8a1648fab412f49 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `9f9c9ed9261a709e321f3e163f00fbca6752956d..5ee4b39ef82f0b3f074eeb568b8d75542afd1e1d`, 9 commits |
| Contract changes | none |
| New units | NEVER_RAN (depth 1); unrun (depth 1); test_what_was_not_run_counts_only_the_changed_lines_mutants (depth 1); ELSEWHERE (depth 1); RUNS_ITS_RUNNER_DIRECTLY (depth 1); PLUGIN_SCRIPT (depth 1); ASSIGNED (depth 1); VARIABLE (depth 1); BARE_SCRIPT (depth 1); NEWER (depth 1); handed_first (depth 1); loaded_by (depth 1); before_any_floor (depth 1); newer_than (depth 1); ruff_targets (depth 1); matches (depth 1); test_what_runs_before_any_floor_needs_nothing_its_python3_lacks (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🔴 1 (`bin/test` refused below the floor before its runner can bootstrap), 🟡 2 (hook-run code unguarded after the census removal), 🟡 3 (a case that skips on ubuntu is misnamed and fails the job), 🟡 4 (the not-run count) |
| Loses a record or crashes | no |
<!-- New units: .github/workflows/test.yml, bin/test, bin/test.cmd, ruff.toml read by the diff-line heuristic and not by the AST -->

- [x] Pass

## What this round was asked

Round 1 of #929 at 692cef31 against origin/release/v0.22.0 (5b1f6fae), the item closed at phase 2: spec compliance and correctness, and anything still standing on a removed fact (the ledger, survivors, Kills:, unguarded-files.txt, the eight FLOOR copies, phases 3-6), text appended instead of rewritten, a second copy of a fact, a removal whose premise is false, a check bent around instead of fixed. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | `bin/test` runs its runner through the launcher, so a `python3` below 3.12 is refused before `run_tests.py` can build the 3.12+ virtualenv it exists to build; the sealer's `Broad gate` row runs `bin/test -q` | `bin/test:35`, `bin/test.cmd:14` | **fixed** `1df94b1d` | fixed at 1df94b1d; executed: base on 3.9.6 built `.venv` with uv and passed 13 (exit 0); tip through the launcher exit 2; tip direct exit 0 |
| 🟡 2 | The interpreter census was removed because the floor rose to 3.12, yet hooks and the modules they load run on the harness's `python3`; nothing now keeps `zip(strict=)` or `X.UTC` out of them, and ruff B905 and UP017 push toward both | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | **fixed** `2e3b2ef7` | fixed at 2e3b2ef7; read: `hooks/dispatch.py:602-604`, `hooks/review-history-guard.py:85`, `ruff.toml` selects B and UP; executed: the Stop hook on 3.9 now loads and draws with `seal_stamp.py`; the pattern finds no hook-run file today |
| 🟡 3 | A new case whose every id skips on ubuntu has no traced call, survives every mutant, and is named `kills nothing its file does not`; the job exits 1 for a reason that is false, contradicting spec.md:91 and test.yml:161 | `.github/scripts/case_check.py:861` | **fixed** `e96f533c` | fixed at e96f533c; executed: fixture with a `skipif(os.name != "nt")` case, `main` returned 1 with that sentence |
| 🟡 4 | A proof-loop kill is recorded for any mutant in a changed file, not on a changed line, so the `not run within the bound` count understates and can vanish | `.github/scripts/case_check.py:875` | **fixed** `a936870b` | fixed at a936870b; read: `path in diff` at :875 against `len(every_diff) - len(diff_killed)` at :936 |
| ⬜ 5 | Phase 2's record names a dangling commit, phases and a ledger fragment that no longer exist, 17 wrappers, and a `test-cases` row that was never built | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | answered | written before the rebase (ad83cfc0) and carried into the tree round 3 read: phase records cite resolving commits; executed: 25 of 29 cited SHAs are off-branch; read: `:57`, `:261`, `:328`, `:391`, `:442`; `phases/phase-1.md:154` |
| ⬜ 6 | The overview cites a removed ledger document and keeps open rows that CI run 38658107547 has answered | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | answered | written before the rebase (6ccc8f31) and carried into the tree round 3 read: the memo cites no removed document; read; the document is absent at the tip |
| ⬜ 7 | The mutant rule was prepended into the case-ceiling paragraph rather than given its own; ragged wrap | `CONTRIBUTING.md:146` | answered | written before the rebase (2b166b1e) and carried into the tree round 3 read: the case rule is its own paragraph; read |
| ❓ | Whether the tip's `windows-latest` and `macos-latest` legs pass | CI run 38658107547 | ❓ out of verified scope | pending when read; the orchestrator reads the run |

## Paste-ready fixes

```sh
# Not through hooks/launch.py, alone of bin/: below the floor run_tests.py
# builds a virtualenv at or above it, with uv or a newer interpreter it
# finds, and runs the suite there (#156). A refusal at entry would stop the
# one script whose job is to get past an old `python3`.
exec python3 "$script" "$@"
```
```bat
rem Not through hooks\launch.py, as bin/test says: below the floor
rem run_tests.py builds a virtualenv at or above it and runs the suite there.
where /q py
if errorlevel 1 goto usepython
py -3 "%script%" %*
exit /b %errorlevel%

:usepython
python "%script%" %*
exit /b %errorlevel%
```
```python
# `bin/test` hands `.github/scripts/run_tests.py` to the interpreter itself:
# below the floor that script builds a virtualenv at or above it and runs the
# suite there, which a refusal at entry would stop.
BOOTSTRAPS = {"test": '"$script"', "test.cmd": '"%script%"'}


def test_every_wrapper_runs_its_script_through_the_launcher():
    """Every file in `bin/`, found by listing it: each interpreter it starts
    is handed the launcher first, so a wrapper added later is held the day it
    is written. `bin/test` and its twin are the one exception, and they hand
    the runner over directly."""
    unheld = {}
    for entry in sorted(os.listdir(BIN)):
        text = read(os.path.join(BIN, entry))
        found = launches(text)
        if entry in BOOTSTRAPS:
            bypass = [line for line, arg in found if arg != BOOTSTRAPS[entry]]
            if not found or bypass:
                unheld[entry] = bypass or "starts no interpreter on its runner"
            continue
        if entry.endswith(".cmd"):
            first = '"%launch%"'
            defined = 'set "launch=%here%..\\hooks\\launch.py"' in text
        else:
            first, defined = '"$here/../hooks/launch.py"', True
        bypass = [line for line, arg in found if arg != first]
        if not found or bypass or not defined:
            unheld[entry] = bypass or "starts no interpreter through the launcher"
    assert not unheld, unheld
```
```markdown
**Python 3.12 is the supported floor**, held as `FLOOR` in `hooks/launch.py`
so this sentence and the code state one number. Every `bin/` wrapper but
`bin/test` runs its script through that launcher, which refuses an older
interpreter with one sentence before the script is read. `bin/test` runs on
whatever `python3` it finds, because its runner builds the virtualenv: with an
interpreter at that floor or newer, refusing a `.venv` it finds below it, and
where it finds neither `uv` nor such an interpreter it says which to install.
```
```python
Every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script
through this file (`bin/test`'s runner builds its own virtualenv at the floor):
```
```python
# The supported floor, read from `hooks/launch.py`, its one source. The
# virtualenv is built and adopted against it. `bin/test` runs this file on
# whatever `python3` it finds, since below the floor this file is what builds
# an environment above it. Loaded by path, because `hooks/` is not on this
# file's `sys.path`.
```
```python
# --- what runs with no launcher in front of it ----------------------------------

# A hook runs under whatever `python3` the harness finds, 3.9 on a stock macOS
# (`hooks/dispatch.py#main`), and so does every module a hook loads in its
# own process. ruff lints them at py312, where B905 asks every `zip` for
# `strict=` (3.10) and UP017 spells `timezone.utc` as `datetime.UTC` (3.11):
# the two constructs that have reached this tree before.
UNLAUNCHED_ABOVE_39 = re.compile(r"zip\(.*strict=|\b\w+\.UTC\b")
LOADED_BY_A_HOOK = (
    "skills/verify/scripts/seal_stamp.py",  # hooks/sealer-stamp.py#load_stamp
    "skills/verify/scripts/unverified_check.py",  # hooks/review-history-guard.py#reader
)


def test_what_a_hook_runs_needs_no_construct_newer_than_a_stock_python3():
    """The launcher holds the floor for `bin/`. Nothing holds it for a hook,
    which runs on the harness's `python3` and fails open when it dies."""
    listed, _missing = on_disk(ROOT, git_listing(ROOT, "ls-files", "hooks/*.py"))
    found = sorted(
        rel
        for rel in [*listed, *LOADED_BY_A_HOOK]
        if UNLAUNCHED_ABOVE_39.search(read(os.path.join(ROOT, rel)))
    )
    assert not found, (
        f"{found} run under the harness's own `python3`, 3.9 on a stock "
        "macOS, and use a construct that needs 3.10 or 3.11"
    )
```
```python
    No `zip`. `hooks/review-history-guard.py` loads this module under the
    harness's own `python3`, 3.9 on a stock macOS, and ruff's B905 would ask
    a `zip` here for the keyword 3.10 added.
    `tests/test_a_script_says_which_interpreter_it_needs.py` keeps it out.
```
```python
NEVER_RAN = (
    "not proved: none of its ids ran its call on this runner, skipped or "
    "deselected, so no mutant can fail it here"
)
```
```python
        never_ran = [n for n in names if not own_ids(hits, file, functions, n)]
        findings += [(f"{file}::{n}", NEVER_RAN) for n in never_ran]
        names = [n for n in names if n not in never_ran]
        if not names:
            continue
```
```text
It runs on ubuntu alone: a case none of whose ids runs its call there, as a
Windows-only case, is named `not proved`, and its work item's mutation table
is where it is proved.
```
```python
ELSEWHERE = (
    '\nimport pytest\n\n\n@pytest.mark.skip(reason="another platform")\n'
    "def test_double_elsewhere():\n    assert m.double(2) == 4\n"
)
```
```python
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, ELSEWHERE)},
            {},
            1,
            [
                "tests/test_m.py::test_double_elsewhere: not proved: none of "
                "its ids ran its call on this runner"
            ],
            id="a case that ran nowhere here is named for that",
        ),
```
```python
def unrun(every_diff, diff_killed):
    """How many of the changed shipped lines' mutants no run gave a verdict.
    A proof's kill on an unchanged line of a changed file is not one of them.

    Reads: nothing — compares the labels it is handed
    """
    return sum(1 for label, *_rest in every_diff if label not in diff_killed)
```
```python
    if unrun(every_diff, diff_killed):
        lines.append(NOT_RUN.format(count=unrun(every_diff, diff_killed)))
```
```python
def test_what_was_not_run_counts_only_the_changed_lines_mutants():
    """A proof that killed a mutant of an unchanged line in a changed file
    does not make a changed line's mutant count as run."""
    module = case_check()
    every_diff = [("m.py:6 `return` made `return None`", "m.py", "a", "b")]
    killed_in_a_proof = {"m.py:2 `return` made `return None`": True}
    assert module.unrun(every_diff, killed_in_a_proof) == 1
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_script_says_which_interpreter_it_needs.py tests/test_a_new_case_protects_what_its_file_did_not.py -q`, clone at 692cef31 | exit 0, 24 passed |
| `python3 .github/scripts/budget_check.py`, clone at 692cef31 | exit 0; `suite-seconds` 6,031 against 7,841; `slow-file` rows 915 against 1,190 and 389 against 506; `enforced-unresolved` 0 |
| `.test_durations` keys at 5b1f6fae against 692cef31, and `--collect-only` of the five modules that lost ids | 227 removed, 0 added, 0 repriced; none of the 227 is collected; the 7 collected ids without a price are this branch's new cases |
| each of 14 `bin/` wrappers with `--help`, launched and direct, on python 3.15 | identical output and exit 0 for every one |
| `/usr/bin/python3` (3.9.6) `hooks/launch.py skills/code-review/scripts/round_record.py --help` | exit 2, the refusal sentence |
| base 5b1f6fae, fresh clone: `/usr/bin/python3 .github/scripts/run_tests.py tests/test_arm_check.py -q -p no:xdist -k command` | exit 0; built `.venv` with uv on CPython 3.13.9; 13 passed |
| tip: the same through `hooks/launch.py` | exit 2, `run-tests: needs python 3.12 or newer` |
| tip: `run_tests.py` direct on 3.9.6 | exit 0, 13 passed |
| probe `test_tmp_stamp39.py` (NAME NOT IN TREE: deleted after the run): `dispatch.py stop` on 3.9.6 over one values file, tip and base | tip printed the stamp and left the file `.drawn.json`; base printed nothing and left it pending |
| the removed census pattern over shipped `.py`, tip and base | tip: `case_check.py`, `gather_changelog.py`, `round_record.py`, `seal.py`, `session_cost.py`; nothing under `hooks/`, nor `seal_stamp.py` or `unverified_check.py` |
| probe `test_tmp_skip.py` (NAME NOT IN TREE: deleted after the run): `case_check.main` on a fixture with a new `skipif(os.name != "nt")` case | exit 1, named `kills nothing its file does not` |
| probe `test_tmp_shas.py` (NAME NOT IN TREE: deleted after the run): 8-hex SHAs cited in the work item against `merge-base --is-ancestor` | 25 of 29 are not ancestors of the tip |
| `gh api …/jobs/116172593664/logs`, the `cases` job at 692cef31 (CI's execution, read here) | 19 proved, 0 named, 299 s; 39 survived; 542 not run within the bound |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A row added to an existing parametrized function is not proved on its own, so growth by rows passes the `cases` job; this branch's own end-to-end cases were merged into rows to pass it (853f2f28) | #942, already deferred by `spec.md` §Scope (the `test-cases` rows and their ceilings) | #942's framer, with the repository owner |
