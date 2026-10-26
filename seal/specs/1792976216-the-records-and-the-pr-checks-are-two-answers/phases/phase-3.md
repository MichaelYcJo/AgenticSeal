# Phase 3: 1792976216-the-records-and-the-pr-checks-are-two-answers

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 41d87aba |

## What this phase was asked

Build phase 3 of `plan.md`, the reframe after review round 3 (framer's commit
`eeccf30a`, approved at `e3b321ad`), as the build's last phase. Plant in
`tests/test_chain_check.py` `Test_retired` the case for the no-root test's
fifth answer: under `--worktree`, a switch to local mode run and not
committed leaves no `seal` in the working tree, so nothing is declared. Show
it red against `gone = False` in the `if WORKTREE:` arm first. Run S9: drop
each of the test's five answers by a mutant in turn and name the case that
kills each. Run S8's applied half: replay the spec's 17 rule-change items onto
`docs/` at `02ee12de` in a scratch clone, run the modules whose code names a
changed document, `README.md`, `README.ko.md` or `docs/`, then run them again
with `docs/` restored. Write `overview.md` from `templates/sdd-overview.md`.
Change no source file and no changelog line. Where the replay or a mutant
fails, record it here and in the hand-back, and leave `spec.md`, `docs/` and
`rounds/` alone. Build on the open questions' defaults: Q2 waits for the pull
request's Windows run, and Q4 is (a), no new gate.

## What this phase found

**The frame holds** (`read`). `chain_check.py#main` holds the no-root test at
lines 2192 to 2196 at `e3b321ad`, and no file under `skills/` or `tests/`
changed between `2f41bbf9` and `e3b321ad`. `Test_retired` stood at line 3359.
`docs/` is unchanged between `02ee12de` and `e3b321ad`, so the policy in force
is still `docs/` at `02ee12de`. The spec's `## Rule changes` holds 17 items,
as the plan's row says.

**The new case was seen red before it was committed** (`executed`). Round 3
finding 2's draft went into `Test_retired` unchanged, after the CI case of
the same test. `bin/mutation-check skills/code-review/scripts/chain_check.py
--replace "        gone = not os.path.lexists(os.path.join(root, home))"
"        gone = False" --tests "bin/test tests/test_chain_check.py -q -p no:xdist
-k test_accepts_under_worktree_a_root_the_working_tree_no_longer_has"` passed
the case against the file as it was and then printed `red`. The case failed at
`assert code == 0`: the check judged the deleted declaration of the earlier
work item and printed "git does not carry this file at HEAD". After that,
`bin/test tests/test_chain_check.py tests/e2e/teammate tests/test_unverified_check.py -q`
gave 604 passed. Round 3 saw 603 there, and the one more is the new case.

**Every answer of the no-root test now has a case** (`executed`). Each
mutant ran once through `bin/mutation-check` with `bin/test
tests/test_chain_check.py -q`, and the tool restored the file and compared its
hash after each run. All five printed `red`:

| Answer dropped | Mutant | Cases that failed |
|---|---|---|
| HEAD without the entry | the CI arm reads `gone = False` | `Test_retired::test_accepts_every_declaration_leaving_with_the_root` |
| HEAD with the entry | the CI arm reads `gone = git(...) is not None` | 33 cases, among them the three parameters of `Test_retired::test_refuses_a_declaration_deleted_with_nothing_absorbing_it`, `Test_retired::test_accepts_a_declaration_a_settle_removed` and 11 cases of `Test_main` |
| git not answering | the CI arm reads `gone = not git(...)` | `Test_retired::test_accepts_every_declaration_leaving_with_the_root`, in its monkeypatched half |
| under `--worktree`, the working tree without the entry | the `if WORKTREE:` arm reads `gone = False` | `Test_retired::test_accepts_under_worktree_a_root_the_working_tree_no_longer_has`, the case this phase added |
| under `--worktree`, the working tree with the entry | the `if WORKTREE:` arm reads `gone = True` | `Test_retired::test_judges_a_root_the_working_tree_has_under_worktree`, `Test_retired::test_judges_the_declarations_where_the_working_tree_has_seal_as_a_file` and `Test_rule_changes_read::test_refuses_the_working_tree_under_worktree_and_reads_head_otherwise` |

No mutant survived, so S9 added no case beyond the planned one.

**S8's applied half holds** (`executed`). In a scratch clone at `41d87aba`,
`rule_changes.py#parse` read the 17 items with no error, and
`rule_changes.py#replay` applied them as one spec, in order, with nothing
refused. That is the loop `settle --apply` runs, `apply_op` per item. Six
documents changed. The probe chose the test modules whose source names
`docs/`, `README.md`, `README.ko.md` or the base name of a changed document:
112 modules. Round 3's selection read only path-like string constants and
found 77. This phase did not compare the two lists, because round 3's probe
was removed. Over the applied `docs/` they gave 1
failed, 4432 passed and 14 skipped. With `docs/` restored from the clone's
commit they gave the same: 1 failed, 4432 passed, 14 skipped. The one failure
in both runs is
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
because the clone was taken before `overview.md` existed. With `overview.md`
in place in this checkout, `bin/test tests/test_chain_hooks_hardening.py -q`
gave 26 passed. `tests/test_docs_line_wrap.py` passed over the applied
`docs/`, so the wrap the reframe took from round 3 finding 1 holds.

**The parse half holds** (`executed`). `python3
skills/code-review/scripts/chain_check.py --baseline release/v0.22.4` exited
0 at `41d87aba` and named no `## Rule changes` problem. It printed the notices
owed at this point: the pull request's state unknown with no pull request
open, the last round's `target:` behind HEAD because `41d87aba` touches
`tests/test_chain_check.py` (a verifying round is owed), and no
`broad-gate.md` and no `guarantee.md` yet.

**`overview.md` passes its reader** (`executed`). `bin/unverified-check` over
this work item's directory read one overview with 3 open rows and exited 0.
