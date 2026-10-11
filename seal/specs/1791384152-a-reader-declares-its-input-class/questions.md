# a reader declares its input class (#835) — questions for the planner

<!-- seal/specs/1791384152-a-reader-declares-its-input-class/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## Decided from the tree, so nobody reopens them

The ticket left these open and the repository answered them; the grounds are
in `spec.md` §*The decisions* and `plan.md` §*Alternatives considered*.

- **The registry is the code, not a table.** The house rule against a shared
  registry, the 1,000-line ceiling, #834's finding about copied judgments, and
  the follow-up list's rider precedent decide it. Q1 below carries the
  ticket's wording to the owner because `agents/framer.md` says a ticket
  asking for what policy forbids is a row, never a silent override.
- **Only code readers declare; test pins do not.** A pin's class is its
  assertion's shape by the inventory's own rule. The four test helper
  modules are code and are in.
- **The population is every top-level unit of every tracked `.py` outside
  `tests/test_*.py`, and no list of calls selects it** (reframed
  2026-10-12 at the owner's review). The frame of 2026-10-08 found readers
  from a list K1 of reading calls, which is an enumeration over an open
  domain with a quiet failure direction — the shape #868, #860, #836 and
  #870 each took rounds to learn. The default is inverted: a unit is exempt
  from nothing and writes `Reads: nothing — <why>` where it reads nothing;
  K1 stays only to refuse a `nothing` on a unit whose body calls a listed
  primitive. `spec.md` §*How a reader is found* weighs (a), (b) and (c)
  and states what (b) costs and cannot see; the owner asked for the
  weighing, not for the choice, so it is not a row.
- **Module bodies are the one corner K1 still selects**: a module whose
  body reads outside any unit (14 at 81037623, provisional) declares in
  its module docstring; a body K1 does not select owes nothing. Full
  inversion there would cost about 251 lines for 14 sites
  (`plan.md` Alternatives); the limit is stated and counted by phase 1.
- **Units inside `tests/test_*.py` stay out**, by one rule on the file name
  and not by a list, and the exclusion is measured: 1,671 non-test `def`s,
  692 calling a listed primitive, at 81037623. The owner's Q1 answer took
  the frame with test functions out; widening is one exclusion deleted,
  weighed after the census has shrunk.
- **The transition is a census that only shrinks**, hashed with the ledger's
  own functions. Under the inverted rule it starts near 1,562 lines and need
  not empty on a schedule: an untouched unit costs nothing listed, a touched
  one declares. How much #834's build shrinks in bulk is #834's (Q7).
- **The build's first phase is the measurement**, at the tree #836, #866,
  #870 and #868 leave, because four siblings are still open and every count
  this frame carries is the reading of 81037623.
- **Rule 2 is a `## Removes` section in `spec.md`, read by the records arm**
  as claims of absence; not a ratchet, not a pull-request-body reader, not a
  second script.
- **The per-phase removal table retires**, because it is a second record of
  the fact the section records once.
- **The `docs/` home is a new document**, `docs/the-reader-registry.md`,
  because no document owns the area (settle §2); the rules' one-sentence
  statements go in `CONTRIBUTING.md` §*What a change to a gate must carry*
  with links.
- **The item lands after #836, #866, #870 and #868 have squashed into
  `release/v0.21.0`, with that branch merged in, and before #834's build.**
  The order is the cost control (`plan.md` §*Operational impact*); it changes
  when the item ships, not what it builds.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The reopen comment on #835 says "the registry the test reads is the inventory table, given its `docs/` home by #834's build", and #834's spec says "the table's permanent home under `docs/`". This frame puts the table's judgments into the code's docstrings and gives `docs/` the rule, because a table every reader change edits is the shared registry `CONTRIBUTING.md` §*House rules* refuses, the inventory is 2,287 lines against a 1,000-line ceiling, and a table beside the code is the copied judgment #834 found disagreeing with itself. Does the owner want the table under `docs/` anyway? | a person (the repository owner) | (a) as framed: declarations in the code, `docs/the-reader-registry.md` states the rule, the inventory's parts stay in #834's directory as the reading of a moment. (b) a table under `docs/`, which needs an `Over the ceiling` entry or a split into eight documents, is a shared file across parallel branches, and leaves the code's docstrings a second copy. (c) both: the docstrings as the registry and a generated listing under `docs/` regenerated at each release by #834's script — a file no branch edits, which is the one shape of (b) the house rule allows; it costs a generator and a release step | (a) | ✅ (a), the repository owner, 2026-10-08: as framed — the `Reads:` line in each reading unit's docstring and the shrink-only census are the registry, and `docs/the-reader-registry.md` states the rule; no table under `docs/` |
| Q2 | Does `evidence_check.py#py_spans` key a top-level function by its bare name and a method by `Class.method`, so that the census's `path#unit` is the ledger's own spelling and `resolve_unit` finds it? | a measurement | the build runs `py_spans` over one hook and reads the keys; if a top-level unit's key is not its bare name, the census writes the key `py_spans` gives, and the document says so | the keys are the ledger's spelling (`docs/the-evidence-ledger.md` cites `path#function` and `path#Class` that way) | ⬜ |
| Q3 | The population and the census at the tree the landed siblings leave, and the backfill's drift cost there. The framer's probe at 81037623 read 1,562 top-level units outside `tests/test_*.py` (657 calling a listed primitive, 195 with no docstring), 14 reading module bodies, and 2,404 released ledger anchors on 952 of those units — every one provisional, because #836, #866, #870 and #868 add and remove units before the build; the probe also matched `load` bare and counted four of this repository's own loaders as `json.load`, so the walker's import resolution will move the K1 numbers | the work | phase 1 measures with the walker the test will use, records every count with the SHA in `phases/phase-1.md`, and phase 4 writes them into `docs/the-reader-registry.md` as the reading at landing | the numbers above, read 2026-10-12 at 81037623 | ⬜ |
| Q4 | Where in `file_claims` the `## Removes` section's lines are cut, and whether `claim_lines` or a sibling function carries the section state; the status word for a named removal that still stands and its exit grade | the work | phase 2 reads `claim_lines`' aside state and cuts the section the same way; `STANDING` is the word unless a vocabulary test refuses it, and it is graded as `NOT_IN_TREE_STATUS` is | `STANDING`, graded like a stated name the tree lacks | ⬜ |
| Q5 | Has #867's one config reader landed when the `## Removes` phase starts? | a measurement | if yes, `Removes from` reads through it; if no, `frozen_from` is generalised to `cutoff_row(root, item)` and `frozen_from` calls it, so one reader exists either way (`plan.md` §*Seams*) | read the tree at the phase's first commit | ✅ yes, read by the framer on 2026-10-12 at 81037623: `evidence_check.py#config_rule` (:3997) returns `hooks/config.py`'s `(config_text, config_rows, value_of)` or the vendored trio, and `#frozen_from` (:4011) reads through it. Phase 3 still generalises `frozen_from` into `cutoff_row`, so the two rows have one reader |
| Q6 | The value of `Removes from`: every 0.21.0 work item framed before this item lands must stay unbound, because their fragments are still live on the release branch until the fold | the work | the build writes the epoch second of the write; a sibling framed after that second is bound | `date +%s` at the write. Re-checked 2026-10-12: still holds — the four open siblings were framed on 2026-10-07 and reframed in place, their ids are older than any second the build will write, and a reframe does not change an id | ⬜ |
| Q7 | How much of the census #834's build shrinks in bulk, and when. Every `Reads:` line written on an anchored unit drifts its released rows and owes a `Re-read ·` row under the freeze: 2,404 occurrences on 952 units at 81037623, provisional, re-measured by phase 1. The inventory rowed 680 code readers; the rest of the 1,562 would take `Reads: nothing` lines from the inventory's own reading, or stay on the census until touched. The run's review calls the re-read cost structural and opens the ledger's premise for 0.22.0 | a person (the repository owner, with #834's frame, after #836's test rows land) | (a) #834 writes lines for the rowed units only, and the unrowed stay on the census until touched: the smallest drift, and `grep -rn "Reads: guess"` is complete for the readers the inventory found. (b) #834 backfills every population unit at once: the census empties and the whole drift is paid in one fragment. (c) (a) now, (b) at a release as a fold fragment, with #836's test rows carrying what they can | (a); nothing in this item's build changes with the answer, and the census makes any of the three a choice #834 takes later | ⬜ |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is ticked by whoever answered, never by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
