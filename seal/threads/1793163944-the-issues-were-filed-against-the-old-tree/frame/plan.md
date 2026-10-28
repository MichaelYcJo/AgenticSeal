# Implementation Plan: 1793163944-the-issues-were-filed-against-the-old-tree

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 4.

## Summary

The crafter applies `frame/design.md` on GitHub, in `MichaelYcJo/AgenticSeal`.
It files three issues, folds 22 issue bodies to the tree at `0b75346f`,
retitles #1040, moves #920 to `release: 0.24.1`, comments on #920 and #1044,
and rewrites the descriptions of milestones 65 (`release: 0.24.0`) and 67
(`release: 0.24.1`). No file of the tree changes outside this work item's
directory. The owner pressed automation (`routing.md`), which authorizes these
GitHub edits.

## Technical context

**Where each edit comes from.** Every change to a body is a row of
`frame/design.md` *Verdicts*, applied through *The name mapping every fold
applies* and the released-records table beside it. A body is changed only
where its row or the mapping says; every other sentence, table and the closing
`Generated with` line stay as they stand. A new issue's title and evidence are
its section of *Findings no open issue holds*, written as full sentences in the
repository's issue style: a symptom paragraph, the evidence with its
coordinates and labels, then *Done when*. A description is the quoted text of
*The two descriptions*, with each `F<n>` replaced by the number phase 1
recorded.

**How a body is edited.** For each issue, in one phase:

1. Fetch the body fresh: `gh issue view <N> --json body,updatedAt`. At the
   frame's read, taken at 2026-10-28T05:24:47Z, every issue this plan edits
   had an `updatedAt` at or before 2026-10-28T04:50:12Z (executed). Where
   `updatedAt` is later than 2026-10-28T05:24:47Z and the edit is not this
   work's own, someone edited the issue after the read: apply the row to the
   body as fetched, and record the difference in the phase record
   (`questions.md` Q2).
2. Write the new body to a file in the crafter's scratch directory, outside
   the tree, through the `Write` tool, and record its path.
3. `gh issue edit <N> --body-file <that file>`, its exit code read directly
   (contract rule 1).
4. Read it back with `gh issue view <N> --json body` and run the old-form
   search below over it.

**The old-form search**, run over each folded body:

```
grep -n -i -w -E 'smith|warden|scribe' <body file>
grep -n -i -E 'seal/specs/|spec\.md|overview\.md|broad-gate|session-cost|mutation-check|rules --check|specseal|0\.22\.4 ones|as of 0\.22\.4|§' <body file>
```

The first search matches whole words, so `describe` is not a hit.

A hit is acceptable only inside a `<commit>:<path>` citation, inside a sentence
of history the issue's row keeps (a dated move comment is not part of the
body), or where the row itself says it stays, such as #1020's
`agents/warden.md:99` at `6fb3b2fd` and `seal rules --check`. The phase record
lists every remaining hit with which of those it is.

**The failure scenario of this approach, six months out.** The folded bodies
carry line numbers read at `0b75346f`, and each later merge moves some of them.
A framer that builds on a stale line number builds on the wrong code. What
keeps that from mattering is contract rule 5: every framer opens the
coordinates it is handed before it builds on them, and a body that names the
function or heading beside the line (as the rows do) still leads to the right
place. The alternative, bodies with no line numbers, costs every framer the
search the line saved.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Fold each body in place, removing the old form where it stands | Line numbers drift after later merges (above) | Chosen. `CLAUDE.md` *The rule a mechanism is kept against*: a change rewrites the text it amends in place, and the next framer reads one body |
| Leave the bodies and post one comment per issue with the mapping | The framer of each issue reads a body that names files that do not exist and a comment that corrects it, and has to choose between them; `CLAUDE.md` names exactly that as what a correction beside the text costs | Rejected |
| Close each issue and refile it under the new names | Every reference to the old number breaks or misleads: the milestone descriptions, #1102's list of the issues before it, #1045 and #1049's cross-references, commit subjects that will cite the issue. The history of each decision splits across two issues | Rejected |
| Commit each folded body into the tree under `trail/`, so the review reads it at a commit | A second copy of every issue body stands in the tree and drifts at the owner's next edit, with nothing that reads the two against each other. GitHub keeps every body's edit history, and the phase record carries each issue's `updatedAt` before and after, which locates the version the review reads | Rejected |
| Replace the milestone groups with a per-issue dependency list on each issue | Keeps the structure the owner asked for out: the description is where `docs/issues-and-milestones.md` *A milestone answers when* puts the order and its grounds, and a dependency list spread over 26 issues is read by opening 26 issues. Premise checked: no check reads the description (read, `.github/scripts/release_completeness_check.py` reads milestone membership and labels only), so the description is free text a person and a framer read | Rejected; the groups are kept, each with its parallel members and its shared files |
| Keep #920 in 0.24.0's small fixes | A chain run spent on a hint of a guard that #1049 may remove in 0.24.1 | Rejected by default; `questions.md` Q1 holds the owner's answer |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | F1, F2 and F3 filed into `release: 0.24.0` with `gh issue create --repo MichaelYcJo/AgenticSeal --milestone "release: 0.24.0" --title <title> --body-file <file>`, titles and evidence from `frame/design.md` *Filed as new issues*; their numbers recorded in `trail/phases/phase-1.md` | `gh issue view <N> --json title,body,milestone` for each, read against its section (S4) | e96fc422 |
| 2 | The 15 folded bodies of 0.24.0 (`frame/design.md` *Verdicts*, *release: 0.24.0*); #1040's title with `gh issue edit 1040 --title`; #920 moved with `gh issue edit 920 --milestone "release: 0.24.1"` and one `gh issue comment 920` naming #1049 and this work item as the reason | For each issue: the read-back and the old-form search of *Technical context*, every remaining hit judged in `trail/phases/phase-2.md` (S1); `gh issue view <N> --json updatedAt` for #1053, #1096 and #1102, unchanged since the read (S2); `gh issue view 920 --json milestone,comments` (S3) | 1844912f |
| 3 | The 7 folded bodies of 0.24.1 (*release: 0.24.1*), including #1049's list gaining #920 and #947's *After* row and #1044 count; one `gh issue comment 1044` saying the count now lives in #947 | The read-back and the old-form search for each, judged in `trail/phases/phase-3.md` (S1); `gh issue view 1044 --json comments` (S6) | |
| 4 | Both descriptions, with `gh api -X PATCH repos/MichaelYcJo/AgenticSeal/milestones/65 -F description=@<file>` and the same for 67, text from *The two descriptions* with the F numbers filled | `gh api repos/MichaelYcJo/AgenticSeal/milestones/<n> --jq .description` equal to the file sent; `gh issue list --repo MichaelYcJo/AgenticSeal --milestone "<title>" --state open --json number` naming the same set as the description, each once, and no closed issue named (S5); `git diff --stat 0b75346f..HEAD -- . ':!seal/threads/1793163944-the-issues-were-filed-against-the-old-tree'` empty (S7) | |

Each phase writes `trail/phases/phase-N.md` from `templates/records/sdd-phase.md`
and commits it. For every issue it touched, the record states the row applied,
`updatedAt` before and after, the `gh` command's exit code, and each remaining
old-form hit with its judgment. A body file in the scratch directory is
removed when the phase closes (contract rule 17).

No phase runs a test of the repository: no tree file outside the records
changes, so nothing the suite reads moves. The broad gate is the
orchestrator's (contract rule 2).

## Operational impact

None in the tree. On GitHub: three new issues in `release: 0.24.0`, 22 bodies
and one title edited, #920 in `release: 0.24.1`, two comments, and two
milestone descriptions rewritten. Because `release_completeness_check.py`
fails a release pull request while its milestone holds an open issue the
release does not carry, F1, F2 and F3 are work 0.24.0 owes before it ships,
and #920 is no longer owed by 0.24.0.
