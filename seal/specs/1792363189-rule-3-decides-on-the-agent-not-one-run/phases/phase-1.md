# 1792363189-rule-3-decides-on-the-agent-not-one-run — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | d6945b16 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Rule 3 of `evals/scripts/noninferiority.py#verdict` aggregates per agent,
as the owner decided in #966's body. Cases first: add S1 to S6 and rename
the two per-grader cases (S7), each seen red as `spec.md` says. Then
rewrite `verdict`'s rule 3 to the total and the naming clause, with the
reason lines of `spec.md` *Data & interfaces*. Rewrite the README, the
module and `verdict` docstrings and the rule 3 case comments in place (S8).
Verified by `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py
tests/test_evals_layout.py -q` exiting 0, with the output of `git grep -n
"at least as often" -- evals tests` quoted here. Build on `questions.md`
Q1's default, `leave it`, so `cheaper_model` is not touched. Phase 2 (the
#957 re-read and the changelog fragment) is not part of this phase.

## What this phase found

**The frame holds, with two corrections to how it is verified.** The
coordinates in `plan.md` §*Technical context* match the tree at 881cc7be:
`verdict` starts at line 577, rule 3's loop sat at 657 to 669, and the
"different number of times" check returns `no result` for any common grader
whose run counts differ, so every grader in the totals has equal runs on
both sides.

- **S2's `CASES` entry is the renamed S7 case.** S2's numbers
  (`shape-report-exists` 2/2 to 1/2, nothing else) are the numbers of the
  per-grader shape case S7 renames. A second entry with the same numbers
  would cover nothing the first does not, so S2 is that renamed case,
  `rule 3: the shape and reach total falling by one shape run`, plus the
  reason assertion.
- **S8's grep cannot see the two docstrings.** Both docstring sentences
  wrapped inside the phrase, as "at / least as often" and "at least as /
  often". At 881cc7be, `git grep -n "at least as often" -- evals tests`
  found `evals/README.md:32` alone. So the grep proves the README sentence
  is gone and says nothing about the docstrings. A wider grep for "as often"
  and "less often" is quoted below as well.

**How rule 3 is now built.** The totals run over `common`: every shape or
reach grader with old runs and new runs both above zero, sorted by
`(case, grader)`. The total line, the naming lines and the baseline-lacks
lines are appended in that order, as *Data & interfaces* says. The
baseline-lacks branch is unchanged in its condition and its text. It now
sits in its own loop after the naming lines, so the order holds.

**The reason assertions are a new test function.** It is
`test_rule_3_names_the_total_and_each_grader_failing_every_new_run`, over a
table of three entries, each asserting `verdict`'s whole return value. One
entry is S2's, one is S3's. The third puts all three line kinds in one
record, with two graders whose passes fell. It pins the line order and the
`(case, grader)` sort, which no other case reads.

**Each new case seen red.** S1 and S5 were run against the tree before the
code changed. S2's to S6's breaks were each written by `mutation-check`
after the code was committed at d6945b16.

| Scenario | Case | Seen red how |
|---|---|---|
| S1 | `rule 3: one shape grader's lost run offset by another's gained run` | Against 881cc7be's `verdict`: red, the old reason "passed 1/2 on the new side, less often than the baseline's 2/2" |
| S2 | the renamed shape case, and the reason entry `the total falls` | The total check replaced by `if False:`: both red, with the reach rename, S6 and the order entry |
| S3 | `rule 3: a grader failing every new run where the baseline passed it, the total held`, and the reason entry | The naming clause replaced by `if False:`: both red, with the order entry. Its reason entry was also red against 881cc7be |
| S4 | `rule 3: a grader the baseline never passed, failing every new run, is not named` | The naming clause made `if not np_:`, naming every 0/n grader: red, alone |
| S5 | `rule 3: a reach run lost and a shape run gained share one total` | Against 881cc7be's `verdict`: red. Under per-kind totals (either kind falling fails): red, alone |
| S6 | `rule 3: a grader the baseline lacks does not offset a lost run` | The totals' filter widened to graders the baseline lacks (`and v[2] and v[4]` to `and v[4]`): red, with the order entry |

Three more breaks, each red: `common` left unsorted (the order entry), a
grader counted as fallen at equal passes (`<` to `<=`, the S2 entry), and
each of the two new reason texts reworded (the reason entries).

**The phase's checks.** `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py
tests/test_evals_layout.py -q` exited 0 with 88 passed. `uvx ruff format
--check` and `uvx ruff check` on the two Python files both exited 0.

`git grep -n "at least as often" -- evals tests` printed nothing and exited 1.
The wider grep, `git grep -n -e "as often" -e "less often" -- evals tests`,
printed:

```
evals/scripts/noninferiority.py:37:passes on the Sonnet side less often and its spend is lower, else `opus`;
evals/scripts/noninferiority.py:945:    reach, passes on the Sonnet side less often and its spend is lower.
tests/test_a_rewritten_definition_proved_non_inferior.py:179:    "rule 3: a shape grader failing as often on the new side as on the baseline": (
tests/test_a_rewritten_definition_proved_non_inferior.py:187:    "rule 3: a shape grader passing less often than a baseline that fails it": (
tests/test_a_rewritten_definition_proved_non_inferior.py:597:    grader, truth, shape or reach, passes on the Sonnet side less often than
tests/test_the_mode_question_is_asked_once.py:1620:    in `src/` as often as at the top. Taking `cwd` for the repository root
```

None of them states a per-grader rule 3. Lines 37, 945 and 597 are the
`model` subcommand's rule, which `questions.md` Q1 keeps per grader. Lines
179 and 187 name a case by its numbers (1/2 to 1/2, and 1/2 to 0/2), not by
the rule. Line 1620 is about another subject.

**Comments rewritten where they now read false.** The comment above the
1/2-to-1/2 case said every other rule 3 case had a baseline passing every
run or a new side passing more. S1, S3, S4 and S5 break that, so the
sentence is gone. The comment above the reach case the baseline lacks said
no other case gives the baseline zero runs of a grader. S6 does, so it now
says S6's grader passes every run and only this case fails one. The comment
above the 1/2-to-0/2 case now says it lowers the total and is named.

**For phase 2.** The `957-*.md` records will carry the new reason lines.
For `warden-phase-2-run-1.md` that is a naming line for
`seeded-9b644676/shape-findings`, and for `sealer-phase-3.md` a total line,
both in the form *Data & interfaces* gives. `.test_durations` still holds
the two old case names and none of the new ones. `spec.md` keeps it out of
scope.
