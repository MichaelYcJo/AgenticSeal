# 1791384152-a-reader-declares-its-input-class — review round 1

| Field | Value |
|---|---|
| Target SHA | 03784ec3418e3536c7d6e96b1feb8782fef9bd6e |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 895 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `8f3d912e195fc850c9109228ec38713bea64811e..f21f151fe83279cf6be05cf7bdedc909f8f568ca`, 6 commits |
| Contract changes | none |
| New units | test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (K1 rows the receiver rule hides), 🟡 2 (a `## Removes` path that escapes or will not read passes as gone), 🟡 3 (K7's false note, the re-stamped anchors that miss `cutoff_row`, and the changelog's upgrade note) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of #835 (PR #895), target 03784ec3 against `origin/release/v0.21.0` at c38f97d7. Attack in this order:

1. **The item must not be a reader that predicts a foreign tool.** The owner's 0.21.0 theme is that a reader observes, forces a format, or is deleted. `tests/reader_registry.py`'s walker and the `Reads:` grammar must not imitate a parser, a lexer, or pytest collection. Check whether the K1 table, or the receiver rule that excludes `ast.walk`, is a guess dressed as a table.
2. **The census can be grown by hand.** The writer refuses to overwrite an existing file, but a line put back by hand passes (the seventh limit). Read the census diff: does any line name a unit that is new or changed on this branch?
3. **The population edge.** Units inside module-level `if`, `try`, `except` and `with` are counted. Check that the walker and `py_spans` agree on such a unit's key, and that a nested def is not counted.
4. **The `## Removes` arm** (`evidence_check.py#removes_section`, `STANDING`/`REFUSED`, exit 2). Try a section with a cutoff and no `Removes from`, a `Removes from` that is not an id, a removed name still in the tree, and a heading inside a fenced block.
5. **The retirement of the per-phase removal table** across five files, and the `Corrected · R5` row against 0.8.0's R5. Are any stale references left in the agents or skills?
6. **The in-place re-stamps** in the live fragments 1791384154, 1791384156, 1791384158 and 1791384159. Is every re-stamped claim still true?
7. **The divergence table in `overview.md`**: K1 620 vs 621, S9 exiting 2 not 1, one-line declarations. Judge each one on its grounds.

Facts arriving as coordinates, executed by the orchestrator at 03784ec3: `bin/evidence-check . --strict` exit 0. Everything else in the smith's report is the smith's, unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | K1's receiver rule treats the table as complete for every module it names; reading calls the table lacks (`os.open`, `os.path.islink`, `re.split`, `shlex.shlex` and others) pass a `nothing`, and `os.open` was caught by name before the rule | `tests/reader_registry.py:209` | **fixed** `e6843d9a` | fixed at e6843d9a; executed differential at the target; the document places `open`, existence tests and the `re` matchers inside K1's families |
| 🟡 2 | a `## Removes` row whose path `place` refuses, or that names a directory or unreadable file, is read as a removal that happened | `skills/evidence-check/scripts/evidence_check.py:6130` | **fixed** `20c4e993` | fixed at 20c4e993; executed: both rows gave no finding; the ledger arm calls the escape BROKEN, and the spec says a coordinate the ledger would refuse is refused here |
| 🟡 3 | plain `evidence-check` now refuses an unreadable `seal/config.md`; K7's re-stamped note says it reads no config row, three re-stamped rows anchor `frozen_from` whose arms moved to `cutoff_row`, and the changelog's upgrade note omits the change | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24` | **fixed** `978aa43a` | fixed at 978aa43a; executed: target exit 2, base exit 0 on a directory `config.md`; the rows and the changelog read |
| ⬜ 4 | this item's `## Removes` does not name the two pins the diff removed, and `overview.md` has no divergence row for them | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:508` | **fixed** `1aa26afa` | fixed at 1aa26afa; read; the spec's own prose says the pins go too |
| ⬜ 5 | two descriptions of a phase record still say it records what it removed | `skills/code-review/scripts/survivor_check.py:142` | answered | the two descriptions in `survivor_check.py` are of phase records as the check meets them, and every phase record written before #835 does carry what it removed; the check reads those records, so the sentence stays true where it stands; read; still true of records already written |
| ⬜ 6 | the census writer can emit a line its own grammar refuses, for a path with whitespace | `tests/reader_registry.py:461` | answered | the writer runs only where no census exists, and this repository's census exists; a path with whitespace in it would be refused line by line by the test that reads it, which is loud, and widening `CENSUS_LINE` is mechanism a fix pass does not add; read; latent while the census file exists |
| 🟢 | no census line names a unit new or changed on this branch, and the census has only shrunk since its cut | `tests/undeclared_readers.txt` | confirmed | executed: 1,584 hashes against `c38f97d7`, and the diff from `33d0b0ca` is three removals |
| 🟢 | the walker and `py_spans` agree on the key of a unit inside a module-level `with`, `if`/`else` and `for`, and a nested `def` is not counted | `tests/reader_registry.py:403` | confirmed | executed on a planted file |
| 🟢 | the `## Removes` arm reads a section with no `Removes from` row, refuses a doubled row, reports a standing dotted name, and ignores a heading and a row inside a fence | `skills/evidence-check/scripts/evidence_check.py:6032` | confirmed | executed, eight planted cases |
| 🟢 | no agent or skill still instructs the retired removal table, and `Corrected · R5` matches 0.8.0's R5 | `agents/smith.md:181` | confirmed | read across agents, skills, templates and docs |
| 🟢 | the divergence table's K1 count, S9 exit code and one-line grammar each stand on their grounds | `seal/specs/1791384152-a-reader-declares-its-input-class/overview.md:26` | confirmed | the K1 count executed; the other two read against spec S1 and the grammar section |

## Paste-ready fixes

```python
# tests/reader_registry.py — add to K1_FUNCTIONS. A module K1 names is judged
# by this table alone, so a reading function it exports is a row here or it
# is not seen.
        "os.open",
        "os.read",
        "os.fdopen",
        "os.readlink",
        "os.lstat",
        "os.access",
        "os.path.islink",
        "os.path.getsize",
        "os.path.getmtime",
        "re.split",
        "shlex.shlex",
```
```python
# tests/test_a_reader_declares_its_input_class.py — two rows for
# test_nothing_beside_a_k1_primitive_is_refused_naming_the_call
        ("import os", "return os.open(p, 0)", "os.open"),
        ("import re", "return re.split(',', s)", "re.split"),
```
```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, in place
# of the two lines that read the body and skip a None
        raw_path, locator, claim = m.group("path"), m.group("locator"), m.group("claim")
        repo, rel = place(root, maps, default_repo, raw_path)
        if repo is None:
            findings.append(
                (
                    REFUSED_STATUS,
                    where,
                    f"`{cell}` — the path escapes the repository, so nothing it "
                    "names can be read as gone — write a path inside the tree",
                )
            )
            continue
        full = os.path.join(repo, rel)
        body = read(full)
        if body is None:
            if os.path.lexists(full):
                findings.append(
                    (
                        REFUSED_STATUS,
                        where,
                        f"`{cell}` — the path is there and will not read as a "
                        "file, so nothing in it can be read as gone",
                    )
                )
            continue
```
```python
# tests/test_a_record_states_what_the_tree_has.py
def test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone(tmp_path):
    """S5 of #835. `place` refuses a path out of the tree, and a directory
    will not read; neither is a removal that happened."""
    root = tmp_path / "r"
    tree(root, **{"pkg__sub.d__x.py": "def g():\n    return 1\n"})
    (tmp_path / "outside.py").write_text("def f():\n    return 1\n", encoding="utf-8")
    h = home(root)
    rows = "| x | `../outside.py#f` | y |\n| x | `pkg/sub.d#g` | y |\n"
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _ = refusals(root)
    assert [s for s, _c, _d in found] == ["REFUSED", "REFUSED"]
```
```text
seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24, K7
- Code grounds: add `skills/evidence-check/scripts/evidence_check.py#cutoff_row@dc04c433`
  beside `frozen_from@060d5968`.
- Verified behavior: after "`frozen_from`'s unreadable arm and its doubled arm
  removed" add "(both arms in `cutoff_row` since #835)".
- Notes: replace the last sentence with
  "Since #835 the records arm reads `Removes from` through `cutoff_row`, so a
  plain `evidence-check` refuses a `seal/config.md` that will not read, or that
  writes `Removes from` twice, at exit 2 too."

Same file, line 16 (Corrected · C1), and
seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:13
(Corrected · --reverify --into): add
`skills/evidence-check/scripts/evidence_check.py#cutoff_row@dc04c433`
beside `frozen_from@060d5968`, then let `--reverify` confirm the hash.
```
```text
seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md,
appended to the paragraph "What an installer sees on upgrade":

  A `seal/config.md` that is there and will not read, or that writes
  `Removes from` twice, now stops a plain `evidence-check` run at exit 2,
  as it already stopped `--reverify`: the records arm reads the row through
  the freeze row's reader, which refuses such a file rather than reading it
  as absent. A repository that declares no `Removes from` row meets this too.
```

## Executed probes

| What was run | Result |
|---|---|
| census against the base: every census line rehashed at `c38f97d7`, and the census as cut at `33d0b0ca` diffed against the target | executed: 0 of 1,584 lines new or changed; 1,587 at the cut, three lines removed since |
| population at the target, and each unit new or changed against the base with its declaration | executed: 1,607 units, 23 new or changed, all 23 declare |
| K1 with and without the receiver rule, over every unit at the target | executed: 627 against 630 units; the difference is the three `ast.walk` callers; `os.open` appears twice, in units that call another primitive |
| eight planted `## Removes` and population cases in one probe module under `tests/` | executed: escaping path, no finding; directory path, no finding; `## Removes ##`, refused as no section; fenced heading and row, not read; no `Removes from` row, still `STANDING`; doubled row, `REFUSED`; a prose line beginning `nothing`, `REFUSED`; module-level block keys agree |
| plain checker on a root whose `seal/config.md` is a directory, and on one with `Removes from` twice, at the target and at the base | executed: target exit 2 `REFUSED` for both; base exit 0 for the directory |
| `bin/test` over `tests/test_a_reader_declares_its_input_class.py`, `tests/test_a_phase_hands_the_next_one_a_record.py`, `tests/test_a_shrunken_corpus_declines_to_judge.py`, `tests/test_the_pull_request_language_is_the_repositorys.py` | executed: 231 passed, exit 0 |
| `bin/test` over the records-arm and freeze modules, narrowed with `-k` to the `## Removes` and cutoff cases | executed: 28 passed, exit 0 |
| `bin/evidence-check . --strict` at `03784ec3` | not run in this round; the orchestrator's executed fact, exit 0 |
| the broad gate (full suite, lint, typecheck) | not yet; the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
