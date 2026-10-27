# Phase 5: 1793057292-agent-lifetime-and-process-archive

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 1718924d |

## What this phase was asked

Make `.github/scripts/release_report.py`'s `DOCUMENTS` glob take
`seal/process/*.md`, so each archive file's bytes are a row beside the other
documents' (the sealer's withhold, 085530de, folded into the frame at
f8408d5e). Write a case in `tests/test_release_report.py`, seen red against
the glob without the entry, then green. Check that every reader of
`DOCUMENTS` and the report's header text still read true. Make one code
commit ending `(#945)`, then this record and phase 5's Status cell.

In the same pass, rewrite in place the record sentences the sealer named.
In `phases/phase-1.md`, the threshold's effect on #930's smith, checked
against `session-cost --segments` on that smith's transcript. In
`overview.md`, the *Fed back* item on where the fold line sits, and the
*Not verified* sentence on the commits after 08469dff. In `changelog.md`,
the archive item gains the report row. Run `tests/test_release_report.py`,
the modules that read `release_report.py` or `DOCUMENTS`, the record
modules over the changed records, `tests/test_chain_hooks_hardening.py`,
`bin/test-layout --check` and `--pairs`, and `uvx ruff check` and
`uvx ruff format --check` over the changed Python files. Do not write the
pull request body.

## What this phase found

**The frame holds for phase 5** (`read`). `DOCUMENTS` stood at
`release_report.py` line 52, and `documents()` is its one reader. The
`release-report` job builds the tag's tree with `git archive "$tag"`
(`.github/workflows/test.yml`), and this repository commits its `seal/`
root, so the tag's tree carries the archive files the tag held. Before the
first archive file is written, the tag's side has none, and the row reads
`new`.

**Two sentences of the script listed the documents, and both are rewritten
in place** (`read`). The module docstring's `<document>` entry and
`documents()`'s docstring named `CLAUDE.md`, `CONTRIBUTING.md` and each
`docs/*.md`. Each now names `seal/process/*.md` too. `HEADER` says "each
document's size", which holds. `docs/release-checklist.md` *5. The release
pull request*, the job's comment in `.github/workflows/test.yml` and
`CONTRIBUTING.md` *Running the checks* say "each document's bytes" or name
the job without a list of documents, so they stand.

**The case joins `Test_main`** (`executed`, `bin/test-layout --pairs`). The
module has no `Test_documents` class, and `bin/test-layout --check` reports
that before and after this phase. The document rows were covered in
`Test_main` by `test_the_release_table_reads_two_trees_and_fails_nothing`,
which reads them through `main`, so the new case
`test_accepts_each_process_archive_file_as_a_document_row` stands beside
it. It also asserts that no other file under `seal/` is a row, with a
`seal/README.md` and a spec's file in the tree.

**The case was seen red** (`executed`, `bin/test
'tests/test_release_report.py::Test_main::test_accepts_each_process_archive_file_as_a_document_row'
-p no:xdist -q` with the case written and the glob unchanged): 1 failed,
`assert [] == ['`seal/process/0.23.0.md` (bytes)']`. With the entry in the
glob, the module returned 16 passed.

**Mutation** (`executed`, `bin/mutation-check` after 1718924d, bounded at
300 s). Replacing `"docs/*.md", "seal/process/*.md")` with `"docs/*.md")`
in `release_report.py`, run over the new case, ended `red: the cases failed
against the mutation (exit 1)`. The tree was clean after the run.

**The threshold sentence in `phases/phase-1.md` placed each cut one slice
early, and it is rewritten in place** (`executed`, `bin/session-cost
--segments` on
`~/.claude/projects/-Users-michael-Documents-GitHub-SpecSeal/c5415a05-3853-4b1d-898b-40ecb4d67259/subagents/agent-aa6874fb2aff9e251.jsonl`,
exit 0). The seven slices read 377,894, 569,013, 655,847, 778,563, 904,072,
931,652 and 941,799, as phase 1's table gives them. The fix-pass rule reads
the largest context before the pass. Under 487,998, the smith is resumed
for its second slice and spawned fresh from its third. Under 806,241, it is
resumed through its fifth slice and spawned fresh from its sixth.
`git grep` finds the old sentence nowhere else in the tree outside
`guarantee.md`, which quotes it as the sealer's finding.

**The fold line's sentence also stands in `phases/phase-2.md`, and it is
left as written** (`read`). Its *Three choices the frame left open*
paragraph says the line sits below the approval line. That paragraph
records what phase 2 built at f7fb7028. Round 1's finding 6 changed the
rule in 5be7d538, and `rounds/round-1.md` records the change. The
`overview.md` *Fed back* item states the rule in force, and it now names
both places.

**The commits after CI run 40430474904 are no longer records only**
(`executed`, `git log --name-only 08469dff..HEAD`). 236a596d, 8eca5d5d,
085530de and f8408d5e change only this work item's records. 1718924d
changes `.github/scripts/release_report.py` and
`tests/test_release_report.py`. `overview.md` *Not verified* now says so,
and names the `236a596d` broad run with the three record commits after it
and before this phase. Two open
rows are added. One holds 1718924d for the orchestrator's next broad run
and the branch's next `tests` run. The other holds the archive's row in the
job's summary for whoever prepares the release, because the job runs only
on a pull request into `main` and no archive file exists yet.

**The narrow checks** (`executed`, each module with `bin/test <module> -q`,
each exit 0). `tests/test_release_report.py` returned 16 passed. The
modules that name `release_report.py`, `DOCUMENTS` or the `release-report`
job: `tests/test_the_release_table_reads_two_trees_and_fails_nothing.py` 1
passed, `tests/test_ci_gives_the_checks_what_they_need.py` 23,
`tests/test_one_table_walker_reads_what_gfm_renders.py` 456 and
`tests/test_release_completeness_check.py` 26. The last two match only a
constant or a case name and do not read the script. The record modules,
run over the changed records: `tests/test_chain_hooks_hardening.py` 26,
`tests/test_a_phase_hands_the_next_one_a_record.py` 13,
`tests/test_the_set_a_work_item_always_has.py` 19,
`tests/test_unverified_check.py` 333, `tests/test_chain_check.py` 256,
`tests/test_settle.py` 75, `tests/test_gather_changelog.py` 50,
`tests/test_the_changelog_is_gathered_at_release.py` 9,
`tests/test_one_word_one_meaning.py` 25,
`tests/test_the_seal_is_taken_once_by_the_sealer.py` 23,
`tests/test_release_hygiene.py` 36,
`tests/test_the_record_is_written_in_words.py` 3,
`tests/test_a_record_carries_no_comment.py` 3 and
`tests/test_docs_line_wrap.py` 39. `bin/unverified-check seal/specs/`
exited 0, counting 48 overviews, 65 open and 121 closed rows.
`bin/test-layout --check` and `--pairs` over `tests/test_release_report.py`
refused nothing and named no pair. `uvx ruff check` and `uvx ruff format
--check` over the two changed Python files reported nothing. The new case
has no entry in `.test_durations` until its next refresh.
