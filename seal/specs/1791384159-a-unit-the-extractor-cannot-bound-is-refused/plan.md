# Implementation Plan: a unit the extractor cannot bound is refused (#870, #848)

<!-- seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-08 by the repository owner, when `smith` was spawned.
Approved 2026-10-12 by the orchestrating session under the owner's `automation` answer and the owner's reframe decision, for the redesign after round 1, when `smith` was spawned; `questions.md` Q5 is built on its default (a).

## Summary

Bound a unit only where a real parser decides its extent — Python's own `ast`
for `.py` and `.pyi`, CommonMark's heading rule for `.md` — and everywhere
else require the format the checker already has: a quoted line, whose region
is the paragraph it sits in. The bracket walk and its nine-family lexer, the
YAML block rule, the declaration opener, the statement words and the
resurrection flag leave the tree, and every sentence that described them goes
with them. #848 is answered by the row quoting a line of the function, which
hashes the whole function where no blank line divides it, and says on the
row what it covers where one does. This repository's own fourteen bare YAML
rows are brought to the format in this branch, and an installer's bare
symbols outside the two parsers read `BROKEN` once with the remedy on the
line.

The first plan (phases 1–4) replaced the indentation rule with the walk. The
owner's review of 2026-10-12 judged the walk a new guessing reader against
0.21.0's theme (`spec.md` §*Why this work item was reframed*), and this plan
replaces phases 2–3's deliverables while keeping phase 1's table and refusal
and phase 4's records as the base the redesign edits.

## Technical context

All coordinates at 64e7b0a6 (this branch's head after round 1 closed), read
2026-10-12.

- `skills/evidence-check/scripts/evidence_check.py#text_regions` (L590–631):
  the quoted-line region, the contiguous run of non-blank lines, whitespace
  normalised on match. Unchanged by this work; the format it already is.
- `#AST_SUFFIXES`, `#HEADING_SUFFIXES`, `#BLOCK_SUFFIXES`, `#BRACE_FAMILY`,
  `#BRACE_SUFFIXES` (L680–706); `#bounding_rule` (L709–732), four answers
  today; `#unbounded` (L735–759), the refusal sentences; `#Resolution`
  (L762–784), the pair plus `refused`; `#resolve_unit` (L803–874), the
  `"brace"`/`"block"` arm at L872; `#brace_family` (L877).
- The lexer, walk and block rule, L879–1214: `StringForm` and the forms
  (L879–917), `_literal_at` (L927), `brace_lexed` (L1016), `brace_span`
  (L1137), `block_span` (L1194). `declaration_opener` (L1216),
  `opens_declaration` (L1226), `STATEMENT_WORDS` (L1241), `generic_units`
  (L1271–1367). All of it leaves.
- The resurrection's consumers: `file_units`' third field (L1490–1542,
  `rule in ("brace", "block")` at L1529); `judge`'s
  `resurrected or len(places) > 1` branch and the `unsure` detail
  (L2336–2385); `migrate`'s `unsure and not proved` branch (L3468–3490);
  `reverify_into` at L4912; `.github/scripts/rider_check.py#region_lines`
  (L505–510) and the module docstring's paragraph (L88). `resolve` (L787)
  returns `resolve_unit(...)[0]`.
- `#minor_region` (L1446), `#content_matches` (L1590): read `bounding_rule`;
  unchanged except that the rename scan finds no units outside the two rules.
- `skills/evidence-check/SKILL.md`: §*A coordinate names content* (L19–45,
  the Major row's "otherwise the declaration rule below"), §*Resolving a unit
  without a parser* (L87–167), §*Verdicts and what to do* (L295–312, the
  `BROKEN` row), §*What the region is* (L434–453), §*Known limits*
  (L722–806: the unsure-place bullet, the eighteen-suffix bullet, the upgrade
  bullet), §*Migrating a pre-anchor ledger* (L808–840).
- `docs/the-evidence-ledger.md` §*What the checker refuses, and what it says
  while refusing*, the paragraph this work item wrote (L268–291) with its
  `Enforced by:` line.
- The tests: `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`
  (698 lines; the refusal cases L82–266 stay, the walk, lexer and YAML cases
  L295–647 go, the document cases L649–698 are rewritten);
  `tests/test_a_row_points_by_content.py` (26 mentions of the text rule);
  `tests/test_a_released_row_is_read_again_in_a_fragment.py` (21, around
  L3343–3420 and L3862–3946, `.go` and `.cs` fixtures the rule was unsure of);
  `tests/test_a_signer_records_a_pact_change.py` (13, L2242–2320);
  `tests/test_the_fixes_name_their_surface.py` (one comment, L1037).
- This repository's rows, measured 2026-10-12 (`spec.md` *In* 8): 14 bare
  YAML rows, 7 in `seal/ledger/1791384162-the-macos-test-leg-runs-in-shards.md`
  and 7 released; `.github/workflows/test.yml` `pytest:` at L32 with no blank
  line to L145 and `ledger:` at L163 to L181; `publish-release.yml` `jobs:` at
  L46, `publish:` L47, blank at L61 and L70, `seal:` L71 to L138. Released
  rows citing units that leave: `seal/releases/0.4.0.md` L51 and L67; this
  item's fragment rows U1–U8 and its `Corrected ·` row for 0.4.0 L17; #867's
  fragment `Re-read ·` rows at L76, L78, L79 citing `resolve_unit`,
  `generic_units` and `file_units` at their 2026-10-08 hashes.
- `seal/config.md`: `Ledger frozen from | 1790993141`; no `Record language`
  row, so the records are English.

**The failure scenario of the chosen approach, in six months.** A row quotes
the signature line of a function whose body has a blank line in it, the body
below the blank line is rewritten, and the row reads `ok`. The bound on it:
the row says on its face which paragraph it covers, the skill says a quoted
line is a paragraph and never a function, and the remedy is one more
coordinate in the same cell; what the walk did in the same case was read
`ok` with nothing on the row to say so. The second scenario: a quoted line
is reworded and the row reads `BROKEN` where a symbol anchor would have read
`DRIFTED`; the cost is a ledger edit, which is the cost the format trades for
never guessing an extent. The third: the quoted line comes to occur twice,
and the recorded hash breaks the tie as it does today; where the row's
content is in neither or both, `BROKEN` names the places.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **#848's own fix** — a line that is only a closing paren continuing the declaration does not end the block | Allman `{` on its own line is still cut; every new formatter shape is a new clause. The reader-of-more-shapes family #834's table shows did not converge | refused (first frame) |
| **The bracket walk over an allow-list of brace languages, with a lexer per family** — phases 2–4 as built | Round 1 found three more shapes inside the nine families: a regex or template that opens a phantom comment puts a declaration back under the indentation rule (#848 again, silent), a column-0 multi-line string ends its constant on line one, and the release note's "every other row keeps its verdict" was false for four kinds. Each is one more clause in a lexer that imitates nine grammars, and the next form it does not know is silent. The owner judged it a guessing reader against 0.21.0's theme | **refused by the owner's review of 2026-10-12**; removed by phase 5 |
| **Keep YAML's block rule, declared a guess** | Round 1's 🟡 2: a comment at the key's indent ends the key. Block scalars, multi-line flow collections, document markers and aliases are the next shapes, and the standard library has no YAML parser to replace the imitation with | refused; `questions.md` Q5 is where the owner overturns it |
| **A per-language parser** (tree-sitter, PyYAML, one grammar per language) | `evidence-ci` vendors the checker as one stdlib file into a consumer's `tools/`; a parser is a dependency to vendor and a grammar per language to version | refused |
| **A two-quote range anchor** `path#"from"…"to"`, so one coordinate covers a unit with blank lines | A new grammar in `ANCHOR_RE`, the one reader #867 just unified, bought for compactness: the cell already holds several coordinates, and nothing has measured how many rows need more than one | refused for now; weigh after a measured count |
| **`--migrate` writes a quoted-line anchor for a row it leaves** | Which line stands for the claim is the author's choice, and the migrator's proof is the stamp, not the content | refused; it names the remedy and leaves the row |
| **Keep the resurrection flag with a constant `False`** | A field no code can set is read by `judge`, `--reverify`, `--migrate` and `rider_check.py` as a fact about the place; the branches it guards are unreachable and the sentences they print are promises about a rule that is gone | refused; `questions.md` Q6 |
| **`ast` for `.py`/`.pyi`, the heading path for `.md`, a quoted line everywhere else, the guessing readers and the flag removed, this repository's rows brought to the format** | the six-month scenarios above | **chosen** |

## Phases

Vertical slices — each phase ends with something runnable and verified. The
narrow check for every phase is the slice of the tests it touches plus the
cases it plants; no phase runs the suite, the repository-wide lint or the
typecheck (agent-contract §2). Each new case is shown red first and the
hand-back says how (§15). Phases 1–4 are closed and keep their commits; the
redesign starts at phase 5 and edits what they built.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The table and the refusal.** `bounding_rule(path)`; the four suffix dispatches read it; `resolve_unit` carries a refusal reason in one reading and the callers unpack it; `.py` that will not parse and a suffix with no rule are `BROKEN` with the reason and the quoted-line remedy; `--reverify` prints and writes nothing. Cases S5, S6, S7, S8 of the first frame | the cases; the `resolve_unit`/`judge` slice; `tests/test_a_rider_reaches_its_file.py` | cfcd630d |
| 2 | **The bracket walk.** The lexer per family, the depth walk, the closer-only last line left out, imbalance refused, the day-one list, `file_units` on `generic_units`'s opener. **Superseded: phase 5 removes it** | the cases of the first frame | 0011e870 |
| 3 | **YAML as a declared block rule.** `"block"` for `.yml`/`.yaml` with the compact sequence. **Superseded: phase 5 removes it, and phase 7 re-anchors the rows it bounded** | the cases of the first frame; `--strict .` byte-identical | a2bc18ec |
| 4 | **The documents and the records** of the first design. **Superseded: phase 8 rewrites them** | the hygiene tests | 951b0a1d |
| 5 | **The format, and the guessing reader leaves.** `bounding_rule` answers `"ast"`, `"heading"` or `None`; `resolve_unit`'s `"brace"`/`"block"` arm goes; `unbounded` adds the anchor's shape to the refusal; `--migrate`'s left reason for such a file reads the refusal (S13); `BRACE_FAMILY`, `BRACE_SUFFIXES`, `BLOCK_SUFFIXES`, `brace_family`, the `StringForm` forms, `_literal_at`, `brace_lexed`, `brace_span`, `block_span`, `declaration_opener`, `opens_declaration`, `STATEMENT_WORDS` and `generic_units` are deleted with the cases that pinned them (`tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` L295–647 and the walk cases of `tests/test_a_row_points_by_content.py`); `text_regions`' docstring states the paragraph rule. Cases S1, S2, S3, S4 (the `.rb` half), S8, S9, S13 red then green. The CI `ledger` job is red from this phase to phase 7, which is the known state the frame accepts, because the rows it refuses are repaired there with the reading they are owed | the cases; the `resolve_unit`/`judge`/`migrate` slice of `tests/test_a_row_points_by_content.py`; `tests/test_a_rider_reaches_its_file.py` | 1e00f933 |
| 6 | **Nothing is unsure any more.** `Resolution` takes Q6's shape and every unpacking site reads it in one commit; `judge`'s resurrection branch, `--reverify`'s and `--migrate`'s unsure branches, `file_units`' third field and `rider_check.py#region_lines`' refusal go; the cases of `tests/test_a_released_row_is_read_again_in_a_fragment.py`, `tests/test_a_signer_records_a_pact_change.py` and `tests/test_a_row_points_by_content.py` that reached their property through an unsure `.go`/`.cs` place are judged per Q7, re-fixtured or deleted, each named in `phases/phase-6.md`. Case S7 widened to the word `resurrected` | the cases; the three modules' slices; `bin/mutation-check` over `judge`'s and `migrate`'s changed units | |
| 7 | **This repository's ledgers are brought to the format.** #864's seven fragment rows re-anchored in place (`test.yml#"pytest:"`); one `Corrected ·` row per released family whose newest member still carries a refused coordinate (0.15.5 S7 → `"ledger:"`; 0.20.0's W3 correction → `"publish:"` and `"seal:"`; 0.20.0 S1 → `"pytest:"`), with the claim unchanged; `Corrected ·` rows with the citation alone for 0.4.0 L51 and L67; this item's own fragment rewritten — U1 narrowed to three answers, U2 to the two refusals, U3 kept, U4–U7 removed, U8 deferred to phase 8, the 0.4.0 L17 `Corrected ·` row restated for the three rules that remain; `--reverify --into` for every released row a changed unit drifted, read first. S4's repository half and S10: `bin/evidence-check --strict .` 0 `BROKEN`, 0 `DRIFTED` against `origin/release/v0.21.0`, quoted in `phases/phase-7.md`; `survivor-check` and `correction-check` over the range | the executed `--strict .` output; `tests/test_a_record_states_what_the_tree_has.py`; `correction-check` | |
| 8 | **The documents say what the code does.** `SKILL.md`'s six sections, `docs/the-evidence-ledger.md`'s paragraph with `Enforced by:` naming S1 and S3, `rider_check.py`'s docstring, the docstrings of `bounding_rule`, `resolve_unit`, `file_units`; `changelog.md` rewritten with the installer paragraph of `spec.md`; the fragment's U8 row; `overview.md` brought to the redesign. Cases S11, S12 | `tests/test_a_record_states_what_the_tree_has.py`; `tests/test_the_fixes_name_their_surface.py`; the eight guard modules the spawn names | |

**The names this plan and `spec.md` give to what phase 5 deletes stop being
in the tree when it lands.** The records arm reads every record of an
unshipped work item (`SKILL.md` §*Verdicts and what to do*, the `NOT-IN-TREE`
row), so from phase 5 on each line of this directory that names a deleted
unit — here, in `spec.md` *In* 5, in the round 1 records — is marked
` · NAME NOT IN TREE` rather than reworded: the frame says what left, and the
marker says it is known to have left.

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.
The evidence ledger had the same problem and no such tolerance. It no longer
has it at all: a ledger row names a symbol and a content hash, so there is no
commit in it for a rebase to orphan.

## Seams with the sibling frames

- **#867** (`seal/config.md` rows, the coordinate grammar, markdown headings
  — `evidence_check.py#heading_level`, `#markdown_lines`, `#ANCHOR_RE`). Landed;
  the `.md` arm of `resolve_unit` and `file_units` calls them and this work
  does not touch them. #867's fragment carries `Re-read ·` rows for 0.4.0's
  L17, L51 and L67 at the 2026-10-08 hashes of `resolve_unit`,
  `generic_units` and `file_units`; phase 7's `Corrected ·` rows supersede
  those families, and `--reverify --into` names what is owed.
- **#864** (the macOS shards). Landed; its fragment holds seven of the bare
  YAML rows, re-anchored in place by phase 7 as a fragment row is.
- **#836** (a row's claim is the test that enforces it; being reframed). The
  row grammar, `ANCHOR_RE` and `Verdict` are unchanged here. The seam is
  `judge`'s `BROKEN` detail text; a refusal still reads `BROKEN` on the
  anchor whatever #836 puts beside it.
- **#835** (a reader declares its input class). The table in `spec.md` *In* 1
  is written in #835's three words; this item does not write the registry.
- **#888** (the opener's shapes). Moot once phase 5 lands; the caller may
  close it.
- Nothing shared with #866, #868, #869, #860, #858, #837.

## What this removes

The bracket walk and its nine-family lexer, the YAML block rule, the
declaration opener, the statement words and the one-line-call guard, the
resurrection flag with every branch it guarded in `judge`, `--reverify`,
`--migrate`, `file_units` and `rider_check.py`, the cases that pinned each,
and every sentence in `SKILL.md`, `docs/the-evidence-ledger.md` and the
docstrings that described a rule bounding a unit without that language's
parser. What it adds is one sentence in `unbounded`, one in `text_regions`'
docstring, one in `--migrate`'s left reason, and the cases that pin them.
Measured 2026-10-12: the code that leaves is about 490 lines of
`evidence_check.py` (L879–1367) plus the consumer branches, against roughly a
dozen lines added.

## Operational impact

- **Every installer**, at the next plugin update (the commit hook) and at the
  next `/specseal:evidence-ci` re-run (the CI copy): every row citing a bare
  symbol in a file that is not `.py`, `.pyi` or `.md` reads `BROKEN` with the
  refusal and the anchor's shape on its line, rows the old rule bounded right
  included; the repair is one quoted line per row and `--reverify`, or under a
  freeze the `Corrected ·` row `--reverify` names. A decorated `.pyi` stub
  reads `DRIFTED` once. Every `.py` and `.md` row keeps its hash and its
  verdict. The changelog fragment says so and says what to run.
- **This repository**: 14 rows change verdict and are repaired in phase 7;
  the released rows that described the text rule take `Corrected ·` rows;
  `--strict .` is clean again at phase 7's close (Q2).
- **The draft pull request's CI `ledger` job** is red between phase 5 and
  phase 7. The broad gate runs once, after the rounds settle.
- No new dependency, no new env var, no migration, no change to
  `templates/evidence-check.yml` or to the vendored-copy test.
- The release carrying this is 0.21.0, already a minor.
