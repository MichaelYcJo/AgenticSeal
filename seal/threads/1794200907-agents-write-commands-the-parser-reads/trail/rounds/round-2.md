# Review round 2: 1794200907-agents-write-commands-the-parser-reads

```seal
target: 2d1113ff, fixes e7b38539..2d1113ff
```

This is a verifying round. The range `e7b38539..2d1113ff` holds four
commits. `d0bb10a7` is the framer's fold of round 1 findings 2, 4 and 5
into `frame/design.md` and `frame/plan.md`, with two rows of *Judgments of
the run*. `a1a916d7` is the implementer's fix of findings 1, 2 and 3.
`25a96e8a` holds round 1's close blocks, and `2d1113ff` is the
orchestrator's rewrite of `pr.md` (executed: `git log` and `git show
--stat` on each). The review ran in a `--no-local` clone at `2d1113ff`
under the scratch directory the spawn named, removed before the hand-back.

Every work item record the proofer's definition names was read whole at
`2d1113ff`: `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No
`pr.<lang>.md` stands, and none is owed: `seal/config.md` gives English for
both language rows (read). `gaps.md` and `routing.md` are unchanged in the
range, and nothing in the range contradicts them.

Carried from round 1 without re-deriving: the transcript counts of
`frame/design.md` G8 to G10, which are the framer's reading; and round 1's
confirmations of the parts of rule 21, step 1, `skills/update/SKILL.md` and
`.claude-plugin/plugin.json` that this range does not touch. Re-established
this round: the existence of rule 21's `check:` target, by `bin/seal rules
--check`, and the shell behaviour finding 3 rests on, by re-running its
`evidence: executed` line.

The implementer's account was weighed as a claim. It claims `bin/test
tests/text tests/behaviour -q` exited 0 at `a1a916d7` with 1811 passed. This
round did not re-run that set. It ran the modules that read a path the range
changed, listed under `## Probes`, and they passed at `2d1113ff`. The account
also claims ruff passed on the test module. That is lint, which this round
leaves to the orchestrator's broad run.

## Findings

None. Each close of round 1 holds, as the confirmations below state, and the
range introduced no defect this round found.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `changelog.md:3` now reads "people answered 21 prompts on Bash
calls in the transcripts read, and 19 of them were in two shapes", and the
seven scratchpad removals were "mostly file by file in a loop". Those are
the counts and the qualifier `frame/design.md:17` (G9) gives: ten `rm`, nine
zsh flags and two of neither kind make 21, and the 19 are the first two
groups. The close said `pr.md:3` still carried the old sentence. `2d1113ff`
replaced that quote with the corrected sentences. All seven quotes in `pr.md`
were found word for word in their sources, with runs of whitespace
collapsed. Items 1 to 6 are in `changelog.md`, and item 7 is in `gaps.md`
(executed: a read-only Python comparison over the two files and `pr.md`).

```seal
confirms: round-1#2
```
What holds: `FACTS` entry 21 at
`tests/text/test_the_agent_contract_holds_the_universal_rules.py:66-67` now
reads "the command forms an agent copies into a shell, two that Claude
Code's parser reads and one it holds for a person". The failure message at
`:209` prints that description, so a dropped zsh spelling no longer reads as
a form the parser reads. The folded `frame/design.md:59` quotes the same
string character for character (read). It agrees with the module's
docstring at `:25-26`, "two that Claude Code's parser reads and one it
cannot", and with rule 21, which says a line the parser cannot read is held
for a person. The module passed at `2d1113ff` (executed, `## Probes`). A
search for the old description, "which Claude Code's parser reads", finds it
only in `trail/phases/phase-1.md:69` and in round 1's record (executed:
`git grep`). The phase record quotes what the mutation run printed at the
commit it names, so it states that commit truly.

```seal
confirms: round-1#3
```
What holds: `skills/agent-contract/SKILL.md:225-226` now says `"${VAR:?}"`
"stops the line where the variable is unset or empty". That is the reason
round 1's fix gave. Under `:?`, both shells still stop on an empty variable
(executed: `sh -c 'V=; echo "${V:?}"'` exit 127, `zsh -c 'V=; echo
"${V:?}"'` exit 1). The rewrap kept the pinned spelling whole.
`tests/behaviour/test_docs_line_wrap.py` and the pin's module passed at
`2d1113ff` (executed). No other file of the work item or the tree states
the guard's reason (executed: `git grep -n unset` over the contract, and
round 1's search for the reason).

```seal
confirms: round-1#4
```
What holds: `frame/plan.md:38` now names all three of the release's other
items, and `:44` adds the row for #1459. The row's claims were read against
#1459's frame as committed at `f80823a6` on
`feat/1459-the-orchestrator-chooses-each-items-route`. That frame rewrites
*Question 1* with the four answers `agentic`, `complete`, `manual` and
`direct`, and adds `### Under agentic` under *Orchestrator: how the work is
routed* (its `frame/design.md` *Scope* items 1 and 2). Its plan's *Overlap
with the release* orders #1445 first. It names no rename of the heading
(read: `git show f80823a6`). Step 1 of `skills/implement/orchestration.md:24-35`
cites *Orchestrator: how the work is routed* by name. The sentence this
work adds there names no routing answer (read). So the row's grounds hold.
The row's provenance sentence at `frame/plan.md:38` says #1459 "has an
uncommitted frame in its worktree". That was true when `d0bb10a7` was
committed at 14:44:47. #1459's frame was committed at 14:45:54 (executed:
`git log --format=%cI`). The sentence names where the row was read from, no
party acts on it, and the committed frame bears the facts the row states, so
this round opens no finding for it.

```seal
confirms: round-1#5
```
What holds: `frame/plan.md:14` now says "Claude Code changes which forms
its parser holds for a person". Row 6 at `:25` says a check "refuses what
the parser reads or passes what the parser holds for a person". A search
for `refus` over the work item, the contract and the test module finds no
other sentence that says the parser refuses a form (executed: `git grep -n
-i refus`). The remaining hits are of other kinds. In `frame/design.md` G7
and G10, a refusal is a `reject` with no person, a category apart. At
`frame/design.md:72` and `plan.md:25`, refusing is the act of a
hypothetical check. `trail/phases/phase-1.md:20-22` records the decision
that replaced the word.

What matched: the two new rows of `frame/plan.md` *Judgments of the run*
(`:55-56`) say what the range did. The folds landed in `d0bb10a7`, and the
fix pass in `a1a916d7`, which touches only `changelog.md`, the contract and
the test module. The `pr.md` rewrite landed in `2d1113ff` (executed: `git
show --stat` on each). The two documents the rows judge against exist at
the cited coordinates: the bold sentence at
`skills/implement/orchestration.md:53-54` and the heading at
`skills/code-review/orchestration.md:16` (read).

What matched: each `fixed` commit touches a path its finding's `location:`
names. `a1a916d7` touches `changelog.md` for finding 1, the test module for
finding 2 and the contract for finding 3. `d0bb10a7` touches `frame/plan.md`
for findings 4 and 5 (executed: `git show --stat`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether agents and the orchestrator stop writing the two shapes once they run under a plugin that holds rule 21 | `gaps.md` *Not verified*, `frame/questions.md` Q1 | a measurement on the transcripts of the first runs under 0.37.0, as Q1 states |
| The transcript counts of G8, G9 and G10, carried from round 1 as the framer's reading | `frame/design.md:16-18` | the framer's `test_tmp_reading.py` reading, which a measurement can repeat |
| The full suite, the repository-wide lint and the typecheck, which the fix pass handed over `unverified`, as rule 2 asks | the `Broad gate` row of `seal/config.md` | the orchestrator's broad run, now due: this round leaves nothing open, and the sealer's spawn follows that run |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py` with `-q`, in the clone at `2d1113ff` | exit 0, 354 passed |
| `bin/seal rules --check` in the clone | exit 0, "all 220 check lines in 68 rule files hold" |
| `sh -c 'V=; echo "${V:?}"'` and `zsh -c 'V=; echo "${V:?}"'` | exit 127 and exit 1: both shells stop on an empty variable under `:?` |
