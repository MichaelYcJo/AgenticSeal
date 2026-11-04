# Closing memo: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the touched modules, every test module that names a changed path, and `tests/text/`, in one scoped run (`trail/phases/phase-1.md`) | the orchestrator, at the broad gate |
| Whether each issue a rewrite cites holds what its sentence sends the reader there for. The phase read each page with `gh` and cited it only where it did (`trail/phases/phase-1.md`, the Q1 answers), and that reading is a judgment of meaning | the proofer, reading each rewrite against its page |

## Not done

Some sentences in the touched files point at a past record by a word, not by a `<commit>:<path>`. A sentence of that kind that leaned on its file's removed citation for its referent was rewritten: in the docstrings of rows 15, 17 and 18 (`frame/design.md` D1, and `trail/phases/phase-1.md` *Departures from the frame*) and the comment above `SESSION_RULE` in `tests/behaviour/test_first_setup_asks_once.py` (round 1, finding 2). Seven stand, all naming #667's frame:

- in `tests/block_shapes.py`, the comment above `RENDERER`;
- in `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py`, the section comments above the oracle cases and above the corpus, the comment naming "The frame's Q7", the case name `test_the_oracle_gives_the_frames_renderer_column` and the docstrings of that case and of the case that opens "The half above is empty".

Each is in a module whose title line names #667, so each still reads as #667's frame. None of them is the issue's `<commit>:<path>` form. The case name also stands because renaming a case is not something `frame/design.md` *Scope* asks for. The list was built by a search for the words that name a record's parts in the touched files, then by reading each hit, so it is a sample: a sentence that points at a removed record in words the search did not hold is not on it.

Bare commits in shipped text stand, as `frame/design.md` *Scope* puts them out. Among them are the two that stand beside a rewritten sentence: `4edc5de6` in `tests/block_shapes.py`'s docstring and `7e44106` in `tests/behaviour/test_first_setup_asks_once.py`'s.
