# Implementation Plan: settle squashes specs into docs/ in place (#953)

Approved 2026-10-20 by the orchestrator, under the owner's `automation` answer and on `questions.md` Q1–Q5's stated assumptions, when `smith` was spawned for phases 1 and 2; phases 3–5 follow in a second spawn.

## Summary

`settle` stops asking a session to write prose into `docs/` beside a marker.
It applies the `## Rule changes` each released spec states. It rewrites in
place, works in merge order, refuses what it cannot place, and removes each
applied directory whole. The CI readers tell a settle from a deletion by
replaying those changes over the base, which needs no marker. `fold-check`
holds every document within one read against one token row, and holds
the index in `<policy root>/README.md`. The prose and the pins that state the
appending fold are rewritten in the same commits. Five phases, each a vertical
slice ending in green narrow cases.

## Technical context

What this builds on, read in this framing:

- `skills/settle/scripts/settle.py` (1057 lines): `#survey` (line 305) lists
  candidates through `unverified_check.py#folded_items` and
  `#retired_by_rule`. `#retire` (561) removes by marker or rule.
  `#retire_process` (827) and `PROCESS_DIRS`/`PROCESS_FILES` (697–718) are
  the process-record arm. It refuses local mode, and keeps doing so.
- `skills/verify/scripts/unverified_check.py`: `FOLD_MARKER` (126),
  `#live_lines` (633), `#folded_items` (1266), `#retired_by_rule` (1394), and
  the `--baseline` arm that excuses a removal (1705–1735).
- `skills/code-review/scripts/chain_check.py#retired` (1771): marker, then
  rule.
- `skills/settle/scripts/fold_check.py` (722 lines): `#target_problem` (239),
  the one resolver `.github/scripts/rules.py#target_problem` delegates to;
  `#shape_problems` (292, marker-bound, kept); `#ceiling_problems` (378) with
  `#parse_over` (524) and `#marker_digest` (336), the freeze;
  `DOCS = "docs"` (82). Rows are read through `hooks/config.py#config_rows`.
- `tests/conftest.py#cutoff_item_is_traceable` (292) reads `folded_items`.
- The tests that hold the appending shape, all of them listed in `spec.md`
  `## Removes`. The biggest are `tests/test_settle_reads_before_it_removes.py`
  (1271 lines, 50 cases) and `tests/test_a_document_has_room_for_the_next_fold.py`
  (605).
- The Read tool's limits, measured in this session: 25,000 tokens per call,
  and 2000 lines per call by its own description. Tokens bind first here
  (`spec.md`, *The one-read row*).

**Failure scenario of the chosen approach, six months on.** Someone hand-edits
`docs/` in a work item's pull request because no gate stops it (Q3). A later
spec's `change` then quotes text the hand edit already moved, and `settle
--apply` refuses that spec at the owner's settle. Nothing is lost: the
refusal is loud and the directory stays. But the fix lands at settle time,
months after the author left, and that is the cost Q3 accepts. The second
scenario is the replay predicate refusing a correct settle whose pull request
also hand-edited a named text (`spec.md`, *The settled predicate*). It errs
toward keeping a directory, and a person sees the refusal at exit 1.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1a. `settle.py` applies the operations itself and writes `docs/` | a bug in the applier rewrites a document wrong across many specs at once | **chosen.** The judgment now happens when the spec is written and reviewed, so applying it judges nothing. A bug is caught by fixture cases and by the replay predicate, which re-derives the result independently of the commit |
| A1b. Keep today's structure: the command lists, and a session writes each rule by hand (`skills/settle/SKILL.md` line 24; `docs/one-root-by-lifetime.md` row *What `settle` is*) | the session paraphrases; "refused, never guessed" cannot be held, because nothing compares the hand text with the operation; every settle costs a judgment pass, so the owner cannot call it at any moment | rejected. The premise that kept it, that only a reader can decide what is still true, no longer applies: what is true is decided at the spec's own pull request (issue #953, *The model*) |
| A2a. The settled predicate: replay the removed specs over the base and compare each named text's count with HEAD's | a hand edit in the same pull request that changes a count reads as not applied, a false refusal | **chosen.** It reads the fact itself, so it records nothing beside the tree, and it errs toward keeping the directory. Counting replaced presence in phase 3, which handles a text held twice |
| A2b. Released and nothing open is enough, with no replay | a branch, or a `settle` bug, deletes a spec whose `add` never landed. CI is green and the rule is gone, and only a reviewer reading the diff could see it | rejected for specs with operations. Kept for pre-model specs, which state no operations (Q2) |
| A2c. Keep a marker, smaller or elsewhere | — | rejected by the owner: "The `<!-- specs/<id> -->` marker paragraph is gone" (#953 item 3) |
| A3a. A sentence is named by quoting it, in plain field words with no symbol (`skills/settle/SKILL.md` §*Rule changes*) | an author quotes text the docs re-wrapped; matching with whitespace collapsed absorbs that | **chosen** by the owner's answer to Q1, built in phase 1. It replaces this frame's first choice, a one-line form with `·`, `§` and `›`, which a reader could trip on |
| A3b. A section only, so `change` replaces the whole section | an op meant for one sentence wipes the section's other rules | rejected: the issue says `change` "rewrites the sentence where it stands" |
| A4a. One `Document token ceiling` row, bytes halved as the estimate, no freeze, replacing `Document line ceiling` | the estimate under-counts a denser script (Q4) | **chosen**. Tokens bind first at every line density `docs/` has (`spec.md`, *The one-read row*) |
| A4b. Two rows, lines and tokens | the line row never binds before the token row here, so it is a second constant that guards nothing | rejected (owner's direction, 2026-10-20: no unnecessary constants) |
| A4c. Keep the structure: a 1000-line row plus `Over the ceiling` with frozen markers | the freeze counts markers, which no longer exist; and lines missed the two documents the tool already cuts at 999 and 666 lines | rejected: its premise, "a marker is the one thing only a fold adds" (`fold_check.py` docstring), goes with the marker |
| A4d. Count tokens with the API's counter | needs a network and a key in CI and in every adopting repository | rejected |
| A4e. A document past the ceiling is a report: named as one to split along its headings, exit 0; this repository declares 25000 | a document grows past one read and only the report says so | **chosen by the owner** (Q6, 2026-10-20). The estimate is a guess, and a guessed reading is a report (`CLAUDE.md`) |
| A4f. A gate: exit 1 until it is split in the same pull request | a single section past the cap cannot be split along headings, so the gate demands the trim the owner forbids; and the cap is one tool's, not the document's | rejected by the owner (Q6) |
| A4g. Hold this repository at its largest estimate until #941 (37,178) | a constant no rule names, and lowered by hand later | rejected: superseded by A4e |
| A5a. The process record leaves with its spec, and `--retire-process` goes | a release whose spec is refused keeps its `rounds/` until the next settle | **chosen** (issue item 6). The arm's own moment, every release, ended when 0.22.0 made `settle` owner-called (`docs/release-checklist.md` line 101), so both arms already run together |
| A5b. Keep `--retire-process` as its own arm | two commands remove from one directory at the same moment | rejected |
| A6a. `docs/README.md` is the index, and the table in `docs/the-record-layout.md` §*docs/* moves into it | — | **chosen**: the owner named the file (#953 item 5) |
| A6b. Keep the record-layout table and call it the index | the framer and `settle` would look in a file whose title is about records | rejected |
| A6c. Keep both | two copies of one list drift at the first split | rejected (`CLAUDE.md`, "A fact has one source") |
| A7a. Keep `fold_check.py` and its command name; change the ceiling arm; add the index arm | the name says "fold" after the fold is renamed | **chosen.** `#target_problem` stays where `rules.py`'s `SIBLINGS` and `bin/rules` find it, so the one resolver does not move. Renaming is churn #941's rewrite can take if it wants it |
| A7b. A new module, with `target_problem` moved into it | every loader of the resolver changes in an item that has no finding against it | rejected |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The section and its reader. `## Rule changes` goes into `templates/sdd-spec.md` above `## Removes`. `skills/settle/scripts/rule_changes.py` holds the parser and an in-memory replay with its refusals (S4, S7). `settle` with no flag becomes the dry run (S8). The section's vocabulary joins `templates/config.md`'s *What no row governs*. `skills/settle/SKILL.md` gains the section's grammar | new `tests/test_settle_applies_rule_changes_in_place.py` cases for parse, replay and refusal, each seen red before the module exists; `tests/test_a_phase_hands_the_next_one_a_record.py` (the template-shape cases) run narrowly | 10aa4947 |
| 2 | `settle --apply`. It writes the policy root in place in merge order, one spec at a time, all or nothing (S1–S3, S5–S7). It removes applied directories whole and spec-less released ones with nothing open. `--retire` and `--retire-process` go, with their tests. `docs/release-checklist.md` §2b, `docs/the-review-record.md:160`, `seal/README.md` with `templates/seal-README.md`, and both READMEs' cheat-sheet rows are rewritten | the phase-1 file's fixture-repo cases (commits, a parallel merge), seen red before `--apply` exists; the rewritten pins in `tests/test_settle_reads_before_it_removes.py`, each seen red against today's text with the old sentence still in place; `tests/test_first_setup_asks_once.py` (the two seal READMEs byte for byte) | 1c01de0c |
| 3 | The settled predicate. It replaces `folded_items` and absorbs `retired_by_rule`, reusing `rule_changes.py`'s replay with no reader or constant of its own. `settle`, `unverified-check --baseline`, `chain-check` and `tests/conftest.py#cutoff_item_is_traceable` ask it (S9–S11). Its rule is stated once, in `docs/the-record-layout.md` §*The fold, and what tells it from a deletion*, rewritten in place with the fold-record statements. `docs/the-review-and-parity-arms.md` lines 133–160 point there rather than restating it | `tests/test_unverified_rows_close.py` and `tests/test_chain_check.py::TestRetired`, re-pointed from markers to applied state. S10 is seen red with the replay stubbed to accept. The marker-only cases are retired, listed case by case in `phases/phase-3.md` | 33793508 |
| 4 | One read and the index. The ceiling arm checks one row, `Document token ceiling`, which replaces `Document line ceiling`, and this repository declares 25000, a document past it reported and never refused (`spec.md`, *The one-read row*, Q6). `Over the ceiling` goes with the freeze. `Policy root`, the one new row, is read by every `docs` constant. The index arm reads paths only, and `docs/README.md` arrives from the record-layout table, which goes. `templates/config.md` (the one statement of both rows and the estimate), `skills/config/SKILL.md`, and `docs/the-record-layout.md` §*The size a reader takes whole* and §*docs/* are rewritten. The prose names each row without restating its value (S12–S14) | `tests/test_a_document_has_room_for_the_next_fold.py`: the freeze and line-row cases retired; token and index cases added, each seen red; the value-copy pin and its two helpers removed rather than rewritten; `#test_this_repository_passes_the_command_with_no_flags` green over this tree with the new `docs/README.md` and the two documents past 25000 reported; `tests/test_the_settings_have_a_front_door.py` run narrowly | cb2f9849 |
| 5 | The model in the prose (S15). `skills/implement/SKILL.md`: the lifetime-table row, the §1 clause sentence and the §3 file-set row for `spec.md`. `agents/framer.md`: write `## Rule changes` as `skills/settle/SKILL.md` §*Rule changes* states it (a pointer, no grammar), pick the place from the index, read the source as `docs/` plus the unsettled specs in merge order, and the round-record sentence in step 4. `templates/sdd-questions.md`'s feed-back line. `docs/the-record-layout.md:278`. `docs/one-root-by-lifetime.md` and `.ko.md`, where they state that the session writes or that `settle` replaces by provenance id. `README.md:116` and `README.ko.md:111`. Each sentence is rewritten, never extended | `tests/test_settle_reads_before_it_removes.py#test_the_implement_skill_names_the_one_writer_of_docs`, rewritten and seen red; a new `tests/test_waiver_decided_at_start.py` case that the framer is pointed to the skill's section and the index, seen red against today's `agents/framer.md`; `git grep -n "one writer that does is" -- ':!seal/specs' ':!changelog'` empty; `tests/test_one_word_one_meaning.py` and `tests/test_both_editions_carry_the_same_folds.py` run narrowly | 79c07d24 |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.

**Notes for the build, from the framing.**

- Every phase runs its own cases narrowly. The suite, the lint and the
  typecheck are the orchestrator's broad gate after the rounds settle
  (contract §2). The framer ran none of them.
- Phase 2 removes about 730 test lines with the process arm. The pull request
  names what those cases caught against what they cost, as `CONTRIBUTING.md`
  §*What a change to a gate must carry* asks. Their one property still alive,
  that a whole released directory passes the readers, is phase 3's S9.
- No new word for an old concept. The act is "apply", the command stays
  `settle`, and "fold" leaves the prose this item rewrites. It stays where the
  legacy readers #941 owns still use it. `tests/test_one_word_one_meaning.py`
  is the check.
- Changing `agents/framer.md` owes no behaviour-eval run.
  `tests/test_a_rewritten_definition_proved_non_inferior.py`'s docstring:
  "nothing here makes a later edit of a definition owe a run, by design".
- A `.ko.md` edition moves with its English one in the same commit
  (`CONTRIBUTING.md` §*House rules*).
- The owner's direction of 2026-10-20 binds phases 3–5. No constant or symbol
  a reader can trip on. A grammar or a value is stated once and pointed to
  everywhere else. Content is compact. The only new row is `Policy root`.

## Operational impact

- **Command change for every repository that installs the plugin.** `settle
  --retire` and `settle --retire-process` are gone, and `settle --apply`
  replaces both. A script that called either now gets an argument error,
  exit 2. The changelog fragment says so.
- **`seal/config.md` rows.** `Policy root` is new and optional (default
  `docs`). `Document token ceiling` replaces `Document line ceiling`. A
  repository that declared a line ceiling has no size check until it
  declares the token row, and the changelog fragment says so. `Over the
  ceiling` is no longer read. A repository that lists documents there loses
  the freeze, and each document is held to the ceiling like any other.
- **`settle` now writes the policy root.** In a repository whose `docs/` is a
  manual or a site, the owner names another `Policy root` before the first
  `settle --apply`, and that run creates the directory.
- **CI readers.** `unverified-check --baseline` and `chain-check` accept a
  released pre-model directory, removed with nothing open, without a marker
  (Q2). They refuse a removed spec whose rule changes HEAD does not hold. The
  shipped `templates/hygiene.yml` is unchanged, since it already fetches full
  history (`fetch-depth: 0`, line 47) and the replay needs it.
- No new dependency, no environment variable, no migration of existing
  records. The 129 legacy marker lines and the backlog are #941's.
