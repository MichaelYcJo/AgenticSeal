# Phase 3: 1793251203-seal-pact-passes-near-misses-of-an-anchor

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 5267a54e |

## What this phase was asked

Build phase 3 against the reframed frame committed at `d2bcca59`, as its
`frame/plan.md` row says, and commit it with this record and its Status
cell. Run what the row's *Verified by* cell names, and see each new case
red against `a5533a3d`. The phase removes the units phase 1 built, which
`frame/design.md` `## Removes` rows 4 to 6 list. It does not rewrite
`changelog.md` or `gaps.md` (`## Removes` row 7): the orchestrator does,
after the hand-back.

## What this phase found

**The frame holds, with one correction found against the tree.** S10's
`git grep -n -i "no anchor table holds\|misses twice\|four columns"` over
`skills/verify/scripts/` and `tests/skills/` does not print nothing. It
prints one line, `skills/verify/scripts/unverified_check.py:413`, which
predates this work item and describes another script's reading of an
indented code block. Over `pact_check.py` and its test module the search
prints nothing (executed). The line stands, because it states a fact about
`unverified_check.py`, not the scan.

**The emphasis pattern keeps no guard a case can watch.** The first commit
of this phase, `d0351fd6`, wrote `EMPHASIS_RUN` with three guards from
`frame/design.md` *Scope* item 2: no space just inside a run, a run that is
the whole delimiter run on its side, and no escaping backslash before the
closing run. None of them can change whether a header is the anchor table.
A key equals an anchor cell's key only where the wrapped text is the word
itself, case folded, and none of the three words holds a space, a `*`, a
`_` or a backslash. So a mutant dropping any guard leaves every decision
the same, and no case can turn it red. `5267a54e` removes the guards. The
pattern is now the run, one to three long, the text it wraps, and the same
run closing the cell. Its comment states why a space inside a run, a nested
run or an escaped delimiter still keys to no anchor cell. The decision is
the crafter's, against `CLAUDE.md` *The rule a mechanism is kept against*
and the contract's mutation rule.

**S6 gained one shape.** `| *Pact_ | Clause | Hash |`, two different runs,
pins the member's "the same run opening and closing the cell". Without it a
mutant that lets any run close the cell stayed unwatched. GitHub renders
`*Pact_` as the literal text, so it is another table by the frame's own
definition (`frame/design.md` *Grounding*, the rendering row).

**A run of four is not watched, and this phase leaves it so.** No case
holds a run of four or more, so widening `{1,3}` to `{1,4}` would pass
every case (read, not run). CommonMark renders `****Pact****` as strong
emphasis nested twice, which shows the word in bold. The frame closes the
member at three (`frame/design.md` *Scope* item 2, `questions.md`
*What the normalisation holds*). A case pinning four as another table would
fix in the tree a shape whose meaning the owner's direction may read as the
same, so none is written. Whether four belongs in the normalisation is the
orchestrator's to put to the framer.

**S4 is a case of its own.** `test_refuses_a_row_it_cannot_grade_at_its_line`
writes every row under the exact header through `conftest.py#anchor_table`.
S4 varies the header, which that group's parameters do not reach, so
`test_refuses_an_undeclared_remote_under_a_lower_case_anchor_header` stands
beside it. The plan's row allows either form.

**Removed with the scan's case, and not carried into S6.** The reordered
header, the header with a fourth column and the table with no outer pipes
were ids of `test_refuses_an_anchor_row_no_anchor_table_holds`. They go with
it. `## Removes` row 6 carries only the plural, code-span and headerless
ids into S6, and this phase follows it.

**Decisions made while writing the code.**

- `header_key` and `EMPHASIS_RUN` hold the normalisation. The module
  docstring names `header_key`, and neither names the proofer:
  `skills/code-review/SKILL.md`'s sentence, phase 4's, points at the
  docstring, so the shape has one source.
- `first_table` takes `key=None`. With a key it reads `config.unfenced`
  once, keeps every line whose cells key to the header's, hands the first
  such line's cells as written to `gfm_table`, and names every further one
  as a second header. Without a key it matches exactly, so the map reads as
  before.
- The second-header sentence still names `| Pact | Clause | Hash |`, the
  header the reader asks for, at the line of the further header. A walk
  refusal quotes the header as the frame writes it.

**Red first, executed.** In a `git clone --no-local` of the worktree at
`a5533a3d`, with this phase's test module copied in,
`bin/test tests/skills/test_pact_check.py -q -p no:xdist -k Test_check`
failed 12 cases and passed 51:

- S3's nine ids, each `assert 2 == 0`, the row refused as one no anchor
  table holds;
- S4, `assert 0 == 2`, the `READ` line counting 0 anchors;
- S5's id, with `UNMATCHED` at line 3 and the row at line 9 refused as one
  no anchor table holds, in place of the second-header sentence;
- the passes case, with every S6 row refused at frame z's lines 7, 13, 19,
  25, 31, 37, 43 and 47.

The clone was removed before hand-back.

**Mutation, executed.** One `seal mutate` call over `pact_check.py`,
against `Test_check` with `-x`, came back with 7 mutants red and none
surviving. The mutants dropped the case fold; narrowed the run to one
character; let any run close the cell; handed the walk the exact header;
compared header cells without the key; left the key out of `check`'s call;
and counted further headers exactly.

**Phase boundary, executed.** One `bin/test` command ran nine modules: the
three the plan names, every other module that reads `pact_check.py` or runs
it through the world in `tests/conftest.py` (`test_a_reference_root_is_read_and_never_taken.py`,
`tests/hooks/test_config.py`, `test_coordinates.py`, `test_seal.py`), the
census module, and the module that globs `skills/*/scripts/`. It counted
1009 passed and 8 skipped, exit 0, with this record and the Status cell in
the tree.

**Lint and format, executed.** `uvx ruff check` and
`uvx ruff format --check` over `pact_check.py` and its test module passed
before each commit. The repository configures no typecheck: `seal/config.md`
*Broad gate* runs ruff and `bin/test`, and `CONTRIBUTING.md` names none.
