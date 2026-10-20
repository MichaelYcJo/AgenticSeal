# The dash shapes become field words (#1000) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.

- *How many records need the one-shot conversion?* None. 0 of 119
  `overview.md` open `## Not verified` with `none`; 0 of 13 `guarantee.md`
  carry a dash verdict; the 13 `; earlier run:` entries are each the bare
  word `withheld` (executed at cf351470, `spec.md` *Data & interfaces*). So
  no script is written (`plan.md` A5a).
- *What does `## Not verified` take?* The no-change block `- nothing` /
  `  why:`, which `## Rule changes` and `## Removes` already use, read through
  one function (`plan.md` A1a).
- *What does the verdict take?* `Verdict: withheld reason: <…>` and
  `Verdict: undecided question: <…>`, one line, #941's `check: none reader:`
  shape (`plan.md` A2a).
- *Is emphasis still read through?* No: exact spelling is the owner's
  direction of 2026-10-20, and the round record's labels already refuse it
  (`docs/the-review-record.md` §*The round record*; `plan.md` A2c).
- *What replaces the `—` shape cell?* Nothing: the three rows move to an
  `| Old spelling | Means |` table. The issue's comment gave `none` as an
  example and left the spelling to the frame (`plan.md` A3a, A3b).
- *Which `docs/` text changes in the diff?* §*The round record*, because
  `chain_check.py` loads it and its own paragraph says the table and loader
  change in one commit. §*The guarantee*'s sentence goes through
  `## Rule changes` (`plan.md` A6c).
- *Do installed repositories' old overviews go red?* Yes, refused naming the
  block, as U+2705 is (`unverified_check.py#OLD_MARK`); a base revision
  still reads the old line. Stated in `plan.md` *Operational impact*.
- *Is #953's four-space continuation the same near miss?* No: it is refused
  at its line, never misread, and a `to:` value needs more than one line
  (`plan.md` A4a).
- *Is the changelog heading `## X.Y.Z — <date>` in scope?* No: only
  `gather_changelog.py` writes and reads it, and the released files carrying
  it never change (`spec.md` *Scope*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | `release: X.Y.Z — <symptoms>` is the same class: the release session types it, and `.github/scripts/publish_release_note.py` reads it with `\s+—\s*`, so a hyphen in its place drops the symptoms and the title falls back to the tag name. Should this item take it? The tree cannot answer it: the issue says this item "takes the rest", while the line a release session copies is `docs/release-checklist.md` §*5. The release pull request* (and §*6*, `docs/branch-and-release.md`), which a pull request may not edit. Through `## Rule changes` the next release's session would still copy the dash line, and the changed reader would drop its title. A ticket asking for what policy forbids is a person's question (`skills/implement/SKILL.md` §*1*) | a person | (a) leave it out: the orchestrator opens a follow-up issue for the release line, with its reader, its two `docs/` homes and the release session's copy changed together; (b) take it here, editing the two `docs/` sections in this diff on the same ground as §*The round record*: the line and its reader must move in one commit, or the next release's title is lost | (a): not built here | answered 2026-10-20 by the repository owner, asked by the orchestrator: (b), take it here. The line, its reader and its `docs/` homes change in one commit; the shape is colon field words, read whole, with a stated fallback naming what it expected; published notes and merged titles keep the dash and are not read again (`spec.md` *Data & interfaces*, `plan.md` A8a and phase 4) |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

Answered rows feed back into `spec.md`'s `## Rule changes` (a policy clause
or an open-questions section) before this directory's work merges.
