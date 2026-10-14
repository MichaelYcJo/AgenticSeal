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

## Not verified

| Item | Who must answer |
|---|---|
| The baseline: the four agents' suites run twice on the merge base, none cut short | the orchestrator, at the phase boundary (`phases/phase-2.md`, the hand-back's command) |
| A smith, framer or sealer case run through the eval: their scaffolds and the sealer's gate outcomes were run, their sessions were not | the orchestrator's baseline run, which is their first |
| The full suite, the repository-wide lint and the typecheck over this branch | the sealer, once the rounds settle |
| The five pre-existing cases under `evals/*/` hold their bounds at the top level, and four of them an inline scaffold, both of which the runner drops | the orchestrator, who decides whether this item or a follow-up rewrites them; this item reads them unchanged |

## Not done

Phase 1, by the orchestrator's order. The baseline, which is the
orchestrator's act. The ledger fragment and the changelog fragment, which
are phase 7's.

## Fed back into the spec

none
