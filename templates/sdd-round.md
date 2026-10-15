# <work-item-id> — review round <N>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/rounds/round-<N>.md — what one review
round reviewed, what it found, and what answered it. The warden writes this
file in the branch worktree under review; the smith's fix pass rewrites each
finding's `Verdict:` line and writes its `Answer:` line, and changes nothing
else; the next round reads it directly. Earlier round files are never edited
or deleted. `docs/the-review-record.md` states the rules; `chain_check.py`
reads `Target SHA` and each finding's `Verdict:` line at the pull request. -->

| Field | Value |
|---|---|
| Target SHA | <sha> against <base> · a verifying round: <sha>, fixes <a>..<b> |

<!-- A round past the cap carries one line here, written by the warden from
the reason the orchestrator's spawn prompt gives:
Extended past round <K>: round <K> found <n>, round <K-1> found <m>, and none is a fix of a fix. -->

## Findings

<!-- One `### <n>. <symptom>` section per finding, numbered from 1, holding
four labelled lines, each at the start of its line with no emphasis:
  Severity:      blocks merge · fix or justify — for people; the check reads
                 none of it
  Location:      `path:line` — the sealer reads a `fixed` commit against it
  Verdict:       the one line the check reads, one of four values:
                   open               what the warden writes
                   fixed <commit>     the commit that fixed it, on this branch
                   answered           the finding does not hold; the answer
                                      says why
                   deferred <home>    the issue or file it went to, by the
                                      filing ladder
  Fix of a fix:  the unit the fixes under review added or changed — only on
                 a finding in such a unit, and a round carrying one gets no
                 fix pass
Then why it matters and the grounds, executed and read labelled apart; the
paste-ready fix in a fenced block, the artefact itself; and `Answer:`, which
the fix pass fills. A ready pull request fails while a finding reads `open`,
and while any `Verdict:` reads a value outside the four, a finding has none
or two, or one stands outside a finding. -->

### 1. <what is wrong, as a symptom, in one line>

Severity: blocks merge
Location: `path:line`
Verdict: open

<why it matters and the grounds, executed and read labelled apart>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

Answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

<!-- One row per thing this round confirmed holds: an earlier round's finding
truly closed, a claim of the frame or the build matched. Never a finding. -->

| What holds | Location | Grounds |
|---|---|---|
| <round N-1's 2 is closed — what> | `path:line` | <how this round confirmed it, executed or read> |

## Not judged

<!-- One row per thing this round could not judge, and who answers it. Never a
finding. -->

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| <the command> | <what came back: what ran, never what was read> |
