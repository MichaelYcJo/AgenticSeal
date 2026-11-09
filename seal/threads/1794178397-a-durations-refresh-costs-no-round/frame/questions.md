# Questions for the planner: a .test_durations refresh costs no review round and no broad run (#1444)

The tree answered these judgments the ticket left open:

- Where the refresh happens, and why not per work item: `frame/plan.md` *Alternatives considered* rows A and F.
- Whether the chain may read a durations-only commit without a round: `frame/plan.md` *Alternatives considered* row B.
- How a refresh reaches a release branch that takes no direct push: `frame/design.md` *Grounding* G3 and G4.
- Whether `STALE_SHARE` changes: `frame/plan.md` *Alternatives considered* row D.
- Whether the refresh is taken at every release or only past the share: `frame/plan.md` *Alternatives considered* row H.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the `durations` job on 0.36.0's release pull request ask the verdict and report both shares, red or green as the file stands? No probe can run it from here: the path runs only on a pull request into `main`, which no framer, crafter or proofer opens, and its condition is read, not run. | a measurement | Green with both shares in the summary: the condition and the script agree with the cases. Red with the sentence: the file is past the share, and the remedy is taken. No verdict asked: the condition is wrong, and a fix lands before the release merges. | The phase cases of scenarios S3 and S4 stand as the evidence, and the condition is the one `release-report` already runs on. | open |
| Q2 | Is the verdict a switch on the union step, with the upload's condition widened to a written union, or a separate last step of the `durations` job? | the work | A switch keeps one invocation and changes how the existing workflow case parses the step's words. A separate step leaves the union step as it is and adds a step that reads the union file. Either meets *Scope* item 3. | A switch, as `frame/design.md` *Data & interfaces* proposes; phase 2 records what it chose in its phase record. | answered: a switch on the union step, with the upload kept where the union was written (`trail/phases/phase-2.md`) |
