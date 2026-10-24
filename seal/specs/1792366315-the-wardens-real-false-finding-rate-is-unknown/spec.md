# Feature Specification: the warden's real false-finding rate is unknown (#971)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Every figure this work produces is re-read from what earlier runs already paid for. A paid run is scheduled only where no free reading can answer, and only by the orchestrator |
| `CLAUDE.md` §*The rule a mechanism is kept against* | A rule is kept for what its history shows it caught. Two wrong rows, one per side, show nothing a new rule would catch (step 3, `questions.md` Q1) |
| `evals/README.md` §*The behaviour suite*: "The cases are generated, never edited by hand" | Every truth this work adds reaches a case directory through `replay_targets.py`, `seed_defects.py` or `rule_cases.py`. No file under `evals/behaviour/` is edited by hand |
| `evals/README.md` §*The behaviour suite*: "Every grader reads an outcome … No judge scores anything" | The classing is done once by reading and committed as evidence. The harness keeps counting rows with regexes, and no model judges a finding |
| `docs/the-review-record.md` §*The round record*, the `location:` row of the grammar table (line 45) | A `location:` is backticked `path`, `path:line` or `path:first-last`. A truth never credits `path#unit`, which the check refuses (`tests/test_a_rewritten_definition_proved_non_inferior.py::test_a_truth_never_matches_a_coordinate_the_check_refuses`) |
| #971's `## Decision` (owner, 2026-10-19) | The new suite takes effect after 0.22.2 closes. #968, #970 and the milestone's closing verdict stay on af9c924b's suite. Until then the figures under both suites are recorded side by side, re-read at no cost |
| #968's body, guard 1 (*What an agent reads decides when it is measured again*) | The warden's preload at the tree this work starts from is not the one its last side measured, so any change to the warden owes a new baseline run (`questions.md` Q1) |
| `seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/spec.md` §*Scope* item 5 | The precedent for a free re-read: committed side JSONs in, new records into this work item's `evals/`, earlier records left as they were judged |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | The changelog entry is `changelog.md` in this directory |

## What the issue's step 1 stands on, opened

The issue says step 1 reads the kept raw output in
`SpecSeal-worktrees/957-baseline-raw/` and `957-phase-3-raw/`. **Neither
exists** (executed 2026-10-19: `ls SpecSeal-worktrees/` lists `971` and
`976` only; the traces the sides name under `/private/tmp/e-*/` are gone).

What the tree does hold, opened and executed on 2026-10-19:

- `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/baseline-warden.json`
  and `warden-phase-3.json` carry, for each of the 18 runs a side, the
  graders' results and `specseal.report_rows`: the `location:` lines of the
  last round record the run printed, verbatim and in order.
- Recomputed from those rows with `side_numbers`' own truth test: baseline
  55 rows, 43 false; phase 3 47 rows, 31 false. These are the records'
  figures. The per-case false counts are the ones the issue's first comment
  gives (7, 12, 1, 0, 2, 7, 2, 7, 5 and 9, 7, 0, 0, 2, 4, 2, 6, 1).
- Every truth grader's recorded result is reproduced by matching its regex
  against the run's joined `report_rows`: 24 of 24 results a side, no
  disagreement. So a side can be re-graded under another suite's truths
  from the committed JSON alone.

**What the committed sides lack:** the finding's text (its title, claim and
severity) and the round record around the `location:` line. The case's diff
is not lost: each case's `scaffold.sh` names the commits it fetches, and
they resolve in this repository.

**What substitutes:** the issue's first comment is the classing, done while
the raw output existed (it says its row counts were executed against the
traces). Its finding column is the only surviving paraphrase of each
finding's text, and this work labels it as such. Each of its rows is tied
to a committed `report_rows` line by side, case, run and location. A class
whose reason rests on a fact about a tree (a file present or absent, a
command's exit code, a line's content) is re-checked at the case's commits.
A class that rests on the finding's wording alone cannot be re-checked by
anyone, and the record says so row by row.

## Scope

**In.**

1. **The classing, in the tree and tied to the committed rows.** Every one
   of the 74 false rows (43 baseline, 31 phase 3) is one row of
   `evals/false-rows.md` in this directory. Each row carries the side, the
   case, the run index, the row index within the run, the `location:` line
   verbatim from the side JSON, the class, and the reason. The class
   vocabulary is the comment's: `real`, `real (truth-miss)`, `remark`,
   `remark (artefact)`, `remark (fenced)`, `wrong`, `unclear`. The finding
   column is labelled as the comment's paraphrase. Every row whose class
   rests on a fact about a tree is re-checked at the case's commits, and
   the command and its result go in the row. The comment's own
   reclassification (phase 3, seeded-ad447367 r1.F2, to `remark
   (artefact)`) is the one carried.
2. **`noninferiority.py regrade`**: a side re-graded under the truth
   graders of another suite revision, from its committed `report_rows`,
   with no eval run. It refuses where the side's own suite cannot be
   reproduced from its rows, and where the two suites differ in anything
   but `truth-` graders (*Data & interfaces*).
3. **The real defects that recurred become truths, through the
   generators.** A defect is a new truth where the classing calls it `real`
   and at least two of the four runs of its case (two runs a side, both
   sides) named it. A `real (truth-miss)` row widens the existing truth it
   belongs to with the coordinate it gave, where that coordinate is a form
   the grammar allows. One committed input file lists every truth this work
   adds or widens, with the classing rows it came from, and the three
   generators read it. The warden's cases are regenerated from it.
4. **The figures under both suites, side by side.** Both committed warden
   sides are re-graded onto the new suite and committed in this
   directory's `evals/`, and `compare` writes their record there. A table
   in `evals/false-rows.md` gives, for each side, the harness false rate
   under af9c924b's suite and under the new one, and the real false rate
   by class.
5. **Every text this changes, rewritten in place** (§19):
   `evals/README.md` (the generator table's truth sources, `regrade` beside
   `run --from-raw`), the module docstrings of `noninferiority.py`,
   `replay_targets.py`, `seed_defects.py` and `rule_cases.py` where they
   state what a truth is.
6. **The changelog fragment**, `changelog.md` in this directory. It states
   the point from which the new suite is the one comparisons use: the
   release after 0.22.2.

**Decided here, with the grounds where a reviewer can open them.** The full
list is the head of `questions.md`.

- *Recurs across runs* means at least two of the four runs. This is the
  smallest count the word allows. Every candidate in the comment's
  *candidates for new truths* table meets it.
- A known limit the shipped round left standing (seeded-9b644676's
  `TypeError` on a non-object `plugin.json`, its bare product-host prefix)
  is a truth. `evals/README.md` says a `truth-` grader is "a real or seeded
  defect the report names". A limit somebody chose to leave is still a
  defect.
- A different defect at another coordinate is its own grader, never a
  widening. seeded-9b644676's test that does not pin the source text is a
  defect in the shipped tests, not the seeded mutation, so crediting it
  through `truth-seeded` would count one find as another.
- seeded-279a580b r0.F1 wrote `chain_check.py#note_rows (line 1876)`. The
  grammar refuses that form, so no grader is widened to credit it, and the
  row stays false under both suites. That is a shape fault in the record,
  not a miss by the grader.

**Out, each with its reason and who answers it.**

- **Step 3, a rule for the warden.** By default it is not built in 0.22.2.
  The two `wrong` rows have different causes, and neither shows a rule the
  definition lacks: the baseline's is an uncovered-test claim made without
  the coverage probe `agents/warden.md` §*Runs are narrow* already orders,
  and phase 3's judges a 0.21-era target by the 0.22 record grammar that a
  replay case puts in front of it. One row a side cannot show that a rule
  works, and a rule added to the preload fails rule 4 unless it removes
  more bytes than it adds. Building it anyway is `questions.md` Q1, the
  owner's, with its cost.
- **The scaffold's artefacts** (8 rows: `scaffold.sh` runs `git rm` on the
  item's `rounds/` and fetches one commit, so citations of the shipped
  rounds look dangling). The fix is in the scaffold, and it changes what
  the warden sees. A side under a changed scaffold cannot be re-read from
  the rows of a side run without it, so it is a new suite with a paid
  baseline. The answerer is the repository owner, as an issue for the
  release after 0.22.2. The orchestrator carries this in its hand-back.
- **The harness reader's two faults** (`FINDING_ROW` counts a `location:`
  line inside a fenced block; a finding written only into a verdict table
  is not counted). The committed rows keep only the matched lines, so a
  corrected reader cannot be re-applied to them, and two sides read by
  different readers do not compare. The answerer is the repository owner,
  in the same issue as the scaffold.
- **Rule 2 itself** (`FALSE_MARGIN`, or a numerator other than the harness
  count). The issue asks for the suite's truths, not a new rule. The
  harness rate stays the number rule 2 reads.
- **A generic replay rule that makes every historical ⬜ answered with a
  correction a truth.** It would add truths no run recurred on, beyond
  what the issue asks, and it depends on parsing old record shapes nobody
  has measured. `plan.md` §*Alternatives considered* weighs it.
- **#957's committed sides and records** (`seal/specs/1792126889-…/evals/`).
  They are inputs, and they stay as they were judged.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 every false row is classed once | Given the two committed warden sides and af9c924b's truths, when the false rows are listed, then `evals/false-rows.md` has exactly one row for each of the 43 + 31, and each row's `location:` equals the side JSON's line byte for byte | One command, written in `phases/phase-1.md`, that joins the table to the JSON rows and exits 0 only on an exact cover. The smith runs it (executed) and the warden re-runs it |
| S2 a class resting on a tree fact is re-checked | Given a row classed `wrong`, `unclear`, any `remark`, or `real` that becomes a truth, when its reason cites a fact about a tree, then the row names the command run at the case's commit and what it gave | Read: the warden opens every `wrong` and `unclear` row and a sample of the rest, and reruns the named command |
| S3 a side re-graded onto its own suite is unchanged | Given `baseline-warden.json` or `warden-phase-3.json`, when `regrade --suite-rev af9c924b` runs, then every run's truth results and the side's rows and false count (55/43, 47/31) are the ones recorded | A case in `tests/test_a_rewritten_definition_proved_non_inferior.py` over a fixture side, seen red (§15), plus the executed command over both committed sides |
| S4 regrade refuses what it cannot stand in for | Given a side whose rows do not reproduce its own recorded truth results, or a target suite that differs from the side's in a non-`truth-` file of a case, when `regrade` runs, then it exits 2 and names the case | Cases in the same module, each seen red |
| S5 a new truth is real and recurred | Given both sides re-graded onto the new suite, when each added or widened truth grader is matched, then it matches rows in at least two runs, and every row it turns from false to found is classed `real` or `real (truth-miss)` in `evals/false-rows.md` | One command in `phases/phase-3.md` joining the re-graded sides to the classing. It exits 0 only when both conditions hold |
| S6 the suite is generated | Given the input file and the generators, when each warden case is regenerated, then the committed case directory is what the generator writes, byte for byte | `git status --porcelain evals/behaviour/` empty after regenerating (executed). Generator cases for an added truth, a widened truth and an entry naming no case, each seen red |
| S7 only the warden's suite moves | Given the base and the head, when the suite tree of each other agent is read, then it is unchanged | `git rev-parse <base>:evals/behaviour/<a>` equals `<head>:…` for `framer`, `smith` and `sealer` (executed) |
| S8 0.22.2 decides on af9c924b's suite | Given this work merged into `release/v0.22.2`, when a 0.22.2 record decides a pass, then it compares sides on af9c924b's suite; a record on the new suite in this directory is labelled side by side and decides nothing | Read: the changelog fragment and `evals/false-rows.md` state it, and S7 shows the framer's and the scribe's issues cannot meet the new suite |
| S9 the figures stand side by side | Given the re-graded sides, when the table is read, then each side shows the harness false rate under both suites and the real false rate by class, each recomputable | The S1 and S5 commands, and `noninferiority.py check` recomputing the new-suite record's verdict from its numbers (executed; a verdict other than `pass` there is recorded and decides nothing) |
| S10 the texts say what the code does | Given the diff, when `evals/README.md` and the four docstrings are read, then they state the truth sources and `regrade` as built, and no sentence states a truth as only *a finding the next round confirmed fixed* where the generator now also reads the input file | Read, and a `git grep` named in `phases/phase-3.md` |

## Data & interfaces

**`evals/false-rows.md`** (this directory). One table, one row per false
row:

`| Side | Case | Run | Row | location: (verbatim) | Class | Finding (the comment's paraphrase) | Reason, and the command re-run |`

Under it, the totals by class for each side, and the side-by-side figures
(S9).

**The input file of added truths.** One JSON file, beside the generators
(`evals/scripts/`). The name is the phase's to choose. Each entry has:

- `case`: the case directory name;
- `grader`: a new name (`truth-<slug>`) or the name of an existing truth it
  widens;
- `finding`: one sentence, which becomes the grader's body;
- `locations`: `path`, `path:line` or `path:first-last` at the case's
  target, each turned into a pattern by `replay_targets.py#truth_pattern`
  and joined as alternatives;
- `from`: the `evals/false-rows.md` rows it came from.

An entry naming a case the generators do not write, or an existing grader
the case does not have, stops the generator with exit 1. This keeps the
file from going stale silently. Its coordinates are at fixed historical
commits, so nothing in it has to be kept in step with the tree.

**`noninferiority.py regrade --side IN.json --suite-rev REV --out
OUT.json`.** It writes IN with each case's `truth-` graders replaced by
REV's (`git show REV:evals/behaviour/<agent>/<case>/graders/truth-*.md`).
Each run's result for each of them is the grader's regex searched, with
`re.M`, over the run's `report_rows` joined by newlines. It also writes
`specseal.suite_rev` and `suite_tree` as REV's. Exit 0 written; 2 when IN
does not reproduce its own recorded truth results from its rows, when REV
changes a case's files other than `truth-` graders, or when IN and REV do
not hold the same cases, naming the case each time. `compare`, `check` and
`side_numbers` are unchanged.

**The re-graded sides and their record** (this directory's `evals/`):
`baseline-warden-<rev>.json`, `warden-phase-3-<rev>.json` and
`971-warden-phase-3-<rev>.md`, where `<rev>` is the first eight hex digits
of the commit that lands the new suite.

## Rule changes

- nothing
  why: internal: each false row is classed and a side is graded again, held by
    tests/test_a_rewritten_definition_proved_non_inferior.py.

## Removes

nothing — the work adds truths, a subcommand and records. Every sentence it
amends (the README's truth sources, the generators' docstrings) is
rewritten in place under §19, and no reader, rule, check or copy leaves the
tree.

## Open questions → questions.md

Framed 2026-10-19 by framer, before the build.
