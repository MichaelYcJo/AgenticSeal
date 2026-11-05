# Closing memo: 1793853197-a-bare-commit-goes-or-states-its-reason

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the touched test modules, every test module that names a changed path, and `tests/test_censuses.py`, in one scoped run (`trail/phases/phase-1.md` *S4*). Phase 2 ran its changed modules, the modules that name them, list tracked files or read `seal/threads`, in one scoped run (`trail/phases/phase-2.md` *The phase boundary*) | answered: the orchestrator's broad run at `71374dc4` against `703ab88c` passed the `Broad gate` row of `seal/config.md`, the whole suite, lint and format check (`trail/gate.md`), and `guarantee.md` sealed on it |
| closed The bare reader's cost on the Windows and macOS CI legs. On this macOS machine the tree case took 2.2 to 2.5 s against 1.4 s at the base, and the one `git cat-file --batch-check` 0.81 s for 6,414 tokens (`trail/phases/phase-2.md` *The cost*) | a measurement no record asks for: it would decide whether the tree case needs a cheaper reader; #1390's run 41981380410 passed every leg, and no record names the case as slow |
| closed Whether each rewrite of a P, G or N line keeps what its reader acts on and drops only provenance. The phase judged each at its line (`trail/phases/phase-1.md`, rows 1 to 85 and the addendum's row 116), and that is a judgment of meaning | answered: the proofer's 4 rounds in `trail/rounds/` read it, and `guarantee.md` sealed |

## Not done

Sentences in the touched docstrings that say how a case was seen red without naming a commit stand, such as "Seen red against the workflow with no `seal` job" in `tests/behaviour/test_a_release_publishes_its_note.py` and "red against a reader without the refusal" in `tests/skills/test_seal_stamp.py`. `frame/design.md` *Scope* puts history that names no commit out, as an open class no method lists whole. Where such a clause stood in a sentence D1 rewrites, it went or stayed with that sentence.
