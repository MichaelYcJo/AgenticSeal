# Closing memo: 1795798115-the-plugin-is-named-for-the-seal

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over phase 1's commits: the full suite, the repository-wide lint and the format check of `seal/config.json`'s `Broad gate` key. The crafter ran the phase-boundary set and linted the files it changed | the orchestrator, at the broad run |
| The broad gate over phase 2's commits. The crafter ran the phase-boundary set and linted and formatted the Python files it changed | the orchestrator, at the broad run |
| Whether the five eval cases under `evals/behaviour/inspector/` reach their graders in a model session. Each case spawns `agentic:inspector`, which no installed release defines, and no paid run was made | the repository owner, at the next run of `evals/scripts/noninferiority.py` over those cases |

## Not done

Phase 1 left two readers that still compute the root's name, though the name is now always `lib/optin.py#HOME`: `skills/implement/scripts/seal.py#display`, called with the shared place, and `skills/settle/scripts/settle.py#threads`, which reads the basename of the root it is given. Both read a path they are handed and fall back to nothing for a second name, so neither stands on the removed fact.

Phase 2 changed the word of the messages that name the final party, and added no case that pins the new word where none pinned the old one. The messages without such a case are in `skills/code-review/scripts/chain_check.py`, such as *the inspector's verdict reads* and *the inspector writes it from*, and in the help lines of `skills/verify/scripts/seal_stamp.py`, `skills/verify/scripts/broad_gate.py` and `skills/implement/scripts/seal.py`. Contract rule 14 asks a change to a message to pin it. The phase did not add one case per message because the change is a rename that the frame proves by search A1 (`frame/design.md` *User scenarios & acceptance*, row *The party's old name is gone*), and the design adds no check (`frame/design.md` *Removes*, its last paragraph). A1 shows the old word gone, and it does not show which word took its place. The two messages that already had a case were shown red with the old word put back, as `trail/phases/phase-2.md` states.

Phase 2's builder did not read its `seal range` file to its last line. The file holds 14112 lines, and the builder's context could not hold them whole. The builder read the sections of every Markdown file outside `evals/` whole, with each hunk's paragraph, and the added lines of every other changed file. It did not read the unchanged lines around each hunk in the Python files, or the eval case files under `evals/behaviour/inspector/`. Those case files are held to the generator's output by `tests/behaviour/test_evals_layout.py::test_the_inspector_cases_are_the_generators_output`, and the generator's added lines were read. The unread part stands in the range file under the crafter's scratch directory, `<scratchpad>/1795798115-the-plugin-is-named-for-the-seal/phase-2/range.txt`, and the command `seal range seal/threads/1795798115-the-plugin-is-named-for-the-seal --from 01472140 --out <file>` writes it again at the commit that closed phase 2.
