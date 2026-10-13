# 1791852613-the-test-durations-are-refreshed-and-say-when-next — questions for the planner

<!-- seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

Framed by `framer` on Fable 5.1, 2026-10-13, under `routing.md`'s
`automation`. No row blocks the build: the two a person owns (Q1, Q5) are
decided here with their grounds, for the owner to overturn at the plan's
approval; two are measurements CI runs give; one is the work's.

## Judgments the issue left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `spec.md` or in
`plan.md`'s Alternatives table.

| Judgment | Answer | Where the grounds are |
|---|---|---|
| Who dispatches the measuring run | The orchestrating session, not the owner and not the smith: `automation` was pressed, and `agent-contract` §6 withholds pushing from every agent. The smith hands back at each push | `plan.md` §*Technical context*, first paragraph |
| Whether a separate measuring branch is needed | No. A push of this branch runs nothing while no pull request is open, and `workflow_dispatch` runs the tip; the measuring commit is reverted by the next commit and the squash removes it | `plan.md` Alternatives J |
| How the file is measured | By `CONTRIBUTING.md`'s recipe as written, on the Windows leg, as one job with `--store-durations`; not on macOS, not locally, not through a new dispatch input | `spec.md` Grounding, Scope 1 and Out; `plan.md` Alternatives E |
| What *when next* is | A check, not a sentence: a suite case that fails when more than one collected case in twenty is unpriced, and a box at release preparation as the planned moment | `plan.md` Alternatives A–D; `spec.md` Scope 2, 3 |
| Where the check reads the collection | From a `conftest.py` hook that runs before `pytest-split`'s `trylast` hook, so a shard sees the whole suite; a partial invocation declines | `plan.md` §*Technical context*, the collection paragraph |
| Whether dead entries count | No. `pytest-split` never reads an entry it did not collect; 838 of them cost bytes and nothing else, and the refresh replaces them | `spec.md` Scope 2 and Out |
| How the budgets are re-set | By the rule beside the values, from the post-refresh run, every leg, a base moving only upward | `spec.md` Scope 4; `plan.md` §*Technical context*, the budgets paragraph |
| Which released rows this work drifts, and where their re-reads go | 0.21.0's S1–S5 and its re-reads of 0.20.0's S1/S2/S8 on `test.yml#"pytest:"`; the quoted `CONTRIBUTING.md` lines of 0.21.0's S5 and 0.20.0's S9; all into this item's fragment | `spec.md` §*Data & interfaces*; `plan.md` §*Technical context*, the ledger paragraph |
| Whether the shard module's existing cases are renamed or edited | No; a function is added beside them, so 0.20.0's S4 and 0.21.0's S1 anchors stand | `spec.md` §*Data & interfaces* |
| Whether the READMEs change | No; neither names the CI legs or the file (`grep`, 2026-10-13) | `spec.md` Out |

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What share of unpriced collected cases makes the file stale enough for the case to fail — `STALE_SHARE`? It is a value a contributor is limited by, so a person is accountable for it | a person — the repository owner, who may overturn the value at the plan's approval | (a) **one in twenty, 0.05**: under the issue's own 3.9 % call would be stricter than the owner's judgment and over it looser; 0.05 is above one cycle's measured growth (4.9 %) so a release that refreshed at preparation stays green through the next cycle, and below today's 9.4 % so the case is red on the real tree before the refresh; (b) **0.03**: fires before a cycle ends even after a refresh at preparation; (c) **0.10**: would have let the file reach where it is today unspoken | (a) | ✅ decided by the frame 2026-10-13 under `automation`: (a), with the grounds in `plan.md` §*The share, and why one in twenty*; the owner may overturn it at approval, and the constant is one line |
| Q2 | What does the measuring run give — the Windows job's time `startedAt` to `completedAt`, its summary line, and the artifact's entry count against `passed` plus `skipped`? | a measurement — the run the session dispatches after phase 1's push; `gh run view <id> --json jobs`, the job's log, `gh run download` | the entry count equals the collected count and the restore commit's unpriced count is zero: phase 2 commits; the job hit its 55-minute budget or the artifact is missing: the hand-back says so and the session re-dispatches with the budget the measured time asks for | none; phase 2 answers it | ✅ answered by phase 2's reading of run 38332345615, 2026-10-13: the Windows job took 37 m 21 s inside its 55 and uploaded the file, which now prices all 13,480 cases as Windows collects them; 213 cases whose ids hold a path separator stay unpriced against the POSIX collection, so the count is 213 and not zero (`phases/phase-2.md`) |
| Q3 | What do the eight jobs of the post-refresh run measure — each shard's time and summary line, the sums against ubuntu's, and the slowest shard's ratio to the mean on each leg? | a measurement — the run the session dispatches after phase 2's push | the slowest Windows shard at or under 12 minutes and every base unchanged: the comment gains the run id and no `timeout` moves; a base moved upward: the rule gives the new value; a sum that is not ubuntu's: a group is missing or doubled, which the shard case should have refused first | none; phase 3 answers it | ⬜ |
| Q4 | Does the `conftest.py` hook see the whole collection on a shard on GitHub, as the `trylast` reading of `pytest-split`'s hook says it must? | the work — phase 3, from the post-refresh run: the suite case green on all seven shards is the answer; locally, phase 1's `uvx` form under `--splits 3` | green on every shard: the reading holds; red on the shards and green on ubuntu: the hook ran after the split, and the phase moves it to `tryfirst` with the reason in its docstring and one more run | the default-order hook, by the wheel's source | ⬜ |
| Q5 | Does `docs/release-checklist.md` §0 gain the box that makes the refresh a planned act at every release's preparation, by the recipe, from the release branch? It is one box in a `docs/` file, which is policy | a person — the repository owner, at the plan's approval | (a) **the box**: the file prices every case of the release at the one moment it can, and the case is the backstop; (b) **no box**: the case alone schedules the refresh, which then lands mid-cycle on whichever pull request crosses the share, every cycle, since one cycle's growth is about the share | (a) | ✅ decided by the frame 2026-10-13 under `automation`: (a), with the grounds in `plan.md` §*The planned refresh at release preparation*; the owner may overturn it at approval |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** The `Status`
column is ticked by whoever answered, never by whoever asked. Q1 and Q5 are
ticked by the frame because `automation` was pressed and nobody is asked
mid-run; the tick records a default built on, not an answer a person gave,
and the approval line of `plan.md` is where a person's name reaches it.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
