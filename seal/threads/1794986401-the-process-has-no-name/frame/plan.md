# Implementation Plan: 1794986401-the-process-has-no-name

## Technical context

The tree as read at `c637848af`.

The places to change are the process lines `frame/design.md` G2 lists, the three citations G3 lists, and the version line G8 names. The README's opening paragraph ends at `README.md:21` and `README.ko.md:24`, and the diagram follows, so the definition paragraph goes between them. `skills/core/SKILL.md` is read by every spawn and printed by the `SessionStart` hook, and is wrapped at 76 columns. `tests/behaviour/test_docs_line_wrap.py` holds some of these files to 88 display columns, so each rewrapped paragraph is checked by that case.

The orchestrator builds the one phase, since `routing.md` answers Implementation `the session`, and writes the fragment and its process rows (G7).

Failure scenario of the chosen approach, in six months: a new document or skill calls the process "the workflow" again, because no check holds the name, and a reader meets both names. The definition paragraph in each README and the core's opening sentence are where a writer meets the name first, and the proofer reads new text against `skills/writing-style/SKILL.md`'s rule that one thing has one name. A second failure: another repository still renders the name word by word. The README's sentence that the name is not translated is the only guard, and nothing in this tree can reach that repository.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. The name "the AgenticSeal process", defined once in each README and in the core's opening, and used at every place in scope | A writer later calls it "the workflow" again, the scenario in *Technical context* | **Chosen** by the owner on 2026-11-18 (issue #1557 *Decision*). A product name is not translated, and "seal" keeps its one meaning. |
| A2. "the seal process" | A reader takes "seal" as the sealer's guarantee and the name as that one step, and a translator renders "seal" again, which is how "도장 체인" arose | Rejected by the owner on 2026-11-18, for these reasons. |
| A3. Keep "the AgenticSeal workflow", and write "GitHub Actions workflow" wherever a GitHub workflow is meant | Every GitHub Actions mention across the tree changes, far more places than the process mentions, and "workflow" still means two things in a reader's head | Rejected by the owner on 2026-11-18. |
| A4. Every "the workflow" meaning the process, across `docs/`, `skills/` and `agents/` | The diff and every spawn's preload grow, and the review reads dozens of places whose context already says which is meant | Rejected by the owner's scope (#1557 *Decision*). |
| A5. A case under `tests/text/` that refuses "the workflow" in the files in scope | It pins wording, and a GitHub Actions mention in those files would need an exception list, which is a list of spellings no script carries (`skills/core/SKILL.md` *The rule a mechanism is kept against*) | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 5 | `frame/design.md` S2's two searches print only the kept lines that scenario lists. `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_release_hygiene.py tests/text/test_every_agent_reads_the_contract.py tests/lib/test_optin.py -q` green. `git grep -n -F '0.38.2' -- . ':!seal/threads'` prints nothing; at `c637848af` it printed `.claude-plugin/plugin.json:4` alone, the line this phase changes (design G8). The proofer reads the definitions against *Data & interfaces* D1 to D5 | 61c98fac8 |

## Overlap with the release

The milestone `release: 0.38.3` holds #1557 alone (design G8), so no work item meets this one.

## Operational impact

This work item is the first and only pull request into `release/v0.38.3`, so it moves `.claude-plugin/plugin.json` from `0.38.2` to `0.38.3`, in the phase 1 commit that adds `changelog.md`. No migration, environment variable or dependency changes. A repository whose `seal/README.md` was written from the template before 0.38.3 keeps its old wording, which no gate reads beyond the marker on its first line. Every spawn's preload grows by the bytes the core gains, which the release report prints.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-18 | The title takes `docs:` | The change renames the process in documents, a skill's prose and code comments, and changes no behaviour any party or check has | `~/.claude/skills/commit-pr-convention/SKILL.md` *커밋 메시지*, the `docs:` row |
| 2026-11-18 | Design G3 and *Scope* item 3 name the three citations of the core's heading that G3's one-line search missed | The phase found them when the cited-section case refused them (`trail/phases/phase-1.md`), and G3 states the tree at `c637848af`, where all six stood | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening *The framer writes a decision's fold* |
