# Phase 2: 1792993972-settle-writes-each-sections-latest-decision

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 0dc1087a |

## What this phase was asked

CI reads a whole removal of a directory that stood at the base as a settle:
`unverified_check.py#settled` and `chain_check.py`'s texts change as the plan
says, with the cases S6, S7 and S9 seen red first. Phase 2 is the last phase,
so it also writes `overview.md` and the changelog fragment from the
repository's templates. Q2 builds on its default: this item's pull request
says `Part of #1033`.

## What this phase found

**The frame holds for the predicate and its texts, and not for S8**
(`read`, then `executed`). S8 says `test_refuses_a_removal_no_settle_explains`
and the fewer-rows cases pass unchanged. They cannot: under *In* item 4 a
directory removed whole is a settle, and four cases held whole removals as
deletions. `overview.md` names each and what it became. What stays a deletion
is a removal of part of a directory: a memo removed from a directory that
stays, a `routing.md` deleted beside a `spec.md` that stays, and a row
dropped from a table. A renamed directory now reads as the old one settled,
and its rows are read where it went.

**`settled` is one line** (the work). `settled(root, ref, directories)`
returns the directories that hold a file at `ref`; its two readers already
pass only directories gone from the head side, and `chain_check.py#retired`
no longer hands it a `here`. `wrote_a_spec`, `policy_documents`, the `SPEC`
constant and the `merged` fixture went with their last reader, and so did
`rule_changes.py#replay`, `apply_op` and `_cut`, which phase 1 had to leave
for `settled`.

**The texts a person reads, each pinned** (the work, contract rule 14):

- `settled: the directory stood at <base> and is gone whole, which reads as
  a settle`, the notice of `unverified-check --baseline`;
- `retired: a settle — the work item's directory stood at the merge base and
  is gone whole`, `chain_check.py#SETTLE_SAYS`;
- `` `## Rule changes` does not parse, so `settle` cannot group this spec by
  the sections it names and the settle has to read it whole: <reason> ``,
  `chain_check.py#RULE_CHANGES_SAYS`;
- the `--baseline` help's "a work item directory that stood at the merge base
  and is gone whole, which reads as a settle", and the module docstring's
  *fewer rows* entry.

A mutation of `SETTLE_SAYS` survived the first cases, because
`Test_retired` compared the output with the constant itself; `0dc1087a` pins
the words, and the mutant is now red. The help and the docstring had no case;
`0dc1087a` adds one.

**The cases were seen red against `0408fccf`** (`executed`). The rewritten
`tests/test_unverified_check.py` and `tests/test_chain_check.py`, copied into
a scratch clone at `0408fccf`, fail 13 cases there: S6 at the predicate and
at `--baseline`, S7, S9's three, S6 at `chain-check` in both its shapes, the
whole-removal shapes that now settle, and the help pin. The S8 cases pass
there and here, as a kept behaviour should.

**Mutations** (`executed`, `mutation-check`, each run bounded at 300 s):
`unverified_check.py` 3 mutants, 3 red; `chain_check.py` 3 mutants, 2 red and
`SETTLE_SAYS` survived, then red after `0dc1087a`. Phase 1's units:
`rule_changes.py` 5 of 5 red, `settle.py` 14 mutants, 13 red, and the
bare-name lookup red after `a8e6a2f9`.

**The narrow checks** (`executed`, exit 0): `bin/test
tests/test_unverified_check.py tests/test_chain_check.py tests/test_settle.py
-q`, 636 passed; and the modules beside them, `tests/test_rule_changes.py`,
`tests/test_settle_reads_before_it_removes.py`,
`tests/test_settle_applies_rule_changes_in_place.py`,
`tests/test_unverified_rows_close.py`, `tests/test_launch.py`,
`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`tests/test_the_pull_request_language_is_the_repositorys.py`,
`tests/test_rules.py`, `tests/test_docs_line_wrap.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/test_a_reference_root_is_read_and_never_taken.py` and
`tests/test_censuses.py`, 525 passed and 8 skipped. `uvx ruff check` and
`uvx ruff format --check` over the changed Python files, and `test-layout
--check` over the changed test files, report nothing.
