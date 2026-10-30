# Review round 4: 1793343707-each-document-serves-one-reader

target: f279997c against 01c0873c

## Findings

### 1. The measure's second count has two readings, and on this work item they give 5 and 3

severity: should
location: `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:267`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:57`, `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:20`
evidence: executed `grep -h '^regression: \|^reopens: ' seal/threads/1793343707-each-document-serves-one-reader/trail/rounds/round-*.md | wc -l`, `grep -h '^regression: \|^reopens: ' seal/threads/1793343707-each-document-serves-one-reader/trail/rounds/round-*.md | sort -u | wc -l`, `git grep -n 'line names' -- docs skills agents`
verdict: fixed 8123af5b

The `add` to `docs/release-checklist.md` *2b. Settle what earlier releases
left behind* is new in the reframe, and the settle writes it into the
checklist. Its bold rule sentence names the second count as "the findings
a `regression:` or `reopens:` line names". Its next sentence says the
count is read from "the `regression:` and `reopens:` lines". These are two
different counts. `agents/proofer.md:119` defines the line: "A line of
that label names the finding whose fix made the unit". So "the
findings a line names" are the earlier findings that get named. The lines
themselves stand on the later findings that recur.

The two counts differ on the first work item the step will read, this one.
Its round records hold five such lines, and they name three distinct
findings: `round-2#1` twice, `round-1#4` twice and `round-1#1` once
(executed). A settling session that follows the bold sentence posts 3. One
that follows the command posts 5. The number goes to the durable
`flow-baseline` log and is held against 0.24.0's "17 recurring of 36".
The issue's own wording is "17 of 36 review findings recurred", which
counts the recurring findings, so the command is the right reading and the
words are wrong. Over #1177 the two readings happen to agree at 3, which
is why the baseline run could not show the gap.

The same words stand in two more places. Scope item 7 at
`frame/design.md:57` says "findings a `regression:` or `reopens:` line
names". The fragment's process row at `changelog.md:20` says "findings
named again", which also reads as the earlier finding. The three places
are the whole class: `grep` for "line names" and "named again" over the
frame, the fragment, `gaps.md` and the phase records found no fourth
(executed).

The fix names the finding that carries the line. The grammar allows a
finding at most one `regression:` or `reopens:` line
(`docs/the-review-record.md` *The round record*), so the line count and
the carrying-finding count are one number. This holds in either `seal/`
root and needs no other condition. The checklist step is this
repository's alone, and its root is shared.

```markdown
<!-- frame/design.md:267, the `to:` of the `add` to docs/release-checklist.md, its first clause -->
  to: **Before `seal settle --apply`, the settling session counts, for each released work item routed through the review chain, the findings, the findings that carry a `regression:` or `reopens:` line, the findings whose every `location:` path is under `seal/threads/`, and the rounds, and posts the four numbers as a comment on the open `flow-baseline` issue.**
```

```markdown
<!-- frame/design.md:57, Scope item 7, the second count -->
findings, findings that carry a `regression:` or `reopens:` line, findings whose every `location:` path is under `seal/threads/`, and rounds
```

```markdown
<!-- changelog.md:20, the process row's Change cell, the parenthesis -->
(findings, findings that carry a `regression:` or `reopens:` line, findings located only in the records, rounds)
```

The two frame lines are the framer's, and the orchestrator folds them. The
fragment's row belongs to whoever writes the fix.

answer: The process row's parenthesis at `changelog.md:20` now reads "findings that carry a `regression:` or `reopens:` line", the round's text as given; the orchestrator folded the two frame lines at `2c7ba65a`. `git grep -n 'named again\|line names'` over the tree finds no other statement of the measure's second count: the hits in `agents/proofer.md`, `docs/` and the code name what a line points at, not the count, and the hits in this round record are the finding's own quotes (executed).

### 2. The fix-pass sentence names two of the three readings its grounds list, and misses the one round 1's paste-ready fix failed

severity: should
location: `agents/crafter.md:168-172`, `tests/text/test_a_moved_rule_leaves_its_definition.py:542-550`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:63`, `seal/threads/1793343707-each-document-serves-one-reader/frame/plan.md:64`
evidence: read `agents/crafter.md:168-172`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:63`, `seal/threads/1793343707-each-document-serves-one-reader/trail/rounds/round-2.md:7-71`
verdict: fixed f6c65dac

The unit is the sentence that phase 7 added to `agents/crafter.md` *A fix
pass writes two lines of each finding and no phase record*. A build phase
made it, so it is new work, not a regression. Scope item 13 gives the
sentence three grounds. Round 1's finding 4 "cited a rule that lands only
at the settle". Round 2's finding 1 "put the removal under a log
condition". It also "counted with `git grep`". The sentence spells out
what the reading is for a procedure step: the step "is read in either
`seal/` root (contract rule 11) and under every condition its file names".
That covers the second and third grounds. It does not cover the first.

Run the first defect through the sentence as written. Round 1's
paste-ready step 7 sent the session to "the four numbers
`docs/the-review-record.md` *The run* names". That text existed only in
this design's `## Rule changes`, which a settle writes after the release
(round 2's finding 1). The step reads the same in a shared root and a
local one. Its file, the settle skill, names no condition that the
citation fails under. So a fix pass that does exactly the reading the
sentence spells out passes that text, and the first of the run's two
carried defects goes through again. The colon reads as the full reading
for a procedure step, so an agent stops at the two axes it names. Contract
rule 12 asks that the fix cover the whole class, and this one does not.
The class is a reader whose copy differs from the one the proofer read: in
its root, under its conditions, and in the release it ships in.

The fix adds the release as a third axis. It holds for a fix pass in any
repository and in either `seal/` root. It names nothing of this
repository, since every repository whose frames carry `## Rule changes`
gets its policy text at a later settle.

```markdown
<!-- agents/crafter.md:168-172 -->
A paste-ready fix is the proofer's claim and not the fix. Apply it only
after reading it as its text's own reader would: a procedure step is read
in either `seal/` root (contract rule 11), under every condition its file
names, and in the release that ships it, where a section it cites holds
that release's text and not what a design's `## Rule changes` writes at a
later settle. Where that reading fails, write the fix in your own words
and say so in `answer:`.
```

```python
# tests/text/test_a_moved_rule_leaves_its_definition.py:547-548, the entry
# for the reading's axes, replacing the one entry that spans both lines
        "in either `seal/` root (contract rule 11), under every condition "
        "its file names, and in the release that ships it",
        "not what a design's `## Rule changes` writes at a later settle",
```

Contract rule 15 asks to see the new entries fail first. Run the case
against `agents/crafter.md` as it stands, before the sentence changes. The
Scope item 13 sentence at `frame/design.md:63` ("a procedure step in every
root and under every condition its file names") and plan row A21b at
`frame/plan.md:64` gain "and in the release that ships it". They are the
framer's, and the orchestrator folds them. If this finding is taken, the
process row that finding 3 asks for states the sentence as it ends up.

answer: Taken, in the pass's own words. Read as the definition's reader would, the round's text fails one way: "and in the release that ships it, where a section it cites holds that release's text" lets "where" read as a condition on the release axis, so a reader may apply the axis only where a cited section holds that text; and "it" there may mean the fix or the step. The commit splits it: the step "is read in either `seal/` root (contract rule 11), under every condition its file names, and in the release that ships it. In that release, a section the step cites holds the text the release ships, not the text a design's `## Rule changes` writes at a later settle." Read in either root and in a user's repository, it holds: `## Rule changes` and the settle are named in the shipped template and skill, and it names nothing of this repository. The pin takes the two sentences as two entries, and the first was seen red against `agents/crafter.md` at `2c7ba65a` (exit 1, "the fix-pass rule lost 'in either `seal/` root (contract rule 11), under every condition its file names, and in the release that ships it.'"). After the commit, `seal mutate` deleted the second sentence, and the case went red, exit 1 (executed). The frame lines are the orchestrator's fold at `2c7ba65a`. Other places stating the sentence: the fragment's entry and process row (finding 3, `8123af5b`); `frame/questions.md:49` only points at Scope item 13; `trail/phases/phase-7.md` is the phase's history and stands (executed, `git grep -n 'paste-ready fix is\|under every condition'`).

### 3. The fragment states no change for the crafter's new fix-pass rule, though the diff changes `agents/crafter.md`

severity: must
location: `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:3`, `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:20`, `seal/threads/1793343707-each-document-serves-one-reader/frame/plan.md:77`
evidence: executed `grep -n -i 'paste' seal/threads/1793343707-each-document-serves-one-reader/changelog.md`
verdict: fixed 8123af5b

`docs/the-record-layout.md` *A change to the way of working writes its
process row in its own fragment* says a work item whose diff changes an
`agents/*.md` file ends its `changelog.md` with a `### Process changes`
table, "one row per change". Phase 7 changes `agents/crafter.md`: a fix
pass now reads a paste-ready fix as its reader would before applying it,
and writes the fix in its own words where that reading fails. The fragment
holds no row for that change, and its `### Changed` entry does not mention
it. A search for "paste" over the fragment printed nothing and exited 1
(executed). The `### Changed` entry does state the run's other agent rule
changes: the three-fix rule's move, and the framer's rule on marks. The
release note lifts the process rows into one table
(`docs/the-record-layout.md` *The release note lifts every process row
into one table*). So 0.25.1's note would leave out a change to how every
user's crafter answers a review round, and the next framer would not read
it. The cause is in the frame. Plan row 7 at `frame/plan.md:77` lists the
fragment's measure row and no row for the crafter sentence, and the
phase built what the row said. A build phase made the unit, so this is an
ordinary finding of new work.

The fix adds one process row after row 20 and one sentence to the
`### Changed` entry, after the sentence on the framer's rule. If finding
2's text is taken, the row's Change cell states the three axes. The
release note reads the fragment in either root, and the row holds under no
condition of its own.

```markdown
<!-- changelog.md, a new last row of ### Process changes -->
| 2026-10-30 | A fix pass reads a round's paste-ready fix as its text's own reader would before applying it, a procedure step in either `seal/` root and under every condition its file names, and writes the fix in its own words where that reading fails, saying so in `answer:` | Twice in this run a fix pass applied a round record's paste-ready text to the settle's step 7 as given, and each carried a new defect into shipped text | https://github.com/MichaelYcJo/AgenticSeal/issues/1148#issuecomment-6520356879 |
```

```markdown
<!-- changelog.md:3, after "... never by a new mark." -->
A fix pass now reads a review round's paste-ready fix as the text's own reader would before applying it, and writes the fix in its own words where that reading fails.
```

Plan row 7's cell at `frame/plan.md:77` is the framer's. It is history
once the row's Status cell is filled, so it needs no fold unless the
framer wants the row to name the fragment's row.

answer: A new last row of `### Process changes` and one sentence in the `### Changed` entry, after the framer's rule. Each states the sentence as it ends up after finding 2, with the release as the third axis, which the round's row text lacked. *A change to the way of working writes its process row in its own fragment* asks for the row and not for an entry sentence. The sentence is there because `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along* has the fragment state what ships, and the entry already states the run's other agent rules. The row's Source, `#issuecomment-6520356879`, is the orchestrator's comment of 2026-10-30 on this recurrence (executed, `gh api`). `tests/github/test_publish_release_note.py` passed in the boundary run, exit 0 (executed).

## Confirmations

confirms: round-3#1
The redesign answers it. Round 3's finding 1 was that `seal settle
--apply` sat under step 7's `flow-baseline` condition. Step 7 of
`skills/settle/SKILL.md` *The settling session's procedure* now reads
"7. Run `seal settle --apply`." with no condition. The skill and the pin's
module are byte for byte the base's:
`git diff --stat fba13ab2 f279997c -- skills/settle/SKILL.md tests/text/test_settle_reads_before_it_removes.py`
printed nothing (executed). The crafter claimed the same, and that claim
holds. The Table B row at `frame/design.md:133` no longer puts the removal
under any condition (read). The `add` to `docs/the-review-record.md` *The
run*, the second place round 3 named, has left `## Rule changes`.
`rule_changes.parse` over the design read 17 operations, none of them in
that document (executed). The new `add` to 2b puts no condition on the
removal. The checklist's code block at `docs/release-checklist.md:37-41`
runs `seal settle --apply` with nothing in front of it (read).

confirms: round-3#2
The redesign answers it. No shipped step counts anything now. `git grep -n
'four numbers\|four counts' -- skills agents templates` printed nothing
and exited 1 (executed), as scenario S9 says. The measure's commands in
*Data & interfaces* use `grep -h` over `<root>/threads/<id>/`, with
`<root>` set to `$(git rev-parse --git-common-dir)/seal` in local mode.
That matches `skills/settle/SKILL.md:265` *In local mode* "Where it reads"
(read). Round 3's executed line, re-run in the clone:
`git grep -h '^\[core\]' -- .git/config` printed nothing and exited 1, and
`grep -h '^\[core\]' .git/config` printed the line and exited 0
(executed). So the new commands read a file under the git directory, which
round 3's commands could not.

confirms: none
The build's other claims hold. The four commands over #1177's
records at `f279997c` print 10, 3, 1 and 8, as S9 states (executed). I
deleted the sentence "Where that reading fails, write the fix in your own
words and say so in `answer:`." from `agents/crafter.md` in the clone
through the `Edit` tool. The fix-pass case then failed on "the fix-pass
rule lost", and the file was put back with `git status --short` empty
(executed). This repeats the phase record's mutant. No case function was
added. The four clauses went into the one case that reads the paragraph,
so there was no group to read them against. The narrow modules for the
paths the range changed were the seven named in plan row 7, with
`tests/skills/test_rule_changes.py` and `tests/skills/test_payload_meter.py`
added. They gave `555 passed`, exit 0 (executed). `ruff check` and `ruff
format --check` over the two changed test files each exited 0 (executed).
All three commits carry `Seal-Routing:
1793343707-each-document-serves-one-reader` (executed). The `add`'s
`section` stands at `docs/release-checklist.md:31-61`, and every `from` of
the 17 operations stands in its section (executed). The frame carries
`Reframed 2026-10-30 by framer, after round 3.` under its mark at
`frame/design.md:340` (read). Carried from round 3 and not established
again: the coordinates of *In local mode* in the settle skill, and the
#1177 record path. No `seal/parity.md` is declared, so this record names
no baseline commit.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the settle after 0.25.1 takes the four counts. That settle writes the `add` into 2b at its step 2, and its step 7 removes the records the counts read. `frame/plan.md` A20c names this as the cost, and no run here can show what that session will do. In shared mode git keeps the removed records at `<commit>:<path>`, so a count it misses can still be taken from history | `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:267` | the owner's settling session, at the settle after 0.25.1 |
| The `add` says the step "ships to no user", and Scope item 7 says "nothing the plugin ships carries it". But the plugin's package holds `docs/release-checklist.md`, and `skills/settle/SKILL.md:146` sends every settling session to its 2b. A user's agent reading this repository's process documents as policy is the ground the issue's proposal P4 moved to #1147 | `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:267`, `skills/settle/SKILL.md:146` | #1147 |
| Round 1's finding 6 stands `deferred frame/questions.md Q2` and is not written up again. Its shortstat was not taken again | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, answering Q2 |
| Carried: the behaviour suite over the agent definitions, the new fix-pass sentence in `agents/crafter.md` among them, not run on Q1's default | `agents/crafter.md:168-172` | the owner, at the pull request |
| Carried from round 1: a finding located in `frame/design.md` `## Rule changes` and fixed there alone passes with no round, and the settle writes that text into the policy root. Findings 1 and 2 are partly located there | `skills/code-review/scripts/chain_check.py:1452-1456` | the owner |
| Carried from round 2: 19 of the 25 commits in `fba13ab2..b3b36143` carry no `Seal-Routing:` trailer | `fba13ab2..b3b36143` | the orchestrator |
| Carried from round 1: GitHub's rendering of the body's fold | `skills/code-review/scripts/pr_body.py` | the orchestrator, reading the first body this change writes |
| The full suite, the repository-wide lint and format check, and the cross-platform run at `f279997c`. The suite is `unverified` here | the branch at `f279997c` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git diff --stat fba13ab2 f279997c -- skills/settle/SKILL.md tests/text/test_settle_reads_before_it_removes.py` in the clone | no output, exit 0 |
| `rule_changes.parse` over the design at `f279997c` with policy root `docs`, each op's `section` and `from` looked up in its document | 17 ops, 0 refusals, 0 missing; the 2b `add` lands in lines 31 to 61 |
| The four measure commands over `seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/` | 10, 3, 1, 8 |
| `grep -h '^regression: \|^reopens: '` over this work item's rounds, with `wc -l` and with `sort -u` then `wc -l` | 5 lines; 3 distinct findings named |
| `git grep -n 'four numbers\|four counts' -- skills agents templates` | no output, exit 1 |
| `git grep -h '^\[core\]' -- .git/config`, then `grep -h '^\[core\]' .git/config` | exit 1 with no output; exit 0 printing the line |
| The last sentence of the new fix-pass clause deleted from `agents/crafter.md` through `Edit`, then `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -k crafters_fix_pass -q -p no:xdist`, then the sentence restored through `Edit` | exit 1, "the fix-pass rule lost"; `git status --short` empty after the restore |
| `bin/test` over the seven modules of plan row 7 with `tests/skills/test_rule_changes.py` and `tests/skills/test_payload_meter.py` | exit 0, `555 passed` |
| `uvx ruff check` and `uvx ruff format --check` over the two changed test files | exit 0 and exit 0 |
| `grep -n -i 'paste'` over this work item's `changelog.md` | no output, exit 1 |
