# Review round 2: 1794986401-the-process-has-no-name

```seal
target: abd417cd6, fixes 3226fdf5a..abd417cd6
```

This is a verifying round. It answers round 1's four findings, all closed
`fixed bc092878b`, and reviews the diff of the fixes, `3226fdf5a..abd417cd6`,
in a `git clone --no-local` checked out at `abd417cd6`. The code read stays
inside that diff. The work item's records were each read whole at
`abd417cd6`: `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`.
`seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed and none stands. `seal/parity.json` is not declared.
Issue #1557 was read again with `gh issue view 1557 --json
title,body,comments`: no comment, and its *Decision* and *Change* are the
ones `frame/design.md` G1 reports.

Carried from round 1 and not re-established: its reading of the 106
`the workflow` lines under `tests/` at `c637848af`, that all but three name
a GitHub Actions workflow; its reading of `CONTRIBUTING.md`'s other
`workflow` lines as GitHub Actions lines; and its confirmations of
*Data & interfaces* D1 to D5, which stand outside the fix diff. Re-run
here: the three counts round 1 executed, the eight modules the fix pass
ran, and the width of each line the fix pass wrote.

The fix pass lengthened `tests/behaviour/test_chain_hooks_hardening.py:417`
to 78 columns, as round 1's own snippet did. That is no finding: the
paragraph's first line, `:415`, was already 79 columns, ruff's
`line-length` is 88 (`pyproject.toml:25`), and no record claims the line
is within 76.

## Findings

### 1. `pr.md:1` quotes `gaps.md` *Not done* in words the fix pass replaced, so the quote no longer stands at its source

```seal
severity: should
location: `seal/threads/1794986401-the-process-has-no-name/pr.md:1`, `seal/threads/1794986401-the-process-has-no-name/gaps.md:13`
evidence: executed a Python comparison of each of the seven `pr.md` quotes with its source, runs of whitespace collapsed; read `seal/threads/1794986401-the-process-has-no-name/pr.md:1-7`, `seal/threads/1794986401-the-process-has-no-name/gaps.md:13`
regression: round-1#2
```

Why it matters: the unit is `gaps.md:13`, the *Not done* sentence that
commit `bc092878b` rewrote. `frame/plan.md` *Judgments of the run* has no
row for that sentence, and round 1 finding 2 asked only for a sentence
naming any line the fix pass kept. The fix pass inserted a clause into the
sentence's middle and left `pr.md` as it was, and that is where the defect
came from. `pr.md:1` quotes "in `docs/`, `skills/` and `agents/`, keep the
word, by the owner's scope". The source now reads "in `docs/`, `skills/`
and `agents/`, and in test docstrings and comments other than those *Scope*
item 4 names, keep the word". Six of the seven quotes match their sources,
and this one does not. `seal pr-body` composes the pull request body from
`pr.md`, so the body would quote the closing memo in words it does not
hold.

The fix follows finding 2. Where finding 2's snippet is applied, the first
sentence of `gaps.md` *Not done* returns to the words `pr.md:1` quotes, and
`pr.md:1` holds unchanged. Where the fix pass keeps the clause instead,
`pr.md:1` quotes the sentence as it stands:

```markdown
- "The places outside `frame/design.md` *Scope* where "the workflow" means the process, in `docs/`, `skills/` and `agents/`, and in test docstrings and comments other than those *Scope* item 4 names, keep the word, by the owner's scope (issue #1557 *Decision*)." (`gaps.md` *Not done*)
```

### 2. `gaps.md` *Not done* calls the list of remaining places a sample and files test docstrings under the owner's scope, though one search makes the list whole and it holds one more docstring naming the process

```seal
severity: should
location: `seal/threads/1794986401-the-process-has-no-name/gaps.md:13`, `tests/behaviour/test_the_contributor_has_a_procedure.py:2`, `seal/threads/1794986401-the-process-has-no-name/frame/design.md:27`
evidence: executed `git grep -n -i workflow -- . ':!seal/threads' ':!docs' ':!skills' ':!agents'` at `abd417cd6`, 623 lines, each line read or matched by pattern as the Probes row states; read `tests/behaviour/test_the_contributor_has_a_procedure.py:1-2`, `CONTRIBUTING.md:56-60`, `seal/threads/1794986401-the-process-has-no-name/frame/plan.md:44`, `seal/threads/1794986401-the-process-has-no-name/frame/design.md:30-32`
regression: round-1#2
```

Why it matters: the unit is `gaps.md:13`, which commit `bc092878b`
rewrote. The frame's *Out* list, at `frame/design.md:32`, leaves "the
workflow" only in `docs/`, `skills/` and `agents/`. The fix pass's own
judgment row, at `frame/plan.md:44`, renamed the lines round 1 named
because "none falls under *Scope*'s *Out*, which names `docs/`, `skills/`
and `agents/`". The fix pass then wrote into `gaps.md:13` that the other
test docstrings and comments keep the word "by the owner's scope", which
neither *Out* nor that row says, and that is where the defect came from.
The sentence adds that the list "is a sample". Contract rule 12 keeps a
list a sample only where no method makes it whole. One `git grep` over the
word lists every line that could name the process outside the three
directories.

That search was run here, and it prints 623 lines. One of them names the
process and is not in *Scope* item 4:
`tests/behaviour/test_the_contributor_has_a_procedure.py:2`, "and what this
repository's own workflow does not ask of them". That docstring states what
`CONTRIBUTING.md` *What a contribution is not asked for* says, and round 1
finding 1 renamed that section's opening to "This repository runs the
AgenticSeal process on itself". So the docstring is a copy of the renamed
fact, the kind round 1 finding 2 asked to be renamed. The sealer reads
`gaps.md` as the build's account of what it left, and this sentence tells
it the rest cannot be listed and was left by the owner.

The fix renames the docstring, names it in *Scope* item 4, and replaces the
`gaps.md` sentence with one the search makes whole. The paragraph is
refilled to 76 columns.

```python
"""`CONTRIBUTING.md` tells an outside contributor where a pull request goes,
and what the AgenticSeal process this repository runs on itself does not
ask of them.
```

```markdown
4. `lib/optin.py`'s docstrings and comments, the sentence at `lib/core.py:14` that restates them, the docstrings at `tests/lib/test_core.py:219`, `tests/skills/test_seal_stamp.py:1564` and `tests/behaviour/test_the_contributor_has_a_procedure.py:2`, the comment at `tests/behaviour/test_chain_hooks_hardening.py:415-419` that names the README's network row, `CONTRIBUTING.md:58`, `templates/setup/seal-README.md` with `seal/README.md`, the header comment of `templates/setup/hygiene.yml`, and the row of `docs/layout/one-root-by-lifetime.md` and its Korean edition use the name.
```

```markdown
The places outside `frame/design.md` *Scope* where "the workflow" means the process, in `docs/`, `skills/` and `agents/`, keep the word, by the owner's scope (issue #1557 *Decision*). Outside those three directories, each tracked line that holds "workflow" and names the process is in *Scope* item 4 (executed: `git grep -n -i workflow -- . ':!seal/threads' ':!docs' ':!skills' ':!agents'`, each line read).
```

The `gaps.md` snippet states a search the fix pass runs and reads before it
writes the sentence. The fix pass also owes the `frame/plan.md:44` row a
mention of the docstring, since the row lists what *Scope* item 4 names.

### 3. *Removes* says no assertion reads "the workflow", that the suite passed, and that *Scope* item 4 updates the heading, and the records and the tree say otherwise

```seal
severity: should
location: `seal/threads/1794986401-the-process-has-no-name/frame/design.md:62`
evidence: executed `git grep -n -i 'the workflow' c637848af -- tests`, 106 lines, and the same search filtered to lines that are not comments and hold a call, an `assert` or a string; read `seal/threads/1794986401-the-process-has-no-name/frame/design.md:26-27`, `seal/threads/1794986401-the-process-has-no-name/frame/design.md:62`, `seal/threads/1794986401-the-process-has-no-name/trail/phases/phase-1.md:7`, `seal/threads/1794986401-the-process-has-no-name/gaps.md:7`, `tests/text/test_every_agent_reads_the_contract.py:128-140`
regression: round-1#3
```

Why it matters: the unit is the *Removes* paragraph at `frame/design.md:62`,
which commit `bc092878b` rewrote. Round 1 finding 3's snippet kept the
exception for the asserted heading inside its opening sentence and named
*Scope* item 3 for it. The fix pass wrote its own sentence instead, and
that is where the four defects below came from.

- "No assertion reads "the workflow"" is false at `c637848af`.
  `tests/text/test_every_agent_reads_the_contract.py:139` held the heading
  "## The first value: efficient development through the workflow", and
  `:140` asserts that heading is a line of the core. The paragraph's next
  sentence names that very line.
- "the suite's cases passed after the rename (`trail/phases/phase-1.md`)"
  is not what the phase says. `trail/phases/phase-1.md:7` reports six
  modules, 271 cases. `gaps.md:7` labels the full suite unverified, for the
  orchestrator to answer. A sentence that says the suite passed is the
  reading contract rule 2 warns against.
- "*Scope* item 4 updates both" is wrong for the heading. *Scope* item 3,
  at `frame/design.md:26`, cites the new heading "at each of the six places
  G3 lists", and G3 lists `tests/text/test_every_agent_reads_the_contract.py:139`.
  *Scope* item 4, at `:27`, does not name that file.
- "The rest are docstrings and comments" is false. Among the rest are
  assertion messages, such as `tests/behaviour/test_release_hygiene.py:1163`
  ("the workflow states no permissions block, so it inherits all"), and
  string arguments, such as the commit message at
  `tests/skills/test_seal.py:322`.

The paragraph is the one *Removes* entry and the plan's judgment that the
change removes nothing cites it (`frame/plan.md:43`), so the sealer reads
it as the build's account. The fix rewrites the `why:` line:

```markdown
  why: the work replaces a word at each place G2 lists and adds one definition paragraph per README and one clause to the core. `git grep -n -i 'the workflow' -- tests` printed 106 lines at `c637848af` (executed). One is a heading an assertion reads, `tests/text/test_every_agent_reads_the_contract.py:139`, which *Scope* item 3 updates with the core's heading. Three are a comment and two docstrings that call the process "the workflow", `tests/behaviour/test_chain_hooks_hardening.py:417`, `tests/lib/test_core.py:219` and `tests/skills/test_seal_stamp.py:1564`, which *Scope* item 4 renames. The rest name a GitHub Actions workflow, in docstrings, comments, assertion messages and string arguments. The phase's six modules passed after the rename (`trail/phases/phase-1.md`), and the full suite is the broad gate's, unverified in `gaps.md`.
```

The snippet reaches every statement of the paragraph. No other record
restates it: `frame/plan.md:43` cites *Removes* for its reason and quotes
none of its words.

### 4. Round 1's close block for finding 4 stands after `## Probes`, outside its finding, so the chain check reads finding 4 as open

```seal
severity: must
location: `seal/threads/1794986401-the-process-has-no-name/trail/rounds/round-1.md:339`, `seal/threads/1794986401-the-process-has-no-name/trail/rounds/round-1.md:189`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.38.3 --root . --worktree` from the repository's root, before this record was written; read `seal/threads/1794986401-the-process-has-no-name/trail/rounds/round-1.md:189-247`, `seal/threads/1794986401-the-process-has-no-name/trail/rounds/round-1.md:329-342`, `templates/records/sdd-round.md:16-34`
regression: round-1#4
```

Why it matters: the unit is the close block at `round-1.md:339-342`, which
commit `abd417cd6` added when it closed finding 4. The frame says nothing
of where a close block stands. `templates/records/sdd-round.md` places it
after the finding's paste-ready fix, inside the finding's section. The fix
pass appended it to the end of the file, below the `## Probes` table, and
that is where the defect came from. The chain check prints two refusals for
it: "a close block outside every finding" at `round-1.md:339`, and finding 4
at `:189` with "no close block, so the finding is open". So the chain holds
a finding open that the fix pass meant to close, and the invariant that
every `fixed` finding is read by the next round cannot be met while the
check cannot see the verdict.

The fix is a move, described here in words so that this record holds no
second close block. Take `round-1.md:339-342`, the fence opened by `seal`,
its `verdict:` and `answer:` lines and the closing fence, out of the end of
the file unchanged, with the blank line before them. Put them after
`round-1.md:246`, the last line of finding 4's paste-ready text, with one
blank line on each side, so they stand before `## Confirmations`. The file
then ends with the `## Probes` table.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `CONTRIBUTING.md:58` reads "This repository runs the AgenticSeal
process on itself" (read). `git grep -n -i workflow -- CONTRIBUTING.md`
prints eleven lines at the target, and each names a GitHub Actions workflow,
its file or `tests/workflows.py` (executed). So `changelog.md:3`'s claim for
`CONTRIBUTING.md` holds, and *Scope* item 4 names the line.

```seal
confirms: round-1#2
```
What holds: `lib/core.py:14-15`, `tests/lib/test_core.py:219-220` and
`tests/skills/test_seal_stamp.py:1564` say the repository runs the
AgenticSeal process (read). Each stood at the coordinate *Scope* item 4
gives at `c637848af` (executed: `git show c637848af:<path>`), and
`changelog.md:3` now names `lib/core.py`. The `gaps.md` sentence the fix
pass wrote is finding 2 of this round, by its `regression:` line.

```seal
confirms: round-1#3
```
What holds: at `c637848af` the *Removes* search prints 106 lines and the two
S2 searches print 48 and 16 (executed), the counts `frame/design.md:42` and
`:62` now give. The comment at
`tests/behaviour/test_chain_hooks_hardening.py:415-419` names the row "the
AgenticSeal process's own steps" (read), the label `README.md:389` carries
by round 1's reading. The rest of the *Removes* sentence is finding 3 of
this round, by its `regression:` line.

```seal
confirms: round-1#4
```
What holds: the six lines are within 76 display columns at the target:
`lib/optin.py:25` is 70, `:315` is 69 and `:326` is 76, `seal/README.md:18`
and `templates/setup/seal-README.md:18` are 73, and
`skills/settle/SKILL.md:449` is 73 (executed: a width count of each line the
fix diff adds). The two README files remain equal (executed: `diff`).
`trail/phases/phase-1.md:6` now says the six lines stayed past 76 and round
1's fix pass refilled them, which holds. The citation in
`skills/settle/SKILL.md:448-449` still resolves, by the cited-section module
passing. Where the close block of this finding stands is finding 4 of this
round.

What matched: the fix pass's run. The eight modules its close of finding 4
names pass, 476 cases, and `uvx ruff check` and `uvx ruff format --check`
pass on the five Python files the fix diff changes (executed).

What matched: `pr.md` quotes 2 to 7 stand word for word at their sources
(executed). The rest of each record holds at the target, apart from the
places findings 1 to 3 name. The `frame/plan.md:44` row names what the fix
pass did for round 1 findings 1 to 3 and the counts round 1 executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD. The label `unverified` at `gaps.md:7` is honest, and finding 3 is the one sentence that says otherwise | `seal/config.json` | the orchestrator, once the review rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the eight modules of the fix pass's close of round 1 finding 4 | exit 0, 476 passed, 5 warnings |
| the same eight modules with `tests/behaviour/test_the_contributor_has_a_procedure.py` | exit 0, 493 passed, 5 warnings |
| `uvx ruff check` and `uvx ruff format --check` over `lib/core.py`, `lib/optin.py`, `tests/lib/test_core.py`, `tests/skills/test_seal_stamp.py`, `tests/behaviour/test_chain_hooks_hardening.py` | exit 0 each |
| `git grep -n -i 'the workflow' c637848af -- tests`, and the two S2 searches at `c637848af` | 106 lines; 48 and 16 lines |
| `git grep -n -i workflow -- . ':!seal/threads' ':!docs' ':!skills' ':!agents'` at the target | 623 lines. The 184 lines outside `.github/` that hold no GitHub, `workflows`, identifier or YAML mark were read one by one. The rest were matched against prose patterns such as "the workflow" and "own workflow", and each match was read. One line names the process outside *Scope* item 4, `tests/behaviour/test_the_contributor_has_a_procedure.py:2`. The list is whole for the lines read and a pattern match for the rest |
| the comparison of each `pr.md` quote with its source, runs of whitespace collapsed | quote 1 fails, quotes 2 to 7 hold |
| `chain_check.py --baseline release/v0.38.3 --worktree`, before this record | refuses `round-1.md:339` as a close block outside every finding, and reads round 1 finding 4 as open |
