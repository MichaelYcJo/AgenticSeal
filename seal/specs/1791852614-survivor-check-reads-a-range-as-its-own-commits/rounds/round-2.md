# 1791852614-survivor-check-reads-a-range-as-its-own-commits — review round 2

| Field | Value |
|---|---|
| Target SHA | 9758b7547770488b7cb0e540bed029a5c9233c1e |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #919 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #873, the verifying round, target 9758b754: the diff of round 1's fixes, `b6b89e8c..d3a8221f`. The reviewer was asked whether 🟡 1 and 🟡 2, recorded fixed at 7f08b48f, are closed; to treat `not_owned` and the three new cases as a finding surface; to judge `report`'s contract change; and to reach the two places the smith left unreached — `not_owned`'s own refusal and the truncation past eight commits.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — a two-dot range now names the commits it lists and does not own | `skills/code-review/scripts/survivor_check.py:550` | confirmed | executed: both not-read cases fail against the sweep at `b6b89e8c` (0 removed, no line) and pass at the target |
| 🟢 | round 1's finding 2 is closed — a timeout inside `own_commits` is a refusal at exit 2 | `skills/code-review/scripts/survivor_check.py:543` | confirmed | executed: the stub case fails against `b6b89e8c` with the `TimeoutExpired` traceback and passes at the target; read: `own_commits` is the sweep's one call through a timed git, `is_ancestor` and `unverified_check.py` set none |
| 🟢 | `not_owned` lists what the range holds beyond `owned`, and refuses where `rev-list` fails | `skills/code-review/scripts/survivor_check.py:550` | confirmed | executed: 10 merged base commits over `f1..f2`, exit 0, 10 named, `f2` not named; `rev-list` failing is exit 2 with its sentence |
| 🟢 | the not-read line shows 8 commits and an ellipsis past 8 | `skills/code-review/scripts/survivor_check.py:2347` | confirmed | executed: 8 shown and ` …` then the full stop; cosmetic, commissions nothing |
| 🟢 | the three new cases and the three-dot assertion | `tests/test_the_sweep_reads_a_range_as_its_own_commits.py:277` | confirmed | executed: the three fail against `b6b89e8c`'s sweep and pass at the target; the three-dot case passes on both, as an old sweep prints no line for any spelling |
| ⬜ 4 | the changelog fragment says the run no longer reports a clean range, and it still does, now with a line naming what it left out | `seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/changelog.md:24` | answered | corrected at 79bda2f3 — the changelog fragment says the run still reports what it read, no longer in silence, and names the commits it left out; read: exit 0, 0 removed and *no removed wording is still standing* after the line; the module docstring and `not_owned` say *in silence*; a correction, outside `Needs a fix` |

## Paste-ready fixes

no paste-ready fix in the report

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
| round-1 | `skills/code-review/scripts/survivor_check.py:526` | round 1's 🟡 1 — fixed |
| round-1 | `skills/code-review/scripts/survivor_check.py:537` | round 1's 🟡 2 — fixed |
| round-1 | `skills/code-review/scripts/survivor_check.py:1385` | round 1's ⬜ 3 — answered |
| round-1 | `skills/code-review/scripts/survivor_check.py:460` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_the_sweep_reads_a_range_as_its_own_commits.py:197` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md:10` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/survivor_check.py:474` | round 1's 🟢 — confirmed |
| round-1 | `docs/the-record-layout.md:168` | round 1's 🟢 — confirmed |
| round-1 | `skills/evidence-check/scripts/correction_check.py:736` | round 1's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| on a two-dot range, an own commit's correction is not measured where the two ends show no net loss at that path | #921, already deferred in round 1 | the owner, through #921 |
