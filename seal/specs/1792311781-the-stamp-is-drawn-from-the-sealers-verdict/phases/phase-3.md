# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | dddcdfdc |


## What this phase was asked

The words and the documents. `docs/the-review-record.md` gains §*The stamp*
between §*The guarantee* and §*The run*: the drawing rule with its
`Enforced by:` naming phase 2's cases, #717's budget paragraph moved with its
marker, and the unchecked paragraph with S10's silences.
`docs/the-broad-gate.md` loses §*Where the stamp is drawn* and gains one
sentence in §*One act, one owner*. Rewritten in place: post-commit's second
duty in `docs/the-commit-gate-inside-git.md`, the orchestrator's stamp
paragraph, `verify`'s **Form** bullet and its base-ref sentence, the sealer's
clause, the hook's and the dispatcher's comments, `bin/seal-stamp`, the
stamp module's docstring and `main`'s description, both READMEs, and the bin
inventory's description. `SEAL_SWEPT` gains the files S11 names. Every pin
the plan's row lists is run.

## What this phase found

**The frame holds; three of its coordinates were narrower or different.**

- `docs/the-commit-gate-inside-git.md:14` is the heading other documents
  cite as §*The commit gate inside git*, so it was not renamed. The second
  duty is named in the document's opening paragraph, which points at
  §*The stamp*, and its latency in the **Latency** bullet with phase 2's
  figures.
- `bin/seal-stamp.cmd` names no stamp and no gate, so it needed no change.
- §*The stamp*'s unchecked paragraph names local mode and a person's own
  commit beside S10's four silences. Phase 2 found the local-mode gap; the
  person's own commit is `spec.md` §*Scope*'s, stated here because that
  paragraph is where a person looks for why no stamp appeared.

**The class went wider than the listed coordinates** (contract §12). Every
sentence that called the broad gate's run a stamp or a seal was found by
sweeping the shipped documents for `gate's stamp`, `broad gate's stamp`,
`run's stamp`, `gate draws`, `sealed run` and `recorded seal`, and each was
reworded: `templates/config.md` (two sentences, one pinned by
`tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`),
`skills/verify/SKILL.md` (a section heading and a red-flag bullet),
`skills/code-review/orchestration.md` (the refusal paragraph and the
preflight's last sentence), `docs/commit-review-gate-spec.md`,
`docs/the-review-and-parity-arms.md`, the gate's refusal for a missing row
and two comments in `broad_gate.py`, and one docstring in
`unverified_check.py`. The sweep of the shipped tree for `SEALED` now hits
only the stamp's title row and label in `seal_stamp.py` and the verdict
constant in `chain_check.py`.

**Left standing, on purpose.** The Seal Test's own vocabulary —
`templates/config.md`'s "a default of `true` seals everything", `verify`'s
"a claim is sealed" — is the concept the sealer's seal is named after, not
an instance of the gate's run, and the gate's refusal sentences that say
"no command to seal over" name what the sealer's seal will cover. None of
them says the gate's run is sealed.

**The fold case had to learn the new members.**
`test_folding_the_seam_cannot_hide_an_instance_it_would_have_found` pins the
`.py` members the sweeps fold; three hooks joined `SEAL_SWEPT`, and
`GATE_SWEPT` is a third sweep, so the pinned set and the phrase set both
grew. Its docstring's counts were replaced by the sets themselves.

**How the pins were seen red.** Every rewritten pin was run against the
documents as phase 2 left them: ten failed — the five document cases of the
hook module, the sealer's clause, both seal sweeps with the new members, the
gate sweep with `docs/the-broad-gate.md`, and the orchestration's
uncommitted-line pin — and all passed once the documents were written.
`bin/rules --check` resolves every `Enforced by:` target, exit 0.

**One red case belongs to phase 5.**
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
fails on this work item: it holds a `spec.md` and no `overview.md`, which
the frame's commit made true and phase 5 writes.
