# Review round 3: 1794200907-agents-write-commands-the-parser-reads

```seal
target: 94a52303 against release/v0.37.0
```

This round reviews a new phase, not a fix pass. The range
`2d1113ff..94a52303` holds six commits that change the code or the frame.
`4c193822` is the framer's fold of the prevention home into the frame:
G18, *Scope* items 6 to 8, S6, two lines of *Data & interfaces*, the
`## Removes` reason, *Alternatives considered* rows 11 and 12, *Phases* row
2 and the last row of *Judgments of the run*. `8b55ee74`, `62e7a003`,
`ba3ba7a4` and `2177805b` are the phase 2 crafter's build, its record and
its rewrap. `94a52303` is the orchestrator's rewrite of G18's two paths and
two new quotes in `pr.md`. `6f6e9b2e` (round 2) and `9a23c853` (the broad
run's record) are records alone (executed: `git log` and `git show --stat`
on each). The review ran in a `--no-local` clone at `94a52303` under the
round's scratch directory, removed before the hand-back.

Every work item record the proofer's definition names was read whole at
`94a52303`: `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`,
`trail/gate.md` and rounds 1 and 2. No `pr.<lang>.md` stands, and none is
owed: `seal/config.md` gives English for both language rows (read). Issue
#1445 and its two comments were read through `gh issue view 1445 --json
title,body,comments`. The second comment is the orchestrator's record of the
prevention home that `skills/implement/orchestration.md` *A problem that
recurs within a run gets a prevention home at once.* asks for.

Carried from rounds 1 and 2 without re-deriving: the transcript counts of
`frame/design.md` G8 to G10, and the confirmations of rule 21's command
forms, step 1 of `skills/implement/orchestration.md`,
`skills/update/SKILL.md:117` and `.claude-plugin/plugin.json`. This range
does not touch any of those parts. Re-established this round: rule 21's
`check:` targets, by `bin/seal rules --check`, and every module that reads a
path the range changed, listed under `## Probes`.

The axes walked: the crafter's new rule against *Scope* item 7; rule 21's
removal clause and check line against *Scope* item 6 and *Data &
interfaces*; the two cases against *Scope* item 8 and S6, with their seen
red re-run; the docstring's count of the class; the mutation claims; the
class the prevention home answers, by a search of the shipped text for
every scratch location; the frame fold's grounds, by a read of the session's
transcripts; the changelog, `gaps.md` and `pr.md` against the frame and the
tree; and the process row the `agents/*.md` change owes. Authorization,
query scope and state transitions have no surface in a diff of prose and two
text cases. Concurrency is the subject of this phase: two agents alive at
once in one scratchpad. It is walked below as the class search.

## Findings

### 1. The frame says the shared scratchpad was removed three times, where G18 and the transcripts hold two removals

```seal
severity: should
location: `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md:90`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/plan.md:62`
evidence: executed a read-only Python scan of every Bash call in the session's transcript and its `subagents/` transcripts for an `rm` whose path ends at the scratchpad or at a bare variable; read `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md:25`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/design.md:90`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/frame/plan.md:62`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/changelog.md:6`, `seal/threads/1794200907-agents-write-commands-the-parser-reads/changelog.md:15`
```

Why it matters: the `## Removes` reason at `frame/design.md:90` says the
crafter's directory "answers the three removals of the shared scratchpad
G18 records". G18 at `frame/design.md:25` records two: the crafter ran the
removal "at 2026-11-09T05:34:41Z and again at 05:46:32Z". The last row of
*Judgments of the run* at `frame/plan.md:62` says "The session's whole
scratchpad was removed three times in this run". Its grounds then name the
same two times and no third. The changelog says "twice", at `:6` and in the
process row at `:15`, and `pr.md:7` quotes that word.

The scan of the session's transcripts found two Bash calls that removed the
whole scratchpad. Both are in the phase 1 crafter's transcript, at
05:34:41Z and 05:46:32Z (executed). No other call in the session, the
orchestrator's included, names the bare scratchpad path in a removal. The
only other removal of a whole directory is the #1454 framer's at 05:29:09Z.
That removal took its own work item's directory, not the scratchpad. The
#1059 crafter also wrote its files straight into the scratchpad root. It
removed them file by file at 05:44:12Z, which bears out G18's account of
the class.

The frame thus states one count in G18 and another in `## Removes` and in
the judgment row. The settle reads *Judgments of the run* for what a
judgment cost and caught (`skills/core/SKILL.md` *A judgment stands on a
source document, and is written down with both*). The sealer reads the
frame against the changelog, which says twice. A third removal may exist
that no Bash call shows. In that case, the row and G18 owe its coordinate,
and the changelog's "twice" is wrong instead. The issue's second comment
also says "three times". It stands outside the tree, and the orchestrator
corrects it there if the count changes.

In `frame/design.md:90`, the reason's clause becomes:

```markdown
answers the two removals of the shared scratchpad G18 records;
```

and in `frame/plan.md:62`, the grounds cell opens:

```markdown
The session's whole scratchpad was removed twice in this run, taking other agents' files with it:
```

The frame is the framer's to fold, and the row at `plan.md:62` is the
orchestrator's. Where a third removal is real, these two snippets do not
apply. G18 and the row then name its time and transcript, and
`changelog.md:6`, `:15` and `pr.md:7` change from "twice" to the count.

```seal
verdict: fixed 647a5495
answer: The orchestrator counted the times it found its files gone, three, and no Bash call names a third whole-scratchpad removal; the round's scan of every transcript is the stronger reading, so the count is two. frame/design.md's Removes reason now says "the two removals" and the last Judgments row of frame/plan.md says "twice", the round's two snippets; the changelog and pr.md already said twice. The fix touches the work item's records alone. The orchestrator corrects the issue's second comment.
```

## Confirmations

What matched: `agents/crafter.md:102-111` adds the rule *Scope* item 7
describes. It follows the shape of `agents/proofer.md` *The clone is named
for the work item and the round*. A phase's writes sit under
`<scratchpad>/<work-item-id>/phase-<n>/`, and a fix pass's under
`<scratchpad>/<work-item-id>/fix-<n>/`. The rule says what `<n>` is in each,
gives the shared scratchpad as the reason, and has the crafter remove that
directory and "never the scratchpad or anything else in it". It ends with
the check line *Scope* item 7 names (read). The definition of `<n>` for a
phase is the phase record's departure. *Scope* item 7 defines `<n>` only for
a fix pass. The departure narrows nothing the frame states, and the record
gives its grounds (read: `trail/phases/phase-2.md:55-63`).

What matched: rule 21's removal example at
`skills/agent-contract/SKILL.md:226-232` names a directory "under
`<scratchpad>/<work-item-id>/`" and says "the removal never names the
scratchpad itself, which every agent of the session shares". Its check line
names both modules on one line, as *Data & interfaces* gives it (read).
Scope item 6 words the clause as "never the scratchpad itself". The build
writes "the removal never names". The phase record states that departure
and its grounds at `trail/phases/phase-2.md:41-47`. It gives the clause one
subject and changes no meaning (read). `bin/seal rules --check` printed "all
221 check lines in 68 rule files hold" and exited 0 (executed), so both
targets exist.

What matched: the two cases at
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:99-137`
assert what *Scope* item 8 lists. One asserts the crafter's two directories
and the shared scratchpad. The other asserts rule 21's
`<scratchpad>/<work-item-id>/` and "never names the scratchpad itself". The
claim "seen red, 2 failed and 4 passed" was re-run this round. With
`agents/crafter.md` and the contract restored to `4c193822` and the module
at HEAD, the module exited 1 with 2 failed and 4 passed. Each case failed on
its first assertion, the one the phase record quotes (executed; the two
files were restored to `94a52303` and `git status --short` was clean).

What matched: the phase record's mutation claim that the "use one
scratchpad" mutant reads red rests on "share" standing once in the crafter's
*Rules* section. It does, at `agents/crafter.md:107`, and the section runs
to the end of the file (executed: `grep -n -i share` over the section).

What matched: the new cases were read against their group. They sit beside
the proofer's, the framer's, the gate log's and the capture example's cases
in the same module. Each pins a different file's sentence, so neither covers
what another case covers. No test file of the module declares `TARGET`, and
`bin/seal layout --pairs` names no pair for it (executed).

What matched: the module docstring now counts five instances, the fifth
the crafter's directories, and names rule 21's clause beside them as the
same repair at the moment of cleanup. That matches the cases the module
holds (read).

What matched: the census failure the phase record names at
`trail/phases/phase-2.md:86-96` is gone at HEAD.
`tests/behaviour/test_every_tracked_file_meets_every_census.py` passed at
`94a52303` (executed). G18 now names the transcript by its file name in "the
session's `subagents/` directory" and the scratchpad as `<scratchpad>`. The
transcript `agent-a5cc507e4ff134b78.jsonl` exists in that directory and
holds both removals G18 times (executed).

What matched: all nine quotes in `pr.md` stand word for word in their
sources, with runs of whitespace collapsed. Items 1 to 8 are in
`changelog.md`, and item 9 is in `gaps.md` (executed: a read-only Python
comparison). Items 6 and 7 come from the fourth item of *Fixed*, as their
coordinates say (read).

What matched: the diff changes `agents/crafter.md`, so
`docs/layout/the-record-layout.md:52` owes a process row.
`changelog.md:15` holds it (read). The new `gaps.md` row names who answers
it, a measurement on the first runs under 0.37.0, and no row left the file
(read: `git diff 2d1113ff..94a52303 -- gaps.md` adds one line and removes
none).

What matched, from a search of the shipped text for every scratch location
(executed: `git grep -n -i scratchpad` over `agents`, `skills`, `docs`,
`templates` and the root documents). Every agent definition that names a
place outside the worktree names one under `<scratchpad>/<work-item-id>/`.
The crafter's was the one missing. The search found two statements outside
the agent definitions that this phase leaves as they stand. Neither is a
finding.

- `skills/code-review/orchestration.md:392` and `:455` put the
  orchestrator's `gate.log` and `pr-body.md` straight into
  `<scratchpad>/<work-item-id>/`. That directory is the parent of every
  agent's directory for the item. Rule 21 now names only the scratchpad as
  the directory a removal never names. The work item's own directory is
  still not "a directory you made under `<scratchpad>/<work-item-id>/`", so
  the rule does not license its removal. Its agents run one after another,
  and the orchestrator writes there only at the broad run, after the last
  round. A removal of that directory still took no file of another party in
  this run (executed: the #1454 framer's removal at 05:29:09Z came before
  any other #1454 agent started).
- `skills/verify/SKILL.md:277`, the *Capture once, filter locally* example,
  writes `<scratchpad>/<work-item-id>/run.txt`. That is a sibling of a
  crafter's `phase-<n>/` and not inside it. The example sits in *The cost of
  a run that repeats*. The crafter's definition sends it to that file's
  *Scope* table at steps 5 and 7, and the crafter's own rule is the more
  specific one, so this round reads no conflict an agent acts on.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether crafters keep their scratch under `phase-<n>/` and `fix-<n>/`, and whether agents stop writing the two shapes, once they run under a plugin that holds this phase | `gaps.md` *Not verified*, `frame/questions.md` Q1, `frame/design.md` S6 | a measurement on the transcripts of the first runs under 0.37.0, as Q1 states |
| The transcript counts of G8, G9 and G10, carried from round 1 as the framer's reading | `frame/design.md:16-18` | the framer's `test_tmp_reading.py` reading, which a measurement can repeat |
| The full suite, the repository-wide lint and the typecheck. `trail/gate.md` records the broad run at `6f6e9b2e`, and phase 2 changed `agents/crafter.md`, the contract and a test module after it | `trail/gate.md`, the `Broad gate` row of `seal/config.md` | the orchestrator's broad run at HEAD, due once finding 1 is settled, before the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_every_tracked_file_meets_every_census.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_chain_hooks_hardening.py` with `-q`, in the clone at `94a52303` | exit 0, 392 passed |
| `bin/seal rules --check` in the clone | exit 0, "all 221 check lines in 68 rule files hold" |
| `git checkout 4c193822 -- agents/crafter.md skills/agent-contract/SKILL.md` in the clone, then `bin/test tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py -q -p no:xdist`, then the two files restored to `94a52303` | exit 1, 2 failed and 4 passed, each new case on its first assertion; `git status --short` clean after the restore |
| a read-only Python scan of the Bash calls in the session's transcript and its `subagents/` transcripts, for an `rm` whose path ends at the scratchpad or at a bare variable | two removals of the whole scratchpad, both by the phase 1 crafter, at 05:34:41Z and 05:46:32Z; one removal of a work item's directory by the #1454 framer at 05:29:09Z; no third removal of the scratchpad |
