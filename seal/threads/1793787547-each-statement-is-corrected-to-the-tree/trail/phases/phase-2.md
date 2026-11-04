# Phase 2: 1793787547-each-statement-is-corrected-to-the-tree

## What this phase found

**The frame holds for this phase.** I checked it against the tree at
`4bb409006` before the first edit (read, unless marked).

- `evals/scripts/rule_cases.py` held each coordinate *Scope* S3 gives: the
  three `# Feature Specification:` titles at `:263`, `:357` and `:764`, the
  four scenario headings without ` *(mandatory)*` at `:270`, `:363`, `:466`
  and `:771`, `SEALER_ROUND`'s `# {item} — review round 1` at `:795`, and
  `routing(branch, planning, implementation)` at `:157`, whose title was
  `# routing` and whose one caller at `:203` held `item`.
- The three templates open with the forms S3 names:
  `templates/records/sdd-design.md:1` `# Design: <work item>`,
  `templates/records/sdd-round.md:1` `# Review round <N>: <work-item-id>`,
  `templates/records/sdd-routing.md:1` `# Routing: <work-item-id>`. The
  design template's scenario heading at `:13` carries ` *(mandatory)*`.
- `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py#hits` skips a
  line only where the whole line is in `RECORD_LINES` (`:151`). So the
  exemption has to hold the heading in its new spelling, as the plan's
  *Technical context* says.
- `git grep` for the old forms under `evals/` listed the 17 `scaffold.sh`
  files and the generator (executed).

**What the regeneration changed.** `python3 evals/scripts/rule_cases.py`
exited 0 and changed exactly the 17 `scaffold.sh` files (executed: `git
status --porcelain`). A tally of the changed lines, with each work item id
replaced by one token, gives the counts the design's *Grounding* row
predicts: 17 routing titles, 11 scenario headings, 10 design titles (5
sealer, 4 crafter builds, 1 proofer) and 5 round titles (executed). No
other line of any case changed.

**The routing title takes the work item id as a parameter.** `routing()`
now takes `item` first, and its one caller passes it (*Data &
interfaces*). The formatter wrapped the caller's line, which changes no
behaviour. The docstring says whose declaration it is.

**The `RECORD_LINES` comment.** It no longer says that the heading lacks
the template's ` *(mandatory)*`, since the exempt line now carries it. The
rest of the comment is unchanged.

**Seen red and mutation.** No case was written new, so contract rule 15
has nothing to show red. I judged that no unit adds behaviour: the
generator's change is the text of four fixture forms, and the new
parameter carries a value the caller already held into one title. I still
ran `seal mutate` at `d66106009` to show that the narrow cases read each
change (executed):

- `RECORD_LINES` back to the old heading, run over
  `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`: verdict
  `red`. `test_no_case_file_holds_a_refused_word` failed on `scenarios` at
  each of the 11 scaffolds that hold the heading. So the exemption change
  was needed, and the case reads it.
- Three mutants of `rule_cases.py` in one batch, each a title put back in
  its old form (the routing title, `SEALER_SPEC`'s design title and
  `SEALER_ROUND`'s title), run over
  `tests/behaviour/test_evals_layout.py -k test_the_sealer_cases_are_the_generators_output`:
  the baseline passed and all three mutants were `red`. A single run of the
  routing mutant failed on `differs:` for each of the five sealer
  scaffolds.

The tree was clean after each restore (executed: `git status --porcelain`
printed nothing).

**Only the sealer cases are held to the generator by a case.**
`tests/behaviour/test_evals_layout.py#test_the_sealer_cases_are_the_generators_output`
compares `evals/behaviour/sealer/` alone, and its docstring says so. For
the other twelve cases, A3's second command is the check: after the
commit, `python3 evals/scripts/rule_cases.py && git status --porcelain
evals/behaviour` printed nothing (executed, exit 0). A12 adds no
mechanism, so this phase adds no case for them.

**Other places that state the old forms, a sample.** `git grep` outside
`seal/threads/` for `Feature Specification`, for `— review round <N>`, for
a `# routing` line and for a statement that the heading lacks
` *(mandatory)*` finds only test fixtures under `tests/`:
`tests/e2e/teammate/test_teammate_flow.py:64`, round titles in
`test_noninferiority.py`, `test_replay_targets.py`, `test_broad_gate.py` and
`test_chain_check.py`, and `# routing` in `test_finding_counts.py`,
`test_optin.py`, `test_chain_check.py`, `test_seal.py` and `test_settle.py`
(executed). Each is the class *Out of scope* O3 keeps out. `evals/README.md:102`
says a record shape the plugin's templates write is exempt, which the
change makes truer and does not contradict (read). This list is a sample,
because the searches match spellings.

**Narrow run.** The plan row's five modules in one `bin/test ... -q`, over
the tree `d66106009` commits, before the commit: 52 passed (executed, exit
0). The collection lists cases from each of the five modules (executed:
`--collect-only`). `uvx ruff check` and `uvx ruff format --check` on the two
changed Python files exited 0 (executed). The A3 `git grep` for the old
forms under `evals/` printed nothing, exit 1 (executed).

**Phase boundary run.** This is the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, run as
one `bin/test ... -q` over 22 modules. They are the plan row's five, the
modules that name `rule_cases`, `evals/behaviour`, `scaffold.sh` or the
`RECORD_LINES` module, the modules that walk the tree and name `.py`,
`.sh` or `evals`, and the four that read this work item's records
(`test_a_phase_hands_the_next_one_a_record.py`,
`test_chain_hooks_hardening.py`, `test_unverified_rows_close.py`,
`test_docs_line_wrap.py`). Each list came from `git grep -l` over
`tests/*.py`. From those lists I left out, by their names and without
reading them, the modules whose subject is a script's own fixtures
(`test_chain_check.py`, `test_mutation_check.py`, `test_arm_check.py`,
`test_agentic_pytest_record.py`, `test_conftest.py`) and the record readers
whose subject is another file. It ran over `d66106009` with this record, the
`gaps.md` row and the Status cell in the working tree: 899 passed and 9
skipped (executed, exit 0). The selection is my reading of "a module that
reads a path the phase changed". A module that reads those files through a
helper these searches do not name is outside it, and the broad run covers
that.
