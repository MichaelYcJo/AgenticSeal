# Phase 2: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

## What this phase found

**The fragment states what phase 1 built, with its facts taken from `trail/phases/phase-1.md`.** The replay's counts, the notices' texts and the reading of a rule document that does not decode are that record's. The fragment opens with `### Added`, since the work adds a notice and changes no behaviour a user had, and the release note groups its summary by the pull request's title and folds each fragment as written (`.github/scripts/publish_release_note.py#release_body`, read).

**The process row is the fragment's own, as `docs/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* asks** of a diff that changes an `agents/*.md` file. Its shape is `templates/records/process.md`'s, and its source is the issue, since the build's commits are squashed at the merge (read against `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/changelog.md`, the sibling that also changed `agents/proofer.md`).

**`gaps.md` gains no row.** This phase left nothing unverified that phase 1's rows do not already name, and took nothing out of reach.

**The narrow run (executed).** At `820bf7b23`, one `bin/test -q` over `tests/behaviour/test_release_hygiene.py`, the five modules `git grep -l -e "changelog.md" -e "Process changes" -- 'tests/*.py'` lists that hold cases, `tests/behaviour/test_chain_hooks_hardening.py` and `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py` exited 0, 189 passed.
