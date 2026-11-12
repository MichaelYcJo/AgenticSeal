# Design: 1794465690-a-passing-release-note-reads-like-a-failure

## Grounding

The tree as read at `3a75cc23d`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `seal/threads/1794465690-a-passing-release-note-reads-like-a-failure/routing.md` (read) | Planning framer, Implementation crafter, through the review chain, into `release/v0.38.0`. The version move rides on #1516, not here. |
| G2. Issue #1496, body and comments (executed: `gh issue view 1496 --json title,body,comments,milestone`) | The owner's choices of 2026-11-10 are settled and not reopened: layout C (no table; the seal floats left with `align="left"`, the badges follow, `<br clear="left">` ends the float; with no seal image the badges stand alone with no float) and colours C3. The issue has no comments. Its four *Done when* bullets are the acceptance below. |
| G3. `docs/releasing/branch-and-release.md` *Cutting a release*, the bullet *The release note publishes itself* (read) | The policy states the header as "an HTML table whose one cell holds the release's counts", the sealed header as "a table whose last cell holds the results", the badges "in two of the seal's reds", and the image as "a cell". Each of those sentences is stale after this work, and `## Rule changes` rewrites them. |
| G4. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work item's subject is the code: two scripts and their tests. So it states its policy changes in `## Rule changes` for the settle, and its pull request does not edit `docs/`. The issue's third *Done when* bullet (the document states the new layout and colours) is met when the settle after 0.38.0 writes the operations below. The ticket ranks below the policy, and the outcome is the same text, so this needs no person. |
| G5. `.github/scripts/release_seal.py:557-576` (read) | The seal finds the header by `note.header(work, closed, people)` and refuses unless `body.count(...)` is exactly 1, then replaces it with `body.replace(...)`. This reading stays. The new header must carry delimiters of its own, so that the substring count cannot match inside a longer line (Scope item 3). |
| G6. `.github/scripts/release_seal.py:40-50`, the docstring, and `tests/github/test_release_seal.py#test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded` (read) | A note edited by hand after publication, and a note a run already sealed, are left alone. This is the premise that keeps the exact-text reading (`frame/plan.md` *Alternatives considered*, row A7). |
| G7. `.github/scripts/publish_release_note.py:643-739` (read) | `table(*cells)` builds both headers. `header` holds the counts in words. `sealed_header` holds the image and the badges, or the badges alone. `badge(label, value)` colours every badge from the pair `BADGE_LABEL_COLOUR = "8e0c12"`, `BADGE_VALUE_COLOUR = "d42420"` (`:667-668`). The comment above that pair (`:659-666`) reads the two reds from `assets/seals/owl.svg`, which exists (executed: `ls assets/seals`). |
| G8. Badge labels (read: `release_seal.py#results`, `publish_release_note.py#count_badges`) | The badges carry these labels: `SEALED`, `commit`, `on` (the branch), `pull requests`, `issues`, `outside contributors`, `suite`, `skipped`, `review`, `work items`, `capped`, `deferred`. A source that cannot be read makes its value `not read` under the same label. |
| G9. Probe of GitHub's renderer, a table header with `border="0"` and `style` (executed: `gh api markdown -F text=@test_tmp_table.md -f mode=gfm -f context=<repo>`, scratch `<scratchpad>/1794465690-a-passing-release-note-reads-like-a-failure/frame/`) | GitHub's output kept `<table>`, `<tr>` and `<td>` and dropped `border` and `style`. This matches what the issue records from the release renderer on 2026-11-10, so the `/markdown` endpoint sanitizes as the release page does. The border cannot be turned off from the note. |
| G10. Probe: layout C on several source lines, with the seal alone on the first line (executed: same command, `test_tmp_sealed.md`) | GitHub reads a line that holds only `<img …>` as the start of a raw HTML block. Its output wraps each `<img>` in a `<p dir="auto">` of its own, so two badges written on one line stack, and each written `<br>` adds a blank line after its paragraph. This shape breaks "one or two to a line". |
| G11. Probe: layout C on one line, unwrapped and inside `<p>…</p>`, and the badges alone on one line (executed: `test_tmp_v1.md`, `test_tmp_v2.md`, `test_tmp_v3.md`) | The two shapes with the image render byte for byte the same: one `<p dir="auto">` holding the seal with `align="left"`, the badges parted by `<br>`, and `<br clear="left">` kept. Without the image, the badges render as one paragraph with no float. In every shape the theme renders as the next paragraph. |
| G12. Probe: the counts in words as `<p>…<br>…</p>` (executed: `test_tmp_words.md`) | GitHub renders it as one paragraph, with the `<br>` breaks kept and no border. |
| G13. The 0.37.5 note as published (executed: `gh api repos/<repo>/releases/latest -H "Accept: application/vnd.github.full+json"`) | Its raw body opens with the two-cell table, and every badge carries `-d42420?labelColor=8e0c12`. That is the shape this work replaces. A published note is never rewritten (`publish_release_note.py` docstring, *It never republishes*), so notes before 0.38.0 keep their tables. |
| G14. Readers of the header's shape (executed: `git grep -n '<table>\|\.header(\|sealed_header\|count_badges\|badge('` outside the two scripts and their two test files) | No other file reads the header's shape. `tests/behaviour/test_a_release_publishes_its_note.py` and `tests/behaviour/test_the_release_seal_is_drawn.py` read the workflow's steps, not the note. |
| G15. Statements that remain true (read: `templates/setup/config.md:463-468`, `skills/config/SKILL.md:57`, `.github/workflows/publish-release.yml:20-35`) | Each one says the header "shows it beside the results" or that the job "rewrites the note's header". Each one still holds under layout C, so none changes. |
| G16. Duplicates, libraries, cause (executed: `git grep -n 'labelColor\|shields'`; read: the imports of both scripts) | Nothing else in the tree builds a badge or colours one, so nothing can be extended instead. The scripts use only the standard library (`html`, `urllib.parse`), so no installed version is in question. The cause is shown by G9 and G13: the border belongs to the table, and the reds belong to the single pair of constants. |
| G17. `seal/follow-up.md`, `seal/parity.json`, `### Process changes` (read) | `seal/follow-up.md` has no rows. `seal/parity.json` is absent. The latest release, v0.37.5, has no `### Process changes` table, and none of the tables in the fragments under `seal/threads/` concerns the release note. |
| G18. `skills/settle/rule-changes.md` *A rule has one shape* (read) | Each operation below rewrites sentences inside the existing bullet, which has no bold rule sentence and no check line. After the settle, the policy sentence that follows each operation's `from:` still has the antecedent it has now, because no `to:` puts a new sentence between the two. The cases that hold the new text are named in *User scenarios & acceptance*. The proofer reads whether the bullet should carry a check line. |

## Scope

In:

1. `publish_release_note.py#header` writes the counts in words as one HTML paragraph on one line: `<p>`, each count line escaped and parted by `<br>`, then `</p>`. The note holds no `<table>`.
2. `publish_release_note.py#sealed_header` writes layout C in the same one-line paragraph. Given an image, the paragraph opens with the seal's `<img … width="W" align="left">`, the badge lines follow parted by `<br>`, and `<br clear="left">` ends the paragraph's text. Given no image, the paragraph holds the badge lines alone, with no `align` and no `clear`. One builder makes the paragraph for both headers and replaces `table`.
3. `release_seal.py#seal_release` finds and replaces the new header by the reading it uses now: `body.count(header) != 1` refuses, and `body.replace(header, replacement)` seals. Its local variable `table` is renamed `header`. The `<p>` and `</p>` that open and close the header are its delimiters. A note whose header line holds the seal's header inside a longer line (a count with one more digit, or one more count line) is refused, not replaced.
4. Every badge's two colours come from one table keyed by its label (colours C3). `SEALED`'s value colour is `d42420` and its label colour `8e0c12`. `suite`'s value colour is `2ea44f`. The value colour of `skipped`, `capped` and `deferred` is `6e7781`. Every label but `SEALED` has the label colour `555555`, and every other label's value colour is `0969da`. The pair `BADGE_LABEL_COLOUR` and `BADGE_VALUE_COLOUR` leaves.
5. The docstrings and comments of both scripts that state the old shape or the two reds are rewritten to state the new ones: `publish_release_note.py:29-33`, `table`'s docstring, `header`'s, the comment at `:659-666`, `badge`'s, and `sealed_header`'s; `release_seal.py:7-10`, `:116-118` and `results`' docstring.
6. `tests/github/test_publish_release_note.py` and `tests/github/test_release_seal.py` hold the new header in both its forms, the colours by label, and the delimiters' refusals (*User scenarios & acceptance*).
7. The policy text of G3 changes through `## Rule changes`, and the pull request leaves `docs/` as it is (G4).

Out:

- Rewriting a note already published. The publisher never republishes (G13), and the seal edits only a note whose header is still the generated one, so 0.37.5 and earlier keep their tables.
- The colours' contrast in either theme. The owner chose C3 after reading the rendered draft (G2).
- The version move, which #1516 carries (G1).
- `templates/setup/config.md`, `skills/config/SKILL.md` and `publish-release.yml`'s comment, which stay true (G15).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The note opens with its counts in a paragraph | Given a release of seven pull requests closing four issues, with two outside contributors. When `release_body` builds the note. Then it opens with `<p>7 pull requests merged<br>4 issues closed<br>2 outside contributors</p>`, a blank line, and then the theme. The note holds no `<table>`, and one pull request closing one issue reads in the singular with no contributors' line. | `tests/github/test_publish_release_note.py#test_the_note_opens_with_a_header_of_its_counts` and `#test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`, through their `header` helper and `HEADER` |
| S2. The sealed header floats the seal beside its badges | Given an image URL, alt text and a width. When `sealed_header` builds. Then the result is one line: `<p><img src="…" alt="…" width="W" align="left">`, the badge lines (each one's badges parted by one space, the lines parted by `<br>`), then `<br clear="left"></p>`. The URL and the alt text are escaped as they are now. | `tests/github/test_publish_release_note.py#test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`, whole-string |
| S3. With no image, the badges stand alone | Given no image. When `sealed_header` builds. Then the result is `<p>`, the same badge lines, then `</p>`, with no `align` and no `clear`. Removing the image `<img …>` and the `<br clear="left">` from S2's result gives this one. | `tests/github/test_publish_release_note.py#test_the_sealed_header_given_no_image_is_its_badges_alone` |
| S4. A badge's colours follow its label | Given each label in G8 and a label in no table entry. When `badge` builds. Then the address's colour field and its `labelColor` are those Scope item 4 gives the label, and a label with no entry takes label `555555` and value `0969da`. Seen red against the `badge` that read the one pair of constants. | `tests/github/test_publish_release_note.py#test_a_badge_takes_its_two_colours_from_its_label`, one parameter per label of G8, and `#test_a_badge_spells_its_label_and_value_as_the_service_reads_them` for a label with no entry; `tests/github/test_release_seal.py`'s `badge` helper and `BADGE_LINES` |
| S5. The seal replaces the paragraph header exactly once | Given a published note holding `header`'s paragraph once. When the seal job runs with the image on, and again with it off. Then the note's paragraph is replaced by S2's header, or by S3's, and nothing else in the note changes. | `tests/github/test_release_seal.py#test_accepts_a_published_note_and_replaces_its_header` and the no-image case beside it, through `HEADER` and `BADGE_LINES` |
| S6. The delimiters keep a longer header from matching | Given a note whose header holds one more count line than the seal computes (an outside contributors line), or one whose pull request count has one more leading digit (`12` where the seal computes `2`). When the seal runs. Then it refuses with `NOT_THERE`, and nothing is uploaded or edited. Seen red against a `header` that writes the count lines with no `<p>` and `</p>` around them. | two parameters of `tests/github/test_release_seal.py#test_refuses_on_any_failure_and_leaves_the_note_as_published`: `the note's header holds one more count line` and `the note's header holds one more digit` |
| S7. The guards that exist still hold | Given a note with the header absent, present twice, edited by one character, or already sealed. When the seal runs. Then it refuses as it does now. | `tests/github/test_release_seal.py#test_refuses_on_any_failure_and_leaves_the_note_as_published` (`the header is not there`, `the header is there twice`), `#test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded`, and `#test_a_second_run_finds_no_header_to_replace_and_writes_nothing` |
| S8. GitHub draws the layout | Given S2's and S3's one-line shapes. When GitHub renders them. Then the seal keeps `align="left"`, the paragraph keeps `<br clear="left">`, and the badges of one line sit side by side. | executed at framing through `gh api markdown` (G11). The release page itself is `frame/questions.md` Q1. |

## Data & interfaces

The note's first line, by `publish_release_note.py#header`, for counts `c1 … cn` (already escaped):

```
<p>c1<br>c2[<br>c3]</p>
```

The sealed header, by `publish_release_note.py#sealed_header`, for badge lines `L1 … Ln`, where each `Li` is its badges joined by one space:

```
<p><img src="URL" alt="ALT" width="W" align="left">L1<br>L2<br>…<br>Ln<br clear="left"></p>    (image)
<p>L1<br>L2<br>…<br>Ln</p>                                                               (no image)
```

Each header is one line, followed in the note by a blank line. A line that opens with `<p>` starts a raw HTML block, and the blank line ends it (G11, G12). The signature of `sealed_header(image_url, alt, width, sealed, results, work, closed, people)` stays as it is, and so does `header(work, closed, people)`.

A badge stays `<img src="https://img.shields.io/badge/{label}-{value}-{colour}?labelColor={edge}" alt="{label}: {value}">`, with `BADGE_URL`'s fields as they are. `colour` and `edge` are read from the table of Scope item 4 by the badge's label.

## Rule changes

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: The note opens with a header, an HTML table whose one cell holds the release's counts as text, one per line: the pull requests merged, the issues they closed, and the outside contributors where there are any.
  to: The note opens with a header, one HTML paragraph holding the release's counts as text, one per line: the pull requests merged, the issues they closed, and the outside contributors where there are any. The paragraph's opening and closing tags keep the seal from matching a longer line of counts, so the seal finds only the whole header.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: It runs the suite at the tag and replaces the note's header with a table whose last cell holds the results the stamp states, as badges, one or two to a line. They are the sealed version and commit, the pull requests merged, the issues closed, the outside contributors where there are any, the suite's counts, the work items and their review rounds, how many were capped, and the issues deferred.
  to: It runs the suite at the tag and replaces the note's header with a paragraph holding the results the stamp states, as badges, one or two to a line. They are the sealed version and commit, the pull requests merged, the issues closed, the outside contributors where there are any, the suite's counts, the work items and their review rounds, how many were capped, and the issues deferred. The header holds no table: GitHub draws a border around every table cell whatever the note's HTML asks, and in dark mode that border frames the seal in grey.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: A badge is a static image from the Shields badge service showing a label and a value in two of the seal's reds, and its alt text is that label and value in words.
  to: A badge is a static image from the Shields badge service showing a label and a value in colours read by its label from one table, so that a passing result does not read like a failure. Every label is grey except `SEALED`'s, which keeps the seal's dark red beside the seal's bright red value. The suite's passed count is green, the skipped, capped and deferred counts are grey, and every other value is blue. A badge's alt text is that label and value in words.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: and the table opens with a cell holding that image at its display width. Its alt text names the image alone, because the badges' alt text carries every number.
  to: and the header opens with that image at its display width, floated left so that the badges stand beside it, and ends with a line break that clears the float. The image's alt text names the image alone, because the badges' alt text carries every number.

- change
  file: docs/releasing/branch-and-release.md
  section: Cutting a release
  from: Under any other value nothing is attached and the table is the results' cell alone;
  to: Under any other value nothing is attached and the badges stand alone, with no float;

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The table builder | `.github/scripts/publish_release_note.py#table` | The one-line paragraph builder of Scope item 2, which both headers use |
| The one pair of badge colours | `.github/scripts/publish_release_note.py#BADGE_LABEL_COLOUR`, `#BADGE_VALUE_COLOUR` | The table keyed by label of Scope item 4. `SEALED`'s entry keeps the two reds, and the comment that reads them from `assets/seals/owl.svg` stays on that entry. |
| The docstring sentences that state a table, a cell or the two reds | `.github/scripts/publish_release_note.py:29-33`, `#header`, `#badge`, `#sealed_header`; `.github/scripts/release_seal.py:7-10`, `:116-118`, `#results` | Rewritten in place to state the paragraph and the colours by label (Scope item 5) |
| The local name `table` for the header the seal looks for | `.github/scripts/release_seal.py#seal_release` | Renamed `header`, because the value is no longer a table |
| The test pins of the table shape and the two reds | `tests/github/test_publish_release_note.py#header`, `#badge`, `#RESULTS_CELL` and the table strings in `#test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another`, `#test_the_sealed_header_given_no_image_is_its_results_cell_alone`, `#test_a_badge_spells_its_label_and_value_as_the_service_reads_them`; `tests/github/test_release_seal.py#HEADER`, `#badge` and the table strings in `#test_accepts_a_published_note_and_replaces_its_header` and the no-image case beside it | Rewritten to pin the paragraph and the colours by label (Scope item 6) |
| The policy sentences that state a table, a cell and the two reds | `docs/releasing/branch-and-release.md` *Cutting a release* | `## Rule changes`, written by the settle |

Framed 2026-11-12 by framer, before the build.
