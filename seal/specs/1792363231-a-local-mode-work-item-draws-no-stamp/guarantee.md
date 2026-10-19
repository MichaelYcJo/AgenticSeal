# 1792363231-a-local-mode-work-item-draws-no-stamp — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 81359f18 against 8db076f8; earlier run: fde537cc withheld |
| Broad gate | 4415c5db against 8db076f8 |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD: only paths under this item's directory follow it | `broad-gate.md:5` (`4415c5db against 8db076f8`) | `git log --no-merges --name-only 4415c5db..HEAD ^8db076f8` at 81359f18 | holds — two commits follow, fde537cc (`broad-gate.md`, `overview.md`) and 81359f18 (`guarantee.md`, `spec.md`), all under this item's directory (executed). The base resolved through `@{upstream}` to 8db076f8 again (executed) |
| Nothing but this item's records changed since the earlier run | the orchestrator's message; the earlier run's `Target SHA` fde537cc | `git diff --stat fde537cc 81359f18` | holds — this item's `guarantee.md` and `spec.md` alone (executed). So every row below whose coordinates are code, tests or other records is carried from the earlier run, whose commands it names |
| S1's case was red before the local writer existed | `spec.md:157` | carried: a scratch clone at fde537cc with the code restored from 8db076f8, `-k test_a_local_mode_sealed_guarantee_queues_one_stamp` | holds — both givens failed, no `queue_for_local_guarantee` (executed in the earlier run; coordinates untouched since) |
| The edit gate's case was red before the gate existed | `phases/phase-2.md`, `plan.md:268` | carried: the same at-base clone, `-k test_the_edit_gate_queues_a_local_mode_sealed_guarantee` | holds — `[Write]` and `[Edit]` failed (executed in the earlier run) |
| S11's refusal at the commit was red before the change | `phases/phase-6.md`, `phases/phase-7.md` | carried: the same at-base clone, `-k test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit` | holds — both givens failed (executed in the earlier run) |
| The refusal through the installed stubs: four refused shapes red, the fifth a quiet one | `phases/phase-6.md` §*Q6*; the pull request body's "five shapes" | carried: the same at-base clone, `-k test_a_sealed_the_branch_does_not_hold_is_stopped_inside_the_commit` | holds — four failed with the commit landing; `a pathspec that leaves it out` passed (executed in the earlier run) |
| The `--no-verify` limit, round 2 finding 1's shape and the local refused-then-resealed case were red before phase 7 | `phases/phase-7.md` seen-red table | carried: the scratch clone with the code restored from 1e956838, the three cases by name | holds — all three failed on the assertion the record names (executed in the earlier run) |
| S11's second case holds only through `sealed_before` | `phases/phase-7.md` | carried: `sealed_before` made to return `False`, `-k test_a_refused_row_over_a_drawn_seal_does_not_draw_again` | holds — failed, a stamp queued (executed in the earlier run) |
| Every sampled case passes at HEAD's code | the phase records' narrow runs | carried: the fifteen node ids at fde537cc, whose code and tests 81359f18 leaves unchanged | holds — 15 passed, exit 0 (executed in the earlier run) |
| The broad run at 59732199 failed on the census module, and 20ea0280 fixed it | `overview.md:26`; `rounds/round-6.md` | carried: the census module at fde537cc and with 59732199's test file | holds — 17 passed; 2 failed naming the stub case (executed in the earlier run) |
| S10: #975's fourteen once-reader cases are unchanged node for node | `spec.md:166`; the pull request body's line 34 | carried: an `ast.dump` comparison against 769f2aa4 | holds — 14 of 14 the same (executed in the earlier run) |
| S10: `hooks/git/` changes in `pre-commit.py`'s docstring alone, and `sealed_before` reads as at 769f2aa4 | `spec.md:166`; the pull request body's line 34 and its "back to its 0.22.1 shape" | carried: `git diff 769f2aa4 HEAD -- hooks/git/ skills/verify/scripts/seal_stamp.py` | holds — docstrings alone (executed, read, in the earlier run) |
| S9: the sealer's definition lost one word, and nothing after 11b90191 | `spec.md:165` | carried: `git diff --stat 11b90191 HEAD -- agents/` | holds — empty (executed in the earlier run) |
| Removes: every row of `spec.md` §*Removes* | `spec.md:279-291` | carried: the `git grep` runs the earlier run named, over code and documents 81359f18 does not touch | holds — nothing of any row stands (executed in the earlier run) |
| The spec's §*Scope* no longer promises the mark grammar | `spec.md:75-79` at 81359f18; the earlier run's `withheld` | `git diff fde537cc 81359f18 -- <item>/spec.md`; `git grep -n -E "REFRAME_RE\|after phase\|mark's grammar"` over this item's `spec.md` and `overview.md`; `sed -n 309,315p spec.md` | holds — the bullet now says the grammar is not widened and why; no other sentence of the spec promises it; the foot carries `after round 2.` alone, and `overview.md:16` records the correction with no mark line, as the bullet says (executed) |
| The pull request body's lines the earlier run named are corrected | `976-pr.md:33`, `:36`, `:38` | read the whole file again | holds for `:36` (six rounds, round 6 on the fix to the census case) and `:38` (the reflog subjects gone, the Windows comparison kept for CI's Windows leg) (read). `:33` is the next row |
| The body's mutation row: "every unit caught except six survivors … two equivalent mutants in the local writer" | `976-pr.md:33`, against `phases/phase-1.md:56-71` and `phases/phase-6.md:148-172` | read those phase records | does not hold — `phases/phase-1.md:61` says of its survivors that "each has an input that only it would change", so the two in the local writer (`not found`, `not branch`) are not equivalent mutants; and not every new unit was mutated: `phases/phase-1.md:68-69` (`not home` "was not run") and `phases/phase-6.md:171-172` (the memoised listing and the arms-first order "were not mutated") (read). The earlier run read only this row's count and missed both |
| The sealer's measurement passed | `evals/sealer-phase-5.md`; the pull request body's line 26 | carried: read, not re-run | holds as read — `Verdict: pass`, 35992.6 → 35600.6 tokens per tool call, 3.5731 → 3.3379 USD (read) |
| The latency figures, 260 → 268 ms and 283 → 310 ms | `phases/phase-6.md` §*Q7*; `changelog.md:51-53`; the pull request body's line 22 | not re-run | unverified — a timing on the smith's machine; the figures in the fragment and the body match the phase record (read). Nobody answers further: it is a report, not a gate |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The issue body (#976 and its comment) | A trigger for a local-mode work item that draws the stamp once, from the sealer's `sealed`, never from the broad gate's run; and #975's Q7 gap, a `sealed` over a commit the branch does not hold after which the item draws no stamp | the build, the changelog, the spec, the pull request body | none |
| The spec | S1–S14 and `## Removes` as the issue asks; §*Scope* now states the mark's grammar is not widened, per `plan.md:10` | the issue; the build in every sampled scenario and every `## Removes` row; `plan.md:10`, `phases/phase-8.md` and `overview.md:16` on the grammar | none |
| The build (the diff, phases 1–8, the fix commits through 20ea0280) | The local writer and its `post-edit` gate; the refusal at `pre-commit` that records what it refused; `post-commit`'s record and guards gone; `sealed_before` back to 769f2aa4; the words rewritten; the grammar left alone | the issue; the spec; every sampled `seen red` and `executed` claim; rounds 1–6; the changelog | none |
| The last round (round 6 at 20ea0280) | No finding; the census fix keeps the strength of the check it replaced | the census module run both ways; rounds 4 and 5 closed; the broad run at 4415c5db after it | none |
| The changelog fragment | Two `Fixed` entries: the local-mode trigger with the sealer's measurement, and the refusal at the commit with its record, its four stated limits and its latency | the code, `docs/the-review-record.md` §*The stamp*, `evals/sealer-phase-5.md`, `phases/phase-6.md` | none |
| The pull request body (`976-pr.md`, not yet posted) | The two gaps and their fixes, the redesign's reason, the before-and-after table, the limits, the measurement, and how it was verified | the code, the changelog, the issue, the six round records, and every row of its verification table but one | line 33, the mutation row: it calls the local writer's two survivors "equivalent mutants" where `phases/phase-1.md:61` says each has an input that would kill it, and says every new unit was caught where `phases/phase-1.md:68-69` and `phases/phase-6.md:171-172` name units never mutated |

Verdict: withheld — the pull request body's line 33 (`976-pr.md:33`) is untrue in two clauses: "two equivalent mutants in the local writer" contradicts `phases/phase-1.md:61`, which says each surviving mutant "has an input that only it would change" (a working directory equal to the common dir for `not found`, a branch named `None` for `not branch`), and "every unit caught except six survivors" under "`mutation-check` on each new unit" contradicts `phases/phase-1.md:68-69` (`not home` was not run) and `phases/phase-6.md:171-172` (the memoised listing and the arms-first order were not mutated); every other line, and the spec's corrected §*Scope*, holds
