# Review round 1: 1794362365-the-definitions-restate-the-contract

```seal
target: f483b4631 against release/v0.37.3
```

The branch was read against `release/v0.37.3` at `9c6907942` over its eleven
commits, `9c6907942..f483b4631`. This is the first round, so no coordinate
or verdict was carried from an earlier one, and every fact below was
established here. `seal/parity.json` is not declared, so no parity
comparison was owed. The work item's records were each read whole at
`f483b4631`: `routing.md`, the three frame files, `gaps.md`, `changelog.md`,
`pr.md` and `trail/phases/phase-1.md`. No `pr.<lang>.md` stands, and
`seal/config.json` names English for both language keys, so none is owed.

The diff was read against both issues as `frame/design.md` G21 quotes their
*Done when*, and against the tree's texts at HEAD. The reviewer's own
definition is the installed 0.37.2 copy, and the rules under review are the
tree's.

## Findings

### 1. The tracer is still told that its probe leaves nothing behind

```seal
severity: must
location: `agents/tracer.md:65-67`, `tests/behaviour/test_a_probe_that_commits_says_so.py:9`, `tests/behaviour/test_a_probe_that_commits_says_so.py:70-81`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:60`
evidence: read `agents/tracer.md:65-67`, `skills/agent-contract/SKILL.md:87-99`, `skills/agent-contract/SKILL.md:183-197`, `tests/behaviour/test_a_probe_that_commits_says_so.py:1-81`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:60`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:82`, `seal/threads/1794362365-the-definitions-restate-the-contract/trail/phases/phase-1.md:75`
```

Why it matters: #1503's *Done when* asks that no text under `agents/` tell
an agent to remove its scratch directory or the files in it, and
`frame/design.md` S5 states it (`:82`). `agents/tracer.md:65-67` still says
"a probe you do run leaves nothing behind (rule 7)". Those are the words of
rule 7 as it stood at `9c6907942`, "A probe leaves nothing behind, whatever
kind of thing it made". Rule 7 at HEAD says the reverse for what sits in
scratch: "What stands under your scratch directory (rule 17) stays there:
the probe file, a clone, a virtual environment inside one"
(`skills/agent-contract/SKILL.md:90-92`). Rule 17 gives the tracer the leaf
`tracer` and says "Nobody removes the scratchpad, a scratch directory or a
file in one" (`:187`, `:192-193`). So a tracer that follows its own
definition removes its probe from its scratch directory, which is the act
#1503 removes.

The frame decided the opposite: *Scope* item 17 says "the tracer's
citation of rule 7 holds under T1" (`frame/design.md:60`). That is a
sentence of what the work concludes, and the target contradicts it,
because T1 replaced the very words the tracer repeats. The crafter's
sample saw the line and kept it on that item (claimed
`trail/phases/phase-1.md:75`, "`frame/design.md` *Scope* item 17 keeps
it"; `agents/tracer.md:66-67` states the retired wording). G8's search
missed it because "leaves" and "nothing" fall on two lines.

The case `test_the_fact_finder_points_a_probe_at_rule_7` pins the stale
words, "leaves nothing behind (rule 7)" (`:78`), and the module's
docstring paraphrases rule 7 the same way (`:9`). Both change with the
sentence, in one commit.

The fix pass owes the definition and the case. The frame lines are the
orchestrator's to fold: *Scope* item 17 then says the tracer takes T1's
words, and S11's list of files gains `agents/tracer.md` and the test module.

```markdown
agents/tracer.md, lines 65-67:
**Constraints, enums and defaults are read, not probed.** An original settles
most of what you are asked by reading, and a probe you do run leaves
nothing outside your scratch directory (rule 7).
```

```python
# tests/behaviour/test_a_probe_that_commits_says_so.py, docstring, line 9:
# "retired. What stays is rule 7's: a probe leaves nothing outside the
# agent's scratch directory, and its"

def test_the_fact_finder_points_a_probe_at_rule_7():
    """`agents/tracer.md` once carried the three shapes verbatim, then a
    pointer at rule 8. Its rule *Constraints, enums and defaults are read,
    not probed* says what reading settles for an original, which the
    orchestrator reads in the tracer's report, and points at rule 7 for a
    probe it does run."""
    tracer = " ".join(read("agents", "tracer.md").split())
    # The citation `(rule 7)`, which the tracer resolves for what a probe it
    # runs may leave, and where.
    assert "outside your scratch directory (rule 7)" in tracer, (
        "the fact-finder can no longer reach the rule for a probe it runs"
    )
```

### 2. Contract rules 7 and 17 each give the removal a second reading

```seal
severity: should
location: `skills/agent-contract/SKILL.md:95-97`, `skills/agent-contract/SKILL.md:183`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:102`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:104`
evidence: read `skills/agent-contract/SKILL.md:87-99`, `skills/agent-contract/SKILL.md:183-197`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:96-106`
```

Why it matters: rule 7 now holds two statements of what goes. Its third
sentence keeps "What stands under your scratch directory (rule 17)", and
names "a clone, a virtual environment inside one" (`:90-92`). Its sixth
sentence, kept from the old rule, says without scope "What the probe made
for ITSELF is what goes" (`:95-96`). A clone or a virtual environment that a
probe made for itself inside the scratch directory is both. One reading
keeps it, and the other has the agent remove it, which is the act #1503
removes. The sentence was written when rule 7 had no place that stays, and
`frame/design.md:102` kept it unchanged ("its last two sentences ... stay").

Rule 17's heading has the opposite problem. It says "remove nothing"
(`:183`), with no object, while rule 7 says everything a probe made outside
the scratch directory "is gone before you hand over", the probe file in a
working tree first among them (`:93-94`, and S8 at `frame/design.md:85`).
The body of rule 17 scopes the ban to "the scratchpad, a scratch directory
or a file in one" (`:192-193`), but the heading is the line an agent scans
first. The heading comes from T2 (`frame/design.md:104`).

Both readings go once each sentence names its scope. The heading stays
under the 88 columns `tests/behaviour/test_docs_line_wrap.py` holds (it is
78). No case pins either sentence: the scratch module reads rule 17 by the
prefix `17 `. The contract grows by about 30 B, inside S9's bound of
12,864 B. T1 and T2 in the frame are the orchestrator's to fold.

```markdown
skills/agent-contract/SKILL.md, rule 7, in place of "What the probe
made for ITSELF is what goes:":
Outside your scratch directory, what the probe made for ITSELF is what
goes:

skills/agent-contract/SKILL.md:183:
## 17 Name your scratch for the work item, keep it, stop only what you started
```

### 3. The plan and the pull request body say the contract costs three agents bytes, and it costs four

```seal
severity: should
location: `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:29`, `seal/threads/1794362365-the-definitions-restate-the-contract/pr.md:2`
evidence: executed `git show <c>:<f> | wc -c` for the four definitions, the contract and the core at `9c6907942` and `f483b4631`; read `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:21`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:29`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:62`, `seal/threads/1794362365-the-definitions-restate-the-contract/pr.md:2`
```

Why it matters: *Alternatives considered* row 2 says the premise for
keeping each definition's own scratch statement, that it costs fewer
preloaded bytes, holds "for a framer, a proofer and a tracer"
(`frame/plan.md:29`). `pr.md:2` quotes that sentence into the pull request
body, where a person reads it as the reason the design was chosen. The
sealer's preload grows too. `wc -c` gives the core 9,322 B, the contract
12,364 B and 12,779 B, and the sealer 11,454 B and 11,058 B, so a sealer
preloads 33,140 B before and 33,159 B after, 19 B more. The same plan says
so twice: *Technical context* names "a framer, a proofer, a sealer and a
tracer" (`:21`), and *Operational impact* gives "a sealer 33,159 B, 19 B
more" (`:62`). The row has omitted the sealer since the frame was written;
the fold at `d41f74c9c` changed only its figure, from 455 B to 415 B.

Both lines are the orchestrator's: the plan row is the frame's, and `pr.md`
is the orchestrator's. The quote must match the row word for word after the
fix.

```markdown
frame/plan.md, row 2, in place of "Checked: it does for a framer, a
proofer and a tracer, by the 415 B of `frame/design.md` G17, and the
crafter's preload falls by more than that.":
Checked: it does for a framer, a proofer, a sealer and a tracer, whose
preloads grow by 19 B to 415 B as the contract grows by the 415 B of
`frame/design.md` G17, and the crafter's preload falls by 781 B
(*Operational impact*).

pr.md, line 2: the same sentence in place of the old one inside the quote.
```

```seal
verdict: fixed 3ad1c31fa
answer: The finding holds. The framer folded it into frame/plan.md Alternatives considered row 2, which now names a framer, a proofer, a sealer and a tracer as the agents whose preloads grow and cites Operational impact for each figure rather than restating one, so the row does not go stale when the fix pass moves the contract's bytes. The orchestrator requoted the row word for word into pr.md at e4e6158ed. The fix touched this work item's records alone.
```

### 4. The round-record form will still say a round's probe was deleted, and no rule change rewrites it

```seal
severity: should
location: `docs/forms/the-round-record.md:50-51`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:212-218`
evidence: executed `git grep -n -i -E 'probe.{0,80}(delet|remov|gone|goes)|(delet|remov).{0,40}probe' -- agents skills docs templates ':!*.py'`; read `docs/forms/the-round-record.md:48-53`, `skills/agent-contract/SKILL.md:89-94`, `agents/proofer.md:86-90`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:212-218`
```

Why it matters: `docs/forms/the-round-record.md:50-51` says "A probe the
line names was deleted under the agent contract's probe rule, so the round
writes it again from its `## Probes` row." Under rule 7 at HEAD, a
proofer's probe that ran in its own clone stands under
`<scratchpad>/<work-item-id>/round-<n>/`, and it stays there
(`skills/agent-contract/SKILL.md:90-92`, `agents/proofer.md:86-90`). Only a
probe in a working tree the prompt named is still deleted. The form is a
policy document, so it changes through `## Rule changes` at the settle, as
the one operation on `docs/running/the-agent-set.md` does
(`frame/design.md:212-218`). No operation names this sentence, so the
settle leaves it stating the old rule. The action it gives stays right: a
later round writes the probe again in its own directory. Its reason does
not. No case pins the sentence (`git grep -n -F "was deleted" -- tests`
prints no line on it).

The operation is the frame's, for the orchestrator to fold.

```markdown
- change
  file: docs/forms/the-round-record.md
  section: The round record
  from: A probe the line names was deleted under the agent contract's probe rule, so the round writes it again from its `## Probes` row.
  to: A probe the line names stands in the earlier round's scratch directory, or was deleted from a working tree under the agent contract's probe rule, so the round writes it again from its `## Probes` row.
```

```seal
verdict: fixed 3ad1c31fa
answer: The finding holds. The framer added the change operation on docs/forms/the-round-record.md The round record to frame/design.md Rule changes as the finding gives it, from and to unchanged, so the settle rewrites the sentence's reason and keeps its action. The form has no Korean copy, so one operation covers it. The fix touched this work item's records alone.
```

## Confirmations

What matched: S1. Claimed 46,860 B for the four definitions
(`trail/phases/phase-1.md:42`); `wc -c` at `f483b4631` gives
`agents/crafter.md` 10,215 B, `agents/framer.md` 14,824 B,
`agents/proofer.md` 10,763 B and `agents/sealer.md` 11,058 B, 46,860 B,
against 48,810 B at `9c6907942`. That is 1,950 B less, inside the bound of
47,310 B (executed).

What matched: S9. Claimed 12,779 B for the contract; `wc -c` gives 12,779 B
at `f483b4631` and 12,364 B at `9c6907942`, inside the bound of 12,864 B
(executed).

What matched: S2. Claimed the census reads 916 of 11,778 at `9c6907942` and
865 of 11,553 at the last code commit (`trail/phases/phase-1.md:56-67`). A
probe written here to #1320's D6, as the phase record describes it, read
every cell of both columns the same, at `9c6907942` and at `f483b4631`
(executed; see *Probes*). The `changelog.md:5` figures match.

What matched: S3. `git grep -n 'read. or .unverified' -- agents` prints
nothing and exits 1 (executed). Each of T4 to T21 stands in its file as the
frame gives it, apart from the two headings of departure 1 (read).

What matched: S4. `git grep -n -i 'share one scratchpad' -- agents skills`
prints `skills/agent-contract/SKILL.md:189` alone (executed). The crafter
claimed `skills/verify/SKILL.md:283-285` contradicts S4, and the
orchestrator judged S4 true as worded. Read here: S4's Given is the contract
and the definitions, and that skill is neither, so S4 holds.

What matched: S11. `git diff --stat 9c6907942...HEAD -- ':!seal/'` lists ten
files, the ones *Scope* items 1 to 12 name (executed).

What matched: departure 1. Claimed T1's and T2's headings exceed the line
limit. Both built headings measure 85 columns, under the 88 the wrap case
holds (executed), and `tests/behaviour/test_docs_line_wrap.py` passes.

What matched: departure 2. Claimed the old proofer clause stayed green with
its sentence deleted, because the clone's path begins with the round's
directory. Read: `<scratchpad>/<work-item-id>/round-<n>/` is a prefix of
`<scratchpad>/<work-item-id>/round-<n>/clone`, so the plain substring test
could not fail. The backticked form at
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:86`
matches only the directory sentence at `agents/proofer.md:88`.

What matched: the new cases against their group. The module holds the
cases on each definition's directory; no other module reads rule 17 or an
`rm -rf` in the contract (executed: `git grep` over `tests` for
`share one scratchpad`, `<leaf>` and `rm -rf`). So
`test_rule_17_names_the_scratch_directory_for_the_work_item` and
`test_no_contract_section_or_definition_writes_a_removal` each cover what
nothing else does. The shown-red claims of `trail/phases/phase-1.md:24-34`
were read against each assertion, and each assertion fails when its
sentence goes (read; not re-run).

What matched: the narrow modules. The scratch module,
`tests/text/test_a_moved_rule_leaves_its_definition.py`,
`tests/behaviour/test_a_probe_that_commits_says_so.py`,
`tests/text/test_broad_gate_rule.py`,
`tests/behaviour/test_docs_line_wrap.py` and
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` pass at
`f483b4631` (executed).

What matched: `pr.md`. Quotes 1, 3, 4, 5 and 6 stand word for word at the
coordinates they name, in `frame/plan.md` rows 1, 8 and 5 of
*Alternatives considered* and the two rows of *Judgments of the run*
(read). Quote 2 matches its row too, and finding 3 is on the row.

What matched: the `## Rule changes` `from`. Its sentence stands word for
word, with whitespace collapsed, in `docs/running/the-agent-set.md:134-143`
(executed).

What matched: the copies of rules 2 to 5. Each sentence G5, G6, G11 and G12
name now cites the rule or keeps only that agent's narrowing:
`agents/crafter.md:66-73`, `:86`, `:106-109`, `:155-156`;
`agents/proofer.md:94-96`, `:167-170`; `agents/sealer.md:133-134`,
`:144-146`; `agents/framer.md:149-151` (read). Each fact a removed crafter
rule held stands where its *Removes* row says: step 4 at
`agents/crafter.md:40-43`, the record's contents at
`skills/implement/SKILL.md:310-315`, and the chain's end at `README.md:307`
and contract rule 6 (read). No lead this work removed is cited anywhere
outside `seal/threads/` (executed: `git grep -n -F` on each lead).

Two gaps hold no finding. The pin "share one scratchpad"
(`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:139`)
holds the wording of rule 17's reason, which
`docs/running/what-a-script-gates.md` *The checks* does not keep a case for;
*Scope* item 11 asks for it, so it holds a fact the frame states. The case
name `test_no_contract_section_or_definition_writes_a_removal` claims any
removal and pins `rm -rf` alone (`:149-160`), which is what *Scope* item 11
states.

Two statements stand and are outside this round's findings. The capture
example of `skills/verify/SKILL.md:277` writes to
`<scratchpad>/<work-item-id>/run.txt`, under no leaf, where rule 17 puts
every captured output under the agent's own leaf. The crafter's and the
framer's definitions said the same before this work, so the change did not
make the gap, and the frame put that file *Out*. `README.md:377-378` says
both the directory and the scratchpad "last as long as the scratchpad
does", which reads badly and says nothing false.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD. The phase record and `gaps.md:7` label it `unverified` for the orchestrator, and that label is honest | `seal/threads/1794362365-the-definitions-restate-the-contract/gaps.md:7` | the orchestrator, by `seal gate --record` |
| Whether Claude Code clears a session's scratchpad, and how large it grows now that nothing is removed | `seal/threads/1794362365-the-definitions-restate-the-contract/frame/questions.md:19` | a measurement, as Q1 states |
| Whether agents under the released text still write an `rm`, and take `-2` where their directory stands | `seal/threads/1794362365-the-definitions-restate-the-contract/frame/questions.md:20` | a measurement, as Q2 states |
| The crafter's eval cases, whose `shape-no-probe-left` graders read fixture files only, so a probe under scratch is outside them (read) | `evals/behaviour/crafter/rule-crafter-count-words/graders/shape-no-probe-left.md` | the owner, where the release runs them |
| The shown-red runs of `trail/phases/phase-1.md:24-34`, read here and not re-run | `seal/threads/1794362365-the-definitions-restate-the-contract/trail/phases/phase-1.md:22-34` | the sealer, in its sample |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_census.py <repo> 9c6907942 f483b4631`, the ten-word census written to #1320's D6 as `trail/phases/phase-1.md:56` describes it, run once from `<scratchpad>/1794362365-the-definitions-restate-the-contract/round-1/` | At `9c6907942`: crafter 274 of 1775, framer 140 of 2391, proofer 151 of 1733, sealer 102 of 1794, tracer 26 of 442, contract 90 of 2048, core 133 of 1595, all 916 of 11778. At `f483b4631`: 254 of 1592, 140 of 2369, 141 of 1695, 81 of 1727, 26 of 442, 90 of 2133, 133 of 1595, all 865 of 11553 |
| `bin/test` over the six modules named under *Confirmations*, `-q`, one command | exit 0 |
