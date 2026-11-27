# Design: scripts read git past submodule settings and a floor (#1640, #1642)

## Grounding

The tree as read at `f7d315f01`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `docs/running/what-a-script-gates.md` *Which gate a script holds*, as the unsettled `## Rule changes` of `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md` leaves it in force: "A setting measured to do it that no `-c` key reaches, such as one a file of the repository carries, is held by a flag on each command it reshapes", and `lib/gitcmd.py`'s docstring names each such setting with its flag (read). The document's own text is still the baseline's, so the first and the last `from` of `## Rule changes` below quote that design's `to` values, and the second quotes the document | The policy already asks for the flag on each command the setting reshapes. #1640's second branch, a reason written where a read stands without the flag, is the weaker reading and is not taken. |
| G2. `lib/gitcmd.py:1-18` and `:247-275`: `git` is the one function that starts git, and it builds each command with `argv`. `git grep -n 'argv(\|subprocess\.\(run\|Popen\|check_output\|check_call\)\|os\.system\|os\.popen' -- lib skills .github/scripts evals/scripts hooks bin` prints `subprocess.run` for git at `lib/gitcmd.py:198` alone, and the other starts it prints run a tests command or an eval (executed) | A flag the runner adds reaches each command a script starts. No script has a second way to start git. |
| G3. What git 2.50.1 prints for a submodule's path, by `sh test_tmp_submodule_probe.sh` in the scratch directory, on a repository with a submodule under no setting, under `diff.ignoreSubmodules=all`, and under a `.gitmodules` entry with `ignore = all` (executed). `diff --raw` of a commit range and of the working tree, `diff HEAD --name-only`, `log --name-only` and `log --name-status` leave the path out under either setting. `diff-tree --name-only -r` leaves it out under the `.gitmodules` entry and prints it under the configuration key. `status --porcelain` leaves out a checkout that moved and a checkout with changed files inside, and prints a staged pointer under every setting. `diff --cached --quiet -- <submodule>` exits 0 over a staged pointer under either setting. `log -- <submodule>` names the same commits under every setting. `--ignore-submodules=none` brings each path and exit code back, on each of the four subcommands | The subcommands the two settings reshape are `diff`, `diff-tree`, `log` and `status`. `lib/gitcmd.py:54-61` names `diff` and `status` and not the other two. |
| G4. The reads the settings reach, listed by `python3 test_tmp_git_literals.py <tree>` in the scratch directory, which walks each `.py` file under `lib`, `skills`, `.github/scripts`, `evals/scripts` and `hooks` by `ast` and prints each call or tuple whose first or second string is a git subcommand (executed; a subcommand held in a variable escapes it, so the list is a sample). `diff`: `skills/code-review/scripts/chain_check.py:400` and `:408`, `skills/implement/scripts/seal.py:1877`, `skills/settle/scripts/settle.py:1595`, `skills/implement/scripts/range_read.py:136`. `diff-tree`: `chain_check.py:977`. `status`: `chain_check.py:463`, `seal.py:1494`, `skills/verify/scripts/broad_gate.py:2157`, `range_read.py:422`. `log` with a path listing: `skills/settle/scripts/settle.py:343`, `:1238` and `:1571`, `skills/settle/scripts/rule_changes.py:685`, `.github/scripts/publish_release_note.py:237` | #1640's list was written from a search. It lacks `chain_check.py#touched`, `settle.py#changed` and the `log` listings. `range_read.py` alone passes the flag. |
| G5. `chain_check.py:974-982` `touched` reads `diff-tree`, and `:1001-1004` `records_only`, `:1007-1033` `follows` and `:1456-1457` decide on its paths (read). `skills/core/SKILL.md` *Judgment is not licence to skip a party* names this check as what holds the rows *No fix that no round reads*, *No seal without the broad run* and *No pull request without a seal* | A commit after the last round that moves only a submodule's pointer is listed as touching no path where `.gitmodules` ignores the submodule, so `follows` lets it stand after the round, the gate and the seal. `.gitmodules` is a file of the repository, so the pull request's workflow reads it as a person's machine does. This is the read a submodule path changes the most. |
| G6. `chain_check.py:386-435` `changed` reads `diff --raw`, and `:1636` hands its paths to `lib/gate.py:13-23` `touches_code` (read) | A pull request whose only change outside the document roots is a submodule's pointer reads as touching no code under either setting, and the parity arm asks nothing of it. #1640 judged this read "may be harmless"; it is not. |
| G7. `tests/lib/test_gitcmd.py:114-169`: `CASES` holds one parameter for each key of `KEYS`, each run under git's defaults and under a value a person or a repository sets, and `test_every_key_has_a_case` compares `KEYS` with `CASES` (read) | The flag's cases take this shape: one for each subcommand and setting G3 measured, and one that compares the table of flags with the cases. |
| G8. Fourteen command forms of G4, each run in this repository with `--ignore-submodules=none` placed directly after the subcommand and without it, under git 2.50.1 and under `/Library/Developer/CommandLineTools/usr/bin/git`, 2.39.3: each form printed the same bytes both ways and exited 0 or 1 (executed, the loop over `diff`, `diff-tree`, `status` and `log` forms in the framer's run) | Under git's defaults the flag changes no reading, and each of the four subcommands takes it in first position. |
| G9. git's release notes, `Documentation/RelNotes/2.30.0.txt:74-76` at tag `v2.45.0` of `git/git`, fetched with `gh api`: "\"git rev-parse\" learned the \"--end-of-options\" to help scripts to safely take a parameter that is supposed to be a revision, e.g. \"git rev-parse --verify -q --end-of-options $rev\"". `2.24.0.txt:18` gives the general option parser the notation (executed). `git grep -n -F 'end-of-options' -- lib skills hooks .github evals/scripts` prints `range_read.py:227` alone, in `_commit`'s `rev-parse` (executed) | #1642 says 2.24 and names `git diff`. The tree passes the option to `rev-parse` alone, which reads it from 2.30. The floor `seal range` sets is 2.30. |
| G10. The release notes of 2.31.0 to 2.50.0, searched for each subcommand G4's probe lists (executed; a search by words, so a sample). The options they add to those subcommands, such as `ls-files --format`, `cat-file -Z`, `cat-file --batch-command` and `ls-tree --oid-only`, appear in no line the probe printed. `2.22.0.txt:21-23` gives `%(trailers)` its `key`, `valueonly` and `separator`, which `chain_check.py:2033` uses (executed) | No command of the scripts was found to need a git newer than 2.30. |
| G11. `git grep -c -e 'git version' -e 'oldest git' -e 'OLDEST' f7d315f01 -- lib skills hooks .github README.md README.ko.md docs CONTRIBUTING.md` prints nothing and exits 1 (executed). `README.md:51` and `README.ko.md:53` ask for `git` and Python 3.12, and `tests/behaviour/test_release_hygiene.py:1014-1030` holds the Python number against `ruff.toml` and both editions (read) | No text and no check states a git version, so the floor replaces nothing. The README sentence a person reads before installing is where the number goes, held as the Python number is. |
| G12. `git version` started thirty times by `subprocess.run` on this machine and timed with `time.perf_counter`: a median of 14 ms, the same as `git rev-parse HEAD` (executed, 2026-11-27) | A version read before every script's first command costs one more process on every run of every script and hook. A read in `seal range` alone costs it once a phase or a pass. |
| G13. The ticket's comments: `gh issue view 1640 --json body,comments` and `gh issue view 1642 --json body,comments` each return an empty `comments` list (executed, 2026-11-27) | Nothing after the bodies changes either request. |
| G14. `git grep -n -F -e 'ignore-submodules' -e 'ignoreSubmodules' f7d315f01 -- lib skills .github hooks evals/scripts` prints `lib/gitcmd.py:55`, `:58` and `:59` and `skills/implement/scripts/range_read.py:134`, `:142`, `:419` and `:429` (executed). The pathspec holds no path under `seal/` and none under `tests/` | S4's search is run at this commit. The three lines of `lib/gitcmd.py` stay in that file, and the four of `range_read.py` go. The search cannot print this frame or a case. |
| G15. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A script holds a gate only on a fact it reads exactly: an exit code, a parser's result, or a line of the plugin's own forms", and "before a fix adapts to an existing structure, ask whether the structure should change" (read) | The version is read from the one line `git version` prints, and a line in another shape is not read and refuses nothing. The flag moves into the runner and is not copied to each caller. |

## Scope

In scope:

1. `lib/gitcmd.py` holds a table of flags beside `KEYS`, `FLAGS`, from a subcommand to the options the runner puts directly after it. It holds `--ignore-submodules=none` for `diff`, `diff-tree`, `log` and `status`. `argv` builds them into the command, so each command `git` starts carries them.
2. `tests/lib/test_gitcmd.py` holds a case for each pair of subcommand and setting that G3 measured to take a path out, a case that the flag changes no reading under git's defaults, and a case that compares `FLAGS` with those cases.
3. `skills/implement/scripts/range_read.py` passes the flag nowhere itself: `DIFF` and `_uncommitted` lose it, with the comments that give its reason.
4. `lib/gitcmd.py` holds the floor, `OLDEST`, as `(2, 30)`, and `older(root)`, which answers with one line where the git that answers is older and with None otherwise. Its docstring states the floor's reason and the rule for a command a later change adds.
5. `seal range` asks `older` before its first git command and refuses with that line at exit 2, writing nothing.
6. `README.md` and `README.ko.md` state the git floor in the sentence that states Python's, and a case holds the number in both against `OLDEST`.
7. `lib/gitcmd.py`'s docstring is rewritten in place for items 1 and 4: the paragraph on a setting no `-c` key holds names the four subcommands and `FLAGS`, and tells no script to pass the flag.

Out of scope:

- **A case for each caller.** The flag is the runner's, so `chain_check.py`, `seal.py`, `broad_gate.py`, `settle.py`, `rule_changes.py` and `publish_release_note.py` change no line and gain no case. The two submodule cases of `tests/skills/test_range_read.py` stay as they are and keep reading the whole command.
- **A version read in every script.** `plan.md` *Alternatives considered* row 5 weighs it.
- **A run of the scripts under git 2.30.** No git older than 2.39.3 stands on this machine. `frame/questions.md` Q1 holds it.
- **The git the suite needs.** `tests/lib/test_gitcmd.py:54` already skips a case under a git older than 2.34. The floor is for the scripts a person's machine starts, under `lib/`, `skills/` and `hooks/`, and `CONTRIBUTING.md` is not changed.
- **`.github/scripts/` and `evals/scripts/`.** They run on GitHub's runners or at the owner's machine. They start git through the same runner and so carry the flags, and the floor is not stated of them.
- **`--ignore-submodules` at a value other than `none`.** `none` is git's default and the value round 3 of `1795742080-a-session-is-bound-by-the-crafters-rules` settled for `seal range`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A listing names a submodule's path whatever the setting | Given a repository whose submodule is ignored by `diff.ignoreSubmodules=all`, or by `ignore = all` in its `.gitmodules` entry. When a script reads `diff`, `log --name-only` or `status --porcelain` through `lib/gitcmd.py#git`, or `diff-tree` under the `.gitmodules` entry. Then the output names the submodule's path as it does under no setting | A parametrized case in `tests/lib/test_gitcmd.py`, one parameter for each pair G3 measured: the bare command prints something else, and the runner's command prints what git prints under no setting. Each parameter seen red with only its subcommand's entry taken out of `FLAGS` |
| S2. The flag changes nothing under git's defaults | Given the same repositories under no setting. When the same commands run. Then each prints what the bare command prints | The same parameters, in the shape of `test_accepts_what_git_prints_under_its_own_defaults` |
| S3. A subcommand added to the table gets a case | Given `FLAGS`. When a subcommand is added to it with no case. Then a case fails | A case that compares the subcommands of `FLAGS` with those of the parameters, as `test_every_key_has_a_case` does for `KEYS`. Seen red with one parameter removed |
| S4. No script passes the flag itself | Given the tree after the build. When the flag is searched for. Then `lib/gitcmd.py` alone holds it | `git grep -n -F -e 'ignore-submodules' -e 'ignoreSubmodules' -- lib skills .github hooks evals/scripts` prints lines of `lib/gitcmd.py` and no other file. At `f7d315f01` it prints `lib/gitcmd.py:55`, `:58` and `:59`, which the design keeps in that file, and `range_read.py:134`, `:142`, `:419` and `:429`, which *Removes* rows 1 and 2 take out (G14) |
| S5. `seal range` still names a submodule | Given the fixtures of `test_accepts_a_submodule_by_name_and_does_not_print_it` and `test_accepts_an_uncommitted_submodule_named_as_not_read`. When `seal range` runs with no flag of its own. Then both cases pass | `tests/skills/test_range_read.py`, unchanged in those two cases. With the `diff` entry, then the `status` entry, taken out of `FLAGS`, each fails |
| S6. `older` reads the version git prints | Given a git whose `version` prints `git version 2.29.3`, `git version 2.30.0`, `git version 2.50.1 (Apple Git-155)`, `git version 2.39.2.windows.1`, or a line in another shape. When `older(root)` is asked. Then it answers with a line naming the printed version and `OLDEST` for the first, and with None for each of the others | Cases in `tests/lib/test_gitcmd.py`, the runner's answer to `version` supplied by the case. The refusing and the accepting cases each seen red against a mutation of the comparison, and the other-shape case seen red with the shape check removed |
| S7. `seal range` says why it cannot run | Given a git older than `OLDEST`. When `seal range <item> --from <commit> --out <file>` runs. Then it prints `older`'s line, exits 2, writes no file, and starts no `rev-parse` | A case in `tests/skills/test_range_read.py`. Seen red with the ask removed |
| S8. The README states the floor | Given `OLDEST`. When either edition of the README is read. Then its requirements sentence states that version | A case beside `test_the_python_floor_is_the_same_number_everywhere` in `tests/behaviour/test_release_hygiene.py`, or where `CONTRIBUTING.md` *The test layout* puts it. Seen red with the number changed in one edition |

## Data & interfaces

- **`lib/gitcmd.py#FLAGS`.** A mapping from a subcommand's name to a tuple of options. `argv(*args)` keeps its signature. The subcommand is the first argument past the global options a caller passes before it (`lib/gitcmd.py#argv`). `argv` puts the subcommand's options directly after it. `Failed.command` and the key `one_run` answers by stay the caller's arguments, without the options, as they stay without the `-c` pairs.
- **`lib/gitcmd.py#OLDEST`.** `(2, 30)`, the major and minor numbers.
- **`lib/gitcmd.py#older(root)`.** It starts `git version` through `git` and reads the first line in the form `git version <major>.<minor>`, followed by anything. A line in another shape, or a git that exits non-zero, is not read: the answer is None and nothing is refused. `Unrun` passes through as from any command. The line it answers with names the version git printed and `OLDEST`; its wording is the builder's, pinned by S6.
- **`seal range`.** `range_read.py#_read` asks `older` before `_commit` and raises `Refused` with the line. The exit code and the unwritten file are those of its other refusals.
- **What the change to the gate must carry** (`CONTRIBUTING.md` *What a change to a gate must carry*). Item 1 makes `chain_check.py` refuse more: a commit or a pull request that changes a submodule's path is now read as changing it under either setting, as it already is under none. A wrong allow there let a change stand after the last round unread. Item 5 reads one line of git's own output in one form, names nothing as unread, and leaves no meaning to an agent.

## Rule changes

- change
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  from: A setting measured to do it that no `-c` key
    reaches, such as one a file of the repository carries, is held by a flag
    on each command it reshapes. `lib/gitcmd.py`'s docstring names each key,
    and each such setting with its flag, with what it changes and the
    subcommands it changes, and one found later is added there and nowhere
    else.
  to: A setting measured to do it that no `-c` key
    reaches, such as one a file of the repository carries, is held by a flag
    `argv` puts on every command of each subcommand the setting reshapes, so
    no script passes it. `lib/gitcmd.py`'s docstring names each key, and each
    such setting with its flag, with what it changes and the subcommands it
    changes, and one found later is added there and nowhere else.
- change
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  from: Whether a call is one of these is read at review, and
    `tests/lib/test_gitcmd.py` holds each key.
  to: Whether a call is one of these is read at review, and
    `tests/lib/test_gitcmd.py` holds each key and each flag.
- add
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  to: **A script under `lib/`, `skills/` or `hooks/` starts no git command
    that a git older than `lib/gitcmd.py#OLDEST` refuses or reads otherwise,
    and the script whose command set that version asks
    `lib/gitcmd.py#older` before its first command.** A person's machine
    runs these scripts on the git it has, and an agent that meets git's own
    refusal mid-run reads it as a fact about the repository. `OLDEST` is the
    version git's release notes give for the newest option those scripts
    pass, and its docstring names that option. A change that adds a command
    only a newer git reads raises `OLDEST` in the same commit and moves the
    ask to its script. `older` reads the one line `git version` prints, and
    a line in another shape refuses nothing.
    check: tests/lib/test_gitcmd.py tests/skills/test_range_read.py
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: exits 2 and writes nothing where the commit is no ancestor of HEAD or the file cannot be written
  to: exits 2 and writes nothing where the commit is no ancestor of HEAD, the file cannot be written, or the git that answers is older than `lib/gitcmd.py#OLDEST`

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| 1. The flag `--ignore-submodules=none` in `DIFF`, and the comment sentence that gives its reason | `skills/implement/scripts/range_read.py#DIFF` | `lib/gitcmd.py#FLAGS` holds the flag for `diff`, and the module's docstring holds the reason. The two cases of S5 keep holding what `seal range` prints |
| 2. The flag in `_uncommitted`'s `status`, and the comment above it | `skills/implement/scripts/range_read.py#_uncommitted` | The same table, for `status` |
| 3. The sentence that tells a script to pass the flag on each such command, with its citation of `range_read.py#DIFF` and `#_uncommitted` | `lib/gitcmd.py`, the module docstring's paragraph opening "A setting that no `-c` key holds" | Rewritten in place by *Scope* item 7: the runner passes it |
| 4. Nothing goes in return for `OLDEST`, `older` and the rule that states them | `lib/gitcmd.py`, `docs/running/what-a-script-gates.md` *Which gate a script holds* | No text and no check of the tree states a git version (G11), so there is no earlier statement or reader to take out. The read answers a refusal a person's git gives today under another message, and it is no mark of a step that failed in a run |

Framed 2026-11-27 by framer, before the build.
