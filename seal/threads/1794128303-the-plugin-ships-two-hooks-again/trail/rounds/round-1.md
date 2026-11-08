# Review round 1: 1794128303-the-plugin-ships-two-hooks-again

```seal
target: 471353125 against release/v0.35.0
```

The round reviewed the branch against `release/v0.35.0` (equal to `main` at
`59b09ba5c`), at `471353125`. No earlier round exists, so no fact is
carried; every coordinate below was opened at the target. The work item's
records that state the present were read whole at the target: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md` and `pr.md`, then the three phase records, against issue #1430
(no comments). The issue's *Done when* list and the frame's *Scope* items 1
to 4 were the compliance axes. The quality axes were the comparison table's
rows, plus three of this change's own: the hook commands' exit path where
their interpreter or script fails, what the pull request body carries
(`skills/code-review/scripts/pr_body.py:9-17`), and the fallback open of the
core where the hook printed nothing.

## Findings

### 1. The `Stop` command no longer exits 0 where its script fails to load, and the shipped text says it does

```seal
severity: should
location: `skills/verify/scripts/seal_stamp.py:1554-1561`, `CONTRIBUTING.md:461-462`, `README.md:313`, `README.ko.md:312`, `docs/checks/the-stamp.md:90-92`, `docs/checks/the-stamp.md:157-158`, `skills/code-review/orchestration.md:531-533`, `skills/verify/scripts/seal_stamp.py:1006-1010`, `lib/launch.py:35-36`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/changelog.md:3`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:23`, `tests/skills/test_seal_stamp.py`
evidence: executed the `Stop` command of `hooks/hooks.json` under `/bin/sh` with `CLAUDE_PLUGIN_ROOT` at a scratch root whose `skills/verify/scripts/seal_stamp.py` raises at load and `PATH=/usr/bin:/bin`: exit 127, stderr the traceback and `/bin/sh: py: command not found`; read `skills/verify/scripts/seal_stamp.py:1554-1561`, `skills/verify/scripts/seal_stamp.py:1613-1630`, `hooks/core-start.py:47-65`, and the removed `release/v0.35.0:tests/skills/test_seal_stamp.py:2288-2305`
```

Why it matters: the launcher wrapped `seal_stamp.py` in `runpy.run_path`
inside `except BaseException` and then `sys.exit(0)`, so its `Stop` entry
exited 0 whatever the script did. The removed case
`test_refuses_to_fail_where_the_script_its_launcher_runs_fails` held that for
a script that raises. The new entry hands `seal_stamp.py` to `python3`
directly, and nothing takes the launcher's place. A `python3` that starts but
cannot load the file exits 1. The shell then runs the `py -3` half, and on a
machine with no `py`, as a stock macOS or Linux has none, the command exits
127 with `py: command not found` at the end of every turn in every
repository. The failure direction stays allow, since 127 is not the
harness's exit 2. But the shipped text says otherwise in each place below:
"Each script exits 0 whatever happens, so the fallback is reached only when
the first interpreter could not start" (`CONTRIBUTING.md:461-462`), "Each
exits 0 whatever happens" (`README.md:313`, `README.ko.md:312`), "`--stop`
exits 0 whatever happens ... so the `py -3` half runs only where `python3`
could not start" (`docs/checks/the-stamp.md:90-92`), "Nothing draws, and
nothing says so, where the `python3` the harness finds cannot load
`seal_stamp.py`" (`docs/checks/the-stamp.md:157-158`, and the same claim at
`skills/code-review/orchestration.md:531-533` and
`skills/verify/scripts/seal_stamp.py:1006-1010`), `lib/launch.py:35-36`, and
the fragment's "each script exits 0 whatever happens" (`changelog.md:3`). The
frame's own *Grounding* row on `CONTRIBUTING.md` *What a change to a gate
must carry* (`frame/design.md:23`) states that each hook "exits 0 whatever it
meets", and the build holds that for `hooks/core-start.py` alone, whose
`__main__` catches its own import (`hooks/core-start.py:61-65`, held by
`tests/hooks/test_core_start.py#Test_main::test_refuses_to_fail_where_its_library_is_gone`).

Phase 2 claimed that the launcher's two failure cases could go because
"`--stop` catches every failure in `main`, which
`Test_main.test_stop_says_nothing_and_exits_0_whatever_it_meets` already
holds". What the code does: `seal_stamp.py:1555-1558` catches what
`drawn_at_stop` raises and nothing else. The write at `:1560-1561`,
`pick_shape` and the stream loop in the `__main__` block at `:1613-1630`, and
the module's own load all stand outside that catch. The case the claim names
calls `stamp.main` in-process, so it cannot see a load failure.

The parse of the four scripts under Python 3.7 and 3.8 grammar succeeded
(executed, `## Probes`), so the load failure needs a `python3` older than
those or a later release's defect. That is rare, and its cost is a visible
error line at every turn rather than a stopped turn, which is why this is a
`should` and not a `must`. The fix is one of two routes, and the frame's
owner picks. Route A keeps the code and makes the text true; it is the one
pasted below, and it reaches each statement listed in `location:`. Route B
gives the `Stop` entry the launcher's catch back. That is a short script
under `hooks/` that runs `seal_stamp.py --stop` inside `except
BaseException` and exits 0. It is not the copy of the draw loop that
`frame/plan.md` *Alternatives considered* rejected, but it changes
`HOOK_FILES` in `tests/behaviour/test_chain_hooks_hardening.py`, *Scope*
item 4's list and the floor derivation, and it owes the removed case back
against the new script. Either route also owes the frame row at
`frame/design.md:23`, which is the orchestrator's to fold, and a pin for each
person-facing sentence it rewrites (contract rule 14). The snippet below
leaves those to the fix pass.

```text
CONTRIBUTING.md:461-462
  old: Each script exits 0 whatever happens, so the fallback is reached
       only when the first interpreter could not start.
  new: Each script exits 0 whatever it meets once its interpreter has
       loaded it, so the fallback is reached where the first interpreter
       could not start or could not load the script; where it could not
       load it and no `py` stands, the command exits non-zero.

README.md:313
  old: Each exits 0 whatever happens.
  new: Each script exits 0 whatever it meets once `python3` has loaded it.

README.ko.md:312
  old: 두 스크립트 모두 무슨 일이 있어도 0 으로 끝납니다.
  new: 두 스크립트 모두 `python3` 가 불러온 뒤에는 무슨 일이 있어도 0 으로 끝납니다.

docs/checks/the-stamp.md:90-92
  old: `--stop` exits 0 whatever happens, since a `Stop` hook that exits 2
       keeps the turn going, so the `py -3` half runs only where `python3`
       could not start.
  new: `--stop` exits 0 whatever it meets once `python3` has loaded the
       file, since a `Stop` hook that exits 2 keeps the turn going, so the
       `py -3` half runs only where `python3` could not start or could not
       load it.

docs/checks/the-stamp.md:157-158
  old: Nothing draws, and nothing says so, where the `python3` the harness
       finds cannot load `seal_stamp.py`, or where the main session's
       working directory is outside the clone the stamp was queued in.
  new: Nothing draws, and nothing says so, where the main session's working
       directory is outside the clone the stamp was queued in. Nothing draws
       either where the `python3` the harness finds cannot load
       `seal_stamp.py`, and there the command exits non-zero: its `py -3`
       half runs, and where no `py` stands the shell's `command not found`
       is what it prints.

skills/code-review/orchestration.md:531-533
  old: the plugin's `Stop` hook draws nothing and says nothing where it
       cannot: a `python3` that cannot load `seal_stamp.py`, or a working
       directory outside the clone.
  new: the plugin's `Stop` hook draws nothing where it cannot: a `python3`
       that cannot load `seal_stamp.py`, or a working directory outside the
       clone.

skills/verify/scripts/seal_stamp.py:1006-1010 (the comment over QUEUED)
  old: plugin's `Stop` hook draws nothing, and says nothing, where it cannot:
  new: plugin's `Stop` hook draws nothing where it cannot:

lib/launch.py:35-36
  old: each script `hooks/hooks.json` names exits 0 whatever happens,
  new: each script `hooks/hooks.json` names exits 0 whatever it meets once
       loaded,

seal/threads/1794128303-the-plugin-ships-two-hooks-again/changelog.md:3
  old: and each script exits 0 whatever happens.
  new: and each script exits 0 whatever it meets once `python3` has loaded it.
```

### 2. The pull request body states no failure direction and no prompt budget, which the issue's *Done when* asks for

```seal
severity: must
location: `seal/threads/1794128303-the-plugin-ships-two-hooks-again/pr.md:1-9`
evidence: read issue #1430 *Done when* (`gh issue view 1430`), `CONTRIBUTING.md` *What a change to a gate must carry*, `skills/code-review/scripts/pr_body.py:9-17`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:23`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/questions.md:16`; executed `grep -n -i "allow\|budget\|block\|failure direction"` over `changelog.md`, `pr.md`, `gaps.md` and `frame/questions.md` of the work item
```

Why it matters: issue #1430 lists "`CONTRIBUTING.md` *What a change to a
gate must carry* is answered in the pull request" under *Done when*. The
frame's *Grounding* row on that section (`frame/design.md:23`) commits the
pull request to "a failure direction, a prompt budget, the platforms not
tested and what each hook removes". The body is `pr.md` plus what `seal
pr-body` copies: the changelog fragment, the plan's `## Phases`, the phase
records' paths, the round and gate blocks, `gaps.md`'s two sections and the
table lines of `frame/questions.md` (`pr_body.py:9-17`). The platform not
tested reaches the body through the `Q1` row and `gaps.md` row 2, and what
each hook removes through the fragment's second and third items. The failure
direction and the prompt budget reach it nowhere. They stand in
`frame/design.md:23`, which the body does not copy, and in the bullet at
`frame/questions.md:16`, which is not a table line. The search for them over
the copied records found no hit. `pr.md` holds only quotes of records
(`skills/code-review/orchestration.md:389-396`), so the repair is two quotes.
The second one quotes the sentence finding 1 disputes: whatever wording the
fold of finding 1 leaves in that row is what the quote copies. `pr.md` is the
orchestrator's to repair.

```markdown
- "The failure direction, the prompt budget and the platform not tested, for `CONTRIBUTING.md` *What a change to a gate must carry*: allow, zero questions, Windows." (`frame/questions.md`, the bullet on the failure direction)
- "The failure direction of both hooks is allow: each exits 0 whatever it meets and blocks nothing, so a wrong hook costs a missing core or a missing stamp and never a stopped turn." (`frame/design.md` *Grounding*, the row on `CONTRIBUTING.md` *What a change to a gate must carry*)
```

### 3. The frame names the cases two acceptance rows verify by the ids they replaced

```seal
severity: should
location: `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:51`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:52`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:69`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:73`
evidence: read `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:51-52`, `:69`, `:73`, `tests/behaviour/test_chain_hooks_hardening.py:28`, `tests/skills/test_seal_stamp.py:2320-2337`; executed `grep -n "test_the_plugin_registers\|test_accepts_a_launcher_the_harness"` over the work item's frame files
```

Why it matters: the scenario *The registration is exactly two entries*
(`frame/design.md:69`) is verified by "the case *Scope* item 1 names", and
*Scope* item 1 (`:51`) names
`tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_no_hook_and_writes_none_into_git`,
which does not exist at the target. The case is
`#test_the_plugin_registers_two_hooks_and_writes_none_into_git`
(`tests/behaviour/test_chain_hooks_hardening.py:28`). The scenario *The stamp
is drawn by the plugin's hook* (`:73`) is verified by "the case *Scope* item
2 names", and item 2 (`:52`) names only the replaced
`Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`,
then says "two cases replace" it and describes one. The two cases are
`Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and
`Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`
(`tests/skills/test_seal_stamp.py:2320-2337`). Phase 1 and phase 2 named
these ids in their records, and the folds of their hand-backs did not carry
them into the frame, as the fold of phase 3 did for item 3's renamed case.
The sealer re-runs claims from the acceptance rows, and an id that resolves
to nothing costs it a search. The frame is the orchestrator's to fold. The
`## Removes` rows on the same cases (`:100`, `:113`) already name the
replacement by role and need no change.

```text
frame/design.md:51 (Scope item 1)
  old: `tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_no_hook_and_writes_none_into_git` becomes the case that reads `hooks/hooks.json` and holds:
  new: `tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_no_hook_and_writes_none_into_git` becomes `#test_the_plugin_registers_two_hooks_and_writes_none_into_git`, which reads `hooks/hooks.json` and holds:

frame/design.md:52 (Scope item 2)
  old: two cases replace `Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`: it reads the `Stop` command
  new: two cases replace `Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`, `Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and `Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`: the first reads the `Stop` command
```

## Confirmations

What matched: *Scope* item 1's registration. `hooks/hooks.json:1-25` holds
exactly a `Stop` entry with no matcher and a `SessionStart` entry matched to
`startup|clear|compact`, each one command in the `python3 … || py -3 …`
shape under `${CLAUDE_PLUGIN_ROOT}`. `.claude-plugin/plugin.json` declares no
`hooks` key, and `git ls-files hooks/` lists `hooks/core-start.py` and
`hooks/hooks.json` alone (executed). `hooks/` is not `export-ignore` in
`.gitattributes`, so it reaches `dist` (read).

What matched: `lib/core.py:126-132` returns "" where `optin.opted_in(cwd)` is
false. `rendered` (`:106-123`) prints the header without a digest, the core
below its frontmatter and `START`, and `parse` is gone. The clone rule in
`origin` (`:79-91`) is the pre-0.33.0 shape (read against
`1ae24b1e0^:hooks/lib/core.py`). `hooks/core-start.py:31-65` exits 0 on every
path, including its own import of `core`.

What matched: the phase 3 claim that `skills/implement/SKILL.md`'s
description is the first fourteen lines of
`1ae24b1e0^:skills/implement/SKILL.md` (executed: `diff` exit 0).

What matched: the phase records' claims that `seal rules --check` and `seal
layout --check` exit 0 (executed at the target: both 0), and that `seal
layout --pairs` names no pair among the tests the diff adds (executed: the
two pairs in the touched modules, in `test_payload_meter.py#Test_imports_of`
and `test_seal_stamp.py#Test_main`, both stand at the base).

What matched: the acceptance greps. `git grep -n "agentic:start\|skills/start"`
outside `seal/threads/` lists the preset block's marker alone, and the
launcher grep lists the four kinds of line phase 2's record names (executed).

What matched: each of the six quotes in `pr.md` stands word for word, with
runs of whitespace collapsed, in the source its coordinate names: five in
`changelog.md` and one in `frame/plan.md` *Judgments of the run*, the prefix
row (executed).

What matched: `skills/update/SKILL.md` step 4b asks nothing and writes
nothing, and answers an empty data directory with `no data directory`, as
`frame/design.md` *Data & interfaces* states. The narrow run of its case
passed (executed, `## Probes`).

The hardening case's name,
`tests/behaviour/test_chain_hooks_hardening.py:28`
`test_the_plugin_registers_two_hooks_and_writes_none_into_git`, says "writes
none into git", and no assertion of it reads a git hook. The base's name
claimed the same, and the frame states no git-hook fact for it to hold.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the lint and the typecheck. This round ran eight modules only, and the suite is `unverified` at the target | the work item | the orchestrator, at its one broad run after the rounds settle |
| Whether Claude Code shows the person a `Stop` command's exit 127 and its stderr at each turn's end, which is finding 1's cost; no case runs the harness | `hooks/hooks.json:8` | the owner, at a session under the installed 0.35.0 |
| Whether the harness reads `hooks/hooks.json`, substitutes `${CLAUDE_PLUGIN_ROOT}` and puts the output in context whole, and whether the `py -3` half runs on Windows: `gaps.md` rows 1 and 2, `frame/questions.md` Q1 and Q2 | `hooks/hooks.json` | the owner, as those rows name |
| Whether a plain request makes the model open `skills/implement/orchestration.md` before its first edit: `gaps.md` row 5, `frame/questions.md` Q3 | `skills/implement/SKILL.md:1-14`, `lib/core.py:54-60` | the owner, at the first plain request under 0.35.0 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks tests/lib/test_core.py tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_seal_stamp.py tests/skills/test_payload_meter.py tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/lib/test_launch.py -q` | exit 0, 321 passed |
| the `Stop` command of `hooks/hooks.json`, run by `/bin/sh -c` with `CLAUDE_PLUGIN_ROOT` set to a scratch root under the round's scratch directory whose `skills/verify/scripts/seal_stamp.py` is `raise RuntimeError("a later release broke")`, `PATH=/usr/bin:/bin`, a `Stop` payload on stdin | exit 127; stdout empty; stderr the `RuntimeError` traceback, then `/bin/sh: py: command not found`. The scratch root was removed afterwards |
| `ast.parse(..., feature_version=(3, 7))` and `(3, 8)` over `skills/verify/scripts/seal_stamp.py`, `hooks/core-start.py`, `lib/core.py` and `lib/optin.py` | all eight parses exit 0 |
| `bin/seal rules --check`; `bin/seal layout --check`; `bin/seal layout --pairs` | 0; 0; 0, with no pair naming a test the diff adds |
| `git grep -n "agentic:start\|skills/start" -- . ':!seal/threads'` and the launcher grep of the scenario *No shipped file names the launcher* | the preset block's marker alone; the four kinds of line phase 2's record names |
| the six quotes of `pr.md`, each looked up in its named source with runs of whitespace collapsed | six found |
| `diff` of the first fourteen lines of `1ae24b1e0^:skills/implement/SKILL.md` and of the target's | exit 0 |
