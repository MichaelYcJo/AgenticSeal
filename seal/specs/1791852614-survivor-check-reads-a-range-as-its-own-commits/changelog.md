### Fixed

- **A fix pass's range that holds a merge of the base no longer reports
  another work item's correction as its own** (#873). `survivor-check`
  compared each file at the range's two ends, so after a merge of the base
  a sentence another work item had corrected on the base read as wording
  this range removed, and its standing copy elsewhere was reported as this
  range's survivor. Now, over `a..b`, the sweep still counts the two ends
  and keeps a removed or a written sentence only where one of the range's
  own commits removed or wrote it in that file. The own commits are the
  ones `git log --ancestry-path --no-merges a..b` lists, the rule
  `docs/the-record-layout.md` §*A range owns the commits that descend from
  its start* states for `round-record close`. Wording the merge brought in
  no longer hides an own survivor either. A range with no merge reports
  exactly what it reported before.

  `A...B`, the spelling CI and the broad gate pass, is read at its two ends
  from the merge base, as before. A change made only inside a merge's
  conflict resolution is in none of the range's own commits, so a two-dot
  range no longer measures it.

  The commits a two-dot range lists and does not own are not read, and the
  report now names them on a `not read` line with the advice to write
  `A...B` for a whole branch. So `origin/<base>..HEAD` on a branch that has
  merged its base says which of the branch's commits it left out, rather
  than reporting a clean range.

- **`survivor-check` refuses a two-dot range whose start is not an ancestor
  of its end** (#873). Such a range owns no commit, and the sweep used to
  measure it over two unrelated trees. It now stops at exit 2 before
  examining anything, naming both ends and saying to write `A...B` for a
  range whose start is on the base. A `survivors.md` row spelled that way
  is read exactly as before. A range whose own commits git cannot list,
  including a `git log` past its timeout, is refused the same way, at exit
  2 rather than a traceback.
