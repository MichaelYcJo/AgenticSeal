# Implementation Plan: 1793240967-the-worktree-guard-was-never-weighed

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 4.

## Summary

The record decides removal: no catch in the issues, the 51 flow logs or the
records at 61 release tags, against about 7,000 lines of hook code and
about 116 s of recorded serial test time (executed: `wc -l` and
`.test_durations`, the moved press cases' 9.9 s left out). Phase 1 moves the `automation` press
reader out of `hooks/worktree_consent.py` into `hooks/lib/press.py`, so the
two gates that read it stop depending on the guard's files. Phase 2 removes
the guard, its consent record, the session lease and the plugin option,
with every case, fixture and person-facing row that stood on them; the
guard's policy document and index row stay for the settle's `remove`, and
`seal rules --check` excuses the document's `check:` lines until then.
Phase 3 removes the command readers only the guard used and prunes
`hooks/lib/cmdline.py` to what the commit notice reaches and reads. Phase 4 rewrites the remaining text that
names the guard and writes the changelog fragment. Each phase leaves its
narrow runs green.

## Technical context

- **Who reads what the guard owns** (executed, `git grep` at `56588d57`).
  `hooks/question-gate.py:53` imports `worktree_consent` for
  `is_routing_question` and `last_routing_answer`;
  `hooks/routing-edit-gate.py:265` imports it inside a function for
  `automation_answered`. Nothing else outside the guard imports it.
  `hooks/lib/tokens.py` is imported by `hooks/worktree-guard.py:212` alone,
  and `hooks/lib/one_heredoc.py` by `tokens.py:70` alone.
  `hooks/lib/cmdline_base.py` is imported by the guard (`:183`, `:224`) and
  `worktree_consent.py:94` alone. `hooks/lib/cmdline.py` is imported by the
  guard (`:203`), `tokens.py:71` and `hooks/implementer-notice.py:47`;
  after this work only the last remains, importing `drop_comments`,
  `drop_heredoc_bodies`, `parse_git` and `split_segments`.
  `hooks/lib/hooksession.py#claude_pid` is called by
  `hooks/session-lease.py:102` alone; `SESSION_VARIABLE` is read by
  `skills/implement/scripts/seal.py:2794`. `agentic-leases/` is written by
  `hooks/session-lease.py` and read by the guard alone.
- **The press reader** is `hooks/worktree_consent.py` from `PROJECTS_ROOT`
  (line 104) through `last_routing_answer` (ending at line 401), less
  `CONSENT_DIR`, `consent_path` and `granted`. It imports `glob`, `json`,
  `os`, `optin` and nothing from `cmdline_base` (read). Its cases are
  `tests/hooks/test_worktree_consent.py` classes `Test_automation_answered`
  and `Test__routing_preset`, and in `Test_module` the cases
  `test_a_session_id_that_reduces_to_nothing_has_no_transcript`,
  `test_no_case_reads_the_real_projects_root`,
  `test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone`, 25
  cases in all (read; counted in `.test_durations`, executed). `tests/conftest.py:488-501` and
  `:1563-1567` patch `worktree_consent.PROJECTS_ROOT`.
- **Why the guard's policy document stays until the settle.** The guard's
  document names five test files on its `check:` lines (executed:
  `test_worktree_guard.py` 7 times, `test_worktree_consent.py` 4,
  `test_creation_flow.py` 2, `test_the_hook_surface_git_offers.py` 2,
  `test_the_frozen_reading_never_grows.py` 1), and phases 2 and 3 delete
  them. `skills/implement/SKILL.md` *Document layout — two roots, three
  lifetimes* has a pull request leave the policy root to the settle, so the
  document and its `docs/README.md` row leave through `## Rule changes`, not
  in this pull request. `seal rules --check` therefore excuses a line in a
  section a pending `remove` with no `from` takes out, at a shared root, as
  the S9 excuser of
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py` already did:
  a refused `check:` line inside a section a pending `remove` takes out is
  excused and named. Both read that fact through
  `skills/settle/scripts/rule_changes.py#pending` and `#removed_by`, one
  reader. The exception to the layout rule that `trail/rounds/round-1.md`
  finding 1 offered in its place would have kept a second reading of the
  policy alive; the fold check needs neither, since it refuses an index row
  only once its document is gone.
- **Full history in CI.** `.github/workflows/test.yml:112-116` and
  `tests/text/test_ci_gives_the_checks_what_they_need.py` cite
  `tests/behaviour/test_the_frozen_reading_never_grows.py` as the case that
  resolves an old commit. Phase 3 deletes that file. The docstring of
  `tests/evals/test_replay_targets.py` says
  `test_a_named_case_is_read_at_every_release_tag` reads the release tags
  (read), which a depth-1 checkout lacks, so it becomes the cited example
  and `fetch-depth: 0` keeps its reason (`frame/questions.md` M1).
- **The failure scenario of the chosen approach.** In six months two live
  sessions share one working tree and one switches its branch. The other's
  next edits land on the switched-to branch, and nothing of this plugin
  stopped the switch. What still stands between them: `git switch` aborts
  where the switch would lose local changes (git-switch(1), read); the edit
  check refuses an edit on a branch no `routing.md` names
  (`docs/the-routing-check.md` *The edit check*); and the limit sentence
  in both READMEs tells a person to give each concurrent session its own
  worktree. A switch onto another declared branch with no conflicting
  local change passes all three. The record shows that shape never caught
  in two months, so it is stated as a limit and not guarded.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep the guard whole | The seven open issues stay open and each new git spelling is another work item, as 21 work items already were. The serial suite keeps paying its about 116 s. The premise that keeps it, that the record shows it catching what nothing else would, was checked across the tracker, the 51 flow logs and the records at 61 tags, and is false | Rejected |
| B. Narrow to worktree creation, the arm `docs/worktree-guard-spec.md` *Decided before git runs* says can only be judged before git runs | Keeps the creation ladder, the consent record, the frozen reader that places a creation, the token reader for `[worktree-ok]`, and the session count its ACTIVE and IDLE rows read: most of the cost. The arm's own `from-use` reports, #237, #257 and #894, are each it holding an unattended run. A worktree created when one session would have done costs disk, not another session's work, so the arm prevents no damage the record names | Rejected |
| C. Narrow to the switch arm's deny while another session is ACTIVE, the one row that could prevent damage | Keeps session detection (`ps`, `lsof`, tty times, transcripts, leases), the frozen reader and the list of git subcommands that leave the tree. #24 says the arm was never judged against a live session; the lease docstring and work item 1788846800 record it denying switches after every session had ended; #692 found that predicting a switch from command text does not converge; on Windows the count is always unusable (#723). Zero catches | Rejected |
| D. Replace the guard: a new, smaller check reading the session count only at `git switch` | A new mechanism with no catch to show for the old one, which `CLAUDE.md` *The rule a mechanism is kept against* asks to be argued from history. The question it would answer, which session is live in this tree, is the part that produced the false denies | Rejected |
| E. Remove the guard, its consent record, its lease, its option and the readers only it used; keep the press reader in a module of its own (chosen) | The failure scenario under *Technical context*: a switch under another live session onto a declared branch, with no conflicting change, passes. Stated as a limit in both READMEs | Chosen |
| F. Keep the press reader where it is, in a `hooks/worktree_consent.py` stripped to it | The file's name then names a record that no longer exists, and every reader of `hooks/question-gate.py` meets an import named for a removed guard | Rejected |
| G. Fold the press reader into `hooks/lib/routing.py` | One module would read two inputs, a model-written `routing.md` and a harness-written transcript, and its cases would join `tests/hooks/test_routing.py`, which #1142 edits in parallel (`tests/hooks/test_routing.py:134` per its body, read). A module of its own keeps the move a rename that the moved cases prove | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `hooks/lib/press.py` holding the press reader, moved byte for byte below a docstring that names no guard; `hooks/question-gate.py` and `hooks/routing-edit-gate.py` import `press`; `hooks/worktree_consent.py` imports the moved names from `press` so the guard keeps working until phase 2; the press cases moved to `tests/hooks/test_press.py` with the labels case of `tests/behaviour/test_the_guard_asks_once_per_session.py`; `tests/conftest.py`'s `PROJECTS_ROOT` patches point at `press` | The moved cases at the new path, no new red-first case: `tests/hooks/test_press.py`, `tests/hooks/test_question_gate.py`, `tests/hooks/test_routing_edit_gate.py`, `tests/hooks/test_worktree_consent.py`, `tests/hooks/test_worktree_guard.py`, `tests/skills/test_test_layout.py` | ec43e94b |
| 2 | `hooks/worktree-guard.py`, `hooks/worktree_consent.py`, `hooks/session-lease.py` and the process walk of `hooks/lib/hooksession.py` removed; `hooks/dispatch.py#GROUPS`, `hooks/hooks.json` and `.claude-plugin/plugin.json` as `frame/design.md` *Data & interfaces* states; every case, fixture, census entry and timing entry of `frame/design.md` *Removes* that stood on these files removed or rewritten; `docs/worktree-guard-spec.md`, its `docs/README.md` row and `tests/behaviour/test_release_hygiene.py`'s `2.50.1` exemption left in place for the settle, and `seal rules --check` excusing a refused `check:` line in a section a pending `remove` takes out, through `skills/settle/scripts/rule_changes.py#pending` and `#removed_by`, with `tests/github/test_rules.py#Test_main::test_a_refusal_in_a_section_a_pending_remove_takes_out_is_excused_and_named`; the gate rows, switch rows and lease sentence of `README.md` and `README.ko.md` removed and the limit sentence written under each gate table | `tests/hooks/test_dispatch.py`, `tests/hooks/test_implementer_mark.py`, `tests/hooks/test_hooksession.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_release_hygiene.py`, `tests/text/test_a_rider_reaches_its_file.py`, `tests/test_conftest.py`, `tests/test_censuses.py`, `tests/skills/test_test_layout.py`, `tests/skills/test_seal.py`, `tests/github/test_rules.py`, `tests/skills/test_fold_check.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` | f528f7a1 |
| 3 | `hooks/lib/cmdline_base.py`, `hooks/lib/tokens.py` and `hooks/lib/one_heredoc.py` removed with `tests/hooks/test_tokens.py`, `tests/hooks/test_one_heredoc.py` and `tests/behaviour/test_the_frozen_reading_never_grows.py`; `hooks/lib/cmdline.py` pruned to the closure of `hooks/implementer-notice.py`'s four imports and to the outputs it reads, so `parse_git`'s `chdirs`, `command_word`'s `unplaced`, `strip_subshell`'s `opened`, `split_segments_with_separators`, `WRAPPED`'s placement column and the rider on `chdirs` go, and `hooks/lib/cmdline.py` leaves `tests/text/test_a_rider_reaches_its_file.py`'s tuple; `tests/hooks/test_cmdline.py` pruned to the cases of what remains; the `cmdline_base` entries of `tests/censuses.py`; the full-history citation moved to `tests/evals/test_replay_targets.py#test_a_named_case_is_read_at_every_release_tag` | `tests/hooks/test_cmdline.py`, `tests/hooks/test_implementer_notice.py`, `tests/hooks/test_dispatch.py`, `tests/test_censuses.py`, `tests/text/test_ci_gives_the_checks_what_they_need.py`, `tests/github/test_rules.py` | 4c9abc11 |
| 4 | The text rows of `frame/design.md` *Removes* rewritten without the guard: `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/gate-misfired.md`, `skills/implement/SKILL.md:257-263` removed as a paragraph whose one example is gone, `skills/implement/orchestration.md:353,357` cited to `docs/the-routing-check.md` *The edit check*, and the hook, script and test comments; `changelog.md` written, naming the removal, the limit, the option a person may have set in `/config`, and the three directories under `.git` a person may delete | The sweep command of `frame/design.md` *Data & interfaces*, quoted in the phase record; `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/github/test_rules.py` | aeed95df |

## Operational impact

- **A person who updates** loses three hooks and the plugin option
  `worktree_guard_language`, declared one release earlier, in 0.24.0. A
  value set in `/config` is read by nothing. `SPECSEAL_LANG` is read by
  nothing; the 0.24.0 notes said it would be read through 0.24.x.
- **Files left on disk.** `<git-common-dir>/agentic-worktree-consent/`,
  `<git-dir>/agentic-worktree-choice/` and `<git-dir>/agentic-leases/` stay
  in clones that ran an earlier release. Nothing reads them, and the
  changelog fragment names them.
- **No new dependency, variable or migration.** The suite loses about 116 s
  of recorded serial time; the `.test_durations` entries of removed cases
  go with them.
- **Where this work meets its siblings in `release: 0.24.1`.** #1142 names
  `tests/censuses.py` and `skills/implement/orchestration.md:397`; #1046
  names `skills/implement/orchestration.md`, `skills/implement/SKILL.md`
  and `hooks/mode-gate.py:16`; #1091 names `skills/implement/SKILL.md`
  (read, each issue's body). The milestone's rule holds: the second to land
  takes the first's change from the release branch.
- **The orchestrator's acts after the pull request.** Comment the record and
  the decision on #1049, as its *Done when* asks, from `frame/design.md`
  *The record*. Name #1049, #20, #24, #630, #723, #886, #893 and #900 in the
  pull request body as closed by the removal, each with the reason that the
  code it reports on is gone. Name `frame/questions.md` P1 in the body.
