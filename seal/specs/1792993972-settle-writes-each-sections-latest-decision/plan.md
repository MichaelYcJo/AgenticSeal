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
work item ships the mechanism; the 0.22.4 release settle runs it.

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
old fact, in its own pull request, found by running the documents' checks
over what it wrote. The class no longer refuses or holds a spec; its cost
moves into the settle's own edits. Nothing is added at the work item's pull
request (`questions.md` answered list, A3).

**How a settle's result is verified.** Each instrument proves one thing and
none proves the whole:

| Instrument | What it proves of a written section |
|---|---|
| the suite, through each rule's `check:` target | the rule the section states still holds in the code; a pin under `tests/` catches a section written away from a pinned sentence |
| `tests/test_docs_line_wrap.py` | no written line passes 88 columns |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` | the section copies no passage of another file, and no file copies it |
| `tests/test_both_editions_carry_the_same_folds.py` | a `.ko.md` edition keeps its English edition's headings |
| `tests/test_rules.py` (`rules --check`) | each check line the section carries is in grammar and names a target that exists |
| `fold-check` | the index names each document, and which documents pass the ceiling |
| the dry run, run again after writing | for each operation, whether its `to` is now found in its section: a report of where the session reworded, which the body explains |
| the CI readers | only that each removal took a whole directory that stood at the base |
| the settle's pull request, reviewed by the owner | that each section states the latest decision and agrees with the code, which no check reads |

**Failure scenario of the chosen approach, six months on.** A settling
session writes a section that states an earlier decision as the latest, or
misreads the code. No check reads that, so it reaches `docs/` unless the
owner's review of the body catches it. The body's per-group grounds (the
spec ids in merge order, which operation was superseded, the code
coordinate) are what make that review cheap. A second scenario: a work
item's pull request removes another work item's whole directory by mistake;
CI reads it as a settle, and only its review sees it.

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

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The settle groups, shows and removes, and the skill states the settling session's procedure. `rule_changes.py` gains the grouping function and the section-range finder and loses `replay`, `conflicts`, `_ancestor`, `apply_op` and `_cut`; `settle.py` prints the dry run of `spec.md` *In* item 1 and does the `--apply` of item 2, with no merge base and no document writes; `skills/settle/SKILL.md` is rewritten in place (*In* items 3 and 6, the replacement sentence); `README.md`, `README.ko.md`, `seal/README.md`, `templates/seal-README.md`, `templates/config.md`, `skills/config/SKILL.md` and `skills/implement/SKILL.md` line 75 say the new behaviour (*In* item 7); the cases of S1 to S5 and S11 written and seen red, the retired cases of `## Removes` removed; S10's read-only dry run over the real tree, its group headings and counts in the phase record | `bin/test tests/test_rule_changes.py tests/test_settle.py tests/test_settle_reads_before_it_removes.py tests/test_settle_applies_rule_changes_in_place.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_both_editions_carry_the_same_folds.py tests/test_rules.py -q`; S10's command and its output | |
| 2 | A whole removal reads as a settle at the pull request. `unverified_check.py#settled` reads that the directory stood at the base (*In* item 4), with its docstring, the `--baseline` help text, the module docstring lines 25 to 27 and the `settled:` notice rewritten; `chain_check.py#SETTLE_SAYS`, `#RULE_CHANGES_SAYS`, `#retired`'s docstring and the module docstring's declaration arm rewritten (*In* item 5); the cases of S6, S7 and S9 written and seen red, S8's cases passing unchanged, the retired predicate cases removed | `bin/test tests/test_unverified_check.py tests/test_chain_check.py tests/test_settle.py -q` | |

Phase 1 comes first because `settle.py#rule_arm` calls the predicate today:
once phase 1 reads the open rows directly through
`unverified_check.py#open_record_rows`, phase 2 can loosen the predicate
without `settle` retiring a directory whose row is still open.

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
