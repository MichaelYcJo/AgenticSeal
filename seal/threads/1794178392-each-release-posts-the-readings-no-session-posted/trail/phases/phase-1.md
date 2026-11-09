# Phase 1: 1794178392-each-release-posts-the-readings-no-session-posted

## What this phase found

**The frame holds for this phase.** Its precondition holds: #1440 merged
into `release/v0.36.0` as `74211b76`, and this branch merged that in at
`e8241733`. Between the frame's commit and `e8241733`, only `74211b76`
touched `skills/verify/scripts/session_cost.py`, its test module,
`README.md`, `README.ko.md`, `skills/verify/orchestration.md`,
`docs/running/measuring-a-run.md`, `docs/releasing/release-checklist.md`,
`tests/text/test_a_segment_feeds_the_flow_log.py` and `lib/routing.py`
(`git log 94d04d30..e8241733` over those paths). That commit moved the line
numbers `frame/plan.md` *Technical context* gives, which state `1f7aaa66`.
At `e8241733`, `report` stands at line 2102, `report_segments` at 2536,
`open_log` at 2829, `post` at 2898, `emit` at 2973 and `main` at 3036.
`projects_dir`, `subagent_transcripts`, `measure_segments` and
`lib/routing.py#parse` stand where the plan says.

**A `slowest` row now carries its call's family.** `analyse` adds a
`family` key to each row, with the value its `by_family` table charges the
call to: `family(ran)` for a `Bash` call and the tool's name otherwise. It
is computed once per call, in the loop that builds `by_family`. `report`
cannot derive the family itself, because a row keeps the command flattened
and cut to 110 characters, while `family` reads the command as the harness
recorded it, newlines kept (#377). So `--json` gains one key in each
`slowest` row, and no number moves. Judged against `analyse`'s docstring,
which forbids moving a number of the plain reading, and `frame/design.md`
*Scope* item 7.

**Departure from `frame/design.md` *Data & interfaces*: `main` decides the
form, not `emit`.** The design says `emit` uses the form without command
text for the captured body alone. `emit`'s `render` is a callable with no
arguments, and the three reports share it. Only `report` prints command
text. So `main`'s `render` calls `report(data, commands=not args.post)`,
and the result is the same: the posted body has no command text, and the
printed reading is unchanged. Passing the flag through `emit` would add a
parameter to three callables, and two of them would ignore it.

**The `# <file name>` lines are written by `emit`, after the path
replacement and before the report.** `emit` takes `read_from`, the
transcripts a row was measured from, beside `path`. It names `path` first,
then each other file once, in order, by its base name. For `--segments`,
`main` passes each row's `transcript`. A resumed agent's file is two rows
and one line. Given an agent's own file, the row's transcript is the given
file's name, so the fence names it once. The plain reading and `--spawns`
pass nothing beyond `path`. The line goes into the captured body only.
`comment_body` fences the whole reading, so the lines open the fence.

**`README.ko.md` changed beside `README.md`.** The frame names only
`README.md` for the `seal cost --post` row (*Scope* items 6 and 7).
`CONTRIBUTING.md` *House rules*, the bullet **Both READMEs move together,
and so does every document with a `.ko.md` edition**, requires the Korean
edition to say the same. So its row says the same two things: each
transcript by file name, and no command text.

**The step 2 sentence of *Scope* item 6 is in.** `skills/verify/orchestration.md`
*Measure the segment, and feed the flow log*, step 2, says the fence opens
with one `# <file name>` line for each transcript the reading was taken
from. The rest of *Scope* item 6 is phase 2's. That covers the paragraph
opening **The command does not make anybody run it.**, the deadline and
the `README.md` `When` cell and command row.

**`emit`'s docstring was corrected.** Its *residual* paragraph said that no
report line printed an absolute path other than the transcript's. The
`slowest` list and the `other` note print command text, and a command can
name any path. The paragraph now says so, and says that `main` asks for the
form without command text wherever the reading is posted (`9c2c8684`).

**Seen red.** The five new cases in
`tests/skills/test_session_cost.py::Test_emit` ran against `e8241733`'s
`emit` and `report`, and all six items failed (`bin/test
tests/skills/test_session_cost.py -q -p no:xdist -k "Test_emit and
(opens_its_fence or names_the_run or named_once or no_command_text)"`,
exit 1). Each failed on its own guard:

- `test_a_posted_reading_opens_its_fence_with_the_transcripts_name[plain]`:
  `assert 'span        ...1 tool calls)' == '# t.jsonl'`
- `...[spawns]`: `assert '0 spawns found in t.jsonl' == '# t.jsonl'`
- `test_a_posted_segments_reading_names_the_run_and_each_agent_file`:
  `assert [] == ['main.jsonl'...roofer.jsonl']`
- `test_a_resumed_agent_file_is_named_once_and_not_once_per_slice`:
  `assert [] == ['main.jsonl'...rafter.jsonl']`
- `test_a_posted_body_carries_no_command_text`:
  `assert '/opt/private-x' not in ...`, the body holding
  `Slowest command charged there: /opt/private-x/bin/deploy --wait`

**Mutation.** One `seal mutate` call over
`skills/verify/scripts/session_cost.py`, eight mutants, the same five cases
with `-x -p no:xdist`. Its baseline passed, and all eight came back `red`
(exit 0). The mutants were: no `# ` lines; `read_from` not read; the
de-duplication removed; the `slowest` list printing the command where it
is posted; the `other` note keeping the command where it is posted; `main`
asking for commands where it posts; a wrong family in `analyse`; and
`--segments` passing no row transcripts. `git status` was clean afterwards.

**Phase boundary.** One `bin/test` command ran over 43 modules: this
module, the modules that name `session_cost.py`,
`skills/verify/orchestration.md` or the root `README.md`, and those that
walk the tracked tree's Markdown or Python. The list is in the hand-back.
The run gave 2097 passed, 7 skipped and 1 failed (exit 1). The failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which refuses a framed work item without `gaps.md`. This phase writes that
file when it closes. With the phase's records written over `9c2c8684`, the
same command gave 2098 passed and 7 skipped (exit 0).

**For phase 2.** The reader that leaves out posted segments matches the
line `emit` writes: `# ` and a base name ending in `.jsonl`, inside the
fence. `emit(args, render, path, read_from)` is the seam where a
`--work-item` reading names its transcripts. Where that reading has no
single given transcript, `path` can be `None`, and `emit` then names only
`read_from`.
