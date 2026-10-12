# Round 2 report — a reader declares its input class (#835)

This is the verifying round for round 1's fixes. I reviewed the fix range
`8f3d912e..f21f151f` at the target `9159ae93`, in a `git clone --no-local` of
the worktree, against `origin/release/v0.21.0` at `c38f97d7`. Coordinates were
carried from `round-1.md`, `round-1-report.md` and `round-1-fixes.md`. Every
verdict below is my own. The fix report's claims were read in full and checked
against the code or a probe. The one fact the orchestrator executed,
`round_record.py close` exit 0 at the target, was not re-run.

## How the findings relate

```
asked 1  🟡 1's fix, K1 by name on every receiver ...... closed; one declaration moved, 632 / 621 / 620 hold
                                                            ⬜ 3  the ledger's R7 row still says the old rule
                                                            ⬜ 6  a test docstring miscounts its new rows
asked 2  🟡 2's fix, the Removes arm's two refusals .... closed; symlink, dangling link, case asserts the text
                                                            🟡 1  a row read through --default-repo or --map
                                                            ⬜ 2  `..` through a missing directory reads as gone
                                                            ⬜ 4  the document lists three refusals, not five
asked 3  🟡 3's fix, K7, three anchors, the changelog .. closed; hashes current, no released row carries it
                                                            ⬜ 5  "as it already stopped --reverify" is half true
asked 4  ⬜ 4's fix, ⬜ 5 and ⬜ 6's answers .............. closed; both answers stand on their grounds
asked 5  depth .......................................... nothing found inside the depth-1 case
```

🟡 1 and ⬜ 2 come from one fact. The fix decides "gone" by asking whether the
joined path exists, but the path it joins comes from `place`, which can send a
row to another checkout or resolve it differently from the kernel. Round 1
closed the two cases it named. These are the two other ways the same line can
still reach a false answer.

## What each asked item came to

**1. Matching a method by its name on every receiver over-selects one
declaration, and that one is still true.** Executed. I ran K1 three ways over
every unit: the target's rule, the build's receiver rule with the base table
(from `8f3d912e`), and the framed reading (name on every receiver, base
table).

- At `2fc65bea`: 632 units, 620 with the receiver rule, 621 framed. These are
  the three numbers in `docs/the-reader-registry.md:162` and `overview.md:26`,
  and all three hold.
- At the target: 641, 627 and 630.
- The target's rule selects 14 units the build's rule did not. Twelve are
  undeclared census units (`shlex.shlex`, `re.split`, `os.path.islink` and
  `arm_check.py#_refuse_unknown`'s `.walk`). K1 picks nobody to declare, so
  nothing changes for those twelve.
- The other two are `tests/reader_registry.py#bindings` and
  `tests/reader_registry.py#k1_calls`, both calling `ast.walk`. `k1_calls`
  already declared `observed`. `bindings` is the one declaration the fix moved,
  from `nothing` to `observed`.

Is `bindings` truly a reader? Its input is an AST its caller parsed. The
document's class table admits two readings of that: `nothing` says *no input
except what a declaring caller handed it*, and `observed` lists *an AST*.
`observed` is therefore a true word, and the spec's framed reading, *matching
a method by its attribute name on every receiver*, is the one that requires
it. The price is that `top_units`, which walks the same kind of AST with
`ast.iter_child_nodes`, stays `nothing`. So the class word follows which
helper a unit calls rather than what it reads. That is the refusing direction
the document chose, and the code comment names it. No `nothing` unit at the
target calls a K1 primitive, and the module test passes (76 passed).

The R7 row in this item's own ledger fragment still states the rule round 1
removed (⬜ 3).

**2. The two refusals hold for a symlink, and the new case pins the refusal
itself, not the crash.** Executed in a planted probe module.

- A symlink inside the root pointing out of it is `REFUSED` with the escape
  text, because `contained` resolves links.
- A dangling symlink is `REFUSED` as *there and will not read*.
- A symlink to a file inside the root holding the unit is `STANDING`.
- `pkg/../kept.py#k`, with `pkg/` present, is `STANDING`.

The fix report says the escape mutation went red through a `TypeError` from
joining a `None` repository. I ran the mutation that matters, which puts back
the build's quiet skip (`continue` before the append). It went red through
the case's `AssertionError` at
`tests/test_a_record_states_what_the_tree_has.py:1765`. Gating the unreadable
refusal off went red the same way. Widening that refusal to every path that
did not read also went red, because the case's third row, `pkg/gone.py#g`,
pins a truly absent file as no finding. The case asserts each refusal's whole
text.

Two paths still read as gone when they are not. A row placed in another
checkout is 🟡 1. A `..` through a directory that does not exist is ⬜ 2.

**3. K7 now says what the plain run does, the three rows cite `cutoff_row` at
its current hash, and no released row carries the false sentence.** Executed
and read. `unit_hash` at the target gives `cutoff_row` dc04c433,
`frozen_from` 060d5968 and `config_rule` 57d7f81f, which match K7, C1 and
1791384159's `Corrected ·` row. A `git grep` for *reads no config row* and
*not among the commands that refuse* finds nothing under `seal/releases/`. The
only live carriers are 1791384156's own `overview.md:31` and
`phases/phase-2.md:60`. Both record that item's decision as it stood then.
The changelog's upgrade note is present, and one clause of it says more than
the code does (⬜ 5).

**4. ⬜ 4 is closed, and the answers to ⬜ 5 and ⬜ 6 stand.** Read.

- ⬜ 4: the two rows `1aa26afa` added to `spec.md`'s own `## Removes` name
  tests the tree no longer has, so the arm reads both as gone.
- ⬜ 5: `records_a_past_state` excludes everything under `phases/` whatever a
  record holds, so its description of what a phase record contains decides
  nothing. It is also true of every record written before #835.
- ⬜ 6: `write_census` refuses wherever the census exists. The census is
  deleted only once it lists nothing, and writing it again then is the one act
  the census forbids. The latent line would be refused loudly, by the test
  that reads it.

**5. Nothing was found inside the depth-1 unit.**
`test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone` asserts
each refusal's whole text, and the mutations above show it red for each arm.

## Findings

### 🟡 1 · A frame's removal is read in the original repository, and a row in a checkout that is not there reads as gone

`skills/evidence-check/scripts/evidence_check.py:6131`. `removal_findings`
places each row through `place(root, maps, default_repo, raw_path)`, which is
the ledger's resolver. For the ledger that is right, because a migration
ledger cites the original repository without a prefix. A `## Removes` row is
a different claim. Spec S1 and S2 say it names something gone *at HEAD*,
meaning from this tree.

Executed, both through `check_records` with the arguments `main` passes:

- With `--default-repo` naming a checkout that holds `old.py` defining `k`,
  and `old.py` absent from this tree, the row `old.py#k` reads `STANDING`. The
  removal happened, and the arm says it did not.
- With `--map legacy=<a path not on disk>`, the row `legacy/a.py#k` gives no
  finding. Nobody can say whether `a.py` is gone, and the arm says it is.

Why it matters:

- `main`'s own comment says a migration repository's CI passes
  `--default-repo` on every run, and a migration that keeps the original's
  layout removes files at paths the original still has. Each such honest row
  then stops CI at exit 2. The only way out is deleting a true row.
- The `--map` half is the quiet direction that round 1's 🟡 2 closed for the
  escape. Only a file genuinely absent from this tree is a removal that
  happened.

The fix reads every row in this tree and refuses a row that names another
checkout.

### ⬜ 2 · A `..` through a directory that does not exist reads as gone while the file it names holds the unit

`skills/evidence-check/scripts/evidence_check.py:6142`. `contained` judges
`nope/../kept.py` by `realpath`, which drops the missing `nope`, so the row is
inside the root. `read` then asks the kernel, which needs `nope` to exist, so
the read fails. Because `os.path.lexists` asks the kernel too, the row is
no finding. Executed: `nope/../kept.py#k` and `kept.py/../kept.py#k` both
gave no finding, with `kept.py` defining `k`. Nobody writes such a row on
purpose, so this is the edge of the check rather than a defect a frame will
meet. Refusing any `..` segment in a `## Removes` path would close it.

### ⬜ 3 · The ledger's R7 row still says `ast.walk` is no primitive

`seal/ledger/1791384152-a-reader-declares-its-input-class.md:25`. The claim
says *`str.split`, a repository's own `load` and `ast.walk` are not
primitives*. Its verified-behaviour cell cites a mutation of *the
module-receiver set*. Since `e6843d9a`, `ast.walk` is refused beside a
`nothing` (it moved from
`test_a_call_k1_does_not_name_leaves_nothing_standing` to
`test_nothing_beside_a_k1_primitive_is_refused_naming_the_call`), and the set
is gone. The cited cases still exist, so no checker sees the row go false. It
folds into the release as written. A correction under `seal/ledger/`.

### ⬜ 4 · The document and the changelog list three refusals, and the fix added two

`docs/the-reader-registry.md:119` lists what the arm refuses as *a cell that
is no coordinate, a test's node id, a bare symbol in a file no parser
bounds*. The `Enforced by:` line under it (`:127`) does not name the new
case. The changelog's *Added* bullet (`changelog.md:24`) gives the same three.
Spec S5 and the ledger's S3/S5 row also stop at those three, and both stay
true as written. The general clause, *a cell the ledger would refuse is
`REFUSED`*, covers the escape and the unreadable path, so nothing stated is
false. But an installer reading either list learns about three of the five
exit-2 refusals.

### ⬜ 5 · The upgrade note says `--reverify` already stopped on a doubled `Removes from`

`seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46`.
*A `seal/config.md` that is there and will not read, or that writes `Removes
from` twice, now stops a plain `evidence-check` run … as it already stopped
`--reverify`.* The unreadable file did already stop `--reverify`. The doubled
`Removes from` row did not, and still does not, because `--reverify` returns
before `check_records`, the only caller of `cutoff_row` for that row. Read, at
`evidence_check.py:6626` onward. A correction under `seal/specs/`.

### ⬜ 6 · A test docstring says its last two rows are round 1's, and they are the next two

`tests/test_a_reader_declares_its_input_class.py:493`. The fix added four rows.
The ones that answer round 1's 🟡 1 are `os.open` and `re.split`. The last two
are `ast.walk` and `pathlib.Path.read_text`, and `pathlib` is no module K1's
table names. The docstring's reason fits `ast.walk` alone.

## Regression tests to plant

- `tests/test_a_record_states_what_the_tree_has.py`: one case reading a row
  through `--default-repo` and one through a `--map` prefix whose checkout is
  absent (🟡 1). Seen red by construction: the probe above gave `STANDING`
  and no finding for exactly these two rows at the target.

## Facts for the evidence ledger

- At `2fc65bea` K1 selects 632 units under the target's rule, 620 under the
  build's receiver rule and 621 under the framed reading. At `9159ae93` the
  same three readings give 641, 627 and 630.
- At `9159ae93` `cutoff_row` hashes to dc04c433, `frozen_from` to 060d5968,
  `config_rule` to 57d7f81f, and the heading D1 cites to 18207f51.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | a `## Removes` row is placed through `--default-repo` and `--map`: a removal from this tree reads `STANDING` when the original holds the path, and a mapped row whose checkout is absent reads as gone | `skills/evidence-check/scripts/evidence_check.py:6131` | open | executed through `check_records`: `STANDING` for the default-repo row, no finding for the mapped row; spec S1/S2 read at HEAD |
| ⬜ 2 | a `..` through a missing directory, or through a file, reads as gone while the file it names holds the unit | `skills/evidence-check/scripts/evidence_check.py:6142` | open | executed: two rows, no finding, `kept.py` defining the unit; `contained` resolves by `realpath`, the read by the kernel |
| ⬜ 3 | the R7 row says `ast.walk` is no primitive and cites a mutation of the receiver set the fix removed | `seal/ledger/1791384152-a-reader-declares-its-input-class.md:25` | open | read against `tests/reader_registry.py:198` and the moved test row; a correction under `seal/ledger/` |
| ⬜ 4 | the document's and the changelog's lists of `## Removes` refusals stop at three, and the `Enforced by:` line does not name the new case | `docs/the-reader-registry.md:119` | open | read; the general clause stays true |
| ⬜ 5 | the upgrade note says `--reverify` already stopped on a doubled `Removes from` | `seal/specs/1791384152-a-reader-declares-its-input-class/changelog.md:46` | open | read: `--reverify` returns before `check_records`; a correction under `seal/specs/` |
| ⬜ 6 | a test docstring calls its last two rows round 1's, and those are `ast.walk` and `pathlib` | `tests/test_a_reader_declares_its_input_class.py:493` | open | read |
| 🟢 | round 1's first finding is closed — K1 judges a module's method by its name, `os.open` and `re.split` are refused, one declaration moved and it is true | `tests/reader_registry.py:198` | confirmed | executed: three readings over every unit at both trees; module test 76 passed |
| 🟢 | round 1's second finding is closed — an escaping path, a symlink out, a directory and a dangling link are `REFUSED`, and the case pins each text | `skills/evidence-check/scripts/evidence_check.py:6132` | confirmed | executed: planted probes; three `mutation-check` runs red through the case's assertion |
| 🟢 | round 1's third finding is closed — K7's note, the three `cutoff_row` anchors and the changelog's note | `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md:24` | confirmed | executed: hashes recomputed at the target; read: no released row carries the sentence |
| 🟢 | round 1's fourth note is closed — the item's `## Removes` names both pins | `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md:513` | confirmed | read: neither test is in the tree, so both rows read as gone |
| 🟢 | round 1's fifth note's answer stands | `skills/code-review/scripts/survivor_check.py:142` | confirmed | read: the predicate excludes `phases/` whatever a record holds |
| 🟢 | round 1's sixth note's answer stands | `tests/reader_registry.py:461` | confirmed | read: the writer runs only where no census exists, and the bad line is refused loudly |

## Executed probes

| What was run | Result |
|---|---|
| K1 three ways — the target's rule, the build's receiver rule with the base table, the framed reading — over every unit at `9159ae93` and at `2fc65bea` | executed: 641 / 627 / 630 at the target; 632 / 620 / 621 at `2fc65bea`; 14 units newly selected at the target, 12 on the census, plus `bindings` and `k1_calls`; no `nothing` unit beside a K1 call |
| planted `## Removes` rows through `check_records`: symlink out, symlink in, dangling symlink, `..` three ways, `--map` to an absent and to a present checkout, `--default-repo` | executed: `REFUSED`, `STANDING`, `REFUSED`; `pkg/../` `STANDING` and the other two no finding; no finding and `STANDING`; `STANDING` |
| `bin/mutation-check` on `removal_findings`: the quiet skip put back, the unreadable refusal gated off, the unreadable refusal widened | executed: all three red through the case's `AssertionError`, file restored |
| `unit_hash` of `cutoff_row`, `frozen_from`, `config_rule`, and the D1 heading's hash | executed: dc04c433, 060d5968, 57d7f81f, 18207f51, each matching its row |
| `bin/test tests/test_a_reader_declares_its_input_class.py` | executed: 76 passed, exit 0 |
| `bin/test tests/test_a_record_states_what_the_tree_has.py`, narrowed with `-k` to the `## Removes`, cutoff and coordinate cases | executed: 35 passed, exit 0 |
| `round_record.py close` at `9159ae93` | not run in this round; the orchestrator's executed fact, exit 0 |
| the broad gate (full suite, lint, typecheck) | not yet; the sealer's, after the rounds settle |

## Paste-ready fixes

### 🟡 1

```python
# skills/evidence-check/scripts/evidence_check.py — removal_findings, in place
# of `repo, rel = place(root, maps, default_repo, raw_path)`. A frame names
# what its work removes from THIS tree, so a row is never read in the
# original, and a row carrying a --map prefix names another checkout.
        if any(raw_path == name or raw_path.startswith(name + "/") for name in maps):
            findings.append(
                (
                    REFUSED_STATUS,
                    where,
                    f"`{cell}` — the path names another checkout through "
                    "`--map`, and a frame names what its work removes from "
                    "this tree — write the path in this tree",
                )
            )
            continue
        repo, rel = place(root, {}, None, raw_path)
```

```python
# tests/test_a_record_states_what_the_tree_has.py
def test_a_removal_is_read_in_this_tree_never_in_another_checkout(tmp_path):
    """S1/S2, round 2 of #835. A row is a claim about HEAD: one the original
    still holds is a removal that happened here, and one in a mapped checkout
    is refused rather than read as gone."""
    root = tmp_path / "r"
    tree(root, **{"kept.py": "def k():\n    return 1\n"})
    orig = tmp_path / "orig"
    tree(orig, **{"old.py": "def k():\n    return 1\n"})
    h = home(root)
    rows = "| x | `old.py#k` | y |\n| x | `legacy/a.py#k` | y |\n"
    work_item(h, "1780000000-live", **{"spec.md": REMOVES_HEAD + rows + REMOVES_TAIL})
    found, _read, _stamps = module().check_records(
        str(root), str(root / "seal"), {"legacy": str(tmp_path / "absent")}, str(orig)
    )
    assert [(s, d) for s, _c, d in found] == [
        (
            "REFUSED",
            "`legacy/a.py#k` — the path names another checkout through `--map`, "
            "and a frame names what its work removes from this tree — write the "
            "path in this tree",
        )
    ]
```

Needs a fix: yes — 🟡 1 (a `## Removes` row is read through `--default-repo`
and `--map`, so a removal that happened reads `STANDING` and a row in an
absent checkout reads as gone)

Loses a record or crashes: no

## Proof block

Opened at `9159ae93` in the review clone, or read through `git show` and
`git diff` over `8f3d912e..f21f151f`:

- `seal/specs/1791384152-a-reader-declares-its-input-class/rounds/round-1.md`,
  `round-1-report.md`, `round-1-fixes.md`; `changelog.md`, `overview.md:26`,
  `spec.md` (the `## Removes` prose at 355–385, scenarios S1–S9, its own
  section at 508), `questions.md:76`
- `tests/reader_registry.py` (lines 40–530), and its base at `8f3d912e`
- `tests/test_a_reader_declares_its_input_class.py` (lines 440–600)
- `tests/test_a_record_states_what_the_tree_has.py` (helpers at 22–60 and
  180–195, the `## Removes` helpers, the new case at 1749–1776)
- `skills/evidence-check/scripts/evidence_check.py`: `read`, `contained`,
  `place`, the ledger row grading at 1760–1830, `removal_findings`,
  `check_records` (6275–6330), the call site at 6200–6215, `main`'s
  `--reverify` returns and its `check_records` call
- `docs/the-reader-registry.md`, `docs/review-chain-spec.md` §*The last round
  verifies*
- `seal/ledger/1791384152-a-reader-declares-its-input-class.md`, the K7 and
  C1 rows of `seal/ledger/1791384156-config-rows-coordinates-and-headings-have-one-reader.md`,
  line 13 of `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md`
- `skills/code-review/scripts/survivor_check.py` (136–150, 910–925)
- `bin/test`, `bin/mutation-check`, `.github/scripts/run_tests.py`
