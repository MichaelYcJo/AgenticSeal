# Design: 1793240967-the-worktree-guard-was-never-weighed

Issue #1049 asks the record to decide whether the worktree guard is kept,
narrowed or removed. The record holds no catch and four reports of the guard
stopping or misleading a run. This work removes the guard, the consent
record it reads, the session lease only it reads, and the command readers
only it uses. The `automation` press reader, which two other gates read, is
kept and moves to a module of its own.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while its history shows what it caught against what it costs. *The record* below shows no catch, so the guard goes. The same clause says a change removes in the same commit what stood on the old fact, which is why the lease, the frozen reader, the token reader and the plugin option leave with the guard |
| `CLAUDE.md` *The goal a design is chosen against* | Between two designs that catch the same defect, the one that stops to ask a person costs more. The guard asks or denies at every site it reaches; removal takes its prompts to zero and catches nothing less that the record shows it catching |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request states the failure direction (the change allows more: no switch and no creation is stopped), the prompt budget (it falls to zero for this gate), platform honesty (the `ps`, `lsof`, tty and transcript inspection leaves, so no platform remains untested for it) and what it removes (`## Removes` below). A removal adds no behaviour, so it plants no red-first case: the existing cases at their new paths and the cases rewritten for the new groups are the proof, as the spawn prompt's verification rule says |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | A pull request does not edit the policy root; the settle writes `## Rule changes`. Two of the removals below are applied by this pull request all the same, because the suite reads the policy root as it stands: `tests/github/test_rules.py#test_every_check_line_in_the_tree_holds` refuses the guard document's `check:` lines once the five test files they name are gone, and `tests/skills/test_fold_check.py#test_accepts_this_repository_with_no_flags` refuses an index row naming a file that is gone. Work item `1793140810-each-directory-holds-everything-in-one-level` edited `docs/` in its pull request for the same kind of reason (`e391ea04`, read). Every other rule change waits for the settle |
| `skills/settle/SKILL.md` *What the dry run shows* | The dry run shows a section whose heading is not there and refuses nothing, so the settle meets the two removals already applied and shows them as such |
| `docs/worktree-guard-spec.md` *Known limits* | "No case runs the switch arm against a live concurrent session; the cases stub the session count." The arm that would prevent damage has never been observed preventing it |
| `docs/the-routing-check.md` *The edit check* and `docs/the-review-record.md` *The run* | `hooks/routing-edit-gate.py` and `hooks/question-gate.py` read the press through `hooks/worktree_consent.py`. The press reader stays; its rules leave with the guard's document, so `## Rule changes` adds them to *The edit check* |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` names every removal once, for the review to read against the diff |
| `seal/threads/1793169129-the-creation-row-still-says-retry-with-worktree-ok/frame/design.md` *Rule changes* | An unsettled design of 0.24.0 changes two sections of `docs/worktree-guard-spec.md`. This design removes the document whole and merges later, so the settle's latest decision for that document is the removal. Its `frame/questions.md` row P1 is open and says "#1049 weighs it with the rest of the guard in 0.24.1" (read) |
| `seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/frame/plan.md` *Technical context* | The option `worktree_guard_language` was declared so that it leaves with the guard; `tests/behaviour/test_chain_hooks_hardening.py#test_every_option_the_manifest_declares_is_one_a_hook_reads` stays green once both leave (read, its round 1 `verdict: fixed 3bee2ec4`) |
| Issue #1049, body (no comments) | The request: record the catches with coordinates or state there are none, decide from the record, and name what `hooks/question-gate.py`, `hooks/routing-edit-gate.py`, `hooks/implementer-notice.py` and `hooks/lib/tokens.py` keep |

## The record

**Catches: none found.** Each search below is `executed` unless it says
otherwise.

| Where | What was read | Found |
|---|---|---|
| The issue tracker | `gh issue view` of #20, #24, #630, #723, #886, #893, #900, #692, #826, #237, #257, #894, #896, #1096; the issue body's title search over 809 issues (the issue author's, not re-run) | Seven open issues, each a defect or a limit of the guard. The four labelled `from-use` (#237, #257, #894, #896) are each the guard stopping or misleading a run. #24 says the `git switch` arm "has never been judged against a live concurrent session" |
| The `flow-measurement` logs | All 51 issues with that label, bodies and comments, searched for `worktree guard`, `worktree-guard` and `the guard` | Every mention is a segment that built, fixed or measured the guard, or a test run of its files. None records the guard stopping a switch or a creation that would have disturbed another session |
| Phase, round, memo and changelog records | Every file under `seal/` named `round-*`, `phase-*`, `gaps.md` or `changelog.md`, at each of the 61 release tags `v0.0.1` to `v0.24.0` | 2,349 mention lines across 84 work items. 21 of those work items were set aside as building or fixing the guard, the gates' shared command readers or the guard's tests (read, by slug). Outside them, 17 lines pair the guard with a verb such as asked, stopped, refused or held; read, none is a catch. One is a cost: `seal/specs/1788846800-an-exited-session-reads-as-live-for-five-minutes/changelog.md:11` (at its release tag) records the guard refusing switches for five minutes after every session ended |
| The code | `hooks/session-lease.py` docstring, lines 16 to 21 | A closed session's lease "hard-denied other sessions' branch switches (measured: two conversations ended minutes apart, and a third could not switch)" |
| The skills | `skills/implement/SKILL.md:257-263` | A session with five uncommitted files met the guard's question, and the usual right answer was not one of its two buttons |

**Cost.** `wc -l` at `56588d57`: `hooks/worktree-guard.py` 3,667,
`hooks/lib/cmdline_base.py` 2,288, `hooks/worktree_consent.py` 630,
`hooks/lib/cmdline.py` 1,382, `hooks/session-lease.py` 128,
`hooks/lib/tokens.py` 118, `hooks/lib/one_heredoc.py` 107,
`docs/worktree-guard-spec.md` 713. Recorded durations in `.test_durations`
(last written by `8a1173c8`): `tests/hooks/test_worktree_guard.py` 354
cases 75.1 s, `tests/hooks/test_worktree_consent.py` 54 cases 18.6 s,
`tests/e2e/creation/` 9 cases 12.2 s,
`tests/behaviour/test_the_hook_surface_git_offers.py` 7 cases 10.7 s,
`tests/hooks/test_session_lease.py` 31 cases 7.4 s, and under 2.5 s for the
rest, against 1,235.6 s for all 6,774 recorded cases. `git log` counts 30
commits to `hooks/worktree-guard.py` since the repository's first commit on
2026-08-31.

## Scope

**In.**

1. The `automation` press reader leaves `hooks/worktree_consent.py` for
   `hooks/lib/press.py`, unchanged in behaviour: `ROUTING_LABELS`, `PRESET`,
   `PROJECTS_ROOT`, `_DECORATION`, `leading_phrase`, `is_routing_question`,
   `transcript_for`, `_routing_preset`, `_routing_answer`, `_content`,
   `_clone_of`, `automation_answered`, `UNREAD` and `last_routing_answer`.
   `hooks/question-gate.py` and `hooks/routing-edit-gate.py` import it there.
   Its cases move with it.
2. The guard leaves: `hooks/worktree-guard.py`, the rest of
   `hooks/worktree_consent.py` (the consent record and its writer), and
   `hooks/session-lease.py`, whose lease nothing else reads (executed,
   `git grep agentic-leases`). `hooks/dispatch.py#GROUPS` loses them, the
   `post-agent` group and its `hooks/hooks.json` entry go, and
   `.claude-plugin/plugin.json` loses `userConfig`, whose one option
   configured the guard.
3. The readers only the guard used leave: `hooks/lib/cmdline_base.py`,
   `hooks/lib/tokens.py` (only the guard imports it, executed),
   `hooks/lib/one_heredoc.py` (only `tokens.py` imports it, executed), the
   process walk in `hooks/lib/hooksession.py` (`PID_VARIABLE`, `is_claude`,
   `claude_pid`, `claude_ancestor`; `SESSION_VARIABLE` stays for
   `skills/implement/scripts/seal.py`), and every definition of
   `hooks/lib/cmdline.py` that `hooks/implementer-notice.py`'s four imports
   do not reach. A name-based closure from `drop_comments`,
   `drop_heredoc_bodies`, `parse_git` and `split_segments` keeps 18 top-level
   names and drops 20 (executed, an `ast` walk; the build confirms it).
4. Every case, fixture, census entry, timing entry and comment that stood on
   the removed code is removed or rewritten, and every text a person or a
   session reads stops naming the guard: `README.md`, `README.ko.md`,
   `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/gate-misfired.md`,
   `skills/implement/SKILL.md`, `skills/implement/orchestration.md`.
5. `README.md` and `README.ko.md` state the limit once, under the gate
   table: no hook of this plugin stops a session from switching the branch
   of a working tree another session is using, so concurrent sessions each
   take their own worktree.
6. `docs/worktree-guard-spec.md` and its row in `docs/README.md` are deleted
   by this pull request (*Grounding*, the layout row). The other policy
   changes are `## Rule changes` for the settle.

**Out.**

- Removing the files the guard left under people's git directories
  (`agentic-worktree-consent/`, `agentic-worktree-choice/`,
  `agentic-leases/`). Nothing reads them after this work, and a cleanup hook
  would be a new mechanism with no catch to show. The changelog fragment
  names them so a person can delete them.
- `evals/behaviour/proofer/replay-1791779434-r5/`. It replays a review round
  of the guard's own work item against that round's commits, which its
  `scaffold.sh` fetches by hash (read), so it does not read this tree's
  guard.
- `skills/implement/scripts/seal.py`'s messages about a switch over a staged
  change (`:2554`, `:2681`) and `skills/config/SKILL.md:172`. Their "guard"
  is `seal mode`'s own refusal, not the worktree guard (read).
- Closing the seven open issues and recording the decision on #1049. Both
  are the orchestrator's acts after the pull request; `frame/plan.md`
  *Operational impact* lists them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A switch or a creation meets no hook of this plugin | Given an opted-in repository, when a session runs `git switch x` or `git worktree add ../w -b w`, or spawns an Agent with `isolation: "worktree"`, then no `PreToolUse` group of `hooks/dispatch.py` holds a gate that reads the command for a switch or a creation | `tests/hooks/test_dispatch.py`, its cases over `GROUPS` rewritten to the new groups |
| S2 The press is read as before, from its new module | Given the cases of `tests/hooks/test_worktree_consent.py` that drive `automation_answered`, `last_routing_answer`, `_routing_preset` and `is_routing_question`, when they run against `hooks/lib/press.py`, then each passes unchanged in what it asserts | `tests/hooks/test_press.py`, `tests/hooks/test_question_gate.py`, `tests/hooks/test_routing_edit_gate.py` |
| S3 The commit notice keeps its reading | Given `hooks/lib/cmdline.py` pruned to what `hooks/implementer-notice.py` reaches, when a command that runs `git commit` is read, then the notice decides as before | `tests/hooks/test_implementer_notice.py`, `tests/hooks/test_cmdline.py` (the cases of kept functions) |
| S4 A person reads no row for a removed hook | Given `hooks/dispatch.py#GROUPS`, when the gate tables of `README.md` and `README.ko.md` are read, then each registered script has one row and no row names `worktree-guard`, `worktree_consent` or `session-lease` | `tests/behaviour/test_chain_hooks_hardening.py#test_the_gate_table_has_one_row_for_each_script_groups_registers` |
| S5 The manifest declares no option nothing reads | Given `.claude-plugin/plugin.json` without `userConfig`, then no script under `hooks/` reads a `CLAUDE_PLUGIN_OPTION_` variable | `tests/behaviour/test_chain_hooks_hardening.py#test_every_option_the_manifest_declares_is_one_a_hook_reads`, its branch for `worktree_guard_language` removed |
| S6 Every check line and index row still resolves | Given the guard's document and its index row deleted, then every `check:` line in the tree names a file that exists and `seal fold` accepts the index | `tests/github/test_rules.py#test_every_check_line_in_the_tree_holds`, `tests/skills/test_fold_check.py#test_accepts_this_repository_with_no_flags`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_section_stands_in_its_file` |
| S7 Nothing outside the records names what was removed | When the sweep command under *Data & interfaces* runs, then it prints only lines under `seal/threads/` and `evals/behaviour/proofer/replay-1791779434-r5/`, the two lines of `docs/the-routing-check.md` and `docs/the-review-record.md` that `## Rule changes` corrects at the settle, and the changelog fragment this work writes | the command, run by the crafter at the last phase and quoted in its phase record |

## Data & interfaces

- `hooks/dispatch.py#GROUPS` after the build: `pre-bash` holds
  `mode-gate.py`; `pre-agent` holds `implementer-mark.py`; `post-bash` holds
  `implementer-notice.py`; `post-edit` holds `lint-python.py` and
  `sealer-stamp-queue.py`; `post-agent` is gone, and so is the
  `PostToolUse` entry of `hooks/hooks.json` whose command runs
  `dispatch.py post-agent`. The other groups are unchanged.
- The sweep command of S7, one line:
  `git grep -n -i -e worktree.guard -e worktree_consent -e session-lease -e cmdline_base -e one_heredoc -e worktree-ok -e shared-tree-ok -e agentic-leases -e worktree_guard_language -e WORKTREE_GUARD`
- `hooks/lib/press.py` exposes `automation_answered(top, session,
  transcript_path="")`, `last_routing_answer(top, session,
  transcript_path="")`, `is_routing_question(question)`, `UNREAD`,
  `ROUTING_LABELS`, `PRESET` and `PROJECTS_ROOT`, with the signatures
  `hooks/worktree_consent.py` gives them at `56588d57`.
- `.claude-plugin/plugin.json` loses its `userConfig` key. Its `version`
  stays as it is; the orchestrator moves it.
- Nothing is written to a person's disk any more by these hooks, and nothing
  that was written is read.

## Rule changes

- remove
  file: docs/worktree-guard-spec.md
  section: The worktree guard
- remove
  file: docs/README.md
  section: The checks
  from: | `docs/worktree-guard-spec.md` | what the worktree guard refuses, and why |
- change
  file: docs/the-routing-check.md
  section: The edit check
  from: Where the person pressed `automation` on the routing question, read
    through `hooks/worktree_consent.py#automation_answered`, it names no
    question tool;
  to: Where the person pressed `automation` on the routing question, read
    through `hooks/lib/press.py#automation_answered`, it names no question
    tool;
- add
  file: docs/the-routing-check.md
  section: The edit check
  to: **The `automation` press is the person's own click on the routing
    question, read from the session's main transcript, and nothing the
    model writes stands in for it.** `hooks/lib/press.py` is its one reader,
    and the edit check and `hooks/question-gate.py` both ask it. The
    transcript is the payload's `transcript_path` where its file name is the
    session id followed by `.jsonl`, and otherwise the one file of that name
    under `~/.claude/projects/`, so a subagent reaches its parent's answer;
    no other session's file and no `subagents/` file is read. The answer is
    read only from a harness-written `AskUserQuestion` result: a `user`
    entry that names an earlier `AskUserQuestion` call by `tool_use_id`,
    carries `isSidechain` set to `false`, and holds a structured
    `toolUseResult`. The routing question is the one single-select question
    whose three options lead with `automation`, `per axis` and
    `no work item`, a label's lead being its text folded to lower case and
    cut where a space is followed by an opening parenthesis, an em dash or a
    hyphen. The answer counts only where it equals one of the option labels
    exactly, so a typed answer is not read. The result entry's own `cwd`
    must lie in the same clone as the repository the gate judges. Of every
    answer to the routing question from that clone, the latest stands, so a
    later `per axis` or `no work item` takes the press back. A `routing.md`
    is never read for it, and every way a read fails is no press. A run
    resumed in a new session, by `/clear`, a new `claude` start or another
    machine, has no press until question 1 is put again; `claude --resume`
    and compaction keep the transcript, so the press survives them.
    check: tests/hooks/test_press.py tests/hooks/test_question_gate.py
- change
  file: docs/the-review-record.md
  section: The run
  from: The file is written by the model, which is why the worktree guard
    never reads it as consent.
  to: The file is written by the model, which is why no gate reads the
    `automation` press from it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The worktree guard | `hooks/worktree-guard.py` | Nowhere. *The record*: no catch. The limit is one sentence in `README.md` and `README.ko.md` under the gate table |
| The consent record and its writer | `hooks/worktree_consent.py`, all but the press reader | Nowhere; only the guard read the record. The press reader lands in `hooks/lib/press.py` |
| The session lease | `hooks/session-lease.py` | Nowhere; only the guard read `agentic-leases/` (executed, `git grep`) |
| The frozen command reader | `hooks/lib/cmdline_base.py` | Nowhere; only the guard and the consent writer imported it (executed) |
| The consent token reader | `hooks/lib/tokens.py` | Nowhere; only the guard imported it (executed) |
| The one heredoc shape | `hooks/lib/one_heredoc.py` | Nowhere; only `tokens.py` imported it (executed) |
| The process walk | `hooks/lib/hooksession.py#PID_VARIABLE`, `#is_claude`, `#claude_pid`, `#claude_ancestor` | Nowhere; only the lease writer and the guard called them (executed). `SESSION_VARIABLE` stays |
| The guard's wider command reading | `hooks/lib/cmdline.py#unglued`, `#merged_view`, `#host_word`, `#reparsed_texts`, `#substitution_bodies` and the private helpers and constants only they reach (`ENV_OPTIONS`, `ENV_STRING`, `SHELLS`, `STRING_HOSTS`, `_ENV_LONG`, `_ENV_SHORT`, `_env_long`, `_env_option`, `_env_walk`, `_env_words`, `_hands_a_string`, `_heredoc_end`, `_paren_end`, `_string_at`, `_without_redirections`) | Nowhere; `hooks/implementer-notice.py`'s four imports do not reach them (executed, `ast` closure) |
| Three hook registrations and a group | `hooks/dispatch.py#GROUPS` entries for the three hooks, the `post-agent` group; the `hooks/hooks.json` `PostToolUse` entry that runs `dispatch.py post-agent` | The groups keep their other gates |
| The plugin option | `.claude-plugin/plugin.json` `userConfig` | Nowhere; it configured the guard's language. `SPECSEAL_LANG` is read by nothing after this |
| The guard's policy document and its index row | `docs/worktree-guard-spec.md`; `docs/README.md` *The checks*, its row | Deleted by this pull request (*Grounding*); the press rules land in `docs/the-routing-check.md` *The edit check* at the settle |
| The guard's cases | `tests/hooks/test_worktree_guard.py`, `tests/hooks/test_worktree_consent.py` (all but the press cases), `tests/e2e/creation/`, `tests/behaviour/test_the_hook_surface_git_offers.py`, `tests/text/test_guard_resolves_the_tree_it_judges.py`, `tests/behaviour/test_the_frozen_reading_never_grows.py`, `tests/hooks/test_session_lease.py`, `tests/hooks/test_tokens.py`, `tests/hooks/test_one_heredoc.py`, the process-walk cases of `tests/hooks/test_hooksession.py`, the cases of `tests/hooks/test_cmdline.py` for removed definitions | Nowhere; what they pinned is gone. The press cases land in `tests/hooks/test_press.py`, and so does `tests/behaviour/test_the_guard_asks_once_per_session.py#test_the_labels_match_the_routing_question_the_orchestrator_asks`, unless the layout check places it elsewhere |
| Cases elsewhere that used the guard as their subject | `tests/hooks/test_implementer_mark.py#test_a_broken_mark_gate_leaves_the_worktree_guards_verdict_alone`; `tests/behaviour/test_one_word_one_meaning.py#test_the_worktree_spec_is_still_the_model` and the guard's entries in `GRAINS` and the Korean grains; `tests/behaviour/test_release_hygiene.py`'s entry for `docs/worktree-guard-spec.md`; `tests/text/test_a_rider_reaches_its_file.py`'s `hooks/worktree-guard.py` entry; the `cmdline_base` parameter of `tests/hooks/test_dispatch.py` | Nowhere, or rewritten to a hook that remains where the case's property still has a subject (`tests/hooks/test_dispatch.py`, `tests/skills/test_test_layout.py`, `tests/test_censuses.py` fixture text) |
| Fixtures, census entries and timing entries | `tests/conftest.py` (the guard loader, the consent directory, the lease directory, the shared-tree prompt texts, the option's `os.environ.pop`, `ps_names_the_parent_or_skip`), `tests/test_conftest.py`'s guard stand-in case, `tests/censuses.py` (the `cmdline_base` frozen and vacated entries, the `SPECSEAL_LANG` comment), `.test_durations` entries of every removed case | Nowhere; each stood on removed code. `tests/conftest.py`'s `PROJECTS_ROOT` patch moves to `press` |
| Text that named the guard | `README.md` and `README.ko.md` (three gate rows, the `[worktree-ok]`, `[shared-tree-ok]`, `WORKTREE_GUARD_IDLE_MIN` and option rows, the lease side effect, the guard's grain); `CONTRIBUTING.md:76`; `.github/ISSUE_TEMPLATE/gate-misfired.md:3,8`; `skills/implement/SKILL.md:257-263`; `skills/implement/orchestration.md:353,357`, cited to `docs/the-routing-check.md` *The edit check* instead; comments in `hooks/dispatch.py`, `hooks/implementer-mark.py`, `hooks/mode-gate.py`, `hooks/question-gate.py`, `hooks/review-skill-gate.py`, `hooks/routing-edit-gate.py`, `hooks/sealer-stamp-queue.py`, `hooks/lib/cmdline.py`, `hooks/lib/hooksession.py`, `skills/verify/scripts/session_cost.py:2886`, `skills/implement/scripts/seal.py:55-56`; `tests/skills/test_seal.py:850`'s planted name; `.github/workflows/test.yml:112-116` and `tests/text/test_ci_gives_the_checks_what_they_need.py`, whose example of a case needing full history becomes `tests/evals/test_replay_targets.py#test_a_named_case_is_read_at_every_release_tag` (`frame/questions.md` M1) | Rewritten in place, each without the guard |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
