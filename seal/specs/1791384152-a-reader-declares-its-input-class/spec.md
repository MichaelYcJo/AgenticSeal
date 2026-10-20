# Feature Specification: a reader declares its input class (#835)

<!-- seal/specs/1791384152-a-reader-declares-its-input-class/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Reframed 2026-10-12 at the owner's request, before anything was built: the
population rule is inverted (§*How a reader is found*), the frame is
re-based on the tree after six siblings landed, and every count is the
reading of a moment. Re-based the same day, on the owner's direction that
this item builds last, against the tree every 0.21.0 sibling left:
`origin/release/v0.21.0` at c38f97d7, merged into this branch as 4ba84e19.
Every count below is read at 4ba84e19 unless it says otherwise. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | both checks run with nobody asked; a check that reads a person's sentence is the guess class the inventory counts as the shape that reopens, so neither check reads one |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | where #835 says the two rules are stated; each gets a bullet there that links to its home |
| `CONTRIBUTING.md` §*House rules* › *A change writes a fragment, never a shared registry* | why the registry is not a table every change edits; three branches once conflicted on one shared file, and eleven were open this release |
| `docs/the-record-layout.md` §*docs/*, §*The size a reader takes whole*, §*A change writes fragments, never a shared file* | what a `docs/` document is (standing policy), the 1,000-line ceiling, and the fragment rule the registry's shape has to satisfy |
| `docs/the-evidence-ledger.md` §*A row is a content anchor, and it names no commit* | the coordinate grammar a `## Removes` row writes, and the rule that the checker calls git for nothing, which bounds what the Removes judgment can read |
| `docs/the-evidence-ledger.md` §*A claim held by a test* and `templates/ledger.md` §*A row held by a test* (#836, landed 23f5977c) | a row that names its test carries no hash, so no docstring line drifts it; the backfill's drift cost below counts hashed anchors only, and a row moved onto its test leaves the count |
| `skills/evidence-check/scripts/evidence_check.py#bounding_rule` and `#unbounded` (#870, landed be464c06) | a unit is bounded by `ast` in `.py` and `.pyi`, by the heading rule in `.md`, and nowhere else; a bare symbol anywhere else is refused with the quoted line to write. The `## Removes` coordinate is read by the same rule and refused the same way |
| `docs/the-commit-gate-inside-git.md` §*The convergence argument is claimed for commits alone* | the one precedent in `docs/` for the owner's direction: a reader that predicts a foreign tool does not converge, and the cure was to observe the act. The population rule below is chosen against the same argument |
| `skills/settle/SKILL.md` §*2. Write one standing statement per segment* | a new `docs/` document is created only for an area that has none; the statement shape with `Enforced by:`; `Enforced by: nothing — <why>` as the shape a rule nothing reads takes |
| `templates/config.md` §*The fold's values*, §*The ledger freeze* | the cutoff-row pattern `Removes from` copies: a work-item id, absent means not checked, an unparsable value is refused naming the row |
| `seal/follow-up.md`, the preamble | a thing tied to a coordinate lives at the coordinate and `grep` is the list that needs no file kept in sync; this is why the registry is the code's own docstrings |
| `skills/implement/SKILL.md` §*5. Incorporate review* | what a mechanism is, for rule 2: a rule, a checker, a template section, a walk |
| `skills/agent-contract/SKILL.md` §12, §14, §15 | enumerate the class; a change to what a person sees is documented and pinned in the same commit; a case is seen red before it is planted |
| #834 `spec.md` §*What the table says* and `inventory/6-tests.md` §*Observations*, `7-records.md`, `8-evidence.md` (branch `chore/834-every-reader-and-record-is-inventoried`) | the class counts and the converged/not-converged split both rules rest on; the finding that the readers patched most often are exemption and classification tables, which is what an enumeration of reading calls would be |
| #834 `handoff.md` §*Review of the run* and §*What the owner decided* (same branch) | 0.21.0's theme — every reader gets one of three fates: observe, force a format, or delete — and the finding that each chain that did not converge sat in a reader imitating a foreign tool. This item is the mechanism meant to hold the theme after the release, so it must not take that shape itself |

Two tests are the precedents the registry check copies, and both are cited by
path so the build opens them: `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
(`tracked_python` walks `git ls-files '*.py'` so the file set is observed,
`judge` resolves a module call through the file's own imports, `ALLOWED`
carries grounds per entry, and `test_the_failure_names_the_site_and_the_repair`
pins the text) and `tests/test_every_reader_ends_a_line_where_gfm_does.py`
(`splitlines_calls` and `_walk`: a census of calls keyed `(path, unit)`, held
closed by a test that is red for a call the list does not name and for a
named unit that no longer makes one).

## Scope

**In.** Two rules, each with the one check that holds it, and the document
that states them.

1. **Every unit of shipped Python declares what it reads, in its own
   docstring.** The registry is the code: every top-level `def` and `class`
   in every tracked `.py` file outside the test modules carries one line
   `Reads: <class> — <what it reads>; unknown <direction>`, or
   `Reads: nothing — <why>`. A test finds the population from the AST and
   refuses a unit with no declaration, a declaration outside the vocabulary,
   a `nothing` declaration on a unit whose body calls a reading primitive
   the test knows, and a census line (the transition, below) whose unit has
   changed or gone. **No list of calls decides who must declare.** The
   population is closed by a rule a walk can apply whole — every unit — and
   the call list is a contradiction check, so a call it does not know leaves
   the unit's duty untouched (§*How a reader is found*).
2. **A mechanism names one it removes, in `spec.md`.** A `## Removes` section
   in the frame's own file holds coordinates in the ledger's grammar, or the
   one line `nothing — <why>`. The records arm of `evidence-check`, which
   already reads every live work item's `spec.md` on every ledger run, reads
   a row's coordinate as a claim of absence: one that still resolves at HEAD
   is a finding. Where `seal/config.md` declares `Removes from`, a live
   `spec.md` of a work item at or above it must carry the section.

The population, the vocabulary, the census, the section's shape and what
neither check can read are each decided below, and `docs/the-reader-registry.md`
is their permanent home.

**Out, and why.**

- **A table under `docs/`, which the ticket's wording asked for.** Decided
  by the owner on 2026-10-08 (`questions.md` Q1, answer (a)) on four grounds
  that are each in the tree: the 1,000-line ceiling against a 2,287-line
  inventory; the shared-file rule against a table every reader change edits;
  a second copy of a judgment the docstring carries once, which is the shape
  #834 found disagreeing with itself; and the table's own `Class` parse,
  which read 1,381 of 1,467 rows. The `docs/` home is therefore the rule,
  not the rows.
- **Test functions, and every other unit inside `tests/test_*.py`.** A test
  pin's class is its assertion's shape, by the inventory's own rule in
  `inventory/6-tests.md`: a presence pin is `guess`, `refused`; an absence
  pin is `guess`, `passed`. The helpers beside the pins are excluded with
  them, by one rule the walker applies to a file name and not by a list of
  calls, and the exclusion's size is measured so nobody mistakes it for
  small: 1,683 non-test top-level `def`s inside the 180 `tests/test_*.py`
  modules at 4ba84e19, 618 of them calling a K1 primitive by the
  import-resolving reading §*The population* states (the framer's probe,
  2026-10-12; the same reading gives 1,654 and 602 at 62c27416, and the
  morning probe's 1,671 and 692 matched module functions bare). The four
  helper modules the inventory counts as code
  (`tests/conftest.py`, `tests/block_shapes.py`, `tests/commonmark_oracle.py`,
  `tests/gfm_table_oracle.py`) are in the population, and so is any other
  tracked `.py` under `tests/` whose name does not begin `test_`. Widening
  the population to the pins' helpers is one exclusion deleted from the
  walker and a census of their units; it is weighed after the census below
  has shrunk, with the number, and not here.
- **`bin/` and the shell steps of `.github/workflows/*.yml`.** No AST; the
  inventory's rows for them (part 5) stay what they are, a reading. The
  mechanism sees Python and says so (§*What neither check can read*).
- **A ratchet on the `guess` count.** It cannot be set before the count is
  known, and the count is known only once the census below is empty, which
  is #834's build. Whether a `Reads: guess` then costs a removal is the
  repository owner's decision, taken with the count; this item prints no
  number and pins none, because a count pinned in prose is the shape
  `inventory/6-tests.md` §*Observations* names as a reader of a sentence.
- **Re-reading whether a declaration is still true.** Nothing re-reads a
  class once written, the way nothing re-reads whether an `Enforced by:`
  target still enforces its sentence (part 7 row 8). The warden reads the
  diff's `Reads:` lines at review; that is where a `guess` and a `nothing`
  are argued.
- **Finding readers by what a run observed them do.** Weighed and not taken
  as the population rule (§*How a reader is found*, (c)); a later item may
  add it as a cross-check on `nothing` declarations, and this frame files
  nothing.
- **Siblings' units.** The build changes no reader's body. Every 0.21.0
  sibling has landed, and no shipped unit carries a `Reads:` line yet
  (`grep -rnE '^\s*Reads: ' --include='*.py' hooks skills .github tests`
  finds none outside `tests/test_*.py` at 4ba84e19), so the 39 units the
  four late siblings added are on the census like every other unit, and
  the 14 they removed are not in the population. `plan.md` §*Seams* names
  each, as the probe read them between 62c27416 and 4ba84e19; the classes
  #866's and #870's specs state beside their units are #834's backfill
  source, not this build's.

## The decisions

### How a reader is found: the default is inverted

The frame of 2026-10-08 found the population from a list K1 of reading
calls: a unit was in the population when its body called one, and *a call
K1 does not know is a K1 row*. The owner's review of the run named what that
is: an enumeration over an open domain — every way Python code can take an
input — whose failure direction is quiet. A unit reading through a call K1
does not list is not found, needs no declaration, and passes with nothing
said. That is the shape #868 took three rounds to learn in bash (every brace
spelling), #860 in merge shapes, #836 in `skip` spellings and #870 in nine
lexers, and each was cured by observation, a forced format, or deletion —
never by one more row. A mechanism meant to hold that theme cannot be built
in the shape the theme refuses. Three ways were weighed.

| | What finds a reader | Failure direction | Cost | Verdict |
|---|---|---|---|---|
| (a) K1, stated plainly | a listed call in the unit's body | **quiet**: an unlisted call exempts the unit and nothing says so | 621 declarations at 4ba84e19 by the import-resolving reading (the morning probe's 657 at 81037623 matched `load` and `run` bare) | rejected: the trap the mechanism exists to prevent, kept as the mechanism's own population rule |
| (b) the default inverted | every top-level unit; a unit is exempt from nothing, and says `nothing` where it reads nothing | **loud**: an undeclared unit fails whatever it calls; what passes is a false declaration, which is a claim a reviewer reads, never an absence nobody sees | 1,587 declarations at 4ba84e19; 2,392 released ledger anchors on 943 of those units, and 691 more in the ten live fragments on 247 units, drift when their docstrings change (§*The census*) | **chosen** |
| (c) found by what a run observed | an audit hook (`sys.addaudithook`: `open`, `subprocess.Popen`, `os.listdir`, …) during the suite, attributed to a unit by its stack | **quiet, moved**: a unit the suite never exercises is never seen; the hooks run as `python3 <script>` children, so the hook has to be injected into each; and a regex over a string — the `guess` class, the one the theme is about — is pure computation that no audit event reports | a runtime harness per process, and a population that changes with which tests ran | rejected as the population rule; it observes `owned` and `observed` reads only, and cannot see a guess |

**(b) is the forced format, applied to the registry itself.** The rule a
walk can apply whole is *every unit declares*, and `ast` over `git ls-files`
is an observed population, not a predicted one. K1 stays, demoted: it no
longer selects who declares, it refuses one lie it can see — `Reads: nothing`
on a unit whose body calls a primitive K1 lists — naming the call. Its miss
direction is now a false `nothing` that passes, on a unit that still had to
declare and whose line the warden reads, where before it was a unit that
never appeared. A call K1 does not know is still a row to add to K1, and the
row buys one more contradiction the check can see, never one more unit in
the population.

**What (b) also reaches that (a) could not.** A unit that decides from text
another unit read — `==`, `in`, `startswith` and no primitive, the
inventory's `understood`-shaped rows — was a voluntary declaration under (a).
Under (b) it declares like every other unit, and its class is the class of
the text it was handed (`guess` where a person wrote it), which is where the
inventory found the reopening families sitting.

**What (b) costs, stated so nobody discovers it.** 1,587 units at 4ba84e19
against 621, and 194 of them have no docstring at all. The census carries
every one until it is touched, so the cost is paid per touch, one docstring
line, by whoever changes the unit — and by #834's backfill where it writes
lines in bulk. A docstring line moves the unit's ledger hash, so each line
written on an anchored unit drifts its rows: at 4ba84e19, 943 population
units carry 2,392 anchors in the 44 released files, each of which owes a
`Re-read ·` row under the freeze, and 247 units carry 691 anchors in the ten
live `seal/ledger/*.md` fragments, which `--reverify` re-stamps in place
until the 0.21.0 fold releases them. A row #836 moved onto its test has no
hash and is in neither count (five released rows at #836's landing, its
`overview.md` §*Not done*). That is the re-read cost the owner's review calls
structural, handed to #834's build in full if it backfills everything at
once; the census makes *at once* a choice and not a requirement, and when
and how much to backfill is #834's spec and the owner's, decided now that
#836's test rows have landed (`questions.md` Q7).

### The registry is the code, and `docs/` holds the rule

A declaration lives where a `# RIDER:` lives: at the coordinate, so that
opening the unit is what finds it and `grep -rn "Reads: guess"` is the list.
`docs/the-reader-registry.md` is the one document for the area, created
because none owns it (`skills/settle/SKILL.md` §2): it states the vocabulary,
the grammar, the population, the census and the `## Removes` section, each
as a standing statement with its `Enforced by:` line, and it records the
counts at landing as the reading of a moment, not as a pin.
`docs/the-record-layout.md`'s *docs/* table gains its row, and
`CONTRIBUTING.md` §*What a change to a gate must carry* gains two bullets that
state each rule in one sentence and link here.

### The vocabulary, and the grammar the check reads

The classes are the inventory's three with one more for a unit that reads
nothing it decides from:

| Class | Means |
|---|---|
| `owned` | a format this repository's own writer produces, or a vocabulary its own checker defines |
| `observed` | a fact asked of the system — an exit code, an AST, `git ls-files`, a JSON a program wrote, an attempted call |
| `guess` | a person's text, or a shape predicted from text the reader does not control |
| `nothing` | the unit decides nothing from any input it did not get as an argument from a unit that declares for it: a writer, a formatter of its own output, a pure function over values. A unit that parses text its caller handed it is not `nothing`; it is the class of where that text came from |

The direction is the inventory's: `refused`, `passed`, `mixed`.

```
Reads: <owned|observed|guess> — <what it reads, for a person>; unknown <refused|passed|mixed>
Reads: nothing — <why the unit is not a reading>
```

One line per unit, anywhere in the unit's docstring, the class word first
after `Reads:` and the direction word last after `; unknown`. The check reads
the two words and nothing between them; the prose is the reviewer's. A unit
that reads several inputs declares the weakest class it reads, `guess` being
weakest. ` — ` and ` -- ` are both the separator, because the words are read
by position and the dash is not read. A `nothing` line's reason is not
empty, the `Enforced by: nothing — <why>` rule.

### The population, by one rule and no list

Every top-level `def` and `class` in every tracked `.py` file whose path
does not match `tests/test_*.py`. The file set is `git ls-files -z --
'*.py'`, read NUL-separated the way `tracked_python` reads it in the
encoding test — so a tracked `.py` in a directory nobody listed is in the
population, and a root that moves is not a hole (the encoding test pins
exactly this with `test_the_walk_reaches_a_root_nobody_listed`). The unit is
the top-level one: methods and nested functions fold into the `class` or
`def` that holds them, and the class declares once for its methods. The
sweep declines when a listed file is not on disk, through
`conftest.decline_if_shrunken`, as every sweep here does.

Read by the framer's probe on 2026-10-12 at 4ba84e19, the merge of
`origin/release/v0.21.0` at c38f97d7 with every 0.21.0 sibling landed; 253
tracked `.py`, 180 of them `tests/test_*.py`, and no `test_*.py` outside
`tests/`. Phase 1 reads the same numbers again with the walker the test
will use, and records them with its own SHA:

| Root | Top-level units | Call a K1 primitive | No docstring |
|---|---|---|---|
| `hooks/` (with `hooks/git/`) | 461 | 162 | 68 |
| `skills/*/scripts/` | 854 | 344 | 69 |
| `.github/scripts/` | 211 | 94 | 49 |
| `tests/`, outside `test_*.py` | 61 | 21 | 8 |
| **total** | **1,587** | **621** | **194** |

The first and third columns are reproduced by one command, run in the
repository root:

```
git ls-files -z -- '*.py' | python3 -c "
import ast, sys, re, collections
c = collections.Counter()
for p in sys.stdin.buffer.read().split(b'\0'):
    p = p.decode()
    if not p or re.fullmatch(r'tests/test_[^/]*\.py', p):
        continue
    tops = [n for n in ast.parse(open(p, encoding='utf-8').read()).body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    c['units'] += len(tops)
    c['no docstring'] += sum(ast.get_docstring(n) is None for n in tops)
print(dict(c))"
```

The K1 column is the probe's import-resolving reading — a method by its
attribute name on any receiver (`.open`, `.read_text`, `.exists`, `.match`,
`.splitlines`, …), `open` and `input` bare, a module function only where
the file's imports bind the name (`subprocess.run`, `json.load`,
`shlex.split`, …), and `os.environ`, `sys.stdin`, `sys.argv` as references
— which is the rule below and the one phase 1's `k1_calls` implements. The
same reading at 62c27416 gives 1,562 / 619 / 195, so the four late
siblings added 25 units net (39 added, 14 removed; `plan.md` §*Seams*).
The morning probe's 657 matched `load` and `run` bare and is superseded.

Excluded by the one rule, and measured: 1,683 non-test top-level `def`s
inside `tests/test_*.py`, 618 of them calling a K1 primitive, and 17
top-level classes.

**K1, the contradiction list.** Two families, each closed by construction
and each a list to extend, never an exemption list to grow:

- **the process boundary** — `open`, `read_text`, `read_bytes`, `read`,
  `readline`, `readlines`, `input`; `subprocess.run`, `check_output`,
  `check_call`, `call`, `Popen`, `getoutput`, `getstatusoutput`, `os.popen`;
  `os.getenv`, `os.environ`, `sys.stdin`, `sys.argv`; `listdir`, `scandir`,
  `walk`, `glob`, `iglob`, `rglob`, `iterdir`; `exists`, `isfile`, `isdir`,
  `lexists`, `stat`;
- **a standard-library parser handed text** — `match`, `search`,
  `fullmatch`, `findall`, `finditer`, `sub`, `subn`; `shlex.split`;
  `json.load`, `loads`; `ast.parse`; `tomllib.load`, `loads`;
  `xml.etree` `parse`, `fromstring`; `csv.reader`, `DictReader`;
  `splitlines`.

Methods are matched by attribute name whatever the receiver, because a
compiled pattern is called on a name; a module function (`json.load`,
`subprocess.run`, `shlex.split`) is matched only where the file's imports
bind that name to that module, the encoding test's `judge` rule, because a
repository that defines its own `load` or `run` must not read as calling the
library's — the framer's probe matched `load` bare and counted four of this
repository's own module loaders as `json.load`, which is the mistake the
rule exists for. `str.split` is not in K1. The one thing K1 decides: a unit
declaring `nothing` whose body calls a K1 primitive is refused, naming the
unit, the call and the line.

**Module bodies.** A statement outside every `def` and `class` can read too:
two modules at 4ba84e19, fifteen `os.environ` references between them —
thirteen in `tests/conftest.py`, which has no module docstring, and two in
`skills/verify/scripts/pytest_record/specseal_pytest_record.py` (:139–140),
which has one (the morning probe's 14 counted sibling-module loads matched
as `json.load` bare; the import rule reads them as this repository's own
loaders). These are not units
of the population and the ledger has no spelling for them, so the rule is
the one place K1 still selects, bounded to a kind of code the walker can
count: a module whose body calls a K1 primitive outside any unit declares
for that body in its **module** docstring, with the same line, and is refused
without it naming the statement. A module body with no such call owes no
line and may carry one. Phase 1 counts the module bodies K1 selects, and the
document states the count and the limit: a module-level read through a call
K1 does not list is unseen, which is quiet, and it is the whole of what
stays quiet in rule 1.

### The census is the transition, and it only shrinks

`tests/undeclared_readers.txt` holds one line `path#unit@hash` for every
population unit undeclared when the check lands, the hash computed by
`evidence_check.content_hash` over the span `evidence_check.py_spans` gives,
imported and not copied. `unit` is the key `py_spans` gives, which for a
top-level `def` or `class` is its bare name (measured by the framer at
4ba84e19: `py_spans` keys `hooks/gate.py`'s `git` as `git`, a method as
`Resolution.__init__`, a nested function as `parsed_spans.walk`, and a
constant by its name; `questions.md` Q2), so the line is the ledger's own
spelling and `resolve_unit` finds it. A unit on the census with its hash unchanged is not
required to declare; one whose hash moved was changed, and the check says
*declare it and remove its line*; a line naming no undeclared population unit
— gone, renamed, declared since, or outside the population — is refused
naming the line. A malformed line is refused by the grammar. When the file
is empty the check says to delete it, and with no file it reads no census.
Under (b) the census starts at about 1,587 lines rather than 621, and it
need not empty on any schedule: a unit nobody touches stays listed with its
hash and costs nothing, and a unit anybody touches declares. The rule binds
every new unit from the landing and every changed one, which is the half of
the inventory's finding that costs — the families that reopened were readers
being changed. #834's build shrinks it in bulk where it chooses to.

### `## Removes`, read by the records arm

`templates/sdd-spec.md` gains the section above the framer's mark:

```markdown
## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| <a copy, a reader, a rule sentence, a test pin> | <path#unit, or path#"heading"[>"line"], or path#"a quoted line"> | <the file or record that now owns it, or why nothing needs to> |
```

or the one line `nothing — <why>`, with the reason not empty (the
`Enforced by: nothing — <why>` rule). The coordinate is the ledger's
grammar without a hash: a function or class for a `.py` or `.pyi` file, a
heading path for a `.md` file, a quoted line for every other file — the
three answers of `evidence_check.py#bounding_rule` (`"ast"`, `"heading"`,
`None`; #870, landed) — with an optional `>"quoted line"` narrowing to one
sentence. The records arm (`evidence_check.py#file_claims`, through
`claim_lines`) reads the rows under this heading as claims of absence and
under no other rule: a coordinate whose `resolve_unit(...).places` is
non-empty at HEAD is a finding, `STANDING`, graded as a stated name the tree
does not carry is graded today; the names on those lines are not read by the
name half. **A coordinate the ledger would refuse is refused here, never
read as gone**: a row whose cell is not a coordinate (the template's
placeholder), a `tests/x.py::test_y` node id (#836's grammar names a test
and no unit), or a bare symbol in a file `bounding_rule` bounds by no rule,
which `resolve_unit` answers as a `Resolution` with no `places` and the
sentence `unbounded` writes in `refused`, is refused naming the row —
otherwise a `foo.ts#bar` row would read as a removal that happened. The
section is read wherever it is present; where `seal/config.md` declares
`Removes from | <work-item id>`, a live `spec.md` at or above it with no
section, or an empty one, is a finding. The row is documented in
`templates/config.md` beside `Ledger frozen from`, whose reader it copies:
absent means not checked, a value that is not a work-item id is refused
naming the row. This repository sets the value at the build, to the epoch
second the row is written, so every 0.21.0 work item framed before it stays
unbound and every later frame is bound.

Why the records arm and not a new script or `unverified-check`: the arm
already opens every live `spec.md` on every ledger run — the advisor after
each commit, CI's evidence job, the broad gate under `--strict` — and it is
the reader that would otherwise refuse a correct removal as a stale name
(`coordinate_misses` reads a `path#name` by token of the file, so a removed
unit is a miss today). One reader of the section, no git, no new hygiene
step. What it cannot read: that the coordinate ever existed, so a misspelled
one in a Python file passes as gone — the warden opens the row at the base
at review; and the `<why>` of a `nothing` row, which the warden reads too.

### What neither check can read

Stated here once, and in the document at landing, so a reader of either
knows the edge before meeting it.

1. **A false declaration.** `Reads: nothing` on a unit that calls a K1
   primitive is refused; `nothing` on a unit reading through a call K1 does
   not list, and `owned` or `observed` on a unit that guesses, pass. The
   declaration exists for the warden to read at review, which is the whole
   re-reading; nothing else reads the prose.
2. **Units inside `tests/test_*.py` other than the pins' assertions.**
   Excluded by one rule on the file name, 618 of them calling a K1
   primitive at 4ba84e19, widened by deleting the rule.
3. **A reader outside Python.** `bin/`, the shell steps of the workflows, a
   `sh -c` string inside a Python call. The walk is `ast`.
4. **A module-level read through an unlisted call.** The one corner where K1
   still selects (§*The population*).
5. **A stale line.** A reader redesigned from `guess` to `owned` keeps its
   old line until somebody moves it; the diff's `Reads:` line is the
   warden's to read.
6. **A `## Removes` coordinate that never existed.** The arm reads HEAD; the
   base is the warden's.

### What this item removes

The per-phase table `templates/sdd-phase.md` §*What this phase removes*
(`| Removed item | Where it must land |`) and its pins in
`tests/test_a_phase_hands_the_next_one_a_record.py`. It recorded one fact —
what a work item takes out of the tree and where it lands — per phase, filled
by the builder, held to its shape by a template pin, its content read by the
next phase at most and drifted by nothing any check tracks (part 7 row 16:
*none tracked*). The `## Removes` section records the same fact once, at the
frame, with a check that reads it; a removal a phase makes that the frame
did not name is a divergence and goes where divergences go, `overview.md`'s
table. Two records of one fact is the shape #834 found disagreeing with
itself. Phase records already written keep their tables; they are records
of a moment.

### What #834's build does with this frame

The home the table moves into is the code: for every inventory row whose
unit is in the population, #834's build writes the row's `Class` and
`Unknown` into the unit's docstring as its `Reads:` line and removes the
unit's census line. For a population unit the inventory did not row, the
inventory's own reading at 5623d728 — every hook, script and helper was read
by an agent and the unit was judged not a reader — is the grounds for a
`Reads: nothing — <why>` line, and whether #834 writes those in bulk, in
part, or leaves them on the census is #834's spec, weighed against the
re-read cost above. The inventory's other columns — `Decides`, `Duplicates`,
`Note` — are the reading of a moment and stay under `inventory/` in #834's
directory, read at the release tag after the directory retires.
`skills/settle/scripts/settle.py#PROCESS_DIRS` does not list `inventory`, so
whether it leaves with the process record or with the fold is #834's spec to
say. The build lands after every other 0.21.0 chain and after this item,
because it touches most reader files and the census has to exist first.

## User scenarios & acceptance *(mandatory)*

Rule 1, the registry check (`tests/test_a_reader_declares_its_input_class.py`):

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| R1 a new unit is undeclared | Given a planted root with a top-level unit in a tracked `.py` outside `tests/test_*.py` that carries no `Reads:` line — one case calls no primitive at all, one calls an unlisted one — when the check runs, then it fails naming `path#unit`, the grammar, and that a pre-existing unit's repair is its census line | the planted cases; seen red first against this tree with one census line removed |
| R2 a declaration outside the vocabulary | Given `Reads: maybe — …`, a class line with no `; unknown <word>`, or `Reads: nothing` with no reason, then it fails naming the unit and the two words it reads | planted cases, one per defect |
| R3 a census unit changed | Given a census line whose hash is not the unit's, then it fails: *declare it and remove its census line* | planted root with a census file |
| R4 a census line names nothing | Given a line for a unit that is gone, renamed, declared since, or outside the population, then it fails naming the line | planted cases, one per cause |
| R5 the population is the file set | Given a tracked `.py` in a directory the test never names, then its units are in the population; given a `def` inside `tests/test_x.py` with no line, then it is not; given `tests/helpers.py` with no line, then it is | planted root with its own git listing |
| R6 the census grammar | Given a line that is not `path#unit@hash`, then it is refused naming the line; given an empty file, the check says to delete it; given no file, no census is read | planted cases |
| R7 the contradiction | Given a unit declaring `nothing` whose body calls one K1 primitive per family (a boundary call, `os.environ`, `sys.stdin`, a parser call through its import, `shlex.split`), then it fails naming the unit, the call and the line; given `str.split`, or a local `load` no import binds to `json`, then it passes; given a `nothing` unit calling a primitive K1 does not list, then it passes, and the case says in its name that this is the stated limit | parametrised planted cases |
| R8 this tree passes | Given this repository at landing, then every population unit is declared or on the census, and the census hashes are the tree's | the real-tree case |
| R9 the failure is the instruction | Given each failure, then its text is pinned whole, names the site and the repair, and the test's docstring states what the walk cannot see (§14, the encoding test's shape) | the pins |
| R10 a module body | Given a module whose body calls a K1 primitive outside any unit and whose module docstring carries no `Reads:` line, then it fails naming the statement; given the line, it passes; given a body with no such call and no line, it passes | planted cases; the two real ones at 4ba84e19 are `tests/conftest.py` (no module docstring, thirteen `os.environ` statements) and the pytest recorder (a docstring, two statements at :139–140) |

Rule 2, the `## Removes` section (`evidence-check`'s records arm):

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a named removal still stands | Given a live `spec.md` with a row whose coordinate resolves at HEAD, when `evidence-check` runs, then it reports `STANDING` with the coordinate, graded like a stated name the tree lacks | planted root with a ledger fragment; `bin/evidence-check` exit |
| S2 a removal that happened | Given a row whose coordinate names no unit at HEAD, then no finding, and no name on that line is read by the name half | planted root; the unit's name absent from the tree |
| S3 the `nothing` line | Given `nothing — <why>`, then no finding; given bare `nothing`, then refused naming the line | planted cases |
| S4 presence under the cutoff | Given `Removes from | N`, a live item at or above N with no section or an empty one fails naming the file; one below N is read where present and not required; with no row, presence is not checked | planted roots, one per branch |
| S5 the row's grammar, and a coordinate the ledger refuses | Given a coordinate cell that is not a coordinate (the template's placeholder), or a `tests/x.py::test_y` node id, then refused naming the row; given a bare symbol in a file `bounding_rule` answers `None` for (`f.ts#bar`), then `resolve_unit` returns no `places` and a `refused` sentence, and the row is refused naming it and the quoted-line form `unbounded` writes, never read as gone | planted cases; the refusal text is `unbounded`'s, pinned by `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` already |
| S6 the row refuses an unreadable value | Given `Removes from | 17x`, then exit 2 naming the row, in the `Ledger frozen from` shape | planted case |
| S7 quoted rows are not read | Given a row inside a fence or an HTML comment, then not read (`claim_lines`) | planted case |
| S8 the templates | Given `templates/sdd-spec.md`, then it carries the section above the mark and the mark is still last; given `templates/sdd-phase.md`, then it carries no *What this phase removes* section and no test pins one; `agents/framer.md`'s writes table and report list name the section | the pins moved in the same commit |
| S9 this item's own row | Given this `spec.md`, then its `## Removes` row names the phase template's section; the arm as it stands reads no quoted locator (`RECORD_COORD_RE`), so the row is silent until phase 3 teaches the arm, reports `STANDING` while the template still carries the section, and is clean once phase 3 removes it | `bin/evidence-check .` at a probe commit inside phase 3, before and after the template edit |

The document and the rules' statement:

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| D1 the home | Given `docs/the-reader-registry.md`, then every statement is a bold rule with grounds and one `Enforced by:` line, under the ceiling, and `fold-check` passes; the three ways to find a reader and the verdict are stated in it with the limits list | `bin/fold-check`; `tests/test_a_folded_statement_names_what_enforces_it.py` |
| D2 the rules are stated once | Given `CONTRIBUTING.md` §*What a change to a gate must carry*, then two bullets name the rules and link to the home; `docs/the-record-layout.md` §*docs/* has the row; `templates/config.md` documents `Removes from`; `seal/config.md` carries it | the text hygiene tests the brief names, and `tests/test_no_passage_is_pasted_into_a_second_file.py`'s ratchet unchanged |

## Data & interfaces

- `tests/undeclared_readers.txt` — one `path#unit@hash` per line, sorted by
  path then unit, LF-ended; the hash is `evidence_check.content_hash` over
  the `py_spans` span, eight hex characters. Read by the registry check only.
- `seal/config.md` row `Removes from | <work-item id>` — read by
  `evidence_check.py`'s records arm through `config_rule()`, the one config
  reader #867 left (`hooks/config.py`, or the vendored copy where no `hooks/`
  sits beside the checker).
- `spec.md` `## Removes` — the table above or `nothing — <why>`; read by the
  records arm.
- The docstring line `Reads: …` — read by the registry check; written by
  whoever writes or changes a population unit or a reading module body, and
  by #834's backfill.

## Rule changes

- nothing
  why: written: a frame names what its work removes, in docs/the-reader-registry.md;
    overturned: the units' input-class lines, taken out at af9c924b.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the per-phase removal table, a second record of what a work item takes out of the tree | `templates/sdd-phase.md#"## What this phase removes"` | this section, at the frame; a removal the frame did not name is a divergence row in `overview.md` |
| the table's pin, which held its two columns and its `none` row | `tests/test_a_phase_hands_the_next_one_a_record.py#test_removes_section_is_a_table_with_a_none_row` | `test_a_phase_record_carries_no_removal_table`, which holds the opposite, beside it; added by the build after round 1's ⬜ 4 |
| the pin that counted three sections | `tests/test_a_phase_hands_the_next_one_a_record.py#test_all_three_sections_exist_outside_comments` | `test_both_sections_exist_outside_comments`, the same pin over two; added by the build after round 1's ⬜ 4 |

## Open questions → questions.md

<!-- The line below is not the review chain's `Reframed <date> by <who>, after
round <N>.` and stands above the mark on purpose: `chain_check.py#frame_foot`
reads the foot from the last line up, takes any other sentence there as the
mark's slot, and returns no mark. Above the mark it is prose, and the mark
stays the foot. -->
Reframed 2026-10-12 by framer, before the build, at the owner's request after the run's review; re-based the same day on the tree every 0.21.0 sibling left (c38f97d7, merged as 4ba84e19).

Framed 2026-10-08 by framer, before the build.
