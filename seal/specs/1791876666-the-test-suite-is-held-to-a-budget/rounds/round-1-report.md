# 1791876666-the-test-suite-is-held-to-a-budget — round 1 report

Reviewed by warden at `692cef31` against `origin/release/v0.22.0` at
`5b1f6fae`, in a `git clone --no-local` of the branch under the session's
scratchpad. No earlier round exists, so nothing is carried.

## How the findings relate

Two of the four findings needing a fix come from one decision: the launcher
was put in front of every `bin/` command, and the old census was removed on
the grounds that the floor is now held. Neither holds for the code that has
to run on an older `python3`. That code is `bin/test`'s runner, whose job is
to bootstrap, and the hooks, which no launcher stands in front of.

- 🔴 1, the bootstrapper. `bin/test` used to work on a stock macOS
  `python3` (3.9). Now the launcher refuses there, before its runner can build
  the 3.12+ virtualenv it was written to build.
- 🟡 2, the hooks. The census that kept 3.10/3.11 constructs out of
  hook-run code was removed because "the floor rose to 3.12". Hooks still
  run on the harness's `python3`, and this branch added one more module to
  that path.
- 🟡 3 and 🟡 4 are unrelated defects in the new regrowth check.
- ⬜ 5–7 are paperwork and prose that still stand on removed facts. They do
  not count toward `Needs a fix`.

What the implementer's account asserted, and what was found:

- *"At or above it the script runs as if run directly"* (spec §Scope item
  4). This holds: 14 wrappers gave the same `--help` output and exit
  launched and direct (`executed`).
- *"`bin/test` builds its virtualenv with an interpreter at that floor or
  newer … where it finds neither `uv` nor such an interpreter it says which
  to install"* (`CONTRIBUTING.md:120`). This no longer holds on a 3.9
  `python3`: the launcher answers first (🔴 1).
- *"the floor rose to 3.12 and both constructs it matched predate it"*
  (`phases/phase-2.md:79-83`, commit 7b7e0b60). The premise is false for
  hooks (🟡 2).
- *"Platform honesty: a case guarding a Windows-only sentence proves itself
  on a run that skips there"* (`spec.md:91`, `test.yml:161`). The run says
  otherwise: such a case is named and the job fails (🟡 3).
- The budget rows, the `.test_durations` cut and the `Enforced by:` move all
  check out (`executed`, see the probes).

## 🔴 1 — `bin/test` now refuses where it used to build its own virtualenv

`bin/test:35` and `bin/test.cmd:14-22` now hand `run_tests.py` to
`hooks/launch.py`. The launcher refuses any interpreter below 3.12. But
`run_tests.py` is the one script in `bin/` that was written to run on an old
interpreter. On a stock macOS `python3` it finds `uv` or a newer Python,
builds `.venv` at 3.12 or above, and runs the suite there.
`tests/test_the_suite_has_a_command_that_is_cheap_twice.py#test_neither_tool_available_names_what_to_install`
and its neighbours pin that design against macOS's 3.9.

Executed, on a machine whose `/usr/bin/python3` is 3.9.6 and with `uv`
installed:

- **Base, `5b1f6fae`.** `/usr/bin/python3 .github/scripts/run_tests.py
  tests/test_arm_check.py -q -p no:xdist -k command`, in a clone with no
  `.venv`, gave exit 0. It printed `bin/test: building …/.venv`, built the
  environment with uv on CPython 3.13.9, and ran 13 passed.
- **Tip, through the launcher as `bin/test` now runs it.** Exit 2 with
  `run-tests: needs python 3.12 or newer, and this is python 3.9.6 …`.
- **Tip, `run_tests.py` run directly on 3.9.** Exit 0, 13 passed. So the
  launcher is the only thing that stops it.

Why it matters:

- A contributor on stock macOS who types `bin/test` is refused, though they
  have everything the runner needs.
- This repository's own `Broad gate` row in `seal/config.md` is
  `… && bin/test -q`. So the sealer's one broad run fails the same way on
  such a machine.
- The runner's no-tool sentences are now unreachable in practice on 3.9.
  Only the in-process cases with a fake `sys` still reach them.
- The refusal also names `run-tests`, a command nobody typed. The launcher's
  docstring promises the command "the way its wrapper spells it", and here
  the wrapper is `test`.

The fix is to leave `bin/test` outside the launcher, exempt it by name in
`test_every_wrapper_runs_its_script_through_the_launcher` with its reason,
and say so in `CONTRIBUTING.md` and in the launcher's docstring. The floor is
still held for `bin/test`: `run_tests.py` builds and adopts only a `.venv` at
or above `FLOOR`, which it reads from the launcher.

## 🟡 2 — The census was removed because the floor rose, but hooks still run on the harness's `python3`

The removed census (NAME NOT IN TREE: `ABOVE_THE_FLOOR`, `test_no_shipped_script_needs_more_than_the_floor_without_saying_so`)
scanned every shipped `.py` for `zip(…, strict=)` (3.10) and `X.UTC`
(3.11). It covered `hooks/`. Commit 7b7e0b60 and `phases/phase-2.md:79-83`
removed it because "the floor rose to 3.12". The floor binds only what
goes through the launcher, and hooks deliberately do not:

- `hooks/dispatch.py#main` (lines 602-604) avoids a strict `zip` because "a
  hook runs under whatever `python3` the harness finds, 3.9 on a stock
  macOS". Phase 2 measured that "on 3.9 the gates decide today"
  (`phases/phase-2.md:407-411`).
- `hooks/review-history-guard.py#reader` loads
  `skills/verify/scripts/unverified_check.py` in its own process. This
  branch deleted the paragraph in
  `skills/verify/scripts/unverified_check.py#live_lines` that warned against
  exactly this: "No `zip`. Ruff's B905 requires the strictness keyword …
  this script carries no interpreter guard".
- `hooks/sealer-stamp.py#load_stamp` loads `seal_stamp.py`. With its guard
  gone, it now runs on 3.9. Executed: under `/usr/bin/python3`, the Stop hook
  at the tip drew the stamp and renamed the values file, where the base drew
  nothing.

`ruff.toml` selects `B` and `UP` at `py312`. So the lint job pushes toward
the very constructs that break here. B905 asks every `zip` for `strict=`, and
UP017 rewrites `timezone.utc` as `datetime.UTC`.

A concrete failure: a contributor adds a `zip` to a hook or to
`seal_stamp.py`'s drawing path, and lint makes them add `strict=True`. Every
check stays green. On a stock macOS the hook then raises `TypeError`, and a
gate fails open. For the Stop hook, `drawings` claims the file before
`fitted` runs, so the drawing is lost.

Executed: the census pattern over the tip finds no file under `hooks/`, and
neither `seal_stamp.py` nor `unverified_check.py`. So a narrowed census
passes today and costs nothing.

## 🟡 3 — A new case that skips on ubuntu is named for killing nothing new, and fails the job

`.github/scripts/case_check.py:849` reads the case's own ids from the traced
run. A function whose every id skips on the runner has no traced call, so
`mine` is empty. Every mutant then takes `code = SURVIVED` at line 861, the
draw runs out, and the function is named `KILLS_NOTHING_NEW`. The job exits 1.

Executed with a probe: a fixture repository changes `m.py`'s `double` and
adds `test_double_on_windows` under `skipif(os.name != "nt")` (NAME NOT IN TREE: a fixture's case).
`case_check.main` returned 1 and named that case (NAME NOT IN TREE: `tests/test_m.py::test_double_on_windows`)
with `kills nothing its file does not: … each it killed was killed by another
case too, or none was`.

The sentence is false: no sibling killed anything, and the case never ran.
`spec.md:91`, the job's comment at `.github/workflows/test.yml:161` and the
module docstring at `case_check.py:76-77` say such a case "proves itself on
a run that skips there". This repository fixes Windows-only defects often,
and the job would turn red on the regression case each of them needs, with a
wrong reason.

The fix below names the function truthfully and keeps it a finding, so the
gate gets no weaker. **Left to the owner** is whether such a case should
instead be a report line. That would let a Windows-only case land, at the
price of `skipif(True)` becoming a way around the gate.

## 🟡 4 — "Not run within the bound" counts mutants of unchanged lines

`case_check.py:875` records a proof-loop kill in `diff_killed` whenever the
mutant's **file** is in the diff (`path in diff`), not its line. Line
936-937 then prints `len(every_diff) - len(diff_killed)` as the number of
changed-line mutants not run. This was found by reading.

The scenario: a pull request changes two lines of `hooks/gate.py`, and a new
case proves itself on mutants of unchanged `gate.py` lines. Each such kill
adds a label that `every_diff` does not hold. When the bound ends before the
report half runs, the count shrinks, or drops to zero or below and the line
disappears. The summary then reads as if every mutant of the changed lines
ran, and no survivor is listed for the ones that never ran.

On this PR every mutated shipped file is new, so the count of 542 is
unaffected.

## ⬜ 5 — Phase 2's record still describes the branch before the rebase and the closure

All of this is paperwork under `seal/specs/`. It is reported as a
correction and is not counted in `Needs a fix`.

- **Dangling and stale commits.** `phases/phase-2.md:6` names `Commit
  652bf297`, which is not an object in the clone. `plan.md:54` closes phase 2
  at `d23a8d2e`, which is mid-phase. Of the 29 short SHAs the work item
  cites, 25 are not ancestors of the tip (`executed`).
- **Superseded statements.** `phases/phase-2.md:57-58` says "#930's
  `seal/budgets.md` is not on this branch … Phase 3 is not started".
  `:328-337` says "Phases 3 to 6 in `plan.md` still name `Kills:` lines".
  `:339` and `:374` carry work "to phase 5", which is now #942's.
- **The ledger.** `:150-155`, `:375` and `:442-462` describe `Corrected ·`
  and `Re-read ·` rows "in the fragment". The fragment was removed in
  0df57c34, and the section says the rebase onto #944 is still to come.
  `phases/phase-1.md:154-162` does the same.
- **Counts and claims.** `:90` ("six of seventeen commands") and `:391`
  ("all 17 `bin/` wrappers") disagree with the 15 wrappers the tree holds and
  the changelog fragment states. `:384` says "every wrapper and hook reaches
  it". `:261` says "Growth by rows is held by #930's `test-cases` budget row",
  and no such row exists: spec §Scope gives the rows to #942. 692cef31 fixed
  the same claim in `case_check.py` only.

## ⬜ 6 — The overview cites a removed document and open rows that CI has since answered

- `overview.md:7` cites `docs/the-evidence-ledger.md` §*A released row is
  read again in the branch's fragment*, which is gone at the tip.
- Its *Not verified* rows ask for the next `cases` and `windows-latest` runs.
  At the tip, run 38658107547's `cases` job proved 19 and named 0 (read from
  its log). The Windows legs were still pending when read.

## ⬜ 7 — The mutant rule was prepended into the time-budget paragraph

`CONTRIBUTING.md:146-162`: the new sentences about what a case owes were
placed in front of the paragraph that sets the 90-second case ceiling. They
sit under its lead sentence, *A case has a budget, and so does each leg*, and
the paragraph now makes two points. The wrap is ragged at `:155-157` and at
`:162`. The behaviour and the facts are right. Splitting the mutant rule into
a paragraph of its own, led by its own sentence, is the rewrite in place that
spec.md:12 asked for.

## Regression tests to plant

- `tests/test_a_script_says_which_interpreter_it_needs.py`: the `bin/test`
  case and the narrowed census case in the fixes below (🔴 1, 🟡 2).
- `tests/test_a_new_case_protects_what_its_file_did_not.py`: a row of
  `test_each_real_path_end_to_end` for a case that ran nowhere here (🟡 3),
  and a direct case for the unrun count (🟡 4).

Each owes its red run before it is committed (contract §15). For 🟡 2,
plant a `zip(a, b, strict=True)` in a hook's copy. For 🔴 1, put the
launcher back in `bin/test`.

## Facts for the evidence ledger

None. #944 removed the ledger, and this repository has nowhere to feed them.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | `bin/test` runs its runner through the launcher, so a `python3` below 3.12 is refused before `run_tests.py` can build the 3.12+ virtualenv it exists to build; the sealer's `Broad gate` row runs `bin/test -q` | `bin/test:35`, `bin/test.cmd:14` | open | executed: base on 3.9.6 built `.venv` with uv and passed 13 (exit 0); tip through the launcher exit 2; tip direct exit 0 |
| 🟡 2 | The interpreter census was removed because the floor rose to 3.12, yet hooks and the modules they load run on the harness's `python3`; nothing now keeps `zip(strict=)` or `X.UTC` out of them, and ruff B905 and UP017 push toward both | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | open | read: `hooks/dispatch.py:602-604`, `hooks/review-history-guard.py:85`, `ruff.toml` selects B and UP; executed: the Stop hook on 3.9 now loads and draws with `seal_stamp.py`; the pattern finds no hook-run file today |
| 🟡 3 | A new case whose every id skips on ubuntu has no traced call, survives every mutant, and is named `kills nothing its file does not`; the job exits 1 for a reason that is false, contradicting spec.md:91 and test.yml:161 | `.github/scripts/case_check.py:861` | open | executed: fixture with a `skipif(os.name != "nt")` case, `main` returned 1 with that sentence |
| 🟡 4 | A proof-loop kill is recorded for any mutant in a changed file, not on a changed line, so the `not run within the bound` count understates and can vanish | `.github/scripts/case_check.py:875` | open | read: `path in diff` at :875 against `len(every_diff) - len(diff_killed)` at :936 |
| ⬜ 5 | Phase 2's record names a dangling commit, phases and a ledger fragment that no longer exist, 17 wrappers, and a `test-cases` row that was never built | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | open | executed: 25 of 29 cited SHAs are off-branch; read: `:57`, `:261`, `:328`, `:391`, `:442`; `phases/phase-1.md:154` |
| ⬜ 6 | The overview cites a removed ledger document and keeps open rows that CI run 38658107547 has answered | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | open | read; the document is absent at the tip |
| ⬜ 7 | The mutant rule was prepended into the case-ceiling paragraph rather than given its own; ragged wrap | `CONTRIBUTING.md:146` | open | read |
| ❓ | Whether the tip's `windows-latest` and `macos-latest` legs pass | CI run 38658107547 | ❓ out of verified scope | pending when read; the orchestrator reads the run |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A row added to an existing parametrized function is not proved on its own, so growth by rows passes the `cases` job; this branch's own end-to-end cases were merged into rows to pass it (853f2f28) | #942, already deferred by `spec.md` §Scope (the `test-cases` rows and their ceilings) | #942's framer, with the repository owner |

## Paste-ready fixes

### 🔴 1 — `bin/test` reaches its runner on any `python3`

`bin/test`, last line:

```sh
# Not through hooks/launch.py, alone of bin/: below the floor run_tests.py
# builds a virtualenv at or above it, with uv or a newer interpreter it
# finds, and runs the suite there (#156). A refusal at entry would stop the
# one script whose job is to get past an old `python3`.
exec python3 "$script" "$@"
```

`bin/test.cmd`, from the line after the missing-runner block to the end:

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

`tests/test_a_script_says_which_interpreter_it_needs.py`, replacing the
wrapper case:

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

`CONTRIBUTING.md:117-122`:

```markdown
**Python 3.12 is the supported floor**, held as `FLOOR` in `hooks/launch.py`
so this sentence and the code state one number. Every `bin/` wrapper but
`bin/test` runs its script through that launcher, which refuses an older
interpreter with one sentence before the script is read. `bin/test` runs on
whatever `python3` it finds, because its runner builds the virtualenv: with an
interpreter at that floor or newer, refusing a `.venv` it finds below it, and
where it finds neither `uv` nor such an interpreter it says which to install.
```

`hooks/launch.py:4`:

```python
Every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script
through this file (`bin/test`'s runner builds its own virtualenv at the floor):
```

`.github/scripts/run_tests.py:85-88`:

```python
# The supported floor, read from `hooks/launch.py`, its one source. The
# virtualenv is built and adopted against it. `bin/test` runs this file on
# whatever `python3` it finds, since below the floor this file is what builds
# an environment above it. Loaded by path, because `hooks/` is not on this
# file's `sys.path`.
```

The changelog fragment's *All fifteen wrappers* sentence needs the same
exception.

### 🟡 2 — a census for what runs with no launcher in front of it

`tests/test_a_script_says_which_interpreter_it_needs.py`, after
`test_the_floor_has_one_source`:

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

`skills/verify/scripts/unverified_check.py#live_lines`, the paragraph
restored in its docstring:

```python
    No `zip`. `hooks/review-history-guard.py` loads this module under the
    harness's own `python3`, 3.9 on a stock macOS, and ruff's B905 would ask
    a `zip` here for the keyword 3.10 added.
    `tests/test_a_script_says_which_interpreter_it_needs.py` keeps it out.
```

### 🟡 3 — a case that ran nowhere here is named for that

`.github/scripts/case_check.py`, beside `KILLS_NOTHING_NEW`:

```python
NEVER_RAN = (
    "not proved: none of its ids ran its call on this runner, skipped or "
    "deselected, so no mutant can fail it here"
)
```

In `check`, before `units = named_units(...)`:

```python
        never_ran = [n for n in names if not own_ids(hits, file, functions, n)]
        findings += [(f"{file}::{n}", NEVER_RAN) for n in never_ran]
        names = [n for n in names if n not in never_ran]
        if not names:
            continue
```

The docstring's lines 76-77, `test.yml:161` and `spec.md:91`:

```text
It runs on ubuntu alone: a case none of whose ids runs its call there, as a
Windows-only case, is named `not proved`, and its work item's mutation table
is where it is proved.
```

`tests/test_a_new_case_protects_what_its_file_did_not.py`, a row of
`test_each_real_path_end_to_end` and the text it uses:

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

### 🟡 4 — count the changed lines' mutants, not the labels

`.github/scripts/case_check.py`, a unit beside `selected`:

```python
def unrun(every_diff, diff_killed):
    """How many of the changed shipped lines' mutants no run gave a verdict.
    A proof's kill on an unchanged line of a changed file is not one of them.

    Reads: nothing — compares the labels it is handed
    """
    return sum(1 for label, *_rest in every_diff if label not in diff_killed)
```

In `check`, replacing lines 936-937:

```python
    if unrun(every_diff, diff_killed):
        lines.append(NOT_RUN.format(count=unrun(every_diff, diff_killed)))
```

`tests/test_a_new_case_protects_what_its_file_did_not.py`:

```python
def test_what_was_not_run_counts_only_the_changed_lines_mutants():
    """A proof that killed a mutant of an unchanged line in a changed file
    does not make a changed line's mutant count as run."""
    module = case_check()
    every_diff = [("m.py:6 `return` made `return None`", "m.py", "a", "b")]
    killed_in_a_proof = {"m.py:2 `return` made `return None`": True}
    assert module.unrun(every_diff, killed_in_a_proof) == 1
```

Needs a fix: yes — 🔴 1 (`bin/test` refused below the floor before its runner can bootstrap), 🟡 2 (hook-run code unguarded after the census removal), 🟡 3 (a case that skips on ubuntu is misnamed and fails the job), 🟡 4 (the not-run count)
Loses a record or crashes: no

## Proof block

Opened in this round: `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/{spec.md,plan.md,questions.md,overview.md,changelog.md,phases/phase-2.md}`,
`hooks/launch.py`, `hooks/sealer-stamp.py`, `hooks/dispatch.py` (the `main`
region), `hooks/review-history-guard.py` (the `reader` region),
`.github/scripts/case_check.py`, `.github/scripts/run_tests.py` (head and
floor), `.github/workflows/test.yml` (the `cases` job), `bin/test`,
`bin/test.cmd`, every `bin/` wrapper's diff, `CONTRIBUTING.md` (lines
114-185), `ruff.toml` (selection), `seal/budgets.md` (diff),
`docs/round-record-spec.md` (diff), `docs/the-broad-gate.md` (diff),
`agents/sealer.md` (diff), `skills/code-review/orchestration.md` (diff),
the diffs of `round_record.py`, `settle.py`, `fold_check.py`,
`broad_gate.py`, `payload_meter.py`, `seal_stamp.py`, `mutation_check.py`
(and its `run_cases`), `arm_check.py`, `unverified_check.py`,
`claude_block.py`, `tests/undeclared_readers.txt`,
`tests/test_a_script_says_which_interpreter_it_needs.py` (tip, and the base's
case list and removed census), `tests/test_a_new_case_protects_what_its_file_did_not.py`,
the diffs of `tests/test_the_commit_gate_decides_at_the_commit.py` and five
smaller test modules, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`
(lines 425-490), `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
(fixtures), `skills/verify/scripts/seal_stamp.py` (lines 700-830).
