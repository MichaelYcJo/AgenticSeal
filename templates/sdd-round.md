# <work-item-id> — review round <N>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/rounds/round-<N>.md — what one review
round reviewed, what it found, and what answered it. The warden writes this
file in the branch worktree under review; the smith's fix pass rewrites each
finding's `verdict:` line and writes its `answer:` line, and changes nothing
else but a coordinate it appends to `location:`; the next round reads it
directly. Earlier round files are never edited or deleted. Words only: no
emoji anywhere in the file. `docs/the-review-record.md` states the rules;
`chain_check.py` reads `Target SHA`, each finding's `verdict:`, `location:`
and `refixes:` lines and each `Confirms` cell at the pull request. -->

| Field | Value |
|---|---|
| Target SHA | <sha> against <base> · a verifying round: <sha>, fixes <a>..<b> |

<!-- A round past the cap carries one line here, written by the warden from
the reason the orchestrator's spawn prompt gives:
Extended past round <K>: round <K> found <n>, round <K-1> found <m>, and none is a fix of a fix. -->

## Findings

<!-- One `### <n>. <symptom>` section per finding, numbered from 1. Its
labels are five lowercase words, each at the start of its line, followed by
`:` and one space, with no emphasis; the check refuses any other spelling
of them.
  severity:  must (fix before merge) or should (fix, or say why not); for
             people, and the check reads none of it
  location:  one or more coordinates, each a backticked `path`, `path:line`
             or `path:first-last` relative to the root, joined by `, `: every
             place the defect shows, and the path the fix goes to where that
             differs. A `fixed` commit must change one of these paths or a
             path under one
  verdict:   the line the check decides on, one of four values:
               open               what the warden writes
               fixed <commit>     the commit that fixed it, on this branch
               answered           the finding does not hold; the answer
                                  says why
               deferred <home>    the issue or file it went to, by the
                                  filing ladder
  refixes:   only on a finding in a unit the fixes under review added or
             changed: the earlier finding as `round-<N>#<n>`, or `round-<N>`
             for a fix pass no finding named. A round carrying one gets no
             fix pass. Delete the line otherwise
  answer:    the fix pass: what was done, why the finding does not hold, or
             where it went
Then why it matters and the grounds, executed and read labelled apart (where
`refixes:` stands, the unit, first); the paste-ready fix in a fenced block,
the artefact itself; and `answer:`. A fix that went to a path `location:`
does not name appends that coordinate to the line and says so in `answer:`.
A ready pull request fails while a finding reads `open`; for a value or a
label the check cannot read; for a `fixed` commit off the branch or touching
no located path; for a `fixed` or `answered` finding the next round neither
confirms nor refixes, or one in the last record, since a verifying round is
owed; and for a fence or comment that never closes. -->

### 1. <what is wrong, as a symptom, in one line>

severity: must
location: `path:12`
verdict: open
refixes: round-1#1

<why it matters and the grounds, executed and read labelled apart>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

<!-- One row per thing this round confirmed holds: an earlier round's finding
truly closed, or a claim of the frame or the build that matched. Never a
finding. `Confirms` is the earlier finding as `round-<N>#<n>` — every
`fixed` or `answered` finding of the round before needs one here or a
`refixes:` line — or `none`. Round 1 has no earlier round: its cells read
`none`. -->

| Confirms | What holds | Location | Grounds |
|---|---|---|---|
| round-1#2 | <what> | `path:line` | <how this round confirmed it, executed or read> |
| none | <a claim of the frame or the build that matched> | `path:line` | <executed or read> |

## Not judged

<!-- One row per thing this round could not judge, and who answers it. Never a
finding. -->

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| <the command> | <what came back: what ran, never what was read> |
