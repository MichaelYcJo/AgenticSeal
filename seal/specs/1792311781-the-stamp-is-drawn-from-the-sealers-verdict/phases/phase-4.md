# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | the commit that adds this record and `evals/sealer-phase-4.json` and `.md` |

## What this phase was asked

The sealer's evaluation, run by the orchestrator, because phase 3 changed one
clause of `agents/sealer.md`: one side of the sealer's cases, two runs a case,
compared with #969's reference side
(`seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/reference-sealer.json`,
rev 1483d8ba) by `noninferiority.py`'s five rules. A `fail` on rule 4 or 5
alone is recorded as it reads.

## Two sides, and why the second is the record

**The first side, at dddcdfdc, read `fail` on rule 4 alone.** The clause
phase 3 wrote ("the stamp is drawn in the orchestrator's session from your
committed `sealed` verdict, once per work item") grew the preload from 24,702
to 24,757 bytes. Every other figure held: 34 of 34 graders passed on both
sides, and tokens per tool call went 37,080.5 → 37,039.3. That side is
history; its files were not committed.

**The orchestrator had the clause shortened rather than recording the fail**
(round 1's fix pass, 6f7aacb2): "a stamp is drawn once from your committed
`sealed`." says the same thing in fewer bytes than the line it replaced, and
the milestone's aim is fewer tokens with the same or a better outcome. The
second side, at 981b0acc, is the record: `evals/sealer-phase-4.json` and
`.md`.

## What this phase found

| Figure, 1483d8ba → 981b0acc | sealer |
|---|---|
| Verdict (`evals/sealer-phase-4.md`) | **pass**, every rule |
| Runs / cut short | 10 / no |
| Preload bytes (agent share) | 24,702 → 24,700 |
| Tokens per tool call | 37,080.5 → 35,992.6 (−2.9%) |
| Tool calls | 77 → 90 |
| Spend USD | 3.3898 → 3.5731 |
| Graders passed | 68 → 68 of 68 |

Both sides ran on one suite: `compare` read the suite tree `5c3e8119…` on
each (Q3, exit 0).

The sealer ran on Opus: across the second side's 10 traces, the 111
assistant events carrying a `parent_tool_use_id` (the sealer's) all name
`claude-opus-5-5`, beside 23 case-session events on Sonnet, which `case.yaml`
sets (counted as #969's phase 4 counted, from every `traces/*.jsonl` line).

**Spend for this phase (eval `costUsd`):** the first side 3.4984, the second
3.5731, **7.0715 in all**.

## Commands

`$S` is the session scratch directory, `$K` is `SpecSeal-worktrees/`, `$E`
is this work item's `evals/`, `$R` is #969's `evals/reference-sealer.json`.

| Command | Exit |
|---|---|
| `noninferiority.py run --agent sealer --rev dddcdfdc --suite-rev dddcdfdc --out $S/975-phase-4/sealer-phase-4.json --runs 2 -j 4 --max-cost-usd 10` | 0 |
| `cp -R` the raw output to `$K/975-phase-4-raw/sealer`, `diff -r`; `run --from-raw`; `cmp`; `compare --old $R` (verdict `fail`, rule 4) | 0, 0, 0, 0 |
| `noninferiority.py run --agent sealer --rev 981b0acc --suite-rev 981b0acc --out $S/975-phase-4b/sealer-phase-4.json --runs 2 -j 4 --max-cost-usd 10` | 0 |
| `cp -R` the raw output to `$K/975-phase-4b-raw/sealer`, `diff -r`; `run --from-raw`; `cmp`; `compare --old $R --out $E/sealer-phase-4.md` (verdict `pass`) | 0, 0, 0, 0 |
| `noninferiority.py check $E/sealer-phase-4.md` | 0 |
