# Review round 2: 1792973486-a-change-only-the-shell-makes-is-a-chore

target: cd9c249b, fixes c6742472..cd9c249b

This round reads the fix range `c6742472..cd9c249b` in the checkout of the
branch at `cd9c249b`: `bb01b549`, `8e656460`, `d1390952`, `cc20b733` and
`cd9c249b`. It answers the three findings of round 1 and reads the new
`CLAUDE.md` sentences and the new changelog fragment again.

Three facts are carried from round 1 and were not re-established: the
routing edit gate matches the `Write`, `Edit` and `NotebookEdit` tools alone
(`hooks/routing-edit-gate.py:57`); work items have renamed files with
`git mv` (`b451e503`, `4b363e68`); and the CI checks run on every pull
request (`.github/workflows/test.yml:3-11`, `.github/workflows/hygiene.yml:3-16`).
No check over any of them failed in this range, and the fix range changes
none of those files. Every verdict below was reached in this round.

## Findings

### 1. The clause `that kind of gate which only such a change passes through` has a second reading that drops the scope of the first sentence

severity: should
location: `CLAUDE.md:21-22`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/spec.md:37-38`
evidence: read `CLAUDE.md:17-22`, `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/spec.md:34-38`
verdict: fixed 76ae375a
regression: round-1#2

The unit is the second new sentence of `CLAUDE.md` *The rule a mechanism is
kept against*, at `CLAUDE.md:18-22`, and its quote at `spec.md:35-38`. The
frame, `spec.md` *Scope* item 1 read with `CLAUDE.md` *Repo rule: text an
agent or a check reads has one reading*, asks for the sentence word for word
and with one reading; the fix commit `8e656460` wrote `a gap in that kind of
gate which only such a change passes through`, and that wording came from
round 1's own paste-ready block for finding 2, which `bb01b549` quoted into
the frame.

The sentence can be read two ways.

- The intended reading attaches `which only such a change passes through` to
  `a gap`. `that kind of gate` points back to the first sentence, a gate
  that stops a session. The sentence then says: a gap in such a gate that
  only a change no work item owns passes through is not a weakness to close.
- `that kind of gate which ...` is also the English construction "the kind
  of gate which ...". In that reading the relative clause defines the kind:
  a gate which only changes no work item owns pass through. `that kind` no
  longer points back to the first sentence, and the exemption covers gaps in
  any gate that only such changes reach.

The two readings lead an agent to different acts. Under the second, the
routing check is not exempt, because work a work item owns passes through it
too. That contradicts the first sentence, which names the routing check as
the gate the principle is about. Under the second reading the exemption also
reaches a gate that does not stop a session, which finding 2 of round 1 took
out. The repository rule says shorter is never bought with a second reading.
Before the fix the clause read `a gap in a gate or a check that only such a
change passes through`, which had the same attachment question but not the
`that kind of ... which` construction that invites the second reading.

The fix names the gap as the thing a change passes through, so `which` has
no noun to attach to. The phrase `S2` greps for, `only such a change passes
through`, stays whole on one line, and line 21 is no longer a 32-column line.
The paragraph from `A rule's proof` on keeps its breaks.

```markdown
it costs**; existing is no reason to keep it. A gate that stops a session,
the routing check among them, guards the work a work item owns. A change
that would be routed `no work item`, such as a formatter run, a dependency
bump or an identifier renamed across files by `sed`, is outside that work, so
where only such a change passes through a gap in that kind of gate, the gap
is not a weakness to close. A rule's proof
is the test or behaviour eval its `check:` line names. A fact has one source,
```

`spec.md` *Scope* item 1 quotes the sentence exactly, so its quote at
`spec.md:34-38` takes the same words:

```markdown
   > A gate that stops a session, the routing check among them, guards the
   > work a work item owns. A change that would be routed `no work item`, such
   > as a formatter run, a dependency bump or an identifier renamed across
   > files by `sed`, is outside that work, so where only such a change passes
   > through a gap in that kind of gate, the gap is not a weakness to close.
```

The changelog fragment states the same clause, and finding 2's block carries
the new words for it.

answer: The finding holds, and the sentence's grounds route it to an ordinary fix pass: the clause came from round 1's paste-ready block, applied as given, so the defect is in how the fix was written, not in the frame. The orchestrator put the record's clause into `spec.md` *Scope* item 1 in eb56b648, and the spec still parses with the no-change block and no error (executed). The smith put the same clause into `CLAUDE.md` in 76ae375a, word for word; `git diff --word-diff 61a8455a -- CLAUDE.md` shows only added words, and `only such a change passes through` stands on one line at `CLAUDE.md:21`, the one hit outside `seal/specs/` (executed by the smith).

### 2. The changelog fragment says no gate is built to catch a change only the shell makes, a claim the `CLAUDE.md` sentence does not make

severity: should
location: `seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/changelog.md:3-11`
evidence: executed `python3 -I -c "import re;print([('only the shell makes' in re.sub(r'\s+',' ',open(p).read())) for p in ('CLAUDE.md','seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/changelog.md')])"`
verdict: fixed 67ac87f4
regression: round-1#3

The unit is the fragment's third sentence, at `changelog.md:8-11`, which
`d1390952` added. The frame is round 1's finding 3, which asked for the
fragment in the words the sentence holds once findings 1 and 2 are answered,
together with `spec.md:42-44`, which says a file renamed with `git mv` inside
a work item is work the work item owns; the fix wrote `so no such gate is
built to catch a change only the shell makes`, a clause `CLAUDE.md` does not
hold, and the clause came from round 1's own draft fragment, which carried
the issue's wording past finding 1's correction.

The command above prints `[False, True]`. With whitespace collapsed, the
phrase `only the shell makes` is absent from `CLAUDE.md` and present in the
fragment. Finding 1 of round 1 changed the sentence's example because a
change only the shell makes includes a work item's `git mv`, which the
routing check never sees and which is work a work item owns. `CLAUDE.md`
now speaks only of a change that would be routed `no work item`. The
fragment adds the broader class back. It tells the reader of the release
note that no gate that stops a session is built to catch a change only the
shell makes, and a work item that only renames files with `git mv` is such
a change. That is the reading finding 1 removed from `CLAUDE.md`.

The fragment's heading also says the gate `is weighed by the work a work item
owns`, where the sentence says it `guards` that work. The block below uses
the sentence's verb so the heading and the body describe one rule. It also
takes finding 1's wording for the gap clause.

```markdown
### Changed

- **A gate that stops a session guards the work a work item owns
  (#1031).** This repository's `CLAUDE.md`, *The rule a mechanism is kept
  against*, now says that a gate that stops a session, the routing check
  among them, guards the work a work item owns. A change that would be
  routed `no work item`, such as a formatter run, a dependency bump or an
  identifier renamed across files by `sed`, is outside that work, so where
  only such a change passes through a gap in that kind of gate, the gap is
  not a weakness to close. The checks that run on every pull request are
  not that kind of gate, and the rule does not exempt them. Nothing the
  plugin installs into a consuming repository changes.
```

answer: The finding holds, and it is routed to an ordinary fix pass for the same reason as finding 1. The smith replaced the fragment with the record's block in 67ac87f4; the whitespace-normalised fragment no longer holds `only the shell makes`, and `tests/test_the_changelog_is_gathered_at_release.py` passes (executed by the smith). The smith also found the same broader claim in `overview.md` *Why this work exists* ("no gate is built to catch it"), which the orchestrator rewrote in 4eb9cf31 to state the principle as `CLAUDE.md` does.

## Confirmations

confirms: round-1#1
The example is now an identifier renamed across files by `sed`, at
`CLAUDE.md:19-20`, and `spec.md:42-44` says a file renamed with `git mv`
inside a work item is work the work item owns. Claimed in the answer: the
sentences went into `CLAUDE.md` word for word, and the word diff shows only
added words. Found: `git diff --word-diff 61a8455a..HEAD -- CLAUDE.md` shows
`{+ +}` runs only and no `[- -]` run, and a Python comparison with
whitespace collapsed found the quote of `spec.md:34-38` in `CLAUDE.md`,
starting directly after `existing is no reason to keep it.` (both
executed). `8e656460` touches `CLAUDE.md`, a path the finding's `location:`
names.

confirms: round-1#2
The first sentence now names `A gate that stops a session, the routing check
among them` (`CLAUDE.md:17-18`). `stops a session` has one meaning in the
tree: a refusal by a `PreToolUse` hook (`hooks/config.py:888-889`,
`tests/test_config.py:904-906`, read), and `hooks/routing-edit-gate.py:285`
answers with that hook's `deny` (read). The checks of
`CONTRIBUTING.md:58-64` run on a pull request and stop no session, so the
sentence no longer reaches them, and `spec.md:40-42` says so for the frame
(read). Claimed in the answer: `git grep` outside `seal/specs/` finds the
`S2` phrase at `CLAUDE.md:22` alone. Found: the same (executed). Finding 1
of this round concerns the second sentence's gap clause, not this scope.

confirms: round-1#3
`changelog.md` exists in the work item, and `overview.md` *Not done* no
longer holds the no-fragment paragraph (`git diff c6742472..cd9c249b`,
executed). Claimed in the answer: `tests/test_the_changelog_is_gathered_at_release.py`
and the fragment's two other readers pass. Found: `bin/test` over that
module, `tests/test_gather_changelog.py` and `tests/test_release_hygiene.py`,
with the modules of `S5` and `tests/test_docs_line_wrap.py`, gave 243 passed
at exit 0 (executed, a probe and not the broad gate). `cc20b733` touches
`overview.md`, a path the finding's `location:` names. The fragment's
wording is finding 2 of this round.

confirms: none
The smith's decline to rewrite `phases/phase-1.md` holds.
`agents/smith.md:153` says a fix pass writes two lines of each finding and
no phase record, and `skills/implement/SKILL.md:478-482` says the same and
that the build's phases keep their records (read). `phases/phase-1.md` binds
itself to `77761ea9` in its `Commit` row, and its claims hold at that
commit, as round 1 checked. Its paragraph on the fragment left the decision
to the orchestrator and did not say none is owed, so it stands on no fact
the fix range changed. The record of the fix range is round 1's `answer:`
lines and the five commits.

confirms: none
`overview.md` *Fed back into the spec* lists two clauses, and each matches
what `bb01b549` added to `spec.md` *Scope* item 1 (`git diff
c6742472..cd9c249b`, executed). Each is marked `inferred during
implementation`, as `templates/sdd-overview.md` asks (read). `questions.md`
*Its wording* states the narrowed scope and its reason, and names finding 2
as the round that narrowed it (read).

confirms: none
`bin/rules --check` exited 0 at `cd9c249b` (executed, a probe). The
paragraph's widest line is 77 columns and line 21 is 32 columns (executed,
`awk`). The short line has the price round 1 accepted, keeping the `S2`
phrase on one line; finding 1's block removes it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head, labelled `unverified` in `overview.md` *Not verified*; that label is honest, since no party ran them | `cd9c249b` | the orchestrator, through `broad-gate` once the rounds settle |
| The removal of the session memory file that held the principle, which lies outside the repository | outside the repository | the orchestrator, after the merge, as `spec.md` *Scope* item 4 says |

## Probes

| Command | Result |
|---|---|
| `git diff c6742472..cd9c249b` | the fix range touches `CLAUDE.md` and five files of the work item, nothing else |
| `git diff --word-diff 61a8455a..HEAD -- CLAUDE.md` | `{+ +}` runs only, no `[- -]` run |
| `python3 -I -c` comparing the whitespace-collapsed quote of `spec.md:34-38` with `CLAUDE.md` | `True True`: the quote stands in the file, directly after the anchor sentence |
| `python3 -I -c` testing `only the shell makes` in `CLAUDE.md` and in the fragment, whitespace collapsed | `[False, True]` |
| `git grep -n 'only such a change passes through' -- ':!seal/specs/'` | `CLAUDE.md:22` alone |
| `awk 'NR>=16 && NR<=36 {print NR, length($0)}' CLAUDE.md` | widest line 77 columns; line 21 is 32 |
| `git grep -n -i -E 'stops? (a\|the) session' -- ':!seal/specs/'` | each hit outside `CLAUDE.md` means a refusal by a hook or a reader that fails closed |
| `bin/test` over the five `S5` modules, `tests/test_docs_line_wrap.py`, `tests/test_the_changelog_is_gathered_at_release.py`, `tests/test_gather_changelog.py` and `tests/test_release_hygiene.py`, `-q` | 243 passed, exit 0 |
| `bin/rules --check` | exit 0 |
