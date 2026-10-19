# 1792366315-the-wardens-real-false-finding-rate-is-unknown — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 837ee9bc |


## What this phase was asked

Regrade both committed warden sides onto 864798a4 and commit them as
`baseline-warden-864798a4.json` and `warden-phase-3-864798a4.json`, with
`compare`'s record between them. Add the two-suite table: af9c924b against
864798a4, with rows, false rows, false rate and recall for each side. Write
`changelog.md`. It says the new suite is the one comparisons use from the
release after 0.22.2, by the owner's decision in #971's body, and that
#968 and #985 in 0.22.2 still measure on af9c924b. Close `overview.md`'s
Not verified rows, leaving the finding-wording row with the owner, then
this record and the Status cell. No paid runs.

## What this phase found

**What was committed (837ee9bc), all executed.**

- `regrade --suite-rev 864798a4` over `baseline-warden.json` and
  `warden-phase-3.json` wrote the two sides into this directory's `evals/`.
  The baseline has 55 rows with 19 false; phase 3 has 47 rows with 12
  false. Both runs exited 0.
- A second regrade at 837ee9bc gave the same bytes for both sides (`cmp`
  exit 0).
- `compare --agent warden --phase 3` over the two wrote
  `971-warden-phase-3-864798a4.md`, `Verdict: pass`.
- `noninferiority.py check` recomputes that verdict from its numbers, exit
  0. #957's own af9c924b record, `warden-phase-3.md`, also checks with exit
  0.

**The figures** (`evals/false-rows.md`, *The figures under both suites*):

| Side | False rows, af9c924b → 864798a4 | Recall, af9c924b → 864798a4 |
|---|---|---|
| baseline | 43/55 → 19/55 | 13/24 → 39/54 |
| phase 3 | 31/47 → 12/47 | 16/24 → 41/54 |

The real false rate, `wrong` over rows, is 1/55 and 1/47 under both
suites. Under the new suite, what stays false is mostly what no suite can
make true: remarks, artefacts, fenced lines, single-run defects and a form
the grammar refuses. The table gives it by class.

**The figures check.** `plan.md` says the S1 and S5 commands recompute
the table's figures. Neither prints recall or the false rows by class, so
this phase adds a third command. It recomputes every figure line of the two
new tables from the four committed sides and the phase 1 classes, and exits
0 only when each line is in `false-rows.md` byte for byte. At 837ee9bc it
printed `figures: 11; not in the table: 0` and exited 0 (executed). Run it
from the repository root:

```sh
python3 - <<'PY'
"""The two-suite figures for each side, from the committed sides. Run from
the worktree root."""

import json
import re
import sys

sys.path.insert(0, "evals/scripts")
import noninferiority as ni

E = "seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/"
I = "seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/"
SIDES = {
    "baseline": {"af9c924b": E + "baseline-warden.json", "864798a4": I + "baseline-warden-864798a4.json"},
    "phase 3": {"af9c924b": E + "warden-phase-3.json", "864798a4": I + "warden-phase-3-864798a4.json"},
}
CLASSES = ("real", "real (truth-miss)", "remark", "remark (artefact)", "remark (fenced)", "wrong", "unclear")
classes = {}
for line in open(I + "false-rows.md", encoding="utf-8"):
    c = [x.strip() for x in re.split(r"(?<!\\)\|", line)[1:-1]]
    if len(c) == 8 and c[0] in SIDES:
        classes[tuple(c[:4])] = c[5]


def false_keys(result):
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


want, by_class = [], {}
for side, suites in SIDES.items():
    for rev, path in suites.items():
        with open(path, encoding="utf-8") as f:
            result = json.load(f)
        n = ni.side_numbers(result)
        truths = [v for v in n["graders"].values() if v[0] == "truth"]
        finds, possible = sum(v[1] for v in truths), sum(v[2] for v in truths)
        want.append(f"| {side} | {rev} | {n['rows']} | {n['false']} | {n['false'] / n['rows']:.3f} | {finds}/{possible} | {finds / possible:.3f} |")
        keys = false_keys(result)
        for cls in CLASSES:
            by_class[(cls, side, rev)] = sum(1 for k in keys if classes[(side, *k)] == cls)
for cls in CLASSES:
    cells = [by_class[(cls, s, r)] for s in SIDES for r in ("af9c924b", "864798a4")]
    want.append(f"| {cls} | " + " | ".join(str(c) for c in cells) + " |")
with open(I + "false-rows.md", encoding="utf-8") as f:
    held = set(f.read().split("\n"))
missing = [line for line in want if line not in held]
print("\n".join(want))
print("\n".join(f"not in the table: {line}" for line in missing))
print(f"figures: {len(want)}; not in the table: {len(missing)}")
sys.exit(1 if missing else 0)
PY
```

**How the checks were seen red (executed).** Three `mutation-check` runs,
all red:

- a phase-3 figure line changed to 11 false rows: the figures check exits 1;
- the baseline's `unclear` count under 864798a4 changed to 0: the figures
  check exits 1;
- the record's `New false rows` changed to 40: `noninferiority.py check`
  exits 1.

The phase 1 join still exits 0 over the extended `false-rows.md`. Its
parser reads 8-cell side rows and 3-cell totals, and the new tables have 7
and 5 cells (executed).

**Where the changelog follows the owner and not the spawn.** The spawn
names #968 and #985 as 0.22.2's comparisons on af9c924b. The owner's
decision in #971's body names #968, #970 and the milestone's closing
verdict. #985 is the 0.22.2 warden change that Q1 moved there. The fragment
names all four, because the ratified decision ranks above a spawn. It
narrows nothing either one says.

**`overview.md` closed** in this record's commit.

- The divergence rows and the fed-back clauses stand as written at each
  phase.
- *Not done* names three things: step 3, which moved to #985; the
  scaffold artefacts and the reader faults, which are the owner's for the
  release after 0.22.2; and the real rows no second run named.
- *Not verified* keeps both rows open. The finding wording stays with the
  owner, as the spawn says. The suite row stays the orchestrator's: no
  broad run exists on this branch, and closing a row on a run nobody made
  would be the counterfeit the check exists to catch.
