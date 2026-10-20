# 1792449518-settle-squashes-specs-into-docs-in-place — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 79c07d24 |

## What this phase was asked

The model in the prose (S15). `skills/implement/SKILL.md`: the lifetime-table
row, the §1 clause sentence and the §3 file-set row for `spec.md`.
`agents/framer.md`: write `## Rule changes` as `skills/settle/SKILL.md`
§*Rule changes* states it (a pointer, no grammar), pick the place from the
index, read the source as `docs/` plus the unsettled specs in merge order,
and the round-record sentence in step 4. `templates/sdd-questions.md`'s
feed-back line, `docs/the-record-layout.md:278`, both editions of
`docs/one-root-by-lifetime.md` where they say the session writes or that
`settle` replaces by provenance id, and `README.md:116` with
`README.ko.md:111`. Each sentence rewritten, never extended.

## What this phase found

- The model has one home, the `docs/` row of the implement skill's
  lifetime table. Stated in the framer and both READMEs as well, it tripped
  `tests/test_no_passage_is_pasted_into_a_second_file.py` (34 shared 15-word
  runs with `README.md`), so those three point to the table instead.
  `#test_the_implement_skill_states_the_model` pins the home and
  `#test_every_other_carrier_points_to_the_model` the pointers.
- The framer's new rule, *A spec states its rule changes*, points at the
  model, the grammar and the index, and restates none of them;
  `tests/test_waiver_decided_at_start.py::test_the_framer_writes_rule_changes_from_the_index`
  holds it, including that no grammar field line appears in the file.
- The same class as `docs/the-record-layout.md:278` stood in four more
  documents: `docs/measuring-a-run.md`, `docs/the-agent-set.md`,
  `docs/the-broad-gate.md` and `docs/the-pact.md` each opened "a work item
  that finds it wrong corrects it". Each now points to `docs/README.md`,
  which states the rule once in the new model (phase 4 moved line 278
  there). The implement skill's §6 *Needs a decision* row was the same class
  and now reads as an `add` in `## Rule changes`.
- `docs/one-root-by-lifetime.md` and its `.ko.md` edition: the
  *What keeps `settle` light* bullets on incremental folding and provenance
  ids, and the dated rows *What `settle` is*, *Where the fold record lives*,
  *What a removal actually breaks*, *Who may write in `docs/`*, the spec-less
  row's "beside the fold record" and *When the process record leaves* were
  rewritten in place in both editions. The dated sections say they are not
  rewritten; the frame's Grounding asks for the rewrite, and
  `overview.md` records it.
- `skills/implement/orchestration.md` said the `<!-- specs/<id> -->` marker
  is "a fold writes"; it now names the changelog gather, which still writes
  it.
- `git grep -n "one writer that does is" -- ':!seal/specs' ':!changelog'`
  returns only the case that asserts its absence.
- Both new pins were seen red with the four carriers stashed back to HEAD's
  text (5 failed), then green.
