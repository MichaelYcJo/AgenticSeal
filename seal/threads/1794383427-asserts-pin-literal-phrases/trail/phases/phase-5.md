# Phase 5: 1794383427-asserts-pin-literal-phrases

## What this phase found

**The frame holds against the merge at `ab3d6bc8c`, except two
statements of the present that the merge made false.** The merge's
parents are `573a7e56a` and `dbed1d5ff`, the commit of #1486 on
`origin/release/v0.37.4`. The merge also brought #1481 at `1a01c761a`,
which changes no module of the two directories (executed,
`git diff --name-only`). Both branches change ten modules, the number the
plan's judgment row gives for `60838ede9` (executed, below). The two
statements are the frame's to fold, and neither changes what this phase
rules:

- design *The criterion*, the paragraph on a kept absence assert, says the
  claims step's assert "is now the claims step's own" `run:` block. At the
  merge, `test_the_body_reaches_the_script_through_the_environment` is
  #1486's text. It reads every step's `run:` block of the parsed workflow
  and holds no listed assert.
- plan *Operational impact* says `.test_durations` keeps the removed
  cases' rows until #1486 removes the file. #1486 removed it, and no
  `.test_durations` stands at the merge (executed, `ls`).

Plan *Overlap with the release*, the #1481 row, says a kept assert that
reads text #1481 changed turns red in phase 5's narrow run once the
branch has taken it. The branch took it through the merge, and the
narrow run at the merge was green (below), so none did.

**The modules both branches changed, by command (design *Scope* item 12).**

```
MB=$(git merge-base 573a7e56a origin/release/v0.37.4)   # 957a3bc7d
git diff --name-only $MB 573a7e56a -- tests/text tests/behaviour > ours.txt     # 52 modules
git diff --name-only $MB origin/release/v0.37.4 -- tests/text tests/behaviour > theirs.txt   # 15 modules
comm -12 ours.txt theirs.txt
```

```
tests/behaviour/test_a_body_naming_two_issues_claims_one.py
tests/behaviour/test_a_declared_label_reaches_the_tracker.py
tests/behaviour/test_a_release_publishes_its_note.py
tests/behaviour/test_release_hygiene.py
tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py
tests/behaviour/test_the_release_check_watches_what_ships.py
tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py
tests/text/test_a_merged_ticket_says_so_on_the_tracker.py
tests/text/test_a_release_cannot_ship_an_untrue_milestone.py
tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py
```

`origin/release/v0.37.4` was `dbed1d5ff` when it ran (executed). Of the
two release commits after the merge base, only `dbed1d5ff` changes a
module of the two directories (executed). The five modules only #1486
changed are outside the list. Two are *Out* in the design. In the other
three, `test_the_release_seal_is_drawn.py`,
`test_the_direct_answer_owes_the_sealers_record.py` and
`test_the_rules_claude_md_names_have_one_home.py`, #1486's hunks hold no
listed assert (executed, *The listing* at the merge).

**The cases #1486 changed or added in the ten modules.** A script under
the phase's scratch directory mapped each hunk of
`git diff -U0 957a3bc7d dbed1d5ff` to the top-level unit it falls in, on
both sides (executed). It gives 23 cases. One is design *Out*:
`test_a_release_publishes_its_note.py#test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`,
which holds 8 listed asserts at the merge and was not read. The other 22
were read whole. In `test_the_release_check_watches_what_ships.py` #1486
changed the helpers `ships_pattern` and `release_step` and the constant
`STAYS_HOME`, and no case. The rulings phase 4 made there stand.

Eight of the 22 cases hold a listed assert at the merge, and design
*Scope* item 1 rules them. The other fourteen hold none, because #1486
rewrote each to read its workflow through `tests/workflows.py#load` and
compare keys and values with `==` or with `in` on a name. Design *Out*
leaves a case that holds no listed assert, so these fourteen stand as
#1486 wrote them:

- `test_a_body_naming_two_issues_claims_one.py#test_the_body_reaches_the_script_through_the_environment`
- `test_a_declared_label_reaches_the_tracker.py#test_a_failed_step_cannot_skip_the_independent_steps_after_it`
- `test_release_hygiene.py#test_the_python_floor_is_the_same_number_everywhere`,
  `#test_the_token_stays_the_smallest_that_can_close_an_issue` and
  `#test_the_check_lines_rules_did_not_read_reach_the_pull_request`
- `test_the_gate_asks_the_range_ci_will_ask.py#test_the_workflow_reader_sees_every_shape_a_base_is_spelled_in`,
  `#test_only_a_base_keyed_under_env_is_a_base` and
  `#test_an_empty_base_fails_the_spelling_check_by_name`
- `test_the_suite_has_a_command_that_is_cheap_twice.py#test_ci_installs_the_parser_the_runner_pins`
  and `#test_ci_runs_the_suite_at_the_floor_the_runner_holds`
- `test_a_merged_ticket_says_so_on_the_tracker.py#test_the_token_is_the_smallest_that_can_add_a_label`
  and `#test_the_trigger_is_a_push_to_a_release_branch_and_nothing_else`
- `test_a_release_cannot_ship_an_untrue_milestone.py#test_the_head_shape_reaches_the_script_rather_than_the_guard`
  and `#test_the_job_asks_for_a_token_that_can_read_issues`

**Eleven asserts phases 1 and 4 kept left the listing with #1486's
rewrite, and their comments left with them.** Each still reads the same
key or value, as an equality on the parsed workflow. The line numbers are
`573a7e56a`'s:

- `test_a_body_naming_two_issues_claims_one.py:59` and `:64`, the
  `PR_BODY` binding and the body's absence from the claims step's `run:`
  block (phase 4). #1486's case reads the absence from every step's
  `run:` block, so phase 4's narrowing at `f25de2b52` is gone with it.
- `test_a_release_publishes_its_note.py:205`, `:207` and `:225`, the
  `dist` job's `needs` and `if` lines and its step's command (phase 4).
- `test_a_release_cannot_ship_an_untrue_milestone.py:63`, `:97` and
  `:126`, the `HEAD_BRANCH` binding, the five environment keys and the
  `GH_TOKEN` binding (phase 1).
- `test_the_release_table_reads_two_trees_and_fails_nothing.py:39`, `:40`
  and `:41`, the `release-report` job's `needs` and `if` lines and its
  checkout's depth (phase 1).

Two asserts phase 4 did not rule, `'origin/other'` and `'bar'` absent
from what `base_spellings` returns, now stand in a loop over a tuple and
leave the listing too. No case or helper phases 1 to 4 removed came back
with the merge (executed: the top-level units at the merge base, at
`573a7e56a` and at the merge compared).

**S1, over the cases phase 5 ruled.** The unit is one assert, a distinct
`path:line`, as in phases 1 to 4. The base is the merge, `ab3d6bc8c`, and
the line numbers are its. The last column is *The listing* at
`ea4da5bf3`.

| Module | Cases ruled | Listed | Kept | Removed | Not ruled | Listed at `ea4da5bf3` |
|---|---|---|---|---|---|---|
| `tests/behaviour/test_a_release_publishes_its_note.py` | 1 | 3 | 3 | 0 | 0 | 3 |
| `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py` | 1 | 1 | 0 | 0 | 1 | 1 |
| `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` | 1 | 7 | 7 | 0 | 0 | 7 |
| `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` | 2 | 3 | 3 | 0 | 0 | 3 |
| `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` | 3 | 7 | 6 | 1 | 0 | 6 |
| Total | 8 | 21 | 19 | 1 | 1 | 20 |

The last column equals the kept count plus the not-ruled count in every
module (executed). The one not ruled is `'foo' in found` at
`test_the_gate_asks_the_range_ci_will_ask.py:362`. `found` is what
`base_spellings` returns over `MISLEADING_WORKFLOW`, a fixture the case
writes, so the assert reads a program's output on a text the case built.

**The rulings, each judged against `frame/design.md` *The criterion*.**

- `test_a_release_publishes_its_note.py#test_the_dist_job_adds_the_release_to_dist_and_goes_red_where_it_cannot`.
  `continue-on-error` absent from every key and scalar of the `dist` job
  (`:185`) and `persist-credentials` absent from its checkout's `with:`
  (`:191`) are kept absences, as phase 4 kept them on the old text. The
  rules are the header comment's paragraph on `dist` and the comment above
  the job's checkout in `.github/workflows/publish-release.yml`. Both stand
  at the merge (read). The bot's address in `GIT_AUTHOR_EMAIL` (`:198`) is
  kept as an environment binding. Each took back phase 4's comment.
- `test_the_suite_has_a_command_that_is_cheap_twice.py#test_the_section_names_the_parser_and_where_it_is_pinned`.
  The four asserts phase 3 kept (`:176` to `:182`) stand as they are.
  #1486 added `` `PyYAML` `` and `` `PYYAML` `` (`:185`), the package a
  reader installs and the constant a reader resolves, and rewrote the two
  fallback commands to carry the third pin (`:186`, `:189`), which a
  reader copies. All are kept. #1486's comment named the facts and not
  their reader, and the `#647` comment above it named the fallback
  commands that now stand under #1486's. Both were rewritten, and the
  fallback commands took a comment of their own.
- `test_a_release_cannot_ship_an_untrue_milestone.py#test_the_gate_runs_only_for_a_release_pull_request`.
  The guard's condition (`:41`) is kept, and takes back phase 1's comment.
  Phase 1's comment called it the step's `if` condition. It is the
  condition of the shell `if` in the step's `run:` script, which
  `guarded_script` returns, and the comment now says so. `exit 0` (`:59`)
  kept phase 1's comment through the merge.
- `test_a_release_cannot_ship_an_untrue_milestone.py#test_every_input_the_script_reads_is_handed_to_it_by_the_step`.
  The `HEAD_SHA` value (`:108`) is kept as the value the runner binds. The
  loop's `assert name in env` holds the five keys in a tuple, outside *The
  listing*. Design *Scope* item 1 rules it, and it is kept as the
  environment keys the runner hands the script. Both took back phase 1's
  comments.
- `test_the_release_table_reads_two_trees_and_fails_nothing.py`, three
  cases. The step's command and its redirection into the step summary
  (`:48`, `:49`) and the worktree command (`:57`) are kept, and their
  comments are phase 1's, cut to what the case still reads. `"git archive"
  not in script` (`:58`) is removed, as phase 1 removed it on the old text:
  it holds a design a shipped release removed, and no rule in force
  forbids the literal. #1486 had kept it in its rewrite, and the merge
  took #1486's hunk. The case #1486 added,
  `test_the_table_reads_this_run_s_union_and_the_tag_s_push_run_s`, holds
  three listed asserts: the `gh run download` command with its `|| true`
  (`:78`), and the `--durations` and `--durations-at` flags with their
  paths (`:82`, `:83`). Each is a command or a flag the runner runs, and
  each is kept with a comment.

The equality asserts on the parsed workflow in these cases, such as the
`dist` job's `needs` and `if` and the download step's `name` and `path`,
are not ruled and take no comment. Phases 1 to 4 left the equality
asserts of a ruled case the same way, for example `checkout[0] == …` of
the `dist` case at `573a7e56a`.

These literals could be read either way, and the proofer reads each
against *The criterion* (S2):

- `` `PyYAML` `` beside `` `PYYAML` `` in one assert, kept as a package
  name and a constant. Read as words, the package name in backticks is a
  phrase of the section's sentence.
- `|| true` kept inside the `gh run download` literal. It is the part of
  the command that lets the step go on where the tag's push run has no
  union, which the case's docstring states.

**A docstring outside the ruled cases stated what a case phase 1 removed
read, and was rewritten at `8deecafb9` (design *Scope* item 7).** The
module docstring of `tests/github/test_release_completeness_check.py`
said `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py` keeps
the cases that read "the two docstrings that draw the input boundary".
Phase 1 removed that case,
`test_the_script_and_this_file_draw_the_input_boundary_the_same_way`.
The docstring now says the module keeps the cases that read the hygiene
workflow's step. It was found by `git grep` on the four edited modules'
names under `tests/` outside the two directories, which lists four
modules of `tests/github/`; the other three citations state what their
modules hold (read). That search finds a citation by the module's name,
so it is a sample: a sentence that paraphrases a removed case without
naming its module is outside it.

**Check lines (design *Scope* items 8 and 9).** No module was deleted and
no case was removed, so no check line outside `docs/` changed. The check
lines that name one of the ten modules were listed by `git grep` on each
module's file name over every `check:` line outside `seal/threads`,
`tests` and `*.py` (executed). All ten stand under `docs/`:
`docs/releasing/issues-and-milestones.md:293`,
`docs/releasing/branch-and-release.md:48` and `:138`,
`docs/releasing/release-checklist.md:195`, `:241`, `:250` and `:344`,
`docs/running/the-broad-gate.md:76`, `:115` and `:124`. The one
assert this phase removed reads none of their rules:
`docs/releasing/release-checklist.md:195` closes the release table's
paragraph, and its module still reads the `release-report` job, its
summary and the tag's whole tree (read). No `docs/` check line loses its
last reader through phase 5. The list was made by command, so it is the
whole class.

**The counts of design *The counts* (S7).** The two forms are the issue's,
by the commands of that table. *The listing* is the script of design *The
listing*, run over the two directories written out of each commit with
`git show`.

| Count | At `18a7e18fb` | At `573a7e56a` | At the merge `ab3d6bc8c` | At `ea4da5bf3` |
|---|---|---|---|---|
| presence form | 388 | 306 | 289 | 289 |
| absence form | 134 | 17 | 15 | 14 |
| the listing | comparisons 735, asserts 696, absence asserts 151, cases 342, modules 72 | comparisons 477, asserts 456, absence asserts 23, cases 269, modules 66 | comparisons 458, asserts 437, absence asserts 21, cases 265, modules 66 | comparisons 457, asserts 436, absence asserts 20, cases 265, modules 66 |

All cells are executed. From `573a7e56a` to the merge the listing loses
26 asserts and gains 7, 456 to 437 (executed, per module). It loses the
eleven kept and the two unruled above, eleven of the *Out* case, which
#1486 rewrote from 19 listed asserts to 8, and two of
`test_ci_gives_the_checks_what_they_need.py`, which is *Out*. It gains
`PyYAML`, the three of #1486's new case, `git archive`, and two of
`test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, which is
*Out*. Phase 5 removes one, `git archive`. The changelog's after-build
column now gives the `ea4da5bf3` counts.

**What was run, and what each run showed.**

- The narrow run at the merge, before any edit: `bin/test tests/text
  tests/behaviour -q` gave 1773 passed and 8 skipped (executed). No kept
  assert had turned red on the text #1481, #1483, #1486 or #1487 changed.
- S1 and S7: executed, as above. The listings, the unit map and the
  definition lists are in the phase's scratch directory.
- S4: `bin/seal rules --check` exits 0, "all 177 check lines in 69 rule
  files hold." (executed at `ea4da5bf3` and at `8deecafb9`).
- S5: phase 5 removed no case, helper or module, so no name was searched.
- S9: the four edited modules gave 26 passed before `ea4da5bf3` was
  committed (executed). `uvx ruff check` and `uvx ruff format --check`
  pass over the ten modules and over
  `tests/github/test_release_completeness_check.py`, whose 38 cases pass
  at `8deecafb9` (executed). The boundary set, `bin/test tests/text
  tests/behaviour -q`, gave 1773 passed and 8 skipped at `8deecafb9` with
  this record, `gaps.md`, `changelog.md` and the Status cell in the tree
  (executed). The two directories hold every module that imports an
  edited one. Four modules of `tests/github/` name an edited module in a
  docstring or a case's name and import nothing from it (read).
- Mutation: `seal mutate` ran once per mutant, each with the case it pins,
  and each went red on the assert it names (executed, failing line read):
  `continue-on-error: true` planted in the `dist` job,
  `persist-credentials: false` planted in its checkout, the backticks
  taken off `PyYAML` in `CONTRIBUTING.md`, `|| true` taken off the
  `gh run download` line of `.github/workflows/test.yml`, and the
  `--durations-at` path pointed at this run's union. The tree was clean
  after each restore (executed, `git status --short`).
- S2 and S3 are the proofer's at review.
