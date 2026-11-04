# Questions for the planner: the behaviour suite is a smoke run (#1254)

The issue left these open, and the tree answered each one. They are not
reopened here.

- Whether rule 3 narrows too, or stays whole: `frame/plan.md`
  *Alternatives considered* A3.
- Whether a side with an unknown token, tool-call or byte figure is still
  `no result`: `frame/plan.md` *Alternatives considered* A4.
- How the three remaining rules are numbered, and what a reason line
  names: `frame/plan.md` *Alternatives considered* A5.
- What "a recorded baseline" asks to be built: `frame/design.md`
  *Grounding*, the `compare` row.
- Where the preload's bytes are read with no run: `frame/design.md`
  *Removes*, the rule 4 row.
- Whether the record's title, the script's name and the test module's name
  count among the sentences to rewrite: `frame/plan.md` *Alternatives
  considered* A6 to A8.
- Whether the suite is removed in place of narrowed: `frame/plan.md`
  *Alternatives considered* A1.
- Whether `regrade` and `model` change: `frame/design.md` *Scope*, Out, and
  `frame/plan.md` *Alternatives considered* A9.
- Whether the work edits `docs/` directly or states a rule change:
  `frame/design.md` *Grounding*, the *Document layout* row.
- Whether a pending design already changes the sentence of `docs/` this
  work changes: `frame/design.md` *Grounding*, the unsettled
  `## Rule changes` row.

Assumed, because a different answer would not change what is built:

- The new name of `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`
  is the crafter's, for what its one case holds. The phase record names it.
- The exact wording of S1's lead, of the README bullet in both editions,
  and of the docstrings S3 rewrites is the crafter's, within the claims
  `frame/design.md` *Scope* gives each.
- Whether each changed case is shown red by committing the test first or
  by running it with S2's hunk stashed is the crafter's choice. The phase
  record says which (`frame/plan.md` *Technical context*).

No row is open.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
