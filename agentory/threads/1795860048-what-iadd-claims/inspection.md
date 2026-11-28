# Inspection: 1795860048-what-iadd-claims

## Claims re-run

This run audits d0c58a80. The commits since the newest earlier block's target, f786ba7e, are cbc99ac1 (`inspection.md`) and d0c58a80 (`frame/design.md`), so the rows whose coordinates they touched are re-run, and the rest stand as the earlier runs left them, at a tree whose `docs/`, `skills/` and `tests/` no commit since 7067750f touched (`git -C <root> log --name-only 7067750f..HEAD`). Each row's result names the run that executed or read it.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run stands at a commit that only the work item's records follow | `trail/gate.md:4` (`run: 7761e175 against 596c79a6`) | `git -C <root> log --ignore-submodules=none --no-merges --name-only 7761e175..HEAD ^596c79a6` | holds (executed, this run): the commits after 7761e175, 7067750f, bd0f7d57, f786ba7e, cbc99ac1 and d0c58a80, touch only paths under `agentory/threads/1795860048-what-iadd-claims/`. The base `release/v0.41.1` resolves through `release/v0.41.1@{upstream}` to 596c79a6 |
| The pull request body's part below `## From the records` is the records' text, and its part above is `pr.md` | the body file the prompt names, rewritten after d0c58a80 | `agentic pr-body agentory/threads/1795860048-what-iadd-claims --body <file> --check` | holds (executed, this run): exit 0, `matches` |
| The changelog bounds the trailer to a shared root | `changelog.md:3` | read against `docs/method/iadd.md:43` and `docs/checks/the-routing-check.md:31-33` | holds (read, run at f786ba7e; untouched since) |
| The routing grounds name the release's items by role | `routing.md:24` | read against `frame/plan.md:23`, and `git -C <root> diff --stat 596c79a6...origin/fix/1648-submodule-pointer-in-typed-diffs` for the version file | holds (read and executed, run at f786ba7e; untouched since): the sentence no longer counts the release's items, and #1648's branch changes `.claude-plugin/plugin.json`, as the sentence and `frame/plan.md:23` say |
| The design's *Grounding* row bounds the trailer to a shared root | `frame/design.md:12` | read against `docs/checks/the-routing-check.md:31-33` | holds (read, this run) |
| Every other statement in the records of the route's trailer and of `direct` | `agentory/threads/1795860048-what-iadd-claims/` | `git -C <root> grep -n -i -e 'no work item' -e 'IADD-Routing' -e 'trailer' -e 'local root' -e 'other work item' -- agentory/threads/1795860048-what-iadd-claims ':!agentory/threads/1795860048-what-iadd-claims/inspection.md'`, and `git -C <root> grep -n -w -e direct` over the same paths, a sample under rule 12 | holds (executed, this run): the first prints `changelog.md:3` and `frame/design.md:12`, both bounded; the second prints `frame/design.md:10-11`, which hold against `skills/implement/routing-question.md:67` and `skills/implement/orchestration.md:526-528` (read) |
| S2: no passage of the cited documents is copied into the definition | `frame/design.md:27` | earlier run: the paste test at 7067750f, and in the clone `<scratchpad>/1795860048-what-iadd-claims/at-base/` with a 22-word run of `docs/forms/the-inspection.md:38-39` pasted in | holds (executed, earlier run; no file it reads changed since): 5 passed, and the pasted run failed it |
| The first wording of the third sub-bullet copied a 17-word run and the paste test refused it | `trail/phases/phase-1.md:5` | none: no commit holds the first wording | unverified, and no party can answer it: the wording was never committed. The S2 row shows the same test refusing a run of that section pasted into that sub-bullet |
| Phase 1 is verified by its named command | `frame/plan.md:19` | earlier run: `uv run --no-project tests/run_tests.py -q tests/behaviour tests/text`, in the clone at 7067750f | holds (executed, earlier run; no file it reads changed since): 891 passed, 10 skipped |
| `## Removes`: nothing is removed, and the changelog names no removal | `frame/design.md` *Removes*, `changelog.md:3` | `git -C <root> diff 596c79a6...HEAD --stat` | holds (executed, this run): 192 insertions, 0 deletions |
| Each sentence of the principle points to the file that holds its rule | `docs/method/iadd.md:32-48` | earlier run: read of `skills/core/SKILL.md:12-15`, `skills/implement/routing-question.md:61,67`, `skills/implement/orchestration.md:526-528`, `docs/checks/the-routing-check.md:31-45`, `docs/forms/the-inspection.md` *The inspection* | holds (read, earlier run; none of those files changed since) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | one principle at the head of `docs/method/iadd.md` *The principles*, every sentence pointing to an existing rule; no change to the cited files; nothing removed | the issue's *Done when*, the diff, the plan, and in its *Grounding* rows the cited clauses, `frame/design.md:12` now bounded to a shared root | none |
| the build | `docs/method/iadd.md:32-48` adds the principle with three sub-bullets, each with its citation; the diff touches no cited file | the design's scope, the issue, the cited files | none |
| the last round | no round ran: `routing.md` reads `Review` `straight to the PR` | `routing.md` *Why this way*, whose grounds describe the diff | none |
| the changelog | `changelog.md:3`: the principle, with the trailer bounded to a shared root | the diff, the issue, `docs/checks/the-routing-check.md:33` | none |
| the orchestrator's part of the pull request body | `pr.md`: `Closes #1676` and two quotes of `frame/plan.md` *Judgments of the run* | `frame/plan.md:31`, word for word; no `pr.<lang>.md` is owed, both language keys read English | none |
| the routing record against the plan | `routing.md:24`: the version-move item merges first, and `frame/plan.md` *Overlap with the release* names the rest | `frame/plan.md:23` | none |

```iadd
target: 7067750f8076be492b237e1b6daa86448f640cd1 against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: withheld reason: the changelog fragment (changelog.md:3, the orchestrator's) says every commit of the route carries `IADD-Routing: no work item`, where the principle (docs/method/iadd.md:43), the issue and docs/checks/the-routing-check.md:33 hold it only where the root is shared; and routing.md:24 (the orchestrator's) calls #1648 the release's other work item, where frame/plan.md:23 names #1677 as a second
```

```iadd
target: f786ba7e6564be6326a9f77695025fcbef9042aa against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: withheld reason: the design's Grounding row (frame/design.md:12, the session's frame) says a commit of no work item carries `IADD-Routing: no work item`, where docs/checks/the-routing-check.md:33 holds it only where the root is shared, the class of the changelog sentence the earlier block withheld on; changelog.md:3 and routing.md:24 now hold
```

```iadd
target: d0c58a80d2c33006cc1045064c97245194995467 against 596c79a6fd4a36fa55ea7fe383d12c8b97119e40
Verdict: cleared
```
