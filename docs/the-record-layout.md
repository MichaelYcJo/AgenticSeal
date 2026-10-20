# The record layout — where each kind of record lives

This repository keeps a dozen kinds of record, and every one of them has one
home. This document is the index: one table per place, each row naming a file
or a file shape and the one question it answers. A reader looking for a rule
or a record opens this index and then one file.

It is a policy document. A file that states a rule this index gives another
home links to that home and does not restate it, because two copies of one
rule are one rule today and two after the first edit to either. Where a copy
is found, the copy is the defect.

## Every kind of record, at a glance

| Kind | Home | Size target | Index |
|---|---|---|---|
| The changelog | `seal/specs/<work-item-id>/changelog.md` while a work item is open; `changelog/<X.Y.Z>.md`, the release's own file, once its release gathers it | each release file is under target, and is the unit | the file name, by version, and `CHANGELOG.md`, which heads each release newest first with a link to its file |
| A work item's files | `seal/specs/<work-item-id>/` | each file under target | the table under *seal/specs/<work-item-id>/* below |
| The repository's rules | `CLAUDE.md` for the rules a session must hold, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
| The configuration | `seal/config.md`, one row per item; `templates/config.md` documents every row | under target | the `Item` column |
| The follow-up list | `seal/follow-up.md`, one row per item that waits on a named party | under target | its rows, each naming who answers it |

## The size a reader takes whole

**A file a reader is meant to take whole fits one read.** The row and the
estimate are `templates/config.md` §*The fold's values*, and what a document
past it owes is `skills/settle/SKILL.md` §*A document past its ceiling is
split, never trimmed*.
Enforced by: tests/test_a_document_has_room_for_the_next_fold.py::test_a_document_past_the_ceiling_is_named_and_the_run_exits_0, tests/test_a_document_has_room_for_the_next_fold.py::test_this_repository_passes_the_command_with_no_flags

## A change writes fragments, never a shared file

A file every branch appends to costs a conflict at the worst moment — after
the broad gate has run, which forces it to run again. So a change writes its
changelog entry into a file of its own, `seal/specs/<work-item-id>/changelog.md`,
never under a heading of `CHANGELOG.md`. No two work items share an id, so no
two branches share a file. A changelog fragment has no line starting `## `,
because that line ends the released section, and the gather refuses a
fragment that has one.

**The fragments are gathered at the release, by one command in one commit**,
and `docs/release-checklist.md` §*2. Gather, bump* holds it. The fragments are
concatenated into the release's own file, `changelog/X.Y.Z.md`, and the
release's heading goes into the index, `CHANGELOG.md`. A fragment lives from
the work item's first entry to the release that ships it.
Enforced by: tests/test_the_changelog_is_gathered_at_release.py::test_the_release_sequence_names_the_gather_step, tests/test_the_changelog_is_gathered_at_release.py::test_a_gather_writes_the_release_file_and_its_index_entry

## A commit after the build brings its changelog fragment along

**A commit after the build that changes what the work item ships updates the
work item's `changelog.md` in the same range.** The build's last phase writes
the fragment and the release gathers it verbatim, so a later commit that
changes behaviour can leave it describing something that no longer ships. The
rule binds whoever writes the commit: the smith's fix pass, a fix written after
the last round, and an integration commit after a sibling's squash, which the
orchestrator writes. A commit that changes nothing a release note states owes
the fragment nothing. 0.18.2 shipped three fragments their own review rounds had
made false, and #795 corrected them by hand before the release.
Enforced by: nothing — the next round's warden reads the fragment against the
diff, and the sealer reads the changelog against the tree.

## The fold, and what tells it from a deletion

The procedure is `skills/settle/SKILL.md`. This section holds the rules its
readers share.

<!-- specs/1790154761-folded-statements-pile-into-one-spec -->
**Every bound statement has the rule's shape, from the cutoff
`seal/config.md`'s `Fold shape from` row names.** The shape is
`skills/settle/SKILL.md` §*A rule has one shape*. The cutoff is compared with
the id in the marker, and ids are epoch-prefixed, so it is a comparison
rather than a list.
Enforced by: skills/settle/scripts/fold_check.py::bound, tests/test_a_folded_statement_names_what_enforces_it.py::test_every_bound_statement_in_docs_has_the_shape

<!-- specs/1790039346-settle-reads-a-marker-inside-a-commented-out-draft -->
**A removed work item directory is a settle, not a deletion, when replaying
it gives what the tree holds.** Each directory a pull request removes whole
is judged as it stood at the merge base: nothing in its record open, and
either no rule to replay (it wrote no `spec.md`, or its spec has no
`## Rule changes` or says `nothing`) or the replay holds. The replay applies
every removed spec's rule changes, in merge order, over the merge base's
`docs/`, and each text an applied operation names must occur as often across
`docs/` at HEAD as in the replay, whitespace collapsed. So a
later spec may rewrite what an earlier one placed, and a split along headings
in the same pull request passes. One predicate,
`unverified_check.py#settled`, answers `settle`, `unverified-check
--baseline` and `chain-check`, and a refusal keeps the directory, the cheaper
mistake.
Enforced by: tests/test_unverified_rows_close.py::test_a_settled_work_item_is_not_read_as_this_branchs_deletion, tests/test_unverified_rows_close.py::test_a_removal_whose_rule_docs_does_not_hold_still_fails, tests/test_unverified_rows_close.py::test_a_spec_with_no_rule_changes_and_nothing_open_is_settled, tests/test_settle_applies_rule_changes_in_place.py::test_what_apply_removed_is_settled_for_the_readers

<!-- specs/1790076070-the-fold-ships-and-the-corpus-is-still-on-disk -->
<!-- specs/1790138190-settle-leaves-twelve-directories-with-no-way-out -->
**A released work item that wrote no `spec.md` states no rule, and it is
retired by that rule, with no marker.** Such an item was below the SDD
ladder: a release entry, a renumbering, a CI repair, a pull request's record.
Those are records of a moment, and a moment states no rule, so nothing has
to be carried out of one: `settle` prints these under their own heading and
`settle --apply` removes them without writing into `docs/` (#517). **One condition narrows it: nothing in the record may
still be open.** An open `## Not verified` row is a claim with an answerer
rather than a rule, so a directory holding one
is kept and named with its rows, and closing each row — a row re-homed is
closed too, `closed` naming where it went — in a pull request merged before the one
that retires the directory is what lets the next retirement take it. The CI
readers ask the rule of the merge base, so a closure in the same pull request
as the removal is still open where they look. `settle` asks it at the merge
base of `--released-at` and `HEAD`, which is where they look until the base
moves past the fork and earlier after, and keeps a directory whose closure
has reached the working branch and not that base (#602). Whether the item wrote a
`spec.md` is asked of its history, so a spec deleted in one commit, or in an
earlier pull request, and the directory in the next is still a deletion. That
condition is a judgment the repository owner may overturn. An item that did
write a `spec.md` leaves when `settle --apply` applies its rule changes.
Enforced by: tests/test_settle_reads_before_it_removes.py::test_the_rule_arm_removes_it_with_no_marker, tests/test_settle_reads_before_it_removes.py::test_a_closure_the_base_has_not_seen_keeps_the_directory

<!-- specs/1790027178-a-shipped-spec-waits-for-a-settle-that-was-never-built -->
**A released spec's rule changes are applied to `docs/` in place, and its
directory goes with them, never before.** `settle --apply` replays each
released spec's `## Rule changes` in merge order, writes what applies, and
removes each applied directory whole; a spec it cannot place applies nothing
and its directory stays. The judgment was made when the spec was written and
reviewed, so applying it judges nothing, and no sentence is written by hand.
No marker is written.
Enforced by: tests/test_settle_applies_rule_changes_in_place.py::test_apply_rewrites_in_place_and_removes_the_directory, tests/test_settle_reads_before_it_removes.py::test_apply_removes_only_what_it_applied

<!-- specs/1790138190-settle-leaves-twelve-directories-with-no-way-out -->
**A settle is not a work item.** It opens no directory under `seal/specs/`.
Its commits are waived one command at a time and what it applied is reviewed
at its pull request (#517). What it leaves already has a home, the pull
request and git history, so it keeps no log of its own. Were it a work item,
each settle would leave a directory for the next one to remove, and settling
would never end; `skills/settle/SKILL.md` §*A settle is not a work item* is
the procedure.
Enforced by: tests/test_settle_reads_before_it_removes.py::test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row

<!-- specs/1790076070-the-fold-ships-and-the-corpus-is-still-on-disk -->
<!-- specs/1790119502-four-shipped-work-items-wait-unfolded -->
**A population floor over the records is replaced, never lowered.** A check
asserting that a sweep of `seal/specs/` read *enough* — `len(records) > 200` —
is answering *did the walk read anything* with a literal that stops being true
the moment the corpus shrinks, and a fold shrinks it by design. The repair
compares the walk against an independent listing of the same tree —
`git ls-tree HEAD` — which holds at any size, and a property the real corpus no
longer exercises moves to a record built in `tmp_path`. A repair is green
before the fold and after it; one green only once the directories are gone is
a lowering. `skills/settle/SKILL.md` §*Answer every check that reads the
corpus* gives the three answers.
Enforced by: tests/test_settle_reads_before_it_removes.py::test_the_skill_names_the_floors_a_fold_has_to_answer

<!-- specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it -->
**`path::name` has one resolver.** An `Enforced by:` target names a unit as
pytest spells a node id, so a method is `::Class::method`, and `fold-check`
and `rules --check` read it through
`skills/settle/scripts/fold_check.py#target_problem`, which looks the name up
through `coordinates.py#named_unit`. A name is looked up where it is
defined. A `def` or `class` its file defines once is accepted, and so is a
file alone. A name defined twice names no one unit and is refused.
Enforced by: tests/test_a_folded_statement_names_what_enforces_it.py::test_a_method_resolves_in_pytests_spelling, tests/test_a_folded_statement_names_what_enforces_it.py::test_the_target_is_resolved_by_named_unit, tests/test_a_folded_statement_names_what_enforces_it.py::test_a_name_defined_twice_is_no_target

<!-- specs/1790154761-folded-statements-pile-into-one-spec -->
**A fold into a document with a `.ko.md` edition is a fold into both, under
the same heading position.** The two editions are prose in two languages, so
the check compares what is language-neutral: the sequence of heading levels,
and the fold-marker ids under each heading position. Whether a Korean
paragraph says what its English one says is review's to read.
`CONTRIBUTING.md` §*House rules* owns the rule.
Enforced by: tests/test_both_editions_carry_the_same_folds.py::disagreements

<!-- specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules -->
**Whether a line is live is asked by what the line does, and the four
readers that ask it give three answers.** These are all four readers, grouped
by the kind of line they read, with the cost each answer is chosen against.
Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_the_statement_names_each_reader_under_its_answer, tests/test_routing_is_recorded.py::test_the_routing_shapes_read_as_the_frame_expects, tests/test_routing_is_recorded.py::test_a_declaration_below_a_comment_opener_nobody_closed_still_reads

- **A line that HOLDS something — a claim or an anchor — is read on
  doubt.** The coordinate kernel's `quoted_lines`, which its `unquoted` and
  `markdown_lines` read through. A fence nobody closed is a malformed file
  whose lines are read, and a commented-out row is a parked claim and is
  read. What this protects is that a claim never leaves a record in silence.
  The wrong answer is loud instead: `BROKEN`, a refused name or exit 2, and a
  person answers it with an edit or a marker.
  Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_each_reader_gives_its_stated_answer_on_each_shape
- **A line that EXCUSES or DECLARES something — a fold marker, a
  `seal/config.md` row, a `routing.md` row — is not taken on doubt, except
  where a declaring reader keeps an older reading that took it.**
  `unverified_check.py#live_lines` parks a line inside any fence or comment,
  closed or not, and a line its two span readings disagree about.
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before the walk:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares unless a fence that closes
  holds it, because that reading never hid one and work item 1790645290
  was bound to miss no row the older reading saw. `hooks/routing.py#shown`,
  which reads a `routing.md` and is not one of the four, keeps the reading
  it gave before the walk the same way, and that reading hid nothing: a row
  below a fence or a comment opener nobody closed still declares there,
  unless a fence that closes holds it. Those rows are the places a line
  nobody wrote live declares something; at every other fence or comment,
  what this protects is that nothing is excused or declared by a line
  nobody wrote live. The wrong answer is a statement left unbound, a hook
  that says nothing, or a gate that asks.
  Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_each_reader_gives_its_stated_answer_on_each_shape
- **A line a record's rows are COUNTED on is blanked the same way on both
  sides of a comparison.** `unverified_check.py#readable` blanks comment text
  and fenced lines with the indices intact, and a region nobody closed to the
  end of the file. So the working tree and the base revision count the same
  table, and the readers that judge a record refuse a hidden table as absent
  rather than read it as empty.
  Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_each_reader_gives_its_stated_answer_on_each_shape

No one rule serves all three kinds. The holding bias would let a fold marker
quoted in an example bind a statement nobody wrote, and the excusing bias
would drop a parked row without a word. A reader of a new kind of line is a
fourth answer, and it is argued against these three.

<!-- specs/1790138190-settle-leaves-twelve-directories-with-no-way-out -->
**A `seal/` root with no work item under it is the state a complete fold ends
in, and it reads as settled, never as unusable.** Git keeps no empty
directory, so the state is two: the tree that ran `settle --apply` holds an
empty `seal/specs/`, and a fresh checkout of that commit holds none. Read as
unusable, `settle` exited 2 on its own finished work, and `unverified-check
--baseline` read the root's own `specs` path as a typo, which would turn every
pull request after a complete fold red, the shipped `templates/hygiene.yml`
included. Only that one path is settled; any other missing path is still
refused, which keeps a misspelt path from passing in silence.
Enforced by: tests/test_settle_reads_before_it_removes.py::test_a_settled_root_is_green_and_says_so, tests/test_unverified_rows_close.py::test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it

<!-- specs/1790076070-the-fold-ships-and-the-corpus-is-still-on-disk -->
**A fold marker on a line of its own is exempt from the wrap limit.** The
marker is matched whole, so wrapping a long work item id stops it being a fold
record, and `tests/test_docs_line_wrap.py` skips a line that is exactly one
marker rather than asking a document to choose between the two.
Enforced by: tests/test_docs_line_wrap.py::test_a_fold_marker_is_skipped_and_the_line_beside_it_is_not

## The unverified record, and the baseline it is read against

<!-- specs/1788873600-the-baseline-is-the-moving-pull-request-base -->
**A baseline reference is resolved once, to a merge base, and every arm reads
that commit.** A branch name is not a commit: it moves while the pull request
is open, so two arms reading it a second apart can compare against two
different trees. The report names the revision it actually compared against,
and a reference sharing no history with the head is exit 2 — a comparison
against nothing is not a comparison.
Enforced by: tests/test_unverified_rows_close.py::test_a_row_the_base_gained_after_the_fork_is_not_a_deletion, tests/test_unverified_rows_close.py::test_a_work_item_squashed_after_the_fork_is_not_this_branchs_removal

## docs/

The standing policy. Its index is `docs/README.md`.

## seal/

What the plugin maintains, read and written by machines. Every `seal/…` path
means `<repo>/seal/` where that directory exists, and the root under the git
common directory otherwise.

| File | The question it answers |
|---|---|
| `seal/README.md` | the export rules, for a session that never loads a skill |
| `seal/config.md` | what this repository says about itself, one row per item |
| `seal/follow-up.md` | which items wait on a named party, and who |
| `seal/specs/<work-item-id>/` | one work item's records, the table below |

## seal/specs/<work-item-id>/

One work item's records, from its first commit to the `settle` fold that
retires the directory. Which file each agent writes is
`skills/implement/SKILL.md` §3's table; this one says what each file answers.

| File | The question it answers |
|---|---|
| `routing.md` | who frames, builds and reviews this work, and where it ends — answered before the first edit |
| `spec.md` | what is built, its scenarios, and the decisions with their grounds |
| `plan.md` | in which phases it is built, how each is shown, and the approval line |
| `questions.md` | which decisions only a person could make, and how each was answered |
| `overview.md` | what the diff cannot show: purpose, divergences, what was not verified |
| `phases/phase-N.md` | what one build phase was asked, found and removed |
| `rounds/round-N.md` | what one review round read, found and closed |
| `changelog.md` | this work item's entry in the next release's notes |
| `broad-gate.md` | the orchestrator's one broad run, on either routing answer |
| `guarantee.md` | whether the sealer sealed the work, against the issue and the tree |

**The files keep these paths and stop mattering at two different times.**
`routing.md`, the SDD set (`spec.md`, `plan.md`, `questions.md`,
`overview.md`, `changelog.md`) and the process record (`rounds/`, `phases/`,
`broad-gate.md`, `guarantee.md`, and a `handoff.md` or `pr.*.md` where one
was written) stay until `settle --apply` applies the spec's rule changes,
and then the directory goes whole (`docs/release-checklist.md` §*2b*). What
a document still cites of it resolves at the tag of the release that
shipped it.
Enforced by: tests/test_settle_applies_rule_changes_in_place.py::test_apply_rewrites_in_place_and_removes_the_directory

## The root records

| File | The question it answers |
|---|---|
| `CLAUDE.md` | the rules a session in this repository must hold, each linking to its home |
| `CONTRIBUTING.md` | how a contribution is made and checked, and what a change to a gate must carry |
| `CHANGELOG.md` | which releases there are: the index, one `## X.Y.Z — <date>` heading each, newest first, with a link to the release's file |
| `changelog/<X.Y.Z>.md` | what one release changed, that release's section alone |
| `README.md` and `README.ko.md` | what the plugin is and how to install it |

**`CHANGELOG.md` and each release's own file carry that release's one
`## X.Y.Z — <date>` line.** `changelog/<X.Y.Z>.md` opens with it, and the
index keeps the same line above the link to the file, because the update
skill an installed copy already carries checks that an update landed by the
first `## ` line of `CHANGELOG.md`. The GitHub Release reads the release's
own file.
Enforced by: tests/test_the_changelog_is_gathered_at_release.py::test_the_index_and_the_release_files_agree

**A `CLAUDE.md` row that points at a home carries three things: the home's
path and section, the moment a session needs the rule, and the act in one
sentence of the row's own, with the value the act needs.** It carries no
table, reasoning or history. Only the home's sentences are pinned, so a stale
value in a row is a reviewer's finding. No two rule documents may share more
15-word runs than their pair was measured at, which does not see a rule
restated in fresh words.
Enforced by: tests/test_the_rules_claude_md_names_have_one_home.py, tests/test_no_passage_is_pasted_into_a_second_file.py
