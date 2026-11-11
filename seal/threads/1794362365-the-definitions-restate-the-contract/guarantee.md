# Guarantee: 1794362365-the-definitions-restate-the-contract

Audited on 2026-11-11 by the sealer, at `0e7a23c4d` against the base
`release/v0.37.3`. Its upstream resolved to `9c6907942` (`executed`:
`git rev-parse --verify --quiet 'release/v0.37.3@{upstream}'`), and
`origin/release/v0.37.3` and the local branch print the same commit.

The gate record `trail/gate.md` names `run: 29c41293c against 9c6907942`.
`29c41293c` is an ancestor of HEAD. The one commit after it, `0e7a23c4d`,
touches only this work item's `trail/gate.md` (`executed`:
`git merge-base --is-ancestor 29c41293c HEAD` and
`git log --no-merges --name-only 29c41293c..HEAD ^9c6907942`). The broad
gate's pass is the orchestrator's account. The sealer read the record and
ran nothing broad (`read`, contract rule 2).

`seal pr-body <item> --body <file> --check` exited 0 with both the
installed plugin's `seal` and the tree's `bin/seal` (`executed`). Both
language keys of `seal/config.json` name English, so no `pr.<lang>.md` is
owed. The repository declares no `seal/parity.json`, and `routing.md`
answers `open the pull request`, so no comparison with an original is owed.

The issues were read with `gh issue view 1474` and `gh issue view 1503`,
each with `--json title,body` and with `--comments` (`executed`). #1474 has
no comment. #1503 has one comment by the repository's owner account, dated
2026-11-11, which amends the issue for the orchestrator. The sealer reads
that comment as the owner's decision.

## Claims re-run

Every run used a `git clone --no-local` at `0e7a23c4d` under
`<scratchpad>/1794362365-the-definitions-restate-the-contract/sealer/at-base/`.
For the base runs, `README.md`, `README.ko.md`, `agents/` and `skills/` were
restored there from `9c6907942` with HEAD's tests kept. For the guard runs,
HEAD's code was restored first and `bin/seal mutate` removed one guard at a
time, run as a single mutant so that the failing line printed.
`git status --short` in the clone was empty after the guard runs. The tree
under audit was not changed. The sample takes every `seen red` claim on
which #1503's *Done when* rests, and the measurements #1474's *Done when*
rests on.

| Claim | Source | Command | Result |
|---|---|---|---|
| The new rule 17 case is red against the old contract | `trail/phases/phase-1.md`, the shown-red table, row 1 | base code restored; `bin/test tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/behaviour/test_a_probe_that_commits_says_so.py -q -p no:xdist -p no:randomly` | Holds. `test_rule_17_names_the_scratch_directory_for_the_work_item` fails at `:141`, "contract rule 17 does not name the scratch directory as `<scratchpad>/<work-item-id>/<leaf>/`" (`executed`) |
| The `rm -rf` absence case is red against rule 21 as it stood at `9c6907942` | `trail/phases/phase-1.md`, the shown-red table, row 4 | the same run | Holds. `test_no_contract_section_or_definition_writes_a_removal` fails at `:166` on `skills/agent-contract/SKILL.md`, quoting rule 21's old removal sentence (`executed`) |
| The orchestrator's removal case is red where the sentence is absent | `trail/rounds/round-2.md` finding 1, its verdict answer | the same run | Holds. `test_the_orchestrators_one_removal_names_the_work_items_directory` fails at `:180` on its directory clause (`executed`) |
| The tracer's case is red against the old tracer sentence | `trail/rounds/round-1.md` finding 1, its verdict answer | the same run | Holds. `test_the_fact_finder_points_a_probe_at_rule_7` fails at `:78` (`executed`). The run printed 4 failed, 8 passed |
| Rule 17's "share one scratchpad" clause pins its sentence | `trail/phases/phase-1.md`, the shown-red table, row 2 | `bin/seal mutate skills/agent-contract/SKILL.md --replace "Agents of one session share one scratchpad, … apart from yours. " ""`, the scratch module | Holds. `red`. The failing line is "contract rule 17 names the directory and not why: agents of one session share one scratchpad" (`executed`) |
| Rule 17's "add `-2` to the leaf" clause pins its sentence | `trail/phases/phase-1.md`, the shown-red table, row 3 | `bin/seal mutate` removing "Where the directory already stands … or the next number free. " | Holds. `red`. The failing line is "contract rule 17 does not say what an agent does where its directory already stands" (`executed`) |
| The proofer's directory clause, now read inside backticks, pins T11's directory sentence alone | `trail/phases/phase-1.md`, *Departure 2*, and the shown-red table, row 7 | `bin/seal mutate agents/proofer.md` removing "Your scratch directory (rule 17) is `<scratchpad>/<work-item-id>/round-<n>/`, and where" (the clone sentence kept) | Holds. `red`. The failing line is "the section does not name the round's scratch directory as `<scratchpad>/<work-item-id>/round-<n>/`". The clone's path, which stays, did not hold it green (`executed`) |
| The orchestrator's case pins the work item's directory | `trail/rounds/round-2.md` finding 1, its verdict answer | `bin/seal mutate skills/implement/orchestration.md` removing "`<scratchpad>/<work-item-id>/`, " | Holds. `red`. The failing line is "the orchestrator's removal does not name the work item's directory as `<scratchpad>/<work-item-id>/`" (`executed`) |
| The orchestrator's case pins "removes nothing else of the scratchpad" | the same verdict answer | `bin/seal mutate` removing ", and removes nothing else of the scratchpad" | Holds. `red`. The failing line is "the orchestrator's removal does not say it removes nothing else of the scratchpad" (`executed`) |
| S1: the four definitions shrink from 48,810 B to 46,860 B, under the bound of 47,310 B | `trail/phases/phase-1.md` S1; `changelog.md:5` | `git show <c>:<f> \| wc -c` at `9c6907942` and HEAD | Holds. Crafter 11,411 B to 10,215 B, framer 14,946 B to 14,824 B, proofer 10,999 B to 10,763 B, sealer 11,454 B to 11,058 B (`executed`) |
| S9: the contract grows from 12,364 B to 12,806 B, under 12,864 B; the tracer holds 2,918 B | `changelog.md:5`; `frame/design.md` G17 | the same | Holds. The core is 9,322 B at both commits (`executed`) |
| S2: the ten-word census reads 916 of 11,778 at the base and 865 of 11,561 after | `changelog.md:5`; `frame/design.md` G18 | `python3 -I round-1/test_tmp_census.py <clone> 9c6907942 0e7a23c4d`, round 1's probe, read before it ran | Holds in every cell. At HEAD: crafter 254 of 1,592, framer 140 of 2,369, proofer 141 of 1,695, sealer 81 of 1,727, tracer 26 of 445, contract 90 of 2,138, core 133 of 1,595 (`executed`) |
| S3: no definition spells out the labels any more | `trail/phases/phase-1.md` S3 | `git grep -n 'read. or .unverified' -- agents` | Holds. No output, exit 1 (`executed`) |
| S4: rule 17 alone states the shared-scratchpad reason | `trail/phases/phase-1.md` S4 | `git grep -n -i 'share one scratchpad' -- agents skills` | Holds. `skills/agent-contract/SKILL.md:189` alone (`executed`) |
| S10: the narrow cases that read the edited files pass | `trail/phases/phase-1.md`, the phase-boundary set; `frame/design.md` S10 | `bin/test` over the 15 modules S10 and G13 name, `-q`, at HEAD in the clone | Holds. 478 passed, exit 0 (`executed`) |
| S11: the diff outside `seal/` holds the files *Scope* names and no other | `trail/phases/phase-1.md` S11 | `git diff --stat 9c6907942...HEAD -- ':!seal/'` | Holds. 12 files: the ten S11 lists, plus `agents/tracer.md` and `tests/behaviour/test_a_probe_that_commits_says_so.py`, which *Scope* item 17 names (`executed`) |
| #1503 *Done when* 1: no text under `agents/` or `skills/` tells an agent to remove its scratch | `trail/phases/phase-1.md` S5 | `git grep -n -i scratch -- agents skills ':!*.py'` filtered for removal words; `git grep -n -E '\brm\b'` and `git grep -n -i -E 'gone before\|is gone\|clean ?up'` over the same paths, each hit read | Holds for agents. The orchestrator's removal is the only hit that orders one, at `skills/implement/orchestration.md:46-53`. *The parties* reads that sentence against the issue (`executed`, `read`) |
| #1503 *Done when* 2: the naming sentences of #544, #1047 and #1445 stand and their case is green | `frame/design.md` S6 | the S10 run | Holds (`executed`) |
| Every `## Removes` row is gone from the tree | `frame/design.md` *Removes* | `git grep -n -F` on each removed sentence's words, 25 phrases, `seal/threads/` excluded | Holds. The only hit is `.test_durations:5786`, which names the removed case. `trail/phases/phase-1.md` names that hit and cites `CONTRIBUTING.md` *Running the checks*, which leaves the file to the release (`executed`, `read`) |
| The facts the removed crafter and sealer sentences held stand where *Removes* says | `frame/design.md` *Removes*, the rows on `agents/crafter.md:50-51`, `:111-113`, `:172-176` and `agents/sealer.md:149-152` | read with whitespace collapsed | Holds. The mutation rule keeps "A unit only renamed or moved adds nothing to break, and owes no run". Step 4 keeps the stop for a missing frame. `skills/implement/SKILL.md:290` and `:315` keep "every departure from the frame". The sealer's Job keeps "never the summary in the prompt that spawned you" (`read`) |
| Each `## Rule changes` `from:` stands in its policy document | `frame/design.md` *Rule changes* | a whitespace-collapsed substring test on `docs/running/the-agent-set.md` and `docs/forms/the-round-record.md` | Holds for both (`executed`) |
| Each quote of `pr.md` stands word for word in `frame/plan.md` | `pr.md:1-8` | a whitespace-collapsed substring test of each quote | Holds, all eight (`executed`) |
| The chain check passes on the records | `trail/rounds/round-3.md` finding 2 (the repeated-passage warning) | `python3 skills/code-review/scripts/chain_check.py --baseline 9c6907942 --root <repo> --worktree` | Holds. Exit 0. The only line is that git carries no guarantee file yet, and the repeated-passage warning round 3 quoted is gone (`executed`) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Rule 17 states the scratch rule once, and no agent removes scratch. The definitions cite rules 2 to 5. The orchestrator removes `<scratchpad>/<work-item-id>/` once the pull request is open "and again after each repair it pushes to the open pull request" (`frame/design.md` *Scope* item 8, T22 at `:198`, T24 at `:212`) | the build, the changelog, the issues' other *Done when* clauses, every claim re-run above | #1503 as the owner amended it, on the repeat. The owner wrote that the orchestrator removes the directory "once, after the pull request opens", and that "For the orchestrator, the one removal above is the exception" to *Done when* clause 1. T22's second sentence orders a removal beyond that one |
| the build | The diff, and `trail/phases/phase-1.md` at its own commits, `18f699ddd` and `39efee911`. Fix pass 1 (`979c60b7d`) and fix pass 2 (`3024a14d3`) are recorded in the rounds' verdict answers. `skills/implement/orchestration.md:50-53`, `README.md:378-380` and `README.ko.md:375-377` state the repeat | the design, as T1 to T25 stand folded. `routing.md` declares `crafter`, and phase 1, the plan's one phase with a commit in its Status cell, has its record | #1503 as amended, on the same sentences as the design |
| the last round (round 3, with its two `fixed 6b27a65dc` findings read at HEAD in place of a verifying round) | Finding 1 asked that the plan row's grounds say the repeat is the orchestrator's judgment and not the owner's words. Finding 2 asked that the `to:` of the `docs/running/the-agent-set.md` rule change drop its copy of the README sentence. Its *Not judged* leaves to the owner whether #1503 confirms the repeat | `6b27a65dc` touches only `frame/plan.md` and `frame/design.md` of this work item. At HEAD, `frame/plan.md:80` carries the grounds finding 1 gave, word for word. `frame/design.md` *Rule changes* carries finding 2's sentence without the word "one", and the round 3 row of *Judgments of the run* records that change. The chain check no longer prints the repeat (`read`, `executed`) | none |
| the changelog | `changelog.md:3` and `:11` state the scratch rule, the figures and the repeat after each repair. `:11` gives the owner one removal and the repeat as the reason a repair clones again | the tree's figures and texts | #1503 as amended, on the repeat. `:11` does not attribute the repeat to the owner, and the issue does not grant it |
| the orchestrator's part of the pull request body | `pr.md`: eight quotes of `frame/plan.md`, quote 6 being the repeat row. `Closes #1474.` and `Closes #1503.` | every quote stands at its coordinate. The repeat row says "The repeat is the orchestrator's judgment, not the owner's words" | #1503 as amended, on the repeat it quotes. `gaps.md` *Not verified*, which the body copies, keeps the broad-gate row open. The row is true as written, and `trail/gate.md` now answers it; the orchestrator may mark the row closed |

The disagreement is narrow. Every party describes the same tree, and every
claim re-run holds. What none of them can settle is whether the owner's
amendment covers the repeat. The owner wrote "once" and "the one removal",
and gave as the reason that nothing clears a session's scratch. That reason
also covers the clones a repair makes after the pull request opens, which
the amendment did not consider. The orchestrator judged the reason to
govern and recorded the judgment as its own (`frame/plan.md:80`). The words
of #1503 do not grant it, and the tree cannot decide it. Only the owner
can.

```seal
target: 0e7a23c4d against 9c6907942
Verdict: undecided question: Does the owner's amendment of #1503, which has the orchestrator remove the work item's scratch directory "once, after the pull request opens" and calls "the one removal above" the only exception to Done when clause 1, also allow the orchestrator to run the same removal again after each repair it pushes to the open pull request, as skills/implement/orchestration.md step 2 (lines 50-53), README.md, README.ko.md and changelog.md now state on the orchestrator's judgment (frame/plan.md Judgments of the run, the row of the repeat removal)? If yes, an Answered line below this block is the owner's grant, and a re-run seals; if no, the repeat goes from those texts, the frame and the scratch module's docstrings, and a round reads that change.
```

Answered 2026-11-11 by the owner: yes. The orchestrator runs the same removal again, with the same literal path, after each repair it pushes to the open pull request, a merge from the base among them; a repair's round and audit clone again, and the removal clears those clones with no prompt. The owner chose this in this session and it is added to #1503's comment thread.

## Re-audit at `fb0cbf824`

Audited again on 2026-11-11 by the sealer, at `fb0cbf824` against the same
base, `9c6907942`. The one commit after the block above, `fb0cbf824`, adds
this file and nothing else (`executed`:
`git log --no-merges --name-only 0e7a23c4d..HEAD` and
`git diff --stat 0e7a23c4d HEAD` with this file excluded, which prints
nothing). So no claim's coordinate changed, and no claim of *Claims re-run*
needed a second run.

- **The gate record still covers HEAD.** `29c41293c` is an ancestor of
  HEAD, and only `trail/gate.md` and this file follow it, both under this
  work item's directory (`executed`).
- **The body check still passes.** `seal pr-body <item> --body <file>
  --check` exited 0 with the installed `seal` and with `bin/seal`
  (`executed`).
- **The owner answered the question.** The `Answered 2026-11-11 by the
  owner:` line above says yes. #1503's second comment, by the owner
  account, adds the repeat to the amendment: "The orchestrator runs the
  same removal again, with the same literal path, after each repair it
  pushes to the open pull request. A merge from the base counts as a
  repair." It also states "The repeat is the only change to the amendment
  above" (`executed`: `gh issue view 1503 --comments`).

The parties were read again against #1503 as the owner now amends it.

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as in the block above, with T22's repeat | #1503's second comment, the build, the changelog | none |
| the build | `skills/implement/orchestration.md:46-53`, `README.md:378-380` and `README.ko.md:375-377` state one removal after the pull request opens and the same command after each repair | #1503's second comment, which names the same literal path and counts a merge from the base as a repair | none |
| the last round (round 3, with its two `fixed 6b27a65dc` findings) | its *Not judged* left the owner's confirmation open | the owner has now answered it | none |
| the changelog | `changelog.md:3` and `:11` state the repeat after each repair | #1503's second comment | none |
| the orchestrator's part of the pull request body | `pr.md` quote 6 quotes the repeat row, which calls the repeat the orchestrator's judgment | the row is still true as a record of who judged first, and the owner has now granted the repeat | none |

`gaps.md`'s broad-gate row is the crafter's account of what it did not
run, and `trail/gate.md` answers it. The orchestrator keeps the row as it
stands.

```seal
target: fb0cbf824 against 9c6907942
Verdict: sealed
```
