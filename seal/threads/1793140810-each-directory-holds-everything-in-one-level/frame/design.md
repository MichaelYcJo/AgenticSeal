# Feature Specification: 1793140810-each-directory-holds-everything-in-one-level

Builds #1060: `templates/`, `hooks/` and `tests/` are split by kind into
directories a reader can tell apart from the listing, `docs/README.md`
groups the policy documents by subject, and the general skills no record
shows used leave the plugin. Milestone `release: 0.23.1`, first work item.
It is a change of place: no gate, check or agent decides anything
differently, except the two readers named under *Scope* that state where a
file stands. The sets below are read from the tree at `d4623900`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Nothing here asks a person mid-run. Each decision only a person can make is a row of `questions.md` with a default, and the build proceeds on the default |
| `CLAUDE.md` *The rule a mechanism is kept against* | A skill stays only while its history shows it used, which is #1060's own criterion for the general skills. The census this work adds derives what it refuses from the tree and stores no list of old paths beside it |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The policy root is the baseline a pull request does not edit. This work edits `docs/` for the spelling of moved paths and for the grouping of the index only, as #1051 did for names (`4420ebd5:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/frame/design.md` *Scope*): a path's spelling and a table's grouping carry no decision |
| `skills/settle/SKILL.md` *Rule changes* | "`file` is a top-level `.md` file of the policy root". `skills/settle/scripts/rule_changes.py` (lines 163 to 169) refuses any other `file`, so a policy document moved into a subdirectory of `docs/` could never again be named by a spec's `## Rule changes` |
| `skills/settle/scripts/fold_check.py` docstring, lines 11 to 23 | `seal fold` reads the policy root's top level alone, for one read and one index. A document in a subdirectory leaves both checks silently |
| `docs/README.md`, its last paragraph | "`docs/experiments/` holds dated scratch documents and is no policy; `settle` never writes there." A subdirectory of the policy root already means *not policy* |
| `CONTRIBUTING.md` *The test layout* | "The file is `tests/test_<stem>.py`." This work rewrites that sentence to name the area directory, and `seal layout --check` reads the directory as it reads the name |
| `tests/test_the_frozen_reading_never_grows.py` | The hash covers `hooks/cmdline_base.py` from `START` (`"""Reading a shell command line`) to the end. The rider above `START` may change, so the file can move with its bytes below the rider untouched |
| `https://code.claude.com/docs/en/plugins-reference` *Fields* and *Standard layout* (read 2026-10-28) | Skills load from `skills/<name>/SKILL.md`, one level. The manifest's `skills` key adds directories "each a directory of `<name>/SKILL.md` folders", and `hooks/hooks.json` is the hooks file loaded by default. A nested `skills/<kind>/<name>/` loads only through that key |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names each removal once, for the review to read against the diff |
| `tests/censuses.py#OLD_NAME_RECORDS` and `#HISTORY_PATH` | The records of a moment keep the paths they were written under: `changelog/`, `CHANGELOG.md`, `seal/process/`, `seal/threads/`, `evals/scripts/recurred_truths.json`, `.test_durations`, the recorded eval cases, and a citation in the form `<commit>:<path>`. #1051's round 1 finding 7 is the cost of rewriting one (`4420ebd5:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-1.md`) |

## Scope

**In.** Each row's set is exact at `d4623900` and was read from the tree
(executed: `git ls-files`, `grep '^TARGET = '` over `tests/test_*.py`).

| Directory | Stays at its top | Moves |
|---|---|---|
| `templates/` | nothing | `templates/records/`: `sdd-design.md`, `sdd-gaps.md`, `sdd-guarantee.md`, `sdd-phase.md`, `sdd-plan.md`, `sdd-questions.md`, `sdd-round.md`, `sdd-routing.md`, `process.md`. `templates/setup/`: `claude-md-block.md`, `config.md`, `hygiene.yml`, `pact.md`, `parity.md`, `seal-README.md` |
| `hooks/` | `hooks.json`, `dispatch.py`, and the 15 gates `hooks/dispatch.py#GROUPS` names: `implementer-mark.py`, `implementer-notice.py`, `lint-python.py`, `mode-gate.py`, `question-gate.py`, `review-skill-gate.py`, `root-migrate.py`, `routing-edit-gate.py`, `sealer-stamp-queue.py`, `sealer-stamp.py`, `session-lease.py`, `stub-remove.py`, `version-check.py`, `worktree-guard.py`, `worktree_consent.py` | `hooks/lib/`: `blocks.py`, `cmdline.py`, `cmdline_base.py`, `config.py`, `console.py`, `gate.py`, `hooksession.py`, `implementer.py`, `launch.py`, `one_heredoc.py`, `optin.py`, `routing.py`, `tokens.py` |
| `tests/` | `conftest.py`, `censuses.py`, `block_shapes.py`, `config_shapes.py`, `commonmark_oracle.py`, `gfm_table_oracle.py`, and the two files whose `TARGET` is under `tests/`: `test_censuses.py`, `test_conftest.py`. `tests/e2e/` stays as it is | the module test files by the first segment of their `TARGET`, a leading dot dropped: `tests/hooks/` (28), `tests/skills/` (17), `tests/github/` (14), `tests/evals/` (4). The 91 files that declare no `TARGET` into `tests/behaviour/` (43) and `tests/text/` (48), by the criterion under *Data & interfaces* |
| `docs/` | every file, `experiments/` included | nothing. `docs/README.md`'s one table becomes one table per subject, Q1's default |
| `skills/` | the 14 skills the workflow names | the eight general skills no record shows used are removed, Q2's default |

`worktree_consent.py` stays at the top although two gates import it,
because `dispatch.py` runs it by its file name in `post-bash` and
`post-agent`. `launch.py` moves although no gate imports it: the top of
`hooks/` holds what `hooks.json` and `dispatch.py` run, and `launch.py` is
run by `bin/seal`, `bin/seal.cmd` and `.github/scripts/run_tests.py`.

**`hooks/lib/cmdline_base.py` keeps its freeze.** Its bytes from `START` on
do not change, so the hash in `tests/test_the_frozen_reading_never_grows.py`
still holds, and that case's `FROZEN` names the new path. The rider above
`START` is rewritten for the new paths it cites. The docstring below the
rider keeps `hooks/optin.py`, `hooks/dispatch.py:72` and
`hooks/commit-review-gate.py` as 86256492 spelt them, which the rider already
says to read as of that commit; the new census passes the file whole, as
`tests/censuses.py#KEPT_FILES` already passes it for `old_names`.
`test_only_the_two_fallback_arms_read_it` reads `hooks/` recursively and its
two readers stay at the top, so its expected list does not change.

**The general skills.** #1060 asks that each be kept, moved out to a plugin
of its own, or removed, decided from whether anything in the record shows it
used. The record read (executed 2026-10-28): commit messages on every ref
(`git log --all --grep`), the work item records at `aa687d35` and at
`4420ebd5` under `seal/`, the agent definitions and `evals/`.

| Skill | What the record shows | Decision |
|---|---|---|
| `confidence-check`, `feature-planner` | `agents/framer.md` step 5 names both, and `tests/test_chain_hooks_hardening.py#UTILITY_SKILLS` pins that `agents/framer.md` is their one caller | kept: the workflow calls them |
| `debug`, `build-fix`, `checkpoint`, `gap-analysis`, `security-audit`, `testing`, `learn`, `audit` | no commit message, record, agent definition or eval names one; the only mentions are `README.md`, `README.ko.md` and each other's `NOT for` clauses | removed |

`audit` is not on #1060's list and is decided by the same criterion: it
checks a repository's `.claude/audit-rules/*.md`, and nothing in the
workflow calls it. The instrument has a blind side: a session that loads a
skill writes no record of it, so the tree cannot show a use that happened.
Q2 holds that, with removal as the default.

**`skills/` keeps one level.** Claude Code finds a skill at
`skills/<name>/SKILL.md`. A split by kind would need the manifest's `skills`
key and would change every `skills/<name>/` citation in the tree, and
removing the eight general skills leaves `skills/` holding only the
workflow's own. Nothing in `skills/` moves.

**Two readers that state where a file stands change with the move.**
`skills/verify/scripts/test_layout.py` `--check` refuses a module test file
outside `tests/<area>/`, and `CONTRIBUTING.md` *The test layout* states the
directory where it now states `tests/test_<stem>.py`. Each test file takes
the repository root from `tests/conftest.py#ROOT` instead of computing it
from its own path, and a case refuses a test file that computes it.

**What moves with the files.** Every living reader of a moved path, in
code and in prose, rewritten in the commit that moves the file (contract
rule 19). The classes:

- code that joins a moved path: each gate's `sys.path.insert`, the
  `HOOKS` joins in `skills/*/scripts/`, `.github/scripts/` and
  `evals/scripts/`, `bin/seal`, `bin/seal.cmd`, `run_tests.py`'s launcher,
  the three `templates` joins (`hooks/root-migrate.py#TEMPLATE`,
  `skills/implement/scripts/seal.py` at lines 1922 and 2043) and
  `install.sh#SOURCE`;
- readers that derive a set of files from a directory, which shrink
  silently instead of failing: `tests/test_launch.py#loaded_by`,
  `hooks/dispatch.py#opted_in`, `evals/scripts/replay_targets.py#CHECK_FILES`;
- `check:` lines in `agents/`, `docs/`, `skills/`, `CONTRIBUTING.md` and
  `tests/`, which `seal rules --check` already refuses when a target is gone;
- prose citations in every living file, `README.ko.md` and the Korean
  editions under `docs/` among them, and the messages a gate prints, such as
  `hooks/routing-edit-gate.py`'s `templates/sdd-routing.md`;
- `ruff.toml`'s comment naming `hooks/git/`, `.github/workflows/test.yml`'s
  `pytest tests/test_arm_check.py`, and the census constants that name a
  moved file (`KEPT_FILES`);
- `.test_durations`, refreshed after the last move, `plan.md`
  *Operational impact*.

**What keeps the old path.** The records `tests/censuses.py#OLD_NAME_RECORDS`
lists, the recorded eval cases `#RECORDED_CASE` matches, a citation in the
form `<commit>:<path>`, and `hooks/lib/cmdline_base.py` below its rider.
None of them is rewritten.

**Out.**

- `docs/` into subject directories, Q1. The readers above make a
  subdirectory of the policy root *not policy*; moving a document there
  would change what `settle` accepts and what `seal fold` checks.
- `bin/`: #1060 says it follows #1051's `seal <subcommand>`, and #1051 left
  `bin/test` in place for this work to decide. It stays: `bin/` is what
  Claude Code puts on PATH, and `bin/test` is typed as written in
  `seal/config.md`'s `Broad gate` row and in `templates/config.md`.
- `skills/*/scripts/`: #1060 does not propose moving them, and an installed
  repository's workflow runs two of them by path at the release it pins.
- `.github/scripts/`, `evals/`, `agents/`, `assets/`, `changelog/`: each
  already holds one kind.
- Behaviour. A test that pins a message changes the path in the message and
  nothing else.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The tree holds the directories this frame fixes | Given HEAD, when `git ls-files templates hooks tests` runs, then every file stands where *Scope* puts it and no file stands at a top level *Scope* moves it out of | a measurement each phase records with its command; the orchestrator reads it at HEAD |
| No living file names a vacated path | Given a file at `hooks/lib/<name>`, `templates/records/<name>`, `templates/setup/<name>` or `tests/<area>/<name>`, when the census runs over every tracked file, then a living line spelling `hooks/<name>`, `templates/<name>` or `tests/<name>` is refused, outside the records, the `<commit>:<path>` form and the frozen file | `tests/censuses.py#vacated_paths`, run by `tests/test_censuses.py`; seen red in phase 1 against the template citations before their sweep |
| Every `check:` target resolves | When `seal rules --check` runs from the tree, then it exits 0 | `tests/github/test_rules.py`, which runs it over the tree |
| Every gate loads from its own file | Given each gate `dispatch.GROUPS` names, when it is loaded in a fresh interpreter with nothing else on `sys.path`, then it loads without an import error | a new case in `tests/test_dispatch.py`, seen red with one gate's `lib` insert removed; `hooks/dispatch.py` skips a gate that fails to load, so a missed import reads as silence |
| The hooks an installed repository registers are the same | Given the tree, when `hooks/hooks.json` is read, then every command names `hooks/dispatch.py` and that file exists | `tests/test_chain_hooks_hardening.py#test_hooks_json_points_at_existing_python_scripts`; the first session of an installed repository is Q3 |
| A replayed check finds its sibling at either path | Given a commit holding `hooks/lib/blocks.py`, when `replay_targets.py` copies a check's files from it, then `blocks.py` is copied from where that commit holds it | a new case in the test file of `evals/scripts/replay_targets.py`, seen red against `CHECK_FILES` as it stands |
| The suite collects the same cases | Given the base and HEAD, when each collects `tests` with `--collect-only -q`, then the node ids are the same set, compared as file name and the rest of the id | per phase over its own files; the whole suite by the orchestrator after phase 4 |
| A module test file stands in its area | Given a test file declaring `TARGET = "hooks/lib/optin.py"` at `tests/test_optin.py`, when `seal layout --check` runs, then it is refused with a line naming `tests/hooks/` | a new case in the test file of `skills/verify/scripts/test_layout.py`, seen red against the script before the change |
| No test file computes the repository root | When the suite collects, then no file under `tests/` but `conftest.py` derives the root from its own `__file__` | a new case in `tests/test_conftest.py`, seen red at phase 3's commit |
| Two test files never share a name | When the suite collects, then no two files under `tests/` have the same file name | a new case in `tests/test_conftest.py`, seen red with a planted duplicate in a fixture tree |
| The removed skills are gone | When `git grep` runs for `agentic:<name>` and `skills/<name>/` of each removed skill, then it matches only records, and `README.md` and `README.ko.md` count fourteen skills | `tests/test_chain_hooks_hardening.py`'s count case; `claude plugin validate .` exits 0 |
| `docs/README.md` indexes by subject | When `seal fold` runs, then every top-level document is on exactly one row of the index's tables | the case `test_accepts_this_repository_with_no_flags` in `tests/test_fold_check.py` (at `tests/skills/` from phase 3), which runs the fold over this repository |

## Data & interfaces

**How a module finds `hooks/lib/`.** Each gate at the top of `hooks/` keeps
its imports as written and inserts
`os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")` where it
inserted its own directory. A module in `hooks/lib/` already inserts its own
directory, which is `lib`. A script outside `hooks/` joins `"hooks", "lib"`
where it joined `"hooks"`. `tests/conftest.py#load_hook_module` takes a path
under `hooks/`, so a module is loaded as `lib/optin.py`.

**How a test file finds the repository.** Each file imports `ROOT` from
`tests/conftest.py` (line 987) where it assigned its own. 134 files assign
one from `__file__` today (executed: `git grep -l __file__ -- 'tests/test_*.py'`).
A file that needs another directory joins it under that `ROOT`.

**Which untargeted file is behaviour and which is text.** A file declaring
no `TARGET` is behaviour where it loads or runs shipped code, and text
otherwise. The reading is the pattern
`load_hook_module|load_module\(|\bload\(|run_hook|subprocess\.|spec_from_file_location|import_module|from conftest import .*\b(repo|git_repo|build_tracked_tree)\b`
over the file. It places files and gates nothing. Measured at `d4623900`
(executed):

- `tests/behaviour/` (43): `test_a_commit_names_its_repository.py`,
  `test_a_document_that_names_a_script_says_how_to_reach_it.py`,
  `test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`,
  `test_a_phase_hands_the_next_one_a_record.py`,
  `test_a_probe_that_commits_says_so.py`,
  `test_a_reference_root_is_read_and_never_taken.py`,
  `test_a_release_is_sized_by_a_criterion.py`,
  `test_a_section_marked_for_one_role_reaches_only_that_role.py`,
  `test_a_shrunken_corpus_declines_to_judge.py`,
  `test_a_signer_declares_its_pact.py`,
  `test_both_editions_carry_the_same_folds.py`,
  `test_chain_hooks_hardening.py`, `test_docs_line_wrap.py`,
  `test_evals_layout.py`, `test_every_orchestrator_act_names_its_delivery.py`,
  `test_every_reader_ends_a_line_where_gfm_does.py`,
  `test_first_setup_asks_once.py`, `test_no_document_names_the_old_roots.py`,
  `test_one_heading_rule_holds_to_commonmark.py`,
  `test_one_table_walker_reads_what_gfm_renders.py`,
  `test_one_word_one_meaning.py`, `test_release_hygiene.py`,
  `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`,
  `test_the_contributor_has_a_procedure.py`,
  `test_the_frozen_reading_never_grows.py`,
  `test_the_gate_asks_the_range_ci_will_ask.py`,
  `test_the_gate_names_every_step_ci_runs.py`,
  `test_the_guard_asks_once_per_session.py`,
  `test_the_hook_surface_git_offers.py`,
  `test_the_hooks_hide_what_a_renderer_hides.py`,
  `test_the_installer_writes_the_block_from_its_template.py`,
  `test_the_pull_request_language_is_the_repositorys.py`,
  `test_the_release_check_watches_what_ships.py`,
  `test_the_release_seal_is_drawn.py`, `test_the_root_migrates_itself.py`,
  `test_the_seal_is_taken_once_by_the_sealer.py`,
  `test_the_sealer_guarantees.py`, `test_the_set_a_work_item_always_has.py`,
  `test_the_stamp_reaches_the_person_it_is_drawn_for.py`,
  `test_the_suite_has_a_command_that_is_cheap_twice.py`,
  `test_the_windows_leg_runs_in_shards_that_make_the_whole.py`,
  `test_unverified_rows_close.py`,
  `test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`.
- `tests/text/` (48): every other file of `tests/test_*.py` that declares no
  `TARGET`. The phase that moves them lists the 48 in its record from the
  same pattern, and a file the pattern sends to `text` whose cases run a
  script through a helper the pattern does not name goes to `behaviour`,
  recorded as a divergence row.

**The module test files by area**, each keeping its file name:

- `tests/hooks/`: `test_blocks.py`, `test_cmdline.py`, `test_config.py`,
  `test_console.py`, `test_dispatch.py`, `test_gate.py`,
  `test_hooksession.py`, `test_implementer.py`, `test_implementer_mark.py`,
  `test_implementer_notice.py`, `test_launch.py`, `test_lint_python.py`,
  `test_mode_gate.py`, `test_one_heredoc.py`, `test_optin.py`,
  `test_question_gate.py`, `test_review_skill_gate.py`,
  `test_root_migrate.py`, `test_routing.py`, `test_routing_edit_gate.py`,
  `test_sealer_stamp.py`, `test_sealer_stamp_queue.py`,
  `test_session_lease.py`, `test_stub_remove.py`, `test_tokens.py`,
  `test_version_check.py`, `test_worktree_consent.py`,
  `test_worktree_guard.py`.
- `tests/skills/`: `test_agentic_pytest_record.py`, `test_arm_check.py`,
  `test_broad_gate.py`, `test_chain_check.py`, `test_coordinates.py`,
  `test_deferral_check.py`, `test_fold_check.py`, `test_mutation_check.py`,
  `test_pact_check.py`, `test_payload_meter.py`, `test_rule_changes.py`,
  `test_seal.py`, `test_seal_stamp.py`, `test_session_cost.py`,
  `test_settle.py`, `test_test_layout.py`, `test_unverified_check.py`.
- `tests/github/`: `test_close_issues_on_release.py`,
  `test_durations_union.py`, `test_gather_changelog.py`,
  `test_issue_claims_check.py`, `test_label_merged_on_release_branch.py`,
  `test_plugin_directory_check.py`, `test_publish_release_note.py`,
  `test_release_completeness_check.py`, `test_release_report.py`,
  `test_release_seal.py`, `test_roll_flow_measurement_issue.py`,
  `test_rules.py`, `test_run_tests.py`, `test_tracker_labels.py`.
- `tests/evals/`: `test_noninferiority.py`, `test_replay_targets.py`,
  `test_rule_cases.py`, `test_seed_defects.py`.

**Import mode.** pytest keeps its default `prepend` mode and no directory
under `tests/` gets an `__init__.py`. pytest puts `tests/` on `sys.path`
when it loads `tests/conftest.py`, which is how `tests/e2e/` files import
`conftest` today, so `from conftest import`, `from censuses import` and the
other helper imports keep working from every subdirectory. In this mode two
test files with one name fail collection, and the new case names the rule
before pytest's own error does.

**The census.** `tests/censuses.py#vacated_paths(rel, root)` reads, for
each tracked file at `hooks/lib/<name>`, `templates/records/<name>`,
`templates/setup/<name>` or `tests/<area>/<name>`, where `<area>` is one of
`hooks`, `skills`, `github`, `evals`, `behaviour` and `text`, the spelling one level up
(`hooks/<name>`, `templates/<name>`, `tests/<name>`) as a path no file
holds, and flags a line of a living file that spells it as a word (not
inside a longer path). It passes the records `OLD_NAME_RECORDS` lists, a
case `RECORDED_CASE` matches, a `<commit>:<path>` citation, the files of its
own `KEPT_FILES`, and a line under `# exempt from vacated_paths: <why>`. It
joins `CENSUSES`.

**The layout reader.** `test_layout.py --check` adds one refusal: a file
declaring a `.py` `TARGET` stands in `tests/<area>/`, where `<area>` is the
first segment of `TARGET` with a leading dot dropped, and a `TARGET` under
`tests/` keeps its file at `tests/`. A file under `tests/e2e/` keeps the
rules it has. The message names the directory the file belongs in.

## Rule changes

- nothing
  why: No rule of the policy root changes. The `docs/` edits are the spellings of moved paths and the grouping of `docs/README.md`'s rows into subject tables, which decide nothing. The one rule this work changes is `CONTRIBUTING.md` *The test layout*, which is outside the policy root and changes in the pull request with its reader.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The eight general skills | `skills/debug/`, `skills/build-fix/`, `skills/checkpoint/`, `skills/gap-analysis/`, `skills/security-audit/`, `skills/testing/`, `skills/learn/`, `skills/audit/` | No record shows one used (*Scope*, *The general skills*). Q2's default; git history holds each |
| Their names in the skill list and the cheat sheet | `README.md` *What ships* and `README.ko.md` *무엇이 들어 있나*, the `Skills` row; `README.md` *Cheat sheet* and its Korean counterpart, the `/agentic:security-audit` and `/agentic:testing` row | The list counts the fourteen that stay, and the cheat sheet loses the row for two commands that no longer exist |
| The repository root computed from each test file's path | 134 test files, each `ROOT = ...__file__...` or `HOOKS = ...__file__...` assignment | `tests/conftest.py#ROOT`, the one source, imported by each file |
| The single table of `docs/README.md` | `docs/README.md`, its table | One table per subject in the same file, each row unchanged |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
