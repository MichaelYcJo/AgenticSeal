# Questions for the planner: the stop judgment holds against later rows (#1288)

The tree and the records answered these judgments that the issue left open. Each is read where its grounds stand, and none is reopened here:

- Whether a later row may reopen a stop on the rule that a defect a branch causes is fixed where it arises: `frame/design.md` G8.
- Whether the three-round weighing point is the numeric cap the owner declined: `frame/plan.md` *Alternatives considered*, the fifth row.
- Whether a `should` raised after a stop gets its fix or a home: `frame/design.md` G1 and G2.
- Whether the gap in a case that holds no fact the frame states is a finding of a third severity: `frame/plan.md` *Alternatives considered*, the fourth and sixth rows.
- Which file holds the proofer's weighing: `frame/plan.md` *Alternatives considered*, the seventh row.
- Whether `docs/running/the-run.md:48` is edited directly or through `## Rule changes`: `frame/design.md` G13, and `frame/plan.md` *Alternatives considered*, the eighth row.
- Whether #97 closes with this work: `frame/design.md` *Scope* item 10.

One assumption stands, because a different answer would not change what is built:

- A stop row's catch-against-cost weighing reads the next round's price as close to a finding round's, as `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* says now. The settle reads each stop row against what it cost and caught.

Q1 is open, and only the owner can answer it. Under `Automation` `yes`, the build goes on on its default, and the pull request body names the row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Is a fix that changes no assertion and no shipped file, such as a test's comment or name, read by the sealer as a fix confined to the work item's records is, so that it owes no verifying round? (#1288 *Done when*, bullet 2) | a person: the repository owner | **No.** The table of `skills/core/SKILL.md` *Judgment is not licence to skip a party* and `skills/code-review/scripts/chain_check.py`'s records arm stay as they are. Every change outside the work item's records is read by a round, which is what the invariant protects. Before a stop, such a fix rides in a fix pass another fix already owes, or costs its own round. After a stop, it takes a home and is not fixed in the branch (`frame/design.md` *Scope* item 1). **Yes, for a comment-only change to a Python file under `tests/`.** The invariant's third row and the records arm admit, after the last round, a commit whose changed `.py` files parse to the same `ast` before and after. A script reads that exactly (`frame/design.md` G14), and the sealer reads the change. A rename, a docstring and a test in another language stay outside it, because `ast` tells them apart or cannot parse them. The records arm, which ships to every user's repository, gains a parser reading for one language and one layout. **Yes, for any change to a test that changes no assertion.** The third row's exception widens to that, and the sealer judges whether an assertion changed. That is a reading of meaning, so the records arm can hold no exact fact for the row, and the change is read by the sealer and by no round: the party the invariant names is skipped for a file outside the records | **No**: the invariant and the records arm stand, and the build writes nothing for this row | open |
