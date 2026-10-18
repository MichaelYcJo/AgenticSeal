# Feature Specification: rule 3 decides on the agent, not on one run (#966)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

No document under `docs/` states the evaluation's rules. Their one home is
`evals/README.md` §*The behaviour suite*, and the code that applies them is
`evals/scripts/noninferiority.py#verdict`.

| Policy clause | What it fixes for this work |
|---|---|
| #966 `## Decision` (owner, 2026-10-19) | **Rule 3 aggregates per agent.** A side's total shape and reach passes are compared with the baseline's, so one grader's one run cannot decide alone. A grader that fails every run of the new side, where the baseline passed it at least once, is still caught, and the reason names it. Chosen over `--runs 3` and over a per-grader tolerance of one run. Settled; this frame implements it and does not reopen it |
| #971 `## Decision` (owner, 2026-10-19) | The suite stays af9c924b's through 0.22.2. Nothing under `evals/behaviour/` changes here, and `--runs` keeps its default of 2 |
| `CLAUDE.md` §*The goal a design is chosen against* | The verdict decides #968's and #970's rewrites unattended. A rule one run can flip either way is a verdict a person has to re-read by hand, which is what this work removes |
| `CLAUDE.md` §*The rule a mechanism is kept against*, contract §19 | Every sentence stating the per-grader rule is rewritten in place, in the commit that changes the code. `git grep` on its words is how they are found (Scope, item 4) |
| contract §14, §15 | Each new reason line is pinned by a case, and each new or changed case is seen red before it is committed |
| `evals/README.md` §*The behaviour suite*, rule 3 | The text being rewritten. It now reads "each shape and reach grader passes on the new side at least as often as on the baseline, and one the baseline lacks passes every new run" |
| `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/phases/phase-2.md` §*The orchestrator closes the phase on the record as it reads* | The case that produced #966. Run 2 passed 70 of 72 shape and reach runs where the baseline passed 66. It read `fail` on one grader, `seeded-9b644676/shape-findings`, 1/2 against 2/2. The record stays as it was judged; this work does not rewrite #957's records |
| `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/guarantee.md`, rows "The eight committed side files…" and "Phase 2's two warden sides…" | The sealer ran `run --from-raw` and `cmp` and found the committed side JSONs byte-identical to what `run` writes from the raw output (executed by #957's sealer). That is why the re-read can start from those committed files |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below |

## Scope

**In.**

1. **Rule 3 in `noninferiority.py#verdict` becomes two checks**, applied to
   the shape and reach graders that both sides ran (old runs > 0 and new
   runs > 0):
   - **The total.** Sum the passes over every such grader, shape and reach
     pooled together, on each side. The new side fails rule 3 where its
     total is below the baseline's. The two sides share a denominator here,
     because a grader run a different number of times is already
     `no result` before rule 3 is reached (`verdict`, the
     "different number of times" check).
   - **The naming clause.** A grader that passed 0 of the new side's runs,
     where the baseline passed it at least once, fails rule 3 and is named,
     whatever the totals say.
2. **What stays as it is.** A shape or reach grader the baseline lacks
   stays outside the totals and keeps its present judgment: it must pass
   every new run. A grader only the baseline carried, inside a case both
   sides ran, stays unjudged. Rules 1, 2, 4 and 5, every `no result`
   condition, `--runs` and the suite are untouched.
3. **The reason lines** that a failing rule 3 writes under `Verdict:`
   (exact text under *Data & interfaces*), each pinned by a case (§14).
4. **Every text stating rule 3, rewritten in place** (§19):
   `evals/README.md` rule 3; the module docstring of `noninferiority.py`
   ("each shape and reach grader passing on the new side at least as often
   as on the baseline"); the `verdict` docstring ("3 each shape and reach
   grader passing at least as often"); and the names and comments of the
   rule 3 cases in `tests/test_a_rewritten_definition_proved_non_inferior.py`
   that describe a per-grader reading. A `git grep -n "at least as often"`
   in `evals/` and `tests/` afterwards finds no sentence stating the
   per-grader rule.
5. **#957's six records, read again under the new rule at no cost.** The
   input is #957's committed side JSONs. `compare` writes each new record
   into this work item's `evals/` directory as `957-<record>.md`. #957's own
   records are not rewritten.
6. **The changelog fragment**, `changelog.md` in this directory
   (`docs/the-record-layout.md` §*A change writes fragments, never a shared
   file*).

**Out, each with its reason.**

- **`noninferiority.py#cheaper_model`, the `model` subcommand.** It
  compares every grader per grader, truths included, and decides the
  sealer's model rather than a pass. #966's decision names rule 3 of
  `verdict`, and `cheaper_model` reads `verdict` only for `no result`, so it
  is unaffected. Whether it should follow is `questions.md` Q1, and the
  default is that it does not change.
- **`--runs` and the suite.** The owner chose aggregation over more runs,
  and #971 holds the suite fixed.
- **#957's committed records** (`seal/specs/1792126889-…/evals/*.md`). They
  are what #957's phases closed on. Rewriting them would make the record of
  that run say something it was never judged by. A side effect: `check` run
  on one of them now reports the stated verdict against the new
  computation. That is named under `plan.md` §*Operational impact*.
- **`.test_durations`.** It holds timing entries keyed by test id, already
  stale for one rule 3 case. It is pytest-split's input and nothing judges
  by it.
- **`run --from-raw`.** The issue names it as the means of the re-read. The
  raw output it reads is gone:
  `/Users/michael/Documents/GitHub/SpecSeal-worktrees/` holds only `976`,
  and a search of `/Users/michael` and `/private/tmp` six levels down finds
  no `957-*raw*` directory (read, 2026-10-19). It is also not needed:
  `compare` reads the saved sides, and those are committed (Grounding,
  guarantee row).

**A consequence of the decided statistic, stated so nobody meets it as a
surprise.** Where the baseline passes every run of every common grader,
nothing can offset a loss, so one run still decides. #957's sealer record
is that case: 29 of 30 against 30 of 30. It stays `fail` on rule 3 under
the new rule. This is the decision working as written, and it is not
reopened here.

## User scenarios & acceptance *(mandatory)*

The numbers are deltas over the `numbers()` fixture in
`tests/test_a_rewritten_definition_proved_non_inferior.py`. In that fixture
`c1/shape-report-exists` and `c1/reach-warden` are both `(kind, 2, 2, 2, 2)`,
read as old passed, old runs, new passed, new runs. `c1/shape-findings`
below is an added grader.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 · one grader's one run is offset | Given `shape-report-exists` 2/2 → 1/2 and `shape-findings` 1/2 → 2/2 (totals 5 and 5), when `verdict` runs, then `pass`. #957 phase 2's shape | A `CASES` entry. Seen red against the tree at 769f2aa4, which fails it |
| S2 · the total falls | Given `shape-report-exists` 2/2 → 1/2 alone (totals 4 → 3), then `fail`, and the reason is the total line naming `c1/shape-report-exists 1/2 against 2/2` | A `CASES` entry plus a reason assertion. Seen red with the total check deleted, when only the naming clause is left |
| S3 · the naming clause | Given `shape-report-exists` 2/2 → 0/2 and `shape-findings` 0/2 → 2/2 (totals 4 and 4), then `fail`, and the reason is the naming line for `c1/shape-report-exists` | A `CASES` entry plus a reason assertion. Seen red with the naming clause deleted |
| S4 · a grader the baseline never passed is not named | Given `shape-report-exists` 0/2 → 0/2 (totals 2 and 2), then `pass` | A `CASES` entry. Seen red against a naming clause that names every 0/n grader whatever the baseline did |
| S5 · shape and reach are pooled | Given `reach-warden` 2/2 → 1/2 and `shape-findings` 1/2 → 2/2 (totals 5 and 5), then `pass` | A `CASES` entry. Seen red against the tree at 769f2aa4, and against per-kind totals |
| S6 · a grader the baseline lacks does not offset | Given `shape-report-exists` 2/2 → 1/2 and `reach-sealer` (0 old runs) 2/2 on the new side, then `fail` on the total. The new grader passing every run is not counted | A `CASES` entry. Seen red against totals that include graders the baseline lacks |
| S7 · what stays | The existing cases keep their expected verdicts: a grader the baseline lacks, short of every new run, `fail`; a grader only the baseline carried, `pass`; a new side passing more often, `pass`; failing as often, `pass`; less often than a baseline that fails it (1/2 → 0/2), `fail`; every `no result` case. The two per-grader cases (shape and reach 2/2 → 1/2) keep `fail` and are renamed for what they now test, the total | `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q` exit 0 |
| S8 · the texts agree | Given the README, the module docstring and the `verdict` docstring, then each states the total and the naming clause, and none states a per-grader comparison | `git grep -n "at least as often" -- evals tests` shows no per-grader rule 3 sentence, read by the reviewer |
| S9 · #957 re-read | Given #957's committed `baseline-<a>.json` and `<a>-phase-N.json`, when `compare` writes `957-<record>.md` for all six, then each `## Graders` table equals #957's record's, and the verdicts are as below (predicted by the framer, confirmed by the phase) | Six `compare` runs; a diff of each `## Graders` section against #957's record; `check` on each new record shows no "it says … and its numbers give …" problem |

**S9's predicted verdicts.** The framer summed each committed record's
`## Graders` table (arithmetic over the tables, executed 2026-10-19; no
repository code ran). Phase 2 confirms or names the divergence.

| #957 record | As recorded | Shape + reach passes, old → new | Predicted under the new rule |
|---|---|---|---|
| `warden-phase-2.md` | `fail` (rule 3, one grader) | 66/72 → 70/72 | `pass` |
| `warden-phase-2-run-1.md` | `fail` (rule 3, five graders) | 66/72 → 66/72 | `fail`, rule 3 by the naming clause alone: `seeded-9b644676/shape-findings` 0/2 against 2/2 |
| `warden-phase-3.md` | `pass` | 66/72 → 70/72 | `pass` |
| `smith-phase-3.md` | `pass` | 48/48 → 48/48 | `pass` |
| `framer-phase-3.md` | `fail` (rule 5) | 64/64 → 64/64 | `fail`, rule 5 alone |
| `sealer-phase-3.md` | `fail` (rules 3 and 5) | 30/30 → 29/30 | `fail`, rule 3 on the total (`rule-sealer-untrue-body/shape-verdict` 1/2 against 2/2) and rule 5 |

Reach passes are equal on both sides of every record, so pooling and
per-kind totals give the same six verdicts.

## Data & interfaces

`verdict(numbers)` keeps its signature and its input. Only rule 3's part of
the `reasons` list changes. Rule 3's lines come in this order: the total
line, then the naming lines sorted by `(case, grader)`, then the existing
lines for graders the baseline lacks, sorted the same way.

The total line, written only when the new total is below the baseline's.
`N` is the sum of runs over the common shape and reach graders, the same on
both sides. The list holds every common grader whose new passes are below
its old ones, sorted:

```
shape and reach graders passed {new}/{N} runs on the new side, fewer than the baseline's {old}/{N} (rule 3): {case}/{name} {np}/{nruns} against {op}/{oruns}, …
```

The naming line, one per common grader with 0 new passes and at least one
baseline pass:

```
{kind} grader {case}/{name} failed every new run (0/{nruns}) where the baseline passed it {op}/{oruns} (rule 3)
```

The baseline-lacks line is unchanged:
`{kind} grader {case}/{name}, which the baseline lacks, failed on the new side ({np}/{nruns}) (rule 3)`.

`render`, `parse_record`, `check` and the record's tables do not change.
The totals are derived from the `## Graders` table, so `check` recomputes
them from a record with nothing added to it.

The re-read records: `seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/evals/957-<name>.md`
for `<name>` in `warden-phase-2`, `warden-phase-2-run-1`,
`warden-phase-3`, `smith-phase-3`, `framer-phase-3`, `sealer-phase-3`.
`--old` is #957's `evals/baseline-<agent>.json`, `--new` is #957's
`evals/<name>.json`, and `--phase` is the number in `<name>`.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The per-grader comparison of rule 3 for graders both sides ran | `evals/scripts/noninferiority.py#verdict`, the `elif oruns and np_ * oruns < op * nruns` branch and its reason line "passed {np_}/{nruns} on the new side, less often than the baseline's {op}/{oruns} (rule 3)" | Replaced by the total and the naming clause in the same function. The decision is #966's |
| The per-grader sentence of rule 3 in the README | `evals/README.md` §*The behaviour suite*, item 3: "each shape and reach grader passes on the new side at least as often as on the baseline" | Rewritten in place to the total and the naming clause. The clause about a grader the baseline lacks stays |
| The per-grader clause of the module docstring | `evals/scripts/noninferiority.py`, module docstring: "each shape and reach grader passing on the new side at least as often as on the baseline" | Rewritten in place |
| The per-grader clause of `verdict`'s docstring | `evals/scripts/noninferiority.py#verdict`: "3 each shape and reach grader passing at least as often" | Rewritten in place |
| The two case names asserting a per-grader reading | `tests/test_a_rewritten_definition_proved_non_inferior.py`, `CASES`: "rule 3: a shape grader passing less often than the baseline" and "rule 3: a reach grader passing less often than the baseline" | Same numbers and expected `fail`, renamed for the total they now exercise. Comments above other rule 3 cases that describe a per-grader reading are rewritten where they would read false |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-19 by framer, before the build.
