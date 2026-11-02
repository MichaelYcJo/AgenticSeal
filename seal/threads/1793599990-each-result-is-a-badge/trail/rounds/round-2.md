# Review round 2: 1793599990-each-result-is-a-badge

```seal
target: 99091356, fixes e569d6f2..99091356
```

This is a verifying round. Its target is the diff of round 1's fixes,
`e569d6f2..99091356` on `feat/1299-the-release-notes-results-are-plain-lines`.
Every coordinate below was opened in a `git clone --no-local` of the branch
worktree checked out at `99091356`. The diff holds three commits. `2a82f15a`
changes `tests/github/test_publish_release_note.py`. `413c8197` appends the
fix pass's two close blocks to `trail/rounds/round-1.md`. `99091356` is the
orchestrator's fold of S3's *Verifiable how* cell in `frame/design.md`, with
one row under `frame/plan.md` *Judgments of the run*. No `seal/parity.md` is
declared, so the round block carries no `original:` line.

Carried from round 1 and not re-derived: the case's place under `Test_module`,
the escape analysis of `badge_text` and `BADGE_URL` (round 1's second
confirmation), and the confirmations on `results`, the re-run guard and the
census, none of which the fix diff touches. Re-derived this round: both
closes, the docstring's claims against `.github/scripts/publish_release_note.py`,
and whether the whole-string assertion alone still goes red with the badge's
`alt` attribute left out.

The orchestrator's spawn prompt claims that 2a82f15a removes the parser and
its two assertions and rewrites the docstring, and that the crafter's
nine-module narrow set exited 0. The first claim was read in the diff. The
second was not re-run whole; the two modules the fix diff touches or reads
were re-run (see *Probes*).

## Findings

### 1. The frame's Scope item 6 still asks for a separate case for the alt text, which the folded S3 row now says is S1's whole-string assertion

```seal
severity: should
location: `seal/threads/1793599990-each-result-is-a-badge/frame/design.md:83-86`
evidence: read `seal/threads/1793599990-each-result-is-a-badge/frame/design.md:83-86`, `seal/threads/1793599990-each-result-is-a-badge/frame/design.md:119`, `seal/threads/1793599990-each-result-is-a-badge/frame/plan.md:97`
```

Why it matters: commit `99091356` rewrites S3's *Verifiable how* cell at
`frame/design.md:119`. The cell now says S3 is verified by "S1's whole-string
assertion, which pins every `alt` attribute byte for byte". The same frame's
*Scope* item 6 at `frame/design.md:83-86` still says the rewritten cases are
"the six cases *Grounding* lists, plus a case for the encoding (S4) and one
for the `alt` text (S3)". The frame now states two things about S3: a case of
its own, and no case of its own. The sealer reads `frame/design.md` against
the tree and finds no S3 case, and it has to choose which sentence the frame
means. The `frame/plan.md:97` judgment row gives the fold's grounds as "a
crafter or sealer reads the frame, not the round". That reader meets item 6
as well as the cell. Contract rule 19 asks that a change remove every other
sentence stating the old fact in the same commit. The fold rewrote the one
sentence the fix pass's close named and left this one.

The finding takes neither a `regression:` nor a `reopens:` line. Item 6 is
the framer's text, unchanged by the fix diff. It has disagreed with the build
since phase 1's departure (`trail/phases/phase-1.md:16-24`), so the fold did
not introduce the defect. It left it standing beside a cell that now
contradicts it. No round 1 finding named item 6.

The fix rewrites item 6's last two lines. The orchestrator may widen the
`frame/plan.md:97` row to name item 6 alongside the S3 cell.

```markdown
6. **The cases that pin the prose lines are rewritten to the badge lines**,
   each new or changed assertion seen red before the change it pins:
   the six cases *Grounding* lists, plus a case for the encoding (S4). The
   `alt` text (S3) is pinned by S1's whole-string assertion.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the parser class `Unimaged`, its function `unimaged` and both
assertions that used them are gone from
`tests/github/test_publish_release_note.py` (read, the diff of `2a82f15a`).
`git grep` finds no other reference to either name in the code or tests
(executed). `html.parser` stays imported at `:48`, and `Folds` at `:334`
still uses it, so the removal leaves no unused import (read). The docstring
at `:922-925` now says "the whole-string assertion pins every alt attribute,
which is #1299 S3", which is the fix round 1 gave. The claim that this one
assertion carries S3 was tested, not taken. With `badge`'s `alt` attribute
removed at `.github/scripts/publish_release_note.py:682`, the case went red
at the `assert sealed == (...)` at `:946-951`, with 1 failed (executed, see
*Probes*). So the docstring's closing claim, "seen red ... with the badge's
alt attribute alone left out", holds without the parser. The two touched
modules gave 106 passed, the same count as round 1, because only assertions
went and no case did (executed).

```seal
confirms: round-1#2
```
What holds: the docstring at `tests/github/test_publish_release_note.py:925-928`
says "The image's URL and alt text, and each badge's alt text, are escaped
... a badge's address is percent-encoded and needs no escape". The code does
this. `sealed_header` escapes `image_url` and `alt` at
`.github/scripts/publish_release_note.py:722`. `badge` escapes only the alt
text at `:682` and builds the address from `badge_text` at `:658-664`,
unescaped (read). The sentence agrees with `badge`'s docstring at `:672-675`
and with `sealed_header`'s at `:710-713`. `git grep` for "every badge are
escaped", "every badge is escaped" and "escapes each badge" finds only
`sealed_header`'s "escapes each badge's alt text" and round 1's own quotes
(executed). That is a search of wordings, so it is a sample.

```seal
confirms: none
```
What matched: `trail/phases/phase-1.md:16-24`, the paragraph headed "S3 is
an assertion in S1's case, not a new case", may stand as it is. It still
names `Unimaged`, which `2a82f15a` removed. A phase record holds "what
building the phase taught", each departure from the frame among it
(`skills/implement/SKILL.md` *`trail/phases/phase-N.md` holds one section*).
The paragraph says what phase 1 built at `9d693098`, the commit
`frame/plan.md:79`'s Status cell names, and that was true there. A fix pass
"writes no `trail/phases/phase-N.md`" (`skills/code-review/orchestration.md`,
and `agents/crafter.md` *A fix pass appends close blocks and writes no phase
record*). The removal is a fact of round 1, and `docs/the-record-layout.md`
*A fact of a work item has one record* gives it one home: finding 1 with its
close at `fixed 2a82f15a`, plus the `frame/plan.md:97` row. Rewriting the
phase record would state that fact twice and erase what the build did. The
paragraph's first claim, that S3 needs no case of its own because S1's case
pins the whole string, is the claim the folded S3 cell now makes. The pull
request body takes only the phase records' paths, not their prose
(`skills/code-review/scripts/pr_body.py:479-484`, read), so the removed
parser does not reach the body. A reader who opens the paragraph meets
round 1's finding 1 among the records the sealer reads (`agents/sealer.md:78`).

```seal
confirms: none
```
What matched: the `odd` input's escape is still pinned without the parser.
The substring assertion at `tests/github/test_publish_release_note.py:964-976`
holds `alt="a &amp; b: say &quot;x&quot;"` and `SEALED: v&lt;1&gt;` byte for
byte (read). The phase record claimed the removed reading made "an escaped
`&`, `<` and `"` come back as written", and that adds nothing the substring
does not already fix.

```seal
confirms: none
```
What matched: `chain_check.py --baseline origin/release/v0.28.1 --root <the
branch worktree> --worktree`, run before this record was written, printed no
notice at a line of this work item's `frame/design.md` naming a test pin or a
copy. So no finding comes from such a notice (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's nine-module narrow set. This round re-ran the two modules the fix diff touches or reads, and not the other seven, which read no path the fix diff changes | `trail/phases/phase-1.md` *The phase-boundary run* | the orchestrator, by `seal gate --base <base> --record <item>` once the rounds settle |
| The full suite, the repository-wide lint and the typecheck at `99091356`, labelled `unverified`, which is honest: no agent has run them | the branch at `99091356` | the orchestrator, by the broad run, and the sealer's spawn after it |
| Round 1's two Not judged rows on how the badges render and whether a browser shows the alt text with images blocked, carried unchanged | `frame/questions.md` Q1, `gaps.md` | the owner, reading v0.28.1's published note |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py -q` | 106 passed, exit 0 |
| `bin/test "tests/github/test_publish_release_note.py::Test_module::test_the_header_is_built_by_one_function_and_its_sealed_twin_by_another" -q`, with `alt="..."` removed from `badge`'s return at `.github/scripts/publish_release_note.py:682` through the Edit tool | 1 failed, exit 1, at `assert sealed == (...)`; the file was restored with `git checkout --` and `git status --short` printed nothing |
| `git grep -n -I` for `Unimaged`, `html.parser`, "every badge are escaped", "every badge is escaped" and "escapes each badge" | no `Unimaged` outside this work item's records; `html.parser` only at `Folds` and in other modules and work items |
