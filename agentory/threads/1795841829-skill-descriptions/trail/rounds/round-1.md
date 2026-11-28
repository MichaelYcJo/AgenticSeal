# Review round 1: 1795841829-skill-descriptions

```iadd
target: c2388b71 against origin/release/v0.41.0
```

Round 1 is a finding round over the whole range from the base,
`origin/release/v0.41.0` at `991a51c7`, to `c2388b71`. No earlier round
exists, so no fact was carried from one and every verdict below was reached
here. The base holds the same `skills/`, `agents/` and `.claude-plugin/` as
the `v0.40.1` tag (executed: `git diff --stat v0.40.1 991a51c7 -- skills
agents .claude-plugin` printed nothing). `agentory/parity.json` is not
declared, so no parity comparison is owed. The records read whole at the
target are `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and
`trail/phases/phase-1.md`. No `pr.<lang>.md` stands, and none is owed,
because both language keys of `agentory/config.json` read `English`.

## Findings

### 1. Three `NOT for:` items are kept as answering a recorded confusion, and the frame records a confusion for two of them

```iadd
severity: should
location: `agentory/threads/1795841829-skill-descriptions/frame/design.md:18`, `agentory/threads/1795841829-skill-descriptions/frame/design.md:32`, `agentory/threads/1795841829-skill-descriptions/frame/design.md:57`, `agentory/threads/1795841829-skill-descriptions/changelog.md:3`
evidence: executed `git grep -n -E 'recorded confusion|confusion (was|is) recorded|records the confusion|confusion on record' c2388b71 -- agentory/threads/1795841829-skill-descriptions docs/experiments tests skills`, `git log --reverse --format=%h -S'prose and structure of a PR body' -- skills/commit-pr-convention/SKILL.md`, `git log --format='%h %s' -i --grep=commit-pr-convention`; read `agentory/threads/1795841829-skill-descriptions/frame/plan.md:36`, `agentory/threads/1795841829-skill-descriptions/frame/design.md:60`
```

Why it matters: the changelog fragment becomes the release note, and it
says that `code-review`, `commit-pr-convention` and `writing-style` "each
keep the one item a recorded confusion asked for" (`changelog.md:3`). The
frame's rule for the build says the same of each kept clause: *Scope* item
3 opens "A `NOT for:` clause stays only where G10 records the confusion it
names" (`frame/design.md:32`), and S2 is titled "A `NOT for:` clause stays
only where a confusion is recorded" (`frame/design.md:57`). G10
(`frame/design.md:18`) records two confusions and no third. It records the
writing-style clause that names `commit-pr-convention`, whose case
docstring says its loss "is what shipped a PR with no prefix", and the
code-review clause on a typed `/code-review`. For `commit-pr-convention` it
names only "commit-pr-convention's other items" as carrying none, and says
nothing of the item the build keeps, the prose and structure of a PR body
or review comment. The plan agrees with G10, not with *Scope* item 3: A6
reads "the two with a recorded confusion" (`frame/plan.md:36`), and S5
reads "The two clauses with a recorded confusion" (`frame/design.md:60`).
The history finds no third: the item stands in `716d8548`, the initial
commit, and no commit message that names `commit-pr-convention` records a
session that took a PR body's prose to it.

The build follows *Scope* item 3's list exactly, so this is no compliance
defect in the code. The defect is that the rule the frame states, and the
release note repeats, is not the rule the build kept to. The paste-ready
fix keeps the build. It states the ground the item actually has, the
receiving side of the writing-style handoff G10 records, in G10, in the
rule and in the release note. Where the fix pass judges instead that the
item has no ground and goes, that is a change of the frame. It then owes
*Scope* item 3's first bullet group, *Data & interfaces*
(`frame/design.md:69`), S2's expected search output, the skill's
frontmatter and the changelog sentence, and this snippet does not apply.

The search above printed `changelog.md:3`, `frame/design.md:18`, `:32`,
`:57`, `:60`, `:86`, `frame/plan.md:36`, `:39` and `frame/questions.md:7`.
Of those, `:60`, `:86`, `plan.md:36`, `plan.md:39` and `questions.md:7` are
true as they stand. The snippet covers the other four. A search on these
words is a sample, so a statement of the same claim in other words can
escape it.

```markdown
frame/design.md:18, G10, after the sentence ending "is what shipped a PR with no prefix":
commit-pr-convention's item on the prose and structure of a PR body or review comment is in `716d8548` too and carries no confusion of its own: it is the receiving side of that handoff, naming `writing-style` for the part of a pull request that skill holds.

frame/design.md:32:
3. **A `NOT for:` clause stays only where G10 records the confusion it names, or where G10 names it as the receiving side of such a clause.**

frame/design.md:57, S2's first cell:
S2 A `NOT for:` clause stays only where G10 grounds it

changelog.md:3, its last sentence:
`code-review` and `writing-style` each keep the one item a recorded confusion asked for: a typed `/code-review` runs Claude Code's built-in command, and the format of a commit, a PR title or a branch belongs to `commit-pr-convention`. `commit-pr-convention` keeps the other side of that last boundary: the prose of a PR body belongs to `writing-style`.
```

### 2. The prefix's grounds say every skill keeps when a session reaches it, which the work item's own records hold unverified

```iadd
severity: should
location: `agentory/threads/1795841829-skill-descriptions/frame/plan.md:97`, `agentory/threads/1795841829-skill-descriptions/pr.md:6`
evidence: executed `git grep -n -F 'when a session reaches it' c2388b71 -- .`, `git grep -n -F 'choose a skill differently' c2388b71 -- .`; read `agentory/threads/1795841829-skill-descriptions/frame/plan.md:25`, `agentory/threads/1795841829-skill-descriptions/frame/plan.md:85`, `agentory/threads/1795841829-skill-descriptions/gaps.md:8-9`
```

Why it matters: the row of *Judgments of the run* that gives the title its
`perf:` grounds the prefix on "Every skill keeps what it does and when a
session reaches it" (`frame/plan.md:97`), and `pr.md:6` quotes that
sentence above the fold, where the owner reads it before merging. The same
plan says otherwise. *Operational impact* says "A session may choose a
skill differently for a request a removed item named" (`frame/plan.md:85`).
*Technical context* names two requests that a removed clause turned away
and that `implement` or `verify` may now claim (`frame/plan.md:25`).
`gaps.md:8-9` hands both questions to the repository owner as unverified.
The grounds state as settled the one behaviour the work item itself cannot
show, so the reader of the body meets the claim with no sign that it is
open. Claimed: every skill keeps when a session reaches it. Found:
`skills/implement/SKILL.md:6-8` and `skills/verify/SKILL.md:7-8` keep their
`Use when:` lines and lost the `NOT for:` lines that bounded them, and
`skills/core/SKILL.md:3-6` and `skills/agent-contract/SKILL.md:3-4` lost
their `Use when:` lines.

The search printed `frame/plan.md:97` and `pr.md:6` alone. A search on
these words is a sample. The snippet keeps the `perf:` verdict, which is
the orchestrator's judgment, and states its grounds as the records hold
them. A quote of `pr.md` must stand in the row word for word, so the two
files change together.

```markdown
frame/plan.md:97, the Grounds cell:
Every skill keeps the opening sentence that says what it does. `code-review`, `commit-pr-convention`, `implement`, `legacy-parity`, `settle`, `verify` and `writing-style` keep the `Use when:` line that says when a session reaches them, and `core` and `agent-contract` still reach every agent preloaded. Every session pays fewer characters of skill descriptions on every turn, and no case or rule changes what a party does. Whether a request that a removed `NOT for:` item named now reaches another skill is unverified, and `gaps.md` hands it to the repository owner.

pr.md:6, replaced by these four quote lines:
- "Every skill keeps the opening sentence that says what it does." (`frame/plan.md` *Judgments of the run*)
- "`code-review`, `commit-pr-convention`, `implement`, `legacy-parity`, `settle`, `verify` and `writing-style` keep the `Use when:` line that says when a session reaches them, and `core` and `agent-contract` still reach every agent preloaded." (`frame/plan.md` *Judgments of the run*)
- "Every session pays fewer characters of skill descriptions on every turn, and no case or rule changes what a party does." (`frame/plan.md` *Judgments of the run*)
- "Whether a request that a removed `NOT for:` item named now reaches another skill is unverified, and `gaps.md` hands it to the repository owner." (`frame/plan.md` *Judgments of the run*)
```

## Confirmations

What matched: *Scope* item 2. `skills/core/SKILL.md:3-6` and
`skills/agent-contract/SKILL.md:3-4` each hold two sentences that say what
the file holds and that every agent receives it preloaded, the core's
naming the `SessionStart` hook as well, and each keeps `user-invocable:
false`. S3's search printed nothing and exited 1 (executed). The removal of
both triggers was weighed against G1 and G11: the orchestrator opens the
contract by its path (`skills/implement/orchestration.md:31`, read), so no
session depends on choosing either skill from its description.

What matched: *Scope* item 3's list. S2's search printed one line each in
`skills/code-review/SKILL.md:9`, `skills/commit-pr-convention/SKILL.md:10`
and `skills/writing-style/SKILL.md:12`, each opening `NOT for:`, and no
other (executed). Each kept line holds the one item *Scope* item 3 names.
The `Use when:` lines and opening sentences of the seven skills are
unchanged (read, `git diff origin/release/v0.41.0..c2388b71 -- skills`).
Each removed clause was weighed against G10. `git log --reverse -S` on a
phrase of each removed clause named the commit G10 names, and each
message, read for `f15b3f99`, `c6b90bad` and `438cffe4`, records no
confusion (executed). One coordinate differs from G10: legacy-parity's
clause stands in `716d8548` and was reworded in `5aed51cb`, the commit G10
names. G10's conclusion is the same either way.

What matched: S1 and *Scope* item 5. M1, as `frame/plan.md:11-19` gives it,
printed the figures `trail/phases/phase-1.md:30-40` quotes, total 3386, at
`c2388b71` (executed). The changelog's "4,860 characters in 0.40.1" holds
because the base's skills equal the tag's (executed, above).

What matched: *Scope* item 1 and Q1. The crafter's counts in
`docs/experiments/2026-11-28-disable-model-invocation-blocks-preload.md:98-101`
were counted again over the two subagent transcripts under
`/Users/x/.claude/projects/` for the sessions the record names. `grep -c`
printed 3 and 3 for the sentinels and 3 and 2 for the body phrases in the
flag-off run, and 0 for all four in the flag-on run (executed). Each
session's transcript holds the prompt the record quotes and no `agentic:`.
The flag-off agent's skills were delivered from the `flag-off/` clone, and
both transcripts carry version `2.1.332` (executed). The two clones'
working trees hold the four edits the record's *Method* lists, and the
flag line only in `flag-on/` (executed, `git -C <clone> diff`). The costs
match each run's JSON output (read). The record's sections are the five
`docs/experiments/README.md` gives, in that order.

What matched: *Scope* item 4. The new case at
`tests/behaviour/test_chain_hooks_hardening.py:385-401` fails on the
intersection of `#skill_groups`' preloaded and user-invoked sets, so the
flag on either preloaded skill names it (read). Phase 1's red runs, the
contract rule 15 claim, are consistent with that reading and were not run
again. The removed case and the removed assertion with its comment are
gone, and the module docstring of
`tests/text/test_the_agent_contract_holds_the_universal_rules.py:39-47`
cites the documentation and the new record (read). The new case covers
what no other case of its group covers: the readme cases that read
`#skill_groups` assert membership, not the flag (read, `:414-425`,
`:495-544`).

What matched: the narrow modules the plan's *Phases* row names, with the
line-wrap, cited-commit and every-agent modules, passed at `c2388b71`,
166 cases (executed). This is no broad run. `gaps.md:7` labels the broad
gate unverified and names the orchestrator as its answerer, and that label
is honest.

What matched: the version move. `.claude-plugin/plugin.json:4` reads
`0.41.0`, the branch's upstream is `origin/release/v0.41.0`, and no file
outside the records and `docs/experiments/` holds `0.40.1` (executed).

What matched: `pr.md`. `agentic pr-body` composed the body from the work
item at `c2388b71` and refused no quote (executed). Each quote stands at
the coordinate it names (read). Finding 2 is about what one quoted sentence
says, not about its quoting.

What matched: the axis *Record against another work item's frame*. The
frames of #1655 and #1659 name no skill's description, frontmatter or
`NOT for:` clause. #1659's design names `agents/framer.md`'s description,
which this work leaves alone (executed, `grep` over each worktree's
`frame/design.md`).

A gap with no finding: the new case reads the flag as the one spelling
`disable-model-invocation: true` and a definition's `skills:` list as the
block form `^  - `, through `#skill_groups`
(`tests/behaviour/test_chain_hooks_hardening.py:360-382`). A flag spelt
`True`, or a definition written with the flow form
`skills: [core, agent-contract]` that `payload_meter.py#frontmatter` reads,
escapes it. The frame chose `#skill_groups` (*Scope* item 4, A10), and the
assertion the case replaced read the same spelling, so no behaviour lost a
case.

A gap with no finding: the docstring citation of the new case at
`tests/text/test_the_agent_contract_holds_the_universal_rules.py:45-46` is
split across two backticked spans, `path` then `#name`, so
`tests/behaviour/test_a_cited_section_stands_in_its_file.py#NAME_TOKEN`
does not read it, and a later rename of the case would leave it dangling
with the suite green.

A gap with no finding: the name of
`#test_the_contract_is_a_skill_that_preloads_and_is_not_a_command` still
says the case holds the preload, which it no longer asserts. The phase
record states the choice (`trail/phases/phase-1.md:45`), and the module
docstring names the case that holds it now.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether Claude Code's skills documentation still reads as G7 quotes it. The page was not fetched again. The measured run settles the behaviour the build rests on | `agentory/threads/1795841829-skill-descriptions/frame/design.md:15` | the orchestrator |
| Whether a plain review request still invokes `agentic:code-review`, and whether a request a removed `NOT for:` item named now loads `implement` or `verify`. No case runs the model's choice of a skill | `agentory/threads/1795841829-skill-descriptions/gaps.md:8-9` | the repository owner |
| The broad gate over the branch | `agentory/threads/1795841829-skill-descriptions/gaps.md:7` | the orchestrator, at the broad run |

## Probes

| Command | Result |
|---|---|
| M1 from `frame/plan.md:11-19`, run in the round's clone at `c2388b71` | nine figures and `total 3386` |
| `git grep -n 'NOT for' -- 'skills/*/SKILL.md'` and `git grep -n -E 'Use when\|NOT for\|disable-model-invocation' -- skills/core/SKILL.md skills/agent-contract/SKILL.md` | three lines, then nothing with exit 1 |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/lib/test_core.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_every_agent_reads_the_contract.py -q` | exit 0, 166 passed |
| `bin/agentic pr-body --body <scratch>/body.md agentory/threads/1795841829-skill-descriptions` | exit 0, the body written with every quote accepted |
| `grep -c` of each sentinel and each body phrase over each run's `subagents/agent-*.jsonl` | flag-off 3, 3, 3, 2; flag-on 0, 0, 0, 0 |
