# 1792363231-a-local-mode-work-item-draws-no-stamp — review round 6

target: 20ea0280, fixes 59732199..20ea0280

## Findings

None. The one test change keeps the strength of the check it replaced and
reads no path list.

## Confirmations

confirms: none
The new check is as strong as the list it replaced. Read:
`tests/test_the_commit_gate_decides_at_the_commit.py:1714-1721`. The old
assertion, `staged.stdout.split() == [rel]`, held two facts after the
pathspec commit of `f.py`: the guarantee is still staged, and nothing else
is staged. The new one holds the same two facts by exit status.
`git diff --cached --quiet -- <rel>` must exit 1, which means a staged
difference at that path. `git diff --cached --quiet -- . :(exclude)<rel>`
must exit 0, which means no staged difference anywhere else.

Both fail closed. A git that errors exits 128, which is neither 1 nor 0,
so a broken pathspec turns the case red rather than passing it. The `.`
pathspec is the whole tree, because `g` runs `git -C <worktree root>`, the
directory `rel` is relative to (`:1676-1677`). It gives the exclusion the
positive pathspec it needs. The smith reported each inverted assertion seen
red (read, from the coordinator's account; not re-run here).

confirms: none
It is sound across platforms by reading. `g` passes its arguments as a list
to `subprocess.run` (`:73-82`), so no shell sees `:(exclude)` or its
parentheses, and no quoting differs between platforms. Pathspec magic is
git's own syntax, the same on every platform, and `rel` is written with
`/`, which git accepts on Windows. A precedent stands in the tree:
`evals/scripts/seed_defects.py:189` passes the short form `:!` the same way.
The module runs wherever `bash` exists (`:42`), Windows legs with Git Bash
included, so CI's Windows leg executes the case.

confirms: none
The two modules pass narrowly at 20ea0280 (executed):
`bin/test tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_the_commit_gate_decides_at_the_commit.py -q -p no:xdist -k "shrunken or corpus or on_disk or census or stopped_inside_the_commit"`
exited 0 with 23 passed. That covers the census module whole and all five
shapes of `test_a_sealed_the_branch_does_not_hold_is_stopped_inside_the_commit`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The case on CI's Windows leg | `tests/test_the_commit_gate_decides_at_the_commit.py:1714-1721` | the orchestrator, from CI |
| The broad run at 20ea0280 | the branch | the orchestrator's `broad-gate --base <base> --record <item>` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_the_commit_gate_decides_at_the_commit.py -q -p no:xdist -k "shrunken or corpus or on_disk or census or stopped_inside_the_commit"` | exit 0, 23 passed, 179 deselected |
| `git grep -n ':(exclude)\|:!' 20ea0280 -- '*.py' '.github/*'` | two hits: this case, and `evals/scripts/seed_defects.py:189` |
