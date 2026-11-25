# Follow-up

**What belongs here, and it is a narrow list.**

A **schedulable item in a repository with no tracker** — something a person
could plan, in a project that has nowhere else to file it. This repository has
a tracker, so it should normally hold none of those.

**Every row names a person, with no condition attached.** An answerer column
reading `repository owner, next time X is opened` is a
condition wearing a person's clothes: nobody agreed to open `X`, so nobody
answers. A row that
cannot name who answers it does not belong in this file.

**Anything tied to a coordinate is a `# RIDER:` comment at the line it is
about.** `grep -rn "RIDER:"` is the repository-wide list, and it needs no file
kept in sync. A rider is not "someone should do this" — it is *"if you open
this file, do this too"*, and its whole value is arriving at the person who
opens the file. Moving it to the coordinate is what makes `next time X is
opened` do its job instead of being written down as though a person had
promised it.

An issue is no better for that purpose. It reaches whoever browses the
tracker; nobody greps the issue list before editing a hook. And a rider has no
completion of its own — it closes when the file it rides on is next changed,
which nothing can schedule.

**What that costs.** Nothing forces a rider to be deleted, so a comment can
outlive the fix it asked for. A rider is a comment and nothing more: it
carries no stamp, and no check reads it. **A rider outliving its fix is the
reader's finding.** Whoever opens the file reads the rider against the code in
front of them, then does what it asks and deletes it, or deletes it as spent.
The judgment is that a rider outliving its fix costs a confused reader for a
minute, while a rider nobody ever sees costs the defect. **This is written
down so it can be overturned**: if spent riders mislead more readers than live
ones reach, the trade was wrong and the list comes back.

## Schedulable items with nowhere else to go

| Item | Who must answer |
|---|---|
| Whether `seal layout --moved` (`skills/verify/scripts/test_layout.py#_moved_main`), the move check `CONTRIBUTING.md` *The test layout* asks for, is kept or dropped, weighed by `skills/core/SKILL.md` *The rule a mechanism is kept against* on what it has caught against what it costs. #1576 kept it in 0.38.6 and sent the question here | the repository owner |
| Whether the AST analyser of `tests/skills/test_session_cost.py`, the units from `SITE_KINDS` to `#classify`, is kept or dropped, weighed by the same rule. Its one recorded catch is #175. #1576 kept it in 0.38.6 and sent the question here | the repository owner |
| Whether the next release's classification of a repository that runs the chain counts fewer fix-made findings on a count or a universal than the 14 of 72 that #1613 measured in owlery releases 0.0.2 to 0.0.4, the issue's second *Done when* line. As many or more sends contract rule 19's clauses on what a change writes to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*. #1613 sent the question here in 0.39.0 | the repository owner |
| Whether the next release's classification of a repository that runs the chain counts fewer findings reopened because a fix left a copy, and fewer findings that named one place stating a fact and did not search for the others, than #1612 measured in owlery releases 0.0.2 to 0.0.4, the issue's second *Done when* line. Beside that count, the transcripts of the same release's sessions and subagents show what each mechanism did: each note of the hook is an `attachment` of type `hook_success` named `PostToolUse:Edit` that holds `skills/agent-contract/SKILL.md` rule 19, and whether the agent's next `Edit` changed a place the note named tells a note acted on from one ignored or false; each refusal of the quote check is a `seal pr-body` output that holds "quotes words" and "does not hold"; each finding whose `evidence:` line carries a listing command is read in the round records. A mechanism whose notes or refusals were mostly ignored or false, or that caught nothing in the release, goes to the same weighing even where the count fell. As many or more sends `seal pr-body`'s quote check, the finding's listing command and `hooks/edit-leaves-copies.py` to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*. #1612 sent the question here in 0.39.0 | the repository owner |
| Whether the next release's classification of a repository that runs the chain counts fewer fix-made defects from a unit no frame designed, and fewer from a fold's restatement, than #1614 measured in owlery releases 0.0.2 to 0.0.4, the issue's second *Done when* line. Beside that count, each mechanism's own record is read: the fix pass's stop, as each round finding whose close `answer:` names a *Scope* item a fold commit added after the round's `target:`, and each *Judgments of the run* row that sent a finding to the fold because its fix needs a unit, with whether a later round's `regression:` or `reopens:` line names that finding; the orchestrator's sort before the pass, as the same rows split by whether the orchestrator sent the finding before the pass or the fix pass's hand-back named it; and the narrowing, as each fold commit after a fix pass read for a frame sentence it added that describes what was built, with each later finding located in a frame sentence a fold wrote. A rule that never fired in the release, or whose folded units are followed by a `regression:` or `reopens:` line as often as #1614's `frame/design.md` G11 measured for unframed ones, goes to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against* even where the count fell. #1614 sent the question here in 0.39.0 | the repository owner |

## Riders waiting on a file another branch holds

| Target | Who must answer |
|---|---|
