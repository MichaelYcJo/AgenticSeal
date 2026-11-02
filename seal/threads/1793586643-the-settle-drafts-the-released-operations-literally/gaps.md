# Closing memo: 1793586643-the-settle-drafts-the-released-operations-literally

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at the branch's HEAD; the phase ran only its boundary set (`frame/questions.md` Q1) | answered: `trail/gate.md`, the `Broad gate` row passed at `a45626d5e` against `30ba21373`, and `guarantee.md` sealed on it |
| closed That `settle.py#draft` writes `\n` as itself on Windows: its `open(..., newline="")` is the one unit whose mutant survived here, since on POSIX `\n` is already the line separator. `test_draft_creates_and_deletes_whole_documents` reads the bytes and goes red there if the write translates | answered: #1292's `tests` run 41384983409 at `3ef45ba3a` passed on its four `windows-latest` legs and every Linux leg; `tests/skills/test_settle.py#test_draft_creates_and_deletes_whole_documents` carries no platform skip |

## Not done

A block that opens on the line right after a table's last row, with no blank line between them, is read by `rule_changes.py#_last_row` as a further row of that table, so a table-row `add` lands after it. GFM ends the table there. Telling where another block begins is a second reading of CommonMark's block starts, and every table in this repository's policy root ends at a blank line, so the draft leaves that case to the settling session, which reads every section the draft wrote.
