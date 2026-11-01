# Design: 1793490088-each-kind-of-restatement-is-measured

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `skills/core/SKILL.md` *The rule a mechanism is kept against* | The rule every decision is judged against. Four of its sentences decide most rows: "A fact has one source, and every other place links to it"; "A script holds a gate only on a fact it reads exactly"; "A reading that is noisy or guessed from words is reported, never used to block"; and "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate". The issue quotes the rule from `CLAUDE.md`, and the rule now stands in the core (read: `CLAUDE.md` *The core* names the core as its home, and the tree's `skills/core/SKILL.md` is the installed 0.27.0 copy's text, executed `diff -q`, no output). |
| **G2** `skills/core/SKILL.md` *The first value: efficient development through the workflow*, "Judgment is spent where meaning is the question, and a script answers the rest" | Whether two passages state the same fact, and whether one has drifted from the other, is a reading. A command lists the candidates exactly; the crafter reads each candidate and writes its verdict at a coordinate. No row decides a meaning by a grammar rule. |
| **G3** `skills/agent-contract/SKILL.md` rule 6 | No agent posts a comment, files an issue or edits a milestone. The crafter writes the table and every drafted issue into this work item's records. The orchestrator posts and files after the seal, as the spawn prompt states. |
| **G4** `skills/agent-contract/SKILL.md` rule 12 | Each kind is a class, so the list of kinds is built by a method that makes it whole: the tree is taken apart into its parts (*Data & interfaces*, *The parts*), and every pair of parts is placed in a kind or named as holding no fact in common. Inside a kind, a paraphrase ranges over an unbounded domain of spellings, so no command lists every paraphrase. The row says so, and a sample is called a sample. |
| **G5** `docs/the-review-record.md` *A finding's `verdict:` decides it, and severity is for people*, "one that has not drifted is no finding, since the templates no longer invite it and #1147 audits what stands" | The policy in force gives the standing copies inside one work item's records to this audit. Kind K10 measures them. The issue's *Out of scope* line "One work item's own records: #1020" names #1020's check of recurrence across one work item's review rounds, which stays out. The owner's first comment on #1147, item 2, says the same: the copies that already stand, and have not drifted, are this audit's to count and decide. |
| **G6** `docs/the-record-layout.md` *seal/threads/<work-item-id>/* and *A fact of a work item has one record, and every other record cites it by path and heading* | The table and the drafts need a home among the files that table lists. `trail/phases/phase-N.md` answers "what building one phase found", and an audit's measurements and decisions are what its phases find. Each kind's row stands in one phase record only, and nothing else in the records restates it. A new file kind, such as an `audit.md`, would answer no question that table lists. |
| **G7** `docs/the-record-layout.md` *A change writes fragments, never a shared file* and *A commit after the build brings its changelog fragment along*; `docs/branch-and-release.md`, the bullet "Feature pull requests write their entry to `seal/threads/<work-item-id>/changelog.md` and leave `plugin.json` alone" | These clauses say where an entry goes, and the second says "A commit that changes nothing a release note states owes the fragment nothing". This work ships nothing a user installs, so no release note sentence is owed and the work item writes no `changelog.md`. `.github/scripts/publish_release_note.py` fails only where no commit of the release's range added a fragment (read, its docstring *It does fail for a range that added no fragment*), and 0.27.1's range already holds three (executed: `ls seal/threads/*/changelog.md` lists the fragments of #1150, #19 and #1128). Plan row A6 weighs writing one. |
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

Out.

- The recurrence of a finding across one work item's review rounds: #1020's check, in `release: 0.29.0`, as the issue's *Out of scope* says (G5).
- Building any decided change. Each is drafted here, filed by the orchestrator, and built by its own issue.
- `tests/behaviour/test_one_word_one_meaning.py`'s removal: #1197's, after this item (G10). K5 measures the module and cites #1197 as its decision.
- Posting the comment, filing the issues, editing a milestone, and writing the issue numbers anywhere: the orchestrator's acts (G3, G8).
- A changelog fragment (G7).
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
| S7 The kinds are whole | Given *The parts*, then every unordered pair of parts, each part with itself included, is placed in a kind or named with the reason no fact is stated in both | read |
| S8 The open part is named | Given a row, then it names what its commands cannot see, and a sample is called a sample | read |

## Data & interfaces

### The parts

The tree at `bf9efcba`, taken apart into the places a fact can be stated (executed: `git ls-tree --name-only bf9efcba`, and a count of `.md` and `.py` files per directory).

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
| K10 standing copies inside one work item's records | P7 with P7 inside one work item | verbatim passages between the records of each of the three work items at `bf9efcba` | 0.24.0's 12 of 17 recurring findings in records alone (`docs/the-record-layout.md`) | `docs/the-review-record.md`, the drifted copy is a finding |
| K11 code text and the policy | P8 with P1, P2, P3 | verbatim passages between a docstring or comment and a rule document; a message a script prints that states a rule | none named | none |
| K12 code and code | P8 with P8; P9 with P9; P10 with P10 | passages of source text that stand in more than one module or case | `seal/follow-up.md`, the row on `console.to_utf8()`: 6 of 13 entry points call it | none |
| K13 the tree's own state restated | P12 with every other part | each `path:line` coordinate in shipped text; each figure about the tree stated without its moment; each list of an enumerable source (registered hooks, agents, skills, templates, `seal/config.md` items, `seal` subcommands) | `seal/follow-up.md`, the row on a figure about a corpus | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` for cited headings |
| K14 the rules no test holds | each `check: none reader:` line in a rule file, by reader | for each such rule, the records at the release tags that cite its section, as evidence its named reader read it | the owner's comment, item 3 | `.github/scripts/rules.py` reads the line's shape |

Every other pair of parts falls in one of these: P5 with P5 outside the editions is K3's; P5, P6 or P9 with P11 states a figure from the tracker and is K13's; P6 with P1 or P2 is K6's where `seal/` holds a template's copy and K3's otherwise. A phase that finds a pair this table does not place adds the pair to a kind, or names why no fact is stated in both, in its record.

**The unit counted.** A passage is a maximal run of words, after the normalisation of `tests/text/test_no_passage_is_pasted_into_a_second_file.py#words`, that stands in two or more files; one passage held by thirteen files is one passage, with thirteen holders. A fact-anchored unit is one coordinate, one figure, one list, one citation or one rule. *Held twice* counts units. *Drifted* counts units whose holders state the fact differently at `bf9efcba`, judged by reading. A list that differs from its source counts as drifted without a reading, since the comparison is exact.

**The commands.** Each row's command is written whole in the record, in a fenced block, and runs at `bf9efcba` with no file outside a scratch copy of that commit. A command longer than a line is a `python3 -I - <<'EOF'` block whose text stands in the record. A command may import a function of the tree at `bf9efcba`, such as `shared_counts`, from the scratch copy, and names the file it imports.

**Caught in the record.** The drifts of a kind the record shows are read from the issues, with each search written whole as its `gh` command, and from the round records at the release tags, with each `git grep <pattern> <tag> -- 'seal/'` written whole. A keyword search is a sample, and the row calls it one. For each drift found it names who caught it (a person reading, a review round, a check) and how late (the releases between the copy's commit and the catch, where `git log` gives both).

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
