# <work-item-id> — review round <N>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/rounds/round-<N>.md — what one review
round reviewed, what it found, and what fixed it. The warden writes this file
in the branch worktree under review; the smith's fix pass fills the `Verdict`
and `Grounds` cells of each open row and changes nothing else; the next round
reads it directly. Earlier round files are never deleted.
`docs/the-review-record.md` states the rules; `chain_check.py` reads
`Target SHA` and the verdict table at the pull request. -->

| Field | Value |
|---|---|
| Target SHA | <the commit reviewed, `<sha> against <base>` · a verifying round: `<sha>, fixes <a>..<b>`> |

<!-- A round past the cap carries one line here, written by the warden from
the reason the orchestrator's spawn prompt gives:
Extended past round <K>: round <K> found <n>, round <K-1> found <m>, and none is a fix of a fix. -->

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | <what is wrong and why it matters; `fix of a fix` where the unit is one the fixes under review added or changed> | `path:line` | open | <the clause, the behaviour, or the constraint> |
| 🟢 | <round N-1's finding 2 is closed — what> | `path:line` | confirmed | <how it was confirmed> |
| ❓ | <what could not be judged> | `path:line` | ❓ out of verified scope | <why, and who answers it> |

<!-- Severities: 🔴 blocks merge · 🟡 fix or justify · 🟢 matches · ❓ out of
verified scope. A 🔴 or 🟡 row carries a bare-integer id and opens at `open`.
The fix pass closes it with one of three verdicts, and adds its grounds after
the warden's as ` · fix pass: <what was done, or why not>`:
  `fixed <commit>`     the commit that fixed it, on this branch
  `answered`           the finding does not hold; the grounds say why
  `deferred <home>`    the issue or file it went to, by the filing ladder
A 🟢 row reads `confirmed`; a ❓ row reads `❓ out of verified scope`. A
ready pull request fails while a 🔴 or 🟡 row reads anything but the fix
pass's three, and while any row reads a word other than these five. -->

## Paste-ready fixes

<one fenced block per 🔴 and 🟡: the artefact itself, not a description of it>

## Executed probes

| What was run | Result |
|---|---|
| <the command> | <what came back: what ran, never what was read> |
