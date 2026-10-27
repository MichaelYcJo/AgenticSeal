# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | bde49386 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 3 only: the rows of #1017 for `hooks/cmdline.py`, only the rows whose
code still stands, then `hooks/one_heredoc.py`, `hooks/tokens.py`,
`hooks/blocks.py`, `hooks/worktree_consent.py`, with k25 also run against
`tests/test_worktree_guard.py`, and `hooks/config.py`. Follow the method and
table shape of phases 1 and 2: rebuild each row at the head with
`bin/mutation-check` and `-x`, run a survivor again against the other test
files that load the module, write a case only where it survives all of them,
and see each new case red alone under its mutant. One commit per module, then
this record and phase 3's Status in `plan.md`. Build on `questions.md`'s
defaults Q1 to Q5. Fake every decision that reads the platform.

## The outcomes

21 rows, rebuilt as 21 mutants. 15 rows are killed by a new case, 3 were
already closed, 3 are equivalent. No row left the tree beyond the ten
`hooks/cmdline.py` rows `spec.md` already settles, and no row is a finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent |
|---|---|---|---|---|---|---|
| `hooks/cmdline.py` | 1bc3345a | 7 | 7 | 7 | 0 | 0 |
| `hooks/one_heredoc.py` | none | 2 | 2 | 0 | 0 | 2 |
| `hooks/tokens.py` | none | 1 | 1 | 0 | 0 | 1 |
| `hooks/blocks.py` | none | 1 | 1 | 0 | 1 | 0 |
| `hooks/worktree_consent.py` | 2b542a71 | 5 | 5 | 3 | 2 | 0 |
| `hooks/config.py` | bde49386 | 5 | 5 | 5 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`. A `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline. Inside single quotes, `\t`, `\r` and `\\`
are the characters as the source spells them.

The before column is the module's batch with `-x` in `--tests`, run when the
build reached the module: first against the module's own test file, then, for
each survivor, against every other test file that loads the module. The files
are listed above each table. The tree then differed from d60c125d only by this
phase's earlier test commits, and every red verdict in another file names a
case that stood at d60c125d. The after column is the same batch against the
module's own file at the module's commit. Every batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`,
or with the case's node id in single quotes for a parametrized one. Each of
those runs printed `red: the cases failed against the mutation (exit 1)` after
a passing baseline, and each failure was the case's own assertion.

## `hooks/cmdline.py`

Records: the issue body's m11, m17, m20, m24, m25, m26 and m47,
`phases/phase-6.md:937` to `:951` at `79f9c3fd`. The body's other ten rows
left the tree with `61a8455a` (`spec.md` *Rows whose code left the tree*) and
ran no mutant. Before: `tests/test_cmdline.py`, then
`tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py tests/test_a_rider_reaches_its_file.py tests/test_ci_gives_the_checks_what_they_need.py tests/test_dispatch.py tests/test_gate_judges_the_repo_it_commits_to.py tests/test_no_shape_the_base_stops_reads_silent.py tests/test_one_heredoc.py tests/test_the_frozen_reading_never_grows.py tests/test_tokens.py tests/test_what_the_reader_understands.py tests/test_worktree_guard.py tests/test_implementer_notice.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| m11: `drop_heredoc_bodies` opens a comment inside `${…}` | `'if not comment and ch == "#" and word_start and not braces:'` `'if not comment and ch == "#" and word_start:'` | SURVIVED, every file | red, `Test_drop_heredoc_bodies::test_accepts_a_body_dropped_where_the_shell_ends_it[a heredoc after a hash inside an expansion]` | killed by a new case |
| m17: `drop_heredoc_bodies` ends a `<<-` body only at an untabbed delimiter | `'                    if (line.lstrip("\t") if dashed else line).rstrip("\r") == delim:'` `'                    if line.rstrip("\r") == delim:'` | SURVIVED, every file | red, `Test_drop_heredoc_bodies::test_accepts_a_body_dropped_where_the_shell_ends_it[a dashed heredoc closed by a tabbed delimiter]` | killed by a new case |
| m20: `split_segments` answers clean for a split that failed | `'return [tokens for _, tokens in items], clean'` `'return [tokens for _, tokens in items], True'` | SURVIVED, every file | red, `Test_split_segments::test_refuses_an_unclosed_quote_as_a_clean_split` | killed by a new case |
| m24: `split_segments_with_separators` answers clean for a split that failed | `'return items, False'` `'return items, True'` | SURVIVED, every file | red, `Test_split_segments_with_separators::test_refuses_an_unclosed_quote_as_a_clean_split` | killed by a new case |
| m25: `merged_view` glues a redirection that carries its target | `'if m and m.end() == len(last):'` `'if m:'` | SURVIVED, every file | red, `Test_merged_view::test_refuses_to_glue_across_a_real_separator[a redirection carrying its target, then a pipe]` | killed by a new case |
| m26: `merged_view` glues `&` before `>` after any separator | `'if sep == "&" and tokens[0].startswith(">"):'` `'if tokens[0].startswith(">"):'` | SURVIVED, every file | red, `Test_merged_view::test_refuses_to_glue_across_a_real_separator[a pipe before a redirection]` | killed by a new case |
| m47: `_env_walk` reads no value after a cluster ending in `S` | `'value = takes_next or (at is not None and at[0] == "next")'` `'value = takes_next'` | SURVIVED, every file | red, `Test__env_walk::test_accepts_the_word_after_a_cluster_ending_in_s_as_its_value`, each of its two parameters by node id | killed by a new case |

## `hooks/one_heredoc.py`

Records: the round 3 comment's o2 and o10, `phases/phase-6.md:1697` at
`fc4f81ae`. Before: `tests/test_one_heredoc.py`, then
`tests/test_tokens.py tests/test_worktree_guard.py`. The module's code is
unchanged since 208803e6, where #942 measured it; only its docstring moved.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| o2: a command of one line is read | `$'    if not newline:\n        return None'` `$'    if False:\n        return None'` | SURVIVED, every file | SURVIVED | equivalent: with no newline, `partition` leaves `rest` empty and `rest.split("\n")` is `[""]`. The delimiter group is `[A-Za-z0-9_]+`, never empty, so `lines.index` raises `ValueError` and `_match` returns None, the None the skipped test returns |
| o10: a quoted word may cross a newline | `$'_QUOTED = r"\'[^\'\\n]+\'"'` `$'_QUOTED = r"\'[^\']+\'"'` | SURVIVED, every file | SURVIVED | equivalent: `_QUOTED` is read only through `_WORD` and `_OPENER`, and `_OPENER` is matched only against `first`, the text before the command's first newline. `first` holds no newline, so `[^']` and `[^'\n]` match the same text in it |

## `hooks/tokens.py`

Records: the round 3 comment's t5, `phases/phase-6.md:1728` at `fc4f81ae`.
Before: `tests/test_tokens.py`, then
`tests/test_worktree_guard.py tests/test_chain_hooks_hardening.py tests/test_noninferiority.py tests/test_cmdline.py`,
with `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
deselected, because it fails until phase 7 writes `overview.md`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| t5: `without_bodies` reads the text without the one shape's reduction | `'return drop_heredoc_bodies(command if reduced is None else reduced)'` `'return drop_heredoc_bodies(command)'` | SURVIVED, every file | SURVIVED | equivalent: where `one_heredoc.reduce` admits a command, `drop_heredoc_bodies` cuts the same body from it. The first line is a regular grammar with no comment, expansion, arithmetic or second `<<`, its quoted words close on that line, and both readers end the body at the first line equal to the delimiter. The mutant's text keeps only the ` <<'D'` the reduction takes out, whose words `<<` and D are never a token of `KNOWN`, since D is `[A-Za-z0-9_]+`. A probe confirmed the reading (below) |

## `hooks/blocks.py`

Records: the round 3 comment's k8, `phases/phase-6.md:1722` at `fc4f81ae`.
Before: `tests/test_blocks.py`, then
`tests/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/test_censuses.py tests/test_chain_check.py tests/test_config.py tests/test_every_reader_ends_a_line_where_gfm_does.py tests/test_fold_check.py tests/test_implementer_notice.py tests/test_one_table_walker_reads_what_gfm_renders.py tests/test_payload_meter.py tests/test_routing.py tests/test_seal.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_unverified_check.py tests/test_unverified_rows_close.py tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| k8: a comment closed anywhere on its line is read as closed | `'return at != -1 and CLOSER not in text[at + 2 :]'` `'return at != -1 and CLOSER not in text'` | SURVIVED on `tests/test_blocks.py`; red on `tests/test_the_hooks_hide_what_a_renderer_hides.py::test_where_the_walk_claims_to_be_exact_it_is` | SURVIVED on `tests/test_blocks.py`; the other file is unchanged | already closed |

## `hooks/worktree_consent.py`

Records: the issue body's k3, k10, k13, k23 and k25, `phases/phase-6.md:696`
to `:703` at `79f9c3fd`. Before: `tests/test_worktree_consent.py`, then
`tests/test_an_automation_run_meets_no_commit_prompt.py tests/test_dispatch.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_the_frozen_reading_never_grows.py tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py tests/test_question_gate.py tests/test_routing_edit_gate.py tests/test_worktree_guard_signals.py tests/test_a_creation_in_another_clone_asks_nobody.py tests/test_a_creation_is_judged_before_git_runs.py tests/e2e/creation/test_creation_flow.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| k3: `main` records a payload with no session id | `$'    if not session:\n        return\n    tool = data'` `$'    if False:\n        return\n    tool = data'` | SURVIVED, every file | red, `Test_main::test_refuses_a_payload_with_no_session_id_where_any_session_is_recorded` | killed by a new case, with `record` replaced by one that records any session |
| k10: `is_routing_question` takes a label set without counting each once | `'return phrases == sorted(ROUTING_LABELS)'` `'return set(phrases) == set(ROUTING_LABELS)'` | SURVIVED on `tests/test_worktree_consent.py`; red on `tests/test_question_gate.py::Test_routing_question_alone::test_refuses_a_near_miss_of_the_routing_question` | SURVIVED on `tests/test_worktree_consent.py`; the other file is unchanged | already closed |
| k13: `_routing_preset` reads an absent `multiSelect` as single-select | `'if not is_routing_question(q) or q.get("multiSelect") is not False:'` `'if not is_routing_question(q) or q.get("multiSelect", False) is not False:'` | SURVIVED, every file | red, `Test__routing_preset::test_refuses_a_question_whose_multi_select_is_absent` | killed by a new case |
| k23: `creation_directory` reads comments | `'text = cmdline.drop_heredoc_bodies(cmdline.drop_comments(command))'` `'text = cmdline.drop_heredoc_bodies(command)'` | SURVIVED, every file | red, `Test_creation_directory::test_refuses_a_creation_written_in_a_comment` | killed by a new case |
| k25: `split_with_separators` doubles no backslash on Windows | `'        command = command.replace("\\", "\\\\")'` `'        pass'` | SURVIVED on `tests/test_worktree_consent.py`; red on `tests/test_worktree_guard.py::Test_split_command::test_a_windows_path_survives_tokenizing` and `tests/test_worktree_guard.py::Test_walk_command::test_a_windows_cd_path_is_not_mistaken_for_an_expansion` | SURVIVED on `tests/test_worktree_consent.py`; the other file is unchanged | already closed |

## `hooks/config.py`

Records: the issue body's c6, c13, c14, c89 and c90, `phases/phase-6.md:836`
to `:850` at `79f9c3fd`. Before: `tests/test_config.py`, then
`tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_signer_declares_its_pact.py tests/test_blocks.py tests/test_chain_check.py tests/test_fold_check.py tests/test_mode_gate.py tests/test_one_table_walker_reads_what_gfm_renders.py tests/test_one_word_one_meaning.py tests/test_pact_check.py tests/test_routing.py tests/test_seal.py tests/test_test_layout.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_the_mode_question_is_asked_once.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_the_records_can_be_carried_out_and_in.py tests/test_unverified_rows_close.py tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py tests/test_broad_gate.py tests/test_rules.py tests/test_settle.py tests/test_question_gate.py tests/test_routing_edit_gate.py`,
with `--timeout 900`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| c6: `hidden_lines` names the last opener left open, not the first | `'return hidden, min(candidates) if candidates else None'` `'return hidden, max(candidates) if candidates else None'` | SURVIVED, every file | red, `Test_hidden_lines::test_refuses_to_name_a_later_fence_left_open_before_the_first` | killed by a new case |
| c13: `config_text` has no guard for an empty home | `$'    if not home:\n        return None, None\n    path = config_path(home)'` `$'    if False:\n        return None, None\n    path = config_path(home)'` | SURVIVED, every file | red, `Test_config_text::test_refuses_an_empty_home_whatever_the_working_directory_holds` | killed by a new case |
| c14: `unreadable_config` says `str(exc)` in place of the reason | `'why = exc.strerror if isinstance(exc, OSError) and exc.strerror else str(exc)'` `'why = str(exc)'` | SURVIVED, every file | red, `Test_unreadable_config::test_refuses_the_error_numbers_wording_and_names_the_reason_alone` | killed by a new case |
| c89: `baseline_commit` drops the walker's refusals from its `why` | `'return None, "; ".join([said, *refusals])'` `'return None, said'` | SURVIVED, every file | red, `Test_baseline_commit::test_refuses_a_table_the_walk_stops_and_names_why_its_row_went_unread` | killed by a new case |
| c90: `renamed_header` renames a header that holds no `Signer` | `$'    if "Signer" not in header:\n        return None, None'` `$'    if False:\n        return None, None'` | SURVIVED, every file | red, `Test_renamed_header::test_refuses_a_header_that_holds_no_signer` | killed by a new case |

## What this phase found

**Three modules got no commit, because no row of theirs needed a case.**
`hooks/one_heredoc.py`'s two rows and `hooks/tokens.py`'s one are
equivalent, and `hooks/blocks.py`'s one was already closed. `plan.md` says
each module lands in one commit. These three land in none, and this record is
where their outcomes stand. Phase 7's `overview.md` can carry it as a
divergence.

**t5's equivalence was read, then probed.** The reading says the two body
readers agree on every command `one_heredoc` admits. A probe,
`tests/test_tmp_t5.py`, ran once and was deleted. It read each command of
`tests/test_one_heredoc.py`'s `corpus()` and `program_corpus()`, with and
without a `[worktree-ok]` at the start of the body. For every command `reduce`
admitted, it compared the bare words `tokens._bare` reads in both texts. 1,488
commands were admitted, and in none did the two sets differ by a word other
than `<<` and the delimiter (`executed`).

**k8 is red on a file #942's record says it survived, under every reading
tried (Q1).** The record keeps no driver. By the order of group 15's decision
points, k8 is `leaves_open`'s closer, which is the table's pair. Three other
readings of "closed anywhere on its line" were run beside it:
`'at = text.rfind(OPENER)'` `'at = text.find(OPENER)'` in `leaves_open`, and
in `walk`, `'pending = leaves_open(line[line.index(CLOSER) + len(CLOSER) :])'`
`'pending = False'` and `'if CLOSER in line and not sticky:'`
`'if not sticky:'`. All four survive `tests/test_blocks.py`. All four are red
on the other files, the first two on
`tests/test_the_hooks_hide_what_a_renderer_hides.py::test_where_the_walk_claims_to_be_exact_it_is`,
whose corpus is seeded and the same on every run (`executed`). That file,
`tests/commonmark_oracle.py` and `hooks/blocks.py` are byte-identical between
208803e6 and the head (`executed`, `git diff --stat`). So #942's k8 was likely
a replacement none of these four is, and a warden who has another reading can
run it against the same files.

**k3 rests on a guarantee the module gives itself, and its case removes it
(contract rule 13).** With no session id, `consent_path` answers "" and
`record` writes nothing, so read against the real `record` the mutant is
equivalent. The case replaces `record` with one that records any session,
and asserts that `main` hands it nothing. A warden who reads k3 as equivalent
with the real `record` can rebuild the pair from the table.

**m47's case rests on GNU env's grammar, read and not run.** The case reads
`env -iS '' -vS 'git commit'`. An empty split string splits into no
argument, so GNU env goes on reading its options, and `-vS` names the string
`git commit`. The mutant reads the empty string as the program and ends env's
options there, so it never reads `git commit`. GNU env is not installed here,
as `tests/test_cmdline.py` already says of its env cases. The direction does
not rest on GNU alone. `reparsed_texts`' docstring says an extra reading
costs a stop and a missed string costs a silence, and the mutant misses one.

**Eight classes were added for functions that had none, two of them
private.** `spec.md` *In* item 2 puts a case in the class of the function the
mutant changes. That gave `Test_split_segments`, `Test__env_walk`,
`Test__routing_preset`, `Test_hidden_lines`, `Test_config_text`,
`Test_unreadable_config`, `Test_baseline_commit` and `Test_renamed_header`.
`bin/test-layout --check` asks each for an accepts case and a refuses case,
so each got both, though its mutant needed one. Each added accepts case reads
an input its function's existing cases do not: a quoted newline, a value with
two code spans, a two-cell header holding `Signer`, a decode error's own
words. The env cases already in `Test_module`'s `TEXTS` table and the
`baseline_commit` case already in `Test_module` stay where they were.

**`bin/test-layout --pairs` named the two new `drop_heredoc_bodies` cases as
one pair, so they are one parametrized case.** Each parameter was seen red
alone on its own mutant, by node id. The one pair `--pairs` still prints for
these files, `tests/test_config.py::Test_pact_signers`'s, is between two
cases this phase did not touch.

**One read ran while a mutant stood in the tree.** During the background
`hooks/config.py` batch against the other files, a `python3 -c` imported
`hooks/config.py` from `hooks/` to try a parity text for c89. The batch's
verdicts do not depend on it, because `mutation-check` removes the module's
bytecode before each run. The text was then confirmed by the c89 case, run
against the restored file. The next phase should read no module while that
module's batch runs.

**No case reads the platform, the process tree or the console without a
fake.** The k3 case runs `main` in the process, with stdin replaced. The c13
case moves the working directory with `monkeypatch.chdir`. The c14 case
builds its `OSError` with an errno and a reason of its own, and builds its
path with `os.path.join`. The k23 case has no backslash, so the Windows
doubling changes nothing in it.

**Run for the phase** (`executed`, at bde49386):
`bin/test tests/test_cmdline.py tests/test_one_heredoc.py tests/test_tokens.py tests/test_blocks.py tests/test_worktree_consent.py tests/test_config.py -q`
exited 0, 557 passed. `bin/test-layout --check` over the six files reads 6
files with 0 refused, and `--pairs` prints the one pair named above.
`uvx ruff check` and `uvx ruff format --check` over the three changed files
exit 0. `git diff d60c125d bde49386 -- tests` removes no line holding
`def test_`.
