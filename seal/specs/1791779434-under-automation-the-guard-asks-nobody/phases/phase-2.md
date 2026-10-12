# 1791779434-under-automation-the-guard-asks-nobody — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 4e733f57 |
| Ran by | unknown — the spawn prompt named neither the agent nor the model, and a segment does not supply that value about itself |

## What this phase was asked

The documents, the orchestration paragraph, the ledger fragment, and a
`Corrected ·` citing row for the released 0.20.0 S6 row. The ledger is
frozen, so no file under `seal/releases/` is edited. M2 is this phase's
measurement and decides the wording of §*Known limits* and of In 3's
paragraph. Write `overview.md` at the end.

## What this phase found

**M2, executed over this machine's transcripts: both events keep the id.**
Of the 115 main transcripts under `~/.claude/projects/` on 2026-10-12, 20
compaction boundaries (the system entries the harness writes at each
compaction, read by their subtype) each
sit under their file's own session id, and none under another. 8 transcripts
hold entries under one id from more than one CLI version (one of them three:
2.1.260, 2.1.263, 2.1.265), which only a later process appending to the same
file under the same id produces, that is, a resume. No transcript holds
another session's id. So the wording names a `/clear`, a new `claude` start
and another machine, and says `claude --resume` and compaction keep the
press. That a `/clear` and a new start issue a new id is still assumed, as
`questions.md` M2 assumed it, and `overview.md` carries it as unverified.

**A loaded file may not name an unreleased version.**
`tests/test_release_hygiene.py::test_no_loaded_file_names_a_version_at_or_above_the_running_one`
refused the first drafts of the Known limits bullet and the orchestration
paragraph, which named the release run by its version. Both now say "a
release run" and cite #894. The changelog fragment, which is not a loaded
file, names it.

**The document edits drifted 48 rows** citing `## Decision matrix`, `##
Known limits`, the routing section of `skills/implement/orchestration.md`
and two headings of `skills/code-review/orchestration.md`. Each claim was
read first, and none speaks to the dirty row, the press's locality or a
resume, so all hold as written. `--reverify --into` wrote three `Re-read ·`
rows here (0.12.0's two routing rows and 0.15.5 A2) and re-stamped in place
the rest, in this fragment and in three other work items' fragments
(`1791384154`, `1791384157`, `1791384160`).

**What the frame left to the orchestrator stays there.** P1's default (a)
puts one sentence in §*Known limits*, which is written, and an issue for the
two choice rows, which this session cannot file (it posts nothing). Neither
`CLAUDE.md` nor `templates/claude-md-block.md` gained a link row, as
`spec.md` §*Out of scope* says.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| none | none |
