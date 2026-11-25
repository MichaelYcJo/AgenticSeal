# Review round 1: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: 018b9dac4 against origin/release/v0.39.0
```

The range is `8d99b99e2..018b9dac4`, read in a `git clone --no-local` checked out at `018b9dac4` under this round's scratch directory. No earlier round exists, so nothing was carried: every fact below was opened this round. Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md`. Read whole in the range: `hooks/edit-leaves-copies.py`, `tests/hooks/test_edit_leaves_copies.py`, and the diff of every other file the range changes. No `pr.<lang>.md` stands, and `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared.

The axes this change owns, beside the table's: what share of real record edits the hook can see at all, what the hook opens when a record is not a plain file, whether the three merged quotes the new check refuses reach any reader, and whether each record's statement of what Q1 measured holds at the target.

## Findings

### 1. `gaps.md` keeps open the row on whether the hook's own text reaches the model, and says Q1 measured only a fixed text, while Q1's Status cell records the measurement of the hook's own text

```seal
severity: should
location: `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/gaps.md:10`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:26`
evidence: executed `git grep -n -E "fixed text|own text|its text delivered" -- seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix ':!seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/trail'` (prints `frame/plan.md:26`, `frame/questions.md:14`, `gaps.md:10`); executed `git diff --stat 5f2b58e9a 018b9dac4 -- hooks lib` (prints nothing); read `frame/questions.md:14`
```

Why it matters: the sealer reads `gaps.md`'s open rows as what nobody established. Claimed at `gaps.md:10`: "Q1's answer measured a hook that printed a fixed text", and the row stays open for the orchestrator. Found at `frame/questions.md:14`, as folded at `626a238cd`: a third `claude -p` session loaded through `--plugin-dir` a plugin holding `hooks/edit-leaves-copies.py`, `lib/` and the `PostToolUse` entry as they stand at `5f2b58e9a`, and the model quoted back the hook's own context naming `pr.md` line 1. `hooks/` and `lib/` are unchanged from `5f2b58e9a` to the target. So the row's sentence is false at the target, and the question it holds is answered for the main session. This settles the orchestrator's first doubt. What Q1 records and what it leaves out are both claims of the orchestrator, labelled executed there; this round did not start a session (`## Not judged`).

What Q1 does not show is the hook's own text inside a subagent. The second session showed a plugin hook's fixed text arriving inside a plugin's subagent, and the third showed the hook's own text in the main session alone. `frame/plan.md:26` says "`frame/questions.md` Q1's measurement found its text delivered in the main session and inside a plugin's subagent", where "its" is the hook the row chooses. That sentence states the same fact a step further than Q1 does, so the fix pass owes it too.

The listing command above is a search on the words of this fact, a sample under contract rules 12 and 19. It printed the three places, and `frame/questions.md:14` is the home both others cite.

```markdown
gaps.md, the row at line 10:
| closed Whether `hooks/edit-leaves-copies.py`'s own text reaches the model in a session that loads the plugin. `frame/questions.md` Q1, its Status cell, records a third session whose plugin held the hook, `lib/` and the `PostToolUse` entry as they stand at `5f2b58e9a`, unchanged at the target in `hooks/` and `lib/`, where the model quoted back the hook's own context naming `pr.md` line 1. The hook's own text inside a subagent was not measured; a plugin hook's fixed text was, in Q1's second session. | the orchestrator, by the session Q1's default names |

frame/plan.md, row at line 26, the sentence in the failure-scenario cell:
`frame/questions.md` Q1's measurement found a plugin hook's text delivered in the main session and inside a plugin's subagent, and this hook's own text in the main session
```

```seal
verdict: fixed f1fd9f345
answer: The `frame/plan.md:26` half is the framer's fold at `17003563a`, whose row now says Q1 found a plugin hook's fixed text in the main session and inside a plugin's subagent, and this hook's own text in the main session. The `gaps.md` half is `f1fd9f345`, in my own words rather than the snippet's: the snippet rewrote the item and kept it closed with the old answerer in place, so the old row is closed as answered for the main session by Q1's third session, and a new open row holds what Q1 did not measure, this hook's own text inside a subagent, with the orchestrator as its answerer. The listing command run again at `f1fd9f345` prints `frame/plan.md:26`, `frame/questions.md:14`, and `gaps.md:10` and `:11`; each states Q1's measurement as Q1's Status cell records it, which is the home the others cite.
```

### 2. The hook takes its context words from `old_string` alone, so it can print nothing for 824 of 2,174 measured edits of work item records, while the frame's grounds measured context taken from the file

```seal
severity: should
location: `hooks/edit-leaves-copies.py:23-28`, `hooks/edit-leaves-copies.py:127-142`, `hooks/edit-leaves-copies.py:212-219`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:17`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:91`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/plan.md:26`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/changelog.md:3`, `tests/hooks/test_edit_leaves_copies.py`
evidence: executed `python3 -I test_tmp_round1_probes.py <clone> <transcripts>` (Probe B, `## Probes`); executed `python3 -I test_tmp_round1_widened.py <clone>`; executed `git grep -n -E "three words on each side|AROUND. words|old_string. alone|words of .old_string|G7's replay found" -- hooks tests/hooks seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix README.md README.ko.md CONTRIBUTING.md SECURITY.md`; read `trail/phases/phase-2.md:17`, `frame/design.md:17`, `frame/plan.md:13`, `frame/plan.md:26`
```

Why it matters: the hook exists to name a copy at the edit that leaves it, and it is blind to more than a third of the edits it runs on. `#_spans` pads a changed span with up to three words of `old_string`. Where `old_string` ends at the change, or starts at it, the span is shorter, and under `MIN_WORDS` or `MIN_CHARS` it is dropped. Probe B put every `Edit` call of a work item's record outside `trail/` and `guarantee.md` that this repository's Claude Code transcripts hold through `_spans`: 2,178 calls, from 14 session transcripts and 353 subagent transcripts. 4 changed only whitespace. Of the other 2,174, 1,350 keep a span and 824 keep none, so for 824 the hook prints nothing whatever copies stand. Of those 824, 471 keep a span once three words of context stand on each side. The probe used four-character filler words for that context, so 471 is a floor. By file, `frame/plan.md` is the worst: 375 of 673 edits keep no span.

The frame accepted another miss. `frame/plan.md:26` names as the hook's failure scenario that "it misses a paraphrased copy", and `frame/plan.md:13` names its false prints. Neither names this miss. The chosen row rests on G7: "G7's replay found the copies it prints at the edit that left them". G7 at `frame/design.md:17` took "each changed span of the old text with three words on each side", the file's text and not `old_string`. Phase 2 named the difference: "G7's replay took its three words of context from the file's old text, not from `old_string`, so it found copies this hook does not find" (`trail/phases/phase-2.md:17`). The fold at `626a238cd` left G7 and the row as they stood. So the measurement the choice rests on is of a different reading from the one built. This answers the orchestrator's third doubt: the false prints stay within what the plan accepted, and the misses do not.

The cure costs one read of a file the hook already checks. After the edit, the edited file holds `new_string` where `old_string` stood, with the same words around it. So the words around `new_string`'s first place in that file are the context `old_string` left out. The probe ran the snippet below once. The three spans it gives for a change at `old_string`'s end, at a cut word's start, and for a deletion are each in the old text. The deletion falls back to `old_string` alone. Where `new_string` also stands earlier in the file than the edit, the context is the earlier place's, and the span then matches nothing or a place that holds those words: the same cost as the false print the docstring already names.

The listing command printed the hook's docstring and comment (`hooks/edit-leaves-copies.py:24`, `:61`, `:129`), `changelog.md:3`, `frame/design.md:17` and `:91`, `frame/plan.md:26`, and a case docstring at `tests/hooks/test_edit_leaves_copies.py:165`, which states the insertion rule and stays true. It is a search on words, a sample under contract rules 12 and 19. The snippet covers the code. The fix pass owes the docstring at lines 23 to 28, the comment at line 61, `changelog.md:3`'s "with three words on each side", and a case in `tests/hooks/test_edit_leaves_copies.py` whose `old_string` ends at the change and whose copy stands in `gaps.md`, seen red against the current `#main`. The frame's `frame/design.md:91` bullet and the G7 sentence of `frame/plan.md:26` are the orchestrator's fold. If the orchestrator keeps `old_string` alone instead, the fold names this miss and its measured share in `frame/plan.md:26`'s failure scenario, and `changelog.md:3` says the hook does not see an edit whose `old_string` holds too few words beyond the change.

```python
def _widened(text, old, new):
    """OLD and NEW, each with the `AROUND` words that stand before and after
    NEW's first place in TEXT, the edited file as it stands after the edit,
    so a change at an end of OLD keeps the words around it. A word cut by
    the edit's edge is joined to the string it touches. OLD and NEW as
    given where NEW is empty or does not stand in TEXT."""
    at = text.find(new) if new else -1
    if at < 0:
        return old, new
    before, after = text[:at], text[at + len(new) :]

    def wrapped(middle):
        head, tail = before.split(), after.split()
        if head and not before[-1].isspace() and middle[:1].strip():
            middle, head = head[-1] + middle, head[:-1]
        if tail and not after[0].isspace() and middle[-1:].strip():
            middle, tail = middle + tail[0], tail[1:]
        return " ".join(head[-AROUND:] + [middle] + tail[:AROUND])

    return wrapped(old), wrapped(new)


# In `main`, in place of the `isfile` check and the `_places` call. The
# open raises on a missing or undecodable file, which `__main__` turns into
# exit 0 as the `isfile` check's return did.
    with open(os.path.join(item, *rel.split("/")), encoding="utf-8") as f:
        old, new = _widened(f.read(), old, new)
    places = _places(item, _records(item), _spans(old, new))
```

```seal
verdict: fixed 3d4a8810e
answer: The frame's half is the framer's fold at `17003563a`: `frame/design.md` *Data & interfaces*, the hook's second bullet, *Scope* items 9 and 11, acceptance row A13, the `## Rule changes` add row, and `frame/plan.md:26` and `:27`. The code is `4be875457`, then `3d4a8810e`. `_widened` takes the three words on each side from the edited file around `new_string`'s first place, falling back to `old_string` alone where `new_string` is empty or not in the file, and `main` opens the edited file in place of the `isfile` check. The snippet was read before it was applied, and one part was not taken. Its conditions `middle[:1].strip()` and `middle[-1:].strip()` survived `seal mutate`, since a joined string that holds a space splits there again in `#_spans`, so `3d4a8810e` removed them. The A13 case `test_accepts_and_names_a_copy_where_old_string_ends_at_the_change` and the edge case `test_accepts_and_names_a_copy_where_a_word_is_cut_at_an_edge` were seen red against the hook that read `old_string` alone: each printed nothing and failed at `json.loads`. `test_accepts_and_names_a_deletion_by_the_words_of_old_string` covers the fallback. At `3d4a8810e`, `seal mutate` over the link skip and each unit of the widening gave 9 mutants, all red. The docstring at lines 23 to 36, the comment over `AROUND` and `changelog.md:3` are rewritten. The listing command run again at `7e4626370` prints the hook's docstring and comments, which state the new reading; `changelog.md:3`; the frame lines the fold wrote; `trail/phases/phase-2.md:17` and this record, which record past acts and stay; `tests/hooks/test_edit_leaves_copies.py:27`, whose `SPAN` the widened reading still gives; `:165`, whose three words on each side of an insertion still hold; and `:223`, the new fallback case.
```

### 3. The hook opens a record that is a link, so a work item in a checked-out repository can make it read a file outside the repository, or `/dev/zero` without end

```seal
severity: should
location: `hooks/edit-leaves-copies.py:114-124`, `hooks/edit-leaves-copies.py:43-51`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:90`, `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/design.md:132`, `tests/hooks/test_edit_leaves_copies.py`
evidence: executed `python3 -I test_tmp_round1_links.py <clone> <scratch>` (`## Probes`); executed `git grep -n -E "file outside the item|outside the item's directory|beyond the work item's records|no file outside" -- hooks tests/hooks seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix README.md README.ko.md CONTRIBUTING.md SECURITY.md docs`; read `SECURITY.md:43-46`, `SECURITY.md:55-59`, `lib/routing.py:284-291`, `hooks/ask-under-automation.py:80-86`
```

Why it matters: `SECURITY.md:43-46` names "a developer with an untrusted repository checked out locally", where "one of the plugin's hooks firing on its own" acts on the repository's content, as a boundary worth reporting, and `SECURITY.md:55` puts "path handling that leaves the repository being checked" in scope. Git commits a link as a link. `#_records` keeps every name in `os.walk`'s `files` that ends in `.md`, and `#_places` opens each one and reads it whole. The probe built a marked root whose work item holds `leak.md`, a link to a file outside the repository, and ran the hook's script on an `Edit` of the item's `frame/design.md`. It exited 0 and named `` `leak.md` line 1 `` with the words it found in that outside file. With a second link `zero.md` to `/dev/zero`, `_records` listed `zero.md` for reading, and `os.path.isfile` is false for it. The probe did not read it, since the read never ends and grows in memory until the harness's hook timeout stops it.

Claimed at `frame/design.md:132`, the `## Rule changes` row the settle writes into `docs/running/what-a-script-gates.md`: the hook "reads no `Write` call and no file outside the item's directory". A link inside the item is such a file. The hook's docstring at lines 43 to 51 lists what prints nothing and names no link. No legitimate record is a link, so skipping links costs nothing the hook was built to find.

The same class stands outside this diff, in code the plugin's other hook reaches: `lib/routing.py#read_declaration` opens each open work item's `routing.md`, and `hooks/ask-under-automation.py#_paragraph` opens a document, each with no check for a link. This finding asks the fix pass for the new hook only. The other two are named for the orchestrator to send where it judges, since the listing command found them in no record of this item. That search is a sample under contract rules 12 and 19. A paraphrase such as "reads only the item's records" escapes it, and `SECURITY.md:28-30`'s "reads a work item's records" stays true once links are skipped.

The snippet replaces `#_records`. Precondition: `os.path.islink` reads the link itself, and `os.path.isfile` follows it; a Windows junction names a directory, so it never stands in `files`. The fix pass also owes a link among the docstring's list at lines 43 to 51, and a case in `tests/hooks/test_edit_leaves_copies.py`: a `.md` link to a file outside the item that holds the replaced words prints nothing, seen red against the current `#_records`. The frame's `frame/design.md:90` bullet on the records it searches, and the row at line 132, are the orchestrator's fold.

```python
def _records(item):
    """The `/`-joined paths of the `.md` files under ITEM this hook
    searches. A link is no record: it can name a file outside the
    repository, or a device whose read never ends."""
    found = []
    for at, _, files in os.walk(item):
        under = os.path.relpath(at, item)
        prefix = "" if under == os.curdir else "/".join(under.split(os.sep)) + "/"
        for name in files:
            full = os.path.join(at, name)
            if os.path.islink(full) or not os.path.isfile(full):
                continue
            if name.endswith(".md") and _read(prefix + name):
                found.append(prefix + name)
    return found
```

```seal
verdict: fixed 4be875457
answer: `#_records` skips a name that `os.path.islink` reads as a link, and its docstring and the module's list of what prints nothing name a link as no record. This is in my own words rather than the snippet's: its `or not os.path.isfile(full)` holds only a name that is not a link and not a regular file, such as a FIFO, which git does not commit, and no case could show that guard red without a read that never ends, so it was left out. `test_refuses_to_print_where_the_words_stand_only_behind_a_link`, a `leak.md` link to a file outside the repository that holds the replaced words, printed the `leak.md` place against the hook before the fix, and prints nothing after it. Mutant 1 of the batch at `3d4a8810e`, the skip replaced with `if False:`, was red. The same class outside the diff, `lib/routing.py#read_declaration` and `hooks/ask-under-automation.py#_paragraph`, is the orchestrator's: `frame/plan.md` *Judgments of the run* sends it to an issue of its own. The listing command run again at `7e4626370` prints `docs/checks/the-pull-request-check.md:49`, on another fact; `frame/design.md:59` and `:133`, which hold at HEAD; `frame/plan.md:67`; and this record. `frame/design.md:90`, the hook's first bullet, says the hook searches the item's `.md` files and names no link, which the search does not print; it is the framer's to fold.
```

## Confirmations

What matched: the quote check of `frame/design.md` *Scope* item 1 and *Data & interfaces*, at `skills/code-review/scripts/pr_body.py:519-565` and `:606-608`. The form reads the line's last `" (` before a backtick, names the line not read otherwise, refuses a path outside the item, an absent file and an undecodable file, and compares collapsed text. `first_part` raises before the translation files are looked for, as `trail/phases/phase-1.md:11` says. Read, and executed: `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/skills/test_pr_body.py tests/behaviour/test_chain_hooks_hardening.py` passed 158.

What matched: the orchestrator's second doubt. Probe A ran `quote_lines` and `_unstood` over every `seal/threads/*/pr.md` at the target. It found 295 quotes and 3 refused: `1794271937-the-readme-narrates-three-migrations/pr.md:4`, `1794289595-the-verifying-round-rule-has-four-owners/pr.md:8` and `1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/pr.md:4`, the three phase 1 named. No line was left unread. Nothing reads those directories through the check. `chain_check.py#body` reads only the item of the judged declarations, which are the `routing.md` files naming the branch or changed in the diff and not carried by a squash (`skills/code-review/scripts/chain_check.py:2192-2202`, `:2318-2320`). `seal settle` reads no `pr.md` (`git grep` of `pr.md` and `OPTIN.PR` over `skills/settle`, `lib`, `bin` and `skills/verify/scripts` prints only `lib/optin.py:68`). No test runs the check over the tree's work items: the test files that name both `seal/threads` and `pr_body` or `pr.md` read fixtures, by reading each match. So nothing now fails, and *Out*'s choice to leave merged items' quotes holds.

What matched: `pr.md`'s three quotes stand word for word at their coordinates: line 1 at `frame/plan.md:20`'s failure-scenario cell, line 2 at the head of `frame/questions.md:14`'s Status cell, and line 3 at `frame/questions.md:15`'s *Default until answered* cell. The orchestrator's `seal pr-body` exit 0 held when run again: `bin/seal pr-body <item> --body <scratch file>` exited 0 and printed no note.

What matched: `gaps.md:8` names this round's proofer as its answerer, asking whether a proofer reads the paste-ready paragraph as asking for the listing command, and whether a fix pass runs it again. Read at the target: `skills/code-review/SKILL.md:246-255` says a finding on a wrong sentence "lists them with a command run at the round's target" and "carries it on its `evidence:` line as `executed`". `skills/implement/fix-pass.md:64-70` has the fix pass run that command "again after its last fix commit" and name in `answer:` each place it still prints. Each reads one way, and findings 1 to 3 of this record follow it. The one point a reader must settle is which command a fix pass runs where an `evidence:` line names several. The paragraph says "the command that lists each place stating a fact", and this record names each listing command by its `git grep`. The row can close.

What matched: the absence searches of `frame/plan.md:42` and acceptance row A6 print nothing at the target (executed: each `git grep -n -F` over `agents skills docs templates` exited 1). `HOOK_ENTRIES` and `HOOK_FILES` carry the hook (`tests/behaviour/test_chain_hooks_hardening.py:35`, `:40`). `hooks/hooks.json` holds the command *Scope* item 10 spells. The `RULES` row of key 31 ties the fix pass's citation to the review skill's paragraph.

What matched: each statement G17 lists names the fourth hook, read in the diff of `README.md`, `README.ko.md`, `SECURITY.md` and `CONTRIBUTING.md`. The Korean edition renders the English item's facts. `changelog.md`'s items each state what the code at the target does, apart from the span context finding 2 names.

The new cases in `tests/hooks/test_edit_leaves_copies.py` and `tests/skills/test_pr_body.py` each cover a path their group did not; no case duplicates another. No case holds a link (finding 3) or a change at `old_string`'s end (finding 2).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The three `claude -p` sessions Q1's Status cell records. Contract rule 6 withholds spawning an agent, and this round started no session, so their outcome is the orchestrator's executed claim, read and not re-run | `seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix/frame/questions.md:14` | the orchestrator, and the sealer at its audit |
| The suite beyond the three modules run here, the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |
| Whether Probe B's share of blind edits holds in another repository that runs the chain. The population is this repository's transcripts alone | finding 2 | the repository owner, beside `seal/follow-up.md`'s #1612 row |
| How the harness stops a hook whose read of `/dev/zero` does not end. The probe did not run that read | finding 3 | the orchestrator, should it want the cost measured |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_round1_probes.py <clone> <transcripts>`, the file under this round's scratch directory; `<transcripts>` is this repository's directory under `~/.claude/projects/`, its `*.jsonl` and `*/subagents/*.jsonl` | Probe A: 295 quotes over every `seal/threads/*/pr.md`, 3 refused (the three Confirmations name), 0 unread. Probe B: 2,178 `Edit` calls of a work item record outside `trail/` and `guarantee.md`; 4 whitespace only, 1,350 keep a span under `_spans`, 824 keep none, 471 of those 824 keep one with three filler words of context on each side. No-span counts by file: `frame/plan.md` 375 of 673, `frame/design.md` 227 of 810, `gaps.md` 144 of 346, `changelog.md` 68 of 295, `frame/questions.md` 12 of 46, `pr.md` 2 of 4 |
| `python3 -I test_tmp_round1_widened.py <clone>` | finding 2's `_widened` gave `record and the next round finds every` for a change at `old_string`'s end and `The settle reads each record and` for a cut word at its start, where `_spans` alone gave none; a deletion gave none either way; every widened span stands in the old text |
| `python3 -I test_tmp_round1_links.py <clone> <scratch>` | the hook's script, on an `Edit` of a scratch item's `frame/design.md`, exited 0 and named `` `leak.md` line 1 ``, a link to a file outside the scratch repository; `_records` listed `zero.md`, a link to `/dev/zero`, for reading, and `os.path.isfile` was false for it |
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/skills/test_pr_body.py tests/behaviour/test_chain_hooks_hardening.py` | 158 passed |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch file>` | exit 0, `wrote:` line, no note |
