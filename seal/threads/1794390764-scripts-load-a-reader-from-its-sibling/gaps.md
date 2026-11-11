# Closing memo: 1794390764-scripts-load-a-reader-from-its-sibling

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1: the full suite, lint and typecheck at HEAD; the phase ran its phase-boundary set alone | the orchestrator, by the broad gate |
| Phase 1: `lib/sibling.py#_same` on Windows, where `__file__` and the path `load` builds may differ in case or separator, and `normcase` with `realpath` is what makes them one; no case runs on Windows here | CI's `windows-latest` job |
| Phase 1: `frame/questions.md` Q1 outside the phase-boundary set: whether a test file the set does not hold meets one `lib/` module instance shared by every script in its `pytest` process | the orchestrator, by the broad gate |

## Not done

Phase 1: the guard inside a function, which would keep a copied-alone
`settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py` at
exit 0 for `--help`. It was within reach and not taken: the guard would be
spelt in each getter or behind one more getter that every call goes
through, and the reason `frame/design.md` *Scope* item 2 gives for the
lazy placement, G10, holds at import for these four.
`trail/phases/phase-1.md` *What this phase found* gives the grounds and the
measurement.
