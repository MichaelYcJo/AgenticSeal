# Review round 1: 1793922920-the-windows-leg-finds-path-defects-last

```seal
target: 4e8b9418 against release/v0.32.6
```

The range is `063e0678..4e8b9418`. Round 1 has no earlier record, so no fact
here is carried from one; each was established this round. The frame was
read at `4e8b9418`: `frame/design.md`, `frame/plan.md` and
`frame/questions.md` as revised at `225448dc` and folded at `4e8b9418`.

## Findings

### 1. Four joins of `routing.ROUNDS_DIR` still carry `trail/rounds` into `os.path.join`, and the frame's list of cross-module sites missed them

```seal
severity: should
location: `hooks/lib/routing.py:578`, `hooks/lib/routing.py:605`, `.github/scripts/release_seal.py:357`, `.github/scripts/finding_counts.py:143`, `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/design.md:14`, `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/design.md:35`, `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/changelog.md:4`, `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/gaps.md:7`
evidence: executed `bin/test test_tmp_slash_probe2.py -q -s -p no:xdist -p no:cacheprovider` in the clone (Probes row 2); read `hooks/lib/optin.py:48`, `hooks/lib/optin.py:53`, `hooks/lib/routing.py:507-508`, `hooks/lib/routing.py:548-550`, `.github/scripts/release_seal.py:383-391`
```

Why it matters: `frame/design.md` *Scope* item 3 takes on, by hand, every
site that joins another module's constant holding `/`, "though the census
cannot see them". It names two, on the ground of *Grounding* row 14 (`:14`):
"Two carry `/` from another module". That count is wrong at `4e8b9418`.
`hooks/lib/optin.py:53` is `ROUNDS = f"{TRAIL}/rounds"`, which is
`trail/rounds`, and `hooks/lib/routing.py:508` is `ROUNDS_DIR = optin.ROUNDS`.
Four calls join it whole:

- `hooks/lib/routing.py:578`, `_ordered(os.path.join(item, ROUNDS_DIR))`.
  `_ordered` (`:548-550`) joins each record name onto it, so on Windows
  every path `routing.rounds` returns is `<item>\trail/rounds\round-N.md`.
  That is the mixed spelling the 1051 failure compared as a string.
- `hooks/lib/routing.py:605`, the `where` of `rounds_unreadable`.
- `.github/scripts/release_seal.py:357` appends the joined path to `unread`,
  and `:391` prints it to a person through `os.path.relpath`, mixed on
  Windows.
- `.github/scripts/finding_counts.py:143`. Its output goes through `rel()`,
  which turns `os.sep` into `/`, so nothing printed differs. The join still
  holds a `/` the house rule this work adds says it may not.

The frame's sweep matched each attribute against `^<NAME> = ` assignments
of string literals, so a constant built by an f-string or bound to another
module's constant fell outside it. The phase record names that limit
("A constant built by an expression ... the list is a sample"), but it
opens with "The cross-module class lists nothing at HEAD after the two hand
repairs". Contract rule 12 asks for a list a method makes whole where the
class is closed. The tracked `.py` files are a closed set, and a parser
resolves an f-string of module constants and a one-step alias. The probe
did that over all 222 tracked files. It found these four calls and no other
join of such a constant from another module. Its other matches were
same-name constants in their own files that hold no `/`. Those are `CONFIG`,
`INDEX`, `ITEM`, the `GATE` of `tests/hooks/test_question_gate.py:40` and
`tests/hooks/test_routing_edit_gate.py:40`, and the `ROUNDS_DIR` that
`skills/verify/scripts/broad_gate.py:172` builds natively.

The paste-ready fix keeps `ROUNDS_DIR` spelt with `/`, because
`skills/code-review/scripts/chain_check.py:495` and `:1426` build git paths
from it. It splits the constant at each of the four joins. The precondition:
`item` and `where` are native paths, as `routing.item_dir` returns them. On
POSIX every path is unchanged. On Windows `routing.rounds` then returns
paths spelt with `\` throughout. Every hook and script that reads round
records consumes those paths, so the fix pass owes a dispatched `tests` run
with the Windows legs, as `skills/code-review/orchestration.md` *Where the
work's risk is platform-specific* says.

```python
# hooks/lib/routing.py:578
        return _ordered(os.path.join(item, *ROUNDS_DIR.split("/")))

# hooks/lib/routing.py:605
    where = os.path.join(item, *ROUNDS_DIR.split("/"))

# .github/scripts/release_seal.py:357
            unread.append(os.path.join(item, *routing.ROUNDS_DIR.split("/")))

# .github/scripts/finding_counts.py:143
        listed = os.path.join(where, *routing.ROUNDS_DIR.split("/"))
```

This snippet does not reach the other statements of the fact. The fix pass
owes those too:

- `frame/design.md:14` ("Two carry `/` from another module"), `:35` ("The
  two sites") and `:68`, the shipped sites that *Data & interfaces* lists.
- `changelog.md:4`, "Four scripts the plugin ships", whose list then gains
  `hooks/lib/routing.py`'s reader of a work item's round records and
  `.github/scripts/release_seal.py`.
- The `## Not verified` row of `gaps.md:7`, whose list of rewritten joins
  then gains the same two files.

### 2. The changelog says nine test sites are joined part by part, and two of them are not

```seal
severity: should
location: `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/changelog.md:4`, `tests/skills/test_seal_stamp.py:1032-1042`
evidence: read `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/changelog.md:4`, `tests/skills/test_seal_stamp.py:1032-1042`, `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/trail/phases/phase-1.md`
```

Why it matters: the *Changed* entry ends "Nine test sites the census flagged
are joined the same way". Seven are: `TARGET` in four modules, `ITEM`,
`CONTRACT` and `CORE`, each now `*NAME.split("/")`. The other two are the
`"/c"` fixture roots of `tests/skills/test_seal_stamp.py#Test_values_dir`.
`:1033` and `:1039` replace them with `str(tmp_path)` and join nothing
differently. The phase record says so itself ("No exemption was written.
The two `"/c"` sites ... take `str(tmp_path)` as the common directory
instead"). The release notes are built from this fragment, so a reader of
v0.32.6 is told a repair that two of the nine sites did not receive.

```markdown
Seven test sites the census flagged are joined the same way, and the two `"/c"` fixture roots in `tests/skills/test_seal_stamp.py` take the case's temporary directory instead.
```

Where the fix pass also applies finding 1, the same entry's first sentence
changes count, which finding 1 lists.

### 3. A chained module-level assignment of a path passes the census, though *Scope* item 1 covers it

```seal
severity: should
location: `tests/censuses.py:1357`, `tests/censuses.py:1351-1353`, `tests/test_censuses.py:1120`
evidence: executed `bin/test test_tmp_slash_probe.py -q -s -p no:xdist -p no:cacheprovider` in the clone (Probes row 1, sample `multi-target`); read `tests/censuses.py:1351-1370`
```

Why it matters: *Scope* item 1 flags "a bare name the file binds exactly
once at module level, by an assignment of a string constant holding `/`".
The census comment (`tests/censuses.py:1327-1334`) says the same. `GATE =
OTHER = "trail/gate.md"` binds `GATE` once, by such an assignment. But
`_constants` reads an `ast.Assign` only where `len(node.targets) == 1`
(`:1357`), so the probe's `A = B = "a/b"` followed by `os.path.join(r, A)`
returned no line. The comment lists what the walk cannot see, and this shape
is not on that list. A contributor reading the comment takes the walk for
wider than it is, and the phase record says the comment was written to
prevent exactly that. The domain of assignment shapes is open: a tuple
target and a walrus are others. Reading every name target of one assignment
closes the shape the frame names. The rest stays under "any expression that
is not one of the three".

```python
def _constants(tree):
    """`{name: text}` for each name TREE binds once, by a module-level
    assignment of a string, `NAME = "<text>"`, `NAME = OTHER = "<text>"` or
    `NAME: str = "<text>"`."""
    counts = collections.Counter(_bound_names(tree))
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets, value = node.targets, node.value
        elif isinstance(node, ast.AnnAssign):
            targets, value = [node.target], node.value
        else:
            continue
        for target in targets:
            if (
                isinstance(target, ast.Name)
                and isinstance(value, ast.Constant)
                and isinstance(value.value, str)
                and counts[target.id] == 1
            ):
                found[target.id] = value.value
    return found
```

It needs a refusing case in `Test_slash_in_join`, shown red against the
`len(node.targets) == 1` it removes:

```python
    def test_refuses_a_constant_a_chained_assignment_binds(self, tmp_path):
        source = 'import os\nGATE = OTHER = "a/b"\nos.path.join(r, GATE)\n'
        root = plant(tmp_path, "tests/x.py", source)
        assert censuses.slash_in_join("tests/x.py", root) == [
            "tests/x.py:3: slash_in_join: "
            + slashed('`GATE` (`"a/b"`)', 'pass `*GATE.split("/")`')
        ]
```

### 4. Three binding kinds the census reads hold no case, and the suite stays green with all three removed

```seal
severity: should
location: `tests/censuses.py:1345-1348`, `tests/censuses.py:1359-1360`, `tests/test_censuses.py:1100-1117`
evidence: executed `bin/test tests/test_censuses.py -q -p no:randomly` in the clone with `ast.alias`, the `name` attribute branch of `_bound_names` and the `ast.AnnAssign` branch of `_constants` each made `False and ...` through the Edit tool, 211 passed, exit 0, then reverted (Probes row 3); read `tests/test_censuses.py:1094-1170`
```

Why it matters: the diff adds these guards, and each holds a fact *Scope*
item 1 states. A name "the file binds exactly once" excludes a constant
also bound by an import or by a definition, which is what
`_bound_names`'s `ast.alias` branch and its `name` attribute branch count
(`:1345-1348`). An "assignment of a string constant" includes the
annotated one `_constants` reads at `:1359-1360`. The phase record's eleven
mutations reach the `Name`-store and `arg` kinds (mutations 6 and 7), and
none of these three. With all three off, all 211 cases of
`tests/test_censuses.py` passed. That suite includes the
`Test_module::test_every_file_no_module_file_declares_meets_every_census`
run over the tree. Probes row 1 shows what the guards do today: an import
or a definition that rebinds the name makes the census pass the join, and
`GATE: str = "a/b"` is flagged. No case holds either behaviour. This is
the *Regression test* row's `should` of `skills/code-review/SKILL.md`
*Probes and regression tests*. The cases below go in
`tests/test_censuses.py`. Each is shown red with only its own branch
removed, as contract rule 15 asks. The `except` name shares the `name`
attribute branch with the definition, so one case holds both.

```python
# in NO_SLASH_JOINED
    "a-constant-an-import-rebinds": (
        'import os\nfrom m import GATE\nGATE = "a/b"\nos.path.join(r, GATE)\n'
    ),
    "a-constant-a-definition-rebinds": (
        'import os\nGATE = "a/b"\n\n\ndef GATE():\n    pass\n\n\nos.path.join(r, GATE)\n'
    ),

# in Test_slash_in_join
    def test_refuses_an_annotated_module_constant(self, tmp_path):
        source = 'import os\nGATE: str = "a/b"\nos.path.join(r, GATE)\n'
        root = plant(tmp_path, "tests/x.py", source)
        assert censuses.slash_in_join("tests/x.py", root) == [
            "tests/x.py:3: slash_in_join: "
            + slashed('`GATE` (`"a/b"`)', 'pass `*GATE.split("/")`')
        ]
```

Where the fix pass applies finding 3, its rewrite keeps the `AnnAssign`
branch, and this case holds the rewritten branch.

## Confirmations

What matched: the census reads no line at `4e8b9418`. The probe ran
`slash_in_join` over the 222 files `git ls-files '*.py'` lists. It listed
nothing and walked 1063 `os.path.join` calls, the counts *Grounding* row 13
gives (executed, Probes row 1). `bin/test tests/test_censuses.py` gave 211
passed, exit 0, `Test_module` and every `Test_slash_in_join` case among
them (executed, Probes row 4). This satisfies S6's first half.

What matched: the eleven sites *Grounding* row 13 lists are the eleven the
diff rewrites. Those are `DESIGN`, `SUITE`, four `TARGET`s, `ITEM`,
`CONTRACT`, `CORE` and the two `"/c"` roots, and each line now joins its
parts or no longer joins a `/` (read, the diff of `063e0678..4e8b9418`). The
two cross-module repairs stand at `skills/verify/scripts/seal_stamp.py:1417`
and `.github/scripts/finding_counts.py:200`. Each is the
`*NAME.split("/")` form `skills/verify/scripts/broad_gate.py:2523` set, and
each returns the same path on POSIX (read). The claim that the census over
the base listed all eleven was read against the diff and not re-run. Probes
row 5 says why.

What matched: `tests/censuses.py:1312-1416` builds what *Scope* item 1 and
*Data & interfaces* ask. It is `slash_in_join(rel, root=None)`, read through
`_python` with no `under`, and resolved by `bindings` and `dotted`. It
flags the call's own line and returns `_held("slash_in_join", ...)`, and it
is added to `CENSUSES` at `:1429`. The comment cites run 40500883542 and
lists the limits the frame names, plus the function-body limit the phase
record adds. `from os import path` followed by `path.join(r, "a/b")` is
flagged too (executed, Probes row 1). That spelling holds no case. It rests
on `bindings`, which the diff does not change, so it opens no finding.

What matched: S5 rests on `Test_judge`'s exemption cases
(`tests/test_censuses.py:78-131`). Those hold `_held` for every census by
the name each one passes. S1's exact line pins the name `slash_in_join`
that the census passes (`tests/test_censuses.py:1121-1128`). The plan's
*Verified by* cell, as folded at `4e8b9418`, says this, and `frame/design.md`
S5 allows it (read). No exemption comment was written. `git grep -n
"exempt from slash_in_join"` lists only the message strings at
`tests/censuses.py:1413` and `tests/test_censuses.py:1087` and the frame's
own lines (executed). `_exempted` reads comment lines only, so those
strings excuse nothing.

What matched: the two `"/c"` fixtures were replaced by `str(tmp_path)` at
`tests/skills/test_seal_stamp.py:1033` and `:1039`. Each case still asserts
what it asserted before. `values_dir` is a plain join of the common
directory, `VALUES_DIR` and the session key
(`skills/verify/scripts/seal_stamp.py:879-881`), so the root's spelling was
never the fact under test (read). The removed `.replace("/", os.sep)` at
`tests/skills/test_broad_gate.py:54` changes nothing on either platform
once `ITEM` is split, and the comment above it still holds (read). The
phase record's grounds for both departures hold.

What matched: `CONTRIBUTING.md:431-439` is one *House rules* bullet beside
the encoding one. It states that a path is joined one part at a time and
why only the Windows leg shows a `/` inside a join. It names the
`slash_in_join` census in `tests/censuses.py` over every tracked `.py`, and
it names the cross-module limit. That meets S7 and *Scope* item 4 (read).

What matched: `routing.md`'s grounds and the plan's *Verified by* cell, as
the orchestrator folded them at `4e8b9418`, state what phase 1 built: a
census and no checklist question, and S5 through `Test_judge` (read). The
revision at `225448dc` moved the three link cases to #1247's work item.
This diff does not touch `tests/skills/test_agentic_pytest_record.py`
(read, the diff stat).

What matched: the dispatched run 42137403140 at `4e8b9418` completed with
conclusion `success`. Each of its four `windows-latest` pytest jobs, its
three `macos-latest` jobs, its two `ubuntu-latest` jobs and `lint` passed,
and `release-report` was skipped (executed, Probes row 6). That run answers
the `gaps.md` row "The rewritten joins on Windows" for the thirteen sites
built. Closing the row is the orchestrator's act. Finding 1's fix, if
applied, needs a run of its own.

A gap that holds no finding: the census flags a bare root literal, as in
`os.path.join("/", "etc")`, and its message tells the writer to "pass each
part as its own argument", which no part can do for a root. On Windows that
join gives `/etc`, with no mixed separator (executed, Probes row 1, sample
`leading-root`). No tracked file holds the shape, and the exemption form
serves it. The coordinate is `tests/censuses.py:1376-1381`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `frame/questions.md` Q2, whether every work item routed to a pull request runs the other platforms before the broad run. It is a person's row, open, with its default (keep the stated limit) kept under `Automation` `yes` | `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/questions.md:16` | the repository owner |
| The broad gate at HEAD: the full suite, the lint and the typecheck. This round ran `tests/test_censuses.py` narrowly and three probes, and labels the suite `unverified` | `seal/config.md` | the orchestrator, by its broad run, and the sealer after it |
| Finding 1's fix on Windows: `routing.rounds` returning paths spelt with `\` throughout, read by every hook and script that consumes round records | `hooks/lib/routing.py:578` | the orchestrator, by a dispatched `tests` run after the fix pass |
| What issue #103 says of run 33715420379 and of the earlier repository's #81 and #96, which the frame did not open and this round did not open | `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/design.md:12` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test test_tmp_slash_probe.py -q -s -p no:xdist -p no:cacheprovider`, a probe in the clone that ran `slash_in_join` over every tracked `.py`, matched each `os.path.join` argument against every module-level and class-level string literal holding `/` in any tracked file, read function-local constants, and ran the census over six sample sources | exit 0. 222 files, 1063 calls, no census line. No attribute argument matched a literal constant in another module. No function-local constant holding `/` was joined. Samples: `GATE: str = "a/b"` flagged; `from os import path` flagged; `A = B = "a/b"` passed; a constant also bound by `from m import GATE` passed; one also bound by `def GATE()` passed; `os.path.join("/", "etc")` flagged |
| `bin/test test_tmp_slash_probe2.py -q -s -p no:xdist -p no:cacheprovider`, a probe in the clone that collected module-level constants holding `/` by a literal or an f-string, followed one-step aliases to them, and matched each `os.path.join` argument the census passes | exit 0. Matches by name, each opened at its definition: `routing.ROUNDS_DIR` at `.github/scripts/finding_counts.py:143` and `.github/scripts/release_seal.py:357`, and `ROUNDS_DIR` at `hooks/lib/routing.py:578` and `:605`, all `optin.ROUNDS`, which is `trail/rounds`. Every other match was a same-name constant in its own file holding no `/` |
| `bin/test tests/test_censuses.py -q -p no:randomly`, with `tests/censuses.py:1345`, `:1347` and `:1359` each prefixed `False and` through the Edit tool | exit 0, 211 passed. All three edits were reverted through the Edit tool, and `git diff --quiet` gave exit 0 afterwards |
| `bin/test tests/test_censuses.py -q -p no:randomly` at `4e8b9418` | exit 0, 211 passed |
| `bin/test test_tmp_base_census.py -q -s -p no:xdist -p no:cacheprovider`, a probe meant to run the census over an archive of `063e0678` | exit 1, `FileNotFoundError` on `evals/scripts/behaviour.py`, because `git archive` left out files `git ls-tree` listed. It settled nothing and was not run again |
| `gh run view 42137403140 --json status,conclusion,jobs` | `status` `completed`, `conclusion` `success`, head `4e8b9418`. Every pytest job and `lint` passed, and `release-report` was skipped |

Each probe file, the base archive and the sample sources were removed
before hand-back. The clone is removed with them.
