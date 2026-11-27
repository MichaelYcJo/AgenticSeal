# Implementation Plan: scripts read git past submodule settings and a floor (#1640, #1642)

## Technical context

The tree as read at `f7d315f01`.

The work builds on the one module that starts git and on the one script that sets the oldest git.

- `lib/gitcmd.py:83-106` holds `KEYS` and `argv`, and `:247-275` holds `git`, which builds each command with `argv("-C", root, *args)`. `:54-61` is the docstring paragraph on a setting no `-c` key holds.
- `tests/lib/test_gitcmd.py:114-169` holds one parameter for each key and the case that compares `KEYS` with them.
- `skills/implement/scripts/range_read.py:134-143` holds `DIFF`, `:414-431` holds `_uncommitted`, and `:219-232` holds `_commit`, whose `rev-parse` passes `--end-of-options`.
- `tests/skills/test_range_read.py:366` and `:466` hold the two submodule cases, each on a fixture whose `.gitmodules` entry reads `ignore = all` and whose configuration sets `diff.ignoreSubmodules` to `all` (`:41-48`).
- `README.md:51` and `README.ko.md:53` state what a person installs, and `tests/behaviour/test_release_hygiene.py:1014-1030` holds the Python number in both.

Constraints the build meets:

- `lib/gitcmd.py` is Python 3.9 syntax and standard library only (`lib/gitcmd.py:72-74`), because hooks reach it on whatever `python3` starts them.
- `argv` is called with a leading `-C <directory>` pair by `git` and by `tests/lib/test_gitcmd.py:141`, `:163` and `:267` and `tests/github/test_release_seal.py:1164`. The last two compare a whole argv for `cat-file`, which takes no flag.
- A case that pins a key runs the bare command first and asserts it prints something else (`tests/lib/test_gitcmd.py:161-163`), so a setting that changes nothing fails the case and does not pass it silently. The flag's cases keep that assertion.
- `diff-tree` is not reshaped by `diff.ignoreSubmodules` (`frame/design.md` G3), so its one parameter is the `.gitmodules` entry. A parameter for the configuration key would fail the bare-command assertion.
- A new case is seen red with only the guard it names removed (contract rule 15). Each parameter of S1 names one subcommand's entry of `FLAGS`.
- A change to a message a person reads is documented and pinned in the same commit (contract rule 14). `older`'s line and `seal range`'s refusal are such messages.
- `tests/behaviour/test_docs_line_wrap.py` holds the prose width of the two README editions, and hygiene's step *both READMEs move together* warns where one changes alone.

What breaks in six months. First, a person sets a submodule's `ignore` because `git status` walks a large submodule slowly, and `chain_check.py --worktree` now walks it on every run, since its `diff --raw` of the working tree carries the flag. The signal is `lib/gitcmd.py#Unrun` naming that command past `TIMEOUT`. The reads with a pathspec, `status -- <one path>`, do not walk it. Second, a later change adds a git option newer than `OLDEST` and raises nothing, because no run starts a git that old and review is the one reader of the rule. The signal is a person's report of git's own refusal, which is what #1642 describes today. `frame/questions.md` Q1 holds the run that would show it. Third, git prints its version in a shape `older` does not read, and `seal range` then meets git's refusal as before. The cost is the message and no wrong refusal.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. The runner passes the flag: `lib/gitcmd.py#FLAGS` holds `--ignore-submodules=none` for the subcommands the settings reshape, and `argv` puts it on each command (`frame/design.md` *Scope* items 1 to 3) | A caller that wants a submodule left out cannot say so, and a whole-tree read of the working tree walks an ignored submodule (*Technical context*) | Chosen. `git` is the one function that starts git (`frame/design.md` G2), so the flag reaches each read by construction, as the `-c` pairs do, and the next script that lists a diff needs to know nothing. No caller wants a submodule left out: each read asks what changed |
| 2. Keep the structure: each script passes the flag at each read, as `range_read.py` does and as #1640's list asks, on `chain_check.py:400`, `:408`, `:463` and `:977`, `seal.py:1494`, `broad_gate.py:2157`, `settle.py:1595` and the `log` listings | The next read is written without it. That is how the defect arrived: `seal range` was written against a module that named no such setting, round 1 of `1795742080-a-session-is-bound-by-the-crafters-rules` found it, and #1640's own list, written from a search, lacks `chain_check.py#touched`, which the invariants of the core stand on (`frame/design.md` G4, G5). Each flag also owes a case seen red at its caller. The premise that keeps the structure, checked: "a script that lists those paths passes the flag on each such command" (`lib/gitcmd.py:59-61`). It held for one script out of those G4 lists | Rejected |
| 3. Judge each read, and write a reason where a submodule's path cannot change the answer, #1640's second branch | The reasons are sentences about what a pathspec can hold, such as "a `routing.md` is no gitlink", and each is a universal the next change to the caller can make false without editing it (contract rule 19). The reads a path does change still need the flag (`frame/design.md` G5, G6) | Rejected. The policy in force asks for the flag on each command the setting reshapes (`frame/design.md` G1) |
| 4. Hold the setting in `KEYS`, as `-c diff.ignoreSubmodules=none` | The key does not reach a `.gitmodules` entry. Round 3 of `1795742080-a-session-is-bound-by-the-crafters-rules` measured it, and `lib/gitcmd.py:58` states it | Rejected, as that round settled |
| 5. The floor is read by the runner: `git` asks `git version` before the first command of each process and refuses below `OLDEST` | One more process on every run of every script and hook, 14 ms each on this machine (`frame/design.md` G12), and each case that loads a script anew pays it again. It also refuses a person on a git between the next lower option's version and 2.30 for commands that read correctly there. It has no catch to its name: #1642 came from a round's *Not judged* row and from no report | Rejected for cost. The script whose command set the floor asks alone |
| 6. State the floor and add no read, #1642's second branch alone: each script stays within 2.30, so nothing needs to say so | An agent runs `seal range` on a git older than 2.30 at the close of a phase, meets a refusal that names the commit and not git, and spends the pass trying other commits. The reader of that message is an agent mid-run, which did not read the README | Rejected as the whole answer. The README states the floor, and `seal range` says so too (`frame/design.md` *Scope* items 5 and 6) |
| 7. Lower what `seal range` needs: drop `--end-of-options` and refuse a `--from` value that opens with `-` in the script | The script then re-encodes which strings git reads as options, which is git's parser's to answer. git's release notes give the flag as the form for a script that takes a revision from a person (`frame/design.md` G9). The floor would then rest on the other options' versions. The release notes read here give 2.22 for `%(trailers)`'s (`frame/design.md` G10) and were not searched below it | Rejected. The flag stays and the floor is 2.30 |
| 8. Read the version only after a command fails, in `lib/gitcmd.py#Exited` | A caller that reads a non-zero exit as an answer never raises `Exited`. `range_read.py#_commit` is one: it reads `rev-parse`'s exit as "does not resolve to a commit" | Rejected. It misses the one command the floor comes from |
| 9. Make the floor real in CI: a job in a container whose git is 2.30 runs the suite | The suite itself needs a newer git in places (`tests/lib/test_gitcmd.py:54`), the job adds a leg every pull request waits on, and no image's git version was read here | Rejected for this work. `frame/questions.md` Q1 holds the one run that answers whether 2.30 reads the scripts' commands |
| 10. State the floor in prose alone, in the README and the docstring, with no constant | The number then stands in three texts with nothing holding them together, which is the state `tests/behaviour/test_release_hygiene.py:1014` exists to stop for Python | Rejected. `OLDEST` is the one source, the README case reads it, and `older` compares against it |
| 11. A case at each caller, such as `follows` refusing a commit that moves an ignored submodule's pointer | It holds the runner's flag a second time, through a fixture of round records, and adds lines to `tests/skills/test_chain_check.py`, which another work item of the release changes | Rejected. S1 holds each subcommand at the runner, and S5 holds one whole command |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2 and 3 of `frame/design.md`, the part of item 7 that rewrites the paragraph on a setting no `-c` key holds, and the cases of S1, S2, S3 and S5. Done when each parameter of S1 was seen red with only its subcommand's entry taken out of `FLAGS`, and `range_read.py` passes the flag nowhere | The *Phase boundary* set of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, as one command through `bin/test`: `tests/lib/test_gitcmd.py`, `tests/skills/test_range_read.py`, `tests/github/test_release_seal.py`, each other test file that reads a path the phase changed, and the tree-wide test files. `seal mutate` over `lib/gitcmd.py#argv`. The search of S4, which prints lines of `lib/gitcmd.py` and of no other file | |
| 2 | *Scope* items 4, 5 and 6, the rest of item 7, and the cases of S6, S7 and S8. Done when each case was seen red as its row of *User scenarios & acceptance* says, both README editions state the floor, and `changelog.md` is committed | The same set, drawn over this phase's paths: `tests/lib/test_gitcmd.py`, `tests/skills/test_range_read.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_docs_line_wrap.py`, each other test file that reads `README.md`, `README.ko.md` or another path the phase changed, and the tree-wide test files. `seal mutate` over `lib/gitcmd.py#older` and over the ask in `range_read.py#_read` | |

## Overlap with the release

Neither other work item had a frame committed when this one was written: `fix/1630-1639-the-orchestrators-records-after-the-last-round` stood at `e503c6961` and `fix/1641-the-cores-margin-depends-on-the-path` at `7f388fa1f`, each holding its `routing.md` alone (read 2026-11-27). The rows below are read from the issues and from the files the spawn names.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| `1795759276-the-orchestrators-records-after-the-last-round` (#1630, #1639) | This work changes no line of `skills/code-review/scripts/chain_check.py` and none of `tests/skills/test_chain_check.py`. It changes a fact that item's records arm reads: `chain_check.py#touched`, and so `follows` and `records_only`, list a submodule's path under a `.gitmodules` `ignore`. Both may change `skills/implement/scripts/range_read.py`, where #1639's *Done when* lets `seal range` read the orchestrator's rows: this work takes two flags out of `DIFF` and `_uncommitted` and adds the ask at the head of `_read`. Both may state operations on `docs/running/what-a-script-gates.md` *The checks*, which the settle writes in merge order | #1640 | This work's diff is the smaller and changes no rule of the records arm, so it is the likelier to be sealed first. Merged first, it lets that item's cases of the records arm run over the runner that already carries the flag, and a conflict in `range_read.py` is met inside rounds that item spends on its own mechanism |
| `1795759278-the-cores-margin-depends-on-the-path` (#1641) | Nothing. Its files are `lib/core.py`, `tests/lib/test_core.py` and the version move, and this work touches none of them and reads no fact of the core's size | either | No order costs more than the other |

## Operational impact

- A person on a git older than 2.30 now reads `seal range`'s refusal with the cause named, where git's own refusal reached them before. Nothing else refuses on the version.
- Both README editions state a git floor for the first time.
- In a repository whose submodule is ignored by `diff.ignoreSubmodules` or by its `.gitmodules` entry, `chain_check.py`, `seal mode`'s guard, `seal settle`'s listings and the release note's fragment listing now read the submodule's path as they do under no setting. For `chain_check.py` this refuses more: a commit that moves the pointer after the last round, the gate or the seal is read as a change outside the work item's records.
- No migration, no environment variable and no dependency. This pull request does not carry the release's version move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
