# Review round 2: 1795569535-a-fix-writes-a-count-into-a-record

```seal
target: 34236295a, fixes 06425c682..34236295a
```

This is the verifying round after round 1's fix pass. The fix diff is `06425c682..34236295a`: `4d3d6ad86`, `5690aa090`, `9ad6fb578`, `8b7ef7b16`, `6cfaf525b`, `365e6a8b4`, `0659cbb8a`, `2e2f6799b` and `34236295a`. It was read in a `git clone --no-local` checked out at `34236295a`. Executed: `git diff --stat 619aeee95..34236295a` lists files under `seal/` alone, so no code, skill, agent definition or test changed after round 1's target.

Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/mechanism-inventory.md`, `trail/rounds/round-1.md` and `seal/follow-up.md`. No `pr.<lang>.md` stands, and `seal/config.json` sets `Commit and pull request language` to English, so none is owed. No `seal/parity.json` is declared.

Carried from round 1, since the fix diff does not touch them: rule 19's paragraph states R1 to R6, each citing sentence reads one way, the `RULES` row pins each link, acceptance rows A4 and A5, and the version. Round 1's issue facts on #1613 and #1615 are carried too. Re-derived this round: every close of round 1, every sentence of the fix diff, and the hooks reference facts that the rewritten `SubagentStop` row rests on. Those facts were read from the hooks and subagents pages that `trail/mechanism-inventory.md:4` names, downloaded into the round's scratch directory.

## Findings

### 1. The inventory says the hooks reference names settings files alone for hooks that run inside a subagent, and the reference names plugins in the same sentence

```seal
severity: should
location: `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/trail/mechanism-inventory.md:37-40`
evidence: executed `curl -sL` of the `hooks.md` and `sub-agents.md` pages `trail/mechanism-inventory.md:4` names into the round's scratch directory, then `grep -n -F 'also run inside'` over `hooks.md` (line 255) and `grep -n -F 'all apply inside'` over `sub-agents.md` (line 788); executed `git blame -L 37,47 34236295a` on the inventory (every line `5690aa090`); read `trail/rounds/round-1.md:42` and `:53`
regression: round-1#2
```

Why it matters: the unit is the bullet at `trail/mechanism-inventory.md:37-40`, which `5690aa090` wrote while it answered round 1's finding 2. It quotes `sub-agents.md` and then says "hooks.md names settings files alone for this, so a design that rests on it probes it". The hooks reference holds this sentence: "Hooks from settings files, managed policy settings, and plugins also run inside subagents." Its next sentence says that tool events such as `PreToolUse` and `PostToolUse` fire the same configured hooks inside a subagent as in the main conversation. Round 1 quoted the same sentence, at `trail/rounds/round-1.md:42` and in its paste-ready fix at `:53`. `frame/design.md` G21 says `5690aa090` corrected the inventory's lines on hook inputs, plugin-scoped names and `SubagentStop` "with the docs' own sentences". This bullet's second sentence states no sentence of the docs, and it contradicts the one round 1 quoted.

A reader acts on this bullet. It tells the next design to probe whether a plugin hook fires inside a subagent, and the reference already answers that. The reader is `frame/plan.md` *Overlap with the release*'s #1615 row, which hands the `SubagentStop` hook and the readers beside it to #1615's framer. `agents/framer.md` step 4 has that framer read this frame where it stands. The `PostToolUse` rows of `frame/plan.md` *Alternatives considered* also assume that hooks fire on a crafter's `Edit` and `Write` calls, since they cost the calls that `frame/design.md` G22 counts for phase 1's crafter. The bullet's doubt has no ground, while those rows hold. No verdict changes. The fix replaces the bullet's second sentence with the reference's own sentence. The same commit's closing paragraph, at lines 56-58, stays true as it stands.

```markdown
- Plugin hooks inside a subagent: hooks.md, "Hooks from settings files,
  managed policy settings, and plugins also run inside subagents. When a
  subagent calls a tool, tool events such as `PreToolUse` and `PostToolUse`
  fire the same configured hooks as in the main conversation"; sub-agents.md,
  "Hooks on tool events from settings files, managed policy settings, and
  plugins all apply inside subagents."
```

```seal
verdict: fixed 122d7efd8
answer: The orchestrator wrote the bullet at `5690aa090` and answers it with no fix pass. `122d7efd8` replaces the bullet's second sentence with the hooks reference's own sentence and sub-agents.md's, as the finding's paste-ready fix gives them, read before it was applied. The same commit marks the inventory's `SubagentHandback` line unconfirmed, the line this round's *Not judged* found no ground for in the two pages it fetched. The fix touches the work item's records alone and the finding is located in them alone, so the sealer reads it (`skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row *No fix that no round reads*).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the fragment's process row has four cells under the four-column header. Executed: `awk -F'|'` over `changelog.md:12-14` prints 4 for each of the three lines. Read: the Why cell is the wording round 1's snippet gives, and no other cell changed in `365e6a8b4`.

```seal
confirms: round-1#2
```
What holds: the `SubagentStop` `agent` row of `frame/plan.md` *Alternatives considered* now gives the stop's input `agent_transcript_path` and the plugin-scoped matcher `^agentic:(crafter|framer)$`. Its old ground, "reads records whole without knowing what changed", is gone. Executed: a search for that phrase in the work item outside `trail/rounds/` exits 1. Read in the downloaded hooks reference: *SubagentStop input* lists `stop_hook_active`, `agent_id`, `agent_type`, `agent_transcript_path` and `last_assistant_message`, and calls `agent_transcript_path` "the subagent's own transcript". *SubagentStart* says a plugin's agent type is "the plugin-scoped identifier such as `my-plugin:reviewer`". *Response schema* says an `ok: false` reason on `SubagentStop` "is fed back to Claude as its next instruction". The agent-hook section says an agent hook ends "After up to 50 turns". So every fact the rewritten row cites holds as read, and the row's "not probed" is honest. `pr.md:2` quotes the verdict cell word for word, executed (*Probes*). The same close's inventory half holds for the field and the plugin-scoped name at `trail/mechanism-inventory.md:30-36` and `:41-44`. It does not hold for the bullet at `:37-40`, which finding 1 takes up as a regression.

```seal
confirms: round-1#3
```
What holds: G21's sentence that no row's verdict rests on a line of the inventory alone is gone, and G21 now says each line is a claim and none was probed here. Read: the `PostToolUse` `agent` row, the agent-definition row and the row on an MCP tool, a monitor or an output style each carry the "not probed" marking round 1 asked for, and the `Stop` or `PostToolBatch` row gained one too. No row of *Alternatives considered* still claims to stand on the tree for a fact it takes from the inventory.

```seal
confirms: round-1#4
```
What holds: the `PostToolUse` `prompt` row and the `seal` subcommand row end with round 1's two snippets, and neither leans on the writer's own read of its range. Executed: a search for "Its catch record is none" and "whole-range read already covers" in the work item outside `trail/rounds/` exits 1. The `SubagentStop` `command` row still names the writer's self-read, as the reason it rejects that hook, which is the use round 1 found standing.

```seal
confirms: round-1#5
```
What holds: `seal/follow-up.md:44` holds #1613's row on the issue's second *Done when* line, naming the repository owner. `routing.md:22`, `frame/questions.md` Q1's default cell and `gaps.md`'s second row each name that row as it stands. Read whole at the target.

```seal
confirms: round-1#6
```
What holds: the `to:` of `frame/design.md` `## Rule changes` holds no sentence on where the rule stood until 0.39.0. Executed: a search for "Until 0.39.0 the rule stood" exits 1. The probe of *Probes* parsed the section with `skills/settle/scripts/rule_changes.py#parse(text, "docs")` at the target. It gives one `add` on `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, with `errors` and `unread` empty. So G20's parse still holds for the folded text.

```seal
confirms: round-1#7
```
What holds: `changelog.md:3` and the `to:` of `frame/design.md` `## Rule changes` each end the measurement at the count, and neither names the parties. Executed: a search for "the framer's fold and the orchestrator's record edits" in the work item outside `trail/rounds/` exits 1, which is the search the close claims.

What matched: the three quotes of `pr.md` stand word for word, with whitespace collapsed, at the sources their coordinates name. Executed (*Probes*). The first coordinate, "the row on weighing every mechanism", picks one row of *Judgments of the run*, which now holds two rows dated 2026-11-25.

What matched: `gaps.md`'s third row is ended with the word `closed` and names round 1's *Confirmations* as its reader. No row left the memo. Read: the word diff of `gaps.md` over `619aeee95..34236295a`.

What matched: G23's transcript sizes are a dated measurement. Executed: at this round the framer's transcript holds 3,822,755 bytes on 827 lines and the crafter's 3,230,451 bytes on 694 lines. Each is larger than G23 gives, because the framer folded and the crafter ran its fix pass after G23 was measured. Under rule 19's R5 a dated measurement stays, and the growth only strengthens the row's ground that the transcript "runs to megabytes".

The orchestrator's doubt, weighed: the `SubagentStop` row's verdict, which hands that reader to #1615, stands against the owner's direction. The direction, in the first row of `frame/plan.md` *Judgments of the run*, adds a mechanism as a phase "where one catches the defect at the act at less cost than a round spends on it". The row does not show that condition met, and gives grounds that it is unlikely here. A catch saves a round only where the sentence would have been that round's one finding. The issue counts such sentences at fewer than one per work item, 14 over 28 work items, which round 1 carried. On the other side, an experimental hook type runs a background model for up to 60 s and 50 turns, on every hand-back of every user's run, over a transcript of megabytes. The reference itself says, of agent hooks, "For production workflows, prefer command hooks". The probe that would measure the row is a session no agent may start under contract rule 6, and the verdict gives it to the orchestrator before #1615's frame. The hand-off reaches #1615's framer, since `agents/framer.md` step 4 has it read the frame of each other open item of the release, and the plan's *Overlap with the release* names the hook to #1615. #1615's body makes the first independent reader of a fix its subject, so a reader built here for rule 19 alone would be weighed again there. The second row of *Judgments of the run* is the orchestrator's, and it allowed the fold either home, "as a phase of this work item or as #1615's". One residue is a person's question: whether the owner reads the direction for the release or for this item. That goes to `## Not judged`.

The suite's label is honest. `gaps.md`'s first row names the orchestrator's broad gate for every test file outside phase 1's boundary run, and for the lint and the format, and the fix diff changed no file under test.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, the full suite, lint and format, under contract rule 2 | `seal/config.json` `Broad gate` | the orchestrator |
| Whether the owner reads the direction to weigh every mechanism as met by a release that weighs the `SubagentStop` hook in #1615, rather than by this item. This round found the verdict standing on the record, and asking is the expensive step. The pull request body quotes both the direction and the verdict | `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md` *Judgments of the run*, first row; *Alternatives considered*, the `SubagentStop` `agent` row | the orchestrator, who judges whether the owner must see it before the pull request |
| The inventory's sentence that a hand-back through `SubagentHandback` reaches a `Pre/PostToolUse` hook as `tool_input.message`. Neither downloaded page states it, and the tools reference it would stand on was not read | `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/trail/mechanism-inventory.md:45-47` | the orchestrator, in the probe the `SubagentStop` row's verdict gives it before #1615's frame |

## Probes

| Command | Result |
|---|---|
| `curl -sL` of the `hooks.md` and `sub-agents.md` pages `trail/mechanism-inventory.md:4` names, into the round's scratch directory, then `grep -n -F` for `also run inside`, `all apply inside`, `agent_transcript_path`, `plugin-scoped`, `next instruction` and `50 turns` | `hooks.md:255` names settings files, managed policy settings and plugins; `sub-agents.md:788` the same; each `SubagentStop` fact of the rewritten row found |
| `python3 -I test_tmp_round2_quotes.py <clone>`: each `pr.md` quote, whitespace collapsed, against its source, and `rule_changes.py#parse` over `frame/design.md` | all three quotes found; one `add`, `errors=[]`, `unread=[]`. The probe ran twice, the second run only to print the parse's `errors` and `unread` fields that the first run's output cut off |
| `awk -F'\|'` over `changelog.md:12-14` | 4 cells on each line |
| `git grep -n -F` over the work item outside `trail/rounds/`, for the phrases round 1's findings 2, 4, 6 and 7 removed | exit 1 |
| `ls -la` and `wc -l` over this session's framer and phase 1 crafter transcripts | 3,822,755 bytes on 827 lines, and 3,230,451 bytes on 694 lines |
