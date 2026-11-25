# Guarantee: 1795569535-a-fix-writes-a-count-into-a-record

Audited at `41f7749e9` against `release/v0.39.0`, which resolves through `release/v0.39.0@{upstream}` to `fd89e2114`. `trail/gate.md` names the run `9a6d59111 against fd89e2114`. That commit is an ancestor of HEAD, and the only commit after it, `41f7749e9`, touches `trail/gate.md` alone (executed: `git log --no-merges --name-only 9a6d59111..HEAD ^fd89e2114`). `seal pr-body <item> --body <pr-body.md> --check` exited 0 with the installed 0.38.8 plugin and with the tree's `bin/seal` (executed). No `seal/parity.json` stands, so no parity comparison is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The new `RULES` row was seen red against the code before the change, failing on `skills/implement/fix-pass.md` | `trail/phases/phase-1.md`, the paragraph opening **Seen red.** | In a `git clone --no-local` at `41f7749e9` under the sealer's scratch `at-base/`, `git checkout fd89e2114 -- skills agents .claude-plugin seal/follow-up.md`, then `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k 30` | holds, executed: exit 1, `test_every_link_names_the_owner[30 ...]` failed on `skills/implement/fix-pass.md`, and the owner's case passed |
| Each link is red alone when its `contract rule 19` citation is removed, and the owner is red when `## 19 ` goes | `trail/phases/phase-1.md`, the mutation table | In the same clone with HEAD's code restored, `bin/seal mutate <file> --replace 'contract rule 19' 'contract rule' --tests "bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k 30"` for `skills/implement/fix-pass.md`, `skills/implement/fold-and-reframe.md`, `skills/implement/orchestration.md` and `skills/code-review/orchestration.md`, and `--replace '## 19 A change rewrites' '## A change rewrites'` on `skills/agent-contract/SKILL.md` | holds, executed: each verdict `red`; each failing line names the mutated carrier, and the owner's mutant failed `test_the_owner_states_the_rule[30 ...]`. `git status --short` printed nothing after the runs. Round 1 had re-run only the `skills/code-review/orchestration.md` row |
| The plan's narrow set passes at HEAD | `frame/plan.md` *Phases*, row 1, the Verified by cell | `bin/test -q -p no:xdist` over the plan's five files and `tests/behaviour/test_docs_line_wrap.py`, in the clone at `41f7749e9` | holds, executed: exit 0, 145 passed |
| Rule 19's heading keeps its number and fits the wrap limit of 88 | `trail/phases/phase-1.md`, the paragraph on rule 19's heading | `grep -n '^## 19' skills/agent-contract/SKILL.md` with its length taken | holds, executed: the line is 88 columns without the `196:` prefix |
| `## Removes` row 1: the framer's count paragraph is gone | `frame/design.md` `## Removes` | `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates` at HEAD | holds, executed: exit 1 |
| `## Removes` row 2: the count clause of the orchestrator's guidance is gone | `frame/design.md` `## Removes` | `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates` at HEAD | holds, executed: exit 1 |
| The changelog's removal of the framer's own count rule leaves no copy | `changelog.md`, the third item of `### Changed` | `git grep -n -i -E 'stated once, beside\|count of a list\|calls one of them the only one' -- ':!seal/threads'` at HEAD | holds, executed: exit 1 |
| The version moves to 0.39.0 and 0.38.8 stands nowhere outside the records | `trail/phases/phase-1.md`, the last paragraph | `git grep -n -F '0.38.8' -- ':!seal/threads'` at HEAD; read the `.claude-plugin/plugin.json` diff | holds, executed: exit 1, and `plugin.json` reads `0.39.0` |
| `pr.md`'s three quotes stand word for word at their sources | `pr.md` | a `python3 -I` check of each quote, whitespace collapsed, against `frame/plan.md` and `frame/questions.md` at HEAD | holds, executed: all three found |
| Round 2 finding 1, `fixed 122d7efd8`: the inventory's bullet on plugin hooks inside a subagent quotes the hooks reference | `trail/rounds/round-2.md` finding 1; `trail/mechanism-inventory.md:37-42` | `git show 122d7efd8`; `curl -sL` of `code.claude.com/docs/en/hooks.md` and `sub-agents.md` into the sealer's scratch `sealer-docs/`, then `grep -n -F` for each quoted sentence | holds, executed: the commit touches `trail/mechanism-inventory.md` alone; the bullet is the finding's paste-ready text; `hooks.md:255` and `sub-agents.md:788` hold the quoted sentences |
| The same commit's second change: the inventory's `SubagentHandback` line is unconfirmed, because "round 2 found no such sentence in the hooks.md and sub-agents.md it fetched" | `trail/mechanism-inventory.md:47-52`, written at `122d7efd8`; `trail/rounds/round-2.md` *Not judged*, row 3 | `cmp` of round 2's downloaded `round-2/docs/hooks.md` with the sealer's fetch; `grep -n -F 'receives as \`tool_input.message\`'` and `grep -n -F 'read \`tool_input.message\`'` over round 2's copy | does not hold, executed: the two copies are identical. Round 2's own copy of `hooks.md` states the line at 2718, under *SubagentStop input*: "The report is that call's `message` input, which a `PreToolUse` or `PostToolUse` hook matched on `SubagentHandback` receives as `tool_input.message`." Line 1981 says the same under the `Agent` tool's result. So round 2's *Not judged* row 3 is false, and the inventory now marks as unconfirmed a line its own named source states |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Rule 19 gains clauses R1 to R6, the fix pass, the fold, the orchestrator's step 1 and the orchestrator's mechanism-edges paragraph cite it, the framer's paragraph and the code-review clause go, a `RULES` row pins the citations, and the version moves to 0.39.0 (`frame/design.md` *Scope* items 1 to 8, `## Removes`) | the issue's *Proposed* and its first *Done when* line; the diff, which changes exactly the files Scope items 1 to 8 name plus `seal/follow-up.md` from round 1 finding 5; `routing.md` *Why this way*, whose grounds describe that diff | none |
| the build | Phase 1 delivered Scope items 1 to 8 at `935f8bf56`, with the red runs, the mutation table and the boundary run (`trail/phases/phase-1.md`) | the design; the claims re-run above; `frame/plan.md`'s Status cell, which names `935f8bf56` and has its phase record | none |
| the last round | Round 2 confirms round 1's seven closes and raises one `should` finding on the inventory, closed `fixed 122d7efd8` by the orchestrator, with three rows under *Not judged* (`trail/rounds/round-2.md`) | the diff and the records at `34236295a`; the fix of its finding 1, which `trail/mechanism-inventory.md:37-42` holds at HEAD | the hooks reference it downloaded: its *Not judged* row 3 says neither page states the `SubagentHandback` line, and round 2's own copy of `hooks.md` states it at 2718 |
| the changelog | Contract rule 19 gains the clauses, four procedures cite it, `agents/framer.md`'s count rule goes, and the version moves to 0.39.0 (`changelog.md`) | the diff; the design. Its process row's "until 0.39.0 the rule against it bound the framer alone" agrees with `frame/design.md` G8, which calls the framer's paragraph the one party-scoped statement of the rule, and G9 calls the code-review clause an application of it to one case | none |
| the orchestrator's part of the pull request body | Three quotes of the records: the owner's direction to weigh every mechanism, the `SubagentStop` row's verdict, and Q1's default, then `Closes #1613` (`pr.md`) | the records it quotes, word for word; the issue, whose second *Done when* line `seal/follow-up.md:44` holds for the owner | none |
| the orchestrator's records-only fix | `122d7efd8` answers round 2 finding 1 and marks the inventory's `SubagentHandback` line unconfirmed (`trail/rounds/round-2.md` finding 1, its `answer:`) | round 2 finding 1, which it fixes as asked | the hooks reference that `trail/mechanism-inventory.md:3-4` names as its source: *SubagentStop input* states the line it marks unconfirmed |

## What the orchestrator fixes

The one claim that does not hold stands in a record, and no code, skill or test is affected. `trail/mechanism-inventory.md:47-52` says the `SubagentHandback` line is unconfirmed. The hooks reference states it, in the copy round 2 downloaded and in the sealer's fetch of the same day.

Why it matters: `frame/plan.md` *Overlap with the release* hands the independent readers of a fix's records to #1615's framer, who reads this frame and its inventory. A reader of a crafter's hand-back through a `PreToolUse` or `PostToolUse` hook on `SubagentHandback` is one of those readers. The inventory now tells that framer to doubt or probe a fact the reference already gives. This is the defect class of round 2's finding 1.

The fix replaces the line's "The claude-code-guide agent also read that ... so this line is unconfirmed." with the reference's sentence and its coordinate. For example:

```markdown
  file list. hooks.md *SubagentStop input*, on v2.1.271 or later: "The
  `last_assistant_message` field then holds the subagent's closing text, if
  any, which is not the delivered report. The report is that call's `message`
  input, which a `PreToolUse` or `PostToolUse` hook matched on
  `SubagentHandback` receives as `tool_input.message`."
```

That commit touches the work item's records alone, so the sealer reads it in the next audit. Round 2's *Not judged* row 3 stays as the round wrote it.

```seal
target: 41f7749e9 against fd89e2114
Verdict: withheld reason: the orchestrator's records-only commit 122d7efd8, which no round read, marks the SubagentHandback line of trail/mechanism-inventory.md:47-52 unconfirmed on round 2's word that neither fetched page states it, and the hooks.md round 2 downloaded states it at line 2718 under SubagentStop input
```

## Re-audit at 4a932c040

Audited at `4a932c040` against `release/v0.39.0`, which still resolves to `fd89e2114`. The commits since the block above's `target:` are `907aeec80`, which touches `guarantee.md` alone, and `4a932c040`, which touches `trail/mechanism-inventory.md` alone (executed: `git log --no-merges --name-only 9a6d59111..HEAD ^fd89e2114`). So `trail/gate.md`'s run `9a6d59111` is followed only by paths under `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/`, and the broad run stands for HEAD. `seal pr-body <item> --body <pr-body.md> --check` exited 0 at `4a932c040` with the installed plugin and with the tree's `bin/seal` (executed). No code, skill, test or other record changed since `41f7749e9`. So every claim of the block above except the inventory's is carried as it was re-run there.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The inventory's `SubagentHandback` sentences quote hooks.md *SubagentStop input* | `trail/mechanism-inventory.md:47-51`, written at `4a932c040` | `git show 4a932c040`; a `python3 -I` check of the quoted text, whitespace collapsed, against the sealer's fetch of `hooks.md` in scratch `sealer-docs/`, which `cmp` showed identical to round 2's copy | holds, executed: the quote stands word for word in the reference, under *SubagentStop input* at line 2718, and the version condition "v2.1.271 or later" is the reference's own. The "unconfirmed" mark and its ground are gone |
| No other text of the work item still calls the `SubagentHandback` line unconfirmed | the work item's records outside `trail/rounds/` and `guarantee.md` | `git grep -n -i 'unconfirmed\|SubagentHandback'` over them at HEAD | holds, executed: the remaining "unconfirmed" lines, `trail/mechanism-inventory.md:75` and `:96`, are about other facts, and no commit since `41f7749e9` touched them |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as in the block above, unchanged since `41f7749e9` | the issue, the diff and `routing.md` *Why this way* | none |
| the build | as in the block above, unchanged | the design and the claims re-run above | none |
| the last round | as in the block above; its *Not judged* row 3 stays as round 2 wrote it, a dated record | the diff and the records at `34236295a` | its *Not judged* row 3, which the inventory no longer builds on |
| the changelog | as in the block above, unchanged | the diff and the design | none |
| the orchestrator's part of the pull request body | as in the block above, unchanged; the body file at `4a932c040` matches the records | the records it quotes and the issue | none |
| the orchestrator's records-only fixes | `122d7efd8` answered round 2 finding 1, and `4a932c040` replaced the `SubagentHandback` sentences with the reference's text, as this file's *What the orchestrator fixes* asked | round 2 finding 1; hooks.md lines 255 and 2718; sub-agents.md line 788 | none |

Read, not decisive: the inventory's closing paragraph, `trail/mechanism-inventory.md:60-62`, still says the lines on hook inputs, plugin-scoped names and `SubagentStop` were re-read by the claude-code-guide agent after round 1's finding 2. Two of the quotes now standing above it came from round 2 and from this audit's reading of the same pages. The paragraph is dated to that re-read and says that none of the lines was probed, which still holds. No reader acts differently on whose reading supplied a quote that the reference holds word for word.

```seal
target: 4a932c040 against fd89e2114
Verdict: sealed
```
