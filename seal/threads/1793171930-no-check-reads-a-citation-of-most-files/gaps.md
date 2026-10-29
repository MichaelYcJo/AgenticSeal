# Overview: 1793171930-no-check-reads-a-citation-of-most-files

## Why this work exists

A heading renamed in any file but `skills/implement/SKILL.md` left its citations pointing at nothing with the suite green; one case now resolves every citation outside the records, and the three it found dangling are corrected.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A census row naming the removed reader | `frame/design.md` *Removes* names the reader's scopes, and not the row `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` holds for `test_the_set_a_work_item_always_has.py#cited_files` / the row is rewritten to name `test_a_cited_section_stands_in_its_file.py#citations` | code | The census fails once the scope it names is gone, and the new reader lists paths from git and applies `on_disk`, which is the class that table holds |
| Two more imports left unused | *Removes* names `import subprocess`, `import pytest` and `on_disk` / `os` and `ROOT` went unused too, and are removed | code | ruff refuses an unused import; nothing else in the module used either (`grep` executed) |
| How a `<commit>:<path>` is kept out | *Data & interfaces*: "`<path>` is the backticked text alone, with no `:` before it, so `<commit>:<path>` is never read" / the path pattern accepts a colon, and the first-segment rule keeps the citation unread | code | With the colon excluded or not, no outcome changed: a first segment holding a colon is no tracked top-level entry. S7 pins the outcome |
| Where a bold lead opens a paragraph | *Data & interfaces*: "a paragraph or list item whose text opens with `**`" / a lead is read on a list item, on the file's first line, or after a blank line; a lead directly under a heading or a closing fence is not | code | The two dropped tests changed no case's outcome, S1 is green without them, and each kept test has a case that goes red under its mutant (phase 1 record) |
| A `skill's` citation of a skill nobody tracks | *Data & interfaces* grammar table: both name forms resolve against `skills/<name>/SKILL.md` "where that file is tracked" / the form with the word `skill's` is read for any name and refused as dangling where that skill is not tracked; the bare backticked name keeps the frame's reading | code | Round 1's finding 2: the word `skill's` already names a skill, so a removed skill's citations dangle as a removed file's do under S7 (`frame/questions.md` judgment 4). The bare form keeps the filter, because any backticked word can stand before italics |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck | the orchestrator, at `seal gate` |
| Whether S1 still meets only what the frame measured once #1053's and #1040's branches land in `release/v0.24.0` (`frame/questions.md` Q2) | the orchestrator, at the rebase |
| Whether S9's warning stands in the full output `seal gate` keeps under `--keep-output`; `bin/test -q` printed it (phase 2 record), and `trail/gate.md` holds no test output at all | the orchestrator, at `seal gate` |

## Not done

nothing

## Fed back into the spec

none
