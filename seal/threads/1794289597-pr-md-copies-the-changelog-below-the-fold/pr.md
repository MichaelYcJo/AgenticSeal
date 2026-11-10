- "The pull request check's body arm holds no layout of its own. It calls `pr_body.py#compared` (`:1818`), the function `seal pr-body --check` calls." (`frame/design.md` *Grounding*, G3)
- "Every clause of that step stays true under this design: `pr.md` is still the body's first part, written once the last phase has closed and before the first round, and `seal pr-body` still writes the body from `pr.md` and the records." (`frame/design.md` *Grounding*, G10)
- "So for this work item, and for every work item whose branch holds this change, the orchestrator writes the body with the tree's `bin/seal pr-body`, run from the work item's checkout, and the sealer's spawn names the tree's `bin/seal pr-body <item> --body <file> --check` as the command of its step 2." (`frame/plan.md` *Operational impact*, the paragraph **In this repository, until 0.37.2 is installed.**)
- "The exchange agrees with the frame's three readings of #1478" (`frame/plan.md` *Judgments of the run*, the first row of 2026-11-10)

Closes #1478.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
