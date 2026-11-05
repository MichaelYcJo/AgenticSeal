# Review round 3: 1793833679-update-reads-the-config-dir-in-use

```seal
target: fbcd2f26, fixes 7ab6c849..fbcd2f26
```

This is a verifying round. It read the diff of the fixes, `7ab6c849..fbcd2f26`,
in the repository's checkout of the branch, as the spawn prompt named it.
The range holds four commits. bf499823 is the orchestrator's routing row
and two frame edits. 9ec4d8e0 is the fix pass. 3505bc3a is round 2's close
block, and fbcd2f26 is the orchestrator's fold. `git show --stat` lists, for
9ec4d8e0, `skills/update/SKILL.md`, the module
`tests/behaviour/test_update_reads_the_config_directory_in_use.py` and the
work item's `changelog.md`. It lists only the work item's `frame/design.md`,
`frame/plan.md` and `trail/rounds/round-2.md` for the other three
(executed). `seal/parity.md` is not declared, and `seal/config.md` has no
`Record language` row, so the record is in English.

Carried from round 2, not re-established: that a line ending in `&&`
continues onto the next line under `zsh -c` as under `bash -c`, which round 2
ran. This round ran the block under `bash -c` alone. Also carried is round
1's list of the needles of `tests/behaviour/test_release_hygiene.py` that
`frame/design.md` G8 names for steps 2b and 3. This round ran the two cases
again rather than reading them again. Re-established here: every verdict
below, round 2's finding 1 mutant, run again, and the narrow runs.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the repair block at `skills/update/SKILL.md:72-75` ends its read
with `&&` at `:73`, so the `printf` at `:74` runs only on a read that exited
0 (read). The crafter claimed a mutant with the `&&` removed read red. This
round ran it again with `bin/seal mutate` over the module: `red`, exit 0
(executed). The failing case was
`test_step_2b_prints_no_repair_where_the_record_cannot_be_read`, at its
first assertion, `assert 0 != 0`. Its output showed `mv '' .stale.bak`, an
`rsync` into `/` and `mkdir -p /.in_use`, which is round 2's defect (executed).
The skill at 7ab6c849 differs from this mutant's block only by that `&&`, so
the same red stands for the crafter's claim of red against 7ab6c849 (read in
`git diff 7ab6c849 9ec4d8e0`). Unmutated, the module passes (executed). The
block's two lines still open with `p=$(` and `printf`, so
`test_step_2b_prints_the_repair_with_this_sessions_paths` keeps its shape
guard, and it passes (executed). The crafter claimed the read raises on a
missing file, bad JSON and a missing key. The program at `:73` opens the
file, calls `json.load` and indexes three keys and one list position, and
each of those raises where it fails (read). The fragment at `changelog.md:3`
now says the block prints nothing and exits non-zero where it cannot read
the install record, and that step 2b's table says to stop (read). `git grep`
on `cannot be read` and `exits non-zero` outside the round records finds
that sentence, the skill's `:69`, and *Scope* 6f, S8 and *Data & interfaces*
at `frame/design.md:36`, `:58` and `:68`. Each says the same thing (executed).
The close holds.

What matched: the new case, `test_step_2b_prints_no_repair_where_the_record_cannot_be_read`
(`tests/behaviour/test_update_reads_the_config_directory_in_use.py:118-128`),
runs the repair fence with neither scratch directory holding a record. It
asserts a non-zero exit and an empty stdout, and its docstring claims no
more than that. It covers what no case of its group covers. The S3 case runs
step 2b's first fence. The repair case runs the second fence on a record
that reads. This case runs the second fence on a record that does not read.
`bin/seal layout --pairs` over the module read 1 file and found 0 pairs, exit
0 (executed).

What matched: the crafter claimed a closed set: it took the skill's bash
fences apart, looking for a command that acts on a path a failed read did
not give, and found only the repair block. The skill holds six fences
(`grep -n` on the fence lines, executed). The fence at `:29-32` runs the
installer. The fence at `:52-55` reads two files and writes nothing. The
fence at `:92-115` runs `rm -f "$f"` on the name `mktemp` gave. The fence
at `:149-203` works on `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"`, a
path the shell spells and no read gives. The fence at `:260-275` is the
output form (read). The claim holds.

What matched: the new last row of step 2b's table (`skills/update/SKILL.md:61`)
sends a read that raised to a stop before step 3, with the error, no repair
and no summary. The block's sentence at `:68-70` points to that row (read).
The fold's *Data & interfaces* block at `frame/design.md:71-72` and the
first command at `:65` match the skill's `:73-74` and `:53` character for
character (`diff`, executed). The routing row at `frame/plan.md:42` routes
round 2's regression to a fix pass because the defect came from round 1's
paste-ready snippet applied as given. That is the second row of
`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame* (read). Its grounds say the frame says nothing of a
failed read. But `frame/plan.md:13` says a failed read stops step 2b loudly,
which round 2 cited. The route is the same under either reading, so this
is no finding. *Scope* 6e and S7 (`frame/design.md:35`, `:57`) state what
round 2 confirmed of round 1's fix pass (read). The crafter's 159 passed is
an aggregate this round did not re-run whole. The runs it did make are in
`## Probes`.

Three gaps are named here, and none is a finding. First, the new row at
`skills/update/SKILL.md:61` covers a raised read of the install record or of
the copy it names. Its reason, "the repair is built from the path this read
could not give", holds for the record alone. Where the record reads and only
the copy's `plugin.json` does not, the repair block's read at `:73` still
gives the path (read). The row's act there is to stop, show the error and
offer no repair. That tells the user nothing false and runs nothing. A
record that names a copy with no readable `plugin.json` is a damaged cache
that neither outcome of the installer leaves, by step 2b's account at
`:42-48`. So it is a limit, by the reasoning of `frame/design.md` G5.
Second, the close claims the read raises on every way the record can fail
to give a path. An `installPath` that is the empty string prints an empty
line and exits 0, so `p` is empty and the repair targets `/` again (read,
`:73`). Claude Code records an absolute `installPath` (`frame/design.md`
G3), so this shape is also outside the flow and a limit by G5's reasoning.
No sentence of the skill names it. Third, S8 at `frame/design.md:58` cites
*Scope* 6f as its check. 6f holds the block's half of the scenario, and no
case holds the half that says step 2b's table stops with no repair. The
crafter's close says so too. Without that pin the `&&` and its case still
keep the block from printing a repair to `/`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the new case holds on the ubuntu and Windows legs (`frame/questions.md` Q2). Run 41935909883 of the `tests` workflow concluded `success` at f8ed5efc, before 9ec4d8e0 (executed, `gh run view`), so no leg has run the new case. This round ran it on macOS alone | `tests/behaviour/test_update_reads_the_config_directory_in_use.py:118-128`, `gaps.md:7` | the orchestrator, by a run of the `tests` workflow on the branch at HEAD |
| Whether a session's Bash call inherits `CLAUDE_CONFIG_DIR` from the Claude Code process that started it | `gaps.md:8` | the orchestrator, by the measurement `gaps.md` names |
| Whether Q1's default, an issue for the class (filed as #1367 by `frame/plan.md:43`), stands | `frame/questions.md:15` | the owner |
| The full suite, the repository-wide lint and the format check at HEAD. The suite's `unverified` label in `gaps.md:9` is honest: nothing in the range claims the full suite passed, and the crafter's 159 passed names the modules it ran. This round leaves nothing open, so what comes due is the orchestrator's broad run and then the sealer's spawn | `gaps.md:9` | the orchestrator's broad run of the `Broad gate` row in `seal/config.md` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_old_block_leaves_through_update.py -q -rs -p no:xdist` | 17 passed, none skipped, exit 0 |
| `bin/test tests/behaviour/test_release_hygiene.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist -k "test_update_reads_the_installed_copy_before_it_summarises or test_update_shows_what_changed_from_the_github_releases or line_wrap or wrap"` | 49 passed, 31 deselected, exit 0 |
| `bin/seal mutate skills/update/SKILL.md --replace 'installed_plugins.json") &&' 'installed_plugins.json")' --tests "bin/test tests/behaviour/test_update_reads_the_config_directory_in_use.py -q -p no:xdist"` | `red`, exit 0: 1 failed, 4 passed, the failure being the new case at `assert 0 != 0` with the `rsync` into `/` in its output |
| `bin/seal layout --pairs tests/behaviour/test_update_reads_the_config_directory_in_use.py` | 1 file read, 0 pairs, exit 0 |
| `diff` of `frame/design.md:71-72` against `skills/update/SKILL.md:73-74`, and of `:65` against `:53` | exit 0 both |
| `git grep -n -F` on `cannot be read` and on `exits non-zero`, outside the round records | `changelog.md:3`, `skills/update/SKILL.md:69`, `frame/design.md:36`, `:58`, `:68`, and unrelated scripts |
| `gh run view 41935909883 --json headSha,conclusion,workflowName` | `tests`, `success`, at f8ed5efc |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.32.2 --root <the checkout> --worktree`, with this record written | exit 0; it names only the gate record and `guarantee.md` as not yet written |
| `bin/test tests/text/test_the_record_is_written_in_words.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist`, with this record written | 50 passed, exit 0 |

`git diff --quiet` exited 0 after the `bin/seal mutate` run, so the skill
was restored (executed). This round made no probe file.
