# Closing memo: 1793862999-unverified-baseline-is-run-by-a-person-only

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, lint and typecheck at HEAD | orchestrator, at the broad gate |
| `Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link` on Windows, where `symlink_or_skip` may skip it | orchestrator, reading the pull request's Windows CI leg |

## Not done

The relaxed reading of a record at a ref stays, although after this change it
has no shipped caller. That reading is `check_text`'s `heading` and
`strict_header` arguments and the ref arm of `open_record_rows`. `settle.py`
calls `open_record_rows` with `ref` None only. Design *Scope* item 4 keeps
`open_record_rows` and `_text_at`, and A4 keeps the relaxed reading, so I
did not remove it. Whether it goes is the orchestrator's decision.
