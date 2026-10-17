# 1792126889-every-agent-is-written-anew-from-its-job — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | f5a71276 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Take the baseline once, at one reference, tree and suite both at af9c924b
(`release/v0.22.1` after #964 merged; the branch at 05d4a70d). For warden,
smith, framer and sealer, one agent at a time and the sealer first,
`noninferiority.py run --agent <a> --rev af9c924b --suite-rev af9c924b
--runs 2 -j 4` with the default `--max-cost-usd`. Keep the raw output
outside the tree and commit the four `evals/baseline-<a>.json` files. Stop
before the next agent if the running spend passes $100, or if one agent's
runs project the four-agent total past it. Answer `questions.md` Q4, Q5 and
Q6 from what the runs wrote. Touch nothing under `agents/`, the contract, any
skill or the harness; if the harness cannot run as the plan says, stop and
hand back.

## What this phase found

**The frame holds.** The cases at af9c924b, recounted with `git ls-tree`,
are 20: warden 9, smith 4, framer 4, sealer 3, scribe none. That is the
frame's count, so a full pass is 40 runs. Nothing under `evals/`, `agents/`
or `skills/` differs between af9c924b and 05d4a70d, so the harness that ran
is the harness at the reference. Each side records suite commit af9c924b
and its agent's suite tree (sealer `2ef872f0`, smith `613190e8`, framer
`62f007f6`, warden `d8dfd549`).

**The raw output went outside the tree by a second command, not by the
command as written.** `run` saves the paid output to `<out>.raw/` beside
`--out`. The command with `--out seal/specs/<id>/evals/baseline-<a>.json`
would have put the raw directory, with its traces, inside the tree. So each
side ran with `--out` in the scratch directory, and the in-tree file was
written by `run --from-raw <scratch>/baseline-<a>.raw --out
seal/specs/<id>/evals/baseline-<a>.json`. `cmp` against the file `run` itself
wrote exits 0 for all four. The JSON in the tree is byte for byte what `run`
wrote.

**Nothing was cut short, and the spend stopped well under the bound.** All
four sides read `cut_short: false` and `partial: false`, and no run carries
an `error`. Nothing was rerun. After each agent the running spend was $3.04,
$9.42, $26.01 and $62.04. Every agent's runs projected the four-agent total
under $100, so the stop rule never fired.

| Agent | Cases | Runs | Cut short | Spend USD | USD per run | Session seconds | Eval wall seconds | Tokens read (harness) | Tokens read (all models) | Preload bytes |
|---|---|---|---|---|---|---|---|---|---|---|
| sealer | 3 | 6 | no | 3.0366 | 0.5061 | 577.2 | 194 | 255,424 | 3,324,087 | 28,358 |
| smith | 4 | 8 | no | 6.3830 | 0.7979 | 1,144.5 | 305 | 333,442 | 8,978,191 | 94,693 |
| framer | 4 | 8 | no | 16.5896 | 2.0737 | 1,875.0 | 565 | 366,118 | 3,164,345 | 93,453 |
| warden | 9 | 18 | no | 36.0352 | 2.0020 | 5,779.5 | 1,602 | 1,265,634 | 66,468,871 | 76,019 |
| **total** | 20 | 40 | no | **62.0444** | 1.5511 | 9,376.2 | 2,666 | 2,220,618 | 81,935,494 | |

Where each column comes from:

- **Spend, session seconds and tokens read (harness)** are
  `noninferiority.py#side_numbers` over the committed file: the sums of
  `total_cost_usd`, `duration_ms` / 1000 and `tokens_read(usage)`.
- **Eval wall seconds** is the eval JSON's top-level `durationSeconds`. The
  runs went four at a time, so it is shorter than the session sum.
- **Tokens read (all models)** is not in the committed file. It is the input,
  cache-read and cache-creation tokens of every model under the session
  `result` event's `modelUsage`, summed over the saved traces (the finding
  below says why).
- **Preload bytes** is the side's `specseal.preload_bytes`: the definition
  plus its `skills:` list, without the `CLAUDE.md` pair. The sealer and warden
  figures equal the frame's d4552372 readings. The smith reads 94,693
  against the frame's 94,493, and the framer 93,453 against 93,195: #964
  changed those preloads, and the baseline is at its tree.
- **The eval's own per-run `costUsd` equals `total_cost_usd`** in every run
  read (the sealer's six, by printing both). The top-level `costUsd` equals
  each side's spend to the fourth place.

**Outcome on the baseline, which phase 2 is judged against.**

- **Sealer:** every grader passed in all 6 runs. Truth finds are 4 of 4.
- **Smith:** every grader passed in all 8 runs. It has no truth grader.
- **Framer:** every grader passed in all 8 runs. It has no truth grader.
- **Warden:** truth finds are 13 of 24, and the report rows are 55, 43 of
  them false (rate 0.782). Five shape graders fell short on the baseline
  itself:
  - `replay-1791384160-r2`: `shape-findings` 1/2, `shape-words-only` 1/2
  - `replay-1791779434-r5`: `shape-findings` 0/2, `shape-words-only` 1/2
  - `seeded-279a580b`: `shape-words-only` 1/2

  Rule 3 of `noninferiority.py#verdict` reads the new side alone and demands
  every shape grader pass in every run. So a phase 2 warden that does exactly
  what the baseline did fails rule 3 on these three cases. That is a property
  of the harness and the cases, which this phase does not touch. Phase 2
  meets it first, and its answerer is the orchestrator, who decides before
  phase 2 runs whether the rule or the cases change. The phase 2 record must
  not be read as a defect of the rewrite if this alone fails it.

**The harness's token figure is the outer session's, not the agent's (Q5).**

- `run_cost` reads `usage` from the session's last `result` event, and that
  `usage` counts only the case session that spawns the agent. The spawned
  agent's tokens are absent from it. They appear only in the same event's
  `modelUsage`, keyed by model, and in the subagent's own assistant events,
  which carry `parent_tool_use_id`.
- The spend does include the agent: in the sealer's first run,
  `total_cost_usd` 0.5500 is `modelUsage`'s Sonnet 0.0662 plus Opus 0.4838.
- So the harness's "tokens read" is 7.7% of what the sealer side read, 3.7%
  of the smith's, 11.6% of the framer's and 1.9% of the warden's. It barely
  moves with the preload this item rewrites.
- Rule 4's token half therefore judges the case session rather than the
  agent; its spend half judges both. That is the harness's reading as it
  stands, and this phase changes none of it. Whether the token rule should
  read `modelUsage` is the orchestrator's to decide before phase 2, and it is
  open in the hand-back. Q8, the real tokens a spawn reads, is also answered
  by `modelUsage` and not by `usage`.

**The trace names the model of every turn, and the definition's `model:` is
honoured (Q6).**

- Every assistant event carries `message.model`. In the sealer's six runs the
  case session's turns read `claude-sonnet-5-5`, which is the case's
  `execution.model`. Every subagent turn (the `parent_tool_use_id` events)
  reads `claude-opus-5-5`, which is `agents/sealer.md`'s `model: opus`.
- The session `result` event's `modelUsage` names both models with their
  `costUSD`, and its `subagent_stats.by_type` reads `{"specseal:sealer": 1}`.
- Every run of every agent spawned exactly one agent of its type.
- For the warden and the smith both sides of the boundary are Opus, and for
  the framer both are Fable 5.1, as `rule_cases.py#MODELS` and the
  definitions set them. So varying `agents/sealer.md`'s `model:` alone does
  vary the model the sealer runs on.

**What the remaining runs will cost, at the baseline's prices (Q4).** The
plan's 126 runs are the baseline's 40 ($62.04), the warden's 18 ($36.04), the
contract's 40 ($62.04), the smith's and the framer's 16 ($22.97) and the
sealer's 12, which is two sealer sides at up to $3.04 each. That totals
**at most $189.17**, against the owner's estimate of about $150; $127.13
of it comes after this phase. A rewrite that shrinks a preload should cost
less than the baseline, and a Sonnet sealer side should cost less than an
Opus one, so the figure is an upper bound at these prices and nobody's
measurement of the later phases.

**The emoji in `baseline-warden.json` are the suite's, copied as data.**
The file holds 50 emoji characters. Forty-five are in the nine copies of
the `shape-words-only` grader's regex, whose range is written in literal
characters. The other five are in three cases' `promptMarkdown`, which
quotes the old records the replays read. No test refuses an emoji in a file under `seal/specs/`, and five
text-reading modules pass with the four files staged (below).

**What was left outside the tree.** The four `baseline-<a>.raw/` directories
(the eval's `raw.json`, `meta.json` and every trace) and `table.py`, which
recomputes this table from them, stay in the session scratch directory at
`957-phase-1/`. The kept eval directories under `/private/tmp/e-*` were
removed by the harness itself; none remains.

### Commands, each with its exit code

Read directly with `; echo $?`, never through a pipe. `$S` is the session
scratch directory's `957-phase-1/`; `$E` is this work item's `evals/`.

| Command | Exit |
|---|---|
| `git ls-tree -d --name-only af9c924b evals/behaviour/<a>/` for each agent | 0 (9, 4, 4, 3, 0) |
| `git diff --stat af9c924b HEAD -- evals agents skills` | 0, empty |
| `python3 evals/scripts/noninferiority.py run --agent sealer --rev af9c924b --suite-rev af9c924b --out $S/baseline-sealer.json --runs 2 -j 4` | 0 |
| the same for `smith` | 0 |
| the same for `framer` | 0 |
| the same for `warden` | 0 |
| `python3 evals/scripts/noninferiority.py run --from-raw $S/baseline-<a>.raw --out $E/baseline-<a>.json`, four times | 0 each |
| `cmp $S/baseline-<a>.json $E/baseline-<a>.json`, four times | 0 each |
| `bin/test tests/test_no_real_identifiers.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_no_document_names_the_old_roots.py tests/test_one_word_one_meaning.py tests/test_no_shape_the_base_stops_reads_silent.py -q -p no:xdist`, the four files staged | 0, 102 passed |
| `git commit` of the four files | 0, f5a71276 |

The sides stand on af9c924b (tree and suite) and were run from the branch at
05d4a70d. The four files are committed at f5a71276, and this record and the
answers in `questions.md` and `plan.md` are in the commit after it.
