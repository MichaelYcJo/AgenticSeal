# Closing memo: 1793591507-the-settle-reads-what-earlier-settles-judged

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at the branch's HEAD; the phase ran only its boundary set (contract rule 2) | answered: `trail/gate.md`, the `Broad gate` row passed at `5c01946f3` against `4ab345cba`, and `guarantee.md` sealed on it |

## Not done

`settle.py#plan_rows` names a plan whose `## Judgments of the run` heading stands twice as not read, through `rule_changes.py#section_lines`. No case holds that branch: a mutant that drops the line stays green over every judgments case. The branch came unchanged from `settle.py#judgments` as #1167 built it, and this phase only moved it into the shared reader, so a case for it is outside what the frame asks.

`--full-history` in `settle.py#earlier_judgments` is the frame's flag, and no case tells it from its absence. Without it, git's history simplification drops a deletion only where a merge's `seal/threads` matches one parent's exactly and the deletion stands on the other parent's line. A release merge into `main` brings that release's deletions, so no normal flow builds that merge, and a case would build it by hand.
