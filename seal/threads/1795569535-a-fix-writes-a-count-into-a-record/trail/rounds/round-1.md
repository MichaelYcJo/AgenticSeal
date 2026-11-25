# Review round 1: 1795569535-a-fix-writes-a-count-into-a-record

```seal
target: 619aeee95 against origin/release/v0.39.0
```

The range is `fd89e2114..619aeee95`, read in a `git clone --no-local` checked out at `619aeee95`. No earlier round exists, so nothing was carried: every fact below was opened this round. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/mechanism-inventory.md`. No `pr.<lang>.md` stands, and `seal/config.json` sets `Commit and pull request language` to English, so none is owed. No `seal/parity.json` is declared.

The axes this change owns, beside the table's: whether each citing sentence reads one way, whether the removed paragraph left a statement or a citation behind, the rendered shape of the fragment's process row, and whether the frame's weighing of mechanisms stands on facts that hold. The issue bodies of #1613 and #1615 were read with `gh issue view`, and the hooks and subagents pages of the Claude Code reference that `trail/mechanism-inventory.md:3-4` names were read this round.

## Findings

### 1. The fragment's process row has three cells under a four-column header, so the release note shows the reason in the Change column and the link in the Why column

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/changelog.md:14`
evidence: executed `awk -F'|'` over `changelog.md:12-14` (header 4 cells, row 3 cells); read `.github/scripts/publish_release_note.py:298-345`, `templates/records/process.md:3`
```

Why it matters: `templates/records/process.md:3` gives four columns: Date, Change, Why and Source. The row at `changelog.md:14` has no cell boundary between "`agents/framer.md`'s count rule goes" and "In releases 0.0.2 to 0.0.4". So the Change cell holds the reason too, the Why cell holds the issue link, and the Source cell is empty. `publish_release_note.py#split_process` lifts each table line whole into the release note's one `### Process changes` table, so a person reading the published note meets the row in this shape. The boundary was lost in `935f8bf56`: at `7833f983f` the row had four cells, and the rewrite of its Why cell dropped the ` | ` before it. This confirms the orchestrator's first doubt.

```markdown
| 2026-11-25 | `skills/agent-contract/SKILL.md` rule 19: a change writes no count and no universal about the tree that a later change makes false, and names the members or cites the list instead; `skills/implement/fix-pass.md`, `skills/implement/fold-and-reframe.md`, `skills/implement/orchestration.md` step 1 and `skills/code-review/orchestration.md` cite it, and `agents/framer.md`'s count rule goes | In releases 0.0.2 to 0.0.4 of a repository that runs the chain, 14 of the 72 defects that commits after round 1 introduced were a count or a universal the next fix made false, and until 0.39.0 the rule against it bound the framer alone | https://github.com/MichaelYcJo/AgenticSeal/issues/1613 |
```

```seal
verdict: fixed 365e6a8b4
answer: The fix pass restored the ` | ` before the Why cell, so the header and the row each hold four cells (executed: `awk -F'|'` over `changelog.md:12-14` prints 4 for each line). The Why cell's wording is the one the finding quotes, and no other cell changed.
```

### 2. The `SubagentStop` agent-hook row rejects on the ground that the stop's input names nothing of what changed, and the hooks reference gives that input the subagent's own transcript

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:27`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/pr.md:2`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/trail/mechanism-inventory.md:30-33`
evidence: read the Claude Code hooks reference (`hooks.md`, the page `trail/mechanism-inventory.md:4` names), section *SubagentStop input*, and its matcher table; read `frame/plan.md:27`, `pr.md:2`
```

Why it matters: `frame/plan.md:27` says of a `SubagentStop` hook of type `agent` that "it still cannot read the range: an `agent` hook holds Read, Grep and Glob and no shell, and the stop's input names no commit range (`frame/design.md` G21, not probed), so it reads records whole without knowing what changed". The hooks reference, section *SubagentStop input*, states that the event receives `agent_transcript_path`, "the subagent's own transcript", beside `last_assistant_message`. That transcript holds each `Edit` and `Write` call the subagent made, with its `file_path` and its new text. So an `agent` hook can learn with Read alone what the stopping crafter or framer wrote. The ground "reads records whole without knowing what changed" does not hold. The row calls this mechanism the cheapest independent reader weighed, and its verdict partly rests on this false ground. Its other ground, that the independent reader is #1615's subject, may still stand. #1615's body does make the first independent reader of a fix its subject.

The same reading answers two lines the inventory calls unconfirmed (`trail/mechanism-inventory.md:32-33`). Plugin hooks "also run inside subagents". The `SubagentStop` matcher takes "plugin-scoped names like `^my-plugin:reviewer$`". The inventory's field list for subagent hooks omits `agent_transcript_path`.

`pr.md:2` quotes the row word for word into the pull request body, so the false ground reaches the reader of the pull request. This round read the reference; it did not probe the harness. Whether the hook then earns a phase here, or stays named to #1615, is the framer's judgment against the owner's direction at `frame/plan.md:60`, made in a fold once the ground is rewritten.

The fix rewrites the row's Failure scenario cell. It also rewrites its Verdict cell's probe sentence to the plugin-scoped name. Then `pr.md:2` is requoted from the cell as it stands after the fold, and `trail/mechanism-inventory.md:30-33` gains the field and loses the two "unconfirmed" claims the reference answers.

```markdown
| A `SubagentStop` hook matched on the crafter and the framer, of type `agent`, that reads the range of the stopping agent against rule 19 before the hand-back reaches the orchestrator | Once per hand-back it is the cheapest independent reader weighed here. The stop's input carries `agent_transcript_path`, the stopping subagent's own transcript, which holds each `Edit` and `Write` call with its path and new text (the hooks reference, *SubagentStop input*, read in round 1; not probed in this harness), so with Read, Grep and Glob it can read what the agent wrote and the text around it. It has no shell, so it reads no commit and runs no `git grep`. An independent reader of a fix's records before the next round is #1615's subject, so building one here decides #1615's question before its frame is drawn | rejected here; `frame/plan.md` *Overlap with the release* names it to #1615. Before any frame rests on it, a probe settles whether a plugin's `SubagentStop` matcher meets a plugin agent by the plugin-scoped name `agentic:crafter`, as the reference's matcher table states, and what `agent_transcript_path` holds in this harness |
```

```markdown
- `hooks/hooks.json` hooks run inside subagents too (hooks.md: "Hooks from settings files, managed policy settings, and plugins also run inside subagents"), and the input carries `agent_type` and `agent_id`. SubagentStart and SubagentStop match by agent name, a plugin agent by its plugin-scoped name such as `^agentic:crafter$`. SubagentStop also receives `agent_transcript_path`, the subagent's own transcript, and `last_assistant_message`.
```

```seal
verdict: fixed 9ad6fb578
answer: Answered by other parties, read by the fix pass at HEAD. The framer's fold at `9ad6fb578` rewrote the `SubagentStop` `agent` row of `frame/plan.md` *Alternatives considered*: it now gives the stop's input `agent_transcript_path` and the plugin-scoped matcher, weighs the hook again, and keeps it rejected here and named to #1615 on other grounds. The orchestrator's `5690aa090` corrected `trail/mechanism-inventory.md` with the reference's sentences on subagent hooks, the plugin-scoped name and `agent_transcript_path`. Its `8b7ef7b16` requoted `pr.md:2` from the cell as the fold left it, and `6cfaf525b` renamed that file's first coordinate.
```

### 3. G21 says each row that cites the inventory names it as not probed, and three rows of *Alternatives considered* rest on its lines without saying so

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/design.md:31`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:26`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:32`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:34`
evidence: read `frame/design.md:31`, each row of `frame/plan.md:24-34`, `trail/mechanism-inventory.md:37-67`
```

Why it matters: `frame/design.md:31` says "no row's verdict rests on a line of it alone: where a verdict cites one, the row names it as not probed". Each row of `frame/plan.md:24-34` was read for a fact that only the inventory gives. Rows 25 and 27 name G21 as not probed. Row 26 cites "(`frame/design.md` G21)" for "up to 50 turns and 60 s" and rests on "The type is experimental" without naming it as not probed. Row 32 cites G21 for the honoured fields and for "A plugin agent's `hooks` frontmatter is ignored", and does not name it as not probed. Row 34 rests on the inventory's monitor and output-style lines (`trail/mechanism-inventory.md:61-64`) and cites nothing. A reader who trusts G21's sentence takes rows 26, 32 and 34 as standing on the tree.

This round read the reference for rows 26 and 32. It states agent hooks are "experimental", have "up to 50 turns" and a 60-second default timeout. The subagents page states plugin subagents ignore `hooks`, `mcpServers` and `permissionMode`. So those rows' facts hold as read. Row 34's monitor and output-style lines were not read (`## Not judged`). The defect is the sentence's claim about the rows, and the fix is the marking.

The fix marks the three rows. In row 26, "(`frame/design.md` G21)" becomes:

```markdown
(`frame/design.md` G21, not probed; the hooks reference states each, read in round 1)
```

In row 32, "the rest `frame/design.md` G21 lists)" becomes "the rest `frame/design.md` G21 lists, not probed)". In row 34, the sentence on a monitor and an output style ends with "(`frame/design.md` G21, not probed)".

```seal
verdict: fixed 9ad6fb578
answer: Answered by the framer's fold at `9ad6fb578`, read by the fix pass at HEAD. G21 now says each line of the inventory is a claim and none was probed here. The `PostToolUse` `agent` row reads "(`frame/design.md` G21, not probed; the hooks reference states each, read in round 1)", the agent-definition row reads "the rest `frame/design.md` G21 lists, not probed", and the row on an MCP tool, a monitor or an output style ends "(`frame/design.md` G21, not probed)".
```

### 4. Two rows reject a hook because the writer's own read of its range already covers the defect, and the row beside them states that such self-reads did not prevent it

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:25`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:29`
evidence: read `frame/plan.md:25`, `frame/plan.md:28`, `frame/plan.md:29`, `frame/plan.md:60`; executed `gh issue view 1613 --json body` and `gh issue view 1615 --json body`
```

Why it matters: the owner's direction, as `frame/plan.md:60` records it, has the frame add a mechanism as a phase where it "catches the defect at the act at less cost than a round spends on it". So each rejecting row needs a ground that stands. Row 25, the `PostToolUse` `prompt` hook, ends "Its catch record is none, and the crafter already reads its range whole before it hands back". Row 29, the `seal` subcommand, ends "which its whole-range read already covers". Row 28 rejects a different hook because "#1615's evidence is that such self-reread rules stood and did not prevent the fix-made defects". #1615's body says so: "They did not prevent the fix-made defects, because the first independent reader of a fix is still the next round". So rows 25 and 29 lean on the self-read that row 28, and the issue it cites, say fails. "Its catch record is none" is no ground either. A mechanism not yet built has no record, and `skills/core/SKILL.md` *The rule a mechanism is kept against* weighs a record against cost for a mechanism that exists. For a proposed one, the expected catch is what the issue measured.

This answers the orchestrator's second doubt in part. Rows 24, 26, 28, 30, 31, 32 and 33 hold on grounds this round found standing; row 34 is under `## Not judged`. Rows 25 and 29 keep other grounds. The reference confirms row 25's single-turn reading of `$ARGUMENTS`, the 30-second default and the background model. Row 29 rests on a word list, which the core keeps out of scripts. So their verdicts may stand, but on those grounds and a cost comparison, not on the self-read. Row 26 already holds the comparison these two rows lack: "at one round per missed sentence, and the issue counts those sentences at fewer than one per work item". The issue gives 14 such sentences over 28 work items.

In row 25, "Its catch record is none, and the crafter already reads its range whole before it hands back" becomes:

```markdown
The defect it would catch is the one a round catches, at one round per missed sentence, which the issue counts at fewer than one per work item, while its reasons reach the writer at every matching call
```

In row 29, "which its whole-range read already covers" becomes:

```markdown
at a cost the issue's count of fewer than one such sentence per work item does not repay
```

```seal
verdict: fixed 9ad6fb578
answer: Answered by the framer's fold at `9ad6fb578`, read by the fix pass at HEAD. The `PostToolUse` `prompt` row ends with the round's first snippet in place of "Its catch record is none, and the crafter already reads its range whole before it hands back", and the `seal` subcommand row ends with the second snippet in place of "which its whole-range read already covers". Both rows keep the verdict `rejected` on the grounds left standing.
```

### 5. The records send the issue's second *Done when* line to a `seal/follow-up.md` row that the target does not hold, while the pull request body closes the issue

```seal
severity: should
location: `seal/follow-up.md`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/routing.md:22`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/gaps.md:8`
evidence: executed `git grep -n 1613 -- seal/follow-up.md` (exit 1, no line); read `routing.md:22`, `frame/questions.md:14`, `gaps.md:8`, `pr.md:3`, `pr.md:5`, `seal/follow-up.md` whole
```

Why it matters: `routing.md:22` says the second *Done when* line "goes to `seal/follow-up.md` with the owner as its answerer". `frame/questions.md:14` has the orchestrator write that row. `gaps.md:8` names "the `seal/follow-up.md` row the orchestrator writes" as the answerer's channel. `pr.md:3` quotes the default into the pull request body, and `pr.md:5` closes #1613. At `619aeee95`, `seal/follow-up.md` holds the two #1576 rows and none for #1613. If the pull request merges as it stands, the issue closes and its second *Done when* line has no home. The row is the orchestrator's to write before the sealer's spawn. `seal/follow-up.md` itself says a repository with a tracker "should normally hold none" of its schedulable items. Its two standing rows name the owner the same way, so the routing decision has precedent. The fix is the row.

```markdown
| Whether the next release's classification of a repository that runs the chain counts fewer fix-made findings on a count or a universal than the 14 of 72 that #1613 measured in releases 0.0.2 to 0.0.4. As many or more sends contract rule 19's clauses on what a change writes to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against* | the repository owner |
```

```seal
verdict: fixed 4d3d6ad86
answer: Answered by the orchestrator's `4d3d6ad86`, read by the fix pass at HEAD: `seal/follow-up.md:44` holds #1613's row on the issue's second *Done when* line, with the repository owner as its answerer. The fix pass's `0659cbb8a` has `gaps.md` name that row as it stands, in place of "the `seal/follow-up.md` row the orchestrator writes".
```

### 6. The `## Rule changes` passage writes the release's history into a policy section

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/design.md:107-111`
evidence: read `frame/design.md:98-114`, `skills/core/SKILL.md` *The rule a mechanism is kept against*, `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*
```

Why it matters: the settle writes the `to:` text into `docs/running/the-agent-set.md`, which agents read as policy. `frame/design.md:107-109` holds "Until 0.39.0 the rule stood in `agents/framer.md` for the frame's counts alone, so it bound the framer and no other party that edits a record". That is history. `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history to "git, the release notes and the work record". The release note already carries it, at `changelog.md:5`. The section's other paragraphs state rules and their reasons and no history, the rule 21 paragraph G12 names as precedent among them. The measurement sentence before it is the rule's reason, dated, and may stay. The fix drops the history sentence and lets the next sentence open the claim.

```markdown
    orchestrator's record edits (#1613). The rule binds every agent
    through the contract, and the orchestrator opens it at step 1 of
    `skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*. Whether a sentence states what the tree holds or a rule that
    must hold is the reader's judgment, so no script reads for one.
```

Finding 7 changes the attribution in the line this snippet opens with. Where both are applied, the first snippet line follows finding 7's wording.

```seal
verdict: fixed 9ad6fb578
answer: Answered by the framer's fold at `9ad6fb578`, read by the fix pass at HEAD. The `to:` of `frame/design.md` `## Rule changes` no longer holds the sentence on where the rule stood until 0.39.0; the sentence opening "The rule binds every agent through the contract" follows the measurement, which ends "were such a sentence (#1613)." as finding 7 asks.
```

### 7. The fragment and the `## Rule changes` passage credit the 14 count sentences to three parties, and the issue gives that split for none of them

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/changelog.md:3`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/design.md:104-107`
evidence: executed `gh issue view 1613 -R MichaelYcJo/AgenticSeal --json body`; read `changelog.md:3`, `frame/design.md:104-107`
```

Why it matters: `changelog.md:3` says the 14 defects "were such a sentence, written by the crafter's fix pass, the framer's fold and the orchestrator's record edits". `frame/design.md:104-107` says the same. The issue body gives the parties for all 72 fix-made defects: the fix pass 44, the orchestrator's record edits 13, the folds 10, merges 4, a CI fix 1. It gives no split for the 14. Its opening attributes them to "a fix pass or a fold". The three parties come from the issue's *Proposed*, which names who the rule should bind, not who wrote the 14. The release note and, after the settle, the policy section would state a breakdown no source holds. The fix ends the measurement at the count, in both places.

```markdown
In releases 0.0.2 to 0.0.4 of a repository that runs the chain, 14 of the 72 defects a commit after round 1 introduced were such a sentence (#1613).
```

In `changelog.md:3` the "(#1613)" is left out, since the item's heading carries it. In `frame/design.md:104-107` the `to:` keeps its indented wrap, and its sentence then ends "were such a sentence (#1613)." with the clause "written by the crafter's fix pass, the framer's fold and the orchestrator's record edits" gone.

```seal
verdict: fixed 365e6a8b4
answer: The fix pass ended `changelog.md:3`'s measurement at the count, "14 of the 72 defects a commit after round 1 introduced were such a sentence.", with the clause naming the crafter's fix pass, the framer's fold and the orchestrator's record edits gone and no "(#1613)", since the item's heading carries it. The framer's fold at `9ad6fb578` made the same cut in `frame/design.md` `## Rule changes`. A search of the work item's records outside `trail/rounds/` for the clause's words found no other copy.
```

## Confirmations

What matched: rule 19's new paragraph at `skills/agent-contract/SKILL.md:202-217` states clauses R1 to R6 of `frame/design.md:75-80` in order, as `trail/phases/phase-1.md:9` claims. R1 is its first three sentences, R2 "Such a sentence", R3 "In its place", R4 the two sentences on where a count stands and on an item's own number, R5 the two sentences on what stays, and R6 the last. This answers `gaps.md:9`, read.

What matched: each citing sentence reads one way. Read: `skills/implement/fix-pass.md:39-42`, `skills/implement/fold-and-reframe.md:23-24`, `skills/implement/orchestration.md:31-36` and `skills/code-review/orchestration.md:180-181`. The orchestrator's "folds of what a crafter names" agrees with `docs/running/the-agent-set.md`, where the orchestrator folds only the statements a crafter's hand-back names as contradicted by HEAD.

What matched: the new `RULES` row pins each link. Executed: the plan's narrow set with `tests/behaviour/test_docs_line_wrap.py` added, `bin/test -q -p no:xdist` over the plan's five files and the wrap test, exited 0 with 145 passed. Executed: `seal mutate` of `skills/code-review/orchestration.md` replacing `contract rule 19` with `contract rule`, which failed `test_every_link_names_the_owner[30 ...]` on that file, as the phase's table at `trail/phases/phase-1.md:22` says. The other four rows of that table were not rerun.

What matched: acceptance rows A4 and A5. Executed: `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates` and `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates`, each exit 1. Executed: a search for `stated once|beside the list|count of a list|#1419` over the tree outside `seal/threads` printed rule 19 itself and two lines about other facts. No text cites the removed `agents/framer.md` paragraph.

What matched: the version. Executed: `.claude-plugin/plugin.json` reads `0.39.0`, and `git grep -n -F '0.38.8' -- ':!seal/threads'` exits 1. Rule 19's heading is 88 columns, executed.

What matched: `frame/design.md:32` G22's count of 96 added lines in `cbaae0c59..7415cad73`, executed with `git diff | grep -c '^+[^+]'`. The 52 lines holding a number or such a word were not recounted, since G22 does not give the pattern.

What matched: each `pr.md` quote stands word for word, whitespace collapsed, at the source its coordinate names, executed. `pr.md:2` is still the subject of finding 2.

What matched: the issue facts the frame cites. Executed with `gh issue view`. 29 of 72 fix-made defects were in code (`frame/plan.md:19`). 14 sentences over 28 work items is fewer than one per work item (`frame/plan.md:26`). #1615's evidence on self-reread rules is as `frame/plan.md:28` gives it. #1613 has no comments (`frame/design.md:28`).

The test group: the new row is the only `RULES` row whose links cite `contract rule 19`, so it covers what no other row does. Its owner fact `## 19 ` pins the number and no clause of the body. `frame/design.md:65-66` A6 and A7 give that reading to the proofer, and it was made above.

The suite's label is honest: `gaps.md:7` names the orchestrator's broad gate as the answerer for every test file outside phase 1's boundary run, and for the lint and the format.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, the full suite, lint and format, under contract rule 2 | `seal/config.json` `Broad gate` | the orchestrator |
| Whether the inventory's monitor, output-style and `PostToolBatch` lines hold, on which rows 30 and 34 partly rest; this round did not read those pages | `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:30`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:34` | the framer, in the fold of findings 2 to 4 |
| Whether, once finding 2's ground is rewritten, the `SubagentStop` `agent` hook earns a phase in this item under the owner's direction, or stays named to #1615 | `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:27`, `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md:60` | the framer, in that fold; the orchestrator where it judges the owner must see it |
| The four mutation rows of `trail/phases/phase-1.md:19-23` other than `skills/code-review/orchestration.md`, which this round did not rerun | `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/trail/phases/phase-1.md:19-23` | read, not rerun; no answerer is owed unless the next round touches the row |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_every_agent_reads_the_contract.py tests/behaviour/test_docs_line_wrap.py` | exit 0, 145 passed |
| `bin/seal mutate skills/code-review/orchestration.md --replace 'contract rule 19' 'contract rule' --tests "bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k 30"` | the mutant failed `test_every_link_names_the_owner[30 a change writes no count or universal a later change makes false]`; the file was restored and `git status --short` printed nothing |
| a `python3 -I` check of each `pr.md` quote, whitespace collapsed, against `frame/plan.md` and `frame/questions.md` | all three found |
| `awk -F'\|'` over `changelog.md:12-14` | header 4 cells, delimiter 4, the row 3 |
