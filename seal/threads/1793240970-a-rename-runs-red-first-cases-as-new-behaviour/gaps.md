# Closing memo: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

## Why this work exists

A rename or a move paid for a case written new and a `seal mutate` run its existing cases already made needless, and now one row of the verify skill says what proves it, which the crafter, the implement skill, the review and the sealer read.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The eval runs' case filter | `frame/plan.md` rows 1 and 2: `--case rule-crafter-rename` and `--case rule-crafter-slugify`. The runner matched no case and spent nothing: `No eval cases found matching --case "rule-crafter-rename"` | `--case '*rule-crafter-rename'` and `--case '*rule-crafter-slugify'` | `claude plugin eval --help`: "`--case <glob>` Filter cases by name glob", and `rule_cases.py#main` writes each case's name as `<agent> <directory>`, so a bare directory name matches nothing |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the orchestrator, through `seal gate` |

## Not done

nothing

## Fed back into the design

none
