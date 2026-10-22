# Review round <N>: <work-item-id>

target: 1a2b3c4 against main

## Findings

### 1. <what is wrong, as a symptom, in one line>

severity: must
location: `path:12`
evidence: read `path:12`
verdict: open
regression: round-1#1

<why it matters and the grounds>

```<lang>
<the paste-ready fix: the artefact, not a description of it>
```

answer: <the fix pass: what was done, why the finding does not hold, or where it went>

## Confirmations

confirms: round-1#2
<what holds, at `path:line`, and how this round confirmed it, executed or read>

confirms: none
<a claim of the frame or the build that matched, at `path:line`, executed or read>

## Not judged

| What | Location | Who answers |
|---|---|---|

## Probes

| Command | Result |
|---|---|
| <the command> | <what came back: what ran, never what was read> |
