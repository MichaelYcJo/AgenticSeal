# Phase 2: 1793490088-each-kind-of-restatement-is-measured

## What this phase found

This record holds the rows of kinds K7, K8, K10, K11, K12, K13 and K14, measured at `bf9efcbab22f421dd5255e6f2b0af77832b6b7e5` (`bf9efcba`), and the comment text the design's *Scope* item 5 defines. Every figure below is a figure at `bf9efcba` unless its sentence names another moment. Each count, command and decision stands once, in its kind's row of *The table* or in the section that row cites; `gaps.md` and every draft cite the row by this path and heading. Kinds K1 to K6 and K9 are `trail/phases/phase-1.md`'s, and this record cites its rows by that path and heading and restates none of them.

### Whether the frame holds

The frame holds, and the build follows it except where this list says. Each item is a departure, with its grounds.

- **K11 reads the prose of code text as segments, not whole files.** The design's G13 probe ran the paste check's normalisation over every `.py` whole. That normalisation drops a line opening with `#` as a heading, so in code it drops most comments and reads code as prose. *Command K11* reads, for Python, each docstring, each block of adjacent comment lines and each string constant of four words or more, and for any other file each block of comment lines, each segment apart, so no run crosses from one segment into the next.
- **K12 reads source text raw, and adds three readers a passage count does not replace.** A passage of code says nothing about whether a copy has drifted, since a copy that drifted shares a shorter run or none. *Command K12* splits each file on whitespace and drops nothing. *Command clones* compares function bodies by `ast.dump` with the name ignored. *Command entry* reads the answer each entry point gives to its streams' encoding against `hooks/lib/console.py#STREAMS`, the one fact the record (`seal/follow-up.md`, the row on `console.to_utf8()`) shows drifting in code. *Command regenerate* compares the generated eval cases with their generator byte for byte.
- **K13's corpus is the shipped text outside `seal/threads/`, `tests/` and `evals/behaviour/`.** The design names "each `path:line` coordinate in shipped text". The command reads `path:line` and `path#name` coordinates whose path names a file of the tree from the repository's top, so a name written without its directory is not read. A cited heading is left to `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which the design names as holding it. *Command figures* reads `.md` files only, through a keyword list, so it is a sample. The one drifted figure this phase found, in `hooks/lib/console.py`, was found by reading K12's instances and not by that command.
- **K14 counts no copy, so its two count columns hold its measure.** *Held twice* holds the `check: none reader:` lines in the files `.github/scripts/rules.py#RULE_FILES` names. *Drifted* holds the lines whose section no record cites, which is the design's "the records at the release tags that cite its section, as evidence its named reader read it". The fiftieth line the second line of *Command nones* counts stands in `tests/text/test_every_agent_reads_the_contract.py`, outside every rule file.
- **K8 compares each fragment with its Release, not the whole body.** A Release body holds the theme, a line per pull request and a glance table the seal job edits (`.github/scripts/publish_release_note.py`'s docstring), none of which a fragment holds. *Command K8* reads the Releases from `v0.24.0`, the first built from fragments (#1053), and leaves the notes before it to #1053's own measure.
- **The comment text stands in no record.** *Scope* item 5 defines it as the preamble and the rows of K1 to K14 copied verbatim. A stored copy would be every row a second time, which plan row A1 and the plan's second row of *Judgments of the run* refuse. *The comment* holds the preamble once and the command that joins it with the two tables, and the joined text is built in a scratch directory and measured there.
- **D6 is a comment for #1038, not a new issue.** Both checks it proposes extend #1038's list of candidates, which decides each candidate before anything is built (design G9).
- **No row of `trail/phases/phase-1.md` looked wrong** when this phase met it: K3's and K4's drafts D2 and D3 are the home of the README and layout repairs, and no phase 2 kind repeats them.

### The table

| Kind | Command | Held twice | Drifted | Caught in the record | Decision | Grounds | Issue |
|---|---|---|---|---|---|---|---|
| K7 records across work items | *Command K7*; *Command quotes*; *Command caught* | 5 passages over 477 file pairs between the records of two work items, 4 passages over 684 file pairs between a record and `docs/`, and 2 `from:` quotes of an unsettled `## Rule changes`, at `bf9efcba` | 0 at `bf9efcba`: 3 of the 5 are a template's own text, 2 a sentence each work item states of itself, 2 of the 4 the `from:` quotes, each standing in its section, and 2 a record quoting a policy sentence as it stands (*Instances K7*) | #1025, found by #1012's framer on 2026-10-25: a `from:` quoted a sentence a backlog settle had already rewritten, and `settle --apply` would have refused the design whole. #1216: at the 0.27.1 settle a released change met the cases pinning its `from` that `trail/phases/phase-1.md` *The table* row K5 counts. The round-record sample places 7 findings here; by its heading 1 is a design's rule change disagreeing with the section it changes, caught by a review round (*Instances K7*). | nothing | G1 "A script holds a gate only on a fact it reads exactly": `skills/settle/scripts/rule_changes.py#parse` and the settle's dry run read each `from` against its section, and a stale `from` is the one drift of this kind the record shows. The passages between work items are each true of its own work item, and a work item's directory leaves at the settle after its release (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). Weighed: the reader's tests cost 0.35 s in `.test_durations` at `bf9efcba` (*Command durations*), and its record is #1025's design refused before it applied. #1216 (`release: 0.28.0`) moves the meeting of a `from` with the suite to the pull request, and #1215 (`release: 0.28.0`) reads the check lines inside a `to`; this row changes neither. | none |
| K8 the release notes | *Command K8*; *Command caught* | 36 fragments published in the 7 Releases from `v0.24.0` to `v0.27.0`, each held in the tree until its settle and in its Release; no copy of the notes in the tree at `bf9efcba` | 0: each fragment's text and each of its process rows stands in its Release's body (*Command K8*) | #1053, closed in 0.24.0: the notes were kept in `changelog/` and in the Release, 26 of 58 published notes had drifted from their files, and nothing compared them for a year. The round-record sample places 18 findings here by a fragment in their `location:`; by heading none is a Release differing from its fragment (*Instances K8*). | nothing | G1 "A fact has one source, and every other place links to it": the fragment is the source, and the Release is built from it at the tag and never republished (`.github/scripts/publish_release_note.py`'s docstring, *It never republishes*); after the settle the fragment leaves the tree and the Release is the one copy. Weighed: the publisher's tests cost 5.80 s in `.test_durations` at `bf9efcba`, and what they hold is how the one copy is built; the drift #1053 measured has not recurred in the 36 fragments since. #1139 and #1153 (`release: 0.28.0`) change what a released entry links to and how the note is laid out, and keep the one copy. | none |
| K10 standing copies inside one work item's records | *Command K10*; *Command caught* | 33 passages over 226 file pairs inside the three work items at `bf9efcba` | 0 at `bf9efcba`: 17 are a row or a sentence a round carries from the round before and says so, 8 a later record quoting the claim it checks, 5 a changelog fragment and its design or plan stating the change a person sees, 1 a sentence two records each state of their own search, and 2 a section or paragraph cited by its name (*Instances K10*) | 0.24.0's 12 of 17 recurring findings stood only in a work item's own records (`docs/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading*, #1148). The round-record sample places 22 findings here; by heading 7 are a record stating what another record or the tree no longer says, each caught by a review round of its own work item, the last in `v0.25.1` (*Instances K10*). | nothing | The policy in force decides this kind: `docs/the-review-record.md` *A finding's `verdict:` decides it, and severity is for people* makes a drifted copy a finding answered by removing it and citing the home, and "one that has not drifted is no finding". None of the 33 has drifted. The 17 carried rows are what `agents/proofer.md` *Earlier rounds carry coordinates, never verdicts* asks of a round ("say in the record which facts you carried"), and each states that round's own scope. G1 "existing is no reason to keep it", weighed against removing them: a copy here lives until its work item's settle, and the review round of its own work item caught every drifted one the sample shows. #1020 (`release: 0.29.0`) holds the recurrence across rounds, which stays out (design G5). | none |
| K11 code text and the policy | *Command K11*; *Command caught* | 50 passages over 3,168 file pairs between the prose of code text and a file of `docs/`, `skills/` or `agents/`, at `bf9efcba` | 0 at `bf9efcba`: in each pair the sentence around the shared run states the same fact (*Instances K11*) | The issue names none. The round-record sample places 13 findings here; by heading 4 are a docstring or a stated limit out of step with a rule text or with the code, each caught by a review round of the work item whose diff held it (*Instances K11*). | a written rule the proofer reads, which stands | G1 "A reading that is noisy or guessed from words is reported, never used to block": whether a docstring and a rule say the same is a reading, and the 50 passages hold. Contract rule 19 asks every change to correct "every other sentence, case and citation stating it, found at least with `git grep` on its words", read by the proofer at review, and the drifts the sample shows were caught by that review. `docs/the-record-layout.md` *The root records* gives a shipped script's comment and docstring to the maintainer reading it, so a docstring stating the rule its code holds serves that reader. Weighed against one source and a link: a link in place of each of the 50 costs the maintainer a second file at each read and removes no drift measured. | none |
| K12 code and code | *Command K12*; *Command clones*; *Command entry*; *Command regenerate*; *Command layout*; *Command caught* | 62 passages over 2,775 file pairs in code text, 100 over 12,246 in `tests/` and 60 over 33,930 in `evals/`; 4 function bodies equal in two or more files of code text and 3 in `tests/`; 47 entry points, each giving an answer to which streams are made UTF-8 or none; 17 eval cases that `evals/scripts/rule_cases.py` writes, and the proofer cases `evals/scripts/replay_targets.py` and `seed_defects.py` write, at `bf9efcba` | 3 at `bf9efcba`: three scripts under `.github/scripts/` give `stderr` the handler `replace` where `hooks/lib/console.py#STREAMS` gives `backslashreplace`. Five more leave `stdin` out, and none of them reads it. 13 entry points give no answer, which `seal/follow-up.md` already holds. The equal bodies are equal, the 17 cases are byte for byte their generator's output, and the proofer cases are their generators' output but for the remote each replay scaffold reads from the clone, by round 1's measure (*Instances K12*). | `seal/follow-up.md`, the row on `console.to_utf8()`: rounds 1 and 2 of work item 1790076050 found one script without the call and the row's own figure written wrong. The round-record sample places 9 findings here; by heading 1 is a helper copied from another module that dropped a guard, caught by a review round in `v0.27.0` (*Instances K12*). | a check, as a candidate for #1038, of the answer every entry point gives, with the three drifted answers repaired; nothing for the rest | G1 "A script holds a gate only on a fact it reads exactly": which call or which pairs a `__main__` holds is read exactly, and `tests/censuses.py#entry_point` already reads it over `hooks/` (20.32 s for `tests/test_censuses.py` in `.test_durations` at `bf9efcba`). `hooks/lib/console.py`'s docstring says of the copies "what must not diverge is the ANSWER", three copies have diverged, and nothing reads `.github/scripts/` or `skills/*/scripts/`. A check with no catch of its own is #1038's to decide (design G9), so D6 drafts the candidate and D7 repairs the three answers. The rest stand. The equal bodies are a `run`, a `_load` and a `quote` or `read` helper in scripts that each run alone. `seal layout --check` refuses a byte-identical helper in two test files and names none at `bf9efcba` (*Command layout*). The generated cases equal their generator, and the one case that compares them, `tests/behaviour/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output` (3.65 s), holds the sealer's five; its weighing is open, since a case red before a commit leaves no record (`gaps.md`). | D6, D7 |
| K13 the tree's own state restated | *Command coordinates*; *Command lists*; *Command figures*; *Command history*; *Command caught* | 9 `path:line` and 113 `path#name` coordinates in shipped text naming a file of the tree, 33 blocks of shipped `.md` naming three or more and half of an enumerable source's members, and 33 figure candidates with no moment on their line, at `bf9efcba` | 3 at `bf9efcba`: `hooks/lib/cmdline.py:28` cites `hooks/dispatch.py:72` for a handler that line has not held since `v0.3.0`; `skills/verify/scripts/unverified_check.py:113` cites `tests/behaviour/test_release_hygiene.py#overwide_rows`, gone since before `v0.16.0`; and `hooks/lib/console.py:46` says "The five scripts under `skills/*/scripts/`" spell the loop inline, where 14 do. Every block and every sampled figure holds. Six more, which no command here reads, are each a docstring, comment or printed header out of step with the code of its own file, and each stands in an open issue: #146, #315, #317, #706, #710 and #1228 (*Instances K13*). | `seal/follow-up.md`, the row on a figure about a corpus stated with no moment: every hand enumeration of the class shipped short, each caught by a review round or by `survivor-check`. The two coordinates stood in 62 and 24 release tags, through `v0.27.0`, and nothing caught them. The round-record sample places 2 findings here by heading, each a frame stating the tree wrongly, caught by a review round. Each of the six an open issue holds was found by a review round of the work item that left it, and filed when that run stopped (*Instances K13*). | one source and a link for the line coordinate; a check, as a candidate for #1038, that a cited name stands in its file; the three drifts repaired; nothing for the lists; the figure class stays the follow-up row's; the six an open issue holds stay that issue's | G1 "Nothing is kept beside the tree to stay in step with it, such as a stored count or coordinate", which `docs/one-root-by-lifetime.md` *The dependency rule* states of records ("A record citing `path:line` breaks it"). The one `path:line` in shipped text that cites the tree's own code has broken, so it becomes a `path#name` (D7); the other 8 name lines of a replay case's commit, not of the tree. Whether a name stands in a file is read exactly, and 2 of the 113 names did not resolve, 1 of them drifted; #1038's candidate 3 already asks whether a dangling citation passes the citation case (#1129, folded there), so the name reader is drafted as an addition to it (D6). The figures are the class the follow-up row holds for the owner, which says "a grep matches a spelling while the class is a kind of claim"; *Command figures* is one more such grep, so the row stands and D7 repairs the figure found. Each block that names most of a source was read, and each names the members its sentence needs (*Instances K13*). The six an open issue holds state what the code of their own file does, which shares no run with another file and is no coordinate, list or figure, so whether each still says it is a reading, the one G1 "A reading that is noisy or guessed from words is reported, never used to block" leaves to a person, and the review rounds that found them made it. Each issue holds its instance's repair and its *Done when*, and a draft or a comment would add only that the sentence stands at `bf9efcba`, which the open issue already claims; D7 does not take them, since one repair would then stand in two work items. | D6, D7 |
| K14 the rules no test holds | *Command nones*; *Command cited* | 49 `check: none reader:` lines in the rule files `.github/scripts/rules.py#RULE_FILES` names, under 40 sections, naming 26 readers, at `bf9efcba` | K14 counts no copy. Its measure here: 4 of the 49 stand in a section no record cites at the 32 release tags from `v0.15.0` to `v0.27.0`, and 15 of the 30 that name a proofer, a round or the sealer stand in a section no record of that party's kind cites (*Instances K14*) | The owner's first comment on #1147, item 3: 33 such lines at `6be0c1f1`, which #1148 kept as the constructive list of the rules with no test. | nothing | G1 "A reading that is noisy or guessed from words is reported, never used to block": a citation is one trace of a reader having read a rule, and a proofer that applies a rule without naming it leaves none, so the count says where no trace stands, not that nobody read. Of the four with no trace, contract rule 13's reader is the proofer, and three sections of `skills/legacy-parity/SKILL.md` name the parity review, which this repository never runs, since it declares no `seal/parity.md`. Each line costs one line of its rule file and is read by `seal rules --check` (2.51 s for `tests/github/test_rules.py` in `.test_durations` at `bf9efcba`). #1147's *Order* says its decisions feed #1038, which reads this table, and the owner's comment item 3 makes a change to the lines an issue of its own; this row decides none. | none |

### Commands

Each block runs at `bf9efcba` against a scratch copy of that commit and reads nothing else, except where its text says. Run `trail/phases/phase-1.md` *Command setup* first, from a clone of this repository that holds the release tags, then *Command setup* below in the same shell.

#### Command setup

```sh
cat > "$S/audit2.py" <<'EOF'
"""#1147 phase 2: the readers of K7, K8 and K10 to K14, run over the scratch
copy "$S/tree" of bf9efcba. It imports phase 1's helper "$S/audit.py" for
the verbatim normalisation and the parts, and adds the parts phase 2 reads.
Nothing outside "$S" is read, except `releases`, `cited` and `caught`,
which read git objects of the repository named as their argument, and
`releases`, which also reads the GitHub Releases through `gh`."""

import ast
import collections
import importlib.util
import io
import itertools
import json
import os
import re
import subprocess
import sys
import tokenize

sys.path.insert(0, os.environ["S"])
import audit  # noqa: E402

T, ALL, MD, read = audit.T, audit.ALL, audit.MD, audit.read
NS = audit.reader()
W, WORDS, WINDOWS = NS["WINDOW"], NS["words"], NS["windows"]
P1, P2, P3 = audit.PARTS["P1"], audit.PARTS["P2"], audit.PARTS["P3"]
P7 = [p for p in ALL if p.startswith("seal/threads/") and p.endswith(".md")]
P8 = [p for p in ALL
      if p.startswith(("hooks/", "bin/", ".github/scripts/", ".github/workflows/", "evals/scripts/"))
      or re.match(r"skills/[^/]+/scripts/", p)]
P9 = [p for p in ALL if p.startswith("tests/")]
P10 = audit.PARTS["P10"]


def text_of(p):
    try:
        return read(p)
    except UnicodeDecodeError:
        return None


def item(p):
    return p.split("/")[2]


def tokens(text):
    """`[(word, line)]`: TEXT normalised as `words` normalises it, each word
    with the 1-based line it stands on. A quoted section name that wraps
    becomes one token on its first line."""
    kept, fence = [], None
    for n, line in enumerate(NS["lines"](text), 1):
        opened = NS["FENCE"].match(line)
        if fence:
            if (opened and opened.group(1)[0] == fence[0] and len(opened.group(1)) >= len(fence)
                    and not line.strip().strip(fence[0])):
                fence = None
            continue
        if opened:
            fence = opened.group(1)
            continue
        if NS["HEADING"].match(line):
            continue
        kept.append((n, line))
    joined = "\n".join(line for _, line in kept)
    joined = NS["SECTION"].sub(lambda m: NS["SECTION_TOKEN"] + "\n" * m.group(0).count("\n"), joined)
    out = []
    for (n, _), line in zip(kept, joined.split("\n")):
        out += [(w, n) for w in line.lower().translate(NS["STRIP"]).split()]
    return out


def segments_of_code(p):
    """The prose of a code file, as a list of segments: for Python each
    docstring, each comment block and each string constant of four words or
    more; for any other file each run of comment lines. Each segment is
    `[(word, line)]`, normalised as `words` normalises prose."""
    text = text_of(p)
    if text is None:
        return []
    segs = []

    def norm(s, line):
        return [(w, line) for w in s.lower().translate(NS["STRIP"]).split()]

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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docs \
                    and len(node.value.split()) >= 4:
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
        s = line.strip()
        m = re.match(r"^(#|::|rem\b|REM\b)(.*)", s)
        if m:
            block += norm(m.group(2), n)
        elif block:
            segs.append(block)
            block = []
    if block:
        segs.append(block)
    return segs


def runs(pairs, toks):
    """Each maximal run of at least WINDOW words a pair shares, as
    `{run: {path: first line}}`; a run another run contains is that run, with
    the holders of both. TOKS maps a path to a list of segments."""
    def wins(segs):
        out = {}
        for seg in segs:
            ws = [w for w, _ in seg]
            for i in range(len(ws) - W + 1):
                out.setdefault(" ".join(ws[i:i + W]), seg[i][1])
        return out

    cache = {p: wins(toks[p]) for p in {x for pair in pairs for x in pair}}
    found = {}
    for a, b in sorted(pairs):
        common = cache[a].keys() & cache[b].keys()
        if not common:
            continue
        for seg in toks[a]:
            ws = [w for w, _ in seg]
            start = None
            for i in range(len(ws) - W + 2):
                inside = i < len(ws) - W + 1 and " ".join(ws[i:i + W]) in common
                if inside and start is None:
                    start = i
                if not inside and start is not None:
                    run = " ".join(ws[start:i - 1 + W])
                    h = found.setdefault(run, {})
                    h[a] = seg[start][1]
                    h[b] = cache[b][" ".join(ws[start:start + W])]
                    start = None
    for run in sorted(found, key=len):
        longer = [r for r in found if r != run and run in r]
        if longer:
            target = found[max(longer, key=len)]
            for path, line in found.pop(run).items():
                target.setdefault(path, line)
    return found


def show(label, found, pairs, limit=300):
    rows = sorted(found.items(), key=lambda kv: (sorted(kv[1]), kv[0]))
    for n, (run, holders) in enumerate(rows, 1):
        where = " + ".join(f"{p}:{holders[p]}" for p in sorted(holders))
        print(f"{label}.{n} [{len(run.split())} words] {where}")
        print(f"    {run[:limit]}")
    print(f"{label}: {len(found)} passages over {len(pairs)} file pairs")


def prose(paths):
    return {p: [tokens(t)] for p in paths if (t := text_of(p)) is not None}


def records(scope):
    """K7 (`across`, `policy`) and K10 (`inside`): the records' passages."""
    toks = prose(P7 + P1)
    if scope == "across":
        pairs = {tuple(sorted(x)) for x in itertools.combinations(P7, 2) if item(x[0]) != item(x[1])}
    elif scope == "inside":
        pairs = {tuple(sorted(x)) for x in itertools.combinations(P7, 2) if item(x[0]) == item(x[1])}
    else:
        pairs = {(b, a) for a in P7 for b in P1}
    show({"across": "K7", "policy": "K7p", "inside": "K10"}[scope], runs(pairs, toks), pairs)


def quotes():
    """K7: each `from:` of an unsettled design's `## Rule changes`, read by
    `skills/settle/scripts/rule_changes.py#parse` of the scratch copy, against
    the section it names, whitespace-folded."""
    spec = importlib.util.spec_from_file_location("rc", os.path.join(T, "skills/settle/scripts/rule_changes.py"))
    rc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rc)
    n = held = 0
    for design in sorted(p for p in P7 if p.endswith("/frame/design.md")):
        parsed = rc.parse(read(design), "docs")
        for op in parsed.ops or ():
            if op.old is None:
                continue
            n += 1
            doc = read(op.file)
            span, _ = rc.section_lines(doc, op.section)
            lines = rc.reader().gfm_lines(doc)
            body = " ".join(" ".join(lines[span[0] - 1:span[1]]).split()) if span else ""
            ok = " ".join(op.old.split()) in body
            held += ok
            print(f"{design}:{op.line} {op.kind} {op.file} *{op.section}*: from {'stands' if ok else 'DOES NOT STAND'}")
    print(f"from quotes {n}; standing in their section {held}")


def code(scope):
    """K11 (`policy`): the prose of code text against the rule documents.
    K12 (`P8`, `P9`, `P10`): source text shared between two files of one
    part, read raw: split on whitespace, nothing dropped, a line per word."""
    if scope == "policy":
        toks = {p: s for p in P8 if (s := segments_of_code(p))}
        toks.update(prose(P1 + P2 + P3))
        pairs = {(a, b) for a in P8 if a in toks for b in P1 + P2 + P3 if b in toks}
        show("K11", runs(pairs, toks), pairs)
        return
    part = {"P8": P8, "P9": P9, "P10": P10}[scope]
    toks = {}
    for p in part:
        t = text_of(p)
        if t is not None:
            toks[p] = [[(w, n) for n, line in enumerate(t.split("\n"), 1) for w in line.split()]]
    pairs = {tuple(sorted(x)) for x in itertools.combinations(sorted(toks), 2)}
    found = runs(pairs, toks)
    groups = collections.Counter()
    for run, holders in found.items():
        groups[" + ".join(sorted({re.sub(r"/[^/]+$", "/", p) if scope != "P10" else "/".join(p.split("/")[:2]) + "/"
                                  for p in holders}))] += 1
    for g, k in groups.most_common(25):
        print(f"{k:5} {g}")
    big = sorted(found.items(), key=lambda kv: -len(kv[1]))[:15]
    for run, holders in big:
        print(f"  [{len(run.split())} words, {len(holders)} holders] {', '.join(sorted(holders)[:4])}{' ...' if len(holders) > 4 else ''}")
        print(f"      {run[:160]}")
    print(f"K12 {scope}: {len(found)} passages over {len(pairs)} file pairs; holders {sum(len(h) for h in found.values())}")


def clones():
    """K12: each function body of a Python file of P8, P9 or P10, its
    docstring left out and its name ignored, that stands with an equal
    `ast.dump` in another file of the same part, at three statements or more
    counted through every nested block."""
    for label, part in (("P8", P8), ("P9", P9), ("P10", P10)):
        by = collections.defaultdict(list)
        for p in part:
            if not p.endswith(".py"):
                continue
            try:
                tree = ast.parse(text_of(p))
            except (SyntaxError, TypeError):
                continue
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    body = node.body[1:] if (node.body and isinstance(node.body[0], ast.Expr)
                                             and isinstance(node.body[0].value, ast.Constant)) else node.body
                    stmts = sum(isinstance(n, ast.stmt) for b in body for n in ast.walk(b))
                    if stmts >= 3:
                        by[ast.dump(ast.Module(body, []))].append((p, node.lineno, node.name))
        groups = [defs for defs in by.values() if len({p for p, _, _ in defs}) >= 2]
        for defs in sorted(groups, key=lambda d: d[0][0]):
            print(f"{label} " + ", ".join(f"{p}:{n}#{name}" for p, n, name in defs))
        print(f"{label}: {len(groups)} function bodies equal in two or more files")


def entry_points():
    """K12: each Python file of P8 with `if __name__ == "__main__"`, and the
    answer it gives to which streams are made UTF-8 with which `errors`:
    `hooks/lib/console.py#STREAMS` where it calls `console.to_utf8()`, the
    `(stream, errors)` pairs its own loop names where it reconfigures in
    place, or none. Each answer is set against `STREAMS`."""
    src = read("hooks/lib/console.py")
    streams = tuple(re.findall(r'\("(std\w+)", "(\w+)"\)', src.split("STREAMS = ", 1)[1].split("\n", 1)[0]))
    tally = collections.Counter()
    for p in sorted(P8):
        t = text_of(p) or ""
        if not (p.endswith(".py") and re.search(r"^if __name__ == ['\"]__main__['\"]", t, re.M)):
            continue
        if "console.to_utf8()" in t:
            answer, how = streams, "calls console.to_utf8()"
        elif ".reconfigure(" in t:
            pairs = tuple(re.findall(r'\("(std\w+)",\s*"(\w*replace|strict|ignore|surrogateescape)"\)', t))
            if not pairs:
                loop = re.search(r'for _?name in \(([^)]*)\):(?:.|\n){0,200}?errors="(\w+)"', t)
                pairs = tuple((n, loop.group(2)) for n in re.findall(r'"(std\w+)"', loop.group(1))) if loop else ()
            answer, how = pairs, "its own loop"
        else:
            answer, how = (), "none"
        same = "the same as STREAMS" if answer == streams else "differs from STREAMS" if answer else "no answer"
        tally[(how, same, answer)] += 1
        print(f"{p}: {how}; {same}: {' '.join(f'{n}={e}' for n, e in answer)}")
    for (how, same, answer), k in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"{k:3} {how}, {same}: {' '.join(f'{n}={e}' for n, e in answer) or '-'}")
    print(f"entry points {sum(tally.values())}")


SHIPPED = [p for p in ALL if not p.startswith(("seal/threads/", "tests/", "evals/behaviour/"))
           and not p.endswith((".png", ".svg", ".ico"))]


def coordinates():
    """K13: each `path:line` and `path#name` coordinate in a file outside
    `seal/threads/`, `tests/` and `evals/behaviour/`, that names a file of the
    tree. A `path:line` past the file's end, or a `path#name` whose name no
    line of the file defines or assigns, is printed, and each printed one is
    read before it counts as drifted."""
    line_re = re.compile(r"(?<![\w./-])((?:[\w-]+/)*[\w.-]+\.(?:py|md|yml|yaml|json|sh|toml)):(\d+)(?:-(\d+))?")
    name_re = re.compile(r"(?<![\w./-])((?:[\w-]+/)*[\w.-]+\.py)#(\w+)")
    exists = set(ALL)
    n_line = n_name = 0
    bad = []
    lines_ok = []
    for p in SHIPPED:
        t = text_of(p)
        if t is None:
            continue
        for k, line in enumerate(t.split("\n"), 1):
            for m in line_re.finditer(line):
                path, a = m.group(1), int(m.group(2))
                if path not in exists:
                    continue
                n_line += 1
                length = len(read(path).split("\n"))
                if a > length or (m.group(3) and int(m.group(3)) > length):
                    bad.append(f"past the end: {p}:{k} -> {m.group(0)} ({length} lines)")
                else:
                    lines_ok.append(f"{p}:{k} -> {m.group(0)}")
            for m in name_re.finditer(line):
                path, name = m.group(1), m.group(2)
                if path not in exists:
                    continue
                n_name += 1
                src = read(path)
                if not re.search(rf"^\s*(?:async\s+)?(?:def|class)\s+{name}\b|^\s*{name}\s*[:=]|^\s*{name}\s*,|,\s*{name}\s*=", src, re.M):
                    bad.append(f"name not defined: {p}:{k} -> {m.group(0)}")
    print("\n".join(bad))
    if "-v" in sys.argv:
        print("\n".join(lines_ok))
    print(f"path:line coordinates {n_line}; path#name coordinates {n_name}; printed for reading {len(bad)}")


def _config_items():
    text = read("templates/setup/config.md")
    heads = re.findall(r"(?m)^## (.+?)\s*$", text)
    fold = text.split("\n## The fold's values", 1)[1]
    return sorted([h for h in heads if h not in ("What no row governs", "The fold's values")]
                  + re.findall(r"(?m)^\| `([^`]+)` \|", fold))


def _subcommands():
    out = subprocess.run([sys.executable, "-I", os.path.join(T, "skills/implement/scripts/seal.py"), "--help"],
                         capture_output=True, text=True).stdout
    return sorted(re.search(r"\{([\w,-]+)\}", out).group(1).split(","))


SOURCES = {
    "hooks": lambda: sorted(os.path.basename(p)[:-3] for p in ALL
                            if re.fullmatch(r"hooks/[\w-]+\.py", p) and p != "hooks/dispatch.py"),
    "agents": lambda: sorted(os.path.basename(p)[:-3] for p in P3),
    "skills": lambda: sorted(p.split("/")[1] for p in ALL if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)),
    "templates": lambda: sorted(os.path.basename(p) for p in ALL if p.startswith("templates/")),
    "config items": _config_items,
    "seal subcommands": _subcommands,
}


def lists():
    """K13: each block (a paragraph, a list or a table) of a shipped `.md`
    that names at least three members of an enumerable source and at least
    half of them, against that source. A block naming every member holds;
    one that names most and not all is printed for reading."""
    blocks = 0
    for name, src in SOURCES.items():
        members = src()
        print(f"== {name}: {len(members)} at bf9efcba: {' '.join(members)}")
        for p in [q for q in SHIPPED if q.endswith(".md") and not q.endswith(".ko.md")]:
            for block in re.split(r"\n\s*\n", read(p)):
                named = [m for m in members if re.search(rf"(?<![\w-]){re.escape(m)}(?![\w-])", block)]
                if len(named) >= 3 and len(named) * 2 >= len(members):
                    missing = sorted(set(members) - set(named))
                    line = read(p)[:read(p).index(block)].count("\n") + 1
                    blocks += 1
                    print(f"  {p}:{line} names {len(named)} of {len(members)}"
                          + (f"; not named: {' '.join(missing)}" if missing else "; all"))
    print(f"blocks naming three or more and half of a source {blocks}")


def figures():
    """K13: each figure about the tree in a shipped `.md` outside
    `seal/threads/`: a number before a noun that counts files, cases or
    rules, with no commit, date or `at` near it. A keyword candidate list,
    read by sample."""
    noun = r"(?:files?|cases?|modules?|hooks?|entry points?|rules?|tests?|scripts?|agents?|skills?|templates?|subcommands?|checks?|documents?|sections?)"
    fig = re.compile(rf"\b(\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|twenty)\s+(?:\w+\s+){{0,2}}{noun}\b", re.I)
    moment = re.compile(r"\b[0-9a-f]{7,40}\b|\b20\d\d-\d\d-\d\d\b|\bv?0\.\d+\.\d+\b|\bat `|\bmeasured\b|#\d+", re.I)
    n = 0
    out = []
    for p in [q for q in SHIPPED if q.endswith(".md") and not q.endswith(".ko.md")]:
        for k, line in enumerate(read(p).split("\n"), 1):
            for m in fig.finditer(line):
                if m.group(1).lower() in ("two", "one") and not re.search(r"\b(the|all|every|both)\s+" + m.group(1), line, re.I):
                    continue
                if moment.search(line):
                    continue
                n += 1
                out.append(f"{p}:{k} {m.group(0)!r}")
    if "-v" in sys.argv:
        print("\n".join(out))
    print(f"figure candidates with no moment on their line {n}")
    return out


def nones():
    """K14: each `check: none reader:` line of a rule file
    (`.github/scripts/rules.py#RULE_FILES`), with the heading it stands
    under and its reader."""
    spec = importlib.util.spec_from_file_location("rules", os.path.join(T, ".github/scripts/rules.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(T, ".github/scripts"))
    spec.loader.exec_module(mod)
    import glob
    out = []
    for pat in mod.RULE_FILES:
        for path in sorted(glob.glob(os.path.join(T, pat))):
            rel = os.path.relpath(path, T)
            head = None
            for k, line in enumerate(read(rel).split("\n"), 1):
                h = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
                if h:
                    head = h.group(1)
                if line.startswith("check: none reader: "):
                    out.append((rel, k, head, line[len("check: none reader: "):].strip()))
    return out


def show_nones():
    rules = nones()
    for r, k, h, w in rules:
        print(f"{r}:{k} *{h}* {w}")
    print(f"check: none lines {len(rules)} in {len({(r, h) for r, _, h, _ in rules})} sections, "
          f"naming {len({w for *_, w in rules})} readers")


def cited(repo):
    """K14: for each rule `nones` lists, the records at the release tags
    v0.15.0 to v0.27.0 that cite its section: a record whose text, folded and
    with `*` and backticks dropped, holds the file's path followed within
    80 characters by the heading's words, or for a contract rule `contract
    rule <N>` or `contract rules ... <N>`. Each record path is counted once,
    by kind: round, guarantee, other. A rule whose reader names the proofer
    or a round is counted again by round records alone, and one naming the
    sealer by `guarantee.md` alone."""
    def git(*a):
        return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout

    tags = [t for t in git("tag", "--sort=creatordate").split() if re.fullmatch(r"v0\.(1[5-9]|2\d)\.\d+", t)]
    texts = {}
    for tag in tags:
        for rel in git("ls-tree", "-r", "--name-only", tag, "--", "seal/").split("\n"):
            if rel.endswith(".md") and rel.startswith(("seal/specs/", "seal/threads/")) and rel not in texts:
                texts[rel] = " ".join(git("show", f"{tag}:{rel}").replace("*", "").replace("`", "").split())
    rules = nones()
    none_any = none_own = 0
    owed = 0
    for rel, k, head, who in rules:
        num = re.match(r"(\d+)\s", head or "")
        if rel == "skills/agent-contract/SKILL.md" and num:
            pat = re.compile(rf"\bcontract rules? (?:\d+, |\d+ and )*{num.group(1)}\b")
        else:
            h = " ".join((head or "").replace("*", "").replace("`", "").split())
            pat = re.compile(re.escape(rel) + r".{0,80}?" + re.escape(h))
        hits = [r for r, t in texts.items() if pat.search(t)]
        kind = lambda r: ("round" if "round" in r.rsplit("/", 1)[-1] else  # noqa: E731
                          "guarantee" if r.endswith("guarantee.md") else "other")
        kinds = collections.Counter(kind(r) for r in hits)
        own = "round" if re.search(r"proofer|round|review", who) else "guarantee" if "sealer" in who else None
        none_any += not hits
        if own:
            owed += 1
            none_own += not kinds[own]
        print(f"{rel}:{k} *{head}* reader '{who}': {len(hits)} records "
              f"(round {kinds['round']}, guarantee {kinds['guarantee']}, other {kinds['other']})"
              + (f"; by its reader's kind ({own}) {kinds[own]}" if own else ""))
    print(f"records read: {len(texts)} at {len(tags)} tags")
    print(f"check: none lines in rule files {len(rules)}; cited by no record {none_any}; "
          f"naming a proofer, a round or the sealer {owed}, of which cited by no record of that kind {none_own}")


def caught(repo):
    """Each finding of a round record at a release tag v0.15.0 or later whose
    text before its first fence matches KEY, placed in a phase 2 kind by the
    paths its `location:` line names, and K13 by its heading's words. A
    keyword sample: a drift worded otherwise is not listed, and a listed one
    is read before it counts."""
    key = re.compile(r"drift|restat|stale|second copy|copy of|copies|a copy|disagree|contradict|"
                     r"out of step|no longer (says|matches|states|exists|stands)|"
                     r"names? (a|the) (file|function|line|section) (that|which) (is gone|does not exist)", re.I)
    k13 = re.compile(r"coordinate|line number|:\d+ (is|was|names)|figure|stated count|count (of|is) (wrong|stale)|"
                     r"no moment|enumerat|list(s|ed)? (of|is) (short|incomplete)|points? at (a|the) (wrong|old)", re.I)
    path = re.compile(r"`?([\w./<>*-]+\.(?:md|py|yml|yaml|json|toml|sh))")

    def git(*a):
        return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout

    def part(p):
        if p.startswith(("seal/threads/", "seal/specs/")):
            return "P7"
        for pre, name in (("docs/", "P1"), ("agents/", "P3"), ("tests/", "P9"), ("evals/scripts/", "P8"),
                          ("evals/", "P10"), ("hooks/", "P8"), ("bin/", "P8"), (".github/", "P8")):
            if p.startswith(pre):
                return name
        if p.startswith("skills/"):
            return "P8" if "/scripts/" in p else "P2"
        return None

    def kinds(paths, head):
        ps = [(p, part(p)) for p in set(paths)]
        out = set()
        recs = [p for p, x in ps if x == "P7"]
        items = {p.split("/")[2] for p in recs if len(p.split("/")) > 3}
        if len(items) >= 2 or (recs and any(x == "P1" for _, x in ps)):
            out.add("K7")
        if len(recs) >= 2 and len(items) == 1:
            out.add("K10")
        if any(x == "P8" for _, x in ps) and any(x in ("P1", "P2", "P3") for _, x in ps):
            out.add("K11")
        for x in ("P8", "P9", "P10"):
            if sum(1 for _, y in ps if y == x) >= 2:
                out.add("K12")
        if any(p.endswith("changelog.md") or p.endswith("publish_release_note.py") for p, _ in ps):
            out.add("K8")
        if k13.search(head):
            out.add("K13")
        return out

    seen = {}
    tags = [t for t in git("tag", "--sort=creatordate").split() if re.fullmatch(r"v0\.(1[5-9]|2\d)\.\d+", t)]
    for tag in tags:
        for rel in git("ls-tree", "-r", "--name-only", tag, "--", "seal/").split("\n"):
            if not (rel.endswith(".md") and "round" in rel.rsplit("/", 1)[-1]):
                continue
            for block in re.split(r"(?m)^### ", git("show", f"{tag}:{rel}"))[1:]:
                head = block.split("\n", 1)[0].strip()
                loc = re.search(r"(?m)^location:(.*)$", block)
                if (rel, head) in seen or not loc or not key.search(block.split("\n```", 1)[0]):
                    continue
                ks = kinds(path.findall(loc.group(1)), head)
                if ks:
                    seen[(rel, head)] = (tag, sorted(ks))
    for (rel, head), (tag, ks) in sorted(seen.items(), key=lambda kv: (kv[1][1], kv[1][0], kv[0])):
        print(f"{','.join(ks)} {tag} {rel} :: {head[:110]}")
    print(f"findings {len(seen)}; " + "; ".join(
        f"{k} {sum(1 for v in seen.values() if k in v[1])}" for k in ("K7", "K8", "K10", "K11", "K12", "K13")))


def releases(repo):
    """K8: each GitHub Release built from changelog fragments (v0.24.0, #1053,
    and after), against the fragments `publish_release_note.py#fragments` of
    the scratch copy reads for its range: each fragment's text without its
    process section, and each process row, whitespace-folded, stands in the
    published body or is named."""
    spec = importlib.util.spec_from_file_location("prn", os.path.join(T, ".github/scripts/publish_release_note.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.ROOT = repo
    fold = lambda s: " ".join(s.split())  # noqa: E731
    heading = m.process_shape()[0]
    total = missing = 0
    for tag in ("v0.24.0", "v0.24.1", "v0.24.2", "v0.25.0", "v0.25.1", "v0.26.0", "v0.27.0"):
        body = json.loads(subprocess.run(["gh", "release", "view", tag, "--json", "body"], cwd=repo,
                                         capture_output=True, text=True, check=True).stdout)["body"]
        entries = m.fragments(m.commit_range(m.previous_tag(tag), tag))
        gone = []
        for work, frag in entries:
            rest, rows = m.split_process(frag, heading)
            if fold(rest) not in fold(body):
                gone.append(work)
            gone += [f"{work} row" for r in rows if fold(r) not in fold(body)]
        total += len(entries)
        missing += len(gone)
        print(f"{tag}: {len(entries)} fragments; not in the Release body: {len(gone)} {' '.join(gone)}")
    print(f"fragments {total}; not in their Release {missing}")


if __name__ == "__main__":
    cmd, args = sys.argv[1], [a for a in sys.argv[2:] if a != "-v"]
    {"records": lambda: records(*args), "quotes": quotes, "code": lambda: code(*args),
     "clones": clones, "entry": entry_points, "coordinates": coordinates, "lists": lists,
     "figures": figures, "nones": lambda: show_nones(),
     "cited": lambda: cited(*args), "caught": lambda: caught(*args), "releases": lambda: releases(*args)}[cmd]()
EOF
```

`"$S/audit.py"` is phase 1's helper, written by its *Command setup*; this block adds nothing to it. Remove `"$S"` after the last block.

#### Command K7

```sh
python3 -I "$S/audit2.py" records across
python3 -I "$S/audit2.py" records policy
```

Last lines at `bf9efcba`: `K7: 5 passages over 477 file pairs` and `K7p: 4 passages over 684 file pairs`.

#### Command quotes

```sh
python3 -I "$S/audit2.py" quotes
```

Last line at `bf9efcba`: `from quotes 2; standing in their section 2`.

#### Command K8

```sh
python3 -I "$S/audit2.py" releases "$(git rev-parse --show-toplevel)"
git ls-tree -r --name-only bf9efcba | grep -i -E '(^|/)(changelog|CHANGELOG|release-notes)' | grep -v -E '^seal/threads/[^/]+/changelog\.md$'; echo "grep exit $?"
```

Run on 2026-11-01. The first prints one line per Release from `v0.24.0` to `v0.27.0` with 16, 5, 4, 1, 2, 5 and 3 fragments, each with 0 not in its body, and last `fragments 36; not in their Release 0`. The second prints no path and `grep exit 1`: the only files of that name at `bf9efcba` are the three work items' fragments.

#### Command K10

```sh
python3 -I "$S/audit2.py" records inside
```

Last line at `bf9efcba`: `K10: 33 passages over 226 file pairs`.

#### Command K11

```sh
python3 -I "$S/audit2.py" code policy
```

Last line at `bf9efcba`: `K11: 50 passages over 3168 file pairs`.

#### Command K12

```sh
python3 -I "$S/audit2.py" code P8
python3 -I "$S/audit2.py" code P9
python3 -I "$S/audit2.py" code P10
```

Last lines at `bf9efcba`: `K12 P8: 62 passages over 2775 file pairs; holders 164`, `K12 P9: 100 passages over 12246 file pairs; holders 220` and `K12 P10: 60 passages over 33930 file pairs; holders 367`. Each first prints the passages grouped by the directories that hold them, and the fifteen with the most holders.

#### Command clones

```sh
python3 -I "$S/audit2.py" clones
```

At `bf9efcba` it prints `P8: 4 function bodies equal in two or more files`, `P9: 3 function bodies equal in two or more files` and `P10: 0 function bodies equal in two or more files`, each after the groups it names.

#### Command entry

```sh
python3 -I "$S/audit2.py" entry
```

At `bf9efcba` its tally reads 16 `calls console.to_utf8(), the same as STREAMS`, 13 `none, no answer`, 10 `its own loop, the same as STREAMS`, 5 `its own loop, differs from STREAMS: stdout=replace stderr=backslashreplace` and 3 `its own loop, differs from STREAMS: stdout=replace stderr=replace`, and its last line is `entry points 47`.

#### Command regenerate

```sh
(cd "$S/tree" && python3 -I evals/scripts/rule_cases.py --out "$S/gen" >/dev/null); echo "generator exit $?"
for d in "$S"/gen/*/*; do diff -rq "$d" "$S/tree/evals/behaviour/${d#"$S"/gen/}" >/dev/null || echo "differs: ${d#"$S"/gen/}"; done
ls -d "$S"/gen/*/* | wc -l
```

At `bf9efcba` it prints `generator exit 0`, no `differs:` line, and `17`.

#### Command layout

```sh
mkdir "$S/repo" && git archive bf9efcbab22f421dd5255e6f2b0af77832b6b7e5 | tar -x -C "$S/repo"
git -C "$S/repo" init -q && git -C "$S/repo" add -A && git -C "$S/repo" -c user.name=audit -c user.email=audit@example.invalid commit -qm audit
(cd "$S/repo" && python3 -I skills/verify/scripts/test_layout.py --check > "$S/layout.txt" 2>&1); echo "layout exit $?"
grep -c -i 'twin\|byte-identical' "$S/layout.txt"
```

`test_layout.py` reads the tracked files of a git repository, so the scratch copy is committed in a repository of its own under `"$S"`. At `bf9efcba` it prints `layout exit 0` and `0`.

#### Command coordinates

```sh
python3 -I "$S/audit2.py" coordinates -v
```

At `bf9efcba` it prints the three lines *Instances K13* reads, the 8 `path:line` coordinates that resolve, and last `path:line coordinates 9; path#name coordinates 113; printed for reading 3`.

#### Command lists

```sh
python3 -I "$S/audit2.py" lists
```

At `bf9efcba` it prints 11 hooks, 5 agents, 14 skills, 15 templates, 8 config items and 20 `seal` subcommands, each with the blocks that name most of them, and last `blocks naming three or more and half of a source 33`.

#### Command figures

```sh
python3 -I "$S/audit2.py" figures -v
```

Last line at `bf9efcba`: `figure candidates with no moment on their line 33`.

#### Command history

```sh
git show bf9efcba:hooks/lib/cmdline.py | sed -n 27,28p
git show bf9efcba:hooks/dispatch.py | sed -n 72p
for t in $(git tag --sort=creatordate | grep '^v'); do printf '%s :: %s\n' "${t}" "$(git show "${t}:hooks/dispatch.py" 2>/dev/null | sed -n 72p)"; done | awk '{k=$0; sub(/^[^ ]+ /, "", k); if (k != p) {print; p = k}}'
git tag --sort=creatordate | grep '^v' | awk '/^v0\.3\.0$/{f=1} f' | wc -l
git log --format='%h %as %s' -G'overwide_rows' bf9efcba -- tests/
git log --format='%h %as %s' -S'test_release_hygiene.py#overwide_rows' bf9efcba -- skills/verify/scripts/unverified_check.py
git merge-base --is-ancestor 3911a8cf 66b34a4e; echo "removal before the comment: exit $?"
git tag --contains 66b34a4e | grep -c '^v'
git grep -c 'for _name, _errors in' bf9efcba -- 'skills/*/scripts/*.py' | wc -l
```

Run on 2026-11-01. The first two print the citation of `hooks/dispatch.py:72` for `except Exception: return ""` and that line as `FAILED = []`. The loop prints `except Exception:` at `v0.0.1` and another line at every tag from `v0.3.0`, and the count after it is 62. The first log's newest line is `3911a8cf`, which removed `overwide_rows` from the test module on 2026-09-29 (the module stood under `tests/` before `e391ea04` moved it), and the second prints `66b34a4e`, which wrote the comment the same day; the ancestry line prints `exit 0`, so the comment was written after the removal, and 24 release tags hold it. The last line prints 14, the files under `skills/*/scripts/` that spell the stream loop inline.

#### Command nones

```sh
python3 -I "$S/audit2.py" nones
git grep -h '^check: none' bf9efcba | wc -l
git grep -l '^check: none' bf9efcba -- tests
```

At `bf9efcba` the first prints `check: none lines 49 in 40 sections, naming 26 readers` last, the second `50`, and the third `bf9efcba:tests/text/test_every_agent_reads_the_contract.py`.

#### Command cited

```sh
python3 -I "$S/audit2.py" cited "$(git rev-parse --show-toplevel)"
```

Its last two lines, run on 2026-11-01, are `records read: 3180 at 32 tags` and `check: none lines in rule files 49; cited by no record 4; naming a proofer, a round or the sealer 30, of which cited by no record of that kind 15`.

#### Command durations

```sh
python3 -I - "$S/tree/.test_durations" <<'EOF'
import collections, json, sys
d = json.load(open(sys.argv[1]))
per = collections.defaultdict(float)
for case, s in d.items():
    per[case.split("::")[0]] += s
for m in ("tests/github/test_publish_release_note.py", "tests/skills/test_rule_changes.py",
          "tests/github/test_rules.py", "tests/test_censuses.py"):
    print(f"{per[m]:7.2f} s {m}")
c = "tests/behaviour/test_evals_layout.py::test_the_sealer_cases_are_the_generators_output"
print(f"{d.get(c, 0):7.2f} s {c}")
EOF
```

It prints at `bf9efcba`: 5.80 s, 0.35 s, 2.51 s, 20.32 s and 3.65 s in that order.

#### Command caught

```sh
python3 -I "$S/audit2.py" caught "$(git rev-parse --show-toplevel)"
```

It reads the round records at every release tag from `v0.15.0` to `v0.27.0` and lists each finding once, at the first tag that holds it. Its last line, run on 2026-11-01, is `findings 47; K7 7; K8 18; K10 22; K11 13; K12 9; K13 2`; a finding the placement puts in several kinds counts in each.

#### Command tracker

```sh
for q in to_utf8 console "path#name" coordinate "line number" docstring "check: none" "reader:" "contract rule 13" "release note" "Release body" restat "carried from round" "generators output" "sealer cases" regenerat figure overwide_rows "five scripts" backslashreplace reconfigure "dangling citation" "entry_point census"; do
  gh issue list --state all --search "$q" --limit 15 --json number,state,title --jq '.[] | "#\(.number) \(.state) \(.title)"'
done | sort -u
for n in 1038 1020 1025 1053 1129 1139 1153 1215 1216 1229; do gh issue view "$n" --json number,state,milestone,title,body; done
```

Run on 2026-11-01, and its first loop again by the fix pass over round 2, which read every open issue it returns, and every one `trail/phases/phase-1.md` *Command tracker*'s first loop returns, against the ground of each kind, K1 to K14: by its title, and by its body where the title does not settle it. The open issues this block's first loop returns on a kind's ground are #146, #238, #317, #506, #706, #710, #1020, #1038, #1102, #1128, #1139, #1153, #1197, #1215, #1216 and #1228, and its second loop views #1229. No issue holds the entry points' stream answer, a check of a cited name, or the three drifts K13's row repairs. Each kind's overlaps are named under its *Instances*, in this record or in `trail/phases/phase-1.md`. A tracker search is a search on words, so the list is a sample of the open issues: one on a kind's ground that no query here spells is not listed.

### Instances

#### Instances K7

The 5 passages between work items, by the number *Command K7* prints at `bf9efcba`, each read in its holders:

- K7.1 the header of `templates/records/sdd-questions.md`'s table, in two `frame/questions.md`. Template text.
- K7.2 `1793457435…/guarantee.md:33` and `1793457436…/guarantee.md:109`, "No finding of it reads `fixed`, so no fix pass's claim is left for this run to read". Each states it of its own last round.
- K7.3 the three `routing.md`, line 13: the owner pressed automation for the three 0.27.1 items run beside one another. One answer given once for three work items, true of each.
- K7.4 the three `routing.md`, line 3: the routing table's rows. Template text.
- K7.5 six round records' `## Not judged` header and the broad gate's row. Template text, and each row names its own round's commit.

The 4 passages between a record and `docs/`: K7p.3 and K7p.4 are the `from:` quotes of `1793457437…/frame/design.md:61` and `1793457435…/frame/design.md:62`, which *Command quotes* reads standing; K7p.1 is `1793457436…/frame/design.md:8` and `guarantee.md:59` naming the bullet of `docs/the-record-layout.md:198` by its own words; K7p.2 is `1793457436…/trail/rounds/round-1.md:19` quoting `docs/the-record-layout.md:91` in quotation marks. None has drifted.

The round-record sample's 7 K7 findings, judged by heading; the body of each was not opened. A design's rule change against its section: `v0.24.0` `1793226631…/trail/rounds/round-1.md` 2 ("The rule change for checklist step 5 says the owner's one act at a release is the merge, but the section ke…"). The other 6 are K10's or K11's.

The open part: a record that restates another work item's record in fresh words. Overlaps: #1216 and #1215 (`release: 0.28.0`) read a design's rule changes at the pull request; neither reads a passage between work items.

#### Instances K8

The 36 fragments are each the text `publish_release_note.py#fragments` reads for its tag's range, and each stands in its Release body whitespace-folded, its process rows too. The round-record sample's 18 K8 findings, judged by heading, are a fragment's sentence out of step with the code or with its own work item's records (K10's), such as `v0.24.0` `1793169128…/trail/rounds/round-1.md` 1 and `v0.26.0` `1793432602…/trail/rounds/round-1.md` 1; none is a Release differing from its fragment.

The open part: a Release edited by hand after it was published is read only where the edit removed a fragment's text. Overlaps: #1139 and #1153 (`release: 0.28.0`).

#### Instances K10

The 33 passages, by the number *Command K10* prints at `bf9efcba`, each read in its holders:

- Carried from the round before, and said to be, 17: K10.3 to K10.13 in `1793457435…/trail/rounds/` (the target paragraph, the `## Not judged` rows for Q1, Q2, the deleted release branch and the mutants, and the probe rows), K10.22 to K10.25 in `1793457436…/trail/rounds/`, and K10.32 and K10.33 in `1793457437…/trail/rounds/`. Each later row says `carried from round <N>` or repeats a row whose answerer is unchanged; Q1 of `1793457436…/frame/questions.md` is `open`, as each carried row says.
- A later record quoting the claim it checks, 8: K10.1 and K10.2 (round 5 quoting the changelog and `frame/design.md:25`), K10.17, K10.19 and K10.20 (`guarantee.md` rows quoting `frame/plan.md:50`, `trail/phases/phase-1.md:5` and `docs/the-record-layout.md:91-94`), K10.18 (round 2 quoting `frame/plan.md:43`), and K10.29 and K10.30 (round 2 quoting the changelog of `1793457437`).
- A changelog fragment and its design or plan stating what a person sees, 5: K10.14 and K10.15 (`1793457436…/changelog.md:3`, `frame/design.md:56`, `frame/plan.md:43`) and K10.26 to K10.28 (`1793457437…/changelog.md:3`, `frame/design.md:28` and `:30`). The design names three report lines, the plan the same three, and the fragment states each with its reason; the wording differs and the facts agree.
- K10.21, "This is a search on wordings, so it is a sample (contract rule 12)", in `1793457436…/trail/phases/phase-1.md:31` and `trail/rounds/round-2.md:26`, each of its own search.
- Cited by name, 2: K10.16 (`frame/design.md:8` and `guarantee.md:59` naming a bullet of `docs/the-record-layout.md`) and K10.31 (`1793457437`'s design, plan and phase record naming a paragraph of `templates/setup/config.md` by its bold lead).

The round-record sample's 22 K10 findings, judged by heading. A record stating what another record or the tree no longer says, 7: `v0.22.1` `1792311781…/rounds/round-2.md` 3; `v0.22.3` `1792628098…/rounds/round-2.md` 1 and `round-3.md` 2; `v0.24.0` `1793169128…/trail/rounds/round-1.md` 1 and `1793188384…/trail/rounds/round-5.md` 1; `v0.24.1` `1793240966…/trail/rounds/round-1.md` 1; `v0.25.1` `1793343707…/trail/rounds/round-1.md` 3. The other 15 are a record against the code or a policy finding.

The open part: a record restating another of its work item's records in fresh words. Overlaps: #1020 (`release: 0.29.0`) reads the recurrence of one finding across rounds, which stays out.

#### Instances K11

The 50 passages, by the number *Command K11* prints at `bf9efcba`, each read with the sentence around the shared run in both holders. By pair: `.github/scripts/` and `.github/workflows/` with the three process documents, 11 (K11.1 to K11.11); `skills/verify/scripts/pact_check.py` with `docs/the-pact.md`, 4 (K11.13 to K11.16); `skills/verify/scripts/unverified_check.py` with `docs/the-record-layout.md` and `skills/implement/SKILL.md`, 4 (K11.17, K11.18, K11.33, K11.34); `hooks/question-gate.py` with `docs/the-review-record.md`, 4 (K11.19 to K11.22); `skills/code-review/scripts/chain_check.py` and `skills/verify/scripts/seal_stamp.py` with `docs/the-review-record.md`, 7 (K11.23 to K11.29); the routing hooks with `docs/the-routing-check.md`, 3 (K11.30 to K11.32); the settle scripts with `skills/settle/SKILL.md`, 6 (K11.35 to K11.40); the verify scripts with `skills/verify/SKILL.md` and `skills/verify/orchestration.md`, 10 (K11.41 to K11.50); and `skills/verify/scripts/session_cost.py` with `docs/measuring-a-run.md`, 1 (K11.12). In each the two sentences state one fact. Three were read closer: K11.15 and K11.16, where `docs/the-pact.md` says the tool "carries no normalisation of the header" and `pact_check.py#header_key` normalises one, agree, since the normalisation only names a near header and reads none; K11.33, where the script leaves out "lower case", is an omission; K11.45 says in the past tense what the skill says in the present.

The round-record sample's 13 K11 findings, judged by heading. Out of step between code text and a rule text or the code, 4: `v0.22.1` `1792252400…/rounds/round-1.md` 2 (its heading quoted under `trail/phases/phase-1.md` *Instances K2*, which counts it as well); `v0.22.1` `1792311781…/rounds/round-6.md` 1 ("The double-stamp limit is stated as one amend while every rewrite of the sealing commit draws a second stamp"); `v0.22.3` `1792619289…/rounds/round-2.md` 1 ("The docstring and the settle pointer say every pull request's edited specs are read, while the check reads …"); `v0.24.0` `1793188384…/trail/rounds/round-1.md` 4 ("Three sentences still state the gather or its files, …"). The other 9 are a behaviour a case did not hold.

The open part: a docstring that restates a rule in fresh words, and a printed message built by concatenation of pieces under four words. Overlaps: none of the open issues reads a pair of code text and a rule document. #146, #317, #706 and #710 (`backlog: review chain & agents`), which the tracker returns on the ground this row's *Caught in the record* cell names, each hold a docstring or comment out of step with the code of its own file. That is code text with the tree's own state, P8 with P12, the pair design *The kinds* gives K13, and a command reading code text against a rule document shares no run with it; *Instances K13* reads each, and this row's count and decision stand.

#### Instances K12

The answers *Command entry* prints at `bf9efcba`, read:

- The 3 that differ in a way a person can see: `.github/scripts/release_report.py`, `release_seal.py` and `rules.py` reconfigure `stdout` and `stderr` with `errors="replace"`. `hooks/lib/console.py#STREAMS` gives `stderr` `backslashreplace`, and its docstring's *`errors` is named.* paragraph says why: a path holding a lone surrogate degrades to its escape and not to a `?`. Drifted.
- The 5 that leave `stdin` out: `skills/code-review/scripts/pr_body.py`, `skills/verify/scripts/arm_check.py`, `core_check.py`, `pact_check.py` and `payload_meter.py`. None reads `sys.stdin` (executed: `git show bf9efcba:<file> | grep -c 'sys\.stdin'`, 0 in each), so the answer each gives covers every stream it uses. Not counted as drifted.
- The 13 with no answer: 6 under `.github/scripts/`, the 4 under `evals/scripts/`, `hooks/lib/launch.py` and 2 under `skills/verify/scripts/`. This is the class `seal/follow-up.md`'s row holds, with its own figures at `11f3cde8`; at `bf9efcba`, 5 of the 14 `.github/scripts/` entry points call `console.to_utf8()`, 3 have their own loop and 6 have neither.
- The 10 own loops that match `STREAMS` are `hooks/dispatch.py`, which `tests/censuses.py#entry_point` exempts at its line, and 9 under `skills/*/scripts/`.

The equal function bodies *Command clones* prints: `run` in three `.github/scripts/` files, `_load` in three, `quote` in `broad_gate.py` and `seal_stamp.py`, and `read`/`_read` in `pact_check.py` and `seal_stamp.py`; under `tests/`, `section` in two behaviour modules whose docstrings differ, a module loader in `tests/conftest.py` and two modules, and `test_a_script_copied_alone_exits_2_and_names_what_it_misses` in four modules, the per-module copies #942's layout made. None has drifted, since each group is equal.

The largest passages *Command K12* prints are the entry-point comment "A console that cannot encode what this prints kills it with stdout empty" in 22 files of code text, the imports and fixtures of test modules, and the prompts, scaffolds and graders the eval generators write into each case. The 17 cases `rule_cases.py` writes are its output byte for byte (*Command regenerate*). This phase did not regenerate the proofer cases `replay_targets.py` and `seed_defects.py` write, which needs the reviewed commits fetched through `refs/pull/*/head`. Round 1 of this work item regenerated them at `bf9efcba` in a clone that fetched them, and its record holds the measure: `trail/rounds/round-1.md` finding 6 and its *Probes* row for the two generators. By that measure the seeded cases are their generator's output, and each replay case differs in its scaffold's `git remote add origin` line alone, which the generator reads from the clone's remote. That difference is an input of the run and not a change of the generator, so it is not counted as drifted. `seal/threads/1793457435-replay-targets-reads-both-layouts/guarantee.md` *Claims re-run*, the row *Scenario 5 after 9237e34b*, holds the same result, and #1229 (`release: 0.27.2`) replaces the cases.

The round-record sample's 9 K12 findings, judged by heading. A copy that drifted: `v0.27.0` `1793443708…/trail/rounds/round-1.md` 2 ("The new `link` helper copies `tests/conftest.py#symlink_or_skip` and drops its missing-parent guard"). The other 8 are K10's or K11's, or a behaviour.

The open part: two functions that do one thing in different code, which no command here compares. Overlaps: #1229 (`release: 0.27.2`) asks whether the committed proofer cases are rebuilt from thread-layout records; D6 and D7 touch neither those cases nor their generators. #1038 is D6's home, where the entry points' answer is proposed as a candidate.

#### Instances K13

The three lines *Command coordinates* prints for reading at `bf9efcba`, read:

- `hooks/lib/cmdline.py:28` cites `hooks/dispatch.py:72` (`except Exception: return ""`) as what turns a gate's failure into silence. Line 72 reads `FAILED = []`. The handler is `hooks/dispatch.py#run_gate`'s `except (Exception, SystemExit)`, and its comment says that since #28 the failure is written down and the `stop` group says it once per session, so the sentence's "silence" is stale as well. The line held the handler at `v0.0.1` only (*Command history*). Drifted.
- `skills/verify/scripts/unverified_check.py:113` lists `tests/behaviour/test_release_hygiene.py#overwide_rows` among the readers that keep their own fence rule. `3911a8cf` (#659) removed it before `66b34a4e` (#663) wrote the comment (*Command history*). Drifted.
- `.github/scripts/release_seal.py:112` says the constant "was `skills/verify/scripts/broad_gate.py#PANEL_VALUE_WIDTH` until #832". A sentence about the past, and it holds.

Of the 8 `path:line` coordinates that resolve, 7 stand in `evals/scripts/recurred_truths.json` as the `locations` of a replay case's finding: lines of the commit that case was cut from, not of the tree. One more, `docs/the-reader-registry.md:31` in the same file, lies past the file's end for the same reason. Neither drifts, since the tree is not what they name.

The figure found reading K12: `hooks/lib/console.py:46` "The five scripts under `skills/*/scripts/` spell the loop inline instead of importing this", where 14 do at `bf9efcba` (*Command history*). The commit that made it true was not traced. Drifted.

The open issues *Command tracker* returns on this kind's ground, each read at `bf9efcba` by the fix pass over round 2. A docstring, comment or printed header that says what the code of its own file does is code text with the tree's own state, P8 with P12, which design *The kinds* gives this kind. It shares no run with another file and is no coordinate, list or figure, so no command here lists it. Six stand out of step with that code:

- #146: `.github/scripts/roll_flow_measurement_issue.py:76-78`, the module docstring, says a lag "can only ever produce a reading that is short a result, never one with an extra issue in it". `#landed_create` excludes `closed_number` because a lag behind a close is "a reading with an extra issue in it" (`:450-453`). Drifted.
- #315: `skills/verify/scripts/arm_check.py:1146-1147` prints that "the reason beside each says whether it was ever mutated", and each reason `run_arms` writes is an exception's name and message or "this arm was not measured" (`:977`, `:1000-1003`, `:1010`). `:1129-1130` prints "so it is not refused", where every arm the run ends with no verdict is printed `no verdict` (`:1027`). Drifted.
- #317: `arm_check.py#Verdict`'s docstring (`:736-745`) calls the never-tried case "the whole reason `refused` exists" and an operator in `not_applicable` "un-asked", where `run_arms` puts an operator that was asked and timed out or could not start in `not_applicable` (`:995-1010`) and an arm with either outcome in `refused` (`:1014-1023`). Drifted.
- #706: `skills/verify/scripts/mutation_check.py:570-575`, `main`'s interrupt comment, says "An interrupt during the baseline wrote nothing", where `mutation_run`'s `finally` puts the file back over the baseline as well, because the cases may write it (`:330-347`). Drifted.
- #710: `arm_check.py:953-958` says a put-back that fails propagates "as the loop's own first write would fail on it", where with `--only` selecting no arm the loop writes nothing and the outer `finally`'s `restore` (`:1035-1044`) is what fails. Drifted.
- #1228: `evals/scripts/replay_targets.py:52-53` and `evals/scripts/seed_defects.py:51` say "A name given twice is one name", and each `say_unanswered` walks the names as given (`replay_targets.py:963-964`, `seed_defects.py:394-395`), so an unanswered name given twice is printed twice. Drifted.

Read and not counted. #706's third item: `mutation_check.py:39` and `skills/verify/SKILL.md:174-175` say a file `not restored` may still hold the break; on the baseline path no break was written, which the sentence leaves out, an omission as K11.33 is. #238: `tests/hooks/test_version_check.py:107` names one property the pair of cases holds across a rewording, where #238 measured two; a test is outside this row's corpus, and the measure is #238's, not run again. #1128 (`release: 0.27.1`): `docs/the-record-layout.md:185-186` says a row below a comment opener nobody closed still declares, which #1128 measured `hooks/lib/config.py#config_table` refusing; its work item, merged at `bf9efcba`, changes the sentence at the 0.27.1 settle through `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md` *Rule changes*.

The 33 blocks *Command lists* prints, each read. A block naming every member: `README.md:36` (the five agents), `docs/one-root-by-lifetime.md:182`, `docs/the-agent-set.md:26`, `README.md:172` (the eleven hooks) and `skills/config/SKILL.md:38` (the eight config items). A block naming most and not all, each naming the members its sentence needs: the agent lists leave out the tracer, which runs only where `seal/parity.md` is declared, or name the parties a sentence is about (`skills/core/SKILL.md:47`, the four that judge; `skills/implement/orchestration.md:137`, the parties an automation run spawns); `docs/what-a-script-gates.md:34` lists the hooks that gate and leaves out the four that print; `README.md:259` is the cheat sheet of the commands a person runs; `skills/implement/acts.md:60` names acts, not a source; `templates/setup/config.md:71` is the table first setup writes. None has drifted.

Of the 33 figure candidates *Command figures* prints, 14 were read, each in its line and the two around it: `README.md:586`, `agents/sealer.md:38`, `CONTRIBUTING.md:182`, `docs/the-broad-gate.md:78`, `docs/the-routing-check.md:38`, `docs/the-review-and-parity-arms.md:68`, `evals/README.md:36`, `skills/confidence-check/SKILL.md:22`, `skills/implement/acts.md:62` and `:76`, `templates/setup/config.md:360`, `skills/config/SKILL.md:97`, `skills/implement/bootstrap.md:118` and `skills/writing-style/SKILL.md:334`. Each holds: "three rules" stands in four files for the three rows of `templates/setup/config.md` *The criterion for choosing a value*, and the three rules of *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* are three. This is a sample of a sample.

The round-record sample's 2 K13 findings, judged by heading: `v0.22.0` `1791933022…/rounds/round-5.md` 2 (a frame's statement that its documents follow its rule on figures) and `v0.24.0` `1793163944…/trail/rounds/round-1.md` 2 (titles still stating an old tree).

The open part: a coordinate whose path has no directory, one in `tests/` or `evals/behaviour/`, a figure in code text, a figure the keyword list does not spell, and a docstring, comment or printed line out of step with the code of its own file that no open issue holds. Overlaps: the issues read above; `seal/follow-up.md`'s figure row, which names the owner; #1038's candidate 3, through #1129; and #506 (`backlog: review chain & agents`), an enumeration the tree does not hold in step, whose item 1 proposes a case that compares a module docstring's enumeration with that module's own names. The figure at `hooks/lib/console.py:46` is that shape, a docstring's enumeration out of step, but it counts copies in other files, under `skills/*/scripts/`, which a case reading the docstring's own module does not reach. D7 repairs the instance and builds nothing #506 proposes, and no draft is a comment for #506: the instance is not a catch #506's proposed case would have made, and K13's row leaves the figure class to the follow-up row.

#### Instances K14

*Command cited* prints each of the 49 lines with the records that cite its section at the 32 release tags. The 4 cited by no record: `skills/agent-contract/SKILL.md:178` (contract rule 13, the proofer at review) and `skills/legacy-parity/SKILL.md:65`, `:73` and `:84` (*What the original sends*, *The original's coordinates*, *Replacement annotation*, the parity review). The 15 cited by no record of their reader's kind are those four; `docs/measuring-a-run.md:70`, `docs/the-agent-set.md:119`, `docs/the-broad-gate.md:167` and `:176`, `docs/the-pact.md:133`, `docs/the-record-layout.md:354` and `docs/what-a-script-gates.md:64`, each cited by work items' other records and by no round record; `skills/legacy-parity/SKILL.md:25` and `:56`, the same; and contract rules 4 and 15 (`skills/agent-contract/SKILL.md:69` and `:194`), whose reader is the sealer and which no `guarantee.md` cites, though round records do (2 and 19).

The open part: a reader who applied a rule and named it in other words, or not at all. A contract rule cited as `rule <N>` without the word `contract` is not counted. Overlaps: #1038 reads this table; #1197 (`release: 0.27.1`) removes three `check:` lines that name `tests/behaviour/test_one_word_one_meaning.py`, none of them a `check: none` line; #1215 (`release: 0.28.0`) asks that the pull request read the shape of each `check:` line a design's `to` adds, a `check: none reader:` line among them, and changes none of the lines this row counts.

### Drafts

Each draft cites this record for its measure. No decision here stands against a sentence of `docs/`, a skill or the core at `bf9efcba`. Each of D6's candidates that #1038 keeps changes the policy sentence the draft names for it. D7 changes code text to the rule it already states, and changes no rule.

#### D6

A comment for #1038, not a new issue.

> #1147's audit, at `bf9efcba`, adds two candidates. Each reads a fact exactly, and neither has a catch of its own, which is this issue's question. The measure is `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` at the sealed commit, *The table* rows K12 and K13, *Instances K12* and *Instances K13*.
>
> 1. **The answer every entry point gives to its streams' encoding.** `tests/censuses.py#entry_point` reads `hooks/` alone, and entry points outside it give an answer `hooks/lib/console.py#STREAMS` does not (*Instances K12*). The row on `console.to_utf8()` in `seal/follow-up.md` holds this candidate's question for the owner, and its home becomes this issue's decision. Keeping it rewrites the sentence of `CONTRIBUTING.md` *House rules* "The `encoding` and `entry_point` censuses in `tests/censuses.py` enforce the first over every tracked `.py` and the second over `hooks/`" in place, in the pull request that builds it: `## Rule changes` reads the policy root alone (`skills/settle/scripts/rule_changes.py#parse`), and `CONTRIBUTING.md` is outside it.
> 2. **A `path#name` in shipped text names a name its file defines.** This widens candidate 3's question, whether a dangling citation passes the citation case (#1129), from a cited heading to a cited name. Keeping it adds a `check:` line to `docs/one-root-by-lifetime.md` *The dependency rule*, through the building work item's `## Rule changes`.

Proposed home: #1038 (`release: 0.27.2`), the issue that decides each proposed check before any is built (design G9). A comment adds no work item to a milestone.

Answers: K12, K13.

#### D7

Title: `fix: comments cite code the tree has moved, a docstring counts fewer inline copies than stand, and release scripts degrade stderr otherwise than the console module says every copy must; each is brought to the tree`

Body:

> The measure, at `bf9efcba`, is `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` at the sealed commit, *The table* rows K12 and K13, *Instances K12* and *Instances K13*.
>
> **Scope.** `hooks/lib/cmdline.py`'s docstring cites its handler by name, `hooks/dispatch.py#run_gate`, and says what that handler does at the work item's base. `skills/verify/scripts/unverified_check.py`'s comment names the reader that holds what `overwide_rows` held, or leaves it out of its list. `hooks/lib/console.py`'s docstring names the inline copies without a count, or with the count and its commit. `.github/scripts/release_report.py`, `release_seal.py` and `rules.py` give `stderr` the handler `hooks/lib/console.py#STREAMS` gives, and a case pins it, as contract rule 14 asks of a change to what a person sees.
>
> **Rule change.** None: each change brings code text to the rule it states.
>
> **Done when.** Each citation the scope names resolves at the base and says what the cited code does, the docstring names the inline copies with no count or with the count at the base and its commit, and each script the scope names gives `STREAMS`'s answer for `stderr`.

Proposed milestone: `release: 0.27.3`, the new patch milestone `trail/phases/phase-1.md` *Drafts* weighs: a fix of drifted code text and of what release scripts print. 0.28.0's #1204 edits `.github/scripts/release_seal.py` and #1215 extends the reader of `.github/scripts/rules.py`, so both start from the repaired lines. It edits `skills/verify/scripts/unverified_check.py` after 0.27.1's #1225, and edits no file D1 or D3 names, so it goes beside them.

Answers: K12, K13.

### The comment

*Scope* item 5's text is this preamble, then the header of *The table* and the rows of K1 to K14 in order, copied from `trail/phases/phase-1.md` *The table* and this record's *The table*. The orchestrator replaces each `D<n>` with the number of the issue it filed, or with #1038 for D6, and links each record at the sealed commit (plan row A7).

#### Preamble

> #1147's audit of where a fact is stated more than once, measured at `bf9efcbab22f421dd5255e6f2b0af77832b6b7e5` (`bf9efcba`): one row for each kind of restatement, K1 to K14. Each row is copied whole from the record that measured it, where its commands, the instances it read and its drafts stand: `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` for K1 to K6 and K9, and `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` for K7, K8 and K10 to K14, each at the sealed commit. A name in italics in a cell is a heading of that row's record.

#### Command comment

```sh
D=seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases
python3 -I - "$D/phase-1.md" "$D/phase-2.md" > "$S/comment.md" <<'EOF'
import re, sys
def table(path):
    body = open(path, encoding="utf-8").read().split("\n### The table\n", 1)[1].split("\n### ", 1)[0]
    return [line for line in body.split("\n") if line.startswith("|")]
one, two = table(sys.argv[1]), table(sys.argv[2])
assert one[:2] == two[:2], "the two tables' headers differ"
text = open(sys.argv[2], encoding="utf-8").read()
pre = text.split("\n#### Preamble\n", 1)[1].split("\n#### ", 1)[0]
pre = "\n".join(re.sub(r"^> ?", "", line) for line in pre.strip().split("\n"))
rows = sorted(one[2:] + two[2:], key=lambda line: int(re.match(r"\| K(\d+) ", line).group(1)))
assert [int(re.match(r"\| K(\d+) ", r).group(1)) for r in rows] == list(range(1, 15)), "a kind is missing"
sys.stdout.write(pre + "\n\n" + "\n".join(one[:2] + rows) + "\n")
EOF
echo "join exit $?"; wc -c < "$S/comment.md"; wc -m < "$S/comment.md"
```

It runs from the repository's top at the commit that holds both records, and reads nothing else. Its figures are measured at the last commit that changed either table, and stated in *Phase-boundary run*.

### Phase-boundary run

The phase adds files under this work item's directory and builds no code, so no case is written new and no `seal mutate` run is owed (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the prose row). The plan's named case was seen red by phase 1, before `gaps.md` stood (`trail/phases/phase-1.md` *Phase-boundary run*); this phase does not remove `gaps.md` to see it red again.

With the records written, one command ran the plan's named case, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, and the modules the two searches of `trail/phases/phase-1.md` *Phase-boundary run* list when run over `tests/` at this branch's head, with `tests/behaviour/test_docs_line_wrap.py` added as there: 28 modules (executed: `bin/test <the case> <the modules> -q`, exit 0, 1641 passed). The set is a sample of two searches, as phase 1's was, and `gaps.md` hands the rest to the broad gate.

Every command block of this record, after phase 1's *Command setup*, was run again from a fresh scratch copy after the record was written, and each printed the figure its block states (executed: the blocks extracted from both records and run in order with `sh`, exit 0; *Command tracker* was run while the rows were decided). The fix pass of round 1 ran *Command durations*, *Command tracker*'s first loop and *Command comment* again, after it changed what each states, and the fix pass of round 2 ran the first loop of both *Command tracker* blocks and *Command comment* again (executed). With the two tables as the fix pass of round 2 left them, at the commit its close blocks in `trail/rounds/round-2.md` name, *Command comment* joined them and the preamble with exit 0 into 25,605 bytes and 25,603 characters, under the length design S5 gives (executed: `wc -c` and `wc -m`), and each of its 14 rows stands as a whole line in its record (executed: `grep -qxF` of each joined row over the two records, no miss).
