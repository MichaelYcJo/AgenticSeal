# 1791781864-the-idle-session-rows-ask-nobody — handoff

Written 2026-10-12, evening KST, by the orchestrating session, when the owner
stopped for the day. The whole run's state is in
`seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md` on
branch `chore/834-every-reader-and-record-is-inventoried`; read it first.

| | |
|---|---|
| Issue(s) | #896 |
| PR | none yet |
| State | framed by `framer` on Fable; `plan.md` approved (0b52518f); phases 1–2 built by the smith on Opus and closed at 17d7ed5f and abe3dc3e (records 79a0577a, 33ff3dd9), pushed |
| Owner's questions | P1 (b) and P2 (a), both at the default the frame is built on |

**Next act, after #894 (PR #897) lands on `release/v0.21.0`:**

1. `git -C <wt> merge origin/release/v0.21.0` (a merge, never a rebase).
   - Expect text conflicts in the module docstring of `hooks/worktree-guard.py`, in `main`, and in `docs/worktree-guard-spec.md` §A. `plan.md` §Seams names each one.
   - #835's rule applies after the merge. Every unit this branch changed that is still on `tests/undeclared_readers.txt` (`fmt_sessions`, `choose`, `main`, …) must declare a `Reads:` line and leave the census. Run `tests/test_a_reader_declares_its_input_class.py` to list them.
2. Resume the smith on phase 3, the shared documents. Its spawn report listed what phase 3 needs from #894's landed text.
   - #894's reframe left the press sentence byte-identical, so this item's copy of it stands.
   - #894's §Known limits sentence about these two rows is replaced by this item's.
3. Open the draft PR, then run the review chain from round 1 over the whole of phases 1–3.
4. Preflight, sealer, PR body, land. This item lands before #834's phase 4.

**Watch for:** the narrow runs must include
`tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` and
`tests/test_the_printed_ledger_name_is_the_file_that_was_read.py`. Also, under
`automation` on Windows, every `git switch` takes row 2's deny, which is a
cost the frame accepted (P1 (c) is the lever).
