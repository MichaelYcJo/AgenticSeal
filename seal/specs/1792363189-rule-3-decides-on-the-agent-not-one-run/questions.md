# rule 3 decides on the agent, not on one run (#966) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**What the tree answered, so nobody reopens it.** #966's decision leaves the
statistic's details open. Each was settled from the tree, and the grounds
are where a reviewer can open them.

| Judgment | Answer | Grounds |
|---|---|---|
| One total, or a total per kind | One total, shape and reach pooled | #966 `## Decision`, "a side's total shape and reach passes"; #957 `phases/phase-2.md` §*Run 2*, the pooled row 66 of 72 against 70 of 72 the decision was made against. On #957's six records both readings give the same verdicts. `plan.md` Alternatives |
| Which graders the totals cover | Shape and reach graders both sides ran. One the baseline lacks keeps its present judgment (every new run passes). One only the baseline carried stays unjudged | `noninferiority.py#verdict`, the comment above the "different number of times" check, and the existing cases for both. Under the fixed suite (#971) neither arises in 0.22.2 |
| A margin on the total | None: the new total must not fall below the baseline's | #966's decision chose aggregation over a tolerance |
| Who the naming clause names | A common grader with 0 new passes where the baseline passed it at least once. A grader both sides fail every run is not named | #966 `## Decision`, word for word |
| Whether a falling total names graders | Yes, every common grader whose passes fell | Rule 1 already names the truths that lost a find. A `fail` with no coordinate sends the reader to the table |
| How the re-read gets its input | `compare` over #957's committed side JSONs, not `run --from-raw` | The raw directories are gone (`spec.md` Scope, Out). #957 `guarantee.md` shows the committed sides byte-identical to `run --from-raw`'s output |
| Where the re-read records go | `evals/957-<name>.md` in this work item. #957's records stay as judged | #957 `phases/phase-2.md`, "the rules are not changed after a run to pass it" |

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the `model` subcommand (`noninferiority.py#cheaper_model`) follow rule 3's aggregation? It still decides Sonnet over Opus per grader, truths, shape and reach alike, so one run can still decide the sealer's model. The tree cannot answer it: #966's decision names rule 3 of `verdict`, and the model rule was #957's own default (Q2 there), a choice of which risk to accept that only the owner holds | a person, the repository owner | **leave it**: `model` stays per grader and stricter than `verdict`. **follow**: its shape and reach comparison becomes the same total and naming clause, while truths stay per grader. That is a second change to a function this frame keeps out of scope | leave it. It does not block this build, because nothing here touches `cheaper_model` | open |
