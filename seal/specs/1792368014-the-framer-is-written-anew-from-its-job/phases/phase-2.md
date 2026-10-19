# 1792368014-the-framer-is-written-anew-from-its-job — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 5dc581c9 |


## What this phase was asked

Take one framer side on phase 1's tree after #976 and #985 had merged
(`questions.md` Q2). The side used suite `af9c924b`, 2 runs a case, 4 at a
time, capped at $25. The raw output is kept outside the tree, and the side
is compared with #967's last framer side as the baseline. The orchestrator
ran the side and committed its records. This phase's record holds the
facts, and the rule-5 breakdown `plan.md` asks for: per run from the kept
traces, the framer's requests, tool calls, tools per request and tokens per
request, and the request and bytes of each opening of `implement` and
`writing-style` (S3, S10, Q4).

## What this phase found

**The side and its verdict** (`executed` by the orchestrator, `read` here
from the records at 5dc581c9).

- The side was taken with `noninferiority.py run --agent framer --rev
  b434e145 --suite-rev af9c924b --runs 2 -j 4 --max-cost-usd 25`, exit 0.
  The raw output is kept at
  `/Users/x/Documents/GitHub/SpecSeal-worktrees/968-framer-raw` on the
  orchestrator's machine: `meta.json`, `raw.json` and eight traces,
  `traces/000.jsonl` to `007.jsonl`.
- `evals/baseline-framer.json` is a byte copy of #967's
  `evals/framer-phase-4.json`. I re-ran that `cmp` here, and it exits 0
  (`executed`).
- `evals/framer-phase-2.md`, written by `compare --phase 2`, reads
  `Verdict: pass`, with every pass rule holding. I re-ran
  `noninferiority.py check` on it, and
  `tests/test_a_rewritten_definition_proved_non_inferior.py`; both exit 0
  (`executed`).

| Figure | Baseline (#967, tree af716289) | This side (b434e145) |
|---|---|---|
| Preload bytes | 86,353 | 26,027 |
| Tokens read, every model | 3,258,508 | 2,956,842 |
| Tool calls | 109 | 172 |
| Tokens per tool call | 29,894.6 | 17,190.9 |
| Spend USD | 16.1196 | 14.7490 |
| Wall seconds | 2,031.1 | 1,954.8 |
| Graders passed | 64 of 64 | 64 of 64 |
| Runs cut short | none | none |

Phase 3 does not run. Its row runs only on a `fail` in phase 2.

**Rule 5, read apart.** The rule reads tokens per tool call. Its new/old
ratio is 0.575, which is the product of two factors:

- 0.907 from total tokens, which fell 9.3%;
- 0.634 from tool calls (109/172), which rose 57.8%.

So most of the fall is the larger call count, not the smaller total. The
traces show where the calls came from: each framer located the headings
first (a `Grep`, or `grep -n` in `Bash`), then read each section as its own
ranged call. `spec.md` §*What moves rule 5* reads a fail; here the side
passed, and this is what the passing figure is made of.

**Per run, from the kept traces** (`executed`, a count over each trace; Q4's
default). `bin/session-cost --segments` does not read the eval's trace
shape: on `traces/000.jsonl` it reports *0 segments found*, because it
looks for a session's `subagents/` directory. So the events carrying
`parent_tool_use_id`, the spawned framer's, were counted directly.

- A request is one distinct assistant `message.id`.
- Its tokens are the input, cache-creation and cache-read counts of that
  message's `usage`.
- A tool call is one `tool_use` block, counted once by its id.

| Case | Run | Requests | Tool calls | Tools per request | Tokens per request | Framer tokens |
|---|---|---|---|---|---|---|
| document-helpers | 0 | 6 | 24 | 4.00 | 35,616 | 213,693 |
| document-helpers | 1 | 6 | 23 | 3.83 | 36,661 | 219,968 |
| keep-trailing-space | 0 | 5 | 18 | 3.60 | 36,836 | 184,182 |
| keep-trailing-space | 1 | 12 | 12 | 1.00 | 39,090 | 469,077 |
| loud-flag | 0 | 6 | 20 | 3.33 | 35,716 | 214,297 |
| loud-flag | 1 | 9 | 22 | 2.44 | 37,593 | 338,335 |
| word-count | 0 | 7 | 25 | 3.57 | 38,579 | 270,052 |
| word-count | 1 | 6 | 20 | 3.33 | 36,593 | 219,556 |
| **side** | | **57** | **164** | **2.88** | **37,354** | **2,129,160** |

The framer's 164 tool calls plus the 8 case sessions' calls, one spawn
each, make the side's 172. The framer's 2,129,160 tokens are 72.0% of the
side's 2,956,842; the remaining 827,682 are the case sessions'. Both are
derived as the difference from the side's totals. The baseline's
per-request figures cannot be recovered, as `spec.md` says, so the
comparison with the baseline stays at the side level.

**When each skill was opened** (`executed`, the same count; bytes are the
tool result's, line-number prefixes included).

| Case | Run | `implement`'s three sections | `writing-style`'s `## English prose rules` | Also read |
|---|---|---|---|---|
| document-helpers | 0 | request 4, three `Read` ranges, 15,044 B | request 4, 2,693 B | — |
| document-helpers | 1 | request 4, three `Read` ranges, 15,044 B | request 5, 2,693 B | — |
| keep-trailing-space | 0 | request 3, three `Read` ranges, 15,044 B | request 3, 2,693 B | `## 구성 규칙`, request 4, 3,836 B |
| keep-trailing-space | 1 | request 6, one `sed -n` of all four, which exited 1 after the first section (1,625 B); read again at request 7 in one call with §*Reference specs* (16,800 B) | request 7, in that call | — |
| loud-flag | 0 | request 4, three `Read` ranges, 15,044 B | request 4, 2,693 B | `## 먼저` and `## 구성 규칙`, request 5, 5,357 B |
| loud-flag | 1 | request 6, three `Read` ranges, 15,044 B | request 6, 2,693 B | `## 먼저` and `## 구성 규칙`, request 7, 5,357 B |
| word-count | 0 | request 4, three `Read` ranges, 15,044 B | request 4, 2,693 B | `## 구성 규칙`, request 5, 3,836 B |
| word-count | 1 | request 4, two `sed -n` calls (7,247 B and 9,507 B) | request 4, in the second call | — |

- **S3.** All 8 runs opened `implement` by its three sections before
  writing the frame, and all 8 opened `## English prose rules` before
  writing. No run read either skill whole: no `Read` of either path without
  an offset, and no `sed` range covering a whole file.
- **The structure rules.** Four runs also read `writing-style`'s
  `## 구성 규칙`. The English section's first lines send a reader who opened
  it alone to that section, and to `## 먼저`.
- **The fallback.** The definition says to read the file whole where a
  heading is not found. No run took it.
