# Implementation Plan: 1793521559-a-finding-is-counted-once

## Technical context

The count builds on three readers that already exist.

- `skills/code-review/scripts/chain_check.py#round_read` (lines 633-732) reads a round record through `hooks/lib/fields.py#read`. It places each block by the record's headings, and refuses a block out of its place. `#finding_of` (lines 735-780) builds the one `Finding` per finding section. Its `paths` joins the finding block's `location:` paths and the close block's. `#record_findings` (line 783) is the entry point that `.github/scripts/release_seal.py#chain_counts` already uses.
- `hooks/lib/routing.py#parse` reads a `routing.md`, and `#rounds` and `#rounds_unreadable` (lines 575-648) list a work item's records.
- `skills/settle/scripts/settle.py#released` (lines 191-214) names the work items whose directory a ref holds.

The new script loads the three by path, as `release_seal.py#readers` (lines 271-280) does. Its cases go in `tests/github/`, as each `.github/scripts/` file's do, and they build fixture trees as `tests/github/test_release_seal.py` does. `conftest.load_module` is the loader there.

`Finding` is a `collections.namedtuple` built at one place, line 767. Its fields are read by attribute in `tests/skills/test_chain_check.py:665` and `:3730`. A new field changes neither case's reading. A new field appended last keeps every positional reading too.

The failure scenario of the chosen approach, six months on: the round record's grammar moves again, say a finding may hold two `location:` lines, or the finding block moves out of its section. `#finding_of` changes with it. If the change merges paths differently and leaves `located` holding the union, the count reads close paths again and nobody sees it. The S7 case in `tests/skills/test_chain_check.py` pins `located` against `paths`. That case is what turns that change red. A second scenario: the step stops being run, the `flow-baseline` issue closes, and the script stays with no reader. `docs/release-checklist.md` *2b* is then the place that names it, and the settle that drops the step removes the script with it. That is `skills/core/SKILL.md` *The rule a mechanism is kept against*, applied at that settle.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the grep, and write the pattern into the step, anchored and limited to the finding block (an `awk` that tracks a `seal` fence whose first line is `severity:`) | The awk re-encodes `hooks/lib/fields.py`'s grammar: where a fence opens and closes, one fence inside another, the block's kind on its first line. The next change to the grammar moves the parser and not the awk, and the count drifts in silence. The Grounding's two grep readings already differ in four of eight regression counts from one change of anchor. That is the drift a reader-spelt pattern produces. | rejected: `skills/core/SKILL.md` *The first value*, "a script does not re-encode that judgment as a grammar rule: it reads what a command wrote or what a real parser returns" |
| A `python3 -c` command written whole in the step, loading `chain_check.py` by path and counting | The code lives in a policy document that a pull request does not edit. A defect in it waits for a design and a settle, and no test reads it, because tests read the tree's code and not a sentence of `docs/`. | rejected: the same count, with no test and no way to fix it inside a pull request |
| `seal settle`'s dry run prints the four numbers per released work item, beside the round count *The judgments* already prints | Every installed repository's settle prints numbers that nothing there reads. The step says it "ships to no user: the plugin's settle procedure (`skills/settle/SKILL.md` *The settling session's procedure*) does not take it". The shipped script, its docstring, the skill's *What the dry run shows* and their cases all grow for one repository's measure. A change to that measure would then be a change to the plugin's output. | rejected: the cost lands on every user and the catch on one repository (`skills/core/SKILL.md` *The rule a mechanism is kept against*) |
| A script under `.github/scripts/` that reads `Parsed.inside` from `round_read` and picks each finding's own block by matching its heading line to a span, with `chain_check.py` unchanged | The script re-derives which block is the finding's, a placement `round_read` has already decided. A span that `round_read` drops, a spoilt one or one with a second number, must be matched the same way in two places. One more reading of the record's structure lives outside its reader. | rejected: `chain_check.py` owns where a path came from, so it is the place that says it |
| Remove the step and its count, as the structure the problem calls to replace | The settle of 0.27.1 posted the numbers to #51 on 2026-10-31 (executed: `gh issue view 51 --json comments`). The step's paragraph says the records-alone number decides whether #1020's recurrence check is the next step, and #1020 is open (executed: `gh issue view 1020 --json state`). Removing the count leaves that decision with no reading. The premise that keeps it is checked: a reader exists, and so does a decision that waits on it. | rejected: the issue asks to keep the four numbers, and the checked premise holds |
| **Chosen**: `chain_check.Finding` gains `located`, the finding block's paths. `.github/scripts/finding_counts.py` counts through `#record_findings`, and the step names that command | The failure scenarios are in *Technical context*: a grammar change that leaves `located` holding the union, which S7 catches, and a script that outlives its step. | chosen: one reader of the record, one command in the step, no output added for users, and a test that reads the rule |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2 and 3 of `frame/design.md` | `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py`, and each module that reads `chain_check.py` or `.github/scripts/` as contract rule 2 lists them. `python3 .github/scripts/finding_counts.py --released-at 813665f0` from the worktree, whose output reads as S8 says and is pasted into the phase record. Each new case seen red as its scenario's row says | 1da90703 |

Scope item 4 is written in `frame/design.md` `## Rule changes` and is applied at the settle after the release. No phase builds it, and the diff edits nothing under `docs/` (S9).

## Operational impact

None for a user. The new script runs only when this repository's settling session types it at step 2b. No workflow runs it. It needs no package beyond Python's standard library and the plugin's own readers. `chain_check.Finding` gains a field that no gate reads, so the pull-request check's exit codes and messages stay as they are.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-01 | The frame was read against #1223 and spawned as committed, with no proposal to the framer | The script through `chain_check.py#record_findings`, the `located` field and the three rule changes meet the issue's *Done when* | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* |
| 2026-11-01 | Round 1's fix pass changed what the script prints under the table, so `frame/design.md` *Data & interfaces*'s Stdout bullet is folded in place to state the two lines | The fix pass names the bullet as standing on the old output and does not edit the frame; the verifying round and any later crafter read one statement | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* |
| 2026-11-01 | Round 2's #1 (`regression: round-1#2`) is routed to an ordinary fix pass, not to the framer; round 2's #2 may be fixed in place | The defect, an absolute path printed through `str(problem)` in a table meant for a public issue comment, came from round 1's paste-ready fix applied as given, which the routing table names as a fix pass; the frame says nothing of the reason's spelling. #2 is a one-line docstring summary in `hooks/lib/routing.py#rounds_unreadable` that states the fact round 1's #1 corrected, so contract rule 19 reaches it; this is the first regression on the unit | `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* |
| 2026-11-01 | After three finding rounds, the run goes on: round 3's #1 (`regression: round-2#1`, `why_not`'s fallback for an `OSError` with no `strerror` pinned by no case) takes an ordinary fix pass and one verifying round, not the framer | The counts shrink (2, 2, 1, all `should`), and the frame holds: it says nothing of `why_not`, which round 2's fix added, and the defect is a missing case for a branch the frame never asked for, not a design that keeps failing; the second regression on the unit is a case left out, which a case or the branch's removal answers | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* and *A regression is routed by comparing the fix with the frame* |
