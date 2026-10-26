# Phase 1: 1792976216-the-records-and-the-pr-checks-are-two-answers

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 4d019bcc |

## What this phase was asked

Build phase 1 of `plan.md`: the two exit-0 states of
`skills/verify/scripts/unverified_check.py` for a pull request that declares
nothing, with cases in `tests/test_unverified_check.py`, and the flow case
`tests/e2e/teammate/test_teammate_flow.py`, which runs every `run:` step of
`templates/hygiene.yml` except the clone against the four bases of `spec.md`
*In* item 7. Show the flow case red at `02ee12de` on the two failing bases
before it passes. Close phase 1 before phase 2 starts.

## What this phase found

**The frame holds** (`read`). The coordinates in `plan.md` *Technical
context* stood where it said: the missing-path refusal at lines 1518 to 1521
and 1590 to 1607, `settled_root` at 1434, and the exit 2 at 1709 to 1718.

**The red was seen at `02ee12de`'s scripts** (`executed`). The branch had
changed nothing outside this work item's directory since `02ee12de`, as
`git diff --stat 02ee12de HEAD` showed: four files, all under this work
item's directory. Against that tree the flow case failed on
exactly two bases, each in the unverified step alone, and passed on the
other two:

| Base | Step that failed | What it printed |
|---|---|---|
| no root | the unverified record is readable | `no such path: seal/specs/ — and nothing under it at origin/main either` |
| a work item with no overview | the unverified record is readable | `no overview.md found under seal/specs/ — nothing was checked` |

The new cases in `tests/test_unverified_check.py` were red the same way
before the code: 13 failed, among them both accepting cases of `Test_main`
in their baseline and plain forms.

**Absence is read at the working tree's top level only.** `spec.md` *In*
item 6 says *the `seal/` directory is not there*. `absent_root` reads that
as: the directory above `seal/` is the one `git rev-parse --show-toplevel`
names, compared with `os.path.samefile`, and holds no `seal/` directory.
Without it, a `seal/specs` typed from a subdirectory, or outside any
repository, would pass in silence. That is the misspelt-path failure
`settled_root` was written to prevent. The rule change in `spec.md`, *where
no `seal/` directory is in the tree*, already reads this way, so nothing in
the frame changes. `Test_main::test_refuses_a_missing_root_below_the_top_level_as_a_typo`
pins it.

**Several paths get one sentence each.** Where every path is in an exit-0
state and they differ, each path prints the sentence of its own state. The
settled root's one-line form for a single path is unchanged.

**Q3 is answered (a)** (`executed`). `bin/test-layout --check
tests/e2e/teammate/test_teammate_flow.py tests/test_unverified_check.py`
printed `2 files read, 0 refused, 0 declare no TARGET`. A document `TARGET`
and a free-named scenario class are both accepted, so the file stays where
the frame put it. `questions.md` is not this phase's to write, so its Status
cell is left for the orchestrator.

**Q2 has a second skip beside the frame's.** The flow case skips where
`symlink_or_skip` cannot link `$RUNNER_TEMP/specseal` to the tree, as Q2's
default says. It also skips where `bash -c 'command -v python3'` fails,
because every step the template runs names `python3`, and the template
pins `ubuntu-latest`, which always has one. Whether either skip fires on
the Windows legs of `.github/workflows/test.yml` is the measurement Q2
names. It is `unverified` here, and the pull request's CI run on
`windows-latest` answers it.

**Scenario S8 holds** (`executed`).
`python3 skills/code-review/scripts/chain_check.py --baseline release/v0.22.4`
exited 0. Its output named no `## Rule changes` problem. It printed the
notices a work item gets before its review: no round record yet, no
`broad-gate.md`, no `guarantee.md`, and the pull request's state unknown
with no pull request open.

**The mutation runs** (`executed`, `bin/mutation-check`, one command per
unit, after `846e25ad`):

| Unit | Mutants | Result |
|---|---|---|
| `absent_root` | the `seal/` directory check dropped; the top-level comparison answering `True`; the `specs` spelling check dropped | 2 red and 1 survived. The case `a typo` was added in `4d019bcc`, and the survivor then ran red |
| `unwritten_root` | `return True`; the `settled_root` exclusion dropped; the spelling check dropped | 3 red |
| `main` | the absent-root branch off; the unwritten-root branch off; that branch reached with a deletion standing; each new sentence replaced by the settled one | 5 red |

The flow file's own helpers, `run_blocks` and `steps_to_run`, were not
mutated. Against green scripts, a mutant that runs fewer steps stays green
by construction. What stands behind the case is that it was red on the two
bases at the old scripts. The refusing case of its class pins the clone
count.
