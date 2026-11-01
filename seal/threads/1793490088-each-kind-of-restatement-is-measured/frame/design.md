# Design: 1793490088-each-kind-of-restatement-is-measured

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `skills/core/SKILL.md` *The rule a mechanism is kept against* | The rule every decision is judged against. Four of its sentences decide most rows: "A fact has one source, and every other place links to it"; "A script holds a gate only on a fact it reads exactly"; "A reading that is noisy or guessed from words is reported, never used to block"; and "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate". The issue quotes the rule from `CLAUDE.md`, and the rule now stands in the core (read: `CLAUDE.md` *The core* names the core as its home, and the tree's `skills/core/SKILL.md` is the installed 0.27.0 copy's text, executed `diff -q`, no output). |
| **G2** `skills/core/SKILL.md` *The first value: efficient development through the workflow*, "Judgment is spent where meaning is the question, and a script answers the rest" | Whether two passages state the same fact, and whether one has drifted from the other, is a reading. A command lists the candidates exactly; the crafter reads each candidate and writes its verdict at a coordinate. No row decides a meaning by a grammar rule. |
| **G3** `skills/agent-contract/SKILL.md` rule 6 | No agent posts a comment, files an issue or edits a milestone. The crafter writes the table and every drafted issue into this work item's records. The orchestrator posts and files after the seal, as the spawn prompt states. |
| **G4** `skills/agent-contract/SKILL.md` rule 12 | Each kind is a class, so the list of kinds is built by a method that makes it whole: the tree is taken apart into its parts (*Data & interfaces*, *The parts*), and every pair of parts gets one of three answers in *The kinds* and the section after it: placed in a kind whose command measures it, named with the reason no fact is stated in both, or named as a pair where a fact can stand in both and no command of this audit reads it, with who answers it. The list is whole because every pair is answered, not because every pair is measured. Inside a kind, a paraphrase ranges over an unbounded domain of spellings, so no command lists every paraphrase. The row says so, and a sample is called a sample. |
| **G5** `docs/the-review-record.md` *A finding's `verdict:` decides it, and severity is for people*, "one that has not drifted is no finding, since the templates no longer invite it and #1147 audits what stands" | The policy in force gives the standing copies inside one work item's records to this audit. Kind K10 measures them. The issue's *Out of scope* line "One work item's own records: #1020" names #1020's check of recurrence across one work item's review rounds, which stays out. The owner's first comment on #1147, item 2, says the same: the copies that already stand, and have not drifted, are this audit's to count and decide. |
| **G6** `docs/the-record-layout.md` *seal/threads/<work-item-id>/* and *A fact of a work item has one record, and every other record cites it by path and heading* | The table and the drafts need a home among the files that table lists. `trail/phases/phase-N.md` answers "what building one phase found", and an audit's measurements and decisions are what its phases find. Each kind's row stands in one phase record only, and nothing else in the records restates it. A new file kind, such as an `audit.md`, would answer no question that table lists. |
| **G7** `docs/the-record-layout.md` *A change writes fragments, never a shared file* and *A commit after the build brings its changelog fragment along*; `docs/branch-and-release.md`, the bullet "Feature pull requests write their entry to `seal/threads/<work-item-id>/changelog.md` and leave `plugin.json` alone" | These clauses say where an entry goes, and the second says "A commit that changes nothing a release note states owes the fragment nothing". This work ships nothing a user installs, so no release note sentence is owed and the work item writes no `changelog.md`. `.github/scripts/publish_release_note.py` fails only where no commit of the release's range added a fragment (read, its docstring *It does fail for a range that added no fragment*), and 0.27.1's range already holds the fragments of #1150, #19 and #1128 (`trail/phases/phase-2.md` *Command K8*, its second line). Plan row A6 weighs writing one. |
| **G8** `skills/code-review/scripts/chain_check.py`, the docstring's `guarantee` arm and `CLOSING_RECORDS` | After the sealer's verdict, a commit is allowed only where it touches `trail/gate.md` or `guarantee.md` (read, `chain_check.py:65` and `:136`). A commit after the seal that writes the filed issues' numbers into any other record leaves the verdict short of HEAD, and the sealer has to run again. Plan row A7 places the numbers where no commit is needed. |
| **G9** Milestone `release: 0.27.2`, its description (executed: `gh api repos/:owner/:repo/milestones/76 --jq .description`) | Its order names "#1147's, #1020's and #951's candidate checks" among the proposals #1038 reads and decides build or drop. A decision of this audit that a kind needs a new check is therefore drafted as a candidate for `release: 0.27.2` under #1038, and is not drafted as a build. |
| **G10** Milestone `release: 0.27.1`, its description (executed: `gh api repos/:owner/:repo/milestones/77 --jq .description`) | #1147 runs after #1150, #19 and #1128, which have merged (read: the three directories under `seal/threads/` at `bf9efcba`). #1197 comes after this item and removes `tests/behaviour/test_one_word_one_meaning.py`; this audit measures that module under K5 and does not decide it again. The issue's *Order* line "After #1020 merges" is older than the milestone's order (the orchestrator's finding, read against the milestone: #1020 is open in `release: 0.29.0`). |
| **G11** `docs/issues-and-milestones.md` *An issue is titled like a commit* and *A milestone answers when, and takes three shapes* | The shape of each drafted issue's title, its prefix, and the reason its proposed milestone fits. |
| **G12** The issue's first owner comment, items 1 and 3 | K9 and K14. The comment counted item 1's citations and item 3's `check: none` lines at `6be0c1f1`. Each row re-counts its item at `bf9efcba` and holds the figure once: `trail/phases/phase-1.md` *The table*, row K9, and `trail/phases/phase-2.md` *The table*, row K14. A figure that differs from the comment's carries its own commit, so the difference is no drift. |
| **G13** The probe of 15-word runs shared between files at `bf9efcba` (executed: a scratch script under the scratchpad that copies the normalisation of `tests/text/test_no_passage_is_pasted_into_a_second_file.py#words` by reading, run with `python3 -I` over every tracked `.md` except `*.ko.md` and every `.py`; deleted before the hand-back) | It sizes the verbatim half of the measurement, so a phase can read every candidate. 538 files read. The pairs between policy documents (`docs/` with `docs/`) share no run, and `docs/` with `skills/*.md` share 4. The large counts lie in code and evals: `evals/` with `evals/` 10,552 runs over 674 file pairs, `hooks/` with `skills/*/scripts/` 1,288 over 64. One passage of 24 runs stands in 13 hook entry points and 5 skill scripts. `seal/README.md` and `templates/setup/seal-README.md` share 824 runs. Docstrings restate policy, for example `docs/the-review-record.md` and `hooks/question-gate.py` share 55. The probe's counts are runs, not facts, which is why *Data & interfaces* counts passages. |

## Scope

In.

1. **The audited commit.** Every count is taken at `bf9efcbab22f421dd5255e6f2b0af77832b6b7e5` (`bf9efcba`), the tip of `origin/release/v0.27.1` this branch was cut from (executed: `git rev-parse --short origin/release/v0.27.1`). Each command reads git objects at that commit (`git grep <pattern> bf9efcba -- <paths>`, `git show bf9efcba:<path>`) or runs from a copy of it made with `git archive bf9efcba` under the scratchpad. This work item's own directory is in no kind's corpus.
2. **One row per kind, K1 to K14 of *Data & interfaces*, each with its measurement.** A row holds the kind's command or commands, written whole so a later run can repeat them; the count of passages or facts the kind holds twice; how many of those have drifted; and the drifts the record shows were caught, by what, and how late. Each drifted instance is named in the record with its coordinates. Each row names what its commands cannot see.
3. **One decision per kind, with its grounds.** The decision is one of the issue's four: one source and a link, a check, a written rule the proofer reads, or nothing. Its grounds cite G1's sentence it stands on and the row's own measure of what the copies cost and what was caught. Where a mechanism already holds the kind (*Data & interfaces*, column *What already holds it*), the row weighs removing or replacing that mechanism as an equal of keeping it, by what its record caught against what it costs.
4. **One drafted issue per decision that changes the tree.** Each draft holds a title in the form of G11, a body with the measure it rests on and its own *Done when*, and a proposed milestone with the reason it fits. A decision that a kind needs a new check is drafted for `release: 0.27.2` as a candidate #1038 decides (G9). Two kinds whose decisions are one change share one draft, and the second row cites the first's draft id.
5. **The comment text.** The comment the orchestrator posts on #1147 is one preamble and the rows of K1 to K14, in that order, copied from the phase records verbatim, with each draft id replaced by its issue number. The preamble names the audited commit and the paths of the two phase records.
6. **The closing memo.** `gaps.md`, from its template, names what went out unmeasured and who answers it.
7. **The pairs no command reads.** *Pairs no command of this audit reads* names each pair of parts where a fact can stand in both and no kind's command reads it. One drafted issue, D8, carries them to their answerer, `gaps.md` names them as not done by citing that section, and the comment's preamble says the audit measured the pairs its kinds place and names the rest by that section.

Out.

- The recurrence of a finding across one work item's review rounds: #1020's check, in `release: 0.29.0`, as the issue's *Out of scope* says (G5).
- Building any decided change. Each is drafted here, filed by the orchestrator, and built by its own issue.
- `tests/behaviour/test_one_word_one_meaning.py`'s removal: #1197's, after this item (G10). K5 measures the module and cites #1197 as its decision.
- Posting the comment, filing the issues, editing a milestone, and writing the issue numbers anywhere: the orchestrator's acts (G3, G8).
- A changelog fragment (G7).
- Measuring the pairs *Pairs no command of this audit reads* names: D8's, filed by the orchestrator at the seal. The issue's *What the audit does* item 1 lists seven kinds and asks for no pair beyond them. The section names each pair's known instance where the audit met one.
- Any check of the repository's run by the crafter beyond the narrow cases plan row *Phases* names (contract rule 2).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A count repeats | Given a row of the table, when a reader runs its command at `bf9efcba` as the record writes it, then the command prints the row's count | executed: the proofer runs every row's command |
| S2 A drift can be opened | Given a row whose drifted count is above 0, when a reader opens each drifted instance's coordinates at `bf9efcba`, then the two places state the fact differently | read: the proofer opens each instance, or a stated sample of them where a row names more than ten |
| S3 A decision stands on the rule | Given a row's decision, then its grounds quote the sentence of G1 it applies and cite the row's measure of cost and catch | read |
| S4 A decision that changes the tree has a draft | Given a decision other than nothing, then a draft with a title, a body and a proposed milestone with its reason stands in the record under its draft id, and the row's issue cell names that id | read |
| S5 The comment fits | Given the preamble and the rows of K1 to K14 joined in order, then the text is at most 65,536 characters, the length GitHub accepts for one comment | executed: `wc -c` over the joined text |
| S6 The tree changes only by the records | Given HEAD of the branch, when `git diff --name-only bf9efcba..HEAD` runs, then every path it prints is under `seal/threads/1793490088-each-kind-of-restatement-is-measured/` | executed |
| S7 Every pair is answered | Given *The parts*, then every unordered pair of parts, each part with itself included, is placed in a kind whose command reads it, or named with the reason no fact is stated in both, or named in *Pairs no command of this audit reads* with who answers it; and a kind's row that a pair is placed in for part of its facts names the part its commands do not read | read: list the 78 pairs of P1 to P12 and find each in *The kinds*, the placement paragraph or the section after it |
| S8 The open part is named | Given a row, then it names what its commands cannot see, and a sample is called a sample | read |

## Data & interfaces

### The parts

The tree at `bf9efcba`, taken apart into the places a fact can be stated (executed: `git ls-tree --name-only bf9efcba`, and a count of `.md` and `.py` files per directory). The parts are not the whole tree: the tracked files no part holds are listed by `trail/phases/phase-3.md` *Command parts*, and D8 carries them with the unmeasured pairs.

| Part | Paths |
|---|---|
| P1 policy | `docs/` |
| P2 instructions | `skills/**/*.md` (the core and the contract among them) |
| P3 definitions | `agents/` |
| P4 templates | `templates/` |
| P5 root files | `README.md`, `README.ko.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `TRADEMARKS.md` |
| P6 the records root | `seal/README.md`, `seal/config.md`, `seal/follow-up.md` |
| P7 work item records | `seal/threads/<id>/`, this work item's excluded |
| P8 code text | docstrings, comments and printed messages in `hooks/`, `skills/*/scripts/`, `bin/`, `.github/scripts/`, `.github/workflows/`, `evals/scripts/` |
| P9 tests | `tests/` |
| P10 evals | `evals/` outside `evals/scripts/` |
| P11 the tracker and the releases | the GitHub Releases, the issues and their comments |
| P12 the tree's own state | what a command reads from the tree itself: which files exist, what a line holds, how many of a thing there are, what a source file enumerates |

### The kinds

| Kind | Pairs of parts | What the commands list | Record of drift in the issue | What already holds it |
|---|---|---|---|---|
| K1 policy and policy | P1 with P1 | verbatim passages | none named | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` |
| K2 policy and instructions | P1 with P2, P1 with P3, P2 with P2, P2 with P3, P3 with P3 | verbatim passages; each contract or core rule an agent definition cites | #1040 | the same module; `tests/text/test_a_moved_rule_leaves_its_definition.py`; `tests/text/test_the_rules_have_one_owner.py` |
| K3 root files and the rest | P5 with P1, P2, P3, P4 | verbatim passages; the layout trees each file draws | #1055 | the same module; `tests/text/test_the_rules_claude_md_names_have_one_home.py`; `docs/the-record-layout.md` *The root records*, the direction rule, `check: none reader: the proofer at review` |
| K4 the editions | `README.md` with `README.ko.md`; `docs/one-root-by-lifetime.md` with `docs/one-root-by-lifetime.ko.md` | the outline; the sections whose facts differ, by reading both editions section by section | #1055 (the gate list) | `tests/behaviour/test_both_editions_carry_the_same_folds.py` |
| K5 tests and evals and the rule text | P9 with P1, P2, P3; P10 with P2, P3 | phrase pins, by the method `475653e7:seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/design.md` states; eval graders that quote a definition | #1111 | #1111's kept pins; `tests/behaviour/test_one_word_one_meaning.py` (#1197) |
| K6 templates and what describes them | P4 with P1, P2, P3; P6 with P4 | each template's headings and table headers against every sentence that lists them; `seal/README.md` and `seal/config.md` against their `templates/setup/` source | none named | the template pins under `tests/behaviour/` |
| K7 records across work items | P7 with P7 across two work items; P7 with P1 | verbatim passages; `## Rule changes` `from:` quotes against the section they quote | the issue's item "records and records across work items" | `skills/settle/scripts/rule_changes.py` reads a `from:` against its section |
| K8 the release notes | P7 `changelog.md` with P11 Releases | a copy of the notes in the tree; Releases whose body differs from what the fragments at the tag build | #1053 | `tests/github/test_publish_release_note.py` |
| K9 a process document holding a rule a shipped file cites | P1's three process documents with P2, P3, P4, P8 | each citation into `docs/branch-and-release.md`, `docs/release-checklist.md` or `docs/issues-and-milestones.md` from a shipped file, and the rule it reads there | the owner's comment, item 1 | none |
| K10 standing copies inside one work item's records | P7 with P7 inside one work item | verbatim passages between the records of each of the three work items at `bf9efcba` | 0.24.0's recurring findings that stood in records alone, counted in `docs/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading* | `docs/the-review-record.md`, the drifted copy is a finding |
| K11 code text and the policy | P8 with P1, P2, P3 | verbatim passages between a docstring or comment and a rule document; a message a script prints that states a rule | none named | none |
| K12 code and code | P8 with P8; P9 with P9; P10 with P10; P8 with P10 for the eval cases a script under `evals/scripts/` writes | passages of source text that stand in more than one module or case | `seal/follow-up.md`, the row on `console.to_utf8()`, measured at `11f3cde8`; `trail/phases/phase-2.md` *The table*, row K12, re-counts it at `bf9efcba` | none |
| K13 the tree's own state restated | P12 with P1, P2, P3, P4, P5, P6 and P8, the shipped text outside `tests/` and `evals/behaviour/` (`trail/phases/phase-2.md` *Whether the frame holds*, the K13 item) | each `path:line` coordinate in shipped text; each figure about the tree stated without its moment; each list of an enumerable source (registered hooks, agents, skills, templates, `seal/config.md` items, `seal` subcommands) | `seal/follow-up.md`, the row on a figure about a corpus | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` for cited headings |
| K14 the rules no test holds | each `check: none reader:` line in a rule file, by reader | for each such rule, the records at the release tags that cite its section, as evidence its named reader read it | the owner's comment, item 3 | `.github/scripts/rules.py` reads the line's shape |

**The unit counted.** A passage is a maximal run of words, after the normalisation of `tests/text/test_no_passage_is_pasted_into_a_second_file.py#words`, that stands in two or more files; one passage held by thirteen files is one passage, with thirteen holders. A fact-anchored unit is one coordinate, one figure, one list, one citation or one rule. *Held twice* counts units. *Drifted* counts units whose holders state the fact differently at `bf9efcba`, judged by reading. A list that differs from its source counts as drifted without a reading, since the comparison is exact.

**The commands.** Each row's command is written whole in the record, in a fenced block, and runs at `bf9efcba` with no file outside a scratch copy of that commit. A command longer than a line is a `python3 -I - <<'EOF'` block whose text stands in the record. A command may import a function of the tree at `bf9efcba`, such as `shared_counts`, from the scratch copy, and names the file it imports.

**Caught in the record.** The drifts of a kind the record shows are read from the issues, with each search written whole as its `gh` command, and from the round records at the release tags, with each `git grep <pattern> <tag> -- 'seal/'` written whole. A keyword search is a sample, and the row calls it one. For each drift found it names who caught it (a person reading, a review round, a check) and how late (the releases between the copy's commit and the catch, where `git log` gives both).

Every pair of parts not in the table above, the pairs unordered and each part with itself included, gets one of the three answers of design G4 here or in the next section.

- **Placed in a kind whose command reads it.** P5 with P5 outside the editions, and P6 with P1 or P2, are K3's, whose passage command reads them (`trail/phases/phase-1.md` *Command setup*, the pairs it lists for K3). A figure stated in P5 or P6 is K13's, whose *Command figures* reads every shipped `.md`, whatever the figure's source.
- **No fact stated in both: a record against any part but the policy.** P7 with P2, P3, P4, P5, P6, P8, P9, P10 and P12, and P7 with P11 for every record but a changelog fragment, which is K8's: a record's table posted on an issue, as this audit's comment is, states the commit the record names. A record states what it read at the moment it names: a round record its `target:` commit, a phase the commit in `plan.md`'s Status, a frame its mark's "before the build". A later change of the other part leaves the record a past state and not a copy that drifted (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, "A round record carries the SHA it reviewed, so it never asserts a present state"). What a record shares with a template (P4) is the form the template gives it, which the record's readers read as the form. The one quote in a record that asserts a present state is a `## Rule changes` `from:`, which quotes P1 and is K7's. `trail/phases/phase-2.md` *Instances K7* and *Instances K10* read the records' shared passages as quotes of what each record checks or as the template's own text.
- **No fact stated in both: a dated entry of the tracker.** P11 with P1, P2, P3, P4, P8, P9, P10 and P12, and P11 with P5 or P6 for any fact but a figure: a closed issue, a comment and a Release state the tree as it stood at their date, as a record states its commit. The release notes, the one tracker entry built from the tree, are K8's.
- **A fact can stand in both, and the framer answers it: an open issue's body or a milestone's description against the tree.** The same pairs as the bullet above. An open body is a request that ranks below the tree's documents, and the framer of the work item that takes it opens what it cites (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*, "Verify clause numbers a ticket cites"). This audit's own spawn is an instance: the issue's *Order* line against the milestone's order (G10).
- **No fact stated in both: P12 with P12.** The tree's state is the source the other parts restate, and it does not state itself twice.

### Pairs no command of this audit reads

In each pair below a fact can stand in both parts, and no kind's command reads the pair. D8, which the orchestrator files at the seal, answers each: it measures the pair with the command of the kind nearest it, or closes it with the reason no record shows a drift there. Where a pair has a known instance, the row names it.

| Pair | What can stand in both | Known instance, or what a kind already reads of it |
|---|---|---|
| P1 with P10 | an eval case or grader quoting a policy rule | K5 reads P10 with P2 and P3 only |
| P3 with P6 | a definition stating what `seal/README.md` or a `seal/config.md` row says | none |
| P4 with P4 | two templates stating one form, such as a foot line's shape | none |
| P4 with P8 | a heading or field a script matches and the template that writes it | none |
| P4 with P9 | a test pinning a template's heading or column | the template pins *The kinds* names under K6 |
| P4 with P10 | an eval fixture carrying a template's text | none |
| P5 with P6 | a root file and the records root stating one fact | the layout tree, which K3's *Command trees* reads (`trail/phases/phase-1.md`); no command reads the pair's passages |
| P5 with P8 | a root file and a docstring or printed message stating one behaviour | none |
| P5 with P9 | a test pinning a sentence of a root file | `tests/text/test_the_rules_claude_md_names_have_one_home.py`, K3's mechanism, holds `CLAUDE.md`'s needles |
| P5 with P10 | an eval fixture carrying a root file's text | none |
| P6 with P6 | two files of the records root stating one fact | none |
| P6 with P8 | a records-root file and the script that reads it, such as the opt-in marker `hooks/lib/optin.py#MARKER` holds | none |
| P6 with P9 | a test pinning a records-root sentence | none |
| P6 with P10 | an eval fixture carrying a records-root file's text | none |
| P8 with P9 | a test pinning a message a script prints | #238's case pinning the notice `hooks/version-check.py` prints (`gaps.md`) |
| P8 with P10 | an eval case copying code text that no script writes | K12's *Command regenerate* reads the cases a script under `evals/scripts/` writes |
| P9 with P10 | a test and an eval case stating one fact | none |
| P11 with P11 | an open issue's body and a milestone's description stating one order or scope | the issue's *Order* line against the milestone's order (G10) |
| P12 with P9 | a coordinate or figure in a test's docstring or comment | K13's corpus leaves out `tests/` (`trail/phases/phase-2.md` *Whether the frame holds*, the K13 item); the record's instances are named in `trail/phases/phase-3.md` *Whether the frame holds*, the item on drift the hand-back did not count |
| P12 with P10 | a coordinate or figure in an eval case | K13's corpus leaves out `evals/behaviour/` (the same item) |

### The table

The comment's rows, and each phase record's table, have these columns:

| Kind | Command | Held twice | Drifted | Caught in the record | Decision | Grounds | Issue |
|---|---|---|---|---|---|---|---|

The *Command* cell cites the fenced block by its heading in the same record, since a table cell cannot hold a block. The *Issue* cell holds a draft id, `D<n>`, or `none`. The fenced blocks and the instance lists stay in the records; the comment links each record at the sealed commit.

### A drafted issue

Under its draft id: the title; the body, with its measure, its scope and its *Done when*; the proposed milestone, with one sentence of why it fits, read against the milestone's description; and the kinds it answers.

## Rule changes

- nothing
  why: The audit measures and decides, and it changes no rule. Each decision that changes a rule is filed as its own issue, and that issue's design states the rule change.

## Removes

- nothing
  why: The work adds this work item's records and nothing else, and adds no mechanism. What each decision takes out of the tree is named in its drafted issue, and that issue's design names it in its own `## Removes`.

Framed 2026-11-01 by framer, before the build.
Reframed 2026-11-01 by framer, after round 2.
