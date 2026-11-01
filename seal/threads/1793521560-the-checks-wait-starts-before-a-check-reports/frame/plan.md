# Implementation Plan: 1793521560-the-checks-wait-starts-before-a-check-reports

## Technical context

The work rewrites one sentence of `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, lines 226-229. That sentence ends the paragraph on reading `gh pr view <N> --json state,mergeable` (lines 213-229). The new paragraph follows that one and keeps its order: under `OPEN` and `MERGEABLE` the orchestrator polls, and then it waits. The paragraph after it, on a conflict with the base (line 231), does not change.

Constraints on the text:

- The file is held to 88 display columns by `tests/behaviour/test_docs_line_wrap.py` (`COVERED`, line 110 on), and fenced code is skipped. The poll's command goes in a fenced block, the file's first.
- `tests/text/test_the_rules_have_one_owner.py:363` pins `` `gh pr checks <N> --watch` `` in the section, so the command keeps that spelling.
- The section is read in every user's repository. The paragraph states gh's behaviour and the limit, and it states no figure measured on this repository. The measurement stays in `frame/design.md` *Grounding*.

The failure scenario of the chosen approach, six months on:

- A gh release renames `headRefOid` or `statusCheckRollup`. The poll's command then exits non-zero and says so, which is a visible break and not a silent pass.
- gh makes `--watch` wait for a first check. The poll then costs one read before the wait, and the paragraph's measured fact names gh 2.100.0, so a reader can tell it is history.
- GitHub lists a pull request's first check later than two minutes. The orchestrator's report then says no check reported on a pull request whose checks arrive later. The owner reads that in the report, so the failure is visible, not a false pass.
- `--watch` ends while a job that waits on another job has not yet listed its check. That depends on when GitHub creates a waiting job's check, which no read-only probe here can show. It concerns the wait itself, not when it starts, and no run has reported it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Poll `gh pr view <N> --json headRefOid,statusCheckRollup` every ten seconds until the pushed commit has a check, for at most two minutes, and then run `gh pr checks <N> --watch` | A slow first check past two minutes is reported as none, and the report shows that to the owner. A renamed JSON field makes the poll's command fail visibly. | Chosen. It reads a parser's result, a SHA and a count, which `skills/core/SKILL.md` *The first value* prefers to reasoning over printed text. It covers both ways the wait starts early: no check on the new head, and the old head still named. The ten-second interval is gh's own `--interval` default in watch mode (`gh pr checks --help`, executed). |
| 2. Run `gh pr checks <N> --watch` again while its exit is 1 and its stderr reads `no checks reported` | It matches gh's wording, which a gh release can change, and then a no-check exit reads as a failure again. Read before the head moves, the old commit's finished checks make `--watch` exit 0 at once, which is a false pass. | Rejected. It gates on a spelling, and it misses the case after a push. |
| 3. Poll `statusCheckRollup \| length` alone, without the head SHA | Right after a push to an open pull request, the count can be the old commit's checks. The poll ends at once, and `--watch` reads finished checks and exits 0. | Rejected. It covers the new pull request and misses the push, which the section's own paragraph names as a moment the orchestrator waits. |
| 4. Sleep a fixed time, then run `--watch` | It has no end condition. A start slower than the sleep fails as it does today, and every push pays the whole sleep. | Rejected. |
| 5. Watch each workflow's run with `gh run watch` | One workflow's run can pass while another workflow's check fails. The sentence this work rewrites states that reason, and it still holds. | Rejected. The reason stays in the new paragraph. |
| 6. A `seal` command that polls and watches, and returns one exit code | A script would answer exactly, and the orchestrator would wait on its exit. But 0.27.2 builds no feat (milestone 76's description). A new command is a mechanism with no record of what it caught (`skills/core/SKILL.md` *The rule a mechanism is kept against*), and the poll is two `gh` calls the orchestrator already makes. | Rejected for this release. It is the change to weigh if the written wait keeps going wrong in runs. |
| 7. Replace the structure: the orchestrator stops waiting on CI and leaves the result to the owner | A defect that only one platform shows is found when the pull request opens, and the repair path in the same section (lines 255-262) starts from that CI result. Without the wait, the repair has no trigger, and the defect reaches the owner's merge unread. | Rejected. The premise that keeps the wait was checked: `skills/code-review/orchestration.md:255-262` (read) starts the repair from the pull request's CI. |
| 8. Also rewrite the Projects (classic) sentence at lines 265-268 | That sentence is in another paragraph, and the REST call it names works. Changing the command it gives needs a probe that writes a pull request body, which a frame cannot run. | Out of scope (`frame/design.md` *Scope*, Out). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 and 2 | Each of the four new assertions is seen red with `813665f0`'s `skills/code-review/orchestration.md` put back, and green after. Then, in one command, `bin/test` on the 13 modules that name the file (executed: `git grep -lE 'code-review/orchestration\|"code-review", "orchestration' -- tests`): `tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py tests/text/test_broad_gate_rule.py tests/text/test_review_axes.py tests/text/test_the_rules_have_one_owner.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`, together with the modules that glob `skills/`, which the crafter lists by contract rule 2's method and names in its phase record. | b5d82ed2 |
| 2 | `frame/design.md` *Scope* item 3: the fragment, and in the commit that adds it, `.claude-plugin/plugin.json` moved from `0.27.1` to `0.27.2`. `docs/branch-and-release.md` *Cutting a release* names the version move as the orchestrator's, and `docs/the-record-layout.md` *A change writes fragments, never a shared file* names the `### Process changes` row as the orchestrator's. The orchestrator's spawn for this phase hands the crafter both, so they land in the one commit with the `### Fixed` entry. | The proofer and the sealer read the fragment against the diff. `git show --stat` of the phase's commit lists `changelog.md` and `.claude-plugin/plugin.json` together. The modules that read `.claude-plugin/plugin.json` run in one command, and the crafter lists them with `git grep -ln 'plugin.json' -- tests`. | |

## Operational impact

No migration, environment variable or dependency. Where a pull request runs CI, the orchestrator's wait after each push gains a poll, usually one or two reads ten seconds apart before `--watch` starts. Where no check ever reports, the wait now ends after two minutes with a line in the report, where before it ended at once with exit 1. The plugin's version moves from `0.27.1` to `0.27.2`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
