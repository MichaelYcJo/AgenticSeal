# Feature Specification: the dash shapes become field words (#1000)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-review-record.md` §*The round record*, the paragraph opening "`chain_check.py` reads the table from this section" | The grammar table is loaded by `chain_check.py` at import, and "a change that moves this heading or the table moves the loader's path in the same commit". So the table's edit is made in this diff, with its loader, and not through `## Rule changes` |
| `docs/the-review-record.md` §*The guarantee* | One `Verdict:` line; a ready pull request needs `sealed`; a retired word fails naming its line. Its sentence naming the dash forms is this spec's one rule change |
| `docs/the-review-record.md` §*The stamp* | The stamp is drawn from `sealed`, and the `Target SHA` row's `; earlier run:` chain reading `sealed` counts as stamped |
| `skills/implement/SKILL.md` §*Document layout — two roots, three lifetimes* | A pull request does not edit the policy root; a spec states its changes in `## Rule changes` |
| `skills/settle/SKILL.md` §*Rule changes* | The no-change block `- nothing` with its one field `why:`, a value continuing four spaces in. Its one statement stays there; `## Not verified` cites it |
| `skills/settle/SKILL.md` §*A rule has one shape* | The precedent for a labelled line's sub-value: `check: none reader: <who reads it>`, and every other spelling refused at its line |
| `skills/implement/SKILL.md` §*4. The closing memo* | `## Not verified` is read by a machine and has one shape besides its table |
| `skills/verify/scripts/unverified_check.py#OLD_MARK` | The precedent for a retired spelling: the working tree's reading refuses it naming the edit, and a base revision's reads it, because a commit cannot be edited |
| `templates/config.md` §*What no row governs* | The words a checker reads stay English; the new words join that list |
| `CLAUDE.md` §*The rule a mechanism is kept against* | A fact has one source; a check gates only a fact it reads, not one guessed from prose |

## Scope

**In.** Every line shape that an agent writes or a check reads and that uses
an em dash as syntax, each made field words, stated once, and every other
spelling refused at its line.

1. **`## Not verified`'s `none — <why>`** in `overview.md` becomes the
   no-change block `- nothing` / `  why: <reason>`, the one `## Rule changes`
   and `## Removes` already use. The block's word, field and continuation
   are spelled once in code, in `skills/verify/scripts/unverified_check.py`,
   which `skills/settle/scripts/rule_changes.py` already loads; both section
   readers read the block through it.
2. **The sealer's verdict.** `Verdict: withheld — <reason>` and
   `Verdict: undecided — <question>` become `Verdict: withheld reason: <…>`
   and `Verdict: undecided question: <…>`. The line is read whole and exactly,
   emphasis included. An earlier run on the `Target SHA` row carries the word
   alone. The `Claims re-run` table's `does not hold — <what came back>` in the
   same template becomes `does not hold: <what came back>`.
3. **The round record's grammar table.** The three old-spelling rows, whose
   `Shape` cell is `—` and whose `Where` and `How many` restate the same fact
   as `nowhere` and `none`, leave the table for a two-column table of their
   own, `| Old spelling | Means |`, whose `Means` cell names the label as a
   code span. `meant_by`'s reading of a label out of the `Refused as` prose
   goes with them.
4. Every template, agent definition, skill, test fixture and eval generator
   that shows one of these shapes is rewritten in place to the new one.

**Out.**

- **The one-shot conversion script.** It converts nothing here: no live
  record carries an old form (counts under *Data & interfaces*). The build
  re-takes the counts at its base and converts by hand anything a sibling
  item landed since.
- **`release: X.Y.Z — <symptoms>`**, typed by the release session and read by
  `.github/scripts/publish_release_note.py`. Same class, but the line a
  session copies is `docs/release-checklist.md` §*5. The release pull
  request*, which this pull request may not edit: `questions.md` Q1.
- **`## X.Y.Z — <date>`**, the changelog heading. Only
  `.github/scripts/gather_changelog.py` writes it and only it reads it, so
  no agent or person types a near miss, and the released `changelog/*.md`
  files carrying it never change, so the reader keeps the old shape whatever
  this item does.
- **The 4-space continuation of `skills/settle/SKILL.md` §*Rule changes***.
  A different class, kept: `plan.md` A4.
- `Enforced by:` and the `## Rule changes` no-change form: #941, merged.
- Output formats in on-demand skills, such as `skills/confidence-check/SKILL.md`'s
  `Not ready: <check> — <what is missing>`: no check reads them, and #940
  rewrites those skills (owner's answer on #941's Q2).
- The em dash in refusal messages (`chain_check.py#DASH`): prose a person
  reads, which no reader parses.
- Prose that uses a dash as punctuation.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the block reads as nothing open | Given an overview whose `## Not verified` holds `- nothing` then `  why: every claim was run`, when `unverified_check.py` reads it, then it counts no row and reports no error; a `why:` value continued four spaces in reads the same | a case in `tests/test_unverified_rows_close.py` |
| S2 the old line is refused in the working tree, read at a base | Given `none — x`, `none - x`, `none`, `None.` or `nothing — x` as the section's first line, when the working tree is read, then each is refused at its line naming the block `- nothing` with `  why: <reason>`; read as a base revision (`strict_header=False`), the same line counts no row and no error | cases in `tests/test_unverified_rows_close.py`, each seen red against the old reader |
| S3 a near miss of the block is refused | `- nothing` with no `why:`, an empty `why:`, `- Nothing`, `* nothing`, `-nothing`, a `why:` at three spaces, a second field, and the block beside a table: each refused at its line | the same file |
| S4 the block is spelled once | The no-change word and its field are written as literals in `unverified_check.py` alone, and `rule_changes.py` and `settle.py` read them from there; every `## Rule changes` case still passes | `git grep -nE '"(nothing\|why)"' -- skills/settle/scripts skills/verify/scripts/unverified_check.py` prints lines of `unverified_check.py` only; `tests/test_settle_applies_rule_changes_in_place.py` |
| S5 the verdict reads in its three shapes | Given `Verdict: sealed`, `Verdict: withheld reason: the body claims a README change` or `Verdict: undecided question: does #12 ask for the flag?`, then `verdict_word` gives `sealed`, `withheld`, `undecided`; a ready pull request fails for the last two naming the file, the verdict and `sealed`; a draft and `--sealing` print the line | `tests/test_the_sealer_guarantees.py` |
| S6 a near miss of the verdict is refused at its line | `Verdict: withheld — x`, `Verdict: withheld - x`, `Verdict: withheld`, `Verdict: withheld reason:`, `Verdict: withheld reason:x`, `Verdict: Sealed`, `Verdict: **sealed**`, `**Verdict:** sealed`, `verdict: sealed`, `Verdict: sealed reason: x`, `Verdict: undecided reason: x`: each refused by the guarantee arm at its line, naming the three shapes; none is read as `sealed` | the same file, each seen red against the old reader |
| S7 a near miss draws no stamp and stops no commit | Each S6 line in a committed `guarantee.md` queues no stamp (`seal_stamp.queue_for_guarantee`), counts as no earlier `sealed` (`sealed_before`), and is not judged by `commitgate.guarantee_off_history` | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_commit_gate_decides_at_the_commit.py` |
| S8 the retired words keep their message | `sound`, `not sound` and `undecidable` fail naming the line and the word changed; the message names the three new shapes and no dash form | `tests/test_the_sealer_guarantees.py` (the retired-word case) |
| S9 an earlier run carries its word alone | `; earlier run: aaa1111 withheld` and `; earlier run: aaa1111 against main sealed` are read; `; earlier run: aaa1111 withheld — x` and `; earlier run: aaa1111 Sealed` are refused by the guarantee arm at the `Target SHA` row's line; the 13 live entries all read | `tests/test_the_sealer_guarantees.py` (`TestEarlierVerdicts`); the live count re-taken |
| S10 the grammar is two tables | `chain.GRAMMAR` holds the 12 rows the reader reads and no other; `chain.OLD_SPELLINGS == {"Target SHA:": "target:", "refixes:": "regression:", "fix of a fix:": "regression:"}`; neither table's cells hold an em dash | `tests/test_chain_check.py` (`TestGrammar`) |
| S11 an old spelling is still refused as the label it means | Every case of `test_a_label_in_another_spelling_is_refused_by_line` passes unchanged | `tests/test_chain_check.py` |
| S12 the loader refuses an old-spellings table it cannot read | No such table; a header other than `Old spelling`, `Means`; a cell that is not one code span; a `Means` that is no label of the grammar table; an `Old spelling` that is one; an old spelling twice; a grammar row whose `Where` is `nowhere`: each a GrammarError naming the document, exit 2 as a command | the parametrised loader case in `tests/test_chain_check.py` |
| S13 no shape is left | Outside `seal/specs/` and `changelog/`, a `git grep -n` for each of `none — <`, `withheld —`, `undecided —` and `does not hold —` (no trailing space, so a sentence wrapped after the dash is found) finds only `docs/the-review-record.md` §*The guarantee*'s sentence, which `## Rule changes` rewrites at the settle; and `docs/the-review-record.md` holds no `nowhere` cell | executed at the last phase |
| S14 the eval fixtures follow | `evals/scripts/rule_cases.py` writes the block, its five sealer scaffolds are regenerated from it, and the sealer graders' patterns still match the new verdict line | `tests/test_evals_layout.py` |

## Data & interfaces

**Live records, counted at cf351470** (executed, `git grep` and an `awk`
over each `overview.md`'s `## Not verified` section):

| Shape | Records carrying it | Converted |
|---|---|---|
| `## Not verified` opening `none` | 0 of 119 `overview.md` (all 119 hold the table) | none owed |
| `Verdict:` with a dash | 0 of 13 `guarantee.md` (12 `sealed`, 1 the retired `sound`) | none owed |
| `; earlier run:` entries | 13 entries in 11 `guarantee.md`, every one the bare word `withheld` | none owed: each already reads under S9 |
| grammar rows with a `—` shape | 3, in `docs/the-review-record.md` | this diff |

Outside `seal/specs/` and `changelog/`, the writers and pins of each shape
(executed, `git grep`):

| Shape | Writers | Reader | Pins |
|---|---|---|---|
| `none — <why>` | `templates/sdd-overview.md` (`## Not verified` comment); `skills/implement/SKILL.md` §4; the two refusal messages in `unverified_check.py#parse_section`; `evals/scripts/rule_cases.py` and its five `evals/behaviour/sealer/rule-sealer-*/scaffold.sh` | `unverified_check.py#parse_section`, which every other reader of the section reaches through `check_text` | 9 fixture lines in `tests/test_unverified_rows_close.py` (4), `test_broad_gate.py`, `test_the_gate_asks_the_range_ci_will_ask.py`, `test_the_gate_names_every_step_ci_runs.py`, `test_the_seal_is_taken_once_by_the_sealer.py`, `test_a_reference_root_is_read_and_never_taken.py` |
| `withheld — ` / `undecided — ` | `templates/sdd-guarantee.md`; `agents/sealer.md` (the base sentence, steps 1, 4 and 5); `skills/code-review/orchestration.md` (two sentences); `chain_check.py#RETIRED_SAYS`; `docs/the-review-record.md` §*The guarantee* (via `## Rule changes`) | `chain_check.py#verdicts_of`, `#verdict_word`, `#earlier_verdicts`, `#guarantee`; the stamp and the commit gate reach the same three through `seal_stamp.py#_chain_check` (`queue_for_guarantee`, `sealed_before`; `hooks/commitgate.py#guarantee_off_history`) | 24 lines in `tests/test_the_sealer_guarantees.py`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_commit_gate_decides_at_the_commit.py` |
| `does not hold — ` | `templates/sdd-guarantee.md` (comment and placeholder) | none | `tests/test_the_sealer_guarantees.py` (the claims-table case) |
| `—` shape cell | `docs/the-review-record.md` §*The round record* | `chain_check.py#grammar`, `#grammar_row`, `#meant_by`, `#OLD_SPELLINGS` | `tests/test_chain_check.py` (`TestGrammar`), `tests/test_the_pull_request_language_is_the_repositorys.py#_round_record_fields` |

**The `## Not verified` block.** The section holds the table or, alone:

```
- nothing
  why: <why nothing in this work item is left unverified>
```

The grammar is `skills/settle/SKILL.md` §*Rule changes*'s no-change block,
cited and not restated. In code, `unverified_check.py` holds the word, the
field and a function reading the block from a section's lines; `parse_section`
and `rule_changes.py#parse` call it. A first line that case-folds to `none` or
`nothing` and is not the block is refused naming the block. A base revision
reads that old line as no rows.

**The verdict line.** One line, exactly one of:

```
Verdict: sealed
Verdict: withheld reason: <the claim, its party, its coordinate>
Verdict: undecided question: <the question, for the owner>
```

One space after each colon and after the word, a non-empty value, no
emphasis and no markup before `Verdict:`. A line that means the verdict,
found the way `chain_check.py#MEANT` finds a misspelt round-record label, and
does not match whole is refused at its line. An owner's
`Answered <date> by <who>: <answer>` line under it is unchanged. The
`Target SHA` row's later-run part is `; earlier run: <sha> <word>`, with
`against <base>` after the SHA where a run names one. The constants
`reason:` and `question:` sit beside `WITHHELD` and `UNDECIDED` in
`chain_check.py`, the one reader.

**The grammar's two tables.** §*The round record* keeps the grammar table
with the twelve rows it reads, and adds, after it:

```
| Old spelling | Means |
|---|---|
| `Target SHA:` | `target:` |
| `refixes:` | `regression:` |
| `fix of a fix:` | `regression:` |
```

`grammar` finds it in the same section by its header row and builds
`OLD_SPELLINGS` from it. The `Where` vocabulary loses `nowhere` and the
`How many` vocabulary loses `none`. The sentence naming "an old spelling a
`nowhere` row names" and the loader paragraph's list of unreadable rows are
rewritten in the same commit, because the section is the grammar's one
statement and the loader reads it.

**Which `docs/` text changes where.** §*The round record* changes in this
diff: the loader reads it, and a release shipping the new loader beside the
old table stops every installed repository's chain check at exit 2. §*The
guarantee*'s sentence changes through `## Rule changes`: the sealer writes
from `agents/sealer.md` and the template, both changed here, so nothing
reads the sentence before the settle that applies it.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The guarantee
  from: and one `Verdict:` line — `sealed`, `withheld — <reason>`, or
    `undecided — <question>`.
  to: and one `Verdict:` line, `sealed`,
    `withheld reason: <the claim, its party, its coordinate>` or
    `undecided question: <the question, for the owner>`, written exactly so
    and with no emphasis. Any other spelling of the line is refused at it,
    and so is an earlier run's verdict on the `Target SHA` row that is not
    one of the three words alone.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `none — <why>` line of `## Not verified` and its reading | `skills/verify/scripts/unverified_check.py#parse_section` (the branch reading a first line that starts `none`, and the two messages naming the line), `templates/sdd-overview.md#"Not verified"`, `skills/implement/SKILL.md#"4. The closing memo — only what the diff cannot show"` | the no-change block, read by the shared block reader; a base revision's old line reads as no rows |
| `rule_changes.py`'s own spelling of the no-change word and its reading of the block | `skills/settle/scripts/rule_changes.py#NO_CHANGE`, `#NO_CHANGE_WRITTEN`, `#parse` (the block branch) | `unverified_check.py`, which `rule_changes.py` already loads |
| The verdict's dash forms and the prefix reading that let a rider through | `skills/code-review/scripts/chain_check.py#verdict_word`, `#RETIRED_SAYS`, `templates/sdd-guarantee.md#"The parties"` (the verdict comment and placeholder), `agents/sealer.md#"Order of work"` and its base sentence, `skills/code-review/orchestration.md` (the two `withheld —` sentences) | the field-word verdict, read whole by `chain_check.py` |
| Reading the verdict line through emphasis | `skills/code-review/scripts/chain_check.py#verdicts_of` (`EMPHASIS` stripped before the match) | refused at its line (S6); `EMPHASIS` stays for the round-record readers that use it |
| The reason after an earlier run's verdict word | `templates/sdd-guarantee.md` (`Target SHA` placeholder), `chain_check.py#earlier_verdicts` | the earlier run's own `guarantee.md` in git history |
| `does not hold — <what came back>` | `templates/sdd-guarantee.md#"Claims re-run"` | `does not hold: <what came back>` |
| The three `nowhere` rows and the words only they used | `docs/the-review-record.md#"The round record"` (rows `Target SHA:`, `refixes:`, `fix of a fix:`), `skills/code-review/scripts/chain_check.py#NOWHERE`, `#NOT_ANY`, `#meant_by`, `#grammar_row` (the `nowhere` branch) | the old-spellings table, whose `Means` cell is read as a code span |
| The pins of the old forms | the 9 `## Not verified` fixture lines and 24 verdict lines named under *Data & interfaces*, `tests/test_chain_check.py#TestGrammar`'s `nowhere` sets and `names no one label` cases, `tests/test_the_pull_request_language_is_the_repositorys.py#_round_record_fields`'s `NOWHERE` filter | rewritten to the new forms in the commit that changes each reader |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-20 by framer, before the build.
