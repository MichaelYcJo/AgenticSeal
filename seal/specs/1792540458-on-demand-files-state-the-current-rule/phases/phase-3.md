# 1792540458-on-demand-files-state-the-current-rule — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | b3953cd5 |


## What this phase was asked

`templates/claude-md-block.md` cut to its rules, 1,000 to 1,500 bytes by
`wc -c`, holding the four headings and the routing bullet of `spec.md`
Scope 2 in its order. This repository's `CLAUDE.md` to about 4,500 bytes or
fewer with no generated copy, its rows judged by Scope 3, and the compact
writing rule of Scope 1. `.github/scripts/claude_block.py`, its
`hygiene.yml` step and the cases holding the copy to the template removed,
the installer cases kept in a module named for the installer. Every sentence
stating the generated copy rewritten in the same commit: `install.sh`, the
update skill's step 4 with the sentence on installing a clone's block, the
preset-setup skill, both READMEs' block rows, and the docstrings of
`hooks/mode-gate.py`, `skills/verify/scripts/unverified_check.py` and
`skills/verify/scripts/broad_gate.py`. The pins that read the block through
`CLAUDE.md` read the template.

## What this phase found

**The frame holds, with three corrections to what it says about the tree.**

- Scope 3 grounds the identifiers row on `plugin_directory_check.py`
  refusing only at the pull request. That script reports the marketplace
  listing and reads no fixture (read, its docstring). The check is
  `tests/test_no_real_identifiers.py`, which `CONTRIBUTING.md` *House rules*
  names and the suite runs at the pull request (read). The conclusion
  stands: a smith writing a fixture opens no file that states the rule
  before the suite refuses it, so the row stays.
- `broad_gate.py` carried the copy's step twice over: in its docstring, as
  the plan says, and as a `PARTITION` entry with the reason no arm mirrors
  it. The entry left with the step, and with it one step of every count the
  gate prints: the `release` job runs 8 steps against `main` and 5 against a
  release branch, and `skills/verify/SKILL.md` *The broad gate* now says two
  steps have a local answer and no arm, one of them a script under
  `.github/scripts/` (executed, `broad_gate.coverage_line` over the workflow).
  The sentence is phase 5's file; it is corrected here because this commit
  made the old count false.
- `skills/update/SKILL.md` and `skills/preset-setup/SKILL.md` are in no later
  phase's cell, though Scope 7 rewrites every skill. This phase rewrote their
  copy sentences and took out the anecdotes that stood beside them (the
  measured release counts in step 4, *Measured the day this step was
  written* and *both measured the same day* in step 2b); the rest of their
  prose is unread against the writing rules. The orchestrator decides whether
  phase 6 takes them.

**Phase 2's boundary set was one module short.** `tests/test_no_document_names_the_old_roots.py`
reads `skills/implement/orchestration.md` by walking the tree, not by name, so
`git grep -l` over `tests` did not list it, and phase 2's rewrap split the
line its allowlist keys on. It went red in this phase's run and was repaired
alone at 5a0d15a6. That commit also carries the two removals staged by
`git rm` before it, `.github/scripts/claude_block.py` and
`tests/test_the_claude_md_block_has_one_source.py`, so between 5a0d15a6 and
0f92ad27 the workflow names a script the tree no longer has. The branch
squashes, so no commit of the merged history holds that state.

**The block is 1,498 bytes** (4,695 at b3154f43, executed `wc -c`), so
`questions.md` Q4 closes inside the range. It keeps every rule Scope 2 names,
in Scope 2's order. Two sentences carry more than Scope 2 lists, each a rule
rather than reasoning: *where the root lands is the user's decision*, which
tells the session not to choose the place itself, and the waiver's spelling
`: '[no-review]';`, without which a session that answered `no work item`
types a token git reads as a pathspec. *Never cut the investigation* stays
beside the batching rule as its bound, and is now pinned.

**`CLAUDE.md` is 3,049 bytes** (8,524 at b3154f43, executed `wc -c`). Its
rows, against Scope 3:

| Row | Judged | Where it is now |
|---|---|---|
| the goal | stays as #923 left it; its heading lost the dash and its subtitle | `CLAUDE.md` |
| the tenet | the same | `CLAUDE.md` |
| merge method per direction | stays: the party merging opens no file that states it | `CLAUDE.md`, heading `Repo rule:` |
| no real identifiers | stays, on the corrected ground above | `CLAUDE.md`, heading `Repo rule:` |
| whose | folds into the writing rule | `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` |
| commit early | leaves; `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* states it and the smith opens it at its first step (read) | the skill |
| fragments | leaves; `skills/code-review/orchestration.md` names the work item's `changelog.md` at the step before the broad run (read, line 195). That line names the file and not who writes it; phase 4 names the party | the orchestration file |
| the generated block and the comment under it | leaves | the installed block, from `templates/claude-md-block.md` |

**Census (S11).** The block's routing bullet is mapped sentence by sentence
in `phases/phase-2.md`; every sentence the block does not keep lands in
`skills/implement/orchestration.md` or `skills/implement/SKILL.md`. Elsewhere:

| What left | Grounds |
|---|---|
| the Tooling bullet's middle dot and parenthesis | the same three rules as three sentences |
| *(worktree-guard hook enforces this)* | reasoning; the hook refuses on its own |
| *the handoff to review runs nothing broad* and *was spent, not banked* | folded: the broad run is once, after the rounds, and an edit after it spends it |
| *Round-trips are most of a round* | reasoning; *Never cut the investigation* keeps the bound |
| *Writing the file below is what CREATES that directory, creating it is what opts the repository in* | reasoning; *Orchestrator: Bootstrap* holds it, and the case that pinned it in the block now reads it there |
| `install.sh`'s comment on #292's measurement | history |
| the hygiene step and its comment | the copy it held is gone; failure direction in `spec.md` *Removes* |

**Cases retired, moved or rewritten** (each new or rewritten one seen red,
executed):

| Case | What happened |
|---|---|
| `tests/test_the_claude_md_block_has_one_source.py`, every case | the module left. Its installer cases moved to `tests/test_the_installer_writes_the_block_from_its_template.py`; its copy cases (`--check`, `--write`, line endings, drives, exit codes, the hygiene step) left with the script; *the block sends a fresh repository to the orchestration file* folded into `tests/test_first_setup_asks_once.py#test_the_preset_sends_a_fresh_repository_to_the_bootstrap`, which now names the file |
| `tests/test_every_reader_ends_a_line_where_gfm_does.py#test_the_claude_md_block_is_cut_where_awk_cuts_it` | retired with the script it ran |
| `tests/test_no_passage_is_pasted_into_a_second_file.py`, `GENERATED` and its case | `tree()` reads every file whole; the case now holds the template read whole |
| `tests/test_first_setup_asks_once.py`, the preset cases | read the template; *opts the repository in* is held in the Bootstrap, not the block |
| `tests/test_review_axes.py`, both preset cases | read the template; the box vocabulary is held in the orchestration file alone |
| `tests/test_waiver_decided_at_start.py#test_the_preset_block_carries_it_too` | reads the template only, and holds question 1's three answers instead of the box vocabulary |
| `tests/test_broad_gate_rule.py#test_the_preset_block_states_the_rule_the_loaded_files_assume` | reads the template, and pins the batching rule's bound |
| `tests/test_the_rules_claude_md_names_have_one_home.py` | `CLAUDE.md` links merge, identifiers and the batch; the removed-link case strips the italic citation |
| `tests/test_the_changelog_is_gathered_at_release.py#test_the_documents_send_a_change_to_its_own_fragment` | `CONTRIBUTING.md` sends the reader to the fragment rule; `CLAUDE.md` no longer does |
| `tests/test_the_gate_names_every_step_ci_runs.py`, the two counting cases and the skill sentence | 8 and 5 steps, 5 and 2 more; the sentence's verb follows its number |
| new: `#test_this_repository_carries_no_copy_of_the_block`, `#test_a_second_install_changes_nothing`, `#test_uninstall_sh_removes_the_block_and_nothing_else` | red under `mutation-check`: a marker put back in `CLAUDE.md`; the installer's replace branch turned off; `uninstall.sh` printing the block's lines. The uninstall case first survived that mutation, because it asserted the markers alone; it now asserts the file is the user's line and nothing else |
| `#test_the_runtime_readers_name_the_template_path` | red against the tree before the two skills were edited (*generated copy* in both) |

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| block: *Where `seal/` exists at neither … first follow the Bootstrap section …; where the root lands is the user's decision* | the actor is whoever the block is loaded into, a session; the condition is both root places |
| block: *Before the first edit, write `seal/specs/<work-item-id>/routing.md` … in a command of its own, then commit it* | the moment is the first edit; done is the commit |
| block: *Under `no work item`, every commit carries `: '[no-review]';` in front of it* | the condition is the answer pressed, not the kind of change |
| `CLAUDE.md`: *an instruction names who acts, when, on which file and what counts as done* | stated as a property of the text, because the actor of the rule is every writer |
| update step 4: *running `./install.sh` from that clone installs the clone's block* | the condition is a session in a clone of the plugin's own repository |

**Restatement pairs of this phase's files** (Scope 10, measured at b3953cd5
with the module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `CLAUDE.md`, `CONTRIBUTING.md` | 0 | 14 | drained; phase 9 removes the entry |
| `agents/smith.md`, `templates/claude-md-block.md` | 0 | 13 | drained; phase 9 removes the entry |
| `README.md`, `skills/update/SKILL.md` | 9 | 9 | the README's install section, outside this item beyond its block rows |
| `README.md`, `skills/config/SKILL.md` | 22 | 22 | phase 6 |
| `README.md`, three more pairs at 1 or 2 | as `BASELINE` | | the README's |
| `README.md` with `agents/smith.md`, `docs/commit-review-gate-spec.md`, `skills/code-review/orchestration.md` | 0 | 4, 5, 10 | drained before this item; phase 9 removes the entries |

**`bash -n install.sh uninstall.sh`** exits 0 (executed). `uninstall.sh`
carried no sentence about the copy and is unchanged.
