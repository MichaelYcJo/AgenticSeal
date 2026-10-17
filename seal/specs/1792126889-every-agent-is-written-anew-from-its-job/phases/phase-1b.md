# 1792126889-every-agent-is-written-anew-from-its-job — phase 1b

| Field | Value |
|---|---|
| Phase | 1b |
| Commit | ad1a93a2 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Build the owner's decision of 2026-10-17: the baseline is a reference, not
an absolute, and the verdict judges whether tokens fell and the outcome held
or improved, not time. In `evals/scripts/noninferiority.py#verdict`, keep
rules 1, 2 and 4; make rule 3 relative (each shape and reach grader passing
on the new side at least as often as on the baseline, keeping the handling
of a grader one side lacks); make rule 5 the tokens read across every model,
from the session's last `result` event `modelUsage`, strictly below the
baseline's; record spend and wall seconds and judge nothing with them;
remove `COST_MARGIN` if nothing else reads it. A run with no `modelUsage` is
no result, never zero. Then re-derive the four baseline files with
`run --from-raw` from the kept raw output and no new run, and show they differ
from phase 1's only in the fields this phase changes. Write the cases first
and see each red, run `mutation-check` on the changed comparisons, rewrite
every text that states the rules, note on `questions.md` Q8 that it is read
from `modelUsage`, and decide whether the change needs a changelog fragment.

## What this phase found

**The frame holds, with two sentences behind it.** The plan's 1b row is what
was built. Two sentences written before the owner's decision are now stale,
and neither is this phase's to rewrite:

- `plan.md` §*Technical context* says the harness is one "this item does not
  touch". Phase 1b touches it.
- `questions.md` Q5's answer ends "Whether rule 4 should read `modelUsage` is
  the orchestrator's, open in phase 1's hand-back". The owner settled it, and
  rule 5 reads `modelUsage` now.

**The rules, as the code now has them** (`noninferiority.py#verdict`):

| Rule | Before | After |
|---|---|---|
| 1 recall | not fallen, one find of noise allowed | unchanged |
| 2 false-finding rate | within `FALSE_MARGIN` of the baseline's | unchanged |
| 3 shape and reach graders | every new-side run passes | fails only where the new side passes a grader less often than the baseline (`np * old_runs < op * new_runs`). A grader the baseline lacks is judged on the new side alone, every run passing. A grader the new side lacks is not judged |
| 4 preload bytes | below the baseline's | unchanged |
| 5 tokens | within 1.1 times the baseline's, from the case session's `usage`; spend within 1.1 times too | strictly below the baseline's, summed across every model of `modelUsage` |
| spend, wall seconds | spend judged by rule 4, seconds not judged | written in the record, judge nothing |
| no result | a side cut short, unequal runs, spend, tokens or bytes unknown | a side cut short, unequal runs, tokens or bytes unknown |

**Field names and the record.**

- `run_cost` now copies `total_cost_usd`, `duration_ms` and `modelUsage` from
  the session's last `result` event. A field the event lacks is `None`. A
  trace with no session `result` event still gives no cost at all.
- `usage` is no longer kept. `modelUsage` already counts the case session's
  model, so `usage` is a part of it, and no rule reads it.
- What this gives up: for the warden and the smith, whose session and agent
  both run on Opus, `modelUsage` holds one key. The case session's share
  cannot be read off a side file any more. Phase 1's table keeps it (1.9% to
  11.6%), and Q5 is answered.
- `tokens_read(model_usage)` sums `inputTokens`, `cacheCreationInputTokens`
  and `cacheReadInputTokens` over every model. It returns `None` for an
  absent or empty `modelUsage`, a model that is not an object, or a model
  missing one of the three counts or carrying a non-integer one. It never
  returns a smaller sum.
- `side_numbers` pools each of spend, tokens and seconds on its own through
  `pooled`, which is `None` where any run lacks that number. A side whose
  spend is unknown but whose tokens are known is therefore judged, not
  refused.
- The record's tokens row is renamed `tokens read, every model`, so a reader
  does not take it for the session's `usage`. No record with the old label
  exists: `git ls-files 'seal/specs/*/evals/*'` lists the four baselines and
  #923's two notes, and none of them is a `compare` record.
- `COST_MARGIN` is gone. `git grep -n COST_MARGIN` outside `seal/specs/`
  finds nothing after `792e9566`.
- The no-result cases in `CASES` were named `rule 5: …`. Rule 5 is the
  tokens now, so they are named `no result: …`.

**The four baselines, re-derived without a run.** First, with the harness at
3603d879, `run --from-raw` over the kept raw output wrote files `cmp`
identical to phase 1's committed four. That proves the raw output is the
same runs. Then the new harness re-derived them. `keydiff.py`, a scratch
script that walks both JSON trees key by key, finds exactly one removed and
one added path per run and nothing else:

| Agent | Runs | `…specseal.cost.usage` removed | `…specseal.cost.modelUsage` added | Other differences | `diff` lines (`<` / `>`) |
|---|---|---|---|---|---|
| sealer | 6 | 6 | 6 | none | 120 / 168 |
| smith | 8 | 8 | 8 | none | 168 / 120 |
| framer | 8 | 8 | 8 | none | 168 / 120 |
| warden | 18 | 18 | 18 | none | 378 / 270 |

The sealer's `modelUsage` is longer than its `usage` because it names two
models (Sonnet for the case session, Opus for the sealer). The other three
name one. The files written into the tree are `cmp` identical to the scratch
copies, and they are committed at b8d02833.

**What the baselines read under the new harness**, through
`noninferiority.py#side_numbers` on the re-derived files:

| Agent | Runs | Tokens read, every model | Case session's `usage` (phase 1's figure) | Share | Spend USD | Seconds | Preload bytes |
|---|---|---|---|---|---|---|---|
| sealer | 6 | 3,324,087 | 255,424 | 7.7% | 3.0366 | 577.2 | 28,358 |
| smith | 8 | 8,978,191 | 333,442 | 3.7% | 6.3830 | 1,144.5 | 94,693 |
| framer | 8 | 3,164,345 | 366,118 | 11.6% | 16.5896 | 1,875.0 | 93,453 |
| warden | 18 | 66,468,871 | 1,265,634 | 1.9% | 36.0352 | 5,779.5 | 76,019 |
| total | 40 | 81,935,494 | 2,220,618 | | 62.0444 | | |

Every token total equals the figure phase 1 summed by hand from the saved
traces. Every one of the 40 runs carries a complete `modelUsage`; no side
reads `None`.

**What this changes for phase 2.** The warden baseline's five short shape
graders (`replay-1791384160-r2`, `replay-1791779434-r5`, `seeded-279a580b`)
no longer fail a new side that does as well as the baseline. A new side
fails one only by passing it less often. Rule 5 asks the warden's 18 runs to
read fewer than 66,468,871 tokens across every model.

**The cases, each seen red.** Against `noninferiority.py` at 3603d879 with
the new tests, the module ran 14 failed, 43 passed, exit 1. Each failure was
for its stated reason: rule 3 failing a grader the baseline fails as often;
a 1.05-times and an equal token figure passing; spend and unknown spend
judged; the record's row label missing; the run cost carrying `usage`; and
`tokens_read` reading `usage`'s keys, so it summed none of `modelUsage`'s,
and it returned a sum or raised where a case wants `None`. Two new cases pass on the old code by
construction, because the old rule 3 already failed more often than the new
one. Those two were seen red against a mutation, below.

| Case (`tests/test_a_rewritten_definition_proved_non_inferior.py`) | Seen red by |
|---|---|
| `CASES["rule 3: a shape grader failing as often on the new side as on the baseline"]` | the old code; M1 |
| `CASES["rule 3: a shape grader passing less often than a baseline that fails it"]` | M2 |
| `CASES["rule 3: a reach grader the baseline lacks, short of every new run"]` | M3 |
| `CASES["rule 5: tokens read across every model equal to the baseline's"]` | the old code; M4, M5 |
| `CASES["rule 5: tokens read across every model 1.05 times the baseline's"]` | the old code; M5 |
| `CASES["spend 1.2 times the baseline's is written and not judged"]` | the old code |
| `CASES["spend and wall seconds unknown, tokens known, are not judged"]` | the old code; M7 |
| `test_a_record_reads_back_to_the_numbers_it_was_written_from` (changed: the tokens row's label, an edited token figure failing rule 5) | the old code |
| `test_spend_and_wall_seconds_are_written_and_never_judge` (replaces `test_a_costlier_side_fails_naming_rule_4_and_wall_seconds_never_judge`) | the old code |
| `test_a_run_records_what_it_cost` (changed: `modelUsage` summed over two models, a `result` event with no `modelUsage` is no result) | the old code |
| `test_a_model_usage_missing_a_count_is_no_token_figure` (new, six shapes) | the old code (all six); M6 (`missing-count`, `null-count`) |

`mutation-check` broke one comparison at a time, ran
`-k verdict_is_recomputed` (or `-k model_usage_missing` for M6), and
restored the file. Each printed `red` and exited 0, and the tree was clean
after all seven:

| Break | What it puts back | Cases red |
|---|---|---|
| M1 | rule 3 reading the new side alone (`np_ < nruns`) | 1 |
| M2 | rule 3 excusing a grader the baseline already fails (`op == oruns and …`) | 1 |
| M3 | rule 3 dropping a grader the baseline lacks (`if False:`) | 1 |
| M4 | rule 5 with `>` for `>=` | 1 |
| M5 | rule 5 with the old 1.1 margin | 2 |
| M6 | a missing count read as zero (`model.get(k) or 0`) | 2 |
| M7 | spend unknown judged as no result again | 1 |

**Every text stating the rules, enumerated.** The instructed
`git grep -n -i -E "COST_MARGIN|five rules|rule 4|every shape and reach grader|within .*COST"`,
widened with `five pass rules` and `pass rules`, outside `seal/specs/` and
`changelog/`, found `evals/README.md`, `evals/scripts/noninferiority.py`,
this module, and `skills/implement/orchestration.md:302`. The last is
`§*Creation consent*, rule 4`, a different rule. A second grep for
`noninferiority`, `tokens read`, `modelUsage` and `total_cost_usd` outside
the same paths found `evals/scripts/behaviour.py:8`. That line names the
grader kinds and no rule, and it is unchanged. The two `hooks/cmdline*.py`
hits are about shell tokens. The README, the module docstring, `verdict`'s,
`run_cost`'s, `tokens_read`'s and `side_numbers`' docstrings, and the test
module's docstring are rewritten. Every old and new fragment was grepped
under `tests` and `evals`. The only reader outside the two files is
`tests/test_evals_layout.py`, which reads the README. It is run below with
the text-reading modules.

**No changelog fragment in this phase.** `noninferiority.py` is this
repository's proof harness for its own agents. No file under `bin/`,
`skills/`, `agents/`, `docs/`, `templates/` or `hooks/` names it
(`git grep -n noninferiority` over those paths finds nothing), so no plugin
user runs it or reads its verdict. Phase 6 writes the item's fragment, with
the per-agent table read from these records.

### Commands, each with its exit code

Read directly with `; echo $?`, never through a pipe. `$S` is the session
scratch directory's `957-phase-1b/`, `$R` is
`SpecSeal-worktrees/957-baseline-raw/` (read only), and `$E` is this work
item's `evals/`.

| Command | Exit |
|---|---|
| `git diff --stat af9c924b HEAD -- evals tests bin` at 3603d879 | 0, empty |
| `noninferiority.py run --from-raw $R/baseline-<a>.raw --out $S/before/baseline-<a>.json`, four times, harness at 3603d879 | 0 each |
| `cmp $S/before/baseline-<a>.json $E/baseline-<a>.json`, four times | 0 each |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist`, new tests, harness at 3603d879 | 1, 14 failed, 43 passed |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q -p no:xdist`, after the change | 0, 68 passed |
| `uvx ruff check` and `uvx ruff format --check` on the two `.py` files | 0, 0 |
| `mutation-check evals/scripts/noninferiority.py --replace … --tests "bin/test <module> -q -p no:xdist -k …"`, M1 to M7 | 0 each (`red`) |
| `noninferiority.py run --from-raw $R/baseline-<a>.raw --out $S/after/baseline-<a>.json`, four times | 0 each |
| `python3 -I $S/keydiff.py $E/baseline-<a>.json $S/after/baseline-<a>.json`, four times | 0 each |
| `noninferiority.py run --from-raw $R/baseline-<a>.raw --out $E/baseline-<a>.json`, then `cmp` with the scratch copy, four times | 0 each |
| `bin/test` over the five text-reading modules phase 1 ran, the four files staged | 0, 102 passed |
| `bin/test` over this module, `test_evals_layout`, `test_every_file_the_plugin_reads_or_writes_names_its_encoding`, `test_the_release_check_watches_what_ships`, `test_the_rules_command_reads_each_rule_off_its_test`, `test_a_document_that_names_a_script_says_how_to_reach_it`, `test_no_passage_is_pasted_into_a_second_file`, `test_one_word_one_meaning`, `test_docs_line_wrap`, `test_no_real_identifiers` | 0, 386 passed, 6 skipped (`no shipped document names it`, as before) |
| `bin/rules --check` | 0, all 416 targets in 60 rule files resolve |
| `bin/test` over `test_a_phase_hands_the_next_one_a_record`, `test_a_question_says_who_can_answer_it`, `test_no_passage_is_pasted_into_a_second_file`, `test_no_real_identifiers`, `test_one_word_one_meaning`, `test_the_record_is_written_in_words`, `test_no_document_names_the_old_roots`, `test_no_shape_the_base_stops_reads_silent`, this record, `questions.md` and `plan.md` staged | 0, 125 passed |

No eval ran and nothing was spent. The kept raw output under `$R` was read
and not written: `run --from-raw` writes only `--out`.
