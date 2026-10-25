# Feature Specification: settle squashes specs into docs/ in place (#953)

Issue #953 is the source of the owner's decisions (2026-10-16), read whole
with its one comment. A spec becomes a migration and `docs/` the baseline it
squashes into. A spec states its rule changes in one section of their own, a
pull request stops editing `docs/`, and `settle` applies those changes in
place, in merge order, when the owner calls it. Nothing appends any more, and
no marker paragraph is written.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | Every mechanism the marker paragraph held up goes in this item or is named for #941: the marker as fold record, the `Over the ceiling` freeze, the process-record arm. A replacement reads a fact; it never keeps a record beside the tree |
| `CLAUDE.md` §*The goal a design is chosen against* | `settle` asks nobody anything. A conflict is refused and printed, never guessed, and a refused spec waits on disk for a later run |
| `docs/one-root-by-lifetime.md` §*What keeps `settle` light* and its table row *What `settle` is* (§*Decided when `settle` was built*) | Overturned in part. "It moves and does not verify" still holds. "The command reads and groups; the session judges and writes" stops holding: under this model the judgment happens when the spec is written and reviewed, so applying it judges nothing. Both editions are rewritten in place where they state the old split |
| `docs/one-root-by-lifetime.md` §*The dependency rule* | `settle` stays the one sanctioned reader of a released work item. The CI readers that refuse a removed directory still need a way to tell a settle from a deletion, and this item gives them one with no marker |
| `docs/the-record-layout.md` §*The fold, and what tells it from a deletion* | Rewritten to the new model. Kept: one predicate for every asker (#602), *nothing open* still keeps a directory, and a population floor is replaced, never lowered. Gone: the marker as fold record and the frozen-marker ceiling. The live-line rule stays for the markers #941 has yet to remove |
| `docs/the-record-layout.md` §*The size a reader takes whole* | One `seal/config.md` row in tokens replaces the line row. The reading tool cuts on tokens first, at every line density `docs/` has (*Data & interfaces*, *The one-read row*) |
| `docs/the-record-layout.md` §*docs/* | Its table already lists every `docs/` file and the question each answers. It moves to `docs/README.md`, so the index has one home |
| `docs/release-checklist.md` §*2b. Settle what earlier releases left behind — when the owner calls it* | Already says `settle` runs when the owner calls it (read at lines 99–104: "not at every release"), so that half of the issue's item 6 holds today. Its sequence (`settle --retire-process`, prose by hand, `fold-check`, `settle --retire`) is rewritten to the new commands |
| `docs/the-review-and-parity-arms.md` (lines 133–160, the retired declarations) | `chain-check` accepts a removed declaration through `folded_items` or `retired_by_rule`. Both are replaced by the one new predicate |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below is the list the review reads against the diff |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The CI readers are gates. The pull request states the failure direction (Q2), the prompt budget (zero) and what is removed |
| `skills/settle/SKILL.md` (whole) | The procedure, rewritten from "write one standing statement per rule" to "apply each spec's rule changes" |
| `skills/implement/SKILL.md` §*Document layout — two roots, three lifetimes* (line 75) | Says "The one writer that does is `settle`". Rewritten to the model: `docs/` is the baseline, a spec's rule changes are the migration, and the source is both, read in merge order |
| `templates/config.md` §*The fold's values* and §*Reference specs* | Rows change here. `Policy root` is added, as the issue requires. `Document token ceiling` replaces `Document line ceiling`, so the count of rows does not grow. `Over the ceiling` goes. The reference-root rule is untouched |

## Scope

**In.**

1. **A spec states its rule changes in `## Rule changes`.** The section is
   added to `templates/sdd-spec.md` and read by one parser. Each item is one of
   `add`, `change` or `remove`, with its place in the policy root and the rule
   as it will read. The grammar is stated once, in `skills/settle/SKILL.md`
   §*Rule changes*, and every other file points there. The debate, the
   alternatives and the measurements stay in the spec's other sections and in
   `plan.md`, and `settle` reads none of them.
2. **A pull request does not edit the policy root.** The model replaces "the
   one writer is `settle`" in `skills/implement/SKILL.md`'s lifetime table, in
   `README.md` and `README.ko.md`, and in every other carrier named under
   `## Removes`. `agents/framer.md` tells the framer to write `## Rule changes`,
   to pick each place from the index, and to read the source as `docs/` plus
   the rule changes of every unsettled spec, in merge order.
   `templates/sdd-questions.md`'s "Answered rows feed back into docs/" becomes
   "into `spec.md`'s `## Rule changes`". This item adds no gate for the rule
   (Q3).
3. **`settle --apply` applies the operations in place**, in merge order,
   all of a spec or none of it. It writes no marker, refuses a place or a text
   that is not there, prints a conflict for the owner, and removes each
   applied directory whole. `settle` with no flag is the dry run.
   `skills/settle/SKILL.md` §*What `--apply` does* states the rules.
4. **A removal is told from a deletion without a marker.** One predicate
   replaces `unverified_check.py#folded_items` and widens `#retired_by_rule`. A
   removed directory is settled when three things hold. It was released at the
   base. Nothing in its record is open. Its rule changes, replayed over the
   base's policy root in merge order, are what HEAD's policy root holds.
   `settle`, `unverified-check --baseline` and `chain-check` all ask it.
5. **Every document stays within one read.** `fold-check`'s ceiling arm
   checks one row, `Document token ceiling`, against estimated tokens. It
   replaces `Document line ceiling`. An absent row is a check not run, as
   today. The `Over the ceiling` row and its marker freeze go. A document
   past the ceiling is a report, not a gate (Q6). `fold-check` and `settle
   --apply` name it as one to split along its own headings, never to trim,
   and exit 0.
6. **`<policy root>/README.md` is the index.** Each line names one topic and
   its file, and a `.ko.md` edition goes on its English edition's line.
   `fold-check` refuses three things: a top-level policy file missing from the
   index or named twice, and an index line that names no file. It checks only
   where the index exists. This item writes `docs/README.md` for this
   repository from the table in `docs/the-record-layout.md` §*docs/*, and that
   table goes. The framer picks a place from the index. `settle` creates the
   index with the policy root, and reports the line owed when an `add` creates
   a document.
7. **The policy root is a `seal/config.md` row.** `Policy root` (default
   `docs`) is read by every reader that hard-codes `docs` today
   (`unverified_check.py:125`, `fold_check.py:82`, `settle.py`). The first
   `settle --apply` creates the root when it is absent. Only that root falls
   under "a pull request does not edit it".
8. **The prose that states the appending fold is rewritten in place, in the
   same commits.** That is every carrier `## Removes` lists, and the test pins
   on them. Each rewritten pin is seen red against the appending text first.

**Out, and whose it is.**

- Rewriting the current `docs/` once, removing its 129 live marker lines
  (counted 2026-10-20 with `git grep -c '^<!-- specs/' -- docs`; #941 counted
  131 on 2026-10-16), and settling the backlog of pre-model specs: #941.
- The `Enforced by:` → `check:` label, and a successor to the marker-bound
  shape arm of `fold-check` (`Fold shape from`): #941. That arm and
  `tests/test_both_editions_carry_the_same_folds.py`, which compares markers,
  are left untouched. They keep reading the legacy markers until #941 removes
  them.
- Splitting the two documents already past the ceiling: #941.
- `settle` in local mode: #955. It keeps refusing local mode.
- Templates and skills an agent opens on demand, beyond the four files the
  issue names: #940.
- The `<!-- specs/<id> -->` markers `gather_changelog.py` writes into
  `changelog/` and `CHANGELOG.md`. They index the changelog, and no fold reads
  them.
- A gate refusing a pull request that edits the policy root (Q3).

**This item's own `docs/` edits are made directly in its diff.** The issue
lists the files it rewrites. It is the change that sets the model up, so it
cannot wait for a `settle` to apply it (see `## Rule changes`).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 change in place | Given a released spec that changes the sentence `old sentence.` in section S of `docs/a.md` to `New rule.`, when `settle --apply` runs, then `docs/a.md` reads `New rule.` where `old sentence.` stood, the rest of the file is byte-identical, no `<!-- specs/` line is added, and the spec's directory is gone | fixture repo case, seen red against the `settle` before `--apply` |
| S2 add inside its section | Given an `add` of `Rule.` to section S, followed by section T, when applied, then `Rule.` ends S's own text, comes before T's heading, and is not at the end of the file | fixture case |
| S3 remove | Given a `remove` of the sentence `x.` from section S and a `remove` of section T, when applied, then `x.` is gone from S, and T's heading and body are gone up to the next heading of the same or higher level | fixture case |
| S4 refused, never guessed | Given a `change` whose sentence is not in its section, or a section that does not exist, or one that appears twice, or a block that does not parse whole, when `settle --apply` runs, then that spec applies nothing, its directory stays, the refusal names the spec, the line and the reason, and the run exits non-zero | fixture case per reason |
| S5 merge order, the later wins | Given spec A changes `x.` to `y.` and spec B, added in a later commit on the same line of history, changes `y.` to `z.`, when applied, then the document reads `z.` and both directories are gone | fixture repo with two commits |
| S6 a conflict is shown | Given specs A and B added on parallel branches merged into the base, both changing `x.` in section S, when applied, then neither is applied for that place, and both are printed as a conflict for the owner | fixture repo with a merge |
| S7 atomic per spec | Given spec A with two operations, the second refused, when applied, then neither applies and A's directory stays whole | fixture case |
| S8 dry run | Given pending specs, when `settle` runs with no flag, then it prints each document's pending operations in merge order, the refusals, and what `--apply` would remove, and writes nothing | fixture case: the tree is unchanged |
| S9 a settle passes the readers | Given a branch that ran `settle --apply`, when `unverified-check --baseline` and `chain-check` run against the base, then each removed directory is named as settled, not reported as a deletion | the two readers' cases, re-pointed from markers |
| S10 a deletion still fails | Given a branch that deletes a released spec's directory and leaves the policy root unchanged although the spec states an `add`, when the readers run, then the removal is refused | same cases, seen red with the replay disabled |
| S11 pre-model spec | Given a released spec with no `## Rule changes` section and nothing open, when it is removed, then the readers accept it (Q2) | reader cases |
| S12 one read | Given `Document token ceiling` 25000 and a document whose estimate is 25001, when `fold-check` or `settle --apply` runs, then it names the document as one to split and exits 0; with the row absent it checks nothing and says so in one line; a `Document line ceiling` row is no longer read | fold-check cases |
| S13 the index | Given `docs/README.md` missing a top-level file, or naming one twice, or holding a line that names no file, when `fold-check` runs, then each is named and it exits 1; this repository's own tree passes | fold-check cases and the existing `test_this_repository_passes_the_command_with_no_flags` |
| S14 policy root | Given `Policy root` names `policy/`, when `settle --apply` runs with no such directory, then it creates `policy/`, writes there, and touches no `docs/` | fixture case |
| S15 the model is stated once | Given the implement skill, the framer definition, the spec template, the settle skill and the READMEs, when read, then the model is stated once, in the `docs/` row of the implement skill's lifetime table, every other carrier points to it, and no carrier still says "the one writer that does is `settle`" or tells a session to write a marker | pins rewritten and seen red against today's text; `git grep` for the old phrases comes back empty outside `seal/specs/` and `changelog/` |
| S16 the resolver stays one | Given `bin/rules --check` and `fold-check`, when either resolves a `path::name` target, then both still go through `fold_check.py#target_problem` | existing `tests/test_a_folded_statement_names_what_enforces_it.py::test_the_target_is_resolved_by_named_unit`, unchanged and green |

## Data & interfaces

**The grammar, merge order and the commands have one home:**
`skills/settle/SKILL.md` §*Rule changes* and §*What `--apply` does*, with
`skills/settle/scripts/rule_changes.py` the one reader (Q1, answered). This
file does not restate them. Phases 3–5 point there too, and add no symbol or
constant of their own.

**The settled predicate** (phase 3; once built, its rule is stated in
`docs/the-record-layout.md` §*The fold, and what tells it from a deletion*
and this paragraph stops being its home). It replaces `folded_items` and
absorbs `retired_by_rule`. It answers for the set of
directories a pull request removes, because a later spec can supersede an
earlier one inside one settle. The replay starts from the policy root at
`base` and applies the removed specs in merge order. For each text an
operation names (its `from`, its `to`, its section heading), the count across
the policy root's top-level documents after the replay must equal HEAD's,
with whitespace collapsed. Counting across the whole root lets a split along
headings pass, and counting, not presence, handles a text held twice.

**The one-read row.** `Document token ceiling` is the one size row, and the
estimate is UTF-8 bytes halved, rounded up. Both are stated once, in
`templates/config.md`, and the one constant lives in `fold_check.py`.

- *Why tokens alone.* The Read tool cuts at 25,000 tokens (measured
  2026-10-20: it reported "cap 25000") and at 2000 lines. Lines bind first
  only where a document averages under about 25 bytes a line under the
  estimate. No top-level `docs/` file averages under 57.9 (`executed`:
  `awk` over `docs/*.md`; lowest is `docs/release-checklist.md`), so 2000
  lines there run to some 58,000 estimated tokens. `docs/worktree-guard-spec.md`
  is under the 1000-line row and past one read. The line row protects
  nothing the token row does not, so it goes.
- *Why bytes halved.* Measured English ran 2.85 bytes a token, mixed Korean
  2.15 (`executed`: `docs/worktree-guard-spec.md` doubled, 148,710 bytes,
  read as 52,121 tokens; `docs/one-root-by-lifetime.ko.md` doubled, 116,632
  bytes, as 54,209). Halving overestimates both. Q4 asks about denser text.
- *A report, not a gate* (Q6, the owner, 2026-10-20). The figure is an
  estimate, and it is one tool's per-call cap, not a property of the
  document. A single section past it cannot be split along headings, so a
  gate could demand the trim the owner forbids. This repository declares
  25000. `fold-check` names `docs/one-root-by-lifetime.ko.md` and
  `docs/worktree-guard-spec.md`, and exits 0 (the orchestrator's run, at
  e1131a97); #941 splits them.

**Config rows** (`templates/config.md`, `skills/config/SKILL.md`): added,
`Policy root` (default `docs`, issue-required). Replaced, `Document line
ceiling` by `Document token ceiling`. Removed, `Over the ceiling`. Unchanged,
`Fold shape from` (#941's). Prose names a row and never restates its value,
so no pin is needed to hold a copy of the value to the row.

**What the build answers from the tree, already looked up.**

- `bin/rules` execs `.github/scripts/rules.py` through `hooks/launch.py`.
  `rules.py#target_problem` resolves an eval-case directory itself and hands
  every other target to `fold_check.py#target_problem`. That function accepts
  a file inside the repository, after `realpath`, and a `path::A::b` that
  `coordinates.py#named_unit` finds defined exactly once as a `def` or
  `class`. It reads no marker, so `fold_check.py` stays where it is and the
  resolver does not move (*Alternatives*, row A7).
- `docs/release-checklist.md` already makes `settle` owner-called (line 101),
  as the caller's unverified claim asked. Settle runs when the owner calls it
  holds today.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the marker as fold record | `skills/verify/scripts/unverified_check.py#folded_items`, and its callers at `chain_check.py#retired`, `settle.py#survey`/`#retire`; `tests/conftest.py#cutoff_item_is_traceable` | the settled predicate (*Data & interfaces*); the conftest helper goes, since it had no caller after #923 |
| the spec-less retirement predicate as a separate function | `skills/verify/scripts/unverified_check.py#retired_by_rule` | absorbed by the settled predicate; its *nothing open* condition and its merge-base reading (#602) carry over unchanged |
| the retirement arm and its flag | `skills/settle/scripts/settle.py#retire`, `--retire` | `settle --apply` |
| the process-record arm and its flag | `skills/settle/scripts/settle.py#retire_process`, `#process_plan`, `#write_process_section`, `PROCESS_DIRS`, `PROCESS_FILES`, `DURABLE`, `--retire-process` | the process record leaves with its spec's directory (issue item 6). Both arms run at the one moment the owner calls `settle`, so a separate arm has no moment of its own left |
| the arm's tests | `tests/test_settle_retires_the_process_record.py`, `tests/test_a_process_record_drop_passes_the_readers.py` | the property they still hold, that a released directory removed whole passes the readers, moves to the settled predicate's cases (S9) |
| the marker freeze | `skills/settle/scripts/fold_check.py#parse_over`, `#marker_digest`, the freeze half of `#ceiling_problems`, `OVER_ROW`, `OVER_ENTRY`, `OVER_SHAPE`, `NONE_LISTED`; the `Over the ceiling` row in `seal/config.md`, `templates/config.md` §*The fold's values* and `skills/config/SKILL.md`; the listed-document cases in `tests/test_a_document_has_room_for_the_next_fold.py` | a document past the ceiling is reported, never frozen or refused (Q6) |
| the line row | `Document line ceiling` in `seal/config.md`, `templates/config.md`, `skills/config/SKILL.md` and `tests/test_the_settings_have_a_front_door.py`'s row list; `skills/settle/scripts/fold_check.py`'s `CEILING_ROW` and the line count in `#ceiling_problems` | `Document token ceiling`, the one size row (*The one-read row*) |
| a value stated twice | `docs/the-record-layout.md`'s restated cutoff and ceiling values; `tests/test_a_document_has_room_for_the_next_fold.py#test_the_record_layout_states_the_values_the_config_rows_hold`, `#prose_disagreements` and `#test_the_prose_pin_fails_when_either_side_moves_alone` | the rows alone; the prose names each row without repeating its value, so no pin has a copy to hold |
| the docs index table | `docs/the-record-layout.md#"docs/"` (its table and the `docs/experiments/` sentence under it) | `docs/README.md` |
| "the one writer is `settle`" | `skills/implement/SKILL.md:75` (the `docs/` row of the lifetime table); `README.md:116`; `README.ko.md:111`; `docs/one-root-by-lifetime.md:655` and its `.ko.md` row; `tests/test_settle_reads_before_it_removes.py#test_the_implement_skill_names_the_one_writer_of_docs` | the model sentence in each place; the pin is rewritten to it |
| the session-writes split | `skills/settle/SKILL.md#"The command reads and lists; you judge and write."`, its §*2. Write one standing statement per rule* and §*4. Retire what the policy absorbed*; `docs/one-root-by-lifetime.md:651` (*What `settle` is*) and §*What keeps `settle` light*'s "replaces by provenance id" bullet, both editions; `settle.py`'s module docstring paragraphs on the provenance comment; `README.md:263`/`README.ko.md:253` (the `settle [--retire]` rows) | the applying model in each; `tests/test_settle_reads_before_it_removes.py#test_the_skill_says_who_judges_and_who_reads`, `#test_the_skill_states_the_destination_rule`, `#test_the_skill_says_the_retirement_is_the_second_half_of_the_fold`, `#test_both_cheat_sheets_carry_the_command`, `#test_the_seal_readme_says_the_step_exists`, `#test_the_release_checklist_carries_the_by_hand_step` and `tests/test_a_document_has_room_for_the_next_fold.py#test_settle_owns_the_placement_rule` are rewritten to the new text |
| the marker-based settle cases | `tests/test_settle_reads_before_it_removes.py#test_retire_removes_only_what_docs_records`, `#test_a_recorded_fold_leaves_the_foldable_list`, `#test_an_interrupted_run_resumes`, `#test_a_marker_quoted_in_prose_is_not_a_fold_record`, `#test_a_marked_item_still_on_disk_is_not_the_fold_being_complete`, `#test_a_complete_retirement_is_not_reported_as_nothing_ever_folded`, `#test_the_fold_is_complete_still_prints_when_it_is`; `tests/test_unverified_rows_close.py#test_a_marker_inside_a_commented_out_draft_is_not_a_fold_record`, `#test_a_marker_inside_a_fenced_block_is_not_a_fold_record`, `#test_a_marker_below_the_top_level_of_docs_is_not_a_fold_record`; `tests/test_chain_check.py::TestRetired::test_a_declaration_a_fold_retired_is_not_one_this_branch_made` | each is rewritten to the applied-state equivalent (S1–S10), or retired where the property was about the marker alone. The phase record says which, case by case |
| a docs edit inside a work item | `templates/sdd-questions.md#"Answered rows feed back into docs/"`; `docs/the-record-layout.md:278` ("a work item that finds one wrong corrects it"); `skills/implement/SKILL.md` §1's "a missing clause means writing it is part of this work" | the same sentence, pointed at `spec.md`'s `## Rule changes` |
| the release step's old sequence | `docs/release-checklist.md#"2b. Settle what earlier releases left behind — when the owner calls it"` (the `settle --retire-process`, `fold-check`, `settle --retire` sequence and "This is a separate branch and a separate pull request from step 2.") ; `docs/the-review-record.md:160`'s `settle --retire-process` sentence and its `Enforced by:` line | the step rewritten to `settle`, `settle --apply`, `fold-check`; the review-record sentence rewritten to "with its spec, at the settle" |
| the fold-record statements | `docs/the-record-layout.md#"The fold, and what tells it from a deletion"`, the statements whose rule is the marker (lines 87–96, 139–154, 156–163) and the frozen ceiling (75–85); `docs/the-review-and-parity-arms.md` lines 133–160 | rewritten in place to the settled predicate. The marker comments above the rewritten statements are #941's to remove with the other 129, and this item does not add one |

## Rule changes

- nothing
  why: this item sets up the section and the `settle` that applies it, so
    its own changes to `docs/` are made in its diff, as the issue lists them,
    and there is nothing left for a later `settle` to apply.

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

The framer revised this frame on 2026-10-20 after phase 2, outside any
review round, at the owner's direction relayed by the orchestrator. The
grammar now points to the skill, and one token row replaces the line row.
After phase 5 it was revised again on the owner's answer to Q6 (the ceiling
is a report) and on the build's divergences in `overview.md`.

Framed 2026-10-20 by framer, before the build.
