# Review round 2: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: 7fa4a1692, fixes 018b9dac4..7fa4a1692
```

This is the verifying round. The fix diff is `018b9dac4..7fa4a1692`, read in a `git clone --no-local` checked out at `7fa4a1692` under this round's scratch directory. The code it reviews is the fix diff: `hooks/edit-leaves-copies.py#_widened`, the link skip in `#_records`, the open in `#main` that replaced the `isfile` check, the rewritten docstring and comment, and the four new cases in `tests/hooks/test_edit_leaves_copies.py`. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `hooks/edit-leaves-copies.py` and `tests/hooks/test_edit_leaves_copies.py`. No `pr.<lang>.md` stands, and `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared, and `seal/config.json` has no `Pact` key.

Carried from round 1 rather than established again: `trail/phases/phase-1.md` and `trail/phases/phase-2.md`, which the fix diff does not change (`git diff --stat 018b9dac4 7fa4a1692` names neither); Probe B's counts over the transcripts, which `frame/plan.md:26` cites; and the coordinates `SECURITY.md:43-46` and `:55` for the boundary a hook acting on a checked-out repository crosses. `hooks/` and `lib/` are unchanged from `3d4a8810e` and from `5604aa15d` to the target (`git diff --stat` printed nothing for each).

This round's own axes, beside the table's: every call in the hook that follows a link, whether `_widened` reads the neighbours of the edit's own place, and whether each record's statement of what Q1 measured holds after the fold at `0aa11aec5`.

## Findings

### 1. The hook still follows a link at the edited file and at the work item's directory, so it reads files outside the repository that the close says it does not read

```seal
severity: should
location: `hooks/edit-leaves-copies.py:254-259`, `hooks/edit-leaves-copies.py:57-59`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/changelog.md:3`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:91`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:133`, `tests/hooks/test_edit_leaves_copies.py`
evidence: executed `python3 -I test_tmp_round2_probes.py <clone> <transcripts> <scratch>` (Probes D and E, `## Probes`); executed `git grep -n -E "is a link|that is a link|a link\b|outside the item's directory|file outside the|outside the repository" -- hooks tests/hooks seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix README.md README.ko.md CONTRIBUTING.md SECURITY.md docs`; read `hooks/edit-leaves-copies.py:126-139`, `:236-259`
reopens: round-1#3
```

Why it matters: round 1's finding 3 said the hook opens a record that is a link, so a checked-out repository can make it read a file outside the repository. The close at `4be875457` fixed one of the three places where the hook follows a link. Claimed in the close: "`#_records` skips a name that `os.path.islink` reads as a link". That holds for the names `os.walk` lists under the item (`hooks/edit-leaves-copies.py:135`), and this round's mutant of that line was red. Two other places still follow a link, and the class was not enumerated:

- `#main` opens the edited file at `:257` with `open`, which follows a link at the file and at every directory over it. The same commit wrote that open in place of the `isfile` check.
- `#_records` starts `os.walk` at the item's directory (`:131`). `os.walk` follows a link at the directory it starts from, though it follows none below it.

Probe D1 made the item's `frame/design.md` a link to a file outside the scratch repository, and ran the hook on an `Edit` whose `old_string`, `finds every`, is too short to make a span alone. The hook named `gaps.md` line 3 with `next round finds every copy it left.`. Only the outside file's words can make that span, so the hook read the outside file. Probe D2 made the item's directory a link to a directory outside the repository. The hook named `deep/er/notes.md` line 3, a file that exists only behind the link. So the hook walks whatever tree such a link names and reads every `.md` file in it on each `Edit`. For a link to a home directory, that walk can run until the harness stops the hook. What it prints is the path and line of each outside file that holds the replaced words.

Three sentences at the target are false under D1 and D2:

- The docstring at `:57-59` says "A `.md` name in the work item that is a link is no record and is not read". Under D1 the edited name is such a link, and it is read.
- `changelog.md:3` says the hook "reads no record that is a link". D1 contradicts it.
- The `## Rule changes` row at `frame/design.md:133` says the hook reads "no file outside the item's directory". D1 and D2 both contradict it.

The listing command above printed those three places, along with `:128`, `frame/design.md:91` and the case docstring at `tests/hooks/test_edit_leaves_copies.py:305`, which stay true. The rest of its output is `CONTRIBUTING.md:485` and `docs/running/the-run.md:49` and `:64`, which state other facts. The command searches on words, so it is a sample under contract rules 12 and 19. The list of places that follow a link was built from the hook's own calls that resolve a path: `open` at `:190` and `:257`, `os.walk` at `:131`, and `optin.marked` in `#_located`. `optin.marked` reads only the root's `README.md`, and that read is bounded (`lib/optin.py:256-272`).

The close also dropped round 1's `or not os.path.isfile(full)`, on the ground that git commits no FIFO (a named pipe). That ground holds for a checkout, the boundary `SECURITY.md:43-46` names: git stores regular files, links and submodules, and nothing else. So the guard is not owed. The close's second ground does not hold. It says no case could show the guard red without a read that never ends. Probe E2 opened a writer on a `.md` FIFO in the item, and the hook at the target read it and named `pipe.md`, which is a red that ends. With no writer (E1), the hook was still running after 5 s.

The snippet covers the code. Precondition: `os.path.islink` reads each name itself and follows no link. The names above `threads/` are not checked, meaning the marked root and every directory over it, so a repository reached through a link, such as macOS `/tmp`, still reads. Python's `os.path.islink` does not report a Windows junction, so a junction at the item stays followed; this is where the snippet stops. The fix pass also owes three more things. The docstring at `:57-59` is rewritten as below. In `changelog.md:3`, "and reads no record that is a link" becomes "and follows no link from the root's `threads/` down to the edited file, and reads no record that is a link". Two cases go in `tests/hooks/test_edit_leaves_copies.py`, D1 and D2 as the probe built them, each printing nothing and each seen red against the target. The reads-on condition in the first bullet at `frame/design.md:91` is the orchestrator's fold. Once the code holds, the row at `:133` holds too.

```python
# In `main`, after `item, rel = located` and before the open:
    # A link from `threads/` down to the edited file, the work item's
    # directory and the edited file among them, can name a file or a
    # directory outside the repository: `open` follows it, and `os.walk`
    # follows the directory it starts at. So the hook reads nothing there.
    parts = rel.split("/")
    under = [os.path.join(item, *parts[:n]) for n in range(len(parts) + 1)]
    if any(os.path.islink(p) for p in [os.path.dirname(item), *under]):
        return
```

```text
The docstring, in place of the sentence at lines 57 to 59:
An edited path with a link anywhere from the root's `threads/` down to the
file, the work item's directory and the file itself among them, prints
nothing, and a `.md` name in the work item that is a link is no record and
is not read: a link can name a file or a directory outside the repository,
or a device whose read never ends.
```

```seal
verdict: fixed fd984795f
answer: The reads-on condition is the framer's fold at `f865cab26`, `frame/design.md:91`: no component of the path from `<root>` down to `<file>`, `<root>` itself among them, is a link. `fd984795f` builds it as one guard in `#main`, before the first open. The guard checks the root, its `threads/`, the item's directory and each component under it down to the edited file with `os.path.islink`, and returns where any is a link. The snippet started at `threads/` and so left the root out, which the fold names. The `#_records` skip stays for a link inside the item. Three cases were each seen red against the hook as it stood at `7fa4a1692`, which `git diff --stat 7fa4a1692 f865cab26 -- hooks lib tests` shows unchanged, and each printed a place where the case asserts nothing. `test_refuses_to_print_where_the_edited_file_is_a_link` is Probe D1. `test_refuses_to_print_where_the_work_items_directory_is_a_link` is Probe D2. `test_refuses_to_print_where_the_root_threads_or_a_directory_in_the_item_is_a_link` holds the other three components. After the commit, `seal mutate` gave 6 mutants, all red: the guard off, the root dropped, `threads/` dropped, the file dropped, the item's directory dropped, and the directories inside the item dropped. The docstring at `:57-61` and `changelog.md:3` now state the guard. On round 1's FIFO close, I rewrote the ground to its first one alone and added no `isfile` guard. Round 1's close gave two grounds. The first holds: git stores regular files, links and submodules and nothing else, so a checkout, the boundary `SECURITY.md:43-46` names, cannot hold a FIFO. The second, that no case could show the guard red without a read that never ends, is false, since Probe E2 shows a red that ends. I did not take the guard because a check against a file git cannot deliver has nothing to catch, and its case would need `os.mkfifo` and a writer thread, which Windows lacks (`skills/core/SKILL.md` *The rule a mechanism is kept against*). The listing command, run again at `fd984795f` with `trail/` left out, prints the hook's docstring at `:59`, its `#_records` docstring at `:130`, the guard's comment at `:258`, `changelog.md:3`, `frame/design.md:91` and `:133`, and the case docstrings at `tests/hooks/test_edit_leaves_copies.py:305`, `:316` and `:336`. Each holds at HEAD. It also prints `frame/design.md:27` and `frame/plan.md:67`, which are dated to the commits they record, and `CONTRIBUTING.md:485` and `docs/running/the-run.md:49` and `:64`, which state other facts. It is a sample.
```

### 2. `frame/plan.md:26` says Q1 found the hook's own text in the main session, while Q1's Status cell at the target also records it inside a plugin's subagent

```seal
severity: should
location: `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:26`
evidence: executed `git grep -n -E "fixed text|own text|its text delivered|inside a subagent|inside a plugin's subagent" -- seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'` (prints `frame/plan.md:26`, `frame/questions.md:14`, `gaps.md:10`, `gaps.md:11`); executed `git show 0aa11aec5 --word-diff=plain`; read `frame/questions.md:14`
```

Why it matters: this is the defect the work item exists to stop, one fact restated in two records with one copy left behind. Claimed at `frame/plan.md:26`: "`frame/questions.md` Q1's measurement found a plugin hook's fixed text delivered in the main session and inside a plugin's subagent, and this hook's own text in the main session". The contrast within that sentence tells a reader that the hook's own text was not measured inside a subagent. The fold at `0aa11aec5` added a fourth session to Q1's Status cell (`frame/questions.md:14`). In that session the hook, as it stands at `5604aa15d`, named `pr.md` line 1 to a plugin agent that made the edit. The same fold edited the row at `frame/plan.md:26` to add the timing, and left this sentence as it stood. `7fa4a1692` then closed the `gaps.md` row on the subagent half on the strength of that fourth session. So the plan's row is the one record that still says the subagent half is unmeasured. A sealer reading it against acceptance row A11 meets two answers.

The listing command printed four places. `frame/questions.md:14` is the home. `gaps.md:10` and `:11` each cite it and agree with it. `frame/plan.md:26` is the drifted copy. The command searches on words, so it is a sample under contract rules 12 and 19. By `docs/forms/the-round-record.md` *The round record*, a drifted copy is answered by removing the copy and citing the home, so the snippet cites Q1 and does not restate it. The row is the frame's, so this is the orchestrator's fold.

```markdown
frame/plan.md, the row at line 26, in place of the sentence opening "`frame/questions.md` Q1's measurement found":
`frame/questions.md` Q1, its Status cell, records where the harness delivered a plugin hook's text and this hook's own text
```

```seal
verdict: fixed f865cab26
answer: The framer's fold at `f865cab26` replaced the sentence at `frame/plan.md:26` with the snippet's citation of Q1's Status cell, so the row no longer restates what Q1 measured. The fix pass made no change for this finding. The listing command, run again at `fd984795f`, prints `frame/plan.md:26`, which now cites the home; `frame/questions.md:14`, the home; and `gaps.md:10` and `:11`, which each cite it and agree with it.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `gaps.md:10` now closes the row on the main session, citing Q1's third session. `gaps.md:11`, opened by `f1fd9f345` and closed by `7fa4a1692`, cites the fourth session, and Q1's Status cell (`frame/questions.md:14`) records both. The plan half held at `17003563a`, when Q1 recorded three sessions. It drifted only at the later fold, `0aa11aec5`, which is finding 2 and not this close. Read at the target, and the listing command was run again (finding 2's `evidence:` line). The fourth session's evidence under the session scratchpad's `release-0.39.0/q1-sub/` was read. Its plugin's `hooks/edit-leaves-copies.py` is byte for byte the target's (`cmp`), and its `PostToolUse` entry is the target's. Its `run.out` holds the main session relaying the subagent's report of the hook's note, which names `pr.md` line 1 with three spans. That session is the orchestrator's executed claim; this round started none (`## Not judged`).

```seal
confirms: round-1#2
```
What holds: `#_widened` (`hooks/edit-leaves-copies.py:142-162`) takes the three words on each side from the edited file around the first place `new_string` stands. It falls back to `old_string` alone where `new_string` is empty or absent, and `#main` feeds it the file it opens (`:257-259`). The docstring at `:23-36`, the comment at `:72-73`, `frame/design.md:92` and `changelog.md:3` each state that reading. Executed: a `seal mutate` batch of five mutants over the link skip, both edge joins, the `if new else -1` guard and the widening call in `#main` was all red. With the widening removed, the hook reads `old_string` alone, so that mutant is the close's "seen red against the hook that read `old_string` alone". `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` passed 43.

What matched: the crafter dropped the snippet's `middle[:1].strip()` and `middle[-1:].strip()`, and this round's reading agrees that dropping them changes no span. Where the joined string opens or ends with whitespace, `_spans` splits it again at that whitespace, so the words come out as they did without the join. Where the string is empty, joining the word before it to the word after it rebuilds the one word the old text held there. So the two mutants that survived were equivalent mutants, and the crafter's account of them holds.

What matched: the caller's second doubt. A repeated `new_string` makes `_widened` read another place's neighbours, and the frame states that limit in three places: `frame/design.md:92`, the docstring at `:32-35`, and the failure scenario of `frame/plan.md:26` ("an edit whose `new_string` stands earlier in the file"). Probe C rebuilt each `Edit` of a work item record from the `originalFile` its transcript result holds. That came to 425 edits that change words, a sample of round 1's 2,178, since only those results carry the file. In 1 of the 422 edits with a non-empty `new_string`, `new_string` first stands earlier than the edit's place, inside another word. There the widened spans lose a span that both the right place and `old_string` alone would have kept. The frame's sentence, that such a span "matches nothing or a place that holds those words", covers that loss, so there is no finding. A reader of the frame does not learn that this case can do worse than `old_string` alone. At 1 in 422, this round judges the gap too small to owe a sentence.

What matched: Q1's timing. Probe F ran the hook's script ten times on an edit payload of this item's `frame/design.md` at the target: 0.030 to 0.038 s a run, against 0.017 s for an interpreter that does nothing. The orchestrator's range of 0.032 to 0.042 s (`frame/questions.md:14`, `frame/plan.md:26`) is of the same order. Its own runs have no file under `q1-sub/`, so the range itself was not re-run.

What matched: `pr.md`'s three quotes. `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch file>` exited 0 with a `wrote:` line and no note, so each quote stands at its file (executed). Line 2's coordinate, the head of Q1's Status cell, still reads as quoted after the fold (read).

What matched: `frame/design.md:91-92` and *Scope* items 9 and 11, A13, the `## Rule changes` add row and `frame/plan.md:27` each state what `#_widened` and the link skip do, apart from what finding 1 names. `frame/plan.md:67` records the fold's routing of round 1's findings, and the fold followed it.

The four new cases each cover a path the group did not: an `old_string` that ends at the change, an edge that cuts a word on either side, the deletion fallback, and a link among the records. No case duplicates another in `Test_main`. No case puts a link at the edited file or at the item's directory (finding 1). No case holds a `new_string` that stands earlier in the file; that is a limit the frame states, and no *Scope* item or acceptance row asks a case to hold it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether Claude Code's `Edit` succeeds on a path that passes through a link and then runs `PostToolUse` with that path. The hook reads whatever payload arrives, so finding 1 stands either way. Contract rule 6 withholds starting a session | finding 1 | the orchestrator, should it want the harness side measured |
| The fourth `claude -p` session in Q1's Status cell, beyond its saved `run.out` and the plugin files compared here: this round started no session | `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/questions.md:14` | the orchestrator, and the sealer at its audit |
| The crafter's `bin/test -q tests/text tests/behaviour tests/hooks tests/skills/test_seal_stamp.py`, 1123 passed and 9 skipped, and its 9 mutants: this round ran the two modules and the five mutants named above, not those. The suite beyond them, the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_round2_probes.py <clone> <transcripts> <scratch>`, the file under this round's scratch directory; `<transcripts>` is this repository's directory under `~/.claude/projects/` | Probe C: 425 `Edit` results of a work item record outside `trail/` and `guarantee.md` that carry `originalFile`, apart from 2 that change only whitespace; none `replace_all`, none with an `old_string` that is not unique, 3 deletions, 421 whose `new_string` first stands at the edit's own place, and 1 where it first stands earlier, inside a word. That one loses a span that the right place and `old_string` alone each keep. Probe D1: the edited `frame/design.md` a link to a file outside the scratch repository; exit 0, and the hook named `gaps.md` line 3, `next round finds every copy it left.`. Probe D2: the item's directory a link to a directory outside; exit 0, and the hook named `deep/er/notes.md` line 3. Probe E1: a `.md` FIFO in the item with no writer; the hook was still running after 5 s and `subprocess.run` killed it. Probe E2: the same FIFO with a writer; exit 0, and the hook named `pipe.md`. Probe F: ten runs on an edit of this item's `frame/design.md`, 0.030 to 0.038 s; `python3 -I -c pass` 0.017 s |
| `bin/seal mutate hooks/edit-leaves-copies.py --tests "bin/test -q -x tests/hooks/test_edit_leaves_copies.py"` with five `--replace` pairs: the link skip, the head join and the tail join each to `if False:`, `if new else -1` removed, and the widening call in `#main` replaced by `f.read()` | baseline passed; 5 mutants, 5 red, each at exit 2, which is pytest's `-x` stop. The link skip and the head join were run again without `-x`, and each was red at exit 1 |
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` | 43 passed |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch file>` | exit 0, `wrote:` line, no note |
