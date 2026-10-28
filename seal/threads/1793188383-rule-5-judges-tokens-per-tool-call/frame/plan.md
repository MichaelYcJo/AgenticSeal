# Implementation Plan: 1793188383-rule-5-judges-tokens-per-tool-call

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

Two phases. Phase 1 rewrites rule 5 of `noninferiority.py#verdict`: a new
side fails it only where its total tokens and its tokens per tool call both
rose by more than `TOKEN_MARGIN`, 0.07 of the baseline's. The cases come
first, each seen red, and every sentence that states the old rule is
rewritten in place. Before its first edit, phase 1 also reads the 17
recorded comparisons with `check` at the base. Phase 2 reads the same 17
records with `check` after the change, writes the table of verdicts into
its phase record, and writes the changelog fragment. No side is paid for.

## Technical context

Coordinates are at the branch's base, `8a1173c8` (read).

- `evals/scripts/noninferiority.py:102` holds `FALSE_MARGIN = 0.05`.
  `TOKEN_MARGIN` goes beside it.
- `evals/scripts/noninferiority.py#verdict` (`:762`). Rule 5 is the last
  comparison, at `:883` to `:893`: a cross-multiplied test of tokens per
  call, `new_tokens * old_calls >= old_tokens * new_calls`, and its reason
  line. The checks above it already return `no result` where either side's
  tokens or calls are None or its calls are zero, so the new comparison
  divides by no zero.
- The sentences that state rule 5 or what judges nothing: the module
  docstring at `:40` to `:53`, the `#tool_calls` docstring at `:416` to
  `:428`, the `#verdict` docstring at `:762` to `:781`, and the
  `#cost_rows` docstring at `:965` to `:969`. In `evals/README.md`
  *The behaviour suite*, item 5 of the pass rules (`:47` to `:50`) and the
  sentence after the list (`:52` to `:53`). `git grep` over the tree outside `seal/`,
  `changelog/` and `CHANGELOG.md` finds no other sentence stating rule 5
  (executed). The released changelog states rule 5 as it shipped, and is
  history this work does not edit.
- `tests/evals/test_noninferiority.py`: `numbers()` at `:97`, whose
  baseline reads 1000000 tokens over 100 calls and whose new side 900000
  over 100; `VERDICTS` at `:1453`, with the four rule 5 entries at `:1537`
  to `:1552`; `Test_verdict::test_refuses_with_a_line_for_each_other_rule`
  at `:1626`; `Test_check_record` at `:1835`, whose edited-cell case edits
  the calls cell at `:1848`.
- A record carries every number rule 5 reads, in its `tokens read, every
  model` and `tool calls` rows, and `#parse_record` reads them back. So
  `noninferiority.py check RECORD.md` recomputes any committed record's
  verdict under the code that runs it, with no side file and no paid run.
  Nothing in the tree runs `check` over a committed record: `check_record`
  is called only by `#check` and by the test module (executed, `git grep`).
- The 17 records, their coordinates and the arithmetic of their rule 5
  figures are `frame/design.md` *Data & interfaces*.

**What breaks in six months.** A rewrite that makes the agent take twice
the calls for the same outcome passes rule 5 and every other rule. The
record shows the doubling in its `tool calls` and `spend USD` rows, which
judge nothing. Today's rule passes the same side, so this work does not
open that gap, and it stays open. The margin adds the second scenario: a
rewrite whose total and tokens per call both rose by 6% passes, because at
two runs a case a rise that size is inside the one recorded spread between
two takes of one text.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Either figure within `TOKEN_MARGIN`: a side fails only where its total tokens and its tokens per tool call both rose by more than 7% of the baseline's** | The two scenarios of *What breaks in six months* above | **Chosen.** It holds the call count out of the verdict in both directions (`frame/design.md` *Data & interfaces*, *Why either figure within the margin is enough*). On the 17 records it fails `957-framer-p3` alone, and it passes the three fails the issue and #967's overview attribute to fewer calls or to noise |
| Either figure falls, with no margin (the issue's first candidate) | `967-warden-p4` still fails, at 1.2% more tokens in all and 0.8% more per call, a rise inside the 6.8-point spread. One run's noise decides it, which the issue's question excludes | Rejected for the noise half. The margin is the only difference from the chosen approach |
| A noise margin on tokens per tool call alone (the issue's second candidate) | A side with fewer calls still fails at any margin narrower than its rise per call. At 7%, `967-framer-p4` fails at 9.5% more per call with 0.5% fewer tokens in all, and `957-sealer-p3` fails at 7.6% more per call with 6.9% fewer in all. A margin wide enough to pass both is wider than any recorded spread, and a side that halves its calls still fails it | Rejected. The bias against fewer calls is structural, and a margin sized for noise does not remove it |
| Total tokens alone, the calls judged by rules 1 to 3 (the issue's third candidate) | It fails `957-warden-p2-run-1`, `957-warden-p2`, `957-warden-p3` and `975-sealer-p4`, each a side that made more calls; `957-warden-p3` and `975-sealer-p4` shipped as passes. At a 7% margin it still fails `957-warden-p2-run-1` at 17.8% and `975-sealer-p4` at 13.5% | Rejected. This was rule 5 until the owner's decision of 2026-10-17 replaced it for the warden's 19.3% more calls with four more truths (`frame/design.md` *Grounding*) |
| Replace the structure: retire rule 5, so tokens and calls are written and judge nothing, as spend is, and rule 4 alone judges cost | A rewrite whose instructions make the agent read more at each call, whole files where it read ranges, raises both figures with outcomes flat and passes. In the recorded set, `957-framer-p3`, at 49.7% more tokens in all and 18.9% more per call, would have passed with no line in its verdict | Not taken. The premise that keeps rule 5 is that it catches a rise beyond noise that rule 4 cannot see, because rule 4 reads the preload's bytes and not what the agent reads after it starts. Checked: `957-framer-p3`'s preload fell from 93453 to 89310 bytes, so rule 4 passed it, and its recorded verdict names rule 5 alone (read). Its rise per call is 2.7 times the margin |
| Spend as the statistic | Spend moves with the model and its price and with output tokens. `957-sealer-p3` spent 34.5% more while reading 6.9% fewer tokens in all | Rejected. The owner's decision judges tokens, and spend stays written and judging nothing |
| Two margins, one for the total and one for tokens per call | Two constants sized from one measured spread, the second with no recorded measurement at all (`questions.md` Q3) | Rejected. One constant, applied to both figures, until a paid pair measures the total's spread |
| Write the re-read as new records, `evals/<issue>-<name>.md` in this work item, as #966 did | Each new record copies numbers already committed, and its verdict line goes stale at the next rule change, while `check` recomputes any record's verdict from the record itself | Rejected. The verdicts go into phase 2's record as a table, each row naming the record's coordinate |
| Rewrite the earlier records' verdict lines in place | Each work item's phase records would then quote verdicts their phases were never judged by | Rejected, on #966's grounds (`frame/design.md` *Grounding*) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **Rule 5 reads the total and the figure per call, with `TOKEN_MARGIN`.** Before the first edit: each of the 17 records extracted with `git show` into a directory outside the tree, `noninferiority.py check` run on each at the base, and each verdict and rule 5 line kept in `trail/phases/phase-1.md` under *What this phase found*. Then the cases of `frame/design.md` *Data & interfaces*, each seen red as its scenario row says; `TOKEN_MARGIN = 0.07` and rule 5 rewritten in `#verdict` with the new reason line; the module, `#tool_calls`, `#verdict` and `#cost_rows` docstrings and `evals/README.md` item 5 and the sentence after the list rewritten in place | `bin/test tests/evals/test_noninferiority.py -q` exit 0, read directly; each case seen red as its scenario row says, and how is written in the phase record; `git grep -n -i -e "tool call below" -e "total tokens, tokens per true find" -e "tool call are fewer" -- evals tests` printing nothing, where at the base it prints five lines (executed), its output quoted in the phase record | c6e47cfe |
| 2 | **The re-read, and the fragment.** `noninferiority.py check` on each of the 17 records at phase 1's commit; `trail/phases/phase-2.md` holding the table `frame/design.md` *Data & interfaces* describes, with phase 1's base column beside it; `changelog.md` written from both phases | 17 `check` runs, each exit code read directly: 0 for `pass` and 1 for `fail`. The rule 5 verdicts and the three verdicts turning to `pass` match S9's prediction, or the divergence is a row of `gaps.md` | |

## Operational impact

- **Every later `compare` judges rule 5 the new way.** No record's shape
  changes, so every committed record still parses.
- **`check` on an older record can now disagree with the verdict it
  states.** On `967-framer-p4`, `967-warden-p4` and `943-sealer-p3b`, S9
  predicts "it says `fail` and its numbers give `pass`". Nothing in the
  tree runs `check` over committed records, so only a reader running it by
  hand meets this, and phase 2's table is where the disagreement is
  explained.
- **The failure direction.** Rule 5 now allows more. A wrong pass ships a
  rewrite whose tokens rose by up to 7% on both figures. A wrong fail costs
  an owner's decision or a paid re-run, which #985's Q1 priced at about 42
  USD for one warden side. At two runs a case the second is the dearer
  mistake.
- **The prompt budget.** The change puts no question in front of anyone.
  It removes the owner's case-by-case answer for a fail on rule 5 alone
  whose rise is inside the margin.
- No migration, no environment variable and no dependency.
