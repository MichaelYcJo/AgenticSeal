# Phase 2: 1794128303-the-plugin-ships-two-hooks-again

## What this phase found

**The frame holds for this phase, with four statements that do not.** Each
coordinate *Scope* item 2 names stood at `783990292` once found by its text.
The four that do not hold, each judged against `frame/design.md` *Scope*
item 2 and the tree at `783990292`:

- *User scenarios & acceptance*, the row *No shipped file names the
  launcher*, expects the grep to list `lib/launch.py`'s and
  `CONTRIBUTING.md:112`'s mentions of the floor launcher and nothing else.
  At `cf6d723a` it lists four kinds of line. The first is the floor
  launcher in more files than the row names: `.github/scripts/run_tests.py:80`,
  `lib/launch.py:31,105`, `tests/lib/test_launch.py`,
  `tests/skills/test_deferral_check.py:14` and `tests/skills/test_settle.py:23`.
  The second is the WSL `bash.exe` launcher at `tests/conftest.py:539`. The
  third is `.test_durations`, which still names the removed launcher
  cases; `frame/plan.md` *Constraints* leaves that file to CI, so it was not
  edited. The fourth is the 0.33.0 to 0.34.1 launcher that *Scope* item 2
  itself asks to be named for removal: `docs/checks/the-stamp.md:95-96`,
  `skills/update/SKILL.md` steps 2 and 4b, `README.md:314`, and the cases
  that pin them. No line names a command or a case of the removed launcher.
- *Scope* item 2 gives `CONTRIBUTING.md`'s bullet the opening **The plugin
  ships two hooks, and nothing it ships writes outside the repository**.
  That is false at `783990292`: `/agentic:update` step 4 writes
  `CLAUDE.md.bak` beside the user's `CLAUDE.md`, and
  `/agentic:parity-setup` writes `~/.claude/agentic/parity-paths.md`
  (`README.md` *Migrations*). The bullet's subject is the hooks, so it reads
  **The plugin ships two hooks, and neither writes outside the
  repository**. The two places that cite the bullet by its opening,
  `docs/running/measuring-a-run.md` and
  `skills/verify/scripts/session_cost.py#emit`, cite that.
- *Scope* item 2 does not name `agents/sealer.md` step 6, "the person's
  `Stop` hook draws it", nor `SECURITY.md:38,49`, which name the stamp's
  hook as the one that fires on its own. Both are statements of the
  person's hook. `agents/sealer.md` now names the plugin's `Stop` hook, and
  `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_the_sealer_queues_the_stamp_once_and_draws_none`
  pins the sentence. `SECURITY.md` names the plugin's hooks.
- `## Removes` names the launcher's cases by class and two `Test_main`
  cases. A third `Test_main` case,
  `test_refuses_settings_that_do_not_parse_with_exit_2`, ran `--install`
  alone, and it went with them. The module docstring's exit-code sentence
  lost "settings that do not parse" for the same reason.

**`skills/start/SKILL.md` step 2 lost one sentence in this phase.** "The
data directory its stamp question passes is `${CLAUDE_PLUGIN_DATA}`" turns
false once the question goes. The file is phase 3's to remove, and the
sentence is a statement of the stamp question, which *Scope* item 2 removes
with every statement of it, so it went here. Nothing else in that file
changed.

**Two cases hold the plugin's `Stop` command, not one.** *Scope* item 2
asks for one case in place of the launcher's drawing case. The launcher's
class also held the drawer on a console it cannot encode to, and
`tests/lib/test_console.py`'s docstring names that case as the one that
holds `lib/console.py`'s fact for the stamp. So
`Test_main.test_the_plugins_stop_command_draws_on_a_console_it_cannot_encode_to`
runs the same command on the three hostile consoles. Both cases read the
`python3` half of the command from `hooks/hooks.json`, with this
interpreter for `python3` and `${CLAUDE_PLUGIN_ROOT}` filled in, as
`tests/hooks/test_core_start.py#command` does for the `SessionStart` half.
The drawing case carries `stamp-drawn-once` and stands in
`test_the_policy_names_the_command_the_marker_and_the_command_to_draw`'s
list. The launcher's two failure cases, a root that is gone and a script
that raises, went with the launcher: `--stop` catches every failure in
`main`, which `Test_main.test_stop_says_nothing_and_exits_0_whatever_it_meets`
already holds.

**Step 4b's command handles a data directory that did not arrive.** *Data &
interfaces* gives the read as `test -f "${CLAUDE_PLUGIN_DATA}/stamp.py"`.
Where the substitution does not happen, that tests `/stamp.py` and reports
no launcher, which says nothing true. The command prints `no data
directory` for an empty value, `launcher <path>` or `no launcher`, and the
table gives each its act. The row asks the person to take the settings
entry out before the file, because an entry whose file is gone fails at the
end of every turn (the old `CONTRIBUTING.md` bullet). The step's case is
`tests/behaviour/test_update_reads_the_config_directory_in_use.py#test_step_4b_reads_the_old_launcher_and_writes_nothing`,
in the module that runs the update skill's commands under `bash`.

**Three pins were added, each beside the text it holds** (contract rule 14):
the line `QUEUED` prints is spelt out in
`Test_main.test_guarantee_queues_the_stamp_and_prints_the_line_naming_it`,
the one-call bootstrap case refuses a third question and any
`seal stamp --` command, and the README case refuses
`The plugin registers no hook`, `seal stamp --install` and
`seal stamp --remove` in either edition.

**Seen red, each with the one guard it names removed:**

- The two `Stop` command cases: `seal mutate hooks/hooks.json` took the
  `Stop` entry out, and all four parametrizations went red with
  `KeyError: 'Stop'` at the command read. That ran before `7cd56623` was
  committed. A second run over `7cd56623` dropped `--stop` from the
  `python3` half, and all four went red at the `systemMessage` read, since
  the script printed the sample.
- The console case: `seal mutate` of `seal_stamp.py`'s `__main__` replaced
  the `reconfigure` call with `pass`, and all three consoles went red at
  `out.strip()`.
- The `QUEUED` pin: `seal mutate` restored the old wording of `QUEUED`, and
  both parametrizations went red at the line comparison.
- The step 4b case: four `seal mutate` runs over `skills/update/SKILL.md`,
  each red. The file test made `false` read `no launcher` for the launcher.
  The empty test made `false` read `no launcher` for an empty directory.
  The sentence "This step asks nothing and writes nothing." deleted failed
  its pin. The row with the file first and the entry second failed its pin.
- The gone-pins: a `Stamp: <line>` added to the update output, a
  `seal stamp --hook` sentence added to bootstrap, a launcher clause added
  to `skills/code-review/orchestration.md`'s stamp paragraph, and
  `seal stamp --install` added to `README.md` each went red at their own
  assertion.
- Every rewritten document pin ran against the tree at `783990292`, with
  this phase's five test modules copied into a scratch worktree that was
  then removed. Nine cases failed, each at the new sentence it pins.

**Mutation runs**, each `seal mutate` over a committed tree, all red, as
listed above: `hooks/hooks.json` twice, `seal_stamp.py` twice and
`skills/update/SKILL.md` five times. The `README.md`, `bootstrap.md` and
`orchestration.md` runs were one each. No unit of this phase was only
renamed or moved.

**The phase's scoped run.** One command, `bin/test` over the plan row's
modules, the whole of `tests/behaviour/` and `tests/text/`, and the 38 other
test modules that name a path this phase changed or read `git ls-files`,
`os.walk` or `glob(` over the tree. It ran over `cf6d723a` with this record,
`gaps.md` and the Status cell in the working tree, which is the content of
the commit that adds them, and gave 5401 passed, 10 skipped and none
failed. `seal rules --check`, `seal layout --check` and
`seal layout --pairs` exit 0 at `cf6d723a`.
