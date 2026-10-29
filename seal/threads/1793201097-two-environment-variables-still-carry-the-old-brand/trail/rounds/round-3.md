# Review round 3: 1793201097-two-environment-variables-still-carry-the-old-brand

target: 307f115b, fixes ffd75e0f..307f115b

## Findings

none

## Confirmations

confirms: round-2#1
The close holds. The finding asked that the `gaps.md` row *The option's
description* be deleted, and `37d07f13` deletes it. The line that commit
removes is the same line as the one the finding's fenced diff removes
(executed, a shell comparison of the two). `gaps.md` now holds no row of that
name (executed, `grep -c` printed 0). The frame no longer differs from the
manifest here. The `userConfig` block that `frame/design.md` *Data and
interfaces* quotes parses equal to the manifest's `userConfig` (executed, a
`python3` comparison of the two objects), so no row is owed in its place.
`37d07f13` changes `gaps.md` alone, the path the finding's `location:` names,
and `307f115b` changes only the `verdict:` and `answer:` lines of
`trail/rounds/round-2.md` (executed, `git show --name-only`; read, the fix
diff). The answer claims that `bin/seal unverified` on `gaps.md` exits 0
after the deletion. It does: exit 0, with 1 overview, 3 open rows, 0 closed
and 0 unreadable (executed). The answer also says that the orchestrator wrote
both lines because no fix pass ran. `docs/the-review-record.md` *The fix pass
writes two lines per finding* closes a correction to a record as
`fixed <commit>` with the record's path on `location:`, and both conditions
hold here. The rule names no other writer of the two lines.

confirms: none
Nothing else stood on the two facts the fix range and its fold changed. One
fact is the sentence `a589145d` replaced at `frame/design.md:80`. The other is
the row `37d07f13` deleted. I enumerated every sentence of the work item that
names the description, a divergence, `gaps.md`, *Data and interfaces*,
"exactly as", "left empty" or "system locale decides" (executed, `grep -n -i -r`
over the work item). Each hit is listed below with why it stands.

- `trail/phases/phase-2.md:90-96` quotes the frame's old sentence. The phase
  record names its commit, `b1df3266`, and the frame it built against,
  `0c451b8c` (line 10). The sentence is true at both.
- `trail/rounds/round-1.md:19-20` quotes the old sentence as it stood at that
  round's target, `958f2f3e`. The answer at `trail/rounds/round-1.md:51` says
  "`gaps.md` records the departure ... as a divergence". That was true at
  `3bee2ec4`, the commit that added the row and the one its verdict names.
  `docs/the-review-record.md` *Every round file stays* keeps a round file as
  written, and a later fix pass writes only its own two lines.
- `trail/rounds/round-2.md:90` names "the fourth divergence row, `gaps.md:14`"
  and `:116` names `gaps.md:20`. Both are true at `a589145d`, that round's
  target. At `307f115b` the same rows stand at `gaps.md:13` and `gaps.md:19`.
  The `target:` line is what dates them, so they are no finding.
- `frame/plan.md:77` says the manifest declares the option "exactly as
  `frame/design.md` *Data and interfaces* gives it". This is true at
  `307f115b`, as the comparison above shows.
- `frame/design.md:26-27`, `:85-88` and `:104-109` speak of the option's shape
  and cost. None of them says what an empty option does, so line 80 is the
  only frame sentence that does (read).
- `changelog.md:3` does not quote the description. It names the
  `SPECSEAL_LANG` fallback and its end (read).

confirms: none
The three divergence rows that remain in `gaps.md` state true divergences at
`307f115b`. The first row, `gaps.md:11`, quotes S5 as it stands at
`frame/design.md:65` (read). The second row, `gaps.md:12`, quotes "prints
`Validation passed`", which `frame/design.md:65` and `frame/plan.md:77` both
still say (read). `claude plugin validate .` at the worktree root exited 0 and
printed `Validation passed with warnings`, and its one warning was the
`CLAUDE.md` warning the row names (executed, Claude Code 2.1.312). The third
row, `gaps.md:13`, says S5 asks for the fields with no condition, and
`frame/design.md:65` still does. The case checks them only where the option is
declared, at `tests/behaviour/test_chain_hooks_hardening.py:181-186` (read).
Its grounds rest on round 2's three extract probes, which are carried and were
not re-run. The fix range touches neither the case nor the frame row.

confirms: none
`gaps.md` *Fed back into the spec*, which reads `none`, stays true after the
fold. `templates/records/sdd-gaps.md` and `skills/implement/SKILL.md` *The
closing memo*, item 4, define that section as the clauses this work added,
marked as inferred during implementation. The sentence at `frame/design.md:80`
was not inferred by the build. It came from a review finding, `round-1#1`, and
the orchestrator folded it into the frame. `skills/implement/orchestration.md`
says a decision made after the frame is committed is folded in place into the
frame, and it asks for no `gaps.md` entry (read).

confirms: none
No shipped text states a fact the folds made false. The fix range changes no
file outside the work item's directory (executed, `git show --name-only`).
`git grep -n -i` for `SPECSEAL_LANG`, "left empty", "system locale", "비워" and
"로케일" outside `seal/threads/` and `changelog/0.*` finds these lines:
`.claude-plugin/plugin.json:25`, `README.md:287`, `README.ko.md:280`,
`hooks/worktree-guard.py:242-252`, the S5 docstring and assertion at
`tests/behaviour/test_chain_hooks_hardening.py:168-186`, the conftest comment
at `tests/conftest.py:350`, and the cases in `tests/hooks/test_worktree_guard.py`
(executed). Each of them names the fallback, says the author's machine exports
the variable, or sets it for a case. Two further hits,
`skills/code-review/SKILL.md:124` and `tests/hooks/test_config.py:916`, use
"left empty" for other things. Nothing under `docs/` speaks of the guard's
language or of the locale it reads (executed, `git grep -n -i` for "korean",
"한국어", "locale", `LANG` and `ko` over `docs/`).

confirms: none
Narrow runs at `307f115b` hold (all executed, `## Probes`). `bin/test -q`
passed over three groups of modules: the 16 that `git grep -l` finds naming
`plugin.json` or `test_chain_hooks_hardening` under `tests/`, and the two that
read `gaps.md` rows, `tests/behaviour/test_unverified_rows_close.py` and
`tests/skills/test_unverified_check.py`. The result was 1797 passed and 4
skipped, exit 0. `bin/seal layout --check` exited 0 and `bin/seal rules --check`
exited 0.

confirms: none
The suite's label is honest. `gaps.md:19` labels the full suite, the lint and
the typecheck unverified, with the orchestrator as the answerer (read).

Carried from rounds 1 and 2 and not re-established: what the plugin manifest
reference *User configuration* says about `userConfig`, the dialog, `/config`
and `CLAUDE_PLUGIN_OPTION_<KEY>`; and round 2's extract probes for the grounds
of the `gaps.md:13` row. Nothing in the fix range changes what either is cited
for.

This round leaves nothing open. What comes due next is the orchestrator's one
`seal gate` run over the branch, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The three Claude Code behaviours round 1 could not judge: loading on a version from before `userConfig`, the dialog on an update, and the variable reaching the hook process. Carried as round 1 left them; the fix range changes none of them | `trail/rounds/round-1.md:164-166` | the owner, as each row there names |
| The full suite, the repository-wide lint and the typecheck | the branch | the orchestrator, at its one `seal gate` run (contract rule 2) |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 16 modules `git grep -l -e plugin.json -e test_chain_hooks_hardening -- tests/` lists, plus `tests/behaviour/test_unverified_rows_close.py` and `tests/skills/test_unverified_check.py` | 1797 passed, 4 skipped, exit 0 |
| `bin/seal layout --check` | 160 files read, 0 refused, exit 0 |
| `bin/seal rules --check` | all 266 check lines in 55 rule files hold, exit 0 |
| `bin/seal unverified` on the work item's `gaps.md` | exit 0; 1 overview, 3 open, 0 closed, 0 unreadable |
| `claude plugin validate .` at the worktree root, Claude Code 2.1.312 | exit 0, `Validation passed with warnings`, the one `CLAUDE.md` warning |
| shell comparison of the line `37d07f13` removes from `gaps.md` with the line the fenced diff of `round-2#1` removes | identical, exit 0 |
| `grep -c "The option's description"` on `gaps.md` | 0, exit 1 |
| `python3` comparison of the `userConfig` block quoted in `frame/design.md` with the one in `.claude-plugin/plugin.json` | equal, exit 0 |
| `git show --name-only` for `37d07f13` and `307f115b` | `gaps.md` and `trail/rounds/round-2.md` only |
| `grep -n -i -r` over the work item for the description, a divergence, `gaps.md`, *Data and interfaces*, "exactly as", "left empty" and "system locale decides" | hits only at the lines the second entry of `## Confirmations` lists, the rows of `gaps.md` and the round records' own text |
| `git grep -n -i` for `SPECSEAL_LANG`, "left empty", "system locale", "비워" and "로케일" outside `seal/threads/` and `changelog/0.*`; the same for "korean", "한국어", "locale", `LANG` and `ko` over `docs/` | hits only at the lines the fifth entry of `## Confirmations` lists; none under `docs/` on the guard's language |
