# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

📋 implement applied
· spec:     #964's body; `spec.md` §*Scope*, §*The tree as it stands, measured*, §*Data & interfaces*, §*Removes*; `plan.md` phase 1 and §*Test rows*; `questions.md`; `docs/the-review-record.md` §*The round record*; `templates/sdd-round.md`
· tests:    phase 1's, in `phases/phase-1.md`, each seen red by one `mutation-check` break
· verified: executed — phase 1's modules, the census and line-wrap modules, ruff, both generators' `--list` and `--case`; read — the four regenerated cases' graders against the template

## Why this work exists

The mechanics #957's agents would trip over leave first, so the agents and
their paid proof are rebuilt on a tree that is green, keeps no list beside
itself, states the round record's grammar once and closes a row with a word.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where the Windows defect was | `plan.md` phase 1: "the test's expectation, or `noninferiority.py#side_path` if the harness builds a wrong path on Windows" / both were wrong | both fixed, in 94b027cc | the case passed a `:`-separated PATH to a function splitting on `os.pathsep`; the function's `/`-literal cache filter keeps every Windows cache entry (`phases/phase-1.md`) |
| Phase 1 writes no new case | `plan.md`: "Phase 1 writes no new case" / phase 1 added nine cases and parametrised one | the cases | the generators gained readers, and the implement skill's §2 asks each rule to name its case; each was seen red (`phases/phase-1.md`) |
| `--case` and `seed_defects.py` | `plan.md` phase 1 names `replay_targets.py` and the four replay cases / `--case` could reach none of the four, and `seed_defects.py` none of its four, once 0.22.0 was tagged | both generators' `--case` read every release tag, in 74083e67 | contract §12, the same window in both; the plan's own verification could not run otherwise, and the README sentence phase 1 rewrites says `--case` regenerates a committed case |

## Not verified

| Item | Who must answer |
|---|---|
| CI green on all three legs at phase 1's commit (`plan.md` phase 1, Verified by): the Windows leg is where the case was red | the orchestrator, at the pull request's first CI run |

## Not done

Phases 2 to 4 are not built yet.

## Fed back into the spec

none
