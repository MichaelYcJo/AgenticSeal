# Design: 1793240968-every-session-reads-bootstrap-and-parity-setup

Issue #1046, milestone `release: 0.24.1`. The branch is
`chore/1046-every-session-reads-bootstrap-and-parity-setup`, cut from
`release/v0.24.1` at `1e82fd0a`, and its head at framing is `e697e1cf`,
which adds only `routing.md`. Every coordinate below is read at `1e82fd0a`
unless it names another commit.

The issue's line numbers were taken at `0b75346f`. At `1e82fd0a` the two
sections stand one line lower, and their sizes are unchanged (executed,
`sed -n` over each range piped to `wc -w`):

| Section of `skills/implement/orchestration.md` | Lines | Words |
|---|---|---|
| *Orchestrator: Bootstrap* | 89 to 280 | 1,847 |
| *Orchestrator: Parity setup* | 281 to 301 | 146 |
| the whole file | 1 to 677 | 7,835 |

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/SKILL.md:28-31`: an orchestrating session reads `skills/implement/orchestration.md` before the first edit | Every orchestrating session pays for the whole file. The two sections apply only where no `seal/` root exists, or where a migration is being declared, so they leave the file every session reads |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it" | *Orchestrator: Parity setup* restates steps 2, 3, 5 and 6 of `skills/parity-setup/SKILL.md` *Procedure* (read, both files side by side). It becomes one sentence that sends a yes to that procedure, and does not move |
| `skills/implement/orchestration.md` *Orchestrator: which of these acts runs itself*: "The row set is mechanical" | The moved section keeps its `Orchestrator:` heading, so it keeps its row. `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py#FILES` reads the new file as a third file |
| `docs/the-agent-set.md` *What a spawn costs*: the acts table covers "both orchestration files" | A third file changes that sentence, through `## Rule changes` below |
| `skills/implement/SKILL.md` *Document layout, two roots, three lifetimes*: the policy root "is the baseline, and a pull request does not edit it" | The four `docs/` sentences this work moves change through `## Rule changes`. No file under `docs/` is edited |
| The pending add of `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md` to `docs/the-record-layout.md` *A change writes fragments, never a shared file*: a work item whose diff changes "a `skills/*/orchestration.md` file" ends its fragment with a `### Process changes` row | The bootstrap leaves the glob that rule names, so the rule names the new file too (`## Rule changes`). This work item's own diff changes `skills/implement/orchestration.md`, so its fragment carries a process row, written by the orchestrator with the fragment |
| Contract rule 19, and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which resolves every citation of a section in the tracked text files, `.py` docstrings included | Every citation of the two headings moves in the commit that moves the heading, or that case goes red |
| The spawn prompt for this framing: "a rename or move is proved by the existing tests at the new path; red-first cases are planned only for new behaviour" | The moved bootstrap is proved by the cases that read it today, re-pointed. One new case pins the one new sentence a session acts on, the pointer in `orchestration.md` |

## Scope

**In.**

1. *Orchestrator: Parity setup* is removed from
   `skills/implement/orchestration.md`. The Bootstrap's step 3 answers a yes
   with one sentence: the orchestrator reads `skills/parity-setup/SKILL.md`
   and follows its *Procedure*, then continues the work.
   `skills/parity-setup/SKILL.md`'s opening paragraph says that the
   bootstrap's yes runs this procedure, and that the command is for a later
   answer. The orchestrator reads the file rather than invoking the skill,
   because its frontmatter carries `disable-model-invocation: true`.
2. *Orchestrator: Bootstrap* moves, unchanged in substance, to a new file,
   `skills/implement/bootstrap.md`, under the same heading.
3. `skills/implement/orchestration.md`'s opening paragraph loses the clause
   that says it holds the root's creation and the parity setup, and gains
   one sentence: where no `seal/` whose `README.md` opens with the marker
   exists at `<repo>/seal/` or at `$(git rev-parse --git-common-dir)/seal/`,
   the orchestrator reads `skills/implement/bootstrap.md` first. That one
   sentence serves both sections, because the parity question is reached
   only through the bootstrap's step 3 and through `/agentic:parity-setup`.
4. The acts table: the Parity setup row goes, and its grounds join the
   Bootstrap row, whose `File` cell names the new file. The table's opening
   prose and its own row say three files where they say two.
5. Every reader of the two headings reads the new file or the procedure:
   `templates/setup/claude-md-block.md:16`, `hooks/mode-gate.py:15-16` and
   `:50-51`, and the cases listed under *Data & interfaces*.
6. The words of `skills/implement/orchestration.md` are counted with `wc -w`
   before (7,835 at `1e82fd0a`) and after, and both counts go into phase 2's
   record.

**Out, each with its reason.**

- `skills/verify/orchestration.md` *Measure the segment, and feed the flow
  log* stays. The issue keeps it: measuring each segment applies to every
  session.
- `.github/scripts/rules.py#RULE_FILES` does not gain the new file. The
  moved text carries no `check:` line (executed, `grep` over lines 89 to 301
  finds none), so `seal rules --check` reads nothing in it today and loses
  nothing by the move. `skills/writing-style/outside-the-review.md` already
  stands outside that list the same way. A later rule written into
  `bootstrap.md` with a check line adds the file in that change.
- The acts check is not widened to a glob. `skills/*/*.md` would sweep in
  `skills/verify/orchestration.md`, whose flow-log act the table holds
  outside on purpose, and `skills/writing-style/outside-the-review.md`
  (`plan.md` *Alternatives considered*, A6).
- Installed copies of the preset block in a person's `~/.claude/CLAUDE.md`
  are not edited. `/agentic:update` re-copies the block. Until it runs, the
  old sentence sends a session to `skills/implement/orchestration.md`, whose
  new opening sentence sends it on (`plan.md` *Operational impact*).
- Test function names stay, so `.test_durations` keeps its keys. Only the
  docstrings and comments that state where the bootstrap is now change.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A session in a repository that has its root | Given a repository with a `seal/` root carrying the marker, when the orchestrator reads `skills/implement/orchestration.md` before the first edit, then it reads neither section, and the file is smaller by the moved words less the words the two phases add to it | `git grep -n -e '## Orchestrator: Bootstrap' -e '## Orchestrator: Parity setup' -- skills/implement/orchestration.md` prints nothing. Phase 2's record holds `wc -w` before (7,835) and after, and names the sentences the phases added |
| S2. A fresh repository, reached through the preset block | Given no root at either place, when the session reads the preset block, then it is sent to `skills/implement/bootstrap.md` *Orchestrator: Bootstrap* first, and to `skills/implement/orchestration.md` *Orchestrator: how the work is routed* by that file's name | `tests/behaviour/test_first_setup_asks_once.py`, the preset cases, with the asserted path moved to the new file |
| S3. A fresh repository, reached through `orchestration.md` | Given no root at either place and a session that opens `skills/implement/orchestration.md` first, for instance under an installed block that predates this work, when it reads the opening paragraph, then one sentence names the condition and `skills/implement/bootstrap.md` | One new case in `tests/behaviour/test_first_setup_asks_once.py`, seen red against the tree before the sentence lands |
| S4. The person answers yes to the parity question | Given the bootstrap's step 3, when the person says the project ports an original, then the orchestrator follows `skills/parity-setup/SKILL.md` *Procedure*, and no second statement of the four fields stands anywhere | `tests/behaviour/test_chain_hooks_hardening.py#test_parity_declaration_is_bootstrappable_not_hand_written`, re-pointed, seen red with the new sentence deleted. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` stays green |
| S5. The moved text is the text that was there | Given phase 1's commit, when the section is compared with the new file's section, then the two are the same bytes | `diff` of `git show <phase 1 commit>:skills/implement/orchestration.md` from `## Orchestrator: Bootstrap` up to `## Orchestrator: how the work is routed`, against `skills/implement/bootstrap.md` from the same heading to its end, exits 0. Phase 2's record holds the command and its exit code |
| S6. The Bootstrap act keeps its delivery | Given the acts table, when the check reads its three files, then the Bootstrap row names `skills/implement/bootstrap.md` and `check: hooks/mode-gate.py`, and no row names `Orchestrator: Parity setup` | `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` |
| S7. No citation is left dangling | Given every tracked text file outside the records, when each citation of a section is resolved, then each resolves | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` |
| S8. Nothing an agent preloads carries the moved heading | Given the agents' `skills:` lists, when the marker check reads every injected file, then the new file is in none of them | `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`, unchanged |

## Data & interfaces

No code interface changes. What moves is text, and the cases that read it.

**`skills/implement/bootstrap.md`, new.** A `#` title, one opening paragraph
naming who reads the file (the orchestrator) and when (no root at either
place), then `## Orchestrator: Bootstrap` and its body as it stands after
phase 1. The section is the file's last, so `section(text, heading, 2)` in
the cases reads it to the end. The opening paragraph shares no run of 15
consecutive words with `skills/implement/orchestration.md`, the window
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` imports.

**`skills/implement/orchestration.md`.**

- Lines 3 to 8: the clause "creating the `seal/` root the first time a
  repository opts in, setting up parity mode where a project ports an
  original" goes. The pointer sentence of *Scope* item 3 is added in the
  same paragraph.
- Lines 263 to 269, step 3 of the Bootstrap: "**Yes**: the orchestrator runs
  the parity setup below, then continues the work." becomes the sentence of
  *Scope* item 1. It cites `skills/parity-setup/SKILL.md` *Procedure* and
  copies none of its words.
- Lines 281 to 301: removed (phase 1). Lines 89 to 280: removed (phase 2).
- Lines 616 to 625: "in this file or in `skills/code-review/orchestration.md`"
  names `skills/implement/bootstrap.md` too; "both files" becomes "the three
  files"; "in either file" becomes "in any of the three".
- Line 666, the Bootstrap row: `File` is `skills/implement/bootstrap.md`.
  `Grounds` gains the Parity row's grounds, reworded for the procedure: the
  yes follows `skills/parity-setup/SKILL.md` *Procedure* and nothing reads
  that it ran; the parity arm wakes on `seal/parity.md` existing, so a setup
  that never happened is silence rather than a refusal, and a guessed
  original produces a file that parses.
- Line 667, the Parity setup row: removed.
- Line 673, the table's own row: "the headings of both files" becomes "the
  headings of the three files".

**`skills/parity-setup/SKILL.md:15-17`.** "The `implement` skill's bootstrap
asks this question once, when it first sets a repository up. This command
is for when the answer was no at the time, ..." says instead that a yes
there runs the procedure below, read by the orchestrator, and that the
command is for an answer given later, a layout that predates the question,
or a changed original.

**`templates/setup/claude-md-block.md:16`.** "first follow the Bootstrap
section of `skills/implement/orchestration.md`" becomes "first follow
`skills/implement/bootstrap.md` *Orchestrator: Bootstrap*". "that file's
*Orchestrator: how the work is routed*" names
`skills/implement/orchestration.md` by path, since "that file" would
otherwise mean the bootstrap.

**`hooks/mode-gate.py:15-16` and `:50-51`.** The two docstring citations
name `skills/implement/bootstrap.md` *Orchestrator: Bootstrap*.

**Cases, each a reader re-pointed.**

| File | Coordinate | Change |
|---|---|---|
| `tests/behaviour/test_first_setup_asks_once.py` | `:56` `ORCH`, `:59-60` `bootstrap()` | `bootstrap()` reads `skills/implement/bootstrap.md` |
| the same | `:63-65` `both_halves()` | reads the new file as well, since its docstring says an absence has to hold in every file the text lives in |
| the same | `:828-830` | the asserted path in the preset's lead is `skills/implement/bootstrap.md` |
| the same | `:54-55`, `:175`, `:243`, `:422` | comments and docstrings that state where the bootstrap or the parity rule is now. History sentences, such as `:136`, stay |
| the same | new case | `orchestration.md`'s opening paragraph names `skills/implement/bootstrap.md` and both places the root can be (S3) |
| `tests/behaviour/test_chain_hooks_hardening.py` | `:237-247` | the bootstrap file names `skills/parity-setup/SKILL.md`, and that skill names `templates/setup/parity.md`; `seal/README.md` is asserted in the bootstrap file |
| `tests/text/test_the_settings_have_a_front_door.py` | `:18-19` `BOOTSTRAP` | `("skills", "implement", "bootstrap.md")` |
| `tests/text/test_the_rules_have_one_owner.py` | `:93` | the criterion's link carrier is the bootstrap file, in place of `ORCH_IMPL` |
| `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` | `:95-98` `FILES`, and the docstrings at `:11-13`, `:130` and `:284` | the new file is the third entry; "both" becomes what the tuple holds. The function name `test_both_orchestration_files_are_read` at `:508` stays |
| `tests/behaviour/test_docs_line_wrap.py` | the file list, `skills/implement/orchestration.md` at `:140` | the new file joins it, for the reason the comment at `:137-139` gives for `orchestration.md` |

## Rule changes

- change
  file: docs/the-agent-set.md
  section: What a spawn costs
  from: tables every `##` heading carrying the `Orchestrator:` marker in both
    orchestration files,
  to: tables every `##` heading carrying the `Orchestrator:` marker in
    `skills/implement/orchestration.md`, `skills/implement/bootstrap.md` and
    `skills/code-review/orchestration.md`,
- change
  file: docs/the-agent-set.md
  section: What a spawn costs
  from: A test holds the table against both files from both sides.
  to: A test holds the table against the three files from both sides.
- change
  file: docs/one-root-by-lifetime.md
  section: What first setup asks
  from: README.md *Coming up from 0.3.x* gives
    (`skills/implement/orchestration.md`, its bootstrap).
  to: README.md *Coming up from 0.3.x* gives
    (`skills/implement/bootstrap.md`).
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 처음 설정에서 무엇을 묻는가
  from: 옮긴다고 알리기만 합니다(`skills/implement/orchestration.md` 의 부트스트랩).
  to: 옮긴다고 알리기만 합니다(`skills/implement/bootstrap.md`).
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: A work item whose diff changes `CLAUDE.md`, an `agents/*.md`
    file or a `skills/*/orchestration.md` file ends its `changelog.md` with
  to: A work item whose diff changes `CLAUDE.md`, an `agents/*.md`
    file, a `skills/*/orchestration.md` file or
    `skills/implement/bootstrap.md` ends its `changelog.md` with

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The parity setup's second statement of four fields and the never-guess rule | `skills/implement/orchestration.md` *Orchestrator: Parity setup* | `skills/parity-setup/SKILL.md` *Procedure* states them, steps 2, 3, 5 and 6, and the Bootstrap's step 3 sends a yes there |
| The acts table's row for the parity setup | `skills/implement/orchestration.md` *Orchestrator: which of these acts runs itself*, the row `Orchestrator: Parity setup` | Its heading is gone. Its grounds join the Bootstrap row, whose step 3 now holds the act |
| The bootstrap, from the file every orchestrating session reads | `skills/implement/orchestration.md` *Orchestrator: Bootstrap* | `skills/implement/bootstrap.md` *Orchestrator: Bootstrap*, the same bytes |
| The opening paragraph's clause that the file holds the root's creation and the parity setup | `skills/implement/orchestration.md` *implement, the orchestrator's half*, the opening paragraph, lines 5 to 7 | The pointer sentence in the same paragraph |
| The assertion that `orchestration.md` names `templates/setup/parity.md` | `tests/behaviour/test_chain_hooks_hardening.py#test_parity_declaration_is_bootstrappable_not_hand_written` | The bootstrap file is asserted to name `skills/parity-setup/SKILL.md`, and that skill to name the template |
| The preset block's "the Bootstrap section of `skills/implement/orchestration.md`" and its "that file's" | `templates/setup/claude-md-block.md` *Git*, the routing bullet at line 16 | The new file's path and heading, and the routing section cited by its own path |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
