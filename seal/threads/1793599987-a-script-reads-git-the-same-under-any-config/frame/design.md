# Design: a script reads git the same under any config (#1283)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source, and every other place links to it" | Which keys reshape git's output, and which subcommands they reshape, is one fact. Today three readers in `skills/settle/scripts/settle.py` each carry their own flags for it, and every other reader carries none. The keys and the subcommands go into one helper, and each `git log` and `git status` a plugin script starts is built by it. |
| The same section, "when fixes chase one mechanism's edge cases, ask what it decides" | #1054, #1139 and #1281 each found one key at one reader on 2026-11-02 and fixed only that reader. The structure that let this happen is one hand-written argv per reader. This work replaces it for every reader of a subcommand a measured key changes, and leaves the calls no key changes as they are (`frame/plan.md` *Alternatives considered*). |
| The same section, "A script holds a gate only on a fact it reads exactly" | A reader whose fields shift under a person's config does not read exactly. `chain_check.py` holds the pull request gate and `seal gate`'s arm 2, so its readers are in scope with the settle's. |
| `docs/what-a-script-gates.md` *Which gate a script holds* | The policy index, `docs/README.md`, says this document answers "what each script reads". The rule goes there through `## Rule changes`, and no pull request edits `docs/` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |
| `skills/implement/SKILL.md` *3. The SDD file set*, the top rung | The change alters observable behaviour: what the settle's dry run lists, the merge order `seal settle` writes in, the fragments the release note holds, and a hint `seal gate` prints. So a frame comes first. |
| contract rule 12 | The issue's call-site list is a sample. This frame lists the whole set by taking the artefact apart. An `ast` walk of every tracked `.py` under `hooks/`, `skills/` and `.github/scripts/` lists each call whose first argument is the literal `git`, or a list or tuple display that opens with it. It finds 60 calls in 23 files (executed, below). Each reader of their output is then judged against each key (*Data & interfaces*). The set of git config keys is a domain this frame cannot close: the keys outside those listed in *Data & interfaces* were not read. |
| #1054, round 3, finding 2 (`seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/trail/rounds/round-3.md`) | Measured `log.showRoot` and `log.showSignature` against `settle.py#history`. The fix was `--root --no-show-signature` at that one call. The round listed the 46 `log.` and `diff.` keys of `git-config(1)` and ran six. This work keeps that measurement. It departs from the per-site flags: the two keys move into the helper, and the flags go (`## Removes`). Grounds: one source, as above. |
| #1139, phase 1, departure 1 (`seal/threads/1793582903-each-entry-links-its-pull-request/trail/phases/phase-1.md`) | `settle.py#adding_commit` gained `--no-follow --root` after a probe. The phase judged `--no-show-signature` unneeded there, because the reader parses only the last line. It also left the renderer's per-path `git log` in `publish_release_note.py#fragments` alone, because that log runs only in the publish workflow where no person's config applies. This work departs on both points. The helper sets every key for every `log` and `status` call, so no judgment at one reader of which key matters there is left to get wrong. And the release note's first `git log` drops a fragment with a non-ASCII path under git's default `core.quotePath`, which CI has as well (executed, below). So a CI-only script is not exempt. |
| #1281, round 1, finding 1 (`seal/threads/1793591507-the-settle-reads-what-earlier-settles-judged/trail/rounds/round-1.md`) | `settle.py#earlier_judgments` gained `-z`, and the fix pass named `settle.py#released` and `rule_changes.py#order` as readers of the same class. This work keeps `-z` as the rule for every reader of paths. |
| `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, the comment above its `ls-files` call | Measured on git 2.50.1 that `core.quotePath=false` alone still quotes a name that holds a newline, and `-z` quotes nothing and splits on the one byte no file name holds. So `-z` is the path rule, and the helper does not set `core.quotePath`. |
| `seal/follow-up.md` | No row there waits on this work. |

What the frame measured. Each probe ran in a scratch repository under
`<scratchpad>/1283-probe/`, with `GIT_CONFIG_GLOBAL=/dev/null` and
`GIT_CONFIG_NOSYSTEM=1`. Each key was set for one command, with `-c` or with
`GIT_CONFIG_COUNT`. The readers ran from a `git clone --no-local` of this
worktree at `5dc1f37e`. git is 2.50.1 (Apple Git-155).

| Measured | Command | Result (executed) |
|---|---|---|
| `log.showSignature=true` on an ssh-signed commit | `git -c log.showSignature=true log --format=%H` | `No signature` printed as a line of its own, before the signed commit's hash |
| the same, under `-z` | `git -c log.showSignature=true log -z --format=%H%x1f%s` | the text opens the signed commit's entry after the earlier NUL |
| the same, other commands | `show <rev>:<path>`, `rev-list HEAD`, `diff-tree -r -z`, `tag --contains` | unchanged |
| `chain_check.py#routing_trailers` under it | the reader called with `GIT_CONFIG_COUNT` setting the key | the commit read as `'No signature\n7f4e2ff5…'`, which the trailer messages cut to its first 8 characters |
| `-c` against the other sources | `-c log.showSignature=false` with the key `true` in `GIT_CONFIG_COUNT`, then in the repository's own `.git/config` | `-c` wins over both |
| `log.showRoot=false` | `git log --name-only --format=%x00%H` | the root commit's paths are not printed; `-c log.showRoot=true` restores them |
| `rule_changes.py#order` under it | the reader over a design the root commit adds | `('100-ascii', None)`, where without the key it named the root commit |
| `log.follow=true`, one path | `git log --format=%s -- d.txt` after a rename | followed into the old name's commit; `-c log.follow=false` restores; with two pathspecs, or one directory, nothing changed |
| `core.quotePath` default, non-ASCII path | `ls-tree -r --name-only`, `log --name-only`, `diff-tree --name-only` without `-z` | `"seal/threads/2-\354\240\225\353\240\254/frame/design.md"`; with `-z`, the path as it is |
| `settle.py#released`, `unverified_check.py#overviews_at`, `rule_changes.py#order`, `publish_release_note.py#fragments` over an id `200-정렬` | each reader with no key set | the id is missing from each answer; `order` gives it `None`, and `fragments` returns only the ASCII fragment |
| `i18n.logOutputEncoding=iso-8859-1` | `git log -1 --format=%s` over the subject `é (#4)` | `\351 ( # 4 )`, which a UTF-8 decode replaces; `-c i18n.logOutputEncoding=UTF-8` restores `é` |
| `status.showUntrackedFiles=no` | `git status --porcelain -- u.txt` over an untracked file | prints nothing; `-c status.showUntrackedFiles=normal` restores `?? u.txt` |
| keys that changed nothing read here | `format.pretty` under `--format`, `log.diffMerges` set to each of its five values on a plain `log --name-only` over a merge, `diff.relative=true` with `-C` at the top | unchanged |
| `worktree list --porcelain` at a non-ASCII path | `git worktree list --porcelain` | the path printed unquoted |
| every git call in the shipped scripts | `ast` walk, described under contract rule 12 above | 60 calls in 23 files, and no call that only names `git` in a comparison, such as `hooks/lib/cmdline.py`, or in a table, such as `skills/verify/scripts/session_cost.py` |

## Scope

In:

1. A helper, `hooks/lib/gitcmd.py`, whose `argv(*args)` returns the argv of
   one git command. The argv opens with `git` and one `-c` for each key
   measured to change what a script reads. Its docstring names each key,
   what it changes, and the subcommands it changes, `log` and `status`. It
   is the one place either list is written.
2. Every `git log` and `git status` a script under `hooks/`, `skills/` or
   `.github/scripts/` starts is built by `gitcmd.argv`. Where a module's
   wrapper serves such a call, the wrapper builds its argv with `gitcmd.argv`,
   and so do that wrapper's other calls. The calls, by the table under
   *Data & interfaces*, are in `settle.py`, `rule_changes.py`,
   `chain_check.py`, `seal_stamp.py`, `broad_gate.py`, `seal.py`,
   `publish_release_note.py`, `close_issues_on_release.py` and
   `release_completeness_check.py`. No hook runs `log` or `status` (read),
   so no hook changes.
3. Item 2 is the proofer's to read at review, by the rule under
   `## Rule changes`. No case pins it (`frame/plan.md` *Alternatives
   considered*).
4. Every reader that takes paths out of git's output asks for them with
   `-z` and splits on NUL: `settle.py#released`, `rule_changes.py#order`,
   `unverified_check.py#overviews_at` and `#tree_at`, the `ls-tree` listing
   in `test_layout.py#_moved_main`, and the first `git log` in
   `publish_release_note.py#fragments`.
5. The flags and sentences that held single keys at single readers go, as
   `## Removes` lists.
6. The rule goes into `docs/what-a-script-gates.md` through
   `## Rule changes`.

Out:

- A git call whose subcommand no measured key changes: `rev-parse`,
  `merge-base`, `cat-file`, `symbolic-ref`, `check-ref-format`,
  `check-ignore`, `ls-remote`, `for-each-ref`, `tag`, `rev-list`,
  `diff-tree`, `diff`, `ls-files`, `ls-tree`, `show <rev>:<path>`,
  `worktree`, `config` and the write commands. They stay as written. That
  covers every call under `hooks/`, and those in `release_seal.py`,
  `tag_release.py`, `plugin_directory_check.py`, `pact_check.py`,
  `test_layout.py` and `unverified_check.py`, except the `-z` of item 4. A
  key found later to change one of them adds that subcommand to the helper's
  docstring, and its calls move then.
- The suite's own git calls under `tests/` and `evals/`. They are not the
  plugin's scripts, no failure under a developer's config is on record, and
  `tests/conftest.py` already sets git config for the suite through
  `GIT_CONFIG_COUNT`, where a later work item can add keys.
- A reader that prints a line of git's output without taking a path out of
  it: `seal.py`'s `status --porcelain` and `ls-files --stage` lines. Git's
  quoting there is a display convention, and changing it changes a message
  for no catch.
- An existence check that reads only whether git printed anything:
  `ls-tree` in `settle.py#notes`, `chain_check.py` at its root check and
  `publish_release_note.py`'s two per-path checks. Quoting does not change
  whether the output is empty.
- A worktree path that holds a newline, which breaks
  `worktree list --porcelain` without `-z`. No flow of the plugin makes
  such a path, and it is a limit.
- `seal/follow-up.md` has no row this work is the prerequisite of.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A signed commit and a person who shows signatures | Given `log.showSignature=true` and an ssh-signed commit, when any plugin script reads `git log`, then each field reads as it does without the key | `tests/hooks/test_gitcmd.py`: the helper's argv under the key, in `GIT_CONFIG_COUNT` and in the repository's own config, prints what it prints without it; seen red with the key's `-c` removed |
| A root commit under `log.showRoot=false` | Given a design or a document the root commit adds, when the settle orders designs or dates documents, then the root commit is named | the same module, one parameter per key |
| One path under `log.follow=true` | Given a path renamed from another, when a reader logs that one path, then no commit of the older name is listed | the same module |
| A subject in another output encoding | Given `i18n.logOutputEncoding=iso-8859-1`, when a reader prints a subject, then non-ASCII text reads as it was committed | the same module |
| An untracked gate record under `status.showUntrackedFiles=no` | Given `trail/gate.md` written and not yet tracked, when `seal gate` ends, then it prints the hint to commit it | the same module, for the status argv |
| A work item whose id is not ASCII | Given a work item `seal/threads/<n>-정렬/`, when the settle lists released items, orders designs, or `seal unverified` lists closing memos at a ref, then the item is in each answer, and `tree_at` returns its paths as they are | cases for `released` and for `rules.order` in `tests/skills/test_settle.py`, where the cases of both stand, and in `tests/skills/test_unverified_check.py#Test_overviews_at` and `#Test_tree_at`; each seen red against `5dc1f37e` |
| A changelog fragment whose id is not ASCII | Given a release range that adds `seal/threads/<n>-정렬/changelog.md`, when the release note is built, then that fragment is in it | a case in `tests/github/test_publish_release_note.py`, seen red against `5dc1f37e` |
| A test module whose name is not ASCII | Given a test file under `tests/` with a non-ASCII name at the base, when `seal layout --moved` lists the base's tests, then the file is listed | a case in `tests/skills/test_test_layout.py`, seen red against `5dc1f37e` |

## Data & interfaces

`hooks/lib/gitcmd.py`, stdlib only, loaded the way each caller already loads
`hooks/lib/` (a hook through `sys.path`, a skill script by
`importlib.util.spec_from_file_location`, and `.github/scripts/` through the
`sys.path` entry `publish_release_note.py` already makes):

```python
def argv(*args):
    """["git", "-c", "<key>=<value>", ..., *args]"""
```

The keys it sets, each from the measurements under `## Grounding`:

| Key | Value | What the key changes when a person sets it otherwise |
|---|---|---|
| `log.showSignature` | `false` | signature text before a commit's fields in `log` and in `show` of a commit |
| `log.showRoot` | `true` | the root commit's paths in `log` |
| `log.follow` | `false` | a one-path `log` follows a rename into another path's commits |
| `i18n.logOutputEncoding` | `UTF-8` | `log` re-encodes subjects and bodies into another encoding |
| `status.showUntrackedFiles` | `normal` | `status --porcelain` leaves untracked paths out |

`core.quotePath` is not set: a reader of paths passes `-z` (Scope item 4).
`-c` outranks every configuration file and `GIT_CONFIG_COUNT` (executed),
and a git that does not know a key ignores it.

Each reader against each key. The readers a key changes:

| Reader | Key | Reading under the key | Change |
|---|---|---|---|
| `settle.py#adding_commit` | `log.follow`, `log.showRoot` | another pull request's number; no number (executed by #1139) | `argv`; its `--no-follow` and `--root` go |
| `settle.py#earlier_judgments` | `log.showSignature`; `i18n.logOutputEncoding` | a removed plan unread (executed by #1281); the printed subject garbled (executed here, at git's level) | `argv`; its `--no-show-signature` goes |
| `settle.py#history` | `log.showRoot`, `log.showSignature` | a document dated wrong (executed by #1054) | `argv`; its `--root` and `--no-show-signature` go |
| `settle.py#released` | `core.quotePath` | a non-ASCII id never released (executed) | `-z` |
| `rule_changes.py#order` | `log.showRoot`; `core.quotePath` | the design falls to the end of the merge order (both executed) | `argv`, `-z` |
| `chain_check.py#routing_trailers` | `log.showSignature` | the commit's hash read with the signature text in front (executed) | `argv` |
| `chain_check.py#carried_by` | `log.showSignature`; `log.follow`; `i18n.logOutputEncoding` | the same field shape as `routing_trailers`, so the notice names a wrong hash; a commit of the old name judged; the subject garbled (read) | `argv` |
| `unverified_check.py#overviews_at` | `core.quotePath` | a non-ASCII item's `gaps.md` never read (executed) | `-z` |
| `unverified_check.py#tree_at` | `core.quotePath` | returns quoted paths, which `Test_tree_at` compares; its one caller in the module reads only whether any came back (read) | `-z` |
| `test_layout.py#_moved_main`, its `ls-tree` | `core.quotePath` | a non-ASCII test file at the base not listed (read) | `-z` |
| `publish_release_note.py#fragments`, the first `log` | `core.quotePath`, under git's default | a non-ASCII fragment left out of the note (executed) | `-z` |
| `publish_release_note.py#fragments`, the per-path `log` | `log.showSignature` | the signature's words read as commits, and `ls-tree` at one fails and stops the run (read) | `argv` |
| `broad_gate.py#uncommitted_line` | `status.showUntrackedFiles` | an untracked `trail/gate.md` gets no hint to commit it (executed, at git's level) | `argv` |

Readers of `log` or `status` whose output a key changes and whose reading
it does not. Each moves to `argv` by Scope item 2, because the criterion is
the command's output, and with no other change. `chain_check.py#carried_by`'s
dirty check and `seal.py`'s `status --porcelain` lose untracked lines under
`status.showUntrackedFiles=no`, and neither reads an untracked line as a
change (read). `seal_stamp.py`'s history loop reads `log --format=%H` and splits on
whitespace: under `log.showSignature` the extra words are tried as commits,
`show` fails for each, and they are skipped (read).
`publish_release_note.py`'s `log -1 --format=%B`, `close_issues_on_release.py`'s
subjects and `release_completeness_check.py#subjects_since` gain lines under
`log.showSignature` that hold no `(#N)` at their end and no `release:` line
(read). The calls of the subcommands under *Scope*, Out, are not changed
by any measured key: those the probe ran are executed (`show <rev>:<path>`,
`rev-list`, `diff-tree -z`, `tag --contains`, `worktree list --porcelain`),
and the rest are read.

## Rule changes

- add
  file: docs/what-a-script-gates.md
  section: Which gate a script holds
  to: **A script reads git the same under any configuration: each git
    command a script under `hooks/`, `skills/` or `.github/scripts/` starts
    whose subcommand `hooks/lib/gitcmd.py` names is built by its `argv`, and
    a script that takes a path out of output git quotes under
    `core.quotePath` asks for it with `-z`.** A person's or a repository's
    git configuration can put text into the fields a script parses, take a
    commit's paths out, or follow a path into another one's history. `argv`
    sets each key measured to do that with `-c`, which outranks every
    configuration file. Its docstring names each key, what it changes and
    the subcommands it changes, and a key or subcommand found later is added
    there and nowhere else. Git quotes the paths its listings print, such as
    those of `ls-tree`, `ls-files` and `status --porcelain` and the
    `--name-only`, `--name-status` and `--raw` output of `log`, `diff` and
    `diff-tree`. `-z` ends each such path with a NUL and quotes none,
    whatever `core.quotePath` says. A reader that only asks whether git
    printed anything, prints git's line as it came, or compares the line
    with an ASCII path the script names takes no path out. `rev-parse` and
    `worktree list --porcelain` print a path unquoted, and a path that holds
    a newline breaks the second, a limit no flow of the plugin reaches. A
    key nobody has measured is a limit until a run shows it changes a
    reading. Whether a call is one of these is read at review, and
    `tests/hooks/test_gitcmd.py` holds each key.
    check: none reader: the proofer at a change that adds or edits a git call in a script

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the flags `--no-follow` and `--root` | `skills/settle/scripts/settle.py#adding_commit` | `hooks/lib/gitcmd.py#argv` sets `log.follow=false` and `log.showRoot=true` for every call |
| the flags `--root` and `--no-show-signature` | `skills/settle/scripts/settle.py#history` | the same helper |
| the flag `--no-show-signature` | `skills/settle/scripts/settle.py#earlier_judgments` | the same helper |
| the docstring sentences that say which key each flag holds | `skills/settle/scripts/settle.py#adding_commit` ("`--no-follow` and `--root` hold that whatever the person's `log.follow` and `log.showRoot` say" and the clause after it), `skills/settle/scripts/settle.py#history` ("`--root` and `--no-show-signature` hold the walk to these fields" and the clause after it), and the module docstring line "The person's `log.showRoot` and `log.showSignature` change nothing it reads." | the helper's docstring names each key; the rule is in `docs/what-a-script-gates.md` *Which gate a script holds* |
| the sentence "The person's `log.showRoot` and `log.showSignature` change none of these dates." | `skills/settle/SKILL.md` *What the dry run shows* | the same rule holds for every script, so a copy for one listing goes |
| the per-reader key cases | `tests/skills/test_settle.py#Test_main::test_a_signed_removal_is_read_under_any_show_signature`, `#Test_main::test_a_document_the_root_commit_added_is_dated_under_any_show_root`, `#Test_main::test_a_signed_commit_is_read_under_any_show_signature`, and the `key, value` parametrization of `#Test_adding_commit::test_accepts_the_oldest_add_under_any_log_config` | `tests/hooks/test_gitcmd.py` holds each key once over the helper's argv, and the three readers build their `log` with it, which the proofer reads in the diff. `Test_adding_commit` keeps an accepts case, which `seal layout --check` requires, as the oldest-add case with no key set |

The helper and the rule are mechanisms this work adds. What they take out
in return is the rows above: five flags at three readers, four sentences,
three cases and one parametrization, each of which held one key at one
reader. The catch record they stand on is #1054 round 3 finding
2, #1139 phase 1 departure 1 and #1281 round 1 finding 1, three findings of
one class at three readers in one day, and the readers under *Data &
interfaces* that no one had measured.

Framed 2026-11-02 by framer, before the build.
