# Phase 1: 1793758948-each-pair-that-can-hold-one-fact-twice-is-measured

## What this phase found

This record holds the rows of the pairs R1, R2, R3, R7 to R11 and R13 to R17, measured at `94635718ea4a79569ac612bcb814114000028be3` (`94635718e`). Every figure below is a figure at `94635718e` unless its sentence names another moment. Each count, command and draft stands once, in its row of *The table* or in the section that row cites; `gaps.md` and every draft cite the row by this path and heading. The pairs R4, R5, R6 and R12, the files F1 to F11, R18 to R21 and the editions E1 to E4 are the later phases'.

### Whether the frame holds

The frame holds, and the build follows it except where this list says. Each item is a finding or a departure, with its grounds.

- **R16 reads one file of P10.** Design *The pairs* gives R16 "M1 over whole text …, leaving out the cases a script under `evals/scripts/` writes". At `94635718e` every case under `evals/behaviour/` is such a case: the 17 `rule-*` cases are `evals/scripts/rule_cases.py`'s, the 4 `replay-*` cases `replay_targets.py`'s and the 4 `seeded-*` cases `seed_defects.py`'s (read: each generator's module docstring; executed: *Command setup*'s `check` prints `generated eval files 247` of the 248 files of P10). So R16 reads P8 against `evals/README.md` alone. The 17 fixture cases are their generator's output byte for byte (*Command R16*, second block). The 8 proofer cases were not regenerated, since their generators fetch the reviewed commits through `refs/pull/*/head`; `gaps.md` names that.
- **Which readings of two files are compared.** Design M1 reads a code file two ways, as its prose segments and as its whole text. The build compares a pair in every reading but one: a code file's segments are not compared with another code file's whole text, because the whole text already holds the segments (`probe.py#COMBOS`). R15 compares segments with segments only, and leaves a test's string constants out of its segments, since design R15 reads "test docstrings and comments" against P8 and its M2 half reads the constants. R16 compares P8's whole text with the prose of `evals/README.md`, as "M1 over whole text" says.
- **P5 holds `README.ko.md`.** #1147's design *The parts* lists it in P5, and #1147's phase 1 `PARTS` left it out (G6). This build follows the design. Its Korean text shares no 15-word run with any part this phase reads but `tests/` (*Instances R9*).
- **A module loaded from the copy writes into the copy.** The first runs loaded `skills/settle/scripts/passages.py` and, through it, `skills/verify/scripts/unverified_check.py` and `hooks/lib/`, and each wrote a `__pycache__` directory into `"$S/tree"`, whose `.pyc` files P8 then counted: P8 read 82 files where the copy tracks 78. The probe sets `sys.dont_write_bytecode`, the three directories were removed, and every count below was taken again after that (executed: `find "$S/tree" -name __pycache__` prints nothing after every block).
- **M2 over graders and prompts lists little.** The 197 graders and prompts hold 11 distinct backticked or double-quoted spans of four words or more (*Command R1*). A grader is a `regex` or `file_exists` check whose body describes what it reads, and its pattern stands in a single-quoted YAML value, which M2 does not read. Two of the 11 are the reader pairing a double quote of one front-matter value with one of the next, and none is a quote of a rule (*Instances R1*). Rows R1 and R10 name the single-quoted patterns in their open part.
- **R7's trees: no root file draws the `seal/` layout at `94635718e`.** #1147 read the tree in `README.md`, `README.ko.md` and `skills/implement/SKILL.md` at `bf9efcba` (G6, its phase 1 *Command trees*). At `94635718e` none of the three draws it, and only `seal/README.md` and `templates/setup/seal-README.md` do (*Command R7*). So R7 holds no tree on its P5 side, and the reading compares the one P6 drawing with the table `docs/layout/the-record-layout.md` *seal/* gives, which is P6 with P1 and #1147's K3.
- **R9's mechanism holds a drift in its own docstring.** Design R9 names `tests/text/test_the_rules_claude_md_names_have_one_home.py` "read for what it holds". Read whole, its module docstring states what `CLAUDE.md` holds, and `CLAUDE.md` at `94635718e` holds none of it (*Instances R9*, D2). A docstring stating the tree's own state is also R19's ground, which phase 3 measures; phase 3 cites D2 rather than drafting it again (plan row A4).
- **R11's drifted entry has a second clause whose other holder is a template.** `seal/README.md` *Layout* says of `config.md` that "no file and no row both mean the default". Within P6, `seal/config.md` states no default and defers to `templates/setup/config.md`, which says an absent `Broad gate` row "is a refusal, not a default" (read). That pair is P6 with P4, #1147's K6, which this work does not measure again (design *Scope*, Out). The clause is not counted in R11, and D1 takes it into its scope because one edit rewrites the entry.
- **R16's two drifts get no draft.** #1254 (`release: 0.32.0`) rewrites the pass rules of `evals/README.md` *The behaviour suite*, and its *Done when* makes `evals/scripts/noninferiority.py#verdict` judge what that section states (executed: `gh issue view 1254`, 2026-11-04). Both drifted statements are those pass rules and the verdict's no-result list, so a repair before #1254 is rewritten by it. Design *Scope* item 5 names a drift an open issue holds under that issue and drafts nothing. #1254's body does not name the two statements, so whether its framer is told of them is the orchestrator's call; no agent posts (contract rule 6).
- **Outside these pairs: `seal/follow-up.md` splits its table.** Line 45 is blank, inside the table of *Schedulable items with nowhere else to go*, so the four rows on lines 46 to 49 render as one paragraph and not as rows (executed: `markdown-it-py` with tables enabled over the copy finds 2 tables, 5 rows and 1 paragraph opening with `|`). `tests/text/test_a_rider_reaches_its_file.py#rows` reads every line opening with `|` and still reads them. This is no fact held twice, so no row counts it and no draft is written. The hand-back names it for the orchestrator.
- **The frame cites #1147's records at a commit the squash orphaned.** Design G6 and G16 and plan *Technical context* cite `79252e48:seal/threads/1793490088-each-kind-of-restatement-is-measured/…`, and design G7 names `79252e48` bare. `79252e48` is the tip of #1147's branch, and no `main` or release ref contains it, so `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash` refuses `frame/design.md:12`, `:22` and `frame/plan.md:10` (executed: *Phase-boundary run*). `48d035aa6`, #1147's squash on `main`, holds the same files of that directory and adds only its `guarantee.md` (executed: `git diff --stat 79252e48 48d035aa6 -- seal/threads/1793490088-each-kind-of-restatement-is-measured/`). This record reads #1147's methods there and cites `48d035aa6`. The frame's lines are the framer's, so the hand-back names them for the orchestrator.
- **Every pair is measured, and none is closed** (plan row A2). Each row's commands ran in this phase's environment.

### The table

| Label | Command | Held twice | Drifted | Open part | Home |
|---|---|---|---|---|---|
| R1 | *Command setup*; *Command R1* | 0 passages over 5,952 file pairs, and 0 of the 11 distinct grader or prompt spans held in a file of `docs/`, at `94635718e` | 0 at `94635718e`: none of the 11 spans stands in a file of P1, P2, P3 or P5, and by reading none is a quote of a rule (*Instances R1*) | a grader or prompt that states a policy rule in other words; a quote under four words; a quote in a single-quoted YAML value, such as a `pattern:` | none |
| R2 | *Command setup*; *Command R2* | 0 passages over 15 file pairs, and 1 item name, `Broad gate`, that a definition and `seal/config.md` both hold, at `94635718e` | 0 at `94635718e` (*Instances R2*) | a definition stating what `seal/README.md` says in other words; an item a definition names without backticks or without the word row or item beside it | none |
| R3 | *Command setup*; *Command R3* | 0 passages over 105 file pairs, and 2 lines of three words or more that two or more templates hold, at `94635718e` | 0 at `94635718e`: both lines are table scaffolding and state no fact (*Instances R3*) | two templates stating one form in different words, such as a foot line spelt another way | none |
| R7 | *Command setup*; *Command R7* | 0 passages over 18 file pairs, and no `seal/` tree drawn in a root file, at `94635718e` | 0 at `94635718e` (*Instances R7*) | a root file stating a fact of the records root in other words, such as where the root lives in each mode | none |
| R8 | *Command setup*; *Command R8*; *Command context* | 1 passage over 468 file pairs, at `94635718e` | 0 at `94635718e` (*Instances R8*) | a docstring, comment or printed message stating a root file's rule in other words | none |
| R9 | *Command setup*; *Command R9*; *Command context* | 6 passages over 930 file pairs, 27 pins in 12 test modules whose literal stands in a root file, and 1 statement of what `CLAUDE.md` holds, read in the module the design names, at `94635718e` | 1 at `94635718e`: `tests/text/test_the_rules_claude_md_names_have_one_home.py`'s module docstring says `CLAUDE.md` keeps a row naming each rule's home, and `CLAUDE.md` keeps none (*Instances R9*) | a test's docstring or comment stating a root file's fact in other words; a pin whose literal reaches the assert through a name, as that module's needles do. Phase 2 found one drift here, the `CONTRIBUTING.md` instance D7 drafts (`trail/phases/phase-2.md` *Whether the frame holds*, the item *Outside these pairs*) | D2 |
| R10 | *Command setup*; *Command R10* | 0 passages over 1,488 file pairs, and 0 of the 11 grader or prompt spans held in a root file, at `94635718e` | 0 at `94635718e` | as R1's, with a root file in place of a policy document | none |
| R11 | *Command setup*; *Command R11* | 0 passages over 3 file pairs, and 4 facts `seal/README.md` states that `seal/config.md` or `seal/follow-up.md` also states, read whole, at `94635718e` | 1 at `94635718e`: `seal/README.md` *Layout* names three items for `config.md`, and `seal/config.md` holds five rows, four of which that list does not name (*Instances R11*) | a fact one file implies and does not state | D1 |
| R13 | *Command setup*; *Command R13*; *Command context* | 1 passage over 465 file pairs, and 9 pins in 4 test modules whose literal stands in a records-root file, at `94635718e` | 0 at `94635718e` (*Instances R13*) | as R9's, with a records-root file in place of a root file | none |
| R14 | *Command setup*; *Command R14* | 0 passages over 744 file pairs, at `94635718e` | 0 at `94635718e` | an eval case stating a records-root fact in other words, or in runs shorter than 15 words, such as a scaffold's one-line marker | none |
| R15 | *Command setup*; *Command R15*; *Command context* | 100 passages over 12,090 file pairs between a test's docstrings and comments and P8's prose segments, and 287 pins in 50 test modules whose literal stands inside one string constant of P8, at `94635718e` | 0 at `94635718e`: each passage's holders state one fact, read at every passage, and a pin is listed only where its literal stands in a constant (*Instances R15*) | a test stating a script's behaviour in other words; a pin whose literal reaches the assert through a name; a message a script builds at run time from parts; a shell or YAML file of P8, whose constants M2 does not read. Phase 2 found one drift here, the test comment D9 drafts (`trail/phases/phase-2.md` *Whether the frame holds*, the item *Outside these pairs*) | none |
| R16 | *Command setup*; *Command R16*; *Command context* | 4 passages over 78 file pairs between P8's whole text and `evals/README.md`, the one file of P10 no generator writes, at `94635718e` | 2 at `94635718e`: `evals/README.md` lists the no-result causes without a side whose preload bytes were not recorded, and the module docstring of `evals/scripts/noninferiority.py` states rule 3 without its third condition (*Instances R16*) | the 8 proofer cases, which no command here regenerated; a statement of the verdict in other words, which shares no 15-word run | #1254 |
| R17 | *Command setup*; *Command R17*; *Command context* | 3 passages over 38,440 file pairs, at `94635718e` | 0 at `94635718e` (*Instances R17*) | a test and an eval case stating one fact in other words | none |

### Commands

Each block runs at `94635718e` against a scratch copy of that commit and reads nothing else, except *Command tracker*, which reads the tracker. Run *Command setup* first, from a clone of this repository, then the other blocks in the same shell.

#### Command setup

```sh
export S="$(mktemp -d)"
mkdir "$S/tree"
git archive 94635718ea4a79569ac612bcb814114000028be3 | tar -x -C "$S/tree"
cat > "$S/probe.py" <<'EOF'
"""#1236 phase 1: the readers of the pairs R1, R2, R3, R7 to R11 and R13 to
R17, run over the scratch copy "$S/tree" of 94635718e. The prose
normalisation is `skills/settle/scripts/passages.py` of that copy (`words`,
`WINDOW`, and the `FENCE`, `SECTION`, `SECTION_TOKEN`, `STRIP` and
`_heading_level` that `words` reads), loaded by path. Nothing outside "$S"
is read.

Ported from #1147 (`48d035aa6:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/`),
each with its changes:
  tokens            phase-2 `tokens`: reads `passages.py`'s `_lines`, `FENCE`,
                    `_heading_level`, `SECTION`, `SECTION_TOKEN` and `STRIP`
                    in place of the test module's names; `check` asserts it
                    gives `passages.words` word for word on every prose file.
  segments_of_code  phase-2 `segments_of_code`: STRIP from `passages.py`, and
                    WITH_CONSTANTS false leaves a file's string constants out.
  runs              phase-2 `runs`: the files sharing a window are found
                    through an index of one side's windows rather than a loop
                    over every pair; each file is read in each reading
                    `readings` gives it, a pair compared in the readings
                    COMBOS names, and a file of BARE without its string
                    constants. The maximal runs, and the merge of a run into
                    a longer run that contains it, are phase-2's.
  pins              phase-1 `pins`: the corpus is the part named, and for P8
                    a literal is held only inside one string constant.
  trees             phase-1 `trees`: reads `docs/layout/the-record-layout.md`
                    in place of `docs/the-record-layout.md`, and every file.
New: whole (design M1's whole-text reading), pair and context (the pair's
readings, and the words around each passage for reading it), quotes (M2
over graders and prompts), config_items (M4's item names), template_lines
(R3's lines), generated (the cases R16 leaves out) and check.
"""

import ast
import collections
import importlib.util
import io
import os
import re
import sys
import tokenize

sys.dont_write_bytecode = True  # a module loaded from the copy writes no __pycache__ into it
T = os.path.join(os.environ["S"], "tree")
_spec = importlib.util.spec_from_file_location("passages", os.path.join(T, "skills/settle/scripts/passages.py"))
PS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(PS)
W = PS.WINDOW


def read(rel):
    with open(os.path.join(T, rel), encoding="utf-8") as f:
        return f.read()


def text_of(p):
    try:
        return read(p)
    except UnicodeDecodeError:
        return None


def files():
    out = []
    for d, subs, names in os.walk(T):
        subs.sort()
        out += [os.path.relpath(os.path.join(d, n), T) for n in sorted(names)]
    return sorted(out)


ALL = files()
MD = [p for p in ALL if p.endswith(".md") and not p.endswith(".ko.md")]
PARTS = {
    "P1": [p for p in MD if p.startswith("docs/")],
    "P2": [p for p in MD if p.startswith("skills/")],
    "P3": [p for p in MD if p.startswith("agents/")],
    "P4": [p for p in ALL if p.startswith("templates/")],
    "P5": [p for p in ("README.md", "README.ko.md", "CLAUDE.md", "CONTRIBUTING.md", "SECURITY.md",
                       "TRADEMARKS.md") if p in ALL],
    "P6": ["seal/README.md", "seal/config.md", "seal/follow-up.md"],
    "P8": [p for p in ALL if p.startswith(("hooks/", "bin/", ".github/scripts/", ".github/workflows/",
                                           "evals/scripts/")) or re.match(r"skills/[^/]+/scripts/", p)],
    "P9": [p for p in ALL if p.startswith("tests/")],
    "P10": [p for p in ALL if p.startswith("evals/") and not p.startswith("evals/scripts/")],
}
# A prose file is read through `words`; a code file two ways (design M1).
CODE = set(PARTS["P8"]) | set(PARTS["P9"]) | {p for p in PARTS["P10"] if not p.endswith(".md")}
COMBOS = {("prose", "prose"), ("prose", "seg"), ("prose", "whole"), ("seg", "prose"),
          ("whole", "prose"), ("seg", "seg"), ("whole", "whole")}


def tokens(text):
    """`[(word, line)]`: TEXT normalised as `passages.words` normalises it,
    each word with the 1-based line it stands on."""
    kept, fence = [], None
    for n, line in enumerate(PS._lines(text), 1):
        opened = PS.FENCE.match(line)
        if fence:
            if (opened and opened.group(1)[0] == fence[0] and len(opened.group(1)) >= len(fence)
                    and not line.strip().strip(fence[0])):
                fence = None
            continue
        if opened:
            fence = opened.group(1)
            continue
        if PS._heading_level(line) is not None:
            continue
        kept.append((n, line))
    joined = "\n".join(line for _, line in kept)
    joined = PS.SECTION.sub(lambda m: PS.SECTION_TOKEN + "\n" * m.group(0).count("\n"), joined)
    out = []
    for (n, _), line in zip(kept, joined.split("\n")):
        out += [(w, n) for w in line.lower().translate(PS.STRIP).split()]
    return out


def norm(s, line):
    return [(w, line) for w in s.lower().translate(PS.STRIP).split()]


def segments_of_code(p, with_constants=True):
    """The prose of a code file, as a list of segments: for Python each
    docstring, each comment block and, unless WITH_CONSTANTS is false, each
    string constant of four words or more; for any other file each run of
    comment lines."""
    text = text_of(p)
    if text is None:
        return []
    segs = []
    if p.endswith(".py") or text.startswith("#!/usr/bin/env python"):
        try:
            tree = ast.parse(text)
        except SyntaxError:
            return []
        docs = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                body = node.body
                if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                        and isinstance(body[0].value.value, str):
                    docs.add(id(body[0].value))
                    seg = []
                    for k, ln in enumerate(body[0].value.value.split("\n")):
                        seg += norm(ln, body[0].value.lineno + k)
                    segs.append(seg)
        for node in ast.walk(tree):
            if with_constants and isinstance(node, ast.Constant) and isinstance(node.value, str) \
                    and id(node) not in docs and len(node.value.split()) >= 4:
                segs.append(norm(node.value, node.lineno))
        block, last = [], None
        for tok in tokenize.generate_tokens(io.StringIO(text).readline):
            if tok.type == tokenize.COMMENT:
                if last is not None and tok.start[0] != last + 1 and block:
                    segs.append(block)
                    block = []
                block += norm(tok.string.lstrip("#"), tok.start[0])
                last = tok.start[0]
        if block:
            segs.append(block)
        return segs
    block = []
    for n, line in enumerate(text.split("\n"), 1):
        m = re.match(r"^(#|::|rem\b|REM\b)(.*)", line.strip())
        if m:
            block += norm(m.group(2), n)
        elif block:
            segs.append(block)
            block = []
    if block:
        segs.append(block)
    return segs


def whole(p):
    """Design M1's second reading of a code file: its whole text, lowercased
    and stripped as `words` strips, nothing dropped, as one segment."""
    text = text_of(p)
    if text is None:
        return []
    return [[(w, n) for n, line in enumerate(text.split("\n"), 1) for w in line.lower().translate(PS.STRIP).split()]]


def readings(p, with_constants=True):
    if p in CODE:
        return {"seg": segments_of_code(p, with_constants), "whole": whole(p)}
    t = text_of(p)
    return {"prose": [tokens(t)]} if t is not None else {}


def wins(segs):
    out = {}
    for seg in segs:
        ws = [w for w, _ in seg]
        for i in range(len(ws) - W + 1):
            out.setdefault(" ".join(ws[i:i + W]), seg[i][1])
    return out


def runs(side_a, side_b, combos=COMBOS, bare=frozenset()):
    """Each maximal run of at least WINDOW words a file of SIDE_A shares with
    a file of SIDE_B, as `{run: {path: first line}}`; a run another run
    contains is that run, with the holders of both. With SIDE_A equal to
    SIDE_B each unordered pair of two files is read once. The pair is read in
    the readings COMBOS names; a file of BARE is read without its string
    constants."""
    same = side_a == side_b
    toks = {p: readings(p, p not in bare) for p in set(side_a) | set(side_b)}
    cache = {(p, r): wins(segs) for p, rs in toks.items() for r, segs in rs.items()}
    index = collections.defaultdict(set)
    for (p, r), ws in cache.items():
        if p in side_b:
            for w in ws:
                index[w].add((p, r))
    found = {}
    n_pairs = (len([p for p in side_a if toks[p]]) * (len([p for p in side_a if toks[p]]) - 1) // 2 if same
               else len([p for p in side_a if toks[p]]) * len([p for p in side_b if toks[p]]))
    for a in sorted(side_a):
        for ra, segs in toks[a].items():
            common = collections.defaultdict(set)
            for w in cache[(a, ra)]:
                for b, rb in index.get(w, ()):
                    if b != a and (ra, rb) in combos and (not same or b > a):
                        common[(b, rb)].add(w)
            for (b, rb), shared in sorted(common.items()):
                for seg in segs:
                    ws = [w for w, _ in seg]
                    start = None
                    for i in range(len(ws) - W + 2):
                        inside = i < len(ws) - W + 1 and " ".join(ws[i:i + W]) in shared
                        if inside and start is None:
                            start = i
                        if not inside and start is not None:
                            run = " ".join(ws[start:i - 1 + W])
                            h = found.setdefault(run, {})
                            h.setdefault(a, seg[start][1])
                            h.setdefault(b, cache[(b, rb)][" ".join(ws[start:start + W])])
                            start = None
    for run in sorted(found, key=len):
        longer = [r for r in found if r != run and run in r]
        if longer:
            target = found[max(longer, key=len)]
            for path, line in found.pop(run).items():
                target.setdefault(path, line)
    return found, n_pairs


def show(label, found, n_pairs, limit=300):
    rows = sorted(found.items(), key=lambda kv: (sorted(kv[1]), kv[0]))
    for n, (run, holders) in enumerate(rows, 1):
        where = " + ".join(f"{p}:{holders[p]}" for p in sorted(holders))
        print(f"{label}.{n} [{len(run.split())} words] {where}")
        print(f"    {run[:limit]}")
    print(f"{label}: {len(found)} passages over {n_pairs} file pairs")


PAIRS = {
    "R1": ("P1", "P10"), "R2": ("P3", "P6"), "R3": ("P4", "P4"), "R7": ("P5", "P6"),
    "R8": ("P5", "P8"), "R9": ("P5", "P9"), "R10": ("P5", "P10"), "R11": ("P6", "P6"),
    "R13": ("P6", "P9"), "R14": ("P6", "P10"), "R15": ("P8", "P9"), "R16": ("P8", "P10"),
    "R17": ("P9", "P10"),
}


def generated():
    """The eval cases a script under `evals/scripts/` writes: the directories
    named `rule-*` (`rule_cases.py`), `replay-*` (`replay_targets.py`) and
    `seeded-*` (`seed_defects.py`)."""
    return {p for p in PARTS["P10"] if re.match(r"evals/behaviour/[^/]+/(rule|replay|seeded)-", p)}


def pair(label):
    """Design M1 over the pair LABEL: `(found, file pairs, bare)`. R15 reads
    the docstrings and comments of tests against P8's prose segments; R16
    reads P8's whole text against `evals/` without the cases a script
    writes."""
    x, y = PAIRS[label]
    a, b = PARTS[x], PARTS[y]
    combos, bare = COMBOS, set()
    if label == "R15":
        combos, bare = {("seg", "seg")}, set(PARTS["P9"])
    if label == "R16":
        b = [p for p in b if p not in generated()]
        combos = {("whole", "prose"), ("whole", "whole")}
    found, n = runs(a, b if x != y else a, combos, bare)
    return found, n, bare


def passages(label):
    found, n, _ = pair(label)
    show(label, found, n)


def context(label, before=12, after=30):
    """For reading: each passage of LABEL with the words around it in each
    holder, BEFORE words ahead of the run and AFTER words past it."""
    found, _, bare = pair(label)
    rows = sorted(found.items(), key=lambda kv: (sorted(kv[1]), kv[0]))
    for n, (run, holders) in enumerate(rows, 1):
        print(f"== {label}.{n}")
        rw = run.split()
        for path in sorted(holders):
            for segs in readings(path, path not in bare).values():
                hit = None
                for seg in segs:
                    ws = [w for w, _ in seg]
                    for i in range(len(ws) - len(rw) + 1):
                        if ws[i:i + len(rw)] == rw:
                            hit = (ws[max(0, i - before):i], ws[i + len(rw):i + len(rw) + after])
                            break
                    if hit:
                        break
                if hit:
                    print(f"  {path}:{holders[path]}: ...{' '.join(hit[0])} [RUN] {' '.join(hit[1])}...")
                    break


def literal(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = [v.value for v in node.values if isinstance(v, ast.Constant)]
        return max(parts, key=len) if parts else None
    return None


def constants(p):
    """Each string constant of a Python file, an f-string's constant parts
    each apart, whitespace-folded."""
    t = text_of(p)
    if t is None or not (p.endswith(".py") or t.startswith("#!/usr/bin/env python")):
        return []
    try:
        tree = ast.parse(t)
    except SyntaxError:
        return []
    return [" ".join(n.value.split()) for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value.strip()]


def corpus_of(part):
    if part == "P8":
        return {p: " \x00 ".join(c) for p in PARTS["P8"] if (c := constants(p))}
    return {p: " ".join(t.split()) for p in PARTS[part] if (t := text_of(p)) is not None}


def pins(part, verbose):
    """An assert under tests/ whose test is a string literal `in` an
    expression, the literal at least four words, standing whitespace-folded
    in a file of PART (for P8, inside one string constant)."""
    corpus = corpus_of(part)
    per_module, rows = collections.Counter(), []
    for rel in [p for p in PARTS["P9"] if p.endswith(".py")]:
        for a in ast.walk(ast.parse(read(rel))):
            if not isinstance(a, ast.Assert):
                continue
            for c in ast.walk(a.test):
                if isinstance(c, ast.Compare) and len(c.ops) == 1 and isinstance(c.ops[0], ast.In):
                    lit = literal(c.left)
                    folded = " ".join(lit.split()) if lit else ""
                    if len(folded.split()) >= 4:
                        homes = [r for r, t in corpus.items() if folded in t]
                        if homes:
                            per_module[rel] += 1
                            rows.append((rel, a.lineno, folded, homes))
    if verbose:
        for rel, line, folded, homes in rows:
            print(f"{rel}:{line} {folded[:100]!r} -> {', '.join(homes[:3])}")
    for rel, k in per_module.most_common():
        print(f"{k:4} {rel}")
    print(f"pins {len(rows)} in {len(per_module)} modules, corpus {part}")


SPAN = re.compile(r"`((?:[^`\n]|\n(?![ \t]*\n))+)`|\"((?:[^\"\n]|\n(?![ \t]*\n))+)\"")


def graders_and_prompts():
    return [p for p in PARTS["P10"] if "/graders/" in p or p.endswith("/prompt.md")]


def quotes(part):
    """Each backticked or double-quoted span of at least four words in an eval
    grader or prompt, whitespace-folded: held where it stands in a file of
    PART; orphaned where it stands in no file of P1, P2, P3 or P5. One line
    per distinct span, with the files that hold it."""
    corpus = corpus_of(part)
    rule = {p: t for q in ("P1", "P2", "P3", "P5") for p, t in corpus_of(q).items()}
    spans = collections.defaultdict(list)
    for p in graders_and_prompts():
        t = read(p)
        for m in SPAN.finditer(t):
            s = " ".join((m.group(1) or m.group(2)).split())
            if len(s.split()) >= 4:
                spans[s].append(f"{p}:{t[:m.start()].count(chr(10)) + 1}")
    held = orphan = 0
    for s, where in sorted(spans.items()):
        homes = [r for r, t in corpus.items() if s in t]
        in_rule = any(s in t for t in rule.values())
        held += bool(homes)
        orphan += not in_rule
        tag = ("HELD " + ", ".join(homes[:3])) if homes else ("ORPHAN" if not in_rule else "in a rule file")
        if homes or "-v" in sys.argv:
            print(f"{tag} :: {len(where)} files, first {where[0]} :: {s[:200]!r}")
    print(f"spans {len(spans)} distinct in {len(graders_and_prompts())} graders and prompts; "
          f"held in {part} {held}; orphaned from P1, P2, P3 and P5 {orphan}")


def config_items():
    """M4 for R2: each backticked token of agents/ that equals an item name,
    or that a sentence calls a row or an item (`` `X` row``, ``row `X` ``),
    against the rows of `seal/config.md` and the items of
    `templates/setup/config.md`: the rows it shows inside its fenced
    examples, and its `## ` headings but the three that name no row."""
    def first_cells(text):
        return {c.strip() for c in re.findall(r"(?m)^\| ([^|]+?) \| .*\|$", text)} - {"Item", "---"}
    rows = first_cells(read("seal/config.md"))
    tmpl, inside = [], False
    for line in read("templates/setup/config.md").split("\n"):
        if PS.FENCE.match(line):
            inside = not inside
        elif inside:
            tmpl.append(line)
    items = first_cells("\n".join(tmpl)) | (
        set(re.findall(r"(?m)^## (.+?)\s*$", read("templates/setup/config.md")))
        - {"What no row governs", "The fold's values", "The seal mark"})
    print(f"seal/config.md rows {len(rows)}: {' / '.join(sorted(rows))}")
    print(f"templates/setup/config.md items {len(items)}: {' / '.join(sorted(items))}")
    shaped = re.compile(r"`([^`\n]+)` (?:row|item)s?\b|\b(?:row|item) `([^`\n]+)`")
    n = held = 0
    for p in PARTS["P3"]:
        for k, line in enumerate(read(p).split("\n"), 1):
            toks = {m.group(1) or m.group(2) for m in shaped.finditer(line)}
            toks |= {t for t in re.findall(r"`([^`\n]+)`", line) if t in rows | items}
            for tok in sorted(toks):
                n += 1
                where = [w for w, src in (("seal/config.md", rows), ("the template", items)) if tok in src]
                held += bool(where)
                print(f"{p}:{k} `{tok}` -> {', '.join(where) or 'NEITHER'}")
    print(f"tokens {n}; naming a row or an item {held}")


def template_lines():
    """R3: each line of three words or more, whitespace-folded, that two or
    more templates hold."""
    by = collections.defaultdict(set)
    for p in PARTS["P4"]:
        t = text_of(p)
        if t is None:
            continue
        for k, line in enumerate(t.split("\n"), 1):
            f = " ".join(line.split())
            if len(f.split()) >= 3:
                by[f].add(f"{p}:{k}")
    shared = {f: w for f, w in by.items() if len({x.rsplit(':', 1)[0] for x in w}) >= 2}
    for f, w in sorted(shared.items(), key=lambda kv: sorted(kv[1])):
        print(f"{' + '.join(sorted(w))}\n    {f[:200]}")
    print(f"lines held by two or more templates {len(shared)}")


def trees():
    """The entries of each `seal/` tree drawn with box characters in a file of
    the tree, and the file names `docs/layout/the-record-layout.md` *seal/*
    tables."""
    entry = re.compile(r"^[│ ]*[├└]── +([^ ]+)")
    for p in ALL:
        t = text_of(p)
        if t is None:
            continue
        names = [m.group(1) for line in t.split("\n") if (m := entry.match(line))]
        if "follow-up.md" in names:
            print(f"{p}: {' '.join(names)}")
    sec = read("docs/layout/the-record-layout.md").split("\n## seal/\n", 1)[1].split("\n## ", 1)[0]
    print("docs/layout/the-record-layout.md *seal/*: " + " ".join(re.findall(r"^\| `seal/([^`]+)`", sec, re.M)))


def check():
    """`tokens` gives `passages.words` word for word on every prose file."""
    bad = [p for p in ALL if p not in CODE and (t := text_of(p)) is not None
           and [w for w, _ in tokens(t)] != PS.words(t)]
    print(f"prose files {len([p for p in ALL if p not in CODE])}; tokens differs from words in {len(bad)}")
    for k, v in PARTS.items():
        print(f"{k} {len(v)}")
    print(f"generated eval files {len(generated())}; graders and prompts {len(graders_and_prompts())}")


if __name__ == "__main__":
    cmd, args = sys.argv[1], [a for a in sys.argv[2:] if a != "-v"]
    {"check": check, "passages": lambda: passages(*args), "pins": lambda: pins(args[0], "-v" in sys.argv),
     "quotes": lambda: quotes(*args), "config": config_items, "lines": template_lines,
     "trees": trees, "context": lambda: context(*args)}[cmd]()
EOF
python3 -I "$S/probe.py" check
```

The scratch copy is the tree git tracks at `94635718e` (executed: `diff` of `find "$S/tree" -type f` against `git ls-tree -r --name-only 94635718e`, no output). At `94635718e` the last block prints `prose files 457; tokens differs from words in 0`, then the size of each part, `P1 24`, `P2 26`, `P3 5`, `P4 15`, `P5 6`, `P6 3`, `P8 78`, `P9 155` and `P10 248`, and last `generated eval files 247; graders and prompts 197`. Remove `"$S"` after the last block.

#### Command R1

```sh
python3 -I "$S/probe.py" passages R1
python3 -I "$S/probe.py" quotes P1 -v
```

Last lines at `94635718e`: `R1: 0 passages over 5952 file pairs`, and `spans 11 distinct in 197 graders and prompts; held in P1 0; orphaned from P1, P2, P3 and P5 11` after the 11 lines *Instances R1* reads.

#### Command R2

```sh
python3 -I "$S/probe.py" passages R2
python3 -I "$S/probe.py" config
```

Last lines at `94635718e`: `R2: 0 passages over 15 file pairs`, and `tokens 8; naming a row or an item 3` after the 8 tokens *Instances R2* reads. Its first two lines name the 5 rows of `seal/config.md` and the 10 items of `templates/setup/config.md`.

#### Command R3

```sh
python3 -I "$S/probe.py" passages R3
python3 -I "$S/probe.py" lines
```

Last lines at `94635718e`: `R3: 0 passages over 105 file pairs` and `lines held by two or more templates 2`.

#### Command R7

```sh
python3 -I "$S/probe.py" passages R7
python3 -I "$S/probe.py" trees
```

At `94635718e` the first prints `R7: 0 passages over 18 file pairs`. The second prints a line for `seal/README.md` and one for `templates/setup/seal-README.md`, each naming `README.md config.md parity.md pact.md follow-up.md threads/<work-item-id>/` and the eight entries under `threads/`, and last `docs/layout/the-record-layout.md *seal/*: README.md config.md parity.md pact.md follow-up.md threads/<work-item-id>/`.

#### Command R8

```sh
python3 -I "$S/probe.py" passages R8
```

Last line at `94635718e`: `R8: 1 passages over 468 file pairs`.

#### Command R9

```sh
python3 -I "$S/probe.py" passages R9
python3 -I "$S/probe.py" pins P5 -v
git show 94635718e:CLAUDE.md | grep -c -E 'branch-and-release|identifiers|cadence|one batch|orchestration\.md'
```

Last lines at `94635718e`: `R9: 6 passages over 930 file pairs`, `pins 27 in 12 modules, corpus P5`, and `0`, the count of lines of `CLAUDE.md` that name a home of the module's rules (*Instances R9*); `grep -c` exits 1 where it counts no line. The third command runs from the clone and not from the copy.

#### Command R10

```sh
python3 -I "$S/probe.py" passages R10
python3 -I "$S/probe.py" quotes P5
```

Last lines at `94635718e`: `R10: 0 passages over 1488 file pairs` and `spans 11 distinct in 197 graders and prompts; held in P5 0; orphaned from P1, P2, P3 and P5 11`.

#### Command R11

```sh
python3 -I "$S/probe.py" passages R11
cat -n "$S/tree/seal/README.md" "$S/tree/seal/config.md" "$S/tree/seal/follow-up.md"
```

Last line of the first at `94635718e`: `R11: 0 passages over 3 file pairs`. The second prints the three files design M7 reads whole: 111, 13 and 54 lines.

#### Command R13

```sh
python3 -I "$S/probe.py" passages R13
python3 -I "$S/probe.py" pins P6 -v
```

Last lines at `94635718e`: `R13: 1 passages over 465 file pairs` and `pins 9 in 4 modules, corpus P6`.

#### Command R14

```sh
python3 -I "$S/probe.py" passages R14
```

Last line at `94635718e`: `R14: 0 passages over 744 file pairs`.

#### Command R15

```sh
python3 -I "$S/probe.py" passages R15
python3 -I "$S/probe.py" pins P8
python3 -I "$S/probe.py" pins P8 -v | awk '/ -> /' | awk 'NR % 29 == 1'
```

At `94635718e` the first prints `R15: 100 passages over 12090 file pairs` last, the second `pins 287 in 50 modules, corpus P8`, and the third the 10 pins *Instances R15* reads.

#### Command R16

```sh
python3 -I "$S/probe.py" passages R16
(cd "$S/tree" && python3 -I -B evals/scripts/rule_cases.py --out "$S/gen" >/dev/null); echo "generator exit $?"
for d in "$S"/gen/*/*; do diff -rq "$d" "$S/tree/evals/behaviour/${d#"$S"/gen/}" >/dev/null || echo "differs: ${d#"$S"/gen/}"; done
ls -d "$S"/gen/*/* | wc -l
```

At `94635718e` the first prints `R16: 4 passages over 78 file pairs` last. The rest is #1147's *Command regenerate* with `-B`: it prints `generator exit 0`, no `differs:` line, and `17`.

#### Command R17

```sh
python3 -I "$S/probe.py" passages R17
```

Last line at `94635718e`: `R17: 3 passages over 38440 file pairs`.

#### Command context

```sh
for r in R8 R9 R13 R15 R16 R17; do python3 -I "$S/probe.py" context "$r"; done
```

It prints each passage of the six rows that hold one, under `== <label>.<n>`, with the 12 words before the run and the 30 after it in each holder. Each instance list below was read from it, and each passage it names was opened at its coordinate where the words around it did not settle the reading.

#### Command tracker

```sh
for q in noninferiority "evals/README" "pass rules" "no result" "seal-README" "seal/README" "config.md" "Record language" "one row per item" "Mode has none" "Commit and pull request language" "absent row" "test_the_rules_claude_md_names_have_one_home" "CLAUDE.md" "one home" "carrier" "needle" "test docstring" "module docstring"; do
  gh issue list --state open --search "$q" --limit 30 --json number,title,milestone --jq '.[] | "#\(.number)\t\(.milestone.title // "-")\t\(.title)"'
done | sort -u
gh issue view 1254 --json title,milestone,body,comments
gh api 'repos/:owner/:repo/milestones?state=open&per_page=100' --jq '.[] | "\(.number)\t\(.title)\topen=\(.open_issues)\t\(.description)"'
```

Run on 2026-11-04, from the clone. The loop prints 39 open issues, each read by title, and #1254 and #1267 by body: #1254 holds R16's two drifts (*Whether the frame holds*, the R16 item), and #1267 holds #1147's untaken readings, none of them these pairs. No other open issue holds a drift this record counts. A tracker search is a search on words, so the list is a sample.

### Instances

#### Instances R1

The 11 spans *Command R1* prints, read. Six are the command `gh issue view <N> --json body,comments` with the number filled in, at line 5 of each `rule-framer-*/prompt.md`: the prompt's own instruction to the framer. One is the fixture's command `python3 -m src.textutil TEXT` (`rule-framer-loud-flag/prompt.md:5`). Two are the headings of a historical round's findings, quoted in the bodies of `proofer/seeded-5fd6b88c/graders/truth-1.md:7` and `truth-2.md:7`. Two are the reader pairing a double quote of one YAML value with one of the next, in `framer/rule-framer-generated-page/graders/shape-no-measurement-row.md:4` and in the nine `shape-findings.md` graders of the proofer cases. None is a quote of a rule, and none has drifted. The P1 side holds none of them, which the 0 held says.

#### Instances R2

*Command R2* lists 8 tokens. Three name an item. `agents/sealer.md:128` says "Choose a `Broad gate` command, or draw a stamp: the row is a person's", and `seal/config.md:10` holds the row; the template's *Broad gate* says an absent row is refused and names no command to write, which agrees. `agents/framer.md:90` and `agents/proofer.md:40` name `Record language`, an item of the template that this repository's `seal/config.md` leaves absent, so neither is a fact `seal/config.md` holds. The other 5 tokens are `frame/plan.md` twice, `## Removes` twice and `## Grounding` once, each beside the word row or item in a sentence about a plan row or a design section; none is a config item.

#### Instances R3

The 2 lines *Command R3* prints: `| | | |`, in `templates/records/sdd-design.md:17`, `templates/records/sdd-plan.md:11` and `templates/setup/parity.md:27`, and `| Field | Value |`, in `templates/records/sdd-guarantee.md:3` and `templates/setup/parity.md:12`. An empty table row and a header row each state no fact.

#### Instances R7

The one drawing of the `seal/` layout, in `seal/README.md` *Layout* and in its byte-identical source `templates/setup/seal-README.md`, names the six entries `docs/layout/the-record-layout.md` *seal/* tables, in the same order (*Command R7*). No root file draws it. Whether the drawing's `config.md` entry is right is R11's (*Instances R11*).

#### Instances R8

R8.1, 18 words in `CONTRIBUTING.md:107`, `.github/scripts/run_tests.py:42` and `bin/test:23`: the full suite is the orchestrator's, run once after the review rounds settle and before the sealer is spawned, and the contract forbids it to every agent. The three holders state one fact.

#### Instances R9

The 6 passages *Command R9* prints, read through *Command context*:

- R9.1, `CONTRIBUTING.md:122` and `tests/censuses.py:756`: what runs before any floor is checked runs on whatever `python3` starts it, and `ruff.toml` lints that set at its per-file target. One fact.
- R9.2, `CONTRIBUTING.md:416` and `tests/text/test_the_rules_claude_md_names_have_one_home.py:81`: the identifiers rule's needle, which the module copies from its home on purpose and asserts no carrier repeats. One fact.
- R9.3, `CONTRIBUTING.md:205` and `tests/text/test_the_suite_runs_with_gh_logged_out.py:36`: the conftest removes every variable starting `GITHUB_`. One fact.
- R9.4 to R9.6, `README.ko.md:305`, `README.md:302` and `README.md:291` with `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:296`, `:278` and `:274`: the case holds each edition's sentences on where the stamp's values and the refusal record are written. One fact each.

The 27 pins *Command R9* prints were read at their assert lines. Each literal stands verbatim in the root file the command names, so its two holders state the same words. Some asserts read another file that holds the same words, such as `bin/test` or the hygiene step name *both READMEs move together*, and the root file states them alike.

The module the design names, read whole. Its `RULES` pins each rule's needles in its home, `CONTRIBUTING.md` *House rules* among them; `CARRIERS` lists the files that may hold no needle, `CLAUDE.md` first; and `LINKED` lists the files that must name a home, and holds no `CLAUDE.md`. Its module docstring says otherwise of `CLAUDE.md`. Line 1 reads "The rules `CLAUDE.md` names have one home each, and `CLAUDE.md` links (#730)". Lines 11 to 13 read "So each rule now has one home, which states it, and `CLAUDE.md` keeps a row that names the home's path and section, says when the rule applies, and gives the act in one sentence of its own words", followed by a table of four rules. Lines 41 to 46 read "What this does not hold: the act sentence in a `CLAUDE.md` row is the rule in other words". At `94635718e` `CLAUDE.md` names none of the four homes (*Command R9*, third block). The module's own comment at lines 137 to 143 says the rows left: the cadence row with #940, the merge and identifiers rows with #1169, and the batch with #1177. The docstring says one of the four left. Drifted: the docstring states a `CLAUDE.md` that the tree no longer holds, and D2 drafts it.

#### Instances R11

Design M7 over `seal/README.md`, `seal/config.md` and `seal/follow-up.md`, each read whole (*Command R11*). The facts one states and another also states:

- `seal/README.md:85` and the comment at `seal/config.md:3`: `config.md` is "what this repository says about itself, one row per item". Held.
- `seal/README.md:30` and `:87`, and `seal/config.md:4`: `seal mode` writes the file and its `Mode` row. Held.
- `seal/README.md:93` and `seal/follow-up.md:5`: `follow-up.md` holds the schedulable items of a repository with no tracker. Held.
- `seal/README.md:85` to `:90`, the *Layout* entry for `config.md`, and `seal/config.md:7` to `:13`. The entry reads "one row per item: `Commit and pull request language`, `Record language`, and `Mode`, which `seal mode` reads and writes. Optional: no file and no row both mean the default". `seal/config.md` holds five rows: `Mode`, `Broad gate`, `Document token ceiling`, `Pull request seal mark` and `Release note seal mark`. Four of them are absent from the entry's list, and two of the list's three are absent from the file. `seal/config.md:4` names `templates/setup/config.md` as the document of every row, and that template has ten items (*Command R2*). Drifted: the entry lists the items as three, and the file beside it holds others. D1 drafts it, with the second clause the item *Whether the frame holds* names.

The README's other facts, such as the marker line and the two modes, have their other holders outside P6 and are other rows' or #1147's kinds.

#### Instances R13

R13.1, 15 words in `seal/config.md:10` and `tests/text/test_broad_gate_rule.py:183`: the `Broad gate` row. The test's `EXAMPLE_ROW` pins the row `templates/setup/config.md` *Broad gate* shows, and its case docstring says the template's row "puts the seconds-long linters ahead of the suite, as this repository's own row does". The two rows are the same text. One fact.

The 9 pins *Command R13* prints were read at their assert lines: 5 read `seal/follow-up.md`'s header, 2 read `seal/README.md`'s opening paragraph, and 2 read a skill or a workflow header that holds the same words as `seal/README.md`. Each literal stands verbatim in the file the command names.

#### Instances R15

The 100 passages *Command R15* prints, each read through *Command context*. In every one, a test's docstring or comment and the code it covers give the same reason for the same behaviour, often in the code's words with the test's issue or round number added. Four were opened whole because they state a table or a figure: R15.16, the environment table `.github/scripts/release_completeness_check.py:65-83` gives and `tests/text/test_a_release_cannot_ship_an_untrue_milestone.py:86-91` restates entry by entry, with the same exit codes; R15.82, R15.86 and R15.87, the figures of `skills/verify/scripts/session_cost.py` measured on one machine, which the tests quote with the same numbers. None has drifted.

The 287 pins are listed only where the literal stands inside one string constant of P8, so each listed pin's two holders state the same words. The 10 *Command R15*'s third block prints were read at their assert lines. Nine read the output, a docstring or a constant of the script whose constant holds the literal: `skills/implement/scripts/seal.py`, `skills/verify/scripts/broad_gate.py` (2), `skills/verify/scripts/session_cost.py` (2), `.github/scripts/release_completeness_check.py`, `hooks/lib/config.py`, `skills/verify/scripts/mutation_check.py` and `skills/settle/scripts/settle.py`. The tenth, `tests/behaviour/test_first_setup_asks_once.py:370`, reads the header of `templates/setup/hygiene.yml`, whose words a constant of `seal.py` also holds. The other 277 are a list and not a reading, and their identity holds by the listing.

#### Instances R16

The 4 passages *Command R16* prints, each holder opened:

- R16.1, `evals/README.md:56` and the `verdict` docstring at `evals/scripts/noninferiority.py:791`. The README reads: "A side cut short, a case the baseline ran and the new side did not, whatever its graders, a case run a different number of times, a run whose `modelUsage` is missing or short of a count, or one whose trace cannot be read or holds no tool call is no result, never a pass." The docstring ends its list with "a side whose tokens, tool calls or preload bytes are None, or whose tool calls are none". The code at `noninferiority.py:827-831` gives no result where a side's tokens, calls or bytes are None, and `:690-691` says bytes is None "where the preload's bytes were not recorded". The README's list leaves that cause out. Drifted.
- R16.2, `evals/README.md:74` and `noninferiority.py:39`: what `regrade` refuses. One fact.
- R16.3, `evals/README.md:39` and the module docstring at `noninferiority.py:43-52`. The README's rule 3 has three conditions: the pooled passes no fewer, no grader failed on every new run where the baseline passed it, "and one the baseline lacks passes every new run". The `verdict` docstring at `:784-787` and the code at `:885-890` hold all three. The module docstring states the first two and stops. Drifted.
- R16.4, `evals/README.md:43` and `noninferiority.py:860`: a grader the new side failed on every run is named. One fact.

The two drifts are one cause: `evals/README.md` *The behaviour suite*, the module docstring and the `verdict` docstring each state the verdict's rules, and each statement differs from the others. Their home is #1254 (*Whether the frame holds*, the R16 item). The commit that made each was not traced.

#### Instances R17

The 3 passages *Command R17* prints, read through *Command context*:

- R17.1, `evals/README.md:107` and `tests/evals/test_noninferiority.py:1335`: no component of the eval tree's path below the system temporary directory holds a refused word. One fact.
- R17.2, `evals/README.md:100` and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:3`: the agent reads a case's `prompt.md` and works in the repository its `scaffold.sh` builds, so neither names the run as a measurement. One fact.
- R17.3, the five `sealer/rule-sealer-*/scaffold.sh` and `tests/skills/test_pr_body.py:161`: the plan-section lines of a pull request body that `seal pr-body` writes, in a fixture body and in the case's expected body. Both are that script's form, and they hold it alike.

### Drafts

Each draft below rests on this record's measure at `94635718e`, and D2 also on `trail/phases/phase-3.md` *Instances R19*, and changes no rule of the policy root. *Command tracker* searched the open issues before each was drafted, and no open issue holds either drift.

#### D1

**Title.** `fix: seal/README.md lists three of config.md's items and says no row means the default, where the file beside it holds five rows and an absent Broad gate row is a refusal`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-1.md` at `94635718e`, *Instances R11* and *Whether the frame holds*, the R11 item.

**What is wrong.** `seal/README.md` *Layout* describes `config.md` as "what this repository says about itself, one row per item: `Commit and pull request language`, `Record language`, and `Mode`, which `seal mode` reads and writes. Optional: no file and no row both mean the default, and `Mode` has none". The list reads as the file's items. `templates/setup/config.md` documents ten, and this repository's `seal/config.md` holds five rows, four of which the list does not name. The second sentence is wrong for `Broad gate`, whose absent row `templates/setup/config.md` *Broad gate* calls "a refusal, not a default". `seal/README.md` is the copy first setup writes from `templates/setup/seal-README.md`, and `tests/behaviour/test_first_setup_asks_once.py` holds the two byte-identical, so every opted-in repository reads the same entry.

**Scope.** The `config.md` entry of *Layout* in `templates/setup/seal-README.md` and in `seal/README.md`. The entry states what the file is and names `templates/setup/config.md` as the document of each item and of what an absent row means, the way the comment at the head of `seal/config.md` already does. Out: any other line of the layout, and `templates/setup/config.md`.

**Done when.** The entry lists no items and makes no claim about an absent row that `templates/setup/config.md` contradicts. The two files stay byte-identical under the existing case. Every other sentence of the tree that lists `config.md`'s items as a closed set is found by a method the hand-back names, and corrected or named.

**Proposed milestone.** `backlog: docs drift`. Its description is "Documents, skills, templates and agent files that claim behaviour the code does not have", and the entry is a template stating a set of items and a default for `config.md` that `templates/setup/config.md` does not give. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** R11.

#### D2

**Title.** `test: the module holding the homes of the rules CLAUDE.md once named says CLAUDE.md keeps a row linking each home, and CLAUDE.md keeps none`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-1.md` at `94635718e`, *Instances R9*, and `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md` at `94635718e`, *Instances R19*.

**What is wrong.** The module docstring of `tests/text/test_the_rules_claude_md_names_have_one_home.py` says at its first line that "`CLAUDE.md` links", at lines 11 to 13 that "`CLAUDE.md` keeps a row that names the home's path and section" for each of four rules, and at lines 41 to 46 what "the act sentence in a `CLAUDE.md` row" cannot hold. At `94635718e` `CLAUDE.md` names none of the four homes. The module's own comment above `LINKED` says the rows left with #940, #1169 and #1177, and `LINKED` holds no `CLAUDE.md`. The cases hold what the module does now: each home states its needles, no carrier repeats one, and each linked file names its home. Only the prose says otherwise, and a reader of it believes `CLAUDE.md` still carries the rows. The same docstring's last paragraph, at lines 48 and 49, says "This is the shape `tests/test_the_ledger_rules_have_one_home.py` set", and that module left the tree at 5b1f6faea (#944), so a reader who opens it for the shape finds nothing (`seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-3.md` *Instances R19*).

**Scope.** That module's docstring, and its name where the docstring's new first line no longer fits it. The cases, `RULES`, `LINKED` and `CARRIERS` stay. Out: `CLAUDE.md`, and every home's text.

**Done when.** The docstring states what the module's cases hold at the commit that changes it, no row of `CLAUDE.md` it does not hold, and no module the tree does not hold offered as standing. A rename, if made, moves every citation of the old name in the same commit, by the census `skills/verify/SKILL.md` *The narrow command still has to be able to fail* asks for.

**Proposed milestone.** `backlog: docs drift`. A test docstring is none of the four kinds its description names, and it is the area whose claim, a text stating what the tree does not hold, this drift is. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** R9, and R19's instance in this docstring (`trail/phases/phase-3.md` *Instances R19*).

### Phase-boundary run

The phase adds files under this work item's directory and builds no code, so no case is written new and no `seal mutate` run is owed (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the prose row). The plan's named case, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, was seen red before `gaps.md` was written, on the line naming this work item (executed: `bin/test <that case> -q -p no:xdist`, exit 1, "1 failed", `work items with no closing overview: ['1793758948-each-pair-that-can-hold-one-fact-twice-is-measured']`).

With the records written, one command ran that case and the 28 test modules two searches list at this branch's head, the searches #1147's phase 1 *Phase-boundary run* used: the modules that read `seal/` of the tree, by `git grep -l -E 'ROOT[^\n]{0,40}("seal"|seal/)|("seal", "threads")' HEAD -- tests`, and those that walk the whole tree, by `git grep -l -E 'ls-files|os\.walk\(ROOT|glob\(.*ROOT.*\*\*' HEAD -- tests`. Of the 29 paths the two print, `tests/conftest.py` is no test module, and pytest loads it for each module it runs (executed: `bin/test <the case> <the 28 modules> -q`, exit 1, "1 failed, 1919 passed"). The named case passed. The one failure is `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash`, on the frame's three citations of `79252e48` (*Whether the frame holds*, the item on the cited commit). This phase wrote none of them (executed: `git diff 867d74676 -- frame/` prints nothing). The set is a sample of two searches, and `gaps.md` hands the rest to the broad gate.

Every command block of this record but *Command tracker* was run again from a fresh scratch copy after the record was written, and each printed what its text states (executed: the blocks extracted from this file and run in order with `bash`; the script the extracted *Command setup* writes is byte-identical to the one the counts came from, and no `__pycache__` stood in the copy at the end).
