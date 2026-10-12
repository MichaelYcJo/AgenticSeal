# 1791384159 — review round 3 report

Round 3 of work item 1791384159 (#870, #848), draft PR #889, at
`ec3a2de22639aafb5e5fe5ed860dbe9f0a0f9b16`. This is a verifying round. Its
target is the diff of round 2's fixes, `4ed965ed..9f36b62c`, plus the table
and close commits. It answers round 2's six verdicts and judges the units
round 2's fixes created: `statement_at`, the `shown` argument of
`resolve_unit`, the five new cases, and the new `BROKEN` sentence for a
quoted line that is gone. All execution ran in a `git clone --no-local` of
the worktree at the target SHA, under the session scratchpad. In that clone
`origin/release/v0.21.0` was pointed at `ad447367`, the merge base.

## How the findings relate

Round 2's fixes close what round 2 found. Two defects sit inside the units
those fixes wrote:

1. **`statement_at` leaves a definition's decorators out.** It reads a
   statement's start from `lineno`, which `ast` puts on the `def` line. So a
   claim on a decorated `def` line reads `ok` after the decorator changes,
   and a claim on a method's decorator hashes the whole class (🟡 1).
2. **One new case is dated the day it was written.** It passes
   `--checked 2026-10-12`, and the checker refuses a date after today. CI ran
   it at 23:44 UTC on 2026-10-11, so the PR's ubuntu leg and macOS shard 1
   are red at the target SHA (🟡 2).

Then four smaller items. `statement_at` widens an arm header or a comment
line to the whole enclosing statement (⬜ 3). The new sentence for a gone
quoted line reads oddly on a markdown heading path (⬜ 4). Two are
corrections to this item's paperwork: one clause of a new `Corrected ·` row
(⬜ 5), and the changelog's condition for which claim rows move (⬜ 6).

## A claim on a decorated definition leaves its decorators out (🟡 1)

`statement_at` takes each statement's span as `node.lineno` to
`node.end_lineno` (`skills/evidence-check/scripts/evidence_check.py:963`).
Since Python 3.8, `ast` puts a decorated definition's `lineno` on its `def`
or `class` line, while the decorators sit inside the node, in
`decorator_list`. The major rule already knows this: `parsed_spans` starts a
definition at `min([child.lineno] + [d.lineno for d in child.decorator_list])`,
and the skill's region table says the span is the whole definition,
"decorators included — a decorator carries behaviour".

Executed against the target, with a probe that loaded the checker:

- `@functools.lru_cache(maxsize=1)` over `def f(a):`, unit `f`: the region is
  4–6 and the claim `>"def f(a):"` is 5–6. After the decorator becomes
  `maxsize=None`, the claim is still 5–6 with the same hash `19d9baaa`, so the
  row reads `ok` over the change.
- Inside `class C`, a claim on `@property` above `def p(self):` gives 1–7,
  the whole class. No statement `statement_at` measures starts at or before
  line 2 and holds it, except the class.
- The same class, a claim on `def p(self):` gives 3–4, without `@property`.

Why it matters: round 2's 🟡 1 was a claim region that left out part of what
the statement is, so a change there read `ok`. That is the same failure,
left behind in the decorator slot. The commit says the claim is "the
statement `ast` gives", and here `ast` gives a node that holds the
decorators. The old indentation rule also left them out, so nothing
regresses. But the release states the parser's answer and does not deliver
it for this shape.

Cost of the fix, counted: this repository's ledgers hold 7 resolving `.py`
quoted claims, and the decorator-aware rule gives every one of them the same
region it has now (executed). No row's hash moves. Fragment row U9
(`seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:22`)
cites `statement_at` and will read `DRIFTED` once, to be read again.

## A new case is dated the day it was written, and CI is red on it (🟡 2)

`test_a_claim_row_in_python_drifts_on_an_edit_inside_its_statement` fills
the row with `--checked 2026-10-12`
(`tests/test_a_unit_the_extractor_cannot_bound_is_refused.py:459`). The
checker refuses a reading dated after the day it runs. Read from the job
log of run 38185027460, at `ec3a2de2`:

```
E   ... `--checked 2026-10-12` is later than today, 2026-10-11 — a reading is not dated after the run that records it
FAILED tests/test_a_unit_the_extractor_cannot_bound_is_refused.py::test_a_claim_row_in_python_drifts_on_an_edit_inside_its_statement - AssertionError: assert 2 == 0
1 failed, 12996 passed, 81 skipped in 371.86s (0:06:11)
```

The macOS shard 1 log has the same single failure (`1 failed, 6262
passed`). The four Windows shards and macOS shards 2 and 3 were still pending
when this round read them. The case passed in this round's clone because the
local date there is already 2026-10-12.

Why it matters: the case's result depends on the runner's clock and time
zone. It is red for any run before 2026-10-12 in the runner's zone, and
green after. The PR's checks at the target SHA are red for that reason
alone. A re-run after midnight UTC will pass, so this is not a defect the
release ships. But it holds the PR red until somebody re-runs and records
why. The module's other cases use a date already past (`2026-10-08` at
line 157, `2026-10-07` at line 383), and one token brings this case into
line with them.

## Smaller items (⬜)

- **⬜ 3, an arm header or a comment line widens to the enclosing
  statement.** `statement_at` measures only `ast.stmt` nodes. An `except`
  handler is not one, and neither is a `case` arm. So a claim on
  `except ValueError:` gives the whole `try` (2–7), and a claim on `case 1:`
  gives the whole `match` (2–6) (executed). A claim on a comment line inside
  a function body gives the whole function (1–5), where the old rule gave
  the line alone (executed). Each widens, so it reads `DRIFTED` more often
  and never `ok` over a change. It costs a re-read when a sibling arm
  changes, and no row in this repository has this shape.
- **⬜ 4, the gone-line sentence on a markdown heading path.** A row citing
  `doc.md#"## A / ### B"`, after `### B` moved under `## C`, reads
  `locator not found — the quoted text is not in the file; quote the line as
  it reads now` (executed). Both headings are in the file. The sentence holds
  if the quoted text is read as the whole path. But a person reads it as
  "these headings are gone", and "quote the line" points away from the
  heading path the skill tells a markdown row to write. Something like "no
  section at that path; write the headings as they read now" would fit a
  heading path better (`skills/evidence-check/scripts/evidence_check.py:1860`).
- **⬜ 5, correction: one clause of the new 0.4.0 correction is false.**
  Fragment row 19 says "a claim row's tie stands, because two unrelated
  units can share one identical line". `judge` keeps a claim row's tie only
  when more than one place holds the claim's content. When exactly one
  does, `if hit and (len(hit) == 1 or not claim)` narrows to it
  (`evidence_check.py:1828`). Executed: in `v.md`, `"Same head"` heads two
  paragraphs, and the claim `>"only here"` is in only one of them. The row
  reads `1 ok` at exit 0. The released row carried the same imprecision,
  since the rule dates from `a77c5172`, before 0.4.0. The correction keeps it
  and its Verified cell says it holds. The cited case
  `test_two_units_sharing_one_claim_line_stay_ambiguous` is the two-hit
  shape only. A wording that holds: "a claim row's tie stands where more than
  one place holds the claim, because two unrelated units can share one
  identical line".
- **⬜ 6, correction: the changelog under-counts which claim rows move.**
  `changelog.md:45` says a quoted claim row reads `DRIFTED` once "where its
  claim grew through lines indented below the quoted one". In `.py`, the
  claim also moves where it never grew. A continuation line like `a,` inside
  a multi-line call was the line alone and is now the whole call (executed
  2–5; the old 3–3 is read from `literal_statements`). A comment line was the
  line alone and is now its function (⬜ 3). A bare minor anchor in a file no
  parser reads also becomes its line alone, and the sentence names only a
  quoted claim. Every such row announces itself as `DRIFTED`, so nothing
  reads `ok` wrongly. Only the installer's expectation is narrower than the
  behaviour.

## What was checked and holds

- **Round 2's yellow 1, in files no parser reads.** A claim is its line:
  `f.ts` claims give 1–1, 2–2 and 4–4, and the module's case passes
  (executed, slice 46 passed). In `.py`, `statement_at` matches the parser for
  a multi-line expression (2–5 from its first line and from a continuation
  line) and for a line inside a string (the assignment, 2–4) (executed). The
  only shapes it misses are 🟡 1 and ⬜ 3. Unparseable `.py` falls back to
  the line, from the `SyntaxError` branch (read).
- **Nothing else predicts a unit's extent.** `literal_statements` still grows
  by indentation, but after this fix its growth reaches a hash only in
  markdown, which the owner's direction keeps (1,259 claims, none past its
  line). In `.py` only its hit line is used. Outside both, the hit is cut to
  its line, and that includes a bare minor anchor. `read_citation`'s calls
  read released `.md` files. `text_regions` bounds by blank lines, which the
  file shows (read).
- **Round 2's yellow 2.** Executed in a temporary repository: `--map
  legacy=<checkout>` names `legacy/src/x.ts#"<a line of the unit>"`,
  `--default-repo` names `src/x.ts#"…"` (there `raw_path` and `rel` are the
  same), and `test_a_mapped_row_is_told_its_own_path` covers `--migrate`'s
  `raw` (slice passed). `read_citation` passes the citation's path, and the
  heading refusal never prints a path (read).
- **Round 2's yellow 3.** The three `Corrected ·` rows exist (fragment rows
  19, 20 and 21). Row 20's reading holds: a bare symbol outside `.py`,
  `.pyi` and `.md` is refused before the repo-wide scan, and `file_units`
  yields nothing there (read). Row 21's holds: "unsure" occurs nowhere in the
  checker (executed grep, 0). Row 19 is ⬜ 5. `survivor-check` with this
  item's `survivors.md` exits 0 and excuses all 36 places, and without it
  exits 1. `correction-check` exits 0. `--strict` over this item's fragment
  reads 185 ok (all executed).
- **Round 2's findings 4, 5 and 6.** The gone-line sentence prints, and
  under `--map` it prints after the row's own path (executed). The changelog
  names the multi-line `.pyi` stub (read). The overview's quote, "A
  `Corrected ·` row supersedes the family of the row it cites, whose
  coordinates are not checked again, and starts a family of its own", is in
  `docs/the-evidence-ledger.md`, wrapped across lines (executed grep over the
  joined text).

What the smith's account asserted that this round did not re-run: six
mutations red, a slice of 973, and `evidence-check --strict` matching the
release branch. The first two are the smith's own runs. The last is part of
the broad gate.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `statement_at` starts a decorated definition at its `def` line, so a claim on a decorated `def` reads `ok` after the decorator changes, and a claim on a method's decorator hashes the whole class | `skills/evidence-check/scripts/evidence_check.py:963` | open | executed: `lru_cache(maxsize=1)` to `maxsize=None` leaves the claim at 5–6 with hash `19d9baaa`; `@property` in `class C` gives 1–7; `def p(self):` gives 3–4; 7 `.py` claims in this repository, 0 move under the fix |
| 🟡 2 | A new case passes `--checked 2026-10-12`, which the checker refuses wherever today is earlier; CI's ubuntu leg and macOS shard 1 are red at the target on that case alone | `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py:459` | open | read: run 38185027460's job logs at `ec3a2de2`, `1 failed, 12996 passed` and `1 failed, 6262 passed`, both this case, "later than today, 2026-10-11" |
| ⬜ 3 | `statement_at` widens an `except` or `case` header, and a comment line, to the whole enclosing statement or function | `skills/evidence-check/scripts/evidence_check.py:961` | open | executed: `except ValueError:` gives 2–7, `case 1:` 2–6, a comment line 1–5; widening reads `DRIFTED`, never `ok` |
| ⬜ 4 | The gone-line sentence on a markdown heading path whose headings are both in the file says the quoted text is not there and to quote the line | `skills/evidence-check/scripts/evidence_check.py:1860` | open | executed: `doc.md#"## A / ### B"` after `### B` moved under `## C` |
| ⬜ 5 | Correction: fragment row 19 says a claim row's tie stands; `judge` breaks it where exactly one place holds the claim | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:19` | open | executed: a one-hit claim tie in `v.md` reads `1 ok`, exit 0; read: `evidence_check.py:1828` |
| ⬜ 6 | Correction: the changelog says a claim row moves where its claim grew; a `.py` continuation or comment line and a bare minor anchor in a file no parser reads also move | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:45` | open | executed: a continuation line gives 2–5; read: the old rule gave 3–3 |
| 🟢 | round 2's yellow 1 is closed in files no parser reads and for every `.py` shape but the decorated definition (🟡 1) and the arm header (⬜ 3) | `skills/evidence-check/scripts/evidence_check.py#minor_region` | confirmed | executed: `f.ts` claims 1–1, 2–2, 4–4; `.py` multi-line expression 2–5, string line 2–4; slice 46 passed |
| 🟢 | round 2's yellow 2 is closed: the remedy names the row's own path under `--map`, `--default-repo` and `--migrate` | `skills/evidence-check/scripts/evidence_check.py#judge` | confirmed | executed: `legacy/src/x.ts#"…"` under `--map`, `src/x.ts#"…"` under `--default-repo`; the `--migrate` case passes |
| 🟢 | round 2's yellow 3 is closed: three `Corrected ·` rows for 0.4.0's lines 20, 58 and 66, and the range row names what answers each place | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:20` | confirmed | executed: `survivor-check` with the exemption exit 0, 36 excused; `correction-check` exit 0; fragment `--strict` 185 ok; rows 20 and 21 read true; row 19's clause is ⬜ 5 |
| 🟢 | round 2's finding 4 is closed: a gone quoted line says to quote it as it reads now | `skills/evidence-check/scripts/evidence_check.py#judge` | confirmed | executed: under `--map` too; the heading-path wording is ⬜ 4 |
| 🟢 | round 2's finding 5 is closed: the installer paragraph names the multi-line `.pyi` stub | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:43` | confirmed | read; the claim condition is ⬜ 6 |
| 🟢 | round 2's finding 6 is closed: the overview grounds the 0.19.0 corrections on the supersede rule | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/overview.md:33` | confirmed | executed: the quoted sentence is in `docs/the-evidence-ledger.md` |
| ❓ | The full suite, the repository-wide lint and typecheck, and `--strict` over every ledger | `seal/` | ❓ out of verified scope | the broad gate; the sealer answers it once the rounds settle |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the eight guard modules the spawn named, in the clone at the target SHA | exit 0, 437 passed |
| `bin/test tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` | exit 0, 46 passed (local date 2026-10-12) |
| A probe loading the target checker: `minor_region` over a decorated function, a class with a decorated method, a multi-line call, a `match`, a `try`, a comment line, a string line and a quoted `.py` major; then a temporary repository for `--map`, `--default-repo`, a heading path that moved, and claim ties; run once and deleted | decorator edit: 5–6 before and after, same hash; `@property` 1–7; `def p` 3–4; call 2–5 from either line; `case` 2–6; `except` 2–7; comment 1–5; string 2–4; quoted major 1–1; `--map` and `--default-repo` paths right; heading path: the gone-line sentence; one-hit claim tie `1 ok` exit 0 |
| A probe over every ledger: each resolving `.py` quoted claim's region now and under a decorator-aware `statement_at`; run once and deleted | 7 claims, 0 differ |
| `bin/evidence-check --strict` narrowed to this item's fragment | exit 0, 185 ok |
| `bin/survivor-check --range origin/release/v0.21.0...HEAD`, without and with this item's `survivors.md` | exit 1, 36 places; with the exemption exit 0, 36 excused |
| `bin/correction-check --range origin/release/v0.21.0...HEAD` | exit 0; no marker dropped; no released ledger file changed |
| `gh pr checks 889`, then the two failed jobs' logs through the jobs API | ubuntu and macOS shard 1 fail on 🟡 2's case alone; lint, ledger, arm-check and release pass; Windows and macOS shards 2–3 pending |
| The full suite, the repository-wide lint and typecheck, and `--strict` over every ledger | not yet, and not this round's: the sealer runs them once after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Declaration shapes the opener never matched (#888) | #888, already deferred in round 1; moot now that the opener has left the tree | the repository owner, who may close #888 as moot |

## Regression tests to plant

- `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`: a claim on a
  decorated definition holds its decorators (🟡 1). It is red at the target,
  where `def p(self):` gives 3–4 and `@property` gives 1–7.

## Facts for the evidence ledger

- Row U9 (`seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:22`)
  cites `statement_at` and reads `DRIFTED` once 🟡 1's fix lands. Its claim
  can name the decorators.
- Row 19's clause about a claim's tie needs ⬜ 5's narrowing. Its Verified
  cell should hold the smith's own reading.

## Paste-ready fixes

### 🟡 1

```python
def statement_at(text, region, line):
    """`(start, end)` of the innermost statement `ast` gives that holds LINE
    inside REGION, or `(line, line)` where none does (round 2 of #870).

    A decorated definition starts at its first decorator, as `parsed_spans`
    reads it: `ast` keeps the decorators inside the definition's node and
    puts its `lineno` on the `def` line, and a decorator carries behaviour
    (round 3 of #870).
    """
    lo, hi = region
    best = (line, line)
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return best
    size = None
    for node in ast.walk(tree):
        if not isinstance(node, ast.stmt):
            continue
        a, b = node.lineno, node.end_lineno or node.lineno
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            a = min([a] + [d.lineno for d in node.decorator_list])
        if lo <= a <= line <= b <= hi and (size is None or b - a < size):
            best, size = (a, b), b - a
    return best
```

```python
DECORATED = (
    "class C:\n"
    "    @property\n"
    "    def p(self):\n"
    "        return 1\n"
    "\n"
    "    def q(self):\n"
    "        return 2\n"
)


def test_a_claim_on_a_decorated_definition_holds_its_decorators():
    """Round 3's yellow 1. `ast` puts a decorated definition's `lineno` on
    its `def` line, so a claim there left the decorator out and read `ok`
    after it changed, and a claim on the decorator hashed the whole class."""
    (region,) = ec.resolve_unit("c.py", "C", DECORATED).places
    assert region == (1, 7)
    assert ec.minor_region("c.py", DECORATED, region, '"def p(self):"') == [(2, 4)]
    assert ec.minor_region("c.py", DECORATED, region, '"@property"') == [(2, 4)]
```

```markdown
| a minor anchor | in `.py`, the statement it names — for a quoted line, the innermost statement `ast` gives that holds it, a definition's decorators included; in a file no parser reads, the line it quotes and nothing below it; in markdown, the quoted line and the lines deeper than it, capped so a claim cannot quietly grow to a whole unit |
```

### 🟡 2

```python
    fill = ["--reverify", "--checked", "2026-10-08", "--ledger", ledger, "."]
```

Needs a fix: yes — 🟡 1 (a claim on a decorated definition leaves its
decorators out), 🟡 2 (a new case dated 2026-10-12 holds CI red wherever
today is earlier)
Loses a record or crashes: no

## Proof block

Opened at the target SHA, in the clone:
`skills/evidence-check/scripts/evidence_check.py` (lines 455–545, 585–1020,
1255–1300, 1739–1890, 2330–2380, 2825–2915);
`skills/evidence-check/SKILL.md` (the diff, line 398);
`tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` (1–80, the
diff, lines 157, 383, 459);
`docs/the-evidence-ledger.md` (30–40, 147–163, and a grep over the joined
text);
`seal/releases/0.4.0.md` (lines 18–20, 56–67);
`seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md`
(rows 9–11, 19–22, 29, 42–47);
`seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/`
`rounds/round-2.md`, `rounds/round-2-fixes.md`, `rounds/round-2-report.md`,
and the diffs of `changelog.md`, `survivors.md` and `overview.md`;
the job logs of run 38185027460 for the ubuntu leg and macOS shard 1.
