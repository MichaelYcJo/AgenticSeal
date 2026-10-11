# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — review round 2

| Field | Value |
|---|---|
| Target SHA | 9f1ede6174477bc70cfc2fa81790ab04a13986bc |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 889 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `4ed965ed21a2751a8fb7c3971469df5d0a797802..9f36b62c995358bfb3905a99af2bd02a5ae6b93f`, 5 commits |
| Contract changes | resolve_unit → region_lines, plan.md, post-review-check.md, phase-6.md, round-1-report.md, round-1.md, round-2-report.md, round-2.md, spec.md, removed_ledger_rows, resolve, judge, read_citation, pytest |
| New units | statement_at (depth 1); test_a_claim_in_a_file_no_parser_reads_is_its_line (depth 1); BLACK (depth 1); test_a_claim_in_python_is_the_statement_ast_gives (depth 1); test_a_claim_row_in_python_drifts_on_an_edit_inside_its_statement (depth 1); test_a_mapped_row_is_told_its_own_path (depth 1); test_a_quoted_line_that_is_gone_says_to_quote_it_as_it_reads_now (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (a quoted claim is still bounded by indentation, which reproduces #848), 🟡 2 (the refusal's shape drops a `--map` prefix), 🟡 3 (three released claims the redesign falsified read `ok`, and the range row hides two) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2, the redesign's first finding round after the owner reframed the item on 2026-10-12 against 0.21.0's theme. Its target is 68127936..9f1ede61, phases 5 to 8: two bounding rules, ast and the heading path, with every other bare symbol refused and pointed at a quoted-line anchor whose region is its paragraph; the guessing reader removed; the repository's 16 YAML rows brought to the format; the documents. Round 1's six deferred findings were the agenda. The spawn named seven things to judge: whether anything still predicts a format; the paragraph region on #848's case; quoted-line stability under reformatting; whether every refusal names an actionable remedy; whether the single Range survivors row hides a live sentence; the Corrected rows retiring released Corrected rows; and the reviewer's own axes. It also ran the eight guard modules once. Facts arrived labelled. Read from the smith: the removals, the 16 rows, the --strict findings identical to the release branch, and the module runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | A quoted claim is bounded by an indentation guess in every file: a claim on #848's signature line hashes 1–2, and a body rewrite reads `ok` | `skills/evidence-check/scripts/evidence_check.py:898` | **fixed** `67da739e` | fixed at 67da739e — `minor_region` takes a quoted claim to the innermost statement `ast` gives in `.py` (`statement_at`) and to the quoted line alone in a file no parser reads, as a bare minor anchor there; markdown keeps the literal rule. Counted first: 7 `.py` quoted claims resolve in this repository's ledgers and 3 move (two in `hooks/cmdline.py#walk_directories`, one in `skills/code-review/scripts/chain_check.py#main`), each read and re-read at 76c0c03d. The skill's region row and the changelog fragment state it at 78082c10; executed: `minor_region` gives 1–2 before and after the body edit; a stamped claim row reads `ok` under `--strict` after it while the unclaimed row reads `DRIFTED`; the same growth in `.py` gives 1–2 for a black `def f(` |
| 🟡 2 | The refusal's quoted-line shape, and `--migrate`'s left reason, are written on the path inside a `--map` checkout, so a row copied from them cites the root repository | `skills/evidence-check/scripts/evidence_check.py:1778` | **fixed** `67da739e` | fixed at 67da739e — `resolve_unit` takes `shown`, the row's own path, and `judge` passes `raw_path`; `--migrate` writes the remedy on `raw`; executed with `--map legacy=…`: `legacy/src/x.ts#multiLine` is told to write `src/x.ts#"…"`, and so is `legacy/src/x.ts:1-5` under `--migrate` (`:2860`) |
| 🟡 3 | Three released claims the redesign falsified read `ok` with no `Corrected ·` row (0.4.0 lines 20, 58, 66), and the survivors range row excuses two of them on a ground that is false for them | `seal/releases/0.4.0.md:58` | answered | corrected at 90f39765 (three `Corrected ·` rows for 0.4.0's lines 20, 58 and 66) and 78082c10 (the survivors range row's ground (2) names each released row it excuses and the correction answering it); executed: `classify` hashes `39108e80` at the target, the narrowed `--strict` reads the three families `ok`, and `survivor-check` without the exemption names `0.4.0.md:20` and `:66`; read: no fragment row cites them |
| ⬜ 4 | A reworded quoted line in a file no parser reads is `BROKEN` with "locator not found" and no remedy | `skills/evidence-check/scripts/evidence_check.py:1804` | **fixed** `67da739e` | fixed at 67da739e — a quoted locator that resolves to nothing, with no destination or name found, reads "— the quoted text is not in the file; quote the line as it reads now"; executed: a Prettier-joined signature resolves to nothing, with `refused=None` |
| ⬜ 5 | The installer paragraph names decorated `.pyi` stubs, while a multi-line stub signature also reads `DRIFTED` once | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:39` | **fixed** `78082c10` | fixed at 78082c10 — the installer paragraph names a `.pyi` stub that is decorated or whose signature runs over several lines, and the quoted claims that move; executed against `ad447367`'s checker: 1–3 before, 1–4 after |
| ⬜ 6 | The overview grounds retiring the 0.19.0 corrections on the two-corrections sentence instead of the supersede rule | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/overview.md:33` | answered | corrected at 78082c10: the overview grounds the 0.19.0 corrections on the supersede rule of `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*; read: `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* |
| 🟢 | Round 1's yellow 1 (the walk ignored the lexer's string and comment state) is moot, because the walk and the lexer left the tree | `skills/evidence-check/scripts/evidence_check.py` | answered | executed: none of *In* 5's names occurs in the module |
| 🟢 | Round 1's yellow 2 (a comment ended a YAML key's compact items) is moot, because the block rule left and a bare YAML key is refused | `skills/evidence-check/scripts/evidence_check.py#bounding_rule` | answered | executed: `.yml` and `.yaml` answer None; the 16 rows are quoted and the narrowed `--strict` reads 0 broken |
| 🟢 | Round 1's yellow 3 (the installer paragraph promised unchanged verdicts) is answered: the paragraph keeps verdicts only for `.py` and `.md`, which holds | `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/changelog.md:27` | answered | read against the code; the one omission left is ⬜ 5 |
| 🟢 | Round 1's finding 4 ("declared on line N" for a call) is moot, because its sentence left with `generic_units` | `skills/evidence-check/scripts/evidence_check.py` | answered | executed grep, 0 |
| 🟢 | Round 1's finding 5 (`--migrate` named no remedy) is answered | `skills/evidence-check/scripts/evidence_check.py:2860` | answered | executed: a `.rb` and an unparseable `.py` row are left with the refusal; the prefix defect is 🟡 2 |
| 🟢 | Round 1's finding 6 (unlisted suffixes were refused) is moot, because every suffix outside the two parsers is refused alike | `skills/evidence-check/scripts/evidence_check.py#bounding_rule` | answered | read |
| 🟢 | #848's case drifts under the paragraph rule, and a blank line splits a unit into the paragraphs the frame names | `skills/evidence-check/scripts/evidence_check.py#text_regions` | confirmed | executed: 1–5 and `DRIFTED` after a body edit; `g.ts` 1–4 and 6–7 |
| 🟢 | The `Corrected ·` rows that retire released `Corrected ·` rows follow `docs/the-evidence-ledger.md` | `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md:13` | confirmed | read: supersede and re-point rules; executed: `correction-check` exit 0, the narrowed `--strict` over the fragment reads 167 ok |
| ❓ | `--strict` over every ledger matching the release branch file by file (33 drifted) | `seal/` | ❓ out of verified scope | not run whole: it is part of the broad gate. The narrowed runs over seven ledger files show only the release branch's own drifts. The sealer answers it |

## Paste-ready fixes

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
```markdown
| Corrected · The row's own recorded hash decides a tie between places, at the major level only; a claim row's tie stands, because two unrelated units can share one identical line | `seal/releases/0.4.0.md#"#### A coordinate names content, not a position">"The row's own recorded"@dbcd3bf8`, `skills/evidence-check/scripts/evidence_check.py#judge@a5c83de3` | **Read** 2026-10-12: `judge`'s tie branch keeps the place whose content reconstructs the row's hash, and a claim's tie stands | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the clause about an unsure place, and the C# overloads and resurrected place in its evidence, went with the declaration rule (#870) |
| Corrected · A unit that moved out of any non-`.py` file, leaving a call behind, is BROKEN with its destination named | `seal/releases/0.4.0.md#"#### What round 6's fixes hold">"A unit that moved"@b5de663d` | **Read** 2026-10-12: a bare symbol outside `.py`, `.pyi` and `.md` is refused before the repo-wide scan, and no such file yields units (`phases/phase-5.md`) | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the claim went with its code, so the grounds hold the citation alone |
| Corrected · A place the declaration rule is unsure of is named with the hash to record | `seal/releases/0.4.0.md#"#### What round 7's fixes hold">"A place the declaration"@b5c855c7` | **Read** 2026-10-12: no place is unsure since #870 (`phases/phase-6.md`) | 2026-10-12 | Corrected 2026-10-12 by work item 1791384159-a-unit-the-extractor-cannot-bound-is-refused: the claim went with its code, so the grounds hold the citation alone |
```

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Declaration shapes the opener never matched (#888) | #888, already deferred in round 1; moot now that the opener has left the tree | the repository owner, who may close #888 as moot |
