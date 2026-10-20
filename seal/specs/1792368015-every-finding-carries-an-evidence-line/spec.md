# Feature Specification: every finding carries an evidence line the check reads

<!-- seal/specs/1792368015-every-finding-carries-an-evidence-line/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

#971's classing found one `wrong` finding on each side, and each stated what
the tree has or lacks without checking it
(`seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md:112`
and `:117`). The first was an uncovered-test claim made while
`agents/warden.md:153-156` already ordered the coverage probe. A sentence
asking for the check stood and did not hold, so the owner's decision of
2026-10-19 (issue #985, `## Decision`) is a shape a check reads: every finding
names what its claim rests on, on one labelled line.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-review-record.md` §*The round record*, the grammar table (`:39-54`) and *The record's grammar is the table below, and nothing else states it* (`:21-37`) | The `evidence:` line is one new row of the table and is stated nowhere else. The check refuses any line the table does not hold, so a missing or misspelt line is refused with no code beside the table |
| `skills/code-review/scripts/chain_check.py#finding_of` (`:1019-1089`), `#counted` (`:1129-1143`), `#misspelt` (`:902-910`), `LABELS`/`SPELT`/`MEANT` (`:443-466`) | Read, not executed: every row whose `Where` is `a finding` is counted per finding, matched whole and refused at its line, and the misspelling reader is derived from the table. A row `one` in a finding is therefore enforced by the module as it stands. `READ_ROWS` (`:146-156`) is only for rows the check reads a meaning from, and `evidence:` decides nothing, so it is not added there |
| `docs/the-review-record.md` §*What the check reads at the pull request*, *Nothing reads a record of the old table's shape* (`:209-216`), and `chain_check.py#main` (`:1816-1885`) | The check opens only the records of the work items the pull request's own commits declare or change, found by the `--baseline` diff. A record merged before the row is read by no check again, so the check's reading scope is the cut-over and no record is rewritten. The paragraph's last sentence, which tells an item in flight to rewrite its records, is rewritten for a line a past round never wrote (`## Removes`) |
| `skills/agent-contract/SKILL.md` §4 | `executed` and `read` are the contract's labels. This work brings them down to the finding and adds no third word: a finding cannot rest on `unverified`, which is a `## Not judged` row |
| `CLAUDE.md` §*The rule a mechanism is kept against*: "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report" | Whether a claim is one of absence is a judgment about prose. The check reads the line's shape and never guesses absence from a heading's words. The absence rule is the reviewer's and the next round's (#985, *The change*, last paragraph) |
| `agents/warden.md` step 7 (`:44-51`) and *Runs are narrow* (`:148-157`) | Step 7 lists the lines a finding holds, and gains `evidence:`. The coverage-probe sentence at `:153-156` is the prose rule that did not hold, and it is rewritten in place into the absence rule and the line |
| `skills/code-review/SKILL.md` §*The record* (`:117-124`) and §*Earlier rounds* (`:89-100`) | The warden opens this at step 1. The record's bullets list a finding's lines and say "executed and read labelled apart", which the line replaces. §*Earlier rounds* is where a later round is told to re-run an `executed` line where it weighs the finding |
| `agents/sealer.md` step 3 (`:68-73`): "a finding's verdict and its commit are the check's to read, not yours" | The sealer weighs no finding, so #985's "the sealer re-runs an `executed` line where it weighs the finding" holds with `agents/sealer.md` unchanged. See `questions.md`, decided from the tree |
| `evals/README.md` §*The behaviour suite*, rules 1 to 5, and `evals/scripts/noninferiority.py:702` (`>=` fails rule 4) | The warden's preload is `agents/warden.md` and the contract, 10,570 + 16,603 = 27,173 bytes at the tree this starts from (executed: `wc -c` at `f10323f8`). The baseline side's preload is 27,173 (read: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/warden-phase-4.md`), so the new preload must be 27,172 bytes or fewer. Every sentence `agents/warden.md` gains is paid for by bytes the file loses |
| Issue #971, owner's decision kept in #985's *Measured how* | The measurement runs on af9c924b's suite (`--suite-rev af9c924b`). #971's new suite takes effect after 0.22.2 |

## Scope

**In.**

1. **One `evidence:` row in the grammar table**, `a finding`, `one`. Its shape
   takes one of two forms. `evidence: executed` is followed by one or more
   backticked commands. `evidence: read` is followed by one or more backticked
   `path:line` or `path:first-last` coordinates. Each list is joined by `, `.
   A `read` coordinate always carries a line, because the line is what a reader
   opens.
2. **A paragraph in `docs/the-review-record.md` §*The round record*** stating
   what the line means:
   - a claim of absence is `executed` only. Absence means nothing catches,
     calls or states something, and `read` cannot show it;
   - the check reads the shape and never whether the claim is one of absence;
   - a later round re-runs an `executed` line where it weighs the finding,
     rather than re-deriving it;
   - a record written before the row lacks the line, and that is no finding.
     No check reads such a record again.

   Each part carries its `Enforced by:` line.
3. **The rewrite of `docs/the-review-record.md:214-215`.** A work item in
   flight across a change to the table meets the change as its own records
   stand. A renamed line is rewritten into its new spelling. An added line is
   never supplied after the round that would have written it.
4. **`templates/sdd-round.md`.** The example finding carries the line. The
   comment's label list says what it holds. The two "executed and read labelled
   apart" clauses (`:62`, `:78`) are rewritten to point at the line.
5. **`skills/code-review/SKILL.md`.** §*The record* adds `evidence:` to its
   list and rewrites its "executed and read labelled apart" bullet. §*Earlier
   rounds* says a later round re-runs an `executed` line where it weighs the
   finding.
6. **`agents/warden.md`.** Step 7 names the line. The coverage-probe sentence
   (`:153-156`) is rewritten in place as the absence rule. The preload must be
   27,172 bytes or fewer.
7. **The cases.** A finding with no line, with two, with the label spelt
   another way, and with each malformed form is refused at its line or
   heading. Both forms and their lists are read. The template is a record the
   check reads with the line in it.
8. **The fixtures** that build a finding and now need the line:
   - `tests/test_chain_check.py#finding` (`:73-94`);
   - `tests/test_broad_gate.py:114`;
   - `tests/test_the_release_seal_is_drawn.py:426`.

   Any other fixture the suite then finds refused is the work's to fix.
9. **The measurement.** One new warden side at the build's commit on
   af9c924b's suite, compared against
   `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/warden-phase-4.json`
   and recorded under this item's `evals/`.
10. **The changelog fragment.** It goes in this item's `changelog.md`
    (`docs/the-record-layout.md` §*A change writes fragments, never a shared
    file*).

**Out, and why.**

- **`skills/code-review/scripts/chain_check.py`, no edit.** The module reads
  every row the table places in a finding (Grounding row 2). Code that names
  the row would be a second statement of the grammar, which `:21` refuses.
  If the build finds a path where the row is not enforced, that is a
  divergence for `overview.md`, not a plan change.
- **No cut-over mechanism in the check.** Two were considered: reading the
  grammar at a record's `target:` commit, or a stored date. In a user
  repository the table lives in the plugin and not in the reviewed tree, so
  the first has nothing to read, and a date is a coordinate kept beside the
  tree (`CLAUDE.md`). `plan.md` Alternatives E.
- **No old record is rewritten.** 119 records under 22 `rounds/` directories
  predate the line (executed: `ls seal/specs/*/rounds/*.md | wc -l`). None is
  read by the check again.
- **`agents/sealer.md`, unchanged.** It reads no finding (Grounding row 8).
- **`## Confirmations` entries get no `evidence:` line.** The issue names
  findings, and the class #971 measured was findings. A confirmation keeps its
  "executed or read" prose, and the row would be refused there as a label
  outside a finding (`chain_check.py#OUTSIDE`).
- **The fix pass's `answer:` line gets no evidence label.** It is the
  smith's, and `skills/implement/SKILL.md` §5 allows two lines per finding.
- **Checking a `read` coordinate against the tree.** A warden in another
  repository cites the plugin's `docs/` (`agents/warden.md:26-29`), so a path
  missing from the reviewed tree is not a false claim. A refusal there would
  be a false refusal.
- **Checking an `executed` command against `## Probes`.** It reads a real
  fact, but the issue does not ask for it, and the table's escaped pipes would
  need a second parser. It is not filed. A later item can raise it from
  `plan.md` Alternatives G.
- **A new behaviour-eval case for the absence rule.** The suite is pinned to
  af9c924b, and a new case would measure on a different suite than the
  baseline. Whether the line cuts `wrong` findings is read on #971's new suite
  after 0.22.2 (#985, *Measured how*).
- **`skills/code-review/orchestration.md`, `skills/implement/orchestration.md`,
  `CONTRIBUTING.md`, `.github/workflows/tests.yml`.** These are #943's and
  #968's files. None states a finding's line set (executed: the `git grep` in
  `plan.md` §*Technical context*), so none needs this change.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A finding with no evidence line | Given a record whose finding holds `severity:`, `location:`, `verdict:` and `answer:` and no `evidence:` line. When the check reads it, then the finding is refused at its heading with `no \`evidence:\` line: a finding carries one`, followed by the row's `Refused as` | A case in `tests/test_chain_check.py::TestFindings`, seen red against the tree before the row lands |
| S2 The label spelt another way | Given `Evidence: read \`a.py:1\``, `**evidence:** …` or `evidence : …`. When the check reads it, then it is refused at its line as a label in another spelling, and the finding is not read past it | `tests/test_chain_check.py::TestFindings::test_a_label_in_another_spelling_is_refused_by_line`, extended to the new label |
| S3 A malformed value | Given each of: `evidence: read \`a.py\`` (no line), `evidence: read a.py:1` (no backticks), `evidence: executed pytest` (no backticks), `evidence: ran \`x\``, `evidence:` with nothing after it, and `evidence: executed \`x\` and more`. When the check reads each, then it is refused at its line with the row's `Refused as` | Cases in `tests/test_chain_check.py::TestFindings`, seen red |
| S4 Two evidence lines | Given a finding with two `evidence:` lines. Then it is refused at the second line, `2 \`evidence:\` lines; a finding carries one` | A case in `tests/test_chain_check.py::TestFindings` |
| S5 Both forms read | Given `evidence: executed \`git grep -n x -- tests\``, `evidence: executed \`a\`, \`b\``, `evidence: read \`a.py:3\`` and `evidence: read \`a.py:3-9\`, \`docs/b.md:12\``. Then each finding is read and decided by its `verdict:` as before | A case in `tests/test_chain_check.py::TestFindings` |
| S6 The template is a record the check reads | `templates/sdd-round.md`'s finding carries one `evidence:` line that matches its row whole, and the table's live label set is nine labels | `tests/test_chain_check.py::TestFindings::test_the_template_is_the_record_the_check_reads` and `TestGrammar::test_the_table_loads_and_every_line_matches_its_row_whole`, updated |
| S7 A claim of absence is `executed` only | The paragraph in `docs/the-review-record.md` states it, and says the check cannot read whether a claim is one of absence | `Enforced by: nothing — whether a claim is one of absence is read from its prose, which the reviewer and the next round judge`, written under the paragraph |
| S8 The warden writes the line | `agents/warden.md` step 7 names `evidence:` among a finding's lines. The rewritten probe sentence says an absence is a probe that is run and named on the finding's `evidence: executed` line | A pin case seen red with the sentence deleted. The `PROBE["warden.md"]` pin in `tests/test_the_seal_is_taken_once_by_the_sealer.py:8201-8204` moves to the new text. Behaviourally, phase 3's side, where every run's record goes through `chain_check --worktree` at step 7 |
| S9 A later round re-runs an `executed` line | `skills/code-review/SKILL.md` §*Earlier rounds* says a round re-runs an earlier finding's `executed` line where it weighs that finding, rather than re-deriving it | A pin case seen red with the sentence deleted |
| S10 A record written before the row is no finding | The paragraph says a record without the line that predates the row is read by no check, and its lack is no finding | A pin case on the paragraph. #971's `false-rows.md:117` is the class: a pre-grammar record judged by the new grammar |
| S11 The warden's preload stays below the baseline's | `wc -c agents/warden.md skills/agent-contract/SKILL.md` totals 27,172 or fewer | Rule 4 of phase 3's `compare` record. Before that, `wc -c` at the phase-2 commit, executed |
| S12 The warden's rewrite is not worse | `noninferiority.py compare` of the new side against `warden-phase-4.json` reads `pass`, or a fail stands under `questions.md` Q1's rule | `seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/warden-phase-3.md`, re-read by `noninferiority.py check` and recomputed by `tests/test_a_rewritten_definition_proved_non_inferior.py` |

## Data & interfaces

One row appended to the table in `docs/the-review-record.md` §*The round
record*, after `answer:` or beside `location:` (the build chooses the position):

```
| `evidence:` | `` evidence: (?:executed `[^`]+`(?:, `[^`]+`)*\|read `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`(?:, `[^`\s:/#][^`\s:#]*:[0-9]+(?:-[0-9]+)?`)*) `` | a finding | one | evidence is `executed` and each command run, or `read` and each `path:line` or `path:first-last` opened, backticked and joined by `, ` |
```

The `read` coordinate is `location:`'s coordinate with the line made
mandatory (`:45`). The shape refuses an absolute path and a `#`, as
`location:`'s does. A command holding a backtick cannot be written, which is
a stated limit (use `$( … )`). The `Refused as` wording is the build's to
settle against the other rows.

In a record the line stands in a finding, conventionally after `location:`:

```
### 1. no case covers the bound the parser keeps

severity: should
location: `tests/test_a_range_owns_what_git_lists_for_it.py`
evidence: executed `git grep -n own_commits -- tests/test_a_range_owns_what_git_lists_for_it.py`
verdict: open
```

Nothing reads a meaning out of the line, and no `Finding` field holds it. A
reviewer reads it.

## Rule changes

- nothing
  why: written: a finding's evidence line and an absence executed only, in
    docs/the-review-record.md *The round record*.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "the grounds, executed and read labelled apart" in the template's comment | `templates/sdd-round.md#"Then why it matters and the grounds, executed and read labelled apart"` (`:62`) | The `evidence:` line's row in `docs/the-review-record.md` §*The round record*. The comment says what the line holds |
| The placeholder's "executed and read labelled apart" | `templates/sdd-round.md#"<why it matters and the grounds, executed and read labelled apart>"` (`:78`) | The example finding's `evidence:` line. The placeholder keeps "why it matters and the grounds" |
| The bullet's "executed and read labelled apart" | `skills/code-review/SKILL.md#"The record">"Each finding gives why it matters and its grounds, executed and read"` (`:122-124`) | The bullet naming the `evidence:` line and the absence rule |
| The coverage-probe sentence | `agents/warden.md#"Runs are narrow, through the repository's runner.">"Asking whether the suite catches a finding is not that run"` (`:153-156`) | The same paragraph, rewritten into the absence rule and the line, in fewer or equal bytes |
| The pin on that sentence | `tests/test_the_seal_is_taken_once_by_the_sealer.py#PROBE` (`:8201-8204`, the `warden.md` entry) | The same entry, pinning the rewritten text. The smith's entry (`:8196-8200`) is untouched |
| "A work item in flight across the update rewrites its records into the shape before its pull request goes ready." | `docs/the-review-record.md#"What the check reads at the pull request">"Nothing reads a record of the old table's shape."` (`:214-215`) | The same paragraph, rewritten: a renamed line is rewritten into its spelling, and an added line is never supplied after the round that would have written it |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-19 by framer, before the build.
