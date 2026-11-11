# Phase 4: 1794383427-asserts-pin-literal-phrases

## What this phase found

**The frame holds against the tree at `ce7463471`, except one sentence of
`frame/plan.md` *Overlap with the release*.** *The listing* of
`frame/design.md` gives 113 asserts, 19 absence asserts and 67 cases over
the 27 modules of group D at `18a7e18fb`, the counts of design *The
groups* (executed). The coordinates design G5 gives for
`tests/behaviour/test_no_document_names_the_old_roots.py` stand at the base
(read). The plan's #1486 row says phase 4 rules the other cases of
`tests/behaviour/test_a_release_publishes_its_note.py` after #1486's
rewrite. #1486 has not reached the branch or `origin/release/v0.37.4`
(executed: `git log --grep='#1486' HEAD` lists none, and
`git log HEAD..origin/release/v0.37.4` lists nothing). The phase ruled the
module as it stands at the base, and the case *Out* names stayed unread.
The sentence is the framer's to fold.

**One listed assert of group D left with the merge.** At the base the
group holds 112 asserts, 18 absence asserts and 66 cases (executed). The
merge at `ce7463471` brought #1524, the pull request of #1483, which removed
`test_the_workflow_is_not_a_step_of_the_release_job` of
`tests/behaviour/test_a_release_publishes_its_note.py`, with its absence
assert at `18a7e18fb`'s `:234` (executed, `git diff 18a7e18fb HEAD`). The
same merge removed `test_the_documents_name_the_ci_also_row` of
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, as phase 3
foresaw (executed: `git grep` finds the name under `tests/` at
`e2fc0cb74` and nowhere under `tests/` at `ce7463471`). That
case is group C's.

**S1, per module of group D.** The unit is one assert, a distinct
`path:line`, as in phases 1 to 3. The 112 asserts of the base add up as 52
kept, 17 removed and 43 not ruled (executed: the ledger summed against
*The listing* per module). The line numbers below are the base's. The
last column is *The listing* at `f25de2b52`. `63a48d5f9` changed only the
old-roots module's docstring after it, and the listing gives the same
totals there (executed).

| Module of `tests/behaviour/` | Listed | Kept | Removed | Not ruled | Listed at `f25de2b52` |
|---|---|---|---|---|---|
| `test_a_body_naming_two_issues_claims_one.py` | 3 | 3 | 0 | 0 | 3 |
| `test_a_cited_section_stands_in_its_file.py` | 2 | 1 | 0 | 1 | 2 |
| `test_a_commit_names_its_repository.py` | 5 | 5 | 0 | 0 | 5 |
| `test_a_declared_label_reaches_the_tracker.py` | 2 | 2 | 0 | 0 | 2 |
| `test_a_document_that_names_a_script_says_how_to_reach_it.py` | 3 | 0 | 0 | 3 | 3 |
| `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` | 3 | 3 | 0 | 0 | 3 |
| `test_a_phase_hands_the_next_one_a_record.py` | 10 | 10 | 0 | 0 | 10 |
| `test_a_probe_that_commits_says_so.py` | 4 | 3 | 1 | 0 | 3 |
| `test_a_reference_root_is_read_and_never_taken.py` | 1 | 0 | 1 | 0 | 0 |
| `test_a_release_publishes_its_note.py` | 7 | 6 | 0 | 1 | 7 |
| `test_a_release_rolls_the_flow_measurement_issue.py` | 3 | 0 | 3 | 0 | 0 |
| `test_a_section_marked_for_one_role_reaches_only_that_role.py` | 10 | 0 | 0 | 10 | 10 |
| `test_a_shrunken_corpus_declines_to_judge.py` | 1 | 0 | 0 | 1 | 1 |
| `test_a_signer_declares_its_pact.py` | 8 | 4 | 4 | 0 | 4 |
| `test_both_editions_carry_the_same_folds.py` | 6 | 1 | 2 | 3 | 4 |
| `test_evals_layout.py` | 1 | 1 | 0 | 0 | 1 |
| `test_every_shipped_agent_and_document_is_measured.py` | 1 | 0 | 0 | 1 | 1 |
| `test_no_document_names_the_old_roots.py` | 4 | 0 | 4 | 0 | 0 |
| `test_one_table_walker_reads_what_gfm_renders.py` | 1 | 0 | 0 | 1 | 1 |
| `test_settle_applies_rule_changes_in_place.py` | 1 | 1 | 0 | 0 | 1 |
| `test_the_contributor_has_a_procedure.py` | 5 | 5 | 0 | 0 | 5 |
| `test_the_gate_asks_the_range_ci_will_ask.py` | 6 | 0 | 2 | 4 | 4 |
| `test_the_old_block_leaves_through_update.py` | 4 | 1 | 0 | 3 | 4 |
| `test_the_release_check_watches_what_ships.py` | 8 | 1 | 0 | 7 | 8 |
| `test_the_release_seal_is_drawn.py` | 5 | 5 | 0 | 0 | 5 |
| `test_this_repository_passes_its_own_checks.py` | 7 | 0 | 0 | 7 | 7 |
| `test_unverified_rows_close.py` | 1 | 0 | 0 | 1 | 1 |
| Total | 112 | 52 | 17 | 43 | 95 |

The last column equals the kept count plus the not-ruled count in every
module. Of the 18 absence asserts, 9 were removed, 1 was kept and 8 were
not ruled. Each removed one held text or a design a shipped release
removed: `rule 8` in three agent definitions, the `Pact notify` key and
the `| Signer |` table, `every top-level` in `CONTRIBUTING.md`, the panel's
`from` row and its old sentence in `skills/code-review/orchestration.md`,
and the old-roots scan's `.specseal` and `OLD_ITEMS` in `lib/`.

The 43 not ruled read a program's output or a text the case built: the
findings of the marked-section walk, the reasons `decline_if_shrunken`
and the table walker give, the fold report's rows, the `seal rules`,
`seal layout` and `seal fold` output, the update step's stdout,
`disagreements()`, `base_spellings()`, the gate's panel, and the messages
the reach check raises (read).

**The step's printed lines in `test_the_release_check_watches_what_ships.py`
were not ruled, and this is a judgment the proofer reads (S2).** Seven
listed asserts read the `::error::` line and the skip line of the hygiene
step *a change to what ships must move the version*. The case reads them
from `.github/workflows/hygiene.yml` as text, which design *What an
assert reads* places among a file's text. They are also the lines the
step prints to a person, and contract rule 14 asks a case to pin such a
line. Phase 3 left `broad_gate.py`'s message constants unchanged on the
same grounds. The phase took the printed-line reading, so they stand as
they are. Read as file text, five would go as wording or a removed design
and the skip-line case would go with its last assert.

**Asserts outside the listing were ruled as well**, as design *Scope*
item 1 asks of each case that holds a listed assert. They are not in the
counts above.

- In `test_a_commit_names_its_repository.py`, the loop over
  `subprocess.run` and `An edit must be able to fail` absent from the
  rule went. The second is a bold lead of the neighbouring rule, which is
  wording. The first never stood in the rule (executed, `git log -S`), and
  no rule in force names that literal.
- In `test_a_reference_root_is_read_and_never_taken.py`, the `cite` entry
  of two readers, the `never writ` pattern and the `## Never` line of the
  framer's and the crafter's definitions went as wording. `stage 1` in the
  proofer's paragraph stays, as the stage of the review skill the proofer
  resolves.
- In `test_a_signer_declares_its_pact.py`, the count of `Pact notify` in
  the template went with the sentence it counted.

**Six kinds of decision recur, each judged against `frame/design.md` *The
criterion*.**

- A literal that is a fact is kept, with a comment directly above it that
  names the fact and its reader. Examples are a workflow's `needs` and
  `if` lines, a step's command, an environment binding, a permission, a
  path, a config key in a bold lead and a table row, a branch name a
  contributor fills in, and a rule number. A literal that held sentence
  words was cut to the fact: `` `git -C` `` in the contract, the bound
  ` 300 s ` and ` 300 seconds `, the citation of *Orchestrator: the order
  inside a ticket*, and `exits 0` in the contribution guide's table.
- An assert that carries #1233's comment stays as it stands. In group D
  those are `test_a_commit_names_its_repository.py:46`,
  `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:64`,
  `test_a_phase_hands_the_next_one_a_record.py:157`, `:172`, `:177` and
  `:205`, `test_a_probe_that_commits_says_so.py:38`, `:63` and `:78`, and
  `test_the_release_seal_is_drawn.py:54` to `:64` (executed, `git blame`
  on `c3e020961`'s lines). Two kept asserts carried a comment from another
  change: `test_a_commit_names_its_repository.py:87`, whose comment names
  the citation and its reader, stays; `test_a_phase_hands_the_next_one_a_record.py:211`,
  whose comment named the decision and not a fact, was cut to the
  citation and its comment rewritten.
- A literal that is a sentence or a word of a sentence is removed. Examples
  are `touches what`, `describes`, `predicted`, `not rewritten`, `due`,
  the `Pact notify` sentence of the config template, and the pairing
  rule's clause in `CONTRIBUTING.md`.
- An absence assert is kept only where a rule in force forbids its
  literal and the rule can be cited. Three stand, under *Absence asserts
  kept* below.
- A case left with no assert is removed (design *Scope* item 6). Two went:
  `test_no_definition_points_a_probe_at_the_retired_rule` and
  `test_the_tracker_doc_says_what_a_title_written_before_this_means`.
  Design *Scope* item 5 removed eleven more, the old-roots scan's cases,
  with `OLD_ROOT`, `KEEP`, `offenders`, `offenders_under`, `COVERED`,
  `DECLINES_COVERAGE`, `DECLINES_KEEP`, `uncovered`,
  `keep_entries_not_in_use` and the imports only they used (`re`,
  `build_tracked_tree`, `decline_if_shrunken`). `NEVER_LINE` and the `re`
  import of the reference-root module went too. No module was left with
  no case, and no module was deleted.
- A case whose name stated what a removed assert read is renamed for what
  it still reads. Five were renamed: `test_it_points_at_the_edit_rule`,
  `test_each_reader_points_at_the_row_and_names_where_it_cites_it`,
  `test_the_template_and_the_config_skill_carry_the_pact_row`,
  `test_the_contribution_guide_names_this_check` and
  `test_the_panel_prints_the_ref_on_the_base_row`. Each docstring that
  stated a removed assert was rewritten in place (design *Scope* item 7).

**Absence asserts kept.** Each comment cites the rule as the comment of
the workflow that states it, because neither rule stands in a policy
document. Each literal is a key or an expression the runner acts on.

- `${{ github.event.pull_request.body }}` absent from the `run:` block of
  the claims step. The rule is the comment above the step *every issue
  this pull request claims, and every one it only names* in
  `.github/workflows/hygiene.yml`: `${{ }}` inside `run:` is substituted
  into the shell script.
- `continue-on-error` absent from the `dist` job, and `persist-credentials`
  absent from its checkout. The rules are the header comment's paragraph
  on `dist` and the comment above the checkout in
  `.github/workflows/publish-release.yml`.

**One kept assert was narrowed, a departure from design *Scope* item 1,
which keeps or removes an assert and cuts its literal.** The claims
step's absence assert read `workflow.split("run:")[-1]`, the last `run:`
block of the whole workflow, which is another step's. `seal mutate` planted
the body in the claims step's own `run:` line, and the assert SURVIVED
(executed, `mutate8.txt`). The assert now reads `step.split("run:", 1)[1]`,
the `run:` block of the step its case already cuts, and the same plant
goes red on it (executed, `mutate11.txt`). It is committed alone at
`f25de2b52`, so the proofer reads it apart from the rulings. A body planted
in another step's `run:` block is now outside the assert, and the rule it
cites is the claims step's.

**These literals could be read either way, and the proofer reads each
against *The criterion* (S2).**

- The two workflow-comment rules above. Neither has a heading or a bold
  lead, which design *The criterion* asks a cited rule to carry. The phase
  read the step's name and the comment's opening as that coordinate.
- `stage 1` in `agents/proofer.md` was kept as a label. Read as words, the
  proofer's entry would keep `frame/design.md` alone.
- `'<' not in filled` in `test_a_release_publishes_its_note.py` was not
  ruled. `filled` is the checklist's `--title` value after the case fills
  its two placeholders, a text the case built from the document.
- `` `main` `` and `plugin.json` in the contribution guide's section were
  kept as the branch a contributor avoids and the file the refusal names.
- `exits 0` was kept as the exit code of the guard. Its row in the table
  is the sentence a maintainer reads.
- `behaviour/` in `evals/README.md` was kept as the directory a reader
  resolves.
- The parametrized `test_the_phase_record_path_is_spelled_the_same_in_every_prose_carrier`
  asserts the same path on the same two files as `:172` and `:187`. The
  design removes a second equal assert only within one case, so it stays
  with a comment.

**Check lines (design *Scope* items 8 and 9).** No check line outside
`docs/` names a module this phase left without a reader. The three in
`RULE_FILES` outside `docs/` that name a group D module,
`skills/implement/SKILL.md:214`, `skills/code-review/SKILL.md:127` and
`skills/writing-style/SKILL.md:267`, keep a case reading their rule (read).
No check line changed.

Under `docs/`, the two lines of design `## Rule changes`,
`docs/layout/one-root-by-lifetime.md:29` and
`docs/layout/one-root-by-lifetime.ko.md:29`, name the old-roots module,
which keeps no case reading their rule. One more line names a module
with no case reading its rule: `docs/layout/the-pact.md:39`, under **A
sentence is contract when another repository's code would be wrong if it
changed**, names `tests/behaviour/test_a_signer_declares_its_pact.py`.
None of that module's cases reads that rule, and none did at the base
either (read). The removed `| Signer |` assert read
`templates/setup/pact.md`, which the rule names, for a table the rule does
not mention. The phase edits no file under `docs/`. The framer folds the
line with phase 1's `docs/forms/the-round-record.md:107` and phase 3's
`docs/running/the-broad-gate.md:33`, both of which stand at `63a48d5f9`
(executed, `grep -n`).

Every other check line naming a module of group D keeps a case that reads
its rule (read). They are `docs/releasing/issues-and-milestones.md:187`
and `:293`, `docs/layout/one-root-by-lifetime.md:60` and the Korean
edition's `:57`, `docs/releasing/branch-and-release.md:48`, `:138` and
`:182`, `docs/forms/the-reader-registry.md:14`,
`docs/layout/the-record-layout.md:156`, `docs/running/the-agent-set.md:124`
and `:169`, `docs/running/the-broad-gate.md:76` and `:149`,
`docs/layout/the-pact.md:53` and `:67`, `docs/checks/the-fold.md:97`, and
`docs/releasing/release-checklist.md:250`. The list was made by `git grep`
on each module's path over every `check:` line outside `tests/`.

**A docstring outside the edited cases cited a removed helper, and was
rewritten (design *Scope* item 7).**
`tests/behaviour/test_both_editions_carry_the_same_folds.py:94` cited
`test_no_document_names_the_old_roots.py#uncovered`. It now states the
condition its own `unread` holds. `tests/test_conftest.py:257` to `:373`
passes the string "the KEEP allowlist's liveness check" to
`decline_if_shrunken` as a fixture reason. It names no unit, and nothing
resolves it, so it stands.

**The counts of design *The counts* (S7).** The two forms are the issue's,
by the commands of that table. *The listing* is the script of design *The
listing*.

| Count | At `18a7e18fb` | At `f25de2b52` |
|---|---|---|
| presence form | 388 | 306 |
| absence form | 134 | 17 |
| the listing | comparisons 735, asserts 696, absence asserts 151, cases 342, modules 72 | comparisons 477, asserts 456, absence asserts 23, cases 269, modules 66 |

All six cells are executed. The counts at `f25de2b52` include what the
release's own merges removed from the two directories:
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, 4 listed
asserts, and the two cases named above, all three by #1524, the pull
request of #1483. The `ba4d85629`
cells of the design reproduce (executed: 388 and 132).

**What was run, and what each run showed.**

- S1: executed, as above. The ledger, the listings at `18a7e18fb`, at the
  base and at `f25de2b52`, and the group split are in the phase's scratch
  directory.
- S4: `bin/seal rules --check` exits 0, "all 177 check lines in 69 rule
  files hold." (executed at `f25de2b52` and at `63a48d5f9`).
- S5: `git grep -n -w -F <name> -- . ':!seal/threads' ':!.test_durations'`
  over each removed case, each removed helper with a distinct name, each
  old case name and each `path#unit` of the old-roots module lists nothing
  at `f25de2b52` (executed). The same search finds the new name
  `test_the_panel_prints_the_ref_on_the_base_row` at its definition, so it
  can find a name that is present (executed). The generic names
  `offenders`, `uncovered`, `COVERED` and `KEEP` are matched elsewhere only
  as local names of other modules (read).
- S6: `grep -n '^def '` on the old-roots module lists `tracked`,
  `lines_naming_the_second_root`, `test_the_core_states_the_second_name_once`,
  `test_each_readme_states_the_second_name_on_one_line_of_shared_or_local`
  and `test_no_other_scanned_file_states_the_second_name` (executed). The
  `#1059` block and `tracked` are byte for byte the base's (executed,
  `diff`). `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`
  passes in the boundary set below.
- S9: the nineteen edited modules gave 209 passed before `9249b920a` was
  committed, over the same bytes (executed). The boundary set,
  `bin/test tests/text tests/behaviour -q`, gave 1788 passed and 8
  skipped at `63a48d5f9` with this record, `gaps.md`, `changelog.md` and
  the Status cell in the tree (executed). `tests/text/` and
  `tests/behaviour/` are the tree-wide files and hold every module that
  reads an edited one. No module outside them imports from an edited
  module (executed, `git grep`).
- Mutation: `seal mutate` ran over each cut literal and each kept absence,
  in the file it pins and with its case. Each went red on the assert that
  names it (executed, failing line read): `` `git -C` `` in the contract,
  `300 s` in the crafter's definition, `300 seconds` in
  `skills/verify/seal-mutate.md`, the ticket citation in
  `skills/implement/SKILL.md`, `exits 0` in `CONTRIBUTING.md`, `stage 1` in
  the proofer's definition, the body planted in the last `run:` block and
  then in the claims step's own, `continue-on-error` planted in the `dist`
  job and `persist-credentials` planted in its checkout. The one SURVIVED
  run is the narrowing above. The tree was clean after each restore
  (executed, `git status --short`).
- S2 and S3 are the proofer's at review.
