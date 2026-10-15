# 1791876666-the-test-suite-is-held-to-a-budget — review round 2

| Field | Value |
|---|---|
| Target SHA | fffee6b2f1663732188b0dfa74c072cc2c5f863b |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #939 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | first — 🟡 1 at .github/scripts/case_check.py#check, a unit round-1's fixes changed |
| Needs a fix | yes — 🟡 1 (a case that skips in its body is still named for killing nothing), 🟡 2 (the census is said to hold hook code to 3.9 and holds two constructs and the syntax) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Verifying round 2 of #929: round 1's fixes over 9f9c9ed9..5ee4b39e (bin/test outside the launcher, the derived hook-run census at 3.9 with ruff's per-file target, NEVER_RAN for a case that never ran, unrun on changed lines), whether Q7 needs a person, and the (now Y) annotations. Narrow checks only.

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

```python
_hits, _seen, _now, _seconds, _skipped = {}, {}, [None], {}, set()
```
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
```python
        hits = {k: sorted(v) for k, v in _hits.items() if k not in _skipped}
```
```python
IN_BODY = (
    "\nimport pytest\n\n\ndef test_double_elsewhere():\n"
    '    if True:\n        pytest.skip("another platform")\n'
    "    assert m.double(2) == 4\n"
)
```
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
```text
It runs on ubuntu alone. A case none of whose ids runs its call there to
the end, as one skipped off Windows by a mark or in its body, can fail under
no mutant, so it is named for that, `not proved: none of its ids ran its call
on this runner`, and the job fails as it does for any case not proved.
```
```markdown
`ruff.toml` lints that code at the version its `per-file-target-version`
names, and `tests/test_a_script_says_which_interpreter_it_needs.py` derives
the set, holds every file of it to that table, and refuses in it the syntax
`ast` rejects at that version and the two constructs ruff pushes toward above
it, `zip(..., strict=)` and `datetime.UTC`. Nothing runs that code at that
version, so a standard-library module or an annotation only a newer
`python3` has, as `tomllib` or `str | None` in a signature, passes both.
```
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
| round-1 | `bin/test:35`, `bin/test.cmd:14` | round 1's 🔴 1 — fixed |
| round-1 | `tests/test_a_script_says_which_interpreter_it_needs.py:185`, `skills/verify/scripts/unverified_check.py:641` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/case_check.py:861` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/case_check.py:875` | round 1's 🟡 4 — fixed |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-2.md:6` | round 1's ⬜ 5 — open |
| round-1 | `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/overview.md:7` | round 1's ⬜ 6 — open |
| round-1 | `CONTRIBUTING.md:146` | round 1's ⬜ 7 — open |
| round-1 | CI run 38658107547 | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
