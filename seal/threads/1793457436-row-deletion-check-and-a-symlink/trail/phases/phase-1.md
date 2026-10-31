# Phase 1: 1793457436-row-deletion-check-and-a-symlink

## What this phase found

**The frame held at every coordinate it names.** Read at a92c358b before the first edit: `unique_by_target` stood at lines 1103 to 1118 and kept the first path per real file. The per-file loop stood at line 1589, its base read at line 1604, the presence arm's `here` at line 1641, and `show()` at lines 1440 to 1447 with `encoding="utf-8", errors="replace"`. In `tests/skills/test_unverified_check.py`, the `linked` fixture's link sorted after its target, and `Test_unique_by_target`, `Test_show` and `test_accepts_a_tracked_link_counted_once_and_not_deleted` stood at the lines the plan gives. `seal/follow-up.md` is absent in this tree, so no follow-up row waited on this work.

**One departure from the frame: a kept path with no relative form is named as outside the repository.** `frame/design.md` *Data & interfaces* defines an outside path as one whose `repo_relative` form starts with `..`, and says a path with no relative form is refused before the loop. That refusal reads only the arguments. After Scope item 1, a link's target on another Windows drive reaches the loop as a kept path, and `repo_relative` returns None for it. Handed to `show()`, it asks git for `<base>:None`, gets None back, and the file leaves the report in silence. That is the outcome Scope item 2 exists to prevent. So the loop treats None as outside as well, with the same notice. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script names what it did not read. The `another volume` parameter of `test_accepts_a_link_to_a_file_beyond_the_repository_as_not_compared` pins it by making `os.path.relpath` raise for the target, so every leg runs it.

**The notice reads `not compared: the file lies outside the repository, so no commit of the repository holds it`.** It is listed under `not compared against <base>:` beside the existing notices. The file's open rows are still printed and counted, because `check_file` runs before the base is read. The case pins the text (contract rule 14).

**The `linked` fixture runs every case on it twice**, with the link's directory sorting after its target (`1780000001-other`) and before it (`1779999999-link`). The design's scenario table asks for both orders. The fixture had one reader before this phase, so the parametrisation reaches no other case. The existing case `test_accepts_a_tracked_link_counted_once_and_not_deleted` gained one assertion: nothing is `not compared` and nothing `left the record`. Without it the case passed at a92c358b in the before order, because the link's blob was named `not compared` and the exit stayed 0.

**A case that covered nothing new was dropped before the commit.** A third parameter of the `unique_by_target` case gave the target before the link. It passed at a92c358b, because the old loop kept the first path it was given. It pinned nothing, so it was removed.

**Each new case was seen red first** (executed):

- `Test_unique_by_target::test_accepts_the_real_files_own_path_wherever_the_link_sorts`, both parameters, against a92c358b's `unique_by_target`: it returned the link's path.
- `test_refuses_a_row_deleted_through_a_tracked_link_naming_the_real_file`, against a92c358b: exit 0 for the before order, scanned whole and by the link's directory alone, and for the after order scanned by the link's directory alone. The after order scanned whole passed at a92c358b, as the frame says it does.
- `test_accepts_a_tracked_link_counted_once_and_not_deleted`, the before order, against a92c358b: the output named the link under `not compared`.
- `test_accepts_a_link_to_a_file_beyond_the_repository_as_not_compared`, both parameters: red against a92c358b, where the notice read `(no ## Not verified section)`. Red again with Scope item 1 built and Scope item 2 left out, where the run exited 0 with no `not compared` section at all, as the plan's row says.
- `Test_show::test_refuses_to_raise_on_a_byte_that_is_not_utf8` passed at a92c358b, as the design's grounding says. It was seen red with `show()` reverted to `text=True` under `en_US.UTF-8`: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff`. The revert was undone before the commit.

**Three `seal mutate` runs, each red** (executed, at 7f9339c1, `seal mutate` exit 0 for each):

- `unique_by_target` made to keep the first path per real file again: 6 of 10 selected cases failed.
- The outside test reduced to `at is None`: the `this volume` case failed.
- The outside test made to skip a None form (`at is not None and ...`): the `another volume` case failed.

**The phase-boundary set ran green** (executed): 27 modules, the 25 under `tests/` that name `unverified_check` or `test_unverified_check`, plus `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` and `tests/behaviour/test_one_word_one_meaning.py`, which list or walk `tests/`. One `bin/test` command: exit 0, 2176 passed, 9 skipped. `tests/skills/test_unverified_check.py` alone ran 354 passed and skipped none, so no link case skipped on this macOS machine. The 9 skips are in other modules. `seal layout --pairs` exited 0. `uvx ruff check` and `uvx ruff format --check` passed on the two changed files.

**No other place states the rule that changed.** The search was `git grep` for `first in sort order`, `first path in sort`, `unique_by_target` and `no ## Not verified section` across the tree, and for `symbolic link`, `tracked link` and `symlink` in `docs/` and `skills/verify/`. It found the function's own docstring and callers and the cases this phase wrote. This is a search on wordings, so it is a sample (contract rule 12). The test module's docstring, which describes the `linked` clone, was rewritten in place to say it is built in both orders.
