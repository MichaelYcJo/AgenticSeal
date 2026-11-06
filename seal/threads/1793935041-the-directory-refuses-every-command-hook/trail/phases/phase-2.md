# Phase 2: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase except on `hooks/lib/gate.py`, which stays.**
The frame's `## Removes` names it "the deny helper", with the ground "no gate
prints a decision", and *Grounding* says it is imported by hook scripts and
their tests alone. At `e666b0d5` no hook imports it. Its one reader is
`skills/code-review/scripts/chain_check.py#parity_readers`, which loads it by
path, and `#originals_of` asks its `touches_code` whether a pull request's
paths reach outside `docs/` and `seal/`. `docs/running/the-review-and-parity-arms.md`
*Parity arm* states that rule with a `check:` line naming
`tests/hooks/test_gate.py`. Removing the module would take a pull-request
arm with it, so the build keeps the module and its test. This was judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against*: the
module is a reader of the pull request's check, not a hook's helper. Every
other coordinate of the phase row stood at `e666b0d5`.

**The closed set of statements on the removed units reached past the
Delivers cell, and each was edited in this phase.** The method was
`git grep -n -E` over the tree, outside `seal/threads/`, for
`question-gate`, `routing-edit-gate`, `lib/press`, `import press`,
`hooksession`, `no-work-item`, `no_work_item`, `NO_WORK_ITEM`, `pre-edit`,
`pre-question` and `The edit check`, then a second grep for the sentences
that state the edit check or the question gate in other words: `edit check`,
`edit gate`, `edit hook`, `refuses the edit`, `the press`, `question 1
again`, `stated default` and `No person is asked mid-run`. The edits beyond
the Delivers cell, each on the ground that the sentence stated a removed
unit:

- `skills/agent-contract/SKILL.md` rule 9 lost its sentence "The routing
  check sees only the edit tools", which cited *The edit check*. No check
  reads an edit now. The docstring of
  `tests/text/test_edits_go_through_the_edit_tool.py` says so.
- `skills/implement/SKILL.md` *Commit at the smallest step*,
  `docs/layout/the-record-layout.md` on the `routing.md` exception to the
  comment refusal, `CONTRIBUTING.md`'s paragraph on a contributor's machine
  having no routing edit gate, and `docs/README.md`'s row for the routing
  check each stated the edit check, and now state the pull request alone.
- `docs/checks/the-fold.md`, `docs/releasing/release-checklist.md` and
  `skills/settle/SKILL.md` said a settle runs `seal no-work-item`; each now
  says its commits carry the trailer. The case that pinned the command,
  `tests/text/test_settle_reads_before_it_removes.py`, keeps its trailer
  assertion and is renamed `test_the_skill_names_how_a_settle_commits`,
  since it no longer reads how a settle edits.
- `skills/code-review/orchestration.md`'s paragraph on a fix pass in a new
  session said the orchestrator puts question 1 again for the press. It now
  says the orchestrator reads `routing.md` and asks nothing again.
- Both READMEs' *Your first work item* said the hooks read `routing.md` and
  that a question under `automation` is refused. They now say the pull
  request's check reads it and state the new guidance in one sentence each.
- `skills/commit-pr-convention/SKILL.md`'s trailer example had the subject
  "the edit check refuses an undeclared branch". It now shows a subject this
  plugin's present can carry.
- `skills/start/SKILL.md` step 4 said every commit of a change with no work
  item ends with the trailer. The third answer of *Question 1* says that
  holds where the root is shared, so step 4 now cites it.
- `.github/ISSUE_TEMPLATE/gate-misfired.md` named both removed gates in its
  `about:` line and its example. They now name a gate or the pull request's
  check. Phase 5's rewrite of the template stands.
- `hooks/implementer-mark.py` and `tests/hooks/test_implementer_mark.py`
  said the branch is resolved "as the edit gate resolves it"; both now name
  `routing.worktree_branch`.
- `bin/seal`'s comment listed `seal no-work-item`; `seal.py`'s help text did
  too, under "One more subcommand records a fact about the session".

**Three units left that the frame's `## Removes` does not name.**
`hooks/lib/routing.py#declared` had one reader, `hooks/question-gate.py`,
and no case. `tests/conftest.py`'s press block, `_no_real_transcripts`,
`ask_entries`, `write_transcript`, `ROUTING_QUESTION` and `ROUTING_OPTIONS`,
was read by the press's and the two gates' tests alone. `seal.py`'s
`import routing` and the `routing.py` row of `HOOK_PURPOSES` stood on
`seal no-work-item` alone. `frame/design.md` *Data & interfaces* says
`HOOK_PURPOSES` "reads `routing.py`'s purpose as the reader of a
declaration". At this phase `seal.py` reads no declaration, so the row goes
with the import. Phase 7 has no `routing.py` row to rewrite.

**`routing.py`'s docstrings and comments said the gate asks again, or the
edit gate refuses, in the module docstring and in `parse`, `current_branch`,
`worktree_branch` and `declarations`.** Each now
says the pull request's check reads the branch as undeclared, that the file
is no declaration, or which unit resolves the branch. The `Automation` comment and
`parse`'s paragraph on the row say no script decides anything on it and the
orchestrator reads it. The design's *Data & interfaces* names the sealer as
a second reader, and `agents/sealer.md` names no read of the row, so the
build states the orchestrator alone. The `rounds` docstring said "the reader
four gates depend on". No gate reads `rounds`, and its readers are
`.github/scripts/finding_counts.py`, `release_seal.py` and `settle.py`, so
it now names them.

**The automation rule is guidance with no check line.** It stands in
`docs/running/the-run.md` *The run*, in the paragraph opening **On a run
whose `routing.md` reads `Automation` `yes`**, written to *Scope* item 3's
sense and to `skills/writing-style/SKILL.md`'s rules for text an agent
reads: the orchestrator is named as the party, the tree and
`frame/questions.md` as where it looks, and the row and the pull request
line as what ends the step. `skills/implement/orchestration.md` cites the
paragraph by its opening words in two places, the end of *Once the batch is
answered* and the paragraph **`Automation` is a record, and no script
decides anything on it**.

**The cases of later phases' hooks that ran the removed gates were moved to
a gate that stays.** `tests/hooks/test_dispatch.py`: the two crash cases now
pair the failing gate with `mode-gate.py` and a Bash payload in place of
`routing-edit-gate.py` and an `Edit`. S6's `press` parameter became
`config`, the module `mode-gate.py` imports, and `both` now breaks
`cmdline.py` with `config.py`. The record list of the oldest-first case
names `review-skill-gate.py` in place of `routing-edit-gate.py`. S2's second
half, a broken and an absent `routing-edit-gate.py` at `pre-edit`, went with
its group, and the `edit` payload helper went with its last caller.
`tests/hooks/test_console.py` runs `mode-gate.py` on its own on a hostile
console. `tests/hooks/test_optin.py`'s scratch-marker case lost its
edit-gate assertion and keeps the two gates that stand.

**Seen red.** Four `seal mutate` runs, each exit 0 with the verdict `red`:

- `hooks/mode-gate.py` with `console.to_utf8()` taken out of its `__main__`
  block, against `tests/hooks/test_console.py -k a_gate_run_on_its_own`: 3
  failed.
- `hooks/dispatch.py` with `pre-bash` emptied, against
  `tests/hooks/test_dispatch.py -k 'shared_module and config'`: 1 failed,
  the new `config` parameter.
- `hooks/mode-gate.py` with its first decision `deny` read as `allow`,
  against `tests/hooks/test_dispatch.py -k 'crashing_gate_take or
  system_exit_at_load'`: 2 failed.
- `skills/implement/orchestration.md` with `` `Seal-Routing: no work item` ``
  cut to `` `Seal-Routing` ``, against
  `tests/behaviour/test_waiver_decided_at_start.py -k
  names_the_record_and_no_per_command_waiver`, the case whose needle moved
  from `seal no-work-item` to the trailer: 1 failed.

The phase adds no behaviour, so no unit owes a mutation run of its own.

**The phase boundary set.** The modules that name a changed path, import a
changed module, or are among the plan row's and `tests/text/` were listed
by `git grep -l -F` over `tests/` for each changed file's path and name:
121 of the tree's 143 test modules. A glob reading, which adds every module
that walks `docs/`, `skills/`, `hooks/` or `agents/`, lists all 143, which
is the suite, so the named set is the one run. One command at the build
commit, `e29a20ba`: 5,040 passed, 10 skipped, exit 0. An earlier run of the
same set, before the commit, failed two cases of
`tests/behaviour/test_docs_line_wrap.py` on lines this phase rewrapped past
88 columns, and those lines were rewrapped before the commit. The plan row's
command, `bin/test tests/behaviour/test_waiver_decided_at_start.py
tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_seal.py
tests/hooks/test_routing.py tests/text/`, passed 940, exit 0.
`seal rules --check` exited 0 with 220 check lines in 70 rule files, and
`seal layout --check` exited 0. The plan row's `git grep` for the phase's
names, run as the first grep above, lists one line outside `seal/threads/`
and `.test_durations`: the parameter id `adds-no-work-item` in
`tests/evals/test_seed_defects.py`, which names a seeded defect and not the
command.
