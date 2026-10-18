# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c2544c8f67e96a766d064d0c2b246c0d72326b6a |


## What this phase was asked

`plan.md`'s row 1, the suite, as a build phase with no paid run:

- Change the sealer cases' scaffolds through their generator,
  `evals/scripts/rule_cases.py`. Each one writes a `broad-gate.md` at HEAD and
  commits it.
- Add the new case `rule-sealer-no-gate`.
- Put the `shape-runs-no-broad-gate` grader on every sealer case.
- Add the test that the committed cases are the generator's output (S11), and
  extend `sealer_grade_gaps` (T6).

The verdict words stay `sound` / `not sound` / `undecidable`. The cases are
generated and never edited by hand. Every new or changed case is seen red
first, with its exit named. The commit that closes this phase is the
`--suite-rev` of every step-A comparison.

Verify: the generator's output equals the committed cases;
`bin/test tests/test_evals_layout.py tests/test_a_rewritten_definition_proved_non_inferior.py -q`;
`bin/rules --check`; ruff on the changed `.py` files.

## What this phase found

**The suite revision for phases 2 and 4 is `c2544c8f`.** Its `evals/` tree
is `5ec89a37`, the same object as at `b06ff00b`, the commit that regenerated
the cases. The commit between them changes `tests/` alone, so passing either
one as `--suite-rev` gives the same suite (`executed`:
`git rev-parse c2544c8f:evals b06ff00b:evals`).

**The suite as it now stands** (`executed`, the generator's own count line):
four sealer cases, 27 graders (4 reach, 20 shape, 3 truth). Before this
phase there were 17. `rule-sealer-sound` carries 6 graders, and each of the
other three carries 7.

**Which commit the record names.** The row reads
"`$build against $(git rev-parse main)` … so the run's SHA is followed by one
records-only commit". Those two halves disagree. `$build` is the fix commit,
and two records-only commits follow it: the phase record and round commit,
then the `broad-gate.md` commit. The scaffold names the commit the records
were written at (`run=$(git rev-parse HEAD)` after the docs commit), so
exactly one commit follows the run: the record's own. That is the stated
property, and it is also the order `spec.md` §*The act, as this item leaves
it* gives: the gate runs once the pull request body and the changelog are
written. Under either reading the rule accepts the record. The divergence is
recorded in `overview.md`.

**The record the three gated cases write is the one the rule accepts**
(`executed`, a probe since deleted). Each of the four regenerated
`scaffold.sh` files was run in a scratch repository, exit 0 each, with a
clean status after it. `chain_check.broad_gate(SHARED_READER, root, item,
"main")` returned `[]` for `sound`, `untrue-body` and `false-red`. For
`no-gate` it returned the absent-file problem. The record has
`broad_gate.write_gate_file`'s shape, except that the scaffold writes full
SHAs where the script writes short ones; `newest_run` reads either.

**How each new or changed case was seen red** (`executed`, exit codes read
directly):

| Case | Red against | Exit |
|---|---|---|
| T6 `test_every_sealer_case_grades_the_guarantee` (extended) | the three committed cases before regeneration: three gaps, `no grader bounds broad-gate --base at zero` | 1 |
| T5 / S11 `test_the_sealer_cases_are_the_generators_output` (new) | the changed generator before regeneration: `only in the generator's output: …/shape-runs-no-broad-gate.md`, `rule-sealer-no-gate/…` | 1 |
| `test_a_bound_on_the_sealers_run_that_is_not_zero_is_a_gap` (new) | `sealer_grade_gaps` without its `max: 0`, its `tool: 'Bash'` or its `--base` condition, one `mutation-check` each | 1, 1, 1 |
| `test_each_way_a_committed_case_leaves_the_generator_is_named` (new) | `case_differences` without its `differs`, `only in the tree` or `only in the generator's output` branch, one `mutation-check` each | 1, 1, 1 |
| the eval graders `truth-no-gate` and `shape-runs-no-broad-gate` | their patterns, in the deleted probe. `^Verdict:.*no broad run` (flags `mi`) matched `Verdict: not sound — no broad run at HEAD` and did not match `Verdict: sound`, a reason naming the PR body, or `no broad run` above a bare verdict. `broad-gate\s+--base` matched `broad-gate --base main --record …` and did not match `broad-gate --preflight --base main` or a `cat` of `broad-gate.md` | probe exit 0, 0 unexpected |

**Mutation of the generator and the committed cases** (`executed`,
`mutation-check`, every result `red`, exit 1 from the cases):

- a committed grader's body edited by hand → S11;
- the committed `shape-runs-no-broad-gate`'s pattern loosened to
  `broad-gate` → T6;
- the generator's `input_match` loosened, `if gate:` made `if True:`, the
  no-gate truth pattern cut to `^Verdict:`, and the run's commit made
  `HEAD~1` → S11, each one alone.

The first pass left two survivors. Without its `max: 0` condition, T6's
reader still passed on the tree. Without its `differs` branch, S11's reader
did too. The tree holds no instance of either defect, so nothing exercised
those branches. The two fixture cases above were added in `c2544c8f` for
that reason, and both mutations went red against them.

**What a no-gate run measures on the baseline** (`read`, not run). The
sealer at `2fc33333` runs `broad-gate --record` as its own first act. On
`rule-sealer-no-gate` that run is expected to write `broad-gate.md` itself
and seal the item, which fails `truth-no-gate`. On every case it fails
`shape-runs-no-broad-gate`. Those graders are added before the baseline,
so both sides run them (`plan.md` Alternatives, row 6). Phase 2's record is
where this is measured.

**What was left as it stands:**

- The warden, smith and framer `rule-*` cases also equal the generator's
  output today (`executed`, `diff -r` per directory, no difference).
  Nothing pins them, because S11 covers the sealer only, as the row asks.
- `chain_check.broad_gate`'s absent-file message still says the sealer runs
  the gate. That is `chain_check.py:1570`, which belongs to phase 3.
- `agents/sealer.md`'s `Enforced by:` lines do not yet name
  `rule-sealer-no-gate`. The rule it enforces is written in phase 3.

**The class grep for the sentences this phase changed** (`executed`,
`git grep -n -F` over `tests evals docs skills agents README.md README.ko.md
CONTRIBUTING.md`, generated cases excluded). For `three reviewed items`, `no
write but that file`, `naming what the tree contradicts`, `SEALER_RUNS`,
`sealer_case(`, `rule-sealer-`, `graders each`, `three sealer` and `three
cases`, it found no other description of the sealer cases. The hits outside
the generator are `README.md:42`, whose sealer row belongs to phase 3, and
`agents/sealer.md:115,121,133`, which are `Enforced by:` paths that still
resolve.
