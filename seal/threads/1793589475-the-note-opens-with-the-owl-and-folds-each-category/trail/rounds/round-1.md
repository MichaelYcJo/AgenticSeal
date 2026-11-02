# Review round 1: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

```seal
target: 3b82bbf31 against bf18be7d1
```

This is the work item's first round, so no fact was carried from an earlier
record; every coordinate below was opened in the worktree at `3b82bbf31` or
in a `git clone --no-local` of it. `seal/parity.md` is not declared, so no
parity comparison applies and the round block has no `original:` line.

## Findings

### 1. The limit sentence says no merged title held a `details` tag, and #1293, merged into this very release, holds three, so the 0.28.0 note will show its line with two stray disclosure widgets

```seal
severity: must
location: `.github/scripts/publish_release_note.py:542-551`, `.github/scripts/publish_release_note.py:684-692`, `seal/threads/1793589475-the-note-opens-with-the-owl-and-folds-each-category/changelog.md:3`, `tests/github/test_publish_release_note.py:645-662`
evidence: executed `gh pr view 1293 --json title,state,mergedAt,baseRefName`, `gh pr list --state merged --limit 3000 --json number,title`, `bin/test tests/github/test_tmp_details_title.py -p no:xdist -q -s`, `gh api -X POST markdown -f mode=gfm -F text=@note.md`, `gh api -X POST markdown -f mode=gfm -F text=@lone.md`
```

Why it matters: the release this branch ships in is the counter-example to
the limit it states. The docstring of `release_body`
(`.github/scripts/publish_release_note.py:684-692`) and the changelog
fragment (`changelog.md:3`) both state the limit's ground as a count:
"0 of the 318 pull request titles merged by 2026-11-02 held a `details` tag
at all", and in the fragment "none of the 318 pull request titles merged by
2026-11-02 held such a tag". Pull request #1293 merged into
`release/v0.28.0` at 03:49 UTC on 2026-11-02. Its title reads "fix: seal
pr-body refused only an exact `<details>` or `</details>` line, and GitHub
ends the fold at one inside a sentence, indented or in capitals, and nests a
second at `<details open>`", with all three tags bare (executed). A list of
every merged title, matched case-insensitively for an opening or closing
`details` or `summary` tag, returns 1 of 320, and that one is #1293
(executed). That list is whole for the merged titles to date, because the
command lists every merged pull request.

What the 0.28.0 note will show was probed. The probe built the note with
`release_body` for the suite's fixture release plus #1293's title, through
`tests/github/test_publish_release_note.py#published`, in the scratch clone.
It then sent the note to GitHub's own Markdown renderer. GitHub's sanitizer
keeps the Fixes fold whole: it pairs the title's `<details>` with its
`</details>`, and closes the `<details open>` inside the list item. So the
fold structure holds for this title. The line itself does not hold.
GitHub's renderer returns it as "Seal pr-body refused only an exact", then
an inserted `<summary>Details</summary>` widget holding " or ", then "line,
and GitHub ends the fold ...", then a second, open `Details` widget holding
"(#1293)" (executed). The three tags the title quotes vanish from the text,
and two disclosure widgets labelled "Details" appear in their place. The
same note's full-changelog fold then publishes this branch's fragment saying
that no title holds such a tag.

A lone `</details>` behaves as the docstring says. A probe of a fold whose
line holds a bare `</details>` alone returned the fold closed at that point,
with the next line outside it (executed). A lone `<details>` opens a
`Details` widget that takes the rest of its line (executed), which the
docstring does not mention. The class is a title whose `<` begins any tag
GitHub's renderer keeps, and its domain is every such tag. The `details` and
`summary` ones are the ones that move the folds. `kind_and_text` (`:542-551`)
also feeds the thanks section (`:581`), so the class reaches that section's
lines as well.

The frame chose to state this as a limit rather than escape it
(`frame/plan.md` *Alternatives considered*, row A6). Its ground was "a
shape found in 0 of 318 merged titles and 0 of 68 published notes". The
first ground no longer holds, and the second will not hold once 0.28.0 is
published. Whether A6's verdict stands is the fix pass's judgment to make
and record in `frame/plan.md` *Judgments of the run*. Either way, the two
sentences that state the count are wrong today, and an agent weighing the
class later reads them as its evidence. A count dated into a docstring is
also a stored number that drifts from the tree, which `skills/core/SKILL.md`
*The rule a mechanism is kept against* asks not to keep.

The render case `test_github_reads_each_fold_as_one_element_holding_its_lines`
(`:645-662`) would not have caught this. Its reader, `Folds`, reads cmark's
output tag by tag with `html.parser`, and does not rebuild the tree as
GitHub's sanitizer does. Over #1293's title it reported three folds with
empty summaries, where GitHub's renderer returns one Fixes fold (executed).
For the titles the case holds, the reader and GitHub agree.

The fix this round recommends escapes the class at the one function every
title line passes through, and drops the count. The escape writes each `<`
outside a code span as `&lt;`. GitHub's renderer then returns #1293's line
with its three tags as text, one list item and no widget, and keeps a
`</details>` quoted in a code span as code (executed: the escaped form sent
to GitHub's renderer). Its precondition: `SPAN` reads a code span as
`close_issues_on_release.py#SPAN` does, as a run of one or two backticks. A
title is one line, so the module's `FENCE` pattern has nothing to remove.

```python
# .github/scripts/publish_release_note.py, the import at :124
from close_issues_on_release import SPAN, keywords_in  # noqa: E402


def kind_and_text(title):
    """`(heading, text)`: where a title's line goes, and what it reads.

    Each `<` outside a code span is written `&lt;`, which GitHub shows as
    `<`, so a title quoting a tag shows the tag and opens or closes no fold
    (#1153; #1293's title holds three `details` tags bare)."""
    title = TRAILING_REF_RE.sub("", title.strip())
    found = TITLE_RE.match(title)
    heading, text = OTHER, title
    if found:
        heading = dict(TYPES).get(found.group("type").lower(), OTHER)
        text = found.group("text")
    # A line reads as a sentence; a title that opens on code keeps its case.
    text = text[:1].upper() + text[1:]
    pieces = re.split(f"({SPAN.pattern})", text)
    return heading, "".join(
        piece if SPAN.fullmatch(piece) else piece.replace("<", "&lt;")
        for piece in pieces
    )
```

The docstring paragraph at `:684-692` becomes:

```text
    Every fold's tags stand on lines of their own, with a blank line after
    the summary line and before the closing tag, so GitHub reads the lines
    between as Markdown. A pull request title reaches its fold with each `<`
    outside a code span written `&lt;` (`kind_and_text`), so a tag it quotes
    is text, inside a code span or out of one. A fragment holding a bare
    `details` tag is refused at `seal pr-body` before its pull request opens
    (#1218).
```

The fragment's last two sentences of its first entry become: "A title that
quotes a tag shows the tag as text, in a code span or out of one, so no
title opens or closes a fold." The render case takes #1293's title among
its pull requests. It asserts the Fixes fold holds the line "Seal pr-body
refused only an exact `<details>` or `</details>` line, ... (#1293)" with
the tags as text. It is seen red against the code at `3b82bbf31`, where
the reader returns the title's tags as folds.

If the fix pass keeps A6, the other course is for the orchestrator to
retitle #1293 with its tags in code spans before the release merges to
`main`, since `publish` reads the titles at that merge. The docstring and
the fragment then state the limit with #1293 as its one instance, and no
count. That course leaves the class open for the next title.

## Confirmations

```seal
confirms: none
```
What matched: each category is one fold in the shape *Data & interfaces*
gives. The tags stand on their own lines, a blank line follows the summary
line and precedes `</details>`, one blank line parts two folds, and the
order is `TYPES`' with Other last (`.github/scripts/publish_release_note.py:714-728`,
read). For every title the suite holds, and for #1293's, GitHub's renderer
returned each category as one `details` element closed where the renderer
closes it (executed, the probe above). Only a lone `</details>` in a title
breaks a fold, which finding 1 covers. A fragment cannot reach a category
fold: the fragments go only into the full-changelog fold (`:742-747`, read),
and #1218 holds their bare tags at `seal pr-body`, as the design states.

```seal
confirms: none
```
What matched: the header guard reads an exact fact. `seal_release` takes
the text `header` returns for the release it re-counts through `publish`'s
own `merged_pulls` and `tally`. It edits only where that text stands in the
published body exactly once (`.github/scripts/release_seal.py:505-512`,
read). The two-cell header does not contain the one-cell text: the first
`<td>` of each differs, the image against the counts. So the note a first
run leaves holds no match, and a second run refuses before the upload
(`:505-519`, read). That case is pinned by
`tests/github/test_release_seal.py:686-703`. The same exact-text guard
already held on a published note: the v0.27.3 note carries the sealed image
in place of its glance table (executed, `gh release view v0.27.3 --json
body`), so GitHub returns a note's body as `publish` wrote it, to the byte
the guard compares.

```seal
confirms: none
```
What matched: the build keeps the earlier decisions the design builds on.
On #718, no step, output or `continue-on-error` of the workflow changed. The
diff touches only its opening comment, and the job and its steps keep
`continue-on-error: true` and their timeouts
(`.github/workflows/publish-release.yml:100-150`, read). On #832, the image
fills the first cell and the results the second. `SEALED` is bold, no frame,
colour or style attribute is added, and the width is `int(width)` from
`draw` (`.github/scripts/publish_release_note.py:632-651`, read). On #857
and #1174, `draw` is outside the diff. On #1117, `publish` and `seal` read
one list at one tag (`.github/scripts/release_seal.py:485-488`, read). The
two departures are the ones issue #1153 asks for, read in its body: "The
note opens with one HTML table", and each category "becomes a `<details>`
whose summary is its name and its count, such as `U+1F41B Fixes (7)`". The
issue's example also writes the summary with the type's emoji, which the
design's decision to keep the type names rests on.

```seal
confirms: none
```
What matched: the phase-2 record claimed that two failing lines of its red
run were not read. It names them as the results case and the dry-run case
(`trail/phases/phase-2.md`). Both are red against phase 1's code by reading.
The results case calls `results`, and the module at `ef978e65f` has no such
function. The dry-run case asserts `alt="The 1.2.3 release seal"` with its
closing quote, and the old alt went on with ": SEALED ..."
(`tests/github/test_release_seal.py:915-938` and `:845-869`, read, against
the deleted lines of `alt_text` in the diff). The record's disclosure is honest, and the
two cases pin what they claim.

```seal
confirms: none
```
What matched: phase 1 claimed that every run collecting
`tests/github/test_publish_release_note.py` installs `cmarkgfm`, which the
module now imports at its top. `.github/workflows/test.yml:149`,
`.github/workflows/publish-release.yml:127` and
`.github/scripts/run_tests.py:135` install it. The one job that installs
pytest alone runs `tests/skills/test_arm_check.py` only
(`.github/workflows/test.yml:242-243`, read). The two changed modules pass
through the repository's runner in the clone at `3b82bbf31`, 95 cases
(executed). This is a narrow run of two modules, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the releases page lays out the two-cell header readably at desktop and phone width (`frame/questions.md` Q1) | the 0.28.0 note on the releases page | the orchestrator of the 0.28.0 release, after the `seal` job |
| Whether a real `gh release edit` leaves the two-cell header as the cases build it, and a real re-run then writes nothing; the cases stand in for `gh` | `.github/scripts/release_seal.py:505-529` | the orchestrator of the 0.28.0 release, after the `seal` job |
| The full suite, the repository-wide lint and the format check at HEAD. The crafter labelled them not verified with the orchestrator as answerer (`gaps.md` *Not verified*), and that label is honest | the branch at its head | the orchestrator, by `seal gate` after the rounds settle |
| The phases' `seal mutate` runs, thirteen mutants in all, each claimed `red` | `trail/phases/phase-1.md`, `trail/phases/phase-2.md` | the sealer, in its sample of the crafter's claims |

Edges judged not worth a finding, with their grounds:

- **Two `plural` functions**, one in each script (`gaps.md` *Not done*).
  Each is one line, and they pluralise different words into outputs that
  never have to agree. The cost of merging them is a load of the publisher
  in `release_rows`, which the row cases call directly. Nothing a reader
  sees can go wrong from the copy.
- **The fragment's "the three counts"** in its second entry. A release with
  no outside contributor carries two. The sentences before it say "the
  outside contributors where there are any", so a reader is not misled.
- **The `Folds` reader is not a tree builder.** It is named under finding 1,
  and the fix there makes the reader's input carry no title tag. Rewriting
  it to build the tree as a browser does would guard only the case finding 1
  closes.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_tmp_details_title.py -p no:xdist -q -s`, a probe that built the note for the fixture release plus #1293's title and wrote it and cmark's HTML to the round's scratch directory | 1 passed, exit 0. cmark's HTML holds the title's three tags raw inside the Fixes fold's list item. The suite's `Folds` reader reported three folds with empty summaries in place of the one Fixes fold. The probe file was deleted afterwards. |
| `gh api -X POST markdown -f mode=gfm -F text=@note.md`, the probe's note through GitHub's renderer | exit 0. The Fixes fold is one element. #1293's line holds two inserted `<summary>Details</summary>` widgets, the second `open`, and the title's tags are gone from its text. |
| `gh api -X POST markdown -f mode=gfm -F text=@lone.md`, a fold whose line holds a lone `</details>`, and one whose line holds a lone `<details>` | exit 0. The first fold closed at the tag, and the next line fell outside it. The second line gained a `Details` widget holding the rest of the line, and its fold stayed whole. |
| `gh api -X POST markdown -f mode=gfm -F text=@escaped.md`, #1293's title with each `<` written `&lt;`, beside a title quoting `</details>` in a code span | exit 0. Both lines are list items of one fold. #1293's tags read as text, and the quoted tag is code. |
| `gh pr list --state merged --limit 3000 --json number,title`, matched for an opening or closing `details` or `summary` tag | 320 merged titles, 1 match: #1293. |
| `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q` in the clone at `3b82bbf31` | 95 passed, exit 0. |
