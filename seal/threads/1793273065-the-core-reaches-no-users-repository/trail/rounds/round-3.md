# Review round 3: 1793273065-the-core-reaches-no-users-repository

target: 8879a14c, fixes 3418f1a3..8879a14c

## Findings

This round opens no finding.

## Confirmations

confirms: round-2#1
The close holds. The fix pass claimed that the core's sentence is now
round 2's proposed text and that a new assertion pins the hook's clause.
`skills/core/SKILL.md:82-86` reads "The routing question is one of that
batch, and the orchestrating session puts the routing question as
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
states; `hooks/routing-edit-gate.py` refuses the first edit until the
routing question is answered." Each clause now names the routing question
as its subject, so neither "puts" nor "is answered" can attach to the batch
(read). It is still one sentence. The hook refuses an edit only while no
routing declaration names the branch and no `seal no-work-item` is recorded
(read `hooks/routing-edit-gate.py:2-9`), so "until the routing question is
answered" says what the hook does. The new assertion at
`tests/text/test_review_axes.py:118-123` was re-run against both trees: the
whitespace-joined core at `3418f1a3` holds the pinned phrase 0 times and at
HEAD once (executed, *Probes*), and the module passes at HEAD (executed,
*Probes*). That is consistent with the red-then-green the fix pass
reported. The orchestrator's fold at
`seal/threads/1793273065-the-core-reaches-no-users-repository/frame/design.md:50-54`
now also names the routing question as the subject of the hook's clause
(read). It keeps the words "one of that batch". The phrase directly follows
the name of the paragraph *Asking a person is the most expensive judgment*,
and that paragraph holds one batch, so this round judges that it has one
referent and is no finding. Its wording is "the session that spawns the
work", where the core says "the orchestrating session". Both name the same
party. The class was enumerated with `git grep` on "one of that batch",
"one of the batch", "until it is answered" and "which the orchestrating
session puts" (executed). Outside the round records it finds the core, the
design, the case and its docstring, and `hooks/lib/press.py:12` and `:191`.
The last two are outside this diff and already name the routing question as
the subject. Carried rather than re-established: what the batch holds
(`skills/implement/SKILL.md:171-175`) and where the routing question is
placed in it (`skills/implement/orchestration.md:97-99`), both from round
2's coordinates.

confirms: round-2#2
The close holds against the prevention home the orchestrator set on #1177
(issuecomment-6499628665, read with `gh api`, updated 2026-10-29T14:36:50Z).
That home puts the exact bytes in `trail/phases/phase-3.md` at its commit
and in the pull request body at the broad gate's HEAD. Every other text
gives the approximate token cost and links there.
`seal/threads/1793273065-the-core-reaches-no-users-repository/gaps.md:26`
now gives "about 2,100 tokens per agent spawn at 3.2 B/token" and names
both homes (read). `changelog.md:3` now says the share "grows by about
1,570 tokens" and gives no byte figure (read). The docstring at
`tests/skills/test_payload_meter.py:316-322` now copies no figure. It says
the old meter "counted the block's one line and missed the core it
imports", which agrees with the design's grounding row on
`payload_meter.py#composition` (read `frame/design.md:24`). The class was
enumerated by a search over every file the branch changes outside `trail/`
for figures of the form `n,nnn B`, `nnnn B`, `6,7nn`, `6,8nn`, `1,786`,
`2,100` and `1,570` (executed). The only byte figures it finds are the
design's grounding row, which is a measurement at the named commit
`8db7dadd`, and the measurements of other files at
`skills/verify/scripts/payload_meter.py:55-56`, `:787`,
`tests/skills/test_payload_meter.py:660-661`, `:782` and
`tests/behaviour/test_chain_hooks_hardening.py:109`, none about the core.
The comment on #1183 (issuecomment-6498975932, read with `gh api`, updated
2026-10-29T14:36:48Z) now gives about 2,100 tokens, states no byte figure,
and names `trail/phases/phase-3.md` as where the bytes live.

The fix pass's own arithmetic was done at a stale size, and this round
checked whether that matters. Its answer says "Both token figures hold at
6,716 B". But `3c43b42e`, its own fix for finding 1 and committed before
`c8dfc556`, grew the core from 6,716 B to 6,749 B (executed, *Probes*). At
HEAD the second read is 6,749 B, about 2,109 tokens at 3.2 B/token. The
share is the block's 99 B plus the core, 6,848 B, which is 5,062 B over
1,786 B and about 1,582 tokens (executed `wc -c`, computed). "About 2,100"
and "about 1,570" stay within 1% of both. This is the drift the home was
set up to absorb, so it is no finding. It does show again that the figures
move with every edit to the core: the pull request body has to be measured
at the gate's HEAD, not copied from phase 3 or from an answer (*Not
judged*).

confirms: none
The labels are honest about scope. The fix pass labelled no broad gate as
run. This round ran the two modules the fix diff changes, not the full
suite (executed, *Probes*). The orchestrator's 246 passes over three
modules after the fold are its own report, and this round did not re-run
them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `8879a14c` | the tree | the orchestrator, through `seal gate` |
| The orchestrator's 246 passes over `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/test_censuses.py` after the fold, which this round did not re-run | the tree at `8879a14c` | the orchestrator, through `seal gate` |
| Whether the pull request body gives the core's exact bytes as measured at the broad gate's HEAD (6,749 B for the core at `8879a14c`), which `gaps.md:26` says it does. `skills/code-review/scripts/pr_body.py` writes no payload figure, so the orchestrator writes that part by hand | the pull request body, not yet written | the orchestrator when it writes the body; the sealer when it reads it |
| Round 1's *Not judged* rows on the symlinked `~/.claude/CLAUDE.md`, `/agentic:update` under `CLAUDE_CONFIG_DIR`, the three-fix stop for an orchestrating session, and Q2. They are outside this fix diff, carried and not re-examined | `seal/threads/1793273065-the-core-reaches-no-users-repository/trail/rounds/round-1.md` | as round 1 names each: the orchestrator, the owner at #1148 |

## Probes

| Command | Result |
|---|---|
| `git show <rev>:skills/core/SKILL.md \| tr -s ' \n' '  ' \| grep -c "refuses the first edit until the routing question is answered"` for `3418f1a3` and HEAD | 0 at `3418f1a3`, 1 at HEAD |
| `git show <rev>:skills/core/SKILL.md \| wc -c` for `1562e058`, `3418f1a3`, `3c43b42e`, HEAD; `wc -c templates/setup/claude-md-block.md` | 6716, 6716, 6749, 6749; the block 99 |
| `bin/test -q tests/text/test_review_axes.py tests/skills/test_payload_meter.py` | exit 0, 48 passed |
| `git grep -n -e "one of that batch" -e "until it is answered" -e "which the orchestrating session puts" -e "one of the batch"` outside `trail/` | `hooks/lib/press.py:12`, `:191`, `frame/design.md:51`, `skills/core/SKILL.md:83`, `tests/text/test_review_axes.py:105`, `:114` |
| `git diff --name-only origin/release/v0.25.0...HEAD`, outside `trail/`, through `grep -nE` for byte and token figures of the core | `changelog.md:3` (token figures only), `frame/design.md:24` (measurement at `8db7dadd`), `gaps.md:26` (token figure only), and measurements of other files in `payload_meter.py`, `test_payload_meter.py` and `test_chain_hooks_hardening.py` |
