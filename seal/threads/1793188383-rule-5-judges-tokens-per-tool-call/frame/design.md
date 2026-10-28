# Feature Specification: 1793188383-rule-5-judges-tokens-per-tool-call

Issue #992. Rule 5 of the behaviour evaluation
(`evals/scripts/noninferiority.py#verdict`) passes a rewrite only where the
tokens read across every model per tool call fall below the baseline's. The
figure is a ratio, so a side that does the same work in fewer calls can fail
it while its total tokens and its spend fall. And at two runs a case, a
rise of under one percent decides it. After this work, rule 5 fails a side
only where its total tokens and its tokens per tool call both rose by more
than a margin, `TOKEN_MARGIN`. Then every recorded comparison of the
issue's work items is read again under the new rule from its committed
record, with no paid run.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Today a fail on rule 5 alone, with every outcome grader holding, is shipped by the owner's answer case by case: Q1 of `0ed5dd3b:seal/specs/1792368015-every-finding-carries-an-evidence-line/questions.md`. After this work the rule decides those cases itself, and no person is asked. |
| `CLAUDE.md` *The rule a mechanism is kept against*, the sentence "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report" | A rise smaller than the recorded spread between two takes of one text is not read as a rise. That spread is 6.8 points of tokens per tool call (`0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md`, *Not done*), and `TOKEN_MARGIN` is sized from it. |
| `CLAUDE.md` *The rule a mechanism is kept against*, the sentence "A mechanism stays only while its history shows what it caught against what it costs" | Rule 5 is kept as a gate, and the premise that keeps it is checked on the recorded set: under the new statistic it still fails #957's framer side, whose total tokens rose 49.7% and whose tokens per call rose 18.9%, and it fails no other record (`plan.md` *Alternatives considered*). |
| `evals/README.md` *The behaviour suite*, item 5 of the pass rules | The reason the rule gives stays and now holds in both directions: the rewrite controls the context each call carries, and how many calls an agent makes is its behaviour, which rules 1 to 3 judge. Today the ratio holds calls out only where calls rise. |
| The owner's decision of 2026-10-17, the row "Phase 2: what rule 5 divides by" of `2fc33333:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/overview.md` | Rule 5 judged the total tokens alone until that decision. It was replaced because the warden made 19.3% more calls, found four more truths and read 17.8% more tokens in all. Total tokens alone is therefore not brought back. |
| `2fc33333:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md` *How the rewrite is proved not worse* | "A rewrite passes where its outcome holds or improves and its tokens fall", every figure against the baseline and none against an absolute. The new rule reads tokens against the baseline only. |
| `8a100e13:seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/plan.md` *Alternatives considered*, the row "Rewrite #957's records in place with the new verdicts" | A committed record stays as it was judged. The re-read writes its verdicts into this work item's phase record and edits no earlier record. |
| `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* | Each scenario below is a case in `tests/evals/test_noninferiority.py`, seen red against the base before `#verdict` changes. |
| contract rule 14 and contract rule 19 | The new reason line is pinned by a case in the same commit, and every sentence that states the old rule is rewritten where it stands (`## Removes`). |

## Scope

**In.**

1. **The statistic.** Rule 5 of `noninferiority.py#verdict` fails the new
   side where both of these hold: its tokens read across every model exceed
   the baseline's by more than `TOKEN_MARGIN` of the baseline's, and its
   tokens per tool call exceed the baseline's by more than `TOKEN_MARGIN`
   of the baseline's. Where either figure stays within the margin, rule 5
   passes. A figure exactly at the margin passes, as a false-finding rate
   exactly at `FALSE_MARGIN` passes rule 2.
2. **The margin.** One constant, `TOKEN_MARGIN = 0.07`, beside
   `FALSE_MARGIN` in `noninferiority.py`, applied to both figures. Its size
   is `questions.md` Q1, and 0.07 is the default the build uses.
3. **The reason line** rule 5 writes when it fails, as `## Data &
   interfaces` gives it, pinned by a case.
4. **The cases** in `tests/evals/test_noninferiority.py`: the rule 5
   entries of `VERDICTS`, the reason line in
   `Test_verdict::test_refuses_with_a_line_for_each_other_rule`, and
   `Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow`,
   as `## Data & interfaces` lists them.
5. **Every sentence that states rule 5 or what judges nothing**, rewritten
   in place: the module docstring of `noninferiority.py`, the docstrings of
   `#tool_calls`, `#verdict` and `#cost_rows`, and `evals/README.md`
   *The behaviour suite*, item 5 and the sentence after the list.
6. **The re-read.** The 17 comparison records `## Data & interfaces` lists
   are read with `noninferiority.py check`, once at the base and once after
   the change. The verdicts go into this work item's phase record as a
   table. No record is written into the tree, and no earlier record is
   edited.
7. **The changelog fragment**, `changelog.md` in this work item, written by
   the build's last phase (`docs/the-record-layout.md`).

**Out.**

- **Rules 1 and 2 against a baseline drawn high.** The issue's section *The
  same shape on rules 1 and 2* widens its question to every rule judged
  against one baseline side at two runs a case. Its *Done when* names rule
  5 alone. This work changes rule 5 alone, and `questions.md` Q2 holds the
  rest.
- **`noninferiority.py#cheaper_model`.** It reads `#verdict` only for a no
  result, and the conditions for a no result do not change. A side with no
  tokens, no tool call count or zero tool calls stays no result.
- **The record's shape.** `#render`, `#cost_rows`' rows, `#parse_record`
  and `COST_ROWS` keep every row and label. A record written before this
  change reads back under the new rule with no edit.
- **A paid side.** The issue's *Done when* re-reads the recorded sides at
  no cost, and this work runs no `noninferiority.py run`.
- **`.test_durations`.** It names the old case identifiers, and CI writes
  that file again.
- **The files other work items own.** None of the files the spawn prompt
  names as owned by #1041 or #1053 is touched. `docs/the-record-layout.md`
  is read for who writes `changelog.md`, and not edited.

## User scenarios & acceptance *(mandatory)*

Every scenario's numbers are the fixture `numbers()` of
`tests/evals/test_noninferiority.py`, whose baseline reads 1000000 tokens
over 100 tool calls, with the override the row names.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a new side with fewer calls and a smaller total, 900000 tokens over 80 calls, when `#verdict` reads it, then rule 5 passes, though its tokens per call rose 12.5% | the `VERDICTS` entry "rule 5: fewer calls and a smaller total, though each call read more", `pass`; seen red against the base, which gives `fail` |
| S2 | Given a new side with more calls and a larger total, 1200000 tokens over 150 calls, when `#verdict` reads it, then rule 5 passes, because its tokens per call fell | the `VERDICTS` entry "rule 5: tokens per tool call falling while the total rises", `pass`, unchanged |
| S3 | Given a new side whose total and tokens per call both rose 10%, 1100000 tokens over 100 calls, when `#verdict` reads it, then rule 5 fails with the reason line of `## Data & interfaces` | `Test_verdict::test_refuses_with_a_line_for_each_other_rule`, its `new_tokens` set to 1100000 and its last line the new reason line; seen red against the base, whose line differs |
| S4 | Given a new side whose total and tokens per call both rose 5%, 1050000 tokens over 100 calls, when `#verdict` reads it, then rule 5 passes, because both rises are within `TOKEN_MARGIN` | the `VERDICTS` entry "rule 5: the total and tokens per tool call both within the margin", `pass`; seen red against the base, which gives `fail` |
| S5 | Given a new side at exactly `TOKEN_MARGIN` above the baseline on both figures, when `#verdict` reads it, then rule 5 passes | a `VERDICTS` entry "rule 5: both figures exactly at the margin", `pass`, its tokens computed from `NI.TOKEN_MARGIN` so a change of Q1's answer keeps the case at the edge; seen red against the base |
| S6 | Given a new side whose total rose 20% and whose tokens per call equal the baseline's, 1200000 tokens over 120 calls, when `#verdict` reads it, then rule 5 passes | the `VERDICTS` entry "rule 5: tokens per tool call equal to the baseline's", `pass`; seen red against the base, which gives `fail` |
| S7 | Given a new side whose total and tokens per call both rose just past `TOKEN_MARGIN`, when `#verdict` reads it, then rule 5 fails | a `VERDICTS` entry "rule 5: both figures past the margin", `fail`, its tokens computed from `NI.TOKEN_MARGIN`; the base also fails it, so it is seen red with rule 5's comparison removed from `#verdict` |
| S8 | Given a passing record whose `New tokens read, every model` cell is edited to 1100000, when `check_record` reads it, then it reports that the record says `pass` and its numbers give `fail`, naming rule 5 | `Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow`, which today edits `New tool calls` from 100 to 90, rewritten to edit the tokens cell. The case as it stands goes red once the rule changes, since the calls edit no longer fails rule 5; the rewritten case is seen red with rule 5's comparison removed from `#verdict` |
| S9 | Given the 17 records of `## Data & interfaces`, when `noninferiority.py check` reads each after the change, then rule 5 fails only `957-framer-p3`, and the verdict of `967-framer-p4`, `967-warden-p4` and `943-sealer-p3b` turns from `fail` to `pass` | the phase 2 record's table, one `check` per record at the base and one at phase 1's commit, each exit code read directly; a verdict other than this prediction goes to `gaps.md` |
| S10 | Given a side with no tokens, no tool call count, or zero tool calls, when `#verdict` reads it, then it is no result, as before | the three `VERDICTS` entries "no result: tokens unknown", "no result: tool calls unknown" and "no result: no tool calls", unchanged |

## Data & interfaces

**The constant.** `TOKEN_MARGIN = 0.07` in `evals/scripts/noninferiority.py`,
next to `FALSE_MARGIN`, with a comment naming where its size comes from:
the 6.8-point spread of `0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md`.

**The rule.** With `T` the tokens read across every model and `C` the tool
calls, old for the baseline and new for the new side, rule 5 fails where
`new T > old T * (1 + TOKEN_MARGIN)` and `new T / new C > old T / old C *
(1 + TOKEN_MARGIN)`. The builder writes the comparison so that a figure
exactly at the margin passes, as rule 2 adds `1e-9` for the same reason.

**Why either figure within the margin is enough.** Total tokens are calls
times tokens per call. Where the new side made fewer calls, its tokens per
call rise by more than its total does, so the rule reads the total. Where
it made more calls, its total rises by more than its tokens per call do, so
the rule reads the figure per call. Either way the call count moves the
verdict in neither direction, and a side fails only where its context rose
by more than its call count explains.

**The reason line.** The line rule 5 appends when it fails, its numbers
formatted as today's line formats them, and the margin as a whole percent:

```
the new side read {new T} tokens across every model over {new C} tool calls, {new T / new C:.1f} a call, against the baseline's {old T} over {old C}, {old T / old C:.1f} a call: the total and the figure per call both rose by more than {TOKEN_MARGIN as a whole percent} (rule 5)
```

For S3 it reads `the new side read 1100000 tokens across every model over
100 tool calls, 11000.0 a call, against the baseline's 1000000 over 100,
10000.0 a call: the total and the figure per call both rose by more than 7%
(rule 5)`.

**The cases that change in `tests/evals/test_noninferiority.py`.**

| Case | Before | After |
|---|---|---|
| `VERDICTS` "rule 5: tokens per tool call 1.05 times the baseline's" | `numbers(new_tokens=1050000)`, `fail` | renamed "rule 5: the total and tokens per tool call both within the margin", `pass` (S4) |
| `VERDICTS` "rule 5: tokens per tool call rising while the total falls" | `numbers(new_tokens=900000, new_calls=80)`, `fail` | renamed "rule 5: fewer calls and a smaller total, though each call read more", `pass` (S1) |
| `VERDICTS` "rule 5: tokens per tool call equal to the baseline's" | `numbers(new_tokens=1200000, new_calls=120)`, `fail` | the same name, `pass` (S6) |
| `VERDICTS` "rule 5: tokens per tool call falling while the total rises" | `pass` | unchanged (S2) |
| `VERDICTS`, two new entries | none | "rule 5: both figures exactly at the margin", `pass` (S5), and "rule 5: both figures past the margin", `fail` (S7) |
| `Test_verdict::test_refuses_with_a_line_for_each_other_rule` | `new_tokens=1000000`, and the per-call reason line | `new_tokens=1100000`, and the new reason line (S3) |
| `Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow` | edits `\| New tool calls \| 100 \|` to 90 | edits `\| New tokens read, every model \| 900000 \|` to 1100000 (S8) |

The `{"tokens": 1100000}` parameter of
`Test_check_record::test_refuses_anything_but_pass` already fails under the
new rule and stays as it is.

**The records the re-read reads.** Each is `<commit>:<path>`, the commit
that added it; every one resolves (executed, `git show`). The rule 5
columns are the arithmetic over each record's `tokens read, every model`
and `tool calls` rows (executed, `git show` and `awk`), and phase 2's
`check` runs are what confirm them.

| Name | Record | Calls | Total tokens | Per call | Rule 5 today | Rule 5 after |
|---|---|---|---|---|---|---|
| 957-framer-p3 | `2fc33333:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/framer-phase-3.md` | up 25.9% | up 49.7% | up 18.9% | fail | fail |
| 957-sealer-p3 | the same directory, `sealer-phase-3.md` | down 13.4% | down 6.9% | up 7.6% | fail | pass |
| 957-smith-p3 | the same directory, `smith-phase-3.md` | down 7.1% | down 7.9% | down 0.8% | pass | pass |
| 957-warden-p2-run-1 | the same directory, `warden-phase-2-run-1.md` | up 19.3% | up 17.8% | down 1.3% | pass | pass |
| 957-warden-p2 | the same directory, `warden-phase-2.md` | up 10.7% | up 6.0% | down 4.2% | pass | pass |
| 957-warden-p3 | the same directory, `warden-phase-3.md` | up 11.7% | up 1.4% | down 9.2% | pass | pass |
| 967-framer-p4 | `f6ae6db6:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/framer-phase-4.md` | down 9.2% | down 0.5% | up 9.5% | fail | pass |
| 967-smith-p4 | the same directory, `smith-phase-4.md` | down 4.5% | down 20.9% | down 17.1% | pass | pass |
| 967-warden-p4 | the same directory, `warden-phase-4.md` | up 0.4% | up 1.2% | up 0.8% | fail | pass |
| 969-sealer-p4 | `4a6e24f6:seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/sealer-phase-4.md` | down 31.0% | down 35.1% | down 5.9% | pass | pass |
| 969-sealer-model | the same directory, `sealer-model.md` | down 20.3% | down 17.1% | up 4.0% | fail | pass |
| 975-sealer-p4 | `f1c9932d:seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.md` | up 16.9% | up 13.5% | down 2.9% | pass | pass |
| 976-sealer-p5 | `75502328:seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/evals/sealer-phase-5.md` | down 10.0% | down 11.0% | down 1.1% | pass | pass |
| 943-sealer-p3 | `b196fe9b:seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/evals/sealer-phase-3.md` | down 6.2% | down 7.6% | down 1.5% | pass | pass |
| 943-sealer-p3b | the same directory, `sealer-phase-3b.md` | down 11.1% | down 10.3% | up 0.9% | fail | pass |
| 968-framer-p2 | `a1909096:seal/specs/1792368014-the-framer-is-written-anew-from-its-job/evals/framer-phase-2.md` | up 57.8% | down 9.3% | down 42.5% | pass | pass |
| 985-warden-p3 | `2ff7b963:seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/warden-phase-3.md` | down 7.2% | down 9.9% | down 2.9% | pass | pass |

Every value of `TOKEN_MARGIN` from 0.01 to 0.18 gives the same 17 rule 5
verdicts (executed, the same arithmetic), so Q1's answer decides later
sides only. Five records keep a `fail` from another rule: `957-sealer-p3`
on rule 3, `957-warden-p2-run-1` on rule 3, `969-sealer-model` on rules 3
and 4, `943-sealer-p3` on rule 4, and `985-warden-p3` on rules 1 and 2
(read, each record's `Verdict:` block). `969-sealer-model` is the Opus
side against the Sonnet side, and `noninferiority.py model` decides it
without rule 5.

The phase 2 table carries, for each record: its name, its coordinate, the
verdict it records, the verdict and the rule 5 line `check` prints at the
base, and the verdict and the rule 5 line `check` prints after the change.
The base column is needed because some records were written under rule 3
before #966 changed it, so a record's own verdict can differ from what the
base code gives.

## Rule changes

- nothing
  why: no document of the policy root `docs/` states the behaviour evaluation's pass rules; they live in `evals/README.md` and `evals/scripts/noninferiority.py#verdict`, outside the policy root, and `tests/evals/test_noninferiority.py` holds them

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| Rule 5 as tokens per tool call below the baseline's, and its reason line | `evals/scripts/noninferiority.py#verdict` | the rule and reason line of `## Data & interfaces`, in the same function |
| The sentence that total tokens are written and judge nothing | `evals/scripts/noninferiority.py`, the module docstring and the `#verdict` docstring; `evals/README.md` *The behaviour suite*, the sentence after the list of pass rules | the same sentences, naming tokens per true find, spend and wall seconds as what judges nothing, since rule 5 now reads the total |
| Rule 5's statement as tokens per tool call | `evals/scripts/noninferiority.py`, the module docstring and the `#verdict` docstring; `evals/README.md` *The behaviour suite*, item 5 | the new rule, stated in each place |
| The reason "Rule 5 divides a run's tokens by this" | `evals/scripts/noninferiority.py#tool_calls`, its docstring | a docstring saying rule 5 reads the call count with the total, so that the count moves the verdict in neither direction; the sentence on tokens per true find stays |
| The clause "tokens per tool call, which rule 5 judges from the rows above it" | `evals/scripts/noninferiority.py#cost_rows`, its docstring | a clause saying rule 5 reads that row's figure together with the total |
| Three `fail` expectations on rule 5 and one reason-line pin | `tests/evals/test_noninferiority.py`, `VERDICTS` and `Test_verdict::test_refuses_with_a_line_for_each_other_rule` | the cases of `## Data & interfaces`, in the same file |
| The edited-cell case's `New tool calls` edit | `tests/evals/test_noninferiority.py#Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow` | the same case editing the tokens cell (S8) |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
