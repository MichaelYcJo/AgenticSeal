# 1791876666-the-test-suite-is-held-to-a-budget — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show; each part written when it happened. Opened at phase 1. -->

📋 implement applied
· spec:     spec.md (Scope, The removal criterion, S1–S4, S6, Removes); plan.md (Technical context, phase 1, Test rows); questions.md Q4, Q6; docs/the-evidence-ledger.md §A released row is read again in the branch's fragment; templates/sdd-phase.md
· evidence: seal/ledger/1791876666-the-test-suite-is-held-to-a-budget.md — Re-read · G4 (seal/releases/0.17.0.md), phase 1
· verified: phases/phase-1.md, which labels each figure executed or read

## Why this work exists

The suite only grows, and a few files whose cases each spawn git and bash hold
most of its time. This work cuts those files by removals a mutation table
proves redundant, and lowers #930's budget rows to match.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| 191 parametrized ids of `test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land` removed, phase 1 | `spec.md` §Removes: "nothing — the frame names no unit … every removed function is a divergence row". The function stays; 191 of its 226 parameter rows leave | the removal | phase 1's mutation table: m1–m5 each still red after, and the counts of killers that are not S2 rows unchanged |
| S3 "the sample's rows all land in `main` or `u` without hooks" | read as true on every leg. On Windows `env -i` finds no git, and the `env -i` rows are the only S2 killers of m4 and m5 | two `env -i` rows kept, skipping on Windows by a named limit (`NO_GIT_UNDER_ENV_I`), as `stdbuf` already did; every other row fails rather than skips | the S9 case's own comment (#692's Windows pass) and `.test_durations`' low-band price of every `env -i` row |
| The battery, m1–m4 | `plan.md` names m1–m4; Q6 asks phase 1 to draw the battery from the docstrings | m1–m5: m5 breaks the stub's lease check (`hooks/githooks.py#_P2`), the shell half of the route m4 breaks in Python | Q6's default lets the work extend the battery |
| `test_every_sampled_name_is_a_corpus_row` removed, phase 2 (NAME NOT IN TREE) | `spec.md` §Removes names no unit; phase 1 planted it as T3 | the removal | the regrowth check reads phase 1's pins as changed functions, and T3's mutant, a misspelt `SAMPLE` name, is killed by S2's own row for that name, so no line could prove it; `mutation-check` with the name misspelt is red without T3 (`phases/phase-2.md`) |
| The regrowth check's runs | `spec.md` §*The regrowth check*: "runs the function's file twice … with the function, which must be red, and with it deselected" | the file once as it stands, then once under each function's mutant, red with the function's own ids the only killers; a file whose proof would pass a five-minute bound is named to restructure | the owner's decisions of 2026-10-14: one run per mutant, read for its killer set, and the proof within five minutes on a pull request |
| `mutation-check --baseline-passed` | the frame names no change to `mutation-check` | an option that skips the run against the file as it is, for a caller that ran it; a bare call is unchanged | without it one run per mutant still costs two file runs, and the five-minute bound would name files the model can afford; released row L7 is corrected in the fragment |
| The five measurers and `## Large test files` in `budget_check.py`, and the rows in `seal/budgets.md` | `plan.md` phase 2 delivers them "where #930 is in the tree" | not built in phase 2 | #930's `seal/budgets.md` and its `budget_check.py` are not on this branch; they follow #930's landing, as the orchestrator's spawn said |
| The ledger fragment, which `plan.md` places in phase 4 | written in phase 1, with the `Re-read · G4` row S6 owes once a cited case's text moves | phase 1 | without it, CI's lenient `evidence-check` exits 1 on the drift; the orchestrator moved the fragment to phase 1, and named `plan.md`'s test-rows correction that the records arm requires |

## Not verified

| Item | Who must answer |
|---|---|
| ✅ Whether each of the 35 sampled rows lands in `main` or `u` without hooks on ubuntu-latest. Only macOS was executed, and Windows was read from `.test_durations`; G4 records 145 rows landing on Linux in 2026-10, not which ones | PR #939's CI run 38477955404 at 480bea69: every ubuntu job passed; three rows failed on macOS and Windows and were fixed at badc0bd4 (`phases/phase-1.md`) |
| That on `macos-latest` and `windows-latest` the fixed sample lands where badc0bd4 says: `shape: nice` and `#686: cd $W unset` run, and `#686: builtin cd` skips on Windows by `NO_CD_INTO_AN_UNQUOTED_PATH` | the next CI run on PR #939, read by the orchestrator |
| The phase-1 file's Windows seconds after the sample (Q4) | #931's next refresh, or a `workflow_dispatch` of `test.yml` on the branch |
| What the `cases` job says on PR #939, and its cost per function (Q6). Locally at 74c23261, with `-n 4` at load averages 94–115, the case file proved 11 functions in 25 s, and the commit-gate file was named to restructure: its one run took 93 s, so its three functions needed 278 s of the 275 s left. On an idle 4-core runner it may fit | the job's first run on PR #939, read by the orchestrator. A restructure finding there is #942's or phase 3's to answer, by testing S2's decision directly |

## Not done

The `slow-file` row is not lowered, because #930's `seal/budgets.md` is not on
this branch. The figures wait in `phases/phase-1.md`, and the later of the two
pull requests lowers the row.

## Fed back into the spec

none
