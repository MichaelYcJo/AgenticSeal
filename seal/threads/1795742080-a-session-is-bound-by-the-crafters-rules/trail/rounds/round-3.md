# Review round 3: 1795742080-a-session-is-bound-by-the-crafters-rules

```seal
target: f725c0b24, fixes 6a32674b1..f725c0b24
```

This round verifies the fixes for round 2. The range `6a32674b1..f725c0b24` holds the round commit `b2061e814`, the framer's fold `70c693d38`, the orchestrator's row correction `5c7781602`, the crafter's fixes `f36001393`, `9f74539cf`, `9199c7fe7`, `28b489c8f`, `8e21cf92d` and `7df9e5da2`, and the close blocks `f725c0b24`. The range holds no merge. The code reviewed is `git diff 6a32674b1..f725c0b24`, which changes `skills/implement/scripts/range_read.py`, `tests/skills/test_range_read.py` and `frame/plan.md`, and adds `trail/rounds/round-2.md`. The round read outside that diff only where the fix reaches: `lib/gitcmd.py:30-52` and `docs/running/what-a-script-gates.md:24-40`, which state where a script records a git setting that changes what it reads.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md` whole at `f725c0b24`. The commit language and the record language are both English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared.

Carried from rounds 1 and 2 and not established again: where the moved rules stand in `skills/implement/SKILL.md`, the G18 searches, the *Overlap with the release* coordinates, the Windows row's answerer, and the five gitlink shapes of the submodule case. Established again at this target: what git does with each submodule setting on `diff --raw` and on `status` (`## Probes` row 1), that each new flag is pinned by a case (rows 2 and 3), the module under git 2.39.3 (row 4), and every claim the close blocks make.

The claims weighed. The crafter's close says it widened the fix to `_uncommitted`, because `git status` hides a submodule whose checkout moved under either setting. The probe shows that: with no setting `status` prints ` M sub`, and under `diff.ignoreSubmodules=all` and under a `.gitmodules` entry with `ignore = all` it prints nothing unless `--ignore-submodules=none` is passed. It says a staged gitlink stays named without the flag, so its case moves the checkout instead. The probe shows `A  sub` under each of the three settings, with and without the flag. That claim holds. The subject of `28b489c8f`, "names a staged submodule pointer as not read whatever the ignore setting", does not match it. The pointer the flag brings back is the unstaged checkout move, and a staged pointer was named before the commit. A commit subject is history and no record a party reads at a step, so this round opens no finding on it. The close says `seal mutate` with only the `DIFF` flag removed read red, with `added`, `moved` and `deleted` failing. Row 2 gives 3 failed and 2 passed for that case, `deleted` among the failures. It says the new case read red with only the `_uncommitted` flag removed. Row 3 gives that. The close says the module passed under git 2.39.3 after `9f74539cf`, and that the tree states no oldest supported git. Row 4 gives 27 passed under `/Library/Developer/CommandLineTools/usr/bin/git`, version 2.39.3 (Apple Git-146). The finding's search, run again, prints `range_read.py` alone outside `tests/` (executed, `## Findings` 1). The close for round 2's finding 2 says `70c693d38` changes `frame/plan.md` alone, and `git diff 6a32674b1..f725c0b24 --stat` agrees.

The orchestrator's row at `frame/plan.md:81` says `DIFF` is a constant the tree has held since `c1563c7a4` and that the frame does not name it. `git show c1563c7a4` adds `DIFF = ("diff", ...)`, and `git grep -n -w DIFF` over the frame prints that row alone (executed). The row states the decision made before the pass, so it is not contradicted by the pass's widening to `_uncommitted`.

`chain_check.py --worktree` printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

## Findings

### 1. The submodule setting `seal range` switches off is named in the script, and `lib/gitcmd.py`, the one place that names such a setting, does not name it

```seal
severity: should
location: `lib/gitcmd.py:47-52`, `skills/implement/scripts/range_read.py:131-135`, `skills/implement/scripts/range_read.py:419-421`
evidence: read `lib/gitcmd.py:30-52`, `docs/running/what-a-script-gates.md:24-40`, `skills/implement/scripts/range_read.py:131-143`, `:416-431`; executed `git grep -n -F -e 'ignoreSubmodules' -e 'ignore-submodules' -- lib skills .github hooks docs` and `bin/test tests/skills/test_tmp_round3_status.py -q -s -p no:xdist` in a clone at `f725c0b24` (`## Probes` row 1)
regression: round-2#1
```

Why it matters: `lib/gitcmd.py:30` opens "This module is the one place that names which keys reshape what a script reads of git, and which subcommands they reshape", and `:49-51` says "A key or a subcommand found later to change a reading is added here and nowhere else". `docs/running/what-a-script-gates.md:24-40`, the policy, says the same of the module's docstring and adds that a key a run has measured stops being a limit. Round 2's probe measured `diff.ignoreSubmodules` taking a submodule's path out of `git diff --raw`, and this round's probe measures it and the `.gitmodules` entry taking a moved checkout out of `git status` as well. The fix names both settings in the comments of `range_read.py`, and `lib/gitcmd.py` names neither. The next script that lists a diff's or a status's paths is written against the module that says it names every such setting, and the same defect lands in it. Round 2 left one such script, `skills/code-review/scripts/chain_check.py:401` and `:409`, to the orchestrator in `## Not judged`.

The grounds. The unit is the comment on `DIFF` and the comment in `_uncommitted`, which `f36001393` and `28b489c8f` wrote. *Data & interfaces* of `frame/design.md:119` has the script start git through `lib/gitcmd.py#git` "as `docs/running/what-a-script-gates.md` *Which gate a script holds* asks", and the fix put the flag beside the other switches and its reason in the script, which round 2's paste-ready fix asked for. Round 2 weighed whether `KEYS` could hold the setting, and it cannot: `-c diff.ignoreSubmodules=none` brings the path back under the configuration key and not under the `.gitmodules` entry (`## Probes` row 1, `RAW gitmodules`). Neither round weighed the docstring's duty to name a setting found later. The defect came from there. The search prints `range_read.py:131`, `:132`, `:134`, `:142`, `:419` and `:429`, and nothing under `lib/` or `docs/`. The search is a sample, since a statement in other words escapes it. The close of round 2's finding 1 holds on what the command prints, as `## Confirmations` says.

The fix. `lib/gitcmd.py`'s docstring gains a paragraph after the sentence on `core.quotePath`, which ends at `:52`:

```text
A setting that no `-c` key holds is named here with the flag that holds
it. `diff.ignoreSubmodules` and the `ignore` of a submodule's entry in
`.gitmodules` take a submodule's path out of `diff`, and out of `status`
where the submodule's checkout moved off the commit the index holds.
`-c diff.ignoreSubmodules=none` does not reach the `.gitmodules` entry,
so a script that lists those paths passes `--ignore-submodules=none` on
each such command, as `skills/implement/scripts/range_read.py#DIFF` and
`#_uncommitted` do.
```

The comment on `DIFF` in `range_read.py` cites the module in place of restating it:

```python
# The options of every `git diff` the command runs. `--ignore-submodules=none`
# is the flag `lib/gitcmd.py` names for a submodule's `ignore` setting.
DIFF = (
```

The comment in `_uncommitted` does the same:

```python
    # `--ignore-submodules=none`, as in DIFF: a submodule whose checkout
    # moved off the commit the index holds is named whatever its `ignore`
    # setting (`lib/gitcmd.py`).
```

The edge case in the script's docstring at `:66-71` states what the command does and not why, so it stays. The paragraph crosses no OS boundary. Whether `tests/lib/test_gitcmd.py` should hold the paragraph is the fix pass's to weigh: that file holds the keys of `KEYS`, and the flag is no key.

```seal
verdict: fixed 89e4f4841
answer: `lib/gitcmd.py`'s docstring gains the round's paragraph as given, after the sentence on `core.quotePath`. The comments on `DIFF` and in `_uncommitted` in `skills/implement/scripts/range_read.py` are replaced by the round's two comments, which cite the module and no longer give the reason. The finding's evidence search, run again, prints `lib/gitcmd.py:55`, `:58` and `:59`, and `range_read.py:131`, `:139`, `:416` and `:426`. `tests/lib/test_gitcmd.py` gains no case. Its cases hold each key of `KEYS` by a repository the key reshapes, and the flag is not a key and is not passed by `argv`. What the flag does is held by `test_accepts_a_submodule_by_name_and_does_not_print_it` and `test_accepts_an_uncommitted_submodule_named_as_not_read`, each seen red in round 2's pass with its flag removed. A case that reads the paragraph would pin wording. The commit changes a docstring and two comments and adds no behaviour, so it owes no `seal mutate` run. `docs/running/what-a-script-gates.md:24-40` still says the docstring names each key and that a key found later is added there. It does not say that a setting with no key is named there with its flag. That file is the policy root, which this pass does not write.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `skills/implement/scripts/range_read.py:136-143` holds `--ignore-submodules=none` in `DIFF`, which every `git diff` of the command takes (`:252`, `:266`, `:373`, `:381`). `:422-430` gives `_uncommitted`'s `git status` the same flag. `HOSTILE` (`tests/skills/test_range_read.py:41-48`) sets `diff.ignoreSubmodules` to `all`, and `built` applies it to every fixture (`:62-72`). The submodule case's base and the new case's base each commit a `.gitmodules` entry with `ignore = all` (`:386-388`, `:467-468`). With only the `DIFF` flag removed, the submodule case fails for three of its five shapes, and with only the `_uncommitted` flag removed, the new case fails (executed, `## Probes` rows 2 and 3). The module passes under git 2.50.1 and 2.39.3 (executed, the narrow set and row 4). Finding 1 of this round is a regression in where the fix wrote its reason, and leaves what the command prints as round 2's finding asked.

```seal
confirms: round-2#2
```
What holds: `frame/plan.md:51`, row 22's middle cell, now says git's print of a submodule replaced by a file was not run for the fold that wrote the row, and that `a-file-in-its-place` holds the limit and not that print. The case holds that id at `tests/skills/test_range_read.py:356`, and its assertions name the path and leave the file's text out (read). `70c693d38` changes `frame/plan.md` alone (executed, `git diff --stat`).

What matched: the new case against its group. `test_accepts_an_uncommitted_change_named_as_not_read` (`tests/skills/test_range_read.py:440-459`) holds a staged rename, an edited record and an untracked file, and no submodule. The new case holds a submodule checkout moved under both ignore settings, which no other case of `_uncommitted` reaches, and it holds the S6 fact that a tracked path with an uncommitted change is named as not read (`frame/design.md:100`) (read). Its docstring does not open with `S6:` as its sibling's does, and its helper's docstring calls a commit that adds `sub` "an empty commit"; both are comments of the case read by whoever next edits it, so neither is a finding.

What matched: the records against the fix. `changelog.md:5` says a path that holds a submodule's commit on either side of the range is named and not printed, which the command now does under either ignore setting (executed, row 2). *Scope* item 11, S6 and *Data & interfaces* need no change for the flag, since each states what is named and not under which setting (read). `gaps.md:7` still labels the suite `unverified` with the orchestrator as its answerer, so the label is honest.

What matched: the narrow set, run once in the clone at `f725c0b24`: `bin/test tests/skills/test_range_read.py tests/skills/test_seal.py tests/lib/test_gitcmd.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` gave 585 passed, exit 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether other scripts that list a diff's or a status's paths drop a submodule under the two settings, such as `skills/code-review/scripts/chain_check.py:401` and `:409`, carried from round 2 | outside the fix range | the orchestrator, which decides whether to file it |
| The oldest git the plugin supports. The tree states none, and the flag was run under git 2.50.1 and 2.39.3 alone | `skills/implement/scripts/range_read.py:136-143`, `:422-430` | the orchestrator, with the owner if a floor is to be stated |
| Whether step 1's sentence on contract rules 4 and 5 needs a count of its own, carried from round 1 and not judged again | `skills/implement/orchestration.md:36-40`, `seal/follow-up.md:48` | the orchestrator, with the framer at the fold |
| `seal range` on Windows | `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/gaps.md:8` | CI's Windows leg |
| The full suite, the repository-wide lint and the format check | the work item's tree | the orchestrator, at the broad run once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round3_status.py -q -s -p no:xdist`, in a clone at `f725c0b24`: a submodule under no setting, under `diff.ignoreSubmodules=all` and under a `.gitmodules` entry with `ignore = all`; `git status --porcelain=v1 -z --no-renames --untracked-files=no` with and without `--ignore-submodules=none` for a moved checkout and for a staged gitlink; `git diff --raw -z` plain, with the flag and with `-c diff.ignoreSubmodules=none` for an added gitlink (git 2.50.1) | 9 passed, exit 0. Moved checkout: ` M sub` under no setting; under either setting nothing without the flag and ` M sub` with it. Staged gitlink: `A  sub` under every setting, with and without the flag. `diff --raw`: under the configuration key, plain prints nothing and the flag and the `-c` key each print `sub`; under `.gitmodules`, plain and the `-c` key print nothing and the flag prints `sub` |
| `bin/seal mutate skills/implement/scripts/range_read.py` with two `--replace` pairs, `DIFF`'s flag removed and `_uncommitted`'s flag removed, `--tests "bin/test tests/skills/test_range_read.py -q -k submodule -p no:xdist"`, same clone | 2 mutants, 2 red, exit 0 |
| The same command with each pair alone, `-k test_accepts_a_submodule_by_name_and_does_not_print_it` for `DIFF`'s and `-k test_accepts_an_uncommitted_submodule_named_as_not_read` for `_uncommitted`'s, same clone | `DIFF`'s: 3 failed and 2 passed, `deleted` among the failures. `_uncommitted`'s: the new case failed. Each mutant red, exit 0 |
| `bin/test tests/skills/test_range_read.py -q -p no:xdist` with `/Library/Developer/CommandLineTools/usr/bin/git` (git 2.39.3, Apple Git-146) first on `PATH`, same clone | 27 passed, exit 0 |
