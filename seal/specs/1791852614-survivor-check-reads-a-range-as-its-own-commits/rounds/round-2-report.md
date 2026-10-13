# 1791852614 — round 2 report (warden)

The verifying round. Target SHA `9758b754`, base `origin/release/v0.21.1`
(`321e9de1`), and the target of this round is the diff of the fixes,
`b6b89e8c..d3a8221f`, two commits. Read and run in a scratch clone of the
worktree at the target SHA, outside the repository. Nothing was written in
the worktree but this file.

## How the answers relate

```
round 1's two findings, fixed at 7f08b48f
   ├─ 🟡 1  the not-read line          → closed (🟢), seen red without it
   ├─ 🟡 2  the timeout in owned       → closed (🟢), the class has one member
   └─ ⬜ 3  the per-commit re-reads     → carried open, not reported again
the new surface
   ├─ not_owned and its refusal        → correct, refusal executed by a probe
   ├─ the truncation past 8 commits    → correct, executed by a probe
   └─ ⬜ 4  the changelog says the run no longer reports a clean range
```

Nothing this round found needs a fix. The one new note sits in the work
item's own changelog fragment, so it is a correction to the paperwork.

## Round 1's 🟡 1 is closed

**Executed.** `not_owned` (`skills/code-review/scripts/survivor_check.py:550`)
lists what `git rev-list --no-merges a..b` holds beyond the list `owned`
returns, and `report` prints it under the examined line
(`survivor_check.py:2347`). Both lists hold full object names, and
`own_commits` keeps a commit that changed nothing as its header alone, so
an own commit is never named as not read.

I ran the three new cases and the amended three-dot case against the sweep
at `b6b89e8c`, with that one file checked out in the clone. The two not-read
cases failed, each on a report reading *0 sentence(s)* with no line. The
three-dot case passed, which is expected, because the old sweep printed no
such line for any spelling. At the target all four pass.

The reading itself is unchanged. `base..feature` after a merge of the base
still exits 0 with 0 removed. That is the owner sentence, and round 1's
finding was the silence and not the reading. Topology cannot tell this shape
from S1's, so a failing exit would also fail every fix range across a merge.

## Round 1's 🟡 2 is closed, and the class has one member

**Read, then executed.** `owned` turns `subprocess.TimeoutExpired` into the
refusal its `None` branch already wrote (`survivor_check.py:543`). The class
is a git call with a timeout reached from `main`, which catches `Refused`
alone. I enumerated it:

- `chain_check.py`'s `git` is the only helper with `timeout=60`, and
  `own_commits` is the only unit the sweep calls through it.
- `is_ancestor` (`chain_check.py:1621`) runs `subprocess.run` with no
  timeout, so the call just before `own_commits` cannot raise this.
- `unverified_check.py`, the module `reader()` loads for `tree_at` and
  `folded_items`, sets no timeout.
- The sweep's own `git` sets none.

The stub case failed against `b6b89e8c` with the `TimeoutExpired`
traceback, and it passes at the target. It reaches the `None` branch as
well, which answers the overview's row.

## The new surface

**`not_owned`, executed.** I built ten base commits merged into a branch and
swept the fix range `f1..f2`. The run exits 0. The line names 10 commits,
shows the oldest 8 and then ` …`, and does not name `f2`. Then I replaced the
module's `git` so that `rev-list` alone fails. The run exits 2 with
`cannot list the commits in a..b in ROOT`, never a traceback. Over `f1...f2` no
line is printed. So the two paths the smith left unreached both behave as
written.

One rendering detail: past 8 commits the line reads `… ….` with the full
stop after the ellipsis. It is a cosmetic matter and commissions nothing.

**The three cases, read.** Each builds the history it names. The stub case
puts its stub on a fresh module per loop, and `owned` looks `chain` up
through the module's globals, so the stub is what `main` reaches.

**`report`'s contract change, read.** The new parameter defaults to `()`,
and `main` is the only caller in the tree. Its new `Reads:` line takes it
off the census, and `tests/undeclared_readers.txt` drops it in the same
commit. CI passes `A...B` (`.github/workflows/hygiene.yml:262`), so CI never
prints the line.

**The ledger rows, executed.** `evidence-check --ledger` over the fragment
answers 91 ok, 0 drifted, 0 broken. R1-1 and R1-2 state what the code does.

## ⬜ 4 — the changelog says the run no longer reports a clean range

**Read.** `seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/changelog.md:24`
says `origin/<base>..HEAD` on a branch that merged its base now names what
it left out, *rather than reporting a clean range*. The run still reports a
clean range: exit 0, *0 sentence(s)*, and *no removed wording is still
standing*. What changed is that it no longer does so in silence. A reader of
the release note could take the sentence to mean the run now fails there.
The module docstring and `not_owned` both say *in silence*, and the
changelog dropped those two words. This is a correction to the work item's
paperwork, outside `Needs a fix`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — a two-dot range now names the commits it lists and does not own | `skills/code-review/scripts/survivor_check.py:550` | confirmed | executed: both not-read cases fail against the sweep at `b6b89e8c` (0 removed, no line) and pass at the target |
| 🟢 | round 1's finding 2 is closed — a timeout inside `own_commits` is a refusal at exit 2 | `skills/code-review/scripts/survivor_check.py:543` | confirmed | executed: the stub case fails against `b6b89e8c` with the `TimeoutExpired` traceback and passes at the target; read: `own_commits` is the sweep's one call through a timed git, `is_ancestor` and `unverified_check.py` set none |
| 🟢 | `not_owned` lists what the range holds beyond `owned`, and refuses where `rev-list` fails | `skills/code-review/scripts/survivor_check.py:550` | confirmed | executed: 10 merged base commits over `f1..f2`, exit 0, 10 named, `f2` not named; `rev-list` failing is exit 2 with its sentence |
| 🟢 | the not-read line shows 8 commits and an ellipsis past 8 | `skills/code-review/scripts/survivor_check.py:2347` | confirmed | executed: 8 shown and ` …` then the full stop; cosmetic, commissions nothing |
| 🟢 | the three new cases and the three-dot assertion | `tests/test_the_sweep_reads_a_range_as_its_own_commits.py:277` | confirmed | executed: the three fail against `b6b89e8c`'s sweep and pass at the target; the three-dot case passes on both, as an old sweep prints no line for any spelling |
| ⬜ 4 | the changelog fragment says the run no longer reports a clean range, and it still does, now with a line naming what it left out | `seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/changelog.md:24` | open | read: exit 0, 0 removed and *no removed wording is still standing* after the line; the module docstring and `not_owned` say *in silence*; a correction, outside `Needs a fix` |

## Executed probes

| What was run | Result |
|---|---|
| `SPECSEAL_CASE_CEILING_S=600 bin/test tests/test_the_sweep_reads_a_range_as_its_own_commits.py tests/test_the_range_rule_states_no_shape.py tests/test_the_rules_have_one_owner.py -q` in the clone at `9758b754` | exit 0, 82 passed |
| the same runner, `-p no:xdist`, the three new cases and the three-dot case, with `survivor_check.py` checked out from `b6b89e8c` in the clone and restored after | exit 1: 3 failed, 1 passed; the stub case failed on `TimeoutExpired` |
| a one-off probe script (deleted after the run): ten base commits merged into the branch, swept as `f1..f2` | exit 0; *not read 10 commit(s)*, 8 shown then ` …`; `f2` not named |
| the same script: the module's `git` replaced so that `rev-list` answers None | exit 2, `cannot list the commits in a..b in ROOT` on stderr |
| the same script: the same history swept as `f1...f2` | exit 0, no not-read line |
| `bin/evidence-check --ledger seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md` over the clone | exit 0, 91 ok, 0 drifted, 0 broken |
| the broad gate (full suite, repository-wide lint, typecheck) | not yet; the sealer's, after the rounds settle, and this round did not run it |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round 1, ⬜ 3, open | `skills/code-review/scripts/survivor_check.py#own_changes` | carried, not re-reported: it closes once at the run's end |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| on a two-dot range, an own commit's correction is not measured where the two ends show no net loss at that path | #921, already deferred in round 1 | the owner, through #921 |

Needs a fix: no
Loses a record or crashes: no

The broad gate comes due. Nothing this round found needs a fix, so the
sealer's spawn is what comes next. ⬜ 4 is a correction to the changelog
fragment, and ⬜ 3 stays carried until the run's end.

## Proof block

Opened at `9758b754`, in the scratch clone:
`seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/rounds/round-1.md`
and `rounds/round-1-report.md`; the fix diff `b6b89e8c..d3a8221f` whole
(the ledger fragment, `changelog.md`, `overview.md`,
`skills/code-review/scripts/survivor_check.py`,
`tests/test_the_sweep_reads_a_range_as_its_own_commits.py`,
`tests/undeclared_readers.txt`); in `survivor_check.py`, `git` through
`not_owned`, `reader`, `retired_directories`, `chain`, `report` and `main`;
in `skills/code-review/scripts/chain_check.py`, `git`, `is_ancestor` and
`own_commits`; the head of
`tests/test_the_sweep_reads_a_range_as_its_own_commits.py` (its helpers);
`.github/workflows/hygiene.yml` (the sweep step); `bin/test`;
`bin/evidence-check`; two other work items' `overview.md` for the ✅
convention. Not opened: `spec.md`, `plan.md`, `phases/`, and the ledger
rows outside the diff.
