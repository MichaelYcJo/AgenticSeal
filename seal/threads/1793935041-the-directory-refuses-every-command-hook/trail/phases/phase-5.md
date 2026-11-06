# Phase 5: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase, with one thing the tree decides.** Every
coordinate of the phase row stood at `7dd6dd14`. Two hooks remained,
`hooks/sealer-stamp-queue.py` at `post-edit` and `hooks/sealer-stamp.py` at
`Stop`, with `hooks/dispatch.py` and `hooks/hooks.json` registering them.
`seal_stamp.py#session_key` took the session from its argument, which the
queue hook read from the hook payload; no shipped file read
`CLAUDE_CODE_SESSION_ID` here, since phase 2 removed `seal no-work-item`'s
read, and *Scope* item 7's clone key keeps it that way. The thing the tree decides is the
settings path. *Data & interfaces* has `--install` merge into
`${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json`, and *Scope* item 7 has
the stamp script read no environment variable. The two cannot both hold in
the script, so the shell spells the path and passes it. The departures below
follow from that and from the tree.

**Departures from the frame, each with its grounds.**

- `--install` and `--remove` take `--settings <file>` beside the data
  directory, and refuse with argparse's exit 2 without it. The script reads
  no environment variable (*Scope* item 7, judged against the portal's
  credential hold `seal.py` names). The caller writes
  `"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json"`, which the shell
  expands.
- `--remove` takes `<data-dir>`, as `--install` does. The entry it takes out
  is the one whose command is exactly `hook_command(<data-dir>)`. A match on
  a substring of the command could take out a person's own entry that names
  the same path.
- `--hook <data-dir>` prints `installed <root>`, `declined` or `neither`.
  The root is read back from the launcher's `ROOT = ...` line, so a person
  who updated by `claude plugin update` alone sees which copy the launcher
  names. A launcher in another shape prints `installed`.
- `skills/implement/bootstrap.md` is read with the Read tool, so the harness
  substitutes nothing in it. `skills/start/SKILL.md` step 2 now names the
  data directory, `${CLAUDE_PLUGIN_DATA}`, which its body receives
  substituted, and bootstrap's question takes the data directory from there.
  Judged against `docs/checks/the-stamp.md` *The stamp's `Stop` hook is the
  person's* and the spike's finding that a skill body is substituted.
- `skills/update/SKILL.md` step 4b runs `seal` from the installed copy `$p`
  that step 2b reads, so `--install` writes the launcher with the new root.
  Step 4b also runs where step 2 reports the plugin already current. A
  person who updated by `claude plugin update` alone reaches 0.33.0 without
  the question, and the owner's own stamp would otherwise stop with nothing
  saying so (*Scope* item 7's reason).
- A values file an earlier release wrote into a per-session directory under
  `<git-common-dir>/agentic-stamp/` is neither drawn nor counted.
  `docs/checks/the-stamp.md` *The stamp* states it as a limit, with
  `seal stamp --from` as the way to draw it. Judged against the owner's rule
  that a shape outside the normal flow gets a limit sentence and not a
  guard.
- `--guarantee` names a file it cannot read and exits 2. The hook it
  replaces stayed silent. A command the sealer runs is read by the sealer,
  and step 6 of `agents/sealer.md` carries an exit of 2 into its report with
  the verdict standing.
- A `Stop` payload of any session in the clone draws every stamp pending
  there. A payload carrying `agent_id` draws nothing, as before. The cases
  that pinned a session's own directory ("another session", "no session")
  are rewritten to the clone. The values file no longer carries a `session`
  key.
- The launcher runs `seal_stamp.py --stop` in its own process through
  `runpy` and exits 0 whatever happens, a `SystemExit` of the script's
  included. A `Stop` hook that exits 2 keeps the turn going.
- `agents/sealer.md`'s *Never* bullet reads "you queue the stamp once from
  your `sealed` and draw nothing", where *Scope* item 7 reads "and nothing
  else draws". The person's `Stop` hook draws, so the frame's words have a
  second reading that is false. Judged against `skills/writing-style/SKILL.md`
  *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*. The *Job* paragraph
  now reads "your writes are `guarantee.md` and the stamp's values file step
  6 queues, and a write not named here is a write you do not make", which
  `tests/text/test_every_agent_reads_the_contract.py` accepts as the bound.

**Q4 of `frame/questions.md`: the module keeps its name.**
`tests/behaviour/test_chain_hooks_hardening.py` lost its three `hooks.json`
cases, its gate-table helpers and case, and the `userConfig` case, and gained
`test_the_plugin_registers_no_hook_and_writes_none_into_git`. What remains
pins the packaging, the READMEs' account of it, and the agent definitions'
wording, and no one name fits those three. A rename moves about 1,100 lines,
and contract rule 19 would then owe every citation of the path, while phase
7 moves `tests/hooks/` anyway. The module docstring now says the name stays
since #1376. Judged against `frame/questions.md` Q4, whose default is (a),
and `skills/core/SKILL.md` *The rule a mechanism is kept against*.

**The routing check's rule moved its check line.**
`docs/checks/the-routing-check.md`'s first rule, that this plugin writes
nothing into a clone's git hooks, was held by a case in
`tests/hooks/test_dispatch.py`. That case asserted `hooks/git/` stays gone.
The assertion moved into the new packaging case, and the rule's `check:`
line names `tests/behaviour/test_chain_hooks_hardening.py`.

**Units removed that the frame's `## Removes` does not name.** Each stood on
the removed hooks alone, and `git grep` found no other caller. Judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against*, which
removes in the same commit what stood on the old fact.

- `tests/conftest.py#run_hook`, `decision_of`, `run`, `q`, `sh`, `payload`,
  and the block of the stamp queue's record helpers: `STAMP_ITEM`,
  `guarantee_record`, `routing_record`, `queued_values`. `q`, `sh`,
  `payload` and `run` built `PreToolUse` payloads, whose hooks left in
  earlier phases.
- `tests/test_conftest.py#Test_q`, the one reader of `q`.
- `tests/behaviour/test_chain_hooks_hardening.py#_hook_commands`, its three
  `hooks.json` cases, `GATE_TABLE`, `gate_table_names`,
  `test_the_gate_table_has_one_row_for_each_script_groups_registers` and
  `test_every_option_the_manifest_declares_is_one_a_hook_reads`. The
  `python3 || py -3` form they held is now
  `tests/skills/test_seal_stamp.py#Test_hook_command`'s.
- `tests/behaviour/test_first_setup_asks_once.py#test_the_gates_table_says_the_root_may_sit_under_the_git_dir`.
  The table it read is gone from both READMEs.
- `tests/hooks/test_console.py#Test_module`. Its hostile-console case moved
  to `tests/skills/test_seal_stamp.py#Test_install.test_accepts_a_launcher_on_a_console_it_cannot_encode_to`.

**Statements edited beyond the Delivers cell.** The method was `git grep -n
-E` over the tree, outside `seal/threads/` and `.test_durations`, for
`sealer-stamp`, `sealer_stamp`, `hooks.json`, `hooks/dispatch`,
`dispatch.py`, `the-session-hooks`, `MESSAGE_RESERVE`, `MESSAGE_BUDGET`,
`session_key`, `NO_SESSION`, `post-edit`, `gate-failure`, `edit gate`,
`edit hook`, `run_hook`, `crafter mark` and `per-session marker`. A second
read went over every line holding the word `hook` in `README.md`,
`README.ko.md`, `CONTRIBUTING.md`, `SECURITY.md`, `docs/`, `skills/`,
`agents/` and `hooks/lib/`. Each line below stated a removed hook as
present and is edited in this phase:

- `skills/config/SKILL.md:128`, "and a hook stays silent".
- `skills/start/SKILL.md` step 2, the data directory.
- `SECURITY.md`'s hooks bullet and its two later mentions.
- `ruff.toml`'s two comments, and `CONTRIBUTING.md`'s floor paragraph,
  which named "a hook" among what runs before the floor.
- `CONTRIBUTING.md`'s "A change to any hook needs a test" and its English-only
  bullet; both READMEs' *Contributing* paragraph and *Language policy*,
  which said "hook" where the plugin now has gates and scripts.
- Both READMEs' *Limits* bullet on Windows, which named a hook entry point.
- `docs/running/what-a-script-gates.md`'s stamp row, as
  `frame/design.md` row 128 asks, and `docs/running/the-broad-gate.md:30`,
  "drawn from that verdict at its write".
- `skills/verify/scripts/session_cost.py#emit`'s docstring, which cited the
  CONTRIBUTING bullet by its old name.
- `hooks/lib/console.py`, `launch.py` and `routing.py`, the docstrings and
  comments naming `dispatch.py`, `hooks.json` and `the-session-hooks.md`;
  then, in the range read, four comments in `blocks.py`, `optin.py` and
  `routing.py` that named hooks as a record's readers (`13cc7053`).
- `skills/verify/scripts/test_layout.py` and
  `tests/skills/test_test_layout.py`, "the formatter the edit hook runs",
  which phase 3's removal of the lint hook left standing.
- `skills/implement/bootstrap.md:63`, `skills/implement/scripts/seal.py:49`,
  `templates/setup/seal-README.md:52` and its copy `seal/README.md`, which
  named the crafter mark and the gates' per-session markers beside the root.
  Phase 4 removed the mark. What stands there now is the stamp's queue and
  refusal records, the throwaway opt-out and the export manifest.
- `tests/censuses.py`, `tests/text/test_a_rider_reaches_its_file.py`,
  `tests/hooks/test_config.py` and `tests/hooks/test_routing.py`,
  docstrings that cited `dispatch.py`; `tests/behaviour/test_docs_line_wrap.py`
  lost the removed document; `tests/behaviour/test_the_release_check_watches_what_ships.py`
  keeps `hooks` in `SHIPS`, with its comment naming `hooks/lib/`.

The census at `13cc7053` finds the names only in cases that assert their
absence. The sweep over `hooks/lib/` is a sample. Two comments it did not
reword still describe a hook path: `hooks/lib/optin.py:97`, a measurement of
a `PreToolUse` hook, and `hooks/lib/routing.py:410`, which says a hook fires
before the commit. Phase 7 rewrites every path under `hooks/lib/` and is
where they are read next.

**Two cases were added after the build, and two were tightened.**
`7647c277` adds
`Test_install.test_refuses_to_fail_where_the_script_its_launcher_runs_fails`:
the launcher's `except BaseException` had no case that could see it, because
`--stop` itself never exits non-zero. `6e5e6e23` adds
`tests/behaviour/test_first_setup_asks_once.py#test_the_stamp_question_is_put_once_where_neither_answer_stands`,
which holds bootstrap's question, the entry's data directory and step 4b
(contract rule 14). `1ff6ff70` reads each README edition's stamp sentences
in *What runs on your machine* alone, after a mutation of the Korean
section survived because *Install* carries the same sentence. `e0a76e74`
moves the two not-absolute cases into a scratch directory. The first run of
the `isabs` mutation wrote `relative/` into the repository root, which was
removed by hand, and the run after `e0a76e74` wrote nothing there.

**Seen red.** The new `tests/skills/test_seal_stamp.py` was run against the
code at `7dd6dd14` in a scratch worktree: 97 failed and 116 passed. Every
case of the six entries failed, the `--stop` case whose `cwd` is outside the
clone among them, and the worktree was removed. After the commits, each
`seal mutate` run below exited 0 with the verdict `red`, except one:

- `seal_stamp.py#drawn_at_stop`, `toplevel(payload.get("cwd"))` as
  `toplevel(None)`, against `-k cwd_outside_the_clone`: 1 failed.
- the `agent_id` guard dropped, against `-k any_end_but`: 1 failed.
- `install`'s no-duplicate `if not any(...)` as `if True:`, against
  `Test_install or Test_hook_command`: 2 failed.
- `remove`'s exact command match as `if hook.get("command"):`, against
  `-k another_launchers_entry`: 1 failed.
- `_data_dir`'s `isabs` check dropped, against `-k not_absolute`: 2 failed,
  run again after `e0a76e74` with the same result.
- `hook_state`'s declined branch as `if False:`, against
  `Test_hook_state or Test_decline`: 2 failed.
- `main`'s `--stop` fallback `message = None` as `raise`, against
  `-k stop_says_nothing`: 1 failed.
- `main`'s named exit 2 as `raise`, against `-k guarantee_refuses_a_file`:
  1 failed.
- the launcher's `except BaseException:` as `except ImportError:`, against
  `-k script_its_launcher_runs_fails`: 2 failed.
- `STOP = "Stop"` read from `os.environ`, against `-k environment`: 1
  failed.
- `hook_command`'s `py -3` as `python`, against `-k python3_first`: 1
  failed.
- `skills/implement/bootstrap.md` without its `seal stamp --hook` sentence,
  `skills/start/SKILL.md` without the data directory, and
  `skills/update/SKILL.md`'s `installed <root>` row running nothing, each
  against `-k stamp_question`: 1 failed each.
- `agents/sealer.md` step 6 without "as it printed it", against
  `-k sealer_queues`: 1 failed.
- `.claude-plugin/plugin.json` with a `hooks` key, against
  `-k registers_no_hook`: 1 failed.
- `README.md`'s network sentence put back as "No hook reaches the network.",
  against `-k reach_the_network`: 1 failed.
- `docs/checks/the-stamp.md`'s refusal writer renamed, against
  `-k refusal_record`: 1 failed.
- `README.ko.md`'s "플러그인은 훅을 하나도 등록하지 않습니다." in *내 컴퓨터에서
  도는 것*, against `-k writes_and_leaves`: `SURVIVED`, exit 1, before
  `1ff6ff70`; `red` after it, 1 failed. `README.md`'s same sentence: `red`.

**The phase boundary set.** The modules that name a changed path, or the
base name of a changed file, were listed by `git grep -l -F` over `tests/`
for the range `7dd6dd14..e0a76e74`, with `tests/text/`, `tests/behaviour/`,
`tests/hooks/`, `tests/skills/test_seal_stamp.py` and `tests/test_conftest.py`
whole: 127 of the 132 test modules. One command through `bin/test` over
`e0a76e74` passed 5,759 with 10 skipped, exit 0. The plan row's command,
`bin/test tests/skills/test_seal_stamp.py tests/behaviour/ tests/text/`,
passed 1,994 with 9 skipped, exit 0, at the build's tree before
`c91f9a13` was committed. After `13cc7053`, `bin/test tests/hooks/
tests/behaviour/test_docs_line_wrap.py` passed 542, exit 0. `seal rules
--check` exited 0 over 217 check lines in 69 rule files. `seal layout
--check` exited 0 with 132 files read and none refused. `uvx ruff check` and
`uvx ruff format --check` over the 25 changed Python files exited 0.
`git ls-files hooks/` lists nine files, all under `hooks/lib/`.

`.test_durations` keeps the removed cases' ids for CI's rebuild, as phase
1's judgment row states.
