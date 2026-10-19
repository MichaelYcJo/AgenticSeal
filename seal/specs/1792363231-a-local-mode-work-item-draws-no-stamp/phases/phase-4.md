# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 12855a96 |


## What this phase was asked

Rewrite the stamp's documents in place, so that each states the local
trigger, the refusal record and the limits that remain:

- `docs/the-review-record.md` §*The stamp*, with
  `test_the_policy_states_the_refusal_record_and_names_its_cases`, and the
  `#976` pointer at line 345 replaced;
- the orchestration's stamp paragraph;
- the hook docstrings and `seal_stamp.py`'s comments;
- both READMEs' stamp sentences;
- `agents/sealer.md:99-100`.

Write the changelog fragment. Open `overview.md` and record guard 3 as a
divergence: `spec.md` S13 says four guards, the build has three, and the
grounds are that guard 1's order leaves guard 3 nothing to decide, shown by
mutation. The documents state three guards. In the orchestration file, edit
only the stamp region, because #943 edits that file elsewhere.

## What this phase found

**The orchestration path in the spawn message did not hold.** It named
`skills/implement/orchestration.md:241-265`, but that file holds no stamp
text. The stamp paragraph stands at `skills/code-review/orchestration.md:241`,
the path `plan.md` row 4 gives, and the edit stayed inside that paragraph.

**Each rewritten sentence was pinned before it changed (contract §14,
§15).** The six document cases were rewritten first:

- `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`
- `test_the_form_bullet_says_what_draws_the_final_seal`
- `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`
- `test_both_readmes_list_the_stamp_hook`
- `test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it`
- `test_the_policy_states_the_refusal_record_and_names_its_cases`, which is
  new

Against the unchanged documents all six went red, exit 1, 6 failed. Each
went green once the documents changed.

**Every other place that tied the stamp to a commit alone was found and
rewritten (contract §12, §19).** `git grep` for the stamp beside "commit",
"local", "queued" and "gap" found these beyond the plan's list:

- `skills/verify/SKILL.md`'s **Form** bullet;
- `docs/the-broad-gate.md:36`;
- `seal_stamp.py`'s module docstring, its values-file comment and its
  `QUEUED` comment.

Each now names the write in local mode. `docs/the-commit-gate-inside-git.md`
names the stamp `post-commit` queues, which still holds for shared mode, so
it stands.

**S8's grep holds.** `git grep -n "#976"` outside this work item's
directory, #975's directory and `changelog/0.22.1.md` hits nothing. The new
case checks that the policy carries no such pointer, and it spells the
pointer in two pieces, so the check does not trip the grep it states.

**§*The stamp* now has three rules, and the refusal record is the new
middle one.**

- The first rule names both triggers, the commit in shared mode and the
  write in local mode, and its `Enforced by:` line gains the nine cases of
  phases 1 and 2.
- The refusal record is a rule of its own under this work item's marker. It
  states three guards, and its `Enforced by:` line names phase 3's nine
  cases.
- The unchecked paragraph no longer names local mode among the silences.
  It names a local guarantee that arrived by a shell write or `seal import`,
  a verdict over a commit off the work item's branch, and the limits the
  refusal record leaves. It also says that nobody has watched the edit
  hook's message on a screen.

**What phase 5 meets.** `agents/sealer.md` loses the word `committed`, and
the overview's `## Not verified` names that measurement as phase 5's. The
changelog fragment carries no evaluation table yet. Phase 5 adds the
sealer's numbers to it, as #975's fragment carries its own.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
