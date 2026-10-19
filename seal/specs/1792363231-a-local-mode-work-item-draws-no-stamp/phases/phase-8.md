# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 8

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | 36c6a381 |


## What this phase was asked

`plan.md` row 8 at 1e956838 asked for the documents and the changelog
fragment to be rewritten in place to the redesign, with each pin seen red
first. The orchestrator excluded one part of the row: the mark grammar
(`chain_check.REFRAME_RE`, its refusal sentence, §*The run*'s sentence,
`templates/sdd-spec.md`'s foot comment and `agents/framer.md`). The
correction after phase 6 carries no `Reframed` line, as the plan's last
`Approved` line says, so that grammar stays as it is.

## What this phase found

**What was rewritten (executed; each pin was seen red against the text as
it stood).**

- `docs/the-review-record.md` §*The stamp*:
  - The unchecked paragraph names only the limits `spec.md` §*Scope* leaves:
    a wrong row committed past the commit gate, the chain the gate never
    reads, local mode's emptied values directory and `seal import`, and the
    coincidence of `plan.md`'s path walk. The guards' words are gone, and
    the silence for a verdict off the branch is narrowed to a local item
    whose branch cannot be read. The pin is the `silence` tuple of
    `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`.
  - The second rule's `Enforced by:` line gains
    `test_a_tracking_ref_left_by_a_rebase_withholds_nothing`. The rule itself
    and the first rule's two sentences were rewritten in phase 7, because
    removing the cases left their citations dangling.
- `docs/the-commit-gate-inside-git.md`:
  - A new rule under this item's marker, after the arms. It covers what the
    refusal reads and from where, the record it writes, the one way on, what
    it does not judge, that it is no arm, and where the stub does not run.
    The pin is `test_the_policy_states_the_guarantee_refusal_beside_the_arms`,
    new, in that document's test module.
  - The latency bullet gains phase 6's figures.
- `skills/code-review/orchestration.md`'s sealer step: a commit refused for
  a row naming a commit the branch does not hold is answered by the sealer
  again at HEAD, never by editing the row. The pin is
  `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`.
- Both READMEs:
  - The side-effect sentence says who writes the record's directory in each
    mode.
  - The git-hooks row names the third refusal and that it has no waiver.
  - The pin is `test_both_readmes_list_the_stamp_hook`, which also asserts
    that the old sentences are gone.
- `changelog.md`'s second entry is rewritten to the refusal at the commit,
  the record, the limit left and the measured latency.

**Where the build departs from row 8.**

- `hooks/sealer-stamp.py`'s docstring is unchanged. It names no refusal
  record, so it holds no sentence that a removed fact stood on.
- `docs/the-review-record.md:284` named `specs/<id>/guarantee.md` with no
  root. `tests/test_no_document_names_the_old_roots.py` refused that line,
  and it had been refusing it since phase 4 wrote it (12855a96). The
  sentence sits in the section this phase rewrites, so it now reads
  `<git-common-dir>/seal/specs/<id>/guarantee.md`, and its pin follows.
- S8's second `git grep` hits the record's directory and functions in both
  modes, because the corrected frame has the commit gate write the record
  too. It also hits `hooks/worktree-guard.py:2123`, where `"reflog"` is a
  git subcommand in a list that has nothing to do with the stamp. Nothing
  it hits describes a reflog guard, a patch-equivalent copy, another ref or
  a count of guards. S8's first `git grep`, for `#976`, exits 1 outside this
  item's directory, #975's, and `changelog/0.22.1.md`.
- During the work an `Edit` replaced the opening of the arms rule's
  `Enforced by:` line in `docs/the-commit-gate-inside-git.md` with a
  placeholder. A second `Edit` restored it before anything ran, and `git
  diff` showed only the latency bullet changed at that point. The commit
  carries the line unchanged.

**Checks (executed, one module a command).**
`test_the_stamp_reaches_the_person_it_is_drawn_for.py` 101 passed and
`test_the_commit_gate_decides_at_the_commit.py` 185 passed. Each of these
exited 0: `test_docs_line_wrap.py`, `test_one_word_one_meaning.py`,
`test_no_real_identifiers.py`, `test_no_document_names_the_old_roots.py`,
`test_no_passage_is_pasted_into_a_second_file.py`,
`test_the_changelog_is_gathered_at_release.py`,
`test_chain_hooks_hardening.py`, `test_release_hygiene.py`,
`test_broad_gate_rule.py`,
`test_a_parallel_agent_names_its_scratch_after_the_work_item.py`,
`test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`test_a_section_marked_for_one_role_reaches_only_that_role.py` and
`test_the_sealer_guarantees.py`. `bin/rules --check` exited 0. `git diff
--stat 11b90191 HEAD -- agents/` is empty (S9). The full suite is
unverified here, and the orchestrator's broad gate answers it.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
