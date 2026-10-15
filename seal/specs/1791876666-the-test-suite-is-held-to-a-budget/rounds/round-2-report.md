# 1791876666-the-test-suite-is-held-to-a-budget — round 2 report

Reviewed by warden at `fffee6b2` against `origin/release/v0.22.0` at
`5b1f6fae`, in a `git clone --no-local` of the worktree under the session's
scratchpad. This is a verifying round. Its target is the fix range
`9f9c9ed9..5ee4b39e` and the record commit after it, and it stayed inside
that range: the census, the wrapper case, `bin/test` and its twin, the
launcher's docstring, `ruff.toml`, the three `case_check.py` changes, their
cases, and the phase-record SHA rewrite.

## How the findings relate

Three of round 1's four findings are closed. The fourth, round 1's 🟡 3, is
closed for one spelling of a platform skip and still open for the other.

- 🟡 1 continues round 1's 🟡 3. A case skipped by a marker is now named
  `not proved`. A case that calls `pytest.skip()` in its body is still named
  `kills nothing its file does not`. That body spelling is this repository's
  more common one: 52 calls in 25 test files.
- 🟡 2 is new, and it is about the census, the fix for round 1's 🟡 2.
  `CONTRIBUTING.md` and `ruff.toml` say the census holds every hook-run file
  to Python 3.9. It holds them to 3.9's syntax and to two constructs. A
  `tomllib` import or a `str | None` signature passes the census and ruff
  both, and dies on a stock macOS `python3`.
- ⬜ 3 and ⬜ 4 are notes on two units the fixes created. ⬜ 5 is a correction
  to `questions.md`: the tree already answers Q7.

What the implementer's account asserted, and what was found:

- *"`bin/test` and `.cmd` run `run_tests.py` directly"*. This holds. Run
  from `/usr/bin/python3` 3.9.6, `bin/test` built a 3.13.9 `.venv` with uv
  and passed 27 cases, exit 0. Every other one of the 15 sh wrappers exits 2
  with the refusal sentence (`executed`). `bin/test.cmd:17` and `:21` hand
  `"%script%"` to `py -3` and to `python` (`read`; no Windows here).
- *"a derived census of the code hooks run, at Python 3.9"*. This holds for
  how it finds files. The census finds 39 files from `hooks/hooks.json`, the
  git hook stubs and `bin/`, `seal_stamp.py` and `unverified_check.py` among
  them. I planted a hook that loads `round_record.py` through
  `os.path.join`, and the census found it plus what it loads in turn
  (`chain_check.py`, `coordinates.py`), and the case went red naming all
  three. A module nothing loads was not found. A module loaded through a
  `pathlib` `/` path was not found either, which the docstring of
  `before_any_floor` admits ("under, for a module reached by a path built
  any other way"). No hook loads one that way today (`executed`, and a
  `read` grep of every hook-run file for dynamic loads). How far the census
  reaches into each file is 🟡 2.
- *"`ruff.toml`'s `[per-file-target-version]` as the one source of that
  version"*, and the claim that ruff's `*` crosses a `/`. Ruff 0.17.0 lints
  `hooks/git/` at py39 under `"hooks/*.py"`: B905 and UP017 are silent there
  and fire in `skills/verify/scripts/` (`executed`). Ruff and the census
  agree on every pattern the table holds. They disagree on a slash-less
  pattern, but only in the direction where the census refuses (⬜ 4).
- *"a case that never ran on this runner is named `NEVER_RAN`, gate
  unchanged"*. This holds for a marker skip, as round 1's fixture showed. It
  does not hold for a body skip (🟡 1).
- *"`unrun` counts only mutants on changed lines"*. This holds. A proof's
  kill is recorded for any line of a changed file, and `unrun` only counts
  labels from `every_diff`, which holds changed lines alone. The survivor
  list draws from the same labels (`read` at `case_check.py:599-606` and
  `:939-951`). The `cases` job at the tip proved
  `test_what_was_not_run_counts_only_the_changed_lines_mutants` on
  `case_check.py:606` (CI's execution, read here).
- *"(now Y)" in the phase records*. This is an in-place correction, not an
  append. Each run was measured at the pre-rebase commit X, so writing Y
  alone would claim a run that never happened on Y's tree. Writing X alone
  points at a commit the branch no longer holds. The sentence that cited X
  was edited where it stands. The one sentence added is a legend, given once
  per record, that says how to read the pair. A probe checked all 16 pairs:
  every Y is on the branch, and where X is still a local object its subject
  matches Y's. No work-item file at the tip cites an off-branch SHA without
  its twin (`executed`). That settles the SHA half of round 1's ⬜ 5. The
  note itself stays carried.
- *"nothing in the range bent a check"*. Nothing did. The bound row of the
  end-to-end case gained a changed `m.py` and an expected
  `not run within the bound` line, which adds an assertion. The row still
  ends at the restructure finding before any mutant runs. The new
  uniqueness assertion (`verdicts`) checks that each function gets one
  verdict. The `APPLIES_THE_SHARED_GUARD` row for `before_any_floor`
  registers a real call to `decline_if_shrunken`. The removed
  `if mine else SURVIVED` guard really is unreachable, because `mine` is
  `own_ids` of a name that was kept only when `own_ids` was non-empty, over
  the same `hits` (`read`).
- *"Q7 needs the owner"*. The tree answers it (⬜ 5).

Every fix holds at its own commit. The touched modules pass at 1df94b1d,
2e3b2ef7, e96f533c, a936870b, 10905de5, 5ee4b39e and fffee6b2 (`executed`,
narrow). CI run 38664361183 at fffee6b2 is green on every leg, Windows and
macOS included, which answers round 1's ❓ (`read`).

## 🟡 1 — a case that skips in its body is still named for killing nothing

`.github/scripts/case_check.py:848` names a function `NEVER_RAN` when
`own_ids` finds none of its ids in `hits`. The tracer adds an id to `hits`
when its call starts (`:152`, `:136`). A marker skip never starts the call,
so it is caught. A body skip, `if os.name != "nt": pytest.skip(...)`,
starts the call. Its first line is traced, so the id is in `hits`. It then
skips under every mutant, and `mutation-check` reads every mutant as
survived.

Executed: a fixture whose new case is `if True: pytest.skip("another
platform")` and then the assertion. `case_check.main` returned 1 and printed
`tests/test_m.py::test_double_elsewhere: kills nothing its file does not`.
That is the false reason round 1's 🟡 3 named. Four places now say a case
skipped on ubuntu is named for never having run: the module docstring at
`:76`, `test.yml:161`, `spec.md:91`, and the work item's changelog fragment,
whose *Added* entry ships as a release note. For this spelling, all four are
false, and the fix below makes them true as written.

The class is "an id whose call does not run its assertions on this runner".
The fix enumerated the marker half of it and not the body half (§12). The
paste-ready fix below drops a skipped call's id from `hits`, so both halves
take the one path the fix built. Applied in the clone, the fix turned the
fixture's line into `not proved: none of its ids ran its call on this
runner`, and the 21 cases of the module still passed (`executed`). An
xfailed call also reports as skipped, so it is left in.

## 🟡 2 — CONTRIBUTING says the census holds hook code to 3.9; it holds two constructs and the syntax

`CONTRIBUTING.md:128-129` says the census "derives the set and holds every
file of it to that version". `ruff.toml:41` says "holds each to this
version". The census does not run the code at that version, because the
suite runs at 3.12 or newer. What `newer_than` does is reject syntax that
`ast` rejects at 3.9, plus `zip(..., strict=)` and `datetime.UTC`.

Executed: I planted `import tomllib` and `def f(x: str | None = None)` in
`hooks/`. `newer_than(..., (3, 9))` returned `[]`, ruff at py39 passed it,
and `/usr/bin/python3` 3.9.6 died on the import. A hook that does this
fails open, and the reader of `CONTRIBUTING.md` was told it could not
happen. Today no hook-run file does it: all 39 compile on 3.9.6, and a grep
for `tomllib`, PEP 604 annotations and the 3.10/3.11 standard-library names
finds nothing (`executed`).

The census also misses syntax: `ast.parse(feature_version=(3, 9))` on 3.13
accepts a PEP 701 f-string, `f"{"a"}"`. Ruff at py39 refuses that one
(`invalid-syntax ... added in Python 3.12`), so the pair still covers it
(`executed`). The fix is to say what is held, not to widen the census:
round 1's finding was the two constructs ruff pushes toward, and those are
held.

## ⬜ 3 — the census case's docstring makes the same claim, in context

`tests/test_a_script_says_which_interpreter_it_needs.py:409` ends with
"holds every file of the set to that table and to that version". The
sentence just before it names B905, UP017 and the two constructs, so in
context it reads closer to the truth than `CONTRIBUTING.md` does. It should
take the same words as 🟡 2's fix when that fix lands.

## ⬜ 4 — `matches` and ruff part on a pattern with no slash

`tests/test_a_script_says_which_interpreter_it_needs.py:395`'s docstring
says it answers "whether ruff's glob `pattern` names `rel`". Ruff also
matches a pattern with no `/` against the file's basename. Executed: with
`"tmp_probe_r2.py" = "py39"` (NAME NOT IN TREE: a probe file, deleted),
ruff linted `skills/verify/scripts/tmp_probe_r2.py` (NAME NOT IN TREE: a
probe file, deleted) at py39, and `matches` answers `False` for
`seal_stamp.py` against `skills/verify/scripts/seal_stamp.py`. In that case
the census reports the file unlinted and the pattern stale. That is a false
red, never a false green, and the table holds no such pattern. Either say so
in the docstring, or add `or ("/" not in pattern and
fnmatch.fnmatchcase(posixpath.basename(rel), pattern))`.

## ⬜ 5 — Q7 is answered by the tree

`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md:25`
asks the owner whether a case that never ran on ubuntu is a finding or a
report line. Four things in the tree answer it.

- The rule. `CONTRIBUTING.md` §*A case is owed by a mutant only it kills*
  says a new case that is not its file's only killer of any mutant "fails
  the job, named". It gives no platform exception.
- The gate rule. A report line would let more through, which CONTRIBUTING
  §*What a change to a gate must carry* asks to justify. Q7's own option
  text names the bypass a report line opens (`skipif(True)`).
- The first goal. `CLAUDE.md`'s first goal makes the design that asks a
  person the costlier one.
- The cost of a red. A red `cases` job does not strand a legitimate
  Windows-only case: the release branch's ruleset requires no status check
  (`gh api …/rules/branches/release%2Fv0.22.0`, read). Such a case lands the
  way a named `restructure` does, with its finding read.

Q7 belongs with the questions the tree answered, at the top of the file.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A new case that calls `pytest.skip()` in its body still starts its call, so it is in `hits`, escapes `NEVER_RAN`, and is named `kills nothing its file does not`; round 1's 🟡 3 is closed only for a marker skip, and the docstring, `test.yml:161` and `spec.md:91` are false for this spelling | `.github/scripts/case_check.py:848` | open | executed: fixture with an in-body skip, `main` returned 1 with the false reason; the paste-ready fix applied in the clone names it `not proved` and the module's 21 cases pass |
| 🟡 2 | `CONTRIBUTING.md` and `ruff.toml` say the census holds every hook-run file to 3.9; it holds 3.9's syntax as `ast` sees it and two constructs, and `import tomllib` or a `str \| None` signature passes it and ruff and dies on 3.9 | `CONTRIBUTING.md:128`, `ruff.toml:41` | open | executed: planted file, `newer_than` returned `[]`, ruff passed, 3.9.6 raised on import; no hook-run file does this today (39 compile on 3.9.6, grep clean) |
| ⬜ 3 | The census case's docstring ends on the same claim as 🟡 2, softened by the sentence before it | `tests/test_a_script_says_which_interpreter_it_needs.py:409` | open | read |
| ⬜ 4 | `matches` says it answers whether ruff's glob names a path, but ruff also matches a slash-less pattern against the basename; the census then refuses a table ruff honours, and is never more lenient than ruff | `tests/test_a_script_says_which_interpreter_it_needs.py:395` | open | executed: ruff 0.17.0 with a basename pattern linted the file at py39; `matches` returned False |
| ⬜ 5 | Q7 is listed as waiting on the owner, and the tree answers it: the case rule has no platform exception, a report line would let more through with the bypass Q7 itself names, and no status check is required on the release branch | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md:25` | open | read: `CONTRIBUTING.md` §*A case is owed by a mutant only it kills* and §*What a change to a gate must carry*, `CLAUDE.md`, the branch ruleset |
| 🟢 | round 1's blocking finding 1 is closed — `bin/test` and its twin hand `run_tests.py` to the interpreter directly | `bin/test:36`, `bin/test.cmd:17` | confirmed | executed: from `/usr/bin/python3` 3.9.6, `bin/test` built a 3.13.9 `.venv` and passed 27, exit 0; the 14 other sh wrappers exit 2 with the refusal |
| 🟢 | round 1's finding 2 is closed — hook-run code is derived, linted at py39, and kept free of `zip(..., strict=)` and `datetime.UTC` | `tests/test_a_script_says_which_interpreter_it_needs.py:401`, `ruff.toml:42` | confirmed | executed: the census found a planted `os.path.join` load and its transitive imports and went red; ruff at py39 silences B905 and UP017 under `hooks/git/` |
| 🟢 | round 1's finding 3 is closed for a case skipped by a marker | `.github/scripts/case_check.py:848` | confirmed | executed at fffee6b2 by the row `a case that ran nowhere here is named for that`; the body-skip half is 🟡 1 |
| 🟢 | round 1's finding 4 is closed — the not-run count reads changed lines' mutants only | `.github/scripts/case_check.py:599` | confirmed | read: `unrun` counts `every_diff` labels; CI's `cases` job at fffee6b2 proved its case on `:606` |
| 🟢 | round 1's ❓ on the Windows and macOS legs | CI run 38664361183 | answered | read: every leg of the tip's run is green, `cases` 21 proved, 0 named |

## Paste-ready fixes

### 🟡 1

`.github/scripts/case_check.py`, inside `TRACER_SOURCE`, the globals line:

```python
_hits, _seen, _now, _seconds, _skipped = {}, {}, [None], {}, set()
```

Above `pytest_sessionfinish`, in the same string:

```python
# A call that skipped in its body started, so its first lines are traced,
# but it asserts nothing on this runner: it is dropped, and the check names
# it as one that never ran. An xfailed call also reports as skipped and
# stays, since under a mutant it can pass and fail a strict mark.
def pytest_runtest_logreport(report):
    if report.when == "call" and report.skipped:
        if not hasattr(report, "wasxfail"):
            _skipped.add(report.nodeid)
```

And the first line of the `with` block in `pytest_sessionfinish`:

```python
        hits = {k: sorted(v) for k, v in _hits.items() if k not in _skipped}
```

`tests/test_a_new_case_protects_what_its_file_did_not.py`, beside
`ELSEWHERE`:

```python
IN_BODY = (
    "\nimport pytest\n\n\ndef test_double_elsewhere():\n"
    '    if True:\n        pytest.skip("another platform")\n'
    "    assert m.double(2) == 4\n"
)
```

And a row beside `a case that ran nowhere here is named for that`:

```python
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, IN_BODY)},
            {},
            1,
            [
                "tests/test_m.py::test_double_elsewhere: not proved: none of "
                "its ids ran its call on this runner"
            ],
            id="a case that skips in its body is named as one that never ran",
        ),
```

The module docstring at `:76`, so its claim covers both spellings:

```text
It runs on ubuntu alone. A case none of whose ids runs its call there to
the end, as one skipped off Windows by a mark or in its body, can fail under
no mutant, so it is named for that, `not proved: none of its ids ran its call
on this runner`, and the job fails as it does for any case not proved.
```

### 🟡 2

`CONTRIBUTING.md:127-129`:

```markdown
`ruff.toml` lints that code at the version its `per-file-target-version`
names, and `tests/test_a_script_says_which_interpreter_it_needs.py` derives
the set, holds every file of it to that table, and refuses in it the syntax
`ast` rejects at that version and the two constructs ruff pushes toward above
it, `zip(..., strict=)` and `datetime.UTC`. Nothing runs that code at that
version, so a standard-library module or an annotation only a newer
`python3` has, as `tomllib` or `str | None` in a signature, passes both.
```

`ruff.toml:40-41`:

```toml
# tests/test_a_script_says_which_interpreter_it_needs.py derives that set,
# holds every file of it to this table, and refuses in each the syntax and the
# two constructs above that this version lacks; nothing runs it at 3.9.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_script_says_which_interpreter_it_needs.py tests/test_a_new_case_protects_what_its_file_did_not.py -q`, with `/usr/bin/python3` 3.9.6 first on `PATH`, clone at fffee6b2 | exit 0; built `.venv` on CPython 3.13.9 with uv; 27 passed |
| each sh wrapper in `bin/` with `--help`, with `/usr/bin/python3` 3.9.6 first on `PATH` | 14 exit 2 with `<name>: needs python 3.12 or newer, and this is python 3.9.6 at …`; `bin/test` exit 0 |
| the touched modules at each fix commit: 1df94b1d, 2e3b2ef7, e96f533c, a936870b, 10905de5, 5ee4b39e, fffee6b2 (`test_a_shrunken_corpus_declines_to_judge.py` beside the census commits) | exit 0 at each |
| `before_any_floor()` at fffee6b2 | 39 files, `seal_stamp.py`, `unverified_check.py` and `run_tests.py` among them; nothing missing |
| probe `test_tmp_census_r2.py` (NAME NOT IN TREE: deleted after the run): a hook gains an `os.path.join` path to `round_record.py`; an unloaded module with `zip(..., strict=True)`; a hook gains a `pathlib` `/` path to `broad_gate.py` | the first is found with `chain_check.py` and `coordinates.py`, and the case fails naming all three; the second is not found; the third is not found (an admitted miss) |
| ruff 0.17.0, `--select B905,UP017`, on one planted file under each of `hooks/git/`, `hooks/`, `skills/verify/scripts/`, `.github/scripts/` | B905 and UP017 fire in the last two only |
| ruff 0.17.0 with a slash-less `per-file-target-version` pattern; then with `hooks/*.py` at py39 and `hooks/git/*.py` at py312 | basename pattern honoured at py39; the overlap linted at py39, as the census's `min` reads it |
| a planted hook file with `import tomllib` and `str \| None`: `newer_than`, ruff at py39, `/usr/bin/python3` | `[]`; ruff passed; 3.9.6 raised `ModuleNotFoundError` |
| `ast.parse(..., feature_version=(3, 9))` on 3.13 of a PEP 701 f-string; ruff at py39 on it and on a `match` | `ast` accepts the f-string; ruff refuses both |
| every census file compiled with `/usr/bin/python3` 3.9.6, and a grep for `tomllib`, PEP 604 annotations, `pairwise`, `StrEnum`, and dataclass `slots=` and keyword-only fields | all compile; the grep finds nothing |
| probe `test_tmp_skip_r2.py` (NAME NOT IN TREE: deleted after the run): `case_check.main` on a fixture whose new case calls `pytest.skip()` in its body | exit 1, `kills nothing its file does not` |
| probe `test_tmp_fix_r2.py` (NAME NOT IN TREE: deleted after the run): 🟡 1's paste-ready tracer fix applied in the clone, then reverted | the fixture's case is named `not proved: none of its ids ran its call on this runner`; `test_a_new_case_protects_what_its_file_did_not.py` 21 passed |
| probe `test_tmp_shas_r2.py` (NAME NOT IN TREE: deleted after the run): every 8-hex SHA in the work item's files but the round records, against `merge-base --is-ancestor` and each twin's subject | 16 `X (now Y)` pairs, every Y on the branch, every subject matched; no off-branch SHA without its twin |
| `gh api` jobs and the `cases` job log of CI run 38664361183 at fffee6b2 (CI's execution, read here) | every job green; `cases`: 21 proved, 0 named, 299 s; 651 not run within the bound |
| Broad gate (full suite, repository-wide lint, typecheck) | not yet: not run by this round, and owed to the sealer once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round 1, ⬜ 5 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | carried, closes at the run's end; its SHA half now has a twin for every off-branch commit (probe above) |
| round 1, ⬜ 6 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | carried, closes at the run's end |
| round 1, ⬜ 7 | `CONTRIBUTING.md:146` | carried, closes at the run's end |

Needs a fix: yes — 🟡 1 (a case that skips in its body is still named for killing nothing), 🟡 2 (the census is said to hold hook code to 3.9 and holds two constructs and the syntax)
Loses a record or crashes: no

Nothing here needs the sealer yet: two 🟡 are open, so the broad gate is not
due until the round that verifies their fixes leaves nothing open.

## Proof block

Files opened: `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-1.md`,
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/questions.md`,
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-1-report.md` (head),
`.github/scripts/case_check.py` (`:100-180`, `:575-606`, `:630-735`, `:791-965`),
`tests/test_a_new_case_protects_what_its_file_did_not.py` (`:1-60`, `:272-350`, `:470-490`),
`hooks/sealer-stamp.py:70-110`, `hooks/review-history-guard.py:75-100`,
`.github/workflows/test.yml:150-200`, `CONTRIBUTING.md` (the floor and case paragraphs, §*What a change to a gate must carry*),
`seal/specs/1791876666-the-test-suite-is-held-to-a-budget/spec.md` (grep), `plan.md:16`,
and the fix range's diff of `.github/`, `bin/`, `hooks/`, `ruff.toml`, `tests/`, `CONTRIBUTING.md`, and ad83cfc0's diff.
