# Review round 3: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: 384f9c04b, fixes 7fa4a1692..384f9c04b
```

This is the verifying round. The fix diff is `7fa4a1692..384f9c04b`, read in a `git clone --no-local` checked out at `384f9c04b` under this round's scratch directory. It holds the fold at `f865cab26` (`frame/design.md:91`, `frame/plan.md:26`), the fix at `fd984795f` (the link guard in `hooks/edit-leaves-copies.py#main`, the docstring at `:57-64`, `changelog.md:3` and three new cases in `tests/hooks/test_edit_leaves_copies.py`), and round 2's close blocks at `384f9c04b`. The code this round reviews is the guard and its three cases. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `hooks/edit-leaves-copies.py` and `trail/rounds/round-2.md`. No `pr.<lang>.md` stands, and `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared, and `seal/config.json` has no `Pact` key.

Carried from rounds 1 and 2 rather than established again: `trail/phases/phase-1.md` and `trail/phases/phase-2.md`, which the fix diff does not change; Probe B's counts, which `frame/plan.md:26` cites; the boundary at `SECURITY.md:43-46`; and round 2's list of the hook's calls that resolve a path, which are `open` at `:192` and `:269`, `os.walk` at `:133`, and `optin.marked` in `#_located`. `lib/` and `hooks/hooks.json` are unchanged over the fix diff (`git diff --stat 7fa4a1692 384f9c04b -- lib hooks/hooks.json` printed nothing). Round 2 judged the `optin.marked` read bounded. This round derived that verdict again, and finding 1 is the result.

This round's own axes, beside the table's, are the order of each read against the guard that should stop it, each guard component against the case that pins it, and the two doubts the caller handed over: a Windows junction, and the FIFO close.

## Findings

### 1. The hook opens the root's `README.md` through a root that is a link before the new guard returns, so "reads nothing" in `changelog.md:3` and the guard's comment is false there

```seal
severity: should
location: `hooks/edit-leaves-copies.py:111-117`, `hooks/edit-leaves-copies.py:257-266`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/changelog.md:3`
evidence: executed `python3 -I test_tmp_round3_root_link.py <clone>/hooks/edit-leaves-copies.py <scratch>/g-target` (Probe G, `## Probes`); executed `git grep -n -E "is a link|that is a link|a link\b|outside the item's directory|file outside the|outside the repository" -- hooks tests/hooks seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix README.md README.ko.md CONTRIBUTING.md SECURITY.md docs ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'`; read `hooks/edit-leaves-copies.py:111-117`, `:253-270`, `lib/optin.py:237-243`, `:256-272`
regression: round-2#1
```

Why it matters: the unit is the link guard that `fd984795f` added to `#main` at `:257-266`. The frame says the hook reads on only where no component of the path from `<root>` down to `<file>`, `<root>` among them, is a link (`frame/design.md:91`, the fold at `f865cab26`). The fix checks the root in `#main`. By then `#_located` has already called `optin.marked` on the root (`:111-113`), and that call opens `<root>/README.md` (`lib/optin.py:242`), following the link. So the defect came from where the guard was placed: after the first open, not before it.

Claimed in round 2's close: the guard is "one guard in `#main`, before the first open". At `:253-269` the guard comes before the open of the edited file. It comes after the open of the root's `README.md`. Probe G made the repository's `seal` a link to a directory outside it, whose `README.md` is a FIFO (a named pipe). A FIFO is used here only because its writer's `open` returns once a reader opens it. The hook at the target opened it, and then printed nothing.

The read is bounded at the marker's length plus two characters (`lib/optin.py:243`). It yields a true or false, and nothing of it is printed. What it leaks is small. Two sentences the fix pass wrote still say something false:

- `changelog.md:3`: "It reads nothing where a link stands anywhere from the root down to the edited file". A person reads this in the release notes.
- The comment at `:257-260`: "So the hook reads nothing on such a path."

The docstring at `:57-61` says such a path "prints nothing". That is true, and it stays as it is.

The listing command printed `:59`, `:130`, `:258`, `changelog.md:3`, `frame/design.md:27`, `:91`, `:133` and `frame/plan.md:67`. It also printed the case docstrings at `tests/hooks/test_edit_leaves_copies.py:305`, `:316-317` and `:336`, and `CONTRIBUTING.md:485` with `docs/running/the-run.md:49` and `:64`. `:258` and `changelog.md:3` are the two false sentences above. `frame/design.md:91` states the reads-on condition, and with the snippet the code reads it as written. `frame/design.md:133`, the `## Rule changes` row, says the hook reads "no file outside the item's directory". The root's `README.md` lies outside the item's directory, but the same row's *Reads* cell names that read ("under a root whose `README.md` opens with the marker"). So this round reads the cell as being about the records, and the snippet leaves it. `frame/design.md:27` and `frame/plan.md:67` are dated to the commits they record. The rest state other facts. The command searches on words, so it is a sample under contract rules 12 and 19. The list of reads was made from the hook's calls that open a path, as carried from round 2. Of those calls, `optin.marked` is the one that runs before the guard.

The snippet moves the root's check into `#_located`, ahead of `optin.marked`. Then both sentences hold as written, and `changelog.md:3` needs no change. Precondition: `os.path.islink` reads the root's name itself and follows no link. The snippet returns `None` at the first `threads` directory whose parent is a link. That loses nothing. The old walk went on upward only to look for a marked root higher up. A path that reaches such a root holds this link under the item, and the guard in `#main` refuses that path anyway. The root's entry in `#main` then stands on nothing, so the snippet drops it. Otherwise its mutant survives every case.

The case `test_refuses_to_print_where_the_root_threads_or_a_directory_in_the_item_is_a_link`, through its `via_root` path, already pins the moved check. With the snippet applied in the clone, the module passed 23. With the new `islink(root)` lines removed it failed, so the case is seen red. No case pins the order, meaning that the check runs before the open. Probe G holds it, because only a FIFO shows an open. A case built that way needs `os.mkfifo`, which Windows lacks, so the fix pass weighs it under contract rule 15 and says what it chose. Where the snippet stops: a `README.md` that is itself a link is not on the path, and `optin.marked` reads through it in every gate of the plugin (`## Not judged`).

```python
# hooks/edit-leaves-copies.py, `_located`, in place of lines 111 to 118:
        if os.path.basename(parent) == optin.WORK_ITEMS:
            root = os.path.dirname(parent)
            # A root that is a link is not opened: `optin.marked` reads its
            # `README.md`, which the link can place outside the repository.
            if os.path.islink(root):
                return None
            if optin.marked(root):
                inner = "/".join(rel[1:])
                if inner.endswith(".md") and _read(inner):
                    return os.path.join(parent, rel[0]), inner
                return None
        here = parent

# `main`, in place of lines 257 to 263:
    # A link from the root's `threads/` down to the edited file can name a
    # file or a directory outside the repository: `open` follows it at the
    # file and at every directory over it, and `os.walk` follows the item's
    # directory it starts at. `_located` has refused a root that is a link
    # before opening it. So the hook reads nothing on such a path.
    parts = rel.split("/")
    on_path = [os.path.dirname(item)]
```

```seal
verdict: fixed 5a4547218
answer: `5a4547218` applies the snippet. `#_located` returns None where the root over the first `threads` directory is a link, ahead of `optin.marked`, and `#main`'s guard drops the root and starts at `threads/`. The guard's comment says what each check covers, in order: `_located` refuses a root that is a link ahead of `optin.marked`, which opens the root's `README.md`, then the guard in `#main` refuses a link at `threads/`, the item's directory or any component under it down to the edited file, before the first record is opened. `changelog.md:3` states the same order. The round's snippet said `changelog.md:3` needs no change, and the orchestrator asked for the order to be stated, so it is rewritten. The docstring names, in one clause, the root's `README.md` that is itself a link as outside the guard, since `lib/optin.py#marked` reads it for every hook and gated command. That case goes to the orchestrator's issue. Seen red: the existing `test_refuses_to_print_where_the_root_threads_or_a_directory_in_the_item_is_a_link`, with the new `islink(root)` check replaced by `if False:`, failed at its `via-root` path (`seal mutate`, exit 0, red). After the commit, a batch of three mutants was all red: that check off, the guard in `#main` off, and `on_path` emptied. I ran my own Probe G, `test_tmp_root_link_fifo.py` under this fix pass's scratch directory: a repository whose `seal` links to a directory whose `README.md` is a FIFO, with a writer thread that records whether a reader opened it. The hook at `5a4547218` did not open it, the hook at `fd984795f` did, and both exited 0 with nothing on stdout. I added no case to pin the order. An out-of-order check costs one read, bounded at the marker's length plus two characters, whose result is a true or false that is never printed. A case that shows the order needs `os.mkfifo`, a writer thread and a skip on Windows, and that costs on every run more than the order protects (`skills/core/SKILL.md` *The rule a mechanism is kept against*). The order is held by the probe above and stated in the comment. The listing command, run again at `5a4547218` with `trail/` left out, prints the hook's `:59`, `:115-116`, `:136` and `:264-265`, which hold at HEAD; `changelog.md:3`, which holds; `frame/design.md:91` and `:133`, which hold as round 3 reads them; `frame/design.md:27` and `frame/plan.md:67`, dated to the commits they record; the case docstrings at `tests/hooks/test_edit_leaves_copies.py:305`, `:316-317` and `:336`, which hold; and `CONTRIBUTING.md:485` and `docs/running/the-run.md:49` and `:64`, which state other facts. It is a sample.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the hook no longer reads the edited file through a link, and no longer walks an item's directory that is a link. Probes D1 and D2 of round 2 are now the cases `test_refuses_to_print_where_the_edited_file_is_a_link` and `test_refuses_to_print_where_the_work_items_directory_is_a_link`. `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` passed 46 (executed). The close's six mutants were re-run as one `seal mutate` batch: the guard off, the root dropped, `threads/` dropped, the file dropped, the item's directory dropped, and the directories inside the item dropped. All six were red at exit 1 (executed). Each new case was then run alone against the mutant of its own component and of one other. The file case was red for the file mutant and survived the root mutant. The directory case was red for the item mutant and survived the file mutant. The third case was red for the root, `threads/` and inner-directory mutants and survived the item mutant (executed). So each component is pinned by exactly one case, and the close's account of which case holds which component is true. The docstring at `:57-64` and `frame/design.md:91` state the guard as built. Finding 1 is the one place where the close does not reach: the order of the root's check against the root's marker read.

```seal
confirms: round-2#2
```
What holds: `frame/plan.md:26` now ends with "`frame/questions.md` Q1, its Status cell, records where the harness delivered a plugin hook's text and this hook's own text". That cites the home and no longer restates it. Round 2's listing command for this finding was re-run at the target. It prints `frame/plan.md:26`, `frame/questions.md:14`, `gaps.md:10` and `gaps.md:11` (executed). The plan row cites the Status cell. `gaps.md:10` and `:11` each cite the session they close on, and the Status cell records the third and fourth sessions (read).

What matched: the caller's first doubt, a Windows junction. The claim is that a junction on the path is still followed, since `os.path.islink` does not report one. That holds for Python's `os.path.islink`. It does not reach the boundary that `SECURITY.md:43-46` names. Git's tree stores a regular file, an executable file, a symbolic link (mode 120000), a directory and a submodule entry, and nothing else. On Windows, a checkout writes a link as a symbolic link where `core.symlinks` is on, which `os.path.islink` reports, and as a plain file that holds the target where it is off. No checkout writes a junction. A junction on the path is therefore made by a person or a process on the machine, which `SECURITY.md:43-46` does not treat as an attacker. The frame owes no sentence on it. `frame/design.md:91` says "a link", the docstring gives the reason ("a link can name a file or a directory outside the repository"), and neither one promises anything about a reparse point that git cannot deliver. This rests on git's object model as read. No Windows run was made (`## Not judged`).

What matched: the caller's second doubt, the FIFO close, which is kept on its first ground alone. After `fd984795f`, a FIFO can reach an `open` of this hook in only one way. It has to be a name under the item that is not a link, because `#main` refuses a path with a link and `#_records` skips a name that is a link (`:137`). Git checks out none of those as a FIFO, and the same holds in a submodule, whose checkout has the same file modes. So an `isfile` guard has nothing a checkout can deliver to catch. The close's second ground, which round 2 refuted, is no longer claimed (`trail/rounds/round-2.md:66`). The close holds.

What matched: the hook's time after the guard. Probe F2 ran the target's script ten times on an edit payload of this item's `frame/design.md`. A run took 0.031 to 0.038 s, against 0.018 to 0.019 s for an interpreter that does nothing. The crafter's 0.028 to 0.036 s is of the same order. No record states the crafter's figure (`git grep` on `0.028` printed nothing outside `trail/`), so no record needs it to hold.

What matched: `pr.md`'s three quotes. `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` exited 0 with a `wrote:` line and no note (executed). Line 1's coordinate, the row at `frame/plan.md:20`, is unchanged by the fold.

What matched: `changelog.md:3` apart from finding 1's clause, `frame/design.md:91` and `frame/plan.md:26` each state what `fd984795f` built. `frame/design.md:133` stands as finding 1 reads it. The timings at `frame/plan.md:26` and `frame/questions.md:14` are dated to `5604aa15d`, and the guard adds a few `lstat` calls to a run.

The three new cases each cover a component that no older case covers. The older `test_refuses_to_print_where_the_words_stand_only_behind_a_link` covers a link among the records. No new case duplicates another in `Test_main`. Each is labelled `A10`. A10's row names a file outside a marked root's `threads/` and not a link, but `frame/design.md:91` states the fact each case holds, so each holds a fact the frame states.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a checked-out `README.md` that is itself a link, to a device such as `/dev/tty`, can block a hook: `optin.marked` opens it for every gate of the plugin, not only this hook, and finding 1's snippet does not reach it. Not probed here, and outside the fix diff | `lib/optin.py:237-243`, `:256-272` | the orchestrator, as an issue of its own beside the one `frame/plan.md:67` names |
| A Windows run of the guard and of a checkout with `core.symlinks` on and off. This round's account of the junction doubt rests on git's object model as read | `hooks/edit-leaves-copies.py:257-266` | the orchestrator's broad run on its Windows runner, should the workflow include one |
| The crafter's narrow set, 1126 passed and 9 skipped. This round ran the two modules named above, not that set. The suite beyond them, the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` | 46 passed |
| `bin/seal mutate hooks/edit-leaves-copies.py --tests "bin/test -q tests/hooks/test_edit_leaves_copies.py"` with six `--replace` pairs: the guard's `if any(...)` to `if False:`; `on_path = [root, os.path.dirname(item)]` to `[os.path.dirname(item)]` and to `[root]`; `range(len(parts) + 1)` to `range(len(parts))` and to `range(1, len(parts) + 1)`; the inner list to `[item, os.path.join(item, *parts)]` | baseline passed; 6 mutants, 6 red, each at exit 1 |
| The same tool, `-k` on each new case: the file case with the file and root mutants; the directory case with the item and file mutants; the third case with the root, `threads/`, inner-directory and item mutants | file case: red, survived; directory case: red, survived; third case: red, red, red, survived |
| `python3 -I test_tmp_round3_root_link.py <clone>/hooks/edit-leaves-copies.py <scratch>/g-target`, the file under this round's scratch directory (Probe G) | exit 0, stdout empty; the FIFO `README.md` behind the linked root was opened by the hook |
| Finding 1's snippet applied to the clone's hook, then Probe G into `<scratch>/g-patched`, `bin/test -q tests/hooks/test_edit_leaves_copies.py`, and `seal mutate` removing the new `islink(root)` lines with `-k root_threads_or_a_directory`; the file restored with `git checkout` afterwards | the FIFO was not opened; 23 passed; with the lines removed, the third case failed |
| `python3 -I test_tmp_round3_time.py <clone>` (Probe F2) | hook 0.031 to 0.038 s over ten runs; `python3 -I -c pass` 0.018 to 0.019 s |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` | exit 0, `wrote:` line, no note |
