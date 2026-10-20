# Implementation Plan: the dash shapes become field words (#1000)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-20 by the orchestrator, under the owner's `automation` answer and Q1's answer, when `smith` was spawned for phases 1–4.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. A later session, a reviewer and CI all read the tree, and a plan
with nobody's name on it is indistinguishable from one nobody approved.

Where the session builds the work itself, `<who>` is still a person and the
moment is still the first edit rather than a spawn — say so in place of the
clause about `smith`, and keep the shape.

That shape is `templates/sdd-routing.md`'s, whose `Answered <date> by <who>,
before the first edit.` line records the other batch the same way: the verb,
the date, who, and the moment it was given. The two are pinned against each
other, so neither spelling can drift into a second convention for one kind of
fact. -->

## Summary

Three shapes a check reads use an em dash as syntax, and each becomes field
words with one reader that refuses every other spelling at its line. `## Not
verified` takes the no-change block the spec sections already use. The
sealer's verdict takes a sub-label on its one line, as `check: none reader:`
does. The round record's three old-spelling rows leave the grammar table for
a two-column table of their own. The release pull request's title line
takes a `symptoms:` sub-label, and its reader and the docs a release session
copies from change with it. No live record carries an old form, so nothing
is converted.

## Technical context

- `skills/verify/scripts/unverified_check.py#parse_section` (lines 695-800)
  reads `## Not verified`. It accepts any first line that case-folds to start
  with `none` (line 710), so `none - x`, `None.` and `nonesuch` all pass as
  "nothing open". `check_text(..., strict_header=False)` is the base
  revision's reading, which already reads a retired mark (`OLD_MARK`, line 78)
  instead of refusing it.
- `skills/settle/scripts/rule_changes.py` (lines 28-41, 105-178) spells
  `nothing` and `why` and reads the no-change block inside its item parser.
  It loads `unverified_check.py` by path already (`reader()`), so the shared
  reader can hold the block without a new import direction.
- `skills/code-review/scripts/chain_check.py`: `VERDICT_LINE`, `WITHHELD`,
  `UNDECIDED`, `RETIRED_VERDICTS` and `RETIRED_SAYS` (lines 83-98);
  `verdicts_of`, `verdict_word`, `guarantee` (lines 1616-1690);
  `earlier_verdicts` (line 1364). `verdict_word` reads a value by its prefix,
  so `withheld - x` and `Sealed` both read as words. `grammar`, `grammar_row`
  and `meant_by` (lines 272-440) read the round-record table, and the
  `nowhere` branch (line 383) requires the shape cell to be `—`.
- The stamp has no reader of its own. `seal_stamp.py#_chain_check` (line
  1011) loads `chain_check.py`, and `_queue_one` (line 1187, under
  `queue_for_guarantee`), `queue_for_local_guarantee` (line 1277),
  `sealed_before` (line 1101) and `hooks/commitgate.py#guarantee_off_history`
  (line 262) call `verdicts_of`, `verdict_word` and `earlier_verdicts`. A
  change to those three is the stamp's change.
- `docs/the-review-record.md` lines 22-37 and 39-56 are the grammar's prose
  and table; lines 274-279 the guarantee's verdict sentence.
- `.github/scripts/publish_release_note.py#title_line_re` (line 122) reads
  `release: <version>\s+—\s*<symptoms>` from the tagged commit's `%B`
  (`commit_message`, line 185), and `title_from` (line 173) falls back to the
  tag name with a log line. `main` (line 507) leaves a release that exists.
  The pins are `tests/test_a_release_publishes_its_note.py` lines 10, 159-166,
  255-260 and 265-295.

**What breaks in six months.** An installed repository whose overviews carry
`none — <why>` goes red at its next pull request after upgrading, every such
overview at once, because CI reads the whole `seal/specs/` with the
plugin's reader. The refusal names the block to write, as U+2705's did. The
changelog fragment says so, and `## Operational impact` below.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1a. `## Not verified` takes the no-change block `- nothing` / `  why:`, read through one function in `unverified_check.py` | An overview's `why:` wrapped at two spaces is refused at its line, as #941's frame met in its own spec. Loud, one edit | **Chosen.** One shape for "this section holds nothing" across `## Rule changes`, `## Removes` and `## Not verified`, and one word for it where `none` and `nothing` were two; the owner's direction of 2026-10-20 rules out a value stated twice |
| A1b. One line, `none why: <reason>`, mirroring `check: none reader:` | A second spelling of "this section is empty" beside the block, with its own reader: the next section that needs one picks between two | Rejected: two shapes for one fact |
| A1c. Keep `none`, swap the dash for a colon, `none: <why>` | A colon is a lookalike of nothing, but the word still differs from the block's, and the reader keeps its prefix match | Rejected for the same split as A1b |
| A2a. The verdict keeps one line and takes a sub-label: `Verdict: withheld reason: <…>`, `Verdict: undecided question: <…>`; the line read whole, emphasis refused | A sealer that writes `**sealed**` is refused where it passed before, and the orchestrator spawns it again | **Chosen.** It is #941's `check: none reader:` shape for a labelled line; the sealer evals' patterns (`^Verdict:\s*\**withheld\b` in four `shape-verdict.md` graders, `^Verdict:.*no broad run` and its siblings in `evals/scripts/rule_cases.py#SEALER_RUNS`) still match without an edit; and exactness is the owner's direction of 2026-10-20. The round record's labels already refuse emphasis (`docs/the-review-record.md` §*The round record*) |
| A2b. Two lines, `Verdict: withheld` then `reason: <…>` under it | A new pairing to read under a line that already carries an owner's `Answered …` line beneath it; the four `^Verdict:.*<what it names>` patterns of `evals/scripts/rule_cases.py#SEALER_RUNS` stop matching, so the sealer's truth graders change too | Rejected: more structure and more pins for the same fact |
| A2c. Keep reading through emphasis | `**sealed**` passes and `**Sealed**` passes, the near miss the owner's direction rules out | Rejected |
| A3a. Keep the old-spelling rows in the grammar table and put a word, `none`, in the shape cell | Each row then states "old spelling" three times, `nowhere`, `none` and `none`, cross-checked by the loader; and `meant_by` keeps finding the meant label by mining the backticks of a prose cell, so an edit to that sentence ("of `target:`, not `verdict:`") stops every chain check at exit 2 | Rejected. The premise that keeps the rows, that the grammar has one table, was checked: the loader finds its table by header row, so a second header in the same section costs one lookup |
| A3b. The old spellings get their own table, `\| Old spelling \| Means \|`, both cells code spans | A rewrite of §*The round record* that drops the second table stops the check at exit 2 naming the document, as dropping the first does | **Chosen.** Each fact stated once; `NOWHERE`, `NOT_ANY`, `meant_by` and the `nowhere` branch leave; the issue's comment gave `none` as an example and left the spelling to the frame |
| A3c. An empty shape cell | A blank cell reads as a value forgotten | Rejected |
| A4a. Keep `skills/settle/SKILL.md`'s four-space continuation | A value wrapped at two spaces is refused at its line, "a line that is not a field of the item above" | **Kept.** A different class: the near miss is refused, never read as something else, and the fix is in the same file at the same line. A `to:` value states a rule and ends with its `check:` line on a line of its own (§*A rule has one shape*), so "a value stays on one line" cannot hold. #953 sealed the rule and #941 met it once |
| A4b. One line per value | Every `to:` that states a rule is refused | Rejected |
| A4c. Any indentation deeper than two spaces continues | A three-space line now reads as continuation, and the depth stops meaning one thing | Rejected: it trades a loud refusal for a looser grammar |
| A5a. The issue's one-shot conversion script, asserting counts and deleted | It asserts 0 before and 0 after and converts nothing | Rejected: the counts were taken (`spec.md` *Data & interfaces*). The build re-takes them at its base and converts by hand anything a sibling landed since |
| A6a. Every `docs/` edit in this diff, as #941 did | Breaks "a pull request does not edit the policy root" (`skills/implement/SKILL.md` §*Document layout*) for text no reader loads | Rejected for §*The guarantee* |
| A6b. Every `docs/` edit through `## Rule changes` | The release ships the new loader beside the old table, and every installed repository's chain check stops at exit 2 until a later settle | Rejected for §*The round record* |
| A6c. Split: the section the loader reads changes in the diff, the guarantee sentence through `## Rule changes` | §*The guarantee* states the old spelling until the owner's next settle | **Chosen.** The loader paragraph states that the table and its loader change in one commit; the sealer writes from the template and its definition, both changed here, so nothing acts on the stale sentence |
| A8a. The release title takes `release: X.Y.Z symptoms: <…>`, read whole, falling back to the tag name with a log line naming the expected shape and the line found | A release session that types the old dash line publishes under the tag name; the job stays green and its log says why, and one `gh release edit` repairs the title | **Chosen**, on the owner's answer to Q1. The sub-label is the verdict's and #941's shape. The fallback stays rather than a failure: the job runs after `main` has moved, and the module's own reasoning (a failed job there is a release stopped half-way) still holds |
| A8b. Fail the publish job on a malformed title line | A typo at the last step leaves a tagged release with no note until someone re-runs the job | Rejected for that reason |
| A8c. Keep reading the dash line too, for the history | Two spellings read, so a near miss of either passes; and no old line is ever read again, because every `vX.Y.Z` tag already has its release and a release that exists is never republished | Rejected |
| A7. Leave the verdict's earlier-run entries free text after the word | `<sha> withheld — x` reads as `withheld` by prefix, and a misspelt `Sealed` counts as no earlier stamp | Rejected: the entry carries the word alone, which every one of the 13 live entries already does |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `## Not verified` reads the no-change block (S1 to S4). The block's word, field and reading move into `unverified_check.py`; `rule_changes.py` and `settle.py` read them from there; the old line is refused in the working tree and read at a base; `templates/sdd-overview.md`, `skills/implement/SKILL.md` §4 and `templates/config.md` §*What no row governs* rewritten; the 9 fixture lines and `evals/scripts/rule_cases.py` rewritten and the five sealer scaffolds regenerated | S2 and S3's cases seen red against the old reader (contract §15); the modules `tests/test_unverified_rows_close.py`, `tests/test_settle_applies_rule_changes_in_place.py`, `tests/test_evals_layout.py` and the five files whose fixtures changed; S4's grep; the overview counts re-taken at the phase's base | |
| 2 | The verdict in field words (S5 to S9). `chain_check.py` reads the line whole, refuses a near miss at its line and an earlier run's entry that is not the word alone; `RETIRED_SAYS` names the new shapes; `templates/sdd-guarantee.md` (verdict, earlier run, `does not hold:`), `agents/sealer.md`, `skills/code-review/orchestration.md` and `templates/config.md` rewritten; the 24 verdict lines in three test files rewritten | S6 and S9's cases seen red against the old reader; the modules `tests/test_the_sealer_guarantees.py`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_commit_gate_decides_at_the_commit.py`; the guarantee and earlier-run counts re-taken; the `bin/settle` dry run lists this spec's change as pending, not refused | |
| 3 | The grammar's two tables (S10 to S12). `docs/the-review-record.md` §*The round record*'s three rows move to the old-spellings table and its two sentences are rewritten; `grammar` reads both tables, and `NOWHERE`, `NOT_ANY`, `meant_by` and the `nowhere` branch go; `templates/config.md`'s grammar sentence names both tables | S12's cases seen red with each branch deleted; the modules `tests/test_chain_check.py` and `tests/test_the_pull_request_language_is_the_repositorys.py` | |
| 4 | The release title line (S15 to S17). `publish_release_note.py#title_line_re` reads `release: X.Y.Z symptoms: <…>` whole; the fallback's log line names the expected shape and quotes the line found; the module docstring, `docs/release-checklist.md` §*5* and §*6*, and `docs/branch-and-release.md`'s bullet rewritten in the same commit as the reader | S16's cases seen red against the old reader; the module `tests/test_a_release_publishes_its_note.py`, S17's case included; S13's sweep over the whole tree, last | |

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

## Operational impact

- **Compatibility break for installed repositories.** An `overview.md` whose
  `## Not verified` opens with `none — <why>` is refused at the next pull
  request, naming the line and the block to write. A `guarantee.md` written
  by an older sealer in a dash form is refused at its line; a ready pull
  request already needed `sealed`, so only the message changes there.
- **The release that ships this item** is the first whose session types
  `release: X.Y.Z symptoms: <…>`, from §*5* as this diff leaves it. A session
  working from memory that types the dash line gets the tag name as the
  title and a log line saying why. The 54 published releases are not
  touched.
- No migration script, no new env var, no new dependency.
- `docs/the-review-record.md` §*The round record* changes in the plugin's
  shipped copy, which every installed `chain_check.py` loads.
