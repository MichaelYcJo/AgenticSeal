# Feature Specification: a unit the extractor cannot bound is refused (#870, #848)

<!-- seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-evidence-ledger.md` §*A row is a content anchor, and it names no commit* — "the major level is the enclosing unit", "an anchor degrades to `DRIFTED`, never to `BROKEN`. Only the major level can be broken" | A span that leaves a unit's body out is not the enclosing unit. Refusing it is `BROKEN` at the one level `BROKEN` is allowed, and it is never an `ok` read over lines nobody hashed |
| `docs/the-evidence-ledger.md` §*What the checker refuses, and what it says while refusing* | The refusal is a sentence a person reads: why the unit cannot be bounded, and which anchor to write instead |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* — "A BROKEN coordinate. Only where a released row carries it under the freeze does `--reverify` name it, with the `Corrected ·` repair, and exit 1"; "A claim that went with its code is a `Corrected ·` row whose grounds hold the citation alone" | What this repository and an installer with `Ledger frozen from` do with a released row the new rule refuses, and with a released row whose claim described the rule this work removes: both repairs already exist, and this work adds no third |
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | Between a reader of more shapes and a refusal with a remedy on the line, the refusal is the one that never reads `ok` over code nobody re-read |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The stop cost is measured before the change ships (`questions.md` Q2, Q3), and the change names what it removes |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | This work writes `changelog.md` and `seal/ledger/<work-item-id>.md` in its own directory and edits no released file |
| `skills/evidence-check/SKILL.md` §*A coordinate names content, never a position*, §*Resolving a unit without a parser*, §*What the region is*, §*Known limits* | The sentences this work rewrites: the major level comes from "`ast` for `.py`; otherwise the declaration rule below"; the bracket walk, the block rule, and "the rule reports how sure it is rather than being asked to be right" |
| #834's `spec.md` §*What the table says* (`origin/chore/834-every-reader-and-record-is-inventoried:seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md`) — "What converged read an owned format or an observed fact and refused the unknown. What did not converge read someone else's text and let the unknown through" | The direction, and the reason the first frame's build is undone: a lexer over nine language families reads someone else's text |
| #834's `handoff.md` §*Review of the run* and §*What the owner decided* (same branch, `seal/specs/1791382684-…/handoff.md`) | The owner's decision of 2026-10-12 that this reframe carries out: force a format; bound a unit only where a real parser decides its extent; require a quoted-line anchor everywhere else |

## Why this work item was reframed

The build of phases 1–4 (closed at 8ca2b57a) replaced the indentation rule
with a bracket walk over a string, comment and bracket lexer for nine language
families, and round 1 (`rounds/round-1.md`) found three more shapes of the
class the walk was written to end: a regex or template literal that opens a
phantom comment and puts a declaration back under the indentation rule
(#848's shape again), a multi-line string with column-0 content that ends its
constant on the first line, and verdicts the release note promised unchanged
that change. The owner read the run against 0.21.0's theme — a reader
observes, forces a format, or is deleted — and judged the lexer a new guessing
reader, which is a cover-up and not an improvement. Every one of round 1's six
findings is a finding about the walk, the lexer, the block rule or the
sentences describing them, and all six are closed by removing what they are
about: 🟡 1 and 🟡 2 by the lexer and the block rule leaving the tree, 🟡 3 by
the installer paragraph being rewritten (*In* 7), ⬜ 4 by its sentence leaving
with `generic_units`, ⬜ 5 by *In* 4, ⬜ 6 by every suffix outside the two
parsers being refused alike, so no list of them exists to be incomplete.

## Scope

**What is wrong, in one paragraph.** Every file that is not `.py`, `.pyi` or
`.md` is bounded by a rule written from the outside of its language: before
this work item, one indentation rule for everything, which ended a unit at the
first line a formatter put back at the declaration's indent — `): number {`
for every multi-line TypeScript signature Prettier writes (#848, executed: the
span is lines 1–2 of a 5-line function), so a rewrite of the body read `ok`
and `--reverify` could not notice because the hash it would write is the one
already there; after phases 1–4, a bracket walk over a hand-written lexer,
which round 1 showed misreading the same shape through a regex (executed:
#848's function after `const SLASHES = /^\/*/;` resolves to 3–4 of 3–7 under
both the base checker and the walk). A rule that imitates a language's grammar
without that language's parser is right until the next form it does not know,
and silent there. The only readers in this checker that have converged are
the two that read a format the file itself declares — Python's own `ast` and
CommonMark's heading rule (#867) — and the quoted-line anchor, whose region is
the run of non-blank lines around a line the row itself quotes.

**In.**

1. **Two bounding rules, and a format everywhere else.** `bounding_rule`
   answers `"ast"` for `.py` and `.pyi`, `"heading"` for `.md`, and `None` for
   every other suffix and for no suffix. The four units that read it
   (`resolve_unit`, `minor_region`, `file_units`, `content_matches`) keep
   reading it and test no suffix themselves (phase 1's U1, kept). Its rows:

   | Suffix | Rule | Input class (#835's words) | What it refuses |
   |---|---|---|---|
   | `.py`, `.pyi` | `ast` spans, as today | observed — the interpreter's own parse | a file the running interpreter cannot parse: `BROKEN`, naming the interpreter version and the error's line (phase 1's U2, kept) |
   | `.md` | the heading path, read on `markdown_lines` (#867) | owned locator over a person's document | a bare symbol, which names no heading (phase 1, kept) |
   | any other suffix, and no suffix | none | — | every bare symbol: `BROKEN`, "no bounding rule for `.ts`; anchor a quoted line instead", with the shape of the anchor on the line |

2. **The quoted-line anchor is the format, and its region is the paragraph.**
   `path#"<a line of the unit>"` resolves by `text_regions` in every file as
   today: the quoted line matched whole with its whitespace normalised, and
   the region the contiguous run of non-blank lines it sits in. Nothing in the
   rule reads the language. What it means for a unit, stated so a row's author
   can read it off the file:

   - A unit with no blank line inside it is one paragraph, and one quoted line
     anywhere in it hashes the whole unit. #848's function is this case: a row
     citing `f.ts#"export function multiLine("` hashes lines 1–5, and a
     body-only edit reads `DRIFTED` (S1). That is #848 answered by the format:
     the row cites the lines that hold the body, by its own quote.
   - A unit with blank lines inside it is several paragraphs, and a quoted
     line hashes the paragraph it is in. A row whose claim is about one of
     them quotes a line of that one; a row whose claim rests on several quotes
     one line of each, in the same `Code grounds` cell, which already holds
     several coordinates per row. **A quoted line is never a function**, and
     the skill says so where it says what the region is (S2).
   - A quoted line that occurs more than once in the file is ambiguous, and
     the row's recorded hash breaks the tie as it does today (`judge`); where
     none or several hold it, `BROKEN` with the places named, as today.

3. **The refusal names the format.** `unbounded` for a suffix no rule bounds
   keeps "no bounding rule for `<suffix>`; anchor a quoted line instead" and
   adds the shape, so the person reading the line can write the row without
   opening the skill. The exact wording is the work's, and it is pinned by a
   case (§14).

4. **`--migrate` names the remedy where it leaves a row.** An old `path:line`
   row in a file no rule bounds is left, as it is today, and its reason reads
   the refusal sentence of *In* 3 instead of "no single unit contains s-e"
   (round 1's ⬜ 5). Writing a quoted-line anchor for the person is out
   (*Out*).

5. **What this removes.** From `skills/evidence-check/scripts/evidence_check.py`:
   `BRACE_FAMILY`, `BRACE_SUFFIXES`, `BLOCK_SUFFIXES`, `brace_family`, the
   `StringForm` forms, `_literal_at`, `brace_lexed`, `brace_span`,
   `block_span`, `declaration_opener`, `opens_declaration`, `STATEMENT_WORDS`,
   `generic_units`, and the resurrection flag — `Resolution.resurrected`, the
   `resurrected or len(places) > 1` branch of `judge`, the "declaration rule
   is unsure" branches of `--reverify` and `--migrate`, `file_units`' third
   field — because once no text rule exists, no code can set it, and a field
   nothing sets is read by nobody honestly. From
   `.github/scripts/rider_check.py`: the resurrection refusal in
   `region_lines` and its paragraph. From the tests: every case whose property
   is the text rule's own — the walk, the lexer's forms, the block rule, the
   statement words, the one-line call, the C# `new` and Swift `case`
   resurrections, the unsure place in `--reverify`, `--migrate` and `--into`
   (`questions.md` Q7 says which modules). From the documents: every sentence
   that describes a bracket walk, a block rule, a declaration rule or how sure
   it is (`SKILL.md`, `docs/the-evidence-ledger.md`, the `rider_check.py`
   module docstring). Measured 2026-10-12 at 64e7b0a6: the lexer, walk and
   block rule are lines 877–1214 of the checker, `generic_units` with its
   opener and words 1216–1367, and the resurrection's consumers sit at
   1490–1542, 2336–2385, 3468–3490 and 4912.

6. **What a person reads changes, so the documents and the pins change with
   it** (agent-contract §14): `SKILL.md` §*A coordinate names content* (the
   major level's "Where it comes from"), §*Resolving a unit without a parser*
   (rewritten as the format: which two rules bound a unit, and that
   everywhere else the anchor is a quoted line whose region is a paragraph),
   §*Verdicts and what to do*'s `BROKEN` row, §*What the region is* (one row
   for "a symbol in any other file"), §*Known limits* (the unsure-place
   bullet, the bracket-walk bullet and the upgrade bullet), §*Migrating a
   pre-anchor ledger*; the paragraph this work item wrote under
   `docs/the-evidence-ledger.md` §*What the checker refuses, and what it says
   while refusing*, rewritten with its `Enforced by:` line; the docstrings of
   `bounding_rule`, `resolve_unit`, `file_units`, `text_regions`.

7. **The installer paragraph is rewritten, and promises only what holds.**
   This work item's `changelog.md` says what an installer sees (below) and no
   longer says "every other row keeps its hash and its verdict" over kinds
   that change (round 1's 🟡 3).

8. **This repository's own rows are brought to the format in this branch.**
   Measured 2026-10-12 at 64e7b0a6 over `seal/ledger.md`, `seal/releases/*.md`
   and `seal/ledger/*.md`: 14 rows cite a bare YAML key and none cites a bare
   symbol in any other refused suffix. Seven sit in #864's fragment
   (`seal/ledger/1791384162-the-macos-test-leg-runs-in-shards.md`, all
   `.github/workflows/test.yml#pytest`) and are re-anchored in place, as a
   fragment row is. Seven are released — `seal/releases/0.15.5.md` S7
   (`test.yml#ledger`), `0.18.0.md` W3 and its 0.18.1 re-read and 0.20.0
   correction (`publish-release.yml#jobs`), `0.20.0.md` S1, S4 and S8
   (`test.yml#pytest`) — and each family whose newest member still carries the
   refused coordinate takes one `Corrected ·` row in this work item's fragment,
   re-pointing the claim onto the quoted line that holds it. The paragraphs
   the quotes hash, read 2026-10-12: `test.yml` has no blank line between
   `pytest:` (line 32) and line 145, nor between `ledger:` (163) and 181, so
   `"pytest:"` and `"ledger:"` hash the jobs the block rule hashed;
   `publish-release.yml` has blank lines at 61 and 70, so a claim about both
   jobs (W3) quotes `"publish:"` and `"seal:"`, two coordinates in one cell.
   The released rows whose claims described the text rule — `0.4.0.md` "The
   declaration rule reports how sure it is" and "`--migrate` answers an
   unsure place" — take a `Corrected ·` row whose grounds hold the citation
   alone, and this work item's own `Corrected ·` row for 0.4.0's "An anchor
   resolves" is rewritten to the three rules that remain.

**Out, and why.**

- **A two-quote range anchor** (`path#"from"…"to"`) that would let one
  coordinate cover a unit with blank lines. It is a new grammar in the one
  reader #867 just unified (`ANCHOR_RE`), and the cell already holds several
  coordinates, so what it buys is compactness. Weigh it after this ships, on
  a measured count of rows that needed more than one quote.
- **`--migrate` writing a quoted-line anchor** for a row it leaves. Which line
  of a cited range stands for the claim is the row's author's choice, and the
  migrator's proof is the stamp, not the content; it names the remedy and
  leaves the row.
- **A YAML parser.** The standard library has none, and `evidence-ci` vendors
  the checker as one stdlib file into a consumer's `tools/`; a dependency there
  is a second file to vendor. The block rule is refused as a guess
  (`questions.md` Q5 is where the owner can overturn that).
- **A per-language parser dependency** (tree-sitter, one grammar per
  language), for the same vendoring reason, and because the row that cites
  the parser's answer is only as stable as that grammar.
- **Declaration shapes the opener never matched** (#888). The opener leaves
  the tree, so there is no shape left for it to miss; the caller may close
  #888 as moot once this lands.
- **#867's readers** (`heading_level`, `markdown_lines`, `ANCHOR_RE`, the
  config rows) and **#836's evidence** (what a row's claim is). Untouched.
- **The `.pyi` suffix.** Phase 1 moved it from the text rule to `ast`, which
  is the parser the format asks for; it stays, and the installer paragraph
  names the one reading it changes.

**What an installer sees on upgrade, and how the release says so.** The
plugin's commit hook `hooks/evidence-advisor.py` imports the checker by path,
so a plugin update reads the installer's ledger with the new rule at the next
commit; the CI copy under `tools/` changes only when `/specseal:evidence-ci`
is re-run (`skills/evidence-ci/SKILL.md` §*Updating later*). At either
moment: **every row citing a bare symbol in a file that is not `.py`, `.pyi`
or `.md` reads `BROKEN`**, with the refusal and the quoted-line shape on its
line — TypeScript, JavaScript, Go, Rust, Java, Kotlin, Swift, C, C++, C#,
YAML, Ruby, shell, everything — including rows the indentation rule bounded
right. The act is one edit per row: quote a line of the unit the claim is
about (`path#"<the line>"@00000000`), then `--reverify`, which fills the hash;
under `Ledger frozen from` the repair is the `Corrected ·` row `--reverify`
names. A `.pyi` row whose stub is decorated reads `DRIFTED` once, because
`ast` takes the decorators into the span. Every `.py` and `.md` row keeps its
hash and its verdict. Nothing reads `DRIFTED` for a body the old span left
out, because no span is guessed any more. The work item's `changelog.md`
carries this paragraph under `### Changed`, the release gathers it into
`changelog/0.21.0.md` and the GitHub Release, and `SKILL.md` §*Known limits*
keeps the one-line version where an installer looks for it.

**The cost, stated.** A repository that cited brace-language units by symbol
loses that anchor and writes quoted lines, which break on a rewording of the
quoted line where a symbol survived one; and a quoted line hashes a
paragraph, so a row about a function with blank lines in it covers only what
it quotes. The frame judges the honest paragraph cheaper than a guessed
function, because the first says on the row what it covers and the second
read `ok` over what it left out; `plan.md` §*Alternatives considered* holds
the weighing, and `questions.md` Q3 is the installer's count.

## User scenarios & acceptance *(mandatory)*

Each case is shown red against the tree before it is planted (agent-contract
§15), and the hand-back says how. Spans are 1-based and inclusive.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 #848 by the format | Given `f.ts` holding `export function multiLine(` / `  opts: { a: number },` / `): number {` / `  return opts.a + 1` / `}`, when a row cites `f.ts#"export function multiLine("`, then the region is lines 1–5 and a body-only edit reads `DRIFTED` under `--strict`; when a row cites `f.ts#multiLine`, then `BROKEN` with "no bounding rule for `.ts`; anchor a quoted line instead" and the shape | the test case; #848's own reproduction script as a test, run against the tree with the quoted anchor |
| S2 a quoted line is a paragraph, never a function | Given `g.ts` holding `export function g(` / `  a: number,` / `) {` / `  const x = a;` / `` (blank) / `  return x;` / `}`, when `"export function g("` resolves, then 1–4; when `"return x;"` resolves, then 6–7; and `SKILL.md` §*What the region is* says a quoted line hashes the paragraph it is in and a unit with blank lines is cited one quote per paragraph | the test case; a case reading the skill for the sentence |
| S3 every other suffix refuses a bare symbol | Given one file per former brace suffix (`.ts .tsx .js .jsx .mjs .cjs .c .h .cc .cpp .hpp .cs .java .kt .kts .swift .go .rs`), `.yml`, `.yaml`, `.rb` and a file with no suffix, when a row cites a bare symbol in each, then `BROKEN` with the suffix named and the remedy, `--reverify` prints the line and writes nothing, and `rider_check.py#region_lines` returns the same sentence | the parametrised case; phase 1's `test_a_bare_symbol_in_a_suffix_no_rule_names_is_refused_with_the_remedy` widened |
| S4 the quoted line resolves everywhere | Given `svc.rb` with `def render` / `  1` / `end` and this repository's `.github/workflows/test.yml`, when `svc.rb#"def render"` and `test.yml#"pytest:"` resolve, then the contiguous runs (1–3; the `pytest` job, 32–145 at 64e7b0a6) | the test case; the repository coordinate executed and quoted in `phases/phase-7.md` |
| S5 Python refuses, never guesses | Phase 1's cases, unchanged: a `.py` the interpreter cannot parse is `BROKEN` naming the version and the error's line; a parsing file reads as it did | the existing cases |
| S6 markdown is a heading path | Phase 1's case, unchanged: a bare symbol in `.md` is refused naming the heading path | the existing case |
| S7 one reading reaches every caller | Given a refused unit, when `rider_check.py` and `survivor_check.py` ask, then each reads `resolve_unit`'s answer and neither derives one; `resurrected` appears in none of the three scripts | phase 1's caller-counting case, plus a source-reading case for the word |
| S8 one suffix table, three answers | Given `bounding_rule`, when its answers are enumerated, then `"ast"`, `"heading"`, `None` and nothing else; the four dispatches read it | phase 1's `test_the_four_dispatches_read_one_table`, narrowed |
| S9 the guessing reader is gone | Given `evidence_check.py`, when the names in *In* 5 are searched for, then none is defined, and no line of the module reads a bracket, a brace family, a YAML indent or a statement word | a source-reading case |
| S10 this repository's ledgers are clean | Given the branch after phase 7, when `bin/evidence-check --strict .` runs, then 0 `BROKEN` and 0 `DRIFTED` that `origin/release/v0.21.0` does not show | the executed output, quoted in `phases/phase-7.md`; the CI `ledger` job |
| S11 the documents say what the code does | Given `SKILL.md`, `docs/the-evidence-ledger.md` and `rider_check.py`'s docstring, when "bracket walk", "block rule", "declaration rule", "resurrect" and "how sure it is" are searched for, then none is found, and the policy paragraph's `Enforced by:` names S1 and S3's cases | `tests/test_a_record_states_what_the_tree_has.py`; a case reading the three files |
| S12 the installer paragraph exists and holds | Given `seal/specs/<this>/changelog.md`, when it is read, then under `### Changed` it says every bare symbol outside `.py`/`.pyi`/`.md` reads `BROKEN` with the remedy, a decorated `.pyi` stub reads `DRIFTED` once, `.py` and `.md` rows keep their verdicts, and what to run; no `## ` line | the fragment, read by a case |
| S13 `--migrate` names the remedy | Given an old `path:line` row in a `.rb` file, when `--migrate` runs, then the row is left and the reason reads the refusal sentence, not "no single unit contains" | the test case |

## Data & interfaces

- `bounding_rule(path) -> "ast" | "heading" | None`, the one suffix table.
  `None` is the refusal for a bare-symbol locator.
- `resolve_unit(path, locator, text)` carries two facts in one reading: the
  places, and the refusal's reason or `None`. Its callers are `judge`,
  `read_citation`, `rider_check.py#region_lines` and `survivor_check.py`'s
  `resolves`; all four are in this repository and change in the same commit.
  The shape, once no field is unsure, is `questions.md` Q6.
- `unbounded(path, rule, text)` adds the shape of the remedy to the sentence
  for `rule is None`; the `ast` and `heading` sentences are phase 1's.
- `text_regions` is unchanged. Its docstring says in one sentence what *In* 2
  says.
- `file_units` yields units for `ast` and `heading` files only. The rename
  scan therefore names no destination for a row in any other file, as it
  already named none for a quoted row; the `BROKEN` line still says
  `file not found` or the refusal, and the remedy is the same quoted line.
- Lines a person reads, pinned by a case each (§14): the refusal with the
  shape, the Python refusal with its interpreter version (kept), the
  `--migrate` left reason.
- No change to `ANCHOR_RE`, the row grammar, the verdict vocabulary, the exit
  codes, `templates/evidence-check.yml`, or the vendored-copy test.

## Rule changes

- nothing
  why: overturned: evidence-check left the tree at 5b1f6fae, and the unit reader it used
    left with this tree's coordinates.py#named_unit in #941.

## Open questions → questions.md

Seven rows: Q1 and Q4 answered by the first build and superseded here, Q2
re-measured for the reframe, Q3 the installer's count (a measurement, open),
Q5 the YAML block rule (a person, with the default the build ships on), Q6
the shape of `resolve_unit`'s answer and Q7 which cases go and which are
re-fixtured (the work). The head of `questions.md` lists what the tickets and
the review left open that the tree answered.

Framed 2026-10-07 by framer, before the build.
Reframed 2026-10-12 by framer, after round 1.
