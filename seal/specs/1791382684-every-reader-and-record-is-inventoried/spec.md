# Feature Specification: every reader and record is inventoried (#834)

<!-- seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #834 §*What the inventory is* | the two tables (readers with an input class, record mechanisms with what drifts them and who re-reads them) and the evidence column, counted from the tracker |
| #834 §*Start here* | the table changes no code; each decision it leads to is its own issue |
| `CLAUDE.md` §*The goal a design is chosen against* | the decisions are weighed for a run that verifies unattended |
| `docs/the-reader-registry.md` §*The four classes and the line that declares one* | a check reads two words of a `Reads:` line and nothing between them; the prose is the reviewer's |
| `docs/the-reader-registry.md` §*What neither check can read* | a false declaration (limit 1) and a stale line (limit 5) pass both checks, and the warden's reading of the diff is their only reader |
| `docs/the-reader-registry.md` §*The census: the units that stood undeclared at landing* | a listed unit owes nothing until it changes, and the census only shrinks |
| `handoff.md` §*Review of the run* and §*What the owner decided (2026-10-12)* | 0.21.0's theme: a reader observes, forces a format, or is deleted; a guess-and-patch loop is reframed against the theme, never given another fix pass |

## Scope

**In.** The inventory, taken against 5623d728 (0.20.0 as shipped), is committed
under `inventory/` in this directory:

| Part | File | What it covers | Rows |
|---|---|---|---|
| 1 | `inventory/1-hooks-shell.md` | hooks that read shell command text: `cmdline`, `cmdline_base`, `tokens`, `one_heredoc`, `worktree-guard`, `worktree_consent`, `commitgate`, `commit-review-gate`, `gate`, `dispatch` | 144 readers |
| 2 | `inventory/2-hooks-rest.md` | every other hook, `hooks/git/*`, the payload fields each hook reads | 113 readers |
| 3 | `inventory/3-review-chain.md` | `chain_check`, `round_record`, `survivor_check` | 130 readers |
| 4 | `inventory/4-ledger-settle-seal.md` | `evidence_check`, `correction_check`, `pact_check`, `settle`, `fold_check`, `seal` | 159 readers |
| 5 | `inventory/5-verify-bin-ci.md` | `skills/verify/scripts/*`, `bin/`, the shell steps of `.github/workflows/*` | 136 readers |
| 6 | `inventory/6-tests.md` | the tests that read the tree's own text, and the four helper modules | 785 readers |
| 7 | `inventory/7-records.md` | record mechanisms, and what each cost in rows and lines since 0.18.0 | 35 mechanisms |
| 8 | `inventory/8-evidence.md` | the 63 issues since 0.18.0, by family and by file | 63 issues |

Each part was taken by one read-only agent from the code itself. Probes that
were executed are marked as executed in their row, and every other row is
`read`. The row counts are each part's own. A parse of the `Class` column
reads 1,381 of the 1,467 reader rows; the rest wrap or quote a pipe.

**Out of the inventory.** No code changes in the inventory itself. The table's
permanent home, and the check that reads it as a registry, were decided by
#835's frame and have landed (dae101ab on `release/v0.21.0`): the registry is
the code, each unit's `Reads:` line, and `docs/the-reader-registry.md` holds
the rule. The build §*The build* framed was the backfill of that registry from
the inventory; §*The reframe* withdraws it, and the item ships as the
inventory alone.

## The build — the inventory's classes move into the code

*This section is the first frame's, kept as it was written because its counts
are what the three review rounds and §*The reframe* argue from. The build it
frames was built in phases 1–3, reviewed in three rounds, and withdrawn.*

Framed 2026-10-12 against 57e2bc13 (this branch with `release/v0.21.0` at
dae101ab merged in). Every count below was executed by the framer's probe at
that tree unless it says `read`; the mapping phase 1 reproduced it by is in
`plan.md` at 8938af5b and in `phases/phase-1.md`.

### What the build writes

`docs/the-reader-registry.md` §*The four classes and the line that declares
one* owns the grammar, and #835's spec §*What #834's build does with this
frame* says what moves: for an inventory row whose unit is in the population,
the row's `Class` and `Unknown` become the unit's docstring line

```
Reads: <class> — <the row's What it reads cell, on one line>; unknown <direction>
```

and the unit's census line leaves `tests/undeclared_readers.txt`. The class
word is the first word of the row's `Class` cell and the direction word the
first word of its `Unknown` cell; what the `Unknown` cell says in parentheses
after that word goes in the paragraph under the line, because the direction
word has to be the line's last word. The line sits after the docstring's
summary line and a blank line, as #835's own units carry it; a unit with no
docstring gets one holding the line. The other columns — `Decides`,
`Duplicates`, `Note` — move nowhere; they stay in `inventory/` as the reading
of a moment.

### Which units, measured

The six reader parts hold 1,467 rows. At 57e2bc13:

| Rows | Count | Fate |
|---|---|---|
| inside `tests/test_*.py` (part 6) | 760 | out of the population by #835's file-name rule; nothing to write |
| on `bin/` and the workflows (part 5) | 10 | no AST; out |
| naming no population unit — a constant, a nested function, a method, a unit since removed | 23 | nothing to write; a constant's reader is rowed under its own unit where one exists |
| naming exactly one population unit | 508 | the unit's line |
| naming several units (`a` + `b` + `c`) | 166 | each named unit gets the row's line |

Those rows name **912 distinct units** of the 1,607 in the population (1,584
on the census). The build writes a line only where the row still describes
the code:

| Units | Count | Fate |
|---|---|---|
| unchanged since 5623d728, one class, the rows agree | **759** | the backfill set; how much of it this release writes is `questions.md` Q1 |
| unchanged, but the rows for the unit name two classes (6) or two directions (1) | 7 | the weakest wins, by the registry's own rule: `guess` over the others, `mixed` over a single direction |
| unchanged, and the `Class` cell starts with no class word | 23 | the smith reads the cell: a cell naming a class in other words gets that class, a cell naming none leaves the unit on the census |
| changed since 5623d728 (hash moved), 3 of them already declared by #835 | 123 | **stay on the census.** The row is a reading of code that is gone; a fresh reading is a judgment no row grounds, and these are the units the siblings rewrote on purpose — `evidence_check.py` (22), `round_record.py` (16), `chain_check.py` (16), `broad_gate.py` (8), `commitgate.py` (8). They declare when next touched, which is the rule's own transition |

The 759 split `guess` 275, `owned` 256, `observed` 228, across 57 files; 43 of
them are in `hooks/worktree-guard.py`, which #894 and #896 were rewriting
when this was framed.

### What a line costs under the ledger freeze

A `Reads:` line moves the unit's hash. Under `Ledger frozen from`, every
released row anchored on that unit then owes a `Re-read ·` row in this item's
fragment, and every live-fragment row is re-stamped in place
(`docs/the-evidence-ledger.md` §*A released row is read again in the branch's
fragment*). Counted at 57e2bc13 over `seal/ledger.md` and
`seal/releases/*.md` (released) and `seal/ledger/*.md` (live), whole-unit
anchors only — a `>` anchor hashes its own statement and a docstring line
does not move it (4 released, 2 live):

| Set | Units | Cited by a ledger | `Re-read ·` rows owed | Live rows re-stamped |
|---|---|---|---|---|
| (a) all 759 | 759 | 514 | **687** (1,093 anchors) | 24 (35 anchors) |
| (b) the 275 `guess` units only | 275 | 180 | 247 (388) | 14 (15) |
| (c) the units no ledger row cites | 245 | 0 released, 1 live | **0** | 1 |
| the whole census, #835 Q7's (b) | 1,584 | 1,035 | 1,337 (2,384) | 413 (687) |
| the 123 stale units, were they read afresh | 123 | 116 | 501 (610) | 357 (468) |

For scale: the whole 0.21.0 run wrote 360 `Re-read ·` rows across nine
fragments, and the run's review called that cost structural
(`handoff.md` §*The ledger's re-read cost is structural*, read). (a) would
write 1.9 times that in one fragment, for a change that cannot falsify a
claim — a docstring line changes no behaviour — and `--checked` on each row
asserts somebody read it (`seal/follow-up.md`'s row on the unread re-stamp).
The frame's default was (c), and Q1 put the choice to the owner once; the
owner answered (c).

### The inventory's fate

`inventory/` stays in this directory. It is the reading the tables above rest
on, not a process record: `settle.py#PROCESS_DIRS` names `rounds` and
`phases`, so `settle --retire-process` leaves it, and `settle --retire` takes
the whole directory when the item folds after its release, after which it is
read at the release tag (`git show v0.21.0:seal/specs/1791382684-…/inventory/`).
Nothing in the build moves or edits it.

## The reframe — the lines leave, the census returns, the item ships as the inventory

Reframed 2026-10-12 after round 3, from the run's three round records
(`rounds/round-1.md` to `round-3.md`, their reports and fix tables), the
three phase records, and the owner's review of the run in `handoff.md`.

### What the three rounds measured

Phases 1–3 wrote 189 `Reads:` lines in 44 files, each transcribed from an
inventory row: the row's `Class` as the class word, the first word of its
`Unknown` cell as the direction, its `What it reads` cell as the prose.

| Round | Read against the code | Lines found false | From a row naming one unit / several |
|---|---|---|---|
| 1 | all 189 units' bodies (4,268 lines of source) | 40: 32 describing a neighbouring unit, 7 class or direction words the body contradicts, 3 line numbers wrong at the commit that wrote them | 3 / 37 |
| 2 | the 32 fixed, the six front units, and three enumerations (71 non-lead units, 40 sharing a line, 80 naming something absent from the body) | 27: 13 more lines naming a read the unit never makes, 4 words from the row, 2 units the round-1 fix had rewritten wrong, 11 the fix pass's own enumerations corrected | 0 / 27 |
| 3 | the three enumerations rerun (95 units), the other 94 printed beside their names and not opened | 4: `_name_at`, rewritten by round 2's fix and false of seven of its eight callers; `_expands`, `cell_index`, `shared_reader` | 0 / 4 |

The last column is the framer's probe over the inventory's `Unit` cells and
the census diff, executed 2026-10-12: 64 of the 189 lines came from a row
naming one unit, 125 from a row naming several. Round 3 stopped the run on
the second fix of a fix (`rounds/round-3.md`, its `Fix of a fix` row reads
`second`). Round 1 read every line beside its body; round 3 then opened 95
against their bodies and left 94 outside its union, reading those lines
without their bodies (its probe table: *read, bodies not opened; this is a
sample, not a verdict*); how many of the 94 round 2 had opened is not
counted. Round 1's own matching
split the lines 83 from rows naming one unit, 97 from rows naming several and
9 unmatched, where the framer's probe above reads 64 and 125.

### The judgment

A `Reads:` line transcribed from a row is a claim about one unit's body made
from an agent's prose about a *reader*, and a reader in the inventory is often
several units (166 of the 674 rows naming a population unit). What a check
reads of the line is two words — `tests/reader_registry.py#declarations`
takes the class word and the last word and refuses each only outside its
vocabulary — and the one lie a check can see is `nothing` beside a K1 call,
which none of the 189 lines says. Everything else in a line is limit 1 and
limit 5 of `docs/the-reader-registry.md` §*What neither check can read*: the
warden's reading of the diff. Three rounds show that reading converging at
the rate of one hand reading per pass, each pass fixing what it found and the
next finding the fix (`sections` in round 2, `_name_at` in round 3). That is
the loop the owner's review of the run names, and under 0.21.0's theme the
fate of the reader that produced it — the transcription, then the hand
re-readings — is deletion, not a fourth pass.

So the subset of the 189 lines a reader can verify mechanically is empty, and
the reframe takes the option the spawn put first: **every unit the build
wrote goes back on the census.** A census line is true by construction — it
is the unit's own hash, and the check refuses it the moment the unit changes —
and it owes nothing until then. The unit declares when touched, by the hand
that just read it, in a diff a reviewer reads one unit at a time: the
transition #835 designed. What that costs is 53 `guess` entries in
`grep -rn "Reads: guess"` that the inventory still lists, in the tree until
the item retires and at the tag after.

### What the reframe removes

The whole of the build's tree change, and every record that claims it:

- the 189 `Reads:` lines and the paragraphs under them in 44 `.py` files, and
  the three `# RIDER:` re-stamps those lines cost (`hooks/optin.py#repo_root`,
  `hooks/review-skill-gate.py#already_asked`,
  `skills/code-review/scripts/round_record.py#units_named_earlier`), which
  return to the hashes of the restored units;
- the removal of the 189 census lines: `tests/undeclared_readers.txt` returns
  to the 1,584 lines #835 landed;
- the ledger fragment's two rows (B1, B2), which claim the lines and the
  shrink, and with them the fragment;
- the changelog fragment's `### Changed` entry;
- phase 4 as the first frame drew it, the guard's lines after #894 and #896:
  #894 landed with its `main` declared (34fc36e9 on `release/v0.21.0`),
  #896's branch declares the three units it touched, and the guard's other
  census units declare when next touched;
- `plan.md`'s mapping rules, and the direction rule rounds 1 and 2 amended
  into them.

What stays: the inventory, with the ten `· NAME NOT IN TREE` markers phase 3
added (true of the tree, and read by nothing while the item has no ledger
fragment); the phase and round records, which are the history this section
rests on; the three rider stamps as #835's tree carried them.

### The direction word, settled

Two definitions coexisted. `plan.md`'s amended rule read the direction off
the unit's own body: `refused` where it raises or stops, `passed` where it
hands back a default. The inventory's `Unknown` cells read it off where the
unknown ends: part 1 row 9 says an unfilled `$` *stays* and `EXPANDS` *then*
makes the target `Unresolved`, and calls that `refused`; part 6's key says a
presence pin is `refused` because a rewording fails it. The registry's is the
inventory's, by #835's own frame — its spec §*The vocabulary, and the grammar
the check reads* says *the direction is the inventory's* — which
`docs/the-reader-registry.md` now states in the inventory's words.

So the direction of a unit is **where an input it does not understand ends,
read through to the decision the unit feeds**: `refused` where that decision
refuses it (raised, stopped, or handed back as a value its caller refuses
on), `passed` where it is let through as if understood, `mixed` where both
happen. A helper's direction is therefore its callers' to read, which is why
a row's direction word, written for the reader as a whole, was wrong on the
helper, and why the narrower rule was tempting: it is readable on one body.
The narrower rule is withdrawn. After phase 4 nothing in the tree carries a
line the inventory's rows wrote, and the definition is
`docs/the-reader-registry.md`'s, for whoever next writes a line on one of
these units.

## What the table says

### Input class by part

Read from the `Class` column (parsed rows, see above).

| Part | owned | observed | guess | unknown passed |
|---|---|---|---|---|
| 1 shell-reading hooks | 18 | 25 | 98 | 64 |
| 2 other hooks | 33 | 51 | 20 | 63 |
| 3 review chain | 74 | 30 | 21 | 68 |
| 4 ledger, settle, seal | 73 | 52 | 28 | 76 |
| 5 verify, bin, CI | 43 | 49 | 39 | 82 |
| 6 tests | 125 | 94 | 508 | 101 |

### Families since 0.18.0

From part 8. *Reopened* counts issues that are a new shape of a defect another
issue in the window had just fixed.

| Family | Issues | Guess | Reopened | Converged? |
|---|---|---|---|---|
| reverify judgment and order | 10 | 0 | 5 | no issue since #829, a window of about 1.5 days |
| broad-gate run attribution | 8 | 8 | 6 | no issue since #846; the defect moved to the recorder's record (#849, #852) |
| worktree-guard shell prediction | 6 | 6 | 4 | no: #854 and #856 after #850's redesign |
| pact markdown reader | 5 | 0 | 4 | the `Pact` row reader yes (#793); the compat reader and the sweep's span no (#844) |
| heredoc body as data | 3 | 3 | 2 | yes, after one exact shape (`hooks/one_heredoc.py`) and the copies removed (#803) |
| records sentence vs code | 3 | 0 | 1 | — |
| fix-range walk over merges | 2 | 0 | 1 | no: #805, #860 open |

What converged read an owned format or an observed fact and refused the
unknown. What did not converge read someone else's text and let the unknown
through, which is #834's own observation, now with the table's counts under it.

### What the table found besides

- **One judgment in several places, disagreeing.** This is the shape #824 ended for one
  ledger row, and it is still present:
  - `Needs a fix` is read three ways (part 3 rows 47, 61; part 5 row 36), and a
    deferred finding's home four ways.
  - `seal/config.md`'s duplicate rows are read first-wins in one place and last-wins
    in another, and an unreadable file gets four answers (part 4 E47, C17, F12, X16).
  - The ledger coordinate grammar is written five times (part 4).
  - The guard and the consent writer pick different directories for one creation
    (part 1 row 127, executed).
  - The `claude` process is found by a substring test in one hook and by an exact
    match in another (part 2 rows 9, 14).
- **Record bookkeeping outweighs claims.** 84% of the ledger rows landed since
  0.18.0 are `Re-read ·` or `Corrected ·` (part 7). `# RIDER:` comments, one stamp
  each with no families, held at 20 with 0 drifted.
- **Guesses where an observed source exists.** The broad gate's panel counts
  still come from pytest's printed summary (part 5 row 26). Units outside Python
  are bounded by indentation (part 4 E17, probe executed).
- **The tests read prose.** 508 of the 727 parsed test rows are guesses. The largest
  cell is a sentence pinned verbatim, and the pin files grew most:
  `test_the_seal_is_taken_once_by_the_sealer.py` went from 5,883 to 9,934 lines
  (part 6).

## Decisions taken from the table

Each is its own issue in milestone `release: 0.21.0`. The three drafted on
2026-10-06 are reopened, each with a comment carrying the table's grounds.

| Issue | Decision | Grounds in the table |
|---|---|---|
| #835 (reopened) | a reader declares its input class; a new mechanism names one it removes | the class counts above; the converged/not-converged split |
| #836 (reopened) | a ledger row's claim is the test that enforces it | part 7: 84% bookkeeping rows; a re-read anchors on the unit it re-read |
| #837 (reopened) | a records-level finding closes once at the run's end | part 8: 18 of 33 review-filed issues from a capped run's last round or its check |
| #866 | a round-record cell has one reader | part 3, part 5: `Needs a fix`, deferred home, `Location`, draft state, the floor's two walks |
| #867 | `seal/config.md`, the coordinate and a heading have one reader each | part 4, part 2: duplicate and unreadable answers, five coordinate grammars, four heading rules |
| #868 | the hooks place a creation, find the session, read the waiver and take a failed git call one way | parts 1 and 2, one executed |
| #869 | the broad gate reads its counts from the recorder | part 5 rows 26, 31, and the mark-file traceback; with #852 |
| #870 | a unit the extractor cannot bound is refused, not guessed | part 4 E17 and E18, probe executed; takes #848 |

## User scenarios & acceptance

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A reader asks what a reader reads | Given the inventory, when they look up a unit, then its row gives file, unit, what it reads, class, unknown input and copies | open `inventory/<part>.md` |
| A reader asks what keeps costing | Given part 8, when they sort by family, then the issues and reopenings per family are counted with their numbers | `inventory/8-evidence.md` §*Counts by family* |
| A decision cites its ground | Given an issue from the table above, when it is opened, then it names the part and row it rests on | the issue bodies |
| The tree carries no line the inventory wrote | Given phase 4's commit, when the 44 `.py` files the build changed and the census are diffed against 7608d82c, then the diff is empty: no `Reads:` line, no paragraph under one, no re-stamped rider | `git diff --quiet 7608d82c ef8fb33c -- '*.py' tests/undeclared_readers.txt`, exit 0 |
| The census is the one #835 landed | Given the head, when the registry test runs, then it passes and the census equals the release branch's: the 1,584 lines #835 landed, less the units siblings have since declared (1,583 at 34fc36e9, after #894 declared `hooks/worktree-guard.py#main`) | `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py`; `wc -l tests/undeclared_readers.txt` |
| No record claims a line | Given the head, when the record checks run, then each exits 0, this item has no ledger fragment, and its changelog fragment holds `### Added` alone | `bin/evidence-check .`; `bin/correction-check --range origin/release/v0.21.0...HEAD`; `bin/survivor-check --range origin/release/v0.21.0...HEAD`, with no exemption file (`phases/phase-5.md`); `bin/unverified-check` with `--baseline origin/release/v0.21.0`; `ls seal/ledger/` names no file of this item; `grep -c "^### " changelog.md` prints 1 |
| The guard is nobody's phase | Given the release branch merged in, when `hooks/worktree-guard.py` is diffed between the base and the head, then this branch changed it nowhere | `git diff --stat origin/release/v0.21.0...<head> -- hooks/worktree-guard.py` prints nothing |

## Data & interfaces

None. The table is a record. Its schema is the column set each part states at
its head. The `Reads:` line's grammar is `docs/the-reader-registry.md`'s, and
this item adds no word to it, and after the reframe its two sentences there
are the direction's definition, with limit 5's sentence on a helper staled
by its caller.

## Rule changes

- nothing
  why: internal: the inventory, which leaves with this directory; overturned: the Reads:
    backfill, withdrawn in its own build.

## Removes

nothing — the reframe withdraws what this item's own build added (189 docstring lines in 44 files, their census removal, two ledger rows, a changelog entry), so the branch's code is the release branch's but for one docstring, the registry test module's statement of the rule (round 5 ⬜ 3); no unit, heading or test pin that stood before this item leaves the tree, and the one rule sentence it replaces is the direction sentence of `docs/the-reader-registry.md`, rewritten to the settled meaning (`overview.md` §*Fed back into the spec*).

The inventory was framed 2026-10-07 by the session; the build above was framed
by the framer, which is the `Planning` row `routing.md` has carried since
2026-10-12, and withdrawn by the framer at the reframe the same day.

Framed 2026-10-12 by framer, before the build.
Reframed 2026-10-12 by framer, after round 3.
