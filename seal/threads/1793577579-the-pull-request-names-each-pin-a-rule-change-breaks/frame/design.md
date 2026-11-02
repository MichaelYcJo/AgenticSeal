# Design: the pull request names each pin a rule change breaks (#1216)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1. Issue #1216 (executed: `gh issue view 1216 --json title,milestone,comments`, milestone `release: 0.28.0`, 0 comments; the body as the spawn folded it) | The scope and *Done when*. At the pull request or in the settle's dry run, each `change` or `remove` whose `from` a file under `tests/` holds names that file and line. Each `to` sharing a 15-word run with another shipped file names the pair, by the reader `tests/text/test_no_passage_is_pasted_into_a_second_file.py` uses. The report is a notice and refuses nothing, and whether a named pin follows the `to` is the reader's judgment. |
| G2. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | Why a pin meets its `from` only at the settle: a pull request does not edit the policy root, and the settle writes each section after the release. The policy in force at a section is the baseline plus the pending designs' operations on it in merge order. |
| G3. The pending operations on the two sections this design changes (executed: `rule_changes.parse` over every `frame/design.md` under `seal/threads/` at `96f424ec`, in a scratch clone) | Only #1215's design (`seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/`) names `docs/the-review-record.md` *What the check reads at the pull request* or `docs/what-a-script-gates.md` *The checks*. Its `add` lands first in the first section, and its two `change` values are the text this design's `from` values quote in the second. Every pending design parses with no error. |
| G4. `docs/the-review-record.md` *What the check reads at the pull request* (read), with #1215's pending `add` | The home of what `chain-check` reads of a design. Its first paragraph lists every input of the check in bold, so a new input changes that sentence (contract rule 19). |
| G5. `docs/what-a-script-gates.md` *The checks*, the row of `skills/code-review/scripts/chain_check.py` (read), with #1215's two pending `change` values | The row's *Reads*, *Unread* and *Agent* cells state what the check reads, what it names and refuses for nothing, and which party judges the meaning. Each cell changes. |
| G6. `skills/code-review/scripts/chain_check.py#rule_changes_read`, `#check_lines_in`, `#rule_changes_of`, `#tracked_files`, `#read_record`, `RULE_CHANGES_UNREAD`, and `#main`'s notice loop (read) | The arm this work extends. It parses each judged or edited design once and sends notices to a list that `main` prints as `path:line  message`, a notice annotation in CI, changing no exit code. The design is read from HEAD, or from disk under `--worktree`. `rules.py`, loaded by #1215, resolves targets in the working tree. |
| G7. `skills/settle/scripts/rule_changes.py#Op`, `#value_lines`, `#section_lines`, `#pattern` (read) | `Op.lines` maps each field to `[(design line, text)]`, so a notice is placed at the first line of a `from` or a `to` with no offset computed back (#1215 design G13 names #1216 as its reader). `section_lines` gives the span a `remove` with no `from` takes out. |
| G8. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` (read whole) and `tests/text/test_a_moved_rule_leaves_its_definition.py`, its docstring and `WINDOW` at `:85` (read) | The reader the issue names. The corpus is every tracked `*.md` under `docs/`, `skills/`, `agents/` and `templates/`, with `CLAUDE.md`, `CONTRIBUTING.md` and `README.md`, and no `*.ko.md`. A file is normalised by `words`: fences and heading lines dropped, a quoted section name made one token, the text lowercased and stripped of five marks. Runs of `WINDOW` words are compared. `WINDOW = 15` is imported from the moved-rule module, whose docstring holds the measurement that chose it. A shipped script cannot import a test module, so the reader has to move for `chain-check` to use it. |
| G9. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, the registry entry `tests/text/test_no_passage_is_pasted_into_a_second_file.py#corpus` at `:84` (read) | The paste test's `corpus` is a registered path lister with its own guard against files listed and not on disk. Keeping the listing in the test, and moving only the selection rule and the normalisation, leaves that registry true. |
| G10. The record, replayed (executed: a `test_tmp_probe.py` run with `python3 -I` from the scratch directory against `rule_changes.py` of a `git clone --no-local` at `96f424ec`, over the tree of `a92c358b^` taken by `git archive`; since removed) | Over the eleven designs the 0.27.1 settle read, 94 operations: string literals of four words or more under `tests/`, docstrings left out, standing whitespace-collapsed in a `from` and not in its `to`, name 26 pins at 26 literal sites. 13 of them are every literal the settle repointed in its 11 failing cases (executed: each literal's count in its module at `a92c358b^` against `a92c358b`, and the settle's hunks of `git show a92c358b -- tests/` read for any it missed). The 13 others did not fail: fixture strings of `tests/skills/test_chain_check.py` and `tests/skills/test_pact_check.py`, two absence asserts (`not in`), and a phrase such as `before the first edit` that the test reads in another file. At three words the same run names 44 and finds no more of the 13. The copy half names 5 pairs from 5 `to` values: the four copies the settle reworded (`gh pr view 1214`, its row "four copies", read), one of them added by two designs. |
| G11. The other settle (executed: the same probe over `14bfd9921^`, the tree the 0.27.x settle #1269 started from) | 10 operations, no pin and no copy named. The settle's body names no failing pin of a `from` (`gh pr view 1269`, read: its two first-run failures were an old-root path a census refuses). |
| G12. The pins #1278 kept (executed: `git grep -F` at HEAD for the settle's repointed texts) | Four of the 13 repointed literals still stand, each now under a comment naming the fact it pins: `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:188`, `tests/text/test_review_axes.py:116`, `tests/text/test_the_record_is_written_in_words.py:113`, `tests/text/test_the_rules_have_one_owner.py:101`. A rewording of those four sentences turns them red at the next settle as it did at 0.27.1. |
| G13. The pending designs, read forward (executed: the probe over the scratch clone at `96f424ec`) | 14 operations, 4 pins named and no copy. All 4 are one citation of `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* in two modules, under the two editions of `docs/one-root-by-lifetime.md`. Neither module reads that document: `tests/behaviour/test_waiver_decided_at_start.py:594` reads `agents/framer.md`, and `tests/text/test_settle_reads_before_it_removes.py:121` reads `agents/framer.md` and the two READMEs (read). So the 0.28.0 settle meets no rule-change pin, and the four would be noise. |
| G14. The cost (executed: the probe's timings) | Reading every `tests/**/*.py` through `ast` took 0.65 s in one run and 1.38 s in another, for 154 files and 7,210 literals of four words or more. Normalising the corpus took 0.07 s to 0.14 s, and matching 94 operations took 0.21 s. |
| G15. `agents/proofer.md` *Order of work* step 7 (read) | The proofer runs `chain_check.py --worktree` before handing back each round record and corrects what it refuses in its record. Nothing tells it to read a notice about the design, so a notice with no reader there catches nothing. |
| G16. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read); `CONTRIBUTING.md` *What a change to a gate must carry* (read) | A reading guessed from words is reported, never used to block, so both halves are notices. The change names the form it reads, what it names as not read, and the party that judges the same text, and it states what it removes or why nothing can go (*Removes*). |
| G17. `ruff.toml` `[per-file-target-version]` (read); `tests/hooks/test_launch.py:208-231` (read); `CONTRIBUTING.md` *The test layout* (read); the orchestrator's finding on #1215's broad run (not opened by the framer) | A module `chain_check.py` loads, directly or through `rule_changes.py`, is linted at the `py39` floor and listed there, and the launch test holds the list. A new shipped module takes one test file with one class per public function. The orchestrator reports that #1215's broad run failed once on both points, so the phase's *Verified by* names both checks. |
| G18. Contract rules 12, 14, 15 and 19 | A notice is text a person reads and is pinned in the commit that adds it. Each new case is seen red first. Every sentence stating what `chain-check` reads of a design is found by a stated method and corrected. The class of pins the reader cannot list is unbounded in its spellings, and *Scope* Out says so. |
| G19. `routing.md` (read) | `Planning` `framer`, `Implementation` `crafter`, `Automation` `yes`: nobody is asked during the run. |
| G20. `seal/follow-up.md` (read); the latest release's `### Process changes` (executed: `gh release view`) | No follow-up row has this work as its prerequisite. No process row bears on this frame. |

The earlier decisions this frame stands on, each with its coordinate. E1 to E5 are built on. E6 is departed from in one point, with the grounds in its row.

| Earlier decision | What this frame takes from it |
|---|---|
| E1. #1214, the 0.27.1 settle (merged at `a92c358b`), whose body found eleven pins and four copies by running the suite and names #1216 (executed: `gh pr view 1214`) | Built on. Its record is the catch this mechanism is weighed against (G10), and its step 8 broad run stays as the one run that reads every check. |
| E2. #1233, merged as #1278: `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md` *Scope* Out, its first item, and G11; its `changelog.md` (read) | Built on. #1278 kept 107 asserts on rule text that pin a fact and handed the pins it did not list to "#1216 at the next pull request whose design breaks one, and the proofer at review". Its *The criterion* is what the proofer applies to a named pin: wording leaves, a fact stays for the settle to repoint. Without this work that handoff has no receiver. |
| E3. #1167, `v0.27.0:seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` *Scope* items 5 and 8 (executed: `git show`), and `skills/core/SKILL.md` *The rule a mechanism is kept against* | Built on. A reading guessed from words is a notice that changes no exit code, and a file the reader cannot read is named as not read. |
| E4. #1263, merged as #1276: `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/changelog.md` (read) | Built on in shape. A band flags a row and a judgment decides it. Here the reader flags a pin or a copy, and the proofer decides whether it is a finding. |
| E5. #1215, merged as #1282 at `8d39d6f80`: its design *Scope* items 1 and 3 and G13 (read) | Built on. `Op.lines` places each notice, and the notices join the list the rule-changes arm already fills. Nothing of #1215's refusal changes. |
| E6. #730's paste check and #107's `WINDOW`, homed in `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/text/test_a_moved_rule_leaves_its_definition.py` (read) | Built on for the method, the corpus and the window. Departed from in where the reader stands: the normalisation, the selection rule and `WINDOW` move to a shipped module that both tests import. The grounds: the issue asks for the reader the paste test uses, and a shipped script cannot import a test module. A second copy of the method in shipped code would be two readers of one form. Both docstrings keep their method and their measurement and cite the module for the code. |

## Scope

In:

1. **`skills/settle/scripts/passages.py` holds the paste check's reader.** It holds `WINDOW`, `in_corpus(rel)` (the selection rule of G8 as a predicate on a repository path), `words(text)` and `windows(words)`, moved as they stand. A comment on `WINDOW` cites `tests/text/test_a_moved_rule_leaves_its_definition.py` for the measurement. It reads no file and runs no command, so each caller lists and reads its own files.
2. **Both test modules use it.** `tests/text/test_no_passage_is_pasted_into_a_second_file.py` imports the module and keeps `corpus`, `shared_counts`, `longest_run`, `over_baseline`, `BASELINE` and the cases that read the tree or plant a paste. Its `corpus` keeps its listing and guard and selects with `in_corpus` (G9). `tests/text/test_a_moved_rule_leaves_its_definition.py` imports `WINDOW` from the module and keeps its own normalisation and its measurement case. The cases that test `words` alone, `test_a_wrapped_section_name_is_one_token` and `test_fences_and_headings_are_not_read_and_case_and_backticks_are_not_words`, move to the new test file `tests/skills/test_passages.py`, which follows `CONTRIBUTING.md` *The test layout*. What the paste test asserts of the tree is unchanged.
3. **`rule_changes.py` reads what an operation takes out and what its `to` repeats.** Three functions, each over text it is handed. `literals(source)` returns `[(line, text)]` for each string constant of one Python source that `ast` reads and that is no docstring, with whitespace runs collapsed, of at least four words; implicit concatenation is joined by the parser. A source that does not parse is the caller's to name. `pins(op, taken, found)` returns the literals of `found` that stand in `taken` and not in the operation's `to`, both whitespace-collapsed, where `taken` is the `from`, or for a `remove` with no `from` the section's text as `section_lines` spans it in the document. `copies(op, texts)` returns, for an `add` or `change` whose `file` `in_corpus` admits, each corpus path other than `file` whose `windows(words(...))` share at least one run with the `to`'s, with the count and one run. It loads `passages.py` by path, as it loads `unverified_check.py`.
4. **`chain_check.py`'s rule-changes arm prints each pin and copy as a notice.** For each design `rule_changes_read` parses with operations, the arm lists the tracked `*.py` files under `tests/` and the tracked corpus files once per run, reads them from the working tree, and prints each pin at the first line of the `from` in the design, or at the operation's line for a `remove` with no `from`, and each copy at the first line of the `to`. A pin's message names the test file, its line and the literal. A copy's message names the corpus file, the count of shared runs of `WINDOW` words and one run. A test file that does not parse or decode is a notice `not read: <why>` at line 0 and is read for nothing. No message carries a tag before it, and no exit code changes. The module docstring's *rule changes* arm and its paragraph on notices say what the arm now reads.
5. **Cases pin the arm at each edge.** One class in `tests/skills/test_chain_check.py` carries the marker `a-rule-change-names-the-pins-and-copies-it-breaks`, which the rule change below names, with these cases. A `change` whose `from` holds a four-word literal of a planted test and whose `to` drops it prints one notice at the `from`'s line naming the test's path and line, and the ready pull request exits 0. A `to` that keeps the literal prints none. A three-word literal and a docstring print none. A `remove` with no `from` names a literal standing in the section it takes out. A `to` sharing one 15-word run with a planted `skills/` file prints one notice naming that file; a 14-word run prints none; a `to` landing in a `*.ko.md` file prints none. A test file that does not parse is named as not read, and the exit code is unchanged. `tests/skills/test_rule_changes.py` gains a class per new function with its accepting and refusing cases. Each case is seen red before it is planted (contract rule 15), against the base or under a named mutation, and the phase record says which.
6. **The proofer reads the notices.** `agents/proofer.md` *Order of work* step 7 gains one sentence. Each notice its `chain_check.py` run prints at a line of a work item's `frame/design.md`, naming a test pin or a copy, is the proofer's to weigh. A named pin that holds a rule's wording, by `docs/what-a-script-gates.md` *The checks*, is a finding. So is a `to` that repeats a passage another file keeps after the settle. A named pin of a fact a reader acts on is no finding, since the settle repoints it. A finding taken from such a notice quotes the notice, so the settle can count what the notices caught.
7. **Every sentence that states what the check reads of a design says it.** The method is `git grep -n -e 'rule_changes' -e 'Rule changes' -e 'chain-check' -e 'chain_check' -- ':!seal/threads' ':!tests' ':!docs'`, run at the build's HEAD and read line by line, as #1215 *Scope* item 5 ran it. A sentence of `docs/` is changed only through `## Rule changes` below. A sentence elsewhere stating what `chain-check` reads of a design is corrected, or named in the phase record as still true.
8. **The lint floor.** `ruff.toml` `[per-file-target-version]` lists `skills/settle/scripts/passages.py` at `py39` (G17).
9. **The changelog fragment.** The work item's `changelog.md`, with a `### Process changes` table, since the diff changes `agents/proofer.md` (`docs/the-record-layout.md` *A change to the way of working writes its process row in its own fragment*).

Out:

- **The settle's dry run.** The issue allows either moment, and this work takes the pull request (`plan.md` *Alternatives considered*, rows 2 and 3). `skills/settle/scripts/settle.py` and `skills/settle/SKILL.md` are #1217's next, and the settle's step 8 broad run stays the one run that reads every check.
- **A pin the reader cannot list**: a literal built at run time, a comparison case folded or by a pattern, a check line that names its own module, an absence assert that an `add` breaks, and a test outside `tests/` or in another language. The class is unbounded in its spellings (contract rule 12), and each meets the suite at the settle's broad run as now.
- **A `to` sharing a run with another pending design's `to`.** Neither is in the tree until the settle writes both.
- **Repointing or removing a pin in this change.** The work names pins. The proofer judges each named one, and the settle repoints a fact.
- **Running the suite over a draft of the policy root at the pull request.** That is #1217's draft and the orchestrator's one broad run (contract rule 2).
- **`.claude-plugin/plugin.json`.** #1215 moved it to `0.28.0`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A `from` a test pins | Given a ready pull request whose design has a `change` whose `from` holds the literal of a planted test's assert and whose `to` drops it, when `chain-check` runs, then it exits 0 and prints one notice at the `from`'s first line naming the test's path, line and literal | The *Scope* item 5 case, seen red against the base, where nothing is printed for the design. |
| S2. A literal the `to` keeps | Given the same design with the literal in the `to` too, when `chain-check` runs, then it prints nothing for the design | The *Scope* item 5 case. |
| S3. A section removed whole | Given a `remove` with no `from` whose section, as the working tree holds it, holds a planted literal, when `chain-check` runs, then the notice stands at the operation's line | The *Scope* item 5 case. |
| S4. A `to` that repeats a passage | Given a `to` sharing one run of 15 words with a planted `skills/` file, when `chain-check` runs, then one notice at the `to`'s first line names that file and one run; with 14 shared words, nothing | The *Scope* item 5 case on both sides of `WINDOW`. |
| S5. What is not read | Given a three-word literal, a docstring holding the `from`, a `to` landing in a `*.ko.md` file, and a test file that does not parse, when `chain-check` runs, then the first three print nothing, the fourth is named as not read, and the exit code is the one the other arms give | The *Scope* item 5 cases. |
| S6. The paste test is unchanged in what it asserts | Given HEAD after the build, when `tests/text/test_no_passage_is_pasted_into_a_second_file.py` runs, then it passes with `BASELINE` untouched, and its planted pastes are named as before | The phase's narrow run, executed by the crafter. |
| S7. The record replays | Given the tree of `a92c358b^` in a scratch directory, when the built `rule_changes.py` functions run over its eleven designs, then each of the 13 repointed literals G10 lists is among the pins named, and the four copies among the pairs | Executed by the crafter in a scratch directory and recorded in the phase record, then removed (contract rule 7). |
| S8. This design passes its own read | Given this work item's pull request, when `chain-check` runs from the tree it builds, then this design's operations print no pin and no copy, and the marker `a-rule-change-names-the-pins-and-copies-it-breaks` is carried by the *Scope* item 5 class | The pull request's `hygiene` run. At the base the framer's probe parsed this section with no error or unread line, named no pin and no copy for its five operations, and found each `from` once: two in the sections as they stand, two in #1215's `to` values (executed). Until the class exists, #1215's arm refuses the `add`'s check line because no test carries the marker, as #1215's own S8 met. |

## Data & interfaces

- `skills/settle/scripts/passages.py` (new): `WINDOW`, `in_corpus(rel)`, `words(text)`, `windows(words)`. No I/O.
- `skills/settle/scripts/rule_changes.py`: `literals(source)`, `pins(op, taken, found)`, `copies(op, texts)`, and a module constant for the four-word floor. `Op`, `parse` and every existing function are unchanged.
- `skills/code-review/scripts/chain_check.py`: two message constants beside `CHECK_LINE_SAYS`, one for a pin and one for a copy, and the composition that lists and reads the files once per run. Exit codes and arguments are unchanged.
- `ruff.toml`: one `per-file-target-version` row.
- No new dependency, environment variable or configuration row.

## Rule changes

- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **For each operation of a design whose `## Rule changes` the check
    parses, the check names the test pins and the copies the settle will
    make, each as a notice at the operation's line in the design, and
    refuses nothing for them.** A pin is a string constant of at least four
    words in a Python file under `tests/`, read through `ast` with its
    docstrings left out, that a `from` holds, or the section a `remove`
    with no `from` takes out, and that the `to` does not hold. A copy is a
    run of 15 words a `to` shares with another rule document, read as
    `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads one,
    through `skills/settle/scripts/passages.py`. A design's operations
    reach the policy root only at the settle, so without the notice a pin
    and a copy meet the suite first there, after the pull request that
    could answer them has merged. The proofer weighs each notice at review.
    A pin of a rule's wording and a copy another file keeps after the
    settle are findings, and the settle repoints a pin of a fact. A
    source the reading cannot read, a test file, a rule document, a
    section a `remove` names or a file listing, is named as not read. A pin the reader cannot list, such as a literal built at
    run time, meets the suite at the settle's broad run.
    check: a-rule-change-names-the-pins-and-copies-it-breaks
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: the migration config's `Baseline commit`, and nothing else of a round record.**
  to: the migration config's `Baseline commit`, and, against a design's operations, the string constants of the test files under `tests/` and the rule documents, and nothing else of a round record.**
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: and the `check:` lines of its `add` and `change` `to` values through `.github/scripts/rules.py`;
  to: and the `check:` lines of its `add` and `change` `to` values through `.github/scripts/rules.py`; against each operation, the string constants under `tests/` through `ast` and the rule documents through `skills/settle/scripts/passages.py`;
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: and each line of a `to` that opens like a `check:` line and is not one;
  to: each line of a `to` that opens like a `check:` line and is not one, and each source it cannot read, a test file, a rule document, a section a `remove` names or a file listing; names each test pin a `from` takes out and each run a `to` shares with another rule document, refusing neither;
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: what a named unread line meant: the orchestrator at the preflight
  to: what a named unread line meant: the orchestrator at the preflight; whether a named pin or copy is a finding: the proofer at review

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the paste check's normalisation and selection rule: `lines`, `words`, `windows`, `FENCE`, `HEADING`, `SECTION`, `SECTION_TOKEN`, `STRIP`, `TOP_FILES`, `TOP_DIRS` | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` | `skills/settle/scripts/passages.py`, which the test imports (*Scope* items 1 and 2) |
| the constant `WINDOW = 15` | `tests/text/test_a_moved_rule_leaves_its_definition.py:85` | `skills/settle/scripts/passages.py#WINDOW`, which the module imports; its measurement stays in its docstring and `#test_the_window_sits_between_what_was_measured` |
| two cases that test `words` alone | `tests/text/test_no_passage_is_pasted_into_a_second_file.py#test_a_wrapped_section_name_is_one_token` and `#test_fences_and_headings_are_not_read_and_case_and_backticks_are_not_words` | `tests/skills/test_passages.py`, the test file of the module that now holds `words` (*Scope* item 2) |

Nothing is removed in return for the notice, and the reason is this. The mechanism adds one reading to `chain-check`'s rule-changes arm. On the record it would have named all 13 literals the 0.27.1 settle repointed and the four copies it reworded, beside 13 pins that did not fail (G10), and nothing at the 0.27.x settle, where nothing failed (G11). Four of the 13 literals still stand as facts #1278 kept (G12), and #1278 handed the pins it did not list to this work (E2). The 0.28.0 settle meets none, and the reading would print 4 notices of noise for one design (G13). Its cost is about one second per `chain-check` run that judges a design with operations (G14), two notice messages, and one sentence the proofer reads. The one candidate to go is the settle's step 8 broad run, and it stays: it is the one run that reads every check, and it alone meets the pins the reader cannot list (*Scope* Out). The move of the paste reader removes no reader: one reader moves so that two callers share it.

Framed 2026-11-02 by framer, before the build.
