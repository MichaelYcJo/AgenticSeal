# Feature Specification: close the mutation gaps the old tests had

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CONTRIBUTING.md` *The test layout*, first paragraph | Where a new case goes. Each shipped module has one file, `tests/test_<stem>.py`, whose first assignment is `TARGET`. It holds one class per public top-level function, `Test_<name>`, spelt as the code spells it, and a private function may have a class too. A case for good input is `test_accepts_<what>` and one for bad input is `test_refuses_<what>`. The file ends with `test_census = census_case(TARGET)` |
| `CONTRIBUTING.md` *The test layout*, *A rebuilt module's record carries its move check or its mutation table* | The mutation table and `bin/mutation-check` with `-x` in its tests command are the instrument #942 used, and this work reuses both |
| `skills/verify/scripts/mutation_check.py`, module docstring | The verdicts the build reads: `red` exit 0, `SURVIVED` exit 1, every run that measured nothing exit 2. A replacement that does not land exactly once is refused before anything runs. `--replace` given more than once is a batch with one baseline |
| `CONTRIBUTING.md`, the paragraph on `.test_durations` | `test_the_durations_file_prices_the_suite` fails when more than one collected case in twenty has no price, or more than one second in twenty of the file belongs to cases no longer collected. The file is refreshed from the branch's `tests` run artifact, never written by hand |
| `CLAUDE.md` *The rule a mechanism is kept against* | Code no caller reaches is not kept by pinning it with a case. It is removed, and the removal is named here |
| Contract rule 15 | A new case counts only after it has been seen red against its mutant |
| `skills/settle/SKILL.md` *Rule changes* and `docs/the-reader-registry.md` *A frame names what its work removes* | The shape of `## Rule changes` below (the no-change block) and of `## Removes` |
| `CLAUDE.md` *Repo rule: no real identifiers in examples or fixtures* | A fixture domain is `example.com` and a user path is `/Users/x/` |

## Scope

### What the list is, read at `134d7203`

The list is the issue's body and its three comments together: the body's
*The gaps* section, and the tables of the round 3, round 4 and round 10
comments. The body says an old gap the later fix passes add is posted as a
comment, so the comments are part of the list and not a later request. Each
row names its record by a path under
`seal/specs/1792628098-tests-rebuilt-one-file-per-module/` and a line at a
pinned commit, read with `git show <commit>:<path>`. The body's commit is
`79f9c3fd`, and each comment names its own. The issue is the one source of
the rows; this spec does not copy them.

Two more survivors are in scope: the two of
`skills/verify/scripts/pytest_record/specseal_pytest_record.py` that the
body's *Two more, recorded only in a review round* names, "the invocation
directory read as the working directory" and "`wasxfail` never written".
They meet the body's own definition of an old gap: they survive the files at
the head of #942 and the old files at `482fed97`. The body left them
uncounted only because their record is a review round. The module is
unchanged between `79f9c3fd` and `134d7203` (`executed`, `git diff --stat`).

### Rows whose code left the tree

A row whose code is gone is not a gap. These rows are settled by this frame
and get no mutant. Each was `executed` at `134d7203`: the file is absent, or
`git grep` finds no definition of the name anywhere in the tree's Python.

| Rows | Where they stood | What removed them |
|---|---|---|
| The body's six `hooks/commitgate.py` rows: phase 5's c2, c15, c17 and c26, group 13's c3 and c6. The two unclear rows of the body's *Unclear* section are c15 and c17, so they go with the module | `hooks/commitgate.py` | `61a8455a` (#1027) deleted the file |
| The body's two `hooks/commit-review-gate.py` rows, g12 and g15. The round 4 comment's g15 is the same row | `hooks/commit-review-gate.py` | `61a8455a` deleted the file |
| The round 3 comment's a5 and a9 | `hooks/answers.py` | `61a8455a` deleted the file |
| The round 3 comment's l1 | `hooks/answer-clear.py` | `61a8455a` deleted the file |
| The round 4 comment's cp1 to cp6 | `_corpora` in `tests/test_the_old_spellings_reach_the_hook.py` | `61a8455a` deleted the file |
| The body's m66 and m68 (`understood`), m77 and m78 (`_cd_target`), m81 (`compose`), m91 (the walk: `walk_directories`, `_step` and `_land`), m117 and m118 (`adds_a_worktree`), m119 and m120 (`apply_chdir`) | `hooks/cmdline.py` | `61a8455a` removed the text reading, and with it every one of these functions |
| The round 3 comment's g3 (`lines`) | `hooks/gate.py` | `61a8455a` cut the module to `touches_code` |
| The body's s62 (`GUARANTEE_PATH`) and s63 (the `diff-tree` call), both marked equivalent | `skills/verify/scripts/seal_stamp.py` | Neither the constant nor a `diff-tree` call stands in the module at `134d7203` |

The body asked that `hooks/cmdline.py`'s rows wait for #1014. #1014 was
closed on 2026-10-25 as superseded by #1027, and #1027 shipped as
`61a8455a`, which removed the text reading. Seven of the module's seventeen
rows name a function that still stands: m11 and m17 (`drop_heredoc_bodies`),
m20 (`split_segments`), m24 (`split_segments_with_separators`), m25 and m26
(`merged_view`), and m47 (`_env_walk`). Those seven are in scope.

### In

1. **Every other row is rebuilt at the branch's head and given one
   outcome.** The build turns each row's sentence into one `--replace OLD
   NEW` pair at the decision point the sentence and its record describe,
   and runs the module's batch against the module's test file with `-x`.
   Each row ends with exactly one of four outcomes:
   - **left the tree**: the decision the sentence describes is no longer
     made by the module at the head. The phase names the commit that
     removed it, found with `git log -S` or `git log -L`, and runs no
     mutant;
   - **already closed**: the mutant is red against the module's test file,
     or, where it survives that file, red against another test file whose
     cases reach the module. The phase names the case that kills it;
   - **killed by a new case**: the mutant survives every test file that
     reaches the module, and a case is added that is seen red on it and
     green on the code;
   - **equivalent**: no input tells the mutant from the code, and the
     phase writes the reason from reading the code.

   A row the records mark equivalent is confirmed by reading the code at
   the head. Where the reading finds an input that tells them apart, the row
   is a gap and gets a case. A row whose survival shows that the code, and
   not the cases, is wrong is the one exception to the four: it is recorded
   as a finding and gets no case (`questions.md` Q4).
2. **A new case goes in the class of the function the mutant changes**, in
   the module's own test file, under the names `CONTRIBUTING.md` *The test
   layout* gives. Where that class does not exist yet, the phase adds it.
   A mutant of a module-level constant goes in the class of the function
   that reads the constant. A mutant the records place in no function goes
   in the class of the function that holds the decision point at the head,
   or in `Test_module` where that point is module-level code.
3. **`hooks/implementer.py` gets its own test file**,
   `tests/test_implementer.py`, with `TARGET = "hooks/implementer.py"` and
   the census line, because the layout gives each shipped module one file.
   Its two rows' cases go there and nowhere else.
4. **`gh_json` in `.github/scripts/close_issues_on_release.py` is removed**
   rather than pinned. It has no caller in the tree (`executed`,
   `git grep gh_json` at `134d7203` finds only its definition and #942's
   records). The row c13 is closed as left the tree, by this work's own
   commit.
5. **The phase record holds each module's mutant table**, one row per
   issue row, with both columns: the verdict against the test files at the
   phase's start, and the verdict after the phase's cases. Each table row
   also holds the `--replace` pair exactly as run, so a reader can rebuild
   the mutant.

### Out

- **A fresh sweep of each module's decision points.** The rows are what
  #942 measured; a module's other survivors at the head are a new
  measurement, and another item's.
- **Any change to shipped code other than the removal of `gh_json`, and a
  line of `hooks/implementer.py` that a census flags once the module has its
  own test file (`questions.md` Q3).** A survivor that shows a defect in the
  code, and not a missing case, is written into the phase record,
  `overview.md` and the hand-back as a finding. It is not fixed here.
- **`hooks/root-migrate.py` and `tests/test_root_migrate.py`.** #1016 changes
  both on another branch, and no row of this list names them.
- **The `hits()` row of `seal/follow-up.md`.** It is a test helper's gap in
  `tests/test_a_release_is_sized_by_a_criterion.py`, not a row of this list,
  and this work is not its prerequisite.

### Where the branches meet

#945 may add a class to `tests/test_session_cost.py` for a new per-segment
column of `skills/verify/scripts/session_cost.py`. This work's cases for
that module go in the classes of the functions they test, `Test_count`,
`Test_load`, `Test_report_segments` and the rest, each placed in the order
the functions stand in the module. A class name both branches add is the one
place the merge is more than textual: two definitions of one class name
leave the second one live. `uvx ruff check` reports a class redefined
without use (F811), so the second branch to merge meets it at lint and puts
its cases into the class that is already there.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A gap that stands is closed | Given a row whose mutant survives every test file that reaches its module at the phase's start, when the phase's case is added, then the mutant is red against the module's test file and the code passes it | The phase record's table: the before column `SURVIVED`, the after column `red` with the new case named; the module's `bin/mutation-check` batch with `-x` exits 0 at the phase's commit |
| A new case was seen red | Given a new case, when it runs alone under its mutant, then it fails, and against the code it passes | `bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -k <case>"` prints `red`, its baseline having passed; the phase record quotes the line |
| A row already closed is not given a second case | Given a row whose mutant is red at the phase's start, when the phase reads the failing case, then no case is added and the table names the killing case and its file | The phase record's table and the diff: no new case for that row |
| A row whose code left the tree gets no mutant | Given a row whose decision the module no longer makes, then the table names the commit that removed it | This spec's table *Rows whose code left the tree*, or the phase record's table with the commit; `git show <commit>` shows the removal |
| An equivalent row says why | Given a row confirmed equivalent, then the table gives the reason no input tells the two apart, from the code at the head | Read by the warden at review |
| `gh_json` is gone | Given the branch's head, then no definition or call of `gh_json` stands in the tree's code, and the module's test file passes | `git grep -n gh_json -- '*.py'` prints nothing; `bin/test tests/test_close_issues_on_release.py -q` exits 0 |
| No case is removed, and the durations file stays true | Given the branch's head, then every case collected at `134d7203` is still collected, and `.test_durations` prices the suite within its share | The diff removes no `def test_`; `test_the_durations_file_prices_the_suite` in the orchestrator's broad gate |
| The cases hold on all three CI legs | Given a case whose decision reads the platform, the process tree or the console, then the case fakes that reading, so it gives the same verdict on Linux, macOS and Windows | The pull request's `tests` jobs on the three legs |
| The concurrent branch meets this one textually | Given #945 adds a class to `tests/test_session_cost.py`, then this work's cases there stand only in `Test_<function>` classes of `session_cost.py`'s functions | The diff of `tests/test_session_cost.py`; `uvx ruff check` at the merge |

## Data & interfaces

No interface changes. The tests change, and one shipped function is
removed: `.github/scripts/close_issues_on_release.py#gh_json`, a function
nothing calls. One test file is added, `tests/test_implementer.py`.

## Rule changes

- nothing
  why: The work adds cases under the layout `CONTRIBUTING.md` *The test layout* already states, and removes one function nothing calls. No rule in `docs/` is added, changed or removed.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The function `gh_json`, which wraps `gh api` and parses its answer as JSON | `.github/scripts/close_issues_on_release.py#gh_json` | Nothing in the tree calls it (`executed`, `git grep gh_json` at `134d7203`). Its one survivor, c13, is closed by its removal and not by a case that would pin code no caller relies on. `_issue_api` makes the module's `gh api` reads and stays |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-27 by framer, before the build.
