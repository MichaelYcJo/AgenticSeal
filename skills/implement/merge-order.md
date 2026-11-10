# implement, the merge order of a release

The orchestrator opens this file where the release holds two or more work
items, before it spawns the first framer of the release, and not otherwise.
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
holds the rest: the branch a pull request lands on, and the version move
that the first pull request into the release branch carries where the
repository names the version when it cuts that branch.

## Orchestrator: the order the work items of a release merge in

Where several work items of the release run side by side, the
orchestrator's prompt that spawns each framer names the release's other
work items: each one's issue, its branch, and its frame's path where the
frame is committed. The orchestrator merges the items in the order their
plans' `frame/plan.md` *Overlap with the release* sections state. Where two
plans state opposite orders for one pair, or where the item ordered first
cannot be sealed before the other, the orchestrator chooses the order,
with the item that carries the move still first, and writes the choice as
a row of `frame/plan.md` *Judgments of the run* in the plan of the item it
merges out of the stated order. The move goes to an
item that no plan orders after another, which the orchestrator chooses
where several are, and the orchestrator merges that item before every
other item of the release, because the first pull request into the branch
carries the move. Once it has landed, items that no plan orders against
each other merge as each is sealed. Where a crafter builds that work item
and its `frame/plan.md` *Operational impact* does not name the move, the
move is a decision the framer folds into that section, as
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* states, before the orchestrator spawns the last
phase, because the crafter reads its version write there. A move made
after a work item's last round owes a verifying round of its own, so
where the chosen item's rounds have already ended, the move goes to
another item that no plan orders after another and whose rounds still
read it, and where no such item is, the chosen item takes the move and
the verifying round it owes.
