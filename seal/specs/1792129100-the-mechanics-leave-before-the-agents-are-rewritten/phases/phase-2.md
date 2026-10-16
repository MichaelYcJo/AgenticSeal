# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 17b6e581 |


## What this phase was asked

The census and the stamps leave. `tests/undeclared_readers.txt`,
`tests/reader_registry.py`, `tests/test_a_reader_declares_its_input_class.py`
and `.github/scripts/rider_check.py` removed. The `Reads:` docstring lines and
the rider stamp lines removed by one-shot scripts in the scratch directory,
each asserting its count before and after, run once and deleted. The stamp
cases of `tests/test_a_rider_reaches_its_file.py` removed and its
`seal/follow-up.md` cases kept. `docs/the-reader-registry.md` rewritten in
place to §*A frame names what its work removes*; `CONTRIBUTING.md`'s census
bullet removed; `seal/follow-up.md`'s rider section rewritten to *a rider is
a comment, and a rider outliving its fix is the reader's finding*;
`.github/workflows/test.yml`'s comment rewritten to the reason that stays.
The spec's `## Removes` rows for the census and the stamps met.

Decided before the spawn: the stamp inside the `RIDER:` HTML comment of
`agents/smith.md` goes with the others and the comment stays, with no agent
eval, recorded as a divergence; anything else that stood on the census or
the stamps leaves in the same commit, found by `git grep`, and where that
would reach into an agent definition or a preloaded skill beyond a dead
reference, a one-line removal and a record.

## What this phase found

**The two counts the frame carried were not counts of this tree.** The
`Reads:` lines: `spec.md` says 364 at d4552372, and 364 is every occurrence
of `Reads:` in a `.py` file there, the census module's own strings and
messages included; lines that begin `Reads:` were 321 at d4552372 and 325 at
74c7963a, 21 of them in the three removed files (all `executed`, `git grep
-c` and a scratch script). The script removed the other 304, in 34 files, in
three shapes: the line closing its docstring (216), the line above the
closing quotes (36), and the line above a further paragraph (52). Twelve
docstrings were left as one summary line above their closing quotes, the
shape `ruff format` refuses, and a second one-shot script joined those 12 in
8 files. The stamps: `spec.md` says 55 `RIDER:` comments in 20 files, and 55
is the number of FILES holding the string `RIDER:` (`git grep -l`); the
checker itself read 12 riders in 11 files at 74c7963a (`rider_check.py#all_riders`,
executed before its removal), each with one stamp.

**One stamp stays, because the bytes it sits in are pinned.** The rider at
`hooks/cmdline_base.py`'s `_git_options` is inside the frozen copy of
`86256492:hooks/cmdline.py`, which
`tests/test_the_frozen_reading_never_grows.py::test_the_bytes_below_the_rider_are_86256492s`
holds byte for byte. The script removed it with the others and the line was
put back; the file's own top stamp, above the pinned bytes, is gone. The
eight `Verified … against …@…` lines in `tests/block_shapes.py` are fixture
text of the rider shapes K1 to K7, which every renderer case still reads as
documents, and stay as the quotations `spec.md` §*Scope* keeps. So
`git grep -n -E "Verified [0-9-]+ against" -- ':!seal/specs' ':!changelog'`
finds nine lines, those two kinds, and no live stamp.

**The checker had more readers than the frame named.** Four other test
modules loaded `rider_check.py`, and their rider cases left with it: 15 in
`tests/test_every_reader_ends_a_line_where_gfm_does.py` (its whole rider
section, cut by a third one-shot script asserting the 15 and that each loads
the checker, plus five `OUT_OF_CLASS` rows), one in
`tests/test_the_hooks_hide_what_a_renderer_hides.py`, the rider row of
`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`'s table
(five readers became four, and `docs/the-record-layout.md`'s statement under
marker 1791852615 with them), and the rider half of
`tests/test_a_unit_is_bounded_where_a_parser_decides.py`'s refused-suffix
case. `tests/test_a_format_has_one_reader.py` lost two heading exemptions and
`tests/test_a_shrunken_corpus_declines_to_judge.py` the census reader's row.
86 test functions left in all, and nothing outside the work records names
one of them (a scratch script, executed).

**What else stood on the two facts, and where it went.** Enumerated with
`git grep -n -i -E "rider check|rider_check|re-?stamp|reverify|census|undeclared|reader.registry|input class|#835|Reads: " -- ':!seal/specs' ':!changelog'`
and the same over `stamp` in `agents skills templates docs hooks .github`:

- `docs/branch-and-release.md`'s marked statement on the stamp (marker
  1788826000) named two removed cases as its `Enforced by:`; it now states
  the half that stays, that the `target:` line is what names a commit, and
  points at `docs/the-review-record.md`. Its hotfix sentence no longer names a
  rider stamp.
- `docs/one-root-by-lifetime.md` and its `.ko.md` edition each lose the
  sentence about the rider stamp's history.
- The coordinate kernel stays and stops naming its two removed readers; its
  `ANCHOR_NAME`…`ANCHOR_HASH` constants had no reader left once
  `rider_check.py` went (`git grep`, executed) and leave, as do its two
  `#835` input-class paragraphs.
- `hooks/blocks.py` names two readers of its walk, `hooks/config.py`'s and
  `unverified_check.py`'s comments stop naming the rider check, and
  `hooks/config.py#config_rows` and `hooks/worktree-guard.py#main` lose the
  sentence that explained their `Reads:` line.
- `skills/implement/scripts/seal.py`'s rider loses its two paragraphs about
  how it was stamped; `hooks/root-migrate.py`'s rider loses its sentence
  about the rider test; `tests/block_shapes.py` and `tests/config_shapes.py`
  lose the clause that the rider check reads `tests/`.
- `.github/workflows/test.yml`'s *Not shallow* comment named the rider test,
  which had not asked git anything since #239. The reason that stays is the
  frozen-copy case, which shows `86256492:hooks/cmdline.py` and skips at
  depth 1, so `fetch-depth: 0` stays and the comment names that case.
  `publish-release.yml`'s comment pointing at it, and
  `tests/test_ci_gives_the_checks_what_they_need.py`'s docstring and message,
  said the old reason and named `tests/test_the_reopening_is_one.py`, which
  is not in the tree; both now name the frozen-copy case.
- `agents/smith.md`: the stamp line inside the `RIDER:` comment is removed
  and its `-->` joins the line above. Nothing outside the comment changed, so
  no agent eval ran.
- Not touched: `docs/the-pact.md`'s marker
  `specs/1791076833-the-reverify-writer-records-before-it-restamps` is a work
  item's id; `tests/test_session_cost.py` keeps
  `python3 .github/scripts/rider_check.py` as a command string it classifies;
  `evals/behaviour/` replays rounds at their own old commits.

**The file name `docs/the-reader-registry.md` stays.** It now holds the one
rule and is titled *What a frame removes*; `CONTRIBUTING.md`,
`templates/sdd-spec.md` and the record layout's index link it by that path,
and a rename is a change to three readers this phase had no reason to make.

**`.test_durations` is not pruned.** The durations case passes with the
removed cases' entries still in the file (`bin/test tests -q -k
"test_the_durations_file_prices_the_suite or
test_no_collected_id_carries_the_interpreters_path"`, exit 0, 2 passed, 7,383
deselected, executed), so #931's method was not needed. That run also
collected the whole suite with no collection error, which is the check that
no module still imports a removed file.

**For phase 3.** The `Reads:` removal moved `chain_check.py`'s lines: the
constants `plan.md` quotes at `:93-191` are now `SEVERITY` at `:98` to
`DEFERRED_VALUE` at `:184`, `records` starts at `:1249`, and the file is
1,597 lines (`grep -n`, `wc -l`, executed). `unverified_check.py#CLOSED` is
still line 75.

**A hook reformats on save here.** A PostToolUse hook ran after edits and
removed an import left unused (`bisect`, in the GFM-lines module). It changed
nothing else this phase saw; `ruff check` and `ruff format --check` over the
51 changed Python files exit 0 (executed).

**The case this phase changed, and how it was seen red.**
`tests/test_a_rider_reaches_its_file.py::test_the_header_says_a_rider_carries_no_stamp_and_no_checker`
replaces the case that pinned the stamp form in the header. Seen red against
the header as it stood at 74c7963a (exit 1, executed), then `mutation-check`
`red` on each of three breaks of the rewritten header at 17b6e581: the
sentence it pins reworded, a `Verified <date>` put back, and `rider_check`
named (executed). The other seven cases of the module are unchanged.

**Verification.** On the tree committed as 17b6e581, all executed: `git grep -n "Reads: " --
'*.py'` finds nothing; `git ls-files` names none of the four removed paths;
`bin/rules --check` exit 0, *all 413 `Enforced by:` targets in 60 rule files
resolve*; `bin/test` over the plan's four modules and the 23 others this
phase edited or that read an edited document, exit 0, 951 passed and 2
skipped (the two collection cases above, run separately); a second batch
over the modules reading `agents/smith.md` and the stamped riders' files,
exit 0, 438 passed.
