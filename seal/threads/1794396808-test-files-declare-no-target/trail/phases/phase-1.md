# Phase 1: 1794396808-test-files-declare-no-target

## What this phase found

**The frame holds against the tree at `74771da90`, with two
departures.** `74771da90` differs from `b9ca37404`, the commit the framer
read, only under `seal/threads/` (executed: `git diff --stat b9ca37404
74771da90`). The coordinates of `frame/plan.md` *Technical context* stand
there: `#check` at `:341`, `#_calls` at `:462`, `#main` at `:1198`, and
`CONTRIBUTING.md` *The test layout* at `:216-338` (read). G11 holds:
`git grep` finds `--all` and `every=` in the tree only in
`skills/verify/scripts/test_layout.py` and its cases (executed). Both
departures are below.

**The counts at the base, design *Scope* item 12.** They were taken at
`74771da90` before any edit, and they equal design *The counts* at
`b9ca37404` (executed).

| Count | At `74771da90` | At `490eb834b` |
|---|---|---|
| last line of `bin/seal layout --check` | `139 files read, 0 refused, 86 declare no TARGET` | `139 files read, 0 refused, 86 declare no TARGET` |
| last line of `bin/seal layout --pairs` | `139 files read, 107 pairs` | `139 files read, 42 pairs` |
| `git grep -c '^# No TARGET: ' -- tests \| wc -l` | 0 | 0 |

**S1: the 66 pairs of `tests/github/test_run_tests.py` are gone, and one
pair is new.** At `490eb834b`, `bin/seal layout --pairs` names no pair of
`tests/github/test_run_tests.py` (executed: `grep -c` over its output
gives 0). Set against the base's output, the only line that is new is
`tests/skills/test_test_layout.py::Test_main:
test_refuses_a_misplaced_class_with_exit_one and
test_refuses_a_directory_outside_a_repository call main with equal
arguments` (executed: `diff` of the two outputs). This is the first
departure. Design G4's probe counted 41 pairs. The 42nd comes from design
`## Removes` row 2, which keeps the second case's refusal "with `--check`
alone", so both cases now call `main(["--check"])`. The two worlds
differ: a monkeypatched `_toplevel` returns a fixture directory in one
case and `None` in the other. By design *Scope* item 11, the class
docstring of `Test_main` now states that input. The pair is correct code,
so no case was rewritten to avoid it (contract rule 18; `frame/plan.md`
A7 rejects the same move for the `main([])` cases).

**S2: `--all` is gone.** `bin/seal layout --check --all` exits 2 and
prints `seal layout: error: unrecognized arguments: --all`. `git grep -n
-e '--all' -- skills/verify/scripts/test_layout.py` lists nothing and
exits 1 (both executed). With the `every` parameter, the refusal of a
twin between two files that declare no `TARGET` went too, as design
`## Removes` row 1 says. That twin is still reported, and the second half
of `Test_check::test_refuses_a_twin_beside_a_declared_file` holds the
report line.

**The reader's change, seen red.** The new row
`only-empty-displays-and-none` of
`Test_pairs::test_refuses_two_cases_whose_calls_show_no_input` calls
`x.parse([], (), strict={}, other=None)` in both cases. It failed against
the reader at `74771da90` on its `layout.pairs(...) == []` line, with the
pair printed (executed, before the reader changed). The second new case,
`Test_pairs::test_accepts_an_empty_display_beside_an_input_as_a_pair`,
asserts that a call passing `[]` beside `"a"` is still compared. This
behaviour already held at the base, so the case passed there. It was
shown red by the `seal mutate` run below that removes its guard. This is the second
departure: the design asks for one case in `Test_pairs`, and the second
case holds the word *every* in design *The pair reader*, which the first
case cannot tell from *any*.

**`seal mutate` over `_carries_no_input` and the `given` line of `_calls`,
after `490eb834b`** (executed, each command exited 0):

| Mutant | Cases run | Verdict |
|---|---|---|
| `return not argument.elts` to `return False` (a list or tuple display never empty) | `-k only-empty-displays-and-none` | red |
| `return not argument.keys` to `return False` (a dict display never empty) | `-k only-empty-displays-and-none` | red |
| `argument.value is None` to `argument.value is False` | `-k only-empty-displays-and-none` | red |
| the four-line `given = not all(...)` to `given = node.args or node.keywords`, the reader at the base (S1's red run) | `-k only-empty-displays-and-none` | red |
| `given = not all(` to `given = not any(` | `-k test_accepts_an_empty_display_beside_an_input_as_a_pair` | red |

Each ran as `bin/seal mutate skills/verify/scripts/test_layout.py
--replace ... --tests "bin/test tests/skills/test_test_layout.py -q -x -p
no:xdist -k <cases>"`. The removal of `--all` adds no behaviour, so it
owes no run.

**`CONTRIBUTING.md` *The test layout*, design *Scope* item 3.** The
paragraph that opened "A test file that declares no `TARGET` stands by
what its cases run" now states kind M and kind T, the reason line, and
that the tree-wide files are the files that declare no `TARGET`, wherever
they stand. Kind D was stated in the section's first paragraph, as "A
case whose assertion reads a shipped document names that document". That
sentence was rewritten there to *The kinds*' D, so no sentence states the
rule twice. The same paragraph now says "lists the files that declare
none", and it says where a pair carries its reason.

**`CONTRIBUTING.md` *What a contribution is asked for*, outside the
section `frame/plan.md` *Technical context* names.** Its line 43 called
`tests/text tests/behaviour` "the tree-wide files *The test layout*
names". Once a file of either directory declares a `TARGET`, the
directories hold more than those files, so the line now says the two
directories "hold the tree-wide files". This is a citation of the rule
item 3 rewrote, corrected under contract rule 19.

**The other statements of the reworded rules, a sample.** `git grep` ran
over the tree outside `seal/threads/` on `declare one yet`, `tree-wide`,
`stands by what its cases run`, `take any name`, `such calls are equal`,
`with no argument`, `--all` beside `layout`, and `TARGET` under `docs/`,
`skills/` and the READMEs (executed). It found `CONTRIBUTING.md:43`
above and nothing else to correct. The search finds only the spellings
it was given, and a statement worded otherwise stands unread. One
sentence was read and left as it stands, for the framer.
`CONTRIBUTING.md` *The test layout* still counts "a pair
`bin/seal layout --pairs` names inside one of the module's classes" as a
reason to write that module's tests anew. Under design *Scope* item 11,
a pair whose class docstring states its reason stays a pair, so that
threshold also counts it. The design does not name the threshold, and
this phase does not change it.

**The phase boundary, as one command** (executed, at the working tree of
`490eb834b` with this record and `gaps.md` written):

```
bin/test tests/text tests/behaviour tests/skills/test_test_layout.py tests/github/test_plugin_directory_check.py tests/github/test_release_report.py tests/github/test_run_tests.py tests/github/test_rules.py tests/lib/test_launch.py tests/skills/test_chain_check.py tests/skills/test_passages.py tests/skills/test_seal.py tests/skills/test_session_cost.py -q
```

The set is the two tree-wide directories and the module this phase
edited. It also holds each test file outside those directories that
names `CONTRIBUTING` or `test_layout` (executed: `git grep -l`), and
`tests/github/test_rules.py`, because `CONTRIBUTING.md` is a rule file.
Two helpers, `tests/conftest.py` and `tests/censuses.py`, name
`CONTRIBUTING.md` only in a comment and a docstring, so they read no
changed path. Run at `490eb834b` before the records were written, the
set gave `1 failed, 2925 passed, 8 skipped`. The one failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
for this work item's missing `gaps.md`, which this phase writes. Run
again with the records written, it gave `2926 passed, 8 skipped` and
exited 0 (S9). `bin/seal layout --check` exits 0 at `490eb834b` (S7,
executed).
