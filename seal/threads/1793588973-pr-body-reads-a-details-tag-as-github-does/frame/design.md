# Design: 1793588973-pr-body-reads-a-details-tag-as-github-does

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms in the one spelling the form gives it." | The refusal reads a character sequence, not a meaning: a copied line, its fenced lines blanked by `unverified_check.py#readable` and its code spans by `.github/scripts/close_issues_on_release.py#SPAN`, holds `<details` or `</details` in any case, followed by whitespace, `/`, `>` or the line's end. The form is the plugin's own: a copied record line writes a `details` tag only in a code span, and the code span is the one spelling that passes. No reading of what the writer meant is made. |
| the same: "before a fix adapts to an existing structure, ask whether the structure should change" | The structure is that `seal pr-body` copies record lines byte for byte and refuses a line it cannot copy faithfully. The route that replaces it, writing the copy so that GitHub renders a tag as text, is weighed as an equal in `frame/plan.md` *Alternatives considered* (A2, A3) and rejected on #1044's premise, the row below that cites it. |
| `docs/what-a-script-gates.md` *Which gate a script holds*: "where the form requires the line, its absence is refused" | A copied line holding a live `details` tag is refused at the record's path and line, as a closing keyword already is (`skills/code-review/scripts/pr_body.py#_claims`). The refusal sentence names the tag it read and the repair: write it in a code span. |
| `docs/the-review-record.md` *The guarantee*: "copied from the work item's records inside one `<details>` block whose `<summary>` names the copy and is followed by a blank line, with nothing inside it folded again" | The rule stands as written. Today the code holds it only for a line equal to `<details>` or `</details>`; this work makes the code hold it for every line GitHub reads as opening or closing a `details` element. The rule's text does not change, so `## Rule changes` holds the no-change block. |
| #1044, `seal pr-body`: `v0.23.1:seal/threads/1793157214-the-pr-bodys-facts-come-from-the-records/frame/design.md:22`, "A copy the command makes from a record, checked byte for byte against that record, is not a second source." (read, `git grep` at the tag) | The premise that keeps the structure. Checked in the tree: `pr_body.py#_check` compares the body's lines below `HEADING` with `_composed`'s lines, which are the records' raw lines (`pr_body.py:254-262`, `:520-546`), and `agents/sealer.md:69-76` reads exit 0 as "the records' own text". An escaped copy would no longer be the record's bytes, so A2 and A3 are rejected on it. |
| #1148 (PR #1191), the fold: `v0.27.0:seal/threads/1793343707-each-document-serves-one-reader/frame/plan.md:40`, A9c chosen, "The orchestrator's part first, the records' copy under it in one `<details>` block, nothing inside folded again" (read) | The fold stays. A4 (fence the copy) and A5 (drop the fold) would reverse A9c, and neither removes the defect (`frame/plan.md` *Alternatives considered*). |
| The row that asked this: `v0.27.0:seal/threads/1793343707-each-document-serves-one-reader/gaps.md:9`, Phase 5, closed by the 0.27.1 settle at `a92c358b8` (#1214) (read) | The four lines the row named are the issue's four lines. The issue measured them; this frame does not re-measure them. |
| The issue's measurement of 2026-10-31 through `gh api markdown -f mode=gfm` (read, the issue body the orchestrator quoted whole; comments: none, the orchestrator's line) | `a sentence with </details> inside it`, an indented `  </details>` and `</DETAILS>` each end the fold; `<details open>` opens a second fold, nested. |
| How GitHub renders more copied lines inside the fold (executed, 2026-11-02: `python3 -I test_tmp_details.py`, which sent each case inside a fold through `gh api markdown -f mode=gfm` and printed the HTML; the probe and its output were deleted) | The fold ends at `</details >` (a space before `>`), at `- item </details> here` (a list item), at `[a </details> b](https://example.com)` (link text), and at `para` followed by `    </details>` (a paragraph continuation). A second fold opens at `a <details> b`, at `a <details/> b`, and at `a sentence <details` with `open> next` on the next line. These render as text and end nothing: `</details>` inside a table cell (the sanitizer drops it), `\</details>`, `<!-- </details> -->`, `</details>` in an indented code block, in a single or double backtick code span, `&lt;/details&gt;`, `<details foo=">`, and `a sentence </details` with `> next` on the next line. |
| the same probe, for the alternatives | A backslash before `<` renders as text in a paragraph and shows as `\<x>` inside an indented code block. `Framed <date> by <who>, before the build.` renders as `Framed  by , before the build.`: GitHub drops a tag it does not allow, keeping no text. |
| Which copied record lines the new reading refuses (executed: `git grep -i -E '</?details([[:space:]/>]\|$)'` over `changelog.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md` and `trail/` of every work item at `HEAD`, `v0.27.0`, `v0.26.0` and `v0.25.1`, each hit read with `close_issues_on_release.py#SPAN`'s pattern removed) | None. One hit stands outside a code span, `v0.27.0:seal/threads/1793343707-each-document-serves-one-reader/trail/phases/phase-5.md:134`, and a phase record is not copied (only its path is). So the over-refusal the reading carries has refused no record line yet. |
| Rule 12, the class (executed: `git grep -n -E '"</?details>"\|<details>' -- '*.py' ':!tests'`) | Two scripts write a `details` fold around copied text: `skills/code-review/scripts/pr_body.py` and `.github/scripts/publish_release_note.py#release_body`, whose fold holds the released changelog fragments. Each fragment is a work item's `changelog.md`, which `pr_body.py#_changed` copies whole into that work item's body, so this refusal reaches it at the fragment's pull request. A settle writes no fragment (`skills/settle/SKILL.md` *A settle is not a work item*). The release note needs no change of its own. |
| Who reads the body (read: `grep -n -i body skills/code-review/scripts/chain_check.py`; `agents/sealer.md:69-80`) | `chain_check.py` reads no pull request body. The sealer reads it through `seal pr-body --check` at step 2 and withholds on any exit but 0; the orchestrator runs `seal pr-body` before every sealer spawn (`skills/code-review/orchestration.md:346-366`). A refusal therefore reaches the orchestrator, which repairs the record line, never a person. |
| The orchestrator's line (read): milestone `release: 0.28.0` puts #1218 before #1204, which also edits `pr_body.py` | #1204's scope (the seal mark on the body and the release note) is out. |

## Scope

In:

1. `skills/code-review/scripts/pr_body.py#_composed` refuses a copied line, outside a fence and a code span, that holds `<details` or `</details` in any case, followed by whitespace, `/`, `>` or the line's end. The line is the record's `readable` line with its code spans blanked by `close_issues_on_release.py#SPAN`, the reading `_claims` already uses for a closing keyword, so the two refusals read one line one way. The refusal stands at the record's path and line, and its sentence names the tag as read and says to write it in a code span. It replaces the equality test against `FOLD` and `FOLD_END`; the `HEADING` test and `_claims` are unchanged.
2. `pr_body.py`'s module docstring and `_composed`'s docstring say what is refused, in place of "equal to `FOLD` or `FOLD_END`". The module docstring's *Limits* list gains the reading's two edges: a line GitHub renders as text is refused too where it is spelt as a tag outside a code span (in a table cell, after a backslash, in an indented code block, in an HTML comment), and a tag between two backticks that are not a code span to GitHub, such as an escaped backtick, is read as inside a span and passes.
3. `tests/skills/test_pr_body.py#Test_compose::test_refuses_a_record_it_cannot_copy_faithfully` gains a refused case for each of the issue's four lines and for the two arms the issue's lines do not reach: `a <details/> b` and a line ending in `<details`. A case passes a backticked `` `</details>` ``. The two existing equality cases stay. The test's docstring says what is refused.
4. This work item's own records write every `details` tag in a code span, so `seal pr-body` composes them with no refusal.

Out:

- The pull request body's shape, the fold, and the release note's fold: unchanged (A4, A5).
- Tags other than `details`. A `<summary>` inside the fold does not end it (the probe). A tag GitHub drops, such as `<who>` in a record line outside a code span, loses its text in the rendered body today; the squash commit and the body file keep it. No issue or row asks this, and this frame names it for the orchestrator only.
- #1204's seal mark on the body and the release note.
- `.claude-plugin/plugin.json`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The issue's four lines are refused | Given a work item whose `changelog.md` gains one line, `a sentence with </details> inside it`, `  </details>`, `</DETAILS>` or `<details open>`, when `pr_body.compose` runs, then it raises `Refused` with one cause at `changelog.md` and that line, and the cause names the tag it read | `tests/skills/test_pr_body.py#Test_compose::test_refuses_a_record_it_cannot_copy_faithfully`, one parameter each; each shown red against the tree at `627c47dd9` |
| S2 Each arm of the reading has a refused case | Given the same with `a <details/> b`, or a line ending in `a sentence <details`, when `compose` runs, then it is refused at that line. Each refused case is shown red with its own guard alone removed: the case-insensitive flag for `</DETAILS>`, the search anywhere in the line for the sentence and the indented line, the whitespace, `/` and line-end arms after the tag name for `<details open>`, `<details/>` and the line ending in `<details` | the same test; the crafter's phase record says how each was shown red |
| S3 A code span passes | Given a `changelog.md` line `` `</details>` in a span ``, when `compose` runs, then nothing is refused, and the line stands in the fold as written | `tests/skills/test_pr_body.py`, a passing case; shown red with the code-span blanking alone removed |
| S4 The exact lines still refuse and a fence still passes | Given the existing parameters `<details>` in `changelog.md` and `</details>` in `gaps.md`, and a fenced `</details>`, when `compose` runs, then the first two are refused at their lines and the fenced one is not | the existing parameters of the same test, green |
| S5 This work item's records compose | Given this work item's records at the phase's commit, when `bin/seal pr-body seal/threads/1793588973-pr-body-reads-a-details-tag-as-github-does --body <scratchpad>/1793588973-pr-body-reads-a-details-tag-as-github-does/pr-body.md` runs, then it exits 0 | executed by the crafter at the phase's close, the body file removed after |

## Data & interfaces

`skills/code-review/scripts/pr_body.py`:

- A module constant holds the reading as one compiled pattern, `</?details` with `re.IGNORECASE`, followed by a lookahead for whitespace, `/`, `>` or the end of the string. Its comment says the form it reads and why a code span is the one spelling that passes.
- `_composed`: the `elif seen[rel][line - 1] in (FOLD, FOLD_END)` arm becomes an arm that searches `CLOSER.SPAN.sub(" ", seen[rel][line - 1])` with that pattern. Its cause is `(rel, line, why)`, where `why` names the matched tag as read, says GitHub would open a second fold there or end the copy's one fold early, and says to write it in a code span. `FOLD` and `FOLD_END` stay, since `_composed` writes them.
- No new import: `CLOSER` is already loaded (`pr_body.py:94-110`).
- Exit codes, the `refused:` line's shape and `_place` are unchanged.

## Rule changes

- nothing
  why: The rule this work makes the code hold, "nothing inside it folded again", stands in `docs/the-review-record.md` *The guarantee* as written. What `seal pr-body` refuses is stated in `skills/code-review/scripts/pr_body.py`'s docstrings, its home, and no policy document states the equality test this replaces.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The equality test of a copied line against `FOLD` and `FOLD_END` | `skills/code-review/scripts/pr_body.py#_composed` | Replaced in place by the tag reading of *Scope* item 1, which refuses every line the equality test refused |
| "A copied line equal to `HEADING`, `FOLD` or `FOLD_END` is refused at the record's line" and `_composed`'s "or, outside a fence, to `FOLD` or `FOLD_END`" | `skills/code-review/scripts/pr_body.py`, the module docstring and `#_composed` | Rewritten in place to the reading of *Scope* item 2 |
| "a copied line equal to `HEADING`, `<details>` or `</details>`" | `tests/skills/test_pr_body.py#Test_compose::test_refuses_a_record_it_cannot_copy_faithfully`, its docstring | Rewritten in place to what the test now refuses |

The work adds no mechanism: it changes what an existing refusal reads.

Framed 2026-11-02 by framer, before the build.
