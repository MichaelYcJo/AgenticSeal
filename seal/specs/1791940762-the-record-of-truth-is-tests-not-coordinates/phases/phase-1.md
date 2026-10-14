# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c8f0b1fc |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The replacement, on one document. Add two rows to
`.github/scripts/budget_check.py` and `seal/budgets.md`:
`enforced-unresolved` (gate, ceiling 0) and `unenforced:<file>` (a two-sided
`+0` family). Use the resolver `skills/settle/scripts/fold_check.py#target_problem`
and add the eval-case branch. Take `docs/the-record-layout.md` to 0
unenforced. See S1–S6 each red. W3: #923's `rule_paragraphs` is not built
anywhere, so build it in `budget_check.py`, where #923 will reuse it, and
record that. Write no ledger rows and no `survivors.md` rows. Apply the
owner's tenet: existing is not a reason to keep.

Added mid-phase by the owner (2026-10-14): a rule's text lives once, as the
first sentence of the docstring of the test that holds it. Add a read-only
`bin/rules <doc>` that walks a document's sections and expands every
`Enforced by:` target to that docstring's first sentence, through the same
resolver; it prints to stdout, writes nothing, never fails, and is shown on
`docs/the-record-layout.md`.

## What this phase found

**W3, answered by the work.** `grep -n rule_paragraphs` found nothing on the
tree rebased onto f975ea66. It is built in `budget_check.py` to #923's
grammar (`**`, `- **`, `* **`, `N. **`, opening a block outside fences,
comments and tables; closing after `Enforced by:` or at a blank line, a
heading, a table or the next list item). A bold word a wrap carries to the
front of a line inside a paragraph opens nothing. `shown_lines`,
`enforcer_lines`, `rule_files` and `targets_of` sit beside it, and
`Paragraph` carries the line, heading, first line and enforcer #923's
identity gate and candidates list need. `docs-history`'s `rule_lines` still
opens on `**` alone; #923 S5 is what widens it, and the two readers are
not yet one.

**The frame's count of the slice was 9; the grammar it names counts 14.**
The five extra are list items (`- **A release ledger file.**` and F3's four
bullets). At the start, 13 of the 14 had no `Enforced by:` inside their
paragraph: two rules (§*A commit after the build…*, §*A range owns…*) had
their line one or more paragraphs below, which the grammar does not reach.
After: 8 rule paragraphs, every one closed by targets that resolve.

| `docs/the-record-layout.md` | before (cb8a1685) | after |
|---|---|---|
| lines · bytes | 336 · 22,734 | 255 · 18,352 |
| rule paragraphs · unenforced | 14 · 13 | 8 · 0 |
| history lines (`docs-history` row) | 11 | 8 |

**The census of the slice's rules**, old paragraph to where it stands now:

| Old | Now |
|---|---|
| §*The size a reader takes whole*, "1,000 lines and 64 KB" | the line half, same heading, enforced by `test_a_document_has_room_for_the_next_fold.py::test_every_document_in_docs_is_under_the_ceiling_or_frozen`. The byte half is gone: nothing enforced it, and its only grounds were ledger rows, which this work item retires |
| the same, `- **A release ledger file.**` | gone with the byte half: with no byte target it is not over target. The table's ledger row now says each release file is under target (the largest is 751 lines) |
| §*A change writes fragments*, "Both kinds of fragment are gathered" | same place, enforced by the gather-step and fold cases |
| §*A commit after the build…* | same place; its `Enforced by:` line moved up to close the rule paragraph |
| §*A range owns the commits…* | same place; its `Enforced by:` line moved up likewise |
| §*A range owns…*, the survivor sweep paragraph | unchanged; phase 2 deletes it with the sweep |
| F1 (the commit-gate cut) | gone: built, and the §*docs/* table names the three files |
| F2 (one changelog file per release) | §*The root records*, as the rule that both files carry the release's `## X.Y.Z — <date>` line, with the update-skill why, enforced by `test_the_index_and_the_release_files_agree` |
| F3 and its four bullets | gone: the live rule was already the paragraph under §*seal/specs/<work-item-id>/*, now bold-led and enforced by three `test_settle_retires_the_process_record.py` cases; "first act of §*2b*" and the guards moved into it. "One file per run is rejected" and "Released items are not exempt" were decision history |
| F4 (the CLAUDE.md homes) | §*The root records*, as the rule a `CLAUDE.md` row carries, enforced by the two modules that held it |

The one pin of a removed sentence, `"Built by #729."` in
`tests/test_settle_retires_the_process_record.py::test_each_carrier_says_when_the_process_record_leaves`,
was seen red on the new document and re-pointed to "`settle --retire-process`
removes it at the next release, fold or no fold".

**S6 contradicts S4, and the build follows S4.** S6 says each rule names a
resolving test "or `nothing — <why>`"; S4 and §*The replacement* count
`nothing` as unenforced. A count of 0 therefore means every rule names a
target. A bare `nothing` with no `— <why>` is read as a target by
`fold_check.py#names_targets` and fails `enforced-unresolved`; a case pins
that.

**The frame says the resolver refuses a name defined twice. It does not.**
`evidence_check.py#named_unit` returns `('def', 'def')` for a function
defined twice and `target_problem` passes it (probe, executed). A constant
is refused. Nothing was added: a second rule in `budget_check.py` alone would
make the two checkers disagree, which is alternative E's failure. The
docstring says so.

**`enforced-unresolved` reads every `Enforced by:` line a renderer shows in a
rule file, inside a rule paragraph or not.** 0 on the tree.

**Today's numbers.** 66 rule files (#923 counted 68 on its own glob),
1,090 rule paragraphs, 972 unenforced; `docs/` 385 of 503. 55 files with a
count above 0 are listed in `## Unenforced rules`; a file at 0 is not listed,
because the family row's ceiling of 0 already holds it. `docs/the-record-layout.md`
is held that way.

**`preload:claude-md` was already over at HEAD.** cb8a1685 grew `CLAUDE.md`
to 9,827 bytes before #930's budgets reached the branch, so the tree's run
failed before this phase. The ceiling is raised to 9,827, and the pull
request body owes `Budget raised: preload:claude-md 9261 -> 9827: <reason>`
(`budget_check.py --baseline origin/release/v0.22.0` exit 1 without it, 0
with it).

**`rules docs/the-record-layout.md` shows how far the docstrings are from the
owner's model.** Of its 21 targets, all resolve; 4 have no docstring, and
several first sentences state no rule (`"S6 of #860."`, `"S2 of #728."`,
`"S7, #805's shape."`, and `chain_check.py#fragment_left_behind`'s return
shape). The command reads them as they are; rewriting a test's first
sentence into the rule it guards is work this phase did not take.

**Every new unit was broken once and a case went red** — 28 mutations
through `mutation-check`, one per unit or branch, over `rule_paragraphs`
(list-item opener, block start, blank-line close, the kept enforcer),
`shown_lines`, `enforcer_lines`, `rule_files`, `targets_of`, `target_problem`
(the eval branch, `case.yaml`, the two segments), `measure_unresolved`,
`unenforced_values`, `measured_row`'s detail, `unlisted_band`'s noun, the
`unenforced` table title, the slice document's own line, and `rules.py`'s
`first_sentence`, `docstring`, `describe`, `render` and `main`. One, the
render line for a section with no enforcer, survived against the fence case
alone and went red against the case that covers it.
