# Design: 1793541311-the-seal-root-files-listed-at-one-home (#1232)

## Grounding

Every coordinate is at the base, `origin/release/v0.27.3` at `cd694aa3`, unless its row names another commit.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | The `seal/` root's files are one fact, the list of them. One place holds it and every other place links it or lists what it lists, the issue's *Done when*. |
| G2 `docs/README.md` *The records*: `docs/the-record-layout.md` answers "where each kind of record lives". `docs/the-record-layout.md`'s opening: "A file that states a rule this index gives another home links to that home and does not restate it [...] Where a copy is found, the copy is the defect." | The home of the list is `docs/the-record-layout.md` *seal/*, and of the work item's files *seal/threads/<work-item-id>/*. A skill that draws the same list is the copy. |
| G3 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the `docs/` row: "a pull request does not edit it", and a design states its changes in `## Rule changes`. | `docs/the-record-layout.md` *seal/* gains its two rows through this design's `## Rule changes`, and so does every sentence of `docs/` this work makes untrue. The build edits no file under `docs/`. |
| G4 The measure, read at `48d035aa`, #1237's squash on `main`: `git show 48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md`, *The table* row K3 and *Instances K3*. The issue cites it at `79252e48`, which no branch holds (executed: `git branch -a --contains 79252e48` lists none; #1270). | At `bf9efcba` the skill's tree lacks `config.md` and the *seal/* table lacks `parity.md` and `pact.md`. The measure's decision for K3: "one source and a link". It rules that `templates/setup/seal-README.md`, and `seal/README.md` written from it, describe the directory they stand in and keep their tree. |
| G5 P1 below (executed): the drift still stands at the base. | The base draws the `seal/` tree in five files. `skills/implement/SKILL.md:102-116` lists no `config.md`. `docs/the-record-layout.md` *seal/* tables `README.md`, `config.md`, `follow-up.md` and `threads/<work-item-id>/` only. |
| G6 Contract rule 12, *A defect belongs to a class, so enumerate the class*. | The class is every place that lists the root's files, drawn or in prose. P1 lists the drawn trees by their box lines; P2 lists every six-line window of a tracked text file outside `seal/threads/` naming three or more of the root's entries. Three prose lists beyond the issue's are in scope (Scope items 2 to 4). Both methods match spellings, so the list is a sample for a list written in words neither matches; *Scope* says where that part stands. |
| G7 #1102, open in `release: 0.29.0` (executed: `gh issue view 1102`), and its comment 6552868724 (executed: `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6552868724`): "The layout tree links the home #1232 gives it." | `README.md` and `README.ko.md` keep their trees in this work; #1102 links them. |
| G8 `skills/settle/SKILL.md` *Rule changes* and *The index*. `docs/README.md` names `docs/the-record-layout.md` and `docs/one-root-by-lifetime.md` with its `.ko.md` edition. | Each `file:` is picked from that index. `docs/the-record-layout.md` *A document with a `.ko.md` edition changes with it, heading for heading*, and `5560c742`'s design wrote a separate `change` for `docs/one-root-by-lifetime.ko.md`, so the Korean edition takes its own item. |
| G9 The unsettled designs' rule changes (read): `seal/threads/1793538229-each-passage-keeps-its-home/frame/design.md` (#1231) changes `docs/the-record-layout.md` *The root records*; `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md` (#1258) changes `docs/release-checklist.md` *5. The release pull request*. | Neither names *seal/* or *The root and its lifetimes*, and *The root records* and *seal/* are sibling `##` sections, so no group of the settle holds both. The policy in force at each section this design changes is the baseline. |
| G10 `docs/one-root-by-lifetime.md` *The root and its lifetimes*: "The layout, file by file, is `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* and `docs/the-record-layout.md`." The Korean edition says the same under *루트와 그 안의 수명*. | Once the skill draws no tree, that sentence names a section that does not give the layout file by file. Contract rule 19: it changes in the same work, through `## Rule changes`. |
| G11 Each note the skill's tree carries has a home outside the tree (read). | `routing.md` written by the session before the first edit and never by a subagent: `skills/implement/SKILL.md` *3. The SDD file set*, the file table's `routing.md` row. The round records leaving at the settle after their release: `docs/the-record-layout.md` *seal/threads/<work-item-id>/*, "The files keep these paths until the settle after their release, and leave together". `trail/gate.md` written by `seal gate --record`: `docs/the-review-record.md` *What the check reads at the pull request*. `guarantee.md` from `templates/records/sdd-guarantee.md`: `agents/sealer.md` *Order of work* step 5 and `docs/the-review-record.md` *The guarantee*. Removing the tree loses no fact. |
| G12 `tests/text/test_no_passage_is_pasted_into_a_second_file.py#test_a_removed_copy_passes_without_a_baseline_edit` (read): "a pair whose count goes down passes". | Removing lines of `skills/implement/SKILL.md` can only lower the `README.md` pair's count, so the ratchet's stored entry for it does not turn red. |
| G13 `seal/config.md` (read) has no `Record language` row. | The records are English. |
| G14 The issue's comments (executed: `gh issue view 1232 --json body,comments`). | It has none, so the body is the request. |

### The probes

Each ran from `<scratchpad>/1793541311-the-seal-root-files-listed-at-one-home/frame/`, which is gone.

- **P1, the drawn trees** (executed). The measure's *Command trees* reader, `^[│ ]*[├└]── +([^ ]+)` over every tracked `.md` file, keeping a file whose entries name `follow-up.md`, run over the worktree at `cd694aa3`. It printed five files. `README.md:123-138`, `README.ko.md:118-132`, `seal/README.md:83-101` and `templates/setup/seal-README.md:83-101` list `README.md config.md parity.md pact.md follow-up.md threads/`. `skills/implement/SKILL.md:102-116` lists `README.md parity.md pact.md follow-up.md threads/`. The *seal/* table lists `README.md config.md follow-up.md threads/<work-item-id>/`.
- **P2, the lists in prose** (executed). Every six-line window of a tracked `.md`, `.py`, `.yml` or `.txt` file outside `seal/threads/`, kept where it names three or more of: `config.md` or "repository's config"; `follow-up.md` or "follow-up list"; `parity.md` or "migration config"; `pact.md` or "the pact"; `threads/`. It printed windows in nine files. Read one by one: the five of P1; `docs/the-record-layout.md` *Every kind of record, at a glance* and *seal/*; `skills/implement/SKILL.md:76`, the `seal/` row of the lifetimes table, "the repository's config, the migration config, the follow-up list"; `skills/verify/orchestration.md:433`, "the root also holds `config.md`, `follow-up.md` and `README.md`"; `skills/implement/scripts/seal.py:94-95`, the module docstring, "Root-level files — `follow-up.md`, `config.md`, `parity.md` — are NOT counted"; and `agents/crafter.md:35-36`, a reading order that lists no root.
- **P3, the rule changes parse and their `from` stands** (executed). In a `git clone --no-local` of the worktree, checked out at `cd694aa3`, `skills/settle/scripts/rule_changes.py#parse` read this design's `## Rule changes` with the policy root `docs`, and `#section_lines` found each `from` in its section with runs of whitespace collapsed. It parsed three `change` items with no refusal and no line named as not read; each section was found once (*seal/* at lines 267-278, *The root and its lifetimes* at 10-26, *루트와 그 안의 수명* at 10-28), each `from` was found in it, and no `to` was.

## Scope

In:

1. **The skill draws no tree.** In `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the fenced tree (lines 100-117) goes. The sentence that leads into it keeps what it says of lifetimes, that what sits directly under the root is permanent and what sits under `seal/threads/` lives as long as its work item, and links `docs/the-record-layout.md` *seal/* and *seal/threads/<work-item-id>/* for each file and the question it answers. The paragraphs after the tree stay.
2. **The lifetimes table lists no root file.** The same section's table, row `seal/`, everything above `threads/`, keeps "Written and read by machines" in its Authority cell and drops the list "the repository's config, the migration config, the follow-up list", which omits `README.md` and `pact.md`. Item 1's link, a few lines below in the same section, names where the files are.
3. **The flow log's location row lists no root file.** In `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, the row `Findings by Location`, the clause "the root also holds `config.md`, `follow-up.md` and `README.md`, which are the repository's own and belong under `docs`" keeps its rule, that everything under the root outside `seal/threads/` is the repository's own and counts under `docs`, and links `docs/the-record-layout.md` *seal/* in place of the three names.
4. **The export docstring lists no root file.** In `skills/implement/scripts/seal.py`'s module docstring, *What the reminder counts, and what it does not*, "Root-level files — `follow-up.md`, `config.md`, `parity.md` — are NOT counted" names the root-level files as every file the root holds outside `threads/`, citing `docs/the-record-layout.md` *seal/*, in place of three of them. No code changes.
5. **The policy changes** are this design's `## Rule changes`, which the settle after 0.27.3 writes: the *seal/* table gains `seal/parity.md` and `seal/pact.md`, and `docs/one-root-by-lifetime.md` with its Korean edition names the record layout alone for the layout file by file.

Out, each with its grounds:

- **`README.md` and `README.ko.md`.** Their trees list what the home lists once item 5 is settled (P1), and #1102 links them (G7).
- **`templates/setup/seal-README.md` and `seal/README.md`.** Each describes the directory it is written into and keeps its tree (G4). Each lists `README.md config.md parity.md pact.md follow-up.md threads/` (P1), what the home lists once item 5 is settled.
- **`docs/the-record-layout.md` *Every kind of record, at a glance*.** It indexes kinds of record, each with its home, and does not list the root's files: its `seal/config.md` and `seal/follow-up.md` rows are the homes of two kinds. The migration config and the pact are each one opt-in's file, with their own documents, `docs/the-review-and-parity-arms.md` and `docs/the-pact.md`.
- **`agents/crafter.md:35-36`.** A reading order naming `seal/follow-up.md` and `seal/parity.md` because the crafter reads those two, not a list of the root (P2).
- **The `seal/threads/<work-item-id>/` half of the seal-README trees.** The issue's class is the root's files. Whether those trees' thread entries match *seal/threads/<work-item-id>/* is not this work's question, and no row of the measure counts it.
- **A list of the root's files written in words neither P1 nor P2 matches.** No search reaches it (G6). It is the proofer's to find at review.
- **Any edit to a file under `docs/`** (G3).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A builder looks up where a root file belongs | Given the build, when a builder reads `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, then it finds the two lifetimes and one link to `docs/the-record-layout.md` *seal/* and *seal/threads/<work-item-id>/*, and no tree | `git grep -n -E '├──\|└──' -- skills` lists nothing; `tests/behaviour/test_a_cited_section_stands_in_its_file.py` green, which holds that each cited section stands |
| S2 Every list of the root's files links the home or lists what it lists | Given the build, when P1 and P2 are run again, then the drawn trees are those of `README.md`, `README.ko.md`, `seal/README.md` and `templates/setup/seal-README.md`, each listing `README.md config.md parity.md pact.md follow-up.md threads/`, and the windows in `skills/implement/SKILL.md`, `skills/verify/orchestration.md` and `skills/implement/scripts/seal.py` name no subset of the root's files | P1 and P2 re-run at the phase boundary, their output in the phase record |
| S3 The settle writes the home whole | Given 0.27.3 released, when the settling session runs `seal settle`, then *seal/* shows one group with this design's `change`, its `from` found; once written, the table holds the six entries P1's trees list | P3 at the frame; the settle's dry run |
| S4 The policy names one home for the layout | Given the settle, when a reader opens `docs/one-root-by-lifetime.md` *The root and its lifetimes* or *루트와 그 안의 수명*, then the layout file by file is `docs/the-record-layout.md` alone | P3 at the frame; the settle's dry run |
| S5 The check reads the rule changes | Given the pull request, when `chain-check` reads this design through `skills/settle/scripts/rule_changes.py`, then it parses three `change` items and refuses nothing | P3; the pull request's chain step |

## Data & interfaces

None. No schema, command, message or exit code changes; item 4 changes a docstring.

## Rule changes

- change
  file: docs/the-record-layout.md
  section: seal/
  from: | `seal/config.md` | what this repository says about itself, one row per item |
  to: | `seal/config.md` | what this repository says about itself, one row per item |
    | `seal/parity.md` | which codebase this repository ports behaviour from, and at which baseline commit; present only where a migration is declared |
    | `seal/pact.md` | what two or more repositories keep together; present only in the repository that holds the pact |
- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: The layout, file by file, is `skills/implement/SKILL.md`
    *Document layout — two roots, three lifetimes* and `docs/the-record-layout.md`.
  to: The layout, file by file, is `docs/the-record-layout.md` *seal/* and
    *seal/threads/<work-item-id>/*.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: 파일 하나하나의 배치는 `skills/implement/SKILL.md` *Document
    layout — two roots, three lifetimes* 와 `docs/the-record-layout.md` 에
    있습니다.
  to: 파일 하나하나의 배치는 `docs/the-record-layout.md` *seal/* 와
    *seal/threads/<work-item-id>/* 에 있습니다.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `seal/` tree | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the fenced block at lines 100-117 | `docs/the-record-layout.md` *seal/* and *seal/threads/<work-item-id>/*; each note the tree carries stands where G11 names |
| The list in the lifetimes table's `seal/` row | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the Authority cell of the row `seal/`, everything above `threads/` | `docs/the-record-layout.md` *seal/*, linked once in the same section (Scope item 1) |
| The three names in the location row | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, row `Findings by Location` | `docs/the-record-layout.md` *seal/* |
| The three names in the export docstring | `skills/implement/scripts/seal.py`, module docstring, *What the reminder counts, and what it does not* | `docs/the-record-layout.md` *seal/* |
| The skill named as a home of the layout file by file | `docs/one-root-by-lifetime.md` *The root and its lifetimes* and `docs/one-root-by-lifetime.ko.md` *루트와 그 안의 수명* | `docs/the-record-layout.md`, through `## Rule changes` at the settle |

This work adds no mechanism: no gate, check, test, mark or rule grammar.

Framed 2026-11-01 by framer, before the build.
