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
| Phase 2: sentences outside the frame's named files | `spec.md` §*Removes* names no README row and no `docs/` `Enforced by:` line for phase 2 | both READMEs' warden row and skills row, and the `Enforced by:` targets in `docs/the-agent-set.md` and `docs/the-broad-gate.md`, rewritten in the warden's commit | `spec.md` §*Grounding*, `CLAUDE.md` row: a change removes what stood on the old fact in the same commit |

## Not verified

| Item | Who must answer |
|---|---|
| CI on its three legs at phase 2's closing commit | the orchestrator |

## Not done

Nothing yet; the phases after phase 2 are `plan.md`'s rows.

## Fed back into the spec

none
