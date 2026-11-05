# Closing memo: 1793862999-unverified-baseline-is-run-by-a-person-only

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, lint and typecheck at HEAD | orchestrator, at the broad gate |
| `Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link` on Windows, where `symlink_or_skip` may skip it | orchestrator, reading the pull request's Windows CI leg |

## Not done

Phase 1 left the relaxed reading of a record at a ref in place, although
after that phase it has no shipped caller. That reading is `check_text`'s
`heading` and `strict_header` arguments and the ref arm of
`open_record_rows`. `settle.py` calls `open_record_rows` with `ref` None
only. The frame phase 1 built to kept it. The orchestrator's judgment of
2026-11-05 (`frame/plan.md` *Judgments of the run*) sent it to the framer,
and design *Scope* item 12 now removes it in phase 3. Phase 2 did not touch
it, so at phase 2's commit the reading still stands in the code.
