# Inspection: 1795860048-what-iadd-claims

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run stands at a commit that only the work item's records follow | `trail/gate.md:4` (`run: 7761e175 against 596c79a6`) | `git -C <root> merge-base --is-ancestor 7761e175 HEAD`; `git -C <root> log --ignore-submodules=none --no-merges --name-only 7761e175..HEAD ^596c79a6` | holds (executed): 7761e175 is an ancestor of HEAD 7067750f, and the one commit after it, 7067750f, touches only `agentory/threads/1795860048-what-iadd-claims/trail/gate.md`. The base `release/v0.41.1` resolves through `release/v0.41.1@{upstream}` to 596c79a6, the base the run names |
| The pull request body's part below `## From the records` is the records' text, and its part above is `pr.md` | the body file the prompt names | `agentic pr-body agentory/threads/1795860048-what-iadd-claims --body <file> --check` | holds (executed): exit 0, `matches` |
| S2: no passage of the cited documents is copied into the definition | `frame/design.md:27` | `uv run --no-project tests/run_tests.py -q tests/text/test_no_passage_is_pasted_into_a_second_file.py`, at HEAD and in the clone `<scratchpad>/1795860048-what-iadd-claims/at-base/` with a 22-word run of `docs/forms/the-inspection.md:38-39` pasted into the third sub-bullet | holds (executed): 5 passed at HEAD. With the pasted run it fails: `docs/forms/the-inspection.md and docs/method/iadd.md share 8 runs of 15 words; the longest is 22 words`, so the check can fail on this principle. The pasted line was restored after the run |
| The first wording of the third sub-bullet copied a 17-word run and the paste test refused it | `trail/phases/phase-1.md:5` | none: no commit holds the first wording | unverified, answerer the orchestrator. The row above shows the same test refusing a run of that section pasted into that sub-bullet, which is the mechanism the claim rests on |
| Phase 1 is verified by its named command | `frame/plan.md:19` | `uv run --no-project tests/run_tests.py -q tests/behaviour tests/text`, in the clone at 7067750f | holds (executed): 891 passed, 10 skipped |
| `## Removes`: nothing is removed, and the changelog names no removal | `frame/design.md` *Removes*, `changelog.md:3` | `git -C <root> diff 596c79a6...HEAD --stat` | holds (executed): 153 insertions, 0 deletions |
| Each sentence of the principle points to the file that holds its rule | `docs/method/iadd.md:32-48` | read of `skills/core/SKILL.md:12-15`, `skills/implement/routing-question.md:61,67`, `skills/implement/orchestration.md:526-528` (*Under agentic*), `docs/checks/the-routing-check.md:31-33,42-45`, `docs/forms/the-inspection.md` *The inspection* | holds (read). The opening sentence's *a cleared inspection says that the work went through it* rests on the core's opening paragraph, which bounds the process at the final inspector's verdict, and on the third sub-bullet's citation; no cited file contradicts it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | one principle at the head of `docs/method/iadd.md` *The principles*, every sentence pointing to an existing rule; no change to the cited files; nothing removed | the issue's *Done when*, the diff, the plan | none |
| the build | `docs/method/iadd.md:32-48` adds the principle with three sub-bullets, each with its citation; the diff touches no cited file (`git diff 596c79a6...HEAD --stat`) | the design, the issue, the cited files (rows above) | none |
| the last round | no round ran: `routing.md` reads `Review` `straight to the PR` | `routing.md` *Why this way*, whose grounds describe the diff: one bullet of a document that governs nothing itself, pointing to the files that hold each rule | none |
| the changelog | `changelog.md:3`: "The commit carries `IADD-Routing: no work item` and the pull request's check prints it." | the diff and the issue in every other sentence | the diff, the issue and the tree: the principle (`docs/method/iadd.md:43`) and the issue both say *where the root is shared*, and `docs/checks/the-routing-check.md:33` says that at a local root a commit carries none. The fragment states it of every commit, so the release note says something false for a local-mode repository |
| the orchestrator's part of the pull request body | `pr.md`: `Closes #1676` and two quotes of `frame/plan.md` *Judgments of the run* | `frame/plan.md:31`, word for word; no `pr.<lang>.md` is owed, both language keys read English | none |
| the routing record against the plan | `routing.md:24`: "#1648, the release's other work item, carries the version move" | `frame/plan.md:23` on #1648 carrying the version move | `frame/plan.md:23`, which names #1677 under *Overlap with the release* as a second item of the release; the branch `fix/1677-mutate-tests-without-a-shell` routes #1677 to the same release. The sentence also states a state outside this branch, which contract rule 19 holds: the text names each item by its role or names the command that reads the state |

```iadd
target: 7067750f8076be492b237e1b6daa86448f640cd1 against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: withheld reason: the changelog fragment (changelog.md:3, the orchestrator's) says every commit of the route carries `IADD-Routing: no work item`, where the principle (docs/method/iadd.md:43), the issue and docs/checks/the-routing-check.md:33 hold it only where the root is shared; and routing.md:24 (the orchestrator's) calls #1648 the release's other work item, where frame/plan.md:23 names #1677 as a second
```
