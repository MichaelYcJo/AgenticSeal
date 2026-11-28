# Design: 1795849897-submodule-pointer-in-typed-diffs

## Grounding

The tree as read at `4a63fef1`.

| Policy clause | What it fixes for this work |
|---|---|
| `lib/gitcmd.py#FLAGS`, and #1640's change to `agents/inspector.md` step 1 | a git read whose output shows a party paths carries `--ignore-submodules=none`, so the repository's `diff.ignoreSubmodules` or a `.gitmodules` entry's `ignore` cannot hide a moved pointer |
| `agents/inspector.md` step 2 | the inspector reads the pull request's diff with `git diff <base>...HEAD` |
| `agents/proofer.md` *A round after a merge of the base reviews the branch's own commits and the merge's resolution* | a verifying round over a merge reads `git log --no-merges -p <a>..<b> ^<base>` and `git show <merge>` |

Probe, `executed` in a scratch repository on 2026-11-28 with `diff.ignoreSubmodules=all`: a branch that only moves a submodule's pointer shows no submodule hunk under `git diff base...HEAD` or `git log --no-merges -p base..HEAD ^base`, and shows it under each with `--ignore-submodules=none`. A merge whose resolution sets the pointer to a third commit shows no hunk under `git show <merge>`, and shows it under `git show --ignore-submodules=none <merge>`.

## Scope

In: the three git reads an agent types by hand to see the diff it judges, the inspector's `git diff <base>...HEAD` and the proofer's `git log … -p` and `git show <merge>`, each carrying `--ignore-submodules=none`, with a case that pins each command's form.

Out: reads that do not show a party the diff it judges. `agents/inspector.md` step 4's `git -C <root> diff <the last record's target>..HEAD -- agentory/threads/<item>/` names only the work item's records, where no submodule stands. The other `git log` and `git show <commit>:<path>` reads in `skills/` read history or a file's text, not a diff a party judges. Scripts already carry the flag through `lib/gitcmd.py#argv`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a repository with `diff.ignoreSubmodules=all` and a pull request that moves a submodule's pointer, when the inspector reads the diff by step 2, then the command it types shows the moved pointer | `tests/behaviour/test_the_inspector_inspects.py`, the case pinning step 2's diff command |
| S2 | Given the same repository and a verifying round over a merge of the base, when the proofer reads the branch's own commits and the merge's resolution, then both commands it types show a moved pointer | `tests/behaviour/test_the_proofer_reviews.py` or the module that holds the proofer's merge paragraph, the case pinning both commands |

## Data & interfaces

No interface changes. Three commands in two agent definitions gain one flag.

## Rule changes

- nothing
  why: the change is to agent definitions, and no document under the policy root states these commands

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| nothing | | the change adds a flag and removes no text |

Framed 2026-11-28 by the session, before the build.
