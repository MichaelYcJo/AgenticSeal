# Guarantee: 1793685432-a-shipped-rule-cites-this-repositorys-process

| Field | Value |
|---|---|
| Broad gate | e16d11007 against 62a15c50e |

The audit read the tree at 8d2e5d61a. The base is `release/v0.30.1`, and
both its upstream and `origin/release/v0.30.1` resolve to 62a15c50e, which
holds #1320. The local branch `release/v0.30.1` resolves to 0c68b9933 and is
not the base (`git rev-parse --verify --quiet`, executed). The last `seal`
block of `trail/gate.md` names `e16d11007 against 62a15c50e`, and e16d11007
is an ancestor of HEAD (`git merge-base --is-ancestor`, executed, exit 0).
`git log --no-merges --name-only e16d11007..HEAD ^62a15c50e` lists 8d2e5d61a
alone, which touches only `trail/gate.md` (executed). The repository tracks
no `seal/parity.md` (`git ls-files`, executed, no output), so this block owes
no `original:` line. `seal pr-body
seal/threads/1793685432-a-shipped-rule-cites-this-repositorys-process
--body <scratchpad>/1793685432-pr-body.md --check` exited 0 (executed). Every re-run
below took place in a `git clone --no-local` at 8d2e5d61a under
`<scratchpad>/1793685432/at-head/`, with a second clone under
`<scratchpad>/1793685432/at-base/` for the states before the change. Both
clones and their logs have been removed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| executed: the 40-module phase-boundary run failed only at `test_every_spec_directory_that_reached_the_ladder_has_an_overview`, because the work item had no `gaps.md` yet | `trail/phases/phase-1.md:13` | in the clone at 8b14bdbb7, the phase's commit before `gaps.md` existed: `bin/test -q -p no:xdist "tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview"` | holds (executed): exit 1, 1 failed, `AssertionError: work items with no closing overview: ['1793685432-a-shipped-rule-cites-this-repositorys-process']`. The run's other count, 1105 passed and 11 skipped over 40 modules, was not re-run |
| executed: after the memo and the records, one run over that module and seven others exited 0 with 177 passed | `trail/phases/phase-1.md:13` | `bin/test -q` over the eight modules the record names, at HEAD | holds (executed): exit 0, 177 passed |
| A2, A3 and A5, and every module that reads an edited path, pass at HEAD | `frame/plan.md` *Phases*, row 1; `trail/phases/phase-1.md:13`; `trail/rounds/round-2.md` *Probes* | `bin/test -q` over 47 modules: every `tests/*.py` that `git grep -l -F` lists for one of the six edited paths, the seven `frame/plan.md` row 1 names, and the eight above | holds (executed): exit 0, 1171 passed and 11 skipped. The crafter's fix-pass run of 21 modules, 594 passed, was not re-run |
| A3 can fail: the move leaves no 15-word run in two files | `frame/design.md` A3; `trail/phases/phase-1.md:9` | in the at-base clone at 8d2e5d61a, `git checkout 0c68b9933 -- docs/releasing/issues-and-milestones.md`, then `bin/test -q -p no:xdist tests/text/test_no_passage_is_pasted_into_a_second_file.py` | holds (executed): exit 1, the module names `docs/releasing/issues-and-milestones.md` and `skills/implement/orchestration.md` sharing 39 runs of 15 words. Restored to HEAD after the run |
| A2 can fail: each new citation resolves | `frame/design.md` A2 | in the at-base clone, `## When it runs` in `skills/settle/SKILL.md` renamed by one substitution asserted to match once, then `bin/test -q -p no:xdist tests/behaviour/test_a_cited_section_stands_in_its_file.py` | holds (executed): exit 1, naming `docs/releasing/release-checklist.md:33` citing `skills/settle/SKILL.md` *When it runs*. Restored to HEAD after the run |
| A1: only the two kept citations name a process document in a shipped tree | `frame/design.md` A1; `trail/phases/phase-1.md:17` | `git grep -n -i -E 'release.checklist\|issues.and.milestones\|branch.and.release\|docs/releasing' -- skills agents templates hooks bin` | holds (executed): `skills/verify/orchestration.md:233` and `skills/verify/scripts/unverified_check.py:112`, nothing else |
| A6: no `check: none reader:` line is added | `frame/design.md` A6; `trail/phases/phase-1.md:17` | `git diff 0c68b9933 -- skills docs \| grep -c '^+check: none reader'`, and the same against 62a15c50e | holds (executed): 0 and 0 |
| the census of removed spellings is empty outside `seal/threads/` | `trail/phases/phase-1.md:7` | `git grep -n -F` on "names its branch's commits on its", "runs when the owner calls it", "A decision is folded into the body in place", "the framer at every frame", "for the settle the owner calls", "re-reads the column" and "rebases the branch", outside `seal/threads/` | holds (executed): every search lists nothing |
| `## Removes`, every row: nothing of each removal stands in the tree | `frame/design.md` *Removes*, seven rows | the census above for rows 1, 3, 6 and 7; `git grep -n -B1 -A1 -E` on "Before starting", "An issue is its body", "its comments together", "Settle what earlier" and `\*2b` outside `seal/threads/`, `CHANGELOG.md` and `.test_durations`, for the citation rows 2, 4 and 5; and `git diff 62a15c50e...HEAD -- skills docs`, read | holds (executed): the citations that remain are `docs/releasing/issues-and-milestones.md:213` (the milestone box of *0. Before starting*), `docs/layout/the-record-layout.md:124` (*2b* for the settle's removal of a directory) and a test reading *0. Before starting* for `.test_durations`. None stands on a moved rule (read). The diff removes each row's text and cites the home it names |
| the removals the changelog names: the checklist citation in the code-review section, the re-read instruction in the implement skill, the issue document's fold paragraph, and the first paragraph of *2b* | `changelog.md:3` | `git diff 62a15c50e...HEAD -- skills docs`, read against each clause | holds (read): each clause matches a hunk, and the diff changes no script, hook or check (`git diff --stat`, executed: only the six prose files and the work item's records) |
| the merge of the base at 5e9ab6658 resolved no conflict | `frame/questions.md` Q1; pull request body, the merge item | `git merge-tree --write-tree 31c4c6f09 62a15c50e`, compared with `git rev-parse 5e9ab6658^{tree}` | holds (executed): exit 0, and both print tree 46794b5c1, so the merge commit is the clean merge |
| no `.github/` line follows a moved rule; 25 lines in 11 files | `frame/design.md` *Grounding*, the `.github/` row; pull request body | `git grep -n -A2 -E 'release-checklist\|issues-and-milestones\|branch-and-release' -- .github/`, counted with `wc -l` and `git grep -l`, and the italic sections it names tallied | holds (executed): 25 lines, 11 files. The sections cited are *5. The release pull request*, *6. After the merge*, *A keyword claims the one number after it*, *A label answers what it is about, and survives the move*, *Work accumulates on a release branch*, and step 2b at `.github/scripts/finding_counts.py:2` for its four numbers, which stay in *2b*. None cites the never-rebase box, the first paragraph of *2b* or *An issue is its body and its comments together* |
| the commits no crafter made touch only the work item's records | pull request body, the last item | `git show --name-only` of 6994533c0, 4e2c0b77d, ac205c11b, 10e3ba4e4, 9b0d988cd, 9fd639b5f, 31c4c6f09, e16d11007 and 8d2e5d61a, filtered for paths outside the work item's directory | holds (executed): none lists a path outside it. Which party made each commit is read from the subjects, not established |
| `.claude-plugin/plugin.json` reads 0.30.1, moved by #1320 | pull request body, the prefix item | `git show <rev>:.claude-plugin/plugin.json` at 0c68b9933 and 62a15c50e, and `git log 0c68b9933..62a15c50e -- .claude-plugin/plugin.json` | holds (executed): 0.30.0 at 0c68b9933, 0.30.1 at 62a15c50e, and 62a15c50e (#1320) is the one commit in the range that touches it |
| the broad run passed with 6360 passed and 12 skipped, chain exit 0 | pull request body, the broad run item | none: the sealer runs nothing broad | unverified: `trail/gate.md` holds only the `run:` line, read at step 1. The counts are the orchestrator's, who ran `seal gate --record` |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Three rules move out of the process documents into the skills that apply them: the never-rebase rule widened to every rebase in `skills/code-review/orchestration.md`, the fold rule in `skills/implement/orchestration.md`, the settle's timing in `skills/settle/SKILL.md`. `skills/implement/SKILL.md` *3. The SDD file set* is brought in line. The process documents keep the person's act and cite the skills, the `.github/` lines and the two `skills/verify/` citations stay, `docs/` is edited directly with a no-change `## Rule changes`, and `## Removes` names seven removals | the issue body's *Scope* and *Done when*, and its second comment on the policy-root boundary, which supersedes the body's *Rule change* paragraph; the diff, hunk for hunk; the A1 and A6 runs; the `.github/` census | none |
| the build | `trail/phases/phase-1.md`: the frame built as drawn, a move owing no new case, the fold sentences moved word for word, four lines re-wrapped, the narrow runs and A1 and A6. Commits 8b14bdbb7 and 620c24798 change only the six prose files and the records | the diff; the re-runs above; round 1's finding 2, whose snippets stand at `trail/phases/phase-1.md:9` and `:11`. Its "five edited paths" is the phase's own run, before 620c24798 added the sixth | none |
| the last round | `trail/rounds/round-2.md` confirms round 1's two closes, and its finding 1 reads `fixed 7867f45cf`: the frame and the memo named five files and six removals. The finding sits in `seal/threads/<item>/` alone, and 7867f45cf and 9fd639b5f touch nothing outside it (executed above), so the sealer reads it | the records at HEAD do what it asked: `frame/design.md` *Data & interfaces* names six files with `skills/implement/SKILL.md`, `## Removes` holds the seventh row word for word, `frame/plan.md` *Technical context* says six files and lists `skills/implement/SKILL.md:303-307`, and `gaps.md` reads "six edited paths" (read). The *Phases* cell keeps "six rows", as the round asked and `frame/plan.md` *Judgments of the run*, second row, records | none |
| the changelog | `changelog.md`: the three skills state the rules they cited, the implement skill no longer tells a party how to recover from a rebase, the checklist and the issue document cite the skills, no script, hook or check changes; two process-change rows | the diff, clause for clause; the design's *Scope* items 1 and 2; round 1's finding 1 | none |
| the orchestrator's part of the pull request body | `Closes #1234`; the prefix and the version; the owner's decisions; the `.github/` count; the two rounds and their closes; the clean merge of the base; the broad run; the commits no crafter made | the issue's title prefix and its second comment; `routing.md`; the round records; the merge-tree comparison; `trail/gate.md`; the path census of those commits; each quoted sentence stands in the record it names (read) | none. The broad run's counts are its own claim, labelled above |

```seal
target: 8d2e5d61a against 62a15c50e
Verdict: sealed
```
