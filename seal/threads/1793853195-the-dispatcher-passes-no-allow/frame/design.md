# Design: the dispatcher passes on deny and ask alone (#1381)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1381's body (executed: `gh issue view 1381 --repo MichaelYcJo/AgenticSeal --json body,comments`, 2026-11-05; the comments are `[]`) | The plugin directory holds `MichaelYcJo/AgenticSeal@dist` (v0.32.3) under `HOOK_GRANTS_PERMISSION` on the five `PreToolUse` entries of `hooks/hooks.json`. The finding names two things a hook must not do: approve a tool call, or change a call's input before it runs. Done when `hooks/dispatch.py` passes on no `allow` and a case holds that a group whose only decision is a gate's `allow` prints no `permissionDecision`. |
| Claude Code's hooks reference, *PreToolUse decision control* (read: `https://code.claude.com/docs/en/hooks`, fetched 2026-11-05) | `"allow"` skips the permission prompt. `updatedInput` under `hookSpecificOutput` replaces the call's input, and with no `permissionDecision` it still changes the call. The deprecated top-level `decision` values `"approve"` and `"block"` map to `"allow"` and `"deny"`. The values are `allow`, `deny`, `ask` and `defer`. Where several hooks decide, `deny` > `defer` > `ask` > `allow`. A `PreToolUse` hook's plain-text stdout goes to the debug log, and an exit 0 with no decision leaves the call to the normal permission flow. So three fields of a gate's output can approve a call or change its input: `permissionDecision: "allow"`, `updatedInput`, and a top-level `decision: "approve"`. |
| `hooks/dispatch.py#merge`, `#RANK` (line 111) and `#classify` (read) | A truthy `permissionDecision` sends a gate's output down the decision path, where the highest `RANK` wins, an unranked value scores 0, and the winner's spelling is printed. That path builds a new object of three fields, so a gate's `updatedInput` never leaves it. Gate JSON without a decision takes the other path, which prints the first such object whole (`merged = dict(jsons[0])`) with later `systemMessage`s joined into it. |
| Probe of `merge(outputs, "PreToolUse")` at `71cfd170` (executed: `python3 -I test_tmp_merge_probe.py <clone>/hooks/dispatch.py`, run from a `git clone --no-local` under the scratchpad, since deleted) | A lone `allow`, a lone `Allow` and a lone `defer` are each printed as the group's `permissionDecision`. `allow` beside `ask` prints `ask` with both reasons. A top-level `{"decision": "approve"}` is printed whole. A `hookSpecificOutput` holding `updatedInput` and no decision is printed whole. `updatedInput` beside `ask` is dropped. A lone `{"systemMessage": "m"}` is printed as itself. |
| The gates at HEAD (executed: `grep -n 'decide(\|"deny"\|"ask"\|print(' hooks/*.py`) | Every `PreToolUse` gate prints a decision object or nothing. `mode-gate` decides `ask` or `deny`, `review-skill-gate` `ask` or `deny`, `question-gate` and `routing-edit-gate` `deny`, and `implementer-mark` prints nothing. No gate prints `allow`, `defer`, `updatedInput`, a top-level `decision`, or JSON without a decision, so no gate's output changes. The issue names only two of the four deciding gates. The other two are `mode-gate` and `routing-edit-gate`. |
| `docs/checks/the-session-hooks.md` *Registration*, lines 13 to 14 (read) | The policy says the strictest decision wins, in the order deny, ask, silence, and that every reason is kept. It says nothing about `allow` or about a gate's JSON without a decision. The rule goes into `## Rule changes` below with the case that holds it. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code, `hooks/dispatch.py`. It states its rule change for the settle and does not edit `docs/` itself. No unsettled design has an operation on `docs/checks/the-session-hooks.md` (executed: `awk` over every `seal/threads/*/frame/design.md` for the `file:` and `section:` lines of `## Rule changes`, which found no match). |
| `skills/settle/rule-changes.md` *Rule changes*, *A rule has one shape* and *The index* (read); `docs/README.md` line 61 (read) | `file:` comes from the index row for `docs/checks/the-session-hooks.md`. The new rule opens with one bold sentence, gives its grounds in prose, and ends with `check: tests/hooks/test_dispatch.py`. The sentence it replaces leaves through a `remove` with a `from`. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact" (read) | The module docstring's *Merging* paragraph (`hooks/dispatch.py` lines 17 to 19) and the `allow` entry of `RANK` change in the same commit as `merge`. The closed set of sentences that state the merge rule was found with `git grep -n -i 'strictest\|deny over ask\|deny, then ask\|over silence\|RANK\b'` (executed). Outside the frames under `seal/threads/`, the matches were the docstring's line 18, `RANK` at lines 111 and 223, the policy sentence above, and the case name `tests/hooks/test_dispatch.py#Test_merge::test_accepts_the_strictest_decision_and_keeps_every_reason`, which still holds. No README states the rule. |
| `hooks/dispatch.py#main`, lines 585 to 590 (read) | `merge` gets `PreToolUse` for every `pre-*` group. The dispatcher runs under whatever `python3` the harness finds, 3.9 on a stock macOS, so the change uses no construct newer than 3.9. |
| Prior decision: work item `seal/threads/1793843890-the-directory-tracks-a-dist-branch/` (#1374, v0.32.3) built `dist`, and the owner submitted `MichaelYcJo/AgenticSeal@dist` on 2026-11-05 (read: that work item's `frame/design.md` *Scope*; the submission date is the orchestrator's finding in the spawn prompt) | This fix reaches the validator only through the `dist` commit of the release after this one. Nothing in this work item touches `dist`, `.gitattributes` or the release workflow. Readiness for command hooks is #1376's (milestone `backlog: plugin directory`) and stays out of scope. |
| The rest of the reading (read) | `seal/follow-up.md` has no row about the dispatcher. `seal/parity.md` does not exist. The latest release, v0.32.3, has no `### Process changes` heading (executed: `gh release view --json body`). `seal/config.md` has no `Record language` row, so the records are in English. |

## Scope

In:

1. `hooks/dispatch.py#merge` passes on a gate's decision only where its value, lowercased, is `deny` or `ask`, and it prints that lowercase word. Any other value is treated as if the gate printed no decision: `allow`, `defer`, a capitalised `Allow`, or an unknown string. Its reason, where it has one, joins the gate's text, so it is kept beside a neighbour's decision as plain text is and is printed as plain text where no decision passes. `RANK` holds `deny` and `ask` alone.
2. On a `PreToolUse` event, the path for gate JSON with no decision removes two fields before it prints, and prints as it does now otherwise. It removes `hookSpecificOutput.updatedInput`, and a top-level `decision` whose value, lowercased, is not `block`. Those are the fields of such an object that Claude Code reads as an input change or an approval (`approve` maps to `allow`). A top-level `block` maps to `deny` and stays, together with its `reason`. Every other field stays, `continue: false` and `stopReason` among them, so the change removes only what approves a call or changes its input. For every other event, the path prints the first object whole, as it does now.
3. The module docstring's *Merging* paragraph says what passes and what does not, in place of "the strictest wins — deny over ask over silence". The comment above `RANK`, if one is added, says why `allow` is absent.
4. Cases in `tests/hooks/test_dispatch.py#Test_merge`, each shown red as contract rule 15 asks:
   - a group whose only decision is a gate's `allow` prints no `permissionDecision`, and the same holds for `Allow` and `defer`. Red against `merge` at `71cfd170`;
   - `allow` beside `ask` prints `ask`, and both reasons are kept. Green at `71cfd170`, so it is shown red with the new code's one guard removed: the line that keeps a dropped decision's reason as text;
   - on `PreToolUse`, an object holding `updatedInput` and an object holding a top-level `decision: "approve"` reach stdout without those fields, and their other fields, a `systemMessage` among them, are printed. Red against `merge` at `71cfd170`;
   - on `PreToolUse`, an object holding a top-level `decision: "block"` with a `reason` reaches stdout with both. Green at `71cfd170`, so it is shown red by removing the `block` exception from the new code.
5. The rule change in `## Rule changes`.

Out:

- Resubmitting the next release's `@dist` and writing the result on #1381. Done when's second bullet is the owner's act after this release ships, and `questions.md` Q1 holds it.
- Readiness for command hooks under a Verified organization. That is #1376 (backlog). The orchestrator ruled it out of scope in the spawn prompt.
- Gate output on events other than `PreToolUse`, such as `PostToolUse`'s top-level `decision: "block"` or `updatedMCPToolOutput`. Neither approves a call or changes its input, and the finding names `PreToolUse` entries alone.
- The event name `main` gives the `session-start`, `session-core` and `post-*` groups (`PostToolUse`, except `stop`). This work does not change what those groups print.
- `README.md` and `README.ko.md`. Neither states the merge rule (executed: the `git grep` in *Grounding*), and both belong to #1382's branch.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A lone allow | Given a `PreToolUse` group whose one gate prints `permissionDecision: "allow"` with a reason, when `merge` runs, then stdout holds no `permissionDecision`, and the call goes to Claude Code's permission flow. The same holds for `Allow` and `defer`. | A new case in `tests/hooks/test_dispatch.py#Test_merge`, red at `71cfd170` because `allow` is printed |
| S2 Allow beside ask | Given one gate's `allow` with reason `ra` and another's `ask` with reason `rk`, when `merge` runs, then the decision is `ask`, and the reason holds `ra` and `rk` | The same module. It is green at `71cfd170`, and it is shown red by removing the line that keeps a dropped decision's reason |
| S3 Deny and ask unchanged | Given the decisions the gates print today, when a group runs, then stdout is what it was at `71cfd170` | The existing `Test_merge`, `Test_classify` and `Test_report` cases, unedited |
| S4 No grant on the JSON path | Given a `PreToolUse` gate that prints `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "updatedInput": {...}}}` or `{"decision": "approve"}`, with or without a `systemMessage`, when `merge` runs, then stdout holds neither `updatedInput` nor `decision`, and holds the message where there was one | A new case in `Test_merge`, red at `71cfd170` because the object is printed whole |
| S4b A block still blocks | Given a `PreToolUse` gate that prints `{"decision": "block", "reason": "r"}`, when `merge` runs, then stdout holds both fields | A new case in `Test_merge`, shown red by removing the `block` exception |
| S5 Other events unchanged | Given a `Stop` or `PostToolUse` group whose gate prints JSON without a decision, when `merge` runs, then the object is printed whole | The existing `Test_classify::test_accepts_a_deny_beside_a_message_that_is_not_text` assertion on `Stop`, unedited |
| S6 The finding | Given the next release's `@dist`, when the owner resubmits it to the plugin directory, then the validation is read for `HOOK_GRANTS_PERMISSION` | Not in this pull request: `questions.md` Q1 |

## Data & interfaces

What a `PreToolUse` group prints, before (probe at `71cfd170`, executed) and after (Scope 1 and 2):

| Gate output | Printed at `71cfd170` | Printed after |
|---|---|---|
| `allow`, reason `ra` | `permissionDecision: "allow"` | `ra` as plain text, with no decision |
| `Allow`, reason `ra` | `permissionDecision: "Allow"` | `ra` as plain text |
| `defer`, reason `rd` | `permissionDecision: "defer"` | `rd` as plain text |
| `allow` `ra` and `ask` `rk` | `ask`, reason `ra` and `rk` | the same |
| `{"decision": "approve", "reason": "r"}` | the object whole | `{"reason": "r"}` |
| `{"decision": "block", "reason": "r"}` | the object whole | the same |
| `hookSpecificOutput` with `updatedInput` and no decision | the object whole | the object without `updatedInput` |
| `{"systemMessage": "m"}` | `{"systemMessage": "m"}` | the same |
| `deny` or `ask` from any gate | as now | as now, with the decision word lowercased |

No other interface changes. `classify`, `readable`, `run_gate`, the failure records and `report` are unchanged.

## What a change to a gate must carry

`CONTRIBUTING.md` *What a change to a gate must carry* (read) asks a change under `hooks/` for six things. This section states the four that the crafter's fragment and the pull request body copy from here.

- **A test seen red.** *Scope* 4 names each case and how it is shown red.
- **The failure direction: the change passes on less and never allows more.** A dropped `allow`, an `approve` and an `updatedInput` each leave the call to Claude Code's normal permission flow, with the input Claude sent. That flow asks the person or applies their own permission rules, so the call is approved at most as it would be with no hook. A `Deny` or `Ask` printed lowercase can only block or ask where Claude Code might have ignored the capitalised spelling. A top-level `block`, `continue: false` and `stopReason` still pass (*Scope* 2). One dropped value is not "ask more": `defer`. It ends the turn in a `-p` run, and dropped, the call goes to the normal permission flow instead. No gate prints `defer` (executed: the grep in *Grounding*), and the plugin directory's text names deny, ask and leaving the call to that flow as what a hook may do. The cheaper mistake is still this direction: a wrong approval from a hook skips the person, and every value this change drops lands where the person or their rules decide.
- **The prompt budget is zero new prompts per session.** No gate at HEAD prints a value or a field this change drops (executed: the grep in *Grounding*), so no call that ran without a prompt before is prompted now. A future gate that printed `allow` would have its calls go to the person's own permission settings, and the plugin would add no question of its own.
- **Platform honesty.** The change reads and writes JSON in one Python process and inspects no process, so it reads nothing that differs across macOS, Linux and Windows. The hook command, `python3 … || py -3 …`, does not change. CI runs the suite on ubuntu, macOS and Windows under Python 3.12 (read: `.github/workflows/test.yml` lines 69 and 104 to 110). No leg runs Python 3.9, the oldest `python3` the dispatcher is written for (`hooks/dispatch.py` lines 588 to 590), so the change uses nothing newer than 3.9, and that floor goes untested in CI.

What the change removes is `## Removes` below. What it reads is the gates' printed output on stdout, the form `classify` already reads, and that reading does not change.

## Rule changes

- remove
  file: docs/checks/the-session-hooks.md
  section: Registration
  from: Where several gates of a group decide, the strictest wins
    (deny, then ask, then silence) and every reason is kept in the merged text.
- add
  file: docs/checks/the-session-hooks.md
  section: Registration
  to: **A `PreToolUse` group passes on `deny` and `ask` alone, so no gate's
    output can approve a call or change its input.** Where several gates
    decide, the stricter of the two wins, and every reason is kept in the
    merged text. A gate's `allow`, or any other decision, counts as no
    decision, and its reason is kept as the gate's text. A gate's JSON
    without a decision reaches Claude Code without its `updatedInput`, and
    without a top-level `decision` other than `block`, which are the two
    fields of it Claude Code reads as an input change or an approval. The plugin
    directory holds a plugin whose hook can approve a call or change its
    input, and no gate here needs to do either: a gate that has nothing to
    refuse prints nothing, and Claude Code's own permission flow decides.
    check: tests/hooks/test_dispatch.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `allow` entry of the decision ranking | `hooks/dispatch.py#RANK` | Nowhere. No decision path passes `allow`, so nothing ranks it. |
| Passing on the winner's spelling of an unranked or capitalised decision | `hooks/dispatch.py#merge`, the `max(..., key=RANK.get(..., 0))` winner | Scope 1: a decision outside `deny` and `ask` is not passed on. One of those two is printed lowercase. |
| Printing a `PreToolUse` gate's decision-less JSON with its `updatedInput` and a top-level `decision` other than `block` | `hooks/dispatch.py#merge`, `merged = dict(jsons[0])` on the `PreToolUse` event | Scope 2: the object without those two fields. Every other event keeps the line as it is. |
| "the strictest wins — deny over ask over silence" | `hooks/dispatch.py`, module docstring, *Merging* paragraph | Rewritten in place (Scope 3). |
| The sentence on the strictest decision winning | `docs/checks/the-session-hooks.md` *Registration* | `## Rule changes` above, written at the settle. |

This work adds no mechanism: no gate, no check, no hook, no mark. It narrows what the dispatcher passes on. The cases it adds pin that narrowing (contract rules 14 and 15), and the rule it adds replaces a sentence of the same section.

Framed 2026-11-05 by framer, before the build.
