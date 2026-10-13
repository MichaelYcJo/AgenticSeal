# Round 1 report — 1791852617-a-docstring-left-short-is-reflowed

| Field | Value |
|---|---|
| Target SHA | c88d537d |
| Base | `origin/release/v0.21.1` at 321e9de1 |
| Range read | `321e9de1..c88d537d`, two commits: the routing declaration and the reflow with its ledger row |
| Ran by | specseal:warden on claude-opus-5-5 |
| Where | a `git clone --no-local` of the worktree at c88d537d under the session scratchpad's `1791852617/round-1/clone`; both probe files were deleted after their run and the clone removed at hand-over |

## Summary

The reflow does what #844 asked and nothing else. Round 3's fence for the
docstring of work item 1791270163 is now the docstring, byte for byte, and no
word and no code changed. The ledger row the smith wrote is the one row that
keeps R6's family from drifting, and it checks clean. Writing no changelog
fragment is right.

- **The docstring matches the fence.** Lines 737–745 of
  `tests/test_one_word_one_meaning.py` equal the nine lines of round 3's
  fence. The words before and after are the same 255 words in the same
  order, and the function body and the rest of the module are unchanged.
- **The re-read row is load-bearing and true.** With the fragment taken out,
  `evidence-check` names `without_the_policy_span` DRIFTED in R6's family of
  three rows. With it in, the family is clean.
- **No changelog fragment is owed.** The rule the smith cites says a commit
  that changes nothing a release note states owes the fragment nothing, and no
  document requires a fragment of every work item.
- **⬜ 1, the row miscounts the lines.** The ledger row and the overview say
  the last five lines were rewrapped. Six lines were rewrapped into five. This
  is paperwork under `seal/`, so it is a correction and does not count toward
  `Needs a fix`.

Nothing in this range loses a record or crashes. The only code change is
inside a docstring.

## What the account claimed, and what was found

- **Claimed (commit c88d537d and `overview.md:16`):** the docstring was
  rewrapped to round 3's fence, and no word and no code changed. Executed: a
  deleted probe parsed the module at the base and at HEAD. The docstring's
  word sequence is identical (255 words). The function body without its
  docstring is the same AST. Every line outside the function is identical.
  The fence taken from round 3's report at 25a05c68 equals lines 737–745 at
  HEAD byte for byte. Claim holds.
- **Claimed (`overview.md:24`):** the issue's coordinate, line 741 at
  eea27ad0, still named the short line at this branch's base. Executed: the
  same probe printed line 741 at eea27ad0 and at the base, and both read
  `continuation line stays inside,` alone. Claim holds.
- **Claimed (the ledger row's Grounds):** the function body, the span regex
  and every other unit R6 names are as #831 left them, and the module's tests
  give 21 passed. Executed: `evidence-check --strict` over
  `seal/releases/0.19.0.md` and over `seal/releases/0.20.0.md` each exits 0
  with nothing drifted, so every R6 coordinate holds its newest recorded
  hash. `bin/test tests/test_one_word_one_meaning.py -q` exits 0 with 21
  passed. Claim holds.
- **Claimed (the ledger row's Grounds and `overview.md:16`):** "the last five
  lines" were rewrapped. Executed: the docstring's last six lines at the base
  (widths 35, 76, 77, 75, 70, 12) became five at HEAD (77, 78, 74, 74, 39). The
  diff removes six lines and adds five. Claim does not hold as worded; see ⬜ 1.
- **Claimed (`overview.md:34`):** no changelog fragment is owed, and other
  work items stand with none. Read: §*A commit after the build brings its
  changelog fragment along* in `docs/the-record-layout.md`, the house rule in
  `CONTRIBUTING.md`, `skills/implement/SKILL.md` and
  `docs/release-checklist.md` §*2. Gather, fold, bump*. Executed: a listing of
  the live work items. Grounds hold; see below.

## Findings from reading

### No changelog fragment is owed, though the cited section is the narrower one

The section the smith cites is about commits made after the build, and its
subject is a fragment that already exists and has gone stale. Its sentence
"A commit that changes nothing a release note states owes the fragment
nothing" is the only written test of whether an entry is owed at all. Nothing
else in the tree requires one. The fragment table in the same document only
says where an entry goes instead of `CHANGELOG.md`. `gather_changelog.py
--check` asks only that every existing fragment reached a release file.

The reflow changes no verdict, no output and no instruction, so the test
answers "nothing owed". Three live work items already stand without a
fragment: 1788177600, 1791019421 and 1791090072, the one the overview names.
Confirmed, with no finding.

### ⬜ 1 — the row and the overview say five lines were rewrapped; six were

`seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md:1` says #844
"rewrapped the last five lines of `without_the_policy_span`'s docstring".
`overview.md:16` says the same. The base docstring ended in six lines, the
short `continuation line stays inside,` line included, and those six became
five. A reader who checks the row against the diff finds a count that does
not match.

The behaviour and every other fact in the row are right, so this is a
correction to the paperwork. It does not count toward `Needs a fix`. The
fragment folds at the release and is frozen after that, so the wording is
cheapest to fix before the fold.

### The routing declaration has no Planning row

This matches every other live work item with no `spec.md`: all six omit the
row, and the 94 with a spec answer it. The template says to delete the row
where there is no answer to give, and no frame was drawn here. Not a finding.

### Class enumeration (agent contract §12)

The class is a docstring line left short when a sentence was inserted in
front of it. A deleted probe scanned every docstring in the four Python
files #831 touched for a line that the next line's first word would have
fitted on. Read, after filtering out table and list layouts: two more
instances stand in the tree, and neither came from #831 or from this branch.

- `hooks/config.py:683` reads `work item there. A person` and was left by
  821e592d.
- `tests/test_every_reader_ends_a_line_where_gfm_does.py:1160` reads `and the
  break moved it by one. The markdown shape read` and was left by 20d1b289
  (#683).

Both are cosmetic, with the same weight as #844 itself. They are outside
this work item's scope, so they go to the Deferred table rather than to the
verdicts.

## Findings from execution

None beyond the confirmations above.

## Regression tests to plant

None. A docstring's wrap is not something a case should pin, and the word
comparison was run as a deleted probe.

## Facts for the evidence ledger

None new. The fragment's re-read row already records what this round ran
again.

## Broad gate

Not yet run, and not this round's to run. This round leaves nothing that
needs a fix. If the orchestrator closes the run on this record, the broad
gate comes due, and the sealer is the next spawn. That spawn runs the full
suite, the repository-wide lint and the typecheck once, at the settled HEAD.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | The re-read row says #844 rewrapped "the last five lines" of the docstring; six lines were rewrapped into five, and `overview.md:16` says the same | `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md:1` | open | executed: the base docstring ends in six lines (widths 35, 76, 77, 75, 70, 12) and HEAD's in five; the diff removes six and adds five. A correction to paperwork under `seal/`, not counted in `Needs a fix` |
| 🟢 | the docstring equals round 3's fence and changes no word and no code | `tests/test_one_word_one_meaning.py:737` | confirmed | executed: a deleted probe; lines 737–745 equal the fence from 25a05c68 byte for byte; the same 255 words in order; the body's AST and every line outside the function unchanged; `bin/test tests/test_one_word_one_meaning.py -q`, exit 0, 21 passed; `ruff check` and `ruff format --check` on the file, exit 0 |
| 🟢 | the re-read row keeps R6's family current at the reflowed unit's hash | `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md:1` | confirmed | executed: `evidence-check --strict --ledger` on the fragment exits 0 (2 ok); on `seal/releases/0.20.0.md` and `seal/releases/0.19.0.md` each exits 0 with nothing drifted; with the fragment moved out, `seal/releases/0.20.0.md` exits 2 with `without_the_policy_span` DRIFTED in a family of three rows, so the row is what clears it |
| 🟢 | no changelog fragment is owed for this work item | `seal/specs/1791852617-a-docstring-left-short-is-reflowed/overview.md:34` | confirmed | read: `docs/the-record-layout.md` states a commit that changes nothing a release note states owes the fragment nothing, and no document requires a fragment per work item; executed: three other live work items carry none, 1791090072 among them |

## Executed probes

| What was run | Result |
|---|---|
| a deleted probe: the module parsed at the base and at HEAD, the docstring's words and the body's AST compared, round 3's fence from 25a05c68 compared with HEAD, line 741 printed at eea27ad0 and at the base | same 255 words; same body; nothing outside the function changed; the fence equals lines 737–745 byte for byte; line 741 is the short line at both revisions; the base's last six docstring lines became five |
| `bin/test tests/test_one_word_one_meaning.py -q` in the clone at c88d537d | exit 0, 21 passed |
| `ruff check` and `ruff format --check` on `tests/test_one_word_one_meaning.py` (ruff 0.17.0 through `uvx`; CI installs ruff unpinned) | exit 0 both |
| `bin/evidence-check --strict --ledger` on the fragment | exit 0; 2 ok · 0 drifted · 0 broken |
| `bin/evidence-check --strict --ledger` on `seal/releases/0.20.0.md`, then on `seal/releases/0.19.0.md` | exit 0, 579 ok · 0 drifted; exit 0, 714 ok · 0 drifted |
| the same check on `seal/releases/0.20.0.md` with the fragment moved out of the clone, then moved back | exit 2; `without_the_policy_span` DRIFTED, "no reading in this row's family of 3 rows holds the current content"; clone status clean after the move back |
| a deleted probe: every docstring in the four Python files #831 touched, scanned for a line the next line's first word would fit on | two prose instances outside this diff, at `hooks/config.py:683` and `tests/test_every_reader_ends_a_line_where_gfm_does.py:1160`; the rest were table or list layouts |
| the broad gate: the full suite, the repository-wide lint and the typecheck | not yet; this round ran none of it, and the sealer answers it once, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Two more docstring lines of the same short shape, neither from #831 nor from this branch: `hooks/config.py:683` (left by 821e592d) and `tests/test_every_reader_ends_a_line_where_gfm_does.py:1160` (left by 20d1b289) | not filed; named here for the ladder | the orchestrator of this run, who decides whether this work item takes them or they wait for the next change to each unit |

## Paste-ready fixes

### ⬜ 1

In the ledger row's Grounds cell, replace the opening of the **Read** clause:

```
**Read** 2026-10-13: #844 rewrapped the last six lines of `without_the_policy_span`'s docstring into five, to the text round 3 of #831 gave as a fence, and changed no code;
```

And `overview.md:16`:

```
Rewrap the last six lines of `tests/test_one_word_one_meaning.py#without_the_policy_span`'s docstring into five, to round 3's fence, change no word and no code, and re-read the one ledger family the rewrap drifts.
```

Needs a fix: no
Loses a record or crashes: no

## Proof block

Files opened in this round:

- the diff `321e9de1..c88d537d`, whole
- `seal/specs/1791852617-a-docstring-left-short-is-reflowed/overview.md` and `routing.md` (through the diff), and `routing.md` against `templates/sdd-routing.md`
- `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md`
- `tests/test_one_word_one_meaning.py` lines 726–745 at HEAD, and line 741 at eea27ad0 and at the base
- round 3's report of work item 1791270163 at 25a05c68, whole
- issue #844
- `seal/releases/0.19.0.md` lines 36, 151 and 213; `seal/releases/0.20.0.md` line 126 and its section heading
- `docs/the-record-layout.md` lines 50–117; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*
- `skills/implement/SKILL.md` lines 50–70 and 580–600; `skills/implement/orchestration.md` lines 485–540; `CONTRIBUTING.md` lines 280–312; `docs/release-checklist.md` lines 60–100
- `ruff.toml`; `bin/test`; `hooks/config.py` lines 676–686; `tests/test_every_reader_ends_a_line_where_gfm_does.py` lines 1150–1166
