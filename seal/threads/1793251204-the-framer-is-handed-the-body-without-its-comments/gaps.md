# Closing memo: 1793251204-the-framer-is-handed-the-body-without-its-comments

## Why this work exists

The framer was handed an issue's body without its comments and asked whether they changed the request; it is now handed the request whole. A sixth framer case, on a question only running the fixture's generator answers, tells the definitions apart by where the answer is written, in `## Grounding` labelled `executed`; its grader for a row left to a measurement passed on both definitions, so the no-row half of #1047's rule is still not seen pinned (*Not verified*).

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where the page case's revision comes from | `frame/design.md` *Data & interfaces*: "The build computes the token by running the case's scaffold and the generator under its scratch directory, and records the command in the phase record." / `rule_cases.py#page_revision` runs the fixture's generator over the files the scaffold commits each time the cases are generated, and the scaffold run under the scratchpad confirmed the same `d8cac16f` | the code | `CLAUDE.md` *The rule a mechanism is kept against*: "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate." A literal would go stale without a word when `TEXTUTIL` or the generator changed |
| Where the side traces were kept | `frame/plan.md` phase 3: `--out <scratchpad>/1793251204-the-framer-is-handed-the-body-without-its-comments/sides/...` / both sides ran with `--out <scratchpad>/1158/sides/...` | the spawn's path | The spawn prompt: "Scratch work goes under `.../scratchpad/1158/`." The side files in `evals/` are the same either way |

## Not verified

| Item | Who must answer |
|---|---|
| S6: the new case was not seen red on `shape-no-measurement-row`. Both side A runs, on the definition at `c48cd5e3`, answered the generator question by running the generator or its logic and left no `a measurement` row (`evals/baseline-framer-generated-page.json`, `trail/phases/phase-3.md`). The no-row half of #1047's rule is held by a grader that has not been seen to fail on any definition, so the issue's last Done-when line for the new case is not met | the owner, at the pull request: whether `Closes #1158` stands (`frame/questions.md` Q2, default (a)) |
| S1: no check reads the orchestrator's production spawn for the line on the issue's comments; the acts table row *Orchestrator: the order inside a ticket* names the limit | the orchestrator, at each framer spawn |

## Not done

Rewording the new case's issue and running side A again (`frame/questions.md` Q2 (b)) was not taken: Q2's default (a) holds, and that default says no second spend on a case that measured what it measured. The five earlier framer cases were not run again with their new spawn line (`frame/plan.md` R3 and R4); #947 reads the whole framer suite at the end of the milestone.

## Fed back into the design

none
