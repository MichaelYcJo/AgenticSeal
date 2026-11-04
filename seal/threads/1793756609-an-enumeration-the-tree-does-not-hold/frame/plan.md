# Implementation Plan: the orchestrator's acts table goes, with the test that holds it (#506)

## Technical context

The table is `skills/implement/acts.md` (79 lines, 18 act rows; executed:
`wc -l`, `grep -c '^| '`). The test is
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` (537
lines, 14 cases). It reads headings through
`tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py#headings`,
loaded by path, and that parser stays for its own module. The policy rule
stating the table is at `docs/running/the-agent-set.md:150-162`. Every other
place that stands on the table is a row of `frame/design.md` *Removes*.

The build is one commit's worth of removals, and it has to land as one
phase. Deleting the test while `docs/running/the-agent-set.md:162` or
`docs/layout/the-pact.md:68` still names it leaves a check line that
`seal rules --check` refuses. Deleting `acts.md` while
`tests/behaviour/test_docs_line_wrap.py#COVERED` or
`tests/text/test_broad_gate_rule.py` still reads it fails those modules.

No case is added, so contract rule 15 has nothing to show red. What the
phase shows instead is that the search in acceptance A1 comes back empty,
and that the narrow modules A4 and A5 name pass.

**The failure scenario of the chosen approach, six months on.** An
orchestrator act is skipped in a run, and a maintainer wants to know which
acts have no delivery. No list answers that. The maintainer reads
`docs/running/what-a-script-gates.md` and the hooks' own documents, or the
old table at `git show v0.31.0:skills/implement/acts.md`. That is
acceptable, because the decision to arm an act starts from the measured
miss in the run's records, and the table never supplied one. If a release
finds several misses that a list would have shown earlier, the trade was
wrong, and the issue that says so cites this row.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep the table and test. Add an `ast` case that pins the docstring's case names to the module (#506 item 1), and widen the row rule to a named list of sections in other files (#506 item 3) | The named list is a second enumeration kept beside the tree, so an act in a file the list does not name is again counted by nobody, which is item 3 one step out. The `ast` case is a mechanism that catches only a docstring of the table's own test. Each addition catches drift of the table and nothing else | Rejected. It adds two mechanisms to a mechanism whose record shows no catch outside itself (`frame/design.md` *Grounding*, the rows on what the test can report and what it caught) |
| A2. Keep the table and test, and split the `Orchestrator:` marker into two meanings, one for payload and one for an act (#506 item 2's second repair) | Every marked heading is renamed or re-marked, so citations across `skills/`, `agents/` and `docs/` move, and both tests move with them. The new mark is a mark added for a table that catches only itself, which `agents/framer.md` *A mark is not the answer to a blocked step* weighs against | Rejected. With the table gone the marker carries one meaning, so the split answers a problem the removal ends (D2) |
| A3. Keep the table and test, build neither repair, and delete only the docstring's enumeration | The table keeps its cost: a row for each new marked heading, `Grounds` cells that restate other files and go stale (`1793688270`'s round 1, finding 2), and re-reading in later phases. Items 2 and 3 stay open as known limits | Rejected. The premise that keeps a structure is that it caught something outside itself, and the record shows it did not |
| A4. Keep `acts.md` as a maintainer's document, and delete only the test | An enumeration with nothing holding it drifts in silence. `skills/core/SKILL.md` says nothing is kept beside the tree to stay in step with it | Rejected |
| A5. Remove the table, the test, the policy rule and every place that stands on them, and build nothing in their place | Six months on, nothing lists which acts have no delivery (*Technical context*) | **Chosen.** It is the one approach that ends all three of #506's items and adds no mechanism |
| A6. State the removal of the policy rule as a `remove` in `## Rule changes` and leave `docs/` for the settle | `docs/running/the-agent-set.md:162` and `docs/layout/the-pact.md:68` name a deleted file until the settle, and `skills/settle/rule-changes.md` *A rule has one shape* refuses such a line. A `remove` with a `from` excuses nothing | Rejected. The work item edits `docs/` directly, as *Document layout — two roots, three lifetimes* allows for a subject in the policy root's text |
| A7. Add a case over every test module that pins the case names its docstring enumerates | The probe found 14 such docstrings in 156 modules and no name that fails to resolve, so the case would catch nothing on the day it is added | Rejected. It is #506 item 1 widened into a mechanism. Whether such pairs are measured is #1236's (O2) |
| A8. Strip the `Orchestrator:` marker from the headings of the orchestration files, now that the table no longer reads it | The marker is what `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` reads if a section is moved into a preloaded file. Stripping it removes that protection, renames the 13 headings under `skills/` that carry it (executed: `git grep -E '^#{2,3} Orchestrator:'`), and moves every citation of them | Rejected (O1) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* D1 items 1 to 10, in one commit | `frame/design.md` acceptance A1 to A7: the A1 `git grep` commands, `seal rules --check`, and the narrow `bin/test` runs A4 and A5 name. The full suite is the orchestrator's broad run | e24c3b31b |

## Operational impact

None for a deployer. The plugin ships one skill file fewer and one rule
fewer in `docs/`. No hook, script, environment variable or dependency
changes. The version stays `0.31.1`. The changelog fragment ends with a
`### Process changes` table, because both `skills/*/orchestration.md` files
change; the crafter writes it with the fragment, as the phase's spawn
asked.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | Phase 1 kept the `COVERED` comment that also heads the `multi-repository.md` entry, kept the first clause of "One parser, two readers" as the one-reader sentence A4 asks for, and wrote the `### Process changes` rows itself; D1 items 7 and 9, their `## Removes` rows, the *Grounding* process-row cell and *Operational impact* now say so | The crafter's hand-back named each statement HEAD contradicts, and each departure keeps what the frame's acceptance rows ask (`trail/phases/phase-1.md`) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph on a decision made after the frame |
| 2026-11-04 | *Grounding*'s row on the record of what the table caught states what each of its three searches returns, #1046, #1102, #1109, #1148, #1163, #1189 and #1231 beside #506, where it said only #506 and #1231 | The fix pass of round 1 re-ran the row's `"acts.md"` search and found four issues, round 1's heading search found four more, and the sealer's audit at aa296c059 found the first fold of this row had left out #1046 and #1148; the conclusion that no issue took its subject from a `still a sentence` row holds for each (the three searches, executed by the orchestrator on 2026-11-04) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph on a decision made after the frame |
