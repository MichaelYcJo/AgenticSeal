# Closing memo: 1793599988-a-citation-opens-after-the-squash

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck over the tree at the phase's commit | answered: `trail/gate.md`, the `Broad gate` row passed at `d04f8fa9d` against `d57e9ee7a`, and `guarantee.md` sealed on it |
| closed The tree case after `release/v0.28.1` is merged in, and any citation it refuses then (`frame/design.md` *Scope* item 6, `frame/questions.md` Q1) | answered: `git log origin/main..origin/release/v0.28.1` lists no commit, and release pull request #1308's `tests` run 41538707128 at `6beac2ee` passed the tree case over a tree holding it |
| closed The tree case on CI's checkout, where only the remote-tracking `main` and `release/*` refs stand | answered: #1303's `tests` run 41532526560 at `bc706e3cb` ran the tree case on CI's checkout, where only the remote-tracking `main` and `release/*` refs stand, and passed |
| closed The module on the Windows leg, where paths are joined with a backslash | answered: #1303's `tests` run 41532526560 at `bc706e3cb` passed on its four `windows-latest` legs and every Linux leg |
| closed The exit-code half of the containment test working alone, apart from git printing no ref when `--contains` fails (`trail/phases/phase-1.md`, the eleventh mutant) | answered: the proofer read the diff in `trail/rounds/round-1.md` to `round-3.md`, and `guarantee.md` sealed after the last |

## Not done

The tree case keeps no floor on the number of citations it reads. A floor
written as a number is a count kept beside the tree, which
`skills/core/SKILL.md` *The rule a mechanism is kept against* refuses, and
the planted cases already hold the reader through the imported
`COMMIT_PATH`.

A work item's own `trail/` and `guarantee.md` are not read under "an
ancestor of HEAD". That is `frame/plan.md` A4, rejected for this item on
the grounds the plan gives.

The four open issues that cite the dead commit in their bodies were not
edited. A tree check reads no issue body, and the frame leaves them to the
orchestrator (`frame/design.md` *Scope*, out).
