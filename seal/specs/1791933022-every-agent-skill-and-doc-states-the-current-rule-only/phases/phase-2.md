# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | not closed — the build ends at this record's commit; the phase closes with the orchestrator's baseline commit |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Build the non-inferiority harness ahead of phase 1, by the orchestrator's
decision: the generators (`replay_targets.py`, `seed_defects.py`,
`rule_cases.py`), `noninferiority.py`, the record test T10–T12, and the
layout test recursing. First act: answer Q7 by running one replay case
through `claude plugin eval` against today's tree and against a copy with
the warden's `## Report` fence deleted, with the broken side expected red
(S10) and the case's session reaching the plugin's agents as production
does; fall back to E7 where the command cannot do that. Keep the probe
bounded and report its cost. Do not take the 38-run baseline: hand back its
command, run count, cost and output files. Mark Q6 accepted.

## What this phase found

**Q7: the command runs on this account, and a case reaches the agents the
way production does.** The session calls `Agent` with `subagent_type`
`specseal:warden`; the warden's own tool calls sit in the run's trace with
their `parent_tool_use_id`, and every grader kind reads them (a `tool_used`
grader counted a subagent's `Bash` call, a `files` grader listed a file the
subagent wrote). E7 is not needed.

**S10 holds for one of its two variants.** On case
`warden replay-1791382684-r5`, one run a side:

| Side | Shape graders | Truth | Report rows · false | Verdict | Cost · wall |
|---|---|---|---|---|---|
| today's tree | 5/5 | 0/1 | 1 · 1 | (baseline) | $2.56 · 503 s |
| `## Report` fence deleted | 5/5 | 0/1 | 3 · 3 | pass | $2.03 · 508 s |
| the two terminal-line rules removed from `agents/warden.md` | 3/5 | 1/1 | 1 · 0 | fail, naming both shape graders | $1.83 · 307 s |

The fence-deleted warden still wrote `## Verdicts` in the record's columns:
the shape stands in `skills/code-review/SKILL.md` and in the clone's earlier
`round-4-report.md`, so deleting one copy changes no output. `check` exits 1
on the failing record and 0 on the passing one; T11 holds the hand-edited
`pass` over failing numbers.

**What the runner has to do, measured.**

1. `context.scaffold_script` is a path to a file beside `case.yaml`; an
   inline script is refused as a path that does not exist. `max_turns`,
   `timeout_seconds` and `model` are read under `execution:` only; a
   top-level copy is dropped and the run takes 10 turns and 300 s.
   `execution.env` takes `EVAL_*` keys alone.
2. In the eval's sandbox `/usr/bin/git` is Xcode's stub and exits 72: it
   cannot write its cache under `/var/folders`. The Command Line Tools'
   binary runs when called by its full path, but a `stat` of it is denied,
   so a `PATH` entry pointing at it is skipped. `run` writes `.shims/git`
   inside the measured tree, which the sandbox reads, and puts it on `PATH`.
3. The session's `PATH` is the caller's, the installed plugin's `bin/`
   included; `run` drops every `/.claude/plugins/cache/` entry and puts the
   measured tree's `bin/` first.
4. The orchestrating session dropped the second paragraph of a two-paragraph
   spawn prompt; the prompt between `BEGIN PROMPT` and `END PROMPT` is one
   paragraph now. A `=====` delimiter is a setext heading the heading rule
   refuses.
5. `--max-cost-usd` is checked before a run launches and never stops one in
   flight; a run is bounded by `timeout_seconds`.
6. `--keep-temp` is what keeps a trace; the kept directory is sealed mode
   000. `run` reads each trace, then removes each kept directory.

**The suite as generated.** 21 cases: warden 9 (4 replay, 4 seeded, 1 rule),
smith 4, framer 4, sealer 3, scribe none — the contract's rules ride every
case as `rule-` graders. Every scaffold ran outside the eval and built its
repository; the three sealer fixtures, run through this tree's
`broad-gate`, gave sealed (exit 0, cell written), not sealed (exit 1) and
refused (exit 2) as their cases expect. 22 rounds of the last two tags have
truth; the replay set is the four smallest diffs, one per work item, all
verifying rounds of 99–132 lines.

**T10 reads hashes, not a diff.** `run` records the sha256 of the measured
tree's preload in the baseline; an agent whose preload now differs owes a
record beside the baseline that measured the preload as it stands and whose
numbers give `pass`. No merge base is computed, so the case runs the same on
a worktree, in CI and after a rebase.

**Seen red.** 26 mutations through `mutation-check`, each red: the five pass
rules (eight cases), the record's recomputation, the cut-short side, the
preload set reaching skills, a record matching another preload, the census
cell, false-row counting, which report print is read, the truth window, the
next round's confirmation, the seed's code tokens, the runner's cleanup and
its `PATH`. Two survived first (the subagent filter, the seed tokens), and
their cases were tightened until red.

**Cost of the phase's probes.** Measured: $7.66 over 15 runs (the three
replay runs above, a first broken run that stopped with no git at $0.47,
and eleven smoke runs at $0.77 together, $0.39 of it the two model-alias
probes). One more replay run was stopped
mid-review once the missing git was found; its result line never arrived,
so its cost is not measured.
