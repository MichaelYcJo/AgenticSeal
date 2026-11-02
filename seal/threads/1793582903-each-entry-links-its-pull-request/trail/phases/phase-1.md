# Phase 1: 1793582903-each-entry-links-its-pull-request

## What this phase found

### The frame, checked before the build

The frame holds for phase 1. Every coordinate that `frame/design.md` and
`frame/plan.md` give for this phase was opened at `c55c3083b` and stood as
stated. That covers the renderer's docstring at `:24-25`, `section` at
`:277-296` with the marker at `:292`, and the test pins at the lines `## Removes`
lists. It also covers `tests/behaviour/test_no_document_names_the_old_roots.py`
`:15` and `:50`, `skills/implement/SKILL.md:61`, `templates/setup/config.md:145`,
`skills/implement/multi-repository.md:28-30`, and `REPO` in the publish step's
environment (`.github/workflows/publish-release.yml:90`).

### Q3, decided: the reader is `settle.py#adding_commit`, loaded by path

The default held, and it cost no `ruff.toml` row. The renderer loads
`skills/settle/scripts/settle.py` with `importlib.util.spec_from_file_location`
under the name `agentic_settle_for_the_note`. It does not put
`skills/settle/scripts/` on `sys.path`, so nothing named `settle` becomes
importable in the renderer's process. Neither the renderer nor `settle.py` is
loaded by a hook-run script, so `tests/hooks/test_launch.py` does not reach
them. It ran green with 8 passed (executed). The grounds are
`frame/questions.md` Q3 and `plan.md` *Alternatives considered*, "A
settle-side copy of the subject reading".

The reader raises `RuntimeError` with `git`'s message where `git log` fails.
The renderer's `pull_request` turns that into `sys.exit`, as its `run`
already does for every other `git` call. Phase 2 decides what `--apply` does
with the same exception. The design names exit 2 for an unreadable release
list, and it says nothing about a failing `git log`.

### Departures from the frame

1. **The reader's `git log` is not the design's.** `frame/design.md` *Data &
   interfaces* names `--no-renames --diff-filter=A --full-history`. The
   reader runs `--no-follow --root --diff-filter=A --full-history`.
   - `--no-renames` went because it cannot change the answer. The pathspec
     names one path, so the path a rename would pair it with is never in the
     diff. `seal mutate` with the flag removed SURVIVED against
     `test_the_note_is_built_from_the_fragments_the_range_added`, which holds
     exactly the case the flag was said to guard: a settle's commit that
     removes one fragment and adds another of the same text (executed, exit 1).
   - `--no-follow` and `--root` came in because a person's git config changed
     the answer. A probe ran in a scratch repository under the scratchpad
     (executed, then removed). With `log.follow=true`, a one-path `git log`
     followed the second path into the first path's add and named its pull
     request, with or without `--no-renames`. Only `--no-follow` held it.
     With `log.showRoot=false`, an add in the root commit was not listed, and
     `--root` restored it.
   - The grounds: the reader runs under `seal settle --apply` in a person's
     repository in phase 2. `settle.py#history` already holds its own walk
     to its fields whatever `log.showRoot` and `log.showSignature` say. The
     judgment stands on `skills/core/SKILL.md` *The rule a mechanism is kept
     against*, which says a script holds a gate only on a fact it reads
     exactly.
   - `--no-show-signature` was not added. A second probe signed a commit
     with an ssh key and set `log.showSignature=true` (executed, then
     removed). The verification, `No signature`, came on stdout ahead of the
     commit's line. The last line was still `<commit>\0feat: signed (#3)`,
     which the reader parses, so the setting changes nothing it returns. The
     closed row in `gaps.md` holds the measurement.
2. **An entry with no number and no text is not written.** The design does
   not say what `section` does with a fragment whose text is its process
   section alone and whose adding commit names no pull request. Its rows go
   into the table, and it gets no entry, so the note does not end in an empty
   part. `Test_section::test_accepts_process_rows_into_one_table_above_the_fragments`
   pins it with a fourth fragment.
3. **A removal the frame's `## Removes` did not name.** The parameter
   ``"one `###` section marked with `<!-- specs/<work-item-id> -->`"`` of
   `tests/behaviour/test_no_document_names_the_old_roots.py#test_the_new_root_and_the_kept_forms_pass`
   is gone. With the `KEEP` entry removed, that line is an offender, so the
   case can no longer say it passes. The docstring's two kinds of kept
   mention are now one.
4. **Cases beyond the plan's *Verified by* cell.**
   - `tests/skills/test_settle.py::Test_adding_commit` holds two cases. The
     first is `test_accepts_the_oldest_add_under_any_log_config`, with
     parameters `log.follow` and `log.showRoot`. The second is
     `test_refuses_a_number_the_subject_does_not_end_with_and_a_failed_git`.
   - `seal layout --check tests` refuses a `Test_<function>` class that has
     no `test_accepts_` or no `test_refuses_` case. The refusing case pins
     three refusals no other case did: a `(#N)` that is not at the subject's
     end, a path no commit adds, and a ref `git` cannot read.
   - `tests/github/test_publish_release_note.py::Test_module::test_a_git_that_cannot_read_the_adding_commit_stops_the_run`
     pins the renderer's wrapper.
   - S3's case also adds a fragment a second time after a removal. Without
     that, nothing pinned "the oldest adding commit", and the same mutation
     would have survived.

### Seen red

- `Test_main::test_each_entry_links_the_pull_request_that_added_it` (S1, S2
  and S3) ran against the renderer at `c55c3083b`. It failed at its first
  assertion, the link line of `1700000001-linked`, with the note holding
  `<!-- specs/1700000001-linked -->`. Its first run failed earlier, in
  `git log -1 --format=%B v1.2.3`, because the case had not changed into the
  repository. That is not the red the case means, so `monkeypatch.chdir` was
  added and the case was run again before any code changed.
- The rewritten marker pins in `Test_main`, `Test_module` and `Test_section`
  failed against the same renderer, either on the old shape of an entry or on
  `section`'s old signature.
- `Test_adding_commit` ran against the reader before `--no-follow` and
  `--root` were added. `[log.follow]` failed at `adding_commit(..., second)`
  with `1 == 2`, and `[log.showRoot]` failed at `adding_commit(..., first)`
  with `None == 1`.
- The two cases added after the code are shown red under mutation below.

### Mutations (`seal mutate`, each red exits 0)

| Unit | Break | Cases | Verdict, at the line it means |
|---|---|---|---|
| `settle.py#adding_commit`, the oldest add | `listed[-1]` to `listed[0]` | `-k test_each_entry_links` | red: the entry linked `#46`, the restore, where `#42` was asserted |
| the same, the subject's end | `\(#(\d+)\)$` to `\(#(\d+)\)` | `-k test_each_entry_links` | red: `#7` where `#44` was asserted |
| the same, `--full-history` | removed | `-k test_a_fragment_the_settle_removed` | red: `None` where `5` was asserted, on the tag that is a merge |
| the same, `--no-follow` | removed | `-k adding_commit` | red: `[log.follow]` alone, `1 == 2` |
| the same, `--root` | removed | `-k adding_commit` | red: `[log.showRoot]` alone, `None == 1` |
| the same, the subject's end | `\(#(\d+)\)$` to `\(#(\d+)\)` | `-k refuses_a_number` | red: `7` where `None` was asserted |
| the same, `git`'s exit | `if r.returncode != 0:` to `if False:` | `-k refuses_a_number` | red: `DID NOT RAISE RuntimeError` |
| `publish_release_note.py#section`, an empty entry | `if lines:` to `if True:` | `-k test_accepts_process_rows` | red: the section ended in `\n\n` |
| the same, the no-number branch | `if number is None` to `if False` | `-k folded` | red: the fold assertion, where the entry with no number gained a line |
| `publish_release_note.py#pull_request` | `sys.exit(...)` to `return None` | `-k cannot_read_the_adding` | red: `DID NOT RAISE SystemExit` |
| the same reader, `--no-renames` (before it was removed) | removed | `-k test_the_note_is_built_from` | SURVIVED, exit 1, which is departure 1 |

One run measured nothing. Its `-k` expression held spaces, which
`--tests` splits, so pytest exited 4 and `seal mutate` reported `no baseline`
with exit 2. It was run again with `-k folded` (the row above).

### Removed text, proved by the cases already there

- `skills/implement/SKILL.md`, `templates/setup/config.md` and
  `skills/implement/multi-repository.md` dropped the marker first.
  `test_no_document_names_the_old_roots.py::test_every_keep_entry_is_still_in_use`
  then failed with
  ``KEEP entries no scanned file carries any more: ['<!-- specs/<work-item-id> -->']``,
  and it passed once the entry went (executed).
- Census, executed at `04338ff07`:
  `git grep -n -e '<!-- specs/' -e 'specs/{item}' -e "work item's marker" -e 'HTML comment naming'`,
  outside `seal/threads/`, `tests/skills/test_unverified_check.py` and
  `.test_durations`. It finds five lines and no writer of the marker.
  - `docs/branch-and-release.md:78` is policy text, which `## Rule changes`
    rewrites at the settle.
  - `tests/behaviour/test_no_document_names_the_old_roots.py:174` is a case
    the old root path must fail.
  - `tests/github/test_publish_release_note.py:366` asserts the marker is
    absent.
  - `tests/skills/test_chain_check.py:2544` quotes a comment opener in a
    code span.
  - `tests/skills/test_settle.py:614` is a citation fixture. A published
    note still carries the marker, and phase 2 reads it.
- `tests/skills/test_unverified_check.py` is out of scope by
  `frame/design.md` *Scope*. That is a sample of the spellings, not a list
  of every way the marker can be named.

### The phase-boundary run (executed at `04338ff07`)

The set is the 43 modules that `git grep` names as reading a path this phase
changed:
- `templates/setup/config.md`, `skills/implement/multi-repository.md` or
  `skills/implement/SKILL.md`;
- the renderer, `skills/settle/scripts/`, or the old-roots module;
- `tests/hooks/test_launch.py`, `tests/behaviour/test_a_release_publishes_its_note.py`,
  `tests/behaviour/test_docs_line_wrap.py` and
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`.

It ran as one `bin/test` command. The result was 2155 passed, 9 skipped and 1
failed, exit 1.
- The failure is
  `test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`.
  It asks for this work item's `gaps.md`, which this record's commit writes.
  The module is run again after it.
- The skips are `test_broad_gate.py:1126` (the shell is not `cmd.exe`) and
  `test_a_document_that_names_a_script_says_how_to_reach_it.py:242` (no
  shipped document names the script).
- `bin/seal layout --check tests` exited 0, with 148 files read and 0
  refused. `uvx ruff check` and `uvx ruff format --check` exited 0 on the
  five changed Python files.

### For phase 2

- `settle.adding_commit(root, revisions, path)` returns `(commit, int or
  None)`, or `(None, None)` where no commit adds the path. It raises
  `RuntimeError` where `git` fails.
- The settle passes `--released-at` as `revisions`, so the oldest add is
  read over the whole history at that ref.
- The renderer's per-path `git log --full-history --format=%H` in
  `fragments` does not hold `log.follow`. It runs only in the publish
  workflow, where no person's config applies, and this phase left it as it
  was.
