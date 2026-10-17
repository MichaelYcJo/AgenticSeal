# 1792126889-every-agent-is-written-anew-from-its-job — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show goes here, each part written when it happens. -->

implement applied
· spec:     spec.md, plan.md, questions.md, phases/phase-1.md, phases/phase-1b.md; #957's body
· tests:    phases/phase-N.md name each case this work added or changed and how it was seen red
· verified: phases/phase-N.md label each command executed or read, with its exit

## Why this work exists

Every agent definition carried its own history and preloaded every skill it
might need; each is written anew from its job, preloads the contract alone
and opens a skill when its act comes, and each rewrite is proved not worse
on outcome and cheaper in tokens against one baseline.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Phase 1: where the in-tree baseline JSON is written | `plan.md` phase 1 names `--out seal/specs/<id>/evals/baseline-<a>.json`; `noninferiority.py run` saves its raw traces beside `--out` | `--out` in the session scratch directory, then `run --from-raw` into the tree, `cmp` identical | `spec.md` §*How the rewrite is proved not worse*: "the raw output stays outside the tree" |
| Phase 1b: what the verdict judges | the frame as drawn judged shape and reach graders on the new side alone and tokens within 1.1 times the baseline's, from the case session's `usage`, with spend judged too | every rule against the baseline; tokens across every model from `modelUsage`, strictly below the baseline's; spend and seconds judge nothing | the owner, 2026-10-17, after phase 1 measured the warden baseline failing its own shape rule and `usage` holding 1.9-11.6% of the tokens; `spec.md` §*How the rewrite is proved not worse* was rewritten to it |
| Phase 2: the wrap check and a definition's `Enforced by:` lines | `spec.md` §*The shape of a definition* item 6 closes each rule with one `Enforced by:` line; `tests/test_docs_line_wrap.py` held such a line outside a fold statement to 88 columns, which one `path::test` target already passes | the wrap check skips, in a file `rules --check` reads, the `Enforced by:` lines of targets that reader resolves | spec silent; a check refusing the shape the spec asks for is fixed rather than the shape bent |
| Phase 2: what rule 5 divides by | after phase 1b rule 5 judged the total tokens across every model; run 1 read 17.8% more in all with 19.3% more tool calls and four more truth finds | tokens across every model per tool call, every `tool_use` block of the trace; total, per true find, spend and seconds recorded and judging nothing | the owner, 2026-10-17, after phase 2's run 1; `spec.md` §*How the rewrite is proved not worse* rewritten to it |
| Phase 2: the call counts the frame quotes | `spec.md` §*How the rewrite is proved not worse* says the warden made 34% more calls and its tokens per call fell 12.3%, from the smith's hand-summed 954 agent calls | the traces: 854 agent calls (+20.3%), 890 `tool_use` blocks against 746 (+19.3%), tokens per call -1.25% | `calls.py` over the kept raw output, `phases/phase-2.md`; rule 5 passes on either figure, and the frame's sentence is the frame's to correct |
| Phase 2: sentences outside the frame's named files | `spec.md` §*Removes* names no README row and no `docs/` `Enforced by:` line for phase 2 | both READMEs' warden row and skills row, and the `Enforced by:` targets in `docs/the-agent-set.md` and `docs/the-broad-gate.md`, rewritten in the warden's commit | `spec.md` §*Grounding*, `CLAUDE.md` row: a change removes what stood on the old fact in the same commit |
| Phase 3: the contract's section numbers | `plan.md` phase 3: "§1 to §N in the new order", every citation rewritten | each rule keeps its number where it stays, the new rules follow at §17 to §20, and 20 citations moved instead of every one | the plan fixes no order, and a renumbered citation is a site to rewrite and review for nothing (`phases/phase-3.md`) |
| Phase 3: one spawn for the build and the evaluation | `plan.md` phase 3 is one row | built and evaluated by two spawns, after a first spawn surveyed for three hours and edited nothing and was stopped | the orchestrator's watchdog; a build and its paid evaluation are separate acts (`phases/phase-3.md`) |
| Phase 3: the framer's verdict | `plan.md` phase 3: every agent's record reads `pass` | the framer reads `fail` on rule 5 (tokens per tool call +18.9%) with its own file nearly unchanged; the phase is closed on it | the framer is rewritten by #968, and the milestone's close judges every agent's last side against af9c924b, so the regression is carried, not dropped |
| Round 1: what the contract's §2 says | `plan.md` phase 3 and `spec.md` §*Scope*: §2 says no agent runs the broad gate and the orchestrator runs it before the sealer | §2 says no agent but the sealer runs it, and that #969 moves the run to the orchestrator | the move of the gate went to #969 with phase 5, and a §2 naming the orchestrator contradicted the sealer it is preloaded into (`rounds/round-1.md` finding 1) |
| Phases 4 to 6 | `plan.md` rows 4 to 6: the smith, the framer, the sealer and the scribe in this item | moved to #967, #968, #969 and #970, each measured against the tree it starts from | the owner, 2026-10-17: one issue per agent, smaller reviews, independent merges |

## Not verified

| Item | Who must answer |
|---|---|
| closed CI on its three legs at phase 2's closing commit | the orchestrator, 2026-10-18: the `tests` workflow green on ubuntu, macOS and Windows at 314f6166 (run 39041691702), 155920f5 (run 39043767134) and 7e8e194e (run 39044553922), the last holding the code the broad gate ran at cc43f940 |
| closed Whether a sentence can end the warden's record with no `verdict:` line (one in 18 in phase 2's run 2, five in 18 in run 1), or a check at the hand-back must | the orchestrator, 2026-10-17: a check — phase 3 had the warden read its record through `chain_check.py` before handing back; it did in 18 of 18 runs and no record lacked a `verdict:` line (`evals/warden-phase-3.md`) |

## Not done

The smith, the framer, the sealer and the scribe are #967 to #970. The sealer's phase-3 record measures a definition that contradicted the new contract and is not the sealer's result. #966 holds the per-grader rule's sample size.

## Fed back into the spec

none
