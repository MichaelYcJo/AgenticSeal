# Phase 4: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | |

## What this phase was asked

Rewrite the descriptions of milestones 65 (`release: 0.24.0`) and 67
(`release: 0.24.1`) with the text of `frame/design.md` *The two
descriptions*, each `F<n>` replaced by the number phase 1 recorded. The
owner's answer to Q1 keeps #920 in 0.24.0's small fixes and out of 0.24.1's
description. The owner's two later changes to 0.24.0's order, relayed by the
orchestrator during phase 3, apply: #1109 leaves the small-fix group, fixed
directly before it without a work item, and #1111 runs after #956. The
orchestrator folded all three into `frame/design.md` (`64dca63a`,
`2cdc12b8`), and this phase wrote that text.

## What this phase found

**The two writes (executed; exit codes read directly).**

| Milestone | Command | Exit code |
|---|---|---|
| 65, `release: 0.24.0` | `gh api -X PATCH repos/MichaelYcJo/AgenticSeal/milestones/65 -F description=@<file>` | 0 |
| 67, `release: 0.24.1` | `gh api -X PATCH repos/MichaelYcJo/AgenticSeal/milestones/67 -F description=@<file>` | 0 |

Before sending, each file was compared with the frame's quoted line at
`2cdc12b8` (`frame/design.md:643` and `:647`), with `F1`, `F2` and `F3`
replaced by #1109, #1110 and #1111: equal, `diff` exit 0 (executed). Read back
with `gh api repos/MichaelYcJo/AgenticSeal/milestones/<n> --jq .description`,
each equals the file sent, `diff` exit 0, the file's closing newline included.
Both open with `Purpose:`.

**S5, against the milestones' open issues (executed, `gh issue list
--milestone <title> --state open`).**

- `release: 0.24.0`: the open set and the set the description names are the
  same 22 issues, #712, #913, #920, #951, #956, #992, #1020, #1039, #1040,
  #1041, #1042, #1043, #1052, #1053, #1055, #1056, #1058, #1096, #1102, #1109,
  #1110 and #1111. No closed issue and no issue of another milestone is named.
- `release: 0.24.1`: the 7 open issues, #947, #1045, #1046, #1047, #1048,
  #1049 and #1091, are each named. The description also names #1044, closed in
  `release: 0.23.1`, and #1103, a merged pull request, in its last sentence
  about #947's count.
- S5 asks each open issue to be named once. The frame's text names #1040
  three times and #920, #951 and #956 twice each in 0.24.0's description,
  where a later step gives an earlier issue as its reason. The text was
  written as the frame states it, and `gaps.md` holds the divergence between
  S5's wording and the frame's text.

**#1109 is open while the description says it "was fixed directly".** The
orchestrator's no-work-item pull request into `release/v0.24.0` closes it;
this phase neither closed nor edited it, as the orchestrator's message says.
`gaps.md` *Not verified* names the orchestrator as who makes the sentence
true.

**S7 (executed).** `git diff --stat 0b75346f..HEAD -- .
':!seal/threads/1793163944-the-issues-were-filed-against-the-old-tree'`
printed nothing, exit 0.

The two description files were written to the crafter's scratch directory
outside the tree and removed by their paths when this phase closed.
