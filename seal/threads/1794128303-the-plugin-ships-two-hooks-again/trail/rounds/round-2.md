# Review round 2: 1794128303-the-plugin-ships-two-hooks-again

```seal
target: 795905dca, fixes 471353125..795905dca
```

This is the verifying round. The code under review is the diff of round 1's
fixes, `471353125..795905dca`: `616d85851` (the `pr.md` repair), `d2b2bb558`
(the frame fold and the route-A judgment row), `db53d635a` (the fix pass),
`765be3b73` (a `gaps.md` row), `5ff17a76c` (round 1's close blocks) and
`795905dca` (the fold of the fix pass into the frame). Beside that diff the
round read the work item's records that state the present whole at
`795905dca`: `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, then the phase
records and `trail/rounds/round-1.md`.

Facts carried from round 1 and not re-derived: the coordinates of finding 1's
`location:` (each opened again at the target), the parse of the hook scripts
under Python 3.7 and 3.8 grammar, and the shape of `hooks/hooks.json`. The
fix diff leaves `hooks/` untouched and changes one comment line of
`skills/verify/scripts/seal_stamp.py` (executed: `git diff --stat
471353125..795905dca -- hooks/ skills/verify/scripts/seal_stamp.py`), so
none of those facts' checks failed. Round 1's executed probe for finding 1
was run again, and a second case was added beside it (`## Probes`).

The axes were the three closes, plus two of this diff's own: every
statement of what a hook command exits where its script fails, enumerated
by `git grep` over the tree rather than from round 1's list, and whether
each new pin fails against the text it replaced.

## Findings

### 1. Two statements of a hook command's exit where its script fails still over-claim: `hooks/core-start.py`'s docstring, and the frame's "neither exits 2"

```seal
severity: should
location: `hooks/core-start.py:15-17`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:23`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/pr.md:8`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/plan.md:68`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/questions.md:9`
evidence: executed `git grep -n -i "whatever happens\|whatever it meets\|could not start\|cannot start\|says nothing where\|nothing says so\|exits 0 once\|once loaded\|exits non-zero\|neither exits 2\|blocks nothing\|never stops a turn\|never a stopped turn"` over the tree; executed `python3 <absent path>` (exit 2) and `python3 <unreadable file>` (exit 2); executed the `Stop` command of `hooks/hooks.json` under `/bin/sh` with `PATH=/usr/bin:/bin` against a scratch root whose `seal_stamp.py` raises (exit 127) and against a root with no `seal_stamp.py` (exit 127, stderr `can't open file ... [Errno 2]` then `py: command not found`); read `hooks/core-start.py:13-17`, `skills/verify/scripts/seal_stamp.py:1554-1561`, `skills/verify/scripts/seal_stamp.py:1613-1630`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:23`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:51`
reopens: round-1#1
```

Why it matters: round 1's close says every statement of the fact now says the
command exits 0 once its script has loaded, and non-zero where `python3`
cannot load it and no `py` stands. That holds for each statement round 1's
`location:` listed. The fix pass's answer says it worked from that list
("Each statement the location lists outside the frame"). It names no search
of its own, and two statements of the same fact stand outside the list.

The first is `hooks/core-start.py:15-17`. It says the script "exits 0 on every
path, printing nothing where it fails, so the `py -3` half of its command in
`hooks/hooks.json` runs only where `python3` could not start". That is the
old sentence, the one the fix rewrote everywhere else. A `python3` that starts
but cannot load the file exits non-zero, and the `py -3` half runs. The frame
already says so for this script: `frame/design.md:51` reads "exits 0 on every
path once loaded ... so the `py -3` half runs only where `python3` could not
start or could not load it". The search for "could not start" lists this
docstring, and no case pins it (executed: the same search over `tests/`).

The second is a claim the fold at `d2b2bb558` wrote into the frame's failure
direction row (`frame/design.md:23`), which `pr.md:8` quotes into the pull
request body: "neither exits 2, so neither blocks a turn", and the `Stop`
command exits "non-zero, which is not exit 2, where no interpreter loads it".
Python exits 2 when it cannot open the file it is handed (executed: an absent
path and an unreadable file both exit 2). On macOS and Linux the `py` half
then fails and the command exits 127, as both probes show. Where `py`
stands, which is the machine the `py -3` half exists for, `py -3` hands the
same file to Python, and the command exits with Python's 2. The `py`
launcher passing its child's exit code through is the one link this round
could not run, since no machine here runs Windows (`## Not judged`). A
`Stop` hook's exit 2 keeps the turn going (`docs/checks/the-stamp.md:91`).
So the row's "never a stopped turn" holds only where no `py` stands. The
judgment row at `frame/plan.md:68` rests route A on the same grounds: "its
cost is a non-zero exit that is not exit 2, so no turn stops".

The row also says "the `Stop` command exits 0 once `python3` has loaded
`seal_stamp.py`". The fix pass's own answer says the write of the drawing at
`seal_stamp.py:1560-1561` stands outside the catch at `:1555-1558`, and
chose "whatever drawing the stamp meets" for that reason. `frame/questions.md:9`
("each script, once loaded, exits 0") says the same as the row. The snippet
below uses the fix pass's wording in both. `lib/launch.py:36` and
`docs/checks/the-stamp.md:92` carry the same gap for a failed write to the
harness's pipe. No agent acts differently on it, so this round opens nothing
for those two.

The fix below takes round 1's route A, which keeps the code and makes the
text true. The other route changes the command so that no exit 2 reaches the
harness. That changes the two-halves shape
`tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_two_hooks_and_writes_none_into_git`
holds, and the frame's owner picks between them. The docstring is the fix
pass's. The frame rows and the `pr.md` quote are the orchestrator's, and the
quote copies whatever wording the fold of `design.md:23` leaves.

```text
hooks/core-start.py:15-17
  old: and a compaction drops it. It writes nothing, and it exits 0 on every path,
       printing nothing where it fails, so the `py -3` half of its command in
       `hooks/hooks.json` runs only where `python3` could not start.
  new: and a compaction drops it. It writes nothing, and once its interpreter
       has loaded it, it exits 0 on every path, printing nothing where it
       fails, so the `py -3` half of its command in `hooks/hooks.json` runs
       only where `python3` could not start or could not load this file.

frame/design.md:23 (the Grounding row on CONTRIBUTING.md *What a change to a gate must carry*)
  old: The failure direction of both hooks is allow: neither exits 2, so
       neither blocks a turn. Once `python3` has loaded it,
       `hooks/core-start.py` exits 0 on every path, its import of `lib/`
       among them; the `Stop` command exits 0 once `python3` has loaded
       `seal_stamp.py`, and non-zero, which is not exit 2, where no
       interpreter loads it. A wrong hook costs a missing core or a missing
       stamp and never a stopped turn.
  new: The failure direction of both hooks is allow, with one exception:
       neither command exits 2, except where `py` stands and the script file
       cannot be opened. Once `python3` has loaded it, `hooks/core-start.py`
       exits 0 on every path, its import of `lib/` among them, and
       `seal_stamp.py --stop` exits 0 whatever drawing the stamp meets. Where
       `python3` cannot load the script, the command exits non-zero. Where no
       `py` stands, the shell's 127 is that exit. Where `py` stands and the
       script file cannot be opened, the exit is Python's 2, and from the
       `Stop` command that exit keeps the turn going. A wrong hook costs a
       missing core or a missing stamp, and a kept turn only in that last case.

pr.md:8
  old: - "The failure direction of both hooks is allow: neither exits 2, so neither blocks a turn." (`frame/design.md` *Grounding*, the row on `CONTRIBUTING.md` *What a change to a gate must carry*)
  new: - "The failure direction of both hooks is allow, with one exception: neither command exits 2, except where `py` stands and the script file cannot be opened." (`frame/design.md` *Grounding*, the row on `CONTRIBUTING.md` *What a change to a gate must carry*)

frame/plan.md:68 (the route-A judgment row, Grounds cell)
  old: its cost is a non-zero exit that is not exit 2, so no turn stops;
  new: its cost is a non-zero exit, which is not exit 2 where no `py` stands,
       so no turn stops there; where `py` stands and the script file cannot
       be opened, the exit is Python's 2 (round 2's finding 1);

frame/questions.md:9
  old: and each script, once loaded, exits 0, so the second half runs only
       where the first could not start or could not load it.
  new: and the second half runs where the first exits non-zero: where
       `python3` could not start or could not load the script, or where
       `seal_stamp.py --stop` fails to write its drawing, the one raise its
       catch leaves out.
```

### 2. *Scope* item 2 reads as two cases replacing three, the two among them

```seal
severity: should
location: `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:52`
evidence: read `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:52`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:73`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/plan.md:45`; executed `git grep -n "def test_the_plugins_stop_command_draws_once_and_exits_0\|def test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to" -- tests`
regression: round-1#3
```

Why it matters: the unit is the clause of *Scope* item 2 that names the
`Stop` command's cases, which the fold at `d2b2bb558` rewrote. The phase's
`frame/plan.md` row (`:45`, phase 2, *Scope* item 2) and the scenario *The
stamp is drawn by the plugin's hook* (`frame/design.md:73`) verify by "the
case *Scope* item 2 names". The fold applied round 1's paste-ready text as
given: "two cases replace `Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`,
`Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and
`Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`:
the first reads ...". So the defect came from round 1's own snippet.

Read as written, the sentence lists three replaced cases, and the two
`Test_main` cases are among them. The tree contradicts that reading: both
stand (`tests/skills/test_seal_stamp.py:2321`, `:2337`), and they are the
replacements. The other reading takes the last two names as the two cases.
The sealer can only tell which is meant by the `stamp-drawn-once` marker the
scenario row names. A frame sentence that an agent reads to find a case has
to have one reading (`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는
글은 한 가지로만 읽히게 쓴다*). The frame is the orchestrator's to fold.

```text
frame/design.md:52 (Scope item 2)
  old: two cases replace `Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`, `Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and `Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`: the first reads
  new: two cases, `Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and `Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`, replace `Test_install.test_accepts_a_launcher_the_harness_runs_at_stop_drawing_once`: the first reads
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `pr.md:7-9` adds the three quotes the finding asked for, so the
body now states the failure direction and the prompt budget that `CONTRIBUTING.md`
*What a change to a gate must carry* asks for. Each of the nine quotes in
`pr.md` stands word for word in the source its coordinate names, with runs of
whitespace collapsed (executed, `## Probes`). The quote at `pr.md:8` copies the
sentence that finding 1 above disputes, and it moves with that fold.

```seal
confirms: round-1#3
```
What holds: *Scope* item 1 (`frame/design.md:51`) names
`#test_the_plugin_registers_two_hooks_and_writes_none_into_git`, which
resolves at `tests/behaviour/test_chain_hooks_hardening.py:28`. *Scope*
item 2 (`:52`) names both `Test_main` cases, which resolve at
`tests/skills/test_seal_stamp.py:2321` and `:2337` (executed: `git grep`
of the three `def` lines). The order of the names in item 2 is finding 2
above.

What matched: the fix pass's claim that its new pins fail against the text
they replace. In a scratch worktree of `795905dca`, with `CONTRIBUTING.md`,
both READMEs, `docs/checks/the-stamp.md` and `skills/code-review/orchestration.md`
put back to `471353125`, the four cases that carry the new pins failed and
the other 32 passed (executed, `## Probes`).
`test_the_house_rule_says_where_each_hook_command_exits_non_zero` was among
the four.

What matched: the rewritten sentences in `CONTRIBUTING.md:461-466`,
`README.md:313-316`, `README.ko.md:312-315`, `docs/checks/the-stamp.md:90-92`,
`docs/checks/the-stamp.md:158-162`, `skills/code-review/orchestration.md:531-533`,
the comment at `skills/verify/scripts/seal_stamp.py:1006-1009` and
`changelog.md:3`. Each one limits its claim of a non-exit-2 to where no `py`
stands, or claims only that nothing draws. Each matches the command as
executed: exit 127 where no `py` stands, for a script that raises and for one
that is absent. The sentence in `trail/phases/phase-2.md` now says that
`--stop` catches what reading the payload and drawing raise, and nothing
that fails at load. That matches `seal_stamp.py:1554-1561` (read).

What matched: `gaps.md`'s diff adds one `## Not verified` row, on whether
Claude Code shows the person a hook command's non-zero exit, and removes or
rewords no row (read: `git diff 471353125..795905dca` of the file).

What matched: the new case is read against its group. In
`tests/behaviour/test_chain_hooks_hardening.py`, the one other case that reads
`CONTRIBUTING.md`'s hook bullet,
`test_the_places_that_reach_the_network_are_named_without_a_count`, pins the
network sentence alone. The new case pins the exit sentences, which no case
pinned before. `bin/seal layout --pairs` exits 0 and names neither module
(executed).

What matched: `bin/seal rules --check` exits 0 at the target (executed), and
the narrow run of the four modules the fixes touch passed (executed,
`## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the typecheck. This round ran four modules only, and the suite is `unverified` at the target | the work item | the orchestrator, at its one broad run after the rounds settle |
| Whether the Windows `py` launcher hands its child's exit 2 back to the harness, the one link of finding 1 no machine here runs | `hooks/hooks.json:8`, `hooks/hooks.json:19` | the owner, or a Windows user, with `frame/questions.md` Q1 |
| Whether Claude Code shows the person a hook command's non-zero exit: `gaps.md` row 6 | `hooks/hooks.json` | the owner, as that row names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/hooks tests/skills/test_seal_stamp.py -q` | exit 0, 235 passed |
| in a scratch worktree of `795905dca` under the round's scratch directory, `git checkout 471353125 --` the five files the fix pass rewrote and pinned, then `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q -p no:randomly` | exit 1, 4 failed and 32 passed: `test_the_house_rule_says_where_each_hook_command_exits_non_zero`, `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`, `test_the_policy_names_the_command_the_marker_and_the_command_to_draw`, `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves`. The worktree was removed afterwards |
| `python3 <absent path>/seal_stamp.py --stop`; `python3 <file of mode 000> --stop` | exit 2; exit 2 |
| the `Stop` command read from `hooks/hooks.json`, run by `/bin/sh -c` with `PATH=/usr/bin:/bin`, a `Stop` payload on stdin, and `CLAUDE_PLUGIN_ROOT` at a scratch root whose `seal_stamp.py` is `raise RuntimeError("a later release broke")`, then at a root with no `seal_stamp.py` | exit 127, stderr ending `/bin/sh: py: command not found`; exit 127, stderr `can't open file ... [Errno 2] No such file or directory` then `/bin/sh: py: command not found`. The scratch roots were removed afterwards |
| each quote of `pr.md`, looked up in its named source with runs of whitespace collapsed | nine of nine found |
| `bin/seal rules --check`; `bin/seal layout --pairs` | 0; 0 |
