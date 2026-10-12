# Feature Specification: every reader and record is inventoried (#834)

<!-- seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #834 §*What the inventory is* | the two tables (readers with an input class, record mechanisms with what drifts them and who re-reads them) and the evidence column, counted from the tracker |
| #834 §*Start here* | the table changes no code; each decision it leads to is its own issue |
| `CLAUDE.md` §*The goal a design is chosen against* | the decisions are weighed for a run that verifies unattended |

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
the rule. The build of this item is the backfill §*The build* frames below.

## The build — the inventory's classes move into the code

Framed 2026-10-12 against 57e2bc13 (this branch with `release/v0.21.0` at
dae101ab merged in). Every count below was executed by the framer's probe at
that tree unless it says `read`; `plan.md` §*Technical context* states the
mapping so phase 1 can reproduce it.

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
them are in `hooks/worktree-guard.py`, which #894 and #896 are rewriting
(`plan.md` §*Phases*, phase 4).

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
The frame's default is (c), and Q1 puts the choice to the owner once.

### The inventory's fate

`inventory/` stays in this directory. It is the reading the tables above rest
on, not a process record: `settle.py#PROCESS_DIRS` names `rounds` and
`phases`, so `settle --retire-process` leaves it, and `settle --retire` takes
the whole directory when the item folds after its release, after which it is
read at the release tag (`git show v0.21.0:seal/specs/1791382684-…/inventory/`).
Nothing in the build moves or edits it.

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
| A rowed unit declares what its row said | Given a unit in the backfill set the build wrote, when its docstring is opened, then its `Reads:` line carries the row's class and direction, and the row's `What it reads` as the prose | `grep -n "Reads:" <file>` beside the row in `inventory/<part>.md` |
| The census shrinks by exactly the units written | Given the build's last commit, when `tests/test_a_reader_declares_its_input_class.py` runs, then it passes, and the census lost one line per unit that gained a line and no other | `bin/test tests/test_a_reader_declares_its_input_class.py`; `git diff --stat origin/release/v0.21.0 -- tests/undeclared_readers.txt` |
| A stale row writes nothing | Given a unit whose hash at HEAD differs from its hash at 5623d728, when the build ends, then it carries no `Reads:` line from the inventory and its census line stands | phase 1's listing against the diff |
| The ledger says what the lines cost | Given Q1's answer, when `evidence-check .` runs at the build's head, then it reports no drifted released row, and the fragment holds exactly the `Re-read ·` rows the answer's set owes | `bin/evidence-check .`; `grep -c "^| Re-read" seal/ledger/1791382684-every-reader-and-record-is-inventoried.md` |

## Data & interfaces

None. The table is a record. Its schema is the column set each part states at
its head. The `Reads:` line's grammar is `docs/the-reader-registry.md`'s, and
the build adds no word to it.

## Removes

nothing — the build adds docstring lines and removes census lines, which is the shrinking `docs/the-reader-registry.md` §*The census* defines; no unit, heading, rule sentence or test pin leaves the tree.

The inventory was framed 2026-10-07 by the session; the build above was framed
by the framer, which is the `Planning` row `routing.md` has carried since
2026-10-12.

Framed 2026-10-12 by framer, before the build.
