### Changed

- **The framer answers a question a read-only command answers by running it (#1047).** `agents/framer.md` gains the rule *A question a command answers is answered by running it*. Where the answer is a behaviour, a time or an output, the framer runs a probe before it writes a row for anybody. A command that only reads, such as `git`, `grep` or `gh`, runs against the tree. Anything that writes runs under `<scratchpad>/<work-item-id>/frame/`, and the repository's code runs from a `git clone --no-local` there. A probe commits nothing and runs none of the repository's checks: no test module, no linter, no typechecker and no `seal gate`. The directory is gone before the framer hands back. The answer goes into `frame/design.md`'s `## Grounding`, labelled `executed`, with the command. A row whose answer is a behaviour, a time or an output is written only where no probe can run in the framer's environment, such as a CI leg on another platform, and its reason says which. The *Job* paragraph no longer lists "no script" among what the framer never builds. Steps 5 and 8, the *Never* list and the residue rule agree with the new rule.

### Added

- **A fifth framer case, `evals/behaviour/framer/rule-framer-sharp-s/` (#1047).** Its issue asks which words `shout` lengthens, `straße` among them, and only running `shout` gives the answer. Beyond the graders every framer case has, one reads that `frame/design.md`'s `## Grounding` holds a line with both `executed` and `STRASSE`. `evals/scripts/rule_cases.py` writes it, and `tests/evals/test_rule_cases.py` pins the pattern. On two runs of each side, the framer before this change failed that grader on both runs and the framer after it passed on both.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-10-29 | The framer runs a read-only probe for a question whose answer is a behaviour, a time or an output, outside the tree, and writes the answer into `frame/design.md`'s `## Grounding` labelled `executed`; an `a measurement` row is left only where no probe can run in its environment | 40 measurement rows across 0.22.x went to the build instead, and 13 were still open when their work item shipped | https://github.com/MichaelYcJo/AgenticSeal/issues/1047 |
