# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — review round 3

| Field | Value |
|---|---|
| Target SHA | ec3a2de22639aafb5e5fe5ed860dbe9f0a0f9b16 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 889 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `d9757eb8bb8c6ac066512b3e916d10f1f41d323b..d9757eb8bb8c6ac066512b3e916d10f1f41d323b`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | first — 🟡 1 at skills/evidence-check/scripts/evidence_check.py#statement_at, a unit round-2's fixes added; 🟡 2 at tests/test_a_unit_the_extractor_cannot_bound_is_refused.py#test_a_claim_row_in_python_drifts_on_an_edit_inside_its_statement, a unit round-2's fixes added |
| Needs a fix | yes — 🟡 1 (a claim on a decorated definition leaves its decorators out), 🟡 2 (a new case dated 2026-10-12 holds CI red wherever today is earlier) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 3 of round 2's fixes: 4ed965ed..9f36b62c plus the table and the close at ec3a2de2. The job was the answers to round 2's six verdicts; statement_at and resolve_unit's new shown argument were a finding surface. The spawn named four things to judge. First, whether anything still predicts a unit's extent outside ast and the heading rule. Second, whether statement_at gives the parser's answer in every .py shape. Third, whether the shown path is right under --map and --default-repo. Fourth, whether the three 0.4.0 corrections are true. It also ran the eight guard modules once. Facts arrived labelled. Read: the orchestrator's direction for round 2's 🟡 1. Read from the smith: the 7-and-3 .py count, the remedies, six mutations and the module runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `statement_at` starts a decorated definition at its `def` line, so a claim on a decorated `def` reads `ok` after the decorator changes, and a claim on a method's decorator hashes the whole class | `skills/evidence-check/scripts/evidence_check.py:963` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; executed: `lru_cache(maxsize=1)` to `maxsize=None` leaves the claim at 5–6 with hash `19d9baaa`; `@property` in `class C` gives 1–7; `def p(self):` gives 3–4; 7 `.py` claims in this repository, 0 move under the fix |
| 🟡 2 | A new case passes `--checked 2026-10-12`, which the checker refuses wherever today is earlier; CI's ubuntu leg and macOS shard 1 are red at the target on that case alone | `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py:459` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; read: run 38185027460's job logs at `ec3a2de2`, `1 failed, 12996 passed` and `1 failed, 6262 passed`, both this case, "later than today, 2026-10-11" |
| ⬜ 3 | `statement_at` widens an `except` or `case` header, and a comment line, to the whole enclosing statement or function | `skills/evidence-check/scripts/evidence_check.py:961` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; executed: `except ValueError:` gives 2–7, `case 1:` 2–6, a comment line 1–5; widening reads `DRIFTED`, never `ok` |
| ⬜ 4 | The gone-line sentence on a markdown heading path whose headings are both in the file says the quoted text is not there and to quote the line | `skills/evidence-check/scripts/evidence_check.py:1860` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; executed: `doc.md#"## A / ### B"` after `### B` moved under `## C` |
| ⬜ 5 | Correction: fragment row 19 says a claim row's tie stands; `judge` breaks it where exactly one place holds the claim | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:19` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; executed: a one-hit claim tie in `v.md` reads `1 ok`, exit 0; read: `evidence_check.py:1828` |
| ⬜ 6 | Correction: the changelog says a claim row moves where its claim grew; a `.py` continuation or comment line and a bare minor anchor in a file no parser reads also move | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:45` | deferred #892 | #892 — the run ended at this record on its reopening bound; carried to #892 with round 3's paste-ready fix; executed: a continuation line gives 2–5; read: the old rule gave 3–3 |
| 🟢 | round 2's yellow 1 is closed in files no parser reads and for every `.py` shape but the decorated definition (🟡 1) and the arm header (⬜ 3) | `skills/evidence-check/scripts/evidence_check.py#minor_region` | confirmed | executed: `f.ts` claims 1–1, 2–2, 4–4; `.py` multi-line expression 2–5, string line 2–4; slice 46 passed |
| 🟢 | round 2's yellow 2 is closed: the remedy names the row's own path under `--map`, `--default-repo` and `--migrate` | `skills/evidence-check/scripts/evidence_check.py#judge` | confirmed | executed: `legacy/src/x.ts#"…"` under `--map`, `src/x.ts#"…"` under `--default-repo`; the `--migrate` case passes |
| 🟢 | round 2's yellow 3 is closed: three `Corrected ·` rows for 0.4.0's lines 20, 58 and 66, and the range row names what answers each place | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:20` | confirmed | executed: `survivor-check` with the exemption exit 0, 36 excused; `correction-check` exit 0; fragment `--strict` 185 ok; rows 20 and 21 read true; row 19's clause is ⬜ 5 |
| 🟢 | round 2's finding 4 is closed: a gone quoted line says to quote it as it reads now | `skills/evidence-check/scripts/evidence_check.py#judge` | confirmed | executed: under `--map` too; the heading-path wording is ⬜ 4 |
| 🟢 | round 2's finding 5 is closed: the installer paragraph names the multi-line `.pyi` stub | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:43` | confirmed | read; the claim condition is ⬜ 6 |
| 🟢 | round 2's finding 6 is closed: the overview grounds the 0.19.0 corrections on the supersede rule | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/overview.md:33` | confirmed | executed: the quoted sentence is in `docs/the-evidence-ledger.md` |
| ❓ | The full suite, the repository-wide lint and typecheck, and `--strict` over every ledger | `seal/` | ❓ out of verified scope | the broad gate; the sealer answers it once the rounds settle |

## Paste-ready fixes

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
```python
    fill = ["--reverify", "--checked", "2026-10-08", "--ledger", ledger, "."]
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/evidence-check/scripts/evidence_check.py:1137` | round 1's 🟡 1 — deferred |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:1194` | round 1's 🟡 2 — deferred |
| round-1 | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:36` | round 1's 🟡 3 — deferred |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:1348` | round 1's ⬜ 4 — deferred |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:3476` | round 1's ⬜ 5 — deferred |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:686` | round 1's ⬜ 6 — deferred |
| round-1 | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/questions.md` | round 1's ❓ — out of verified scope |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:898` | round 2's 🟡 1 — fixed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:1778` | round 2's 🟡 2 — fixed |
| round-2 | `seal/releases/0.4.0.md:58` | round 2's 🟡 3 — answered |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:1804` | round 2's ⬜ 4 — fixed |
| round-2 | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:39` | round 2's ⬜ 5 — fixed |
| round-2 | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/overview.md:33` | round 2's ⬜ 6 — answered |
| round-2 | `skills/evidence-check/scripts/evidence_check.py` | round 2's 🟢 — answered |
| round-2 | `skills/evidence-check/scripts/evidence_check.py#bounding_rule` | round 2's 🟢 — answered |
| round-2 | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:27` | round 2's 🟢 — answered |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:2860` | round 2's 🟢 — answered |
| round-2 | `skills/evidence-check/scripts/evidence_check.py#text_regions` | round 2's 🟢 — confirmed |
| round-2 | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:13` | round 2's 🟢 — confirmed |
| round-2 | `seal/` | round 2's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Declaration shapes the opener never matched (#888) | #888, already deferred in round 1; moot now that the opener has left the tree | the repository owner, who may close #888 as moot |
