# Phase 2: 1793732301-the-readme-is-written-for-a-first-reader

## What this phase found

**The frame holds for this phase, with three exceptions below.** Read
before the build: `.claude-plugin/plugin.json` carries the `description`
the page opens with. Every coordinate the pin table names exists at
27a7a389c. `templates/setup/seal-README.md` gives the two by-hand moves as
code spans after "From local to shared:" and "From shared to local:". The
`readers` table of
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` has four
entries besides the two READMEs. `skills/implement/acts.md` holds the row
*Orchestrator: the run ends with a verifying round*. Q1 and Q2 stay open.
The page follows Q2's default (a): the owl is the relative path
`assets/seals/owl.svg`, and the workflow is a `mermaid` block.

**The manifest's sentence does not fit on one line.** It is 141 columns,
and `tests/behaviour/test_docs_line_wrap.py#LIMIT` holds README prose to
88. So the sentence stands as the paragraph directly under
`# AgenticSeal`, wrapped over two lines, as the old page wrapped it. The
assertion *Scope* 7 adds reads that paragraph with its line breaks folded,
and asserts that a blank line, and nothing else, stands between the title
and it. Judged against `frame/design.md` *Scope* 7 and S2, which say "the
first line", and against the `LIMIT` row of *Grounding*.
`docs/layout/one-root-by-lifetime.md` *Naming* says "the first line of
README.md under its title", and that sentence stood over the same
two-line paragraph before this phase.

**The import's refusal list has no home in the two documents `## Removes`
names.** Its row sends the list to `docs/layout/one-root-by-lifetime.md`
*Shared or local* and `templates/setup/seal-README.md`. Neither states the
refusals (read). Their only statement is the command itself,
`skills/implement/scripts/seal.py`, its refusal messages and
`seal import --help`, which names the two flags. The page states the one
refusal a first reader meets, that an import which cannot tell where the
zip came from writes nothing. It names `seal import --help` for the flags
and links the policy section for why a copy is not a sync. Judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has
one source": the command is that source here.

**`frame/questions.md:17` fails `tests/test_censuses.py`.** The case
`Test_module::test_every_file_no_module_file_declares_meets_every_census`
names that line under `real_identifiers`, for
the raw-file host named in Q2's options cell. This phase did not
change that file (read: `git diff --stat 27a7a389c a734aa9ea` lists no
path under `seal/`), and the census judges each file on its own, so the
failure predates the phase. The census reads every tracked file, and no
earlier phase ran it. The file is the framer's, so this phase does not
edit it.

**What left the page that `## Removes` does not name.** Each item either
restated a fact that has another home, or was history:

- The *Limits* bullet "Unread last fixes fail in one place" restated
  K3.2's fact a second time. *The review chain* now says the checks fail a
  ready pull request whose last fixes no round read, and links
  `docs/checks/the-pull-request-check.md`.
- The Windows bullet opened "one defect is still open there". Its own body
  said the console-encoding defect was closed, and named only the `py -3`
  fallback, unrun on Windows. The bullet now states those two facts and no
  count of open defects.
- The hook timings (220 ms to 104 ms, and 323 ms to 120 ms) were a
  measurement of one change, so they are history and go to git
  (`skills/core/SKILL.md`, "History goes to git"). The page keeps the fact
  that one process serves all the hooks of an event.
- The paragraph after the old gate table, on what CI reads of
  `routing.md` and of the `Seal-Routing` trailers. Its home is
  `docs/checks/the-routing-check.md`, which the routing-edit-gate row
  links.
- The paragraph on `verify` as the crafter's own gate, and the advice to
  call `@agent-agentic:proofer` from a fresh session. Their homes are
  `skills/verify/SKILL.md` and `agents/proofer.md`, which *The parties*
  links. The proofer's cold start stays, in one sentence.
- The homes of a leftover finding (`seal/follow-up.md`, `questions.md`, the
  pull request body). Their home is `docs/running/the-run.md` *The run*,
  which *The review chain* links.
- The sentence "Two things work with no agent at all", and the separate
  *Inline switches* table, whose one row joined *Commands*.
- Each hook row's edge cases, tightened under *Scope* 2: core-start's copy
  in a clone of this repository, review-skill-gate's pass for a skill a
  person invokes, question-gate's resumed and plain-text cases, and
  sealer-stamp's silence at a subagent's end. Each row links its home where
  one exists: `docs/checks/the-routing-check.md`,
  `docs/checks/the-session-hooks.md` *The implementer mark and notice*,
  `hooks/question-gate.py`, and `docs/checks/the-stamp.md`.

*Commands* keeps the old cheat sheet's commands and adds none.
`seal mode`, `seal pr-checks`, `seal export` and `seal import` stand under
*Shared or local*, where a first reader meets them.

**The paste check caught a sentence of this build.** The first draft of the
implementer-notice row shared two 15-word runs with
`docs/checks/the-session-hooks.md` (executed: the run named the pair). That
file's *The implementer mark and notice* is the row's home, so the row was
reworded and links it.

**Other statements of the facts the page moved** (contract rule 19). The
method is `git grep -n -i readme` over `skills`, `agents`, `docs`, `hooks`,
`templates`, `.github`, `CONTRIBUTING.md` and `CLAUDE.md`, with each hit
read. A search on one word makes this list a sample.

- `skills/implement/scripts/seal.py:1060` prints, when both roots exist,
  "the plugin README's *Shared or local* section has both commands". The
  section now names `seal mode` and says the two by-hand moves are in the
  root's own `seal/README.md`, so the message reaches the moves one link
  further on. It stands: changing a printed message is a script change,
  which `frame/design.md` *Data & interfaces* excludes, and contract rule 14
  would ask for a pin with it. It is handed back as a leftover.
- `skills/implement/scripts/seal.py:19` and `:1418` say what `README.md`
  carried, in the past tense, and stand as history. `:1758` and `:2499`
  speak of "the README's `mv` by hand". The by-hand `mv` now stands in
  `seal/README.md`, of which that phrase is still true, so both stand.
- `hooks/mode-gate.py:209` and `tests/hooks/test_mode_gate.py:321` say the
  gate row says "once per session per repository". The mode-gate row keeps
  those words.
- `tests/hooks/test_review_skill_gate.py:144` says the README steers toward
  a worktree per concurrent session. *What runs on your machine* keeps that
  sentence.
- `docs/checks/the-session-hooks.md:19`, `CONTRIBUTING.md:444` and
  `CONTRIBUTING.md:475` stay true: the gate table keeps one row per
  `GROUPS` script, the network paragraph stands in *What runs on your
  machine*, and *How it works* links the context-file study.
- The case names that say "cheat sheet"
  (`tests/text/test_a_document_has_room_for_the_next_fold.py`,
  `tests/text/test_settle_reads_before_it_removes.py`,
  `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`)
  stand. They name a table of commands, and both editions still carry one.
- `.test_durations` still names the two removed cases and the old name of
  the paste check's main case. It is the runner's timing file, and this
  phase does not edit it.

**The cases, each seen red** (executed):

- *Scope* 7, S2. The new assertion ran red against the old page before
  the rewrite, which held the badge under the title. After the commit,
  three `seal mutate` runs over `README.md` each went red:
  "inspects" changed to "reviews" in the sentence, the blank line under
  the title removed, and a paragraph "See below." put above the sentence.
- *Scope* 4, S4. With `BASELINE` gone,
  `test_no_pair_of_rule_documents_shares_a_run` ran red against the old
  page, naming `README.md` with `skills/implement/acts.md` and with
  `skills/implement/SKILL.md`. After the commit, `seal mutate` pasted
  K3.1's sentence back above *License*, and the case went red, naming
  `README.md` and `skills/implement/SKILL.md`, one run. The main case was
  renamed from `test_no_pair_shares_more_than_it_was_measured_at`, as S4
  allows, because no count is measured any more. `over_baseline` is now
  `shared_runs`, and its sentence drops "where N were measured". S5's case
  passes against it unchanged.
- `switch_block` reads the two moves from `templates/setup/seal-README.md`
  and runs them once. Two `seal mutate` runs over the template went red:
  `git add "…/seal"` changed to `git add seal` (git exited 128 from the
  subdirectory), and a third code span added to the first move (three
  spans where two are read).
- The other repoints only point a case at a new heading, or take a
  README.md arm out of a parametrisation, so they add no behaviour and owe
  no mutation run (`skills/verify/SKILL.md` *The narrow command still has
  to be able to fail*). The cases pass at the new heading:
  `test_the_readme_gives_the_switch_under_the_first_work_item`, renamed
  from `test_the_readme_gives_both_moves_under_first_run` because the
  section is now *Your first work item*, and
  `test_the_cheat_sheet_does_not_offer_the_runner` at `## Commands`. The
  four by-hand asserts left the first of them, with `COMMON` and `TOP`,
  which nothing else read.

**The narrow set** (executed, one command at a734aa9ea): `bin/test -q`
over the twenty-five modules of the pin table and five that read every
tracked `.md` or test file (`test_a_cited_section_stands_in_its_file.py`,
`test_one_heading_rule_holds_to_commonmark.py`, `tests/test_censuses.py`,
`test_a_cited_commit_outlives_the_squash.py`,
`test_a_shrunken_corpus_declines_to_judge.py`). 784 passed and 2 failed.
`test_both_editions_carry_the_same_folds.py::test_every_paired_document_carries_the_same_headings`
fails at line 116 with "README: the heading levels differ: English [1, 2,
3, 2, 3, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2], Korean [1, 2, 2, 2, 2, 2, 2, 2,
2, 3, 2, 3, 3, 2, 2, 2, 2]", which the plan expects until phase 3. The
census case fails on `frame/questions.md:17`, above. `uvx ruff check` and
`uvx ruff format --check` over the six changed test modules exited 0.

ded17da0b then edits `README.md` alone: the *Commands* section says the
`seal` commands are on the Bash tool's PATH and typed after `!`, the
routing paragraph says "the hooks" read `routing.md` where it said "each
hook", since core-start and lint-python do not, and one paragraph is
re-wrapped. The same set ran again over the tree ded17da0b commits, in the
same one command,
with the same result: 784 passed, and the same two cases failed on the
same lines (executed). The Status cell names ded17da0b.

**What phase 3 inherits.** The Korean arms this phase left in place are
`READMES["README.ko.md"]` and `LEFT_BEHIND["README.ko.md"]` in
`tests/behaviour/test_first_setup_asks_once.py`, the `README.ko.md` entry
of `readers`, the `README.ko.md` row of
`tests/behaviour/test_unverified_rows_close.py`, the Korean heading
literal in `tests/text/test_the_mode_is_a_row_and_a_command.py`, and the
Korean literals of `tests/behaviour/test_chain_hooks_hardening.py` and
`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`.
The by-hand asserts and `switch_block` no longer read either edition. The
English outline the Korean edition matches is the sequence above.
