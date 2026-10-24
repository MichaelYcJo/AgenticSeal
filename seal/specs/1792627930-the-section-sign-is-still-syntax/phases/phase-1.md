# Phase 1: 1792627930-the-section-sign-is-still-syntax

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 0ca1bee3 |

## What this phase was asked

The contract's numbering, on the base `release/v0.22.3` at 0d62145a, which
already holds #986, #1009 and #988. The 20 headings become `## N title`,
rule 12's heading loses its dash, and the preamble names the citation
spelling. Every contract citation in a living file becomes `contract rule N`,
or `rule N` in the contract and `agents/`. The heading reader becomes one,
imported by the five modules that copied it. The citation reader reads the
new spelling across a line break. The label `session_cost.py` prints for a
spawn, and the sentence in `skills/verify/orchestration.md` that describes
it, change with their pin. The record holds each agent's preload bytes at
base and head, and recomputes its coordinates at HEAD before the first edit.

Coordinates recomputed at HEAD 8caf42f2 before the first edit:
`git grep -n -I -P '\x{00A7} ?[0-9]' -- . ':!seal/specs/' ':!changelog/' ':!CHANGELOG.md' ':!evals/behaviour/'`
printed 362 lines in 93 files (executed). The phase's work was the subset of
those lines that cite the contract, read one line at a time. All living
files held 743 lines in 143 files at that HEAD, against the frame's 747 in
144 at a16acb40 (executed).

## What this phase found

**The frame holds, with two drifts.** The counts moved with the base, as the
plan expected. `spec.md` *Data & interfaces* places the `hooks/config.py`
load in `unverified_check.py` at its line 1047; at HEAD it is at 1054 to
1070 (read). Neither changes what is built.

**What stayed after the phase (executed, the same command).** 20 lines, none
a contract citation: `docs/release-checklist.md` steps 2 to 6 cited from
`.github/` and three test modules, `skills/implement/SKILL.md` steps 1 and 3
cited from `agents/framer.md`, two hooks and four test modules, the
`seal/follow-up.md` release section for 0.12.2, CommonMark's numbered
sections in four test modules, and `rounds/round-3-report.md` section 1 in
one test module. Phases 2 and 3 take them.

**The preamble had to shrink for rule 4 to hold.** The rewrite as first
written put four of five preloads above the base (framer +10, smith +16,
warden +22, scribe +25, sealer -5 bytes, executed), because the simulation
in `plan.md` left the preamble out and the new sentence naming both
spellings costs about 40 bytes. The preamble's list of agent names
(`smith, warden, framer, sealer, scribe, and whichever arrives next`) went:
the heading above it already says the rules bind every agent this plugin
spawns, and no case pinned the list (read: `grep` over `tests/` for its
words found none).

**Preload bytes, `noninferiority.py#preload_bytes` (executed).**

| Agent | Base 0d62145a | After phase 1 | Change |
|---|---|---|---|
| framer | 25255 | 25187 | -68 |
| smith | 24746 | 24684 | -62 |
| warden | 25370 | 25314 | -56 |
| sealer | 23383 | 23300 | -83 |
| scribe | 18545 | 18492 | -53 |

The warden's base is 25370, not the 25109 of `plan.md` *Technical context*:
#988 grew `agents/warden.md` after a16acb40 (executed).

**Rule 12's heading** reads `## 12 A defect belongs to a class, so enumerate
the class`. **A list of two rules** is written as two citations, `rule 7 and
rule 8`, because the reader reads one number per citation.

**Where the path to the contract was named,** as in `CONTRIBUTING.md`, the
printed spawn block of `session_cost.py` and its docstring, the citation
became `contract rule N in skills/agent-contract/SKILL.md` so a reader who
does not know the contract can still find it.

**The printed spawn label** is now `Contract rule 6 — an agent spawned another
agent`, and the closing line `Contract rule 6 binds the agents this plugin
spawns`. The four pins in `tests/test_session_cost.py` were rewritten first
and seen red against the old script (executed: 4 failed), then green.

**Cases seen red.** The new heading and citation cases ran red against the
contract before its headings changed (executed: 58 failed). Mutation-check
over each unit added, each killed (exit 0, executed): the line-break
tolerance of `CITATION`, the bare-home branch of `cited_sections`, the
refusal in `misspelled_headings`, `HEADING` accepting a leading symbol, and
the start-line count. The start-line mutation first survived, so
`test_a_wrapped_citation_is_named_at_the_line_it_starts_on` was added at
0ca1bee3 and the mutation then killed it.

**Q4 did not arise here:** a contract citation names a number the contract
has, and `test_every_cited_section_exists` reads every one.
