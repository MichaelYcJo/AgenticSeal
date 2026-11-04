# Implementation Plan: each statement is corrected to the tree (#1346, #1338)

## Technical context

Eleven corrections, each a statement that says what the tree does not hold.
`frame/design.md` *Scope* S1 to S11 gives each one's coordinate at
a3e08d64a and the claim the corrected text makes. Most are one sentence or
one comment. Three carry more than their sentence:

- S1 removes the only `Record language` from `templates/setup/seal-README.md`,
  so the file's entry in
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#ROW_READERS`
  goes in the same commit. Without that, its case goes red on a file that
  no longer tells a session which row to read. `seal/README.md` is held
  byte-identical to the template by
  `tests/behaviour/test_first_setup_asks_once.py:579`, so both copies change
  in one edit.
- S3 changes a generator and regenerates 17 `scaffold.sh` files. The
  frame's probe already made that change in a scratch clone (design
  *Grounding*): the generator exits 0 and exactly 17 files differ. That
  bounds the diff the crafter should see. `routing()` gains the work item
  id as a parameter. `RECORD_LINES` must keep the scenario heading exempt
  in its new spelling, because the word `scenario` is refused everywhere
  else in a case.
- S9's sentence is pinned word for word by
  `tests/text/test_the_release_tail_does_not_end_at_the_tag.py#test_the_fixed_name_sentence_names_the_file_that_holds_the_name`.
  The pinned literal is the drifted claim, so the case's literal and its
  docstring move with the sentence.

S5 is a list built by two censuses, one of removed modules and one of
removed cases, taken from git history and searched over every
`tests/*.py`. The crafter re-runs both at its commit, since contract rule 12
asks for the method, and the design names each command. The 12 statements
the measure found (11 in S5, 1 in S4) are joined by one it missed:
`tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py:38-40` splits
the module name across two comment lines.

No case is added and no case is asserted for a new behaviour, so contract
rule 15 has nothing to show red. What each phase shows is its acceptance
rows and the narrow modules they name.

**The failure scenario of the chosen approach, six months on.** A README,
a template or a docstring again states a set, a count or a reader, and the
tree changes under it. This work adds no check that would catch that. The
corrections cite a home (S1, S7, S9) where they could have copied it. A
citation points at the copy, and only the home can drift. What is left to
drift is a statement that cites nothing, and the same kind of measure as
#1236 finds it. The comment in `ruff.toml` and the sentence in
`CONTRIBUTING.md` (S8) still name two modules. If either module moves its
job again, both sentences are wrong again, as they were after #942.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. S1: keep the README entry's list, extended to the ten items `templates/setup/config.md` documents, with a correct sentence on absent rows | The list is a third copy of the ten items, beside the template and `skills/config/SKILL.md:38`, in a file copied into every repository at first setup. The next item the template adds leaves it short, as the list of three was left short | Rejected. The template is the home, and the entry cites it as `seal/config.md:3-5` does |
| A2. S1: cite the template and keep the README in `ROW_READERS` by naming `Record language` elsewhere in it | The README would name a row only to satisfy a list built for documents that tell a session which row to read. The entry it reads would then hold a sentence with no reader | Rejected. The file stops being a row reader, and its pin goes (`frame/design.md` *Removes*) |
| A3. S7: list all seven items of `CONTRIBUTING.md` *What a change to a gate must carry* in the template's comment | The list is a copy. The section gained *What it removes* at 5b1f6faea and *What it reads* at 96c11614f, and the template's list was not extended at either (the measure's *Instances F6*) | Rejected |
| A4. S7: cite the section, and name the prompt budget and what the change removes as the two items only the body answers | It states a second time which items only the body answers, which the section's closing paragraph states. If the section changes that pair, the template drifts the same way | Rejected |
| A5. S7: cite the section alone, as the list of what this body answers | A contributor who reads only the template sees no item until the section is opened. The template's first sentence still says why the bar is higher, and the section is one link away | **Chosen**. #1339 offers it as one of two scopes |
| A6. S9: name every file that spells the plugin's name: `plugin.json`, `marketplace.json` and both READMEs' install lines | A list of holders kept beside the tree. A new document with an install line makes it false, which is the drift F1 found in the other direction | Rejected |
| A7. S9: name `plugin.json` as the copy `plugin_directory_check.py` reads, and claim nothing about the other holders | A reader planning a rename is not told where else the name stands. The paragraph says the name is fixed and does not get renamed, and it already says a marketplace file keys its entry on the name | **Chosen** |
| A8. S4: rename the module to a name that states what it holds, and move every citation of the old name | The name is cited once outside the records, in the `check:` line at `docs/layout/the-record-layout.md:188` (executed: `git grep`), and six times in `.test_durations`. That line stands in *The root records*, where 1793732301's pending `change` operation stands. A rename edits that section beside a pending operation and moves seven lines, to correct an identifier that the docstring's first line already explains | Rejected. The premise that keeps the name was checked. The name reads as a set of rules picked out by where they came from, and the new first line says `CLAUDE.md` once named them. If a reviewer reads the name as a present claim that misleads, the rename is a follow-up with the census `skills/verify/SKILL.md` asks for |
| A9. S4: keep the name, and rewrite the docstring to what the cases hold | Six months on, a reader may open `CLAUDE.md` because of the module's name and find no rows. The docstring's first line, the first thing the module shows, says they left | **Chosen** |
| A10. S3: change `tests/e2e/teammate/test_teammate_flow.py:64` with the rest | One test fixture's title changes while about a dozen others in `tests/` keep the old round and routing titles. Each fixture's reader is a script that reads no title, which the measure judged holds | Rejected (`frame/design.md` *Out of scope* O3) |
| A11. S5's `derivers`: keep the `SyntaxWarning` catch, and give a reason that names no module | A guard that catches nothing under Python 3.12.11, 3.13.9 or 3.14.3, over all 155 tracked test modules (executed), kept for a warning nobody has seen. Its docstring's own preference is to let the next one show | Rejected. The catch and its paragraph go |
| A12. S5: add a check that refuses a docstring or comment citing a module or case the tree does not hold | The measure found 31 fixture names and 38 sentences that name a past moment among the spans that resolve nowhere. A script reading them would refuse correct text. #1344 puts a check out of scope | Rejected |
| A13. S6: replace the citation of the removed work item with the argument alone | Nothing is lost if the row already states the argument whole. If the cited section holds more than the row restates, a reader has nowhere to read it | Either form meets *Done when*. The crafter picks one when it reads the cited section at `aa687d357`, and the phase record says which |
| A14. Eleven phases, one per issue | Eleven spawns, each one to three lines of diff. Each pays a full spawn's reading for a single comment | Rejected |
| A15. Four phases, each a slice by the reader the statement misleads: the root's README with its pin, the eval generator with its cases, the test docstrings, and the documents and forms | A phase that fails holds up the items grouped with it. The four slices share no file, so a failed phase holds up none of the others | **Chosen** |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* S1 and S2 | acceptance A1 and A2: `cmp seal/README.md templates/setup/seal-README.md`, the census of `config.md`'s items re-run, and `bin/test tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/hooks/test_optin.py tests/behaviour/test_docs_line_wrap.py -q` | 8c8c8a24f |
| 2 | `frame/design.md` *Scope* S3 | acceptance A3: the `git grep` for the old forms prints nothing; after the commit, `python3 evals/scripts/rule_cases.py && git status --porcelain evals/behaviour` prints nothing; `bin/test tests/evals/test_rule_cases.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/behaviour/test_evals_layout.py tests/behaviour/test_the_sealer_guarantees.py tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py -q` | d66106009 |
| 3 | `frame/design.md` *Scope* S4 and S5 | acceptance A4 and A5: the two censuses re-run, each line listed and read; `bin/test` on every module S4 and S5 touch; `uvx ruff check` and `uvx ruff format --check` on the same files | bb9a21e77 |
| 4 | `frame/design.md` *Scope* S6 to S11 | acceptance A6 to A11: the `git show aa687d357:…` heading check, the `gh label list` lookup, and `bin/test tests/text/test_a_rider_reaches_its_file.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_docs_line_wrap.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_a_cited_commit_outlives_the_squash.py -q` | a5c2e825b |

The full suite, the repository-wide lint and the typecheck are the
orchestrator's broad run, after the rounds settle (contract rule 2).

## Operational impact

None for a deployer. No hook, script interface a user calls, environment
variable or dependency changes. `templates/setup/seal-README.md` changes,
and first setup copies it into a new repository's `seal/README.md`. A
repository that set up earlier keeps its copy, and only the marker line on
its first line is read, which is unchanged (read:
`hooks/lib/optin.py:66`, `skills/implement/bootstrap.md:17`). The 17 eval
cases change their fixture records, so a paid run after this work grades
the new cases, and runs before it graded the old ones. The last build phase
moves `.claude-plugin/plugin.json` from `0.31.1` to `0.31.2` in the commit
that adds the changelog fragment. The fragment carries no
`### Process changes` table (`frame/design.md` *Grounding*).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | #1338: the form's `labels:` line names the existing label `hooks-gates`, and no label is created | The issue says the area's label is `hooks-gates`, and `gh label list` lists it (executed by the framer). Creating `gate` would add a second label for one area | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
| 2026-11-04 | One pull request takes #1346's ten items and #1338 into `release/v0.31.2`, and it moves `plugin.json` to `0.31.2` in the commit that adds the changelog fragment, as the first pull request into that branch | `routing.md` *Why this way*; the release branch names 0.31.2, and `plugin.json` reads `0.31.1` | `skills/implement/orchestration.md` *Orchestrator: how the work is routed* |
| 2026-11-04 | #1336 regenerates the eval cases with `rule_cases.py --out` and runs no paid eval; the pull request says that the paid runs #1107, #1178 and #1266 are waiting on will grade the changed cases | #1336's *Done when* asks the pull request to say so; a paid run is not part of correcting a statement | `skills/implement/orchestration.md` *Orchestrator: how the work is routed* |
| 2026-11-04 | The design's *Grounding* row on removed modules cited under `tests/` is folded from 51 lines to 48 | Phase 3 re-ran the row's method as written and counted 48 at a3e08d64a and at 8bb802586 (`trail/phases/phase-3.md`); the frame's count was not reproducible. The row's other cells, and the 7 names of the removed-cases row, hold | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the fold of a crafter's hand-back |
| 2026-11-04 | S6 cites the removed work item at the hex commit `aa687d357`, not at `v0.13.0`, and the plugin version moves in phase 4's fragment commit, not in an orchestrator commit; the frame's sentences on both are folded | Phase 4 found `tests/censuses.py#old_names` refuses the `v0.13.0:` form and used the parent of the removing commit, whose file is byte-identical (`trail/phases/phase-4.md`); the orchestrator's spawn of phase 4 delegated the version move with the fragment | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the fold of a crafter's hand-back |
| 2026-11-04 | Round 1's four `should` findings are fixed in this pull request, none deferred; the frame's *Out of scope* O2 is folded to keep only `hooks/lib/config.py`'s code out, since its docstring took #1334's class | Each finding is a sentence of a document, a docstring or a skill stating what the tree does not hold, within #1334's, #1335's and #1341's *Done when*, and each fix changes no assertion; the fix pass found one more instance, `skills/config/SKILL.md:9-10`, and fixed it at cc3c83283 | `skills/implement/orchestration.md` *Orchestrator: drain the rows before the broad run, and keep the records*, first row |
| 2026-11-04 | Round 2's one `should` finding, a `regression:` of round 1's finding 2 located in `frame/design.md`, is fixed by the orchestrator's fold at baebc9ef8 with no fix pass and no verifying round; the run ends at round 2 | The regression is the frame's count of direct `docs/` edits, which the fix pass could not edit and the orchestrator's fold at 35e0c9af1 missed: the fix did something the frame did not say, so the frame is folded. The fold touches the work item's records alone, so the sealer reads it and no round is owed. Round 2 confirms round 1's four findings | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* and *A regression is routed by comparing the fix with the frame* |
