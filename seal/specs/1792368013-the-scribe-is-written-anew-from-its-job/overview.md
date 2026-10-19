# 1792368013-the-scribe-is-written-anew-from-its-job — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

The scribe preloads the contract alone and opens `legacy-parity` at its first
step, and `legacy-parity` writes its verdicts as four words and names who
writes the parity mark, so no agent reading it takes itself for that writer.

## Where spec and implementation diverged

Opened at phase 1, where `tests/test_chain_hooks_hardening.py` asked for this
file once the frame was in the tree.

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Line coordinates moved after the frame (phase 1) | the frame was drawn at d7691951, before #976 and #943 merged; `## Removes` and S7 name `skills/implement/orchestration.md:240` and `:54`, `README.md:234`, `:421` and `README.ko.md:226`, `:379` | the same sentences at `orchestration.md:238` and `:52`, `README.md:240`, `:427` and `README.ko.md:231`, `:384`, found by the greps the frame names | the spawn prompt said the orchestration file moved under #943; each sentence was found by its words, not its number (`phases/phase-1.md`) |
| Eight README sentences, where the frame names four (phase 2) | `## Removes` names *The smith asks* at `README.md:234`, `:421` and `README.ko.md:226`, `:379`; those four are not two pairs of twins, and each README states the bootstrap as the smith's act three times, plus once more as *the smith creates from `templates/`* | all eight now name the user's session: `README.md:240`, `:393`, `:420`, `:427` and `README.ko.md:231`, `:384`, `:413`, `:421` | contract §12, the class and not the coordinate; `skills/implement/orchestration.md` §*Orchestrator: Bootstrap — create what's missing* gives both the question and the creation to the orchestrating session |
| `tests/test_chain_hooks_hardening.py#test_the_readme_group_counts_are_derived_too` gains two spellings (phase 2) | the frame does not name the case; the README's group counts became three and thirteen, and the case held no spelling for either | `3: ("three", "세")` and `13: ("Thirteen", "열세")` added | the case derives each count from the tree and says to add a spelling rather than loosen the check |
| `tests/test_review_axes.py`'s module docstring rewritten (phase 1) | `## Removes` does not name it; it said *`❓ out of verified scope` records that you looked and could not decide* | it now names a row of `## Not judged`, the label `code-review` writes for that today | the docstring quoted a label this item removes from the last file that carried it; contract §19, a change removes what stood on the old fact |

## Not verified

| Item | Who must answer |
|---|---|
| Whether a scribe spawn opens `legacy-parity` at step 1, returns facts and no verdict, and returns `original not found` where the original does not resolve: no case runs the scribe (#957's Q3) | the repository owner, at the first parity run |
| closed the full suite on this branch | the orchestrator's `broad-gate --base release/v0.22.2 --record <item>` at d9fac6ed, exit 0: 7598 passed, 13 skipped, chain exit 0 (`broad-gate.md`); the run at b9de905c failed on a real user path in `plan.md`, fixed at d9fac6ed |

## Not done

nothing. `skills/implement/scripts/seal.py:678` printed *The first time the
smith works in a repository it asks which one, and creates it.* to a person
who runs a `seal` subcommand where no `seal/` exists, the fact the eight
README sentences above stated. It was left at phase 2 because no case read
it, and was fixed after phase 3 at the orchestrator's request: the line now
names *your session*, and
`tests/test_the_mode_is_a_row_and_a_command.py::test_the_refusal_names_the_session_as_the_one_that_asks`
reads it, seen red against the old line first.

## Fed back into the spec

none
