# 1791384152-a-reader-declares-its-input-class — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 248c33b2 |
| Ran by | smith on Opus, as `handoff.md`'s State row records the spawn |

## What this phase was asked

The measurement, at the build's own tree. The walker as a module the test
imports (`population(root)`, `k1_calls(unit)`, `module_body_calls`), the
census writer that emits `tests/undeclared_readers.txt` from the walker, and
this record: units per root, units K1 selects, units with no docstring,
module bodies K1 selects, non-test defs inside `tests/test_*.py` and how many
K1 selects, ledger anchors on population units in the released files and the
live fragments, and which of the 39 sibling-added units are on the census.
Every number is recorded with the SHA it was read at, and a number that
differs from the frame's 4ba84e19 reading is recorded with both values. No
reader's body changes. The spawn added: each new case seen red before it is
planted, and one mutation per new unit.

## What this phase found

**Every number was read at 2fc65bea**, the branch head before phase 1's
commit, by the walker as 248c33b2 holds it. 2fc65bea differs from 4ba84e19
only in this work item's own four records (`git diff --stat 4ba84e19
2fc65bea`), so a difference below is the walker's rule, not the tree.

| Count | Frame, at 4ba84e19 | Walker, at 2fc65bea |
|---|---|---|
| tracked `.py` / of them `tests/test_*.py` | 253 / 180 | 253 / 180 |
| population units: `hooks/` · `skills/*/scripts/` · `.github/scripts/` · `tests/` outside `test_*.py` | 461 · 854 · 211 · 61 = **1,587** | 461 · 854 · 211 · 61 = **1,587** |
| units calling a K1 primitive, same roots | 162 · 344 · 94 · 21 = **621** | 162 · 343 · 94 · 21 = **620** |
| units with no docstring | 68 · 69 · 49 · 8 = **194** | 68 · 69 · 49 · 8 = **194** |
| module bodies K1 selects | 2: `tests/conftest.py` (13 `os.environ`, no module docstring), the pytest recorder (2, :139–140, docstring) | the same 2, the same 15 references at the same lines |
| non-test top-level `def`s in `tests/test_*.py` / calling K1 / top-level classes | 1,683 / 618 / 17 | 1,683 / **606** / 17 |
| whole-unit anchors on population units, released files (44) | 2,392 on 943 units | 2,392 on 943 units, and 7 more narrowed by `>` (2,399 in all) |
| whole-unit anchors, live fragments (10) | 691 on 247 units | 691 on 247 units, and 3 more narrowed (694 on 248) |
| units added / removed between 62c27416 and the build's tree | 39 / 14 | 39 / 14, the same names `plan.md` §*Seams* lists, all 39 on the census |

**The one K1 difference is `ast.walk`, and the walker is the side that is
right.** The frame's probe matched a method by its attribute name on every
receiver, so `skills/verify/scripts/arm_check.py#_refuse_unknown`, whose only
K1-shaped call is `ast.walk`, counted as a reader. The walker judges a method
by the table wherever its receiver is a module K1 itself names (`ast`, `os`,
`os.path`, `re`, `json`, …), so `ast.walk` and `os.path.join` are not `walk`
and `join`, and by its attribute name everywhere else. The same rule is the
whole of the 618 → 606 difference inside the test modules (the frame's rule
reproduces 618 on the walker's population there). The first draft of the
walker went the other way, judging every import-bound receiver by the table,
and read 616: it lost five units whose regex calls go through a sibling
module's compiled pattern (`close_issues_on_release.FENCE.sub`). The
`K1_MODULES` rule is the one that keeps both, and
`test_nothing_beside_a_k1_primitive_is_refused_naming_the_call` pins the
sibling-pattern case while `test_a_call_k1_does_not_name_leaves_nothing_standing`
pins `ast.walk`.

**The population reaches a `def` inside a module-level `if`, `try` or
`except`, and the frame's command does not.** `spec.md`'s reproducing
command reads `ast.parse(...).body`, which stops at the first compound
statement. The walker takes every `def` and `class` inside no other `def` or
`class`, which is also every key `py_spans` gives without a dot. At this tree
the two agree, because no shipped file defines a unit under a module-level
compound statement; the first walker draft descended into `ast.stmt` only and
missed an `except` handler, which `test_methods_and_nested_functions_fold_into_their_unit`
caught. A name a module defines twice is one census line hashed over every
span; none exists at this tree.

**The census only shrinks by convention, and the writer is the half that can
hold it.** No check can tell a line put back from a line that was always
there without reading history, which the registry check does not do. So
`write_census` refuses where the file exists, the test module's docstring
lists a census line added by hand as its sixth limit, and the diff of
`tests/undeclared_readers.txt` is the warden's. This is a limit `spec.md`
§*What neither check can read* does not list; `overview.md` carries it.

**The walk is a scope that lists paths from git**, so
`tests/test_a_shrunken_corpus_declines_to_judge.py` went red on it the
moment the module was tracked, and `tracked_python` is classified there under
`APPLIES_THE_SHARED_GUARD`. It returns the missing half; phase 2's real-tree
case declines on it.

**Seen red (§15), each through `bin/mutation-check` against 248c33b2, every
verdict `red`:** one break per new unit — `bindings`, `dotted`, `k1_call`,
`k1_calls`, `module_body_calls`, `Declaration`, `declarations`, `Unit`,
`Module`, `evidence_check`, `tracked_python`, `top_units`, `unit_hash`,
`population`, `census_lines`, `read_census`, `write_census`, the
`K1_MODULES` and `CENSUS_LINE` constants, and the test module's
`census_entries` and `contradictions`. The R5, R6 and R7 cases are the ones
those breaks turned red.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
