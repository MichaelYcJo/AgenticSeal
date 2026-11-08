# Review round 3: 1794128303-the-plugin-ships-two-hooks-again

```seal
target: 9cec57f87, fixes 795905dca..9cec57f87
```

This is the verifying round. The code under review is the diff of round 2's
fixes, `795905dca..9cec57f87`: `05698548c` (round 2's record), `a19d215ea`
(the orchestrator's frame fold and its judgment row), `80540e348` (the fix
pass), `6435149f6` (round 2's close blocks) and `9cec57f87` (the fold of one
`frame/questions.md` bullet). `a19d215ea` changes the design: each hook
command in `hooks/hooks.json` now ends with ` || exit 0`. So this round
reviews that command shape as code, not only the answers to round 2. Beside
the diff, the round read the work item's records that state the present,
each whole at `9cec57f87`: `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. It then read
the three phase records, `trail/rounds/round-1.md` for its coordinates and
`trail/rounds/round-2.md` whole.

Facts carried from earlier rounds and not re-derived: the parse of the hook
scripts under the 3.7 and 3.8 grammars (round 1), and the coordinates round
2's finding 1 lists, each opened again at the target. Re-derived this round:
what each command exits where its script cannot be opened. That was run
against the old and the new `hooks/hooks.json` (`## Probes`).

The axes were the two closes, plus three of this diff's own. The first is
every statement of what a hook command exits or prints where its script
fails. It was listed by `git grep` over the tree for the phrases such a
statement uses, and each hit was read. The second is every sentence whose
reason stood on the old fact that a command's exit is its script's exit.
The third is the GFM table rows the fold wrote into the work item's records.
Each table row of the files the diff touches was split on its unescaped
pipes and counted against its header. That covers the files the diff
touches and every file of the work item's directory, which is a closed set.

## Findings

### 1. Three table rows the fold wrote hold an unescaped `||`, so the settle's reader stops at the plan's row and GitHub cuts the two frame rows short

```seal
severity: should
location: `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/plan.md:68`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:23-24`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/pr.md:8`
evidence: executed `skills/settle/scripts/settle.py#plan_rows` over `frame/plan.md` at the target, which returned three rows and the refusal "has a `Date | Judgment | Grounds | Judged against` table that stops at `| 2026-11-08 | Round 2 reopened round 1's finding 1: ...`, which is not a 4-cell row written `| … | … | … | … |` — every row below it would go unread"; executed a count of the cells split on unescaped pipes in every table row of the files `git diff --name-only 795905dca..9cec57f87` lists and of the work item's directory, which listed `frame/design.md:23` (4 cells, header 2), `frame/design.md:24` (4 cells, header 2) and `frame/plan.md:68` (6 cells, header 4) and nothing else; read `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:24`, `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md:69`, `skills/settle/scripts/settle.py:1040-1077`, `lib/config.py:1062`
regression: round-2#1
```

Why it matters: the units are three table cells the fold at `a19d215ea`
wrote for round 2's finding 1. They are the *Grounding* row on
`CONTRIBUTING.md` *What a change to a gate must carry* (`frame/design.md:23`),
the *Grounding* row on *House rules* (`:24`) and the round 2 row of
*Judgments of the run* (`frame/plan.md:68`). The frame asks for the shape
` || exit 0` (*Scope* item 1, and `frame/plan.md`'s round 2 judgment row).
The fold wrote that shape into table cells with its two pipes unescaped,
though the same file escapes them one row down (`:24`, `\|\|`) and in the
acceptance table (`:69`). So the defect came from the fold, not from the
frame it applied.

In a GFM table a `|` splits a cell even inside a code span unless it is
written `\|`. The effects differ by reader.

- `frame/plan.md:68`: the settle reads *Judgments of the run* through
  `lib/config.py#gfm_table` (`settle.py:1072`). That reader stops at this
  row and names the table as not read. The row itself and the phase 1 row
  below it (`:69`) go unread. Round 2's judgment, which the settle exists to
  weigh against what it cost, is the one row it cannot list.
- `frame/design.md:23-24`: rendered on GitHub, each row has four cells
  under a two-column header, so the cell ends at "each command ends with `"
  and the rest is dropped. On `:23` that drops the prompt budget and the
  untested platform, which *What a change to a gate must carry* asks the
  pull request to name.

The fix rewords the three cells so that no pipe stands in them, as
`gaps.md` row 12 already words the same fact ("a closing `exit 0`").
Escaping them as `\|\|` would also parse. But `pr.md:8` quotes `:23` word
for word, and a quote of the escaped cell would carry the backslashes into
the pull request body, where no table removes them. So the snippet changes
`pr.md:8` with `:23`. The three frame cells and the quote are the
orchestrator's.

```text
frame/design.md:23 (Grounding, the row on CONTRIBUTING.md *What a change to a gate must carry*)
  old: each command ends with ` || exit 0`, so it exits 0 whatever happens,
  new: each command ends with a closing `exit 0`, so it exits 0 whatever happens,

frame/design.md:24 (Grounding, the row on CONTRIBUTING.md *House rules*)
  old: is the shape both hook commands take before their closing ` || exit 0`;
  new: is the shape both hook commands take before their closing `exit 0`;

frame/plan.md:68 (Judgments of the run, the round 2 row, Judgment cell)
  old: Each command now ends with ` || exit 0`, so the rule
  new: Each command now ends with a closing `exit 0`, so the rule

pr.md:8
  old: each command ends with ` || exit 0`, so it exits 0 whatever happens,
  new: each command ends with a closing `exit 0`, so it exits 0 whatever happens,
```

```seal
verdict: fixed fc6405ddb
answer: The orchestrator rewrote the three frame cells and the `pr.md:8` quote at `fc6405ddb` so that no pipe stands in them. This fix pass ran a census over the files the crafter writes, `gaps.md`, `changelog.md` and `trail/phases/phase-1.md` to `phase-3.md`, at `d39edd697`. It counted the cells of each table row, splitting on unescaped `|`, against the row's header, and found no row whose count differs, so none needed a change (executed).
```

### 2. `lib/launch.py`'s reason for keeping the hooks off the launcher no longer holds once each command ends with ` || exit 0`

```seal
severity: should
location: `lib/launch.py:35-39`
evidence: read `lib/launch.py:19-21`, `lib/launch.py:35-39`, `lib/launch.py:48`, `ruff.toml:32-35`, `CONTRIBUTING.md:110-121`, `hooks/hooks.json:8`, `hooks/hooks.json:19`; executed `git grep -n "run through it\|do not run through\|harness's word for keeping" -- . ':!seal/threads'`, which lists `lib/launch.py:35` and `:38` alone, so no case pins the sentence
regression: round-2#1
```

Why it matters: the unit is the docstring sentence `80540e348` rewrote for
round 2's finding 1. *Scope* item 2 asks that `lib/launch.py:35-37` "name
the hook scripts in place of the launcher" (the phase 2 row of
`frame/plan.md`). The fix now reads: "The plugin's two hooks do not run
through it: each command `hooks/hooks.json` registers ends with ` || exit 0`
and exits 0 whatever happens, while this launcher's refusal is exit 2, which
from a `Stop` hook is the harness's word for keeping the turn going". Before
the design change that reason held, because a command's exit was its
script's. After it, a launcher's exit 2 inside either half meets the closing
` || exit 0` and never reaches the harness. So the sentence gives a reason
the new shape removed, and it sets the two facts side by side as though they
still conflicted. The defect came from the fix pass keeping the old reason
while it wrote the new command shape into the same sentence.

The reason that does hold is the floor. `FLOOR` is 3.12 (`lib/launch.py:48`),
and the launcher refuses anything below it before the script is read
(`:19-21`). The hook scripts are linted at 3.9 because they "run on whatever
`python3` starts" them, and "macOS ships 3.9 under that name"
(`ruff.toml:32-35`, `CONTRIBUTING.md:110-121`). An agent that reads the
sentence as it stands, and sees that ` || exit 0` absorbs the exit 2, may
route a hook through the launcher. On a stock Mac that hook would then print
no core and draw no stamp, and with ` || exit 0` nothing would say so.

```text
lib/launch.py:35-39
  old: scripts share. The plugin's two hooks do not run through it: each command
       `hooks/hooks.json` registers ends with ` || exit 0` and exits 0 whatever
       happens, while this launcher's refusal is exit 2, which from a `Stop` hook
       is the harness's word for keeping the turn going
       (`docs/checks/the-stamp.md`).
  new: scripts share. The plugin's two hooks do not run through it: each script
       `hooks/hooks.json` names runs on whatever `python3` starts it, 3.9 on a
       stock Mac, and this launcher refuses anything below `FLOOR` before the
       script is read. Behind each command's closing ` || exit 0` that refusal
       would reach nobody, so the core would not print and the stamp would not
       draw, with nothing to say so (`ruff.toml`, *per-file-target-version*).
```

This snippet is a docstring and assumes no OS boundary. It reaches every
statement of the reason: the search in `evidence:` lists no other.

```seal
verdict: fixed d39edd697
answer: Before writing the sentence, the fix pass checked the reason against the code (read). `lib/launch.py#FLOOR` is `(3, 12)`, and the docstring's own `:19-21` says the launcher exits 2 below it before the script is read. `ruff.toml`'s *per-file-target-version* comment and `CONTRIBUTING.md:118-121` say that the scripts the hook commands run start on whatever `python3` is found, and that macOS ships 3.9 under that name. The docstring now gives that floor as the reason the hooks do not run through the launcher. The paste-ready text was taken in substance with one clause changed: "that refusal would reach nobody ... with nothing to say so" became "that refusal would end in exit 0". Whether Claude Code shows a hook's stderr when its exit is 0 is not something the tree records, so the sentence claims only the exit and what would not happen. A wider search than the round's, `git grep -i "run through it\|not run through\|through the launcher\|harness's word for keeping\|hooks.*launch\.py"`, found no other statement of the reason: `.github/scripts/run_tests.py:80` and `CONTRIBUTING.md:112` are about `bin/test` and `bin/seal`, and `tests/lib/test_launch.py:200` about a wrapper (executed). No case pins the docstring.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: both commands in `hooks/hooks.json` (`:8`, `:19`) end with
` || exit 0`, so each exits 0 where its script cannot be opened. The case
`tests/behaviour/test_chain_hooks_hardening.py#test_each_hook_command_exits_0_where_its_script_cannot_be_opened`
runs each command under `sh` with no script under `${CLAUDE_PLUGIN_ROOT}` and
a scratch `py` that exits 2. It passes at the target and fails with exit 2
for both events against the `hooks/hooks.json` of `795905dca` (executed,
`## Probes`). So the fix pass's claim that it was seen red holds. The
over-claims round 2 named are now true sentences: `hooks/core-start.py:15-18`
says the script exits 0 on every path once loaded and the command exits 0
through its closing ` || exit 0`, and `hooks/core-start.py:62-66` turns every
raise into exit 0 (read). The same is true of `frame/design.md:23` (its
cells are finding 1 above), `frame/plan.md:68`, `frame/questions.md:9` at
`9cec57f87` and `pr.md:8`. The person-facing sentences in `CONTRIBUTING.md:458-463`,
`README.md:311-314`, `README.ko.md:310-313`, `docs/checks/the-stamp.md:87-92`
and `docs/checks/the-stamp.md:158-160` each state the one rule, and their
pins fail against the text of `795905dca`: three cases failed and 35 passed
(executed, `## Probes`). The claims the fix pass left standing were read
again. `skills/code-review/orchestration.md:531-533` and the comment at
`skills/verify/scripts/seal_stamp.py:1006-1010` say only that nothing draws
where `python3` cannot load the script, and that still holds. Neither of the
two new defects above is a reopening of this finding: the over-claim it
named is gone, and each defect stands in a unit the fix made.

```seal
confirms: round-2#2
```
What holds: *Scope* item 2 (`frame/design.md:52`) now names
`Test_main.test_the_plugins_stop_command_draws_once_and_exits_0` and
`Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`
first, then the one case they replace, so the sentence has one reading. Both
ids resolve at `tests/skills/test_seal_stamp.py:2321` and `:2337` (executed:
`git grep` of the three `def` lines, which finds the two and not the
replaced one).

What matched: the new case is read against its group. The other cases that
run a hook command run only its `python3` half: `tests/hooks/test_core_start.py`,
the two `Test_main` `Stop` command cases, and `tests/lib/test_launch.py#hooked`,
which reads the first part only. The registration case holds the shape and
runs nothing. The new case alone runs the whole command under a shell, so it
covers what no case in its group covered. `bin/seal layout --pairs` exits 0
and names none of these modules (executed).

What matched: the `gaps.md` diff marks the row on a non-zero exit reaching the
person `closed` in place and removes no row (read: `git diff
795905dca..9cec57f87` of the file). Each of the nine quotes in `pr.md`
stands word for word in the source its coordinate names, with runs of
whitespace collapsed (executed, `## Probes`).

What matched: `trail/phases/phase-2.md:66-71` now says that a script that
fails to load is caught by nothing in the script, and that the closing
` || exit 0` keeps the exit at 0. That matches `hooks/hooks.json:8` and
`skills/verify/scripts/seal_stamp.py`'s `--stop` branch (read).

Observed, no finding: the comment at
`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:97-98`
still says that where the script cannot load, "the command says something".
Under ` || exit 0` the command still writes Python's error and the shell's
`command not found` to stderr, but it exits 0. Whether Claude Code shows the
stderr of a hook that exits 0 is not something this round ran. The sentence
the comment introduces, at `skills/code-review/orchestration.md:531-533`,
holds either way.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the typecheck. This round ran five modules only, and the suite is `unverified` at the target | the work item | the orchestrator, at its one broad run after the rounds settle |
| Whether `#test_each_hook_command_exits_0_where_its_script_cannot_be_opened` runs or skips on CI's Windows leg, where `sh` must start a `#!/bin/sh` scratch file named `py`; this round ran it on macOS alone | `tests/behaviour/test_chain_hooks_hardening.py:89-120` | the CI run at the pull request |
| Whether the shell the harness uses on Windows runs ` || exit 0` as `sh` does, beside whether the `py -3` half starts there | `hooks/hooks.json:8`, `hooks/hooks.json:19` | the owner, or a Windows user, with `frame/questions.md` Q1 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/lib/test_launch.py tests/hooks tests/skills/test_seal_stamp.py -q` | exit 0, 245 passed |
| in a scratch worktree of `9cec57f87` under the round's scratch directory, `git checkout 795905dca -- hooks/hooks.json`, then `pytest -p no:randomly tests/behaviour/test_chain_hooks_hardening.py -k "exits_0_where_its_script_cannot_be_opened or registers_two_hooks"` | exit 1: both `#test_each_hook_command_exits_0_where_its_script_cannot_be_opened` cases failed with exit 2 and Python's `can't open file ... [Errno 2]`, and the registration case failed on `assert 2 == 3` |
| in the same worktree with `hooks/hooks.json` restored, `git checkout 795905dca -- CONTRIBUTING.md README.md README.ko.md docs/checks/the-stamp.md`, then `pytest -p no:randomly tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | exit 1, 3 failed and 35 passed: `test_the_house_rule_says_each_hook_command_exits_0_whatever_happens`, `test_the_policy_names_the_command_the_marker_and_the_command_to_draw`, `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves`. The worktree was removed afterwards |
| `settle.py#plan_rows` over `frame/plan.md`, loaded by path with `python3 -c` | three rows read (`:65-67`) and one refusal at `:68`, quoted in finding 1 |
| the cells of every table row in the files the fix diff touches and in the work item's directory, split on unescaped pipes and counted against each table's header, by `python3 -c` | three rows off their header: `frame/design.md:23`, `frame/design.md:24`, `frame/plan.md:68` |
| each quote of `pr.md`, looked up in its named source with runs of whitespace collapsed | nine of nine found |
| `bin/seal rules --check`; `bin/seal layout --pairs` | 0; 0 |
