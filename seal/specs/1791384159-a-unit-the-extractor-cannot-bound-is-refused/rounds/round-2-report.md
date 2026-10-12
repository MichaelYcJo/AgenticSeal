# 1791384159 — review round 2 report

Round 2 of work item 1791384159 (#870, #848), draft PR #889, at
`9f1ede6174477bc70cfc2fa81790ab04a13986bc`. This is the redesign's first
finding round. The target is `68127936..9f1ede61`, phases 5 to 8. The merge of
`origin/release/v0.21.0` at `ad447367` (1e05daa3) sits inside that range, so
the redesign's own change was read as `1e05daa3..9f1ede61`. All execution ran
in a `git clone --no-local` of the worktree at the target SHA. In that clone
`origin/release/v0.21.0` was pointed at `ad447367`, the merge point the spawn
named, because the source worktree carries no such ref.

## How the findings relate

The redesign removes every rule that bounded a unit by imitating a grammar. Three
things did not come along with it:

1. **One guess is still running, one level down.** A quoted claim (`>"…"`) is
   still bounded by indentation in every file. #848's shape comes back through
   a claim on the signature line (🟡 1).
2. **The remedy line is wrong for one kind of row.** The refusal writes the
   quoted-line shape on the path relative to the mapped checkout. A `--map` row
   copied from it then cites the root repository (🟡 2).
3. **Three released claims about the removed rule still read `ok`.** Their
   coordinates point at a unit the diff did not change. Two of them are among
   the 37 places the survivors range row excuses, on a ground that is false
   for them (🟡 3).

Then three smaller items: a reworded quoted line that gives no hint (⬜ 4), an
installer paragraph that names one `.pyi` change out of two (⬜ 5), and a
mis-cited rule in `overview.md` (⬜ 6). Round 1's six findings are all
answered or moot.

## A quoted claim is still bounded by indentation, so #848 returns through a claim (🟡 1)

`minor_region` sends every quoted claim to `literal_statements`
(`skills/evidence-check/scripts/evidence_check.py:877`). From line 898 that
function grows the claim from the quoted line down through every line indented
deeper, up to `CLAIM_CAP` lines. In TypeScript, Go or YAML, indentation is
formatting. This is the indentation rule the redesign deleted at the major
level, still running at the minor level.

Executed against the target, with #848's function in `f.ts`:

- `resolve_unit("f.ts", '"export function multiLine("', …)` gives 1–5, as S1
  claims.
- `minor_region` with the claim `>"export function multiLine("` gives 1–2.
  The `): number {` line is back at column 0, so the claim stops there.
- After the body is rewritten (`opts.a + 1` to `opts.a * 2`), the claim still
  gives 1–2.
- A ledger row `src/f.ts#"export function multiLine(">"export function multiLine("@…`,
  stamped by `--reverify`, reads `ok` under `--strict` after that body rewrite.
  The row without the claim reads `DRIFTED`.

Why it matters: the redesign's own documents say no span is guessed any more.
`docs/the-evidence-ledger.md` says a quoted line's region is "the paragraph it
sits in, which the file itself shows and no grammar decides". The skill's region
table (`skills/evidence-check/SKILL.md:398`) says a minor anchor is "the
statement it names". In a file no parser reads, nothing names a statement. The
lines come from an indentation guess, and that guess read `ok` over a body it
left out. That is #848 again.

The same growth runs in `.py` too: a claim on a black-formatted `def f(` whose
`):` sits at column 0 gives 1–2 and leaves the body out (executed). There a
parser exists, so the innermost `ast` statement holding the line is the honest
bound. That half needs a count of this repository's `.py` claim rows before it
changes any hash. The block below covers the files no parser reads.

Cost of the fix, measured over `seal/ledger.md`, `seal/releases/*.md` and
`seal/ledger/*.md`: 1,259 claims sit in non-`.py` files. Every one is in `.md`
and none grows past its quoted line, so no row in this repository changes. An
installer's rows that pair a quoted major with a quoted claim in such a file
read `DRIFTED` once, and the installer paragraph should say so.

## The refusal's remedy drops a `--map` prefix, so a copied row cites the wrong repository (🟡 2)

`judge` resolves a row through `place`, which strips a `--map` prefix and
returns `rel` relative to the mapped checkout. `resolve_unit(rel, …)` then
builds the refusal with `unbounded(rel, …)`
(`skills/evidence-check/scripts/evidence_check.py:1772` and `:1778`), so the
shape is written on `rel`, not on the row's own path. `--migrate` does the
same at `:2860`.

Executed in a temporary repository with `--map legacy=<checkout>`:

```
BROKEN   legacy/src/x.ts#multiLine  no bounding rule for `.ts`; anchor a quoted line instead: `src/x.ts#"<a line of the unit>"@00000000`, ...
LEFT  legacy/src/x.ts:1-5  no bounding rule for `.ts`; anchor a quoted line instead: `src/x.ts#"<a line of the unit>"@00000000`, ...
```

Why it matters: the line is meant to be the edit, written out (`overview.md`
divergence row 4, "the row's own path"). A row copied from it resolves against
the root and no longer against the mapped checkout. A migration is where
`--map` is used, and there the new repository often keeps the old repository's
paths. In that case the copied row hashes the new code and `--reverify` stamps
it `ok`: the evidence silently moves to the other repository. The rows
affected are exactly the ones this release turns `BROKEN`, cross-repo citations
of TypeScript, Java or Go originals, so it hits the population the redesign
most affects. Rows placed through `--default-repo` are unprefixed and are
not affected.

## Three released claims about the removed rule read `ok`, and the range row excuses two (🟡 3)

The frame enumerated two released rows whose claims described the text rule
(`spec.md` *In* 8): 0.4.0's "The declaration rule reports how sure it is" and
"`--migrate` answers an unsure place". The build corrected those, H1, and four
0.19.0 corrections, and the policy for that repair holds (see the 🟢 row
below). Three more members of the same class have no `Corrected ·` row:

| Released row | Claim | Why it no longer holds |
|---|---|---|
| `seal/releases/0.4.0.md:20` | the row's own hash decides a tie "AND whether an unsure place is still the row's unit"; Verified: two C# overloads resolve by hash, "a lone resurrected place … is BROKEN with the repo-wide scan" | no place is unsure any more, and a bare `.cs` symbol is refused before any tie |
| `seal/releases/0.4.0.md:58` | "A unit that moved out of any non-`.py` file, leaving a call behind, is BROKEN with its destination named"; Verified: `src/app.js` and `src/app.kt` report `identical content at …#render (moved?)` and `--reverify` re-anchors | a bare symbol in any such file is refused before the scan, `file_units` yields nothing there, and `--reverify` writes nothing |
| `seal/releases/0.4.0.md:66` | "A place the declaration rule is unsure of is named with the hash to record" | the rule and its unsure places are gone |

Each family's newest reading is a `Re-read ·` row in `seal/releases/0.19.0.md`
(lines 198, 201 and 203). All three cite
`skills/evidence-check/scripts/evidence_check.py#classify@39108e80`, and
`classify` still hashes `39108e80` at the target (executed). So the narrowed
`--strict` over `0.4.0.md` and `0.19.0.md` reads all three `ok`. The build
read only the rows `--strict` called drifted (`overview.md`, *verified*:
"Read — each drifted released row's claim"). A claim whose coordinate is
unchanged while the behaviour it describes left with another unit never
drifts, and so it was never read.

The survivors file shows the same gap. Running `survivor-check` without the
exemption names `seal/releases/0.4.0.md:20` and `:66` among its 37 places. The
range row's ground (2) excuses them as "released ledger rows … whose families
this item's fragment corrects or re-reads". For these two families that is not
true: no row in the fragment cites either one. So the one `| Range |` row
hides two live false sentences. The other 35 places match the kinds the row
lists (fixture strings, other work items' records, the three true sentences,
`.test_durations`, and released rows whose families are corrected).

Why it matters: the ledger is what this repository holds the tree to. After the
fold, three rows will state behaviour the tree does not have, under a verdict
that says somebody re-read them. The repair already exists and this work item
uses it: a `Corrected ·` row, with the citation alone where the claim went with
its code.

## Smaller items (⬜)

- **⬜ 4, a reworded quoted line gives no hint.** In a file no parser reads,
  `file_units` yields nothing, so a quoted locator that stopped matching reads
  `BROKEN … locator not found` and nothing else
  (`skills/evidence-check/scripts/evidence_check.py:1804`). Executed: Prettier
  joining #848's signature onto one line gives `Resolution([], refused=None)`.
  This is the cost the frame states and the skill's *Known limits* records. But
  it is the commonest `BROKEN` an installer will meet after this release, and it
  is the one line that names no remedy.
- **⬜ 5, the installer paragraph names one `.pyi` change of two.**
  `changelog.md:39` says a decorated `.pyi` stub reads `DRIFTED` once. A
  multi-line stub signature does too. Executed against `ad447367`'s checker: the
  old rule gave 1–3 for `def f(\n    x: int,\n    y: int,\n) -> int: ...` and
  `ast` gives 1–4. That is #848's own shape, fixed for `.pyi`. The paragraph
  promises nothing false, since it keeps verdicts only for `.py` and `.md`, but
  it leaves this kind out.
- **⬜ 6, the overview cites the wrong rule.** `overview.md:33` justifies
  retiring the four 0.19.0 corrections with "Once both have folded, a
  `Corrected ·` row citing one of them retires it". That sentence is about a
  released row corrected twice. The rule that licenses the act is the one
  before it: a `Corrected ·` row "supersedes the family of the row it cites …
  and starts a family of its own", and a released `Corrected ·` row is such a
  family. The act is right and the cited ground is not.

## What was checked and holds

- **Nothing guessing is left at the major level.** None of the names *In* 5
  lists is defined or mentioned in the checker (executed grep, each 0).
  "bracket walk", "declaration rule", "how sure it is" and "resurrect" are
  absent from the skill, the policy document and `rider_check.py`. The one
  "block rule" in `rider_check.py:322` is the comment-block rule, not YAML's.
  `rider_check.py`'s comment-block reading is a format this plugin owns.
- **#848 drifts under the paragraph rule.** Executed: the signature quote
  hashes 1–5, and a body edit reads `DRIFTED` under `--strict`. A blank line
  splits the unit where the frame says: `g.ts` gives 1–4 and 6–7. Two adjacent
  functions with no blank line between them (normal Go and C output) are one
  paragraph, 1–6. That means extra `DRIFTED`, not silence.
- **What a formatter does to a quoted row.** This is read from the code; the
  formatters themselves were not run. A line matches with its whitespace
  normalised, so reindenting and gofmt's column alignment still find the line.
  The hash keeps interior and leading whitespace (`normalise`), so either one
  reads `DRIFTED`. Prettier rewrapping a signature changes the quoted line
  itself, which gives ⬜ 4's `BROKEN`. Removing a blank line at the start of a
  block merges paragraphs, which reads `DRIFTED`. No reformat produces `ok`
  over a change.
- **The refusal names an act.** The no-rule sentence carries the shape, and
  `--reverify` fills `@00000000` (executed: `00000000 -> 4e8a57af`, and the row
  reads `ok`). The Python sentence names the interpreter. The markdown sentence
  names `"## <heading>"`. The exception is 🟡 2.
- **The released `Corrected ·` rows follow the policy.** Three of the four
  0.19.0 corrections keep the claim and re-point a coordinate whose case was
  deleted or re-fixtured. That is the policy's repair for a moved anchor ("a
  `Corrected ·` row re-points it"). The fourth, and 0.4.0's two, drop clauses
  that went with the code and hold the citation alone where nothing is left.
  `correction-check` over the range exits 0 (executed). The narrowed
  `--strict` over the fragment reads 167 ok and nothing else (executed).
- **The YAML rows.** No bare non-parser coordinate stands outside a family a
  `Corrected ·` row supersedes. The narrowed `--strict` over 0.15.5, 0.18.0,
  0.18.1, 0.20.0, #864's and #869's fragments reads 0 broken. Its 11 drifted are
  the release branch's own `templates/config.md`, `OUT_OF_CLASS` and
  `agents/warden.md` rows (executed). `"ledger:"`'s paragraph does start at the
  job comment on line 147, as divergence row 7 says (read).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A quoted claim is bounded by an indentation guess in every file: a claim on #848's signature line hashes 1–2, and a body rewrite reads `ok` | `skills/evidence-check/scripts/evidence_check.py:898` | open | executed: `minor_region` gives 1–2 before and after the body edit; a stamped claim row reads `ok` under `--strict` after it while the unclaimed row reads `DRIFTED`; the same growth in `.py` gives 1–2 for a black `def f(` |
| 🟡 2 | The refusal's quoted-line shape, and `--migrate`'s left reason, are written on the path inside a `--map` checkout, so a row copied from them cites the root repository | `skills/evidence-check/scripts/evidence_check.py:1778` | open | executed with `--map legacy=…`: `legacy/src/x.ts#multiLine` is told to write `src/x.ts#"…"`, and so is `legacy/src/x.ts:1-5` under `--migrate` (`:2860`) |
| 🟡 3 | Three released claims the redesign falsified read `ok` with no `Corrected ·` row (0.4.0 lines 20, 58, 66), and the survivors range row excuses two of them on a ground that is false for them | `seal/releases/0.4.0.md:58` | open | executed: `classify` hashes `39108e80` at the target, the narrowed `--strict` reads the three families `ok`, and `survivor-check` without the exemption names `0.4.0.md:20` and `:66`; read: no fragment row cites them |
| ⬜ 4 | A reworded quoted line in a file no parser reads is `BROKEN` with "locator not found" and no remedy | `skills/evidence-check/scripts/evidence_check.py:1804` | open | executed: a Prettier-joined signature resolves to nothing, with `refused=None` |
| ⬜ 5 | The installer paragraph names decorated `.pyi` stubs, while a multi-line stub signature also reads `DRIFTED` once | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:39` | open | executed against `ad447367`'s checker: 1–3 before, 1–4 after |
| ⬜ 6 | The overview grounds retiring the 0.19.0 corrections on the two-corrections sentence instead of the supersede rule | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/overview.md:33` | open | read: `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* |
| 🟢 | Round 1's yellow 1 (the walk ignored the lexer's string and comment state) is moot, because the walk and the lexer left the tree | `skills/evidence-check/scripts/evidence_check.py` | answered | executed: none of *In* 5's names occurs in the module |
| 🟢 | Round 1's yellow 2 (a comment ended a YAML key's compact items) is moot, because the block rule left and a bare YAML key is refused | `skills/evidence-check/scripts/evidence_check.py#bounding_rule` | answered | executed: `.yml` and `.yaml` answer None; the 16 rows are quoted and the narrowed `--strict` reads 0 broken |
| 🟢 | Round 1's yellow 3 (the installer paragraph promised unchanged verdicts) is answered: the paragraph keeps verdicts only for `.py` and `.md`, which holds | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:27` | answered | read against the code; the one omission left is ⬜ 5 |
| 🟢 | Round 1's finding 4 ("declared on line N" for a call) is moot, because its sentence left with `generic_units` | `skills/evidence-check/scripts/evidence_check.py` | answered | executed grep, 0 |
| 🟢 | Round 1's finding 5 (`--migrate` named no remedy) is answered | `skills/evidence-check/scripts/evidence_check.py:2860` | answered | executed: a `.rb` and an unparseable `.py` row are left with the refusal; the prefix defect is 🟡 2 |
| 🟢 | Round 1's finding 6 (unlisted suffixes were refused) is moot, because every suffix outside the two parsers is refused alike | `skills/evidence-check/scripts/evidence_check.py#bounding_rule` | answered | read |
| 🟢 | #848's case drifts under the paragraph rule, and a blank line splits a unit into the paragraphs the frame names | `skills/evidence-check/scripts/evidence_check.py#text_regions` | confirmed | executed: 1–5 and `DRIFTED` after a body edit; `g.ts` 1–4 and 6–7 |
| 🟢 | The `Corrected ·` rows that retire released `Corrected ·` rows follow `docs/the-evidence-ledger.md` | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:13` | confirmed | read: supersede and re-point rules; executed: `correction-check` exit 0, the narrowed `--strict` over the fragment reads 167 ok |
| ❓ | `--strict` over every ledger matching the release branch file by file (33 drifted) | `seal/` | ❓ out of verified scope | not run whole: it is part of the broad gate. The narrowed runs over seven ledger files show only the release branch's own drifts. The sealer answers it |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the eight guard modules the spawn named, in the clone at the target SHA | exit 0, 437 passed |
| A probe loading the target checker: `resolve_unit` and `minor_region` over #848's function, `g.ts`, a Prettier-joined signature, two adjacent Go functions, a black `def f(`; run once and deleted | 1–5; claim 1–2 before and after a body edit; 1–4 and 6–7; nothing, `refused=None`; 1–6; `.py` claim 1–2 |
| The same probe's CLI half, in a temporary repository with `--map legacy=<checkout>`: `--strict`, `--reverify`, a body edit, `--strict`, `--migrate` | the mapped refusal and the `--migrate` left reason both write `src/x.ts#"…"`; `--reverify` fills `@00000000`; after the edit the unclaimed row is `DRIFTED` and the claim row is `ok` |
| A probe resolving five `.pyi` shapes under `ad447367`'s checker and the target's; run once and deleted | multi-line signature 1–3 to 1–4; one-line and constant unchanged; overloads 2–2/4–4 to 1–2/3–4; a class with a multi-line method: nothing to 1–4 |
| `bin/survivor-check --range origin/release/v0.21.0...HEAD`, without and with this item's `survivors.md` | exit 1, 37 places, among them `seal/releases/0.4.0.md:20` and `:66`; with the exemption exit 0, all 37 excused |
| `bin/correction-check --range origin/release/v0.21.0...HEAD` | exit 0; no marker dropped; no released ledger file changed |
| `bin/evidence-check --strict` narrowed to `0.4.0.md` and `0.19.0.md` | exit 2; 914 ok, 2 drifted, both `templates/config.md` (the release branch's own) |
| `bin/evidence-check --strict` narrowed to this item's fragment | exit 0; 167 ok |
| `bin/evidence-check --strict` narrowed to 0.15.5, 0.18.0, 0.18.1, 0.20.0 and #864's and #869's fragments | exit 2; 2312 ok, 11 drifted, 0 broken; every drift is a `templates/config.md`, `OUT_OF_CLASS` or `agents/warden.md` row |
| The hash of `classify` at the target | `39108e80`, the hash 0.19.0's three re-reads record |
| A count of claim rows in non-`.py` files over every ledger, and how many grow past their quoted line | 1,259, all `.md`; none grows |
| The full suite, the repository-wide lint and typecheck, and `--strict` over every ledger | not yet, and not this round's: the sealer runs them once after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Declaration shapes the opener never matched (#888) | #888, already deferred in round 1; moot now that the opener has left the tree | the repository owner, who may close #888 as moot |

## Regression tests to plant

- `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`: a quoted claim
  in a file no parser reads is its own line (🟡 1). The case is red at the
  target, where `minor_region` gives 1–2.
- The same module: a `--map` row's refusal and `--migrate` reason carry the
  row's own path, prefix included (🟡 2). It is red at the target, where both
  print `src/x.ts`.

## Facts for the evidence ledger

- 0.4.0's rows at lines 20, 58 and 66 each take a `Corrected ·` row in
  `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md`.
  Each `Verified behavior` cell must hold the smith's own reading, not this
  report's.

## Paste-ready fixes

### 🟡 1

```python
def minor_region(path, text, region, minor):
    """[(start, end)] inside `region`, or [] when the minor anchor is stale.

    **An empty answer is not BROKEN.** The minor level narrows what is hashed;
    it never decides whether the row resolves. A minor anchor that stopped
    matching means that place changed, and *it changed, go re-read* is the
    honest report — so the caller widens to the major unit and says DRIFTED.
    Reporting BROKEN here would send somebody to edit the ledger, which is the
    bookkeeping this design exists to remove.

    Ambiguity widens for the same reason: several matches is not a place.

    **In a file no parser reads, a quoted claim is the line it quotes**
    (round 2 of #870). Growing it by indentation is the rule #870 removed at
    the major level, and it ended a claim on #848's signature line before the
    body, so a rewrite of the body read `ok`.
    """
    lines = gfm_lines(text)
    rule = bounding_rule(path)
    if minor.startswith('"'):
        found = literal_statements(lines, region, unescape(minor[1:-1]))
        if rule is None:
            found = [(a, a) for a, _b in found]
    elif rule == "ast":
        found = name_statements(text, region, minor)
    else:
        found = literal_statements(lines, region, minor)
    return found if len(found) == 1 else []
```

```python
def test_a_claim_in_a_file_no_parser_reads_is_its_line():
    """A quoted claim was grown by indentation in every file, so a claim on
    #848's signature line hashed lines 1-2 and a body rewrite read `ok`."""
    text = (
        "export function multiLine(\n  opts: { a: number },\n): number {\n"
        "  return opts.a + 1;\n}\n"
    )
    region = ec.resolve_unit("f.ts", '"export function multiLine("', text).places[0]
    assert region == (1, 5)
    claim = '"export function multiLine("'
    assert ec.minor_region("f.ts", text, region, claim) == [(1, 1)]
```

```markdown
| a minor anchor | the statement it names, capped so a claim cannot quietly grow to a whole unit; in a file no parser reads, the line it quotes |
```

### 🟡 2

```python
    unit = resolve_unit(rel, locator, body)
    if unit.refused:
        # Before the repo-wide scan, because a refused unit was never found
        # and so cannot have moved: no unit in a file of this kind is
        # bounded, and a hint pointing elsewhere would send the reader past
        # the one fix that works — the anchor the line names (#870). The
        # shape is written on the row's own path: a `--map` prefix dropped
        # from it re-points the copied row at ROOT (round 2 of #870).
        return found("BROKEN", unbounded(raw_path, bounding_rule(rel), body))
```

```python
                rule = bounding_rule(rel)
                if rule is None or (rule == "ast" and py_spans(body) is None):
                    # No unit here is bounded, so none can contain the range;
                    # the reason a person reads is the refusal, which names
                    # the anchor to write instead, on the row's own path
                    # (#870, round 1's finding 5, round 2's yellow 2).
                    left.append((m.group(0), unbounded(raw, rule, body)))
                    failed = True
                    continue
```

```python
def test_a_mapped_row_is_told_its_own_path(repo, tmp_path):
    """The shape is the edit to make, so it carries the `--map` prefix: written
    on the path inside the mapped checkout, the copied row cites ROOT."""
    other = tmp_path / "orig"
    (other / "src").mkdir(parents=True)
    (other / "src" / "x.ts").write_text("export function f() {\n}\n", encoding="utf-8")
    cite(repo, "legacy/src/x.ts#f@00000000")
    r = run(["--strict", "--map", f"legacy={other}", "."], str(repo))
    assert no_rule("legacy/src/x.ts", "`.ts`") in r.stdout, r.stdout
    ledger = repo / "seal" / "ledger" / "f.md"
    ledger.write_text("| C1 | `legacy/src/x.ts:1-2` | read | 2026-09-01 | n |\n", encoding="utf-8")
    _migrated, left, _unproven = ec.migrate([str(ledger)], str(repo), {"legacy": str(other)})
    assert dict(left)["legacy/src/x.ts:1-2"] == no_rule("legacy/src/x.ts", "`.ts`"), left
```

### 🟡 3

```markdown
| Corrected · The row's own recorded hash decides a tie between places, at the major level only; a claim row's tie stands, because two unrelated units can share one identical line | `seal/releases/0.4.0.md#"#### A coordinate names content, not a position">"The row's own recorded"@dbcd3bf8`, `skills/evidence-check/scripts/evidence_check.py#judge@a5c83de3` | **Read** 2026-10-12: `judge`'s tie branch keeps the place whose content reconstructs the row's hash, and a claim's tie stands | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the clause about an unsure place, and the C# overloads and resurrected place in its evidence, went with the declaration rule (#870) |
| Corrected · A unit that moved out of any non-`.py` file, leaving a call behind, is BROKEN with its destination named | `seal/releases/0.4.0.md#"#### What round 6's fixes hold">"A unit that moved"@b5de663d` | **Read** 2026-10-12: a bare symbol outside `.py`, `.pyi` and `.md` is refused before the repo-wide scan, and no such file yields units (`phases/phase-5.md`) | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the claim went with its code, so the grounds hold the citation alone |
| Corrected · A place the declaration rule is unsure of is named with the hash to record | `seal/releases/0.4.0.md#"#### What round 7's fixes hold">"A place the declaration"@b5c855c7` | **Read** 2026-10-12: no place is unsure since #870 (`phases/phase-6.md`) | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the claim went with its code, so the grounds hold the citation alone |
```

Needs a fix: yes — 🟡 1 (a quoted claim is still bounded by indentation, which reproduces #848), 🟡 2 (the refusal's shape drops a `--map` prefix), 🟡 3 (three released claims the redesign falsified read `ok`, and the range row hides two)
Loses a record or crashes: no

## Proof block

Opened at the target SHA, in the clone:
`skills/evidence-check/scripts/evidence_check.py` (lines 30–45, 154–196,
425–470, 540–1000, 1224–1264, 1678–1687, 1700–1860, 2800–2870);
`.github/scripts/rider_check.py` (diff, 491–516);
`skills/code-review/scripts/survivor_check.py` (diff, 1895–1935, 2225–2260);
`skills/evidence-check/SKILL.md` (95–135, 390–402, 690–720, 775–800);
`docs/the-evidence-ledger.md` (30–215, and the diff);
`tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` (1–127, 437–492);
`tests/test_a_row_points_by_content.py` (2670–2830);
`seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/`
`rounds/round-1.md`, `overview.md`, `routing.md`, `spec.md`, `changelog.md`,
`survivors.md`;
`seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md`;
`seal/ledger/1791384162-the-macos-test-leg-runs-in-shards.md`;
`seal/releases/0.4.0.md` (lines 18–20, 51, 55–67), `0.19.0.md` (180–204),
`0.9.1.md` (172), `0.20.0.md` (203, 207);
`.github/workflows/test.yml` (145–148, 179–183).
Not opened: #834's `handoff.md` on `origin/chore/834-…`, whose decision this
round takes from `spec.md`'s grounding.
