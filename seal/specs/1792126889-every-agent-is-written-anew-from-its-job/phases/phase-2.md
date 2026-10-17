# 1792126889-every-agent-is-written-anew-from-its-job — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 71a50320 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Prove the approach on one file, the warden. Write `agents/warden.md` anew to
`spec.md` §*The shape of a definition*: `skills: [agent-contract]` only, step
1 opening `skills/code-review/SKILL.md`, the record step opening the section
of `skills/writing-style/SKILL.md` for the record's language, the warden's
rules kept as `## Rules` paragraphs (the branch worktree's record path, each
new test read against its group, the verifying round, the carried-fact
table, the clone, the probe rules), the batching number gone, no emoji, no
proof block. Write `skills/code-review/SKILL.md` anew to the same shape: two
stages, the axes, probes against regression tests, the record pointing at
`templates/sdd-round.md` and the grammar table without restating it, no proof
block, one pointer line to the orchestrator's half, and the `answer:` line
#964's grammar now demands. Recount the pins on the two files, re-point those
on a rule that stays and remove those on narration (Q7). Rewrite
`tests/test_every_agent_reads_the_contract.py` to S1 and S2 (T1, T2), green on
the warden and skipped by name for the other four until phase 5. Commit the
rewrite, then run the warden set once, paid, against `evals/baseline-warden.json`
with the suite at af9c924b, and write `evals/warden-phase-2.md` with
`compare`. One paid run; a `fail` is recorded and handed back, not reworked.

Continued after the owner's decision on run 1 (2026-10-17), unattended: make
rule 5 tokens across every model per tool call, a tool call being every
`tool_use` block of a run's trace, no count being no result, total tokens,
per true find, spend and seconds recorded and judging nothing, test-first
with `mutation-check` on the comparison; re-derive the four baselines and
run 1's side at no cost and keep run 1's record as
`evals/warden-phase-2-run-1.md`; fix the two defects run 1 found (a finding
with no `verdict:` line, a quoted emoji) by pointing at the grammar table's
rows, adding as little as a spawn pays for; run the warden set once more,
paid, stop rule $50, and close the phase in `plan.md` on `pass` or hand
back on `fail` with no further run.

## What this phase found

Two paid runs of the warden set, with a rule change and two fixes to the
definition between them. Run 1 judged the rewrite at 71a50320 under the
rules of phase 1b, and read `fail`; the owner then changed rule 5 to tokens
per tool call (2026-10-17, `spec.md` §*How the rewrite is proved not
worse*), run 1 was re-read under it at no cost, and run 2 judged the
rewrite with the two fixes at 71bafe0f.

### Run 1, at 71a50320

**Run 1 read `fail`, and the outcome improved.** Its record is now
`evals/warden-phase-2-run-1.md`, its side `evals/warden-phase-2-run-1.json`,
both re-derived from the kept raw output under the per-call rule (below);
the first record, written under phase 1b's rules, stands at 9e82c320.

| | Baseline (af9c924b) | Run 1 (71a50320) |
|---|---|---|
| Truth finds (recall) | 13 of 24 | 17 of 24 |
| Report rows / false rows | 55 / 43 | 44 / 28 |
| False rate | 0.782 | 0.636 |
| Shape and reach grader passes, of 36 graders × 2 runs | 66 of 72 | 66 of 72 |
| Preload bytes (agent share) | 76,019 | 30,508 |
| Tokens read, every model | 66,468,871 | 78,306,931 |
| Tool calls, every `tool_use` block | 746 | 890 |
| Tokens per tool call | 89,100.4 | 87,985.3 (-1.25%) |
| Tokens per true find | 5,112,990 | 4,606,290 |
| Spend USD | 36.0352 | 40.3114 |
| Session seconds | 5,779.5 | 7,576.1 |
| Eval wall seconds | 1,602 | 2,046 |

**The call count this record first gave was wrong, and two figures in the
frame stand on it.** This record's first version and the hand-back gave the
agent's tool calls as 954 against 710 (+34%), a sum made by hand over
`per_run.py`'s lines. The traces hold 854 against 710 (+20.3%) for the agent
alone, and 890 against 746 (+19.3%) for every `tool_use` block, the session's
36 on each side included (`calls.py` over both kept raw directories). So
tokens per tool call fell 1.25% in run 1, not the 12.3% `spec.md`
§*How the rewrite is proved not worse* quotes, and "34% more calls" there is
20.3%. Rule 5 passes on either figure. The sentence is the frame's, so it is
named here and in the hand-back rather than rewritten.

The truth finds rose in two replays and one seeded case and fell in none.
The shape and reach passes are 66 on both sides, but not the same 66: all
five baseline shortfalls phase 1 named passed on both new runs, and six new
ones stand in the seeded cases, below.

**Each failing rule of run 1, and what in the rewrite it pointed at.**

- **Rule 3, `shape-findings`, four seeded cases (279a580b 1/2, 4d316179 1/2,
  9b644676 0/2, ad447367 1/2, each 2/2 on the baseline).** Five of the 18
  records carry no `verdict:` line at all, and every one of the five carries
  its `answer:` lines (runs 011, 013, 014, 015, 017 of the saved traces;
  counted with `grep -c '^verdict:'` over each record the session printed).
  The grader requires a finding's `verdict:` line. The rewrite names
  `answer:` in both files and leaves `verdict: open` to the grammar table
  and the template, where the old `agents/warden.md` §Report spelled the
  three lines a finding holds, `verdict: open` among them. It points at
  `skills/code-review/SKILL.md` §*The record* and the warden's step 7, which
  name the `answer:` line and not the `verdict: open` line.
- **Rule 3, `shape-words-only`, seeded-9b644676 (1/2, 2/2 on the baseline).**
  Run 014's record quotes the code under review's old marks (U+1F7E1 and
  U+2B1C, each with a number) in a finding's heading and grounds. Both files forbid an emoji in the
  record; neither says that a mark quoted from the code is spelled in words.
  The old definition did not say it either, and the baseline fell short on
  the same grader in three other cases (phase 1).
- **Rule 5 as phase 1b had it, total tokens, 78,306,931 against 66,468,871
  (+17.8%).** The preload fell by 45,511 bytes and the calls rose 19.3%.
  Opening the four plugin files at their steps is four or five calls a run,
  where the baseline's runs opened the template and the review-record
  document in one or two, so about 40 of the 144 extra calls, an estimate
  from `per_run.py`'s listing of which files each run opened. The rest is
  review depth, which is also where the four extra truth finds and the
  fifteen fewer false rows came from. Under the per-call rule run 1 passes
  rule 5. Which sentence drove the depth is not measured: `unverified`,
  answerer the orchestrator.

### The rule change, and run 1 re-read at no cost

**Rule 5 reads tokens across every model per tool call** (8dad1b29).
`noninferiority.py#tool_calls` counts every `tool_use` block a run's trace
holds, the session's and the agent's, a block an event repeats counted once
by its id (none repeats in the 58 saved warden, smith, framer and sealer
traces: `calls.py` printed equal all and unique counts); a trace that cannot
be read or holds none gives no count, and the side is no result. The verdict
compares cross-multiplied, `new_tokens * old_calls >= old_tokens *
new_calls` failing, so equal figures compare equal. The record writes tool
calls, tokens per tool call and tokens per true find, the last two derived
for a reader and not read back; total tokens, per find, spend and seconds
judge nothing. `evals/README.md`, the module's and the test module's
docstrings are rewritten in place; `git grep` for the old sentences
("the spawned agent's included, are", "Spend and wall seconds are written",
"short of a count is no result") finds nothing in `tests` or `evals`.

**The four baselines and run 1's side, re-derived** (cd244ff0) by
`run --from-raw` from `SpecSeal-worktrees/957-baseline-raw/` and
`957-phase-2-raw/`. `keydiff.py` against the committed files finds one added
path per run and nothing else: `specseal.tool_calls`, 18 in the warden's, 8
in the smith's, 8 in the framer's, 6 in the sealer's and 18 in run 1's. The
tool calls per side: warden 746, smith 197, framer 112, sealer 97.

**Run 1 re-read reads `fail`, on rule 3 alone**: the five shape graders
above; rule 5 passes at 87,985.3 tokens per call against 89,100.4.

### The two fixes (71bafe0f)

- The warden's step 7 names the four lines every finding holds,
  `severity:`, `location:`, `verdict: open` and `answer:`, and
  `skills/code-review/SKILL.md` §*The record* names them as the rows the
  grammar table places in a finding as `one`.
- Both files say a mark quoted from the code under review is written as its
  code point or in words, never as the character.

`agents/warden.md` is 163 lines and 10,252 B after them, and
`skills/code-review/SKILL.md` 157 lines and 9,302 B; the preload is 30,620 B.

### Run 2, at 71bafe0f: `fail` on one grader, every other figure better

The record of the phase is `evals/warden-phase-2.md`, its side
`evals/warden-phase-2.json` (`--from-raw`, `cmp` identical to the scratch
file), the raw output kept at `SpecSeal-worktrees/957-phase-2b-raw/`. Per
the spawn, no third run.

| | Baseline (af9c924b) | Run 2 (71bafe0f) |
|---|---|---|
| Truth finds (recall) | 13 of 24 | 16 of 24 |
| Report rows / false rows | 55 / 43 | 39 / 22 |
| False rate | 0.782 | 0.564 |
| Shape and reach grader passes, of 36 graders × 2 runs | 66 of 72 | 70 of 72 |
| Preload bytes (agent share) | 76,019 | 30,620 |
| Tool calls, every `tool_use` block | 746 | 826 (+10.7%) |
| Tokens per tool call (rule 5) | 89,100.4 | 85,317.2 (-4.2%) |
| Tokens read, every model | 66,468,871 | 70,472,015 (+6.0%) |
| Tokens per true find | 5,112,990 | 4,404,501 (-13.9%) |
| Spend USD | 36.0352 | 37.8482 |
| Session seconds | 5,779.5 | 6,669.7 |
| Eval wall seconds | 1,602 | 1,841 |

**The one failing rule.** Rule 3: `seeded-9b644676/shape-findings` passed
1/2 against the baseline's 2/2. Run 014's record holds three findings, each
with `severity:`, `location:` and `answer:` and none with a `verdict:` line,
although that run opened `skills/code-review/SKILL.md`,
`templates/sdd-round.md` and the grammar table under the plugin root before
it wrote. So the fix took the omission from five records of 18 to one, and
did not end it. What it points at: the `verdict: open` line is named in the
warden's step 7 and the skill's record section, and once in 18 runs the
agent still left it out; nothing between the write and the hand-back
checks the record against the table. `unverified`, answerer the
orchestrator: whether a sentence can close it or a check at the hand-back
must.

**Everything else held or improved.** Recall rose by three finds net (four
cases up, one replay down one find, inside rule 1's noise), the false rate
fell from 0.782 to 0.564, rule 5 passes, and the other short graders
improved: `replay-1791779434-r5/shape-findings` went from 0/2 to 1/2 (its
run 007 wrote a record with no finding at all) and every other shortfall the
baseline had passed on both runs. No record of run 2 quotes an emoji
(`shape-words-only` 18 of 18).

**`plan.md`'s Status cell for phase 2 stays empty.** Its Verified-by cell
asks for `evals/warden-phase-2.md` reading `pass`, and it reads `fail`. The
rewrite stands at 71bafe0f, and whether phase 2 closes on this record is the
orchestrator's call.

**This step's spend** is $37.8482, run 2 alone; the rule change and the
re-derivations ran nothing paid. Phase 2's two runs together spent $78.1596.

**The plugin-root path works.** Every new run opened
`skills/code-review/SKILL.md`, `skills/writing-style/SKILL.md`,
`templates/sdd-round.md` and `docs/the-review-record.md` under the extracted
plugin tree; the replay clones carry older copies of all four, and the
baseline's runs read those (`per_run.py`'s `@repo`). The warden read
`writing-style` by section (`sed -n` over the `## English prose rules`
range), not whole.

**The frame holds, with one class it did not name.** `spec.md` §*The shape
of a definition* item 6 closes each rule with an `Enforced by:` line, and
`tests/test_docs_line_wrap.py` held such a line outside a fold statement to
88 columns, which one `path::test` target passes. The check refused the
shape; it was fixed, not the shape bent (the overview's divergence row).
The README rows and the two `docs/` `Enforced by:` lines are the other
sentences that stood on the warden's preload and the old case names.

**Decisions the frame left open, with their grounds.**

- **Where a step's path resolves.** In every eval case the clone is a
  repository that may hold its own `skills/`, `templates/` and `docs/`, the
  replays an older SpecSeal. Step 1 says those paths are the plugin's, two
  directories above the base directory the harness prints with the
  contract. Grounds: the traces above.
- **The record path rule says "at the path your prompt names, and never the
  main checkout"**, not "never the clone": in every eval case the prompt
  names the clone as the branch's tree.
- **The broad gate's owner leaves the warden.** The warden names the command
  and its record (`broad-gate`, `broad-gate.md`), not an agent, because
  phase 5 moves the run from the sealer to the orchestrator; the two owner
  pins in `tests/test_the_seal_is_taken_once_by_the_sealer.py` now read the
  smith alone.
- **The writing-style step names two sections**, `## English prose rules`
  and `## 문장 규칙`, by the record's language.
- **The applied-skill line of `overview.md`** is written as `implement
  applied` without the emoji the template's header carries; the template is
  phase 4's.

**For phase 3, a sentence this phase made false.** Contract §10 says the
numbers that judge each agent's batching are in that agent's definition. The
warden's number left with this phase (S6); the contract is phase 3's.

### The pins (Q7), recounted

Modules naming `agents/warden.md` by path: 23; naming
`skills/code-review/SKILL.md`: 6 (`git grep -l` over `tests`, both as the
frame counted). The readers are wider: 57 modules reach an agent definition
or a skill by any spelling, and after the rewrite 16 of them failed on 20
cases, beside the one failure that predates this phase
(`test_every_spec_directory_that_reached_the_ladder_has_an_overview`, closed
by this commit's `overview.md`).

Re-pointed, the rule staying:

- `tests/test_every_agent_reads_the_contract.py` rewritten to T1 and T2; the
  bounds case kept; the four `PINS` sentences, the identity case and the
  bare-name case replaced by T1, which holds the one sentence exactly.
- `test_a_moved_rule_leaves_its_definition.py::test_a_citation_is_not_a_copy`:
  the §9 application re-pointed to the new sentence.
- `test_one_word_one_meaning.py::test_the_two_definitions_name_what_they_actually_keep`:
  the warden half now reads that the reviewer never writes its own mark.
- `test_review_axes.py::test_a_later_round_inherits_no_verdict_anywhere`:
  extended over the warden's carried-fact table.
- `test_the_record_is_written_in_words.py::test_the_template_the_format_and_the_two_definitions_carry_no_emoji`:
  reads `## The record`; its proof-block exemption left with the block.
- `test_a_parallel_agent_names_its_scratch_after_the_work_item.py::test_the_wardens_clone_is_named_for_the_work_item_and_the_round`:
  reads `## Rules`.
- `test_docs_line_wrap.py`: the skip of a rule file's line of targets, and
  its new case.
- `test_the_seal_is_taken_once_by_the_sealer.py`: the two owner cases read
  the smith alone.
- `docs/the-agent-set.md` and `docs/the-broad-gate.md`: `Enforced by:`
  re-pointed to T1.
- Both READMEs: the warden's row lists `agent-contract`, and the skills row
  counts four preloaded and twelve loaded on demand, `code-review` among them
  (`test_chain_hooks_hardening.py`'s two README cases).

Removed, one line each, because the sentence was narration:

- `test_a_probe_that_commits_says_so.py`: "left a git worktree behind", the
  incident behind the leavings rule, which `code-review` no longer tells.
- `test_the_handoff_before_round_one.py::test_the_reviewers_contract_expects_batched_reads_and_probes`:
  the 1.89 figure and the batching sentence, which are §10's and the
  per-segment table's (S6).
- `test_a_moved_rule_leaves_its_definition.py`: the `1.89` kept phrase.
- `test_one_word_one_meaning.py`: "You keep the review mark" and "the commit
  gate can be waived without one", the opening's description of the mark.
- `test_the_rules_have_one_owner.py`: the warden as a carrier of rule 10;
  the warden claims no seal.

Unchanged and green, the rule and its phrase kept: the suite-label audit and
the `## Not judged` field (`test_broad_gate_rule.py`), the runner, the `uv`
venv and no `bin/test` (`test_the_suite_has_a_command_that_is_cheap_twice.py`),
the verifying round's two phrases, the regression and reopens sentences, the
reference root, #36 and §8, §9 and the scratch fixture, the axes, the
fixture chain and the timeout, the identifiers link, `Record language`, the
coverage probe and what comes due.

### The cases, each seen red

| Case | Seen red by |
|---|---|
| T1 `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone` | the old warden, exit 1 (3 problems); the four skipped definitions each give 2 or 3 problems on `shape_problems`; `mutation-check` M1 (the sentence), M2 (a second `skills:` entry) |
| T2 `…::test_every_file_a_step_names_exists` | M3 (`skills/code-reviews/SKILL.md`) |
| `…::test_a_second_preload_is_caught`, `…::test_a_missing_or_extra_section_is_caught`, `…::test_a_sentence_anywhere_but_the_opening_is_caught`, `…::test_a_path_that_does_not_resolve_is_caught` | M12-M15, one break of each helper |
| `test_a_moved_rule_leaves_its_definition.py::test_the_warden_writes_its_record_in_the_branch_worktree` | M4 |
| `…::test_the_warden_reads_each_new_test_against_its_group` | M5 |
| `test_review_axes.py::test_a_later_round_inherits_no_verdict_anywhere`, extended | M6 |
| `test_docs_line_wrap.py::test_a_line_of_targets_in_a_rule_file_is_skipped_wherever_it_stands` | before the change, exit 1 (`prose_lines` took no `rule_file`); M7, which also turns both files' wrap cases red |
| `test_one_word_one_meaning.py::test_the_two_definitions_name_what_they_actually_keep`, changed | M8 |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py::test_the_wardens_clone_is_named_for_the_work_item_and_the_round`, re-pointed | M9 |
| `test_the_record_is_written_in_words.py::test_the_template_the_format_and_the_two_definitions_carry_no_emoji`, re-pointed | M10 (an emoji in `## The record`) |
| `test_a_moved_rule_leaves_its_definition.py::test_a_citation_is_not_a_copy`, changed | M11 |
| `test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`, the cases `rule 5: tokens per tool call falling while the total rises`, `… rising while the total falls`, `no result: a side whose tool calls are unknown`, `no result: a side with no tool calls` | the harness at c0cc89e9, exit 1 (7 failed, 55 passed); MB (the total judged again: both `while the total` cases red), ME (the zero-call guard removed) |
| the same, `rule 5: tokens per tool call equal to the baseline's` | passes on the old total rule by construction; MA (`>` for `>=`) |
| `…::test_a_record_reads_back_to_the_numbers_it_was_written_from`, `…::test_spend_and_wall_seconds_are_written_and_never_judge`, changed | the harness at c0cc89e9, exit 1 |
| `…::test_a_run_counts_every_tool_call_its_trace_holds`, new | the harness at c0cc89e9, exit 1; MC (no de-duplication by id), MD (no calls read as zero), MF (an unknown run's calls summed as zero) |

Each `mutation-check` printed `red: the cases failed against the mutation
(exit 1)` and exited 0, and the tree was clean after all twenty-one.

### Commands, each with its exit code

Read directly with `; echo $?` or into a file, never through a pipe. `$S` is
the session scratch directory's `957-phase-2/`; `$E` is this work item's
`evals/`; `$K` is `SpecSeal-worktrees/957-phase-2-raw/`.

| Command | Exit |
|---|---|
| `bin/test` over the 57 candidate modules, before the rewrite | 1: 1 failed (the missing overview), 2,580 passed, 10 skipped |
| `bin/test tests/test_every_agent_reads_the_contract.py -q -p no:xdist`, new module, old warden | 1: 1 failed (T1 on the warden), 17 passed, 4 skipped |
| the 57 modules, after the rewrite | 1: 21 failed |
| the 57 modules and five hygiene modules, after re-pointing | 1: 1 failed (the missing overview), 2,786 passed, 14 skipped |
| `uvx ruff check` and `uvx ruff format --check` on the 11 changed `.py` | 0, 0 |
| `bin/rules --check` | 0, 443 targets in 60 rule files |
| `git commit` | 0, 71a50320 |
| `mutation-check`, M1-M15 | 0 each (`red`) |
| `python3 evals/scripts/noninferiority.py run --agent warden --rev 71a50320 --suite-rev af9c924b --out $S/warden-phase-2.json --runs 2 -j 4` | 0; 18 runs, none cut short |
| `noninferiority.py run --from-raw $S/warden-phase-2.raw --out $E/warden-phase-2.json`, then `cmp` | 0, 0 |
| `noninferiority.py compare --agent warden --phase 2 --old $E/baseline-warden.json --new $E/warden-phase-2.json --out $E/warden-phase-2.md` | 0, `Verdict: fail` |
| `noninferiority.py check $E/warden-phase-2.md` | 1, its numbers give `fail` |
| `bin/payload-meter --agent warden` | 0: 43,826 B, 13,696 tokens estimated |
| `bin/payload-meter --root <af9c924b's agents/ and skills/> --agent warden` | 0: 89,337 B, 27,918 tokens estimated |
| `python3 -I $S/per_run.py` over both sides' JSON and traces | 0 |
| `bin/test tests/test_chain_hooks_hardening.py -q -k overview` | 0 |
| `bin/unverified-check` on this work item | 0: 1 open, 0 closed |

The run 1 rows above name the side and record before their rename to
`…-run-1.…` at cd244ff0. After the owner's decision, `$T` is the session
scratch directory's `957-phase-2b/` and `$R` is
`SpecSeal-worktrees/957-baseline-raw/`:

| Command | Exit |
|---|---|
| `python3 -I $T/calls.py` over the five kept trace directories | 0: every `tool_use` block, unique by id, session and agent: warden 746/746/36/710, run 1 890/890/36/854, sealer 97, smith 197, framer 112 |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist`, new cases, harness at c0cc89e9 | 1: 7 failed, 55 passed |
| the same with `test_evals_layout.py`, after the change | 0: 73 passed |
| `uvx ruff check` and `uvx ruff format --check` on the two `.py` | 0, 0 |
| `git commit` | 0, 8dad1b29 |
| `mutation-check evals/scripts/noninferiority.py`, MA-MF (MA, MB, ME first ran `-k` on a case id with spaces, collected nothing, and stopped at `no baseline`, exit 2; rerun over `-k verdict_is_recomputed`) | 0 each (`red`) |
| `noninferiority.py run --from-raw` into `$T` for the four baselines and run 1, then `python3 -I $T/keydiff.py` against the committed files | 0 each; one added `specseal.tool_calls` per run, nothing else |
| the same into `$E`, then `cmp` with `$T` | 0 each |
| `noninferiority.py compare … --new $E/warden-phase-2-run-1.json --out $E/warden-phase-2-run-1.md` | 0, `Verdict: fail` (rule 3) |
| `bin/test` over the harness, `test_evals_layout`, `test_no_real_identifiers`, `test_no_passage_is_pasted_into_a_second_file`, `test_one_word_one_meaning`, the files staged | 0 |
| `git commit` | 0, cd244ff0 |
| `bin/test` over the 25 modules that read the two files, after the fixes | 0: 1,048 passed, 4 skipped |
| `bin/rules --check` | 0 |
| `git commit` | 0, 71bafe0f |
| `python3 evals/scripts/noninferiority.py run --agent warden --rev 71bafe0f --suite-rev af9c924b --out $T/warden-phase-2.json --runs 2 -j 4` | 0; 18 runs, none cut short |
| `noninferiority.py run --from-raw $T/warden-phase-2.raw --out $E/warden-phase-2.json`, then `cmp` | 0, 0 |
| `noninferiority.py compare --agent warden --phase 2 --old $E/baseline-warden.json --new $E/warden-phase-2.json --out $E/warden-phase-2.md` | 0, `Verdict: fail` (rule 3, one grader) |
| `noninferiority.py check $E/warden-phase-2.md` | 1, its numbers give `fail` |
| `bin/payload-meter --agent warden` | 0: 43,938 B, 13,731 tokens estimated |

`payload-meter`'s totals hold the `CLAUDE.md` pair, 13,318 B on this
machine. The raw output of the new side, with `run.log`, is kept at `$K` for
a later rule change to re-read.

## The orchestrator closes the phase on the record as it reads

Closed 2026-10-17 by the orchestrator, under the owner's standing
instruction for this unattended run (decide; file what cannot be decided).
The record reads `fail`, and it stays `fail`: the rules are not changed after
a run to pass it. The phase closes anyway, for these reasons, each read off
the two records:

- Rule 3 fails on one grader by one run (`seeded-9b644676/shape-findings`,
  1/2 against 2/2). Across all 36 graders the new side passes 70 of 72 runs
  where the baseline passes 66, and the defect the first run showed, a
  record without `verdict:` lines, fell from 5 of 18 records to 1.
- Every other figure is better than the baseline's: recall 16 against 13,
  false rate 0.564 against 0.782, preload 30,620 against 76,019 bytes,
  tokens per tool call 4.2% below.
- The remaining miss is answered by a check rather than a sentence. Neither
  the old warden nor this one is told to read its own record through
  `chain_check.py` before it hands back, and that check refuses a finding
  with no `verdict:` line by construction. Phase 3 adds that step to
  `agents/warden.md`, and phase 3 runs the warden's set again (every
  preload changes with the contract), so the step is measured there at no
  extra run. Phase 3's warden record is where this phase's one failing
  grader is read again.
- Whether two runs a case are enough for a per-grader rule, when the
  baseline itself passes 66 of 72, is a measurement design the run cannot
  settle; it is filed as an issue in milestone `release: 0.22.1`.
