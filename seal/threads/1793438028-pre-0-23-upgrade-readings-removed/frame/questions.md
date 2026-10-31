# Questions for the planner: 1793438028-pre-0-23-upgrade-readings-removed

## Judgments the ticket left open that the tree answered

- Which readings beyond the issue's list are in the class, and which stay:
  `frame/design.md` *Scope* (the method, items 5 to 10, and *Out of scope,
  found and kept*).
- `hooks/stub-remove.py` goes with the rest: `frame/design.md` *Grounding*,
  the row on `hook-install.py`, and `frame/plan.md` Alternatives A.
- The `renames` entry of `.claude-plugin/marketplace.json` stays:
  `frame/design.md` *Grounding*, the row on the platform's reference, and
  `frame/plan.md` Alternatives F.
- `skills/settle/scripts/rule_changes.py#EARLIER` stays: `frame/plan.md`
  Alternatives G.
- How `docs/the-routing-check.md` changes so the stub test can leave in this
  pull request: `frame/plan.md` Alternatives C1 to C3, and the executed
  probe in its *Technical context*.
- Pins are deleted, not rewritten into their opposites: `frame/plan.md`
  Alternatives D and E.
- Which `KEPT_OLD_NAMES` items stay until the settle: `frame/design.md`
  *Removes*, the census row, and *Grounding*, the 1793240969 precedent.
- Which release the release note sends a person through: `frame/design.md`
  *Scope*, *The release note*. Any release from 0.23.0 to 0.26.x carries the
  moves, and 0.26.0 is the last that carries every one. The marketplace's
  `#<ref>` form is read from the platform's reference and has not been run,
  and the fragment says so.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `seal.py#carries_clone` stay as a helper once it reads `PLUGIN_CLONE` alone, or fold into `#workflow_at` and `#remove_workflow`? The tree cannot answer it before the edit: it depends on how the two callers read once the second arm is gone, and both give the same behaviour | the work | (a) Keep the helper: one name for "this plugin's clone line", read by both callers. (b) Fold it: two `PLUGIN_CLONE in text` tests and one name fewer | (a), unless phase 3 finds the helper's docstring has nothing left to say | open |
