# Design: #1299, each result in the release note's sealed header is a badge in the seal's reds

Every coordinate below was opened in the worktree at `64d09e81`, the tip of
`feat/1299-the-release-notes-results-are-plain-lines`, cut from
`release/v0.28.1` at `40e6c23e` (the v0.28.0 merge). The issue was read
with `gh issue view 1299 --json body,comments` on 2026-11-02 (executed). Its
comment list is empty, which matches the orchestrator's finding in the
spawn.

The note has two writers, named here by job as #1153's and #1204's designs
name them. `publish` is `.github/scripts/publish_release_note.py`, run by
the `publish` job of `.github/workflows/publish-release.yml`. `seal` is
`.github/scripts/release_seal.py`, run by the `seal` job after `publish`
created the release in the same run.

A badge here is a small image with two parts side by side: a label on the
left, a value on the right, each on its own background colour. The badges
come from the Shields badge service, which draws one from its URL alone and
keeps nothing. Its host is written in words in these records, never as a
domain, because `tests/censuses.py#real_identifiers` reads every tracked
file, records included, and refuses a domain outside `ALLOWED_DOMAINS`
(*Scope* item 4). GitHub's image proxy is likewise named in words.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| The issue's *The change*, *Decisions already made (owner, 2026-11-02)* and *What the frame decides* (executed: `gh issue view 1299`) | Built on. Each result becomes a static badge, a label and a value, in the seal's reds. The owner chose badges over a 3x2 grid of numbers and an aligned number column, ships them in 0.28.1, and leaves v0.28.0's published note as it is. The frame decides the labels, the colours, which badges share a line, the style, and the six points the issue lists. |
| `routing.md` (read) | `Automation` `yes`, `Planning` `framer`. No person is asked anything after routing, so every row of `questions.md` carries the default the build proceeds on. |
| v0.28.0's published note (executed: `gh release view v0.28.0 --json body`) | The right cell today is `<b>SEALED</b> v0.28.0 at 40e6c23e on main<br>10 pull requests merged<br>10 issues closed<br>the suite at 6328 passed and 12 skipped<br>10 work items over 32 review rounds<br>0 of them capped<br>0 issues deferred`, as the issue quotes it. The image cell's `src` names the repository's former name, which GitHub redirects; this work leaves the image cell as it is. |
| #1153, as its design states it (`seal/threads/1793589475-the-note-opens-with-the-owl-and-folds-each-category/frame/design.md` *Grounding* and *Scope* item 3, read): the image's `alt` text is `The <version> release seal` "because the second cell carries every number as text", and the header has "no frame, colour or style attribute of its own, so the text reads in the page's own theme", from #832's stamp on "the terminal's own background" | Built on for the numbers: each badge's `alt` text is its label and value in words, so a reader whose client draws no image still has every number, and the image's `alt` stays what it is. Departed from on colour, at the owner's decision in #1299: the badges carry the seal's reds. They are images, so the page's theme does not recolour them; their text is white on dark red and stays legible on a light and a dark page. |
| #1204, as its design states it (`seal/threads/1793593418-two-config-rows-show-the-seal-mark/frame/design.md` *Scope* item 4, read) and `release_seal.py#seal_release` (`:571-580`, read) | Built on. `Release note seal mark` decides only whether `seal` attaches the image and draws the image's cell. `sealed_header` builds both shapes from the same result lines (`publish_release_note.py:645-669`). The badges go in the results cell in both shapes (*Scope* item 1). |
| #1204's pull request mark, `skills/code-review/scripts/pr_body.py#MARK` (`:212`, read), and `git grep -n sealed_header` (executed) | The pull request mark is one `<img>` of the plugin's icon, and `pr_body.py` calls neither `sealed_header` nor `results`; only `release_seal.py:574` and `:578` and two test modules do. The pull request body renders no results cell, so it is out of scope. |
| #718, as `release_seal.py`'s docstring (`:38-50`) and `seal_release` (`:562-568`) state it (read) | Built on. `seal` never fails the release, and it edits the note only where `publish`'s header, `publish_release_note.py#header`, stands in it exactly once. After the first run the note holds the sealed header, so a re-run finds no such header, uploads nothing and edits nothing. `header` and `counts` are not changed here, so the text the guard looks for is unchanged, and a sealed header made of `<img>` tags cannot hold it. |
| #832 and #857, as `release_seal.py`'s docstring (`:14-22`) and `assets/seals/README.md` *The little owl — from 0.25.1* state them (read) | Built on. The image is the plugin's icon, `.claude-plugin/icon.png`, drawn from `assets/seals/owl.svg`, copied byte for byte. Nothing in the image, its width or its `alt` changes. |
| Executed 2026-11-02: the icon's pixels decoded with a stdlib PNG reader in the probe directory, counting opaque colours, and `grep` on `assets/seals/owl.svg` for its fills | The icon is 512 by 512 with 185,088 opaque pixels. Its most common colour is `#d42420`, 29,122 pixels exactly: the raised relief of the owl and the fret border, `owl.svg`'s `fill="#d42420"` (line 18). The wax's dark outer edge is `owl.svg`'s gradient stop `#8e0c12` (line 3), 3,087 pixels within 6 of each channel. These two are the badges' value and label colours (*Data & interfaces*). |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | Weighed for the new dependency. The badge host is no gate, check or step: no job calls it, because a badge is a URL written into the note and fetched only by a reader's page. So it can fail no job and turns nothing red. What it costs is a reader's page depending on an outside host for the cell's look; what a reader sees when the host or the proxy fails is below, and every number survives in the `alt` text. It is kept on the owner's decision and on that cost. `## Removes` names what goes in return. |
| Executed 2026-11-02: `curl` on the Shields host's `/badge/<label>-<value>-<colour>` path with `?labelColor=8e0c12`, reading each SVG's `<title>` and fills | `suite-6328%20passed-d42420` draws `suite: 6328 passed` with fills `#8e0c12` and `#d42420`. `a--b__c%20d-x--y__z%20w-d42420` draws `a-b_c d: x-y_z w`, so a doubled `-` and a doubled `_` are each one literal character and `%20` is a space. `on-release%2Fv0.28.1-d42420` draws `on: release/v0.28.1`. `odd-50%25%20%26%20%23%20%3F-d42420` draws `odd: 50% & # ?`. Each answered 200 `image/svg+xml`. |
| Executed 2026-11-02: `curl` on the Shields host's `/static/v1?label=&message=&color=&labelColor=` form, with `urlencode` and `quote` spellings of `+` and spaces | The query form draws the same values with no doubling, `+` written `%2B` included. It is the alternative `plan.md` A2 weighs. |
| Executed 2026-11-02: `curl -sI` on a badge from the Shields host | `cache-control: max-age=432000, s-maxage=432000`: a badge may be cached for five days. A badge's URL holds its whole content, so a cached badge is never stale. |
| Executed 2026-11-02: `gh api -X POST markdown -f mode=gfm -f context=MichaelYcJo/SpecSeal` over a two-cell table holding an image and three badges, two on one line | GitHub's renderer keeps each `<img>` with its `alt`, moves the badge URL to `data-canonical-src`, points `src` at its image proxy, and wraps each image in a link to the proxied address. The `<br>` and the space between two badges stay. |
| Executed 2026-11-02: `curl` on the proxy addresses that render gave | The proxy serves the badge as 200 `image/svg+xml` with the same five-day cache header and the same `<title>`. For an origin that answers 404 (`https://example.com/seal.png`), the proxy answers 404 `text/plain`, so a reader's browser gets no image there. |
| Executed 2026-11-02: the same render over an `<img>` with a `data:` URI and a `<span style>` | The renderer drops the `data:` URI's `src` and the `style` attribute. A badge drawn inline, or a cell coloured by style, does not reach a reader; an image at an outside address is the only way the cell gets colour (`plan.md` A5, A6). |
| What a browser shows for an image the proxy cannot serve (unverified: no browser runs in this environment; answerer a measurement, `questions.md` Q1) | The assumption is that the browser shows the `alt` text in the image's place, as browsers do for a broken image. The build is the same either way: the `alt` text carries the number whatever the browser draws. |
| `tests/censuses.py#ALLOWED_DOMAINS` (`:885-891`) and `#refused_domains` (`:915-934`), and `tests/test_censuses.py:959` (read) | Every tracked file is swept, and a domain outside the list is refused. The list's comment says a domain "joins `ALLOWED_DOMAINS` by a deliberate edit, never to make a test pass", and `w3.org` and `claude.com` stand there for a real service the files must name. The badge host joins on the same grounds (*Scope* item 4, `plan.md` A10). |
| Policy in force on the seal job's header: `docs/branch-and-release.md` *Cutting a release* (read) still holds the glance-table sentences, and the unsettled designs change them in merge order: #1153 (`4ab345cba`, #1294), then #1204 (`50673927c`, #1297) (executed: `git log` on both designs; `git grep` of `section: Cutting a release` across `seal/threads/*/frame/design.md`) | The sentences in force are #1204's `to` values. `## Rule changes` below quotes them as its `from` values. #1139's operation on the same section touches the entries' links, which this work leaves. |
| The cases that pin today's shape (read): `tests/github/test_publish_release_note.py#Test_main::test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another` (`:877-924`) and `#test_the_sealed_header_given_no_image_is_its_results_cell_alone` (`:926-950`); `tests/github/test_release_seal.py` `#test_accepts_a_published_note_and_replaces_its_header` (`:669-742`), `#test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone` (`:744-778`), `#test_a_dry_run_draws_and_prints_and_writes_nothing` (`:941-1000`, the line `<b>SEALED</b> ...<br>` at `:964`) and `#Test_module::test_the_results_are_the_stamps_rows_in_words` (`:1011-1036`) | Each pins the prose lines this work replaces, and each is rewritten to the badge lines (*Scope* item 6). `#test_a_second_run_finds_no_header_to_replace_and_writes_nothing` (`:780-801`) asserts no shape of the sealed header, so it stands unchanged as the re-run's case. |
| The milestone `release: 0.28.1`'s description (executed: `gh api .../milestones`) and `grep -n` of `publish_release_note.py` (executed) | #1283 may edit the `git log` calls, which sit at `:188-266` (`git`, `previous_tag`, `commit_range`, `fragments`, `pull_request`). The header helpers sit at `:611-669`. This work's edits in the file stay in `plural`, `counts`, `table`, `header`, `sealed_header` and new helpers beside them, plus one import line, so the two merge without a conflict in the same lines. |
| v0.28.0's `### Process changes` (executed: `gh release view v0.28.0`), and `seal/follow-up.md` (read) | The three process rows concern the proofer's notices, the settle's unmeasured rows and the second `seal pr-body` run; none bears on the note's header. No follow-up row waits on this work. |

## Scope

In scope:

1. **Each result in the sealed header's results cell is a badge.** In
   `publish_release_note.py`, `sealed_header` writes each line of the
   results cell as one or two badges, side by side, parted by one space;
   lines stay parted by `<br>` through `table`. Each badge is an `<img>`
   whose `src` is the Shields `/badge/<label>-<value>-<value colour>` path
   with `?labelColor=<label colour>`, and whose `alt` is the label, a colon,
   a space and the value. The lines and their badges, in order, are in
   *Data & interfaces*. The results cell is the same in the two-cell header
   and in the one-cell header #1204 builds where the image is off. The
   image's cell, its `alt` and its width are unchanged.
2. **Each label and value is encoded so it means the same in the URL.**
   Each `-` is doubled, then each `_` is doubled, then the text is
   percent-encoded with nothing left safe (`urllib.parse.quote(text,
   safe="")`), so a space is `%20`, a `/` is `%2F` and a `%` is `%25`. The
   `alt` text is then HTML-escaped as every attribute in the header is
   today; the URL needs no escape, because the encoding leaves no character
   HTML reads.
3. **`release_seal.py#results` hands the stamp's results as labelled
   values, not as phrases.** It returns the same two parts it returns today,
   the sealed part and the other results, each as badge lines: lists of
   `(label, value)` pairs. A row not read gives the value `not read` for
   each badge it feeds. `release_rows`, `LABELS` and the dry run's printed
   rows are unchanged.
4. **The badge host joins `tests/censuses.py#ALLOWED_DOMAINS`**, with a
   comment saying it is the host the release note's badges are drawn by
   (#1299), as `w3.org` and `claude.com` carry theirs.
5. **`publish`'s own header is unchanged.** `header` and `counts` keep
   their text, because `header`'s text is what `seal` finds and replaces,
   and because a note whose seal did not run keeps its counts as text.
6. **The cases that pin the prose lines are rewritten to the badge lines**,
   each new or changed assertion seen red before the change it pins:
   the six cases *Grounding* lists, plus a case for the encoding (S4).
   The `alt` text (S3) is pinned by S1's whole-string assertion.
7. **The code's own text states the badges**: `sealed_header`'s docstring
   (`publish_release_note.py:646-659`), `results`' docstring
   (`release_seal.py:186-193`), the comment above `LABELS`
   (`release_seal.py:115-123`), and the comment at the top of
   `publish-release.yml` (`:30-31`, "a table of the stamp's results as
   text").
8. **The policy text changes through `## Rule changes`**, which the settle
   after the release writes.

Out of scope:

- v0.28.0's published note and every note before it. `publish` never
  republishes, and nothing here edits a published release (the owner's
  decision).
- The pull request body's seal mark (#1204). It is the icon alone and
  renders no results cell (*Grounding*).
- The image's cell: the PNG, its `alt`, its width, and the row that turns
  it on.
- `publish`'s header and the counts' words in it (*Scope* item 5,
  `plan.md` A9).
- The `git log` calls in `publish_release_note.py`, which #1283 owns.
- The grid of numbers and the number column (the owner's decision).
- A colour of its own for a value not read (`plan.md` A8), and a badge
  style other than the service's default (`plan.md` A11).
- The terminal stamp and every file it runs from.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the two-cell header is badges | Given `RELEASE`'s pull requests, a sealed part and results as `results` returns them, and an image URL. When `sealed_header` builds the header, then the first cell is the image as today, and the second holds the badge lines of *Data & interfaces* in order, each badge's `src` and `alt` exactly as given there, lines parted by `<br>` and badges on a line by one space. | The rewritten `tests/github/test_publish_release_note.py` case pinning the whole string, seen red against today's `sealed_header` |
| S2 the one-cell header is the same cell | Given the same input and no image. Then the table's one cell is byte for byte the two-cell header's second cell. | The rewritten no-image case in the same module |
| S3 every number is in the `alt` text | Given the header S1 builds. Then each badge's `alt` attribute holds its label and value, as `label: value`, in order, the outside contributors included where there are some. | S1's whole-string assertion, which pins every `alt` attribute byte for byte, seen red with the `alt` attribute alone left out of the badge |
| S4 a value with `-`, `_`, a space and other separators keeps its meaning | Given a label and a value holding `-`, `_`, a space, `/`, `%`, `&`, `?`, `#`, `<` and `"`. When the badge is built, then reading its `src` by the Shields path grammar (split the badge segment at each single `-`, read `--` as `-`, `__` as `_`, a single `_` as a space, then percent-decode) gives back the label, the value and the colour exactly. | A new case in the same module, its decoder written in the case; seen red against an encoder that percent-encodes alone without doubling. The service's own reading of the doubled form is the framer's probe (*Grounding*) |
| S5 the stamp's results are labelled values | Given `tests/github/test_release_seal.py#ROWS`. When `results` reads them, then the sealed part and the other results are the pairs of *Data & interfaces*; given rows with every tree source not read, the review, work items, capped and deferred values are each `not read`. | The rewritten `#Test_module::test_the_results_are_the_stamps_rows_in_words` |
| S6 a note built for a test tag carries the badges | Given the note `publish` writes for the test tag `v1.2.3`, under the row `yes` and under the row absent. When `seal`'s `main` runs, then the edited note's header is the badge header of that shape, every other byte of the note unchanged. | The rewritten `#test_accepts_a_published_note_and_replaces_its_header` and `#test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone` |
| S7 a re-run of `seal` leaves the header | Given the note as the first run left it, under either answer of the row. When `seal` runs again, then it uploads and edits nothing and names the header it did not find. | `#test_a_second_run_finds_no_header_to_replace_and_writes_nothing`, unchanged and green |
| S8 the census reads the badge host as allowed | Given the build's tree. When the census sweep reads every tracked file, then no line naming the badge host is refused. | `tests/test_censuses.py`, in the broad gate |
| S9 the rule changes parse | `skills/settle/scripts/rule_changes.py#parse` reads `## Rule changes` with no refusal, and `apply_op` places each operation on the section as #1204's operations leave it. | Executed by the framer in a scratch clone (`plan.md` *Technical context*), and by `seal chain-check` at the pull request |

## Data & interfaces

**Colours**, two constants in `publish_release_note.py`, read from the
icon (*Grounding*):

| Part | Colour | Where it is in the seal |
|---|---|---|
| the label, left | `8e0c12` | `assets/seals/owl.svg`'s wax gradient, its outer stop: the seal's dark edge |
| the value, right | `d42420` | `owl.svg`'s relief fill, and the icon's most common colour: the raised owl and border |

**One badge**, for the label `suite` and the value `6328 passed`, the host
written here in words:

```
<img src="https://<Shields image host>/badge/suite-6328%20passed-d42420?labelColor=8e0c12" alt="suite: 6328 passed">
```

The service's default style is used, so the URL carries no `style`
parameter, and the text keeps its case as written.

**The results cell's lines**, for v0.28.0's numbers, one bracket per badge:

```
[SEALED | v0.28.0]
[commit | 40e6c23e] [on | main]
[pull requests | 10 merged]
[issues | 10 closed]
[outside contributors | 2]            only where there are some
[suite | 6328 passed] [skipped | 12]
[review | 32 rounds] [work items | 10]
[capped | 0] [deferred | 0]
```

- The first two lines are `results`' sealed part: the version, and the
  tagged commit with each branch `release_rows` continues it with. The
  commit is the eight characters `release_rows`' `tag` row holds.
- The next two or three lines are `publish`'s counts, built beside
  `counts` from the same `work`, `closed` and `people`.
- The last three lines are `results`' other part. `review` is the rounds
  with `plural`'s singular for one; `capped` and `deferred` are the counts
  alone, as the owner's sketch writes them.
- Not read: `review` and `work items` both read `not read` where the items
  row is not read; `capped` and `deferred` each read `not read` where their
  row is not.

**Interfaces.**

- `publish_release_note.py#sealed_header(image_url, alt, width, sealed,
  results, work, closed, people)` keeps its parameters. `sealed` and
  `results` become lists of badge lines, each a list of `(label, value)`
  pairs. It returns the table as today, through `table`.
- New beside it, in the same file: the two colours, the badge URL's shape,
  the encoder of S4, the builder of one badge, and the builder of the count
  lines. Their names are the builder's.
- `release_seal.py#results(rows)` returns `(sealed, lines)` as badge lines.
- `header`, `counts`, `table` and `release_rows` keep their signatures and
  their output.

## Rule changes

- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: It runs the suite at the tag and replaces the note's header with a
    table whose last cell holds the results the stamp states, as text, one
    per line.
  to: It runs the suite at the tag and replaces the note's header with a
    table whose last cell holds the results the stamp states, as badges, one
    or two to a line.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: the work items and their review rounds, how many were capped, and
    the issues deferred.
  to: the work items and their review rounds, how many were capped, and
    the issues deferred. A badge is a static image from the Shields badge
    service showing a label and a value in two of the seal's reds, and its
    alt text is that label and value in words. So a reader whose client
    draws no image, or who opens the note while the service does not
    answer, still has every result.
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: Its alt text names the image alone, because the results' cell
    carries every number.
  to: Its alt text names the image alone, because the badges' alt text
    carries every number.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The phrases `results` composes from the rows: "the suite at … and …", "… work items over … review rounds", "… of them capped", "… deferred", and the "work items not read" family | `.github/scripts/release_seal.py#results` | The labelled pairs of *Data & interfaces*: the label carries what the phrase said around the number. |
| The bold `SEALED` text line and the prose lines of the results cell | `.github/scripts/publish_release_note.py#sealed_header` | The `SEALED` badge and the badge lines, in the same function. |
| The docstring sentences on prose lines: `sealed_header`'s "the stamp's results one per line, as the stamp sets them beside its disc: `SEALED` in bold", `results`' "in the phrases of the alt text written by hand for 0.17.0's seal", the `LABELS` comment's "they reach the note as the lines beside it in the header's second cell", and the workflow comment's "a table of the stamp's results as text" | `publish_release_note.py:646-659`, `release_seal.py:120-123` and `:186-193`, `.github/workflows/publish-release.yml:30-31` | The same places, rewritten to the badges (*Scope* item 7). |
| The test pins of the prose lines | the six cases *Grounding* lists in `tests/github/test_publish_release_note.py` and `tests/github/test_release_seal.py` | The same cases, rewritten to the badge lines (*Scope* item 6). |
| The policy sentences stating the results as text, one per line | `docs/branch-and-release.md` *Cutting a release*, as #1204's `to` values leave it | `## Rule changes` above, written at the settle, never by this pull request. |
| What the badges take out in return for the outside host they add | none | The badges add no gate, check, hook, step or line grammar: no script reads a badge, and no job calls the host. What they replace is the phrase composition above, which goes in full. The census allowlist gains one host by the list's own route (*Scope* item 4); nothing in the census can go for it, since every other entry still has a file that names it. |

Framed 2026-11-02 by framer, before the build.
