# Review round 1: 1794200907-agents-write-commands-the-parser-reads

```seal
target: 9e192e27 against release/v0.37.0
```

The range is `dfd0c995..9e192e27`, nine commits. This is the first round,
so no earlier round carries a coordinate or a close to answer. The review
ran in a `--no-local` clone of the branch under the round's scratch
directory, removed before the hand-back. Every work item record named by
the proofer's definition was read whole at `9e192e27`: `routing.md`, the
three frame files, `trail/phases/phase-1.md`, `gaps.md`, `changelog.md` and
`pr.md`. No `pr.<lang>.md` stands, and none is owed, because `seal/config.md`
gives English for both language rows. Issue #1445 and its one comment were
read through `gh issue view 1445 --json title,body,comments`.

The axes walked: the rule's text against *Scope* item 1 and *Data &
interfaces*; the pin against S4; the two unpinned edits against S3 and S5;
the version move; the changelog and `pr.md` against the frame's own
readings; the overlap with the release's other items; the class the change
answers, by a search of the shipped text; and whether the rule's stated
reasons are true of the shells it names. Authorization, query scope,
concurrency and state transitions have no surface in a diff of prose and
one test table.

## Findings

### 1. The changelog and `pr.md` give the prompt counts more widely than the frame's reading found them

```seal
severity: should
location: `seal/threads/1794200907-agents-write-commands-the-parser-reads/changelog.md:3`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/pr.md:3`
evidence: read `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md:17`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/changelog.md:3`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/pr.md:3`
```

Why it matters: the changelog becomes the release note, and `pr.md` becomes
the pull request body. The two disagree with the reading they cite.
The changelog says "people answered 21 such prompts", where "such" means a
command line the parser cannot read. `frame/design.md:17` (G9) counts the
same 21 differently. Ten were an `rm` on a variable path, nine were a zsh
expansion flag, and two were "neither (a chained line the parser called
too complex, and a read outside the working directory)". A read outside the
working directory is a path permission prompt, not a line the parser could
not read. So "21 such" counts at least one prompt of another kind.

The next sentence says "seven of them agents removing what they had made
under the scratchpad file by file in a loop". G9 says the seven were
"mostly file by file in a `for` loop", so not all seven were loops.
`pr.md:3` quotes that sentence word for word, so it carries the same
overstatement, and a fix to the changelog leaves the quote unmatched until
`pr.md` changes with it.

The fix rewrites both sentences in `changelog.md:3` and the same quote in
`pr.md:3`. Nothing else in the tree states these counts. The frame states
them correctly, and the phase record does not repeat them.

```markdown
From 2026-11-03 to 2026-11-09, people answered 21 prompts on Bash calls in the transcripts read, and 19 of them were in two shapes. Ten were an `rm` whose path held a variable, seven of them agents removing what they had made under the scratchpad, mostly file by file in a loop. Nine were a zsh expansion flag such as `${(f)"$(cat list)"}`, which agents used to pass a list of test files to one command.
```

and in `pr.md:3`:

```markdown
- "Ten were an `rm` whose path held a variable, seven of them agents removing what they had made under the scratchpad, mostly file by file in a loop. Nine were a zsh expansion flag such as `${(f)"$(cat list)"}`, which agents used to pass a list of test files to one command." (`changelog.md` *Fixed*, the first item)
```

```seal
verdict: fixed a1a916d7
answer: The first item of changelog.md *Fixed* now says people answered 21 prompts on Bash calls and that 19 of them were in two shapes, and that the seven scratchpad removals were mostly file by file in a loop, as frame/design.md G9 found; the sentences are the paste-ready fix's. pr.md is the orchestrator's and was left as it stands, so its third quote still carries the old sentence until the orchestrator rewrites it.
```

### 2. The pin's failure message says the parser reads the zsh form that rule 21 says it cannot read

```seal
severity: should
location: `tests/text/test_the_agent_contract_holds_the_universal_rules.py:66-67`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md:59`
evidence: read `tests/text/test_the_agent_contract_holds_the_universal_rules.py:22-29`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py:65-69`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py:206-209`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/trail/phases/phase-1.md:66-69`
```

Why it matters: entry 21 of `FACTS` describes all three spellings as "the
command forms an agent copies into a shell, which Claude Code's parser
reads". The third spelling, `${(f)"$(cat list)"}`, is the form rule 21
says the parser cannot read. `test_each_section_holds_its_rule` prints
the description beside the missing spelling. So a person whose edit drops
the zsh form reads that rule 21 "no longer holds the command forms ...
which Claude Code's parser reads: ['`${(f)"$(cat list)"}`']". That message
states the opposite of the rule. Phase 1's mutation run printed this message
(`trail/phases/phase-1.md:66-69`). The same module's docstring
(`:25-26`) uses "reads" for the forms the parser accepts: "two that Claude
Code's parser reads and one it cannot". So "the parser reads" means one
thing in the docstring and another in the entry eight lines below. The
frame's *Data & interfaces* (`frame/design.md:59`) prescribed the string,
so the frame line changes with the code. Contract rule 14 covers a message
someone reads and acts on.

```python
    21: (
        "the command forms an agent copies into a shell, two that Claude "
        "Code's parser reads and one it holds for a person",
        ("`xargs <runner> < list`", '`"${VAR:?}"`', '`${(f)"$(cat list)"}`'),
    ),
```

and in `frame/design.md:59`, the quoted value becomes ("the command forms
an agent copies into a shell, two that Claude Code's parser reads and one
it holds for a person").

```seal
verdict: fixed a1a916d7
answer: FACTS entry 21 now reads "the command forms an agent copies into a shell, two that Claude Code's parser reads and one it holds for a person", the value the folded frame/design.md *Data & interfaces* gives, so the failure message no longer says the parser reads the zsh form. The frame half was folded by the framer in d0bb10a7. The module passed with the new description in the fix pass's run of tests/text and tests/behaviour.
```

### 3. Rule 21 says `"${VAR:?}"` stops the line where the variable is unset, and leaves out the empty case the parser asks about

```seal
severity: should
location: `skills/agent-contract/SKILL.md:225-226`
evidence: executed `sh -c 'V=; echo "${V:?}"'` (exit 127, "parameter null or not set") and `zsh -c 'V=; echo "${V:?}"'` (exit 1); read `skills/agent-contract/SKILL.md:224-226`
```

Why it matters: the rule gives a reason for the guard: `"${VAR:?}"`
"stops the line where the variable is unset". That reason is also true
of `"${VAR?}"`, which lets an empty variable through. What the colon adds
is the empty case, and that is the case Claude Code's prompt names:
"Dangerous rm operation on possibly-empty variable path" (issue #1445's
comment). Both shells stop on an empty `V` under `${V:?}` (executed above).
Rule 21 asks the agent to write to the aim where no example fits. An agent
that takes this reason as the aim can write `"${VAR?}"` and meet the same
prompt. The pinned spelling `"${VAR:?}"` stays as it is. Only the reason
beside it changes. No other file of the diff states the reason. The
changelog and the frame name the form without it.

```markdown
literal path, or writes each variable in its path as `"${VAR:?}"`, which
stops the line where the variable is unset or empty. A directory you made is
```

```seal
verdict: fixed a1a916d7
answer: Rule 21 now says "${VAR:?}" stops the line where the variable is unset or empty, so the reason names the empty case the colon adds and the prompt asks about. The pinned spelling is unchanged, and the paragraph was rewrapped to the file's width.
```

### 4. The plan's *Overlap with the release* names two of the release's three other items and leaves out #1459, which changes the same orchestration file

```seal
severity: should
location: `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/plan.md:36-43`
evidence: executed `gh issue view 1459 --json title,body`, `git diff --stat dfd0c995..HEAD` in the worktree of `feat/1459-the-orchestrator-chooses-each-items-route`; read `agents/framer.md:82-92`, `skills/implement/orchestration.md:447-452`
```

Why it matters: the orchestrator merges the release's items in the order
their plans' *Overlap with the release* sections state
(`skills/implement/orchestration.md:450-451`). The spawn names #1059, #1454
and #1459 as this release's other items. The section has rows for #1059
and #1454 only, and its opening sentence says "Both other items". #1459's
issue changes the routing question in `skills/implement/orchestration.md`
(*Question 1* and *Orchestrator: how the work is routed*). This diff adds a
sentence to step 1 of *Orchestrator: the order inside a ticket* in the same
file, and step 1 cites *Orchestrator: how the work is routed*.
`agents/framer.md:84-85` says two items meet "where both change the same
file". #1459's branch holds only its `routing.md` so far (executed), so the
row reads its issue, as this section's other rows read theirs. The merge
order does not change, because this item carries the version move and
merges first. A missing row still leaves the orchestrator to find the
overlap itself.

```markdown
The frames of #1059 and #1454 held only their skeletons when this frame was written, and #1459 had no frame when its row was added, so each row reads the item's issue and the spawn's description of it.

| #1459, the orchestrator chooses each item's route | `skills/implement/orchestration.md`: #1459 changes the routing question and *Orchestrator: how the work is routed*, and this work adds one sentence to step 1 of *Orchestrator: the order inside a ticket*, which cites that section by name | #1445 | This item carries the version move and merges before every other item of the release. The two edits are in different sections of one file, so #1459 takes the base in with a text merge, inside a round it runs anyway. If #1459 renames that section, it carries the citation in step 1 with it. |
```

```seal
verdict: fixed d0bb10a7
answer: The framer's fold added a row for #1459 to frame/plan.md *Overlap with the release* and rewrote the section's opening sentence to name all three items; the fix pass read the fold and changed nothing for this finding.
```

### 5. The plan still says the parser refuses the forms, after the phase and the fold settled that it holds them for a person

```seal
severity: should
location: `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/plan.md:14`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/plan.md:25`
evidence: executed `git grep -n -i refus` over the work item, the contract and the test module; read `seal/threads/1794200907-agents-write-commands-the-parser-reads/trail/phases/phase-1.md:19-26`, `git show 16c0b84f`
```

Why it matters: phase 1 decided that "rule 21 says a line the parser cannot
read is held for a person to approve, not that it is refused". It gave the
reason that "'Refused' would read as a denial no person sees"
(`trail/phases/phase-1.md:19-26`). The orchestrator's fold `16c0b84f`
rewrote the `## Rule changes` passage of `frame/design.md` to match. Two
statements of the old wording remain in the frame. `plan.md:14` says "Claude
Code changes which forms its parser refuses". `plan.md:25` (alternative 6)
says a check "refuses what the parser reads or passes what it refuses".
Contract rule 19 asks a change to correct every sentence that stated the
old fact. Otherwise the frame keeps both wordings, and the sealer reads
them as two claims about what the parser does. The search found no other
instance in the work item, the contract or the test module. Where
`frame/design.md` G7, G8 and G10 say "refusals", they mean a distinct
category: a `reject` with no person (`source` `config`). Those stand
correct.

```markdown
The chosen approach's failure scenario, six months out: Claude Code changes which forms its parser holds for a person. It may start to ask about `$(cat list)`, or stop accepting `"${VAR:?}"`.
```

and in row 6 of *Alternatives considered*:

```markdown
| 6. A check: a hook or script that reads an agent's command before it runs | It re-encodes Claude Code's judgment, refuses what the parser reads or passes what the parser holds for a person, and brings back the `PreToolUse` gates #1416 and #1430 removed | Rejected (`skills/core/SKILL.md` *The rule a mechanism is kept against*, and the issue's *Done when*) |
```

```seal
verdict: fixed d0bb10a7
answer: The framer's fold rewrote frame/plan.md's failure scenario to "holds for a person" and row 6 of *Alternatives considered* to "passes what the parser holds for a person"; the "refuses" left in row 6 is the check's act, not the parser's. The fix pass read the fold and changed nothing for this finding.
```

## Confirmations

What matched: rule 21 stands at `skills/agent-contract/SKILL.md:216-231`
under the heading `frame/design.md` *Data & interfaces* gives, after rule
19. It ends with the check line that section names. Its body holds every
example *Scope* item 1 lists: `xargs <runner> < list`, `<runner> $(cat
list)`, the two zsh forms, the unquoted variable, the literal or guarded
`rm` path, and one `rm -rf` of a directory. It also says these are examples
and not a list (read). The numbering holds: 20 is listed as retired, and
21 is the next number (executed: the module run below).

What matched: `FACTS` gains entry 21 with the three spellings *Data &
interfaces* names (`tests/text/test_the_agent_contract_holds_the_universal_rules.py:65-69`).
The docstring's count changed from two pinned facts to three (`:22-29`).
The existing parametrized cases cover the entry, so no new case function
was owed, and no duplicate check names a pair for this module (read). The
claim "seen red, 5 failed and 14 passed" is consistent with the module's
structure. With entry 21 present and rule 21 absent,
`test_each_section_holds_its_rule[21]` fails on an empty body,
`test_no_pin_is_its_own_heading` raises `KeyError: 21` at `headings[number]`,
and the three `test_deleting_a_pinned_phrase_is_caught[21-...]` cases raise
`KeyError: 21` at `spans(text)[number]`. That makes five failures (read, not
re-run). `test_deleting_a_pinned_phrase_is_caught` deletes each spelling
inside the suite on every run. So the mutation claim is held by the suite
itself, and this round's run of the module was green.

What matched: `skills/update/SKILL.md:117` reads `rm -f "${f:?}"`. `f` is
set by `f=$(mktemp)` in the same block, so the guard changes no outcome
where `mktemp` succeeded (read). *Scope* item 3 and S3 hold.

What matched: step 1 of `skills/implement/orchestration.md:32-35` adds the
sentence *Scope* item 5 describes. It cites `contract rule 21` in that
spelling and names the file to open. It states no form of its own, so the
forms keep one source. It agrees with `skills/implement/SKILL.md:21-25`
and `skills/code-review/orchestration.md:95-96`, which say the contract
reaches the orchestrator only when the orchestrator opens it (read). S5
holds as read.

What matched: `.claude-plugin/plugin.json:4` reads `0.37.0`, and no file
outside `seal/threads/` names `0.36.0` (executed: `git grep -n -F` for each
version in the clone). The move rides in `b58bd082` with the changelog
fragment, as `frame/plan.md` *Operational impact* says.

What matched: the diff changes `skills/implement/orchestration.md`, so
`docs/layout/the-record-layout.md:52` owes a `### Process changes` table.
`changelog.md:9-13` holds one row for step 1. Phase 1 says the contract is
not among the files that rule lists, and the rule confirms it (read).

What matched: every quote in `pr.md` stands word for word in its source.
Items 1 to 6 are in `changelog.md`, and item 7 is in the first row of
`gaps.md` *Not verified*, up to its semicolon. `pr.md` carries
`Closes #1445.` (read). Finding 1 changes item 3's source and quote together.

What matched: no check, hook or script was added. The diff touches no file
under `hooks/`, `bin/` or any `scripts/` directory, so the issue's
*Done when* second bullet holds (read: `git diff --stat`).
`bin/seal rules --check` printed "all 220 check lines in 68 rule files
hold" and exited 0 (executed). So rule 21's `check:` target exists.

What matched: this round searched the shipped text by spelling. It covered
`agents`, `skills`, `docs`, `templates`, `evals`, `hooks`, `bin` and the
root documents, excluding `seal/threads`. The searches looked for an `rm`
on an unguarded variable, a zsh expansion flag, a `for` loop that removes,
and a runner fed an unquoted variable. The only hits were `git rm -r
--cached "$(git rev-parse --show-toplevel)/seal"`, which is a command
substitution and not a variable path, and rule 21's own examples
(executed). This agrees with G14's one instance. Like G14, it is a sample
of an open class, since a search by spelling cannot list every form.

What matched: the frame states that `$(cat list)` and `xargs ... < list`
split a list the same way in bash and zsh, and an unquoted `$F` splits in
bash only (G11). That agrees with how the two shells expand
(read). Rule 21's clause "which bash splits and zsh does not" is true.

The build's account was weighed as a claim. The hand-back says
`bin/test tests/text tests/behaviour -q` exited 0 "at dcf5b135".
`trail/phases/phase-1.md:90-93` records that run at `77e93ac7` and a module
re-run after `df508485`. `dcf5b135` changed only the work item's records
(executed: `git show --stat dcf5b135`), so the difference changes no
outcome. This round did not re-run that set. The run below covers the
modules that read a path this diff changed.

The `## Rule changes` passage in `frame/design.md:65-78` adds a section to
`docs/running/the-agent-set.md`. Its `check:` names the module that pins
rule 21's command forms. Those forms are a fact an agent copies into a
shell, not a rule's wording, so the pin is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether agents and the orchestrator stop writing the two shapes once they run under a plugin that holds rule 21 | `gaps.md` *Not verified*, `frame/questions.md` Q1 | a measurement on the transcripts of the first runs under 0.37.0, as Q1 states |
| The transcript counts of G8, G9 and G10, which this round read as the framer's reading and did not re-derive | `frame/design.md:16-18` | the framer's `test_tmp_reading.py` reading, which a measurement can repeat |
| The full suite, the repository-wide lint and the typecheck, which the crafter handed over `unverified`, as rule 2 asks | the `Broad gate` row of `seal/config.md` | the orchestrator's broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_release_hygiene.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_the_old_block_leaves_through_update.py`, `tests/behaviour/test_update_reads_the_config_directory_in_use.py`, `tests/text/test_edits_go_through_the_edit_tool.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py` with `-q`, in the clone at `9e192e27` | exit 0, 476 passed |
| `bin/seal rules --check` in the clone | exit 0, "all 220 check lines in 68 rule files hold" |
| `sh -c 'V=; echo "${V:?}"'` and `zsh -c 'V=; echo "${V:?}"'` | exit 127 and exit 1: both shells stop on an empty variable under `:?` |
