# Evals

Every case lives under `behaviour/<agent>/` and is run one agent at a time by
`scripts/noninferiority.py`. `claude plugin eval` reads a case at any depth
under `evals/`, so `tests/test_evals_layout.py` holds every case here to the
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

**A rewrite of an agent's preload is proved not worse by running this suite
on the old tree and on the new one, judged on outcome first and then on
cost.** `scripts/noninferiority.py run` runs one agent's cases on one side
and records, per run, the graders, the report's finding rows and the cost
its trace's `result` event carries (spend, seconds, tokens), beside the
preload's bytes. `compare` writes the record the five pass rules of
`noninferiority.py#verdict` judge, and
`tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes it.
Nothing in the tree makes a later edit owe a run.

**Every grader reads an outcome, never a sentence of a definition.** A
`truth-` grader is a real or seeded defect the report names, a `shape-`
grader is the work in the shape its next reader needs, and a `reach-` grader
is the session spawning the agent. No judge scores anything.

The cases are generated, never edited by hand. `--list` shows what a
generator can write, and `--case NAME` writes one case:

| Generator | Cases |
|---|---|
| `scripts/replay_targets.py` | `warden/replay-*`: a round record's target, each finding the next round confirmed fixed a `truth-` grader |
| `scripts/seed_defects.py` | `warden/seeded-*`: a shipped diff with one mutation in a unit it touched |
| `scripts/rule_cases.py` | `<agent>/rule-*`: a fixture repository the agent works in, graded on what it produced |

```bash
python3 evals/scripts/noninferiority.py run --agent warden --rev <merge base> \
  --out seal/specs/<id>/evals/baseline-warden.json
python3 evals/scripts/noninferiority.py compare --agent warden --phase N \
  --old seal/specs/<id>/evals/baseline-warden.json --new <new side>.json \
  --out seal/specs/<id>/evals/warden-phase-N.md
```
