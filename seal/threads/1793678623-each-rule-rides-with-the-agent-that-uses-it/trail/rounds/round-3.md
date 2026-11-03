# Review round 3: 1793678623-each-rule-rides-with-the-agent-that-uses-it

```seal
target: cab91086e, fixes d544e722b..cab91086e
```

This is a verifying round. It reads the diff of the last fixes,
`git diff d544e722b cab91086e`, which holds 1fecf8ee8, 6a0d36caf, d90b20d83,
139bfad50 and cab91086e (executed). Outside `seal/` the diff changes only the
docstrings of `tests/behaviour/test_a_commit_names_its_repository.py` and
`tests/behaviour/test_a_probe_that_commits_says_so.py` (executed). The
branch's base is `release/v0.30.1` at 0c68b9933, which is also the merge base
(executed). The repository tracks no `seal/parity.md` (`git ls-files`,
executed, no output), so no `original:` line is owed. `seal/config.md` has no
`Record language` row, so the record is English. The runs took place in a
`git clone --no-local` at cab91086e under this round's scratch directory,
which has since been removed.

Carried from round 2 and not re-established: the census reading at
d544e722b, 766 of 10,769 words shared, with the contract at 70 of 1,975. It
was carried because its check holds: no file outside `seal/` and `tests/`
changed between d544e722b and cab91086e (`git diff --stat`, executed, no
output), and the census reads only those files. Also carried from round 1:
each agent's `skills:` list is `core` and `agent-contract`. Every verdict
below was reached this round.

The fix pass's account was read as a claim. It claimed to have read every
file of the work item's directory whole against HEAD. It named five frame
statements HEAD contradicted, and the orchestrator folded four at cab91086e
and left D5 with a row in `frame/plan.md` *Judgments of the run*. Round 2's
finding 3 was closed with the claim that every row of `gaps.md` was read
whole and that rows 10 and 15 match Q1. That claim does not hold for rows 7
and 11, as finding 1 sets out. The other claims hold, as the confirmations
set out.

## Findings

### 1. Two more gaps rows hand a question to Q1's measurement, and Q1 asks neither

```seal
severity: should
location: `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/questions.md:16`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:7`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:11`
evidence: read `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/frame/questions.md:16`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:7`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:11`
reopens: round-2#3
```

Why the close does not hold: round 2's finding 3 named a defect in one row,
`gaps.md:14`. That row handed a question to "Q1's measurement", and Q1 did
not count what the row asks. 6a0d36caf widened Q1, and for row 14 the close
holds. Q1 now asks whether a framer or a probe writes the `git -C` form. It
also counts every agent's commits (`frame/questions.md:16`, read). But the
close also claimed that every row of `gaps.md` was read against HEAD. It
named rows 10 and 15 as the other rows that cite Q1. A search for `Q1` over
the work item lists five rows: 7, 10, 11, 14 and 15 (`git grep`, executed).
The close's list left out rows 7 and 11. Contract rule 12 makes the fix owe
every instance its cause produces. It also says that a sample handed back as
a whole list is a finding. Rows 7 and 11 were written by phases 1 and 3
(`git log`, executed). The reopen is not about those phases. It is about the
fix's enumeration, which named the class whole and was a sample.

The two instances:

- `gaps.md:7` asks two questions. Does an agent that adds a rule take the
  number after the highest one used? Does a session that reads an old
  record's rule 8 or rule 20 find it named as retired? The row hands "the
  live reading" to Q1. Q1 asks about the installed preload, the crafter's
  phase-boundary runs and the `git -C` form of commits. It asks nothing about
  numbering.
- `gaps.md:11` asks three questions about agents spawned under 0.30.1. Do
  they still resolve `skills/` paths at the plugin's root? Do they still
  write the `original:` line? Do they still read a reference root? The row
  names "Q1's measurement" as the answerer. Q1 counts none of the three.

Why it matters: contract rule 4 asks that each `unverified` claim name who
answers it. Whoever answers Q1 as written counts preload rows,
phase-boundary runs and commits. They never look for a path resolution, an
`original:` line, a reference-root read or a rule's number. So the live half
of rows 7 and 11 has no answerer. A complete answer to Q1 would leave both
rows open with nobody to close them. This is the defect round 2 found in row
14, at two more rows.

The snippet widens Q1 again, so that the five rows citing it can stand as
written. Its question becomes general and names each act the rows hand to
it. The statements it touches are Q1's question cell and its options cell.
Rows 7, 10, 11, 14 and 15 of `gaps.md` then hold without an edit.
`frame/plan.md:85` says Q1 now states "the commits Q1 counts". That row is
the run's dated record of the fold, and it stays as written. The fix pass may
instead give rows 7 and 11 another answerer in their second cell. If it does,
it owes the reason in the close.

```markdown
In frame/questions.md, Q1's question cell, replace from "and does a framer
or a probe" up to "No probe can answer it" with:

and does every agent spawned under it take each act whose text this item
moved, as the `gaps.md` *Not verified* rows that cite this question name
them: a framer's or any probe's commit in the `git -C` form contract rule 6
states, a `skills/` path resolved at the plugin's root through contract rule
11, the `original:` line written from `skills/legacy-parity/SKILL.md`
*Recording the comparison*, a reference root read from
`skills/implement/SKILL.md` *Document layout*, a new rule numbered after the
highest one used, and an old record's rule 8 or 20 read as retired? No probe
can answer it

In the same row's options cell, after "of commits in the `git -C` form",
add:

; and, over the same transcripts, each other act a `gaps.md` *Not verified*
row hands to this question, and whether it took the form the moved text
states
```

```seal
verdict: fixed e896e0e33
answer: The finding holds. My round 2 close named rows 10 and 15 from memory, and that was a sample. This time the rows were listed by command: `git grep -n Q1 -- seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md` (executed). It lists five rows: 7, 10, 11, 14 and 15, and no other row of `gaps.md` names Q1. Each row was read whole against Q1 at HEAD, which 7f36b8d33 widened (read). 7f36b8d33 rewrote Q1 in the orchestrator's own words and did not use the snippet. Row 7 asks whether an agent that adds a rule takes the number after the highest used, which Q1 now asks. Its second question said "a session reading an old record's rule 8 or rule 20", while Q1 asks about an agent reading rule 8, 16 or 20. So e896e0e33 rewords the row to "an agent reading an old record's rule 8, 16 or 20". Q1's measurement reads agents' transcripts, so a session was a reader it never opens, and 16 is a number this work retired after phase 1 wrote the row. Row 10, the crafter's phase-boundary runs and its `git -C` commits, matches Q1's crafter set and its every-agent commit form. Row 11 names three acts, and Q1 now names each of them. They are paths resolved at the plugin's root through rule 11, the parity record written from `skills/legacy-parity/SKILL.md` *Recording the comparison*, and a reference root read from `skills/implement/SKILL.md` *Document layout*. Row 14, a framer's or a probe's `git -C` commit, matches Q1's every-agent commit. Row 15, what a spawn pays under 0.30.1, matches Q1's installed preload and the `preload` rows. One part of Q1 is the frame's, and I did not change it. Its options cell lists the measurements, but reading an old rule 8, 16 or 20 as retired is not among them, while its question asks that.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the close `fixed 6a0d36caf` holds. S2 now says that the contract
no longer holds the phase-boundary set. It says that of the commit rule the
contract holds only rule 6's sentence, which states the `git -C` form and
points at implement's rule. That sentence is in the contract
(`frame/design.md:108`, read; `skills/agent-contract/SKILL.md:83-86`, read).
A search of the contract for "phase boundary" finds no line (`git grep`,
executed, exit 1). Rule 2 now holds only the slice tests, the broad gate and
the `unverified` hand-over (`skills/agent-contract/SKILL.md:35-42`, read).
S2's verification cell names
`test_the_contract_points_every_agents_commit_at_the_rule`, which stands at
`tests/behaviour/test_a_commit_names_its_repository.py:70` (read). That
module and `tests/text/test_broad_gate_rule.py` passed in this round's narrow
run (executed). Scope 2 at `frame/design.md:47-51` states the same fact in
the same terms (read).

```seal
confirms: round-2#2
```
What holds: the close `fixed d90b20d83` holds for the changelog. The census
half of `changelog.md:6` reads "766 of 10,769". That is round 2's executed
reading at d544e722b, and no file the census reads has changed since
(executed, the diff above). The preload half matches HEAD. Each agent's
definition, the core and the contract sum to 31,730, 34,836, 30,840, 30,556
and 23,970 bytes (`wc -c`, executed), as the bullet says. The frame half is
6a0d36caf's. D6 now says that the last phase record states the commit it
measured. It says a later fix brings the changelog's figures to HEAD, and
the body copies the figures from the changelog (`frame/design.md:339-343`,
read). S7 and S8 say the same (`frame/design.md:113-114`, read).
`trail/phases/phase-4.md:38-75` names the commits its tables measured (read).

The fix claims two docstrings, and the changelog's first bullet, say that no
step of the agents that commit without implement's *2.* opens it. That
holds. The framer's step 3 reads `## The language the records are written
in`, *1.* and *3.* of that file (`agents/framer.md:49-52`, read). A search of
the proofer's, sealer's and tracer's definitions for "implement" finds no
citation of that file. The two proofer lines it finds say "implementer"
(`grep`, executed). The rewrapped docstrings pass the lint and the
formatter's check (`uvx ruff check`, `uvx ruff format --check` on the two
files, executed, exit 0).

Scope item 6 (`frame/design.md:62-63`) still says the measurement goes "in
the last phase record, for the pull request". It does not say that the body
copies the figures from there. Phase 4 holds both readings with the commit
each measured. `seal pr-body` copies the phase records' paths (round 2's
coordinate `skills/code-review/scripts/pr_body.py:9-17`, carried). So the
sentence is true as written, and it is no finding.

```seal
confirms: none
```
What matched: the four statements the orchestrator folded at cab91086e, each
read against HEAD. D1's phase-boundary row says the verify row "now holds
the set itself" (`frame/design.md:237`). The *Phase boundary* row holds it
(`skills/verify/SKILL.md:144`). D3's heading for rule 11 (`frame/design.md:284`)
is the contract's heading word for word (`skills/agent-contract/SKILL.md:132`).
D6's flags (`frame/design.md:325-329`) and phase 4's *Verified by* cell
(`frame/plan.md:69`) give `--at` the base and `--root` HEAD. The script's
usage line and docstring say the same, and so does its parser
(`.github/scripts/release_report.py:4`, `:9-10`, `:316-318`). S8
(`frame/design.md:114`) matches `trail/phases/phase-4.md:56-75` and
`changelog.md:6`. Each is read.

```seal
confirms: none
```
What matched: D5, which the orchestrator left as it stands. Its figures are
labelled as estimates that the measurement decides (`frame/design.md:309`).
Phase 4 sets them against the measured change (`trail/phases/phase-4.md:50-52`,
read). Its last sentence prices rule 16's move "for the crafter and the
framer when they read *2.*" (`frame/design.md:320-321`). The framer's step
reads other sections (`agents/framer.md:49-52`). The sentence reads as a
cost that applies when the framer reads *2.*, not as a claim that its step
does. So it does not contradict the changelog's "no step of theirs opens
that section". The plan's alternatives on implement's *2.* and *5.*
(`frame/plan.md:53`, `:57`) price the framer's read of the whole file the
same way. *Grounding* counts that read in 53 of 54 spawns
(`frame/design.md:35`). Each is read. No finding.

```seal
confirms: none
```
What matched: the narrow run at cab91086e. One `bin/test` command over the
two modules whose docstrings changed covered S2's two verification modules.
It also covered the contract-shape module and the cited-section module.
It exited 0 with 79 passed (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, lint and typecheck at HEAD. The suite is `unverified` here | the repository's `Broad gate` row in `seal/config.md` | the orchestrator, at the broad run after the rounds settle. With no finding left open, the sealer's spawn follows it |
| Whether agents spawned under 0.30.1 take the acts the moved text states | `frame/questions.md` Q1, once finding 1 widens it | the Q1 measurement on the first 0.30.1 transcripts |

## Probes

| Command | Result |
|---|---|
| `git diff --stat d544e722b cab91086e -- ':!seal/' ':!tests/'` | exit 0, no output |
| `git grep -n -i "phase.boundary" -- skills/agent-contract/SKILL.md` | exit 1, no lines |
| `cat agents/<agent>.md skills/core/SKILL.md skills/agent-contract/SKILL.md \| wc -c` for each of the five agents, at cab91086e | 31,730, 34,836, 30,840, 30,556 and 23,970 |
| `git grep -n "Q1" -- seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/ ':!*/trail/rounds/*'` | `frame/plan.md:85`, `frame/questions.md:16`, and `gaps.md` rows 7, 10, 11, 14 and 15 |
| `bin/test` over `tests/behaviour/test_a_commit_names_its_repository.py`, `tests/behaviour/test_a_probe_that_commits_says_so.py`, `tests/text/test_broad_gate_rule.py`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `-q`, in the scratch clone at cab91086e | exit 0, 79 passed |
| `uvx ruff check` and `uvx ruff format --check` over the two changed test files, in the same clone | exit 0 each |
| `grep -n "implement" agents/framer.md agents/proofer.md agents/sealer.md agents/tracer.md` | framer lines 22, 49, 71, 165 and 182; proofer lines 68 and 92, each "implementer"; sealer and tracer none |
