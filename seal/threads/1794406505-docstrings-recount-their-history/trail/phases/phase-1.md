# Phase 1: 1794406505-docstrings-recount-their-history

## What this phase found

**The count at the base is the one design G5 states (design *Scope* item
8).** The counting command of design *Data & interfaces*, taken from that
file into the phase's scratch directory and run with `python3 -I` at
`38123f839`, printed `{'files': 50, 'lines': 33491, 'blank': 2776,
'prose': 13216, 'code': 17499, 'hits': 869}`, and its `--hits` listing held
133 lines of `skills/verify/scripts/session_cost.py`, the figure *Scope*
item 2 gives (executed). At `18ffe5ff0` it prints `{'files': 50, 'lines':
33406, 'blank': 2776, 'prose': 13131, 'code': 17499, 'hits': 755}`, and 19
of those lines are `session_cost.py`'s (executed). The code line count is
the same at both commits.

**The frame holds against the tree, except for two statements.** Each is a
claim about the tree, and neither changes what this phase builds.

- Design G9 says three cases read a script's prose. A fourth does:
  `tests/skills/test_session_cost.py::Test_module::test_the_module_states_the_rule_and_the_two_shapes_it_misses`
  holds `token_thirds`' docstring to name the check's path, the subscript
  and division residuals, and `#192`, "the issue the class came from"
  (executed: the phase boundary run over the rewritten docstring, before the
  case changed, failed on `assert "#192" in text`; the commit it ran at was
  amended into `18ffe5ff0` to carry the case's change). G9 calls its own list a sample, so the
  broad gate would have found this case, and the phase boundary run found it
  first. `#192` there is the provenance of a present fact, which design
  *Scope* item 1 removes. As `frame/plan.md` *Phases* asks, the case changed
  in the same commit as the sentence: it keeps its three present facts and
  loses the `#192` assertion. Judged against `skills/core/SKILL.md` *The
  rule a mechanism is kept against*: a change removes what stood on the old
  fact in the same commit.
- Design S1 says the code command exits 0 for a phase's range. For
  `c21b4248f..18ffe5ff0` it prints `2 .py files differ in text; code differs
  in: ['tests/skills/test_session_cost.py']` and exits 1 (executed). The one
  file it names is the case above, whose code changed by the plan's own
  allowance. `skills/verify/scripts/session_cost.py` is not in that list, so
  its code with every docstring removed is the same at both commits. S1 and
  `frame/plan.md` *Phases*' allowance for a pinning case disagree for any
  phase that meets such a case. This record reads S1 as holding for the
  scripts the phase rewrote, and names the disagreement for the orchestrator.

**Every docstring and comment of `session_cost.py` was read, not only the
hit lines.** The file was read whole, start to end, and each sentence was
judged by design *Scope* item 1. Sentences outside the hit listing went or
were rewritten where they recount: `plan.md`'s accepted alternative and
failure scenario, `questions.md` Q1 and Q4, work item
`1788873620-two-in-range-values-make-one-that-is-not`, "round 1's 🟡 1",
"no longer", "was", "had", "now" and "today" where they set the present
against a former state, and `skills/verify/orchestration.md` "prescribed"
or "wrote out" a procedure "until this was written".

**The 19 hit lines that stay, each with its keep class.**

| Line at `18ffe5ff0` | Class | Why it stays |
|---|---|---|
| 667 | K4 | `only_reads`: the owner's answer that any `<<` keeps a line out, its issue as the one coordinate |
| 819, 830, 1198, 1261, 1718 | K3 | "the harness measured here" and "measured over the same three runs" name the observed harness and the evidence of `DELEGATING` |
| 2304 | K3 | "`mostly` is measured": the evidence the printed word rests on, the wait being 98% of the interval |
| 1268, 2303 | K2 | "a measured run": a run the meter reads |
| 1396, 1425, 2045, 2373, 2951, 2976, 2989 | K2 | "measured" for what the meter reads now: a turn, a segment, a transcript read on its own or beside another |
| 2633, 2653, 2657 | K5 | the comments over the printed comparability lines of `report_segments`, which name #377 and #642 and stay unchanged as printed text; each comment states the shape an older reading carries and why the printed line names an issue rather than a release |

**Five sentences fit no class cleanly, and `frame/questions.md` Q1's
default kept each, rewritten in the present tense.**

- `count`'s docstring: "That exception is why this was first recorded as
  harmless" became "why a probe on `output_tokens` alone reads as
  harmless". The history went; the caution to the next prober stays.
- `measure_segments`' docstring: "The 700 ... corrects an inherited one. #145
  published *a median of about 1,000 seconds*" became "it is not the 1,000
  `spawn_cycles` carries ... 1,000 is the MEAN (1,018)". The two figures
  still stand side by side in the file, so the sentence that tells them
  apart stays.
- `report_breaches`' docstring: "round 1 of #120 spawned two agents and
  disclosed neither" became "a reviewing agent has spawned two agents and
  disclosed neither". It is the evidence that delivering the rule is not
  enough, K3 without its provenance.
- `report_breaches`' docstring: "Making it an exit code is a later work
  item's" became "a choice to make against these readings rather than
  against a guess". It states why the line stops nothing.
- `analyse`'s docstring held three paragraphs on how `span_s` and the family
  split moved at #300, #377 and #642. The rules themselves are stated at the
  arithmetic, in `family`, `runs_git` and `only_reads`, so the history went
  whole. One present sentence stays, because no other place in the function
  says it: a reading under an earlier family rule differs in `by_family`,
  `unnamed` and the two repeats figures, and `report_segments` prints which.

**A disagreement the file held before this phase, and still holds.**
`DELEGATING`'s comment and `spawn_cycles`' docstring say a subagent runs for
"a median of about 1,000 seconds". `measure_segments`' docstring says that
over its population of 43 runs the median is 716 s and 1,000 is the mean.
The two populations differ (67 spawns of three runs against 433 segment
rows), so the tree cannot say whether the first figure is a median of its
own population or a mean. A prose-only phase does not re-measure it, and
`gaps.md` *Not done* holds it.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings, the *A comment or docstring inside source* row of
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*, and the one test edit removes an assertion and adds no case.

**S6 and S5 at `18ffe5ff0`.** `uvx ruff check` and `uvx ruff format --check`
over `skills/verify/scripts/session_cost.py` and
`tests/skills/test_session_cost.py` both exit 0, and both name the files
they read (executed). The phase boundary set ran as one command,
`bin/test tests/skills/test_session_cost.py tests/text tests/behaviour -q`,
over the tree this record is committed with: 2042 passed, 8 skipped, exit 0
(executed). G10's module, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
is in it. `tests/skills/test_seal.py` names the script's path in a
parameter and does not run it, so it is not in the set.
