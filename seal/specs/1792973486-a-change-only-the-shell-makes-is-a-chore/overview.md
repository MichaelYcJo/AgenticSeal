# Overview: 1792973486-a-change-only-the-shell-makes-is-a-chore

## Why this work exists

The owner's principle that a gate that stops a session guards the work a work item owns, so that a gap only a change routed `no work item` passes through is not a weakness to close, stood in one session's memory; it now stands in `CLAUDE.md`, which every session and agent here reads.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| none | | | |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator's broad run; the repository has no typecheck to run (#951 adds one) |

## Not done

The session memory that held the principle before this work is removed by the orchestrator once this pull request merges, as issue #1031's *Done when* says; it is outside the repository, so no commit here can remove it.

## Fed back into the spec

- The principle names a gate that stops a session, the routing check among them, and not every check: the checks every pull request runs judge a change no work item owns as any other (inferred during implementation, round 1 finding 2; `bb01b549`).
- The example is an identifier renamed across files by `sed`, because a file renamed with `git mv` inside a work item is work the work item owns (inferred during implementation, round 1 finding 1; `bb01b549`).
