# Phase 1: 1793795305-the-behaviour-suite-is-a-smoke-run

## What this phase found

**The frame holds, with two gaps in the list S4 hands the build.** I
checked it against the tree at `94dd5809d` before the first edit (read,
unless marked).

- `evals/scripts/noninferiority.py#verdict` ran its `no result` checks,
  then rules 1 to 5, as *Technical context* says. Rule 3's block, from the
  `common = sorted(` line to the loop over a grader the baseline lacks,
  stood as the plan gives it.
- The 13 `check:` lines that name a case of the suite stand (executed: the
  design's `git grep`, piped to `wc -l`, prints 13).
- `.github/workflows/test.yml` runs `.github/scripts/release_report.py` in
  the `release-report` job, `if: ... github.base_ref == 'main'`, and the
  script prints each agent's preload bytes against the last tag. So S1's
  sentence on where the bytes are read with no run is true of the tree.
- `.claude-plugin/plugin.json` held `0.31.2`, and no other file outside
  `seal/` spells that version as the plugin's (executed: `git grep`).
- **Gap 1: S4 names too few cases.** Eight more cases, eleven ids, of
  `tests/evals/test_noninferiority.py` made a record fail through rule 1,
  2 or 5, so S2 turns each one red. They are
  `Test_render::test_refuses_a_failing_side_with_its_reasons_and_a_cut_one_as_no_result`
  (recall),
  `Test_read_record::test_refuses_a_record_that_does_not_parse_or_says_otherwise`
  (tokens), `Test_check_record::test_refuses_anything_but_pass[fail]`
  (tokens), `Test_check_record::test_refuses_an_edited_cell_the_verdict_does_not_follow`
  (tokens, and it asserted `rule 5`), the four ids of
  `Test_check_record::test_a_count_row_spelt_otherwise_is_read_as_naught`
  and `Test_check_record::test_a_count_padded_with_more_spaces_is_read`
  (the false rows), `Test_check::test_refuses_a_failing_record_and_one_over_two_suites`
  (recall), and `Test_model::test_refuses_a_record_it_cannot_read_or_trust[edited]`
  (tokens). The docstring of
  `Test_tokens_read::test_refuses_a_short_model_usage_as_no_figure` said
  that rule 5 passes a rewrite on a count read as zero. The probe below
  shows each of them red against S2.
- **Gap 2: S1 leaves out one sentence of the section.** The last paragraph
  of `evals/README.md` *The behaviour suite* said that a row count spelt
  otherwise reads as 0, "so a record edited by hand can pass `check` on a
  count it never read". After S2 no pass rule reads a count, so the clause
  implied a verdict the count no longer moves. The closed set of
  *Technical context* holds the section whole, so this phase rewrote it.

I built to the frame as it stands, and to these two gaps as below.

**Decisions, each with its grounds.**

- **D1. The `VERDICTS` rows of rules 1, 2, 4 and 5.** Each of the four
  figures that judged keeps one row that expects `pass`: "recall fallen by
  two finds", "a false-finding rate risen by a tenth", "a preload no
  smaller than the baseline's" and "the tokens and the tokens per tool call
  both up", each "written and not judged". The four unknown-figure rows
  now expect `pass` under the same suffix. Ten rows of those rules went,
  so `VERDICTS` holds 25 rows where it held 35 (executed: the keys counted
  at `94dd5809d` and at HEAD). Two of the ten failed rule 1 ("one find
  fewer, found by no new run" and "two truths one find fewer each is no
  longer noise"). Eight already passed and pinned a boundary S2 removes:
  the noise row of rule 1, the two margin rows of rule 2, and five rows of
  rule 5, its four two-figure rows and its exact-margin row. A row kept
  for them would pass with nothing behind it.
  Its name would also state a margin the tree no longer holds. This
  departs from S4's wording, "become rows that expect pass", and the
  frame's `## Removes` names only the rows that expected `fail` or
  `no result`. Judged against `skills/core/SKILL.md` *The rule a mechanism
  is kept against* ("in the same commit removes what stood on the old
  fact") and the crafter's rule that a case covering nothing its group
  does not already cover is not added.
- **D2. Rule 3's rows are renumbered by clause.** The rows that named
  `rule 3:` now name the clause they exercise, `rule 1:`, `rule 2:` or
  `rule 3:`. Judged against `frame/plan.md` *Alternatives considered* A5,
  under which a reader looks a number up in a three-rule list.
- **D3. The cases that failed a record through another rule fail it
  through rule 1.** The test module gains `SHAPE_FELL`, which is `GRADED`
  with its shape grader passing one run fewer. Each case of gap 1 that
  needed a failing record now builds it from `SHAPE_FELL`. The edited-cell
  case edits a `## Graders` row in place of the token row, and asserts
  `(rule 1)`. `model_numbers` gains `("c1", "reach-framer"): ("reach", 0,
  0, 1, 2)`, so its own verdict fails rule 3 alone. The case now asserts
  that exact verdict, with its one reason line, and `model` still prints
  `sonnet` on it. This is S4's and acceptance A6's point.
- **D4. The two row-count cases move from `Test_check_record` to
  `Test_parse_record`.** With no rule reading a count, `check_record`
  returns the same answer whatever count is read. So the cases now assert
  the count `parse_record` reads, 0 for a row spelt otherwise and 15 for a
  padded one. That is what the rewritten README sentence states (gap 2).
  Judged against the crafter's rule that a case goes to the group of the
  function it covers.
- **D5. Test names.** `test_accepts_a_new_side_no_worse_than_the_baseline`
  is now `test_accepts_a_side_no_rule_fails`, and
  `test_refuses_with_rule_3s_lines_in_their_order` is now
  `test_refuses_with_each_rules_line_in_its_order`.
  `test_refuses_with_a_line_for_each_other_rule` is now
  `test_accepts_a_side_worse_on_every_figure_no_rule_reads`, acceptance
  A1's case. `test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short`
  is removed, as S4 says.
- **D6. The renamed module is
  `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py`,**
  the name of its one case (`frame/questions.md` left the name to the
  build). The four docstrings that cited the old path no longer cite a
  name that HEAD lacks. Each says the cases came from one behaviour module
  and gives the path where that module's remaining case stands. A
  `<commit>:<path>` citation was weighed and not taken. The path held the
  module only from `e391ea04b` (#1099), after #942 had moved the cases out,
  so no commit shows the old path holding them.
- **D7. The script's other text.** The comment above rule 3's block said
  "Rule 3 judges the agent". It now names rules 1 and 2 by their new
  numbers. The `cost_rows` docstring says that no row judges anything. The
  `tool_calls` docstring keeps what the function returns and says that the
  record writes the count and that it judges nothing (`## Removes`, the
  rule 5 reasoning row). The `verdict` docstring names the keys it reads
  and says that an unknown figure gives no `no result`.

**How each changed case was shown red (contract rule 15).** I took the
plan's first way.

- The S4 cases were committed at `4a9e1dd56`, before the verdict changed.
  `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k "Test_verdict
  or Test_render or Test_read_record or Test_check_record or Test_parse_record
  or Test_cheaper_model or Test_check or Test_model or Test_tokens_read"`
  then gave 14 failed and 50 passed (executed). I read each failing line.
  The eight converted rows failed `== ("pass", [])` on `fail` (recall, the
  false rate, the bytes, the tokens) or on `no result` (the four unknown
  figures). Both cases of the order test failed on the `(rule 3)` suffix,
  and the A1 case failed on rule 5's line. `Test_render`'s two cases
  failed on the `non-inferiority` title and on the `(rule 3)` suffix. The
  edited-cell case failed on `any("(rule 1)" in p ...)`.
- After S2 at `189e51d64`, I copied the base module, the module as
  `a5e47e20e` holds it, to a probe file `tests/evals/test_tmp_old_noninferiority.py`.
  The probe set `NI.TOKEN_MARGIN = 0.07` so that it would import, and ran
  once against the new script. It gave 26 failed and 235 passed (executed).
  The 26 are the rows and cases that D1 to D5 rework or remove, and gap 1's
  eleven ids are among them. The probe file was deleted after the run.
- The reworked cases that pass both before and after S2 were each shown red
  with `bin/seal mutate` at `189e51d64`, one break each (executed, every
  verdict `red`, each failing line read):
  1. the rule 1 suffix set back to `(rule 3)`: the two order cases and
     `Test_render`'s failing-side case go red;
  2. the rule 2 suffix set back to `(rule 3)`: the second order case goes
     red;
  3. rule 3's test `np_ < nruns` broken to `np_ < 0`:
     `Test_cheaper_model::test_accepts_sonnet_where_every_grader_holds_and_it_spent_less`
     goes red on its verdict assertion, `('pass', []) == ('fail', [...])`;
  4. the removed `no result` arm for unknown tokens, calls or bytes put
     back: the four unknown-figure rows go red;
  5. rule 1's `if new_total < old_total:` broken to `if False:`:
     `Test_read_record`, `Test_check_record`'s `[fail]` and edited-cell
     cases, `Test_check` and `Test_model[edited]` go red, 5 of the 8
     selected;
  6. `header_field`'s pattern loosened to allow any spaces: the four ids
     of the spelt-otherwise case go red;
  7. `header_field`'s value made to refuse a space: the padded case goes
     red.

**The rename is a move, with no case written new.**
`tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py`
passes at the new path (executed: in the plan's command below). The census
of the old spelling, `git grep -n 'proved_non_inferior'` at `a5e47e20e`,
prints 9 lines in three groups (executed). One is `.test_durations:139`,
which the design's *Grounding* leaves to the runner. Six are this work
item's own frame files, which state the rename. Two are
`seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:236`
and `frame/plan.md:77`. Those two give a command that ran at that work
item's phase 2 commit, so neither states the present. No file a case
imports names the old path.

**The phase-boundary run.** It ran at `eb4d31b60` as one command,
`bin/test -q` over 84 modules (executed, exit 0, 5104 passed and 1
skipped). The modules are the plan row's nine, every test module that
names a path the phase changed, and every module that walks the tracked
tree. The paths are the script, the test modules, `evals/README.md`, both
READMEs, `plugin.json`, a `changelog.md`, `seal/threads/` and the renamed
module. A module walks the tree where it uses `git_listing`, `ls-files`,
`build_tracked_tree`, `corpus(` or `os.walk(ROOT`. The skip is
`tests/skills/test_broad_gate.py:1126`, "the shell here is not cmd.exe".
The plan row's command, `bin/test -q tests/evals/test_noninferiority.py
tests/evals/test_replay_targets.py tests/evals/test_rule_cases.py
tests/evals/test_seed_defects.py
tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py
tests/behaviour/test_evals_layout.py
tests/behaviour/test_both_editions_carry_the_same_folds.py
tests/behaviour/test_docs_line_wrap.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, also ran there
on its own (executed, exit 0, 400 passed).
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
passes at `eb4d31b60` (executed). It failed on the tree `9c36bbdac`
commits, before `gaps.md` existed (executed), which is the point the
framer reported.
`uvx ruff check` and `uvx ruff format --check` pass on every Python file
the range changes (executed). `bin/seal layout --pairs` names no pair in
either changed test module (executed).

**The three enumeration commands of `frame/plan.md` *Technical context*,
at `eb4d31b60`** (executed). The citation census lists 32 files. I read
each hit outside the closed set that is not a `check:` line. Only
`docs/running/measuring-a-run.md:86` calls the suite the proof of a
rewrite, and the design's `## Rule changes` changes it at the settle. Every
other hit names the suite, its directory or its script, and claims nothing
about a rewrite.

The citation census, `git grep -l -i -E 'evals/README|noninferiority|evals/behaviour|behaviou?r (suite|evals?)|행동 eval' -- ':!seal/' ':!.test_durations' ':!evals/behaviour/'`, exit 0:

```
.github/scripts/rules.py
README.ko.md
README.md
agents/framer.md
agents/proofer.md
agents/sealer.md
docs/layout/the-record-layout.md
docs/running/measuring-a-run.md
docs/running/the-agent-set.md
evals/README.md
evals/scripts/behaviour.py
evals/scripts/noninferiority.py
evals/scripts/replay_targets.py
evals/scripts/rule_cases.py
evals/scripts/seed_defects.py
hooks/lib/console.py
skills/agent-contract/SKILL.md
skills/code-review/SKILL.md
skills/settle/rule-changes.md
skills/verify/SKILL.md
tests/behaviour/test_a_cited_section_stands_in_its_file.py
tests/behaviour/test_evals_layout.py
tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py
tests/behaviour/test_the_sealer_guarantees.py
tests/censuses.py
tests/evals/test_noninferiority.py
tests/evals/test_rule_cases.py
tests/github/test_rules.py
tests/test_censuses.py
tests/text/test_a_cited_commit_outlives_the_squash.py
tests/text/test_a_question_says_who_can_answer_it.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py
```

The phrase sample, the second command, exit 0, 72 lines. It is a sample,
because a sentence in other words is outside it (`gaps.md`). Each hit
falls in one of six kinds:

- a line of the closed set as S1 to S4 left it, in `evals/README.md`, the
  script or its test module, the three pass rules and their numbers among
  them;
- the script's or the test module's name, in a usage line or a citation;
- a rule number of another document, as at `agents/crafter.md:64` and
  `agents/framer.md:146`, which cite contract rules;
- `docs/running/measuring-a-run.md:85-87`, which the design's
  `## Rule changes` changes at the settle;
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py:691-694`,
  #1255's file, whose example of a numbered list outside the contract stays
  true because the pass rules stay numbered;
- a word that is not about the suite: "proved once" in
  `docs/checks/the-stamp.md:93`, "no worse than the row" in
  `skills/verify/scripts/broad_gate.py:1502`, "approved on" in the two
  stamp files, and "fix-pass rule" in
  `tests/text/test_a_moved_rule_leaves_its_definition.py`.

The output:

```
agents/crafter.md:64:    (rule 3), the account the rule *Before you hand back, your range and the
agents/framer.md:146:linter, no typechecker and no `seal gate` (rule 2). The directory is gone
docs/checks/the-stamp.md:93:the right payload. A screenshot of the probe proved once that such bytes
docs/running/measuring-a-run.md:85:criterion and not a band in this sense: the pass rules of
docs/running/measuring-a-run.md:87:rewrite proved itself not worse, and they file nothing. A reading past
evals/README.md:4:`scripts/noninferiority.py`. `claude plugin eval` reads a case at any depth
evals/README.md:11:Run the suite through `noninferiority.py run`, not through
evals/README.md:23:`scripts/noninferiority.py run` runs one agent's cases on one side and
evals/README.md:37:are read by one reader. `compare` writes the record the three pass rules of
evals/README.md:38:`noninferiority.py#verdict` judge:
evals/README.md:54:`tests/evals/test_noninferiority.py` recomputes the record. Nothing in the tree
evals/README.md:59:its count reads as 0, which no pass rule reads.
evals/README.md:62:without a run.** `noninferiority.py regrade --side IN.json --suite-rev REV
evals/README.md:99:The path of the tree `noninferiority.py run` loads is the base directory of
evals/README.md:102:`tests/evals/test_noninferiority.py` *Test_run_side* refuses one that does.
evals/README.md:127:python3 evals/scripts/noninferiority.py run --agent proofer --rev <merge base> \
evals/README.md:129:python3 evals/scripts/noninferiority.py compare --agent proofer --phase N \
evals/scripts/behaviour.py:8:its kind for `noninferiority.py`: `reach-`, `shape-`, `truth-`.
evals/scripts/noninferiority.py:4:  noninferiority.py run --agent A (--rev REV | --tree DIR) --out FILE.json
evals/scripts/noninferiority.py:6:  noninferiority.py run --from-raw FILE.raw --out FILE.json
evals/scripts/noninferiority.py:7:  noninferiority.py compare --agent A --phase N --old OLD.json --new NEW.json
evals/scripts/noninferiority.py:9:  noninferiority.py check RECORD.md
evals/scripts/noninferiority.py:10:  noninferiority.py model RECORD.md
evals/scripts/noninferiority.py:11:  noninferiority.py regrade --side IN.json --suite-rev REV --out OUT.json
evals/scripts/noninferiority.py:44:three pass rules judge, a smoke run for gross breakage of the agent's
evals/scripts/noninferiority.py:761:    """`(verdict, [reason])` the three pass rules give NUMBERS, the merged
evals/scripts/noninferiority.py:825:            f"side, fewer than the baseline's {old_total}/{runs} (rule 1): {fell}"
evals/scripts/noninferiority.py:831:                f"the baseline passed it {op}/{oruns} (rule 2)"
evals/scripts/noninferiority.py:837:                f"the new side ({np_}/{nruns}) (rule 3)"
evals/scripts/noninferiority.py:967:    lines += [f"- {r}" for r in reasons] or ["- every pass rule holds"]
skills/verify/scripts/broad_gate.py:1502:    no worse than the row itself. And a directory at the root named like a
skills/verify/scripts/seal_stamp.py:97:# The red wax seal the owner approved on 2026-10-31 (#1174). The owner chose
tests/behaviour/test_a_cited_section_stands_in_its_file.py:691:    such as the behaviour suite's pass rules, so only `contract rule <N>`
tests/behaviour/test_a_cited_section_stands_in_its_file.py:694:    text = f"pass rule {max(numbers) + 1} holds"
tests/behaviour/test_evals_layout.py:13:`evals/scripts/noninferiority.py` reads: a scaffold in every case, one grader
tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py:8:`tests/evals/test_seed_defects.py`. `evals/scripts/noninferiority.py`'s are in
tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py:9:`tests/evals/test_noninferiority.py`.
tests/censuses.py:26:`evals/scripts/noninferiority.py` loads it by path, without pytest, to mask
tests/censuses.py:919:    `evals/scripts/noninferiority.py#masked` reads a kept round record by
tests/evals/test_noninferiority.py:1:"""`evals/scripts/noninferiority.py`, one class per function.
tests/evals/test_noninferiority.py:3:Rebuilt by #942's phase 5 from the `noninferiority.py` half of one
tests/evals/test_noninferiority.py:7:and reach graders against a baseline by three pass rules, and reads a side
tests/evals/test_noninferiority.py:10:The pure units, the pass rules, the record's writer and reader, the trace
tests/evals/test_noninferiority.py:37:TARGET = "evals/scripts/noninferiority.py"
tests/evals/test_noninferiority.py:39:NI = load_module(os.path.join(ROOT, *TARGET.split("/")), "noninferiority_under_test")
tests/evals/test_noninferiority.py:42:    "behaviour_for_noninferiority",
tests/evals/test_noninferiority.py:558:            "import noninferiority as ni\n"
tests/evals/test_noninferiority.py:1484:    "rule 1: the total falling by one shape run": (
tests/evals/test_noninferiority.py:1488:    "rule 1: the total falling by one reach run": (
tests/evals/test_noninferiority.py:1492:    "rule 1: a new side passing more often": (
tests/evals/test_noninferiority.py:1496:    "rule 1: a reach run lost and a shape run gained share one total": (
tests/evals/test_noninferiority.py:1505:    "rule 2: a grader failing every new run where the baseline passed it, the total held": (
tests/evals/test_noninferiority.py:1514:    "rule 2: a grader the baseline never passed, failing every new run, is not named": (
tests/evals/test_noninferiority.py:1518:    "rule 1: a grader the baseline lacks does not offset a lost run": (
tests/evals/test_noninferiority.py:1527:    "rule 1: a shape grader failing as often as on the baseline": (
tests/evals/test_noninferiority.py:1531:    "rule 3: a reach grader the baseline lacks, short of every new run": (
tests/evals/test_noninferiority.py:1535:    "rule 1: a shape grader only the baseline carried, in a case both sides ran": (
tests/evals/test_noninferiority.py:1606:                    "the baseline's 4/4 (rule 1): c1/shape-report-exists 1/2 against 2/2"
tests/evals/test_noninferiority.py:1617:                    "the baseline's 4/4 (rule 1): c1/reach-proofer 1/2 against 2/2, "
tests/evals/test_noninferiority.py:1620:                    "where the baseline passed it 2/2 (rule 2)",
tests/evals/test_noninferiority.py:1622:                    "the new side (1/2) (rule 3)",
tests/evals/test_noninferiority.py:1740:        assert text.endswith("\nVerdict: pass\n\n- every pass rule holds\n")
tests/evals/test_noninferiority.py:1746:            "side, fewer than the baseline's 2/2 (rule 1): c1/shape-x 1/2 against 2/2\n"
tests/evals/test_noninferiority.py:1894:        assert any("(rule 1)" in p for p in problems)
tests/evals/test_noninferiority.py:1919:                "the new side (1/2) (rule 3)"
tests/evals/test_rule_cases.py:6:generated truth is read back through `noninferiority.py#grader_from`, the
tests/evals/test_rule_cases.py:26:ni = load_script("noninferiority")
tests/skills/test_seal_stamp.py:46:# The wax seal's fifteen colours the owner approved on 2026-10-31 (#1174) and
tests/skills/test_seal_stamp.py:153:# wax seal the owner approved on 2026-10-31 (#1174), transcribed from its SGR
tests/text/test_a_moved_rule_leaves_its_definition.py:514:    assert paragraph, "`agents/crafter.md` lost its fix-pass rule"
tests/text/test_a_moved_rule_leaves_its_definition.py:556:        assert clause in paragraph, f"the fix-pass rule lost {clause!r}"
tests/text/test_a_moved_rule_leaves_its_definition.py:563:        assert gone not in paragraph, f"the fix-pass rule still says {gone!r}"
```

The file listing, `git ls-files '*non_inferior*'`, exit 0, prints nothing.
