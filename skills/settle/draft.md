# settle, the draft

The settling session opens this file before it runs `seal settle --draft`,
which step 4 of `skills/settle/SKILL.md` *The settling session's procedure*
takes where the session chooses to.

## What `--draft` writes

**`seal settle --draft` writes a starting text for step 4 of the procedure,
and no section it writes is settled.** It reads what the dry run reads, and
writes each operation of each design the dry run groups into the policy root
in the working tree, where `skills/settle/rule-changes.md` *Rule changes*
places its kind. The designs
come in merge order, a design's operations in the order it lists them, and
each operation is written over the text the earlier ones left. A superseded
operation is written like any other, because the script has no notion of
which decision is latest. It creates the document an `add` with no `section`
names, deletes one a `remove` leaves empty, keeps each document's line ends,
and writes nothing outside the policy root.

- **What it prints.** One line for each operation it did not place:
  `not placed`, the operation's kind, its work item, its design's coordinate,
  and the reason. The reason is one of these: the document or the heading is
  not there, the heading is there twice, the `from` is not in its section
  exactly once, or an `add` with no `section` names a document that exists.
  The operations after one not placed are written all the same. The last two
  lines count the operations placed of all of them, and send the settling
  session to step 4. It exits 0 whatever it placed, since an operation not
  placed is no verdict.
- **What it refuses.** `--draft` beside `--apply`, or beside `--from`, exits
  2 with one sentence and writes nothing. A root holding no work item prints
  its settled line and writes nothing.
- **It is run once, before the first edit of the policy root.** It writes
  over the policy root as it stands, so a second run writes every operation
  again over what the first wrote. No guard stops that.
  `git checkout HEAD -- <policy root>` followed by
  `git clean -f -- <policy root>` returns the root to `HEAD` before a second
  run.

**The script answers what a script answers exactly, and the settling session
judges the rest.** The draft answers where the grammar places each
operation, and whether its heading and its `from` stand there once. Every
question of meaning stays the settling session's, as step 4 states: which
operation is a group's latest decision, and what an earlier one it restates
leaves standing; whether a section the draft wrote reads as one rule, or
holds a check line with the old paragraph still running on below it; whether
a sentence still names what another design removed; how each operation not
placed is written; and whether the code has moved past the decision. A
section the draft wrote is a listing of what the designs said, in place, and
is decided no more than the dry run's groups are.
