# Phase 1: 1793251203-seal-pact-passes-near-misses-of-an-anchor

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | ce323fe9 |

## What this phase was asked

Build phase 1, the anchor table's near misses, against the committed frame
at `44df3d1d`, and commit it with this record and its Status cell. Each new
case is seen red against `28edee12`, as the plan's *Verified by* cell
states, and the phase runs the command that cell names. Edit no file of the
parallel work items #1123, #1127 and #1158, and write no `changelog.md`.

## What this phase found

**The frame holds, with three corrections found against the tree.**

- **S5 cannot be seen red against `28edee12`.** At that commit no row scan
  exists, so the d06 frame already prints exactly one `REFUSED` line, and a
  count of one passes. The count pins plan A11, which only the new scan can
  break. It was shown red by `seal mutate` instead: with the guard
  `if not table_refusals:` replaced by `if True:`, five ids of
  `test_refuses_an_anchor_row_nobody_reads` failed, the new d06 id among
  them.
- **S5 is an assertion on its group, not a new case.** The walk's
  frame-level refusals are already one parametrised case,
  `test_refuses_an_anchor_row_nobody_reads`. It gained the d06 shape as the
  id `a row under a blank line`, and every id now asserts that the frame is
  refused once. A separate case would cover nothing that group does not.
- **The frame's own text fails a census.** `frame/design.md` line 49 writes
  the probe's d16 remote on a domain other than `example.com`. The
  `real_identifiers` census refuses it, through
  `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`.
  That case fails at the frame commit `44df3d1d` as well, run in a scratch
  clone, so it predates this phase. A crafter does not write the frame, so
  the line stands for the orchestrator. S1's "another host" shape is written
  `git@git.example.com:org/orders-api.git` here.

**W1, the two sentences.** `questions.md` W1 left their names and words to
this phase. Both are constants in `pact_check.py` and are pinned whole by
the test module's copies:

- `UNDECLARED`, formatted with the cell as written: "the `Pact` cell names
  `{cell}`, a pact this signer's `seal/config.md` does not declare in its
  `Pact` row, so no `seal pact` grades the row — write the origin URL of a
  pact that row declares, or add `{cell}` to that row".
- `OUTSIDE_TABLE`: "the row names a pact this signer declares and a clause,
  and no anchor table holds it, so nothing grades it — write it as a row of
  a table headed exactly `| Pact | Clause | Hash |`".

Both pass `tests/behaviour/test_one_word_one_meaning.py`. W1's Status cell
in `questions.md` is not a crafter's write, so it is still `open`.

**Decisions made while writing the code.**

- The row scan is `stray_rows`, and the line reader it uses is `row_cells`.
  `row_cells` adds an outer pipe only where the line leaves one out. A line
  whose leading spaces and tabs reach four columns, a tab counting to the
  next multiple of four (`blocks.columns`), is an indented code block and
  reads as no row. The passes case pins a four-space line, a tab line and a
  two-spaces-and-a-tab line in the frame that holds no anchor table. At
  `ce323fe9` the code kept the leading spaces alone, so a tab-indented line
  read as a row; round 1, finding 1, found it, and `1783b55a` counts
  columns instead.
- A row is refused only where the remote cell and the heading cell are two
  different cells, as `frame/design.md` *Scope* item 2 says. No cell can be
  both a bare remote and a heading, so the distinction changes nothing a
  case can reach. It is kept because it is the rule's wording.
- `test_refuses_an_anchor_row_no_anchor_table_holds` holds the nine shapes
  of the probe (d07, d08, d09, d12, d13, d14, d15, d26, d24). It also holds
  one more of the class: a near-miss table under the next heading, below a
  correct anchor table. There the walk reads the anchor table and refuses
  nothing, so only the scan sees the row.
- The passes case gained a row that misses twice: a near-miss header over a
  remote one letter off. It pins the limit `## Rule changes` adds to
  *What this does not see*, and it is what turns the mutant `if headings:`
  red.

**A walker limit found by trying, outside this plan.** An anchor table
followed by a blank line and then an indented code block whose line is
written `| … |` is refused by `hooks/lib/config.py#gfm_table`. The refusal
calls the line a row the walk never reaches. GitHub renders that line as
code, so the refusal is wrong in the loud direction. The plan does not edit
`hooks/lib/config.py`, so this phase leaves it alone, and the passes case
does not place an indented block below an anchor table.

**Red first, executed.** In a `git clone --no-local` of the worktree at
`28edee12`, with this phase's test module copied in, these twelve ids failed:
S1's two ids, which exited 0, and S3's ten ids, of which nine exited 0 and
the one below a graded anchor table exited 1. The clone was removed before
hand-back.

**Mutation, executed.** One `seal mutate` call over `pact_check.py` with ten
mutants, run against `Test_check`, came back with every mutant red. The
mutants were the undeclared arm, the walk-refused guard, the exclusion of
the walked rows, the scan's condition replaced by `remotes`, by `headings`
and by `False`, each outer pipe given, the kept indentation, and the
declared-remote test made to accept any remote. None of the ten narrowed
the scan to this pact alone; that mutant survived until round 1, finding 2,
and the id `a row naming another pact the signer declares` turns it red.

**Phase boundary, executed.** One `bin/test` command ran eleven modules and
counted 1011 passed, 8 skipped and 1 failed: the three modules the plan
names, every module that reads `pact_check.py` or runs it through the world
in `tests/conftest.py`, and the modules that sweep the shipped scripts'
text. The one failure is the census above.
