# Implementation Plan: the seeded scaffold hides the shipped rounds, and the harness reader miscounts findings (#986)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved 2026-10-22 by the orchestrator, under the owner's `automation` answer and the defaults of Q1 to Q4, when `smith` was spawned.

<!-- The line above is the record that the gate happened. The orchestrator
writes it when it spawns the build, in the shape and on the terms
`skills/implement/orchestration.md` *The plan is approved at the spawn*
states, including the shape where `routing.md` answers `Implementation`
with `the session`. A later session, a reviewer and CI all read the tree,
and a plan with nobody's name on it cannot be told from one nobody approved.
The line shares its shape with `templates/sdd-routing.md`'s `Answered <date>
by <who>, before the first edit.`: the verb, the date, who, and the moment.
The two are pinned against each other, so neither spelling can drift into a
second convention for one kind of fact. -->

## Summary

Two phases, each closed by free cases and no paid run. Phase 1 makes the
harness read a round record through the check's own split and keep the
record it read, so the count of findings and the count of finds come from
one reader, and a reader corrected later can be applied to every side taken
from now on. Phase 2 builds each seeded case at its work item's round 1
target, the tree the real first review saw, so nothing in it cites a record
or a commit the clone lacks, and nothing in the clone holds the build
without the seed. The paid baseline is `questions.md` Q1, not run by
default.

## Technical context

The code this builds on, opened at 65db1096:

- `evals/scripts/noninferiority.py:73` `FINDING_ROW`, `^location: .*$`
  over the whole printed text. `:188` `report_rows` finds the last
  `cat <...>/round-N.md` result in a trace and returns the lines
  `FINDING_ROW` matches. `:385` `annotate` stores them as `report_rows`.
  `:506` `side_numbers` counts rows and false rows from them, and takes
  each `truth-` grader's passes from the eval's recorded results. `:1118`
  `grade` searches a grader's regex over rows joined by newlines. `:1156`
  `regraded`, `:1220` `unreproduced` and `:1274` `regrade` read
  `report_rows` too. `:980` `compare` refuses two sides whose suite trees
  differ. `:1023` `model` reads a record, never a side.
- `skills/code-review/scripts/chain_check.py:910` `finding_spans` splits
  the one `## Findings` section at its `### ` headings. `:819` `label_of`
  names a line's label. `:470` `SHARED_READER` is
  `skills/verify/scripts/unverified_check.py`, whose `readable` blanks
  fenced and commented lines. `:957` `findings` drops a finding it refuses,
  which is right for the check and wrong for a count of false findings.
- `evals/scripts/replay_targets.py:162` `record_reader` loads the check and
  its reader once; `:234` `labelled_round` and the table readers read a
  round record of either shape; `:368` `confirmed` reads the next round's
  confirmations; `:559` `targets` turns a round into a target with its
  base, branch and truths; `:662` `scaffold` fetches target and base.
- `evals/scripts/seed_defects.py:151` `targets` takes a shipped squash
  commit and its first parent; `:120` `seed` picks the first operator on a
  line `commit^1..commit` added in a Python unit; `:227` `scaffold`
  fetches the commit alone, mutates, `git rm`s the rounds and amends;
  `:249` `prompt`; `:266` `graders`.
- `evals/scripts/recurred_truths.json`: 17 entries, six of them for
  `seeded-279a580b` (two) and `seeded-9b644676` (four), applied by case name
  at the case's target by `replay_targets.py:501` `truths_with`.

**What breaks in six months.** Phase 1's reader is the check's split, so
the next change to the round record's grammar moves the harness with it in
the same commit, which is the point. The cost is that a grammar change also
changes the rows of every kept side when they are next read. Both sides of a
comparison are read by the same reader at `compare`, so they still compare;
a figure written in an old record and recomputed from its side later can
differ, and the record, not the side, is what was judged. Phase 2's cases
depend on round 1's target being fetchable from the repository's GitHub
remote. A pull request's head ref keeps its commits there today
(`git ls-remote origin refs/pull/879/head` answered, executed by the
framer), and a repository that deleted pull refs would stop the scaffold at
its fetch, loudly.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| S1. Keep the structure: the squash tree with its rounds removed, and the prompt saying the work item's records are withheld | The prompt tells the warden a fact about the setup that production never tells it, and a warden that still flags a dangling citation is not stopped by a sentence. A real dangling citation in a case is then suppressed by the same sentence. Whether the artefact rows fall is readable only by a paid run, so no free case proves the fix | Rejected. The premise that keeps the structure, that the `git rm` is needed so no verdict is inherited, was checked: `agents/warden.md` *Rules* already says earlier rounds carry coordinates, never verdicts |
| S2. Replace with the issue's reading: keep the squash tree and its shipped rounds, fetch the pull request's head so every cited commit resolves, and write the report to `round-<N+1>.md` | Round N's `target:` names a commit whose tree is the build without the seed, and the closing commits after it touch only records, so `git diff <round N target> HEAD` shows the seed in a few lines. The warden's step 7 runs the check over its record, which then owes every closed finding of round N a `confirms:`, `reopens:` or `regression:` line (`docs/the-review-record.md` *The round record*), so the case asks a verifying round's question. Records of the old table shape in the shipped rounds are refused by the check, which the warden reads as noise | Rejected: it measures a different question and leaks the answer |
| S3. Keep the squash tree and its shipped rounds, fetch nothing more, and write the report to `round-<N+1>.md` | The verifying-round obligation of S2 stands. The records cite `fixed <commit>` lines whose commits do not resolve, which is the other half of the artefact #971 classed (seeded-4d316179 r0.F2) | Rejected |
| S4. Build the case at round 1's target of the shipped work item, against round 1's base, with round 1's confirmed fixes as truths beside the seed | Round 1's target must be fetchable, which a deleted pull ref breaks (stated above). The six recurred truths of two seeded cases were read at squash commits and go. Round 1's target holds the defects round 1 found, which counted false would raise the seeded false rate, so they become truths by the replay rule | Chosen. The tree is the one the first review saw, so no citation dangles and no earlier round exists to owe a reference. Every claim of the fix is checked by a free scaffold run (spec S10) |
| S5. As S4, naming each case by its round 1 target | A stale `recurred_truths.json` entry would stop the generator, which fails closed. But the case name would name the original commit, which is the one object the seed must not be diffed against | Rejected for the squash name, which names the shipped item and an object the new clone never fetches |
| R1. Keep `FINDING_ROW` and make it skip fenced lines | A second statement of the grammar, which #1000 has already moved once. The next shape change drifts the harness from the check without a word, and the fault this issue names returns | Rejected under `CLAUDE.md` *The rule a mechanism is kept against*: a fact has one source |
| R2. Read through `chain_check.py#record_findings` | It drops every finding it refuses, so a warden writing a broken `location:` line lowers its own false-finding rate. That is the harness failing open on the number rule 2 reads | Rejected |
| R3. Split by `chain_check.py#finding_spans` over the shared reader's lines, one row per section, a refused section still a row | A record with two `## Findings` sections gives no rows, as the check's split does; the `shape-findings` grader does not catch that case | Chosen; the limit is the check's own |
| K1. Keep storing rows, now by the new reader | The defect again one level up: the next reader cannot be applied to sides that keep only this reader's output | Rejected |
| K2. Keep the printed record whole in the side | A side grows by the records' bytes, about 18 records a warden side. A record can hold a user path the identifier scan refuses, so the text is masked where the scan would refuse it (`questions.md` Q4) | Chosen |
| T1. Leave `truth-` results to the eval's whole-file search | A fenced line that matches a truth credits a find with no row behind it, so recall and the false rate are read by two readers | Rejected |
| T2. Grade `truth-` results from the reader's rows in `side_numbers` | The eval's own score, which still reads the whole file, no longer matches the record's numbers. Nothing reads that score | Chosen |

## Phases

Vertical slices: each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The reader.** The smith, in `evals/scripts/noninferiority.py`: the finding rows of a text by `chain_check.py#finding_spans` over the shared reader's lines, loaded as `replay_targets.py#record_reader` loads them; `annotate` keeping `report_text` in place of `report_rows`, masked by `questions.md` Q4; `side_numbers`, `regraded`, `unreproduced` and `regrade` reading rows and `truth-` passes from it (spec *Data & interfaces*); the refusal of a side without `report_text` in `compare` and `regrade`; `FINDING_ROW` and `report_rows` removed. Test-first in `tests/test_a_rewritten_definition_proved_non_inferior.py`: spec S1 to S7, and every case that builds a side by hand given `report_text`. `evals/README.md` (the sentence on what a side records, the `regrade` paragraph) and the module docstring rewritten in place. Done when every case below passes and no line of the tree outside `seal/` names `report_rows` or `FINDING_ROW` | S1 to S7 each seen red first, with the command and its exit in `phases/phase-1.md`; `mutation-check` red for the masked text read unmasked, for the refusal dropped, and for `truth-` passes taken from the eval again; `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; S7's executed command over `seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/baseline-warden.json` exit 2; `git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` empty; `ruff check` and `ruff format --check` on the touched `.py` files | ba469747 |
| 2 | **The seeded case.** The smith, in `evals/scripts/seed_defects.py`: targets read from round 1's record at each shipped squash commit through `replay_targets.py`'s readers; the seed chosen over `base..target`; the scaffold of spec *Data & interfaces*, with no `git rm`; round 1's confirmed fixes as truths beside `truth-seeded`; the case name kept as the squash's first 8 hex. The six seeded entries removed from `recurred_truths.json`. The four seeded cases regenerated with `--case` (`questions.md` Q3 for one that cannot be built). Test-first: spec S8 and S9, and the generator cases that name `seeded-279a580b` updated in place. `evals/README.md`'s `seed_defects.py` row and the stated point, the module docstring, and `changelog.md` in this directory written. Done when every regenerated scaffold has been run and every check of S10 holds | S8 and S9 seen red first; S10 executed once per case, network fetches included, each line in `phases/phase-2.md`; S11 `git status --porcelain evals/behaviour/` empty after regenerating; S12 `git rev-parse` of every other case tree equal at base and head; S13's `git grep`; `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; `ruff check` and `ruff format --check` on the touched `.py` files | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past
one, which someone can open.

The party that builds a phase fills its cell as the phase closes, not at the
end. A phase reconstructed afterwards is reconstructed from the diff, which is
where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. The party that builds the phase
writes it to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes.

Where feature branches squash, these commits stop resolving at the merge, and
**a rebase during the work does the same thing earlier and more quietly**,
because the orphaned object still answers `git cat-file` in the worktree that
wrote it. **The party that rebases the branch re-reads this column after the
rebase**, or the column names commits that resolve in one clone and nowhere
else. Nothing measures from this column, which is why that is tolerable.

## Operational impact

- **A new suite and a new reader, from a stated point.** From the squash
  commit that lands this work on `release/v0.22.3`, a warden comparison runs
  both sides on the new seeded cases, and both keep `report_text`.
  `compare` refuses a pair across that point twice over: the suite trees
  differ, and a side taken before it keeps no text. The changelog fragment
  says so.
- **No committed side can be compared or regraded again.** Their records
  stay, and `check` still recomputes them.
- **A warden side's JSON grows** by its printed records. No size limit in
  the tree applies to a side (executed by the framer: a `git grep` of
  `tests/`, `.github/scripts/` and `hooks/` for a byte or file-size cap
  found none outside the preload).
- **Phase 2's scaffold runs need network access** to the repository's
  GitHub remote, as every case's scaffold already does at an eval run.
- No new dependency and no new environment variable.
