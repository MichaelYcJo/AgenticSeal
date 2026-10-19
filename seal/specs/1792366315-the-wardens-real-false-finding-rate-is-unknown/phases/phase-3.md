# 1792366315-the-wardens-real-false-finding-rate-is-unknown — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 864798a4 |


## What this phase was asked

Add truths through the generators: one input JSON that the three
generators read, and the warden's cases regenerated from it.

- First, with nothing changed, regenerate the nine existing cases byte for
  byte. That run answers `questions.md` Q3, and this record states the
  answer.
- The other agents' suite trees stay unchanged.
- Every new truth matches in at least two runs.
- Every row that turns from false to found is one phase 1 classed `real`.
- A regrade onto this phase's commit is refused if any warden case file
  other than a `truth-` grader changed.
- Check whether `tests/test_evals_layout.py` allows the input JSON where it
  is put.

Close with this record and the Status cell. No paid runs.

## What this phase found

**`questions.md` Q3: an empty diff (executed).** At 9ff7bbca, with nothing
changed, these regenerated the nine warden cases:

- `replay_targets.py --case` for the four replay cases;
- `seed_defects.py --case` for the four seeded cases;
- `rule_cases.py`, which writes every agent's fixture cases.

All three exited 0, and `git status --porcelain evals/behaviour/` printed
nothing. The committed suite is what its generators write.

**`questions.md` Q2: only in the text (read).** The historical round 2
record of 1791382684 holds one coordinate in each Location cell. Its
finding 1 is at `correction_check.py:780` and its finding 2 at
`hooks/routing.py:415`. The units are in the finding text and the fix
block. So the input file widens the two graders, and `overview.md` carries
the divergence row Q2 asks for. truth-1 gains the eight units of the
record's list that the runs cited. truth-2 gains `unverified_check.py:767`,
the unit whose class the record puts in its finding 2. A unit the runs
cited that the record does not list, such as `hooks/dispatch.py:449`, is not
added.

**What was built** (commits 953f7386 and 864798a4).

- `evals/scripts/recurred_truths.json` holds 17 entries: 15 new truths and
  2 widenings.
  - replay-1791382684-r2: truth-1 and truth-2 widened; truth-step-refused,
    truth-mapping-same-script and truth-inspect-reads added.
  - replay-1791382684-r5: truth-direction-quoted, truth-changelog-history,
    truth-acceptance-exits-1, truth-old-phrase-kept and
    truth-direction-unplaced added.
  - rule-warden-one-finding: truth-shout-twice-uncovered added.
  - seeded-279a580b: truth-sdd-cutoff and truth-cutoff-in-docs added.
  - seeded-9b644676: truth-no-commit-unpinned, truth-host-prefix,
    truth-manifest-not-object and truth-docstring-pipeline added.
- Each entry's `from` names its rows in `evals/false-rows.md` as `side case
  run row`.
- `replay_targets.py` gained `recurred_truths` and `truths_with`.
  `truth_pattern` now wraps the new `truth_option`, and its bytes are
  unchanged: the regeneration with an empty input file gave an empty diff
  (executed).
- `seed_defects.py#graders` and `rule_cases.py#warden_case` apply the
  entries through `truths_with`, beside their own truths.
- The README's generator paragraph and the docstrings of the three
  generators state the new truth source. A `git grep` for the texts
  stating what a truth is found no other place. The README's sentence that
  a `truth-` grader is a real or seeded defect still holds.

**`tests/test_evals_layout.py` allows the input JSON in `evals/scripts/`
(executed and read).** The test finds a case as a directory holding
`case.yaml` or `prompt.md` (`case_dirs`), so a JSON file beside the
generators is no case and nothing there is checked against it. The module
passed with the file in place, before and after it was filled. The
encoding, lint and real-identifier modules, which read every tracked file,
passed too. The runner reads only `--eval-dir evals/behaviour/<agent>`, so
it never meets the file.

**The suite moved only where it should (executed).**

- `git diff --name-only 8a100e13 864798a4 -- evals/behaviour` lists only
  `graders/truth-*` files. So the regrade refusal on non-truth files cannot
  meet this commit, and both sides regrade onto it.
- The framer's, smith's and sealer's suite trees are the same hash at
  8a100e13 and at 864798a4. The scribe has no suite at either.
- Regenerating every case a second time at 864798a4 left `git status
  --porcelain evals/behaviour/` empty (S6).

**The S5 join (executed: it printed `problems: 0` and exited 0 at
864798a4).** It regrades both committed sides onto the new suite with
`noninferiority.py#regrade`, in a temporary directory. Then it holds two
conditions. Every row that turns from false to found must be classed `real`
or `real (truth-miss)` in `evals/false-rows.md`, and no row may go from
found to false. Every entry's grader must pass in at least two runs. Run it
from the repository root:

```sh
python3 - <<'PY'
import argparse, json, os, re, sys, tempfile
sys.path.insert(0, "evals/scripts")
import noninferiority as ni

REV = "864798a4"
E = "seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/"
SIDES = {"baseline": E + "baseline-warden.json", "phase 3": E + "warden-phase-3.json"}
TABLE = "seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md"
REAL = ("real", "real (truth-miss)")

classes = {}
with open(TABLE, encoding="utf-8") as f:
    for line in f:
        c = [x.strip() for x in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(c) == 8 and c[0] in SIDES:
            classes[tuple(c[:4])] = c[5]
with open("evals/scripts/recurred_truths.json", encoding="utf-8") as f:
    entries = json.load(f)


def false_rows(result):
    out = set()
    for case in result["cases"]:
        name = case["dir"].rsplit("/", 1)[1]
        found = [re.compile(g["config"]["pattern"], re.M) for g in case["graders"]
                 if ni.kind(g["name"]) == "truth" and g.get("type") == "regex"]
        runs = [r for arm in case["arms"].values() for r in arm]
        for i, run in enumerate(runs):
            for j, row in enumerate(run["specseal"]["report_rows"]):
                if not any(t.search(row) for t in found):
                    out.add((name, str(i), str(j)))
    return out


problems, runs = [], {}
with tempfile.TemporaryDirectory() as d:
    for side, path in SIDES.items():
        out = os.path.join(d, "side.json")
        if ni.regrade(argparse.Namespace(side=path, suite_rev=REV, out=out)) != 0:
            problems.append(f"{side}: regrade onto {REV} refused")
            continue
        with open(path, encoding="utf-8") as f:
            old = json.load(f)
        with open(out, encoding="utf-8") as f:
            new = json.load(f)
        for name, i, j in sorted(false_rows(old) - false_rows(new)):
            cls = classes.get((side, name, i, j))
            if cls not in REAL:
                problems.append(f"{side} {name} run {i} row {j}: found now, classed {cls}")
        for name, i, j in sorted(false_rows(new) - false_rows(old)):
            problems.append(f"{side} {name} run {i} row {j}: found before, false now")
        for case in new["cases"]:
            name = case["dir"].rsplit("/", 1)[1]
            for run in [r for arm in case["arms"].values() for r in arm]:
                for g in run["graders"]:
                    if g["passed"]:
                        runs[(name, g["name"])] = runs.get((name, g["name"]), 0) + 1
        print(f"{side}: {ni.side_numbers(new)['rows']} rows, {ni.side_numbers(new)['false']} false on {REV}")
for e in entries:
    n = runs.get((e["case"], e["grader"]), 0)
    print(f"{e['case']} {e['grader']}: {n} runs")
    if n < 2:
        problems.append(f"{e['case']} {e['grader']}: matched {n} runs, fewer than two")
print("\n".join(problems))
print(f"problems: {len(problems)}")
sys.exit(1 if problems else 0)
PY
```

It printed `baseline: 55 rows, 19 false on 864798a4` and `phase 3: 47 rows,
12 false on 864798a4`. Of the 17 graders, 4 passed in two runs, 6 in three
and 7 in four. These are figures to record; phase 4 commits the sides and
their record. Two mutations through `mutation-check` showed the join can
fail, and both were red (executed):

- `truth-host-prefix` renamed in the input file, so its grader matches no
  run;
- a turned row of `false-rows.md` (baseline seeded-9b644676, run 0, row 2)
  reclassed `remark`.

**What the ±15 window does to two truths of replay-1791382684-r5.**
`truth_pattern` reads a line within ±15 of the location. So
truth-changelog-history at `changelog.md:12` also accepts `changelog.md:7`,
the coordinate of truth-old-phrase-kept. A run that named only the
first-bullet defect is credited with both. Every row involved is `real`,
so S5 holds. The spec's rule, *locations through `truth_pattern`*, is
followed as it stands. A narrower window is a change to every truth the
generators write, and this phase does not make it.

**One defect row stays false by choice.** The baseline's replay-1791382684-r2,
run 1, row 2 gives a bare `plan.md` for the mapping-rule defect. A bare-path
alternative would also credit phase 3's fenced row (run 0, row 6), a
`remark (fenced)`, and break S5. So truth-mapping-same-script reads
`plan.md:56` and `:134` only, and that row stays false under both suites.

**How the cases were seen red.**

- The eight generator cases (an added truth, a widened truth, five stale or
  malformed entries, and the replay and seeded generators reading the file)
  ran red before the code existed: `rule_cases` had no `rt` and
  `replay_targets` no `TRUTHS` (executed).
- Of 14 single-unit mutations of what the phase added, 13 were red against
  those cases (executed).
- The survivor drops the `(?:…)` around `truth_pattern`'s single
  alternative. It is equivalent as a regex, and it changes the bytes the
  generator writes. Against the byte-for-byte regeneration of
  replay-1791382684-r2 it was red (executed). The case files it changed
  were written back by regenerating at the restored source, and the tree
  was clean afterwards.

**For phase 4.**

- The suite's commit is 864798a4, so the regraded sides are
  `baseline-warden-864798a4.json` and `warden-phase-3-864798a4.json`.
- The S5 join above holds for that commit, and its false counts are the
  new-suite figures: 19 of 55 and 12 of 47.
