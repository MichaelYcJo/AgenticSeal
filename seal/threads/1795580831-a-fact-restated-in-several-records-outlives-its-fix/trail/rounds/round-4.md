# Review round 4: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: 794e4650c, fixes 384f9c04b..794e4650c
```

This is the verifying round. The fix diff is `384f9c04b..794e4650c`, read in a `git clone --no-local` checked out at `794e4650c` under this round's scratch directory. It holds the fix at `5a4547218` (`hooks/edit-leaves-copies.py#_located`, the guard and its comment in `#main`, the docstring at `:57-66`, and `changelog.md:3`) and round 3's close block at `794e4650c`. The code this round reviews is `#_located`'s new root check and the narrowed guard in `#main`. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/rounds/round-3.md` and `hooks/edit-leaves-copies.py`. No `pr.<lang>.md` stands, and `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared, and `seal/config.json` has no `Pact` key.

Carried from rounds 1 to 3 rather than established again: Probe B's counts, which `frame/plan.md:26` cites; the boundary at `SECURITY.md:43-46`; round 2's list of the hook's calls that resolve a path, with `optin.marked` in `#_located` as the one that runs before the guard; and round 3's reading of `frame/design.md:133` as being about the records. `lib/`, `hooks/hooks.json` and `tests/` are unchanged over the fix diff (`git diff --stat 384f9c04b 794e4650c -- tests lib hooks/hooks.json` printed nothing).

This round's own axes, beside the table's: every `optin.marked` call on the walk in `#_located` against a link above it, the order of the root's check against the marker read and the case that holds it, and the two questions the caller handed over. The caller put a root `README.md` that is itself a link out of scope, as an issue of its own with `lib/routing.py#read_declaration`, and this round leaves it there.

## Findings

### 1. The hook still opens a `README.md` through a link before the guard returns, where a directory named `threads` stands below the link, so "It reads nothing" in `changelog.md:3` and the guard's comment is still false

```seal
severity: should
location: `hooks/edit-leaves-copies.py:113-119`, `hooks/edit-leaves-copies.py:263-270`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/changelog.md:3`
evidence: executed `python3 -I test_tmp_round4_probes.py <clone>/hooks/edit-leaves-copies.py <scratch>/p-head head`, and the same against the hook of `fd984795f` (Probe H, `## Probes`); executed `git grep -n -E "reads nothing|read nothing|opens no record|before it opens" -- hooks tests/hooks seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix README.md README.ko.md CONTRIBUTING.md SECURITY.md docs ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'`; read `hooks/edit-leaves-copies.py:99-124`, `:259-280`, `lib/optin.py:237-272`
reopens: round-3#1
```

Why it matters: round 3's close says `changelog.md:3` now holds. It does not hold in every case its words cover. `#_located` walks up from the edited file, and it calls `optin.marked` on the parent of every directory named `threads` it meets, innermost first (`:113-119`). The new check refuses only the candidate root that is itself a link (`:117`). A candidate that stands below a link is not itself a link, so its `README.md` is opened through the link. Only after that does the walk reach the real root, and only then does the guard in `#main` refuse the path.

Probe H builds that case. The marked root's `threads/<item>` is a link to a directory outside the repository. Under it stands `sub/threads/x/frame/design.md`, and `sub/README.md` is a FIFO (a named pipe, used only because opening it shows up on the writer's side). The edit is of that `design.md` through the link. At `794e4650c` the hook opened the FIFO and printed nothing. It did the same at `fd984795f`, so the defect predates `5a4547218`, and that fix left it standing.

The read is bounded at the marker's length plus two characters (`lib/optin.py:243`), it yields a true or false, and nothing of it is printed. The file it reads sits in the directory the `Edit` call itself already reached through the same link. So what leaks is close to nothing, and the code needs no change. What is false is the absolute the text promises:

- `changelog.md:3`: "It reads nothing where a link stands anywhere from the root down to the edited file". A person reads this in the release notes.
- The comment at `:270`: "So the hook reads nothing on such a path."

Each further case of this kind costs another round while the sentences promise "nothing" for every read. A code fix does not end that. A walk that checks each component for a link before each `marked` call cannot see a link above an inner candidate until it has passed that candidate. This round applied such a walk in the clone, and Probe H still opened the FIFO (`## Probes`). The fix is to say what the guard decides: it opens no record and prints nothing, which the existing link cases pin through the command. Then the next edge case of the walk is no finding.

The listing command printed `:270` and `changelog.md:3`, the two sentences above, and `docs/checks/the-pull-request-check.md:137` and `docs/layout/the-pact.md:120`, which state other facts. `frame/design.md:91` says "It reads on where", meaning the hook goes on to search the records. That holds as built, and the snippet leaves it. The docstring at `:57-63` says such a path "prints nothing", which holds. The command searches on words, so it is a sample under contract rules 12 and 19.

```text
seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/changelog.md:3, in place of
"It reads nothing where a link stands anywhere from the root down to the edited file: it checks"
write
"Where a link stands anywhere from the root down to the edited file, it opens no record and prints nothing: it checks"
and leave the rest of the sentence as it stands.

hooks/edit-leaves-copies.py:270, in place of
    # directory it starts at. So the hook reads nothing on such a path.
write
    # directory it starts at. So the hook opens no record on such a path.
```

```seal
verdict: fixed 49f795cc4
answer: I took the snippet's wording with no code change. `changelog.md:3` now opens "Where a link stands anywhere from the root down to the edited file, it opens no record and prints nothing: it checks", and the rest of the sentence stands. The guard's comment, now at `hooks/edit-leaves-copies.py:273`, says the hook "opens no record on such a path". The orchestrator asked the docstring to name the read that stays, and the hook's one clause (`:61-66`) now names two marker reads of `lib/optin.py#marked` outside the guard, each bounded at the marker's length and printed nowhere. One is the root's `README.md` where it is itself a link. The other is the `README.md` beside a directory named `threads` that stands below a link on the path, which `_located` reads on its way up before it meets the link (Probe H). The listing command, run again at `7d11432d0` with `trail/` left out, prints `hooks/edit-leaves-copies.py:273` and `changelog.md:3`, which hold at HEAD, and `docs/checks/the-pull-request-check.md:137` and `docs/layout/the-pact.md:120`, which state other facts. It is a sample.
```

### 2. No case holds the order of the root's link check against the marker read, and the close's reason for planting none rests on a cost that does not stand

```seal
severity: should
location: `tests/hooks/test_edit_leaves_copies.py`, `tests/hooks/test_edit_leaves_copies.py:6-9`, `hooks/edit-leaves-copies.py:113-119`
evidence: executed `bin/seal mutate hooks/edit-leaves-copies.py --tests "bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py"` with `--replace "if os.path.islink(root):" "if optin.marked(root) and os.path.islink(root):"` (survived); executed `bin/test -q -p no:xdist tests/hooks/test_tmp_round4_order.py` at the target (passed) and under the same mutant (red); executed `python3 -I test_tmp_round4_probes.py` against the hooks of `794e4650c` and `fd984795f` (Probe I); read `tests/hooks/test_edit_leaves_copies.py:15-20`, `tests/conftest.py:517-557`, `hooks/edit-leaves-copies.py:99-124`
reopens: round-3#1
```

Why it matters: `5a4547218` changed one behaviour, the order. The root's link check now runs before `optin.marked` opens the root's `README.md`. `changelog.md:3` now states that order to a person: "it checks the root before it opens the root's `README.md`". No case holds it. With the check moved behind the marker read (`if optin.marked(root) and os.path.islink(root):`), the hook's module passes whole. `test_refuses_to_print_where_the_root_threads_or_a_directory_in_the_item_is_a_link` stays green, because the path is still refused. A claim a fix writes into a document closes when a test pins it (`skills/code-review/SKILL.md` *A finding is not closed too early*). A behaviour the diff changed that no case then holds is the *Regression test* row's `should`.

Claimed in round 3's close: "A case that shows the order needs `os.mkfifo`, a writer thread and a skip on Windows, and that costs on every run more than the order protects". That cost belongs to a case run through the hook's command. The module already loads the hook in process (`:20`, `hook = load(TARGET, ...)`). `#_located` takes `optin` as its second argument (`:99`). So a stub whose `marked` records each root it is asked about shows the order with no FIFO, no thread and no subprocess. `tests/conftest.py:517` already gives `symlink_or_skip`, and `:543` gives `fifo_or_skip`, so the skip costs no new code either. Probe I ran that call in 15 microseconds. At `794e4650c` the stub was asked about no root. At `fd984795f` it was asked about `via-root/seal`. The probe case below, run as a file of the clone, passed at the target and was red under the mutant above. So the case is seen red, and the order the close chose not to pin can be pinned for the price of one in-process call. The close weighed a cost that the cheaper form does not have, so the choice does not stand under contract rule 15 or `skills/core/SKILL.md` *The rule a mechanism is kept against*.

The module's docstring says the cases run the hook's command (`:6-9`). The new class calls a unit, so the snippet amends that sentence too. The class is named for the unit, as `tests/lib/test_lines.py:299` names `Test__paragraph_ends_at`, and its case opens with `test_refuses_`, as `seal layout --check` asks. This snippet covers the case and the docstring. `changelog.md:3`'s order clause needs no change once a case holds it.

```python
# tests/hooks/test_edit_leaves_copies.py, the module docstring, in place of
# "The registration is held by `tests/behaviour/test_chain_hooks_hardening.py`.":
# `Test__located` calls `#_located` alone, with a stub of `lib/optin.py`, to
# show the order of its reads. The registration is held by
# `tests/behaviour/test_chain_hooks_hardening.py`.

# the imports:
import json
import types

from conftest import census_case, load, mark_root, symlink_or_skip

# a class after `Test_main`, before `test_census`:
class Test__located:
    def test_refuses_a_root_that_is_a_link_before_it_reads_the_roots_marker(
        self, tmp_path
    ):
        """A10, round 3's finding 1. The root is a link, and `#_located`
        returns None without asking `optin.marked` about it, which would
        open the root's `README.md` through the link. The stub records each
        root it is asked about, so the order shows with no FIFO."""
        real = item(tmp_path / "real", {"frame/design.md": design(AFTER)})
        via_root = tmp_path / "via-root"
        via_root.mkdir()
        # Precondition: a directory link, which Windows makes only with
        # `target_is_directory`; the helper skips where links are not allowed.
        symlink_or_skip(str(real.parent.parent), str(via_root / "seal"), directory=True)
        asked = []
        optin = types.SimpleNamespace(
            WORK_ITEMS="threads", marked=lambda root: asked.append(root) or True
        )
        path = via_root / "seal" / "threads" / ITEM / "frame" / "design.md"
        assert hook._located(str(path), optin) is None
        assert asked == []
```

```seal
verdict: fixed 7d11432d0
answer: I applied the snippet's class, imports and module docstring sentence, with one addition. `seal layout --check` refused a class with no `test_accepts_` case, so `Test__located` also holds `test_accepts_a_root_that_is_no_link_once_it_reads_the_roots_marker`. In that case the root is a directory, the stub is asked about it once, and `#_located` returns the item and the record's path. It is also the control that shows the stub is consulted at all. The class docstring says the pair differ by whether the root is a link. `seal layout --check` and `seal layout --pairs` pass on the module. Seen red: after the commit, `seal mutate` with `-k Test__located` was red for the order-swapped mutant (`if optin.marked(root) and os.path.islink(root):`) and for the check removed. Under the swap, the accepting case's path is the same as before, so the red is the refusing case's `asked == []`. The close of round 3 weighed only the cost of a FIFO case run through the hook's command. The in-process form has no such cost, so round 3's ground is withdrawn and the order is now pinned.
```

### 3. The link cases call `symlink_to` bare, where every other test module uses `symlink_or_skip`, so a Windows machine without the link privilege turns them into errors for code nobody touched

```seal
severity: should
location: `tests/hooks/test_edit_leaves_copies.py:311`, `tests/hooks/test_edit_leaves_copies.py:330`, `tests/hooks/test_edit_leaves_copies.py:350`, `tests/hooks/test_edit_leaves_copies.py:367`, `tests/hooks/test_edit_leaves_copies.py:370`, `tests/hooks/test_edit_leaves_copies.py:372`
evidence: executed `git grep -c -E "\.symlink_to\(|os\.symlink\(" -- tests ':!tests/conftest.py'` (prints this module alone, 6); executed `git grep -c symlink_or_skip -- tests` (13 modules beside `tests/conftest.py`); executed `git log --format="%h %s" -S symlink_to -- tests/hooks/test_edit_leaves_copies.py` (prints `fd984795f` and `4be875457`); read `tests/conftest.py:517-540`
regression: round-2#1
```

Why it matters: this is outside the fix diff. This round opened the module to judge finding 2, and reports what it found there. `tests/conftest.py:517-540` states the rule. A Windows machine needs a privilege to make a link. A bare `os.symlink` "turns a missing privilege into a red suite for code nobody touched", and `symlink_or_skip` skips there instead. Every other test module that makes a link uses the helper. This module makes six links bare. Five came with `fd984795f`, round 2's fix of finding 1 (`:330`, `:350`, `:367`, `:370`, `:372`). The sixth, `:311`, came with `4be875457`, round 1's fix of finding 3. The frame says the cases are seen red (`frame/design.md` *Scope* item 11), and says nothing of how a link is made. So the defect came from the fix passes, which wrote the links without the repository's helper.

Four of the six targets are directories (`:350`, `:367`, `:370`, `:372`). `Path.symlink_to` without `target_is_directory` makes a file link on Windows. Those four cases print nothing there whatever the guard does, because nothing resolves through such a link. The helper's `directory=True` makes the link the case means. Round 2's close is not reopened by this: the guard holds, and its cases pin it on POSIX (round 3's confirmation of round-2#1).

```python
# tests/hooks/test_edit_leaves_copies.py, the import:
from conftest import census_case, load, mark_root, symlink_or_skip

# :311
        symlink_or_skip(str(outside), str(directory / "leak.md"))
# :330
        symlink_or_skip(str(outside), str(directory / "frame" / "design.md"))
# :350
        symlink_or_skip(str(outside), str(home / "threads" / ITEM), directory=True)
# :367
        symlink_or_skip(str(real.parent.parent), str(via_root / "seal"), directory=True)
# :370
        symlink_or_skip(str(real.parent), str(via_threads / "threads"), directory=True)
# :372
        symlink_or_skip(str(real / "frame"), str(via_frame / "frame"), directory=True)
```

```seal
verdict: fixed 7d11432d0
answer: I applied all six lines as the snippet gives them, with the import. The four directory links pass `directory=True`, and the new `Test__located` refusing case uses the helper the same way. The listing command `git grep -c -E "\.symlink_to\(|os\.symlink\(" -- tests ':!tests/conftest.py'`, run again at `7d11432d0`, prints nothing and exits 1, so no test module makes a link bare. No new case is owed. The six cases assert what they asserted before, and `bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py` passed 25 on POSIX. The skip path on Windows without the link privilege was not run here: that is the orchestrator's broad gate, or a Windows runner.
```

## Confirmations

What matched: the root case of round 3's finding 1, though the finding is reopened above for the case it left. The crafter's FIFO probe, `test_tmp_root_link_fifo.py` under the fix pass's scratch directory, was run again. Against the hook at `794e4650c` the root's FIFO `README.md` was not opened. Against the hook at `fd984795f` it was. Both exited 0 with nothing on stdout (executed). So the close's account of that probe is true.

What matched: the close's three mutants. Run again as one `seal mutate` batch on the module, the new `islink(root)` check off, the guard in `#main` off, and `threads/` dropped from `on_path` were each red at exit 1 (executed). `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` passed 46 (executed). The walk change loses nothing: a link root met at an inner `threads` returns None where the old walk went on up, and a path that reaches a marked root above holds that link under the item, which the guard refuses anyway (read, `:108-124`, as round 3 argued).

What matched: the docstring's new clause at `:61-63`, that a root `README.md` which is itself a link stands outside the guard, states what is built (read). The caller sends that case to its own issue.

What matched: `pr.md`'s three quotes. `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` exited 0 with a `wrote:` line and no note (executed). `uvx ruff check` and `uvx ruff format --check` on `hooks/edit-leaves-copies.py` alone passed (executed).

What matched: the records read whole. Apart from finding 1's clause, `changelog.md:3` states what `5a4547218` built. `frame/design.md:91` and `:133` stand as round 3 reads them. The timings at `frame/plan.md:26` and `frame/questions.md:14` are dated to `5604aa15d`. `gaps.md`'s open rows name the orchestrator's broad gate. Nothing else in the files read whole is contradicted by the target (read).

Probe I also showed a second form of the nested walk, with a stub whose `marked` answers true. Where the inner `sub/README.md` behind the link opens with the marker, `#_located` takes `sub` as the root, and the guard checks from there down. `frame/design.md:91` names `<root>` as a directory whose `README.md` opens with the marker, and the link then stands above that root. Such a layout needs a second marked root already standing at the link's target, and the `Edit` call reaches the same files through the same link. This round reads it as outside the frame's condition and opens no finding for it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's narrow set, 1126 passed and 9 skipped, which `boundary.txt` under the fix pass's scratch directory shows (read). This round ran the two modules named above, not that set. The suite beyond them, the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |
| A Windows run of the link cases, with and without the link privilege, which finding 3's grounds read from `tests/conftest.py:517-540` and did not run | `tests/hooks/test_edit_leaves_copies.py:304-378` | the orchestrator's broad run on the workflow's `windows-latest` rows |
| A root `README.md` that is itself a link, read by `lib/optin.py#_first_line` for every hook | `lib/optin.py:237-272` | the orchestrator, as the separate issue its spawn prompt names, with `lib/routing.py#read_declaration` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_round4_probes.py <clone>/hooks/edit-leaves-copies.py <scratch>/p-head head`, the file under this round's scratch directory (Probes H and I) | H: exit 0, stdout empty, the FIFO `sub/README.md` behind the item's link opened. I: `_located` returned None, and the stub's `marked` was asked about no root, in 0.000015 s |
| The same, against `fd984795f`'s hook written to `<scratch>/old/hooks/` | H: the FIFO opened. I: `_located` returned the item, and `marked` was asked about `via-root/seal` |
| The same, against the clone's hook with each component checked for a link on the walk up, and the guard in `#main` taken out; `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` on that hook; the file restored with `git checkout` | H: the FIFO still opened; 46 passed |
| `python3 -I test_tmp_root_link_fifo.py`, the crafter's probe under the fix pass's scratch directory, against the hooks of `794e4650c` and `fd984795f` | `794e4650c`: the root's FIFO not opened; `fd984795f`: opened; both exit 0, stdout empty |
| `bin/seal mutate hooks/edit-leaves-copies.py --tests "bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py"` with four `--replace` pairs: `if os.path.islink(root):` to `if optin.marked(root) and os.path.islink(root):`, the same to `if False:`, the guard's `if any(...)` to `if False:`, and `on_path = [os.path.dirname(item)]` to `on_path = []` | baseline passed; the order mutant survived; the other three red at exit 1 |
| `bin/test -q -p no:xdist tests/hooks/test_tmp_round4_order.py` in the clone, at the target and under the order mutant through `seal mutate` | passed at the target; red under the mutant, `asked` holding the linked root |
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` at the target | 46 passed |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` | exit 0, `wrote:` line, no note |
| `uvx ruff check hooks/edit-leaves-copies.py`; `uvx ruff format --check hooks/edit-leaves-copies.py` | both exit 0 |
