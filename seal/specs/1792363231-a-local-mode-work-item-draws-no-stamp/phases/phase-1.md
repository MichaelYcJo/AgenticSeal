# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | b701bb53 |


## What this phase was asked

Build the local writer, `seal_stamp.queue_for_local_guarantee(path,
session)`. Pull the values assembly of `_queue_one` into a helper that both
writers share, and keep the shared-mode cases green with their bodies
unchanged. Each new case is seen red against the tree as it stands, then
green. `questions.md` Q1 was answered (a), so the writer is built as framed.
Q2 is open with default (a), a stated limit, and the build rests on (a). Q3
belongs to phase 2.

## What this phase found

**The frame holds, with two corrections about the tree.**

- `chain_check.py:73` does not load `routing.py`. `ROUTING` is a path, and
  only `main` loads it. The writer loads it with `chain.load(chain.ROUTING,
  …)` and reads `optin` through the loaded module, as `routing.optin`, so
  no third loader exists.
- `optin.home_at` alone does not rule out shared mode. Take the path
  `<repo>/seal/specs/<id>/guarantee.md`: the directory above `seal/` is
  `<repo>`, and `home_at` answers `<repo>/seal`, so the check passes. The
  writer therefore also requires `optin.git_common_dir(<main worktree>)` to
  resolve to that directory. The main worktree is the first entry of
  `git -C <common> worktree list --porcelain`. A scratch probe ran that
  command from a main checkout's `.git`, from the common dir a linked
  worktree shares, and from a bare repository, and it named the main
  worktree each time.

**How the writer reads what it does not refuse on.** An unreadable
`guarantee.md` raises, which is what the shared writer's docstring states
for its own reads. The gate in phase 2 must be silent on that exception. A
`routing.md` or `broad-gate.md` that cannot be read counts as absent: the
first then means no `Branch` row, and the second means no `gate` row. A
work item with no `rounds/` directory gets a stamp reading `0` rounds,
pinned in the re-seal case.

**The helper is `_queue_values`.** `_queue_one` keeps its one
`.splitlines(` call, on the `git ls-tree` listing, and passes the result
on. Neither the helper nor the local writer calls `.splitlines(`: the
writer splits the `worktree list` output with `split("\n", 1)`. So
`tests/test_every_reader_ends_a_line_where_gfm_does.py`'s list of units
that may call it needed no new entry.

**Every unit added was mutated, one `mutation-check` run each, at
b701bb53.** Seventeen runs were made. A case went red for each refusal
(shape, common dir, local root, verdict, target, earlier `sealed`, a values
file already present, the branch ancestry), for the rounds count, the
absent `rounds/`, and the helper's count, base and item. Four mutants
survived, and each has an input that only it would change.

- `os.path.realpath` on the git-derived common dir and on `home_at`'s
  answer. On darwin, git and `realpath(path)` both return resolved paths.
  The reason for the call is the forward slashes git prints on Windows,
  which is Q3, so the CI Windows leg is what checks it. That is two runs.
- `not found`. `realpath("")` is the working directory, so the guard only
  matters when the working directory is the common dir. `not home` has the
  same reason and was not run.
- `not branch`. Without it, `refs/heads/None` is asked for, and only a
  branch named `None` would answer.

Two checks were removed, in b701bb53, because no case could make them
fail. One refused when the `worktree` prefix was missing, which `not found`
already covers. The other refused when the guarantee could not be read,
which now raises. `os.path.normcase` was dropped too, because Q3 is phase
2's to decide on CI's Windows leg.

**Cases beyond the frame's list.** S4's parametrized case gains `no Target
SHA row`, the second refusal in `spec.md` §*Data & interfaces*, which no
given in S4 named. S5's writer-half case also writes the same `sealed`
text to `notes.md` under a local work item. That backs the writer's own
check of the path's shape, because phase 2's gate returns before it
imports the writer.

**What phase 2 can rely on.** The writer returns `[]`, or a list holding
`seal_stamp.QUEUED` formatted with the id and the values file's real path.
It runs one `git worktree list` call and loads `chain_check.py` only after
the path's last three parts read `seal/specs/<id>/guarantee.md`. The gate's
own check of the path's shape, which S6 asks for, is what keeps the other
edits from paying for that call.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
