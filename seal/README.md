# What AgenticSeal maintains in seal/

This directory exists for AI sessions to hand work to each other. It is one
root laid out by lifetime: the rows that outlive a work item at the top, and
each work item whole under `seal/threads/<work-item-id>/`, where it stays until
its release is settled. The settle writes into `docs/` each section the
released specs' `## Rule changes` name, as their latest decision, and
`settle --apply` removes each released directory whole whose record holds no
open row, whether or not it wrote a `spec.md`. A settle is not a work item and
opens no directory here.
`skills/settle/SKILL.md` is the procedure and `skills/settle/scripts/settle.py`
the command behind it. A work item's directory is safe to delete wholesale
**once its open rows have been moved out**, which *Export rules* below says
where to read: nothing that must survive is allowed to live only there.

It lives at one of two places, and its presence at either, with this file's
first line as it stands, is what opts the repository into the workflow.
There is no config key. **Shared mode** keeps
it at `<repo>/seal/` and commits it (gitignored files don't follow worktrees
or other machines), so every clone reads it and CI can check pull requests
against it. **Local mode** keeps the
same root at `$(git rev-parse --git-common-dir)/seal/`, under the common git
directory: every linked worktree of the clone shares it, nothing under it is
ever a commit candidate, and no `.gitignore` line is needed. What local mode
gives up is CI, because the pull-request checks read committed files, and
any other machine, which starts empty.

**`seal mode local` and `seal mode shared` switch between the two.** Each
moves the root, stages the change and records the mode in `config.md`
beside this file, and leaves `.github/` alone; whoever ran the command
commits the change. Whether CI checks pull requests is a second answer:
`seal pr-checks install` writes `.github/workflows/hygiene.yml` where this
root is in the tree, `seal pr-checks remove` takes it out, and
`seal pr-checks` says which is the case. `seal mode` alone says where the root is and what that row claims,
and `seal mode --check`, which the pull-request checks run, exits non-zero
when the two disagree. Nothing reads the row at runtime: the folder's
location is the only signal. The by-hand move asks git for both paths, so
the commands land the same from a subdirectory. From local to shared:
`mv "$(git rev-parse --git-common-dir)/seal" "$(git rev-parse --show-toplevel)/seal"`,
`git add "$(git rev-parse --show-toplevel)/seal"` and a commit. From shared
to local: `git rm -r --cached "$(git rev-parse --show-toplevel)/seal"`,
`mv "$(git rev-parse --show-toplevel)/seal" "$(git rev-parse --git-common-dir)/seal"`
and a commit of the removal.

**`seal export` and `seal import` are the way across between machines**, and
the only one there is: local mode's records reach no other clone by
themselves. `seal export` zips this root alone; `seal import` merges a zip
back and never overwrites a file, so a name already here keeps its bytes and
the incoming copy lands beside it as `<name>.incoming<ext>`. What sits
*beside* this root under the git directory is what must not travel: the
smith mark, the worktree choices, any lease, and
the last export's manifest at `agentic-last-export.json`. The export walks
this directory and nothing else, which is why the root has to be its own.

**The first line of this file is the marker.** `hooks/optin.py#MARKER` holds
the same line, and every gate reads a `seal/` whose `README.md` does not open
with it as a repository that never opted in: a directory the project keeps for
itself, as a package named `seal` has one. First setup that meets such a
directory writes nothing into it and keeps the root under the git directory.
Leave the line as it is.

**The throwaway opt-out is the file `.git/agentic-scratch`, and it cannot be
committed.** Where it exists, every gate reads the repository as one that
never opted in and says nothing. It is for a repository built to be thrown
away, such as a fixture made by hand to reproduce a gate decision. It lives
under the git directory because a marker committed in the tree would turn
the workflow off in every clone.

## Export rules

`skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep
the records* states who moves the rows still open in a work item's directory
out of it, when, and where each one goes.

## Layout

```
seal/
├── README.md            this file
├── config.md            what this repository says about itself, one row per
│                        item: `Commit and pull request language`,
│                        `Record language`, and `Mode`, which `seal mode`
│                        reads and writes. Optional: no file and no row both
│                        mean the default, and `Mode` has none; an absent
│                        one is filled in from where the root is
├── parity.md            migration config, only where one is declared
├── pact.md              the pact, only in the repository that holds one
├── follow-up.md         schedulable items in a repository with no tracker
└── specs/<work-item-id>/  one work item, whole
    ├── routing.md         which way it was routed, written before the first edit
    ├── spec.md, plan.md, questions.md, overview.md, changelog.md
    ├── phases/
    │   └── phase-N.md     what one build phase was asked and found
    ├── rounds/
    │   └── round-N.md     target SHA, verdicts, paste-ready fixes, executed probes
    ├── broad-gate.md      the one broad run, at a SHA, against the base
    └── guarantee.md       the sealer's verdict on the work, at a SHA
```

There is no task list here and no directory for one. `plan.md`'s Phases table
is where the work records how far it got, in a Status column whose closed value
is the commit that closed the phase: a past state someone can open, rather
than a tick anyone can type.

Reports meant for humans go to PR comments; this directory is for the **next
session**. The two audiences never share a file.
