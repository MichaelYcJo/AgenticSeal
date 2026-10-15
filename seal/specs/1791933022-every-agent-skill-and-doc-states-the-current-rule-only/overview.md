# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — overview

📋 implement applied
· spec:     `spec.md` §*Non-inferiority, proved per phase*, §*Scope*, S9–S13, S16, §*Data & interfaces*; `plan.md` phase 2, T10–T12, E1/E7; `questions.md` Q6, Q7; `agents/warden.md` §*Report*; `docs/the-reader-registry.md` through `tests/reader_registry.py#GRAMMAR`
· evidence: none yet — the ledger fragment is phase 7's (`plan.md` phase 7)
· verified: executed — the Q7 probe (three replay runs), every scaffold, the three sealer fixtures through `broad-gate`, 26 mutations, the census and layout modules; read — the eval runner's grader and case schema from the binary's own authoring prompt

## Why this work exists

A rewrite of an agent's preload is judged against today's definitions by a
suite nobody scores by hand, so compacting cannot ship a worse agent unseen.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Phase order | `plan.md` orders the check (phase 1) before the harness (phase 2) / phase 2 was built first | phase 2 first | the orchestrator's decision at this spawn: phase 1 is #930's checker and waits for #930's branch to settle, and phase 2 depends on none of it |
| S10's first variant | S10: the warden "with its `## Report` fence deleted … the comparator writes `Verdict: fail`" / that side wrote the same table and the comparator wrote `pass` | the measurement stands; S10 is shown by its second variant, the `Needs a fix:` rule removed, which is `fail` | `evals/q7-fence-deleted.md` and `evals/q7-needs-a-fix-removed.md`; the fence has copies the warden reads (`phases/phase-2.md`) |
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

## Not verified

| Item | Who must answer |
|---|---|
| The baseline: the four agents' suites run twice on the merge base, none cut short | the orchestrator, at the phase boundary (`phases/phase-2.md`, the hand-back's command) |
| A smith, framer or sealer case run through the eval: their scaffolds and the sealer's gate outcomes were run, their sessions were not | the orchestrator's baseline run, which is their first |
| The full suite, the repository-wide lint and the typecheck over this branch | the sealer, once the rounds settle |
| ✅ The five pre-existing cases under `evals/*/` hold their bounds at the top level, and four of them an inline scaffold, both of which the runner drops | removed at c7d8bcc8, each on the grounds in its divergence row; `tests/test_evals_layout.py` now holds every case under `evals/` to that schema |
| A bare session's use of a skill the rewrites change: implement and code-review invoked from their descriptions, and a PR body written to writing-style. No case reads either once the five cases left, and every case runs through an agent | the orchestrator, at the phase that rewrites each skill |

## Not done

Phase 1's Status cell and its phase record. Both acts of `plan.md`'s row 1
are built; the orchestrator's spawn for act (ii) keeps the phase open until
phase 3's baseline and warden rewrite, which the row itself does not say. The
baseline, which is the orchestrator's act. The changelog fragment, which is
phase 7's.

## Fed back into the spec

none
