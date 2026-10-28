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

**A rewrite of an agent's preload is proved not worse by running this suite
on the old tree and on the new one, judged on outcome first and then on
cost, each against the baseline and none against an absolute.**
`scripts/noninferiority.py run` runs one agent's cases on one side and
records, per run, the graders, the round record the session printed and the
cost its trace's `result` event carries (spend, seconds and `modelUsage`,
every model's tokens) and its tool calls (every `tool_use` block in the
trace, the session's and the agent's), beside the preload's bytes. The
record is kept whole as `report_text`, with each user path and host that
the `real_identifiers` census in `tests/censuses.py` refuses replaced by the
fixture one.
Whenever `compare` or `regrade` reads a side, a run's findings are the
`### ` sections of the record's one `## Findings` section, split by
`chain_check.py#finding_spans` over the lines its shared reader leaves, so a
`location:` line in a fence or a comment is no finding, and a finding in a
shape the check refuses still counts. A `truth-` grader over the round
record is graded on those findings, so recall and the false-finding rate
are read by one reader. `compare` writes the record the five pass rules of
`noninferiority.py#verdict` judge:

1. recall has not fallen, except by one find where every truth grader that
   lost it is still found by at least one new run;
2. the false-finding rate is within `FALSE_MARGIN` of the baseline's;
3. the shape and reach graders both sides ran, pooled, pass no fewer runs
   on the new side than on the baseline; one of them the new side failed on
   every run, where the baseline passed it at least once, fails the side by
   name; and one the baseline lacks passes every new run;
4. the preload is fewer bytes than the baseline's;
5. the tokens read across every model, the spawned agent's included, per
   tool call are fewer than the baseline's. The rewrite controls the context
   each call carries, and how many calls an agent makes is its behaviour,
   which rules 1 to 3 judge (`noninferiority.py#tool_calls`).

Total tokens, tokens per true find, spend and wall seconds are written in
the record and judge nothing. A side cut short, a case the baseline ran and
the new side did not, whatever its graders, a case run a different number
of times, a run whose `modelUsage` is missing or short of a count, or
one whose trace cannot be read or holds no tool call is no result, never a
pass.
`tests/evals/test_noninferiority.py` recomputes the record. Nothing in the tree
makes a later edit owe a run.

**A side already paid for is read again under another suite's truths
without a run.** `noninferiority.py regrade --side IN.json --suite-rev REV
--out OUT.json` grades each run of IN on REV's `truth-` graders, the
grader's regex searched over the run's findings. It writes OUT naming
REV's suite and the one IN's runs answered, which a side regraded again
keeps. It refuses, naming the case, a side whose own suite does not give
back, from each run's whole `report_text`, the truth results it recorded,
and a suite at REV that differs from IN's in anything but `truth-` graders
or holds other cases: a change to a prompt, a scaffold or a `shape-` grader
asks the agent something its runs never answered, and only a run measures
that.

**A side that keeps no `report_text` is refused.** `compare` and `regrade`
exit 2 on such a side, naming its file: it was taken before #986, it keeps
the rows the old reader matched and not the record, and no reader can read
it again. Its committed record stays as it was judged, and `check` and
`model`, which read a record and no side, still read it.

**A proofer comparison compares two sides taken from the same point.** The
squash commit that lands #986 on `release/v0.22.3` is that point for the
proofer's suite, whose directory carried the agent's earlier name until the rename: from it, both sides run the seeded cases built at round 1's
target and both keep `report_text`. No side taken before it compares with
one taken after it, and `compare` refuses such a pair twice over, since the
suite trees differ and the earlier side keeps no text.

**Every grader reads an outcome, never a sentence of a definition.** A
`truth-` grader is a real or seeded defect the report names, a `shape-`
grader is the work in the shape its next reader needs, and a `reach-` grader
is the session spawning the agent. No judge scores anything.

**No case tells the agent under test that the run is a measurement.** The
agent reads a case's `prompt.md` and works in the repository its
`scaffold.sh` builds, so neither file holds a word that names the run, its
graders or its cases as such. Two kinds of text are exempt: a record shape
this plugin's templates write, and a value a replay or seeded generator
copies from this repository into its case.
`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` holds the
words and the exemptions, and names each hit by its file, line and word.

The cases are generated, never edited by hand. `replay_targets.py` and
`seed_defects.py` take `--list` for what they can write, `--count N` for the
N smallest and `--case NAME` for one committed case again, read at every
release tag; `rule_cases.py` takes no selection and writes every fixture
case:

| Generator | Cases |
|---|---|
| `scripts/replay_targets.py` | `proofer/replay-*`: a round record's target, each finding the next round confirmed fixed a `truth-` grader |
| `scripts/seed_defects.py` | `proofer/seeded-*`: a shipped work item's round 1 target, against round 1's base, with one mutation in a unit the build added, amended into the target with the target's own committer and date, and neither a copy of the unmutated target commit nor a remote left in the clone; the mutated line is a `truth-` grader, and so is each finding round 1 fixed that round 2 confirmed |
| `scripts/rule_cases.py` | `<agent>/rule-*`: a fixture repository the agent works in, graded on what it produced |

All three also read `scripts/recurred_truths.json`. A real defect a case
did not list, named by at least two of the case's classed runs, is a
`truth-` grader of that case. A listed truth that a run found at a
coordinate its regex missed is widened with that coordinate. Each entry
names its case, the grader it adds or widens, its locations and the
classing rows it came from. Where the ±15 lines around a location would
reach another truth of the case, it also names a narrower `window`, because
no two truths of one case may accept the same `location:` line. An entry
the case cannot take stops the generator with exit 1.

```bash
python3 evals/scripts/noninferiority.py run --agent proofer --rev <merge base> \
  --out seal/threads/<id>/evals/baseline-proofer.json
python3 evals/scripts/noninferiority.py compare --agent proofer --phase N \
  --old seal/threads/<id>/evals/baseline-proofer.json --new <new side>.json \
  --out seal/threads/<id>/evals/proofer-phase-N.md
```
