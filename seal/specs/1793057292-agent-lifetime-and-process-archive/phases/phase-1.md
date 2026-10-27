# Phase 1: 1793057292-agent-lifetime-and-process-archive

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 765ba3ac |

## What this phase was asked

Build the largest per-turn context in `skills/verify/scripts/session_cost.py`:
a function, a column of `report_segments` and a key on each
`measure_segments` row, which `--json` prints. Its cases go in a class of
their own in `tests/test_session_cost.py`, apart from the existing function
classes that #1017's branch adds cases to, and each S row's case (S1 to S3)
is seen red first. Rewrite in place the list of a row's numbers in
`skills/verify/orchestration.md` *Measure the segment, and feed the flow
log*, step 1. Run the column over the 0.22.0 run's transcripts that remain
and record here the largest context of the resumed smith and of each fresh
smith, which transcripts were gone, and the threshold the reading gives,
with Q3's default (461,000) where the transcripts are gone (S4). Run
`skills/settle/scripts/rule_changes.py#parse` over this `spec.md`, as
`plan.md`'s Verified by asks. Run only the touched modules, `test-layout
--check` and `--pairs`, and `uvx ruff check` and `uvx ruff format --check`
over the changed Python files.

## What this phase found

**The frame holds for phase 1, with one fact about the transcripts that is
wrong** (`executed`). `plan.md` row T-B says two session transcripts from
2026-10-13 to 2026-10-15 remain, found with `find -newermt`, and that
whether #930's smith is among their segments is unknown. Those two,
`916bffa3-48e6-48e2-89cd-46a64841f442.jsonl` and
`20f122bc-1e8b-46c6-8158-88431e504d2d.jsonl` under
`~/.claude/projects/-Users-michael-Documents-GitHub-SpecSeal/`, are earlier
runs: their smiths build #835 to #922, and none builds an issue of the
0.22.0 milestone. The 0.22.0 run is
`c5415a05-3853-4b1d-898b-40ecb4d67259.jsonl`, whose rows run from
2026-10-13T07:17Z to 2026-10-16T08:32Z. `find -newermt` on the main file
missed it because the file was last written on 2026-10-19. Its smiths build
#923, #929, #930, #931 and #944, all milestone 0.22.0 (`gh issue view`),
and #941 phases 1 and 8, milestone 0.22.3.

**No transcript of the 0.22.0 run is gone** (`executed`, `session-cost
--json` over the run's transcript). The run's 116 `Agent` calls and the 116
segment transcripts beside it join to one another except one pair: the
framer spawned as `Frame #941 docs rewrite` opens 1.03 s before its spawn's
result, outside the 1.0 s tolerance. Every smith is named. Q3's fallback to
461,000 is not needed.

**The reading reproduces the owner's figure for the resumed smith**
(`executed`). #930's smith, `agent-aa6874fb2aff9e251.jsonl`, reached
941,799 tokens of context in one turn and spent 274,346,384 tokens, the two
numbers #945's comment of 2026-10-14 states. The comment's 1,099 turns is
the count of rows carrying `usage` in that file. Counted once per message,
as this column and `token_totals` count, they are 469 turns.
`session-cost --segments` on that file, the agent's own transcript, cut at 6
coordinator messages into 7 slices, prints:

```
  agent                             span  calls  t/turn    gap        tokens     context
  …-aa6874fb2aff9e251.jsonl  1/7   32.8m    180    1.48    10s   274,346,384     377,894
  …-aa6874fb2aff9e251.jsonl  2/7   23.2m    161    1.96    10s             —     569,013
  …-aa6874fb2aff9e251.jsonl  3/7   15.7m     94    1.62     7s             —     655,847
  …-aa6874fb2aff9e251.jsonl  4/7   23.5m    155    1.76     8s             —     778,563
  …-aa6874fb2aff9e251.jsonl  5/7   22.3m    170    1.91     7s             —     904,072
  …-aa6874fb2aff9e251.jsonl  6/7    6.6m     35    1.84     6s             —     931,652
  …-aa6874fb2aff9e251.jsonl  7/7    2.1m     12    1.09     8s             —     941,799
```

**Seven smiths were resumed, and one of them read more than #930's**
(`executed`). A resumed smith is one whose file the coordinator's messages
cut into two slices or more. Its first slice is the phase it was spawned
fresh for:

| Smith | Slices | First slice | Largest |
|---|---|---|---|
| Build #930 phase 1 | 7 | 377,894 | 941,799 |
| Build #931 phase 1 | 7 | 281,154 | 841,789 |
| Build #929 phase 1 | 6 | 268,959 | 572,906 |
| Build #923 phase 2 eval harness | 3 | 527,634 | 646,163 |
| Build #941 phase 1 worktree-guard doc | 3 | 422,220 | 622,187 |
| Build #944 phase 1 | 2 | 363,829 | 960,259 |
| #944: seal.py ledger path and kernel move | 4 | 179,215 | 269,222 |

**The 49 fresh smiths read from 143,833 to 806,241** (`executed`). A fresh
smith here is one spawned and never resumed, so its file is one slice. The
smallest is `#929 fix round-4 finding`, and the largest is `#923 phase 3: new
review record`, at 806,241. The next largest are `#923 phase 3 second half`
at 769,946 and `Build #944 phase 4: cut to kernel` at 649,150. The 44 of the
49 that build a 0.22.0 issue span the same range. The comment's range for
fresh spawns, 165k to 461k, does not reproduce. The five fresh smiths that
opened before the comment was posted (2026-10-14T04:45Z) read 161,149
(#931's rebase pass), 161,724, 384,358, 457,776 (#941 phase 8) and 487,998
(#944 phase 3). #944 phase 3 opened at 04:24Z, so it may have reached its
largest after the comment.

**The threshold the reading gives is 806,241, under Q3's option (a)**
(`executed`). Option (a) asks for the largest context a fresh smith reached
in the 0.22.0 run, and that is #923 phase 3's 806,241. Phase 2 writes the
number, and two readings of the question would write a different one.
Read over the fresh smiths the comment could have seen, the figure is
487,998, not the comment's 461,000. The fix-pass rule
(`skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh
smith, and a fix pass resumes the implementer*) reads the implementer's
largest context before the pass and resumes below the threshold. Held
against the table above, the threshold alone gives this for #930's smith.
Under 487,998, it would have been resumed for its second slice, because its
first read 377,894, and spawned fresh from its third, because its second
read 569,013. Under 806,241, it would have been resumed through its fifth
slice, because its fourth read 778,563, and spawned fresh from its sixth,
because its fifth read 904,072. The figure is the orchestrator's to choose
for phase 2, and Q3's `Status` cell is the orchestrator's to write, because
`questions.md` is not among the files this phase writes.

**The function reads a file and answers per window, not per slice**
(the work). `spec.md` *Data & interfaces* names a function computing one
slice's largest context from the slice's assistant messages. It was built as
`largest_context(path, cuts=())`, which reads the transcript once and
returns one value per window of `in_windows(cuts, ...)`. `segment_slices`
calls it once per file and reads each kept slice's value at its window, so
a resumed file is opened once for the column rather than once per slice.
Every message carrying a `usage` block counts, whether or not it calls a
tool. Each counts once by `message_key`, at the largest value each of the
three input fields reached across its rows. A window with no message
answers None, and the table prints a dash. Where there are cuts, a message
whose stamp does not parse is dropped, as `segment_slices` drops a turn.
`load`'s `turns`, `token_thirds` and the run's `context` line are
unchanged.

**One existing case in `Test_main` changed** (the work). Every new case is
in `Test_largest_context`, placed between `Test_family` and `Test_module`.
`Test_main::test_the_printed_segment_table_names_each_agent_and_its_own_span`
anchored each printed row at its token cell with `$`, so any new column
breaks it. Its two patterns now end with the context cell, 300 for the
smith and 40 for the warden. #1017's branch adds cases to `Test_main` too,
so a text conflict at those two lines is possible at its merge.

**`README.md` stated the same list of columns, and it is corrected**
(`executed`). The `session-cost --segments` row in `README.md` listed a
row's span, calls, tools per turn, mean gap and tokens. It now names the
context too, in the separate commit 765ba3ac. Its first wording copied the
orchestration step's 15 words, and
`tests/test_no_passage_is_pasted_into_a_second_file.py` refused it, so the
README words it differently. `README.md` is not among the files `plan.md`
names for phase 1. It was changed under contract rule 19, because the
sentence states the old fact. `git grep -n "mean gap and"` outside
`seal/specs` finds one other site, a case's docstring in
`tests/test_session_cost.py` at line 4526. That docstring describes what
its case compares, and the case does not compare the new key, so it stands.

**Each new case was seen red against the tree as it stood** (`executed`,
`bin/test tests/test_session_cost.py -p no:xdist -q -k "Test_largest_context
or test_the_printed_segment_table_names_each_agent_and_its_own_span"` at
3c686a96 with the cases written and the code unchanged, 7 failed):

| S row | Case | Red at 3c686a96 | Red under its mutant |
|---|---|---|---|
| S1 | `test_accepts_a_segments_largest_turn_as_a_json_key_and_a_column` | `KeyError: 'largest_context'` | the legend line cut |
| S1 | `Test_main::test_the_printed_segment_table_names_each_agent_and_its_own_span` | no context cell after the tokens | the context cell removed from the row |
| S2 | `test_accepts_a_message_split_over_rows_once` | `AttributeError`, no `largest_context` | rows summed instead of kept at their largest |
| S2 | `test_accepts_every_input_field_of_a_turn` | `AttributeError` | `cache_creation_input_tokens` dropped from `CONTEXT_FIELDS` |
| S2 | `test_accepts_a_turn_that_called_no_tool` | `AttributeError` | messages with no `tool_use` skipped |
| S3 | `test_accepts_each_slice_of_a_resumed_file_as_its_own` | `KeyError` | the whole file's value given to every slice |
| S3 | `test_refuses_a_zero_for_a_slice_that_holds_no_assistant_message` | `KeyError` | `default=None` made `default=0` |

**Mutations** (`executed`, `mutation-check` over
`skills/verify/scripts/session_cost.py` after b7b73086, each bounded at
300 s). The batch of the seven mutants in the last column above, run over
the seven cases, gave 7 red and 0 survived. Each mutant was then run alone
over the one case written for it, and each run ended `1 failed`. The tree
was clean after each run.

**`rule_changes.py#parse` reads this spec's `## Rule changes` with no
refusal** (`executed`, `parse(text, "docs")`, with `docs` being the policy root
`settle.py` passes). It returns 10 operations and no error. Each `from:`
text is found in its file, matched as `rule_changes.py#pattern` matches,
with whitespace runs collapsed. Called with an absolute policy root, `parse`
refuses every `file:`, because it matches `<policy root>/<name>.md` as text.

**The narrow checks** (`executed`, exit 0). `bin/test
tests/test_session_cost.py` returned 228 passed. `bin/test
tests/test_a_segment_feeds_the_flow_log.py tests/test_one_word_one_meaning.py
tests/test_docs_line_wrap.py tests/test_the_chain_section_has_one_shape.py
tests/test_session_cost.py -q` returned 330 passed. `bin/test
tests/test_no_passage_is_pasted_into_a_second_file.py
tests/test_a_document_has_room_for_the_next_fold.py
tests/test_the_frozen_reading_never_grows.py
tests/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py
tests/test_a_segment_feeds_the_flow_log.py -q` returned 147 passed and 8
skipped after the README rewording. `bin/test-layout --check
tests/test_session_cost.py` refused nothing. `--pairs` named no pair in
`Test_largest_context`. `uvx ruff check` and `uvx ruff format --check` over
the two changed Python files report nothing. The new cases have no entry in
`.test_durations` until its next refresh.
