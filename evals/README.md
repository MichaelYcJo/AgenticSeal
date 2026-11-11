# Evals

Every case lives under `behaviour/<agent>/` and is run one agent at a time by
`scripts/noninferiority.py`. `claude plugin eval` reads a case at any depth
under `evals/`, so `tests/behaviour/test_evals_layout.py` holds every case here to the
schema the runner reads: `max_turns`, `timeout_seconds`, `model` and
`allowed_tools` under `execution:`, where a top-level copy is dropped, and
`context.scaffold_script` the name of a file beside `case.yaml`, where an
inline script is refused.

Run the suite through `noninferiority.py run`, not through
`claude plugin eval .` directly. Inside the eval's sandbox on macOS the
system `git` is a stub that exits 72, and the installed plugin's `bin/` is on
`PATH`. `run` gives each session a `git` that works and puts the measured
tree's `bin/` first.

## The behaviour suite — `behaviour/<agent>/`

**The suite is a smoke run for gross breakage of an agent's output: `compare`
reads the new side's shape and reach graders against a recorded baseline
side.** A pass claims nothing about whether a rewrite is worse or means the
same, which the proofer's reading of the diff judges.
`scripts/noninferiority.py run` runs one agent's cases on one side and
records, per run, the graders' results, the cost its trace's `result` event
carries (spend, seconds and `modelUsage`, every model's tokens) and its tool
calls (every `tool_use` block in the trace, the session's and the agent's),
beside the preload's bytes. The trace itself, with the round record the
session printed, stays under `<out>.raw/` beside the side. Every grader, a
`truth-` grader among them, counts the result the eval recorded. `compare`
writes the record the three pass rules of `noninferiority.py#verdict`
judge:

1. the shape and reach graders both sides ran, pooled, pass no fewer runs
   on the new side than on the baseline;
2. none of them fails every new run where the baseline passed it at least
   once, and one that does fails the side by name;
3. a shape or reach grader the baseline lacks passes every new run.

The truth graders, the tokens read across every model, the spawned agent's
included, and those tokens per tool call are written in the record and
judge nothing, beside spend, wall seconds and the preload's bytes. The
preload's bytes are read with no run: `.github/scripts/release_report.py`
prints each agent's preload bytes against the last tag on every pull
request into `main`. A side cut short, a case the baseline ran and the new
side did not, whatever its graders, and a case run a different number of
times each give no result, never a pass.
`tests/evals/test_noninferiority.py` recomputes the record. Nothing in the tree
makes a later edit owe a run. A record written before #1487 carries header
rows `compare` no longer writes, which `check` and `model` read past.

**Two sides compare only over one suite.** `compare` refuses, with exit 2, a
pair whose trees of `evals/behaviour/<agent>/` differ, since a changed
suite needs a new baseline.

**Every grader reads an outcome, never a sentence of a definition.** A
`truth-` grader is a real or seeded defect the report names, a `shape-`
grader is the work in the shape its next reader needs, and a `reach-` grader
is the session spawning the agent. No judge scores anything.

**No case tells the agent under test that the run is a measurement.** The
agent reads a case's `prompt.md` and works in the repository its
`scaffold.sh` builds, so neither file holds a word that names the run, its
graders or its cases as such. A record shape this plugin's templates write
is exempt, and a replay or seeded case is not read, since its bytes are a
record.
`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` holds the
words and the exemption, and names each hit by its file, line and word.
The path of the tree `noninferiority.py run` loads is the base directory of
every skill the agent reads, so no component of it below the system
temporary directory holds one of those words either;
`tests/evals/test_noninferiority.py` *Test_run_side* refuses one that does.

The rule cases are generated, never edited by hand:
`scripts/rule_cases.py` takes no selection and writes every
`<agent>/rule-*` case, a fixture repository the agent works in, graded on
what it produced. The `proofer/replay-*` and `proofer/seeded-*` cases are
records: each is a review of a target at a recorded commit, with a `truth-`
grader for each defect it holds, and no script writes one again.

```bash
python3 evals/scripts/noninferiority.py run --agent proofer --rev <merge base> \
  --out seal/threads/<id>/evals/baseline-proofer.json
python3 evals/scripts/noninferiority.py compare --agent proofer --phase N \
  --old seal/threads/<id>/evals/baseline-proofer.json --new <new side>.json \
  --out seal/threads/<id>/evals/proofer-phase-N.md
```
