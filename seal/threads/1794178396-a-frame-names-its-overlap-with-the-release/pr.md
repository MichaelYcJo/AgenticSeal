- "**A frame names where its work meets the release's other work items and which of them merges first, and the orchestrator merges in that order (#1443).**" (`changelog.md` *Changed*, the first item)
- "Two items meet where both change the same file, or where one changes a rule, a check or a fact that the other's change reads or adds content to." (`changelog.md` *Changed*, the first item)
- "Where two plans state opposite orders for one pair, or the item ordered first cannot be sealed before the other, the orchestrator chooses the order and writes it as a row of *Judgments of the run* in the plan of the item it merges out of the stated order." (`changelog.md` *Changed*, the first item)
- "**The plugin's version moves from 0.35.1 to 0.36.0** in `.claude-plugin/plugin.json`." (`changelog.md` *Changed*, the second item)
- "The pull request's title takes `feat:`, and the kind that came closest is `fix:`." (`frame/plan.md` *Judgments of the run*, the prefix row)
- "whether a framer writes `frame/plan.md` *Overlap with the release* as `agents/framer.md` steps 4 and 8 ask, and whether an orchestrator merges in the stated order" (`gaps.md` *Not verified*, the second row)

Closes #1443.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
