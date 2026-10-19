# 1792366315-the-wardens-real-false-finding-rate-is-unknown — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c1a2f8a5 |


## What this phase was asked

Build `evals/false-rows.md`, the classification table: one row per false
row of #957's two committed warden sides (43 baseline and 31 phase 3, 74 in
all). Each row carries its verbatim `location:` line, its class and the
command that re-checks it. Write the join that exits 0 only on an exact
one-to-one match with the rows recomputed from the committed side JSON, and
mark the rows whose finding text is only in #971's first comment. The
inputs are `baseline-warden.json` and `warden-phase-3.json` under
`seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/`, and
the comment (`gh issue view 971 --comments`). The raw output directories do
not exist. Close the phase with this record and `plan.md`'s Status cell;
later phases are not this spawn's.

## What this phase found

**The join.** Run it from the repository root. It needs nothing beyond the
standard library and `evals/scripts/`.

```sh
python3 - <<'PY'
import json, re, subprocess, sys
sys.path.insert(0, "evals/scripts")
from behaviour import squote
from noninferiority import kind, side_numbers

REV = "af9c924b"
SIDES = {
    "baseline": "seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/baseline-warden.json",
    "phase 3": "seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/warden-phase-3.json",
}
TABLE = "seal/specs/1792366315-the-wardens-real-false-finding-rate-is-unknown/evals/false-rows.md"
CLASSES = ("real", "real (truth-miss)", "remark", "remark (artefact)",
           "remark (fenced)", "wrong", "unclear")
CELL = re.compile(r"(?<!\\)\|")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


problems, want = [], {}
for side, path in SIDES.items():
    with open(path, encoding="utf-8") as f:
        result = json.load(f)
    if result["specseal"]["suite_tree"] != git("rev-parse", f"{REV}:evals/behaviour/warden").strip():
        problems.append(f"{side}: its suite tree is not {REV}'s")
    false = 0
    for case in result["cases"]:
        name = case["dir"].rsplit("/", 1)[1]
        truths = [g for g in case["graders"] if kind(g["name"]) == "truth" and g.get("type") == "regex"]
        files = [p[:-3] for p in git("ls-tree", "--name-only", f"{REV}:{case['dir']}/graders").split()
                 if p.startswith("truth-")]
        if sorted(files) != sorted(g["name"] for g in truths):
            problems.append(f"{side} {name}: its truths are not {REV}'s")
        for g in truths:
            if "pattern: " + squote(g["config"]["pattern"]) not in git("show", f"{REV}:{case['dir']}/graders/{g['name']}.md").splitlines():
                problems.append(f"{side} {name}: {g['name']}'s pattern is not {REV}'s")
        found = [re.compile(g["config"]["pattern"], re.M) for g in truths]
        runs = [r for arm in case["arms"].values() for r in arm]
        for i, run in enumerate(runs):
            for j, row in enumerate(run["specseal"]["report_rows"]):
                if not any(t.search(row) for t in found):
                    want[(side, name, str(i), str(j))] = row
                    false += 1
    if false != side_numbers(result)["false"]:
        problems.append(f"{side}: {false} false rows here, {side_numbers(result)['false']} by side_numbers")

got, classes, totals = {}, {}, {}
try:
    with open(TABLE, encoding="utf-8") as f:
        lines = f.read().split("\n")
except OSError as error:
    lines = []
    problems.append(f"{TABLE}: {error.strerror}")
for line in lines:
    cells = [c.strip() for c in CELL.split(line)[1:-1]]
    if len(cells) == 8 and cells[0] in SIDES:
        key = tuple(cells[:4])
        if key in got:
            problems.append(f"twice: {key}")
        got[key], classes[key] = cells[4], cells[5]
        if cells[5] not in CLASSES:
            problems.append(f"no such class: {key} {cells[5]!r}")
    elif len(cells) == 3 and cells[0] in CLASSES + ("all false rows",):
        totals[cells[0]] = (cells[1], cells[2])

for key in sorted(set(want) | set(got)):
    if key not in got:
        problems.append(f"no row in the table: {key}")
    elif key not in want:
        problems.append(f"not a false row of the side: {key}")
    elif got[key] != want[key]:
        problems.append(f"location differs: {key}")
for label in CLASSES + ("all false rows",):
    counted = tuple(
        str(sum(1 for k in got if k[0] == side and (label == "all false rows" or classes[k] == label)))
        for side in SIDES
    )
    if totals.get(label) != counted:
        problems.append(f"total for {label}: the table says {totals.get(label)}, its rows give {counted}")

print("\n".join(problems))
print(f"false rows: {sum(1 for k in want if k[0] == 'baseline')} baseline, "
      f"{sum(1 for k in want if k[0] == 'phase 3')} phase 3; table rows: {len(got)}; problems: {len(problems)}")
sys.exit(1 if problems else 0)
PY
```

It recomputes the false rows with `side_numbers`' own test and checks its
count against `side_numbers`. It also checks that each side's suite tree,
truth grader names and truth patterns are af9c924b's. Then it exits 0 only
when the table holds each false row once, with its `location:` byte for
byte, and the totals table matches the rows. At c1a2f8a5 it printed
`false rows: 43 baseline, 31 phase 3; table rows: 74; problems: 0` and
exited 0 (executed).

**How the join was seen red.** Before the table existed it exited 1 with 83
problems: the missing file, 74 missing rows and 8 totals (executed). Then
`mutation-check` broke the committed table once per command, and each run
was red: a location changed by one digit, a class changed so a total no
longer matched, a total changed, a row's index moved off a false row, a
row's index moved onto another row's key, and a class outside the
vocabulary (six runs, executed). Two mutations of the join's own provenance
checks were red too: comparing against the smith's suite tree, and
comparing patterns with a character appended (executed). One mutation
survived: disabling the location comparison leaves the correct table green.
That unit is exercised only by a wrong table, which the first table
mutation is.

**The frame holds where it can be measured.** These parts were executed:

- 43 and 31 false rows, recomputed with `side_numbers`.
- The per-case counts `spec.md` quotes from the comment.
- The truths the sides carry are af9c924b's.
- `plan.md`'s example re-check: `git cat-file -e
  7ef6abbf:docs/the-review-record.md` exits 128.

**Where the frame does not hold, and what was built instead.**

- *Every `remark` row names its re-run command* (`plan.md` phase 1,
  Verified by; `spec.md` S2). The two `remark (fenced)` rows cannot. Their
  class rests on where a line sat in the printed record, and that record is
  gone. The committed rows keep the `location:` line alone. Each of the two
  rows says so in its Reason cell instead of naming a command. Two
  cost-only `remark` rows name a command for their coordinate. Their class
  rests on a judgment no command decides, and each row says that too.
- *Mark the rows whose finding text is only in the comment.* That is every
  row: the sides keep only `location:` lines, and the traces are gone. The
  Finding column's header and the file's *How to read a row* say so once.
  A per-row tag would be the same word 74 times.
- Two facts in the comment have moved. Its commit 2dfa53a9 (phase 3,
  seeded-4d316179 r1.F2) does not resolve in this clone. #877 is closed
  now, where the comment saw it open (phase 3, seeded-ad447367 r1.F2).
  Neither changes a class. Both rows record it.
- The comment's location column is a paraphrase, and it differs from the
  committed line in places. For example, the baseline's replay-1791382684-r5
  r0.F5 is `changelog.md:12, …:7` in the JSON and `changelog.md:11-16` in
  the comment. The table takes the JSON's line.

**`questions.md` Q4, answered by this phase.** Each comment row was matched
to JSON rows by its location within the run, and a row grouping both runs
became one table row per run. For every false row, the comment's `rN.FM`
is run N and row M-1 of that run's `report_rows` (executed: a script over
the table's Finding cells found no exception). The two fenced lines are
rows 5 and 6 of phase 3's replay-1791382684-r2 run 0, after F5 at row 4.
The join is the arbiter, and it exits 0. This record cannot write the
question's Status cell; the hand-back carries it.

**What phase 3 can read from the table.** Each recurring candidate's runs
can be counted from the Side, Case and Run columns. The rows of one defect
are linked in two ways. Within a side, a Finding cell says *the same
finding as rN.FM*. Across sides, a Reason cell opens *Same as the
baseline's rN.FM*. The baseline's replay-1791382684-r2 run 1
row 1 is classed `real` but holds a `parse_section` half that is truth-2's,
and the comment's class is carried unchanged. The phase-3 side's
seeded-279a580b run 0 row 3 is `real` for its count half, and its other
half is an artefact.

**Two checks ran outside this clone, and repeating them needs a scratch
clone.** The `remark` rows of seeded-279a580b and the `wrong` row of
seeded-ad447367 rest on running a module at the case's commit with the
scaffold's seed applied. That was done in scratch clones made with `git
clone --shared` from this worktree, and the commands are in the rows.
