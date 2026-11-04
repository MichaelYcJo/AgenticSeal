# Implementation Plan: each pair that can hold one fact twice is measured (#1236)

## Technical context

The work builds nothing in the tree. Each phase measures a group of the design's rows at `94635718e`, drafts an issue for each drift its rows find, and writes all of it into its own `trail/phases/phase-N.md` under `## What this phase found`. The design's *Data & interfaces* holds the methods, the pairs, the files, the editions, the row's columns and a draft's shape.

What the phases build on, by coordinate:

- The normalisation: `skills/settle/scripts/passages.py#words`, `#windows` and `WINDOW` at `94635718e`, loaded by path from the scratch copy.
- #1147's readers, read with `git show 48d035aa6:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/<record>`: `phase-1.md` *Command setup* for `passages`, `pins`, `templates` and `trees`; `phase-2.md` *Command setup* for `segments_of_code`, `runs`, `coordinates`, `lists`, `figures` and K12's whole-text reading in `code`. Each one ported names in its docstring the function it ports and each change it makes. Design G8 says why a port is needed.
- The mechanisms a row names, read for what they compare and not run: `tests/text/test_the_rules_claude_md_names_have_one_home.py` (R9), `.github/scripts/plugin_directory_check.py` (F1, F2), the readers of `.test_durations`, `pytest-split` and `test_the_durations_file_prices_the_suite` (F8) and `tests/behaviour/test_both_editions_carry_the_same_folds.py` (E1 to E4).
- The tracker through `gh`, read-only, for R18 and for each phase's search before a draft.

How the review chain reads the records. The proofer reads each phase record against the design. Every label of the phase has one row (design S3). The proofer runs each row's command at `94635718e` and compares the printed count (S1), opens the drifted instances (S2), reads each draft (S4) and runs S5's `git diff --name-only`. A finding on a row is a finding on a record, and its fix rewrites the row in its one record. The sealer reads the records against the issue's *Done when* and the tree.

Failure scenario of the chosen approach, six months on. The drafts are filed, and the records have left with this directory at the settle after 0.31.1. A later audit wants to repeat a count. The commands stand in the records at the release tag (`git show v0.31.1:<path>`), and they read `94635718e` by name, so they print the same counts. What a later run cannot repeat is the reading: whether two holders state one fact, and whether it drifted. The instance lists keep each verdict at its coordinate, so the later run reads what changed and does not judge the rest again.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** #1147's methods ported into one new probe script, its text written whole in the records, its normalisation taken from `skills/settle/scripts/passages.py` (chosen) | A ported function counts differently from #1147's, so a figure here and #1147's figure for a neighbouring kind are not comparable. Each port names its changes, and no row compares its count with #1147's | chosen (design G8) |
| A1 alternative: #1147's scripts run unchanged at the base | `audit.py#reader` finds no `words` in the test module, and `trees` reads a path that is gone, so the setup fails before the first count | rejected (design G8) |
| A1 alternative: the pairs measured at `bf9efcba`, where #1147's scripts run | The count is of text that #1102 and #1317 have since replaced, and the issue reads each pair "at the work item's base" | rejected |
| **A2** Every pair measured, and a pair closed only where its commands cannot run in the phase's environment (chosen) | A measured pair whose drifts are all paraphrase reads 0 drifted, and its whole risk sits in the open part. The row names that part (design S6) | chosen: once the script exists, a measure costs one function per method, while a closure rests on a keyword search, which is a sample (design G4) |
| A2 alternative: each pair whose #1147 row names no known instance closed by the record's searches alone | Most of the 21 pairs are never read at the base, and a later audit reads a closure as a measure of the text | rejected |
| **A3** The commands kept in the records, and no check added (chosen) | A drift on a pair that is not measured again recurs, and nothing in the tree refuses it until a review round reads it | chosen: a check stands on what it caught (design G1), and these rows are the first record of what a check here would catch; a drift that no review caught is drafted as its own issue, which may ask for a check |
| A3 alternative: the paste check `tests/text/test_no_passage_is_pasted_into_a_second_file.py` widened from its corpus (`passages.py#in_corpus`, `TOP_FILES`, `TOP_DIRS`) to these pairs | The check refuses an eval fixture's deliberate copy of a template, or a test docstring that quotes the message its script prints. Both are copies a reader acts on, so the gate answers "these differ" where nothing drifted, and it holds a gate with no record of a catch on these pairs | rejected. The premise that keeps the corpus as it is: no record yet shows what a widened corpus would catch here. Checked: #1147's *The table* holds no row for these pairs, which is why the issue exists (design G6) |
| A3 alternative: the measuring script committed under `tests/` or `.github/scripts/` | A mechanism with no record of a catch, kept beside the tree to stay in step with it (design G1) | rejected |
| **A4** Four phases by method: passages and pins, forms and files, the tree's state and the tracker, the editions (chosen) | A drift that crosses methods, such as one heading stated in a template, a script and a test, is found in two phases. The later phase's tracker search finds the earlier draft in the records, and its row cites that draft instead of drafting again | chosen |
| A4 alternative: one phase for every row | One spawn reads the code clusters and both languages of four documents, and the context runs short before the last rows; #1147 split for the same reason (read: its plan, row A1's first alternative) | rejected |
| **A5** The orchestrator files the drafts after the run's last round and before the broad gate, and records each draft id with its issue number in `## Judgments of the run` (chosen) | A draft filed before the sealer reads the records may be one the sealer finds wrong. Its correction is then a comment on or a close of a filed issue | chosen: after the verdict, `skills/code-review/scripts/chain_check.py` allows a commit to touch only `trail/gate.md` and `guarantee.md` (read: `CLOSING_RECORDS`, line 165), so numbers written after the seal need a second sealer run |
| A5 alternative: the drafts filed after the seal, their numbers named in the pull request body only | The records keep the draft ids and never the numbers, and the settle reads the records | rejected |
| A5 alternative: the crafter files each draft as its phase closes | Contract rule 6 withholds filing from every agent | rejected |
| **A6** No comment on #1236 (chosen) | A reader of #1236 alone sees no counts. The pull request that closes it links the records | chosen: the records are what *Done when* asks for, and a comment copies them; a post from this session through the harness was refused once on 2026-11-04 (the orchestrator's finding) |
| A6 alternative: a comment with every row's table, as #1147 posted | It restates the records in a third place, which is the copy #1147's run spent four rounds removing (design G16) | rejected |
| **A7** M2 lists each grader or prompt quote that stands in no rule file (chosen) | The orphan list holds quotes of a prompt's own wording or of code, which were never rule text, so it is long. Each is read, and the row counts only a quote of a rule | chosen (design G12) |
| A7 alternative: passages only for R1 | A grader quoting a sentence #1317 removed is read by no command | rejected |
| **A8** #1147's parts P1 to P12 and its 21 pairs kept as the unit of the work (chosen) | A fact whose two holders fall in one part, such as two eval cases, is K12's and not measured here | chosen. The premise: each part's path prefixes still hold files at the base, so each pair names the same files it named. Checked: each part's prefix lists files at `94635718e` (executed: `git ls-tree -r --name-only` counted per prefix), and design G7's command prints the same 11 files |
| A8 alternative: the tree cut again into parts at the base, since `docs/` is now grouped | The issue's *Done when* names the pairs of #1147's section, so a new cut leaves each pair of that section to be mapped by hand, and nothing the cut adds is a pair #1147 did not answer | rejected |
| **A9** Each edition pair read whole, section by section (chosen) | One phase reads about 730 lines in each language (executed: `wc -l` over the eight files). That phase holds nothing else | chosen: the set is closed, so a sample would be the method contract rule 12 refuses |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 2 for R1, R2, R3, R7 to R11 and R13 to R17; item 5 for those rows; item 6, `gaps.md` from its template | each row's command, run at `94635718e`, prints its count; design S3 for the phase's labels; design S5; `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` | a53d00337 |
| 2 | *Scope* items 1 and 2 for R4, R5, R6 and R12; item 3; items 5 and 6 for those rows | the same, for its rows | 1a35c6ae5 |
| 3 | *Scope* items 1 and 2 for R18 to R21; items 5 and 6 for those rows | the same, for its rows | 39bbaa6c4 |
| 4 | *Scope* item 4; items 5 and 6 for E1 to E4 | the same, for its rows; design S3 over every label; design S7 | |

## Operational impact

None for a deployer: the tree changes only under this work item's directory.

For the orchestrator, after the run's last round and before the broad gate (plan row A5):

- It files each draft with `gh issue create`, its title and body as the draft gives them and its milestone as the draft proposes, under `frame/questions.md` Q1's default.
- It writes one row of `## Judgments of the run` that maps each draft id to its issue number, in a commit that touches only this work item's records, which the sealer reads.
- Where the harness refuses `gh issue create`, the draft already stands whole in its phase record, so nothing is copied. The row names each unfiled draft by its record and heading and names the owner as its filer, the pull request body names the same drafts, and the run continues. Whether the harness refuses `gh issue create` is unverified, and the orchestrator answers it at its first attempt.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | The frame cites #1147's records at 48d035aa6, #1147's squash on `main`, where it cited 79252e48, the tip of #1147's branch | 79252e48 is on no branch the squash kept, so `tests/text/test_a_cited_commit_outlives_the_squash.py` refuses it; the work item's files at 48d035aa6 differ from 79252e48 only by `guarantee.md` (`git diff --stat`, executed by the orchestrator), so every cited coordinate reads the same | `tests/text/test_a_cited_commit_outlives_the_squash.py`; `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph on a decision made after the frame |
| 2026-11-04 | *The files* rows F1 and F8 and *Technical context* name the readers phase 2 found: `plugin_directory_check.py` reads `plugin.json`'s name and the outside catalogs' `marketplace.json`, never this repository's, and `.test_durations` is read by `pytest-split` and `test_the_durations_file_prices_the_suite`, not by `tests/conftest.py` | Phase 2's hand-back named both statements as contradicted by the tree; the orchestrator read `tests/conftest.py`'s mentions of the file and the script's `MANIFEST` line (executed: `grep -n`) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph on a decision made after the frame |
