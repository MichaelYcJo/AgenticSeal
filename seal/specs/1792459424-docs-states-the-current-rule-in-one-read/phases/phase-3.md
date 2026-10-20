# 1792459424-docs-states-the-current-rule-in-one-read — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 346369b7 |

## What this phase was asked

The no-change block, `- nothing` with `  why:`, in place of
`nothing — <why>` in `## Rule changes` and `## Removes`: `rule_changes.py`,
`unverified_check.py#NOTHING`, `settle.py`, `templates/sdd-spec.md`,
`skills/settle/SKILL.md`, `docs/the-reader-registry.md`, and #953's spec
rewritten to it. S10's cases seen red, and `bin/settle`'s dry run listing
#953's spec and this one as nothing to apply.

## What this phase found

- **`nothing` is an item of the grammar.** `rule_changes.GRAMMAR` holds it
  beside `add`, `change` and `remove`, with `why` its one required field, so
  the field reader, the empty-value refusal and the unknown-field refusal
  are the ones every item has. What is its own: it stands alone in the
  section, and a line opening with `nothing` in any case that is not the
  block is refused at its line with `NO_CHANGE_WRITTEN`, which names the
  block. Because the vocabulary case derives its words from `GRAMMAR`,
  `templates/config.md` *What no row governs* now lists `nothing` and
  `why:`.
- **`unverified_check.py#NOTHING` is gone.** After phase 1 its one reader
  was `rule_changes.py`, which no longer reads the em-dash form. `settle.py`
  names the block in its heading through `rule_changes.NO_CHANGE`.
- **`## Removes` has no reader in code.** The block there is read by the
  review, as the table is; the template and `docs/the-reader-registry.md`
  say so.
- **This item's own `## Rule changes` does not parse.** `spec.md` line 199
  continues `why:` two spaces in, where the grammar takes four, and
  `bin/settle --released-at HEAD` refuses it at that line: "a line that is
  not a field of the item above". The phase may not write `spec.md`; the
  orchestrator or the framer owes the two spaces, and the hand-back names
  it. #953's spec parses: the same run holds it only for its open
  `questions.md` row Q4, which is #953's own.
- **The sweep of the three phases' facts.** A `git grep` for the old label,
  the cutoff row, the fold marker and the em-dash form, outside `seal/specs/`
  and `changelog/`, found five sentences still stating them: both READMEs'
  limit bullet, two lines of `agents/framer.md`, `skills/settle/SKILL.md`'s
  apply bullet, `docs/the-record-layout.md`'s settle sentence and a
  docstring in `unverified_check.py`. 346369b7 rewrites each. What the grep
  still finds is a test's planted refusal, the case pinning that the
  template no longer says it, and
  `evals/behaviour/warden/replay-1791382684-r5/prompt.md`, a recorded
  review prompt replayed as it was given, left as written.
- **The checks at the boundary (executed):** S10's cases were run red
  against 37faed02 (14 failed), then green; the settle, unverified, phase
  record, vocabulary, wrap and meta modules pass, after the vocabulary line
  of `templates/config.md` was re-wrapped in 728091c1; `bin/rules --check`
  and `bin/fold-check` exit 0; ruff clean; each unit added to
  `rule_changes.py` and `settle.py` was mutated once, and each run was red.
