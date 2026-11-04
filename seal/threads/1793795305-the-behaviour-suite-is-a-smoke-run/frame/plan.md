# Implementation Plan: the behaviour suite is a smoke run (#1254)

## Technical context

The work narrows one verdict and corrects what states it. Every coordinate
is read at `bac426446`.

- `evals/scripts/noninferiority.py#verdict` (lines 776 to 912) runs its
  `no result` checks first, then rules 1 to 5 in order, and gathers reason
  lines. Rule 3 is the block from the `common = sorted(` line to the loop
  over a grader the baseline lacks. That block stays as it is, except for
  the suffix of its three reason lines. Everything after it (rules 4 and 5)
  and everything between the `unknown` check and rule 3 (the `unknown`
  check, rule 1 and rule 2) goes. `cheaper_model` calls `verdict` for its
  `no result` alone, so it follows the narrower set with no edit of its own.
- `merged`, `render`, `cost_rows`, `parse_record` and `check_record` keep
  building, writing and reading every figure. Only `render`'s title line
  changes (design *Scope* S3).
- `tests/evals/test_noninferiority.py#VERDICTS` drives
  `test_accepts_a_side_no_rule_fails` (rows that expect
  `pass`) and `test_refuses_a_side_a_rule_fails_or_numbers_that_give_no_result`
  (the rest). A row moved from `fail` or `no result` to `pass` moves from
  the second test to the first, so the red to show for each is the first
  test run against the verdict before S2. The way to show it is to commit
  the test change first, or to run it with S2's hunk stashed. Either is
  the crafter's choice, and the phase record says which.
- `README.md:356-358` and `README.ko.md:362-364` are one bullet in two
  editions, and they change in one commit.
  `tests/behaviour/test_both_editions_carry_the_same_folds.py` names both
  (executed: `git grep -l` over `tests/`), so the phase runs it.
- The renamed module's case reads `evals/behaviour/proofer/` and imports
  `test_rule_cases.truth_regex`. Only its file name changes. Its case
  function and docstring stay, because neither claims anything about a
  rewrite.

**The enumeration the hand-back reports (contract rule 12).** The closed
set is the diff, plus `evals/README.md` *The behaviour suite*,
`evals/scripts/noninferiority.py` and `tests/evals/test_noninferiority.py`,
each read whole. The open part, the other sentences of the tree, is found
by two commands and one file listing. All three ran at `bac426446`
(executed), and their hits are in design *Grounding*'s row on the
sentences that call the suite the proof of a rewrite:

```
git grep -l -i -E 'evals/README|noninferiority|evals/behaviour|behaviou?r (suite|evals?)|행동 eval' -- ':!seal/' ':!.test_durations' ':!evals/behaviour/'
git grep -n -i -E 'non[-_ ]?inferior|not worse|no worse|proved? (on|not|itself)|five pass|pass rules?|FALSE_MARGIN|TOKEN_MARGIN|\(rule [1-5]\)|"rule [1-5]:|is proved on|증명하는' -- ':!seal/' ':!.test_durations' ':!docs/experiments/' ':!evals/behaviour/'
git ls-files '*non_inferior*'
```

The first is a census of every file that names the suite. The second is a
phrase sample: a sentence can claim proof in a wording no command here
matches, and the hand-back calls it a sample. The third lists a file whose
name makes the claim, which no content search finds. `docs/experiments/` is left
out because its documents are dated and are not policy (`docs/README.md`,
read). The settle does not write there.

**Failure scenario of the chosen approach, six months on.** A rewrite keeps
every shape and reach grader green and loses a real finding the proofer
used to make, and the smoke run says `pass`. That is the trade the measure
made. Recall is still written in the record, so the next measurement reads
recall from the records again. The proofer's reading of the diff is what
judges a shift in meaning. If a defect of a rewritten preload is found in
use that the old recall rule would have caught, that issue is the record
that reopens rule 1.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Remove the suite and its runner (replaces the structure) | 13 `check:` lines in 7 shipped files name cases that nothing then runs or keeps (design *Grounding*). The one catch on record was read by the shape graders, and the suite is the only thing that drives a whole agent session. The measure weighed this as an equal and decided `narrow` | Rejected. The premise that keeps the structure is checked: the catch came from rule 3, and the measure shows it (instances 4 and 5) |
| A2 Keep the five rules and rewrite only the lead sentence | The verdict keeps failing rewrites on recall, the false-finding rate and tokens that no reading found worse. The README would then say one thing while `verdict` does another | Rejected. The issue's *Done when* asks `verdict` to judge what the section states |
| A3 Narrow rule 3 too, to "a grader failing every new run" | The one catch was 5 of 18 records missing a line, then 1 of 18. A grader that passed 13 of 18 runs fails no "every run" rule, so the narrowed rule would have passed the only defect the record shows | Rejected. Rule 3 stays whole |
| A4 Keep `no result` for unknown tokens, tool calls or preload bytes | A side whose trace lost `modelUsage` would be refused although its shape and reach graders were read, so a figure that judges nothing would still block a verdict | Rejected. Unknown is written `unknown`, as spend already is |
| A5 Keep the suffix `(rule 3)` on all three reason lines, or drop rule numbers | With `(rule 3)` kept, a reader looks up rule 3 in a three-rule list and finds only the last clause. With numbers dropped, a reason no longer points at its clause, and #1255's file loses its example of a numbered list outside the contract | Rejected. The rules are numbered 1 to 3. The cost is that a later measurement reading `(rule N)` across old and new records would mix two numberings. The title (`smoke run` against `non-inferiority`) tells the two kinds of record apart |
| A6 Rename `evals/scripts/noninferiority.py` and its test module | The issue names both paths as its coordinates. `tests/censuses.py`, which #1255 owns, cites the script by path, so two branches of one release would edit that file | Rejected. Out of scope (design *Scope*, Out) |
| A7 Keep the record's title `non-inferiority` | Every record would claim non-inferiority above `Verdict: pass`, which is the claim the issue takes back | Rejected. S3 |
| A8 Keep the module name `test_a_rewritten_definition_proved_non_inferior.py` | Every test listing and every docstring that cites it keeps saying that the suite proves a rewrite | Rejected. The cost is one `git mv` and four docstring lines, and its one `.test_durations` entry is 0.012 seconds (design *Grounding*) |
| A9 Remove `regrade` as well, since truth graders judge nothing | `model` reads truth graders to choose the sealer's model, and `regrade` re-reads them on a paid side. Removing it changes something the measure did not decide | Rejected for this work item |
| A10 Two phases, the verdict and then the other sentences | One more crafter spawn and one more phase record for five edits whose wording follows S1, all read by the same review round | Rejected. One phase |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* S1, S2, S3, S4 and S5 | Each changed case of S4 is shown red against `verdict` before S2, and the phase record says how (contract rule 15). Then `bin/test -q tests/evals/test_noninferiority.py tests/evals/test_replay_targets.py tests/evals/test_rule_cases.py tests/evals/test_seed_defects.py tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py tests/behaviour/test_evals_layout.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_docs_line_wrap.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` exits 0. The three commands of *Technical context* are run at the phase's commit, and the hits are read against acceptance A7 | eb4d31b60 |

## Operational impact

- **The version moves in this work item.** It is the first work item of
  `release/v0.32.0` (the spawn's finding; design *Grounding*). The commit that
  adds `seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/changelog.md`
  also moves `.claude-plugin/plugin.json` from `0.31.2` to `0.32.0`, as
  `docs/releasing/branch-and-release.md` *Cutting a release* states. That
  section names the orchestrator as the one who makes this move. The
  fragment carries no `### Process changes` table (design *Grounding*).
- **What a person reads changes.** A record written by
  `noninferiority.py compare` after this release opens with `smoke run`, and
  it fails only on shape and reach graders. A side that was `no result` for
  an unknown token count now gets a verdict. The fragment states both.
- No migration, no new environment variable, no new dependency, and no paid
  run.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | The frame is folded to phase 1 as built: S1 gains the row-count paragraph, S4 and `## Removes` state the `VERDICTS` rows and the cases phase 1 reworked, A2 and the plan name the tests and the module as renamed, and the measure is cited at `569780eff` | The crafter's hand-back named each statement HEAD contradicts (phase record gaps 1 and 2, D1, D3 to D5); the measure's commit `3937d861` is reached by no `main` or release ref, so `tests/text/test_a_cited_commit_outlives_the_squash.py` refuses it, and `569780eff` (#1257's squash onto `main`) holds the same file byte for byte (executed: `git diff --quiet`). The same unreached citation stood in all three frames of the release, carried from the issue bodies, so the issue bodies of #1254, #1255 and #1256 are corrected in place as its prevention home | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
