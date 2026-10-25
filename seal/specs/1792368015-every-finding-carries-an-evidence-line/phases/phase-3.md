# 1792368015-every-finding-carries-an-evidence-line — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 8d4585b0 |


## What this phase was asked

Phase 3 is the measurement. The orchestrator ran its paid side. The smith
was asked two things. First, find the cause of the side's fail at no cost,
before anything is run again, testing one hypothesis first: a replay case's
earlier round records predate `evidence:`, step 7's `chain_check` refuses
them, and the warden spends its round on the refusal instead of the code.
The report gives the cause with trace coordinates, says whether it is this
item's change or noise, and names the smallest fix if it is the change. The
owner's rule is that a fail is recorded and its cause fixed once before a
second run. Second, once the owner decided, close the phase on that
decision, with the warden's row in the changelog fragment.

## What this phase found

**The measurement** (executed by the orchestrator, recorded at 8d4585b0 in
`evals/warden-phase-3.md`). One warden side ran at ba2a3187 on af9c924b's
suite, eighteen runs, none cut short. It was compared against #967's
`warden-phase-4.json`, which is `evals/baseline-warden.json` here.

| | Baseline | New |
|---|---|---|
| Preload bytes | 27,173 | 27,168 |
| Tokens per tool call | 87,862.4 | 85,306.7 |
| Spend USD | 41.7424 | 39.7893 |
| Tool calls | 940 | 872 |
| Report rows | 43 | 39 |
| Recall, true finds | 19 | 13 |
| False rate | 0.558 | 0.641 |

The verdict is `fail` on rules 1 and 2: recall fell, and the false-finding
rate rose. Every lost find is in a replay case. Every seeded case and the
rule case held.

**The diagnosis** (executed by the smith: Python scripts over the raw
output's `raw.json` and `traces/*.jsonl`, kept beside the worktree at
`985-warden-raw/`, and over every committed warden side on this suite;
nothing was re-run).

*The hypothesis does not hold.* In the 18 traces, every `chain_check`
result that names `evidence:` names the record the run itself is writing.
None names an earlier record. In the three replay cases that lost finds,
the earlier records are 0.21 table records. The check refused them as
old-shape records, with no `## Findings` and no `target:`, before the row
existed too (`traces/000.jsonl:155`, `traces/003.jsonl:147`). What the check
refused in a run's own record was its `verdict: open` lines, which it is
told to leave, and its references into those old-shape records. In two runs
it also refused an `evidence:` line of the run's own (`traces/003.jsonl:147`,
`traces/017.jsonl:154`). The first mixed `executed` and `read` on one line,
and the check at `:176` no longer names it. The time went the other way. The
two `replay-1791382684-r2` runs cost $3.05 and $2.71 against $4.30 and $4.79,
and read 5.2M and 4.9M tokens against 9.0M and 11.5M.

*Every finding carries the line.* All 39 findings of the 18 final records
carry an `evidence:` line, and 28 of them are `executed`. No finding raises
a record written before the row. That is `questions.md` Q4's answer for this
side.

*Where the six finds were lost.*

- **`replay-1791382684-r2`, truth-1, truth-2 and truth-3, 4 of 6 to 0 of
  6.** The prompt asks the round to check the fixes, then to "read the rest
  of the build `7608d82c..HEAD` fresh". Both new runs declined that read.
  Each record's `## Not judged` says the warden's verifying-round rule keeps
  the round inside the fix diff (`traces/000.jsonl:145`, the record's
  write, and the report at `:203`; `traces/001.jsonl:189`). truth-2,
  `hooks/routing.py:400-430`, lies outside the fix range `a6b0ac20..bf1e425a`
  and inside the build range (executed: `git diff --name-only` of both
  ranges), so only the declined read can find it. truth-1 is a class
  finding across the build's units. Baseline run 0 found it as one row
  naming six files, and neither new run wrote a class row. The
  verifying-round paragraph of `agents/warden.md` is the same at the
  baseline's preload and at ba2a3187. `git diff f10323f8 ba2a3187 --
  agents/warden.md` holds only this item's two hunks, step 7's list and the
  probe sentence (executed).
- **`replay-1791382684-r5`, truth-2, 1 of 2 to 0 of 2.**
  `docs/the-reader-registry.md:144-174` was not reached. Both new runs
  located the direction sentence at `:31-36`.
- **`replay-1791384160-r2`, truth-2, 1 of 2 to 0 of 2.** The truth is
  `skills/code-review/orchestration.md:369`. There the phrase "A / merge of
  the base inside the range brings none" wraps across two lines. Neither new
  run opened that file. `traces/005.jsonl:153` searched for the carriers with
  a line-based `git grep`, and its pattern `a merge of the base` cannot match
  across the wrap. That search is the finding's `evidence: executed` line.

*The same cases on the earlier sides of this suite.* Six sides ran on
af9c924b's suite before this one, from #957, #967 and this item's baseline.
Their truth totals are 13, 17, 16, 16, 14 and 19 (executed). The baseline's
19 is the highest of the six, and this side's 13 equals the lowest.

- `replay-1791382684-r2` found 2, 2, 1, 2, 1 and 4 of its 6 truths. The
  runs whose rows reach `hooks/routing.py`, the mark of the build read,
  were 2, 1, 1, 1, 1 and 2 of 2. This side reached it 0 of 2 times. At the
  earlier rate of 8 in 12, 0 of 2 comes about one time in nine.
- `replay-1791382684-r5` truth-2 was 0 of 2 on three of the six sides.
- `replay-1791384160-r2` truth-2 was 0 of 2 on the `2fc33333` side.

*Reading.* No trace coordinate ties a lost find to a sentence this item
changed. The largest loss rests on a scope decision under a paragraph that
did not change. Every other drop has happened on an earlier side of the same
suite. The fail reads as noise against a high baseline, which two runs a
case cannot prove. No sentence of this item is shown to cause the fail, so
the text had no fix to make before a second run.

**One link stays open.** The absence rule asks for a search, and a
line-based search is narrower than reading. `traces/005.jsonl:153` missed a
phrase that wraps across two lines. One case cannot show whether that costs
finds in general. #971's new suite is where it can be read again after
0.22.2.

**The owner's decision, 2026-10-19:** "노이즈로 기록하고 출시". The fail on
rules 1 and 2 is recorded as noise, the item ships, and no second side runs.
The grounds are the diagnosis above:

- the baseline's 19 is the highest of six sides on af9c924b;
- the `replay-1791382684-r2` loss traces to the verifying-round rule, which
  this item did not change;
- `replay-1791382684-r5` truth-2 and `replay-1791384160-r2` truth-2 were
  0 of 2 on earlier sides too.

`questions.md` Q1 covered a fail on rule 5 alone, and this fail was on rules
1 and 2. The decision is the owner's own, and Q1 is not its ground.
