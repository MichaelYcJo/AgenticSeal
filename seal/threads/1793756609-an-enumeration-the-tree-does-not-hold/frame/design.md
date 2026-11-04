# Design: the orchestrator's acts table goes, with the test that holds it (#506)

Issue #506, the second item of milestone `release: 0.31.1`. The framer read
the body and its one comment with `gh issue view 506 --json body,comments`
on 2026-11-04 (executed). The body names three places where an enumeration
is not held in step with the tree. The owner's comment of 2026-11-03 moves
the judgment of "whether the table and its enumeration stay" into this
release. Every coordinate below is at acf37c448, which differs from
0cb6014d1 only by this work item's `routing.md` (`git diff --stat`,
executed).

The body's paths are from an older tree. At HEAD the module is
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, the
table is `skills/implement/acts.md` *Orchestrator: which of these acts runs
itself*, and the act outside the table lives in
`skills/verify/orchestration.md` *Measure the segment, and feed the flow log*
(read, located with `git grep`, executed).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A mechanism stays only while its record of what it caught outweighs what it costs." "Nothing is kept beside the tree to stay in step with it." "When fixes chase one mechanism's edge cases, ask what it decides." The table is an enumeration kept beside the headings, and #506's three items are three edge cases of it. This clause decides the work (D1) |
| `routing.md` *Why this way* (read) | "The owner ... left #506's choice of repair to this work item's framer." The orchestrator's spawn adds that the owner's answer of 2026-11-04 includes removing the table and its enumeration altogether (the orchestrator's finding; the framer did not open that answer) |
| Issue #506, the owner's comment of 2026-11-03 (executed: `gh issue view`) | "Whether the table and its enumeration stay is judged there", in release 0.31.1, after #1317 |
| What the test can report (read: `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py#findings`, `#_delivery` and `#rows`, every message string) | The module has eleven finding messages. Each one names a row of the table, a heading's relation to the table, or the table's own absence. None names a defect in an orchestrator act or in its delivery. So every defect the test can catch is a defect in the table itself (D1) |
| The record of what the table cost (read: the four records in the next cell) | `1793688270-a-check-line-names-a-case-or-the-rule-carries-none/trail/rounds/round-1.md` finding 2: a review round spent a `should` on a stale `Grounds` cell. `1793726048-the-stop-judgment-holds-against-later-rows/trail/phases/phase-1.md`: the phase re-read `acts.md:76` to show it stayed true. `1793661729-each-document-is-cut-by-who-opens-it/trail/phases/phase-4.md`: three headings took the marker and `acts.md` took three rows because the table's rule asked for them. `1793732301-the-readme-is-written-for-a-first-reader/trail/phases/phase-2.md`: `README.md` shared a passage with `acts.md` |
| The record of what the table caught (executed: `gh issue list --state all --search` for `'"still a sentence" in:body'`, `'"acts.md"'` and `'"which of these acts"'`) | Since the table shipped in 9647894f2 (v0.13.1), the `"acts.md"` search returns #506, #1102, #1189 and #1231, the search for the section's heading, `"which of these acts"`, returns #506, #1046, #1109, #1148 and #1163, and the `"still a sentence" in:body` search returns #506 alone (each run by the orchestrator on 2026-11-04 with `gh issue list --state all --limit 50 --search`). Each is about the table's limits, a defect in one of its rows, what reading it cost, a census pair or a run's measurement; no issue took its subject from a `still a sentence` row. These searches match a few phrases, so they are a sample |
| `skills/core/SKILL.md` *A judgment stands on a source document* and #330's own grounds, as #506 *What is not here* quotes them (read) | "Only an act with a measured miss gets a mechanism." A miss is measured from a run's records and its flow-log reading, not from the table. So the table supplies no input to the one decision it was kept for |
| Homes of the facts the `Grounds` cells state (read: a sample of three) | `docs/running/what-a-script-gates.md` tables `hooks/question-gate.py`'s reach. `docs/checks/the-session-hooks.md` states that `implementer-notice` prints and blocks nothing. `docs/running/measuring-a-run.md:119` states that the posting command does not make anybody run it. A `Grounds` cell restates its hook's home. This is a sample, and the cells' text stays readable at `git show v0.31.0:skills/implement/acts.md` (executed: `git cat-file -e`) |
| `docs/running/the-agent-set.md` *What a spawn costs* (read) | The rule "The orchestrator's acts are counted, each against what delivers it" is a bold paragraph inside the section, at `:150-162`, with a check line naming the test. The section's other rules do not refer to it |
| `skills/settle/rule-changes.md` *A rule has one shape* (read) | "A check line is refused at its line for ... a path that is no file of the repository." Only a pending `remove` with no `from` excuses a refused line, and it takes a whole section. So deleting the test with a `## Rule changes` operation would leave `docs/running/the-agent-set.md:162` and `docs/layout/the-pact.md:68` refused at HEAD |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A work item whose subject is the policy root's text edits it directly in its pull request. This item's subject is one rule of `docs/` and the mechanism under it, and the two check lines cannot wait for the settle. So it edits `docs/` directly and `## Rule changes` holds the no-change block. 1793688270 and 1793750411 judged the same way for their `docs/` text (read: their `## Rule changes`) |
| Unsettled `## Rule changes` (executed: `awk` over every `frame/design.md` under `seal/threads/`, the `file:` and `section:` lines) | Two designs hold pending operations. They name `docs/running/the-run.md` *The run* and `docs/layout/the-record-layout.md` *The root records*. This work touches neither, and it moves no section, so it re-points nothing |
| `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` module docstring, and `docs/running/the-agent-set.md` *What a spawn costs* (read) | The `Orchestrator:` marker keeps a section out of every agent's payload, and that test holds it. With the table gone the marker has this one meaning left, which settles #506 item 2's "the marker carries two meanings" without a split (D2) |
| `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* (read) | The diff changes `skills/implement/orchestration.md` and `skills/code-review/orchestration.md`, so `changelog.md` ends with a `### Process changes` table. The phase's spawn hands its crafter the rows with the fragment |
| `docs/releasing/branch-and-release.md` *Cutting a release*, through #1317's grounding (read: `1793750411-rule-text-carries-no-history/frame/design.md`), and `.claude-plugin/plugin.json` (executed: `grep version`) | The version moves in the first work item of a release. It reads `0.31.1` already, so this work item leaves it |
| `1793750411-rule-text-carries-no-history/frame/design.md` *Scope* O2 and its phase records (read) | #1317 left `acts.md` and both sides of each census pair it belongs to for this item. The other sides in `skills/implement/orchestration.md` are heading citations, "Orchestrator: what needs a person…" and "a work item that commits in more than one repository". They name the sections they cite and stay. Deleting `acts.md` ends each pair |
| `seal/follow-up.md` (read) | No row waits on this work |
| Docstring enumerations of cases across `tests/` (executed: an `ast` probe over `git ls-files 'tests/*.py' 'tests/**/*.py'`, run once from the scratch directory and deleted) | 14 of 156 test modules name a `test_` case in backticks in their module docstring. Every name resolves: four are module file names and one is a case in `tests/behaviour/test_release_hygiene.py`, checked by hand. So #506 item 1 has no live instance outside the module this work deletes. The probe reads backticked names only, so it is a sample of the class |

## Scope

### D1 The table, its test and the rule that states them go

The judgment, against `skills/core/SKILL.md` *The rule a mechanism is kept
against*: the table and its test catch only their own drift, and they cost a
row for every marked heading, a review finding, re-reading in later phases,
and three open edge cases that #506 says would each need more mechanism. The
decision the table was kept for, which act to arm next, is made from a
measured miss, and the table supplies none. So the table goes with
everything that stood on it, and nothing replaces it.

In scope, each a row of `## Removes`:

1. `skills/implement/acts.md`, the whole file.
2. `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, the
   whole module. #506 item 1, its docstring's enumeration, goes with it.
3. `docs/running/the-agent-set.md` *What a spawn costs*: the paragraph that
   opens "**The orchestrator's acts are counted, each against what delivers
   it.**" and its check line.
4. `docs/layout/the-pact.md` *One routing answer, one id, every gated
   repository*: the check line's second target. The line keeps
   `tests/behaviour/test_a_signer_declares_its_pact.py`.
5. `skills/implement/orchestration.md`, the opening's sentence that begins
   "`skills/implement/acts.md` tables each act addressed to the orchestrator".
6. `skills/code-review/orchestration.md`, the opening: the sentence keeps
   "Every `##` heading here opens with `Orchestrator:`." and loses the clause
   that cites `acts.md`.
7. `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py#headings`
   docstring: the paragraph "**One parser, two readers.**" goes but for its
   first clause, kept as one sentence naming `marked_headings` as the one
   reader left, which A4 asks the docstring to name.
8. `tests/text/test_broad_gate_rule.py#test_the_acts_table_row_names_the_preflight_and_stays_a_sentence`,
   the case. The fact it pinned beyond the row, that a session skipping the
   preflight loses only time, stands at
   `skills/code-review/orchestration.md:487`.
9. `tests/behaviour/test_docs_line_wrap.py`, the `COVERED` entry for
   `skills/implement/acts.md`. The comment line above it stays, as the
   comment of the `skills/implement/multi-repository.md` entry it also
   heads: both files were cut from the same file in one commit.
10. `.test_durations`: the 22 entries naming the deleted module, the deleted
    case, or a parameter on `skills/implement/acts.md` (executed: `grep -c`).

The list is whole for the tree outside `seal/threads/`. It was built from
every file `git grep` lists for the path `acts.md`, the module's name, the
section's title, and the table's words `Delivered by`, `still a sentence`
and `part of its parent` (executed). One hit is left on purpose; see O3.

### D2 Neither of #506's repairs is built

#506 item 2 (the table reads the marker) and item 3 (the table cannot reach
an act outside two files) are limits of the table, and they leave with it.
Splitting the marker would add a second mark for a table that no longer
exists. A named list of sections would be a second enumeration beside the
tree, the shape #506 names. Item 1's case would hold a docstring that no
longer exists, and the probe under *Grounding* found no other live
instance.

### Out of scope

- O1. The `Orchestrator:` marker on every heading stays, and no heading is
  renamed. Its one remaining meaning is the payload rule, which
  `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`
  holds. A rename would move citations across the tree for no catch.
- O2. Docstring enumerations of cases in the other 13 test modules. Every
  name resolves today (*Grounding*, the probe row). Whether such pairs are
  measured belongs to #1236, the next item of this milestone, which measures
  pairs of parts that can hold one fact twice (its title, executed:
  `gh issue view 1236`).
- O3. `tests/skills/test_session_cost.py:15-20` says "one is still a
  sentence". It sits in a block the module labels as docstrings quoted "as
  they stood", and it states no fact of the table. It is test history, not
  rule text.
- O4. Earlier work items' records that cite `acts.md`. They are history, and
  each leaves with its directory at the settle after its release.
- O5. The posting act in `skills/verify/orchestration.md`. Its limit is
  already stated at `docs/running/measuring-a-run.md:119`.
- O6. Arming any act that the table read as `still a sentence`. #506 *What
  is not here* excludes it on #330's grounds.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 Nothing names the table | Given HEAD after the build, when the tree outside `seal/threads/` is searched for the table and its test, then no file names them, except O3's history line | `git grep -n -E 'acts\.md\|test_every_orchestrator_act_names_its_delivery\|which of these acts runs itself\|Delivered by\|part of its parent' -- ':!seal/threads'` prints nothing; `git grep -n 'still a sentence' -- ':!seal/threads'` prints only `tests/skills/test_session_cost.py` |
| A2 The policy root holds no rule about the table | Given `docs/running/the-agent-set.md` *What a spawn costs*, when it is read, then the acts paragraph and its check line are gone and the section's other rules are unchanged; given `docs/layout/the-pact.md`, then its check line names `tests/behaviour/test_a_signer_declares_its_pact.py` alone | `git diff` of the two files; `seal rules --check` refuses no check line |
| A3 The orchestration files cite no table | Given both `skills/*/orchestration.md`, when their openings are read, then neither cites `acts.md`, and `skills/code-review/orchestration.md` still says every `##` heading opens with `Orchestrator:` | `git diff` of the two files |
| A4 The marker test keeps its reach | Given the marker test, when it runs, then its cases pass unchanged and its `headings` docstring names one reader | `bin/test tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` |
| A5 The tests that read the removed file still pass | Given the wrap list, the broad-gate module and the script-naming module, when they run, then they pass and none is parametrized on `acts.md` | `bin/test tests/behaviour/test_docs_line_wrap.py tests/text/test_broad_gate_rule.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/text/test_no_passage_is_pasted_into_a_second_file.py` |
| A6 No mechanism is added | Given the diff, when it is read, then it adds no test, check, hook, mark or rule, and `## Removes` names every removal | the proofer reads `## Removes` against the diff |
| A7 The version stays | Given `.claude-plugin/plugin.json`, when it is read after the build, then it reads `0.31.1` | `git diff` shows no change to it |

## Data & interfaces

No interface changes. Nothing imports the deleted module: `acts`, `rows`
and `findings` are read by its own cases alone (executed: `git grep` for the
module name lists docstrings and comments only). The marker test's
`headings` keeps its signature and its one caller, `marked_headings`.

## Rule changes

- nothing
  why: This work item's subject is the policy root's text, the rule in `docs/running/the-agent-set.md` *What a spawn costs* that the orchestrator's acts are counted, together with the table and test that rule names, so it edits `docs/` directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*. A `remove` with a `from` would leave the two check lines naming the deleted test refused at HEAD until the settle. No section moves, so no unsettled design's operation is re-pointed.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the acts table, its four delivery values and its paragraphs | `skills/implement/acts.md` | nowhere: it caught only its own drift (D1). Its text stays readable at `git show v0.31.0:skills/implement/acts.md`, and each `Grounds` cell restates a hook's own home |
| the test holding the table, and its docstring's enumeration of cases (#506 item 1) | `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` | nowhere: every message it can report is about the table (D1) |
| the rule "The orchestrator's acts are counted, each against what delivers it", with its check line | `docs/running/the-agent-set.md` *What a spawn costs* | nowhere: the rule stated the table. The payload rule above it stays |
| the check line's target `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` | `docs/layout/the-pact.md` *One routing answer, one id, every gated repository* | nowhere: the test held the table's row for the multi-repository act, not this rule. The line keeps `tests/behaviour/test_a_signer_declares_its_pact.py` |
| the sentence citing `acts.md` | `skills/implement/orchestration.md`, the opening above *Orchestrator: the order inside a ticket* | nowhere: an orchestrating session did not open the file it cited |
| the clause citing `acts.md` *Orchestrator: which of these acts runs itself* | `skills/code-review/orchestration.md`, the opening above *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* | nowhere: the clause before it, that every `##` heading opens with `Orchestrator:`, stays |
| the paragraph "One parser, two readers", but its first clause, kept as one sentence naming the one reader left | `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py#headings` | nowhere: one reader is left |
| the case pinning the acts row for the pull-request section | `tests/text/test_broad_gate_rule.py#test_the_acts_table_row_names_the_preflight_and_stays_a_sentence` | the preflight fact it read stays at `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, which the module's other cases read |
| the `COVERED` entry for `acts.md`; its comment stays, heading the `multi-repository.md` entry | `tests/behaviour/test_docs_line_wrap.py#COVERED` | nowhere: the file is gone |
| the 22 entries for the removed cases and the `acts.md` parameters | `.test_durations` | nowhere: they price cases nothing collects |

Framed 2026-11-04 by framer, before the build.
