# Review round 1: 1793678623-each-rule-rides-with-the-agent-that-uses-it

```seal
target: e045e7264 against release/v0.30.1
```

This round reviews the branch at e045e7264 against `release/v0.30.1`, which
is 0c68b9933, the 0.30.0 release. No earlier round exists, so no fact is
carried; every fact below was opened this round. The repository declares no
`seal/parity.md` (`git ls-files seal/parity.md`, executed, no output), so no
`original:` line is owed. The runs took place in a `git clone --no-local` at
e045e7264 in the session scratchpad, which has since been removed.

Stage 1 read the diff against issue #1313 (`gh issue view 1313 --json
body,comments`, executed, no comments), `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, the four phase records and `gaps.md`. Stage 2 read the
changed tests against the cases they replace.

## Findings

### 1. The commit rule leaves the preload of agents that still commit, and no file they open at that step states it

```seal
severity: should
location: `skills/agent-contract/SKILL.md:76-85`, `tests/behaviour/test_a_commit_names_its_repository.py:10-12`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/changelog.md:3`
evidence: executed `git grep -n "git -C" -- agents/ skills/code-review/SKILL.md skills/agent-contract/SKILL.md skills/core/SKILL.md`, `grep -n -i commit agents/framer.md agents/proofer.md agents/sealer.md agents/tracer.md skills/code-review/SKILL.md`
```

Why it matters: old contract rule 16 told every agent how to commit so that a
failed `cd` cannot land the commit in the session's own repository. In a
review spawn, that repository is the checkout of the branch under review. D1
moves the rule to `skills/implement/SKILL.md` *2.* on the grounds that "the
parties that commit read that file: the crafter (87 of 88 spawns), the session
where it builds, and the orchestrator" (`frame/design.md:235`). The frame's
own reading names a fourth party. Row 16 says "the framer commits only where a
spawn prompt asks, as this one did" (`frame/design.md:141`). The framer reads
only three sections of implement: the language section, *1.* and *3.*
(`agents/framer.md:49-52`). It never reaches *2.*, where the rule now stands.

The rule also covers a probe that commits. That is why
`skills/code-review/SKILL.md` *Probes and regression tests* names
`tests/behaviour/test_a_probe_that_commits_says_so.py` as its check, and that
module's docstring records #82: a review agent's round-1 probes that committed
(`tests/behaviour/test_a_probe_that_commits_says_so.py:3-7`, read). At HEAD,
no preloaded file and no section of `skills/code-review/SKILL.md` says how to
commit. The search above lists only the sealer's two read-only `git -C <root>`
commands. The proofer opens implement in 38 of 136 spawns (`frame/design.md`
*Grounding*), and even then *2.* is the builder's test-first section. So the
proofer's probes, the sealer's re-runs and a framer asked to commit each lose
the form at the step where they commit.

The claim was that "every other agent stops paying 714 bytes per spawn" with
nothing lost. The reading shows the framer and every agent whose probes commit
losing a rule they act on. The fix below puts back one pointer sentence of
about 230 bytes, against the 714 that left. The preload still falls for every
agent.

The snippet covers the contract, the case module's docstring that states the
same premise, and the changelog bullet. It leaves `frame/design.md` row 16
and D1 as the framer wrote them, since the frame is the framer's reading, and
the fix pass's close names them. A fix pass that prefers no contract bytes
may instead add the pointer to `skills/code-review/SKILL.md` *Probes and
regression tests* and to `agents/framer.md`. That still leaves the sealer's
and the tracer's probes without the form, and the close should then say so.

```markdown
In skills/agent-contract/SKILL.md, rule 6, after "and spawn no agent.":

A commit you do make, a probe's included, writes the repository's absolute
path after `git -C` in a command of its own, as `skills/implement/SKILL.md`
*A commit names its repository in the command that makes it* states.

In tests/behaviour/test_a_commit_names_its_repository.py, docstring lines 10-12:

The rule stands in `skills/implement/SKILL.md` *2. Implement test-first, and
let each rule name its test*, read by the crafter, the session that builds
and the orchestrator; contract rule 6 points every other agent's commit at it.

In the work item's changelog.md, first bullet, after "all read that file.":

Contract rule 6 points every other agent's commit, a probe's included, at it in one sentence.
```

```seal
verdict: fixed 3a4d969b7
answer: The finding holds. The framer commits where a spawn prompt asks (`frame/design.md:141`) and reads only implement's language section, *1.* and *3.* (`agents/framer.md:49-52`). A proofer, sealer or tracer probe may commit in its clone, and none of them opens implement *2.*. So at the step where they commit, no file in front of them gave the `git -C` form. 3a4d969b7 applies the contract sentence of the paste-ready fix as given, in rule 6 after "and spawn no agent.", 220 bytes. It was read against the tree first. Rule 11 resolves its `skills/` path as the plugin's ("here" is the contract). The cited bold lead stands at `skills/implement/SKILL.md:193`, and `test_a_cited_section_stands_in_its_file.py` resolves it. "In a command of its own" is the rule's own first sentence, so the sentence restates nothing past it. The contract was chosen over the cheaper alternative, `skills/code-review/SKILL.md` and `agents/framer.md`. The contract is the one file all five agents have in front of them at every step. The alternative reaches the proofer and the framer only. It leaves the sealer's and the tracer's probes without the form, and it states the sentence twice. The docstring and changelog fixes were written in my own words, not the snippet's. The docstring of `tests/behaviour/test_a_commit_names_its_repository.py` now says that rule 6 states the form for agents that commit at a step that never opens *2.*. The changelog's first bullet says the same. Its last bullet now gives the preloads at 3a4d969b7: crafter 31,730, framer 34,836, proofer 30,840, sealer 30,556 and tracer 23,970, each still below v0.30.0. Its *Process changes* row on the commit rule names the sentence and its grounds. A new case, `test_the_contract_points_every_agents_commit_at_the_rule`, was seen red against the contract before the edit: exit 1, 1 failed and 4 passed. It then went green. `gaps.md` gains the row that whether a 0.30.1 agent follows the sentence is Q1's measurement. dbf25435e corrects `tests/behaviour/test_a_probe_that_commits_says_so.py`'s docstring, which said a probe owes only rules 7 and 9. `frame/design.md` row 16 and D1, and `frame/plan.md`'s *Alternatives considered* row on rule 16, still say that only builders and the orchestrator commit. They are the framer's, and are left as written. `trail/phases/phase-4.md`'s preload table is phase 4's reading at 08b43c65f, 220 bytes below HEAD for each agent.
location: `skills/agent-contract/SKILL.md:83-86`, `tests/behaviour/test_a_commit_names_its_repository.py:10-18`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/changelog.md:3`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/gaps.md:14`
```

## Confirmations

```seal
confirms: none
```
What matched: the preload rows in `trail/phases/phase-4.md` and the
changelog. The definition, the core and the contract were summed with
`git show <commit>:<path>` and `wc -c` at 0c68b9933 and at HEAD (executed).
At the base they are crafter 33,081, framer 36,362, proofer 32,293, sealer
31,879 and tracer 25,085. At HEAD they are 31,510, 34,616, 30,620, 30,336 and
23,750. Each agent's `skills:` list is `core` and `agent-contract`, so the sum
is what `release_report.py#preloads` reads. No agent's preload grows (S7).

```seal
confirms: none
```
What matched: the ten-word census (S8). A probe written this round from D6's
method, independently of the crafter's, read every tracked `.md` and `.py`
file outside `seal/` and `tests/` at both commits (executed). It gave the
frame's base reading in every cell, 934 of 11,209, and the phase 4 HEAD
column in every cell, 754 of 10,733.

```seal
confirms: none
```
What matched: phase 1's departure from D2. The builders claimed that D2's
"up to the highest heading" cannot hold for D2's own list. The highest
heading at HEAD is 19 and the list holds 20, so that reading would count a
listed 20 as a fault on the tree D2 builds. `numbering_faults` instead runs
its range to the larger of the two
(`tests/text/test_the_agent_contract_holds_the_universal_rules.py:145-160`,
read). That is the stricter reading, and it matches D2's sentence that a new
rule takes the number after the highest one used. The list is whole at HEAD:
the contract never held a `## 21` heading (`git log --oneline -S"## 21 " --
skills/agent-contract/SKILL.md`, executed, no lines), and every number from 1
to 20 is a heading or a listed number.

The `gaps.md` row on the highest number is answered for this diff. 20 is
listed. The limit stays a review duty on later diffs, as the module docstring
says. The three planted cases each fail on a different branch of
`numbering_faults`: an unlisted gap, a repeat, and a listed heading. None
duplicates the module's existing numbering case. One limit is not in the
docstring. `RETIRED` reads a list written with a comma before `and`, such as
`8, 16, and 20`, only as far as `16`. A heading 20 would then pass unseen.
The preamble does not use that spelling, so this is no defect today.

```seal
confirms: none
```
What matched: phase 4's departure from D6 and the plan. The
`.github/scripts/release_report.py` docstring gives `--at` as the tag's tree
and `--root` as this one (`:8-10`). `main` reads `at` from `--at` and `now`
from `--root` (`:317-325`, read). So the frame's `--at <clone at HEAD>` would
have measured HEAD as the tag, and the builders' flags are the right ones.

```seal
confirms: none
```
What matched: no tracked file outside the records cites a retired number as a
live rule (S4). A whitespace-folded regex over `git ls-files` outside `seal/`,
`CHANGELOG.md` and `.test_durations` looked for `rule` or `rules`, an optional
list, then 8, 16 or 20 (executed). It found only the five rule 8 mentions in
`tests/behaviour/test_a_probe_that_commits_says_so.py`, each naming 8 as
retired. A `git grep` for 8, 16 and 20 after the section sign (U+00A7), and for
`contract's rule`, `eighth rule` and `twentieth`, found no citation
(executed). The method covers the
`rule N` spellings. A citation in other words is still a sample, as the phase
records say.

```seal
confirms: none
```
What matched: each D3 removal is reachable at its step (S6), read at HEAD.

- `skills/legacy-parity/SKILL.md:102-121` *Recording the comparison* states
  the proofer's round-block `original:` line and `unread` finding. It also
  states the sealer's verdict-block line and its `withheld` verdict, and both
  steps open that skill in the same sentence.
- `skills/implement/SKILL.md:77-80` states that a reference root is read where
  the work touches it. The crafter opens that file at step 1, and the framer
  through *A design states its rule changes* (`agents/framer.md:181-183`).
- The crafter's old half, "cited where `frame/design.md` cites it", is not
  restated there. Crafter step 8 still asks for each decision with the
  document it was judged against, so the citation stays owed.
- Contract rule 11 now holds the plugin-path sentence for all five
  definitions, and tracer step 1 rests on it.
- The removed preamble sentences stand in every definition's opening sentence
  and in the core's *Each agent judges its own target*.

```seal
confirms: none
```
What matched: the two `gaps.md` rows saying no case reads the phase-boundary
set or the plugin-path sentence. A `git grep` over `tests/` and `evals/` for
the set's words (`glob the directory`, `plan row names`, `test modules that
read a path`) and for `two directories above` found no line at 0c68b9933,
exit 1, and none at HEAD (executed). So the moves took no case away from
either sentence. `skills/verify/SKILL.md` *The narrow command still has to be
able to fail* asks no new case of a move. These rows are limits that predate
the change, not defects it made. A `git grep` for `phase.boundary` outside
`tests/` lists only `agents/crafter.md:47`, `skills/verify/SKILL.md:144` and
an unrelated `skills/code-review/orchestration.md:21` (executed). The set has
one statement.

```seal
confirms: none
```
What matched: the framer's subject judgment, `## Rule changes` `- nothing`
(D7). `docs/running/the-agent-set.md:20-23` says how a retired rule keeps its
number "is the contract's own preamble", which still holds (read). `git grep`
over `docs/` for `rule 2`, `preload`, the moved sentences' words and counts
of contract rules found no sentence stating a fact this diff changes
(executed). `git diff --stat 0c68b9933..HEAD` touches no `docs/` file, and in
`skills/*/orchestration.md` only the re-pointed rule 16 citation (S9,
executed).

```seal
confirms: none
```
What matched: the history search (the issue's *What the reading removes*).
At HEAD, D1's pattern grep over `agents/*.md`, the core and the contract
found no sentence of history (executed). Every hit is a present-tense
instruction about releases or tags.

```seal
confirms: none
```
What matched: the changed and dependent modules pass at HEAD. One `bin/test`
command over eleven modules exited 0 with 371 passed (executed): the contract
module, the cited-section, commit, probe and reference-root modules, the
moved-rule, one-owner, every-agent, broad-gate-rule, line-wrap and
writing-style-section modules.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, lint and typecheck at HEAD: the suite is `unverified` here | the repository's `Broad gate` row | the orchestrator, at the broad run after the rounds settle |
| Whether agents spawned under 0.30.1 commit in the `git -C` form, run the set from the verify row and resolve plugin paths through rule 11 | `frame/questions.md` Q1 | the Q1 measurement on the first 0.30.1 transcripts |
| Whether a paid behaviour-suite run is owed for this preload rewrite | `frame/plan.md` *Judgments of the run* | the orchestrator, whose judgment it is; this round read its grounds in `evals/README.md` and took no run |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the eleven modules named above, `-q`, in the scratch clone at e045e7264 | exit 0, 371 passed |
| `python3 -I test_tmp_census.py <clone> 0c68b9933 e045e7264`, one file written this round to D6's method | exit 0; 934 of 11,209 at the base and 754 of 10,733 at HEAD, every per-file row equal to the phase 4 table; the file, its output and the clone were deleted |
| `git log --oneline -S"## 21 " -- skills/agent-contract/SKILL.md` | exit 0, no lines |
| `git grep` over `tests/` and `evals/` for the phase-boundary set's words and `two directories above`, at 0c68b9933 | exit 1, no lines |
