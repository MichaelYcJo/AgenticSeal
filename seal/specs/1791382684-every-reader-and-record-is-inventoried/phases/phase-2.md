# 1791382684-every-reader-and-record-is-inventoried — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 36491ddb |
| Ran by | smith on opus, as the run-level `handoff.md` §*Starting on a new machine* item 4 names the spawn |

## What this phase was asked

A `Reads:` line on every unit of Q1's answered set, (c), the units no
released ledger row cites, in every file but `hooks/worktree-guard.py`, and
the census lines of exactly those units removed, by a one-shot script that
asserts each landing and is deleted after. The hand-read units are decided
here, the weakest class winning. `hooks/worktree-guard.py` is not touched:
#894 and #896 are both editing it.

## What this phase found

**189 units in 44 files carry a line, and the census lost exactly their 189
lines (1,584 to 1,395).** By class: observed 76, owned 61, guess 52; by
direction: passed 105, refused 64, mixed 20. That is phase 1's set: (c)'s 241
less the 25 units in `hooks/worktree-guard.py` and the 27 in
`hooks/cmdline_base.py`, whose bytes below the rider are pinned.

**How they were written.** `test_tmp_reads_writer.py`, run from the
scratchpad on phase 1's JSON, then deleted with it, wrote 184: 156 into an
existing docstring after its first paragraph and a blank line, and 28 as a
new docstring holding the line. It re-read each written file and asserted
that the unit's docstring now holds exactly one `Reads:` line, inside the
grammar, with the class and direction it meant to write; it then removed the
census lines of the units it wrote and asserted the count. Ten lines were
written or repaired by hand with `Edit`:

- **Five cells the script refused**, because the cell holds a backslash (a
  regular expression, `\|`, `\NNN`) that a docstring without an `r` prefix
  would read as an escape: `hooks/answers.py#_squash`,
  `skills/code-review/scripts/chain_check.py#target_shas` and
  `#declared_pull_head`, `skills/verify/scripts/unverified_check.py#split_row`,
  `tests/conftest.py#gathered_entry`. Each line says what the regular
  expression matches in words, which is Q4's trim.
- **Two cells with no clause boundary inside the width**,
  `hooks/sealer-stamp.py#load_stamp` and
  `skills/code-review/scripts/round_record.py#opens_at`: cut by hand, the
  rest under the line.
- **Three clause cuts that split a parenthesis or left one word under the
  line**: `hooks/dispatch.py#read_record` and `#flat` (one row),
  `skills/evidence-check/scripts/evidence_check.py#shared_reader`,
  and `tests/commonmark_oracle.py#_hidden_commonmark`.

**The paragraph under the line has two shapes.** Where the cell was cut, the
rest follows as `What it reads, continued: …` (32 units). Where the row's
`Unknown` cell says more than its direction word, that text follows as
`<Direction>: …` (56 units), which is where the spec puts what the cell says
after the direction. Two lines run past 110 characters (114 and 116); both
are one-line docstrings, whose quotes the width did not count.

**What the hand-read units came to.** Of phase 1's 30, the ones Q1's (c)
reaches:

| Unit | Rows say | Decided | Written |
|---|---|---|---|
| `skills/verify/scripts/unverified_check.py#check_text` | owned refused (row 75), guess mixed (row 76) | guess, mixed | yes |
| `skills/implement/scripts/seal.py#plugin_workflow` | `owned/observed`, refused (X23) | observed, refused | yes |
| `hooks/worktree-guard.py#lease_owner_alive` | observed mixed (row 104), guess passed (row 105) | guess, mixed | phase 4 |
| `main` of `hooks/git/pre-commit.py`, `post-commit.py`, `reference-transaction.py` | observed, `Unknown` is `—` | no direction | no: on the census |
| the eleven `hooks/cmdline_base.py` units of row 49 | guess, `Unknown` and `What it reads` are `—` | no direction | no: on the census, and the file is pinned |

The rest are cited by a released row, so (c) leaves them on the census
whatever they decide to: `hooks/answers.py#given` (guess, refused),
`hooks/ledger-migrate.py#main` (observed, passed), `round_record.py#measure`
(guess, passed), `seal.py#import_` (guess, refused), `arm_check.py#run_arms`
(observed, mixed), `evidence_check.py#pact_change_item`, `seal.py#install_workflow`
and `#unsafe` (observed), and the five with `n/a` for a direction
(`evidence_check.py#content_hash`, `#normalise`, `#released_drift`,
`fold_check.py#markers`, `#marker_digest`). A row whose `Unknown` cell names
no direction grounds no line: the line's last word is the direction, and
writing one would be a reading no row made.

**Three `# RIDER:` stamps moved, and the frame counted no record but the
ledger.** A rider is stamped `Verified <date> against <unit>@<hash>`, the
same hash a ledger row carries, so a docstring line drifts it:
`hooks/optin.py#repo_root`, `hooks/review-skill-gate.py#already_asked` and
`skills/code-review/scripts/round_record.py#units_named_earlier`, found red by
`tests/test_a_rider_reaches_its_file.py::test_every_rider_stamp_resolves_and_reproduces_its_hash`.
Each rider was read beside its unit's diff, which is the docstring line
alone, and still says what the code does: the root is resolved again by each
caller, the session id is joined raw, and `EMPHASIS` is applied to the whole
entry. Each was re-stamped by `.github/scripts/rider_check.py --reverify
--only <file>`, one file at a time; the check then read 20 ok, 0 drifted.
The other records that carry a unit's hash were read too: the census is the
one this phase means to move, and `evidence-check`'s records arm read 7
stamps with none drifted.

**The ledger.** No unit written is cited by a released row, so nothing owes
a `Re-read ·` row, and none is cited by a live row either: the one live row
(c) reaches is on `hooks/worktree-guard.py#_first_finding_in`, phase 4's.
`bin/evidence-check .` after the writes: exit 0, 8,396 ok, 0 drifted.

**What ran.** `bin/test -q -p no:cacheprovider` over 45 modules — the 34
that read source text, a docstring or a hash (`__doc__`, `getsource`,
`get_docstring`, `hashlib`, `lineno`, `read_bytes()`, `below_floor`) and the
eleven suite-wide guards: 3,708 passed, 2 failed, both the rider case and its
companion above; after the re-stamp, `tests/test_a_rider_reaches_its_file.py`
and `tests/test_a_reader_declares_its_input_class.py` passed, 126.
`uvx ruff format --check` and `uvx ruff check` over the 44 changed `.py`
files: clean. The whole suite was not run; it is the sealer's.
