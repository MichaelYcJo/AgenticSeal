# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

📋 implement applied
· spec:     #964's body; `spec.md` §*Scope*, §*Marks and labels*, §*The census and the stamps leave*, §*The tree as it stands, measured*, §*Data & interfaces*, §*Removes*; `plan.md` phases 1 and 2 and §*Test rows*; `questions.md`; `docs/the-review-record.md` §*The round record*; `docs/the-reader-registry.md`; `templates/sdd-round.md`
· tests:    phase 1's and phase 2's, in `phases/phase-1.md` and `phases/phase-2.md`, each seen red by `mutation-check`
· verified: executed — phase 1's and phase 2's modules, the census and line-wrap modules, `bin/rules --check`, ruff, both generators' `--list` and `--case`, the whole collection with the durations case; read — the four regenerated cases' graders against the template

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
| How many `Reads:` lines and stamps there were | `spec.md`: "364 lines in `.py` files", "55 `RIDER:` comments in 20 files" / 364 is every `Reads:` occurrence at d4552372, strings included; 304 declaration lines outside the removed files and 21 inside them at 74c7963a; 55 is the files holding `RIDER:`, and the checker read 12 riders | the tree's counts, asserted by the scripts | the scripts assert what they remove, and a figure that is not a count of the thing cannot be asserted (`phases/phase-2.md`) |
| A stamp the grep still finds | `plan.md` phase 2, Verified by: "`git grep -n -E "Verified [0-9-]+ against"` finds nothing outside `seal/specs/` and `changelog/`" / it finds nine lines: one stamp in the frozen copy in `hooks/cmdline_base.py`, eight in the fixture shapes of `tests/block_shapes.py` | both kept, in 17b6e581 | the frozen bytes are pinned to `86256492` by `tests/test_the_frozen_reading_never_grows.py`; the fixtures are quotations `spec.md` §*Scope* keeps, read by the renderer cases as documents |
| Removals the frame did not name | `spec.md` §*Removes* names the stamp cases of one module / four more modules loaded the checker, and the kernel's anchor constants, a marked statement in `docs/branch-and-release.md`, a sentence in both editions of `docs/one-root-by-lifetime`, the liveness statement's rider reader, and comments in the kernel, the block walk, the config reader and three riders stood on it | removed or rewritten in 17b6e581, each named in `phases/phase-2.md` | `CLAUDE.md` §*The rule a mechanism is kept against*: what stood on the old fact leaves in the same commit; the spawn named the class and the `git grep` that enumerates it |
| A stamp inside an agent definition | `spec.md` §*Scope*: "The five definitions under `agents/`" are #957's / one of the twelve stamps closes the `RIDER:` comment in `agents/smith.md` | removed in 17b6e581, the comment kept; no agent eval | decided before the spawn: a stamp of a removed checker cannot stay, and the line is inside a comment, so nothing the smith does changes |
| T1 "unchanged" | `plan.md` §*Test rows*: T1 is the module "as it stands after phase 2, its stamp cases gone", mutation "unchanged" / its case pinning the stamp form in the header would pin a sentence the phase removes | that case rewritten to pin that the header names no stamp and no checker, seen red at 74c7963a and by three `mutation-check` breaks | contract §14: the header is what a person reads to learn the convention, and its new text needs a pin; the module's other seven cases are unchanged |
| What `test.yml`'s comment names | `plan.md` phase 2: "rewritten to the reason that stays, or removed with `fetch-depth` where none does" / the rider test had asked git nothing since #239, and the reason `tests/test_ci_gives_the_checks_what_they_need.py` gave named `tests/test_the_reopening_is_one.py`, which the tree does not hold | the comment, `publish-release.yml`'s and that module's docstring and message name the frozen-copy case, which skips at depth 1; `fetch-depth: 0` stays | the frozen-copy case is the live reason, read and run in this phase |

## Not verified

| Item | Who must answer |
|---|---|
| CI green on all three legs at phase 1's commit (`plan.md` phase 1, Verified by): the Windows leg is where the case was red | the orchestrator, at the pull request's first CI run |
| The test modules of the 34 scripts phase 2 changed only in their docstrings, beyond the modules `phases/phase-2.md` names as run: a case that reads a docstring whole would meet the removed `Reads:` line there | the sealer, at the broad gate |

## Not done

Phases 3 and 4 are not built yet.

## Fed back into the spec

none
