# Implementation Plan: every finding carries an evidence line the check reads

<!-- seal/specs/1792368015-every-finding-carries-an-evidence-line/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

The grammar table in `docs/the-review-record.md` gains one row, `evidence:`,
which stands in a finding and is required once. `chain_check.py` already counts
and matches every row the table places in a finding, so the refusal needs no
code. The template, the review skill and the warden's definition state the line
in place of the prose they carry now. The warden's preload must not grow. One
paid warden side, compared against #967's last side, shows the rewrite is not
worse.

## Technical context

**The check needs no edit (read).**

- `chain_check.py#finding_of` (`:1030-1040`) builds its row list from
  `GRAMMAR.values()` where `where == IN_FINDING`. It counts each row with
  `#counted`, which refuses a `one` row with no line at the heading and a
  second line at that line. It then matches each line whole against the
  row's shape (`:1041-1055`).
- `label_of` iterates `LABELS`, and `misspelt` iterates `SPELT` and `MEANT`.
  All three are derived from `GRAMMAR` at import (`:443-466`).
- `READ_ROWS` (`:146-156`) lists only rows the check reads a value from.
  `severity:` and `answer:` are absent from it and are still enforced, and
  `evidence:` joins them on the same terms.
- The grammar loader admits a label row in `a finding` with `one`
  (`#grammar_row`, `:400-412`). Its shape must open with the label, and
  `evidence: (?:…)` does.

**Who reads round records, and which ones (executed, `git grep`).**

| Reader | Records it reads | Effect of the row |
|---|---|---|
| CI's `chain_check` (`.github/workflows/hygiene.yml:183`, the tree's copy) | Only the work items the pull request's own commits declare or change (`chain_check.py#main`, `:1816-1885`) | A record merged before the row is never read again. Every record of a pull request opened after the row lands must carry the line |
| The warden's step-7 `chain_check --worktree` (`agents/warden.md:47-51`) | The branch's records | Runs the plugin's copy. From this release on, it refuses the warden's own finding without the line, and the warden corrects it |
| `broad_gate.py#rounds_rows` (`:2511-2548`) | The work item's own records | A refused record adds nothing to the `deferred` row. The item's own records are new, so nothing changes |
| `.github/scripts/release_seal.py#chain_counts` (`:305-394`) | Every record of every pull request in the release, at the tag | v0.22.2's tag holds records written before the row: #966, #971, #976, #978, and any item merged before this one. One refused record sets the panel's `deferred` row to `not read` for that release (`questions.md` Q2) |
| `evals/scripts/noninferiority.py#report_rows` (`:188`) | The `location:` lines of a run's record (`FINDING_ROW`, `:73`) | No effect. Grading never reads the new line |

**The baseline can stand (executed).** #967's warden side is
`seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/warden-phase-4.json`.
It ran at rev `af716289` on suite `af9c924b7c5b…` with `claude-opus-5-5`, nine
cases at two runs each, and spent $41.7424. The case is three facts:

- **The preload is the same.** Its two preload hashes equal `shasum -a 256` of
  `agents/warden.md` (`9506b562…`) and `skills/agent-contract/SKILL.md`
  (`642b0da6…`) at `f10323f8`.
- **The files the warden opens are unchanged where it reads them.**
  `af716289` no longer resolves after its squash. #967's squash `f6ae6db6`
  stands in for it. `git diff --stat f6ae6db6 f10323f8` over `agents skills
  templates docs CLAUDE.md` names three files the warden opens:
  - `docs/the-review-record.md` changed only from `:265` on, which is
    §*The stamp*. The warden opens §*The round record* (`:8-145`).
  - `skills/code-review/scripts/chain_check.py` lost `strict=False` in one
    `zip` (`:893`) and gained `earlier_verdicts` for `guarantee.md`. No line
    on the record path changed.
  - `templates/config.md` changed wording in §*Broad gate* (`:27`,
    `:226-344`), not §*Reference specs* (`:363`).
  - `skills/code-review/SKILL.md`, `templates/sdd-round.md`,
    `skills/writing-style/SKILL.md` and `CONTRIBUTING.md` did not change.
- **The suite is the same.** It is pinned with `--suite-rev af9c924b`.

That is the comparison #968's framer made for the framer. One residue cannot
be pinned: the Claude Code version that runs the new side
(`claudeVersion` 2.1.302 on the baseline). The paid side records its own, and
the phase-3 record names the difference.

**#943's files are not touched.** `git grep` for a finding's label set
(`` `severity:` ``) in `skills/code-review/orchestration.md`,
`skills/implement/orchestration.md`, `CONTRIBUTING.md` and
`.github/workflows/tests.yml` finds nothing (executed). The orchestrator's
transition duty below is an act in this release's spawn prompts, not a doc
edit. #968's lines in `skills/implement/orchestration.md:381,416` are not
near anything this work changes.

**The risk phase 3 measures.** In a replay case, the warden's step-7 read
runs the measured tree's `chain_check` over the replayed branch. That
branch's earlier records predate the line, so the check refuses each of
their findings. #971's `false-rows.md:117` is this class: a pre-grammar
record judged by a later grammar, which counted as a `wrong` finding. Two
things guard against it. Step 7 already scopes the correction to "your
record", and the S10 paragraph says the missing line is no finding. If
rule 2 still fails on such rows, the cause is a sentence of this item, and
the fix and re-run is the one phase 3 budgets for.

**What breaks in six months.**

- **A warden writes `evidence: read` for a claim of absence.** The shape holds
  and the check passes it. Only the next round, or the person reading the
  record, sees that a `read` cannot show an absence. This is #985's stated
  limit, and S7 says so in the doc.
- **A warden satisfies the shape with a command that shows nothing,** such as
  `` `true` ``. The check cannot tell, and only a later round's re-run can.
- **A probe's command cannot be re-run.** The probe file was deleted under
  contract §7, so a later round re-runs a probe by writing it again from the
  `## Probes` row. The doc's paragraph says so.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. A new `evidence:` row, `a finding`, `one`, two backticked forms | A label a warden forgets is refused at the pull request, after the round. The warden's step-7 read catches it first, and the eval measures whether it does | **chosen**: the table is the grammar's one statement and the check already enforces every row it holds |
| B. Fold the label into `location:`, e.g. `` location: `a.py:12` (read) `` | `location:` names where the defect shows and the path a fix changes, and a `fixed` commit must touch one of its paths (`docs/the-review-record.md:91-99`). Grounds a finding read elsewhere would become paths a fix is held to touch. An `executed` command has no coordinate form. The fix pass appends to `location:` (`:101-105`), so the line would carry two writers' facts | rejected: it saves one line and makes the `fixed` rule read grounds as defect sites |
| C. Keep the prose rule and sharpen it in `agents/warden.md` | The sentence at `agents/warden.md:153-156` already ordered the coverage probe, and #971's row `false-rows.md:112` is a claim made without it | rejected by the owner's decision of 2026-10-19 |
| D. The check guesses an absence claim from the heading's words ("no", "missing", "lacks") and demands `executed` | A heading is free prose, so the guess refuses true `read` findings and passes absence claims worded otherwise | rejected: `CLAUDE.md`, "a noisy reading, or one guessed from words, is a report" |
| E. A cut-over in the check, by the grammar at a record's `target:` commit or by a date | In a user repository the table is the plugin's and the reviewed tree has none at any commit. A date is a stored coordinate kept beside the tree | rejected: the check's reading scope (records of the pull request's own items) is already the cut-over |
| F. Row `at most one`, with the requirement stated in code | Two statements of one count, the table's and the code's, drifting apart | rejected (`docs/the-review-record.md:21`) |
| G. Check each `executed` command against a `## Probes` row | Reads a real fact. The table's escaped pipes need a second cell parser, and the issue does not ask for it | out of scope (`spec.md`) |
| H. Check that a `read` path exists at the target commit | A warden in another repository cites the plugin's `docs/` (`agents/warden.md:26-29`), which that tree does not hold, so the check refuses a true claim | rejected |
| I. Take a fresh baseline side at `f10323f8` (about $42) | The same read set, measured twice. It buys nothing the hash comparison above does not show | rejected: #967's side stands, saving about $42 |
| J. The sealer re-runs `executed` lines | The sealer's step 3 gives a finding's verdict to the check (`agents/sealer.md:68-73`). Re-running the warden's evidence would re-judge what the verifying round already re-ran, and would change the sealer's preload, owing a sealer side | rejected: the sealer weighs no finding, so #985's clause holds with its definition unchanged |
| K. Measure on #971's new suite `11ebe8f4` | The owner keeps 0.22.2 on af9c924b (#971) | rejected |
| L. Rewrite the old records so every record in the tree carries the line | It writes evidence nobody recorded at the time, and no check reads those records again | rejected: the spawn prompt forbids it, and the reading scope makes it unnecessary |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The grammar.** The `evidence:` row in `docs/the-review-record.md`, the meaning paragraph with its `Enforced by:` lines (S7, S10), and the rewrite of `:214-215`. `templates/sdd-round.md`'s example finding and comment. The fixtures at `tests/test_chain_check.py#finding`, `tests/test_broad_gate.py:114` and `tests/test_the_release_seal_is_drawn.py:426` gain the line. New cases S1 to S5 are added, and S6's two cases are updated. No paid run | S1 to S5 seen red against the tree before the row, and S6 with the template's line deleted. Then `tests/test_chain_check.py`, `tests/test_broad_gate.py` and `tests/test_the_release_seal_is_drawn.py` run narrow and green, with any fixture the suite then refuses fixed and named in the phase record | |
| 2 | **The instructions.** `agents/warden.md` gets step 7's list and the probe sentence rewritten as the absence rule (S8). `skills/code-review/SKILL.md` gets §*The record*'s list and bullet and §*Earlier rounds*' re-run sentence (S9). The `PROBE["warden.md"]` pin moves, and the pins for S8 to S10 are added. The changelog fragment is written. No paid run | Each new pin seen red with its sentence deleted. `wc -c agents/warden.md skills/agent-contract/SKILL.md` totals 27,172 or fewer (S11), executed. The pinned modules run narrow and green | |
| 3 | **The measurement.** One warden side: `python3 evals/scripts/noninferiority.py run --agent warden --rev <phase-2 commit> --suite-rev af9c924b --out seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/warden-phase-3.json`. Then `compare --agent warden --phase 3 --old seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/warden-phase-4.json --new … --out …/evals/warden-phase-3.md`. **Paid: about $42** (the baseline's $41.74, #957's phase 3 $36.67). A `fail` that a sentence of this item caused is fixed and re-run once, about $42 more, so the ceiling is **about $84**. A fail with no sentence to blame follows `questions.md` Q1. Scheduling the run is the orchestrator's | `noninferiority.py check` on the record exits 0, or exits 1 with the reason Q1 lets stand, recorded in `phases/phase-3.md`. The phase record also counts how many of the 18 runs' records carry an `evidence:` line on every finding. It reads them from the traces `run` saves under `<out>.raw/` (`noninferiority.py:12-17`), because the graders at af9c924b read only `location:` lines. Whether a run reported an earlier record's missing line as a finding is read there too (`spec.md` S10) | |

The phases come in this order because phase 2's sentences cite the row
phase 1 writes, and phase 3 measures phase 2's commit. The first review round
follows phase 3. Its records are written under this item's grammar, so they
carry the line too (*Operational impact*).

## Operational impact

- **No migration and no rewrite.** The 119 existing records stay as they are,
  and no check reads them again.
- **This release's wardens run from the 0.22.1 plugin cache**, which knows
  no `evidence:` line. CI runs the tree's `chain_check`, which requires it. So
  from the moment phase 1 is committed, every warden spawned on this branch,
  and on any 0.22.2 branch that has rebased onto it, must be told in its
  spawn prompt to write the line. It must also read its record through the
  tree's copy, `python3 <worktree>/skills/code-review/scripts/chain_check.py`,
  not the cache's. Otherwise each of its findings is refused at the pull
  request. This is the orchestrator's act for 0.22.2 only, and from 0.22.3 the
  cache carries the line.
- **Order within 0.22.2.** No other 0.22.2 branch holds a round record of its
  own today (executed: `git diff --name-only` of #943's, #968's and #970's
  branches against their base). An item whose rounds are written before this
  item merges must merge before it, or have its rounds written after. The
  rewritten `:214-215` gives that rule.
- **v0.22.2's release panel.** The `deferred` row reads `not read`, because
  the records of the items merged before this one lack the line
  (`questions.md` Q2).
- **A user repository** meets the row when it moves `templates/hygiene.yml`'s
  `v<version>` pin. An item in flight across that move finishes under the
  rewritten `:214-215`.
- **No new dependency, no new environment variable.**
