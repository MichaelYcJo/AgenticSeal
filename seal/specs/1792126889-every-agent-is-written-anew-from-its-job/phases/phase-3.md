# 1792126889-every-agent-is-written-anew-from-its-job — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 93c1878c (the build; the phase closes after the evaluation, and `plan.md`'s Status cell stays empty until then) |
| Ran by | specseal:smith on Opus 5.5 (spawn 3a, build only) |

## What this phase was asked

Build only; a separate spawn runs the four agents' sets after this one.
Write `skills/agent-contract/SKILL.md` anew: one opening paragraph, then
`§1`…`§N`, each a short rule paragraph with its `Enforced by:` line, no
incident histories, the four rules of `spec.md` §*Rules the rewrite states in
place*, §2 saying no agent runs the broad gate and the orchestrator runs it
before the sealer, and the "each agent's numbers" sentence made true. Write
the old-to-new section map, rewrite the contract citations with one one-shot
script asserting its counts, and rewrite `docs/the-agent-set.md`'s
section-number sentence to *from this edition*. Give `agents/warden.md`'s
record step one sentence: read the record through
`skills/code-review/scripts/chain_check.py` before handing back and correct
what it refuses. Plant T3, T4 and T5, each seen red first, run every module
that reads the contract or a rewritten citation, fix or remove the failing
pins, run `bin/rules --check` and `ruff` on the changed Python, commit, and
write this record.

## What this phase found

**The contract.** 20,368 B, 369 lines, 17 sections before; 16,537 B, 281
lines, 20 sections after. Every section ends in an `Enforced by:` line (the
old file had none, so there was no target to keep). What left: the "How the
sections are numbered" heading (its rule is now one sentence of the opening
paragraph), every measured incident (#30's worktree, #36's prompts, the 28
minutes, the 128 shell edits, the milestone-49 stops, the "sat in two
definitions" histories), and §3's, §5's and §6's explanatory paragraphs.
§9's gate grammar stays whole: `tests/test_edits_go_through_the_edit_tool.py`
pins it, and it is rule rather than history.

**Rules keep their numbers where they stay, rather than a new order.** The
plan says "§1 to §N in the new order" and fixes no order. Every renumbered
citation is a site to rewrite and a site a reviewer has to check, so the
order that moves the fewest is the one chosen: old §16 (where `seal/`
resolves) joins old §11 (the record language), since it existed only because
§11 could not be followed without it, and old §17 moves up to §16. The four
new rules are §17–§20. A reader wanting a grouped order can still have one;
it costs every citation in the tree, which this phase judged not worth it.

| Old | New |
|---|---|
| §1–§10 | §1–§10 (§2 rewritten: no agent runs the broad gate) |
| §11 | §11 (now also holds old §16) |
| §12–§15 | §12–§15 |
| §16 | §11 |
| §17 | §16 |
| none | §17 clean up only what you started |
| none | §18 a check that refuses correct code is fixed or reported |
| none | §19 a change rewrites the text it amends in place |
| none | §20 do not avoid the change a problem calls for |

**Citations.** Outside the contract, 20 `§16`/`§17` sites before
(`git grep -P "§1[67](?!\d)"`, excluding `seal/specs`, `changelog` and the
contract, the same 20 the 957-phase-3-survey `sites.txt` lists). One script made
17 exact substitutions, each asserted to match once, then was deleted. After it,
10 sites: 6 are the new §16 (the commit rule), 1 is a historical
"the old §16, now part of §11" in a measurement docstring, and 3 were pins
rewritten by hand below. Three sites read "contract §11 and §16 each record
…", and the contract no longer records that history, so they now say
"§11 was written to end" (§19's rule applied to its own rewrite). T3 reads
145 citations in 264 files (121 outside the contract), and none names a
section the contract lacks.

**§2 now contradicts the sealer until phase 5.** `agents/sealer.md`
§*Rules* ("The broad gate is yours. The contract's §2 leaves each definition
to say …"), `docs/the-broad-gate.md` §*One act, one owner*, `CONTRIBUTING.md`
line 108 and `agents/smith.md`'s "the sealer takes the broad gate once" still
state the old owner. Plan row 5 rewrites each of them with the gate's new
order, so they are left for it; only the dangling `Enforced by:` target in
`docs/the-broad-gate.md` was re-pointed here.

**The batching figures.** §10 now points each kind of segment at
`docs/the-review-record.md` §*The per-segment bars* and says no definition
states a second copy. T5 was red on `agents/smith.md` (1.08–1.17) and
`agents/framer.md` (1.4, and the 0.15.1 framers' 2.3–3.1), so this phase
removed the smith's item 5 and the framer's figure paragraph and one
sentence, and pointed the framer at its row. The framer's other
measurements, which carry no "tools per turn", are phase 4's.

**The warden's sentence.** `chain_check.py` refuses any finding that reads
`open`, and the warden writes `verdict: open` by rule, so the sentence names
that one refusal as the one the warden leaves standing. The command it names
is `python3 skills/code-review/scripts/chain_check.py --baseline <base> --worktree`.

**New cases, each seen red (exit 1):**

- T3 `test_every_cited_section_exists`, red with a planted `contract §21` in
  `skills/implement/orchestration.md:32`, then restored. Its can-fail cases
  plant one number above the last heading in four trees and spellings, and
  one keeps another file's `§N` in a definition from counting.
- T4 `test_the_four_rules_stand_with_their_enforcers`, red with
  "never kill by command name" deleted from §17, then restored.
- T5 `test_no_definition_states_a_tools_per_turn_figure`, red on the tree as
  it stood (smith and framer), green after their figures went.
- `mutation-check`, one break per new unit, each `red`: the other-file guard
  in `cited_sections`, the citation extraction in `cited_sections`, and the
  second alternative of `TOOLS_PER_TURN`.

**Pins changed (Q7: re-pointed where the rule stays, removed where it was
narration):**

- `test_the_agent_contract_holds_the_universal_rules.py`: PINS 2 to "No agent
  runs any of the three"; 16 to the commit rule's pin; 17–20 added;
  `test_the_root_resolution_rule_says_why_it_is_universal` replaced by
  `…_states_both_places` (the "why" was history);
  `test_the_method_lessons_moved_in` removed (it pinned the four incident
  stories).
- `test_a_commit_names_its_repository.py`: `section(17)` to `section(16)`;
  the "is the last section" assert removed (it held while §17 was newest).
- `test_a_probe_that_commits_says_so.py`: the `#36` incident pin removed.
- `test_broad_gate_rule.py`: `test_the_prohibition_itself_has_one_home…`
  re-pointed to the new §2; `test_the_smith_carries_the_batching_rule…`
  replaced by `test_the_implementers_bar_is_not_the_reviewers_and_has_one_home`;
  `test_only_one_definition_assigns_the_broad_gate` removed (it pinned
  §2's "One definition … does hand them over", which is gone; T7 in phase 5
  replaces it); the refusal pins moved to the new §3 wording; the unused
  `DASH` constant removed.
- `test_the_handoff_before_round_one.py`: the smith's-number test now
  asserts §10's pointer; `test_the_framers_definition_carries_its_own_number`
  replaced by `…_points_at_its_bar`.
- `test_a_moved_rule_leaves_its_definition.py`: the smith's "1.08–1.17" and
  "§10's number for you" kept-application pins removed.

**Verified (executed):**

- The 69 modules `git grep -l -E "agent-contract|§[0-9]" -- tests` names, run
  together with `-n auto` after the last pin fix: 4525 passed, 15 skipped,
  1 failed (`test_docs_line_wrap.py` on one contract line this phase broke).
  After the rewrap, that module with the two contract modules: 111 passed,
  exit 0.
- The eight modules whose pins changed: 353 passed, 4 skipped, exit 0.
- `bin/rules --check`: exit 0, all 463 targets in 60 rule files resolve.
- `uvx ruff check` and `uvx ruff format --check` over the ten changed
  Python files: exit 0 both.

**Not run here:** the four agents' evaluation sets (`evals/<agent>-phase-3.md`)
are the next spawn's, and the full suite is the orchestrator's, after the
rounds settle.

## The evaluation (spawn 3b)

Asked: run the sealer's, the smith's, the framer's and the warden's sets
once each, in that order, paid, against the build at 93c1878c with the suite
at af9c924b and the baselines as they stand; keep each side's raw output in
`SpecSeal-worktrees/957-phase-3-raw/<agent>/`; write `evals/<agent>-phase-3.json`
by `run --from-raw` and `evals/<agent>-phase-3.md` by `compare`; stop before
the next agent past $90; re-run only on a named transient; change no rule and
no definition. Ran by specseal:smith on Opus 5.5.

**Two verdicts read `pass` and two read `fail`.** The smith and the warden
pass. The framer fails rule 5 alone. The sealer fails rules 3 and 5, and its
record is not the sealer's result (below). Nothing was cut short, every side
read `partial: false`, and nothing was re-run: neither failure has a
transient cause to name.

| | sealer base | sealer 3 | smith base | smith 3 | framer base | framer 3 | warden base | warden 3 |
|---|---|---|---|---|---|---|---|---|
| Verdict | | fail (3, 5) | | pass | | fail (5) | | pass |
| Truth finds (recall) | 4 of 4 | 3 of 4 | none | none | none | none | 13 of 24 | 16 of 24 |
| Report rows / false rows | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 55 / 43 | 47 / 31 |
| False rate | 0 | 0 | 0 | 0 | 0 | 0 | 0.782 | 0.660 |
| Shape and reach passes | 30 of 30 | 29 of 30 | 48 of 48 | 48 of 48 | 64 of 64 | 64 of 64 | 66 of 72 | 70 of 72 |
| Preload bytes (agent share) | 28,358 | 24,527 | 94,693 | 90,594 | 93,453 | 89,310 | 76,019 | 27,032 |
| Tool calls, every `tool_use` block | 97 | 84 | 197 | 183 | 112 | 141 | 746 | 833 |
| Tokens per tool call (rule 5) | 34,268.9 | 36,861.5 | 45,574.6 | 45,194.4 | 28,253.1 | 33,595.1 | 89,100.4 | 80,940.4 |
| Tokens read, every model | 3,324,087 | 3,096,365 | 8,978,191 | 8,270,573 | 3,164,345 | 4,736,908 | 66,468,871 | 67,423,379 |
| Tokens per true find | 831,022 | 1,032,122 | unknown | unknown | unknown | unknown | 5,112,990 | 4,213,961 |
| Spend USD | 3.0366 | 4.0836 | 6.3830 | 5.9980 | 16.5896 | 17.3532 | 36.0352 | 36.6656 |
| Session seconds | 577.2 | 578.6 | 1,144.5 | 1,320.6 | 1,875.0 | 2,027.6 | 5,779.5 | 6,807.8 |
| Eval wall seconds | 194 | 1,244 | 305 | 409 | 565 | 627 | 1,602 | 1,860 |

Every figure but the wall seconds is `noninferiority.py#side_numbers` over the
committed side files (`summary.py`, a scratch script); the tool calls agree
with a separate count of every `tool_use` block in the kept traces (sealer
84, smith 183, framer 141, warden 833, and the baselines' 97, 197, 112, 746).
The wall seconds are each eval's `durationSeconds`.

**The phase's spend is $64.1004** (sealer 4.0836, smith 5.9980, framer
17.3532, warden 36.6656). The running total never neared the $90 stop.

**`payload-meter` at ab2dda7c** (no file under `agents/` or `skills/` changed
after 93c1878c), each total holding the 13,318 B `CLAUDE.md` pair:

| Agent | Preloaded files, bytes | Total bytes | Tokens, estimated |
|---|---|---|---|
| sealer | `agents/sealer.md` 7,990; contract 16,537 | 37,845 | 11,827 |
| smith | `agents/smith.md` 20,829; contract 16,537; `implement` 32,228; `writing-style` 21,000 | 103,912 | 32,472 |
| framer | `agents/framer.md` 19,545; contract 16,537; `implement` 32,228; `writing-style` 21,000 | 102,628 | 32,071 |
| warden | `agents/warden.md` 10,495; contract 16,537 | 40,350 | 12,610 |

### The sealer: measured against a definition the contract now contradicts

**Not to be read as the sealer's result.** `agents/sealer.md` still says the
broad gate is the sealer's, and the new contract's §2 says no agent runs it;
phase 5 rewrites the sealer with the gate before it and measures the sealer
for decision. The orchestrator dropped the sealer from this phase while the
run was in flight and, on finding it had already finished (exit 0, $4.08,
1,244 s, not partial), kept this record under that label.

What the record says, as read: rule 3, `rule-sealer-untrue-body/shape-verdict`
1/2 against 2/2, and rule 5, 36,861.5 tokens per call against 34,268.9.
Recall fell by one find (`truth-untrue-body` 1/2), which rule 1 reads as
noise.

**What the runs did about the gate** (`gate.py` over both sides' traces): in
6 of 6 runs on each side, the sealer's first act after locating the clone
was `broad-gate --base main --record <item>`. The contract's new §2 did not
stop it. Every first call on both sides exited 134: the eval sandbox blocks
the pyenv interpreter's library (`libpython3.12.dylib ... blocked by
sandbox`). On the baseline all six runs worked round it with a shim to
another interpreter and reached `SEALED` (2 or 3 gate calls each). On the
new side five did; run 004 (`rule-sealer-untrue-body`, run 0) made one gate
call, read the refusal, re-ran the phase record's seen-red claim itself,
found the pull request body's untrue README claim, and then wrote no
`guarantee.md`, handing back that no verdict can be recorded without the
gate. That one run is both rule 3's shortfall and the lost find. Rule 5
does not rest on it: its 33,992 tokens per call are below the side's
figure, and the other five runs read 34,937 to 39,202 against the
baseline's 29,518 to 36,481 (`permodel.py`). Whether the new §2 shaped that stop is not
measured: `unverified`, answerer phase 5's measurement. The sandbox's
interpreter refusal is the same on both sides and in every run, so it is
not a transient this spawn could re-run away.

### The smith: `pass`

Every grader passed on every run on both sides, the preload fell 4,099
bytes, calls fell 197 to 183, and tokens per call fell 0.8%. No smith run on
either side ran a broad check (`broad-gate`, a whole-suite `unittest
discover`, `pytest`, `ruff` or `mypy`): 0 commands on both.

### The framer: `fail`, rule 5 alone

Every grader passed on every run on both sides, and the preload fell 4,143
bytes. Rule 5: 33,595.1 tokens per call against 28,253.1 (+18.9%), with
calls up 112 to 141 (+25.9%) and total tokens up 49.7%. Every token is the
one model's (`claude-fable-5-1`) on both sides.

What it points at, read from the traces: the new side's runs explored more.
Bash calls rose 26 to 42 and Reads 47 to 54, and the new runs opened files no
baseline run opened: `docs/the-record-layout.md` 7 times (grepping its
changelog-fragment rules), the contract 3 times, `templates/sdd-routing.md`,
`sdd-overview.md`, `seal-README.md`, `config.md` and `sdd-changelog.md`.
No sentence in the framer's preload names `the-record-layout.md` or the
changelog fragment at either revision (`git grep` over `agents/framer.md`
and the contract), so which change drove the exploration is not shown.
Tokens per call grow with the calls a run makes, since each call carries the
context before it, so more exploration raises rule 5's figure as well as the
total. The per-run figure is wide on both sides (baseline 19,415 to 54,983
tokens per call; new 24,258 to 66,117) over two runs a case. `unverified`,
answerer the orchestrator: whether phase 4's rewrite of the framer is where
this is answered.

### The warden: `pass`, and the questions phase 2 left

**Phase 2's failing grader does not recur.** `seeded-9b644676/shape-findings`
passed 2/2 (run 2 of phase 2: 1/2). **No record with a finding lacks its
`verdict:` line**: in all 18 printed records the `### <n>.` findings equal the
`verdict:` lines (`scan.py`; phase 2's run 2 had three records short, one of
them with none). Two records hold no finding at all, both
`replay-1791779434-r5` (a verifying round whose records confirm earlier
findings and open none). That grader was 0/2 on the baseline as well, and
it is the side's only shortfall: 70 of 72.

**The warden reads its record through `chain_check.py` in every run.**
Counted from the traces (`ccorder.py`): 39 agent calls run
`chain_check.py … --worktree`, in 18 of 18 runs, and in every run at least
one comes after the agent's first write of the round record. The baseline
made 0 such calls in 18 runs, and phase 2's run 2 made 1 in 1 run. Those 39
calls account for 39 of the 87 calls the side added over the baseline;
tokens per call still fell 9.2%.

Recall is 16 of 24 as in phase 2 (three finds up on the baseline net), the
false rate 0.660 against the baseline's 0.782 (phase 2's run 2: 0.564), and
the preload 27,032 bytes against 76,019.

### `plan.md`'s Status cell for phase 3 stays empty

Its Verified-by cell asks for all four records reading `pass`. Two read
`fail`, and the orchestrator decided (2026-10-17) that the sealer is measured
in phase 5, so the cell stays empty: sealer measured in phase 5, and the
framer's rule 5 is the orchestrator's call.

### Commands, each with its exit code

`$S` is the session scratch directory's `957-phase-3b/`, `$K` is
`SpecSeal-worktrees/957-phase-3-raw/`, `$E` is this work item's `evals/`.

| Command | Exit |
|---|---|
| `python3 evals/scripts/noninferiority.py run --agent <a> --rev 93c1878c --suite-rev af9c924b --out $S/<a>-phase-3.json --runs 2 -j 4`, for sealer, smith, framer, warden | 0 each |
| `cp -R $S/<a>-phase-3.raw $K/<a>/`, with the run's log as `run.log` | 0 each |
| `noninferiority.py run --from-raw $K/<a>/<a>-phase-3.raw --out $E/<a>-phase-3.json`, then `cmp` with `$S` | 0, 0 each |
| `noninferiority.py compare --agent <a> --phase 3 --old $E/baseline-<a>.json --new $E/<a>-phase-3.json --out $E/<a>-phase-3.md` | 0 each: sealer `fail`, smith `pass`, framer `fail`, warden `pass` |
| `noninferiority.py check $E/<a>-phase-3.md` | sealer 1, smith 0, framer 1, warden 0 |
| `bin/payload-meter --agent <a>` | 0 each |
| `python3 -I $S/scan.py`, `gate.py`, `ccorder.py`, `summary.py`, `permodel.py` over the kept sides and the baselines | 0 each |

The scratch scripts were deleted with `$S`; what they counted is above.
