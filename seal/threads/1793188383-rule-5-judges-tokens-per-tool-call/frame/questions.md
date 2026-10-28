# Questions for the planner: 1793188383-rule-5-judges-tokens-per-tool-call

## Answered by the tree, not to be reopened

- **The statistic is either figure within the margin.** The issue asks
  which statistic holds the call count out of rule 5 and is not decided by
  one run's noise. The 17 recorded comparisons answer it: only the chosen
  rule passes the fewer-call sides and the noise-sized rise together, and
  it still fails `957-framer-p3`. The grounds are `plan.md` *Alternatives
  considered* and `frame/design.md` *Data & interfaces*.
- **Rule 5 stays a gate and is not retired.** `CLAUDE.md` says a mechanism
  stays only while its history shows what it caught. Under the new rule,
  rule 5 still names `957-framer-p3`, a rise of 49.7% in all that rule 4
  passed because the preload fell. The margin is what keeps a rise inside
  the recorded spread from deciding, which `CLAUDE.md`'s sentence on noisy
  readings asks for. The grounds are the row "Replace the structure" of
  `plan.md` *Alternatives considered*.
- **Total tokens alone is not brought back.** It was rule 5 until the
  owner's decision of 2026-10-17 replaced it
  (`2fc33333:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/overview.md`,
  the row "Phase 2: what rule 5 divides by").
- **One margin applies to both figures.** The one recorded spread is of
  tokens per call, and no spread of the total is recorded, so a second
  constant would have nothing to be sized from. Q3 holds the measurement.
- **A figure exactly at the margin passes**, as a false-finding rate
  exactly at `FALSE_MARGIN` passes rule 2 (`noninferiority.py#verdict`,
  the `1e-9` in rule 2's comparison).
- **The re-read covers #968's record too.** The issue's *Done when* names
  #957, #967, #969, #975, #976, #943 and #985. `a1909096`'s
  `framer-phase-2.md` is #968's comparison of the same kind, and leaving it
  out would leave its rule 5 verdict under the new rule unknown. Reading it
  costs one `check`.
- **The re-derived records are not re-read.** #966's `957-*.md` records
  (`8a100e13`) and #971's `971-warden-phase-3-11ebe8f4.md` (`8db076f8`)
  carry the same `tokens read, every model` and `tool calls` rows as the
  #957 records they were derived from (executed, `git show` of each), and
  rule 5 reads only those rows.
- **The re-read writes no record into the tree.** `check` recomputes a
  record's verdict from the record, so a copy would hold numbers already
  committed under a verdict line that goes stale at the next rule change.
  The verdicts go into phase 2's record as a table (`plan.md`
  *Alternatives considered*).
- **No rule of `docs/` changes.** No document of the policy root states
  the evaluation's pass rules (executed, `git grep` over `docs/`), so
  `## Rule changes` holds the no-change block.
- **The work needs no file another work item owns.** It edits
  `evals/scripts/noninferiority.py`, `evals/README.md` and
  `tests/evals/test_noninferiority.py`, and writes its own records. It
  reads `docs/the-record-layout.md` for who writes `changelog.md` and edits
  nothing in it.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How large is `TOKEN_MARGIN`? The tree gives one measurement to size it from: two takes of one `writing-style` text differed by 6.8 points of tokens per tool call (`0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md`, *Not done*). Turning that into a bar is a value somebody has to be accountable for, as `FALSE_MARGIN`'s 0.05 is. Every value from 0.01 to 0.18 gives the same verdicts on the 17 recorded records (executed, arithmetic over their rows), so the answer decides later sides only | a person | **0.05**, `FALSE_MARGIN`'s size: below the one recorded spread, so a rewrite that changed nothing can still fail on one take. **0.07**: the smallest whole percent that covers the recorded spread. **0.10**: wider than any recorded spread, and it passes a real rise of up to 10% on both figures. A different value changes one constant, and S5 and S7 read the constant, so no case changes | 0.07 | open |
| Q2 | Does this work item also change how rules 1 and 2 read a baseline drawn high? The issue's section *The same shape on rules 1 and 2* widens its question to every rule judged against one baseline side at two runs a case: #985's proofer side failed rules 1 and 2 against a baseline that, by the issue's figures, which this frame did not re-read and the owner answers for, was the highest of six recorded sides. Its *Done when* names rule 5 alone. The tree cannot settle it: any change to rules 1 and 2 needs either a baseline pooled from several paid sides of one suite, or a decision that those rules become a report under `CLAUDE.md`'s sentence on noisy readings. Both are a choice about what the evaluation gates, which the owner holds | a person | **Rule 5 alone**: this work ships as framed, and `gaps.md` names the section as not done, citing this row. **Rules 1 and 2 too**: the frame is redrawn with a rule for which recorded sides form one baseline, or with those rules as a report, and the work grows by a phase or a work item | rule 5 alone | open |
| Q3 | What is the spread of the total tokens, and of tokens per tool call, between two takes of one tree for one agent at two runs a case? The one recorded pair, #967's two warden takes, is an upper bound only: #969's files changed between them, and the first take's records, `668fd5f4` and `a3bf3832`, no longer resolve (executed, `git show`), so its total is not recorded | a measurement | Two paid sides of one tree for one agent, compared with `noninferiority.py compare`. This work pays for none, since the issue re-reads at no cost | `TOKEN_MARGIN` sized from the 6.8-point figure and applied to both figures; the row stays open until a release pays for such a pair | open |
