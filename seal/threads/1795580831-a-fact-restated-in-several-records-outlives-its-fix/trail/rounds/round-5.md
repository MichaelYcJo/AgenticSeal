# Review round 5: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: 15fd04b81, fixes 794e4650c..15fd04b81
```

This is the verifying round. The fix diff is `794e4650c..15fd04b81`, read in a `git clone --no-local` checked out at `15fd04b81` under this round's scratch directory. It holds the wording fix at `49f795cc4` (`hooks/edit-leaves-copies.py`, the docstring at `:61-66` and the guard's comment at `:273`, and `changelog.md:3`), the test fix at `7d11432d0` (`Test__located` and the six link calls in `tests/hooks/test_edit_leaves_copies.py`), its removal at `d03b194f5` and restoration at `00908b8da`, round 4's close blocks at `9a0f0a45b`, the fold at `58ecf9f95` (`frame/design.md:91` and `:133`, and the first row of `frame/plan.md` *Judgments of the run*), and `seal/follow-up.md:45` at `15fd04b81`. The code this round reviews is the docstring clause, the comment and `Test__located`. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, `trail/rounds/round-3.md`, `trail/rounds/round-4.md`, `hooks/edit-leaves-copies.py` and `seal/follow-up.md`'s row for #1612. Rounds 1 and 2 were read for their headings and closes. No `pr.<lang>.md` stands, and `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared, and `seal/config.json` has no `Pact` key.

Carried from rounds 1 to 4 rather than established again: Probes H and I of round 4, the FIFO read under a linked item and the in-process stub call, which this round did not run again; the boundary at `SECURITY.md:43-46`; and round 2's list of the hook's calls that resolve a path. Round 4's second form of Probe I, an inner `README.md` behind a link that opens with the marker, is a further edge of links inside the limit the repository owner set on 2026-11-25 (`frame/design.md:91`, `frame/plan.md:67`), so this round opens no finding for it.

The caller's scope: the hook's link handling is closed at that limit. A further edge of links within it is no finding, and a statement that contradicts it is one. This round's own axes, beside the table's, are each statement of the limit against the code and against the others, the frame's sentences that the fold and the follow-up row left behind, and each case of `Test__located` against the mutant it claims.

## Findings

### 1. The hook's docstring says the two marker reads outside the guard are bounded at the marker's length, where the code, `lib/optin.py` and three frame statements of the limit bound them at the marker's length plus two characters

```seal
severity: should
location: `hooks/edit-leaves-copies.py:61-67`
evidence: executed `git grep -n -o -E ".{0,40}(bounded at|marker's length).{0,50}" -- hooks lib seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'`; read `hooks/edit-leaves-copies.py:61-67`, `lib/optin.py:236-244`, `lib/optin.py:256-262`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:91`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:133`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:67`
regression: round-4#1
```

Why it matters: the unit is the docstring clause `49f795cc4` added at `:61-66`, which names the reads outside the link guard. The frame states the limit as two marker reads "bounded at the marker's length plus two characters" (`frame/design.md:91`, and the same words at `:133` and `frame/plan.md:67`). Round 4's finding 1 asked only for the changelog line and the comment. The orchestrator asked the fix pass to name the read that stays in the docstring, and the fix pass wrote the bound without its two characters. So the defect came from the fix pass's restatement of a fact the frame already held.

`lib/optin.py:243` reads `f.readline(len(MARKER) + 2)`. Its docstrings at `:238-239` and `:260-261` say "bounded at the marker's length and the two characters a line end can take". The hook's docstring at `:62-63` says "bounded at the marker's length and printed nowhere". That states the limit differently from the code and from each other statement of it. The docstring is the place `skills/core/SKILL.md` *The first value* gives a hook's edge cases, so a person who reads the limit there reads a wrong bound. It is also one instance of the defect this work item exists for: one fact in four places, and one of them drifted at the fix that wrote it.

The listing command printed `hooks/edit-leaves-copies.py:62-63`, the wrong statement; `lib/optin.py:238` and `:260`, whose sentences go on to the two characters; and `frame/design.md:91`, `:133` and `frame/plan.md:67`, which hold. Round 4's close of finding 1 repeats the short bound, but it is a record of what the fix pass did, under `trail/`, which the command leaves out. The command searches on words, so it is a sample under contract rules 12 and 19. The snippet covers the one place that is wrong.

```python
# hooks/edit-leaves-copies.py, the module docstring, in place of lines 61 to 67:
the repository, or a device whose read never ends. Two reads stand outside
that guard, each the marker read of `lib/optin.py#marked`, bounded at the
marker's length and the two characters a line end can take, and printed
nowhere: the root's `README.md` where it is itself a link, as every hook
and gated command reads it, and the `README.md` beside a directory named
`threads` that stands below a link on the path, which `_located` reads on
its way up before it meets the link. The hook writes nothing, starts no
process and reaches no network. Its command
```

```seal
verdict: fixed 10635995c
answer: `10635995c` applies the snippet. The docstring at `hooks/edit-leaves-copies.py:61-70` now bounds the two marker reads "at the marker's length and the two characters a line end can take", as `lib/optin.py:238-239` and `:260-261` state it. The remaining lines of the paragraph are rewrapped so no line runs past the others. `uvx ruff check hooks` is clean. `bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py tests/test_censuses.py` exited 0. The listing command, run again at `10635995c` with `trail/` left out, prints the hook's `:62-63`, which now hold; `lib/optin.py:238` and `:260`; and `frame/design.md:91`, `:133` and `frame/plan.md:67`, which hold. It is a sample.
```

### 2. `frame/questions.md` Q2 says a lower count leaves the three mechanisms as built, while the follow-up row `15fd04b81` rewrote sends a mechanism to the weighing even where the count fell

```seal
severity: should
location: `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/questions.md:15`, `seal/follow-up.md:45`
evidence: executed `git grep -n -o -E ".{0,60}(hold as built|even where the count fell|what it named against what was|As many or more).{0,60}" -- seal/follow-up.md seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'`; read `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/questions.md:15`, `seal/follow-up.md:45`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:13`
```

Why it matters: `frame/questions.md:15`, the *Options & what each implies* cell of Q2, says: "Fewer: the quote check, the listing command and the hook hold as built." At `15fd04b81` the follow-up row, the place the question waits for the owner, says instead: "A mechanism whose notes or refusals were mostly ignored or false, or that caught nothing in the release, goes to the same weighing even where the count fell." The two now give different outcomes for the same answer. The settle and the owner read both. The frame's cell is the copy, since `seal/follow-up.md` outlives the work item's directory, and `docs/forms/the-round-record.md` *The round record* answers a drifted copy by removing it and citing the home (`frame/design.md` G3).

This finding takes neither a `regression:` nor a `reopens:` line. The unit it stands on, the follow-up row, was changed by the orchestrator's records commit and not by a fix pass, and no earlier finding named it.

The listing command printed `seal/follow-up.md:44`, #1613's row, which states another fact; `seal/follow-up.md:45`, the home; and `frame/questions.md:15`, twice, the Options cell. `frame/plan.md:13` names "the follow-up row of `frame/questions.md` Q2, which weighs what the hook named against what was rewritten". That cites the row and agrees with its new clause on whether the agent's next `Edit` changed a named place, so the snippet leaves it. The command searches on words, so it is a sample under contract rules 12 and 19. The snippet changes only the Options cell. Q2's *Default until answered* cell, which `pr.md:3` quotes, stays as it is.

```text
seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/questions.md:15,
the Options & what each implies cell of Q2, in place of
"Fewer: the quote check, the listing command and the hook hold as built. As many or more: the settle after that release weighs the quote check, the listing command and the hook against what they cost, under `skills/core/SKILL.md` *The rule a mechanism is kept against*, the hook by what it named against what was then rewritten"
write
"Fewer, or as many or more: `seal/follow-up.md`, the row #1612 sent there, says what the count and each mechanism's own record in that release send to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*"
```

```seal
verdict: fixed 1dd2f85f2
answer: The orchestrator's fold at `1dd2f85f2` rewrote Q2's *Options & what each implies* cell at `frame/questions.md:15`. It now reads "What each answer sends to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*, the count and each mechanism's own record together, is #1612's row of `seal/follow-up.md`". So the cell cites the home and no longer restates what a lower count does. The fix pass made no change for this finding. The listing command, run again at `10635995c` with `trail/` left out, prints `seal/follow-up.md:44`, #1613's row, which states another fact, and `seal/follow-up.md:45`, the home. It no longer prints `frame/questions.md:15`. It is a sample.
```

### 3. The older row of *Judgments of the run* still sends `lib/routing.py#read_declaration` to an issue of its own, while the row the fold added says it gets no issue in this release, and no issue holds either link case

```seal
severity: should
location: `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:68`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:67`
evidence: executed `git grep -n -E "read_declaration|#_paragraph|issue of its own|get no issue" -- seal ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'`, which prints, for this work item, `frame/plan.md:67` and `:68` alone; executed `gh issue list -R MichaelYcJo/AgenticSeal --state all --search "read_declaration"` (empty) and `gh issue list -R MichaelYcJo/AgenticSeal --state all --search "ask-under-automation link"` (no issue on the case); read `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:67-68`
```

Why it matters: the row `58ecf9f95` added at `frame/plan.md:67` closes with the owner's decision: "A root `README.md` that is itself a link, and `lib/routing.py#read_declaration`, are `lib/`'s and get no issue in this release". The older row at `:68` still ends: "The same class outside the diff, `lib/routing.py#read_declaration` and `hooks/ask-under-automation.py#_paragraph`, which round 1 named, goes to an issue of its own". This is the statement the caller's scope names, one that contradicts the limit. The two rows give two homes for `read_declaration`. The newer row says nothing of `hooks/ask-under-automation.py#_paragraph`, so the older row's issue is the only home it has, and no such issue exists. The template gives *Judgments of the run* "a leftover's home" (`templates/records/sdd-plan.md:35`). The sealer and the settle read each row for it, and `skills/core/SKILL.md` *The rule a mechanism is kept against* has a change rewrite the text it amends in place.

This finding takes neither a `regression:` nor a `reopens:` line. The unit is the fold's row, written by the orchestrator, and no earlier finding named it.

The listing command printed `:67` and `:68` alone in this item's records outside `trail/`. Round 3's and round 4's *Not judged* rows also name the separate issue, but they record where each round sent the question, under `trail/`. The command searches on words, so it is a sample under contract rules 12 and 19. The snippet rewrites `:68`'s last sentence. The home of `hooks/ask-under-automation.py#_paragraph` is the orchestrator's or the owner's to name, and the snippet marks where it goes.

```text
seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:68,
the Judgment cell, in place of
"The same class outside the diff, `lib/routing.py#read_declaration` and `hooks/ask-under-automation.py#_paragraph`, which round 1 named, goes to an issue of its own"
write
"The same class outside the diff, which round 1 named: `lib/routing.py#read_declaration` is decided in the row on the hook's handling of links, and `hooks/ask-under-automation.py#_paragraph` goes to HOME NOT IN TREE"
where HOME NOT IN TREE is the issue the orchestrator opens for it, or the newer row's decision
once the owner extends it to `_paragraph`, and the words stand in no tree until then.
```

```seal
verdict: fixed 1dd2f85f2
answer: The orchestrator's fold at `1dd2f85f2` rewrote the older row's last sentence at `frame/plan.md:68`. `lib/routing.py#read_declaration` is now decided in the row on the hook's handling of links, `:67`, so the plan gives it one home. The row places `hooks/ask-under-automation.py#_paragraph` outside the class, because it opens `docs/running/the-run.md` under `CLAUDE_PLUGIN_ROOT`, the plugin's own copy, and no file of the repository being checked. That needs no issue, so the snippet's placeholder home is not used. The fix pass made no change for this finding. The listing command, run again at `10635995c`, prints `frame/plan.md:67` and `:68` alone in this work item's records outside `trail/`, and they now agree. It also prints the other work items' records under `seal/threads/`, which state their own facts. It is a sample.
```

## Confirmations

```seal
confirms: round-4#1
```
What holds: `changelog.md:3` now says "Where a link stands anywhere from the root down to the edited file, it opens no record and prints nothing", and the guard's comment at `hooks/edit-leaves-copies.py:273` says "the hook opens no record on such a path". Both hold as built: the guard at `:274-278` returns before the first record is opened, and round 4's Probe H, carried, printed nothing. Round 4's listing command, re-run at the target with `trail/` left out, printed `:273`, `changelog.md:3` and the two other facts at `docs/checks/the-pull-request-check.md:137` and `docs/layout/the-pact.md:120` (executed), as the close says. The docstring clause the same commit added is finding 1, as a `regression:`.

```seal
confirms: round-4#2
```
What holds: `Test__located` stands at the target as `7d11432d0` wrote it. `git diff --stat 7d11432d0 15fd04b81 -- tests hooks` printed nothing, so the crafter's account that `d03b194f5` and `00908b8da` cancel out holds (executed). Round 4's mutants were run again: `bin/seal mutate hooks/edit-leaves-copies.py` under `-k Test__located` with the order swapped (`if optin.marked(root) and os.path.islink(root):`) and with the check removed (`if False:`) was red for both (executed). The refusing case alone, `-k test_refuses_a_root_that_is_a_link`, was red under the swap (executed), so the order is pinned.

Claimed in the close: "Under the swap, the accepting case's path is the same as before, so the red is the refusing case's `asked == []`." That is not what the code does. Under the swap, the accepting case also fails, at `tests/hooks/test_edit_leaves_copies.py:506`, with `asked` holding the root twice, because the mutant asks `marked` once in the swapped condition and once more on the next line (executed, `-k test_accepts_a_root_that_is_no_link`). Its red does not come from the order. The close's conclusion still stands, because the refusing case is red alone. `bin/seal layout --check tests/hooks/test_edit_leaves_copies.py` read 1 file and refused none (executed), which matches the caller's claim.

```seal
confirms: round-4#3
```
What holds: the listing command `git grep -c -E "\.symlink_to\(|os\.symlink\(" -- tests ':!tests/conftest.py'` exits 1 at the target and prints nothing (executed). The six calls pass `symlink_or_skip` its arguments in the order `tests/conftest.py:517` declares, `(target, link, directory=False)`, and the four directory links pass `directory=True` (read, the fix diff). `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` passed 48 (executed). The skip path on Windows was not run (`## Not judged`).

What matched: the fold's statements of the limit. `frame/design.md:91` and `:133` and `frame/plan.md:67` state what the code does: `#_located` checks `os.path.islink(root)` before `optin.marked` (`hooks/edit-leaves-copies.py:120-122`); `#main` checks `threads/`, the item and each component down to the file (`:274-278`); `#_records` skips a file that is a link, and `os.walk` follows no directory link (`:142-147`); and the marker read is `readline(len(MARKER) + 2)` (`lib/optin.py:243`) (read). The row's count, that rounds 1 to 4 spent most findings on links, holds: six of their nine findings are about links (read, the findings' headings). `hooks/hooks.json` sets no `timeout` on the entry, so the harness's default applies, as the row's grounds say (read).

What matched: the follow-up row's account of each mechanism's record. In transcripts under `/Users/x/.claude/projects/` on this machine, a `PostToolUse` hook's note on an `Edit` is an `attachment` of type `hook_success` named `PostToolUse:Edit`, whose `stdout` holds the printed object with its `additionalContext`. A second attachment of type `hook_additional_context` carries the context too (executed, a read of the transcripts' JSON lines). The hook's text holds `RULE`, `` `skills/agent-contract/SKILL.md` rule 19 `` (`hooks/edit-leaves-copies.py:99`). The quote check's refusal holds "quotes words" and "does not hold" (`skills/code-review/scripts/pr_body.py:269-270`) (read).

What matched: `pr.md`'s three quotes. `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` exited 0 with a `wrote:` line and no note (executed). `uvx ruff check` and `uvx ruff format --check` on the hook and its test module passed (executed).

What matched: the records read whole. Apart from findings 2 and 3, nothing in them is contradicted by the target. `changelog.md:3` states the guard as built. `gaps.md`'s open rows name the orchestrator's broad gate. The timings at `frame/plan.md:26` and `frame/questions.md:14` are dated to `5604aa15d` (read).

`Test__located`'s accepting case holds A9's precondition, which `Test_main`'s printing cases hold through the command. What only it adds is the stub's control: it shows the stub is asked at all, so the refusing case's `asked == []` can fail. `seal layout --check` refuses a class without an accepting case, and `seal layout --pairs` names no duplicate pair for the module (executed). It is no finding (`tests/hooks/test_edit_leaves_copies.py:493-506`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The crafter's narrow set, 1128 passed and 9 skipped, which `boundary.txt` under the fix pass's scratch directory shows (read). The file names neither its commit nor its command. This round ran the two modules named above and not that set. The suite beyond them, and the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |
| A Windows run of the link cases and `Test__located`, with and without the link privilege | `tests/hooks/test_edit_leaves_copies.py:307-381`, `tests/hooks/test_edit_leaves_copies.py:489-525` | the orchestrator's broad run on the workflow's `windows-latest` rows |
| The home of `hooks/ask-under-automation.py#_paragraph`, which finding 3's snippet leaves to be named | `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:68` | the orchestrator, or the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` | 48 passed |
| `bin/seal layout --check tests/hooks/test_edit_leaves_copies.py`; `bin/seal layout --pairs tests/hooks/test_edit_leaves_copies.py` | 1 file read, 0 refused; 1 file read, 0 pairs |
| `bin/seal mutate hooks/edit-leaves-copies.py --tests "bin/test -q -p no:xdist tests/hooks/test_edit_leaves_copies.py -k Test__located"` with `if os.path.islink(root):` replaced by `if optin.marked(root) and os.path.islink(root):`, and by `if False:` | baseline passed; 2 mutants, 2 red |
| The same order mutant with `-k test_refuses_a_root_that_is_a_link`, then with `-k test_accepts_a_root_that_is_no_link` | red, then red at `:506` with `asked` holding the root twice |
| `git grep -c -E "\.symlink_to\(\|os\.symlink\(" -- tests ':!tests/conftest.py'` | exit 1, nothing printed |
| `git diff --stat 7d11432d0 15fd04b81 -- tests hooks` | nothing printed |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` | exit 0, `wrote:` line, no note |
| `uvx ruff check` and `uvx ruff format --check` on `hooks/edit-leaves-copies.py` and `tests/hooks/test_edit_leaves_copies.py` | both exit 0 |
| `python3 -I` over the JSON lines of the transcripts under `/Users/x/.claude/projects/`, counting the attachments named `PostToolUse:Edit` by type and comparing each `hook_additional_context` with the `hook_success` of the same tool use | both types stand; each `hook_success` read holds the `additionalContext` in its `stdout` |
