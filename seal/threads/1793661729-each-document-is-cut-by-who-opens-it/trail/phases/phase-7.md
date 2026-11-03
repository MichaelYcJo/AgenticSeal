# Phase 7: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase.** It was read against the tree at
b1880c1db before the first command (read). D8 names the spawns, the two
sides, the split and the live reading. S9 and S10 name what each shows.
This phase changes no file outside this work item's records, so phase 6's
S2 reading stands at HEAD: `git diff --stat 308424df6 b1880c1db -- agents
skills/core skills/agent-contract` prints nothing (executed).

**The census's spawns, found again.** *Grounding* counted 1,004 subagent
transcripts under `~/.claude/projects/<project>/`. The directory now holds
1,011 (`find ~/.claude/projects/<project>/ -path '*/subagents/*.meta.json'
| wc -l`, executed). The seven more are this work item's crafter spawns,
phases 1 to 7, each described "Build phase N of #1312" in its
`.meta.json`. The replay leaves them out. The per-type counts then match
*Grounding*: crafter 78, framer 169, proofer 134 and sealer 159 (the
replay's output below). An agent type is the name after the colon, so the
framer's 169 are 53 `agentic:framer` and 116 spawns under the plugin's old
prefix, and the sealer's 159 are 55 and 104 (a count of `agentType` over
the `.meta.json` files, executed).

**S9 holds (executed).** `bin/seal fold` at b1880c1db printed:

```
seal fold: held 23 documents under docs/ to 25000 estimated tokens, 0 past it
seal fold: the index docs/README.md names every document
```

It exited 0. The largest policy document is now
`docs/releasing/branch-and-release.md`, 23,768 bytes, about 11,884
estimated tokens (`wc -c` over `git ls-files 'docs/*.md'`, executed).
`docs/the-review-record.md` was 50,774 bytes at the base (*Grounding*).

**How the replay reads D8: four decisions.**

- **The before side is the same calls replayed against the base
  2d38c75af, not the bytes the transcripts recorded.** The transcripts were
  taken under every release up to 0.29.0. Their files differ from the
  base's for reasons outside this work item. Replaying both trees holds the
  calls fixed, so only this work item's diff moves the reading. Judged
  against D8 *Comparable*, which asks for the same spawns and the same
  calls. The recorded bytes are printed beside each type for scale.
- **The unit is the UTF-8 bytes of the lines a call returns.** The Read
  tool's line-number prefix is not counted. *Grounding*'s census used the
  JSON length of each result, a different unit, and its script was
  removed, so its per-file counts are not reproduced here. The replay's
  counts are its own, and its rule for which path a call read is `rel` in
  the script below.
- **What a spawn cites is its definition and its prompt.** The definition
  is `agents/<type>.md`, at the base for the before side and at both trees
  for the after side. The prompt is the transcript's first user message. A
  citation is a backticked `.md` path, with or without an italic section
  title after it, and a path alone cites the whole file. The core's and the
  contract's citations are not counted. D8 names the definition and the
  prompt, and the core's citation of `skills/implement/orchestration.md`
  names the batch, which is the orchestrator's act. Judged against D8 *The
  split*.
- **Where a whole-file read goes at HEAD.** D8 sends it to "the file that
  now holds the step's cited section". A read of a document moved whole
  goes to its new path. A read of a cut file goes to two kinds of file. The
  first is the file that kept its path, where the spawn cites a section
  still in it or cites the file whole. The second is each file a cited
  section moved into: a section moved in where its heading stands in that
  file at HEAD and not at the base. Where the spawn cites none of these, the
  read goes to the file that kept its path. For the two documents phase 5
  deleted, it goes to every file their text went to. A deleted document
  the spawn names whole goes to every such file too. That charges the read
  about the old document's bytes, which is the direction that does not
  flatter the cut. Judged against D8 *After* and *Comparable*.

A ranged read takes the same lines at HEAD, as D8 says. A ranged read of a
deleted document has no file to read at HEAD. It is counted at its base
bytes, since S7 found those lines moved unchanged (`trail/phases/phase-5.md`
*S7*). The output lists these calls per type, 33 in all.

What the replay does not count: it replays Read calls only, so a file read
through `cat`, `sed` or `grep` is not in it. A call to a path the base does
not hold is left out. Such a path is another work item's record under
`seal/`, or a file an earlier release renamed. A call outside a checkout or
the plugin cache is left out too, such as a session's saved tool result or
a scratchpad. A call whose result held no file lines (an error, an image,
or an "unchanged since last read" stub) is left out. The output counts each
kind per type.

**The readings (executed).** The script was kept in the session scratchpad,
read only the transcripts and `git show` output, and wrote nothing. This is
its whole text:

```python
"""Replay the Read calls of past agent spawns against two trees (D8).

Read-only: it reads transcripts and `git show` output and writes nothing.

python3 replay.py <repo> <base> <head> <transcripts dir> [--files]
"""
import collections, glob, json, os, re, subprocess, sys

REPO, BASE, HEAD, TDIR = sys.argv[1:5]
SHOW_FILES = "--files" in sys.argv
TYPES = ("crafter", "framer", "proofer", "sealer")
# This work item's own crafter spawns ran after the framer's census; leave them out
# so the spawns are the census's 1,004 transcripts.
EXCLUDE_DESC = re.compile(r"#1312")

def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, check=True).stdout

def ls(rev):
    return set(git("ls-tree", "-r", "--name-only", rev).decode().split("\n")) - {""}

base_files, head_files = ls(BASE), ls(HEAD)
_blob = {}
def lines(rev, path):
    k = (rev, path)
    if k not in _blob:
        text = git("show", f"{rev}:{path}")
        _blob[k] = text[:-1].split(b"\n") if text.endswith(b"\n") else text.split(b"\n")
    return _blob[k]

# Lineage: each base path and the HEAD files its text stands in.
lineage = {p: [p] for p in base_files if p in head_files}
for row in git("diff", "-M", "--name-status", BASE, HEAD).decode().splitlines():
    f = row.split("\t")
    if f[0].startswith("R"):
        lineage[f[1]] = [f[2]]
lineage.update({
    "docs/the-review-record.md": ["docs/forms/the-round-record.md", "docs/forms/the-guarantee.md",
        "docs/checks/the-pull-request-check.md", "docs/checks/the-stamp.md", "docs/running/the-run.md"],
    "docs/the-record-layout.md": ["docs/layout/the-record-layout.md", "docs/checks/the-fold.md",
        "docs/checks/the-unverified-record.md"],
    "skills/settle/SKILL.md": ["skills/settle/SKILL.md", "skills/settle/rule-changes.md",
        "skills/settle/local-mode.md", "skills/settle/named-directories.md", "skills/settle/draft.md"],
    "skills/implement/SKILL.md": ["skills/implement/SKILL.md", "skills/implement/orchestration.md"],
    "skills/verify/SKILL.md": ["skills/verify/SKILL.md", "skills/verify/seal-arms.md",
        "skills/verify/seal-mutate.md"],
})

def norm(t):
    return re.sub(r"\s+", " ", t).strip()

_titles = {}
def titles(rev, path):
    """Per line, the titles of the headings that enclose it."""
    k = (rev, path)
    if k not in _titles:
        stack, out, fence = [], [], False
        for raw in lines(rev, path):
            s = raw.decode("utf-8", "replace")
            if s.startswith("```"):
                fence = not fence
            m = None if fence else re.match(r"(#{1,6})\s+(.*)", s)
            if m:
                lvl = len(m.group(1))
                stack = [x for x in stack if x[0] < lvl] + [(lvl, norm(m.group(2)))]
            out.append({t for _, t in stack})
        _titles[k] = out
    return _titles[k]

def new_titles(h):
    """The headings of a HEAD file that its base version did not hold: what moved in."""
    at_head = set().union(*titles(HEAD, h))
    return at_head - (set().union(*titles(BASE, h)) if h in base_files else set())

def matches(cited, heading_titles):
    for t in cited:
        for h in heading_titles:
            if h == t or (re.fullmatch(r"\d+\.", t) and h.startswith(t + " ")):
                return True
    return False

ROOTS = (
    (re.compile(r".*/Documents/GitHub/(?:SpecSeal|AgenticSeal)-worktrees/(.+)"), (1, 2)),
    (re.compile(r".*/Documents/GitHub/(?:SpecSeal|AgenticSeal)/(.+)"), (0,)),
    (re.compile(r".*/\.claude/plugins/cache/[^/]+/[^/]+/[^/]+/(.+)"), (0,)),
    (re.compile(r".*/\.claude/plugins/marketplaces/[^/]+/(.+)"), (0,)),
)

def rel(path, files):
    """The repository path of an absolute path under a checkout, a worktree
    (named by one or two components) or the plugin cache."""
    for pattern, skips in ROOTS:
        m = pattern.fullmatch(path)
        if m:
            parts = m.group(1).split("/")
            for k in skips:
                s = "/".join(parts[k:])
                if s in files:
                    return s
            return None
    return path if path in files else None

CIT = re.compile(r"`([^`\s]+?\.md)`(?:'s)?(?:\s+\*([^*]+)\*)?", re.S)
def citations(text, files):
    """{path: set of titles, or a set holding None for a whole-file citation}."""
    out = collections.defaultdict(set)
    for m in CIT.finditer(text):
        p = rel(m.group(1), files)
        if p:
            out[p].add(norm(m.group(2)) if m.group(2) else None)
    return out

def definition(rev, typ):
    return b"\n".join(lines(rev, f"agents/{typ}.md")).decode()

def measure(rev, path, rng, cited, whole):
    ls_, ts = lines(rev, path), titles(rev, path)
    lo, hi = rng if rng else (0, len(ls_))
    tot = cit = 0
    for i in range(lo, min(hi, len(ls_))):
        n = len(ls_[i]) + 1
        tot += n
        if whole or matches(cited, ts[i]):
            cit += n
    return tot, cit

def spawn_reads(jsonl):
    prompt, calls, results = "", {}, {}
    for line in open(jsonl):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        c = (d.get("message") or {}).get("content")
        if not prompt and d.get("type") == "user":
            prompt = c if isinstance(c, str) else " ".join(
                b.get("text", "") for b in c or [] if isinstance(b, dict))
        if not isinstance(c, list):
            continue
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use" and b.get("name") == "Read":
                calls[b["id"]] = b.get("input", {})
            if b.get("type") == "tool_result":
                body = b.get("content")
                text = body if isinstance(body, str) else "".join(
                    x.get("text", "") for x in body or [] if isinstance(x, dict))
                # A read that returned file lines; an error, an image or an
                # "unchanged since last read" stub is not one.
                ok = not b.get("is_error") and bool(re.match(r"\s*\d+\t", text))
                results[b.get("tool_use_id")] = (ok, len(text.encode()))
    return prompt, [(calls[k], results.get(k, (False, 0))) for k in calls]

defs = {(rev, t): citations(definition(rev, t), base_files if rev == BASE else head_files)
        for rev in (BASE, HEAD) for t in TYPES}

agg = collections.defaultdict(lambda: collections.Counter())
per_file = collections.defaultdict(lambda: collections.Counter())
spawns = collections.Counter()
for meta in sorted(glob.glob(os.path.join(TDIR, "*/subagents/*.meta.json"))):
    m = json.load(open(meta))
    typ = m.get("agentType", "").split(":")[-1]
    if typ not in TYPES or (typ == "crafter" and EXCLUDE_DESC.search(m.get("description", ""))):
        continue
    spawns[typ] += 1
    prompt, reads = spawn_reads(meta[: -len(".meta.json")] + ".jsonl")
    pc = citations(prompt, base_files)
    bcite = collections.defaultdict(set)
    for src in (defs[(BASE, typ)], pc):
        for p, ts in src.items():
            bcite[p] |= ts
    hcite = collections.defaultdict(set)  # HEAD file -> titles, None for whole
    for b, ts in bcite.items():
        for h in lineage.get(b, []):
            hcite[h] |= {t for t in ts if t}
            if None in ts and (len(lineage[b]) == 1 or h == b or b not in head_files):
                hcite[h].add(None)
    for h, ts in defs[(HEAD, typ)].items():
        hcite[h] |= ts
    a = agg[typ]
    for inp, (ok, recorded) in reads:
        fp = inp.get("file_path", "")
        b = rel(fp, base_files)
        if not b:
            if any(p.fullmatch(fp) for p, _ in ROOTS):
                a["calls to a path the base tree does not hold" +
                  (", a record under seal/" if "/seal/" in fp else ", another")] += 1
            else:
                a["calls outside a checkout or the plugin cache"] += 1
            continue
        if not ok:
            a["calls that returned no text"] += 1
            continue
        off, lim = inp.get("offset"), inp.get("limit")
        rng = None
        if off is not None or lim is not None:
            lo = max(int(off or 1) - 1, 0)
            rng = (lo, lo + int(lim or 2000))
        bt, bc = measure(BASE, b, rng, bcite.get(b, set()) - {None}, None in bcite.get(b, set()))
        L = lineage.get(b, [])
        if rng:
            targets = [L[0]] if b not in head_files and len(L) == 1 else ([b] if b in head_files else [])
        elif len(L) == 1:
            targets = L
        elif None in bcite.get(b, set()) and b not in head_files:
            targets = L  # a cut document named whole: every file its text went to
        else:
            # The file that kept the read's path, where a cited section stands in
            # it, and each file a cited section moved into from it.
            stay = b in head_files and (None in bcite.get(b, set()) or any(
                matches(hcite.get(b, set()) - {None}, s) for s in titles(HEAD, b)))
            moved = [h for h in L if h != b and any(
                matches(hcite.get(h, set()) - {None}, {t})
                for t in new_titles(h))]
            targets = ([b] if stay else []) + moved
            if not targets:
                targets = [b] if b in head_files else L
        if targets:
            at = ac = 0
            for h in targets:
                t, c = measure(HEAD, h, rng, hcite.get(h, set()) - {None}, None in hcite.get(h, set()))
                at, ac = at + t, ac + c
        else:  # a ranged read of a deleted file: its lines moved unchanged (S7)
            at, ac = bt, bc
            a["ranged reads of a deleted file, counted at base"] += 1
        a["calls"] += 1
        a["recorded"] += recorded
        a["base"] += bt; a["base cited"] += bc
        a["head"] += at; a["head cited"] += ac
        f = per_file[(typ, b)]
        f["calls"] += 1; f["base"] += bt; f["head"] += at

for typ in TYPES:
    a = agg[typ]
    print(f"{typ}: {spawns[typ]} spawns, {a['calls']} Read calls replayed")
    print(f"  base {a['base']:>10,}  cited {a['base cited']:>10,}  rest {a['base'] - a['base cited']:>10,}")
    print(f"  head {a['head']:>10,}  cited {a['head cited']:>10,}  rest {a['head'] - a['head cited']:>10,}")
    print(f"  change {a['head'] - a['base']:+,} ({(a['head'] - a['base']) / a['base']:+.1%}); "
          f"recorded in the transcripts {a['recorded']:,}")
    for k in ("calls to a path the base tree does not hold, a record under seal/",
              "calls to a path the base tree does not hold, another",
              "calls outside a checkout or the plugin cache", "calls that returned no text",
              "ranged reads of a deleted file, counted at base"):
        print(f"  {k}: {a[k]}")
    if SHOW_FILES:
        rows = sorted(((f["head"] - f["base"], p, f) for (t, p), f in per_file.items()
                       if t == typ and f["head"] != f["base"]), key=lambda r: r[0])
        if len(rows) > 10:
            rows = rows[:6] + rows[-4:]
        for d, p, f in rows:
            print(f"    {d:+10,}  {f['calls']:4d} calls  {f['base']:>9,} -> {f['head']:>9,}  {p}")
```

`python3 replay.py <repository root> 2d38c75af b1880c1db
~/.claude/projects/<project>/ --files` exited 0 and printed this. Under
each type, the indented lines are the six files whose replayed bytes fell
most and the four that rose most, by the path each call read at the base:

```
crafter: 78 spawns, 1258 Read calls replayed
  base  5,638,326  cited  2,331,190  rest  3,307,136
  head  5,274,434  cited  2,000,685  rest  3,273,749
  change -363,892 (-6.5%); recorded in the transcripts 5,788,342
  calls to a path the base tree does not hold, a record under seal/: 325
  calls to a path the base tree does not hold, another: 189
  calls outside a checkout or the plugin cache: 70
  calls that returned no text: 1
  ranged reads of a deleted file, counted at base: 10
      -332,765    79 calls  1,946,845 -> 1,614,080  skills/implement/SKILL.md
       -39,872    23 calls    138,787 ->    98,915  skills/settle/SKILL.md
        -6,604     5 calls     16,347 ->     9,743  skills/verify/SKILL.md
          -512     8 calls     22,324 ->    21,812  agents/sealer.md
          -506     3 calls      1,637 ->     1,131  skills/settle/scripts/fold_check.py
          -138     2 calls        374 ->       236  tests/behaviour/test_docs_line_wrap.py
        +1,230     5 calls     19,187 ->    20,417  tests/skills/test_rule_changes.py
        +1,281     3 calls      3,366 ->     4,647  docs/README.md
        +1,312    22 calls     32,854 ->    34,166  README.md
        +8,338    24 calls     42,575 ->    50,913  skills/implement/orchestration.md
framer: 169 spawns, 316 Read calls replayed
  base  4,669,123  cited  2,112,343  rest  2,556,780
  head  4,577,686  cited  2,009,959  rest  2,567,727
  change -91,437 (-2.0%); recorded in the transcripts 4,147,020
  calls to a path the base tree does not hold, a record under seal/: 465
  calls to a path the base tree does not hold, another: 172
  calls outside a checkout or the plugin cache: 79
  calls that returned no text: 2
  ranged reads of a deleted file, counted at base: 13
       -59,024    21 calls    266,734 ->   207,710  skills/settle/SKILL.md
       -24,430    62 calls    997,083 ->   972,653  skills/implement/SKILL.md
       -11,684     4 calls     41,237 ->    29,553  skills/verify/SKILL.md
        -3,380     4 calls    169,534 ->   166,154  skills/verify/scripts/seal_stamp.py
        -1,710    18 calls    447,640 ->   445,930  docs/the-review-record.md
        -1,323     6 calls     54,823 ->    53,500  agents/sealer.md
          +556     3 calls     75,131 ->    75,687  docs/the-record-layout.md
        +1,166     6 calls    110,101 ->   111,267  skills/settle/scripts/rule_changes.py
        +1,907     1 calls      2,549 ->     4,456  docs/README.md
        +7,215     5 calls     42,254 ->    49,469  skills/implement/orchestration.md
proofer: 134 spawns, 44 Read calls replayed
  base    375,093  cited    253,774  rest    121,319
  head    375,093  cited    253,774  rest    121,319
  change +0 (+0.0%); recorded in the transcripts 339,509
  calls to a path the base tree does not hold, a record under seal/: 21
  calls to a path the base tree does not hold, another: 0
  calls outside a checkout or the plugin cache: 144
  calls that returned no text: 0
  ranged reads of a deleted file, counted at base: 7
sealer: 159 spawns, 13 Read calls replayed
  base    162,270  cited     23,334  rest    138,936
  head    146,072  cited     23,334  rest    122,738
  change -16,198 (-10.0%); recorded in the transcripts 111,438
  calls to a path the base tree does not hold, a record under seal/: 200
  calls to a path the base tree does not hold, another: 7
  calls outside a checkout or the plugin cache: 191
  calls that returned no text: 0
  ranged reads of a deleted file, counted at base: 3
       -16,546     1 calls     43,170 ->    26,624  skills/settle/SKILL.md
            -2     2 calls     11,240 ->    11,238  skills/verify/scripts/unverified_check.py
          +350     1 calls     31,700 ->    32,050  skills/settle/scripts/rule_changes.py
```

**What the readings say.** No agent type's replayed total moved toward
more cost. The crafter's fell 6.5%, almost all of it on
`skills/implement/SKILL.md`, which phase 4 cut: 79 calls read 332,765 fewer
bytes. The framer's fell 2.0%, from the three skills phases 3 and 4 cut.
The proofer's 44 replayed calls read no file whose bytes changed, except 7
ranged reads of the deleted review record, counted at base. The sealer's
fell 10.0%, all of it one read of `skills/settle/SKILL.md`.

**A limit: most of the framer's reads are ranged, and a range lands on
other text at HEAD.** A read-only count over the same transcripts found 61
of the framer's 62 replayed reads of `skills/implement/SKILL.md` ranged,
and 19 of its 21 reads of `skills/settle/SKILL.md` (executed, a variant of
the script above that also counted ranged calls per file; removed after
the run). D8 has a ranged read take the same lines at HEAD. Where a section
moved out, those line numbers now hold other text. So the framer's split
moved for that reason as well: its cited bytes fell by 102,384 and its
uncited bytes rose by 10,947. The split of a ranged read says what the old
line numbers hold at HEAD, not what a framer under 0.30.0 would open. The
live reading is `frame/questions.md` Q1's.

**The weighing.** `docs/running/measuring-a-run.md` *A band flags a
reading for judgment, and a judgment decides whether it is worse* has the
crafter of a work item that measures the process weigh a reading that
moved toward more cost, beside the reading. No band is declared for this
replay, so no reading is flagged by one; each reading that rose is weighed
here. The reading is `worse` only where its cost outweighs what was bought.

- **`skills/implement/orchestration.md`: crafter +8,338 over 24 calls,
  framer +7,215 over 5.** Phase 4 moved the orchestrator's batch, ladder
  and drain into it (7927ac736). It grew from 23,653 bytes and 385 lines to
  31,003 bytes and 503 lines (`git show <commit>:<path> | wc -c` and `wc
  -l` at 2d38c75af and b1880c1db, executed). One crafter call read it whole
  and pays about 7,350 bytes more. The other 28 calls are ranged. A listing
  of their `offset` and `limit` shows ranges taken against longer copies of
  the file in earlier releases, with offsets up to 675, so they ran past
  the base's line 385 (executed, a read-only listing removed after the
  run). At HEAD the same ranges reach lines 386 to 503. What it bought: a
  crafter's whole read of `skills/implement/SKILL.md` is 30,663 bytes at
  the base and 25,275 at HEAD (`wc -c`, executed), and the crafter reads it
  at nearly every spawn, 332,765 fewer bytes over 79 calls here. Not
  `worse`.
- **`docs/README.md`: crafter +1,281 over 3 calls, framer +1,907 over 1.**
  Phase 5 rewrote the index into five group tables, each under its group's
  reader sentence (47533e717 and each group's commit). It grew from 2,549
  to 4,456 bytes (`wc -c`, executed). A framer reads it whole to pick a
  `file:` (D3). What it bought: the index says which group a reader opens,
  and the 50,774-byte review record became five documents, each opened by
  its own reader. Not `worse`.
- **`README.md`: crafter +1,312 over 22 ranged calls.** Phase 5's longer
  `docs/<group>/` paths and phase 2's `seal fold` row moved it, about 60
  bytes a call. What it bought: each path names its group. Not `worse`.
- **`skills/settle/scripts/rule_changes.py`: framer +1,166 over 6 calls,
  sealer +350 over 1; `tests/skills/test_rule_changes.py`: crafter +1,230
  over 5.** Phase 2's group check (D4, S5) and its cases moved them. What
  it bought: a design can name `docs/<group>/<name>.md`, which a grouped
  root needs. Not `worse`.
- **`docs/the-record-layout.md`: framer +556 over 3 calls.** The decision
  above charges a whole read of a deleted document with every file its text
  went to. The two new documents cut from it each carry a title and a
  reader sentence (D3). This is the cost of that rule's direction, and
  phase 5 bought the fold's and the unverified record's own documents with
  it. Not `worse`.

No reading is `worse`, so no issue follows, as that paragraph says.

**Where the reading goes.** This record holds it, as the same paragraph
says for a crafter's measurement. `frame/questions.md` Q1 stays open: the
live reading is the first work item run under the installed 0.30.0. Its
default has that run's orchestrator apply this phase's commands to that
run's spawn transcripts. With that release's commit as the head, the
script's `recorded in the transcripts` line then holds what the live
spawns read. Its `EXCLUDE_DESC` names this work item's own spawns and is
the line that changes.

**No mutation is owed.** This phase adds no behaviour: it adds a record, a
closing-memo row, a Status cell and the changelog fragment. `skills/verify/SKILL.md`
*The narrow command still has to be able to fail* asks no run of a unit
that adds nothing to break.

**The narrow run (executed).** The phase-boundary set is every test module
that reads a work item's records or the changelog fragment. The list came
from `git grep -l -E 'changelog\.md|trail/phases|gaps\.md|seal/threads|"threads"|ls-files'
-- 'tests/*.py' 'tests/**/*.py'`, without `conftest.py`: 64 modules, the
closing-overview case and the censuses among them. With this record,
`gaps.md` and `changelog.md` written and staged, so that the readers that
list tracked files list them, `bin/test -q --no-header $(cat mods7.txt)`
exited 0 with 4362 passed and 1 skipped.
