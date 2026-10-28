# Phase 1: 1793171930-no-check-reads-a-citation-of-most-files

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 577daff6 |

## What this phase was asked

Build the new module `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
with its reader and S1 to S8, each seen red first. S1 goes red naming the
three citations the frame lists, then green once they are fixed. Remove what
`frame/design.md` *Removes* lists. In `tests/behaviour/test_one_word_one_meaning.py`,
touch only lines 461 and 462, because #913 edits the same file at 761 and 771.

## What this phase found

**The red runs.** The cases were first run against a stub reader that read
nothing: all eleven failed, exit 1. Against the stub, S7's not-read half and
S8 failed only on their count, so each one's own red was shown by a mutant
instead. With the full reader written, S1 failed with exit 1 before the
corrections and named exactly the frame's three coordinates:
`.github/scripts/gather_changelog.py:43`,
`skills/verify/scripts/mutation_check.py:103` and
`tests/behaviour/test_one_word_one_meaning.py:461`. After the three
corrections, the module passed with exit 0. At 577daff6 the reader reads 372
citations in the tree, and none dangles. The frame's scan counted 370.

**Mutation.** Every unit of the reader was broken with `seal mutate`, in eight
batches. Each batch ran against the case meant to catch its mutants. Of 29
mutants, 28 went red on the first run. One survived: with the liveness test removed from
`sections`, S4 stayed green. Its fenced lead stood right under the fence's
opening line, so the paragraph-opening test refused it before liveness was
asked. A blank line inside the fence (577daff6) fixed the fixture, and the rerun went red.

**Three conditions were dropped because no case could tell them apart from
their absence** (393f6c9b).
- *Data & interfaces* says `<path>` has no `:` before it, so a
  `<commit>:<path>` is never read. The reader's path pattern does accept a
  colon. Such a citation is still not read, because its first segment holds
  the colon and is no tracked top-level entry. S7 pins the outcome.
- Heading text is no longer whitespace-collapsed; `rule_changes.heading_text`
  already trims it.
- A bold lead opens a paragraph where it is a list item, the file's first
  line, or follows a blank line. A lead directly under a heading or a closing
  fence, with no blank line between, is not read. S1 stays green on that
  reading.

The fixtures gained the shapes the kept conditions decide: a first-line lead,
a bold run on a paragraph's second line, a wrapped list lead, an unclosed
lead, a markdown line opening with `#120`, a markdown quote pair across a
line break, and an untracked file standing on disk.

**What the frame's *Removes* did not name.**
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`'s
  `APPLIES_THE_SHARED_GUARD` named `test_the_set_a_work_item_always_has.py#cited_files`.
  That census fails once the scope is gone. Its row now names the new
  module's `#citations`, which lists paths from git and applies `on_disk`.
  The census only finds a module that git tracks, so the new file had to be
  staged before that module could pass.
- After the removal, `os` and `ROOT` also became unused in
  `tests/behaviour/test_the_set_a_work_item_always_has.py`, besides the
  three imports the frame named. All five are removed.

**The line limit on #913's file held.** The correction to
`tests/behaviour/test_one_word_one_meaning.py` changes line 461 alone. The
`<commit>:<path>` form moved to the end of that line, so line 462 stays as it
was.

**`.test_durations`** loses the three keys the frame named. The new cases
have no timing entries. #1039 edits the same file.
