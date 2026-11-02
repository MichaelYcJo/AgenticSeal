# Review round 1: 1793599990-each-result-is-a-badge

```seal
target: f6772422 against release/v0.28.1
```

The target is the branch `feat/1299-the-release-notes-results-are-plain-lines`
at `f6772422` against `release/v0.28.1`, resolved as `origin/release/v0.28.1`
at `40e6c23e`. Every coordinate below was opened in a `git clone --no-local`
of the branch worktree at `f6772422`. No earlier round exists, so no fact was
carried and every fact here was established this round. No `seal/parity.md`
is declared, so the round block carries no `original:` line.

The documents read in stage 1 were issue #1299 (executed: `gh issue view
1299`), `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `trail/phases/phase-1.md` and
`changelog.md`, and the rule changes of #1153 and #1204 on the same two
sections. The axes walked were inputs (the rows `release_rows` builds),
exclusions and boundaries (a row not read, a suite split over two rows, a
value holding the address's separators), response shape (the cell's lines,
badge order, the one-cell header), error paths (`results` raising inside
`seal_release`), security (escaping of every attribute), and two axes of
this change's own: the outside host a reader's page now depends on, and the
census of real domains.

## Findings

### 1. The sealed header case carries a parser and two assertions that cannot fail while the assertions above them pass

```seal
severity: should
location: `tests/github/test_publish_release_note.py:311-341`, `tests/github/test_publish_release_note.py:982-988`, `tests/github/test_publish_release_note.py:1014-1016`
evidence: read `tests/github/test_publish_release_note.py:311-341`, `tests/github/test_publish_release_note.py:945-1016`, `seal/threads/1793599990-each-result-is-a-badge/trail/phases/phase-1.md:435-443`
```

Why it matters: the phase record claims that S3 needs no case of its own,
because "S1's case already pins the whole header string, every `alt`
attribute included, so a separate case would cover nothing its group does
not". That reasoning is right, and it applies equally to what was built in
the case's place. At `tests/github/test_publish_release_note.py:976-981` the
case asserts that `sealed` equals one exact string, `RESULTS_CELL` included.
The assertion at `:983-988` then feeds that same string to `Unimaged` and
compares the result with a constant. A string equal to a fixed literal always
parses to the same cells, so `:983-988` can fail only when `:976-981` has
already failed. The same holds for `odd`. The assertion at `:1001-1013`
checks a substring that runs from the first cell's `<td>` to the second
cell's closing `</td>`. So `unimaged(odd)[1]` at `:1014-1016` is fixed by
it. Neither assertion can catch a mutant the exact-string assertions miss.
Commit `9d693098` rewrote the docstring from "the alt reading seen red with
the badge's alt attribute alone left out" to a sentence that credits the
whole case with that red. That fits this reading: with the `alt` attribute
removed, the exact string fails first and the reading never runs.

The cost is the class `Unimaged` and the function `unimaged`, 31 lines of
test helper at `:311-341`, plus two assertions that a later editor has to
keep in step with `RESULTS_CELL` for no coverage. The proofer definition's
rule *Each new test is read against its group* makes an assertion that
covers nothing its group does not already cover a `should` finding.
`html.parser` stays imported, because `Folds` at `:367` uses it.

The fix removes the helper and the two assertions. It also states in the
docstring where S3 is pinned:

```python
# Delete tests/github/test_publish_release_note.py:311-341, the block from
# `class Unimaged` through `return reader.cells`, with the two blank lines
# after it, and the two assertions:
#   :982-988  `# The page read with no image drawn ...` and `assert unimaged(sealed) == [...]`
#   :1014-1016  `assert unimaged(odd)[1] == (...)`
# In the case's docstring, replace
#   "Each badge's alt text is its label
#    and value, so a reader whose client draws no image reads every
#    result in words."
# with
#   "Each badge's alt text is its label and value, so a reader whose client
#    draws no image reads every result in words; the whole-string assertion
#    pins every alt attribute, which is #1299 S3."
```

```seal
verdict: fixed 2a82f15a
answer: The finding holds: a string equal to a fixed literal always parses to the same cells, so neither reading could fail while the exact-string assertions above it passed. `Unimaged`, `unimaged` and both assertions are removed, and the docstring now says the whole-string assertion pins every alt attribute, which is #1299 S3, in the fix's words merged with finding 2's sentence. `trail/phases/phase-1.md` and `frame/design.md` S3 still describe the parser reading; the hand-back names both.
```

### 2. The sealed header case's docstring says every badge is escaped, and the badge's address is not

```seal
severity: should
location: `tests/github/test_publish_release_note.py:957-958`
evidence: read `tests/github/test_publish_release_note.py:945-961`, `.github/scripts/publish_release_note.py:667-682`, `.github/scripts/publish_release_note.py:710-713`
```

Why it matters: commit `ddbef6c1` removed `html.escape(url)` from `badge`.
In the same commit it rewrote two sentences. `badge`'s docstring now says
"The address needs no escape" (`.github/scripts/publish_release_note.py:672-675`).
`sealed_header`'s "as `badge` escapes each badge" became "as `badge` escapes
each badge's alt text" (`:712-713`). The same claim in the test that pins
this shape was left standing. At
`tests/github/test_publish_release_note.py:957-958` the docstring says "The
URL, the alt text and every badge are escaped, so a quote cannot end an
attribute and a `<` opens no tag". An agent reading the case for what it
pins is told that it pins an HTML escape of each badge. The code says the
opposite, and a later editor could put the escape back on that reading.
Contract rule 19 asks that a change remove every sentence stating the old
fact in the same commit. The two in the script were found and this one was
not.

```python
        result in words. The image's URL and alt text, and each badge's alt
        text, are escaped, so a quote cannot end an attribute and a `<` opens
        no tag; a badge's address is percent-encoded and needs no escape.
```

```seal
verdict: fixed 2a82f15a
answer: The finding holds: `sealed_header` escapes the image's URL and alt and `badge` escapes only each badge's alt text. The docstring now says so and that a badge's address is percent-encoded and needs no escape, which is the fix's sentence rewrapped. `git grep` for the old wording and for `escapes each badge` finds no other place stating it.
```

## Confirmations

```seal
confirms: none
```
What matched: the crafter's count. `bin/test` over
`tests/github/test_publish_release_note.py` and
`tests/github/test_release_seal.py` gave 106 passed with exit 0 at
`f6772422` (executed). The census module and the two release behaviour
modules gave 181 passed with exit 0 (executed).

```seal
confirms: none
```
What matched: the escape departure (`trail/phases/phase-1.md:445-454`)
holds. `urllib.parse.quote(text, safe="")` leaves only ASCII letters,
digits and `_.-~` unencoded, so `badge_text`
(`.github/scripts/publish_release_note.py:658-664`) never emits `&`, `"`,
`<` or `>`. `BADGE_URL` (`:655`) holds only `:/?=` and the two colour
constants. An HTML escape of the address therefore changes no byte, so
removing it removes nothing (read). The alt text keeps its escape at `:682`,
and the `odd` input pins it at
`tests/github/test_publish_release_note.py:1001-1013` (read).

```seal
confirms: none
```
What matched: `results` cannot raise on the suite unpacking. The claim is
that the suite always has two parts
(`.github/scripts/release_seal.py:206-209`). `release_rows` writes it either
as `P passed, S skipped` in one row or as `P passed` and `S skipped` in a row
and its continuation (`:160-164`). Both split into exactly two parts
(read). Should the shape ever change, `main` catches every exception and
exits 0 (`:611`), so the release still does not turn red (read).

```seal
confirms: none
```
What matched: the badge values match *Data & interfaces*. `review` carries
`plural(rounds, 'round')` from the items row (`.github/scripts/release_seal.py:174`).
So one round reads `1 round`, which `tests/github/test_release_seal.py:282-284`
pins. `capped` takes the `C` of `C of N` and `deferred` the count of
`N issues`. When the items row is not read, both `review` and `work items`
read `not read`, and when the capped or deferred row is not read, its own
badge reads `not read` (`:212-221`). The rewritten case pins all of it at
`tests/github/test_release_seal.py:1043-1060` (read, and executed in the
106).

```seal
confirms: none
```
What matched: the re-run guard is unchanged. `header` and `counts` keep
their output (`.github/scripts/publish_release_note.py:615-644`, only
`counts`' docstring changed). `seal_release` still looks for `header`'s
exact text before it builds anything (`.github/scripts/release_seal.py:566-572`).
A sealed header made of `<img>` tags cannot hold that text. The unchanged
case `test_a_second_run_finds_no_header_to_replace_and_writes_nothing`
passed in the 106 (executed).

```seal
confirms: none
```
What matched: the census entry is the exact host, and the phase boundary's
narrowing holds. `refused_domains` skips a domain equal to an entry or
ending in `.` plus an entry (`tests/censuses.py:925`). So the exact host
allows that host and its subdomains, and not the service's parent domain
(read). Adding an entry only adds skips, so no file the census accepted
before is refused now. That is the ground on which the phase-boundary run
left out the modules that read the census only through `conftest.py`
(read).

```seal
confirms: none
```
What matched: the stale statements of the prose cell are gone from the
code, the workflow comment and the touched tests, apart from finding 2.
The method was `git grep` over the tree, outside this work item, on the old
cell's wordings: `SEALED</b>`, `the suite at`, `one per line`,
`results as text`, `of them capped`, `review rounds`, `results' cell`,
`results cell`, `carries every number`, `bold` and `phrases` (executed). It
is a search of wordings, so it is a sample. The hits that remain are
`publish`'s header, which still states its counts one per line
(`.github/scripts/publish_release_note.py:31-35`) and stays as it is (*Scope*
item 5). The others are `docs/branch-and-release.md`, which the settle
rewrites from `## Rule changes`, and the docstrings that name what each case
was seen red against.

```seal
confirms: none
```
What matched: `chain_check.py --baseline origin/release/v0.28.1 --root
<the branch worktree> --worktree` printed no notice at a line of this work
item's `frame/design.md` naming a test pin or a copy, so no finding comes
from such a notice (executed, before this record was written).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a reader's browser shows each badge's alt text when the badge service or GitHub's image proxy cannot serve it | `frame/questions.md` Q1, `gaps.md` | a measurement: the owner opens v0.28.1's published note with images blocked |
| How the badges look on a published release page; this round read the HTML and did not render it | `.github/scripts/publish_release_note.py:698-722` | the owner, reading v0.28.1's note once the seal job has run |
| The crafter's `bin/seal mutate` runs and its compile check of the twelve mutants were read in `trail/phases/phase-1.md:504-527` and not re-run | `.github/scripts/publish_release_note.py`, `.github/scripts/release_seal.py`, `tests/censuses.py` | the sealer, where it samples the crafter's claims |
| The full suite, the repository-wide lint and the typecheck at `f6772422`, labelled `unverified` by the crafter, which is honest: the phase ran only its boundary set | the branch at `f6772422` | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q` | 106 passed, exit 0 |
| `bin/test tests/test_censuses.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_a_release_publishes_its_note.py -q` | 181 passed, exit 0 |
| `git grep -n -I` on the old cell's wordings, outside this work item | the hits listed under the seventh confirmation, and none in code that builds the cell |
| `bin/seal layout --pairs` | no pair in `tests/github/test_publish_release_note.py` or `tests/github/test_release_seal.py` |
