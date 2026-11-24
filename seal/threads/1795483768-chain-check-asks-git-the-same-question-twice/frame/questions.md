# Questions for the planner: 1795483768-chain-check-asks-git-the-same-question-twice (#1603)

The ticket and the spawn left these open, and the tree answered each. They are not reopened here:

- Which reads cannot change within one run, the working-tree reads under `--worktree` among them: `frame/design.md` *Grounding*, *Which reads cannot change within one run*.
- Whether `settle` repeats a read within one run: `frame/design.md` *Grounding*, *`settle` repeats reads within one run*, and *`settle`'s only git read after a write asks where the common git directory is*.
- Where the memo lives, and whether `lib/gitcmd.py` widens the change past the issue: `frame/design.md` *Grounding*, *Where a per-run memo has to live*, and `frame/plan.md` *Alternatives considered* A1 and A2.
- Whether batching is worth its code against memoizing alone: `frame/plan.md` *Alternatives considered* A5 to A9.
- How the cases that count or order git calls are treated: `frame/design.md` *Grounding*, *The cases that count or order the git calls*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | After phase 2, is a further phase worth reading the judged work item's records through one batch per work item (`frame/plan.md` *Alternatives considered* A7)? The framer cannot answer it. It turns on what one git process costs on the Windows runner and on what phases 1 and 2 saved there, which only `workflow_dispatch` runs of the pushed branch show, and no subagent pushes or dispatches. | a measurement | A further phase saves about one process per record file of each judged work item, as many as A7 counts for #1581's real run, and adds a second store beside the run memo. No further phase leaves those reads one process each per run, as phase 1 makes them. | No further phase. The orchestrator reads S8's run after phase 2 and records its judgment in `frame/plan.md` *Judgments of the run*. | answered 2026-11-24: no further phase, by `frame/plan.md` *Judgments of the run* |
