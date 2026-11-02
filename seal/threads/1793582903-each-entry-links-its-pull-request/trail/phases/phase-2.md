# Phase 2: 1793582903-each-entry-links-its-pull-request

## What this phase found

### The frame, checked before the build

The frame holds for phase 2. Every coordinate that `frame/design.md` and
`frame/plan.md` give for this phase was opened at `71a5b7f62`. Each stood
as stated, shifted only by the 58 lines phase 1 added to `settle.py`.
`#apply` is now at `:1273-1324`, `#merged_pull_requests` at `:322-359`, and
the `Unasked` handler in `main` at `:1419-1423`. "Shared mode never asks
`gh`." stood at `skills/settle/SKILL.md:483`, and the not-on-PATH case at
`tests/skills/test_settle.py:1592`.

### Decisions

1. **A `git` that cannot read what a note is checked by stops `--apply`
   with exit 2, and nothing is removed.** Phase 1 left this to phase 2.
   `adding_commit`, `version` and the `ls-tree` of the fragment each raise
   `RuntimeError` where `git` fails. `notes` turns that into `Unread`, and
   `main` prints `NOTE_UNREAD` and returns 2. The grounds are the design's
   rule that an unreadable release list exits 2 and removes nothing
   (`frame/design.md` *Scope* item 4). An unknown adding commit leaves the
   pull request unknown, and removing on an unknown is the quiet path that
   rule refuses. `skills/core/SKILL.md` *The rule a mechanism is kept
   against* says a script holds a gate only on a fact it reads exactly.
   `Test_main::test_a_git_that_cannot_read_the_adding_commit_stops_apply`
   pins it.
2. **Every directory is classified before the first removal.** `apply`
   reads every record's open rows and every note first, then removes. The
   frame asks that the list be read "before the first removal". A note read
   when a directory's turn came would have removed the directories sorting
   before a failing one. S6's no-note directory sorts first, so the case
   sees that order (the mutation below).
3. **The checks run in the order fragment, number, tag, and stop at the
   first that fails.** The design lists the three reasons in that order.
   An adding commit that names no pull request leads to no tag lookup and
   asks no `gh`, even where a version tag holds the commit. S7's case
   holds such a commit under `v1.0.0`.
4. **Where the fragment can be read is `git show <commit>:<path>`, the
   commit being the one `--released-at` resolves to.** The note check runs
   only where `--released-at` holds the `changelog.md`, so that commit
   holds it by construction, and its hash outlives the ref moving. The
   adding commit would name the text as first added, which a later commit
   of the range may have edited.
5. **The release list is parsed page by page.** `gh api --paginate` prints
   one JSON array per page, back to back. `published_releases` reads them
   with `json.JSONDecoder.raw_decode`, and refuses empty output and any
   page that is not a list of objects. A probe read this repository's
   releases through it, as one page of 100 and as three of 30 (below).
6. **The closing line always names both counts**, as `removed N
   directories; kept K with a row to close and M whose note lacks its
   entry`. A suffix printed only when M is not zero would give one line two
   shapes. The design asks for the two counts apart (*Data & interfaces*,
   *Output*). Three existing pins in `Test_apply` changed with it.
7. **A directory with no note to read prints its reason first under its
   `removed` line**, before any `not read:` line and the closed rows. Every
   such directory in shared mode gets one, so a repository whose work
   items write no `changelog.md` sees `no note read: <ref> holds no
   `changelog.md` in its directory` under each removal. Two `Test_apply`
   pins gained that line.

### Departures from the frame

1. **The refusal for the release list is a sentence of its own,
   `RELEASES_UNASKED`.** The design names "the existing `UNASKED` sentence"
   (*Data & interfaces*, *The release list*). That sentence says `gh`
   cannot be asked "which pull requests merged", says "Nothing was read",
   and explains local mode. None of that is true of the release list. A
   person reads the line and acts on it (contract rule 14), so it has to
   say what was asked. The new sentence names the releases, says nothing
   was removed, and says why a repository with version tags needs `gh`.
   The mutation that swaps the two sentences is red.
2. **The dry run's heading of what `--apply` removes changed.**
   `settle.py#REMOVES_HEADING` said `--apply` removes "each released
   directory whose record holds no open row", which this phase makes
   false where the root is shared. Scope item 5 does not list it. It now
   adds "unless its version's published note, which `--apply` alone reads,
   lacks its entry". `Test_module::test_the_dry_runs_headings_say_who_decides`
   pins the new text. The local heading is unchanged, because local mode
   reads no note.
3. **`seal/README.md` changed with `templates/setup/seal-README.md`.**
   `tests/behaviour/test_first_setup_asks_once.py:594` holds the two byte
   for byte, so the template's sentence could not change alone.
4. **The renderer's `TAG_RE` is now `settle.py#VERSION_RE`.** The design
   says the version is read "as `publish_release_note.py#previous_tag`
   reads tags". The settle cannot load the renderer, which is not shipped,
   and the renderer already loads `settle.py`. So the one pattern lives in
   `settle.py` and the renderer takes it. That way the note is published at
   the tag whose note the settle reads (`skills/core/SKILL.md`, a fact has
   one source). The renderer's module ran green with it.
5. **`settle.py#ask_gh` was taken out of `merged_pull_requests`.** The
   release list asks `gh` the same way: PATH lookup, timeout, the
   non-zero exit and its first line. One helper runs both. The local-mode
   refusal cases (`absent`, `fails`, `garbled`, `entry`) ran green over it.
6. **`test_shared_mode_never_asks_gh` became
   `test_shared_mode_asks_gh_for_no_note_it_cannot_read`.** Its name and
   docstring stated the rule this work removes. Its fixture asks no `gh`
   for either command, so it became S7: the dry run with a `routing.md`
   naming a branch, and `--apply` over the three no-note cases. It reads
   the stub's call log instead of a `GH` not on PATH, as the design's S7
   puts it. An empty log shows `gh` never ran, and a missing `gh` would
   show only that a run without it exits 0.
7. **Two sentences outside Scope item 5's list were amended.** They are
   `skills/settle/SKILL.md` *A released work item with no
   `frame/design.md`*, which restated the removal condition, and the
   module docstring of `tests/skills/test_settle.py`.
8. **The SKILL describes the old marker in words.** The first wording
   spelt `<!-- specs/<id> -->`.
   `test_no_document_names_the_old_roots.py::test_no_shipped_document_names_the_old_roots`
   refused it at `skills/settle/SKILL.md:458`, as the design's `## Removes`
   row for that module foresaw. The code spells the marker because it
   matches it. The check reads documents, and passed after the rewording.
9. **A version-shaped number left a docstring.** `version`'s docstring
   named a second tag to show the order by number.
   `test_release_hygiene.py::test_no_loaded_file_names_a_version_at_or_above_the_running_one`
   refused it at `settle.py:430`. The docstring now says the three parts
   are compared as numbers.

### Seen red

- Against the tree at `71a5b7f62`, before any code:
  - S4 (`test_apply_keeps_a_directory_its_published_note_does_not_carry`)
    failed at `assert code == 1` with `0 == 1`. Both directories were
    removed.
  - S6 (`test_apply_stops_where_the_release_list_cannot_be_read`, all three
    states) failed at `assert code == 2` with `0 == 2`.
  - S7b's kept case (`test_apply_keeps_a_directory_whose_tag_has_no_published_release`,
    both states) failed at `assert code == 1` with `0 == 1`.
  - The git case (`test_a_git_that_cannot_read_the_adding_commit_stops_apply`)
    failed at `assert code == 2` with `0 == 2`.
  - S7 failed at its first `removed` assertion, on the missing `no note
    read:` line. S7b's removal half failed on the same missing line.
  - S5 and S8 failed only on the closing line. Their own reds are the
    mutations below.
- S7's `gh`-not-asked half cannot be red against a tree that never asks
  `gh`. It is red under the mutation that asks for the list with no
  version tag.

### Mutations (`seal mutate`, each red exits 0)

| Unit | Break | Cases (`-k`) | Verdict, at the line it means |
|---|---|---|---|
| `apply`, open rows first | `[i for i in ids if not held[i]]` to `ids` | `before_its_note` | red: S8's `gh.calls() == []`, one `api` call |
| `notes`, no list without a tag | `if not pending:` to `if False:` | `shared_mode_asks` | red: S7's `gh.calls() == []`, one `api` call |
| `notes`, a note that lacks the entry keeps | `elif not any(carries(...))` to `elif False` | `does_not_carry` | red: S4, both directories removed |
| `carries`, no digit after N | `(?!\d)` removed | `does_not_carry` | red: S4, `pull/420` read as #42 |
| `carries`, the old marker | the marker clause removed | `note_carries` | red: S5[marker], kept |
| `version`, by number | the key `(tuple, name)` to `(name, name)` | `does_not_carry` | red: S4, `v1.10.0`'s note read, `1700000001-a` removed |
| `published_releases`, drafts left out | the `draft is False` test removed | `no_published_release` | red: S7b[a draft], `0 == 1` |
| `notes`, no published release at all | `if not published:` to `if False:` | `publishes_no_release` | red: kept, `1 == 0` |
| `notes`, a tag with no release keeps | `(True, NO_RELEASE...)` to `(False, ...)` | `no_published_release` | red: removed, `0 == 1` |
| `published_releases`, each page a list of objects | the `dict` test removed | `release_list_cannot` | red by exception: S6[entry] raised `AttributeError: 'int' object has no attribute 'get'` |
| `main`, the releases sentence | `RELEASES_UNASKED` to `UNASKED` | `release_list_cannot` | red: S6's `startswith`, the merged-pull-requests sentence printed |
| `notes`, `git` failure to `Unread` | `except RuntimeError` to `except KeyError` | `cannot_read_the_adding_commit_stops_apply` | red by exception: the `RuntimeError` reached the case uncaught |
| `apply`, local mode reads no note | `if not found["local"]:` to `if True:` | `local_mode` | red: `test_apply_in_local_mode_names_a_gaps_md_away_from_its_place`, a `no note read:` line under `removed` |
| `apply`, exit 1 for a note | `1 if kept or kept_for_note` to `1 if kept` | `does_not_carry` | red: S4, exit 0 |
| `apply`, every note read before the first removal | the eager `notes` call moved into the loop, per directory | `release_list_cannot` | red: S6's `bare.exists()`, `1700000000-bare` removed before `gh` failed |

Two runs are red by an uncaught exception, not by an assertion. A person
would see that traceback with the guard gone, so the case still holds
the guard. The last row first ran as two `--replace` flags, and `seal
mutate` read them as two mutants. The second SURVIVED, exit 1, because
the eager call it left in place still raised first. It was run again as
one contiguous replace, the row above.

### The probe (executed, read-only, nothing left)

`python3 -c` loaded `settle.py` from the worktree and called
`published_releases('.')` against this repository's releases. It read 68
published releases with `per_page=100`, one page, and again with
`per_page=30`, three pages back to back. The two maps were equal.
`v0.27.3` was among them, and its body holds the old marker, which the
first settle under this change reads (`plan.md` *Operational impact*).

### Places that stated the old removal condition

Method: `git grep` on the old fact's words outside `seal/threads/` and
`.test_durations`. The words were `holds no open row`, `never asks gh`
with and without backticks, `each with a row to close`, and the two
phrasings `--apply` takes before `removes`.
That is a sample of the spellings, not a list of every way the rule can
be put (contract rule 12).
- Amended: the README rows, both editions of the `seal/` README, the
  SKILL's usage block, *What `--apply` does*, *In local mode* and *A
  released work item with no `frame/design.md`*, the procedure's step 11,
  `settle.py`'s module docstring, `--apply` help, `apply` docstring and
  `REMOVES_HEADING`, and `tests/skills/test_settle.py`'s module docstring.
- Stand as they are:
  - `docs/the-record-layout.md:108` and `docs/release-checklist.md:48` are
    policy text, which `## Rule changes` rewrites at the settle.
  - `docs/the-record-layout.md:236`, `skills/settle/SKILL.md:542`,
    `settle.py#REMOVES_HEADING_LOCAL`, and the local cases at
    `tests/skills/test_settle.py:1553` and
    `tests/text/test_settle_reads_before_it_removes.py:225` state local
    mode, which this work leaves unchanged.
- `.test_durations` still names `test_shared_mode_never_asks_gh`. It is
  a timing file, and a renamed case only loses its recorded time.

### The phase-boundary run (executed at `54b7183b6`)

The set is 72 modules, run as one `bin/test` command. It holds every test
module that `git grep` finds naming `skills/settle`, `settle.py`,
`seal-README`, `README.md`, `README.ko.md`, `publish_release_note` or the
`seal` README by its parts. It also holds every module that names
`"skills"` and walks or globs, plus `tests/hooks/test_launch.py`.
- The first run, at `cae15ac23`, ended 4447 passed, 11 skipped and 2
  failed, exit 1. The two failures are departures 8 and 9.
- At `54b7183b6` it ended 4449 passed and 11 skipped, exit 0.
- After it, `ad5bb8116` and `0044d5015` changed only
  `tests/skills/test_settle.py`. That module ran again at `0044d5015`,
  exit 0.
- `tests/hooks/test_launch.py` was in the set. `settle.py` is still not
  loaded by a hook-run script.

Also executed, each with its exit code read:
- `bin/seal layout --check tests` exited 0, with 148 files read and 0
  refused.
- `bin/seal layout --pairs` exited 0 and named no pair in
  `tests/skills/test_settle.py`.
- `bin/seal rules --check` exited 0: "all 283 check lines in 55 rule
  files hold". This phase wrote no check line.
- `uvx ruff check` and `uvx ruff format --check` exited 0 on
  `settle.py`, `.github/scripts/publish_release_note.py`,
  `tests/skills/test_settle.py` and
  `tests/text/test_settle_reads_before_it_removes.py`.
