# Implementation Plan: the settle folds named directories the person marks (#1054)

## Technical context

Every coordinate is at the base, `57d6665b5`.

- **`skills/settle/scripts/settle.py`** (1,152 lines). `main` (1056-1137) parses `--root`, `--released-at` and `--apply`, resolves the root through `hooks/lib/optin.py#home_at`, and returns the settled line before `survey` where the root holds no work item (1112-1119). `survey` (741-793) builds the dict `report` (854-963) prints, section by section, ending with what `--apply` removes and the closing sentence. `apply` (1002-1053) reads the tree again and takes nothing but `released` and `records` from the survey. The listing is a function beside `survey` that `main` calls only with `--from`, and a block of `report` printed only when it is given, so a run without the flag reaches no new line.
- **The order** is `skills/settle/scripts/rule_changes.py#order` (351-379): `git log --full-history --topo-order --reverse --no-renames --diff-filter=A --name-only` over the work items. The listing reads one `git log ... --name-status --cc` per named directory, which gives both the adding commit and the last change in one call (design P1). Each heading constant of `settle.py` is read by `tests/skills/test_settle.py#test_the_dry_runs_headings_say_who_decides`, so the new heading joins that set.
- **`skills/settle/SKILL.md`** (419 lines) holds the intro, the usage block, *What the dry run shows*, *The settling session's procedure*, *What `--apply` does* with the reference-root paragraph, and *What this does not do*. The procedure gains the first question as its opening step, the proposal and the second question after the dry run, the promoted rows in the writing step, and the rows with their marks in the body step. The new rules of *Scope* items 4 to 7 go in one new section the procedure links, so no rule is stated twice.
- **The readers of these texts.** `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` pins the reference-root paragraph's facts and classifies `seal settle` in `SHIPPED`. `tests/text/test_settle_reads_before_it_removes.py` pins the cheat-sheet cell and the skill's procedure heading. `tests/behaviour/test_docs_line_wrap.py` reads the wrap of every changed `.md`. `README.md:265` and `README.ko.md:259` carry the command's row.

**The failure scenario in six months.** A team names a directory of two hundred decision records. The proposal table is long, and the person answers "as proposed" without reading it, so a decision the session misread reaches the policy root. The pull request body still lists every row with its grounds, and the owner's review of the settle's pull request is the place that catches it. A second scenario: the owner of a named directory deletes a document a section cites by path, and the citation then names a path only git history holds. Nothing checks a bare path in `docs/`, so the citation stays until a reader meets it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| `settle.py` prints each document's section, proposal and grounds, as a literal reading of the issue's *Done when* asks | The script reads a document's words to guess a section and a mark. A decision record that names no section heading, or names one in other words, gets a wrong section or a wrong mark that reads as checked | Rejected. `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (design D5). The script prints git's facts and the session proposes |
| A separate command, such as `seal harvest`, replaces the settle for named directories and writes its own pull request | The promoted decisions and the released designs naming one section are written in two pull requests from two timelines, so neither writes the section as its latest decision | Rejected. A promoted document joins its section's group as a design does, and only the settle holds the groups. The issue names `seal settle --from` |
| A `seal/config.md` row names the directories, read at every settle | A directory named once is read at every settle whether the person meant it then or not, and the row is a configuration the issue rules out | Rejected by the issue's *The settle skill asks for them*: "no configuration row names one" |
| One proposal row per document and section, so a person marks each part | A document bearing on three sections is three rows, and the person marks parts of one decision apart from one another | Rejected. The issue asks for one row per document. A row names each section it bears on, and its grounds say what a promote writes, which lets a row promote part of a document |
| A promoted section cites its document by path in its grounds | The owner of the named directory deletes or moves the document, and the citation names a path only git history holds | Chosen. `templates/setup/config.md` *Reference specs* already asks the statement the settle folds to cite what it read, and a path opens in one step |
| A promoted section cites nothing, and the settle's pull request body alone names the document | A later reader has to find the pull request from `git log` on the section before learning that a document outside `seal/` decided it | Rejected for the reason above. The body still lists every row |
| A promoted section cites the document as `path@commit` | A squash or a rewrite orphans the commit, and the coordinate is kept beside the tree to stay in step with it | Rejected. `skills/core/SKILL.md` *The rule a mechanism is kept against* |
| A ledger under `seal/` records each skipped document, and the dry run leaves out a document the ledger holds unchanged | The ledger is state kept beside the tree, and a document edited without a commit, or moved, reads as unchanged or as new by the ledger's guess | Rejected (design G3). The last settle's pull request body already holds each row with its mark, and git says whether a document changed since that settle's merge |
| Every skipped document is proposed again with no distinction from a new one | The person re-reads and re-marks the same skipped records at every settle | Rejected. The session proposes it `skip` again with grounds naming the earlier settle, so the person's earlier mark stands unless the document changed |
| The listing reads only `.md` files | Another tool's spec in `.yaml` or `.txt` is never proposed, and a list of extensions is a list of spellings a script carries | Rejected. Every file `git ls-files --cached --others --exclude-standard` lists is a document, and the session proposes a non-decision file `skip` |
| Documents are ordered by the commit that last changed each | A record revised for a typo after a later decision moves after it and reads as the latest | Rejected as the listing's sort key. The listing sorts by the adding commit, as a design's place is read, and prints the last change beside it. The session places a promoted document in its group as of its last change, where it decides |
| `--from` beside `--apply` is accepted and ignored | A person reads an accepted flag as one the command acted on, and expects the named directory settled or cleaned | Rejected. The pair exits 2 with one sentence |
| The second question is one question per document | A run naming a directory of twenty records stops twenty times | Rejected. The issue's two questions; the table is put once, and its answers are "as proposed", "skip every row", or the row numbers to flip |
| The listing refuses a named directory holding no document | A person who named an empty directory gets exit 2 and loses the run | Rejected. The directory is listed with zero documents, and no second question follows where the listing holds none |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1, 2 and 3, and from item 8 `settle.py`'s module docstring and `--from` help and `SHIPPED`'s reason for `seal settle` | The cases for design A1 to A6, each seen red against the base, and `tests/skills/test_settle.py` with `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` in one command | `8578438c1` |
| 2 | Design *Scope* items 4 to 7, and the rest of item 8: `skills/settle/SKILL.md`, the two `README` rows and `templates/setup/config.md` *Reference specs* | `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, `tests/behaviour/test_docs_line_wrap.py` and every other module that reads a changed path, in one command; `seal rules --check` where a `check:` line is written; design A9's `git grep` read at the phase's close | `7868ee56f` |

## Operational impact

No migration, environment variable or dependency. `seal settle` gains a flag; a run without it prints what it printed. A settling session asks one question before it starts, and a second only where a named directory holds a document. A session that cannot ask takes the empty answer, so an unattended settle behaves as before.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-02 | `--from` naming a directory above the `seal/` root stays accepted, and the skill states it as a limit; design *Scope* item 2 gains the sentence | Phase 1's crafter raised it in `gaps.md` *Not done*. A person names a directory that holds decisions, and one holding the whole repository is outside that flow; a guard that subtracted the root's files would be a new reading for a shape the flow does not produce, and the session's `skip` proposal already answers it | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
