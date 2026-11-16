# Implementation Plan: 1794797697-a-census-cell-states-an-impossible-result

## Technical context

The tree as read at `75a725770`.

`agents/framer.md` is 250 lines. Its `## Rules` section opens at `:139`. The paragraph opening *A question a command answers is answered by running it* stands at `:155-170` and gives the framer read-only probes, their scratch directory and their record in `## Grounding`. The new paragraph follows it at `:171`, because it applies that paragraph's run to one more kind of command: a search whose result a frame cell states. The file is wrapped at 88 display columns and its longest line is 87 (`frame/design.md` G8).

The orchestrator builds the one phase, since `routing.md` answers Implementation `the session`. The orchestrator writes the fragment and its process row (G11 of the design).

Failure scenario of the chosen approach, in six months: the framer runs the search at the frame's commit and accounts for each line, yet the build creates a line the search matches, such as a new test that names the removed identifier in a refusal message. The run at the frame's commit could not see that line, and the crafter meets it as #1500's crafters met theirs. The fold path of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* still catches it, and the cell's stated exclusions tell the crafter where to look first. A second failure: the paragraph adds the bytes design G14 estimates to every framer spawn, paid whether or not the frame writes a search. If a release shows framers rarely writing searches, the paragraph's cost exceeds its catches, and *The rule a mechanism is kept against* removes it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. A rule paragraph in `agents/framer.md`: the framer runs the search at the frame's commit and accounts for each printed line before writing the cell, and the cell states the result the account leaves | The scenario in *Technical context*: a line only the build creates. The run at the frame's commit cannot see it | **Chosen.** G3 of the design shows the run at #1500's frame commit printed every line its crafters later met, except its own frame files, which C3 covers. The rule holds both of the issue's forms: the run is the first, and C4, a cell that names what stays, is the second. |
| A2. Only the issue's second form: a search cell names what it excludes rather than stating that it finds nothing, with no run | The framer names the exclusions it thinks of, and a kept name that matches a pattern by substring, such as `COMMENTED_OLD_TABLE`, is one no one thinks of until a command prints it. #1500's phase 2 cell already named #1492's records as what the search finds, and still failed on three other groups | Rejected. Without the run, the exclusions are as unchecked as "finds nothing" was. A1 keeps this form as its C4. |
| A3. No rule: the issue records why the folds cost less than the rule | Each search a framer writes wrong costs a crafter's search for the cause, a paragraph of a phase record, the orchestrator's re-run and a judgment row, as #1500 paid twice in one run (G2). The cell also reads as a claim no build can satisfy until it is folded | Rejected. The rule costs a `git grep` the framer can already run (it only reads), and the bytes per framer spawn that design G14 estimates. One fold's crafter search, phase-record paragraph and re-run cost more than that. |
| A4. The guidance in the templates: a note in the *Verified by* header of `templates/records/sdd-plan.md` and the *Verifiable how* header of `templates/records/sdd-design.md` | The note is copied into every frame and read as a placeholder, and the rule then has two homes, the template and `agents/framer.md`. A later change to one leaves the other stale | Rejected. A framer's rules live in its definition, which the framer reads before it opens a template. |
| A5. A script that runs each search a frame cell holds, at the pull request or in `chain_check.py` | Whether a printed line is one the build removes, one the design keeps or one in an excluded file is a judgment of meaning, which `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* keeps out of scripts. A script that runs commands written in records also runs whatever a record holds | Rejected. |
| A6. Replace the structure: no search in a *Verified by* cell at all, and the phase record lists the readers of a removed name instead | A removal then has no command that can be re-run to show the name is gone. `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row *Names or places only*, asks for that search, and the crafter's phase record already writes it there | Rejected. The premise that keeps the structure is that a search is the proof a removal owes, and the row asks for it (read). What fails is the stated result, which A1 checks. |
| A7. Move the check to the crafter: the crafter runs each search before building | `agents/crafter.md` step 3 already says whether the frame holds, and #1500's crafters ran the searches there. The cost the issue names is that check: a crafter's search for why the cell fails, and the orchestrator's fold that follows | Rejected. The defect is made where the cell is written, and the framer can run the same search there for less. |
| A8. A case under `tests/text/` that asserts `agents/framer.md` holds the rule | It pins the rule's wording, so a rewording breaks it while a framer that ignores the rule passes it | Rejected under `docs/running/what-a-script-gates.md` *The checks* (G7 of the design). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 and 2 | `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_release_hygiene.py` green. The proofer reads the new paragraph against *Data & interfaces* C1 to C5. `git grep -n -F '0.38.1' -- . ':!seal/threads'` prints nothing; at `75a725770` it printed `.claude-plugin/plugin.json:4` alone, the line this phase changes (design G10) | |

## Overlap with the release

The spawn names no other open work item of release 0.38.2, and the milestone holds #1548 alone (design G10), so no work item meets this one. #1422 of 0.38.1, which the issue names, closed with no change to `agents/framer.md` (design G12).

## Operational impact

This work item is the first and only pull request into `release/v0.38.2`, so it moves `.claude-plugin/plugin.json` from `0.38.1` to `0.38.2`. Phase 1 makes the move in the commit that adds the work item's `changelog.md`, as `docs/releasing/branch-and-release.md` *The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`.* asks. No migration, environment variable or dependency changes. A framer spawned from 0.38.2 on runs each search it writes into a frame cell, which adds one read-only command per search to its run.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
