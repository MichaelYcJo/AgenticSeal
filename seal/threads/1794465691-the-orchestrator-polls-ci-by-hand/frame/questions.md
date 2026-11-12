# Questions for the planner: 1794465691-the-orchestrator-polls-ci-by-hand

Judgments the ticket left open that the tree answered:

- What `seal pr-wait` reads: `frame/design.md` *Data & interfaces*, and `plan.md` *Alternatives considered*, rows 1 to 4.
- The exit code for each outcome: `frame/design.md` *Data & interfaces*, the table of exit codes, against *Grounding* G3.
- How the cases hold `gh`'s behaviour without a network: `frame/design.md` *Scope* item 2, and *Grounding* G14.
- Whether a cancelled check is a pass: `frame/design.md` *Grounding* G7, and scenario S7.
- Whether a check read with nothing pending is final: `frame/design.md` *Grounding* G10, and scenario S6.
- Whether the read before a push stays, and in what form: `plan.md` *Alternatives considered*, row 6.
- Whether the command stops at the first failed check: `plan.md` *Alternatives considered*, row 5.
- Whether the whole wait has a limit: `plan.md` *Alternatives considered*, row 8.
- Whether the orchestrator waits on CI at all: settled by #1222, `frame/design.md` *Grounding* G6.

No row needs a person. Both rows below are measurements that no read-only probe from a frame can take.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | On this work's own pull request, the first real run of `seal pr-wait <N>`: does it exit 0 only once every job of the `pull_request` runs has finished, `durations` and `release-report` among them where #1516's matrix still runs them, and how many seconds pass between the push and the first `pull_request` check listed on it? A frame pushes nothing and opens no pull request, so no probe here can watch a push reach its checks. The orchestrator takes the reading when it opens the pull request and after each push to it. | a measurement | If the command exits before a listed job has finished, the runs read of `frame/design.md` *Data & interfaces* misses a case and the work reopens. If the first check takes longer than two minutes to appear, the limit is too short and changes in `pr_wait.py` and the paragraph. If both hold, nothing changes. | The build proceeds on the ten-second interval and the two-minute limit. | open |
| Q2 | On GitHub Enterprise Server, where gh may not ask for a check's event, does `gh pr checks --json event` print an empty event for every check, so that `seal pr-wait` never starts and ends at exit 3? gh asks for the field only where the server reports the feature (`checks.go`'s `PullRequestFeatures`, design G7), and no Enterprise Server is reachable from this environment. Whoever runs the plugin against one can answer by running the command on a pull request there. | a measurement | If the event is empty there, exit 3 names the commit and says no `pull_request` check reported, which is visible and not a pass; a later change could count every check there. If the event is present, nothing changes. | Exit 3, as *Data & interfaces* states. | open |
