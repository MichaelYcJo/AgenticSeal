# Round 1 report — a reader declares its input class (#835)

Reviewed at `03784ec3` against `origin/release/v0.21.0` at `c38f97d7`, in a
`git clone --no-local` of the worktree. No earlier round exists, so nothing
was carried. The smith's account (`overview.md`, the commit messages, the
ledger fragment) was read in full and treated as claims; each one I relied on
is checked below against the code or a probe.

## How the findings relate

```
asked 1  K1 and the receiver rule ......... 🟡 1  the rule hides reading calls the table lacks
asked 2  the census ........................ clean (executed)
asked 3  the population edge ............... clean (executed)
asked 4  the ## Removes arm ................ 🟡 2  a path that escapes or will not read is "gone"
asked 5  the retired removal table ......... ⬜ 4, ⬜ 5  paperwork only
asked 6  the in-place re-stamps ............ 🟡 3  the new config read made one re-stamped row false
asked 7  the divergence table .............. every row stands on its grounds
```

🟡 3 is a consequence of the same commit as 🟡 2. `check_records` now calls
`cutoff_row` on every run, so the plain checker reads `seal/config.md` for the
first time. That is the change the K7 row and the changelog did not follow.

## What each asked item came to

**1. The walker does not imitate a foreign tool, and K1's table is used only
where a missing row is cheap.** The population is `git ls-files` plus `ast`,
both observed. The test-module exclusion is a rule this repository owns on the
file name, and it is not pytest's collection: `tests/sub/test_deep.py` is in
the population, which pytest would collect. The `Reads:` grammar is owned by
`tests/reader_registry.py`. K1 is a closed list over an open domain, which the
document says plainly, and it decides only whether a `nothing` is a
contradiction. The receiver rule is where this goes wrong (🟡 1).

**2. No census line names a unit that is new or changed on this branch.**
Executed. Every one of the 1,584 lines was hashed against its unit at the base
`c38f97d7`, and every hash matches. The census as first cut at `33d0b0ca`
held 1,587 lines, and the only edits since are three removals:
`check_records`, `file_claims` and `frozen_from`, each of which now declares.
At the target the population is 1,607 units, which is 1,584 census lines plus
23 declared units, and those 23 are exactly the units new or changed against
the base.

**3. The walker and `py_spans` agree on the key of a unit inside a
module-level block, and a nested `def` is not counted.** Executed on a planted
file with a `def` inside `with`, inside both arms of an `if`/`else`, inside
`for`, and a nested `def` inside a function. `top_units` returned the four
top-level names and not the nested one, `resolve_unit` resolved each, and the
name defined twice was hashed over both spans and written once to the census.

**4. The `## Removes` arm holds on every case the brief named, and fails one
it did not.** Executed. With `Ledger frozen from` declared and no `Removes
from` row, a section is still read and a standing name is `STANDING`. `Removes
from` written twice is refused naming the row. A `## Next` heading inside a
fence does not end the section, a row inside that fence is not read, and a row
after the fence is. The case that fails is a coordinate `place` refuses, which
is 🟡 2.

**5. No agent or skill still instructs a removal table.** Read. The framer,
the smith, `skills/implement/SKILL.md`, `docs/the-agent-set.md` and
`templates/sdd-phase.md` all point at the frame's section. Two descriptions in
`skills/code-review/scripts/survivor_check.py` still say a phase record holds
what it removed, which stays true of the records already written (⬜ 5). The
`Corrected · R5` row matches 0.8.0's R5: the field-table claim is unchanged,
the *three sections* claim now reads two, and the renamed case is cited by its
new name.

**6. Every re-stamped claim but one still holds.** Read, and executed where
noted. The seven `agents/smith.md#"## Phases"` rows in fragment 1791384154
make claims the edit to the phase-record sentence does not touch. The S8
re-read in 1791384156 and 1791384158 still holds, because the new removal
section follows the `Row | Value | Absent` shape two earlier sections already
use, and `test_the_template_is_one_item_value_table_whose_first_row_is_the_language`
passes. The O5 and K25 rows on `APPLIES_THE_SHARED_GUARD` hold, since the
registry's scope is now listed there. K7 in 1791384156 does not hold (🟡 3).

**7. Each divergence in `overview.md` stands on its grounds.**

- K1 620 against 621. The smith's account is right. Executed at the target,
  the receiver rule changes the set of K1-calling units by exactly the
  `ast.walk` callers: `skills/verify/scripts/arm_check.py#_refuse_unknown` and
  two new units in `tests/reader_registry.py`. It also drops two `os.open`
  calls, in `skills/implement/scripts/seal.py#write_zip` and
  `skills/implement/scripts/seal.py#write_members`, and both units call another
  primitive, so the unit count does not move. The count is right, and the
  rule behind it is 🟡 1.
- S9 exiting 2, not 1. Spec S1 grades `STANDING` like a stated name the tree
  lacks, and `exit_code` counts every records finding other than `DRIFTED`
  and `EXTERNAL` as refused. Exit 2 is the spec's answer, and the plan's cell
  was wrong.
- One-line declarations. The direction word is read as the last word of one
  line, and the grammar says one line per unit. A wrapped line has no last
  word to find without deciding where prose ends, so the narrowing is sound.
- The census shrinking by convention, and the population's edge, are stated
  where a reader meets them, and both are measured in items 2 and 3.

## Findings

### 🟡 1 · The receiver rule turns K1's table into a complete list for every module it names, and the table is not complete

`tests/reader_registry.py:209`. Where a method's receiver is a module K1
names, `k1_call` judges the call by `K1_FUNCTIONS` alone. `K1_MODULES` is
derived from that same table, so the rule asserts that the table lists every
reading function of `os`, `os.path`, `re`, `shlex`, `json`, `ast`, `glob`,
`csv` and the rest.

It does not. Measured at the target, calls of these exist in the tree and are
judged by no row: `os.open`, `os.fdopen`, `os.readlink`, `os.access`,
`os.path.islink`, `os.path.getsize`, `os.path.getmtime`, `re.split` and
`shlex.shlex`. `os.open` was caught before the rule by its method name and is
not caught now, and `os.read` would fall the same way. The document names the
families as *the process boundary (`open` … directory listings and existence
tests)* and *the `re` matchers*, so `os.open`, `os.path.islink` and `re.split`
sit inside families the reader is told K1 covers.

Why it matters: a `nothing` on a unit calling one of these passes. No unit
does so today, since the tree's six `nothing` declarations are all in
`tests/reader_registry.py`. But the next unit that does is the contradiction
this check exists to see, and its miss is now caused by the rule written to
remove one false positive, not by a row nobody thought of. The fix is the
missing rows and one case per family, below.

### 🟡 2 · A `## Removes` row whose path escapes the tree, or does not read, is read as a removal that happened

`skills/evidence-check/scripts/evidence_check.py:6130`. `removal_findings`
computes `body = None if repo is None else read(...)` and then skips the row
when `body is None`. `place` returns no repository for a path outside the
tree, and `read` returns None for a directory or a file that will not open.
All three come out as no finding, which is the verdict for a removal that
happened.

Executed: `../outside.py#f`, with that file present one level above the root
and defining `f`, gave no finding. `pkg/sub.d#g`, where `pkg/sub.d` is a
directory, gave no finding. The ledger arm calls the first `BROKEN` with
*path escapes the repository*, and `place`'s own docstring says it answers
None *rather than a quiet skip, so all three callers have to say something
about such a row*.

Why it matters: the spec's rule for this arm is *a coordinate the ledger would
refuse is refused here, never read as gone*, and the test for the bare-symbol
case is named after that sentence. A row nobody can check passes as a claim
that holds. Only a file that is genuinely absent is a removal that happened.

### 🟡 3 · The plain checker now refuses an unreadable `seal/config.md`, and the records that describe it say it does not

The behaviour is deliberate and documented in `templates/config.md`:
`check_records` calls `cutoff_row` at
`skills/evidence-check/scripts/evidence_check.py:6294`, before its early
return, so every `evidence-check` run reads the config file. Executed: with
`seal/config.md` as a directory, the target exits 2 with `REFUSED
seal/config.md` and the base exits 0. With `Removes from` written twice, the
target exits 2. Three records did not follow.

- K7 in `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24`
  ends *`evidence-check` without `--reverify` reads no config row, so it is
  not among the commands that refuse*. That is now false, and this branch
  re-stamped the row in place with `2026-10-12` as if re-read.
- The same row, C1 on line 16, and the `Corrected ·` row in
  `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:13`
  were re-stamped to `frozen_from@060d5968`. That hash now covers a one-line
  delegation. The unreadable and doubled-row arms these claims rest on, and
  that K7's verified-behaviour cell says were mutated, moved into
  `cutoff_row`, which none of the three rows cites. An edit to those arms will
  no longer drift any of them.
- The changelog's *What an installer sees on upgrade*
  (`seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:38`)
  does not say that a consuming repository's plain `evidence-check`, and so
  its CI ledger job and commit advisor, now stops at exit 2 on a config file
  that will not read, whether or not it declares `Removes from`.

Why it matters: the ledger's rows fold into the released files, and K7 would
ship a false sentence about which commands refuse. The changelog is the one
place an installer learns that a run that passed before now fails.

### ⬜ 4 · This item's own `## Removes` does not name the two pins it removed

`seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:508`. The
section names the phase template's heading. The diff also removes two pins
from `tests/test_a_phase_hands_the_next_one_a_record.py`:
`test_removes_section_is_a_table_with_a_none_row` is deleted, and `test_all_three_sections_exist_outside_comments` is renamed. NAME NOT IN TREE
§*What this item removes* says *and its pins*. Neither appears as a row or as
a divergence in `overview.md`, which is where the document sends a removal the
frame did not name.

### ⬜ 5 · `survivor_check.py` still describes a phase record as recording what it removed

`skills/code-review/scripts/survivor_check.py:142` and `:917`
(`records_a_past_state`). Both say a phase record holds *what it removed*.
That stays true of every phase record already written, so the behaviour and
the fact are right, and only the description of a new record is stale.

### ⬜ 6 · The census writer would write a line its own grammar refuses

`tests/reader_registry.py:461`. `CENSUS_LINE` takes a path with no whitespace,
`#` or `@`, while `test_a_path_with_a_space_is_one_path` shows such a path is
in the population. `write_census` writes whatever `census_lines` returns, so a
census cut over a tree holding `hooks/two words.py` would be refused line by
line by the test that reads it. The writer refuses to run again while the file
exists, so this is latent.

## Regression tests to plant

- `tests/test_a_reader_declares_its_input_class.py`: two rows in
  the existing contradiction case's parameter list, `os.open` and `re.split`
  (🟡 1). Seen red against the target by construction: neither name is in
  `K1_FUNCTIONS`, and the receiver rule stops the name match.
- `tests/test_a_record_states_what_the_tree_has.py`: one case for an escaping
  path and a directory path, both `REFUSED` (🟡 2). Seen red: the probe above
  returned no finding for both at the target.

## Facts for the evidence ledger

- At `03784ec3` the receiver rule changes which units call a K1 primitive only
  through `ast.walk` (627 with the rule, 630 without), and it drops two
  `os.open` calls whose units call another primitive.
- At `03784ec3` the census lists 1,584 units, every hash matches its unit at
  `c38f97d7`, and the 23 units outside it are exactly the units new or changed
  against that base.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | K1's receiver rule treats the table as complete for every module it names; reading calls the table lacks (`os.open`, `os.path.islink`, `re.split`, `shlex.shlex` and others) pass a `nothing`, and `os.open` was caught by name before the rule | `tests/reader_registry.py:209` | open | executed differential at the target; the document places `open`, existence tests and the `re` matchers inside K1's families |
| 🟡 2 | a `## Removes` row whose path `place` refuses, or that names a directory or unreadable file, is read as a removal that happened | `skills/evidence-check/scripts/evidence_check.py:6130` | open | executed: both rows gave no finding; the ledger arm calls the escape BROKEN, and the spec says a coordinate the ledger would refuse is refused here |
| 🟡 3 | plain `evidence-check` now refuses an unreadable `seal/config.md`; K7's re-stamped note says it reads no config row, three re-stamped rows anchor `frozen_from` whose arms moved to `cutoff_row`, and the changelog's upgrade note omits the change | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24` | open | executed: target exit 2, base exit 0 on a directory `config.md`; the rows and the changelog read |
| ⬜ 4 | this item's `## Removes` does not name the two pins the diff removed, and `overview.md` has no divergence row for them | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:508` | open | read; the spec's own prose says the pins go too |
| ⬜ 5 | two descriptions of a phase record still say it records what it removed | `skills/code-review/scripts/survivor_check.py:142` | open | read; still true of records already written |
| ⬜ 6 | the census writer can emit a line its own grammar refuses, for a path with whitespace | `tests/reader_registry.py:461` | open | read; latent while the census file exists |
| 🟢 | no census line names a unit new or changed on this branch, and the census has only shrunk since its cut | `tests/undeclared_readers.txt` | confirmed | executed: 1,584 hashes against `c38f97d7`, and the diff from `33d0b0ca` is three removals |
| 🟢 | the walker and `py_spans` agree on the key of a unit inside a module-level `with`, `if`/`else` and `for`, and a nested `def` is not counted | `tests/reader_registry.py:403` | confirmed | executed on a planted file |
| 🟢 | the `## Removes` arm reads a section with no `Removes from` row, refuses a doubled row, reports a standing dotted name, and ignores a heading and a row inside a fence | `skills/evidence-check/scripts/evidence_check.py:6032` | confirmed | executed, eight planted cases |
| 🟢 | no agent or skill still instructs the retired removal table, and `Corrected · R5` matches 0.8.0's R5 | `agents/smith.md:181` | confirmed | read across agents, skills, templates and docs |
| 🟢 | the divergence table's K1 count, S9 exit code and one-line grammar each stand on their grounds | `seal/specs/1791384152-a-reader-declares-its-input-class/overview.md:26` | confirmed | the K1 count executed; the other two read against spec S1 and the grammar section |

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

## Paste-ready fixes

### 🟡 1

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

### 🟡 2

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

### 🟡 3

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

Needs a fix: yes — 🟡 1 (K1 rows the receiver rule hides), 🟡 2 (a `## Removes`
path that escapes or will not read passes as gone), 🟡 3 (K7's false note, the
re-stamped anchors that miss `cutoff_row`, and the changelog's upgrade note)

Loses a record or crashes: no

## Proof block

Files opened at `03784ec3` in the review clone, or read through `git show`
and `git diff` against `c38f97d7`:

- `tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py`,
  `tests/undeclared_readers.txt` (and its cut at `33d0b0ca`)
- `skills/evidence-check/scripts/evidence_check.py` (the diff; `py_spans`,
  `parsed_spans`, `resolve_unit`, `place`, `read`, `exit_code`, the records
  counting in `main`, `coordinate_misses`, `heading_path`)
- `docs/the-reader-registry.md`, `templates/config.md`, `templates/sdd-spec.md`,
  `templates/sdd-phase.md`, `seal/config.md`
- the diffs of `agents/framer.md`, `agents/smith.md`, `docs/the-agent-set.md`,
  `docs/the-record-layout.md`, `skills/implement/SKILL.md`, `CONTRIBUTING.md`,
  `tests/conftest.py`, `skills/verify/scripts/pytest_record/specseal_pytest_record.py`,
  `tests/test_a_record_states_what_the_tree_has.py`,
  `tests/test_a_released_row_is_read_again_in_a_fragment.py`,
  `tests/test_a_shrunken_corpus_declines_to_judge.py`,
  `tests/test_a_phase_hands_the_next_one_a_record.py`
- `skills/code-review/scripts/survivor_check.py` (lines 136–150 and 905–935)
- `seal/ledger/1791384152-a-reader-declares-its-input-class.md`, and the
  re-stamped rows of the fragments 1791384154, 1791384156, 1791384158 and
  1791384159
- `seal/releases/0.8.0.md` R5 and R4, `seal/releases/0.7.0.md` P2, P3 and P5,
  `seal/releases/0.5.0.md` S8, and the released rows fragment 1791384154
  re-reads
- `seal/specs/1791384152-a-reader-declares-its-input-class/`: `overview.md`,
  `survivors.md`, `handoff.md`, `changelog.md`, `spec.md` (outline, the
  limits, what it removes, the scenarios, its own `## Removes`)
- `bin/test`, `.github/workflows/test.yml` (the Python matrix)
