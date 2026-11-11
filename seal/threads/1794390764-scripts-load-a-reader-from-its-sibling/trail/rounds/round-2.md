# Review round 2: 1794390764-scripts-load-a-reader-from-its-sibling

```seal
target: afc05486a, fixes 707107377..afc05486a
```

This is a verifying round. The range `707107377..afc05486a` holds the
`pr.md` fix `af7b9370a`, fix pass 1 (`82b1693a0`, `703882aae`,
`e2d4013f0`, `4b2cabc58`, `427fbd2d5`), the close blocks `d30dd28d1` and
the framer's fold `afc05486a`. The code read is that range's diff. The
work item's present-state records (`routing.md`, `frame/design.md`,
`frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`,
`pr.md`) were read whole at `afc05486a`. `Commit and pull request
language` is English, so no `pr.<lang>.md` is owed. The probes and narrow
runs ran in a `git clone --no-local` of the branch at `afc05486a`, under
this round's scratch directory.

Carried from round 1 and not established again: that the four lazy
readers of `chain_check.py` (`:1177`, `:1420`, `:1648`, `:1815`) end the
check at exit 2 in their own result; G10 and phase 2's S6 rows for the
unguarded scripts; S1's count and S8's comparison; and the phase records,
which no commit in the range changed. The framer's fold cites the first
of these as round 1's and as not traced by the framer.

## Findings

### 1. `release_seal.py#main` catches the loader's exit around loads and exits 0, and its warning reads `Absent: 2`

```seal
severity: should
location: `.github/scripts/release_seal.py:602-612`, `.github/scripts/release_seal.py:39-44`, `tests/github/test_release_seal.py:721`, `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/frame/design.md:94-115`, `seal/threads/1794390764-scripts-load-a-reader-from-its-sibling/changelog.md:3`
evidence: executed `python3 test_tmp_main_absent.py <clone>` (`release_seal.main` with `sibling.ROOT` at an empty directory and `DRY_RUN=1`), and `git grep -nE 'except[^:]*(SystemExit|BaseException)|except *:' -- '*.py' ':!tests' ':!evals/behaviour'`; read `.github/scripts/release_seal.py:290-331`, `:412-424`, `:514-539`, `:596-612`, `lib/sibling.py:18-24`, `git show 3285f1a04:.github/scripts/release_seal.py` `_module` and `main`
reopens: round-1#1
```

Why it matters: round 1's close of finding 1 says that "the other catches
of `SystemExit` outside `tests/` end the run at exit 2 or catch no load".
That is false of `release_seal.py#main`. Its `except (Exception,
SystemExit)` at `:604` stands around `seal_release`, which loads
`publisher()` at `:518`, `gate()` through `suite_counts`, and
`lib/optin.py` and `lib/config.py` through `mark_on` at `:423-424`. None of
these loads is inside `going_on`, and `main` returns 0. The two sites the
fix named hold, and the class it claimed to list is not whole. A search
for every handler that can catch `SystemExit` (named, `BaseException`, or
a bare `except`) lists thirteen sites outside `tests/`. The others catch no
load, re-raise, or are the lazy readers carried above. A handler that names
a tuple held in a variable would escape that search, so the list is whole
for the spellings Python offers in an `except` clause and a sample beyond.

The probe ran `main` with every module absent. It returned 0, and stderr
held the loader's sentence about `publish_release_note.py`, ending
"Nothing was read." Stdout held two lines:

- `no seal: Absent: 2 -- the note stays as it was published`
- `::warning::release seal skipped: Absent: 2`

So three things a person reads are wrong or empty:

- The `::warning::` line is the one GitHub raises to the run's summary. It
  names no file, and its "2" reads as a count. At the base the same failure
  was `FileNotFoundError: [Errno 2] No such file or directory: '<path>'`
  (read: the base's `_module` executed a spec built on the absent path), so
  the warning named the file. Phase 2 lost the path (`SystemExit: 2` at
  `707107377`), and the fix pass renamed it to `Absent: 2`.
- `lib/sibling.py`'s docstring ties the sentence to its exit: "exit 2 says
  nothing was read (#590)". `main` exits 0. Where the absent file is
  `lib/config.py`, `seal_release` has already printed the panel's rows at
  `:538-539` when `mark_on` reaches the load, so "Nothing was read." follows
  rows that were read.
- The module docstring at `:43-44` says "Every failure here is one log line
  and one `::warning::` with an exit of 0". An absent module is now two
  log lines and a warning that names nothing.

The fold put `main` among the sites that "load outside `going_on`, so the
sentence is written and the run then ends", and the framer asked this
round to weigh it. `main`'s contract is the one `going_on` was made for:
the job exits 0 whatever fails, and its own line says what went wrong.
So `main` loads inside the block and names `Absent.path` in its line, as
`chain_counts` does:

```python
def main():
    tag = os.environ.get("TAG", "").strip()
    repo = os.environ.get("REPO", "").strip()
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN -- nothing will be uploaded or edited")
    try:
        import sibling

        # The job exits 0 whatever fails, and the loader's "Nothing was
        # read." pairs with exit 2, so an absent module raises
        # `lib/sibling.py#Absent` with no sentence and the line below names it.
        with sibling.going_on():
            seal_release(tag, repo, dry)
    except (Exception, SystemExit) as problem:
        if isinstance(problem, Refused):
            reason = str(problem)
        # `Absent`'s path; an `ImportError` carries a `path` of its own.
        elif isinstance(problem, SystemExit) and getattr(problem, "path", None):
            reason = f"{problem.path} is absent"
        else:
            reason = f"{type(problem).__name__}: {problem}"
        reason = " ".join(reason.split())
        print(f"no seal: {reason} -- the note stays as it was published")
        print(f"::warning::release seal skipped: {reason}")
    return 0
```

```python
# tests/github/test_release_seal.py, in Test_main
    def test_names_an_absent_module_in_its_own_line_and_exits_0(
        self, monkeypatch, tmp_path, capsys
    ):
        """#1482. The seal exits 0 whatever fails, so an absent module is
        named in the `no seal` line and the warning, and the loader's
        sentence, whose "Nothing was read." pairs with exit 2, is kept back
        (round 2, finding 1)."""
        mod = seal()
        import sibling

        plugin = tmp_path / "no-plugin"
        monkeypatch.setattr(sibling, "ROOT", str(plugin))
        monkeypatch.setenv("TAG", "v0.0.1")
        monkeypatch.setenv("REPO", "o/r")
        assert mod.main() == 0
        said = capsys.readouterr()
        assert said.err == ""
        absent = plugin / ".github" / "scripts" / "publish_release_note.py"
        assert f"::warning::release seal skipped: {absent} is absent" in said.out
```

The case is seen red against `main` at `afc05486a`, where stderr holds the
sentence and the warning reads `Absent: 2`. The `import sibling` inside the
`try` has no OS precondition: an absent `lib/sibling.py` is a
`ModuleNotFoundError`, which the same `except` names at exit 0.

The snippets do not reach every statement of the old fact, and the fix
pass owes the rest, through the framer for the frame:

- `frame/design.md` *Scope* item 4: "There are two" becomes three, and
  `release_seal.py#main` leaves the sites that load outside `going_on`.
- S7, and the *Removes* row "for the two callers that go on".
- `changelog.md:3`: "Where `seal gate` or the release seal goes on without
  a module, as each does for the round records' counts". The release seal
  then names any absent module in its own line.
- The docstring paragraph at `release_seal.py:39-44` becomes true again,
  and needs no edit.

```seal
verdict: fixed 5532345fb
answer: The finding holds, and round 1 finding 1's close answer was wrong to say every other catch ends at exit 2 or catches no load. `release_seal.py#main` now runs `seal_release` inside `sibling.going_on()` and imports `sibling` inside its `try`; its `no seal` line and `::warning::` name the file as `<path> is absent`, the job still ends at exit 0, and no "Nothing was read." is written. `Test_main::test_names_an_absent_module_in_its_own_line_and_exits_0` failed before the fix, and mutants removing the block or the path from the warning turned it red. `changelog.md:3` is corrected in the same commit; the module docstring holds again unchanged. The design states `main` as the third caller that goes on at `0e8801ab7`.
```

### 2. A row of `Test_rounds_rows` is named `absent` and stubs a plain `SystemExit(2)` that no absent file raises any more

```seal
severity: should
location: `tests/skills/test_broad_gate.py:1572-1591`
evidence: read `tests/skills/test_broad_gate.py:1572-1591`, `skills/verify/scripts/broad_gate.py:1836-1848`, `lib/sibling.py:51-58`, `lib/sibling.py:114-117`; executed `git grep -nE 'SystemExit\(' -- tests` and `git grep -n 'SystemExit\|sys.exit' -- lib/`
regression: round-1#1
```

Why it matters: the unit is `broad_gate.py#rounds_rows`, which `82b1693a0`
changed. Round 1's finding 1 and the frame's *Scope* item 4 ask that an
absent check be named in the gate's own line. The fix met that with an
`except sibling.Absent` arm ahead of `except (Refused, SystemExit)`, and
left this case's statements of the old fact standing. Its docstring says
the row covers a check "that `lib/sibling.py#load` finds absent and exits
for", and its id is `absent`. Since `82b1693a0`, `load` raises `Absent`, so
an absent file takes the new arm and writes the line. The row stubs a plain
`SystemExit(2)`, which takes the second arm silently. Nothing in
`chain_check.py`'s load chain raises a plain `SystemExit` when imported
(`lib/` raises none, and `chain_check.py:286` and `:310` exit only where
`sibling` itself is absent or the file runs as `__main__`). So the row pins
an arm no absent file reaches, under a name saying it does. The next person
to edit the gate's absent path reads this case as its coverage.
`test_names_the_absent_check_in_its_own_line_and_goes_on` is the real
absent case. The search for test stubs that build a `SystemExit` finds no
other row standing in for the loader's exit.

```python
    @pytest.mark.parametrize(
        "raised", [ValueError("planted"), SystemExit(3)], ids=["raises", "exits"]
    )
    def test_refuses_to_stop_a_run_where_the_check_will_not_load(
        self, tmp_path, monkeypatch, raised
    ):
        """A label never stops a run that passed: a check that raises or
        exits while it loads leaves the count alone beneath it. An absent
        check is `lib/sibling.py#Absent`, which the case below holds."""
```

This snippet keeps the `SystemExit` arm of `rounds_rows` and its pin. If
the fix pass judges that arm dead and removes it, the row goes with it,
and the comment at `broad_gate.py:1836-1837` still holds.

```seal
verdict: fixed d984a81ee
answer: The finding holds. The row is now `SystemExit(3)` under the id `exits`, and its docstring points at `test_names_the_absent_check_in_its_own_line_and_goes_on` for an absent check; a mutant dropping `SystemExit` from `rounds_rows`' last catch turned the renamed row red.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `changelog.md:3` names the ten commands that print the sentence
when copied alone, and says every other script ends as before. Its claim
that each script under `skills/`, `.github/scripts/` and `evals/scripts/`
reaches the plugin's other modules through `lib/sibling.py` holds (executed:
a `grep` of every tracked script there for a plain `import` or `from` of a
`lib/` stem other than `sibling` prints nothing). The sentence that a file
absent "prints ... and exits 2" is false of `release_seal.py#main`, which
finding 1 of this round holds and whose fix carries that line.

```seal
confirms: round-1#3
```
What holds: `lib/lines.py:70` spells `INVISIBLE` by code point, as the
base's `unverified_check.py:148` did (executed: round 1's check prints
`False`, and `grep -c ufe0f` prints 1). The close's scan claim holds. Of
every `.py` file the branch changes, only
`.github/scripts/publish_release_note.py` (three lines) and
`tests/skills/test_chain_check.py` (one line) hold one of the seven
characters. Each holds the same count at `3285f1a04` (executed).

```seal
confirms: round-1#4
```
What holds: the four copied-alone cases take the `["--help"]` row and pass
(executed). Each row asserts exit 2 and the sentence. A copy whose guard sat
in the first loading function would print its help at exit 0, so the
`[help]` row is the one that fails (read: the four cases at
`test_settle.py:3695`, `test_fold_check.py:367`, `test_pact_check.py:115`,
`test_payload_meter.py:1418`). The close's mutants were not run again. The
docstring line each case gains runs past 88 columns unwrapped. `ruff`
selects no line-length rule here, so this is no finding (executed: `uvx
ruff check` and `uvx ruff format --check` over the eleven changed files,
both 0).

```seal
confirms: round-1#5
```
What holds: `pr.md:2` gives A14 the reason `frame/plan.md:91` gives, that
the arm drops `skills/settle/scripts/fold_check.py` with the eight files.
Each of `pr.md`'s four quotes stands word for word at `plan.md:90`, `:91`,
`:94` and `:149` at `afc05486a` (read).

What matched: `lib/sibling.py#Absent` and `#going_on` do what the fold's
*Data & interfaces* states (read: `lib/sibling.py:51-77`, `:114-117`). The
exit's code is 2 and its `path` is the file's. Inside the block nothing is
written, and the counter nests and is restored on every way out of the
`with`. `tests/lib/test_sibling.py#Test_going_on` holds both halves, and
`seal layout --check` and `--pairs` over the three changed test modules
refuse nothing and name no pair (executed). The cases S7 names, at
`test_release_seal.py:695` and `test_broad_gate.py:1593`, stand under
those names and pass (executed).

What matched: the fold's *Scope* item 4 describes the code as it stands.
It names the two callers inside `going_on` (`release_seal.py:323`,
`broad_gate.py:1839`) and `main`'s `no seal` line at exit 0 (read).
Finding 1 weighs the last.

What matched: `routing.md`, `frame/questions.md`, `frame/plan.md`'s new
judgment row and `gaps.md`'s new row hold no sentence the target
contradicts (read). `gaps.md` takes no row out.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; this round ran the fix pass's test modules alone | the whole tree | the orchestrator, by the broad gate |
| `frame/questions.md` Q1, now with `lib/sibling.py#_going_on`, a counter at module level that one shared instance carries across the test files of a `pytest` process | `lib/sibling.py:61-77`, `frame/questions.md` Q1 | the orchestrator, by the broad gate |
| `lib/sibling.py#_same` on Windows, carried from round 1 | `lib/sibling.py:79` | CI's `windows-latest` job |
| The five workflows that run the scripts under `.github/scripts/`, carried from round 1 | `.github/workflows/` | CI, on the release pull request, the merge to `main` and the next tag |
| The fix pass's mutants for findings 1 and 4, which the close blocks report as red; this round read the cases and did not mutate | `tests/lib/test_sibling.py`, the four copied-alone cases | the sealer, against the fix pass's hand-back |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_main_absent.py <clone>`, `release_seal.main` with `sibling.ROOT` at an empty directory and `DRY_RUN=1` | return 0; stdout `no seal: Absent: 2 -- ...` and `::warning::release seal skipped: Absent: 2`; stderr the loader's sentence about `publish_release_note.py`, ending "Nothing was read." |
| `bin/test tests/lib/test_sibling.py tests/github/test_release_seal.py` with `test_broad_gate.py::Test_rounds_rows` and the four copied-alone cases | 78 passed |
| `bin/seal layout --check` over the seven changed test modules, and `--pairs` over `test_sibling.py`, `test_broad_gate.py` and `test_release_seal.py` | 0 refused; 0 pairs |
| `uvx ruff check` and `uvx ruff format --check` over the eleven changed `.py` files | exit 0 each |
| the seven invisible characters, scanned in each `.py` file the branch changes, at HEAD and at `3285f1a04` | the same four lines in two files at both commits, none new |
