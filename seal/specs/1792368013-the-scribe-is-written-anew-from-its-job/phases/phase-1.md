# 1792368013-the-scribe-is-written-anew-from-its-job — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c6738f51 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Rewrite `skills/legacy-parity/SKILL.md` to #957's shape, with its four
verdict words (`differs`, `grounded`, `equivalent`, `unread`), the writers of
the parity mark named, the migration config pointing at `templates/parity.md`
for its fields, and an `Enforced by:` line on each rule. Change the five B5
places that propose `docs/policies/` as the policy root. Plant T4 and T5,
remove the emoji case's `SKIP`, and add the skill to
`tests/test_docs_line_wrap.py#COVERED`. The frame was drawn at d7691951,
before #976 and #943 merged, so every line coordinate is found again.

## What this phase found

**The frame holds, with its line numbers moved.** Every sentence it names is
in the tree with the words it quotes. The B5 line of
`skills/implement/orchestration.md` is now `:238` (the frame says `:240`),
and S7's one surviving hit is `:52` (the frame says `:54`), moved by the
merges after the frame; the spawn prompt names #943 for this file. The README sentences phase 2 changes are now `README.md:240`, `:427`
and `README.ko.md:231`, `:384`. `overview.md` records the moves.

**The skill's sections, and which of them the scribe reads.** The opening
paragraph names three sections the scribe reads: *The migration config*, *What
the original sends* and *The original's coordinates*. *What the original
sends* was the `###` under the three-way judgment and is now a `##` section
of its own, so the scribe's step 1 can name it without sending the scribe
into the judging section above it. The resolution order ends with the caller
asking and recording, and a reader that cannot ask returns `original not
found`.

**`Enforced by:` per rule.** Three rules have a case: the migration config
(`tests/test_chain_hooks_hardening.py::test_parity_declaration_is_bootstrappable_not_hand_written`,
which reads the template's fields and `parity-paths.md`), the parity review
(T4 and the existing `test_legacy_parity_still_points_at_that_table`) and the
record (T5). The other five read `nothing — <why>`: the premise and the
three-way judgment are judgments the parity review reads, the trace and the
coordinates have no case because no case declares `seal/parity.md`, and the
replacement annotation is read by a reviewer.

**T5 stays in `tests/test_review_axes.py` (Q4).** The group rule found no
closer module: `tests/test_chain_hooks_hardening.py`,
`tests/test_the_commit_gate_decides_at_the_commit.py` and
`tests/test_the_records_can_be_carried_out_and_in.py` read the mark's file as
the gate reads it, and none reads the skill's text. `test_review_axes.py` is
the one module that pins `legacy-parity`'s sentences.

**One docstring outside the frame stood on a removed label.**
`tests/test_review_axes.py`'s module docstring quoted `` `❓ out of verified
scope` `` as the label for an axis looked at and not decided. This phase
removes that label from the last file that carried it, so the docstring now
names a row of `## Not judged`, which `code-review` writes for that today.
`overview.md` records it as a divergence.

**`tests/test_chain_hooks_hardening.py` was red before this phase.**
`test_every_spec_directory_that_reached_the_ladder_has_an_overview` asks for
`overview.md` once `spec.md` and `plan.md` are in a work item, so it failed
from the frame's commit on. This phase opened `overview.md` at its first
divergence, as `skills/implement/SKILL.md` §3 says, and the module is green.

**The byte budget, set here for phase 2.** `skills/legacy-parity/SKILL.md` is
5,688 B at c6738f51 (5,325 at 1d665d48). A draft of the scribe in the shape
phase 2 writes measured 3,319 B, so the two files would read 9,007 B against
the 9,088 B `spec.md` §*How the rewrite is measured* allows. The contract is
16,603 B on both sides.

### The pins on `legacy-parity` (Q3), sorted

| Case | Rule or narration | Re-pointed to, or removed because |
|---|---|---|
| `tests/test_review_axes.py::test_legacy_parity_still_points_at_that_table` | rule | unchanged: the Parity review section keeps *across the same comparison axes* |
| `tests/test_the_record_is_written_in_words.py#SKIP` | — | removed with its comment and the loop reading it (`## Removes`) |
| `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` pair with `implement` | — | unchanged at 1; the module is green, so no pair grew and none appeared |
| `tests/test_chain_hooks_hardening.py::test_parity_declaration_is_bootstrappable_not_hand_written` | rule | unchanged: the template keeps its four field names and `parity-paths.md`, `orchestration.md` keeps `templates/parity.md` |

### The new cases, each seen red

T4 and T5 were run against the tree before the rewrite and failed: T4 read
the labels as the four emoji, and T5 lost *the warden in a review round*. T6
went red once the emoji left with `SKIP` still in place, on its own *carries
no mark any more* assertion, and green once `SKIP` left. After the commit,
`mutation-check` broke each sentence below; every run read `red: the cases
failed against the mutation (exit 1)`, exited 0 and left `git status` clean.

| Case | Mutation | The assertion that went red |
|---|---|---|
| T4 | `grounded` capitalised | the labels are `['differs', 'Grounded', 'equivalent', 'unread']` |
| T4 | a fifth line `unclear` added to the block | the labels are `[…, 'unread', 'unclear']` |
| T4 | the sentence saying the four words are the labels made *Verdicts:* | *no longer says the four words are the only labels* |
| T5 | *the warden in a review round, and* deleted | *lost 'the warden in a review round'* |
| T5 | *The scribe and the smith write none.* deleted | *lost 'The scribe and the smith write none.'* |
| T6 | `U+1F534` put back before `differs` | *skills/legacy-parity/SKILL.md:91* named |

### Commands, each with its exit code

Read with `; echo $?` or from `mutation-check`'s own verdict line, never
through a pipe.

| Command | Exit |
|---|---|
| `bin/test` T4 and T5 (`-k "four_words or names_its_writer"`) before the rewrite | 1: 2 failed |
| `bin/test tests/test_the_record_is_written_in_words.py tests/test_review_axes.py` with `SKIP` still in place | 1: T6 failed, 11 passed |
| `bin/test tests/test_the_record_is_written_in_words.py tests/test_review_axes.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py -q` | 0: 61 passed |
| `bin/test tests/test_chain_hooks_hardening.py -q`, before and after `overview.md` | 1 (1 failed, 55 passed), then 0 (56 passed) |
| `bin/rules --check --root <worktree>` | 0 |
| `uvx ruff check` and `uvx ruff format --check` on the three changed `.py` files | 0, 0 |
| `git grep -n 'docs/policies' -- ':!seal/specs' ':!changelog' ':!tests' ':!.test_durations'` | 0: `skills/implement/orchestration.md:52` alone, the sentence saying not to create it |
| `bin/unverified-check <worktree>` | 0 |
| `mutation-check`, six runs above, `-p no:xdist` | 0 each, `red` each |
