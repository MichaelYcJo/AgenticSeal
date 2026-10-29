# Review round 2: 1793163944-the-issues-were-filed-against-the-old-tree

target: 7cc6af5c, fixes a895ce30..7cc6af5c

This round verifies the fixes for round 1. The range holds four commits:
`bb9130fc`, the orchestrator's frame lines; `81b9a229`, the crafter's fix
pass, which made the GitHub edits and added `trail/phases/phase-5.md` and
Q2's Status cell; `8e5261cf`, the two answers; and `7cc6af5c`, the
orchestrator's three remaining title sentences in the frame. Round 1's
coordinates are carried, not searched again: its two findings' `location:`
lines, its paste-ready text, and `gh` as the reader of the GitHub side. Each
verdict below is re-derived. The owner has not answered whether titles
change. The retitles build on round 1's default, and that is not judged
here.

## Findings

### 1. The fix pass wrote a phase record, and both verdicts name its commit, which holds the record and not the repair

severity: should
location: `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/rounds/round-1.md:23`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/rounds/round-1.md:96`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/phases/phase-5.md`
evidence: read `agents/crafter.md:153-162`, `docs/the-review-record.md:135-143`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/plan.md:88-92`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/rounds/round-1.md:89`, `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/rounds/round-1.md:151`
verdict: fixed a28fbc24
regression: round-1#1

The unit is `trail/phases/phase-5.md`, which the fix pass's commit
`81b9a229` added, together with the two verdict lines that name that commit.
The fixes of both round-1 findings made it, and finding 1's comes first.
`frame/plan.md:88-92` asks each build phase for a phase record, and
`frame/design.md` says nothing about a fix pass. The fix pass added a fifth
phase record anyway, and the defect came from applying the build phases'
record rule to a fix pass.

Two policy sentences set out how a fix pass closes, and the range follows
neither:

- `agents/crafter.md:153`: "A fix pass writes two lines of each finding and
  no phase record."
- `docs/the-review-record.md:135-143`: "A repair a commit made, a
  correction to a record among them, closes `fixed <commit>`", and "A repair
  made outside the tree, an issue or a pull request body edited, makes no
  commit on the branch and closes `deferred <where it was repaired>`".

Both answers state that `81b9a229` "changes none of the frame lines this
finding names: the orchestrator folded those at `bb9130fc`". So the commit
that made the in-tree repair is `bb9130fc`, and the rest of the repair is on
GitHub. `fixed 81b9a229` points a later reader, the sealer included, at a
commit that adds a record and repairs nothing. The phase record exists only
so that the named commit can touch a path on `location:`.

The substance of both fixes holds (see *Confirmations*), so the repair is
to the record alone. The evidence `phase-5.md` holds, each `updatedAt` and
exit code and the old and new titles, belongs in the `answer:` lines.

```text
trail/rounds/round-1.md:23 and :96, each:
verdict: fixed bb9130fc

Each answer: drop the sentence that names 81b9a229 and phase-5.md, and say
that bb9130fc corrected the frame lines `location:` names, and that the
GitHub edits (each `gh issue edit` exit 0, read back equal, with the
updatedAt values now in phase-5.md) made no commit. Remove
`trail/phases/phase-5.md` from both `location:` lines.

git rm seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/trail/phases/phase-5.md
```

Before acting, the fix pass weighs the other reading: keep `phase-5.md` and
answer this finding `rejected`, if the orchestrator's spawn prompt asked for
a phase record and the owner wants GitHub acts recorded in the tree. Then
`agents/crafter.md:153` stands against the record, and the answer names who
decided that.

answer: The finding holds, and the other reading was weighed and not taken. The orchestrator's round 1 spawn prompt asked for `trail/phases/phase-5.md`, but its round 2 message withdraws that request, and nobody asked for GitHub acts to be recorded in the tree. So `agents/crafter.md:153` and `docs/the-review-record.md` *The round record* decide it. Commit `a28fbc24` applies the fix line as written. Both verdicts in `trail/rounds/round-1.md` now read `fixed bb9130fc`, the orchestrator's commit that changed `frame/design.md` on each finding's `location:`. Each `answer:` drops the sentence naming `81b9a229` and `phase-5.md`. Each answer says that `bb9130fc` corrected the frame lines and that the GitHub edits made no commit. Each answer now carries what `phase-5.md` held: finding 1's three body edits with their exit codes and `updatedAt` before and after, and finding 2's eight titles, old and new, with their exit codes. The appended `phase-5.md` coordinate is gone from both `location:` lines, and `git rm` removed the file. A `git grep` of the work item directory for `phase-5` and `81b9a229` now finds them only in this round record, which describes the range it reviewed. `frame/questions.md` Q2's Status cell, added in `81b9a229`, stands.

## Confirmations

confirms: round-1#1
The close holds on GitHub (executed, `gh issue view <N> --json
body,updatedAt` and a word diff against each body's previous version from
`userContentEdits`). #1109's third *Done when* bullet now reads round 1's
text and nothing else changed. #1110 gains the census bullet under *What
this work decides* and nothing else changed. #1111's second *How it
differs* bullet drops "so this issue runs after #1040", and the new
`## Order` section names #956 and #1040 with the owner's ground. All three
edits are dated 2026-10-28T06:06Z. `frame/design.md:508-509` and `:570-572`
at `7cc6af5c` hold round 1's text (read). Pull request #1112 merged into
`release/v0.24.0` at 2026-10-28T06:01:35Z (executed, `gh pr view 1112`).
So milestone 65's "#1109 was fixed directly" now holds, which closes round
1's *Not judged* row about that sentence.

confirms: round-1#2
The close holds. Each of the eight live titles equals the text of round 1's
`gh issue edit` commands, string for string (executed, `gh issue view <N>
--json title` compared by script with the record at `7cc6af5c`). #1040's
title is unchanged. `frame/design.md:47-50` lists the nine titles, and the
false premise is gone. The three sentences `7cc6af5c` corrected
(`frame/design.md:190-195` and *Data & interfaces*, `frame/questions.md`'s
answered bullet, and `frame/plan.md` *Summary* and *Operational impact*) now
state nine titles. A `git grep` of the work item's frame, `gaps.md` and
`routing.md` for title statements finds no other sentence saying one title
changes. `frame/plan.md:84`, phase 2's row, names #1040's title as the act
of that phase, which is true (executed).

confirms: none
`frame/questions.md` Q2's Status cell, new at `81b9a229`, agrees with phases
2 and 3, which record every `updatedAt` before an edit as earlier than the
frame's read (read). Phase 5's explanation of #1109's later `updatedAt`,
2026-10-28T06:01:52Z, as an event that left the body unchanged agrees with
#1112's merge 17 seconds earlier and with the edit history: #1109's body
has no edit between 05:29:34Z and 06:06:36Z (executed, `userContentEdits`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the eight retitles stand: the owner has not answered, and they build on round 1's default | `frame/design.md:47-50` | the owner, through the orchestrator |
| The broad gate over this branch; this round ran no suite, lint or typecheck | `trail/gate.md`, not yet written | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `gh api graphql` for `body` and `userContentEdits` of #1109, #1110 and #1111, then `git diff --no-index --word-diff=plain` against the previous version | only round 1's text changed in each |
| `gh issue view <N> --json title` for #712, #1039, #1040, #1042, #1043, #1045, #1046, #1048, #1049, compared with the `gh issue edit` lines of `round-1.md` at `7cc6af5c` | eight equal; #1040 unchanged |
| `gh pr view 1112 --json state,mergedAt` | MERGED 2026-10-28T06:01:35Z |
| `git grep -n -i -E "one title\|only #1040\|one exception\|#1040's title\|retitle\|titles?"` over the frame, `gaps.md` and `routing.md` at `7cc6af5c` | three hits, each stating the current fact |
