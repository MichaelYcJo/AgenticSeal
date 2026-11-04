# Phase 2: 1793758948-each-pair-that-can-hold-one-fact-twice-is-measured

## What this phase found

This record holds the rows of the pairs R4, R5, R6 and R12 and of the files F1 to F11, measured at `94635718ea4a79569ac612bcb814114000028be3` (`94635718e`). Every figure below is a figure at `94635718e` unless its sentence names another moment. Each count, command and draft stands once, in its row of *The table* or in the section that row cites; `gaps.md` and every draft cite the row by this path and heading. The pairs R1 to R3, R7 to R11 and R13 to R17 are `trail/phases/phase-1.md`'s, and R18 to R21 and the editions E1 to E4 are the later phases'. Draft ids continue from phase 1's D1 and D2.

### Whether the frame holds

The frame holds, and the build follows it except where this list says. Each item is a finding or a departure, with its grounds.

- **F8's reader is not `tests/conftest.py`.** Design *The files* says of F8 that "`tests/conftest.py` reads the file". At `94635718e` the conftest records every collected node id (`pytest_collection_modifyitems`) and gives `posix_id`, and reads no `.test_durations` (read: `tests/conftest.py:900-940`). Two readers read the file. `pytest-split` 0.11.0, the version `.github/workflows/test.yml:149` installs, divides the shards by it. `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite` judges whether it is stale. The row names what each does with an id that names no case (*Instances F8*).
- **What M3 counts as a template unit.** Design M3 reads "each heading line, table header row and `<!-- -->` marker of a template". The build reads headings in the markdown templates only, outside their fences, since a `#` line of `templates/setup/hygiene.yml` is a YAML comment. A header row is the line above a delimiter row, in any template, fenced or not, since `templates/setup/config.md` shows its table inside a fence. A marker is a comment that opens and closes on one line, so the opening comment of `templates/setup/pact.md` is prose, and R6's M1 reads it. One heading, `## <a clause: what another repository's code depends on>` (`templates/setup/pact.md:43`), is a placeholder whole, which every heading fits, so it is listed as a shape and matched against nothing (`probe2.py#forms`).
- **What M3 reads in P8 and P9.** Design M3 reads "the string constants of P8, the literals of P9". The build reads each string of a Python file line by line: a constant whole, a docstring among them, an f-string with `{}` for each value it formats, and a tuple or list of strings as a header row, since `hooks/lib/config.py` and `skills/verify/scripts/pact_check.py` hold their tables' headers as tuples (`probe2.py#views`). A docstring's section headings are therefore listed as orphans, and each was read.
- **The orphans are sorted for reading, and the sort decides nothing.** `probe2.py#near_ratio` marks an orphan heading as near a template heading by its spelling. That is a reading guessed from words, which design G1 says is reported and never used to decide. Every orphan of P8 was read, and every near orphan of P9 was read. The 293 orphan headings of P9 that are near no template heading were read by a sample of every twentieth, 15 headings (*Instances R5*). `gaps.md` *Not done* names the rest.
- **When a record's title in a fixture counts as stating the form.** A test hands a record to a reader that does not read its title, so a title there states nothing of the form; the 46 near orphans of P9 are of that kind or were planted on purpose (*Instances R5*). An eval case's records are different. The agent under evaluation reads them as a work item's records, and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:29-33` says that a scaffold copies "the record shapes … from this plugin's templates" and that "a record written in the plugin's shape is what the agent meets in production too". So a title or heading that `evals/scripts/rule_cases.py` writes into a fixture record states the form, and R4 counts a difference there as drifted (design G2: the meaning is read, and no grammar rule decides it).
- **M3 lists no orphan in P10.** Design M3 lists as orphaned "a constant or literal", which is P8's and P9's. The cases of P10 that hold record forms are `evals/scripts/rule_cases.py`'s output byte for byte (`trail/phases/phase-1.md` *Command R16*, second block), so R4's orphans read their source, and R6 counts their copies there (*Instances R6*).
- **R12 reads the rows of `seal/follow-up.md` as well.** Design R12 gives M4 and M1. A records-root file stating a script's behaviour in other words shares no 15-word run with the script, so the build also read whole the 7 rows of `seal/follow-up.md` *Schedulable items with nowhere else to go*, the one P6 file whose rows state facts of code, and compared each statement of P8's code with the code. That reading found R12's drift.
- **The handoff's coordinates, opened.** Phase 1's hand-back named four things for this phase. Each was confirmed against the tree. `probe2.py` sets `sys.dont_write_bytecode` before it loads `probe.py`, and its `check` prints `__pycache__ in the copy 0` (executed). M4's marker comparison is R12's, and *Instances R12* holds it. No row of this phase meets the `config.md` entry of `templates/setup/seal-README.md`, so nothing here cites D1: R5's pin `'Commit and pull request language'` stands in that entry, and its assert at `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:46` reads `skills/commit-pr-convention/SKILL.md` (read). F11 reads `seal/follow-up.md:47` and phase 1's R9.1 (*Instances F11*).
- **Outside these pairs: two drifts in phase 1's open parts.** D7's second instance, `CONTRIBUTING.md:126-130`, is a root file stating a test's fact in other words, which is P5 with P9, R9's pair; it stands in the sentence after R9.1's passage, which phase 1 read as one fact, and that reading holds for the passage. D9, a test comment stating that `hooks/lib/config.py` reads a row no script reads, is P9 with P8, R15's pair, and the class R15's open part names. M4's item list found it. Phase 1's rows count passages and pins, and neither instance is one, so this record does not rewrite them; each is drafted here, since design *Scope* item 5 drafts every drift no open issue holds.
- **Every pair and file is measured, and none is closed** (plan row A2). Each row's commands ran in this phase's environment.

### The table

| Label | Command | Held twice | Drifted | Open part | Home |
|---|---|---|---|---|---|
| R4 | *Command setup*; *Command R4* | 32 of the 79 template units M3 matches held in a string of P8, and 45 distinct orphans (42 headings, 3 markers) listed, at `94635718e` | 6 at `94635718e`: four record forms whose title or heading `evals/scripts/rule_cases.py` writes into its fixture records in a shape no template gives (*Instances R4*) | a heading or header a script builds from parts or reads without its hashes; a template's form stated in prose; a shell, YAML or JSON file of P8, whose strings M3 does not read | D3 |
| R5 | *Command setup*; *Command R5* | 56 of the 79 units held in a string of P9, 446 distinct orphans (395 headings, 51 markers) listed, and 37 pins in 13 test modules whose literal stands in a template, at `94635718e` | 0 at `94635718e` (*Instances R5*) | a test stating a template's form in other words; the orphan headings outside the sample *Instances R5* reads; a pin whose literal reaches the assert through a name | none |
| R6 | *Command setup*; *Command R6* | 0 passages over 3,720 file pairs, and 24 of the 79 units held in a file of P10, at `94635718e` | 0 counted here at `94635718e`: the generated cases hold R4's drifted forms as `rule_cases.py` writes them, and R4 counts them at that source (*Instances R6*) | an orphan in P10, which M3 does not list; a case stating a template's form in other words | D3 |
| R12 | *Command setup*; *Command R12* | 1 passage over 234 file pairs; the opt-in marker in `hooks/lib/optin.py` and on the first line of both README files; 9 item names a string of P8 holds; and 1 statement of P8's code among the rows of `seal/follow-up.md`, at `94635718e` | 1 at `94635718e`: the `--worktree` row of `seal/follow-up.md` cites a warning that `read_record`'s docstring no longer gives (*Instances R12*) | a records-root file stating a script's behaviour in other words outside `seal/follow-up.md`'s rows; an item name a script builds from parts | D4 |
| F1 | *Command files*; *Command F* | 3 facts at `94635718e`: the plugin's name, its description and its owner, each held with `.claude-plugin/plugin.json`, and the name and description with the README editions | 1 at `94635718e`: `docs/releasing/branch-and-release.md:204-206` says `plugin.json` holds the one copy of the plugin's name and nothing else in the tree spells it, and this file spells it twice (*Instances F1*) | a document stating the name's holders in other words | D8 |
| F2 | *Command files*; *Command F* | 4 facts at `94635718e`: the name, the description, the version and the icon, each held with the file *Instances F2* names | 0 at `94635718e`; F1's instance is the sentence that names this file as the name's one copy | the license, which is F9's row | none |
| F3 | *Command files*; *Command F* | 1 fact at `94635718e`: the committed text is LF, held by `evals/scripts/behaviour.py:153` | 0 at `94635718e` | a document stating line endings without naming the file | none |
| F4 | *Command files*; *Command F* | 0 at `94635718e`: its one fact, that a blank issue may be opened, no other file states (*Instances F4*) | 0 at `94635718e` | none | none |
| F5 | *Command files*; *Command F*; *Command tracker* | 2 facts at `94635718e`: the two gates the form names, and the label it applies | 1 at `94635718e`: the form applies the label `gate`, and the tracker holds no label of that name (*Instances F5*) | a document stating what a misfire report holds, which no file at `94635718e` states | D5 |
| F6 | *Command files*; *Command F* | 8 facts at `94635718e`, each held with `CONTRIBUTING.md`, `.github/workflows/test.yml` or `.github/workflows/hygiene.yml` (*Instances F6*) | 1 at `94635718e`: the comment on a gate change lists four of the seven items `CONTRIBUTING.md` *What a change to a gate must carry* asks a pull request for, and leaves out the one that section says only the pull request body answers (*Instances F6*) | none | D6 |
| F7 | *Command files* | 0 at `94635718e`: no document names an entry of the file (*Instances F7*) | 0 at `94635718e` | a document naming an ignored path without naming the file | none |
| F8 | *Command files*; *Command F* | 6,323 ids against 3,552 test functions in 149 modules, read from their AST: 25 ids name no function, 0.47% of the file's seconds, and 44 functions no id names; and 2 facts `CONTRIBUTING.md` states of the file, at `94635718e` | 0 at `94635718e`: the stale ids are what `CONTRIBUTING.md:166` says the file becomes between refreshes, under the thresholds the case holds (*Instances F8*) | a case a hook or `pytest_generate_tests` builds, and each parameter id, which the AST does not give | none |
| F9 | *Command files*; *Command F* | 1 fact at `94635718e`: MIT is the code's license, held by `.claude-plugin/plugin.json`, `TRADEMARKS.md` and both README editions | 0 at `94635718e` | none | none |
| F10 | *Command files*; *Command F* | 6 facts at `94635718e`, each held with the file *Instances F10* names | 0 at `94635718e` | the entries' figures of bytes and pixels, which no command here redrew | none |
| F11 | *Command files*; *Command F* | 5 facts at `94635718e`, each held with the file *Instances F11* names | 1 at `94635718e`: `ruff.toml:40-42` says `tests/hooks/test_launch.py` refuses the syntax and constructs the floor lacks, which `tests/censuses.py#floor_syntax` does (*Instances F11*) | a comment stating the lint in other words | D7 |

### Commands

Each block runs at `94635718e` against a scratch copy of that commit and reads nothing else, except *Command history* and *Command tracker*, which read the clone's history and the tracker, and the third line of *Command files*, which fetches `pytest-split` 0.11.0. Run `trail/phases/phase-1.md` *Command setup* first, from a clone of this repository, then *Command setup* below, then the other blocks in the same shell.

#### Command setup

```sh
cat > "$S/probe2.py" <<'EOF'
"""#1236 phase 2: the readers of the pairs R4, R5, R6 and R12 and of F8,
run over the scratch copy "$S/tree" of 94635718e. Phase 1's `$S/probe.py`
(its *Command setup*) is loaded by path and gives `PARTS`, `ALL`, `PAIRS`,
`pair`, `passages`, `context`, `pins`, `config_items`, `read`, `text_of`
and `PS`. The one change to it is two entries added to `PAIRS`, R6 and
R12, so that its `pair` reads them.

New: forms (design M3's template units), views (the strings of a Python
file: each constant whole, each f-string with `{}` for each value it
formats, and each tuple or list of strings as a table header row), m3 (M3
over one part, with the orphans and NEAR, a reading aid that sorts them),
items and marker (design M4 for R12), durations (F8) and check.
"""

import ast
import collections
import importlib.util
import os
import re
import sys

sys.dont_write_bytecode = True  # a module loaded from the copy writes no __pycache__ into it
_spec = importlib.util.spec_from_file_location("probe", os.path.join(os.environ["S"], "probe.py"))
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)
P.PAIRS.update({"R6": ("P4", "P10"), "R12": ("P6", "P8")})

HEADING = re.compile(r"^#{1,6} \S")
MARK = re.compile(r"<!--.*?-->")
PLACEHOLDER = re.compile(r"<[^<>]+>")


def fold(s):
    return " ".join(s.split())


def rx_of(line):
    """A template line as a regex: each `<placeholder>` matches any text, the
    rest is literal, whitespace folded."""
    out, last = [], 0
    for m in PLACEHOLDER.finditer(line):
        out += [re.escape(line[last:m.start()]), ".+?"]
        last = m.end()
    out.append(re.escape(line[last:]))
    return "".join(out)


def forms():
    """Design M3's units: each heading line of a markdown template, each table
    header row (the line above a delimiter row) of any template, and each
    one-line `<!-- -->` marker. `[(kind, "path:line", text, regex)]`."""
    out = []
    for p in P.PARTS["P4"]:
        lines = P.read(p).split("\n")
        fence = False
        for k, line in enumerate(lines, 1):
            if p.endswith(".md") and P.PS.FENCE.match(line):
                fence = not fence
                continue
            f = fold(line)
            if p.endswith(".md") and not fence and HEADING.match(f):
                # a title that is one placeholder is a shape every heading fits, and is not matched
                kind = "shape" if PLACEHOLDER.fullmatch(f.split(" ", 1)[1]) else "heading"
                out.append((kind, f"{p}:{k}", f, rx_of(f)))
            if f.startswith("|") and k < len(lines) and re.match(r"^\|(\s*:?-+:?\s*\|)+$", fold(lines[k]).replace(" ", "")):
                out.append(("header", f"{p}:{k}", f, rx_of(f)))
            for m in MARK.finditer(line):
                out.append(("marker", f"{p}:{k}", m.group(0), re.escape(m.group(0))))
    return out


def render(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) else "{}" for v in node.values)
    return None


def views(p):
    """`[(line, text)]`: each line of each string of the Python file P, whole
    constants and f-strings rendered, and each tuple or list of two or more
    strings, or of one string where its name ends in HEADER or TABLE, as a
    header row `| a | b |`."""
    t = P.text_of(p)
    if t is None or not (p.endswith(".py") or t.startswith("#!/usr/bin/env python")):
        return []
    try:
        tree = ast.parse(t)
    except SyntaxError:
        return []
    inner, out = set(), []
    for n in ast.walk(tree):
        if isinstance(n, ast.JoinedStr):
            inner |= {id(v) for v in n.values}
    named = {id(n.value) for n in ast.walk(tree) if isinstance(n, ast.Assign)
             and any(isinstance(t_, ast.Name) and t_.id.endswith(("HEADER", "TABLE")) for t_ in n.targets)}
    for n in ast.walk(tree):
        if id(n) in inner:
            continue
        s = render(n)
        if s is not None:
            for k, line in enumerate(s.split("\n")):
                if line.strip():
                    out.append((n.lineno + k, fold(line)))
        if isinstance(n, (ast.Tuple, ast.List)) and n.elts and all(
                isinstance(e, ast.Constant) and isinstance(e.value, str) for e in n.elts) \
                and (len(n.elts) >= 2 or id(n) in named):
            out.append((n.lineno, "| " + " | ".join(fold(e.value) for e in n.elts) + " |"))
    return out


def lines_of(p):
    t = P.text_of(p)
    return [] if t is None else [(k, fold(x)) for k, x in enumerate(t.split("\n"), 1) if x.strip()]


def side(part):
    """The other part's text as M3 reads it: P8's and P9's strings, P10's
    lines."""
    get = lines_of if part == "P10" else views
    return {p: v for p in P.PARTS[part] if (v := get(p))}


def holds(unit, text):
    kind, _, f, rx = unit
    if kind == "heading":
        return bool(re.search(r"(?<![#\w])" + rx + r"(?!\s*\w)", text))
    if kind == "header":
        return re.search(r"\s*".join(map(re.escape, f.replace("|", " | ").split())), text) is not None \
            if not PLACEHOLDER.search(f) else re.search(rx, text) is not None
    return re.search(rx, text) is not None


def m3(part):
    """M3 over PART: each template unit with the files of PART that hold it;
    then each string of P8 or P9 shaped as a records heading or holding a
    marker that no template unit matches, the orphans."""
    units, other = forms(), side(part)
    held_units = 0
    for u in units:
        if u[0] == "shape":
            print(f"shape {u[1]} {u[2][:80]!r} -> not matched")
            continue
        where = [f"{p}:{k}" for p, v in other.items() for k, t in v if holds(u, t)]
        held_units += bool(where)
        print(f"{u[0]} {u[1]} {u[2][:80]!r} -> {len(where)}{': ' + ', '.join(where[:4]) if where else ''}")
    print(f"units {len(units)} (shapes {sum(u[0] == 'shape' for u in units)}, headings {sum(u[0] == 'heading' for u in units)}, headers "
          f"{sum(u[0] == 'header' for u in units)}, markers {sum(u[0] == 'marker' for u in units)}); "
          f"held in {part} {held_units}")
    if part == "P10":
        return
    heads = [u for u in units if u[0] == "heading"]
    marks = {u[2] for u in units if u[0] == "marker"}
    doc_heads = set()
    for p in P.ALL:
        if p.endswith(".md") and not p.startswith("templates/"):
            doc_heads |= {fold(x) for x in P.read(p).split("\n") if HEADING.match(fold(x))}
    orphans = collections.defaultdict(list)
    for p, v in other.items():
        for k, t in v:
            if HEADING.match(t) and not any(re.fullmatch(u[3], t) or re.fullmatch(u[3], t.replace("{}", "x"))
                                            for u in heads):
                orphans[("heading", t)].append(f"{p}:{k}")
            for m in MARK.finditer(t):
                if m.group(0) not in marks:
                    orphans[("marker", m.group(0))].append(f"{p}:{k}")
    tags = collections.Counter()
    for (kind, t), where in sorted(orphans.items()):
        tag = "-"
        if kind == "heading":
            near = max(heads, key=lambda u: near_ratio(u[2], t))
            if near_ratio(near[2], t) >= NEAR:
                tag = f"near {near[1]}"
            elif t in doc_heads:
                tag = "doc"
        tags[tag.split()[0]] += 1
        if "-v" in sys.argv or tag.startswith("near") or (part == "P8" and tag == "-"):
            print(f"ORPHAN {kind} {tag} {t[:90]!r} :: {len(where)}: {', '.join(where[:3])}")
    print(f"orphans in {part} {len(orphans)} distinct ({sum(k == 'heading' for k, _ in orphans)} headings, "
          f"{sum(k == 'marker' for k, _ in orphans)} markers); headings near a template heading "
          f"{tags['near']}; others standing as a heading of a file outside templates/ {tags['doc']}")


NEAR = 0.8


def near_ratio(form, line):
    """How close a heading LINE is to a template heading FORM, its
    placeholders taken out of both, the hashes taken off and both
    lowercased: 1.0 where one of two words or more opens or ends the other,
    else difflib's ratio."""
    import difflib
    a = PLACEHOLDER.sub("", form).lstrip("#").strip().lower()
    b = line.replace("{}", "").lstrip("#").strip().lower()
    if not (a and b):
        return 0.0
    if len(min(a, b, key=len).split()) >= 2 and (a.startswith(b) or b.startswith(a) or a.endswith(b) or b.endswith(a)):
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


READERS = {"config_value": 1, "value_of": 1, "declared_value": 1, "rows_named_below": 2, "doubled_row": 0}


def items():
    """M4 for R12: each item name P8 holds, as a whole string constant equal to
    an item or row name, or as the item argument of a reader of
    `hooks/lib/config.py` (READERS) resolved through module-level names,
    against the rows of `seal/config.md` and the items of
    `templates/setup/config.md`. A bare name resolves in its own module
    first, then in any module of P8."""
    rows, tmpl = set(), set()
    cap = io_capture()
    with cap:
        P.config_items()
    for line in cap.lines[:2]:
        names = set(line.split(": ", 1)[1].split(" / "))
        (rows if line.startswith("seal/config.md") else tmpl).update(names)
    names = rows | tmpl
    consts, local = collections.defaultdict(set), collections.defaultdict(dict)
    trees = {}
    for p in P.PARTS["P8"]:
        t = P.text_of(p)
        if t is None or not (p.endswith(".py") or t.startswith("#!/usr/bin/env python")):
            continue
        trees[p] = ast.parse(t)
        for n in trees[p].body:
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str):
                for tg in n.targets:
                    if isinstance(tg, ast.Name):
                        consts[tg.id].add(n.value.value)
                        local[p][tg.id] = n.value.value
    found = collections.defaultdict(set)
    for p, tree in trees.items():
        for n in ast.walk(tree):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value.strip() in names:
                found[n.value.strip()].add(f"{p}:{n.lineno}")
            if isinstance(n, ast.Call):
                f = n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, "id", None)
                if f in READERS and len(n.args) > READERS[f]:
                    a = n.args[READERS[f]]
                    name = a.attr if isinstance(a, ast.Attribute) else getattr(a, "id", "")
                    vals = ({a.value} if isinstance(a, ast.Constant) and isinstance(a.value, str)
                            else {local[p][name]} if isinstance(a, ast.Name) and name in local[p]
                            else consts.get(name, {f"<unresolved {ast.unparse(a)}>"}))
                    for v in vals:
                        found[v].add(f"{p}:{n.lineno} {f}()")
    for v in sorted(found):
        where = [w for w, src in (("seal/config.md", rows), ("the template", tmpl)) if v in src]
        print(f"{v!r} -> {', '.join(where) or 'NEITHER'} :: {len(found[v])}: {', '.join(sorted(found[v])[:6])}")
    print(f"item names P8 holds {len(found)}; in the template {sum(v in tmpl for v in found)}; "
          f"in seal/config.md {sum(v in rows for v in found)}; template items P8 holds none of: "
          f"{' / '.join(sorted(tmpl - set(found))) or 'none'}")


class io_capture:
    def __enter__(self):
        import io
        self._old, self._buf = sys.stdout, io.StringIO()
        sys.stdout = self._buf
        return self

    def __exit__(self, *exc):
        sys.stdout = self._old
        self.lines = self._buf.getvalue().split("\n")


def marker():
    """M4's marker comparison: `hooks/lib/optin.py#MARKER` against the first
    line of `seal/README.md` and of `templates/setup/seal-README.md`, exact,
    and each other P8 string that holds the marker's text."""
    tree = ast.parse(P.read("hooks/lib/optin.py"))
    m = next(n.value.value for n in tree.body if isinstance(n, ast.Assign)
             and any(getattr(t, "id", "") == "MARKER" for t in n.targets))
    print(f"MARKER {m!r}")
    for p in ("seal/README.md", "templates/setup/seal-README.md"):
        first = P.read(p).split("\n", 1)[0]
        print(f"{p} first line {first!r}: {'equal' if first == m else 'DIFFERS'}")
    body = m.lstrip("# ")
    for p in P.PARTS["P8"]:
        for k, t in views(p):
            if body in t and p != "hooks/lib/optin.py":
                print(f"also {p}:{k} {t[:90]!r}")


def durations():
    """F8: each id of `.test_durations` against the test functions its module
    defines, read from the module's AST: the file, then each `Class::name`
    or `name` with its `[parameters]` taken off, a module-level name bound
    by assignment counted as a function. A case a pytest hook or a
    `pytest_generate_tests` builds is not in the AST, and the parameter ids
    are not read. Also each test function no id names."""
    import json
    held = json.loads(P.read(".test_durations"))
    defined = {}
    for p in P.PARTS["P9"]:
        if not (p.endswith(".py") and os.path.basename(p).startswith("test_")):
            continue
        tree = ast.parse(P.read(p))
        names = set()
        for n in tree.body:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name.startswith("test"):
                names.add(n.name)
            if isinstance(n, ast.Assign):  # `test_census = census_case(TARGET)`
                names |= {tg.id for tg in n.targets if isinstance(tg, ast.Name) and tg.id.startswith("test")}
            if isinstance(n, ast.ClassDef) and n.name.startswith("Test"):
                names |= {f"{n.name}::{m.name}" for m in n.body
                          if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)) and m.name.startswith("test")}
        defined[p] = names
    no_file, no_case, seconds, gone = [], [], sum(held.values()), 0.0
    named = collections.defaultdict(set)
    for node, s in held.items():
        path, _, rest = node.partition("::")
        base = re.sub(r"\[.*\]$", "", rest)
        if path not in defined:
            no_file.append(node)
            gone += s
        elif base not in defined[path]:
            no_case.append(node)
            gone += s
        else:
            named[path].add(base)
    unnamed = [f"{p}::{n}" for p, ns in sorted(defined.items()) for n in sorted(ns - named[p])]
    for node in no_file + no_case:
        print(f"NO CASE {node} {held[node]:.3f}s")
    for u in unnamed:
        print(f"UNPRICED {u}")
    print(f"ids {len(held)}; naming no test module {len(no_file)}; naming no function of their module "
          f"{len(no_case)}; their seconds {gone:.1f} of {seconds:.1f} ({gone / seconds:.2%}); "
          f"test functions {sum(map(len, defined.values()))} in {len(defined)} modules, no id naming {len(unnamed)}")


def check():
    """The units M3 reads, by kind, and that no `__pycache__` stands in the
    copy."""
    kinds = collections.Counter(u[0] for u in forms())
    print(f"template units {sum(kinds.values())}: " + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items())))
    print(f"__pycache__ in the copy {sum(1 for d, _, _ in os.walk(P.T) if d.endswith('__pycache__'))}")


if __name__ == "__main__":
    cmd, args = sys.argv[1], [a for a in sys.argv[2:] if a != "-v"]
    {"forms": lambda: [print(u[:3]) for u in forms()], "m3": lambda: m3(args[0]),
     "items": items, "marker": marker, "passages": lambda: P.passages(args[0]),
     "context": lambda: P.context(args[0]), "pins": lambda: P.pins(args[0], "-v" in sys.argv),
     "durations": durations, "check": check}[cmd]()
EOF
python3 -I "$S/probe2.py" check
```

At `94635718e` it prints `template units 80: header 26, heading 51, marker 2, shape 1` and `__pycache__ in the copy 0`. Of the 80, the shape is matched against nothing, so 79 units are matched. Remove `"$S"` after the last block.

#### Command R4

```sh
python3 -I "$S/probe2.py" m3 P8
```

Last two lines at `94635718e`: `units 80 (shapes 1, headings 51, headers 26, markers 2); held in P8 32` and `orphans in P8 45 distinct (42 headings, 3 markers); headings near a template heading 5; others standing as a heading of a file outside templates/ 0`. Above them it prints each unit with the strings that hold it, and each of the 45 orphans *Instances R4* reads.

#### Command R5

```sh
python3 -I "$S/probe2.py" m3 P9
python3 -I "$S/probe2.py" m3 P9 -v | grep '^ORPHAN heading - ' | wc -l
python3 -I "$S/probe2.py" m3 P9 -v | grep '^ORPHAN heading - ' | awk 'NR % 20 == 1'
python3 -I "$S/probe2.py" pins P4 -v
```

At `94635718e` the first prints `units 80 (shapes 1, headings 51, headers 26, markers 2); held in P9 56` and, last, `orphans in P9 446 distinct (395 headings, 51 markers); headings near a template heading 46; others standing as a heading of a file outside templates/ 56`, after the 46 near orphans *Instances R5* reads. The second prints `293`, the orphan headings neither near nor a heading of another file. The third prints the 15 of them *Instances R5* reads. The fourth prints the 37 pins and, last, `pins 37 in 13 modules, corpus P4`.

#### Command R6

```sh
python3 -I "$S/probe2.py" passages R6
python3 -I "$S/probe2.py" m3 P10 | tail -1
(cd "$S/tree" && for p in '^# Feature Specification' '— review round 1' '^# routing$' '^## User scenarios & acceptance$'; do printf '%s: ' "$p"; grep -rlE -- "$p" evals/behaviour | wc -l; done)
```

At `94635718e` it prints `R6: 0 passages over 3720 file pairs`, `units 80 (shapes 1, headings 51, headers 26, markers 2); held in P10 24`, and the number of case files under `evals/behaviour/` holding each of R4's drifted forms: 10, 5, 17 and 11.

#### Command R12

```sh
python3 -I "$S/probe2.py" passages R12
python3 -I "$S/probe2.py" marker
python3 -I "$S/probe2.py" items
sed -n 42p "$S/tree/seal/follow-up.md"
sed -n '/^def read_record/,/^    if WORKTREE/p' "$S/tree/skills/code-review/scripts/chain_check.py"
```

At `94635718e` the first prints `R12: 1 passages over 234 file pairs` last. The second prints the marker and `equal` for both files, and no `also` line. The third prints a line for each name and, last, `item names P8 holds 9; in the template 8; in seal/config.md 5; template items P8 holds none of: Commit and pull request language / Record language`; its first line, `'<unresolved item>' -> NEITHER`, is the reader's own parameter inside `hooks/lib/config.py` and `fold_check.py`'s loop over its `ROWS`, and names no item. The last two print the row *Instances R12* reads and `read_record`'s docstring.

#### Command files

```sh
(cd "$S/tree" && cat -n .claude-plugin/marketplace.json .claude-plugin/plugin.json .gitattributes .github/ISSUE_TEMPLATE/config.yml .github/ISSUE_TEMPLATE/gate-misfired.md .github/PULL_REQUEST_TEMPLATE.md .gitignore LICENSE assets/seals/README.md ruff.toml | wc -l)
python3 -I "$S/probe2.py" durations | tail -1
uv run --no-project --with 'pytest-split==0.11.0' python -I -c "import inspect, pytest_split.algorithms as a; print(inspect.getsource(a._get_items_with_durations)); print(inspect.getsource(a._remove_irrelevant_durations))"
```

The first prints `517`, the lines of the ten files design M7 reads whole; F8, `.test_durations`, is read by the second. At `94635718e` the second prints `ids 6323; naming no test module 0; naming no function of their module 25; their seconds 7.6 of 1614.4 (0.47%); test functions 3552 in 149 modules, no id naming 44`, after the 25 ids and 44 functions it names. The third prints the two functions of `pytest-split` 0.11.0 *Instances F8* reads; it fetches the package into `uv`'s own cache, and runs from any directory.

#### Command F

```sh
(cd "$S/tree"
grep -rn -F '.gitattributes' evals/scripts
grep -n -e 'blank_issues' -e 'contact_links' .github/ISSUE_TEMPLATE/config.yml
grep -n -F 'labels:' .github/ISSUE_TEMPLATE/gate-misfired.md; ls hooks/routing-edit-gate.py hooks/question-gate.py
sed -n '/^## What a change to a gate must carry/,/^## House rules/p' CONTRIBUTING.md | grep -c '^- \*\*'
grep -n -F 'nothing else in the tree' docs/releasing/branch-and-release.md; grep -n -F '"agentic"' .claude-plugin/marketplace.json; grep -c -F 'agentic@agenticseal' README.md README.ko.md
grep -n -w 'MIT' LICENSE .claude-plugin/plugin.json TRADEMARKS.md README.md README.ko.md
grep -n 'FLOOR =' hooks/lib/launch.py; grep -n -F 'test_launch' ruff.toml CONTRIBUTING.md; grep -n -e 'floor_syntax` census' -e 'derives the set' tests/censuses.py tests/hooks/test_launch.py
grep -n '^select' ruff.toml
grep -n -F 'which `hooks/lib/config.py` reads' tests/behaviour/test_the_pull_request_language_is_the_repositorys.py
grep -n -F 'One source' .github/workflows/hygiene.yml)
```

Each line is a search for the other holder of a fact the rows read, and each is a search on words, so the list it makes is a sample. At `94635718e` it prints the coordinates *Instances F1* to *Instances F11* and *Instances R4* cite: among them `evals/scripts/behaviour.py:153`, `blank_issues_enabled: true` alone, `labels: gate`, `7` bold items in the gate section, `docs/releasing/branch-and-release.md:204`, `.claude-plugin/marketplace.json:9` and `:15`, `2` install lines in each README edition, `FLOOR = (3, 12)`, `ruff.toml:40` and `CONTRIBUTING.md:126`, `tests/hooks/test_launch.py:210` and `tests/censuses.py:761`, the `select` line, the comment at `:44` and the two `One source` lines at `.github/workflows/hygiene.yml:111` and `:161`.

#### Command history

```sh
git show d218cdd27 -- templates/records/sdd-design.md | grep -E '^[-+]# '
git log --format='%h %ad' --date=short -S'Feature Specification' 94635718e -- evals/scripts/rule_cases.py
git log --format='%h %ad' --date=short -S'the more permissive of' 94635718e -- skills/code-review/scripts/chain_check.py
git log --format='%h %ad' --date=short -S'Should `chain_check.py --worktree`' 94635718e -- seal/follow-up.md
git log --format='%h %ad' --date=short -S'floor_syntax' 94635718e -- tests
git log --format='%h %ad' --date=short -S'refuses in each the syntax' 94635718e -- ruff.toml
git log --format='%h %ad' --date=short -S'**What it removes.**' 94635718e -- CONTRIBUTING.md
git log --format='%h %ad' --date=short -S'**What it reads.**' 94635718e -- CONTRIBUTING.md
git log --format='%h %ad' --date=short 94635718e -- .github/PULL_REQUEST_TEMPLATE.md
git log --format='%h %ad' --date=short -S'labels: gate' 94635718e -- .github/ISSUE_TEMPLATE/gate-misfired.md
git log --format='%h %ad' --date=short -S'nothing else in the tree' 94635718e -- docs
git log --format='%h %ad' --date=short -S'which `hooks/lib/config.py` reads and a session looks' 94635718e -- tests
```

Run from the clone. At `94635718e` it prints, block by block: the template's title line going from `# Feature Specification: <work item>` to `# Design: <work item>`; `8350c5788 2026-10-16`; `8350c5788 2026-10-16` and `716d8548d 2026-08-31`; `0155f0f52 2026-09-08`; `cbf97bf55 2026-10-24`; `ce448bbef 2026-10-15`; `5b1f6faea 2026-10-15`; `96c11614f 2026-10-31`; `ab14194b1 2026-10-28`, `5b1f6faea 2026-10-15` and `5f8fea996 2026-09-21`; `716d8548d 2026-08-31`; `b451e503d 2026-10-20`, `9b644676f 2026-10-08` and `a0208dcd8 2026-09-22`; `c3e020961 2026-11-02`.

#### Command tracker

```sh
for q in "Feature Specification" "rule_cases" "fixture" "scaffold" "review round title" "routing.md title" "follow-up.md" "read_record" "worktree local mode" "PULL_REQUEST_TEMPLATE" "pull request template" "issue template" "gate-misfired" "What a change to a gate must carry" "label gate" "ruff.toml" "floor_syntax" "test_launch" "plugin name" "nothing else in the tree spells" "Commit and pull request language" "test_durations" "LICENSE" "seal art" "gitattributes" "gitignore"; do
  gh issue list --state open --search "$q" --limit 30 --json number,title,milestone --jq '.[] | "#\(.number)\t\(.milestone.title // "-")\t\(.title)"'
done | sort -u
gh api 'repos/:owner/:repo/labels/gate' --silent >/dev/null 2>&1; echo "label gate exit $?"
gh api 'repos/:owner/:repo/labels/hooks-gates' --silent >/dev/null 2>&1; echo "label hooks-gates exit $?"
gh label list --search gate --json name --jq '.[].name'
gh issue view 1319 --json body,comments --jq '.body, (.comments[] | .body)'
gh api 'repos/:owner/:repo/milestones?state=open&per_page=100' --jq '.[] | "\(.number)\t\(.title)\t\(.description)"'
```

Run on 2026-11-04, from the clone. The loop prints 22 open issues, each read by title, and #1319 by its body and comments. None holds a drift this record counts. #1319 holds the fixed forms agents exchange and the record files that state one fact twice; its census names no eval fixture's titles, no contributor form under `.github/` and none of the sentences D4 to D9 name. #1107, #1178 and #1266 hold paid runs of the eval cases, which D3's regeneration changes (D3 names them). The label checks print `label gate exit 1`, `label hooks-gates exit 0`, and `hooks-gates` and `review-chain` for the search. A tracker search is a search on words, so the list is a sample.

### Instances

#### Instances R4

The 45 orphans *Command R4* prints, each read at its coordinate in `"$S/tree"`.

Six are drifted. Each is a record form `evals/scripts/rule_cases.py` writes into the fixture records of the eval cases, in a shape no template gives:

- `# Feature Specification: shout ends with one exclamation mark` (`:263`, the proofer case's `frame/design.md`), `# Feature Specification: {}` (`:357`, each crafter build's) and `# Feature Specification: shout keeps empty text empty` (`:764`, `SEALER_SPEC`). `templates/records/sdd-design.md:1` gives `# Design: <work item>`. The template said `# Feature Specification: <work item>` until d218cdd27 (#1151) renamed it, and the fixture lines date from 8350c5788, before the rename (*Command history*). The rename case of the same module, written later, writes `# Design: shout is renamed exclaim` (`:458`), which R4 lists as held.
- `## User scenarios & acceptance` (`:270`, `:363`, `:466` and `:771`). `templates/records/sdd-design.md:13` gives `## User scenarios & acceptance *(mandatory)*`. `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:29-36` exempts this exact line from its refused words and says it is the template's heading "without the ` *(mandatory)*` the template carries", and gives no reason for the difference.
- `# {item} — review round 1` (`:795`, `SEALER_ROUND`, each sealer case's `trail/rounds/round-1.md`). `templates/records/sdd-round.md:1` gives `# Review round <N>: <work-item-id>`.
- `# routing` (`:159`, `routing`, every case's `routing.md`). `templates/records/sdd-routing.md:1` gives `# Routing: <work-item-id>`.

No reader of the plugin reads a record's title, so the cases run the same either way. What differs is what the agent under evaluation meets: a design titled with the name 0.23.0 retired, and records titled otherwise than any session writes them (*Whether the frame holds*, the item on a fixture's title).

The other 39 are not a template's form:

- 6 more of `rule_cases.py`'s fixtures: the fixture project's own files (`# Contributing` at `:124`, `# textutil` at `:198` and `:442`, `# Helpers` at `:614`, `## shout` at `:616`), the issue body `# #101 shout turns empty text into a lone mark` (`:760`), and `# {item} — broad gate` (`:836`), the title of `trail/gate.md`.
- `skills/verify/scripts/broad_gate.py:2502`, which writes the title of `trail/gate.md` as `# {name} — broad gate` and which the probe renders `# {} {} broad gate`. No template gives `trail/gate.md`, and this title and the fixture's agree.
- 6 headings of the pull request body `skills/code-review/scripts/pr_body.py` writes (`## From the records`, `## What changed`, `## How it was built`, `## Review rounds`, `## Questions`, ``### `{path}` ``). That form's home is the script, and no template gives it. Its `## Broad gate` at `:186` shares the words of `templates/setup/config.md:209` and is listed as held, a match of words between two forms.
- 15 headings of reports a script prints: `skills/verify/scripts/payload_meter.py` (5), `skills/verify/scripts/session_cost.py` (1), `evals/scripts/noninferiority.py` (3), `.github/scripts/release_report.py` (2), `.github/scripts/durations_union.py` (2), and the two headings of the release note's tail at `.github/scripts/publish_release_note.py:453` and `:455`.
- 6 section headings of a module docstring: `skills/verify/scripts/pact_check.py` (5) and `.github/scripts/issue_claims_check.py:42`.
- `hooks/lib/cmdline.py:140`, a shell comment a docstring quotes.
- `skills/code-review/scripts/chain_check.py:173`, the pattern `### (?P<number>[1-9][0-9]*)\. .+` that reads a finding's heading. It is the shape of `templates/records/sdd-round.md:9`, `### 1. <what is wrong, as a symptom, in one line>`, with the number free, and the two agree.
- 3 markers: `<!-- specs/<id> -->` and `<!-- specs/{work_item_id} -->` at `skills/settle/scripts/settle.py:126` and `:437`, the line that opened a release note's entry before #1139 and that `settle --apply` still reads in the notes published then, as the module's docstring says; and the sentence at `hooks/lib/blocks.py:195` about a line whose last `<!--` has no `-->` after it, a docstring's prose.

The 32 held units each stand in a string of P8 in the template's words, by the listing. Beyond M3, the two steps of `.github/workflows/hygiene.yml` that say "One source: `templates/setup/hygiene.yml`" (`:111` and `:161`) were read against `templates/setup/hygiene.yml:69-91`: each step's name is the template's, and each runs the same script with the same argument from the repository's own path in place of the clone. They agree.

#### Instances R5

The 46 orphan headings *Command R5* marks near a template heading, each read at its coordinate:

- 21 are near misses a case plants so that a reader is shown to refuse, name or pass over them: `tests/skills/test_rule_changes.py` (10 spellings of `## Rule changes`, at `:172` to `:177`, `:209` and `:236`), `tests/skills/test_settle.py` (4 spellings of `## Judgments of the run`, at `:1282` to `:1284`, `:1321`, `:1349` and `:1555`), `tests/skills/test_unverified_check.py` (6 spellings of `## Not verified`, at `:201`, `:350`, `:360`, `:1318` and `:1399`), and `## Findings (3)` at `tests/evals/test_noninferiority.py:824`. `tests/skills/test_chain_check.py:1473` names its own as `NEAR_HEADING`.
- 15 are the titles of records a case hands to a reader that does not read the title: round records (`# i — review round 1` and `2`, `# r — review round 1`, `# review round`, `# Review round 1`), routing declarations (`# routing`, `# {} routing`, `# {} — routing`), designs (`# Design`, `# a design`, `# Grounding`), `trail/gate.md` (three titles naming a work item), and `templates/records/process.md` written into a scratch tree as `# Process changes` (`tests/text/test_a_record_carries_no_comment.py:61`), whose case reads the comment under it.
- 8 are no record's form: sections of a document a case reads (`## The broad gate` of `skills/verify/orchestration.md`, `## The migration config` of `skills/legacy-parity/SKILL.md`), the pull request body's `## Review rounds`, a release-note fragment's `### Removed`, and `tests/skills/test_payload_meter.py`'s fixture files (`# probe`, `## probe`, `## Repo rules`, `## Repo rules {}`).
- `### 1.` (8 sites, `tests/evals/test_rule_cases.py:345` and `tests/skills/test_chain_check.py:1347` and `:4314` among them) reads a finding's heading by the opening `templates/records/sdd-round.md:9` gives it, and agrees.
- `## User scenarios & acceptance` (`tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:36`) is the exemption R4's second drifted form stands under. Its comment states the template's heading and the difference, so the test and the template agree, and the difference is R4's.

The 15 of the other 293 orphan headings *Command R5*'s third block prints, read at their coordinates: each is a fixture document's heading (`# H`, `# a heading`, `# b`, `## B ##`, `## Here`, `## Same`, `### Three`, `### 2. the second` among them) or a heading a case writes to test a reader of sections (`## Orchestrator: also fenced`, `## Where this draws the line`), and none is a record's form. The 56 orphan headings that stand as a heading of another file are that file's sections, which a case reads.

The 51 orphan markers, each read in *Command R5*'s listing with `-v` and five at their coordinates: the HTML comments that `tests/skills/test_unverified_check.py`, `tests/hooks/test_config.py`, `tests/skills/test_broad_gate.py`, `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` and their neighbours plant to test how a reader hides a comment; `<!-- specs/<id> -->` entries, the old release-note marker R4 reads, in `tests/skills/test_settle.py` and `tests/skills/test_unverified_check.py`; `<!-- Verdict: sealed -->` at `tests/skills/test_chain_check.py:2919`, a verdict planted inside a comment to be refused; and `<!-- Closes #6 -->` at `tests/github/test_close_issues_on_release.py:445`, whose comment says the keyword's reading there is unmeasured. Each is planted on purpose.

The 37 pins *Command R5*'s fourth block prints stand verbatim in a template, by the listing. Eight were read at their assert lines: some read the template itself, and some read another file holding the same words, such as `tests/skills/test_chain_check.py:4116`, which reads `chain_check.py`'s output, and `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:798`, which reads `agents/crafter.md`. The pin `'Commit and pull request language'` (`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:46`) reads `skills/commit-pr-convention/SKILL.md`, and the comment above it is D9's.

#### Instances R6

*Command R6*'s first block finds no passage of 15 words or more that a template shares with an eval case, the opening comment of `templates/setup/pact.md` among the templates. The 24 units held in P10 stand in the generated cases' `scaffold.sh` files, in their graders and in `evals/README.md:31` (`## Findings`), each in the template's words.

The generated cases also hold R4's four drifted forms, as *Command R6*'s third block counts: `# Feature Specification` in the 10 cases built from the proofer's, the four crafter builds' and the five sealer cases' designs, `— review round 1` in the 5 sealer cases, `# routing` in all 17, and `## User scenarios & acceptance` in those 10 and the rename case. They are `rule_cases.py`'s output byte for byte (`trail/phases/phase-1.md` *Command R16*, second block, at `94635718e`), so the generator is their one source, and R4 counts each form once there. D3 regenerates them.

#### Instances R12

M1: R12.1, 35 words in `seal/config.md:3` and `skills/implement/scripts/seal.py:1491`. The comment at the head of `seal/config.md` is the one `seal.py#NEW_CONFIG` writes, and `seal/config.md:3` says that `seal mode` created the file. One fact.

M4, the marker: `hooks/lib/optin.py:70` holds `# What AgenticSeal maintains in seal/`, and the first line of `seal/README.md` and of `templates/setup/seal-README.md` is that line exactly. No other string of P8 holds it. Held.

M4, the item names: 9 names a string of P8 holds, each as a module constant or as the item a reader of `hooks/lib/config.py` is called with, and each an item `templates/setup/config.md` documents. `seal/config.md` holds rows for 5 of them; for `Pact`, `Policy root` and `Reference specs` the reader returns the template's default where no row stands, which the template states. The template's two language items are read by agents, and no script reads them (phase 1's *Instances R2* reads the agents' side). None has drifted.

The rows of `seal/follow-up.md`, read whole: of its 7 rows, the one at `:42` states a fact of P8's code. The others state facts of `skills/implement/SKILL.md` (`:43`), of test modules (`:44`, `:48`, `:49`, which phase 1's R13 reads), of the lint (`:47`, F11's), or of no file (`:46`). The row at `:42` asks whether `chain_check.py --worktree` should read routing declarations from the working tree, and argues: "It is not unsafe on the axis `read_record`'s docstring warns about". At `94635718e` `read_record`'s docstring reads "The file as git carries it at HEAD, or on disk under `WORKTREE`; None where there is none." (`skills/code-review/scripts/chain_check.py:474-476`), and warns about nothing. The warning the row cites, that a working tree differing from HEAD makes the local run "the more permissive of the two", stood in that docstring when the row was written (0155f0f52, 2026-09-08) and left it at 8350c5788 (#923, 2026-10-16) (*Command history*). Drifted: the row cites a docstring for an argument the docstring no longer makes, and D4 drafts it. The same row cites "that item's `frame/design.md` *The sharp question*" for work item `1788817289-local-mode-from-first-setup-to-the-gate`, whose directory is not under `seal/threads/` at `94635718e`. That citation is P6 with P7, outside this pair, and D4 takes it because one edit rewrites the row.

#### Instances F1

Read whole, 17 lines. The plugin's entry is named `agentic` (`:9`) with the description `.claude-plugin/plugin.json:5` gives, word for word, and the description is `README.md:8-9`'s first sentence. The owner `MichaelYcJo` is `plugin.json`'s author. `renames` maps `specseal` to `agentic` (`:14-16`). Each is held.

Drifted: `docs/releasing/branch-and-release.md:204-206` says "`.claude-plugin/plugin.json` holds the one copy; nothing else in the tree spells it, which is why `plugin_directory_check.py` reads the name out of that file instead of carrying a literal". This file spells the name at `:9` and `:15`, and each README edition spells it in its two install lines, `agentic@agenticseal` (*Command F*). The reason the sentence gives holds: `.github/scripts/plugin_directory_check.py#plugin_name` reads the name from `plugin.json` and carries no literal, and compares it with the entries of two marketplace files outside this repository, never with this file. The sentence's count of the name's holders is what drifted. The sentence moved between documents three times (*Command history*); the commit that first made it untrue was not traced. D8 drafts it.

#### Instances F2

Read whole, 21 lines. The name is F1's. The description is held with F1 and `README.md:8-9`. The version, `0.31.1`, is the one `docs/releasing/branch-and-release.md:15` says this file carries. The icon, `./.claude-plugin/icon.png`, is the file `.github/scripts/release_seal.py#draw` reads and copies (its docstring, lines 14 to 21), and `assets/seals/README.md:180-182` says the same. The license, MIT, is F9's row. None has drifted.

#### Instances F3

Read whole, 1 line: `* text=auto eol=lf`. `evals/scripts/behaviour.py:153` says "The committed cases are LF (`.gitattributes`)" and writes each case with `newline="\n"`. Held. `evals/scripts/seed_defects.py:349` says a checkout can end a line with CRLF under `core.autocrlf`, which is a case it handles in a user's repository, not a statement about this file.

#### Instances F4

Read whole, 1 line: `blank_issues_enabled: true`. No other file states it. `SECURITY.md:5-10` sends a vulnerability report to the private advisory page and asks for no public issue, and this file names no `contact_links` entry pointing there; that is an absence, and the two state nothing that disagrees. `CONTRIBUTING.md` *Proposing a new gate or skill* says a proposal opens an issue first, which a blank issue allows.

#### Instances F5

Read whole, 24 lines. Its `about` line names "The routing edit gate, the question gate, or another gate", and `hooks/routing-edit-gate.py` and `hooks/question-gate.py` exist. Held. Its example, "routing-edit-gate refused an edit on a branch a routing.md names", is a wrong call in the direction the gate is built to avoid, which agrees with the gate.

Drifted: `labels: gate` (`:4`). The tracker holds no label named `gate`; `gh api repos/:owner/:repo/labels/gate` exits 1, and the label for this area is `hooks-gates`, "Hooks, the commit gate, the worktree guard" (*Command tracker*). GitHub applies no label a repository does not hold, so a report filed through the form arrives unlabelled. The line stands since the first commit (*Command history*). Whether a `gate` label ever stood in the tracker was not read. No document states what a misfire report holds, so the form's fields have no second holder. D5 drafts the label.

#### Instances F6

Read whole, 34 lines. Eight facts, each held: the base is the open `release/vX.Y.Z` branch and not `main` (`CONTRIBUTING.md:5-6`); it is the one branch beginning `release/` in the dropdown (`:12-14`); a pull request into `main` is a release, and CI refuses one that changes what ships and leaves `plugin.json` alone (`:25-29`, and the version step of `.github/workflows/hygiene.yml`); nothing else catches the wrong base, since the milestone step answers `nothing to judge` for a head that is no release branch (`.github/scripts/release_completeness_check.py:357-363`); the Edit button changes the base (`CONTRIBUTING.md:21-23`); a contribution is not asked for a work item, a round record, a fragment or a version bump (`:53-75`, whose table also names two more, and the template says "including"); `bin/test tests/<file> -q` on the module touched (`:41-42`); and CI runs the rest on three platforms (`.github/workflows/test.yml:69-108`).

Drifted: the comment at `:29-34` tells a pull request that changes a gate to "Add: the test seen failing before the fix, which way the change leans (refusing more, or letting more through), whether it puts a new question in front of a person, and the platforms you could not test", and then that `CONTRIBUTING.md`, *What a change to a gate must carry*, "is the whole of it". That section asks a pull request for seven things (*Command F*): the four the comment names, and what the change removes, what the gate reads, and the gap only work with no work item passes through. It says of the prompt budget and of what a change removes that "Both are answered in the pull request body or they are not answered" (`CONTRIBUTING.md:396-399`). The comment is the pull request body's form and leaves one of those two out. *What it removes* entered the section at 5b1f6faea (2026-10-15) and *What it reads* at 96c11614f (2026-10-31); the template's list dates from 5f8fea996 (2026-09-21) and was not extended at either (*Command history*). D6 drafts it.

#### Instances F7

Read whole, 18 lines: Claude Code's local settings, macOS and editor files, and Python's caches. No document of the tree names an entry of this file or says a path of this repository is ignored by it. `.venv` is kept out of the index by the `.gitignore` of `*` that `uv` writes inside it, which `.github/scripts/run_tests.py` and its tests check, and not by this file. It states no fact another place states.

#### Instances F8

*Command files*' second block, at `94635718e`: no id names a module that is not there; 25 ids name a function their module does not define, holding 0.47% of the file's seconds; and 44 test functions are named by no id. Each of the 25 is a case renamed or removed since the file was last refreshed, such as `tests/behaviour/test_waiver_decided_at_start.py::test_the_template_PARSES_into_the_TWO_NEWEST_rows_it_ships`, whose module now defines `test_the_template_PARSES_into_the_NEWEST_row_it_ships`, one of the 44.

What the readers do with an id that names no case. `pytest-split` 0.11.0 drops every duration whose id is not a collected item before it averages, and gives a collected case with no id that average (`_remove_irrelevant_durations` and `_get_items_with_durations`, executed: *Command files*' third block), so such an id moves no case between shards. `test_the_durations_file_prices_the_suite` fails where more than `STALE_SHARE`, 0.05, of the collected cases have no price or of the file's seconds belong to ids the suite no longer collects (read: its module, lines 43 to 46, 90 and 285 to 296); at 0.47% of the seconds the second half holds, and the first needs the collection, which this row does not run.

Two facts `CONTRIBUTING.md` states of the file are held: "one collected case in twenty (`STALE_SHARE`)" and "one second in twenty" (`:181-183`) are the case's 0.05; and the file is measured by the Windows shards with `--store-durations --clean-durations` and divides the macOS shards too (`:166-178`), as `.github/workflows/test.yml:94-108` runs it. `CONTRIBUTING.md:166` says the file "goes stale as cases are added", so the 25 ids are that statement at work and not a drift.

#### Instances F9

Read whole, 21 lines: the MIT License, copyright "AgenticSeal contributors". `.claude-plugin/plugin.json:11` reads `"license": "MIT"`, `TRADEMARKS.md:3-4` names the MIT License and this file, and both README editions name MIT under their license heading and send the emblem to `TRADEMARKS.md` (*Command F*). Held.

#### Instances F10

Read whole, 319 lines. Six facts with another holder, each held:

- the plugin's icon is drawn from `owl.svg`, and the release note's `seal.png` is a copy of that icon (`:180-182`): `.github/scripts/release_seal.py`'s docstring, lines 14 to 21, and `docs/releasing/branch-and-release.md:98`;
- the drawings are not under the MIT License (`:15-17`): `TRADEMARKS.md:7-18`, which also lists this directory's files, the icon, `seal-mark.txt` and `seal.png`;
- `skills/verify/scripts/seal-mark.txt` is a 16 × 16 sprite (`:159-161`): the file holds 16 lines of 16 characters;
- every cell of the wax is one of fifteen colours (`:167`): `skills/verify/scripts/seal_stamp.py:24` and `:106`;
- `seal_stamp.py#read_sprite`, `#build`, `#SPRITE_COLOURS` and `DROP` (`:129-132`, `:161-165`, `:259`): each is defined in that module;
- no code reads an entry's files (`:19`): no script names `assets/seals/`, and the one mention, `.github/scripts/publish_release_note.py:653`, is a comment.

The byte counts and pixel rules the entries give were not redrawn here; they are the open part.

#### Instances F11

Read whole, 61 lines, and read with `seal/follow-up.md:47` and phase 1's R9.1. Five facts with another holder, each held:

- `lint-python` acts only where a project configures ruff (`:3-5`): `hooks/lint-python.py`'s docstring, which names `ruff.toml` among the files it looks for;
- `target-version = "py312"` is "the floor hooks/lib/launch.py holds" (`:27`): `FLOOR = (3, 12)` at `hooks/lib/launch.py:47`, `CONTRIBUTING.md:114`, and `tests/hooks/test_launch.py:167-175`, which holds the two equal;
- what runs before any floor is checked runs on whatever `python3` starts it and is linted at the per-file target (`:35-39`): `CONTRIBUTING.md:122-126` and `tests/censuses.py:756-760`, the passage phase 1's R9.1 reads;
- macOS ships 3.9 under that name (`:37`): `CONTRIBUTING.md:136`;
- `E501` is not selected (`seal/follow-up.md:47`): `select` at `:55` takes `E4`, `E402`, `E7` and `E9`, and no `E5`.

The comment's account of the rules left out, BLE001, PLW1510, S110 and S112 (`:12-17`), has no other holder; `select` at `:55` names none of their families, so the file agrees with itself.

Drifted: `:40-42` says "tests/hooks/test_launch.py derives that set, holds every file of it to this table, and refuses in each the syntax and the two constructs above that this version lacks", and `CONTRIBUTING.md:126-130` says the same of that module. At `94635718e` `tests/hooks/test_launch.py#test_what_runs_before_any_floor_is_linted_at_the_floor` derives the set and holds it to the table, and its docstring says that "the `floor_syntax` census in `tests/censuses.py` refuses in each file the table names what a `python3` at its version cannot run" (`:210-212`). `tests/censuses.py:761-763` says the same from its side, and `tests/censuses.py#floor_syntax` is the code that parses with `feature_version` and names `zip(..., strict=)` and `datetime.UTC`. The refusal moved to the census at cbf97bf55 (#942, 2026-10-24), and the `ruff.toml` sentence dates from ce448bbef (2026-10-15) (*Command history*). D7 drafts both holders, since one cause wrote both.

### Drafts

Each draft below rests on this record's measure at `94635718e` and changes no rule of the policy root. *Command tracker* searched the open issues before each was drafted, and no open issue holds any of their drifts.

#### D3

**Title.** `test: the eval cases' fixture records carry titles no template gives, a design still titled Feature Specification among them`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances R4* and *Instances R6*, and *Whether the frame holds*, the item on a fixture's title.

**What is wrong.** `evals/scripts/rule_cases.py` writes the records of each fixture case: a design, a plan, a routing declaration, and for the sealer's cases a phase record, a round record and a closing memo. Four of its forms differ from the template that gives the same record. Its designs are titled `# Feature Specification: …`, the title `templates/records/sdd-design.md` dropped for `# Design: <work item>` in #1151; the rename case, written later, already uses `# Design:`. Its scenario heading lacks the template's ` *(mandatory)*`. Its round record is titled `# {item} — review round 1`, where the template gives `# Review round <N>: <work-item-id>`. Its routing declaration is titled `# routing`, where the template gives `# Routing: <work-item-id>`. No script reads a title, so no case changes its verdict. The agent under evaluation reads these records as a work item's records, and `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` states the intent that a scaffold copies the record shapes from this plugin's templates, so the agent meets what a session writes in production.

**Scope.** The four forms in `evals/scripts/rule_cases.py`, and the cases it writes under `evals/behaviour/`, regenerated with `rule_cases.py --out`. `RECORD_LINES` in `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` and its comment, where the scenario heading changes, since that line is exempt from the refused word `scenario` only in its exact spelling. `tests/e2e/teammate/test_teammate_flow.py:64` writes `# Feature Specification: a work item` into a test fixture whose reader does not read the title; the issue decides whether it goes with the rest. Out: the templates, and every reader of records.

**Done when.** Each record a fixture case holds opens with the title its template gives, and its headings are the template's. The cases under `evals/behaviour/` are the generator's output byte for byte again. The paid runs that #1107, #1178 and #1266 wait for grade the cases this changes, and the pull request names that.

**Proposed milestone.** `backlog: review chain & agents`. Its description names "the agents that run the chain", and these cases are what the agents' behaviour is measured on, beside #1107, #1178 and #1266 in the same milestone. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** R4, and R6's copies of R4's forms.

#### D4

**Title.** `fix: the follow-up row on chain_check.py --worktree argues from a docstring warning that #923 removed, and cites a work item no longer under seal/threads/`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances R12*.

**What is wrong.** The row of `seal/follow-up.md` *Schedulable items with nowhere else to go* that asks whether `chain_check.py --worktree` should read routing declarations from the working tree argues that "It is not unsafe on the axis `read_record`'s docstring warns about". `read_record`'s docstring in `skills/code-review/scripts/chain_check.py` warned, when the row was written, that a working tree differing from HEAD makes the local run the more permissive of the two. #923 removed that warning, and the docstring now says only where the file is read from. A reader who opens the docstring to weigh the row's argument finds no axis there. The row also sends the reader to `frame/design.md` *The sharp question* of work item `1788817289-local-mode-from-first-setup-to-the-gate`, whose directory is no longer under `seal/threads/`, so the citation reaches it only through git history. Which commit removed the directory was not traced.

**Scope.** That one row: its argument stated in its own words, or cited where it now stands, and its citation of the removed work item given as a commit and path that reach it, or replaced by the argument itself. Out: the question the row asks the owner, which stays the owner's, and `chain_check.py`.

**Done when.** Every coordinate the row cites holds, at the commit that changes it, what the row says it holds.

**Proposed milestone.** `backlog: docs drift`. Its description is "Documents, skills, templates and agent files that claim behaviour the code does not have", and the row claims a docstring states a warning the code no longer has. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** R12.

#### D5

**Title.** `fix: the gate-misfire issue form applies the label gate, which the tracker does not have, so every report through it arrives unlabelled`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances F5*.

**What is wrong.** `.github/ISSUE_TEMPLATE/gate-misfired.md` applies `labels: gate`. The repository holds no label named `gate`, and its label for this area is `hooks-gates`. GitHub applies no label the repository does not hold, so a report of a gate's wrong call arrives with no label, and a search by `hooks-gates` does not find it.

**Scope.** The form's `labels:` line, naming a label the tracker holds, or the label created, whichever the owner picks. Out: the form's fields.

**Done when.** An issue opened through the form carries a label that `gh label list` lists.

**Proposed milestone.** `backlog: gates & hooks`. Its description names "how a hook fails", and the form is how a person reports a gate that failed. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** F5.

#### D6

**Title.** `docs: the pull request template asks a gate change for four of the seven things CONTRIBUTING.md asks, and leaves out what it removes, which only the body answers`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances F6*.

**What is wrong.** The comment in `.github/PULL_REQUEST_TEMPLATE.md` on changing a gate lists what to add: the test seen failing, the failure direction, whether a new question reaches a person, and the platforms not tested. `CONTRIBUTING.md` *What a change to a gate must carry*, which the comment calls "the whole of it", also asks what the change removes, what the gate reads, and whether a gap is one only work with no work item passes through. That section says the prompt budget and what a change removes are answered in the pull request body or not at all. A contributor who follows the template writes a body without the second, and nothing else asks for it.

**Scope.** The comment's list, made to name every item the section asks of the pull request, or cut to the citation of the section alone. Out: `CONTRIBUTING.md`; its own short list under *What a contribution is asked for* names four items and is P5's, outside this measure.

**Done when.** The template names no subset of the section's items as what a gate change adds, and no item the section says only the body answers is left out of it.

**Proposed milestone.** `backlog: docs drift`. Its description names documents and templates whose claims the tree does not bear out, and this template claims a list is the section's whole. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** F6.

#### D7

**Title.** `docs: ruff.toml and CONTRIBUTING.md say test_launch.py refuses what the floor cannot run, which the floor_syntax census does since #942`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances F11*.

**What is wrong.** The comment above `[per-file-target-version]` in `ruff.toml`, and the paragraph on the Python floor in `CONTRIBUTING.md` *Running the checks*, each say that `tests/hooks/test_launch.py` derives the set of files that run before any floor is checked, holds it to the table, and refuses in each the syntax and the two constructs the version lacks. Since #942 the module derives and holds the set, and `tests/censuses.py#floor_syntax` does the refusing; both test files say so. A reader who opens `test_launch.py` for the refusal does not find it.

**Scope.** The two sentences, which name the census for the refusal. Out: the tests, which agree with each other.

**Done when.** Each sentence names the code that does what it says, at the commit that changes it.

**Proposed milestone.** `backlog: docs drift`. Its description is "Documents, skills, templates and agent files that claim behaviour the code does not have", and both sentences claim a module does what another does. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** F11, and the `CONTRIBUTING.md` instance in R9's open part (*Whether the frame holds*, the item *Outside these pairs*).

#### D8

**Title.** `fix: branch-and-release.md says plugin.json holds the plugin's name alone, and the marketplace file and both READMEs spell it`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances F1*.

**What is wrong.** `docs/releasing/branch-and-release.md`, in the paragraph *The plugin's name is fixed*, says `.claude-plugin/plugin.json` "holds the one copy; nothing else in the tree spells it". `.claude-plugin/marketplace.json` names the plugin's entry with it and maps the old name to it, and each README edition spells it in its install commands. The paragraph's conclusion holds, since `plugin_directory_check.py` reads the name from `plugin.json` and carries no literal, but a reader planning a rename from it would leave the marketplace file and the install lines with the old name.

**Scope.** That sentence, which says where the name is written, or names `plugin.json` as the copy the scripts read. Out: the manifests and the READMEs.

**Done when.** The paragraph names no single copy of the name that the tree contradicts.

**Proposed milestone.** `backlog: docs drift`. Its description is "Documents, skills, templates and agent files that claim behaviour the code does not have", and the sentence claims a state of the tree the tree does not have. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** F1.

#### D9

**Title.** `test: a comment says hooks/lib/config.py reads the Commit and pull request language row, and no script reads it`

**Body.**

The measure is `seal/threads/1793758948-each-pair-that-can-hold-one-fact-twice-is-measured/trail/phases/phase-2.md` at `94635718e`, *Instances R12* (the item names M4 lists) and *Whether the frame holds*, the item *Outside these pairs*.

**What is wrong.** In `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_skill_names_the_file_and_the_row`, the comment above the second assert calls `Commit and pull request language` "The row's item, which `hooks/lib/config.py` reads and a session looks for in the file". No script calls a reader of `hooks/lib/config.py` with that item, and no string of the scripts holds it; a session reads the row by the skill's instruction. The comment came with #1278.

**Scope.** That comment. Out: the assert, which reads the skill, and `hooks/lib/config.py`.

**Done when.** The comment names who reads the row as the tree has it at the commit that changes it.

**Proposed milestone.** `backlog: docs drift`. A test comment is none of the four kinds its description names, and it is the area whose claim, a text stating a reader the code does not have, this drift is, as phase 1's D2 judged for a test docstring. No `release:` milestone's description names it (`frame/questions.md` Q1's default, against `docs/releasing/issues-and-milestones.md` *A milestone answers when, and takes three shapes*).

**Answers.** None of this phase's rows; R15's open part in `trail/phases/phase-1.md` *The table*.

### Phase-boundary run

The phase adds files under this work item's directory and builds no code, so no case is written new and no `seal mutate` run is owed (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the prose row).

With the record and `gaps.md` committed at a2f276ef8, one command ran the case plan row 1 names and row 2's "the same" carries, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, and the 28 test modules that phase 1's two searches list at that head, the modules that read `seal/` of the tree and those that walk the whole tree (`trail/phases/phase-1.md` *Phase-boundary run* gives both searches; `tests/conftest.py`, which they also print, is no test module). It exited 0 with "1920 passed" (executed: `bin/test <the case> <the 28 modules> -q`). The set is a sample of two searches, and `gaps.md` hands the rest to the broad gate.

Every command block of this record but *Command history* and *Command tracker* was run again, after phase 1's *Command setup*, from a fresh scratch copy after the record was written, and each printed what its text states (executed: the blocks extracted from the two records and run in order with `bash`; the script the extracted *Command setup* writes is byte-identical to the one the counts came from, and no `__pycache__` stood in the copy at the end). *Command history* and *Command tracker* were run on 2026-11-04 from the clone, and printed what their text states.
