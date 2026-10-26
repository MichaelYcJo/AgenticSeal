# Phase 1: 1793051803-settle-runs-in-local-mode

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | e1815c53 |

## What this phase was asked

`settle` and `settle --apply` run in local mode, built against `spec.md`
*In* items 1 to 11: the refusal goes, the work items are read and removed
under the directory holding the resolved root, released is asked of `gh`
with the three unreleased states and the `gh` refusal, each spec is read
from its directory, the merge-commit order goes into `rule_changes.py`, and
the dry run gains its local lines and the settled local root. In the same
commits, `settle.py`'s docstring and `skills/settle/SKILL.md` state it, with
the three limits. Q1 builds on its default, `gh` alone. Each S row's case is
seen red before it goes green. A `gh` stub on `PATH` works on Windows too,
and `.test_durations` prices no removed case.

## What this phase found

**The frame holds, with one placement it names wrongly** (`read`). Every
coordinate in `plan.md` *Technical context* is where it says:
`settle.py#main`'s local-mode branch, `optin.py#home_at`,
`unverified_check.py#open_record_rows` joining its directory under the root
it is handed, `policy_root` reading a local `config.md` through `home_at`,
`routing.py#parse` reading the `Branch` row, and `rule_changes.py#_ancestor`.

- **S2's case for the new ordering function is in `tests/test_settle.py`,
  not `tests/test_rule_changes.py`.** `tests/test_rule_changes.py`'s
  docstring says the cases that read merge order and ancestry "run `settle`
  over a repository and are in `tests/test_settle.py`", and the case of
  `rule_changes.py#order` stands there in `Test_module`. The new case,
  `test_merge_order_of_local_specs_is_their_merge_commits_place`, stands
  beside it. This divergence goes to `overview.md` in phase 2.
- **`_ancestor` is not shared.** It answers False when its two commits are
  equal, so a `--released-at` given as the merge commit's own hash would
  read as not reaching it. `settle.py#reaches` asks
  `git merge-base --is-ancestor <commit> <ref>` itself.

**The choices the frame left to the build** (the work):

- The dry run's local lines. The first line is `local mode: the seal/ root
  is <path>, under the git directory`. A `released in local mode` list gives
  `<id>  pull request #<n>  merge commit <oid>`, and an `unreleased in local
  mode and untouched` list gives `<id>  <why>`. The three reasons read: "no
  `routing.md` names a branch in its `Branch` row, so `gh` was not asked";
  "no pull request from `<branch>` has merged"; and "`<ref>` reaches no merge
  commit of the pull requests from `<branch>` that merged: #<n> at <oid>".
  The removal heading in local mode adds "In local mode no commit holds these
  directories; `seal export` takes a copy for whoever wants one". An
  unordered pair says "no ancestry orders their pull requests' merge
  commits". This line is a second constant, `UNORDERED_LOCAL`, so that the
  shared-mode cases stay as they were (S6). Each shape is pinned in
  `tests/test_settle.py`.
- The settled local root says `settle: <path> is the seal/ root, in local
  mode, and its specs/ holds no work item`, with no fresh-checkout clause.
- The `gh` refusal is one sentence, `UNASKED`, naming `gh`, what it said,
  and the limit "a repository on a host `gh` cannot ask cannot settle in
  local mode". Three answers are refused: `gh` absent from `PATH`, a query
  that exits non-zero, and an answer at exit 0 that is not a list. The third
  would produce the same silent zero as the first two.
- `gh` is found with `shutil.which` and run by the path it returns, as
  `chain_check.py#pull_request_from_gh` does, so a `gh.cmd` on Windows is
  run. The query is bounded at `GH_TIMEOUT`, 60 s. A timeout is a refusal.
- A listed pull request whose `mergeCommit` is null counts as no merged pull
  request. Where several merged pull requests come from one branch, the
  first one `gh` lists whose merge commit the ref reaches is taken.
- In local mode `--released-at` is checked with `git rev-parse --verify`
  before `gh` is asked, so a ref that does not resolve gets the existing
  refusal and `gh` is never asked.
- A `routing.md` whose `Review` or `Destination` row is unreadable parses to
  nothing in `routing.py#parse`, even with a `Branch` row. Such a work item
  reads as naming no branch.
- `--released-at`'s help text names the local-mode meaning (contract rule
  19).
- The local cases run `main` in process with a `gh` stub first on `PATH`: a
  Python script behind a `gh` shell wrapper, or a `gh.cmd` on Windows, as
  `tests/conftest.py#_write_gh_stub` writes them. It answers from a JSON file
  beside it and logs each call. The absent `gh` is the module constant `GH`
  set to a name no directory holds, since `git` and `gh` share `/usr/bin` on
  a CI runner and `PATH` cannot drop one alone.

**A layout refusal shaped one name** (`executed`). `test-layout --check`
refuses a class with no `test_refuses_` case. The removed local-mode refusal
was `Test_main`'s only one, so the `gh` case is named
`test_refuses_a_gh_that_cannot_be_asked_in_local_mode`.

**The cases were seen red against `b61eb0c6`** (`executed`, `bin/test
tests/test_settle.py tests/test_settle_reads_before_it_removes.py -q -p
no:xdist`, with the new cases written and the code as it stood). 17 cases
failed there: S1, the pinned texts, S2's two cases and the new
`merge_order` case, S3, S4, S5's four, S7, S9, S8's two, the `ROUTING`
sibling case and S10. S6, `test_shared_mode_never_asks_gh`, passed there,
since shared mode never asked `gh`. It went red under the mutant that sends
shared mode down the local branch of `survey`. The five cases `e1815c53`
adds were found by mutants that survived the first cases' reading. Each was
seen red under its mutant: the ref check, the answer that is not a list, the
null merge commit, the per-branch cache and the row's path in the local
directory.

**Mutations** (`executed`, `mutation-check`, each run bounded at 300 s, over
`bin/test tests/test_settle.py -q -p no:xdist -x`): `settle.py` 26 mutants,
26 red. They cover `reaches`, `resolves`, each refusal in
`merged_pull_requests`, `declared_branch`, the cache and the three reasons
in `released_local`, `records_of`, the ref check in `survey`, the spec read
and the order in `timeline`, the local lines in `report`, the records root in
`apply`, `open_rows` and `in_tree`, the settled local root and the refusal's
exit in `main`. `rule_changes.py#merge_order` 2 mutants, 2 red. The tree was
clean after each batch.

**The narrow checks** (`executed`, exit 0): `bin/test tests/test_settle.py
tests/test_rule_changes.py tests/test_settle_reads_before_it_removes.py
tests/test_settle_applies_rule_changes_in_place.py
tests/test_docs_line_wrap.py
tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_rules.py
tests/test_a_shrunken_corpus_declines_to_judge.py
tests/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/test_a_reference_root_is_read_and_never_taken.py
tests/test_censuses.py tests/test_unverified_rows_close.py
tests/test_one_heading_rule_holds_to_commonmark.py tests/test_launch.py
tests/test_the_rules_command_reads_each_rule_off_its_test.py -q` returned 513
passed and 8 skipped at `3ae07972`. After `e1815c53`, `bin/test
tests/test_settle.py -q -p no:xdist` returned 68 passed. `uvx ruff check`
and `uvx ruff format --check` over the changed Python files report nothing,
and `test-layout --check` and `--pairs` over the changed test files report
no refusal and no pair.

**`.test_durations`** (`executed`): the entries of the two removed cases,
`Test_main::test_refuses_local_mode_rather_than_reading_an_empty_repository`
and `test_the_module_and_the_skill_both_say_local_mode_is_refused`, are
gone, and the file still parses as JSON. The new cases are unpriced until
the next refresh from a `tests` run.
