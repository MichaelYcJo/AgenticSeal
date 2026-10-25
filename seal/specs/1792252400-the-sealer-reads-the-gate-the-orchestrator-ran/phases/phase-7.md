# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | the commit that adds this record, `overview.md`, `changelog.md` and the `questions.md` answers |

## What this phase was asked

The close, at no spend. `overview.md`: the purpose, each divergence from the
plan with its grounds, `## Not verified` closed with the word `closed` or
left open with its answerer, the fed-back clauses. `changelog.md` completed
to S15, keeping phase 5's in-flight paragraph, with the sealer's row of
#957's per-agent table at 2fc33333 and at the close, each figure read from
`evals/*.json` with `noninferiority.py#side_numbers`. `questions.md`: rows
the work answered marked so, Q1 and Q2 left open on their built defaults.

## What this phase found

**The four sides read the same through `side_numbers` as their phase records
say.** A scratch script imported `noninferiority.py` and printed each side's
figures; every one below matches phases 2, 4 and 6 to the digits those
records carry. The traces:

| Figure in `changelog.md` | Value | Record | Committed at | `side_numbers` field |
|---|---|---|---|---|
| Preload bytes at 2fc33333 | 24,652 | `evals/baseline-sealer.json` | 9184881a | `bytes` |
| Preload bytes at 5ca68b5d | 23,792 | `evals/sealer-phase-4.json` | d27f7994 | `bytes` |
| Preload bytes at b394e929 | 23,825 | `evals/reference-sealer.json` | cb1940e3 | `bytes` |
| Tokens per tool call at 2fc33333 | 35,490.9 (3,549,090 / 100) | `evals/baseline-sealer.json` | 9184881a | `tokens` / `calls` |
| Tokens per tool call at 5ca68b5d | 33,386.8 (2,303,686 / 69) | `evals/sealer-phase-4.json` | d27f7994 | `tokens` / `calls` |
| Tokens per tool call at b394e929 | 34,849.8 (2,648,585 / 76) | `evals/reference-sealer.json` | cb1940e3 | `tokens` / `calls` |
| Spend USD at 2fc33333 | 3.1901 (3.1900638) | `evals/baseline-sealer.json` | 9184881a | `spend` |
| Spend USD at 5ca68b5d | 2.8036 (2.8036474) | `evals/sealer-phase-4.json` | d27f7994 | `spend` |
| Spend USD at b394e929 | 2.9882 (2.9882399) | `evals/reference-sealer.json` | cb1940e3 | `spend` |
| Spend USD, the Sonnet copy | 1.4076 (1.4075849) | `evals/sealer-sonnet-phase-4.json` | d27f7994 | `spend` |
| Graders passed at 2fc33333 | 39 of 54 | `evals/baseline-sealer.json` | 9184881a | `graders`, summed |
| Graders passed at 5ca68b5d | 54 of 54 | `evals/sealer-phase-4.json` | d27f7994 | `graders`, summed |
| Graders passed at b394e929 | 54 of 54 | `evals/reference-sealer.json` | cb1940e3 | `graders`, summed |
| Graders passed, the Sonnet copy | 53 of 54 | `evals/sealer-sonnet-phase-4.json` | d27f7994 | `graders`, summed |
| Runs, cut short | 8 each, none | all four | as above | `runs`, `cut` |
| Verdict 2fc33333 → 5ca68b5d | pass | `evals/sealer-phase-4.md`, line 71 | d27f7994 | — |
| Suite of the step-A sides | c2544c8f | the three step-A records | as above | `suite` |
| Suite of the reference | b394e929 | `evals/reference-sealer.json` | cb1940e3 | `suite` |

The item's spend is the four `spend` figures summed: 10.3895 USD
(10.389536), which `questions.md` Q5 now reads.

**The close's row has no verdict, by design.** The reference side ran the
renamed suite, so `compare` is never asked across it (S10). The changelog
table gives it its own row with `none` in the verdict cell rather than an
arrow from 2fc33333, which ran a different suite.

**Nothing has merged into the base since the branch was cut.** `git fetch
origin release/v0.22.1` left it at 2fc33333, the merge base, so none of
#967, #968 and #970 has landed in it. No rebase happened, and phase 3's
class grep stands as measured (Q7).

**Two overview rows were already done and leave `## Not done`.** T7 was built
at 1459b26f, so it is a divergence row now. *The sealer's two files*
was renamed by phase 5: `git grep -E "SEALERS_FILES|sealer's two files"`
outside `seal/specs/` and `changelog/` finds nothing. One site stays
standing. `skills/verify/SKILL.md:253` still says "The sealer's is the only
one drawn", and it goes to #967.

**What the check at the pull request still owes is the orchestrator's.**
`chain_check.py` names three things: no `rounds/round-N.md`, no
`broad-gate.md` and no `guarantee.md`. The review chain writes the first,
the orchestrator's broad run the second, and the sealer the third. None of
them is this phase's.

## Commands

`$W` is the worktree, `$S` this phase's scratch directory.

| Command | Exit |
|---|---|
| `python3 $S/figures.py` (`side_numbers` over the four sides) | 0 |
| `git -C $W fetch origin release/v0.22.1`; `git rev-parse FETCH_HEAD origin/release/v0.22.1` | 0; both 2fc33333 |
| `$W/bin/rules --check --root $W` | 0, 465 targets in 60 rule files resolve |
| `python3 $W/skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.1 --root $W --worktree` | 0; not judged as a ready pull request (no pull request exists); it names no round record, no `broad-gate.md` and no `guarantee.md` |
| `$W/bin/unverified-check --baseline origin/release/v0.22.1 <this item>/overview.md` | 0; 2 open, 1 closed |
| `$W/bin/test` over the 65 test modules `git grep -l -E "changelog\|overview.md\|questions.md" -- tests` names (`conftest.py` left out) `-q` | 0, 4290 passed, 4 skipped |
