# Phase 1: 1793528484-the-process-measured-on-0-27-2

## What this phase found

### The measured state

- **The after tree is `94b03636`**, the head of `origin/release/v0.27.2` after `git fetch origin` when the phase started (executed: `git rev-parse origin/release/v0.27.2`). It is the commit the frame was cut from. `git diff --stat 94b03636 94b03636 -- . ':!seal/threads' ':!seal/follow-up.md'` printed nothing (executed), so no process change landed after the frame. Scenario S8's `git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'` printed nothing at `ff453b0a` (executed).
- **The before trees** are `f95f0ba8` for preload and `a8d83663`, the `v0.21.1` tag, for every other tree measure, as `frame/design.md` *Scope* item 1 says.
- **The after work items, for CI**, with the pull request each merged through (executed: `gh pr view <n> --json number,headRefName,baseRefName,state,mergeCommit,mergedAt`):

| Work item | Pull request | State | Merge commit | Head of the run read |
|---|---|---|---|---|
| #1221 | #1248 | merged | `ad5246ce` | `f82eecd9` |
| #1222 | #1250 | merged | `161a42aa` | `c87f1bed` |
| #1223 | #1252 | merged | `a8269d90` | `f11a5ba7` |
| #1229 | #1253 | merged | `94b03636` | `451986d5` |
| #1038 | #1257 | open, `before its merge` | none | `f8d1b8f6` |

#1038's branch head is now `f8d1b8f6` (executed: `gh pr view 1257 --json headRefOid`). The frame read its records at `3937d861` (`frame/design.md` G7). Phases 2 and 3 read #1038 at the head they find and name it.

### Whether the frame holds

Three facts of `frame/plan.md` *Technical context* hold. At `94b03636` every agent definition lists `core` and `agent-contract`, and at `a8d83663` the definitions are `framer.md`, `scribe.md`, `sealer.md`, `smith.md` and `warden.md` (executed: `preload.py` below). `.test_durations` at `94b03636` prices 6,181 cases at 994.8 seconds (executed: `suite.py`). Run `41296448338` lists the ubuntu job, three macOS shards and four Windows shards (executed: `gh api .../runs/41296448338/jobs --paginate`).

Three readings the frame names do not give the body's figure. Each is a departure, and each is decided below.

1. `frame/design.md` *Scope* item 3 reads "every file under `docs/`". At `a8d83663` that is 718,396 B, not the body's 708 KB. The files directly under `docs/` give 708,070 B, which is the body's figure. `docs/experiments/` holds the other 10,326 B.
2. *Scope* item 3 reads "every file under `skills/` and `templates/` that no agent's `skills:` list names". At `a8d83663` that is 2,432,367 B, of which 1,994,369 B are files under a `scripts/` directory. No reading found gives the body's 463 KB.
3. *Scope* item 4 counts cases "as `.test_durations` prices them". At `a8d83663` the file prices 13,482 cases, not the body's 13,914. `bin/test --collect-only -q -p no:xdist` at `a8d83663` collects 13,914.

### The measures

Every figure below is `executed` by the command named in its row, and each command stands whole under *Commands*. Bytes are raw bytes, and a KB is 1,000 bytes, because 708,070 B is the body's 708 KB.

**Preload per spawn, and `CLAUDE.md`** (`preload.py`). The before is re-run at `f95f0ba8`; `a8d83663` gives the same seven figures.

| Measure | Body | Re-run at `f95f0ba8` | After at `94b03636` | Before |
|---|---|---|---|---|
| framer, framer | 99,089 B | 99,089 B (19,809 + agent-contract 20,426 + implement 37,844 + writing-style 21,010) | 36,402 B (14,146 + core 9,077 + agent-contract 13,179) | reproduced |
| smith, crafter | 106,350 B | 106,350 B (27,070 + 20,426 + 37,844 + 21,010) | 33,108 B (10,852 + 9,077 + 13,179) | reproduced |
| warden, proofer | 102,229 B | 102,229 B (33,258 + 20,426 + code-review 27,535 + 21,010) | 32,008 B (9,752 + 9,077 + 13,179) | reproduced |
| sealer, sealer | 36,113 B | 36,113 B (15,687 + 20,426) | 32,262 B (10,006 + 9,077 + 13,179) | reproduced |
| scribe, tracer | 29,554 B | 29,554 B (3,764 + 20,426 + legacy-parity 5,364) | 25,198 B (2,942 + 9,077 + 13,179) | reproduced |
| `CLAUDE.md` | 9,261 B | 9,261 B | 1,143 B | reproduced |

#1052's reading at `0b75346f` is cited from the body as a middle point and not re-run, as *Scope* item 2 says: framer 22,513 B, crafter 21,461, proofer 21,898, sealer 21,386, tracer 15,236, `CLAUDE.md` 3,425.

The after tree adds a session-side preload that the `CLAUDE.md` row does not count. The plugin's `SessionStart` hook prints `skills/core/SKILL.md`, 9,077 B at `94b03636`, into each session (read: `hooks/hooks.json` *SessionStart* and `hooks/lib/core.py#HEADER`; `CLAUDE.md` *The core*). At `a8d83663` no `skills/core/` exists (executed: `preload.py`'s skill list there). Phase 3 decides how the reading compares the two sides; this phase records the figure.

**`docs/`, and the skills and templates opened on demand** (`ondemand.py`).

| Measure | Body | Re-run at `a8d83663` | After at `94b03636` | Before |
|---|---|---|---|---|
| D2 `docs/`, the files directly under it | 708 KB | 708,070 B | 242,145 B | reproduced |
| D1 `docs/`, every file | 708 KB | 718,396 B | 252,477 B | not reproduced (+1.5 per cent) |
| O2 `skills/` and `templates/`, less each preloaded `SKILL.md`, less files under a `scripts/` directory | 463 KB | 437,998 B | 344,602 B | not reproduced (-5.4 per cent) |
| O1 the same, with the `scripts/` files | 463 KB | 2,432,367 B | 1,394,735 B | not reproduced |

**The suite** (`suite.py`, and `bin/test --collect-only` in a scratch clone).

| Measure | Body | Re-run at `a8d83663` | After at `94b03636` | Before |
|---|---|---|---|---|
| cases, as `pytest --collect-only` collects them | 13,914 | 13,914 | 6,277 | reproduced |
| cases, as `.test_durations` prices them | 13,914 | 13,482 | 6,181 | not reproduced (-3.1 per cent) |
| Windows seconds, the sum of `.test_durations` | 7,861 s | 7,861.7 s | 994.8 s | reproduced |
| test lines, `.py` files under `tests/` | 160,228 | 160,138 (191 files) | 94,690 (158 files) | not reproduced (-90 lines, -0.06 per cent) |
| test lines, every file under `tests/` | 160,228 | 161,673 (192 files) | 94,690 (158 files) | not reproduced |

**CI per pull request** (`ci.py`, then `subsets.py` over the before lines). A leg's figure is the median over runs of the runner-minutes summed over the leg's `pytest` jobs.

| Measure | Body | Re-run over 60 runs of 2026-10-13 | After over 5 runs | Before |
|---|---|---|---|---|
| slowest job, median over runs | 12.3 min | 11.6 min (max 39.9) | 2.8 min (max 3.0) | not reproduced |
| ubuntu | 9.9 | 9.4 | 1.5 | not reproduced |
| Windows | 42.4 | 40.8 | 8.9 | not reproduced |
| macOS | 21.6 | 19.8 | 3.6 | not reproduced |

The before sample is 60 runs and the after sample 5, one per after work item, since each branch had one completed, uncancelled `tests` run on a `pull_request` event. #1038's row is run `41298025465`, `before its merge`. The before sample takes every push to a pull request on that day, several to a branch, while the after sample takes one run per branch.

### What the CI before is, where it does not reproduce

No subset found gives the body's four figures together (executed: `subsets.py`):

| Subset of the 60 runs | Runs | Slowest, median | ubuntu | Windows | macOS | Leg maxima |
|---|---|---|---|---|---|---|
| every run | 60 | 11.6 | 9.4 | 40.8 | 19.8 | 11.1 · 45.2 · 25.0 |
| successful runs | 48 | 11.6 | 9.4 | 41.0 | 20.2 | 11.1 · 45.2 · 24.5 |
| created on 2026-10-13 in UTC+9 | 52 | 11.5 | 9.4 | 40.8 | 19.9 | 11.1 · 45.2 · 25.0 |
| 12 consecutive runs from 05:14Z | 12 | 11.3 | 9.8 | 41.9 | 19.8 | 11.1 · 45.2 · 24.0 |
| 12 consecutive runs from 05:27Z | 12 | 11.4 | 9.8 | 41.9 | 19.8 | 11.1 · 45.2 · 24.0 |
| 12 consecutive runs from 05:34Z | 12 | 11.9 | 9.9 | 43.2 | 19.8 | 11.1 · 45.2 · 24.0 |

The last three rows are every window of 12 consecutive runs whose leg maxima are the "max 11.1 · 45.2 · 24.0 over 12 runs on 2026-10-13" of `v0.22.0:seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md` *The budgets*, the `ci-minutes` row (read). The body's 12.3 min and Windows 42.4 are run `38477758775`'s slowest job and Windows leg; that run's ubuntu is 6.9 and its macOS 22.7. Its phase record `phase-3.md` at `v0.22.0`, *The numbers*, cites that run for 6.9, 42.4 and 22.7 (read). The body's ubuntu 9.9 and macOS 21.6 are no median of any subset above.

### The decisions, each with its grounds

1. **`docs/` is read as the files directly under it (D2), and D1 stands beside it.** D2 gives the body's 708 KB at `a8d83663`, and *Scope* item 3 asks for the reading that gives the body's figure, run the same way at the after tree. Judged against: `frame/design.md` *Scope* item 3.
2. **The on-demand set is labelled not reproduced, and O2 is the reading phase 3 compares on, with O1 beside it.** The body's figure is a prose size, and O1 is 82 per cent `scripts/` code at `a8d83663`. O2 is the frame's set without code, and it is the nearest reading found, 5.4 per cent under. Searched: the frame's two sets, with and without `.md`-only, `scripts/` and the whole directories of named skills, at `f95f0ba8`, `a8d83663`, `v0.21.0`, `v0.21.1` and `v0.22.0`; then every union of the parts of the tree at `a8d83663` within 600 B of 463,000 or 474,112 B. The three unions found are arbitrary mixes, such as two preloaded `SKILL.md` files kept and three dropped, and none is a reading anybody would state. `git log --all -S'463 KB'` finds only this frame (executed). Judged against: `frame/design.md` *Scope* item 3 and `frame/plan.md` *Alternatives considered* A1, "the comparison rests on the re-run".
3. **Cases are read as `pytest --collect-only` collects them, and `.test_durations`' count stands beside it.** The collected count reproduces the body's 13,914 exactly, so it is the reading the body's figure matches; the durations file holds 432 cases fewer at `a8d83663` and 96 fewer at `94b03636`. Collection runs no case, so it is not the broad gate's full suite. It ran through `bin/test` in a `git clone --no-local` at each tree in the scratch directory, and each clone, with the virtual environment `bin/test` built inside it, was removed after. Judged against: `frame/design.md` *Scope* item 4, "the reading that does is found", and `skills/agent-contract/SKILL.md` rules 2 and 7.
4. **Test lines are labelled not reproduced.** `wc -l` over the `.py` files under `tests/` is 90 lines under the body. Every file under `tests/` lives at its top level at `a8d83663`, so no directory choice closes the gap, and the readings tried are `.py` only, every file, `test_*.py` only, and `test_*.py` anywhere in the tree. Judged against: `frame/design.md` *Scope* item 4.
5. **The CI before set is every run `created=2026-10-13` returns, in UTC, and it is labelled not reproduced.** *Scope* item 5 names "the `tests` runs on pull requests of 2026-10-13", and GitHub's `created` filter reads the date in UTC. The UTC+9 day gives the same medians within 0.1 min. The slowest job is the slowest job of any kind in a run. In 58 of the 60 before runs and in all 5 after runs it is a Windows `pytest` shard; in run `38336741194` it is a macOS shard, and in run `38352045124` the ubuntu job. Judged against: `frame/design.md` *Scope* item 5 and G11, and `frame/plan.md` *Alternatives considered* A1.

### What the next phases need

- Every before of *Scope* items 2 to 5 has its re-run figure, so phase 3's table rests on the re-run where the body's figure did not reproduce (`frame/plan.md` *Alternatives considered* A1).
- The suite shrank between the trees: 13,914 collected cases to 6,277. The CI figures follow the suite, so phase 3's reading of CI cannot separate a faster runner from a smaller suite.
- #1038's head is `f8d1b8f6`, not the `3937d861` the frame read.

### Commands

Every command ran with the working directory at this worktree, or at a clone of this repository where a row says so. Each probe is saved under its file name in one directory, since `ondemand.py` and `suite.py` import `preload.py`, and is run from that directory with the working directory at the clone.

```sh
git fetch origin && git rev-parse origin/release/v0.27.2
git diff --stat 94b03636 94b03636 -- . ':!seal/threads' ':!seal/follow-up.md'
git diff --stat origin/release/v0.27.2...HEAD -- . ':!seal/threads/1793528484-the-process-measured-on-0-27-2'
for n in 1248 1250 1252 1253 1257; do gh pr view $n --json number,headRefName,baseRefName,state,mergeCommit,mergedAt; done
gh pr view 1257 --json headRefOid
for c in f95f0ba8 a8d83663 94b03636; do python3 preload.py $c; done
for c in a8d83663 94b03636; do python3 ondemand.py $c; python3 suite.py $c; done
git clone --no-local <this repository> clone && git -C clone checkout a8d83663 && (cd clone && bin/test --collect-only -q -p no:xdist | tail -1)
# the same at 94b03636: "6277 tests collected"
git log --all --format='%h %ci %s' -S'463 KB'
python3 ci.py --created 2026-10-13 > ci-before.txt
python3 subsets.py ci-before.txt
python3 ci.py --branch test/1221-a-windows-run-names-its-skipped-cases --branch fix/1222-the-checks-wait-starts-before-a-check-reports --branch fix/1223-a-finding-is-counted-once --branch test/1229-the-proofer-cases-come-from-thread-records --branch chore/1038-the-record-decides-each-proposed-verifier
for r in 41292519665 41293403435 41294349566 41296448338 41298025465; do gh api repos/MichaelYcJo/AgenticSeal/actions/runs/$r -q '[.id,.head_sha[0:8]]|@tsv'; done
```

`preload.py`:

```python
"""Preload per spawn at one commit: bytes of agents/<a>.md plus each
skills/<s>/SKILL.md its skills: list names, and the bytes of CLAUDE.md."""
import subprocess
import sys


def show(c, p):
    return subprocess.run(["git", "show", f"{c}:{p}"], capture_output=True, check=True).stdout


def ls(c, *paths, recursive=False):
    args = ["git", "ls-tree"] + (["-r", "-l"] if recursive else ["--name-only"]) + [c, "--", *paths]
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout.splitlines()


def skills(text):
    lines = text.decode().splitlines()
    assert lines[0].strip() == "---", "no frontmatter"
    out, inlist = [], False
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        if ln.startswith("skills:"):
            inlist = True
        elif inlist and ln.lstrip().startswith("- "):
            out.append(ln.split("- ", 1)[1].strip())
        elif inlist and ln and not ln[0].isspace():
            inlist = False
    return out


def agents(c):
    return {p: skills(show(c, p)) for p in ls(c, "agents/") if p.endswith(".md")}


if __name__ == "__main__":
    c = sys.argv[1]
    for p, sk in agents(c).items():
        parts = [len(show(c, p))] + [len(show(c, f"skills/{s}/SKILL.md")) for s in sk]
        print(f"{p}\t{sum(parts)}\t{'+'.join(map(str, parts))}\t{','.join(sk)}")
    print(f"CLAUDE.md\t{len(show(c, 'CLAUDE.md'))}")
```

`ondemand.py`:

```python
"""Bytes of docs/ and of the skills/ and templates/ files no agent's skills:
list names, summed from git ls-tree -r -l at one commit, under four readings."""
import sys

from preload import agents, ls

c = sys.argv[1]
rows = []
for ln in ls(c, "docs", "skills", "templates", recursive=True):
    meta, path = ln.split("\t", 1)
    _, typ, _, size = meta.split()
    if typ == "blob":
        rows.append((path, int(size)))
preloaded = {f"skills/{s}/SKILL.md" for sk in agents(c).values() for s in sk}


def total(pred):
    return sum(size for p, size in rows if pred(p))


def under_st(p):
    return p.startswith(("skills/", "templates/")) and p not in preloaded


readings = {
    "D1 docs/, every file": lambda p: p.startswith("docs/"),
    "D2 docs/, files directly under it": lambda p: p.startswith("docs/") and p.count("/") == 1,
    "O1 skills/ and templates/ minus preloaded SKILL.md, every file": under_st,
    "O2 the same, without files under a scripts/ directory": lambda p: under_st(p) and "/scripts/" not in p,
}
for name, pred in readings.items():
    print(f"{total(pred)}\t{name}")
```

`suite.py`:

```python
"""The suite at one commit: .test_durations' case count and summed seconds,
and the lines of the tests/ files, read with git show and git ls-tree."""
import json
import subprocess
import sys

from preload import ls, show

c = sys.argv[1]
d = json.loads(show(c, ".test_durations"))
print(f"durations: {len(d)} cases, {sum(d.values()):.0f} s")
for prefix in ("tests/", "evals/"):
    sub = {k: v for k, v in d.items() if k.startswith(prefix)}
    print(f"  {prefix}: {len(sub)} cases, {sum(sub.values()):.0f} s")
paths = [ln.split("\t", 1)[1] for ln in ls(c, "tests", recursive=True) if ln.split()[1] == "blob"]
py = [p for p in paths if p.endswith(".py")]
lines_all = sum(show(c, p).count(b"\n") for p in paths)
lines_py = sum(show(c, p).count(b"\n") for p in py)
print(f"tests/ lines: every file {lines_all} ({len(paths)} files), .py {lines_py} ({len(py)} files)")
```

The seconds to one decimal came from `git show <c>:.test_durations | python3 -c 'import json,sys; d=json.load(sys.stdin); print(len(d), repr(sum(d.values())))'`, which printed `13482 7861.700248900036` at `a8d83663` and `6181 994.7552299999999` at `94b03636`.

`ci.py`:

```python
"""CI per pull request: for each `tests` workflow run on a pull_request event,
completed and not cancelled, the slowest job's minutes and each leg's
runner-minutes summed over the leg's pytest jobs, read with gh api.
Usage: ci.py --branch <b> [--branch <b> ...]  |  ci.py --created <YYYY-MM-DD>"""
import argparse
import json
import statistics
import subprocess
from datetime import datetime

REPO = "repos/MichaelYcJo/AgenticSeal/actions"


def api(path):
    out = subprocess.run(["gh", "api", "--paginate", path], capture_output=True, text=True, check=True).stdout
    dec, pages, i = json.JSONDecoder(), [], 0
    while i < len(out):
        if out[i].isspace():
            i += 1
            continue
        page, i = dec.raw_decode(out, i)
        pages.append(page)
    return pages


def t(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


ap = argparse.ArgumentParser()
ap.add_argument("--branch", action="append", default=[])
ap.add_argument("--created")
a = ap.parse_args()
queries = [f"branch={b}" for b in a.branch] or [f"created={a.created}"]
runs = []
for q in queries:
    for page in api(f"{REPO}/workflows/test.yml/runs?event=pull_request&per_page=100&{q}"):
        runs += page["workflow_runs"]
runs = [r for r in runs if r["status"] == "completed" and r["conclusion"] != "cancelled"]
legs = {"ubuntu": [], "windows": [], "macos": []}
slowest = []
for r in sorted(runs, key=lambda r: r["created_at"]):
    jobs = [j for page in api(f"{REPO}/runs/{r['id']}/jobs?per_page=100") for j in page["jobs"]]
    done = [j for j in jobs if j["conclusion"] not in ("skipped", None) and j["started_at"] and j["completed_at"]]
    mins = {j["name"]: (t(j["completed_at"]) - t(j["started_at"])).total_seconds() / 60 for j in done}
    per_leg = {}
    for leg in legs:
        ms = [m for n, m in mins.items() if n.startswith(f"pytest ({leg}-")]
        if ms:
            per_leg[leg] = sum(ms)
            legs[leg].append(sum(ms))
    top = max(mins, key=mins.get)
    slowest.append(mins[top])
    print(f"{r['id']}\t{r['created_at']}\t{r['head_branch']}\t{r['conclusion']}\tattempt {r['run_attempt']}\tslowest {mins[top]:.1f} ({top.split(',')[0]})\t"
          + "\t".join(f"{k} {v:.1f}" for k, v in per_leg.items()))
print(f"runs {len(slowest)}; slowest job median {statistics.median(slowest):.1f}, max {max(slowest):.1f}")
for leg, v in legs.items():
    if v:
        print(f"{leg}: median {statistics.median(v):.1f} runner-min over {len(v)} runs (min {min(v):.1f}, max {max(v):.1f})")
```

`subsets.py`:

```python
"""Readings of ci.py's per-run lines (argv[1]) over subsets of the runs: every
run, the successful runs, the runs of 2026-10-13 in UTC+9, and each window of
12 consecutive runs whose leg maxima are the 0.22.0 spec's 11.1, 45.2, 24.0."""
import re
import statistics
import sys

rows = []
for ln in open(sys.argv[1]):
    f = ln.rstrip("\n").split("\t")
    if len(f) < 8:
        continue
    d = {"t": f[1], "c": f[3], "slow": float(re.search(r"slowest ([\d.]+)", f[5]).group(1))}
    for x in f[6:]:
        k, v = x.split()
        d[k] = float(v)
    rows.append(d)
LEGS = ("ubuntu", "windows", "macos")


def stats(rs):
    med = lambda k: round(statistics.median([r[k] for r in rs]), 1)  # noqa: E731
    return (len(rs), med("slow"), *(med(k) for k in LEGS), tuple(max(r[k] for r in rs) for k in LEGS))


print("every run", stats(rows))
print("success", stats([r for r in rows if r["c"] == "success"]))
print("UTC+9 day", stats([r for r in rows if r["t"] < "2026-10-13T15:00:00Z"]))
for i in range(len(rows) - 11):
    w = rows[i:i + 12]
    if stats(w)[5] == (11.1, 45.2, 24.0):
        print("window", w[0]["t"], w[-1]["t"], stats(w))
```
