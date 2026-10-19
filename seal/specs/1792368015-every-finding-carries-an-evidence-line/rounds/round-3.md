# 1792368015-every-finding-carries-an-evidence-line — review round 3

target: ffed3c38, fixes 12660916..ffed3c38

This verifying round read the one commit after the broad run,
`12660916..ffed3c38`, which changes one line of
`tests/test_a_rewritten_definition_proved_non_inferior.py`. Round 2 opened
no finding, so it closed nothing this round owes a `confirms:` line. This
round found the change right and complete, and it opens nothing.

## Findings

## Confirmations

confirms: none
The change is right. In the `git` helper of
`test_a_labelled_record_is_read_by_the_grammar_of_the_commit_that_wrote_it`,
`text=True` becomes `encoding="utf-8"` (read,
`tests/test_a_rewritten_definition_proved_non_inferior.py:1560-1568`). With
`encoding` given, `subprocess.run` still decodes the output to `str`, so
`.stdout.strip()` and every caller of the helper read what they read before.
The encoding test and the touched module pass together, 257 tests
(executed). I restored `text=True` in the round's clone, and the encoding
test failed at `:1563` with the message the orchestrator's broad run
reported (executed). The fix is what removes that failure.

confirms: none
The change is complete. With the fix reverted, the encoding test walks the
whole tree and names that one call and no other, so the branch added no
other call that reads or writes in the locale's encoding (executed). The
branch's added I/O calls agree with that. `replay_targets.py`'s copy of each
check file opens with `encoding="utf-8"`. Its `git` helper, which the branch
did not change, already names the encoding. The new test reads and writes
through `read_text` and `write_text` with `utf-8` (executed, the diff search
in `## Probes`). The commit before it, 12660916, adds one row to
`overview.md` and changes no code (executed, `git show --stat`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate again at ffed3c38, since the last broad run was at 12660916 and an edit followed it (`unverified`) | the branch | the orchestrator's `broad-gate` run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist` | 257 passed |
| `bin/test tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py -q -p no:xdist`, with `text=True` restored at `:1567` in the round's clone, then restored | 1 failed, 150 passed; the one site named is `tests/test_a_rewritten_definition_proved_non_inferior.py:1563` |
| `git diff b196fe9b..ffed3c38 -- '*.py'`, searched for added `text=True`, `open(`, `read_text(`, `write_text(` and `subprocess.` lines | 8 added lines, every one naming `utf-8` except the helper's `subprocess.run`, whose encoding sits on its own line |
