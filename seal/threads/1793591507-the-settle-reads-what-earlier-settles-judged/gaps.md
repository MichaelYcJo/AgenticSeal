# Closing memo: 1793591507-the-settle-reads-what-earlier-settles-judged

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at the branch's HEAD; the phase ran only its boundary set (contract rule 2) | the orchestrator, at `seal gate` after the review rounds settle |

## Not done

`settle.py#plan_rows` names a plan whose `## Judgments of the run` heading stands twice as not read, through `rule_changes.py#section_lines`. No case holds that branch: a mutant that drops the line stays green over every judgments case. The branch came unchanged from `settle.py#judgments` as #1167 built it, and this phase only moved it into the shared reader, so a case for it is outside what the frame asks.

`--no-renames` and `--full-history` in `settle.py#earlier_judgments` are the frame's flags, and no case tells either from its absence. The query's pathspec is `seal/threads`, so git's diff holds only paths under it, and a rename can pair two paths only when both are there. On this repository's history, the query lists 55 deleted plans with renames on and with them off (executed). A case would have to build a work item directory renamed in place, which no settle does.
