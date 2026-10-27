# 1792363189-rule-3-decides-on-the-agent-not-one-run — overview

## Why this work exists

Rule 3 of the behaviour evaluation judged each shape and reach grader on its own over two runs, so one run of one grader could fail a rewrite whose passes rose; it now adds up a side's passes and names a grader lost on every run, the statistic the owner chose on 2026-10-19.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S2 has no `CASES` entry of its own (phase 1) | the scenario table lists S2 beside S7's rename; the per-grader shape case S7 renames already carries S2's numbers (`shape-report-exists` 2/2 → 1/2) | S2 is the renamed case plus a reason assertion | a second entry with the same numbers covers nothing the first does not (`phases/phase-1.md` §*What this phase found*) |
| S8's grep sees only the README (phase 1) | S8 verifies the rewrite with `git grep -n "at least as often" -- evals tests` | the phase record quotes a wider grep for `as often` and `less often` as well | both docstring sentences break across a line inside the phrase, so at 881cc7be the grep found only `evals/README.md:32` (executed by the smith) |
| A statement of the old rule outside `evals/` and `tests/` (round 1) | Scope 4 narrowed the sweep to `evals/` and `tests/`; Grounding §19 asks for every sentence stating the per-grader rule | #957's `spec.md:224-228` rewritten in place to point at `evals/README.md` rule 3 (7d2bc3d1) | `rounds/round-1.md` finding 1, confirmed closed by `rounds/round-2.md` |

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether `model` (`noninferiority.py#cheaper_model`) should follow rule 3's aggregation; it still compares per grader | answered by the default: `questions.md` Q1's `leave it` shipped in 0.22.2 through #982 and release pull request #997, which the owner merged into `main` on 2026-10-19, and `evals/scripts/noninferiority.py#cheaper_model` still compares per grader at 434334d9 (default taken by the 0.22.4 settle) |

## Not done

Rule 3 still lets one run decide where the baseline passed every run of every grader, since nothing can offset a loss; #957's sealer record is that case. It is the decided statistic working as chosen, recorded in `spec.md` Scope rather than tuned. `.test_durations` keeps the two old case names, out of scope by `spec.md`.

## Fed back into the spec

nothing
