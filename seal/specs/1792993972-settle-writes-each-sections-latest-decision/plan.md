# Implementation Plan: settle writes each section's latest decision (#1033)

Approved 2026-10-26 by the orchestrator under the owner's automation answer, when `smith` was spawned for phases 1 and 2.

## Summary

`settle` stops applying each released spec's `## Rule changes` as a literal
find-and-replace in merge order. The script groups the released specs by the
sections their operations name, shows each group's history beside the section
as it stands, lists every open row of every released record, and removes
directories. The session the owner runs the settle in writes each section as
the group's latest decision, checked against the code, and closes every open
row from the tree, asking nobody; its pull request states each judgement for
the owner. The CI predicate that tells a settle from a deletion keeps only
the facts it can read. The grammar of `## Rule changes` does not change. This
work item ships the mechanism; the 0.22.4 release settle runs it. After
round 3 the procedure's step 6 runs the rules' `check:` targets and no
searched set of test modules, and step 8, the repository's broad gate, is
the one run that reads every check, run again after any fix (phase 3).

## Technical context

**The present mechanism, read at `b12f3335`.**

- `skills/settle/scripts/settle.py#rule_plan` (lines 275 to 336) parses each
  released spec as `--released-at` holds it, orders the specs by the commit
  that added each `spec.md` (`rule_changes.py#order`), holds a spec for a
  parse error, a missing adding commit, a name differing only in case, or an
  open row in the working tree or at the merge base, refuses both specs of a
  pair no ancestry orders at one place (`rule_changes.py#conflicts`), and
  hands the rest to `rule_changes.py#replay`. `replay` applies each spec whole
  or not at all with `apply_op`, and a spec after a refused one at an
  overlapping place waits (`rule_changes.py` lines 320 to 355). `settle.py#apply`
  writes what the replay returns and removes each applied directory and each
  spec-less directory `rule_arm` retires.
- `settle.py#rule_arm` (lines 253 to 272) asks `unverified_check.py#settled`
  of the working tree and of the merge base of `--released-at` and `HEAD`,
  which is #602's rule: a closure that has not reached that base keeps the
  directory.
- `skills/verify/scripts/unverified_check.py#settled` (lines 1274 to 1335) is
  the one predicate. A directory is settled when it stood at the base with
  nothing open in its record, and either it states no rule or a replay of
  every removed spec over the base's policy root leaves each named text as
  often in the head's policy root as in the replay. Its readers are
  `unverified_check.py --baseline` (lines 1727 to 1768) and
  `chain_check.py#retired` (lines 2126 to 2132), both run by
  `.github/workflows/hygiene.yml` against `origin/<base_ref>`.
- `skills/code-review/scripts/chain_check.py#rule_changes_read` (lines 1583
  to 1597) parses each judged and each edited work item's section with
  `rule_changes.py#parse` and nothing else: it never places a `from`.

**What the tree holds now** (executed: a shell walk over `seal/specs/` and
`git ls-tree --name-only origin/main seal/specs/`). Of the 45 work item
directories on this branch, 41 are released at `origin/main`. Of those 41,
35 hold the no-change block and 6 state rule changes (`1792533444`,
`1792540458`, `1792619408`, `1792624592`, `1792627930`, `1792628098`). Every
one of the 41 has at least one open `## Not verified` row, about 62 rows in
all by an `awk` count that is not the reader's (`questions.md` Q3).
`1792935671` and the other 0.22.4 work items are not released at
`origin/main`.

**Why the predicate has to change in this item, not later.** The settle's
pull request goes to `release/v0.22.4`; CI asks the predicate at that
branch's tip, where the 41 records still hold their rows open, so the
current predicate refuses every removal and the pull request is red. The
release pull request then goes to `main`, where the same rows stand open, so
even a closure merged first in its own pull request (the present two-step
rule) leaves the release pull request red until a later release. And a
superseded spec's `to` text is by design not in `docs/`, so the replay count
refuses it too.

**#952's class, green at the pull request and red at the settle.** Its
rounds found three shapes (`seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/rounds/round-1.md`
finding 3, `round-2.md` finding 1, `round-3.md` finding 1): a test pinning a
sentence the spec retires, a README copying the rule's new sentence that the
duplicate-passage check refuses once the sentence lands in `docs/`, and a
`to` line that lands past 88 columns. All three came from a settle that
writes `to` text verbatim and may write no sentence by hand. Under this
design the settling session writes the text, so it wraps lines, words a
section that would copy another file, and retires a pin that stands on the
old fact, in its own pull request, found by the repository's broad gate,
which it runs after `--apply` and again after each fix (*Step 6 after round
3* below). The class no longer refuses or holds a spec; its cost
moves into the settle's own edits. Nothing is added at the work item's pull
request (`questions.md` answered list, A3).

**How a settle's result is verified.** Each instrument proves one thing and
none proves the whole. In this repository every row naming a module under
`tests/` runs inside the `Broad gate` row, which the settling session runs
at step 8; step 6 runs only the rules' `check:` targets:

| Instrument | What it proves of a written section |
|---|---|
| each rule's `check:` target, at step 6 and again inside the broad gate | the rule the section states still holds in the code |
| the repository's `Broad gate` row (`seal/config.md` line 10), after `--apply`, run again after any fix | every check reads what the session wrote, those no search of the tests' text lists included; the pull request opens on a passing run with no edit after it |
| a pin under `tests/`, inside the broad gate | a section written away from a pinned sentence |
| `tests/test_docs_line_wrap.py` | no written line passes 88 columns |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` | the section copies no passage of another file, and no file copies it |
| `tests/test_both_editions_carry_the_same_folds.py` | a `.ko.md` edition keeps its English edition's headings |
| `tests/test_rules.py` (`rules --check`) | each check line the section carries is in grammar and names a target that exists |
| `fold-check` | the index names each document, and which documents pass the ceiling |
| the dry run, run again after writing | for each operation, whether its `to` is now found in its section: a report of where the session reworded, which the body explains |
| the CI readers | only that each removal took a whole directory that stood at the base |
| the settle's pull request, reviewed by the owner | that each section states the latest decision and agrees with the code, which no check reads |

**Step 6 after round 3.** Round 3's finding 1, a second regression on step 6
of `skills/settle/SKILL.md` *The settling session's procedure*, closed
`deferred the frame`. The unit has been rewritten twice. `ffeadf29` gave it
a set, the `tests/` modules naming the policy root's directory, for round
1's finding 5. `72fc2c58` widened that to the modules holding `docs` as a
word or a changed file's name, for round 2's finding 1. Each time a module
outside the spelling read a changed document: round 2 found three that join
a path from its parts, and round 3 found
`tests/test_one_heading_rule_holds_to_commonmark.py`, which lists every
tracked `.md` file. A setext line written into `docs/the-review-record.md`
passed the 106 modules of step 6's set and failed that module (round 3,
executed there). Round 3 also names a class no spelling closes: a module
that reaches a document through a helper in another file
(`tests/conftest.py:31-46` `review_chain_text`) or a script it runs.

What step 6 decides is the question `CLAUDE.md` *The rule a mechanism is
kept against* puts once fixes chase a mechanism's edge cases. It decides
nothing: no step reads its result, and step 8 runs the repository's `Broad
gate` row, which in this repository is `ruff check`, `ruff format --check`
and `bin/test -q`, the whole suite (`seal/config.md` line 10, read). Step 6's
set was 106 of the 176 `tests/test_*.py` modules for one changed file
(round 3, executed; the 176 executed by `ls tests/test_*.py | wc -l` at
`27177bf2`), so it ran two thirds of the suite without being the suite. And
the skill is the plugin's, run in any repository, where `tests/` and `docs`
as a word are this repository's layout. So step 6 runs what the frame can
name for any repository, each rule's `check:` targets and the dry run, and
step 8 is where every other check shows. Round 1's finding 5 objected that a
session reading the `check:` targets as the set "finds the rest at step 8,
which runs once". The objection rested on step 8 having no path after a
failure. Step 8 now has one: a failure is changed, the failing modules run,
and the row runs again. `README.md` lines 68 to 76 ask that "nothing edits
between that run and the PR", which a second run after a fix keeps (read).

**Failure scenario of the chosen approach, six months on.** A settling
session writes a section that states an earlier decision as the latest, or
misreads the code. No check reads that, so it reaches `docs/` unless the
owner's review of the body catches it. The body's per-group grounds (the
spec ids in merge order, which operation was superseded, the code
coordinate) are what make that review cheap. A second scenario: a work
item's pull request removes another work item's whole directory by mistake;
CI reads it as a settle, and only its review sees it. A third, of step 6: a
settle that rewrites a pinned sentence, as the 0.22.4 settle will (the pin
`questions.md` A9 names), fails its first broad run on that pin and runs
the row a second time after the fix. That second run is the cost of step 6
holding no searched set, and it is a run, not a stop: nobody is asked.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Keep the literal replay and rewrite each stale `from` by hand** (#1025 part 1) | Three stale `from` values arose in one release from three different causes (another spec, the backlog settle, a knock-on of a refused spec). Each settle meets new ones and every spec behind them waits; the 41 rows hold forever, since nothing brings a row back to its answerer | rejected: it treats the instances, and the timeline keeps producing them |
| **`chain-check` replays every unsettled spec in merge order and refuses a `from` the replay no longer finds** (#1025 part 2) | Every pull request fails for another spec's staleness; a later spec that supersedes an earlier one cannot merge until someone rewrites the earlier spec's released record; it adds a gate to every pull request and still answers neither the rows nor the code moving past a spec | rejected: a new gate that moves the stop earlier without removing it |
| **The script applies each group whose latest operation places, and the session writes the rest** | Two writers of one policy root; an operation that places is not checked against the code, which is step 3 of the owner's direction; the reviewer cannot tell which sections a person-like judgement wrote | rejected |
| **Chosen: the script groups, shows and removes; the settling session writes and decides; the body states; the owner reviews** | A wrong decision reaches `docs/` unless the review catches it (*Technical context*) | chosen: it is the owner's direction, it removes the class of refusal, and it asks nobody |
| **Keep the structure: the predicate as it is** (rows open at the base, the replay count) | Certain, not possible: the settle's pull request is red at `release/v0.22.4`'s tip, where the 41 rows are open, and the release pull request is red at `main`; a superseded spec's `to` is absent by design. The premise that kept it, that a settle applies text verbatim and moves only closed records, is false under this design (checked: `unverified_check.py` lines 1290 to 1335 and `hygiene.yml` lines 157 to 195) | rejected |
| **Read the record as the removing commit's parent held it** | The settle's pull request is squashed into `release/v0.22.4`, so the closures and the removal become one commit and the parent holds the rows open: the release pull request is red. It works only with a closure pull request merged first, one more pull request and wait per settle, and the replay count still has to go | rejected |
| **Chosen: settled means the directory stood at the base and is gone whole** | A pull request outside a settle that removes a whole work item directory passes CI as a settle; its diff shows the removal, and its rows stay in git. No step of the workflow removes another work item's directory, so this is a limit, written into the rule, and not a guard (`docs/the-record-layout.md` rewritten) | chosen: the two facts it reads are facts, and a predicate that read more would read words |
| **Add "present at `origin/main`" to the predicate** | Every reader must be handed a second ref and fetch it; it catches only a pull request into a release branch that removes an unreleased sibling's whole directory, a shape no flow produces | rejected: a gate for an edge outside the normal flow |
| **Keep the structure: the grammar as it is** | The failure was never the grammar's shape but the precondition the settle put on `from`; with the precondition gone, `from` still locates the text for the settling session and the reviewer. A spec author may keep writing long exact `from` values that matter less than before, which costs a framer some care and nothing else | chosen (premise checked: every `spec.md` under `seal/specs/` parses, executed with `rule_changes.py#parse` before this item's section was written) |
| **A new section-level grammar** (one operation stating a section's rule) | Every spec in the tree is in the old grammar, so they would need a second reader until they settle, and every framer, the template and `chain-check` would change for no failure the old shape caused | rejected |
| **Run the settle in this work item** | The 41 directories, six groups and about 62 row decisions enter this item's review rounds, judged against a frame that cannot state those decisions in advance; a settle is not a work item (`skills/settle/SKILL.md` *A settle is not a work item*), and the removal of 41 directories hides the mechanism's diff | rejected |
| **Chosen: ship the mechanism; the 0.22.4 release settle runs it** | The settle depends on the owner calling step 2b before the release pull request; if it is skipped, the 41 wait one more release, as today | chosen: the smaller safe path; the dry run over the real tree (S10) shows the mechanism meets the corpus before anything is removed |
| **A pull-request check that applies a spec's `to` texts and runs the documents' checks** (#952 round 3's open row) | It would check text that the settling session will reword, so it reads a guess and could only be a report | rejected (`questions.md` A3) |
| **Keep the structure: step 6's searched set as `72fc2c58` left it, with its sentence on what the set holds** | Certain: the sentence says the set holds the checks that read every document, and the heading module is outside it (round 3 finding 1, executed). The premise that keeps it, that the set holds every module reading a changed file, is false | rejected |
| **Keep the search, add `-e '*.md'`, and state the class it cannot find** (round 3's second option, paste-ready) | A module that lists documents another way (`endswith(".md")`, a suffix test) or reads one through a helper is still outside the set, so the limit sentence is needed anyway, and the next round that meets such a module asks for a fifth spelling. The set, 125 modules over six files (round 3, executed), runs about two thirds of the 176 modules and stays a partial run. Its spellings (`tests/`, `docs` as a word) are this repository's layout, in a skill every repository runs | rejected: a fourth spelling for a set no step reads |
| **Name the instruments: the `check:` targets and the line-length, passage, edition and heading modules** (round 3's first option) | The named modules are this repository's files, written into a plugin skill that other repositories run, and a stored list goes stale when a check is added (`CLAUDE.md` *The rule a mechanism is kept against*: nothing kept beside the tree to stay in step with it) | rejected; the `check:` targets alone are kept, since every spec names them |
| **Search the tree for a run of words of each sentence the session removed, and change each pin or copy it finds** | A pin splits its string across lines and a copy may wrap differently, so the search misses by spelling exactly as step 6's did, and the passage and line-length checks still show only in the broad run | rejected |
| **Run the whole suite at step 6, then the broad gate at step 8** | Two full runs in every settle, the first before `--apply`, so the checks that read the corpus fail at the second anyway; `README.md` lines 68 to 76 take the broad checks once the edits are done | rejected |
| **Chosen: step 6 runs each rule's `check:` targets and the dry run; step 8's `Broad gate` row is the one run reading every check, run again after a fix, done when it passes with no edit after it** | A settle that breaks a pin or a whole-tree check runs the broad gate twice (*Technical context*, third scenario). A repository whose `Broad gate` row runs less than its whole suite meets a check outside the row in CI, the case of any pull request | chosen: complete by construction, the same text in every repository, and no set to keep spelled |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The settle groups, shows and removes, and the skill states the settling session's procedure. `rule_changes.py` gains the grouping function and the section-range finder and loses `replay`, `conflicts`, `_ancestor`, `apply_op` and `_cut`; `settle.py` prints the dry run of `spec.md` *In* item 1 and does the `--apply` of item 2, with no merge base and no document writes; `skills/settle/SKILL.md` is rewritten in place (*In* items 3 and 6, the replacement sentence); `README.md`, `README.ko.md`, `seal/README.md`, `templates/seal-README.md`, `templates/config.md`, `skills/config/SKILL.md` and `skills/implement/SKILL.md` line 75 say the new behaviour (*In* item 7); the cases of S1 to S5 and S11 written and seen red, the retired cases of `## Removes` removed; S10's read-only dry run over the real tree, its group headings and counts in the phase record | `bin/test tests/test_rule_changes.py tests/test_settle.py tests/test_settle_reads_before_it_removes.py tests/test_settle_applies_rule_changes_in_place.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_both_editions_carry_the_same_folds.py tests/test_rules.py -q`; S10's command and its output | a8e6a2f9 |
| 2 | A whole removal reads as a settle at the pull request. `unverified_check.py#settled` reads that the directory stood at the base (*In* item 4), with its docstring, the `--baseline` help text, the module docstring lines 25 to 27 and the `settled:` notice rewritten; `chain_check.py#SETTLE_SAYS`, `#RULE_CHANGES_SAYS`, `#retired`'s docstring and the module docstring's declaration arm rewritten (*In* item 5); the cases of S6, S7 and S9 written and seen red, S8's cases passing unchanged, the retired predicate cases removed | `bin/test tests/test_unverified_check.py tests/test_chain_check.py tests/test_settle.py -q` | 0dc1087a |
| 3 | The settling session runs the `check:` targets at step 6 and the broad gate reads every check at step 8, after round 3's finding 1. Steps 6 and 8 of `skills/settle/SKILL.md` *The settling session's procedure* are rewritten in place to `spec.md` S13's target text, step 7 unchanged: step 6 loses the searched set, its `git grep` command and its sentence on what the set holds, and step 8 loses "once" and gains the failure path and its done condition. `tests/test_settle_reads_before_it_removes.py::test_the_skill_states_the_settling_sessions_procedure` drops its three strings pinning the set and its command and the string "Run the repository's `Broad gate` row once.", gains "Run each rule's `check:` targets over what you wrote", "The step is done when every `check:` target passes", "step 8 runs every one", "It is the one run that reads every check" and "The step is done when the row passes with no edit after it" in that order, asserts that `git grep` is absent from the procedure, and its docstring's sentences on rounds 1 and 2 give way to one on round 3: step 6 holds no searched set and step 8 reads every check. The `changelog.md` clause "runs each rule's `check:` targets and every test module naming the policy root's directory or a file it changed over what it wrote" becomes "runs each rule's `check:` targets over what it wrote and the repository's broad gate after `--apply`, again after any fix, so the pull request opens on a passing run with no edit after it". Outside this work item's frame, no file but these three states step 6's set or step 8's "once" (executed: `git grep` for the set's sentence, its command and "row once" outside the round records at `27177bf2`) | the case seen red against `27177bf2`'s skill text and green after; `bin/test tests/test_settle_reads_before_it_removes.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_docs_line_wrap.py tests/test_one_heading_rule_holds_to_commonmark.py -q` | open |

Phase 1 comes first because `settle.py#rule_arm` calls the predicate today:
once phase 1 reads the open rows directly through
`unverified_check.py#open_record_rows`, phase 2 can loosen the predicate
without `settle` retiring a directory whose row is still open. Phase 3 is
the redesign after round 3 and touches only the skill's procedure, its pin
and the changelog fragment; phases 1 and 2 keep their commits.

## Operational impact

- **The 0.22.4 release settle must run the tree's script.** `bin/settle` on
  the Bash tool's PATH is the installed plugin's, 0.22.3 at framing time,
  which is the literal replay. On the preparation branch, after this item
  merges into `release/v0.22.4`, the owner's session runs
  `python3 skills/settle/scripts/settle.py` and
  `python3 skills/settle/scripts/settle.py --apply`. CI already runs the
  tree's readers (`hygiene.yml` lines 160 and 194), so the settle's pull
  request and the release pull request are judged by the new predicate.
- **What the 0.22.4 settle meets.** Six released specs with rule changes,
  two of them refused today (`1792619408`, `1792627930`), 35
  with the no-change block, and every one of the 41 held by open rows that
  the settling session decides. `1792935671` waits for the next release's
  settle with the other 0.22.4 work items.
- **The settle may edit outside `docs/`.** Where a written section leaves a
  case under `tests/` or a README copy standing on the old fact, the settle's
  pull request changes it and names it (`questions.md` A9). The settle still
  opens no work item.
- No migration, no new dependency, no new environment variable. The grammar
  of `## Rule changes` is unchanged, so no spec in the tree is rewritten.
- The pull request for this item states the failure direction (the predicate
  allows more), a prompt budget of zero, and what it removes, as
  `CONTRIBUTING.md` *What a change to a gate must carry* asks.
