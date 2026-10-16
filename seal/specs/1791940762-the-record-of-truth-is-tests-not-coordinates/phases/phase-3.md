# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | ef1dc948 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The data leaves, as `plan.md` phase 3 states it: `git rm` the 45 released
ledger files, `seal/ledger.md` and the ledger fragments, with the S7 case
planted first and seen red; delete `docs/the-evidence-ledger.md` (#944 owns
the deletion, not #941) and move its still-ruling statements whole to their
homes, `docs/the-record-layout.md` and `skills/settle/SKILL.md`; rewrite the
layout tables. By the orchestrator's decision on phase 2's open item 1,
remove `settle.py#coordinates` and `#segment_of`, which group settle's report
by ledger rows, and the grouping's sentences in the settle skill, release
checklist §2b and both READMEs. No new ledger rows; `enforced-unresolved` at
0 at every commit.

## What this phase found

**The data.** 0655544e removed 47 files: `seal/ledger.md`, the 45
`seal/releases/*.md` and one fragment, `seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md`
(#930's). S7 is `tests/test_release_hygiene.py::test_this_repository_has_one_root_laid_out_by_lifetime`,
which named all three paths on the tree before the removal (executed, red),
with `test_a_planted_ledger_file_is_named` planting each; two mutations of
`ledger_leftovers` turned the planted case red. Twelve cases whose subject was
the real ledger went with it, across `test_release_hygiene.py` (7 units),
`test_unverified_rows_close.py`, `test_settle_reads_before_it_removes.py`
(3 cases, 3 helpers), `test_the_ledger_fragments_fold_at_release.py` (2) and
`test_a_row_points_by_content.py` (1); the five-copies case lost its ledger
copy and `test_one_word_one_meaning.py` its three ledger exemptions.

**The grouping.** 6fdf1530: settle's report lists the released, unfolded
items under *waiting for a fold*, and the session places each by its spec.
Fourteen grouping and section-liveness cases went with `coordinates`; the
census lost three lines and `test_a_format_has_one_reader.py` one exemption.
Settle §2 is renamed *Write one standing statement per rule*; its three pins
were red on the new heading and re-pointed. `unverified_check.py#live_lines`'s
docstring no longer cites the deleted indented-row case; that an indented
marker is no fold record was executed (`folded_items` returned `set()`).

**The census of `docs/the-evidence-ledger.md`**, every statement to its new
home or out (ef1dc948):

| Statement | Now |
|---|---|
| A coordinate names content, never a position | out, with the ledger |
| An anchor degrades to `DRIFTED`, never to `BROKEN` | out, with the ledger |
| Which file a change writes (the ledger half) | out, with the ledger |
| A released ledger file never changes; a re-read is a citing row; families; a citation that does not hold; `--into`; `correction-check`; without the row; the five things `--reverify` leaves | out, with the ledger |
| A row may name the test; the sealed run's record; one form or the other; a released row moves onto its test | out, with the ledger |
| `path::name` has one resolver | layout §*The fold…*, ledger half cut, names `enforced-unresolved` |
| A name a person reads is the file opened; a narrowed read names what it skipped | out, with the ledger |
| The checker parses each Python file once | out: `evidence_check.py#py_spans`'s docstring states it, and phase 4's kernel module holds the cases |
| A unit is bounded only where a real parser decides | out: `evidence_check.py#resolve_unit`'s docstring states it; phase 4's kernel module |
| A baseline reference is resolved once | layout §*The unverified record, and the baseline it is read against* |
| Every folded statement has the fold's shape | layout §*The fold…*, history sentences cut |
| A document over the ceiling takes no new statement | layout §*The fold…*, split history cut; its values pin re-pointed and renamed `test_the_record_layout_states_the_values_the_config_rows_hold` |
| A fold into a `.ko.md` edition is a fold into both | layout §*The fold…* |
| A directory is folded, then removed; the marker is the record | layout §*The fold…*, one paragraph, worded to link the skill |
| A marker counts only on a live line; both readings; the top level | layout §*The fold…*; the top-level paragraph is plain and its test joins the head's line |
| A released work item with no `spec.md` | layout §*The fold…* |
| Whether a line is live, six readers | layout §*The fold…*; each bullet names its cell test; *not one of the seven* now *of the six*; the sweep clause and `#667` cut |
| A fold is not a work item | layout §*The fold…*, fragment half cut |
| A population floor is replaced, never lowered | layout §*The fold…* |
| A `seal/` root with no work item reads as settled | layout §*The fold…* |
| A fold marker is exempt from the wrap limit | layout §*The fold…*, its stray chain-check sentence cut |

**Nothing moved into `skills/settle/SKILL.md`, and the wrap limit is why.** The
first draft put the fold-not-a-work-item, floor, retirement and target-grammar
rules there with their `Enforced by:` lines. That file and `CONTRIBUTING.md`
are held to 88 columns by `tests/test_docs_line_wrap.py`, which skips only an
`Enforced by:` line inside a marked `docs/` statement; every line naming a
test case was over (executed, red). Both files were restored and the
statements went to the layout. The settle skill changed in this phase only by
losing the grouping.

**The layout and the settle skill now share 14 fifteen-word runs, the same
count the deleted document's pair was measured at.** The first draft shared
three passages word for word; they were reworded in the layout to link the
skill, and `test_no_passage_is_pasted_into_a_second_file.py` passes with no
baseline row added (executed).

**Every live citation of the file is re-pointed or retired.**
`git grep -n the-evidence-ledger` outside `seal/specs/`, `changelog/` and
`.test_durations` names nothing (executed). A fold or liveness citation now
names the layout; a citation of a ledger section in a file phases 4 and 5
delete names *the ledger policy at `v0.21.1`*. Two printed messages,
`evidence_check.py#INTO_HELD` and the advisor's, name the evidence-check skill
instead; the pin of the first was red against the old text (`mutation-check`).
Three units whose docstrings changed declare their read class now
(`overflow_rows`, `fence_spans`, `conftest.py#committed_round_records_on_disk`)
and left the census, which refuses a re-hash.

**The layout's own history count rose by two and came back.** Bullet lines
are not rule lines to `docs-history`'s reader, so the two `#667` mentions in
the liveness bullets counted; they now say *before the walk*.

**Budgets.** The deleted file's two rows (`docs-history` 4, `unenforced` 13)
go. `unenforced:docs/the-record-layout.md` stays 0, held by the family row.
`budget_check.py` exit 0 on the tree and against `origin/release/v0.22.0`
with an empty body.
