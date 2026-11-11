- "A13. The guard stands inside the function that first loads, in `settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py`, so a lone copy still prints its help at exit 0" (`frame/plan.md` *Alternatives considered*, rejected: a lone copy of those four run with `--help` now exits 2)
- "A14. `loaded_by` reads a tracked path only where it is handed to `sibling.load`, in the call or through a module-level name" (`frame/plan.md` *Alternatives considered*, rejected: it drops `skills/settle/scripts/fold_check.py` with the eight files, so the walk reads every tracked-path string and leaves out only those under `tests/`)
- "A17. The moved cases keep the module name they read, so that `seal layout --moved` passes, and *Scope* item 10 changes in place of S8" (`frame/plan.md` *Alternatives considered*, rejected: S8 compares the moved cases with module names read as one)
- "The merge `f55d551de` took #1488, whose `test_release_hygiene.py` case kept the chain check's reader-path assert with a comment; the resolution keeps that comment over this branch's `lib/lines.py`" (`frame/plan.md` *Judgments of the run*, the row of the merge)

Closes #1482.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
