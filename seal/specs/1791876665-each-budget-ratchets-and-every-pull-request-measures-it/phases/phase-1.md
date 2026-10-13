# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | d2ff259e |
| Ran by | smith on Opus 5.5, as `routing.md`'s models line gives it |

## What this phase was asked

Take one budget end to end and stop before phase 2: `seal/budgets.md` with the
`preload:warden` row; `.github/scripts/budget_check.py` (measure, two-sided
compare, ratchet against `--baseline`, the `Budget raised:` body line, exit
codes 0/1/2, summary); the `hygiene.yml` step; `tests/test_a_budget_ratchets.py`
with T1–T7, T12, T13, T16; the `docs/the-record-layout.md` §*seal/* row.
Re-measure the starting value with the checker at this phase's own SHA and use
that value, not the frame's. Record before and after numbers and the probe
results here: +1,000 B to `agents/warden.md` → exit 1, −3,000 B → exit 1
asking to lower, a raise with and without the line. Say first whether the
frame holds against the tree. Do not push: the plan's last verification, the
hygiene step green on the branch's pull request, is owed at the push. Note for
later phases what #929's and #931's frames say back to this one.

## What this phase found

**Whether the frame holds.** Read against the tree at dd00bc84 before the
first edit.

- Holds: `payload_meter.py`'s `agents_in` and `composition` give the agent
  share without the `CLAUDE.md` pair; `hooks/config.py#gfm_table` reads a
  `seal/` table by its header; `unverified_check.py#merge_base` resolves the
  base; `hygiene.yml` carries `PR_BODY` through `env:` and reads only.
- Does not hold, and built around here rather than sent back:
  1. **The broad gate's partition.** `tests/test_the_gate_names_every_step_ci_runs.py`
     refuses a `release` step no `PARTITION` row classifies, and pins the
     counts the gate prints over this repository's workflow. The plan named
     neither. The step is excluded with its reason, the feature count moves
     from 9/4 to 10/5 and the release count from 11/8 to 12/9, and the two
     count cases keep their names because released ledger rows cite them.
     `skills/verify/SKILL.md`'s sentence quoting the feature count moved with
     its pin, and the two released rows quoting the old counts (`Corrected ·
     N10`, `Corrected · P2` of 0.20.0) are corrected in the fragment.
  2. **The body is read once per event.** `hygiene.yml` listed no `edited`
     type, and a re-run replays the first event's body, so the line S3 asks
     for would be read only at the next push. `edited` is added.
  3. **A `CONTRIBUTING.md` sentence** said two always-on steps can refuse a
     contribution; the budget step is a third. Rewritten in place now, since
     the step lands now.
  4. **The plan's case names** were written without `test_`, and
     `evidence-check`'s records arm refused all sixteen at exit 2 — the
     lenient reading, which CI's ledger job runs. Corrected in `plan.md`'s
     test-rows table to the names the tree carries, the later phases' five
     marked as not yet planted.
  Each is a row of `overview.md` §*Where spec and implementation diverged*.

**The number, before and after.** `preload:warden` measured 102,229 bytes at
dd00bc84 by `payload_meter.py --json` (agents/warden.md 33,258,
agent-contract 20,426, code-review 27,535, writing-style 21,010), the frame's
number, and 102,229 by `budget_check.py` itself at 5343c159 and again at
d2ff259e. This phase touched none of the four files, so before and after are
the same, and the row's ceiling is the measurement: headroom 0 and a band top
of 104,273. So every pull request that grows one of those four files needs the
ceiling and the line in the same pull request — #929 and #931 included, when
they rebase onto this. `questions.md` Q5 stays at the frame's 2 %: nothing
here measured noise, because the number is deterministic from the tree.

**The probes** (`executed`, a scratch clone of d2ff259e with the checker of
d2ff259e run from this worktree, `--root` on the clone; the clone was removed
after; the same exits at 83895d9a, before the summary marked an undeclared
raise):

| Probe | Exit | What it said |
|---|---|---|
| the tree as committed | 0 | `preload:warden` 102,229 against 102,229, holds |
| +1,000 B to `agents/warden.md` (S1) | 1 | measured 103,229 bytes is over the ceiling 102,229 by 1,000 |
| −3,000 B from `agents/warden.md` (S4) | 1 | ceiling 102,229 sits above the band: 99,229 at 2 % allows at most 101,213; lower it to 99229 |
| ceiling raised 102229 → 104000, body empty (S2) | 1 | names the row and the line to write, `Budget raised: preload:warden 102229 -> 104000: <reason>`; the summary marks the raise not declared |
| the same raise, body carrying that line (S3) | 0 | the summary lists the raise with its reason |
| the same raise against `--base-ref main` (S6) | 0 | the summary says the raise was read at a release |

**Every case seen red** (`executed`, each through `bin/mutation-check` on a
committed tree, the file restored from held bytes; 35 mutations, every one
`red`). T1: the compare off by one. T2: `>` as `>=` on each edge. T3: the
lower band removed. T4: the baseline read dropped, the line matched by any
mention of the name, the numbers not compared, the list marker and the
backticks not read, the undeclared raise left out of the summary. T5: a
missing row read as new, a gate made a report read as unchanged, the
undeclared removal left out of the summary. T6: the whole check skipped at
`main`, and the release flag ignored. T7: a new row read as a raise from 0.
T12: the summary to stdout with the step file set, and a path in it. The
report row failing the run. T16: each refusal skipped or read empty — the row
refusals, the missing file, the walker's refusal, a comma ceiling, a slack in
words or in another unit, an unknown kind, a duplicate, a unit mismatch, a
family with no subject, an unset body variable, an unresolvable baseline — and
the missing sibling module. The partition row renamed away turned
`test_every_step_the_workflow_runs_is_classified` red. The two count cases
were red at the commit that added the step, before their numbers moved.
T13 has no mutation by design (`plan.md`'s row).

**Design settled while building.** The checker loads its three readers from
its own repository, never from `--root`, so a fixture tree needs no copy of
them. A missing file an agent names is exit 2, because a measurement that
counts it as 0 bytes would read as a cleanup. The summary goes to the step
file alone where the runner sets one; what failed goes to stdout either way.

**Owed at the push.** The plan's last verification: the `hygiene` run on the
branch's pull request, with the new step green at the pushed tip. Nothing
here can run it.

**For the later phases.** From `handoff.md`, as the orchestrator relayed them:

- #929's frame, Q2: the two-sided band on the `ci-minutes:*` rows fails quiet
  runs — 3 of 5 recent pull request runs fall under it on one leg (Windows
  35.6 < 36.9, ubuntu 8.8 < 9.4, macOS 19.9 < 20.0). The owner approved the
  default: per-run rows are one-sided. Phase 3 builds them so, and the lower
  band stays for the tree budgets.
- #929's Q3: `suite-seconds` and the slow-file rows read the committed
  `.test_durations`, so growth is caught at the refresh rather than at the
  pull request that caused it; #931's frame narrows the gap.
- #931's Q4: this item's `budgets` job and #931's `durations` job both land
  in `test.yml`; #931's default is two separate jobs.
- #931's alternative J: its stale-share constant stays a test constant beside
  this file's rows, because a two-sided ratchet cannot hold a measurement
  that drops to 0 at every refresh.
