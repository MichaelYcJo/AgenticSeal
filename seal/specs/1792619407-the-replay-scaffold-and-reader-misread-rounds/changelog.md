### Fixed

- **The warden's false-finding rate counted lines that are no finding, and
  a side kept nothing a corrected reader could read again (#986).** The
  harness matched every `location:` line of a printed round record, a
  fenced fix block's among them, and a side kept only those matched lines.
  A side now keeps the record whole, as `report_text`, with each user path
  and host the identifier scan refuses replaced by the fixture one. Its
  findings are read by `chain_check.py#finding_spans` over the lines the
  check's shared reader leaves, so a line in a fence or a comment is no
  finding, and a finding in a shape the check refuses still counts as
  false. A record holding a comment or fence that never closes is one the
  check refuses and reads as no finding; it counts one false finding for
  each raw finding heading, fenced ones included, and finds no truth. A
  `truth-` grader over the round record is graded on
  those findings. `compare` and `regrade` refuse, with exit 2 and the side's file
  named, a side that keeps no `report_text`; every side committed before
  #986 is one.
- **A seeded case cited round records and commits its clone did not hold
  (#986).** It was built on the shipped squash commit with the work item's
  rounds removed, so the tree named records that were gone and branch
  commits no squash reaches. It is now built at the work item's round 1
  target against round 1's base, the tree the first review saw. Each
  finding round 1 fixed that round 2 confirmed is a `truth-` grader beside
  the seed. The amend keeps the target's committer and date, so the log
  does not point at the seed's commit. After it, the scaffold removes the
  remote, so a bare `git fetch` fetches nothing, then expires the
  reflog, removes `FETCH_HEAD` and prunes what nothing reaches, so the
  target's original commit is gone from the clone. The scaffold's check of
  the line it mutates reads a trailing carriage return as the line's end,
  so a case also builds where git checks files out with CRLF line ends, as
  git for Windows does. The cases are `seeded-279a580b`,
  `seeded-ad447367`, `seeded-8a100e13` and `seeded-f1c9932d`.
  `seeded-4d316179` takes no seed at its round 1 target. In
  `seeded-9b644676` two of round 1's truths accept one line. Both were
  replaced by the next smallest shipped commits that build.

### Changed

- **The warden's suite takes effect from a stated point (#986).** The point
  is the squash commit that lands #986 on `release/v0.22.3`. From it, a
  warden comparison runs both sides on the seeded cases built at round 1's
  target, and both keep `report_text`. No side taken before it compares
  with one taken after it.
