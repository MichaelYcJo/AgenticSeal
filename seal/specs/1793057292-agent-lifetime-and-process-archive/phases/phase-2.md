# Phase 2: 1793057292-agent-lifetime-and-process-archive

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | f7fb7028 |

## What this phase was asked

Write the two orchestration files once each. In
`skills/code-review/orchestration.md`, rewrite the fix-pass section in place
under a heading that names both rules: each phase is a fresh smith handed
the phase records, and a fix pass resumes the implementer only below the
threshold phase 1 measured, 806,241 (the orchestrator's answer to Q3,
f60e965c), written with its source and the command that reads it. In the
sealer section, add the `mergeable` reading and the merge route with its
verifying round, delete the paragraph *A hand-back's verification claim is
a claim*, and drop the heading's clause *and a phase is re-run*. In
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*, add the folding rule, the `handoff.md` rule and the prevention-home
rule, and rewrite the acts table's rows. Move every citation of the two old
headings and the pins `spec.md` `## Removes` names (S5 to S9), each pin seen
red against the old text first. Run the touched modules, the document
modules that read these files, `bin/test-layout --check` and `--pairs`, and
`uvx ruff check` and `uvx ruff format --check` over the changed Python
files. Build on `questions.md`'s defaults; stop after phase 2.

## What this phase found

**The frame holds for phase 2, and three of its lists were short of the
tree** (`executed`, a search of every tracked file outside `seal/specs`,
`changelog` and `.test_durations` with whitespace collapsed, so a phrase
wrapped across lines is found). Each was corrected in f7fb7028 under
contract rule 19:

- `skills/verify/orchestration.md` *The broad gate* cites the heading with
  *and a phase is re-run*, wrapped over two lines, which is why the plan's
  single-line `git grep` did not list it. `## Removes` names
  `CONTRIBUTING.md`, `skills/implement/SKILL.md` and
  `skills/implement/orchestration.md` only.
- `tests/test_review_axes.py#test_the_fix_pass_resumes_the_implementer` pins
  the old rule's words (*resuming the session that built the branch*), and
  it went red once the section was rewritten. `## Removes` does not name it.
  It is rewritten in place to pin what the new S5 cases do not: the reason a
  resume is worth taking below the threshold, the fresh spawn where the
  implementer's session is gone, and the limit a compaction leaves.
- `tests/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`
  names the sealer section by its old heading. Its `section` reader matches
  the heading as a prefix, so the old string still found the shortened
  heading and the case stayed green. The string follows the new heading; it
  is not a new pin and had no red to show.

**The heading cannot carry the threshold** (the work). The plan asks for a
heading naming both rules, and its Verified by greps for *fix pass resumes
the implementer*. `tests/test_docs_line_wrap.py` holds this file to 88
columns, headings included, and every wording that kept the phrase and a
condition ran to 89 columns or more. The heading is *Orchestrator: a phase
is a fresh smith, and a fix pass resumes the implementer* (81 columns), and
the condition is in the section's second bold sentence, which rule 18 of
`tests/test_the_rules_have_one_owner.py` pins.

**Three choices the frame left open** (the work). The folding rule names the
orchestrator as the party that folds a decision into the frame, because the
decision reaches the orchestrator and the section is its. The line `plan.md`
carries until the fold sits on a line of its own below the approval line,
as *The plan is approved at the spawn* requires of any line beside it, and
the orchestrator deletes it in the commit that folds. The `mergeable`
paragraph also names `MERGEABLE`, the third value `gh` returns, as the one
under which CI is waited on, so all three values have a reading.

**One phrase of the prevention-home rule keeps the frame's two readings**
(the work). *Scope* item 4 says the home is "a rule in the work item that
rewrites the file the act is read from" and that the orchestrator records it
"on that work item's issue". The section copies those words. Read one way,
the work item is the one in progress; read the other, it is whichever work
item rewrites that file. The framer is the one to settle it.

**Each pin was seen red against the old text** (`executed`, `bin/test
tests/test_the_rules_have_one_owner.py tests/test_broad_gate_rule.py
tests/test_every_orchestrator_act_names_its_delivery.py -p no:xdist -q` with
the tests written and the documents unchanged, 11 failed; the acts-table
module run again with the headings renamed and the rows not yet moved):

| S row | Case | Red against the old text |
|---|---|---|
| S5 | `test_the_owner_states_the_rule[17 each phase is a fresh smith]` | the sentence is in no carrier |
| S5 | `test_the_owner_states_the_rule[18 a fix pass resumes the implementer only below the threshold]` | the sentence is in no carrier |
| S5 | `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` | `ValueError`, no section under the new heading |
| S5 | `tests/test_review_axes.py#test_the_fix_pass_resumes_the_implementer`, rewritten | each of its three phrases counts 0 in f60e965c's file, and each mutant below turns it red |
| S6 | `test_every_orchestrator_act_names_its_delivery` | two rows name headings gone, two headings have no row |
| S6 | `tests/test_broad_gate_rule.py#test_the_acts_table_row_names_the_preflight_and_stays_a_sentence` | 0 rows name the section |
| S6 | `tests/test_broad_gate_rule.py#test_the_broad_gate_section_states_its_own_timing` and `test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn` | the old heading is still cited, and no line is the new heading |
| S7 | `test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` | the section does not say it reads `mergeable` |
| S8 | `test_every_link_names_the_owner[6 the pull request opens once the sealer has sealed]` | `skills/implement/orchestration.md` cites the old heading |
| S9 | `test_a_decision_after_the_frame_is_folded_into_it` | the order does not state the folding rule |
| S9 | `test_a_handoff_file_is_written_only_to_move_the_work` | the order does not state the `handoff.md` rule |
| S9 | `test_a_recurring_problem_gets_a_prevention_home` | the order does not state the prevention-home rule |

S8's grep, `git grep -n "a phase is re-run" -- . ":!seal/specs"
":!changelog"`, prints nothing at f7fb7028 (`executed`, exit 1). The case
`9 a hand-back's verification claim is a claim` and its paragraph are gone.

**Mutations** (`executed`, `bin/mutation-check` after f7fb7028, each batch
bounded at 300 s, the tree clean after each). Twelve mutants of
`skills/code-review/orchestration.md`, one per pinned sentence (the
threshold, the phase rule, the command, the reason, the fallback, the
compaction limit, the `mergeable` command, `UNKNOWN`, the rebase, the
verifying round, `--no-merges`, the order of the merge), run over
`tests/test_the_rules_have_one_owner.py` and `tests/test_review_axes.py`:
12 red, 0 survived. Eleven mutants of `skills/implement/orchestration.md`,
nine over the three new rules and two restoring the old headings in the
acts table, run over the two pin modules and
`tests/test_every_orchestrator_act_names_its_delivery.py`: 11 red, 0
survived. The sentence that the orchestrator deletes the `plan.md` line in
the folding commit is pinned by no case.

**The narrow checks** (`executed`, exit 0 unless named). `bin/test` over
the four changed test modules, `tests/test_every_orchestrator_act_names_its_delivery.py`,
`tests/test_docs_line_wrap.py`, `tests/test_no_passage_is_pasted_into_a_second_file.py`
and `tests/test_one_word_one_meaning.py` returned 148 passed. Thirty-two
document modules that read the changed files returned 870 passed, 8 skipped
and 2 failed: `tests/test_review_axes.py#test_the_fix_pass_resumes_the_implementer`,
rewritten above, and
`tests/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`.
`bin/test-layout --check` and `--pairs` over the four changed test files
refused nothing and named no pair; none declares `TARGET`. `uvx ruff check`
and `uvx ruff format --check` over them report nothing.

**This work item has no `overview.md`, and a case fails on it at the base**
(`executed`, the run above; `read`, the directory at f60e965c holds no
`overview.md`).
`tests/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`
refuses a work item with a `spec.md` and no `overview.md`. No row of
`plan.md` writes one, and phase 2 found no divergence that a removal would
put there, so this phase wrote none. The orchestrator answers it before the
broad gate: phase 4 opens the memo, or the next spawn is told to.

**`.test_durations` still names the removed case**
`test_the_owner_states_the_rule[9 a hand-back's verification claim is a
claim]`, priced at 0.0009 s (`read`). This phase left it for the file's next
refresh: `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness`
fails only where entries the suite no longer collects hold more than
`STALE_SHARE` of the file's seconds. That case reads the whole suite's
collection, so whether it passes is `unverified`, and the orchestrator
answers it.
