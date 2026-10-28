# Review round 2: 1793201097-two-environment-variables-still-carry-the-old-brand

target: a589145d, fixes 99c1649a..a589145d

## Findings

### 1. `gaps.md` records the option's description as a divergence from the frame, and the frame now quotes the manifest's text word for word

severity: should
location: `seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/gaps.md:13`
evidence: read `seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/gaps.md:13`, `seal/threads/1793201097-two-environment-variables-still-carry-the-old-brand/frame/design.md:80`, `.claude-plugin/plugin.json:25`
verdict: fixed 37d07f13

The row's *Spec says* cell states, in the present tense, that
`frame/design.md` *Data and interfaces* says "Left empty, the system locale
decides." Since `a589145d` that sentence is gone from the frame. Line 80 now
holds the manifest's description, and a comparison of the two strings found
the manifest's text inside line 80 unchanged (executed, a `python3` read of
both files). So the row states a divergence that no longer exists. The
sealer's step 4 reads the spec and the build against each other, and the
next reader of this memo is told the manifest departs from the frame. Both
would find a quote the frame does not hold.

The unit is this row, which `3bee2ec4` added for `round-1#1`. It was true
at that commit. The defect came from `a589145d`, the orchestrator's commit
that folded round 1 into the frame. That commit rewrote `frame/design.md:80`
and left this row, which stood on the old sentence. So contract rule 19 is
the rule it breaks: a change removes, in the same commit, what stood on the
fact it amends. The fold is not a fix pass's commit, so the finding carries
neither a `regression:` nor a `reopens:` line. The close of `round-1#1` holds
(see `## Confirmations`).

The rest of this class was enumerated with `git grep -n -i "system locale
decides"` over the work item (executed). `changelog.md:3` describes the
locale only with neither value set, which is true. `trail/rounds/round-1.md`
quotes the old text as what it found at `958f2f3e`, its target.
`trail/phases/phase-2.md:90-96` states the frame as it stood when phase 2
built `b1df3266`, the commit its own table names. Each of the three is true at
the commit it names. Only the `gaps.md` row speaks of the frame as it is now.

The fix deletes the row. Its history is already in `round-1#1` and in
`a589145d`, so a reworded row would state the same fact a second time.

```diff
-| The option's description | `frame/design.md` *Data and interfaces*: "Left empty, the system locale decides." The manifest says "Left empty, the variable SPECSEAL_LANG decides through 0.24.x, then the system locale.", and S5's case asserts the description names `SPECSEAL_LANG` | The manifest's text, from `trail/rounds/round-1.md` finding 1 | `hooks/worktree-guard.py#_lang` reads `SPECSEAL_LANG` before the locale wherever the option is empty. The description is the help text Claude Code shows where a person sets the option, in its dialog and in `/config`, and the README that states the fallback is not shown there. The frame's text told the person the fallback exists for, the owner with `SPECSEAL_LANG=ko` and an `en_US.UTF-8` locale, that an empty option gives English. The next minor release removes the clause and its assertion with the read |
```

answer: The orchestrator, whose fold at `a589145d` left the row, deleted it as the diff above gives at `37d07f13`; `bin/seal unverified` on `gaps.md` exits 0 after. No fix pass ran for this finding, so the orchestrator writes both its lines.

## Confirmations

confirms: round-1#1
The close holds. `.claude-plugin/plugin.json:25` reads "Left empty, the
variable SPECSEAL_LANG decides through 0.24.x, then the system locale." That
matches `hooks/worktree-guard.py:248-256`: the option first, then
`SPECSEAL_LANG`, then `LC_ALL` and `LANG` (read). The fix pass claimed that
S5 pins the clause. `tests/behaviour/test_chain_hooks_hardening.py:186`
asserts it, and a probe that put the frame's old sentence back turned the case
red on that line (executed, `## Probes`). The pin cannot quietly outlive the
read either. `tests/censuses.py:1029-1036` keeps `SPECSEAL_LANG` only until
the next minor release removes that entry with the read. Once the entry goes,
`tests/censuses.py#old_names` flags every living line that still spells the
name, and the description and the assertion are two of them (read,
`tests/censuses.py:1086-1110`). Nothing still tells a person what an empty
option does without the fallback. `git grep -n -i` for `SPECSEAL_LANG`, "left
empty", "system locale", "비워" and "로케일" over the tree outside
`seal/threads/` and `changelog/0.*` found the manifest, both README rows
(`README.md:287`, `README.ko.md:280`), the `_lang` docstring and comment, the
census comment, the conftest comment and the tests (executed). Each of them
names the fallback, or describes the variable the suite sets. The fragment at
`changelog.md:3` names it too (read). `grep -n -i` for "language", "언어" and
"locale" in `hooks/worktree-guard.py` found no prompt that tells a person how
the language is chosen (executed).

confirms: round-1#2
The close holds. `tests/behaviour/test_chain_hooks_hardening.py:181-186`
checks the option's fields only where `userConfig` declares it. I re-ran the
fix pass's probe from its answer on three extracts of `a589145d`. With the
declaration and the guard's read both removed, the case passed. With only the
declaration removed, it failed on
`assert {'WORKTREE_GUARD_LANGUAGE'} == set()`. With the description clause
reverted, it failed on the description assertion (all executed, `## Probes`).
So the docstring's last sentence is now true: the case is red after the guard
leaves and before its option leaves, and it passes again once both are gone. A
missing declaration is still refused while the guard reads the option. The
crafter's seven `seal mutate` mutants are its own account and were not re-run.
The three probes above cover the paths the finding named.

confirms: none
The fourth divergence row, `gaps.md:14`, states a true divergence.
`frame/design.md:65` (S5) still says the manifest "declares
`worktree_guard_language` with `type`, `title` and `description` and no other
field" with no condition. `a589145d` changed only line 80 of the frame (read,
the fix diff). The case checks those fields only where the option is declared.
The row's grounds hold. `frame/plan.md:53-55` says the case is red "until the
option goes with it", and the probe without the declaration or the read shows
that the old check could not pass again, while the new one does (executed).

confirms: none
The fold is otherwise sound. The quoted description at `frame/design.md:80`
holds the manifest's string, so the phase 2 row of `frame/plan.md:77`,
"exactly as `frame/design.md` *Data and interfaces* gives it", is true of the
manifest again (executed, a `python3` comparison of the two files). No other
sentence of `frame/design.md` or `frame/plan.md` states what an empty option
does (read).

confirms: none
Narrow runs at `a589145d` hold. The 16 modules under `tests/` that
`git grep -l` finds naming `plugin.json` or `test_chain_hooks_hardening`
passed: 1426 passed, 4 skipped, exit 0. `claude plugin validate .` exited 0
with only the `CLAUDE.md` warning that `gaps.md:12` already records.
`bin/seal layout --check` and `bin/seal rules --check` each exited 0 (all
executed, `## Probes`).

confirms: none
The suite's label is honest. `gaps.md:20` labels the full suite, the lint
and the typecheck as unverified, with the orchestrator as the answerer (read).

Carried from round 1 and not re-established: what the plugin manifest
reference *User configuration* says about `userConfig`, the dialog, `/config`
and `CLAUDE_PLUGIN_OPTION_<KEY>`. This round did not re-read the reference;
nothing in the fix range changes what it is cited for.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The three Claude Code behaviours round 1 could not judge: loading on a version from before `userConfig`, the dialog on an update, and the variable reaching the hook process. Carried as round 1 left them; the fix range changes none of them | `trail/rounds/round-1.md:164-166` | the owner, as each row there names |
| The full suite, the repository-wide lint and the typecheck | the branch | the orchestrator, at its one `seal gate` run (contract rule 2) |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 16 modules `git grep -l -e plugin.json -e test_chain_hooks_hardening -- tests/` lists | 1426 passed, 4 skipped, exit 0 |
| `claude plugin validate .` at the worktree root, Claude Code 2.1.312 | exit 0, `Validation passed with warnings`, the one `CLAUDE.md` warning |
| `bin/seal layout --check` | 160 files read, 0 refused, exit 0 |
| `bin/seal rules --check` | all 266 check lines in 55 rule files hold, exit 0 |
| `git archive a589145d` into three extracts under `<scratchpad>/1793201097-two-environment-variables-still-carry-the-old-brand/round-2/`, each edited with the Edit tool, then `pytest -q -p no:xdist -p no:cacheprovider` on `test_every_option_the_manifest_declares_is_one_a_hook_reads` in each | description clause reverted: exit 1 on the `SPECSEAL_LANG` assertion; `userConfig` and the guard's option read removed: exit 0; `userConfig` removed alone: exit 1 on `assert {'WORKTREE_GUARD_LANGUAGE'} == set()`. The extracts were removed |
| `python3` comparison of the description in `.claude-plugin/plugin.json` with `frame/design.md` line 80 | the manifest's string stands in line 80 |
| `git grep -n -i` for `SPECSEAL_LANG`, "left empty", "system locale", "비워" and "로케일" outside `seal/threads/` and `changelog/0.*`; `git grep -n -i "system locale decides"` over the work item | hits only at the lines `## Confirmations` and finding 1 list |
