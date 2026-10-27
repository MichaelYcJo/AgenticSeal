# Phase 4: 1793057292-agent-lifetime-and-process-archive

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 756a59d3 |

## What this phase was asked

Write `templates/process.md`, the one line in `agents/framer.md` step 4
(S13, S14), and the work item's `changelog.md` fragment. Close the work
item, since this is the last phase: this record, the closing memo
`overview.md`, which
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
requires, and `plan.md`'s Status column. Shape the memo and the fragment on
`seal/specs/1793051803-settle-runs-in-local-mode/` at fa7d1374. The memo's
`## Not done` names the parameter of
`tests/test_unverified_rows_close.py#test_the_documents_state_the_merge_base_footing`
the settle turns red, and its `## Not verified` names the full suite and
Linux and Windows for the orchestrator. The fragment and the memo carry the
gate-change items `phases/phase-3.md` recorded, copied. See every changed
pin red first. Run the modules touched, the modules that read
`agents/framer.md` and the templates, the record modules over the new
records, `tests/test_chain_hooks_hardening.py`, `bin/test-layout --check`
and `--pairs`, and `uvx ruff check` and `uvx ruff format --check` over the
changed Python files. Build on `questions.md`'s defaults.

## What this phase found

**The frame holds for phase 4, except that S13's case did not reach the new
template** (`executed`). `tests/test_a_record_carries_no_comment.py` read
only `templates/sdd-*.md`, and *Data & interfaces* fixes the file name as
`templates/process.md`, so a comment put into it passed every census case.
The census now reads `RECORD_TEMPLATES`, the `sdd-*.md` templates and
`process.md`. Its count case reads 9, and its planted case puts a comment
into a `process.md` and expects it refused at its line. The emoji census of
`tests/test_the_record_is_written_in_words.py` reads `templates/*.md`, so it
reached the new template unchanged.

**`spec.md` still says 461,000** (`executed`, `git grep -n "806,241\|461,000"`).
*Scope* item 2 says the fix pass resumes below 461,000 tokens, while
`skills/code-review/orchestration.md` line 30 says 806,241, the answer to
Q3. The folding rule this work item writes asks the orchestrator to fold a
later decision into the frame in place, and Q3's answer is not folded into
*Scope* item 2. The memo records it as a divergence. `spec.md` is not among
the files a phase writes, so the fold is the orchestrator's.

**S14 has no case** (`read`, `spec.md` S14 names the warden). The line went
into step 4 after the sentence on earlier work items' round records: the
archive of the highest version, `seal/process/<X.Y.Z>.md`, read once where
the `seal/` root holds one. "The latest" in *Scope* is read as the highest
version, because a file's time would read two ways.
`tests/test_every_agent_reads_the_contract.py#test_every_file_a_step_names_exists`
does not read the new path, because its pattern takes `skills/`,
`templates/`, `docs/` and `agents/` paths only, and no archive file exists.

**The memo carries a section the template does not**, `## The gate change,
for the pull request`, copied from `phases/phase-3.md`, as the spawn asked.
No reader of `overview.md` matches section headings other than the five the
template has (`executed`, `git grep` of the headings over `*.py`).

**Each changed pin was seen red** (`executed`):

| S row | Case | Red |
|---|---|---|
| S13 | `tests/test_a_record_carries_no_comment.py::test_the_record_templates_are_found` | at 1b548e6c with the census widened and no `templates/process.md`: `assert 8 == 9` |
| S13 | `tests/test_a_record_carries_no_comment.py::test_a_comment_put_back_is_refused_at_its_line` | under `RECORD_TEMPLATES` narrowed back to `("sdd-*.md",)`, the old census: the planted `process.md` comment is not found |
| S13 | `tests/test_a_record_carries_no_comment.py::test_no_record_template_carries_a_comment` | under a comment written into `templates/process.md`: `templates/process.md:3` |
| S13 | `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block`, unchanged | under an emoji written into the template's header row |

**Mutations** (`executed`, `bin/mutation-check` after 756a59d3, each bounded
at 300 s and each ending `red`, the tree clean after each). The three
mutants in the last column above, each run over its one case: 3 red, 0
survived. The framer's line has no case to run a mutant over.

**The narrow checks** (`executed`). `bin/test
tests/test_a_record_carries_no_comment.py
tests/test_the_record_is_written_in_words.py
tests/test_every_agent_reads_the_contract.py -q`, the plan's Verified by,
returned 28 passed. The 58 test modules that name `templates/` or
`agents/framer.md`, run one at a time with `bin/test <module> -q`, exited 0
except `tests/test_chain_hooks_hardening.py`, whose one failure was
`test_every_spec_directory_that_reached_the_ladder_has_an_overview` naming
this work item before `overview.md` was written. With the records written,
18 modules that read the work item's records or the documents they cite,
`tests/test_chain_hooks_hardening.py`, `tests/test_unverified_check.py`,
`tests/test_gather_changelog.py`, `tests/test_chain_check.py` and
`tests/test_settle.py` among them, each exited 0 (1,180 passed).
`bin/unverified-check seal/specs/` and `bin/unverified-check --baseline
origin/main seal/specs/` exited 0, the first counting 48 overviews, 68 open
and 117 closed rows. `gather_changelog.py --version 0.23.0 --dry-run` exited
0 and printed this work item's fragment. `bin/test-layout --check` and
`--pairs` over the changed test file refused nothing and named no pair; it
declares no `TARGET`. `uvx ruff check` and `uvx ruff format --check` over it
report nothing.
