# Phase 1: 1793862999-unverified-baseline-is-run-by-a-person-only

## What this phase found

**The frame held where the build reached it, with three exceptions.**
`git grep` outside `skills/verify/scripts/unverified_check.py` and
`tests/skills/test_unverified_check.py` names none of the eleven removed units,
as design *Grounding* says. The exceptions are these:

- Design A4's *Verifiable how* names `tests/skills/test_settle.py`,
  `Test_open_record_rows`. No such class is in that file. The class is
  `tests/skills/test_unverified_check.py:1743`, and it still passes.
- Design *Grounding* (the importers row) says `settle.py` uses `check_text` and
  `open_record_rows`. That is true, but `settle.py` calls `open_record_rows`
  with `ref` None only (lines 944 and 1795), and calls `check_text` on the
  disk's text (line 1770). The relaxed reading at a ref therefore has no
  shipped caller. Only the tests reach it.
- `docs/checks/the-fold.md` lines 139-145 still state that a record's rows
  are blanked "the same way on both sides of a comparison", so that "the
  working tree and the base revision count the same table". The design's
  `## Rule changes` does not name this passage. The comparison it describes
  left with `--baseline`. The phase does not edit `docs/`, so the sentence
  goes to the orchestrator.

**Q1 is answered: none.** With `overviews` reading `os.path.realpath`, all 302
cases of `tests/skills/test_unverified_check.py` pass. So no kept plain-run case
asserts a path given as named, and `overviews` reads each argument at its real
path (design *Scope* item 3, plan *Alternatives considered* row 5). I judged
this against `frame/questions.md` Q1's own options.

**The real-path reading had no case behind it, so the phase adds one.** The
first mutation run turned `os.path.realpath` into `os.path.abspath`, and the
mutant survived every case of `Test_main`, `Test_overviews` and `Test_module`.
The cases that used to reach that reading were the `Test_as_named` and
`--baseline` cases, and they left. A case linking a clone under the default
reference row still survived the mutant. The default row matches a `specs`
part wherever it stands in the path. Only a `Reference specs` prefix row
reads where the path begins (`hooks/lib/config.py#under_reference_root`).
`Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link`
therefore writes a prefix row, and the mutant now goes red on it. Design
*Scope* item 5 lists no new case besides A1. This addition departs from the
frame, on the ground of `skills/verify/SKILL.md` *The narrow command still has
to be able to fail*.

**`SETTLED` loses one clause, against the letter of *Scope* item 4.** Item 4
keeps the three exit-0 states' messages. `SETTLED` ended "and nothing left the
record without being closed". That clause claims what the base comparison
measured, and no run measures it now. I removed the clause under
`skills/core/SKILL.md` *The rule a mechanism is kept against*, which says a
change removes what stood on the old fact. The settled-root case pins the
new sentence and asserts that "left the record" is absent from it (contract
rule 14). `ABSENT` lost "and nothing to compare against the base", as item 4
says, and the no-root case pins its new text.

**The removal reached a little past the list in `## Removes`, each part for the
same reason.** None of these parts remained in use once the `--baseline` cases
were gone:

- The `forked` fixture lost its `gained` ref.
- The helpers `drop_line`, `replace_in`, `link_of`, `reported_paths`,
  `NAMED_LINK` and `a_named_link` went. `## Removes` names fixtures but not
  helpers.
- `test_refuses_a_memo_deleted_from_a_work_item_that_stays` and
  `test_accepts_an_overview_tracked_under_a_skipped_directory` went with the
  other `--baseline` cases. Each one ran only under a baseline.
- Two kept cases lost their base clause from their names:
  `test_accepts_no_root_in_the_tree` and
  `test_accepts_a_tracked_link_counted_once`.
- `tests/behaviour/test_unverified_rows_close.py` also lost the `collapsed`
  helper and the `posix_id` import. Only the two removed pins used them.

**Docstrings past *Scope* item 4's list were rewritten.** The set is closed. I
listed it with a grep of the module and its test module for `base`,
`baseline`, `compar`, `delet`, `merge.base` and `squash`, and read every hit.
Each docstring and comment that described a base comparison now says what the
unit does for the callers it has today. Beyond item 4's list, these were
rewritten:

- in the module: `blank_fences`, `readable`, `sections`, the `OLD_MARK`
  comment, `_LooseHeading` and the comment in `parse_section`;
- in the test module: the module docstring, the `LEGACY` comment and the
  docstrings of `Test_unique_by_target`, `Test_show`, `Test__LooseHeading`,
  `Test_parse_section` and `Test_sections`.

**Commits:** `a9661924` (the removal, the marker move and the pins),
`aba6d39d` and `988a9afb` (the link case). Executed at `988a9afb`:

- A1 was red against the unchanged script: "DID NOT RAISE SystemExit".
- Five mutants were run against `-k 'Test_main or Test_overviews or
  Test_module'`, each through `seal mutate`. Four went red at once: re-adding
  `--baseline`, restoring the `SETTLED` clause, restoring the `ABSENT` clause,
  and `return 1` to `return 0` on an unreadable section. The real-path mutant
  went red once the link case was added.
- `bin/seal rules --check` excuses one line, `one-merge-base` at
  `docs/checks/the-unverified-record.md:14`. Every other line holds.
- `git grep -n 'a-settle-is-no-deletion' -- tests` names only
  `tests/skills/test_chain_check.py:4026`.
- One `bin/test` run over the phase-boundary set gave exit 0: 2767 passed and
  10 skipped.
