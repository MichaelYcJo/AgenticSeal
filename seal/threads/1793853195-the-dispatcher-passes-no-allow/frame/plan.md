# Implementation Plan: the dispatcher passes on deny and ask alone (#1381)

## Technical context

- `hooks/dispatch.py:111` holds `RANK = {"deny": 3, "ask": 2, "allow": 1}`.
- `hooks/dispatch.py#merge` (from line 208) sorts each gate's output by `classify` into decisions, JSON objects and plain text. On the decision path (lines 220 to 252) it takes the highest-ranked decision, scoring an unranked value 0, and prints the winner's own spelling. The reason is the gates' reasons and texts joined, and a JSON neighbour's `systemMessage` is kept beside it. On the JSON path, after line 252, it prints `dict(jsons[0])` whole and joins the later objects' `systemMessage`s into it. Where neither applies, it prints the texts joined.
- `hooks/dispatch.py#readable` and `#classify` (lines 161 to 205) decide the path. Any truthy `permissionDecision` goes down the decision path. A falsy one, or none, goes down the JSON path.
- `hooks/dispatch.py#main` (lines 585 to 607) gives `merge` the event name `PreToolUse` for every `pre-*` group. It prints the merged output only where it is not blank.
- The dispatcher runs under the `python3` the harness finds, 3.9 on a stock macOS (`hooks/dispatch.py` lines 588 to 590), so the change uses nothing newer than 3.9.
- `tests/hooks/test_dispatch.py#Test_merge` (lines 492 to 523) builds decisions with the module's `decision(kind, reason)` helper (line 80) and calls `merge` directly. `decision_of` reads a printed decision. The new cases go there.
- The probe in `frame/design.md` *Grounding* shows what `merge` prints at `71cfd170` for each shape this work changes (executed).

Failure scenario of the chosen approach, six months on: Claude Code adds a new `PreToolUse` field that approves a call or changes its input. The JSON path removes only the two fields named today, so a gate printing the new field would have it passed on, and the plugin directory could raise the finding again. No gate prints such a field, and the *Registration* rule this work adds states the principle, so whoever adds that gate meets the rule before the directory does.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| The issue's proposal alone: `merge` drops `allow` on the decision path, and the JSON path stays as it is | A `PreToolUse` gate's `{"decision": "approve"}` or `updatedInput` with no decision is still printed whole (probe, executed), and Claude Code reads the first as an `allow` and the second as an input change (hooks reference, read). The finding names both. If the validator reads the JSON path, the next `@dist` is held again, and one more release goes by before anyone learns why. The issue's title, "passes on deny and ask alone", would also stay untrue. | Rejected. The JSON path is in scope as Scope 2. |
| Chosen: Scope 1 and Scope 2. The decision path passes `deny` and `ask` alone, and on `PreToolUse` the JSON path removes `updatedInput` and a top-level `decision` other than `block` | The failure scenario in *Technical context* above. | Chosen. It changes no gate's output (executed: the gates' prints at HEAD). It covers the three fields Claude Code reads as a grant or an input change, and it never allows more (`frame/design.md` *What a change to a gate must carry*). |
| On `PreToolUse`, the JSON path passes the gates' `systemMessage`s alone and drops every other field. This was the frame's first choice, replaced after the orchestrator's P1 asked for a stated failure direction | A top-level `decision: "block"` (Claude Code maps it to `deny`), a `continue: false` and a `stopReason` would all be dropped, and each drop lets a call or a turn go ahead that the gate stopped. That is a wrong allow, the direction `CONTRIBUTING.md` *What a change to a gate must carry* calls the expensive mistake. No gate prints any of them today. | Rejected. Removing exactly the fields that approve or change input keeps every refusal. |
| Replace the structure: register each `PreToolUse` gate in `hooks/hooks.json` directly and drop the dispatcher for that event. Each `pre-*` group holds one gate today (`hooks/dispatch.py#GROUPS`, read), so no merge happens there | A gate that raises would end its process with no record, so the failure report `#28` built (`run_gate`, `FAILED`, `report`) would no longer cover `PreToolUse`. Every gate would also pay its own interpreter start-up again, which the module docstring measures at about 110 to 180 ms each. Each gate file would become the thing the validator reads, and none prints `allow`, but a second `PreToolUse` gate in one group would bring the merge back. | Rejected. The premise that keeps the dispatcher is checked: the load isolation and the failure report live in `hooks/dispatch.py#run_gate` and `#report` (read), and no other module provides them. |
| One builder that prints only named fields for every event, in place of the JSON path's whole-object copy | `session-start`, `session-core`, `post-edit` and `stop` print fields a single list would have to name for each event. A gate that later prints a field the list lacks loses it with nothing said. `PostToolUse` and `Stop` fields grant no permission and change no tool input. | Rejected. On `PreToolUse` too: see the row on passing `systemMessage` alone. |
| Pass `defer` on as well, following Claude Code's precedence `deny` > `defer` > `ask` > `allow` | `defer` ends the turn in a `-p` run. No gate prints it, and the plugin has no use for it. Passing it on would leave the title's "deny and ask alone" untrue for one value, and the plugin directory's text does not list it among what a hook may do. Dropping it is the one drop that does not reduce to "ask more", and `frame/design.md` *What a change to a gate must carry* says so. | Rejected. `defer` counts as no decision. |
| Print a passed decision in the gate's own spelling, as now | A gate's `Deny` would reach Claude Code in a spelling its reference does not list, and the hooks reference does not say whether the value is case-sensitive (read). | Rejected. The lowercase word is printed, at no other cost. |
| Drop a dropped decision's reason along with the decision | The issue's proposal keeps it beside a neighbour's decision as text is kept. Dropping it loses what the gate said, which the module docstring says an overruled gate still has for the user. | Rejected. Its reason joins the gate's text. |
| State as a limit that the JSON path prints a `PreToolUse` gate's object whole, and change no code there | The sentence describes the very behaviour the finding names, and a static reader of `merge` still sees a dispatcher that can change a call's input. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* 1, 2, 3 and 4 | The new `tests/hooks/test_dispatch.py#Test_merge` cases, each shown red as *Scope* 4 says, with how it was shown written in the phase record. `tests/hooks/test_dispatch.py` passes whole in the crafter's narrow run, and the existing cases in it are unedited (S3, S5). | |

*Scope* 5 is the rule change, and it is already written in `frame/design.md` *Rule changes*. The settle writes it into `docs/checks/the-session-hooks.md`. No phase builds it.

## Operational impact

No migration, environment variable, dependency or compatibility break. No gate prints anything this work stops passing on, so no installed repository sees a change in behaviour. The change reaches the plugin directory only through the `dist` commit of the release after this one, which `.github/workflows/publish-release.yml` adds at the tag (work item `1793843890`). Whether it clears `HOOK_GRANTS_PERMISSION` is read when the owner resubmits that `@dist` (`questions.md` Q1).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
