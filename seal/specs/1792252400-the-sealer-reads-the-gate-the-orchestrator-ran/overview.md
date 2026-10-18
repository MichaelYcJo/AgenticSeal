# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — overview

<!-- The closing memo (implement skill, step 4). Opened at phase 1's divergence
and closed by phase 7. Only what the diff cannot show goes here. -->

## Why this work exists

The broad gate becomes the orchestrator's one command before the sealer is
spawned, so the sealer reads the record that run wrote, no longer runs it a
second time, and writes its verdict as `sealed`, `withheld` or `undecided`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which commit the sealer cases' `broad-gate.md` names (phase 1) | `plan.md` row 1: "naming `$build against $(git rev-parse main)` … so the run's SHA is followed by one records-only commit". `$build` is followed by two. The scaffold names the commit the records were written at, which one commit follows: the record's own | the stated property: one records-only commit | the row contradicts itself, and the property is the one `spec.md` §*The act, as this item leaves it* orders: the gate runs once the pull request body and `changelog.md` are written. Either reading passes `chain_check.broad_gate` (`phases/phase-1.md`) |
| T7 and `noninferiority.py model` (phase 3) | `plan.md` row 3 closes with phase 3's commit, and row 4 runs `model` "built in phase 3's commit". Phase 3 first closed at 394ed499 (de849341) without T7, which was in neither of its two spawns | built afterwards by a later spawn, test-first, at 1459b26f; phase 3 re-closed there (ed486efd) | phase 4 cannot decide the model without it, and T7 was seen red against de849341 before the build (`phases/phase-3.md`) |
| Contract §2's `Enforced by:` line (phase 3) | `plan.md` row 3 is verified by `bin/rules --check` exit 0. 394ed499 renamed the case §2 named, so the check exited 1 on one of 464 targets from 394ed499 to 1459b26f | the orchestrator repointed the line at 5ca68b5d, and phase 4's Opus side ran at 5ca68b5d rather than at phase 3's commit | phase 4's side then reads the contract as it stands; the row's exit 0 did not hold at 394ed499, and the phase record says so (`phases/phase-3.md`) |
| The sealed case's name (phase 5) | `plan.md` row 5 regenerates the four cases; row 6 reads each grader's passed count against phase 4's | `rule-sealer-sound` renamed `rule-sealer-sealed`, with its directory, work item and branch; phase 6's table maps the two by hand | the case's slug names the verdict, and its six graders are unchanged but for the verdict regex (`phases/phase-5.md`, `phases/phase-6.md`) |
| The class grep for the old words (phase 5) | `plan.md` row 5: `git grep -n -E "\bsound\b\|not sound\|undecidable"` | `git grep -n -w` over `sound` and `undecidable` in every case, the plan's form reported beside it | in `git grep -E`, `\b` did not match a word boundary: the plan's form missed `SOUND = "sound"` in `chain_check.py` (`phases/phase-5.md`) |
| Edits outside row 5's list (phase 5) | `plan.md` row 5 names no `docs/the-broad-gate.md` or `docs/the-review-and-parity-arms.md` line and no `chain_check.py` refusal message | three pre-existing long lines rewrapped without a word changed (`agents/sealer.md:95`, `docs/the-broad-gate.md:123`, `docs/the-review-and-parity-arms.md:108`); the missing-guarantee message says the orchestrator's broad run (53d5c471); `docs/the-review-and-parity-arms.md:100` names the orchestrator | `tests/test_docs_line_wrap.py` was red at phase 4's tree on those three lines; the two owner sentences are the class phase 3's grep missed (contract §12) |
| The reference side's revision (phase 6) | `plan.md` row 6: `run --rev <phase 5> --suite-rev <phase 5>` | `--rev b394e929 --suite-rev b394e929`, the commit after phase 5's close that gives T7's two record reads `encoding="utf-8"` | phase 5 left that pre-existing failure to the orchestrator before any broad run; `git diff --stat 284b3597 b394e929 -- evals/behaviour` is empty, so the suite is phase 5's; after round 1 added `rule-sealer-stale-gate` the reference was re-run at `--rev 90fa7046 --suite-rev 90fa7046` and replaces it (`phases/phase-6.md`) |
| `skills/verify/SKILL.md` §*Every agent seals what it verified* | `plan.md` row 3 lists `skills/verify/SKILL.md`; the section still says "The sealer's is the only one drawn" while the orchestrator's run draws it | left to #967; the sites row 3 named at 397-404, 428 and 947 were rewritten | `questions.md` Q7 names that section as #967's, and the word `seal` is held by `tests/test_one_word_one_meaning.py`; phase 5 found none of the old verdict words there (`phases/phase-3.md`, `phases/phase-5.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| closed The four regenerated sealer cases have not run on a model: no grader of `rule-sealer-no-gate` and no `shape-runs-no-broad-gate` has read a trace | the orchestrator's sides: the baseline at 2fc33333 (9184881a) read both, 0 of 2 and 0 of 8; phase 4 at 5ca68b5d (d27f7994) and the reference at b394e929 (cb1940e3) passed every grader, 54 of 54, and the five-case reference at 90fa7046 68 of 68 (`phases/phase-2.md`, `phases/phase-4.md`, `phases/phase-6.md`) |
| The full suite, the repository-wide lint and the typecheck at the last round's commit | the orchestrator, by `broad-gate --base release/v0.22.1 --record 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran` after the review rounds settle; not yet run |
| CI on its three legs at the pull request's head | the orchestrator, at the pull request |

## Not done

| Item | Who must answer |
|---|---|
| `skills/verify/SKILL.md` §*Every agent seals what it verified* calls the drawn stamp the sealer's | #967, which owns that section (`questions.md` Q7) |
| The warden, the smith and the framer are not measured again for contract §2's change | the owner, `questions.md` Q1; the default, not here, is built |
| Round 1's fix changes one sentence of `agents/warden.md` (what comes due is the orchestrator's broad run, then the sealer's spawn), so the warden's read set moved after its last measured side; nothing is measured here | the milestone close, which re-judges the warden's side |

## Fed back into the spec

none — the answered questions are measurements and sorting work (Q3 to Q7);
none of them states a rule a `docs/` policy would carry.
