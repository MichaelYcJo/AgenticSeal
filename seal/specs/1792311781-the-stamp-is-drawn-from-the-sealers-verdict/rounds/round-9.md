# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 9

target: 82584daf, fixes 527afede..82584daf

## Findings

The repair closes what the sealer withheld on: the page no longer gives the
stamp to the broad gate or cites the removed section, and the new case is
red on the page as f2f7b6d5 carries it. Two findings remain, both `should`.
The new pattern lets through the phrase #975's own documents use for the old
drawer, and the page's history leaves out the third emblem the gate's run
drew.

### 1. The new stamp sweep passes "the broad gate's run draws the stamp", the phrase #975 uses for the old drawer

severity: should
location: `tests/test_one_word_one_meaning.py:477-486`
verdict: fixed fa551683
regression: round-8

The unit is `STAMP_GIVEN_TO_THE_GATE` and the comment above it
(`tests/test_one_word_one_meaning.py:477-486`), added by d6e9d285, the fix
pass after round 8 that answered the sealer's `withheld` and that no finding
commissioned. The frame's S11 row (`spec.md:116`) and phase 3's row
(`plan.md:183`) extend `SEAL_SWEPT` so that none of its files says the broad
gate draws or writes the stamp, and phase 3's own sweep looked for `gate's
stamp`, `run's stamp` and `gate draws` (`phases/phase-3.md:42-46`); the fix
wrote a pattern that allows at most two `\w+` words between `gate` and
`stamp`, so `run's stamp` and `the gate's run draws the stamp` pass it, and
the defect came from how the fix was written, not from the frame.

Why it matters: the case's docstring says no swept file "says the gate draws
one", and the comment says it reads "by construction rather than by a list
of sentences". #975's documents name the old drawer as "the broad gate's
run" (`docs/the-review-record.md:272-273`, and the page's own new sentence
at `assets/seals/README.md:6`). A sentence that slides back to the old fact
is most likely to be written in that phrase, and that is the phrase the
pattern lets through. The two-word window also cannot reach the passive
order, `a stamp drawn by the broad gate`.

Executed (probe row 3). Against ten sentences that give the stamp to the
gate, the pattern refused four (`The broad gate draws a stamp`, `the broad
gate's stamp`, `the broad gate draws its stamp`, `the broad-gate stamps the
tree`) and let six pass: `the broad gate's run draws the stamp`, `the broad
gate's run drew the stamp`, `the broad gate's run's stamp`, `a stamp drawn by
the broad gate`, `the stamp is drawn from the broad gate's run` and `the
stamp the broad gate draws`. Of six true sentences it let five pass, among
them `The broad gate draws nothing` and the page's `the broad gate's run drew
it when the run passed`, and refused `the broad gate draws no stamp`.

The pattern below refused nine of the ten, all but `the stamp the broad gate
draws`, and let the same five true sentences pass. It found nothing in any
`SEAL_SWEPT` file at 82584daf, found the page's three instances at f2f7b6d5,
and `LITERAL_SEAM` finds no seam in it, so the fold case at
`tests/test_one_word_one_meaning.py:658-671` still holds (probe row 3). It
still refuses `the broad gate draws no stamp`, as the current pattern does,
and no swept file says that. Show the widened reach red before it is
committed: plant `the broad gate's run draws the stamp` in one swept file in
a scratch clone and see the case fail.

```python
# #975: the stamp is drawn once per work item from the sealer's `sealed`
# (`docs/the-review-record.md` §*The stamp*), and `docs/the-broad-gate.md`
# §*Where the stamp is drawn* is gone. Read by construction rather than by a
# list of sentences: the gate, possessive or not, with at most three words
# before `stamp`, each of which may carry an apostrophe (`gate's stamp`,
# `gate draws a stamp`, `gate's run draws the stamp`, `gate's run's stamp`,
# `gate stamps`); the passive `stamp drawn by` or `from the gate`; and the
# removed section's name. `The broad gate draws nothing` stays allowed, which
# is what `skills/verify/SKILL.md` and `seal_stamp.py` say since #975. `The
# gate draws no stamp` would be refused, and no swept file says it.
STAMP_GIVEN_TO_THE_GATE = re.compile(
    r"\bgate(?:'s)?(?:\s+[\w']+){0,3}\s+stamps?\b"
    r"|\bstamps?\s+(?:is\s+|was\s+)?drawn\s+(?:by|from)\s+"
    r"the\s+(?:broad[\s-])?gate"
    r"|Where the stamp is drawn",
    re.I,
)
```

answer: the record's pattern and comment, applied as written; the fold case's comment now says the pattern carries two apostrophes with more than blanks and a string prefix between them. `test_the_stamp_sweep_reads_the_gates_run_and_the_passive` pins ten sentences that give the stamp to the gate (the record's nine it refuses, and `a stamp drawn from the broad-gate run`) and three true ones it lets pass; `the stamp the broad gate draws` is named in its docstring as still passing. executed: that case red against the two-word pattern on `the broad gate's run draws the stamp`, green after; with the widened pattern, `The broad gate's run draws the stamp.` planted in `assets/seals/README.md` turned `test_no_instructing_document_gives_the_stamp_to_the_broad_gate` red, and the plant was removed; the module 26 passed with no hit in any `SEAL_SWEPT` file, the `LITERAL_SEAM` closure case among them; `uvx ruff check` and `uvx ruff format --check` exit 0. read: `git grep -n -F` of the old comments' `at most two words` and `one apostrophe and no second` under `tests/` finds nothing after the change, so no other case pinned them.

### 2. The emblems page leaves out the S that 0.20.0 to 0.22.0 carried, under a heading that says every emblem

severity: should
location: `assets/seals/README.md:1`, `assets/seals/README.md:6-8`, `assets/seals/README.md:69`
verdict: fixed 9e8c1532

The new history sentence is true of what it names, and the page around it
is not complete. A reader asking which emblems the gate's run drew before
#975 learns two of three, under a heading d6e9d285 rewrote to "every emblem
the stamp has carried".

Read. The page's entries are the gold lily, 0.10.0 to 0.16.0, and the red
lily, 0.17.0 to 0.19.0 (`assets/seals/README.md:27`, `:48`). Its candidates
section calls the chart the stamp has used since the red lily "a
placeholder, Georgia Bold's S" (`:76-80`). Line 69 says the emblem that
follows the red lily is added when its release is tagged.

Executed (probe row 4). `skills/verify/scripts/seal-mark.txt` is in the
tree at v0.20.0, v0.21.0 and v0.22.0, `seal_stamp.py` at each tag reads its
chart from it, and `git diff v0.20.0 82584daf` of that file is empty. At
v0.22.0, `broad_gate.py` prints `stamp.stamp(rows, shape)` on a terminal
(line 3137) and otherwise writes the stamp's values for the hook (`signal`,
lines 3241-3280). So the stamps of v0.20.0, v0.21.0, v0.21.1 and v0.22.0
carried a third emblem, drawn from the gate's run, and the page has no entry
for it, though all four releases are tagged.

What the sentence does say holds (executed, probe row 4): v0.10.0's
`broad_gate.py` prints `stamp.stamp(rows, …)` on success (line 640) and the
`not_sealed` words with no drawing on failure (line 601), and v0.16.0 and
v0.19.0 draw over a written cell or write the values the hook draws.

Not a regression: the heading claimed every emblem before d6e9d285, and line
69 stands as 149ca9ec wrote it. The fix kept the claim rather than making
it, so this is an ordinary finding. The S's own entry, its `.ans` and `.png`,
is a separate piece of work; the fix below only stops the page from claiming
what it does not hold.

```markdown
# assets/seals/ — the emblems the stamp has carried

The stamp is the sealer's. It is drawn once per work item, at the commit of
a `guarantee.md` reading `sealed` (`docs/the-review-record.md` §*The
stamp*): the panel of what the records at that commit say, and a wax disc
with an emblem pressed into it. Before #975 the broad gate's run drew it
when the run passed. It drew the gold lily and the red lily below, and from
0.20.0 through 0.22.0 the placeholder S that §*Candidates for #857*
describes, which has no entry here yet. The emblem has changed since #30
first drew it. This directory keeps each version as the terminal drew it,
so a reader can see an earlier one without checking out an old tag.
```

Line 69, in place of its first sentence:

```markdown
The emblem that follows the red lily, the placeholder S, has been on every
release's stamp since 0.20.0 and has no entry yet.
```

answer: the record's wording, applied as written to the title, the history paragraph and line 69's first sentence; the rest of line 69's paragraph stands. The page now claims only the gold lily and the red lily as entries and names the S as having none. The S's own entry, its `.ans` and `.png`, is filed as #978 (milestone `release: 0.22.2`) and is not this pass's. The class was enumerated by `git grep -n -i -E` of `every emblem`, `each emblem`, `both emblems` and `all emblems` outside `seal/specs/` and `CHANGELOG.md`: the page's title and history sentence, and the `SEAL_SWEPT` comment at `tests/test_one_word_one_meaning.py:240`, which said "every emblem the stamp has carried" and now says "the emblems"; `overview.md`'s emblems-page row names the S and #978, and its Not done names the missing entry. executed: the one-word, real-identifier, line-wrap, pasted-passage and words modules 82 passed with the page changed, the stamp sweep finding no hit on its new sentences. read: no test reads the page's text other than the stamp sweep (`git grep` of `assets/seals` under `tests/`).

## Confirmations

confirms: none
The sealer's `withheld` at f2f7b6d5 is answered. `assets/seals/README.md:1-10`
no longer says the broad gate draws the stamp or cites §*Where the stamp is
drawn*; it says the stamp is the sealer's and links `docs/the-review-record.md`
§*The stamp* (read). `test_no_instructing_document_gives_the_stamp_to_the_broad_gate`
fails with the page as f2f7b6d5 carries it, on three hits: the heading,
`The broad gate draws a stamp` and the removed section's name, as its
docstring says; it passes at 82584daf (executed, probe rows 1 and 2). The
page is in `SEAL_SWEPT` (`tests/test_one_word_one_meaning.py:240-244`, read).

The class outside the swept list holds too (executed, probe row 5). A
`git grep` over the tree outside `tests/`, `seal/specs/`, `CHANGELOG.md` and
`changelog/`, in both orders, gate before stamp and stamp before gate with up
to six words between, finds no sentence that gives the stamp to the broad
gate: `README.md:385`, `agents/sealer.md:99`, `skills/verify/SKILL.md:257`,
`broad_gate.py:265` and `seal_stamp.py:418` and `:542` are each true as they
read. The one test docstring that still says `broad-gate` draws the stamp
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1406`) is the
history `overview.md` §*Not done* leaves standing.

The page's summary agrees with §*The stamp* on what the stamp carries, "what
the records at the commit say" (`docs/the-review-record.md:296`, read). It
puts the drawing "at the commit", where §*The stamp* puts it at the end of
the turn in which the guarantee was committed (`:269-270`); the page links
the section, so the precise rule has one source.

The new `overview.md` row's coordinates hold (read): `spec.md:181` is the
`## Removes` row for §*Where the stamp is drawn*, `phases/phase-3.md:42-46` is
the sweep claim, and d6e9d285 changes `assets/seals/README.md` and
`tests/test_one_word_one_meaning.py`, the two paths the row names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round. `broad-gate.md` names 2475178a, and d6e9d285 and 82584daf changed the tree after it | — | the broad run after the rounds settle, before the sealer is spawned again |

## Probes

| Command | Result |
|---|---|
| `bin/test` of `test_one_word_one_meaning.py`, `test_no_real_identifiers.py`, `test_docs_line_wrap.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_the_record_is_written_in_words.py` with `-q`, in the round's clone at 82584daf | 81 passed, exit 0 |
| `assets/seals/README.md` checked out at f2f7b6d5 in the clone; `bin/test tests/test_one_word_one_meaning.py -q -k test_no_instructing_document_gives_the_stamp`; the file restored to 82584daf; `git status --short` | 1 failed, three hits on the page (the heading, `draws a stamp`, the section name), exit 1; clean after the restore |
| one probe script, run once with the clone's interpreter and deleted: `STAMP_GIVEN_TO_THE_GATE` and the wider pattern of finding 1 against ten sentences that give the stamp to the gate and six true ones, the wider pattern over every `SEAL_SWEPT` file at 82584daf and over the page at f2f7b6d5, and `LITERAL_SEAM` over the wider pattern | current: 4 of 10 refused, 5 of 6 true passed; wider: 9 of 10 refused, the same 5 of 6 passed, 0 hits at 82584daf, 3 at f2f7b6d5, no seam; exit 0 |
| `git ls-tree` and `git show` of `broad_gate.py`, `seal_stamp.py`, `seal-mark.txt` and `agents/sealer.md` at v0.10.0, v0.16.0, v0.19.0, v0.20.0, v0.21.0 and v0.22.0; `git diff --stat v0.20.0 82584daf -- skills/verify/scripts/seal-mark.txt` | the gate draws or queues the stamp at every tag; `seal-mark.txt` from v0.20.0 on, unchanged since; diff empty |
| `git grep -n -i -P` of gate then stamp, and stamp then gate, with up to six words between, outside `seal/specs/`, `CHANGELOG.md`, `changelog/` and `tests/` | six hits, each true as it reads (Confirmations) |
| this record: copied into the clone and staged; `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_docs_line_wrap.py` with `-q`; `chain_check.py --baseline f6ae6db6 --root <the clone> --worktree` | 81 passed, exit 0; exit 0 as a draft, with this record's two `open` verdicts, the broad run and the guarantee behind HEAD, and the sealer's `withheld` named, and no refusal of this record's shape |
