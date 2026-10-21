# Feature Specification: the seeded scaffold hides the shipped rounds, and the harness reader miscounts findings (#986)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md holds WHAT this work
delivers and how we'll know. The policy documents in docs/ outrank this file;
the framer cites them and does not restate them. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | The proof of each fix is a case that runs for free. A paid side is scheduled only where no free reading answers, and by the orchestrator. The paid baseline is `questions.md` Q1, with a default the owner can overturn at the pull request |
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source. The harness stops spelling the round record's grammar as its own pattern and reads the record through the reader the check uses. The removed pattern and every text that stood on it leave in the same commit |
| `docs/the-review-record.md` *The round record*: "The record's grammar is the two tables below, and nothing else states it" | A finding is a `### <n>.` section of the one `## Findings` section, read from the lines `reader.readable` leaves, so a line in a fence or a comment is no line. The harness counts findings by that split and by no second pattern |
| `docs/the-review-record.md` *The round record*: "A squash orphans the commit after the merge" | A case built on a squash commit cannot hold the branch commits the shipped records name, however much it fetches by the squash. That is why the seeded case moves off the squash commit (`plan.md` *Alternatives considered*) |
| `agents/warden.md` *Order of work* steps 3 and 7, and `docs/the-review-record.md` *The round record*: "Every finding of round N at `fixed <commit>` or `rejected` is named by a `confirms:`, a `reopens:` or a `regression:` line of round N+1" | A warden handed a tree holding rounds 1 to N reads them and runs the check over its own record, which then owes every closed finding of round N a reference. A seeded case that kept the shipped rounds would ask a verifying round's question, not a first review's |
| `agents/warden.md` *Rules*: "Earlier rounds carry coordinates, never verdicts" | Read for the alternative that keeps the rounds: the definition already forbids inheriting a verdict, so the reason `seed_defects.py#scaffold` gives for its `git rm` ("so no earlier verdict is inherited") is not what decides the choice. The verifying-round question and the leak below decide it |
| `evals/README.md` *The behaviour suite*: "The cases are generated, never edited by hand" | Every seeded case reaches `evals/behaviour/warden/` through `seed_defects.py`. No case file is edited by hand |
| `evals/README.md` *The behaviour suite*, the `regrade` paragraph: "a change to a prompt, a scaffold or a `shape-` grader asks the agent something its runs never answered, and only a run measures that" | The new seeded scaffold makes a new suite. `noninferiority.py#compare` already refuses two sides whose suite trees differ, so no side taken before this work compares with one taken after it |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* (owner direction, binding) | Every sentence this work writes into `evals/README.md`, a docstring or a frame names who acts, when, on which file and what counts as done, uses no symbol as syntax in prose, and states each value once |
| `seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/spec.md` *Scope*, the two Out items | The source of both defects, and the precedent for the stated point: a suite change takes effect from a named moment, and figures under the old suite stay as they were judged |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file* | The changelog entry is `changelog.md` in this directory |

## What the issue's facts stand on, opened

**Defect 1 is in the seeded cases, not the replay cases** (executed
2026-10-22 by the framer). No `evals/behaviour/warden/replay-*/scaffold.sh`
runs `git rm`, and `replay_targets.py#scaffold` writes none. The four
`seeded-*/scaffold.sh` each end with `git rm -rq --ignore-unmatch
seal/specs/<item>/rounds` and an amend (`seed_defects.py#scaffold`). All 8
`remark (artefact)` rows of
`seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md`
are seeded cases: 279a580b, 4d316179 twice a side, 9b644676 and ad447367.

**"Fetches one commit" is the second half of the same cause** (executed
2026-10-22). The seeded scaffold fetches the squash commit alone. The
commits the shipped records name are branch commits, and a squash makes
none of them its ancestor: `git merge-base --is-ancestor e10a7c35 279a580b`
and the same for `be3c452a` exit 1. Both are ancestors of the pull
request's head, `refs/pull/879/head` at `5fd60565` (`git ls-remote origin`
and `git merge-base --is-ancestor` exit 0).

**The seeded scaffold also leaves the unmutated commit named in the clone**
(read; the framer ran no scaffold). The scaffold checks out the commit and
amends the mutation into it, and git writes both moves to the reflog by
default, so `git reflog` in the clone names the commit whose diff against
HEAD is the seed. Nothing in the tree records whether a run used it: the
traces of #957's sides are gone. This work closes it because it is in the
scaffold this work rewrites, and a later fix would make a second new suite
and a second baseline.

**"A finding written only into a verdict table" is the shape before #1000.**
Since #1000 a record holds no table a finding stands in: a finding is a
`### <n>.` section with labelled lines (`docs/the-review-record.md` *The
round record*). Read by that grammar, a finding exists only as a section. A
record that puts findings anywhere else has no section for them and fails
the `shape-findings` grader, which pass rule 3 reads.

**The fenced line is real today.** Every finding's paste-ready fix is a
fenced block (`templates/sdd-round.md`), and a fix to a round record is a
block of record lines. `FINDING_ROW` (`noninferiority.py:73`) matches
`^location: ` anywhere in the printed text, and so does every `truth-`
grader. #971 classed two such rows, both in `replay-1791382684-r2`.

**The committed sides keep matched lines only** (read). A run's
`specseal` holds `report_rows`, `cost` and `tool_calls`
(`noninferiority.py#annotate`). The printed record is in the trace, and the
traces are not committed, so no reader written later can be applied to any
committed side.

## Scope

**In.**

1. **The harness reads a round record by the grammar's own split.** In
   `evals/scripts/noninferiority.py`, a finding row is one `### <n>.`
   section of the one `## Findings` section of the lines `reader.readable`
   leaves, split by `chain_check.py#finding_spans`, loaded the way
   `replay_targets.py#record_reader` loads it. The row's text is the
   section's `location:` lines, or empty where the section has none. A
   section the check would refuse is still one row, so a finding written in
   a broken shape counts as false instead of vanishing. `FINDING_ROW` goes.
2. **A side keeps the record it was graded on.** Each run's `specseal`
   keeps the last printed record whole, as `report_text`, in place of
   `report_rows`. Rows are derived from it whenever a side is read, so a
   reader corrected later is applied to every side that keeps its text.
3. **Recall is read by the same reader.** Wherever `noninferiority.py`
   counts a side (`side_numbers`, `regrade`), a `truth-` grader's result
   for a run is its regex searched over that run's finding rows
   (`noninferiority.py#grade`), not the eval's search of the whole file. A
   fenced `location:` line then neither adds a row nor finds a truth.
4. **A side without `report_text` is refused, by name.** `compare` and
   `regrade` exit 2 on a side any run of which keeps no `report_text`,
   saying the side was read by the reader before #986 and cannot be read
   again. Every side committed before this work is one. Their committed
   records stay as they were judged, and `check` and `model`, which read a
   record and no side, still read them.
5. **The seeded case is built at its work item's round 1 target.** For a
   shipped squash commit, `seed_defects.py` reads the work item's round 1
   record at that commit, through the readers `replay_targets.py` already
   uses for both record shapes, and builds the case at round 1's target
   against round 1's base. The mutation lands on a line `base..target`
   added inside a Python unit. The tree is the one the real round 1
   reviewed: no round record exists in it, and every branch commit its
   files name is an ancestor of the target.
6. **The seeded scaffold fetches the target and the base, removes no file,
   and leaves no copy of the unmutated commit.** After the amend, the
   scaffold expires the reflog, removes `FETCH_HEAD` and prunes unreachable
   objects, so the target's original commit neither resolves in the clone
   nor is named by any file under its `.git/`. The `git rm` line goes.
7. **A seeded case's truths are the seed and round 1's confirmed fixes.**
   Built at round 1's target, the tree carries the defects round 1 found.
   Each finding round 1 closed `fixed` that round 2 confirmed is a `truth-`
   grader of the case, by `replay_targets.py`'s own rule for round 1, so a
   warden naming one is not counted false.
8. **The four committed seeded cases are regenerated under their names.** A
   case keeps the name `seeded-<first 8 hex of the shipped squash commit>`,
   which names the shipped item and no object the new clone holds. The
   smith regenerates `seeded-279a580b`, `seeded-4d316179`,
   `seeded-9b644676` and `seeded-ad447367` with `--case`. One that cannot be
   built is replaced by the next smallest shipped commit, and
   `phases/phase-2.md` says which and why (`questions.md` Q3).
9. **The six `recurred_truths.json` entries of the seeded cases go.** Their
   coordinates were read at the squash commits, and `truths_with` would
   apply them at the round 1 target by case name without a word
   (`replay_targets.py#truths_with`). A later classing of a side under the
   new suite derives entries for the new trees.
10. **Every text this changes, rewritten in place** (contract section 19):
    `evals/README.md` (what a side records, the `regrade` paragraph, the
    generator table's `seed_defects.py` row, and a sentence giving the
    stated point), and the module docstrings of `noninferiority.py` and
    `seed_defects.py`, with the `report_rows` and `report_shape` docstrings
    wherever they state the old reading.
11. **The changelog fragment**, `changelog.md` in this directory. It names
    the stated point: the squash commit that lands this work on
    `release/v0.22.3`. From it, a warden comparison runs both sides on the
    new seeded suite and keeps the record text in both, and no side taken
    before it compares with one taken after.

**Decided here, with the grounds where a reviewer can open them.** The full
list is the head of `questions.md`.

- The seeded case moves to round 1's target rather than keeping the shipped
  rounds (`plan.md` *Alternatives considered*, rows S1 to S4).
- The kept text is masked only where the repository's identifier scan
  would refuse it, and a `location:` path never starts with `/`, so masking
  a user path changes no row (`questions.md` Q4).
- The replay cases keep their scaffold. Their trees are a round's real
  target, earlier rounds and their commits included, and #971 classed no
  artefact row in them.

**Out, each with its reason and who answers it.**

- **The paid baseline.** By default it is not run in this work.
  `questions.md` Q1 is the owner's, with its price.
- **The eval's own whole-file truth search.** `claude plugin eval` still
  greps the report file, fences included, for its own score. The record's
  numbers no longer read that score (scope item 3), so it decides nothing.
  Changing the eval tool is not this repository's to do.
- **What the eval tool shows the session besides the clone.** Whether a
  case session can read its own `scaffold.sh` or graders is the eval
  tool's, and was the same before this work. The scaffold names the
  original target in its fetch line, as it named the squash commit before.
- **Re-reading the committed sides.** They keep rows and not the record,
  which is the defect itself. Nothing can recover the text.
- **The other agents' suites.** No smith, framer or sealer case prints a
  round record, so their rows are empty under both readers, and their case
  directories do not change.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a fenced location is no row | Given a printed record whose one finding's fenced fix block holds a `location:` line, when the side is read, then the run has one row, the finding's own `location:` line | A case in `tests/test_a_rewritten_definition_proved_non_inferior.py`, seen red against `FINDING_ROW` (two rows) |
| S2 a finding in a broken shape still counts | Given a finding section with no `location:` line, and another whose line reads `` location: `a.py#unit` ``, when the side is read, then each is one row and each is false | A case in the same module, seen red against `FINDING_ROW`, which misses the section with no `location:` line; and against `chain_check.py#record_findings` used as the reader, which drops both |
| S3 a location line outside a finding is no row | Given `location:` lines in `## Not judged`, in an HTML comment and above `## Findings`, when the side is read, then none is a row | A case, seen red against `FINDING_ROW` |
| S4 a truth matched only inside a fence is not found | Given a `truth-` grader whose pattern matches only the fenced line of S1, when the side is counted, then that grader passes no run and the row stays the one row | A case over `side_numbers`, seen red against the eval's recorded `passed` |
| S5 the reader is the check's | Given `chain_check.py#finding_spans` replaced by one returning no section, when a side is read, then it has no rows | A case with the function patched, seen red against a reader that does not call it |
| S6 the record is kept whole | Given a trace whose session printed two records with `cat`, when the side is annotated, then `report_text` is the last one, byte for byte, and the run carries no `report_rows` | The case `test_the_report_rows_are_the_last_report_the_session_printed`, rewritten in place and renamed for the text, seen red against the old `annotate` |
| S7 a side without the text is refused | Given a side any run of which has no `report_text`, when `compare` or `regrade` reads it, then it exits 2 and the message names the side and says it was read by the reader before #986 | One case per subcommand, seen red against the old code; and the executed command over `seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/baseline-warden.json` |
| S8 the seeded case is round 1's tree | Given a generator fixture whose shipped item has a round 1 record, when `seed_defects.py` writes the case, then the scaffold fetches round 1's target and base, checks out the target, holds no `git rm`, and ends with the reflog expired, `FETCH_HEAD` removed and unreachable objects pruned; the prompt names HEAD and round 1's base, and no commit of the unmutated tree | A generator case in the same module, seen red against the old `scaffold` |
| S9 the seeded truths include round 1's confirmed fixes | Given a round 1 record with one finding closed `fixed` that round 2 confirms, when the case is written, then the case holds that `truth-` grader beside `truth-seeded`, and no two truths accept one `location:` line | A generator case, seen red; `test_no_two_truths_of_a_warden_case_accept_one_location` over the regenerated suite |
| S10 the regenerated scaffolds run and hide nothing | Given each regenerated `seeded-*/scaffold.sh`, when the smith runs it in an empty scratch directory, then it exits 0; `git grep -n 'seal/specs/<item>/rounds/'` in the clone finds nothing; every commit named in the item's `plan.md` Status column resolves with `git cat-file -e`; `git cat-file -e <the target's original commit>` exits non-zero; and `grep -r <that commit> .git --exclude-dir=objects` finds nothing | Executed by the smith in phase 2 and written to `phases/phase-2.md`, one line per case. It fetches from the repository's GitHub remote and costs nothing |
| S11 the suite is generated | Given the generators and `recurred_truths.json`, when every warden case is regenerated, then `git status --porcelain evals/behaviour/` is empty | Executed by the smith |
| S12 only the seeded cases move | Given the base and the head, when the case trees are read, then every `replay-*` and `rule-*` case of the warden, and the `smith`, `framer` and `sealer` suites, are unchanged | `git rev-parse <base>:<dir>` equals `<head>:<dir>` for each (executed) |
| S13 the texts say what the code does | Given the diff, when `evals/README.md`, the two module docstrings and the changelog fragment are read, then they state the kept text, the grammar's split, the refusal, the round 1 tree and the stated point as built, and `git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` finds nothing | Read by the warden, and the `git grep` executed |

## Data & interfaces

**A run's `specseal` in a side** (`noninferiority.py#annotate`):
`report_text`, a string, the output of the last `cat <...>/round-N.md` (or
`<...>-report.md`) the case session ran without error, verbatim apart from
the masking of `questions.md` Q4; the empty string where the session
printed none. `report_rows` is no longer written. `cost` and `tool_calls`
are unchanged.

**The finding rows of a text.** A function of `noninferiority.py`, named by
the smith, returns one string per `### ` section that
`chain_check.py#finding_spans` finds over `SHARED_READER.readable(text)`:
that section's lines `chain_check.py#label_of` reads as `location:`, joined
by a newline, or the empty string. A record with no `## Findings`, or with
two, gives no rows, as the check's split does.

**Counting a side** (`noninferiority.py#side_numbers`). Rows and false rows
come from the finding rows of each run's `report_text`. A `truth-` grader's
passes come from `noninferiority.py#grade` over the same rows. Reach and
shape graders keep the eval's recorded results. A run with no
`report_text` raises the refusal of scope item 4, which `compare` and
`regrade` turn into exit 2.

**`regrade`.** Its own-suite check becomes: each `truth-` result the side
recorded equals that grader's regex over the whole `report_text`, which is
what the eval searched, so the kept text is shown to be the graded file.
Everything else in `regrade` is unchanged.

**A seeded case** (`seed_defects.py`). Its target is round 1's target and
base, read from the work item's `rounds/round-1.md` at the shipped squash
commit. Its scaffold, in order: `git init`, the remote, a fetch of the
target, a fetch of the base, the base ref where round 1 names one, a
checkout of the branch at the target, the mutation, the amend, then the
reflog expired, `FETCH_HEAD` removed and unreachable objects pruned, so no
copy of the original commit is left. Its prompt keeps its
present sentences with round 1's base. Its graders are `report_shape`'s,
`truth-seeded`, and round 1's confirmed fixes.

## Rule changes

- nothing
  why: the rules this work changes live in evals/README.md, outside the
    policy root, and are rewritten there in place by the build; no file of
    docs/ states the harness reader or the seeded scaffold.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The harness's own pattern for a finding row | `evals/scripts/noninferiority.py#FINDING_ROW` | The grammar's split, `skills/code-review/scripts/chain_check.py#finding_spans` over the shared reader's lines |
| The matched `location:` lines a side stored per run | `evals/scripts/noninferiority.py#report_rows` | `report_text`, the record kept whole; rows are derived from it when a side is read |
| Comparing or regrading a side that keeps rows and not the record | `evals/scripts/noninferiority.py#side_numbers` | Can go: such a side cannot be read by the reader again. Its committed record stays, and `check` still recomputes it |
| The removal of the work item's rounds from a seeded clone | `evals/scripts/seed_defects.py#scaffold` | Can go: the case is built at round 1's target, where no round record exists yet |
| The squash commit as a seeded case's tree | `evals/scripts/seed_defects.py#targets` | Round 1's target and base of the shipped work item |
| The six entries naming `seeded-279a580b` and `seeded-9b644676` | `evals/scripts/recurred_truths.json` | Can go: their coordinates were read at squash commits no case is built on. The next classed side under the new suite derives entries for the new trees |
| The case pinning the old reader | `tests/test_a_rewritten_definition_proved_non_inferior.py#test_the_report_rows_are_the_last_report_the_session_printed` | Rewritten in place for `report_text` (S6), under a name that says so |
| The four seeded case directories as generated today | `evals/behaviour/warden/seeded-279a580b/`, `seeded-4d316179/`, `seeded-9b644676/`, `seeded-ad447367/` | Rewritten by `seed_defects.py --case` under the same names; a case that cannot be built is removed and its replacement named in `phases/phase-2.md` |

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

Framed 2026-10-22 by framer, before the build.
