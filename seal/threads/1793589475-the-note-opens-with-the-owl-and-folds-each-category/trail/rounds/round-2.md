# Review round 2: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

```seal
target: f02aed992, fixes 3b82bbf31..f02aed992
```

This is a verifying round. It reads the diff of the fix pass and the frame
folds around it, `3b82bbf31..f02aed992`, in a `git clone --no-local` of the
worktree at `f02aed992`. `seal/parity.md` is not declared, so the round block
has no `original:` line.

Carried from round 1, not re-established: the base `bf18be7d1`, and what
GitHub's renderer does with a lone closing `details` tag inside a fold's list
item (it closes the fold there, round 1's third probe). Re-established this
round: the escape-removed mutant, the list of merged titles (now 320), and
what GitHub's renderer does with each title shape the escape might miss.

## Findings

None. Round 1's one finding is confirmed closed below, and the fix diff
holds no new defect worth a finding. The edges this round found are listed
under `## Not judged` with the grounds for not raising them.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed 789522175` holds. The fix pass claimed that
removing the escape alone turns all three title cases red. This round wrote
that mutant again in the clone: `kind_and_text`'s return at
`.github/scripts/publish_release_note.py:563` changed to `return heading,
text`, and nothing else. It ran the render case and the two bare-tag cases
alone, and all three failed, exit 1 (executed). The render case failed at
`tests/github/test_publish_release_note.py:680`: the reader returned an
empty fold `('', [])` at index 1 where the Fixes fold with #1293's line was
expected, so #1293's bare tags were read as folds. Both bare-tag cases
failed at `:693`, the first assertion: the body held `- A bare` followed by
the raw tag, not by `&lt;`. These are the lines the fix pass named. The line
was then restored, and the module passed with
`tests/github/test_close_issues_on_release.py`, 95 cases, exit 0 (executed).

The code does what the frame folded in. `SPAN_OR_LT_RE` (`:544`) wraps
`close_issues_on_release.py#SPAN` in one group, and `SPAN` has no group of
its own and no flags (`.github/scripts/close_issues_on_release.py:123`,
read). So `m.group(1)` is the code span when one matched and `None` when the
match was a lone `<`. The scan is left to right, so a `<` before a backtick
is escaped before any span starting at that backtick is read. The two
callers are the fold lines (`:715`) and the thanks section (`:593`), and no
other line of the module writes a title into the note (read: every `title`
line in the module). The count of 0 in 318 and the limit sentence are gone
from `release_body`'s docstring (`:696-703`) and from the changelog fragment
(`changelog.md:3`, read). A title holding `<details>` or `</details>`, bare,
in a code span of one or two backticks, or in a triple-backtick span, comes
back from GitHub's renderer as text or code inside one list item of a whole
fold (executed, the second probe below). This round did not send #1293's
own title to GitHub's renderer; round 1's fourth probe sent its escaped form
and recorded it as text.

So no well-formed title opens or closes an element through a tag it quotes.
Two malformed shapes still do, and they are named under `## Not judged`.

```seal
confirms: none
```
What matched: the new case is read against its group, and it covers what
the group does not. The render case
(`tests/github/test_publish_release_note.py:661-680`) holds #1293, whose
title pairs its tags, and reads the folds only. The new case (`:682-701`)
holds a lone opening tag and a lone closing tag. It asserts the escaped
text in the thanks line (`### Thanks to`), which no other case in the module
checks. It also asserts the raw `&lt;` in the body, which the render case
does not, since that case reads the folds as rendered text. The fix pass
also claimed a second mutant, one that escaped inside code spans too, was
red at `:680`. By reading, it is: a code span keeps `&lt;` literally, so
#17's line would read `A title quoting &lt;/details> (#17)` and miss the
expected list (read, not run).

```seal
confirms: none
```
What matched: the frame folds at `c835b4cbd` and `f02aed992` state what the
code does. The design's *Scope* item 5 (`frame/design.md:70-80`) says each
`<` outside a code span becomes `&lt;` and fragments are not escaped. The
plan's A6 row now reads "Rejected for fragments and for reading a tag", and
its *Judgments of the run* row cites `skills/core/SKILL.md` as what it was
judged against. The design's *Grounding* row keeps its dated count of 0 in
318 as the result of a probe run on that date, and names #1293 as the title
that came after. That row records a probe, not a stored number the code
rests on (all read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| `ruff check` and `ruff format --check` on the two changed Python files. The fix pass claimed exit 0. The clone's test environment has no `ruff`, and none is on the path, so this round did not run them | `.github/scripts/publish_release_note.py`, `tests/github/test_publish_release_note.py` | the orchestrator, by `seal gate` after the rounds settle |
| The full suite, the repository-wide lint and the format check at HEAD, still labelled not verified with the orchestrator as answerer (`gaps.md` *Not verified*). The label is honest | the branch at its head | the orchestrator, by `seal gate` after the rounds settle |
| Round 1's rows on the releases page's layout of the header and on a real `gh release edit`, carried unchanged; the fix diff does not touch them | the 0.28.0 note on the releases page | the orchestrator of the 0.28.0 release, after the `seal` job |

Edges judged not worth a finding, with their grounds:

- **A malformed code span still lets a tag through.** `SPAN` reads a code
  span as a backtick run of one or two, and CommonMark reads one as a run
  closed by a run of the same length, with a backslash before a backtick
  making it no opener. Where the two disagree, the escape leaves the `<` raw,
  and the renderer reads a tag. Two shapes were sent through GitHub's
  renderer (executed, the second probe below). A title holding a
  backtick, an opening `details` tag and then two backticks, and a title
  holding a backslash and a backtick before the same, each came back with a
  `Details` widget inside its list item. The fold stayed whole, and the
  `AFTER` line stayed outside it. A closing tag in either shape would close
  the fold early, as round 1's lone-tag probe showed. A triple-backtick
  opener with a double-backtick closer is a third shape of the same cause
  (read against `SPAN`, not run). None of the 320 merged titles holds any of
  these shapes. Only #1293 holds a `<` at all, and none holds a backslash
  before a backtick (executed, the title list below). The cost if it ships
  is one line of one note, for a title whose own Markdown is already broken,
  and a `gh release edit` fixes it. The docstring's claim that a quoted tag
  "opens or closes no fold" holds for every title whose code spans
  CommonMark and `SPAN` read alike. A reader that follows CommonMark's
  run-length and backslash rules would close the gap, and it would be a
  second code-span reader beside `SPAN` for a shape no title has held.
- **An autolink in a title now renders as a broken link.** Before the fix,
  a title holding `<https://example.com>` rendered as a link. Now its `<` is
  written `&lt;`, and GitHub's extended autolink takes the trailing `>` into
  the address, so the link points at the address followed by `%3E`
  (executed, the second probe below). None of the 320 merged titles holds a
  `<` followed by an address. A conventional-commit subject names an issue
  or a file, not an address in angle brackets.
- **A backslash before a `<` now shows `&lt;`.** A title holding
  `\<details>` showed `<details>` before the fix and now shows `&lt;details>`
  as text, because the backslash escapes the `&` the fix wrote (executed,
  the second probe below). No element opens either way. No merged title
  holds the shape. A title's `&` entities are read as Markdown before and
  after the fix alike, so that is outside the fix diff.
- **`frame/plan.md` cites itself.** Its *Technical context* section
  (`frame/plan.md:42-43`) cites `frame/plan.md` *Judgments of the run* from
  inside `frame/plan.md`, and the line runs past the paragraph's wrap. Both read correctly and no agent acts on them
  wrongly.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_publish_release_note.py -p no:xdist -q -k "each_fold_as_one_element or bare_tag_in_a_title"` in the clone with `kind_and_text`'s return written `return heading, text` through the `Edit` tool | 3 failed, 46 deselected, exit 1. The render case failed at `:680` with `('', [])` at index 1 in place of the Fixes fold. Both bare-tag cases failed at `:693`. The line was restored afterwards. |
| `bin/test tests/github/test_tmp_round2_edges.py -p no:xdist -q -s`, a probe that ran `kind_and_text` over ten title shapes, wrote them as one fold's lines followed by an `AFTER` line, and rendered the note with `cmarkgfm` keeping raw HTML; then `gh api -X POST markdown -f mode=gfm -F text=@edges.md` on the same note | 1 passed, exit 0; then exit 0. In both renderers, the bare tag, the one-, two- and three-backtick spans and the escaped tag came back as text or code. The two malformed-span shapes kept a raw `details` tag, which GitHub's renderer returned as a `Details` widget inside the list item. The autolink came back with an address ending in `%3E`, and the backslash shape as the text `&lt;details>`. GitHub's renderer closed the fold after its last line, with `AFTER` outside it. The probe file and `edges.md` were deleted afterwards. |
| `gh pr list --state merged --limit 3000 --json number,title`, matched for any `<`, for a backslash before a backtick, and for `<http` | 320 merged titles. 1 holds a `<`: #1293. 0 hold a backslash before a backtick. 0 hold `<http`. |
| `bin/test tests/github/test_publish_release_note.py tests/github/test_close_issues_on_release.py -q` in the clone at `f02aed992` | 95 passed, exit 0. This is a narrow run of two modules, not the broad gate. |
