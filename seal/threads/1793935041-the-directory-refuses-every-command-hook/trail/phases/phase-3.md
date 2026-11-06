# Phase 3: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase, with one departure the owner decided
mid-run.** Every coordinate of the phase row stood at `ef263ff5`:
`bootstrap.md:132`, `release-checklist.md:324,360`,
`branch-and-release.md:19`, `publish-release.yml:8` and
`publish_release_note.py:8` each cited the hook the row names.
`agents/crafter.md` holds no sentence that stood on `lint-python.py`, so it
is not edited, as the row allows. The departure is the description of
`skills/code-review/SKILL.md`. *Scope* item 5 says the description "says
the built-in `/code-review` is the bug sweep". The owner's rule, relayed by
the orchestrator during the build, replaces that. Where this plugin is
installed, a plain request such as "review this PR <url>" or "검토해봐
<url>" runs this plugin's review, and the person names no skill. Claude
Code's built-in `/code-review` runs when the person types that command by
name. The description's `Use when:` now claims a request, in plain words and
naming no skill, to review a PR, a diff or a branch or to re-review after
fixes. Its `NOT for:` names a person typing `/code-review` by name. The text
was written to `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은
한 가지로만 읽히게 쓴다*: the person is the party, and the reading is one.
The new case
`tests/behaviour/test_chain_hooks_hardening.py#test_a_plain_review_request_is_the_review_skills_and_the_typed_command_is_not`
pins it under contract rule 14, beside the group's case on the skills'
`Use when:` scaffolding.

**Three units left that the frame's `## Removes` does not name.**
`tests/conftest.py#reason_of` was read by the removed gates' tests alone.
`tests/behaviour/test_first_setup_asks_once.py#test_the_gate_that_reads_the_absence_exists_and_is_wired`
asserted that `mode-gate.py` exists and is wired, so it went with the gate.
The `PostToolUse` matcher in `hooks/hooks.json` was `Write|Edit|NotebookEdit`,
and `NotebookEdit` stood on `lint-python.py` alone:
`hooks/sealer-stamp-queue.py#TOOLS` reads `Write` and `Edit`. The matcher is
now `Write|Edit`. Each was judged against `skills/core/SKILL.md` *The rule a
mechanism is kept against*: a change removes, in the same commit, what stood
on the old fact.

**The closed set of statements on the removed units reached past the
Delivers cell, and each was edited in this phase.** The method was
`git grep -n -E` over the tree, outside `seal/threads/` and
`.test_durations`, for `mode-gate`, `mode_gate`, `review-skill-gate`,
`review_skill_gate`, `version-check`, `version_check`, `lint-python`,
`lint_python`, `pre-bash`, `pre-skill` and `session-start`, then a second
grep for the sentences that state them in other words: `mode gate`,
`review-skill gate` and `version check`. The edits beyond the Delivers
cell, each on the ground that the sentence stated a removed unit:

- `hooks/dispatch.py`: `run_gate`'s docstring gave lint-python's argv as the
  reason argv is swapped, and `describe`'s example named `pre-bash`. Both
  now state the present. `opted_in`'s docstring counted "thirteen of the
  fifteen gates". Four stand, so it now says every gate that asks
  `optin.py`, a statement with no count to go stale.
- `hooks/lib/config.py`'s module docstring and eight passages named
  `mode-gate.py` as the row's second reader, or "a hook" as a kind of
  caller. No hook imports the module now, so each names the commands.
  `hooks/lib/optin.py#home_at`, `hooks/lib/blocks.py`'s opening and
  `hooks/implementer-notice.py#already_told` cited the removed gates. Each
  now states its own ground.
- `skills/verify/scripts/broad_gate.py`: `fenced_row`'s docstring and two
  refusal messages a person sees named "the mode gate's" reader. The two
  messages are pinned by an added assertion each in
  `tests/skills/test_broad_gate.py`.
- `skills/config/SKILL.md:83`, `templates/setup/config.md` at three places,
  `skills/implement/scripts/seal.py#write_row`'s comment and the docstring
  of the matching case in `tests/skills/test_seal.py` named the mode gate.
- `README.md` and `README.ko.md`: the four gate rows, the lint-python
  sentence, the side effects of version-check and lint-python, and the
  network paragraph. Each edition now says no hook reaches the network.
  `CONTRIBUTING.md`'s network bullet now says no hook does today and keeps
  the limits a hook that did would need. `SECURITY.md` said the hooks run
  around commits, branch switches and session start. It now names agent
  spawns, commits, file edits and the end of a turn. Phase 5's rewrite of
  that bullet stands.
- `docs/running/what-a-script-gates.md` *The checks* lost the rows of
  `mode-gate.py`, `review-skill-gate.py` and `lint-python.py`.
- `ruff.toml`'s header said the file exists because lint-python acts where a
  project configures ruff. It now names `ruff check` and
  `ruff format --check`, which the broad gate runs.
- `skills/verify/scripts/seal_stamp.py#MESSAGE_RESERVE`'s comment gave the
  longest gate-failure report as 567, 975 and 1,381 UTF-16 units for one,
  two and three failed gates. Over the new `GROUPS`, `longest_report` gives
  559, 959 and 1,357, and
  `tests/hooks/test_dispatch.py#test_two_failed_gates_fit_the_reserve_with_every_field_at_its_cap`
  failed until the comment carried them.
- `tests/text/test_a_rider_reaches_its_file.py` listed
  `hooks/review-skill-gate.py` as a file holding a rider. The rider went with
  the file. `tests/skills/test_test_layout.py`'s example path was
  `hooks/mode-gate.py`, and is now a name no file holds.
- `tests/behaviour/test_docs_line_wrap.py`'s docstring cited
  `skills/code-review/SKILL.md:6` as a 92-column line. The rewritten
  description wraps, so the docstring now states the exclusion without the
  coordinate.

**The rule the version notice stood on keeps a case.**
`docs/releasing/release-checklist.md`'s paragraph on a notice that an update
landed cited `tests/hooks/test_version_check.py` at line 360. Its sentence on
the session-start hook now names `/agentic:update`, which prints the reload
for the person to type. The added case
`tests/behaviour/test_release_hygiene.py#test_update_names_the_reload_and_what_it_was_measured_to_reach`
reads `skills/update/SKILL.md` *Output* for the reload command, what it was
measured to reach and the restart for what was not, and the paragraph's
`check:` line names that module.

**The automation promise is reworded to the sense of
`docs/running/the-run.md` *The run*, as the orchestrator's judgment row of
2026-11-06 asked.** Question 1's `automation` description in
`skills/implement/orchestration.md` now reads "This is the last routing
question: the run stops again only for what only you can decide and would
be costly to undo." Box 1's Checked cell says the run stops only for what
only the person can decide. Both READMEs' opening paragraph and *Your first
work item* bullet say the same, in one commit. Box 1's label "run end to
end without stopping to ask" stays, because
`tests/behaviour/test_waiver_decided_at_start.py` pins it and the Checked
cell under it carries the condition. The paragraph of `the-run.md` said the
person "was told that the run would not stop to ask", and now says what
they were told. The plugin's one-line description, "without asking
anyone", stands, and `gaps.md` *Not done* says where and why.

**The cases of later phases' hooks that ran the removed gates were moved
to gates that stay.** After this phase no registered gate prints a
decision. In `tests/hooks/test_dispatch.py` a case about how a decision
passes through a group plants a denier in a copy of `hooks/`: `DENIES` as
`denies.py` in a patched `GROUPS`, or over `implementer-mark.py` at
`pre-agent`. A case about a broken gate breaks `sealer-stamp-queue.py` at
`post-edit` through the new `edit` payload, since that group stands until
phase 4. The unreadable-shape case plants its shape at `pre-agent` and its
message at `post-edit`. The hostile-console case of `Test_main` plants
`DENIES_WITH_THE_COMMAND`, so the reason it reads back is the payload's
command. S6 and S6b name `implementer-mark.py`, `implementer-notice.py` and
`sealer-stamp.py`. The two-groups case of `describe` plants its four groups,
since no gate sits in two groups of today's `GROUPS`. The lint-python argv
case went with its gate. `tests/hooks/test_console.py` runs
`hooks/sealer-stamp.py` on its own on a hostile console, with a stamp
written for its session, and reads `SEALED` back. `tests/hooks/test_optin.py`
lost the three review-skill-gate cases and the two version-check cases, and
its scratch-marker case keeps `implementer-notice.py`.
`tests/hooks/test_config.py`'s refusal case lost its mode-gate half.

**Seen red.** Sixteen `seal mutate` runs after the build commit `3f2be2b7`
and the docstring commit `442d21a3`, each exit 0 with the verdict `red`:

- `hooks/dispatch.py`, the stdin reconfigure without `encoding`, against
  `-k console_cannot_decode`: 3 failed.
- `describe`'s group expansion emptied, against `-k every_group_that_loads`:
  1 failed.
- `if kind == "unreadable":` never taken, against
  `-k not_a_hooks_output_and_ends_nothing`: 1 failed.
- `RANK` without `deny`, against the two crash cases, `Test_main`'s group
  case, the unknown-group case and the hostile-console case: 7 failed.
- `path_part` without its `.` and `..` guard, against
  `-k outside_the_records`: 1 failed.
- `opted_in`'s fallback `return True` as `return False`, against
  `-k broken_opt_in_module`: 1 failed.
- the draw's sort reversed, against `-k oldest_first`: 1 failed.
- `run_gate`'s load-failure append as `pass`, against S6, S6b, the
  end-of-turn case, the run-failure case, the walk-twin case and three
  `Test_record` cases: 6 failed and 3 passed. The three passed cases call
  `record` directly or compare a broken gate with an absent one, which the
  append does not reach.
- `hooks/sealer-stamp.py` without `console.to_utf8()`, against
  `tests/hooks/test_console.py -k on_its_own`: 3 failed.
- `skills/update/SKILL.md` with "so restart for those" as "so reload for
  those", against the new release-hygiene case: 1 failed.
- `broad_gate.py`'s fenced and commented messages each put back to name the
  mode gate, against the two pinned cases: 1 failed each.
- `skills/code-review/SKILL.md` without "and naming no skill", and without
  "by name", against the new description case: 1 failed each.
- `README.md` with "No hook reaches the network." changed, against the
  network case: 1 failed.
- `skills/implement/SKILL.md` with the lint sentence changed, against
  `tests/text/test_the_rules_claude_md_names_have_one_home.py`: 1 failed.

The phase adds no behaviour to shipped code; the runs show each moved,
rewritten or added case can fail. `tests/hooks/test_config.py`'s refusal
case kept the half that stood, so it owes no run.

**The phase boundary set.** The modules that name a changed path or import
a changed module were listed by `git grep -l -E` over `tests/` for the
changed files' paths and names, 117 modules, with `tests/text/` and
`tests/hooks/` whole. One command through `bin/test` over the tree the
build commit `3f2be2b7` holds, run just before it was committed: 5,671
passed, 10 skipped, exit 0. `442d21a3` after it changes one docstring. An
earlier, narrower run over the plan row's modules and the touched modules
failed two cases of `tests/behaviour/test_docs_line_wrap.py` on lines this
phase spliced past 88 columns in `skills/implement/SKILL.md` and
`README.ko.md`, and those lines were rewrapped before the commit. The plan row's command, `bin/test
tests/behaviour/test_first_setup_asks_once.py
tests/behaviour/test_chain_hooks_hardening.py tests/text/`, passed 525, exit
0. `seal rules --check` exited 0 with 220 check lines in 70 rule files, and
`seal layout --check` exited 0. `uvx ruff check` and
`uvx ruff format --check` over the changed Python files exited 0. The plan
row's `git grep` for the phase's names, both greps above, lists these lines
outside `seal/threads/` and `.test_durations`, and none states a removed
unit as present:

- `hooks/lib/cmdline.py:18` records a measurement of a `dispatch.py
  pre-bash` call. The module goes in phase 4.
- `tests/hooks/test_dispatch.py:809,812` use `session-start` as the group of
  a record another version wrote, which is the case's point.
- The docstrings of the new description case, of the new release-hygiene
  case and of `test_a_rider_reaches_its_file.py:101` name the review-skill
  gate or the session-start notice as what left.
- `skills/settle/SKILL.md:82`, `skills/settle/scripts/rule_changes.py:648`
  and `tests/skills/test_settle.py:3081,3099` name "the session-start move",
  an earlier release's move of the thread layout, not a hook.
- `tests/behaviour/test_the_release_check_watches_what_ships.py:303` names
  the release workflow's version check, not the hook.

`.test_durations` keeps the removed cases' ids for CI's rebuild, as phase
1's judgment row states.
