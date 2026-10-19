# 1792368015-every-finding-carries-an-evidence-line — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | open: a draft holding the smith's diagnosis of the first side, before the orchestrator closes the phase |


## What this phase was asked

Phase 3 is the measurement, and its paid side is the orchestrator's. The
side at ba2a3187 failed rules 1 and 2 against #967's `warden-phase-4.json`
(`evals/warden-phase-3.md`). Recall fell from 19 to 13, and the false rate
rose from 0.558 to 0.641. The smith was asked to find the cause at no cost,
before anything is run again. The hypothesis to test first: a replay case's
earlier round records predate `evidence:`, step 7's `chain_check` refuses
them, and the warden spends its round on the refusal instead of the code.
The smith reports the cause with trace coordinates, says whether it is this
item's change or noise, and names the smallest fix if it is the change. The
owner's rule is that a fail is recorded and its cause fixed once before a
second run. The evaluation is not run again here.

## What this phase found

This is a draft diagnosis. Every figure below was read from the committed
sides and from the raw output at `985-warden-raw/` beside the worktree
(executed: Python scripts over `raw.json`, `traces/*.jsonl` and the side
JSONs). Nothing was re-run.

**The hypothesis does not hold.** In the 18 traces, every `chain_check` result
that names `evidence:` names the record the run itself is writing. None names
an earlier record. In the three replay cases that lost finds, the earlier
records are 0.21 table records. The check refused them as old-shape records
(no `## Findings`, no `target:`) before the row existed too, as in
`traces/000.jsonl:155` and `traces/003.jsonl:147`. What the check refused in a run's own record was
its `verdict: open` lines, which it is told to leave, and its references
into those old-shape records. In two runs it also refused an `evidence:`
line of the run's own (`traces/003.jsonl:147`, `traces/017.jsonl:154`).
The first is an evidence
line mixing `executed` and `read`, which the check at `:176` no longer
names. The time went the other way. The two
`replay-1791382684-r2` runs cost $3.05 and $2.71 against $4.30 and $4.79,
with 5.2M and 4.9M tokens read against 9.0M and 11.5M.

**Every finding carries the line.** All 39 findings of the 18 final records
carry an `evidence:` line, and 28 of them are `executed`. No finding names an
earlier record's missing line. This answers `questions.md` Q4 for this side.

**Where the six finds were lost.**

- **`replay-1791382684-r2`, truth-1, truth-2 and truth-3 (4 of 6 to 0 of
  6).** The prompt asks the round to check the fixes and then to "read the
  rest of the build `7608d82c..HEAD` fresh". Both new runs declined that
  read. Each record's `## Not judged` says the warden's verifying-round rule
  keeps the round inside the fix diff (`traces/000.jsonl:145`, the record's
  write, and the report at `:203`; `traces/001.jsonl:189`). truth-2,
  `hooks/routing.py:400-430`, lies outside the fix range `a6b0ac20..bf1e425a`
  and inside the build range (executed: `git diff --name-only` of both
  ranges). It can only be found by the read the runs declined. truth-1 is a
  class finding across the build's units, and baseline run 0 found it as
  one row naming six files. Neither new run wrote a class row. The
  verifying-round paragraph of `agents/warden.md` is byte-identical at the
  baseline's preload and at ba2a3187. `git diff f10323f8 ba2a3187 --
  agents/warden.md` holds only this item's two hunks: step 7's list and the
  probe sentence (executed).
- **`replay-1791382684-r5`, truth-2 (1 of 2 to 0 of 2).**
  `docs/the-reader-registry.md:144-174` was not reached. Both new runs
  located the direction sentence at `:31-36`.
- **`replay-1791384160-r2`, truth-2 (1 of 2 to 0 of 2).** The truth is
  `skills/code-review/orchestration.md:369`, where the phrase "A / merge of the
  base inside the range brings none" wraps across two lines. Neither new run
  opened that file. `traces/005.jsonl:153` searched for the carriers with a
  line-based `git grep` whose pattern `a merge of the base` cannot match
  across the wrap, and that search is the finding's `evidence: executed`
  line. `traces/004.jsonl` cites the same kind of search.

**The same cases on the six earlier sides of this suite.** All six are on
af9c924b's suite, from #957, #967 and this item's baseline. Their truth
totals run 13, 17, 16, 16, 14 and 19 (executed). The baseline's 19 is the
highest of the six, and this side's 13 equals the lowest, af9c924b's own
baseline. Per case, the earlier sides read:

- `replay-1791382684-r2`: 2, 2, 1, 2, 1 and 4 truths of 6. Runs whose rows
  reach `hooks/routing.py`, the mark of the build read: 2, 1, 1, 1, 1 and
  2 of 2. This side reaches it 0 of 2 times. At the earlier rate of 8 in 12,
  0 of 2 comes about one time in nine.
- `replay-1791382684-r5` truth-2: 0 of 2 on three of the six sides.
- `replay-1791384160-r2` truth-2: 0 of 2 on the `2fc33333` side.

**Reading.** No trace coordinate ties a lost find to a sentence this item
changed. The largest loss rests on a scope decision whose governing paragraph
did not change, and every per-case drop has happened on an earlier side of
the same suite. So the fail reads as noise against a high baseline. Two runs
a case cannot prove that. One link stays open. The absence rule asks for a
search, and a line-based search is narrower than reading:
`traces/005.jsonl:153` missed a wrapped phrase. Whether that costs finds
in general, one case cannot show.

**The smallest fix.** No sentence of this item is shown to cause the fail,
so the text has no fix to make before a second run. Making the
verifying-round rule yield to a prompt that asks for a wider read would
change a paragraph this item did not touch, and the cases do not show it
caused this side's drop. `questions.md` Q1 covers a rule-5-only fail, and
this fail is on rules 1 and 2. Whether to record it as noise, run a second
side as it stands, or treat the search's narrowness as the cause is
therefore the owner's decision. The orchestrator carries it.
