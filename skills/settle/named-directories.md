# settle, the directories a person names

The settling session opens this file where the person's answer to the first
question of `skills/settle/SKILL.md` *Directories a person names* names a
directory, before step 2 of that file's *The settling session's procedure*
runs the dry run with `--from`.

## Directories a person names

**`--from` refuses four things, each with exit 2 and one sentence, and reads
and removes nothing**: a path that names no directory in the working tree,
a path outside the repository, the `seal/` root or a path under it, whose
records the settle already reads, and `--from` beside `--apply`. `--apply`
removes only under `seal/threads/`, and a flag it accepted would read as
one it acted on. Each sentence about a path names it as it was read, from
the directory `seal settle` runs in. A named directory holding no document
is listed with 0 documents.

**The listing is not a proposal.** Each of its lines is what git answers
about one file, as `skills/settle/SKILL.md` *What the dry run shows* gives
them: its path, its two
commits, and whether the working tree changed it. The script reads no
document's content, so a line says nothing of what the document decides,
which section it bears on, or whether it is promoted, and neither does the
document's place in the listing, its directory, its name or its extension.
The proposal is the settling session's to write, and the mark is the
person's.

**The settling session writes one proposal row per document**, after
reading the document whole with the code it bears on:

- **The place** is named as an operation of `skills/settle/rule-changes.md`
  *Rule changes* names one: a `file` picked from the index
  (`skills/settle/rule-changes.md` *The index*) and a `section`. It names an
  existing heading, or a new section or a new document marked as new. A
  document bearing on several sections names each in its one row. The
  document's own headings decide nothing.
- **The proposal** is `promote` or `skip`.
- **The grounds** say what a promote writes, read from the document and
  checked against the code. A document holding one decision the code bears
  out and one the code has left is proposed `promote`, with grounds naming
  the first alone. A plan not yet built, a decision the code has since
  left, a document whose decisions bear on no section of the policy, and a
  file of the `seal/` root are each proposed `skip`, with that reason as the
  grounds.
- **A document skipped at an earlier settle** is proposed `skip` again, with
  grounds naming that settle's pull request, where two facts hold: the last
  settle's pull request body holds the document's row marked `skip`, and
  the document's last change is a commit that settle's merge commit reaches
  (`git merge-base --is-ancestor <last change> <merge commit>` exits 0). The
  session finds the last settle's pull request from the latest settle's
  commit among those that changed the policy root, since a work item whose
  subject is the policy root changes it too (`skills/implement/SKILL.md`
  *Document layout — two roots, three lifetimes*). Every other document is
  new, a document no
  commit adds among them.

**The second question puts the numbered table to the person once**, before
the first edit, in this shape:

| # | Document | Place | Proposal | Grounds | Mark |
|---|---|---|---|---|---|

The `Mark` cell is empty in the question and holds the person's mark in
the pull request body. The answers are "as proposed", "skip every row", or
the numbers of the rows whose mark the person flips, and every answer
continues. A listing that holds no document asks nothing.

**Only a row the person's answer leaves marked `promote` is written, and it
is written as a released design's operation is.** It joins the group of the
place it names, and the group is ordered by commits, the listing's beside
the designs', a document deciding as of its last change. The session writes
the section as the group's latest decision checked against the code, in its
own words and with no marker, and the section's grounds cite the document
by its repository path, as the paragraph on reference roots under
`skills/settle/SKILL.md` *What `--apply` does* asks of a statement a settle
writes.

**A named directory is read and never written.** No step of the settle
writes, moves or removes a file under it, and `seal settle --apply` removes
only under `seal/threads/` and refuses `--from`. A promoted decision reaches
the policy root in the settling session's words with the document's path,
and the document stays where it was, as it was.
