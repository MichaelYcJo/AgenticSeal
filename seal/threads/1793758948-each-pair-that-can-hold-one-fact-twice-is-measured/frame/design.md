# Design: each pair that can hold one fact twice is measured (#1236)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `skills/core/SKILL.md` *The rule a mechanism is kept against* | Three of its sentences decide most rows. "A fact has one source, and every other place links to it" is what a drift is read against. "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate" keeps every measuring command in the records and out of the tree. "A reading that is noisy or guessed from words is reported, never used to block" makes the figure lists a reported sample. |
| **G2** `skills/core/SKILL.md` *The first value: efficient development through the workflow*, "Judgment is spent where meaning is the question, and a script answers the rest" | A command lists the candidates of a pair exactly. Whether two holders state one fact, and whether one has drifted from the other, is the crafter's reading, written at each candidate's coordinate. No row decides a meaning by a grammar rule. |
| **G3** `skills/agent-contract/SKILL.md` rule 6; `routing.md` *Why this way* (read) | No agent files an issue or posts a comment. The crafter drafts each issue whole in its phase record. The orchestrator files the drafts, as `routing.md` and the issue's *Scope* say ("A drift a measurement finds is filed as an issue of its own"). |
| **G4** `skills/agent-contract/SKILL.md` rule 12 | Each pair is a class. A command that lists every instance of what it reads is whole for that reading. A paraphrase ranges over an unbounded domain of spellings, so no command lists every paraphrase, and each row names that part as its open part. A list made by a keyword search is a sample, and its row calls it one. |
| **G5** Issue #1236, its body and both comments (executed: `gh issue view 1236 --json body,comments`, 2026-11-04) | The body's *Scope*, *Done when* and *Rule change* ("None") stand. The first comment (2026-11-01) re-homes #1147's `## Not verified` row on the edition pairs' prose here. The owner's comment (2026-11-03) moves the item to `release: 0.31.1` and replaces the body's *Milestone* paragraph. The body's *Order* is met: #1102 is closed in `release: 0.31.0` (executed: `gh issue view 1102`, closed 2026-11-03). |
| **G6** #1147's records at `48d035aa6` (read: `git show 48d035aa6:seal/threads/1793490088-each-kind-of-restatement-is-measured/<path>`) | `frame/design.md` *Pairs no command of this audit reads* names the 21 pairs, and *The parts* defines P1 to P12. `trail/phases/phase-3.md` *Whether the frame holds*, the item *The parts are not whole*, lists the 11 files in no part, and its *Command parts* lists them. `trail/phases/phase-1.md` and `phase-2.md` *The table* and *Commands* hold each kind's command. Each kind's method this work reuses is cited at those coordinates and is not restated here. |
| **G7** The 11 files at the base (executed: phase 3's *Command parts* at 48d035aa6, run with `94635718e` in place of `bf9efcba`) | It prints the same 11 paths at the base as at `bf9efcba`. |
| **G8** Whether #1147's commands run at the base (executed: `git show 94635718e:tests/text/test_no_passage_is_pasted_into_a_second_file.py \| grep -c -E '^def (words\|windows\|lines)\b'` printed 0; `git cat-file -e 94635718e:docs/the-record-layout.md` exited 128; `git show 94635718e:skills/settle/scripts/passages.py \| grep -n '^def '` printed `in_corpus`, `words` and `windows`) | They do not run unchanged. `audit.py#reader` takes `words` and `windows` from a test module that no longer defines them, since `skills/settle/scripts/passages.py` is now their one home. `audit.py#trees` reads a path that `docs/layout/the-record-layout.md` replaced. So each method is ported into a new probe script, with the normalisation taken from `passages.py`, and the record names each adaptation. |
| **G9** `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*, "A fact of a work item has one record, and every other record cites it by path and heading" (read) | What a phase measures and drafts is "what building one phase found", so it stands in that phase's `trail/phases/phase-N.md`. Each row stands in one phase record only. `gaps.md` and every draft cite a row by path and heading and restate none of its figures. |
| **G10** `docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along*, "A commit that changes nothing a release note states owes the fragment nothing" (read) | The work ships nothing a user installs, so it writes no `changelog.md`. The release range already holds #1317's and #506's fragments (read: `seal/threads/1793750411-rule-text-carries-no-history/changelog.md` and `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/changelog.md`). |
| **G11** The open issues that hold an instance in these pairs (executed: `gh issue view` for 238, 390, 506, 1235, 1319, 2026-11-04) | #238 (`backlog: review chain & agents`) and #390 (`backlog: gates & hooks`) are open and keep their instances, except #390's third item, the test docstring's "eleven", which no longer stands at `94635718e` (`trail/phases/phase-3.md` *Whether the frame holds*). #506's item 1 instance, a test module docstring, left with its module in PR #1333 (executed: `git ls-tree -r --name-only 94635718e tests \| grep orchestrator_act` printed nothing). #506's design hands the docstring enumerations of the other test modules to this item (read: `seal/threads/1793756609-an-enumeration-the-tree-does-not-hold/frame/design.md` *Out of scope*, O2). #1235 repaired #1147's D7 drifts and is closed. #1319 holds facts that two records state, which are pairs inside P7 and outside these 21. |
| **G12** #1317's sweep (read: `seal/threads/1793750411-rule-text-carries-no-history/frame/design.md` *D4 The census*; executed: `git log --oneline` lists `0cb6014d1`, whose subject ends `(#1317) (#1332)`, below the base) | This release removed sentences from `skills/` and `docs/`. An eval grader that quoted a removed sentence now quotes text that no file holds. A passage reader does not list such a quote, so method M2 below also lists each grader quote that stands in no rule file. |
| **G13** `CONTRIBUTING.md` lines 435-437 (read) | The editions "need not be literal translations, but they must tell the same story about what exists". That is the criterion of the edition reading. `tests/behaviour/test_both_editions_carry_the_same_folds.py` holds the outline, so the reading is of what stands under the headings, paragraphs, list items, tables and fenced blocks alike. |
| **G14** `docs/releasing/issues-and-milestones.md` *An issue is titled like a commit*, *A milestone answers when, and takes three shapes* and *An issue is its body and its comments together* (read) | They give a drafted issue's title shape and the grounds for its proposed milestone. The third one makes method M6 read an issue's comments with its body, since a comment can replace a body's paragraph, as the owner's comment on #1236 does. |
| **G15** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read); the unsettled designs' `## Rule changes` (executed: `sed -n '/^## Rule changes/,/^## Removes/p'` over each `seal/threads/*/frame/design.md`) | This work item's subject is its own records, and it changes no rule of the policy root, so `## Rule changes` holds nothing. Two unsettled designs change a section. `1793726048-the-stop-judgment-holds-against-later-rows` changes `docs/running/the-run.md` *The run*, which bounds the review rounds of this run. `1793732301-the-readme-is-written-for-a-first-reader` changes `docs/layout/the-record-layout.md` *The root records*, so that no two rule documents share a 15-word run and no stored count stands. The rest of that section is in force as the base states it, and its table gives `README.md` and `README.ko.md` the question "what the plugin is and how to install it", which E1 is read against. |
| **G16** #1147's run, `48d035aa6:seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md` *Judgments of the run*, the second row (read) | That audit ran four review rounds, and every finding after round 1 was a record restating another record's figure or answering one question twice. This frame takes that row's rules as its own: a count, a command or a decision stands once; every figure carries its commit; the tracker is searched before a draft. |

## Scope

In.

1. **The measured commit.** Every count of the tree is taken at `94635718ea4a79569ac612bcb814114000028be3` (`94635718e`), and R18's count of the tracker, which has no commit, at the moment its reader ran, stated in its row; the tip of `origin/release/v0.31.1` this branch was cut from (executed: `git rev-parse 94635718e origin/release/v0.31.1`, both the same). Each command that counts the tree reads git objects at that commit or a `git archive 94635718e` copy under the phase's scratch directory, and R18's reader reads the tracker through `gh`. This work item's own directory is in no corpus.
2. **One row per pair R1 to R21** of *Data & interfaces*, *The pairs*, measured by the methods that table names. A row holds the columns of *The row*.
3. **One row per file F1 to F11** of *The files*. Each file is read whole for a fact another place states. Each fact found is measured as a pair is, with its other holder named. A file that states no such fact is named as stating none, with the reason.
4. **One row per edition pair E1 to E4** of *The editions*. Both editions are read section by section, and each section's facts are compared. This answers the row the first comment on #1236 re-homes.
5. **The drafts.** Before each draft, the tracker is searched, and the search is written whole. A drift an open issue already holds is named under that issue, and nothing is drafted for it. Every other drift gets a drafted issue in the shape of *A drafted issue*. Drifts with one cause share one draft.
6. **`gaps.md`** from its template. It names what went out unmeasured by citing each row's open part, and names who answers each item.

Out.

- Repairing any drift. The issue says this work repairs none.
- The pairs #1147's kinds K1 to K14 measured. They are not measured again.
- The instances #238 and #390 hold. Each row names them and drafts nothing for them (G11).
- The pairs inside P7 that #1319 measures (G11).
- Committing a measuring script, or adding any check. A decision that a pair needs a check is a drafted issue (G1; plan row A3).
- A changelog fragment (G10).
- A comment on #1236 carrying the tables. The records are what *Done when* asks for (plan row A6).
- Filing the drafts and posting anything: the orchestrator's acts (G3; plan *Operational impact*).
- Any check of the repository's beyond the narrow case the plan's *Phases* names (contract rule 2).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A count repeats | Given a row, when a reader runs its command at `94635718e`, or for R18 against the tracker, as the record writes it, then the command prints the row's count, R18's as of the moment its row states | executed: the proofer runs every row's command |
| S2 A drift can be opened | Given a row whose drifted count is above 0, when a reader opens each instance's coordinates at `94635718e`, or for R18 in the tracker, then the two holders state the fact differently, R18's as of the moment its row states | read: the proofer opens each instance, or a stated sample where a row names more than ten |
| S3 Every item is answered once | Given the phase records, then each label R1 to R21, F1 to F11 and E1 to E4 heads exactly one row, in one phase record, and each row is measured or closed as *The row* defines | executed: for each label, `cat trail/phases/*.md \| grep -c -F '\| <label> \|'` prints 1 |
| S4 A drift has a home | Given a row whose drifted count is above 0, then each instance names an open issue that holds it or a draft id, and each draft has a title, a body and a proposed milestone with its reason | read |
| S5 The tree changes only by the records | Given HEAD, when `git diff --name-only 94635718e..HEAD` runs, then every path it prints is under `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/` | executed |
| S6 The open part is named | Given a row, then it names what its commands cannot see, and a sample is called a sample | read |
| S7 No figure stands twice | Given the records, then each count stands in its row alone, and `gaps.md` and each draft cite the row by path and heading | read: the proofer reads `gaps.md` and each draft against the rows |

## Data & interfaces

### The methods

Each method is a function of a probe script. The first phase writes the script whole in its record's *Command setup*, and a later phase adds its functions in its own *Command setup*, as #1147's phase 2 imported phase 1's, or writes a script of its own where it ports none of #1147's readers. Each script reads a `git archive 94635718e` copy, and R18's reader reads the tracker as `gh` returns it. Its prose normalisation is `skills/settle/scripts/passages.py#words`, `#windows` and `WINDOW`, loaded from that copy.

- **M1 Passages.** Each maximal run of at least `WINDOW` words that a file of one part shares with a file of the other. It ports `runs` and `segments_of_code` from #1147's phase 2 *Command setup* (G6). A prose file is read through `words`. A code file (P8, P9, and a non-`.md` file of P10) is read two ways: as its prose segments, and as its whole text lowercased and stripped as `words` strips, so a heredoc or a string constant that carries a document's text is in reach.
- **M2 Quotes and pins.** In a test, each assert whose test is a literal of at least four words `in` an expression: #1147's `pins` (phase 1 *Command setup*), with the other part as its corpus. In an eval grader or prompt, each backticked or double-quoted span of at least four words. Each one is listed as held where it stands whitespace-folded in the other part. Each grader or prompt quote is also listed as orphaned where it stands in no file of P1, P2, P3 or P5 (G12). An orphan is a drift candidate and is read before it counts.
- **M3 Forms.** Each heading line, table header row and `<!-- -->` marker of a template under `templates/`, against the string constants of P8, the literals of P9 and the text of P10. Listed as held where the other part holds it. A constant or literal shaped as a records heading (a line opening with `#` and a space) or a marker that stands in no template is listed as orphaned. It is read before it counts, since a test may plant a wrong form on purpose.
- **M4 Records-root facts.** The opt-in marker `hooks/lib/optin.py#MARKER` against the first line of `seal/README.md` and of `templates/setup/seal-README.md`. Each `seal/config.md` item name that a P8 string constant or a P3 backticked token holds, against the rows of `seal/config.md` and the items of `templates/setup/config.md`. Each comparison is exact.
- **M5 The tree's state.** #1147's `coordinates`, `lists` and `figures` (phase 2 *Command setup*), with the corpus widened to the part the row names. A `figures` list is a keyword candidate list, read by a stated sample. Its class stays the `seal/follow-up.md` row on a figure about a corpus stated with no moment. For R19 it adds the docstring enumeration: each backticked `test_*` or `#name` that a docstring or comment under `tests/` names, against the functions the tree holds, read from the modules' AST.
- **M6 The tracker.** The open issues with their bodies and comments, and the open milestones with their descriptions, read through `gh`. Each backticked milestone title an open issue states is compared with the milestone it stands in. Each `#N` a milestone description names is compared with the issue's milestone. Each difference is read against the issue's comments before it counts (G14).
- **M7 Reading whole.** The files are read whole, and every fact one states that another place states is listed with both coordinates.

**The unit counted.** A passage is one maximal run, whatever the number of its holders. A fact-anchored unit is one quote, pin, heading, marker, item name, coordinate, list, figure, milestone statement, or, for an edition pair, a block of a section: a paragraph, a list item, a table row or a fenced block, read against its counterpart in the other edition. *Held twice* counts units. *Drifted* counts units whose holders state the fact differently at `94635718e`, or for R18 at the moment its row states, judged by reading. A comparison that is exact, such as a list against its source, counts a difference as drifted without a reading.

### The pairs

The pairs are #1147's *Pairs no command of this audit reads*, in its order. What can stand in both parts is that table's second column. Where a row of that table names a kind, its reader or its mechanism, the method below is that kind's, widened to the pair.

| Label | Pair | Methods |
|---|---|---|
| R1 | P1 with P10 | M1; M2 over graders and prompts, with the orphans (K5's method widened) |
| R2 | P3 with P6 | M1; M4, the item names `agents/` holds |
| R3 | P4 with P4 | M1; each line of three words or more that two templates hold, whitespace-folded |
| R4 | P4 with P8 | M3 |
| R5 | P4 with P9 | M3; M2 with templates as the corpus (K6's mechanism widened) |
| R6 | P4 with P10 | M1; M3 |
| R7 | P5 with P6 | M1; the `seal/` layout tree each file draws (K3's `trees`, ported, reading `docs/layout/the-record-layout.md`) |
| R8 | P5 with P8 | M1 |
| R9 | P5 with P9 | M1; M2 with P5 as the corpus (K3's mechanism, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, read for what it holds) |
| R10 | P5 with P10 | M1; M2 |
| R11 | P6 with P6 | M7 over the three files; M1 |
| R12 | P6 with P8 | M4; M1 |
| R13 | P6 with P9 | M1; M2 with P6 as the corpus |
| R14 | P6 with P10 | M1 |
| R15 | P8 with P9 | M2 with P8's string constants as the corpus; M1 between test docstrings and comments and P8's prose segments |
| R16 | P8 with P10 | M1 over whole text (K12's method widened), leaving out the cases a script under `evals/scripts/` writes, which K12's *Command regenerate* compares |
| R17 | P9 with P10 | M1 |
| R18 | P11 with P11 | M6 |
| R19 | P12 with P9 | M5 over `tests/`, with the docstring enumeration (G11) |
| R20 | P12 with P8, its lists and figures | M5's `lists` and `figures` over P8's prose segments |
| R21 | P12 with P10 | M5's `coordinates` and `figures` over `evals/behaviour/` |

### The files

The files G7 lists, each read whole by M7. Each row names the facts it is read for first. The reading is not limited to them.

| Label | File | Read first for |
|---|---|---|
| F1 | `.claude-plugin/marketplace.json` | name, description and version, against `plugin.json` and the README editions; `.github/scripts/plugin_directory_check.py` reads `plugin.json`'s name and the `marketplace.json` of the two outside catalogs, never this repository's, and the row names what it compares |
| F2 | `.claude-plugin/plugin.json` | the same, and the icon `.github/scripts/release_seal.py` reads |
| F3 | `.gitattributes` | a rule a document states about line endings or diffs |
| F4 | `.github/ISSUE_TEMPLATE/config.yml` | where an issue is opened, against `SECURITY.md` and `CONTRIBUTING.md` |
| F5 | `.github/ISSUE_TEMPLATE/gate-misfired.md` | the form, against what `CONTRIBUTING.md` and `docs/` say a misfire report holds |
| F6 | `.github/PULL_REQUEST_TEMPLATE.md` | the form, against `skills/commit-pr-convention/SKILL.md` and `CONTRIBUTING.md` *What a change to a gate must carry* |
| F7 | `.gitignore` | a path a document says is ignored, or is committed |
| F8 | `.test_durations` | its case ids against the suite's functions, read from the modules' AST and not by running the suite; `pytest-split` and `test_the_durations_file_prices_the_suite` read the file (`tests/conftest.py` records collected ids and gives `posix_id`), and the row names what each reader does with an id that names no case |
| F9 | `LICENSE` | the license name, against the manifests, the README editions and `TRADEMARKS.md` |
| F10 | `assets/seals/README.md` | the seal art's facts, against `.github/scripts/release_seal.py`'s docstring and the README editions |
| F11 | `ruff.toml` | each rule a document states about the lint, such as the `seal/follow-up.md` row on comment width, which says `E501` is not selected |

### The editions

| Label | English | Korean |
|---|---|---|
| E1 | `README.md` | `README.ko.md` |
| E2 | `docs/layout/one-root-by-lifetime.md` | `docs/layout/one-root-by-lifetime.ko.md` |
| E3 | `docs/experiments/README.md` | `docs/experiments/README.ko.md` |
| E4 | `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` | `docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.ko.md` |

The list is whole: `git ls-files -- '*.ko.md'` prints these four Korean editions (executed). Each pair is read whole, section by section, so the reading is whole and is not a sample. A section's fact is a claim about what exists or what happens. A difference in wording that states the same fact is no drift (G13).

### The row

Each phase record's table has these columns:

| Label | Command | Held twice | Drifted | Open part | Home |
|---|---|---|---|---|---|

The *Command* cell cites the fenced block by its heading in the same record, since a table cell cannot hold a block. *Held twice* and *Drifted* carry their commit, or for R18 the moment the tracker was read. *Open part* names what the commands cannot see. *Home* holds, for each drifted instance, the open issue that holds it or a draft id `D<n>`, or `none`. Each instance stands under the record's *Instances <label>* heading with its coordinates.

A row is **closed** in place of measured only where its commands cannot run in the phase's environment. Its *Command* cell then cites the tracker search and the round-record search that show no drift there, each written whole: `gh issue list --state all --search <words>` and `git grep <pattern> <tag> -- seal/` at the release tags. A keyword search is a sample, and the row calls it one. The record names why the commands could not run.

### A drafted issue

Under its draft id, in the phase record whose row found the drift: the title in the shape G14 names; the body, with the measure, cited by the record's path and heading and the commit `94635718e`, or for R18 the moment its row states, the scope and a *Done when*; the proposed milestone, with one sentence of why it fits against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*; and the labels of the rows it answers. A draft proposes a `backlog:` milestone by its area (`frame/questions.md` Q1).

## Rule changes

- nothing
  why: The work measures the pairs and drafts an issue for each drift, as #1147 did. A decision that changes a rule is filed as its own issue, and that issue's design states the rule change.

## Removes

- nothing
  why: The work adds this work item's records and nothing else, and it adds no mechanism. What a drafted issue takes out of the tree is named in that issue, and its own design names it in its `## Removes`.

Framed 2026-11-04 by framer, before the build.
