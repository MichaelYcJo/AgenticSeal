# Review round 3: 1792973486-a-change-only-the-shell-makes-is-a-chore

target: 8a66584e, fixes d7da1203..8a66584e

This round reads the fix range `d7da1203..8a66584e` in a `git clone
--no-local` of the branch at `8a66584e`: `eb56b648`, `76ae375a`, `67ac87f4`,
`4eb9cf31` and `8a66584e`. It answers the two findings of round 2.

Three facts are carried from rounds 1 and 2 and were not re-established: the
routing edit gate matches the `Write`, `Edit` and `NotebookEdit` tools alone
(`hooks/routing-edit-gate.py:57`); the CI checks run on every pull request
(`.github/workflows/test.yml:3-11`, `.github/workflows/hygiene.yml:3-16`);
and `stops a session` means a refusal by a `PreToolUse` hook
(`hooks/config.py:888-889`). The fix range changes none of those files
(`git diff --stat d7da1203..8a66584e -- hooks .github` is empty, executed).
Every verdict below was reached in this round.

## Findings

This round opens no finding. Both closes of round 2 hold, and the one text
the fix range added beyond round 2's blocks, the rewritten sentence of
`overview.md` *Why this work exists*, states nothing the frame does not.
With nothing open, what comes due is the orchestrator's broad run, and the
sealer's spawn after it.

## Confirmations

confirms: round-2#1
The gap clause now reads `so where only such a change passes through a gap
in that kind of gate, the gap is not a weakness to close` at
`CLAUDE.md:20-22`. It is round 2's paste-ready block line for line
(`git diff d7da1203..8a66584e -- CLAUDE.md`, executed). The second reading
round 2 named came from `that kind of gate which ...`, and no relative
clause follows `that kind of gate` any more: with whitespace collapsed,
`which only` is absent from `CLAUDE.md` (executed). So `that kind of gate`
can only point back to the first sentence, a gate that stops a session, and
the gap is the one thing the change passes through. Read either as a place
or as a condition, `where` leads an agent to the same act. The answer
claims that the smith put the clause into `CLAUDE.md` word for word, the word
diff shows only added words, and the `S2` phrase stands at `CLAUDE.md:21` as
the one hit outside `seal/specs/`. Found: `git diff --word-diff
61a8455a..HEAD -- CLAUDE.md` shows six `{+ +}` runs and no `[- -]` run; a
Python comparison with whitespace collapsed finds the quote of
`spec.md:34-38` in `CLAUDE.md`, directly after `existing is no reason to
keep it.`; and `git grep` finds `CLAUDE.md:21` alone (all executed).
Claimed: the spec still parses with the no-change block. Found: `bin/settle
--released-at HEAD`, run without `--apply`, exits 0 and holds this work item
back only for the open `Not verified` row of `overview.md`, with no parse
error (executed; it wrote nothing). `76ae375a` touches `CLAUDE.md` and
`eb56b648` touches `spec.md`, both paths the finding's `location:` names.
The paragraph's widest line is still 77 columns, and the short line moved
from line 21 (32 columns) to line 22 (42 columns). That is the price rounds
1 and 2 accepted for keeping the `S2` phrase on one line, and
`tests/test_docs_line_wrap.py` passes.

confirms: round-2#2
`changelog.md` is round 2's block line for line (`git diff
d7da1203..8a66584e`, executed). Re-run of round 2's `evidence:` command:
it printed `[False, False]`, so `only the shell makes` is now absent from the
fragment as from `CLAUDE.md` (executed). The heading takes the sentence's
verb, `guards`, and the fragment's second sentence equals the second
sentence of `CLAUDE.md` with whitespace collapsed (executed). The answer
claims that `tests/test_the_changelog_is_gathered_at_release.py` passes. Found:
it passes in the run of 243 cases below. `67ac87f4` touches `changelog.md`,
the path the finding's `location:` names. Claimed: the orchestrator
rewrote `overview.md` *Why this work exists* in `4eb9cf31` "to state the
principle as `CLAUDE.md` does". Found: `overview.md:5` no longer holds `no
gate is built to catch it`, and it states the scope and the gap clause in
its own words. It says "a change routed `no work item`" where `CLAUDE.md`
says "a change that would be routed `no work item`", and it leaves out
"the routing check among them". That is no finding. `overview.md` is the
implementer's account; no release note carries it, and settle removes it
with the work item. A change actually routed `no work item` is one of the
changes `CLAUDE.md` names, so the words do not widen the principle, and the
principle's one source stays `CLAUDE.md`.

confirms: none
The class of round 2's finding 2 was enumerated over the tree (contract
rule 12). `git grep -n -E 'kind of gate which|only the shell makes|no (such
)?gate is built'` finds, outside the round records that quote the old
words, the work item's title in `spec.md:1`, `plan.md:1` and
`questions.md:1`, then `spec.md:4` and `routing.md:17` (executed). The
titles are the issue's name. `spec.md:4-11` reports the owner's principle as
#1027's review set it, with its qualifier `with no Write, Edit or
NotebookEdit before it`, and *Scope* item 1 then gives the text `CLAUDE.md`
holds, with round 1's reasons for the narrowing. `routing.md:17` is the
routing record's reason, dated before the first edit, a record of that
moment like `phases/phase-1.md`, which round 2 held is not rewritten.
Neither tells the reader of a release note what the work ships, which was
the finding's ground, and the fix range does not touch either line. So
neither is raised.

confirms: none
The fix pass kept to its two lines per finding. `git diff
d7da1203..8a66584e -- seal/specs/1792973486-a-change-only-the-shell-makes-is-a-chore/rounds/round-2.md`
changes the `verdict:` and `answer:` lines of findings 1 and 2 and nothing
else (executed). The fix range touches `CLAUDE.md`, `spec.md`,
`changelog.md`, `overview.md` and `round-2.md`, and no other file
(executed).

confirms: none
The modules that read `CLAUDE.md` and the fragment pass: `bin/test` over the
five `S5` modules, `tests/test_docs_line_wrap.py`,
`tests/test_the_changelog_is_gathered_at_release.py`,
`tests/test_gather_changelog.py` and `tests/test_release_hygiene.py` gave
243 passed at exit 0. `bin/rules --check` exited 0, with all 249 check lines
in 62 rule files holding. Both were executed in the clone, and both are
probes, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head, labelled `unverified` in `overview.md` *Not verified*; that label is honest, since no party ran them | `8a66584e` | the orchestrator, through `broad-gate` once the rounds settle |
| The removal of the session memory file that held the principle, which lies outside the repository; it still stands, as it should before the merge | outside the repository | the orchestrator, after the merge, as `spec.md` *Scope* item 4 says |

## Probes

| Command | Result |
|---|---|
| `git diff --stat d7da1203..8a66584e` | `CLAUDE.md`, `spec.md`, `changelog.md`, `overview.md` and `round-2.md` changed, nothing else |
| `git diff --stat d7da1203..8a66584e -- hooks .github` | empty |
| `git diff --word-diff 61a8455a..HEAD -- CLAUDE.md` | six `{+ +}` runs, no `[- -]` run |
| `python3 -I -c` comparing the whitespace-collapsed quote of `spec.md:34-38` with `CLAUDE.md` and with the fragment, and testing `which only` and `only the shell makes` | quote in `CLAUDE.md` and after the anchor: `True True`; second sentence in the fragment: `True`; `which only` in `CLAUDE.md`: `False`; `only the shell makes` in `CLAUDE.md`, fragment and overview: `[False, False, False]` |
| round 2 finding 2's `evidence:` command, as written there | `[False, False]` |
| `git grep -n 'only such a change passes through' -- ':!seal/specs/'` | `CLAUDE.md:21` alone |
| `awk 'NR>=16 && NR<=36 {print NR, length($0)}' CLAUDE.md` | widest line 77 columns; line 22 is 42 |
| `git grep -n -E 'kind of gate which\|only the shell makes\|no (such )?gate is built'` | outside the round records: three titles, `spec.md:4` and `routing.md:17` |
| `bin/settle --released-at HEAD`, without `--apply` | exit 0; this work item held by the open `Not verified` row of `overview.md`; nothing written |
| `bin/test` over the five `S5` modules, `tests/test_docs_line_wrap.py`, `tests/test_the_changelog_is_gathered_at_release.py`, `tests/test_gather_changelog.py` and `tests/test_release_hygiene.py`, `-q` | 243 passed, exit 0 |
| `bin/rules --check` | exit 0 |
