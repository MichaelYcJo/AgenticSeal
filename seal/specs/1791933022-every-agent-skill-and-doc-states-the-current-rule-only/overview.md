# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — overview

📋 implement applied
· spec:     `spec.md` §*Non-inferiority, proved per phase*, §*Scope*, S9–S13, S16, §*Data & interfaces*; `plan.md` phase 2, T10–T12, E1/E7; `questions.md` Q6, Q7; `agents/warden.md` §*Report*; `docs/the-reader-registry.md` through `tests/reader_registry.py#GRAMMAR`
· evidence: none — the ledger left the tree in 0.22.0 (#944)
· verified: executed — the Q7 probe (three replay runs), every scaffold, the three sealer fixtures through `broad-gate`, 26 mutations, the census and layout modules; read — the eval runner's grader and case schema from the binary's own authoring prompt

## Why this work exists

A rewrite of an agent's preload is judged against today's definitions by a
suite nobody scores by hand, so compacting cannot ship a worse agent unseen.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Phase order | `plan.md` orders the check (phase 1) before the harness (phase 2) / phase 2 was built first | phase 2 first | the orchestrator's decision at this spawn: phase 1 is #930's checker and waits for #930's branch to settle, and phase 2 depends on none of it |
| S10's first variant | S10: the warden "with its `## Report` fence deleted … the comparator writes `Verdict: fail`" / that side wrote the same table and the comparator wrote `pass` | the measurement stands; S10 is shown by its second variant, the `Needs a fix:` rule removed, which is `fail` | `evals/q7-fence-deleted.md` and `evals/q7-needs-a-fix-removed.md`; the fence has copies the warden reads (`phases/phase-2-suite-build.md`) |
| T10's reading | `spec.md`: the test recomputes "for every `agents/*.md` and preloaded skill that differs from the merge base" / it compares each agent's preload hashes with the ones the baseline recorded | hashes | spec silent on how the merge base is found; a hash comparison needs none, holds on a worktree and in CI, and an edit after a passing record makes the record stale |
| Scaffold field | `plan.md`: each case carries `scaffold.sh` / the runner reads `context.scaffold_script` as a path | `scaffold.sh` named by that field | measured: an inline script is refused as a path that does not exist |
| Case bounds | `plan.md`: `case.yaml` carries `runs`, `max_turns`, `timeout_seconds`, `model` / the runner reads the last three under `execution:` only | under `execution:` | measured: top-level copies are dropped |
| Rule cases | `spec.md`: one case per census rule an output can show / one fixture case per agent run, each carrying one `rule-` grader per rule | graders per rule, cases per fixture | a census row names `<case>/<grader>`, which a grader per rule satisfies; one fixture per rule would multiply the 38 runs by the rule count |
| Replay selection | `spec.md`: from the tree's rounds and the last two tags / the four smallest diffs with truth, one per work item | smallest first | cost: a verifying round of ~100 lines is ~$2.5 a run; the generator lists all 22 rounds with truth |
| Replacing one case | `plan.md` phase 1: the two cases "replaced from `--list`" / the generators wrote only the N smallest, one per work item, which would pick the ledger round again | `--case NAME` on `replay_targets.py` and `seed_defects.py`, exit 1 for a name not on the list | a case written by hand would be the one case nobody can regenerate; `replay-1791382684-r2` shares its work item with `replay-1791382684-r5`, which the one-per-item rule would refuse and `spec.md` names as the first candidate |
| A run with no cost | `spec.md` rule 5: a side cut by `--max-cost-usd` or a timeout is no result / a run whose trace has no `result` event, or one missing `total_cost_usd`, `duration_ms` or `usage` | the side's spend, tokens and seconds are unknown and the verdict is `no result` | T3 (`plan.md`): such a trace is "refused" and never read as zero cost; a cost of zero would pass rule 4 by construction |
| `evals/commit-gate/` | `plan.md` phase 1 (ii): each pre-0.22.0 case fixed to the measured schema or removed | removed at c7d8bcc8 | it guarded that the commit gate interrupts an unreviewed commit inside the eval. Its scaffold made `.specseal/`, which opts nothing in (`hooks/optin.py`), so the gate could not fire, and its grader passed on any `review` in the last message. No agent's preload decides the gate; `tests/test_the_commit_gate_decides_at_the_commit.py` and `tests/test_an_automation_run_meets_no_commit_prompt.py` hold it |
| `evals/lint-hook/` | the same | removed at c7d8bcc8 | it guarded that the PostToolUse lint hook reformats a Python file. Its scaffold configures no ruff, so `hooks/lint-python.py` stays out by design and the grader failed by construction. The hook is in no preload; `tests/test_lint_python.py` holds it |
| `evals/implement-proof/` | the same | removed at c7d8bcc8 | it guarded that a bare session invokes the implement skill, writes the file and ends with the proof block. The file is held by the four smith cases' `shape-built`, through the agent that preloads the skill. The proof-block regex scores a sentence of the skill, the class phase 1 (i) removed, and nothing in the tree parses that line. The bare-session trigger is held by no other case (row in `## Not verified`) |
| `evals/review-verdicts/` | the same | removed at c7d8bcc8 | it guarded that code-review catches a planted spec violation and ends with its proof block. `warden/rule-warden-one-finding` plants a spec violation and grades the finding on its path and line, through the agent that preloads code-review. The proof block is the same sentence grader, and the `Skill` grader's pattern also matches Claude Code's built-in `code-review` skill, so it could not tell which skill fired |
| `evals/pr-body-style/` | the same | removed at c7d8bcc8 | it guarded that a Korean PR body follows writing-style, scored by an LLM judge, which `spec.md` §*The proof* refuses. No agent writes a PR body (contract §6), so no preload rewrite is measured by it. No other case holds it (row in `## Not verified`) |
| The budget sentences outside §*Removes* | `spec.md` §*Removes* lists the budget sentences by coordinate / the concept also stood in `skills/verify/SKILL.md`'s two step counts, `broad_gate.py`'s comment over `PARTITION`, a pin in `tests/test_the_seal_is_taken_once_by_the_sealer.py`, the durations refresh in `CONTRIBUTING.md` with the failing case's message and two cases, a comment in `tests/test_ci_gives_the_checks_what_they_need.py`, and the 0.22.0 changelog fragments of #931 and #944 | each rewritten in place at 6ef6f36e | `CLAUDE.md` §*The rule a mechanism is kept against*: a change removes what stood on the old fact in the same commit; listed in `phases/phase-2.md` |
| A floor the budget step kept | not in §*Removes* / `test_the_workflow_reader_finds_the_env_assignment_the_file_already_has` held at least four base spellings in `hygiene.yml`, and the budget step was the fourth | the reader's count is held against an independent listing of the file's code lines naming a base | a floor on the tree's count stops being true when a step leaves; the listing holds at any count |
| Where the release table is read | `plan.md` row 2: `docs/release-checklist.md:82–93` rewritten in place / that paragraph sat in §2, the preparation commit, before the release pull request exists | the paragraph is in §5, *The release pull request* | the table prints only on the pull request into `main` |
| T6's reach | `plan.md` T6: a renamed target on a scratch copy of the tree / every target the tree shows is in `docs/*.md`, so a rename alone passes a walk of `docs/*.md` alone | a gone target is also planted in a file of each other glob | the case has to be red under the mutation T6 names |
| When a fix of a fix stops the passes | `spec.md` S9 and §*What leaves*: "at the second such round in a run the orchestrator runs no fix pass" / `questions.md` Q1, answered after the frame: "a fix of a fix stops the fix passes before round 3 as well, and the item goes back to its framer" | any round carrying the mark stops the passes (`docs/the-review-record.md` §*The run*); `spec.md` S9 and its two §*What leaves* rows rewritten to it at 1912e63d | Q1 is the owner's answer and postdates the frame; the phase 3 spawn names it as governing |
| Where T15 lives | `plan.md` T15: `tests/test_broad_gate.py::test_a_file_naming_another_commit_fails_a_ready_pull_request` / the arm that fails is `chain_check.py`'s | `tests/test_chain_check.py::TestMain::test_a_broad_gate_file_naming_another_commit_fails_a_ready_pull_request` | #942: a test sits in the file of the module it exercises |
| The check's cutoffs and the approval notice | the old check grandfathered items by `*_FROM` ids and printed a notice for an unfilled `plan.md` approval line / `spec.md` §*Data & interfaces* names five arms and neither | both left with the rebuild | neither is among the arms the spec names; every item a cutoff excused is merged and is not judged again |
| The panel's `item` and `rounds` rows | `spec.md` §*Data & interfaces*: "the panel and the stamp values are unchanged" / `item` read `#<pr> · <id>` from the record's `PR` row, and `rounds` appended `· capped` from `Needs a fix` | `item` is the id alone; `rounds` counts every record's deferrals and carries no `capped` | both fields leave the record by the same spec; nothing else holds what they read |
| Which SHA is a broad-gate run | the old reader took the first SHA-shaped word of the cell / a cell whose tree word is not a SHA then reads the base as the run | the first word of the newest entry, where it is SHA-shaped | found by `tests/test_broad_gate.py::TestSpelling` while building; reading the base as the run passes a stale gate |
| `⬜` outside the records | S10 lists `⬜` / 19 code comments cite a past finding as `round 1's ⬜ 4`, and `questions.md` and `## Not verified` use `⬜` as an open status | left | neither is the severity the record removed; the citations are history in comments, #940's and #942's when those files are rewritten |
| The two hook test modules | §*Removes*: `tests/test_chain_hooks.py` and `tests/test_chain_hooks_hardening.py` leave whole / they held 77 cases on the commit gate, the lease, `hooks.json` and the READMEs beside 21 on the guard | restored at ed63c3af without the guard's cases | the frame's coordinate was wider than its reason, "the check at the pull request" replaces a reminder, not the commit gate; deleting them left `docs/the-review-and-parity-arms.md`'s `Enforced by:` resolving nowhere |
| S10's other spellings | S10: none of the fields outside `seal/specs/` and `changelog/` / history in test docstrings (`tests-todo row 5`), the replay cases' quoted prompts, `truth-2`'s citation of `docs/round-record-spec.md:693` at its clone's commit, stale `.test_durations` entries | left | each records a past state that is true as written; rewriting a replay's prompt or truth would change what the case replays (`phases/phase-3.md`) |
| A pact print at the pull request | §*Removes* lists `chain_check.py#pact_notices` / `docs/the-pact.md` §*A signer's CI prints and verifies nothing* still stated the print and its three cases | the section states that nothing reads the pact at a pull request, enforced by nothing | the arm and its module left with phase 3's first half; the document had kept their rule |
| The em-dash console case | not in §*Removes* / `test_console_is_not_utf8.py`'s plain-text case drove the guard's reminder | removed | no plain-text post-bash gate prints non-ASCII now; the dispatcher's `reconfigure` is unchanged and its JSON cases stay |

## Not verified

| Item | Who must answer |
|---|---|
| The baseline: the four agents' suites run twice on the merge base, none cut short | the orchestrator, at the phase boundary (`phases/phase-2-suite-build.md`, the hand-back's command) |
| A smith, framer or sealer case run through the eval: their scaffolds and the sealer's gate outcomes were run, their sessions were not | the orchestrator's baseline run, which is their first |
| The full suite, the repository-wide lint and the typecheck over this branch | the sealer, once the rounds settle |
| ✅ The five pre-existing cases under `evals/*/` hold their bounds at the top level, and four of them an inline scaffold, both of which the runner drops | removed at c7d8bcc8, each on the grounds in its divergence row; `tests/test_evals_layout.py` now holds every case under `evals/` to that schema |
| A bare session's use of a skill the rewrites change: implement and code-review invoked from their descriptions, and a PR body written to writing-style. No case reads either once the five cases left, and every case runs through an agent | the orchestrator, at the phase that rewrites each skill |
| The `release-report` job on GitHub: its shell step, the `gh api` calls and the summary append ran nowhere; the script ran locally against v0.21.1 with that tag commit's real job list | 0.22.0's release pull request into `main`, the job's first run |
| S12's seconds over the modules naming `chain_check` or `broad_gate`: 1,482 s read from `.test_durations`, whose entries predate this phase and hold none for `test_chain_check.py` or `test_broad_gate.py` | the sealer's broad run, which measures them |
| How the eval runner grades `not_contains` on a file that was never written, which the sealer's two non-green cases ask of `broad-gate.md` | phase 4, which replaces the three cases |
| Whether the old check also paired a deleted declaration with an added one as a rename (`chain_check.py#changed` diffs with `-M`) | the repository owner, at phase 4's arm work |

## Not done

The baseline, which is the orchestrator's act. The changelog fragment, which
is phase 5's. The hygiene step that fetches `refs/pull/*/head`, which the
rebuilt check no longer needs: removing it reaches `broad_gate.py`'s step
list, two test modules and two release documents (`phases/phase-3.md`).
`evals/scripts/replay_targets.py` reads a round's asked paragraph from a
section new records do not carry (part B).

## Fed back into the spec

none
