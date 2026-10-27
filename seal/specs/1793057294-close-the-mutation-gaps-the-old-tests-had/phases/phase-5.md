# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 8ef4f419 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 5 only: the rows of #1017 for
`skills/code-review/scripts/chain_check.py`, `skills/implement/scripts/seal.py`,
`skills/settle/scripts/settle.py`, `skills/settle/scripts/rule_changes.py` and
`evals/scripts/seed_defects.py`. Follow the method and table shape of phases 1
to 4: rebuild each row at the head with `bin/mutation-check` and `-x`, run a
survivor again against the other test files that load the module, write a case
only where it survives all of them, and see each new case red alone under its
mutant. Raise `--timeout` for `chain_check.py` where its baseline nears 300 s.
`settle.py` and `rule_changes.py` were rewritten after #942 measured them, so
many of their rows may have left the tree; record each such row with the
commit that removed or rewrote its code. One commit per module that needs one,
then this record and phase 5's Status in `plan.md`. Build on `questions.md`'s
defaults Q1 to Q5. Fake every decision that reads the platform.

## The outcomes

18 rows, rebuilt as 16 mutants. 12 rows are killed by a new case, 2 were
already closed, 2 are equivalent, and 2 left the tree. No row is a finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent | Left the tree |
|---|---|---|---|---|---|---|---|
| `skills/code-review/scripts/chain_check.py` | d94c5e99 | 5 | 5 | 4 | 0 | 1 | 0 |
| `skills/implement/scripts/seal.py` | none | 1 | 1 | 0 | 0 | 1 | 0 |
| `skills/settle/scripts/settle.py` | a8886e23 | 6 | 4 | 2 | 2 | 0 | 2 |
| `skills/settle/scripts/rule_changes.py` | 8ef4f419 | 1 | 1 | 1 | 0 | 0 | 0 |
| `evals/scripts/seed_defects.py` | 6da752f2 | 5 | 5 | 5 | 0 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`. A `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline.

The before column is the module's batch with `-x -p no:xdist` in `--tests`,
first against the module's own test file at 52365dda, then, for each survivor,
against every other test file that names the module, found with
`git grep -l` over `tests/`. The other files are listed above each table. Where
a batch over other files ran after this phase's cases were written, those
cases were deselected by name, so each batch ran the cases that stood at
52365dda. The chain_check batch over other files ran with pytest-xdist on and
deselected
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which fails until phase 7 writes `overview.md`. The after column is the same
batch against the module's own file at the module's commit. Every batch passed
its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`,
or with the case's node id in single quotes for a parametrized one. Each of
those runs printed `red: the cases failed against the mutation (exit 1)` and
exited 0, so its baseline passed against the code. Each failure was the case's
own assertion, except sd2's, whose mutant raises `IndexError` in the case
(*What this phase found*).

## `skills/code-review/scripts/chain_check.py`

Records: the issue body's k12, `phases/phase-5.md:503` and `:513`, re-run at
`phases/phase-6.md:1267` and `:1277`, and g17 and g18, `phases/phase-6.md:1274`
to `:1277`, all at `79f9c3fd`; the round 10 comment's c3 and c4,
`phases/phase-7.md:556` and `:557` at `9ca0867e`. Before:
`tests/test_chain_check.py`, then
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_moved_rule_leaves_its_definition.py tests/test_a_phase_hands_the_next_one_a_record.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_signer_declares_its_pact.py tests/test_broad_gate.py tests/test_broad_gate_rule.py tests/test_chain_hooks_hardening.py tests/test_ci_gives_the_checks_what_they_need.py tests/test_config.py tests/test_conftest.py tests/test_coordinates.py tests/test_every_reader_ends_a_line_where_gfm_does.py tests/test_first_setup_asks_once.py tests/test_gate.py tests/test_one_word_one_meaning.py tests/test_release_hygiene.py tests/test_replay_targets.py tests/test_seal_stamp.py tests/test_the_direct_answer_owes_the_sealers_record.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_the_sealer_guarantees.py tests/test_unverified_check.py tests/test_unverified_rows_close.py`,
which run 1,752 passed and 9 skipped on the code. The own-file batches ran with
`--timeout 1500`, the other-file batch with `--timeout 2400`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| k12: `reopened_of` reads its value against the `regression:` row | `'    found = as_row(REOPENS_ROW, value)'` `'    found = as_row(REGRESSION_ROW, value)'` | SURVIVED, every file | SURVIVED | equivalent: `finding_of` is the one caller, and it hands `reopened_of` only the value of a line the `reopens:` shape already matched whole. The `regression:` shape is that shape with its `#<n>` made optional, and both name the groups `round` and `finding`. So every value the caller can hand matches the `regression:` row with the same two groups, and `reference` returns the same pair. Both shapes are read from the shipped `docs/the-review-record.md` at import, never from the repository under check |
| g17: `declared_for_this_branch` takes two committed declarations naming the branch | `'    if len(matching) > 1:'` `'    if False:'` | SURVIVED, every file | red, `Test_declared_for_this_branch::test_refuses_two_committed_declarations_naming_the_branch` | killed by a new case |
| g18: `declared_for_this_branch` reads a detached HEAD as a branch | `$'    if not branch:\n        return [], (\n            "the branch could not be read'` `$'    if False:\n        return [], (\n            "the branch could not be read'` | SURVIVED, every file | red, `Test_declared_for_this_branch::test_refuses_a_detached_head_with_no_head_ref_as_no_branch` | killed by a new case |
| c3: `tracked_declarations` lists the whole tree, not `seal/specs/` | `'out = git(root, "ls-tree", "-r", "-z", "HEAD", "--", f"{routing.WORK_ITEMS}/")'` `'out = git(root, "ls-tree", "-r", "-z", "HEAD")'` | SURVIVED, every file | red, `Test_declared_for_this_branch::test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy[a-routing-md-outside-the-work-items]` | killed by a new case |
| c4: `tracked_declarations` parses every file listed, not `routing.md` alone | `'        if os.path.basename(path) != routing.FILENAME:'` `'        if False:'` | SURVIVED, every file | red, `Test_declared_for_this_branch::test_accepts_the_one_routing_md_under_the_work_items_beside_a_decoy[another-file-of-a-work-item]` | killed by a new case |

## `skills/implement/scripts/seal.py`

Records: the issue body's s47, `phases/phase-5.md:715` and `:730` at
`79f9c3fd`. Before: `tests/test_seal.py`. The other files that name the module
were not run, because the reading below shows no input tells the two apart.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| s47: `import_` catches no `NotImplementedError` from `testzip` | `'except (zipfile.BadZipFile, RuntimeError, NotImplementedError) as bad:'` `'except (zipfile.BadZipFile, RuntimeError) as bad:'` | SURVIVED on `tests/test_seal.py` | SURVIVED, the file is unchanged | equivalent: `NotImplementedError` is a subclass of `RuntimeError` (`executed`, `issubclass` in this worktree's interpreter), and `RuntimeError` stands in the same clause, so every exception the longer clause catches the shorter one catches too |

## `skills/settle/scripts/settle.py`

Records: the round 3 comment's st10, st13, st25 and st27,
`phases/phase-6.md:1742` at `fc4f81ae`, and the round 10 comment's s4 and s5,
`phases/phase-7.md:568` and `:569` at `9ca0867e`. Before: `tests/test_settle.py`,
then
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_routing.py tests/test_rule_changes.py tests/test_settle_applies_rule_changes_in_place.py tests/test_settle_reads_before_it_removes.py tests/test_unverified_rows_close.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| st10: a row open at the base is not read for a spec | no mutant | not run | not run | left the tree: `91d57028` (#1035, closing #1033) removed `rule_plan`, the one place that asked `open_record_rows` of the merge base for a spec, with the merge base itself. At the head every `open_record_rows` call reads the working tree, `None` in place of a base. Found with `git log -S 'open_record_rows(root, base, directory)' -- skills/settle/scripts/settle.py` |
| st13: a count of one is written plural | `'        f"released at {ref}: {total} work item{plural(total)}; "'` `'        f"released at {ref}: {total} work items; "'` | red on `tests/test_settle.py`, `Test_main::test_local_mode_lists_a_released_and_an_unreleased_item` | red, the same case | already closed |
| st25: an abbreviated name is read as any id | `'            return bool(stem) and work_item_id.startswith(stem)'` `'            return bool(stem)'` | red on `tests/test_settle.py`, `Test_report::test_the_report_lists_what_an_apply_would_remove` | red, the same case | already closed |
| st27: a directory kept at the base with nothing open gets no line | no mutant | not run | not run | left the tree: `91d57028` removed `write_rule_kept`, whose `if not rows and base` branch wrote that line, with `rule_arm` and the heading for a directory kept at the base. Found with `git log -S 'the rule does not hold at' -- skills/settle/scripts/settle.py` |
| s4: `tracked_text` scans `seal/specs/` too | `'        if not rel or rel.startswith(SPECS + "/"):'` `'        if not rel:'` | SURVIVED, every file | red, `Test_tracked_text::test_refuses_a_file_under_the_work_items_and_a_binary_file` | killed by a new case |
| s5: `citations` counts a `tests/` file naming `specs` as a reader of `seal/specs` | `'        if rel.startswith(TESTS) and SPECS in text:'` `'        if rel.startswith(TESTS) and "specs" in text:'` | SURVIVED, every file | red, `Test_citations::test_refuses_a_tests_file_naming_specs_alone_as_a_reader` | killed by a new case |

## `skills/settle/scripts/rule_changes.py`

Records: the round 3 comment's r4, `phases/phase-6.md:1742` at `fc4f81ae`.
Before: `tests/test_rule_changes.py`, then
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/test_a_language_section_of_writing_style_opens_alone.py tests/test_a_phase_hands_the_next_one_a_record.py tests/test_chain_check.py tests/test_settle.py tests/test_settle_applies_rule_changes_in_place.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_unverified_check.py tests/test_waiver_decided_at_start.py`,
835 passed and 8 skipped under the mutant.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| r4: `parse` reads a second section | `'    if len(found) > 1:'` `'    if False:'` | SURVIVED, every file | red, `Test_parse::test_refuses_a_second_section_at_its_heading` | killed by a new case |

## `evals/scripts/seed_defects.py`

Records: the round 3 comment's sd2, sd3, sd6, sd8 and sd9,
`phases/phase-6.md:1746` at `fc4f81ae`. The module is unchanged since then
(`executed`, `git diff fc4f81ae HEAD --stat`). Before:
`tests/test_seed_defects.py`, then
`tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_replay_targets.py`,
which run 15 passed on the code.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| sd2: a commit adding no work item is taken | `'    if len(items) != 1:'` `'    if len(items) > 1:'` | SURVIVED, every file | red, `Test_target_of::test_refuses_a_squashed_pull_request_with_no_round_1_to_seed[adds-no-work-item]` | killed by a new case |
| sd3: a commit with no round 1 is taken | `$'    if not first:\n        return None, "holds no round 1 record"'` `$'    if False:\n        return None, "holds no round 1 record"'` | SURVIVED, every file | red, `Test_target_of::test_refuses_a_squashed_pull_request_with_no_round_1_to_seed[holds-no-round-1-record]` | killed by a new case |
| sd6: a seed is found inside a string | `'if text.count(old) == 1 and (line, TOKEN[old]) in code:'` `'if text.count(old) == 1:'` | SURVIVED, every file | red, `Test_seed::test_refuses_a_line_no_seed_may_take[inside-a-string]` | killed by a new case |
| sd8: a line whose text occurs twice is seeded | `'            if source.count(text) != 1:'` `'            if False:'` | SURVIVED, every file | red, `Test_seed::test_refuses_a_line_no_seed_may_take[whose-text-occurs-twice]` | killed by a new case |
| sd9: a line in no unit is seeded | `$'            if not unit:\n                continue'` `$'            if False:\n                continue'` | SURVIVED, every file | red, `Test_seed::test_refuses_a_line_no_seed_may_take[outside-any-unit]` | killed by a new case |

## What this phase found

**The two rewrites the spawn named are #1033 and #955, and only the first
removed rows.** `plan.md` names the commits `91d57028` and `fa7d1374`, and the
spawn named their issues. `91d57028` is #1035, which closed #1033, and
`fa7d1374` is #1036, for #955 (`executed`, `git show -s`). `91d57028` removed
the merge base from settle, and st10 and st27 with it. `fa7d1374` added local
mode and left every row's code standing. Of rule_changes' one row and
settle's four other rows, each decision still stands at the head.

**st13 is one reading of four places (Q1).** The settle #942 measured printed
one count through `plural` in its report, the count of released work items.
The head's report prints four counts through `plural`, and the pair sits on
the first line's count of released work items, which is the count the old
report had. It is red on a local-mode case, which reads `1 work item` for one
released item.

**sd2's mutant raises rather than takes.** With `!= 1` read as `> 1`, a
squashed pull request that adds no `routing.md` goes on to `items[0]`, and
`target_of` raises `IndexError`. The row's sentence says the commit is taken.
The new case is red by that exception, since it asserts the commit is left out
with the count. No narrower pair realises "a commit adding no work item is
taken", because every path past the count reads `items[0]`.

**g18's case pins a sentence, because the sentence is all the mutant
changes.** Under the mutant a detached HEAD still matches no declaration, so
the list is empty either way. The mutant's why tells the person that nothing
declared the branch and names an empty branch, "declares ``". The case asserts
the why's opening words, "the branch could not be read", which is what the
person reads (contract rule 14).

**`bin/test-layout --pairs` named sd2's and sd3's first cases as one pair, so
they are one parametrized case.** Each parameter was seen red alone on its own
mutant, by node id. The other new cases read the same way: c3 and c4 are one
accepts case over two decoys, a `routing.md` in a team's own `specs/` and a
work item's `notes.md` holding a declaration's text, and each decoy is red on
its own mutant alone. sd6, sd8 and sd9 are one refusal case over three
sources, each putting the line no seed may take before the line that takes it.

**Each new function class holds both kinds of case.** `Test_seed`,
`Test_tracked_text` and `Test_citations` are new, and `bin/test-layout
--check` asks each for an accepts case and a refuses case. Each accepts case
reads an input its group did not: a line two operators could take, a file
nobody committed, and a line citing one work item twice.

**One module got no commit, because its row needed no case.**
`skills/implement/scripts/seal.py`'s one row is equivalent. `plan.md` says each
module lands in one commit, and this record is where its outcome stands.
Phase 7's `overview.md` can carry it as a divergence, as phase 3's three.

**The two equivalent rows each leave a name no input reaches on its own.** In
s47, `NotImplementedError` beside `RuntimeError` catches nothing the clause
does not already catch. The comment above it keeps the name as the record of a
traceback measured on 2026-09-03. In k12, `reopened_of` reads its value
against the `reopens:` row whole, a match `finding_of` has already made on
the line. Under `CLAUDE.md` *The rule a mechanism is kept against*, either may
be one to remove rather than keep. Removing either changes shipped code, which
`spec.md` *Out* leaves out of this work, so phase 7 can carry both into
`overview.md` for the repository owner to decide.

**No row was closed by giving an existing case a fixture, and no case fakes a
guarantee the real dependency gives (contract rule 13).** Every new case runs
the real git in a scratch repository. The g18 case detaches HEAD with git and
removes `GITHUB_HEAD_REF` from the environment, which is how a workflow with
no pull request ref meets the check. The settle and seed cases compare what
they read from disk or from git as text, so a CRLF checkout on Windows gives
the same verdict.

**`chain_check.py`'s baseline stayed well under the bound here, and the
batches passed one above it anyway.** Its own-file baseline took 59.9 s with
`-p no:xdist`, and 112.9 s at the after batch while other runs shared the
machine. `.test_durations` prices the file at about 261 s on Windows
(`plan.md` *Technical context*), so the own-file batches ran with
`--timeout 1500` and the other-file batch with `--timeout 2400`. No run timed
out.

**Run for the phase** (`executed`, at 8ef4f419):
`bin/test tests/test_chain_check.py tests/test_seal.py tests/test_settle.py tests/test_rule_changes.py tests/test_seed_defects.py -q`
exited 0, 794 passed. `bin/test-layout --check` over the five files reads 5
files with 0 refused. `--pairs` prints 1 pair, `tests/test_seal.py::Test_pinned`'s
two cases, which this phase did not touch. `uvx ruff check` and
`uvx ruff format --check` over the four changed test files exit 0.
`git diff 52365dda 8ef4f419 -- tests` removes no line holding `def test_`.
