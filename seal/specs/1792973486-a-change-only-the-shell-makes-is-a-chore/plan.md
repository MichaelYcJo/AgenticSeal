# Implementation Plan: a change only the shell makes is a chore

Approved 2026-10-26 by the orchestrator under the owner's automation answer, when `smith` was spawned.

## Summary

One phase. The smith inserts the two sentences `spec.md` *Scope* item 1
gives, word for word, into `CLAUDE.md` *The rule a mechanism is kept
against*, directly after its first sentence, and edits no other file. The
principle gets no `check:` line, and no other file is rewritten, because the
search in `spec.md` *Scope* item 3 found none that states the opposite.

## Technical context

What this builds on, read at `e1edfa43`:

- **The section.** `CLAUDE.md:14` is the heading *The rule a mechanism is
  kept against*. Its one paragraph runs from line 16 to line 30, and its
  first sentence ends `existing is no reason to keep it.` on line 17. The
  paragraph holds no `check:` line (executed: `grep -n 'check:' CLAUDE.md`
  finds only the mid-line mention on line 18).
- **Who writes `CLAUDE.md`.** `settle` writes only top-level `.md` files of
  the policy root (`skills/settle/SKILL.md` *Rule changes*), which is `docs`
  here because `seal/config.md` has no `Policy root` row (read). Pull
  requests edit `CLAUDE.md` in place: `5aed51cb` (#940) and `b451e503`
  (#941) last changed this section (executed: `git log -- CLAUDE.md`). The
  repository's `CLAUDE.md` holds no `specseal:start` marker (executed: grep,
  count 0), so neither `install.sh` nor `/specseal:update` writes into it.
- **The checks that read `CLAUDE.md`.** `.github/scripts/rules.py`
  `RULE_FILES` names `CLAUDE.md`, and `tests/test_rules.py` runs it over the
  tree. `tests/test_the_rules_claude_md_names_have_one_home.py`,
  `tests/test_no_passage_is_pasted_into_a_second_file.py`,
  `tests/test_one_word_one_meaning.py` and
  `tests/test_a_release_is_sized_by_a_criterion.py` read the file. No test
  pins a sentence of this section (executed: `git grep` over `tests`,
  `.github`, `skills`, `hooks` and `bin` for its first two sentences and its
  heading, no hit).
- **The premise.** The principle holds because work a work item owns is
  written through the edit tools, where `hooks/routing-edit-gate.py`
  refuses an edit on an undeclared branch (`skills/implement/SKILL.md`
  *1. Read the spec before the code*, read). For every agent, contract
  rule 9 makes that so (`skills/agent-contract/SKILL.md` *9 Edits go through
  the `Edit` tool*, read, held by `tests/test_edits_go_through_the_edit_tool.py`).
- **The memory.** The principle's only copy today is a session memory file
  outside the repository, which the orchestrator removes after the merge
  (`spec.md` *Scope* item 4).

**The failure scenario of the chosen approach, six months on.** A reviewer
cites the sentence to wave off a gap that work a work item owns does pass
through, such as a new edit tool the routing check does not match, or a
session that writes a work item's files through the shell. The sentence
does not cover either, because it names only a change that would be routed
`no work item`, but a reader in a hurry may still stretch it. The warden of
that later review is what catches the stretch. A second failure is drift: a
later document restates the principle in its own words, and the two copies
part. `tests/test_no_passage_is_pasted_into_a_second_file.py` catches a
pasted copy and not a reworded one, so that one is a reviewer's finding.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Two sentences inside the existing paragraph, after its first sentence; the build edits `CLAUDE.md` in place** (chosen) | The stretch and the drift of *Technical context* | Chosen. The first sentence weighs a mechanism by what it caught, and the new sentences say which catches count, so they read as its consequence. The owner named this section |
| **Replace the structure: give the principle a `CLAUDE.md` section of its own** | A heading of its own reads as a rule with its own scope, apart from the weighing it follows from. The file then holds two sections on when a mechanism earns its place, and a reader has to tell which one decides | Rejected. The premise that keeps the one paragraph, checked: its first sentence is the weighing the new sentences apply (`CLAUDE.md:16-17`, read), and the paragraph already gathers the section's other principles without sub-headings |
| **State the principle in the policy root through `## Rule changes`, for example in `docs/the-routing-check.md`, and link to it from `CLAUDE.md`** | The principle covers every gate and check, and a routing document would scope it to one. `docs/the-routing-check.md` does not exist until the settle that applies #1027's spec. The `CLAUDE.md` row would be a link to a home a session opens only when it already knows to | Rejected. The owner named `CLAUDE.md`, and `docs/the-record-layout.md` *The root records* makes it the home of the rules a session must hold |
| **Close the gap instead: a gate that reads `git status` after each Bash call** | It runs on every Bash call, and what it catches is chores. Each catch costs a question or a `seal no-work-item` run with nothing behind it, against `CLAUDE.md` *The goal a design is chosen against* | Rejected by the owner on 2026-10-26 (issue #1031 body) |
| **Add a `check:` line, or a test that pins the sentences' words** | The test proves the words exist and nothing about any gate. `.github/scripts/rules.py` says it cannot tell a test that exists from one that asserts the rule. A `check: none reader:` line at the paragraph's end would read as covering every sentence of a paragraph that has had none | Rejected. The section's other sentences carry no `check:` line, and its readers are the warden and the reviewer of a gate's pull request, through `CONTRIBUTING.md` *What a change to a gate must carry* |
| **Also rewrite the places that mention the shell route** (`spec.md` *Scope* item 3) | Each one restating the principle is a second source, and the sentence in #1027's spec would gain a later operation on text another unsettled spec adds, the shape #1025 reports as broken | Rejected. Each place states a fact the principle agrees with, and none calls the gap a weakness to close |
| **Also add the principle to `templates/claude-md-block.md`** | Every consuming repository's sessions would carry a rule about how this repository designs its gates | Rejected. The block governs a session's own conduct, and the owner named this repository's `CLAUDE.md` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The two sentences of `spec.md` *Scope* item 1 in `CLAUDE.md` *The rule a mechanism is kept against*, after its first sentence, with the paragraph's lines reflowed and no other word changed | `git diff --word-diff 61a8455a -- CLAUDE.md` (S1); `git grep -n 'only such a change passes through'` finds `CLAUDE.md` alone outside `seal/specs/` (S2); `bin/test tests/test_rules.py tests/test_the_rules_claude_md_names_have_one_home.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_a_release_is_sized_by_a_criterion.py -q` (S5) | 77761ea9 |

## Operational impact

None. No migration, environment variable, dependency or compatibility
change. The orchestrator removes the session memory file after the merge
(`spec.md` *Scope* item 4).
