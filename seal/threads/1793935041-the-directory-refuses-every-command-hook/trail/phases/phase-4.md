# Phase 4: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase.** Every coordinate of the phase row stood
at `fae5966f`. `hooks/lib/cmdline.py` had one importer,
`hooks/implementer-notice.py`, and `hooks/lib/implementer.py` had the two
implementer hooks alone, as *Scope* item 6 says. The sentence that cited
the notice in `skills/implement/orchestration.md` was the Planning
paragraph, near line 326. `docs/checks/the-session-hooks.md` held *The
implementer mark and notice* as its own section. The folded part of
*Scope* item 1 asked for three things, and each was buildable as written:
the entry invoked by the model, question 1 put every time with the
ladder's answer marked, and the review skill opening the core once. The
phrase "without asking anyone" stood at the four places the row names,
with two copies in `marketplace.json`.

**Part 1, the implementer mark and notice.** The four modules and their
four test files left with `git rm`. `hooks/hooks.json` lost the
`PreToolUse` `Agent|Task` entry and the `PostToolUse` `Bash` entry, and
`hooks/dispatch.py#GROUPS` lost `pre-agent` and `post-bash`. Two groups
remain, `post-edit` and `stop`, for phase 5. `agents/sealer.md` step 4
gained one sentence. Where `routing.md`'s `Implementation` row reads
`crafter`, every phase of `frame/plan.md` whose Status cell holds a commit
has its `trail/phases/phase-N.md`. A declared party that left no record is
a `withheld` reason that names the phase. The new case
`tests/behaviour/test_the_sealer_guarantees.py#TestDefinition::test_step_4_withholds_where_a_declared_crafter_left_no_phase_record`
pins four phrases of that sentence. It was seen red against the tree
before the sentence was written.

**Part 2, the entry takes a plain request.** `skills/start/SKILL.md` lost
`disable-model-invocation: true`. Its description now has the shape the
other model-invoked skills have. `Use when:` claims a request, in plain
words, to change code where the plugin is installed, or a typed
`/agentic:start <issue or request>`. `NOT for:` names a question about how
code works, a review request, which is `code-review`'s, and a session
already orchestrating a work item. Where `$ARGUMENTS` is empty, the
request is the person's message that brought the session to the skill.
Step 4 reads the ladder for which answer of question 1 to mark, and says
the ladder never skips the question. Step 5 puts question 1 with that
answer marked. A `no work item` answer makes the change as the third
answer of *Question 1* describes, and takes none of the later steps. The
sentence "The steps below are then not taken", which let the ladder skip
the question, is gone. `skills/implement/orchestration.md` gained the rule
under *Question 1*. Question 1 is put every time, whatever the ladder
reads. On the ladder's last rung the orchestrator marks `no work item`,
and on either rung above it marks `automation`. The mark is
` (Recommended)` after the label, and the options keep the table's order.
`skills/code-review/SKILL.md` now opens the core once, by the entry's
step 1, before it follows its orchestration file. Three new cases pin
these, each seen red against the tree before its text was written:
`tests/behaviour/test_chain_hooks_hardening.py#test_a_plain_request_to_change_code_is_the_entrys`,
`#test_the_review_skill_opens_the_core_once_where_it_orchestrates`, and
`tests/behaviour/test_waiver_decided_at_start.py#test_question_1_is_put_every_time_with_the_ladders_answer_marked`.
The marketplace case in `test_chain_hooks_hardening.py` gained an
assertion that the published description does not hold "without asking
anyone". It was seen red before the four descriptions changed.

**One departure from the frame: the implement skill's `NOT for:`.**
`skills/implement/SKILL.md`'s description claims "implementing a feature,
starting a ticket". With `start` model-invoked, two descriptions would
claim the same plain request, and the model would pick one by wording.
The implement skill's `NOT for:` now names a plain request to change code
that no work item has started yet, which `start` takes first. The row did
not name this edit. It was judged against `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: a request a model reads
should have one owner. Whether the model follows the split is a
`gaps.md` *Not verified* row.

**Units removed that the frame's `## Removes` does not name.** Each was
read by the removed hooks or their tests alone. Each was judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*, which
removes in the same commit what stood on the old fact.

- `hooks/lib/routing.py#for_branch`, `worktree_branch`, `unborn_branch`
  and `rebase_branch`. `git grep` found their callers in
  `hooks/implementer-notice.py`, `hooks/lib/implementer.py` and their tests
  only. The module's docstring and the `parse` and `item_dir` docstrings
  now name the readers that remain: `chain_check.py` reads `Planning`, and
  the sealer reads `Implementation` (`agents/sealer.md` step 4).
- `tests/conftest.py#branch_of`, `git_dir`, `opt_in`, and the block headed
  "the implementer family's declaration and calls": `ITEM`,
  `run_dispatch`, `declare`, `declare_crafter`, `spawn` and `bash`. No
  remaining module imports any of them.
- `tests/skills/test_seal.py#BESIDE_THE_ROOT` lost `agentic-implementer`
  and `agentic-planner`. No shipped script writes either file now.

**The cases of the remaining groups were moved to gates that stay.**
`tests/hooks/test_dispatch.py` ran the implementer gates as its examples.
A case about a group's shape now plants a group in a copy of `hooks/`
(`pre-planted`, `pre-x`, `post-x`), or names a gate that is gone
(`gone-a.py`, `gone-b.py`) where the case reads a record and no gate runs.
A case about a broken shared module breaks `lib/console.py`, which both
stamp gates import, or `lib/optin.py`, which `sealer-stamp.py` imports.
`Test_main` plants its denier over `sealer-stamp-queue.py` at `post-edit`.
`Test_module` asserts `sorted(GROUPS) == ["post-edit", "stop"]`.
`tests/hooks/test_optin.py`'s scratch-marker case now writes a stamp for
its session in local mode and reads that `sealer-stamp.py` draws nothing
while the marker stands. `tests/behaviour/test_first_setup_asks_once.py`'s
gates-table case now names the `sealer-stamp` row as the opt-in row it
reads. `tests/skills/test_seal.py`'s export and import cases now plant
`agentic-last-export.json`, a file that still stands beside the root, in
place of `agentic-implementer`.

**Statements of the removed units edited beyond the Delivers cell.** The
method was `git grep -n -E` over the tree, outside `seal/threads/` and
`.test_durations`, for `implementer-mark`, `implementer-notice`,
`implementer_mark`, `implementer_notice`, `hooks/lib/implementer`,
`hooks/lib/cmdline`, `cmdline.py`, `implementer.py`, `pre-agent`,
`post-bash`, `for_branch`, `agentic-implementer` and `agentic-planner`.
A second grep looked for the reworded rules: `types \`/agentic:start`,
`never types`, `user-invoked`, `without asking anyone`, `아무에게도 묻지`
and `The steps below are then not taken`. The list is the closed set for
these words. Each line below stated a removed unit or the old entry rule,
and is edited in this phase:

- `README.md` and `README.ko.md`: the opening sentence, *Your first work
  item*, the routing question's sentence, *How it works*, the Core row, the
  skills row, where `start` joins the list a session loads on its own, the
  `/agentic:start` row of the commands table, the first bullet of
  *Limits*, and the two implementer rows of the gates table.
- `CLAUDE.md`: the core paragraph names the entry skill, invoked by the
  model or typed.
- `CONTRIBUTING.md:484`, `SECURITY.md`'s hooks bullet,
  `docs/README.md`'s row for `the-session-hooks.md`, and the opening of
  `docs/checks/the-session-hooks.md`.
- `docs/checks/the-routing-check.md`'s limit sentence names a session the
  entry skill never reached.
- `.claude-plugin/plugin.json` and both descriptions in
  `.claude-plugin/marketplace.json`.
- `hooks/sealer-stamp.py`'s docstring cited `implementer-notice.py` for its
  silent shape and `implementer.py` for its stance. Each sentence now
  states the ground itself.

`SECURITY.md` was not in the row. Its bullet named agent spawns and
commits as times a hook runs, which stopped being true in this phase, so
it now names a file edit and the end of a turn. Phase 5 still rewrites
that bullet when the last hooks leave.

**Seen red.** Seven `seal mutate` runs after the build commit `d8f69f7c`,
each exit 0 with the verdict `red`:

- `hooks/lib/optin.py`, the scratch-marker condition as `if False:`,
  against `tests/hooks/test_optin.py -k scratch_marker_under_the_common`:
  1 failed.
- `hooks/dispatch.py`, the load-failure append as `pass`, against the
  shared-module, subagent-stop and broken-opt-in cases: 4 failed.
- `hooks/sealer-stamp-queue.py`, `import console` as
  `import console, optin`, against the shared-module case: the `optin`
  parameter failed.
- `hooks/dispatch.py#GROUPS` with a `pre-agent` group added, against
  `-k no_group_installs`: 1 failed.
- `hooks/dispatch.py#RANK` without `deny`, against the cases that read a
  decision through a group: 6 failed.
- `skills/start/SKILL.md` with the skip sentence put back, against
  `-k every_time`: 1 failed, on the `not in` line.
- `README.md` with the `sealer-stamp` row renamed, against the
  gates-table case: 1 failed.

The phase removes behaviour and adds text. The runs show that each moved
or rewritten case can fail. Units only removed owe no run.

**The phase boundary set.** The modules that name a changed path or import
a changed module were listed by `git grep -l -E` over `tests/` for the
changed files' paths and names. `tests/conftest.py`'s needles were left
out, since every module loads it and no remaining module imports a removed
helper. The set was 119 of the 135 modules: 94 by name, with
`tests/text/`, `tests/behaviour/`, `tests/hooks/` and
`tests/skills/test_seal.py` whole. One command through `bin/test` over the
tree `d8f69f7c` holds: 5,050 passed, 10 skipped, exit 0. The plan row's
command, `bin/test -q tests/behaviour/ tests/text/`, passed 1,788 with 9
skipped, exit 0. `seal rules --check` exited 0 over 219 check lines in 70
rule files. `seal layout --check` exited 0 with 135 files read and none
refused. `uvx ruff check` and `uvx ruff format --check` over the changed
Python files exited 0.

The read of the range against HEAD found three passages spliced past 88
columns. They were in `hooks/lib/routing.py`'s module docstring,
`hooks/sealer-stamp.py`'s silent-failure paragraph and
`docs/checks/the-routing-check.md`'s limit paragraph. The read also found
a doubled verb in `README.md` *How it works*, "starts, starts with". Commit
`396f91b9` corrects the four. The touched modules,
`tests/behaviour/test_docs_line_wrap.py`,
`test_waiver_decided_at_start.py`, `test_chain_hooks_hardening.py`,
`test_first_setup_asks_once.py`, `tests/hooks/test_routing.py`,
`test_sealer_stamp.py` and `tests/text/`, passed 679, exit 0, before that
commit.

**The census of the phase's names.** The plan row's `git grep` for the
names above lists these lines outside `seal/threads/` and
`.test_durations`. None states a removed unit as present:

- the guard cases themselves, which assert that a phrase is absent;
- `disable-model-invocation` in the other user-invoked skills;
- `tests/text/test_a_rider_reaches_its_file.py:99`, which names
  `hooks/lib/cmdline.py` as the file whose rider left with it;
- the sealer case's docstring, which names the hooks that left.

`/agentic:start` stands in `skills/core/SKILL.md:7`, `CLAUDE.md`,
`docs/layout/the-record-layout.md:176`, `skills/implement/orchestration.md`
at three places, `docs/checks/the-routing-check.md:14`,
`skills/update/SKILL.md:137` and `skills/verify/scripts/payload_meter.py`.
In each it is the skill's name, the step the skill runs, and not a claim
that a person typed it, so each stands.

Three lines are left for phase 5, which removes what they describe.
`hooks/sealer-stamp.py:55` calls the queue hook "the edit gate".
`docs/checks/the-session-hooks.md` keeps its paragraph on merging
`PreToolUse` decisions, though no `PreToolUse` group is registered. The
merge code in `hooks/dispatch.py` stays until then. `.test_durations`
keeps the removed cases' ids for CI's rebuild, as phase 1's judgment row
states.
